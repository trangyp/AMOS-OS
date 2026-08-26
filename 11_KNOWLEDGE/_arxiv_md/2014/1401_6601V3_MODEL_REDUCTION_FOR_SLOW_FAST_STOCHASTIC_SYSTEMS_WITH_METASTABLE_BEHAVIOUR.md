---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1401.6601v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1401.6601v3_Model_reduction_for_slow-fast_stochastic_systems_with_metastable_behaviour

> Source: 1401.6601v3_Model_reduction_for_slow-fast_stochastic_systems_with_metastable_behaviour.pdf

> Pages: 23

---


## Page 1


arXiv:1401.6601v3  [physics.chem-ph]  22 Apr 2014
Model reduction for slow–fast stochastic systems with metastable behaviour
Maria Bruna,1, 2, a) S. Jonathan Chapman,1 and Matthew J. Smith2
1)Mathematical Institute, University of Oxford, Oxford, OX2 6GG, U.K.
2)Computational Science Laboratory, Microsoft Research, Cambridge, CB1 2FB,
U.K.
(Dated: 4 April 2018)
The quasi-steady-state approximation (or stochastic averaging principle) is a useful tool in the study of mul-
tiscale stochastic systems, giving a practical method by which to reduce the number of degrees of freedom in
a model. The method is extended here to slow–fast systems in which the fast variables exhibit metastable
behaviour. The key parameter that determines the form of the reduced model is the ratio of the timescale
for the switching of the fast variables between metastable states to the timescale for the evolution of the slow
variables. The method is illustrated with two examples: one from biochemistry (a fast-species-mediated chem-
ical switch coupled to a slower-varying species), and one from ecology (a predator–prey system). Numerical
simulations of each model reduction are compared with those of the full system.
I.
INTRODUCTION
Understanding the impact of noise on nonlinear dy-
namical systems has been an active ﬁeld of research for
many years, with a wide range of applications in physics,
chemistry, biology, ecology and earth science. Although
the addition of noise sometimes does not change the
qualitative dynamics and can be modelled by adding a
stochastic perturbation to the deterministic solution tra-
jectory (as in the linear noise approximation1), there is a
growing number of applications in which noise has been
shown to be crucial to explain features which cannot be
captured by deterministic models. For example, in deter-
ministic systems with multiple stable steady states the
addition of even a small amount of noise causes these
states to become metastable, with the stochastic sys-
tem undergoing random transitions between the deter-
ministic steady states.
Examples include genetic reg-
ulatory networks,2 lactose utilisation networks and the
bet-hedging in bacteria.3,4 This behaviour cannot be cap-
tured by the deterministic model,5 but can be explained
successfully with a stochastic model.6
A common feature of many complex dynamical sys-
tems is the presence of processes evolving on widely sep-
arated timescales. This can present a challenge for nu-
merical simulation. Often we are only interested in the
behaviour of solutions on a long timescale,7 but in princi-
ple to determine this we need to resolve processes occur-
ring on the fastest timescale. Metastability complicates
this further, since the switching rate between states in-
troduces a new implicit timescale to the process.
For
example, several ecological systems are believed to be
able to switch between alternative states, such as be-
tween tree and grass-dominated vegetation.8,9 A few key
mechanisms may be suﬃcient to explain the observed
bi-stability of these systems, but a wide range of other
ecosystem components (such as the resident bird com-
munity) respond to these dynamics, and may do so at
a)Electronic mail: bruna@maths.ox.ac.uk
diﬀerent rates; for example the population size of a resi-
dent bird community may respond relatively quickly to a
sudden switch in the dominant vegetation type, but the
carbon content of the soil may respond relatively slowly.
This raises questions about how to eﬃciently and accu-
rately simulate the dynamics of such systems: can the
evolution of the slowly evolving components be predicted
without simulating the full evolution of all the fast com-
ponents?
In this paper we bring together these two features,
multiple timescales and metastability, and consider noisy
systems with slow and fast metastable components. We
develop a method to remove the fast degrees of freedom
while retaining the metastable behaviour in the resulting
mathematical description of the slow processes.
Most of the work done to remove fast degrees of free-
dom from stochastic multiscale systems is based on ex-
tending the principle of slow or centre manifold theory
of deterministic dynamical systems. This assumes that
the phase space can be decomposed into fast variables
x which relax very quickly and slow variables y, which
change more slowly:
ǫdx
dt = F(x, y),
x(0) = x0,
(1a)
dy
dt = G(x, y),
y(0) = y0,
(1b)
where ǫ ≪1 quantiﬁes the separation of timescales.
The standard singular perturbation theory, based on
Fenichel’s theory,10 consists of taking the limit ǫ →0 and
assuming that the fast variables x have equilibrated onto
the centre manifold, F(x, y) = 0. The ﬂow on this slow
manifold (with reduced dimensionality) is then given by
dy
dt = G(h(y), y),
y(0) = y0,
(2)
where F(h(y), y) = 0.11 Note that the projection onto
the slow manifold is valid even if F(x, y) = 0 has more
than one solution for y ﬁxed; given the initial condition
x0, the fast system evolves deterministically to one of the
steady states as determined by F(x, y). However, this is


## Page 2


2
0
20
40
60
80
100
0
100
200
300
400
500
600
 
 
num. particles
time t
X
Y
(a)
0
100
200
300
400
500
600
0
0.002
0.004
0.006
0.008
0.01
 
 
num. particles
stationary density
X
(b)
Eq. (13)
FIG. 1. (a) Single realisation of (6) obtained using the exact NRM SSA with X(0) = 400 and Y (0) = 200. (b) Comparison
of the stationary distribution ρ(x) given by (13) (solid dark blue line) and the histogram of X from SSA of (6) (107 samples
used, light blue area). We use τy = 25 and the parameter values (7).
no longer true when we introduce noise in the system:
noise can make x(t) ﬂuctuate between several states sat-
isfying F(x, y) = 0 and (2) does no longer capture the
dynamics of y(t). Developing a good approximation for
the dynamics of system (1) in the presence of multiple
stable states and noise is the key problem that we ad-
dress here.
There exists a variety of approximation methods to
generalise this model reduction to stochastic systems.
The theoretical foundation of these can be traced back
to the stochastic centre manifold theory developed in
Ref. 12. A good introduction to the existing techniques,
classiﬁed according to the stochastic system representa-
tion, can be found in Ref. 13.
Consider the following
stochastic counterpart of (1):
dX = 1
ǫ F(X, Y )dt + 1
√ǫσ(X, Y )dWX(t), X(0) = X0,
(3a)
dY = G(X, Y )dt + Σ(X, Y )dWY (t),
Y (0) = Y0, (3b)
where WX(t) and WY (t) are independent standard Brow-
nian motions. Even though the presence of noise makes
rigorous analysis more complicated, the idea is concep-
tually very simple: one assumes that, “freezing” the slow
variables at Y (t) = ˆy, the fast process X(t) reaches a
unique stationary density ρˆy(x) (or rather a quasi-steady
density), which is the analogue of the unique steady-state
in the deterministic system. The slow stochastic system
analogous to (2) is then obtained by averaging in the fast
variables over this density:
dY = G(Y )dt + Σ(Y )dWY (t),
(4)
where
G(Y ) =
Z
G(x, Y )ρˆy(x) dx,
Σ(Y ) =
Z
Σ(x, Y )ρˆy(x) dx,
(5)
a process known as stochastic averaging.14 This process
is sometimes referred to as the quasi-steady-state (QSS)
reduction.15 The changes in Y (t) may push X(t) away
from its previous quasi-steady density, but by assumption
fast transients in X(t) die out quickly and a new quasi-
steady density ρˆy(x) applies. Numerical schemes based
on the QSS are analysed in Ref. 7 and implementations
of those can be found in Ref. 16 and 17.
The underlying assumption of the above method is
that X(t) is well approximated by a random variable cho-
sen from its steady-state distribution ρˆy(x), conditioned
on a ﬁxed value of Y (t) = ˆy.18 However, this might not be
true if the fast degrees of freedom exhibit metastability.
Our goal in this paper is to extend the model reduction
of slow–fast stochastic systems to scenarios in which the
fast variables do not have a single invariant measure over
the timescales of interest, but switch randomly between
a number of invariant measures.
Consider the stochastic metastable process for a sin-
gle variable X(t). The standard example of metastable
behaviour is Brownian motion with a double well poten-
tial [resulting in a stationary density similar to the one
shown in Fig. 1(b)]. On short timescales the particle is
most likely found near one of the two potential minima,
but on long timescales the particle can transition over the
energy barrier that separates the two wells. This prob-
lem itself can be thought of a slow–fast system, where the
ﬂuctuations of x(t) within a well is the fast process, and
the metastable transitions between wells play the role of
a (discrete) slow process, since they typically occur on a
timescale τs ≫ǫ.
The aim of model reduction techniques for metastable
processes is to eliminate the fast degrees of freedom while
retaining the slow metastable transitions.
The exten-
sion of the QSS to metastability is known as quasi-
stationary analysis (QSA) and is based on WKB pro-
jection methods.19 The main feature of model reduc-
tion in this context is that, instead of averaging over
a global quasi-stationary density ρ(x) (as in the QSS,
which would average over all the metastable basins), it is
assumed that X(t) relaxes in one basin of attraction Bj


## Page 3


3
and is well-approximated by a stationary random pro-
cess chosen from the quasi-stationary density ρj(x) re-
stricted on basin Bj. Then the reduced low-dimensional
model consists of a discrete jump process between states
j, where the switching rates are calculated from the tran-
sition rates of the original process X(t).18,20,21 In higher-
dimensional systems where analytical approximations are
not possible, computational techniques can be applied to
determine the state space of the metastable variables and
to sample the transition probabilities. A recent survey of
such techniques applied to the simulation of rare events
in molecular dynamics (such as conformation changes)
can be found in Ref. 22.
Now suppose X is coupled to an additional slow vari-
able Y . For ease of exposition we focus on the simpler
case in which the dynamics of X are independent of Y .
As we will discuss in section V, the extension to the more
general case is conceptually straightforward. We see that
three timescales are required to characterise such a sys-
tem: the timescale of the fast variables ǫ, the timescale
of the switches of the fast variables τs ≫ǫ, and the
timescale of the slow variables τy ≫ǫ.
We are inter-
ested in approximating the system on the slowest of these
timescales.
We will examine how the reduced model changes with
the relative size of τs and τy. If τy ≪τs, the reduced
model is simply a discrete jump process.20 If τy ≫τs,
the slow variables evolve on a timescale which is even
slower than the switches in x and the classical QSS ap-
proximation applies. In the intermediate regime in which
τy = O(τs) things become more interesting, as the evolu-
tion of y critically depends on the metastable behaviour
of x. This is the main contribution of the present work.
The rest of this paper is organised as follows. In Sec.
II we introduce a model chemical system with which we
will illustrate the model reduction method. In section III
we describe the idea behind our analysis and show how
to obtain a reduced model in the slow timescale when the
fast process is monostable, and how this changes when
there is metastability. We introduce the three character-
istic timescales in our slow–fast model system with bista-
bility, from which we deﬁne three regimes depending on
their relative sizes.
We present the three correspond-
ing reduced models and show numerical comparisons be-
tween these reduced slow-scale stochastic models and the
full slow–fast process using a stochastic simulation algo-
rithm (SSA). In section IV we apply the method to a
simple predator–prey model with bistable prey and use
it to estimate the mean extinction time of the predator.
More background on why we choose this particular case
study will be given in the beginning of that section. In
the concluding section V we brieﬂy discuss the results in
the context of current directions of research in theoreti-
cal ecology and stochastic nonlinear dynamics. The jus-
tiﬁcation of the reduced models through a perturbation
analysis of the corresponding Fokker–Planck equations is
presented in appendix A.
II.
MODEL PROBLEM
We introduce the following model as an example of
a slow–fast system with bistability. A system with two
chemical species X and Y changes according to the re-
actions
∅
k1/ǫ
−−−⇀
↽−−−
k2/ǫ X,
2X
k3/ǫ
−−−⇀
↽−−−
k4/ǫ 3X,
(6a)
∅
k5(X)/τy
−−−−−−⇀
↽−−−−−−
k6/τy
Y
(6b)
Note that the evolution of the chemical X is self-
determining, while the production of chemical Y depends
on the amount of X present in the system through the
function k5(x). We suppose the system is in a well-mixed
reactor of unit volume. We have chosen to write the reac-
tion rates for X(t) in terms of ﬁxed k1 to k4 and a small
parameter ǫ; by varying ǫ we can change the timescale
for the evolution of X without changing the equilibrium
distribution. Similarly, we have chosen to write the reac-
tion rates for Y (t) in terms of ﬁxed k5(x) and k6 and a
parameter τy.
The set of four reactions (6a) governing X(t) is known
as the Schl¨ogl model.23 This model has two favourable
states (or basins of attraction) for some parameter val-
ues, and the stochastic system displays bistable switching
between these states even for parameter values for which
the deterministic model is monostable.24
The stochastic model of the six chemical reactions (6)
introduces the propensity functions
α1(x) = k1/ǫ,
α2(x) = k2x/ǫ,
α3(x) = k3x(x −1)/ǫ,
α4(x) = k4x(x −1)(x −2)/ǫ,
α5(x) = k5(x)/τy,
α6(y) = k6y/τy,
which are such that the probability of reaction i hap-
pening in time dt is αidt.25 The system may then be
simulated by using a stochastic simulation algorithm
(SSA) such as the exact Gillespie’s Direct Method.26 Here
we use the equivalent exact and eﬃcient Next Reaction
Method (NRM).27
The timescale for the evolution of X is set by the decay
rate k2/ǫ. Similarly the timescale for the evolution of Y
is set by the decay rate k6/τy.
Thus if ǫ and τy are
to represent these timescales we should choose k2 and
k6 to be of order unity. The other rates determine the
equilibrium values of X and Y . If we suppose a typical
equilibrium value of X is O(δ−1), this corresponds to
k1 = O(δ−1), k3 = O(δ), k4 = O(δ2). In Fig. 1(a) we plot
one realisation of the SSA of (6) obtained for X(0) = 400,
Y (0) = 200, τy = 25, and
k1 = 0.6 δ−1,
k2 = 1,
k3 = 0.48 δ,
k4 = 0.0666 δ2,
k5(x) = 0.833 x,
k6 = 1,
ǫ = 0.025,
δ = 0.01.
(7)
The parameters values are chosen such that system (6)
is bistable in X(t) (as in Ref. 24) and Y (t) evolves in


## Page 4


4
the same timescale as switches in X.
The rate k5(x)
(which we will also use in the simulations that follow)
is such that the production reaction for Y can be writ-
ten as X −→X + Y with rate 0.833/τy. We also plot
the stationary distribution of X, obtained by a long time
simulation of the SSA with ﬁnal time t = 106 and record-
ing the value of X every ∆t = 0.1 in Fig. 1(b). We see
that for these parameter values the system (6) has two
favourable states for X. We see that X(t) spends quite
a long time ﬂuctuating around one of these states be-
fore switching to the other. In section A 2 we will derive
an analytical approximation of the mean switching times
between states and ﬁnd that is exponentially large in the
parameter δ. We want to understand how the oscillation
between these two states inﬂuences the dynamics of Y ,
and obtain an eﬃcient and accurate way to take this ef-
fect into account without having to simulate the full X
dynamics.
A.
Continuous approximation: the chemical Langevin and
the Fokker–Planck equations
For ease of exposition we will apply our model reduc-
tion techniques not to (6) directly, but to the continu-
ous approximation of this system given by the chemical
Langevin equation. This approximation is similar to the
numerical method of τ-leaping.28 The idea of the approxi-
mation is that for large X and Y the propensity functions
do not change signiﬁcantly after each individual reaction
event, which enables us to jump forward many reaction
events without updating the propensities. The change in
the number of molecules between timesteps is then Pois-
son distributed. If we now take a limit in which many
reactions are considered between timesteps, but still with
a small relative change in the number of molecules, X and
Y may be approximated by continuous random variables
and the change in molecular numbers between timesteps
is approximately normally distributed (see Refs. 24 and
29 for more details of this approximation). In that case
we arrive at the chemical Langevin equations
dX = v(X)
ǫ
dt +
r
2d(X)
ǫ
dWX(t),
(8a)
dY = V (X, Y )
τy
dt +
s
2D(X, Y )
τy
dWY (t),
(8b)
which are of the same form as the slow–fast system of
stochastic diﬀerential equations (3).
The drift coeﬃ-
cients v(x), V (x, y) and the diﬀusion coeﬃcients d(x) and
D(x, y) are given by
v(x) = k1 −k2x + k3x(x −1) −k4x(x −1)(x −2),
d(x) = 1
2[k1 + k2x + k3x(x−1) + k4x(x −1)(x −2)] ,
V (x, y) = k5(x) −k6y,
D(x, y) = 1
2[k5(x) + k6y].
(9)
Let P(x, y, t)dxdy be the probability that X(t) ∈[x, x +
dx) and Y (t) ∈[y, y + dy) at time t. Then the chemical
Fokker–Planck (FP) equation for the joint probability
distribution function corresponding to (8) is given by
∂P
∂t (x, y, t) =1
ǫ
∂
∂x
 ∂
∂x[d(x)P] −v(x)P

+ 1
τy
∂
∂y
 ∂
∂y [D(x, y)P] −V (x, y)P

.
(10)
This equation is complemented with no-ﬂux boundary
conditions on [0, ∞)2 since the probability P must remain
normalised for all times.
The stationary distributions of X and Y , ρ(x) and q(y)
respectively, correspond to taking the limit t →∞in the
marginal probability densities
ρ(x) = lim
t→∞
Z
P(x, y, t) dy,
q(y) = lim
t→∞
Z
P(x, y, t) dx.
(11)
Since the dynamics of X do not depend on Y , it is
straightforward to solve for ρ(x) by integrating (10) with
respect to y to give
∂
∂x
 ∂
∂x[d(x)ρ] −v(x)ρ

= 0,
(12)
where we have used no-ﬂux boundary conditions at y = 0
and y = ∞. Thus the stationary distribution of X is
given by
ρ(x) =
A
d(x) exp
Z x
0
v(s)
d(s)ds

,
(13)
where A is the normalisation constant. The solution (13)
is plotted in Fig. 1(b) as a blue solid line. As expected,
the results compare well with the results obtained by the
long time stochastic simulations.
III.
REDUCED SLOW-SCALE MODELS VIA
STOCHASTIC AVERAGING
In this section we show how the stochastic model (6)
may be reduced when ǫ is small, and how the reduced
model depends on the size of τy relative to the size of τs.
A.
The case when X(t) is monostable
To give some context to the reduced models which
follow, we ﬁrst consider the simpler case in which the
fast species X is monostable. In Fig. 2(a) we present a
stochastic simulation of (6) with X(0) = Y (0) = 0 for
δ = 0.01, ǫ = 0.025, τy = 25, k1 = 0.8δ−1, and k2 to
k6 as in (7). In contrast to Fig. 1, we see that for this
value of k1 the stochastic model ﬂuctuates about a single
value. This is demonstrated in Fig. 2(b), where we plot


## Page 5


5
0
50
100
150
200
250
300
350
400
0
100
200
300
400
500
600
 
 
num. particles
time t
X
Y
(a)
æ
300
400
500
600
0.000
0.002
0.004
0.006
0.008
0.010
x
ρ(x)
(b)
FIG. 2. (a) Single realisation of (6) obtained using the exact NRM SSA. (b) Marginal stationary distribution ρ(x) given by
(13) with the stable point x0 marked with the red circle. We use τy = 25, X(0) = Y (0) = 0, and the parameter values (7)
except that k1 = 0.8δ−1.
the stationary distribution ρ(x) using (13). The maxi-
mum of the stationary distribution is x0 ≈437.8, which
satisﬁes v(x0) −d′(x0) = 0.
In this case, since the relaxation time of X to its equi-
librium density is much faster than the decay time of the
slow reaction, the slow chemical reactions (6b) can be
well-approximated by16,17
∅
k5/τy
−−−−⇀
↽−−−−
k6/τy
Y
(14)
where k5 is the average production rate, given by
k5 =
Z ∞
0
k5(x)ρ(x) dx.
(15)
For our particular example in which k5(x) = k5x, the
eﬀective production rate is simply k5 = k5X.
The analogous quasi-steady-state reduction in the
chemical Langevin equation (8b) is
dY = V (Y )
τy
dt +
s
2D(Y )
τy
dWY (t),
where
V (y) =
Z
V (x, y)ρ(x) dx,
D(y) =
Z
D(x, y)ρ(x) dx.
like in the stochastic averaged model (4) and (5) de-
scribed in Sec. I.
B.
The case when X(t) is bistable
Let us now consider the case when X(t) is bistable,
that is, it switches between two favourable states as
shown in Fig. 1. Figure 3(a) shows an illustrative tra-
jectory of the system (6) for X(0) = Y (0) = 0, with
parameter values given by (7).
Figure 3(b) shows the
stationary density ρ(x) computed using (13).
We de-
note the two peaks of this density by x± and the relative
minimum (or unstable node) as x∗. Now it is not clear
whether it is appropriate to use the standard stochastic
averaging technique, since the assumption that X(t) con-
verges quickly to a stationary process with measure ρ(x)
0
50
100
150
200
250
300
350
400
0
100
200
300
400
500
600
 
 
num. particles
time t
X
Y
(a)
æ
æ
æ
100
200
300
400
500
600
0.000
0.002
0.004
0.006
0.008
x
ρ(x)
(b)
FIG. 3. (a) Single realisation of (6) obtained using the exact
NRM SSA. (b) Marginal stationary distribution ρ(x) given by
(13) with the two stable ﬁxed points x± and unstable ﬁxed
point x∗marked with red circles. We use τy = 25, X(0) =
Y (0) = 0, and the parameter values (7).


## Page 6


6
0
100
200
300
400
500
0
100
200
300
400
500
600
 
 
time t
num. particles
Regime 1
(a)
0
100
200
300
400
500
0
100
200
300
400
500
600
 
 
time t
num. particles
Regime 2
(b)
0
100
200
300
400
500
0
100
200
300
400
500
600
 
 
time t
num. particles
Regime 3
(c)
FIG. 4. Evolution of X(t) (blue lines) and Y (t) (green lines) from a single realisation of (6) obtained using the exact SSA.
We use the parameter values (7), X(0) = Y (0) = 200, and vary τy to change between regimes. (a) Regime 1: τy = 2500. (b)
Regime 2: τy = 25. (c) Regime 3: τy = 0.25.
is challenged by the metastable behaviour of X(t).
To obtain a reduced slow system now we ﬁrst need to
characterise this metastable behaviour. In particular, we
see that a third timescale τs emerges in the problem as
the characteristic time for switches of the fast variable
X(t) between the two favourable states. Typically this
timescale is much longer than the relaxation timescale
for X(t) within each well (indeed, this is the deﬁnition of
metastability used here).
Thus we have the following scenario.
On a short
timescale X(t) relaxes to a quasi-stationary distribution
centred around one of x−or x+. On the longer timescale
of τs the system switches from one of these distributions
to the other, as X(t) makes the transition between wells.
The nature of the reduced mode depends crucially on
the relative sizes of the switching timescale τs and the
timescale for the slow process τy. We will see that there
are three parameter regimes, corresponding to τs ≪τy,
τs ∼τy and τs ≫τy, respectively. Illustrative simula-
tions of each of these regimes are shown in Fig. 4. In
Subsections III C–III E we present the reduced stochas-
tic model appropriate for each regime, together stochas-
tic simulations comparing the reduced model to the full
system. The mathematical justiﬁcation for the reduced
models is given in appendix A.
C.
Regime 1: ǫ ≪τs ≪τy
A sample trajectory in this regime is shown in Fig-
ure 4(a). In this case, X has time to fully equilibrate
on the timescale of the evolution of Y . Thus the stan-
dard stochastic averaging can be used, and the eﬀective
production rate of Y can be computed as if X was monos-
table as
∅
k5/τy
−−−−⇀
↽−−−−
k6/τy
Y ,
k5 =
Z ∞
0
k5(x)ρ(x) dx.
(16)
We call (16) reduced model 1 or RM1. A derivation of
this model using the associated Fokker–Planck equation
is given in A 1.
In Figures 5 and 6 we compare simulation results (us-
ing the NRM SSA) of the full system (6) and the re-
duced system RM1. We use a long timescale for Y (t),
τy = 2500, so that the system is in Regime 1. The sta-
tionary marginal density q(y) (histograms obtained by a
long time simulation of both models) is plotted in Fig. 5.
Clearly, the reduced model provides a very good approx-
imation to the histogram coming from the full-system
simulation. The beneﬁt of eliminating the fast variable
is illustrated by the fact that the RM1 histogram took
only 0.8 seconds to compute while the full system his-
togram required over 14 hours of computing time (using
a standard desktop computer). In Fig. 6 we compare the
time-dependent behaviour of the exact full model and
RM1, plotting the mean and standard deviation of Y (t),
µY and σY respectively. We initialise the system with
X(0) ∼ρ(x) and Y (0) = 0. While the mean obtained
0
50
100
150
200
250
300
350
400
0
0.005
0.01
0.015
0.02
0.025
0.03
 
 
y
q(y)
Full
RM1
FIG. 5. Comparison of the marginal stationary density q(y)
in regime 1: full system (6) (solid black line) and approxi-
mate reduced model 1 (16) (dash red line). Both histograms
are computed by running the NRM algorithm up to t = 107
taking recordings every ∆t = 5 (2 × 106 samples). We use
τy = 2500 and the parameter values (7).


## Page 7


7
from the RM1 approximation is indistinguishable from
that of the full system, the standard deviation is slightly
underestimated by RM1. We note that the error in σY
in Fig. 6(b) is in fact quite small relative to the mean
µY (0.65%), and this is why this diﬀerence is only just
recognisable in Fig. 5.
0
5000
10000
15000
0
50
100
150
200
250
 
 
(a)
time t
µY
0
5000
10000
15000
0
2
4
6
8
10
12
14
16
 
 
(b)
time t
Full
RM1
σY
FIG. 6. Comparison of the time-dependent (a) mean µY (t)
and (b) standard deviation σY (t): full system (6) (solid black
line) and approximate reduced model 1 (16) (dash red line).
Black and red curves are computed as the average over 1.1 ×
104 and 105 realisations respectively with initial conditions
Y (0) = 0 and X(0) ∼ρ(x) (for (6) only). We use τy = 2500
and the parameter values in (7).
D.
Regime 2: ǫ ≪τs ∼τy
When the timescale for the evolution of species Y is of
the same order as that of the switches in X(t), it is im-
portant to keep the bistable nature of the system in the
reduced model, since Y responds diﬀerently depending
on which well X is in. Fig. 4(b) shows an example of the
system in this regime. As in the one-dimensional exam-
ple described in Sec. I, using a QSA the bistability can be
kept in by introducing a discrete two state stochastic pro-
cess S(t) governing the jumps of X(t): S(t) = S−when
X(t) is in the left well Ω−= [0, x∗) and S(t) = S+ when
X(t) is in the right well Ω+ = (x∗, ∞). Within each well
X quickly reaches a quasi-equilibrium, and therefore we
can use a modiﬁed stochastic averaging conditional on
the value of S. Then the reduced stochastic system is
S−
k−
−−⇀
↽−−
k+
S+,
∅
k5(S)/τy
−−−−−−⇀
↽−−−−−−
k6/τy
Y
(17a)
where the eﬀective production rate takes one of two val-
ues depending on whether X is in the left or right well,
k5(S±) =
Z
Ω±
k5(x)ρ±(x) dx;
(17b)
here ρ± is the normalised stationary density of X con-
ditional on being in the left (minus) or right (plus)
well. This deﬁnition corresponds to imposing a reﬂecting
boundary condition on x∗in (12).30 A formal derivation
of this model is given in A 2. We denote this reduced sys-
tem by reduced model 2 or RM2. The rate constants k±
of the process for S(t) are the inverse of the mean switch-
ing times T± for X to jump from one well to the other
[the switching timescale τs is such that T± ∼O(τs)]. De-
termining these rates accurately is one of the main chal-
lenges of Regime 2; we will return to this issue in section
III F. For the chemical X(t), we will ﬁnd that
k−= 0.0931,
k+ = 0.0835.
(17c)
A comparison of a sample trajectory of the system ob-
tained from a NRM simulation of the full system and of
the reduced system RM2 is shown in Fig. 7. We choose
the timescale of Y (t) such that τy ∼τs and the system is
in Regime 2. In Fig. 7(a), the X(t) and Y (t) populations
simulated from the full model (6) are shown in dark blue
and green solid lines, respectively. The two-valued light
blue curve represents the bistable switching of X(t) and
takes as values the conditional average values
X± =
Z
Ω±
xρ±(x) dx,
(18)
according to when X(t) ∈Ω±. Fig. 7(b) shows one tra-
jectory of the reduced model (17). In RM2, X(t) is not
explicitly simulated, but we can still illustrate an ap-
proximate trajectory using the switch variable S(t): in
the ﬁrst half of Fig. 7(b), we plot X± as speciﬁed by
S(t) = S± as well as the corresponding 95% conﬁdence
interval of ρ±(x) (dash blue lines). In the second half,
to allow for an easier comparison with Fig. 7(a), we plot
instead samples X from ρ±(x) depending on the value of
S(t) (taken every ∆t = 0.1). Using this procedure, we
can make a run of the RM2 look very similar to a full
model run as in Fig. 7(a).
While Fig. 7 indicates that the qualitative behaviour
of the reduced model (17) is similar to that of the full
system, a more quantitative comparison is appropriate.
In Fig. 8 we compare the stationary distributions of Y
(histograms) obtained from a long-time NRM simulation


## Page 8


8
0
100
200
300
400
500
0
100
200
300
400
500
600
time t
num. particles
(a)
0
100
200
300
400
500
0
100
200
300
400
500
600
time t
num. particles
(b)
FIG. 7.
Comparison of one single realisation in Regime 2
of (a) the exact full system (6) and (b) the approximated
reduced model 2 (17) using the NRM algorithm.
We use
τy = 25, X(0) = 0 [i.e.
S(0) = S−in (b)], Y (0) = 200,
and the parameter values (7). In (a), the simulated quanti-
ties X(t) and Y (t) are shown in dark blue and green, respec-
tively. The lighter blue line shows reduced two-valued curve
X± corresponding to the bistable switch [X± if X(t) ∈Ω±,
see (18)].
In (b), the simulated variable Y (t) is shown in
green, and the approximate representation of X(t) from the
simulated S(t) in shown as follows: in the ﬁrst half, X± (ac-
cording to S(t) = S±) and the 95% conﬁdence intervals of
ρ±(x) are plot as solid and dash blue lines, respectively. In
the second half, the solid blue line shows samples taken every
∆t = 0.1 from ρ±(x) as per S(t) = S±.
of the full model (6) and the reduced model 2 (17). To
illustrate the need for a new model reduction in Regime
2, we also plot the histogram obtained by a standard
stochastic averaging using RM1 (16).
The RM2 solu-
tion is in excellent agreement with the full system, while
the RM1 approximation considerably underestimates the
variance of the distribution. In Fig. 9 we show a com-
parison of the mean and standard deviation of Y (t) for
the three models. We initialise the system with Y (0) = 0
and X(0) ∼ρ(x). Note that the latter is not required for
RM1 since X(t) has been eliminated from that model;
in contrast, the initialisation for RM2 is S(0) = S± de-
pending on the well in which the sample from ρ(x) is in
0
100
200
300
400
500
0
0.005
0.01
0.015
0.02
0.025
0.03
 
 
y
q(y)
Full
RM1
RM2
FIG. 8. Comparison of the marginal stationary density q(y)
in regime 2: full system (6) (solid black line) and approximate
reduced models 1 (16) (dash red line) and 2 (17) (dot-dash
blue line).
All three histograms are computed by running
the NRM algorithm up to t = 107 taking recordings every
∆t = 0.5 (2×107 samples). We use τy = 25 and the parameter
values (7).
[namely, S(0) = S−with probability
R
Ω−ρ(x)dx, and S+
otherwise]. We see that while the RM1 (16) captures the
behaviour of the mean of Y fairly well, it signiﬁcantly
underestimates the variance of Y .
E.
Regime 3: ǫ ∼τy ≪τs
Now consider a scenario in which τy ≪τs, as illus-
trated in Fig. 4(c). Species Y is now fast by comparison
to the switches of X between wells. Thus on the slow-
est timescale of τs both X and Y have time to reach a
quasi-equilibrium, conditional on X being in a given well.
In this case, when we eliminate the fast variables we are
left only with the binary switch S(t). Hence the reduced
system in Regime 3 on the τs timescale is simply
S−
k−
−−⇀
↽−−
k+
S+,
(19)
where k± are given in (17c); see A 3 for more details. We
call this the reduced model 3 (RM3). When S(t) = S−
(resp.
S+), the system has a quasi-stationary density
Q−(x, y) [resp. Q+(x, y)], which is the stationary den-
sity conditional on X being in the left (resp. right) well.
To clarify this, in Fig. 10 we plot the joint stationary
density Q(x, y) and the two marginal stationary densi-
ties ρ(x) and q(y) obtained by the long-time exact sim-
ulation of the full system (6) with τy such that the sys-
tem is in Regime 3. This conﬁrms that Y (t) is also bi-
modal in this regime [even though the switches between
its two modes are still controlled by X(t)]. To obtain the
quasi-stationary densities Q±(x, y) [and the correspond-
ing marginals ρ±(x) and q±(y)], we follow a similar pro-


## Page 9


9
0
50
100
150
0
50
100
150
200
250
 
 
(a)
time t
µY
0
50
100
150
0
10
20
30
40
50
60
 
 
Full
RM1
RM2
(b)
time t
σY
FIG. 9. Comparison of the time-dependent (a) mean µY (t)
and (b) standard deviation σY (t): full system (6) (solid black
line) and approximate reduced models 1 (16) (dash red line)
and 2 (17) (dot-dash blue line). Black, red, and blue curves
are computed as the average over 1.1 × 104, 105, and 105
realisations respectively with initial conditions Y (0) = 0 and
X(0) ∼ρ(x). We use τy = 25 and the parameter values in
(7).
ceeding using a long-time simulation of (6) but with a
reﬂecting boundary condition at x∗.
In Fig. 11 we compare a sample trajectory of the full
set of reactions (6) with sample trajectory of the reduced
system (19). We choose τy = 0.25 so that the system is
in Regime 3. Figures 11(a) and (c) show the evolution
of X(t) and Y (t) respectively from (6), together with
the two-valued ﬁltered curves to represent the switches
in X(t) given by
(X(t), Y (t)) =
(
(X−, Y −),
if S(t) = S−, (X(t) < x∗),
(X+, Y +),
if S(t) = S+, (X(t) > x∗),
(20)
where
X± =
Z
Ω±
xQ±(x, y) dxdy,
(21)
and similarly for Y ±. Fig. 11(b) and (d) show one trajec-
tory of the RM3 (19), where the output S(t) is mapped to
X
Y
(a)
log(Q)
0
100
200
300
400
500
600
0
0.002
0.004
0.006
0.008
0.01
0.012
 
 
num. particles
density
ρ(x)
q(y)
(b)
FIG. 10. (a) Logarithm of the joint stationary density Q(x, y)
and (b) marginal stationary densities ρ(x) and q(y) measured
from a long simulation (up to t = 106 taking recordings every
∆t = 0.1) of the full system (6) (blue and green histograms,
respectively). We use τy = 0.25 and the parameters values
(7).
X(t) and Y (t) units using the quasi-stationary densities
ρ±(x) and q±(y) [similarly to what we did in Fig. 7(b)].
In the ﬁrst half of Figs. 11(b,d) we plot (X(t), Y (t)) (20)
(solid lines) and the 95% conﬁdence intervals (dashed
lines) of ρ±(x) and q±(y). In the second half, instead
of the average quantities we plot sampled values (X, Y )
from Q±(x, y) [depending on the value of S(t)].
This
leads to qualitatively very similar output as with the full
model in the left column of Fig. 11.
In the next two ﬁgures we show a quantitative compar-
ison in Regime 3 between the full system and all three
reduced models. In Fig. 12 we compare the stationary
distribution of Y obtained by long-time simulations of
the four models. We note an excellent agreement between
the histogram from RM3 (solid green line) and that from
the full model (solid black line). But this is not surprising
since to get q(y) with the RM3 we use the quasi-steady
densities q±(y) =
R
Ω± Q±(x, y) dx (obtained in turn from
a full model simulation with a reﬂecting condition at x∗),
and the only output from RM3 is the proportion of time
spend in the left/right wells. The histogram from RM2
(dot-dash blue line) captures the bimodality of Y in this


## Page 10


10
0
100
200
300
400
500
0
200
400
600
0
100
200
300
400
500
0
100
200
300
400
0
100
200
300
400
500
0
200
400
600
0
100
200
300
400
500
0
100
200
300
400
Y
Y
X
X
time t
time t
time t
time t
(a)
(b)
(c)
(d)
FIG. 11. Comparison of one realisation in Regime 3 of (a,c)
the exact full system (6) and (b,d) the approximated reduced
model 3 (19) using the NRM algorithm. We use τy = 0.25,
X(0) = 0 [i.e. S(0) = S−in (b,d)], Y (0) = 200, and the
parameter values (7). In (a,c), the simulated quantities X(t)
and Y (t) are shown in dark blue and light green, respectively.
The two-valued curves in (a,c) are computed from (20). In
(b,c), the approximate representation of (X(t), Y (t)) from the
simulated S(t) in shown as follows: in the ﬁrst half, (20) and
the 95% conﬁdence intervals of ρ±(x) and q±(y) are plot as
solid and dash lines, respectively. In the second half of (b)
and (d), curves show samples of ρ±(x) and q±(y), respectively,
taken every ∆t = 0.1 from as per S(t) = S±.
regime, but it gets the conditional means and variances
substantially wrong. This is because X and Y are vary-
ing in the same timescale whereas RM2 supposes that
X is much faster than Y . If the timescales in Regime 3
satisﬁed ǫ ≪τy ≪τs, we would expect RM2 to give a
good approximation to the full model dynamics.
Fig. 13 shows the mean µY (t) and the standard de-
viation σY (t) of Y obtained from 105 realisations of the
four models.
We initialise the system in the left well
(S(0) = S−), using X(0) ∼ρ−(x) and Y (0) ∼q−(y)
for the models that require explicit X or Y initialisation.
The values of µY (t) and σY (t) corresponding to RM3 can
be calculated from S(t). A simple calculation shows that
they are given by
µY (t) = Y −+
 Y + −Y −

s+(t),
σ2
Y (t) = σ2
Y−+
h
σ2
Y+ −σ2
Y−
i
s+(t)
+

Y + −Y −
2 s+(t)[1 −s+(t)],
(22)
where s+(t) is the estimated probability that S(t) = S+
and σ2
Y± =
R
(y −Y ±)2q±(y)dy. The mean µY of both
RM2 and RM3 captures well the mean of the full model,
while RM1 misses the transient and jumps quickly to its
stationary value (since it is taking X to be equilibrated
instantly at t = 0). Similarly, the global standard devi-
ation σY of the full model is well approximated by RM2
and RM3, while RM1 underestimates (this is to be ex-
0
100
200
300
400
500
0
0.005
0.01
0.015
0.02
0.025
0.03
 
 
y
q(y)
Full
RM1
RM2
RM3
FIG. 12. Comparison of the marginal stationary density q(y)
in regime 3: full system (6) (solid black line) and approxi-
mate reduced models 1 (16) (dash red line), 2 (17) (dot-dash
blue line), and 3 (19) (solid green line). All four histograms
are computed by running the NRM algorithm up to t = 106
taking recordings every ∆t = 0.1 (107 samples).
We use
τy = 0.25 and the parameter values (7).
pected as we have eliminated the noise coming from the
switches of X).
F.
Estimation of mean-switching times
In reducing the fast variable X to a two-state Markov
process in the reduced models 2 and 3 (corresponding to
taking the limit δ →0 as we will see in Appendix A 2),
the key pieces of information we need to extract are the
switching rates k+ and k−. These are the inverses of the
mean transition (or escape) times T+ and T−. In this
section we show how to accurately obtain these rates for
the chemical system.
The
estimation
of
the
mean
escape
times
for
metastable processes is a classical problem that has re-
ceived much attention in the literature.31 As δ →0 the
escape times become exponentially small in δ and may
be estimated by a variety of techniques in exponential
asymptotics.19,20 In some cases the process for X may
be too complicated to estimate the mean escape times
analytically, and a numerical estimate must be used.32
However, when ǫ and δ are small but non-zero even the
deﬁnition of escape becomes an issue: at what stage has
the process X reached the other well?
For our simple bistable X(t) process (8a), the mean
time to reach any given point x1, given we start at
X(0) = x0 is given exactly by24
T−(x0, x1) =
Z x1
x0
Z z
0
ρ(s)
d(z)ρ(z)dsdz,
with
x0 < x1,
T+(x0, x1) =
Z x0
x1
Z ∞
z
ρ(s)
d(z)ρ(z)dsdz,
with
x0 > x1.
(23)


## Page 11


11
0
5
10
15
20
80
100
120
140
160
180
200
220
 
 
(a)
time t
µY
0
5
10
15
20
0
20
40
60
80
100
120
 
 
Full
RM1
RM2
RM3
(b)
time t
σY
FIG. 13. Comparison of the time-dependent (a) mean µY (t)
and (b) standard deviation σY (t): full system (6) (solid black
line) and approximate reduced models RM1 (16) (dash red
line), RM2 (17) (dot-dash blue line), and RM3 (19) (solid
green line). All curves are computed as the average over 105
realisations with initial conditions X(0) ∼ρ−(x) and Y (0) =
Y −≈95. We use τy = 25 and the parameter values in (7).
The curves for RM3 are computed using (22).
The question is, what values do we choose for x0 and x1?
For x0 we could choose the local maximum of ρ in the
left-hand well (which we denote by x−), or we could sam-
ple from the stationary distribution conditional on being
in the left-hand well (which we denote by ρ−).
Since
in the limit ǫ ≪τs equilibration within a well is rapid
by comparison to transitions between wells, we could in
principle start with any value of x0 in the left-hand well
and we would obtain the same transition time to leading
order.
For x1 we could use x∗, the minimum of ρ, which sat-
isﬁes
d′(x∗) −v(x∗) = 0.
We then need to double the mean ﬁrst passage time to
ﬁnd the mean escape time, since a particle at x∗will
return to the well it came from with probability one half.
Alternatively, since equilibration within a well is rapid by
comparison to transitions between wells, we may choose
any x1 which is suﬃciently far from x∗so that immediate
return to the left-hand well is unlikely. For example, we
could choose the mean (x∗+x+)/2, where x+ is the local
maximum of ρ in the right-hand well.24
In Table I we present values of T± [using (23)] and the
corresponding results obtained by the SSA (with relative
standard error of less than 1%, achieved with roughly 104
exits) for several choices of x0 and x1. We see that there
is a small but signiﬁcant variation in the switching times
despite the fact that ǫ is quite small. To decide which of
these times to use we consider here what properties we
require of the reduced system (17a). If we denote s±(t)
as the probability that S(t) = S± then s+(t) satisﬁes
ds+
dt = k−−(k−+ k+)s+,
(24)
where we have used the relation s−+s+ = 1 to eliminate
s−. If we initialise X in the left-hand well [by sampling
from ρ−(x)] then s+(0) = 0, giving
s+(t) =
k−
k−+ k+

1 −e−(k−+k+)t
.
(25)
The stationary value s+ =
k−
k−+k+ = 1 −θ, represents
the proportion of time that X spends in the right-hand
well on average. For S to be a good approximation to
X this should be equal to the integral of ρ(x) over the
right-hand well. This gives us one relationship between
k+ and k−, which determines the ratio between the mean
switching times T±. It can be shown that choosing k+
and k−which satisfy this constraint will ensure that the
reduced process accurately captures the mean behaviour
of Y .
To accurately capture the variance in Y we need to
capture the rate of approach to this stationary solution
accurately, i.e. we need to determine the time constant
ψ = 1/(k−+k+). We can avoid the diﬃculty of determin-
ing when a switch in X has occurred by considering the
time dependent mean of both X and the reduced process
S. If we can match the decay rates of these means, then
we will have determined the rate constant ψ accurately.
The mean of X under the reduced model is given by
X(t) = θX−+(1−θ)X+−(1−θ)(X+−X−)e−t/ψ, (26)
where X± =
R
Ω± xρ±(x) dx are the mean values of X re-
stricted to the right and left well respectively. The equi-
librium value is X∞= θX−+ (1 −θ)X+. By comparing
(26) to an ensemble of short-time stochastic simulations
of the full process X(t) we are able to get a good estimate
ψ, which is then enough to determine k−and k+.
In Figure 14(a) we show the computed time evolution
of X, the mean of the full X process (obtained as the
average of 105 runs). If from this we subtract the large
time behaviour X∞and then take a logarithm we should
obtain a straight line with gradient −1/ψ, as shown in
Fig. 14(b). We ﬁt a straight line to the part of the curve
in which X −X∞lies between 80% and 40% of its initial


## Page 12


12
TABLE I. Mean exit times T−and T+ to leave the left and right wells, respectively, as derived from numerical simulations and
theory. We compare the results obtained using diﬀerent start and end points.
T−(left →right)
T+ (right →left)
x0
x1
Eq. (23)
SSA
x0
x1
Eq. (23)
SSA
ρ−(x0)
(x∗+ x+)/2
11.1190
11.1275
ρ+(x0)
(x−+ x∗)/2
11.5366
11.5573
x−
(x∗+ x+)/2
11.4443
11.4610
x+
(x−+ x∗)/2
11.8714
11.9482
0
(x∗+ x+)/2
11.6121
11.3253
1000a
(x−+ x∗)/2
11.9853
12.1354
0
x∗
b
13.7263
13.7463
1000a
x∗
b
11.2982
11.5974
a The starting point for the right to left transitions, which in theory should be x = ∞, is placed at x = 1000, where ρ+(1000) ∼10−59.
The relative error in the theoretical values using ∞or 1000 are O(10−4).
b The values T± using x1 = x∗are multiplied by two (both in the theory and SSA) since there is, roughly speaking, a 50% chance to fall
either side once X(t) reaches the unstable point x∗.
0
1
2
3
4
5
6
100
120
140
160
180
200
220
240
260
 
 
(a)
time t
X
0
1
2
3
4
5
6
−1.2
−1
−0.8
−0.6
−0.4
−0.2
0
0.2 (b)
time t
log((X(t) −X∞)/b)
FIG. 14. Estimation of ψ from (26). (a) Time-evolution of the
mean X(t) with X(0) = X−(solid blue line). The stationary
value X∞is shown as a dash red line. The curve has been
obtained from 105 SSA realisations of the full model (6). (b)
Transformation log((X −X∞)/b) with b = (θ −1)(X+ −X−)
using X(t) in (a). The parameter ψ is estimated from the
slope of this curve, using (26). The black dashed line shows
the section we use for the linear ﬁt (shown in as a dot-dashed
red line).
value, in order to avoid any initial transients. The ﬁt is
good, and leads to the following values for θ, ψ and T±:
θ = 0.4729,
ψ = 5.6602,
T−= 10.7379,
T+ = 11.9697.
(27)
We see that these are in the same range as those in Ta-
ble I. These are the values of T± that have been used in all
simulations for RM2 and RM3 presented in Subsections
III D and III E.
IV.
CALCULATING EXTINCTION TIMES IN A
PREDATOR–PREY SYSTEM
In this section we apply the model reduction methods
developed above to an ecological model. In particular, we
consider the probability of extinction of a population of
predators when the prey undergoes a metastable stochas-
tic process with bistability. This case study allows us to
summarise the application of the method and, in partic-
ular, the two ingredients that one must extract from the
original slow–fast system, namely the quasi-stationary
densities and the mean switching times.
Most impor-
tantly, this model invites us to push the method further
by examining its performance with a system with absorb-
ing states. We are thus interested in capturing the evo-
lution of the system for low numbers. As a result, rather
than using the continuous Fokker–Planck (FP) approxi-
mation for both species as we did for the chemical system,
in this section we use the discrete description based on
the backward master equation for the dynamics of the
slow variable whose extinction we want to study.
We brieﬂy give some background to our choice of
model for this case study. One of the most fundamental
questions in population biology concerns the persistence
of species and populations, or conversely their risk of
extinction.33 Stochastic population models have become
a common tool to investigate how the mean time to ex-
tinction depends on properties of the ecosystem. How-
ever, performing detailed mathematical investigations to
understand how extinction risk depends on properties of
the ecosystem is limited by the availability of tractable
yet relevant models. A number of simple stochastic mod-
els of population dynamics have been used to study the
eﬀects of demographic processes on the mean time to
extinction.33 A small subset of these have looked at the
situation in which a population exhibits bistability (e.g.
Refs. 34–36). These are predominantly cases in which
there simultaneously exists a positive and a zero abun-


## Page 13


13
TABLE II. Propensity functions.
Prey
Predator
Transition
Propensity αi
Transition
Propensity αi
X →X + 1 α1(x) = λx −λ x2
κ
Y →Y + 1 α3(y) = ˜λy
X →X −1 α2(x) = µx +
βzx2
1+βhx2
Y →Y −1 α4(x, y) = ˜µy +
˜βy2
K(x)
dance attractor (locally stable steady states in the de-
terministic model). However, Palamara et al.37 recently
studied the mean time to extinction in simple predator–
prey stochastic systems and reported a region of param-
eter space in which the prey population is bistable be-
cause there exists two alternative attractors with positive
abundance, although they did not investigate that region
for the mean time to extinction. We choose to use the
model in Ref. 37 in the bistable regime as the basis for
our case study because the population dynamics exhib-
ited by the prey in this region are closely analogous to
the bistable dynamics of X in the chemical reaction case
(e.g. Fig. 15). To this we add a “predator” population
whose abundance is inﬂuenced by the abundance of the
prey, but does not itself inﬂuence the prey population
(for example it survives on the direct by-products of the
prey, such as dung beetles; while this is not strictly pre-
dation we will use the terms “predation” and “predator”
here for clarity). In this case study we consider the prob-
ability of extinction of such a predator population when
the prey undergoes a metastable stochastic process with
bistability. We do not choose this example to represent
any actual predator–prey system but rather to illustrate
the advantages of using our model reduction techniques
to enable the calculation of a property of domain-speciﬁc
interest; in this case enabling eﬃcient calculation of the
probability of extinction of a population.
We identify three regimes as in the previous chemical
example, depending on the relative timescales for prey-
population switches and predator dynamics, and use our
reduction method to measure the extinction rate of the
predator population without having to simulate the com-
putationally costly full predator–prey system. We con-
sider the following birth and death model for the prey37,
X
k1
−→2X,
X
k2
−→∅,
(28a)
where
k1(x) = λ

1 −x
κ

,
k2(x) = µ +
βxz
1 + βhx2 .
Here the reproduction of X corresponds to the Ver-
hulst logistic model for population growth,38 where λ
is the intrinsic growth rate of the population and κ
is referred to as the carrying capacity of the environ-
ment.
This abstraction is commonly used to repre-
sent the limiting-eﬀects of population density on pop-
ulation growth, through mechanisms such as resource
limitation.39 The population death rate includes a con-
stant death rate µ (predator-free death rate) and a
predation-induced death rate. We use a Holling’s Type
III functional response, representing a situation in which
predators consume multiple prey items and switch in
their feeding preference to predating on species X when it
becomes particularly abundant.39 The term βx is known
as the attack rate, h is the prey handling time and z is
the abundance of predators. Since we want this example
to showcase the applicability of the method in a practi-
cal problem, here we do not introduce small parameters
ǫ and δ as in the chemical system to make the character-
istic timescales of the fast variable explicit.
We suppose that the predator pool for x (parame-
terised by z) is composed of many species, of which we
pick one, denoted by y. We assume that changes in the
predator y are negligible from the point of view of the
prey, that is we can take z to be constant. We take the
predator population to evolve according to the logistic
model40
Y
k3
−→2Y,
Y
k4
−→∅,
(28b)
where
k3 = ˜λ,
k4(x, y) = ˜µ +
˜βy
K(x),
where K(x) is a prey-dependent carrying capacity of the
predator population. We will use K(x) = ˜κ(1 + xθ) in
what follows. The second term in k4 accounts for com-
petition for resources: the death rate per individual in-
creases with the predator population size and decreases
with increasing availability of prey. Note therefore that,
from an ecological standpoint, Y does not necessarily de-
pend on X to maintain a positive population size, but
its abundance is inﬂuenced by the availability of X. See
table II for a summary of the propensity functions for
each of the reactions.
In Fig. 15 we plot one run of the predator–prey system
(28) for the following set of parameters
λ = 1.5,
µ = 0.5,
β = 0.015/z,
κ = 1000,
h = 0.0055z,
˜λ = 5.5/τy,
˜µ = 3.5/τy,
˜β = 5.5/τy,
˜κ = 0.002,
θ = 2,
(29)
for three diﬀerent timescales τy for the predator. As be-
fore, we vary τy relative to the prey switching timescale
τs [which we ﬁnd to be τs = O(102) in the next sub-
section, see (31)] to move between regimes. Fig. 15(a)
corresponds to τy = 104 and is an example of a Regime


## Page 14


14
0
500
1000
1500
2000
0
100
200
300
400
500
 
 
time t
population
(a)
Regime 1
0
500
1000
1500
2000
0
100
200
300
400
500
 
 
time t
population
(b)
Regime 2
0
500
1000
1500
2000
0
100
200
300
400
500
 
 
time t
population
(c)
Regime 3
FIG. 15. Evolution of the prey X(t) (blue lines) and the predator Y (t) (green lines) from a single realisation of (28) obtained
using the NRM algorithm. We use the parameter values (29), X(0) = 200, Y (0) = 50, and vary τy to change between regimes.
(a) Regime 1: τy = 104. (b) Regime 2: τy = 100. (c) Regime 3: τy = 1.
1 situation: the predator population hardly responds to
ﬂuctuations in the abundance of the prey.
Fig. 15(b)
shows a run with τy = 100, which corresponds to Regime
2. Finally, in Fig. 15(c) the timescale of predator dynam-
ics is set to be much shorter than the switching time of
the prey by using τy = 1, which ﬁts with the deﬁnition
of third regime.
We notice a new and interesting eﬀect in this bistable
system as we vary the timescale of the population of in-
terest and change the regime: the predator population
in Regime 3 [Fig. 15(c)] has become extinct before the
ﬁnal simulation time Tf = 2000. This is only one run
of the stochastic system, but if we repeat the same ex-
periment many times a clear pattern emerges: in Regime
3 the predator population reacts quickly to a low level
of prey population and its chances of becoming extinct
increase substantially. On the other hand, in Regime 1
the predator population only sees an average of the prey
population and not its low and high levels and there-
fore the carrying capacity always stays at a level where
time to extinction is long (since ˜λ > ˜µ, giving a basic
reproduction ratio above one.38) In what follows we use
the slow–fast model reduction procedure to characterise
the mean extinction time of the predator population as
a function of its timescale relative to the switching time
of the bistable prey population.
A.
Quasi-stationary densities and mean switching times
Following the same procedure as for the chemical sys-
tem, we compute the stationary density ρ(x) of the prey
(in this case it is a stationary distribution conditioned on
the fact that extinction has not occurred, the so-called
quasi-stationary density38).41
It is well-known that the Chemical Langevin approx-
imation should not be used to predict the extinction
rate or the quasi-stationary density near the extinction
state, because it fails to correctly describe the very large
ﬂuctuations necessary to reach the absorbing state of
zero particles.42 However, here we focus on a parame-
ter regime for which the metastable prey population is
large and the relaxation time to its quasi-steady density
ρ(x) is extremely small compared to its mean time to
extinction. We thus ﬁnd that the stationary solution of
the Fokker–Planck equation with a reﬂecting boundary
condition at x = 0, equation (13), gives an accurate es-
timate of the prey quasi-stationary density. Methods to
determine this density more accurately in the region near
extinction are available (see e.g. Ref. 43). The drift and
diﬀusion coeﬃcients are
v(x) = x[k1(x) −k2(x)],
d(x) = 1
2x[k1(x) + k2(x)],
(30)
The resulting stationary density, which we denote again
by ρ(x), is shown in Fig. 16(a).
We observe that
ρ(x) is bimodal, indicating that the prey population is
metastable and will switch between its two favourable
states x−= 108.5 and x+ = 352.1.
In Fig. 16(b) we show the histograms of the quasi-
stationary predator distributions q±(Y ) conditioned on
the event of low and high prey levels respectively (X
lower or higher than x∗= 205.0), for the parameter val-
ues in (29) and τy = 100. We use the capital letter Y
to emphasise that we are not taking the continuum limit
here (assuming Y is large is not appropriate if we are
interested in extinction)
Next, we evaluate the mean-switching times between
the low and high prey-population levels as in section
III F. The mean time X spends in each well is estimated
from the stationary density shown in Fig. 16(a).
The
evolution of the mean of X is calculated by averaging
over 106 realisations up to Tf = 80. As before, we ﬁt an
exponential decay to the portion of the curve in which
x −x∞lies between 80% and 40% of its initial value.
From this analysis we obtain the following values for θ, ψ
and T±:
θ = 0.3004,
ψ = 76.8366,
T−= 109.8315,
T+ = 255.7689.
(31)
We note that the mean switching times T± set the size of
the switching timescale τs. Having obtained the quasi-


## Page 15


15
æ
æ
æ
æ
æ
æ
æ
æ
100
200
300
400
500
0.000
0.001
0.002
0.003
0.004
0.005
0.006
x
ρ(x)
(a)
0
50
100
150
0
0.02
0.04
0.06
0.08
 
 
q(Y )
Y
(b)
q−(Y )
q+(Y )
FIG. 16. (a) Quasi-stationary marginal density ρ(x) computed from (13) using the drift and diﬀusion coeﬃcients in (30). (b)
Quasi-stationary marginal densities q±(Y ) of Y from SSA of (28) conditional on the prey being at low (−, black histogram)
and high (+, red histogram) levels respectively, obtained from 107 steps of the NRM algorithm. We use τy = 100 and the
parameter values (29).
steady densities ρ±(x) of the fast metastable species and
its mean switching times T±, we are ready to apply the
reduced model approximations to simulate the predator–
prey system. Our goal is to estimate the mean time to
extinction (MTE) of the predator population.
B.
Mean times to extinction
Since we are interested in extinction we do not use
a continuum approximation for Y but retain a discrete
approximation. We denote by Tn the MTE of Y given
that Y (0) = n.
It can be determined exactly via the
backward master equation.15 We will use this approach
on the original model as well as on the reduced ones, as
detailed below.
1.
Full system
We denote by T m
n the two-dimensional MTE of the full
system (28) given that X(0) = m and Y (0) = n. It can
be easily shown [see analogous one-dimensional example
in (35) below] that it satisﬁes
−1 = α1(m)T m+1
n
+ α2(m)T m−1
n
+ α3(n)T m
n+1 + α4(m, n)T m
n−1
−[α1(m) + α2(n) + α3(n) + α4(m, n)]T m
n ,
(32)
with absorbing left-boundary conditions T m
0
= 0, T 0
n =
tn and a boundary condition at m = κ, α2(n)(T m−1
n
−
T m
n ) = 1, using that α1(κ) = 0. Here tn is the mean time
to extinction when there is no prey, which can be found
by solving Eq. (35) below replacing α4(n) by α4(0, n). In
principle this deﬁnes an inﬁnite set of diﬀerence equations
for T m
n
for n ≥1 and 0 ≤m ≤κ.
However, noting
that α4 ≫α3 for large n (due to the quadratic term in
α4, representing the competition), we can introduce an
artiﬁcial right boundary condition at n = N for large
N and use a similar argument to that of m = κ to give
α4(m, N)(T m
N−1 −T m
N ) = −1. This boundary condition
can be imposed by adopting the convention that α3(N) =
0.
Finally, to obtain Tn we integrate T m
n
against the
quasi-stationary density ρ(x) in Fig. 16(a).
2.
Reduced model 1 (τs ≪τy)
The appropriate reduced model for the system in
Regime 1, analogous to RM1 in (16), is
Y →Y + 1 : α3(Y ) = ˜λY,
Y →Y −1 : α4(Y ) = ˜µY +
˜βY 2
K ,
1
K =
Z ∞
0
ρ(x)
K(x) dx.
(33)
To obtain the MTE from (33), we consider what can the
predator population do in the ﬁrst short time interval δt:
Tn −δt = α3(n)δtTn+1 + α4(n)δtTn−1
+ [1 −α3(n)δt −α4(n)δt] Tn.
(34)
Hence we obtain
α3(n)Tn+1 −[α3(n)+ α4(n)]Tn + α4(n)Tn−1 = −1. (35)
Similarly as before, we solve (35) together with T0 = 0
and α3(N) = 0 for N large.
3.
Reduced model 2 (τs ∼τy)
Analogously to RM2 deﬁned in (17a), the reduced
model in Regime 2 has a death rate dependent on


## Page 16


16
whether the prey is at a low or high population level:
Y →Y + 1: α3(Y ) = ˜λY,
Y →Y −1: α±
4 (Y ) = ˜µY +
˜βY 2
K±
,
1
K±
=
Z
Ω±
ρ±(x)
K(x) dx,
(36a)
where ρ±(x) are the quasi-stationary prey densities taken
from ρ(x) conditioned on X ∈Ω± (left or right wells).
The switches between low- and high-level prey population
obey the reactions
S−
k−
−−⇀
↽−−
k+
S+,
k± = 1/T±
(36b)
with T± given in (31). This time the MTE must take
into account the initial state of the boolean variable S(t).
Denote T ±
n the MTE given that S(0) = S± and Y (0) =
n, respectively. Then, following a similar argument as
before, T ±
n obey
α3(n)T ±
n+1 + α±
4 (n)T ±
n−1 + k±T ∓
n
−[α3(n) + α±
4 (n) + k±]T ±
n = −1,
(37)
with T ±
0
= 0 and by convention α3(N) = 0.
Again
this results in a closed set of equations, now with 2N
equations and unknowns.
4.
Reduced model 3 (τy ≪τs)
Recall that the reduced model 3 does not keep track of
explicit Y dynamics but instead only those of the switch-
ing variable S. In order to extract a MTE in this reduced
model, we must introduce a new pair of reactions to rep-
resent Y -extinction from each of the wells:
S−
k−
−−⇀
↽−−
k+
S+,
S−
r−
−→∅,
S+
r+
−→∅,
(38)
where k± = 1/T± as before and ∅means “Y is extinct”.
Here the rates of predator extinction from the right and
left wells are r± = 1/Π±, where Π± are the MTE of Y
starting from its quasi-stationary distribution q±(Y ) and
conditional of X staying in a given well for all times. To
evaluate Π±, we solve the equation for the MTE in the
full system (32) but with a reﬂective boundary condition
at X = x∗, and integrate the resulting matrix T m
n against
the quasi-stationary densities Q±(m, n) (computed sim-
ilarly as for the chemical system). For any τy one ﬁnds
that Π−≪Π+ since it is much more likely for the preda-
tor to become extinct when the prey population is in the
left well than when it is in the right well [as can be seen
in Fig. 16(b)].
From (38) it is easy to show that the
MTE T ± of the reduced model in Regime 3 given that
S(0) = S± is
T ± =
k−+ k+ + r∓
k+r−+ k−r+ + r−r+
.
(39)
The approximation given by RM3 of the MTE Tn if we
don’t know where X(t) started [X(0) ∼ρ(x)] is given by
T = θT −+ (1 −θ)T +. Note that the result in RM3 does
not depend on the initial value of Y .
5.
Results
Using the exact expressions deﬁned above for the MTE
of Y (t) in the original system as well as in each reduced
model, we can look at the accuracy of each reduced model
relative to the exact full model as a function of τy. We
show the results in Fig. 17 for Y (0) = 30 and the param-
eter values (29) and (31). We choose the right boundary
at n = N such that the results are insensitive to N; we
ﬁnd that N = 150 is a good choice. The region of va-
lidity of each reduced model is set by the switching scale
τs ∼102 (e.g., when τy ∼102 the system is in Regime
2).
10
−1
10
0
10
1
10
2
10
3
10
4
10
5
10
0
10
1
10
2
10
3
10
4
10
5
10
6
10
7
 
 
Tn
τy
Full
RM1
RM2
RM3
FIG. 17. Theoretical mean time to extinction Tn of Y as a
function of τy. Curves obtained from the reduced models RM1
(35), RM2 (37) and RM3 (39), and the exact full system MTE
(32). We use n = 30, N = 150 and the parameter values (29)
and (31). The system (28) is in Regime 2 for τy around 100,
and moves towards Regime 1 (3) for larger (smaller) values of
τy.
We ﬁnd that the MTE computed from the full model
increases with τy roughly linearly (as expected) from
τy ∼O(102), but that for faster timescales it becomes
less sensitive to τy (see black line with circles in Fig. 17).
This is because, when the system is in Regime 3 and Y (t)
is fast, the main contribution to the T is the time it takes
for a switch in X from the right to the left well to occur
(i.e. T+ = 1/k+ on average) multiplied by the proba-
bility that X started in the right well, which is 1 −θ.
Once the switch to the low-level prey has occurred, the
extinction of Y is almost instantaneous for τy →0. This
is because this extinction occurs at a rate r−[see (38)]
which scales like 1/τy. If we do this simple calculation,
we ﬁnd that Tn should tend to T+(1 −θ) = 178.94 as


## Page 17


17
TABLE III. Mean time to extinction Tn of Y with Y (0) = n = 30 obtained from theory and simulations of the full system and
the reduced models in three parameter τy regimes. We use the same parameters and equations as in Fig. 17. For the simulated
MTE, we run iterations of the SSA until the standard error in the estimate of Tn is below 1% and indicate the execution times
in parenthesis.
Model
Regime 1 (τy = 104)
Regime 2 (τy = 100)
Regime 3 (τy = 1)
Th.
SSA
Th.
SSA
Th.
SSA
Full
6.968×105
6.545×105 (≈97h)a
2600.5
2566.7 (1097s)
219.24
219.58 (464s)
RM1
7.394×105
7.313×105 (11s)
7394.5
7333.2 (11s)
73.945
73.975 (10s)
RM2
7.043×105
7.058×105 (13s)
2790.8
2796.9 (8s)
197.64
199.98 (162s)
RM3
1.840×105
1.825×105 (0.9s)
2015.3
2018.1 (0.01s)
202.25
203.709 (0.005s)
a Value of T30 for τy = 104 computed from 400 runs of (28) (relative error of 6%). CPU time estimated from the execution time of 400
runs and the 104 runs required to obtain values with 1% relative error (estimated from the number of rounds required for τy = 104 in
the reduced models).
0
2
4
6
8
10
x 10
5
0
1
2
3
4
5
6 x 10
−6
distribution
T30
Regime 1
(a)
0
2000
4000
6000
8000
10000
0
1
2
3
4
5
6 x 10
−4
distribution
T30
Regime 2
(b)
0
50
100
150
200
250
300
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
 
 
x 10−2
distribution
T30
Regime 3
(c)
Full
RM1
RM2
RM3
FIG. 18. Distribution of the time to extinction Tn with Y (0) = n = 30 for the parameters in (29) and τy = 104, 100 and 1
(corresponding roughly to a system in Regime 1, 2 and 3 respectively). Histograms computed by 105 rounds of the SSA of the
full system (28), and reduced models 1 (33), 2 (36) and 3 (38), respectively [except for the full system in (a), in which only
3300 rounds are used].
τy →0, using (31).
This value is consistent with the
results plotted in Fig. 17. We see that the approxima-
tion of the MTE given by RM2 agrees very well with the
exact MTE from the full system throughout the whole
range of timescales τy except for very small scales where
a small error can be perceived. As expected, the approxi-
mation to the MTE of RM1 is good for slow timescales τy
such that the system is in Regime 1 (τy →∞), but very
poor for fast timescales in Regime 3 when the MTE is
highly dependent on the bistable prey behaviour. Con-
versely, the approximation of RM3 is good in Regime
3 (τy small), but underestimates the MTE of Y when
the predator is very slow (and is thus not as sensible to
switches to the low-level in the prey population).
In Table III we compare the theoretical results of
Fig. 17 with those obtained from multiple repetitions
of the SSA. We do this to have an idea of the compu-
tational time reduction that each reduced model gives
relative to the original system. We choose three values
of the timescale τy such that they are representative of
each regime: τy = 104 for Regime 1, τy = 100 for Regime
2, and τy = 1 for Regime 3. To compute Tn numerically,
we run the SSA of the full system (28) and the three re-
duced models RM1 (33), RM2 (36), and RM3 (38). We
initialise the system with Y (0) = 30 and X(0) ∼ρ(x)
[equivalently, for RM2 and RM3, S(0) = S−with proba-
bility θ] and run the simulation until Y (t) = 0. We record
the ﬁnal time and repeat the process until the standard
error in Tn is below 1%. The twelve simulation values
of T30 in Table III required O(104) runs to achieve such
relative error.
Finally, in Fig. 18 we show the histograms of the time
to extinction T30 obtained from the simulations. We com-
pare the distribution of T30 of the full system with those
from the reduced models.
We see that the Regime 2
model does a good job of capturing the distribution for
the whole range of values of τy. In contrast the reduced
models 1 and 3 fail to capture the distribution of T30
near the origin when used outside of their regime of va-
lidity. This would be important if, for instance, we were
interested in the probability that the predator population
became extinct within one year.
V.
SUMMARY AND DISCUSSION
In this paper we developed a model reduction tech-
nique for slow–fast stochastic systems with metastability.
This is a generalisation of previous approaches based on
stochastic averaging principles,17 when the average of the


## Page 18


18
fast process switches between diﬀerent quasi-stationary
densities instead of relaxing to a unique stationary mea-
sure. Interestingly, we found that we can still accurately
describe the behaviour of metastable slow–fast systems
while improving numerical eﬃciency substantially by in-
troducing a switch variable to describe the metastable
process and using stochastic averaging separately in each
of the basins of attraction.
We focused on a simple class of metastable slow–fast
stochastic systems consisting of two species, one of which
(X) is fast with exponentially long bistable switches. The
second species (Y ), which we assume is the species of
interest, has dynamics that are coupled to the bistable
species.
We identiﬁed three dynamical regimes that
led to diﬀerent model reductions in both of our two-
species metastable systems.
When the dynamics of Y
are much slower than the switches in X (and thus not af-
fected by the bistable behaviour) then the reduced model
RM1 is equivalent to the standard fast-variables reduc-
tion used in monostable systems.17 However, in the other
two regimes, when the evolution of Y is of the same or-
der or faster than the switches in X, then the switches
in X must be taken into account. Our key insight is that
two ingredients are required to build a reduced model for
slow–fast system with metastability in general. The ﬁrst
ingredient is knowledge of the transition rates between
the diﬀerent basins of attraction for the fast variables
(which could of course be more than two in other situa-
tions). The second ingredient is the need for estimates of
the quasi-stationary densities of the fast variables, con-
ditioned on being in each basin of attraction. This is the
procedure used by Markov state models for the modelling
of molecular kinetics, with powerful yet computationally
expensive tools available to do this in high-dimensional
systems, more suited for parallel computation.44
In the chemical example, we showed how asymptotic
approximations of the transition rates can be obtained
from the Fokker–Planck equation, as well as from a short
SSA run of the full system. In general applications the
latter approach is likely to be more feasible because the
Fokker–Planck equations can only be used in a limited set
of analytically tractable models. However, as seen in sec-
tion III F, care must be taken in deﬁning what it means
for the system to have switched to another favourable
state.
Switching rates have been inferred from other
model parameters in a related way for ion channels.45,46
For both the chemical and the ecological examples, we
obtained the quasi-stationary densities of the fast vari-
ables from both the Fokker–Planck equation equation
and the SSA results: again, the limitations of using the
Fokker–Planck equation for more general purposes ap-
ply. However, once the conditional quasi-steady densities
and the switching rates have been obtained, then we can
compute the eﬀective rates for the slow variables condi-
tioned on each basin and the transition ﬂuxes between
sub-models.
In this work we assumed a known slow–fast model with
ﬁxed parameters. One natural extension to our study is
to systems in which the parameters aﬀecting the regime
may change through time. For example, if τy changed
through time, then one may be inclined to dynamically
change the reduced model being employed. This would
require building a set of rules or boundaries to discern be-
tween regimes (precomputed), and checking during a sim-
ulation whether any of these have been crossed. However,
the extra computational eﬀort involved in such a process
is likely to be more costly than simply using the reduced
model 2 (RM2) throughout the simulation. This model
interpolates between Regimes 1 and 3 and is valid in the
whole parameter regime for τy (e.g. see Fig. 17). To our
knowledge this is the ﬁrst method that can be used in the
whole spectrum of τy in the class of systems considered
here, thus extending the method in Ref. 28 to cases with
more than one stable state, while still keeping it simple (a
one-dimensional model plus the switch variable), in con-
trast to more complicated fully two-dimensional models
appropriate in Regime 3.47 A potentially more interest-
ing situation arises if the (quasi-)stationary density of
the fast variable ρ(x) changes dynamically; maybe even
through a two-way coupling with y. In this case, the RM2
as presented would need to be modiﬁed to since one needs
to update dynamically the mean switching times T± and
the conditional densities ρ±(x). Moreover, it could hap-
pen that ρ(x) evolved from a bimodal to unimodal shape,
in which case the system would move into into the monos-
table regime. A possible strategy would be to establish
a timestep ∆y such that ǫ ≪∆y ≪τy, and every ∆y
stop the simulation, do a short run of the full dynamics
to re-evaluate T ˆy
± and ρˆy
±(x), parameterised by current
value of Y = ˆy.
We applied our techniques to a metastable system with
an absorbing state; the predator–prey stochastic model
with bistable prey (X), and showed that the reduced
models can be used to predict the mean times to extinc-
tion (MTE) of the predator population Y in an accurate
and eﬃcient way. Fundamentally, this showed that the
method can be applied more generally to two-dimensional
systems, even with absorbing states. This implies that
the speciﬁc forms of the rates and the coupling between
X and Y do not matter for the application of our model
reduction techniques. Moreover, the model reduction has
provided some new insights into how the routes to ex-
tinction of the predator change as we varied its relative
timescale to the prey switching and its quasi-stationary
density changed from unimodal to bimodal. In particu-
lar, the reduced model RM2 can identify the huge diﬀer-
ence between the MTE of Y when the prey population
X is at its low or high level, and, most importantly, how
this fact together with the bistable process translates into
the overall MTE. The speciﬁc application of our approx-
imations to enable the eﬃcient calculation of the mean
time to extinction in Regime 2 is, to our knowledge, new
to the literature and clearly illustrates the value of the
approximations of reduced model 2 (explicit Y with a
switch variable for X) over the original system to esti-
mate the mean time to extinction. It was fortunate for


## Page 19


19
these equations that we could assess our estimates with
the backward master equation; however, this will rarely
be possible for higher-dimensional ecological models. It
is in such situations that having insight into the appro-
priate reduction method is most valuable, giving one the
ability to select the appropriate stochastic reduced model
to obtain accurate approximations eﬃciently. In high di-
mensional systems with several variables displaying in-
trinsic metastable behaviour, one could use a combina-
tion of our method presented here for the MTE and the
computational approaches discussed in Ref. 44 to split
the space into basins of attraction and approximate the
transitions times.
Finally, this work could be extended to enable long-
term predictions of complex real bistable systems. This
could, for example, enable new insights into our under-
standing of critical transitions and our ability to predict
them.9 In recent years there has been a lot of eﬀort in in-
vestigating time-series of systems prone to critical transi-
tions in an attempt to enable predictions of transitions.48
Could we detect the dynamical regime of a bistable sys-
tem from its dynamics without knowing the parameters
or model? If we could then it is possible to imagine using
similar ingredients to those used here to infer the mean
switching times characterising the metastable processes
and the reaction time (after a switch) for the variables of
interest.
ACKNOWLEDGMENTS
We thank J. M. Newby, G. M. Palamara, and Y. G.
Kevrekidis for useful discussions on aspects of this ar-
ticle.
We also thank M. Geissbuehler and T. Lasser
for their Morgenstemning colormap.49 M.B. is partially
funded by the EPSRC (EP/I017909/1) and Microsoft Re-
search, Cambridge and by St John’s College, Oxford, in
the form of a Junior Research Fellowship.
Appendix A: Perturbation analysis of the three bistable
regimes
In this appendix we provide formal derivations of the
three reduced models in the main text using a pertur-
bation analysis at the level of the Fokker–Planck equa-
tion for the joint probability density P(x, y, t). In A 1
we consider the asymptotic regime τs ≪τy (Regime 1),
resulting in the reduced model 1. The more interesting
reduced model 2, appropriate when τs ∼τy, is derived
in A 2 using a WKB perturbation method. Finally, in
A 3 we discuss the regime when τy ≪τs and the reduced
model 3 is appropriate.
We consider the Fokker–Planck equation (10) for the
joint probability density P(x, y, t). The main timescale
of interest is that of the evolution of Y , so let us rescale
time with τy to give
∂P
∂t (x, y, t) = τy
ǫ
∂
∂x
 ∂
∂x[d(x)P] −v(x)P

+ ∂
∂y
 ∂
∂y[D(x, y)P] −V (x, y)P

,
(A1)
where τy/ǫ ≫1.
1.
Regime 1: ǫ ≪τs ≪τy
First we consider equation (A1) for short times such
that t = O(ǫ). We deﬁne the fast time ˜t as t = (ǫ/τy)˜t
and write ˜P(x, y, ˜t) = P(x, y, t), to give, at leading order,
∂˜P (0)
∂˜t
= ∂
∂x
 ∂
∂x[d(x) ˜P (0)] −v(x) ˜P (0)

.
(A2)
As ˜t →∞, the solution of (A2) converges to
˜P (0)(x, y) = ρ(x)q(y),
(A3)
where ρ(x) is the normalised steady solution of (A2)
[given by (13)], and
q(y) =
Z ∞
0
P(x, y, 0) dx.
Now we move back to O(1) times and consider equation
(A1). Expanding P ∼P (0) + ǫ/τy P (1) + · · · , gives, at
leading-order,
∂
∂x
 ∂
∂x[d(x)P (0)] −v(x)P (0)

= 0.
(A4)
Thus
P (0)(x, y, t) = C(y, t)ρ(x),
(A5)
where C(y, t) is arbitrary at this stage. Matching this
solution for long times with the short times solution (A3)
gives C(y, 0) = q(y). At the next order equation (A1)
gives
∂P (0)
∂t
= ∂
∂x
 ∂
∂x[d(x)P (1)] −v(x)P (1)

+ ∂
∂y
 ∂
∂y[D(x, y)P (0)] −V (x, y)P (0)

.
(A6)
Integrating this equation with respect to x (using no-ﬂux
boundary conditions at x = 0, ∞) gives the following
solvability condition for C:
∂C
∂t (y, t) = ∂
∂y
 ∂
∂y

D(y)C(y, t)

−V (y)C(y, t)

(A7)
where
F(y) =
Z
F(x, y)ρ(x) dx,
for F = D, V.


## Page 20


20
Finally, since
C(y, t) =
Z ∞
0
P(x, y, t) dx
we see that C(y, t) is the marginal density for Y (t), so
that (A7) gives the evolution of the probability density
function of a reduced process for Y (t) where the fast
variable X(t) has been averaged out. Going back to the
original time variable we can then write
∂p
∂t (y, t) = 1
τy
∂
∂y
 ∂
∂y

D(y)p

−V (y)

(A8)
Equation (A8) is the Fokker–Planck equation associated
with the reduced stochastic model (16) appropriate for
Regime 1 when Y is approximated by a continuous ran-
dom variable. This asymptotic reduction relies on the
fact that the stochastic process for X reaches steady state
on a timescale which is faster than the timescale for the
evolution of Y .
2.
Regime 2: ǫ ≪τs ∼τy
To analyse Regime 2 asymptotically we need to ensure
that X is metastable, and quantify the switching time.
We suppose then that 1/δ, the typical equilibrium value
of X, is large, and scale the rate constants as in (7). We
set ˆx = δx, where ˆx is O(1) as δ →0. We will see that
τs ∼er/δ for some constant r > 0. In terms of the new
scaled variables equation (A1) becomes
∂P
∂t = τy
ǫ
∂
∂ˆx
 ∂
∂ˆx[δ ˆd(ˆx)P] −ˆv(ˆx)P

+ ∂
∂y
 ∂
∂y[D(ˆx, y)P] −V (ˆx, y)P

,
(A9)
where ˆd(ˆx) = δd(x), etc. With this scaling we see that
the diﬀusion δ ˆd(ˆx) of X is weaker than the drift ˆv(ˆx)
when δ ≪1, which is the reason that switches do not
occur frequently (τs ≫ǫ); the parameter δ makes ex-
plicit this separation of timescales between drift of X
and switches in X (this is the weak noise limit50).
It is convenient to write (A9) in the form
ˆǫ∂P
∂t + ˆǫ∂Jy
∂y = Lδ,
(A10)
where ˆǫ = ǫ/τy, Jy = −∂
∂y[D(ˆx, y)P] + V (ˆx, y)P and Lδ
is a linear operator acting on the variable ˆx only:
LδP ≡∂
∂ˆx
 ∂
∂ˆx[δ ˆd(ˆx)P] −ˆv(ˆx)P

.
(A11)
The marginal stationary density in ˆx [ρ(x) in (13)] cor-
responds to the zero-eigenvalue eigenfunction Lδ, that is
Lδρ(ˆx) = 0, giving, in the scaled variables,
ρ(ˆx) =
A
ˆd(ˆx)
exp
"
1
δ
Z ˆx
0
ˆv(s)
ˆd(s)
ds
#
,
(A12)
where A is the normalisation constant.
The novelty in this bistable problem is the coupling of
X with Y , that is, in the term Jy in (A10). We sketch
the following calculation since it follows closely that of
Refs. 19 and 20.
By using a WKB approximation for
small δ (with ˆǫ ≪δ) we ﬁnd solutions to (A10) of the
form
P ∼







A−φ(ˆx)
ˆx < ˆxv
∗,
1
2φ(ˆxv
∗)e−γ∗(ˆx−ˆxv
∗)2/2δ

A+ + A−+ (A+ −A−)erf
q
|γ∗|
2δ (ˆx −ˆxv
∗)

ˆx ≈ˆxv
∗,
A+φ(ˆx)
ˆx > ˆxv
∗.
(A13)
where
φ(ˆx) = eu(ˆx)/δ
ˆd(ˆx)
,
u(ˆx) =
Z ˆx
0
ˆv(s)
ˆd(s)
ds,
γ∗= −ˆv′(ˆxv
∗)
ˆd(ˆxv∗)
,
(A14)
and ˆxv
∗is the turning point at which u′(ˆxv
∗) = 0. Here
A−and A+ are independent of ˆx but are undetermined,
and may depend on both y and t. Deﬁne
Φ± =
1
A±
Z
Ω±
P± dˆx ≡
Z
Ω±
φ dˆx.
(A15)
We note that A+Φ+ = 1 −θ introduced in section III F.
These integrals can be evaluated using Laplace’s method,


## Page 21


21
giving
Φ± ∼
s
2πδ
γ±
φ(ˆxv
±),
(A16)
where ˆxv
± are the maxima of u (or the zeros of ˆv) in Ω±
and
γ± = −ˆv′(ˆxv
±)
ˆd(ˆxv
±)
.
In the one-dimensional case we could now use the nor-
malisation condition on P to give a relationship between
A+ and A−, namely 1 = Φ−A−+ Φ+A+. But in the
two-dimensional case we only have that
p(y, t) =
Z ∞
0
P(ˆx, y, t) dˆx = A−(y, t)Φ−+ A+(y, t)Φ+.
(A17)
Deﬁne
p±(y, t) = Φ±A±(y, t),
(A18)
which we can interpret as the marginal density for Y
given X is in the left/right well, multiplied by the prob-
ability that X is in that well. To calculate the exponen-
tially slow transition rates we need to calculate the ﬁrst
eigenvalue/eigenfunction of Lδ, given by
Lδρ1 = λ1ρ1,
(A19)
say. Following Ward,19 a good approximation of the ﬁrst
eigenfunction ρ1 is the derivative of (A13) with respect
to the unknown constant. Using ρ1(ˆx) = ∂P/∂A−, gives
ρ1(ˆx) ∼







φ(ˆx)
ˆx < ˆxv
∗,
1
2φ(ˆxv
∗)e−γ∗(ˆx−ˆxv
∗)2/2δ

1 −Φ−
Φ+ −

1 + Φ−
Φ+

erf
q
|γ∗|
2δ (ˆx −ˆxv
∗)

ˆx ≈ˆxv
∗,
−Φ−
Φ+ φ(ˆx)
ˆx > ˆxv
∗.
(A20)
To obtain λ1 we use a spectral projection method that
makes use of the adjoint operator L∗
δ, given by
L∗
δϕ ≡

δ ˆd(ˆx)∂2ϕ
∂ˆx2 + ˆv(ˆx)∂ϕ
∂ˆx

,
(A21)
together with boundary conditions ϕ′(ˆx) = 0 on ˆx =
0, ∞. The eigenfunctions of the adjoint operator satisfy
L∗
δξj = λjξj,
(A22)
with the orthogonality relationship ⟨ρi, ξj⟩= δij where
δij is the Kronecker delta. The adjoint eigenfunction cor-
responding to λ0 = 0 is simply ξ0 = 1. The ﬁrst adjoint
eigenfunction ξ1(ˆx) is approximately (see e.g. Ref. 20)
ξ1(ˆx)∼









Φ+
Φ−(Φ++Φ−)
ˆx < ˆxv
∗,
Φ+
Φ−(Φ++Φ−) −
1
2Φ−erf
q
|γ∗|
2δ (ˆx −ˆxv
∗)

ˆx ≈ˆxv
∗,
−1
(Φ++Φ−)
ˆx > ˆxv
∗,
(A23)
The ﬁrst eigenvalue can now be computed by taking
the inner product of (A19) with a suitable test function
ϕ:
⟨ϕ, Lδρ1⟩= λ1⟨ϕ, ρ1⟩.
(A24)
Here we use ϕ = 1Ω−. The left hand side gives
⟨ϕ, Lδρ1⟩=
Z ˆxv
∗
0
Lδρ1 dˆx =
 ∂
∂ˆx[δ ˆd(ˆx)ρ1] −ˆv(ˆx)ρ1

ˆx=ˆxv∗
=
√
δ ˆd(ˆxv
∗)ρ′
1(z)|z=0
= −
√
δeu(ˆxv
∗)/δ

1 + Φ−
Φ+
 r
|γ∗|
2π .
(A25)
The right-hand side is
⟨ϕ, ρ1⟩=
Z ˆxv
∗
0
ρ1 dˆx = Φ−∼
s
2πδ
γ−
φ(ˆxv
−),
(A26)
using (A16). Combining (A25) and (A26) gives the ex-
ponentially small eigenvalue
λ1 ∼−
ˆd(ˆxv
−)
2π

1 + Φ−
Φ+
 s
|γ∗|
γ−
exp
u(ˆxv
∗) −u(ˆxv
−)
δ

.
(A27)
Note that the argument of the exponential is negative
since u(ˆxv
∗) < u(ˆxv
−).
Finally, we seek the diﬀerential equations describing
the evolution of A+ and A−.
First we integrate the
equation (A10) with respect to ˆx (equivalent to taking


## Page 22


22
the inner product with the adjoint eigenfunction ξ0 = 1):
ˆǫ

1, ∂P
∂t + ∂Jy
∂y

= ⟨ξ0, LδP⟩= ⟨L∗
δξ0, P⟩= 0. (A28)
From the left-hand side we have

1, ∂P
∂t

= Φ−
∂A−
∂t
+ Φ+
∂A+
∂t ,
(A29)
and

1, ∂Jy
∂y

=
Z
Ω−
∂
∂y

V (ˆx, y)A−−∂
∂y [D(ˆx, y)A−]

φ(ˆx) dˆx
+
Z
Ω+
∂
∂y

V (ˆx, y)A+ −∂
∂y [D(ˆx, y)A+]

φ(ˆx) dˆx.
(A30)
Taking the integrals over Ω± inside the y derivatives and
using that ρ±(ˆx) = φ(ˆx)/Φ±, we ﬁnd

1, ∂Jy
∂y

= Φ−
∂
∂y

V −(y)A−−∂[D−(y)A−]
∂y

+ Φ+
∂
∂y

V +(y)A+ −∂[D+(y)A+]
∂y

,
(A31)
where
F ±(y) :=
Z
Ω±
F(ˆx, y)ρ±(ˆx) dˆx,
for F = D, V. (A32)
Thus
0 = Φ−
∂A−
∂t
+ Φ+
∂A+
∂t
+ Φ−
∂
∂y

V −(y)A−−∂[D−(y)A−]
∂y

+ Φ+
∂
∂y

V +(y)A+ −∂[D+(y)A+]
∂y

.
(A33)
Next we take the inner product of (A10) with the ﬁrst
adjoint eigenfunction:
ˆǫ

ξ1, ∂P
∂t + ∂Jy
∂y

= ⟨ξ1, LδP⟩= ⟨L∗
δξ1, P⟩= λ1⟨ξ1, P⟩.
(A34)
Using (A13) and (A23) gives another PDE for A−and
A+:
∂A−
∂t
−∂A+
∂t
−∂
∂y
∂[D−(y)A−]
∂y
−V −(y)A−

+ ∂
∂y
∂[D+(y)A+]
∂y
−V +(y)A+

= λ1
ˆǫ (A−−A+).
(A35)
Rearranging (A33) and (A35) we ﬁnd the following sys-
tem for A−(y, t) and A+(y, t):
∂A−
∂t
−∂
∂y
∂[D−(y)A−]
∂y
−V −(y)A−

= λ1
ˆǫ
Φ+
Φ−+ Φ+
(A−−A+),
(A36a)
∂A+
∂t
−∂
∂y
∂[D+(y)A+]
∂y
−V +(y)A+

= λ1
ˆǫ
Φ−
Φ−+ Φ+
(A+ −A−).
(A36b)
Using (A18), we can write (A36) in terms of probabilities,
p±(y, t):
∂p−
∂t −∂
∂y
∂[D−(y)p−]
∂y
−V −(y)p−

= λ1
ˆǫ
1
Φ−+ Φ+
(Φ+p−−Φ−p+),
(A37a)
∂p+
∂t −∂
∂y
∂[D+(y)p+]
∂y
−V +(y)p+

= λ1
ˆǫ
1
Φ−+ Φ+
(Φ−p+ −Φ+p−).
(A37b)
Finally, rescaling time in (A37) back to the original time
variable [recall that in (A1) we had scaled time with τy],
we ﬁnd that
∂p−
∂t −1
τy
∂
∂y
∂[D−(y)p−]
∂y
−V −(y)p−

= k+p+−k−p−,
(A38a)
∂p+
∂t −1
τy
∂
∂y
∂[D+(y)p+]
∂y
−V +(y)p+

= k−p−−k+p+,
(A38b)
where
k−=
Φ+
Φ−+ Φ+
|λ1|
ǫ ,
k+ =
Φ−
Φ−+ Φ+
|λ1|
ǫ .
(A39)
These rates can be identiﬁed as the transition rates from
the left to right well and vice versa (introduced in section
III F).
Equations (A38) are the Fokker–Planck equations as-
sociated with the reduced stochastic model (17a) appro-
priate for Regime 2 when Y is approximated by a con-
tinuous random variable.
3.
Regime 3: ǫ ∼τy ≪τs
In Regime 3 both X and Y switch between localised
metastable states. A similar analysis to that in §A 2 can
be used. In our simpliﬁed example in which the bistable
variable X is independent of Y the switching rate is
exactly given by §A 2; all that remains is to calculate


## Page 23


23
the quasi-stationary density for each metastable state.
To approach this analytically requires a two-dimensional
WKB (ray theory) approach, which is considerable more
complicated than the one-dimensional version in §A 2.
If the system was fully coupled, a two-dimensional ver-
sion of the eigenvalue calculation of §A 2 would be re-
quired to analytically determine the transition rates.47
Alternatively we could numerically obtain the quasi-
stationary densities of each well and the mean switching
times between attractors using short bursts of stochastic
simulation, as described in Sec. III F. Such a numerical
approach could in principle be extended to an arbitrary
number of attractors and/or higher dimensions as an au-
tomated process. However, as we have seen, care needs
to be taken to deﬁne the boundaries between attractors
and in determining the switching times.22
1P. Thomas, A. V. Straube,
and R. Grima, BMC Syst. Biol. 6,
39 (2012).
2H. H. McAdams and A. Arkin, Trends Genet. 15, 65 (1999).
3E. M. Ozbudak, M. Thattai, H. N. Lim, B. I. Shraiman,
and
A. van Oudenaarden, Nature 427, 737 (2004).
4J.-W. Veening, W. K. Smits,
and O. P. Kuipers, Annu. Rev.
Microbiol. 62, 193 (2008).
5W. Horsthemke and R. Lefever, Noise-induced transitions: The-
ory and applications in physics, chemistry, and biology, 1st ed.,
Vol. 15 (Springer-Verlag, Berlin and New York, 1984).
6R. Wang, J. A. Dearing, P. G. Langdon, E. Zhang, X. Yang,
V. Dakos, and M. Scheﬀer, Nature 492, 419 (2012).
7W. E, D. Liu, and E. Vanden-Eijnden, Comm. Pure Appl. Math.
58, 1544 (2005).
8A. C. Staver, S. Archibald,
and S. A. Levin, Science 334, 230
(2011).
9M. Scheﬀer, S. R. Carpenter, T. M. Lenton, J. Bascompte,
W. Brock, V. Dakos, J. van de Koppel, I. A. van de Leemput,
S. A. Levin, E. H. van Nes, M. Pascual,
and J. Vandermeer,
Science 338, 344 (2012).
10N. Fenichel, J. Diﬀer. Equations 31, 53 (1979).
11M. Desroches, J. Guckenheimer, B. Krauskopf, C. Kuehn, H. M.
Osinga, and M. Wechselberger, SIAM Rev. 54, 211 (2012).
12P. Boxler, Probab. Theory Rel. 83, 509 (1989).
13G. W. A. Constable, A. J. McKane, and T. Rogers, J. Phys. A:
Math. Theor. 46, 295002 (2013).
14G. Wainrib, Electronic Communications in Probability 18, 1
(2013).
15C. W. Gardiner, Handbook of Stochastic Methods for Physics,
Chemistry and the Natural Sciences, 3rd ed. (Springer-Verlag,
New York, 2004).
16Y. Cao, D. T. Gillespie, and L. R. Petzold, J. Chem. Phys. 122,
014116 (2005).
17C. V. Rao and A. P. Arkin, J. Chem. Phys. 118, 4999 (2003).
18J. M. Newby and S. J. Chapman, J. Math. Biol. (2013).
19M. J. Ward, in Analyzing Multiscale Phenomena Using Singu-
lar Perturbation Methods, edited by J. Cronin and R. O’Malley
(AMS publications, Providence, RI, 1998) pp. 151–184.
20R. Hinch and S. J. Chapman, Eur. J. Appl. Math 16, 427 (2005).
21J. M. Newby, Phys. Biol. 9, 026002 (2012).
22C. Hartmann,
R. Banisch,
M. Sarich,
T. Badowski,
and
C. Sch¨utte, Entropy 16, 350 (2013).
23F. Schl¨ogl, Z. Phys. 253, 147 (1972).
24R. Erban, S. J. Chapman, I. G. Kevrekidis, and T. Vejchodsk´y,
SIAM J. Appl. Math. 70, 984 (2009).
25Some authors would use the convention that the propensity func-
tion for the third reaction, 2X
k3/ǫ
−→3X, is k3x(x −1)/2ǫ instead
of k3x(x −1)/ǫ. See Ref. 26 for a discussion on conventions re-
garding reaction rates.
26D. T. Gillespie, J. Phys. Chem. 81, 2340 (1977).
27M. A. Gibson and J. Bruck, J. Phys. Chem. A 104, 1876 (2000).
28Y. Cao, D. T. Gillespie, and L. R. Petzold, J. Chem. Phys. 124,
044109 (2006).
29D. T. Gillespie, J. Chem. Phys. 113, 297 (2000).
30This is in contrast to the Parallel Replica Algorithm,32 which
deﬁnes quasi-stationary distributions using absorbing boundary
conditions.
31H. Risken, The Fokker-Planck Equation, Methods of Solution
and Applications (Springer, 1996).
32C. Le Bris, T. Leli`evre, M. Luskin, and D. Perez, Monte Carlo
Methods Appl. 18, 119 (2012).
33O. Ovaskainen and B. Meerson, Trends Ecol. Evol. 25, 643
(2010).
34C. E. Brassil, Ecol. model. 143, 9 (2001).
35B. Dennis, Oikos 96, 389 (2002).
36S. J. Schreiber, Theor. Popul. Biol. 64, 201 (2003).
37G. M. Palamara, G. W. Delius, M. J. Smith, and O. L. Petchey,
J. Theor. Biol. 334, 61 (2013).
38I. N˚asell, J. Theor. Biol. 211, 11 (2001).
39P.
Turchin,
Complex
Population
Dynamics:
A
Theoreti-
cal/Empirical Synthesis (Princeton University Press, 2003).
40J. Grasman and R. HilleRisLambers, Ecol. model. 103, 71 (1997).
41This is because if we waited long enough in the stochastic model,
extinction would eventually occur, and therefore the stationary
density is not deﬁned. In other words, there is a “leak” at x = 0.
42D. A. Kessler and N. M. Shnerb, J. Stat. Phys. 127, 861 (2007).
43M. Assaf and B. Meerson, Phys. Rev. E 81, 021116 (2010).
44J.-H. Prinz, H. Wu, M. Sarich, B. Keller, M. Senne, M. Held,
J. D. Chodera, C. Sch¨utte,
and F. No´e, J. Chem. Phys. 134,
174105 (2011).
45E. Abad, J. Reingruber, and M. S. P. Sansom, J. Chem. Phys.
130, 085101 (2009).
46W. Chen, R. Erban, and S. J. Chapman, SIAM J. Appl. Math.
74, 208 (2014).
47P. C. Bressloﬀand J. M. Newby, SIAM J. Appl. Dyn. Syst. 12,
1394 (2013).
48V. Dakos, S. R. Carpenter, W. A. Brock, A. M. Ellison, V. Gut-
tal, A. R. Ives, S. K´eﬁ, V. Livina, D. A. Seekell, E. H. van Nes,
and M. Scheﬀer, PLoS ONE 7, e41010 (2012).
49M. Geissbuehler and T. Lasser, Opt. Express 21, 9862 (2013).
50P. C. Bressloﬀand J. M. Newby, in First-Passage Phenomena
and Their Applications, edited by R. Metzler, G. Oshanin, and
S. Redner (World Scientiﬁc, 2013) pp. 1–29.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
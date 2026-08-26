---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1201.5229v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1201.5229v1_Cross-entropy_optimisation_of_importance_sampling_parameters_for_statistical_mod

> Source: 1201.5229v1_Cross-entropy_optimisation_of_importance_sampling_parameters_for_statistical_mod.pdf

> Pages: 16

---


## Page 1


arXiv:1201.5229v1  [cs.PF]  25 Jan 2012
Cross-entropy optimisation of importance
sampling parameters for statistical model
checking
Cyrille J´egourel, Axel Legay and Sean Sedwards⋆
INRIA Rennes - Bretagne Atlantique,
{cyrille.jegourel,axel.legay,sean.sedwards}@inria.fr
Abstract. Statistical model checking avoids the exponential growth of
states associated with probabilistic model checking by estimating prop-
erties from multiple executions of a system and by giving results within
conﬁdence bounds. Rare properties are often very important but pose
a particular challenge for simulation-based approaches, hence a key ob-
jective under these circumstances is to reduce the number and length
of simulations necessary to produce a given level of conﬁdence. Impor-
tance sampling is a well-established technique that achieves this, however
to maintain the advantages of statistical model checking it is necessary
to ﬁnd good importance sampling distributions without considering the
entire state space.
Motivated by the above, we present a simple algorithm that uses the
notion of cross-entropy to ﬁnd the optimal parameters for an importance
sampling distribution. In contrast to previous work, our algorithm uses
a low dimensional vector of parameters to deﬁne this distribution and
thus avoids the often intractable explicit representation of a transition
matrix. We show that our parametrisation leads to a unique optimum
and can produce many orders of magnitude improvement in simulation
eﬃciency. We demonstrate the eﬃcacy of our methodology by applying
it to models from reliability engineering and biochemistry.
1
Introduction
The need to provide accurate predictions about the behaviour of complex sys-
tems is increasingly urgent. With computational power becoming ever-more af-
fordable and compact, computational systems are inevitably becoming increas-
ingly concurrent, distributed and adaptive, creating a correspondingly increased
burden to check that they function correctly. At the same time, users expect
high performance and reliability, prompting the need for equally high perfor-
mance analysis tools and techniques.
The most common method to ensure the correctness of a system is by testing
it with a number of test cases having predicted outcomes that can highlight
speciﬁc problems. Testing techniques have been eﬀective discovering bugs in
⋆To whom correspondence should be addressed.


## Page 2


many industrial applications and have been incorporated into sophisticated tools
[9]. Despite this, testing is limited by the need to hypothesise scenarios that may
cause failure and the fact that a reasonable set of test cases is unlikely to cover
all possible eventualities; errors and modes of failure may remain undetected and
quantifying the likelihood of failure using a series of test cases is diﬃcult.
Model checking is a formal technique that veriﬁes whether a system satisﬁes a
property speciﬁed in temporal logic under all possible scenarios. In recognition of
non-deterministic systems and the fact that a Boolean answer is not always use-
ful, probabilistic model checking quantiﬁes the probability that a system satisﬁes
a property. In particular, ‘numerical’ (alternatively ‘exact’) probabilistic model
checking oﬀers precise and accurate analysis by exhaustively exploring the state
space of non-deterministic systems and has been successfully applied to a wide
variety of protocols, algorithms and systems. The result of this technique is the
exact (within limits of numerical precision) probability that a system will satisfy
a property of interest, however the exponential growth of the state space limits
its applicability. The typical 108 state limit of exhaustive approaches usually
represents an insigniﬁcant fraction of the state space of real systems that may
have tens of orders of magnitude more states than the number of protons in the
universe (∼1080).
Under certain circumstances it is possible to guarantee the performance of
a system by specifying it in such a way that (particular) faults are impossible.
Compositional reasoning and various symmetry reduction techniques can also be
used to combat state-space explosion, but in general the size, unpredictability
and heterogeneity of real systems [2] make these techniques infeasible. Static
analysis has also been highly successful in analysing and debugging software and
other systems, although it cannot match the precision of quantitative analysis of
dynamic properties achieved using probabilistic and stochastic temporal logic.
While the state space explosion problem is unlikely to ever be adequately
solved for all systems, simulation-based approaches are becoming increasingly
tractable due to the availability of high performance hardware and algorithms.
In particular, statistical model checking (SMC) combines the simplicity of testing
with the formality and precision of numerical model checking; the core idea being
to create multiple independent execution traces of the system and individually
verify whether they satisfy some given property. By modelling the executions
as a Bernoulli random variable and using advanced statistical techniques, such
as Bayesian inference [14] and hypothesis testing [27], the results are combined
in an eﬃcient manner to decide whether the system satisﬁes the property with
some level of conﬁdence, or to estimate the probability that it does. Knowing
a result with less than 100% conﬁdence is often suﬃcient in real applications,
since the conﬁdence bounds may be made arbitrarily tight. Moreover, statistical
model checking may oﬀer the only feasible means of quantifying the performance
of many complex systems. Evidence of this is that statistical model checking has
been used to ﬁnd bugs in large, heterogeneous aircraft systems [2]. Notable sta-
tistical model checking platforms include APMC [11], YMER [28] and VESTA
[23]. Well-established numerical model checkers, such as PRISM [17] and UP-


## Page 3


PAAL [3], are now also including statistical model checking engines to cope with
larger models.
A key challenge facing statistical model checking is to reduce the length (steps
and cpu time) and number of simulation traces necessary to achieve a result
with given conﬁdence. The current proliferation of parallel computer architec-
tures (multiple cpu cores, grids, clusters, clouds and general purpose computing
on graphics processors, etc.) favours statistical model checking by making the
production of multiple independent simulation runs relatively easy. Despite this,
certain models still require a large number of simulation steps to verify a prop-
erty and it is thus necessary to make simulation as eﬃcient as possible. Rare
(unlikely) properties pose a particular problem for simulation-based approaches,
since they are not only diﬃcult to observe (by deﬁnition) but their probability
is diﬃcult to bound [10].
The term ‘rare event’ is ubiquitous in the literature, but here we speciﬁcally
consider rare properties deﬁned in temporal logic. This distinguishes rare states
from rare paths that may or may not contain rare states. The distinction does not
signiﬁcantly alter the mathematical derivation of our algorithm, however it af-
fects the applicability of simple heuristics that are able to ﬁnd (reasonably) good
importance sampling distributions. This is of relevance because our algorithm
works by a process of iterative reﬁnement, starting from an initial distribution
that must produce at least a few traces that satisfy the property. In what fol-
lows we consider discrete space Markov models and present a simple algorithm
to ﬁnd an optimal set of importance sampling parameters, using the concept of
minimum cross-entropy [16,25]. Our parametrisation arises naturally from the
syntactic description of the model and thus constitutes a low dimensional vector
in comparison to the state space of the model. We show that this parametrisa-
tion has a unique optimum and demonstrate its eﬀectiveness on reliability and
(bio)chemical models. We describe the advantages and potential pitfalls of our
approach and highlight areas for future research.
2
Importance sampling
Our goal is to estimate the probability of a property by simulation and bound
the error of our estimation. When the property is not rare there are standard
bounding formulae (e.g., the Chernoﬀand Hoeﬀding bounds [4,12]) that relate
absolute error, conﬁdence and the required number of simulations to achieve
them, independent of the probability of the property. As the property becomes
rarer, however, absolute error ceases to be useful and it is necessary to consider
relative error, deﬁned as the standard deviation of the estimate divided by its
expectation. With Monte Carlo simulation relative error is unbounded with in-
creasing rarity [21], but it is possible to bound the error by means of importance
sampling [24,10].
Importance sampling is a technique that can improve the eﬃciency of sim-
ulating rare events and has been receiving considerable interest of late in the
ﬁeld of statistical model checking (e.g., [5,1]). It works by simulating under an


## Page 4


(importance sampling) distribution that makes a property more likely to be seen
and then uses the results to calculate the probability under the original distri-
bution by compensating for the diﬀerences. The concept arose from work on the
‘Monte Carlo method’ [18] in the Manhattan project during the 1940s and was
originally used to quantify the performance of materials and solve otherwise in-
tractable analytical problems with limited computer power (see, e.g., [15]). For
importance sampling to be eﬀective it is necessary to deﬁne a ‘good’ importance
sampling distribution: (i) the property of interest must be seen frequently in
simulations and (ii) the distribution of the paths that satisfy the property in the
importance sampling distribution must be as close as possible to the distribu-
tion of the same paths in the original distribution (up to a normalising factor).
The literature in this ﬁeld sometimes uses the term ‘zero variance’ to describe
an optimal importance sampling distribution, referring to the fact that with
an optimum importance sampling distribution all simulated paths satisfy the
property and the estimator has zero variance. It is important to note, however,
that a sub-optimal distribution may meet requirement (i) without necessarily
meeting requirement (ii). Failure to consider (ii) can result in gross errors and
overestimates of conﬁdence (e.g. a distribution that simulates just one path that
satisﬁes the given property). The algorithm we present in Section 3 addresses
both (i) and (ii).
Importance sampling schemes fall into two broad categories: state depen-
dent tilting and state independent tilting [6]. State dependent tilting refers to
importance sampling distributions that individually bias (‘tilt’) every transition
probability in the system. State independent tilting refers to importance sam-
pling distributions that change classes of transition probabilities, independent of
state. The former oﬀers greatest precision but is infeasible for large models. The
latter is more tractable but may not produce good importance sampling distri-
butions. Our approach is a kind of parametrised tilting that potentially aﬀects
all transitions diﬀerently, but does so according to a set of parameters.
2.1
Estimators
Let Ωbe a probability space of paths, with f a probability density function
over Ωand z(ω) ∈{0, 1} a function indicating whether a path ω satisﬁes some
property φ. In the present context, z is deﬁned by a formula of an arbitrary
temporal logic over execution traces. The expected probability γ that φ occurs
in a path is then given by
γ =
Z
Ω
z(ω)f(ω) dω
(1)
and the standard Monte Carlo estimator of γ is given by
˜γ =
1
NMC
NMC
X
i=1
z(ωi)


## Page 5


NMC denotes the number of simulations used by the Monte Carlo estimator and
note that z(ωi) is eﬀectively the realisation of a Bernoulli random variable with
parameter γ. Hence Var(˜γ) = γ(1 −γ) and for γ →0, Var(˜γ) ≈γ. Let f ′ be
another probability density function over Ω, absolutely continuous with zf, then
Equation (1) can be written
γ =
Z
Ω
z(ω) f(ω)
f ′(ω)f ′(ω) dω
L = f/f ′ is the likelihood ratio function, so
γ =
Z
Ω
L(ω)z(ω)f ′(ω) dω
(2)
We can thus estimate γ by simulating under f ′ and compensating by L:
˜γ =
1
NIS
NIS
X
i=1
L(ωi)z(ωi)
NIS denotes the number of simulations used by the importance sampling esti-
mator. The goal of importance sampling is to reduce the variance of the rare
event and so achieve a narrower conﬁdence interval than the Monte Carlo esti-
mator, resulting in NIS ≪NMC. In general, the importance sampling distribution
f ′ is chosen to produce the rare property more frequently, but this is not the
only criterion. The optimal importance sampling distribution, denoted f ∗and
deﬁned as f conditioned on the rare event, produces only traces satisfying the
rare property:
f ∗= zf
γ
(3)
This leads to the term ‘zero variance estimator’ with respect to Lz, noting that,
in general, Var(f ∗) ≥0.
In the context of statistical model checking f usually arises from the speciﬁ-
cations of a model described in some relatively high level language. Such models
do not, in general, explicitly specify the probabilities of individual transitions,
but do so implicitly by parametrised functions over the states. We therefore
consider a class of models that can be described by guarded commands [7] ex-
tended with stochastic rates. Our parametrisation is a vector of strictly positive
values λ ∈(R+)n that multiply the stochastic rates and thus maintain the abso-
lutely continuous property between distributions. Note that this class includes
both discrete and continuous time Markov chains and that in the latter case our
mathematical treatment works with the embedded discrete time process.
In what follows we are therefore interested in parametrised distributions and
write f(·, λ), where λ = {λ1, . . . , λn} is a vector of parameters, and distinguish
diﬀerent density functions by their parameters. In particular, µ is the original
vector of the model and f(·, µ) is therefore the original density. We can thus
rewrite Equation (2) as
γ =
Z
Ω
L(ω)z(ω)f(ω, λ) dω


## Page 6


where L(ω) = f(ω, µ)/f(ω, λ). We can also rewrite Equation (3)
f ∗= zf(·, µ)
γ
and write for the optimal parametrised density f(·, λ∗). We deﬁne the optimum
parametrised density function as the density that minimises the cross-entropy
[16] between f(·, λ) and f ∗for a given parametrisation and note that, in general,
f ∗̸= f(·, λ∗).
2.2
The cross-entropy method
Cross-entropy [16] (alternatively relative entropy or Kullback-Leibler divergence)
has been shown to be an eﬀective directed measure of distance between distri-
butions [25]. With regard to the present context, it has also been shown to be
useful in ﬁnding optimum distributions for importance sampling [22,6,19].
Given two probability density functions f and f ′ over the same probability
space Ω, the cross-entropy from f to f ′ is given by
CE(f, f ′) =
Z
Ω
f(ω) log f(ω)
f ′(ω) dω =
Z
Ω
f(ω) log f(ω) −f(ω) log f ′(ω) dω
= H(f) −
Z
Ω
f(ω) log f ′(ω) dω
(4)
where H(f) is the entropy of f. To ﬁnd λ∗we minimise CE(z(ω)f(ω, µ), f(ω, λ)),
noting that H(f(ω, µ)) is independent of λ:
λ∗= arg max
λ
Z
Ω
z(ω)f(ω, µ) log f(ω, λ) dω
(5)
Estimating λ∗directly using Equation (5) is hard, so we re-write it using impor-
tance sampling density f(·, λ′) and likelihood ratio function L(ω) = f(ω, µ)/f(ω, λ′):
λ∗= arg max
λ
Z
Ω
z(ω)L(ω)f(ω, λ′) log f(ω, λ) dω
(6)
Using Equation (6) we can construct an unbiased importance sampling estimator
of λ∗and use it as the basis of an iterative process to obtain successively better
estimates:
˜λ∗= λ(j+1) = arg max
λ
Nj
X
i=1
z(ω(j)
i )L(j)(ω(j)
i
) log f(ω(j)
i , λ)
(7)
N j is the number of simulation runs on the jth iteration, λ(j) is the jth set of
estimated parameters, L(j)(ω) = f(ω, µ)/f(ω, λ(j)) is the jth likelihood ratio
function, ω(j)
i
is the ith path generated using f(·, λ(j)) and f(ω(j)
i , λ) is the
probability of path ω(j)
i
under the distribution f(·, λ(j)).


## Page 7


3
A parametrised cross-entropy algorithm
We consider a system of n guarded commands with vector of rate functions
K = (K1, . . . , Kn) and corresponding vector of parameters λ = (λ1, . . . , λn). In
any given state the probability that command k is chosen is given by
λkKk
⟨K, λ⟩
where the notation ⟨·, ·⟩denotes a scalar product. For the purposes of simulation
we consider a space of ﬁnite paths ω ∈Ω. Let Uk(ω) be the number of transitions
of type k occurring in ω. We therefore have
f(ω, λ) =
n
Y
k
(λk)Uk(ω)
Uk(ω)
Y
s=1
Ks
k
⟨Ks, λ⟩
Here vector K is indexed by s to emphasise its state-dependence. The likelihood
ratios are thus of the form
L(j)(ω) =
n
Y
k
 
µk
λ(j)
k
!Uk(ω) Uk(ω)
Y
s=1
⟨Ks, λ(j)⟩
⟨Ks, µ⟩
We substitute these expressions in the cross-entropy estimator Equation (7) and
for compactness substitute zi = z(ωi), ui(k) = Uk(ωi) and li = L(j)(ωi) to get
arg max
λ
N
X
i=1
lizi log
n
Y
k

λui(k)
k
ui(k)
Y
s=1
Ki,s
k
⟨Ki,s, λ⟩


(8)
= arg max
λ
N
X
i=1
n
X
k
liziui(k)

log(λk) +
ui(k)
X
s=1
log(Ki,s
k ) −
ui(k)
X
s=1
log(⟨Ki,s, λ⟩)


We partially diﬀerentiate with respect to λk and get the non-linear system
∂f
∂λk
(λ) = 0 ⇔
N
X
i=1
lizi

ui(k)
λk
−
|ωi|
X
s=1
Ki,s
k
⟨Ki,s, λ⟩

= 0
(9)
where |ωi| is the length of the path ωi.
Theorem 1. A solution of Equation (9) is almost surely a maximum, up to a
normalising scalar.
Proof. Using a standard result, it is suﬃcient to show that the Hessian matrix
in λ is negative semi-deﬁnite. Consider fi:
fi(λ) =
X
k
ui(k)

log(λk) +
ui(k)
X
s=1
log(Ki,s
k ) −
ui(k)
X
s=1
log(⟨Ki,s, λ⟩)




## Page 8


The Hessian matrix in λ is of the following form with v(s)
k
=
K(s)
k
⟨K(s),λ⟩and vk =
(v(s)
k )1≤s≤Uk(ω):
Hi = G −D
where G = (gkk′)1≤k,k′≤n is the following Gram matrix
gkk′ = ⟨vk, vk′⟩
and D is a diagonal matrix such that
dkk = uk
λ2
k
.
Note that asymptotically dkk =
1
λk
PN
s=1 v(s)
k . We write 1N = (1, . . . , 1) for the
vector of N elements 1, hence
dkk = 1
λk
⟨vk, 1N⟩.
Furthermore, ∀s, Pn
k=1 λkv(s)
k
= 1. So, Pn
k′=1 λk′vk′ = 1N. Finally,
dkk =
n
X
k′=1
λk′
λk
⟨vk, vk′⟩.
Let x ∈Rn. To prove the theorem we need to show that −xtHx ≥0.
−xtHx = xtDx −xtGx
(10)
=
X
k,k′
λk′
λk
⟨vk, vk′⟩x2
k −
X
k,k′
⟨vk, vk′⟩xkxk′
=
X
k<k′
λk′
λk
x2
k + λk
λk′ x2
k′ −2xkxk′

⟨vk, vk′⟩

=
X
k<k′
 r
λk′
λk
xk −
r
λk
λk′ xk′
!2
⟨vk, vk′⟩
≥
0
The Hessian matrix H of f is of the general form
H =
N
X
i=1
liziHi
which is a positively weighted sum of non-positive matrices.
⊓⊔
The Hessian is negative semi-deﬁnite because if λ is a solution then xλ, x ∈R+,
is also a solution. The fact that there is a unique optimum, however, makes it
conceivable to ﬁnd λ∗using standard optimising techniques such as Newton and


## Page 9


quasi-Newton methods. To do so would require introducing a suitable normalis-
ing constraint in order to force the Hessian to be negative deﬁnite. In the case of
the cross-entropy algorithm of [19], this constraint is inherent because it works
at the level of individual transition probabilities that sum to 1 in each state.
We note here that in the case that our parameters apply to individual transi-
tions, such that one parameter corresponds to exactly one transition, Equation
(12) may be transformed to Equation (9) of [19] by constraining ⟨K, λ⟩= 1.
Equation (9) of [19] has been shown in [20] to converge to f ∗, implying that
under these circumstances f(·, λ∗) = f ∗and that it may be possible to improve
our parametrised importance sampling distribution by increasing the number of
parameters.
3.1
The algorithm
Equation (9) leads to the following expression for λk:
λk =
PN
i=1 liziui(k)
PN
i=1 lizi
P|ωi|
s=1
Ks
k
⟨Ks,λ⟩
(11)
In this form the expression is not useful because the right hand side is dependent
on λk in the scalar product. Hence, in contrast to update formulae based on
unbiased estimators, as given by Equation (7) and in [19,6], we construct an
iterative process based on a biased estimator but having a ﬁxed point that is the
optimum:
λ(j+1)
k
=
PNj
i=1 liziui(k)
PNj
i=1 lizi
P|ωi|
s=1
Ks
k
⟨Ks,λ(j)⟩
(12)
Equation (12) can be seen as an implementation of Equation (11) that uses the
previous estimate of λ in the scalar product, however it works by reducing the
distance between successive distributions, rather than by explicitly reducing the
distance from the optimum. We oﬀer no proof of convergence here, but assert
that if it converges it converges to λ∗.
To use the algorithm it is necessary to start with an initial simulation dis-
tribution f(·, λ(0)) and number of simulations N0 that produce at least a few
traces that satisfy the property. The choice of λ(0) and N0 is highly dependent
on the model and the property and must in general be established by heuristics
or trial and error. When the number of parameters is small and the property
is very rare, an eﬀective strategy is to iterate the algorithm with relatively low
N0 and random parameters until a suitable trace is observed. If the model and
property are similar to a previous combination for which parameters were found,
those parameters are likely to provide a good initial estimate. Increasing the pa-
rameters associated to obviously small rates may help (along the lines of simple
failure biasing [24]), however the rareness of a property expressed in temporal
logic may not always be related to low probabilities. Finding good initial distri-
butions for arbitrary systems and temporal properties is the subject of ongoing
work.


## Page 10


Given a suﬃcient number of traces from the ﬁrst iteration, Equation 12
should provide a better set of parameters. The expected behaviour is that on
successive iterations the number of traces that satisfy the property increases,
however it is important to note that the algorithm optimises the quality of the
distribution and that the number of traces that satisfy the property is merely
emergent of that. As has been noted, in general f(·, λ∗) ̸= f ∗, hence it is likely
that fewer than 100% of traces will satisfy the property when simulating under
f(·, λ∗). One consequence of this is that an initial set of parameters may produce
more traces that satisfy the property than the ﬁnal set (see, e.g., Figure 4).
It is conceivable that certain guarded commands play no part in traces that
satisfy the property, in which case Equation (12) would make the corresponding
parameter zero with no adverse eﬀects. It is also conceivable that an important
command is not seen on a particular iteration, but making its parameter zero
would prevent it being seen on any subsequent iteration. To avoid this it is
necessary to adopt a ‘smoothing’ strategy [19] that reduces the signiﬁcance of
an unseen command without setting it to zero. The strategy adopted for the
examples shown below is to divide the parameter of unseen commands by two.
The eﬀects of this can be seen in Figure 6. An alternative approach is to add
a small fraction of the initial (or previous) parameters to every new parameter
estimate. Whatever the strategy, since the parameters are unconstrained it is
advisable to normalise them after each iteration (i.e., P
k λk = const.) in order
to judge progress.
Once the parameters have converged it is then possible to perform a ﬁnal
set of simulations to estimate the probability of the rare property. The usual as-
sumption is that Nj ≪NIS ≪NMC, however it is often the case that parameters
converge fast, so it is expedient to use some of the simulation runs generated
during the course of the optimisation as part of the ﬁnal estimation.
4
Examples
The following examples are included to illustrate the performance of our algo-
rithm and parametrisation. The ﬁrst is an example of a chemical system, often
used to motivate stochastic simulation, while the second is a standard repair
model. All simulations were performed using our statistical model checking plat-
form, PLASMA [13].
4.1
Chemical network
Following the success of the human genome project, with vast repositories of
biological pathway data available online, there is an increasing expectation that
formal methods can be applied to biological systems. The network of chemi-
cal reactions given below is abstract but typical of biochemical systems and
demonstrates the potential of statistical model checking to handle the enormous
state spaces of biological models. In particular, we demonstrate the eﬃcacy of


## Page 11


our algorithm by applying it to quantify two rare dynamical properties of the
system.
We consider a well stirred chemically reacting system comprising ﬁve reac-
tants (molecules of type A, B, C, D, E), a dimerisation reaction (13) and two
decay reactions (14,15):
A + B
k1
→C
(13)
C
k2
→D
(14)
D
k3
→E
(15)
Under the assumption that the molecules move randomly and that elastic colli-
sions signiﬁcantly outnumber unreactive, inelastic collisions, the system may be
simulated using mass action kinetics as a continuous time Markov chain [8]. The
semantics of Equation (13) is that if a molecule of type A encounters a molecule
of type B they will combine to form a molecule of type C after a delay drawn
from an exponential distribution with mean k1. The decay reactions have the
semantics that a molecule of type C (D) spontaneously decays to a molecule of
type D (E) after a delay drawn from an exponential distribution with mean k2
(k3). The reactions (13,14,15) are modelled by three guarded commands having
importance sampling parameters λ1, λ2 and λ3, respectively. A typical simula-
tion run is illustrated in Figure 1, where the x-axis is steps rather than time to
aid clarity. A and B combine rapidly to form C which peaks before decaying
slowly to D. The production of D also peaks while E rises monotonically.
0
500
1500
2500
0
200
600
1000
Steps
Number of molecules
A,B
C
D
E
Fig. 1. A typical stochastic simulation
trace of reactions (13-15).
970
975
980
985
990
995
x
Probability
(i)
(ii)
10−28
10−18
10−8
460
465
470
475
480
485
y
Fig. 2. (i) Pr[♦C ≥x] (ii) Pr[♦D ≥y]
With an initial vector of molecules (1000, 1000, 0, 0, 0), corresponding to types
(A, B, C, D, E), the state space contains ∼1015 states. We know from a static
analysis of the reactions that it is possible for the numbers of molecules of C
and D to reach the initial number of A and B molecules (i.e., 1000) and that


## Page 12


this is unlikely. To ﬁnd out exactly how unlikely we consider the probabilities of
the following rare properties deﬁned in linear temporal logic: (i) ♦C ≥x, x ∈
{970, 975, 980, 985, 990, 995} and (ii) ♦D ≥y, y ∈{460, 465, 470, 475, 480, 485}.
The results are plotted in Figure 2.
To establish an initial distribution our algorithm (Equation (12)) was iter-
ated with random parameters and N0 = 1000 until one or more traces were
observed that satisﬁed the property in question. No more than 10 such itera-
tions were needed in any case. The algorithm was then iterated 20 times using
Nj = 1000. Despite the large state space, this value of Nj was found to be suf-
ﬁcient to produce reliable results. Starting from randomly chosen initial values,
the convergence of parameters can be seen in Figure 3. Figure 4 illustrates that
the number of paths satisfying a property can actually decrease as the quality
of the distribution improves. Figure 5 illustrates the convergence of the estimate
and sample variance using the importance sampling parameters generated dur-
ing the course of running the algorithm. The initial set of parameters appear to
give a very low variance, however this is clearly erroneous with respect to sub-
sequent values. Noting that the variance of standard Monte Carlo simulation of
rare events gives a variance approximately equal to the probability and assuming
that the sample variance is close to the true variance, Figure 5 suggests that we
have made a variance reduction of approximately 107.
0
5
10
15
20
Iteration
0.4
1.0
1.4
λ1
λ2
λ3
Fig. 3. Convergence of parameters for
♦D ≥470 in the chemical model using
Nj = 1000.
0
5
10
15
20
Iteration
Number of true paths
400
600
1000
Fig. 4. Convergence of number of paths
satisfying ♦D ≥470 in the chemical
model using Nj = 1000.
4.2
Repair model
To a large extent the need to certify system reliability motivates the use of formal
methods and thus reliability models are studied extensively in the literature. The
following example is taken from [19] and features a moderately large state space
of 40,320 states that can be investigated using numerical methods to corroborate
our results.


## Page 13


0
5
10
15
20
Iteration
10−36
10−17 10−10
Probability
Variance
Fig. 5. Convergence of probability and
sample variance for ♦D ≥470 in the
chemical model using Nj = 1000.
0
5
10
15
20
Iteration
10−9
10−4
1
10
λ2
λ4
λ6
λ8
λ10
λ12
Fig. 6.
Convergence
of
parameters
(dashed/solid
lines)
and
eﬀect
of
smoothing strategy (circles) in repair
model using Nj = 10000.
The system is modelled as a continuous time Markov chain and comprises
six types of subsystems (1, . . . , 6) containing, respectively, (5, 4, 6, 3, 7, 5) com-
ponents that may fail independently. The system’s evolution begins with no
failures and with various probabilistic rates the components fail and are re-
paired. The failure rates are (2.5ǫ, ǫ, 5ǫ, 3ǫ, ǫ, 5ǫ), ǫ = 0.001, and the repair rates
are (1.0, 1.5, 1.0, 2.0, 1.0, 1.5), respectively. Each subsystem type is modelled by
two guarded commands: one for failure and one for repair. The property under
investigation is the probability of a complete failure of a subsystem (i.e., the
failure of all components of one type), given an initial condition of no failures.
This can be expressed in temporal logic as Pr[X(¬init U failure)].
Figure 6 shows the convergence of parameters (dashed/solid lines) and high-
lights the eﬀects of the adopted smoothing strategy (circles). Parameters λ2 and
λ4 (the parameters for repair commands of types 1 and 2, respectively) are at-
tenuated from the outset by the convergence of the other parameters (because
of the normalisation). Once their values are small relative to the normalisation
constant (12 in this case), their corresponding commands no longer occur and
their values experience exponential decay as a result of smoothing (division by
two at every subsequent step). Parameters λ6 and λ10 (the parameters for repair
commands of types 3 and 5, respectively) converge for 12 steps but then also
decay. The parameters for the repair commands of types 4 and 6 (solid lines)
are the smallest of the parameters that converge. The fact that the repair tran-
sitions are made less likely by the algorithm agrees with the intuition that we
are interested in direct paths to failure. The fact that they are not necessarily
made zero reinforces the point that the algorithm seeks to consider all paths to
failure, including those that have intermediate repairs.
Figure 7 plots the number of paths satisfying X(¬init U failure) and sug-
gests that for this model the parametrised distribution is close to the optimum.
Figure 8 plots the estimated probability and sample variance during the course
of the algorithm and superimposes the true probability calculated by PRISM
[26]. The long term average agrees well with the true value (an error of -1.7%,


## Page 14


based on an average excluding the ﬁrst two estimates), justifying our use of the
sample variance as an indication of the eﬃcacy of the algorithm: our importance
sampling parameters provide a variance reduction of more than 105.
0
5
10
15
20
0
2000
6000
10000
Iteration
Number of true paths
Fig. 7. Convergence of number of paths
satisfying X(¬init U failure) in the re-
pair model using Nj = 10000.
0
5
10
15
20
Iteration
10−12
10−9
10−6
Probability
Variance
Fig. 8. Convergence of estimated prob-
ability and sample variance for repair
model using Nj = 10000. True proba-
bility shown as horizontal line.
5
Conclusions and future work
Statistical model checking addresses the state space explosion associated with
exact probabilistic model checking by estimating the parameters of an empirical
distribution of executions of a system. By constructing an executable model,
rather than an explicit representation of the state space, SMC is able to quantify
and verify the performance of systems that are intractable to an exhaustive
approach. SMC trades certainty for tractability and often oﬀers the only feasible
means to certify real-world systems. Rare properties pose a particular problem to
Monte Carlo simulation methods because the properties are diﬃcult to observe
and the error in their estimated probabilities is diﬃcult to bound. Importance
sampling is a well-established means to reduce the variance of rare events but
requires the construction of a suitable importance sampling distribution without
resorting to the exploration of the entire state space.
We have devised a natural parametrisation for importance sampling and have
provided a simple algorithm, based on cross-entropy minimisation, to optimise
the parameters for use in statistical model checking. We have shown that our
parametrisation leads to a unique optimum and have demonstrated that with
very few parameters our algorithm can make signiﬁcant improvements in the
eﬃciency of statistical model checking. We have shown that our approach is
applicable to standard reliability models and to the kind of huge state space
models found in systems biology. We therefore anticipate that our methodology
has the potential to be applied to many complex natural and man-made systems.


## Page 15


An ongoing challenge is to ﬁnd ways to accurately bound the error of results
obtained by importance sampling. Speciﬁcally, the sample variance of the results
may be a very poor indicator of the true variance (i.e. with respect to the un-
known true probability). Recent work has addressed this problem using Markov
chain coupling applied to a restricted class of models and logic [1], but a simple
universal solution remains elusive. A related challenge is to ﬁnd precise means
to judge the quality of the importance sampling distributions we create. Our
algorithm ﬁnds an optimum based on an automatic parametrisation of a model
described in terms of guarded commands. This description is usually derived
from a higher level syntactic description that is likely optimised for compactness
rather than consideration of importance sampling. As such, there may be alter-
native, equivalent ways of describing the model that produce better importance
sampling distributions. Applying existing work on the robustness of estimators
(see, e.g., Chapter 4 in [21]), we hope to adapt our algorithm to provide hints
about improved parametrisation.
References
1. Benoˆıt Barbot, Serge Haddad, and Claudine Picaronny. Coupling and Importance
Sampling for Statistical Model Checking. In Cormac Flanagan and Barbara K¨onig,
editors, TACAS’12, Lecture Notes in Computer Science, Tallinn, Estonia, March
2012. Springer. To appear.
2. Ananda Basu, Saddek Bensalem, Marius Bozga, Benoˆıt Caillaud, Benoˆıt Delahaye,
and Axel Legay. Statistical abstraction and model-checking of large heterogeneous
systems. In John Hatcliﬀand Elena Zucca, editors, Formal Techniques for Dis-
tributed Systems, volume 6117 of Lecture Notes in Computer Science, pages 32–46.
Springer Berlin / Heidelberg, 2010.
3. Johan Bengtsson, Kim Larsen, Fredrik Larsson, Paul Pettersson, and Wang Yi.
Uppaal a tool suite for automatic veriﬁcation of real-time systems. In Rajeev Alur,
Thomas Henzinger, and Eduardo Sontag, editors, Hybrid Systems III, volume 1066
of Lecture Notes in Computer Science, pages 232–243. Springer Berlin / Heidelberg,
1996.
4. Herman Chernoﬀ. A Measure of Asymptotic Eﬃciency for Tests of a Hypothesis
Based on the sum of Observations. Ann. Math. Statist., 23(4):493–507, 1952.
5. Edmund Clarke and Paolo Zuliani. Statistical model checking for cyber-physical
systems. In Tevﬁk Bultan and Pao-Ann Hsiung, editors, Automated Technology
for Veriﬁcation and Analysis, volume 6996 of Lecture Notes in Computer Science,
pages 1–12. Springer Berlin / Heidelberg, 2011.
6. P.-T. De Boer, V.F. Nicola, and R.Y. Rubinstein. Adaptive importance sampling
simulation of queueing networks.
In Winter Simulation Conference, volume 1,
pages 646–655, 2000.
7. Edsger W. Dijkstra. Guarded commands, nondeterminacy and formal derivation
of programs. Commun. ACM, 18:453–457, August 1975.
8. D. T. Gillespie. Exact stochastic simulation of coupled chemical reactions. Journal
of Physical Chemistry, 81:2340–2361, 1977.
9. P. Godefroid, M. Levin, and Molnar. D. Automated whitebox fuzz testing. In
NDSS, 2008.


## Page 16


10. Philip Heidelberger.
Fast simulation of rare events in queueing and reliability
models. ACM Trans. Model. Comput. Simul., 5:43–85, January 1995.
11. Thomas H´erault, Richard Lassaigne, Fr´ed´eric Magniette, and Sylvain Peyronnet.
Approximate probabilistic model checking. In Bernhard Steﬀen and Giorgio Levi,
editors, Veriﬁcation, Model Checking, and Abstract Interpretation, volume 2937 of
Lecture Notes in Computer Science, pages 307–329. Springer Berlin / Heidelberg,
2004.
12. Wassily Hoeﬀding. Probability Inequalities for Sums of Bounded Random Vari-
ables. Journal of the American Statistical Association, 58(301):13–30, March 1963.
13. Cyrille J´egourel, Axel Legay, and Sean Sedwards. A Platform for High Performance
Statistical Model Checking – PLASMA. In Cormac Flanagan and Barbara K¨onig,
editors, TACAS, Lecture Notes in Computer Science, Tallinn, Estonia, March 2012.
Springer. To appear.
14. Sumit K. Jha and et al.
A Bayesian Approach to Model Checking Biological
Systems. In 7th. Intl. Conf. on Computational Methods in Systems Biology, pages
218–234. Springer-Verlag, 2009.
15. H. Kahn. Stochastic (Monte Carlo) Attenuation Analysis. Technical Report P-88,
Rand Corporation, July 1949.
16. S. Kullback. Information Theory and Statistics. Dover, 1968.
17. Marta Kwiatkowska, Gethin Norman, and David Parker. PRISM: Probabilistic
Symbolic Model Checker.
In Tony Field, Peter Harrison, Jeremy Bradley, and
Uli Harder, editors, Computer Performance Evaluation: Modelling Techniques and
Tools, volume 2324 of Lecture Notes in Computer Science, pages 113–140. Springer
Berlin / Heidelberg, 2002.
18. N. Metropolis and S. Ulam. The Monte Carlo Method. Journal of the American
Statistical Association, 44(247):335–341, September 1949.
19. Ad Ridder. Importance sampling simulations of markovian reliability systems using
cross-entropy. Annals of Operations Research, 134:119–136, 2005.
20. Ad Ridder. Asymptotic optimality of the cross-entropy method for markov chain
problems. Procedia Computer Science, 1(1):1571 – 1578, 2010.
21. Gerardo Rubino and Bruno Tuﬃn, editors. Rare Event Simulation using Monte
Carlo Methods. Wiley, 2009.
22. R. Rubinstein.
The Cross-Entropy Method for Combinatorial and Continuous
Optimization. 1:127–190, 1999.
23. K. Sen, M. Viswanathan, and G. A. Agha. VESTA: A statistical model-checker
and analyzer for probabilistic systems. In QEST, pages 251–252. IEEE, September
2005.
24. Perwez Shahabuddin. Importance Sampling for the Simulation of Highly Reliable
Markovian Systems. Management Science, 40(3):333–352, March 1994.
25. J. Shore and R. Johnson. Axiomatic derivation of the principle of maximum en-
tropy and the principle of minimum cross-entropy. IEEE Transactions on Infor-
mation Theory, 26(1):26–37, January 1980.
26. The PRISM website. www.prismmodelchecker.org.
27. H. Younes and R. Simmons. Probabilistic veriﬁcation of discrete event systems
using acceptance sampling. In Computer Aided Veriﬁcation, volume 2404, pages
23–39. Springer, 2002.
28. H˚akan Younes. YMER: A Statistical Model Checker. In Kousha Etessami and
Sriram Rajamani, editors, Computer Aided Veriﬁcation, volume 3576 of Lecture
Notes in Computer Science, pages 171–179. Springer Berlin / Heidelberg, 2005.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1201_5229v1_cross_entropy_optimisation_of_importance_sampling_parameters_for_statistical_mod
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2012/1201_5229V1_CROSS_ENTROPY_OPTIMISATION_OF_IMPORTANCE_SAMPLING_PARAMETERS_FOR_STATISTICAL_MOD.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

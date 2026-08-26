---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1304.5404v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1304.5404v3_A_scalable_computational_framework_for_establishing_long-term_behavior_of_stocha

> Source: 1304.5404v3_A_scalable_computational_framework_for_establishing_long-term_behavior_of_stocha.pdf

> Pages: 31

---


## Page 1


A scalable computational framework for establishing long-term
behavior of stochastic reaction networks
Ankit Gupta, Corentin Briat, Mustafa Khammash∗
Department of Biosystems Science and Engineering (D-BSSE),
Swiss Federal Institute of Technology–Z¨urich (ETH-Z), 4058 Basel, Switzerland
Corresponding author; e-mail: mustafa.khammash@bsse.ethz.ch
November 6, 2018
Abstract
Reaction networks are systems in which the populations of a ﬁnite number of species evolve through
predeﬁned interactions. Such networks are found as modeling tools in many biological disciplines such
as biochemistry, ecology, epidemiology, immunology, systems biology and synthetic biology. It is now
well-established that, for small population sizes, stochastic models for biochemical reaction networks are
necessary to capture randomness in the interactions.
The tools for analyzing such models, however,
still lag far behind their deterministic counterparts. In this paper, we bridge this gap by developing
a constructive framework for examining the long-term behavior and stability properties of the reaction
dynamics in a stochastic setting. In particular, we address the problems of determining ergodicity of
the reaction dynamics, which is analogous to having a globally attracting ﬁxed point for deterministic
dynamics. We also examine when the statistical moments of the underlying process remain bounded with
time and when they converge to their steady state values. The framework we develop relies on a blend of
ideas from probability theory, linear algebra and optimization theory. We demonstrate that the stability
properties of a wide class of biological networks can be assessed from our suﬃcient theoretical conditions
that can be recast as eﬃcient and scalable linear programs, well-known for their tractability. It is notably
shown that the computational complexity is often linear in the number of species. We illustrate the
validity, the eﬃciency and the wide applicability of our results on several reaction networks arising in
biochemistry, systems biology, epidemiology and ecology. The biological implications of the results as
well as an example of a non-ergodic biological network are also discussed.
1
arXiv:1304.5404v3  [q-bio.MN]  5 May 2014


## Page 2


Author Summary
In many biological disciplines, computational modeling of interaction networks is the key for understand-
ing biological phenomena. Such networks are traditionally studied using deterministic models. However,
it has been recently recognized that when the populations are small in size, the inherent random ef-
fects become signiﬁcant and to incorporate them, a stochastic modeling paradigm is necessary. Hence,
stochastic models of reaction networks have been broadly adopted and extensively used. Such models,
for instance, form a cornerstone for studying heterogeneity in clonal cell populations.
In biological applications, one is often interested in knowing the long-term behavior and stability
properties of reaction networks even with incomplete knowledge of the model parameters. However for
stochastic models, no analytical tools are known for this purpose, forcing many researchers to use a
simulation-based approach, which is highly unsatisfactory. To address this issue, we develop a theoret-
ical and computational framework for determining the long-term behavior and stability properties for
stochastic reaction networks. Our approach is based on a mixture of ideas from probability theory, lin-
ear algebra and optimization theory. We illustrate the broad applicability of our results by considering
examples from various biological areas. The biological implications of our results are discussed as well.
Introduction
Reaction networks are used as modeling tools in many areas of science. Examples include chemical re-
action networks [1], cell signalling networks [2], gene expression networks [3], metabolic networks [4],
pharmacological networks [5], epidemiological networks [6] and ecological networks [7]. Traditionally, re-
action networks are mathematically analyzed by representing the dynamics as a set of ordinary diﬀerential
equations. Such a deterministic model is reasonably accurate when the number of network participants is
large. However, when this is not the case, the discreteness in the interactions becomes important and the
dynamics inherently noisy. This random component of the dynamics cannot be ignored as it can strongly
inﬂuence the system’s behavior [8–10]. To understand the eﬀects of this randomness, stochastic mod-
els are needed, and the most common approach is to model the reaction dynamics as a continuous-time
Markov process. The most common approach is to model the dynamics as a continuous-time Markov pro-
cess whose states denote the current population size. Many recent works have employed such stochastic
models to study the impact of noise [11–14].
In stochastic models, the underlying Markov process (X(t))t≥0 is a pure-jump process whose state
space S contains all the population size vectors that are reachable by the random dynamics. The prob-
ability distribution of (X(t))t≥0 evolves according to a system of linear ordinary diﬀerential equations
(ODEs), known as the Chemical Master Equation (CME) or Forward Kolmogorov Equation [15]. The
dimension of the system of ODEs is equal to the number of elements in the state space S, with each
element representing a possible combination of reacting species abundances. When S is ﬁnite and small
in size, the CME can be solved analytically since it is simply a small and ﬁnite system of linear diﬀerential
equations. However, for inﬁnite state-spaces an exact solution to the CME is diﬃcult to obtain except
in some special cases [17,22]. Beyond these special cases, current methods often rely on truncating the
inﬁnite state-space to obtain ﬁnite approximations of the CME [23], and then resorting to eﬃcient numer-
ical methods for their solutions. Such methods include Expokit [18], which is based on Krylov Subspace
Identiﬁcation, or the backward Euler method proposed in [19], among others. Such an approach works
well only for relatively small systems, as the curse-of-dimensionality renders the numerical solution of the
truncated master equation of larger systems prohibitive. Nevertheless, recent methods based on Tensor
Train (TT) and Quantized Tensor Train (QTT) representations [20,21] show that for CME problems that
admit bounded TT ranks, storage costs and computational complexity that grow linearly in the number
of species may be achieved. These and other methods for the numerical solutions of the CME remain
active topics of research.
2


## Page 3


When S is inﬁnite or very large in size, the most common approach for approximating the solutions of a
CME is by simulating a large number of trajectories of the underlying Markov process (X(t))t≥0, and using
the sample values of X(t) to estimate the distribution at time t. Such simulations are performed using
Monte Carlo procedures such as Gillespie’s stochastic simulation algorithm (SSA) or its variants [24–26].
Since the simulation time of SSA depends linearly on the number of reactions that occur during the
simulation time period, these procedures can be cumbersome for large networks. It is well-known that
the stochastic eﬀects caused by the random timing of reactions become less important when the population
size is large. The dynamical law of large numbers proved by Kurtz [27] shows that under an appropriate
scaling relationship between the population size, reaction rates and the system size, the stochastic model
of a reaction network converges to the deterministic model, as the system size goes to inﬁnity. Under this
scaling relationship, one can also approximate the stochastic dynamics with certain stochastic diﬀerential
equations (SDEs) that are easier to simulate and analyze [28, 29]. However, these SDE approximations
can only work when the population sizes of all the species in the reaction network are large, which is
often not the case. For a detailed survey on the topic of estimating the solution of a CME, we refer the
readers to the paper [30] which contains an exhaustive list of methods for this purpose.
In many biological applications, one in interested in analyzing the long-term behavior or stability
properties of a reaction network. This is fairly straightforward for deterministic models because many
tools from the theory of ordinary diﬀerential equations can be used for this analysis [31]. However, the
stability properties of stochastic models for reaction networks are diﬃcult to verify for the following
reasons. Let us consider a stochastic reaction network whose dynamics is represented by the Markov
process (X(t))t≥0 with state space S. The evolution of the distributions of this Markov process is given
by (p(t))t≥0 which is the solution of the CME corresponding to the reaction network. Heuristically, we
regard the stochastic dynamics to be stable when the family of distributions (p(t))t≥0 is “well-behaved”
with time. In this paper, we consider several notions of “well-behaved” dynamics. The strongest of these
notions is the concept of ergodicity [32] which means that there exists a unique stationary distribution π for
the Markovian dynamics, such that p(t) →π as t →∞, irrespective of the initial distribution p(0). This is
analogous to having a globally attracting ﬁxed point in the deterministic setting. If S is ﬁnite, the process
is ergodic if and only if it is irreducible, in the sense that all the states in S are reachable from each other.
It is hence enough to check irreducibility of the process using e.g. matrix methods [33, 34]. Contrary
to this situation, our main interest in this paper is in analyzing the stability properties of stochastic
reaction networks with an inﬁnite state space S. Note that in such cases, irreducibility no longer implies
ergodicity, since the trajectories of the Markov process may blow up with time (see the carcinogenesis
example in the discussion section). In this regard, ergodicity cannot be considered as a generic property
of reaction networks with inﬁnite state-spaces since both ergodic and non-ergodic processes can be found
in nature. Assuming ergodicity without verifying it beforehand seems to be therefore unreasonable from
both theoretical and practical perspectives. The direct veriﬁcation of stability properties like ergodicity is
generally not possible as the CME cannot be explicitly solved, except in some restrictive cases [17,22]. The
common approach of using Monte Carlo simulations for estimating the solutions of a CME is inadequate
for assessing the long-term behavior and stability properties of a stochastic reaction network, because
one can only simulate ﬁnitely many trajectories and those too for a ﬁnite amount of time. Some methods
for analyzing stability properties without the need for simulations exist, but they either work for speciﬁc
networks [16,22], very special classes of networks such as zero-deﬁciency networks [35], or assume system
size approximations where the stochastic dynamics is represented by an SDE [36,37]. Such system size
approximations do not hold when some species are present in low copy numbers, and even if they hold,
the approximation error generally blows up with time [29].
Hence the stochastic dynamics and the
corresponding SDE may have completely diﬀerent long-term behaviors. Our aim, in this paper, is to
develop a theoretical and computational framework for analyzing the long-term behavior and stability
properties of stochastic models for reaction networks that do not rely on computationally expensive
Monte Carlo simulations or on system size approximations of the stochastic dynamics. A similar goal
3


## Page 4


is also achieved in the works [38, 39] where results on stability and moments bounds are also obtained.
The approach proposed in [40] is built upon a Foster-Lyapunov criterion [32] and a quadratic Foster-
Lyapunov function in order to estimate the location of the stationary distribution. In the same, yet
diﬀerent, spirit, the proposed approach also relies on a Foster-Lyapunov condition but using a linear
Foster-Lyapunov function that allows us to establish ergodicity, moment bounds, moment convergence
and the existence of attractive sets for moments. While the approach in [40] is fully computational, the
one we propose is also theoretical and allows us to conclude on structural properties of classes of networks
such as structural ergodicity, structural boundedness of moments and structural convergence of moments.
Our approach relies on a mixture of simple ideas from stochastic analysis, linear algebra, polynomial
analysis and optimization. Even though our conditions are only suﬃcient, we demonstrate their broad
applicability by successfully establishing stability properties of several reaction networks taken from the
literature.
We mentioned before that the stochastic and the deterministic models of a reaction network are
connected through the dynamical law of large numbers [27]. It might be tempting to think that the
stability properties of a stochastic model can be assessed by studying the stability properties of the
corresponding deterministic model.
However in general, the stochastic and deterministic models can
have very diﬀerent stability properties.
This is because a deterministic model cannot capture noise
induced eﬀects which may have a signiﬁcant impact on the long-term behavior of a system. For example,
in the synthetic Toggle Switch by Gardener [41], the deterministic model exhibits bistability and hence
starting from diﬀerent initial values, the system can converge to two diﬀerent steady states. On the
other hand, the corresponding stochastic model is ergodic (see network (35)) and hence the solution of
the CME converges to the same stationary distribution irrespective of the initial distribution. A similar
phenomenon occurs with the repressilator (see [42] and network (36)), where the stochastic model is
ergodic while the deterministic model exhibits oscillations. On the other hand, it is also possible to
ﬁnd networks for which the deterministic model has a locally asymptotically stable equilibrium point,
implying that whenever the initial condition is contained within its region of attraction, the trajectories
converge to it. If the initial condition lies outside this region of attraction, then the trajectories of such a
network become unbounded with time. In the stochastic setting, the randomness causes each trajectory
to leave the region of attraction in ﬁnite time, and then become unbounded suggesting that there is
no stationary distribution for the dynamics (see network (22) and Figure 1). This lack of stationary
distribution is because the stochastic dynamics can jump potential wells from one macroscopic ﬁxed
point which is stable to another ﬁxed point which is unstable [43]. A more striking example of divergent
deterministic and stochastic behaviors is given by network (26) (see also Figure 2). While the deterministic
model has a unique globally stable ﬁxed point, the stochastic model is non-ergodic and all the moments
grow unboundedly with time. In this example it is impossible to predict the stochastic behavior from
the deterministic model. The above examples illustrate that the stability properties of the stochastic
dynamics can, in general, not be assessed from the stability properties of the deterministic dynamics.
Our results can help in understanding the stability properties of the moments of a Markov process
(X(t))t≥0 representing a reaction network. In particular, we present a method to check if these moments
remain bounded with time and if they converge to their steady state values as time goes to inﬁnity. Such
results can help in verifying the suitability of a model for a given system and in designing biological con-
trollers that drive the moments to speciﬁc steady state values. We provide easily computable bounds for
the moments that hold uniformly in time. We also determine bounds for the steady state moment values,
which can help in understanding the properties of the steady state distribution, even if this distribution
is not explicitly computable. In many biological applications, it is of great interest to explicitly compute
the ﬁrst few moments of the process (X(t))t≥0 without solving the corresponding CME. One can easily
express the dynamics of these moments as a system of ordinary diﬀerential equations, but generally this
system is not closed when the network has nonlinear interactions. Many moment closure methods that
suggest schemes to close these equations to obtain approximations for the moments have been proposed
4


## Page 5


(see e.g. [44,45] and references therein). The results obtained in this paper can be used to ascertain the
correctness of a given moment closure method for a speciﬁc network (see the example based on the net-
work (29)). Furthermore, several moment closure methods are developed under an implicit assumption
that the moment-generating function corresponding to the solution of the CME exists for all times. One
of our results provides a way to easily check that this assumption is indeed valid.
Reaction networks. Let us now formally describe reaction networks. Motivated by the literature
on chemical kinetics, we refer to the network participants as molecules which may belong to one of d
species S1, . . . , Sd. There are K reactions in the network and for any k = 1, . . . , K, the stoichiometric
vector ζk = (ζk,1, . . . , ζk,d) denotes the change in the number of molecules in each of the species due to
the k-th reaction.
Deterministic models. Consider the deterministic model for the reaction network described above.
In this setting, the state of the system is described by a vector of concentrations of the d species which we
denote by κ ∈Rd
≥0. The concentration of a species is simply its molecular count divided by the system
volume. Let ˜λk(κ) be the ﬂux associated with the k-th reaction (see [8]). To ensure positivity of the
system, we require that ˜λk(κ) = 0 whenever κi = 0 and ζk,i < 0. If the initial state is κ0, then the
evolution of concentrations is given by (φκ0(t))t≥0 which satisﬁes the Reaction Rate Equations (RRE) of
the form
dφκ0(t)
dt
=
K
X
k=1
˜λk(φκ0(t))ζk with φκ0(0) = κ0.
(1)
We are interested in the long-term behavior and stability of our reaction dynamics. More precisely, we
would like to check if the following conditions are satisﬁed.
DC1 For any κ0, there is a compact set K(κ0) such that φκ0(t) ∈K(κ0) for all t ≥0.
DC2 There exists a compact set K0 such that for any κ0, we have φκ0(t) ∈K0 for large values of t.
DC3 There is a κeq such that for any κ0 we have φκ0(t) →κeq as t →∞.
The ﬁrst condition, DC1, says that for any κ0, the entire trajectory (φκ0(t))t≥0 stays within some compact
set. We would expect this to be true for most realistic systems. Hence a violation of this property may
suggest a ﬂaw in the deterministic model. The second condition, DC2, says that there is an attractor set
for the dynamics, where all the trajectories eventually lie, irrespective of their starting point. The last
condition, DC3, says that there is a globally attracting ﬁxed point for the deterministic model. Using
techniques from the theory of dynamical systems [31, 46], one can verify these conditions, without the
need of simulating the deterministic model. There is also a general theory to check condition DC3 for
reaction networks satisfying mass-action kinetics (see [47–50]). Broadly speaking, these three conditions
present diﬀerent ways of saying that the reaction dynamics is “well-behaved”. Our goal in this paper is
to develop a theoretical and computational framework for verifying conditions similar to DC1, DC2 and
DC3 for stochastic models of reaction networks.
Stochastic models. Consider the stochastic model corresponding to the reaction network described
above. In this setting, the ﬁring of reactions are discrete events and the state of the system refers to the
vector of molecular counts of the d species. When the state is x, the k-th reaction ﬁres after a random
time which is exponentially distributed with rate λk(x). The functions λ1, . . . , λK are known as the
propensity functions in the literature. To ensure positivity of the system, we require that if x + ζk /∈Nd
0,
then λk(x) = 0, where N0 is the set of non-negative integers. The dynamics can be represented by the
Markov process (Xx0(t))t≥0 where x0 is the initial state. Note that if Xx0(t) = (X1(t), . . . , Xd(t)), then
Xi(t) is the number of molecules of Si at time t.
It is important to select a suitable state space S for the Markov process representing the reaction
dynamics. We choose S to be a non-empty subset of Nd
0 satisfying the following properties:
5


## Page 6


(A) If x ∈S and λk(x) > 0 for some k = 1, . . . , K, then x + ζk ∈S.
(B) There is no proper subset S1 ⊂S satisfying part (A).
Observe that part (A) ensures that if x0 ∈S then Xx0(t) ∈S for all t ≥0 and hence S can be taken to
be the state space of all the Markov processes describing the stochastic reaction network with an initial
state x0 in S. Part (B) implies that the reaction dynamics cannot be contained in a proper subset of S.
The role of this assumption will become clear in the next section, when we discuss the issue of state space
irreducibility. Note that in certain cases, such as the pure-birth network ∅−−⇀S1, a suitable state space
satisfying the above criteria cannot be found. There also exist cases where the above criteria restricts
the choice of state space. For example, for the pure-death network S1 −−⇀∅, the only possible choice
for state space is S = {0}. Finally we remark that if the reactions in a network satisfy a conservation
relation then the state space must be chosen with an initial condition in mind. For example, for the
network S1 ⇌S2, the sum of molecular counts of S1 and S2 is preserved by the reactions. Hence if we
wish to study the stochastic dynamics with the initial sum as n, then the correct choice for state space
is S = {(x1, x2) ∈N2
0 : x1 + x2 = n}.
Let P(S) denote the space of probability distributions over S, endowed with the weak topology which
is metrized by the Prohorov metric (see [51]). For any x, y ∈S let px(t, y) denote the following probability
px(t, y) = P (Xx(t) = y) .
(2)
Deﬁning px(t)(A) = P
y∈A px(t, y), for any A ⊂S, we can view px(t) as an element in P(S). In fact,
px(t) is the distribution at time t of the Markov process (Xx(t))t≥0. The dynamics of px(t) is given by
the Chemical Master Equation (CME) which has the following form:
dpx(t, y)
dt
=
K
X
k=1
(px(t, y −ζk)λk(y −ζk) −px(t, y)λk(y)) ,
(3)
where px(0, y) = 1 if x = y and px(0, y) = 0 for all y ̸= x. Theoretically, one can ﬁnd px(t, y) for any t ≥0
and y ∈S, by solving this system. However this system consists of as many equations as the number of
elements in S. Hence an explicit solution is only possible when S is ﬁnite, which only happens in very
restrictive cases where all the reactions preserve some conservation relation. Typically, S is inﬁnite and
solving this system analytically or even numerically is nearly impossible, except in some restrictive cases
(see [17]). From now on, we assume that S is inﬁnite.
The above discussion shows that at the level of distributions, we can view the stochastic dynamics
(Xx0(t))t≥0 as the deterministic dynamics (px0(t))t≥0, which satisﬁes the CME. However, the major
diﬃculty in analyzing this deterministic dynamics is that it occurs over an inﬁnite dimensional space
P(S). Nevertheless we can recast the conditions DC1, DC2 and DC3 in the stochastic setting as below.
SC1 For any x0, there is a compact set K(x0) ⊂P(S) such that px0(t) ∈K(x0) for all t ≥0.
SC2 There exists a compact set K0 ⊂P(S) such that for any x0 ∈S we have px0(t) ∈K0 for large
values of t.
SC3 There is a π ∈P(S) such that for any x0 we have px0(t) →π as t →∞.
Each of the above conditions give an important insight about the long-term behavior and stability of
the stochastic dynamics. The ﬁrst condition, SC1, says that for every ϵ ∈(0, 1) we can ﬁnd a ﬁnite set
Aϵ ⊂S such that each px0(t) puts at least (1 −ϵ) of its mass in Aϵ. In other words, the probability
that the state of the underlying Markov process at any time t is inside Aϵ is greater than (1 −ϵ). We
would expect this to be true for most realistic models. If condition SC2 holds then the evolution of
distributions have a compact attractor set in P(S), where all the trajectories eventually lie irrespective
6


## Page 7


of their starting point. This suggests that in the long run, the family of processes {(Xx0(t))t≥0 : x0 ∈S},
spend most of their time on the same set of states. The last condition SC3 says that the evolution of
distributions have a globally attracting ﬁxed point π. If this holds, then the Markov process representing
the reaction dynamics is ergodic with π as the unique stationary distribution. For understanding the
long-term behavior of a stochastic process, ergodicity is a desirable property to have. In the long-run, the
proportion of time spent by any trajectory of an ergodic process, in any subset of the state space is equal
to the stationary probability of that subset (see (12)). In other words, information about the stationary
distribution can be obtained by observing just one trajectory for a suﬃciently long time. Such a result can
have important applications. For example, consider a culture with a large number of identical cells with
each cell having the same reaction network. If we can show that this intracellular network is ergodic, then
by observing the long-term reaction dynamics in a single cell, using for example. time-lapse microscopy,
we can obtain statistical information about all the cells at stationarity. Conversely, ergodicity allows us
to obtain the stationary distribution of a single-cell by observing the distribution over the population,
using for example ﬂow cytometry.
In this paper we develop a general framework for checking conditions SC1, SC2 and SC3. How-
ever, the scope of our paper is broader than that. As mentioned in the introduction, we obtain easily
computable bounds for the statistical moments of the underlying Markov process and investigate when
these moments converge with time. We also present conditions for the distribution of the process to be
light-tailed.
Results
Preliminaries
In this section we discuss the main results of our paper.
In particular, we explain how conditions
SC1, SC2 and SC3 can be veriﬁed without having to simulate the trajectories of the Markov process
representing the reaction dynamics. Intuitively, these conditions can only hold if the Markov process
has a low probability of hitting states that have a very large size. In our case, the states are vectors in
Rd and so we can measure their size by using any norm on Rd. The central theme of this paper is to
demonstrate that for many networks, long-term behavior can be easily analyzed by choosing the right
norm for measuring the state sizes. This right norm has the form
∥x∥v =
d
X
i=1
vi|xi|,
(4)
where v is a positive vector in Rd satisfying the following condition.
Condition 1 (Drift-Diﬀusivity Condition) For a positive vector v ∈Rd, there exist positive con-
stants c1, c2, c3, c4 and a nonnegative constant c5 such that for all x ∈S
K
X
k=1
λk(x)⟨v, ζk⟩≤c1 −c2⟨v, x⟩and
(5a)
K
X
k=1
λk(x)⟨v, ζk⟩2 ≤c3 + c4⟨v, x⟩+ c5⟨v, x⟩2.
(5b)
Here ⟨·, ·⟩denotes the standard inner product on Rd. If we consider the process (∥Xx0(t)∥v)t≥0, then its
dynamics can be seen to have two components drift and diﬀusion which have the form PK
k=1 λk(x)⟨v, ζk⟩
and PK
k=1 λk(x)⟨v, ζk⟩2 respectively when Xx0(t) = x (see page 2 in the Supplementary Material S1).
7


## Page 8


Condition 1 gives upper-bounds for the magnitude of these two components and hence we call it the
drift-diﬀusivity condition (abbreviated to Condition DD from now on; the abbreviations DD1 and DD2
stand for the ﬁrst and second inequality, respectively). Observe that when the process (∥Xx0(t)∥v)t≥0
goes above c1/c2 then it experiences a negative drift, suggesting that it will move downwards. This fact
will be crucial for our analysis.
For now, we assume that a vector v satisfying Condition DD has been found.
In later sections
we demonstrate how v can be determined for a large class of networks by solving suitably constructed
optimization problems.
For any positive integer r, let mr
x0(t) denote the r-th moment of ∥Xx0(t)∥v deﬁned by
mr
x0(t) = E (∥Xx0(t)∥r
v) =
X
y∈S
∥y∥r
vpx0(t, y).
(6)
Similarly let Ψr(x0, t) denote the r-th moment of Xx0(t) at time t. Then Ψr(x0, t) is a tensor of rank r
whose entry at index (i1, . . . , ir) ∈{1, 2, . . . , d}r is given by
Ψr
i1...ir(x0, t) =
X
y∈S
yi1 . . . yirpx0(t, y),
(7)
where y = (y1, . . . , yd) and px0(t) is the distribution of Xx0(t).
Suppose that for some positive constants r and Cr(x0) we have
sup
t≥0
mr
x0(t) ≤Cr(x0).
(8)
For any M > 0, let KM be the compact (ﬁnite) set deﬁned by KM = {x ∈S : ∥x∥v ≤M} and let Kc
M
denote its complement. Markov’s inequality (see [52]) implies that for any ϵ > 0 we can choose M large
enough to satisfy
sup
t≥0
px0(t, Kc
M) = sup
t≥0
P (∥Xx0(t)∥r
v > M r) ≤sup
t≥0
E (∥Xx0(t)∥r
v) ≤Cr(x0)
M r
< ϵ.
Hence Prohorov’s theorem (see Chapter 3 in [51]) ensures that condition SC1 holds. Similarly we can
prove that condition SC2 will hold if for some r > 0 there exists a constant ˆCr such that
lim sup
t→∞mr
x0(t) ≤ˆCr for all x0 ∈S.
(9)
Relations (8) and (9) give uniform and asymptotic upper-bounds for mr
x0(t). Using these relations we
can also obtain uniform and asymptotic upper-bounds for the entries of Ψr(x0, t). Such moment bound
results have applications in queuing theory and control theory (see [53]). In Theorem 2 we show that
under certain conditions, (8) and (9) hold and the upper-bounds can be easily computed.
Instead of the r-th moment of the process (∥Xx0(t)∥v)t≥0, one can ask if the exponential moment of
this process is uniformly bounded from above. This will happen if for some γ > 0 we have
sup
t≥0
E

eγ∥Xx0(t)∥v
= sup
t≥0
X
y∈S
eγ∥y∥vpx0(t, y) < ∞.
(10)
If (10) holds, then the distribution px0(t) is light-tailed (a distribution is called light-tailed if its tails are
majorized by an exponential decay) uniformly in t. This shows that all the cumulants of the distribution
px0(t) exist, which is an important result for the following reason.
There is a considerable body of
research dedicated to estimating the moments of the process (Xx0(t))t≥0 directly without computing the
distribution functions px0(t). For any integer r > 0, one can easily write the diﬀerential equations for
8


## Page 9


the dynamics of the ﬁrst r moments. However when the reaction network has nonlinear interactions, this
system of equations is not closed for any r. Various moment closure methods (see [54, 55]) exist that
specify ways to close these equations artiﬁcially and estimate the moments approximately. A popular
moment closure method is the cumulant-neglect method which ignores the higher order cumulants of the
distribution px0(t) for all t ≥0. Of course this method is only valid when the higher order cumulants
exist. This is guaranteed if (10) holds. In Theorem 3 we give conditions for verifying (10).
We now come to the question of checking condition SC3 which says that the process (Xx0(t))t≥0 is
ergodic. This can only happen if the state space S is irreducible, which means that all the states are
accessible from each other. Recall the deﬁnition of px(t, y) from (2). Mathematically, we say that S is
irreducible if for all x, y ∈S, we have px(t1, y) > 0 and py(t2, x) > 0 for some t1, t2 > 0. In order to check
the irreducibility of S, one has to verify that there is no proper subset S1 ⊂S, such that once the process
reaches a state in S1, it stays in S1 forever. For reaction networks with mass-action kinetics, methods
for checking irreducibility have recently been reported in [56] and [57]. These methods can be extended
to situations where the propensity functions are positive in the positive orthant. When the propensity
functions vanish inside the positive orthant, the problem of checking irreducibility can become much more
complicated, and to the best of our knowledge no methods exist in the literature for this purpose.
We mentioned before that the vector v is chosen so that the process (∥Xx0(t)∥v)t≥0 has a negative
drift at large values. Assuming irreducibility, this is suﬃcient to verify ergodicity of (Xx0(t))t≥0 (see
Proposition 4).
Suppose that condition SC3 is satisﬁed and the process (Xx0(t))t≥0 is ergodic with stationary dis-
tribution π. For any positive integer r, let Πr denote the r-th moment of the stationary distribution π.
Then Πr is a tensor of rank r deﬁned in the same way as Ψr(x0, t) (see (7)), with px0(t, y) replaced by
π(y). Using Theorem 2 we can determine the values of r for which Πr is ﬁnite (componentwise) and
Ψr(x0, t) →Πr as t →∞(see Theorem 5). We can also identify functions f : S →R for which
lim
t→∞E(f(Xx0(t))) =
X
y∈S
f(y)π(y) < ∞
(11)
holds for any x0 ∈S. If f is such a function, then the ergodic theorem for Markov processes (see [58])
says that
lim
t→∞
1
t
Z t
0
f(Xx0(s))ds =
X
y∈S
f(y)π(y) almost surely,
(12)
for any x0 ∈S. Lastly, we also obtain conditions to check if the stationary distribution π is light-tailed
(see Theorem 6).
General Results
In this section, we formally present the main results of our paper. Their proofs are given in the Supple-
mentary Material S1.
Moment bounds. Our ﬁrst result establishes that for certain values of r, we can obtain uniform
and asymptotic moment bounds for the r-th moment of the process (∥Xx0(t)∥v)t≥0.
Theorem 2 Assume that Condition DD holds. Let rmax be given by
rmax =
 1 + 2c2
c5
if c5 > 0
∞
if c5 = 0.
(13)
For any positive integer r, if r < rmax then there exist positive constants Cr(x0) and ˆCr such that (8)
and (9) hold.
9


## Page 10


The values of the constants Cr(x0) and ˆCr can be explicitly computed using a recursive relationship (see
the Supplementary Material S1). Note that if v = (v1, . . . , vd), then for any y = (y1, . . . , yd) ∈S we have
yi ≤∥y∥v/vi for any i. Hence for any i1, . . . , ir ∈{1, 2, . . . , d} we have Ψr
i1...ir(x0, t) ≤mr
x0(t)/ Qr
j=1 vij
Therefore using Theorem 2, we can obtain uniform and asymptotic moment bounds for the reaction
dynamics (Xx0(t))t≥0 (see the Supplementary Material S1).
Observe that if c5 = 0 then rmax = ∞. In this case, Theorem 2 says that for each positive integer r
and x0 ∈S there exists a constant Cr(x0) such that (8) holds. By showing that we have a C > 0 such
that Cr(x0) ≤r!Cr for all positive integers r, we obtain our next result, which gives suﬃcient conditions
to check (10).
Theorem 3 (Uniform Light-Tailedness) Suppose that Condition DD holds with c5 = 0. Given an
initial state x0 ∈S there exists a γ > 0 such that
sup
t≥0
E

eγ∥Xx0(t)∥v
= sup
t≥0
X
y∈S
eγ∥y∥vpx0(t, y) < ∞.
Ergodicity and Moment Convergence.
The next result veriﬁes the ergodicity of a reaction
network satisfying Condition DD. It follows from Theorem 7.1 in Meyn and Tweedie [59].
Proposition 4 (Ergodicity) Assume that the state space S of the Markov process (Xx0(t))t≥0 is ir-
reducible and Condition DD1 holds. Then this process is exponentially ergodic in the sense that there
exists a unique distribution π ∈P(S) along with constants B, c > 0 such that for any x0 ∈S
sup
A⊂S
|px0(t, A) −π(A)| ≤Be−ct for all t ≥0.
This result says that as t →∞, the distribution px0(t) converges to π exponentially fast. Henceforth we
assume that the process (Xx0(t))t≥0 is ergodic with stationary distribution π.
Let f : S →R be a function such that for some positive integer r < (rmax −1), there exists a C > 0
satisfying |f(x)| ≤C(1 + ∥x∥r
v) for all x ∈S. Using Theorem 2 we can prove that for such a f, the
relations (11) and (12) hold. As a consequence we obtain the following result about the convergence of
moments with time.
Theorem 5 (Moment Convergence) Assume that Condition DD holds. Let r be any positive integer
satisfying r < (rmax −1). Then Πr is ﬁnite (componentwise) and Ψr(x0, t) →Πr as t →∞.
If f(x) = ∥x∥r
v then Theorem 2 and (11) imply that for any positive integer r < (rmax −1) there exists a
positive constant ˆCr such that
X
y∈S
∥y∥r
vπ(y) ≤ˆCr.
(14)
In particular, if c5 = 0 then rmax = ∞and (14) holds for each r. By proving the existence of a constant
C > 0 such that ˆCr ≤r!Cr for all positive integers r we get our last result which shows that the stationary
distribution is light-tailed.
Theorem 6 (Light-Tailedness at stationarity) Suppose that Condition DD holds with c5 = 0. Then
there exists a γ > 0 such that
X
y∈S
eγ∥y∥vπ(y) < ∞.
The framework described above is very general and can be applied to any network that satisﬁes
Condition DD. In what follows, we specialize the results for two wide classes of networks with mass-
action kinetics, namely reaction networks with monomolecular and bimolecular reactions. It will be,
however, pointed out in the examples that the scope of our approach is much broader since more general
propensities, such as those involving Hill functions or more general mass-action kinetics, can be considered.
10


## Page 11


Methods
Using the analytical tools developed in the previous sections, several general results can be stated for
the class of unimolecular reaction networks and bimolecular reaction networks. In what follows, when
we say that a moment is bounded, we mean that it is bounded uniformly in time (as in (8)).
This
can be established using Theorem 2 once Condition DD is veriﬁed. Furthermore, when we say that
a moment is globally converging, we mean that it converges to its equilibrium value as time tends to
inﬁnity, irrespective of the initial state x0. Once, Condition DD is veriﬁed, this can established using
Theorem 5.
The main aim of the section is to develop a theoretical and computational framework for checking
Condition DD.
Results for stochastic unimolecular reaction networks
Let us then consider a unimolecular reaction network which involves d species that interact through K
reaction channels of the form:
∅
ki
0
−−⇀
Si,
Si
k0
i
−−⇀
∅,
Si
kℓ
i
−−⇀
Pd
j=1 νjℓ
i Sj
(15)
where i = 1, . . . , d, ℓ∈{1, . . . , Ni}, Ni > 0 and νjℓ
i
∈N0. The reaction rates ki
0, k0
i and kℓ
i are positive
real numbers. In accordance with (3), the reactions are indexed from n = 1 to K, and corresponding
propensities and stoichiometries are denoted by λn(x) and ζn, respectively.
Motivations. The unimolecular case may seem quite restrictive at ﬁrst sight and not of particular
practical interest. We demonstrate below that, on the contrary, the proposed results on unimolecular re-
action networks complete existing ones and are, therefore, of practical and theoretical interests. Although
some explicit solutions for the CME are indeed known for some particular unimolecular reactions [17], it
is still unknown whether the CME admits an closed-form solution for all possible type of unimolecular
reactions. Note that we assume here that no simpliﬁcation nor assumption is made on the problem, we
are dealing with the very general unimolecular case.
The results developed of this section are useful in several ways. First of all, all types of unimolecular
reactions can be handled with the proposed approach, making it more general than existing ones in this
regard. Moreover, given a speciﬁc reaction network, the method allows one to establish whether a unique
stationary distribution exists without solving the CME. This is particularly important since unimolecular
networks may not be ergodic. In this case, the network can exhibit unstable behaviour which may suggest
a ﬂaw in the model if the considered real-world system exhibits stable trajectories. Moreover, in certain
design applications such as those in synthetic biology, it seems natural to design networks that have
well-behaved dynamics.
Checking ergodicity provides a convenient way to determine if the network
dynamics is well-behaved. Note, furthermore, that it is, in general, diﬃcult to infer ergodicity directly
from the solution of the CME (when it is known) since proving the existence of a unique globally attractive
stationary distribution amounts to check convergence of the solution to the CME to the same distribution
for all possible initial distributions, which are in inﬁnite number in our setup. This fact is even more true
when large networks are considered since the explicit form of the solution to the CME is, in this case,
very intricate [17]. The proposed results allow one to circumvent this diﬃculty and demonstrate that
ergodicity can be assessed by very simple means, i.e. using basic notions of linear algebra. The results
can be furthermore used to assess the structural ergodicity of a reaction network, that is, the ergodicity
of a network for any combination of the rate parameters, by very simple means. This very strong and
practically relevant notion is extremely diﬃcult, again, to check from the solution of the CME since it
would require to check the convergence of the solution of the CME to the same stationary distribution
for all initial conditions and all positive values of the rate parameters, a very cumbersome task, even for
11


## Page 12


small networks. Finally, the results pertaining on unimolecular networks will also turn out to play an
important role in the ergodicity analysis of bimolecular reaction networks.
Theoretical results. Let us start with several theoretical results that characterize the long-term
behavior of unimolecular networks of the form (15).
Proposition 7 (Ergodicity of unimolecular networks) Let us consider the general unimolecular re-
action network (15) and assume that the state-space of the underlying Markov process is irreducible. Let
the matrices A ∈Rd×d and b ∈Rd
≥0, ||b|| ̸= 0, be further deﬁned as
K
X
n=1
λn(x)⟨v, ζn⟩= x⊺Av + b⊺v.
(16)
Then, the following statements are equivalent:
1. The matrix A is Hurwitz-stable, i.e. all its eigenvalues lie in the open left half-plane.
2. There exists a vector v ∈Rd
>0 such that Av < 0.
Moreover, when one of the above statements holds, the Markov process describing the reaction network is
exponentially ergodic and all the moments are bounded and globally converging.
⋄
The above result shows that, for unimolecular networks, ergodicity and the existence of moment bounds
can be directly inferred from the properties of the matrix A deﬁned in (16). The second statement, which
characterizes the Hurwitz-stability of A in an implicit way, will turn out to play a key role in the analysis
of unimolecular and bimolecular reaction networks since checking whether Av < 0 for some v > 0 is a
linear programming problem.
It is important to stress that, in the result above, if we simply demand that the moments be bounded
and converging, then A may be allowed to have zero eigenvalues in certain cases. Note, however, that
the moments will converge to values that may depend on the initial conditions.
In the case that the structure of the network (the reactions and the stoichiometries) is exactly known,
but that the reaction rates are subject to uncertainties, the above theorem can be robustiﬁed to account
for these uncertainties. To this aim, suppose that the matrix A depends on a vector δ ∈[−1, 1]η where
η ∈N is the number of distinct uncertain parameters. We write this matrix as A(δ) and assume that
there exists a matrix A+ ∈Rd×d satisfying the following properties:
1. A(δ) ≤A+ (in the componentwise sense) for all δ ∈[−1, 1]η
2. There exists a δ∗∈[−1, 1]η such that A+ = A(δ∗).
Note that such a matrix A+ may not exist, especially when some entries are not independent. However,
when A+ exists we have the following result.
Proposition 8 (Robust ergodicity) Let us consider the general unimolecular reaction network (15)
described by some uncertain matrices A(δ) and b(δ), ||b(δ)|| ̸= 0. Assume further the matrix A(δ) admits
the upper-bound A+ deﬁned above and that the state-space of the underlying Markov process is irreducible
for all uncertain parameter values δ ∈[−1, 1]η. Then, the following statements are equivalent:
1. The matrix A(δ) is Hurwitz-stable for all δ ∈[−1, 1]η.
2. The matrix A+ is Hurwitz-stable.
3. There exists a positive vector v ∈Rd such that A+v < 0.
Moreover, when one of the above statements holds, the Markov process describing the reaction network is
robustly exponentially ergodic and all the moments are bounded and globally converging.
⋄
12


## Page 13


Observe that checking the Hurwitz-stability property of each A(δ) is equivalent to checking it for only
A+. Hence we can conclude that, in this case, checking ergodicity of a family of networks is not more
complicated than checking ergodicity of a single network. The case when the matrix A+ is not deﬁned is
more complicated and is discussed in the supplementary material S1.
Computational results. We now present several computational results that accompany the theoret-
ical results of the previous section. It is possible to extract many computational results from our general
framework, but for simplicity we only address the problems of checking ergodicity and computing the
ﬁrst-order moment bounds. The asymptotic ﬁrst-order moment bound, deﬁned in Theorem 2, is given
by bC1 = c1/c2. So the question arises: what is the smallest value for such a ratio? Or, in other words,
what is the smallest attractive compact set for the ﬁrst-order moment of ⟨v, X(t)⟩? Several numerical
methods, solving exactly or approximately this problem, are discussed in the supplementary material S1.
One of them is the following optimization problem which is fully equivalent to Proposition 7:
Optimization problem 9 Let us consider the general unimolecular reaction network (15) and assume
that the state-space of the underlying Markov process is irreducible. Assume further that the optimization
problem
maxz,v z
s.t.
z > 0, v > ε
(zI + A)v ≤0
(17)
is feasible with (z∗, v∗) as minimizer. Then, we have bC∗
1 ≤b⊺v∗/z∗and Proposition 7 holds.
A striking feature about the above optimization program is that the numbers of variables and con-
straints are given by d + 1 and 2d + 1, respectively. This means that the optimization problem scales
linearly with respect to the number of species (d) in the network, and is independent of the number of
reactions K. Therefore, from the point of view of this optimization problem, the size of a unimolecu-
lar network can be identiﬁed with the number of species, and not the number of reactions. The above
optimization problem can be eﬃciently solved using a bisection algorithm over z that is globally and
geometrically converging to z∗. Each iteration consists of solving a linear program, a class of optimiza-
tion problems known to be very tractable, and for which numerous advanced solvers exist [60]. These
properties, altogether, make the overall approach highly scalable, which is necessary for dealing with very
large networks.
Results for stochastic bimolecular reaction networks
Similar results are now presented for stochastic bimolecular reaction networks which, in addition to the
unimolecular reactions (15), also involve bimolecular reactions of the form:
Si + Sj
kℓ
ij
−−⇀
Pd
m=1 νmℓ
ij Sm,
Si + Sj
k0
ij
−−⇀
∅
(18)
where i, j = 1, . . . , d, ℓ∈{1, . . . , Nij}, Nij > 0, and νmℓ
ij
∈N0. The reaction rates kℓ
ij and k0
ij are positive
real numbers.
Theoretical results for bimolecular networks. When bimolecular reaction networks of the form
(15)-(18) are considered, the left-hand side of condition (5a) can be expressed as
K
X
i=1
λk(x)⟨v, ζk⟩= x⊺M(v)x + x⊺Av + b⊺v
(19)
where M(v) ∈Rd×d is symmetric, A ∈Rd×d and b ∈Rd
≥0. Let S :=
ζ1
. . .
ζK

be the stoichiometry
matrix of the bimolecular reaction network (15)-(18), and let Sq be the restriction of S to bimolecular
reactions, only. Further deﬁne a set
Nq :=

v ∈Rd : v > 0, v⊺Sq = 0
	
.
13


## Page 14


When v ∈Nq, the quadratic term x⊺M(v)x in (19) vanishes, and equation (19) reduces to
K
X
i=1
λk(x)⟨v, ζk⟩= x⊺Av + b⊺v
which is exactly the same expression as in the case of unimolecular networks. This means that, with
the additional constraint that v ∈Nq, all the results derived for unimolecular networks directly apply to
bimolecular networks as well. This allows us to obtain the following result.
Proposition 10 (Ergodicity of bimolecular networks) Let us consider the bimolecular reaction net-
work of the form (15)-(18) such that ||b|| ̸= 0 in (19) and assume that the state-space of the underlying
Markov process is irreducible. Assume further that the network admits a non-empty Nq.
If there exists a vector v ∈Nq such that the inequality Av < 0 holds, then the stochastic bimolecular
reaction network (15)-(18) is ergodic and all the moments are bounded and globally converging.
⋄
It is important to mention that the existence of a non-empty set Nq is a prerequisite for utilizing the
above result. Non-emptiness of Nq is equivalent to the existence of a conservation relation for all the
bimolecular reactions, i.e. the value of (at least) a positive linear combination of the species populations
remains unchanged when any of the bimolecular reactions ﬁres. Note that this deﬁnition extends to more
general mass-action kinetics as well. A necessary condition for the non-emptiness of Nq is that Sq is not
full-row rank. This non-emptiness condition may seem restrictive at ﬁrst sight, but it will be shown that
several important reaction networks from the literature satisfy this condition.
Whenever Nq is empty or there is no v ∈Nq such that Av < 0 holds, the next result can be used.
Proposition 11 (Ergodicity of bimolecular networks) Let us consider the bimolecular reaction net-
work of the form (15)-(18) such that ||b|| ̸= 0 in (19) and assume that the state-space of the underlying
Markov process is irreducible. Assume further that one of the following statements holds:
1. There exists v ∈Rd
>0 such that Av < 0 and M(v) ≤0 hold.
2. There exists v ∈Rd
>0 such that M(v) is negative deﬁnite.
Then, the stochastic bimolecular reaction network (15)-(18) is ergodic and all the moments up to order
(⌊1 + 2c2/c5⌋−2) are bounded and globally converging.
⋄
In the above result, the ﬁrst statement can be checked using a linear program since the inequalities are
componentwise. Checking the second statement, however, requires a semideﬁnite program, which is a
more general convex program, that can be solved using solvers such as SeDuMi [61] and SDPT3 [62].
More details on the above result can be found in the supplementary material S1.
Computational results for bimolecular networks. It is shown here that, once again, the theo-
retical results can be easily turned into linear programs that can be checked in a very eﬃcient way. The
following result is the numerical translation of Proposition 10.
Optimization problem 12 Let us consider a bimolecular reaction network (15)-(18) and assume that
the state-space of the underlying Markov process is irreducible. Assume further that Nq ̸= ∅and that the
optimization problem
maxz,v z
s.t.
z > 0, v > ε
(zI + A)v ≤0
v⊺Sq = 0.
(20)
is feasible with (z∗, v∗) as minimizer. Then, we have bC∗
1 ≤b⊺v∗/z∗and Proposition 10 holds.
14


## Page 15


The computational complexity of this optimization problem scales linearly with the number of species
and can therefore be solved for large networks.
The following optimization problem is the computational counterpart of the ﬁrst statement of Propo-
sition 11.
Optimization problem 13 Let us consider a bimolecular reaction network of the form (15)-(18) and
assume that the state-space of the underlying Markov process is irreducible. Assume further that the
nonlinear optimization problem
maxz,v z
s.t.
z > 0, v > ε
(zI + A)v ≤0
M(v) ≤0.
(21)
is feasible with (z∗, v∗) as minimizer. Then, we have bC∗
1 ≤b⊺v∗/z∗and Proposition 11 holds.
The above optimization problem does not scale as nicely as (20) since, in the worst case, the number
of constraints related to M(v) is quadratic in the number of species. The problem, however, remains
tractable due to the linear programming structure.
Qualitative diﬀerences between deterministic and stochastic dynamics
In this section we illustrate that stochastic and deterministic models of the same reaction network may
exhibit very diﬀerent qualitative behaviors. Therefore assessing ergodicity or the convergence of moments
of a stochastic model from the stability properties of the corresponding deterministic model is, in general,
incorrect. To support this claim, we consider two reaction networks.
Jumping potential wells
Our ﬁrst example shows that stochastic dynamics can jump potential wells and leave the stability
regions of the deterministic dynamics, resulting in an unstable behavior. Consider the following reaction
network:
∅
αβ
−−⇀
S
S
α+β
−−⇀
∅
S + S
1
−−⇀
3S
(22)
where 0 < α < β. The deterministic dynamics for this network is given by
˙κ = f(κ) := κ2 −(α + β)κ + αβ
(23)
where κ ∈R≥0 denotes the concentration of S. The ﬁxed points for the dynamics are κ−= α and
κ+ = β, respectively. From the graph {(κ, f(κ)) ∈R≥0 × R : κ ∈R≥0}, it is immediate that the ﬁxed
point κ−= α is locally asymptotically stable with the region of attraction as [0, β) while the other ﬁxed
point κ+ = β is unstable.
We now consider the stochastic version of this network and let A be the generator of the corresponding
Markov process. For the identity function f(x) = x we have
Af(x) = 1
2x2 −

α + β + 1
2

x + αβ
(24)
The polynomial on the right-hand side has two positive roots that are
x± = α + β + 1
2 ±
s
α + β + 1
2
2
−2αβ.
(25)
15


## Page 16


This means that for all x ∈N0 satisfying x ≥1 + x+, we have Af(x) ≥ε, for some ε > 0, implying that
the drift is positive. So if the state of the state of the network reaches a value that is greater than 1+x+,
then there is a possibility that the trajectories become unbounded with time.
To demonstrate this, we pick α = 7/2 and β = 21/2. In such a case, the largest root of the polynomial
on the right-hand side of (24) is x+ =
 29 +
√
547

/2 ≃26.194 > β. We can see that the region where
the drift Af(x) is negative is actually larger than the region of attraction of the locally asymptotically
stable ﬁxed point for the deterministic dynamics. This is due to the fact that the propensity function of
the bimolecular reaction diﬀers from whether we are in the deterministic or in the stochastic setting.
Let us now set the initial condition κ0 = 0 for the deterministic model and x0 = 0 for the stochastic
one.
Note that they both lie within the region of attraction of the ﬁxed point of the deterministic
dynamics and in the region of negative drift for the stochastic dynamics. We then perform 1000 SSA
runs over 100 seconds and stop the simulation when the propensity function x(x−1)/2 of the bimolecular
reaction exceeds the value corresponding to 15000 molecules (approx. 1.12 × 108). At this rate value,
the bimolecular reaction ﬁres, on average, every 10−8 seconds, leading to an explosion of the state of the
system and to unbounded trajectories. Out of 1000 SSA runs, all were stopped before the end of the
simulation time-period (100 seconds). This behavior strongly indicates that the system is not ergodic
despite the the fact that the deterministic model has a locally asymptotically stable ﬁxed point. Figure
1 illustrates the above discussion.
Figure 1: Trajectory of the state of the deterministic system (23) with initial condition
κ0 = 0 (top); Sample path of the Markov process describing the network (22) with initial
condition x0 = 0 (bottom). Whereas the trajectory of the state of the deterministic model converges
to a stationary value, the trajectory of the state of the stochastic model goes unbounded.
Globally stable deterministic dynamics does not imply moments stability
16


## Page 17


In the previous example, the stochastic and deterministic behaviors were diﬀerent, but one can still
understand stochastic instability through the deterministic model. The deterministic dynamics posseses a
region in which the solutions explode and the randomness in the stochastic dynamics allows it to enter this
region in ﬁnite time and grow unbounded thereafter. We now present an example which is more striking in
the sense that the deterministic model cannot be used in any way to infer the instability of the stochastic
model. In this example, the deterministic dynamics has a unique ﬁxed point which is exponentially stable,
while the stochastic dynamics is not ergodic with all its moments growing unboundedly with time.
Consider the reaction network given by
∅
1
−−⇀
S1
∅
1
−−⇀
S2
S1 + S2
1
−−⇀
∅.
(26)
Let κ ∈R2
≥0 be the vector of concentrations. The state of the deterministic model evolves according to
˙κ1(t)
=
1 −κ1(t)κ2(t)
˙κ2(t)
=
1 −κ1(t)κ2(t).
(27)
Assume that the initial conditions satisfy κ2(0)−κ1(0) = α, for some α ∈R. Then we have the following
result.
Theorem 14 The unique equilibrium point of the dynamics (27) given by
κ∗
1 = 1
2

−α +
p
α2 + 4

and κ∗
2 = 1
2

α +
p
α2 + 4

.
(28)
is globally exponentially stable.
In the stochastic setting, the picture is completely diﬀerent as the next result indicates.
Theorem 15 The Markov process corresponding to the stochastic model of network (26) is not ergodic
and all its moments grow unboundedly with time. Moreover, if X1(0) −X2(0) = α for some α > 0, we
have that E[X1(t) −X2(t)] = α for all t ≥0.
To illustrate this result, we simulate the deterministic and the stochastic process (10000 SSA runs)
for κ1(0) = 0, κ1(0) = α, X1(0) = 0, X2(0) = α and α = 2. The results are shown in Figure 2.
Finding an attractive compact set for the ﬁrst-order moments
The goal of this section is to compute a compact set that is attractive for the ﬁrst-order moment of
⟨v, X(t)⟩using the optimization problems (17) or (20). Due to the moment closure problem [54], analytical
expressions for the steady-state values of the moments of bimolecular reaction networks are not available,
and hence this is an important class of networks to analyze. Consider the following bimolecular reaction
network
∅
k
−−⇀
S1,
S1
γ1
−−⇀
∅
S1 + S1
k12
−−⇀
S2,
S2
k21
−−⇀
S1 + S1
S2
γ2
−−⇀
∅.
(29)
representing a dimerization process, i.e.
S1 dimerizes to S2.
It is easily seen that this network is
irreducible since any point in the state-space can be reached from any other point in a ﬁnite number
of reactions having nonzero propensities.
Choosing v in Nq, e.g.
v⊺=
1
2
, yields that c∗
1 = k
and c∗
2 = min{γ1, γ2}, hence the network is exponentially ergodic, and all the moments are bounded and
converging. On solving the optimization problem (20) with numerical values k = 1, γ1 = γ2 = 0.2, k12 = 1
17


## Page 18


Figure 2: Comparison of the trajectories of the deterministic and stochastic (ﬁrst-order
moments) models of the reaction network (26) with initial condition κ1(0) = 0, κ2(0) = 2,
X1(0) = 0 and X2(0) = 2 for the deterministic (top) and stochastic dynamics (bottom),
respectively. We can see that while the deterministic trajectories converge to their equilibrium point,
the ﬁrst-order moments grow without bound.
and k21 = 0.1, we get that ˆC1 = c∗
1/c∗
2 = 5 which coincides with the theoretical value k/ min{γ1, γ2}. One
can regard {(x1, x2) ∈R2
>0 : v⊺x ≤ˆC1} to be an attractive compact set in which the ﬁrst-order moments
of ⟨v, X(t)⟩eventually lie. To validate this calculation, Monte-Carlo simulations were performed which
yield
lim
t→∞E[⟨v, X(t)⟩] = 5.024 ± 0.05,
(30)
showing the correctness of the attractive compact set. To further illustrate this result, several trajectories
of E[X1(t)] and E[X2(t)] for diﬀerent initial conditions are plotted in Figure 3.
We now discuss how the computation of an attractive compact set for the ﬁrst-order moments can be
used to assess whether a closure method leads to a result that is consistent with the stochastic dynamics.
The idea is to check whether the closed system converges towards a value which lies within the compact
set. Let us consider the reaction network (29) and close the ﬁrst-order moments equations by neglecting
the second order cumulant, i.e. neglecting the variance. By doing so, we get the model
˙˜µ1(t)
=
k −γ1˜µ1(t) −k12˜µ1(t)(˜µ1(t) −1) + 2k21˜µ2(t)
˙˜µ2(t)
=
k12˜µ1(t)(˜µ1(t) −1) −γ2˜µ2(t)
(31)
where ˜µ1 and ˜µ2 are the approximate ﬁrst-order moments of the system. The unique positive equilibrium
point for this model is given by
˜µ∗
1
=
1
2k

−γ1 +
k12γ2
γ2 + k21
+
√
∆

˜µ∗
2
=
k12
2(γ2 + k21) ˜µ∗
1(˜µ∗
1 −1)
(32)
18


## Page 19


Figure 3: Trajectories of the ﬁrst order moments µ1(t) = E[X1(t)] and µ2(t) = E[X2(t)] of network
(29) for diﬀerent initial conditions (averaging is performed over 5000 cells). The trajectories
converge to the unique steady-state value located inside the compact set (the surface below the dashed
line), very close to the boundary.
where ∆=

−γ1 +
k12γ2
γ2 + k21
2
+ 4kk12γ2
γ2 + k21
.
With the same parameter values as before, we ﬁnd that ˜µ∗
1 = 1.6238 and ˜µ∗
2 = 1.6881 and therefore
v⊺˜µ∗= 5 for v⊺=

1
2

, showing that the state of the closed system converges to the boundary of the
compact set. Note that SSA also predicts that the trajectories of the ﬁrst-order moments converge to the
boundary of this set. However the actual equilibrium values for the ﬁrst-order moments of the stochastic
dynamics are µ∗
1 ≃1.1450 and µ∗
2 ≃1.9350, which diﬀer from the ones obtained with the closure method.
This discrepancy is expected since the variance has been neglected.
This example shows how attractive compact sets for the moments can be used as a test for the momet-
closure methods by checking whether the closed system predicts trajectories that that converge inside
those compact sets. However, note that in the current state, these compact sets can only be used to
obtain a lower bound on the closure-error whenever the trajectories of the closed dynamics converge to a
point outside the compact set. In such a case, the lower bound on the closure-error ε is simply given by
the distance between the equilibrium point of the closed-system
ε ≥inf
θ∈C ||˜µ∗−θ||2
(33)
where C is the attractive (convex) compact set and ˜µ∗is the equilibrium point of the closed dynamics.
19


## Page 20


Feedback loop
Let us consider the feedback loop network of Figure 4 represented by the reaction network
S1
k2
−−−⇀
S1 + S2,
∅
f(S3)
−−−⇀
S1
S3
k32
−−−⇀
S2 + S2,
S2 + S2
k23
−−−⇀
S3
Si
γi
−−−⇀
∅.
(34)
where S1 is mRNA and S2 is the corresponding protein. The dimer S3 acts back on the gene expression
through an arbitrary bounded nonnegative function f(·).
Figure 4: Feedback loop with arbitrary feedback rule.
We have the following result:
Result 16 For any positive values of the rate parameters and any bounded nonnegative function f(·), the
feedback loop with dimerization (34) is ergodic and all the moments are bounded and globally converging.
Stochastic switch
Let us consider the stochastic switch of [63] described by the unimolecular stochastic reaction network
∅
f1(S1
2)
−−⇀
S0
1,
S0
1
k1
−−⇀
S0
1 + S1
1
∅
f2(S1
1)
−−⇀
S0
2,
S0
2
k2
−−⇀
S0
2 + S1
2
Sj
i
γi,j
−−⇀
∅.
(35)
20


## Page 21


Above S0
i and S1
i represent mRNAs and proteins of gene i, respectively. The functions f1(·) and f2(·)
are arbitrary bounded nonnegative functions. We have the following result:
Result 17 For any positive values of the rate parameters and any bounded nonnegative functions f1(·)
and f2(·), the stochastic switch (35) is ergodic and all the moments are bounded and globally converging.
Repressilator
We consider here the stochastic repressilator of Figure 5 (see also [42]) involving N genes.
Figure 5: N-gene repressilator.
The reaction network corresponding to this N-gene repressilator is given by
∅
f1(S1
N )
−−⇀
S1
1
∅
f2(S1
1)
−−⇀
S1
2
∅
f3(S1
2)
−−⇀
S1
3
...
...
...
∅
fN(S1
N−1)
−−⇀
S1
N
S1
1
k1
−−⇀
S1
1 + S2
1
S1
2
k2
−−⇀
S1
2 + S2
2
S1
3
k3
−−⇀
S1
3 + S2
3
...
...
...
S1
N
kn
−−⇀
S1
N + S2
N
S1
i
γi
−−⇀
∅, i = 1, . . . , N
S2
i
δi
−−⇀
∅, i = 1, . . . , N
(36)
21


## Page 22


where fi(x) = αi+βi/(1+xn), αi, βi, n > 0. Above, S1
i and S2
i are the mRNA and protein corresponding
to gene i. We have the following result:
Result 18 For any positive values of the rate parameters ki, γi, δi, αi, βi and n, the stochastic N-gene
repressilator (36) is ergodic and all the moments are bounded and globally converging.
Stochastic SIR model
We consider here the following SIR-model, similar to the one in [64], deﬁned as
∅
ks
−−⇀
S,
∅
ki
−−⇀
I,
S
γs
−−⇀
∅
I
γi
−−⇀
∅,
R
γr
−−⇀
∅,
S + I
ksi
−−⇀
2I
I
kir
−−⇀
R,
R
krs
−−⇀
S.
(37)
where birth and death reactions represent people entering and leaving the process, respectively. The only
bimolecular reaction is the contamination reaction which turns one susceptible person into an infectious
one. The two last reactions represent how infectious people are recovering and how recovered people
become susceptible again. We then have the following result:
Result 19 For any positive values of the rate parameters, the SIR-model (37) is ergodic and all the
moments are bounded and globally converging.
Circadian clock
Let us consider the circadian oscillator of [65], depicted in Figure 6, which is a network involving 9 species
and 18 reactions.
Applying the developed theory on this model, we obtain the following result:
Result 20 For any positive values of the rate parameters, the circadian clock model of [65] is ergodic
and all the moments are bounded and globally converging.
Using, for instance, the values of [65] and solving for the optimization problem (20) using linprog and
Yalmip [66], we ﬁnd that c1 = 402.5768 and c2 = 0.1992. Typical trajectories for the proteins A, R
and C are depicted in Figure 7 where we can observe the expected oscillatory behavior. When averaging
the populations of the proteins A, R and C over a population of 2000 cells, we obtain the sample-
average trajectories depicted in Figure 8. Convergence to stationary values is easily seen. Moreover, from
the ergodicity property, we can even state that these ﬁxed points for the sample-averages are globally
attracting and that they coincide with the asymptotic time-average (dashed lines). The steady-state
average values for the proteins A, R and C are given by 222.1797, 534.8853 and 549.7195, respectively.
p53 model
Let us consider one of the oscillatory p53 models of [67], which is described by the reactions
∅
k1
−−⇀
S1,
S1
k2
−−⇀
∅,
S1
f(S1,S3)
−−⇀
∅
S3
k6
−−⇀
∅,
S2
k5
−−⇀
S3,
S1
k4
−−⇀
S1 + S2.
(38)
where S1 is the number of p53 molecules, S2 the number of precursor of Mdm2 molecules and S3 the
number of molecules of Mdm2. The function f(x, y) =
k3y
x+k7 implements a nonlinear feedback on the
degradation rate of p53. We have the following result:
Result 21 For any positive values of the rate parameters, the oscillatory p53 model (38) is ergodic and
all the moments are bounded and globally converging.
22


## Page 23


Figure 6: Circadian clock model of [65].
Lotka-Volterra model
We consider here the stochastic reaction network
∅
αi
−−⇀
Si,
Si
βi
−−⇀
Si + Si
Si + Sj
γij
−−⇀
Sj,
Si
δi
−−⇀
∅
(39)
which is an open analogue of the deterministic Lotka-Volterra system of [68]. The ﬁrst set of reactions
represent immigration, the second one reproduction, the third one competition due to overpopulation
and the last one deaths/migrations. We obtain then the following result, which is a stochastic analogue
of the results in [69] obtained in the deterministic setting:
Theorem 22 Let us deﬁne Γ(v) = [viγij] and assume that one of the following conditions hold:
1. there exists v > 0 such that the matrix Γ(v) + Γ(v)⊺is positive deﬁnite;
2. there exists v > 0 such that the Γ(v) + Γ(v)⊺is copositive, i.e. xT (Γ(v) + Γ(v)⊺)x ≥0 for all x ≥0,
and βi −δi < 0 for all i = 1, . . . , n.
Then, the stochastic reaction network (39) is ergodic and all the moments up to order

1 + 2c2
c5

−2 are
bounded and globally converging.
23


## Page 24


Figure 7: Sample-path of the species of the circadian clock model.
Schl¨ogl model
In order to illustrate that the method can be applied to systems with more general mass-action
kinetics, we consider the stochastic version of the well-known Schl¨ogl model [70]:
2S
k1XA
−−−→
3S
k2
−−−→
2S
∅
k3
−−−→
S
k4XB
−−−→
∅
(40)
where S is the main molecule in the network. The above model is derived in the supplementary material
S1 where we have assumed that the other molecular populations do not vary over time. Note that in the
present form the model has an inﬁnite state-space and involves a single trimolecular reaction. We then
have the following result.
Theorem 23 For any positive values of the rate parameters k1, k2, k3, k4 and any positive values for XA
and XB, the Markov process describing the Schl¨ogl model (40) is exponentially ergodic.
Note, however, that we cannot say anything on the stability of the moments (besides the fact that the
ﬁrst order-moment converges) since the condition DD2 does not hold here due to the presence of a cubic
term. Note that extending the condition DD2 to handle more general cases, such as this one, might be
possible.
Discussion
The central theme of this paper is to verify the ergodicity and moment boundedness of reaction networks
in the stochastic setting. Note that even though we mainly consider mass-action kinetics in this paper,
the framework also applies to more general kinetics described, for instance, by Hill functions (see the
24


## Page 25


Figure 8: Time evolution of the sample averages of the species A (top), R (left) and C
(right) of the circadian clock model (2000 cells averaging). The dashed-lines correspond to the
(asymptotic) time-average.
examples on the repressilator and the stochastic switch) and more general mass-action kinetics. These
results have several interesting and important biological implications.
For example, the ergodicity of a network shows that population-level information could be obtained by
observing a single trajectory for a long time. Such an insight can be used to leverage diﬀerent experimental
techniques for a given application. For example, consider a clonal cell population with each cell having a
gene-expression network that is ergodic. Then the stationary distribution (at the population level) of the
species involved in this network can be ascertained by observing a single cell over time. In other words,
to obtain stationary distributions one can either collect samples over time from a single cell (e.g. using
time-lapse microscopy) or one can take a snapshot of the entire cell population at some ﬁxed time (e.g.
using ﬂow-cytometry). Due to ergodicity, both these approaches will yield the same information. Hence,
far from being a technical condition, ergodicity can have far reaching experimental implications.
As a property of a network, ergodicity also sheds important light on the long range behaviors that can
be exhibited by that network. One may expect that most endogenous biochemical networks to be ergodic
in order to achieve robustness with respect to variability in initial conditions and kinetic parameters, thus
ensuring proper biological functions in spite of environmental disturbances. As also mentioned in the
introduction, ergodicity is a non-trivial property which needs to be carefully established and cannot be
generically assumed. To illustrate this, let us consider a simpliﬁed version of the model of carcinogenesis
considered in [71] which is given by
25


## Page 26


∅
k1
−−⇀
S1,
S1
k12
−−⇀
S2
S2
k21
−−⇀
S1,
S2
f(x)
−−⇀
∅
(41)
where f(x) =
γ2
α + x2
, α > 0. When k1 > γ2, the trajectories of the species grow unbounded, as shown
in Figure 9, emphasizing then non-ergodicity of the model for this choice of parameters.
Figure 9: State trajectories of the carcinogenesis model (41) with the parameters k1 = 5,
k12 = 1, k21 = 1, γ2 = 4 and α = 1. The dashed lines correspond to the average trajectories computed
over 1000 cells.
The ideas we use for analysis can also be applied for rationally designing circuits in synthetic biology,
where it is important that the network be (structurally) ergodic in order to ensure that the dynamics
has the desired behavior irrespective of the initial conditions. Such a design is crucial because the initial
conditions are usually unknown or diﬃcult to control at certain times, e.g. after cell division or after the
transfection of plasmids in the cell.
Our results on boundedness and convergence of statistical moments enable veriﬁcation of the suit-
ability of a stochastic model and to characterize the properties of its steady-state distributions, even
if such a distribution is not explicitly computable. One application of this is to provide justiﬁcations
and insights for using moment closure techniques which have been extensively used to study stochastic
chemical reaction networks. Some of these techniques [72, 73] are based on manipulations of the mo-
ment generating function of the underlying stochastic process. The existence of this moment generating
function is implicitly assumed in such techniques but it may not always hold, thereby jeopardizing the
validity of the technique. In this article, we show that under certain conditions, the distribution of the
stochastic process is uniformly light-tailed, which proves that the moment generating function exists for
all time. Certain moment closure techniques (see [74, 75]) prescribe ways to approximate higher order
moments as a function of lower order moments. Such an approximation is, however, only reasonable if
26


## Page 27


the higher order moments are bounded over time. This can be easily assessed with our approach and one
can even quantify the error by explicitly computing the moment bounds as described in this article.
Finally, the techniques developed here will prove invaluable for designing synthetic biological control
systems and circuits whose objective is to steer the moments of the network of interest to a speciﬁc
steady-state value. Until now, no theory has provided guidance for such a design. The speciﬁcs are
outside the scope of this article and will be pursued elsewhere.
Acknowledgments
The authors are grateful to Stephanie Aoki and Christine Khammash who spent some of their precious
time in producing several illustrative pictures.
Author contributions
C.B. and A.G. contributed equally to this work. C.B., A.G. and M.K. devised the research; C.B. and
A.G. carried out the research; C.B., A.G. and M.K. wrote the paper; A.G. developed the mathematical
framework; C.B. developed the results for unimolecular and bimolecular reaction networks, and applied
them to the examples.
Funding
This work has been supported by ETH and the Human Frontier Science Program Grant RGP0061/2011.
References
[1] ´Erdi P, T´oth J (1989) Mathematical models of chemical reactions. Nonlinear Science: Theory and
Applications. Princeton, NJ: Princeton University Press, xxiv+259 pp. Theory and applications of
deterministic and stochastic models.
[2] Papin JA, Hunter T, Palsson BO, Subramaniam S (2005) Reconstruction of cellular signalling net-
works and analysis of their properties. Nat Rev Mol Cell Biol 6: 99–111.
[3] Thattai M, van Oudenaarden A (2001) Intrinsic noise in gene regulatory networks. Proceedings of
the National Academy of Sciences 98: 8614-8619.
[4] Schuetz R, Zamboni N, Zampieri M, Heinemann M, Sauer U (2012) Multidimensional optimality of
microbial metabolism. Science 336: 601-604.
[5] Berger SI, Iyengar R (2009) Network analyses in systems pharmacology. Bioinformatics 25: 2466-
2472.
[6] Hethcote H (2000) The mathematics of infectious diseases. SIAM Review 42: 599-653.
[7] Bascompte J (2010) Structure and dynamics of ecological networks. Science 329: 765-766.
[8] Goutsias J (2007) Classical versus stochastic kinetics modeling of biochemical reaction systems.
Biophysical Journal 92: 2350–2365.
[9] McAdams HH, Arkin A (1999) It’s a noisy business! Genetic regulation at the nanomolar scale.
Trends in genetics : TIG 15: 65–69.
27


## Page 28


[10] Levin MD, Morton-Firth CJ, Abouhamad WN, Bourret RB, Bray D (1998) Origins of individual
swimming behavior in bacteria. Biophysical Journal 74: 175 - 181.
[11] Elowitz MB, Levine AJ, Siggia ED, Swain PS (2002) Stochastic gene expression in a single cell.
Science 297: 1183-1186.
[12] Arkin AP, Rao CV, Wolf DM (2002) Control, exploitation and tolerance of intracellular noise. Nature
420: 231–237.
[13] Kierzek AM, Zaim J, Zielenkiewicz P (2001) The eﬀect of transcription and translation initiation
frequencies on the stochastic ﬂuctuations in prokaryotic gene expression. Journal of Biological Chem-
istry 276: 8165-8172.
[14] McAdams HH, Arkin A (1997) Stochastic mechanisms in gene expression.
Proc Natl Acad Sci,
Biochemistry 94: 814–819.
[15] Gillespie DT (1997) A rigorous derivation of the chemical master equation. Physica A 188: 404–425.
[16] Laurenzi IJ (2000) An analytical solution of the stochastic master equation for reversible bimolecular
reaction kinetics. The Journal of Chemical Physics 113: 3315–3322.
[17] Jahnke T, Huisinga W (2007) Solving the chemical master equation for monomolecular reaction
systems analytically. Journal of Mathematical Biology 54: 1–26.
[18] Sidje RB (1998) Expokit: A software package for computing matrix exponentials. ACM Transactions
on Mathematical Software 24(1): 130–156.
[19] Jenkinson G, Goutsias J (2012) Numerical integration of the master equations in some models of
stochastic epidemiology. PLOS One 7(5): e36160.
[20] Dolgov SV, Khoromskij BN (2012) Tensor-product approach to global time- space-parametric dis-
cretization of chemical master equation. Preprint 68, Max-Planck-Institut fr Mathematik in den
Naturwissenschaften.
[21] Kazeev
V,
Khammash
M,
Nip
M,
Schwab
C
(2014)
Direct
Solution
of
the
Chemical
Master
Equation
Using
Quantized
Tensor
Trains.
PLoS
Comput
Biol
10(3):
e1003359.
doi:10.1371/journal.pcbi.1003359.
[22] Grima R, Schmidt DR, Newman TJ (2012) Steady-state ﬂuctuations of a genetic feedback loop: An
exact solution. The Journal of Chemical Physics 137: 035104.
[23] Munsky B, Khammash M (2006) The ﬁnite state projection algorithm for the solution of the chemical
master equation. Journal of Chemical Physics 124.
[24] Gillespie DT (1976) A general method for numerically simulating the stochastic time evolution of
coupled chemical reactions. Journal of Computational Physics 22(4): 403–434.
[25] Gillespie DT (1977) Exact stochastic simulation of coupled chemical reactions.
The Journal of
Physical Chemistry 81(25): 2340–2361.
[26] Gibson MA, Bruck J (2000) Eﬃcient exact stochastic simulation of chemical systems with many
species and many channels. The Journal of Physical Chemistry A 104: 1876-1889.
[27] Kurtz TG (1971) Limit theorems for sequences of jump Markov processes approximating ordinary
diﬀerential processes. J Appl Probability 8: 344–356.
28


## Page 29


[28] van Kampen NG (1961) A power series expansion of the master equation. Canad J Phys 39: 551–567.
[29] Kurtz TG (1976) Limit theorems and diﬀusion approximations for density dependent Markov chains.
Math Programming Stud : 67–78.
[30] Goutsias J, Jenkinson G (2013) Markovian dynamics on complex reaction networks. Physics Reports
529: 199 - 264.
[31] Khalil HK (1992) Nonlinear systems. New York: Macmillan Publishing Company, xii+564 pp.
[32] Meyn S, Tweedie RL (2009) Markov chains and stochastic stability. Cambridge: Cambridge Univer-
sity Press, second edition, xxviii+594 pp. With a prologue by Peter W. Glynn.
[33] Earnshaw BA, Keener JP (2010) Global asymptotic stability of solutions of nonautonomous master
equations. SIAM J Applied Dynamical Systems 9: 220-237.
[34] Schnakenberg J (1976) Network theory of microscopic and macroscopic behavior of master equation
systems. Rev Mod Phys 48: 571–585.
[35] Anderson DF, Craciun G, Kurtz TG (2010) Product-form stationary distributions for deﬁciency zero
chemical reaction networks. Bull Math Biol 72: 1947–1970.
[36] Lemarchand H (1980) Asymptotic solution of the master equation near a nonequilibrium transition:
The stationary solutions. Physica A: Statistical Mechanics and its Applications 101: 518 - 534.
[37] Malek Mansour M, Van Den Broeck C, Nicolis G, Turner JW (1981) Asymptotic properties of
markovian master equations. Annals of Physics 131: 283 - 313.
[38] Engblom S (2012) On the stability of stochastic jump kinetics. ArXiv:12023892 .
[39] Rathinam M (2014) Moment growth bounds on continuous time markov processes on non-negative
integer lattices. To appear in the Quaterly of Applied Mathematics .
[40] Dayar T, Hermanns H, Spieler D, Wolf V (2011) Bounding the equilibrium distribution of markov
population models. Numerical Linear Algebra with Applications 18: 931–946.
[41] Gardner TS, Cantor CR, Collins JJ (2000) Construction of a genetic toggle switch in escherichia
coli. Nature 403: 339–342.
[42] Elowitz MB, Leibler S (2000) A synthetic oscillatory network of transcriptional regulators. Nature
403: 335–338.
[43] Vellela M, Qian H (2008) Stochastic dynamics and non-equilibrium thermodynamics of a bistable
chemical system: the schl¨ogl model revisited. Journal of the Royal Society Interface 6(39): 925–940.
[44] Hespanha JP (2008) Moment closure for biochemical networks. In: 3rd International Symposium on
Communications, Control and Signal Processing. St. Julian’s, Malta, pp. 142–147.
[45] Grima R (2012) A study of the accuracy of moment-closure approximations for stochastic chemical
kinetics. The Journal of Chemical Physics 136: 154105.
[46] Smale S (2004) Diﬀerential Equations, Dynamical Systems & an introduction to Chaos. Academic
Press.
[47] Feinberg M (1972/73) Complex balancing in general kinetic systems. Arch Rational Mech Anal 49:
187–194.
29


## Page 30


[48] Feinberg M (1995) The existence and uniqueness of steady states for a class of chemical reaction
networks. Arch Rational Mech Anal 132: 311–370.
[49] Horn F, Jackson R (1972) General mass action kinetics. Arch Rational Mech Anal 47: 81–116.
[50] Horn F (1972/73) Necessary and suﬃcient conditions for complex balancing in chemical kinetics.
Arch Rational Mech Anal 49: 172–186.
[51] Ethier SN, Kurtz TG (1986) Markov processes : Characterization and Convergence. Wiley Series in
Probability and Mathematical Statistics: Probability and Mathematical Statistics. New York: John
Wiley & Sons Inc., x+534 pp.
[52] Kallenberg O (2002) Foundations of modern probability.
Probability and its Applications (New
York). New York: Springer-Verlag, second edition, xx+638 pp.
[53] Pemantle R, Rosenthal JS (1999) Moment conditions for a sequence with negative drift to be uni-
formly bounded in lr. Stochastic Processes and their Applications 82: 143-155.
[54] Hespanha JP (2008) Moment closure for biochemical networks. In: 3rd International Symposium on
Communications, Control and Signal Processing. St. Julian’s, Malta, pp. 142–147.
[55] Pendar H, Platini T, Kulkarni RV (2013) Exact protein distributions for stochastic models of gene
expression using partitioning of poisson processes. Physical Review E 87: 042720.
[56] Paulev´e L, Craciun G, Koeppl H (2013) Dynamical properties of discrete reaction networks. Journal
of Mathematical Biology : 1-18.
[57] Gupta A, Khammash M (2013) Determining the long-term behavior of cell populations: A new proce-
dure for detecting ergodicity in large stochastic reaction networks. Technical Report arXiv:1312.2879,
ETH-Z¨urich.
[58] Norris JR (1998) Markov chains, volume 2 of Cambridge Series in Statistical and Probabilistic Math-
ematics. Cambridge: Cambridge University Press, xvi+237 pp. Reprint of 1997 original.
[59] Meyn SP, Tweedie RL (1993) Stability of Markovian processes. III. Foster-Lyapunov criteria for
continuous-time processes. Adv in Appl Probab 25: 518–548.
[60] Boyd S, Vandenberghe L (2004) Convex Optimization. Cambridge, MA, USA: Cambridge University
Press.
[61] Sturm JF (2001) Using SEDUMI 1.02, a Matlab Toolbox for Optimization Over Symmetric Cones.
Optimization Methods and Software 11: 625–653.
[62] T¨ut¨unc¨u RH, Toh KC, Todd MJ (2003) Solving semideﬁnite-quadratic-linear programs using SDPT3.
Mathematical Programming Ser B 95: 189–217.
[63] Tian T, Burrage K (2006) Stochastic models for regulatory networks of the genetic toggle switch.
Proc Natl Acad Sci 103(22): 8372–8377.
[64] Chen WY, Bokka S (2005) Stochastic modeling of nonlinear epidemiology. J theor Biol 234: 455–470.
[65] Vilar JMG, Kueh HY, Barkai N, Leibler S (2002) Mechanisms of noise-resistance in genetic oscillator.
Proc Natl Acad Sci 99(9): 5988–5992.
[66] L¨ofberg J (2004) Yalmip : A toolbox for modeling and optimization in MATLAB. In: Proceedings
of the CACSD Conference. Taipei, Taiwan. URL http://control.ee.ethz.ch/~joloef/yalmip.
php.
30


## Page 31


[67] Geva-Zatorsky N, Rosenfeld N, Itzkovitz S, Milo R, Sigal A, et al. (2006) Oscillations and variability
in the p53 system. Molecular Systems Biology 2: 2006.0033.
[68] Gopalsamy K (1984) Global asymptotic stability in volterra’s population systems. Journal of Math-
ematical Biology 19: 157–168.
[69] Champagnat N, Jabin P, Raoul G (2010) Convergence to equilibrium in competitive Lotka-Volterra
and chemostat systems. Compte Rendus de l’Acad´emie des Sciences - Math´ematique 348(23-24):
1267–1272.
[70] Schl¨ogl F (1972) Chemical reaction models for non-equilibrium phase transition.
Zeitschrift f¨ur
Physik 253(2): 147–161.
[71] Bois FY, Zeise L, Tozer TN (1990) Precision and sensitivity of pharmacokinetic models for cancer risk
assessment: Tetrachloroethylene in mice, rats, and humans. Toxicology and applied pharmacology
102: 300–315.
[72] Lee C, Kim KH, Kim P (2009) A moment closure method for stochastic reaction networks. The
Journal of Chemical Physics 130(13): 134107.
[73] Ale A, Kirk P, Stumpf MP (2013) A general moment expansion method for stochastic kinetic models.
The Journal of Chemical Physics 138(17): 174101.
[74] Gomez-Uribe CA, Verghese GC (2007) Mass ﬂuctuation kinetics: Capturing stochastic eﬀects in
systems of chemical reactions through coupled mean-variance computations. The Journal of Chemical
Physics 126(2): 024109.
[75] Singh A, Hespanha JP (2011) Approximate moment dynamics for chemically reacting systems. IEEE
Transactions on Automatic Control 56(2): 414–418.
31

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1304_5404v3_a_scalable_computational_framework_for_establishing_long_term_behavior_of_stocha
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2013/1304_5404V3_A_SCALABLE_COMPUTATIONAL_FRAMEWORK_FOR_ESTABLISHING_LONG_TERM_BEHAVIOR_OF_STOCHA.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

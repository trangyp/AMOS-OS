---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1809.04613v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1809.04613v1_Discrepancies_between_extinction_events_and_boundary_equilibria_in_reaction_netw

> Source: 1809.04613v1_Discrepancies_between_extinction_events_and_boundary_equilibria_in_reaction_netw.pdf

> Pages: 17

---


## Page 1


arXiv:1809.04613v1  [q-bio.MN]  12 Sep 2018
Discrepancies between extinction events and boundary equilibria
in reaction networks
David F. Anderson∗
Daniele Cappelletti†
September 14, 2018
Abstract
Reaction networks are mathematical models of interacting chemical species that are primarily used
in biochemistry. There are two modeling regimes that are typically used, one of which is deterministic
and one that is stochastic. In particular, the deterministic model consists of an autonomous system of
diﬀerential equations, whereas the stochastic system is a continuous time Markov chain. Connections
between the two modeling regimes have been studied since the seminal paper by Kurtz (1972), where
the deterministic model is shown to be a limit of a properly rescaled stochastic model over compact time
intervals. Further, more recent studies have connected the long-term behaviors of the two models when
the reaction network satisﬁes certain graphical properties, such as weak reversibility and a deﬁciency
of zero.
These connections have led some to conjecture a link between the long-term behavior of the two
models exists, in some sense. In particular, one is tempted to believe that positive recurrence of all
states for the stochastic model implies the existence of positive equilibria in the deterministic setting,
and that boundary equilibria of the deterministic model imply the occurrence of an extinction event in
the stochastic setting. We prove in this paper that these implications do not hold in general, even if
restricting the analysis to networks that are bimolecular and that conserve the total mass. In particular,
we disprove the implications in the special case of models that have absolute concentration robustness,
thus answering in the negative a conjecture stated in the literature in 2014.
1
Introduction
Reaction systems are mathematical models that are used to describe the dynamical behavior of interacting
chemical species. Such models are often utilized in the biochemical setting, where they describe biological
processes. Traditionally, we distinguish between a deterministic and a stochastic modeling regime, with
the deterministic regime appropriate when the counts are so high that the concentrations of the species can
be well modeled via a set of autonomous diﬀerential equations and with the stochastic model appropriate
when the counts are low. For the stochastic model, one usually assumes the counts of the diﬀerent chemical
species involved evolve according to a continuous time Markov chain in Zd
≥0 (where d is the number of
distinct chemical species).
It is natural to wonder about the relationship between the stochastic and deterministic models for
reaction systems. The ﬁrst paper in this direction was [16], where it was shown that on compact time
intervals, the deterministic model is the weak limit of the stochastic model, conveniently rescaled, when
the initial counts of molecules go to inﬁnity in an appropriate manner (see Theorem 3.1 below). Followup
works consider piecewise deterministic limits in multiscale settings [7, 14, 15, 19], and connections have been
found between equilibria of the deterministic model and stationary distributions of the stochastic model,
under certain assumptions [3, 5, 8, 10].
Further connections have been studied in terms of Lyapunov
functions of the deterministic model and stationary distributions of the stochastic model [4].
The focus of this paper is on the relationship (or lack thereof) between the occurrence of extinction
events in the stochastic model and the equilibria of the corresponding deterministic model. The relevance
of this question resides in the fact that equilibria of the deterministic model are typically easier to analyze
than the state space of the stochastic model, so ﬁnding a link between the two is desirable. Moreover,
understanding when extinction events can occur is relevant in the biological setting as such events may
imply that the production of a certain protein has halted, or that a certain important reactant is eventually
∗Department of Mathematics, University of Wisconsin-Madison, email: anderson@math.wisc.edu.
Supported by Army
Research Oﬃce grant W911NF-18-1-0324.
†Department of Mathematics, University of Wisconsin-Madison, email: cappelletti@math.wisc.edu.
1


## Page 2


consumed completely. However, we demonstrate through the analysis of a number of examples that a
series of expected connections do not hold in general, and therefore discourage interested researchers from
assuming them, or trying to prove them. In particular, we prove Conjecture 3.7 in [6] to be false. To better
understand the work carried out here, we brieﬂy describe some of the work in [6].
In [6], an interesting connection between extinction events and systems with absolute concentration
robustness (ACR) is unveiled.
ACR systems are deterministic reaction systems in which at least one
chemical species has the same value at every positive equilibrium of the system. Such species are called
absolute concentration robust (ACR) species. As an example, consider the network
A+B
κ1
2B
B
κ2
A
(1)
Under the assumption of mass-action kinetics, the considered system is ACR: the species A has the value
κ2/κ1 in all the positive equlibria of the system. When modeled stochastically, the reaction B →A can
take place until no molecules of B are left. When this happens, no reaction can take place anymore as
each of the reactions in (1) requires a molecule of B as a reactant. We call this an extinction event and
note that it eventually occurs with a probability of one, regardless of the rate constants κ1, κ2 ∈R>0. This
diﬀering qualitative behavior between the two models (robustness for the ODE and eventual extinction for
the stochastic) was studied in [6] and was proven to be general, in the following sense. In [20], Shinar and
Feinberg provided suﬃcient necessary conditions for a deterministic reaction system to be ACR. However,
in [6] it was shown that the stochastic model will, with a probability of one, undergo an extinction event if
the reaction network satisﬁes those same conditions and also has a positive conservation relation. Moreover,
the eventual extinction holds regardless of choice of rate constants or initial condition.
The assumptions of [6] (and by extension [20]) seem technical and do not unveil a clear reason for
why the family of stochastic models considered have almost sure extinction events. Since under the same
assumptions the corresponding deterministic system is ACR, it seems natural to conjecture that (i) ab-
solute concentration robustness of the associated deterministic model, and (ii) the existence of a positive
conservation relation, are suﬃcient to imply almost sure extinction for the stochastic model. This is the
content of Conjecture 3.7 in [6].
Belief in Conjecture 3.7 in [6] becomes even stronger when we realize that conservative ACR determin-
istic reaction systems often have boundary equilibria. For example, in the model (1), the deterministic
model has boundary equilibria of the form (a, 0), which are attracting for initial conditions where the
total mass is lower than κ2/κ1. In the stochastic model the species B is eventually completely consumed,
showing that the behaviors of the two models do have some connection. Returning to the general setting,
the existence of boundary equilibria occurs often for conservative ACR models since on certain invariant
regions the total “mass” of the species (as determined by the positive conservation law) is strictly less than
the ACR value, implying there can be no positive equilibria in that invariant region. Since the invariant
regions are compact due to the existence of a mass conservation, the ODE solution is often attracted to
the boundary. Intuitively, such attraction might indicate a propensity of the stochastic model to reach the
boundary, and get absorbed.
However, in section 5, we will show with non-trivial examples that the intuition the conjecture is based
upon does not hold in general. In particular, we show that no assumption in the main result of [6] can be
eliminated. Moreover, we do so with bimolecular examples (which are the most commonly used examples
in the biological setting). In section 6, we will further explore the connection (or rather, the lack thereof)
between extinction events of the stochastic model and equilibria of the associated deterministic model, and
put to rest the common misconceptions that (i) a complete lack of positive equilibria in a conservative
deterministic model implies the occurrence of an extinction event in the stochastic model, and (ii) that
positive recurrence of all the states of the stochastic model implies the existence of a positive equilibrium
of the associated deterministic model.
The outline of the remainder of the paper is as follows. In section 2, we provide the necessary material
on notation, and the formal introduction of the relevant mathematical models. In section 3, we will state
the classical result from [16, 17] precisely. This results provides a connection between the behavior of
the stochastic and deterministic models on compact time intervals. We will then provide examples which
demonstrate a discrepancy in the long-term behavior of the models (in terms of explosions and positive
recurrence of the stochastic model with respect to blow-ups and compact trajectories of the deterministic
model). In section 4, we provide the necessary deﬁnitions relating to extinctions in the present context.
In particular, we point out that extinctions should refer to both species and reactions, as opposed to just
2


## Page 3


the counts of species. Finally, in sections 5 and 6 we provide our main results and analyze a number of
examples as described in the previous paragraph.
2
Necessary Background and Notation
2.1
Notation
We denote the non-negative integer numbers by Z≥0. We also denote the non-negative and the positive
real numbers by R≥0 and R>0, respectively. Given a real number a, we denote by |a| its absolute value.
For any real vector v ∈Rd, we denote its ith entry by vi, and we use the notation
∥v∥1 =
d
X
i=1
|vi|.
We further write v > 0 and say that v is positive if every entry of v is positive. Moreover, given two real
vectors v, w ∈Rd, we write v ≥w if vi ≥wi for all 1 ≤i ≤d. Finally, given a set A, we denote its
cardinality by |A|.
2.2
Basic deﬁnitions of reaction network theory
A reaction network is a triple G = (X, C, R). X is a ﬁnite non-empty set of symbols, referred to as species,
and C is a ﬁnite non-empty set of linear combinations of species with non-negative integer coeﬃcients,
referred to as complexes. After ordering the set of species, the ith species of the set can be identiﬁed with
the vector ei ∈R|X |, whose ith entry is 1 and whose other entries are zero. It follows that any complex
y ∈C can be identiﬁed with a vector in Z|X |
≥0 , which is the corresponding linear combination of the vectors
ei. Finally, R is a non-empty subset of C × C, whose elements are called reactions, such that for any y ∈C,
(y, y) /∈R. Following the common notation, we will denote any element (y, y′) ∈R by y →y′. We require
that every species in X appears in at least one complex, and that every complex in C appears as an element
in at least one reaction. Note that under this condition, a reaction network is uniquely determined by the
set of reactions R.
In this paper, species will always be letters and will be alphabetically ordered.
A directed graph can be associated in a very natural way to a reaction network by considering the set
of complexes as nodes and the set of reactions ad directed edges. Such a graph is called a reaction graph.
Usually, a reaction network is presented by means of its reaction graph, which deﬁnes it uniquely. By using
the reaction graph, we can further deﬁne the terminal complexes as those nodes that are contained in some
strongly connected component of the graph, that is those nodes y such that for any directed path from y
to another complex y′ there exists a directed path from y′ to y. We say that a complex is non-terminal if
it is not terminal.
We deﬁne the stoichiometric subspace of a reaction network as
S = spanR{y′ −y : y →y′ ∈R}.
We also let ℓdenote the number of connected components of the reaction graph (or linkage classes of the
network) and deﬁne the deﬁciency of the network as
δ = |C| −ℓ−dim S.
The geometric interpretation of the deﬁciency is not clear from the above deﬁnition, see [13] for more
detailes on this object.
We say that a vector v ∈Z|X | is a conservation law if it is orthogonal to the stoichiometric subspace S.
We say that a network is conservative if there is a positive coservation law: this means that it is possible
to assign a mass to the molecules of each chemical species such that the total mass (i.e. the sum of the
masses of all the molecules present) is conserved by the occurrence of every reaction.
We say that a reaction network is bimolecular if maxy∈C ∥y∥1 ≤2. Many biological models fall into this
category, since it is often the case that at most two molecules react at a time.
Finally, we associate with each reaction y →y′ ∈R a positive real number κy→y′, called a rate constant.
A reaction network with a choice of rate constants is called a mass-action system, and a stochastic or a
deterministic dynamics can be associated with it, as described later.
A mass-action system is usually
presented by means of the reaction graph, where the reactions have been labelled with the corresponding
rate constant. An example of this can be found in (1).
3


## Page 4


2.2.1
Stochastic Model
In a stochastic mass action system, the evolution in time of the copy-numbers of molecules of the diﬀerent
chemical species is considered. Speciﬁcally, the copy-numbers of the molecules of diﬀerent chemical species
at time t ≥0 form a vector X(t) ∈Z|X |
≥0 . The process X is assumed to be a continuous time Markov chain.
Speciﬁcally, for any two states x, x′ ∈Z|X |
≥0 the transition rate from x to x′ is given by
q(x, x′) =
X
y→y′∈R
y′−y=x′−x
λy→y′(x),
where
λy→y′(x) = κy→y′
|X |
Y
i=1
yi−1
Y
j=0
(xi −j)
for x ∈Z|X |
≥0
is the stochastic mass action rate function of y →y′. Note that λy→y′(x) > 0 if and ony if x ≥y, which
prevent the entries of the process X from becoming negative. Also, note that the process is conﬁned within
an stoichiometric compatibility class, that is for every t ≥0
X(t) ∈{X(0) + v : v ∈S} ∩Z|X |
≥0 .
It is worth noting that the stochastic mass-action kinetics follows from the assumption that the molecules
of the diﬀerent species are well-mixed, so the propensity of each reaction to take place is proportional to
the number of possible sets of molecules that can give rise to an occurrence of the reaction. Other kinetics
may arise in diﬀerent scenarios, but in the present paper we are only concerned with mass action systems.
2.2.2
Deterministic Model
In a deterministic mass action system the evolution in time of the concentrations of the diﬀerent chemical
species is modeled. We consider the concentrations of the diﬀerent chemical species at time t ≥0 as a
vector z(t) ∈R|X |
≥0 . It is then assumed that the function z is a solution to the Ordinary Diﬀerential Equation
(ODE)
d
dtz(t) = g(z(t)),
(2)
where
g(x) =
X
y→y′∈R
(y′ −y)κy→y′
|X |
Y
i=1
xyi
i
for x ∈R|X |
≥0
is the deterministic mass action species formation rate. As in the stochastic case, the solution z is conﬁned
within a stoichiometric compatibility class, meaning that for any t ≥0
z(t) ∈{z(0) + v : v ∈S} ∩R|X |
≥0 .
Finally, as for stochastic models, the choice of mass action kinetics corresponds to the assumption that the
molecules of the diﬀerent species are well-mixed. Other kinetics (such as Michaelis-Menten kinetics, Hill
kinetics, power law kinetics) are considered in the literature, but are not dealt with in this paper.
3
Correspondences between the two modeling regimes and known
discrepancies
The aim of this section is to describe why it was believed that certain properties of the deterministic mass
action system would imply the occurrence of extinction events for the stochastically modeled mass action
system. Here, we brieﬂy describe or give reference to some known connections between the two modeling
regimes, and provide some warnings in the form of examples of discrepancies between the two models.
4


## Page 5


3.1
Connections
The ﬁrst connection found between stochastic and deterministic models dates back to [16]. The situation
considered is the following: a reaction network G is given. It is assumed that the volume V of a container
where the chemical transformations occur is increased. The propensity of a reaction to occur changes with
the volume, depending on how many molecules are needed (i.e. need to collide) for the reaction to take
place. Speciﬁcally, the rate constants scale with the volume as
κV
y→y′ = V 1−∥y∥1κy→y′,
for some ﬁxed positive constants κy→y′. A family of continuous-time Markov chain {XV }V is then deﬁned,
with XV being the process associated with the stochastic mass action system with rate constants κV
y→y′.
Then, the following holds [16, 17].
Theorem 3.1. Assume that for a ﬁxed positive state z0 ∈R|X |
>0 and for all ε > 0 we have
lim
V →∞P
V −1XV (0) −z0
 > ε

= 0.
Moreover, assume that the solution z of the ODE (2) with z(0) = z0 is unique and is deﬁned up to a ﬁnite
ﬁxed time T > 0. Then, for any ε > 0
lim
V →∞P

sup
t∈[0,T ]
V −1XV (t) −z(t)
 > ε

= 0.
Roughly speaking, the theorem states the rescaled stochastic processes XV converge path-wise to the
ODE solution of the deterministic mass action system, over compact intervals of time. The theorem also
holds for more general kinetics than mass action kinetics, as long as the rate functions λy→y′ are locally
Lipschitz [17]. Theorem 3.1 has been extended for the multiscale setting [15].
It is interesting to note that model reduction techniques over compact intervals of time also work for
both the deterministic and stochastic models in the exact same manner. In particular, we refer to the
assumptions under which intermediate species can be eliminated from a multiscale model, and to the
description of the resulting simpliﬁed model [9, 11].
3.2
Known discrepancies
Here we cite some known examples showing that compactness of the trajectories of a deterministic mass
action system do not imply positive recurrence or even regularity (that is, lack of explosions) for the
associated stochastic model. Moreover, we demonstrate that a blowup of the deterministic mass-action
system does not in general imply explosions for the associated stochastic mass action system.
In [1] it is shown that the mass action system
0
κ1
2A+B
κ2
4A+4B
κ3
A
(3)
is transient (i.e. all states are transient) when stochastically modeled, for all choices of rate constants. For
the deterministic mass action system, however, for any choice of rate constants there exists a compact set
K such that for all initial conditions z(0), a t∗> 0 exists with z(t) ∈K for all t > t∗(the system is said
to be permanent, a property that in this case follows from the network being strongly endotactic [12]).
Moreover, in [1] it is also shown that for any choice of rate constants the mass action system
0
κ1
2A
κ2
4A+B
κ2
6A+4B
κ3
3A
(4)
is explosive (in the sense of [18]) when stochastically modeled, while the deterministic mass action system
is permanent as for (3) (which again follows because the network is strongly endotactic).
Since Theorem 3.1 holds, we expect the time of drifting towards inﬁnty of the processes XV associated
with (3) to increase with V . Similarly, the time until explosion of the processes XV associated with (4)
necessarily tends to inﬁnity, as V →∞.
We have shown examples of mass action systems that are somehow well behaved if deterministically
modeled, and transient or explosive if stochastically modeled.
For completeness, we also present here
an example of a mass action system that is positive recurrent (i.e. all states are positive recurrent) if
5


## Page 6


stochastically modeled, while the associated determinisitc ODE solution has blow-ups for any positive
initial condition. The system is discussed in [2] and is the following.
A
1
2
2A
3
1
3A
1
4A.
(5)
It is worth citing here a very similar example, also discussed in [2], where the behaviour of the two modeling
regimes is similar. Consider the mass action system
A
1
2
2A
7
4
3A
6
1
4A
1
5A
(6)
It is shown in [2] that the corresponding stochastic mass action system is explosive for any positive initial
condition X(0), and the associated deterministic mass action system has a blow up for any positive initial
condition z(0).
Other examples of coincidence between the long-term behaviour of the stochastic and deterministic
models of mass action systems are given by the family of complex balanced systems, and are studied in [5,
8, 10]. The existence of such connections and Theorem 3.1 contributed to the formulation of the conjecture
that “mass action systems with ACR species when deterministically modeled undergo an extinction event
when stochastically modeled”, for the reasons concerning boundary equilibria of the deterministic model
already discussed in the Introduction. However, we have shown in this section that the long-term dynamics
of stochastically and deterministically modeled mass action systems can diﬀer greatly.
4
Extinction
In this section, we will formally describe what is meant by the term “extinction” in the present context.
We begin with the following standard deﬁnitions.
Deﬁnition 4.1. Consider a stochastic mass action system. We say that
• a state x′ is reachable from x if for some t > 0
P(X(t) = x′ | X(0) = x) > 0;
• a set Γ ⊆Z|X |
≥0 is reachable from x if for some t > 0
P(X(t) ∈Γ | X(0) = x) > 0;
• a set Γ ⊆Z|X |
≥0 is closed if for all t > 0
P(X(t) ∈Γ | X(0) ∈Γ) = 1;
• a reaction y →y′ ∈R is active at a state x if λy→y′(x) > 0.
• a set Γ ⊆Z|X |
≥0 is an extinction set for the reaction y →y′ ∈R if Γ is closed and y →y′ is not active
at any state of Γ.
Deﬁnition 4.2. Consider a stochastic mass action system.
We say that the process X undergoes an
extinction event at time t∗> 0 if there is a reaction y →y′ ∈R and an extinction set Γ for y →y′ such
that X(t∗) ∈Γ and X(t∗−) /∈Γ.
The meaning of the above deﬁnition is the following: at a certain time t∗the copy-number of some
chemical species (or a set of chemical species) gets so low that a certain reaction can not occur anymore,
and the loss is irreversible.
In connection with Deﬁnition 4.2, we give some useful results.
Proposition 4.1. Consider a stochastic mass action system, and two reactions y →y′, ˜y →˜y′ ∈R, with
y′ ≥˜y . Assume that no extinction set for y →y′ is reachable from the state x. Then, no extinction set
for ˜y →˜y′ is reachable from x.
6


## Page 7


Proof. Since no extinction set for y →y′ is reachable from x, any closed set Γ that is reachable from x
contains a state x′ such that λy→y′(x′) > 0, or equivalently x′ ≥y. Hence, the state x′ + y′ −y is reachable
from x′, and since Γ is closed it follows that x′ + y′ −y ∈Γ. Moreover, since x′ ≥y and y′ ≥˜y we have
x′ + y′ −y ≥y′ ≥˜y, which implies that λ˜y→˜y′(x′ + y′ −y) > 0 and that Γ is not an extinction set for
˜y →˜y′. This concludes the proof.
Proposition 4.2. Consider a stochastic mass action system, and two reactions y →y′, ˜y →˜y′ ∈R, with
y ≥˜y. Assume that no extinction set for y →y′ is reachable from the state x. Then, no extinction set for
˜y →˜y′ is reachable from x.
Proof. As in the proof of Proposition 4.1, since no extinction set for y →y′ is reachable from x, any closed
set Γ that is reachable from x contains a state x′ with λy→y′(x′) > 0, which is equivalent to x′ ≥y. Since
y ≥˜y, we have x′ ≥˜y, which is equivalent to λ˜y→˜y′(x′) > 0. This concludes the proof.
5
Extinction and ACR systems
We give here the formal deﬁnition of system that has Absolute Concentration Robustness (ACR) . The
deﬁnition is purely in terms of deterministic systems, and the precise connection with extinction events
will be described later.
Deﬁnition 5.1. Consider a deterministic mass action system. The system is said to be Absolute Concen-
tration Robust (ACR) if there exists an index 1 ≤i ≤|X| and a real number u ∈R>0 such that all c > 0
with g(c) = 0 satisfy ci = u. In this case, the ith species is called an ACR species with ACR value u.
Note that, by deﬁnition, all deterministic mass action systems with no positive equilibria, or with only
one positive equilibrium are ACR. Speciﬁcally, in these cases all species are ACR. However, such degenerate
cases elude the sense of the deﬁnition of ACR models, which captures an important biological property:
whenever the system is at a positive equilibrium (and there could be many positive equilibria), some
special chemical species are always expressed at the same level, and are therefore “robust” to environmental
changes.
Structural suﬃcient conditions for a model to be ACR can be found in the following result, due to
Feinberg and Shinar [20].
Theorem 5.1. Consider a deterministic mass action system and assume
1. there exists at least one c > 0 with g(c) = 0;
2. the reaction network has deﬁciency 1;
3. there are two non-terminal complexes y ̸= y′ such that only the ith entry of y′ −y is diﬀerent from 0.
Then, the ith species is ACR.
Note that the assumption on the existence of a positive equilibrium is not needed for the theorem to
hold, since if there were none then all the species would automatically be ACR by Deﬁnition 5.1. However,
the assumption was included because this degenerate case was not considered in [20].
The connection with extinction events is given by the following result, due to Anderson, Enciso, and
Johnston [6].
Theorem 5.2. Consider a stochastic mass action system and assume
1. there exists at least one c > 0 with g(c) = 0;
2. the reaction network has deﬁciency 1;
3. there are two non-terminal complexes y ̸= y′ such that only the ith entry of y′ −y is diﬀerent from 0;
4. the reaction network is conservative.
Then, an extinction event occurs almost surely. In particular, with a probability of one the process X
enters a closed set Γ ⊂Zd
≥0 such that λy→y′(x) = 0 for all x ∈Γ and for all y →y′ ∈R with y being a
non-terminal complex.
7


## Page 8


As an example of how to apply Theorems 5.1 and 5.2, consider the mass-action system (1).
The
deﬁciency is δ = 4 −2 −1 = 1, the two non-terminal complexes A + B and B are such that their diﬀerence
is A, and there is at least one c > 0 with g(c) = 0.
Hence, by Theorem 5.1, when deterministically
modeled, the mass action (1) is ACR, and in particular the species A appears with the same value at every
positive equilibrium of the system. In fact, it can be easily checked that all positive equilibria are of the
form

κ2
κ1 , β

for some β > 0, where the species are ordered as (A, B). Moreover, the reaction network of
(1) is conservative, since (1, 1) is a positive conservation law. Hence, by Theorem 5.2, the stochastically
modeled mass action system will, with a probability of one, undergo an extinction event. In particular, both
reactions B →A and A + B →2B cannot occur after the extinction. Since the total mass is conserved,
this can only mean that the molecules of B are eventually completely consumed.
Note that under the assumptions of Theorem 5.2, the deterministically modeled mass action system is
ACR. Since the assumption of Theorem 5.2 are quite technical in nature, as discussed in the Introduction
it was thought for a long time that the real reason leading to the extinction event in the stochastic mass
action system was the associated deterministic mass action system being ACR. This seemed plausible
since ACR systems often exhibit attracting boundary equilibria. As an example, if the total mass of the
deterministic mass action system (1) is lower then the ACR value of A, that is if ∥z(0)∥< κ2/κ1, then the
ODE solution is conﬁned within a compact stoichiometric compatibility class with no positive equilibria,
and is eventually attracted by the boundary equilibrium (z(0), 0). This resembles what happens with the
stochastically modeled system.
In this section we show that such intuition is not correct. We do so by proving that if you remove
any of the technical assumptions (2), (3), and (4) from Theorem 5.2, while maintaining the absolute
concentration robustness of the associated deterministic mass action system, then the result no longer
holds. Moreover, the previous sentence holds even if we add the additional constraint that the reaction
network be bimolecular.
Example 1: assumption (4) cannot be removed
In [6], the authors realized that assumption (4) could not be removed from the statement of Theorem 5.2,
and proved that with the following example. Consider the reaction network
A+B
κ1
0
B
κ2
A+2B
(7)
The mass action system satisﬁes the assumptions of Theorem 5.1 and the species A is ACR, with ACR
equilibrium κ2/κ1. The only assumption of Theorem 5.2 that is not met is (4), as the network is not
conservative. Indeed, the stoichiometric subspace is
S =

s
s

: s ∈R

and no positive vector is contained in
S⊥=

s
−s

: s ∈R

.
In [6], it is shown that the stochastically modeled mass action system does not undergo any extinction
event if X1(0) < X2(0) (remember we assume the species to be alphabetically ordered). In this case, the
stationary distribution is computed by using birth and death process techniques, and every state is shown
to be positive recurrent.
We can modify (7) to obtain the bimolecular mass action system
A+B
κ1
0
B
κ2
A+C
C
κ3
κ4
2B
(8)
The mass action system (8) still satisﬁes the assumptions of Theorem 5.1, and it can therefore be concluded
that the species A is ACR. In fact, the ACR value for A is still κ2/κ1. Again, the only assumption of
8


## Page 9


Theorem 5.2 that is not satisﬁed is (4), since it can be checked that the orthogonal to the stoichiometric
subspace is
S⊥=





s
−s
−2s

: s ∈R


,
which does not contain any positive vector. Deﬁne the conserved quantity m = X1(0) −X2(0) −2X3(0)
and assume that m < 0. We will show that no extinction set for any reaction exists, which in turn proves
that no extinction event can occur.
Note that since X is conﬁned within a stoichiometric compatibility class, for any t ≥0
X1(t) −X2(t) −2X3(t) = m < 0.
Assume that from X(0) a state x′ can be reached with λA+B→0(x′) = 0. Then, either
(i) x′
2 = 0, or
(ii) x′
2 > 0 and x′
1 = 0.
Suppose we are in case (i). Then, since
m = x′
1 −2x′
3 < 0,
we must have x′
3 > 0. Hence the reaction C →2B can take place, in which case at least one molecule of B
is present. At this point, either A + B →0 is active, or we are in case (ii). Hence, assume that (ii) holds.
Then B →A + C can occur, which can then be followed by C →2B. After these two reactions take place,
both a molecule of A and a molecule of B are necessarily present, so a state is reached where the reaction
A + B →0 is active.
Combining all of the above, we have proven that no extinction set for A + B →0 is reachable from
X(0). By applying Proposition 4.2, it follows that the same holds for the reaction B →A + C. Then, by
Proposition 4.1 we have that no extinction set for C →2B is reachable from X(0), and ﬁnally by applying
Proposition 4.1 we conclude that the same holds for 2B →C. In conclusion, no extinction event can occur
with the chosen initial conditions.
Example 2: assumption (2) cannot be removed
Consider the bimolecular mass action system
A+B
κ1
B+C
κ2
κ3
2B
κ4
2D
C
κ5
A
D
κ6
B
(9)
The following holds.
The species A is ACR. Moreover, there exists at least one c > 0 with g(c) = 0. Indeed, it can
be checked that
g(c) =




−κ1c1c2 + κ5c3
κ2c2c3 −κ3c2
2 −2κ4c2
2 + κ6c4
κ1c1c2 −κ2c2c3 + κ3c2
2 −κ5c3
2κ4c2
2 −κ6c4




is zero if and only if c2 = c3 = c4 = 0 or
c =
κ3κ5
κ1κ2
, s, κ3
κ2
s, 2κ4
κ6
s2

for some s ∈R>0.
The reaction network has deﬁciency 2. This can be easily checked, since
S = spanR











−1
0
1
0



,




0
1
−1
0



,




0
−1
0
1











and
δ = |C| −ℓ−dim S = 8 −3 −3 = 2.
9


## Page 10


There are two non-terminal complexes y ̸= y′ such that only the second entry of y′ −y is
diﬀerent from 0. Indeed, the two complexes B + C and C are non-terminal and their diﬀerence is B.
It is interesting to note that in this example the species B is not the ACR species, so the conclusions of
Theorem 5.1 do not hold.
The reaction network is conservative. Indeed, the vector (1, 1, 1, 1) is a positive conservation law.
Hence, all assumptions of Theorem 5.2 are fulﬁlled except for (2), and the deterministically modeled mass
action system is ACR. We will show that no extinction event can take place for the stochastic mass action
system, if we choose an initial condition X(0) with the minimal requirements that the conserved mass
m = X1(0) + X2(0) + X3(0) + X4(0) ≥2 and that X2(0) + X4(0) ≥1. Speciﬁcally, we will show that there
is no extinction set for any y →y′ ∈R which is reachable from X(0) .
Assume that a state x′ with λA+B→B+C(x′) = 0 is reachable from X(0). Then, there are two cases:
• We have x′
2 = 0. Note that the only reaction reducing the total number of B and D molecules is
2B →B + C, which decreases the total number by 1 but can only take place if at least 2 molecules of
B are present. Hence, at least one molecule of B or D is always present (because X2(0)+X4(0) ≥1),
which implies that x′
2 + x′
4 ≥1. More speciﬁcally, from x′
2 = 0 it follows that x′
4 ≥1, implying that
the reaction D →B can take place. Hence, a state with at least one molecule of B can be reached.
Either A + B →B + C is active at this state, or the following case can be considered.
• We have x′
2 > 0 and x′
1 = 0. We consider three further subcases:
– If x′
3 > 0, then a molecule of A can be created by the occurrence of C →A, which does not
modify the number of molecules of B. Hence, a state can be reached where A + B →B + C is
active.
– If x′
3 = 0 and x′
2 ≥2, then a molecule of B can be transformed into a molecule of C through
2B →B + C, which only consumes one molecule of B. This subcase is therefore reduced to the
previous one.
– If x′
3 = 0 and x′
2 = 1, then
2 ≤m = x′
1 + x′
2 + x′
3 + x′
4 = 0 + 1 + 0 + x′
4,
which implies that x′
4 ≥1 and an additional molecule of B can be created by the occurrence of
D →B. This subcase is therefore reduced to the previous one.
It follows from the above analysis that no extinction set for A + B →B + C is reachable from X(0). By
consecutive applycations of Proposition 4.1, it follows that the same occurs for all the other reactions as
well.
Remark 5.1. As noted above, in this case the two non-terminal complexes B + C and C diﬀer in the
second entry, but the second species (that is B) is not ACR. This is not what prevents the occurrence of an
extinction event. A similar analysis as before can be conducted on the following bimolecular mass action
system:
A+B
κ1
B+C
κ2
κ3
2B
B
κ4
κ5
2E
κ6
2D
C
κ7
A
D
κ8
E
(10)
For completeness, the analysis of (10) is carefully carried out in the Appendix. There, it is shown that the
species A is the only ACR species, with ACR value (κ3κ7)/(κ1κ2). Moreover, the only two non-terminal
complexes diﬀering in one entry are A+B and B, and they diﬀer in the ﬁrst entry. It is further shown that
(10) satisﬁes all the assumptions of Theorem 5.2, except for (2), and that no extinction event can occur
provided that
2X1(0) + 2X2(0) + 2X3(0) + X4(0) + X5(0) ≥4,
2X2(0) + X4(0) + X5(0) ≥2.
10


## Page 11


Example 3: assumption (3) cannot be removed
Consider the following bimolecular mass action system.
A+B
κ1
B+C
κ2
κ3
2B
C
κ4
A
(11)
The following holds.
The species A is ACR. Moreover, there exists at least one c > 0 with g(c) = 0. Indeed, it can
be checked that
g(c) =


−κ1c1c2 + κ4c3
κ2c2c3 −κ3c2
2
κ1c1c2 −κ2c2c3 + κ3c2
2 −κ4c3


is zero if and only if c2 = c3 = 0 or
c =
κ3κ4
κ1κ2
, s, κ3
κ2
s

for some s ∈R>0.
The reaction network has deﬁciency 1. Indeed,
S = spanR





−1
0
1

,


0
1
−1





and
δ = |C| −ℓ−dim S = 5 −2 −2 = 1.
There are no non-terminal complexes y ̸= y′ such that y′ −y has only one entry diﬀerent
from 0. This can be easily checked, since the only non-terminal complexes are A + B and C.
The reaction network is conservative. Indeed, the vector (1, 1, 1) is a positive conservation law.
We will now show that no extinction event can occur for the stochastically modeled mass action system,
provided that X2(0) ≥1 and the conserved mass m = X1(0) + X2(0) + X3(0) ≥2. Note that for any time
t ≥0 we have X2(t) ≥1, since the only reaction decreasing the number of molecules of B is 2B →B + C,
which removes one molecule of B and can only take place if at least two molecules of B are present. Assume
that a state x′ is reached from X(0), such that λA+B→B+C = 0. Then, it must be that x′
1 = 0. There are
two cases:
• We have x3 ≥1. Hence, a molecule of A can be created through the occurrence of C →A, and a
state is reached where the reaction A + B →B + C is active.
• We have x3 = 0. Hence, 2 ≤m = x′
2 which means that the reaction 2B →B + C can take place, and
this case is reduced to the previous one.
In conclusion, no extinction sets for A + B →B + C are reachable from X(0). It can be shown that the
same holds for all other reactions by applying Proposition 4.1 succesively.
Remark 5.2. By imposing more restricitve assumptions, we can formulate new conjectures. For example,
one may be tempted to try to prove that the existence of ACR species implies the occurrence of an extinction
event (in the stochastic model) for binary mass action systems in which the coeﬃcient of the species in all
complexes are either 0 or 1 (in more biological terms, this implies that there is no autocatalytic production).
However, we give here an example showing that this is not true. Consider the mass action system
A+B
κ1
C+E
κ2
κ3
B+D
C
κ4
A
B
κ5
D
κ6
E
κ7
(12)
11


## Page 12


We prove in the Appendix that A is an ACR species, and no extinction event can occur for the stochastic
model, provided that
X1(0) + X2(0) + X3(0) + X4(0) + X5(0) ≥2,
X2(0) + X4(0) + X5(0) ≥1.
Moreover, the only assumption of Theorem 5.2 that is not satisﬁed by (12) is (3).
6
Stationary distributions and equilibria of the associated deter-
ministic model
Connections between the equilibria of a deterministic mass action system and the stationary distributions
of the corresponding stochastic mass action system have been studied for a special class of models, called
complex balanced mass action systems [3, 5, 8, 10]. However, in general the existence of positive equilibria
for the deterministic mass action system does not imply the positive recurrence of the associated stochastic
mass action system, as shown in (1), (3), and (4).
Conversely, it was intuitively thought that the existence of a stationary distribution of the stochastic
mass action system would imply the existence of a positive equilibrium of the associated deterministic mass
action system. The idea was that a positive equilibrium could be related to the mean of the stationary
distribution, or to some sort of weighted average thereof. If that were true, the lack of positive equilibria
for the deterministic mass action system would have implied the transience of the states of the associated
stochastic model. In particular, for models with a conservative reaction network, the transience of positive
states would have implied the absorption at the boundary due to the ﬁniteness of the state space, hence
an extinction event.
The fact that lack of positive equilibria in the deterministic mass action system does not imply the
transience of the associated stochastic mass action system is, however, shown in (5). However, the question
was still open for models with a conservative network, and we close it here with the following bimolecular
example.
Consider the bimolecular mass action system
A+B
κ1
B+C
κ2
κ3
2B
C
κ4
A
κ5
E
A+D
κ6
D+E
κ7
κ8
2D
(13)
The following holds.
The reaction network is conservative. Indeed, it can be checked that (1, 1, 1, 1, 1) is a positive
conservation law.
There is no positive c with g(c) = 0 for a general choice of rate constants. We have
g(c) =






−κ1c1c2 + κ4c3 + κ5c5 −κ6c1c4
κ2c2c3 −κ3c2
2
κ1c1c2 −κ2c2c3 + κ3c2
2 −κ4c3
κ7c4c5 −κ8c2
4
−κ5c5 + κ6c1c4 −κ7c4c5 + κ8c2
4






By imposing c > 0, it follows that g(c) = 0 is equivalent to the system









c3 = κ3
κ2 c2
c3 = κ1
κ4 c1c2
c5 = κ8
κ7 c4
c5 = κ6
κ5 c1c4
The system has a positive solution if and only if
c1 = κ3κ4
κ1κ2
= κ5κ8
κ6κ7
.
12


## Page 13


Hence, no positive equilibria exist if the rate constants do not satisfy the above equality. It is interesting
to note that, when a positive equilibrium exists, the above equation implies that the species A is ACR.
All positive states are positive recurrent.
We will prove something more: each set of the form
Υm = {x ∈Z5
≥0 : x2, x4 ≥1, ∥x∥1 = m}
for some m ≥2 is closed and irreducible. Since the sets Υm are ﬁnite, it follows that they only contain
positive recurrent states. We obtain the desired result by noting that every positive state is contained in
some set Υm, for some m ≥2. So, it suﬃces to show that for a given m ≥2 the set Υm is closed and
irreducible.
We begin by showing that Υm is closed. This is equivalent to showing that from a state with a least
one molecule of B and one molecule of D, it is impossible to reach a state with no molecules of B or no
molecules of D. This follows from noting that the only reaction decreasing the number of molecules of B
is 2B →B + C, which decrease the number of molecules of B by one, but it can only occur if at least
two molecules of B are present. The same holds for the species D, whose molecules can only be decreased
through 2D →D + E.
To show that Υm is irreducible, we can show that for all x ∈Υm, the state (m −2, 1, 0, 1, 0) can be
reached from x, and viceversa. Indeed, if X(0) = x then the reaction 2B →B+C can take place x2−1 times,
and the reaction 2D →D+E can take place x4 −1 times. Hence, the state (x1, 1, x3 +x2 −1, 1, x5 +x4 −1)
is reached. Now, if all the molecules of C and E are consumed by the reactions C →A and E →A, then
the state (∥x∥1 −2, 1, 0, 1, 0) = (m −2, 1, 0, 1, 0) is reached.
Conversely, if X(0) = (m−2, 1, 0, 1, 0), then the reaction A+B →B+C can take place x2+x3−1 times,
and the reaction A+D →D+E can take place x4+x5−1 times. The state (x1, 1, x2+x3−1, 1, x4+x5−1)
is reached. From here, the state x can be reached if the reaction B + C →2B takes place x2 −1 times and
D + E →2E takes place x5 −1 times.
Appendix
Analysis of the mass action system (10)
Consider the bimolecular mass action system (10), which we repeat here for convenience.
A+B
κ1
B+C
κ2
κ3
2B
B
κ4
κ5
2E
κ6
2D
C
κ7
A
D
κ8
E
The following holds.
The species A is ACR. Moreover, there exists at least one c > 0 with g(c) = 0. Indeed, we
have that
g(c) =






−κ1c1c2 + κ7c3
κ2c2c3 −κ3c2
2 −κ4c2 + κ5c2
5
κ1c1c2 −κ2c2c3 + κ3c2
2 −κ7c3
2κ6c2
5 −κ8c4
κ4c2 −2(κ5 + κ6)c2
5 + κ8c4






is zero if and only if c2 = c3 = c4 = c5 = 0 or
c =
κ3κ7
κ1κ2
, s, κ3
κ2
s, 2κ4κ6
κ5κ8
s,
rκ4
κ5
s

for some s ∈R>0.
The reaction network has deﬁciency 2. Indeed,
S = spanR

















−1
0
1
0
0






,






0
1
−1
0
0






,






0
−1
0
0
2






,






0
0
0
1
−1

















13


## Page 14


and
δ = |C| −ℓ−dim S = 10 −4 −4 = 2.
There are two non-terminal complexes y ̸= y′ such that only the ﬁrst entry of y′ −y is
diﬀerent from 0. The two complexes A + B and B are non-terminal and their diﬀerence is A. Note that
A is the only ACR species, and A + B and B are the only two non-terminal complexes whose diﬀerence
has only one entry that is not zero.
The reaction network is conservative. Indeed, the vector (2, 2, 2, 1, 1) is a positive conservation
law.
We will show that no extinction event can take place for the stochastically modeled mass action system,
provided that
2X1(0) + 2X2(0) + 2X3(0) + X4(0) + X5(0) ≥4,
2X2(0) + X4(0) + X5(0) ≥2.
Assume that a state x′ with λA+B→B+C(x′) = 0 is reachable from X(0). Then, there are two cases.
• We have x′
2 = 0. For any t ≥0, consider the quantity
h(t) = 2X2(t) + X4(t) + X5(t).
The only reaction capable of reducing h(t) is 2B →B + C. This reaction decreases h(t) by 2, but
it can only take place if at least 2 molecules of B are present, in which case h(t) ≥4. Hence, under
the assumption that m(0) ≥2, for all t ≥0 we necessarily have h(t) ≥2. Since x′ is reachable from
X(0) and x′
2 = 0, we have x′
4 + x′
5 ≥2. By potentially letting the reaction D →E take place, we
may assume that x′
4 ≥2. Hence, the reaction 2E →B can occur and the number of molecules of B
can become positive. At this point, either a state where A + B →B + C is active is reached, or we
consider the following case.
• We have x′
2 > 0 and x′
1 = 0. We have three subcases:
– If x′
3 > 0, then a molecule of A can be created by the occurrence of C →A, which does not
modify the number of molecules of B. Hence, a state can be reached where A + B →B + C is
active.
– If x′
3 = 0 and x′
2 ≥2, then a molecule of B can be transformed into a molecule of C through
2B →B + C, which only consumes one molecule of B. This subcase is therefore reduced to the
previous one.
– If x′
3 = 0 and x′
2 = 1, then
4 ≤2x′
1 + 2x′
2 + 2x′
3 + x′
4 + x′
5 = 0 + 2 + 0 + x′
4 + x′
5,
which implies that x′
4 + x′
5 ≥2. By potentially using the reaction D →E, we can assume that
x′
4 ≥2 and a molecule of B can be created by the reaction 2E →B. This subcase is therefore
reduced to the previous one.
It follows that no extinction set for A + B →B + C is reachable from X(0). By consecutive applycations
of Proposition 4.1, it follows that the same occurs for all the other reactions as well, so no extinction event
can occur.
14


## Page 15


Analysis of the mass action system (12)
Consider the bimolecular mass action system (10), which we repeat here for convenience.
A+B
κ1
C+E
κ2
κ3
B+D
C
κ4
A
B
κ5
D
κ6
E
κ7
We have the following.
The species A is ACR. Moreover, there exists at least one c > 0 with g(c) = 0. Indeed, it can
be checked that
g(c) =






−κ1c1c2 + κ4c3
−κ1c1c2 + κ2c3c5 −κ3c2c4 −κ5c2 + κ7c5
κ1c1c2 −κ2c3c5 + κ3c2c4 −κ4c3
κ2c3c5 −κ3c2c4 + κ5c2 −κ6c4
κ1c1c2 −κ2c3c5 + κ3c2c4 + κ6c4 −κ7c5






is zero if and only if c2 = c3 = c4 = c5 = 0 or
c =

u, s, κ1u
κ4
s, κ5
κ6
s, κ5 + κ1u
κ7
s

for some s ∈R>0,
where u is the unique positive real number satisfying
κ2
1κ2κ6u2 + κ1κ2κ5κ6u −κ3κ4κ5κ7 = 0,
namely
u = −κ2κ5κ6 +
p
κ2
2κ2
5κ2
6 + 4κ2κ3κ4κ5κ6κ7
2κ1κ2κ6
.
The reaction network has deﬁciency 1. Indeed,
S = spanR

















−1
−1
1
0
1






,






0
1
−1
1
−1






,






1
0
−1
0
0






,






0
−1
0
1
0

















and
δ = |C| −ℓ−dim S = 8 −3 −4 = 1.
There are no non-terminal complexes y ̸= y′ such that y′ −y has only one entry diﬀerent
from 0. This can be easily checked, since the only non-terminal complexes are A + B and C.
The reaction network is conservative. Indeed, the vector (1, 1, 1, 1, 1) is a positive conservation
law.
We will show that under the assumption
m = X1(0) + X2(0) + X3(0) + X4(0) + X5(0) ≥2, X2(0) + X4(0) + X5(0) ≥1,
no extinction event can occur for the stochastic model. To this aim, ﬁrst note that the quantity
h(t) = X2(t) + X4(t) + X5(t)
15


## Page 16


is always greater than or equal to 1. Indeed, the only reaction that can decrease this quantity is
B + D →C + E.
However, under the action of this reaction h(t) decreases by 1, but the reaction is active only if at least one
molecule of B and one molecule of D are present, implying h(t) = 2. Assume that a state x′ is reachable
from X(0), with λA+B→C+E(x′) = 0. This implies that one of the two following cases occurs.
• We have x′
2 = 0. Since h(t) ≥1 for all t ≥0, it follows that at least one molecule of D or one molecule
of E is present. Hence, a molecule of B can be created by the reactions D →E and E →B. Either
a state where A + B →C + E is active is reached, or we are in the following case.
• We have x′
1 = 0 and x′
2 ≥1. One of the two following subcases holds.
– We have x′
3 ≥1. Then, a molecule of A can be created through C →A and a state is reached
where A + B →C + E is active.
– We have x′
3 = 0. Hence,
2 ≤m = x′
1 + x′
2 + x′
3 + x′
4 + x′
5 = x′
2 + x′
4 + x′
5.
Thanks to the reactions B →D, D →E, and E →B, we can transform all the molecules
of B, D, and E into at least one molecule of B and one molecule of D, so that a state where
B + D →C + E is active is reached. Upon the action of B + D →C + E, a molecule of C is
then produced, and this subcase reduces to the previous one.
In conclusion, no extinction set for A + B →C + E is reachable from X(0). By applying Proposition 4.1,
it follows that the same holds for the other reactions. Hence, no extinction event can occur.
References
[1] David F. Anderson, Daniele Cappelletti, Jinsu Kim, and Tung D. Nguyen. Tier structure of strongly
endotactic reaction networks. submitted, 2018.
[2] David F. Anderson, Daniele Cappelletti, Masanori Koyama, and Thomas G. Kurtz. Non-explosivity
of stochastically modeled reaction networks that are complex balanced. Accepted to Bulletin of Math-
ematical Biology, 2018.
[3] David F. Anderson and Simon L. Cotter. Product-form stationary distributions for deﬁciency zero
networks with non-mass action kinetics. Bull. Math. Bio., 78(12), 2016.
[4] David F. Anderson, Gheorghe Craciun, Manoj Gopalkrishnan, and Carsten Wiuf. Lyapunov func-
tions, stationary distributions, and non-equilibrium potential for reaction networks. Bull. Math. Bio.,
77(9):1744–1767, 2015.
[5] David F. Anderson, Gheorghe Craciun, and Thomas G. Kurtz. Product-form stationary distributions
for deﬁciency zero chemical reaction networks. Bulletin of mathematical biology, 72(8):1947–1970,
2010.
[6] David F. Anderson, Germ´an A. Enciso, and Matthew D. Johnston. Stochastic analysis of biochemical
reaction networks with absolute concentration robustness. Journal of The Royal Society Interface,
11(93):20130943, 2014.
[7] Karen Ball, Thomas G. Kurtz, Lea Popovic, and Greg Rempala. Asymptotic analysis of multiscale
approximations to reaction networks. The Annals of Applied Probability, 16(4):1925–1961, 2006.
[8] Daniele Cappelletti and Badal Joshi.
Graphically balanced equilibria and stationary measures of
reaction networks. SIAM Journal on Applied Dynamical Systems, 17(3):2146–2175, 2018.
[9] Daniele Cappelletti and Carsten Wiuf. Elimination of intermediate species in multiscale stochastic
reaction networks. The Annals of Applied Probability, 26(5):2915–2958, 2016.
[10] Daniele Cappelletti and Carsten Wiuf. Product-form poisson-like distributions and complex balanced
reaction systems. SIAM Journal of Applied Mathematics, 76(1):411–432, 2016.
16


## Page 17


[11] Daniele Cappelletti and Carsten Wiuf. Uniform approximation of solutions by elimination of inter-
mediate species in deterministic reaction networks. SIAM Journal on Applied Dynamical Systems,
16(4):2259–2286, 2017.
[12] Manoj Gopalkrishnan, Ezra Miller, and Anne Shiu. A geometric approach to the global attractor
conjecture. SIAM Journal on Applied Dynamical Systems, 13(2):758–797, 2014.
[13] J. Gunawardena. Chemical reaction network theory for in-silico biologists. Available for download at
http://vcp.med.harvard.edu/papers/crnt.pdf, 2003.
[14] Hye-Won Kang, Wasiur R KhudaBukhsh, Heinz Koeppl, and Grzegorz A Rempa la.
Quasi-
steady-state approximations derived from the stochastic model of enzyme kinetics. arXiv preprint
arXiv:1711.02791, 2017.
[15] Hye-Won Kang and Thomas G. Kurtz. Separation of time-scales and model reduction for stochastic
reaction networks. The Annals of Applied Probability, 23(2):529–583, 2013.
[16] Thomas G Kurtz. The relationship between stochastic and deterministic models for chemical reactions.
The Journal of Chemical Physics, 57(7):2976–2978, 1972.
[17] Thomas G. Kurtz. Strong approximation theorems for density dependent Markov chains. Stochastic
Processes and Their Applications, 6(3):223–240, 1978.
[18] James R. Norris. Markov chains. Cambridge university press, 1998.
[19] Peter Pfaﬀelhuber and Lea Popovic. Scaling limits of spatial compartment models for chemical reaction
networks. The Annals of Applied Probability, 25(6):3162–3208, 2015.
[20] Guy Shinar and Martin Feinberg. Structural sources of robustness in biochemical reaction networks.
Science, 327(5971):1389–1391, 2010.
17

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1809_04613v1_discrepancies_between_extinction_events_and_boundary_equilibria_in_reaction_netw
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1809_04613V1_DISCREPANCIES_BETWEEN_EXTINCTION_EVENTS_AND_BOUNDARY_EQUILIBRIA_IN_REACTION_NETW.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

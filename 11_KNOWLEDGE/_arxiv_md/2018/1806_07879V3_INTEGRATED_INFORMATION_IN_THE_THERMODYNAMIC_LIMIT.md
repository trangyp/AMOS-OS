---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1806.07879v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1806.07879v3_Integrated_information_in_the_thermodynamic_limit

> Source: 1806.07879v3_Integrated_information_in_the_thermodynamic_limit.pdf

> Pages: 13

---


## Page 1


arXiv:1806.07879v3  [q-bio.NC]  4 Jul 2018
Integrated information in the thermodynamic limit
Miguel Aguilera∗and Ezequiel Di Paolo†
IAS-Research Center for Life, Mind, and Society,
University of the Basque Country, Donostia, Spain
(Dated: July 5, 2018)
The capacity to integrate information is a prominent feature of biological and cognitive systems.
Integrated Information Theory (IIT) provides a mathematical approach to quantify the level of inte-
gration in a system, yet its computational cost generally precludes its applications beyond relatively
small models. In consequence, it is not yet well understood how integration scales up with the size
of a system or with diﬀerent temporal scales of activity, nor how a system maintains its integration
as its interacts with its environment. Here, we show for the ﬁrst time how measures of informa-
tion integration scale when systems become very large. Using kinetic Ising models and mean-ﬁeld
approximations from statistical mechanics, we show that information integration diverges in the
thermodynamic limit at certain critical points. Moreover, by comparing diﬀerent divergent tenden-
cies of blocks of a system at these critical points, we delimit the boundary between an integrated
unit and its environment. Finally, we present a model that adaptively maintains its integration
despite changes in its environment by generating a critical surface where its integrity is preserved.
We argue that the exploration of integrated information for these limit cases helps in addressing a
variety of poorly understood questions about the organization of biological, neural, and cognitive
systems.
I.
INTRODUCTION
Cognition emerges from the distributed activity of
many neural, bodily, and environmental processes. The
problem of large-scale integration of neural processes is
crucial for understanding how uniﬁed cognitive and be-
havioural states arise from the coordination of these dis-
tributed sources of activity. Evidence [1, 2] suggests this
integration process is non-decomposable: we cannot un-
derstand it in terms of modular components or timescales
of activity in a neural system nor can we decouple neural
activity from the external environment [3]. The diﬀerent
components and scales of the cognitive process are deeply
intertwined. Yet, the functional components of the pro-
cess are still able to maintain their diﬀerentiated charac-
teristics in order to generate complex adaptive patterns
of behaviour.
How can such an integrated, complex organization
emerge and be maintained? One of the most attractive
theories is that neural activity is coordinated into a co-
herent yet ﬂexible ‘dynamic core’ [4, 5], which balances
opposing tendencies of integration and segregation. The
interplay of these opposing tendencies generates infor-
mation (understood as described by information theory,
not in a semantic or intensional sense) that is highly di-
versiﬁed among functional parts of the nervous system,
and at the same time uniﬁed into a coherent whole, thus
displaying highly complex patterns of activity.
∗sci@maguilera.net; Also at ISAAC Lab, Arag´on Institute of En-
gineering Research, University of Zaragoza, Zaragoza, Spain.
† Also at Ikerbasque, Basque Foundation for Science, Bizkaia,
Spain, and the Centre for Computational Neuroscience and
Robotics,
Department of Informatics,
University of Sussex,
Brighton, UK.
Integrated information is deﬁned as the information
possessed by a system which is above and beyond the
information that is available from the sum of its parts.
Information integration was ﬁrst conceived of as linked to
consciousness [5, 6] but it can also be manifested with-
out awareness [7] and has been used more generally to
describe biological autonomy [8]. Although the topic of
information integration has received interest from diﬀer-
ent communities in recent years, we are still lacking a full
understanding of the principles that underlie this funda-
mental process: how integrative forces are deployed tem-
porally or spatially, how they cope with the surrounding
environment, or how they scale with the size of the sys-
tem.
Diﬀerent approaches have proposed ways to formalize
this idea; one of the most popular has been developed as
a measure connected to consciousness under the name of
integrated information theory (IIT, [6]). In its latest ver-
sions, IIT is based on interventionist notions of causality
to characterize the causal inﬂuences between the compo-
nents of a system [6, 8].
That is, instead of assessing
whether a system is uniﬁed into a coherent whole by
analysing its behaviour in regular conditions, IIT pro-
poses that the forces integrating the behaviour of the
system are better captured by observing its behaviour
under perturbations.
IIT postulates that any subset of elements of the sys-
tem is a mechanism [9] integrating information if its in-
trinsic cause-eﬀect power (i.e., its ability to determine
past and future states) is irreducible.
Irreducibility is
measured in terms of integrated information ϕ, which
when larger than 0 indicates that the subset of elements
at its current state constrains the past and future states
of the system in a way that cannot be decomposed in two
or more independent cause-eﬀect sets of relations. That
is, ϕ captures the level of irreducibility of the system,


## Page 2


2
understood in the sense that even the least disrupting
bipartition of the system into two disconnected halves
(this is called the minimum information partition, MIP)
would imply a loss of information in the causal power of
the system. Aside from computing integrated informa-
tion at the level of mechanisms, IIT postulates a com-
posite measure Φ, which is computed from the set of all
mechanisms (each one deﬁned by a value of ϕ) computed
in the original system and the system under bidiriectional
partitions. A system with Φ > 0 is described as forming
an irreducible unitary whole. Since many subsets of the
system may present Φ > 0, the boundaries of the system
are deﬁned around the subset with larger Φ. A detailed
description of IIT measures is provided in Appendix A.
Nevertheless, current formulations of IIT present some
limitations for studying brain organization. We propose
that, in order to extend current uses of IIT to capture
some important aspects of neural organization, we should
re-examine some of the main assumptions behind its con-
ception:
• Scalability. A system can present diﬀerent lev-
els of integration at diﬀerent spatial and tempo-
ral scales [10, 11] and, in general, it is not well
understood how integration behaves at diﬀerent
scales.
However, analyses of the properties of
brain-inspired statistical mechanical models have
unveiled how many processes in neural systems take
the form of phase transitions occurring in the ther-
modynamic limit, showing properties that diverge
as the size of the system scales up. Here we apply
models from statistical mechanics to describe in-
tegration in terms of the tendencies of the system
near the thermodynamic limit.
• Temporal deployment The latest formulations
of IIT [6] attempt to capture the dynamical na-
ture of neural systems by focusing on the dynam-
ics of causal processes, not taking the stationarity
or ergodicity of the system as initial assumptions.
Nevertheless, IIT is only measured at a single scale
of temporal activity, since it analyses integration
in the causal power of a mechanism from one time
step to the next. We propose a modiﬁcation of ϕ
to study integration along diﬀerent temporal spans,
showing that systems at critical points must be
evaluated for very long timescales.
• Non-decomposability. As we mentioned, empir-
ical evidence points to the non-decomposability of
cognitive processes. In its current formulation, IIT
considers elements outside the system under anal-
ysis as independent sources of noise. Here, we pro-
pose instead that the level of integration of a system
must be evaluated in the context of the other sys-
tems it is coupled to (therefore not assuming that
elements in the environment are just sources of sta-
tistical noise). This modiﬁcation allows us to cor-
rectly determine the boundary between a system
and its environment in the thermodynamic limit.
Some of the assumptions and modiﬁcations pointed out
here are explained later in the text, and a detailed ac-
count and comparison between IIT and our measure of
integrated information can be found in Appendix B. Part
of the reasons why some of the aspects above have not
yet been addressed is that, due to its computational com-
plexity, the application of current IIT measures is limited
to very small systems and short timescales. In general,
IIT has been tested in small toy models (e.g., [6, 12], al-
though some alternative formulations try to circumvent
this problem, see [13, 14]). In contrast, our approach,
apart from the modiﬁcations proposed above, introduces
some simpliﬁcations and approximations in order to mea-
sure integrated information as a system scales to very
large sizes.
Speciﬁcally, we introduce a simple kinetic
Ising model of inﬁnite size and quasi-homogeneous con-
nectivity, which presents an exact mean ﬁeld solution
that we use to simplify the calculation of integrated in-
formation ϕ of the mechanisms of a system.
We proceed as follows. First, we introduce the kinetic
Ising model and a mean ﬁeld approximation for solving it.
Then, we introduce a measure of integrated information
and how it can be computed for Ising models of inﬁnite
size.
Finally, we present the results of our method in
three scenarios of increasing complexity for depicting how
integrated information can be used to characterize an
integrated system interacting with an environment:
• In the ﬁrst scenario, we illustrate the measure in
a simple homogeneous model.
In the thermody-
namic limit, we can describe integrated informa-
tion as the susceptibility of the system to changes
in the direction of the minimum information par-
tition (MIP). Consequently, integrated information
diverges when the system is near a critical point.
• The second scenario depicts a system coupled to
an external environment, showing the system and
the system-environment compound both show in-
tegrated information diverging near a shared crit-
ical point.
Nevertheless, depending on the cou-
pling strength, the system and system-environment
mechanisms present diﬀerent speeds of divergence.
This allows us to delimit the dominant dynamical
unit where integration takes place.
• Finally, we tune the parameters of a system with
internal self-regulation in order to present high in-
tegration when interacting with a variety of envi-
ronments. The system’s internal inhibitory interac-
tions generate a critical surface in the direction of
the MIP which describe the viable region in which
its integration is maintained.
The results presented here represent a ﬁrst attempt at us-
ing integrated information theory to delimit the bound-
aries of a family of inﬁnite size systems that can be for-
mally solved. The interest of the study is twofold. First,
it allows us to check some of the assumptions of IIT and
propose some modiﬁcations to maintain its consistency in


## Page 3


3
the thermodynamic limit, and to propose a way to adapt
IIT measures for very large systems. Second, although
the results presented are obtained from relatively sim-
ple cases, they oﬀer an opportunity to speculate about
how the causal integrative forces of a system (both its
internal cohesion and the coupling with its environment)
might scale up when a system approaches the thermo-
dynamic limit. This provides an opportunity to address
unanswered questions about integrated organization of
biological and cognitive systems.
II.
MODEL
We start by describing a general model deﬁning causal
temporal interactions between variables.
Looking for
generality, we use the least structured statistical model
(i.e., a maximum caliber model [15]) deﬁning causal cor-
relations between pairs of units from one time step to
the next. We study a kinetic Ising model where N bi-
nary variables (Ising spins) si evolve in discrete time,
with synchronous parallel dynamics (Fig 1.A). Given the
conﬁguration of spins at the previous step, s(t −1) =
{s1(t−1), . . ., sN(t−1)}, the spins si(t) are independent
random variables drawn from the distribution:
p(si(t)|s(t −1)) =
eβsi(t)hi(t)
2 cosh(βhi(t))
(1)
where
hi(t) = Hi +
X
j
Jijsj(t −1)
(2)
The parameters Hi and Jij represent the local ﬁelds at
each spin and the couplings between pairs of spins, and
β is the inverse temperature of the model. Without loss
of generality, we assume β = 1.
A.
Mean ﬁeld kinetic Ising model
We focus on the particular case of a system of inﬁnite
size where Hi = 0. The system is divided into diﬀerent
regions (from 1 to 3 depending on the example), and the
coupling values Jij are positive and homogeneous for each
intra- or inter-region connections Jij =
1
NR JSR, where R
and S are regions of the system with sizes NR, NS and
i ∈S, j ∈R.
For a system of inﬁnite size (and all regions with also
inﬁnite size), a mean ﬁeld approximation allows to cal-
culate the ﬁeld of all units i belonging to the region S
as:
hi(t) =
X
R
JSRmR(t −1),
mR(t −1) =
1
NR
X
j∈R
sj(t −1)
(3)
where mR(t −1) is the mean ﬁeld of region R(t −1).
Now we can exactly deﬁne the update of the mean ﬁeld
variables using Eq 1 as:
mS(t) = tanh(
X
R
JSRmR(t −1))
(4)
B.
Integrated Information ϕ
We use a simpliﬁed version of the integrated eﬀect in-
formation described by IIT [6], implementing some modi-
ﬁcations to measure the scaling of integrated information
in the thermodynamic limit. In IIT, both causes and ef-
fects of a state are taken into account. For simplicity,
we consider only the eﬀects of a particular state. Also,
although IIT is deﬁned only for the immediate eﬀects
after one update of the state of the system, we deﬁne
integrated information ϕ(τ) for an arbitrary number of
updates of the system. See Appendix B for a list of the
diﬀerences between IIT and the measure employed here.
Given an initial state s(τ0), we deﬁne a ‘mechanism’
M (following IIT’s nomenclature) as a subset of units
{si(τ0)}i∈M. The integrated information of mechanism
M, ϕM, is deﬁned as the distance between the behaviour
of the original system to a system in which a partition
(from the set of possible bipartitions) is applied over the
units in M. Fig 1.B depicts an example of a partition.
When a partition is applied, the input coming from the
partitioned connections of the system is replaced by a
random unconstrained noise (binary white noise in the
case of an Ising model).
Once the partition is applied, the probability of the
state s(τ0 + τ) is computed after τ updates, injecting
noise at the partitioned elements during each update.
Then, integrated information is deﬁned as the distance
D between the conditional probability distributions at
t + τ:
ϕcut
M (τ) = D(p(s(τ0+τ)|s(τ0)), pcut(s(τ0+τ)|s(τ0))) (5)
where D(p1, p2) refers to the Wasserstein distance (also
known as earth mover’s distance) used by IIT to quantify
the statistical distance between probability distributions.
Here cut speciﬁes the partition applied over the elements
of mechanism M, cut = {Sc
1, Sc
2, Sf
1 , Sf
2 }, where Sc
1, Sc
2
design the blocks of a bipartition of the mechanism at the
current state {si(t)}i∈M, and Sf
1 , Sf
2 refer to the blocks
of a bipartition (not necessarily the same) of the updated
state of the units {si(t + 1)}i∈M. Fig 1.B represents the
partition cut = {{s1(t), s2(t)}, {s3(t)}, {s1(t + 1), s2(t +
1), s3(t + 1)}, {}}.
Speciﬁcally, IIT computes integrated information as
the value of ϕcut under the minimum information parti-
tion (MIP), which is the partition of mechanism with the
least diﬀerence to the original partition (i.e., ϕMIP
M
(τ) =
mincut ϕcut
M (τ)). We use ϕM(τ) to denote the minimum
information partition integrated information ϕMIP
M
(τ).


## Page 4


4
FIG. 1. Kinetic Ising model. A: Description of the inﬁ-
nite size kinetic Ising model. B: Description of the partition
schema used to deﬁne perturbations. Partitioned connections
(black arrows) are injected with random noise.
Note that some important modiﬁcations have been
made.
The most important one is that IIT considers
the element outside of the mechanism as unconstrained
sources of noise. As we show in Figure B2, this can radi-
cally change the results of integrated information theory,
provoking spurious divergences at points other than the
critical point. To preserve the consistency of our results,
we let elements outside the mechanism operate normally
(see Appendix B B3 for details).
C.
Integrated information in the mean ﬁeld model
We now show how integrated information can be com-
puted for the mean ﬁeld approximation of the Ising
model. Thanks to the mean ﬁeld approximation we can
simplify the calculation of the probability distributions
of trajectories p(s(τ0 + τ)|s(τ0)), pcut(s(τ0 + τ)|s(τ0)) to
a Markovian distribution dependent on the mean ﬁeld at
the previous step.
In general, p(s(τ0 + τ)|s(τ0)) can be computed recur-
sively applying the equation:
p(s(τ0 + τ)|p(τ0)) =
X
s(τ0+τ−1)
p(s(τ0 + τ)|s(τ0 + τ −1))p(s(τ0 + τ −1)|s(τ0))
(6)
In the kinetic Ising model of iniﬁne size, the mean ﬁelds
of the system’s regions are deterministic, and instead of
computing all possible paths of the system we can just
determine the evolution of the mean ﬁeld using Equa-
tion 4. Moreover, knowing the mean ﬁeld of each region
we can calculate the value of the eﬀective ﬁelds h(τ0 + τ)
received by each unit using Equation 3. Also, given the
mean ﬁeld value at a speciﬁc point, the posterior proba-
bility distribution of each unit is independent. Thus, us-
ing the value of h(τ0 + τ) computed evolving from s(τ0)
we can just take:
p(si(τ0 + τ)|s(τ0)) = p(si(τ0 + τ)|hi(τ0 + τ))
(7)
In this context, the calculation of the Wasserstein dis-
tance D is drastically simpliﬁed, and we can compute ϕ
as the sum of distances between independent binary vari-
ables, which is equivalent to computing the diﬀerence of
their mean values:
ϕcut
M (τ) = 1
2
X
R
NR|mR(τ0 + τ) −mcut
R (τ0 + τ)|
(8)
Once we can calculate ϕ, we still have the problem of
ﬁnding the MIP of the system. Luckily, since the con-
nectivity of the system is homogeneous for all nodes in
the same region, ﬁnding the MIP is equivalent to ﬁnding
the partition that cuts the lowest number of connections.
For inﬁnite size systems where inter-region connections
are not zero, the MIP will be one of the possible parti-
tions that isolate just one node of the system. Also, the
partition that isolates a single unit in time t always has
a smallest value of ϕ than the partition isolating a node
at time t+1, since partitioning the posterior distribution
corresponds to a larger diﬀerence between mR(τ0 + τ)
and mcut
R (τ0 + τ).
Thus, ﬁnding the MIP corresponds
to ﬁnding which region R of the system least aﬀects fu-
ture states when one node of the region is isolated in the
partition at time t (e.g., Fig 1.B).
Finally, we deﬁne a function FR(m(τ0), τ, {JS,R}) that
recursively applies the update rule in Eq 4 for τ steps
starting from an initial value with a mean ﬁeld value
m(τ0), such that mR(τ0 + τ) = FR(m(τ0), τ, J). In our
mean ﬁeld approximation, applying the MIP to the quasi-
homogeneous system described here is equivalent to just
removing one connection [16] between one or more pairs
of regions {S, R}cut, whereas the connections between
the rest of regions {S, R}uncut remain intact. Therefore
the update rule applied by function F to the partitioned
system is F(m(τ0), τ, {{JS,R}uncut, {(1−
1
NR )JS,R}cut}).
Assuming that the number of units per region is equal
to NR = rRN and P rR = 1, we get a simpliﬁed expres-
sion for the partitioned and unpartitioned terms:
F R
cut(m0, τ, x)
= FR(m0, τ, {{JS,R}uncut, {(1 −x
rR
)JS,R}cut})|
(9)
where m0 = m(τ0) and x =
1
N in the partitioned case
and x = 0 otherwise.
Now, computing the unparti-
tioned and partitioned cases case is equivalent to cal-
culating F R
cut(m0, τ, 0) and F R
cut(m0, τ, 1
N ) respectively.
Given this, assuming N →∞we calculate the ﬁnal form
of ϕ as a sum of the derivatives of function F R
cut(m0, τ, x):
ϕcut
M (τ)
= lim
N→∞
1
2
X
R
NR|F R
cut(m0, τ, 0) −F R
cut(m0, τ, 1
N )|
= 1
2
X
R
|rRF ′
R
cut(m0, τ, 0)|
(10)


## Page 5


5
FIG. 2. Homogeneous kinetic Ising model. A: Magne-
tization of the inﬁnite size kinetic Ising model. B: Value of
ϕMN (τ) for diﬀerent temporal spans. C: Value of ϕMN (τ →
∞) for an inﬁnite temporal span. D: Value of ϕMM (τ →∞)
for diﬀerent mechanisms of size M and an inﬁnite temporal
span.
where F ′(m0, τ, x) = dF ′(m0,τ,x)
dx
. Note that this deﬁnes
integrated information in similar terms as the magnetic
susceptibility typically used in Ising model to identify
critical points, although in this case the mean ﬁeld of the
system is diﬀerentiated along the parametrical direction
of the MIP.
III.
RESULTS
A.
Integrated information in a homogeneous
kinetic Ising model
As an example, we compute numerically the value of
ϕMN (τ) for a homogeneous kinetic Ising model contain-
ing just one region (as in Fig 1.A). The system only has
one parameter J describing all connections in the system.
For diﬀerent values of J, we compute ϕ for the system
starting from a state in the stationary solution. For doing
so, we need to know how to compute Fcut(m0, τ, x), that
is, how to compute the mean ﬁeld of units at a particular
time.
First, we numerically compute Fcut(m0, τ, x) and ϕMN
for diﬀerent values of J for the largest mechanism MN
of size N, and diﬀerent values of τ and m(τ0) equal to
the value at the stationary solution of the system. We
estimate the values of the derivative as F ′
cut(m0, τ, 0) =
(Fcut(m0, τ, dx) −Fcut(m0, τ, 0))/dx, using a value dx =
10−10. As we observe in Fig 2.B, the value of ϕMN (τ)
appears to diverge as τ grows [17].
Similarly, we numerically compute ϕMN(τ →∞) by
using the mean ﬁeld of the model iterating the equa-
tion m(t) = tanh(Jm(t −1)) until the diﬀerence in the
update is smaller than 10−15.
In Fig 2.C we observe
how ϕMN (τ →∞) shows an apparent divergence around
J = 1. Also, we compute the value of ϕMM (τ →∞) for
diﬀerent mechanisms of size M as a fraction of N. As
shown in Fig 2.D, the resulting value of integrated in-
formation still diverges but is smaller than the value of
ϕMN (τ) of the whole system, indicating that the system
is irreducible.
We can go beyond numerical computations and cal-
culate the analytic value of ϕMN (τ →∞) near the
point of divergence by approximating the values of
Fcut(m0, τ →∞, 0) around J = 1 as the value of m
that solves m = tanh(Jm). Note that, more generally,
we can compute Fcut(m0, τ →∞, x) just by substituting
J ←J(1 −x).
The system has a trivial solution at m = 0.
Also,
for J > 1 the solution at m = 0 becomes unstable and
a pair of solutions in a pitchfork bifurcation (Fig 2.A).
Although there is no analytic solution of the problem, we
can compute the value of m near J = 1 by approximating
the hyperbolic tangent by the ﬁrst two terms of its Taylor
series, ﬁnding that in the limit J →1+ we approximate:
Fcut(m0, τ →∞, x) = ±
s
3(J(1 −x) −1)
(J(1 −x))3
ϕMN (τ →∞) = 1
2

√
3 (2J −3)
2
p
J3(J −1)

(11)
Thus, we can conﬁrm that the value of integrated infor-
mation ϕMN(τ →∞) diverges when J →1+. This has
interesting implications. If the a system must maintain a
growing level of integration as its size increases, it needs
to be poised near a critical point that shows a divergence
of the values of ϕ.
B.
Integrated information for measuring
agent-environment asymmetries
We apply the proposed measure of integrated infor-
mation to the problem of determining the boundaries
of an agent interacting with an environment.
One of
the central aspects of agency is the existence of agent-
environment asymmetries [18], in which the part of the
system corresponding to the agent is able (to an extent)
to deﬁne the terms in which it relates to the surround-
ing milieu. We test our measure in two simple cases of
systems presenting asymmetries in their interaction.
We model a minimal case of agent-environment bidi-
rectional interaction with two regions, where only the
region corresponding to the ‘agent’ has the capacity to
self-regulate through recurrent connections (Fig 3.A). In
this case, we have two regions A and E, only A presenting
self-connections. The mean ﬁeld of the system is updated


## Page 6


6
as:
mA(t + 1) = tanh(1
2(JAAmA(t) + JAEmE(t)))
mE(t + 1) = tanh(JEAmA(t))
(12)
For
simplicity,
we
study
the
case
where
agent-
environment connections are symmetric JAE = JEA =
Jc, and JAA = Jr. We numerically compute that the
system has an similar solution than the previous case,
presenting a pitchfork bifurcation at a critical point
(Fig 3.B,D).
Moreover, we compute the value of ϕM(τ →∞) for
diﬀerent mechanisms.
For the case of the mechanism
covering the whole system M = AE, we look for the
MIP of the system by isolating single units of the mecha-
nism at s(t) (Fig 1.B). If we isolate a unit from region A,
two connections are cut (one with value Jr and one with
value Jc). Otherwise, if we isolate a unit from region E,
only one connection with value Jc is cut. Thus, this sec-
ond partition is always the MIP of the system (MIPAE).
For M = A, the only candidate for the MIP is isolating
one node from A, therefore cutting one connection with
value Jr (MIPA). Finally, for mechanism E there are no
connections within the mechanism and we can directly
conclude that ϕE = 0.
Now, the question is: can we consider A as an individ-
ual system or should we consider instead the coupled sys-
tem AE as an integrated unit? Assuming rA = rE = 0.5,
we deﬁne the values of integrated information as:
ϕA = 1
4(|
X
R=A,E
F ′
R
MIPA
(m0, τ, 0)|)
ϕAE = 1
4(|
X
R=A,E
F ′
R
MIPAE
(m0, τ, 0)|)
(13)
In Fig 3.C,E we estimate the value of ϕA, ϕAE for τ →
∞an initial value m0 corresponding to the stationary
solution of the system, and values of Jc = 0.8 (left) and
Jc = 1.2 (right). We observe that in all cases the values of
ϕA, ϕAE diverge next to the critical point. Nevertheless,
in the ﬁrst case when agent-environment connections are
weaker ϕA > ϕAE next to the critical point. In contrast,
for stronger couplings between agent and environment
ϕA < ϕAE in the vicinity of the critical point.
We validate this results by solving Eq 12 near critical-
ity. We do this by transforming it into a system of one
equation mA = tanh( 1
2(JAAmA + JAE tanh(JEAmA)))
and ﬁnding its Taylor series near mA = 0. We obtain
that near the critical point:
FA(m0, τ →∞, 0) =
s
3(JAA + JAEJEA −2)
JAEJ3
EA + 1
4(JAA + JAEJEA)3
FE(m0, τ →∞, 0) = tanh(JEAFA(m0, τ →∞, 0))
(14)
Similarly, FA(m0, τ →∞, x) and FE(m0, τ →∞, x) are
easily calculated by adding a (1 −x) factor to the parti-
tioned connections. Thus, we ﬁnd that the location of the
critical point which is the one satisfying JAA+JAEJEA =
2 (Fig 3.F). From here, we get:
F ′
A|MIPA = 3
2
−JAA
JAEJ3
EA + 1
4(JAA + JAEJEA)3
·(1
4(JAA + JAEJEA)2FA + 1
FA
)
F ′
E|MIPA =
JEA
cosh(JEAFA)2 F ′
A|MIPA
F ′
A|MIPAE = 3
2
−JAEJEA
JAEJ3
EA + 1
4(JAA + JAEJEA)3
·(J2
EA
3
+ 1
4(JAA + JAEJEA)2FA + 1
FA
)
F ′
E|MIPAE =
JEA
cosh(JEAFA(m0, τ →∞, 0))2 F ′
A|MIPAE
where FR
=
FR(m0, τ
→
∞, 0) and F ′
R|MIPS
=
F ′
R
MIPS
(m0, τ →∞, 0).
Near the critical point at (JAA + JAEJEA) →2+, the
values of integrated information are approximated by the
expressions:
ϕA = JAAK(JAA + JAEJEA −2)−1/2,
ϕAE = JAEJEAK(JAA + JAEJEA −2)−1/2,
K =
√
3(1 + JEA)
q
JAEJ3
EA + 1
4(JAA + JAEJEA)3
(15)
by deﬁning KA = JAAK and KAE = JAEJEAK we de-
scribe with these variables the level of integrated infor-
mation of the agent and the whole agent-environment
system near the critical point.
In Fig 3.G we observe
that there is a transition from the agent being the sys-
tem with highest integration to the agent-environment.
This illustrates that, near a critical point, the value of
integrated information scales up indeﬁnitely in an agent-
environment system. In the case of symmetric interaction
only for some cases the agent can be identiﬁed as the pre-
dominant integrated unit in the system, while in others
the agent-environment system is the predominant unit.
C.
Adaptive integrated information facing
environmental diversity
We have just used integrated information for delimit-
ing an agent interacting with a static environment. The
environment was ‘passive’ in the sense that it showed no
self-interaction.
This is not a common scenario, since
typically environments change and display their own dy-
namics. A key aspect of agency is the ability of an agent
to sometimes modulate the coupling with its environment
to preserve its individuality [18], generating an interac-
tional asymmetry between agent and environment. Thus,


## Page 7


7
FIG. 3. Asymmetric interaction in a kinetic Ising model. A: Basic agent connected to an environment. B, C, D, E:
Values of the mean ﬁelds (only positive values are shown) of the stable solution (top) and ϕ(τ →∞) (bottom) for the agent
and environment nodes of the model at stability for Jc = 0.8 (left) and Jc = 1.2 (right) and diﬀerent values of Jr. F: location
of the critical point in the parameter space for diﬀerent combinations of Jr, Jc. G: Constants multiplying ϕA(τ →∞) and
ϕAE(τ →∞) near the critical point, showing which is the most irreducible unit of the system.
a basic feature of living and cognitive sysetms is to dis-
play adaptive mechanisms regulating its coupling to the
environment to maintain their level of functional integra-
tion for a range of external environments.
In order to characterize a scenario that is more real-
istic in this sense, we model an agent with two internal
regions A and B, interacting with an environment E with
recurrent connections (Fig 4.A). A and B present feed-
back loops that we ﬁt in order to maintain integration
for a range of environmental parametric conﬁgurations.
The evolution of the system is described by:
m(t + 1) = tanh(Jm(t))
(16)
where m and J describe in vector and matrix notation
the mean ﬁelds and couplings of the three regions A, B
and E. We assume that the environment is deﬁned by
two parameters deﬁning the agent environment couplings
JAE = JBE = JEA = JEB = Jc and environmental self-
couplings JEE = 1. Values of JAA, JAB, JBA, JBB will
be tuned maximize integration. We also assume rS =
rM = rE = 1/3.
In particular, the system will be tuned to maximize the
integrated information of the agent AB, ϕAB while fac-
ing 5 diﬀerent environments deﬁned by values of Jc from
the set {0.8, 0.9, 1.0, 1.1, 1.2}. We calculate ϕ for diﬀer-
ent parameters as in previous cases, testing the possible
candidates for the MIP (in the case of ϕAB, the MIP can-
didates are isolating one node either from A or B) and
the one minimizing integrated information is chosen.
In order to ﬁnd the parameter values that maximize
ϕAB for the set of environments, we ﬁrst run a microbial
genetic algorithm [19] and then (using the parameters of
the agent with larger ﬁt) a Nelder-Mead algorithm [20]
to adjust the results. For both algorithms, the ﬁtness
function is deﬁned as the value of ϕAB(τ), with some ex-
ceptions. For reducing the computational cost, the value
of τ will be 104 for the genetic algorithm and 105 for the
Nelder-Mead algorithm. In order to avoid the case where
A and B are independent integrated units, ﬁtness will be
set to zero in the case that ϕA or ϕB are larger than ϕAB.
As well, ﬁtness is set to zero in the case where ϕAB does
not converge to a stationary value.
After running the genetic and Nelder-Mead algo-
rithms, we obtain an agent with parameters JAA =
0.09973671, JAB = −0.85774749, JBA = −0.8995672 and
JBB = 0.14326043. This agent presents negative weights
connecting A and B and positive self-coupling values.
Thus, each region will inhibit the behaviour of the other
while reinforcing itself, therefore regulating its activity to
maintain high integrated information for the presented
environments.
After tuning the parameters of the system, we evaluate
its behaviour for diﬀerent environments. For the values of
Jc used during training, we ﬁnd that the mean values of
regions A and B, mA and mB display a similar transition
than the previous examples (Fig 4.B shows the case of
Jc = 1, although other cases are similar).
Moreover,
we can observe that there is a divergence of the values
of ϕAB for a range of values of Jc (Fig 4.C). For larger
values of Jc the transition disappears and the values of
ϕAB do not diverge.
The example presented here displays an important
qualitative change in comparison with the previous one.


## Page 8


8
FIG. 4. Adaptive integration in a kinetic Ising model. A: Adaptive sensorimotor system connected to an environment.
B: Values of the mean ﬁelds of the stable solution for a Jc = 1. C: Values of ϕAB(τ) for diﬀerent values of Jc. F: The blue area
represents the surface in Jc and JEE where ϕ(τ →∞) diverges.
The value of ϕAB diverges but not only for a speciﬁc en-
vironment due to ﬁne tuning of its self-couplings as in
the previous case. Instead, the divergence is maintained
for an approximate range of Jc of [−1.21, 1.21]. More-
over, this divergence is also maintained if we modify the
value of JEE, displaying a surface in which the value of
ϕ(τ) diverges (Fig 4.D). This means that the points of
divergence from previous examples are transformed here
into a critical surface that maintains integration of the
system for a wide range of environmental parameters.
That is, the agent is able to self-regulate to some extent
to maintain its integration, and thus its viability as an
agent.
IV.
DISCUSSION
We have proposed a simpliﬁed measure of IIT measure
ϕ which, together with mean ﬁeld approximations in a
kinetic Ising model, allows us to capture for the ﬁrst time
integrated information in very large systems, up to the
thermodynamic limit. Using this method we are able to
compute ϕ for inﬁnite size mean ﬁeld kinetic Ising models
with quasi-homogeneous inﬁnite-range connectivity.
Our models, although highly idealized, allow us to
speculate about some of the properties of integrated neu-
ral organization. First, we observe that, despite the in-
ﬁnite size of the models, the amount of integrated infor-
mation is bounded for most of its parameter space. Only
near critical points does the level of total integrated infor-
mation diverge, suggesting that integrated entities need
to organize themselves close to critical points in their pa-
rameter space to maintain their level of integration as
their size grows. This suggests that it may be of greater
interest to describe brain organization in terms of diverg-
ing tendencies of IIT in diﬀerent modules rather than in
therms of the speciﬁc values of ϕ in ﬁnite systems.
Furthermore, we have shown how integrated informa-
tion can be used to deﬁne the boundaries between a
system and its environment by comparing the divergent
tendencies of their joint and individual integration. For
doing so, some of the assumptions of current formula-
tions of IIT had to be modiﬁed.
Our tests show that
integrated information cannot, in principle, be measured
in a brain independently of its environment (bodily and
extra-bodily), nor by assuming that the environment is
an independent source of noise.
Moreover, our results
show that near critical points in some cases both the
system and system-environment integrated information
diverges. Nevertheless, we have shown how to charac-
terize the dominant dynamical unit by comparing the
diﬀerence in the diverging tendencies between the two
conﬁgurations.
Our results connect the emergence of boundaries of in-
tegration with phenomena related to criticality. Systems
near critical points are maximally sensitive to changes in
some directions of their parameter space (generally mea-
sured as the susceptibility of the system to changes in
this parametrical direction). Here, we capture integrated
information measures by applying diﬀerent partitions to
the system which are interpreted as changes in particular
directions of the parameter space. Thus, the level of in-
tegrated information corresponds to the susceptibility of
the system for the minimum information partition, i.e.,
the partition with the less signiﬁcant eﬀect on the sys-
tem’s causal powers. In the framework of IIT, systems
highly sensitive to their minimum information partition
are interpreted as maximally irreducible units.
This could allow further simpliﬁcations in order to
measure integrated information in complex models or
even empirical setups. By testing the behaviour of a sys-
tem when perturbations in its components are introduced
(i.e., noise injected in partitioned connections), the inte-
grated information of a mechanism can be described as


## Page 9


9
the minimal susceptibility the set of perturbations from
diﬀerent partitions. The connection between information
integration and critical susceptibility allows us to spec-
ulate about the link between integration and properties
that have been postulated as pervasive of living beings
such as self-organized criticality [21].
By interpreting integrated information in terms of sus-
ceptibilities in the parametrical direction of partitions of
the system, we can think of integration as the sensitivity
of a system to the decoupling of the modules composing
it. In our last example, we show how internal regulation
results in the capacity for maintaining this susceptibil-
ity for a range of diﬀerent situations. We hypothesize
that this can be achieved by similar dynamics as those of
systems showing self-organized criticality, which are at-
tracted to critical points of maximum susceptibility. This
could be achieved in systems capable of self-organizing
near points where they maintain maximal sensitivity to
the integrity of their internal organization while they in-
teract with changing environments (e.g., maintaining in-
ternal invariances near critical surfaces [22]).
V.
CONCLUSION
The core ideas that IIT intends to capture apply to
a variety of poorly understood questions in biological
and cognitive systems. By introducing some modiﬁca-
tions to take into account diﬀerent temporal spans and
inﬂuences from the environment, and studying the be-
haviour of integration measures in the thermodynamic
limit, we have shown the existence of critical points that
maximise a system’s integration, for instance, an organ-
ism or a cognitive agent. The fact that our case stud-
ies remain general and abstract (we do not specify any
detail about the neural, sensorimotor, and environmen-
tal processes involved) suggests that robust individuation
and susceptibility towards loss of integration are inherent
consequences of maximising a tendency towards integra-
tion, and so they are likely to be observable trends in all
systems that are able to do so.
A limiting assumption in our approach is the homo-
geneity of the elements within a each region. Biological
systems cannot be assumed to present such a degree of
homogeneity and the variability in their components and
interactions has to be accounted for.
Our framework,
however, can take into account higher levels of hetero-
geneity by introducing a larger number of regions. In the
case of three regions we observe that tuning the param-
eters of the system results in the extensions of critical
points of diverging integration into regions of the pa-
rameter space.
We expect (but have not yet veriﬁed)
that increasing the number of interacting regions will
still result in critical regions of divergent integration. In
brain network models, it has been found that structural
heterogeneity can generate extended critical-like regions
[23], thus we may also expect this phenomenon to be re-
inforced in the presence of higher heterogeneity in our
models. Our results are also limited to models with sta-
tionary solutions where we can evaluate the stable so-
lution when the temporal span tends to inﬁnity.
This
is not a limitation of the method, though. The results
of more realistic systems presenting cyclic or chaotic dy-
namics could be harder to interpret, although they are in
principle tractable within the framework presented here
and could be explored in further work.
The models presented here allow a shift of focus to-
ward the integrative tendencies of systems as they grow
or evolve. This opens up the applicability of IIT to a
range of questions about changes over developmental and
evolutionary time. Even in the simple cases we have con-
sidered, the existence of critical points that maximise in-
tegration may be important for understanding apparent
jumps in complexity, including the transitions at the ori-
gin of life [24] or cognitive developmental transitions [25].
Focusing on the divergent tendencies of integration
measures, we are able to capture the asymmetry of agent-
environment interactions. Thinking interactions with the
environment in this terms is fruitful for grounding no-
tions such as the individuality or the autonomy of a sys-
tem. Often, these concepts have been formalized in terms
of self-determination and independence from an environ-
ment [26, 27]. By contrast, our examples show how both
integration of a system and integration between system
an environment can diverge together, while the level of in-
dividuality of the system can be quantiﬁed by the relative
divergence speed of both terms. This is a robust ﬁnding
obtained under the minimal assumptions and thus, we
suggest, a general trend in large complex systems. The
key data of interest as systems scale up are not so much
the absolute values of integrated information, but the
relative divergent tendencies of system integration and
system-environment integration.
In addition, by exploring diﬀerent kinds of agent-
environment conﬁgurations, we observe that agents as-
sumed to maximise integration are likely to do so robustly
for a range of environmental situations due to the exis-
tence of critical surfaces. The existence of these surfaces
that guarantee maximal integration is coherent with pos-
tulates at the theoretical foundations of adaptive systems
research, such as the existence of ‘regions of viability that
guarantee the integrity of an agent [28, 29]. While such
conditions of viability have often been imposed by the
designer or assumed to be given by evolutionary or ma-
terial constraints, our approach allows to think of them
as critical regions emerging at the level of the integrative
forces of the system. This illustrates how viability regions
could scale up from material or pre-given constraints to
regions deﬁned by increasing complexity of the integrated
activity of a system.
ACKNOWLEDGMENTS
M.A.
was
supported
by
the
UPV/EHU
post-
doctoral training program ESPDOC17/17 and project


## Page 10


10
TIN2016-80347-R funded by the Spanish Ministry of
Economy and Competitiveness.
Appendix A: IIT 3.0
In the last version of integrated information theory [6],
integrated information of a subset of elements of a sys-
tem is computed as follows. For a system of elements S
in state s, we describe the input-output relationship of
the system elements through its corresponding transition
probability function p, describing the probabilities of the
transitions from one state to another for all possible sys-
tem states. IIT requires that p satisﬁes the Markov prop-
erty (i.e., the state at time t only depends on the state at
time t −1), and that the current states of elements are
independent, conditional on the past state of the system.
This conditions are satisﬁed by the asymmetric kinetic
Ising model used here.
For any two subsets of S, called the mechanism M
and the purview P, we can deﬁne the cause and eﬀect
repertoires of P over M, that is, how M in its current
state {si(t)}i∈M, constrains the potential past or future
states of {si(t−1)}i∈P or {si(t+1)}i∈P. Cause and eﬀect
repertoires of the system are described by the probability
distributions p(Pt−1|Mt) = p({si(t−1)}i∈P|{si(t)}i∈M)
and p(Pt+1|Mt) = p({si(t + 1)}i∈P|{si(t)}i∈M).
The integrated cause-eﬀect information of M is then
deﬁned as the distance between the cause-eﬀect reper-
toires of the mechanism, and the cause-eﬀect repertoires
of their minimum information partition (MIP) over the
purview that is maximally irreducible,
ϕcause = max
P

min
cut
 D(p(Pt−1|Mt), pcut(Pt−1|Mt))

ϕeffect = max
P

min
cut
 D(p(Pt+1|Mt), pcut(Pt+1|Mt))

(A1)
where cut is a partition of the mechanism into two halves,
and pcut the cause or eﬀect probability distribution under
the partition,
cut = {M1, P1, M2, P2}
pcut(P|M) = p(P1|M1) ⊗p(P2|M2)
(A2)
The integrated information of the mechanism M is the
minimum of its corresponding integrated cause and eﬀect
information,
ϕ = min(ϕcause, ϕeffect)
(A3)
The integrated information of the entire system is then
deﬁned as the distance between the cause-eﬀect structure
of the system, and cause-eﬀect structure deﬁned by its
minimum information partition, eliminating constraints
from one part of the system to the rest:
Φ = min
cut D(C, Ccut)
(A4)
For both the integrated information of a mechanism
(ϕ) and the integrated information of a system (Φ), dis-
tance D is computed as the Wasserstein or earth movers
distance. Finally, if S is a subset of elements of a larger
system, all elements outside of S are considered as part
of the environment and are conditioned on their current
state throughout the causal analysis. Further details of
the steps described here can be found in reference [6]
Appendix B: Simpliﬁed integrated information ϕ
Measures in this paper are inspired by the IIT frame-
work, although we apply some modiﬁcations and simpli-
ﬁcations.
B1.
Temporal range
First, as we mentioned in the paper, we only compute
the value of ϕ for the eﬀects of the current system in a
posterior state t + τ, while IIT computes the minimum
of ϕcause and ϕeffect at t −1 and t + 1. However, IIT
can also deal with temporal scales. As IIT operates with
the transition probability matrix of a system, one could
compute this matrix from time t to time t + τ and apply
the operations for computing ϕ over it. This implies that
the noise injected by partitions in the connections that
are cut down is only injected at time t, and the system
behaves normally for the following steps. In our case, we
inject independent noise at every update from time t to
t + τ.
We can test the diﬀerence between the two approaches
in a homogeneous kinetic Ising model with Hi = 0 and
Jij = J. As we showed in the paper, applying a contin-
uous noise injection in partitions makes the value of ϕ
diverge around the critical point J = 1 as τ grows (Fig-
ure B2.A). Conversely, in we only apply an initial noise
injection at partitioned connections, we see that the mea-
sured ϕ operates in a diﬀerent way (Figure B2.B). In this
case, as τ increases, the value of ϕ decreases as the sys-
tem regains stability in its original position. Moreover,
for small values of τ the values of J with larger ϕ are
above the critical point. However, we observe that, the
closer we are to the critical point, the slower ϕ decreases.
This is due to a phenomena called ‘critical slowing down’,
a phenomena characteristic of critical dynamics in which
the response time of a system near criticality tends to
inﬁnity. Curiously, if we compute the cumulative sum of
the values of ϕ from 1 to τ, i.e. ϕcum =
τP
τ ′=1
ϕ(τ ′) (Fig-
ure B2.C), we observe that the result is identical to the
case of continuous noise injection at partitions.


## Page 11


11
FIG. B1. Temporal ranges of integration. (A) Values of ϕ(τ) using continuous injection of noise for diﬀerent values of J. (B)
Values of ϕ(τ) using an initial injection of noise for diﬀerent values of J. (C) Values of ϕcum =
τP
τ′=1
ϕ(τ ′) using an initial
injection of noise for diﬀerent values of J.
B2.
Purview
In IIT, integrated information of a mechanism ϕMIP
M
is evaluated not only for a particular mechanism M, but
also for a purview P. If the mechanism deﬁnes which
units of {si(t)}i∈M we take into account, the purview
deﬁnes which units of the future state {si(t + τ)}i∈P we
take into account. Given these subset of present and fu-
ture states, partitions are computed over the join space
of {si(t)}i∈M and {si(t + τ)}i∈P, and the purview P
with maximum integrated information for its MIP is se-
lected. Here for simplicity, we apply the partition over
{si(t)}i∈M and {si(t + τ)}i∈M, making the mechanism
and purview coincide, and the distance for computing in-
tegrated information is measured for the distance of all
elements of the system, not only the elements contained
in the purview.
Allowing more choices of purview could make a big
diﬀerence in certain systems, although in the quasi-
homogeneous systems tested in the paper the diﬀerences
are small.
B3.
Elements outside of a mechanism
More importantly, there are signiﬁcant diﬀerences from
the IIT framework in the way we treat the elements
that are outside of the evaluated mechanism M.
In
IIT, elements outside the mechanism are assumed to
be unconstrained (i.e., as random as possible). We de-
cided to modify this assumption because it can have dra-
matic eﬀects when measuring the behaviour of large sys-
tems. Speciﬁcally, assuming unconstrained elements out-
side the mechanism create an artifact that provokes a
shift in the critical point of the system (this will be de-
tailed in future work).
Let’s exemplify an example using an homogeneous
Ising model with local ﬁelds Hi = 0 and couplings
Jij = J. As we shown, compute the value of ϕ for the
whole system using continuous noise injection at parti-
tioned connection yields a divergence around the critical
point at J = 1. Now, we will show what is the behaviour
of its internal mechanisms assuming diﬀerent behaviours
of the units outside of the mechanism.
First, we compute values of mechanism covering a frac-
tion of the system M/N (since the system is homoge-
neous, any fraction we choose has the same behaviour)
assuming that the elements outside of the mechanism
M keep operating normally (Figure B2.A). In this case,
we observe that the divergence of ϕM is maintained, al-
though the value of ϕM decreases with the mechanism
size.
In contrast, if we accept IIT assumption and take the
elements of the mechanism as independent sources of
noise, the behaviour of ϕM changes radically.
In this
case, the divergence is maintained but takes place at a
diﬀerent value of the parameter J (Figure B2.B). This
happens because independent sources of noise have a zero
mean ﬁeld value, and thus the phase transition of the sys-
tem takes place at larger values of J that compensate the
units that now are contributing with a zero mean ﬁeld.
Thus, we think that considering the elements outside of
the mechanism as independent sources of noise can be
misleading about the operation of mechanisms that are
embedded in large systems.
A less loaded assumption could be maintaining the
state of the units outside of the mechanism with the static
values that they had at time t, that is, maintaining their
mean ﬁeld constant.
We can see at Figure B2.C that
this behaviour is also not satisfactory, since for mecha-
nism sizes smaller than N the value of ϕM decreases very
rapidly, and it is exactly zero at the critical point. We
can understand this thinking that the eﬀect of constant
ﬁelds is equal to adding a value of Hi equal to the in-
put from frozen units, therefore breaking the symmetry
of the system and precluding a phase transition.


## Page 12


12
FIG. B2. Eﬀects of the environment in integrated information. Values of ϕM(τ →∞) of a mechanism M of size M for diﬀerent
values of J, assuming that elements outside of the mechanism operate (A) normally, (B) as independent sources of noise, and
(C) as static input ﬁelds.
B4.
Mean ﬁeld approximation of partitioned
systems
We
simplify
the
calculation
of
the
probabili-
ties
p({si(t + τ)}i∈M|{si(t)}i∈M)
and
pcut{si(t +
τ)}i∈M|{si(t)}i∈M) by using a mean ﬁeld approximation
described by Equations 3 and 4.
In the case of partitioned systems for computing inte-
grated information, cutting connections injects uniform
noise on the input node. In the mean ﬁeld approxima-
tion, this would be equivalent to inject a zero mean ﬁeld
signal, which is equivalent to setting to zero the aﬀected
connection weights when computing hi(t).
B5.
Integrated conceptual information
Finally, once ϕ is computed, IIT proposes a second
level of calculations for computing integrated conceptual
information Φ where new bidirectional partitions are ap-
plied to the system. In our case, given the homogeneity
of the system, we do not compute conceptual information
since all the mechanisms composing each set have similar
behaviour. Thus, for simplicity we do not apply a second
level of partitions.
[1] Danielle
S.
Bassett
and
Michael
S.
Gazzaniga,
“Understanding
complexity
in
the
human
brain,”
Trends in Cognitive Sciences 15, 200–209 (2011).
[2] Luiz
Pessoa,
“Understanding
brain
networks
and
brain
organization,”
Physics of Life Reviews 11, 400–435 (2014).
[3] Miguel
Aguilera,
Manuel
G.
Bedia,
Bruno
A.
Santos,
and
Xabier
E.
Barandiaran,
“The
sit-
uated
HKB
model:
how
sensorimotor
spatial
coupling
can
alter
oscillatory
brain
dynamics,”
Frontiers in Computational Neuroscience 7 (2013), 10.3389/fncom.2013.00117.
[4] Francisco J. Varela, “Resonant cell assemblies: a new
approach to cognitive functions and neuronal synchrony,”
Biological Research 28, 81–95 (1995).
[5] Giulio Tononi and Gerald M. Edelman, “Consciousness
and Complexity,” Science 282, 1846–1851 (1998).
[6] Masafumi Oizumi,
Larissa Albantakis,
and Giulio
Tononi, “From the phenomenology to the mechanisms of
consciousness: integrated information theory 3.0,” PLoS
computational biology 10, e1003588 (2014).
[7] Liad Mudrik,
Nathan Faivre,
and Christof Koch,
“Information
integration
without
awareness,”
Trends in Cognitive Sciences 18, 488–496 (2014).
[8] William Marshall, Hyunju Kim, Sara I. Walker, Giulio
Tononi,
and Larissa Albantakis, “How causal analysis
can reveal autonomy in models of biological systems,”
Phil. Trans. R. Soc. A 375, 20160358 (2017).
[9] We use the term ‘mechanism’ in the technical sense de-
scribed later and not in the speciﬁc sense of eﬃcient
causality of the mechanical kind. We acknowledge that
diﬀerent forms of causal and enabling relations between
processes are possible and relevant, yet we retain the term
‘mechanism’ in this context to remain coherent with the
existing literature.
[10] Erik P. Hoel, Larissa Albantakis, William Marshall,
and Giulio Tononi, “Can the macro beat the micro?
Integrated information across spatiotemporal scales,”
Neuroscience of Consciousness 2016 (2016), 10.1093/nc/niw012.
[11] William
Marshall,
Larissa Albantakis,
and Giulio
Tononi,
“Black-boxing
and
cause-eﬀect
power,”
PLOS Computational Biology 14, e1006114 (2018).
[12] Larissa
Albantakis,
Arend
Hintze,
Christof
Koch,
Christoph Adami, and Giulio Tononi, “Evolution of in-
tegrated causal structures in animats exposed to envi-
ronments of increasing complexity,” PLoS computational
biology 10, e1003966 (2014).
[13] Adam B. Barrett and Anil K. Seth, “Practical Mea-
sures of Integrated Information for Time-Series Data,”
PLOS Computational Biology 7, e1001052 (2011).


## Page 13


13
[14] Masafumi Oizumi, Shun-ichi Amari, Toru Yanagawa,
Naotaka Fujii, and Naotsugu Tsuchiya, “Measuring In-
tegrated Information from the Decoding Perspective,”
PLOS Computational Biology 12, e1004654 (2016).
[15] Steve
Press,
Kingshuk
Ghosh,
Julian
Lee,
and
Ken
A.
Dill,
“Principles
of
maximum
entropy
and
maximum
caliber
in
statistical
physics,”
Reviews of Modern Physics 85, 1115–1141 (2013).
[16] Note that cutting a connection implies injecting uniform
noise, which in the mean ﬁeld approximation is equiva-
lent to substitute the input by a zero mean ﬁeld or just
removing the connection. This is an important approx-
imation that allow us to obtain the main results of the
paper, although it will only be valid when the size of the
system is inﬁnite and τ is larger than 1.
[17] Note that for larger τ the partition is applied for a longer
period of time, and therefore yielding larger integration
in some cases.
[18] Xabier E Barandiaran, Ezequiel Di Paolo, and Marieke
Rohde, “Deﬁning agency:
Individuality, normativity,
asymmetry, and spatio-temporality in action,” Adaptive
Behavior 17, 367–386 (2009).
[19] Inman Harvey, “The Microbial Genetic Algorithm,” in
Advances in Artiﬁcial Life. Darwin Meets von Neumann,
Lecture Notes in Computer Science (Springer, Berlin,
Heidelberg, 2009) pp. 126–133.
[20] J.
A.
Nelder
and
R.
Mead,
“A
Sim-
plex
Method
for
Function
Minimization,”
The Computer Journal 7, 308–313 (1965).
[21] Per Bak, Chao Tang,
and Kurt Wiesenfeld, “Self-
organized criticality,” Physical review A 38, 364 (1988).
[22] Miguel Aguilera and Manuel G. Bedia, “Adaptation to
criticality through organizational invariance in embodied
agents,” Scientiﬁc Reports 8, 7723 (2018).
[23] Paolo Moretti and Miguel A. Muoz, “Griﬃths phases
and the stretching of criticality in brain networks,”
Nature Communications 4, 2521 (2013).
[24] Sara
Imari
Walker
and
Paul
C.
W.
Davies,
“The
algorithmic
origins
of
life,”
Journal of The Royal Society Interface 10, 20120869 (2013).
[25] P. C. M. Molenaar
and H. L. J. van der Maas,
“Commentary on:
”Piaget’s stages:
The unﬁnished
symphony of cognitive development” by D.H. Feldman,”
New Ideas in Psychology 22 (2004), https://doi.org/10.1016/j.newide
[26] Nils
Bertschinger,
Eckehard
Olbrich,
Ni-
hat
Ay,
and
Jrgen
Jost,
“Autonomy:
An
information
theoretic
perspective,”
Biosystems Modelling Autonomy, 91, 331–345 (2008).
[27] David Krakauer, Nils Bertschinger, Eckehard Olbrich,
Nihat Ay, and Jessica C Flack, “The information theory
of individuality,” arXiv preprint arXiv:1412.2447 (2014).
[28] William Ross Ashby, Design for a brain; the origin of
adaptive behavior (New York, Wiley, 1960).
[29] Xabier E. Barandiaran and Matthew D. Egbert, “Norm-
establishing and norm-following in autonomous agency,”
Artiﬁcial Life 20, 5–28 (2014).

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
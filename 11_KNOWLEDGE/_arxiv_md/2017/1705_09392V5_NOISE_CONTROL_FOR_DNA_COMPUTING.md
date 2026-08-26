---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1705.09392v5
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1705.09392v5_Noise_Control_for_DNA_Computing

> Source: 1705.09392v5_Noise_Control_for_DNA_Computing.pdf

> Pages: 13

---


## Page 1


2017
Noise Control for DNA Computing
Tomislav Plesa1, Konstantinos C. Zygalakis2, David F. Anderson3, Radek Erban1
Abstract
Synthetic biology is a growing interdisciplinary ﬁeld, with far-reaching applications, which aims to design
biochemical systems that behave in a desired manner. With the advancement of strand-displacement DNA
computing, a large class of abstract biochemical networks may be physically realized using DNA molecules.
Methods for systematic design of the abstract systems with prescribed behaviors have been predominantly
developed at the (less-detailed) deterministic level. However, stochastic effects, neglected at the deterministic
level, are increasingly found to play an important role in biochemistry. In such circumstances, methods for
controlling the intrinsic noise in the system are necessary for a successful network design at the (more-detailed)
stochastic level. To bridge the gap, the noise-control algorithm for designing biochemical networks is developed
in this paper. The algorithm structurally modiﬁes any given reaction network under mass-action kinetics, in
such a way that (i) controllable state-dependent noise is introduced into the stochastic dynamics, while (ii) the
deterministic dynamics are preserved. The capabilities of the algorithm are demonstrated on a production-decay
reaction system, and on an exotic system displaying bistability. For the production-decay system, it is shown that
the algorithm may be used to redesign the network to achieve noise-induced multistability. For the exotic system,
the algorithm is used to redesign the network to control the stochastic switching, and achieve noise-induced
oscillations.
1Mathematical Institute, University of Oxford, Andrew Wiles Building, Radcliffe Observatory Quarter, Woodstock Road, Oxford, OX2 6GG, UK
2School of Mathematics, The University of Edinburgh, Maxwell Building, Peter Guthrie Tait Road, Edinburgh, EH9 3FD
3Department of Mathematics, University of Wisconsin–Madison, 480 Lincoln Drive, Madison Wi, 53706-1388
1. Introduction
Synthetic biology is an interdisciplinary ﬁeld of science and
engineering that aims to construct biochemical systems with
prescribed behaviors [1, 2]. At the theoretical level, the syn-
thetic systems may signiﬁcantly enhance our understanding
of biology. At the practical level, they may have broad appli-
cations, e.g. in medicine [3, 4, 5, 6, 7, 8], industry [9, 10], and
nanotechnology [11, 12]. The systems may also be of interest
to NASA for optimizing extraterrestrial explorations [13]. A
proof-of-concept for synthetic biology is a synthetic oscillator
called the repressilator, which was implemented in vivo [14].
The experimental advances since the repressilator range from
isolated synthetic biochemical networks, to microorganisms
containing partially, or even fully, synthetic DNA molecules
(synthetic life) [15, 16, 17, 18]. Examples include microor-
ganisms containing a synthetic bistable switch [19], and a
cell-density controlling quorum sensor [20], microorganisms
producing antimalarial drugs [7, 8], and synthetic systems
designed for tumor detection, diagnosis and adaptive drug-
response [4, 5].
The construction of biochemical networks in synthetic bi-
ology may be broken down into two steps: ﬁrstly, an abstract
system is constructed, displaying prescribed properties, and
taking the form of a chemical reaction network [21, 22, 23].
Secondly, the abstract network is mapped to a suitable phys-
ical network, which may then be integrated into a desired
environment (e.g. a test-tube, or a living cell) [24].
In the ﬁrst step of network construction, the goal is to
obtain an abstract network with desired dynamics. In this
paper, we consider two dynamical models of reaction net-
works under mass-action kinetics [25, 23]: the determinis-
tic model, and the stochastic model (see Methods for more
details). The deterministic model takes the form of the re-
action rate equations, which are ordinary-differential equa-
tions governing the time-evolution of the species concen-
trations [23, 25]. The stochastic model takes the form of
a Markov chain, which may be simulated using the Gille-
spie stochastic simulation algorithm [26]. The Gillespie al-
gorithm generates noisy copy-number time-series, with the
copy-number distribution matching that obtained from the
underlying chemical master equation [23, 25, 26, 27]. The
stochastic model is more-detailed, taking into an account
the discreteness of the species counts, and the stochastic na-
ture of the dynamics, which may be particularly important
in biochemistry, where reaction networks may contain low-
abundance species [31, 32, 14, 19, 22, 28, 29, 30]. On the
other hand, the deterministic model is less-detailed, and more
appropriate when the species are in high-abundance, and the
discreteness and stochasticity are negligible [33].
In the second step of network construction, the goal is to
engineer a physical network whose dynamics match well the
dynamics of a given abstract network, over a suitable time-
interval. Engineering an appropriate physical network may
proceed indirectly, by altering a preexisting physical network,
or directly, by engineering a network, which involves a given
set of physical species, from scratch. The advantage of the
arXiv:1705.09392v5  [q-bio.MN]  20 Jun 2017


## Page 2


Noise Control for DNA Computing — 2/13
former approach is that a preexisting network may display
(partially) desirable dynamical properties. However, such a
network may involve DNA and RNA molecules, proteins, and
metabolites [2], some of which may have complex biophys-
ical properties. Consequently, the disadvantage is that the
structure (and, thus, the dynamics) of such a network cannot
generally be modiﬁed in an arbitrary manner. In the latter
approach, one may choose the physical species, at the expense
of having to build a network from scratch. In the subﬁeld of
DNA computing, the latter approach is followed, and physi-
cal networks are engineered with chemical species consisting
exclusively of DNA molecules, interacting via the toehold-
mediated DNA strand-displacement mechanism [24]. DNA
production is systematic and cost-effective, and, due to the
fact that DNA biophysics is relatively well-understood, one
has more freedom in controlling the structure of correspond-
ing physical networks. More precisely, an abstract network
under mass-action kinetics may be mapped to a DNA-based
physical network provided it consists of up to second-order re-
actions, with rate coefﬁcients varying over up to six orders of
magnitude. The resulting physical network has identical deter-
ministic dynamics as the abstract network (in the asymptotic
limit of some of the kinetic parameters [24]), up to a scaling
of the dependent variables. A proof-of-concept for DNA com-
puting is a synthetic oscillator called the displacillator, which
was implemented in vitro [34].
While the deterministic model of reaction networks is less-
detailed, it is also simpler than the stochastic model, making it
attractive for guiding the construction of networks, predicting
accurately their mean-ﬁeld behavior [24, 14, 19, 21, 22, 23].
However, when noise is an important part of the dynamics,
the stochastic model has to be considered. The intrinsic noise,
often arising in biochemistry, may be controlled in two ways:
it may be decreased (e.g. as in [32]), in order to reduce the dif-
ferences between the stochastic and deterministic dynamics.
On the other hand, it may be increased, in a state-dependent
manner, in order to favorably change the stochastic dynamics.
In the language of molecular computing, the latter approach
corresponds to exploiting the proven computational power of
the stochastic reaction networks [35], by reprogramming the
underlying intrinsic noise. Let us note that exploitations of the
noise for enhancing biological functions have been reported
in applications [31, 30]. In this paper, we follow the latter
approach, and present the noise-control algorithm (given as
Algorithm 1) which maps an input reaction network to output
networks whose stochastic dynamics have an additional con-
trollable state-dependent noise. Importantly, the input and out-
put networks have identical deterministic model in appropriate
limits of some of the parameters introduced by the algorithm.
The algorithm may play a signiﬁcant role in the biochemical
network synthesis, allowing for a deterministic-stochastic hy-
brid approach. More precisely, when constructing abstract
and physical networks, one may use the deterministic model
to guide the construction, and then apply the algorithm to
favorably modify the intrinsic noise in the stochastic model,
while preserving the desired deterministic dynamics. The
algorithm may also be used to adjust the intrinsic noise to
favorably interact with environment-induced effects (e.g. ex-
trinsic noise).
The rest of the paper is organized as follows: we introduce
Algorithm 1 by applying it to the test network (1), which at the
deterministic level displays a globally attracting equilibrium
point. We show that the algorithm can favorably modify the
stationary probability distribution underlying (1) at arbitrary
points of the state-space, without inﬂuencing the determin-
istic dynamics. For example, it is shown that the algorithm
may be used to redesign (1) to achieve noise-induced multi-
modality (multistability). We then apply Algorithm 1 to the
exotic network (11), which at the deterministic level displays
a bistability involving an equilibrium point and a limit cy-
cle. The algorithm is used to redesign (11) to increase the
stochastic switching between the two attractors, and to achieve
noise-induced oscillations.
2. A One-species Regular System
Consider the one-species production-decay reaction network
ˆ
R(s), given by (1).
ˆ
R(s) :
∅
k1
−→s,
s
k2
−→∅,
(1)
dˆx
dt = k1 −k2 ˆx,
ˆx(0) = ˆx0.
(2)
Species s from network (1) reacts according to the two re-
actions with rate coefﬁcients k1,k2 ∈R≥, where R≥is the
set of nonnegative real numbers, and ∅is the zero-species
(denoting species which are not of interest). In this paper,
we assume reaction networks are under mass-action kinet-
ics, with the reactions taking place in unit-volume reactors.
Let us denote the concentration of species s from (1) at time
t ∈R≥by ˆx = ˆx(t) ∈R≥. The initial value problem for the
deterministic model (also called the drift) for network (1) is
given by system (2), with ˆx0 ≥0 (see also Methods). Since the
deterministic model (2) has a globally attracting equilibrium
point, given by k1/k2, network (1) is said to be regular [23].
Let us denote the copy-number of species s from (1) at
time t ≥0 by ˆX(t) ∈N0, where N0 is the set of integers.
Under the stochastic model, ˆX(t) is modelled as a continuous-
time, discrete-space Markov chain (see also Methods), which
can be generated by using the Gillespie stochastic simulation
algorithm [26]. Given ˆX(t), there will be a mean interevent
time until one of the reactions from (1) ﬁres. The mean
interevent time is given by 1/ ˆα( ˆX(t)), and when the event
takes place, the probability that the i-th reaction from (1) ﬁres
is equal to ˆαi( ˆX(t))/ ˆα( ˆX(t)), for i ∈{1,2}. Here, ˆα1 = k1,
and ˆα2(x) = k2x, are the so-called propensity functions of the
ﬁrst, and second, reactions from (1), respectively. Function
ˆα(x) = k1 +k2x is the total propensity function of network (1),
i.e. the sum of propensity functions of all the underlying
reactions.
We now wish to structurally modify network (1) in such
a way that the deterministic model from (2) is preserved,


## Page 3


Noise Control for DNA Computing — 3/13
while an arbitrary nonnegative function, deﬁned on a bounded
discrete domain, is added to the total propensity function
of (1). The latter requirement implies that the interevent time
would be controllably decreased in a state-dependent manner.
Equivalently, the two requirements imply that a controllable
state-dependent noise would be introduced into the stochastic
dynamics. We have designed a three-step algorithm, given
as Algorithm 1, which achieves such goals for arbitrary re-
action networks under mass-action kinetics. Let us describe
properties of the algorithm by applying it on network (1).
Firstly, we wish to introduce an additional species ¯s into
network (1), in such a way that species s and ¯s satisfy a pair-
wise stoichiometric conservation law. Secondly, we require
that the enlarged network has the same deterministic model
as network (1), despite the added species ¯s, which may be
achieved by adding another auxiliary species. More precisely,
let us consider network ˆ
R1(s, ¯s)∪R2
1(¯s), given by:
ˆ
R1(s, ¯s) :
¯s+I1 k1
−→s+I1,
s
k2
−→¯s,
R2
1(¯s) :
∅
1/µ
−−→I1,
¯s+I1 1/µ
−−→¯s.
(3)
Species s, ¯s,I1 from (3) react according to the four reactions
with rate coefﬁcients k1,k2,1/µ ∈R≥. Network ˆ
R1 = ˆ
R1(s, ¯s),
given in (3), is obtained from network ˆ
R = ˆ
R(s), given by (1),
in the following way: since the ﬁrst reaction in ˆ
R increases
copy-number of s by one, ¯s and I1 are added to the reactants
of the reaction, and I1 is added to the products, leading to the
ﬁrst reaction in ˆ
R1. Since the second reaction in ˆ
R decreases
copy-number of s by one, ¯s is added to the products, leading
to the second reaction in ˆ
R1. This ensures that the desired
conservation law holds. The superscript in I1 indicates that
species I1 is involved as a catalyst in a reaction of ˆ
R1 in which
s is increased by one. The subscript in R2
1 = R2
1(¯s) indicates
that the network describes production and decay of I1.
The initial value problem for the deterministic model of (3)
is given by
dx
dt = k1(c−x)y−k2x,
dy
dt = 1
µ (1−(c−x)y),
x(0) = x0,
y(0) = y0,
(4)
where x = x(t) ∈[0,c]∩R≥, and y = y(t) ∈R≥, are the con-
centrations of species s, and I1, from (3), respectively, with
x0,y0,c ∈R≥. We have used the kinetic conservation law
¯x(t) = c −x(t), where ¯x(t) is the concentration of species ¯s,
and c < ∞is a time-independent conservation constant. Note
that the conservation law truncates x-state-space. Let us now
describe relationships between systems (2) and (4), starting
with the weak statement: for c > k1/k2, and for any µ ≥0,
solutions of (2) and (4) are the same in the long-time limit
t →∞. More precisely, the x-component of the equilibrium
point of (4) is identical to the equilibrium point of (2), and
both are stable. In Supplementary Information (SI) Text,
we justify the strong statement: for sufﬁciently large c, and
for µ ≪1, solutions of (2) and (4), with the same initial con-
ditions, are approximately the same at each time t ≥0. For
these reasons, we call R2
1 a drift-corrector network.
2.1 Zero-Drift Network R3
1,1
Having completed the ﬁrst two steps, let us focus on the third
(and ﬁnal) step, in which we introduce arbitrary noise into the
stochastic model of (3), without inﬂuencing the deterministic
model (4). Let us start our consideration by embedding into (3)
network R3
1,1 = R3
1,1(s, ¯s), which is given by
R3
1,1(s, ¯s) :
s+ ¯s
k1,1
−−→2s,
s+ ¯s
k1,1
−−→2¯s.
(5)
The subscript in R3
1,1 indicates that the underlying reactions
have one molecule of s, and one of ¯s, as reactants. The two
reactions in (5) preserve the conservation law from (3). Fur-
thermore, they ﬁre with the same rates, with the ﬁrst reaction
leading to a unit-production, while the second to a unit-decay,
of species s. Consequently, embedding R3
1,1 into (3) does not
affect the underlying deterministic model (4), and we call R3
1,1
a zero-drift network. However, R3
1,1 does affect the underly-
ing stochastic model [36, 37, 38, 23]. To illustrate this, let us
consider network R3
1,1 in isolation: the reactions from (5) ﬁre
when X(t) ∈(0,C), but not when X(t) ∈{0,C}, so that R3
1,1
in isolation ﬁres until X(t) takes one of the extreme values
{0,C}. Here, X(t) ∈N0, and C ∈N, C < ∞, are the copy-
number of species s appearing in (3) and (5) at time t ≥0,
and the conservation constant, respectively. Let us note that a
possible biologically-relevant realization of network (5), aside
from DNA strand-displacement mechanism, is a dimer ver-
sion of the bifunctional histidine kinase/phosphatase reported
in [39].
In SI Text, we derive equation (SI7) which describes the
effective behavior of the Markov chain X(t) from network
ˆ
R1 ∪R2
1 ∪R3
1,1 in the limit µ →0, and it follows that the
effective total propensity function of the network, denoted
α(x), satisﬁes
α(x) ≈ˆα(x)+2K1,1β1,1(x), as µ →0,
(6)
ˆα(x) = k1 +k2x.
(7)
Function ˆα(x) has the form of the total propensity of net-
work (1), and K1,1β1,1(x) is the propensity function of reac-
tions in (5), with the scaled factors given by
K1,1 =
C
2
2
k1,1,
β1,1(x) =
C
2
−2
x(C −x).
(8)


## Page 4


Noise Control for DNA Computing — 4/13
Function β1,1(x) is displayed in Figure 1(a), where one can
notice its parabolic shape, arising from the underlying conser-
vation law X(t)+ ¯X(t) = C, which holds for all t ≥0, where
¯X(t) ∈N0 is the copy-number of ¯s at time t ≥0. Compar-
ing (6) and (7), it follows that, as µ →0, the mean interevent
time for X(t), from network ˆ
R1∪R2
1 ∪R3
1,1, is lower than that
of ˆX(t), from network (1), in the regions of the common state-
space where β1,1(x) ̸= 0, i.e. for x ∈(0,C). Coefﬁcient K1,1
controls by how much the interevent time is reduced. Equiv-
alently, β1,1(x), and K1,1, determine the support, and magni-
tude, respectively, of the state-dependent intrinsic noise which
network (5) introduces into the dynamics of network (3).
To study this further, in SI Text we derive the following
two equations (given as (SI9), and (SI13), respectively)
lim
K1,1→0 p(x) ≈
(
1
x!

k1
k2
x
exp

−k1
k2

,
if x ∈[0,C],
0,
otherwise,
(9)
lim
K1,1→∞p(x) ≈





1−1
C
k1
k2 ,
if x = 0,
1
C
k1
k2 ,
if x = C,
0,
otherwise,
(10)
where p(x) is the stationary probability mass function (PMF)
corresponding to network ˆ
R1 ∪R2
1 ∪R3
1,1 in the limit µ →0,
i.e. the probability that there are x molecules of species s as
µ →0 in the long-time limit t →∞. Let us interpret analytical
results (9) and (10), and compare them with the numerically
obtained counterparts. In Figure 1(b), we display numerically
obtained stationary x-marginal PMFs for different values of
K1,1, with the rest of the (dimensionless) parameters ﬁxed to
k1 = 2.5, k2 = 0.5, µ = 10−3, and C = 15. It can be seen that,
for K1,1 = 0, i.e. when the zero-drift network R3
1,1 does not
ﬁre, the PMF matches that of network (1), i.e. it is a Poisso-
nian, as predicted by (9). Let us note that the matching of the
PMFs of networks (1) and ˆ
R1 ∪R2
1 ∪R3
1,1 relies on choosing
sufﬁciently large rate coefﬁcients 1/µ in the drift-corrector
network R2
1. When K1,1 = 5, the PMF appears closer to a uni-
form distribution, than does the PMF when K1,1 = 0. Finally,
for the larger value K1,1 = 105, i.e. when zero-drift network
R3
1,1 ﬁres much faster than network ˆ
R1, the PMF redistributes
across the domain, accumulating at the boundary, and becom-
ing bimodal. This is in qualitative agreement with (6), and in
quantitative agreement with (10), which predicts p(0) ≈0.7
and p(15) ≈0.3. In Figure 1(c), a representative sample path
is shown, obtained by applying the Gillespie algorithm on
network ˆ
R1 ∪R2
1 ∪R3
1,1, when K1,1 = 105. Also shown is
a trajectory obtained by numerically solving the determinis-
tic model (4). Consistent with Figure 1(b), the sample path
switches between the boundary of the state-space, with a bias
towards the left boundary point x = 0. This is in contrast to
the deterministic trajectories, which are globally attracted to
the equilibrium point x = 5.
2.2 General Zero-Drift Networks R3
n,¯n
Zero-drift network R3
1,1(s, ¯s), given by (5), involves a sin-
gle molecule of s and ¯s as reactants, and adds the noise at
x ∈[1,C −1], i.e. in the interior of the state-space. Similar
networks may be used to add the noise at any point in the
state-space, without inﬂuencing the deterministic dynamics.
In particular, in (19) and (20), we present general zero-drift
networks R3
n,¯n(s, ¯s), which involve n molecules of s, and ¯n
of ¯s, as reactants, and add the noise at x ∈[n,C −¯n], where
n, ¯n ∈N0, and (n + ¯n) ≤C (see also SI Text). Embedding a
union of such networks, ∪(n,¯n)R3
n,¯n(s, ¯s), into (3), we arrive
at the result similar to (6), with K1,1β1,1(x) replaced by the
linear combination ∑(n,¯n) Kn,¯nβn,¯n(x). The scaled rate coefﬁ-
cient Kn,¯n, and function βn,¯n(x), are given as (S14), and (S15),
respectively, in SI Text, where we also justify that an arbi-
trary nonnegative function, with compact support, may be
approximated by a suitable sum ∑(n,¯n) Kn,¯nβn,¯n(x). To illus-
trate general zero-drift networks, let us start with embedding
into network (3) zero-drift network R3
5,10(s, ¯s), satisfying (19)
with n = 5 and ¯n = 10. In Figure 1(d), we show propensity
function β5,10(x), which is nonzero only at x = 5. In (e),
we show the numerically approximated stationary x-marginal
PMFs underlying network ˆ
R1 ∪R2
1 ∪R3
5,10 for different val-
ues of K5,10, with the rest of the parameters as in Figure 1(b).
One can notice that, under the action of network R3
5,10, the
PMF is gradually decreased to nearly zero at x = 5 (the de-
terministic equilibrium), and becomes bimodal, with the two
noise-induced maxima at x = 4 and x = 6. In (f), we show a
corresponding representative sample path.
In general, noise-induced multimodality may be achieved
by a suitable combination of zero-drift networks. For example,
let us synthetize noise such that the stationary PMF is trimodal,
and nearly zero everywhere, except at x ∈{1,7,11}. Such a
task may always be achieved by a suitable combination of the
basis zero-drift networks, i.e. those zero-networks that induce
noise only at a single point in the state-space (e.g. subnetwork
R3
5,10 with propensity function shown in Figure 1(d), see also
SI Text). In the present case, one could construct the thirteen
basis zero-drift networks which add large enough noise at
x ∈[0,15] \ {1,7,11}. Here, for simplicity, we achieve the
task with only four zero-drift networks. In Figures 1(g)–(i),
we consider network ˆ
R1 ∪R2
1 ∪(R3
0,15 ∪R3
2,9 ∪R3
8,5 ∪R3
12,0).
We denote β(x) ≡β0,15(x)+β2,9(x)+β8,5(x)+β12,0(x), and,
for simplicity, take K ≡K0,15 = K2,9 = K8,5 = K12,0. The
resultant propensity function β(x) is shown in (g), while in (h)
it can be seen that the PMF becomes trimodal for sufﬁciently
large K, with the maxima at x = {1,7,11}. This is consistent
with the corresponding representative sample path shown in
blue in panel (i), which display tristability. Let us note that,
while the stochastic dynamics display multistability in (c), (f)
and (i), the corresponding deterministic dynamics, also shown
in the plots, remain monostable.


## Page 5


Noise Control for DNA Computing — 5/13
3. A Two-species Exotic System
Consider the two-species network ˜
R(s1,s2), given by
˜
R(s1,s2) :
∅
k1
−→s1,
∅
k7
−→s2,
s1
k2
−→2s1,
s2
k8
−→∅,
2s1
k3
−→3s1,
s1 +s2
k9
−→s1 +2s2,
s1 +s2
k4
−→s2,
2s2
k10
−−→3s2,
2s1 +s2
k5
−→s1 +s2,
3s2
k11
−−→2s2,
s1 +2s2
k6
−→2s1 +2s2,
(11)
where species s1 and s2 react according to the eleven reactions
with rate coefﬁcients k1,k2,...,k11 ≥0. We denote the copy-
numbers of species s1, and s2, at time t by X1(t), and X2(t),
respectively. It was established in [21] that, for particular
choices of the rate coefﬁcients, the deterministic model of
reaction network (11), given as equation (SI17) in SI Text, ex-
hibits exotic dynamics: it undergoes a homoclinic bifurcation,
and displays a bistability involving a limit cycle and an equi-
librium point. On the other hand, it is demonstrated in [22]
that the stochastic model of (11) is not necessarily sensitive
to the deterministic bifurcation, and may effectively behave
in a monostable manner. The latter point is demonstrated in
Figure 2(c), where we show in red numerically approximated
x1-solutions of (SI17), one initiated in the region of attraction
of the equilibrium point, while the other of the limit cycle. For
a comparison, we also show in blue a representative sample
path generated by applying the Gillespie algorithm on (11). It
can be seen that the stochastic solution spends signiﬁcantly
more time near the deterministic equilibrium point. To gain a
clearer picture, we display in Figures 2(a), and (b), the joint,
and the x1-marginal, stationary PMFs, respectively, underly-
ing network (11), which have been obtained numerically for
the same parameter values as in Figure 2(c). In (b), one can
notice that the PMF is bimodal, but the left peak, correspond-
ing to the limit cycle, is signiﬁcantly smaller than the right
peak, which corresponds to the stable equilibrium point.
We now apply Algorithm 1 on network (11) to achieve
two goals. Firstly, we balance the sizes of the two peaks
of the stationary PMF from Figure 2(b), thereby forcing the
stochastic system to spend comparable amounts of time at
the two deterministic attractors. Secondly, we reverse the
situation shown in Figure 2(b), by making the left PMF
peak signiﬁcantly larger than the right one, thereby forc-
ing the stochastic system to spend most of the time near
the limit cycle. We could achieve the goals by introducing
species ¯s1, ¯s2 into (11), and using suitable basis zero-drift
networks. We take a simpler approach, by mapping (11)
to ˜
R1(s1,s2, ¯s2)∪R2
1(¯s2)∪(R3
0,C2−10(s2, ¯s2)∪R3
30,0(s2, ¯s2)),
which is given by equation (SI18) in SI Text. For our pur-
poses, only one of ¯s1, ¯s2 is sufﬁcient, since the stochastic
dynamics of s1 and s2 are coupled. We have chosen ¯s2 for
convenience, since x2-state-space may be truncated at a lower
value, C2 = 180, than x1-state-space (see also Figure 2 (a)).
The x2-component of the deterministic limit cycle satisﬁes
x2 ∈(10,30). Correspondingly, we introduce two zero-drift
networks: R3
0,C2−10(s2, ¯s2), and R3
30,0(s2, ¯s2), which redis-
tribute the PMF from x2 ∈[0,10], and from x2 ∈[30,C2],
respectively, to the limit cycle region, x2 ∈(10,30). We ﬁx
the scaled rate coefﬁcient K2
0,C2−10 to a large value (so that the
PMF is nearly zero for x2 ∈[0,10]), and vary the coefﬁcient
K2
30,0, which redistributes the PMF from the deterministic
equilibrium point to the limit cycle. Network R2
1(¯s2) is neces-
sary for the preservation of the deterministic dynamics of (11)
under the application of Algorithm 1.
In Figures 2(d), and (e), we show the joint, and x1-marginal,
stationary PMFs for an intermediate value of K2
30,0, when
the PMF is partially redistributed from x2 ∈[30,C2] to x2 ∈
(10,30), so that the two peaks in (e) are of comparable sizes.
In Figure 2(f), we show a representative sample path, obtained
by applying the Gillespie algorithm on network (SI18) from
SI Text, together with the deterministic trajectories obtained
by solving (SI17). One can notice that the stochastic system
now spends signiﬁcantly more time near the limit cycle, when
compared to (c). In Figures 2(f)–(g), we show analogous
plots, but for a sufﬁciently large value of K2
30,0, when the
PMF is almost completely redistributed from x2 ∈[30,C2] to
x2 ∈(10,30). Now, in contrast to Figures 2(a)–(c), the PMF
becomes essentially unimodal, and concentrated around the
limit cycle. Let us note that the red trajectories from Fig-
ures 2(f) and (i) were generated by numerically solving the
deterministic model of network (11), given by (SI17). For our
purposes, it is not necessary to solve the corresponding (stiff)
deterministic model of network (SI18). The reason is that
Algorithm 1 does not inﬂuence the deterministic equilibrium
points of a given reaction network, regardless of the choice
of the kinetic algorithm parameters. For example, while the
deterministic limit cycle is not necessarily preserved for the
algorithm parameters chosen in Figure 2(i), the enclosed de-
terministic unstable focus is necessarily preserved. Thus, the
blue sample path corresponds to noise-induced oscillations
either near a deterministic limit cycle, or near a deterministic
unstable focus.
4. Summary
In this paper, we have presented the noise-control algorithm,
which is given as Algorithm 1. The algorithm maps an input
chemical reaction network to output networks, all under mass-
action kinetics, by introducing appropriate additional species
and reactions, such that the output networks satisfy the follow-
ing two properties. Firstly, the output networks have the same
deterministic model as the input network, in appropriate limits
of some of the parameters (rate coefﬁcients) introduced by
the algorithm. Secondly, controllable state-dependent noise is
introduced into the stochastic model of the output networks.
Thus, Algorithm 1 may be used to control the intrinsic noise
of a given reaction network under mass-action kinetics, while


## Page 6


Noise Control for DNA Computing — 6/13
preserving the deterministic dynamics. Let us note that the
asymptotic conditions for the algorithm parameters are nec-
essary for preservation of the time-dependent deterministic
solutions. However, the time-independent deterministic so-
lutions (the deterministic equilibrium points), which capture
important features of the deterministic dynamics, are pre-
served under the algorithm even if the asymptotic conditions
are not satisﬁed.
The algorithm has been applied to a test problem, taking
the form of the one-species production-decay system given
by (1). Using analytical and numerical methods, we have
shown that the additional intrinsic noise, introduced by the
algorithm, may be used to favorably modify the stationary
probability mass function at arbitrary points in the state-space,
as demonstrated in Figure 1. For example, in Figure 1(b),
the noise is added to the whole interior of the state-space,
while in (e) only at a single point, in both cases resulting in
noise-induce bimodality. On the other hand, in Figure 1(h),
by adding the noise to speciﬁc points in the state-space, the
network is redesigned to display noise-induced trimodality.
As shown in Figures 1(c), (f), (i), the blue stochastic trajec-
tories display multistability, while the red deterministic ones
remain monostable.
The algorithm has also been applied to a more challenging
problem, taking the form of the two-species system given
by (11), which, for the parameters taken in this paper, at the
deterministic level displays a bistability involving an equi-
librium point and a limit cycle [21, 22]. At the stochastic
level, the system is signiﬁcantly more likely to be found near
the equilibrium point, as demonstrated in Figures 2(a)–(c).
We have used the algorithm to redesign network (11), so that
the stochastic system spends comparable amounts of time
near the two attractors, as demonstrated in Figures 2(d)–(f).
The network was also redesigned to display noise-induced
oscillations, which is shown in Figures 2(g)–(i).
The controllable state-dependent noise is generated by
Algorithm 1 using the zero-drift networks (19) and (20). Any
nonnegative function, deﬁned on a bounded discrete domain,
may be represented by a linear combination of propensity
functions induced by an appropriate union of the zero-drift net-
works. Thus, choosing suitable zero-drift networks, the algo-
rithm may control the intrinsic noise at arbitrary points in the
state-space of the stochastic dynamics of reaction networks.
The cost of such a precision in nose-control is a larger number
of reactants in the underlying zero-drift networks. However,
while the high-molecular reactions introduced by the algo-
rithm are more expensive to synthetize, they do not limit
applicability of Algorithm 1 to synthetic biology. The reason
for this is that such reactions may always be broken down
into sets of up-to bi-molecular reactions, with asymptotically
equivalent deterministic and stochastic dynamics [40, 41]. In
particular, a zero-drift network, involving reactions of order
(n+ ¯n), may be broken down into 2(n+ ¯n)−2 reactions of up-
to second-order, which may be readily mapped to DNA-based
physical networks.
Algorithm 1 may constitute a qualitatively novel ﬁnding
which will facilitate the progress of DNA computing [24].
In particular, a hybrid approach for constructing DNA-based
reaction networks may be used: the deterministic model may
be used to guide the construction of reaction networks, and
then Algorithm 1 may be applied to favorably reprogram
the intrinsic noise in the stochastic model, while preserving
the mean-ﬁeld behavior. The algorithm may be of critical
importance when the synthetic networks involve species at
low copy-numbers, since then the stochastic effects may play a
signiﬁcant role [31, 32, 14, 19, 22, 28, 29, 30], uncontrollably
contaminating the performance of the synthetic networks. In
such circumstances, Algorithm 1 may be used for controlling
the stochastic effects, enriching the DNA-based synthetic
systems with novel, noise-induced functionalities.
5. Methods
Let us consider the mass-action reaction network R given by
R(s1,...,sN) :
N
∑
i=1
cijsi
k j
−→
N
∑
i=1
c′
ijsi, j ∈{1,...,M},
(12)
where s1,...,sN are the reacting species, kj the reaction rate
coefﬁcients, and cij,c′
ij the stoichiometric coefﬁcients. Let
us denote by cj,c′
j ∈NN
0 the vectors of the stoichiometric
coefﬁcients of reaction j, and ∆x j = c′
j −c j.
The deterministic model of reaction network (12) is given
by the following system of ordinary-differential equations
(ODEs), also known as the reaction rate equations [23, 25]:
dx
dt =
M
∑
j=1
kjxc j∆xj,
i ∈{1,...,N}.
(13)
Here, x = x(t) ∈RN
≥is the vector of species concentrations,
i.e. xi(t) is the concentration of species si at time t, and
xcj ≡∏N
l=1 x
cl j
l , with the convention that 00 ≡1.
The stochastic model of reaction network (12) is given by
the following system of difference-differential equations, also
known as the chemical master equation (CME) [23, 25, 27]:
∂
∂t p(x,t) = L p(x,t) = ∑
j
(E
−∆x j
x
−1)
 αj(x)p(x,t)

.
(14)
Here, p(x,t) is the probability mass function (PMF), i.e. the
probability that the vector of copy-numbers X = X(t) ∈NN
0
of species s1,...,sN at time t is given by x. Linear operator
L is called the forward operator, and step operator E
−∆x j
x
is
such that E
−∆x j
x
p(x,t) = p(x−∆xj,t). Function αj(x) is the
propensity function [23, 25] of the j-th reaction from (12),
and is given by
αj(x) = kjxc j = kj
N
∏
l=1
x
cl j
l ,
(15)


## Page 7


Noise Control for DNA Computing — 7/13
where x
cl j
l
denotes a falling factorial of xl, i.e. x
cl j
l
≡xl(xl −
1)...(xl −cl j +1).
Acknowledgments
The authors would like to thank the Isaac Newton Institute
for Mathematical Sciences, Cambridge, for support and hospi-
tality during the programme “Stochastic Dynamical Systems
in Biology: Numerical Methods and Applications”, where
work on this paper was undertaken. The authors would also
like to thank John J. Tyson (Department of Biology, Virginia
Polytechnic Institute and State University, USA) for a discus-
sion on a possible realization of network (5) via a bifunctional
histidine kinase/phosphatase from [39]. This work was sup-
ported by EPSRC grant no EP/K032208/1. This work was
partially supported by a grant from the Simons Foundation.
Konstantinos C. Zygalakis was supported by the Alan Tur-
ing Institute under the EPSRC grant EP/N510129/1. David
F. Anderson would like to acknowledge the NSF grant NSF-
DMS-1318832, and Army Research Ofﬁce grant W911NF-
14-1-0401. Radek Erban would also like to thank the Royal
Society for a University Research Fellowship.
References
[1] Endy, D., 2005. Foundations for Engineering Biology.
Nature, 483: 449–453.
[2] Andrianantoandro, E., Basu, S., Karig, D. K., Weiss,
R., 2006. Synthetic biology: new engineering rules for
an emerging discipline. Molecular Systems Biology, 2:
2006.0028.
[3] Abil, Z., Xiong, X., Zhao, H., 2015. Synthetic Biology
for Therapeutic Applications. Molecular Pharmaceutics,
12(2): 322–331.
[4] Anderson, J. C., Clarke, E. J., Arkin, A. P., Voigt, C.
A., 2006. Environmentally Controlled Invasion of Can-
cer Cells by Engineered Bacteria. Journal of Molecular
Biology, 355(4): 619–627.
[5] Benenson, Y., Gil, B., Ben-Dor, U., Adar, R., and Shapiro,
E., 2004. An Autonomous Molecular Computer for Logi-
cal Control of Gene Expression. Nature, 429: 423–429.
[6] Goeddel, D. V., Kleid, D. G., Bolivar, F., Heyneker, H.
L., Yansura, D. G., Crea, R., Hirose, T., Kraszewski,
A., Itakura, K., and Riggs, A. D., 1979. Expression in
Escherichia Coli of Chemically Synthesized Genes for
Human Insulin. Proc. Natl Acad. Sci. USA, 76(1): 106–
110.
[7] Ro, D., Paradise, E. M., Ouellet, M., Fisher, K. J., New-
man, K. L., Ndungu, J. M., Ho, K. A., Eachus, R. A.,
Ham, T. S., Kirby, J., Chang, M. C. Y., Withers, S. T.,
Shiba, Y., Sarpong, R., and Keasling, J. D., 2006. Produc-
tion of the antimalarial drug precursor artemisinic acid in
engineered yeast. Nature, 440: 940–943.
[8] Westfall, P. J., et al, 2012. Production of amorphadiene
in yeast, and its conversion to dihydroartemisinic acid,
precursor to the antimalarial agent artemisinin. Proc. Natl
Acad. Sci. USA, 109: E111–E118.
[9] Widmaier, D. M., Tullman-Ercek, D., Mirsky, E. A., Hill,
R., Govindarajan, S., Minshull, J., and Voigt, C. A., 2009.
Engineering the Salmonella Type III Secretion System to
Export Spider Silk Monomers. Molecular Systems Biol-
ogy, 5(309).
[10] Sedlak, M., and Ho, W. Y., 2004. Production of Ethanol
from Cellulosic Biomass Hydrolysates Using Geneti-
cally Engineered Saccharomyces Yeast Capable of Cofer-
menting Glucose and Xylose. Applied Biochemistry and
Biotechnology, 114(1): 403–416.
[11] Ball, P., 2005. Synthetic Biology for Nanotechnology.
Nanotechnology, 16: R1–R8.
[12] Jungmann, R., Renner, S., and Simmel, F. C., 2008. From
DNA Nanotechnology to Synthetic Biology. Applied Bio-
chemistry and Biotechnology, 2(2): 99–109.
[13] Menezes, A. A., Cumbers, J., Hogan, J. A., Arkin, A.
P., 2015. Towards synthetic biological approaches to re-
source utilization on space missions. Journal of The Royal
Society Interface, 12(102): 20140715.
[14] Elowitz, M. B., Leibler, S., 2000. A Synthetic Oscillatory
network of Transcriptional Regulators. Nature, 403: 335–
338.
[15] Deamer, D., 2005. A giant step towards artiﬁcial life?
Trends in Biotechnology, 23(7): 336–338.
[16] Glass, J. I,Assad-Garcia, N., Alperovich, N., Yooseph, S.,
Lewis, M. R., Maruf, M., III, C. A. H., Smith, H. O., and
Venter, J. C., 2006. Essential Genes of a Minimal Bac-
terium. Proceedings of the National Academy of Sciences,
103(2): 425–430.
[17] Gibson, D. G., Benders, G. A., Andrews-Pfannkoch, C.,
Denisova, E. A., Baden-Tillson, H., Zaveri, J., Stockwell,
T. B., Brownley, A., Thomas, D. W., Algire, M. A., Mer-
ryman, C., Young, L., Noskov, V. N., Glass, J. I., Venter,
J. C., Ill, C. A. H., Smith, H. O., 2008. Complete Chemi-
cal Synthesis, Assembly, and Cloning of a Mycoplasma
genitalium Genome. Science’s STKE, 319(5867): 1215–
1220.
[18] Gibson, D.G., et al, 2010. Creation of a bacterial cell
controlled by a chemically synthesized genome. Science,
329(5987): 52–56.
[19] Gardner, T. S., Cantor, C. R., and Collins, J. J., 2000.
Construction of a Genetic Toggle Switch in Escherichia
Coli. Nature, 403: 339–342.
[20] You, L., Cox Ill, R. S., Weiss, R., and Arnold, F. H., 2004.
Programmed Population Control by Cell-Cell Communi-
cation and Regulated Killing. Nature, 428: 868–871.


## Page 8


Noise Control for DNA Computing — 8/13
[21] Plesa, T., Vejchodsk´y, T., and Erban, R., 2016. Chemical
Reaction Systems with a Homoclinic Bifurcation: An
Inverse Problem. Journal of Mathematical Chemistry,
doi:10.1007/s10910-016-0656-1.
[22] Plesa, T., Vejchodsk´y, T., and Erban, R., 2016. Test
Models for Statistical Inference:
Two-Dimensional
Reaction Systems Displaying Limit Cycle Bifurca-
tions and Bistability, chapter contribution submitted
to Stochastic Dynamical Systems, Multiscale Model-
ing, Asymptotics and Numerical Methods for Compu-
tational Cellular Biology, Ed. D. Holcman, available as
https://arxiv.org/abs/1607.07738.
[23] ´Erdi, P., T´oth, J. Mathematical Models of Chemical Re-
actions. Theory and Applications of Deterministic and
Stochastic Models. Manchester University Press, Prince-
ton University Press, 1989.
[24] Soloveichik, D., Seeling, G., Winfree, E., 2010. DNA as
a Universal Substrate for Chemical Kinetics. Proceedings
of the National Academy of Sciences, 107(12): 5393–
5398.
[25] Anderson, D. F., Kurtz, T. G. Stochastic Analysis of Bio-
chemical Systems. Springer, 2015.
[26] Gillespie, D., 1977. Exact Stochastic Simulation of Cou-
pled Chemical Reactions. Journal of Physical Chemistry,
81(25): 2340–2361.
[27] Van Kampen, N. G. Stochastic Processes in Physics and
Chemistry. Elsevier, 2007.
[28] Erban, R., Chapman, S. J., Kevrekidis, I. and Vejchodsk´y,
T., 2009. Analysis of a stochastic chemical system close
to a SNIPER bifurcation of its mean-ﬁeld model. SIAM
Journal on Applied Mathematics, 70(3): 984–1016.
[29] Duncan, A., Liao, S., Vejchodsk´y, T., Erban, R., Grima,
R., 2015. Noise-induced multistability in chemical sys-
tems: discrete vs continuum modelling. Physical Review
E, 91, 042111.
[30] Yates, C., Erban, R., Escudero, C., Couzin, I., Buhl, J.,
Kevrekidis, I., Maini, P., and Sumpter, D., 2009. Inherent
Noise can Facilitate Coherence in Collective Swarm Mo-
tion. Proceedings of the National Academy of Sciences,
106(14): 5464–5469.
[31] Vilar, J. M. G., Kueh, H. Y., Barkai, N. and Leibler, S.,
2002. Mechanisms of Noise-resistance in Genetic Oscil-
lators. Proceedings of the National Academy of Sciences
of the United States of America, 99(9): 5988–5992.
[32] Dublanche, Y., Michalodimitrakis, K., Kummerer, N.,
Foglierini, M. and Serrano, L., 2006. Noise in Transcrip-
tion Negative Feedback Loops: Simulation and Experi-
mental Analysis. Molecular Systems Biology, 2(41): E1–
E12.
[33] Kurtz, T. G., 1972. The Relationship between Stochas-
tic and Deterministic Models for Chemical Reactions.
Journal of Chemical Physics, 57: 2976–2978.
[34] Srinivas, N. Programming Chemical Kinetics: Engineer-
ing Dynamic Reaction Networks with DNA Strand Dis-
placement. PhD Thesis, California Institute of Technol-
ogy, Pasadena, California, 2015.
[35] Soloveichik, D., Cook, M., Winfree, E., Bruck, J., 2008.
Computation with Finite Stochastic Chemical Reaction
Networks. Natural Computing, 7(4): 615–633.
[36] Ohkubo, J., Shnerb, N., and Kessler, D. A., 2008. Tran-
sition Phenomena Induced by Internal Noise and Quasi-
Absorbing State. Journal of the Physical Society of Japan,
77, 044002.
[37] Biancalani, T., Dyson, L., and McKane, A. J., 2014.
Noise-Induced Bistable States and Their Mean Switching
Time in Foraging Colonies. Physical Review Letters, 112,
038101.
[38] Saito, N., and Kaneko, K., 2015. Theoretical Analysis of
Discreteness-Induced Transition in Autocatalytic Reac-
tion Dynamics. Physical Review Letters, 91, 022707.
[39] Subramanian, K., Paul, M. R., Tyson, J. J., 2013. Poten-
tial Role of a Bistable Histidine Kinase Switch in the
Asymmetric Division Cycle of Caulobacter crescentus.
PLOS Computational Biology, 9, e1003221.
[40] Wilhelm, T., 2000. Chemical systems consisting only of
elementary steps - a paradigma for nonlinear behavior.
Journal of Mathematical Chemistry, 27: 71–88.
[41] Plesa, T., 2017. Stochastic Approximation of High-
molecular by Bi-molecular Reactions. In preparation.
[42] Klonowski, W., 1983. Simplifying principles for chemical
and enzyme reaction kinetics. Biophysical Chemistry,
18(3): 73–87.
Supplementary Information (SI) Text
The Deterministic Dynamics of Network
ˆ
R1 ∪R2
1 in
the Limit µ →0
Let us analyse system (4) in the asymptotic limit µ →0. It
follows from the Tikhonov theorem [42] that the ODE for
y, given by second equation in (4), reduces to the algebraic
equation y = (c−x)−1 as µ →0. Substituting the algebraic
equation into (4) results in
dx
dt = k1 −k2x,
x(0) = x0, as µ →0.
(SI1)
Initial value problems (2) and (SI1) have the same form, and
let us denote their solutions by ˆx(t; ˆx0) and x(t; x0), respec-
tively. Then, choosing c ≥maxt≥0 ˆx(t; ˆx0) < ∞, and x0 = ˆx0,
ensures that concentration of auxiliary species ¯s is nonnega-
tive, ¯x(t) = c−x(t) ≥0, and that the solutions of (2) and (4)
are asymptotically equivalent in the limit µ →0.


## Page 9


Noise Control for DNA Computing — 9/13
The Stochastic Dynamics of Network ˆ
R1 ∪R2
1 ∪R3
1,1
in the Limit µ →0
The chemical master equation (CME) [27] induced by network
ˆ
R1 ∪R2
1 ∪R3
1,1 is given by
∂
∂t p(x,y,t) =

L 1 + 1
µ L 2
1 +K1,1L 3
1,1

p(x,y,t),
(SI2)
where x(t),y(t) ∈N0 are copy-numbers of species s,I1 from
(3), respectively, with
L 1 = k1(E−1
x
−1)((C −x)y)+k2(E+1
x
−1)x,
L 2
1 = (E−1
y
−1)+(C −x)(E+1
y
−1)y,
L 3
1,1 = (E−1
x
+E+1
x
−2)β1,1(x),
(SI3)
and K1,1,β1,1(x) given in (8). Operators L 1,L 2
1 ,L 3
1,1 are
induced by subnetworks ˆ
R1,R2
1,R3
1,1, respectively.
Let us analyse system (SI2) in the limit µ →0, and con-
sider the following power-series expansion:
p(x,y,t) = p0(x,y,t)+ µ p1(x,y,t)+...
+ µipi(x,y,t)+...,
(SI4)
with i ≥2. Substituting (SI4) into (SI2), and equating terms
of equal powers in µ, the following system of equations is
obtained:
O
 1
µ

: −L 2
1 p0(x,y,t) = 0,
O(1) : −L 2
1 p1(x,y,t) = (L 1 +K1,1L 3
1,1
−∂
∂t )p0(x,y,t).
(SI5)
Order 1/µ equation. A suitable form of the zero-order ap-
proximation of the PMF follows from the Bayes theorem:
p0(x,y,t) = p0(y|x)p0(x,t), where p0(y|x) is the stationary
PMF of y conditional on x, while p0(x,t) is the marginal PMF
of x. Substituting p0(x,y,t) = p0(y|x)p0(x,t) into the ﬁrst
equation in (SI5), with t,x ﬁxed, leads to −L 2
1 p0(y|x) = 0. It
follows that p0(y|x) is a Poisson distribution with parameter
(C −x)−1, so that the zero-order PMF is given by
p0(x,y,t) =
 1
y!

1
(C −x)
y
exp

−
1
(C −x)

p0(x,t).
(SI6)
Order 1 equation. Substituting (SI6) into the second
equation in (SI5), summing over all the possible states y ∈
N0, using (SI3), and equalities ∑y yp0(y|x) = (C −x)−1 and
∑y p0(y|x) = 1, one obtains the effective CME, given by
∂
∂t p0(x,t) =
 L +K1,1L 3
1,1

p0(x,t),
(SI7)
where L is the forward operator corresponding to network
(1), and has the following form
L = k1(E−1
x
−1)+k2(E+1
x
−1)x.
(SI8)
Limit K1,1 →0
Setting the left-hand side (LHS) to zero, and taking K1,1 = 0
in (SI7), and assuming C is ﬁxed to a sufﬁciently large value,
it follows that the stationary PMF is a Poisson distribution
with parameter k1/k2 [27]:
p0(x) =
(
1
x!

k1
k2
x
exp

−k1
k2

,
if x ∈[0,C],
0,
otherwise.
(SI9)
Limit K1,1 →∞
Let us substitute the power-series expansion
p0(x) = f0(x)+
1
K1,1
f1(x)+...
+
 1
K1,1
i
fi(x)+...,
(SI10)
with i ≥2, into (SI7) with the LHS set to zero, and consider
the limit K1,1 →∞. Then, equating terms of equal powers in
1/K1,1, one obtains:
O (1) : −L 3 f0(x) = 0,
O
 1
K1,1

: −L 3
1,1 f1(x) = L f0(x).
(SI11)
Order 1 equation. The solution to the ﬁrst equation in (SI11)
is given by
f0(x) =





1−a
C,
if x = 0,
a
C,
if x = C,
0,
otherwise,
(SI12)
where a ∈R≥is an arbitrary constant.
Order 1/K1,1 equation. Multiplying the second equation
in (SI11) by x, and summing over x ∈N0, with the conven-
tion that f0(x) = 0 and β1,1(x) = 0 for x /∈[0,C], one obtains
the solvability condition 0 = ∑∞
x=0 xL f0(x), which implies
a = k1/k2. Substituting a into (SI12) leads to the zero-order
approximation of the stationary PMF:
f0(x) =





1−1
C
k1
k2 ,
if x = 0,
1
C
k1
k2 ,
if x = C,
0,
otherwise.
(SI13)
Zero-Drift Networks R3
n,¯n
The propensity function of reactions underlying R3
n,¯n(s, ¯s),
n, ¯n ∈N0, and (n+ ¯n) ≤C, is given by Kn,¯nβn,¯n : [0,C] →R≥,
with
Kn,¯n = Mn,¯nkn,¯n,
(SI14)
and
βn,¯n(x) = (Mn,¯n)−1
n−1
∏
i=0
(x−i)
¯n−1
∏
i=0
((C −i)−x), (SI15)


## Page 10


Noise Control for DNA Computing — 10/13
where the scaling factor Mn,¯n is introduced to approximately
normalize βn,¯n(x), and is given by
Mn,¯n =
n−1
∏
i=0

n
n+ ¯nC −i
 ¯n−1
∏
l=0

¯n
n+ ¯nC −i

.
(SI16)
Here, we take the convention ∏N
i=0 f(i) = 1 if N < 0, where
f(i) is an arbitrary function of i. Function βn,¯n(x) is nonzero
on the interval [n,C −¯n], with the single maximum approxi-
mately at Cn/(n+ ¯n).
Interior zero-drift networks. Zero-drift network R3
n,¯n(s, ¯s),
with n, ¯n ̸= 0, satisﬁes (19), and the propensity function of its
reactions, which is proportional to (SI15), is nonzero only in
the interior of the state-space. Since the propensity function of
R3
n,¯n(s, ¯s), with n, ¯n ̸= 0, attains its maximum in the interior of
the domain, we call the network an interior zero-drift network.
Boundary zero-drift networks. Network R3
0,¯n(s, ¯s), satisfy-
ing (20), is a zero-drift network in the limit µ0,¯n →0. Further-
more, in the same limit, the ﬁrst two reactions from (20) have
the same propensity function, which is proportional to (SI15)
with n = 0, and which is nonzero at the left boundary point,
x = 0. Similarly, network R3
n,0 = R3
0,n(¯s,s; ¯B,kn,0,µn,0) is a
zero-drift network as µn,0 →0, and its ﬁrst two reactions have
the same propensity function, which is nonzero at the right
boundary point, x = C. Since networks with n = 0 (respec-
tively, ¯n = 0) generate propensity functions with the maximum
values at the left (respectively, right) boundary point, we call
such networks left (respectively, right) boundary zero-drift
networks.
Basis zero-drift networks. Stoichiometric coefﬁcients n, ¯n
control the support of the intrinsic noise, which network R3
n,¯n
introduces into the stochastic dynamics, via the control of
support of the compact function (SI15). The larger the sum
(n+ ¯n) is, with (n+ ¯n) ≤C, the smaller the support of (SI15),
and, hence, one obtains a more precise noise-control. In the
special case when n+ ¯n = C, the propensity function (SI15)
is nonzero only at a single point in the state-space, x = n.
We call networks R3
n,¯n(s, ¯s), with n+ ¯n = C, basis zero-drift
networks, and the corresponding propensity functions basis
propensity functions. Any nonnegative function, deﬁned on a
bounded discrete domain, may be represented by a suitable
linear combination of the basis propensity functions.
The Deterministic Model for Network ˜
R
The deterministic model of network (11) is given by
dx1
dt = k1 +k2x1 +k3x2
1 −k4x1x2 −k5x2
1x2 +k6x1x2
2,
dx2
dt = k7 −k8x2 +k9x1x2 +k10x2
2 −k11x3
2,
(SI17)
where x1 = x1(t),x2 = x2(t) are the concentrations of species
s1,s2, respectively, at time t.
Applying Algorithm 1 on Network ˜
R
Network ˜
R1(s1,s2, ¯s2)∪R2
1(¯s2)∪(R3
0,C2−10(s2, ¯s2)∪R3
30,0(s2, ¯s2))
is given by
˜
R1(s1,s2, ¯s2) :
∅
k1
−→s1,
s1
k2
−→2s1,
2s1
k3
−→3s1,
s1 +s2
k4
−→s2,
2s1 +s2
k5
−→s1 +s2,
s1 +2s2
k6
−→2s1 +2s2,
¯s2 +I1
2
k7
−→s2 +I1
2,
s2
k8
−→¯s2,
s1 +s2 + ¯s2 +I1
2
k9
−→s1 +2s2 +I1
2,
2s2 + ¯s2 +I1
2
k10
−−→3s2 +I1
2,
3s2
k11
−−→2s2 + ¯s2,
R2
1(¯s2) :
∅
1/µ
−−→I1
2,
¯s2 +I1
2
1/µ
−−→¯s2,
R3
0,C2−10(s2, ¯s2) :
(C2 −10)¯s2
k2
0,C2−10
−−−−→s2 +(C2 −11)¯s2,
C2s2 +B2
k2
0,C2−10
−−−−→(C2 −1)s2 + ¯s2 +B2,
(C2 −10)¯s2
1/µ0,C2−10
−−−−−−→(C2 −10)¯s2 +B2,
C2s2 +B2
1/µ0,C2−10
−−−−−−→C2s2,
R3
30,0(s2, ¯s2) :
30s2
k2
30,0
−−→29s2 + ¯s2,
C2 ¯s2 + ¯B2
k2
30,0
−−→s2 +(C2 −1)¯s2 + ¯B2,
30s2
1/µ30,0
−−−−→30s2 + ¯B2,
C2 ¯s2 + ¯B2
1/µ30,0
−−−−→C2 ¯s2.
(SI18)


## Page 11


Noise Control for DNA Computing — 11/13
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Copy−number x
β1,1(x)
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Copy−number x
β5,10(x)
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Copy−number x
β(x)
(a)
(d)
(g)
0
5
10
15
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Copy−number x
Stationary PMF p(x)
 
 
K1,1 = 0
K1,1 = 5
K1,1 = 105
0
5
10
15
0
0.05
0.1
0.15
0.2
0.25
Copy−number x
Stationary PMF p(x)
 
 
K5,10 = 0
K5,10 = 5
K5,10 = 105
0
5
10
15
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
0.45
0.5
Copy−number x
Stationary PMF p(x)
 
 
K = 0
K = 5
K = 105
(b)
(e)
(h)
0
10
20
30
40
50
60
70
80
90
100
0
5
10
15
20
Time t
Copy−number X(t)
 
 
Stochastic
Deterministic
0
10
20
30
40
50
60
70
80
90
100
0
5
10
15
Time t
Copy−number X(t)
 
 
Stochastic
Deterministic
0
10
20
30
40
50
60
70
80
90
100
0
5
10
15
Time t
Copy−number X(t)
 
 
Stochastic
Deterministic
(c)
(f)
(i)
Figure 1. Panels (a), (d) and (g) display propensity functions β1,1(x), β5,10(x) and β(x) ≡β0,15(x)+β2,9(x)+β8,5(x)
+β12,0(x), respectively. Panels (b), (e) and (h) display the stationary PMF of networks ˆ
R1 ∪R2
1 ∪R3
1,1, ˆ
R1 ∪R2
1 ∪R2
5,10 and
ˆ
R1 ∪R2
1 ∪(R3
0,15 ∪R3
2,9 ∪R3
8,5 ∪R3
12,0), respectively, where ˆ
R1 ∪R2
1 is given by (3), while the rest of the (zero-drift)
networks are as given in second step of Algorithm 1. In (h), K ≡K0,15 = K2,9 = K8,5 = K12,0. Panels (c), (f), and (i) display
in blue the sample paths, corresponding to the PMFs shown as the blue histograms in (b), (e) and (h), respectively, and were
obtained by applying the Gillespie algorithm on the underlying networks. Also shown in red are the deterministic trajectories,
obtained by numerically solving the corresponding deterministic models. The dimensionless parameters are ﬁxed to: k1 = 2.5,
k2 = 0.5, µ = 10−3, C = 15, and the state-space for species I1 is bounded in (b), (e) and (h) by 50. In (b) and (e), the
two-species stationary chemical master equation (CME) was numerically solved, while in (h) the boundary zero-drift networks
are taken in the asymptotic limits µ0,15,µ12,0 →0. The blue and red trajectories from panel (i) were generated with
(µ0,15)−1M0,15 = (µ12,0)−1M12,0 = 107. The trajectories from (c), (f) and (i) were all initiated at the deterministic
equilibrium, X(0) = 5.


## Page 12


Noise Control for DNA Computing — 12/13
(a)
(d)
(g)
0
50
100
150
200
250
300
0
0.002
0.004
0.006
0.008
0.01
0.012
0.014
Copy−number x1
Stationary PMF p(x1)
0
50
100
150
200
250
300
0
0.002
0.004
0.006
0.008
0.01
0.012
Copy−number x1
Stationary PMF p(x1)
0
50
100
150
200
250
300
0
0.005
0.01
0.015
0.02
0.025
0.03
Copy−number x1
Stationary PMF p(x1)
(b)
(e)
(h)
0
10
20
30
40
50
60
70
80
90
100
0
50
100
150
200
250
300
Time t
Copy−number X1(t)
 
 
Stochastic
Deterministic
0
10
20
30
40
50
60
70
80
90
100
0
50
100
150
200
250
300
Time t
Copy−number X1(t)
 
 
Stochastic
Deterministic
0
10
20
30
40
50
60
70
80
90
100
0
50
100
150
200
250
300
Time t
Copy−number X1(t)
 
 
Stochastic
Deterministic
(c)
(f)
(i)
Figure 2. Panel (a) displays the joint stationary PMF of network (11), while (d) and (g) display the stationary PMFs of
network (SI18) from SI Text for (K0,C2−10,K30,0) = (1018,2×108) and (K0,C2−10,K30,0) = (1018,1018), respectively, with the
rest of the parameters being the same. Panels (b), (e) and (h) display the x1-marginal PMFs corresponding to (a), (b) and (c),
respectively. Panels (c), (f) and (i) display in blue the sample paths, corresponding to the PMFs shown in (b), (e) and (h),
respectively, and were obtained by applying the Gillespie algorithm on the underlying networks. Also shown in red are two
deterministic trajectories, one initiated near the equilibrium point, while the other near the limit cycle, obtained by numerically
solving equation (SI17) from SI Text. The dimensionless parameters are ﬁxed to: k1 = 4, k2 = 1.408, k3 = 0.0518, k4 = 0.164,
k5 = 3.1×10−3, k6 = 4.8×10−3, k7 = 4, k8 = 8, k9 = 0.16, k10 = 0.104, k11 = 2.1×10−3. In (a)–(b), (d)–(e) and (g)–(h),
the stationary chemical master equation (CME) is numerically solved, with the state-space is truncated to
(x1,x2) ∈[0,C1]×[0,C2], where C1 = 300, C2 = 180, and µ,µ0,C2−10,µ30,0 →0. The blue sample paths from panels (f) and
(i) were generated with (µ−1,(µ0,C2−10)−1M0,C2−10,(µ30,0)−1M30,0) = (103,1020,2×1010) and
(µ−1,(µ0,C2−10)−1M0,C2−10,(µ30,0)−1M30,0) = (103,1020,1020), respectively. The blue trajectories from (c), (f) and (i) were
all initiated near the deterministic limit cycle.


## Page 13


Noise Control for DNA Computing — 13/13
Input: Let the input reaction network be given by
ˆ
R(s1,...,sN) :
N
∑
i=1
ci jsi
k j
−→
N
∑
i=1
c′
i jsi, j ∈{1,...,M},
(16)
where s1,...,sN, are the species, kj the reaction rate coefﬁcients, and cij,c′
ij the stoichiometric coefﬁcients.
(1) Step: Reaction network ˆ
R, given by (16), is mapped to a pairwise conservative network ˆ
R1 given by
ˆ
R1(s1,...,sN, ¯s1,..., ¯sN) :
N
∑
i=1

ci jsi +(∆xij ¯si +I
∆xij
i
)×1N(∆xij)
 kj
−→
N
∑
i=1

c′
i jsi −(∆xi j ¯si)×1N(−∆xi j)+I
∆xij
i
×1N(∆xij)

, j ∈{1,...,M}.
(17)
Here, ¯si,I
∆xij
i
are additional species, ∆xi j = (c′
ij −cij), and 1N(·) is the indicator function of the natural numbers.
(2) Step: For each species I
∆xij
i
, a drift-corrector network is constructed, R2
∆xij(¯si) = R2
∆xij(¯si; I
∆xij
i
,µ), given by
R2
∆xij(¯si) :
∅
1/µ
−−→I
∆xij
i
,
∆xi j ¯si +I
∆xij
i
1/µ
−−→∆xi j ¯si.
(18)
where 0 ≤µ ≪1.
(3) Step: For each species ¯si, a union of zero-drift networks may be constructed. Let n, ¯n ∈N0, and (n+ ¯n) ≤Ci. Network
R3
n,¯n(si, ¯si) = R3
n,¯n(si, ¯si; ki
n,¯n), with n, ¯n ̸= 0, is given by
R3
n,¯n(si, ¯si) : nsi + ¯n¯si
ki
n,¯n
−−→(n+1)si +(¯n−1)¯si,
nsi + ¯n¯si
ki
n,¯n
−−→(n−1)si +(¯n+1)¯si.
(19)
Network R3
0,¯n(si, ¯si) = R3
0,¯n(si, ¯si; Bi,ki
0,¯n,µ0,¯n), with ¯n ̸= 0, is given by
R3
0,¯n(si, ¯si) : ¯n¯si
ki
0,¯n
−−→si +(¯n−1)¯si,
Cisi +Bi
ki
0,¯n
−−→(Ci −1)si + ¯si +Bi,
¯n¯si
1/µ0,¯n
−−−→¯n¯si +Bi,
Cisi +Bi
1/µ0,¯n
−−−→Cisi,
(20)
where 0 ≤µ0,¯n ≪1, and Bi is an additional species. Network R3
n,0 = R3
0,n(¯si,si; ¯Bi,ki
n,0,µn,0).
Output: An output reaction network R is given by
R = ˆ
R1 ∪R2 ∪R3,
(21)
where R2 = ∪i ∪∆xij R2
∆xij(¯si), and R3 = ∪i ∪(n,¯n) R3
n,¯n(si, ¯si).
Algorithm 1. The noise-control algorithm.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
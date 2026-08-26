---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1205.1767v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1205.1767v1_The_main_transition_in_the_Pink_membrane_model__finite-size_scaling_and_the_infl

> Source: 1205.1767v1_The_main_transition_in_the_Pink_membrane_model__finite-size_scaling_and_the_infl.pdf

> Pages: 9

---


## Page 1


arXiv:1205.1767v1  [cond-mat.soft]  8 May 2012
The main transition in the Pink membrane model: ﬁnite-size scaling and
the inﬂuence of surface roughness
Sina Sadeghi and R. L. C. Vink
Institute of Theoretical Physics, Georg-August-Universit¨at G¨ottingen,
Friedrich-Hund-Platz 1, D-37077 G¨ottingen, Germany
We consider the main transition in single-component membranes using computer simulations of
the Pink model [D. Pink et al., Biochemistry 19, 349 (1980)].
We ﬁrst show that the accepted
parameters of the Pink model yield a main transition temperature that is systematically below
experimental values. This resolves an issue that was ﬁrst pointed out by Corvera and co-workers
[Phys. Rev. E 47, 696 (1993)]. In order to yield the correct transition temperature, the strength
of the van der Waals coupling in the Pink model must be increased; by using ﬁnite-size scaling, a
set of optimal values is proposed. We also provide ﬁnite-size scaling evidence that the Pink model
belongs to the universality class of the two-dimensional Ising model. This ﬁnding holds irrespective
of the number of conformational states. Finally, we address the main transition in the presence
of quenched disorder, which may arise in situations where the membrane is deposited on a rough
support. In this case, we observe a stable multi-domain structure of gel and ﬂuid domains, and the
absence of a sharp transition in the thermodynamic limit.
PACS numbers: 87.16.D-, 87.14.Cc, 64.70.-p, 82.20.Wt
I.
INTRODUCTION
Lipid membrane bilayers are abundant in nature and
to understand their properties is of paramount impor-
tance [1–3]. One aspect that has received much attention
are collective phenomena (phase transitions) taking place
in these systems. Among the diﬀerent phase transitions
that can occur [4–7], the main phase transition is pre-
sumably the most important and well studied one [8, 9].
This transition, typically driven by the temperature T ,
is between a “gel” and a “ﬂuid” phase. At low T , the bi-
layer is in the gel phase (characterized by nematic chain
order of the lipid tails), while at high T the bilayer as-
sumes the ﬂuid phase (characterized by the absence of
nematic chain order).
Computer simulations have become a well established
tool to model the main transition. The challenge in sim-
ulations is to strike a balance between the level of detail
to include, and the time and length scale one wishes to
address [10]. Since collective phenomena involve many
molecules and entail large length scales it is clear that,
in order to describe the main transition, a signiﬁcantly
coarse-grained particle model is crucial. Strictly speak-
ing, one needs to address the thermodynamic limit (in-
ﬁnite particle number) since only there phase transition
properties become properly deﬁned. Indeed, the need for
coarse grained modeling of lipid bilayers is well recog-
nized [11–13].
An early and highly successful coarse grained approach
to study the main transition has been the particle model
introduced by David Pink and co-workers [14–16]. In this
model, the so-called Pink model, only the orientational
degrees of freedom of the hydrophobic lipid tails are in-
cluded, while the positional degrees of freedom of the hy-
drophilic heads are disregarded. This model, due to its
simplicity, allows for the investigation of very large sys-
tems, and the nature of the main transition can be probed
in great detail. Indeed, key features of the main transi-
tion in the Pink model compare well to experiments [17].
However, despite the great success the Pink model has
enjoyed, there remain some open questions. In Ref. 18,
it was noted that the Pink model at the experimentally
determined transition temperature does not undergo any
transition. While in systems of ﬁnite size there were indi-
cations of a transition, these vanished in larger systems.
This raises the question as to why no transition could
be detected. The aim of this paper is to resolve this is-
sue. As it turns out, to properly model the main transi-
tion, a ﬁnite-size scaling study is essential.
Computer
simulations inevitably deal with only a ﬁnite number
of particles, and their output will depend on the num-
ber of particles used, especially near phase transitions.
Finite-size scaling provides the framework to systemati-
cally extrapolate simulation data to the thermodynamic
limit.
To date, ﬁnite-size scaling studies of the Pink
model are scarce, with Ref. 18 being a notable excep-
tion. The present paper aims to ﬁll this gap. Our main
ﬁnding is that, in order to observe the main transition
in the Pink model at experimentally relevant tempera-
tures, one of the model parameters needs to be adjusted.
This follows quite naturally when one realizes that the
universality class of the Pink model is just the one of
the two-dimensional (2D) Ising model [15]. As we will
show for three lipid species, the “standard” Pink model
parameters yield a critical temperature distinctly below
the experimental main transition temperature. Conse-
quently, a “re-tuning” of the standard Pink parameters
is urgently needed.
As an application, we also address the fate of the main
transition in the presence of quenched (immobilized) im-
purities using the Pink model. The experimental motiva-
tion to do so is that this situation may resemble that of
a membrane supported on a rough substrate. In binary
lipid mixtures, the eﬀect of such impurities on lateral


## Page 2


2
phase separation has recently attracted much attention
[19–24]. In this paper, we present simulation results for
the corresponding scenario in a single component bilayer
undergoing the main transition. Within the framework
of the Pink model, we ﬁnd that quenched impurities pre-
vent the main transition from taking place, already at
low impurity concentrations. Instead of the formation of
macroscopic gel and ﬂuid domains, we now obtain a sta-
ble multi-domain structure, which strikingly resembles
experimental results. The theoretical justiﬁcation is that
the impurities induce a change in universality toward the
2D random-ﬁeld Ising class. As is well known, the latter
does not support an order-disorder phase transition in
the thermodynamic limit [25–28].
II.
THE PINK MODEL
In the Pink model, the lipid bilayer is assumed to con-
sist of two independent monolayers. Each monolayer is
represented by a triangular 2D lattice consisting of N
sites, and each lattice site contains a single lipid chain.
Each lipid molecule is comprised of two independent hy-
drophobic acyl chains and a hydrophilic polar head. The
polar heads are translationally frozen to the lattice, and
no particular structure for the polar head groups is as-
sumed. The only degrees of freedom included in the Pink
model are the acyl chain conformations. These are not
simulated directly (i.e. one does not explicitly model the
carbon atoms) but are captured in a coarse-grained fash-
ion whereby the chain conformations are grouped into
α = 1, . . . , q discrete states.
The original Pink model
uses q = 10, but we will consider diﬀerent values also.
These states include the ground state (α = 1), eight low-
energy excitations (α = 2, . . . , q −1), while all remaining
conformations are grouped into a single disordered state
(α = q). Each state α is characterized by three coarse-
graining parameters, namely an internal energy Eα, a
cross-sectional area Aα, and a degeneracy Dα counting
the number of chain conformations with energy Eα and
area Aα.
A.
coarse graining parameters
To determine the coarse graining parameters, we as-
sume that a single acyl chain consists of i = 1, . . . , M
carbon atoms, thereby containing M −1 carbon-carbon
bonds, and that bonds are either in a trans or gauche
conﬁguration.
The trans conﬁguration yields the low-
est energy, while the gauche conﬁguration has a slightly
higher energy. The energy diﬀerence between the trans
and gauche conﬁguration is denoted Γ (Table I). To un-
derstand the diﬀerence in geometry between trans and
gauche bonds consider a chain segment of four consecu-
tive carbon atoms. The positions of the ﬁrst three atoms
deﬁne a two-dimensional plane. In the trans conﬁgura-
tion, the fourth atom remains in the plane, while in the
FIG. 1. Typical chain conformations of the Pink model with
M = 7, showing (numbered) carbon atoms placed on the
nodes of a hexagonal lattice.
The atom connected to the
head group is labeled i = 1 but for clarity the head group is
only drawn for the ground state. The z-direction indicates
the bilayer normal, while the vertical double-arrows indicate
the projected length. (a) The ground state α = 1, consisting
of only trans bonds. (b) The two conformations that consti-
tute the ﬁrst excited state α = 2 containing one gauche bond
(marked with a cross).
(c) Conformation belonging to the
second excited state α = 3. The internal energy is the same
as in (b) but the projected length is shorter (the other α = 3
conformation has the gauche bond between atoms 3 −4).
gauche conﬁguration, it leaves the plane, and it can do so
inward or outward. Thus, each gauche bond is two-fold
degenerate. In the Pink model, it is assumed that each
2n-th gauche bond takes the chain back to the original
plane, and so the gauche degeneracy is given by
G = 2ceil(n/2)
,
(1)
where n denotes the total number of gauche bonds in the
chain, and where the function ceil means “rounding-up”
to the nearest integer.
It is convenient to mathematically represent the chain
conformations on a hexagonal lattice with next-nearest
neighbor distance 2a.
We emphasize that this lattice
is merely an aid to identify the low energy chain con-
formations which are needed to set the coarse-graining
parameters: it should not be confused with the trian-
gular simulation lattice on which the Pink Hamiltonian
will eventually be deﬁned. The carbon atoms are placed
on the nodes of the hexagonal lattice following certain
rules, and nearest-neighbor connections between atoms
represent carbon-carbon bonds. The ground state α = 1
corresponds to the chain conformation that is maximally
stretched [Fig. 1(a)]. Note that, in the ground state, the
atoms are alternatingly placed on the left and right lattice
node, yielding a characteristic “zig-zag” pattern.
The
ground state by deﬁnition contains only trans bonds, its
internal energy is set to zero as a reference E1 = 0, and it
is obviously non-degenerate D1 = 1. The cross-sectional
area of the ground state has experimentally been deter-
mined as A1 = 20.4 ˚A2 [14]. We also introduce the pro-
jected length l of the conformation, deﬁned as the dif-
ference in z-coordinate between the carbon atom closest


## Page 3


3
to the head group (i = 1) and the one furthest away
(i = M), with the z-direction as indicated in the ﬁgure.
For the ground state, it follows that l1 = (M −1)a.
The eight low-energy excitations (α = 2, . . . , 9) are
obtained by systematically incorporating gauche bonds.
The eﬀect of such a bond is to disrupt the “zig-zag” pat-
tern of the ground state. That is, one no longer places the
atoms alternatingly on left and right nodes, but also al-
lows for “excursions” whereby for two consecutive atoms
the same direction is chosen. Each such excursion cor-
responds to a gauche bond, and has energy cost Γ. The
gauche bonds are introduced according to the following
rules:
(1) The two bonds in the chain closest to the
head group must always be in the trans conﬁguration.
In Fig. 1, these correspond to the bonds between atoms
1 −2 and 2 −3. (2) At most three gauche bonds are
allowed, and each time such a bond is included there is
an energy cost Γ. (3) The projected chain length l must
obey l1 −l ≤3a. (4) The acyl chain cannot fold back
onto itself. In the coordinate system of Fig. 1, this means
that the z-coordinates of the atoms must obey zi+1 ≥zi.
Following these rules, we show in Fig. 1(b) the chain
conformations (i) and (ii) that form the ﬁrst excited state
α = 2.
In (i), a single gauche bond is placed at the
very chain end, while in (ii) it is placed at the second-
last position.
One immediately sees that both confor-
mations have the same energy E2 = Γ, and the same
projected length l2 = (M −2)a. To compute the cross-
sectional area, one assumes volume conservation for the
lipid chains: Aαlα = A1l1.
Hence, from the (known)
ground state values, the cross-sectional area of the ex-
cited state follows.
Note that, by placing the gauche
bond at the third-last position [Fig. 1(c)], a shorter
projected length is obtained, and so conformation (c)
does not belong to the ﬁrst excited state (even though
it has the same energy).
The total degeneracy of the
ﬁrst exited state D2 = 4, which is the total number
of conformations, multiplied by the gauche degeneracy
of Eq. (1).
The coarse-graining parameters of the re-
maining excited states can be found analogously, and
are listed for completeness in Table I. Finally, for the
completely disordered state α = q = 10, one assumes
E10 = (0.42M −3.94) × 10−13 erg, A10 = 34 ˚A2, and
degeneracy D10 = 6 × 3M−6, which have their origins in
experimental considerations [16].
B.
Pink model Hamiltonian
Having speciﬁed the coarse-graining parameters, the
Hamiltonian of the Pink model can be written as [30]
HPink = H0 + HVDW + HP
.
(2)
The ﬁrst term is the total internal energy of the acyl
chains H0 = PN
i=1 Es(i), with the sum over all N sites
of the triangular lattice, and s(i) ∈{1, . . ., q} the confor-
mational state at the i-th lattice site. The second term
state (α)
Eα
lα
Dα
ground state
1
0
M −1
1
kink





























2
Γ
M −2
4
3
Γ
M −3
4
4
Γ
M −4
4
5
2Γ
M −2
2(M −6)
6
2Γ
M −3
2(M −8)
7
2Γ
M −4
2(M −10)
8
3Γ
M −3
8(M −8)
9
3Γ
M −4
16(M −10)
disordered
10
E10
l1A1/A10
6 × 3M−6
TABLE I. The coarse graining parameters used to describe
the acyl chain conformations in the q = 10 Pink model [14–16,
29]. For each state conformation α, we list the internal energy
Eα, the projected length lα, and the degeneracy Dα.
The
energy of a single gauche bond equals Γ = 0.45 × 10−13 erg,
while M denotes the number of carbon atoms in the chain.
represents the anisotropic van der Waals interaction be-
tween adjacent acyl chains HVDW = −J0
P
⟨i,j⟩Is(i) Is(j),
with J0 the van der Waals coupling constant, and ⟨i, j⟩
a sum over all 3N nearest-neighboring sites on the tri-
angular lattice. The precise value of J0 depends on the
chain length, and explicit expressions are provided else-
where [14, 15, 31]. However, it has been noted that these
parameters do not always yield a main transition at the
expected temperature [18], and so we will also propose
our own values later on. The (dimensionless) variables
Iα measure nematic chain order, and can be expressed in
terms of the cross-sectional areas [16, 18]
Iα = ωα
9
5
A1
Aα
−4
5
  A1
Aα
5/4
,
(3)
where ω10 = 0.4 for the disordered state α = 10, and
ωα = 1 otherwise.
The last term in the Hamiltonian accounts for the in-
teraction between the hydrophilic polar head groups and
between them and water and also steric interactions from
both head groups and the lipid chains. Although it is
possible to consider a more realistic pairwise interaction
between the headgroups [30], this interaction can be ap-
proximated with a simple pressure term HP = ΠA, where
Π is an eﬀective lateral pressure acting on the lipid chains
in the bilayer membrane, and A the total cross-sectional
area occupied by the lipids chains
A =
N
X
i=1
As(i)
.
(4)
III.
MONTE CARLO METHODS
To study the phase behavior of the Pink model, we use
the Monte Carlo (MC) simulation method. We mostly


## Page 4


4
use triangular lattices of size N = L × L with periodic
boundary conditions. The principal MC move consists
of randomly picking one of the lattice sites, read-out the
conformational state α of that site, and propose a new
state β drawn randomly from the set of q possible states.
The new conﬁguration is accepted with the Metropolis
criterion
Pacc(α →β) = min

1, Dβ
Dα
exp

−∆H
kBT

,
(5)
where D denotes the state degeneracy, ∆H the energy
diﬀerence between initial and ﬁnal conﬁguration as given
by Eq. (2), kB the Boltzmann constant, and T the tem-
perature. The degeneracy compensates for the fact that
some of the states have a much larger entropy, and should
therefore appear more often in the ensemble average.
By virtue of the MC move, the total projected area
A given by Eq. (4) ﬂuctuates during the course of the
simulation. In fact, A plays the role of order parame-
ter since it changes abruptly at the main phase transi-
tion. Hence, it is instructive to measure the distribution
P(A|T, Π), deﬁned as the probability to observe a con-
ﬁguration with projected area A. The distribution de-
pends on the imposed temperature and pressure, as well
as on the linear extension L of the triangular simula-
tion lattice. At the main transition, P(A|T, Π) assumes
a characteristic bimodal shape, from which a number of
important phase properties are obtained (explicit exam-
ples are provided in the next section). We note that even
with very long simulation runs, distributions P(A|T, Π)
of high statistical quality are diﬃcult to obtain, espe-
cially in the vicinity of the main transition. The reason
is related to free energy barriers that arise from the for-
mation of interfaces [32–34]. To overcome this problem,
we combine our MC simulations with a biased sampling
scheme called successive umbrella sampling [35]; the lat-
ter ensures that P(A|T, Π) is sampled accurately over
the entire (speciﬁed) range in A of interest. A ﬁnal in-
gredient to economize simulation time is the use of his-
togram reweighting [36]. A single simulation run yields
P(A|T, Π) at a given temperature T and eﬀective pres-
sure Π; histogram reweighting enables us to extrapolate
the measured distribution to diﬀerent values T ′, Π′. For
example, extrapolations in the pressure are performed
using P(A|T, Π′) ∝P(A|T, Π) e−(Π′−Π)A/kBT . Extrapo-
lations in the temperature can be performed analogously,
but also require storage of the energy histograms; for im-
plementation details see Ref. 37.
IV.
RESULTS
A.
the “standard” Pink model revisited
We ﬁrst consider the main transition in a membrane
consisting of DPPC lipids to settle a controversy when
this system is being simulated using the Pink model. The
acyl chains in DPPC consist of M = 16 carbon atoms,
 40
 45
 50
 55
 60
 70
P(A−) (arb. units.)
A−(Å2)
T>Tc
T≈Tc
1.0
1.1
1.2
 288
 290
 292
 294
 296
T(K)
(a)
U1
(b)
L = 20
L = 30
L = 40
L = 50
FIG. 2. Simulation results for DPPC obtained using the Pink
model with “standard” parameters. (a) Probability distribu-
tion P( ¯A) of the cross-sectional area per molecule. Note that
we have adopted the convention to plot the average area per
lipid, ¯A = 2A/N, with A given by Eq. (4). At high temper-
ature, irrespective of the value of Π, P( ¯A) is single-peaked
corresponding to one phase (solid line). At low temperature,
P( ¯A) becomes double-peaked provided Π = ΠCOEX, indica-
tive of two-phase coexistence (dotted line).
(b) Finite-size
scaling analysis to locate the critical temperature Tc. Plotted
is the Binder cumulant U1 as a function of temperature T for
diﬀerent system sizes L. The intersection of the curves for
diﬀerent L yields Tc.
and the experimentally obtained main transition tem-
perature TDPPC = 314.0 K [31]. However, simulations
based on the Pink model could not detect a transition
at this temperature [18]. The latter simulations used the
“standard” Pink parameters as listed in Table I, van der
Waals coupling constant J0 = 0.710 × 10−13 erg, and
pressure Π = 30 dyn/cm.
Hence the question arises
as to why no transition could be detected. To answer
this question we perform additional DPPC simulations
using the Pink model, with the same parameters as in
Ref. 18, but over a wider range in temperature and pres-
sure. The picture that emerges is the following: At high
temperature the distribution P(A|T, Π) is always single-
peaked (corresponding to one phase) for all value of the
lateral pressure Π.
At low temperature, P(A|T, Π) is
doubled-peaked for a special value of the lateral pres-
sure, Π = ΠCOEX, corresponding to two-phase coexis-
tence [Fig. 2(a)].
Here, the left peak reﬂects the gel-
phase, the right peak the fluid-phase. The numerical
criterion to locate ΠCOEX is to vary Π until the ﬂuctua-
tion ⟨A2⟩−⟨A⟩2 reaches a maximum [38], with the ther-


## Page 5


5
M
J0
Tc
ΠCOEX
Tm
J∗
0
Π∗
COEX
DMPC
14
0.618
270.3
4.3
296.9
0.690
15.6
DPPC
16
0.710
291.7
4.6
314.0
0.772
18.1
DSPC
18
0.815
321.5
21.6
327.9
0.833
26.7
TABLE II. Critical point parameters for three lipid species,
with M the number of carbon atoms in a single chain. We list
the critical temperature Tc and coexisting pressure ΠCOEX
obtained in simulations of the Pink model using the “stan-
dard” value of the van der Waals coupling constant J0. The
resulting estimates of Tc are to be compared to the experi-
mental melting temperatures Tm: Tc clearly underestimates
Tm in all cases. Instead, by using the Pink model with the re-
tuned values J∗
0 proposed in this work, Tc coincides with Tm,
with corresponding critical pressure Π∗
COEX (coupling con-
stants in units of 10−13 erg, temperatures in K, and pressures
in dyn/cm).
mal averages computed as ⟨Am⟩=
R
Am P(A|T, Π) dA.
At the temperature T = Tc where the transition from a
single to doubled-peaked distribution occurs, the system
becomes critical.
To locate the critical temperature a
ﬁnite-size scaling analysis is performed, whereby we plot
the Binder cumulant U1 = ⟨∆2⟩/⟨|∆|⟩2, ∆≡A −⟨A⟩,
versus temperature T for diﬀerent system sizes L. In the
thermodynamic limit
lim
L→∞U1 =





1
T < Tc,
U ∗
1
T = Tc,
π/2
T > Tc,
(6)
while in systems of ﬁnite size, curves for diﬀerent L inter-
sect at T = Tc [39, 40]. In Fig. 2(b), we show the result
for DPPC obtained using the “standard” Pink model pa-
rameters: the data scale as expected, and from the in-
tersection the critical temperature Tc can be accurately
“read-oﬀ”.
The corresponding estimates of Tc as well as the coex-
istence pressures ΠCOEX for three lipid species are col-
lected in Table II. For all lipid species considered, the
computed critical temperature Tc is distinctly below the
experimental melting temperature Tm. In other words: if
one simulates the Pink model at the experimental melt-
ing temperature Tm, one is always inside the one-phase
region, where P(A|T, Π) is single-peaked! This, appar-
ently, is the reason why no phase transition could be
seen in previous studies [18]. One possibility to get the
proper value for the transition temperature, i.e. such that
Tc coincides with Tm, is to re-tune the value of J0. This
has been done for the three lipid species by systemati-
cally changing the coupling constant J0 using histogram
reweighting and ﬁnite-size scaling. Our proposed values
J∗
0 and corresponding pressures Π∗
COEX for the three lipid
species are summarized in Table II.
For completeness,
we still conﬁrm the universal-
ity class of the critical point,
which for the Pink
model is expected to be the one of the 2D Ising
 0
 10
 20
 30
 40
-2
-1
 0
 1
 2
 3
t L1/ν
χ L-γ/ν
χ L-γ/ν
χ L-γ/ν
L = 20
L = 30
L = 40
L = 50
FIG. 3. Susceptibility scaling function χ L−γ/ν versus t L1/ν
for DPPC obtained using the “standard” Pink model. The
data for diﬀerent system sizes strikingly collapse using 2D
Ising values for the critical exponents.
model [15].
To this end, we consider the susceptibil-
ity χ =
 ⟨∆2⟩−⟨|∆|⟩2
/(kBT L2) [41], which diverges
at the critical point χ ∝|t|−γ, t = T/Tc −1, with critical
exponent γ. In systems of ﬁnite size, the divergence is
rounded, but γ can still be obtained using the standard
ﬁnite-size scaling procedure of plotting χ L−γ/ν versus
t L1/ν [42], where ν is the correlation length critical ex-
ponent. Provided suitable values γ, ν, Tc are used, data
for diﬀerent L collapse. The result for DPPC is shown
in Fig. 3, where the “standard” parameters of the Pink
model were used.
Indeed, by using the 2D Ising val-
ues {γ = 7/4, ν = 1}, and Tc = 291.7 K of Table II,
an excellent data collapse is observed (similar good col-
lapses are obtained for DMPC and DSPC also). The or-
der parameter critical exponent has also been measured,
and the 2D Ising value β = 1/8 was conﬁrmed (scaling
plot not shown). Therefore, even though the Pink model
is a 10-state model, its critical behavior remains in the
universality class of the 2D Ising model.
This further
motivates the idea of reducing the q = 10 states in the
Pink model to an eﬀectively two-state description as is
frequently done [15, 17, 43–45].
B.
modiﬁed Pink model with fewer states
We now consider the eﬀect of lowering the number
of states in the Pink model. For this purpose, an ap-
propriate number of intermediate states was removed,
based on the maximum number of gauche bonds. In the
“standard” 10-state Pink model at most three gauche
bonds are allowed.
We now consider the case where
at most two gauche bonds are permitted, by removing
states α = 8, 9 from Table I, yielding an 8-state model
(to keep the total number of states constant the degen-
eracy of the removed states was added to the disordered
state, but we emphasize that this correction is small).
We apply our previous ﬁnite-size scaling analysis to the


## Page 6


6
resulting 8-state model for DPPC, using the “standard”
value J0 = 0.710 × 10−13 erg.
As expected, the crit-
ical point remains in the universality class of the 2D
Ising model, but it is “shifted” to Tc = 309.4 K and
ΠCOEX = 26.0 dyn/cm. Similarly, by allowing at most
one gauche bond, a 5-state model is obtained. In this
case, the DPPC critical point is located at Tc = 351.5 K
and ΠCOEX = 87.7 dyn/cm.
Therefore, lowering the number of states in the Pink
model while leaving the other parameters untouched, one
ﬁnds that both the critical temperature and pressure in-
crease.
This trend is consistent with the Pink model
simulations of Ref. 46 for DPPC performed at the exper-
imental melting temperature Tm but with a lower number
of states. In these simulations, hysteresis loops indicat-
ing a ﬁrst-order transition are clearly visible around Tm
for q < 6. Indeed, as our scaling analysis shows, by low-
ering the number of states q, Tc eventually exceeds Tm,
resulting in a genuine phase transition at Tm.
To conclude: lowering the number of states q does not
aﬀect the universality class of the Pink model, which re-
mains 2D Ising (provided q ≥2, of course). Hence, the
topology of the phase diagram remains the same, merely
the critical point gets shifted. Depending on the parame-
ters used, the main transition in the Pink model is either
ﬁrst-order (T < Tc), or it is 2D Ising critical (T = Tc).
We do not claim that the main transition as observed
in experiments necessarily conforms to this scenario (we
return to this point in Section V).
C.
Pink model with quenched disorder
As a ﬁnal illustration, we consider the main transition
in a solid-supported membrane, which has received con-
siderable attention in experiments [6, 47–51]. A striking
feature observed in one of these studies is the formation of
coexisting gel and ﬂuid domains that do not coalesce with
time, but instead form a multi-domain structure that is
stable over hours [50].
To understand the stability of
this structure is not trivial, due to the large amount of
line interface it contains. Here we attempt to reproduce
such a multi-domain structure within the framework of
the Pink model. Our hypothesis is that the solid sup-
port onto which the membrane is deposited has a certain
roughness. Since surface roughness is random and time
independent, it constitutes a form of quenched disorder.
We assume that this gives rises to regions on the sur-
face where certain lipid tail conformations are preferred
over others. We capture this eﬀect in the Pink model by
randomly labeling a fraction p of the lattice sites as “pin-
ning sites”. At the pinning sites, the corresponding lipid
chain is ﬁxed into the ground state conformation. This
extension is trivially incorporated into our MC simula-
tions: we simply do not apply the MC move to pinning
sites. We specialize to DSPC, using the “standard” Pink
parameters of Tables I and II.
In Fig. 4(a), we show ln P(A|T, Π) at T = 291 K and
 40
 45
 50
 55
 60
 70
−30
−20
−10
 0
ln P(A−)
A−(Å2)
(a)
∆F / kBT
(b)
"l_200x300.dat" matrix
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
FIG. 4. DSPC simulation results for T = 291 K in the absence
of quenched disorder. (a) The natural logarithm of P( ¯A) at
ΠCOEX and system size L = 50. The barrier ∆F is related to
the line tension via Eq. (7). (b) Typical snapshot of the bi-
layer with the lipids color-coded according to their conforma-
tional state for a 200×300 lattice. The snapshot was taken at
cross-sectional area ¯A = 54.4 ˚A2 chosen “between the peaks”
of P( ¯A). A pronounced coexistence between a single gel and
ﬂuid domain is observed.
ΠCOEX = −18.9 dyn/cm in the absence of quenched dis-
order (p = 0). At this temperature, which is well below
Tc, the main transition is strongly ﬁrst-order.
Conse-
quently, there is a signiﬁcant line tension σ between gel
and ﬂuid domains; the latter is related to the free energy
barrier [34, 52]
∆F ≡kBT ln (Pmax/Pmin) = 2σL
,
(7)
indicated by the vertical double-arrow in Fig. 4(a). Here,
Pmin is the value of P(A|T, Π) at the minimum “between
the peaks”, while Pmax denotes the average peak value.
The physical motivation for Eq. (7) is that, for cross-
sectional areas “between the peaks”, the bilayer reveals
a coexistence between two slab domains where the to-
tal interface length equals 2L [Fig. 4(b)].
For DSPC,
and assuming the lattice constant to be 1 nm, we ob-
tain σ ∼1.1 pN, which is compatible with experimental
values [53].
Next, we consider a DSPC bilayer with a fraction
p = 0.03 of the lattice sites marked as “pinning sites”. In
Fig. 5(a), we show distributions P(A|T, Π) for T = 291 K
obtained for 4 diﬀerent random positions (samples) of
pinning sites. Even though the temperature is the same
as in Fig. 4(a), a unique double-peaked distribution
can no longer be identiﬁed.
In contrast, P(A|T, Π) is
strongly sample dependent, and a multitude of rather
exotic shapes is revealed. This behavior is characteris-
tic of systems that belong to the universality class of the


## Page 7


7
 40
 45
 50
 55
 60
 70
P(A−) (arb. units.)
A−(Å2)
(a)
n = 1
n = 2
n = 3
n = 4
(b)
"lq3_200x300.dat" matrix
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
FIG. 5.
DSPC simulation results for T = 291 K in the
presence quenched disorder, with a fraction of pinning sites
p = 0.03. (a) Typical distributions P( ¯A) for 4 diﬀerent sam-
ples of pinning sites, and system size L = 50.
In contrast
to Fig. 4(a), a ﬁrst-order transition can no longer be identi-
ﬁed. (b) Typical bilayer snapshot obtained at ¯A = 54.4 ˚A2
for a 200 × 300 lattice. A stable structure of multi-domains is
observed.
1.0
1.1
1.2
1.3
1.5
1.6
 287
 289
 291
 293
 295
T(K)
U1
L = 20
L = 30
L = 40
L = 50
FIG. 6.
The (disorder-averaged) Binder cumulant U1 as a
function of temperature T for DSPC with a fraction p = 0.03
of pinning sites. In contrast to Fig. 2(b), an intersection of
the curves for diﬀerent L can no longer be identiﬁed. Instead,
as the system size L increases, U1 →π/2, indicative of the
one phase region. For each system size, the disorder average
comprised 200 samples of pinning sites.
2D random-ﬁeld Ising model (2D-RFIM) [21].
Hence,
by introducing the pinning sites, we have changed the
universality class of the Pink model from ordinary 2D
Ising toward 2D-RFIM (the pinning sites essentially cor-
respond to a ﬁeld of inﬁnite strength acting at random
locations).
There are two features of the 2D-RFIM universality
class that are remarkably consistent with experimental
results for the main transition in supported membranes.
First of all, 2D-RFIM universality implies the absence
of macroscopic coexistence between gel and ﬂuid do-
mains [25–28].
Indeed, inspection of simulation snap-
shots [Fig. 5(b)] reveals an equilibrium multi-domain
structure, that is highly anisotropic, strongly resembling
experimental AFM images [50]. A second (related) fea-
ture is that the 2D-RFIM has no true phase transition in
the thermodynamic limit. In ﬁnite systems, there may
be signs of a transition (or even several transitions; note
that some of the distributions in Fig. 5(a) are triple-
peaked), but they will be “smeared” over a wide temper-
ature range, and do not persist in the thermodynamic
limit. Precisely this behavior has also been reported in
experiments [48, 50]. Simulation evidence that the pin-
ning sites prevent a sharp transition in the thermody-
namic limit follows from the (disorder-averaged) Binder
cumulant U1 =

∆2
/[⟨|∆|⟩2], where [·] denotes an av-
erage over diﬀerent samples of pinning sites. As shown
in Fig. 6, U1 →π/2 as L increases, consistent with only
a single phase.
V.
CONCLUSION
In this paper, the main phase transition in single-
component phospholipid membranes was investigated us-
ing the Pink model. Our simulations of the pure mem-
brane (i.e. without quenched disorder) conﬁrm the forma-
tion of macroscopic gel and ﬂuid domains below a critical
temperature Tc, and at the coexistence pressure ΠCOEX.
We also demonstrated that, using the accepted values of
the Pink model parameters, Tc falls below experimentally
measured transition temperatures. This explains why no
phase transition was detected at the experimental transi-
tion temperature in the simulations of Ref. 18. To resolve
this issue, we propose that the strength of the van der
Waals coupling in the Pink model be increased. By using
the values proposed in this work, Tc of the Pink model in
the thermodynamic limit coincides with the experimen-
tal main transition temperature. In addition, ﬁnite-size
scaling was applied to conﬁrm the universality class of
the critical point in the Pink model, which was shown to
be 2D Ising. This result holds irrespective of the number
of conformational states q (as long as q ≥2, of course).
Hence, to capture the generic features of membrane phase
behavior, a highly-detailed model is not always needed
(which is consistent with the ﬁndings of Ref. 24).
We have also used the Pink model to describe the
main transition in the presence of quenched disorder,


## Page 8


8
which may arise in case the membrane is deposited on a
rough support. Assuming that this induces regions in the
membrane where certain tail conformations become pre-
ferred, the universality class changes toward that of the
2D random-ﬁeld Ising model. In the presence of quenched
disorder, the Pink model reveals a stable multi-domain
structure, and the absence of a sharp transition; these
ﬁndings are indeed consistent with some of the experi-
mental observations.
Although the Pink model (both the pure version and
the one containing quenched disorder) seems well suited
to describe the main transition, we wish to end with a
warning. By using the Pink model, one inevitably casts
the main transition into the Ising universality class. This
may not be entirely appropriate, as the main transition
is essentially a melting transition leading to the forma-
tion of nematic chain order. A liquid-crystal model may
therefore be more suitable, such as the Maier-Saupe ap-
proach followed in Ref. 54. If, indeed, the main transi-
tion occurs close to a critical point [43, 55] it may well be
necessary to replace the discrete set of states of the Pink
model by a continuous one [56]. In that case, one enters
the regime of Heisenberg-type models (which, provided
certain conditions are met, do support 2D phase transi-
tions [57–59]). The investigation of the main transition in
terms of such a continuous model could be an interesting
topic for future work.
ACKNOWLEDGMENTS
This work was supported by the Deutsche Forschungs-
gemeinschaft (Emmy Noether VI 483 and the SFB-937).
[1] Jacobson K, Mouritsen OG, and Anderson RGW, Lipid
rafts:
at a crossroad between cell biology and physics,
Nat. Cell Biol. 9, 7 (2007)
[2] Simons K and Ikonen E, Functional rafts in cell mem-
branes, Nature 387, 569 (1997)
[3] Engelman DM, Membranes are more mosaic than ﬂuid,
Nature 438, 578 (2005)
[4] Mouritsen OG, Physics of biological membranes, in:
D Baeriswyl,
M Droz, A Malaspinas,
and P Mar-
tinoli (Eds.), Physics in Living Matter, vol. 284 of
Lecture Notes in Physics, chap. 8, 76–109 (Springer,
Berlin/Heidelberg, 1987)
[5] Risbo J, Sperotto MM, and Mouritsen OG, Theory of
phase equilibria and critical mixing points in binary lipid
bilayers, J. Chem. Phys. 103, 3643 (1995)
[6] Keller D, Larsen NB, Møller IM, and Mouritsen OG, De-
coupled Phase Transitions and Grain-Boundary Melting
in Supported Phospholipid Bilayers, Phys. Rev. Lett. 94,
025701 (2005)
[7] Kranenburg M and Smit B, Phase Behavior of Model
Lipid Bilayers, J. Phys. Chem. B 109, 6553 (2005)
[8] Nagle JF, Theory of the Main Lipid Bilayer Phase Tran-
sition, Annu. Rev. Phys. Chem. 31, 157 (1980)
[9] Mouritsen OG, Theoretical models of phospholipid phase
transitions, Chem. Phys. Lipids 57, 179 (1991)
[10] M¨uller M, Katsov K, and Schick M, Biological and syn-
thetic membranes: What can be learned from a coarse-
grained description?, Phys. Rep. 434, 113 (2006)
[11] Orsi M, Michel J, and Essex JW, Coarse-grain mod-
elling of DMPC and DOPC lipid bilayers, J. Phys.: Con-
dens. Matter 22, 155106 (2010)
[12] H¨omberg M and M¨uller M, Main phase transition in lipid
bilayers: Phase coexistence and line tension in a soft,
solvent-free, coarse-grained model, J. Chem. Phys. 132,
155104 (2010)
[13] Marrink SJ, Risselada J, and Mark AE, Simulation of
gel phase formation and melting in lipid bilayers using
a coarse grained model, Chem. Phys. Lipids 135, 223
(2005)
[14] Pink DA, Green TJ, and Chapman D, Raman scattering
in bilayers of saturated phosphatidylcholines. Experiment
and theory, Biochemistry 19, 349 (1980)
[15] Pink DA, Georgallas A, and Zuckermann MJ, Phase
transitions and critical indices of a phospholipid bilayer
model, Z. Phys. B 40, 103 (1980)
[16] Caill´e A, Pink D, Verteuil FD, and Zuckermann MJ, The-
oretical models for quasi-two-dimensional mesomorphic
monolayers and membrane bilayers, Can. J. Phys. 58,
581 (1980)
[17] Mouritsen OG, Boothroyd A, Harris R, Jan N, Lookman
T, MacDonald L, Pink DA, and Zuckermann MJ, Com-
puter simulation of the main gel–ﬂuid phase transition of
lipid bilayers, J. Chem. Phys. 79, 2027 (1983)
[18] Corvera E, Laradji M, and Zuckermann MJ, Application
of ﬁnite-size scaling to the Pink model for lipid bilayers,
Phys. Rev. E 47, 696 (1993)
[19] Yethiraj A and Weisshaar JC, Why Are Lipid Rafts Not
Observed In Vivo?, Biophys. J. 93, 3113 (2007)
[20] G´omez J, Sagu´es F, and Reigada R, Eﬀect of integral
proteins in the phase stability of a lipid bilayer: Applica-
tion to raft formation in cell membranes, J. Chem. Phys.
132, 135104 (2010)
[21] Fischer T and Vink RLC, Domain formation in mem-
branes with quenched protein obstacles:
Lateral het-
erogeneity and the connection to universality classes,
J. Chem. Phys. 134, 055106 (2011)
[22] Machta BB, Papanikolaou S, Sethna JP, and Veatch SL,
Minimal Model of Plasma Membrane Heterogeneity Re-
quires Coupling Cortical Actin to Criticality, Biophys. J.
100, 1668 (2011)
[23] Ehrig J, Petrov EP, and Schwille P, Near-critical ﬂuc-
tuations and cytoskeleton-assisted phase separation lead
to subdiﬀusion in cell membranes., Biophys. J. 100, 80
(2011)
[24] Fischer T, Risselada HJ, and Vink RLC, Membrane lat-
eral structure: The inﬂuence of immobilized particles on
domain size, arXiv:1205.1001 (2012)
[25] Imry Y and Ma SK, Random-Field Instability of the Or-
dered State of Continuous Symmetry, Phys. Rev. Lett.
35, 1399 (1975)
[26] Imbrie JZ, Lower Critical Dimension of the Random-
Field Ising Model, Phys. Rev. Lett. 53, 1747 (1984)


## Page 9


9
[27] Bricmont J and Kupiainen A, Lower critical dimension
for the random-ﬁeld Ising model, Phys. Rev. Lett. 59,
1829 (1987)
[28] Aizenman M and Wehr J, Rounding of ﬁrst-order phase
transitions in systems with quenched disorder, Phys. Rev.
Lett. 62, 2503 (1989)
[29] Mouritsen OG, Boothroyd A, Harris R, Jan N, Lookman
T, MacDonald L, Pink DA, and Zuckermann MJ, Com-
puter simulation of the main gel–ﬂuid phase transition of
lipid bilayers, J. Chem. Phys. 79, 2027 (1983)
[30] Mouritsen OG, Computer Studies of Phase Transitions
and Critical Phenomena (Springer-Verlag, Berlin, 1984)
[31] Ipsen JH, Jørgensen K, and Mouritsen OG, Density ﬂuc-
tuations in saturated phospholipid bilayers increase as the
acyl-chain length decreases, Biophys. J. 58, 1099 (1990)
[32] Fischer T and Vink RLC, The Widom-Rowlinson mixture
on a sphere: elimination of exponential slowing down at
ﬁrst-order phase transitions, J. Phys.: Condens. Matter
22, 104123 (2010)
[33] Neuhaus T and Hager JS, 2D Crystal Shapes, Droplet
Condensation, and Exponential Slowing Down in Simu-
lations of First-Order Phase Transitions, J. Stat. Phys.
113, 47 (2003)
[34] Binder K, Monte Carlo calculation of the surface tension
for two- and three-dimensional lattice-gas models, Phys.
Rev. A 25, 1699 (1982)
[35] Virnau P and Muller M, Calculation of free energy
through successive umbrella sampling, J. Chem. Phys.
120, 10925 (2004)
[36] Ferrenberg AM and Swendsen RH, Optimized Monte
Carlo data analysis, Phys. Rev. Lett. 63, 1195 (1989)
[37] Fischer T and Vink RLC, Restricted orientation ”liquid
crystal” in two dimensions: Isotropic-nematic transition
or liquid-gas one(?), EPL 56003 (2009)
[38] Orkoulas G, Fisher
ME, and Panagiotopoulos
AZ,
Precise simulation of criticality in asymmetric ﬂuids,
Phys. Rev. E 63, 051507 (2001)
[39] Binder K, Finite size scaling analysis of ising model block
distribution functions, Z. Phys. B 43, 119 (1981)
[40] Binder K, Critical Properties from Monte Carlo Coarse
Graining and Renormalization, Phys. Rev. Lett. 47, 693
(1981)
[41] Orkoulas G, Panagiotopoulos AZ, and Fisher ME, Crit-
icality and crossover in accessible regimes, Phys. Rev. E
61, 5930 (2000)
[42] Newman MEJ and Barkema GT, Monte Carlo Methods
in Statistical Physics (Clarendon Press, Oxford, 1999)
[43] Doniach S, Thermodynamic ﬂuctuations in phospholipid
bilayers, J. Chem. Phys. 68, 4912 (1978)
[44] Michonova-Alexova EI and Sug´ar IP, Component and
state separation in DMPC/DSPC lipid bilayers: a Monte
Carlo simulation study., Biophys. J. 83, 1820 (2002)
[45] Ehrig J, Petrov EP, and Schwille P, Phase separation and
near-critical ﬂuctuations in two-component lipid mem-
branes: Monte Carlo simulations on experimentally rele-
vant scales, New J. Phys. 13, 045019 (2011)
[46] Mouritsen OG, Studies on the lack of cooperativity in the
melting of lipid bilayers, BBA – Biomembranes 731, 217
(1983)
[47] Xie AF, Yamada R, Gewirth AA, and Granick S, Ma-
terials Science of the Gel to Fluid Phase Transition in
a Supported Phospholipid Bilayer, Phys. Rev. Lett. 89,
246103 (2002)
[48] Tokumasu F, Jin AJ, Feigenson GW, and Dvorak JA,
Atomic force microscopy of nanometric liposome adsorp-
tion and nanoscopic membrane domain formation, Ultra-
microscopy 97, 217 (2003)
[49] Seeger HM, Cerbo AD, Alessandrini A, and Facci P, Sup-
ported Lipid Bilayers on Mica and Silicon Oxide: Com-
parison of the Main Phase Transition Behavior, J. Phys.
Chem. B 114, 8926 (2010)
[50] Charrier A and Thibaudau F, Main Phase Transitions
in Supported Lipid Single-Bilayer, Biophys. J. 89, 1094
(2005)
[51] Yang J and Appleyard J, The Main Phase Transi-
tion of Mica-Supported Phosphatidylcholine Membranes,
J. Phys. Chem. B 104, 8097 (2000)
[52] Billoire A, Neuhaus T, and Berg BA, A determination of
interface free energies, Nucl. Phys. B 413, 795 (1994)
[53] Karatekin E, Sandre O, Guitouni H, Borghi N, Puech
PH, and Brochard-Wyart F, Cascades of Transient Pores
in Giant Vesicles:
Line Tension and Transport, Bio-
phys. J. 84, 1734 (2003)
[54] Marcelja S, Molecular Model for Phase Transition in Bi-
ological Membranes, Nature 241, 451 (1973)
[55] Marˇcelja S, Chain ordering in liquid crystals, BBA -
Biomembranes 367, 165 (1974)
[56] Scoville-Simonds M and Schick M, Theory of the eﬀect of
unsaturation on the main-chain transition, Phys. Rev. E
67, 011911 (2003)
[57] van Enter ACD and Shlosman SB, First-Order Transi-
tions for n-Vector Models in Two and More Dimensions:
Rigorous Proof, Phys. Rev. Lett. 89, 285702 (2002)
[58] Bl¨ote HWJ, Guo W, and Hilhorst HJ, Phase Transi-
tion in a Two-Dimensional Heisenberg Model, Phys. Rev.
Lett. 88, 047203 (2002)
[59] Fish JM and Vink RLC, Finite-size eﬀects at ﬁrst-order
isotropic-to-nematic transitions, Phys. Rev. B 80, 014107
(2009)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1205_1767v1_the_main_transition_in_the_pink_membrane_model_finite_size_scaling_and_the_infl
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2012/1205_1767V1_THE_MAIN_TRANSITION_IN_THE_PINK_MEMBRANE_MODEL_FINITE_SIZE_SCALING_AND_THE_INFL.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

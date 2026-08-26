---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1609.01569v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1609.01569v1_Statistical_Mechanics_and_Kinetics_of_Amyloid_Fibrillation

> Source: 1609.01569v1_Statistical_Mechanics_and_Kinetics_of_Amyloid_Fibrillation.pdf

> Pages: 68

---


## Page 1


Statistical Mechanics and Kinetics of Amyloid Fibrillation
Liu Hong1,∗,
Chiu Fan Lee2,∗, Ya Jing Huang1
1Zhou Pei-Yuan Center for Applied Mathematics, Tsinghua University, Beijing 100084, P.R. China
2Department of Bioengineering, Imperial College London, South Kensington Campus, London SW7 2AZ, UK
∗Correspondence: zcamhl@tsinghua.edu.cn, c.lee@imperial.ac.uk
Amyloid ﬁbrillation is a protein self-assembly phenomenon that is intimately related to well-
known human neurodegenerative diseases. During the past few decades, striking advances have been
achieved in our understanding of the physical origin of this phenomenon and they constitute the
contents of this review. Starting from a minimal model of amyloid ﬁbrils, we explore systematically
the equilibrium and kinetic aspects of amyloid ﬁbrillation in both dilute and semi-dilute limits. We
then incorporate further molecular mechanisms into the analyses. We also discuss the mathematical
foundation of kinetic modeling based on chemical mass-action equations, the quantitative linkage
with experimental measurements, as well as the procedure to perform global ﬁtting.
L.H. and Y.J.H. would like to dedicate this paper to the memory of Prof. Chia-Chiao Lin (1916-2013), a great
applied mathematician, a beloved advisor and a dear friend, on his 100-year anniversary.
List of Symbols
[Ai]
Concentration of ﬁlaments of size i
[Ci]
Concentration of cells in state i
Ns(ns) Number (concentration) of s-mer
N (β)
s
(n(β)
s ) Number (concentration) of monomers in the beta-sheet conﬁguration
N R
s (nR
s ) Number (concentration) of monomers in the random coil conﬁguration
m
Monomer concentration
P
Number concentration of total aggregates
M
Mass concentration of total aggregates
Poli
Number concentration of oligomers
Moli
Mass concentration of oligomers
arXiv:1609.01569v1  [q-bio.BM]  6 Sep 2016


## Page 2


2
mtot
Total concentration of proteins
m0
Initial monomer concentration
P0
Initial number concentration of aggregates
M0
Initial mass concentration of aggregates
nc
Critical nucleus size for primary nucleation
n2
Critical nucleus size for secondary nucleation
Km
Critical saturation concentration for elongation
Ks
Critical saturation concentration for secondary nucleation
m∗
F
Critical ﬁbrillar concentration
m∗
M
Critical micellar concentration
k+
e
Rate constant for monomer association
k−
e
Rate constant for monomer dissociation
kn
Rate constant for primary nucleation
k2
Rate constant for surface catalysed secondary nucleation
k+
f
Rate constant for ﬁlaments fragmentation
k−
f
Rate constant for ﬁlaments annealing
k+
c
Forward reaction rate constant for conformation conversion
k−
c
Backward reaction rate constant for conformation conversion
k+
b
Rate constant for membrane binding
k−
b
Rate constant for membrane unbinding
kapp
Apparent ﬁber growth rate
kmax
Maximal ﬁber growth rate
t1/2
Half-time for ﬁbrillation
tlag
Lag-time for ﬁbrillation


## Page 3


3
I.
INTRODUCTION
The importance of understanding amyloid ﬁbrillation comes not only from its intimate relation to amyloid diseases,
such as the well-known Alzheimer’s, Huntington’s and Parkinson’s diseases [1, 2], but also from its physical simplicity
and universality as a typical self-assembling phenomenon of linear biomolecules [3]. Various thermodynamic and
kinetic approaches borrowed from classical polymer statistical mechanics, the kinetics of chemical reactions as well
as non-equilibrium processes have been developed and applied to experimentally and biologically relevant amyloid
systems with great success [4–6]. Related fruitful results, developments and applications in the past decades constitute
the focus of our current paper: a self-contained review on the thermodynamic and kinetics of amyloid ﬁbrillation.
Thermodynamics and kinetics are two sides of the same coin. The latter deals with time-dependent ﬁbrillation
processes in general; while the former is more focused on the ﬁnal time-independent properties of the amyloid system
– the equilibrium state. In the current review, we will present the thermodynamics and kinetics of amyloid ﬁbrillation
separately in order to keep each part clear and self-contained. But readers should bear in mind of the intrinsic corre-
lations between those two descriptions, like requirements on reaction rate constants for various ﬁbrillation processes
in order to guarantee the existence of a genuine thermodynamic equilibrium state [7].
The whole review is organized into three major sections. The ﬁrst one is focused on the thermodynamics of amyloid
ﬁbrillation by using the language of statistical mechanics; the next two are devoted to kinetic descriptions based
on chemical mass-action equations. To be speciﬁc, the former provides a systematic exploration of various amyloid
ﬁbrillation processes, including both model formulation and analysis; while the latter is about the mathematical
foundation of kinetic modeling as well as its linkage with experimental observations.
II.
STATISTICAL MECHANICS OF AMYLOID FIBRILLATION
Although polymer physics is a well established ﬁeld of science, novel physics governing the behaviour of the systems
is still being uncovered. In the case of self-assembling biopolymers, the novelty comes from the fact that the binding
energy driving the polymerization process is relatively low compared to covalently bonded polymers. Hence, polymer
breakage and re-joining can potentially contribute to the polymerization kinetics at an experimentally and physiolog-
ically relevant scale. The polymeric system is thus called “living” since every polymer can shrink through breakage
and grow through elongation via monomer additions and through end-to-end joining with another polymer. Taking
these processes into account are important for the complete description of the kinetics of self-assembling polymers.


## Page 4


4
In this section, we will focus purely on how a system of living semi-ﬂexible polymers behave at thermal equilibrium.
FIG. 1: (A) A system of spherical particles (beads) with sticky patches on polar ends will self assemble into polymers if the
patches are stickiness enough (B). (C) In the minimal model considered here, the interactions within polymer act as Hookean
springs between the beads to enforce extensile restriction and rigidity. The size of the beads has been shrunken to show the
springs. (D) The speciﬁc potential energy functions governing the deviation in extension △l (solid line) and angle △θ (broken
line) are assumed to be quadratic.
A.
How to construct a minimal model
We will start by considering a minimal model of polymerizing monomers as depicted in Fig. 1A. Namely, the
monomers are purely spherical particles (beads) with two sticky patches at two opposite ends. We assume that the
beads are in an over-damped environment and so their movement is Brownian. The “stickiness” is short-ranged and
is quantitatively described by two quadratic energy functions: one controls the distance between the connected beads
and the other enforces the rigidity of the resulting polymers (Fig. 1C and 1D). We denote the distance between two
connected beads by l0 + △l. Given any consecutive segment of three monomers in a polymer, if the three monomers


## Page 5


5
are not co-linear, we denote the angular deviation by △θ (Fig. 1C). A polymer thus consists of a series of beads such
that for all consecutive pairs of beads, the absolute values of the deviations, |△l|, are smaller than the distance cutoﬀ
lc; and that all deviation angles, △θ, are also less than the cutoﬀθc. The energy function for such a s-polymer is then
U({x}) =
s−1
X
k=1
A△l2
k +
s−2
X
h=1
B△θ2
h −E(s −1),
(1)
where k enumerates the number of distant bonds, h enumerates the number of angular bonds, and E is the binding
energy between the patches that promotes aggregation.
Let us now imagine that at t = 0, we put these monomers in an inert solvent of a certain temperature T (Fig. 1A).
The solvent is inert in the sense that their role in the system is purely to provide the thermalizing eﬀects of a heat
bath. The whole system is further connected to a much larger thermal bath of temperature T in such a way that
heat, but not the beads, can ﬂow back and forth between the system and the large heat bath. In other words, we
are investigating the system from the perspective of a canonical ensemble [8]. The setup of this thought experiment
corresponds to a typical experimental procedure in which polymerising monomers are ﬁrst dissolved in an appropriate
solvent and then left unperturbed in the course of the experiment. In our case, if the binding energy is strong enough
(i.e., E is large), then we expect that these monomers will self-assemble into polymers (Fig. 1B). Here, we will assume
that the threshold angle θc is small enough that we do not need to worry about the interactions of distant parts of the
same polymer beyond what is already considered in our energy function. In particular, we can ignore the formation
of loops in the system.
Although highly simpliﬁed, the model presented here is of relevance to some colloidal systems studied experimentally
[9]. But as we will show, the greatest virtue of this minimal model is its analytical tractability.
B.
How to deal with the dilute limit
By the dilute limit, we mean that the concentration of solute and the resulting polymers in the system are dilute
enough that we can ignore all solute interactions except those that lead to polymerization as described in the previous
section. Given this assumption, the free energy density of the overall system can be calculated with the mean-ﬁeld
method. Speciﬁcally, we consider a system of N monomers in a volume V . The total partition function can be written
in terms of the internal partition function of a single s-mer with its ﬁrst bead’s position ﬁxed in space, zs, in the
following manner [10]:
Ztot =
′Y
s
1
Ns!
V zs
Λ3
Ns
,
(2)


## Page 6


6
where Ns denotes the number of s-mers in the system and the prime in the product denotes the number conservation
of monomers: P∞
s=1 sNs = N. Since we are dealing with “classical” (i.e., not quantum mechanical) objects, the kinetic
part of the partition function (resulting from momentum integrations) is irrelevant [11] and so Ztot corresponds to the
conﬁgurational partition function, with Λ being an arbitrary constant of dimension length to make Ztot dimensionless.
The denominator Ns! is in (2) because the s-mers in the system are all indistinguishable and that the free energy
is extensive. Note that these polymers are indistinguishable purely because we have chosen not to distinguish them
in our analysis, which is typically the case in experiments [12].
The total partition function in (2) follows from a mean-ﬁeld approximation in the sense that the sequence {Ns} is
ﬁxed by minimizing the free energy of the system
Ftot = −kBT log Ztot .
(3)
In other words, ﬂuctuations away from the minimising sequence {Ns} are ignored. Such an approximation is expected
to be qualitatively correct away from any critical points [8], which, as we shall see, this system does not possess.
To proceed further analytically, we still need to calculate the s-mer partition function zs, which is of the form:
zs = 4πl2
0e(s−1)βE
Λ3(s−1)
 Z lc
−lc
d△le−βA△l2
!s−1  
l2
0
Z θc
0
d△θ sin(△θ)e−βB△θ2
!s−2
= 4π3/2l2
0eβE
Λ3√βA

l2
0
√πeβE
Λ3β3/2√
AB
s−2
,
(4)
for s > 1, while z1 = 1. Note that in (4), the factor 4πl2
0 comes from integrating over the orientation of the polymer
given that the ﬁrst bead is ﬁxed in space, the integrals in the ﬁrst brackets stem from the longitudinal degrees of
freedom and the those in the second brackets from the angular degrees of freedom along the polymer chain. To arrive
at (4), we have taken the limits of integration to inﬁnity, which is legitimate since βA, βB are typically high where
β ≡kBT.
The total free energy can now be expressed as
Ftot = −kBT
′
X
s

Ns log
V zs
Λ3

−log Ns!

= −kBT
′
X
s

Ns log
V zs
Λ3

−Ns log Ns + Ns

= β−1
(
N1

log N1 −log V
Λ3 −1

+
′
X
s
Ns

log Ns −log V
Λ3 −χs −ξ −1
)
,
(5)


## Page 7


7
and
ξ = log 4π1/2Λ3β5/2A1/2B2
l2
0
−βE,
(6)
χ = log
l2
0π1/2
Λ3β3/2A1/2B + βE .
(7)
Given (5), we can ﬁnally minimise Ftot with respect to Ns using the Lagrange multiplier method to enforce the
conservation P
s sNs = N. To do so, we minimise the following summation with λ being the Lagrange multiplier
Ftot + λ(
X
s
sNs −N)
(8)
with respect to the set {Ns}, which leads to
N1 =
V
Λ3 eλ,
(9)
Ns =
V
Λ3 e(χ+λ)s+ξ
for s > 1,
(10)
or for s > 1,
Ns
V
= K
N1
V
1
m∗
F
s
,
(11)
where
m∗
F = β3/2A1/2B
l2
0π1/2eβE ,
(12)
K = 4π1/2β5/2A1/2B2
l2
0eβE
.
(13)
(11) expresses the s-mer concentration ns ≡Ns/V in terms of monomer concentration m = n1 ≡N1/V . Since s can
be as big as we want, by the conservation of mass (P
s≥1 sns = N/V ≡mtot), we know that m can never exceed
m∗
F for otherwise the terms in the brackets in (11) will blow up with s. Indeed, we shall see that m asymptotically
approaches m∗
F as mtot increases. For this reason, we shall call m∗
F the critical ﬁbrilar concentration (CFC) [10, 13].
Note that although the system transition from being monomer-dominated to ﬁbril-dominated as mtot increases, it
never goes through a phase transition in the thermodynamic sense [11] since the derivatives of the free energy are
always continuous. This is also reﬂected, e.g., by the lack of discontinuities in mtot (Fig. 2). In the regime where
mtot ≫m∗
F , m ≃m∗
F , and (11) shows that the size distribution of polymers is exponential, with the average size
given by
p
mtot/K [10, 14–16].
Let us now try to substitute in experimentally motivated parameters to see how our model corroborate with
observation. Since we are primarily interested in protein aggregation, we take the average size l0 to be 1nm, and


## Page 8


8
the binding energy E to be 25kBT. To estimate the spring constant A and B, we make the assumption that each
monomer within a polymeric chain has a wriggle room of around 10% of its size, i.e., lc ∼l0/10 and θc ∼0.1rad.
From this we can estimate A as 100E/l2
0 and B as 100E. Using these parameters, we ﬁnd that m∗
F ≃9.8×10−7nm−3
or around 9.8µM. The corresponding ﬁbrillation behaviour of this system is shown in Fig. 2.
With regard to experimental observation, the predicted exponential length distribution seems to deviate from some
experimental studies [17, 18]. Van Raaij et al. has interpreted the observed peaks as a result of the ﬁnite resolution
of the atomic force microscopy imaging and length measurement procedure [19]. Besides this explanation, it is also
known that it can take on the order of months for mature ﬁbrils to form [20]. Therefore, the appearance of the peaks
observed may also reﬂect the fact that the self-assembled systems have not yet reached thermal equilibrium.
0
5
10
0
0.2
0.4
0.6
0.8
1 x 10
−6
(A)
mtot [nm−3]
m [nm−3]
0
5
10
0
2
4
6
8
10
(B)
 [nm−3]
mtot−m [nm−3]
50
100
150
200
0
0.005
0.01
0.015
0.02
0.025
0.03
0.035
s
(C)
ns [nm−3]
mtot
FIG. 2: Using the parameters in the text, (A) depicts how the monomer concentration changes as monomer concentration
increases; and correspondingly for the concentration of the ﬁbrilar species (B). (C) The size (length) distribution of the system
at mtot ≃10nm−3. The distribution is exponential but note the discontinuity at s = 1 (highlighted by the red circle). The
unit of the concentrations is nm−3.
C.
How to generalize to the semi-dilute limit
In the dilute limit, mutual interactions between the solutes beyond the polymerizing interactions are ignored. What
if we now increase the concentration of the solute so that such an approximation is no longer valid. This takes us
to the semi-dilute limit. We will ﬁrst discuss the simplest and ubiquitous type of interactions: volume exclusion
interactions.


## Page 9


9
1.
Pure volume exclusion interactions
To take steric interactions into account, we start again with the non-interacting free energy density (see (5)):
f0 = β−1
Z
dsn(s)

log n(s) + log Λ3 −χs −ξ −1

,
(14)
where we have ignored the monomeric contribution, and pass to the continuum description in s since we are primarily
interested in the ﬁbril-dominant regime (mtot ≫CFC). We then add to f0 the following interaction term:
fint =
Z
dsds′n(s)n(s′)B(s, s′) .
(15)
In the above equation, B(s, s′) is the second virial coeﬃcients corresponding to the steric interactions of two semi-
ﬂexible polymers of length s and s′, and is of the form [21]:
B(s, s′) = 2π
3 l3
0 + π(s + s′)l3
0
2
+ 2ss′l3
0| sin φ|,
(16)
where φ is the angle between the two polymers. To deal with the additional variable φ, we ask ourselves what would
happen to the system given the steric interactions. From the physics of liquid crystals [22, 23], we expect that as the
polymer concentration increases, the system can become nematic, i.e., the semi-ﬂexible polymers will be aligned.
In other words, we anticipate that similar to liquid crystals [23], as the solute concentration increases, the system
will ﬁrst go through a phase separation where the regions of the system can be partitioned into two phases, one
nematic and the other isotropic. If the concentration increases further, the system will become fully nematic. This
is indeed what is observed experimentally in, for instance, a system of ﬁbrilising hens lysozyme [24] (Fig. 3). We
will now incorporate this expected picture into our free energy minimisation. Speciﬁcally, we will consider both free
energy densities in the isotropic and nematic phases, fI and fN respectively. For fI, we can simply add to (5) the
average over the angle that two randomly oriented semi-ﬂexible make (since the system is isotropic) in (16), hence
fI = f0({nI(s)}) +
Z
dsds′n(s)n(s′)
2π
3 l3
0 + π(s + s′)l3
0
2
+ πss′l3
0

.
(17)
Using again the Lagrange multiplier method to enforce protein number conservation, one ﬁnds that the distribution
nI(s) that minimises fI is exponential as before, although the mean size is now
p
mIe8ψI/3/K, where mI is the total
protein concentration and ψI is the volume fraction of proteins in the isotropic phase [25].
In the nematic phase, the picture is more complicated. Since the polymers can elongate, it was found that the
ﬂexibility of the polymer has to be taken into account in order to stop the unrealistic lengthening of the polymers in
the nematic phase [26]. Here, we will again quote the results in [25], in which it was found that by minimising the free


## Page 10


10
energy in the nematic phase, the length distribution is again exponential, and the mean size is now approximately
p
mNe4ψI/K. Here, mN is the total protein concentration in the nematic phase. These results are in the regime
where the mean polymer length is much greater than the persistence length of the polymer.
Minimizing fI and fN separately is not the whole story since there is also the possibility of phase separation.
Namely, the volume of the system can be partitioned into isotropic and nematic regions. In the thermodynamic limit,
we usually ignore the surface energy coming from the interface separating the isotropic and nematic regions. The
minimisation is thus performed on the following free energy density:
ftot(vtot, mtot) = vIfI(mI) + vNfN(mN)
vtot
,
(18)
where vI(vN) is the total volume of the isotropic (nematic) regions and cI(cN) is solute concentration in the isotropic
(nematic) regions. The conservation laws are therefore vI + vN = vtot and vImI + vNmN = vtotmtot. Minimising
ftot with respect to v and m ﬁnally enables us to conﬁrm the expectation we had from the beginning. Namely, as
solute concentration increases, regions of nematic phase appear in the system and co-exist with the isotropic phase.
The polymer length distributions in both phase remain exponential, although the average length in the nematic
is higher than that in the isotropic region [27]. As the solute concentration increases further, regions of isotropic
phase disappear and the whole system will be in the nematic phase. As mentioned, these theoretical ﬁndings are
corroborated by experimental study on self-assembling hens lysozyme [24, 28] (see Fig. 3).
FIG. 3: Glass vials (1 cm wide) with hen lysozyme ﬁbril containing solutions imaged between crossed polars. Concentrations
are indicated in mM. The lit up regions correspond to the nematic phase. Image is taken from [24] with copyright permission.
2.
With lateral interactions
We have seen how the isotropic-nematic phase transition in a system of semi-ﬂexible polymers is typically ac-
companied by phase separation. In this section, we will show that if the polymers are mutually attractive (beyond


## Page 11


11
the end-to-end binding that leads to the joining of the two polymers), then the tendency for phase separation is
even stronger. Speciﬁcally, using again our minimal model system shown in Fig. 1, we imagine that besides the
strong directional attractive interactions schematically depicted by the red (dark grey) patches, the beads are weakly
attractive(∼kBT) towards each other, i.e., the green (light grey) areas of the beads are also weakly sticky.
To appreciate conceptually how interacting polymers behave at thermal equilibrium, the Flory-Huggins theory is
a good starting point since it is conceptually simple and can be easily analysed numerically. Here, we will ignore the
rigidity of the polymers and focus solely on the eﬀects of attractive interactions on the system’s phase behaviour.
Using the lattice model where each lattice site can be either occupied by one solvent molecule and by one monomer,
the following Flory-Huggins free energy density of mixing can be derived [29]:
fm(φ) = 1
¯nφ ln φ + (1 −φ) ln(1 −φ) + χφ(1 −φ),
(19)
where φ is the volume fraction of the polymers in the system and ¯n is the number of monomers in the polymer.
We note that in the above formula, all polymers are of the same length, i.e., we have ignored the disperse length
distribution here for simplicity. The parameter χ summarises the interactions of the monomers and is of the form
χ ≡
z
2kBT [2ems −emm −ess],
(20)
where emm, ess, ems are the interaction energy for the monomer-monomer, solvent-solvent, and monomer-solvent
pairs on the lattice, respectively. Here, we assume that the monomers are weakly attractive (emm ∼−kBT) and for
simplicity, we set ess = 0 = ems. Moreover z is the coordination number of the lattice, which for a 3D cubic lattice is
6. As a result, the interaction parameter χ is −3emm/kBT.
The ﬁrst two terms in (19) promotes phase separation, while for positive χ, fm becomes concave down when χ is
large enough, this is a signature of phase separation, which means that we will need to minimise the total free energy
by considering the possibility of having the system partition into two parts of distinct phases as in the previous section
(see (18)). A typical phase diagram is shown in Fig. 4.
The key feature here is that as the polymers elongate, the tendency to phase separate gets stronger even if the
polymers are only weakly attractive towards each other. Experimentally, it is observed that many amyloid ﬁbrils
aggregate in solution and thus in-vitro and in-vivo phase separation of amyloid ﬁbrils may be expected to occur.
Indeed, the observed clustering of sup35 ﬁbrils in the cytoplasm of yeast cells may be a signature of such phase
separation (Fig. 5).


## Page 12


12
FIG. 4: A typical phase diagram of a phase separating polymeric system according to the classic Flory-Huggins theory [30].
Phase separated polymer drops (inset) form in the two-phase region is bounded by the blue (dark grey) curve. At ﬁxed peptide
volume fraction, the tendency for the system to phase separate increases as the self-assembled ﬁbrils elongate (indicated by the
red (light grey) arrow).
D.
How to incorporate oligomers
We have so far focused on the behaviour of ﬁbrilising system in which there are only monomers or ﬁbrils. In the
case of amyloid ﬁbrils, the situation is more complex. Indeed, mounting evidence has indicated that proteins in the
monomeric form and oligomeric form (potentially amorphous aggregates of tens of proteins), instead of proteins in
the ﬁbrillar form, are predominantly responsible for cell death [32]. In this section, we will incorporate the oligomeric
species into our analysis. To model the presence of oligomers, we borrow the treatment of spherical micelles formation
in a solution of surfactants [13].
Speciﬁcally, we assume that the monomers can aggregate together to form an
amorphous cluster.
However, there is an optimal number of monomers, W, in the cluster in the sense that the
corresponding cluster partition function is greatest. In this system, a monomer can be classiﬁed into three categories:
(1) monomeric, (2) part of an oligomer (which we call a micelle), and (3) part of an ﬁbril. The total partition function
in this system can be written as [10]:
Ztot =
′Y
s,p
V N1
Λ3N1N1!
(V z(f)
s
)Ns
Λ3NsNs!
(V z(m)
p
)Mp
Λ3MpMp! ,
(21)


## Page 13


13
FIG. 5:
(A) Section through a tomogram of a yeast cell in which amyloid ﬁbrils formed from Sup35 are close to the cell
membrane. The nucleus is outlined in magenta and the vacuole in brown. (B) Rendered 3D model from serial tomograms
of this cell. Amyloid ﬁbrils are in green; membrane, blue; nucleus, magenta; vacuole, brown; mitochondria, purple; and large
complexes (presumably ribosomes) as gray dots. (C) Section through of a cell in which the aggregate of amyloid ﬁbrils is of
a form of a drop (green). (D) Rendered 3D model of the dot from serial tomograms. (Coloring as in B.) This ﬁgure is taken
from [31] with copyright permission.
where z(f)
s
and z(m)
p
are the internal partition functions for the ﬁbrillar and micellar species. We have also singled out
the monomeric contribution to the partition to highlight the fact that there are three diﬀerent species in the system.
We now model the micellar partition function as
z(m)
p
= δpW
 α
Λ3
W −1
eW Em ,
(22)
where α is of the order of the dimension of the monomer. Speciﬁcally, all micelles are assumed to be of size W for
simplicity and the clustering is driven by the binding energy Em per monomer. If we ignore the ﬁbrillar species for the
time being, then using again the Lagrange multiplier method as before, we ﬁnd that we can again relate the micellar
concentration to the monomer concentration m:
mW = 1
α
 m
m∗
M
W
,
(23)
where m∗
M = (αeβEm)−1. For W ∼O(10), we can see that m is bounded above at around m∗
M, i.e., most monomers
are in the micellar form at mtot > m∗
M. On the other hand, for m ≪m∗
M, mK is negligible. For this reason, we call
m∗
M the critical micellar concentration (CMC).
If we now incorporate the ﬁbrilar species into the picture, the system is eﬀectively partitioned into multiple regimes:
if mtot is smaller than both the CMC and the CFC, then the system is dominated by mtot. If the CMC is lower than
the CFC and mtot > CMC, then the micellar species will dominate the system; while if the CFC is lower than the
CMC, ﬁbrils will be dominant if mtot > CFC [10] (Fig. 6A). Note that even though if the CFC is lower than the CMC,


## Page 14


14
the micelles would still be transiently present in the system, and their existence may have important implications in
the ﬁbrillation kinetics as proposed in [33] (Fig. 6B). A similar model has also been recently studied using molecular
dynamics simulation in [34].
FIG. 6: (A) At ﬁxed mtot, the system can be dominated by distinct species depending on the strength of the ﬁbrilar binding
energy EF and the micellar binding energy EM. (B) A schematic of a potential nucleation pathway of ﬁbrillation proposed in
[33]. Starting with a pool of monomers, micelles form quickly due to the fast (potentially diﬀusion-limited) formation kinetics.
within the micelles, the protein concentration is high and thus facilitates the slow nucleation of nuclei of ﬁbrils. As ﬁbrils
elongate, the monomers in the system will be eventually depleted below the CMC and thus the micelles will disappear in the
system.
E.
How to incorporate internal monomeric structures
Another natural generalisation of our minimal bead-and-stick model is the incorporation of the internal monomeric
structure into our analysis. A peptide can in general be in multiple states, e.g., in the form of a beta sheet, random
coil, alpha helix. In the speciﬁc case of Aβ peptides, the monomeric state is in the random-coil conﬁguration, while
the peptides are predominately in the beta-sheet state in the ﬁbrillar form [35]. In terms of our minimal model, we
can account for this modiﬁcation by assigning a nonzero value to the monomeric partition function z(R)
1
= γ > 0
corresponding to the random coil state in (2); while for monomers in the beta-sheet form, the monomeric partition
function z(β)
1
is again set to one. Here, γ is positive means that the monomer in the random coil state is preferred
over the beta sheet state in the ﬁbrillar form, which originates from the fact that the random coil is entropically
more favourable. At thermal equilibrium, we expected have m(β) = e−γm(R). The total monomer concentration
m is therefore m(β) + m(R) = m(R)(1 + e−γ). Incorporating the ﬁbrillar species into the picture and writing the


## Page 15


15
concentration of s-mers in terms of that of the monomer as done in (11), we have
ns = K
 m(R)
eγm∗
F
s
= K
 m
ˆm∗
F
s
(24)
where ˆm∗
F is (1+eγ)m∗
F (see (11)). In other words, most of qualitative analyses as before remains the same, except now
the critical ﬁbrillar concentration is increased by the factor (1+eγ), which signiﬁes that the monomeric concentration
m is generally increased when the random coil-beta sheet transition [36, 37] is taken into account at the monomeric
level. We note that a more detailed analysis of the eﬀects of the degree of freedom from the monomeric conformation
can be found in [3].
F.
How to incorporate multiple ﬁbril morphologies
Besides the possibility of micelle formation, real biopolymers, and amyloid ﬁbrils in particular, are likely to consist
of two or more ﬁlaments. In addition, multiple morphologies may co-exist in the system [38]. The simplest way to
model such a system is to imagine that each bead in Fig. 1A also possesses a sticky patch on the equator. If the new
“patch on the side” is small in area, then a two-ﬁlament ﬁbril will form naturally (Fig. 7). In fact, many amyloid ﬁbrils
seemed to consist of ﬁlaments twisted together, which could be incorporated into our minimal model by twisting the
location of the side patch along the axial direction (Fig. 7). The formalism employed so far can again be generalised
to consider this system. Interestingly, as far as minimising the total free energy is concerned, the only eﬀects of the
lateral association of ﬁlaments are to double the capping energy E, where the factor 2 comes from the additional
axial bond due to the bundling of the two ﬁlaments [27]. Because of this increase of capping energy via bundling, the
species that dominate the system will always be the two-ﬁlament polymers. So how does this theoretical predictions
square with experimental observations that multiple morphology exist? The simplest resolution again points to the
conclusion that under typical experimental conditions, the self-assembly of amyloid ﬁbril has not yet reached the
thermal equilibrium state.
G.
Summary
Here we will summarise the key conclusions one can draw from statistical mechanics with regards to biopolymer
self-assembly.
1. The existence of a critical ﬁbrillar concentration (CFC) below which ﬁbrillar mass is negligible. The emergence


## Page 16


16
FIG. 7: A schematic of a twisting ﬁbre consisting of two ﬁlaments. In this model, besides the axial bonds (blue arrows) along
the longitudinal direction of the ﬁbre, there are lateral bonds (red patched) that bind the two ﬁlaments together.
of such a critical concentration comes purely from the fact that the aggregates concerned consist of a large
number of monomers.
2. Above the CFC, the length distribution of the ﬁbrils is exponential. This remains so even in the semi-dilute
limit if the ﬁbril-ﬁbril interactions are purely steric.
3. When micellar or other oligomeric species are taken into account, each distinct type of aggregates will have their
speciﬁc critical concentrations, and the one with the lowest critical concentration will have the dominating mass
density at high protein concentration (Fig. 6).
4. If ﬁbrils of distinct widths exist, the mass density of the widest ﬁbrils will dominate the system at thermal
equilibrium.
5. If the ﬁbrils exhibit attractive lateral interactions, there will be a strong tendency for phase separation of ﬁbrils
to occur.
We note that the existence of CFC is a well established experimental observation. However, experimentally measured
ﬁbrillar length distributions seem generally to deviate from the predicted exponential distribution.
In addition,
multiple morphologies of ﬁbrils seem to co-exist in typical experimental conditions. These observations indicate that
protein amyloid formation does not reach thermal equilibrium at the typical experimental timescale. Therefore, to
account quantitatively for the experimental observation, we generally need a kinetic description of amyloid ﬁbrillisation
tailored for the speciﬁc experimental condition.
III.
KINETICS OF AMYLOID FIBRILLATION
In the ﬁrst part, we have presented a general review on the thermodynamics of amyloid ﬁbrillation. However, due
to the lack of a mature non-equilibrium thermodynamics theory, currently we can only deal with the equilibrium


## Page 17


17
states and the phase transition between them. In order to understand many unsolved puzzles concerning with the
time evolution of an amyloid system, such as how ﬁbrils grow, how they replicate, how they interact with cells and be
cytotoxic, we need to turn to a kinetic theory. The mathematical modeling based on chemical mass-action equations
provides us a uniﬁed framework as well as a quantitative linkage between experimental observations and underlying
molecular mechanisms. Fruitful results and interesting physical insights have been obtained based on this formulation
in the past several years. In what follows, we will focus on two aspects: one is a systematic exploration of the kinetic
formulation of amyloid ﬁbrillation, including both molecular mechanism basis and model analysis (Fig. 8); the other
is the mathematical foundation of kinetic modeling as well as its linkage with experimental facts.
A.
How ﬁbrils grow
When examining a given amyloid system, a ﬁrst question coming to mind usually would be how amyloid ﬁbrils are
able to grow? Regardless of various possible explanations for other self-assembling phenomena in nature [39–42], we
are really astonished at the fact that there is one truly simple answer valid for almost all amyloid ﬁbrils. That is
elongation, the process of which incorporates free protein molecules (or monomers as stated in literature) into existing
ﬁbrillar aggregates by monomer association and dissociation at ﬁbril ends in a linear sequential way. Elongation not
only is a geometrical consequence of the intrinsic one-dimensional structure of amyloid ﬁber, but also has a deep root
in both thermodynamics and kinetics, that is monomer association is more favorable than that of oligomers in general
[43, 44]. We will come back to this point later.
As an elementary step in amyloid ﬁbrillation, elongation has been paid great attention to in the past studies.
Pioneer works dated back to Oosawa and his colleagues for their preliminary examination on actin formation in the
late 1950s [45]. They are among the ﬁrst ones who wrote down the explicit reaction schemes and rate laws for protein
self-assembling, i.e. once formed by nucleation processes (which will be discussed in next section), actins will extend
or shrink by association or dissociation of monomeric units at one end mostly. They further veriﬁed that the initial
rate of actin growth varies linearly with the monomer concentration, which implies that monomeric, rather than
oligomeric, subunits have been added to actin ﬁlaments and make them to grow [43], since the latter will give rise to
a nonlinear dependence on the monomer concentration.
The linear dependence of elongation rate on the monomer concentration has been further investigated by Collins
et al. through a combination of kinetic modeling and single-molecule ﬂuorescence measurements on the NM domain
of yeast prion protein Sup35 [44]. Again, the initial rate of ﬁber growth was found to be directly proportional to the


## Page 18


18
nk 
nk 
ek 
ek 
ek 
ek 
ak 
ak 
ck 
&RQIRUPDWLRQDOFRQYHUVLRQ
3UHFRQYHUVLRQ
2QSDWKZD\
FRQYHUVLRQ
2IISDWKZD\
FRQYHUVLRQ
ck 
ck 
1XFOHDWLRQ
k 
k 
fk 
fk 
3ULPDU\
QXFOHDWLRQ
6HFRQGDU\
QXFOHDWLRQ
(ORQJDWLRQ
0RQRPHU
LQGHSHQGHQW
0RQRPHU
GHSHQGHQW
*URZWK
6DWXUDWLRQ
$PRUSKRXV
DJJUHJDWLRQ
6DWXUDWHG
HORQJDWLRQ
6DWXUDWHG
VHFRQGDU\QXFOHDWLRQ

ck 
ak 
ak 
ek 
ek 
ek 
ek 
FIG. 8: A cartoon depicting various microscopic mechanisms of amyloid ﬁbrillation discussed in the current paper.
concentration of soluble NM over a range of 0 ∼1µM. However, at a higher NM concentration (> 10µM), the rate of
ﬁber growth shows a weaker-than-linear law. The reason for this is believed to be “a conformational rearrangement of
NM after binding to ﬁber ends becomes rate limiting at high NM concentration” [44], a speciﬁc case of the saturation


## Page 19


19
phenomenon. A quantitative treatment will be presented in the section of saturation.
Recently, Knowles and his colleagues developed a novel technique to measure the rate of ﬁber elongation directly
[46, 47], which to some extent avoids the indistinguishability of several diﬀerent ﬁbrillation processes presented simul-
taneously in traditional methods. According to their setup, prepared fragments of amyloid ﬁbrils have been attached
to the surface of a quartz transducer. So that, once new monomers add to the ﬁbrils, the resulting nanogram mass
changes will be monitored through a shift in the resonance frequency of the quartz oscillator. Again, two diﬀerent
regimes in the ﬁber elongation rate are highlighted: an initial linear dependence on the monomer concentration, and
a subsequent saturation of the growth rate at high monomer concentrations.
In literature, the possibility of ﬁber elongation through oligomer addition has been discussed from time to time [48–
51]. For example, Serio et al. proposed a oligomer-based mechanism called “Nucleated Conformational Conversion”
[48], in which “structurally ﬂuid oligomeric complexes appear to be crucial intermediates in de novo amyloid nucleus
formation” and “rapid assembly ensues when these complexes conformationally convert upon association with nuclei”,
to explain the assembling of prion protein Sup35. However, since in general “monomer addition is more rapid and
eﬃcient” than oligomer addition [44], nowadays a common conclusion has been reached that ﬁber elongation has
a ﬁrst-order concentration dependence on both monomeric and ﬁbril species, revealing a bimolecular mechanism of
growth through monomer addition to both ends of existing ﬁbrils.
Now we are going to formulate above discussions into a quantitative model.
If only the elongation process is
included, it is straightforward to show that the mass concentration and number concentration of aggregates (see their
mathematical deﬁnitions and physical meanings in section of how to quantify ﬁbrillation kinetics) evolve according to
following equations:
d
dtP = 0,
(25)
d
dtM = k+
e mP −k−
e P,
(26)
where k+
e and k−
e denote the reaction rate constants for monomer association and dissociation respectively. Clearly,
the ﬁrst term on the right-hand side of (26) represents the desired process of ﬁber elongation by monomer addition
at ﬁbril ends (here the geometrical factor 2 is not directly written out); while the second one is the corresponding
inverse process, whose necessity lies on “the maintenance of monomer pool” in the equilibrium state [52].
It is noted that, according to (25), the number concentration is conserved, i.e. P(t) = P(0). This is a signiﬁcant
feature of elongation, in contrast to all kinds of nucleation processes which will be introduced in the following section.
Towards the mass concentration, obviously its growth rate is maximal at the beginning of the reaction and then


## Page 20


20
decreases monotonically. Actually, we have
M(t) = (M0 −ϵ)e−κt + ϵ,
(27)
where κ = k+
e P0, ϵ = mtot −k−
e /k+
e , M(0) = M0 and P(0) = P0 are the initial mass and number concentrations
of aggregates. Accordingly, the half-time and apparent ﬁber growth rate (see section on how to quantify ﬁbrillation
kinetics for their deﬁnitions) are given by
t1/2 = ln 2
κ
∝P −1
0
,
(28)
kapp = ϵ + M0
2mtot
κ ∝P0.
(29)
Here, both t1/2 and kapp are only concerned with the number concentration of seeds P0 rather than the mass con-
centration M0. This is another signiﬁcant feature of the elongation process. Contrarily, as we will show, the speed
of secondary nucleation generally depends on the mass concentration of seeds M0; while that of primary nucleation
does not rely on seeds at all. Finally, from the static solution M(∞) = ϵ, we can exactly see that the inverse reac-
tion – monomer dissociation is essential to maintain a genuine thermodynamic equilibrium as well as an observable
“monomer pool” at the end of reaction [52].
In (26), the rate constants for monomer association and dissociation are assumed to be independent of ﬁbril length.
An indirect support comes from the argument that they are “characterized by the local interaction of a monomer
with the end of a ﬁbril”, so that “the total length of the ﬁbril is likely to introduce only a minor eﬀect through
the reduction of the diﬀusive encounter rate when the size of the ﬁbril increases” [47]. Under the assumption of
ﬁbril length independence, there are plenty of studies attempting to determine exact values of the rate constants for
monomer association and dissociation. For example, by AFM analysis Collins et al. reported the rate constant for
ﬁber elongation of yeast prion protein Sup35 is approximately k+
e ≈2 × 105M −1s−1 at a soluble NM concentration
of 2.5µM and can be two times bigger at higher concentrations [44]. Knowles et al. found an elongation rate of
(9.2 ± 0.3) × 103M −1s−1 for insulin at a concentration of 0.17mM by quartz crystal microbalance, equivalent to one
molecule attaching every 3.1±1.2s on average [46, 53]. At 2.5mg/ml Aβ25−35 peptide, Kellermayer et al. determined
k+
e ≈106M −1s−1 and k−
e ≈10s−1 through scanning-force kymograph, given the equilibrium monomer concentration
to be 10µM [54]. In a similar way, referring to a critical concentration of α-synuclein at 2µM, Pinotsi et al. [55] gave
an average growth rate of k+
e ≈(1 ± 0.375) × 103M −1s−1 as well as a lower bound for the average dissociation rate
k−
e ≈(2.0 ± 0.8) × 10−3s−1 by two-color single-molecule localization microscopy.
From above far-from-complete list, we can clearly see that the rate constant for ﬁber elongation varies for at least


## Page 21


21
three orders of magnitude from protein to protein and could also be inﬂuenced by the pH condition, salt concentration,
temperature and etc. [55]. This fact to some extent reveals the intrinsic high complexity and heterogeneity of ﬁber
elongation processes. Actually, for the growth of individual ﬁlament, an intermittent, stop-and-go behavior has been
widely conﬁrmed [56, 57], which shows ﬁber elongation operates “in a way analogous to the landscape models of
protein folding deﬁned by stochastic dynamics on a characteristic energy surface” [27, 47]. Therefore, the current
single-reaction-rate-based picture turns out to be a rough average of various underlying stochastic processes concerning
with the ﬁber growth. Readers should be aware of this point.
B.
How ﬁbrils replicate
Generally speaking, the ﬁbrillation of amyloid proteins is constituted by two aspects: nucleation and growth. In
the previous section, we have shown how elongation provides a simple way to let ﬁbrils grow. But we still lack a
knowledge on where those templates (or seeds) for elongation come from and how they evolve during the ﬁbrillation
procedure. As far as we know, there are at least three basic processes contributing to the generation of new seeds, i.e.
primary nucleation, surface-catalysed secondary nucleation and fragmentation. There is a long story for the study of
primary nucleation in crystal and liquid formation. Surface-catalysed secondary nucleation and fragmentation present
two alternative ways to bypass the slow seeding procedure of primary nucleation by making use of existing ﬁbrils in
the system, so they are also named as “secondary nucleation” in literature. A major diﬀerence between them is that
the former dependents on the monomer concentration, while the latter does not.
Secondary nucleation plays a key role in the ﬁbrillation of amyloid proteins [6, 58]. In the presence of secondary
nucleation, the ﬁbrillation speed will be dramatically accelerated and time courses for ﬁber mass concentration will be
changed into a sigmoidal shape with prominent lag phase. Furthermore, in contrast to primary nucleation and surface-
catalysed secondary nucleation, fragmentation will not only cause a global change of the ﬁber length distribution, but
also largely enhance the cytotoxicity by generating more harmful oligomers. Detailed discussions could be found in
following sections correspondingly.
1.
Primary nucleation: rate-limiting step
For diﬀerent amyloid proteins under diﬀerent conditions, time courses for ﬁbrillation may vary considerably from
each other, but in general a sigmoidal-like behavior with a prominent lag phase is observed if initial proteins are all in


## Page 22


22
monomeric form [59]. Furthermore, by introducing certain amount of pre-seeded ﬁlaments into the system at the very
beginning of the reaction, the lag phase can be completely removed [5]. This evidence reveals that amyloid ﬁbrillation
involves a process called primary nucleation, in which nuclei of aggregates are formed from monomeric proteins directly.
In contrast, the formation of amorphous aggregates, which often acts as competitive pathways against regular amyloid
ﬁbrils, is generally believed to follow a non-nucleated polymerization (or random polymerization) [60–62].
The idea of primary nucleation has been extensively explored in various natural phenomena, such as the formation
of snow ﬂakes, clouds and bubbles, the crystallization of mineral, metal, protein and DNA, etc. [63–69]. It is the
ﬁrst step in the formation of either a new thermodynamic phase or a new structure via self-assembly, and typically
determines how long we have to wait before the new phase or self-organised structure appears. According to whether
the process is catalyzed by particles of foreign substance (like surface and substrate) or not, primary nucleation could
be further divided into two categories: homogeneous nucleation and heterogeneous nucleation. The latter usually
occurs much more often and faster than the former. This behavior could be understood by classical nucleation theory
(CNT), which predicts the nucleation rate [70–72]
R = NSZje
−∆G∗
kBT

,
(30)
where ∆G∗is the free energy barrier for forming a critical nucleus, which will be explicitly deﬁned later.
kBT
represents the thermal energy with the Boltzmann constant kB and the absolute temperature T. NS is the number
of nucleation sites. j is the rate for monomers attaching to the nucleus. Z is called the Zeldovich factor, which is the
forward probability for a critical nucleus to grow diﬀusively into a larger nucleus rather than shrink back to nothing.
To further model the free energy barrier, CNT treats the microscopic nucleus as a macroscopic droplet, so that the
free energy ∆G for forming a nucleus can be generally written as the sum of a bulk term proportional to the volume
of the nucleus and a surface term proportional to its surface area. Especially for homogeneous nucleation, the nucleus
modeled by a sphere of radius r gives [70–72]
∆G = 4
3πr3∆g + 4πr2σ.
(31)
The ﬁrst term stands for the volume contribution, in which ∆g is the free energy diﬀerence per unit volume between
the nucleated and non-nucleated phases and usually negative. The second term comes from the interface between the
nucleus and its surroundings. σ is the surface tension and always positive. As a consequence, for small r, the surface
term dominates and ∆G(r) > 0; while for large r, the volume term dominates and ∆G(r) < 0. Especially at some
intermediate value of r, the free energy goes through a maximum, corresponding to a least probability for nucleus


## Page 23


23
occurring. This is called the critical nucleus and occurs at dG/dr = 0, which gives a critical nucleus radius
r∗= −2σ
∆g .
(32)
Adding new monomers to nuclei larger than this critical radius decreases the free energy, so the overall nucleation rate
is then limited by the probability of forming the critical nucleus, which is ∆G∗= 16πσ3/[3(∆g)2]. This is exactly the
free energy barrier needed in the CNT expression for the nucleation rate R above.
The reason for heterogeneous nucleation occurring much easier than homogeneous nucleation is that the nucleation
barrier ∆G∗is much lower at a surface.
For homogeneous nucleation, the nucleus is approximated by a sphere.
However, for heterogeneous nucleation, when a nucleus is formed at the surface, its form is not completely spherical
and depends on the contact angle [73, 74]. This geometrical factor reduces the interfacial area and so the interfacial
free energy, which in turn reduces the nucleation barrier. In principle, we expect nucleation to be fastest when the
nucleus forms a small contact angle on its surface. However, detailed calculation is not straightforward and will not
be listed here.
From the kinetic aspect, primary nucleation, including both both homogeneous and heterogeneous nucleation, is
often modelled with the following formula [33, 75]
dP
dt = kn(m −m∗
F )nc,
(33)
where kn is the macroscopic reaction rate constant. With respect to the microscopic nucleation rate R considered
in above thermodynamic picture, we expect limV →∞R/Ns = kn in the limit of suﬃciently large volume. m∗
F is the
critical ﬁbrillar concentration and (m−m∗
F ) is also known as supersaturation. Supersaturation is the driving force for
both the initial nucleation step and the following growth, both of which could not occur in saturated or undersaturated
conditions. nc stands for the critical nucleus size, that can be as large as 10, but generally ranges between 2 and 4.
In the 1960s, Oosawa et al. borrowed this idea to study of the polymerisation of actin [43, 76] and wrote down
a reaction scheme consisting of three basic process – primary nucleation, monomer association and dissociation.
However, they did not include the supersaturation eﬀect explicitly, since mostly the protein concentration used for
ﬁbrillation is much higher than that required for saturation. According to Oosawa’s model, the number concentration
and mass concentration of aggregates evolve according to
d
dtP = knmnc,
(34)
d
dtM = k+
e mP−k−
e P + ncknmnc.
(35)


## Page 24


24
In above model, the inverse process for primary nucleation has been omitted. A major reason is that it is accounted
by a boundary term k−
n [Anc] (where k−
n is the rate constant and [Anc] is the concentration of critical nucleus), not
compatible with other terms constituted by moments M and P (the moment-closure method we introduced in the
section of how to coarse-grain model can systematically solve this problem). The last two terms underlying in (35) are
generally negligible too, due to the fact that under proper ﬁbrillation conditions, ﬁber elongation is more energetically
favorable and proceeds faster than primary nucleation and monomer dissociation [43]. This leads to an important
conclusion – the major role of primary nucleation in ﬁbrillation is to generate new seeds rather than directly consuming
free monomers like elongation. Similar argument also applies to secondary nucleation introduced in the next section.
Typical amyloid systems, which follow above mechanism without referring to secondary nucleation, include actins in
KCl solvents [77] (see Fig. 9A), γC-crystallin [78] and Apo C-II [79] etc.
According to [80], Oosawa’s model admits analytical solutions as follows
M(t) = mtot −(mtot −M0)

µsech
 ν + λβµt
2/nc,
(36)
P(t) = P0 + kn(mtot −M0)ncµ(βλ)−1
tanh(ν + βλµt) −tanh(ν)

,
(37)
where λ =
q
knk+
e (mtot −M0)nc, β =
p
nc/2, γ = βk+
e P0/λ, µ =
p
1 + γ2 and ν = arcsinh(γ). mtot, M(0) = M0
and P(0) = P0 are the total protein concentration, initial mass and number concentrations of aggregates respectively.
Especially, in the absence of initial seeds M0 = P0 = 0, we have M(t) = mtot[1 −sech2/nc(λβt)], which recovers the
classical Oosawa’s result [76].
Insight into the early time behaviour of ﬁber mass concentration can be obtained by expanding (36) around t = 0
M(t) = M0 + k+
e P0(mtot −M0)t + 1
2(mtot −M0)[λ2 −(k+
e P0)2]t2 + O(t3),
t →0.
(38)
This expression recovers the characteristic t2 dependence relating to the primary nucleation in Oosawa’s theory [76].
An additional term linear in time is raised by the growth of pre-added seeds. This diﬀerence actually provides a
simple way to distinguish the seeding contributions from primary nucleation and pre-added seeds.
After some calculation, the half-time and the apparent ﬁber growth rate are given respectively as
t1/2 =
1
λβµ

arccosh(2nc/2µ) −ν

,
(39)
kapp = λβµ
nc
mtot + M0
mtot
p
2ncµ2 −1.
(40)
According to above integrated rate laws, we can easily see that, in the absence of initial seeds M0 = P0 = 0, the
half time of ﬁbrillation is proportional to λ−1, which means t1/2 ∝m−nc/2
tot
, a prominent feature of seeding through


## Page 25


25
primary nucleation; on the contrary, if high concentrations of preformed seeds are added to the system, γ ≫1 and
we recover results for pure elongation t1/2 ∝(k+
e P0)−1.
Again, we can take advantage of this diﬀerence in scaling relations to separate the elongation process from primary
nucleation. At ﬁrst, without any initial seeds, the critical nucleus size for primary nucleation nc could be directly read
out by examining the scaling dependence of half-time under diﬀerent initial monomer concentrations. Furthermore,
parameter λ provides a combined knowledge of both primary nucleation and elongation. Finally, by adding high
concentrations of performed seeds into the system, seeding through primary nucleation will be completely suppressed
and the elongation rate could be extracted from the ﬁbrillation kinetics solely. Similar argument is also applicable to
secondary nucleation.
0
2
4
6
8
10
0
5
10
15
20
25
t(h)
M(μ M)
A
0
2
4
6
8
0
5
10
15
20
25
t(h)
M(μ M)
B
FIG. 9: Actin growth in the presence of KCl v.s. MgCl2, which highlights two diﬀerent dominated mechanisms [81]. (A)
Action samples were prepared with 40 mM KCl at monomer concentrations mtot = 7.4, 9.6, 12.4, 14.2, 16.2, 18.4, and 20.5 µM
separately (blue circles). Predictions based on the NE model (red dashed lines) in (34) and (35) were performed with nc = 4,
kn = 3×109M −3s−1, k+
e = 9×102M −1s−1, k−
e = 10−3s−1. (B) Action samples were prepared with 0.6 mM MgCl2 and 0.5 mM
EGTA at monomer concentrations mtot = 6.7, 8.5, 11.5, 14.9, 17.3, 20.3, and 22.9 µM. Predictions based on the NEF model
in (47) and (48) were performed with nc = 6, kn = 2 × 1016M −5s−1, k+
e = 9 × 104M −1s−1, k−
e = 0.18s−1, k+
f = 6 × 10−7s−1,
k−
f = 0.
2.
Monomer-dependent secondary nucleation: self-catalysed process
As indicated by the early time expansion of solutions for primary nucleation, a linear growth in the presence of
initial seeds and a growth depending on t2 for purely monomeric proteins are expected [82], which cannot account
for the apparent high cooperativity of ﬁbrillation observed in many amyloid systems. For example, in 1980 Ferrone


## Page 26


26
et al.
[83] observed an exponential growth at the early stage of aggregation for the aberrant gelation of sickle-
hemoglobin. Later, they studied the kinetics of polymerization of hemoglobin S and found a transition time much
shorter than the lag phase predicted by primary nucleation only [84, 85]. Miranker et al. observed a similar process
in Islet amyloid polypeptide (IAPP) [86]. Intriguingly, they found that both the reaction order and the activation
enthalpy of two nucleation processes are identical, which made them to conclude that both primary nucleation and
monomer-dependent secondary nucleation are “alternative manifestations of the same, surface-catalyzed nucleation
event” [87]. Above observations conﬁrmed the existence of a secondary pathway for nucleation, which generates new
nuclei by making use of the surface of existing aggregates in the system. Therefore, this kind of mechanism is called
surface-catalysed secondary nucleation. Since it depends on both monomer concentration and ﬁber concentration, it
is also known as monomer-dependent secondary nucleation, in contrast to a diﬀerent kind of secondary nucleation
mechanism – fragmentation that is monomer independent. Just as Miranker claimed, monomer-dependent secondary
nucleation is a special kind of heterogeneous nucleation and takes the surface of amyloid ﬁbrils as catalyst. Therefore,
it proceeds much faster than primary nucleation and exhibits an exponential growth due to the self-catalysed nature.
Besides sickle-hemoglobin[83], hemoglobin S [84, 85] and IAPP [87], Aβ40 [88] and Aβ42 [89, 90] (See Fig. 10) have
also been revealed to adopt the surface-catalyzed secondary nucleation mechanism.
A model, incorporating both primary nucleation and monomer-dependent secondary nucleation, could be expressed
as
d
dtP = knmnc + k2mn2M,
(41)
d
dtM = k+
e mP −k−
e P+ncknmnc + n2k2mn2M,
(42)
where the new term k2mn2M accounts for the contribution of secondary nucleation on seeding, which is proportional
to the surface area of existing aggregates (scale as M). The parameter n2 stands for the critical nucleus size for
secondary nucleation, analogous to nc for primary nucleation. It is noted that when n2 = 0, above equations oﬀers a
good approximation to the model of fragmentation, an alternative secondary nucleation mechanism going to be shown
in the next section. Therefore, we can use the same model to describe both monomer dependent and independent
secondary nucleations by just tuning the parameter n2. As we have stated in the section of primary nucleation that
the major role of various nucleation processes is to create new sites for elongation rather than increasing the mass of
aggregates directly, the terms underlying in (42) could be neglected with respect to elongation.
Under this condition, ﬁrst-order self-iterative solutions have been obtained through ﬁxed-point analysis [91] by


## Page 27


27
Cohen et al. [92] as
M(t) = M(∞) −[M(∞) −M0]e−k∞t
B−+ C+eκt
B+ + C+eκt · B+ + C+
B−+ C+
k2
∞/(κ¯k∞)
,
(43)
P(t) =
Pl(t)
1 + Pl(t)/P(∞),
(44)
in which Pl(t) = (C+κeκt + C−κe−κt)/k+
e is the linearized solution for early time.
κ =
q
(k+
e m0 −k−
e )k2mn2
0 ,
λ
=
q
k+
e knmnc
0 ,
C±
=
k+
e P0/(2κ) ± k+
e M0/[2(m0k+
e
−k−
e )] ± λ2/(2κ2),
k∞
=
k+
e P(∞),
¯k∞
=
p
k2∞−4C+C−κ2, B± = (k∞± ¯k∞)/(2κ).
M(0) = M0, P(0) = P0 and M(∞) = mtot −k−
e /k+
e , P(∞) =
(k+
e )−1
q
2κ2/[n2(n2 + 1)] + 2λ2/nc + 2M0κ2/(ncm0) + (k+
e P0)2 are the aggregates number concentration and mass
concentration at the beginning and in the equilibrium respectively. m(0) = m0 = mtot −M0 and mtot are the initial
and total monomer concentrations. Alternative solutions for early time based on perturbation methods could be found
in [85, 93] and we will not go into them here.
According to self-iterative solutions, the half-time and apparent ﬁber growth rate can be extracted,
t1/2 ≈κ−1 ln(1/C+),
(45)
kapp ≈κ
2
k2
∞/(κ¯k∞)
B+ + 1
.
(46)
It is clear, in the absence of initial seeds M0 = P0 = 0, the half time of ﬁbrillation is around 2κ−1 ln(κ/λ), which
means t1/2 ∝m−(n2+1)/2
tot
, a feature of seeding through secondary nucleation. As primary nucleation only enters into
the half-time through a logarithmic correction, its inﬂuence will be limited to early time, which is expectable since
secondary nucleation is more eﬀective in generating seeds. Furthermore, even if medium amount of preformed seeds
are introduced to the system λ ≪k+
e P0 ≪κ, the scaling dependence of half-time on monomer concentration will not
be changed except for a logarithmic correction, showing only primary nucleation is screened out in this step. Unless
high concentrations of preformed seeds are added k+
e P0 ≫κ, we can not eliminate the eﬀect of secondary nucleation
and recover the result for pure elongation t1/2 ∝(k+
e P0)−1.
Since the major role of primary nucleation and secondary nucleation is to generate new seeds, it is generally
expected, by introducing preformed seeded into the system, various nucleation mechanisms could be partially or even
completely screened out. The examination above conﬁrms this point from an analytical point. In particular, we see
that ﬁrstly primary nucleation and then secondary nucleation are suppressed with an increase of seeds concentration.
As long as two nucleation processes are well separated in time, given by
p
k+
e knmnc
tot ≪
q
k+
e k2mn2+1
tot
, rates of
primary nucleation, secondary nucleation and elongation could be extracted respectively by simply varying the seeds
concentration. In this way, the signiﬁcant role of seeds in ﬁbrillation kinetics could be fully appreciated. All these


## Page 28


28
discussions are applicable to the fragmentation case in the next section by just setting n2 = 0.
FIG. 10: Kinetics of A42 aggregation is shifted from surface catalyzed secondary nucleation dominated mechanism to frag-
mentation dominated by continuously increasing agitating speeds. The upper plots show the time proﬁle of A42 aggregation
under diﬀerent shear rates generated by agitating the sample under diﬀerent speeds; and the lower ones show the corre-
sponding power-law relationships between the half-time and the initial monomer concentration of A42.
In (A), the rate
parameters
p
k+
e kn = 42.4M −1s−1 and
p
k+
e k2 = 2.8 × 105M −3/2s−1, nc = n2 = 2 are ﬁxed and k+
f = k−
f = 0. In (B)-(F),
q
k+
e k+
f = 0.6, 0.9, 1.4, 1.9M −1/2s−1 are taken respectively under each shear rate in replace of
p
k+
e k2. Figure is taken from
[90] with copyright permission.
3.
Monomer-independent secondary nucleation: fragmentation and annealing
Another eﬃcient way to generate seeds without involving primary nucleation is fragmentation, which means one
ﬁlament breaks into two smaller fragments. In principle, breaking into three or more pieces simultaneously is also
possible but extremely rare. The universality of fragmentation in amyloid formation has long been established in the
famous book of Oosawa [43]. It is well-known that single ﬁlament becomes mechanically unstable and tends to break
when exceeding certain threshold in length [44, 58]. Even for bundled ﬁbrils, breakage is unavoidable in the presence
of mechanical stress [94], thermal motion [95–97], or chaperons like Hsp104 [98].
Compared to surface-catalysed secondary nucleation, fragmentation is monomer-independent and thus becomes
predominant under the condition of low monomer concentration. It can dramatically accelerate the formation of
breakable ﬁlaments and change time courses for mass concentration of aggregates into a sigmoidal like behavior.
Fragmentation could further alter the ﬁber length distribution globally just like elongation and enhance the toxicity
of ﬁbril samples by generating more harmful oligomers in low molecular weight. Due to its signiﬁcant roles in both
amyloid ﬁbrillation and cytotoxicity, fragmentation has been paid plenty of attention to in past studies. And many
typical amyloid systems have been shown to follow this mechanism, including actins in MgCl2 solvents [77] (see Fig.


## Page 29


29
9B), Sup35 NW region [44], Ure2p [99], CsgBtrunc [100], Steﬁn B [101], β2-microglobulin [102], WW domain [103],
α-synucleins [104] and insulin [105] etc.
Generally speaking, fragmentation rates are length-dependent. In literature, several assumptions have been pro-
posed, including the random scission, the central scission, and the Gaussian scission [106, 107] and modiﬁed par-
tially random scission [108] etc. The latter two got supports from ﬁberlike PI264-b-PFS48 micelles under sonica-
tion [109], thermodynamically induced shear degradation of polystyrene in semiconcentrated solutions [107], single-
stranded random-coiled poly-(uridylic acid), double-stranded helical DNA, and triple-stranded helical poly-(adenylic
acid)·2poly(inosinic acid) [108]. Hill suggested a formula in log form for polymer fragmentation and annealing based
on statistical mechanics [110]. And it has been applied by Hong et al. to the study of several amyloid proteins [111].
In the presence of ﬁber-length-dependent fragmentation, the derivation of self-closed models for ﬁber formation
becomes a big trouble. Based on Maximum Entropy Principle [112–114], a systematical and reliable way has been
proposed to derive close-formed mass-action equations from microscopic length-dependent fragmentation models [111]
(see section on how to coarse-grain model for details). In particular, under the assumption of totally random scission
(or length-independent fragmentation), the kinetics of ﬁber formation can be expressed by the following model:
d
dtP = knmnc + k+
f [M −(2nc −1)P] −k−
f P 2,
(47)
d
dtM = k+
e mP −k−
e P+ncknmnc,
(48)
where k+
f is the rate constant for length-independent fragmentation, and k−
f is that for the inverse process – ﬁlaments
annealing. Terms for ﬁber fragmentation and annealing in (47) are explicit and can be obtained directly from the
microscopic model. Since here ﬁbrils are not allowed to break into monomers directly and so is annealing, no term for
fragmentation or annealing will enter into the equation for M(t). This is a dramatic feature of ﬁber fragmentation
and annealing, which only aﬀect the number concentration of aggregates and keep the mass concentration conserved.
As an inverse process of fragmentation, ﬁlaments annealing is crucial for the ﬁber length distribution, number
concentration of aggregates as well as their average length. Based on (47), it is clearly seen that in the absence of
annealing (by setting k−
f = 0), the average length of ﬁbrils will be around 2nc −1, in contrast to the estimated lower
bounds of at least hundreds of monomers.
Again, by ﬁxed-point analysis, self-iterative solutions could be derived in exactly the same form as those in (43) and
(44), except for some internal parameters have to be changed correspondingly [115], i.e. the linearized solution for early
time Pl(t) = C1ek1t + C2ek2t −nck+
f ϵ, number concentration of aggregates in equilibrium P(∞) = 2M(∞)
 2nc −
1 +
q
(2nc −1)2 + 4k−
f M0/k+
f
−1, κ =
q
(k+
e m0 −k−
e )k+
f , as well as C± = k+
e C1,2/k1,2, where k1,2 = −k−
f P0 ±


## Page 30


30
q
(k−
f P0)2 + κ2, C1,2 = (1 −k2,1/k1,2)−1[P0 −k2,1(M0 + knmnc
0 /κ2 + nck+
f k−
f P0ϵ/κ2)]. The same expressions for
the half-time and apparent ﬁber growth rate could be obtained as in (45) and (46) and will not be addressed here.
Just note in current case, except for a logarithmic correction, t1/2 ∝m−1/2
tot
and kapp ∝m1/2
tot , a special case of
monomer-dependent secondary nucleation with n2 = 0 for fragmentation as we claimed.
Models constituted by above four basic mechanisms: elongation, primary nucleation, surface-catalyzed secondary
nucleation and fragmentation (as well as monomer dissociation and ﬁlaments annealing as two typical inverse pro-
cesses) could already explain most ﬁbrillation kinetics observed in experiments. In the past several years, fruitful
results have been obtained in this direction [5, 6], which greatly enhance our understandings on the underlying mi-
croscopic processes, the kinetics and thermodynamics of amyloid ﬁbrillation, eﬀects of pH value, temperature and
etc. Besides this main framework, several key issues need to be addressed to provide a complete picture. Firstly, we
have mentioned that high monomer concentration could dramatically change the kinetics of amyloid formation, which
is known as saturation. Luckily, the eﬀect of saturation could be easily accounted through a Michaels-Menton-like
formula, though model analysis becomes far more diﬃcult. Secondly, it is well-known that the formation of amyloid
ﬁbrils is a direct consequence of protein misfolding, and the conformational conversion of monomers and oligomers
plays an inreplaceable role in it. However, the step of conformational conversion is easily neglected in kinetics due to
the interference of primary nucleation.
C.
How high concentration aﬀect
In the section of ﬁber growth, we have mentioned that ﬁber elongation shows a sub-linear dependence in the
regime of high monomer concentration. In fact, this phenomenon is rather universal and has a deep physical basis on
saturation. It is imaginable, in the presence of too many monomers competing for the same ﬁbril end at the same time,
the ﬁber end will appear to be “saturated” since the incorporation of each monomer requires certain amount of time
and can not be ﬁnished at once. As a consequence, the elongation process appears to be blind to the instantaneous
monomer concentration in the system and shows a weaker-than-linear dependence.
Physically, the process of saturated elongation could be modeled through a “dock-lock” mechanism [116, 117], which
includes two sub-steps – unspeciﬁc attachment and detachment of a monomer with the ﬁbril end, and subsequent
conformational change of the attached monomer to make the attachment speciﬁcally. Usually, the second process is
the rate-limiting step. For example, Scheibel et al. studied how nuclei mediate the conversion of soluble NM domain
of Sup35 to the amyloid form in the elongation phase of ﬁber formation [118]. By creating single-cysteine substitution


## Page 31


31
mutants at diﬀerent positions of NM domain to provide unique attachment sites for various probes, they estab-
lished that elongation is a two-step process involving the capture of an intermediate, followed by its conformational
conversion.
If we take Pbound and Pfree = P −Pbound as the number concentration of ﬁbril ends which has and has not monomers
unspeciﬁcally attached, the “dock-lock” mechanism is expressed through following equations
d
dtM = kcPbound,
(49)
d
dtPbound = k+
a mPfree −k−
a Pbound −kcPbound,
(50)
where k+
a , k−
a and kc represent reaction rate constants for monomer unspeciﬁc attachment, detachment and confor-
mational change at the ﬁbril end. It is clear that the three terms on the right-hand side of (50) account for the
contribution of each step mentioned in the “dock-lock” mechanism to ﬁbril ends respectively.
To eliminate the additional variable Pbound, we refer to the classical Quasi Stead-State Approximation [119, 120],
which assumes the generation and consumption of Pbound are always in a dynamical equilibrium. Such that we can
take the sum of terms on the right-hand side of (50) to be zero, i.e.
0 = k+
a mPfree −k−
a Pbound −kcPbound,
which gives solutions in a form of the famous Michaelis-Menten equation for enzyme kinetics [121],
Pfree = P

1 + m
Km
−1
,
Pbound = P m
Km

1 + m
Km
−1
.
Here the Michaelis constant Km = (k−
a + kc)/k+
a .
Inserting above formula into (49), a simpliﬁed model incorporating the process of saturated elongation is reached,
d
dtM = k+
e mP

1 + m
Km
−1
,
(51)
d
dtP = knmnc + k2mn2M,
(52)
in which the new rate constant for ﬁber elongation is deﬁned as k+
e
= kc/Km = kck+
a /(k−
a + kc).
Compared
to the formula in the section of ﬁber growth, a correction factor (1 + m/Km)−1 has been added. Therefore, by
introducing an “eﬀective” monomer concentration as m/(1 + m/Km), above model will recover the classical one
without saturation. Furthermore, if monomer concentration is much higher than the critical saturation concentration
(given by the Michaelis constant Km) m ≫Km, the eﬀective monomer concentration becomes a constant Km;


## Page 32


32
otherwise if the monomer concentration is much lower than the critical saturation concentration m ≪Km, the eﬀective
monomer concentration approaches to the real monomer concentration. In this way, both the linear dependence of
ﬁber elongation rate in the regime of low monomer concentration and sub-linear dependence in the high regime could
be explained by a uniﬁed picture based on saturated elongation. And the Michaelis constant Km serves as a key to
characterize the transition from linear to sub-linear (Fig. 11A and 11B).
The model for saturated elongation is far more diﬃcult to solve than the classical one without saturation. In the
absence of initial seeds, a suggested practical solution is (unpublished result)
M(t) = mtot

1 −

1 + 1
θy(1 + y)α/(1+α)
−θ
,
(53)
where y = ϵeκt/√1+α, α = mtot/Km, θ =
p
2/[n2(n2 + 1)] and κ =
q
k+
e k2mn2+1
tot
. A critical concentration of ﬁbrils
M(0)/mtot = ϵ = k+
n mnc−n2−1
tot
/(2k2) ≪1 has been introduced to seed the system, so that the resulting expression for
M(t) matches the leading order term for early time. In the special case of n2 = 0, which corresponds to fragmentation,
the solution reduces to
M(t) = mtot

1 −e

−y(1 + y)α/(1+α)

,
(54)
by exploiting the identity limb→∞(1 + a/b)b = ea. Meanwhile, we have
P(t) =
√
θ2 + αϑ2κ
2k+

1 −
 m
mtot
1/θ
,
(55)
where ϑ =
p
2/[(n2 + 1)(n2 + 2)]. Again, we need to pay attention to the case n2 = 0, which gives
P(t) = 1
2knmnc
tott + k2mtot
κ
ln
1 + y
1 + ϵ

.
(56)
Based on above solutions, we can roughly determine the half time and the apparent ﬁber growth rate as
t1/2 ∼ln(1/ϵ)
√
1 + α/κ,
(57)
kapp ∼κ/
√
1 + α.
(58)
It is easily seen that t1/2 ∝m−(n2+1)/2
tot
in the regime of low monomer concentrations mtot ≪Km and t1/2 ∝m−n2/2
tot
in the regime of high monomer concentrations mtot ≫Km. Especially, when n2 = 0 and mtot ≫Km, we have
t1/2 ∝ln(1/mtot), which well explains the observed sub-linear dependence of ﬁber elongation under the condition of
high monomer concentrations.
In principle, all monomer-dependent processes may get saturated once the monomer concentration exceeds certain
threshold. And large amyloid proteins are more prone to get saturated than smaller ones under the same condition,


## Page 33


33
FIG. 11: (A)-(B): Saturation of elongation rate for α-synuclein under diﬀerent concentrations of soluble proteins and a constant
3.5µM seeds. Images are taken from [122]. (C)-(D): Saturation of surface catalyzed secondary nucleation for Aβ40 under various
monomer concentrations without initial seeds. Data ﬁtting was performed according to (59) and (60) with k+
e = 6×105M −1s−1,
kn = 2 × 10−6M −1s−1, k2 = 3 × 103M −2s−1, Ks = 6 × 10−6M, nc = n2 = 2. Images are taken from [88] with copyright
permission.
since the former generally requires a longer time to ﬁt itself to the ﬁbrillar structure. In view of saturation, the
model for surface catalyzed secondary nucleation (41) requires to be modiﬁed too (see Fig. 11C and 11D). Following
a similar “dock-lock” mechanism as well as derivations for saturated elongation, saturated secondary nucleation could
be formulated as
d
dtP = knmnc + k2
mn2
1 + (m/Ks)n2 M,
(59)
d
dtM = k+
e mP,
(60)
where Ks is the critical saturation concentration for secondary nucleation. Again, if monomer concentration is much
lower than the critical saturation concentration m ≪Ks, we will recover the classical model without saturation;
contrarily, if monomer concentration is much higher m ≫Ks, only a constant concentration of monomers Ks could
contribute to secondary nucleation due to saturation.
Self-iterative solutions in a similar form of (43) and (44) could be derived for above model through ﬁxed-point
analysis. Interested readers may refer to [88] for details. Basically, everything is the same except k2 is replaced by
k2/[1 + (mtot/Ks)n2]. Of particular interest is the scaling behavior of half-time, which are solved within logarithmic
corrections as t1/2 ≈κ−1 ln(1/C+), where κ =
q
k+
e k2mn2+1
0
/[1 + (m0/Ks)n2], C+ = k+
e P0/(2κ) + k+
e M0/(2m0k+
e ) +
λ2/(2κ2), λ =
q
k+
e knmnc
0 . And m(0) = m0, P(0) = P0, M(0) = M0 are the monomer concentration, number and
mass concentration of seeds at the start of reaction respectively. Thus, in the presence of high monomer concentration
m0 ≫Ks, we have t1/2 ∝m−1/2
tot
, similar as that for the model of fragmentation; while in the regime of low monomer
concentration m0 ≪Ks, the half-time t1/2 ∝m−(n2+1)/2
tot
, which recovers the unsaturated case as expected. The
model combined both saturated elongation and saturated secondary nucleation is similar and will not be shown here.


## Page 34


34
D.
How to incorporate diﬀerent conformations
It is well-known that the formation of amyloid ﬁbrils is a direct consequence of the misfolding of amyloid proteins
[1, 123].
As an example, in one of the most well studied amyloid systems – prion, Prusiner identiﬁed that the
conformational conversion of prion protein from PrP to PrPsc gives rise to the famous mad cow disease and scrapie
in sheep [124]. In human, prion causes Creutzfeldt-Jakob disease (CJD) and kuru. According to the molecular size,
conformational conversion could be divided into either monomer conversion or oligomer conversion. While based on
the position where the conformational conversion happens inside the whole ﬁbrillation procedure, it can be classiﬁed
into pre-, on-pathway and oﬀ-pathway conversion separately.
Among them, pre-conversion is a prerequisite for primary nucleation, elongation and surface catalyzed secondary
nucleation. It is directly related to monomer conversion and means the conformation of monomers has to be adjusted
in order to be incorporated into ﬁbrillar structures [125, 126]. The kinetic modeling of conformational pre-conversion
is most straightforward. All terms concerning instantaneous monomer concentration m(t) in previous models should
be replaced by a new concentration of monomers in the unfolded (or partially unfolded) state mu(t) as required by
the ﬁbrillar structure [127].
mu(t) =
Z t
0
k+
c m(τ)e−(k+
c +k−
c )(t−τ)dτ + mu(0)e−(k+
c +k−
c )t,
(61)
is the solution of
dmu
dt
= k+
c (m −mu) −k−
c mu,
(62)
where k+
c and k−
c are the forward and backward reaction rate constants for protein conversion between the folded
and unfolded states. In practice, the eﬀect of conformational pre-conversion is easily neglected due to the existence
of other rate-limiting steps, like primary nucleation.
This fact is fully appreciated based on following argument.
If conformational conversion of monomers is faster than ﬁber growth rate, which is generally limited by primary
nucleation, we could assume monomers in the folded and unfolded states are in dynamic equilibrium and apply QSSA
approximation to obtain k+
c (m −mu) −k−
c mu = 0. By redeﬁning ˜kn = [k+
c /(k+
c + k−
c )]nckn, ˜k+
e = [k+
c /(k+
c + k−
c )]k+
e ,
˜k2 = [k+
c /(k+
c + k−
c )]n2k2, the model in (41) and (42) is recovered without including conformational pre-conversion
explicitly.
In contrast to pre-conversion, objects of on-pathway and oﬀ-pathway conversion are both oligomers. Their main
diﬀerence lies on whether conformational conversion is necessary for ﬁbril generation or not.
In the on-pathway
conversion, oligomers need to take some rearrangements in structure, for example repacking from globular oligomeric


## Page 35


35
conformation to linear ﬁbril-like conformation, before growing into mature ﬁbrils; while in the oﬀ-pathway conversion,
conformational conversion of oligomers will leads to amorphous aggregates in competition with ﬁbrillar aggregates.
The kinetic modeling of on-pathway and oﬀ-pathway conversions is far more diﬃcult than pre-conversion, due to the
conformational variety of oligomers, complicated interactions between oligomers, ﬁbrils and amorphous aggregates
etc. Preliminary results for on-pathway conversion leading to ﬁbrillary aggregates in transthyretin(TTR) [128], tau
proteins [129], insulin stabilized by Zn2+ [130] etc., and oﬀ-pathway conversion leading to the formation of amorphous
aggregates [60–62] could be found in literature. But details will be omitted with a pity.
Besides those well-formulated mechanisms discussed in current paper, there are still many processes, which play an
important role in changing the morphology of ﬁbrils, aﬀecting ﬁbril thermodynamic stability, modifying ﬁbrillation
kinetic proﬁles etc., worthy of exploring. For instance, Anderson et al. observed glucagon ﬁbrils are able to generate
new ﬁbril ends by continuously branching, which prefers an angle of 35o −40o along the forward direction of parent
ﬁbril and never occurs at the tip [131]. Murphy et al. further included lateral aggregation of ﬁlaments into ﬁbrils
to build up a complete description of Aβ ﬁbrillation [132].
Most importantly, in vivo conditions are completely
diﬀerent from that in vitro [133, 134]. Not only the cellular crowding environment [135, 136], but also synthesis
[137], degradation [138] and transportation [139, 140] of amyloid proteins may exert a great impact on the ﬁbrillation
kinetics. However, currently we still lack a quantitative characterization for most of them. These interesting topics
have to be left to the future with regrets.
E.
How cytotoxicity arise
After looking into so many ﬁbrillation mechanisms, we still have no idea about the most important issue, i.e. how
the aggregation of misfolded amyloid proteins aﬀects normal cell function and gives rise to amyloidosis? To answer
this question, we ﬁrst need to make sure which species of aggregates is responsible for cytotoxicity. For quite a long
time, mature ﬁbrils have been taken for granted as the major cause of cell damage [2]. However, this view has been
challenged again and again in recent years, with accumulated evidences coming from the morphology, atomic structure
and functions of oligomers and ﬁbrils both in vitro and in vivo [141, 142]. Now heterogeneous oligomers are generally
believed far more toxic than mature ﬁbrils [143–145]. Meanwhile, solvable monomers are considered as less harmful
to cells even in a misfolded state [146, 147].
In literature, several mechanisms have been proposed for the molecular basis of cytotoxicity caused by oligomeric
species. Most arguments are based on the interaction between oligomers and lipid membrane. It is generally believed


## Page 36


36
0
1
2
3
4
M/mtot
0
0.2
0.4
0.6
0.8
1.0
1.2
(A) Primary nucleation rate kn
+
t(h)
0
0.1
0.2
P(μ M)
10-5
10-3
10-1
101
0
1
2
3
4
0
0.2
0.4
0.6
0.8
1.0
1.2
(B) Elongation rate ke
+
t(h)
0
1
2
0
0.5
1
1.5
0
1
2
3
4
0
0.2
0.4
0.6
0.8
1.0
1.2
(C) Elongation rate ke
-
t(h)
0
1
2
0
0.2
0.4
0.6
0.8
0
1
2
3
4
0
0.2
0.4
0.6
0.8
1.0
1.2
(D) surface-catalyzed 
secondary nucleation rate k2 
t(h)
0
1
2
3
4
0
0.1
0.2
0.3
0.4
kn
+
ke
+
ke
+
ke
+
kn
+
kn
+
ke
-
ke
-
ke
+
kn
+
k2
k2
ke
-
k2
k2
ke
-
0
2
4
6
8
M/mtot
0
0.2
0.4
0.6
0.8
1.0
(E) Fragmentation rate kf
+
t(h)
0
1
2
3
4
P(μ M)
10-5
10-4
10-3
10-2
10-1
0
2
4
6
8
0
0.2
0.4
0.6
0.8
1.0
(F) Fragmentation rate kf
-
t(h)
0
1
2
3
4
10-5
10-4
10-3
10-2
10-1
0
5
10
15
20
0
0.2
0.4
0.6
0.8
1.0
1.2
(G) Conversion rate kc
+
t(h)
0
1
2
3
4
0
0.1
0.2
0.3
0.4
0.5
0
5
10
15
20
0
0.2
0.4
0.6
0.8
1.0
1.2
(H) Conversion rate kc
-
t(h)
0
1
2
3
4
0
0.1
0.2
0.3
0.4
0.5
kf
+
kf
+
kf
+
kf
-
kf
-
kf
-
kf
+
kf
-
kc
+
kc
+
kc
+
kc
+
kc
-
kc
-
kc
-
kc
-
FIG. 12: Inﬂuence of rate constants on the ﬁbrillation kinetics. In (A-C), rates for primary nucleation, elongation and monomer
dissociation are changed with respect to those in Fig. 9A (mtot = 18.4µM) by one or two orders of magnitude higher or lower.
The base line is drawn in black. Lines in purple and red mean increasing the parameter, while lines in green and blue mean
decreasing. In (D-H), similar procedures are performed on rates for monomer-dependent secondary nucleation, fragmentation,
annealing and monomer conversion respectively. To be exact, parameters in (D) are taken according to those for the ﬁrst
subplot of Fig. 10 with mtot = 3.5µM; parameters for (E) and (F) are the same as Fig. 9B with mtot = 11.5µM; (G) and
(H) show a modiﬁed NE model by introducing an additional step of monomer conversion in (62). Besides k+
c = 0.01s( −1),
k−
c = 0.001s( −1), mtot = 18.4µM, other parameters are taken from Fig. 9A.
that the binding of oligomers could dramatically aﬀect the shape and permeability of lipid membrane [148, 149],
induce undesired pores or ion-channel-like structures [150, 151], and give rise to fatal abnormal ion leakage therefore
[152, 153]. For instance, Demuro et al. observed in Xenopus oocytes that Aβ(1-42) oligomers can lead to abnormal


## Page 37


37
Ca2+ ﬂux independent of ion-channel from 5 to 40 mer [154]. Schauerte et al. further pointed out that hexamer is the
smallest stable oligomer that can penetrate cell membrane, whereas 12 to 14-mers give rise to the largest ion current
[155]. By MD simulation, Jang et al. proposed that 16- to 24-mers of Aβ arrange into pore-like structures [156],
which are compatible with the pores observed by atomic force microscopy [157, 158]. Meanwhile, Shafrir et al. found
that Aβ pores is an assembly made up of six hexamers [159].
Alternative hypothesis based on cellular regulatory network suggests that in vivo the exposed ﬂexible hydrophobic
surfaces of oligomers can promote aberrant protein interactions, deregulate cytosolic stress response [160, 161], trigger
inﬂammatory responses, oxidative damage [162], alter kinase and phosphatase activities, increase neuroﬁbrillary
tangles [147, 163, 164], change synaptic plasticity [165–168] and so on.
Recently, Hong and his colleagues extended kinetic models for amyloid ﬁbrillation and included the cell damage
caused by oligomer formation too [169]. Four basic assumptions have been put forward as a general criterion for
modeling, i.e. (1) the basic procedure of amyloid formation is well formulated by kinetic models; (2) cell damage
is mainly caused by oligomers, rather than mature ﬁbrils or monomers, through their binding to lipid membrane;
(3) cytotoxicity is quantiﬁed through the amount of membrane-bounded oligomers (or leaked ion concentration in
original manuscript); (4) oligomer binding does not aﬀect the kinetics of amyloid formation. Or, in other words, the
consumption of oligomers during membrane binding could be neglected. The last assumption is generally unnecessary,
however mathematically it oﬀers a simple way to get rid of the feed-back inﬂuence of oligomer consumption during
membrane binding and keep previous well-formulated equations of ﬁbrillation kinetics unaﬀected.
Besides two equations for number concentration and mass concentration of aggregates P(t) and M(t), which char-
acterize the ﬁbrillation process under diﬀerence mechanisms in previous sections, the concentration of cells in diﬀerent
states, classiﬁed based on the number of membrane-bounded oligomers, evolves according to
d
dt[Cj] = Poli(t)
N−1
X
i=0
k+
b (i)[Ci] −
N
X
i=1
k−
b (i)[Ci],
j = 0, · · · , N
(63)
where [Ci] is the concentration of cells in state i, in which the lipid membrane has been bounded with i oligomers.
The current deﬁnition of cellular state is quite natural, since the condition of cell damage is positively correlated with
the amount of bounded oligomers according to assumption (3) above. The total cell concentration ctot = PN
i=0[Ci] is
a constant, in which N stands for the maximal number of oligomers allowed to be bounded to the same membrane.
k+
b (i) and k−
b (i) are rate constants for oligomer binding and unbinding, which potentially depend on the cellular
state. According to [170, 171], k+
b ∼(2 −5) × 105M −1s−1 and k−
b ∼5 −300s−1 on average. Poli(t) is the number
concentration of oligomers at time t and can be expressed as a function of M(t) and P(t) according to the moment-


## Page 38


38
closure method shown in section of how to coarse-grain model. However, it is still uncertain whether Moli (the mass
concentration of oligomers) or even more complicated functions are required to include those toxic species and their
relative damage to cells explicitly.
Especially, a simple two-state model including only normal and damaged cells is obtained when N = 1, based on
which the fraction of damaged cells is given by
[C1]/ctot =
Z t
0
k+
b Poli(τ)e

−
Z t
τ
[k+
b Poli(σ) −k−
b ]dσ

dτ.
(64)
Once the time course for Poli(t) is determined through the ﬁbrillation kinetics, a full knowledge about the progress
of cell damage caused by oligomers binding could be obtained. A similar approach by examining the leaked ion
concentration has been adopt by Hong et al. [169] and applied to β2m and IAPP ﬁbrils induced membrane leakage
with great success (see Fig. 13).
FIG. 13: hIAPP ﬁbril growth and hIAPP-induced membrane leakage: (A) ﬁbril mass concentration measured by ThT ﬂuores-
cence; (B) the amount of membrane leakage under diﬀerent initial protein concentration; (C) the half-time for ﬁbril formation
and membrane leakage; and (D) the amount of membrane leakage under diﬀerent concentrations of seeds. Image is taken
from [169] with copyright permission, but all ﬁttings are re-performed according to (63) with k+
n = 4 × 10−5M −1s−1, k+
e =
1.2×105M −1s−1, k−
e = 0s−1, k+
f = 7×10−5s−1, k−
f = 1×104M −1s−1, k+
b = 1.5×105M −1s−1, k−
b = 2.5×10−3s−1, n = 1, nc =
2, no = 40. Particularly, in (D) mtot = 2.5 × 10−5M, k+
b = 6 × 105M −1s−1, k−
b = 1 × 10−3s−1 and M(0)/P(0) = 400.
F.
How to manipulate ﬁbrillation
A central aim for examining various ﬁbrillation mechanisms is to manipulate the kinetics of amyloidosis. Based
on diﬀerent targets, there are basically two large groups of approaches to achieve this goal. The indirect approach
is to control the environment, in which amyloid ﬁbrillation takes place. Here the word “indirect” means we will not
manipulate amyloid proteins or ﬁbrils directly. Alternatively, by varying the temperature, pH value, salt concentration
etc., reaction rate constants for diﬀerent processes will be changed accordingly. As a result, we can either accelerate or


## Page 39


39
decelerate any given amyloid ﬁbrillation, as well as increase or decrease the population of any oligomeric and ﬁbrillar
species. To be concrete, by decreasing the elongation rate, monomers will be overpopulated; otherwise, the population
of mature ﬁbrils will be enlarged. To increase the population of oligomers is a bit complex, which requires increasing
the rate of primary nucleation and decreasing that of elongation at the same time.
According to the classical transition state theory (TST) for elementary chemical reactions, the rate constant for a
given process is determined by the Arrhenius equation [172, 173]
k = A exp[−Eact/(kBT)],
(65)
where A is referred to as the frequency factor, and E is regarded as the activation energy, which in principle is a
function of various experimental conditions, Eact = Eact(temperature, pH value, salt concentration etc.). Therefore,
if we know how the activation energy for various elementary ﬁbrillation processes relies on conditions quantitatively,
we can control the ﬁbrillation kinetics as well as the population of each species freely as we wish.
Although for many cases the indirect approach is quite useful, it suﬀers some intrinsic limitations, e.g. it is diﬃcult
to make a big change of some ﬁbrillation conditions in experiments; some conditions may play a complex role in
determining the reaction rate and no quantitative or qualitative description is available; in many cases, changing one
condition may aﬀect almost all processes at the same time, which makes it almost impossible to perform analysis.
The direct approach means to manipulate the concentration of each species directly. Varying the initial monomer
concentration and seeds concentration are two most popular and eﬀective methods in vitro, whose eﬀects on ﬁbril-
lation kinetics and species populations have been fully appreciated in previous sections. In vivo, directly adding or
removing monomers and seeds becomes less promising. Therefore, speciﬁc binding through antibodies and chaperons
is introduced to control the ﬁbrillation kinetics as well as species population.
Antibodies and chaperons are both well-known for their speciﬁcity in binding to certain molecular structures. In
principle, we can diminish any monomeric, oligomeric and ﬁbrillar species by introducing proper antibody or chaperon
into the system, which therefore allows us to manipulate each elementary ﬁbrillation process independently. For
example, nano-particles have been widely used in literature to inhibit amyloid ﬁbrillization, induce ﬁbril dissociation
and mitigate neurotoxicity [174–176]. Similarly, many chaperon molecules, like Hsp70 family members, are known
for their ability to inhibit and reverse the formation of amyloid aggregates [177–179]. Now, searching for various
promising antibodies and chaperons to inhibit amyloid ﬁbrillation, or to prevent and cure amyloidosis as a potential
goal, becomes very popular in this ﬁeld (see Fig. 14 as an exmaple). Though in many cases, the molecular basis for
why it works has not yet been clariﬁed.


## Page 40


40
To mathematically probing various potential binding eﬀects of antibodies (or chaperons) on amyloid ﬁbrillation is
a systematic and laborious task, and has not been developed into a mature theoretical framework. Here we just look
into one particular example to show how to do it in principle. The mechanism of antibody blocking ﬁbril ends and
stopping the elongation process could be formulated into
d
dt[B] = −k+
b Pfree[B] + k−
b Pbound,
(66)
d
dtPfree = knmnc + k2mn2M−k+
b Pfree[B] + k−
b Pbound,
(67)
d
dtM = k+
e mPfree −k−
e Pfree,
(68)
where Pfree = P −Pbound and Pbound = btot −[B] are concentrations of free ﬁbril ends and antibody blocked ﬁbril
ends separately. [B](t) is the free antibody concentration at time t, and btot is the total concentration of antibodies,
which is conserved during reactions. k+
b and k−
b are rate constants for antibody binding and unbinding respectively.
In a similar way, antibody binding oligomers and blocking primary nucleation or secondary nucleation, chaperons
binding ﬁbrils and reversing amyloid formation, etc. could be modeled and will not be addressed further.
In the presence of antibody or chaperon, model analysis becomes far more diﬃcult. However, under one particular
condition interested in experiments, i.e. the rates for antibody (or chaperon) binding and unbinding are much faster
than the ﬁbrillation speed, we can safely apply the Partial Equilibrium Approximation (PEA) to (66) and suppose
terms on the right-hand side cancelling each other at every moment, meaning −k+
b [B]P + k−
b (btot −[B]) = 0. Then
class results for P and M without antibody binding are recovered. This leads to an important conclusion that, in
order to manipulate amyloid ﬁbrillation, the rate for antibody unbinding must be slower than that of ﬁbrillation.
FIG. 14: Brichos slows down Aβ42 aggregation by inhibiting the surface catalyzed secondary nucleation. (A)-(C): From left
(blue) to right (green), 0%, 10%, 15%, 35%, 50%, 75% and 100% Aβ42 monomer equivalents of Brichos have been added
respectively. The concentration of monomeric Aβ42 is 3 µM. (D)-(F): The blue line corresponds to the situation in the absence
of Brichos. The green dashed lines in (D)-(F) respectively show predictions for the cases in which primary nucleation, elongation
and secondary nucleation are inhibited. Image is taken from [180] with copyright permission.


## Page 41


41
G.
Summary
The ﬁbrillation kinetics is a central issue in the study of amyloidosis and amyloid diseases. In the past several years,
fruitful results and plenty of deep physical insights have been obtained in this direction. Among them, mathematical
modeling based on chemical mass-action equations oﬀers a uniﬁed framework to treat this problem. In the current
section, we focus on how to apply kinetic modeling to explain various kinetic phenomena we have observed in real
amyloid systems, which could be characterized and classiﬁed according to the half-time and ﬁber apparent growth
rate as shown in Table I. Actually, the scaling relations between half-time of ﬁbrillation (or ﬁber apparent growth
rate) and monomer concentration provide us a useful way in practice to pick out the proper model, to classify amyloid
systems based on their own ﬁbrillation mechanisms (see Fig. 15) etc.
Mechanism
t1/2
kapp
parameters
NE
λ−1
λ
λ =
p
knk+
e mnc
tot
NES
κ−1
s
ln(κs/λ)
κs
κs =
q
k+
e k2mn2+1
tot
NEF
κ−1
f
ln(κf/λ)
κf
κf =
q
k+
e k+
f mtot
NE*
√1 + αλ−1
λ/√1 + α
α = mtot/Km
NE*S
√1 + ακ−1
s
ln(κs/λ)
κs/√1 + α
NE*F
√1 + ακ−1
f
ln(κf/λ)
κf/√1 + α
NES*
√1 + βκ−1
s
ln(κs/λ)
κs/√1 + β
β = (mtot/Ks)n2
NE*S*
p
(1 + α)(1 + β)κ−1
s
ln(κs/λ) κs/
p
(1 + α)(1 + β)
seeded E
ν−1
ν
ν = k+
e P0
seeded E*
αν−1
ν/α
TABLE I: A summary of half-time and apparent ﬁber growth rate under diﬀerent ﬁbrillation mechanisms. Capital E stands for
elongation, S for surface catalyzed secondary nucleation, F for fragmentation and ∗for saturation of corresponding processes.
“Seeded” means conditions with pre-added seeds. In general, fragmentation can be regarded as a special case of secondary
nucleation with n2 = 0.
IV.
MATHEMATICAL AND APPLICATION FOUNDATIONS
The former section is wholly based on macroscopic kinetic models for the mass concentration and number concen-
tration of ﬁbrils, but why we can adopt this simple picture and how its accuracy is compared to models at a molecular


## Page 42


42
FIG. 15: Scaling relationships between kapp, t1/2, and mtot for eight fragmentation dominated amyloid proteins, i.e. the yeast
prion Sup35 NW region (purple triangles up), Csg Btrunc (red squares), Ure2 protein (cyan pentacles), β2-microglobulin (brown
stars), steﬁn B (blue cross), α-synucleins (black triangles down), WW domain (yellow circles), and insulin (green diamonds).
Image is taken from [127] with copyright permission.
lever have never been addressed. For this purpose, here we are going to the mathematical foundation of kinetic mod-
eling, in which the mathematical linkage between models at the microscopic scale (molecular lever) and macroscopic
scale (what we adopted in the former section) will be clariﬁed in quantity. Interestingly, this linkage provides us ways
to reconstruct the full ﬁber length distribution from a knowledge of mass concentration and number concentration
of ﬁbrils in a high accuracy, which is generally believed to be very diﬃcult as an inverse problem. Finally, issues on
how to convert model predictions into experimental observations, how to determine unknown model parameters and
how to perform reliable global ﬁttings are discussed too, in order to provide a relatively comprehensive review on the
kinetic aspect.
A.
How to quantify ﬁbrillation kinetics
In order to quantify the kinetics of amyloid ﬁbrillation, let’s introduce the ﬁber length distribution {[Ai], i ≥1}, each
of whose components represents the concentration of aggregates containing exactly i protein molecules. Especially,
muiv[A1] stands for the concentration of monomers. According to diﬀerent reaction schemes for amyloid aggregation
which we have addressed in details in the main text, the time evolution of {[Ai](t)} will be characterized through a
group of coupled ordinary diﬀerential equations (without taking the spacial distribution into consideration) by using
laws of mass-action. This leads to the so-called “microscopic chemical kinetic equations”, since they contain a full
knowledge of the ﬁber length distribution.
On the other hand, either due to resolution limitation of experiments which makes it impossible to obtain a full
spectrum of ﬁber length distribution, or for a purpose to speed up simulation without taking too many details into
consideration, a simple coarse-grained description is preferred. Among various candidates, formulation involving two


## Page 43


43
macroscopic quantities – the number concentration and mass concentration of aggregates (including both oligomers
and ﬁbrils)
P =
∞
X
i=nc
[Ai],
M =
∞
X
i=nc
i · [Ai],
(69)
where nc stands for the critical nucleus size, is the most popular and welcomed. A basic reason is that this formulation
actually provides a simplest self-consistent way to examine the amount of amyloid ﬁbrils formed inside a given system,
a quantity we are most interested in.
From above deﬁnition, we can see that P and M are actually the zeroth and ﬁrst-order moments of ﬁber length
distribution {[Ai]} for i ≥nc. The total mass concentration mtot =
∞
P
i=1
i · [Ai] is another often used ﬁrst-order moment.
In particular, if oligomer concentration [Ai] (2 ≤i ≤nc −1]) could be neglected, we will have mtot = m(t) + M(t),
an equality representing the mass conservation of total protein molecules during ﬁbrillation. In principle, other high
order moments could also be introduced into the formulation in order to achieve a high accuracy, but in many cases
it is not very worthwhile due to the sacriﬁce of both simplicity and eﬃciency. In literature, the governing equations
of moments are referred to as “macroscopic chemical kinetic equations” in contrast to microscopic formulation based
on ﬁber length distribution.
The relation between macroscopic and microscopic chemical kinetic equations is an interesting question. In fact, a
whole branch of statistical physics is dealing with such problems on how to derive macroscopic quantities and their
governing kinetic equations from a knowledge of microscopic descriptions [181]. There are enormous investigations,
fruitful results and endless debates in history which are far beyond the scope of this paper. But on current speciﬁc
topic, almost all issues could be solved by some well-formulated moment-closure methods. We will come back to this
point with all necessary details in the next section.
At last, we want to introduce the half time of ﬁbrillation t1/2 and the apparent ﬁber growth rate kapp [127], i.e.
M(t1/2) = M(0) + M(∞)
2
,
kapp =
1
mtot
dM
dt

t=t1/2
.
(70)
These two quantities are essential to characterize the kinetics of amyloid ﬁbrillation in an empirical way (see (89)),
even without referring to any models or analytical solutions. Two additional quantities appear in literature from time
to time too. One is the lag time, which is deﬁned as tlag = t1/2 −1/(2kapp). The lag time has an intuitive physical
meaning, which measures how long an amyloid system has to wait in order to accumulate enough seeds to pass the
phase dominated by primary nucleation. In the presence of secondary nucleation, the lag time becomes prominent
due to the sigmoid ﬁbrillation proﬁle, and could be greatly shortened by an introduction of initial seeds. There are


## Page 44


44
also other ways to deﬁne the lag time in literature, e.g. the time when the mass concentration of aggregates reaches
1% of its static value [182]. Obviously, our deﬁnition is more natural and meaningful in physics. The other quantity is
related to the speed of ﬁbril growth, its maximal value to be exact. However, in most cases the maximal ﬁber growth
rate kmax relies on the whole ﬁbrillation proﬁle, which makes it diﬃcult to determine and use.
B.
How to coarse-grain model
In last section, we have introduced the ﬁber length distribution and its moments in diﬀerent orders, like the number
concentration and mass concentration of aggregates. We have also claimed there is a direct connection between the
macroscopic and microscopic chemical kinetic equations. Now we are going to address this point based on the method
of moment closure.
Without loss of generality, we consider the reaction scheme proposed for the length-dependent fragmentation [111].
According to laws of mass-action, the time evolution of ﬁber length distribution obeys following equations
d[A1]
dt
= −nck+
n [A1]nc + nck−
n [Anc] −k+
e [A1]
∞
X
j=nc
[Aj] + k−
e
∞
X
j=nc+1
[Aj],
(71)
d[Ai]
dt
= k+
e [A1]([Ai−1] −[Ai]) −k−
e ([Ai] −[Ai+1]) + 2
∞
X
j=nc+i
k+
f (i, j −i)[Aj]
−
i−nc
X
j=nc
k+
f (j, i −j)[Ai] −2
∞
X
j=nc
k−
f (i, j)[Ai][Aj] +
i−nc
X
j=nc
k−
f (j, i −j)[Aj][Ai−j]
+(k+
n [A1]nc −k−
n [Ai] −k+
e [A1][Ai−1] + k−
e [Ai])δi,nc,
i ≥nc.
(72)
As a consequence, it is straightforward to show that the number concentration P(t) and mass concentration M(t) of
aggregates evolve according to
d
dtP = k+
n (mtot −M)nc −k−
n [Anc] +
∞
X
i=nc
∞
X
j=i+nc
k+
f (i, j −i)[Aj] −
∞
X
i=nc
∞
X
j=nc
k−
f (i, j)[Ai][Aj],
(73)
d
dtM = nck+
n (mtot −M)nc −nck−
n [Anc] + k+
e (mtot −M)P −k−
e P + k−
e [Anc],
(74)
which clearly are not closed, as unknown variables {[Ai]} have not been expressed through P and M.
To solve this problem, a systematic moment closure method based on Maximum Entropy Principle [112, 113] has
been proposed and applied with great success [111, 169, 183] (as shown in Fig. 16). Namely, we seek for solutions of


## Page 45


45
following constrained optimization problem, i.e.
max
S({[Ai]}) = −kB
∞
X
i=nc
([Ai] ln[Ai] −[Ai]),
(75)
s.t.
∞
X
i=nc
[Ai] = P,
∞
X
i=nc
i · [Ai] = M, [A1] +
∞
X
i=nc
i · [Ai] = mtot.
(76)
It could also be translated into an equivalent variational problem through the method of Lagrangian multiplier,
δ
δ[Ai]

S({[Ai]})/kB + λ1

∞
X
i=nc
[Ai] −P

+ λ2

∞
X
i=nc
i · [Ai] −M

+ λ3

[A1] +
∞
X
i=nc
i · [Ai] −mtot

= 0,
(77)
where λ1, λ2 and λ3 are Lagrangian multipliers. The solution of above equation is given by
[A1] = e(λ3),
(78)
[Ai] = e[λ1 + i(λ2 + λ3)],
(79)
based on which λ1, λ2 and λ3 are related to P(t), M(t) and mtot as
λ1 = ln

P 2
M −(nc −1)P

−nc ln

M −ncP
M −(nc −1)P

,
(80)
λ2 = ln

M −ncP
M −(nc −1)P

−ln(mtot −M),
(81)
λ3 = ln(mtot −M).
(82)
Put these formulas back into (73) and (74), we obtain desired macroscopic chemical kinetic equations solely concerning
with P(t) and M(t).
In [111], it has been proven that above moment closure method based on Maximum Entropy Principle is mathe-
matically equivalent to Partial Equilibrium Approximation on ﬁber elongation, which assumes the elongation process
is much faster than primary nucleation and fragmentation. Therefore, for given number concentration P(t) and mass
concentration M(t) of aggregates, each component of ﬁber length distribution {[Ai]} is considered in quasi-equilibrium
with each other, which is exactly the way how we are able to express [Ai](t) as a function of P(t), M(t) and mtot.
C.
How to reconstruct ﬁber length distribution from moments
In previous section, we have focused on how to simplify the model by coarse-graining, which turns out to be a very
promising approach with tremendous successful applications. However, during coarse-graining, we are facing with
an inevitable loss of information. Original knowledge of full ﬁber length distribution has been compressed into that
about only two macroscopic moments – the number and mass concentration of aggregates to be exact. Is it possible


## Page 46


46
FIG. 16: Accuracy of moment-closure method through comparisons on the ﬁber mass concentration, number concentration and
ﬁber length distribution in (A-C). Values obtained from microscopic kinetic equations (71) and (72) are drawn in circles and
that from moment-closure methods in solid lines. (D) Application to the polymerization of WW domain. Image is taken from
[111] with copyright permission.
to reconstruct original ﬁber length distribution based on a knowledge of these two moments? This is a question not
only of mathematical interest, but also with great practical usage. In principle, inverse problems are generally very
diﬃcult to solve and do not admit a unique solution [184–186]. But, in current case without considering ﬁlaments
fragmentation and annealing, as we are so lucky to have a complete understanding about underlying microscopic
processes, the full ﬁber length distribution at any time could be explicitly extracted just from one moment – mass
concentration of aggregates as well as some knowledge about the initial length distribution. A brief derivation is listed
as follows.
Without loss of generality, let us start with following microscopic model, including primary nucleation, elongation
and secondary nucleation [187],
d[Ai]
dt
= k+
e m(t)([Ai−1] −[Ai]) + knm(t)ncδi,nc + k2m(t)n2
mtot −m(t)

δi,n2,
i ≥nc
(83)
where n2 ≥nc > 0. Introduce the generating function [188]
C(z, t) =
∞
X
j=nc
zj · [Aj](t),
(84)
which is a natural mathematical generalization of the physical moments. Especially, we have P(t) = C(z = 1, t) and
M(t) = ∂C(z,t)
∂z
|z=1. In fact, the ful ﬁber length distribution could be recovered from the generating function, i.e.
[Aj](t) = 1
j!
∂jC(z,t)
∂zj

z=0 for i ≥nc, which means the generation function is a one-to-one mapping of the ﬁber length
distribution.
It is straightforward to show that the generating function satisﬁes following equation
∂C(z, t)
dt
= k+
e m(t)(z −1)C(z, t) + knm(t)ncznc + k2m(t)n2[mtot −m(t)]zn2.
(85)
Deﬁne a new time scale τ(t) =
R t
0 k+
e m(s)ds, which acts as the characteristic time for ﬁber elongation, above equation


## Page 47


47
could be rewritten as
∂C(z, τ)
dτ
= (z −1)C(z, τ) +

knm(τ)ncznc + k2m(τ)n2[mtot −m(τ)]zn2
 ∂t
∂τ ,
(86)
whose solution is given by
C(z, τ(t)) =
Z t
0
e−(z−1)[τ(s)−τ(t)]

knm(s)ncznc + k2m(s)n2[mtot −m(s)]zn2

ds + C(z, 0)e(z−1)τ(t).
(87)
Now the ﬁber length distribution at any given time t could be calculated through following formula
[Aj](t) = 1
j!
∂jC(z, t)
∂zj

z=0
=
Z t
0
Θj−nc(t, s)knm(s)ncds +
Z t
0
Θj−n2(t, s)k2m(s)n2[mtot −m(s)]ds
+
j
X
k=nc
Θj−k(t, 0)[Ak](0),
(88)
where τ(t) =
R t
0 k+
e m(s)ds and Θk(t, s) = eτ(s)−τ(t)[τ(t) −τ(s)]k/k!. During the calculation, we use identities 00 = 1
and 0! = 1.
Above formula provides the mathematical foundation on how to extract the full ﬁber length distribution at any
time just based on the time course of monomer concentration (or mass concentration of aggregates M(t)) as well as
the initial ﬁber length distribution. This is a quite astonishing result, as we have mentioned that inverse problems
are usually extremely diﬃcult to solve and do not admit a unique solution in general. Our success in this case could
be contributed to two reasons: one is we have a complete knowledge on the microscopic kinetics which governs the
time evolution of ﬁber length distribution; the other is both primary nucleation and secondary nucleation can solely
aﬀect the concentration of single species [Anc] or [An2]. The only way to perform a global change of the ﬁber length
distribution is elongation, which follows a Poisson process characterized by the integral kernel Θk(t, s) with intrinsic
time scale τ(t) =
R t
0 k+
e m(s)ds, since each monomer association is obviously random and independent of each other.
In the presence of ﬁlaments fragmentation and annealing, an additional global change of the ﬁber length distribution
will be introduced besides elongation. How to include these two processes into above picture explicitly is an unsolved
problem. In particular, Michaels et al. derived approximate solutions for length-independent fragmentation in open
and close systems [189]. While for general models with length-dependent fragmentation and annealing, an empirical
method has been proposed, whose theoretical foundation lies on the fact that during the procedure of moment-closure,
the microscopic ﬁber length distribution is expressed through macroscopic moments based on Maximum Entropy
Principle. The thus obtained ﬁber length distribution directly determines the accuracy of macroscopic equations,
which as a consequence could be adopted as an empirical candidate to approximate the exact ﬁber length distribution
without introducing new errors. This empirical approach has been applied to examine a fragmentation-only model


## Page 48


48
and matches perfectly with numerical solutions and experimental data for ﬁber-like PI264-b-PFS48 micelles under
sonication as shown in Fig. 17 [183]. In addition, similar procedure has been shown eﬀective for a more complicated
model, including primary nucleation, elongation and length-dependent fragmentation [190].
FIG. 17: Accuracy of approximate ﬁber length distribution constructed from moment-closure method for a fragmentation-
only model. Comparisons were made among TEM measurements of ﬁber-like PI264-b-PFS48 micelles under sonication (black
symbols), exact ﬁber length distribution in (71) and (72) (red solid curves), and approximate ﬁber length distributions (brown
and blue dashed curves). Image is taken from [183]) with copyright permission.
D.
How to make a connection to experiments
According to Nilsson [191], there are three criteria that deﬁne a protein aggregate as an amyloid ﬁbril: green
birefringence upon staining with Congo Red, ﬁbrillar morphology, and β-sheet secondary structure. Based on these
three criteria, plenty of novel instruments and techniques have been developed to probe amyloid ﬁbrils and their
kinetics. Instead of providing a comprehensive review on each technique, like its basic setup, procedure and protocols,
advantages and limitations, we will focus on the relation between those physical quantities we can measure and
mathematical quantities we have deﬁned for characterizing the ﬁbrillation kinetics.
The most widely adopted technique to monitor the ﬁbrillation kinetics is Thioﬂavin T (ThT) ﬂuorescence. When
it binds to β-sheet-rich structures, like those in amyloid aggregates, the dye displays enhanced ﬂuorescence and a
characteristic red shift of its emission spectrum [192, 193]. It has been shown that: (1) the ThT ﬂuorescence intensity
increases nearly linearly with the total amount of amyloid ﬁbrils for several orders of magnitude; (2) the ﬂuorescence
intensity is independent of number concentration of amyloid ﬁbrils if mass concentration is constant; (3) if the number
concentration is ﬁxed as in the extension kinetic study, the increase of average length of amyloid ﬁbrils corresponds to
an increase in the ﬂuorescence intensity too [194, 195]. These features make ThT ﬂuorescence an unusually sensitive
and eﬃcient reporter for the mass concentration of aggregates M(t), despite of limitations that ThT is not perfectly
speciﬁc for amyloid ﬁbrils, as well as some amyloid ﬁbrils do not aﬀect the ﬂuorescence. In experiments, following


## Page 49


49
empirical formula is often used to interpret the ﬂuorescence intensity observed during amyloid ﬁbrillation [104],
F(t) = F(0) +
A
1 + e[−kapp(t −t1/2)],
(89)
where F(t) is the ﬂuorescence intensity at time t, F(0) is the background ﬂuorescence intensity at the starting time,
and A is a ﬁtting constant to correlate the mass concentration of aggregates with the absolute ﬂuorescence intensity.
Based on above formula, we can easily extract the apparent ﬁber growth rate kapp and half-time of ﬁber formation
t1/2 from data ﬁtting.
The goal of any absorption spectroscopy, e.g. Fourier transform infrared (FTIR) spectroscopy, ultraviolet-visible
(UV) spectroscopy, circular dichroism (CD) etc., is to detect the presence of certain molecular structure by measuring
the light absorbed at each wavelength.
It has been established that, in FTIR, a peak near 1645cm−1 indicates
random coil, 1655cm−1 for α-helix and 1620 −1640cm−1 for β-sheet [196]; while in far-ultraviolet (170 −250nm)
circular dichroism, a pronounced double minimum at 208 and 222nm indicates α-helical structure, and a single
minimum at 204nm or 217nm reﬂects random-coil or β-sheet structure [197, 198]. Thus we can make a quantitative
correlation between the fraction of certain structure (say β-sheet as an indicator of amyloid ﬁbrils) with absorbed
light intensity at the corresponding wavelength. Here we take the CD spectroscopy as a simple example, in which the
fraction of β-sheet structure could be expressed through the measured ellipticity as [199]
Cbeta
Cbeta + Ccoil
= Θobs
217 −Θ0
217
Θmax
217 −Θ0
217
,
(90)
where Θ0
217 is the ellipticity at 217nm at the beginning of time; while Θobs
217 and Θmax
217 represent observed and maximal
ellipticity at 217nm during the whole measurement. Cbeta and Ccoil represent the concentration of β-sheet and random
coil structures separately.
Instead of light absorption, dynamic light scattering (DLS) is a technique that can be used to determine the size
distribution proﬁle of small particles in suspension or polymers in solution [200]. Although light scattering by particles
in solution depends on a number of factors, the most relevant one is the ratio of particle size with respect to quantity
λ/[2π sin(θ/2)], where λ is the wavelength of incident light and θ is the angle of detection [132, 201]. As the average
length of amyloid ﬁbrils is expected to get larger during amyloid ﬁbrillation, the intensity of light scattered by ﬁbrils
will be directly proportional to the mass concentration of aggregates [62, 202],
Iscat(t) =
QλM(t)
4l sin(θ/2),
(91)
where l is the monomer size, Q is a constant depending on the setup.


## Page 50


50
Currently, transmission electron microscopy (TEM), atomic-force microscopy (AFM) and scanning-force microscopy
(SFM) are most advanced techniques with highest resolution. According to [203], the smallest distance that can be
resolved with a TEM is approximately 0.2−0.5nm and, for STM, a typical resolution of several tenths of one nanometer
can be achieved. In comparison, the diameter of typical ﬁlaments is around 3 −4nm and 8 −10nm for mature ﬁbrils,
while the length may vary from hundreds of nanometers to a few micrometers [204–206]. Therefore, we may use
those instruments to directly observe the growth, inhibition, propagation and adaptation of single ﬁbril and even its
breakage and branching in real time [131, 207–209]. With high-resolution images in hand, the ﬁber length distribution
could be extracted to certain accuracy, based on which both the number concentration and mass concentration of
aggregates could be obtained. As a conclusion, advanced high-resolution microscopies could provide us most detailed
information about amyloid ﬁbrils, both their morphology and kinetics, though at an great expense of money and time.
E.
How to determine model parameters
How to determine unknown parameters is a key step in model application. Although it is as important as modeling
itself, details behind parameter ﬁtting have seldom been clariﬁed.
A major obstacle is that usually most model
parameters are empirical and hard to be precisely determined by either experiments or fundamental principles in
nature. Their accuracy and validity heavily depends on the experience of modelers.
Here we face with the same problem. In current study, the parameters, we adopted for describing amyloid ﬁbrillation,
cell damage and antibody inhibition in the main text, can be roughly divided into four groups.
The initial protein concentration mtot, mass concentration M0 and number concentration P0 of initial seeds, total
cell concentration ctot and antibody concentration btot are generally pre-speciﬁed in the setup. They are not adjustable
during the ﬁtting and can be classiﬁed into Group I.
Group II contains those application-insensitive parameters, like the critical nucleus size nc, the monomer disassoci-
ation rate k−
e and ﬁlaments annealing rate k−
f in some cases. Since their values have a minor inﬂuence on the model
performance, according to Occam’s Razor, they can set to a default value (usually nc = 2 and k−
e = k−
f = 0). In
mathematics, sensitivity analysis allows a systematical determination of model parameters in this group.
Group III contains those parameters which can be determined either by experiments or by some fundamental
principles. For example, as discussed in section of how ﬁbrils grow, the ﬁber elongation rate k+
e for diﬀerent amyloid
proteins has been measured by plenty of techniques in recent years.
We can directly take their values from the
literature giveing the same amyloid protein under similar experimental conditions.


## Page 51


51
The last group includes those freely adjustable model parameters. In most cases, the primary nucleation rate kn,
critical nucleus size n2 and rate k2 for surface-catalyzed secondary nucleation, ﬁber fragmentation rate k+
f are essential
for modeling the ﬁbrillation kinetics, and oligomer binding and unbinding rates k+
b and k−
b for modeling cell damage.
The ﬁrst four parameters can be gotten by performing global ﬁtting of amyloid formation, while the last two are
determined through data on cytotoxicity (a sensitivity analysis of model parameters could be learned from Fig. 18).
In this sense, there will be no free tunable parameter left.
t1/2
fib (min-1)
0
100
200
300
400
500
kn
+
ke
+
kf
+
kf
-
kb
+
kb
-
decrease 0.5X
baseline value
increase 2X
kapp
fib (min-1)
0
0.005
0.01
0.015
0.02
kn
+
ke
+
kf
+
kf
-
kb
+
kb
-
t1/2
cell(min-1)
0
200
400
600
800
1000
kn
+
ke
+
kf
+
kf
-
kb
+
kb
-
kapp
cell(min-1)
0
0.005
0.01
0.015
kn
+
ke
+
kf
+
kf
-
kb
+
kb
-
FIG. 18: Model sensitivity on six adjustable parameters. The baseline values are taken in accordance with those in Fig. 13B.
All six reaction rates are changed by either two times or one half with respect to their baseline values separately.
F.
How to perform global ﬁtting
As claimed by John von Neumann, “With four parameters I can ﬁt an elephant, and with ﬁve I can make him
wiggle his trunk.” An over-ﬁt of experimental data with too many undetermined model parameters is encountered
from time to time. Although a great eﬀort has been dedicated to eliminate unnecessary model parameters as shown
in last section, we are still facing with the problem how to perform a ﬁtting reasonably and robustly. Global ﬁtting,
as suggested by its name, provides a nice way to partially solve this diﬃculty and make the ﬁtting more reliable and
promising.
The central idea of global ﬁtting is to try to ﬁt all data at the same time with the same parameters. In a such
way, the redundancy in model parameters could be eliminated as much as possible and those key parameters will be


## Page 52


52
highlighted. Although, the requirement of global ﬁtting is quite natural from a theoretical view, in practice it is not
so easy to perform it. One obstacle is data noise. In the presence of large noise, a global ﬁt becomes impossible, which
means we have to either try best to eliminate noise source and perform measurements as precisely as possible, or
include the inﬂuence of noise into modeling at the beginning (e.g. stochastic models). Another obstacle comes from
the high dimensionality of the parameter space. Eﬃcient global exploration methods, applicable to high dimensional
space, has to be implemented during the procedure of ﬁtting. In contrast, local exploration methods or those only
valid for low dimensional space are not applicable. Finally, quantitative judgements or scores are needed in order to
tell which group of model parameters gives the best ﬁtting.
For this purpose, programs for global ﬁtting have been developed for the kinetic models we have discussed in the
main text [210]. Various global exploration methods, such as simulated annealing, genetic algorithm, particle swarm
method ect., have been implemented into the program to avoid local trapping (private codes). Generally speaking,
according to our own experience, simulated annealing is eﬃcient and reliable in most cases; genetic algorithm consumes
the longest CPU time among the three; while particle swarm is also quite slow, but in some cases it gives better results
than simulated annealing. In these programs, nonlinear least-square regression is adopted to minimize the sum of
squared errors between experimental data and those predicted by the model. Now we plan to take the inﬂuence of
noises on global ﬁtting into consideration. Related works are going on.
V.
CONCLUSION
In the past decades, due to the increasing interest on amyloid related diseases, a variety of amyloid proteins and
their ﬁbrillation processes have been investigated in details. In this self-contained reviewed, fruitful results on both
thermodynamics and kinetics of amyloid ﬁbrillation have been shown and discussed, with a purpose to provide a
relatively comprehensive physical picture on what we know and what we do not know in this ﬁeld. As a summary,
facts we have learned from thermodynamic and kinetic modeling are:
1. The existence of a critical ﬁbrillar concentration below which ﬁbrillar mass is negligible;
2. Above the critical ﬁbrillar concentration, the length distribution of the ﬁbrils is exponential. This remains so
even in the semi-dilute limit, if the ﬁbril-ﬁbril interactions are purely steric;
3. If the ﬁbrils exhibit attractive lateral interactions, there will be a strong tendency for phase separation of ﬁbrils;
4. Molecular mechanisms of amyloid ﬁbrillation could be formulated into a group of microscopic chemical kinetic


## Page 53


53
equations concerning with ﬁber length distribution;
5. Low-order moments, a function of ﬁber length distribution, evolves according to macroscopic chemical mass-
action equations derived by moment-closure method;
6. Mass concentration and number concentration of aggregates are two most widely used moments and provide a
well characterization of ﬁbrils;
7. In many cases, ﬁber length distribution could be reconstructed from moments exactly or approximately once
the underlying ﬁbrillation kinetics is known;
8. Primary nucleation, elongation and secondary nucleation, including monomer-independent fragmentation and
monomer-dependent surface catalyzed secondary nucleation, constitute a basic framework for amyloid ﬁbrilla-
tion, which has been applied to many amyloid systems successfully;
9. Conformational conversion of monomeric, oligomeric and ﬁbrillar structures is crucial for amyloid ﬁbrillation
but easily neglected in kinetic modeling due to other rate-limiting steps;
10. Eﬀect of high monomer concentration on ﬁber elongation and surface catalyzed secondary nucleation could be
explained by saturation;
11. Oligomers binding to lipid membrane play a key role in cytotoxicity and can easily included in kinetic models;
12. Quantitative knowledge on how to manipulate amyloid species and ﬁbrillation kinetics could be learned from
kinetic modeling, which provides us a power method to probe amyloidosis.
In our opinion, answering the following questions would constitute fruitful research direction:
1. How to incorporate various morphologies of amyloid ﬁbrils into the thermodynamic picture?
2. How to construct a complete picture of phase separation and transition for amyloid ﬁbrillation?
3. How to include oligomeric species explicitly in kinetic models?
4. How to model lateral association of protoﬁbrils or ﬁlaments into mature ﬁbrils, like coiling and twisting?
5. How to determine various reaction rate constants under a given ﬁbrillation condition?
6. How to systematically quantify the eﬀect of antibody and chaperon in order to manipulate amyloid ﬁbrillation?


## Page 54


54
7. How to correlate amyloidosis with their ﬁbrillation mechanisms at a molecular level?
8. How to probe amyloid diseases with kinetic modeling?
Acknowledgment
This work was supported by the National Natural Science Foundation of China (Grants 11204150), Tsinghua Uni-
versity Initiative Scientiﬁc Research Program (Grants 20151080424) and the program of China Scholarships Council
(CSC). Y.J.H also acknowledges the Postdoctoral Science Foundation of China (2015M581050).
[1] Christopher M Dobson. Protein folding and misfolding. Nature, 426(6968):884–890, 2003.
[2] Fabrizio Chiti and Christopher M Dobson.
Protein misfolding, functional amyloid, and human disease.
Annu. Rev.
Biochem., 75:333–366, 2006.
[3] John S Schreck and Jian-Min Yuan. Statistical mechanical treatments of protein amyloid formation. International journal
of molecular sciences, 14(9):17420–17452, 2013.
[4] Aimee M Morris, Murielle A Watzky, and Richard G Finke. Protein aggregation kinetics, mechanism, and curve-ﬁtting:
a review of the literature. Biochimica et Biophysica Acta (BBA)-Proteins and Proteomics, 1794(3):375–397, 2009.
[5] Samuel IA Cohen, Michele Vendruscolo, Christopher M Dobson, and Tuomas PJ Knowles. From macroscopic measure-
ments to microscopic mechanisms of protein aggregation. Journal of molecular biology, 421(2):160–171, 2012.
[6] JE Gillam and CE MacPhee. Modelling amyloid ﬁbril formation kinetics: mechanisms of nucleation and growth. Journal
of Physics: Condensed Matter, 25(37):373101, 2013.
[7] Liu Hong, Xianghong Qi, and Yang Zhang. A lattice-gas model for amyloid ﬁbril aggregation. EPL (Europhysics Letters),
94(6):68006, 2011.
[8] HB Callen. Thermodynamics and an introduction to thermostatistics. 1985.
[9] Yufeng Wang, Yu Wang, Dana R Breed, Vinothan N Manoharan, Lang Feng, Andrew D Hollingsworth, Marcus Weck,
and David J Pine. Colloids with valence and speciﬁc directional bonding. Nature, 491(7422):51–55, 2012.
[10] Chiu Fan Lee. Self-assembly of protein amyloids: A competition between amorphous and ordered aggregation. Physical
Review E - Statistical, Nonlinear, and Soft Matter Physics, 80(3):031922, 2009.
[11] K Huang. Statistical mechanics, 2nd. Edition (New York: John Wiley & Sons), 1987.
[12] Daan Frenkel. Why colloidal systems can be described by statistical mechanics: some not very original comments on the
gibbs paradox. Molecular Physics, 112(17):2325–2329, 2014.


## Page 55


55
[13] Jacob N Israelachvili. Intermolecular and surface forces: revised third edition. Academic press, 2011.
[14] ME Cates and SJ Candau. Statics and dynamics of worm-like surfactant micelles. Journal of Physics: Condensed Matter,
2(33):6869, 1990.
[15] Jeroen van Gestel and Simon W de Leeuw. A statistical-mechanical theory of ﬁbril formation in dilute protein solutions.
Biophysical journal, 90(9):3134–3145, 2006.
[16] Jeremy D Schmit, Kingshuk Ghosh, and Ken Dill. What drives amyloid molecules to assemble into oligomers and ﬁbrils?
Biophysical journal, 100(2):450–458, 2011.
[17] Salman S Rogers, Paul Venema, Leonard MC Sagis, Erik van der Linden, and Athene M Donald. Measuring the length
distribution of a ﬁbril system: a ﬂow birefringence technique applied to amyloid ﬁbrils. Macromolecules, 38(7):2948–2958,
2005.
[18] Wei-Feng Xue, Steve W Homans, and Sheena E Radford. Amyloid ﬁbril length distribution quantiﬁed by atomic force
microscopy single-particle image analysis. Protein Engineering Design and Selection, page gzp026, 2009.
[19] Martijn E Van Raaij, Jeroen Van Gestel, Ine MJ Segers-Nolten, Simon W De Leeuw, and Vinod Subramaniam. Concen-
tration dependence of α-synuclein ﬁbril length assessed by quantitative atomic force microscopy and statistical-mechanical
theory. Biophysical journal, 95(10):4871–4878, 2008.
[20] Bertrand Morel, Lorena Varela, Ana I Azuaga, and Francisco Conejero-Lara. Environmental conditions aﬀect the kinetics
of nucleation of amyloid ﬁbrils and determine their morphology. Biophysical journal, 99(11):3801–3810, 2010.
[21] Paul van der Schoot and Michael E Cates. Growth, static light scattering, and spontaneous ordering of rodlike micelles.
Langmuir, 10(3):670–679, 1994.
[22] P G de Gennes and J Prost. The physics of liquid crystals (International Series of Monographs on Physics). Number 83.
Oxford university press, 1995.
[23] Doi. M and Sam F Edwards. The theory of polymer dynamics. 1986.
[24] Adam M Corrigan, Christian M¨uller, and Mark RH Krebs. The formation of nematic liquid crystal phases by hen lysozyme
amyloid ﬁbrils. Journal of the American Chemical Society, 128(46):14740–14741, 2006.
[25] P Van Der Schoot and ME Cates. The isotropic-to-nematic transition in semi-ﬂexible micellar solutions. EPL (Europhysics
Letters), 25(7):515, 1994.
[26] T. Odijk. Eﬀect of micellar ﬂexibility on the isotropic-nematic phase transition in solutions of linear aggregates. Journal
Physics France, 48(1):125–129, 1987.
[27] Chiu Fan Lee, James Loken, Letitia Jean, David J Vaux, et al. Elongation dynamics of amyloid ﬁbrils: A rugged energy
landscape picture. Physical Review E, 80(4):041906, 2009.
[28] Chiu Fan Lee. Isotropic-nematic phase transition in amyloid ﬁbrilization. Physical Review E - Statistical, Nonlinear, and
Soft Matter Physics, 80(3), 2009.


## Page 56


56
[29] Jean-Louis Barrat and Jean-Pierre Hansen. Basic concepts for simple and complex liquids. Cambridge University Press,
2003.
[30] Masao Doi. Introduction to polymer physics. Oxford university press, 1996.
[31] Helen R Saibil, Anja Seybert, Anja Habermann, Juliane Winkler, Mikhail Eltsov, Mario Perkovic, Daniel Casta˜no-Diez,
Margot P Scheﬀer, Uta Haselmann, Petr Chlanda, et al. Heritable yeast prions have a highly organized three-dimensional
architecture with interﬁber structures. Proceedings of the National Academy of Sciences, 109(37):14906–14911, 2012.
[32] Mary P Lambert, AK Barlow, Brett A Chromy, C Edwards, R Freed, M Liosatos, TE Morgan, I Rozovsky, B Trommer,
Kirsten L Viola, et al. Diﬀusible, nonﬁbrillar ligands derived from aβ1–42 are potent central nervous system neurotoxins.
Proceedings of the National Academy of Sciences, 95(11):6448–6453, 1998.
[33] Aleksey Lomakin, David B Teplow, Daniel A Kirschner, and George B Benedek.
Kinetic theory of ﬁbrillogenesis of
amyloid β-protein. Proceedings of the National Academy of Sciences, 94(15):7942–7947, 1997.
[34] An?ela ˇSari´c, Yassmine C Chebaro, Tuomas P J Knowles, and Daan Frenkel. Crucial role of nonspeciﬁc interactions in
amyloid nucleation. Proceedings of the National Academy of Sciences, 2014.
[35] Aneta T Petkova, Yoshitaka Ishii, John J Balbach, Oleg N Antzutkin, Richard D Leapman, Frank Delaglio, and Robert
Tycko.
A structural model for alzheimer’s β-amyloid ﬁbrils based on experimental constraints from solid state nmr.
Proceedings of the National Academy of Sciences, 99(26):16742–16747, 2002.
[36] Liu Hong and Jinzhi Lei. Statistical mechanical model for helix-sheet-coil transitions in homopolypeptides. Physical
Review E, 78(5):051904, 2008.
[37] Liu Hong. A statistical mechanical model for antiparallelsheet/coil equilibrium. J. Chem. Phys, 129(225101):1–225101,
2008.
[38] Ivan Usov, Jozef Adamcik, and Raﬀaele Mezzenga. Polymorphism complexity and handedness inversion in serum albumin
amyloid ﬁbrils. ACS nano, 7(12):10465–10474, 2013.
[39] George M Whitesides and Paul E Laibinis. Wet chemical approaches to the characterization of organic surfaces: self-
assembled monolayers, wetting, and the physical-organic chemistry of the solid-liquid interface. Langmuir, 6(1):87–96,
1990.
[40] Abraham Ulman. Formation and structure of self-assembled monolayers. Chemical reviews, 96(4):1533–1554, 1996.
[41] Frank Schreiber. Structure and growth of self-assembling monolayers. Progress in surface science, 65(5):151–257, 2000.
[42] Abraham Ulman. An Introduction to Ultrathin Organic Films: From Langmuir–Blodgett to Self–Assembly. Academic
press, 2013.
[43] Fumio Oosawa and Sho Asakura. Thermodynamics of the polymerization of protein. 1975.
[44] Sean R Collins, Adam Douglass, Ronald D Vale, Jonathan S Weissman, et al. Mechanism of prion propagation: amyloid
growth occurs by monomer addition. PLoS biology, 2:1582–1590, 2004.


## Page 57


57
[45] Fumio Oosawa, Sho Asakura, Ken Hotta, Nobuhisa Imai, and Tatsuo Ooi.
G-f transformation of actin as a ﬁbrous
condensation. Journal of Polymer Science, 37(132):323–336, 1959.
[46] Tuomas PJ Knowles, Wenmiao Shu, Glyn L Devlin, Sarah Meehan, Stefan Auer, Christopher M Dobson, and Mark E
Welland. Kinetics and thermodynamics of amyloid formation from direct measurements of ﬂuctuations in ﬁbril mass.
Proceedings of the National Academy of Sciences, 104(24):10016–10021, 2007.
[47] Alexander K Buell, Jamie R Blundell, Christopher M Dobson, Mark E Welland, Eugene M Terentjev, and Tuo-
mas PJ Knowles. Frequency factors in a landscape model of ﬁlamentous protein aggregation. Physical review letters,
104(22):228101, 2010.
[48] Tricia R Serio, Anil G Cashikar, Anthony S Kowal, George J Sawicki, Jahan J Moslehi, Louise Serpell, Morton F Arnsdorf,
and Susan L Lindquist. Nucleated conformational conversion and the replication of conformational information by a prion
determinant. Science, 289(5483):1317–1321, 2000.
[49] Pierre O Souillac, Vladimir N Uversky, and Anthony L Fink. Structural transformations of oligomeric intermediates in
the ﬁbrillation of the immunoglobulin light chain len. Biochemistry, 42(26):8094–8104, 2003.
[50] Byron Caughey and Peter T Lansbury Jr. Protoﬁbrils, pores, ﬁbrils, and neurodegeneration: Separating the responsible
protein aggregates from the innocent bystanders. Annual review of neuroscience, 26(1):267–298, 2003.
[51] Gal Bitan, Marina D Kirkitadze, Aleksey Lomakin, Sabrina S Vollers, George B Benedek, and David B Teplow. Amyloid
beta-protein (abeta) assembly: Abeta40 and abeta42 oligomerize through distinct pathways. Proceedings of the National
Academy of Sciences, 100(1):330–335, 2003.
[52] B O’Nuallain, S Shivaprasad, I Kheterpal, and R Wetzel. Thermodynamics of aβ(1-40) amyloid ﬁbril elongation. Bio-
chemistry, 44(38):12709–12718, 2005.
[53] Alexander K Buell, Christopher M Dobson, and Mark E Welland. Measuring the kinetics of amyloid ﬁbril elongation
using quartz crystal microbalances. In Amyloid Proteins, 849:101–119, 2012.
[54] Mikl´os SZ Kellermayer, ´Arp´ad Karsai, Margit Benke, Katalin So´os, and Botond Penke. Stepwise dynamics of epitaxially
growing single amyloid ﬁbrils. Proceedings of the National Academy of Sciences, 105(1):141–144, 2008.
[55] Dorothea Pinotsi, Alexander K Buell, Celine Galvagnion, Christopher M Dobson, Gabriele S Kaminski Schierle, and
Clemens F Kaminski. Direct observation of heterogeneous amyloid ﬁbril growth kinetics via two-color super-resolution
microscopy. Nano letters, 14(1):339–345, 2013.
[56] Jesper Ferkinghoﬀ-Borg, Jesper Fonslet, Christian Beyschau Andersen, Sandeep Krishna, Simone Pigolotti, Hisashi
Yagi, Yuji Goto, Daniel Otzen, and Mogens H Jensen. Stop-and-go kinetics in amyloid ﬁbrillation. Physical Review
E, 82(1):010901, 2010.
[57] Michael M W¨ordehoﬀ, Oliver Bannach, Hamed Shaykhalishahi, Andreas Kulawik, Stephanie Schiefer, Dieter Willbold,
Wolfgang Hoyer, and Eva Birkmann. Single ﬁbril growth kinetics of α-synuclein. Journal of molecular biology, 427(6):1428–


## Page 58


58
1435, 2015.
[58] Tuomas PJ Knowles, Christopher A Waudby, Glyn L Devlin, Samuel IA Cohen, Adriano Aguzzi, Michele Vendruscolo,
Eugene M Terentjev, Mark E Welland, and Christopher M Dobson. An analytical solution to the kinetics of breakable
ﬁlament assembly. Science, 326(5959):1533–1537, 2009.
[59] Tuomas PJ Knowles, Duncan A White, Adam R Abate, Jeremy J Agresti, Samuel IA Cohen, Ralph A Sperling, Erwin J
De Genst, Christopher M Dobson, and David A Weitz. Observation of spatial propagation of amyloid assembly from
single nuclei. Proceedings of the National Academy of Sciences, 108(36):14746–14751, 2011.
[60] Masato Kodaka. Interpretation of concentration-dependence in aggregation kinetics. Biophysical chemistry, 109(2):325–
332, 2004.
[61] Ravindra Kodali and Ronald Wetzel. Polymorphism in the intermediates and products of amyloid assembly. Current
opinion in structural biology, 17(1):48–57, 2007.
[62] Evan T Powers and David L Powers. Mechanisms of protein ﬁbril formation: nucleated polymerization with competing
oﬀ-pathway aggregation. Biophysical journal, 94(2):379–391, 2008.
[63] Johannes Diderik Van der Waals, Richard Threfall, John F Adair, and Friedrich Roth. The continuity of the liquid and
gaseous states. 1889.
[64] R Becker and W D¨oring. The kinetic treatment of nuclear formation in supersaturated vapors. Ann. Phys, 24(719):752,
1935.
[65] IAkov Ilich Frenkel. Kinetic theory of liquids. Dover Publications, 1955.
[66] Jens Lothe and G M Pound. Concentration of clusters in nucleation and the classical phase integral. The Journal of
Chemical Physics, 48(4):1849–1852, 1968.
[67] HJLER Reiss, JL Katz, and ER Cohen.
Translation–rotation paradox in the theory of nucleation.
The Journal of
Chemical Physics, 48(12):5553–5560, 1968.
[68] Ryoichi Kikuchi. The translation-rotation paradox in the nucleation theory. Journal of Statistical Physics, 1(2):351–375,
1969.
[69] Yumeng Shi, Wu Zhou, Ang-Yu Lu, Wenjing Fang, Yi-Hsien Lee, Allen Long Hsu, Soo Min Kim, Ki Kang Kim, Hui Ying
Yang, Lain-Jong Li, et al. Van der waals epitaxy of mos2 layers using graphene as growth templates. Nano letters,
12(6):2784–2791, 2012.
[70] FF Abraham. Homogeneous nucleation: The pretransition theory of vapor condensation, 1974.
[71] Pablo G Debenedetti. Metastable liquids: concepts and principles. Princeton University Press, 1996.
[72] Richard P Sear. Quantitative studies of crystal nucleation at constant supersaturation: experimental data and models.
CrystEngComm, 16(29):6506–6522, 2014.
[73] NHj Fletcher. Size eﬀect in heterogeneous nucleation. The Journal of chemical physics, 29(3):572–576, 1958.


## Page 59


59
[74] AI Hienola, PM Winkler, PE Wagner, H Vehkam¨aki, A Lauri, I Napari, and M Kulmala. Estimation of line tension and
contact angle from heterogeneous nucleation experimental data. The Journal of chemical physics, 126(9):094705, 2007.
[75] NS Tavare. Industrial crystallization: Process simulation. Analysis and Design, Plenum Press, New York, 1995.
[76] Fumio Oosawa and Michiki Kasai. A theory of linear and helical aggregations of macromolecules. Journal of molecular
biology, 4(1):10–21, 1962.
[77] Albrecht Wegner. Spontaneous fragmentation of actin ﬁlaments in physiological conditions. 1982.
[78] Yongting Wang, Sarah Petty, Amy Trojanowski, Kelly Knee, Daniel Goulet, Ishita Mukerji, and Jonathan King. Formation
of amyloid ﬁbrils in vitro from partially unfolded intermediates of human γc-crystallin. Investigative ophthalmology &
visual science, 51(2):672–678, 2010.
[79] Katrina J Binger, Chi LL Pham, Leanne M Wilson, Michael F Bailey, Lynne J Lawrence, Peter Schuck, and Geoﬀrey J
Howlett. Apolipoprotein c-ii amyloid ﬁbrils assemble via a reversible pathway that includes ﬁbril breaking and rejoining.
Journal of molecular biology, 376(4):1116–1129, 2008.
[80] Samuel IA Cohen, Michele Vendruscolo, Christopher M Dobson, and Tuomas PJ Knowles. Nucleated polymerisation in
the presence of pre-formed seed ﬁlaments. International journal of molecular sciences, 12(9):5844–5852, 2011.
[81] Albrecht Wegner and Paula Savko. Fragmentation of actin ﬁlaments. Biochemistry, 21(8):1909–1913, 1982.
[82] Jean-Christophe Rochet and Peter T Lansbury.
Amyloid ﬁbrillogenesis: themes and variations.
Current opinion in
structural biology, 10(1):60–68, 2000.
[83] Frank A Ferrone, James Hofrichter, HR Sunshine, and WA Eaton. Kinetic studies on photolysis-induced gelation of sickle
cell hemoglobin suggest a new mechanism. Biophysical journal, 32(1):361, 1980.
[84] Frank A Ferrone, James Hofrichter, and William A Eaton. Kinetics of sickle hemoglobin polymerization: I. studies using
temperature-jump and laser photolysis techniques. Journal of molecular biology, 183(4):591–610, 1985.
[85] Frank A Ferrone, James Hofrichter, and William A Eaton. Kinetics of sickle hemoglobin polymerization: Ii. a double
nucleation mechanism. Journal of molecular biology, 183(4):611–631, 1985.
[86] Shae B Padrick and Andrew D Miranker. Islet amyloid: phase partitioning and secondary nucleation are central to the
mechanism of ﬁbrillogenesis. Biochemistry, 41(14):4694–4703, 2002.
[87] Amy M Ruschak and Andrew D Miranker. Fiber-dependent amyloid formation as catalysis of an existing reaction pathway.
Proceedings of the National Academy of Sciences, 104(30):12341–12346, 2007.
[88] Georg Meisl, Xiaoting Yang, Erik Hellstrand, Birgitta Frohm, Julius B Kirkegaard, Samuel IA Cohen, Christopher M
Dobson, Sara Linse, and Tuomas PJ Knowles. Diﬀerences in nucleation behavior underlie the contrasting aggregation
kinetics of the aβ40 and aβ42 peptides. Proceedings of the National Academy of Sciences, 111(26):9384–9389, 2014.
[89] Erik Hellstrand, Barry Boland, Dominic M Walsh, and Sara Linse.
Amyloid β-protein aggregation produces highly
reproducible kinetic data and occurs by a two-phase process. ACS chemical neuroscience, 1(1):13–18, 2009.


## Page 60


60
[90] Samuel IA Cohen, Sara Linse, Leila M Luheshi, Erik Hellstrand, Duncan A White, Luke Rajah, Daniel E Otzen, Michele
Vendruscolo, Christopher M Dobson, and Tuomas PJ Knowles. Proliferation of amyloid-β42 aggregates occurs through
a secondary nucleation mechanism. Proceedings of the National Academy of Sciences, 110(24):9758–9763, 2013.
[91] Andrzej Granas and James Dugundji. Fixed point theory. Springer Science & Business Media, 2013.
[92] Samuel IA Cohen, Michele Vendruscolo, Christopher M Dobson, and Tuomas PJ Knowles. Nucleated polymerization
with secondary pathways. II. determination of self-consistent solutions to growth processes described by non-linear master
equations. The Journal of chemical physics, 135(6):065106, 2011.
[93] Frank Ferrone. Analysis of protein aggregation kinetics. Methods in enzymology, 309:256–274, 1999.
[94] Joan E Sanders, Barry S Goldstein, and Daniel F Leotta. Skin response to mechanical stress: adaptation rather than
breakdown-a review of the literature. Journal of rehabilitation research and development, 32:214–214, 1995.
[95] C F Lee. Thermal breakage of a discrete one-dimensional string. Physical Review E, 80:31134, 2009.
[96] SM Loveday, XL Wang, MA Rao, SG Anema, and Harjinder Singh. β-lactoglobulin nanoﬁbrils: Eﬀect of temperature
on ﬁbril formation kinetics, ﬁbril morphology and the rheological properties of ﬁbril dispersions. Food Hydrocolloids,
27(1):242–249, 2012.
[97] Chiu Fan Lee. Thermal breakage of a semiﬂexible polymer: breakage proﬁle and rate. Journal of Physics: Condensed
Matter, 27(27):275101, 2015.
[98] Peter Tessarz, Axel Mogk, and Bernd Bukau. Substrate threading through the central pore of the hsp104 chaperone as
a common mechanism for protein disaggregation and prion propagation. Molecular microbiology, 68(1):87–97, 2008.
[99] Li Zhu, Xu-Jia Zhang, Ling-Yun Wang, Jun-Mei Zhou, and Sarah Perrett. Relationship between stability of folding
intermediates and amyloid formation for the yeast prion ure2p: a quantitative analysis of the eﬀects of ph and buﬀer
system. Journal of molecular biology, 328(1):235–254, 2003.
[100] Neal D Hammer, Jens C Schmidt, and Matthew R Chapman. The curli nucleator protein, csgb, contains an amyloidogenic
domain that directs csga polymerization. Proceedings of the National Academy of Sciences, 104(30):12494–12499, 2007.
[101] Katja ˇSkerget, Andrej Vilfan, Maruˇsa Pompe-Novak, Vito Turk, Jonathan P Waltho, Duˇsan Turk, and Eva ˇZerovnik.
The mechanism of amyloid-ﬁbril formation by steﬁn b: Temperature and protein concentration dependence of the rates.
Proteins: Structure, Function, and Bioinformatics, 74(2):425–436, 2009.
[102] Wei-Feng Xue, Steve W Homans, and Sheena E Radford. Systematic analysis of nucleation-dependent polymerization
reveals new insights into the mechanism of amyloid self-assembly.
Proceedings of the National Academy of Sciences,
105(26):8926–8931, 2008.
[103] Neil Ferguson, John Berriman, Miriana Petrovich, Timothy D Sharpe, John T Finch, and Alan R Fersht. Rapid amyloid
ﬁber formation from the fast-folding ww domain fbp28. Proceedings of the National Academy of Sciences, 100(17):9814–
9819, 2003.


## Page 61


61
[104] Vladimir N Uversky, Jie Li, and Anthony L Fink. Metal-triggered structural transformations, aggregation, and ﬁbrillation
of human α-synuclein a possible molecular link between parkinson’s disease and heavy metal exposure.
Journal of
Biological Chemistry, 276(47):44284–44296, 2001.
[105] Liza Nielsen, Ritu Khurana, Alisa Coats, Sven Frokjaer, Jens Brange, Sandip Vyas, Vladimir N Uversky, and Anthony L
Fink. Eﬀect of environmental factors on the kinetics of insulin ﬁbril formation: elucidation of the molecular mechanism.
Biochemistry, 40(20):6036–6046, 2001.
[106] M Ballauﬀand BA Wolf. Degradation of chain molecules. 1. exact solution of the kinetic equations. Macromolecules,
14(3):654–658, 1981.
[107] M Ballauﬀand BA Wolf. Degradation of chain molecules. 2. thermodynamically induced shear degradation of dissolved
polystyrene. Macromolecules, 17(2):209–216, 1984.
[108] Masato Tanigawa, Masashi Suzuto, Kiyohiro Fukudome, and Kiwamu Yamaoka.
Changes in molecular weights and
molecular weight distributions of diﬀerently stranded nucleic acids after sonication: Gel permeation chromatography/low
angle laser light scattering evaluation and computer simulation. Macromolecules, 29(23):7418–7425, 1996.
[109] G´erald Gu´erin, Hai Wang, Ian Manners, and Mitchell A Winnik. Fragmentation of ﬁberlike structures: sonication studies
of cylindrical block copolymer micelles and behavioral comparisons to biological ﬁbrils. Journal of the American Chemical
Society, 130(44):14763–14771, 2008.
[110] TERRELL L Hill. Length dependence of rate constants for end-to-end association and dissociation of equilibrium linear
aggregates. Biophysical journal, 44(2):285, 1983.
[111] Liu Hong and Wen-An Yong. Simple moment-closure model for the self-assembly of breakable amyloid ﬁlaments. Bio-
physical journal, 104(3):533–540, 2013.
[112] Edwin T Jaynes. Information theory and statistical mechanics. Physical review, 106(4):620, 1957.
[113] Edwin T Jaynes. On the rationale of maximum-entropy methods. Proceedings of the IEEE, 70(9):939–952, 1982.
[114] Steve Press´e, Kingshuk Ghosh, Julian Lee, and Ken A Dill. Principles of maximum entropy and maximum caliber in
statistical physics. Reviews of Modern Physics, 85(3):1115, 2013.
[115] Thomas CT Michaels and Tuomas PJ Knowles.
Role of ﬁlament annealing in the kinetics and thermodynamics of
nucleated polymerization. The Journal of chemical physics, 140(21):214904, 2014.
[116] William P Esler, Evelyn R Stimson, Joan M Jennings, Harry V Vinters, Joseph R Ghilardi, Jonathan P Lee, Patrick W
Mantyh, and John E Maggio. Alzheimer’s disease amyloid propagation by a template-dependent dock-lock mechanism.
Biochemistry, 39(21):6288–6295, 2000.
[117] Phuong H Nguyen, Mai Suan Li, Gerhard Stock, John E Straub, and D Thirumalai.
Monomer adds to preformed
structured oligomers of aβ-peptides by a two-stage dock–lock mechanism. Proceedings of the National Academy of Sciences,
104(1):111–116, 2007.


## Page 62


62
[118] Thomas Scheibel, Jesse Bloom, and Susan L Lindquist. The elongation of yeast prion ﬁbers involves separable steps of
association and conversion. Proceedings of the National Academy of Sciences of the United States of America, 101(8):2287–
2292, 2004.
[119] M Bodenstein and H Lutkemeyer. Quasi-steady state assumption. z. Physics and Chemistry, 114, 1924.
[120] Sidney William Benson et al. Foundations of chemical kinetics. 1960.
[121] Leonor Michaelis and Maud L Menten. Die kinetik der invertinwirkung. Biochem. z, 49(333-369):352, 1913.
[122] Alexander K Buell, C´eline Galvagnion, Ricardo Gaspar, Emma Sparr, Michele Vendruscolo, Tuomas PJ Knowles, Sara
Linse, and Christopher M Dobson.
Solution conditions determine the relative importance of nucleation and growth
processes in α-synuclein aggregation. Proceedings of the National Academy of Sciences, 111(21):7671–7676, 2014.
[123] Margaret Sunde and Colin CF Blake. From the globular to the ﬁbrous state: protein structure and structural conversion
in amyloid formation. Quarterly reviews of biophysics, 31(01):1–39, 1998.
[124] Stanley B Prusiner. Novel proteinaceous infectious particles cause scrapie. Science, 216(4542):136–144, 1982.
[125] Jeﬀery W Kelly. The alternative conformations of amyloidogenic proteins and their multi-step assembly pathways. Current
opinion in structural biology, 8(1):101–106, 1998.
[126] Yanming Xing, Akihiro Nakamura, Tatsumi Korenaga, Zhanjun Guo, Junjie Yao, Xiaoying Fu, Takatoshi Matsushita,
Kumiko Kogishi, Masanori Hosokawa, Fuyuki Kametani, et al. Induction of protein conformational change in mouse
senile amyloidosis. Journal of Biological Chemistry, 277(36):33164–33169, 2002.
[127] Liu Hong, Xianghong Qi, and Yang Zhang. Dissecting the kinetic process of amyloid ﬁber formation through asymptotic
analysis. The Journal of Physical Chemistry B, 116(23):6611–6617, 2011.
[128] Scott A Peterson, Thomas Klabunde, Hilal A Lashuel, Hans Purkey, James C Sacchettini, and Jeﬀrey W Kelly. Inhibiting
transthyretin conformational changes that lead to amyloid ﬁbril formation.
Proceedings of the National Academy of
Sciences, 95(22):12956–12960, 1998.
[129] Sarah L Shammas, Gonzalo A Garcia, Satish Kumar, Magnus Kjaergaard, Mathew H Horrocks, Nadia Shivji, Eva
Mandelkow, Tuomas PJ Knowles, Eckhard Mandelkow, and David Klenerman. A mechanistic model of tau amyloid
aggregation based on direct observation of oligomers. Nature communications, 6, 2015.
[130] Chuang-Chung Lee, Arpan Nayak, Ananthakrishnan Sethuraman, Georges Belfort, and Gregory J McRae. A three-stage
kinetic model of amyloid ﬁbrillation. Biophysical journal, 92(10):3448–3458, 2007.
[131] Christian Beyschau Andersen, Hisashi Yagi, Mauro Manno, Vincenzo Martorana, Tadato Ban, Gunna Christiansen,
Daniel Erik Otzen, Yuji Goto, and Christian Rischel. Branching in amyloid ﬁbril growth. Biophysical journal, 96(4):1529–
1536, 2009.
[132] Monica M Pallitto and Regina M Murphy. A mathematical model of the kinetics of β-amyloid ﬁbril growth from the
denatured state. Biophysical journal, 81(3):1805–1822, 2001.


## Page 63


63
[133] Christopher M Dobson. Principles of protein folding, misfolding and aggregation. In Seminars in cell & developmental
biology, volume 15, pages 3–16. Elsevier, 2004.
[134] Leila M Luheshi, Damian C Crowther, and Christopher M Dobson. Protein misfolding and disease: from the test tube
to the organism. Current opinion in chemical biology, 12(1):25–31, 2008.
[135] Larissa A Munishkina, Elisa M Cooper, Vladimir N Uversky, and Anthony L Fink. The eﬀect of macromolecular crowding
on protein aggregation and amyloid ﬁbril formation. Journal of Molecular Recognition, 17(5):456–464, 2004.
[136] Andrea Magno, Amedeo Caﬂisch, and Riccardo Pellarin. Crowding eﬀects on amyloid aggregation kinetics. The Journal
of Physical Chemistry Letters, 1(20):3027–3032, 2010.
[137] AY Hung, C Haass, RM Nitsch, W Qiao Qiu, M Citron, RJ Wurtman, JH Growdon, and DJ Selkoe. Activation of protein
kinase c inhibits cellular production of the amyloid beta-protein. Journal of Biological Chemistry, 268(31):22959–22962,
1993.
[138] Deng-Shun Wang, Dennis W Dickson, and James S Malter. β-amyloid degradation and alzheimer’s disease. BioMed
Research International, 2006, 2006.
[139] Joseph D Buxbaum, Gopal Thinakaran, Vassilis Koliatsos, James OCallahan, Hilda H Slunt, Donald L Price, and San-
gram S Sisodia. Alzheimer amyloid protein precursor in the rat hippocampus: transport and processing through the
perforant path. The Journal of neuroscience, 18(23):9629–9637, 1998.
[140] Shermali Gunawardena and Lawrence SB Goldstein. Disruption of axonal transport and neuronal viability by amyloid
precursor protein mutations in drosophila. Neuron, 32(3):389–401, 2001.
[141] Christian Haass and Dennis J Selkoe.
Soluble protein oligomers in neurodegeneration: lessons from the alzheimer’s
amyloid β-peptide. Nature reviews Molecular cell biology, 8(2):101–112, 2007.
[142] Alfonso De Simone, Luciana Esposito, Carlo Pedone, and Luigi Vitagliano. Insights into stability and toxicity of amyloid-
like oligomers by replica exchange molecular dynamics analyses. Biophysical journal, 95(4):1965–1973, 2008.
[143] Dominic M Walsh and Dennis J Selkoe. Aβ oligomers–a decade of discovery. Journal of neurochemistry, 101(5):1172–1184,
2007.
[144] Marcus F¨andrich. Oligomeric intermediates in amyloid formation: structure determination and mechanisms of toxicity.
Journal of molecular biology, 421(4):427–440, 2012.
[145] Massimo Stefani. The oligomer species: Mechanistics and biochemistry. Amyloid Fibrils and Preﬁbrillar Aggregates:
Molecular and Biological Properties, pages 127–150, 2013.
[146] David H Small, Su San Mok, and Joel C Bornstein. Alzheimer’s disease and aβ toxicity: from top to bottom. Nature
Reviews Neuroscience, 2(8):595–598, 2001.
[147] Kenjiro Ono, Margaret M Condron, and David B Teplow. Structure–neurotoxicity relationships of amyloid β-protein
oligomers. Proceedings of the National Academy of Sciences, 106(35):14745–14750, 2009.


## Page 64


64
[148] Pamela T Wong, Joseph A Schauerte, Kathleen C Wisser, Hao Ding, Edgar L Lee, Duncan G Steel, and Ari Gafni.
Amyloid-β membrane binding and permeabilization are distinct processes inﬂuenced separately by membrane charge and
ﬂuidity. Journal of molecular biology, 386(1):81–96, 2009.
[149] Thomas L Williams and Louise C Serpell. Membrane and surface interactions of alzheimers aβ peptide–insights into the
mechanism of cytotoxicity. FEBS Journal, 278(20):3905–3917, 2011.
[150] Ricardo Capone, Felipe Garcia Quiroz, Panchika Prangkio, Inderjeet Saluja, Anna M Sauer, Mahealani R Bautista,
Raymond S Turner, Jerry Yang, and Michael Mayer. Amyloid-β-induced ion ﬂux in artiﬁcial lipid bilayers and neuronal
cells: resolving a controversy. Neurotoxicity research, 16(1):1–13, 2009.
[151] Masahiro Kawahara. Neurotoxicity of β-amyloid protein: oligomerization, channel formation and calcium dyshomeostasis.
Current pharmaceutical design, 16(25):2779–2789, 2010.
[152] Maarten FM Engel, Lucie Khemt´emourian, C´ecile C Kleijer, Hans JD Meeldijk, Jet Jacobs, Arie J Verkleij, Ben de Kruijﬀ,
J Antoinette Killian, and Jo WM H¨oppener. Membrane damage by human islet amyloid polypeptide through ﬁbril growth
at the membrane. Proceedings of the National Academy of Sciences, 105(16):6033–6038, 2008.
[153] Wei-Feng Xue, Andrew L Hellewell, Walraj S Gosal, Steve W Homans, Eric W Hewitt, and Sheena E Radford. Fibril
fragmentation enhances amyloid cytotoxicity. Journal of Biological Chemistry, 284(49):34272–34282, 2009.
[154] Angelo Demuro, Martin Smith, and Ian Parker.
Single-channel ca2+ imaging implicates aβ1–42 amyloid pores in
alzheimers disease pathology. The Journal of cell biology, 195(3):515–524, 2011.
[155] Joseph A Schauerte, Pamela T Wong, Kathleen C Wisser, Hao Ding, Duncan G Steel, and Ari Gafni. Simultaneous
single-molecule ﬂuorescence and conductivity studies reveal distinct classes of aβ species on lipid bilayers. Biochemistry,
49(14):3031–3039, 2010.
[156] Hyunbum Jang, Fernando Teran Arce, Ricardo Capone, Srinivasan Ramachandran, Ratnesh Lal, and Ruth Nussinov.
Misfolded amyloid ion channels present mobile β-sheet subunits in contrast to conventional ion channels. Biophysical
journal, 97(11):3029–3037, 2009.
[157] Arjan Quist, Ivo Doudevski, Hai Lin, Rushana Azimova, Douglas Ng, Blas Frangione, Bruce Kagan, Jorge Ghiso, and
Ratnesh Lal. Amyloid ion channels: a common structural link for protein-misfolding disease. Proceedings of the National
Academy of Sciences of the United States of America, 102(30):10427–10432, 2005.
[158] HAI Lin, Rajinder Bhatia, and Ratneshwar Lal. Amyloid β protein forms ion channels: implications for alzheimers disease
pathophysiology. The FASEB Journal, 15(13):2433–2444, 2001.
[159] Yinon Shafrir, Stewart Durell, Nelson Arispe, and H Robert Guy. Models of membrane-bound alzheimer’s abeta peptide
assemblies. Proteins: Structure, Function, and Bioinformatics, 78(16):3473–3487, 2010.
[160] Benedetta Bolognesi, Janet R Kumita, Teresa P Barros, Elin K Esbjorner, Leila M Luheshi, Damian C Crowther, Mark R
Wilson, Christopher M Dobson, Giorgio Favrin, and Justin J Yerbury. Ans binding reveals common features of cytotoxic


## Page 65


65
amyloid species. ACS chemical biology, 5(8):735–740, 2010.
[161] Heidi Olzscha, Sonya M Schermann, Andreas C Woerner, Stefan Pinkert, Michael H Hecht, Gian G Tartaglia, Michele
Vendruscolo, Manajit Hayer-Hartl, F Ulrich Hartl, and R Martin Vabulas. Amyloid-like aggregates sequester numerous
metastable proteins with essential cellular functions. Cell, 144(1):67–78, 2011.
[162] Henry W Querfurth and Frank M LaFerla. Mechanisms of disease. N Engl J Med, 362(4):329–344, 2010.
[163] Angelo Demuro, Erene Mina, Rakez Kayed, Saskia C Milton, Ian Parker, and Charles G Glabe. Calcium dysregulation
and membrane disruption as a ubiquitous neurotoxic mechanism of soluble amyloid oligomers.
Journal of Biological
Chemistry, 280(17):17294–17300, 2005.
[164] David M Holtzman, Alison Goate, Jeﬀrey Kelly, and Reisa Sperling. Mapping the road forward in alzheimers disease.
Science translational medicine, 3(114):114ps48–114ps48, 2011.
[165] Dennis J Selkoe. Resolving controversies on the path to alzheimer’s therapeutics. Nature medicine, 17(9):1060–1065,
2011.
[166] Yuesong Gong, Lei Chang, Kirsten L Viola, Pascale N Lacor, Mary P Lambert, Caleb E Finch, Grant A Kraﬀt, and
William L Klein. Alzheimer’s disease-aﬀected brain: presence of oligomeric aβ ligands (addls) suggests a molecular basis
for reversible memory loss. Proceedings of the National Academy of Sciences, 100(18):10417–10422, 2003.
[167] Frank M LaFerla. Calcium dyshomeostasis and intracellular signalling in alzheimer’s disease. Nature Reviews Neuroscience,
3(11):862–872, 2002.
[168] Paul R Turner, Kate OConnor, Warren P Tate, and Wickliﬀe C Abraham. Roles of amyloid precursor protein and its
fragments in regulating neural activity, plasticity and memory. Progress in neurobiology, 70(1):1–32, 2003.
[169] Liu Hong, Ya-Jing Huang, and Wen-An Yong. A kinetic model for cell damage caused by oligomer formation. Biophysical
journal, 109:1338–1346, 2015.
[170] Sonia M Gregory, Allison Cavenaugh, Velvet Journigan, Antje Pokorny, and Paulo FF Almeida. A quantitative model
for the all-or-none permeabilization of phospholipid vesicles by the antimicrobial peptide cecropin a. Biophysical journal,
94(5):1667–1680, 2008.
[171] Sonia M Gregory, Antje Pokorny, and Paulo FF Almeida. Magainin 2 revisited: a test of the quantitative model for the
all-or-none permeabilization of phospholipid vesicles. Biophysical journal, 96(1):116–131, 2009.
[172] Henry Eyring. The activated complex in chemical reactions. The Journal of Chemical Physics, 3(2):107–115, 1935.
[173] Eric V Anslyn and Dennis A Dougherty. Modern physical organic chemistry. University Science Books, 2006.
[174] Celia Cabaleiro-Lago, Fiona Quinlan-Pluck, Iseult Lynch, Stina Lindman, Aedin M Minogue, Eva Thulin, Dominic M
Walsh, Kenneth A Dawson, and Sara Linse.
Inhibition of amyloid β protein ﬁbrillation by polymeric nanoparticles.
Journal of the American Chemical Society, 130(46):15437–15443, 2008.
[175] Seong Il Yoo, Ming Yang, Jeﬀrey R Brender, Vivekanandan Subramanian, Kai Sun, Nam Eok Joo, Soo-Hwan Jeong,


## Page 66


66
Ayyalusamy Ramamoorthy, and Nicholas A Kotov. Inhibition of amyloid peptide ﬁbrillation by inorganic nanoparticles:
functional similarities with proteins. Angewandte Chemie International Edition, 50(22):5110–5115, 2011.
[176] Yi-Hung Liao, Yu-Jen Chang, Yuji Yoshiike, Yun-Chorng Chang, and Yun-Ru Chen. Negatively charged gold nanoparticles
inhibit alzheimer’s amyloid-β ﬁbrillization, induce ﬁbril dissociation, and mitigate neurotoxicity. Small, 8(23):3631–3639,
2012.
[177] Chunjuan Huang, Han Cheng, Shufeng Hao, Hui Zhou, Xujia Zhang, Jianen Gao, Qi-Hong Sun, Hongyu Hu, and Chih-
chen Wang. Heat shock protein 70 inhibits α-synuclein ﬁbril formation via interactions with diverse intermediates. Journal
of molecular biology, 364(3):323–336, 2006.
[178] Krzysztof Liberek, Agnieszka Lewandowska, and Szymon Zietkiewicz. Chaperones in control of protein disaggregation.
The EMBO journal, 27(2):328–335, 2008.
[179] Li-Qiong Xu, Si Wu, Alexander K Buell, Samuel IA Cohen, Li-Jun Chen, Wan-Hui Hu, Sarah A Cusack, Laura S Itzhaki,
Hong Zhang, Tuomas PJ Knowles, et al. Inﬂuence of speciﬁc hsp70 domains on ﬁbril formation of the yeast prion protein
ure2. Phil. Trans. R. Soc. B, 368(1617):20110410, 2013.
[180] Samuel IA Cohen, Paolo Arosio, Jenny Presto, Firoz Roshan Kurudenkandy, Henrik Biverst˚al, Lisa Dolfe, Christopher
Dunning, Xiaoting Yang, Birgitta Frohm, Michele Vendruscolo, et al. A molecular chaperone breaks the catalytic cycle
that generates toxic aβ oligomers. Nature structural & molecular biology, 22(3):207–213, 2015.
[181] Lev Davidovich Landau and EM Lifshitz. Statistical physics, part i. Course of theoretical physics, 5:468, 1980.
[182] Fabio Librizzi and Christian Rischel. The kinetic behavior of insulin ﬁbrillation is determined by heterogeneous nucleation
pathways. Protein science, 14(12):3129–3134, 2005.
[183] Pengzhen Tan and Liu Hong. Modeling ﬁbril fragmentation in real-time. The Journal of chemical physics, 139(8):084904,
2013.
[184] Shao-Yun Fu, Chee-Yoon Yue, Xiao Hu, and Yiu-Wing Mai. Characterization of ﬁber length distribution of short-ﬁber
reinforced thermoplastics. Journal of materials science letters, 20(1):31–33, 2001.
[185] Thorsten P¨oschel, Nikolai V Brilliantov, and Cornelius Fr¨ommel.
Kinetics of prion growth.
Biophysical journal,
85(6):3460–3474, 2003.
[186] Albert Tarantola. Inverse problem theory and methods for model parameter estimation. siam, 2005.
[187] Thomas CT Michaels, Gonzalo A Garcia, and Tuomas PJ Knowles. Asymptotic solutions of the oosawa model for the
length distribution of bioﬁlaments. The Journal of chemical physics, 140(19):194906, 2014.
[188] Sergei K Lando. Lectures on generating functions, volume 23. American mathematical society Providence, RI, 2003.
[189] Thomas CT Michaels, Pernille Yde, Julian CW Willis, Mogens H Jensen, Daniel Otzen, Christopher M Dobson, Alexan-
der K Buell, and Tuomas PJ Knowles. The length distribution of frangible bioﬁlaments. The Journal of chemical physics,
143(16):164901, 2015.


## Page 67


67
[190] Liu Hong. Link the ﬂuorescence and TEM studies on amyloid ﬁber formation – to reconstruct the ﬁber length distribution
based on the knowledge of moments evolution. arXiv preprint arXiv:1212.4555, 2012.
[191] Melanie R Nilsson. Techniques to study amyloid ﬁbril formation in vitro. Methods, 34(1):151–160, 2004.
[192] Ritu Khurana, Chris Coleman, Cristian Ionescu-Zanetti, Sue A Carter, Vinay Krishna, Rajesh K Grover, Raja Roy, and
Shashi Singh. Mechanism of thioﬂavin t binding to amyloid ﬁbrils. Journal of structural biology, 151(3):229–238, 2005.
[193] Matthew Biancalana and Shohei Koide. Molecular mechanism of thioﬂavin-t binding to amyloid ﬁbrils. Biochimica et
Biophysica Acta (BBA)-Proteins and Proteomics, 1804(7):1405–1412, 2010.
[194] Hironobu Naiki, Keiichi Higuchi, Masanori Hosokawa, and Toshio Takeda. Fluorometric determination of amyloid ﬁbrils
in vitro using the ﬂuorescent dye, thioﬂavine t. Analytical biochemistry, 177(2):244–249, 1989.
[195] H Naiki, K Higuchi, K Nakakuki, and T Takeda. Kinetic analysis of amyloid ﬁbril polymerization in vitro. Laboratory
investigation; a journal of technical methods and pathology, 65(1):104–110, 1991.
[196] Michael Jackson and Henry H Mantsch. The use and misuse of ftir spectroscopy in the determination of protein structure.
Critical reviews in biochemistry and molecular biology, 30(2):95–120, 1995.
[197] John T Pelton and Larry R McLean.
Spectroscopic methods for analysis of protein secondary structure.
Analytical
biochemistry, 277(2):167–176, 2000.
[198] Norma J Greenﬁeld. Using circular dichroism spectra to estimate protein secondary structure. Nature protocols, 1(6):2876–
2890, 2006.
[199] Guiyang Li, Ping Zhou, Zhengzhong Shao, Xun Xie, Xin Chen, Honghai Wang, Lijuan Chunyu, and Tongyin Yu. The
natural silk spinning process. European Journal of Biochemistry, 268(24):6600–6606, 2001.
[200] Bruce J Berne and Robert Pecora. Dynamic light scattering: with applications to chemistry, biology, and physics. Courier
Corporation, 2000.
[201] SR Aragon and R Pecora. Theory of dynamic light scattering from polydisperse systems. The Journal of Chemical
Physics, 64(6):2395–2404, 1976.
[202] Bettce J Berne. Interpretation of the light scattering from long rods. Journal of molecular biology, 89(4):755–758, 1974.
[203] S Rigden John. Macmillan Encyclopedia of Physics. Simon & Schuster, Macmillan, 1996.
[204] Tomasz Kowalewski and David M Holtzman. In situ atomic force microscopy study of alzheimers β-amyloid peptide on
diﬀerent substrates: New insights into mechanism of β-sheet formation. Proceedings of the National Academy of Sciences,
96(7):3688–3693, 1999.
[205] R Ward, K Jennings, Robert JEPRAS, William NEVILLE, D Owen, Julie HAWKINS, Gary CHRISTIE, J Davis, Ashley
GEORGE, E Karran, et al. Fractionation and characterization of oligomeric, protoﬁbrillar and ﬁbrillar forms of β-amyloid
peptide. Biochem. J, 348:137–144, 2000.
[206] Ritu Khurana, Cristian Ionescu-Zanetti, Maighdlin Pope, Jie Li, Liza Nielson, Marina Ram´ırez-Alvarado, Lynn Regan,


## Page 68


68
Anthony L Fink, and Sue A Carter. A general model for amyloid ﬁbril assembly based on morphological studies using
atomic force microscopy. Biophysical journal, 85(2):1135–1144, 2003.
[207] Tadato Ban, Daizo Hamada, Kazuhiro Hasegawa, Hironobu Naiki, and Yuji Goto. Direct observation of amyloid ﬁbril
growth monitored by thioﬂavin t ﬂuorescence. Journal of Biological Chemistry, 278(19):16462–16465, 2003.
[208] Tadato Ban, Masaru Hoshino, Satoshi Takahashi, Daizo Hamada, Kazuhiro Hasegawa, Hironobu Naiki, and Yuji Goto.
Direct observation of aβ amyloid ﬁbril growth and inhibition. Journal of molecular biology, 344(3):757–767, 2004.
[209] Tadato Ban, Keiichi Yamaguchi, and Yuji Goto. Direct observation of amyloid ﬁbril growth, propagation, and adaptation.
Accounts of chemical research, 39(9):663–670, 2006.
[210] Georg Meisl, Julius B Kirkegaard, Paolo Arosio, Thomas CT Michaels, Michele Vendruscolo, Christopher M Dobson,
Sara Linse, and Tuomas PJ Knowles. Molecular mechanisms of protein aggregation from global ﬁtting of kinetic models.
Nature protocols, 11(2):252–272, 2016.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1609_01569v1_statistical_mechanics_and_kinetics_of_amyloid_fibrillation
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1609_01569V1_STATISTICAL_MECHANICS_AND_KINETICS_OF_AMYLOID_FIBRILLATION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

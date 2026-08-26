---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1008.2327v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1008.2327v1_Density_functional_theory_for_strongly-interacting_electrons__Perspectives_for_P

> Source: 1008.2327v1_Density_functional_theory_for_strongly-interacting_electrons__Perspectives_for_P.pdf

> Pages: 38

---


## Page 1


Density functional theory for strongly-interacting electrons:
Perspectives for Physics and Chemistry
Paola Gori-Giorgia and Michael Seidlb
a Department of Theoretical Chemistry and Amsterdam Center for Multiscale Modeling,
FEW, Vrije Universiteit, De Boelelaan 1083,
1081HV Amsterdam, The Netherlands
b Institute of Theoretical Physics, University of Regensburg, D-93040 Regensburg, Germany
(Dated: February 28, 2022)
Abstract
Improving the accuracy and thus broadening the applicability of electronic density functional theory
(DFT) is crucial to many research areas, from material science, to theoretical chemistry, biophysics
and biochemistry. In the last three years, the mathematical structure of the strong-interaction limit
of density functional theory has been uncovered, and exact information on this limit has started
to become available. The aim of this paper is to give a perspective on how this new piece of exact
information can be used to treat situations that are problematic for standard Kohn-Sham DFT. One
way to use the strong-interaction limit, more relevant for solid-state physical devices, is to deﬁne a
new framework to do practical, non-conventional, DFT calculations in which a strong-interacting
reference system is used instead of the traditional non-interacting one of Kohn and Sham. Another
way to proceed, more related to chemical applications, is to include the exact treatment of the
strong-interaction limit into approximate exchange-correlation energy density functionals in order
to describe diﬃcult situations such as the breaking of the chemical bond.
1
arXiv:1008.2327v1  [cond-mat.str-el]  13 Aug 2010


## Page 2


I.
INTRODUCTION
Density functional theory (DFT),1 in its Kohn-Sham (KS) formulation,2 has been a real
breakthrough for electronic structure calculations, allowing to treat systems much larger
than those accessible to wavefunction methods. KS DFT, together with its extension to
time-dependent (TD) phenomena (TDDFT),3 made possible the theoretical study of an
incredible huge number of chemical, physical, and biological processes.
The key idea of KS DFT is an exact mapping2 between the physical, interacting, many-
electron system and a model system of non-interacting fermions with the same density.
Only one term, the so called exchange-correlation (xc) energy functional (containing all
the complicated many-body eﬀects) needs to be approximated. Although in principle this
functional is unique (or “universal”), a large number of approximations have been developed
in the last twenty years, both by chemists and physicists, often targeting diﬀerent systems,
diﬀerent properties, and diﬀerent phenomena. In a way, the emergence of such a “functional
zoology” simply reﬂects the intrinsic diﬃculty of building a single general approximation able
to recognize and capture, for each given system or process, the many-body eﬀects relevant
for its description.
Despite the large number of available approximate functionals and of their successful
applications, there are still important cases in which KS DFT can fail, which is why the quest
for better xc functionals continues to be a very active research ﬁeld (for recent reviews see,
e.g., Refs. 4–8). For example, present-day KS DFT encounters problems in the treatment of
near-degeneracy eﬀects (rearrangement of electrons within partially ﬁlled levels, important
for describing bond dissociation but also equilibrium geometries, particularly for systems
with d and f unsaturated shells), in the description of van der Waals long-range interactions
(relevant, for example, for biomolecules and layered materials), and of localization eﬀects
due to strong electronic correlations (as those occurring in Mott insulators and in low-density
nanodevices, but also occurring in bond dissociation). These problems can hamper more
or less severely (and sometimes in an unpredictable way) a given calculation, depending
on their relative importance with respect to other eﬀects that are better captured by the
available approximate functionals.
This work primarily aims at describing a diﬀerent approach to some of the unsolved
problems of present-day DFT, focussing on the treatment of systems with strong spatial
2


## Page 3


correlations. The key idea is to recognize that the non-interacting Kohn-Sham reference
system is not always the best choice. The main idea of Kohn and Sham, which can be
summarized as “Let’s solve a model system having the same density of the physical one
and approximate the remaining missing energy with a density functional”, can be rigorously
generalized to model systems diﬀerent from the non-interacting one of Kohn and Sham.9 This
freedom can be used to choose model systems that are able to capture some of the relevant
eﬀects (for example near-degeneracy or strong correlations), whose computational cost is
still low, and for which it is easier to design approximate density functionals that recover
the missing energy. For example, in recent years this strategy has been used to address the
problems of near-degeneracy eﬀects and van der Waals interactions by using a model system
with a weak long-range-only interaction (and having the same density of the physical system,
as in KS theory). The preliminary results are so far very successful,10–17 as proved by the
growing number of research groups that are now working on the practical implementation
of this “short-range DFT - long-range wavefunction” (srDFT-lrWF) method.13–23
Strong correlations, however, remain a big challenge for DFT, and in many cases are
also beyond the reach of the srDFT-lrWF method. By “strong electronic correlation” we
mean here the study of systems in which the electron-electron interaction largely dominates
over the kinetic energy, creating strong spatial correlations. In such cases, it may happen
that we need very many (billions) of Slater determinants for a proper description of the
relevant physics, with all the natural occupation numbers becoming very small. For these
situations both the non-interacting KS system and the weak-interacting hamiltonian of the
srDFT-lrWF method are not the best starting point: they are not able to capture the
physics of the system under study so that trying to describe the missing energy with an
approximate density functional is often a daunting task (or, alternatively, the srDTF-lrWF
method becomes as expensive as solving the Schr¨oedinger equation for the physical system).
In order to “visualize” this concept, Fig. 1 schematically represents the diﬀerence between
near-degeneracy eﬀects, characterized by the presence of few more important states with re-
spect to the occupied KS orbitals (that can be captured with a weak-interacting hamiltonian,
like the one used in the srDFT-lrWF method), and strong correlations, where very many
(billions) of Slater determinants are needed for a proper description of the relevant physics
(notice that here we are not talking about getting the energy with high accuracy, but only
about describing the right physics: once we have a model hamiltonian which is able to do
3


## Page 4


that, the idea is, as in KS theory, to correct the energy with a density functional). In this
ﬁgure levels drawn with a solid line represent the occupied KS states (labeled with “KS”),
and dotted levels the empty ones. On the left, we have a typical near-degenerate system,
in which few empty states strongly couple to the ground state: including them would be
enough to describe the right physics of the system, although for an accurate energy many
more states would be needed. On the right we have a strongly correlated system in which
billion of states are strongly coupled to the ground state. From the point of view of the ex-
act ﬁrst-order density matrix, the ﬁrst case corresponds to having some natural occupation
numbers ni close to 1/2 (if we consider natural spin orbitals with 0 ≤ni ≤1), while the
second case corresponds to having all ni ≪1. Of course this simple, schematic, picture may
be very diﬀerent if we use a spin-unrestricted formalism to deﬁne the KS system (see also
Sec. VI A 2), instead of a restricted one, as mostly used throughout this paper.
Prototype systems displaying near-degeneracy eﬀects are the Be isoelectronic series
(where the 2s and the 2p KS levels become more and more degenerate as the atomic number
Z increases), and the H2 molecule along its dissociation curve, where the σg and σu KS
energies get closer and closer as the molecule is stretched. These two simple examples are
paradigmatic of many situations occurring in the study of chemical and physical problems,
from heavy elements to the stretching of the chemical bond in general. A simple example
of strong electronic correlation are low density nanodevices such as quantum dots. As the
electronic density is lowered, spatial correlations between the electrons become stronger and
stronger, and, as shown in Refs. 24,25 for a simple model consisting of two electrons in an
harmonic potential, all the natural occupation numbers become very small, indicating the
presence of an inﬁnite number of important states. In real systems studied in experiments, in
which low-density electrons are conﬁned at the interfaces of semiconductor heterostructures,
this phenomenon leads, for example, to intriguing patterns in the addition energy spectra,26
which are suggestive of strong spatial correlations and have never been fully explained.
Of course, in general there are very many diﬀerent physical situations which need a huge
number of Slater determinants to be described, and many corresponding ansatz wavefunc-
tions, models or methods that can do that, each one being able to capture diﬀerent phys-
ical phenomena. Typical examples are the density-matrix renormalization group (DMRG)
method, the Laughlin wavefunction, the unrestricted Hartree-Fock plus symmetry restora-
tion wavefunction, and dynamical mean ﬁeld theory.
4


## Page 5


near-degeneracy
strong correlation
} KS
} KS
few more 
important states 
to capture the 
right physics
many more 
important states 
to capture the 
right physics
some ni ∼1/2
all ni ≪1
FIG. 1: Schematic illustration of the diﬀerence between near-degeneracy eﬀects, in which few more
important states with respect to the Kohn-Sham occupied levels are needed in order to capture
the right physics, and strongly-correlated systems, which need billions of Slater determinants. The
ﬁrst case is usually characterized by the presence of natural occupation numbers ni close to 1/2,
while the second case often corresponds to natural occupations that are all very small. In this
ﬁgure levels drawn with a solid line represent the occupied KS states, and dotted levels the empty
ones. On the left, we have a typical near-degenerate system, in which few empty states strongly
couple to the ground state: including them would be enough to describe the right physics of the
system, although for an accurate energy many more states would be needed. On the right we have
a strongly correlated system in which billion of states are strongly coupled to the ground state.
The main object of this paper is to review and discuss the perspectives of a new way to
deal with the case of strong spatial correlations in a DFT framework. For a given N-electron
system with density ρ(r), we construct, in a mathematical rigorous way, a model system
consisting of N electrons having the same density ρ(r) and maximum possible correlation
between the N electronic positions.
We call this model system the “strictly correlated
electron” (SCE) model, and we use it as a complementary alternative to the KS ansatz
5


## Page 6


for DFT. We also propose simple approximate density functionals to recover the diﬀerence
between the energies of the physical system and of the SCE model, following the same ideas
used in KS DFT. The SCE model is able to capture the inﬁnitely many Slater determinants
needed to describe strong spatial correlations, and, as we shall see in the next sections, it
is the natural counterpart of the KS ansatz. It also provides a rigorous lower bound for the
exact exchange-correlation functional of KS DFT, simply because the electrons cannot be
more correlated than the SCE state in a given one electron density ρ(r).
The paper is organized as follows. After reviewing the basics of DFT in Sec. II, in order
to emphasize the analogies and the diﬀerences between the usual KS DFT and the “SCE
DFT”, we parallel, throughout Secs. III-VI, the two approaches. Thus, Secs. III-VI contain
a KS part, which quickly reviews the main formalism pertinent to the KS ansatz, and a
SCE part, which explains how the same concepts can be generalized using the SCE model
as a reference system. In Sec. VII we report ﬁrst applications of the SCE-DFT method
to few-electron quantum dots at low density.
Although, as previously mentioned, bond
dissociation can be viewed as a near-degeneracy eﬀect (which can be described by the weak
interacting hamiltonian of the srDFT-lrWF method or, e.g., by density matrix functional
theory27,28 or by a mixture of Hartree-Fock and Hartree-Fock-Bogoliubov methods29), it
is also characterized by strong spatial correlations between the electrons involved in the
stretched bond, whose physics can be captured by the SCE limit. In Section VIII, thus,
we discuss possible ways to include the exact information contained in the SCE limit into
functionals useful for chemical applications, with emphasis on bond dissociation. The last
Sec. IX is devoted to conclusions and perspectives.
II.
THE HOHENBERG-KOHN FUNCTIONAL AND ITS BASIC PROPERTIES
We begin by deﬁning the problem and reviewing the basic properties of the Hohenberg-
Kohn functional.
We generally consider here systems of N interacting electrons, bound by a given external
potential v(r) in D-dimensional space (r ∈RD). The corresponding Hamiltonian,
ˆHα[v] = ˆT + α ˆVee +
N
X
i=1
v(ri),
(2.1)
6


## Page 7


with the universal operators of the kinetic energy,
ˆT = −ℏ2
2m
N
X
i=1
∂2
∂r2
i
,
(2.2)
and the Coulomb repulsion between the electrons,
ˆVee = e2
2
N
X
i,j=1
1 −δij
|ri −rj|,
(2.3)
has four independent parameters: the particle number N, the spatial dimension D, the
RD →R function v = v(r) of the external potential, and a tunable dimensionless interaction
strength α ≥0 (which will be set to its realistic value α = 1 at the end). Unlike α and v,
the parameters N and D will not be indicated explicitly in our notation.
Due to the Ritz principle, the ground-state energy of ˆHα[v] is given by
Eα[v] = min
Ψ→N⟨Ψ| ˆHα[v]|Ψ⟩,
(2.4)
where the condition Ψ →N addresses all (normalized) spin-1
2 fermionic wave functions in
D-dimensional space,
Ψ = Ψ(r1, ..., rN; σ1, ..., σN),
(2.5)
with ri ∈RD and spin variables σi. A considerably simpler function is the particle density,
ρ(r) = N
X
σ1,...,σN
Z
dDr2...dDrN
Ψ(r, r2, ..., rN; σ1, ..., σN)

2
,
(2.6)
which is normalized according to
R
dDrρ(r) = N. In terms of this function as the variable,
the universal Hohenberg-Kohn (HK) functional of DFT is deﬁned as30,31
Fα[ρ] = min
Ψ→ρ⟨Ψ| ˆT + α ˆVee|Ψ⟩≥0
(2.7)
where the condition Ψ →ρ now addresses only those fermionic N-electron wave functions
Ψ that are, via Eq. (2.6), associated with the same given particle density ρ = ρ(r). Here,
“universal” means that Fα[ρ] does not depend on the parameter v = v(r). [It does, however,
depend on the spatial dimension D and on the particle number N =
R
dDrρ(r).] If the
functional Fα[ρ] was known explicitly in terms of the density ρ, the ground-state energy of
Eq. (2.4) could be obtained by a considerably simpler minimization procedure,
Eα[v] = min
ρ→N
n
Fα[ρ] +
Z
dDrρ(r)v(r)
o
(2.8)
7


## Page 8


where the condition ρ →N now addresses all (non-negative) density functions ρ(r) that are
normalized to the same given particle number N. Eq. (2.8) is called the (second part of
the) HK theorem [the ﬁrst part being the statement that the external potential v(r) in the
Hamiltonian of Eq. (2.1) is unambiguously ﬁxed by its ground-state density ρ(r)].
Introducing a Lagrangian multiplier µ to account for the condition ρ →N (and writing
Fα=1[ρ] ≡F[ρ]), we obtain from Eq. (2.8) the Euler equation
δF[ρ]
δρ(r) + v(r) = µ,
(2.9)
to be solved for the wanted density function ρ(r). Since F[ρ] is not known explicitly in terms
of the density ρ, the crucial problem of DFT is to ﬁnd approximate ways of treating F[ρ]
and its functional derivative δF[ρ]/δρ(r).
Clearly, the complexity of the many-body problem is hidden in the HK functional Fα[ρ].
An equivalent functional is
eFβ[ρ] = min
Ψ→ρ⟨Ψ|β ˆT + ˆVee|Ψ⟩= βF1/β[ρ].
(2.10)
Since a minimizing wave function here at the same time minimizes Eq. (2.7) for the inter-
action strength α = 1/β, the parameter β may be dubbed the “interaction weakness”.
For a given density ρ and interaction strength α in Eq. (2.7), let Ψα[ρ] be a minimizing
wave function. With Tα[ρ] = ⟨Ψα[ρ]| ˆT|Ψα[ρ]⟩and V (α)
ee [ρ] = ⟨Ψα[ρ]|ˆVee|Ψα[ρ]⟩we have
Fα[ρ] = Tα[ρ] + αV (α)
ee [ρ].
(2.11)
We make here the usual assumption that Ψα[ρ] depends smoothly on the parameter α. (This
assumption may break down, e.g., for a uniform electron gas at low density going through
a ferromagnetic phase transition). Then, Fα[ρ] is diﬀerentiable with respect to α and, due
to the minimum property, Eq. (2.7), the Hellmann-Feynman theorem implies32–34
d
dαFα[ρ] = ⟨Ψα[ρ]|ˆVee|Ψα[ρ]⟩.
(2.12)
In particular, we can write Eq. (2.11), in terms of the universal functionals35
V (α)
ee [ρ] ≡d
dαFα[ρ],
Tα[ρ] ≡Fα[ρ] −α d
dαFα[ρ].
(2.13)
An immediate consequence of Eq. (2.12) is the coupling-constant integral32–34
F1[ρ] −F0[ρ] =
Z 1
0
dα V (α)
ee [ρ].
(2.14)
8


## Page 9


In an analogous way, the corresponding formula for the functional eFβ[ρ] is obtained,
F1[ρ] −eF0[ρ] =
Z 1
0
dβ eTβ[ρ]
(2.15)
(notice that eF1[ρ] = F1[ρ]).
Here, eTβ[ρ] = ⟨eΨβ[ρ]| ˆT|eΨβ[ρ]⟩where eΨβ[ρ] = Ψα=1/β[ρ] is
a minimizing wave function in Eq. (2.10), eTβ[ρ] = Tα=1/β[ρ]. Substituting β = α−1, we
obtain36,37
F1[ρ] −eF0[ρ] =
Z ∞
1
dα
α2 Tα[ρ].
(2.16)
We deﬁne a density ρ to be ground-state-(α, v)-representable if there exists a single-
particle external potential vα[ρ](r) (whose existence is not always granted38) such that ρ is
a ground-state density of the Hamiltonian
ˆHα[ρ] = ˆT + α ˆVee +
N
X
i=1
vα[ρ](ri).
(2.17)
In this case, Ψα[ρ] is a ground state of ˆHα[ρ]; the corresponding ground-state energy,
Eα[ρ] = Fα[ρ] +
Z
dDr vα[ρ](r)ρ(r),
(2.18)
however, can be degenerate.
Similarly, the Hamiltonian
ˆeHβ[ρ] = β ˆT + ˆVee +
N
X
i=1
evβ[ρ](ri),
evβ ≡βvα=1/β
(2.19)
has the ground state eΨβ[ρ] = Ψ1/β[ρ] and the ground-state energy
eEβ[ρ] = eFβ[ρ] +
Z
dDr evβ[ρ](r) ρ(r).
(2.20)
III.
ZERO AND STRICT COULOMB CORRELATION
A.
Non-interacting electrons (NIE)
The usual Kohn-Sham system corresponds to the non-interacting limit α = 0 of the HK
functional Fα[ρ],
F0[ρ] = lim
β→∞
1
β
eFβ[ρ] = min
Ψ→ρ⟨Ψ| ˆT|Ψ⟩≡Ts[ρ].
(3.21)
9


## Page 10


Being a ground state of the non-interacting Hamiltonian ˆHα=0[ρ], the minimizing wave
function Ψ0[ρ] = eΨ∞[ρ] = ΨNIE[ρ] is, in most cases, a single Slater determinant of N spin-
orbitals φi(r, σ) which obey the Kohn-Sham (KS) single-particle Schr¨odinger equations
n
−ℏ2
2me
∇2 + v0[ρ](r)
o
φi(r, σ) = ϵiφi(r, σ).
(3.22)
Consequently, Ts[ρ] is the kinetic energy of N =
R
dDrρ(r) non-interacting electrons in a
given ground-state density ρ = ρ(r). By construction, the KS potential v0[ρ](r) is such that
the orbitals reproduce the given density,
X
i,σ
|φi(r, σ)|2 = ρ(r).
(3.23)
Implicitly, in terms of these orbitals (rather than explicitly in terms of the density ρ itself),
Ts[ρ] is given by
Ts[ρ] = ℏ2
2me
X
i,σ
Z
dDr|∇φi(r, σ)|2.
(3.24)
Non-interacting electrons (NIE) have zero Coulomb correlation. For example, N = 2
such electrons in a given density ρ(r) have opposite spins and occupy the same spatial
orbital ψ(r) =
q
1
2ρ(r) (the situation can become more complicated if the corresponding
KS potential has a degenerate ground state, something that rarely happens for N = 2).
When their two positions are measured simultaneously, the results r1 and r2 are completely
uncorrelated – when only the partial result r1 is noticed while the result r2 is ignored or
hidden, its probability distribution is rigorously independent of the particular value of r1.
In this case, the expectation of ˆVee is given by
V (0)
ee [ρ] = e2
Z
dDr1
Z
dDr2
|ψ(r1)ψ(r2)|2
|r1 −r2|
= 1
2U[ρ]
(N = 2),
(3.25)
with the explicit density functional of the Hartree energy,
U[ρ] = e2
2
Z
dDr
Z
dDr′ ρ(r)ρ(r′)
|r −r′| .
(3.26)
If the electrons were repulsive bosons (b), an arbitrary number N of them could occupy the
same orbital ψ(r). In this case, Eq. (3.25) would be generalized to V (0)
ee [ρ] = V (0)
bb [ρ] where
V (0)
bb [ρ] = N −1
N
U[ρ]
(bosons).
(3.27)
10


## Page 11


For N ≥3, however, non-interacting electrons must occupy two or more diﬀerent orbitals.
Consequently, their positions can no longer be completely uncorrelated. This eﬀect is some-
times called Pauli correlation, since it is not caused by a true repulsive (Coulomb) force
between the electrons, but merely by the Pauli principle. As a result, the true value of
V (0)
ee [ρ] is for N ≥3 lower than the bosonic value of Eq. (3.27),
V (0)
ee [ρ] = U[ρ] + Ex[ρ] ≤N −1
N
U[ρ].
(3.28)
The exchange energy Ex[ρ] < 0 is another implicit density functional,
Ex[ρ] = −e2
2
X
i,j
δmis,mj
s
Z
dDr
Z
dDr′ψ∗
i (r)ψj(r)ψ∗
j(r′)ψi(r′)
|r −r′|
,
(3.29)
with φi(r, σ) = ψi(r)χmis(σ). In Eq. (3.28), the equal sign, implying Ex[ρ] = −1
N U[ρ], holds
for N ≤2, while Ex[ρ] < −1
N U[ρ] for N ≥3.
B.
Strictly correlated electrons (SCE)
In the case α > 0, the Coulomb repulsion between the electrons is turned on in the
Hamiltonian ˆHα[ρ] of Eq. (2.17). Now, the ground state Ψα[ρ] has, in addition to Pauli
correlation (for N ≥3), also true Coulomb correlation which is caused by a repulsive force
which lowers the value of V (α)
ee [ρ] as α grows. Here we consider the extreme limit α →∞of
inﬁnitely strong repulsion,39,40 which we call the “strictly correlated electrons” (SCE) limit,
lim
α→∞
1
αFα[ρ] = eF0[ρ] = min
Ψ→ρ⟨Ψ|ˆVee|Ψ⟩≡V SCE
ee
[ρ].
(3.30)
The functional V SCE
ee
[ρ] is the natural counterpart of the KS non-interacting kinetic energy
Ts[ρ] and was ﬁrst addressed about ten years ago,39,40 but only treated in an approximated
way, using physically motivated models.40,41 Only recently V SCE
ee
[ρ] and the square |Ψ∞[ρ]|2 =
|eΨ0[ρ]|2 = |ΨSCE[ρ]|2 of the corresponding minimizing wave function have been treated
exactly in Ref. 42, where the interested reader can ﬁnd more mathematical details.
In
the following, we summarize the basics of the SCE solution, describing the physics that is
captured by V SCE
ee
[ρ].
V SCE
ee
[ρ] corresponds to the lowest possible value of the expectation of the electron-electron
repulsion in a given density ρ(r). In other words, the functional V SCE
ee
[ρ] deﬁnes a classical
problem with a given smooth density. Thus, in contrast to Ψα[ρ] for ﬁnite α < ∞, the
11


## Page 12


limiting wave function Ψ∞[ρ] does no longer depend on the spin variables σ1, ..., σN, and,
since the limit is classical (even if it is an unusual classical problem because of the constraint
of the smooth density), we can only determine |Ψ∞[ρ]|2, which, in terms of the spatial
variables r1, ..., rN, is no longer a regular function, but rather a Dirac-type distribution,
describing electrons with strictly correlated positions. In practice, this means that the N
results ri ∈RD (i = 1, ..., N) of a simultaneous measurement of all electronic positions in
the distribution |Ψ∞[ρ]|2 are no longer independent of each other, but strictly related via N
so-called co-motion functions fi(r),
ri = fi(r)

i = 1, ..., N;
f1(r) ≡r

.
(3.31)
In other words, the position r1 of one electron ﬁxes the positions ri (i > 1) of all the others.
The co-motion functions obey the group properties42
n
f1(fn(r)), ..., fN(fn(r))
o
=
n
f1(r), ..., fN(r)
o
(n = 1, ..., N),
(3.32)
so that Eq. (3.31) does not conﬂict with the symmetry postulate on a wave function for
identical fermions. Moreover, as the position of one of the electrons determines the positions
of all the others, the probability of ﬁnding one electron at position r in the volume element
dDr must be the same of ﬁnding the ith electron at position fi(r) in the volume element
dDfi(r). This means that all the co-motion functions for a given N-electron density ρ = ρ(r)
must satisfy the diﬀerential equation42
ρ(fi(r))dDfi(r) = ρ(r)dDr
(i = 1, ..., N),
(3.33)
whose initial conditions are ﬁxed by making the corresponding V SCE
ee
[ρ], given by
V SCE
ee
[ρ] = e2
2
N
X
i,j=1
Z
dDr ρ(r)
N
1 −δij
|fi(r) −fj(r)|,
(3.34)
minimum.42. Thus, similarly to the N single-particle orbitals φi(r, σ) in the NIE Kohn-Sham
state, the co-motion functions fi(r) are ﬁxed by the given density function ρ = ρ(r).42
Equation (3.34) should be viewed as the counterpart of Eq. (3.24) which, also implicitly,
represents the density functional Ts[ρ] ≡T NIE[ρ] for the non-interacting kinetic energy in
terms of the orbitals φi(r, σ). The latter represent the counterpart of the co-motion functions
fi(r) in Eq. (3.34). The counterpart of Eqs. (3.28) and (3.29) for the functional V (0)
ee [ρ], in
12


## Page 13


0
 0.05
 0.1
 0.15
 0.2
 0.25
 0.3
 0.35
 0
 2
 4
 6
 8
 10  12  14
prob. r12
r12
H-
physical
KS
SCE
FIG. 2: The probability distribution for the electron-electron distance r12 for the H−anion calcu-
lated with a very accurate wavefunction for the physical system, with the “exact” Kohn-Sham (KS)
Slater determinant (built from a very accurate density), and with the strictly correlated electron
(SCE) construction. All quantities are in Hartree atomic units.
contrast, is the limit α →∞of Tα[ρ], which, as we shall see later, must be treated with some
care since it diverges but still yields a ﬁnite “ﬁrst-order” correction to the energy functional
V SCE
ee
[ρ].
The two functionals Ts[ρ] and V SCE
ee
[ρ] deﬁne two diﬀerent and complementary model
systems in which the one-electron density is the same. A simple way to grasp the very
diﬀerent physics captured by the two model systems is to look at the probability density
P(r12) of ﬁnding two electrons at a distance r12.
As an example, in Fig. 2 we report
this probability P(r12) for the H−anion calculated using a very accurate wavefunction for
the physical system (see Refs. 43,44 and references therein), using the Kohn-Sham non-
interacting Slater determinant (constructed from the same accurate density), and using the
SCE construction (see also Ref. 45). The three probabilities P(r12) correspond to three
systems having the same one-electron density, that is, the same probability to ﬁnd one
electron at r in the volume element d3r. As we see from Fig. 2, the probability distribution for
13


## Page 14


the electron-electron distance is very diﬀerent: in the KS system there is a higher probability
of ﬁnding the two electrons close to each other than in the physical system, in which there
is Coulomb repulsion. In the SCE state, the two electrons never get closer than a certain
distance r0 ≈4.2 a.u., and they avoid each other as much as possible without breaking the
constraint of being in the given one-electron density.
C.
Density scaling
For a given density ρ = ρ(r), we consider the usual continuous set of scaled densities
ρλ(r),
ρλ(r) = λDρ(λr)
(λ > 0).
(3.35)
The prefactor λD guarantees that
R
dDr ρλ(r) =
R
dDr ρ(r) for all λ > 0.
As the orbitals φi(r, σ) solve the KS equations Eq. (3.22) and yield in Eq. (3.23) the
density ρ(r), the scaled orbitals φ(λ)
i (r, σ) = λD/2φi(λr, σ) yield the scaled density ρλ(r),
N
X
i=1
X
σ
|φ(λ)
i (r, σ)|2 = ρλ(r),
(3.36)
and solve the modiﬁed KS equations
n
−ℏ2
2me
∇2 + v0[ρλ](r)
o
φ(λ)
i (r, σ) = ϵ(λ)
i φ(λ)
i (r, σ),
(3.37)
where v0[ρλ](r) = λ2v0[ρ](λr) and ϵ(λ)
i
= λ2ϵi. Therefore, Eq. (3.24) implies46
Ts[ρλ] = λ2Ts[ρ].
(3.38)
For completeness, we note that35,46
U[ρλ] = λU[ρ],
Ex[ρλ] = λEx[ρ],
V (0)
ee [ρλ] = λV (0)
ee [ρ].
(3.39)
Similarly, as the co-motion functions fi(r) solve the SCE equation (3.33) for the density
ρ(r), the scaled co-motion functions
f (λ)
i
(r) = 1
λfi(λr)
(3.40)
solve the corresponding equations for the scaled density ρλ(r). Consequently, Eq. (3.34)
implies the scaling behavior
V SCE
ee
[ρλ] = λV SCE
ee
[ρ].
(3.41)
14


## Page 15


We notice that the HK functional has a more involved scaling behavior,46
F[ρλ] = λ2Fα[ρ]
(α = λ−1),
(3.42)
which is an immediate consequence of Eq. (2.7) with Eqs. (2.2) and (2.3). Thus, for ﬁnite
α (0 < α < ∞), we could, without loss of generality, conﬁne ourselves to the case α = 1.
IV.
WEAK AND STRONG COULOMB CORRELATION
Dropping the subscripts α and the superscript (α) in Eq. (2.11), we now address the
realistic situation with interaction strength α = 1,
F[ρ] = T[ρ] + Vee[ρ].
(4.43)
Here, F[ρ] = Fα=1[ρ], etc. For N ≥2, the two contributions on the right-hand side obey the
relations
T[ρ] = ⟨Ψα=1[ρ]| ˆT|Ψα=1[ρ]⟩≥Ts[ρ] ≡min
Ψ→ρ⟨Ψ| ˆT|Ψ⟩≥0,
(4.44)
Vee[ρ] = ⟨Ψα=1[ρ]|ˆVee|Ψα=1[ρ]⟩≥V SCE
ee
[ρ] ≡min
Ψ→ρ⟨Ψ|ˆVee|Ψ⟩≥0.
(4.45)
(In the trivial case N = 1, of course, we have T[ρ] = Ts[ρ] > 0 and Vee[ρ] = V SCE
ee
[ρ] = 0.)
These inequalities hold, since the realistic wave function Ψα=1[ρ] is signiﬁcally diﬀerent from
each one of the two minimizing wave functions on the right-hand side, Ψα=0[ρ] = ΨNIE[ρ]
and Ψ∞[ρ] = ΨSCE[ρ], respectively. While the latter ones are characterized completely by N
single-particle orbitals φi(r, σ) or, respectively, by N co-motion functions fi(r), the realistic
wave function Ψα=1[ρ] is mathematically much more involved. Describing electrons with
ﬁnite Coulomb repulsion, it has neither zero nor strict, but rather some ﬁnite Coulomb
correlation, a situation which is much harder to describe mathematically.
The non-interacting kinetic energy Ts[ρ] in Eq. (4.44) can be considered as the zero-
point kinetic energy resulting (by the uncertainty principle) from the spatial conﬁnement
of non-interacting electrons in the density ρ = ρ(r). For interacting electrons (α = 1), this
zero-point energy is increased by Coulomb correlation, since one such electron, due to the
repulsion by the other ones, has less eﬀective space available than a non-interacting one
(α = 0) within the same given density ρ = ρ(r). Consequently, the resulting diﬀerence,
Tc[ρ] = T[ρ] −Ts[ρ] > 0,
(4.46)
15


## Page 16


is called kinetic energy due to correlation. [We note in passing that, as α →∞grows beyond
its realistic value α = 1, this zero-point energy grows indeﬁnitely, see Eq. (4.50) below.]
On the other hand, increasing Coulomb repulsion (α →∞) lowers the expectation of
the operator ˆVee (which is a measure for the average inverse distance |r −r′|−1 between two
electrons in the state Ψα[ρ]). The second inequality, Eq. (4.45), expresses the fact that this
lowering is maximum in the limit α →∞of strict correlation, while it is lesser in realistic
systems with α = 1 and ﬁnite correlation. Therefore, following Ref. 36, the diﬀerence
Vd[ρ] = Vee[ρ] −V SCE
ee
[ρ] > 0
(4.47)
is called decorrelation energy.37
Combining the fundamental scaling law of Eq. (3.42) with the expressions in Eq. (2.13),
one ﬁnds the individual scaling properties of the functionals T[ρ] and Vee[ρ],
T[ρλ] = λ2Tα[ρ],
Vee[ρλ] = λV (α)
ee [ρ]



(α = λ−1),
(4.48)
in contrast to Eqs. (3.38) and (3.41). From section III, we know the ﬁnite limits
lim
α→0 Tα[ρ] = Ts[ρ],
lim
α→0 V (α)
ee [ρ] = V (0)
ee [ρ],
lim
α→∞V (α)
ee [ρ] = V SCE
ee
[ρ].
(4.49)
In addition, we have the divergent limit47
α →∞:
Tα[ρ] →TZP[ρ]α1/2 + O(α0),
(4.50)
where TZP[ρ] is the leading coeﬃcient of the expansion describing zero-point oscillations
of strictly correlated electrons about the SCE limit.47 Consequently, the high-density limit
(HDL) of Eq. (4.48) reads
λ →∞:



T[ρλ] →λ2Ts[ρ] = Ts[ρλ],
Vee[ρλ] →λV (0)
ee [ρ] = V (0)
ee [ρλ].
(4.51)
In the low-density limit (LDL), in contrast, we have
λ →0 :



T[ρλ] →λ3/2TZP[ρ] = TZP[ρλ],
Vee[ρλ] →λV SCE
ee
[ρ] = V SCE
ee
[ρλ].
(4.52)
Here, we have used Eqs. (3.38), (3.39), (3.41), and the relation TZP[ρλ] = λ3/2TZP[ρ] from
Ref. 47.
16


## Page 17


Now, we see that the kinetic energy T[ρλ] in the HK functional
F[ρλ] = T[ρλ] + Vee[ρλ]
(4.53)
becomes dominant and approaches its non-interacting value Ts[ρλ] in the HDL (λ →∞),
while in the LDL (λ →0), the potential energy Vee[ρλ] becomes dominant and approaches its
strictly correlated limit V SCE
ee
[ρλ]. Therefore, we call an electron system with given ground-
state density ρ weakly correlated (WCOR), when T[ρ] ≫Vee[ρ] or, more precisely,
F[ρ] ⪆T[ρ] ⪆Ts[ρ] ≫Vee[ρ]
(4.54)
and strongly correlated (SCOR), when Vee[ρ] ≫T[ρ] or, more precisely,
F[ρ] ⪆Vee[ρ] ⪆V SCE
ee
[ρ] ≫T[ρ].
(4.55)
V.
APPROXIMATING THE HK FUNCTIONAL
A.
Exchange-correlation (xc) and kinetic-decorrelation (kd) energies
When the single-particle orbitals φi(r, σ) of Eq. (3.24) and the co-motion functions fi(r) of
Eq. (3.34) can be constructed rigorously for any given density ρ = ρ(r), the functionals Ts[ρ]
and V SCE
ee
[ρ] can be treated exactly. Consequently, there are two natural ways of partitioning
the HK functional F[ρ]. The usual one of Kohn and Sham,
F[ρ] = Ts[ρ] + EH
xc[ρ],
EH
xc[ρ] ≡Tc[ρ] + Vee[ρ],
(5.56)
treats Ts[ρ] exactly, and looks for an approximation to the remaining contribution EH
xc[ρ].
Since F[ρ] = F1[ρ] and Ts[ρ] = F0[ρ], Eq. (2.14) now reads
EH
xc[ρ] =
Z 1
0
dα V (α)
ee [ρ].
(5.57)
The KS DFT scheme works well for weakly and moderately correlated systems (WCOR).
For SCOR systems, where F[ρ] is dominated by V SCE
ee
[ρ], better results should be obtained
by partitioning the HK functional as
F[ρ] = V SCE
ee
[ρ] + Ekd[ρ],
Ekd[ρ] ≡T[ρ] + Vd[ρ],
(5.58)
17


## Page 18


with V SCE
ee
[ρ] to be treated exactly and Ekd[ρ] to be approximated. Eq. (2.15) now reads
Ekd[ρ] =
Z 1
0
dβ eTβ[ρ] ≡
Z ∞
1
dα
α2 Tα[ρ].
(5.59)
The natural counterpart of this so-called kinetic-decorrelation (kd) energy36,37 Ekd[ρ] is
the xc-Hartree energy EH
xc[ρ] of Eqs. (5.56,5.57). This functional is usually written as
EH
xc[ρ] = Exc[ρ] + U[ρ],
(5.60)
with the functional of the exchange-correlation (xc) energy,
Exc[ρ] = V (0)
ee [ρ] −U[ρ]
|
{z
}
Ex[ρ]
+ Vee[ρ] −V (0)
ee [ρ] + Tc[ρ]
|
{z
}
Ec[ρ]
,
(5.61)
where we have introduced the correlation energy Ec[ρ]. An equivalent representation is
Exc[ρ] =

T[ρ] −Ts[ρ]

+

Vee[ρ] −U[ρ]

.
(5.62)
Note also that
Ekd[ρ] = Ts[ρ] + Exc[ρ] −

V SCE
ee
[ρ] −U[ρ]

.
(5.63)
B.
Local-density approximation (LDA) for Exc[ρ] and Ekd[ρ]
A simple approximation to the functional Exc[ρ] or, equivalently, EH
xc[ρ] = Exc[ρ] + U[ρ]
is the local-density approximation (LDA),
ELDA
xc
[ρ] =
Z
dDr ρ(r) ϵ(D)
xc (rs(r)).
(5.64)
As a function of r, the dimensionless local density parameter rs(r) is given by
rs(r) =

1
ρ(r)BD
1/D
⇔
ρ(r) =
1
BD rs(r)D ,
(5.65)
where BD is the volume of a D-dimensional ball with radius aB = ℏ2/mee2. E.g.: B3 = 4π
3 a3
B,
B2 = πa2
B. The crucial quantity in Eq. (5.64) is ϵ(D)
xc (rs), the xc energy per particle in the
D-dimensional uniform electron gas with (uniform) density ¯ρ = (BDrD
s )−1.
The functions ϵ(D)
xc (rs) for D = 2, 3 are not known analytically, but accurate parametriza-
tions of numerical Quantum Monte Carlo (QMC) data are available. In the case D = 2,
the data and parametrization of Attaccalite et al.48 are nowadays widely used. For D = 3,
18


## Page 19


popular parametrizations of the Ceperley and Alder QMC data49 are the ones of Vosko, Wilk
and Nusair50 and of Perdew and Wang.51 Remarkably, the function ϵ(3)
xc (rs) can be interpo-
lated accurately between its high- (rs ≪1) and low-density (rs ≫1) limits, almost without
relying on any QMC input at all.52 Finally, for D = 1 parametrized QMC data of the ground
state energy of a uniform electron gas with regularized electron-electron interaction are also
available.53
Given ELDA
xc
[ρ], a corresponding LDA for Ekd[ρ] is readily obtained from Eq. (5.63),37
ELDA
kd
[ρ] =
Z
dDr ρ(r) ϵ(D)
kd (rs(r)),
(5.66)
with the kd energy per particle in the D-dimensional uniform electron gas,
ϵ(D)
kd (rs) = t(D)
s
(rs) + ϵ(D)
xc (rs) −a(D)
M
rs
.
(5.67)
The non-interacting kinetic energy t(D)
s
(rs) per particle in the uniform electron gas (in units
of 1 Ha = e2/aB = mee4/ℏ2) is known analytically,
t(2)
s (rs) = 1
2
(1 + ζ)2 + (1 −ζ)2
2r2
s
= 1 + ζ2
2r2
s
,
(5.68)
t(3)
s (rs) =
3
10
9π
4
2/3(1 + ζ)5/3 + (1 −ζ)5/3
2r2
s
,
(5.69)
and the coeﬃcient a(D)
M
determines the Madelung energy (in units of 1 Ha),
a(2)
M = −1.1061,
a(3)
M = −0.89593.
(5.70)
The Madelung energy
a(D)
M
rs
exactly corresponds to the thermodynamic limit (number of
particles and volume going to inﬁnity with the particle density kept ﬁxed) of V SCE
ee
[ρ]/N in
a uniform electron gas (with the usual cancellation between the Hartree term, the electron-
background and the background-background interaction energies). Thus, as in KS theory,
the LDA is uniquely deﬁned as the approximation that makes the method exact in the limit
of uniform density.
C.
Exact ﬁrst-order approximation for Exc[ρ] and Ekd[ρ]
In KS DFT the exact ﬁrst-order approximation for Exc[ρ] is the exchange energy of
Eq. (3.29), which, as said, is an implicit functional of the density through the KS orbitals.
19


## Page 20


The “ﬁrst-order” approximation for Ekd[ρ] corresponds to zero point (ZP) oscillations
around the SCE minimum.47 The proof that this is indeed the exact ﬁrst-order correction is
rather lengthy and the interested reader can ﬁnd all the details in Ref. 47.
Basically, in the SCE limit the total potential energy of a classical conﬁguration
Epot(r1, ..., rN) =
X
i<j
e2
|ri −rj| +
X
i
vSCE[ρ](ri) ,
(5.71)
where vSCE[ρ](r) is the external potential associated with the density ρ at zero kinetic en-
ergy, is constant on the D-dimensional subspace Ω0 = {f1(r), . . . , fN(r)} of the full ND-
dimensional conﬁguration space42 and is expected to have a minimum with respect to varia-
tions perpendicular to Ω0, implying that its Hessian has D eigenvectors with null eigenvalue
and ND −D eigenvectors with positive eigenvalue ω2
µ(r) at every point on Ω0.47 In terms
of these eigenvalues, the small β and the large α expansion of eTβ[ρ] deﬁned after Eq. (2.15)
and Tα[ρ] of Eq. (2.11) read
lim
β→0
eTβ[ρ] = β−1/2TZP[ρ] + O(β0)
(5.72)
lim
α→∞Tα[ρ] = α1/2TZP[ρ] + O(α0),
(5.73)
with
TZP[ρ] = 1
2
Z
dDr ρ(r)
N
ND−D
X
µ=1
ωµ(r)
2
.
(5.74)
Thus, as anticipated in Sec. IV, in the strict correlation limit the kinetic energy grows
indeﬁnitely. However, both Eqs. (5.72) and (5.73) when inserted in Eq. (5.59) yield the
ﬁnite result
EZP
kd [ρ] = 2 TZP[ρ] =
Z
dDr ρ(r)
N
ND−D
X
µ=1
ωµ(r)
2
,
(5.75)
which is the SCE counterpart of the exact exchange energy of Eq. (3.29) for KS theory. The
energy EZP
kd [ρ] has a highly non trivial functional dependence on ρ, so that its functional
derivative is not easily accessible.
20


## Page 21


VI.
EXACT TREATMENT OF Ts[ρ] OR V SCE
ee
[ρ]
A.
The Kohn-Sham approach (exact Ts[ρ])
1.
Spin-restricted formalism
With Eq. (5.56) for the HK functional F[ρ], the Euler equation Eq. (2.9) reads
δTs[ρ]
δρ(r) + Φ[ρ](r) + vxc[ρ](r) + v(r) = µ,
(6.76)
with the electrostatic potential
Φ[ρ](r) ≡δU[ρ]
δρ(r) = e2
Z
dDr′ ρ(r′)
|r −r′|
(6.77)
of the density ρ(r) and the xc potential,
vxc[ρ](r) ≡δExc[ρ]
δρ(r) .
(6.78)
When the approximation Eap
xc [ρ] used for Exc[ρ] is an explicit density functional, the cor-
responding functional derivative vap
xc[ρ](r) = δEap
xc [ρ]/δρ(r) can be evaluated for any given
density function ρ(r).
By varying the density through variations of the orbitals, Eq. (6.76) for interacting elec-
trons is formally equivalent to the corresponding equation for a system of non-interacting
electrons in the KS eﬀective external potential
vKS[ρ](r) = Φ[ρ](r) + vxc[ρ](r) + v(r).
(6.79)
Thus, the KS orbitals satisfy the equations
n
−ℏ2
2me
∇2 + vKS[ρ](r)
o
φi(r, σ) = ϵKS
i φi(r, σ),
(6.80)
which have to be solved self-consistently with Eq. (3.23).
Since the exchange-correlation functional must be approximated in practice, one obtains
an approximate ground-state energy for the physical interacting system, Eap
0
= Ts[ρ] +
(Eap
xc [ρ] + U[ρ]) +
R
dDrρ(r) v(r).
Employing in Eq. (6.80) the exact quantum-mechanical operator of the kinetic energy, the
functional Ts[ρ] is treated exactly here. Consequently, this approach works well in the case
of WCOR systems when Ts[ρ] is the dominant contribution to F[ρ]. For SCOR systems, in
21


## Page 22


contrast, we will analyze in the next section a complementary approach based on the exact
treatment of V SCE
ee
[ρ]. Before doing so, however, we brieﬂy review the widely used spin-DFT
(or unrestricted Kohn-Sham) formalism.
2.
Spin-unrestricted formalism
In practical calculations the spin-DFT version54 of KS DFT is widely used. Although
the Hoehenberg-Kohn functional only depends on the total density ρ(r), in spin DFT one
introduces the functional Ts[ρ↑, ρ↓],
Ts[ρ↑, ρ↓] =
min
Ψ→ρ↑,ρ↓⟨Ψ| ˆT|Ψ⟩,
(6.81)
which corresponds to the kinetic energy of a non-interacting system having given spin den-
sities ρ↑(r) and ρ↓(r), with
ρσ(r) = N
X
σ2,...,σN
Z
dDr2...dDrN
Ψ(r, r2, ..., rN; σ, σ2, ..., σN)

2
,
(6.82)
and ρ↑+ ρ↓= ρ. The functional Ts[ρ↑, ρ↓] can be used to decompose the HK functional as
F[ρ] = Ts[ρ↑, ρ↓] + U[ρ] + Exc[ρ↑, ρ↓] +
Z
dDr v(r) ρ(r),
(6.83)
where Exc[ρ↑, ρ↓] is deﬁned as the correction needed to make Eq. (6.83) exact. The idea is
to have a non-interacting system with the same spin densities of the true, interacting, one.
This constraint deﬁnes two eﬀective potentials vKS,↑[ρ](r) and vKS,↓[ρ](r), and two sets of
orbitals such that P
i |φi,σ(r)|2 = ρσ(r).
Notice that we have (for the exact functionals evaluated at the exact density and spin
densities) Ts[ρ↑, ρ↓] ≥Ts[ρ], Exc[ρ↑, ρ↓] ≤Exc[ρ], and Ts[ρ↑, ρ↓] + Exc[ρ↑, ρ↓] = Ts[ρ] + Exc[ρ].
Using the spin-unrestricted KS reference system instead of the restricted one allows to mimic
some correlation eﬀects, similarly to the spin-unrestricted Hartree Fock method.
B.
The SCE approach (exact V SCE
ee
[ρ])
The non-interacting functionals Ts[ρ] and Ts[ρ↑, ρ↓] require a self-consistent procedure for
their calculation. This is because the density (or the spin densities) is determined by the
KS orbitals by the simple equation P
i |φi(r)|2 = ρ(r), while determining the orbitals from
22


## Page 23


the density requires a highly non-trivial procedure (for which very many diﬀerent numerical
techniques have been proposed in the last years, e.g.,55–57).
The construction of the complementary functional V SCE
ee
[ρ] for strictly correlated electrons
for a given density ρ(r) can be simpler, because the density determines the co-motion func-
tions fi(r) via the diﬀerential equations (3.33). In other words, in the SCE case it is easier
to determine the co-motion functions from the density than to determine the density from
the co-motion functions. In particular, V SCE
ee
[ρ] has been directly constructed for spherically
symmetric densities,42 while algorithms to solve the SCE equations in the general case are
under study: a very promising way to proceed is to exploit the similarity between the SCE
problem and mass transportation theory.58
The problem of calculating V SCE
ee
[ρ] can be reformulated as42
V SCE
ee
[ρ] = min
ψ→ρ
Z
|ψ(r1, r2, . . . , rN)|2 X
j>j
1
|ri −rj|,
(6.84)
where |ψ|2 is the spatial part of the many-electron wavefunction. As said, in fact, in the
SCE case, the electrons are strongly distinguished by their relative positions, so that the spin
state (or more generally, the statistics) does not play a role.42 The functional V SCE
ee
[ρ] is thus
the same as the spin unrestricted functional V SCE
ee
[ρ↑, ρ↓] (of course with ρ↑+ ρ↓= ρ). This
means that also the exact kinetic and decorrelation functional Ekd[ρ] is the same in the spin
restricted and spin unrestricted formalism. However, when we deal with approximations for
Ekd[ρ] this might not be true. In Sec. VII B, we will compare the results for a quantum dot
with three electrons obtained by using the local spin density functional ELSD
kd [ρ↑, ρ↓] with
those from the LDA functional.
Since the co-motion functions can be constructed from the density, in the SCE ap-
proach we can obtain the many-electron energy by directly minimizing the expression
F[ρ]+
R
dDrv(r)ρ(r) with respect to the density function ρ(r), according to Eq. (2.8). To this
end, the HK functional F[ρ] must be partitioned as in Eq. (5.58) where an approximation
Eap
kd[ρ] is required for the functional Ekd[ρ],
Eap[v] = min
ρ→N
n
V SCE
ee
[ρ] + Eap
kd[ρ] +
Z
dDrv(r)ρ(r)
o
.
(6.85)
Unlike the KS equations, this approach should be particularly suitable for SCOR systems for
which the HK functional is dominated by V SCE
ee
[ρ]. In such cases, the density is dominated
by strong spatial correlations rather than by the quantum mechanical shells. In practical
23


## Page 24


calculations, the minimization of Eq. (6.85) can be carried out by expanding the density on
a suitable basis set or by using a grid. A simple example of such a calculation is reported
in the next Sec. VII A.
Another equation that the minimizing density must satisfy can be obtained by varying
the energy with respect to ρ(r):
δE[v]
δρ(r) = δV SCE
ee
[ρ]
δρ(r)
+ δEkd[ρ]
δρ(r) + v(r) = µ,
(6.86)
where µ is the chemical potential. Although the functional V SCE
ee
[ρ] depends on the density
in a rather complicated way via the co-motion functions [see Eq. (3.34)], its functional
derivative vSCE[ρ](r) ≡−δV SCE
ee
[ρ]
δρ(r)
satisﬁes the classical equilibrium equation42
∇vSCE[ρ](r) =
N
X
i=2
r −fi(r)
|r −fi(r)|3,
(6.87)
which has a very simple physical meaning: the potential vSCE[ρ](r) must compensate the net
force acting on the electron in r, resulting from the repulsion of the other N −1 electrons
at positions fi(r). The one-body potential vSCE[ρ](r) is the counterpart of the KS eﬀective
potential of Eq. (6.79) and corresponds to the Lagrange multiplier for the constraint Ψ →ρ
in the minimization of Eq. (3.30). Thus, another possibility to solve the SCE-DFT equations
is to look for the density ρ(r) that satisﬁes Eqs. (6.86), (6.87) and (3.34). This last way
to proceed, however, raises some questions about the uniqueness of the solution, questions
that will be addressed in future work.
VII.
SCE-DFT APPLIED TO FEW-ELECTRON QUANTUM DOTS
In this Section we report preliminary applications of the SCE-DFT method on simple
quantum dots models with few electrons.
Quantum dots are nanodevices in which the motion of electrons is quantized in all
three dimensions through the lateral conﬁnement of a high-mobility modulation-doped two-
dimensional electron gas in a semiconductor heterostructure (for a review, see, e.g.,59). Be-
cause the conﬁnement of electrons in these “artiﬁcial atoms” can be varied at will, they
have become a playground in which the basic physics of interacting electrons can be largely
explored and theoretical models can be tested. The number of conﬁned electrons can vary
24


## Page 25


from a few to several hundred, with smaller numbers of electrons becoming increasingly
technologically important in nandevices such as the single-electron transistor.
In quantum dots the correlation eﬀects between electrons need to be considered carefully
because the external conﬁnement can become much weaker than in real atoms, where the
independent electron model with mean-ﬁeld theories usually gives good results. As the con-
ﬁnement strength is lowered, the mutual Coulomb interaction becomes gradually dominant.
The physics of this regime can be thus much better captured by SCE-DFT than by tradi-
tional KS-DFT. Indeed, KS DFT has proved useful for studying quantum dots in the weakly
correlated regime (e.g.,59–63), while the medium and strongly-correlated regime, and in par-
ticular the cross-over from the Fermi liquid behavior to the Wigner-crystal-like state, has
only been accessible to wavefunction methods, e.g., conﬁguration interaction59,64,65 (only
for very small dots), Quantum Monte Carlo (e.g.,66–68) or unrestricted Hartree-Fock plus
symmetry restoration.69 Here we explore with SCE-DFT the regime of weak conﬁnement
(strong correlation), where state-of-the-art KS-DFT breaks down.
We thus consider a simple quantum-dot model consisting of N electrons in two dimensions
(2D) laterally conﬁned by a parabolic potential:
ˆH = −ℏ2
2m∗
N
X
i=1
∇2
i + e2
ϵ
N
X
i=1
N
X
j=i+1
1
|ri −rj| + m∗ω2
2
N
X
i=1
r2
i ,
(7.88)
where m∗is the eﬀective mass and ϵ the dielectric constant.
For now we only analyze single dots for which we obtain circularly symmetric densities,
ρ(r) = ρ(r). In this case, the problem of determining V SCE
ee
[ρ] can be separated into an
angular part and a radial part.42 The distance r from the center of the dot of one of the
electrons can be freely chosen, and it then determines the distances from the center of all the
other N −1 electrons via radial co-motion functions fi(r), as well as all the relative angles
θij(r) between the electrons.42 The radial co-motion functions fi(r) can be constructed as
follows.42 Deﬁne an integer index k running for odd N from 1 to (N −1)/2, and for even N
from 1 to (N −2)/2. Then
f2k(r) =



N −1
e (2k −Ne(r)) r ≤a2k
N −1
e (Ne(r) −2k) r > a2k
f2k+1(r) =



N −1
e (Ne(r) + 2k)
r ≤aN−2k
N −1
e (2N −2k −Ne(r)) r > aN−2k,
(7.89)
25


## Page 26


where ai = N −1
e (i),
Ne(r) =
Z r
0
2π xρ(x) dx,
(7.90)
and N −1
e (y) is the inverse function of Ne(r). For odd N, these equations give all the needed
N −1 radial co-motion functions, while for even N we have to add the last function,
fN(r) = N −1
e (N −Ne(r)).
(7.91)
The relative angles θij(r) between the electrons can be found by minimizing numerically the
electron-electron repulsion energy P
i>j[fi(r)2 + fj(r)2 −2fi(r)fj(r) cos θij]−1/2. The radial
co-motion functions of Eqs. (7.89)-(7.91) satisfy Eq. (3.33) for 2D circularly symmetric ρ,
2π fi(r)ρ(fi(r)) |f ′
i(r)| dr = 2π rρ(r) dr,
(7.92)
and, together with the minimizing angles θij(r), yield the minimum expectation of ˆVee.42
Physically, the solution of Eqs. (7.89)-(7.91) makes the N electrons always be in N diﬀerent
circular shells, each of which contains, on average in the quantum mechanical problem (at
α = 1), one electron. In the SCE limit, the electrons become strictly correlated, and all
ﬂuctuations are suppressed (see, e.g.,70): the space is divided into N regions, each of which
always contains exactly one electron.
A.
The case N = 2
In this case the minimizing angle is always θ12(r) = π and there is only one co-motion
function given by
f2(r) = N −1
e (2 −Ne(r)),
(7.93)
with f2(f2(r)) = r, thus ensuring the equivalence of the two electrons.
We switch to eﬀective Hartee units (ℏ= 1, a∗
B =
ϵ
m∗aB = 1, e = 1, m∗= 1), and we
deﬁne f(r) ≡f2(r), so that
V SCE
ee
[ρ] =
Z ∞
0
dr 2π r ρ(r)
N
1
r + f(r) =
Z a1
0
dr 2π r
ρ(r)
r + f(r),
(7.94)
where we have used the fact that, since the electrons are indistinguishable, integrating from
0 to ∞is equivalent to integrate N times from 0 to a1 = N −1
e (1). This is a characteristic of
the SCE limit: the space is divided in N equivalent regions, so that to calculate the energy
26


## Page 27


we only need to treat one of them. In a way, the SCE limit seems to become more “local”,
a characteristic which may prove very useful if we deal with approximations. However, we
also have to keep in mind that, although for an exact evaluation of V SCE
ee
[ρ] we need indeed
only one of the N equivalent regions, in order to ﬁnd how to divide the space in those N
regions we need often to perform a classical minimization over the whole space. This will
become clearer in the next example with N = 3 electrons.
The exact “ﬁrst-order” or zero-point energy is, in this case, given by
EZP
kd [ρ] =
Z a1
0
dr πr ρ(r) [ω1(r) + ω2(r)] ,
(7.95)
with
ω1(r) =
s
r2 + f(r)2
rf(r) (r + f(r))3
(7.96)
ω2(r) =
s
2 (1 + f ′(r)2)
−f ′(r) (r + f(r))3
(7.97)
In Ref. 37 we have evaluated the energy functional Eap[v] = V SCE
ee
[ρ] + Eap
kd[ρ] +
R
dDrv(r)ρ(r) using the exact input densities from Ref. 71, and we have compared the results
with standard KS-LDA ones (notice that for two-dimensional electronic structure calcula-
tions LDA is still the most widely used functional). At this postfunctional level we have found
that, as expected, for large values of the conﬁning parameter ω (corresponding to higher
densities) the KS LDA result is superior to the SCE-DFT. However, as ω becomes smaller
(which corresponds to lowering the density and thus approaching the strongly-correlated
regime), the SCE-DFT results with its approximations for Eap
kd[ρ] become better and better,
highly outperforming KS-LDA. These results are summarized in Fig. 3, where we report
the absolute % error on the total energy as a function of the conﬁnement parameter ω for
KS-LDA and for SCE-DFT with Eap
kd[ρ] = 0 (curve labeled SCE), with Eap
kd[ρ] = ELDA
kd
[ρ] of
Eq. (5.66) (SCE-LDA), and with Eap
kd[ρ] = EZP
kd [ρ] of Eq. (5.75) (SCE-ZP). For the ground
state energy of the 2D electron gas (which deﬁnes the LDA functional) we have used the
data and parametrization of Attaccalite et al.48 We see from Fig. 3 that for ω ≲0.007 the
SCE-ZP result is the most accurate. The much simpler SCE-LDA is also very reasonable in
this regime, reducing the error of KS-LDA by a factor 5-10.
The next step is to perform self-consistent SCE-DFT calculations, in which the density
is determined by minimizing the energy functional. Here we report very preliminary results
27


## Page 28


0
 5
 10
 15
 20
 25
 30
 35
 40
 0.001
 0.01
 0.1
 1
% error on E[!]
" (effective Hartree)
KS-LDA
SCE
SCE-LDA
SCE-ZP
FIG. 3: The absolute % error on the total energy as a function of the conﬁnement parameter ω
made by the functional Eap[v] = V SCE
ee
[ρ] + Eap
kd[ρ] +
R
dDrv(r)ρ(r) with Eap
kd[ρ] = 0 (SCE), with
Eap
kd[ρ] = ELDA
kd
[ρ] of Eq. (5.66) (SCE-LDA), and with Eap
kd[ρ] = EZP
kd [ρ] of Eq. (5.75) (SCE-ZP).
The results obtained with standard KS-LDA are also reported. In this ﬁgure all calculations are
done at the postfunctional level only.
obtained by parametrizing the density with a set of Ng gaussians:
ρ{p}(r) = C−1
 Ng
X
i=1
ci e−b2
i r2
!2
,
(7.98)
where {p} denotes the set of the 2Ng variational parameters {bi, ci; i = 1, . . . Ng}. The
constant C ensures that ρ(r) is normalized to N = 2 electrons, and the functional form
guarantees that ρ(r) ≥0 everywhere. As an example, here we consider two cases with small
conﬁning parameter, ω = 0.0072846 and ω = 0.00221088, for which we ﬁnd that Ng = 3
gaussians are enough to accurately reproduce the exact density (when the ﬁtted densities
are inserted in Eap[v] the error with respect to the energy obtained with the exact densities
is ∼0.01%).
We consider only the simple SCE-LDA functional and perform the direct
28


## Page 29


0
 0.02
 0.04
 0.06
 0.08
 0.1
 0.12
 0
 10
 20
 30
 40
 50
 60
2! r "(r)
r
# = 0.0072846
exact
SCE-LDA
 0
 0.01
 0.02
 0.03
 0.04
 0.05
 0.06
 0.07
 0
 20
 40
 60
 80
 100
2! r "(r)
r
# = 0.00221088
exact
SCE-LDA
FIG. 4: Radial densities for N = 2 electrons in a two-dimensional model quantum dot for two
diﬀerent values of the conﬁning parameter ω. The exact values71 are compared with the results
obtained by the direct minimization of the energy functional SCE-LDA of Eq. (7.99). Eﬀective
Hartree atomic units are used. The corresponding total energies have relative errors, respectively,
of 5.4% and 4.4%.
minimization
Eap[v] = min
{p}
n
V SCE
ee
[ρ{p}] + ELDA
kd
[ρ{p}] +
Z
dDrv(r)ρ{p}(r)
o
(7.99)
with respect to the parameters {p}. This way of proceeding is probably not the best one both
in terms of eﬃciency and accuracy, but the aim here is only to show a proof of principle.
Better procedures are currently under study. The minimizing densities are compared in
Fig. 4 with the exact ones obtained from the solution given in Ref. 71.
Although the
densities obtained are quite reasonable, it is evident that the LDA approximation for the
functional Ekd[ρ] has a tendency to give densities that are too diﬀuse. The total energies
obtained in this way are quite accurate, with errors of 5.4% (for ω = 0.0072846) and 4.4%
(for ω = 0.00221088), corresponding, respectively, to absolute errors of 3 mH∗and 1 mH∗.
B.
The case N = 3
In this case we have two co-motion functions, f2(r) and f3(r), and two relative angles
that have to be minimized numerically for each value of the distance r ∈[0, a1] of one of
the electrons from the center of the dot. Notice that if, say, electron 1 is in the circular
29


## Page 30


shell 0 ≤r ≤a1, then electron 2 is in the shell a1 ≤f2(r) ≤a2, and electron 3 is in
a2 ≤f3(r) < ∞. Thus, even if we only need to compute the minimizing angles for r ∈[0, a1],
we explore the whole space where ρ(r) ̸= 0 through the positions of the other N −1 electrons.
The quantum dot with N = 3 electrons is also a useful example to discuss the spin state
in the framework of SCE-DFT. Accurate wavefunction methods, in fact, (see, e.g.,64,67) ﬁnd
that the ground state for the N = 3 dot with ω ≲0.05 is fully spin polarized. As discussed in
Sec. VI B, the functional V SCE
ee
[ρ], being essentially classic, is independent of the spin state.
The exact functional Ekd[ρ] should thus be the same as the exact functional Ekd[ρ↑, ρ↓], when
the exact density or the exact spin densities are used. When constructing approximations,
however, one could obtain better results with Ekd[ρ↑, ρ↓], as in KS-DFT.
Here we consider only the SCE-LDA and SCE-LSD functionals, and we apply them at the
postfunctional level using as input the Diﬀusion Monte Carlo densities from Refs. 66,68. We
study the values ω = 0.01562, 0.005 and 0.001, which already lie in the regime where KS-LDA
orbitals become diﬃcult to obtain (notice that the KS-LDA results of Fig. 3 were obtained
at the postfunctional level, using the exact densities as input). As said, we explore the two
options ELDA
kd
[ρ] and ELSD
kd [ρ↑, ρ↓] for which we use the parametrization of the 2D electron
gas energy of Attaccalite et al.48 This functional is based on accurate Diﬀusion Monte Carlo
(DMC) data predicting a weakly ﬁrst order transition from the unpolarized gas to the
fully polarized state at rs ≈26. Even if the existence of this transition has been recently
questioned in Ref. 72, we stick here to the original Attaccalite et al. parametrization. Since
the densities involved are quite low, corresponding often to rs > 26, the correct deﬁnition
(within the chosen parametrization) of the LDA functional consists in taking in each point
of space the ground state energy of the electron gas with the same density, i.e.,
ELDA
kd
[ρ] =
Z
dDr ρ(r) {ϵkd (rs(r), ζ = 0) θ (25.56 −rs(r)) + ϵkd (rs(r), ζ = 1) θ (rs(r) −25.56)} ,
(7.100)
where rs(r) = (πρ(r))−1/2, ζ = (ρ↑−ρ↓)/ρ, and θ is the Heaviside step function. For the
values of the conﬁnement parameter ω considered here (for which the ground state of the
dot is fully polarized), instead, the “exact” LSD functional (i.e., the one which has not only
the exact local density in each point of space, but also the exact local spin densities) is
ELSD
kd [ρ↑, 0] =
Z
dDr ρ(r)ϵkd(rs(r), ζ = 1).
(7.101)
30


## Page 31


TABLE I: Relative % errors on the total energy of a model two-dimensional quantum dot consisting
of 3 electrons conﬁned in an harmonic potential vext(r) = 1
2ω2r2. Columns as follows: SCE are
the results obtained by setting Ekd[ρ] = 0, SCE-LDA are those obtained by using ELDA
kd
[ρ] of
Eq. (7.100), and SCE-LSD are those obtained by using ELSD
kd [ρ↑, 0] of Eq. (7.101).
ω
SCE SCE-LDA SCE-LSD
0.01562 −15.1
3.4
3.9
0.005
−10.6
3.6
3.7
0.001
−6.7
2.8
2.8
In Table I we report the % errors on the total energies (with respect to the DMC energies)
obtained with the two functionals. We also show the results corresponding to Eap
kd[ρ] = 0,
labeled “SCE”. We see that the quality of the two local approximations is rather good, with
the LSD results slightly worse than the LDA ones for ω = 0.01562 and ω = 0.005. This
is due to the fact that for these values of the conﬁning parameter ω, rs(r) is often still
smaller that 26, so that a lower energy is obtained by considering the true ground state of
the electron gas. At ω = 0.001, we have rs(r) always greater than 26 so that LDA and
LSD become the same. In other words, the SCE-LDA functional predicts a transition to
the fully polarized state at a much lower ω with respect to the one predicted by accurate
wavefunction methods. This transition in the SCE-LDA method entirely depends on the
delicate physics of the 2D uniform electron gas, and it is thus questionable in view of the
latest results of Ref. 72.
This simple example shows that the next step for the construction of functionals useful
for SCE-DFT is probably by considering simple exchange models, which would allow to
distinguish between diﬀerent spin states, generalizing to nonuniform densities what has
been done for the uniform electron gas in Ref. 73.
VIII.
IS THE SCE LIMIT RELEVANT FOR CHEMICAL APPLICATIONS?
The results of the previous Section suggest that the SCE formalism can have an impact
on solid-state devices involving electron gas in low dimensional systems (quantum wires,
dots, point contacts, etc.), in the low-density, strongly-interacting regime, where traditional
31


## Page 32


KS DFT is not of much use. It is however less evident whether the SCE limit could be also
relevant for applications in chemistry.
If we consider the simplest chemical system, the H2 molecule, we see that, as we stretch
the chemical bond, the energy and physics of the system is exactly described by the SCE
limit, as electrons in a stretched bond have strong spatial correlations (see, e.g., Fig. 11 of
Ref. 74). This feature is very interesting and promising, since the stretching of the chemical
bond is one of the typical situations in which restricted KS-DFT encounters problems, being
unable to describe the strong correlation occurring between the electrons involved in a single
or in a multiple bond. Thus, the SCE limit contains useful exact information that is usually
missed by state-of-the-art (restricted) KS-DFT. However, when we deal with real chemical
systems the situation is diﬀerent from that of the simple H2 molecule, since only the electrons
involved in the stretched bonds are strongly correlated. The SCE limit applied to the whole
system would give much too low energies, producing serious overcorrelation. In other words,
we cannot expect the SCE-DFT scheme to work for chemistry, where often both the orbital
description and strong spatial correlation are important at the same time.
What we could do, instead, is trying to include the exact information contained in the SCE
limit into approximate exchange-correlation functionals. Attempts in this direction have
been done in the past, leading to the construction of the interaction-strength-interpolation
(ISI) functional.39,75 As shown in Eq. (5.57), the exchange-correlation energy of KS-DFT is
given by (in this section we use Hartree atomic units)
Exc[ρ] =
Z 1
0
dαV (α)
ee [ρ] −U[ρ].
(8.102)
Since the functional V (α)
ee [ρ] approaches the SCE limit as α →∞, the idea of the ISI
functional is to construct the α-dependence of Wα[ρ] = V (α)
ee [ρ] −U[ρ] by interpolating
between the α →0 (exchange energy and second-order G¨orling-Levy perturbation energy76
EGL2
c
[ρ]),
Wα→0[ρ] = V (α→0)
ee
[ρ] −U[ρ] = Ex[ρ] + 2 α EGL2
c
[ρ] + O(α2),
(8.103)
and the α →∞limits (SCE plus ZP oscillations47),
Wα→∞[ρ] = V (α→∞)
ee
[ρ] −U[ρ] = V SCE
ee
[ρ] −U[ρ] + TZP[ρ]
√α
+ O(α−q)
q ≥5
4.
(8.104)
However, this way of proceeding leads to serious size-consistency errors. The size-consistency
problem of the ISI functional is related to the fact that the interpolation is done on the global
32


## Page 33


quantity Wα[ρ]. Moreover, when the ISI was ﬁrst proposed an exact treatment of the SCE
limit was not available, so that the functional relied on physical approximations for the SCE
and ZP energies.41,75
As a possible way out, the exact solution of the SCE limit, now available, makes accessible
not only global, but also local quantities. This new access to local quantities could be used to
construct local interpolations along the DFT adiabatic connection, restoring size consistency
(for critical reviews on the size-consistency issue in DFT see also77,78). We thus rewrite
Eq. (8.102) in terms of an energy density wα(r; [ρ]),
Exc[ρ] =
Z
dDrρ(r)
Z 1
0
dα wα(r; [ρ]),
(8.105)
with
Z
dDrρ(r)wα(r; [ρ]) = Wα[ρ] = V (α)
ee [ρ] −U[ρ].
(8.106)
The idea is then to use the energy densities wα(r; [ρ]) in the α →0 and α →∞limits,
describing locally the quantities of Eqs. (8.103)-(8.104), in order to construct an interpolation
for the α−dependence of wα(r; [ρ]).
Since the energy density wα(r; [ρ]) is not uniquely
deﬁned, we must use the same gauge for the weak and and the strong-interaction limits. A
very reasonable and physical choice would be the gauge deﬁned by the exchange-correlation
hole,
wα(r, [ρ]) = 1
2
Z
dDuρα
xc(r, u)
u
,
(8.107)
where u = r2 −r1, u = |u| and the exchange-correlation hole ρα
xc(r, u) is simply related to
the pair density P α
2 (r1, r2) obtained from the wavefunction Ψα,
P α
2 (r1, r2) = N(N −1)
X
σ1,...,σ2
Z
dDr3 . . . dDrN|Ψα(r1, σ1, . . . rN, σN)|2,
(8.108)
ρα
xc(r, u) =
1
ρ(r)
Z dˆu
4π (P α
2 (r, r + u) −ρ(r)ρ(r + u)) .
(8.109)
The α →0 limit of wα(r; [ρ]) is thus the exchange energy density deﬁned in the gauge of the
exchange hole, for which one could use the exact exchange hole or a good approximation,
e.g., the one of Becke and Roussel.79 The α →∞limit of wα(r; [ρ]) is exactly given by the
SCE solution, which is already deﬁned in the gauge of the exchange-correlation hole (see
also Ref. 45),
wα→∞(r, [ρ]) = 1
N
N
X
i,j=1
1 −δij
|fi(r) −fj(r)| −
Z dDu
u ρ(r + u).
(8.110)
33


## Page 34


Much more diﬃcult is to have a local expression for the next leading terms, both for α →0
and α →∞, deﬁned in the same gauge. The zero-point term of Eq. (5.75), which determines
how the α →∞limit is approached to orders α−1/2, is, in fact, expressed in a gauge which
is not the one of the exchange-correlation (xc) hole. The G¨orling-Levy perturbation theory
is also diﬃcult to deﬁne locally in terms of the xc-hole gauge.
Routes to deﬁne and calculate the local next leading terms will be pursued in future
work. For the ZP term, one could actually directly calculate the pair-density associated to
the O(α−1/2) wavefunction,47 and produce the exact exchange-correlation hole in this limit.
For the α →0 leading correction, one should probably use diﬀerent correlation-strength
indicators than the GL perturbation theory.
A very promising route could be the one
described by Becke in Ref. 80, which considers the local normalization of the exact exchange
hole as an indicator of strong non-dynamical correlation.
The main message of this Section is that the SCE limit contains useful exact information
for critical situations in Chemistry such as stretched bonds. However, one has to be able
to use this exact information locally, where it is needed. This direction of research will be
pursued in future work.
IX.
CONCLUDING REMARKS
The strong-interaction limit of density functional theory, exactly solved in the last three
years, contains useful physical and chemical information, typically missed by standard Kohn-
Sham DFT. In this paper we have outlined some paths to fully exploit this piece of exact
information, with the aim of broadening the applicability of DFT for electronic structure
calculations in solid-state physical devices and in chemical systems, addressing fundamental
issues of standard KS DFT.
The mathematical structure of the strong-interaction limit of DFT has been uncovered in
Refs. 42,45,47. However, solving the relevant equations for a general density in an eﬃcient
way is still an open problem, which will be addressed in future work, exploiting the formal
similarity with mass transportation theory.58
Another line of research for future work is based on the fact that the strictly correlated
problem deﬁned by the strong-interaction limit of DFT provides a physical, rigorous, lower
bound for the exact exchange-correlation functional of standard Kohn-Sham DFT, a feature
34


## Page 35


which may be exploited for the construction of approximate functionals.81
The calculation and study of energy densities in the strong-interaction limit of DFT will
also provide useful information to be included into approximate functionals, and will be the
object of future work.
Acknowledgments
We thank Cyrus Umrigar and Devrim Guclu for the densities of the N = 3 quantum dots.
This work was supported by the Netherlands Organization for Scientiﬁc Research (NWO)
through a Vidi grant.
1 W. Kohn, Rev. Mod. Phys. 71, 1253 (1999).
2 W. Kohn and L. J. Sham, Phys. Rev. A 140, 1133 (1965).
3 E. Runge and E. K. U. Gross, Phys. Rev. Lett. 52, 997 (1984).
4 A. E. Mattsson, Science 298, 759 (2002).
5 J. P. Perdew, A. Ruzsinszky, J. Tao, V. N. Staroverov, G. E. Scuseria, and G. I. Csonka, J.
Chem. Phys. 123, 062201 (2005).
6 A. D. Becke and E. R. Johnson, J. Chem. Phys. 127, 124108 (2007).
7 Y. Zhao, N. E. Schultz, and D. G. Truhlar, J. Chem. Theory Comput. 2, 364 (2006).
8 A. J. Cohen, P. Mori-Sanchez, and W. T. Yang, Science 321, 792 (2008).
9 A. Savin, in Recent Developments of Modern Density Functional Theory, edited by J. M. Sem-
inario (Elsevier, Amsterdam, 1996), pp. 327–357.
10 T. Leininger, H. Stoll, H.-J. Werner, and A. Savin, Chem. Phys. Lett. 275, 151 (1997).
11 R. Pollet, A. Savin, T. Leininger, and H. Stoll, J. Chem. Phys. 116, 1250 (2002).
12 J. G. ´Angy´an, I. Gerber, A. Savin, and J. Toulouse, Phys. Rev. A 72, 012510 (2005).
13 E. Goll, H.-J. Werner, and H. Stoll, Phys. Chem. Chem. Phys. 7, 3917 (2005).
14 E. Goll, H.-J. Werner, H. Stoll, T. Leininger, P. Gori-Giorgi, and A. Savin, Chem. Phys. 329,
276 (2006).
15 E. Fromager, J. Toulouse, and H. J. A. Jensen, J. Chem. Phys. 126, 074111 (2007).
35


## Page 36


16 J. Toulouse, I. C. Gerber, G. Jansen, A. Savin, and J. G. ´Angy´an, Phys. Rev. Lett. 102, 096404
(2009).
17 B. G. Janesko, T. M. Henderson, and G. E. Scuseria, J. Chem. Phys. 130, 081105 (2009).
18 E. Livshits and R. Baer, Phys. Chem. Chem. Phys. 9, 2932 (2007).
19 E. Goll, H. Stoll, C. Thierfelder, and P. Schwerdtfeger, Phys. Rev. A 76, 032507 (2007).
20 E. Goll, T. Leininger, F. R. Manby, A. Mitrushchenkov, H.-J. Werner, and H. Stoll, Phys.
Chem. Chem. Phys. 10, 3353 (2008).
21 E. Fromager, R. Cimiraglia, and H. J. A. Jensen, Phys. Rev. A 81, 024502 (2010).
22 J. Paier, B. G. Janesko, T. M. Henderson, G. E. Scuseria, A. Gr¨uneis, and G. Kresse, J. Chem.
Phys. 132, 094103 (2010).
23 W. Zhu, J. Toulouse, A. Savin, and J. G. ´Angy´an, J. Chem. Phys. 132, 244108 (2010).
24 J. Cioslowski and K. Pernal, J. Chem. Phys. 113, 8434 (2000).
25 J. Cioslowski and M. Buchowiecki, J. Chem. Phys. 125, 064105 (2006).
26 N. B. Zhitenev, R. C. Ashoori, L. N. Pfeiﬀer, and K. W. West, Phys. Rev. Lett. 79, 2308 (1997).
27 O. Gritsenko, K. Pernal, and E. J. Baerends, J. Chem. Phys. 122, 204102 (2005).
28 D. R. Rohr, K. Pernal, O. V. Gritsenko, and E. J. Baerends, J. Chem. Phys. 129, 164105 (2008).
29 T. Tsuchimochi and G. E. Scuseria (2009).
30 M. Levy, Proc. Natl. Acad. Sci. U.S.A. 76, 6062 (1979).
31 M. Levy and J. P. Perdew, in Density Functional Methods in Physics, edited by R. M. Dreizler
and J. da Providencia (Plenum, New York, 1985).
32 J. Harris, Phys. Rev. A 29, 1648 (1984).
33 D. C. Langreth and J. P. Perdew, Solid State Commun. 17, 1425 (1975).
34 W. Yang, J. Chem. Phys. 109, 10107 (1998).
35 M. Levy and J. P. Perdew, Phys. Rev. A 32, 2010 (1985).
36 Z. F. Liu and K. Burke, J. Chem. Phys. 131, 124124 (2009).
37 P. Gori-Giorgi, M. Seidl, and G. Vignale, Phys. Rev. Lett. 103, 166402 (2009).
38 E. H. Lieb, Int. J. Quantum. Chem. 24, 24 (1983).
39 M. Seidl, J. P. Perdew, and M. Levy, Phys. Rev. A 59, 51 (1999).
40 M. Seidl, Phys. Rev. A 60, 4387 (1999).
41 M. Seidl, J. P. Perdew, and S. Kurth, Phys. Rev. A 62, 012502 (2000).
42 M. Seidl, P. Gori-Giorgi, and A. Savin, Phys. Rev. A 75, 042511 (2007).
36


## Page 37


43 D. E. Freund, B. D. Huxtable, and J. D. Morgan, Phys. Rev. A 29, 980 (1984).
44 P. Gori-Giorgi and A. Savin, Phys. Rev. A 71, 032513 (2005).
45 P. Gori-Giorgi, M. Seidl, and A. Savin, Phys. Chem. Chem. Phys. 10, 3440 (2008).
46 M. Levy, in The single-Particle Density in Physics and Chemistry, edited by N. March and
B. Deb (Academic Press, London, 1987).
47 P. Gori-Giorgi, G. Vignale, and M. Seidl, J. Chem. Theory Comput. 5, 743 (2009).
48 C. Attaccalite, S. Moroni, P. Gori-Giorgi, and G. B. Bachelet, Phys. Rev. Lett. 88, 256601
(2002).
49 D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. 45, 566 (1980).
50 S. J. Vosko, L. Wilk, and M. Nusair, Can. J. Phys. 58, 1200 (1980).
51 J. P. Perdew and Y. Wang, Phys. Rev. B 45, 13244 (1992).
52 J. Sun, J. P. Perdew, and M. Seidl, Phys. Rev. B 81, 085123 (2010).
53 M. Casula, S. Sorella, and G. Senatore, Phys. Rev. B 74, 245427 (2006).
54 U. von Barth and L. Hedin, J. Phys. C 5, 1629 (1972).
55 R. van Leeuwen and E. J. Baerends, Phys. Rev. A 49, 2421 (1994).
56 Q. Zhao, R. C. Morrison, and R. G. Parr, Phys. Rev. A 50, 2138 (1994).
57 F. Colonna and A. Savin, J. Chem. Phys. 110, 2828 (1999).
58 G. Buttazzo, L. De Pascale, and P. Gori-Giorgi, in preparation (2010).
59 S. M. Reimann and M. Manninen, Rev. Mod. Phys. 74, 1283 (2002).
60 H. Jiang, H. U. Baranger, and W. Yang, Phys. Rev. B 68, 165337 (2003).
61 H. Jiang, D. Ullmo, W. Yang, and H. U. Baranger, Phys. Rev. B 69, 235326 (2004).
62 E. R¨as¨anen, A. Harju, M. J. Puska, and R. M. Nieminen, Phys. Rev. B 69, 165309 (2004).
63 S. Pittalis, E. R¨as¨anen, C. R. Proetto, and E. K. U. Gross, Phys. Rev. B 79, 085316 (2009).
64 M. Rontani, C. Cavazzoni, D. Bellucci, and G. Goldoni, J. Chem. Phys. 124, 124102 (2006).
65 S. A. Blundell and K. Joshi, Phys. Rev. B 81, 115323 (2010).
66 A. Ghosal, A. D. Guclu, C. J. Umrigar, D. Ullmo, and H. U. Baranger, Nature Phys. 2, 336
(2006).
67 L. Zeng, W. Geist, W. Y. Ruan, C. J. Umrigar, and M. Y. Chou, Phys. Rev. B 79, 235334
(2009).
68 A. D. Guclu, A. Ghosal, C. J. Umrigar, and H. U. Baranger, Phys. Rev. B 77, 041301 (2008).
69 C. Yannouleas and U. Landman, Rep. Prog. Phys. 70, 2067 (2007).
37


## Page 38


70 P. Ziesche, J. Tao, M. Seidl, and J. P. Perdew, Int. J. Quantum Chem. 77, 819 (2000).
71 M. Taut, Phys. A: Math. Gen. 27, 1045 (1994).
72 N. D. Drummond and R. J. Needs, Phys. Rev. Lett. 102, 126402 (2009).
73 W. J. Carr, Phys. Rev. 122, 1437 (1961).
74 A. M. Teale, S. Coriani, and T. Helgaker, J. Chem. Phys. 132, 164115 (2010).
75 M. Seidl, J. P. Perdew, and S. Kurth, Phys. Rev. Lett. 84, 5070 (2000).
76 A. G¨orling and M. Levy, Phys. Rev. A 50, 196 (1994).
77 P. Gori-Giorgi and A. Savin, J. Phys.: Conf. Ser. 117, 012017 (2008).
78 A. Savin, Chem. Phys. 356, 91 (2009).
79 A. D. Becke and M. R. Roussel, Phys. Rev. A 39, 3761 (1989).
80 A. D. Becke, J. Chem. Phys. 119, 2972 (2003).
81 E. R¨as¨anen, M. Seidl, and P. Gori-Giorgi, in preparation (2010).
38

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 1008_2327v1_density_functional_theory_for_strongly_interacting_electrons_perspectives_for_p
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2010/1008_2327V1_DENSITY_FUNCTIONAL_THEORY_FOR_STRONGLY_INTERACTING_ELECTRONS_PERSPECTIVES_FOR_P.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

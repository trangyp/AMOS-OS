---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1411.5989v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1411.5989v1_A_semiclassical_non-adiabatic_theory_for_elementary_chemical_reactions

> Source: 1411.5989v1_A_semiclassical_non-adiabatic_theory_for_elementary_chemical_reactions.pdf

> Pages: 17

---


## Page 1


arXiv:1411.5989v1  [physics.chem-ph]  20 Nov 2014
A semiclassical non-adiabatic theory for
elementary chemical reactions
S. Aubry
Laboratoire L´eon Brillouin(CEA-CNRS)
CEA Saclay, 91191-Gif-sur-Yvette, France
serge.aubry91gmail.com
October 10, 2018
Abstract: Electron Transfer (ET) reactions are modeled by the dynamics of
a quantum two-level system (representing the electronic state) coupled to a ther-
malized bath of classical harmonic oscillators (representing the nuclei degrees of
freedom). Unlike for the standard Marcus theory, the complex amplitudes of the
electronic state are chosen as reaction coordinates. Then, the dynamical equations
at non vanishing temperature become those of an eﬀective Hamiltonian submitted
to damping terms and their associated Langevin random forces. The advantage
of this new formalism is to extend the original theory by taking into account both
ionic and covalent interactions. The standard theory is recovered only when co-
valent interactions are neglected. Increasing these covalent interactions from zero,
the energy barrier predicted by the standard theory ﬁrst depresses, next vanish
(or almost vanish) and for stronger covalent interactions, covalent bond formation
takes place of ET. In biochemistry, the standard Marcus theory often fails to ex-
plain the enzymatic reactions especially those with non Arrhenius behavior which
are barrierless and also dissipate little heat. We claim that this improved theory
should yield an interesting tool for understanding them.
keywords: Chemical reactions, Electron Transfer, Covalence, Ionicity, Mixed
Valence.
Chemical reactions are primarily changes of electronic states (associated with
molecular and environmental reorganization) which appear either in radical ioniza-
tion (redox) or in the forming/breaking of chemical bonds. They can be generally
decomposed into sequences of elementary chemical reactions (ECR), each of them
corresponding to a single transition between two diﬀerent electronic states. The
1


## Page 2


simplest example of ECR is an electron transfer (ET) between a Donor and an
Acceptor but it may also correspond more generally to exciton creation, exciton
transfer etc.... The rate of chemical reactions often obeys the Arrhenius law which
manifests the existence of an energy barrier between the reactants and the prod-
ucts which has to be overcome under the eﬀect of thermal ﬂuctuations. These
energy barriers are usually quite large compared to the room temperature energy
(≈0.026eV at 300K). There are also chemical reactions which do not obey the
Arrhenius law (with a positive energy barrier). This is the situation for free radi-
cals with unpaired electrons which are often highly reactive and generate covalent
bonds.
The standard theory for ET (redox) mostly due to (author?) [Marcus 1993],
considers the free energy of the whole system as a function of the nuclei (reaction)
coordinates when the electron is on the Donor site (reactants) or on the Acceptor
site (products). These functions are approximate as paraboloids schematically rep-
resented ﬁg.1. There are two regimes called normal when at constant coordinates,
the electronic excitation from Donor to Acceptor requires to absorb a positive
energy Eel and inverted when Eel is negative.
The lowest point at the intersection of these two surfaces determines the min-
imum free energy ∆G⋆to be provided to the system for transferring the electron
between Donor and Acceptor. This energy barrier may be reached because of the
thermal ﬂuctuations of the nuclei with a probability per unit time proportional
to e−∆G⋆
kBT which yields the main factor of the Arrhenius law. At this point the
two electronic states on Donor and Acceptor are degenerate so that ET may oc-
cur by quantum tunneling. Actually, it is assumed there is an overlap between
the two orbitals necessary for allowing tunneling but which also raise the de-
generacy and open a gap at the intersection between the two diabatic surfaces
ﬁg.1. This overlap (and gap) is generally assumed to be small. Then, one ob-
tains two non-intersecting adiabatic surfaces. However, the real evolution of the
electronic wave function is not considered as a continuous process. Instead of,
electron tunneling is considered as a discontinuous jump which occur with some
probability depending on the time during which resonance lasts thus depending
on the phonons (or vibrons) and the temperature. The transition probability be-
tween the two diabatic surfaces A(T) which contributes to the prefactor of the
Arrhenius law is empirically calculated from the Landau-Zener model.
In the
normal regime, ET does not require any diabatic transition while in the inverted
regime a diabatic transition from the upper to the lower energy surface is neces-
sary (see ﬁg.1). Current researches related to this problem of ET are still very
active for example in the ﬁeld of Organic Mixed Valence Compounds (author?)
[Hankache & Wenger 2011, Lambert & Heckmann 2012].
Our purpose is to propose a semiclassical theory which describes the dynamics
2


## Page 3


E
el
Donor
Acceptor
!G
*
!G
0
Normal
Donor
Acceptor
E
el
!G
0
!G
*
Diabatic transition
Inverted
Reaction Coordinates
Figure 1: Standard Theory: The surfaces of energy versus Reaction Coor-
dinates are two intersecting paraboloids, one corresponding to the reactants
and one to the products. A small gap opening at intersection determines the
lower energy (adiabatic) surface (thick line) and the upper energy (adiabatic)
surface (dotted line).
3


## Page 4


of ET (or ECR) as a continuous process. The nuclei are still considered as classical
particles while the dynamics of the electronic state is treated quantumly preserving
possible phase coherence. Our model becomes equivalent to a quantum spin 1/2
coupled to a phonon bath (spin-Boson model). Early study of similar models were
done for application to NMR (author?) [Redﬁeld 1957] and later for chemical re-
actions (author?) [Meyer & Miller 1978 , Stock & Thoss 1996, XiaoGen Song et al. 2008,
Miller 2009] but using diﬀerent approaches for example the density matrix theory.
However, our spin-boson model is diﬀerent from those studied earlier because
both the z and x spin components are coupled with the phonon bath instead of
the only z component. Thus our model has the advantage to interpolate between
a redox chemical reaction and a covalent bond formation which was never done
before. Otherwise, we use a simpler formalism for direct derivation of the quan-
tum dynamical equations and then a standard mean ﬁeld approximation yields the
semiclassical approximation.
We start from ﬁrst principles and consider very generally, the global quantum
Hamiltonian H = He(R) + P
i
P2
i
2Mi of our reacting system consisting of many
interacting electrons α with coordinates r = {rα} also interacting with a collection
of quantum nuclei i with masses Mi and coordinates Ri. It is the sum of the
Hamiltonian He(R) of the whole system of electrons in the potential generated by
the nuclei and of their kinetic energy operator which depends on their momenta
operators Pi =
¯h
i ∇Ri.
The standard Born-Oppenheimer (BO) approximation
assumes that the global wavefunction has the form Ψ(r, R, t) = Φ(R, t)ψ0(r, R)
where ψ0(r, R) is the electronic groundstate of Hamiltonian He(R).
Its eigen
energy E0(R) becomes the interaction potential of the nuclei. Theories done in
the framework of the BO approximation (author?) [Anslyn & Doughtery 2006]
consider that chemical species correspond to local minima of this potential energy
surface and that chemical reactions are transitions between those minima induced
by thermal ﬂuctuations which help to overcome energy barriers (transition state).
These theories are valid when the other electronic states remain far in energy so
that they are not involved.
We consider now an ET which involves an electronic subspace E(R) spanned
by two diabatic states ψD(r, R) and ψA(r, R) real and orthogonal (LCAO repre-
sentation). For a standard ET, the diabatic electronic state D would be the initial
state with an electron on the Donor site and the ﬁnal state A those with this elec-
tron transferred on the Acceptor site. Thus, we assume that during the transition,
the electronic state remains conﬁned in this 2D subspace E(R) that is the global
wave function takes the form Ψ(r, R, t) = ΦD(R, t)ψD(r, R) + ΦA(R, t)ψA(r, R).
All the other electronic states are supposed to remain far in energy so that their
possible hybridization can be discarded.
Integration over all the electronic variables r yields the nuclei Hamiltonian
4


## Page 5


< Ψ(r, R, t)|He(R) + P
i
P2
i
2Mi |Ψ(r, R, t) >r= ˜He + ˜K which operates in the two-
components wave function space Φ(R, t) =
 
ΦD(R, t)
ΦA(R, t)
!
.
˜He is a 2 × 2 ma-
trix which has the form ˜He =
 
ED(R)
Λ(R)
Λ(R)
EA(R)
!
only dependent on R while
the projected kinetic energy operator ˜K = P
i,α
P 2
i,α
2Mi can be expressed with the
following overlap integrals an,m
i,α (R) =
1
Mi
R ψn(r, R)∂ψm(r,R)
∂Ri,α
dr for n, m = D or
A. Orthonormalization implies aD,D(R) = 0 and aA,A(R) = 0 and aD,A
i,α (R) =
−aA,D
i,α (R) =
1
Mi
R ψD(r, R)∂ψA(r,R
∂Ri,α dr real. We deﬁne vector A(R) = {aD,A
i,α (R)} =
{−aA,D
i,α (R)}. We also deﬁne the matrix elements for n, m = D or A, wn,m(R) =
wm,n(R) = P
i
1
2Mi
R ∇Riψn(r, R).∇Riψm(r, R)dr.
Then, the projected kinetic
operator P
i
P2
i
2Mi becomes the 2 × 2 matrix of operators ˜K =
 
KDD
KDA
KAD
KAA
!
where KDD = P
i
P2
i
2Mi + ¯h2wD,D(R), KAA = P
i
P2
i
2Mi + ¯h2wA,A(R), KDA =
−i¯h
2 (A.P+P.A)+ ¯h2
2 ∇.A+¯h2wD,A(R) = K⋆
AD. Using the base of Pauli matrices
σx, σy, σz (with standard commutation relations [σx, σy] = 2iσz, [σy, σz] = 2iσx,
[σz, σx] = 2iσy), the fully quantum Hamiltonian appears a collection of quantum
nuclei coupled to a single quantum spin 1/2
˜H
=
X
i
P2
i
2Mi
+ Vph(R)
+
˜Λ(R)σx + Π(R, P)σy + W(R)σz
(1)
where Vph(R) = 1
2(ED(R)+EA(R))+ ¯h2
2 (wD,D(R)+wA,A(R)), W(R) = 1
2(ED(R)−
EA(R)) + ¯h2
2 (wD,D(R) −wA,A(R)), ˜Λ(R) = Λ(R) + ¯h2
2 ∇.A(R) + ¯h2wD,A(R) and
Π(R, P) = ¯h
2 (A(R).P + P.A(R)).
For going further, it is now convenient to assume that 1) Potential Vph(R)
is quadratic and then choosing the origin of the nuclei coordinates as well as the
origin of the energies at its minimum, the nuclei potential takes the form Vph(R) =
1
2R.M.R where M is a positive elasticity matrix. 2) We assume a linear behavior
for the spin coeﬃcients of σz (charge coupling), W(R) = W(0)+∇.W(0).R, of σx
(covalent coupling) ˜Λ(R) = ˜Λ(0) + ∇.˜Λ(0).R and of σy Π(R, P) = ¯hA(0).P. We
also assume A(0) = 0 for simplicity (though it would not be a big deal to conserve
this coupling with σy) 1. Then, it is convenient to use the base of normal modes
1Despite the use of bases of diabatic states is ubiquitous for understanding electronic
structures and dynamics in physics and chemistry, they have no strict deﬁnition as proven
5


## Page 6


obtained by diagonalization of matrix M.
Hamiltonian (1) becomes that of a single quantum spin 1/2 submitted to an
external ﬁeld (ǫx, 0, ǫz) and linearly coupled to a collection of quantum normal
modes n (harmonic oscillators with unit mass and frequency ωn) by constants
kx
n, 0, kz
n.
˜H =
X
n
1
2

p2
n + ω2
nq2
n

+ kx
nqnσx + kz
nqnσz

+ ǫxσx + ǫzσz
(2)
Path integral methods were used for studying this model in the fully quantum case
in the case for ǫz = 0 and with no transverse coupling kx
n = 0 ( see (author?)
[Leggett et al. 1987] and references therein). It is nevertheless simpler and suﬃ-
cient in our context to use a mean ﬁeld approximation where the coupling terms
qnσz (and similarly for qnσx) are replaced by qn¯σz + ¯qnσz −¯qn¯σz ( the expected
value of an operator a is ¯a =< Ψ(t)|a|Ψ(t) > with |Ψ(t) > the global wave func-
tion at time t). Thus, we neglect the ﬂuctuation operators (qn −¯qn)(σz −¯σz).
This mean ﬁeld approximation turns out to be equivalent to the standard classi-
cal approximation. It is valid when the relevant nuclei displacements generated
by the molecular reorganization during ET are much larger than their quantum
ﬂuctuations < (qn −¯qn)2 >1/2 which is often true in real situations.
The Ehrenfest equation i¯h˙¯a(t) = [ ˜H, a] provides closed equations for the time
derivatives of {¯pn, ¯qn} and ¯σx, ¯σy, ¯σz which do not involve any other variables.
They correspond to those of a quantum spin σ submitted to the time dependent
classical ﬁeld with components (ǫx+P
n kx
n¯qn(t), 0, ǫz +P
n kz
n¯qn(t)) and to classical
oscillators n submitted to external time dependent forces fn(t) = kx
n¯σx(t)+kz
n¯σz(t).
It is convenient to describe this spin ϕD(t)| ↑> +ϕA(t)| ↓> with its two complex
coordinates ϕD(t) and ϕA(t) in the eigenbase of σz Donor-Acceptor (fulﬁlling the
normalisation condition |ϕD|2 + |ϕA|2 = 1).
Since the nuclei variables obey linear equations, the general solution ¯qn(t) of
each linear oscillator can be explicitly calculated as the sum of a function of the
external force fn(t) and a solution of the free oscillator chosen randomly according
to the Boltzman statistics (author?) [Aubry & Kopidakis 2003, Aubry 2007]. It
comes out after substitution in the spin equations that the dynamics of the elec-
tronic (or spin) components is described by two equations corresponding to those
of a Hamiltonian system where (ϕ⋆
D, i¯hϕD) and (ϕ⋆
A, i¯hϕA) are pairs of conjugate
variables but also submitted to dissipative and random forces
i¯h ˙ϕD
=
∂Heff
∂ϕ⋆
D
+ ζz(t)ϕD + ζx(t)ϕA
in ref. (author?) [Van Voorhis et al. 2010]. A good criteria to ﬁnd them, is that they
depend smoothly on the nuclei coordinates R with overlaps A(0) as small as possible.
Actually this assumption is necessary to justify the above low order expansion.
6


## Page 7


+
Z t
0

Γzz(t −τ) ˙Z(τ) + Γxz(t −τ) ˙X(τ)

dτ

ϕD
+
Z t
0

Γxz(t −τ) ˙Z(τ) + Γxx(t −τ) ˙X(τ)

dτ

ϕA
(3)
i¯h ˙ϕA
=
∂Heff
∂ϕ⋆
A
−ζz(t)ϕA + ζx(t)ϕD
−
Z t
0

Γzz(t −τ) ˙Z(τ) + Γxz(t −τ) ˙X(τ)

dτ

ϕA
+
Z t
0

Γxz(t −τ) ˙Z(τ) + Γxx(t −τ) ˙X(τ)

dτ

ϕD
(4)
The eﬀective Hamiltonian in 4 is
Heff(ϕD, ϕA)
=
ǫxX + ǫzZ
−1
2Γxx(0)X2
−
Γxz(0)XZ −1
2Γzz(0)Z2
(5)
where Z = ¯σz = |ϕD|2 −|ϕA|2 and X = ¯σx = ϕ⋆
DϕA + ϕDϕ⋆
A. Heff is nothing
but the energy minimum with respect to all the nuclei coordinates of the whole
system at ﬁxed electronic amplitudes ϕD,ϕA 2.
The memory (or damping) functions in 4 are deﬁned as
Γxx(t)
=
X
n
(kx
n)2
ω2n
cos ωnt =
Z
˜Γxx(ω) cos ωt dω
Γzz(t)
=
X
n
(kz
n)2
ω2n
cos ωnt =
Z
˜Γzz(ω) cos ωt dω
Γxz(t)
=
Γzx(t) =
X
n
kz
nkx
n
ω2n
cos ωnt =
Z
˜Γxz(ω) cos ωt dω
(6)
They fulﬁll 0 ≤Γzz(0), 0 ≤Γxx(0) and Γ2
zx(0) ≤Γzz(0)Γxx(0).
Assuming a
large system with many classical oscillators, these functions may be assumed to be
smooth and to vanish at large time as for a standard classical Langevin bath. Then,
the absence of random forces ζα(t), this eﬀective Hamiltonian Heff necessarily
decays in time (essentially because of nonadiabaticity) (author?) [Aubry 2007].
Temperature appears in eqs.(3,4) through the gaussian random forces with
correlations fulﬁlling the Langevin conditions at temperature T
< ζz(t)ζz(t + τ) >t
=
kBTΓzz(τ)
2A
similar
Hamiltonian
was
introduced
phenomenologically
in
(author?)
[Aubry & Kopidakis 2003]
without
microscopic
justiﬁcations
but
the
form
which
was used, was not correct because we omitted covalent terms and artiﬁcially introduced
extra nonlinear capacitive terms.
7


## Page 8


< ζx(t)ζx(t + τ) >t
=
kBTΓxx(τ)
< ζx(t)ζz(t + τ) >t
=
kBTΓxz(τ)
(7)
The Fourier transforms of the memory functions (6) have to vanish at large
frequency for ω > ωc where ωc is the maximum phonon frequency. Then, far from
electronic resonances ∆el >> ¯hωc, the characteristic frequency of the electronic
dynamics is much beyond ωc so that the eﬀect of damping disappears. Eqs.7 also
show that the random forces have a spectrum below ωc with slow variations at
the scale of the electron dynamics. We are in the adiabatic regime where the BO
approximation is valid. When the random forces bring the electronic system near
resonance, the validity of the BO approximation breaks down and nonadiabaticity
manifests by energy dissipation into the phonon bath.
Deﬁning new conjugate variables ID, θD, IA, θA by ϕD = √IDe−iθD and ϕA =
√IAe−iθA, and next the conjugate variables I = (IA −ID)/2 = −Z/2 and θ =
θA −θD, this eﬀective Hamiltonian becomes only a function −1
2 ≤I ≤1
2, θ mod
2π on a sphere with poles I = ± 1
2 and where θ corresponds to the longitude and
φ deﬁned as sin φ = 2 ∗I to the latitude. Then
Heff
=
−2ǫzI + ǫx
p
1 −4I2 cos θ −2Γzz(0)I2
+
2Γxz(0)I
p
1 −4I2 cos θ −1
2Γxx(0)(1 −4I2) cos2 θ
(8)
represents the true energy surface on which the system evolves during ET. At
zero temperature (0K) and assuming the damping terms vanishes, the dynami-
cal equations would be those of an integrable Hamiltonian system on a sphere.
All trajectories would be periodic on closed orbits deﬁned by a constant energy
Heff(I, θ). Figs.2 and 3 show both 3D and contour plots for several examples.
We assume that the (initial) transfer integral ǫx is small as in the standard
theory and that our system is initially at the Donor pole I = −1/2. The Ac-
ceptor pole corresponds to I = +1/2. When there are no covalent interactions
(Γxx(0) = Γxz(0) = 0), our theory is nothing but a diﬀerent representation of the
standard Marcus theory except that we now have explicit dynamical equations
which intrinsically describe the diabatic transitions through the damping terms
(without needing the Landau-Zeener model). The two Marcus energy surfaces are
the paraboloids obtained from Hamiltonian (2) where σx = 0, pn = 0 and σz = +1
(electron on Donor) or σz = −1 (electron on Acceptor). The reaction energy is
∆G0 = −2ǫz and λ = 2Γzz(0) is the so called reorganization energy known in the
litterature. Then the barrier energy takes the standard form
∆G⋆= (λ + ∆G0)2
4λ
(9)
The electronic excitation energy is Eel = 2(Γzz(0) −ǫz) = ∆G0 + λ.
8


## Page 9


- 3
- 2
- 1
0
1
2
3
- 0.4
- 0.2
0.0
0.2
0.4
I
I
!
!
Donor
Acceptor
Saddle Point
Normal
I
!
Donor
Acceptor
!
I
- 3
- 2
- 1
0
1
2
3
- 0.4
- 0.2
0.0
0.2
0.4
Inverted
Figure 2:
Two examples of 3D plots of the the energy landscape Heff(I, θ)
in the normal (left) and the inverted regime (right) of the Marcus theory
with below their corresponding contour plots (the sphere I, θ is represented
within the Mercator projection where the poles are single points appearing
as the thick lines). Covalent interactions (Γxx(0) = Γxz(0) = 0) vanish and
Γzz(0) = 1., ǫz = 0.1, ǫx = −0.1 (left) and Γzz(0) = 1., ǫz = 1, ǫx = −0.1
(right).
9


## Page 10


In the normal regime, when Eel > 0, the energy surface (see ﬁg.2 left) exhibits
a saddle point which corresponds to the top of the energy barrier between the
donor and acceptor state. At the inversion point where Eel = 0, the saddle point
and the two maxima on the sphere of Heff(I, θ) merge with the minimum near the
pole I = −1/2 which thus become a single maximum so that in the inverted regime
Eel < 0, there is no more energy barrier (see ﬁg.2 right). In both regimes, the two
poles on the sphere Donor and Acceptor are surrounded by periodic and stable
orbits with frequency ωel obtained by linearizing the equations (3,4) which turns
out to be related to |Eel| = ¯hωel. When this electronic frequency ωel is beyond
the phonon spectrum that is |Eel| >> ¯hωc, the damping terms have negligible
dissipative eﬀect in eqs.3,4 so that the poles are practically stable at 0K. At non
vanishing temperature, the thermal forces in eqs.3,4, generate adiabatic random
ﬂuctuations of the electronic frequency |Eel|. If these ﬂuctuations bring |Eel| in
the phonon range below ¯hωc, the damping terms in eqs.3,4 become eﬃcient. The
system is no more adiabatic and then ET may occur with some probability. We
have already shown in (author?) [Aubry 2007] that reaching this resonance is
equivalent to reach the intersection between the two paraboloids so that we recover
a standard Arrhenius law (despite there is apparently no energy barrier for Heff).
On contrary, in the inverted regime but near the inversion point where Eel < ¯hωc,
ET should spontaneously occurs even at 0K because the phonon bath can absorb
eﬃciently the reaction energy. ET is then very fast.
When covalent interactions are present Γxx(0) ̸= 0, the standard Marcus theory
may drastically fail. Then, either ET still occur but with an energy barrier which
may be much smaller than those given by eq.9 and may even vanish or a covalent
bond forms instead of ET. The reason of this failure is that the standard Marcus
theory only takes into account an overlap term which does not depend on the
distance Donor Acceptor. Actually it does because it is also obviously coupled
to the phonon ﬁeld. This covalent term may be often negligible so the standard
Marcus theory is then successful.
However, the covalent has no reason to be
always negligible. We shall claim in a forthcoming paper that the existence of
covalent term could be the key for a correct understanding of the so much puzzling
enzymatic functions in biochemistry which involve soft molecules and electronic
orbitals sometime quite extended.
Considering the limit Γzz(0) << Γxx(0) and ǫz < Γxx(0) (then Γxx(0) >>
|Γxz(0)|), there are two energy minima on the sphere (see ﬁg.3 left) corresponding
both to covalent bonds where θ = 0mod π and I = Ic ≈
ǫz
2Γxx(0) with |Ic| < 1/2 and
two maxima on θ = π/2 mod π. Actually, only the lowest minimum is physically
acceptable for the covalent bond. In physical situations, the overlap term Λ(R) is
expected to exponentially vanish at large distance Donor-Acceptor, but due to the
linear approximation on Λ(R) in (1), it does not and change sign. Thus potential
10


## Page 11


Donor
!
!
I
- 3
- 2
- 1
0
1
2
3
- 0.4
- 0.2
0.0
0.2
0.4
Covalent state
Acceptor
I
I
Donor
Acceptor
!
I
!
- 3
- 2
- 1
0
1
2
3
- 0.4
- 0.2
0.0
0.2
0.4
Figure 3: Same as ﬁg.2 but for some examples with covalent interactions. On
the left side ǫz = 0.2, ǫx = −0.01, Γzz(0) = 1, Γxx(0) = 2. and Γxz(0) = −0.1.
correspond to a situation where the ﬁnal state is a covalent state. On the
right side : ǫz = ǫx = 0, Γxx(0) = Γzz(0) = 1. and Γxz(0) = 0) correspond to
an ideally isoenergetic and barrierless situation.
11


## Page 12


Heff(I, θ) is well-described only on the part of the sphere where Λ(R) keeps the
same sign as Λ(0) and only the trajectories restricted to this region are physically
acceptable. The same problem appears in the well-known SSH model (author?)
[Schrieﬀer & Heeger 1979]. The poles I = ±1/2 are unstable because they belong
to large amplitude time periodic orbits with frequency in the range of phonon
frequencies. These trajectories are dissipative and converge toward the minimum
energy solution which is the covalent bond. This is the situation of free radicals
which spontaneously bind without activation energy.
The most interesting situation is obtained in the intermediate case, when both
charge and covalent interactions are present. Fig.3 shows the ideal case obtained
for well chosen parameters where ǫx = ǫz = 0, Γxx(0) = Γzz(0), Γxz(0) = 0.
Then Heff(I, θ) is minimum along two degenerate paths θ = 0 or π/2 which is
quite similar to those of a dimer model with Targeted Energy Transfer (TET)
(author?) [Aubry et al. 2001] but as noted above, only one of these paths is
physically relevant. For model parameters near but not equal to their ideal values,
the energy proﬁle between Donor and Acceptor is still rather ﬂat with small energy
barrier if any. Instead of pure degeneracy, there is a strong softening of the global
dynamics (involving both the electron and phonons motions). ET may then occur
spontaneously and very fast at 0K providing the reaction energy be slightly positive
without energy barrier. If there is a small energy barrier, then ET would occur
eﬃciently at a small temperature as soon the thermal energy is beyond this energy
barrier.
We illustrate this dynamics for an example in this situation which could be
understood independantly of the general theory.
Instead of a direct numerical
integration of eqs.4 for a model involving a phonon continuum, it is much easier
to consider an equivalent model where there is only a small number of phonons
submitted to a standard damping and a Langevin force with a white spectrum
corresponding to a given bath at some temperature. We choose Hamiltonian
H = (ǫz + kzuz)Z + (ǫx + kxux)X + 1
2p2
z + 1
2Ω2
zu2
z + 1
2p2
x + 1
2Ω2
xu2
x
(10)
which involves two harmonic oscillators with unit mass and coordinates uz and ux
with damping constants γz and γx respectively. The ﬁrst oscillator is only coupled
to the charge term Z = |ϕD|2 −|ϕA|2 and the second one only to covalent term
X = ϕAϕ⋆
D + ϕDϕ⋆
A. Its dynamical equations are
i¯h ˙ϕD
=
(ǫz + kzuz)ϕD + (ǫx + kxux)ϕA
(11)
i¯h ˙ϕA
=
−(ǫz + kzuz)ϕA + (ǫx + kxux)ϕD
(12)
¨uz
+
γz ˙uz + Ω2
zuz + kzZ = ηz(t)
(13)
¨ux
+
γx ˙ux + Ω2
xux + kxX = ηx(t)
(14)
12


## Page 13


where ηz(t) (resp. ηx(t) are random gaussian white noise at temperature T which
fulﬁlls the Langevin condition < ηz(t+τ)ηz(t) >= 2kBTγzδ(τ) , < ηz(t+τ)ηx(t) >=
0 and < ηx(t + τ)ηx(t) >= 2kBTγxδ(τ). The harmonic oscillators variables may
be eliminated in a similar way as in the general case (2) which yields eqs.4 with
memory kernels with the form
Γzz(t)
=
k2
z
Ω2z
e−γz
2 t

cos ˜Ωzt + γz
2˜Ωz
sin ˜Ωzt

(15)
Γxx(t)
=
k2
x
Ω2x
e−γx
2 t

cos ˜Ωxt + γx
2˜Ωx
sin ˜Ωxt

(16)
Frequencies ˜Ωz =
q
Ω2z −γ2z
4
and ˜Ωx =
q
Ω2x −γ2x
4
may be real (underdamped
case) or purely imaginary (overdamped case) but in both case, the memory kernels
remain real. There is no cross term Γxz(t) = 0 because phonons are either coupled
to the charge term or to the covalent term but not to both. These functions at
time 0 determine the eﬀective Hamiltonian (5) appearing in (4). Forces ζz(t) and
ζx(t) are random, gaussian and its correlations obey eqs.7.
This modeling may be qualitatively correct only when the electronic frequencies
are comparable with the phonon frequencies.
The reason is that the memory
functions of this model do not exibit a sharp cut-oﬀat any ωc and consequently
electronic damping would persist in the BO regime while it should not.
We choose to illustrate our present study by an example at 0K but with ultra-
fast ET. We just integrate numerically eqs.14 at 0K (without random force) which
requires only few seconds of computer time using for example the programming
language Mathematica.
Fig.4 shows an example of ultrafast ET versus time at 0K and the correspond-
ing variations of the phonon variables. For this example, parameters were chosen
in order to be in the barrierless situation (where Γzz(0) = Γxx(0) and Γxz(0) = 0)
and also to have a small reaction energy ∆G0 = 2ǫz ≈0.06eV positive ( but not
zero) (see ﬁg.1). Note that in that situation, the standard Marcus model would
expect a relatively large energy barrier ∆G⋆= ǫz−Γzz(0))2
2Γzz(0)
≈Γzz(0)
2
≈0.5eV which
would prevent any eﬃcient electron transfer up to room temperature.
To give some idea of the time scale of ET predicted by our model in physical sit-
uations, reasonable energy units should scale about the order of 1eV = 1.610−19J
while phonon energy quanta ¯hΩz and ¯hΩx should scale at most in the range of
optical phonons energy ∼0.1eV . Then, if we rescale the time unit in order that
¯h = 1, the unit of time appearing ﬁg.4 would range about 6.58×10−16 second.Thus
in this example the time for ET, would range physically about the order of 1ps
which is ultrafast (that is faster by many orders of magnitude than the character-
istic time of most electron transfer). Such ultrafast ET is possible even at 0K but
13


## Page 14


Figure 4: Electron Density on Acceptor versus time in the Dimer example
(14) (with ¯h = 1) at 0K. Insert shows the variation of uz(t) ( representing
the local reorganisation due to ET) while the covalent coordinate ux(t) si-
multaneously varies only back and forth. Parameters are chosen to be in an
almost isoenergetic situation ǫz = 0.03, ǫx = −0.001, kz = kx = 0.1, Ωz =
Ωx = 0.1, γz = γx = 0.2.
14


## Page 15


in rather optimized regimes between underdamped and overdamped.
Actually, in our semiclassical theory, phonon damping do not matter for de-
termining the energy proﬁle and the energy barriers but it is essential for the
dynamics of the electron transfer to be fast. Fastness at 0K requires of course a
barrierless situation but also to be in a non adiabatic regime in order the reaction
energy may be quickly dissipated into the phonon bath. On contrary, in adiabatic
regimes even with no energy barrier, for example in the Marcus inverted regime
far from the inversion point, the electron dynamics is much faster than the phonon
dynamics. There is no energy dissipation and ET cannot occur at 0K 3.
A detailed study of ET as a function of temperature in our model would be
quite instructive for checking both Arrhenius and non Arrhenius behaviors in var-
ious regimes. We have not done it. Actually, this work would require much longer
numerical calculations because of long statistics on the random forces. It is left
for future work 4.
We expect an Arrhenius behavior when there is a large energy barrier or/and
no phonon dissipation. Then, since ET at 0K is not possible, thermal ﬂuctuations
are necessary for allowing ET. They generate random forces which acts adiabati-
cally on the electronic state ( represented on the sphere I, θ) and consequently its
random diﬀusion on this sphere. Thus this electronic state may reach the vicinity
of the transition state with activation energy ∆G⋆(with the Arrhenius probability
proportional to e−∆G⋆
kBT ). Then non-adiabatic eﬀects can take place and produce
ET (quantum tunneling) with some extra probability contributing to the prefactor
A(T).
If ∆G⋆becomes small or negligible, the Arrhenius factor e−∆G⋆
kBT becomes con-
stant and unity in most range of temperature so that the reaction rate cannot obey
anymore an Arrhenius law and is essentially described by its prefactor A(T). As
shown in our above example, when ∆G⋆= 0, ET occurs very fast at 0K following
a non random coherent trajectory. At non vanishing temperature, thermal ﬂuctu-
3unless by chemiluminescence that is very slowly by photon emission. Note that as well
as the phonon bath, the photon bath is also coupled to the ECR and may also contribute to
dissipate the reaction energy. But there are two important diﬀerences. First the spectrum
of the photon bath extends to inﬁnity without any frequency cut-oﬀ(like ωc) and second
the photon bath is generally only weakly coupled to ECR in a regime where the above mean
ﬁeld (or semiclassical) approximation is not valid. Then, this coupling is usually treated
as a quantum perturbation leading to a Fermi Golden rule for the transition probabilities.
4Note that since eqs. 14 contain purely white random forces, it is possible to derive
exact Fokker-Planck equations describing the time evolution of the probability density
P(ϕD, ϕA, uz, ˙uz, ux, ˙ux; t) in the phase space.
However, it is not clear whether these
equations would provide more eﬃcient numerical methods (compared to a direct statistical
study of the initial equations with random Langevin forces).
15


## Page 16


ations are expected to disturb the coherence of this ideal trajectory which should
become stochastic. One should expect a decrease of the rate of ET as tempera-
ture grows. These intuitive predictions could be numerically and quantitatively
examined on our model (14).
In summary, we have built a simple semiclassical theory of ECR using the
complex electronic amplitudes as reaction coordinates instead of the nuclei coordi-
nates. This new formalism allows one to treat within the same model both charge
and covalent interactions. In the limit where only charge interactions are present,
we recover the standard redox theory of ET (with extra reﬁnements for describing
the quantum tunneling without any empirical use of the Landau-Zeener eﬀect).
Our model may also be applied in situations where the Arrhenius law does not
hold. With only the covalent interactions, we can model the covalent binding of
free radicals (with no energy barriers). We also expect intermediate situations
with ﬁnely tuned charge and covalent interactions, with almost ﬂat energy proﬁle.
Those ECR are ultrafast elementary chemical reactions even at zero temperature.
I acknowledge George Kopidakis and Jos´e Teixeira for valuable discussions and
Laboratoire L´eon Brillouin for its hospitality.
References
[Marcus 1993] R.A.
Marcus,
Rev.Mod.Phys.
65
(1993)
599-610,
see
also
http://en.wikipedia.org/wiki/Marcus theory
[Hankache & Wenger 2011] J. Hankache and O.S. Wenger, Chem. Rev. 111 (2011)
51385178 doi:10.1021/cr100441k
[Lambert & Heckmann 2012] C. Lambert and A. Heckmann Angew. Chem. Int.
Ed. 51 (2012) 326-392 doi: 10.1002/anie.201100944
[Redﬁeld 1957] A.G. Redﬁeld, IBM Journal of Research and Development 1 (1957)
19
[Meyer & Miller 1978 ] H-D Meyer and W.H. Miller, J.Chem.Phys. 70 (1978)
3214-3223; doi :10.1063/1.437910
[Stock & Thoss 1996] G. Stock and M. Thoss, Phys.Rev.Lett. 78 (1996) 578-581
[ XiaoGen Song et al. 2008] XiaoGeng
Song,
Haobin
Wang,
and Troy
Van
Voorhis, J.Chem.Phys. 129 (2008) 144502 ; doi: 10.1063/1.2991294
[Miller 2009] W.H. Miller, The Journal of Physical Chemistry 113 (2009) 1405
16


## Page 17


[Anslyn & Doughtery 2006] E.V. Anslyn, D.A. Doughtery, Modern Physical Or-
ganic Chemistry, University Science Books (2006) ; pp 365373
[Van Voorhis et al. 2010] Troy Van Voorhis, Tim Kowalczyk, Benjamin Kaduk,
Lee-Ping Wang and Qin Wu, Annu. Rev. Phys. Chem 61 (2010) 149-70 doi:
10.1146/annurev.physchem.012809.103324
[Leggett et al. 1987] A.J. Leggett, S. Chakravarty, A.T. Dorsey, M.P.A. Fisher,
A. Garg and W. Zwerger, Rev. Mod. Phys. 59 (1987) 1-85
[Schrieﬀer & Heeger 1979] W.P. Su, J.R. Schrieﬀer, and A.J. Heeger, Phys. Rev.
Lett. 42 (1979) 1698
[Aubry et al. 2001] S. Aubry, G. Kopidakis, A.M. Morgante and G.T. Tsironis,
Physica B 296 (2001) 222-236
[Aubry & Kopidakis 2003] S. Aubry and G. Kopidakis, Int. J. of Mod. Phys. B17
(2003) 3908-3921.
[Aubry 2007] S. Aubry, J. Phys.: Condens. Matter 19 (2007) 255204.
17

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
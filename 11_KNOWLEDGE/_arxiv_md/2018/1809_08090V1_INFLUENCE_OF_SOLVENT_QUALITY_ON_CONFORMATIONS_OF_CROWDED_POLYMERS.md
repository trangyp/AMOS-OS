---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1809.08090v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1809.08090v1_Influence_of_Solvent_Quality_on_Conformations_of_Crowded_Polymers

> Source: 1809.08090v1_Influence_of_Solvent_Quality_on_Conformations_of_Crowded_Polymers.pdf

> Pages: 12

---


## Page 1


arXiv:1809.08090v1  [cond-mat.soft]  21 Sep 2018
Inﬂuence of Solvent Quality on Conformations of Crowded Polymers
Wyatt J. Davis and Alan R. Denton∗
Department of Physics, North Dakota State University, Fargo, ND 58108-6050, USA
The structure and function of polymers in conﬁned environments, e.g., biopolymers in the cy-
toplasm of a cell, are strongly aﬀected by macromolecular crowding. To explore the inﬂuence of
solvent quality on conformations of crowded polymers, we model polymers as penetrable ellipsoids,
whose shape ﬂuctuations are governed by the statistics of self-avoiding walks, appropriate for a
polymer in a good solvent. Within this coarse-grained model, we perform Monte Carlo simulations
of mixtures of polymers and hard-nanosphere crowders, including trial changes in polymer size and
shape. Penetration of polymers by crowders is incorporated via a free energy cost predicted by poly-
mer ﬁeld theory. To analyze the impact of crowding on polymer conformations in diﬀerent solvents,
we compute average polymer shape distributions, radius of gyration, volume, and asphericity over
ranges of polymer-to-crowder size ratio and crowder volume fraction. The simulation results are ac-
curately predicted by a free-volume theory of polymer crowding. Comparison of results for polymers
in good and theta solvents indicates that excluded-volume interactions between polymer segments
signiﬁcantly aﬀect crowding, especially in the limit of crowders much smaller than polymers. Our
approach may help to motivate future experimental studies of polymers in crowded environments,
with possible relevance for drug delivery and gene therapy.
I.
INTRODUCTION
Polymer conformations can be inﬂuenced by macro-
molecular crowding [1, 2], which occurs when the vol-
ume accessible to a macromolecule is reduced by the
presence of other macromolecules (crowders) in solution,
or by geometric conﬁnement imposed by hard bound-
aries [3, 4]. Over the past four decades, this phenomenon
has drawn increasing interest within the biophysics com-
munity for its ubiquity in cellular and other biological
environments [5–13].
Inside cells, macromolecules oc-
cupy up to 20% of the volume of the cytoplasm and
up to 40% of the volume of the nucleoplasm [14, 15].
Excluded-volume interactions with crowders inﬂuences
the conformational and diﬀusional behavior of biopoly-
mers (proteins, RNA, DNA) within cells [4, 16] and can
signiﬁcantly modify biomolecular processes, such as pro-
tein folding [17]. Macromolecular crowding also has been
implicated in promoting polymer aggregation associated
with cataract formation [18] and in the pathogenesis
of neurodegenerative diseases, such as Alzheimer’s dis-
ease [19]. Closely related is the conﬁnement of polymers
by nanoparticles in nanocomposite materials [20–26].
The impact of crowding on biopolymer structure and
function has been investigated in a variety of modeling
and experimental studies [27–39]. For example, in a se-
ries of computational studies [32–35], the structure and
function of RNA were shown to be strongly inﬂuenced
by crowding. Recent experiments combined ﬂuorescence
microscopy and particle tracking methods to show that
DNA conformations and mobility respond to crowding
by dextran (mimicing cytoplasm conditions) [36, 37].
Other experiments showed that crowding by dextran or
polyethylene glycol (PEG) inﬂuences the stability and
∗alan.denton@ndsu.edu
folding of actin [38]. Diﬀusion NMR and neutron scat-
tering were used to probe the size (radius of gyration)
of PEG in aqueous solution with Ficoll 70 crowders [39].
While many such studies have explored the impact of
crowding on polymer size, relatively few thus far have
addressed the inﬂuence of crowding on polymer shape.
The signiﬁcance of aspherical polymer conformations
was recognized by Kuhn [40], who pointed out that the
gross shape of a linear polymer, when viewed from a refer-
ence frame tied to the principal axes of the chain, matches
that of an elongated, ﬂattened ellipsoid. A linear poly-
mer chain can be realistically modeled by a random walk,
whose steps are analogous to polymer segments. Math-
ematical studies have demonstrated that an ensemble of
random walks, analogous to an ensemble of polymer con-
formations, can be characterized by statistical distribu-
tions of size and shape [41–48]. The conformations of a
random walk (or polymer chain) can be quantiﬁed by the
gyration tensor, whose eigenvalues (in the principal axis
frame) determine the radius of gyration and the principal
radii of a general ellipsoid.
Early statistical mechanical studies of an ideal polymer
(i.e., in a theta (θ) solvent), modeled as a freely-jointed,
segmented chain or a random walk (RW) of independent
steps, yielded accurate approximations [49–52], and an
exact expression [53, 54], for the probability distribu-
tion of the radius of gyration.
Subsequent simulation
studies produced accurate ﬁtting formulas for the distri-
butions of the gyration tensor eigenvalues of ideal (RW)
polymers [55–57] and nonideal, self-avoiding walk (SAW)
polymers [58].
The inﬂuence of solvent on excluded-volume interac-
tions between segments of a polymer in a dilute solution,
and in turn on scaling with segment number N (or molec-
ular weight) of the average radius of gyration Rg is well
understood [59, 60].
A polymer in a θ solvent, mod-
eled by a random walk, has Rg ∼N 1/2, while a polymer
in a good solvent, modeled by a self-avoiding walk, has


## Page 2


2
Rg ∼N 3/5 (roughly).
For polymers in crowded envi-
ronments, however, the inﬂuence of solvent on size and
shape distributions is relatively poorly understood [61].
In previous work, we studied the inﬂuence of nanopar-
ticle crowding on the conformations of polymers in θ sol-
vents – speciﬁcally, the radius of gyration distribution
within a spherical polymer model [62] and the shape dis-
tribution within the ellipsoidal polymer model [63–65].
The purpose of the present paper is to investigate the
inﬂuence of solvent quality (good vs. θ) on the confor-
mations of crowded polymers. By comparing data from
molecular simulations with predictions from free-volume
theory, we demonstrate the importance of solvent quality
for the sizes and shapes of crowded polymers. In Sec. II,
we review the coarse-grained model of polymers as soft,
penetrable ellipsoids. In Sec. III, we outline our computa-
tional methods: Monte Carlo simulation and free-volume
theory. In Sec. IV, we present and interpret results for
shape distributions and average geometric properties of
crowded polymers in good solvents. Finally, in Sec. V,
we conclude and suggest possible extensions of our work.
II.
MODELS
A.
Coarse-Grained Model of Polymer Coil
FIG. 1.
Model of a linear polymer coil (red chain) ap-
proximated as a general ellipsoid that ﬂuctuates in size and
shape according to random-walk statistics and is penetrable
by hard-sphere nanoparticles (blue spheres).
To eﬃciently explore the inﬂuence of nanoparticle
crowding on the conformations of polymers in good sol-
vents, we adopt a coarse-grained model of a polymer as a
ﬂuctuating ellipsoid whose shape distribution is governed
by the gyration tensor of a self-avoiding walk (Fig. 1):
T =
1
N
N
X
i=1
ri ri ,
(1)
where ri is the position relative to the center of mass of
segment (step) i of N total segments. The eigenvalues
of the gyration tensor – Λ1, Λ2, Λ3 in three dimensions
– determine the radius of gyration of the polymer in a
particular conformation:
Rp =
 
1
N
N
X
i=1
r2
i
!1/2
=
p
Λ1 + Λ2 + Λ3 .
(2)
(For reference, the gyration tensor relates to the moment
of inertia tensor I via T = R2
p1 −I, with unit tensor 1.)
The root-mean-square (rms) radius of gyration, which
can be measured in scattering experiments, is given by
Rg =
q
R2p

=
p
⟨Λ1 + Λ2 + Λ3⟩,
(3)
where the angular brackets denote an ensemble average
over polymer conformations.
If the ensemble average in Eq. (3) is deﬁned relative
to a frame of reference that rotates with the polymer’s
principal axes and, furthermore, the principal axes are
labelled to preserve the order of the eigenvalues from
largest to smallest (Λ1 > Λ2 > Λ3), then the average
tensor describes an anisotropic object [45, 46]. The eigen-
values of the gyration tensor deﬁne an ellipsoid,
x2
Λ1
+ y2
Λ2
+ z2
Λ3
= 3 ,
(4)
where (x, y, z) are the coordinates of a point on the sur-
face and the eigenvalues relate to the principal radii Ri
via Λi = R2
i /3 (i = 1, 2, 3). This general ellipsoid is a
coarse-grained representation of the average shape of the
polymer (e.g., the tertiary structure of a biopolymer).
Each triplet of eigenvalues {Λ1, Λ2, Λ3} characterizes a
unique polymer conformation and ellipsoid shape.
In the absence of crowders, a three-dimensional SAW,
modeling conformations of a linear polymer in a good
solvent, has an average shape (eigenvalue) distribution
determined by Monte Carlo simulations [58] to be accu-
rately described by a probability distribution,
P0(Λ1, Λ2, Λ3) =
3
Y
i=1
Pi0(Λi) ,
(5)
where the three factors are given by
Pi0(Λi) =
1
Γ(νi)
νi
αi
νiΛi
αi
νi−1
exp

−νiΛi
αi

(6)
and αi and νi are ﬁt parameters, tabulated in Table I for
polymer chains of length N = 104. The factorized form
of Eq. (5) assumes independent eigenvalues – aside from
the ordering condition – an assumption that proves ac-
curate for suﬃciently long polymers, with the exception
of rare conformations in which an extreme extension in
one direction can aﬀect the probability of an extension
in an orthogonal direction.


## Page 3


3
TABLE I. Parameters for shape distribution in Eq. (6) [58]
for polymer chains of length N = 104.
eigenvalue i
αi
νi
Γ(νi)
1
7591.0120 3.35505 2.84226
2
1604.3861 4.71698 15.8132
3
544.16323 5.84822 92.8188
TABLE II. Parameters for shape distribution in Eq. (7).
eigenvalue i
ai
bi
ci
1
11847.9
2.35505 22.3563
2
1.11669×109 3.71698 148.715
3
1.06899×1014 4.84822 543.619
An uncrowded SAW polymer of N segments, each of
(Kuhn) length l, has rms (average) radius of gyration
Rg(0) = CN νl, with Flory exponent ν = 0.588 and am-
plitude C = 0.44108 [58]. For comparison, in a θ solvent,
Rg(0) =
p
N/6 l. Since the gyration tensor eigenvalues
increase with N in proportion to N 2ν, it is convenient
to deﬁne scaled eigenvalues, λi ≡Λi/(N νl)2, in terms of
which the shape distribution can be expressed as
Pi0(λi) = aiλbi
i exp(−ciλi) ,
(7)
where the parameters ai, bi, and ci, derived from αi and
νi, are tabulated in Table II. The individual eigenvalue
distributions diﬀer somewhat from the factors in Eqs. (6)
and (7). Each is obtained from the parent distribution
[Eq. (5)] by integrating over the other two eigenvalues,
with limits set by eigenvalue ordering (λ1 > λ2 > λ3):
P1(λ1) =
Z λ1
0
dλ2
Z λ2
0
dλ3 P0(λ) ,
(8)
P2(λ2) =
Z ∞
λ2
dλ1
Z λ2
0
dλ3 P0(λ) ,
(9)
P3(λ3) =
Z ∞
λ3
dλ1
Z λ1
λ3
dλ2 P0(λ) ,
(10)
where λ ≡{λ1, λ2, λ3} represents a triplet of scaled eigen-
values. For comparison, Fig. 2 shows the scaled eigen-
value distributions of uncrowded polymers in good and θ
solvents. Note that, accounting for the diﬀerent scaling
factors – N for RW polymers, but N 1.176 for SAW poly-
mers – the unscaled eigenvalues are signiﬁcantly larger
for a SAW polymer in a good solvent than for a RW
polymer in a θ solvent.
Amidst crowders of volume fraction φc, the rms radius
of gyration Rg(φc) and the principal radii Ri(φc) are re-
lated to the scaled eigenvalues via
Rg(λ1, λ2, λ3, φc) = Rg(0)
C
p
⟨λ1 + λ2 + λ3⟩
(11)
and
Ri(λi, φc) = Rg(0)
C
p
3λi = 3.9269Rg(0)
p
λi .
(12)
For comparison, in a θ solvent, Ri = Rg(0)√18λi and
Rg(φc) = Rg(0)
p
6 ⟨λ1 + λ2 + λ3⟩.
(13)
The principal radii determine the average volume of the
ellipsoidal polymer via
vp(λ1, λ2, λ3, φc) = 4π
3 ⟨R1R2R3⟩.
(14)
0
0.05
0.1
λ
0
50
100
P(λ, φc=0)
 SAW
 RW
0
0.1
0.2
0.3
0.4
0.5
λ1
0
2
4
6
8
P1(λ1, φc=0)
λ3
λ2
λ1
FIG. 2.
Probability distributions P(λ) of scaled gyration
tensor eigenvalues λ = {λ1, λ2, λ3} of uncrowded polymers
(φc = 0) in a good solvent (SAW, solid curves) and in a θ
solvent (RW, dashed curves).
Inset: largest eigenvalue λ1
distributions.
The deviation of a polymer’s average shape from spher-
ical is conveniently quantiﬁed by an asphericity parame-
ter [45, 46], deﬁned as
A = 1 −3⟨λ1λ2 + λ1λ3 + λ2λ3⟩
⟨(λ1 + λ2 + λ3)2⟩
.
(15)
A perfect sphere has all eigenvalues equal and A = 0,
while an elongated object with one eigenvalue much
larger than the others has A ≃1. Crowding agents mod-
ify the eigenvalue probability distributions and, in turn,
the rms radius of gyration and asphericity of a polymer.
As in our previous studies of crowding of RW poly-
mers in a θ solvent [63–65], our model extends the classic
Asakura-Oosawa-Vrij (AOV) model of colloid-polymer
mixtures [66, 67], which idealizes nonadsorbing polymers
as eﬀective spheres of ﬁxed size (radius of gyration). Al-
though qualitatively describing depletion-induced demix-
ing of colloid-polymer mixtures, the AOV model com-
pletely neglects polymer conformational ﬂuctuations, the
inﬂuence of crowding on polymer size and shape, and the
penetrability of polymers by smaller colloids (nanoparti-
cles).
We investigate polymer crowding within an ex-
tended model of polymer-nanoparticle mixtures that in-
cludes all of these features.


## Page 4


4
B.
Polymer Penetration Model
To allow for penetration of polymers by crowders,
we further extend the AOV model, following previous
work [63–65, 68], by deﬁning an average penetration free
energy ε that represents the average loss in conforma-
tional entropy of a polymer upon penetration by a hard-
nanosphere crowder of radius Rc (see Fig. 1). The de-
pendence of ε on q can be motivated from a simple scal-
ing argument for an uncrowded polymer in the N →∞
(q ≫1) limit [59]. Given that ε should be proportional
to both the fraction of polymer volume occupied by the
nanosphere and the number of polymer segments, we
make the scaling ansatz,
βε ∼R3
c
vp
Y (q) ,
(16)
where the scaling function Y (q) is proportional to N.
Since N ∼[Rg(0)]1/ν in a good solvent, it follows that
Y (q) ∼q1/ν, which implies
βε ∼R3
c
vp
q1/ν ∼R3
g(0)
vp
q1/ν−3 ,
(17)
where q
≡Rg(0)/Rc is the uncrowded polymer-to-
crowder size ratio. For a SAW polymer in a good solvent
at temperature T , polymer ﬁeld theory [69–72] predicts
ν = 0.588 and, in the limit in which the crowders are
much smaller than the polymers (q ≫1):
βε ≃18.4R3
g(0)
vpq1.29932 .
(18)
For q <∼1, nanosphere insertions are so costly in free en-
ergy that the polymer is practically impenetrable. Crow-
ders then inﬂuence the polymer shape mostly from out-
side. Conversely, for q ≫1, penetration is less costly
and crowding can occur from both inside and outside the
polymer. If the polymer were approximated as a sphere
of ﬁxed radius, we would have vp = (4π/3)R3
g(0) and
βε ≃
4.4
q1.29932 ,
(19)
an expression that has been used in previous studies of
colloid-polymer mixtures in the q ≫1 limit [73]. In our
study, however, we used the more general expression of
Eq. (18), which applies to a polymer of arbitrary shape.
In comparison, for a RW polymer, βε ≃4πR3
g(0)/(qvp),
reducing to βε ≃3/q in the spherical polymer model.
The coarse-grained ellipsoidal polymer model should
be reasonable if, in the time required for the crowders
to signiﬁcantly change their conﬁguration, the polymer
has suﬃcient time to equilibrate by visiting a representa-
tive sample of its possible conformations. We must then
assume a separation of time scales between diﬀusion of
crowders and conformational rearrangement of the poly-
mer. For purposes of a rough estimate, we assume that
a statistically independent conﬁguration of crowders is
achieved when each crowder diﬀuses a distance compara-
ble to its diameter, while the polymer conformation equi-
librates in the time it takes for each segment to diﬀuse
a distance comparable to the segment length.
Equat-
ing these distances – presuming similar diﬀusion rates –
gives a lower limit on the allowed size of a crowder (up-
per limit on q) for which the model is reasonable. This
simple estimate yields q ≃
p
N/6 for a RW polymer and
q ≃CN ν for a SAW polymer. Thus, for most practi-
cal purposes, and certainly for the systems considered in
Sec. IV, the coarse-grained ellipsoidal polymer model is
quite justiﬁed.
III.
METHODS
A.
Monte Carlo Simulation
Adapting methods developed in previous studies of
polymer crowding [63–65], we simulated a single ellip-
soidal polymer, ﬂuctuating in conformation according to
the model described in Sec. II A, immersed in a ﬂuid
of hard nanospheres.
In the canonical ensemble, with
ﬁxed numbers of particles at constant temperature in a
cubic cell of ﬁxed volume with periodic boundary con-
ditions, we implemented a variation of the Metropolis
Monte Carlo (MC) algorithm.
Trial displacements of
nanospheres and polymers were performed by translat-
ing the center of a particle at position (x, y, z) to a new
position (x + ∆x, y + ∆y, z + ∆z), where ∆x, ∆y, and
∆z were chosen independently and randomly in the range
[−0.2Rc, 0.2Rc].
Trial displacements of polymers were coupled with trial
rotations and shape changes as a single composite move.
To ensure uniform sampling of the polymer orientation,
deﬁned by a unit vector u aligned with the long axis of
the ellipsoid, we generated a new orientation unew from
an old orientation uold via [74]
unew = uold + τv
|uold + τv| ,
(20)
where v is a randomly oriented unit vector and the toler-
ance τ was chosen randomly in the range [−0.1, 0.1]. Trial
variations in polymer shape were performed by changing
one set of gyration tensor eigenvalues λold = {λ1, λ2, λ3}
to a new set λnew = {λ1 + ∆λ1, λ2 + ∆λ2, λ3 + ∆λ3},
where ∆λ1, ∆λ2, and ∆λ3 were chosen independently
and randomly in the ranges [−0.01, 0.01], [−0.003, 0.003],
and [−0.001, 0.001]. A trial move (displacement, rota-
tion, and shape change) was accepted with probability
Pacc = min
P0(λnew)
P0(λold) e−β∆F, 1

,
(21)
where ∆F is the change in free energy resulting from the
change in number of particle overlaps. For the polymer-
nanosphere penetration energy, we used Eq. (18) with the


## Page 5


5
polymer volume predicted by free-volume theory. While
in principle we should iterate until vp computed from the
simulation equals vp predicted by the theory, in prac-
tice the theory proved suﬃciently accurate that no itera-
tions were required. A trial move resulting in overlap of
hard nanospheres (yielding inﬁnite ∆F) was immediately
rejected.
A move that creates/eliminates a polymer-
nanosphere overlap yields ∆F = ±ε (see Sec. II B).
During a simulation, we checked whether a trial move
resulted in overlap of a nanosphere with the polymer. For
each candidate – identiﬁed as a nanosphere whose cen-
ter lies inside a sphere centered on the ellipsoid of radius
equal to the sum of the nanosphere radius and the longest
principal radius of the ellipsoid – we diagnosed overlap by
computing the closest distance between the nanosphere
center and the surface of the ellipsoid, which involves
computing the roots of a 6th-order polynomial [75]. Af-
ter an accepted change in polymer conformation, we re-
ordered the eigenvalues by size. During each simulation,
we averaged over MC steps, a step being deﬁned as a
trial displacement of every nanosphere and a trial change
in polymer conformation, to compute ensemble averages
of eigenvalue distributions and polymer geometric prop-
erties (see Sec. IV). We coded our simulations in Java
within the Open Source Physics Library [76]. Figure 3
shows a typical snapshot from a simulation.
FIG. 3.
Snapshot of a simulation of Nn = 216 nanospheres
(blue spheres) and one polymer (red ellipsoid) in a cubic sim-
ulation cell.
The rms radius of gyration of the uncrowded
polymer equals ﬁve times the nanosphere radius (q=5).
B.
Free-Volume Theory of Crowding
To guide choices of system parameters and to help
interpret our simulation results, we adapted a free-
volume theory previously developed for colloid-polymer
mixtures [63–65]. The theory generalizes the theory of
Lekkerkerker et al. [77] from the AOV model [66, 67] of
hard, spherical polymers to a model of soft, penetrable,
aspherical polymers, as described in Sec. II.
The free-volume theory approximates the mean value
of a quantity Q(λ), averaged over polymer shapes, by
⟨Q⟩=
Z ∞
0
dλ1
Z λ1
0
dλ2
Z λ2
0
dλ3 Q(λ)P(λ, φc) ,
(22)
where
P(λ, φc) = α(λ, φc)
αeﬀ(φc) P0(λ)
(23)
is the shape probability distribution of the crowded poly-
mer, α(λ, φc) is the free-volume fraction of a polymer of
shape λ ≡{λ1, λ2, λ3} amidst hard nanospheres of aver-
age volume fraction φc, and
αeﬀ(φc) =
Z ∞
0
dλ1
Z λ1
0
dλ2
Z λ2
0
dλ3 α(λ, φc)P0(λ)
(24)
is the eﬀective free-volume fraction, averaged over poly-
mer shapes. Note that the limits of the eigenvalue in-
tegrals in Eqs. (22) and (24) are chosen to respect the
eigenvalue ordering (λ1 > λ2 > λ3). Previous studies of
crowding of RW (ideal) polymers [63–65] did not impose
eigenvalue ordering.
While this simple approximation
proves very accurate and eﬃcient for RW polymers, it
turns out to be less accurate for SAW polymers, increas-
ingly so with increasing crowder volume fraction.
According to the Widom particle insertion theo-
rem [78], the free-volume fraction is related to the av-
erage work W required to insert a polymer of shape λ
into a sea of hard spheres of volume fraction φc via
α(λ, φc) = exp[−βW(λ, φc)] .
(25)
The average insertion work or, equivalently, the free en-
ergy required to distort the hard-sphere ﬂuid and create
the volume and interfacial area suﬃcient to accommodate
the polymer, can be expressed as
W(λ, φc) = p(φc)vp(λ) +
I
S
dS γ(φc, r) ,
(26)
where p and γ are the pressure and interfacial tension of
the hard-sphere ﬂuid, respectively, vp(λ) is the volume
of the polymer, and the integral is over a closed surface
S, deﬁned by the surface of the ellipsoidal polymer and
parametrized by surface position vector r. This expres-
sion conveniently and conceptually separates thermody-
namic properties of the hard-sphere ﬂuid from geometric
properties of the polymer.


## Page 6


6
Assuming a smooth interface between the polymer and
the hard-sphere ﬂuid, the interfacial tension, which de-
pends on the curvature of the interface – dictated by the
polymer shape – can be expanded in powers of the mean
curvature
K(r) = 1
2

1
R1(r) +
1
R2(r)

(27)
and the Gaussian curvature
H(r) =
1
R1(r)R2(r) ,
(28)
where R1(r) and R2(r) are the local radii of curvature at
a point r on the interface. Thus,
γ(φc, r) = γ∞(φc)+κ(φc)K(r)+ ¯κ(φc)H(r)+· · · , (29)
where γ∞is the interfacial tension of a ﬂat interface
(with inﬁnite radii of curvature) and the coeﬃcients κ(φc)
and ¯κ(φc) are bending rigidities of the hard-sphere ﬂuid,
which depend only on the hard-sphere volume fraction.
Substituting Eq. (29) into Eq. (26) and integrating over
eigenvalues yields the curvature expansion of the inser-
tion work:
W(λ, φc) = p(φc)vp(λ) + γ∞(φc)ap(λ)
+ κ(φc)cp(λ) + 2π¯κ(φc) + · · · ,
(30)
where ap(λ) is the surface area of the ellipsoidal polymer,
cp(λ) =
I
S
dS K(r)
(31)
is the integrated mean curvature, and we have exploited
the Gauss-Bonnet theorem:
I
S
dS H(r) = 2πχ ,
(32)
where the Euler characteristic χ = 1 for an ellipsoid.
Substituting Eq. (30) into Eq. (25) and neglecting higher-
order terms in the curvature expansion yields an approx-
imation for the polymer free-volume fraction:
α(λ, φc) = exp{−β[p(φc)vp(λ) + γ∞(φc)ap(λ)
+ κ(φc)cp(λ) + 2π¯κ(φc)]} .
(33)
In the limit of an inﬁnitesimally small (point-like) poly-
mer coil (λ →0), vp(λ), ap(λ), and cp(λ) all tend to
zero and the free-volume fraction then reduces to 1 −φc,
implying that
¯κ(φc) = −kBT
2π ln(1 −φc) .
(34)
Finally, to incorporate the penetrability of the polymers,
the crowder volume fraction is replaced by an eﬀective
volume fraction, φ′
c = φc(1 −e−βε) [63–65, 68]. Combin-
ing Eqs. (33) and (34) yields the ﬁnal approximation for
the polymer free-volume fraction:
α(λ, φc) = (1 −φ′
c) exp{−β[p(φ′
c)vp(λ) + γ∞(φ′
c)ap(λ)
+ κ(φ′
c)cp(λ)]} ,
(35)
from which mean values follow via Eqs. (22)-(24).
With knowledge of p(φc), γ∞(φc), and κ(φc) in the
curvature expansion of the insertion work [Eq. (30)], the
free-volume theory can be implemented to predict the
dependence of polymer size and shape on crowding by a
hard-sphere ﬂuid. For example, the radius of gyration
Rg(φc) can be explicitly computed from
Rg(φc) = Rg(0)
C
Z
dλ P(λ, φc)
p
λ1 + λ2 + λ3 .
(36)
To compute the results reported in Sec. IV, we used
the accurate Carnahan-Starling expressions for the hard-
sphere ﬂuid properties [79, 80]:
βp(φc) =
3φc
4πR3c
1 + φc + φ2
c −φ3
c
(1 −φc)3
βγ∞(φc) =
3
4πR2c
φc(2 −φc)
(1 −φc)2 + ln(1 −φc)

βκ(φc) =
3φc
Rc(1 −φc) .
(37)
For the integrated mean curvature, we numerically eval-
uated the integral in Eq. (31) over a grid of eigenvalues
and stored the results in a look-up table for later access.
IV.
RESULTS
A.
Simulation Protocol
For several choices of uncrowded polymer-to-crowder
size ratio q and crowder volume fraction φc, we performed
simulations of a polymer coil (modeled as a ﬂuctuating,
penetrable ellipsoid) and Nn=216 nanosphere crowders,
initialized on a cubic lattice (6 × 6 × 6 array). After an
equilibration stage of 5 × 104 MC steps, we collected
statistics for the three eigenvalues of the gyration tensor
at intervals of 103 MC steps for 104 intervals. For each
parameter combination, we ran ﬁve independent simu-
lations and averaged over runs to obtain statistical er-
rors. We ran test simulations for longer times and larger
systems to ensure that the system had reached equilib-
rium and that ﬁnite-size eﬀects were negligible.
From
the raw eigenvalue data, we obtained probability distri-
butions [Eq. (23)] as histograms (see Figs. 4 and 5) and
computed average polymer geometric properties: radius
of gyration [Eq. (11)], volume [Eq. (14)], and asphericity
[Eq. (15)] (see Figs. 6 and 7).


## Page 7


7
0
0.02
0.04
0.06
0.08
0.1
λ1
0
20
40
60
80
100
P1(λ1,φc)
φc=0.1
φc=0.2
φc=0.3
Theory
Uncrowded
q=5
a)
0
0.01
0.02
0.03
0.04
0.05
λ2
0
50
100
150
200
P2(λ2,φc)
b)
0
0.005
0.01
0.015
0.02
λ3
0
100
200
300
P3(λ3,φc)
c)
FIG. 4. Eigenvalue probability distributions (λ1 > λ2 > λ3)
of gyration tensor of a crowded polymer coil in a good sol-
vent, modeled as a ﬂuctuating, penetrable ellipsoid, governed
by self-avoiding-walk statistics.
Simulation data (symbols)
are compared with predictions of free-volume theory (solid
curves) for a single polymer, with uncrowded rms radius of
gyration equal to ﬁve times the nanoparticle radius (q = 5),
amidst Nn = 216 hard nanosphere crowders of volume fraction
φc = 0.1 (triangles), 0.2 (squares), and 0.3 (circles). Dashed
curves show uncrowded (φc = 0) distributions.
0
0.005
0.01
0.015
0.02
 λ1
0
100
200
300
400
P1(λ1,φc)
φc=0.1
φc=0.2
φc=0.3
Theory
Uncrowded
q=10
a)
0
0.005
0.01
0.015
0.02
λ2
0
200
400
600
P2(λ2,φc)
b)
0
0.002
0.004
0.006
0.008
0.01
λ3
0
200
400
600
800
P3(λ3,φc)
c)
FIG. 5.
Same as Fig. 4, but for uncrowded polymer-to-
nanosphere size ratio q = 10. Notice changes in horizontal
and vertical scales.


## Page 8


8
B.
Comparison of SAW and RW Polymers of
Equal Uncrowded Size
We ﬁrst present and discuss results that illustrate the
inﬂuence of solvent quality on conformations of crowded
SAW and RW polymers having the same uncrowded size
(radius of gyration). Figures 4 and 5 show our simula-
tion results for the eigenvalue probability distributions
for q = 5 and q = 10, respectively, over a range of
crowder volume fraction. Also shown are predictions of
our free-volume theory.
Simulation and theory are in
reasonable agreement, deviations increasing with φc as
polymer-crowder correlations strengthen, and both pre-
dict progressive shifts to lower eigenvalues (smaller prin-
cipal radii) and narrowing of the distributions with in-
creasing crowder volume fraction. These results reveal
that, with increasing φc, not only do polymer coils tend
to contract along each principal axis, but also ﬂuctua-
tions in size and shape are suppressed – more so for
q = 10 than for q = 5. The slightly larger deviations
between theory and simulation at larger q – evident es-
pecially at higher φc – reﬂect limitations of the theory
associated with neglecting higher-order terms in the cur-
vature expansion of the interfacial tension [Eqs. (29) and
(30)]. These deviations propagate forward and aﬀect the
predicted size and shape of the crowded polymer, which
depend on averages over the eigenvalue distributions.
Figure 6 illustrates the inﬂuence of crowding on geo-
metric properties of a polymer coil. The average radius
of gyration, volume, and asphericity of the polymer all
decrease monotonically with increasing crowder volume
fraction. Polymers of uncrowded Rg equal to the crow-
der radius (q = 1) are relatively insensitive to crowding,
experiencing only a 15% reduction in size at φc = 0.3,
while larger polymers (q = 5, 10) contract signiﬁcantly
more than smaller polymers at the same φc. The crowd-
ing eﬀect predicted at q = 1, though relatively weak,
is stronger than that determined from the experiments
of ref. [39], in which no signiﬁcant change in radius of
gyration was observed over the same range of φc. Al-
though its source is unclear, this quantitative disagree-
ment may result from some mismatch between our model
and the experimental system. It may be, for example,
that the conformational statistics exhibited by the poly-
mer (PEG) in water are not quite those of a SAW, or
that the interactions between crowding agents (Ficoll 70)
diﬀer from hard-sphere interactions, or that the polymer-
crowder interactions are not purely entropic.
The tendency of polymer contraction to increase with
increasing q, at ﬁxed φc, is a result of the free energy
cost associated with penetration of a polymer by crow-
ders. Figure 7 illustrates more directly the variation of
polymer geometry with size ratio, showing that radius of
gyration, volume, and asphericity all decrease monotoni-
cally with increasing q. Evidently, the larger the polymer
relative to the crowder, the more severe the inﬂuence of
crowding on polymer conformation. This trend can be
explained by the fact that the total penetration energy
scales as q1/ν = q1.7 for a given φc. The latter scaling fol-
lows from the scaling of the penetration energy as q1/ν−3
[Eq. (17)] and the number of penetrating nanospheres
per polymer as q3. While our results for the dependence
of Rg on φc and q are qualitatively consistent with the
measurements of Palit et al. [39] for aqueous solutions of
PEG and Ficoll 70, in that polymer contraction increases
monotonically with increasing q and φc, quantitative dif-
ferences exist.
Future studies may determine whether
the discrepancies can be accounted for by the particular
chain statistics of PEG in water or by non-hard-sphere
interactions between the Ficoll 70 crowders or by other
limitations of our model.
Also shown in Figs. 6 and 7 are corresponding predic-
tions of free-volume theory for both SAW and RW poly-
mers. Results for SAW polymers from simulation and
theory generally agree closely, as found also in previous
studies of RW polymer [63–65]. For clarity of presenta-
tion, we do not include here previously reported simu-
lation data for RW polymers, as they are in near-exact
agreement with simulation. As noted in Sec. III A, the
output values of vp are suﬃciently close to the input val-
ues (from free-volume theory) that no iterations between
simulation and theory were required. We emphasize that
imposing ordering of eigenvalues turns out to have neg-
ligible eﬀect on the results for RW polymer, but is more
signiﬁcant for SAW polymer, especially at higher φc.
While polymers in diﬀerent solvents show qualitatively
similar responses to crowding, all geometric measures de-
creasing with increasing φc, there are signiﬁcant quanti-
tative diﬀerences. For the same q and φc, a SAW poly-
mer (in a good solvent) has a consistently smaller volume
[Figs. 6b and 7b] and higher asphericity [Figs. 6c and
7c] than a RW polymer (in a θ solvent). Thus, a SAW
polymer in a crowded environment is more compressed
and more elongated than a RW polymer of the same un-
crowded size (same q). The comparison of crowded sizes
of SAW and RW polymer is somewhat more complicated.
Fig. 6a shows that for q = 1 the SAW polymer is con-
sistently less contracted over the whole range of crowder
volume fraction, while for q = 5 and q = 10, the SAW
polymer contracts less at lower φc, but more at higher φc.
This cross-over with increasing q and φc in the degree of
contraction of SAW and RW polymers reﬂects a complex
interplay between, on the one hand, chain statistics and
conformational entropy, and on the other hand, penetra-
tion free energy (see Sec. II B). When we consider, how-
ever, polymers of the same segment number (molecular
weight), rather than the same uncrowded size, the re-
sponses of SAW and RW polymers to crowding are more
distinct, as we discuss in the next section.
C.
Comparison of SAW and RW Polymers of
Equal Segment Number
Thus far, when comparing the crowded conformations
(sizes and shapes) of a SAW polymer in a good solvent


## Page 9


9
0
0.1
0.2
0.3
Crowder Volume Fraction  φc
0
0.5
1
Radius of Gyration  Rg(φc) / Rg(0)
q=1 
q=5
q=10
Theory (SAW)
Theory (RW)
a)
0
0.1
0.2
0.3
Crowder Volume Fraction  φc
0
0.5
1
1.5
2
Polymer Volume  vp(φc) / Rg
3(0)
b)
0
0.1
0.2
0.3
Crowder Volume Fraction  φc
0
0.1
0.2
0.3
0.4
0.5
Asphericity  A
0
0.1
0.2
0.3
0
0.1
0.2
0.3
0.4
0.5
c)
FIG. 6.
Average geometric properties a polymer (modeled
as a ﬂuctuating, penetrable ellipsoid) vs. nanosphere crowder
volume fraction φc: (a) rms radius of gyration, (b) volume, (c)
asphericity. Simulation data are shown for SAW polymers of
uncrowded polymer-to-nanosphere size ratio q = 1 (triangles),
q = 5 (circles), and q = 10 (squares). For some points, error
bars are smaller than symbols. Corresponding predictions of
free-volume theory are shown for SAW polymers (solid curves)
and RW polymers (dashed curves).
4
6
8
10
Polymer-Crowder Size Ratio  q
0
0.5
1
Radius of Gyration  Rg(φc) / Rg(0)
φc=0.1
φc=0.2
φc=0.3
Theory (SAW)
Theory (RW)
a)
4
6
8
10
Polymer-Crowder Size Ratio  q
0
0.5
1
Polymer Volume  vp(φc) / Rg
3(0)
b)
4
6
8
10
Polymer-Crowder Size Ratio  q
0
0.1
0.2
0.3
0.4
0.5
Asphericity  A
c)
FIG. 7. Average geometric properties of a polymer (modeled
as a ﬂuctuating, penetrable ellipsoid) vs. uncrowded polymer-
to-nanosphere size ratio q: (a) radius of gyration, (b) volume,
(c) asphericity. Simulation data are shown for SAW polymers
and nanosphere crowder volume fraction φc = 0.1 (triangles),
φc = 0.2 (circles), and φc = 0.3 (squares). For some points,
error bars are smaller than symbols. Corresponding predic-
tions of free-volume theory are shown for SAW polymers (solid
curves) and RW polymers (dashed curves).


## Page 10


10
with those of a RW polymer in a θ solvent, we have con-
sidered polymers of the same uncrowded radius of gyra-
tion (same q value). Since the scaling of Rg(0) with seg-
ment number N depends on the solvent quality [59] (see
Sec. II A), we have implicitly been comparing polymers
of diﬀerent segment numbers.
Our predictions, while
of fundamental interest and qualitatively consistent with
observed trends, may be diﬃcult to compare with exper-
iments in which polymers of the same molecular weight
are studied under diﬀerent solvent conditions. To facili-
tate more direct comparisons with experiments, we now
compare predictions for polymers of equal segment num-
ber in good and θ solvents.
Given the segment (Kuhn) length l of a linear polymer
coil, the radius of a spherical crowder, and the size ratio
qRW of a RW polymer in a θ solvent, the scaling rela-
tions (Sec. II A) determine the size ratio qSAW of a SAW
polymer of equal segment number in a good solvent:
qSAW = C6ν(Rc/l)2ν−1q2ν
RW .
(38)
As an example, motivated by the recent experiments of
Palit et al. [39], we consider aqueous solutions of PEG
and Ficoll 70 crowder. Taking the Kuhn length of PEG
in water – considered good solvent conditions at room
temperature – as l = 7.6 ˚A [81] (twice the persistence
length), the radius of Ficoll 70 as Rc = 55 ˚A [82], and
qRW = 3, we obtain qSAW ≃7 and N ≃3000 segments.
(For comparison, qSAW = 1 translates into qRW ≃0.6 and
N ≃120.)
Figure 8 compares the geometric properties of this
polymer in good and θ solvents. With increasing crow-
der volume fraction, the inﬂuence of crowding on con-
formations of a polymer of a given molecular weight –
quantiﬁed by radius of gyration, volume, and asphericity
– is consistently stronger in a good solvent than in a θ
solvent. These trends are not surprising, given our gen-
eral understanding that crowding eﬀects become more
prominent with increasing q, and considering that qSAW
here exceeds qRW by more than a factor of two. What is
perhaps most notable is that the average polymer shape
(asphericity), while strongly dependent on crowder vol-
ume fraction, is relatively insensitive – compared with
average polymer size – to a change in solvent quality. It
is worth noting that our Rg vs. φc data have a sign of
curvature (positive) that is opposite that of the experi-
mental data [39]. Quantitative comparisons are compli-
cated, however, by the relative simplicity of our model
and the fact that, for given molecular weights of PEG,
the measured uncrowded radii of gyration obey neither
RW nor SAW chain statistics.
0
0.1
0.2
0.3
Crowder Volume Fraction  φc
0
0.5
1
Radius of Gyration  Rg( φc) / Rg(0)
q=3 (RW) 
q=7 (SAW)
Simulation
a)
0
0.1
0.2
0.3
Crowder Volume Fraction  φc
0
0.5
1
1.5
2
Polymer Volume  vp(φc) / Rg
3(0)
b)
0
0.1
0.2
0.3
Crowder Volume Fraction  φc
0
0.1
0.2
0.3
0.4
0.5
Asphericity  A
0
0.1
0.2
0.3
0
0.1
0.2
0.3
0.4
0.5
c)
FIG. 8. Average geometric properties of PEG (modeled as
a ﬂuctuating, penetrable ellipsoid) vs.
volume fraction φc
of Ficoll 70 crowders (modeled as hard spheres) in water. (a)
radius of gyration, (b) volume, and (c) asphericity of the poly-
mer. Simulation data (symbols) and theoretical predictions
(solid curves) for SAW model of a polymer in a good solvent
with q ≃7 are compared with predictions for RW model of
the same polymer in a θ solvent with q = 3 (dashed curves).
For both cases, the polymer contains N ≃3000 segments,
comparable to the experiments of ref. [39].


## Page 11


11
V.
CONCLUSIONS
To summarize, we have investigated the dependence
on solvent quality of polymer conformations in crowded
environments. For computational eﬃciency and concep-
tual simplicity, we modeled a polymer coil as an eﬀective
ellipsoid whose size and shape ﬂuctuate according to the
underlying statistics of random walks. Speciﬁcally, ﬂuc-
tuations of the principal radii follow the probability dis-
tributions of the gyration tensor eigenvalues of either a
self-avoiding walk – for a polymer in a good solvent – or
a random walk – for a polymer in a θ solvent. Crowders
are modeled as hard-sphere nanoparticles that mutually
interact via a hard-sphere pair potential and are allowed
to penetrate the volume enclosed by polymers with an
average free energy cost predicted by ﬁeld theory.
We implemented this coarse-grained model of polymer-
crowder mixtures via Monte Carlo simulation and free-
volume theory for polymers in good and θ solvents. As
input to both simulations and theory, we used eigenvalue
distributions previously determined from molecular sim-
ulations of random walks. Our simulation data indicate
that, with increasing crowder volume fraction and un-
crowded polymer-to-crowder size ratio q, polymers be-
come smaller and more compact (i.e., more spherical), in
good agreement with predictions of free-volume theory.
While the conformations of SAW and RW polymers dis-
play similar qualitative trends, they exhibit signiﬁcant
quantitative diﬀerences. For polymers that are equal in
either radius of gyration or segment number, the inﬂu-
ence of crowding is consistently stronger in a good solvent
than in a θ solvent. This dependence on solvent quality
can be attributed to the important role of segment self-
avoidance on both the statistics and the penetrability of
a polymer chain in a good solvent. Our prediction can
be experimentally tested by measuring the radius of gy-
ration of polymers in dilute and crowded solutions under
diﬀerent solvent conditions, achievable by varying either
temperature or concentration of a cosolvent.
The model considered here, in which polymer shapes
are governed by random-walk statistics and crowders
are treated as inert hard spheres, has the virtue of iso-
lating and highlighting the role of excluded volume in
polymer crowding.
Quantitative description of many
real systems, however, may require incorporating intra-
chain interactions (chain enthalpy), with appropriate un-
crowded eigenvalue distributions, crowder-crowder inter-
actions, and internal structure of crowders. For exam-
ple, real biopolymers may follow diﬀerent chain statis-
tics, while speciﬁc crowders may be compressible and, if
charged, may mutually interact by screened electrostatic
potentials. Moreover, while our model of mobile poly-
mers and crowders is designed to apply most closely to
macromolecular crowding of biopolymers in cellular en-
vironments, a model of polymers amidst ﬁxed obstacles
may be more applicable to polymer nanocomposite ma-
terials. Future work should investigate the dependence
of polymer conformations on chain statistics, crowder-
crowder interactions, crowder structure, and crowder mo-
bility. Further simulations of more explicit (e.g., bead-
spring) models of polymers in crowded environments [32–
35] also would help to test, calibrate, and reﬁne the
coarse-grained ellipsoidal polymer model.
ACKNOWLEDGMENTS
This work was supported by the National Science
Foundation under Grant No. DMR-1106331.
Valuable
discussions with Wei Kang Lim and Sylvio May and help-
ful correspondence with Sergio J. Sciutto are gratefully
acknowledged.
[1] R. J. Ellis, Curr. Opin. Struct. Biol. 11, 114 (2001).
[2] R. J. Ellis, Trends in Biochem. Sci. 26, 597 (2001).
[3] A. P. Minton, J. Biol. Chem. 276, 10577 (2001).
[4] C. Jeon, Y. Jung, and B.-Y. Ha, Soft Matter 12, 9436
(2016).
[5] A. P. Minton, Biophys. J. 32, 77 (1980).
[6] A. P. Minton, Biopolymers 20, 2093 (1981).
[7] A. P. Minton, Biophys. J. 78, 101 (2000).
[8] A. P. Minton, Biophys. J. 88, 971 (2005).
[9] K. Richter, M. Nessling, and P. Lichter, J. Cell Sci. 120,
1673 (2007).
[10] K. Richter, M. Nessling,
and P. Lichter, Biochim. Bio-
phys. Acta 1783, 2100 (2008).
[11] A. H. Elcock, Curr. Opin. Struct. Biol. 20, 1 (2010).
[12] R. Hancock, in Genome Organization and Function in
the Cell Nucleus, edited by K. Rippe (Wiley-VCH, Wein-
heim, 2012) pp. 169–184.
[13] A. R. Denton, in New Models of the Cell Nucleus: Crowd-
ing and Entropic Forces and Phase Separation and Frac-
tals, edited by R. Hancock and K. W. Jeon (Academic
Press, UK, 2013) pp. 27–72.
[14] J. R. C. van der Maarel, Introduction to Biopolymer
Physics (World Scientiﬁc, Singapore, 2008).
[15] R. Phillips, J. Kondev, and J. Theriot, Physical Biology
of the Cell (Garland Science, New York, 2009).
[16] X.-W. Huang, Y. Peng, J.-H. Huang,
and M.-B. Luo,
Phys. Chem. Chem. Phys. 19, 29975 (2017).
[17] M. S. Cheung, Curr. Opin. Struct. Biol. 23, 2012 (2013).
[18] A. Stradner, G. Foﬃ, N. Dorsaz, G. Thurston,
and
P. Schurtenberger, Phys. Rev. Lett. 99, 198103 (2007).
[19] S. Mittal, R. K. Chowhan,
and L. R. Singh, Biochim.
Biophys. Acta, Gen. Subj. 1850, 1822 (2015).
[20] A. I. Nakatani, W. Chen, R. G. Schmidt, G. V. Gordon,
and C. C. Han, Polymer 42, 3713 (2001).
[21] T.
Kramer,
R.
Schweins,
and
K.
Huber,
J. Chem. Phys. 123, 014903 (2005).
[22] T. Kramer, R. Schweins, and K. Huber, Macromol. 38,
151 (2005).
[23] T. Kramer, R. Schweins, and K. Huber, Macromol. 38,
9783 (2005).


## Page 12


12
[24] A. C. Balazs, T. Emrick, and T. P. Russell, Science 314,
1107 (2006).
[25] M. E. Mackay, A. Tuteja, P. M. Duxbury, C. J. Hawker,
B. Van Horn, Z. Guan, G. Chen,
and R. S. Krishnan,
Science 311, 1740 (2006).
[26] K. Nusser, S. Neueder, G. J. Schneider, M. Meyer,
W. Pyckhout-Hintzen, L. Willner, A. Radulescu,
and
D. Richter, Macromol. 43, 9837 (2010).
[27] D. P. Goldenberg, J. Mol. Biol. 326, 1615 (2003).
[28] R. I. Dima and D. Thirumalai, J. Phys. Chem. B 108,
6564 (2004).
[29] M. Cheung, D. Klimov, and D. Thirumalai, Proc. Natl.
Acad. Sci 102, 4753 (2005).
[30] E. Chen, A. Christiansen, Q. Wang, M. S. Cheung, D. S.
Kliger,
and P. Wittung-Stafshede, Biochem. 51, 9836
(2012).
[31] A. Linhananta, G. Amadei, and T. Miao, J. Phys.: Conf.
Ser. 341, 012009 (2012).
[32] N. A. Denesyuk and D. Thirumalai, J. Am. Chem. Soc.
133, 11858 (2011).
[33] N. A. Denesyuk and D. Thirumalai, Biophys. Rev. 5, 225
(2013).
[34] N. A. Denesyuk and D. Thirumalai, J. Phys. Chem. B
117, 4901 (2013).
[35] H. Kang, P. A. Pincus, C. Hyeon,
and D. Thirumalai,
Phys. Rev. Lett. 114, 068303 (2015).
[36] C. D. Chapman, S. Gorczyca,
and R. M. Robertson-
Anderson, Biophys. J. 108, 1220 (2015).
[37] S. M. Gorczyca, C. D. Chapman, and R. M. Robertson-
Anderson, Soft Matter 11, 7762 (2015).
[38] I. A. Gagarskaia, O. I. Povarova, V. N. Uversky, I. M.
Kuznetsova, and K. K. Turoverov, J. Mol. Struct. 1140,
46 (2017).
[39] S. Palit, L. He, W. A. Hamilton, A. Yethiraj,
and
A. Yethiraj, Phys. Rev. Lett. 118, 097801 (2017).
[40] W. Kuhn, Kolloid-Zeitschrift 68, 2 (1934).
[41] M. Fixman and W. H. Stockmayer, Annu. Rev. Phys.
Chem. 21, 407 (1970).
[42] K. ˇSolc, J. Chem. Phys. 55, 335 (1971).
[43] K. ˇSolc, Macromol. 6, 378 (1973).
[44] D. N. Theodorou and U. W. Suter, Macromol. 18, 1206
(1985).
[45] J. Rudnick and G. Gaspari, J. Phys. A: Math. Gen. 19,
L191 (1986).
[46] J. Rudnick and G. Gaspari, Science 237, 384 (1987).
[47] M. Bishop and C. J. Saltiel, J. Chem. Phys. 88, 6594
(1988).
[48] M. Bishop, J. H. R. Clarke, A. Rey, and J. J. Freire, J.
Chem. Phys. 94, 4009 (1991).
[49] M. Fixman, J. Chem. Phys. 36, 306 (1962).
[50] P. J. Flory and S. Fisk, J. Chem. Phys. 44, 2243 (1966).
[51] M. E. Fisher, J. Chem. Phys. 44, 616 (1966).
[52] P. J. Flory, Statistical Mechanics of Chain Molecules
(Wiley, New York, 1969).
[53] H. Fujita and T. Norisuye, J. Chem. Phys.
52, 1115
(1970).
[54] H. Yamakawa, Modern Theory of Polymer Solutions
(Harper & Row, New York, 1970).
[55] S. J. Sciutto, J. Phys. A: Math. Gen. 27, 7015 (1994).
[56] M. Murat and K. Kremer, J. Chem. Phys. 108, 4340
(1998).
[57] F. Eurich and P. Maass, J. Chem. Phys. 114, 7655 (2001).
[58] S. J. Sciutto, J. Phys. A: Math. Gen. 29, 5455 (1996).
[59] P. G. de Gennes, Scaling Concepts in Polymer Physics
(Cornell, Ithaca, 1979).
[60] D. Lhuilier, J. Phys. France 49, 705 (1988).
[61] S. Gooßen, A. R. Br´as, W. Pyckhout-Hintzen, A. Wis-
chnewski, D. Richter, M. Rubinstein, J. Roovers, P. J.
Lutz, Y. Jeong, T. Chang, and D. Vlassopoulos, Macro-
mol. 48, 1598 (2015).
[62] B. Lu and A. R. Denton, J. Phys.: Condens. Matter 23,
285102 (2011).
[63] W. K. Lim and A. R. Denton, J. Chem. Phys. 141,
114909 (2014).
[64] W. K. Lim and A. R. Denton, J. Chem. Phys. 144,
024904 (2016).
[65] W. K. Lim and A. R. Denton, Soft Matter 12, 2247
(2016).
[66] S. Asakura and F. Oosawa, J. Chem. Phys. 22, 1255
(1954).
[67] A. Vrij, Pure & Appl. Chem. 48, 471 (1976).
[68] M.
Schmidt
and
M.
Fuchs,
J. Chem. Phys. 117, 6308 (2002).
[69] E. Eisenriegler, A. Hanke,
and S. Dietrich, Phys. Rev.
E 54, 1134 (1996).
[70] A. Hanke, E. Eisenriegler,
and S. Dietrich, Phys. Rev.
E 59, 6853 (1999).
[71] E. Eisenriegler, J. Chem. Phys. 113, 5091 (2000).
[72] E. Eisenriegler, A. Bringer,
and R. Maassen, J. Chem.
Phys. 118, 8093 (2003).
[73] P. G. Bolhuis, E. J. Meijer, and A. A. Louis, Phys. Rev.
Lett. 90, 068304 (2003).
[74] D. Frenkel and B. Smit, Understanding Molecular Simu-
lation, 2nd ed. (Academic, London, 2001).
[75] J. C. Hart, in Graphics Gems IV, edited by P. S. Heckbert
(Academic, San Diego, 1994) pp. 113–119.
[76] H. Gould, J. Tobochnik,
and W. Christian, Introduc-
tion to Computer Simulation Methods (Addison Wesley,
2006).
[77] H. N. W. Lekkerkerker, W. C.-K. Poon, P. N. Pusey,
A. Stroobants, and P. B. Warren, Europhys. Lett.) 20,
559 (1992).
[78] B. Widom, J. Chem. Phys. 39, 2808 (1963).
[79] S. M. Oversteegen and R. Roth, J. Chem. Phys. 122,
214502 (2005).
[80] J.-P. Hansen and I. R. McDonald, Theory of Simple Liq-
uids, 3rd ed. (Elsevier, London, 2006).
[81] H. Lee, R. M. Venable, A. D. MacKerell,
and R. W.
Pastor, Biophys. J. 95, 1590 (2008).
[82] B. van den Berg, R. Wain, C. M. Dobson,
and R. J.
Ellis, EMBO J. 19, 3870 (2000).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
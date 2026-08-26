---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1810.06726v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1810.06726v1_Geometric_quantization_of_localized_surface_plasmons

> Source: 1810.06726v1_Geometric_quantization_of_localized_surface_plasmons.pdf

> Pages: 25

---


## Page 1


arXiv:1810.06726v1  [physics.optics]  15 Oct 2018
Geometric quantization of localized surface plasmons
Ory Schnitzer1
1Department of Mathematics, Imperial College London,
180 Queen’s Gate, SW7 2AZ, London, UK
Abstract
We consider the quasi-static problem governing the localized surface plasmon modes and per-
mittivity eigenvalues ǫ of smooth, arbitrarily shaped, axisymmetric inclusions.
We develop an
asymptotic theory for the dense part of the spectrum, i.e., close to the accumulation value ǫ = −1
at which a ﬂat interface supports surface plasmons; in this regime, the ﬁeld oscillates rapidly along
the surface and decays exponentially away from it on a comparable scale. With τ = −(ǫ+1) as the
small parameter, we develop a surface-ray description of the eigenfunctions in a narrow boundary
layer about the interface; the fast phase variation, as well as the slowly varying amplitude and
geometric phase, along the rays are determined as functions of the local geometry. We focus on
modes varying at most moderately in the azimuthal direction, in which case the surface rays are
meridian arcs that focus at the two poles. Asymptotically matching the diverging ray solutions
with expansions valid in inner regions in the vicinities of the poles yields the quantization rule
1
τ ∼πn
Θ + 1
2
 π
Θ −1

+ o(1),
where n ≫1 is an integer and Θ a geometric parameter given by the product of the inclusion
length and the reciprocal average of its cross-sectional radius along its symmetry axis.
For a
sphere, Θ = π, whereby the formula returns the exact eigenvalues ǫn = −1 −1/n.
We also
demonstrate good agreement with exact solutions in the case of prolate spheroids.
1


## Page 2


I.
INTRODUCTION
In nanoplasmonics, the surface-plasmon resonances of metallic nanoparticles and nanos-
tructures are exploited in order to manipulate light on nanometric, subwavelength, scales
[1–3]. The plasmonic eigenvalue problem is fundamental to this area of applied physics, as
it determines the plasmonic eigenmodes supported by a given inclusion, or cluster of inclu-
sions [4–8]. The same spectral problem arises in several other areas, such as in the theory
of composite media [9]; the plasmonic spectrum is also closely linked to the specturm of the
Neumann–Poincar´e integral operator [10–12]. There is an enormous body of literature on
this problem, with recent developments including analyses of strongly interacting particles
using separation of variables [13, 14], transformation optics [15], multipole methods [16],
matched asymptotic expansions [17, 18] and layer-potential techniques [12, 19]; analysis of
corners [20, 21]; application to stimulated emission [22] and second-harmonic generation
[23]; regular shape perturbations [24, 25]; extensions incorporating nonlocality [26–29] and
retardation [30–34]; and high-mode-number asymptotics [35, 36].
The plasmonic eigenvalue problem naturally arises when looking for nontrivial time-
harmonic solutions of Maxwell’s equations, in the absence of any external forcing and in
the limit where the inclusion is small compared to the electromagnetic wavelength.
In
the latter regime, a quasi-static description holds in the vicinity of the inclusion, whereby
the ﬁeld can be derived from a potential ϕ.
The plasmonic eigenvalue problem is then
to ﬁnd permittivity eigenvalues ǫ, deﬁned here relative to the background medium, and
corresponding eigenfunctions ϕ that satisfy Laplace’s equation
∇2ϕ = 0
(1)
in the inclusion and background domains, together with the transmission conditions
ϕ(i) = ϕ(o),
ǫ∂ϕ(i)
∂n
= ∂ϕ(o)
∂n
(2)
on the inclusion boundary, where superscripts (i) and (o) henceforth refer to the inside and
outside of the inclusion, respectively. We also require that the potentials attenuate,
ϕ →0,
(3)
at large distances from the inclusion; while it’s actually the gradient that must attenuate,
so that the near ﬁeld matches with outward propagating solutions of Maxwell’s equations,
the present formulation is convenient as it eliminates an immaterial additive freedom.
2


## Page 3


The plasmonic eigenvalues are scale invariant and depend solely on the geometry of the
inclusion; for smooth geometries, the spectrum consists of an inﬁnite discrete set of negative
real eigenvalues accumulating at ǫ = −1.
The associated set of modes can be used to
rigorously expand, for example in the electromagnetic context, the near ﬁeld induced by
arbitrary external forcing and for an arbitrary — complex valued and frequency dependent
— inclusion permittivity [7, 8]. In particular, for metallic inclusions in the visible regime, the
real part of the inclusion permittivity is negative while the imaginary part, which accounts
for ohmic losses, is often relatively small; at frequencies where the inclusion permittivity is
near to one of the eigenvalues, the surface-plasmon mode which correspond to it may be
resonantly excited, depending on the level of losses and overlap between the external forcing
and that mode. The subwavelength nature of the surface-plasmon modes is also crucial in
this context, as radiation losses are negligible in this regime [1].
It is usually the lowest-order plasmonic modes that are resonantly excited; for example,
only the three “dipolar” modes of a subwavelength sphere, with eigenvalue ǫ = −2, are
excited by an incident plane wave [1]. In the other extreme, there are the high-mode-number
modes with eigenvalues near the accumulation point of the spectrum. As the accumulation
value is approached the eigenfunctions oscillate along the boundary, and decay away from it,
on shorter and shorter length scales. Such high-mode-number (or large-wavenumber) modes
can only be excited by external sources in the near ﬁeld, close to the inclusion boundary;
for realistically lossy inclusions, they are typically not manifested as isolated resonances,
given the high density of states, but rather contribute collectively. Theoretically, they are
known to play a dominant role in some of the most fascinating eﬀects discussed in relation
to plasmonics, such as perfect lensing [37–39], anomalous localized resonance [40] and Van
der Waals interactions [41, 42].
In three dimensions, the convergence of the eigenvalues to the accumulation value is
usually algebraic; e.g., for a sphere geometry the unique eigenvalues are exactly
ǫ = −1 −1
n,
(4)
where n ∈N. Recently, Miyanishi [36] proved a Weyl’s law for arbitrarily shaped smooth in-
clusions in three dimensions, providing the unsigned leading-order asymptotics of the ordered
eigenvalues counting multiplicities in terms of two global geometric properties: the Euler
characteristic and Willmore energy.
This remarkable mathematical result unfortunately
3


## Page 4


does not provide any connection between the asymptotic eigenvalues and their correspond-
ing eigenfunctions, nor asymptotic approximations for those eigenfunctions. Furthermore,
this leading order result it is not accurate enough to distinguish between adjacent eigen-
values, nor does it provide the asymptotics for the set of unique eigenvalues without prior
knowledge of the degeneracy (e.g., to compare with (4) it is necessary to know that for
spheres the nth unique eigenvalue is 2n + 1 degenerate). In the plasmonics context, asymp-
totic solutions of the eigenvalue problem for high mode numbers could potentially be used
to study the optical excitation of a nano-metallic particle in scenarios where the collective
response of the high-order modes dominates [39, 40, 43]. To this end, it is necessary to ﬁnd
at least leading-order asymptotic approximations for the eigenfunctions, as well as accurate
eigenvalue asymptotics, up to an order depending on the smallness of the imaginary part of
the inclusion permittivity.
In this paper, we put forward a novel approach for ﬁnding asymptotic solutions of the
plasmonic eigenvalue problem in the high-mode-number limit. Our approach is based on
the observation that high-order modes are strongly conﬁned to the boundary and oscil-
late rapidly along it; they are locally tantamount to surface plasmons of a ﬂat interface.
We propose that singular perturbation techniques [44], namely matched asymptotics and
WKBJ-type expansions, could be used to develop a surface-plasmon-ray description for the
eigenfunctions of smooth, arbitrarily shaped, inclusions, together with quantization rules
governing the corresponding eigenvalues. Our approach is inspired by the geometric theory
of diﬀraction [45] and its application to ﬁnding asymptotic solutions to eigenvalue problems
[46, 47]. To demonstrate this approach, we focus herein on one family of shapes, smooth
axisymmetric inclusions, that is general yet relatively easily addressed. For simplicity, we
assume that the thickness is a single-valued function of the axial co-ordinate, that the tips
are locally spheroidal; furthermore, among all the large-wavenumber modes we focus on
those that vary moderately in the azimuthal direction.
We were led to this work after
studying the exact eigenfunctions of spheres and realizing their relation to surface plasmons
of a ﬂat interface. We accordingly ﬁnd it useful to preface our asymptotic analysis with a
brief discussion of this linkage.
Flat surfaces and spheres.
Consider ﬁrst an inﬁnite plane interface, say y = 0,
separating two homogeneous half spaces. Looking for surface-wave solutions of (1)–(3) in
the form ϕ = ψ(y) exp(iβx), we ﬁnd ǫ ≡−1 with eigenfunctions ψ(y) ∝exp(−β|y|) (see
4


## Page 5


2π/β
ǫ = −1
x
∝e−β|y|+iβx
y
ǫ = −1 −1/n
2π/n
O(1/n)
ϑ
1
FIG. 1. (a) Surface plasmons at a ﬂat interface. (b) A high-mode number (or large-wavenumber)
axisymmetric localized surface plasmon mode of a sphere.
ﬁgure 1(a)); here β is a real wavenumber and (x, y) are Cartesian co-ordinates along and
normal to the interface, respectively. Physically, these solutions represent surface plasmons,
i.e., quasi-static collective oscillations of surface-polarization charge and electric ﬁeld; surface
plasmons are the limiting case of electromagnetic surface waves (surface plasmon polaritons)
as the plasmon wavelength, 2π/β, becomes small compared to the wavelength of light in the
bulk media [1]. Turning to the case of smooth inclusions, it becomes clear that modes that
oscillate rapidly along the boundary of the particle (and hence are strongly conﬁned to it)
must correspond to eigenvalues near the accumulation value, since on the small scale of the
oscillations the smooth surface is approximately ﬂat.
With the above surface-plasmon solutions in mind, let us now inspect the modes of a
sphere, which are known in closed form [7]. The exact expression (4) immediately reveals
the high-mode-number asymptotics of the eigenvalues. To describe the eigenfunctions, we
scale the sphere radius to unity and introduce spherical co-ordinates (r, ϑ, φ), where for
each n there are modes having azimuthal dependence exp(imφ), where m = −n, . . . , n. In
the axisymmetric case, m = 0, the eigenfunctions are ϕ = r−(n+1)Pn(cos ϑ) for r > 1 and
rnPn(cos ϑ) for r < 1, where Pn are the Legendre polynomials. In the high-mode number
limit, the boundary localization transitions from being algebraic to exponential:
ϕ ∼e−n|r−1|Pn(cos ϑ)
as
n →∞.
(5)
The dependence of the axisymmetric eigenfunctions on the polar angle ϑ is more subtle. In
5


## Page 6


the “outer” limit, namely with ϑ ﬁxed,
Pn(cos ϑ) ∼

2
πn sin ϑ
1/2
cos [(n + 1/2)ϑ −π/4]
as
n →∞.
(6)
As expected, the mode is locally a surface plasmon of a ﬂat interface, with a constant
wavenumber β ≈n; note the slow amplitude variation on the scale of the radius, as well
as the comparably slow phase accumulation, corresponding to an O(1) correction to the
wavenumber. Clearly, the outer approximation (6) diverges at the two poles; there is an
“inner region” near to the pole at ϑ = 0,
ϑ = O(1/n) :
Pn(cos ϑ) ∼J0(nϑ)
as
n →∞,
(7)
with a similar expansion holding near ϑ = π (see ﬁgure 1(b)). Note the relative enhancement
of the eigenfunctions at the poles.
II.
SMOOTH AXISYMMETRIC INCLUSIONS
A.
Geometry
Consider a smooth axisymmetric inclusion of length 2a; for simplicity, we assume that
the inclusion’s thickness is a single-valued function of the axial co-ordinate and that the tips
are locally spheroidal. In light of the scale invariance of the plasmonic eigenvalue problem,
it is natural to adopt a dimensionless convention where lengths are normalised by a. Using
cylindrical co-ordinates (ρ, φ, z), the inclusion boundary can be deﬁned as
ρ = f(z),
−1 ≤z ≤1,
(8)
where f(z) is a smooth thickness proﬁle that is positive for −1 < z < 1 and vanishes at the
tips z = ±1; the assumption that the tips are locally spheroidal implies
f 2 ∼2
κl
(z + 1)
as
z →−1;
f 2 ∼2
κr
(1 −z)
as
z →1,
(9)
where κl, κr > 0 are shape constants encapsulated in f(z). Figure 2 shows a dimensionless
schematic of the geometry.
6


## Page 7


−1
1
z
s
ν
ζ(s)
1/κ(s)
x(s, ν, φ)
ρ
̺(s) = f(ζ)
symmetry 
axis
FIG. 2. Dimensionless schematic of the axisymmetric geometry.
B.
Symmetry and boundary-ﬁtted co-ordinates
Since the eigen-potentials ϕ are deﬁned up to an arbitrary multiplicative factor, we may
consider them to be dimensionless. As discussed in the introduction, the plasmonic eigen-
value problem consists of Laplace’s equation (1), the transmission conditions (2), as well
as attenuation at large distances. For axisymmetric inclusions, symmetry implies that the
eigen-potentials can be sought in the form
ϕ = ψeimφ,
m ∈Z,
(10)
where ψ is independent upon the azimuthal angle φ. It will be convenient to use orthogonal
boundary-ﬁtted coordinates (s, ν, φ), which can be deﬁned in some ﬁnite neighbourhood of
the boundary. On the boundary, the normal coordinate ν vanishes and s coincides with the
arc length measured along a meridian arc starting from z = −1; we take ν to be positive in
the domain external to the particle. As shown in ﬁgure 2, we denote ρ = ̺(s) and z = ζ(s)
on ν = 0, and let κ(s) be the signed curvature of a meridian arc, positive when the center
of curvature is inside the inclusion. We show in the appendix that, in a neighbourhood of
the boundary where the boundary-ﬁtted co-ordinates are deﬁned, Laplace’s equation (1) is
∂
∂s
 
̺ + ν
p
1 −̺′2
1 + κν
∂ψ
∂s
!
+ ∂
∂ν

̺ + ν
p
1 −̺′2

(1 + κν)∂ψ
∂ν

−
m2(1 + κν)
̺ + ν
p
1 −̺′2ψ = 0,
(11)
7


## Page 8


where ̺′ = d̺/ds and ψ is considered as a function of s and ν. The interfacial conditions
(2) are likewise re-written as
ψ(i) = ψ(o),
ǫ∂ψ(i)
∂ν
= ∂ψ(o)
∂ν
at
ν = 0.
(12)
C.
Large wavenumber limit
Our interest here is in surface-plasmon modes with eigenvalues close to the accumulation
point ǫ = −1. We accordingly deﬁne the eigenvalue deviation τ through
ǫ = −1 −τ,
(13)
and consider the plasmonic eigenvalue problem in the limit
τ →0,
(14)
with m and f(z) ﬁxed. As already discussed in the introduction, in this regime we anticipate
modes that oscillate rapidly along the surface, which is why we shall also refer to (14) as
the large wavenumber limit. Our assumption m = O(1) limits the present study to modes
that vary only moderately in the azimuthal direction.
III.
SURFACE PLASMON RAYS
A.
Boundary layer and WKBJ ansatz
We know, from the structure of Laplace’s equation, that the potential must attenuate
rapidly away from the interface on a scale which is comparable to the wavelength of the
rapid oscillations along the surface. It is not a priori evident, however, how that short
length scale, say δ > 0, relates to τ except that δ(τ) →0 as τ →0; the sign of τ is also not
obvious. While the solution for a sphere suggests δ = O(τ) and τ > 0, there are examples of
geometries where τ < 0 (e.g., even modes for cylinder and sphere dimers) and δ ≫τ (e.g.,
ellipses). We shall here determine the short scale δ(τ), along with the sign of τ, as part of
the analysis.
To consider the boundary-layer about the particle surface, we write
ψ(s, ν) = Ψ(s, N),
N = n/δ(τ),
(15)
8


## Page 9


and consider the limit τ →0 with N, rather than ν, ﬁxed. Laplace’s equation (11) becomes,
for N ̸= 0,
δ2 ∂
∂s
 
̺ + δN
p
1 −̺′2
1 + δκN
∂Ψ
∂s
!
+ ∂
∂N

̺ + δN
p
1 −̺′2

(1 + δκN) ∂Ψ
∂N

−δ2m2(1 + δκN)
̺ + δN
p
1 −̺′2Ψ = 0
(16)
and the interfacial conditions (12) become
Ψ(i) = Ψ(o)
,
∂Ψ(o)
∂N
+ ∂Ψ(i)
∂N + τ ∂Ψ(i)
∂N
= 0
at
N = 0.
(17)
Conditions in the limits N →±∞are subject to asymptotic matching with a particle-scale
outer region, corresponding to the limit τ →0 with ν ﬁxed.
As prompted, the rapid variation in the normal direction must be accompanied by com-
parably rapid variations along the interface. This, along with the form of (16) suggests
looking for boundary-layer solutions in the form of a WKBJ ansatz
Ψ = A(s, N; τ) exp

± i
δ
Z s
k(t) dt

,
(18)
where A(s, N; τ) is a complex function and k(s) a scaled wavenumber, which without loss
of generality is assumed to be positive real. Substituting (18) into (16), we ﬁnd
∂
∂N

̺ + δN
p
1 −̺′2

(1 + δκN) ∂A
∂N

−
k2 
̺ + δN
p
1 −̺′2

1 + δκN
A
± iτ
k

̺ + δN
p
1 −̺′2

1 + δκN
∂A
∂s ± iδ ∂
∂s
 
̺ + δN
p
1 −̺′2
1 + δκN
kA
!
+ δ2 ∂
∂s
 
̺ + δN
p
1 −̺′2
1 + δκN
∂A
∂s
!
−δ2m2(1 + δκN)
̺ + δN
p
1 −̺′2A = 0,
(19)
whereas (17) give the conditions
A(i) = A(o),
∂A(o)
∂N
+ ∂A(i)
∂N + τ ∂A(i)
∂N
= 0
at
N = 0.
(20)
B.
Slowly varying surface plasmons
Without loss of generality, let the potential in the the boundary layer be O(1). The form
of the governing equations (19)–(20) then suggests the asymptotic expansion
A ∼A0 + δA1 + δ2A2 + · · · ,
(21)
9


## Page 10


where at leading O(1) Laplace’s equation (19) gives
∂2A0
∂N2 −k2A0 = 0
(22)
and the interfacial conditions (20) give
A(i)
0 = A(o)
0 ,
∂A(i)
0
∂N + ∂A(o)
0
∂N
= 0
at
N = 0.
(23)
We see from (22)–(23) that A0 either grows or attenuates exponentially as |N| →∞.
Exponential growth contradicts our picture of highly conﬁned surface modes (and clearly
leads to a contradiction when matched to the outer region, where the potential satisﬁes an
attenuation condition at large distances from the particle and must remain ﬁnite within
it). We conclude that A0 attenuates exponentially and hence that the outer potential is
exponentially small in δ. This implies, in turn, that the boundary-layer ﬁeld attenuates at
all algebraic orders:
Al →0
as
|N| →∞,
l = 0, 1, 2, . . .
(24)
Note that the leading-order problem (22)–(24) is homogeneous; nevertheless, for s ﬁxed,
it possesses a two-parameter family of non-trivial solutions in the form
A0(s, N) = a(s)e−k(s)|N|,
(25)
where a(s) is a complex amplitude. Substituting (25) into ansatz (18) shows that the leading-
order solution locally resembles a surface plasmon at a ﬂat interface; in fact, the existence of
non-trivial solutions to (22)–(24) is a consequence of our choice to perturb the permittivity
away from −1. We next extend the analysis to higher orders in order to determine the slow
variation of the wavenumber k(s) and complex amplitude a(s), along with the scaling of δ
and the sign of τ.
C.
The short scale δ(τ) and the sign of τ
At O(δ), Laplace’s equation (19) gives
∂2A1
∂N2 −k2A1 = −1
̺F1{A0},
(26)
10


## Page 11


where we deﬁne
F1{A0} =
∂
∂N
p
1 −̺′2 + ̺κ

N ∂A0
∂N

−Nk2 p
1 −̺′2 −̺κ

A0
± ik̺∂A0
∂s ± i ∂
∂s (̺kA0) .
(27)
The form of the interfacial conditions (20) at this order depends on the scaling of δ(s) and
the sign of τ. Let’s assume, at ﬁrst, that δ ≪τ. Then conditions (20) give
A(i)
1 = A(o)
1 ,
∂A(i)
0
∂N
?= 0
at
N = 0,
(28)
which with (25) is a contradiction. If, conversely, we assume that δ ≫τ, then
A(i)
1 = A(o)
1 ,
∂A(o)
1
∂N
+ ∂A(i)
1
∂N
?= 0
at
N = 0.
(29)
In this case we ﬁnd an O(δ) problem, consisting of (26), (29) and the decay condition (24),
that is a forced variant of the homogeneous O(1) one. We can therefore only expect solutions
to exist under certain “solvability conditions” on the forcing terms appearing on the right
hand side of (26). By deriving these conditions it can be shown that for ﬁnite ̺ and a ̸= 0
the problem for A1 does not posses any solutions.
We therefore deduce that δ(τ) = O(τ) and without loss of generality set δ = |τ|. The
transmission conditions (20) give
∂A(o)
1
∂N
+ ∂A(i)
1
∂N
= −sgn(τ)∂A(i)
0
∂N
at
N = 0
(30)
and we are left to consider the cases of positive and negative τ. The O(δ) problem is now
forced by the right hand sides of both (26) and (30); for τ < 0, it can be shown that solutions
exist only for negative k(s), which is again a contradiction. We therefore proceed with
δ = τ > 0.
(31)
D.
Relation between wavenumber and local geometry
With (31), the solvability condition for the problem consisting of (24), (26) and (30) can
be shown to be
k(s) =
p
1 −̺′2(s)
̺(s)
,
(32)
11


## Page 12


which gives the wavenumber, scaled by the permittivity deviation τ, as a function of the local
thickness of the inclusion. Interestingly, in the case of a sphere, ̺(s) = sin s, whereby (32)
yields k(s) ≡1; thus a sphere is a special geometry for which the wavenumber is uniform.
The complex amplitude a(s) remains undetermined and so we shall continue to the next
order. For this, we require A1. Given the complexity of the expressions, we solve (26) and
apply the transmission conditions (30) and attenuation (24) using Mathematica [48]. This
yields the solvability condition (32) — which can also be derived directly from the governing
equations — along with A1, in which a(s) appears as well as one extra unknown function,
say b(s), that does not feature in the subsequent analysis.
E.
Slow variation of amplitude and phase
At O(τ 2), Laplace’s equation (19) gives
∂2A2
∂N2 −k2A2 = −1
̺F1{A1} −1
̺F2{A0},
(33)
where we deﬁne
F2{A0} =
∂
∂N

κN2p
1 −̺′2∂A0
∂N

−k2 
̺κ2N2 −κ
p
1 −̺′2N2
A0
± ik
p
1 −̺′2N −̺κN
 ∂A0
∂s ± i ∂
∂s
hp
1 −̺′2 −̺κ

NkA0
i
+ ∂
∂s

̺∂A0
∂s

−m2
̺ A0;
(34)
the transmission conditions (20) give
A(i)
2 = A(o)
2 ,
∂A(o)
2
∂N
+ ∂A(i)
2
∂N
= −∂A(i)
1
∂N
at
N = 0;
(35)
and A2 also satisﬁes the attenuation condition (24). Just as in the previous order, we ﬁnd
a forced variant of the homogeneous O(1) problem. The solvability condition at this order
is found to be
± 2ida
ds + 1 −̺′2 ± i̺′p
1 −̺′2
̺
p
1 −̺′2
a = 0,
(36)
a diﬀerential equation governing a(s). Noting that a(s) is complex, we write
a = |a| exp(iγ),
(37)
12


## Page 13


where we later refer to γ as the slow phase. By splitting (36) into real and imaginary parts
we obtain diﬀerential equations where the amplitude and slow phase appear separately,
d
ds
 ̺|a|2
= 0,
dγ
ds = ±1
2k,
(38)
the rate of accumulation of the slow phase being simply proportional to that of the fast phase.
Integration of (38), followed by substitution into (25), (21) and (18), yields leading-order
solutions in the form
ψ ∼const. ×
1
p
̺(s)
exp

±i
1
τ + 1
2
 Z s
k(t) dt −k(s)|ν|/τ

,
(39)
where k(s) is provided by (32).
IV.
EIGENVALUE QUANTIZATION
A.
General boundary-layer solution
To generate a general boundary-layer approximation we superimpose the two leading-
order solutions in (39):
ψ ∼
X
±
c±
p
̺(s)
exp

±i
1
τ + 1
2

θ(s) −k(s)|ν|/τ

.
(40)
Here c± are complex constants and we deﬁne the phase factor
θ(s) =
Z s
0
k(t) dt.
(41)
The wavenumber k(s), provided in (32) in terms of ̺(s), can also be expressed in terms of
the shape function f(z):
k(s) =
1
f(ζ)
p
1 + f ′(ζ)2.
(42)
Since [cf. (9)]
k = κl + o(1)
as
z →−1,
k = κr + o(1)
as
z →1,
(43)
and since f > 0 for |z| < 1, θ(s) is well deﬁned by (44) and is a monotonically increasing
function of s; using (A1) we can write θ(s) as
θ(s) =
Z ζ(s)
−1
dz
f(z).
(44)
13


## Page 14


We shall later ﬁnd the geometric parameter
Θ =
Z 1
−1
dz
f(z)
(45)
to play an important role in the selection of discrete eigenvalues; note that Θ equals the
product of the inclusion length and the reciprocal average of its cross-sectional radius along
its symmetry axis.
We interpret the leading-order boundary-layer solution (40) as being formed of left- and
right-going surface-plasmon rays that traverse the meridian arcs (note that, since m = O(1),
the azimuthal wavenumber is small relative to the longitudinal one). At this stage, the
coeﬃcients c± and the eigenvalue deviation τ remain undetermined. Clearly (40) is singular
at the poles, where ̺ = 0. At these singularities, the surface plasmon rays focus and the
boundary-layer scaling (15) and the WKBJ ansatz (18) break down. We next show that
(40) can be matched with inner regions near to the poles, and that this quantizes τ and
determines the coeﬃcients c± (up to a common multiplicative constant).
B.
Matching with pole regions
Consider ﬁrst the inner region at O(τ) distances from the pole at z = −1. Noting that
̺ ∼s as s →0, for s = O(τ) the boundary-layer solution (40) becomes O(τ −1/2) large. We
accordingly expand the potential as
ψ(s, ν; τ) ∼τ −1/2Ψl(S, N)
(46)
and consider the inner limit where the stretched co-ordinates S = s/τ and N are ﬁxed. The
leading inner potential Ψl satisﬁes Laplace’s equation [cf. (11)]
1
S
∂
∂S

S ∂Ψl
∂S

+ ∂2Ψl
∂N2 −m2
S2 Ψl = 0,
N ̸= 0;
(47)
along with the transmission conditions [cf. (2)]
Ψ(o)
l
= Ψ(i)
l ,
∂Ψ(o)
l
∂N
+ ∂Ψ(i)
l
∂N
= 0
at
N = 0,
(48)
which do not involve the eigenvalue deviation τ; the attenuation conditions
Ψl →0
as
|N| →∞
(49)
14


## Page 15


as well as the condition of asymptotic matching with the boundary-layer solutions in the
limit S →∞.
Regarding the latter, we note that the inner limit of the leading O(1)
boundary-layer solution (40),
∼(τS)−1/2e−κl|N| X
±
c±e±iκlS,
(50)
should match with the corresponding boundary-layer limit of the inner expansion.
Separable solutions that satisfy (47)–(49) and are regular at S = 0 are proportional to
Jm(βS) exp(−β|N|), where β is an arbitrary separation constant. Since
Jm(κlS) ∼
1
√2πκlS
X
±
e±i(κlS−αm)
as
S →∞,
(51)
where
αm = mπ
2
+ π
4 ,
(52)
the need to match with (50) implies that the requisite inner solution is simply
Ψl(S, N) = clJm(κlS)e−κl|N|,
(53)
where the pre-factor cl is linked to the boundary-layer coeﬃcients through
c± = cl
e∓iαm
√2πκl
.
(54)
The above relations determine the boundary-layer solution in terms of a single multiplicative
constant, say cl (and the eigenvalue deviation τ).
We next consider the pole region near z = 1.
The relevant inner limit is with ˜S =
(sz=1 −s)/τ and N ﬁxed. The problem formulation is similar to the ﬁrst inner region and
hence
ψ ∼τ −1/2Ψr( ˜S, N),
Ψr( ˜S, N) = crJm(κr ˜S) exp(−κr|N|),
(55)
where cr is an unknown pre-factor. Similar to before, the inner limit of the boundary-layer
solution (40),
∼(τ ˜S)−1/2e−κr|N| X
±
c±e±i( 1
τ + 1
2)Θ∓iκr ˜S,
(56)
where we used θ(s) ∼Θ −κr(sz=1 −s) as z →1, should match with the boundary-layer
limit of (55), obtained using (51) with κlS replaced by κr ˜S. This matching condition links
cr to the boundary-layer coeﬃcients:
cre±iαm
√2πκr
= c±e±i( 1
τ + 1
2)Θ.
(57)
15


## Page 16


C.
Global solvability
At this stage we have determined the global form of the solution, which is composed of
the boundary-layer solution (40), characterized by the coeﬃcients c±, and the solutions in
the two inner pole regions, which are respectively characterized by coeﬃcients cl and cr.
These four coeﬃcients are related through the four matching conditions provided in (54)
and (57), which can be combined to give the matrix equation







√2πκl
0
−e−iαm
0
0
√2πκl
−eiαm
0
√2πκreiΘ( 1
τ + 1
2)
0
0
−eiαm
0
√2πκre−iΘ( 1
τ + 1
2)
0
−e−iαm














c+
c−
cl
cr







=







0
0
0
0







.
(58)
For a non-trivial solution the determinant of the matrix must vanish, which yields the
solvability condition [cf. (52)]
sin
π
2 −Θ
1
τ + 1
2

+ mπ

= 0.
(59)
This condition, in turn, implies the asymptotic quantization rule
1
τ ∼πn
Θ + 1
2
 π
Θ −1

+ o(1)
for
1 ≪n ∈N.
(60)
For each asymptotic eigenvalue, solving (58) yields a leading-order approximation for the
corresponding eigen-potentials.
V.
EXAMPLES: SPHERES, SPHEROIDS AND ASYMMETRIC SHAPES
It is illuminating to apply our asymptotic theory to the case of a sphere, for which
the eigenvalues and eigenfunctions are known in closed form. The thickness proﬁle for a
sphere is f(z) =
√
1 −z2, whereby the integral (45) gives Θ = π. The leading term in
the quantization rule (60) thus returns the exact eigenvalues (4), with the correction term
accordingly vanishing. The corresponding mode for given m and n is determined by solving
(58); let cl = 1, then cr = (−1)m+n and c± = (2π)−1/2e∓iαm. The corresponding boundary-
layer solution (40) and pole solutions (53) and (55) together constitute a leading-order
approximation for the eigenfunctions of a sphere, which generalize the asymptotic structure
discussed in the introduction, from m = 0 to arbitrary m = O(1).
16


## Page 17


h = 0.7
h = 0.25
n
n ≫1
m = 0
m = 1
m = 2
n ≫1
m = 0
m = 1
1
2.818
3.096
1.646
1.227
-7
12.261
1.163
2
1.8
1.885
1.558
1.295
9
5.718
1.281
3
1.513
1.541
1.437
1.294
3.667
3.745
1.365
4
1.377
1.389
1.347
1.269
2.6
2.843
1.415
5
1.299
1.304
1.284
1.238
2.143
2.344
1.437
6
1.247
1.250
1.239
1.211
1.889
2.036
1.439
7
1.211
1.212
1.205
1.187
1.727
1.833
1.428
8
1.183
1.185
1.180
1.168
1.615
1.691
1.410
9
1.163
1.163
1.160
1.151
1.533
1.588
1.390
10
1.146
1.146
1.144
1.138
1.471
1.510
1.367
11
1.132
1.133
1.131
1.126
1.421
1.450
1.344
12
1.121
1.121
1.120
1.116
1.381
1.403
1.324
13
1.112
1.112
1.111
1.108
1.348
1.365
1.304
14
1.104
1.104
1.103
1.101
1.32
1.333
1.286
15
1.097
1.097
1.096
1.094
1.296
1.306
1.269
16
1.091
1.091
1.090
1.088
1.276
1.284
1.254
17
1.085
1.085
1.085
1.083
1.258
1.265
1.240
18
1.080
1.080
1.080
1.079
1.242
1.248
1.228
19
1.076
1.076
1.076
1.075
1.229
1.233
1.216
20
1.072
1.072
1.072
1.071
1.216
1.220
1.206
21
1.069
1.069
1.069
1.068
1.205
1.208
1.196
22
1.066
1.066
1.065
1.065
1.195
1.198
1.188
23
1.063
1.063
1.063
1.062
1.186
1.188
1.180
TABLE I. Eigenvalues −ǫ for a prolate spheroid of thickness to length ratio h. The asymptotic
values for n ≫1, provided by (60) with Θ = π/h, are compared with exact values for m = 0, 1
and 2, for two values of h.
Consider next a prolate spheroid, in which case f(z) = h
√
1 −z2, where h is the ratio
of the minor and major axes. From (45) we ﬁnd Θ = π/h, with the asymptotic eigenvalues
and eigenfunctions following from (60) and (58) similarly to before; note that in this case
the second term in (60) does not vanish. In table I we compare the eigenvalues predicted by
17


## Page 18


(60) with the exact eigenvalues, which are known in terms of associated Legendre functions
of the ﬁrst and second kind (see, e.g., [7]). The rate of convergence of the exact values to the
asymptotic ones with increasing n is seen to be slower for smaller values of h. In fact, it is
evident from (60) that our asymptotic analysis fails in the slender-body limit h ≪1 as the
two terms in (60) become comparable; this non-commutativity of limits is to be expected,
given that the longitudinal modes of elongated particles tend to −∞, rather than −1, in the
slender-body limit. The convergence of the asymptotic values to the exact ones is also seen
to decelerate with increasing m, especially for small h. As m is increased and h is made
smaller, the surface-plasmon rays deviate from the meridian arcs and the modes gradually
approach the 2D modes of a circular cylinder, which all share the eigenvalue ǫ = −1. The
large |m| and slender-body limits are further discussed in §VI.
Of course, it is just as easy to apply the theory to other permissible shapes for which
the exact solution is unavailable. To give one example, for an asymmetric inclusion whose
thickness proﬁle is f(z) = h(p + z)
√
1 −z2, where p > 1, we ﬁnd from (45) that Θ =
(π/h)/
p
p2 −1.
VI.
CONCLUDING REMARKS
Plasmonic modes of smooth axisymmetric inclusions, with eigenvalues close to accumu-
lation and moderate azimuthal number m, can be interpreted as being composed of surface-
plasmon rays traversing the meridian arcs of the boundary. In this description, the modes
are conﬁned to a narrow boundary layer about the interface, where the eigen-potentials are
locally surface plasmons of a ﬂat interface. The wavenumber and amplitude slowly vary
along the rays, as a function of the local thickness of the inclusion; in addition to the fast
phase oscillations, there is also a slow phase accumulation associated with the geometry and
the azimuthal dependence. At the poles the boundary-layer ﬁelds diverge and are seen to
match with inner regions where the surface plasmons focus and are ampliﬁed. The WKBJ
analysis leading to the surface-plasmon ray description is somewhat unconventional in that
three (rather than two) consecutive orders need to be considered just to determine the
leading-order solution. This is because the local wavenumber is not known a priori, as in
traditional geometric optics, for example, but rather is governed by the geometry and must
be determined as part of the analysis.
18


## Page 19


By matching the right- and left-going surface-plasmon solutions in the boundary layer
with the two inner pole regions, the original eigenvalue problem is reduced to a matrix
equation governing a set of four scalar coeﬃcients. Solvability of the reduced problem yields
the two-term quantization rule (60) for the eigenvalue deviation. The leading order term
simply states that a whole number n of plasmon half-wavelengths ﬁt along the meridian arc
connecting the inclusion poles. In the special case of a sphere, the wavenumber is uniform
and equal to 1/τ, so that this condition reads n × (π/τ) = π, which remarkably yields the
exact eigenvalues (4). For more general shapes the wavenumber varies over the surface and
the eﬀective plasmon path is proportional to the geometric parameter Θ. The correction
term in (60), which is also given in terms of Θ, is due to the slow phase accumulation along
the rays and at the two poles. We note that in the physics literature a diﬀerent quantization
rule has been proposed, where the wavenumber is not determined by the local geometry
but rather from the dispersion relation of an electromagnetic surface wave (surface-plasmon
polariton) propagating along a ﬂat surface [49, 50]; that description is only relevant to
high-order modes of large inclusions, i.e., outside the quasi-static regime.
Curiously, the two leading terms in the quantization rule (60) are independent of the
azimuthal number m, even though the latter aﬀects the slow accumulation of phase both
along the rays and at the poles. In the case of a sphere, we know from the exact solution (4)
that this remains true to all asymptotic orders. The exact solution in the case of a spheroid
demonstrates, however, that this is not the case in general. While in the present paper the
asymptotic analysis was carried out with m ﬁxed, we expect that a similar approach could
be applied to study the large-|m| modes. In the latter case, the plasmon rays deviate from
the meridian arcs and, instead of focusing at the poles, they bounce back and forth between
circular caustics, deﬁned by the intersection of the boundary with certain constant-z planes.
We note that without knowledge of the large-|m| eigenvalue asymptotics it does not seem
possible to compare (the leading term of) the quantization rule (60) with the Weyl’s law
proved in [36].
The thickness proﬁle f(z) was also held ﬁxed in our asymptotic analysis. Accordingly, our
asymptotic approximations are not useful for rapidly varying, or very slender, shapes, unless
exceedingly high mode numbers are considered; examples of such inclusions include ﬁnite
cylinders truncated over a short scale, like the nano rods commonly used in plasmonic ap-
plications [51], and high-aspect-ratio needle-like inclusions, like the small-h prolate spheroid
19


## Page 20


discussed in §V. Singular perturbation techniques [44], especially slender-body theory, could
be used to ﬁnd asymptotic solutions in the latter limits, for both low-order and high-order
modes.
We focused in this paper on smooth axisymmetric shapes, for which the axial symmetry
allows decoupling the azimuthal dependence and the formation of ray singularities is fairly
evident. Whereas deriving the surface-plasmon-ray equations for an arbitrary 3D interface
would probably not be much more diﬃcult than the axisymmetric analysis in §III, inferring
the global structure of the solution for general shapes would be intractable in most cases.
For smooth planar inclusions in 2D, however, it is clear that there is just a single ray, that
traverses the boundary with no singularity forming. It can be shown that in that case the
boundary-layer analysis leaves the eigenvalues undetermined at all algebraic orders. Indeed,
for smooth planar inclusions the rate of convergence to the accumulation point is exponential
[35]. In the ray-theory picture, it seems necessary to account for the weak self-interaction
of the exponential tail of the surface-plasmon ray with the boundary. The techniques of
exponential asymptotics [52] may be useful in addressing the 2D high-mode-number limit.
We lastly note that with increasing mode number the plasmon wavelength ultimately
becomes commensurate with the scale of surface roughness or the scale at which local elec-
tromagnetic theory breaks down. In most plasmonic excitation problems, where only low-
order modes signiﬁcantly contribute to the optical response, these deviations from ideality
are immaterial. In scenarios where high-mode-number are important, however, it may be
important to account for roughness and nonlocal corrections. A generalized plasmonic eigen-
value problem that approximately accounts for nonlocality can be formulated based on the
hydrodynamic Drude model [26, 27]. A perturbation analysis of this problem in the limit
where the Fermi screening length is small compared to the inclusion size conﬁrms that, for
moderate mode numbers, the eﬀect of nonlocality is weak but becomes more pronounced as
the mode number increases [29]. It is clear that for high mode numbers, where the plasmon
wavelength is comparable with the screening length, nonlocality is no longer a perturbative
eﬀect and that the accumulation of eigenvalues predicted in the local case is ultimately reg-
ularized. It would therefore be interesting to analyze the nonlocal eigenvalue problem in the
double limit of high-mode number and small Fermi-screening length.
Acknowledgements.
The author acknowledges funding from EPSRC through New
Investigator Award EP/R041458/1.
20


## Page 21


Appendix A: Boundary-ﬁtted co-ordinates
Our goal here is to derive the form of Laplace’s equation in terms of the boundary-ﬁtted
co-ordinates (s, ν, φ) deﬁned in §II. Writing the arc length as
s =
Z ζ
−1
p
1 + f ′(t)2 dt
(A1)
and using f(ζ) = ̺(s), we ﬁnd
f ′(ζ) = d̺
ds
p
1 + f ′(ζ)2,
f ′(ζ)2 =
 1 −̺′(s)2−1 ̺′(s)2.
(A2)
We next parameterise the boundary as
xS(s, φ) = f(ζ)ˆeρ(φ) + ζˆez,
(A3)
where (ˆeρ,ˆez,ˆeφ) are the unit vectors associated with the cylindrical co-ordinates (ρ, z, φ).
We also write the normal unit vector, pointing into the background domain, as
ˆn(s, φ) = (ˆeρ(φ) −f ′(ζ)ˆez)
 1 + f ′(ζ)2−1/2 .
(A4)
In some ﬁnite neighbourhood of the boundary, the position of any point x = zˆez + rˆer(φ)
can be written as
x = xS(s, φ) + νˆn(s, φ),
(A5)
which gives the transformation between the cylindrical and boundary-ﬁtted co-ordinates. In
particular, our interest is in the scale factors
hs =

∂x
∂s
 ,
hν =

∂x
∂ν
 ,
hφ =

∂x
∂φ
 ,
(A6)
where x here is treated as a function of the boundary-ﬁtted co-ordinates. Substituting (A5)
into (A6) gives hν = 1 and
hs =

∂xS
∂s + ν ∂ˆn
∂s
 ,
hφ =

∂xS
∂φ + ν ∂ˆn
∂φ
 .
(A7)
Noting that
∂ˆn
∂s = κˆt,
(A8)
where ˆt = ∂xS/∂s is a tangent unit vector and κ(s) is the signed curvature of a meridian
arc such that κ(s) ≷0 wherever f ′′(ζ) ≶0, we ﬁnd
hs(s, ν) = 1 + κ(s)ν.
(A9)
21


## Page 22


To similarly simplify hφ we use (A3), (A4) and (A7) to ﬁnd
hφ(s, ν) =
̺(s)∂ˆeρ
∂φ + ν ∂ˆn
∂φ
 =
̺(s) + ν
 1 + f ′(ζ)2−1/2 ,
(A10)
which with (A2) reduces to
hφ(s, ν) = ̺(s) + ν
 1 −̺′(s)21/2
(A11)
for ν not too large. Using the above expressions for the scale factors, the Laplacian operator
can be written as
∇2ϕ =
1

̺ + ν
p
1 −̺′2

(1 + κν)
"
∂
∂s
 
̺ + ν
p
1 −̺′2
1 + κν
∂ϕ
∂s
!
+ ∂
∂ν

(̺ + ν
p
1 −̺′2)(1 + κν)∂ϕ
∂ν

+
1 + κν
̺ + ν
p
1 −̺′2
∂2ϕ
∂φ2
#
.
(A12)
[1] S. A. Maier. Plasmonics: fundamentals and applications. Springer Science & Business Media,
2007.
[2] J. A. Schuller, E. S. Barnard, W. Cai, Y. C. Jun, J. S. White, and M. L. Brongersma.
Plasmonics for extreme light concentration and manipulation.
Nat. Mater., 9(3):193–204,
2010.
[3] B. Luk’yanchuk, N. I. Zheludev, S. A. Maier, N. J. Halas, P. Nordlander, H. Giessen, and
C. T. Chong. The fano resonance in plasmonic nanostructures and metamaterials. Nat. Mat.,
9(9):707, 2010.
[4] F. Ouyang and M. Isaacson. Surface plasmon excitation of objects with arbitrary shape and
dielectric constant. Philos. Mag., 60(4):481–492, 1989.
[5] D. R. Fredkin and I. D. Mayergoyz.
Resonant behavior of dielectric objects (electrostatic
resonances). Phys. Rev. Lett., 91(25):253902, 2003.
[6] I. D. Mayergoyz, D. R. Fredkin, and Z. Zhang. Electrostatic (plasmon) resonances in nanopar-
ticles. Phys. Rev. B, 72(15):155412, 2005.
[7] V. V. Klimov. Nanoplasmonics. CRC Press, 2014.
[8] T. J. Davis and D. E. G´omez. Colloquium: An algebraic model of localized surface plasmons
and their interactions. Rev. Mod. Phys., 89(1):011003, 2017.
22


## Page 23


[9] D. J. Bergman.
Dielectric constant of a two-component granular composite: A practical
scheme for calculating the pole spectrum. Phys. Rev. B, 19(4):2359, 1979.
[10] D. Grieser. The plasmonic eigenvalue problem. Rev. Math. Phys., 26(03):1450005, 2014.
[11] K. Ando and H. Kang. Analysis of plasmon resonance on smooth domains using spectral
properties of the Neumann–Poincar´e operator. J. Math. Anal. Appl., 435(1):162–178, 2016.
[12] H. Ammari, P. Millien, M. Ruiz, and H. Zhang. Mathematical analysis of plasmonic nanopar-
ticles: the scalar case. Arch. Ration. Mech. Anal., 224(2):597–658, 2017.
[13] V. V. Klimov and D. V. Guzatov. Strongly localized plasmon oscillations in a cluster of two
metallic nanospheres and their inﬂuence on spontaneous emission of an atom. Phys. Rev. B,
75(2):024303, 2007.
[14] V. V. Lebedev, S. S. Vergeles, and P. E. Vorobev. Surface modes in metal–insulator composites
with strong interaction of metal particles. Appl. Phys. B, 111(4):577–588, 2013.
[15] J. B. Pendry, A. I. Fern´andez-Dom´ınguez, Y. Luo, and R. Zhao. Capturing photons with
transformation optics. Nature Phys., 9(8):518–522, 2013.
[16] S. Yu and H. Ammari. Plasmonic interaction between nanospheres. SIAM Rev., 60(2):356–385,
2018.
[17] O. Schnitzer. Singular perturbations approach to localized surface-plasmon resonance: Nearly
touching metal nanospheres. Phys. Rev. B, 92(23):235428, 2015.
[18] O. Schnitzer.
Asymptotic approximations for the plasmon resonances of nearly touching
spheres. arXiv preprint arXiv:1807.01636, 2018.
[19] E. Bonnetier, C. Dapogny, F. Triki, and H. Zhang. The plasmonic resonances of a bowtie
antenna. arXiv preprint arXiv:1803.02614, 2018.
[20] K. Perfekt and M. Putinar. Spectral bounds for the Neumann-Poincar´e operator on planar
domains with corners. J. Anal. Math., 124(1):39–57, 2014.
[21] E. Bonnetier and H. Zhang.
Characterization of the essential spectrum of the Neumann-
Poincar´e operator in 2d domains with corner via weyl sequences.
arXiv preprint
arXiv:1702.08127, 2017.
[22] D. J. Bergman and M. I. Stockman. Surface plasmon ampliﬁcation by stimulated emission
of radiation: quantum generation of coherent surface plasmons in nanosystems. Phys. Rev.
Lett., 90(2):027402, 2003.
23


## Page 24


[23] K. Li, M. I. Stockman, and D. J. Bergman.
Enhanced second harmonic generation in a
self-similar chain of metal nanospheres. Phys. Rev. B, 72(15):153401, 2005.
[24] D. Grieser, H. Uecker, S. Biehs, O. Huth, F. R¨uting, and M. Holthaus. Perturbation theory
for plasmonic eigenvalues. Phys. Rev. B, 80(24):245405, 2009.
[25] K. Ando, H. Kang, Y. Miyanishi, and E. Ushikoshi. The ﬁrst hadamard variation of Neumann-
Poincar´e eigenvalues on the sphere. arXiv preprint arXiv:1805.02414, 2018.
[26] Y. Luo, A. Fernandez-Dominguez, A. Wiener, S. A. Maier, and J. B. Pendry. Surface plasmons
and nonlocality: a simple model. Phys. Rev. Lett., 111(9):093901, 2013.
[27] S. Raza, S. I. Bozhevolnyi, M. Wubs, and N. A. Mortensen. Nonlocal optical response in
metallic nanostructures. J. Phys. Condens. Matter, 27(18):183204, 2015.
[28] O. Schnitzer, V. Giannini, R. V. Craster, and S. A. Maier. Asymptotics of surface-plasmon
redshift saturation at subnanometric separations. Phys. Rev. B, 93(4):041409, 2016.
[29] O. Schnitzer, V. Giannini, S. A. Maier, and R. V. Craster. Surface plasmon resonances of
arbitrarily shaped nanometallic structures in the small-screening-length limit. Proc. R. Soc.
A, 472(2191):20160258, 2016.
[30] D. J. Bergman and D. Stroud. Theory of resonances in the electromagnetic scattering by
macroscopic bodies. Phys. Rev. B, 22(8):3527, 1980.
[31] M. S. Agranovich, B. Z. Katsenelenbaum, A. N. Sivov, and N. N. Voitovich.
Generalized
method of eigenoscillations in diﬀraction theory. Wiley-VCH Pub, 1999.
[32] A. Farhi and D. J. Bergman. Non-quasi-static eigenstates of maxwell’s equations in a two-
constituent composite medium and their application to a calculation of the local electric ﬁeld
of an oscillating dipole. In Plasmonics: Metallic Nanostructures and Their Optical Properties
XIII, volume 9547, 2015.
[33] H. Ammari, M. Ruiz, S. Yu, and H. Zhang. Mathematical analysis of plasmonic resonances for
nanoparticles: the full maxwell equations. J. Diﬀerential Equations, 261(6):3615–3669, 2016.
[34] P. Y. Chen, D. J. Bergman, and Y. Sivan. Generalizing normal mode expansion of electro-
magnetic green’s tensor to lossy resonators in open systems. arXiv preprint arXiv:1711.00335,
2017.
[35] K. Ando, H. Kang, and Y. Miyanishi. Exponential decay estimates of the eigenvalues for
the Neumann-Poincar´e operator on analytic boundaries in two dimensions. arXiv preprint
arXiv:1606.01483, 2016.
24


## Page 25


[36] Y. Miyanishi. Weyl’s law for the eigenvalues of the Neumann–Poincar´e operators in three
dimensions: Willmore energy and surface geometry. arXiv preprint arXiv:1806.03657, 2018.
[37] J. B. Pendry. Negative refraction makes a perfect lens. Phys. Rev. Lett., 85(18):3966, 2000.
[38] I. A. Larkin and M. I. Stockman. Imperfect perfect lens. Nano Lett., 5(2):339–343, 2005.
[39] A. Farhi and D. J. Bergman. Analysis of a Veselago lens in the quasistatic regime. Phys. Rev.
A, 90(1):013806, 2014.
[40] G. W. Milton and N.-A. P. Nicorovici. On the cloaking eﬀects associated with anomalous
localized resonance. Proc. Royal Soc. Lond., 462(2074):3027–3059, 2006.
[41] V. V. Klimov and A. Lambrecht. Van der Waals forces between plasmonic nanoparticles.
Plasmonics, 4(1):31–36, 2009.
[42] Y. Luo, R. Zhao, and J. B. Pendry. van der Waals interactions at the nanoscale: The eﬀects
of nonlocality. Proc. Natl. Acad. Sci. U.S.A., 111(52):18422–18427, 2014.
[43] A. Farhi and D. J. Bergman. Eigenstate expansion of the quasistatic electric ﬁeld of a point
charge in a spherical inclusion structure. Phys. Rev. A, 96(4):043806, 2017.
[44] E. J. Hinch. Perturbation methods. Cambridge university press, 1991.
[45] J. B. Keller. Geometrical theory of diﬀraction. JOSA, 52(2):116–130, 1962.
[46] J. B. Keller. Corrected bohr-sommerfeld quantum conditions for nonseparable systems. Ann.
Phys., 4(2):180–188, 1958.
[47] J. B. Keller and S. I. Rubinow. Asymptotic solution of eigenvalue problems. Ann. Phys.,
9(1):24–75, 1960.
[48] Wolfram Research, Inc. Mathematica, Version 11.3. Champaign, IL, 2018.
[49] Y. Fang and X. Tian. Resonant surface plasmons of a metal nanosphere can be considered in
the way of propagating surface plasmons. arXiv preprint arXiv:1412.2664, 2014.
[50] W. Liu, R. F. Oulton, and Y. S. Kivshar. Geometric interpretations for resonances of plasmonic
nanoparticles. Sci. Rep., 5:12148, 2015.
[51] H. Chen, L. Shao, Q. Li, and J. Wang. Gold nanorods and their plasmonic properties. Chem.
Soc. Rev., 42(7):2679–2724, 2013.
[52] J.-M. Vanden-Broeck and S. J. Chapman. Exponential asymptotics and capillary waves. SIAM
J. Appl. Math., 62(6):1872–1898, 2002.
25

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
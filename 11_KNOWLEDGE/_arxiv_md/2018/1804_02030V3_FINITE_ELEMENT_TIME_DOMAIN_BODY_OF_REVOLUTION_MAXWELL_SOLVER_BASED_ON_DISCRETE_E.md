---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1804.02030v3
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1804.02030v3_Finite_Element_Time-Domain_Body-of-Revolution_Maxwell_Solver_based_on_Discrete_E

> Source: 1804.02030v3_Finite_Element_Time-Domain_Body-of-Revolution_Maxwell_Solver_based_on_Discrete_E.pdf

> Pages: 41

---


## Page 1


Finite Element Time-Domain Body-of-Revolution Maxwell
Solver based on Discrete Exterior Calculus
Dong-Yeop Naa, Ben-Hur V. Borgesb, Fernando L. Teixeiraa
aElectroScience Laboratory and department of Electrical and Computer Engineering, The Ohio State
University, Columbus, OH 43212, USA
bElectrical and Computer Engineering Department, University of S˜ao Paulo, S˜ao Carlos, SP
13560-970, Brazil
Abstract
We present a ﬁnite-element time-domain (FETD) Maxwell solver for the analysis of
body-of-revolution (BOR) geometries based on discrete exterior calculus (DEC) of dif-
ferential forms and transformation optics (TO) concepts. We explore TO principles to
map the original 3-D BOR problem to a 2-D one in the meridian ρz-plane based on a
Cartesian coordinate system where the cylindrical metric is fully embedded into the con-
stitutive properties of an eﬀective inhomogeneous and anisotropic medium that ﬁlls the
domain. The proposed solver uses a (TEφ, TMφ) ﬁeld decomposition and an appropriate
set of DEC-based basis functions on an irregular grid discretizing the meridian plane.
A symplectic time discretization based on a leap-frog scheme is applied to obtain the
full-discrete marching-on-time algorithm. We validate the algorithm by comparing the
numerical results against analytical solutions for resonant ﬁelds in cylindrical cavities
and against pseudo-analytical solutions for ﬁelds radiated by cylindrically symmetric an-
tennas in layered media. We also illustrate the application of the algorithm for a particle-
in-cell (PIC) simulation of beam-wave interactions inside a high-power backward-wave
oscillator.
Keywords:
body-of-revolution, ﬁnite-element time-domain, Maxwell equations,
discrete exterior calculus, transformation optics.
1. Introduction
The solution of Maxwell’s equations in circularly symmetric or body-of-revolution
(BOR) geometries is important for a plethora of applications involving analysis and
design of microwave devices (e.g. cavity resonators, coaxial cables, waveguides, antennas,
high-power ampliﬁers, etc.) [1, 2, 3, 4, 5, 6, 7, 8, 9], electromagnetic scattering [10, 11,
12, 13], metamaterials [14], and exploration geophysics [15, 16, 17, 18, 19, 20, 21], to
name a few. Azimuthal ﬁeld variations in BOR problems can be described by Fourier
Email addresses: na.94@osu.edu (Dong-Yeop Na), benhur@sc.usp.br (Ben-Hur V. Borges),
teixeira.5@osu.edu (Fernando L. Teixeira)
Preprint submitted to Elsevier
September 26, 2018
arXiv:1804.02030v3  [physics.comp-ph]  25 Sep 2018


## Page 2


modal decomposition, with the modal ﬁeld solutions reduced to a two-dimensional (2-
D) problem in the meridian ρz-plane. Frequency-domain ﬁnite element (FE) Maxwell
solvers for BOR problems have been developed in the past by discretizing the second-
order vector wave equation using edge elements for either the electric or the magnetic
ﬁeld [6, 7, 12, 14, 22] which avoids some of the pitfalls encountered when using scalar
elements [10].
It is highly desirable to develop BOR FE solvers in the time domain as well. Time-
domain FE solvers are better suited for simulating broadband problems, for capturing
transient processes such as those involved in beam-wave interactions [23, 24, 25], and for
handling non-linear problems. However, the use of the second-order vector wave equation
as a starting point for a time-domain FE formulation, as done in frequency-domain
Maxwell FE solvers, is inadequate. This is because the vector wave equation admits
solutions of the form t∇φ, which are not original solutions of Maxwell’s equations and,
even if not excited by (properly set) initial conditions, may emerge in the course of the
simulation due to round-oﬀerrors and pollute the results for long integration times [26].
To avoid this problem, a mixed (basis) FE solver based directly on the ﬁrst-order should
be adopted in the time domain [27, 28, 29, 30].
In this paper, we present a mixed FE BOR solver for time-domain Maxwell’s curl
equations based on transformation optics (TO) [31, 32, 33, 34, 35, 36] and discretization
principles based on the discrete exterior calculus (DEC) of diﬀerential forms [23, 27,
37, 38, 39, 40, 41, 42, 43, 44].
We explore TO principles to map the original three-
dimensional (3-D) BOR problem to an equivalent problem on the 2-D meridian plane
where the resulting metric is not the cylindrical one but instead the Cartesian one (i.e.,
with no radial factors present).
The cylindrical metric becomes fully embedded into
the constitutive properties of an eﬀective (artiﬁcial) inhomogeneous anisotropic medium
that ﬁlls the entire domain. In this way, a Cartesian 2-D FE code can be retroﬁtted
to this problem with no modiﬁcations necessary except to accommodate the presence of
anisotropic media. Similar ideas have been explored in the past but restricted to the
frequency-domain ﬁnite-diﬀerence (FD) context and to structured grids only [45]. In the
FE context considered here, DEC principles are used to discretize Maxwell’s equations
on unstructured (irregular) grids using discrete diﬀerential (Whitney) forms [33, 37, 40,
46, 47]. Unstructured grids permits a more ﬂexible representation of irregular geometries
and reduce the need for geometrical defeaturing. In addition to the above advantages,
the proposed formalism facilitates treatment of the coordinate singularity on the axis of
symmetry (z axis) because it does not require any modiﬁcation of the basis functions
for ρ = 0 (otherwise necessary in prior BOR FE solvers [6, 12, 22]). As detailed in the
Appendix, the DEC formalism also facilitates implementation of perfectly matched layers
(PML) to truncate the outer boundaries. We validate the algorithm against analytical
solutions for resonant ﬁelds in cylindrical cavities and against pseudo-analytical solutions
for the radiated ﬁelds by cylindrically symmetric antennas in layered media. We also
illustrate the application of the algorithm to the simulation of wave-beam interactions in
a high-power microwave backward-wave oscillator (BWO).
2


## Page 3


Figure 1: Depiction of an axisymmetric structure.
2. Formulation
2.1. Exploration of transformation optics (TO) concepts
Consider a BOR object with symmetry axis along z, such as the waveguide structure
depicted in Fig. 1. It is well known that the vector operators (gradient, curl, and di-
vergence) in cylindrical coordinates have additional metric scaling factors not present in
Cartesian coordinates. However, by exploiting TO concepts [31, 32, 38], we can map the
cylindrical-system Maxwell’s curl equations to a Cartesian-like equations where the met-
ric factors are embedded into artiﬁcial constitutive tensors. For convenience we denote
these calculations under the generic banner of TO but some of these ideas actually pre-
date TO per se. They can be traced to earlier applications involving Maxwell’s equations
in BOR geometries and to Weitzenbock identities involving diﬀerential forms of diﬀerent
degrees [48] in cylindrical (polar) coordinates.
Starting from Maxwell’s equations in cylindrical coordinates, and considering artiﬁcial
anisotropic permittivity and permeability tensors ¯¯ϵ′ and ¯¯µ′ of the form
¯¯ϵ′ = ¯¯ϵ · ¯¯Rϵ = ¯¯ϵ ·


ρ
0
0
0
ρ−1
0
0
0
ρ

,
(1)
¯¯µ′ = ¯¯µ · ¯¯Rµ = ¯¯µ ·


ρ−1
0
0
0
ρ
0
0
0
ρ−1

,
(2)
where the constitutive parameters of the original medium are given by
¯¯ϵ =


ϵρ
0
0
0
ϵφ
0
0
0
ϵz

,
¯¯µ =


µρ
0
0
0
µφ
0
0
0
µz

.
3


## Page 4


and using the following rescaling for the ﬁelds
E′ = ¯¯RE · E =


1
0
0
0
ρ
0
0
0
1

· E,
(3)
D′ = ¯¯RD · D =


ρ
0
0
0
1
0
0
0
ρ

· D,
(4)
B′ = ¯¯RB · B =


ρ
0
0
0
1
0
0
0
ρ

· B,
(5)
H′ = ¯¯RH · H =


1
0
0
0
ρ
0
0
0
1

· H,
(6)
we can rewrite the resulting Maxwell’s curl equations as
∇′ × E′ = −∂B′
∂t ,
(7)
∇′ × H′ = ∂D′
∂t ,
(8)
D′ = ¯¯ϵ′ · E′,
(9)
B′ = ¯¯µ′ · H′,
(10)
with
∇′ × A′ =

ˆρ
ˆφ
ˆz
∂
∂ρ
∂
∂φ
∂
∂z
A′
ρ
A′
φ
A′
z

.
(11)
The modiﬁed curl operator in the equivalent (primed) system seen in (11) is devoid of
any radial scaling and thus locally isomorphic to the Cartesian curl operator.
4


## Page 5


(a)
(b)
Figure 2: (2+1) setup for ﬁelds on (a) primal and (b) dual meshes at the meridian plane. The vertical
axis is ρ and the horizontal axis is z.
2.2. Field decomposition
We decompose the ﬁelds into two sets: TEφ- and TMφ-polarized ﬁelds, corresponding
to {E′ρ, E′z, B′φ} and {E′φ, B′ρ, B′z}, respectively. In what follows, we use superscripts
∥or ⊥to denote ﬁelds transverse or normal to the 2-D meridian plane. The TEφ ﬁeld
components can be expressed as E′∥and B′⊥and the TMφ as E′⊥and B′∥. In the DEC
context, the electric ﬁeld intensity, the magnetic ﬂux density, the electric ﬂux density,
and the magnetic ﬁeld intensity are likewise represented as 1-, 2-, 2-, and 1-forms1 on the
3-D Euclidean space, respectively [38]. For present analysis based on the meridian plane
(a 2-D manifold), E∥is transverse to the plane and still is represented as a 1-form. On
the other hand, E⊥should be represented as a 0-form since it is a point-based quantity
on this manifold. Likewise, although B⊥is a 2-form in 3-D, B∥is represented as a 1-form
on the 2-D meridian plane (see Fig. 2).
11- and 2-forms correspond to physical quantities naturally associated to line and surface integrals,
respectively.
5


## Page 6


2.3. Mixed FE time-domain BOR solver
We factor the transverse (i.e. ρ and z) and normal (i.e. φ) variations of the polarization-
decomposed Maxwell ﬁelds on the 2-D meridian plane as
E′ (ρ, φ, z, t) =
Mφ
X
m=−Mφ
E′∥
m (ρ, z, t) Φm (φ) +
Mφ
X
m=−Mφ
E′⊥
m (ρ, z, t) Ψm (φ) ,
(12)
B′ (ρ, φ, z, t) =
Mφ
X
m=−Mφ
B′⊥
m (ρ, z, t) Φm (φ) +
Mφ
X
m=−Mφ
B′∥
m (ρ, z, t) Ψm (φ) ,
(13)
where Mφ is the maximum order of the Fourier harmonics considered and
Φm (φ) =



cos (mφ) ,
for m < 0
1,
for m = 0
sin (mφ) ,
for m > 0
,
(14)
Ψm (φ) =



sin (mφ) ,
for m < 0
1,
for m = 0
cos (mφ) ,
for m > 0
.
(15)
Substituting (12) and (13) into (7), by using the orthogonality between modes, i.e.
Z 2π
0
Φm (φ) Φn (φ) dφ = Cmδmn,
(16)
Z 2π
0
Ψm (φ) Ψn (φ) dφ = Cmδmn,
(17)
where Cm = π for m ̸= 0 and C0 = 2π, we obtain the modal Faraday’s law as
∇′∥× E′∥
m (ρ, z, t) = −∂B′⊥
m (ρ, z, t)
∂t
,
(18)
∇′∥× E′⊥
m (ρ, z, t) = −∂B′∥
m (ρ, z, t)
∂t
+ |m| E′∥
m (ρ, z, t) × ˆφ,
(19)
for m = −Mφ, ..., Mφ, where ∇′∥= ˆρ∂/∂ρ + ˆz∂/∂z.
We discretize (18) and (19) on the meridian plane using an unstructured mesh based
on simplicial (triangular) cells and by expanding the ﬁelds in a mixed basis as scalar or
vector proxies of discrete diﬀerential forms (Whitney forms) [27, 38, 43]. In particular,
the TEφ ﬁeld is expanded as
E′∥
m (ρ, z, t) =
N1
X
j=1
E∥
j,m (t) W(1)
j
(ρ, z) ,
(20)
B′⊥
m (ρ, z, t) =
N2
X
k=1
B⊥
k,m (t) W(2)
k
(ρ, z) ,
(21)
where W(p)
q
is the vector proxy of a Whitney p-form w(p)
q
[24] associated with the q-th
p-cell (p = 0, 1, 2 for nodes, edges, and facets, respectively) on the grid, and Np is the
6


## Page 7


total number of p-cells on the grid. The expressions for the Whitney forms and their
proxies are provided in Appendix A. Likewise, the TMφ ﬁeld is represented as
E′⊥
m (ρ, z, t) =
N0
X
i=1
E⊥
i,m (t) ˆφ W(0)
i
(ρ, z) ,
(22)
B′∥
m (ρ, z, t)=
N1
X
j=1
B∥
j,m (t) W(RWG)
j
(ρ, z).
(23)
In what follows, we denote W(1)
j
× ˆφ = W(RWG)
j
, since this expression recovers the so-
called Rao-Wilton-Glisson (RWG) functions [49, 50] 2. Note that we use dummy index
subscripts i, j, and k to indicate the i-th node, j-th edge, and k-th face, respectively.
The various basis functions above are depicted in Fig. 3, see also [52, 53].
By substituting (20) and (21) into (18), and (22) and (23) into (19), we obtain the
following equations
N1
X
j=1
E∥
j,m (t)

∇′∥× W(1)
j

= −∂
∂t
N2
X
k=1
B⊥
k,m (t) W(2)
k
(24)
N0
X
i=1
E⊥
i,m (t) ∇′∥W(0)
i
= −∂
∂t
N1
X
j=1
B∥
j,m (t) W(1)
j
+ |m|
N1
X
j=1
E∥
j,m (t) W(1)
j ,
(25)
for m = −Mφ, ..., Mφ and where we have used the fact that ∇′∥×

ˆφW(0)
i

=

∇′∥W(0)
i

×
ˆφ. The equations above can be recast using the exterior calculus of diﬀerential forms as
N1
X
j=1
E∥
j,m (t)

d′∥w(1)
j

= −∂
∂t
N2
X
k=1
B⊥
k,m (t) w(2)
k ,
(26)
N0
X
i=1
E⊥
i,m (t)

d′∥w(0)
i

= −∂
∂t
N1
X
j=1
B∥
j,m (t) w(1)
j
+ |m|
N1
X
j=1
E∥
j,m (t) w(1)
j ,
(27)
where d′∥= dρ ∂/∂ρ + dz ∂/∂z is the exterior derivative on the meridian plane.
Applying DEC principles, (26) can be paired to the 2-cells of the mesh and (27) to
the 1-cells of the mesh (see Appendix B) so that, by invoking the generalized Stokes’
theorem [27, 38, 40, 43, 44] (see Appendix C), the exterior derivative can be replaced by
incidence operators on the mesh (see also Appendix D). Next, by discretizing the time
derivatives using central-diﬀerences in a staggered manner (leap-frog time discretization)
we obtain the following update equations for Faraday’s law

B⊥
m
n+ 1
2 =

B⊥
m
n−1
2 −∆t [Dcurl] ·
h
E∥
m
in
,
(28)
h
B∥
m
in+ 1
2 =
h
B∥
m
in−1
2 −∆t

[Dgrad] ·

E⊥
m
n −|m|
h
E∥
m
in
,
(29)
2In other words, W(RWG)
j
is the Hodge dual of W(1)
j
in 2-D [40, 43, 51].
7


## Page 8


(a)
(b)
(c)
(d)
Figure 3: Vector proxies of various degrees of Whitney forms on the mesh: (a) W(1)
j
, (b) W(2)
k , (c) W(0)
i
,
and (d) W(RWG)
j
. Note that tj is a unit vector tangential to j−th edge and parallel to its direction and
nk is a unit vector normal to k−th face.
where ∆t is a time step increment and the superscript n indicates the time-step index.
[Dcurl] and [Dgrad] are N2 ×N1 and N1 ×N0 incidence matrices, respectively, that encode
the curl and the gradient operators on the FE mesh with elements in the set {−1, 0, 1}
(see Appendix D). The ﬁeld unknowns are represented by the column vectors

B⊥
m

=

B⊥
m,1, ..., B⊥
m,N2
T ,
h
E∥
m
i
=
h
E∥
m,1, ..., E∥
m,N1
iT
,
h
B∥
m
i
=
h
B∥
m,1, ..., B∥
m,N1
iT
, and

E⊥
m

=

E⊥
m,1, ..., E⊥
m,N0
T .
We proceed along similar lines for Ampere’s law by expressing the D′ and H′ ﬁelds
as
D′ (ρ, φ, z, t) =
Mφ
X
m=0
D′∥
m (ρ, z, t) Φm (φ) +
Mφ
X
m=0
D′⊥
m (ρ, z, t) Ψm (φ) ,
(30)
H′ (ρ, φ, z, t) =
Mφ
X
m=0
H′⊥
m (ρ, z, t) Φm (φ) +
Mφ
X
m=0
H′∥
m (ρ, z, t) Ψm (φ) .
(31)
8


## Page 9


After substituting (30) and (31) to (8), applying trigonometric orthogonality to the
resulting equations, and matching the ﬁeld components, we arrive at
∇′∥× H′∥
m (ρ, z, t) = ∂D′⊥
m (ρ, z, t)
∂t
,
(32)
∇′∥× H′⊥
m (ρ, z, t)= ∂D′∥
m (ρ, z, t)
∂t
−|m| H′∥
m (ρ, z, t) × ˆφ.
(33)
As before, we discretize (32) and (33) on the 2-D meridian plane, the important diﬀerence
being that the discretization for D′ and H′ is on the dual mesh [33, 38, 43, 51], as opposed
to the FE (primal) mesh as done for E′ and B′. In this way, we obtain
D′∥
m (ρ, z, t) =
˜
N1
X
j=1
D∥
j,m (t) ˜
W(RWG)
j
(ρ, z) ,
(34)
H′⊥
m (ρ, z, t) =
˜
N0
X
i=1
H⊥
i,m (t) ˆφ ˜W
(0)
i
(ρ, z) ,
(35)
D′⊥
m (ρ, z, t) =
˜
N2
X
k=1
D⊥
k,m (t) ˜
W(2)
k
(ρ, z) ,
(36)
H′∥
m (ρ, z, t) =
˜
N1
X
j=1
H∥
j,m (t) ˜
W(1)
j
(ρ, z) .
(37)
where we use the tilde˜to denote quantities associated with the dual mesh. Similar to the
discrete counterparts of Faraday’s law, by substituting (34) and (35) into (32) and (36)
and (37) into (33) and by applying DEC principles and a leap-frog time discretization to
the resulting equations, we obtain the discrete representations of Ampere’s law as

D⊥
m
n+1 =

D⊥
m
n + ∆t
h
˜Dcurl
i
·
h
H∥
m
in+ 1
2 ,
(38)
h
D∥
m
in+1
=
h
D∥
m
in
+ ∆t
h
˜Dgrad
i
·

H⊥
m
n+ 1
2 −|m|
h
H∥
m
in+ 1
2 
,
(39)
where
h
˜Dcurl
i
and
h
˜Dgrad
i
are incidence matrices on the dual mesh, with sizes ˜N2 × ˜N1
and ˜N1 × ˜N0, respectively. As before,

H⊥
m

,
h
D∥
m
i
,
h
H∥
m
i
, and

D⊥
m

are column vectors
containing the degrees of freedom of the modal ﬁelds.
We use the (discrete) Hodge star operator
[33, 38, 43, 51] to convert the discrete
Ampere’s law from the dual mesh to the primal mesh. In this way,
[⋆ϵ]0→0 ·

E⊥
m
n+1 = [⋆ϵ]0→0 ·

E⊥
m
n
+ ∆t

[Dgrad]T ·

⋆µ−11→1 ·
h
B∥
m
in+ 1
2 
,
(40)
[⋆ϵ]1→1 ·
h
E∥
m
in+1
= [⋆ϵ]1→1 ·
h
E∥
m
in
+∆t

[Dcurl]T ·

⋆µ−12→2 ·

B⊥
m
n+ 1
2 −|m|

⋆µ−11→1 ·
h
B∥
m
in+ 1
2 
,
(41)
9


## Page 10


where
h
˜Dcurl
i
= [Dgrad]T ,
h
˜Dgrad
i
= [Dcurl]T and the discrete Hodge matrix elements
are given by [38, 43, 47]
[⋆ϵ]1→1
J,j
=
Z
Ω
(ϵ0ρ) w(1)
J
∧⋆

w(1)
j

=
Z
Ω
(ϵ0ρ) W(1)
J
· W(1)
j dV
|
{z
}
vector proxy representation
,
(42)

⋆µ−12→2
K,k =
Z
Ω
 µ−1
0 ρ

w(2)
K ∧⋆

w(2)
k

=
Z
Ω
 µ−1
0 ρ

W(2)
K · W(2)
k dV
|
{z
}
vector proxy rep.
,
(43)
[⋆ϵ]0→0
I,i
=
Z
Ω
 ϵ0ρ−1
w(0)
I
∧⋆

w(0)
i

=
Z
Ω
 ϵ0ρ−1 h
W(0)
I
ˆφ
i
·
h
W(0)
i
ˆφ
i
dV
|
{z
}
vector proxy rep.
,
(44)

⋆µ−11→1
J,j
=
Z
Ω
(µ0ρ)−1 w(RWG)
J
∧⋆

w(RWG)
j

=
Z
Ω
(µ0ρ)−1 h
W(1)
J
× ˆφ
i
·
h
W(1)
j
× ˆφ
i
dV
|
{z
}
vector proxy rep.
,
(45)
where Ωis the (compact) spatial support of the Whitney forms, and the ρ, ρ−1 factors
result from the use of the TO in the mapping, as discussed before, where they enter
as modiﬁers of constitutive properties rather than diﬀerential operator factors.
The
discrete Hodge matrices deﬁned in (42), (43), (44), and (45) are instantiations of the
(discrete) Galerkin-Hodge operator. It should be emphasized that the Galerkin-Hodge
operator is not a natural consequence of DEC. The Galerkin-Hodge operator was origi-
nally proposed in [54]. It satisﬁes a number of built-in properties for stability in arbitrary
simplicial meshes as discussed, for example, in references [43],[55],[56],[57]. In particular,
the Galerkin-Hodge operator enforces standard local energy positivity [42].
The ﬁeld updates in (40) and (41) call for sparse linear solvers due to the presence
of the matrices [⋆ϵ]0→0 and [⋆ϵ]1→1. From (42) and (44), it is seen that [⋆ϵ]0→0 and
[⋆ϵ]1→1 are diagonally dominant and symmetric positive deﬁnite matrices; consequently,
the linear solve can be performed very quickly. Nevertheless, this needs to be repeated
at every time step. The linear solve can be obviated by computing a sparse approximate
inverse (SPAI) of [⋆ϵ]0→0 and [⋆ϵ]1→1 prior to the start of the time updating procedure.
This strategy is discussed in [25] and [41].
The present algorithm is explicit and hence
conditionally stable. The stability conditions are discussed in Appendix G.
2.4. Symmetry axis singularity treatment
For BOR problems where the line ρ = 0 (symmetry axis) is part of the solution
domain (for example, in hollow waveguides), it becomes necessary to treat the ﬁeld
behavior there by means of appropriate boundary conditions. The boundary conditions
at ρ = 0 are mode-dependent and should account for the cylindrical coordinate system
singularity and the related degeneracy of the ˆρ and ˆφ unit vectors there. When m = 0,
there is no ﬁeld variation along azimuth and, in the absence of charges at ρ = 0, both
azimuthal and radial ﬁeld components are zero at ρ = 0. On the other hand, the axial
ﬁeld component should be zero for m ̸= 0 [58] since the axial direction is invariant with
10


## Page 11


(a)
(b)
(c)
(d)
Figure 4: Field boundary conditions on the primal mesh for the TEφ ﬁeld with (a) perfect magnetic
conductor (m = 0) and (b) perfect electric conductor (m ̸= 0) and for the TMφ ﬁeld with (c) perfect
magnetic conductor (m ̸= 0) and (d) perfect electric conductor (m = 0). Dashed lines indicate Dirichlet
boundary condition, for example edges on the z axis representing a perfect electric conductor boundary
for TEφ ﬁeld in (b), or nodes on the z axis representing a perfect electric conductor boundary for the
TMφ ﬁeld in (d).
11


## Page 12


respect to φ and a ﬁeld dependency of the form cos (mφ) or sin (mφ) with m ̸= 0 would
imply a multivalued result at ρ = 0 due to the coordinate degeneracy there. As a result,
when m = 0, the boundary ρ = 0 can be represented as a perfect electric conductor
for the TEφ ﬁeld and as a perfect magnetic conductor for the TMφ ﬁeld. Conversely,
when m ̸= 0, the ρ = 0 boundary can be represented as a perfect magnetic conductor
for the TEφ ﬁeld and as a perfect electric conductor for the TMφ ﬁeld. A homogeneous
Neumann boundary condition for the electric ﬁeld can be used to represent the perfect
magnetic conductor case and a homogeneous Dirichlet boundary condition for the perfect
electric conductor case. Implementation of such boundary conditions on the primal mesh
is illustrated in Fig. 4. Dashed lines in Fig. 4b and 4d denote the Dirichlet boundary
implementation: along the z axis, the perfect electric conductor condition is enforced
on grid edges for the TEφ case and on grid nodes for the TMφ case. Likewise, Fig. 4a
and 4c illustrate application of the Neumann boundary condition: along the z axis, the
perfect magnetic conductor condition is enforced on grid edges for the TEφ case and on
grid nodes for the TMφ case.
Using the boundary conditions described above, the present FETD-BOR Maxwell
solver does not require any modiﬁcations in the basis functions on the grid cells adjacent
to the z axis, unlike prior FE-BOR Maxwell solvers.
3. Numerical Examples
In order to validate present FETD-BOR Maxwell solver, we ﬁrst consider a cylindrical
cavity and compare the resonance frequency results to the analytical predictions. Then,
we illustrate two practical examples of devices based on BOR geometries: logging-while-
drilling sensors used for Earth formation resistivity proﬁling in geophysical exploration
and relativistic BWO for high-power microwave applications.
3.1. Cylindrical cavity
We simulate the eigenfrequencies of a hollow cylindrical cavity with metallic walls
using the present FETD-BOR Maxwell solver, and compare the results to analytic pre-
dictions. The cavity has radius a = 0.5 m and height h = 1 m, as depicted in Fig. 5.
Magnetic and electric dipole current sources M (r, t) and J (r, t) oriented along φ and
excited by broadband Gaussian-modulated pulses are placed at arbitrary locations inside
the cavity rs = (ρs, φs, zs), so that
M (r, t) , J (r, t) = ˆφ G(t) δ (r −rs) =
= ˆφ G(t) δ

r∥−r∥
s


π + 2π
Mφ
X
m=1
cos [m (φ −φs)]


(46)
where G(t) = e−[(t−tg)/(2σg)]2 sin [2πfg (t −tg)] with tg = 20 ns, σg = 1.9 ns, and fg = 300
MHz, and r∥= ρˆρ + zˆz.
We use Fourier series expansion to describe δ (φ −φs) in
(46) in order to match the modal ﬁeld expansion used before. A total of four dipole
sources (electric and magnetic currents) are used to excite a rich gamut of eigenmodes,
as illustrated in Fig. 5. The meridian plane of the cylindrical cavity is discretized by
an unstructured grid with 4, 045 nodes, 11, 939 edges, and 7, 895 faces (seen as the ρz
12


## Page 13


Figure 5: Schematic view of the simulated cylindrical cavity with perfect electric conductor (PEC) walls.
The cavity dimensions are a = 0.5 m and h = 1 m.
Table 1: Maximum time-step intervals for various cases in the simulation of cylindrical metallic cavity.
m = 0
m ̸= 0
TEφ-pol.
TMφ-pol.
m = 1
m = 2
m = 3
m = 4
∆tmax [ps]
10.009
10.249
10.009
6.4792
4.5545
3.4843
plane for φ = 180o in Fig. 7). The metallic boundaries are treated as perfect electric
conductors. In this case, the maximum azimuthal modal order Mφ was set equal to 4 to
investigate the ﬁeld solution up to this order. Higher order modes can be included by
simply increasing Mφ. This is straightforward since azimuthal modal ﬁelds with diﬀerent
orders are orthogonal to each other. From the stability analysis in Appendix
G, the
maximum time-step intervals for various cases are presented in Table 1. Here we chose
∆t = 1 ps for the simulations and used a total of 1×107 time steps to provide suﬃciently
narrow resonance peaks. By recording the time history of the electric ﬁeld values at
arbitrary locations inside the cavity and performing a Fourier transform, we obtain the
eigenfrequencies as peaks in the Fourier spectrum. Fig. 6 shows the normalized spectral
amplitude as a function of frequency.
The black solid line is the result obtained by
using present FETD-BOR Maxwell solver. The red dashed and blue solid lines indicate
analytic predictions for the eigenfrequencies of the TEmnp and TMmnp modes in this
13


## Page 14


Figure 6:
Normalized spectral amplitude for E, showing the eigenfrequencies of the cavity.
Black
solid lines correspond to the present FETD-BOR result. Red solid and blue dashed lines are analytic
predictions for the TEmnp and TMmnp eigenfrequencies, respectively.
cavity, respectively. The analytic expressions for the eigenfrequencies are given by
fTEmnp = 2c
π
r
χ′2
mn +
pπ
h
2
,
for m = 0, 1, ..., n = 1, 2, ..., p = 1, 2, ... ,
(47)
fTMmnp = 2c
π
r
χ2mn +
pπ
h
2
,
for m = 0, 1, ..., n = 1, 2, ..., p = 0, 1, ... ,
(48)
where c is speed of light, χmn and χ′
mn are the roots of the equations Jm (aχmn) = 0
and J′m (aχ′
mn) = 0, respectively, with Jm (·) being the Bessel function of ﬁrst kind and
J′m (·) its derivative with respect to the argument. It is clear from Fig. 6 that there is
a great agreement between the simulated and analytic eigenfrequencies. Table 2 shows
the relative error between the simulated fs and analytical fa frequencies. The relative
error is below 0.03 % in all cases, indicating the accuracy of the proposed ﬁeld solver.
To illustrate the ﬁeld behavior, Figs. 7 and 8 show snapshots for electric ﬁeld intensity
and magnetic ﬂux density distribution inside the cavity on four ρz planes with φ =
0o, φ = 90o, 180o, 270o and two ρφ planes with z = 0.2 m and 0.8 m, at four time
instants: 1.0024 µs, 1.0028 µs, 1.0032 µs, and 1.0036 µs. Due to the location of the
dipole sources, the transient ﬁelds produced include many eigenmodes, and are basically
asymmetric. It can be seen that the (tangential or normal) boundary conditions on the
outer perfect electric conductor walls for electric ﬁeld intensity and magnetic ﬂux density
are well satisﬁed. Moreover, the correct ﬁeld distribution along the symmetry axis is well
reproduced by the chosen boundary conditions at ρ = 0, without any spurious artifacts.
14


## Page 15


(a)
(b)
(c)
(d)
Figure 7: Transient snapshots for Ez inside the cylindrical cavity at (a) 1.0024 [µs], (b) 1.0028 [µs], (c)
1.0032 [µs], and (d) 1.0036 [µs].
15


## Page 16


(a)
(b)
(c)
(d)
Figure 8: Transient snapshots for Bz inside the cylindrical cavity at (a) 1.0024 [µs], (b) 1.0028 [µs], (c)
1.0032 [µs], and (d) 1.0036 [µs].
16


## Page 17


Table 2: Eigenfrequencies for the cylindrical cavity and normalized errors between numerical and analytic
results.
Resonant modes
fa [MHz]
|fa −fs| /fa × 100 [%]
TM010
229.6369
1.1854 × 10−2
TE111
231.1104
8.0278 × 10−4
TM011
274.2865
2.4558 × 10−2
TE211
327.9619
1.0503 × 10−2
TE112
347.7241
1.7614 × 10−2
TM110
365.8931
2.8110 × 10−2
TM012
377.8003
7.0851 × 10−3
TE011, TM111
395.4463
1.5709 × 10−3
TE212
418.4005
9.3816 × 10−3
TE311
428.3025
6.0946 × 10−3
TE012, TM112
473.1572
1.2629 × 10−2
TE113
483.1273
4.4680 × 10−3
TM210
490.4134
5.2154 × 10−3
TE312
500.9421
1.0443 × 10−2
TM013
505.2060
2.0998 × 10−3
TM211
512.8404
8.3352 × 10−3
TM020
527.1202
2.3910 × 10−2
TE411
529.4750
6.8899 × 10−3
TE121
530.7481
2.5411 × 10−2
TE213
536.2453
5.4133 × 10−3
TM021
548.0472
2.9989 × 10−2
3.2. Logging-while-drilling sensor simulation
Logging-while-drilling sensors have BOR geometries and are routinely used for hy-
drocarbon exploration [16, 17, 18, 19, 20, 21]. As the drilling process is performed, these
sensors record logs obtained by the measurements of ﬁelds produced by loop (multi-coil)
antennas present in the sensor and reﬂected from the surrounding geological formation.
Logging-while-drilling sensors are typically equipped with a series of transmitter and re-
ceiver loop antennas that are wrapped around the outer diameter of a metallic mandrel
attached to the bit drill [59, 60, 61, 62, 63, 64]. Fields produced by the transmitter coil(s)
interact with the adjacent well-bore environment and are detected by a pair (or more)
of receiver coils along the logging-while-drilling sensor at same axial distance from the
transmitter(s). Two types of measurements are typically used to determine the resis-
tivity proﬁles of the adjacent formation. The ﬁrst is the amplitude ratio (AR) between
the electromotive force (e.m.f.) excited at the two receiver coils and the second is their
phase diﬀerence (PD). In this section, we consider a prototypical concentric logging-while-
drilling sensor generating a TMφ ﬁeld distribution in the formation with m = 03. The
logging-while-drilling sensor depicted in Fig. 9 consists of a metallic cylindrical mandrel
modeled as a perfect electric conductor inside a concentric cylindrical borehole. Three
3Not only the geometry but also the ﬁeld excitation is axisymmetric in this case.
17


## Page 18


Figure 9: Logging-while-drilling sensor problem geometry (from inner to outer features): metallic man-
drel, transmit (Tx) and receive (Rx) coil antennas, mud-ﬁlled borehole, and adjacent geological forma-
tion.
loop antennas are used: one as transmitter and two as receivers. The borehole created
by the drilling process is ﬁlled with a lubricant ﬂuid (mud). The three coil antennas are
moving downward in tandem as the drilling process occur.
We consider two scenarios for the adjacent Earth formation, as shown in Fig. 10.
In the ﬁrst scenario, the borehole is ﬁlled with a low conductive (oil-based) ﬂuid (mud)
having σ = 0.0005 S/m and surrounded by geological formations with diﬀerent conduc-
tivities. We compute the AR and PD as a function of the formation conductivity. In
the second scenario, the borehole is ﬁlled with a high conductive (water-based) ﬂuid
having σ = 2 S/m, and the formation has three horizontal layers with diﬀerent con-
ductivities as shown. We compute the AR and PD as the set of coil antennas (sensor)
moves downward. In both cases, the relative permittivity and permeability are assumed
equal to one everywhere, and the transmitter coil radiates a 2 MHz signal. In the time
domain, this is implemented through a current signal along the transmitter coil given by
ITx(t) = r(t) sin (ωt), where
r(t) =









0,
t < 0
0.5

1 −cos
 ωt
2α

,
0 ⩽t < αT
1,
t ⩾αT,
(49)
is a raised-cosine ramp function, T = 2π/ω is the signal period, and α is the number of
sine wave cycles during the ramp duration αT. The use of ramp function mitigates high
frequency components otherwise produced by an abrupt turn-on at t = 0, and yields
faster convergence of AR and PD (after approximately one time period T) [21]. We
18


## Page 19


(a)
(b)
Figure 10: Logging-while-drilling sensor responses. (a) First scenario: the conductivity of the adjacent
geological formation is varied. (b) Second scenario: the sensor moves downward through a borehole
surrounded by a geological formation with three horizontal layers.
choose α = 0.5 to yield a continuous ﬁrst-order derivative and no DC (zero-frequency)
component for the signal. From the time-domain signals computed at the two receivers,
we extract the corresponding phases θ and amplitudes A using
θ = tan−1
 q2 sin (ωt1) −q1 sin (ωt2)
q1 cos (ωt2) −q2 cos (ωt1)

,
(50)
A =

q1
sin (ωt1 + θ)
 ,
(51)
where q1 and q2 are signals computed at times t1 and t2, respectively [21]. Next, the AR
and PD are calculated as
AR = ARx2/ARx1,
(52)
PD = θRx2 −θRx1.
(53)
The azimuthal electric current along the transmitter coil is modeled as a nodal current
density on the meridian plane and the metallic mandrel is regarded as perfect electric
conductor. The FE domain is truncated by a PML to mimic an open domain. We use 8
layers for the PML to yield a reﬂectance below −50 dB [30].
Fig. 11 shows results for the behavior of AR and PD versus the conductivity on
a homogeneous formation. The results are compared against previous results obtained
by the ﬁnite-diﬀerence time-domain (FDTD) and the numerical mode matching (NMM)
methods [21]. There is excellent agreement between the results.
Results for the second
scenario are shown in Fig. 12, where PD is plotted as a function of the z position of
the transmitter, zTx, and compared against previous results obtained by the FDTD and
NMM methods [21]. Again, an excellent agreement is obtained. As expected, the PD
19


## Page 20


is higher when the coil antennas are within high attenuation (high conductivity) layer
and vice versa. The conductance proﬁle and the corresponding axial extension of each
formation is shown in green color in Fig. 12. Fig. 13a−Fig. 13f show snapshots of the
electric ﬁeld distributions for diﬀerent zTx to illustrate the ﬁeld behavior.
3.3. Backward-wave oscillator (BWO) in the relativistic regime
In this section, we consider a backward-wave oscillator (BWO) driven by energetic
electron beams in the relativistic regime designed to produce a high-power microwave
signal [65], as depicted in Fig. 14. The proposed FETD-BOR solver is incorporated into a
PIC algorithm [66, 67, 68] to simulate the wave-plasma interaction in the device [9]. The
PIC algorithm is based on an unstructured grid and explained in detail in [9, 24, 25]. For
this problem it suﬃces to consider the TEφ polarized ﬁeld with m = 0. In a relativistic
BWO, the energy of space-charge modes is converted into microwaves via Cerenkov
radiation [69]. The BWO employs a slow-wave structure to produce such radiation [70].
In present case, the BWO system consists of a cathode, an anode, a slow-wave structure
with sinusoidal corrugations, a beam collector, and a coaxial output port, as depicted
in Fig. 15a. The electron beam is produced by an external voltage between the cathode
and anode. In the slow-wave structure, the space charge modes evolve to TM01 modes.
The oscillation of the modal ﬁeld leads to beam velocity modulation and a quasi-periodic
bunching of the electron beam distribution. Lateral beam conﬁnement is obtained by an
externally applied static magnetic ﬁeld. Coherent RF signals are detected and extracted
at the coaxial RF output port as illustrated in Fig. 15a. The outer radial boundary of
the slow-wave structure is expressed as R (z) = (A −B) cos (2πz/C) + B where A and
B are maximum and minimum radii, respectively, and C is the axial corrugation period.
For X-band operation, we set A = 1.95 cm, B = 1.05 cm, and C = 1.67 cm for a beam-
velocity v = 2.5 × 108 m/s. The coaxial RF output port is truncated by a PML [29, 30].
The unstructured mesh has N0 = 2, 892, N1 = 8, 155, N2 = 5, 264, and lave=1.4468 mm
where lave is an average edge size. The time step is ∆t = 0.5 ps corresponding to the
Courant-Friedrichs-Lewy (CFL) number 0.5. As typical in PIC simulations, we employ a
coarse-graining of the phase space, and each “superparticle” in the simulation represents
1.5 × 108 electrons. The resultant electron density ne yields a Debye length λD = 20.24
mm. The resulting number-density per Debye sphere ND equals 5.56 × 1011 particles
and hence a collisionless plasma assumption is valid in this case. The self-ﬁeld evolution
and spectrum at the output port are shown in Figs. 16a and 16b, respectively. From
Fig. 16a, it is seen that the ﬁeld grows to an RF oscillation near 50 ns and saturates at
around 100 ns. The output signal has a peak at 8.27 GHz, as shown in Fig. 16b. Fig.
15a shows the electron beam distribution at 43.7 ns. The velocity of each particle is
color-encoded and the bunching eﬀect due to velocity modulation is clearly visible. Fig.
15b also illustrates the steady-state proﬁle of the BWO system at 83.3 ns. The vector
plot of the corresponding self-ﬁelds clearly shows that a strong TM01 mode is indeed
present.
4. Conclusion
We presented a new ﬁnite-element time-domain (FETD) Maxwell solver for the anal-
ysis of body-of-revolution (BOR) geometries. The proposed solver is based on discrete
20


## Page 21


exterior calculus (DEC) and transformation optics (TO) concepts.
We explored TO
principles to map the original 3-D problem from a cylindrical coordinate system to an
equivalent problem on a 2-D (Cartesian-like) meridian ρz plane, where the cylindrical
metric is factored out from the diﬀerential operators and embedded on an eﬀective (ar-
tiﬁcial) inhomogeneous and anisotropic medium that ﬁlls the domain. This enables the
use of Cartesian 2-D FE code with no modiﬁcations necessary except to accommodate
the presence of anisotropic media. The spatial discretization is done on an unstructured
mesh on the 2-D meridian plane and eﬀected by decomposing the ﬁelds into their TEφ
and TMφ components and expanding each eigenmode into an appropriate set of (vector
or scalar) basis functions (Whitney forms) based on DEC principles. A leap-frog (sym-
plectic) time-integrator is applied to the semi-discrete Maxwell curl equations and used
to obtain a fully discrete, marching-on-time evolution algorithm. Unlike prior solvers,
the present FETD-BOR Maxwell solver does not require any modiﬁcations on the basis
functions adjacent to the symmetry axis. Rather, the ﬁeld behavior on the symmetry
axis can be simply implemented through properly selected homogeneous Dirichlet and
Neumann applied to the eigenmodal expansion.
Acknowledgments
This work was supported in part by National Science Foundation grant ECCS-
1305838, Department of Defense, Defense Threat Reduction Agency grant HDTRA1-
18-1-0050, Ohio Supercomputer Center grants PAS-0061 and PAS-0110, S˜ao Paulo State
Research Foundation (FAPESP) grant 2015/50268-5, and the Ohio State University Pres-
idential Fellowship program.
The content of the information does not necessarily reﬂect the position or the policy
of the U.S. federal government, and no oﬃcial endorsement should be inferred.
21


## Page 22


(a)
(b)
Figure 11: Computed (a) AR and (b) PD (in deg.) by a logging-while-drilling sensor surrounded by
homogeneous geological formations with diﬀerent conductivities. This corresponds to the ﬁrst scenario
in Fig. 10. The results from the present algorithm are compared against FDTD and NMM results [21]
(see more details in the main text).
22


## Page 23


Figure 12: Computed PD (deg.) between the two receivers of the logging-while-drilling sensor versus
the z position of the transmitter coil antenna. This corresponds to the second scenario in Fig. 10. The
results from the present algorithm are compared against FDTD and NMM results [21] (see more details
in the main text).
23


## Page 24


(a)
(b)
(c)
(d)
(e)
(f)
Figure 13: Electric ﬁeld distribution during the half period for zTx = (a) −50 inch, (b) −25 inch, (c) 5
inch, (d) 25 inch, (e) 50, and (f) 70 inch. Note that zTx = 0 at the interface between ﬁrst (5 S/m) and
second (0.0005 S/m) formations.
24


## Page 25


Figure 14:
Relativistic backward-wave oscillator with a sinusoidally-corrugated slow-wave structure
driven by a relativistic electron beam.
(a)
(b)
Figure 15: Snapshots for (a) the velocity-modulated electron beam at 43.7 ns and (b) the electric ﬁeld
(self-ﬁeld) distribution at 83.3 ns. The vertical axis is ρ and horizontal axis is z.
25


## Page 26


(a)
(b)
Figure 16: Output signals from the BWO device in (a) time domain and (b) frequency domain.
26


## Page 27


Appendix A. Whitney forms and pairing operations
Whitney p-forms are canonical interpolants of discrete diﬀerential p-forms [? ]. As
explained below, Whitney p-forms are naturally paired to the p-cells of the mesh, where
p refers to the dimensionality, i.e. p = 0 refers to nodes, p = 1 to edges, p = 1 to facets
and so on [38]. On simplices (e.g. on triangular cells in 2-D or tetrahedral cells in 3-D),
Whitney 0-, 1-, and 2-forms are expressed as [38, 52? ]
w(0)
i
= λi,
(A.1)
w(1)
i
= λiadλib −λibdλia,
(A.2)
w(2)
i
= 2 (λiadλib ∧dλic + λibdλic ∧dλia + λicdλia ∧dλib) ,
(A.3)
where d is the exterior derivative, ∧is the exterior product, ia, ib, and ic denote the grid
nodes belonging to the i-th p-cell for p = 1 or 2, and λ denotes the barycentric coordinate
associated to a given node.
The corresponding vector proxies for Whitney 0-, 1-, and 2-forms write as [24, 38]
W(0)
i
= λi,
(A.4)
W(1)
i
= λia∇λib −λib∇λia,
(A.5)
W(2)
i
= 2 (λia∇λib × ∇λic + λib∇λic × ∇λia + λic∇λia × ∇λib) ,
(A.6)
One of the key properties of Whitney p-forms is that they admit a natural “pairing”
with the p-cells of the mesh [38]. Computationally, the pairing operation between an i-th
p-cell of the grid σi
(p) and a Whitney form w(p)
j
associated with the j-th p-cell is eﬀected
by the integral below and yields [38, 43]
D
σi
(p), w(p)
j
E
=
Z
σi
(p)
w(p)
j
= δi,j,
(A.7)
where δi,j is the Kronecker delta, for p = 0, . . . , 3 in 3-D space.
Appendix B. Generalized Stokes’ theorem
The generalized Stokes’ theorem of exterior calculus [38, 43, 40, 71, 72] states
D
σ(p+1), dw(p)
j
E
=
D ∂σ(p+1)

(p) , w(p)
j
E
(B.1)
where ∂is the boundary operator that maps an (oriented) p-cell on the grid to the set
of (oriented) (p −1)-cells comprising its boundary. Note that ∂2 = 0 and hence d2 = 0
from (B.1). This latter identity is the exterior calculus counterpart of the vector calculus
identities ∇× ∇= 0 and ∇· ∇× = 0.
The generalized Stokes’ theorem recovers Stokes’ and Gauss’ theorems of vector cal-
culus for p = 1, 2, respectively, and the fundamental theorem of calculus for p = 0.
27


## Page 28


Appendix C. Discrete Maxwell’s equations
By pairing Faraday’s law for the TEφ ﬁeld set in (26) with K-th 2-cells σK
(2) of the
FE grid (primal mesh) and applying the generalized Stokes’ theorem, we obtain
*
σK
(2),
N1
X
j=1
E∥
j,m (t)
h
d′∥w(1)
j
i+
= −
*
σK
(2), ∂
∂t
N2
X
k=1
B⊥
k,m (t) w(2)
k
+
,
(C.1)
*
∂σK
(2)

(1) ,
N1
X
j=1
E∥
j,m (t) w(1)
j
+
= −
*
σK
(2), ∂
∂t
N2
X
k=1
B⊥
k,m (t) w(2)
k
+
.
(C.2)
Using

∂σK
(2)

(1) = PN1
j=1 CK,jσj
(1), where CK,j is the incidence matrix associated to the
exterior derivative applied to 1-forms (curl operator on the mesh), see Appendix D), we
obtain [38, 43, 73, 74]
N1
X
j=1
CK,jE∥
j,m (t) = −∂
∂tB⊥
K,m (t) ,
(C.3)
for m = −Mφ, ..., Mφ. The elements of the incidence matrix take values in the set of
{−1, 0, 1},
Likewise, pairing (27) with J-th 1-cells σJ
(1) of the primal mesh gives
*
σJ
(1),
N0
X
i=1
E⊥
i,m (t)
h
d′∥w(0)
i
i+
−
*
σJ
(1), |m|
N1
X
j=1
E∥
j,m (t) w(1)
j
+
= −
*
σJ
(1), ∂
∂t
N1
X
j=1
B∥
j,m (t) w(1)
j
+
,
(C.4)
and applying generalized Stokes’ theorem to the left-hand side of (C.4) yields
*
∂σJ
(1)

(0) ,
N0
X
i=1
E⊥
i,m (t) w(0)
i
+
−
*
σJ
(1), |m|
N1
X
j=1
E∥
j,m (t) w(1)
j
+
= −
*
σJ
(1), ∂
∂t
N1
X
j=1
B∥
j,m (t) w(1)
j
+
,
(C.5)
Similarly to before, we can write

∂σJ
(1)

(0) = PN0
i=1 GJ,iσi
(1), where GJ,i is the incidence
matrix associated to the exterior derivative applied to 0-forms (gradient operator on the
mesh), and obtain
N0
X
i=1
GJ,iE⊥
i,m (t) −|m| E∥
J,m (t) = −∂
∂tB∥
J,m (t) ,
(C.6)
An analogous procedure can be used to obtain the discrete rendering of Ampere’s law
for on the dual mesh.
28


## Page 29


Figure D.17: Example (primal) unstructured mesh.
Appendix D. Incidence Matrices
Incidence matrices can be used to represent on a mesh the discrete exterior deriva-
tive or, equivalently, the grad, curl, and div operators distilled from their metric struc-
ture [38, 43, 72]. Since, from (B.1), the discrete exterior derivative can be seen as the
dual of the boundary operator, incidence matrices encode the relationship between each
oriented p-cell of the mesh and its boundary oriented (p −1)-cells (say, between an edge
and its boundary nodes, a face element and its boundary edges, and so on). To provide
a concrete example, we consider a small mesh with perfect magnetic conductor (or free
edges) boundaries as depicted in Fig. D.17. Red-colored numbers denote the nodal in-
dices, black-colored numbers the edge indices, and blue-colored numbers the face indices.
Intrinsic edge orientation is deﬁned by ascending index order of the two nodes associated
with any given edge. For example, if we consider [Dcurl], of size N2 × N1, there are
three edges wrapping face number 6: edges 8, 9, and 20. As a result, [Dcurl]6,8 = 1,
[Dcurl]6,9 = −1, and [Dcurl]6,9 = 1.
The sign is determined by comparing the intrinsic
orientation of each edge with the curl in Fig. D.17: if they are opposite, the element
is −1, otherwise it is +1. Furthermore, [Dcurl]6,j = 0 for all other j−th edges. This is
represented in Fig. D.18a, which shows the entire [Dcurl] for this mesh. A curl orien-
tation on each face is supposed to follow the intrinsic orientation of the ﬁrst local edge
(i.e. an edge with the smallest index among three edges for the face). Likewise, if we
consider [Dgrad], of size N1 × N0, there are two nodes connected to edge 10: nodes 4 and
5. The corresponding elements are [Dgrad]10,4 = −1 and [Dgrad]10,5 = 1. The element for
the diverging node with the gradient (the intrinsic edge orientation) in Fig. D.17 is −1,
otherwise it is +1.
29


## Page 30


Appendix E. Discrete Hodge Matrix
A (discrete) Hodge star operator encodes all metric information and is used to trans-
fer information between the primal and dual meshes [38, 40, 47, 51, 75]. Here, we use
a Galerkin-Hodge construction [40, 41, 54, 75], which leads to symmetric positive deﬁ-
nite matrices and enables energy-conserving discretizations with standard local energy
positivity in arbitrary simplicial meshes [43]. As noted in Section 2, the Galerkin-Hodge
operator is not a natural consequence of DEC [57].
The Hodge operator also incorporates the constitutive properties (permittivity and
permeability) of the background medium [30]. Inhomogeneous and anisotropic media can
be easily dealt with by incorporating piecewise constant permittivity and permeability
over each cell, for example. In the present FETD-BOR solver, the elements of the Hodge
matrices including the radial scaling factor from the cylindrical metric are assembled by
adding the contributions from all cells as:
[⋆ϵ]1→1
J,j
=
N2
X
k=1
Z
Ωk
(ϵkρk) W(1)
J
· W(1)
j dV,
(E.1)

⋆µ−12→2
K,k =
N2
X
k=1
Z
Ωk
 µ−1
k ρk

W(2)
K · W(2)
k dV,
(E.2)
[⋆ϵ]0→0
I,i
=
N2
X
k=1
Z
Ωk
 ϵkρ−1
k
 h
W(0)
I
ˆφ
i
·
h
W(0)
i
ˆφ
i
dV,
(E.3)

⋆µ−11→1
J,j
=
N2
X
k=1
Z
Ωk
 µ−1
k ρ−1
k
 h
W(1)
J
× ˆφ
i
·
h
W(1)
j
× ˆφ
i
dV,
(E.4)
where Ωk is the area of the k−th cell, and ρk = P3
i=1 ρki/3 where ρki is ρ coordinate
of i−th node touching k−th face and for simplicity we have assumed isotropic media
assuming permittivity and permeability values ϵk and µk, resp., on cell k. Since Whitney
forms have compact support, we can express the global discrete Hodge matrix as a sum
of local matrices (excluding element-wise permittivity and permeability information) for
the K-th face as
[T ]0→0
K
= ∆K


1/6
1/12
1/12
1/12
1/6
1/12
1/12
1/12
1/6

,
(E.5)
[T ]1→1
K
= ∆K


T 1→1
11
T 1→1
12
T 1→1
13
T 1→1
21
T 1→1
22
T 1→1
23
T 1→1
31
T 1→1
32
T 1→1
33

,
(E.6)
[T ]2→2
K
= 4∆K (∇λ1 × ∇λ2) · ˆφ,
(E.7)
30


## Page 31


where ∆K is the area of K-th face and
T 1→1
11
= ∇λ1 · ∇λ1
6
+ ∇λ2 · ∇λ2
6
−∇λ1 · ∇λ2
6
,
(E.8)
T 1→1
12
= ∇λ1 · ∇λ1
6
−∇λ2 · ∇λ2
6
−∇λ1 · ∇λ2
6
,
(E.9)
T 1→1
13
= ∇λ1 · ∇λ1
6
−∇λ2 · ∇λ2
6
+ ∇λ1 · ∇λ2
6
,
(E.10)
T 1→1
21
= T 1→1
12
,
(E.11)
T 1→1
22
= ∇λ1 · ∇λ1
2
+ ∇λ2 · ∇λ2
6
+ ∇λ1 · ∇λ2
2
,
(E.12)
T 1→1
23
= ∇λ1 · ∇λ1
6
+ ∇λ2 · ∇λ2
6
+ ∇λ1 · ∇λ2
2
,
(E.13)
T 1→1
31
= T 1→1
13
,
(E.14)
T 1→1
32
= T 1→1
23
,
(E.15)
T 1→1
33
= ∇λ1 · ∇λ1
6
+ ∇λ2 · ∇λ2
2
+ ∇λ1 · ∇λ2
2
.
(E.16)
Due to the local support of the Whitney forms, the above Hodge matrices are very
sparse (and diagonally dominant). Their sparsity patterns for the mesh in Fig. D.17 are
provided in Fig. E.19. The number of non-zero elements per row (or column) in these
Hodge matrices is invariant with respect to the mesh size, so the sparsity increases for
larger meshes.
Appendix F. Cartesian-like PML implementation
A perfectly matched layer (PML) is used to absorb outgoing waves in FE simulations,
enabling analysis of open-domain problems [76, 77]. As described before, in the present
FETD-BOR the spatial discretization is performed in the meridian plane mapped onto
a Cartesian domain with the cylindrical metric factor transferred to the constitutive
relations. The resulting constitutive relations correspond to a medium that is inhomo-
geneous and doubly anisotropic. As such, a Cartesian PML implementation extended
to such media can be used.
Such formulation exists [78] and is adapted here to the
FETD-BOR case as follows.
In the 2-D Cartesian plane, the PML can be eﬀected as an analytic continuation on
the spatial variables to complex space [77, 78], given by u →˜u =
R u
0 su (u′) du′ where
su (u′) is a complex stretching variable and u stands for ρ or z. This transformation can
also be expressed as
r
′∥→˜r
′∥= ¯¯Γ · r
′∥,
(F.1)
where ¯¯Γ = ˆρˆρ (˜ρ/ρ) + ˆzˆz (˜z/z). As before, the apostrophe ′ in r
′∥denotes the transverse
coordinates on the 2-D meridian plane. The modiﬁed nabla operator (posterior to the
TO-based transformation and hence devoid of the 1/ρ factor in the φ derivative) following
such analytical continuation is given by
∇′ →˜∇′ = ˆρ 1
sρ
∂
∂ρ + ˆφ ∂
∂φ + ˆz 1
sz
∂
∂z ,
(F.2)
31


## Page 32


or simply
˜∇′ = ¯¯S · ∇′,
(F.3)
where ¯¯S = ˆρˆρ (1/sρ)+ ˆφˆφ (1)+ ˆzˆz (1/sz). Following [78], since su (u) and ∂/∂u′ commute
when u ̸= u′ and ¯¯S is a diagonal tensor, the following identity holds for any vector a in
the Cartesian-like 2-D meridian plane:
∇′ ×
¯¯S−1 · a

=

det¯¯S
−1 ¯¯S ·
¯¯S · ∇′
× a.
(F.4)
Applying this analytic continuation to (18), (19), (32), and (33) in the Fourier domain
(with time convention of ejωt) yields the modiﬁed Maxwell’s equations for each mode m
as
˜∇′∥× E′∥c
m

˜r
′∥
= −jωB′⊥c
m

˜r
′∥
,
(F.5)
˜∇′∥× E′⊥c
m

˜r
′∥
= −jωB′∥c
m

˜r
′∥
+ |m| E′∥c
m

˜r
′∥
× ˆφ,
(F.6)
˜∇′∥× H′∥c
m

˜r
′∥
= jωD′⊥c
m

˜r
′∥
,
(F.7)
˜∇′∥× H′⊥c
m

˜r
′∥
= jωD′∥c
m

˜r
′∥
−|m| H′∥c
m

˜r
′∥
× ˆφ,
(F.8)
with constitutive relations in analytic-continued complex space as
D′c
m

˜r
′∥
= ¯¯ϵ′ (ω) · E′c
m

˜r
′∥
,
(F.9)
B′c
m

˜r
′∥
= ¯¯µ′ (ω) · H′c
m

˜r
′∥
,
(F.10)
where the superscript c denotes non-Maxwellian (complex space) ﬁelds and ¯¯ϵ′ and ¯¯µ′
indicates constitutive parameters of the original medium incorporating the radial scaling
factors from the TO mapping. Next, using (F.1) and (F.3), we can revert (F.5)−(F.8)
back to a real-valued spatial domain by writing
¯¯S · ∇′∥
× E′∥c
m
¯¯Γ · r
′∥
= −jωB′⊥c
m
¯¯Γ · r
′∥
,
(F.11)
¯¯S · ∇′∥
× E′⊥c
m
¯¯Γ · r
′∥
= −jωB′∥c
m
¯¯Γ · r
′∥
−|m| ˆφ × E′∥c
m
¯¯Γ · r
′∥
,
(F.12)
¯¯S · ∇′∥
× H′∥c
m
¯¯Γ · r
′∥
= jωD′⊥c
m
¯¯Γ · r
′∥
,
(F.13)
¯¯S · ∇′∥
× H′⊥c
m
¯¯Γ · r
′∥
= jωD′∥c
m
¯¯Γ · r
′∥
+ |m| ˆφ × H′∥c
m
¯¯Γ · r
′∥
.
(F.14)
32


## Page 33


Using the identity (F.4), we can rewrite (F.11)−(F.14) as
∇′∥×
h¯¯S−1 · E′∥c
m
¯¯Γ · r
′∥i
= −jω

det¯¯S
−1 ¯¯S · B′⊥c
m
¯¯Γ · r
′∥
,
(F.15)
∇′∥×
h¯¯S−1 · E′⊥c
m
¯¯Γ · r
′∥i
= −jω

det¯¯S
−1 ¯¯S · B′∥c
m
¯¯Γ · r
′∥
−|m|

det¯¯S
−1 ¯¯S ·
n
ˆφ × E′∥c
m
¯¯Γ · r
′∥o
,
(F.16)
∇′∥×
h¯¯S−1 · H′∥c
m
¯¯Γ · r
′∥i
= jω

det¯¯S
−1 ¯¯S · D′⊥c
m
¯¯Γ · r
′∥
,
(F.17)
∇′∥×
h¯¯S−1 · H′⊥c
m
¯¯Γ · r
′∥i
= jω

det¯¯S
−1 ¯¯S · D′∥c
m
¯¯Γ · r
′∥
+ |m|

det¯¯S
−1 ¯¯S ·
n
ˆφ × H′∥c
m
¯¯Γ · r
′∥o
.
(F.18)
We can further verify the identity below

det¯¯S
−1 ¯¯S ·
n
ˆφ × E′∥c
m
¯¯Γ · r
′∥o
= ˆφ ×
h¯¯S−1 · E′∥c
m
¯¯Γ · r
′∥i
,
(F.19)

det¯¯S
−1 ¯¯S ·
n
ˆφ × H′∥c
m
¯¯Γ · r
′∥o
= ˆφ ×
h¯¯S−1 · H′⊥c
m
¯¯Γ · r
′∥i
.
(F.20)
and introduce a new set of ﬁelds deﬁned as
E′a
m

r
′∥
= ¯¯S−1 · E′c
m
¯¯Γ · r
′∥
,
(F.21)
H′a
m

r
′∥
= ¯¯S−1 · H′c
m
¯¯Γ · r
′∥
,
(F.22)
D′a
m

r
′∥
=

det¯¯S
−1 ¯¯S · D′c
m
¯¯Γ · r
′∥
,
(F.23)
B′a
m

r
′∥
=

det¯¯S
−1 ¯¯S · B′c
m
¯¯Γ · r
′∥
,
(F.24)
so that, by substituting (F.21)−(F.24) back into (F.15)−(F.18), and utilizing the identi-
ties (F.19) and (F.20), we ﬁnally obtain
∇′∥× E′∥a
m

r
′∥
= −jωB′⊥a
m

r
′∥
,
(F.25)
∇′∥× E′⊥a
m

r
′∥
= −jωB′∥a
m

r
′∥
+ |m| E′∥a
m

r
′∥
× ˆφ,
(F.26)
∇′∥× H′∥a
m

r
′∥
= jωD′⊥a
m

r
′∥
,
(F.27)
∇′∥× H′⊥a
m

r
′∥
= jωD′∥a
m

r
′∥
−|m| H′∥a
m

r
′∥
× ˆφ.
(F.28)
with
D′a
m

r
′∥
=

det¯¯S
−1 n¯¯S · ¯¯ϵ′ (ω) · ¯¯S
o
· E′a
m

r
′∥
,
(F.29)
B′a
m

r
′∥
=

det¯¯S
−1 n¯¯S · ¯¯µ′ (ω) · ¯¯S
o
· H′a
m

r
′∥
.
(F.30)
33


## Page 34


The above expressions show that E′a
m, H′a
m, D′a
m, and B′a
m obey Maxwell’s equations in
an equivalent PML medium with constitutive parameters given by
¯¯ϵPML =

det¯¯S
−1 n¯¯S · ¯¯ϵ′ (ω) · ¯¯S
o
,
(F.31)
¯¯µPML =

det¯¯S
−1 n¯¯S · ¯¯µ′ (ω) · ¯¯S
o
.
(F.32)
As an example, consider a background medium with
¯¯ϵ (ω) =


ϵρ (ω)
0
0
0
ϵφ (ω)
0
0
0
ϵz (ω)

,
(F.33)
¯¯µ (ω) =


µρ (ω)
0
0
0
µφ (ω)
0
0
0
µz (ω)

,
(F.34)
with ϵρ (ω) = ϵφ (ω) = ϵz (ω) =

1 +
σm
jωϵ0

, corresponding to a lossy, isotropic, homoge-
neous medium. After the TO-based mapping, we obtain
¯¯ϵ′ (ω) = ¯¯ϵ (ω) · ¯¯Rϵ =


ϵρ (ω) ρ
0
0
0
ϵφ(ω)
ρ
0
0
0
ϵz (ω) ρ

,
(F.35)
¯¯µ′ (ω) = ¯¯µ (ω) · ¯¯Rµ =


µρ (ω) ρ
0
0
0
µφ(ω)
ρ
0
0
0
µz (ω) ρ

,
(F.36)
As a result, by using (F.31) and (F.32), the elements of the resulting PML constitutive
tensor write as:
ϵPML
ρ
(ω) = ϵ0

1 + σm
jωϵ0
  jωϵ0 + σPML
ρ

(jωϵ0 + σPML
z
) ,
(F.37)
ϵPML
φ
(ω) = ϵ0

1 + σm
jωϵ0

(jωϵ0)2
 jωϵ0 + σPML
ρ

(jωϵ0 + σPML
z
),
(F.38)
ϵPML
z
(ω) = ϵ0

1 + σm
jωϵ0
  jωϵ0 + σPML
z

 jωϵ0 + σPML
ρ
,
(F.39)
µPML
ρ
(ω) = µ0
 jωϵ0 + σPML
ρ

(jωϵ0 + σPML
z
) ,
(F.40)
µPML
φ
(ω) = µ0
(jωϵ0)2
 jωϵ0 + σPML
ρ

(jωϵ0 + σPML
z
),
(F.41)
µPML
z
(ω) = µ0
 jωϵ0 + σPML
z

 jωϵ0 + σPML
ρ
.
(F.42)
where σPML
ρ
and σPML
z
are the artiﬁcial PML conductivities along ρ and z respectively.
The presence of jω factors in the above Fourier-domain elements produce modiﬁca-
tions in the corresponding ﬁeld equations in the time-domain. These modiﬁcations are
34


## Page 35


implemented using an auxiliary diﬀerential equation (ADE) approach as described in,
e.g., [29, 30].
Appendix G. Stability Conditions
To determine the stability conditions, we express the ﬁeld update in matrix form as
¯wn+1 = ¯¯G · ¯wn =
¯¯I + ¯¯T

· ¯wn
(G.1)
with
¯wn =








B⊥
m
n−1
2
h
B∥
m
in−1
2

E⊥
m
n
h
E∥
m
in







,
¯wn+1 =









B⊥
m
n+ 1
2
h
B∥
m
in+ 1
2

E⊥
m
n+1
h
E∥
m
in+1








,
(G.2)
and
¯¯T =





¯¯0N2×N2,
¯¯0N2×N1,
¯¯0N2×N0,
−∆t [Dcurl]
¯¯0N1×N2,
¯¯0N1×N1,
−∆t [Dgrad] ,
∆t |m|¯¯IN1×N1
¯¯0N0×N2,
∆t ¯¯XTMφ,
−∆t2 ¯¯XTMφ · [Dgrad],
∆t2 |m| ¯¯XTMφ
∆t ¯¯XTEφ,
−∆t |m| ¯¯A,
−∆t2 |m| ¯¯A · [Dgrad] ,
−∆t2 ¯¯XTEφ · [Dcurl] −∆t2 |m|2 ¯¯A




,
(G.3)
where
¯¯XTMφ =

[⋆ϵ]0→0−1
· [Dgrad]T ·

⋆−1
µ
1→1 ,
(G.4)
¯¯XTEφ =

[⋆ϵ]1→1−1
· [Dcurl]T ·

⋆−1
µ
2→2 ,
(G.5)
¯¯A =

[⋆ϵ]1→1−1
·

⋆−1
µ
1→1 .
(G.6)
A necessary condition for stability is
λ ¯¯G
 ≤1 for all eigenvalues λ ¯¯G of ¯¯G [79].
When m = 0, the ﬁeld update equation becomes decoupled into two independent
numerical integrators for TEφ and TMφ ﬁelds. In this case, following [41], we can easily
obtain the stability criteria for both polarizations in closed form as
∆tTEφ,m=0 ≤
2
r
max

λXTEφ·[Dcurl]
,
(G.7)
∆tTMφ,m=0 ≤
2
r
max

λXTMφ·[Dgrad]
,
(G.8)
where λXTEφ·[Dcurl] and λXTMφ·[Dgrad] denote the eigenvalues of XTEφ ·[Dcurl] and XTMφ ·
[Dgrad] respectively.
35


## Page 36


When m ̸= 0, we can simply represent ¯¯G using 2 × 2 block matrices ¯¯X and [D] as
¯¯G =
¯¯I(N2+N1)×(N2+N1),
−∆t [D]
∆t ¯¯X,
¯¯I(N0+N1)×(N0+N1) −∆t2 ¯¯X · [D]

(G.9)
where
¯¯X =
¯¯0N0×N2,
¯¯XTMφ
¯¯XTEφ,
−|m| ¯¯A

,
(G.10)
and
[D] =
¯¯0N2×N0,
[Dcurl]
[Dgrad]
−|m|¯¯IN1×N1

.
(G.11)
Therefore, the stability condition is similarly obtained as
∆tm̸=0 ≤
2
r
max

λ ¯¯X·[D]

(G.12)
where λ ¯¯X·[D] are the eigenvalues of ¯¯X · [D]. Note that in this case the maximum time
step depends on the modal index magnitude |m|.
References
References
[1] J.-M. Jin, The ﬁnite element method in electromagnetics, John Wiley & Sons, New Jersey, 2015.
[2] J.-F. Lee, G. M. Wilkins, R. Mitra, Finite-element analysis of axisymmetric cavity resonator using
a hybrid edge element technique, IEEE Trans. Microw. Theory Techn. 41 (11) (1993) 1981–1987.
[3] F. L. Teixeira, J. R. Bergmann, Moment-method analysis of circularly symmetric reﬂectors using
bandlimited basis functions, IEE Proc. - Microw. Antennas Prop. 144 (3) (1997) 179–183.
[4] F. L. Teixeira, J. R. Bergmann, B-spline basis functions for moment-method analysis of axisym-
metric reﬂector antennas, Microw. Opt. Tech. Lett. 14 (3) (1997) 188–191.
[5] G. M. Wilkins, J. F. Lee, R. Mittra, Numerical modeling of axisymmetric coaxial waveguide dis-
continuities, IEEE Trans. Microw. Theory Techn. 39 (8) (1991) 1323–1328.
[6] A. D. Greenwood, J.-M. Jin, Finite-element analysis of complex axisymmetric radiating structures,
IEEE Trans. Antennas Propag. 47 (8) (1999) 1260–1266.
[7] X. Rui, J. Hu, Q. H. Liu, Higher order ﬁnite element method for inhomogeneous axisymmetric
resonators, Progress In Electromagnetics Research B 21 (2010) 189–201.
[8] W. Tierens, D. D. Zutter, BOR-FDTD subgridding based on ﬁnite element principles, Journal of
Computational Physics 230 (12) (2011) 4519 – 4535. doi:https://doi.org/10.1016/j.jcp.2011.
02.028.
[9] D.-Y. Na, Y. A. Omelchenko, H. Moon, B.-H. V. Borges, F. L. Teixeira, Axisymmetric charge-
conservative electromagnetic particle simulation algorithm on unstructured grids: Application to
microwave vacuum electronic devices, J. Comp. Phys. 346 (2017) 295 – 317.
[10] A. Khebir, J. D’Angelo, J. Joseph, A new ﬁnite element formulation for RF scattering by complex
bodies of revolution, IEEE Transactions on Antennas and Propagation 41 (5) (1993) 534–541.
doi:10.1109/8.222272.
[11] L. Medgyesi-Mitschang, J. Putnam, Electromagnetic scattering from axially inhomogeneous bodies
of revolution, IEEE Transactions on Antennas and Propagation 32 (8) (1984) 797–806. doi:10.
1109/TAP.1984.1143430.
36


## Page 37


[12] A. D. Greenwood, J.-M. Jin, A novel eﬃcient algorithm for scattering from a complex BOR using
mixed ﬁnite elements and cylindrical PML, IEEE Trans. Antennas Propagat. 47 (4) (1999) 620–629.
[13] A. N. O’Donnell, R. J. Burkholder, High-frequency asymptotic solution for the electromagnetic
scattering from a small groove around a conical or cylindrical surface, IEEE Trans. Antennas Prop.
61 (2) (2013) 1003–1008.
[14] Y. B. Zhai, X. W. Ping, W. X. Jiang, T. J. Cui, Finite-element analysis of three-dimensional
axisymmetric invisibility cloaks and other metamaterial devices, Commun. Comput. Phys. 8 (4)
(2010) 823–834.
[15] D. Pardo, L. Demkowicz, C. Torres-Verd´ın, M. Paszynski, Simulation of resistivity logging-while-
drilling (LWD) measurements using a self-adaptive goal-oriented hp ﬁnite element method, SIAM
J. Appl. Math 66 (6) (2006) 2085–2106.
[16] M. S. Novo, L. C. da Silva, F. L. Teixeira, Comparison of coupled-potentials and ﬁeld-based ﬁnite-
volume techniques for modeling of borehole EM tools, IEEE Geosci. Remote Sens. Lett. 5 (2) (2008)
209–211.
[17] M. S. Novo, L. C. da Silva, F. L. Teixeira, Three-dimensional ﬁnite-volume analysis of directional
resistivity logging sensors, IEEE Trans. Geosci. Remote Sens. 48 (2) (2010) 1151–1158.
[18] D. Hong, W. F. Huang, H. Chen, Q. H. Liu, Novel and stable formulations for the response of
horizontal-coil eccentric antennas in a cylindrically multilayered medium, IEEE Trans. Antennas
Propag. 65 (4) (2017) 1967–1977.
[19] S. Yang, D. Hong, W. F. Huang, Q. H. Liu, A stable analytic model for tilted-coil antennas in a
concentrically cylindrical multilayered anisotropic medium, IEEE Geosci. Remote Sens. Lett. 14 (4)
(2017) 480–483.
[20] Y. Fang, Z. Y. J. Dai, J. Zhou, Q. H. Liu, Through-casing hydraulic fracture evaluation by induction
logging i: An eﬃcient EM solver for fracture detection, IEEE Trans. Geosci. Remote Sens. 55 (2)
(2017) 1179–1188.
[21] Y.-K. Hue, F. L. Teixeira, L. S. Martin, M. S. Bittar, Three-dimensional simulation of eccentric
LWD tool response in boreholes through dipping formations, IEEE Trans. Geosci. Remote Sens.
43 (2) (2005) 257–268.
[22] M. F. Wong, M. Prak, V. F. Hanna, Axisymmetric edge-based ﬁnite element formulation for bodies
of revolution: Application to dielectric resonators, IEEE MTT-S Digest (1995) 285–288.
[23] F. L. Teixeira, Time-domain ﬁnite-diﬀerence and ﬁnite-element methods for Maxwell equations
in complex media, IEEE Trans. Antennas Propag. 56 (2008) 2150–2166. doi:10.1109/TAP.2008.
926767.
[24] H. Moon, F. L. Teixeira, Y. A. Omelchenko, Exact charge-conserving scattergather algorithm for
particle-in-cell simulations on unstructured grids: A geometric perspective, Comput. Phys. Com-
mun. 194 (2015) 43–53. doi:http://dx.doi.org/10.1016/j.cpc.2015.04.014.
[25] D.-Y. Na, H. Moon, Y. A. Omelchenko, F. L. Teixeira, Local, explicit, and charge-conserving
electromagnetic particle-in-cell algorithm on unstructured grids, IEEE Trans. Plasma Sci. 44 (2016)
1353–1362. doi:10.1109/TPS.2016.2582143.
[26] R. A. Chilton, R. Lee, The discrete origin of FETD-newmark late time instability, and a correction
scheme, J. Comput. Phys. 224 (2007) 1293–1306.
[27] B. He, F. L. Teixeira, On the degrees of freedom of lattice electrodynamics, Phys. Lett. A 336
(2005) 1–7. doi:http://dx.doi.org/10.1016/j.physleta.2005.01.001.
[28] B. He, F. L. Teixeira, Sparse and explicit FETD via approximate inverse Hodge (mass) matrix,
IEEE Microw. Wireless Compon. Lett. 16 (2006) 348–350.
[29] B. Donderici, F. L. Teixeira, Conformal perfectly matched layer for the mixed ﬁnite-element time-
domain method, IEEE Trans. Antennas Propag. 56 (4) (2008) 1017–1026.
[30] B. Donderici, F. L. Teixeira, Mixed ﬁnite-element time-domain method for transient Maxwell equa-
tions in doubly dispersive media, IEEE Trans. Microw. Theory Techn. 56 (1) (2008) 113–120.
doi:10.1109/TMTT.2007.912217.
[31] F. L. Teixeira, W. C. Chew, Diﬀerential forms, metrics, and the reﬂectionless absorption of elec-
tromagnetic waves, J. Electromagn. Waves Appl. 13 (1999) 665–686. doi:http://dx.doi.org/10.
1163/156939399X01104.
[32] J. B. Pendry, D. Schurig, D. R. Smith, Controlling electromagnetic ﬁelds, Science 312 (2006) 1780–
1782. doi:10.1126/science.1125907.
[33] B. He, F. L. Teixeira, Diﬀerential forms, Galerkin duality, and sparse inverse approximations in
ﬁnite element solutions of Maxwell equations, IEEE Trans. Antennas Propag. 55 (2007) 1359–1368.
doi:10.1109/TAP.2007.895619.
[34] J. A. Silva-Macedo, M. A. Romero, B.-H. V. Borges, An extended FDTD method for the analysis
37


## Page 38


of electromagnetic ﬁeld rotations and cloaking devices, Progress In Electromagnetics Research 87
(2008) 183–196.
[35] O. Ozgun, M. Kuzuoglu, Software metamaterials: Transformation media based multiscale tech-
niques for computational electromagnetics, J. Comput. Phys. 236 (2013) 203–219.
[36] O. Ozgun, M. Kuzuoglu, Cartesian grid mapper: Transformation media for modeling arbitrary
curved boundaries with Cartesian grids, IEEE Antennas Wireless Propag. Lett. 13 (2014) 1771–
1774.
[37] L. Kettunen, K. Forsman, A. Bossavit, Discrete spaces for div and curl-free ﬁelds, IEEE Transactions
on Magnetics 34 (5) (1998) 2551–2554. doi:10.1109/20.717588.
[38] F. L. Teixeira, W. C. Chew, Lattice electromagnetic theory from a topological viewpoint, J. Math.
Phys. 40 (1999) 169–187. doi:http://dx.doi.org/10.1063/1.532767.
[39] D. N. Arnold, R. S. Falk, R. Winther, Finite element exterior calculus, homological techniques, and
applications, Acta Numerica 15 (2006) 1–155.
[40] J. Kangas, T. Tarhasaari, L. Kettunen, Reading Whitney and ﬁnite elements with hindsight, IEEE
Transactions on Magnetics 43 (4) (2007) 1157–1160. doi:10.1109/TMAG.2007.892276.
[41] J. Kim, F. L. Teixeira, Parallel and explicit ﬁnite-element time-domain method for Maxwell’s equa-
tions, IEEE Trans. Antennas Propag. 59 (2011) 2350–2356. doi:10.1109/TAP.2011.2143682.
[42] F. L. Teixeira, Diﬀerential forms in lattice ﬁeld theories: An overview, ISRN Math. Phys. 2013
(2013) 16. doi:http://dx.doi.org/10.1155/2013/487270.
[43] F. L. Teixeira, Lattice Maxwell’s equations, Prog. Electromagn. Res. 148 (2014) 113–128.
doi:
10.2528/PIER14062904.
[44] S. C. Chen, W. C. Chew, Numerical electromagnetic frequency domain analysis with discrete ex-
terior calculus, J. Comp. Phys. 350 (2017) 668 – 689. doi:https://doi.org/10.1016/j.jcp.2017.
08.068.
[45] D. M. Shyroki, Eﬃcient Cartesian-grid-based modeling of rotationally symmetric bodies, IEEE
Trans. Microw. Theory Techn. 55 (6) (2007) 1132–1138.
[46] B. He, F. L. Teixeira, Mixed E-B ﬁnite elements for solving 1-D, 2-D, and 3-D time-harmonic
Maxwell curl equations, IEEE Microw. Compon. Lett. 17 (5) (2007) 313–315.
[47] B. He, F. L. Teixeira, Geometric ﬁnite element discretization of Maxwell equations in primal and
dual spaces, Phys. Lett. A 349 (2006) 1–14. doi:http://dx.doi.org/10.1016/j.physleta.2005.
09.002.
[48] P. R. Kotiuga, Weitzenbock identities and variational formulations in nanophotonics and micromag-
netics, IEEE Transactions on Magnetics 43 (4) (2007) 1669–1672. doi:10.1109/TMAG.2007.892497.
[49] S. Rao, D. Wilton, A. Glisson, Electromagnetic scattering by surfaces of arbitrary shape, IEEE
Transactions on Antennas and Propagation 30 (3) (1982) 409–418. doi:10.1109/TAP.1982.1142818.
[50] K. F. Warnick, Numerical Analysis for Electromagnetic Integral Equations, Artech House, Boston,
2008.
[51] A. Gillette, C. Bajaj, Dual formulations of mixed ﬁnite element methods with applications,
Computer-Aided Design 43 (10) (2011) 1213 – 1221, solid and Physical Modeling 2010.
doi:
https://doi.org/10.1016/j.cad.2011.06.017.
[52] A. Bossavit, Whitney forms: A class of ﬁnite elements for three-dimensional computations in elec-
tromagnetism, IEE Proc., Part A: Phys. Sci., Meas. Instrum., Manage. Educ. 135 (1988) 493–500.
doi:10.1049/ip-a-1.1988.0077.
[53] P. W. Gross, P. R. Kotiuga, Electromagnetic Theory and Computation: A Topological Approach,
Cambridge Univ. Press, Cambridge, 2004.
[54] J. Dodziuk, Finite-diﬀerence approach to the Hodge theory of harmonic forms, Am. J. Math. 98 (1)
(1976) 79–104.
URL http://www.jstor.org/stable/2373615
[55] T. Tarhasaari, L. Kettunen, A. Bossavit, Some realizations of a discrete Hodge operator: a rein-
terpretation of ﬁnite element techniques [for EM ﬁeld analysis], IEEE Trans. Magn. 35 (3) (1999)
1494–1497. doi:10.1109/20.767250.
[56] A. Bossavit, Computational electromagnetism and geometry (5): The Galerkin hodge, J. Japan
Soc. Appl. Electromagn. Mech. 8 (2) (2000) 203–209.
[57] P. R. Kotiuga, Theoretical limitations of discrete exterior calculus in the context of computational
electromagnetics, IEEE Trans. Magn. 44 (6) (2008) 1162–1165. doi:10.1109/TMAG.2007.915998.
[58] J. E. Lebaric, D. Kajfez, Analysis of dielectric resonator cavities using the ﬁnite integration tech-
nique, IEEE Trans. Microw. Theory Techn. 37 (11) (1989) 1740–1748.
[59] H. Li, H. Wang, Investigation of eccentricity eﬀects and depth of investigation of azimuthal resis-
tivity LWD tools using 3d ﬁnite diﬀerence method, J. Petroleum Sci. Eng. 143 (2016) 211–225.
38


## Page 39


[60] Z. Q. Zhang, Q. H. Liu, Simulation of induction-logging response using conjugate gradient method
with nonuniform fast Fourier and fast Hankel transforms, Radio Sci. 36 (4) (2001) 599–608.
[61] M. S. Novo, L. C. da Silva, F. L. Teixeira, A comparative analysis of Krylov solvers for three-
dimensional simulations of borehole sensors, IEEE Geosci. Remote Sens. Lett. 8 (1) (2011) 98–102.
[62] H. O. Lee, F. L. Teixeira, L. E. S. Martin, M. S. Bittar, Numerical modeling of eccentered LWD
borehole sensors in dipping and fully anisotropic earth formations, IEEE Trans. Geosci. Remote
Sens. 50 (3) (2012) 727–735.
[63] G. S. Liu, F. L. Teixeira, G. J. Zhang, Analysis of directional logging tools in anisotropic and
multieccentric cylindrically-layered earth formations, IEEE Trans. Antennas Propag. 60 (1) (2012)
318–327.
[64] G. S. Rosa, J. R. Bergmann, F. L. Teixeira, A robust mode-matching algorithm for the analysis of
triaxial well-logging tools in anisotropic geophysical formations, IEEE Trans. Geosci. Remote Sens.
55 (5) (2017) 2534–2545.
[65] S. H. Gold, G. S. Nusinovich, Review of high-power microwave source research, Rev. Sci. Instrum.
68 (1997) 3945–3974. doi:http://dx.doi.org/10.1063/1.1148382.
[66] J. M. Dawson, Particle simulation of plasmas, Rev. Mod. Phys. 55 (1983) 403–447. doi:10.1103/
RevModPhys.55.403.
[67] R. W. Hockney, J. W. Eastwood, Computer Simulation Using Particles, CRC Press, New York,
1988.
[68] C. K. Birdsall, A. B. Langdon, Plasma Physics via Computer Simulation, CRC Press, New York,
2004.
[69] R. A. Cairns, A. D. R. Phelps, Generation and Application of High Power Microwaves, CRC Press,
New York, 1997.
[70] U. Chipengo, M. Zuboraj, N. K. Nahar, J. L. Volakis, A novel slow-wave structure for high-power-
band backward wave oscillators with mode control, IEEE Trans. Plasma Sci. 43 (2015) 1879–1886.
doi:10.1109/TPS.2015.2431647.
[71] S. S. Cairns, The generalized theorem of Stokes, Trans. Amer. Math. Soc. 40 (1936) 167–174.
[72] L. Kettunen, K. Forsman, A. Bossavit, Gauging in Whitney spaces, IEEE Transactions on Magnetics
35 (3) (1999) 1466–1469. doi:10.1109/20.767243.
[73] T. J. Hughes, W. K. Liu, T. K. Zimmermann, Lagrangian-Eulerian ﬁnite element formulation for
incompressible viscous ﬂows, Comput. Method Appl. M. 29 (1981) 329–349.
[74] A. H. Guth, Existence proof of a nonconﬁning phase in four-dimensional U(1) lattice gauge theory,
Phys. Rev. D 21 (1980) 2291–2307.
[75] T. Tarhasaari, L. Kettunen, A. Bossavit, Some realizations of a discrete hodge operator: a rein-
terpretation of ﬁnite element techniques [for EM ﬁeld analysis], IEEE Transactions on Magnetics
35 (3) (1999) 1494–1497. doi:10.1109/20.767250.
[76] J.-P. Berenger, A perfectly matched layer for the absorption of electromagnetic waves, Journal of
Computational Physics 114 (2) (1994) 185 – 200. doi:https://doi.org/10.1006/jcph.1994.1159.
[77] F. L. Teixeira, W. C. Chew, Complex space approach to perfectly matched layers: a review and some
new developments, International Journal of Numerical Modelling: Electronic Networks, Devices and
Fields 13 (5) (2000) 441–455. doi:10.1002/1099-1204(200009/10)13:5<441::AID-JNM376>3.0.CO;
2-J.
[78] F. L. Teixeira, W. C. Chew, General closed-form PML constitutive tensors to match arbitrary
bianisotropic and dispersive linear media, IEEE Microw. Guided Wave Lett. 8 (6) (1998) 223–225.
[79] S. Wang, F. L. Teixeira, Some remarks on the stability of time-domain electromagnetic simulations,
IEEE Trans. Antennas Propag. 52 (3) (2004) 895–898.
39


## Page 40


(a)
(b)
Figure D.18: Incidence matrices for (a) curl [Dcurl] and (b) gradient

Dgrad

operators for the mesh in
Fig. D.17.
40


## Page 41


(a)
(b)
(c)
(d)
Figure E.19: Sparsity patterns for discrete Hodge matrices corresponding to the toy mesh depicted in
Fig. D.17: (a) [⋆ϵ]0→0, (b) [⋆ϵ]1→1, (c)
h
⋆−1
µ
i1→1
, and (d)
h
⋆µ−1
i2→2
.
41

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1804_02030v3_finite_element_time_domain_body_of_revolution_maxwell_solver_based_on_discrete_e
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1804_02030V3_FINITE_ELEMENT_TIME_DOMAIN_BODY_OF_REVOLUTION_MAXWELL_SOLVER_BASED_ON_DISCRETE_E.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

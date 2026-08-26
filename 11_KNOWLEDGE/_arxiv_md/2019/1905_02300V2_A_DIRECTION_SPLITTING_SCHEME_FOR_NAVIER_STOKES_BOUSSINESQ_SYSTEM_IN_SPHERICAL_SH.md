---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.02300v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1905.02300v2_A_direction_splitting_scheme_for_Navier-Stokes-Boussinesq_system_in_spherical_sh

> Source: 1905.02300v2_A_direction_splitting_scheme_for_Navier-Stokes-Boussinesq_system_in_spherical_sh.pdf

> Pages: 18

---


## Page 1


A direction splitting scheme for Navier-Stokes-Boussinesq system in
spherical shell geometries
Aziz Takhirova, Roman Frolova, Peter Mineva,∗
aDepartment of Mathematical and Statistical Sciences, University of Alberta, Edmonton, AB, T6G 2G1, Canada
Abstract
This paper introduces a formally second-order direction-splitting method for solving the incompressible
Navier-Stokes-Boussinesq system in a spherical shell region. The equations are solved on overset Yin-Yang
grids, combined with spherical coordinate transforms. This approach allows to avoid the singularities at the
poles and keeps the grid size relatively uniform. The downside is that the spherical shell is subdivided into
two equally sized, overlapping subdomains that requires the use of Schwarz-type iterations. The temporal
second order accuracy is achieved via an Artiﬁcial Compressibility (AC) scheme with bootstrapping (see
[1, 2],). The spatial discretization is based on second order ﬁnite diﬀerences on the Marker-And-Cell (MAC)
stencil. The entire scheme is implemented in parallel using a domain decomposition iteration, and a direction
splitting approach for the local solves. The stability, accuracy and weak scalability of the method is veriﬁed
on a manufactured solution of the Navier-Stokes-Boussinesq system and on the Landau solution of the
Navier-Stokes equations on the sphere.
Keywords:
Splitting methods, Navier-Stokes equations on the sphere, Parallel algorithm.
1. Introduction
This article presents a new direction-splitting scheme for solving the incompressible Navier-Stokes-
Boussinesq system:
∂u
∂t + (u · ∇)u + ∇p −Pr ∆u = g Pr RaT in Ω× (0, Tf]
∇· u = 0 in Ω× (0, Tf]
u = 0 on ∂Ω× (0, Tf]
(1.1)
∂T
∂t + (u · ∇)T −∆T = 0 in Ω× (0, Tf]
T = 0 on ∂Ω× (0, Tf]
(1.2)
in a spherical shell domain that can be deﬁned in terms of a spherical coordinate triple (r, θ, φ) as:
Ω= {(r, θ, φ) ∈[R1, R2] × [0, π] × [0, 2π)} .
∗Corresponding author
Email addresses: takhirov@ualberta.ca (Aziz Takhirov), frolov@ualberta.ca (Roman Frolov), pminev@ualberta.ca
(Peter Minev)
Preprint submitted to ArXiv.org
February 26, 2020
arXiv:1905.02300v2  [math.NA]  25 Feb 2020


## Page 2


In the above, g is the unit vector in the direction of gravity, and Pr, Ra are the Prandtl and Rayleigh numbers,
respectively. The system (1.1)-(1.2) models the ﬂow of a heat conducting ﬂuid, under the assumption that the
temperature-induced density variation inﬂuences signiﬁcantly only the buoyancy force and the ﬂuid remains
incompressible. It is widely applied to model the ﬂow in the atmospheric boundary layer ([3]), oceanic ﬂows
([4]), as well as, if combined with an equation for the magnetic ﬁeld, the ﬂow in the Earth’s dynamo ([5]).
Even though for the most part of the discussion, we assume homogeneous Dirichlet boundary conditions
on the two spherical surfaces r = R1, r = R2, the approach is applicable to Neumann and Robin boundary
conditions as well.
One widely used approach for numerical approximations of diﬀerential equations in spherical shell ge-
ometries is based on the use of a spherical transformation that transforms the domain into a parallelepiped.
The obvious advantage of this approach is the simple computational domain, which allows for the use of
structured grids and the eﬃcient schemes developed for them. Moreover, the grid can naturally follow the
geometry of the domain, without requiring too many cells, as would possibly be in the case of a Cartesian
formulation. However, the singularity of the transformation and the grid convergence near the poles have for
many years been a diﬃculty in the development of accurate ﬁnite diﬀerence and pseudo-spectral schemes.
Several diﬀerent treatments have been proposed for dealing with these problems. For example, in [6], the pole
singularity issue is avoided by replacing the equations at the poles with equations, analogous to boundary
conditions, while in [7], a redeﬁnition of the singular coordinates is proposed. Other suggested approaches
include applying L’Hospital’s rule [8] to singular terms and switching to Cartesian formulations around the
poles [9].
On the other hand, the grid convergence has been a more serious problem.
In particular, it
produces a solution with uneven resolution, requires very small time steps for explicit or IMEX schemes
since the time step size is limited by the minimum grid size, and causes convergence problems for iterative
solvers. Therefore, diﬀerent grid systems have been suggested in the literature that give quasi-uniform res-
olution and avoid the grid convergence problems. One such approach is the ”cubed sphere” of [10], which
is a grid that covers a spherical surface with six components corresponding to six faces of a cube. Even
though, the resulting grid is quasi-uniform, it still has singularities at the corner points of the faces and it
is non-orthogonal. Some of the other suggested unstructured grids include the isocahedral grid of [11] and
non-orthogonal rhombahedral grid of [12].
In this study we adopt an alternative approach, proposed by [13], employing the so-called Yin-Yang grids.
It starts with a decomposition of the domain into two overlapping subdomains, combined with two diﬀerent
spherical transforms whose axes are perpendicular to each other, cf. Fig. 1. As a result, both subdomains are
transformed into identical parallelepipeds that can be gridded with the same uniform grids. This approach
automatically removes the transforms singularities at the poles, at the expense of the introduction of two
subdomains, so that the two local solutions must be coupled by means of Schwarz-type iterations. It has
been used for simulations of mantle convection [14], core collapse supernovae [15], atmospherical general
circulation model [16] and visualization in spherical regions [17]. Some advantages of Yin-Yang approach
2


## Page 3


are that the metric tensors are simple, the resolution is quasi-uniform, and it requires modest programming
eﬀort for extending the code from a single latitude-longitude grid. The main novelty of this paper is that
the Yin-Yang domain decomposition is combined with a direction splitting time discretization that, in case
of linear parabolic equations, is unconditionally stable on grids on the spherically transformed domains.
The advection can be included either in an IMEX fashion, or by including the linearized advection operator
into the entire operator that is further split direction-wise. The resulting splitting scheme is conditionally
stable, since the direction-wise operators are not positive, but our numerical experience demonstrated that
the second approach yields an algorithm that has better stability performance. This is why the rest of the
paper concerns only this type of schemes. To our knowledge, the stability of the direction splitting approach
has not been rigorously studied in the context a spherical coordinate system. Therefore, we prove below
that it is unconditionally stable in case of a scalar heat equation, in a simply shaped domain (in terms of
spherical coordinates). The case of the full Navier-Stokes-Boussinesq system is more involved and we do not
provide a rigorous proof here. However, our numerical experience shows that the a direction splitting is still
unconditionally stable if the advection terms are omitted and if the velocity-pressure decoupling is done via
the AC method proposed in [1].
The rest of the paper is organized as follows. In the next section, we brieﬂy recall the deﬁnition of the
Yin-Yang domain decompostion. In Section 3 we present the numerical scheme for the advection-diﬀusion
and Navier-Stokes equations on each of the subdomains. In Section 4, we discuss the implementation details,
and in Section 5 we present the numerical experiments.
2. Spatial discretization and the Yin-Yang grid
In this section, we brieﬂy recall the deﬁnition of the composite Yin-Yang grid following [13]. The grid
consists of two identical overlapping latitude-longitude grids whose axes are perpendicular to each other.
The Yin grid is based on a spherical transformation
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
x
= r sin θ cos φ
y
= r sin θ sin φ
z
= r cos θ,
and covers the region
Ω1 :=

(r, θ, φ) ∈[R1, R2] ×
π
4 −ε, 7π
4 + ε

×
π
4 −ε, 3π
4 + ε

,
where ε ≪1 is a parameter determining the overlap.
The Yang grid is obtained via another spherical
transformation:
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
x
= −r sin ˜θ cos ˜φ
y
= r cos ˜θ
z
= r sin ˜θ sin ˜φ,
3


## Page 4


such that its axes is perpendicular to the axes of the Yin transform, and covers the region
Ω2 :=

r, ˜θ, ˜φ

∈[R1, R2] ×
π
4 −ε, 7π
4 + ε

×
π
4 −ε, 3π
4 + ε

.
The choice of the second axes should be such that the Yang grid fully covers the gap of the Yin one, and the
overlapping subregions are of the same size (see Fig. 1,). Otherwise, it is identical to the Yin grid modulo
two rotations. The resulting Yin-Yang grids are quasiuniform, the coordinate transformations from (r, θ, φ)
to (r, ˜θ, ˜φ) and its inverse, as well as the metric tensors on both grids are identical. As a consequence, the
methods and codes developed for the standard latitude-longitude grid can be applied to both grids.
Figure 1: Yang (left) and Yin-Yang (right) grids. Each subgrid is further decomposed into blocks for a parallel implementation
corresponding to a CPU distribution 1 × 3 × 2.
3. Direction-splitting time discretization
3.1. Preliminaries
In the sequel of the paper we will frequently make use of the following notations. For a time sequence
wk, k = 1, 2, . . . we denote the average between two time levels as wk+1/2 = (wk+1 + wk)/2, and the explicit
extrapolation to level k + 1/2 by w∗,k+1/2 = 3wk/2 −wk−1/2. For two regular enough functions u, v deﬁned
in the spherical shell we denote their weighted L2 inner product as: (u, v)ω :=
R2
´
R1
π´
0
2π
´
0
uvωdrdθdφ, where ω
denotes a non-negative weight. In most cases the weight is given by the weight of the spherical transform
ω = r2 sin θ, however, in some of the estimates given below, the weight will be appropriately modiﬁed. The
corresponding norm is given by ∥u∥2
ω = (u, u)ω.
4


## Page 5


3.2. Direction splitting of the advection-diﬀusion equation
Since the PDEs are identical in both domains, it is suﬃcient to develop the numerical scheme for the Yin
domain. Then the Schwarz domain decomposition method can be used to iterate between the subdomains.
We ﬁrst present Douglas [18] type direction splitting scheme for the heat equation. Consider
∂tT −κ∆T = 0 in Ω1 × (0, Tf],
T = 0 on ∂Ω1 × (0, Tf],
(3.1)
where the Laplacian in spherical coordinates is given by
∆= Drr + Dθθ + Dφφ, Drr := 1
r2 ∂r
 r2∂r

, Dθθ :=
1
r2 sin θ∂θ (sin θ∂θ) , and Dφφ :=
∂φφ
r2 sin2 θ.
The Douglas direction splitting scheme for this equation can be summarized in the following factorized form:
h
I −τ
2Drr
i h
I −τ
2Dθθ
i h
I −τ
2Dφφ
i δT n+1
τ
= ∆T n,
(3.2)
where δT n+1 := T n+1 −T n denotes the ﬁrst time diﬀerence of the time sequence T k, τ is the time step, and I
is the identity operator. We ﬁrst notice that this splitting can be considered as an Euler explicit scheme whose
time diﬀerence operator is multiplied by

I −τ
2Drr
 
I −τ
2Dθθ
 
I −τ
2Dφφ

, that is a consistent perturbation
of I and stabilizes the scheme. If the spatial derivative operators are positive and commute with respect to
some inner product, the stability of this scheme is not hard to establish.
Unfortunately, Drr, Dθθ, and Dφφ do not commute with respect to the weighted product (., .)ω, and their
positivity is far from being clear. The main obstacle to commutativity of the one-dimensional operators
comes from the non-constant terms in the denominators of Dθθ and Dφφ. Therefore, the scheme (3.2) should
be modiﬁed as follows. We ﬁrst introduce the modiﬁed spatial operators:
ˆDθθ :=
1
R2
1 sin θ∂θ (sin θ∂θ) , ˆDφφ :=
∂φφ
R2
1 sin2 θ1
,
and ˆ∆:= Drr + ˆDθθ + ˆDφφ,
where θ1 = π
4 −ε. Then it is easy to check that Drr, ˆDθθ and ˆDφφ, supplied with zero Dirichlet boundary
conditions, commute. Moreover,
−

ˆDθθT, T

ω ≥0,
−

ˆDφφT, T

ω ≥0
(3.3)
and
−
h
ˆDθθ −Dθθ
i
T, T

ω ≥0 and −
h
ˆDφφ −Dφφ
i
T, T

ω ≥0.
(3.4)
These inequalities immediately yield that:

−ˆ∆T, T

ω ≥(−∆T, T)ω .
(3.5)
In order to obtain an unconditionally stable second order scheme, we start from the second order Adams-
Bashforth scheme:
δT n+1
τ
= ∆T ∗,n+1/2,
5


## Page 6


and stabilize it by multiplying the time diﬀerence in the left hand side by

I −τ
2Drr
 h
I −τ
2 ˆDθθ
i h
I −τ
2 ˆDφφ
i
.
Since this perturbation is only ﬁrst order consistent with the identity operator, we subtract from the right
hand side the ﬁrst order perturbation term, taken at the previous time level. The resulting splitting scheme
reads:
h
I −τ
2Drr
i h
I −τ
2
ˆDθθ
i h
I −τ
2
ˆDφφ
i δT n+1
τ
= ∆T ∗,n+1/2 −1
2
ˆ∆δT n.
(3.6)
Note that, assuming enough regularity of the exact solution in space and time, this is a second-order per-
turbation of the second-order explicit Adams-Bashforth scheme (3.2), the perturbation being given by:
τ 2
2
ˆ∆δ2T n+1
τ 2
+
τ 2
4 (Drr ˆDθθ + Drr ˆDφφ + ˆDθθ ˆDφφ) −τ 3
8 Drr ˆDθθ ˆDφφ
 δT n+1
τ
.
We have the following stability result for the scheme (3.6).
Theorem 3.1. Assuming enough regularity of the exact solution T of the semi-discrete scheme (3.6), it is
unconditionally stable; more precisely, it satisﬁes the following estimate:
τ
N−1
X
n=1
∥T n+1 −T n∥2
ω
τ 2
+ 1
2∥∇T N∥2
ω + 1
4
 ∥∂θ
 T N −T N−1
∥2
ω1 + ∥∂φ
 T N −T N−1
∥2
ω2

(3.7)
≤1
2∥∇T 1∥2
ω + 1
4
 ∥∂θ
 T 1 −T 0
∥2
ω1 + ∥∂φ
 T 1 −T 0
∥2
ω2

,
where ω1 =

1 −r2
R2
1

sin θ ≥0 and ω2 =

r2
R2
1 −1

sin θ
sin2 θ1 ≥0.
Proof. Expanding the left hand side of (3.6) we get:
h
I −τ
2
ˆ∆+ τ 2
4

Drr ˆDθθ + Drr ˆDφφ + ˆDθθ ˆDφφ

−τ 3
8 Drr ˆDθθ ˆDφφ
 δT n+1
τ
= ∆T ∗,n+1/2 −1
2
ˆ∆δT n.
(3.8)
Rearranging all the ∆and ˆ∆terms, we obtain
δT n+1
τ
−1
2
h
∆−ˆ∆
i  T n+1 −2T n + T n−1
−∆T n+1/2
+
τ 2
4

Drr ˆDθθ + Drr ˆDφφ + ˆDθθ ˆDφφ

−τ 3
8 Drr ˆDθθ ˆDφφ
 δT n+1
τ
= 0.
(3.9)
Next we multiply (3.9) by v = δT n+1 and integrate by parts. Then the second term gives
−1
2
h
∆−ˆ∆
i  T n+1 −2T n + T n−1
, T n+1 −T n
ω
= 1
4

∥∂θ
 T n+1 −T n
∥2
ω1 −∥∂θ
 T n −T n−1
∥2
ω1 + ∥∂θ
 T n+1 −2T n + T n−1
∥2
ω1

(3.10)
+ 1
4

∥∂φ
 T n+1 −T n
∥2
ω2 −∥∂φ
 T n −T n−1
∥2
ω2 + ∥∂φ
 T n+1 −2T n + T n−1
∥2
ω2

.
The third term is
−

∆T n+1/2, T n+1 −T n
ω = 1
2
 ∥∇T n+1∥2
ω −∥∇T n∥2
ω

.
(3.11)
6


## Page 7


The remaining terms are all dissipative:

Drr ˆDθθδT n+1, δT n+12
ω =
ˆ
Ω
r2 sin θ
R2
1
|∂rθδT n+1|2,
(3.12)

Drr ˆDφφδT n+1, δT n+1
ω =
ˆ
Ω
r2 sin θ
R2
1 sin2 θ1
|∂rφδT n+1|2,
(3.13)

ˆDθθ ˆDφφδT n+1, δT n+1
ω =
ˆ
Ω
r2 sin θ
R4
1 sin2 θ1
|∂θφδT n+1|2,
(3.14)
and
−

Drr ˆDθθ ˆDφφδT n+1, δT n+1
ω =
ˆ
Ω
r2 sin θ
R4
1 sin2 θ1
|∂rθφδT n+1|2.
(3.15)
Substituting (3.10)-(3.15) into (3.9), and summing for n = 1, . . . , N −1 completes the proof.
The factorized scheme for the advection-diﬀusion equation (1.2) is obtained in a similar fashion and takes
the following form:
h
I −τ
2

Drr −un+1/2
r
∂r
i
[I −τ
2

ˆDθθ −un+1/2
θ
∂θ
r
 
I −τ
2

ˆDφφ −un+1/2
φ
∂φ
r sin θ
 δT n+1
τ
= ∆T ∗,n+1/2 −1
2
ˆ∆δT n + un+1/2 · ∇T n.
(3.16)
3.3. Direction-splitting discretization of the Navier-Stokes system
Now we present the direction splitting scheme for the Navier-Stokes equations (1.1).
Our numerical
scheme is based on the AC regularization:
∂tu1 + (u1 · ∇)u1 + ∇p1 −1
Re∆u1 = 0
χτ∂tp1 + ∇· u1 = 0,
(3.17)
where χ = O (1) is an artiﬁcial compressibility regularization parameter, and Re is the Reynolds number. It
is well-known that the resulting approximation (u1, p1) is ﬁrst-order accurate in time (see [19]). A second
order scheme can be constructed using the bootstrapping approach of [1, 2], which requires additionally to
solve the system:
∂tu2 + (u2 · ∇)u2 + ∇p2 −1
Re∆u2 = 0
χτ∂t (p2 −p1) + ∇· u2 = 0,
(3.18)
p1 being given by (3.17). In the following, for the sake of brevity, we will only discuss the direction splitting
implementation of the ﬁrst order approximation (3.17).
The higher order correction for u2, p2 is solved
identically.
First, consider the standard semi-implicit Crank-Nicholson approximation of the system for
(u1, p1):
un+1
1
−un
1
τ
+ u∗,n+1/2
2
· ∇un+1/2
1
+ ∇pn+1/2
1
−1
Re∆un+1/2
1
= 0
χ
 pn+1
1
−pn
1

+ ∇· un+1/2
1
= 0
7


## Page 8


Note that we use the second order velocity u2 as advecting velocity, which allows us to assemble a single
linear system for both systems. We can rewrite the momentum equation by eliminating pn+1
1
from the ﬁrst
equation:
un+1
1
−un
1
τ
+ u∗,n+1/2
2
· ∇un+1/2
1
+ ∇pn
1 −1
Re∆un+1/2
1
−1
2χ∇∇·un+1/2
1
= 0
pn+1
1
= pn
1 −1
χ∇· un+1/2
1
.
In order to produce a factorized scheme for each velocity component, the ∇∇· operator must be also split
somehow, and we use the Gauss-Seidel type splitting of the ∇∇· operator, which was originally proposed in
[2] in the Cartesian case:
∇∇·un+1/2 ≃














∂r

∂r(r2un+1/2
r
)
r2
+
∂θ

sin θu∗,n+1/2
θ

r sin θ
+
∂φu∗,n+1/2
φ
r sin θ

∂θ
r

∂r(r2un+1/2
r
)
r2
+
∂θ

sin θun+1/2
θ

r sin θ
+
∂φu∗,n+1/2
φ
r sin θ

∂φ
r sin θ

∂r(r2un+1/2
r
)
r2
+
∂θ

sin θun+1/2
θ

r sin θ
+
∂φun+1/2
φ
r sin θ















:=





D11 + D12 + D13
D21 + D22 + D23
D31 + D32 + D33




un+1/2
3.3.1. Equation for the r-component of the velocity
Using the mass conservation equation ∇· u = 0, it is possible to write the ﬁrst component of the system
as follows:
∂tur + u · ∇ur −∆ur
Re + ∂rp + 1
Re
2ur
r2 −1
Re
2
r3 ∂r
 urr2
−
u2
θ + u2
φ
r
= 0,
where u · ∇v = ur∂rv + uθ
∂θv
r + uφ
∂φv
r sin θ is the advection operator. Let Lrr, Lrθ and Lrφ be the diﬀerential
operators that act in each space direction:
Lrru = 1
Re
 
Drru −2u
r2 + 2∂r
 r2u

r3
!
+ D11u −u∗,n+1/2
2,r
· ∂rur, Lrθu =
 ˆDθθ
Re −u∗,n+1/2
2,θ
· ∂θ
r
!
u,
Lrφu =
 ˆDφφ
Re −u∗,n+1/2
2,φ
·
∂φ
r sin θ
!
u and Lr = Lrr + Lrθ + Lrφ
The factorized scheme for the r-component takes the following form:
h
I −τ
2Lrθ
i h
I −τ
2Lrφ
i h
I −τ
2Lrr
i un+1
1,r −un
1,r
τ
= Lru∗,n+1/2
1,r
+ ˆ∆un−1/2
1,r
−∂rpn
1 +
D12u∗,n+1/2
1,θ
+ D13u∗,n+1/2
1,φ
2χ
+

u∗,n+1/2
θ
2
+

u∗,n+1/2
φ
2
r
.
(3.19)
3.3.2. Equation for the θ–component of the velocity
Again using ∇· u = 0, the θ-component of the momentum equation can be expressed as:
∂tuθ + u · ∇uθ −∆uθ
Re + ∂θp
r
+ 1
Re
uθ
r2 sin2 θ −2 cos θ
Re
∂θ (uθ sin θ)
r2 sin2 θ
−2
Re
∂θur
r2
−2 cos θ
Re
∂r
 urr2
r3 sin θ
+
uruθ −u2
φ cot θ
r
= 0.
8


## Page 9


Let Lθr, Lθθ and Lθφ be deﬁned as follows:
Lθru =
Drr
Re −u∗,n+1/2
2,r
· ∂r

u, Lθφu =
 ˆDφφ
Re −u∗,n+1/2
2,φ
·
∂φ
r sin θ
!
u,
Lθθu = 1
Re

ˆDθθu −
u
r2 sin2 θ + 2 cos θ
sin θ ∂θ (u sin θ)

+
u · u∗,n+1/2
2,φ
cot θ
r
+ u∗,n+1/2
2,θ
· ∂θu
r
+ D22u
2χ ,
and Lθ = Lθr + Lθθ + Lθφ
The factorized scheme for the θ-component takes the following form:
h
I −τ
2Lθφ
i h
I −τ
2Lθr
i h
I −τ
2Lθθ
i un+1
1,θ −un
1,θ
τ
= Lθu∗,n+1/2
1,θ
+ ˆ∆un−1/2
1,θ
−∂θpn
1
r
+
D21un+1/2
1,r
+ D23u∗,n+1/2
1,φ
2χ
+ 1
Re
 2
r2 ∂θun+1/2
1,r
+ 2 cos θ
r3 sin θ∂r

un+1/2
1,r
r2
(3.20)
−
u∗,n+1/2
r
· u∗,n+1/2
φ
r
.
3.3.3. Equation for the φ–component of the velocity
The φ-component of the momentum equation is given by:
∂tuφ + u · ∇uφ + uruφ + uθuφ cot θ
r
−∆uφ
Re +
∂φp
r sin θ + 1
Re

uφ
r2 sin2 θ −2 cos θ
r2 sin2 θ∂φuθ −
2
r2 sin θ∂φur

= 0
Let Lφr, Lφθ and Lφφ be deﬁned as follows:
Lφru =
Drr
Re −u∗,n+1/2
2,r
· ∂r

u and Lφθu =
 ˆDθθ
Re −u∗,n+1/2
2,θ
· ∂θ
r
!
u
Lφφu = 1
Re

ˆDφφ −
1
r2 sin2 θ

u −
u∗,n+1/2
φ
· u
r sin θ
−
u∗,n+1/2
2,r
+ u∗,n+1/2
2,θ
cot θ
r
u and Lφ = Lφr + Lφθ + Lφφ
The factorized scheme for the φ-component is then:
h
I −τ
2Lφr
i h
I −τ
2Lφθ
i h
I −τ
2Lφφ
i un+1
1,φ −un
1,φ
τ
= Lφu∗,n+1/2
1,φ
+ ˆ∆un−1/2
1,φ
−∂φpn
1
r sin θ + 1
Re

2
r2 sin θ∂φun+1/2
1,r
+ 2 cos θ
r2 sin2 θ∂φun+1/2
1,θ

+ D31un+1/2
1,r
+ D32un+1/2
1,θ
.
(3.21)
3.3.4. Pressure update
pn+1
1
= pn
1 −1
χ∇·un+1/2
1
.
(3.22)
9


## Page 10


4. Implementation and parallelization
The equations (3.16), (3.19)-(3.21) are solved as a sequence of 1D equations in each space direction. For
example, solving (3.16) consists of the following steps:
ξn+1
τ
:= 1
2∆T ∗,n+1/2 −1
2
ˆ∆δT n + un+1/2 · ∇T n
ηn+1
τ
:=
h
I −τ
2
ˆDθθ
i h
I −τ
2
ˆDφφ
i T n+1 −T n
τ
⇒
h
I −τ
2Drr
i
ηn+1 = ξn+1
ζn+1
τ
:=
h
I −τ
2
ˆDφφ
i T n+1 −T n
τ
⇒
h
I −τ
2
ˆDθθ
i
ζn+1 = ηn+1
h
I −τ
2
ˆDφφ
i  T n+1 −T n
= ζn+1 ⇒T n+1 =
 T n+1 −T n
+ T n.
Similar strategy is applied for the Navier-Stokes approximation. Each 1D system is spatially approximated
using second-order centered ﬁnite diﬀerences on a non-uniform grid. In order to ensure the inf-sup stability,
the unknowns are approximated on a MAC grid, where the velocity components are stored at the face centers
of the cells, while the scalar variables are stored at the cell centers.
To solve the system on each domain in parallel we use the approach developed in [20], where we ﬁrst
perform Cartesian domain decomposition of both computational grids using MPI, and then solve the resulting
set of tridiagonal linear systems using domain-decomposition-induced Schur complement technique. Note,
that the Schur complement can be computed explicitly (see [20] for details) and so the system in each
direction can be solved directly by the Thomas algorithm, avoiding the need of iterations on each of the two
subdomain. Then, in order to obtain the approximation on the entire spherical shell, we iterate between the
Yin and Yang grids using either additive or multiplicative overlapping Schwarz methods. The solution on
each grid is computed using only boundary data that is interpolated from the currently available solution
on the other grid, using Lagrange interpolation.
In the additive Schwarz implementation, we use an even total number of CPUs. Then we split the global
communicator into two equal parts, and assign to each grid one of the communicators. In the multiplicative
Schwarz implementation, we use the global communicator to solve the problem on each grid sequentially.
The overall solution procedure in case of the multiplicative Schwarz iteration can be summarized as
follows:
Algorithm 4.1. Repeat until convergence:
For i = 1, 2
1) Obtain interpolated boundary values Tbd for ∂Ωi from Ω3−i.
2) Solve the temperature equation in Ωi with using extrapolated velocity values u∗,n+1/2
2
.
3) Obtain interpolated boundary values ubd for ∂Ωi from Ω3−i.
10


## Page 11


4) If

´
∂Ωi
ubd · n
 ≥tol, then minimize the functional (ε ≪1):
J (v) := 1
2 |v −ubd|2
ℓ2 +
1
2ε|∂Ωi|2

ˆ
∂Ωi∩{θ,φ bdry }
v · n +
ˆ
∂Ωi∩{r bdry }
ubd · n

2
,
using the Conjugate Gradient Algorithm until J (·) ≤tol.
5) Update ubd := v and solve the momentum equation in Ωi with the interpolated Dirichlet boundary
conditions in θ, φ directions and with the original boundary conditions in the r direction.
6) Compute the pressure in Ωi using the second equation in (3.17).
7) Interpolate the pressure values at the boundary of ∂Ωi using the available pressure on Ω3−i.
End for.
Step 4 is meant to ensure that there is no spurious mass ﬂux generated through the internal (artiﬁcial)
boundaries due to the interpolation. It is optional, and as our numerical experience shows, it rarely changes
signiﬁcantly the results. Therefore, it is skipped while producing the numerical results presented in the next
section. Skipping Step 7, however, can seriously reduce the rate of convergence of the Schwarz iteration,
as observed in the numerical simulations. Clearly, the AC method for the Navier-Stokes equations does
not require boundary conditions on the pressure. Nevertheless, the exchange of the pressure values does
inﬂuence the pressure gradient that appears in (3.19)-(3.21), and thus it seems to inﬂuence signiﬁcantly the
convergence of the overall iteration. This eﬀect is not well understood and while some other authors (see for
example [21]) also interpolate the pressure values near the internal boundaries, others (e.g. [22] ) interpolate
only the velocity on the internal boundaries.
Another interesting feature of the domain decomposition iteration described above is that it allows to use
the previously computed iterates in order to reduce the splitting error of the direction splitting approximation.
For example, if the factorized form of the direction-split approximation for a given quantity ψ is given by:
(I −Lψ,r)(I −Lψ,θ)(I −Lψ,φ)(ψn,k −ψn−1) = G
where the superscript n denotes the time level of the solution and k denotes the domain decomposition
iteration level, then the splitting error can be reduced by using the modiﬁed equation:
(I −Lψ,r)(I −Lψ,θ)(I −Lψ,φ)(ψn,k −ψn,k−1) = G + (ψn,k−1 −ψn−1) −Lψ(ψn,k−1 −ψn−1),
(4.1)
where Lψ = Lψ,r +Lψ,θ +Lψ,φ. Indeed, in (4.1), the splitting error term (Lψ,rLψ,θ +Lψ,rLψ,φ +Lψ,θLψ,φ −
Lψ,rLψ,θLψ,φ)(ψn,k −ψn−1) at iteration level k has been reduced by the same term at the previous iteration
level (Lψ,rLψ,θ + Lψ,rLψ,φ + Lψ,θLψ,φ −Lψ,rLψ,θLψ,φ)(ψn,k−1 −ψn−1). If this error reduction is employed,
then the iteration becomes a block-preconditioned overlapping domain decomposition iteration, the precon-
ditioner being the factorized operator (I −Lψ,r)(I −Lψ,θ)(I −Lψ,φ). We must also remark here that this
11


## Page 12


iteration needs to converge to an accuracy of the order of τ 2 for the solution of equation (3.17) and τ 3 for
the solution of equation (3.18), in order to preserve the second order accuracy of the overall algorithm.
5. Numerical tests
5.1. Time and space convergence
We verify the convergence rates in space and time using the following manufactured solution, given in a
Cartesian form:
u = cos(t)
 2x2yz, −xy2z, −xyz2T , p = cos(t)xyz, T = 2 cos(t)x2yz.
(5.1)
The parameters used in this test are R1 = 1, R2 = 2, Ra = 1, Pr = 1, and the grids used in the tests are
uniform in each direction. The convergence of the approximation is tested using both, the additive and
multiplicative versions of the scheme. The grid used for the time convergence tests consists of 20 × 92 × 192
MAC cells on each of the two subdomains. The solution error is computed at the ﬁnal time Tf = 10. For the
space convergence tests, the time step is chosen small enough to not inﬂuence the overall error, τ = 0.0001,
and the ﬁnal time is Tf = 1. The grid diameter is computed as the maximum diameter of the MAC cells in
Cartesian coordinates. In both cases the domain decomposition iterations are converged so that the l2 norm
of the diﬀerence between two subsequent iterates, for any of the computed quantities is less than 10−6 (l2
norm denotes the standard mid-point approximation to the L2 norm). Also, the splitting error reduction,
as outlined by equation (4.1), is employed at each iteration.
The graphs of the l2 norm of the errors in both cases are presented in Figure 2. They clearly demonstrate
the second order accuracy of the scheme in space and time.
Next we verify the accuracy of the proposed algorithm on a physically more relevant analytic solution of
the Navier-Stokes equations in a spherical setting, due to Landau (see [23] and [24] for a recent review). The
source term of the equations is equal to zero in this case, and the solution is steady and axisymmetric. In all
cases presented in ﬁgure 4 the multiplicative Schwarz version of the algorithm is used with its convergence
tolerance being set to 10−6, the time step is equal to 10−3, and R1 = 1, R2 = 2. We ﬁrst present in the
top left graph of ﬁgure 4 the l2 error for the velocity and pressure as a function of the grid diameter, at
Re = 1 and the overlap is ϵ = 0.1 The scheme clearly exhibits again a second order convergence rate in
space. In the top right graph we demonstrate the inﬂuence of the overlap size on the error at Re = 1, the
grid size in the r, φ, θ directions being 2.7778 × 10−2, 1.7027 × 10−2, 3.6121 × 10−2 correspondingly. The
eﬀect of the overlap on the error is insigniﬁcant, however, it seriously impacts the stability of the algorithm
i.e. the increase of the overlap improves the stability, particularly at large Reynolds numbers. Finally, the
bottom graph demonstrates the eﬀect of the Reynolds number on the error. Again, the overlap is 0.1 and the
grid sizes are equal to 2.7778 × 10−2, 1.7027 × 10−2, 3.6121 × 10−2 . We should note that the exact solution
for the velocity scales like Re−1 and therefore the errors in the graph are multiplied by the corresponding
Reynolds number. Clearly, the oscillations in the error decrease slower with the increase of the Reynolds
12


## Page 13


number. These oscillations are due to the artiﬁcial compressibility algorithm, since the initial data for the
pressure corresponds to a divergence-free velocity, while the pressure evolution is determined by a perturbed
continuity equation (see [25] and [26] for a detailed discussion on this issue).
Figure 2: Log-log plot of the errors; multiplicative Schwarz iteration. Left graph contains the temporal errors at Tf = 10, while
the right graph contains the spatial error plotted at Tf = 1; R1 = 1, R2 = 2, Ra = 1, Pr = 1.
Figure 3: Log-log plot of the errors; additive Schwarz approach. Left graph contains the temporal errors at Tf = 10, while the
right graph contains the spatial error plotted at Tf = 1; R1 = 1, R2 = 2, Ra = 1, Pr = 1.
5.2. Weak parallel eﬃciency
Next we test the parallel eﬃciency of the code based on the scheme introduced in the previous section.
Since we are interested in solving large size problems, we only measure the weak scalability of our code. The
problem size is 100×100×100 grid cells per each of the Yin and Yang grids on each CPU, and the maximum
number of CPUs used is 960.
Besides, since in the possible applications of this technique (atmospheric
boundary layer, Earth’s dynamo) the thickness of the spherical shell is much smaller than the diameter of
the shell, we use a two-dimensional grid of processors for the grid partitioning. It must be noted though, that
making the grid partitioning three dimensional does not change much the parallel eﬃciency results presented
in this section. The scaling eﬃciency is computed as the ratio of the CPU time on 32 cores divided by the
13


## Page 14


1e-05
1e-04
1e-03
1e-02
1e-01
 0.1
 Error 
 h 
L2(u)
L2(p)
slope 2
1e-04
1e-03
1e-02
 0.01
 0.1
 1
 Error 
 Overlap 
L2(u)
L2(p)
Figure 4: l2 errors. Top left: convergence in space, Re=1. Top right: eﬀect of the overlap on the error; Re=1. Bottom: eﬀect
of the Reynolds number on the velocity error as a function of time.
14


## Page 15


CPU time on n ≥32 cores. The reason for this deﬁnition of eﬃciency is that the particular cluster used in
the scaling tests has processors containing 32 cores each, and the eﬃciency drops very signiﬁcantly between
1 and 32 cores (to about 75%). After this, when the number of cores is a multiple of 32 the eﬃciency remains
very close to the one at 32 cores. One possible explanation of this phenomenon is that in case when the
number of cores is signiﬁcantly less than 32 cores, they need to share the memory bandwidth and cache with
a smaller number of cores, since presumably the rest of the available cores on the given processor are idle
(see e.g. [27], p. 152). Again, we are interested in very large computations, and therefore, using a minimum
of 32 cores is very reasonable.
The scaling results are performed using the Compute Canada (see https://www.computecanada.ca/)
Graham cluster of 2.1GHz Intel E5 −2683 v4 CPU cores, 32 cores per node, and each node connected
via a 100 Gb/s network. The results were calculated using the wall clock time taken to simulate 10 time
steps. We ran two tests, using a ﬁxed number of 1 and 10 domain decomposition iterations, and we present
the scaling results in Fig. 5. The parallel eﬃciency is very slightly dependent on the number of domain
decomposition iterations, and remains above 90% for the number of cores ranging between 32 and 960 (the
maximum allocatable without a special permission on the particular cluster). In our opinion, this is an
excellent scaling result for an implicit scheme for the incompressible Boussinesq equations.
Figure 5: Parallel scalability using up to 960 CPU cores
Acknowledgments
The authors would like to acknowledge the support, under a Discovery Grant, of the National Science
and Engineering Research Council of Canada (NSERC).
This research was enabled in part by support provided by Compute Canada (www.computecanada.ca).
15


## Page 16


References
References
[1] J. Guermond, P. Minev, High-order time stepping for the incompressible Navier–Stokes equations,
SIAM Journal on Scientiﬁc Computing 37 (6) (2015) A2656–A2681.
arXiv:https://doi.org/10.
1137/140975231, doi:10.1137/140975231.
URL https://doi.org/10.1137/140975231
[2] J.-L. Guermond, P. D. Minev, High-order time stepping for the Navier-Stokes equations with minimal
computational complexity, J. Comput. Appl. Math. 310 (2017) 92 – 103.
[3] S. Marras, J. Kelly, M. Moragues, A. Muller, M. Kopera, M. Vazquez, F. Giraldo, G. Houzeaux,
O. Jorba, A review of element-based Galerkin methods for numerical weather prediction: Finite ele-
ments, spectral elements, and discontinuous Galerkin, Arch. Computat. Methods Eng. 23 (2016) 673–
722.
[4] Y. Song, T. Hou, Parametric vertical coordinate formulation for multiscale, Boussinesq, and non-
Boussinesq ocean modeling, Ocean Modelling 11 (2006) 298–332.
[5] N. Schaeﬀer, D. Jault, H.-C. Nataf, A. Furnier, Turbulent geodynamo simulations: a leap towards
Earth’s core, Geophysical Journal International 211 (1) (2017) 1–29.
[6] W. Huang, D. M. Sloan, Pole condition for singular problems: The pseudospectral approximation, J.
Comput. Phys. 107 (2) (1993) 254 – 261. doi:https://doi.org/10.1006/jcph.1993.1141.
URL http://www.sciencedirect.com/science/article/pii/S0021999183711411
[7] K. Mohseni, T. Colonius, Numerical treatment of polar coordinate singularities, J. Comput. Phys.
157 (2) (2000) 787 – 795. doi:https://doi.org/10.1006/jcph.1999.6382.
URL http://www.sciencedirect.com/science/article/pii/S0021999199963829
[8] M. D. Griﬃn, E. Jones, J. D. Anderson, A computational ﬂuid dynamic technique valid at the centerline
for non-axisymmetric problems in cylindrical coordinates, J. Comput. Phys. 30 (3) (1979) 352 – 360.
doi:https://doi.org/10.1016/0021-9991(79)90120-7.
URL http://www.sciencedirect.com/science/article/pii/0021999179901207
[9] P. M. J. Freund, S. Lele, Direct simulation of a supersonic round turbulent shear layer, AIAA paper (97)
(1997) 0760.
URL https://arc.aiaa.org/doi/abs/10.2514/6.1997-760
[10] C. Ronchi, R. Iacono, P. Paolucci, The cubed sphere: A new method for the solution of partial diﬀerential
equations in spherical geometry, J. Comput. Phys/ 124 (1) (1996) 93 – 114. doi:https://doi.org/
16


## Page 17


10.1006/jcph.1996.0047.
URL http://www.sciencedirect.com/science/article/pii/S0021999196900479
[11] J. R. Baumgardner, Three-dimensional treatment of convective ﬂow in the earth’s mantle, Journal of
Statistical Physics 39 (5) (1985) 501–511. doi:10.1007/BF01008348.
URL https://doi.org/10.1007/BF01008348
[12] S. Zhong, M. T. Zuber, L. Moresi, M. Gurnis, Role of temperature-dependent viscosity and sur-
face plates in spherical shell models of mantle convection, Journal of Geophysical Research: Solid
Earth 105 (B5) 11063–11082.
arXiv:https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.
1029/2000JB900003, doi:10.1029/2000JB900003.
URL https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2000JB900003
[13] A. Kageyama, T. Sato, “Yin-Yang grid”: An overset grid in spherical geometry, Geochemistry, Geo-
physics, Geosystems 5 (9). arXiv:https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1029/
2004GC000734, doi:10.1029/2004GC000734.
URL https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2004GC000734
[14] P. J. Tackley, Modelling compressible mantle convection with large viscosity contrasts in a three-
dimensional spherical shell using the yin-yang grid, Physics of the Earth and Planetary Interiors 171 (1)
(2008) 7 – 18, recent Advances in Computational Geodynamics: Theory, Numerics and Applications.
doi:https://doi.org/10.1016/j.pepi.2008.08.005.
URL http://www.sciencedirect.com/science/article/pii/S0031920108002276
[15] Wongwathanarat, A., M¨uller, E., Janka, H.-Th., Three-dimensional simulations of core-collapse su-
pernovae: from shock revival to shock breakout, A&A 577 (2015) A48.
doi:10.1051/0004-6361/
201425025.
URL https://doi.org/10.1051/0004-6361/201425025
[16] Y. Baba, K. Takahashi, T. Sugimura, K. Goto, Dynamical core of an atmospheric general circulation
model on a Yin–Yang grid, Monthly Weather Review 138 (10) (2010) 3988–4005. arXiv:https://doi.
org/10.1175/2010MWR3375.1, doi:10.1175/2010MWR3375.1.
URL https://doi.org/10.1175/2010MWR3375.1
[17] N. Ohno, A. Kageyama, Visualization of spherical data by Yin–Yang grid, Computer Physics Commu-
nications 180 (9) (2009) 1534 – 1538. doi:https://doi.org/10.1016/j.cpc.2009.04.008.
URL http://www.sciencedirect.com/science/article/pii/S0010465509001180
[18] J. Douglas, Alternating direction methods for three space variables, Numerische Mathematik 4 (1)
(1962) 41–63. doi:10.1007/BF01386295.
17


## Page 18


[19] J. Shen, On error estimates of the penalty method for unsteady Navier-Stokes equations, SIAM J.
Numer. Anal. 32 (2) (1995) 386–403.
[20] J. L. Guermond, P. D. Minev, Start-up ﬂow in a three-dimensional lid-driven cavity by means of a
massively parallel direction splitting algorithm, International Journal for Numerical Methods in Fluids
68 (7) 856–871.
arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1002/fld.2583, doi:10.
1002/fld.2583.
URL https://onlinelibrary.wiley.com/doi/abs/10.1002/fld.2583
[21] F. S. H.S. Tang, S. Casey Jones, An overset-grid method for 3d unsteady incompressible ﬂows, J.
Comput. Phys. 191 (2) (2003) 567 – 600. doi:https://doi.org/10.1016/S0021-9991(03)00331-0.
URL http://www.sciencedirect.com/science/article/pii/S0021999103003310
[22] B. Merrill, Y. Peet, P. Fischer, J. Lottes, A spectrally accurate method for overlapping grid solution of
incompressible Navier–Stokes equations, J. Comput. Phys. 307 (2016) 60 – 93. doi:https://doi.org/
10.1016/j.jcp.2015.11.057.
[23] L. Landau, A new exact solution of the Navier-Stokes equations, C.R. Acad. Sci. USSR 43 (1944)
286–295.
[24] L. Li, Y. Li, X. Yan, Homogeneous solutions of stationary Navier–Stokes equations with isolated singu-
larities on the unit sphere. I. One singularity, Arch. Rational Mech. Anal. 227 (2018) 1091–1163.
[25] T. Ohwada, P. Asinari, Artiﬁcial compressibility method revisited: Asymptotic numerical method for
incompressible Navier–Stokes equations, J. Comput. Phys. 229 (2010) 1698–1723.
[26] V. DeCaria, W. Layton, M. McLaughlin, A conservative, second order, unconditionally stable artiﬁcial
compression method, Comput. Methods Appl. Mech. Engrg. 325 (2017) 733–747.
[27] J. W. Keating, Direction-splitting schemes for particulate ﬂows, PhD thesis, University of Alberta,
Edmonton, http://hdl.handle.net/10402/era.33972. (2013).
18

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1905_02300v2_a_direction_splitting_scheme_for_navier_stokes_boussinesq_system_in_spherical_sh
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1905_02300V2_A_DIRECTION_SPLITTING_SCHEME_FOR_NAVIER_STOKES_BOUSSINESQ_SYSTEM_IN_SPHERICAL_SH.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

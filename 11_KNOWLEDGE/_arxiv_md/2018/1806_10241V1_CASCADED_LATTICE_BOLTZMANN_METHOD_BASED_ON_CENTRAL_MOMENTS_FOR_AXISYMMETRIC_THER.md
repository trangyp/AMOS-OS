---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1806.10241v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1806.10241v1_Cascaded_Lattice_Boltzmann_Method_based_on_Central_Moments_for_Axisymmetric_Ther

> Source: 1806.10241v1_Cascaded_Lattice_Boltzmann_Method_based_on_Central_Moments_for_Axisymmetric_Ther.pdf

> Pages: 49

---


## Page 1


Cascaded Lattice Boltzmann Method based on Central
Moments for Axisymmetric Thermal Flows Including
Swirling Eﬀects
Farzaneh Hajabdollahi, Kannan N. Premnath, Samuel W. J. Welch
Department of Mechanical Engineering, University of Colorado Denver, 1200 Larimer
street, Colorado, 80217 , U.S.A
Abstract
A cascaded lattice Boltzmann (LB) approach based on central moments and
multiple relaxation times to simulate thermal convective ﬂows, which are driven
by buoyancy forces and/or swirling eﬀects, in the cylindrical coordinate system
with axial symmetry is presented. In this regard, the dynamics of the axial and
radial momentum components along with the pressure are represented by means
of the 2D Navier-Stokes equations with geometric mass and momentum source
terms in the pseudo Cartesian form, while the evolutions of the azimuthal mo-
mentum and the temperature ﬁeld are each modeled by an advection-diﬀusion
type equation with appropriate local source terms. Based on these, cascaded
LB schemes involving three distribution functions are formulated to solve for
the ﬂuid motion in the meridian plane using a D2Q9 lattice, and to solve for
the azimuthal momentum and the temperature ﬁeld each using a D2Q5 lattice.
The geometric mass and momentum source terms for the ﬂow ﬁelds and the
energy source term for the temperature ﬁeld are included using a new sym-
metric operator splitting technique, via pre-collision and post-collision source
steps around the cascaded collision step for each distribution function. These
result in a particularly simple and compact formulation to directly represent
the eﬀect of various geometric source terms consistently in terms of changes in
Email addresses: farzaneh.hajabdollahiouderji@ucdenver.edu (Farzaneh
Hajabdollahi), kannan.premnath@ucdenver.edu (Kannan N. Premnath),
Sam.Welch@ucdenver.edu (Samuel W. J. Welch)
Preprint submitted to Elsevier
June 28, 2018
arXiv:1806.10241v1  [physics.flu-dyn]  26 Jun 2018


## Page 2


the appropriate zeroth and ﬁrst order moments. Simulations of several complex
buoyancy-driven thermal ﬂows and including rotational eﬀects in cylindrical
geometries using the new axisymmetric cascaded LB schemes show good agree-
ment with prior benchmark results for the structures of the velocity and thermal
ﬁelds as well as the heat transfer rates given in terms of the Nusselt numbers.
Keywords:
Lattice Boltzmann method, Central moments, Multiple relaxation
times, Axisymmetric Flows, Thermal Convection
1. Introduction
Fluid motion in cylindrical coordinates with axial symmetry that is driven
by rotational eﬀects and/or thermal buoyancy eﬀects arise widely in a num-
ber of engineering applications and geophysical contexts (e.g., [1, 2, 3, 4, 5]).
Some examples of technological applications encountering heat and mass trans-
fer eﬀects in axisymmetric ﬂows include pipeline systems, heat exchangers, solar
energy conversion devices, crystal growth and material processing systems, elec-
tronic cooling equipment and turbomachinery. Computational methods play an
important role for both fundamental studies of the ﬂuid mechanics and heat
transfer aspects and as predictive tools for engineering design of such systems.
In general, ﬂuid motion in cylindrical coordinates due to swirling eﬀects and
buoyancy forces, and accompanied by thermal and mass transport is three-
dimensional (3D) in nature.
Computational eﬀort for such problems can be
signiﬁcantly reduced if axial symmetry, which arise in various contexts, can be
exploited; in such cases the system of equations can be reduced to set of quasi-
two-dimensional (2D) problems in the meridian plane. Traditionally, numerical
schemes based on ﬁnite diﬀerence, ﬁnite volume or ﬁnite elements were con-
structed to solve the axisymmetric Navier-Stokes (NS) equations for the ﬂuid
ﬂow along with the advection-diﬀusion equation for the energy transport (e.g.,
[6, 7]).
On the other hand, lattice Boltzmann (LB) methods, which arise as min-
imal kinetic models of the Boltzmann equation, has attracted much attention
2


## Page 3


and application to a wide range of ﬂuid ﬂows and heat and mass transfer prob-
lems [8, 9, 10, 11]. They are based on the streaming of the distribution functions
of particle populations along discrete lattice directions followed by collision on
discrete nodes represented as a relaxation process. The hydrodynamics then
arises from the averaged eﬀect of the stream-and-collide steps, where the ﬂow
variables are related to the various kinetic moments of the distribution of the
particle populations. Hence, the LB methods are characterized as mesoscopic
computational approaches, which have certain unique features and advantages.
These include the following.
The streaming step is linear and exact and all
nonlinearity is modeled locally in the collision step; by contrast, the convective
term in the NS equation is nonlinear and nonlocal. As a result, the pressure ﬁeld
is obtained locally in the LB methods, circumventing the need for the solution
of the time consuming elliptic Poisson equation as in traditional methods. The
exact-advection in the streaming step combined with the collision step based on
a relaxation model leads to a second order accurate method with relatively low
numerical dissipation. The kinetic model for the collision step can be tailored
to introduce additional physics as necessary and its additional degree of free-
dom can be tuned to improve numerical stability. Various boundary conditions
for complex geometries can be represented using relatively simple rules for the
particle populations. Finally, the locality of the method makes it amenable for
almost ideal implementation on parallel computers for large scale ﬂow simula-
tions.
Following an approach for the solution of the Boltzmann equation in cylin-
drical coordinates [12], during the last two decades, various LB schemes for
athermal ﬂows (i.e., without heat transfer eﬀects) have been introduced [13,
14, 15, 16, 17, 18, 19, 20, 21]. These approaches can be categorized accord-
ing to the following: (i) Coordinate transformation method [13, 14, 15, 16, 17],
in which the axisymmetric mass and momentum equations are reformulated
as quasi-2D ﬂow equations in the Cartesian forms with additional geometric
source terms and then solved using a LB scheme. (ii) Vorticity-stream function
approach [18], where LB models are introduced to simulate ﬂows in cylindri-
3


## Page 4


cal coordinates written in terms of the vorticity and stream function equations.
(iii) Radius-weighted formulation [19], in which a simpliﬁed LB method is de-
rived from a discretization of the continuous Boltzmann equation in cylindrical
coordinates recast in a radius-weighted form. An analysis of these axisymmet-
ric LB models were performed by [20]. Generally, these approaches solve for
the axial and radial velocity components in the meridian plane using a popu-
lar single relaxation time (SRT) model for the representation of the collision
step in the LB scheme. The azimuthal velocity ﬁeld to represent axisymmetric
swirling or rotational ﬂows is computed using an additional LB scheme based
on a separate distribution function in a double distribution function (DDF)
framework [19, 21].
Further progress in the LB methods for the simulation of axisymmetric ther-
mal ﬂows have been reported in various studies [22, 23, 24, 25, 26, 27, 28, 29, 30,
31]. Earlier LB models in this regard [22, 23] used an hybrid approach, in which
the energy equation was solved via a ﬁnite diﬀerence scheme. Later, [24, 25]
solved the axisymmetric equation for the temperature ﬁeld written in terms of a
pseudo-2D advection-diﬀusion equation with a source term using a LB scheme
based on a separation distribution function from that for the ﬂow ﬁeld. On
the other hand, [26, 27] extended the radius-weighted formulation approach for
axisymmetric ﬂuid ﬂow [19] for the simulation of thermal energy transport. A
fractional-step based LB ﬂux solver for axisymmetric thermal ﬂow was pre-
sented in [29]. All these approaches were based on the common SRT model [32],
in which, during the collision step, the distribution functions relax to their local
equilibria using a single relaxation parameter. This was further extended by the
introduction of two tunable parameters as coeﬃcients to the additional gradient
terms in the equilibrium distribution functions [31]. Generally, SRT based LB
schemes are known to be susceptible to numerical instabilities for convection-
dominated ﬂows or ﬂuids with relatively low values of transport coeﬃcients.
In order to address this issue, the collision step based on a multiple relaxation
time (MRT) model [33] has been constructed, in which raw moments of diﬀerent
orders relax at diﬀerent rates. Few MRT LB schemes for axisymmetric thermal
4


## Page 5


convective ﬂows have recently been developed [25, 28, 29].
On the other hand, further improvements to the collision step enhancing
the ﬂow and thermal transport modeling capabilities can be achieved via the
introduction of the cascaded collision model [34]. In this approach, the eﬀects
of collisions are represented in terms of relaxation of diﬀerent orders of central
moments, which are obtained by shifting the particle velocity, by the local ﬂuid
velocity at diﬀerent rates. As the collision model is prescribed based on a lo-
cal moving frame of reference, the relaxation steps for successive higher order
moments exhibit a cascaded structure. The cascaded collision formulation was
shown to be equivalent to considering relaxation to a generalized equilibrium in
the rest or lattice frame of reference [35], and was augmented with forcing terms
in 2D and 3D in [36, 37]. Improvements in the numerical properties achieved
using such advanced cascaded collision models based on central moments were
recently demonstrated [38]. A modiﬁed formulation based on central moments
involving relaxation to discrete equilibria rather than continuous Maxwellian
equilibria was also proposed [39]. In order to accelerate convergence of steady
ﬂows, a preconditioned cascaded LB method was constructed and studied in [40],
and whose Galilean invariance properties were signiﬁcantly improved via correc-
tions to equilibria in [41]. The cascaded LB scheme has recently been extended
for simulating ﬂows with heat transfer in 2D [42, 43] and in 3D in our recent
work [44]. However, for axisymmetric thermal convective ﬂows including rota-
tional eﬀects, no such advanced LB schemes are available in the literature.
In this work, we present a new cascaded LB formulation for thermal ﬂows
in cylindrical coordinate with axial symmetry, and including rotational eﬀects.
The mass, momentum (i.e., axial, radial and azimuthal components) and energy
equations rewritten in pseudo-2D Cartesian forms in the meridian plane contain
additional geometric source terms, which are included in the respective cascaded
LB schemes via a novel symmetric time-split formulation [45]. In this approach,
three separate distribution functions are considered: one for the density, axial
and radial momentum components, another one for the azimuthal momentum
component and ﬁnally third one for the temperature ﬁeld. Each of the three
5


## Page 6


distribution functions evolves according to a cascaded LB scheme.
For this
triple distribution functions framework, a two-dimensional, nine velocity (D2Q9)
model is used to solve for the axisymmetric NS equations for the axial and
radial momentum components, while a two-dimensional ﬁve velocity (D2Q5)
model is employed to compute the azimuthal momentum and the temperature
ﬁeld, both of whose evolution are represented by advection-diﬀusion equations
with source terms. The use of symmetric operation split formulations based
on pre-collision and post-collision source steps for incorporating the geometric
source terms for axisymmetric thermal ﬂows including swirl eﬀects leads to a
particulary simpliﬁed formulation, which is consistent with the classical Strang
splitting. The application of central moments based cascaded LB schemes using
MRT can enhanced numerical stability of the LB simulations, and the use of
symmetric operator splitting yields a scheme that is second order in time, as
demonstrated numerically [45]. Such an axisymmetric cascaded LB approach
for the simulation of thermally stratiﬁed and/or rotating ﬂows in cylindrical
geometries can lead to reduced computational and memory costs when compared
to a 3D cascaded LB formulation. Several numerical axisymmetric benchmark
problems focusing on buoyancy-driven ﬂows and rotational eﬀects are considered
to validate our operator-split axisymmetric cascaded LB schemes for thermal
ﬂows. These include the Taylor-Couette ﬂow, natural convection in an annulus
between two co-axial vertical cylinders, Rayleigh-Benard convection in a vertical
cylinder, cylindrical lid-driven cavity ﬂow, mixed convection in a tall vertical
annulus and melt ﬂow during Czochralski crystal growth in a vertical rotating
cylinder.
This paper is organized as follows. In the next section (Sec. 2), cascaded LB
methods for axisymmetric thermal ﬂows with swirl eﬀects using a symmetric
operator split formulation for the various geometric sources and forces are pre-
sented. Numerical results for various benchmark problems are presented and
discussed in Sec.3. Finally, the paper concludes with a summary in Sec.4.
6


## Page 7


2. Cascaded LB Methods for Axisymmetric Thermal Convective Flows
with Swirling Eﬀects: Symmetric Operator Splitting Formulation
We will now present cascaded LB methods based on central moments and
MRT for the computation of thermal convective ﬂows in the cylindrical co-
ordinates with axial symmetry, by also taking into account azimuthal rota-
tional/swirling eﬀects.
A triple distribution functions based LB approach is
considered, where the geometric source terms arising in the pseudo-2D macro-
scopic equations are represented using symmetric operator splitting around the
cascaded collision steps [45]. The solution of the resulting cascaded LB mod-
els then yields the local ﬂuid ﬂow variables such as the radial axial and az-
imuthal velocity ﬁelds, pressure (or density) ﬁeld, and the temperature ﬁeld in
the meridian plane. First, we summarize the macroscopic governing equations
for axisymmetric thermal ﬂows subjected to rotation/swirl.
2.1. Governing equations for thermal ﬂows in cylindrical coordinates with axial
symmetry
For incompressible, axisymmetric thermal ﬂows subjected to rotational/swirling
eﬀects, the macroscopic governing equations in the cylindrical coordinate system
(r, θ, z) can be written as [19, 26]
∂tρ + ∂r(ρur) + ∂z(ρuz) = −ρur
r ,
(1a)
∂t(ρur) + ∂r(ρu2
r) + ∂z(ρuruz) = −∂rp + ∂r(2µ∂rur) + ∂z[µ(∂zur + ∂ruz)](1b)
+ρu2
θ
r −ρu2
r
r + 2µ∂rur
r
−2µur
r2 + F b
r ,
∂t(ρuz) + ∂r(ρuruz) + ∂z(ρu2
z) = −∂zp + ∂r[µ(∂ruz + ∂zur)] + ∂z(2µ∂zuz)(1c)
−ρuruz
r
+ µ(∂zur + ∂ruz)
r
+ F b
z ,
∂t(ρuθ) + ∂r(ρuruθ) + ∂z(ρuzuθ) = ν
 ∂2
∂r2 (ρuθ) + ∂2
∂z2 (ρuθ)

−2ρuruθ
r (1d)
+ρν
r ∂ruθ −ρνuθ
r2 ,
∂tφ + ∂r(urφ) + ∂z(uzφ) = ∂r(Dφ∂rφ) + ∂z(Dφ∂zφ) −urφ
r
+ Dφ
r ∂rφ. (1e)
7


## Page 8


Here, r, z and θ represent the coordinates in the radial, axial and azimuthal
directions, respectively; accordingly, ur, uz and uθ denote the ﬂuid velocity
components in the respective directions, and F b
r and F b
z are radial and axial
components of the external body forces, respectively. ρ and p represent the
density and pressure, respectively, while ν and µ = ρν correspond to the kine-
matic and dynamic viscosities of the ﬂuid, respectively. φ is the passive scalar
variable, which is the temperature ﬁeld T in the present study (i.e. φ = T)
and Dφ is the coeﬃcient of diﬀusivity. Equations (1a)-(1c) represent the ax-
isymmetric NS equations for the axial and radial components of the velocity
ﬁeld in the meridian plane. The structure of the evolution equations for the
azimuthal momentum (ρuθ) and the scalar ﬁeld (φ) given in Eqs. (1d) and (1e)
respectively, is similar in form, viz., advection-diﬀusion equation with a source,
and hence they can be solved using the same numerical procedures.
In order to represent the above macroscopic equations in cylindrical coor-
dinates in a set of pseudo-2D Cartesian forms, we apply the following coordi-
nate/variable transformations:
(r, z) 7−→(y, x),
(ur, uz) 7−→(uy, ux),
ρuθ 7−→ψ.
(2)
Then, the resulting equations in pseudo-Cartesian forms involve additional terms
when compared to the standard ﬂow and thermal transport equations in 2D,
which can be regarded as geometric source terms. The latter will be introduced
via a symmetric operator splitting technique in the respective cascaded LB for-
mulation in the following. Thus, the mass and momentum equations for the
ﬂuid motion in the meridian plane (Eqs.(1a)-(1c)) can be written in pseudo-2D
8


## Page 9


Cartesian forms as
∂tρ + ∂y(ρuy) + ∂x(ρux) =M A
,
(3a)
∂t(ρux) + ∂r(ρu2
x) + ∂y(ρuxuy) = −∂xp + ∂x[2µ∂xux] + ∂y[µ(∂yux + ∂xuy)]
+ F A
x + F b
x,
(3b)
∂t(ρuy) + ∂x(ρuxuy) + ∂y(ρu2
y) = −∂yp + ∂x[µ(∂xuy + ∂yux)] + ∂y[2µ∂yuy]
+ F A
y + F b
y,
(3c)
where the geometric mass source M A and the momentum source vector F A =
(F A
x , F A
y ) can be represented as
M A = −ρuy
y ,
(4a)
F A
x = −ρuxuy
y
+ µ(∂xuy + ∂yux)
y
,
(4b)
F A
y = ψ2
ρy −ρu2
y
y + 2µ∂yuy
y
−2µuy
y2 .
(4c)
Then, the total force F = (Fx, Fy) in this approach becomes
Fx = F A
x + F b
x,
Fy = F A
y + F b
y.
(5)
Here, the body force F b = (F b
x, F b
y) could be a volumetric force such as the buoy-
ancy force or the Lorentz force. Similarly, the azimuthal momentum equation
for ψ = ρuθ can be written as
∂tψ + ∂x(uxψ) + ∂y(uyψ) = Dψ(∂2
xψ + ∂2
yψ) + Sψ,
(6)
where the corresponding geometric source term Sψ can be expressed as
Sψ = −2uyψ
y
+ µ
y ∂y(ψ
ρ ) −νψ
y2 ,
(7)
and Dψ is the coeﬃcient of diﬀusivity, which is equal to the kinematic viscosity
of the ﬂuid ν, i.e. Dψ = ν. Finally, the axisymmetric advection-diﬀusion equa-
tion for the scalar, i.e., temperature ﬁeld (φ = T) in the pseudo-2D cartesian
coordinate system reads as
∂tφ + ∂x(uxφ) + ∂y(uyφ) = ∂x(Dφ∂xφ) + ∂y(Dφ∂yφ) + Sφ,
(8)
9


## Page 10


where the source term Sφ is given as
Sφ = −uyφ
y
+ Dφ
y ∂yφ.
(9)
Our goal, then, is to represent the evolution of the axial and radial momentum
components along with density (Eqs.(3)-(5)) using a distribution function fα,
azimuthal momentum (Eqs.(6)-(7)) using another distribution function gα, and
the scalar temperature ﬁeld (Eqs.(8)-(9)) using a third distribution function
hα. We use a D2Q9 lattice for fα, while for both gα and hα, a D2Q5 lattice
would suﬃce since to represent advection-diﬀusion type equations, the lattice
is required to satisfy only a lower degree of symmetry than the lattice used for
the Navier-Stokes equations. In each case, a cascaded LB scheme based on a
symmetric operator splitting will be constructed in the following.
2.2. Cascaded LB scheme for axial and radial velocity ﬁelds: operator splitting
for mass and momentum source terms
In order to consistently include the geometric mass and momentum sources
along with any external body force given in Eqs.(4) and (5) in a cascaded LB
scheme, we will employ s symmetric operator splitting strategy around its colli-
sion term [45]. First, we deﬁne the following components of the particle velocities
for the D2Q9 lattice:
|ex⟩= (0, 1, 0, −1, 0, 1, −1, −1, 1)† ,
(10a)
|ey⟩= (0, 0, 1, 0, −1, 1, 1, −1, −1)† ,
(10b)
where † is the transpose operator and their components for any particle direction
α are denoted by eαx and eαy, where α = 0, 1, · · · 8. We also need the following
9-dimensional vector
|1⟩= (1, 1, 1, 1, 1, 1, 1, 1, 1)†
(11)
whose inner product with the distribution function fα deﬁnes its zeroth moment.
Here, and in the following, we have used the standard Dirac’s bra-ket notation
10


## Page 11


to represent the vectors. The corresponding nine orthogonal basis vectors may
be represented by (e.g. [36]):
K0 = |1⟩,
K1 = |ex⟩,
K2 = |ey⟩, K3 = 3 |e2
x + e2
y⟩−4 |1⟩,
K4 = |e2
x −e2
y⟩,
K5 = |exey⟩,
K6 = −3 |e2
xey⟩+ 2 |ey⟩,
K7 = −3 |exe2
y⟩+ 2 |ex⟩,
K8 = 9 |e2
xe2
y⟩−6 |e2
x + e2
y⟩+ 4 |1⟩.
(12)
Here and henceforth, symbols such as |e2
xey⟩= |exexey⟩denote a vector that
result from the element wise vector multiplication of vectors |ex⟩, |ex⟩and |ey⟩.
The above set of vectors can be organized by the following orthogonal matrix
K = [K0, K1, K2, K3, K4, K5, K6, K7, K8] ,
(13)
which maps changes of moments under collisions due to a cascaded central
moment relaxation back to changes in the distribution function (see below). As
the cascaded collision operator is built on the moment space, we ﬁrst deﬁne the
central moments and raw moments of order (m+n) of the distribution function
fα and its equilibrium f eq
α as

ˆκxmyn
ˆκeq
xmyn

=
X
α

fα
f eq
α

(eαx −ux)m(eαy −uy)n,
(14)
and

ˆκ
′
xmyn
ˆκeq′
xmyn

=
X
α

fα
f eq
α

em
αxen
αy,
(15)
respectively. Here and in what follows, the prime (′) symbols denote various
raw moments. The central moments of the equilibrium are constructed to be
equal to those for the Maxwellian, which then serve as attractors during the
cascaded collision represented as a relaxation process [34].
In the following,
an operator splitting based cascaded LB scheme will be constructed to solve
Eqs.(3)-(5). First, we represent the solution of the mass and momentum equa-
tions in the meridian plane (Eq.(3)) without the respective source terms (i.e.
MA, F A
x , F b
x, F A
y , F b
y) by means of the evolution of the distribution function fα
11


## Page 12


using the usual collision and streaming steps (C and S, respectively) as
Step C :
f p
α = fα + (K · bp)α,
(16a)
Step S :
fα(x, t) = f p
α(x −eα∆t, t),
(16b)
where eα = (eαx, eαy), ∆t is the time step, f p
α is the post-collision distribution
function at a location x and time t. bp = (bp0, bp1, bp2 . . . bp8) denotes the changes
of diﬀerent moments under collision based on the relaxation of central moments
to their equilibria in a cascaded fashion [34]. With the mass and momentum
being conserved during collision bp0 = bp1 = bp2 = 0, and the changes in the higher
order non-conserved moments are given by ([34, 35, 36])
bp3 = ω3
12
n
2c2
sρ + ρ(u2
x + u2
y) −(bκ
′
xx + bκ
′
yy)
o
,
bp4 = ω4
4
n
ρ(u2
x −u2
y) −(bκ
′
xx −bκ
′
yy)
o
,
bp5 = ω5
4
n
ρuxuy −bκ
′
xy
o
,
bp6 = ω6
4
n
2ρu2
xuy + bκ
′
xxy −2uxbκ
′
xy −uybκ
′
xx
o
−1
2uy(3bp3 + bp4) −2uxbp5,
bp7 = ω7
4
n
2ρuxu2
y + bκ
′
xyy −2uybκ
′
xy −uxbκ
′
yy
o
−1
2ux(3bp3 −bp4) −2uybp5,
bp8 = ω8
4
n
c4
sρ + 3ρu2
xu2
y −
h
bκ
′
xxyy −2uxbκ
′
xyy −2uybκ
′
xxy + u2
xbκ
′
yy + u2
ybκ
′
xx
+4uxuybκ
′
xy
io
−2bp3 −1
2u2
y(3bp3 + bp4) −1
2u2
x(3bp3 −bp4)
−4uxuybp5 −2uybp6 −2uxbp7.
(17)
Here, ω3, ω4. · · · ω8 are relaxation parameters, where ω3, ω4 and ω5 are related to
the bulk and shear viscosities and the other ωi inﬂuence the numerical stability
of the method. In particular, the bulk viscosity is given by ξ = c2
s( 1
ω3 −1
2)∆t and
the shear viscosity by ν = c2
s( 1
ωj −1
2)/∆t, where j = 4, 5, and c2
s = c2/3, where
c = ∆x/∆t. In this work, we consider the lattice units, where ∆x = ∆t = 1
and hence the speed of sound cs = 1/
√
3, and the higher order relaxation
parameters ω6, ω7 and ω8 are set to unity for simplicity. After the streaming
step (see Eq.(16b)), the output density ﬁeld and the velocity ﬁeld components
(designated with a superscript ”o”) as the zeroth and ﬁrst moments of fα ,
12


## Page 13


respectively:
ρo = P8
α=0 fα,
ρouo
x = P8
α=0 fαeαx,
ρouo
y = P8
α=0 fαeαy
(18)
We then introduce the inﬂuence of the mass source MA in Eq. (3a) and the
momentum sources F A
x = F A
x + F b
x and Fy = F A
y + F b
y in Eqs. (3b) and (3c),
respectively, as the solution of the following two sub problems, referred to as
the mass source step M and momentum source step F, respectively:
Step M : ∂tρ = M A,
(19a)
Step F : ∂t(ρu) = F = F A + F b,
(19b)
where u = (ux, uy) and FA = (F A
x , F b
y) etc.
In our previous work [45], we
constructed a symmetric operator splitting based approach to incorporate a
single momentum source in a cascaded LB method. In the present work, we
further extend this approach to symmetric splitting of multiple operators related
to mass and momentum sources. In other words, we perform two symmetric
steps of half time steps of length ∆t/2 of M and F, one before and the other after
the collision step. The overall symmetrized operator splitting based cascaded
LB algorithm implementing all the four operators (C, S, M and F) during the
time interval [t, t + ∆t] may be written as
fα(x, t + ∆t) = M1/2 F1/2 C F1/2 M1/2 S fα(x, t),
(20)
where M1/2 and F1/2 represent solving Eqs. (19a) and (19b), respectively, over
time step ∆t/2. Both of these steps introduce the eﬀect of geometric mass and
momentum source and the body forces directly in the momentum space.
Solving Eqs. (19a) and (19b) for the ﬁrst part of symmetric sequence needed
in Eq.(20) yields ρ −ρo = M A ∆t
2 , ρux −ρuo
x = Fx ∆t
2 and ρuy −ρuo
y = Fy ∆t
2 .
Thus, we have
Pre-collision Mass Source Step M1/2 :
ρ = ρo + M A ∆t
2
(21a)
Pre-collision Momentum Source Step F1/2 :
ρux = ρuo
x + Fx
∆t
2 , (21b)
ρuy = ρuo
y + Fy
∆t
2 , (21c)
13


## Page 14


where M A, Fx and Fy are given in Eqs. (4a)-(4c) and (5). Based on Eq. (20),
the next step is the collision step, which is performed using the updated density
and velocity ﬁelds (ρ, ux, uy) given in Eqs. (21a)-(21c) and then determining
the change of moments under collision bpβ (β = 3, 4 . . . 8) using Eq. (17). Then,
implementing the other part of the symmetrized mass and momentum steps
with using a half time step to solve Eqs. (19a) and (19b), we obtain the target
density and velocity ﬁeld after collision represented as (ρp, up
x, up
y) via ρp −ρ =
M A ∆t
2 , ρup
x −ρux = Fx ∆t
2 and ρup
y −ρuy = Fy ∆t
2 . Thus, we have
Post-collision Momentum Source Step F1/2 :ρup
x = ρux + Fx
∆t
2
up
y = ρuy + Fy
∆t
2 ,
(22a)
Post-collision Mass Source Step M1/2 : ρp = ρ + M A ∆t
2 ,
(22b)
By rewriting the above results for the post-collision source steps in terms of the
output density ρo and velocity ﬁeld uo = (uo
x, uo
y) via Eqs. (21a)-(21c), we get
ρp = ρo + M A∆t,
ρup
x = ρuo
x + Fx∆t,
ρup
y = ρuo
y + Fy∆t.
(23)
To eﬀectively design the post-collision distribution function f p
α in the cascaded
LB scheme so that Eq.(23) is precisely satisﬁed, we consider f p
α = fα + (K · bp)α
and taking its zeroth and ﬁrst moments, we obtain
ρp = Σαf p
α = Σαfα + Σβ⟨Kβ|1⟩bpβ,
(24a)
ρup
x = Σαf p
αeαx = Σαfαeαx + Σβ⟨Kβ|ex⟩bpβ,
(24b)
ρup
y = Σαf p
αeαy = Σαfαeαy + Σβ⟨Kβ|ey⟩bpβ.
(24c)
Since the orthogonal basis vectors |Kβ⟩given in Eq. (12) satisfy Σβ⟨Kβ|1⟩=
9bp0, Σβ⟨Kβ|ex⟩= 6bp1, Σβ⟨Kβ|ey⟩= 6bp2, Eqs. (24a)-(24c) become
ρp = ρo + 9bp0,
ρup
x = ρuo
x + 6bp1,
ρup
y = ρuo
y + 6bp2.
(25)
Comparing Eqs.(23) and (25), it follows that the change of the zeroth moment
(bp0) and the ﬁrst moments (bp1 and bp2) due to mass and momentum source can
be written as
bp0 = M A
9 ∆t,
bp1 = Fx
6 ∆t,
bp2 = Fy
6 ∆t.
(26)
14


## Page 15


where MA follows from Eq. (4a), Fx and Fy are given in Eq. (5) and (4b)-
(4c). These expressions eﬀectively provide the desired post-collision states of
the distribution function, i.e. f p
α due to mass and momentum sources. Thus,
ﬁnally expanding (K · bp)α in Eq. (16a), the components of the post-collision
distribution functions read as
f p
0
=
f0 + [bp0 −4(bp3 −bp8)] ,
f p
1
=
f1 + [bp0 + bp1 −bp3 + bp4 + 2(bp7 −bp8)] ,
f p
2
=
f2 + [bp0 + bp2 −bp3 −bp4 + 2(bp6 −bp8)] ,
f p
3
=
f3 + [bp0 −bp1 −bp3 + bp4 −2(bp7 + bp8)] ,
f p
4
=
f4 + [bp0 −bp2 −bp3 −bp4 −2(bp6 + bp8)] ,
f p
5
=
f5 + [bp0 + bp1 + bp2 + 2bp3 + bp5 −bp6 −bp7 + bp8] ,
f p
6
=
f6 + [bp0 −bp1 + bp2 + 2bp3 −bp5 −bp6 + bp7 + bp8] ,
f p
7
=
f7 + [bp0 −bp1 −bp2 + 2bp3 + bp5 + bp6 + bp7 + bp8] ,
f p
8
=
f8 + [bp0 + bp1 −bp2 + 2bp3 −bp5 + bp6 −bp7 + bp8] .
(27)
where bp0, bp1 and bp2 are obtained from Eq. (26) and bp3, bp4, · · · , bp8 from Eq. (17)
2.3. Cascaded LB scheme for azimuthal velocity ﬁeld: operator splitting for
source term
We now construct a novel cascaded LB scheme for the solution of the equa-
tion of the azimuthal momentum component (ψ = ρuθ) given in Eqs. (6) and (7)
using a D2Q5 lattice [45]. First, deﬁning the vectors corresponding to particle
velocity components and a 5-dimensional vector |1⟩as
|ex⟩= (0, 1, 0, −1, 0)† ,
(28a)
|ey⟩= (0, 0, 1, 0, −1)† ,
(28b)
|1⟩= (1, 1, 1, 1, 1)† ,
(28c)
where taking the inner product of the distribution function gα with |1⟩deﬁnes
its zeroth moment. Using these, the ﬁve orthogonal basis vectors can be written
15


## Page 16


as
L0 = |1⟩, L1 = |ex⟩, L2 = |ey⟩,
L3 = 5 |e2
x + e2
y⟩−4 |1⟩, L4 = |e2
x −e2
y⟩,
(29)
which can be grouped together as the following transformation matrix that
converts the changes in moments to those in the distribution functions:
L = [L0, L1, L2, L3, L4] .
(30)
In order to design a cascaded collision operator to solve for the azimuthal mo-
mentum, which acts as a passive scalar ﬁeld ψ = ρuθ described by on advection-
diﬀusion equation under the action of a local source term (Eqs. (6) and (7)),
we deﬁne the following central moments and raw moments of the distribution
function gα and its equilibrium geq
α as

ˆκψ
xmyn
ˆκeq,ψ
xmyn

=
X
α

gα
geq
α

(eαx −ux)m(eαy −uy)n,
(31)
and

ˆκψ′
xmyn
ˆκeq,ψ′
xmyn

=
X
α

gα
geq
α

em
αxen
αy.
(32)
respectively. The central moments of the equilibrium ˆκeq,ψ
xmyn are devised be equal
to those for the Maxwellian after replacing the density with the scalar ﬁeld in its
expression. Then the cascaded collision step is written in terms of relaxation of
diﬀerent central moments to their equilibria. Similar to the previous section, a
symmetrized operator split scheme will now be developed to solve Eqs. (6) and
(7) in the cascaded LB formulation. First, we represent the solution of Eq. (6)
without the source term (Eq. (7)) through the collision and streaming steps of
the distribution function gα as
Step C :
gp
α = gα + (L · bq)α,
(33a)
Step S :
gα(x, t) = gp
α(x −eα∆t, t).
(33b)
16


## Page 17


where gp
α is the post-collision distribution function and bq = (bqo, bq1, · · · bq4) rep-
resents the changes of diﬀerent moments under a cascaded collision prescribed
as a relaxation process in terms of central moments, which reads as [45]
bq1
=
ωψ
1
2
h
ψux −bκψ′
x
i
,
bq2
=
ωψ
2
2
h
ψuy −bκψ′
y
i
,
bq3
=
ωψ
3
4
h
2c2
sψ −(bκψ′
xx + bκψ′
yy) + 2(uxbκψ′
x + uybκψ′
y ) + (u2
x + u2
y)ψ
i
+ uxbq1 + uybq2,
bq4
=
ωψ
4
4
h
−(bκψ′
xx −bκ
′ψ
yy) + 2(uxbκψ′
x −uybκψ′
y ) + (u2
x −u2
y)ψ
i
+ uxbq1 −uybq2, (34)
where ωψ
1 , ωψ
2 , ωψ
3 and ωψ
4 are the relaxation parameters. Since ψ is conserved
during collision, bqo = 0. The relaxation parameters for the ﬁrst order moments
(ωψ
1 and ωψ
2 ) are related to diﬀusivity Dψ = ν = c2
sψ( 1
ωψ
j −1
2)∆t, j=1,2 where
c2
sψ is a free parameter, which is set to 1/3.
The relaxation parameters for
the higher order moments, which inﬂuence numerical stability, are taken to be
unity in this study. After the streaming step in Eq.(33b), the output passive
azimuthal momentum ﬁeld ψo is computed as the zeroth moment of gα as
ψo =
4
X
α
gα.
(35)
The source term Sψ, which was eliminated in the above, will now be intro-
duced by appropriately combining its eﬀect after solution of the following such
problem:
Step R :
∂tψ = Sψ
(36)
Its solution will now be combined with the split solution obtained in the absence
of the source term in Eqs.(33a) and (33b) via a symmetric operator splitting
technique over a time interval [t, t + ∆t], analogous to that considered in the
previous subsection. This can be represented as
gα(x, t + ∆t) = S R1/2 C R1/2gα(x, t),
(37)
The pre-collision source step R1/2 is executed via a solution of Eq.(36) over a
17


## Page 18


duration ∆t/2, which yields ψ −ψo = Sφ ∆t
2 , and hence
Pre-collision Source Step R1/2 : ψ = ψo + Sψ ∆t
2
(38)
Based on this updated scalar ﬁeld, the changes of diﬀerent moments under
collision bqβ, β = 1, 2, 3, 4, given in Eq.(34) can be computed.
Similarly, the
other part of the source step R1/2 with half time step following collision can be
performed by solving Eq.(36), which can be expressed as
Post-collision Source Step R1/2 : ψp = ψ + Sψ ∆t
2
(39)
where ψp is the target scalar ﬁeld after collision. By rewriting it in terms of the
output scalar ﬁeld ψo using Eq. (38), we have
ψp = ψo + Sψ∆t.
(40)
In order for the post-collision distribution function gp
α = gα + (L · bq)α to satisfy
Eq. (40), we write its zeroth moment as
ψp = Σαgp
α = Σαgα + Σβ⟨Lβ|1⟩bqβ.
(41)
Since Σβ ⟨Lβ|1⟩qβ = 5bqo via orthogonal of basis vectors (see Eq.(29)), it follows
from Eqs.(35) and (41) that ψp = ψo + 5bq0. Comparing this with Eq.(40), we
get the change of the zeroth moment bqo due to the presence of the source term
Sψ as
bq0 = Sψ
5 ∆t.
(42)
Finally, the components of the post-collision distribution function in Eq.(33a)
can be expressed after expanding (L · bq)α as
gp
0
=
g0 + [bq0 −4bq3] ,
gp
1
=
g1 + [bq0 + bq1 + bq3 + bq4] ,
gp
2
=
g2 + [bq0 + bq2 + bq3 −bq4] ,
gp
3
=
g3 + [bq0 −bq1 + bq3 + bq4] ,
gp
4
=
g4 + [bq0 −bq2 + bq3 −bq4] ,
(43)
18


## Page 19


where bqo (i.e., the change of the zeroth moment due to source) is given in Eq. (42)
and bqβ, β = 1, 2, 3, 4 (i.e., the changes of the higher, non-conserved, moments
under collision) is obtained from Eq. (34).
2.4. Cascaded LB scheme for temperature ﬁeld: operator splitting for source
term
As in the previous section, we consider a D2Q5 lattice, and use the orthogo-
nal basis vectors Lβ and the transformation matrix L given in Eqs. (29) and (30),
respectively, to design a cascaded LB scheme for the solution of the temperature
ﬁeld φ = T. Its evolution is presented by the advection-diﬀusion equation with
a source term given in Eqs. (8) and (9). The various central moments and raw
moments of the corresponding distribution function hα and its equilibrium heq
α
are deﬁned as

ˆκφ
xmyn
ˆκeq,φ
xmyn

=
X
α

hα
heq
α

(eαx −ux)m(eαy −uy)n,
(44)
and

ˆκφ′
xmyn
ˆκeq,φ′
xmyn

=
X
α

hα
heq
α

em
αxen
αy.
(45)
As before, we use the symmetrized operator splitting to include the source term
Sφ in the cascaded LB scheme, which can be presented as :
hα(x, t + ∆t) = S R1/2 C R1/2hα(x, t),
(46)
where C and S denote the collision and streaming steps, respectively, of gα used
to solve Eq. (8) (without Sφ)
Step C: hp
α
=
hα + (L · br)α,
(47a)
Step S: hα(x, t)
=
hp
α(x −eα∆t, t).
(47b)
Here, hp
α is the post-collision distribution function and br = (bro, br1, br2, br3, br4) is
the change of diﬀerent moments under collision, with bro = 0 due to φ being a
19


## Page 20


collision invariant. In the above, after the streaming step, the solution of the
output scalar ﬁeld φo is computed via the zeroth moment of hα as
φo =
4
X
α=0
hα.
(48)
The operator R1/2 applied twice in Eq.(46) represents the split solution of the
scalar ﬁeld due to the source term of the evolution equation ∂tφ = Sφ before
and after collision over a half time step ∆t/2. Thus, the pre-collision source
step can be expressed as
Pre-collision Source Step R1/2 : φ = φo + Sφ
2 ∆t.
(49)
This updated scalar ﬁeld φ is then used to compute the changes of diﬀerent
moments under collision brβ, β = 1, 2, 3, 4, which can be written as
br1
=
ωφ
1
2
h
φux −bκφ′
x
i
,
br2
=
ωφ
2
2
h
φuy −bκφ′
y
i
,
br3
=
ωφ
3
4
h
2c2
sφ −(bκφ′
xx + bκφ′
yy) + 2(uxbκφ′
x + uybκφ′
y ) + (u2
x + u2
y)φ
i
+ uxbr1 + uybr2,
br4
=
ωφ
4
4
h
−(bκφ′
xx −bκ
′φ
yy) + 2(uxbκφ′
x −uybκφ′
y ) + (u2
x −u2
y)φ
i
+ uxbr1 −uybr2,
(50)
where the relaxation parameters ωφ
1 and ωφ
2 are related to the thermal diﬀusivity
Dφ via Dφ = c2
sφ( 1
ωφ
j −1
2)∆t, j = 1, 2, where c2
sφ = 1
3 and ωφ
3 = ωφ
4 = 1 in this
work. Following this, the post-collision source step R1/2 can be represented as
Post-collision Source Step R1/2 : φp = φ + Sφ
2 ∆t
(51)
where φp is the target scalar ﬁeld following collision, which via Eq.(49) reads as
φp = φo + Sφ∆t. The post-collision distribution function hp
α = hα + (L ·br)α can
be made to satisfy this condition using Eq. (48) and using Σβ ⟨Lβ|1⟩brβ = 5br0
after taking its zeroth moment, i.e. φp = P
α hp
α. This provides the following
zeroth moment change due to Sφ after collision
br0 = Sφ
5 ∆t.
(52)
20


## Page 21


Finally, the post-collision distribution function hp
α can be explicitly written after
expanding (L · br)α in Eq.(47a) as follows:
hp
0
=
h0 + [br0 −4br3] ,
hp
1
=
h1 + [br0 + br1 + br3 + br4] ,
hp
2
=
h2 + [br0 + br2 + br3 −br4] ,
hp
3
=
h3 + [br0 −br1 + br3 + br4] ,
hp
4
=
h4 + [br0 −br2 + br3 −br4] ,
(53)
where bro is obtained form Eq. (52) and brβ, β = 1, 2, 3 and 4, follows from
Eq. (50) due to various non-conserved moment changes under collision.
3. Results and Discussion
In this section, the cascaded LB schemes described above will be applied to
and studied for diﬀerent complex ﬂow benchmark problems to validate them
for simulations of axisymmetric ﬂows with heat transfer and including rota-
tional/swirling eﬀects.
These include the following: (a) Taylor-Couette ﬂow
between two rotating circular cylinders, (b) natural convection in an annulus
between two stationary coaxial vertical cylinders, (c) Rayleigh-Benard convec-
tion inside vertical cylinder heated at the bottom and cooled at the top, (d)
cylindrical cavity ﬂow driven by the motion of the top lid, (e) mixed convection
in a slender vertical annulus subjected to the inner cylinder rotation, and (f)
melt ﬂow in a cylinder during Czochralski crystal growth process.
3.1. Taylor-Couette ﬂow
As the ﬁrst test problem, the classical shear-driven circular Couette ﬂow
between two circular cylinders is considered [46]. This problem is used to as-
sess the cascaded LB scheme for the azimuthal velocity component uθ given in
Sec. 2.3, whose evolution is represented by Eqs. (6) and (7). The radii of the
inner and outer cylinders are deﬁned as Ri and Ro, respectively. Let the angu-
lar velocities of the inner and outer cylinders be Ωi and Ωo, respectively, which
21


## Page 22


induce an azimuthal ﬂow within their annulus gap. The analytical solution for
such a cylindrical Couette ﬂow is given in terms of the radial variation of the
azimuthal velocity as follows:
uθ(r) = Ar + B
r ,
where A = ΩoR2
o−ΩiR2
i
R2o−R2
i
, B = (Ωi−Ωo)R2
i R2
o
R2o−R2
i
. Here, r is the radial distance from
the cylindrical axis. For ease of representation, this can be written in a non-
dimensional form as
uθ(r)
uo
=
1
1 −β2 [(κ −β2) r
Ri
+ Ri
r (1 −κ)],
where uo = ΩiRi, β is the radius ratio given by β = Ri/Ro and κ denotes the
angular velocity ratio, i.e., κ = Ωo/Ωi.
In our simulation, periodic boundary conditions are applied in the axial di-
rection and the values of the azimuthal velocities at the inner and outer cylinder
are prescribed as uθ(r = Ri) = ΩiRi = uo and uθ(r = Ro) = ΩoRo = κ
β uo,
respectively using the Dirichlet boundary condition implementation scheme as-
sociated with the advection-diﬀusion equation representing the dynamics of
uθ [47].
The outer cylinder radius is resolved by 200 lattice nodes and the
lattice location for the inner cylinder ﬁxed using Ri = βRo for diﬀerent choices
of β.
The periodic axial direction is discretized using 3 lattice nodes.
The
relaxation times in the cascaded LB scheme representing the kinematic shear
viscosity are set as ωj = 1/τ, j = 4, 5, where τ = 0.6, and uo is chosen such that
the rotational Reynolds number Re = uoRi/ν becomes 5. Figure 1 presents
a comparison of the velocity proﬁles computed using the cascaded LB scheme
against the analytical solution at the angular velocity ratio κ = 0.1 for various
values of the radius ratio β (β = 0.103, 0.203, 0.303 and 0.503). It is clear that
the agreement between the numerical and analytical solution is very good.
3.2. Natural convection in an annulus between two coaxial vertical cylinders
In order to validate our cascaded LB schemes for axisymmetric ﬂows with
heat transfer, we simulate a buoyancy-driven ﬂow between two coaxial station-
ary cylinders, which is a prototype problem of both fundamental and practical
22


## Page 23


Figure 1: Comparison between the analytical velocity proﬁle (solid lines) and the cascaded LB
solution (symbols) for the Taylor-Couette ﬂow between two circular cylinders at an angular
velocity ratio κ = 0.1 and for various values of the radius ratio β.
23


## Page 24


interest. Since the ﬂow ﬁeld is coupled to the temperature ﬁeld via the buoyancy
force in view of Eqs. (3a)-(3c), (4a)-(4c), (5), (8) and (9), this problem facilitates
a thorough examination of the eﬃcacy of the coupling between the cascaded LB
schemes presented in Sec. 2.2 and 2.4. The schematic of this problem is depicted
in Fig .2, where Ri, Ro, H and g are the radii of the inner cylinder and outer
cylinder, the height of the cylinder and the gravitation acceleration, respectively.
Figure 2: Schematic illustration of the geometry and boundary conditions for natural convec-
tion in a vertical annulus.
For the velocity ﬁeld, no-slip boundary conditions are considered on all four
walls involving the inner and outer cylindrical surfaces, and top and bottom
walls. The inner and outer walls of the lateral cylindrical side walls are main-
tained at temperatures of TH and TL, respectively, where TH > TL, while the
top and bottom walls are considered to be thermally insulated (adiabatic). As a
result, this generates a body force due to buoyancy in the axial direction, which
under the Boussinesq approximation, can be written as gβ(T −To), where β is
the thermal expansion coeﬃcient, and To = (TH + TL)/2. This body force com-
ponent is added to the geometric source terms in Eq. (5) for F b
x, which then sets
up natural convection within the annulus of the axisymmetric geometry. This
thermally driven ﬂow problem is characterized by two dimensionless numbers,
24


## Page 25


viz., the Rayleigh number Ra and Prandtl number Pr deﬁned as
Ra = gβ(TH −TL)L3
αν
, Pr = ν
α,
where L = Ro −Ri is the annual gap serving as the characteristic length,
and ν and α are the kinematic viscosity and thermal diﬀusivity, respectively. In
addition, the geometric parameters inﬂuencing this problem are the aspect ratio
H/L and the radius ratio Ro/Ri, both of which are set to 2 in the present study.
The no-slip conditions for the velocity ﬁeld are implemented using the standard
half-way bounce back scheme in the cascaded LB method, while the imposed
temperature and no heat ﬂux conditions on the boundaries are represented
using the approach presented in [47]. All the spatial derivatives needed in the
source terms in Eqs.(4b), (4c) and (9) are computed using a central diﬀerence
scheme, and the computational domain is resolved using a grid resolution of
200 × 200 in the axial and radial directions, respectively. The characteristic
velocity due to natural convection
p
gβ(TH −TL)Ri is kept small so that the
ﬂow can be regarded as incompressible. We performed simulations at Pr = 0.7
and Ra = 103, 104 and 105. Figure 3 presents the computed streamlines and
isotherms for three diﬀerent Ra = 103, 104 and 105.
It is clear that as Ra increases, the vortical patterns turn to be progressively
more complex, with the Ra = 105 case generating additional pairs of vortices
around the middle of the annulus. Furthermore, as Ra increase, the isotherms
are greatly distorted, and the velocity and thermal boundary layers become
thinner near the hot and cold lateral walls signifying the strengthened convection
mode of heat transfer. It may be noted that all these observations are consistent
with prior studies based on other numerical methods (e.g., [48, 49, 28]). Then
in order to quantify the rates of heat transfer on the lateral walls, the overall
Nusselt numbers Nui and Nuo on the inner and outer cylinders can be deﬁned
as
Nui =
−Ri
H(TH −TL)
Z H
o
(∂yTi)dx, Nuo =
−Ro
H(TH −TL)
Z H
o
(∂yTo)dx,
and hence the average Nusselt number Nu = (Nui + Nuo)/2. Table 1 shows
25


## Page 26


r
z
100
150
200
0
50
100
150
200
(a) Re=103
r
z
100
150
200
0
50
100
150
200
(b) Re=104
r
z
100
150
200
0
50
100
1
(c) Re=105
(d) Re=103
r
z
100
150
200
0
50
100
150
200
(e) Re=104
r
z
100
150
200
0
50
100
150
200
(f) Re=105
Figure 3: streamlines and isotherms for the natural convection between two co-axial vertical
cylinders at Pr = 0.7 and (a,d) Ra = 103, (b,e) Ra = 104 and (c,f) Ra = 105 computed using
cascaded LB schemes. Top row presents streamlines and the bottom row the isotherms.
26


## Page 27


a comparison of the average Nusselt number computed using the cascaded LB
scheme for Ra = 103, 104, and105 against prior numerical benchmark results [48,
49, 28]. It can be seen that our predictions for the average Nusselt numbers agree
well with those obtained by other methods.
Table 1: Comparison of the average Nusselt number Nu for diﬀerent Ra for natural convec-
tion in a cylindrical annulus computed using axisymmetric cascaded LB schemes with other
reference numerical solutions.
Ra
Cascaded LB schemes
Ref. [48]
Ref. [49]
Ref. [28]
103
1.688
-
-
1.692
104
3.211
3.037
3.163
3.215
105
5.781
5.760
5.882
5.798
3.3. Rayleigh-Benard convection in a circular vertical cylinder
We now demonstrate the ability of our axisymmetric cascaded LB schemes
to simulate Rayleigh-Benard convective in a vertical cylinder, which is classical
thermally-driven ﬂow and has been well studied experimentally and using con-
ventional numerical methods (e.g. [50, 5]). Here, the ﬂuid is heated from below,
where the bottom wall is at temperature TH while the top wall is kept at a
lower temperature TL and lateral wall of a cylinder of radius R and height H is
maintained to be adiabatic (see Fig. 4). As a result of the buoyancy force gen-
erated, this sets up natural convection currents, whose dynamics is governed by
the Rayleigh number Ra = gβ(TH −TL)H3/(αν), Prandtl number, Pr = ν/α
and the cylinder aspect ratio RA = H/R. For the purpose of validating the
novel LB schemes presented in this work, we set Pr = 0.7, Ra = 5 × 103 and
RA = 1 and the domain is resolved by 100 × 100 lattice nodes by using the
relaxation times ωj = 1/τ, j = 4, 5, where τ = 0.85. No slip, and constant
temperature and adiabatic boundary conditions are represented by using the
same approaches are mentioned earlier, and the axis of symmetry is taken into
account by using the mirror boundary conditions for the particle distribution
functions in the LB schemes.
27


## Page 28


Figure 4: Schematic illustration of Rayleigh-Benard Convection in a vertical cylinder.
Figure 5 show the steady isotherms and velocity vectors. Interestingly, it
can be seen that based on the initial conditions for temperature, diﬀerent ﬂow
patterns and isotherms are observed. In particular, if the initial temperature
is set to TL everywhere, an up ﬂow draft around the center of the cylinder is
observed, while if a higher buoyancy force is prescribed by the initial conditions,
a down ﬂow convective current around the center of the cylinder is set up. Those
reversal in ﬂow patterns are consistent with ﬁndings based on other numerical
schemes [26, 5].
(a) Up-ﬂow
(b) Down-ﬂow
Figure 5: Isotherms and velocity vectors for Rayleigh-Bernard convection in a vertical cylinder
at Ra = 5 × 103, Pr = 0.7, RA = 1. Left column: Up-ﬂow pattern and Right column: Down-
ﬂow pattern.
In addition, Table 2 presents a comparison of the maximum velocity in di-
28


## Page 29


Table 2:
Comparison of the dimensionless maximum velocity obtained using the scale
p
gβH(TH −TL) for Rayleigh Benard convection in a vertical cylinder at Ra = 5 × 103
computed using axisymmetric cascaded LB schemes with reference data.
Ra
Reference
Up-ﬂow
Down-ﬂow
Ref. [26]
0.353
0.351
5 × 103
Ref. [5]
0.353
0.353
Present Work
0.353
0.351
mensionless form using the natural convection velocity scale
p
gβH(TH −TL)
obtained using axisymmetric cascaded LB approach with results from the work
of [26, 5]. Evidently, the computed results agree very well with those reported
in the literature.
3.4. Swirling ﬂow in a lid-driven cylindrical container
In this section, we investigate the ability of the axisymmetric cascaded LB
schemes to accurately simulate the dominant role played by the swirling motion
and its coupling with the complex radial and axial ﬂow induced in the meridian
plane. In this regard, we consider the symmetry breaking ﬂow in a cylindrical
container of radius R and height H driven by a rotating top end wall at angular
velocity Ω(see Fig. 6).
The dynamics of this ﬂow is presented by Eqs.
(3a)-(3c), (4a)-(4c), (6)
and (7), whose solution scheme via our cascaded LB formulation is presented
in Sec.2.2 and 2.3.
Brieﬂy, as the ﬂuid in the vicinity of the top lid gains
azimuthal motion, it is ejected radially outward, and then downward due to the
constraining eﬀect of the side wall. Subsequently as the ﬂuid reaches the bottom
it is pushed radially inward, and when it is closer to the axis, it travels upward,
thereby completing ﬂow circulation in the meridian plane. The details of the
physics and the ﬂow pattern depend on the aspect ratio RA = H/R and the
rotational Reynolds number Re = R2Ω/ν. Various experiments (e.g., [51, 52])
and numerical simulations (e.g., [53, 54, 55]) have revealed that for certain
combinations of the characteristic parameters RA and Re, distinct recirculation
29


## Page 30


Figure 6: Schematic of swirling ﬂow in a conﬁned cylinder driven by a rotating top lid.
regain around the cylinder axis, designated as the vortex breakdown bubble,
may occur. For example, Refs. [52, 56] show that for cases (RA, Re) equal to
(1.5, 990) and (2.5,1010), no vortex breakdown bubbles occur whereas for (1.5,
1290), they do occur.
In order to asses and validate our cascaded LB schemes presented earlier to
simulate such complex swirling ﬂow, we consider the following four test cases:
Re = 990 and Re = 1290 with RA = 1.5 and Re = 1010 and Re = 2020 with
RA = 2.5. The computational domain is resolved using a mesh resolution of
100×150 for RA = 1.5 and 100×250 for RA = 2.5. No-slip boundary conditions
are used at bottom, lateral and top walls: uθ = ur = uz = 0 at z = 0 and r = R,
and uθ = rΩ, ur = uz = 0 at z = H. The streamlines computed using the
cascaded LB schemes for the above four cases are in Fig. 7. It can be seen that
no vortex break-down bubbles appear for (RA, Re) equal to (1.5, 990) and (1.5,
1010). On the other hand, one vortex break down bubble is seen at (1.5, 1290)
and two break down bubbles occur in the vicinity of the cylinder axis. These
distinct regimes in swirling ﬂows and the complex ﬂow structure for diﬀerent
30


## Page 31


(RA, Re) cases are strikingly consistent with prior numerical solution (e.g., [56,
19, 21, 57]). Quantitative comparison of the computed structure of the axial
velocities along the axis of symmetry obtained using the axisymmetric cascaded
LB schemes for the above four sets of the aspect ratios RA and Reynolds number
Re against the results from a NS-based solver (given in [56]) are shown in Fig. 8.
Here, the axial velocity is scaled by the maximum imposed azimuthal velocity
uo = ΩR on the rotating lid and the axial distance z by the cylinder height H.
The numerical results of our central moments based cascaded LB method for
the axial velocity proﬁles are in very good agrement with the NS-based solution
approach [56].
Also, in particular, notice local negative values for the axial
velocities for the cases Re = 1290 and RA = 1.5 and Re = 2200 and RA = 2.5,
which is an indication of the presence of one or more vortex breakdown bubbles.
As such, both the magnitudes and the shapes of the axial velocity distributions
are well reproduced by our cascaded LB approach using operator splitting to
represent complex ﬂows in cylindrical coordinates.
3.5. Mixed convection in a slender vertical annulus between two coaxial cylinders
We will now assess our new axisymmetric LB computational approach based
on central moments to simulate the combined eﬀects of rotation and buoyancy
forces on the ﬂow and heat transfer in conﬁned cylindrical spaces. In this re-
gard, we investigate mixed convection in a slender vertical annulus between two
coaxial cylinders arising due to inner side wall rotation, which has numerous
applications related to rotating machinery and various other heat transfer sys-
tems. This problem involving both natural convection and forced convection
due to rotation can test all the three axisymmetric cascaded LB formulations
(Secs. 2.2-2.4) in a uniﬁed manner.
A schematic arrangement of this axisymmetric thermal ﬂow problem is
shown in Fig. 9. It consist of two coaxial cylinders of height H, with an an-
nular gap D = Ro −Ri, where Ri and Ro are the radii of the inner and outer
cylinders, respectively. The lateral walls of the inner and outer cylinders are
maintained at temperatures TH and TL, respectively, where TH > TL, and their
31


## Page 32


(a) RA = 1.5, Re=990
(b) RA = 1.5, Re=1290
(c) RA = 2.5, Re=1010
(d) RA = 2.5, Re=2200
Figure 7: Computed streamline patterns in the meridian plane due to swirling ﬂow in a
conﬁned cylinder driven by a rotating lid at various aspect ratios and Reynolds numbers
using the axisymmetric cascaded LB sachems: (a) RA = 1.5 and Re = 990, (b) RA = 1.5 and
Re = 1290 (c)RA = 2.5 and Re = 1010 and (d)RA = 2.5 and Re = 2200.
32


## Page 33


(a) Re=990, RA = 1.5
(b) Re=1290, RA = 1.5
(c) Re=1010, RA = 2.5
(d) Re=2200, RA = 2.5
Figure 8: Dimensionless axial velocity proﬁle uz/uo as a function of the dimensional axial
distance z/H for (a) RA = 1.5 and Re = 990, (b) RA = 1.5 and Re = 1290 (c)RA = 2.5 and
Re = 1010 and (d)RA = 2.5 and Re = 2200: Comparison between axisymmetric cascaded LB
scheme predictions and NS-based solver results ([56])
33


## Page 34


Figure 9: Schematic of the arrangement for mixed convection in a slender cylindrical annulus
with inner lateral wall rotation.
bottom and top ends are thermally insulated. The inner cylinder is subjected
to rotation at an angular velocity Ωi, while the outer cylinder and the end walls
are considered to be rigidly ﬁxed. As noted in a recent study [30], this problem
is governed by the following characteristic dimensionless parameters: Prandtl
number Pr = ν/α, radius ratio Rio = Ro/Ri slenderness ratio η = H/(Ro−Ri),
Reynolds number Re = ΩiRiD/ν, Grashof number Gr = gβ(TH −TL)D3/ν2,
and σ = Gr/Re2, where the parameter σ is used to measure the strength of
the buoyancy force relative to the centrifugal force. Hence, σ characterizes the
degree of mixed convection.
In the present study, we set Pr = 0.7, Rio = 2, η = 10, Re = 100, and
three cases of σ are considered: σ = 0, 0.01 and 0.05.
The grid resolution
used for all the three cases is 40 × 400, in which the location of the inner
cylinder from the axis Ri is at 40.
Figure 10 shows the computed contours
of the azimuthal velocity, temperature ﬁeld, vorticity and streamlines for the
above three values of σ. When σ = 0, there is no buoyancy force and the ﬂow
and the temperature ﬁelds are inﬂuenced by the centrifugal force and the forced
34


## Page 35


Figure 10: Contours of (a) azimuthal velocity, (b) temperature, (c) vorticity, and (d) stream-
lines for mixed convection in a slender cylindrical annulus for three diﬀerent values of σ
computed using the axisymmetric cascaded LB schemes.
35


## Page 36


convection eﬀects, which manifest in the form of ﬁve pairs of counter-rotating
cells, viz., the classical Taylor vortex cells arising from centrifugal ﬂow instability
between curved walls [2]. As σ is increased, the presence of buoyancy forces and
the associated natural convective ﬂuid currents alter the overall ﬂow structure
and the temperature ﬁeld by their complicated interactions with primary vortex
cells induced by the swirling eﬀects from inner wall rotation. For example, when
σ = 0.05, a four-pairs based Taylor vortex structure, rather than ﬁve-pair of
vortex cells observed for σ = 0, arises from the relative weakening eﬀects of the
centrifugal forces in the presence of heating . The strength of the Taylor vortex
in the positive azimuthal direction θ is seen to be enhanced, while that negative
θ direction appear to be diminished and these observations are consistent with
the benchmarks results [58, 59] and recent numerical simulations [29]. In order
to quantify the heat transfer rate in the presence of mixed convection, a mean
equivalent thermal conductivity at the inner cylinder can be deﬁned as
keq|i = lnRio
µ
Z H
o

−r∂T
∂r |r=Ri

dr.
Table 3 presents a comparison of the equivalent thermal conductively computed
using the axisymmetric cascaded LB formulations against the benchmark results
[58, 59] for diﬀerent values of σ. Very good quantitative agrement is seen and
this validates the ability of the cascaded LB schemes in the cylindrical coordinate
system to represent complex ﬂows with heat transfer.
Table 3: Comparison of the mean equivalent thermal conductivity at the inner cylinder in a
slender vertical cylindrical annulus during mixed convection for Re = 100, Pr = 0.7, Rio =
2, η = 10 at diﬀerent values of σ.
σ
Ref. [59]
Ref. [58]
Present Work
0
1.473
1.393
1.395
0.01
1.370
1.383
1.378
0.05
1.324
1.323
1.321
36


## Page 37


3.6. Melt ﬂow and convection during Czochralski crystal growth in a rotating
cylindrical crucible
As the last test problem, we simulate melt ﬂow and convection during
Czochalski crystal growth, based on a conﬁguration reported by Wheeler [60],
using our axisymmetric cascaded LB schemes. This Wheeler’s benchmark prob-
lem involved both forced convection due to the rotation of the crucible and the
crystal and natural convection arising from heating eﬀects in the presence of
gravity. It has been studied by a variety of numerical schemes (e.g., [61, 62, 22,
30]). The geometric arrangement of this problem is shown in Fig. 11.
Figure 11: Geometric arrangement of melt ﬂow and convection during Czochralski crustal
growth in a rotating crucible−Wheeler’s benchmark problem.
Liquid melt in a cylindrical rotating crucible of radius Rc and height H at
an angular rotation rate of Ωc undergoes stirred vortical motion in the meridian
plane, which is aided by the angular rotation of the solid crystal of radius Rx
at rate Ωx. In addition, natural convection is set up due to the buoyancy force
generated from a diﬀerential heating, where the bottom is insulated and its
crucible side is maintained at a temperature TH, while the crystal is at a lower
temperature TL (i.e., TL < TH).
These can be prescribed in terms of the
37


## Page 38


following boundary conditions, where the (x, z) coordinates are scaled by Rc :
ur = uθ = ∂uz
∂r = ∂T
∂r = 0
for
r = 0 0 ≤z ≤α
ur = uz = 0, uθ = ΩcRc, T = TH
for
r = 1 0 ≤z ≤α
ur = uz = 0, uθ = rΩc, ∂T
∂z = 0
for
z = 0 0 ≤r ≤1
ur = uz = 0, uθ = rΩx, T = TL
for
z = α 0 ≤r ≤β
∂ur
∂r = ∂uθ
∂z = 0, uz = 0, T = TL + r −β
1 −β (TH −TL)
for
z = α β ≤r ≤1
where α = H/Rc, β = Rx/Rc. This ﬂow problem is characterized by the fol-
lowing dimensionless parameters: Reynolds numbers due to crucible and crystal
rotations Rec = R2
cΩc/ν and Rex = R2
xΩx/ν, and Prandtl number Pr = ν/α.
We investigate the ability of the axisymmetric cascaded LB schemes for the sim-
ulation of mixed convection associated with the Wheeler’s benchmark problem
for the following two cases: (a) Rex = 100, Rec = −25 and (b) Rex = 1000,
Rec = −250, where the negative sign denotes that the sense of rotation of the
crystal is apposite to that of the crucible. We take Pr = 0.05, α = 1, and β = 1
and use a grid resolution of 100 × 200 for the simulation of both the cases.
Figure 12 shows the streamlines and isotherm contours in the meridian plane
of the liquid melt motion for the two cases. It can be seen that a recirculating
vortex appears around the upper left region below the crystal in both cases in
addition to the primary vortex. The center of this secondary vortex is found to
move to the right at higher Reynolds numbers as a result of higher associated
centrifugal forces. On the other hand, the forced convection has modest eﬀect
on the temperature distribution, as they are largely alike for both the cases due
to the relatively low Reynolds numbers considered.
Table 4 shows the computed absolute maximum values of the streamfunc-
tion ψmax for the above two cases and compared with prior numerical results
presented in [22, 61]. In the pseudo-2D Cartesian coordinates, this is obtained
by solving for ψ using ∂ψ/∂y = −yux and ∂ψ/∂x = yuy. The good agree-
ment conﬁrms that the new axisymmetric cascaded LB schemas presented in
38


## Page 39


(a) Rex = 100, Rec = −25
(b) Rex = 1000, Rec = −250
(c) Rex = 100, Rec = −25
(d) Rex = 1000, Rec = −250
Figure 12: Streamlines (upper row) and isotherms (bottom row) corresponding to two cases
of the Wheeler’s benchmark problem of melt ﬂow and convection during Czochralshi crystal
growth: Rex = 100, Rec = −25 (left) and Rex = 1000, Rec = −250 (right).
39


## Page 40


this study can eﬀectively simulate complex ﬂow and heat transfer problems in
cylindrical geometries.
Table 4: Comparison of the maximum value of the stream function ψmax computed using
the axisymmetric cascaded LB schemes with reference numerical solutions for the Wheeler’s
benchmark problem.
Reference
Rex = 102, Rec=-25
Rex = 103, Rec=-250
Present Work
0.1183
1.123
Ref. [63]
0.1140
1.114
Ref. [61]
0.1177
1.148
40


## Page 41


4. Summary and Conclusions
Thermally stratiﬁed ﬂuid convection including rotational eﬀects within cylin-
drical conﬁned spaces represents an important class of ﬂows with numerous engi-
neering applications. Exploiting axial symmetry in such problems leads to their
representation in terms of a quasi-2D system of equations with geometric source
terms in the meridian plane, which can signiﬁcantly reduce computational and
memory costs when compared to their 3D modeling.
In this work, we have presented axisymmetric cascaded LB schemes for con-
vecttive ﬂows with combined rotation and thermal stratiﬁcation eﬀects in cylin-
drical geometries. A triple distribution functions based approach is employed in
this regard, in which the axial and radial momentum as well as the pressure ﬁeld
are solved using a D2Q9 lattice based cascaded LB scheme, while the azimuthal
momentum and the temperature ﬁeld are solved using the two other cascaded
LB schemes, each based on a D2Q5 lattice. The collision step in these three
schemes is based on the relaxation of diﬀerent central moments at diﬀerent
rates to represent the dynamics of the ﬂuid motion as well as the advection-
diﬀusion transport of the passive scalar ﬁelds in a consistent framework. The
geometric mass, momentum and energy source terms arising in the quasi-2D
formulation are incorporated using a simpler operator splitting based approach
involving a symmetric application of their eﬀects given in terms of appropriate
change of moments for two half time steps around the collision step. This new
computational approach is then used to simulate a variety of complex axisym-
metric benchmark thermal ﬂow problems including natural convection between
two coaxial cylinders, Rayleigh-Benard convection in a vertical cylinder, mixed
convection in a slender vertical annulus between two cylinders under combined
rotation and buoyancy forces, and convective ﬂow of a melt during Czochralski
crystal growth in a rotating cylindrical crucible. Comparison of the computed
results obtained using the axisymmetric cascaded LB schemes for such ther-
mal convective ﬂows for the structures of the ﬂow and thermal ﬁelds, as well
as the heat transfer rates given in terms of the Nusselt number against prior
41


## Page 42


benchmark numerical solutions demonstrate their good accuracy and validity.
42


## Page 43


References
References
[1] H. P. Greenspan, The theory of rotating ﬂuids, Tech. rep., Cambridge Uni-
versity Press, London (1968).
[2] E. L. Koschmieder, Bénard cells and Taylor vortices, Cambridge University
Press, New York, 1993.
[3] I. V. Shevchuk, Modelling of convective heat and mass transfer in rotating
ﬂows, Springer, New York, 2016.
[4] K. Fujimura, Time-dependent vortex breakdown in a cylinder with a ro-
tating lid, Trans. ASME, J. Fluids Eng 199 (1997) 450–453.
[5] A. Lemembre, J.-P. Petit, Laminar natural convection in a laterally heated
and upper cooled vertical cylindrical enclosure, Int. J. Heat Mass Transfer
41 (16) (1998) 2437–2454.
[6] E. Barbosa, O. Daube, A ﬁnite diﬀerence method for 3d incompressible
ﬂows in cylindrical coordinates, Comp. Fluids 34 (8) (2005) 950–971.
[7] A. Guardone, L. Vigevano, Finite element/volume solution to axisymmetric
conservation laws, J.Comp. Phys 224 (2) (2007) 489–518.
[8] X. He, L.-S. Luo, Theory of the lattice Boltzmann method: From the
Boltzmann equation to the lattice Boltzmann equation, Phys. Rev. E 56 (6)
(1997) 6811.
[9] S. Succi, The lattice Boltzmann equation: for ﬂuid dynamics and beyond,
Oxford university press, 2001.
[10] C. K. Aidun, J. R. Clausen, Lattice-Boltzmann method for complex ﬂows,
Annu. Rev. Fluid Mech 42 (2010) 439–472.
[11] T. Krüger, H. Kusumaatmaja, A. Kuzmin, O. Shardt, G. Silva, E. M.
Viggen, The Lattice Boltzmann Method, Springer, 2017.
43


## Page 44


[12] L. Mieussens, Discrete-velocity models and numerical schemes for the
Boltzmann-BGK equation in plane and axisymmetric geometries, Journal
of Computational Physics 162 (2) (2000) 429–466.
[13] I. Halliday, L. Hammond, C. Care, K. Good, A. Stevens, Lattice Boltzmann
equation hydrodynamics, Phys. Rev. E 64 (1) (2001) 011208.
[14] K. N. Premnath, J. Abraham, Lattice Boltzmann model for axisymmetric
multiphase ﬂows, Phys. Rev. E 71 (5) (2005) 056706.
[15] T. Lee, H. Huang, C. Shu, An axisymmetric incompressible lattice Boltz-
mann model for pipe ﬂow, Int. J. Mod. Phys.C 17 (05) (2006) 645–661.
[16] T. Reis, T. N. Phillips, Modiﬁed lattice Boltzmann model for axisymmetric
ﬂows, Phys. Rev. E 75 (5) (2007) 056703.
[17] J. G. Zhou, Axisymmetric lattice Boltzmann method, Phys. Rev. E 78 (3)
(2008) 036701.
[18] S. Chen, J. Tölke, S. Geller, M. Krafczyk, Lattice Boltzmann model for
incompressible axisymmetric ﬂows, Phys. Rev. E 78 (4) (2008) 046703.
[19] Z. Guo, H. Han, B. Shi, C. Zheng, Theory of the lattice Boltzmann equa-
tion: lattice Boltzmann model for axisymmetric ﬂows, Phys. Rev. E 79 (4)
(2009) 046708.
[20] H. Huang, X.-Y. Lu, Theoretical and numerical study of axisymmetric
lattice Boltzmann models, Phys. Rev. E 80 (1) (2009) 016701.
[21] Q. Li, Y. He, G. Tang, W. Tao, Improved axisymmetric lattice Boltzmann
scheme, Phys. Rev. E 81 (5) (2010) 056707.
[22] Y. Peng, C. Shu, Y. Chew, J. Qiu, Numerical investigation of ﬂows in
Czochralski crystal growth by an axisymmetric lattice Boltzmann method,
J. Comp. Phys 186 (1) (2003) 295–307.
44


## Page 45


[23] H. Huang, T. Lee, C. Shu, Hybrid lattice Boltzmann ﬁnite-diﬀerence simu-
lation of axisymmetric swirling and rotating ﬂows, Int. J. Numer. Methods
Fluids 53 (11) (2007) 1707–1726.
[24] S. Chen, J. Tölke, M. Krafczyk, Simulation of buoyancy-driven ﬂows in
a vertical cylinder using a simple lattice Boltzmann model, Phys. Rev. E
79 (1) (2009) 016704.
[25] Q. Li, Y. He, G. Tang, W. Tao, Lattice Boltzmann model for axisymmetric
thermal ﬂows, Phys. Rev. E 80 (3) (2009) 037702.
[26] L. Zheng, B. Shi, Z. Guo, C. Zheng, Lattice Boltzmann equation for ax-
isymmetric thermal ﬂows, Comp. & Fluids 39 (6) (2010) 945–952.
[27] L. Zheng, Z. Guo, B. Shi, C. Zheng, Kinetic theory based lattice Boltzmann
equation with viscous dissipation and pressure work for axisymmetric ther-
mal ﬂows, J. Comp. Phys. 229 (16) (2010) 5843–5856.
[28] L. Li, R. Mei, J. F. Klausner, Multiple-relaxation-time lattice Boltzmann
model for the axisymmetric convection diﬀusion equation, Int. J. Heat Mass
Transfer 67 (2013) 338–351.
[29] Z. Wang, W. Zhang, J. Zhang, Lattice Boltzmann simulations of axisym-
metric natural convection with anisotropic thermal diﬀusion, Int. J. Heat
Mass Transfer 101 (2016) 1304–1315.
[30] Y. Wang, C. Shu, C. Teo, A fractional step axisymmetric lattice Boltzmann
ﬂux solver for incompressible swirling and rotating ﬂows, Comp. Fluids 96
(2014) 204–214.
[31] Z. Wang, N. Dang, J. Zhang, A modiﬁed lattice Bhatnagar-Gross-Krook
model for axisymmetric thermal ﬂow, Int. J. Heat Mass Transfer 108 (2017)
691–702.
[32] Y. Qian, D. d’Humières, P. Lallemand, Lattice BGK models for Navier-
Stokes equation, EPL (Europhys. Lett) 17 (6) (1992) 479.
45


## Page 46


[33] D. d’Humières, I. Ginzburg, M. Krafczyk, P. Lallemand, L.-S. Luo,
Multiple–relaxation–time lattice Boltzmann models in three dimensions,
Phil. Trans. Roy. Soc. London A 360 (1792) (2002) 437–451.
[34] M. Geier, A. Greiner, J. G. Korvink, Cascaded digital lattice Boltzmann au-
tomata for high Reynolds number ﬂow, Phys. Rev. E 73 (6) (2006) 066705.
[35] P. Asinari, Generalized local equilibrium in the cascaded lattice Boltzmann
method, Phys. Rev. E 78 (1) (2008) 016701.
[36] K. N. Premnath, S. Banerjee, Incorporating forcing terms in cascaded lat-
tice Boltzmann approach by method of central moments, Phys. Rev. E
80 (3) (2009) 036702.
[37] K. N. Premnath, S. Banerjee, on the three dimensional central moment
lattice-Boltzmann method, J. Stat. Phys. 43 (2011) 747–749.
[38] M. Geier, M. Schönherr, A. Pasquali, M. Krafczyk, The cumulant lattice
Boltzmann equation in three dimensions: Theory and validation, Comp.
Math. Appl 70 (4) (2015) 507–547.
[39] A. De Rosis, Non-orthogonal central moments relaxing to a discrete equi-
librium: A D2Q9 lattice Boltzmann model, EPL (Europhys Lett) 116 (4)
(2017) 44003.
[40] F. Hajabdollahi, K. N. Premnath, Improving the low mach number steady
state convergence of the cascaded lattice Boltzmann method by precondi-
tioning, Computers & Mathematics with Applications.
URL http://dx.doi.org/10.1016/j.camwa.2016.12.034
[41] F. Hajabdollahi,
K. N. Premnath,
Galilean-invariant preconditioned
central-moment lattice boltzmann method without cubic velocity errors for
eﬃcient steady ﬂow simulations, Physical Review E 97 (5) (2018) 053303.
[42] K. V. Sharma, R. Straka, F. W. Tavares, New cascaded thermal lattice
Boltzmann method for simulations of advection-diﬀusion and convective
heat transfer, Int. J. Therm. Sci 118 (2017) 259–277.
46


## Page 47


[43] L. Fei, K. H. Luo, C. Lin, Q. Li, Modeling incompressible thermal ﬂows us-
ing a central-moments-based lattice Boltzmann method, Int. J. Heat Mass
Transfer 120 (2018) 624–634.
[44] F. Hajabdollahi, K. N. Premnath, Central moments-based cascaded lattice
Boltzmann method for thermal convective ﬂows in three-dimensions, Int.
J. Heat Mass Transfer 120 (2018) 838–850.
[45] F. Hajabdollahi, K. N. Premnath, Symmetrized operator split schemes for
force and source modeling in cascaded lattice boltzmann methods for ﬂow
and scalar transport, Physical Review E 97 (6) (2018) 063303.
[46] G. Taylor, Stability of a viscous liquid contained between two rotating
cylinders, Phil. Trans. Roy. Soc. Lond. A 223 (1923) 289–343.
[47] H. Yoshida, M. Nagaoka, Multiple-relaxation-time lattice Boltzmann model
for the convection and anisotropic diﬀusion equation, J. Comp. Phys
229 (20) (2010) 7774–7795.
[48] R. Kumar, M. Kalam, Laminar thermal convection between vertical coaxial
isothermal cylinders, Int. J. Heat Mass Transf 34 (1991) 513.
[49] M. Venkatachalappa, M. Sankar, A. Natarajan, Natural convection in an
annulus between two rotating vertical cylinders, Acta Mech. 147 (2001)
173.
[50] S. Liang, A. Vidal, A. Acrivos, Buoyancy-driven convection in cylindrical
geometries, J. Fluid Mech 36 (2) (1969) 239–258.
[51] K. Hourigan, L. Graham, M. Thompson, Spiral streaklines in pre-vortex
breakdown regions of axisymmetric swirling ﬂows, Phys. Fluids 7 (12)
(1995) 3126–3128.
[52] K. Fujimura, H. Yoshizawa, R. Iwatsu, H. S. Koyama, J. M. Hyun, Veloc-
ity measurements of vortex breakdown in an enclosed cylinder, Journal of
Fluids Engg 123 (3) (2001) 604–611.
47


## Page 48


[53] A. Y. Gelfgat, P. Bar-Yoseph, A. Solan, Stability of conﬁned swirling ﬂow
with and without vortex breakdown, J. Fluid Mech 311 (1996) 1–36.
[54] E. Serre, P. Bontoux, Vortex breakdown in a three-dimensional swirling
ﬂow, J. Fluid Mech 459 (2002) 347–370.
[55] H. M. Blackburn, J. Lopez, Symmetry breaking of the ﬂow in a cylinder
driven by a rotating end wall, Phys. Fluids 12 (11) (2000) 2698–2701.
[56] S. Bhaumik, K. Lakshmisha, Lattice Boltzmann simulation of lid-driven
swirling ﬂow in conﬁned cylindrical cavity, Comp. Fluids 36 (7) (2007)
1163–1173.
[57] J. Zhou, Axisymmetric lattice Boltzmann method revised, Phys. Rev. E 84
(2011) 036704.
[58] C. J. Ho, F. J. Tu, An investigation of transient mixed convection of cold
water in a tall vertical annulus with a heated rotating inner cylinder, Int.
J. Heat Mass Transfer 36 (1993) 2847–2859.
[59] K. S. Ball, B. Farouk, On the development of Taylor vortices in a vertical
annulus with a heated rotating inner cylinder, Int. J. Numer. Meth. Fluids
7 (1987) 857–867.
[60] A. Wheeler, Four test problems for the numerical simulation of ﬂow in
Czochralski crystal growth, J. Cryst. Growth 102 (4) (1990) 691–695.
[61] D. Xu, C. Shu, B. C. Khoo, Numerical simulation of ﬂows in Czochralski
crystal growth by second-order upwind QUICK scheme, J. Crystal Growth
173 (1997) 123–131.
[62] C. Shu, Y. Chew, Y. Liu, An eﬃcient approach for numerical simulation
of ﬂows in Czochralski crystal growth, J. Cryst. Growth 181 (4) (1997)
427–436.
48


## Page 49


[63] Y. Peng, C. Shu, Y. T. Chew, J. Qiu, Numerical investigation of ﬂows in
Czochralski crystal growth by an axisymmetric lattice Boltzmann method.,
J. Comput. Phys. 186 (2003) 295–307.
49

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
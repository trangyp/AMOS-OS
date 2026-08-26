---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.08475v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1903.08475v1_A_Generalized_Solution_Method_for_Parallelized_Computation_of_the_Three-dimensio

> Source: 1903.08475v1_A_Generalized_Solution_Method_for_Parallelized_Computation_of_the_Three-dimensio.pdf

> Pages: 12

---


## Page 1


Draft version March 21, 2019
Preprint typeset using LATEX style AASTeX6 v. 1.0
A GENERALIZED SOLUTION METHOD FOR PARALLELIZED COMPUTATION OF THE THREE-DIMENSIONAL
GRAVITATIONAL POTENTIAL ON A MULTI-PATCH GRID IN SPHERICAL GEOMETRY
Annop Wongwathanarat
Max-Planck-Institut f¨ur Astrophysik, Karl-Schwarzschild-Str. 1, 85748 Garching, Germany
ABSTRACT
We present a generalized algorithm based on a spherical harmonics expansion method for eﬃcient computation
of the three-dimensional gravitational potential on a multi-patch grid in spherical geometry. Instead of solving
for the gravitational potential by superposition of separate contributions from the mass density distribution on
individual grid patch our new algorithm computes directly the gravitational potential due to contributions from
all grid patches in one computation step, thereby reducing the computational cost of the gravity solver. This
is possible by considering a set of angular weights which are derived from rotations of spherical harmonics
functions deﬁned in a global coordinate system that is common for all grid patches. Additionally, our algo-
rithm minimizes data communication between parallel compute tasks by eliminating its proportionality to the
number of subdomains in the grid conﬁguration, making it suitable for parallelized computation on a multi-
patch grid conﬁguration with any number of subdomains. Test calculations of the gravitational potential of a
tri-axial ellipsoidal body with constant mass density on the Yin-Yang two-patch overset grid demonstrate that
our method delivers the same level of accuracy as a previous method developed for the Yin-Yang grid, while
oﬀering improved computation eﬃciency and parallel scaling behaviour.
Keywords: methods: numerical — gravitation
1. INTRODUCTION
When modeling self-gravitating systems a gravity solver
that calculates the gravitational potential by solving the Pois-
son’s equation is one of the central components in the simu-
lations. For multi-dimensional hydrodynamical simulations
of self-gravitating ﬂows the Poisson’s equation is solved at
every hydrodynamical time step, and thus can be responsible
for a signiﬁcant fraction of the computational cost. Hence,
several techniques for an eﬃcient gravity solver have been
developed over the past decades. An algorithm of choice is
often decided by the complexity of the mass density distri-
bution on the computational domain and the numerical tech-
nique used to solve the coupled hydrodynamic equations. For
instance, hierarchical tree-based algorithm (e.g., Appel 1985;
Jernigan 1985; Porter 1985; Barnes & Hut 1986; Hernquist &
Katz 1989) is usually the preferred choice in particle-based
codes due to its ﬂexibility in considering arbitrary geome-
try. On the other hand, for grid-based codes a solver based
on Fast Fourier Transform (FFT) can easily be applied when
the grid spacing is uniform (Hockney 1970; Boris & Roberts
1969). For problems with large spatial dynamic ranges such
as cosmological structure formation or star cluster forma-
tion an adaptive mesh reﬁnement (AMR) technique is em-
annop@mpa-garching.mpg.de
ployed in order to achieve high eﬀective spatial resolution.
On such adaptive grids iterative multi-grid gravity solvers
(e.g., Ricker 2008) are usually used, but an application of
the tree-based solver on AMR grids has also recently been
investigated (W¨unsch et al. 2018).
In stellar hydrodynamics, three-dimensional (3D) simu-
lations have mostly been performed on a spherical polar
grid. For this class of simulations a common choice of grav-
ity solvers is the algorithm based on a spherical harmonics
expansion of the Green’s function developed by M¨uller &
Steinmetz (1995). This gravity solver has been employed, for
example, in several 3D CCSNe simulations (e.g., Vartanyan
et al. 2019; Glas et al. 2018; Wongwathanarat et al. 2017;
Lentz et al. 2015) due to its high computation eﬃciency in
a case where the gravitational potential is dominated by the
monopole term contribution from a central quasi spherical
body (e.g., the proto-neutron star in CCSNe). It has also
been adapted for a calculation on a Cartesian mesh (Couch
et al. 2013), and is now implemented as a modular compo-
nent in recent versions of the Flash code (Fryxell et al. 2000;
Dubey et al. 2009). On the other hand, an alternative algo-
rithm which solves the discretized Poisson’s equation on a
spherical polar grid using FFT has recently been developed
by M¨uller & Chan (2018). This algorithm gives more ac-
curate solutions of the gravitational potential than those ob-
tained by the multipole expansion technique for extremely
asymmetric density conﬁgurations such as an oﬀ-center point
arXiv:1903.08475v1  [physics.comp-ph]  20 Mar 2019


## Page 2


2
A. Wongwathanarat
mass. Such an algorithm will particularly be more advanta-
geous in cases where multiple components of mass concen-
tration are present on the grid.
Because spatial discretization of the computational domain
by a spherical polar grid introduces a severe time step con-
straint imposed by small grid zones in the polar regions, mod-
ern multi-patch grid techniques in spherical geometry such as
the Yin-Yang grid (Kageyama & Sato 2004) and the cubed-
sphere grid (Ronchi et al. 1996) have recently been receiving
more attention. These grid techniques avoid coordinate sin-
gularities at the poles, and therefore help to speed up simula-
tions by increasing the allowed time step size. At the Garch-
ing supernova group, the Yin-Yang grid, which is a two-patch
overset grid conﬁguration, is implemented into the ﬁnite-
volume neutrino-radiation hydrodynamic code Prometheus-
Vertex (Fryxell et al. 1989; Rampp & Janka 2002), and is
now being used extensively by for performing state-of-the-
art calculations of core-collapse supernovae (CCSNe) in 3D
(Summa et al. 2018; Melson et al. 2015).
Computation of self-gravity on a multi-patch grid in spher-
ical geometry is non-trivial. Extensions of the spherical har-
monics solver by M¨uller & Steinmetz (1995) and the FFT-
based solver by M¨uller & Chan (2018) for a multi-patch grid
are not readily available. For the case of the Yin-Yang grid,
Wongwathanarat et al. (2010) resorted to a simple approach.
They interpolated the density ﬁeld on the Yin-Yang grid onto
an auxilliary spherical polar grid, and then applied the algo-
rithm by M¨uller & Steinmetz (1995) without any modiﬁca-
tion. While this approach provides an easy workaround to
the solution, it is not ideal since it introduces an additional
source of errors through interpolation of the density ﬁeld.
Moreover, the method cannot be easily and eﬃciently par-
alellized for computation with a large number of processes
because of complicated data communication pattern.
A more eﬃciently parallelized approach for solving the
gravitational potential directly on the Yin-Yang grid based
on the algorithm by M¨uller & Steinmetz (1995) has re-
cently been proposed by Almanst¨otter et al. (2018, here-
after AMJM18). In their method, the gravitational potential
is computed by adding contributions from the mass density
distribution on the Yin and the Yang grid section, which are
evaluated separately. Since each grid patch in the Yin-Yang
grid conﬁguration is simply the low-latitude part of the usual
spherical polar grid, solving for the gravitational potential
using this approach is straightforward. Although this method
eliminates the need for interpolation of the density ﬁeld onto
a spherical polar grid and is easily parallelized on distributed-
memory systems, it is still not optimal. On the one hand,
the computational cost is increased because it calculates two
sets of potential. On the other hand, the data communication
volume among parallel compute tasks is also enlarged by a
factor of two when compared to computation on a spheri-
cal polar grid with the same number of compute tasks. The
latter imposes a limit to the parallel scalability of the algo-
rithm. Furthermore and most importantly, an extension of
this algorithm for other multi-patch conﬁgurations in spheri-
cal geometry with a larger number of grid sections (e.g., the
cubed-sphere grid) would signiﬁcantly decrease its compu-
tational eﬃciency because the additional computational cost
and the size of data communication are proportional to the
total number of grid patches.
In this paper, we derive a new algorithm for eﬃcient com-
putation of the 3D gravitational potential on a multi-patch
grid in spherical geometry based on spherical harmonics ex-
pansion. Our method is a generalization of the method by
M¨uller & Steinmetz (1995). It diﬀers from the previous al-
gorithm by AMJM18 in that our method calculates the sum
of all contributions to the gravitational potential from all grid
patches in one computation step. It takes full advantage of
the symmetry property of the multi-patch grid conﬁguration
when calculating angular weights for the density distribution
on each grid patch by utilizing rotational transformations of
spherical harmonics. Data communication between compute
tasks in parallel computation is minimized such that there is
no dependency on the number of grid patches in the mesh
conﬁguration. Consequently, this gravity solver is suitable
not only for the Yin-Yang grid with two grid sections but
also for other multi-patch conﬁgurations in spherical geome-
try that consist of a larger number of grid patches.
Our paper is organized as follows: We begin by summa-
rizing the basic algorithm by M¨uller & Steinmetz (1995) for
solving the 3D gravitational potential on a spherical polar
grid in Section 2. Then, we present our generalization of
the basic algorithm for a multi-patch grid conﬁguration in
spherical geometry, and give explicit formulae of angular and
radial weights needed for reconstruction of the gravitational
potential in Section 3. In Section 4, we detail our implemen-
tation of the new algorithm for the case of computation on
the Yin-Yang overset grid. Our algorithm is validated with a
test computation on the Yin-Yang grid. The results are shown
in Section 5 along with a performance analysis of our algo-
rithm in comparison with the previous method by AMJM18.
We conclude with discussions in Section 6.
2. BASE ALGORITHM ON A SPHERICAL POLAR
GRID
2.1. Basic equations
A brief summary of the eﬃcient algorithm by M¨uller &
Steinmetz (1995) for solving the integral form of the Pois-
son’s equation is as follows. The Poisson’s equation in its
integral form reads
Φ(r) = −G
Z
d3r′ ρ(r′)
|r −r′|.
(1)
Here, G is the gravitational constant, r = (r, θ, φ) is a coordi-
nate vector in spherical polar coordinates, and ρ(r) is the den-
sity distribution function. To solve this equation the Green’s
function |r −r′|−1 is expanded into spherical harmonics. Fol-


## Page 3


Generalized 3D gravity solver on a spherical multi-patch grid
3
lowing this expansion, the gravitational potential at a point r
can then be expressed as
Φ(r) = −G
∞
X
ℓ=0
4π
2ℓ+ 1
ℓ
X
m=−ℓ
Ym
ℓ(θ, φ) · [Aℓm(r) + Bℓm(r)] (2)
where the radius dependence functions Aℓm and Bℓm describ-
ing contributions to the gravitational potential from the mass
distribution inside and outside of a radial coordinate r are de-
ﬁned as
Aℓm(r) =
1
rℓ+1
"
4π
dΩ′Ym ∗
ℓ(θ′, φ′)
r
Z
0
dr′(r′)ℓ+2ρ(r′)
(3)
and
Bℓm(r) = rℓ
"
4π
dΩ′Ym ∗
ℓ(θ′, φ′)
∞
Z
r
dr′(r′)1−ℓρ(r′)
(4)
with dΩ= sin θ dθ dφ. Here we use the deﬁnition
Ym
ℓ(θ, φ) =
s
2ℓ+ 1
4π
(ℓ−m)!
(ℓ+ m)! · Pm
ℓ(cos θ) · eimφ
(5)
for spherical harmonics of degree ℓand order m where Pm
ℓare
the associated Legendre polynomials. Complex conjugates
of spherical harmonics Ym
ℓare denoted as Ym ∗
ℓ.
Using the deﬁnition in Eq. (5) and an identity for Pm
ℓwith
negative orders,
P−m
ℓ
= (−1)m (ℓ−m)!
(ℓ+ m)!Pm
ℓ,
(6)
Eq. (2) can be re-written as
Φ(r) = −G
∞
X
ℓ=0
ℓ
X
m=0
2
δm
(ℓ−m)!
(ℓ+ m)!Pm
ℓ(cos θ)
· Gℓm(r, φ) + Hℓm(r, φ)
(7)
where
Gℓm(r, φ) =
1
rℓ+1
"
4π
dΩ′Pm
ℓ(cos θ′)
× cos (m(φ −φ′))
r
Z
0
dr′(r′)ℓ+2ρ(r′)
(8)
and
Hℓm(r, φ) = rℓ
"
4π
dΩ′Pm
ℓ(cos θ′)
× cos (m(φ −φ′))
∞
Z
r
dr′(r′)1−ℓρ(r′).
(9)
The coeﬃcient δm is deﬁned by
δm =

2,
if m = 0,
1,
otherwise.
(10)
2.2. Discretized formulae on a spherical polar grid
Let us construct a spherical polar grid of Nr × Nθ × Nφ grid
cells, and use indices i, j, and k to label the ith, jth, and kth
grid cell in the r-, θ-, and φ-direction, respectively. For each
grid cell Zi jk coordinates of the (lower)higher side of the cell
in each coordinate direction are denoted by r(−)+
i
, θ(−)+
j
, and
φ(−)+
k
. To compute the gravitational potential on this grid nu-
merically using Eq. (7) we make two assumptions. Firstly,
we assume that the density distribution inside a grid cell Zi jk
is constant, and is approximated by the cell-averaged density
ρi jk. Secondly, we truncate the summation over spherical har-
monic degree ℓat a chosen value ℓmax.
Consider a case that the gravitational potential is to be cal-
culated at grid zone interfaces in the radial direction, Gℓm and
Hℓm can be numerically computed for the nth radial grid in-
terface as
Gℓm(r+
n , φ) =
1
(r+n )ℓ+1
n
X
i=1
Nθ
X
j=1
Nφ
X
k=1
ρi jkR(ℓ)
in,iT (ℓm)
j
F (m)
k
(11)
and
Hℓm(r+
n , φ) = (r+
n )ℓ
Nr
X
i=n+1
Nθ
X
j=1
Nφ
X
k=1
ρi jkR(ℓ)
out,iT (ℓm)
j
F (m)
k
(12)
where
F (m)
k
= cos (mφ) C(m)
k
+ sin (mφ) S(m)
k .
(13)
The angular weights T (ℓm)
j
, C(m)
k , and S(m)
k
in Eqs. (11)–(13)
are deﬁned by
T (ℓm)
j
=
θ+
j
Z
θ−
j
dθ′ sin θ′Pm
ℓ(cos θ′),
(14)
C(m)
k
=
φ+
k
Z
φ−
k
dφ′ cos (mφ′),
(15)
and
S(m)
k
=
φ+
k
Z
φ−
k
dφ′ sin (mφ′).
(16)
The integrals T (ℓm)
j
can be computed analytically with help of
recurrence formulae for the associated Legendre polynomi-
als, while the integrals C(m)
k
and S(m)
k
are elementary. Analytic
solutions to these integrals are already explicitly given by
Zwerger (1995) and recently also in the work by AMJM18.
Finally, the radial integrals
R(ℓ)
in,i =
r+
i
Z
r−
i
dr′(r′)ℓ+2
(17)


## Page 4


4
A. Wongwathanarat
ξ
η
ζ , ζ′
ξ′
η′ , η′′
ξ′′
x
y
z , ζ′′
α
β
γ
Figure 1. Schematic diagram showing deﬁnitions of the Euler angles
α, β, and γ in the z-y′-z′′ convention. The Euler angles parametrize
the rotational transformation from the [ξηζ] coordinate system to
the [xyz] coordinate system.
and
R(ℓ)
out,i =
r+
i
Z
r−
i
dr′(r′)1−ℓ
(18)
are also easy to compute.
Following the implementation steps suggested by M¨uller
& Steinmetz (1995) the angular parts of the summations in
Eqs. (11) and (12) deﬁned by
A(ℓm)
C,i =
Nθ
X
j=1
Nφ
X
k=1
ρijkT (ℓm)
j
C(m)
k
(19)
and
A(ℓm)
S,i
=
Nθ
X
j=1
Nφ
X
k=1
ρijkT (ℓm)
j
S(m)
k .
(20)
are computed ﬁrst. Then, the radial summations can be eval-
uated eﬃciently by utilizing recurrence relations
iX
i′=1
R(ℓ)
in,i′A(ℓm)
C/S,i′ = R(ℓ)
in,iA(ℓm)
C/S,i +
i−1
X
i′=1
R(ℓ)
in,i′A(ℓm)
C/S,i′
(21)
and
Nr
X
i′=i
R(ℓ)
out,i′A(ℓm)
C/S,i′ = R(ℓ)
out,iA(ℓm)
C/S,i +
Nr
X
i′=i+1
R(ℓ)
out,i′A(ℓm)
C/S,i′.
(22)
3. GENERALIZED ALGORITHM FOR A MULTI-PATCH
GRID IN SPHERICAL GEOMETRY
When solving for the gravitational potential on a multi-
patch grid conﬁguration in spherical geometry, e.g., the Yin-
Yang grid (Kageyama & Sato 2004) and the cubed-sphere
grid (Ronchi et al. 1996), the angular integrals over the 4π
spherical surface area in Eqs. (3) and (4) are splitted into Ng
parts with Ng being the number of grid patches in the consid-
ered grid conﬁguration. Each integration part is performed
over the solid angle Ωg covered by the gth grid patch. The
functions Aℓm and Bℓm can then be re-written as
Aℓm(r) =
1
rℓ+1
Ng
X
g=1
"
Ωg
dΩ′w(θ′, φ′)Ym ∗
ℓ(θ′, φ′)
×
r
Z
0
dr′(r′)ℓ+2ρ(r′)
(23)
and
Bℓm(r) = rℓ
Ng
X
g=1
"
Ωg
dΩ′w(θ′, φ′)Ym ∗
ℓ(θ′, φ′)
×
∞
Z
r
dr′(r′)1−ℓρ(r′)
(24)
where the complex conjugates of spherical harmonics are
multiplied by a weight function w(θ, φ) to account for over-
lapping area in the case of an overlapping grid conﬁgura-
tion. This surface weight function takes a value of 1/ng(θ, φ)
where ng(θ, φ) is the number of grid patches covering an an-
gular position (θ, φ). By deﬁnition, w thus equals to 1 in the
nonoverlapping region. An integration of this weight func-
tion over the entire surface of all grid patches yields 4π stera-
dian, i.e.
Ng
X
g=1
"
Ωg
dΩ′w(θ′, φ′) = 4π.
(25)
Typically, multi-patch grids in spherical geometry are de-
signed such that each patch is geometrically identical to ease
complications in the implementation of a numerical scheme
on such grids. Meshes are often constructed using coordinate
systems that are local to each grid patch. These local coor-
dinate reference frames are related by rotational transforma-
tion about the common coordinate origin. Evaluation of the
angular parts of the integrations in Eqs. (23) and (24) now
become much more complicated than in the case of a spher-
ical polar grid since each spherical harmonic mode takes a
diﬀerent functional form on each grid patch due to coordi-
nate transformations. Nevertheless, because under rotational
transformation a spherical harmonic of degree ℓand order
m is simply a linear combination of spherical harmonics of
the same degree deﬁned in the rotated reference frame and,
in addition, because each grid patch is geometrically identi-
cal the integrations in Eqs. (23) and (24) can be simpliﬁed
considerably.
Let (r, ϑg, ϕg) be the spherical coordinates of a point r in
a reference frame [ξηζ](g) deﬁned for the construction of the
gth grid patch. Since coordinates in reference frames of all


## Page 5


Generalized 3D gravity solver on a spherical multi-patch grid
5
grid patches transform only by rotations about the coordi-
nate origin the radial coordinate r remains equal for all grid
patches, and is thus denoted without the subscript g. Com-
ponents of the Cartesian coordinates (ξg, ηg, ζg) are related to
the spherical coordinates in the same reference frame by the
usual coordinate transformation,
ξg = r sin ϑg cos ϕg,
(26)
ηg = r sin ϑg sin ϕg,
(27)
and
ζg = r cos ϑg.
(28)
The corresponding inverse transformation reads
r =
q
ξ2g + η2g + ζ2g,
(29)
ϑg = arccos (ζg/r),
(30)
and
ϕg = arctan (ηg/ξg).
(31)
The rotational transformation from the [ξηζ](g) coordinate
system to the [xyz] coordinate system can be decomposed
into three elemental rotations with the amount of rotations
given by the Euler angles αg, βg, and γg. In the z-y′-z′′ con-
vention, the sequence of rotation is a rotation by an angle
αg around the ζg axis, then by an angle βg around the ro-
tated η′
g axis, and ﬁnally by an angle γg around the rotated
ζ′′
g axis (see Fig.1). Correspondingly, the rotational transfor-
mation matrix relating the Cartesian coordinates (ξg, ηg, ζg)
to (x, y, z) is given by
R(g) = Rζ′′g (γg) Rη′g(βg) Rζg(αg)
=

cαgcβgcγg −sαgsγg
sαgcβgcγg + cαgsγg
−sβgcγg
−cαgcβgsγg −sαgcγg −sαgcβgsγg + cαgcγg
sβgsγg
cαgsβg
sαgsβg
cβg

(32)
where we abbreviate cos {αg, βg, γg} and sin {αg, βg, γg} as
c{αg,βg,γg} and s{αg,βg,γg}, respectively, in the above matrix equa-
tion for compactness.
Once the rotation operator is deﬁned relations between
spherical harmonics in the [xyz] and [ξηζ](g) coordinate sys-
tems are given by
Ym
ℓ(θ, φ) =
ℓ
X
m′=−ℓ
Dℓ
m′m(αg, βg, γg)Ym′
ℓ(ϑg, ϕg)
(33)
where coeﬃcients of the linear combinations are elements
of the Wigner D-matrix, Dℓ
m′m (Wigner 1931).
Naturally,
the Wigner D-matrix is a function of the three Euler angles
characterizing the rotational transformation between the two
coordinate systems. With the rotational transformation de-
ﬁned using the z-y′-z′′ convention, elements of the Wigner
D-matrix are expressed as 1
Dℓ
m′m(α, β, γ) = e−im′α · dℓ
m′m(β) · e−imγ
(34)
with the reduced Wigner d-matrix, dℓ
m′m given by
dℓ
m′m(β) =
p
(ℓ−m)! (ℓ+ m)! (ℓ−m′)! (ℓ+ m′)!
×
smax
X
s=0
"
(−1)ℓ−m−s
s! (m + m′ + s)! (ℓ−m −s)! (ℓ−m′ −s)!
·

cos β
2
2s+m+m′ 
sin β
2
2ℓ−m−m′−2s#
.
(35)
The summation index s is an integer starting from 0 to smax
which is set by smax = min (ℓ−m, ℓ−m′) such that argu-
ments of the factorials in the denominator are always posi-
tive.
However, care must be taken when evaluating dℓ
m′m(β) nu-
merically. Computation of dℓ
m′m(β) directly using Eq. (35)
is known to suﬀer from serious loss of precision at high de-
gree ℓdue to cancellation of terms consisting of huge ﬂoat-
ing point numbers (Tajima 2015). To circumvent this prob-
lem we calculate dℓ
m′m(β) by Fourier decomposition, which
results from factorization of the second elemental rotation of
the transformation (Edmonds 1964). The reduced Wigner-d
matrix dℓ
m′m(β) of any angle β can be computed by (Trapani
& Navaza 2006)
dℓ
m′m(β) = im−m′
ℓ
X
u=−ℓ
dℓ
um′( π
2)dℓ
um( π
2)eiuβ.
(36)
with the Fourier coeﬃcients computed by utilizing recur-
rence formulae
dℓ
ℓ0( π
2) = −
r
2ℓ−1
2ℓ
d(ℓ−1)
(ℓ−1)0( π
2),
(37)
dℓ
ℓm( π
2) = −
s
ℓ(2ℓ−1)
2(ℓ+ m)(ℓ+ m −1) · d(ℓ−1)
(ℓ−1)(m−1)( π
2),
(38)
and
dℓ
m′m( π
2) =
2m
√(ℓ−m′)(ℓ+ m′ + 1)
· dℓ
(m′+1)m( π
2)
−
s
(ℓ−m′ −1)(ℓ+ m′ + 2)
(ℓ−m′)(ℓ+ m′ + 1)
· dℓ
(m′+2)m( π
2).
(39)
The starting condition for these recursions, i.e. the apex of
the dℓ
m′m( π
2) matrix pyramid, is given by d0
00( π
2) = 1.
We proceed in our derivation by taking the complex conju-
gate of Eq. (33), and then substituting the result in Eqs. (23)
1 A number of diﬀerent notations of the Wigner D-matrix are used in the
literature. Here, we adopt the same notation as in Morrison & Parker (1987)
where Dℓ
m′m(α, β, γ) is equal to Dℓ
m′m(−α, −β, −γ) with the notation that is
employed in the original work by Wigner (1931).


## Page 6


6
A. Wongwathanarat
and (24). The functions Aℓm and Bℓm now take the forms
Aℓm(r) =
1
rℓ+1
Ng
X
g=1
ℓ
X
m′=−ℓ
h
Dℓ
m′m(αg, βg, γg)
i∗
×
"
Ωg
dω′
gw(ϑ′
g, ϕ′
g)Ym ∗
ℓ(ϑ′
g, ϕ′
g)
r
Z
0
dr′(r′)ℓ+2ρ(r′)
(40)
and
Bℓm(r) = rℓ
Ng
X
g=1
ℓ
X
m′=−ℓ
h
Dℓ
m′m(αg, βg, γg)
i∗
×
"
Ωg
dω′
gw(ϑ′
g, ϕ′
g)Ym ∗
ℓ(ϑ′
g, ϕ′
g)
∞
Z
r
dr′(r′)1−ℓρ(r′)
(41)
where dωg = sin ϑg dϑg dϕg. It is important to note that,
along with the transformation of spherical harmonics, the an-
gular integrals on each grid section in Eqs. (40) and (41) have
also been transformed into integrals in the [ξηζ](g) coordinate
system that is local to each grid patch. This coordinate trans-
formation will allow us to fully exploit the symmetry prop-
erty of the grid conﬁguration when we evaluate these angular
integrals numerically.
Inserting these results into Eq. (2), and using identities for
the reduced Wigner d-matrix (Edmonds 1964)
dℓ
−m′−m(β) = (−1)m′−mdℓ
m′m(β),
(42)
dℓ
−m′m(β) = (−1)ℓ+mdℓ
m′m(π −β),
(43)
and the identity in Eq. (6) for the associated Legendre poly-
nomials to eliminate terms containing spherical harmonics
with a negative order, we obtain, after algebraic rearrange-
ment, an expression for the gravitational potential
Φ(r) = −G
∞
X
ℓ=0
ℓ
X
m=0
s
(ℓ−m)!
(ℓ+ m)!Pm
ℓ(cos θ)
· cos (mφ)Iℓm(r) + sin (mφ)Jℓm(r) .
(44)
The functions Iℓm and Jℓm expand into
Iℓm(r) = K(ℓm)
CC (r) + K(ℓm)
CS (r) + L(ℓm)
CC (r) + L(ℓm)
CS (r)
(45)
and
Jℓm(r) = K(ℓm)
S S (r) −K(ℓm)
SC (r) + L(ℓm)
S S (r) −L(ℓm)
SC (r)
(46)
with the deﬁnitions
K↕⇕
(ℓm)(r) =
1
rℓ+1
Ng
X
g=1
ℓ
X
m′=0
N(ℓmm′)
↕⇕,g
r
Z
0
dr′(r′)ℓ+2 P(ℓm′)
⇕,g (r′)
(47)
and
L↕⇕
(ℓm)(r) = rℓ
Ng
X
g=1
ℓ
X
m′=0
N(ℓmm′)
↕⇕,g
∞
Z
r
dr′(r′)1−ℓP(ℓm′)
⇕,g (r′) (48)
where each of the symbols ↕and ⇕represent modes C or S .
The integrands P(ℓm′)
C,g
and P(ℓm′)
S,g
are deﬁned by
P(ℓm′)
C,g (r) =
"
Ωg
dωgw(ϑg, ϕg)Pm′
ℓ(cos ϑg) cos (m′ϕg)ρ(r),
(49)
and
P(ℓm′)
S,g (r) =
"
Ωg
dωgw(ϑg, ϕg)Pm′
ℓ(cos ϑg) sin (m′ϕg)ρ(r).
(50)
And ﬁnally, the four modes normalization factors N(ℓmm′)
CC,g ,
N(ℓmm′)
CS,g
N(ℓmm′)
S S,g , and N(ℓmm′)
SC,g
are given by
N(ℓmm′)
CC,g
=
2
λm′m
s
(ℓ−m′)!
(ℓ+ m′)!
n
cos (mγg + m′αg) · dℓ
m′m(βg)
+ µm′(−1)ℓ+m+m′ cos (mγg −m′αg) · dℓ
m′m(π −βg)
o
,
(51)
N(ℓmm′)
CS,g
=
2
λm′m
s
(ℓ−m′)!
(ℓ+ m′)!
n
sin (mγg + m′αg) · dℓ
m′m(βg)
−µm′(−1)ℓ+m+m′ sin (mγg −m′αg) · dℓ
m′m(π −βg)
o
,
(52)
N(ℓmm′)
S S,g
= 2µm
λm′m
s
(ℓ−m′)!
(ℓ+ m′)!
n
cos (mγg + m′αg) · dℓ
m′m(βg)
−µm′(−1)ℓ+m+m′ cos (mγg −m′αg) · dℓ
m′m(π −βg)
o
,
(53)
and
N(ℓmm′)
SC,g
= 2µm
λm′m
s
(ℓ−m′)!
(ℓ+ m′)!
n
sin (mγg + m′αg) · dℓ
m′m(βg)
+ µm′(−1)ℓ+m+m′ sin (mγg −m′αg) · dℓ
m′m(π −βg)
o
(54)
with the coeﬃcients
λm′m =

2,
if m = m′ = 0,
1,
otherwise
(55)
and
µm =

0,
if m = 0,
1,
otherwise.
(56)
It is worth noting that the expression for the gravitational
potential on a spherical polar grid derived in Section 2 (Eq. 7)
can easily be recovered by setting Ng = 1 with the Euler
angles αg = βg = γg = 0.
4. IMPLEMENTATION FOR COMPUTATION ON THE
YIN-YANG GRID
In this section, we demonstrate how the algorithm that
we derived in the previous section is applied to compute


## Page 7


Generalized 3D gravity solver on a spherical multi-patch grid
7
ξyin
ζyin
ηyin
ζyin
ξyin
ηyin
ζyin
Figure 2. The Yin-Yang grid conﬁguration as viewed from three diﬀerent directions: along +y-direction (left), +x-direction (middle), and +z-
direction (right). The Yin grid is depicted in red, while the Yang grid is shown with blue color. The grid conﬁguration is rotationally symmetric
with respect to all three viewing axes.
the gravitational potential on the Yin-Yang overset grid con-
ﬁguration. The Yin-Yang grid in its most basic conﬁgura-
tion consists of two geometrically identical overlapping grid
patches. Each grid section, Yin or Yang, is simply the low-
latitude part of the usual spherical polar grid, and therefore
forms an orthogonal grid on the surface of a sphere. For this
particular reason, the algorithm for computation of the grav-
itational potential on the Yin-Yang grid is an easy extension
of the base algorithm derived for the case of a spherical polar
grid in Section 2. A pseudo-algorithm providing guidance
for implementing our new gravity solver is presented in Sec-
tion 4.3.
4.1. Yin-Yang grid orientation and transformations
First of all, we construct the Yin and the Yang grid which
spans the angular ranges
π
4 −∆≤ϑYin/Yang ≤3π
4 + ∆
(57)
and
−3π
4 −∆≤ϕYin/Yang ≤3π
4 + ∆
(58)
in the colatitude and azimuthal directions of their local coor-
dinate reference frames, respectively. The angular resolution
in both coordinate directions on both grid patches is denoted
by ∆. We choose a radial grid which is equidistant with a
radial grid resolution ∆r. It spans the range
Rib ≤r ≤Rob
(59)
where Rib and Rob are the inner and the outer radius of the
computational domain. Transformation rules between Carte-
sian and spherical coordinates are given by Eqs. (26)–(31).
Because the Yin-Yang grid conﬁguration is symmetric Carte-
sian coordinates of a point in both the Yin and the Yang co-
ordinate system are transformed to coordinates of the other
grid patch by a matrix equation of the same form, i.e.

ξYin/Yang
ηYin/Yang
ζYin/Yang

=

−1 0 0
0
0 1
0
1 0


ξYang/Yin
ηYang/Yin
ζYang/Yin

.
(60)
The Yin-Yang coordinate transformation matrix translates
to a rotation about an axis ˆS = (ξYin/Yang, ηYin/Yang, ζYin/Yang) =
(0,
1√
2,
1√
2) by an angle π. Hence, instead of aligning the
[xyz] coordinate reference frame with either the reference
frame of the Yin or the Yang grid we choose to align the po-
lar axis ˆz with the axis ˆS, and deﬁne the relative orientation
of the Yin grid with respect to the [xyz] coordinate reference
frame such that

x
y
z

=

1
0
0
0
1√
2 −1√
2
0
1√
2
1√
2


ξYin
ηYin
ζYin

.
(61)
Transformation of the Yang coordinates to the [xyz] system
can then be obtained by combining Eq. (60) and (61). This
particular choice of orientation results in a grid that possesses
rotational symmetry of order 2 about all coordinate axes of
the [xyz] coordinate system (see Fig. 2).
Once the choice of grid orientation for the Yin-Yang grid
with respect to the [xyz] coordinate system is deﬁned, the
three Euler angles describing the rotational transformation
from the Yin and the Yang coordinate system to the [xyz]
system can be computed by solving trigonometric equations
resulting from Eqs. (32),(60), and (61). This yields
(αYin, βYin, γYin) = (π
2, π
4, 3π
2 )
(62)
and
(αYang, βYang, γYang) = (π
2, π
4, π
2).
(63)
One can see that only the rotation angle γ of the third ele-
mental rotation diﬀers between the two sets of Euler angles.


## Page 8


8
A. Wongwathanarat
As a result, this allows us to simplify calculations of angular
weights necessary for computation of the gravitational poten-
tial by evaluating only one set of weights, either for the Yin
or the Yang grid, and obtain the weights for the other grid
patch by multiplying with a factor 1 or -1. The multiplica-
tion factor depends on the spherical harmonic mode. This
will be demonstrated in the following steps.
4.2. Discretized formulae on the Yin-Yang grid
As in the case of computation on a spherical polar grid
we approximate the density distribution inside a grid cell ijk
on the Yin and the Yang patch by the cell-averaged density
ρi jk,Yin/Yang. In addition,we also truncate the summation se-
ries over spherical harmonics degree at a degree ℓmax, and
an assumption for the weight accounting for overlapping sur-
face area w is applied. When computing surface integrals
we assume a constant weight within an angular grid zone
jk, thereby replacing the weight function w by a surface-
averaged value wjk = 1 −0.5α jk where α jk is the fraction
of overlapping surface area (see e.g., Wongwathanarat et al.
2010, for details).
To calculate the gravitational potential at cell vertices of a
grid zone i jk on the Yin-Yang grid we rewrite the potential
in a compact form as
Φ(r+
i , ϑ+
j,g, ϕ+
k,g) =
ℓmax
X
ℓ=0
ℓ
X
m=0
Q(ℓm)
C, jk,g·M(ℓm)
C,i +Q(ℓm)
S, jk,g·M(ℓm)
S,i . (64)
The gravitational potential expressed in this form reﬂects di-
rectly the actual implementation of the method in our numer-
ical code. The prefactors Q(ℓm)
↕, jk,g are deﬁned by
Q(ℓm)
C,jk,g = −G
s
(ℓ−m)!
(ℓ+ m)!Pm
ℓ(cos θ+
jk,g) cos (mφ+
jk,g)
(65)
and
Q(ℓm)
S,jk,g = −G
s
(ℓ−m)!
(ℓ+ m)!Pm
ℓ(cos θ+
jk,g) sin (mφ+
jk,g)
(66)
where θ+
jk,g = θ(ϑ+
j,g, ϕ+
k,g) and φ+
jk,g = φ(ϑ+
j,g, ϕ+
k,g), both of
which can be computed easily by utilizing coordinate trans-
formations. Furthermore, by coordinate transformation rules
in Eqs. (60) and (61), one ﬁnds that
θ(ϑ+
j,Yang, ϕ+
k,Yang) = θ(ϑ+
j,Yin, ϕ+
k,Yin)
and
φ(ϑ+
j,Yang, ϕ+
k,Yang) = φ(ϑ+
j,Yin, ϕ+
k,Yin) + π.
Thus Q(ℓm)
↕,jk,Yang = (−1)mQ(ℓm)
↕,jk,Yin, thereby allowing us to sim-
ply store only one set of weights in an actual computation.
On the other hand, the radial weights for reconstruction
of the gravitational potential at the nth radial grid interface,
M(ℓm)
↕,i
are computed as
M(ℓm)
↕,i
=
1
(r+
i )ℓ+1
iX
i′=1
R(ℓ)
in,i′B(ℓm)
↕,i′ + (r+
i )ℓ
Nr
X
i′=i+1
R(ℓ)
out,i′B(ℓm)
↕,i′
(67)
with
B(ℓm)
↕,i
=
Yang
X
g=Yin
E(ℓm)
↕,i,g ≡
Yang
X
g=Yin
Nθ
X
j=1
Nφ
X
k=1
ρi jk,gU(ℓm)
↕,jk,g
(68)
and R(ℓ)
in,i′ and R(ℓ)
out,i′ deﬁned by Eqs. (17) and (18). The angu-
lar weights U(ℓm)
↕, jk,g are deﬁned by
U(ℓm)
C,jk,g = w jk
ℓ
X
m′=0

N(ℓmm′)
CC,g C(m′)
k
+ N(ℓmm′)
CS,g S(m′)
k

T (ℓm′)
j
,
(69)
and
U(ℓm)
S, jk,g = w jk
ℓ
X
m′=0

N(ℓmm′)
S S,g S(m′)
k
−N(ℓmm′)
SC,g C(m′)
k

T (ℓm′)
j
(70)
with N(ℓmm′)
↕⇕,g
deﬁned by Eqs.(51–54). It is worth noting that
the surface weights w jk and the integrals T (ℓm′)
j
, C(m′)
k
, and
S(m′)
k
(Eqs.14–16) take the same values on both the Yin and
the Yang grid because of the symmetry of the grid conﬁg-
uration and, in addition, because these angular integrals are
performed using coordinates that are local on each grid patch.
Finally, it is also important to note that both the prefac-
tors Q(ℓm)
↕,jk,g and the angular weights U(ℓm)
↕,jk,g need to be eval-
uated only once at an initialization step. These coeﬃcients
can be re-used to compute the gravitational potential of any
mass distribution represented on the Yin-Yang grid. This is
valid under the assumption that the angular grid remains ﬁxed
throughout the simulation.
4.3. Computation steps
Consider a case in which the Yin-Yang grid is decomposed
only in the angular directions into smaller subdomains. As-
sume that the number of subdomains equals the number of
compute tasks, Ntasks, being used for computation of the grav-
itational potential on a distributed memory system. For this
computational setup the parallelized algorithm to compute
the gravitational potential using Eq. (64) can be summarized
into the following steps:
1. Compute and store prefactors Q(ℓm)
↕,jk,g (Eqs. 65–66) and
angular weights U(ℓm)
↕, jk,g (Eqs. 69–70).
2. Each compute task calculates angular summations
E(ℓm)
↕,i,g = PNθ
j=1
PNφ
k=1 ρi jk,gU(ℓm)
↕,jk,g (Eq. 68).
3. Perform a summation of E(ℓm)
↕,i,g across all compute tasks
to obtain B(ℓm)
↕,i .
4. Each compute task calculates radial summations M(ℓm)
↕,i
(Eq. 67) by using recurrence relations
iX
i′=1
R(ℓ)
in,i′B(ℓm)
↕,i′ = R(ℓ)
in,iB(ℓm)
↕,i
+
i−1
X
i′=1
R(ℓ)
in,i′B(ℓm)
↕,i′
(71)


## Page 9


Generalized 3D gravity solver on a spherical multi-patch grid
9
and
Nr
X
i′=i
R(ℓ)
out,i′B(ℓm)
↕,i′ = R(ℓ)
out,iB(ℓm)
↕,i
+
Nr
X
i′=i+1
R(ℓ)
out,i′B(ℓm)
↕,i′ .
(72)
5. Multiply M(ℓm)
↕,i
with prefactors Q(ℓm)
↕, jk,g and add contri-
butions from all ℓand m moments to reconstruct the
gravational potential.
To ensure consistency of results when computing the sum-
mations in step 2 and 3 in parallel we evaluate these summa-
tions by using the two-sum algorithm (Møller 1965; Knuth
1981). The implementation of the two-sum algorithm for the
summation between compute tasks (step 3) using the Mes-
sage Passing Interface (MPI) library follows that of He &
Ding (2001).
The computation steps summarized above are very similar
to the paralellized algorithm proposed by AMJM18. The dif-
ferences between the two algorithms are as follows: First of
all and most importantly, deﬁnitions of the angular weights
U(ℓm)
↕,jk,g are diﬀerent. In AMJM18, the angular weights are
simply the integrations of spherical harmonics deﬁned in the
Yin or the Yang coordinate system, which are rotated with re-
spect to each other. These weights take similar forms as those
computed for a spherical polar grid, but are multiplied by the
surface weight factor w to account for grid overlaps. Because
of this the radial weights E(ℓm)
↕,i,g for each multipole moment
of the expansion that results from these angular integrations
cannot be directly added into one set of radial weights B(ℓm)
↕,i .
The algorithm of AMJM18 thus computes two sets of poten-
tial from these radial weights in the subsequent steps, and
then these are added together in the ﬁnal computation step.
That is, the gravitational potential is calculated by consider-
ing two sources corresponding to the mass density distribu-
tion on each grid patch separately. On the other hand, the
angular weights U(ℓm)
↕, jk,g derived in our algorithm consider in-
tegrations of spherical harmonics deﬁned in a global coordi-
nate system that is common for all grid patches. These spher-
ical harmonics functions are transformed into linear combi-
nations of spherical harmonics deﬁned in the local coordinate
system of each grid patch, and are integrated. This transfor-
mation is directly reﬂected by the appearance of summations
over all spherical harmonics order m′ in Eqs. (69) and (70).
As a result, our algorithm computes only one set of radial
weights B(ℓm)
↕,i
which is used by all grid patches in subsequent
steps to reconstruct the gravitational potential.
These fundamental diﬀerences lead to an improvement of
the computational eﬃciency of the new gravity solver. It
is easy to see that the operation counts in steps 4 and 5 of
the algorithm are reduced by a factor of two compared with
AMJM18. In addition, the size of data communication be-
tween MPI processes at step 3 decreases by half in compar-
ison to AMJM18. The algorithm by AMJM18 exchanges
2 × Ngrid × Nr × 1
2[(ℓmax + 1)2 + ℓmax + 1] × log2 Ntasks ﬂoating-
point numbers in total, assuming that the recursive doubling
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
−8
−7
−6
−5
−4
ηYin
ξYin
log10(Relative error)
Figure 3. Pseudocolor plot displaying errors of the gravitational po-
tential of a tri-axial ellipsoid of constant density computed on the
Yin-Yang grid conﬁguration relative to the semi-analytic solution in
a cut-plane through the equator of the Yin grid section. The angular
resolution of the Yin-Yang grid is 1◦with 800 equidistant radial grid
zones. The potential is calculated up to a maximum order ℓmax = 80
of the multipole expansion. The black solid line depicts the surface
of the ellipsoid. The relative errors are shown in logarithmic scale.
10−4
10−3
10−2
10−1
0
10
20
30
40
50
60
70
80
This work
AMJM18
Maximum relative error
ℓmax
Figure 4. Maximum error of the gravitational potential of a tri-axial
ellipsoid of constant density computed on the Yin-Yang grid con-
ﬁguration relative to the semi-analytic solution plotted versus the
maximum order of the multipole expansion ℓmax. The angular res-
olution of the Yin-Yang grid is 1◦with 800 equidistant radial grid
zones. Results calculated by using our new algorithm (black solid
line) display excellent agreement with those computed using the al-
gorithm by AMJM18 (red dashed line).
algorithm (Thakur et al. 2005) is used for the global reduc-
tion operation. In contrast, our new method eliminates the
factor Ngrid from the expression.
5. NUMERICAL TEST AND ANALYSIS
5.1. Gravitational potential of a homogeneous ellipsoid
As a test case for our algorithm we calculate the gravita-
tional potential of a homogeneous ellipsoidal body on a Yin-
Yang grid setup with an angular resolution ∆of 1◦and an


## Page 10


10
A. Wongwathanarat
equidistant radial grid of 800 zones. The radius of the inner
and outer grid boundary, Rib and Rob, are set to 0 and 2, re-
spectively. For the purpose of comparison with results com-
puted by AMJM18 we employ the same parameters as listed
in their work for this test setup. The surface of the tri-axial
ellipsoid is deﬁned by the equation
X
a
2
+
Y
b
2
+
Z
c
2
= 1
(73)
with parameters for the semi-axes set to a = 1, b = 1.5 and
c = 2. Coordinates X, Y and Z relate to Cartesian coordinates
in the Yin and the Yang grid system by
X = ξYin cos( π
8) −ηYin sin( π
8)
= −ξYang cos( π
8) −ζYang sin( π
8),
(74)
Y = ξYin sin( π
8) + ηYin cos( π
8)
= −ξYang sin( π
8) + ζYang cos( π
8),
(75)
and
Z = ζYin = ηYang,
(76)
i.e. the shortest principle axis of the ellipsoid is tilted with
respect to the ξ-axis of the Yin grid by an angle π
8. The den-
sity ρ for any given point inside the ellipsoidal surface is set
to ρ0 = 1, while ρ = 0 outside of the ellipsoid.
The analytical solution of the gravitaional potential of this
homogeneous ellipsoidal body is given by (Chandrasekhar
1969). The solution at a point R = (X, Y, Z) reads
Φ(R) = πGρ0abc
h
A(R)X2 + B(R)Y2 + C(R)Z2 −D(R)
i
(77)
with the functions A(R), B(R), C(R) and D(R) deﬁned by
A(R) =
∞
Z
u0(R)
du
h
(a2 + u)3(b2 + u)(c2 + u)
i−1
2 ,
(78)
B(R) =
∞
Z
u0(R)
du
h
(a2 + u)(b2 + u)3(c2 + u)
i−1
2 ,
(79)
C(R) =
∞
Z
u0(R)
du
h
(a2 + u)(b2 + u)(c2 + u)3i−1
2 ,
(80)
and
D(R) =
∞
Z
u0(R)
du
h
(a2 + u)3(b2 + u)(c2 + u)
i−1
2 .
(81)
The value u0 determining the lower limit of the integrations
is u0 = 0 for a point R that lies outside of the ellipsoidal
surface. On the other hand, in the case of a point R inside of
the ellipsoidal surface, u0 is given by the positive root of the
equation
X2
a2 + u0
+
Y2
b2 + u0
+
Z2
c2 + u0
= 1.
(82)
100
101
102
This work
AMJM18
0
0.2
0.4
0.6
0.8
1
1
10
100
Wall-clock time [s]
Scaling eﬃciency
Number of MPI processes
Figure 5.
Averaged wall clock time to solution (top) and strong
scaling eﬃciency (bottom) versus the number of MPI processes for
computation of the gravitational potential on the Yin-Yang grid con-
ﬁguration with 800 radial zones and 1◦angular resolution. Black
and red solid lines show results calculated with our new algorithm
and the algorithm by AMJM18, respectively. Dashed lines represent
the ideal scaling behaviour.
To compute this solution semi-analytically we solve Eq. (82)
for u0 by using the bisection method with the tolerance er-
ror of 10−14. Then, the functions A(R), B(R), C(R) and D(R)
are integrated numerically using the Simpson’s rule as imple-
mented in the Fortran subroutine qsimp (Press et al. 1986).
The upper limit for the integrations is set to 1016, and the inte-
grations are evaluated up to a fractional accuracy of 5×10−14.
Our result for this test is shown in Figure 3, which displays
the color-coded distribution of relative errors in the equato-
rial slice through the Yin-Yang grid. The ﬁgure shows errors
for the case computed with ℓmax = 80. The error distribution
shows a maximum value at the surface of the ellipsoid, which
is marked in Figure 3 by the black solid line to guide the eyes.
This is because of poor representation of the ellipsoidal sur-
face on the Yin-Yang grid with limited spatial resolution. We
also compute the maximum relative error as a function of
ℓmax, and show the results in Figure 4. The maximum rela-
tive error rapidly decreases until it approaches an asymptotic
value at ℓmax ∼70 since the spatial discretization error play
a more dominant role at high values of ℓmax. In addition,
we implemented the algorithm by AMJM18 into our gravity
solver, and perform the same test with their algorithm. As
one can see from the curve of the maximum error versus ℓmax
in Figure 4 our solver shows excellent agreement with the
method by AMJM18 at all values of ℓmax. We observe the
maximum relative diﬀerence between results computed with
our and their algorithm at a level of ∼10−9 only, even at high
values of ℓmax.


## Page 11


Generalized 3D gravity solver on a spherical multi-patch grid
11
Table 1. Averaged wall-clock time for computation of the gravita-
tional potential on the Yin-Yang grid with 800 radial zones and 1◦
angular resolution for diﬀerent number of MPI processes using our
algorithm (second column) and the algorithm by AMJM18 (third
column).
Number of MPI processes
Wall-clock time [s]
This work
AMJM18
1
106.6
159.5
2
53.07
80.02
4
26.04
39.18
8
13.68
20.59
16
7.310
11.10
32
4.283
6.561
64
2.526
4.022
92
1.960
3.164
184
1.340
2.233
368
1.007
1.719
782
0.816
1.553
5.2. Performance and scaling eﬃciency
Table 1 lists the wall-clock time to solution averaged over
20 calculations of the gravitational potential on the Yin-Yang
grid with 1◦angular resolution and 800 radial zones using
diﬀerent numbers of MPI processes.
For comparison we
show both timing data for our method and for our implemen-
tation of the method by AMJM18. The data is also plotted
in Fig. 5 (upper panel) along with the strong scaling eﬃ-
ciency (bottom panel). These numbers are measured using
the Intel Xeon Gold 6148 Processors equipped on the Co-
bra high-performance computing system at the Max Planck
Computing and Data Facility.
Our data shows that by applying our new algorithm for
computation on the Yin-Yang grid using a single CPU core
the computational eﬃciency is increased by about 30% when
compared with the method by AMJM18. A more detailed
analysis of both methods reveals that about 70% of the to-
tal computing time is, in fact, spent to compute the radial
weights E(ℓm)
↕,i,g in step 2 due to additional costs associated with
the usage of the two-sum algorithm. Although the operation
count at this step is equal for both algorithms, we already ob-
serve a 30% gain here. This gain factor results from the fact
that our algorithm computes only one set of radial weights
instead of two sets as required by AMJM18 method. Conse-
quently, the number of load/store instructions in the angular
summation loops, which is the computational bottleneck in
our implementations, is reduced. This demonstrates that it
can be misleading to compare operation counts when gaug-
ing the relative computational eﬃciency between two algo-
rithms.
As we increase the number of MPI compute tasks we begin
to observe beneﬁts from smaller data communication volume
required by our algorithm when compared with the method
by AMJM18. While the scaling eﬃciency of our method is
improved only slightly relative to the algorithm of AMJM18,
the wall-clock time to solution is reduced by almost a fac-
tor of two when using 782 MPI processes with respect to the
method by AMJM18. We also point out that although the
strong scaling eﬃciency we report in this work is very diﬀer-
ent from that which is shown by AMJM18, cross-comparison
of the scaling eﬃciency should be taken with cautions since
it depends strongly on details of how an algorithm is imple-
mented and also on details of the system running the algo-
rithm.
6. DISCUSSIONS AND CONCLUSIONS
In this work, we have presented a generalization of the
multipole expansion based gravity solver by M¨uller & Stein-
metz (1995) for eﬃcient computation of the 3D gravitational
potential on a multi-patch grid conﬁguration in spherical
geometry. We derive explicit formulae of angular and ra-
dial weights for reconstruction of the gravitational potential
by considering integrals of spherical harmonics deﬁned in a
global coordinate system that is common to all subdomains
in the multi-patch grid conﬁguration. These spherical har-
monics functions are transformed into linear combinations
of spherical harmonics deﬁned in the local coordinate refer-
ence frame of each individual grid patch. This transformation
eases complications of having to integrate diﬀerent functions
on diﬀerent grid patches when evaluating these angular and
radial weights numerically. Linear coeﬃcients for the ro-
tational transformation of spherical harmonics are given by
elements of the well-known Wigner D-matrix (Wigner 1931)
that can be evaluated eﬃciently by recursion relations for any
set of Euler angles characterizing the transformation between
the local and global coordinate system.
We have applied our new algorithm for calculations of the
3D gravitational potential on the Yin-Yang overset grid. Val-
idation of our algorithm is done by comparison of the numer-
ical solution to a semi-analytical solution of the gravitational
potential of a tri-axial ellipsoidal body with homogeneous
mass density. For this test we computed using the maximum
degree of the multipole expansion ℓmax of up to 80. At this
value of ℓmax the numerical error of the gravitational poten-
tial is dominated by the spatial discretization error associated
with the chosen grid resolution. It is important to note that a
suitable choice of ℓmax is problem- and resolution dependent.
Judging from our experiences, in 3D simulations of CCSNe,
which is one of the application areas of our new method, an
ℓmax of ∼20 should already be adequate for typical angular
grid resolutions of 1–2 degree.
Our results demonstrate that our algorithm yields a solu-
tion that is as accurate as that obtained by the recent algo-
rithm of AMJM18 proposed for the Yin-Yang grid. Perfor-
mance wise, our algorithm beneﬁts from reduced computa-
tional cost and smaller data communiation volume between
parallel compute tasks, thus yielding a faster gravity solver


## Page 12


12
A. Wongwathanarat
with better parallel scaling eﬃciency in comparison with the
previous method.
Our new algorithm is easy to implement into an exisit-
ing solver that is based on the multipole expansion method
because it involves only minor modiﬁcation to the calcula-
tions of angular weights at an initialization step of the gravity
solver. We present detailed implementation steps of the algo-
rithm for the case of the Yin-Yang grid conﬁguration in Sec-
tion 4.3. These implementation steps can be applied also for
computations on other multi-patch grids in spherical geome-
try. In the case of a non-orthogonal angular grid, computa-
tion of angular weights, which involves integrations of spher-
ical harmonics, are more complicated than the computation
on the Yin-Yang grid conﬁguration that considers orthogo-
nal angular meshes. Nevertheless, these integrations can ei-
ther be approximated or evaluated by numerical integrations.
Once the angular weights are computed, the remaining steps
of the algorithm remain unchanged.
In a future work, we plan to implement this algorithm into
our newly developed high-order ﬁnite-volume hydrodynamic
code, Apsara (Wongwathanarat et al. 2016), which is capable
of dealing with general multi-block structured grids in curvi-
linear coordinates. We also plan to investigate how our algo-
rithm can be re-formulated such that it yields higher-order of
accuracy of the solution.
The author is grateful to Ewald M¨uller for a careful reading
of the manuscript, and to Ninoy Rahman and Tobias Melson
for fruitful discussions. The author thanks also the anony-
mous referee for his/her constructive comments. Computa-
tions are carried out on the Cobra high-performance comput-
ing system at the Max Planck Computing and Data Facility.
Software: VisIt (Childs et al. 2012)
REFERENCES
Almanst¨otter, M., Melson, T., Janka, H.-T., & M¨uller, E. 2018, ApJ, 863,
142
Appel, A. W. 1985, SIAM Journal on Scientiﬁc and Statistical Computing,
vol. 6, no. 1, January 1985, p. 85-103., 6, 85
Barnes, J., & Hut, P. 1986, Nature, 324, 446
Boris, J. P., & Roberts, K. V. 1969, Journal of Computational Physics, 4,
552
Chandrasekhar, S. 1969, Ellipsoidal ﬁgures of equilibrium
Childs, H., Brugger, E., Whitlock, B., et al. 2012, in High Performance
Visualization–Enabling Extreme-Scale Scientiﬁc Insight, 357–372
Couch, S. M., Graziani, C., & Flocke, N. 2013, ApJ, 778, 181
Dubey, A., Antypas, K., Ganapathy, M. K., et al. 2009, Parallel Computing,
35, 512
Edmonds, A. 1964, Drehimpulse in der Quantenmechanik (Mannheim,
Bibliographisches Institut)
Fryxell, B., M¨uller, E., & Arnett, D. 1989, in Nuclear Astrophysics, ed.
M. Lozano, M. I. Gallardo, & J. M. Arias
Fryxell, B., Olson, K., Ricker, P., et al. 2000, ApJS, 131, 273
Glas, R., Just, O., Janka, H.-T., & Obergaulinger, M. 2018, ArXiv e-prints,
arXiv:1809.10146
He, Y., & Ding, C. H. Q. 2001, The Journal of Supercomputing, 18, 259
Hernquist, L., & Katz, N. 1989, ApJS, 70, 419
Hockney, R. 1970, Methods Comput. Phys. 9: 135-211(1970).
Jernigan, J. G. 1985, in IAU Symposium, Vol. 113, Dynamics of Star
Clusters, ed. J. Goodman & P. Hut, 275–283
Kageyama, A., & Sato, T. 2004, Geochemistry, Geophysics, Geosystems, 5,
Q09005
Knuth, D. E. 1981, The Art of Computer Programming, Volume II:
Seminumerical Algorithms, 2nd Edition (Addison-Wesley)
Lentz, E. J., Bruenn, S. W., Hix, W. R., et al. 2015, ApJL, 807, L31
Melson, T., Janka, H.-T., & Marek, A. 2015, ApJL, 801, L24
Møller, O. 1965, BIT Numerical Mathematics, 5, 37
Morrison, M. A., & Parker, G. A. 1987, Australian Journal of Physics, 40,
465
M¨uller, B., & Chan, C. 2018, ArXiv e-prints, arXiv:1806.06623
M¨uller, E., & Steinmetz, M. 1995, Computer Physics Communications, 89,
45
Porter, D. H. 1985, PhD thesis, California Univ., Berkeley.
Press, W. H., Flannery, B. P., Teukolsky, S. A., & Vetterling, W. T. 1986,
Numerical Recipes: The Art of Scientiﬁc Computing (New York, NY,
USA: Cambridge University Press)
Rampp, M., & Janka, H.-T. 2002, A&A, 396, 361
Ricker, P. M. 2008, ApJS, 176, 293
Ronchi, C., Iacono, R., & Paolucci, P. S. 1996, Journal of Computational
Physics, 124, 93
Summa, A., Janka, H.-T., Melson, T., & Marek, A. 2018, ApJ, 852, 28
Tajima, N. 2015, PhRvC, 91, 014320
Thakur, R., Rabenseifner, R., & Gropp, W. 2005, The International Journal
of High Performance Computing Applications, 19, 49
Trapani, S., & Navaza, J. 2006, Acta Crystallographica Section A, 62, 262
Vartanyan, D., Burrows, A., Radice, D., Skinner, M. A., & Dolence, J.
2019, MNRAS, 482, 351
Wigner, E. 1931, Gruppentheorie und ihre Anwendung auf die
Quantenmechanik der Atomspektren, Wissenschaft (Braunschweig,
Germany) (J.W. Edwards)
Wongwathanarat, A., Grimm-Strele, H., & M¨uller, E. 2016, A&A, 595,
A41
Wongwathanarat, A., Hammer, N. J., & M¨uller, E. 2010, A&A, 514, A48
Wongwathanarat, A., Janka, H.-T., M¨uller, E., Pllumbi, E., & Wanajo, S.
2017, ApJ, 842, 13
W¨unsch, R., Dinnbier, F., Walch, S., & Whitworth, A. 2018, MNRAS, 475,
3393
Zwerger, T. 1995, PhD thesis, PhD Thesis, TechnischeUniversit¨at
M¨unchen, (1995)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1903_08475v1_a_generalized_solution_method_for_parallelized_computation_of_the_three_dimensio
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1903_08475V1_A_GENERALIZED_SOLUTION_METHOD_FOR_PARALLELIZED_COMPUTATION_OF_THE_THREE_DIMENSIO.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

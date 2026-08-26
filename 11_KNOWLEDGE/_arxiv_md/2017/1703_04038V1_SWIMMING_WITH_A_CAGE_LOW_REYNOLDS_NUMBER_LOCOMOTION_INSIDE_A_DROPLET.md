---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1703.04038v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1703.04038v1_Swimming_with_a_cage__Low-Reynolds-number_locomotion_inside_a_droplet

> Source: 1703.04038v1_Swimming_with_a_cage__Low-Reynolds-number_locomotion_inside_a_droplet.pdf

> Pages: 26

---


## Page 1


Swimming with a cage: Low-Reynolds-number locomotion inside a droplet
Shang Yik Reigh,1, 2, ∗Lailai Zhu,3, 4, † François Gallaire,3, ‡ and Eric Lauga1, §
1Department of Applied Mathematics and Theoretical Physics,
Center for Mathematical Science, University of Cambridge,
Wilberforce Road, Cambridge CB3 0WA, United Kingdom
2Max-Plank-Institut für Intelligente Systeme,
Heisenbergstraße 3, 70569 Stuttgart, Germany
3Laboratory of Fluid Mechanics and Instabilities,
Ecole Polytechnique Fédérale de Lausanne, Lausanne, CH-1015, Switzerland
4Current address: Linné Flow Centre and Swedish e-Science Research Centre (SeRC), KTH Mechanics,
SE-100 44 Stockholm, Sweden; Department of Mechanical and Aerospace Engineering,
Princeton University, Princeton, NJ-08544, USA.
Abstract
Inspired by recent experiments using synthetic microswimmers to manipulate droplets, we investigate the
low-Reynolds-number locomotion of a model swimmer (a spherical squirmer) encapsulated inside a droplet of
comparable size in another viscous ﬂuid. Meditated solely by hydrodynamic interactions, the encaged swimmer
is seen to be able to propel the droplet, and in some situations both remain in a stable co-swimming state. The
problem is tackled using both an exact analytical theory and a numerical implementation based on boundary
element method, with a particular focus on the kinematics of the co-moving swimmer and droplet in a con-
centric conﬁguration, and we obtain excellent quantitative agreement between the two. The droplet always
moves slower than a swimmer which uses purely tangential surface actuation but when it uses a particular
combination of tangential and normal actuations, the squirmer and droplet are able to attain a same veloc-
ity and stay concentric for all times. We next employ numerical simulations to examine the stability of their
concentric co-movement, and highlight several stability scenarios depending on the particular gait adopted by
the swimmer. Furthermore, we show that the droplet reverses the nature of the far-ﬁeld ﬂow induced by the
swimmer: a droplet cage turns a pusher swimmer into a puller, and vice versa. Our work sheds light on the
potential development of droplets as self-contained carriers of both chemical content and self-propelled devices
for controllable and precise drug deliveries.
∗reigh@is.mpg.de
† lailai.zhu@epﬂ.ch
‡ francois.gallaire@epﬂ.ch
§ e.lauga@damtp.cam.ac.uk; S. Y. Reigh and L. Zhu contributed equally to this work.
1
arXiv:1703.04038v1  [cond-mat.soft]  11 Mar 2017


## Page 2


I.
Introduction
Droplets have recently been used as small, isolated, aqueous compartments to encapsulate, incu-
bate and manipulate cells for biological assays [1]. Such droplet-based cell encapsulation is com-
monly accomplished in microﬂuidic devices which are able to precisely produce and manipulate mi-
crodroplets of adjustable sizes[2, 3]. Current microﬂuidic technology allows a high-throughput and
controllable analysis to be performed on individual cells in their own discrete microenvironments.
In related work, droplets have been used to cage motile organisms such as the nematode Caenorhab-
ditis elegans (C. elegans)[4, 5] in order to carry out developmental work. In these studies, the size of
an encaged adult C. elegans is comparable to the droplet radius. Despite their mobility, the worms
failed to propel their liquid cages, because they were immobilized. In the work of Ref. [4], the droplet
was tightly squeezed inside a capillary tube, forming a plug thus immobilized hydrodynamically by the
lubrication ﬁlm while in the work of Ref. [5], the droplet was anchored mechanically by a microﬂuidic
trap.
Motivated by these droplet-based encapsulations of motile organisms, we raise in this paper a sim-
ple question: is it possible for a microswimmer encaged in a droplet to propel its viscous cage and
co-swim with it? One could envision setups of this type of interest to the drug delivery community us-
ing droplets as small self-contained units propelled and steered by their internal synthetic swimmers.
Recently, microrobots propelled by a magnetically-rotated helical appendage mimicking the ﬂagella
of bacteria such as Escherichia coli (E. coli) were fabricated[6, 7], encapsulated and operated inside
a water-in-oil droplet in microﬂuidic chips[8]. In this case, the droplets were not mobile, presum-
ably for two reasons: the swimmer was much smaller than the droplet and the droplet was large
compared to the height of the micro-ﬂuidic chips so that it was tightly squeezed and thus anchored
hydrodynamically[4]. Excitingly, the same group managed however to use their microrobots to push
a droplet of comparable size from the exterior when the droplet was unbounded or loosely bounded.
In this paper, we conduct a combined theoretical and numerical study of a three-dimensional (3D)
model microswimmer encapsulated in a droplet in free space. The size of the swimmer is of the same
order as the radius of the droplet and we attempt to answer the following fundamental questions:
Will the droplet co-swim with the swimmer? What is the swimming velocity of the droplet compared
to that of the swimmer? How are the kinematics and energetics of the microswimmer affected by the
conﬁnement due to the presence of the droplet? How stable is the co-movement of the concentric pair
of swimmer and droplet?
2


## Page 3


II.
Problem description
We consider, in the creeping-ﬂow regime, the locomotion of a 3D microswimmer encapsulated in a
droplet. Due to hydrodynamic interactions, the motion of the swimmer is inﬂuenced by the presence
of the droplet interface. The geometrical setup is shown in Fig. 1a. We use a spherical, axisymmetric
squirmer[9, 10] as our model swimmer.
It achieves locomotion by squirming, i.e. by generating
tangential and/or normal velocities on its ﬁxed spherical surface. This is a classical model for physical
actuation of microorganisms continuously deforming their bodies or beating their densely-packed
cilia, and has been employed in the past to address a variety of biophysical aspects of locomotion[11–
18]. The shape of the droplet is maintained as spherical by maintaining a sufﬁciently large surface
tension γ on its interface, i.e. we assume to remain in the low-Capillary number limit. The radius of
the squirmer is denoted by a while that of the droplet is b > a, respectively, and χ = b/a > 1 is the
size ratio. The ﬂuid phases inside and outside the droplet are marked as phase 1 and 2. Both are
Newtonian, with dynamic viscosities of µ(1) and µ(2), and λ = µ(2)/µ(1) denotes the viscosity ratio.
Both Cartesian (x,y,z) and spherical (r,θ,φ) coordinate systems are used, shown in Fig. 1b.
We then solve the steady Stokes equations for ﬂuid phase 1 and 2,
∇pß = µ(i)∇2vß,
∇·vß = 0,
(1)
where pß is the dynamic pressure and vß the ﬂuid velocity in phase (i), where i = 1 or 2. Following
classical work[9, 10], we impose normal and/or tangential squirming velocities on the surface of
the swimmer r = a to represent its effective swimming motion. These velocities are assumed to be
time-independent and axisymmetric about its swimming direction, i.e., the z axis passing through the
centers of the squirmer and droplet. The squirmer drives the droplet to co-swim in the same direction,
and hence the problem is fully axisymmetric about the z axis. The velocity of the swimmer and droplet
are denoted by US and UD respectively.
In the laboratory frame of reference, the ﬂuid velocity components v(1) = (v(1)
r ,v(1)
θ ) on the swimmer
surface, r = a, are given by
v(1)
r |r=a =
∞
∑
n=0
AnPn(ξ)+USP1(ξ),
v(1)
θ |r=a =
∞
∑
n=1
BnVn(ξ)−USV1(ξ),
(2)
where An (respectively Bn) indicates the n-th mode of the normal (respectively tangential) squirming
3


## Page 4


θ
a
b
(a)
(b)
z
x
US
UD
Phase 1
Phase 2
µ(1)
µ(2)
z
x
y
Figure 1 (a) Three-dimensional sketch of a spherical swimmer of radius a (green) inside a spherical droplet of
radius b (magenta). (b) The squirmer and the droplet co-swim in the z direction with a velocity of US and UD,
respectively. The ﬂuids inside and outside the droplet are marked as phase 1 and phase 2 and are
distinguished by their viscosity µ(1) and µ(2), respectively.
velocities, Pn are the Legendre polynomial, ξ ≡cosθ, Vn = −2P1
n (ξ)/(n2 +n), and P1
n is the associated
Legendre function of the ﬁrst kind of order 1. In Eq. (2), US is the value of the unknown swimming
velocity of the swimmer, and UD is the unknown swimming speed of the droplet.
On the droplet interface r = b, the normal velocities in the droplet frame vanishes because the
droplet does not deform. In addition, the tangential velocities and tangential stresses are continuous
across the interface. These boundary conditions formulated in the laboratory frame are written as
v(1)
r |r=b = v(2)
r |r=b = UD cosθ,
v(1)
θ |r=b = v(2)
θ |r=b,
Π(1)
rθ |r=b = Π(2)
rθ |r=b,
(3)
4


## Page 5


where Πß = −pßI + µ(i) h
∇vß+(∇vß)Ti
is the stress tensor for ﬂuid i. Furthermore, the velocity v(2)
decays to zero in the far ﬁeld r ≫b.
Finally, the total hydrodynamic forces exerted on both the swimmer and on the droplet interface
are zero, which will be used to determine the values of both swimming velocities, US and UD. For an
unbounded squirmer in a single-phase ﬂuid, the velocity US ≡U0 is given by[9, 10]
U0 = 2B1 −A1
3
·
(4)
III.
Analytical theory
We ﬁrst solve the problem analytically. The methodology is based on Lamb’s general solution of the
Stokes equations in spherical coordinates[19, 20]. For a single-phase ﬂuid with viscosity µ, the ﬂuid
velocity ﬁeld v can be expanded in spherical harmonics as
v =
∞
∑
n=−∞
h
∇φn +
n+3
2µ(n+1)(2n+3)r2∇pn −
n
µ(n+1)(2n+3)rpn
i
,
(5)
where pn and φn are solid spherical harmonics satisfying ∇2pn = 0 and ∇2φn = 0, respectively. In
axisymmetric ﬂow, pn and φn are expressed by a series of Legendre functions as
pn(r,ξ) = ˜pnrnPn(ξ),
φn(r,ξ) = ˜φnrnPn(ξ),
where ˜pn and ˜φn are constants independent of r and ξ.
The radial and tangential velocity components vr and vθ are then obtained as
vr =
∞
∑
n≥0
h
¯pnrn+1 + ¯φnrn−1 + ¯p−(n+1)r−n + ¯φ−(n+1)
1
rn+2
i
Pn(ξ),
vθ =
∞
∑
n≥1
h
−n+3
2
¯pnrn+1 −n+1
2
¯φnrn−1 + n−2
2
¯p−(n+1)r−n + n
2
¯φ−(n+1)r−(n+2)i
Vn(ξ),
(6)
where
¯pn =
n
2µ(2n+3) ˜pn,
¯φn = n ˜φn.
Note that the solution for the ﬂow in region 1 may contain all terms in the brackets of Eq. (6) while
those in region 2 only contain the last two terms due to the boundary condition at inﬁnity.
Applying this framework to our case, we use Eq. 6 for both the inner and outer ﬂuid, solving for the
5


## Page 6


unknown constants ¯pnß, ¯φnß, ¯p(i)
−(n+1) and ¯φ(i)
−(n+1) (i = 1,2) using the boundary conditions, Eqs. 2-3,
together with the condition at inﬁnity. Taking the n = 0,1 terms in the series expansion of Eq. (6) with
the use of Eqs. 2-3 leads to the system for the inner ﬂuid
¯p(1)
−1 + 1
a2 ¯φ(1)
−1 = A0,
¯p(1)
−1 + 1
b2 ¯φ(1)
−1 = 0,
a2 ¯p(1)
1 + ¯φ(1)
1
+ 1
a ¯p(1)
−2 + 1
a3 ¯φ(1)
−2 = A1 +US,
−2a2 ¯p(1)
1 −¯φ(1)
1
−1
2a ¯p(1)
−2 + 1
2a3 ¯φ(1)
−2 = B1 −US,
b2 ¯p(1)
1 + ¯φ(1)
1
+ 1
b ¯p(1)
−2 + 1
b3 ¯φ(1)
−2 = UD,
(−2−1
λ )b2 ¯p(1)
1 −¯φ(1)
1
−1
2b ¯p(1)
−2 +(1
2 −1
λ ) 1
b3 ¯φ(1)
−2 = −1
2UD.
(7)
Hence, the constants ¯p(1)
n
and ¯φ(1)
n
(n = −2,−1 and 1) are obtained explicitly in terms of both US and
UD. The constants in the outer ﬂuid are then given by
¯p(2)
−2 = 1
b2 ¯φ(2)
−2 +bUD,
¯φ(2)
−2 = 1
λ

b5 ¯p(1)
1 + ¯φ(1)
−2

,
(8)
and the condition at inﬁnity leads trivially to ¯p(2)
−1 = 0 and ¯φ(2)
−1 = 0.
Applying the force-free condition for the swimmer, we have
F =
Z
ˆS Π(1) · ˆrdS = −4π∇
h
r3p(1)
−2
i
= 0,
(9)
which leads to ¯p(1)
−2 = 0. Applying the same condition for the droplet, we obtain ¯p(2)
−2 = 0. Plugging
the two constants into Eq. 7, we obtain the values of all underdetermined constants together with the
velocity of the swimmer, US, and that of the droplet, UD, as,
US = Ξ1λ +Ξ2
∆
,
(10)
and
UD = 10(A1 +B1)χ2
∆
,
(11)
6


## Page 7


where
Ξ1 = 2(2B1 −A1)χ5 −10(A1 +B1)χ2 +6(2A1 +B1),
Ξ2 = 3(2B1 −A1)χ5 +10(A1 +B1)χ2 −6(2A1 +B1),
∆= 3
h
2(χ5 −1)λ +3χ5 +2
i
.
(12)
Similarly to case of an unbounded squirmer (see Eq. 4), the swimming velocities US and UD are seen
to be independent of the squirming modes An or Bn for n ≥2, but depend only on A1 and B1.
In order to complete the calculation and charactarize the ﬂow in both ﬂuids, we need to calculate
the values of the constants ¯pn, ¯φn, ¯p−(n+1) and ¯φ−(n+1) for n ≥2 in the series expansion from Eq. (6).
The velocities inside and outside the droplet in the laboratory frame are then obtained to be
v(1)
r
=
A0
χ2 −1
n
χ2a
r
2
−1
o
P0(ξ)+ A1 +B1
∆
n
6(λ −1)
r
a
2
−10(λ −1)χ2 +2(2λ +3)χ5a
r
3o
P1(ξ)
+
∞
∑
n=2
1
∆n
n
(N1An +N2Bn)
r
a
n+1
+(N3An +N4Bn)
r
a
n−1
+(N5An +N6Bn)
a
r
n
+(N7An +N8Bn)
a
r
n+2o
Pn(ξ),
v(1)
θ
= −A1 +B1
∆
n
12(λ −1)
r
a
2
−10(λ −1)χ2 −(2λ +3)χ5a
r
3o
V1(ξ)
+
∞
∑
n=2
1
∆n
n
−n+3
2
(N1An +N2Bn)
r
a
n+1
−n+1
2
(N3An +N4Bn)
r
a
n−1
+ n−2
2
(N5An +N6Bn)
a
r
n
+ n
2(N7An +N8Bn)
a
r
n+2o
Vn(ξ),
v(2)
r
= 10(A1 +B1)χ5
∆
a
r
3
P1(ξ)−
∞
∑
n=2
c1An +c2Bn
∆n
n 1
χ2
a
r
n
−
a
r
n+2o
Pn(ξ),
v(2)
θ
= 5(A1 +B1)χ5
∆
a
r
3
V1(ξ)−
∞
∑
n=2
c1An +c2Bn
2∆n
nn−2
χ2
a
r
n
−n
a
r
n+2o
Vn(ξ),
(13)
where the values of all undeﬁned constants are provided in Appendix A.
We can ﬁnally calculate the power consumption of the squirmer, P, which is equal to rate of
working done by the squirmer on the ﬂuid,
P = −
Z
ˆS v(1) ·Π(1) ·n ˆSdS,
(14)
7


## Page 8


where n ˆS denotes the normal vector on ˆS pointing towards the ﬂuid. We obtain
P
4πµ1a =

22χ2 +1
χ2 −1 A2
0 +2(Z1 +Z2)Z3
(A1 +B1)2
∆2
+
∞
∑
n≥2
1
(2n+1)∆2n

2

anNoA2
n +bnNeB2
n +(anNe +bnNo)AnBn

+
4
n(n+1)

cn ¯NoA2
n +dn ¯NeB2
n +(cn ¯Ne +dn ¯No)AnBn

+C0A0,
(15)
where C0 is given in terms of the surface tension of the droplet, γ, as C0 = {γ −µ(2)A0(2χ2 +1)/(χ2 −
1)}/(πµ(1)a2χ) based on the condition Π(2)
rr −Π(1)
rr = 2γ/b. Again, all undeﬁned constants are given in
Appendix A.
IV.
Numerical simulations
In parallel with our theoretical approach, we use numerical simulations based on a 3D boundary
element method. By choosing the characteristic length, velocity, and stress as b, λγ/{µ(2)(1+λ)}, and
γ/b respectively, the nondimensional boundary integral formulation for the matching-viscosity case
(λ = 1) can be obtained. The nondimensional velocity u(x0) at position x0 everywhere in the domain
is classically written as
u(x0) = 1
2π
Z
˜S κ(x)n(x)·G(x0,x)dS(x)−1
4π
Z
ˆS q(x)·G(x0,x)dS(x),
(16)
where ˜S and ˆS denote the surface of the droplet and swimmer respectively, n the normal vector on ˜S
towards the outer ﬂuid, κ = −1
2∇s · n the mean curvature of ˜S, and q the density of the single-layer
potential on ˆS. The tensor G is the free-space Green’s function, also known as the Stokeslet or the
Oseen-Burgers tensor,
G(x0,x) = δ
r + (x0 −x)(x0 −x)
r3
,
(17)
where δ is identity tensor and r = |x0 −x|. As shown in Eq. 16, only single-layer integration is per-
formed, which is sufﬁcient for the rigid body motion of the swimmer and the dynamics of a matching-
viscosity droplet[21].
The surfaces of the swimmer and droplet are discretized using zero-order ﬂat quadrilateral and
second-order curved triangular elements respectively. For the spherical swimmer, a six-patch struc-
8


## Page 9


z
x
y
y
x
z
x
(a)
(b)
(c)
Figure 2 Meshing of the swimmer-droplet pair used in numerical simulations: (a) The 3D view of the meshes
of the droplet (triangular elements) and swimmer (quadrilateral elements), where adaptive mesh reﬁnement is
implemented on the swimmer; half of the droplet interface is removed for visualisation purposes. (b) The
projection view on the xy plane. (c) The projection view on the xz plane.
tured mesh[22, 23] consisting of 600 (before mesh reﬁnement) elements is constructed. The number
of elements on the droplet interface is around 2500 (∼5000 discretized points).
Gauss-Legendre
quadrature is applied on the quadrilateral elements to compute nonsingular integrations; on triangu-
lar elements, we compute the integrations using a symmetric Gaussian quadrature rule[24]. When x0
is on the surfaces ˜S or ˆS, the surface integrals become singular and different desingularization strate-
gies are chosen: on the droplet interface ˜S, the well-known integral identity for G is exploited and
hence the ﬁrst integral in Eq. 16 becomes
Z
˜S κ(x)n(x)·G(x0,x)dSx =
Z
˜S[κ(x)−κ(x0)]n(x)·G(x0,x)dSx,
(18)
where the O(r−1) singularity of the original integrand is removed; on the squirmer surface ˜S,
each quadrilateral element is divided into four triangular sub-elements, where polar coordinates
transformation[25] with Gauss-Legendre quadrature is adopted to desingularize the integral. Both
integrals in Eq. 16 tend to be nearly singular when the distance between the two surfaces ˜S and ˆS
is too small. Desingularizing measures are hence taken for them: on the droplet interface ˜S, a high-
order near-singularity subtraction is implemented by following Ref. [26] and on the swimmer surface
ˆS, adaptive mesh reﬁnement is utilized. Figure 2 presents a schematic view of the adaptively-reﬁned
9


## Page 10


mesh.
A crucial numerical difﬁculty arising from droplet/bubble simulations based on Lagrangian inter-
face representation is to maintain the quality of the mesh of the interface. In order to guarantee
the smoothness and orthogonality of the triangle mesh over a long time evolution, we implement a
so-called ‘passive mesh stabilization’ scheme [27, 28]. At each time step, the scheme searches the
optimal tangential ﬁeld that is added to the normal velocity to update the Lagrangian points, min-
imizing a global kinetic-energy-like norm that quantiﬁes the clustering and distortion of the mesh.
This scheme signiﬁcantly slows down mesh degradation. Its effectiveness was proved in the previous
study on a squeezed pancake droplet in a microﬂuidic chip based on an accelerated boundary integral
implementation[29].
In contrast to the inﬁnite-surface tension assumed in the theory, a large but ﬁnite surface tension
is adopted in the simulations and hence the numerical droplet is not strictly spherical but slightly
deformable. The strength of the typical ratio of viscous stresses to surface tension forces is measured
by the capillary number, Ca ≡µ(2)B1/γ, and Ca = 0 corresponds to the theoretical limit of inﬁnite
surface tension. We vary Ca numerically from 10−3 to 10−2, without detecting signiﬁcant changes
in the kinematics of the swimmer. We hence use Ca = 10−3 throughout our study, and are able to
approximate well the Ca = 0 limit from our a posteriori comparison with the theory.
V.
Results
A.
Squirming with purely tangential velocities
In this section, we start by investigating the instantaneous dynamics of a droplet encapsulating a
squirmer using solely tangential surface velocities, i.e. with An = 0. If one further sets the Bn (n ≥3)
modes to zero, as is classically done for the squirmer model [12], the swimming gait consists of only
B1 and B2 modes: the B1 mode determines the swimming velocity while the B2 mode captures the
leading order disturbance ﬂow induced by the swimmer, namely a stresslet (or force dipole). We deﬁne
β ≡B2/B1 to measure the relative strength of the stresslet. The squirmer is said to be neutral when
β = 0, while it is a pusher (respectively a puller) when β is negative (respectively positive). Varying the
value of β allows to model the majority of swimming microorganisms and synthetic microswimmers:
pushers model ﬂagellated bacteria such as E. coli [30] while biﬂagellated green algae such as C.
reinhardtii[31–33] are pullers. Neutral swimmers may be considered as special cases of synthetic
swimmers such as Janus particles self-propelling owing to various phoretic mechanisms or some active
droplets driven by Marangoni stresses[34–41].
10


## Page 11


(a)
(b)
US/U0
λ = 0.1
λ = 1
λ = 10
λ = 3
λ = 5
UD/U0
UD/US
λ
Figure 3 (a): Velocity US of the swimmer squirming with tangential surface actuation only; (b): Velocity UD of
the droplet, scaled by that of an unbounded squirmer, U0 = 2B1/3. In both cases, the velocities are plotted as
a function of the size ratio, χ = b/a for viscosity ratios λ = 0.1, 1, 3, 5 and 10. The inset of (b) shows the ratio,
UD/US, of the droplet velocity over the swimmer velocity in log-log form.
1.
Velocity of the swimmer and droplet: theory
For a tangential squirmer, the velocities US and UD are given analytically by
US
U0
= 3
∆{(2χ5 −5χ2 +3)λ +3χ5 +5χ2 −3},
UD
U0
= 15χ2
∆
,
(19)
where ∆is deﬁned in Eq. 12 and we use the swimming velocity U0 of an unbounded squirmer as the
reference scale, U0 = 2B1/3. Both velocities are functions solely of the size ratio, χ, and the viscosity
ratio, λ.
We plot in Fig. 3a the dependence of the swimmer velocity US on χ and λ. The velocity decreases
monotonically with λ. When the outer and inner phase have matching viscosities (λ = 1), US is not
affected by the presence of the droplet, and is thus equal to the unbounded velocity U0 for all values
of χ. The squirmer swims faster than the unbounded one when the outer phase is less viscous than
11


## Page 12


UD/US
UD/US
Theory
Simulation
Figure 4 The ratio UD/US between the droplet velocity, UD, and the swimmer velocity, US, as a function of the
size ratio χ. The swimmer employs only tangential squirming modes and the viscosity ratio is λ = 1. Green
solid lines and red squares indicate results from the theory and numerical simulations, respectively.
the inner (λ < 1), and swims slower in the opposite limit, λ > 1. When λ ̸= 1, the velocity US varies
with the size ratio χ non-monotonically, reaching its maximum value for λ < 1 when the swimmer
is tightly conﬁned, χ ≈1.1 ∼1.2, namely when the droplet is slightly larger than the swimmer. The
result is similar when λ > 1 and the minimum is reached. For any viscosity ratios, US = U0 in the limit
of χ = 1 and χ →∞. The former corresponds to the situation when the droplet exactly encompasses
the swimmer and the latter to when the droplet is much larger than the swimmer. In Fig. 3b, we
further show that the velocity UD of the droplet decreases monotonically with χ, as well as with λ.
The inset of Fig. 3b presents the ratio UD/US of the droplet velocity over the swimmer velocity as a
function of χ in a log-log form, this ratio decays as χ−3 for large χ. It is important to note that for any
values of χ or λ the swimmer is always faster than the droplet, US > UD. The concentric conﬁguration
is thus not a steady state if the swimmer only applies tangential forcing.
2.
Comparisons between theory and simulations
Here we consider the dynamics of a neutral swimmer (β = 0), a pusher with β = −5 and a puller
with β = 5 encapsulated inside a same-viscosity droplet (λ = 1). For simplicity we further take Bn = 0
for n ≥3 and An = 0 for all n. Since the velocities UD and US are independent of β, the ratio UD/US
only depends on the value of χ. This functional dependence is plotted in Fig. 4, showing an excellent
agreement between the theory (green lines) and numerical data (red squares).
Next in Fig. 5a-c, we plot the ﬂow velocity ﬁeld, v/B1, in the laboratory frame for the pusher (a),
neutral (b) and puller (c) swimmers respectively. The size ratio is χ = 2. Theoretical results are shown
12


## Page 13


3
4
5
6 7 8 9
 
 
−5
−2.5
0
2.5
5
−2
−1
0
1
2
Theory
Simulation
3
4
5
6 7 8 9
 
 
0.1
0.2
0.3
0.4
0.5
0.6
0.1
0.2
0.3
0.4
0.5
0.6
 
 
 
0.5
1
1.5
2
2.5
0.5
1
1.5
2
2.5
 
Theory
Simulation
(a)
(b)
(c)
(d)
(e)
(f)
 
 
0.5
1
1.5
2
2.5
0.5
1
1.5
2
2.5
 
β = −5
β = 0
β = 5
|v|/B1
|v|/B1
Pusher
Puller
Neutral
 
 
−5
−2.5
0
2.5
5
−2
−1
0
1
2
Theory
Simulation
3
4
5
6 7 8 9
10
−2
10
−1
10
0
3
4
5
6 7 8 9
z/a
vz/B1
z/a
r/a
r/a
r/a
r/a
r/a
r/a
vz/B1
z/a
vz/B1
 
 
−5
−2.5
0
2.5
5
−2
−1
0
1
2
3
4
5
6 7 8 9
10
−2
10
−1
10
0
3
4
5
6 7 8 9
10
−4
10
−2
10
0
Theory
Simulation
r−2
r−2
r−2
r−2
r−3
r−3
β = −5
β = 0
β = 5
US/B1 = 2/3
US/B1 = 2/3
US/B1 = 2/3
θ = 0
θ = π
θ = 0
θ = π
θ = 0
θ = π
|v|/B1
|v|/B1
|v|/B1
Figure 5 Illustration of velocity ﬁelds, v, in the laboratory frame. Comparison between the theory and
simulations for a pusher with β = −5 (a, d), a neutral swimmer with β = 0 (b, e), and a puller β = 5 (c, f). The
viscosity ratio is λ = 1 and the size ratio is χ = 2. Black spheres denote the swimmers and solid magenta
circular lines the droplets. The green arrows indicate the swimming directions. The left column (a, b, c)
display the velocity vectors (white arrows) of v/B1 and the contours of its magnitude |v|/B1. Theoretical results
are shown on the left panels while the numerical results are shown on the right. The right column (d, e, f)
shows the theoretical (blue solid line) and numerical (empty red circles) data of the scaled velocity along the z
axis, vz/B1, where the dot-dashed line indicates the swimmer velocity of US/B1 = 2/3. The velocity magnitude,
|v|/B1, versus the distance, r/a, along the anterior θ = 0 (z > 0) and posterior θ = π (z < 0) directions is shown
in a log-log form; the dashed curves denote the leading order velocity v(2)
r |leading at θ = 0 and π. The spatial
decay of |v|/B1 in the far ﬁeld follows the r−2 law for the pusher/puller and r−3 law for the neutral swimmer.
13


## Page 14


on the left panel and numerical data on the right. The numerical predictions show good agreement
with the theoretical data in most of the ﬂow domain except very close to the droplet interface where
numerical errors arise from the nearly-singular integration.
For the neutral swimmer, note that the velocity ﬁeld is not affected at all by the presence of the
droplet. This is corroborated by the fact that neither the swimming velocity nor the power are im-
pacted by the droplet, as implied by Eq. 10 and Eq. 15. This results from the vanishing radial velocity
in the droplet frame, such that the spherical droplet interface introduces no perturbation and hence
does not inﬂuence the swimming dynamics.
For the pusher in a drop, similarly to a pusher in free space, ﬂuid is locally pushed away from
the anterior (θ = 0) and posterior (θ = π) parts of the swimmer and comes to the lateral directions
(θ = π/2). Due to the non-penetrating nature of the droplet interface, two counter-rotating toroidal
vortices form inside. Outside the droplet the ﬂuid is drawn towards its poles and expelled away on
the equatorial plane. Interestingly the ﬂow signature of a local pusher turns therefore into a puller
in a far ﬁeld. More quantitatively one can show that the velocity ﬁelds of a puller with β > 0 and a
pusher with −β satisfy the relation
vr|β (r,π −θ)+vr|−β (r,θ) = 0,
vθ|β (r,π −θ)−vθ|−β (r,θ) = 0,
(20)
which indicates that the mirror symmetry about the equatorial plane θ = π/2 of the ﬂow ﬁeld of the
pusher with −β is equivalent to the reversed ﬂow ﬁeld of the puller with β.
We next investigate the spatial variation of v (z)/B1 along the z axis in Fig. 5d, e and f for the
three swimmers. Here again, numerical data (empty red circles) agree very well with the theoretical
predictions (solid bule line). The velocity magnitude, |v|/B1, decays in the far-ﬁeld from the swimmer
center as r−2 for the pusher/puller and r−3 for the neutral swimmer. The velocity distribution v (z)
over z for the pusher and that for the puller are symmetric about z = 0, as implied by Eq. 20. For
both swimmers, two stagnation points appear near the droplet interface r = b, one close to the frontal
interface and other close to the rear. They can be observed in Fig. 5.
It is worth emphasizing the result that the presence of droplet reverses the direction of the far-
ﬁeld ﬂow with respect to that of a pusher/puller in free space (Fig. 5a and c). This can be made
more precise by an analysis of the theoretical predictions in Eq. 13. With only B1 and B2 modes, the
14


## Page 15


leading-order contribution to the radial velocity v(2)
r
in the outer phase is
v(2)
r |leading = −c2
∆2χ2
a
r
2
B2P2 (ξ),
(21)
and that to the radial velocity of an unbounded pusher/puller is given by Ref. [10] as
vr|leading = −
a
r
2
B2P2 (ξ).
(22)
Their ratio is v(2)
r |leading/vr|leading = c2/
 ∆2χ2
, which is negative for any size ratio χ > 1 hence ratio-
nalizing the velocity inversion.
3.
Power consumption
When the viscosities inside and outside the droplet are equal (λ = 1) and the swimmer uses tan-
gential surface actuations alone, the power consumption P based on Eq. 15 is simpliﬁed to
P
4πµ1a = 4
3B2
1 +
∞
∑
n≥2
8 ¯dn
n(n+1)¯∆n
B2
n,
(23)
where
¯dn = 4χ2n+3 −(2n+3)χ4 +(2n−1),
¯∆n = 8χ2n+3 −(2n+1)(2n+3)χ4
+2(2n−1)(2n+3)χ2 −(2n−1)(2n+1).
(24)
Restricting then our attention to the simplest squirmer with Bn = 0 for n ≥3, the power becomes
P
4πµ1aB2
1
= 4
3

1+
4χ7 −7χ4 +3
8χ7 −35χ4 +42χ2 −15β 2

,
(25)
of a similar form to that of an unbounded squirmer[10]
P0
4πµ1aB2
1
= 4
3

1+ 1
2β 2

.
(26)
Theoretical and numerical values of P show excellent agreement, as shown in Fig. 6. The power
of an encapsulated squirmer, P, always exceeds that of an unbounded one, P0. From a practical
standpoint, P approximately doubles when the radius of the droplet is 50% larger than that of the
15


## Page 16


Theory
Simulation
P/P0
P/P0 −1
Figure 6 Similar to Fig. 4, but for the power consumption of the squirmer, P, scaled by the unbounded value,
P0. In contrast to the velocities, P depends also on modes |Bn| (n ≥2). Here |β| = |B2/B1| = 5 and Bn = 0
(n ≥3). The inset shows the χ−3 scaling of the nondimensional excess power P/P0 −1.
swimmer. We further observe that P is negatively correlated to χ, and the swimmer expends more
energy due to a stronger conﬁnement. The inset log-log plot indicates that scaled excessive power
P/P0 −1 decreases with the size ratio as χ−3.
B.
Co-swimming by combining tangential and normal squirming
We have shown in the previous sections that a swimmer employing solely tangential squirming
modes, Bn, is always faster than the droplet, i.e. US > UD. Thus, the swimmer and droplet cannot
remain concentric. With the idea of using artiﬁcial swimmers encapsulated in a droplet for control-
lable cargo delivery, it is attempting to try and tune the squirming gait such that the swimmer and
droplet co-move with a same velocity US =UD and maintain a concentric conﬁguration. We ﬁnd that a
squirmer combining both tangential and normal velocities is able to accomplish this, as shown below.
The results in Eq. 10 and 11 imply that the swimming velocities US and UD only depend on the ﬁrst
modes, A1 and B1. We deﬁne α ≡A1/B1 to indicate the relative strength of the modes. By comparing
Eq. 10 and 11, we ﬁnd that a particular value of α, denoted by αco, allows to obtain equal velocities,
namely
αco = (4λ +6)χ5 −10λχ2 +6(λ −1)
(2λ +3)χ5 +10λχ2 −12(λ −1),
(27)
16


## Page 17


1
2
3
4
5
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
 
 
λ = 0.1
λ = 1
λ = 3
λ = 5
λ = 10
Uco
SD/U0
Figure 7 The co-swimming velocity Uco
SD of the squirmer and droplet, as a function of the size ratio χ and
viscosity ratio λ. The ﬁrst-mode normal squirming is tuned to be A1 = αcoB1 such that the squirmer and
droplet swim with a same velocity Uco
SD .
leading to a co-swimming squirmer and droplet velocity, Uco
SD, given by
UD = US = Uco
SD =
10B1χ2{(6λ +9)χ5 −6(λ −1)}
∆{(2λ +3)χ5 +10λχ2 −12(λ −1)}·
(28)
For any size ratio χ > 1, αco > 0 and thus a positive A1 mode, which contributes to the swimming
velocity negatively and therefore enables the squirmer to co-swim with the droplet.
The inﬂuence of conﬁnement χ and viscosity ratio λ on the resulting co-swimming speed is depicted
in Fig. 7 by plotting the scaled co-moving speed Uco
SD/U0, where U0 = 2B1/3 is the velocity of an
unbounded squirmer with pure tangential modes. Even for small viscosity ratio (λ = 0.1), the co-
moving velocity Uco
SD of the pair remains below 0.7U0. Simulations have been performed to determine
the values of αco and Uco
SD for the λ = 1 case, and here again the numerical results show excellent
agreement with the theory (not shown).
The relation between the mode strength α and the size ratio χ required to achieve concentric co-
swimming is given by Eq. 27 for arbitrary viscosity ratio λ. When λ is ﬁxed, the particular value αco
ensuring co-swimming is easily chosen as a function of χ. Conversely, one may determine a particular
size ratio χco as a function of α by solving the quintic equation. In the case of λ = 1, the required size
ratio χco is simply given by
χco =
 α +1
α −1/2
1/3
.
(29)
17


## Page 18


It implies that for a given swimmer with ﬁxed modes one may select a particular size of droplet
transportable by the swimmer in a co-swimming state. This encouraging result points to a practical
route toward building self-propelled chemical droplets.
C.
Stability of co-swimming state: axisymmetric conﬁguration
While the analysis above shows that co-swimming is possible, it is not clear a priori if such con-
ﬁguration would be stable. In order to address the stability of swimmers, we perform numerical
simulations for a swimmer-droplet pair which are initially off-center but axisymmetric. The stability
problem depends on many parameters including the size ratio χ, the viscosity ratio λ, the value of
the mode ratio αco, the stresslet strength β, and the initial offset distance zoff. In order to make the
problem tractable, we restrict the parameter values as χ = 0.5, λ = 1, αco = 1.4 and β = −5,0,5. We
use zoff = zsq −zdp to denote the offset distance in the axial direction, where zsq and zdp are the axial
positions of the swimmer and droplet respectively and all simulations start with zoff(t = 0) = ±0.2a.
Figure 8 (top row) displays the time evolution of zoff for a swimmer which starts initially ahead
(blue dot-dashed lines) or behind (red solid lines) using a tangential squirming of β = −5 (pusher,
a), β = 0 (neutral, b) and β = 5 (puller, c). The physical characteristic time T = b/B1 is used to
scale the time t. For the co-moving pusher as shown in Fig. 8a, the offset zoff(0) decays to zero
regardless of its sign: the concentric co-moving state is recovered and remains stable. The inﬂuence
of zoff(0) for the co-moving neutral swimmer is shown in Fig. 8b. The concentric co-movement is
seen to be stable if the swimmer is initially ahead of the droplet, but it is unstable and yields a ﬁnite-
time collision between the swimmer and the droplet interface, when the swimmer is initially behind.
In contrast, for the puller illustrated in Fig. 8c, the swimmer eventually touches the rear interface
indicating instability when zoff(0) < 0, while when zoff(0) > 0, the pair reaches an eccentric co-moving
state that is asymptotically stable. In the later case, the swimmer is close to the front droplet interface
but separated by a thin lubrication ﬁlm which acts to stabilize their co-movement via hydrodynamic
interactions. The asymptotically steady thickness of the ﬁlm is about 0.08a.
The stability properties of the co-moving state seen in Fig. 8 may be interpreted physically by
examining the disturbance ﬂow ﬁeld induced by the swimmer. We plot in Fig. 8 (middle row) the
disturbance ﬂow patterns corresponding to the co-moving swimming gaits which consist of normal
squirming αco (dashed magenta lines) and tangential squirming β (solid black lines). The distur-
bance ﬂow of the pusher and puller is characterized by a stresslet oriented in the swimming direction,
decaying as 1/r2; that of the neutral swimmer resembles a source dipole along the same direction, de-
caying faster as 1/r3. The analysis of Ref. [10] shows that the ﬂow induced by the A1 mode squirming
18


## Page 19


−1
−0.5
0
0.5
1
 
 
.
zoﬀ(0)/a = −0.2
zoﬀ(0)/a = 0 2
 
 
 
t/T
t/T
t/T
t/T=0
t/T=0
zoﬀ/a
(a)
(b)
(c)
repulsive 
repulsive 
attractive 
repulsive 
repulsive 
repulsive 
attractive 
attractive attractive 
attractive 
repulsive 
attractive 
(β= −5)
(β= 0
(β= 5
(d)
(e)
(f)
(g)
(h)
(i)
(j)
(k)
(l)
β =−5
α = 1.4
β = 0
α = 1.4
β = 5
α = 1.4
Pusher
Neutral
Puller
)
)
0
1
2
3
0
1
2
3
4
5 0
10
20
30
40
50
Figure 8 Stability of co-swimming state. Top: Time evolution of the axial offset position zoff of a swimmer with
a co-moving swimming gait αco = 1.4 with added tangential squirming with (a): β = −5 (pusher); (b): β = 0
(neutral); and (c): β = 5 (puller). The swimmer is ahead/behind of the droplet center by 0.2a at t/T = 0 in the
top (zoff > 0)/bottom (zoff < 0) row. The horizontal lines zoff/a = 1 and −1 indicate where the swimmer touches
the front and rear of the droplet interface respectively. The solid and dashed circles indicate the swimmer’s
initial and ﬁnal positions respectively. Middle: Disturbance ﬂow ﬁeld induced by a swimmer with a co-moving
swimming gait that superimposes a normal squirming of αco = 1.4 onto a tangential squirming of (d): β = −5
(pusher); (e): β = 0 (neutral); and (f): β = −5 (puller). The solid black and dashed magenta lines denote the
ﬂow patterns generated by the tangential and normal squirming gaits respectively. Bottom: Inﬂuence of the
disturbance ﬂows and resulting hydrodynamic interactions on the behavior of a co-moving pusher (g, j),
neutral (h, k), and puller swimmer (i, l). The green solid sphere indicates the initial location of the swimmer
while the yellow dashed circle its ﬁnal location (the green dot-dashed circle in 8i indicates an intermediate
location.)
19


## Page 20


is equivalent to that by a neutral swimmer with B1 = A1. The details of this disturbance ﬂow dictate
hydrodynamic interactions between the swimmer and its environment. As can be seen in Fig. 8d, a
body located in front of or behind a pusher tends to be repelled by it while it will tend to be attracted
for a puller. In contrast for a neutral swimmer with A1 > 0, ahead of the swimmer will be repulsive
while it will tend to be attractive behind it.
We then link in Fig. 8 (bottom row) the disturbance ﬂow of the swimmer and its relative movement
with respect to the droplet, where solid/dashed circles denote the swimmer’s initial/ﬁnal location
(the dot-dashed circles denotes an intermediate position). As seen in Fig. 8g, for a co-moving pusher
initially ahead of the droplet center, the repulsive ﬂow in front of the swimmer, consisting of both
repulsive ﬂows from tangential squirming of β = −5 and normal squirming of α = 1.4, is stronger
than its rear counterpart and brings the swimmer back to the center (stable). For the same swimmer
but initially closer to the rear of the droplet as depicted in Fig. 8j, the rear ﬂows dominate. While
the ﬂows induced by the two squirming modes are of opposite sign, the repulsive ﬂow arising from
tangential squirming is likely to overcome the attractive one of the normal squirming due to the
faster-decaying and shorter-ranged disturbance ﬂow of the latter (1/r3 vs. 1/r2).
The behavior of the co-moving neutral swimmer can be understood along the same vein, as il-
lustrated in Fig. 8h and k, and similarly for the puller when its is initially located behind that of
the droplet (Fig. 8l). The only non-intuitive result is the asymptotically-stable eccentric location of
the co-moving puller that is originally closer to the droplet front as illustrated in Fig. 8i. Initially,
the gap between the swimmer and interface is relatively large, therefore the longer-ranged attractive
ﬂow from the tangential squirming will outweigh the shorter-ranged repulsive one from the normal
squirming, and the swimmer will be attracted towards the interface. As the gap width decreases,
the repulsive short-range ﬂow becomes stronger, eventually dominating and preventing the swim-
mer from further approaching the interface. This explains, at least qualitatively, why hydrodynamic
interactions lead in this situation to a stable eccentric conﬁguration.
Additional simulations were then performed with 1/χ ranging from 0.3 to 0.7 and β ranging from
−5 to 5. These simulations show that the stability properties of the co-moving state is independent of
the size ratio χ and depend only on β. As shown in Fig. 9, when β ≤0, the concentric co-movement
state is stable regardless of the sign of the initial offset zoff. When β ≥1, the eccentric co-moving
state is stable if the swimmer is initially ahead (zoff > 0) while no stable co-moving conﬁguration is
observed otherwise (zoff < 0).
20


## Page 21


-5 -4 -3 -2 -1
0
1
2
3
4
5
β
zoﬀ< 0
zoﬀ> 0
   Stable 
(concentric)
   Stable 
(eccentric)
Unstable
Figure 9 The dependence of the stability of the co-moving state on the stresslet strength β.
D.
Stability of co-swimming state: non-axisymmetric conﬁguration
We next address the issue of stability when the initial position of the swimmer center is not aligned
with the droplet along the z axis.
Since the system is not axisymmetric in this case, we employ
numerical simulations allowing the swimmer to display rotational motion. We track the two offset
distance in x and z directions with xoff = xsq −xdp and zoff = zsq −zdp. When χ = 2 and αco = 1.4, we
consider three types of swimmers, namely a pusher with stresslet strength β = −5, a neutral swimmer
with β = 0, and a puller with β = 5.
We ﬁrst plot in Fig. 10a the trajectories of pullers in the laboratory frame with an initial offset
(xoff,zoff) = (0.2a,0.2a). Initially the system is not axisymmetric but after a slight rotation the swimmer
settles in an axisymmetric conﬁguration. Although the rotational motion is small, it occurs early in
the dynamics, in particular before the swimmer closely approaches the droplet. After that, the system
becomes equivalent to the axisymmetric situation considered in Fig 8c and the swimmer reaches a
stable state maintaining a thin gap with the droplet.
Next we show in Fig. 10b the trajectories of pushers with an initial offset (xoff,zoff) = (0.2a,−0.2a).
The swimmer slightly rotates but in this case does not align with the droplet axisymmetrically. Instead,
due to the attractive ﬂows in the lateral directions, the pusher approaches the droplet and eventually
collides with it. Other cases with the initial offset (xoff,zoff) = (0.2a,0.2a) or (0.2a,0) exhibit similar
behaviors as in Fig. 10b with no stable conﬁgurations. Also pullers with the initial offset (xoff,zoff) =
(0.2a,−0.2a) or (0.2a,0) and neutral swimmers with (xoff,zoff) = (0.2a,±0.2a) or (0.2a,0) do not settle
a stable conﬁguration. Additional simulations by changing the size ratio and stresslet strength leads
to similar results.
21


## Page 22


−0.1
0
0.1
0.2
0.3
0.4
0.5
0
1
2
3
4
5
6
x/a
z/a
z/a
zoﬀ
xoﬀ
Initial stage
Equilibrium stage
      (stable)
(a)
0
0.2
0.4
0.6
0.8
1
−0.2
0
0.2
0.4
0.6
0.8
x/a
Initial stage
Eventual collision
     (unstable)
(b)
β = −5
β = 5
Figure 10 Trajectories of swimmers in droplets initially in non-axisymmetric conﬁgurations shown in the
laboratory frame: (a) pullers (β = 5) with an initial offset (xoff,zoff) = (0.2a,0.2a) and (b) pushers (β = −5) with
an initial offset (xoff,zoff) = (0.2a,−0.2a) . The blue diamonds and red circles denote the droplet and swimmer
centers respectively. The arrows indicate the swimming directions. The puller with the initial conﬁgurations in
(a) has a stable conﬁguration while other swimmers collide with the droplet surface.
VI.
Conclusion
In this paper, we have studied in the creeping ﬂow regime the dynamics of a spherical squirmer
encapsulated in an undeformable droplet using both theory and computations. The incompressible
Stokes equations were ﬁrst solved analytically, and when the swimmer and droplet are concentric,
we obtained exact solutions of the swimmer and droplet velocities, the ﬂow velocity ﬁelds and its
dissipated power. Along with this analytic approach, numerical simulations based on a boundary
element method were performed and the numerical results agreed well with the theoretical results.
The analytical solutions provide a useful physical picture of the instantaneous dynamics for the
concentric conﬁguration of the squirmer and droplet. For a squirmer using pure tangential surface
actuations, although their movement are doomed to be transient, the theoretical results state that the
22


## Page 23


swimmer is always faster than the droplet. When the normal surface velocities are incorporated on
top of tangential modes, the squirmer and droplet are able to co-swim with a same velocity and thus
to remain concentric.
When the swimmers are slightly displaced from the concentric position, we found that they would
either return to the center (stable), deviate further and eventually touch the droplet interface (unsta-
ble), or reach an eccentric steady-state position (stable). Such ﬁnal states depend on swimming gaits
or relative locations of swimmers.
The ultimate goal of encaging swimmers is to help transport and deliver small chemical payloads,
and thus a lot of future work lies ahead for swimmer-droplet complexes. Questions including swim-
ming near complex boundaries or near walls, or non-axisymmetrically, will have to be tackled. Surfac-
tants, which are commonly used in droplet-based microﬂuidics to prevent coalescence, could perhaps
be used here to prevent collision between swimmers and interface, with interesting physical conse-
quences. Finally, if heterogeneous ﬂuid mixtures are to be transported in the droplet, it will important
to quantify their mixing and chemical fate as they move along with the swimmer.
VII.
Acknowledgements
Gioele Balestra is acknowledged for his helpful suggestions on making the 3D schematic plot. The
computer time is provided by the Swiss National Supercomputing Centre (CSCS) under project ID
s603 and by SNIC (Swedish National Infrastructure for Computing).
A VR International Postdoc
Grant from Swedish Research Council (L.Z.), an ERC starting grant ’SimCoMiCs 280117’ (F.G.), a
Marie Curie CIG Grant (E.L.) and an ERC Consolidator grant (E.L.) are gratefully acknowledged.
A.
Constants in ﬂow solution
The undeﬁned constants for the ﬂuid velocity ﬁelds in Eq. 13 and the power calculations in Eq. 15
are given in Table I.
23


## Page 24


Table I The constants for the ﬂuid velocity ﬁeld given in Eq. 13 and the power in Eq. 15.
∆n = λ{(2n+1)2(χ2n−1 −1)(χ2n+3 −1)
−(2n−1)(2n+3)(χ2n+1 −1)2}
(n ≥2)
N1 = n(2n−1){(χ2n+1 −1)λ +1}
−(n−2){(2n+1)(χ2n−1 −1)λ −2χ2n−1 +2n+1}
N2 = −2(2n−1){(χ2n+1 −1)λ +1}
+2{(2n+1)(χ2n−1 −1)λ −2χ2n−1 +2n+1}
N3 = (n−2)(2n+3){(χ2n+1 −1)λ +1}
−n{(2n+1)(χ2n+3 −1)λ +2χ2n+3 +2n+1}
N4 = −2(2n+3){(χ2n+1 −1)λ +1}
+2{(2n+1)(χ2n+3 −1)λ +2χ2n+3 +2n+1},
N5 = χ4n+2[−(n+1)(2n+3){(1−χ−2n−1)λ +1}
+(n+3){(2n+1)(1−χ−2n−3)λ +2χ−2n−3 +2n+1}]
N6 = χ4n+2[−2(2n+3){(1−χ−2n−1)λ +1}
+2{(2n+1)(1−χ−2n−3)λ +2χ−2n−3 +2n+1}]
N7 = χ4n+2[−(n+3)(2n−1){(1−χ−2n−1)λ +1}
+(n+1){(2n+1)(1−χ−2n+1)λ −2χ−2n+1 +2n+1}]
N8 = χ4n+2[−2(2n−1){(1−χ−2n−1)λ +1}
+2{(2n+1)(1−χ−2n+1)λ −2χ−2n+1 +2n+1}]
c1 = −n+3
2
N1χ2n+3 −n+1
2
N3χ2n+1 + n−2
2
N5χ2 + n
2N7
c2 = −n+3
2
N2χ2n+3 −n+1
2
N4χ2n+1 + n−2
2
N6χ2 + n
2N8
an =
2n+3
n
−n−1

N1 −(n−1)N3 +

n+ 2n−1
n+1

N5 +(n+2)N7
bn =
2n+3
n
−n−1

N2 −(n−1)N4 +

n+ 2n−1
n+1

N6 +(n+2)N8
cn = n(n+2)N1 +(n−1)(n+1)N3 +(n−1)(n+1)N5 +n(n+2)N7
dn = n(n+2)N2 +(n−1)(n+1)N4 +(n−1)(n+1)N6 +n(n+2)N8
No = N1 +N3 +N5 +N7
Ne = N2 +N4 +N6 +N8
¯No = −n+3
2
N1 −n+1
2
N3 + n−2
2
N5 + n
2N7
¯Ne = −n+3
2
N2 −n+1
2
N4 + n−2
2
N6 + n
2N8
Z1 = 2(2λ +3)χ5 −10(λ −1)χ2 +6(λ −1)
Z2 = (2λ +3)χ5 +10(λ −1)χ2 −12(λ −1)
Z3 = 2{(2λ +3)χ5 +3(λ −1)}
24


## Page 25


[1] M. He, J. S. Edgar, G. D. Jeffries, R. M. Lorenz, J. P. Shelby, and D. T. Chiu, Anal. Chem. 77, 1539 (2005).
[2] S. Köster, F. E. Angile, H. Duan, J. J. Agresti, A. Wintner, C. Schmitz, A. C. Rowat, C. A. Merten, D. Pisig-
nano, A. D. Grifﬁths, et al., Lab Chip 8, 1110 (2008).
[3] M. Chabert and J.-L. Viovy, Proc. Natl. Acad. Sci. U.S.A. 105, 3191 (2008).
[4] J. Clausell-Tormos, D. Lieber, J.-C. Baret, A. El-Harrak, O. J. Miller, L. Frenz, J. Blouwolff, K. J. Humphry,
S. Köster, H. Duan, et al., Chem. Biol. 15, 427 (2008).
[5] H. Wen, Y. Yu, G. Zhu, L. Jiang, and J. Qin, Lab Chip 15, 1905 (2015).
[6] L. Zhang, J. J. Abbott, L. Dong, B. E. Kratochvil, D. Bell, and B. J. Nelson, Appl. Phys. Lett. 94, 064107
(2009).
[7] S. Tottori, L. Zhang, F. Qiu, K. K. Krawczyk, A. Franco-Obregón, and B. J. Nelson, Adv. Mater. 24, 811
(2012).
[8] Y. Ding, F. Qiu, X. C. Solvas, F. W. Y. Chiu, B. J. Nelson, and A. deMello, Micromachines 7, 25 (2016).
[9] M. J. Lighthill, Comm. Pure Appl. Math. 5, 109 (1952).
[10] J. R. Blake, J. Fluid Mech. 46, 199 (1971).
[11] V. Magar, T. Goto, and T. Pedley, Q. J. Mech. Appl. Math. 56, 65 (2003).
[12] T. Ishikawa, M. P. Simmonds, and T. J. Pedley, J. Fluid Mech. 568, 119 (2006).
[13] S. Michelin and E. Lauga, Phys. Fluids 22, 111901 (2010).
[14] A. Doostmohammadi, R. Stocker, and A. M. Ardekani, Proc. Natl. Acad. Sci. U.S.A. 109, 3856 (2012).
[15] A. Zöttl and H. Stark, Phys. Rev. Lett. 108, 218104 (2012).
[16] O. S. Pak and E. Lauga, J. Eng. Math. 88, 1 (2014).
[17] C. Datt, L. Zhu, G. J. Elfring, and O. S. Pak, J. Fluid Mech 784, R1 (2015).
[18] J.-B. Delfau, J. Molina, and M. Sano, EPL 114, 24001 (2016).
[19] H. Lambs, Hydrodynamics, 6th ed. (Cambridge University Press, 1932).
[20] J. Happel and H. Brenner, Low Reynolds Number Hydrodynamics (Noordhoff International publishing,
Leyden, 1973).
[21] C. Pozrikidis, Boundary integral and singularity methods for linearized viscous ﬂow (Cambridge University
Press, 1992).
[22] J. J. L. Higdon and G. P. Muldowney, J. Fluid Mech. 298, 193 (1995).
[23] L. Zhu, E. Lauga, and L. Brandt, J. Fluid Mech. 726, 285 (2013).
[24] D. Dunavant, International journal for numerical methods in engineering 21, 1129 (1985).
25


## Page 26


[25] C. Pozrikidis, A practical guide to boundary element methods with the software library BEMLIB, 1st ed. (CRC
Press, 2002).
[26] A. Zinchenko and R. Davis, J. Fluid Mech. 564, 227 (2006).
[27] A. Z. Zinchenko, M. A. Rother, and R. H. Davis, Phys. Fluids 9, 1493 (1997).
[28] A. Zinchenko and R. Davis, J. Fluid Mech. 725, 611 (2013).
[29] L. Zhu and F. Gallaire, J. Fluid Mech. 798, 955 (2016).
[30] H. C. Berg, E. coli in Motion (Springer, New York, 2004).
[31] J. P. Hernandez-Ortiz, P. T. Underhill, and M. D. Graham, J. Phys. Condens. Matter 21, 204107 (2009).
[32] S. E. Spagnolie and E. Lauga, J. Fluid. Mech. 700, 105 (2012).
[33] R. E. Goldstein, Annu. Rev. Fluid. Mech. 47, 343 (2015).
[34] N. Yoshinaga, K. H. Nagai, Y. Sumino, and H. Kitahata, Phys. Rev. E 86, 016108 (2012).
[35] M. Schmitt and H. Stark, EPL 101, 44008 (2013).
[36] S. Herminghaus, C. C. Maass, C. Krüger, S. Thutupalli, L. Goehring, and C. Bahr, Soft Matter 10, 7008
(2014).
[37] C. C. Maass, C. Krüger, S. Herminghaus, and C. Bahr, Anuu. Rev. Condens. Matter Phys. 7, 171 (2016).
[38] R. Golestanian, T. B. Liverpool, and A. Ajdari, Phys. Rev. Lett. 94, 220801 (2005).
[39] J. L. Anderson, Annu. Rev. Fluid. Mech. 21, 61 (1989).
[40] W. Wang, W. Duan, S. Ahmed, T. E. Mallouk, and A. Sen, Nano Today 8, 531 (2013).
[41] P. H. Colberg, S. Y. Reigh, B. Robertson, and R. Kapral, Acc. Chem. Res. 47, 3504 (2014).
26

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
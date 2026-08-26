---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1712.08442v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1712.08442v2_Influence_of_the_Extrinsic_Curvature_on_2D_Nematic_Films

> Source: 1712.08442v2_Influence_of_the_Extrinsic_Curvature_on_2D_Nematic_Films.pdf

> Pages: 20

---


## Page 1


arXiv:1712.08442v2  [cond-mat.soft]  12 May 2018
Inﬂuence of the Extrinsic Curvature on 2D Nematic Films
G. Napoli1 and L. Vergori2
1Dipartimento di Matematica e Fisica “E. De Giorgi”, Università del Salento, 73100 Lecce, Italy. E-mail:
gaetano.napoli@unisalento.it
2Dipartimento di Ingegneria, Università degli Studi di Perugia, 06125 Perugia, Italy. E-mail:
luigi.vergori@unipg.it
October 5, 2018
Abstract
Nematic ﬁlms are thin ﬂuid structures, ideally two-dimensional, endowed with an in-plane
degenerate nematic order. In this paper we examine a generalisation of the classical Plateau
problem to an axisymmetric nematic ﬁlm bounded by two coaxial parallel rings. At equilib-
rium, the shape of the nematic ﬁlm results from the competition between surface tension, which
favours the minimization of the area, and the nematic elasticity which instead promotes the
alignment of the molecules along a common direction. We ﬁnd two classes of equilibrium solu-
tions in which the molecules are uniformly aligned along the meridians or parallels. Depending
on two dimensionless parameters, one related to the geometry of the ﬁlm and the other to
the constitutive moduli, the Gaussian curvature of the equilibrium shape may be everywhere
negative, vanishing or positive. The stability of these equilibrium conﬁgurations is investigated.
1
Introduction
Fluid ﬁlms, such as soap ﬁlms or lipid membranes, often give rise to shapes, as beautiful as complex,
that have fascinated scientists of all times and of several areas of Science. Since, as known, the energy
of an idealized two-dimensional ﬂuid ﬁlm is proportional to the area it occupies, with the surface
tension being the constant of proportionality, the minimizers of the energy and area functionals
are the same. For this reason the problem of determining minimal surfaces with given boundaries
(raised ﬁrst by Euler) has relevance not only in geometry but also in physics and engineering. As
a classical example, a soap ﬁlm attached to two twin coaxial parallel rings takes the shape of a
catenoid, the only non-planar minimal surface of revolution. On the other hand, the study of ultra
thin structures subjected to the simultaneous action of various forces gives rise to new Plateau-like
problems whose solutions, besides being of interest from the mathematical-physic point of view,
may be used to engineer new devices controlling the geometric properties of soft shells.
An insightful approach to study the interplay between orientational order and geometry is given
by
nematic ﬁlms.
These are ﬂuid ﬁlms endowed with an in-plane nematic order provided by
elongated molecules which may freely glide and/or rotate while keeping their axes lying on the
local tangent plane. The recent review by Zhang et al. [24] reports how liquid crystalline vesicles
exhibit a large variety of shapes due to the interplay between in-plane liquid crystalline order and
1


## Page 2


bending elasticity. Chen and Kamien [2] found axisymmetric equilibrium shapes of nematic ﬁlms
by minimizing a combination of surface tension and nematic elastic energies. They showed that
the nematic order is able to support a rich class of shapes in addition to the classical constant
mean curvature surfaces. In the same energetic framework, Giomi [7] searched for axisymmetric
interfaces whose boundaries are two given coaxial rims and argued that only two branches of
solution are allowed: the catenoidal shape when the surface tension is the dominant eﬀect, and the
pseudospherical hyperboloidal shape when the nematic elasticity plays a predominant role. In [7]
it has been shown that the competition between nematic elasticity and surface tension induces a
ﬁrst order phase transition between the two branches. More recently, the same problem has been
re-examined in terms of forces by Barrientos et al. [1].
It ought to be said that in all the studies quoted above only the contribution due to the intrinsic
curvatures of the ﬂux lines of the director ﬁeld has been accounted for in the elastic free energy
of the nematics. Such a contribution is related to the spatial variations of the director ﬁeld on
the curved substrate. More recently, it has been demonstrated that also the extrinsic curvature
terms, i.e. curvatures related to the geometry of the substrate itself, are relevant in the energetic
balance [15, 14, 11, 19]. The potential applications of these new theories in soft matter and their
elegant mathematical formalism have produced a vivid research activity in the communities of both
theoretical physicists [8, 10, 5, 12, 4] and applied mathematicians [20, 21, 17, 22, 18].
In this paper, we revise the variational problem studied in [7] in the light of the correction to
the two-dimensional nematic free energy proposed in a previous work of ours [14]. This correction
includes terms accounting for the extrinsic curvature of the nematic ﬁlm which are instead missing
in [7]. As a result of the competition between the nematic elasticity and the surface tension, equi-
librium shapes with positive, vanishing or negative Gaussian curvature can be obtained depending
on the magnitudes of the constitutive parameters, the radius of the bounding rings and the distance
between them. The inclusion of the extrinsic curvature terms in the energy functional, on the one
hand, makes the solutions obtained by Giomi [7] no longer admissible, on the other hand, it opens
to new scenarios in which the boundary anchoring is crucial in the determination of the equilibrium
shapes.
The paper is organized as follows. In Sec. II we introduce the model for the energy functional
of a 2D nematic ﬁlm, and write down the equilibrium equations and appropriate sets of boundary
conditions. The specialization of the equilibrium problem to axisymmetric shapes and homoge-
neous alignments of the molecules of the nematics is considered in Sec. III, where, depending on
the (uniform) alignment of the director ﬁeld, the equilibrium equations are solved numerically or
analytically. In Sec. IV, we study the local stability of the solutions considering both in-plane
strong anchoring and natural boundary conditions on the nematic director. Sec. V contains instead
some concluding remarks. The paper is closed by two appendices in which we illustrate the notation
adopted throughout the paper, report lengthy calculations and derive rigorously the equilibrium
equations.
2
The model
We assume that the nematic ﬁlm is schematised by a regular surface S with unit normal ﬁeld ν.
We denote n the nematic director and assume it to be a smooth unit vector ﬁeld tangent to S. The
interplay between the geometry of the ﬁlm and the director ﬁeld will be studied by minimising the
2


## Page 3


following energy functional
W =
Z
S

γ + k
2 |∇sn|2

dA,
(1)
where γ is the surface tension, k the elastic constant of the nematics and ∇s indicates the surface
gradient. We anticipate from the beginning that the choice of the diﬀerential operator ∇s strongly
aﬀects the shape of the equilibrium conﬁguration. In most of the existing literature on nematic shells
or ﬁlms, the energy formula is usually expressed in terms of the covariant derivative (commonly
denoted D) instead of the surface gradient. What should be the most appropriate form of the energy
is still on debate. In favour of our constitutive model for the free energy it must be said that the
energy formula (1) can be derived from the classical three-dimensional Frank’s model by means of a
perturbation analysis. Speciﬁcally, regarding the nematic ﬁlm as a thin ﬂuid layer whose thickness
is much smaller than the minimum radius of curvature of S, to leading order the Frank free energy
density approximates to
2wF = k1(divsn)2 + k2(n · curlsn)2 + k3|n × curlsn|2,
(2)
where divs and curls are, respectively, the surface divergence and surface curl [15]. Next, note
that, under the one–constant approximation (k1 = k2 = k3 = k), (2) reduces to (k/2)|∇sn|2.
To appreciate the diﬀerences between our model and that studied by Giomi [7], observe that the
surface gradient and the covariant derivative of the director ﬁeld n are related through the simple
relation ∇sn = Dn + ν ⊗Ln, where L is the extrinsic curvature tensor of S. Consequently, we
have |∇sn|2 = |Dn|2 + |Ln|2. It is then evident that our free energy density exhibits an extra term
reﬂecting the coupling of the extrinsic curvature of the ﬁlm with the nematic order.
2.1
Equilibrium equations
The Euler-Lagrange equations associated with the energy functional (1) can be readily derived
by following consolidated variational schemes [13]. Speciﬁcally, denoting σ, T and G the stress,
couple-stress and micro-torque tensors, respectively, and g and the micro-couple density acting on
the nematic molecules, the balance equations of forces, and macro- and micro-torques read
divsσ = 0,
(3a)
divsT −εσ = 0,
(3b)
t · (divsG −g) = 0,
(3c)
where t ≡ν × n represents the conormal vector, and ε is the Ricci alternator. Specializing the
analytical scheme introduced in [13] to the energy functional (1) gives
σ =

γ + k
2|∇sn|2

P
(4a)
−k[(∇sn)T ∇sn + (ν · ∆sn)ν ⊗n],
T = k

ν ⊗(∇sn)T t −t ⊗Ln

,
(4b)
G = k∇sn,
g = 0,
(4c)
where P ≡I −ν ⊗ν denotes the projection onto the tangent plane, ⊗the tensor product, and
∆s ≡divs∇s is the Laplace-Beltrami diﬀerential operator on S.
3


## Page 4


Observe ﬁrst that in view of (4) and (3c) the balance equation of macro-moments (3b) is
identically satisﬁed (see Appendix B for details). Next, inserting (4c) into (3c) yields the equilibrium
equation for the in-plane orientation of n in the simple form
t · ∆sn = 0.
(5)
Adopting the most common terminology in the literature, we shall refer to (5) as the director
equation. We now denote e1 and e2 the principal directions on S, and parametrize the director
through the convex angle α contained between e1 and n as
n = cos αe1 + sin αe2.
(6)
In this way, the director equation (5) can be rewritten as
∆sα −divsω+2Hτn = 0,
(7)
where ω is the vector parametrising the spin connection on S, H is the mean curvature, and τn is
the geodesic torsion [3] of the ﬂux lines of the director ﬁeld.
By substituting (4a) into (3a) and projecting along ν, we arrive at the so-called shape equation
2H

γ + k
2 |∇sn|2

−k
n
(∇sn)T (∇sn) · L
+ divs[(ν · ∆sn)n]
o
= 0.
(8)
On the other hand, the projection of (4a) onto the tangent plane yields (see Appendix B)
(∆sα −divsωs + 2Hτn)(∇sα −ωs) = 0,
(9)
which, as an immediate consequence of the director equation (7), is identically satisﬁed.
2.2
Boundary conditions
For 2D nematic ﬁlms with boundary, the shape and director equations must be supplemented by
appropriate boundary conditions. Here, we shall assume that the nematic ﬁlm is simply supported,
that is the boundary is ﬁxed, while the surface can freely rotate about the tangent to the boundary.
This obviously entails that the component of the macro-torque along the unit tangent vector ﬁeld
l must vanish, viz, orienting l such that ν × l coincides with the in-plane outward normal k to ∂S,
l · Tk = 0
on ∂S.
(10)
As the boundary conditions on the director are concerned, we shall take into consideration the
following two cases:
(i) natural boundary conditions which are valid whenever the molecules of the nematics may
freely rotate about the normal ν at the boundary, and impose the following restriction on the
micro-torque G 1:
t · Gk = 0
on ∂S.
(11)
1See the ﬁrst line of formula (20) in [13]. Employing the divergence theorem, one can easily deduce that the vector
multiplied by the virtual rotation δθ, GT t, must have zero component along the in-plane normal to ∂S to allow free
rotations of the molecules of the nematics at the boundary.
4


## Page 5


(ii) in-plane strong anchoring boundary conditions which are valid whenever the in-plane direction
of n is ﬁxed at the boundary. In other words, whenever the angle α is prescribed at the
boundary.
2.3
Axisymmetric shapes
Hereinafter, we shall limit our analysis to 2D nematic ﬁlms schematised by axisymmetric surfaces
of genus 1, bounded by two ﬁxed coaxial circular rings of radius r placed at distance 2h one
each other as displayed in Figure 1. For this class of surfaces the parallels and meridians (with
tangent directions ep and em, respectively) are lines of curvature, namely ep and em are principal
directions, and the vector ﬁeld ω is divergence-free and tangent to the boundary [16]. Observe now
that, according to the convention on the orientation of the unit tangent vector ﬁeld l agreed in the
previous subsection, at the upper (resp. lower) boundary l ≡ep (resp. l ≡−ep) and k ≡em (resp.
k ≡−em). Thus, for 2D axisymmetric ﬁlms, in view of (4b), the boundary condition (10) reads
k(Ln · em)(t · ep) = 0
on ∂S.
(12)
Figure 1: Schematic representation of an axisymmetric 2D nematic ﬁlm. At any point P we deﬁne
both the Darboux frame {n, t, ν} and the orthonormal basis {ep, em, ν}, with ep and em being the
principal directions.
For the sake of simplicity, we limit further our analysis to uniform equilibrium alignments, i.e.
homogeneous solutions to the director equation. Within this ansatz, equation (7) reduces to
Hτn = 0,
(13)
5


## Page 6


that is satisﬁed on the catenoid (the only surface of revolution bounded by the two given coaxial
rings with vanishing mean curvature) irrespective of the (uniform) alignment of the molecules, or
when the alignment of the director ﬁeld is such that the geodesic torsion τn vanishes identically.
But, the catenoid satisﬁes the shape equation (8) if and only if k = 0, that is when the functional
(1) reduces to the energy of a soap ﬁlm. The classical result on the equilibrium shape of a soap
ﬁlm attached to two coaxial rings with the same radius is then recovered. More interestingly, the
equation τn = 0 implies that the director ﬁeld is aligned along a principal direction on S. This
means that, on the axisymmetric surface at hand, at equilibrium the only two uniform alignments
are those with n oriented along the parallels (α ≡αp = 0) or the meridians (α ≡αm = π/2).
3
Equilibrium shapes
To determine the equilibrium shapes of the nematic ﬁlm when the molecules are oriented along
the parallels or meridians, we express the position vector r using cylindrical coordinates, r =
(ρ(z) cos ϕ, ρ(z) sin ϕ, z), with ρ(z) > 0 for all z ∈[−h, h], ϕ ∈[0, 2π], and introduce the dimension-
less quantities ̺ = ρ/r and ζ = z/h. Thanks to such parametrisation and nondimensionalization
the energy functional (1) may be rewritten as
W = 2πγr2
Z 1
−1
w(̺, ̺′, ̺′′, α, α′)dζ,
(14)
where the prime denotes diﬀerentiation with respect to ζ, and
w =

1 + c
̺2α′2 + ̺′2 + ξ2 cos2 α
̺2(ξ2 + ̺′2)
+ ξ2̺′′2 sin2 α
(ξ2 + ̺′2)3

× ̺
p
ξ2 + ̺′2.
(15)
The dimensionless parameters ξ ≡h/r and c ≡k/(2γr2) in (15) give, respectively, a measure of
the slenderness and the ratio between the magnitudes of the surface tension and elastic stiﬀness of
the nematic ﬁlm.
The shape equations (8) corresponding to the two homogeneous equilibrium alignments, α ≡αi
(i = p, m), can be written as
 d
dζ2
∂w
∂̺′′ −d
dζ
∂w
∂̺′ + ∂w
∂̺

α≡αi
= 0.
(16)
Equation (16) with i = m is a fourth order ordinary diﬀerential equation (ODE), whereas for i = p
(16) is a second order ODE. Since the boundary is assumed ﬁxed, (16) must be solved subject to
the boundary conditions
̺(−1) = ̺(1) = 1.
(17)
These two boundary conditions are suﬃcient to determine the equilibrium shapes when α ≡αp.
Two more boundary conditions are instead necessary when the molecules are oriented along the
meridians. Since within the parametrisation and nondimensionalization adopted here the boundary
condition (12) reduces to
̺′′ sin2 α = 0
at ζ = ±1,
(18)
6


## Page 7


the two additional boundary conditions to add to (16) with i = m are
̺′′(−1) = ̺′′(1) = 0.
(19)
It is worth noting that when the molecules are oriented along the parallels the boundary conditions
(18) are identically satisﬁed.
For the sequent stability analysis of the equilibria it is convenient to specify also the boundary
conditions on the angle α.
The natural anchoring boundary conditions result in the Neumann
conditions
α′(±1) = 0,
(20)
while assuming that the molecules of the nematics are forced to align tangentially to the delimiting
rims leads to the Dirichlet boundary conditions
α(±1) = 0.
(21)
Obviously, both the uniform alignments α ≡αi (i = p, m) meet the boundary conditions (20),
whereas α ≡αp is the only uniform equilibrium alignment which satisﬁes the boundary conditions
(21).
3.1
Director ﬁeld aligned along the parallels
Let us now examine the equilibrium conﬁgurations in details and start with the case α ≡αp. In
this case, the shape equation (16) reads
(̺2 + c)̺̺′′ −(̺2 −c)(̺′2 + ξ2) = 0,
(22)
and, as discussed above, has to be solved subject to the Dirichlet boundary conditions (17). The
resulting boundary value problem (BVP) can be solved exactly to yield
̺±(ζ) =
q
2 −a2c ± 2
√
1 −a2c cosh(ξaζ)
a
,
(23)
where the solution with the subscript + (respectively, −) refers to the case c < 1 (respectively,
c > 1). When c = 1 the solution of the BVP is the cylindrical shape ̺ ≡1. The positive constant
a in (22) is a root of the equation
ξ = 1
aarccosh

±a2(c + 1) −2
2
√
1 −a2c

.
(24)
For any ﬁxed values of c ≥c⋆≈0.0257 and ξ > 0 equations (24) can be solved uniquely for
a > 0. On the contrary, if 0 < c < c⋆, depending on the value of ξ, equation (24) may admit
one, two or three roots (see Figure 2). In the limiting case c = 0, (24) admits two roots for any
ξ < ξ⋆≡max
s>0
arccosh
 s2 −1

√
2s
≈0.663, exactly one root if ξ = ξ⋆and no root if ξ > ξ⋆.
Figure 3 displays equilibrium shapes at diﬀerent c. The cylindrical conﬁguration (c = 1) sep-
arates the equilibrium shape with inward concavity (0 ≤c < 1) from those with an outward
concavity (c > 1). Consequently, at equilibrium the Gaussian curvature of the nematic ﬁlm is
negative if 0 ≤c < 1, vanishing if c = 1 and positive if c > 1. In the particular case c = 0, i.e.
7


## Page 8


100
101
102
103
a
0
0, 2
0, 4
0, 6
0, 8
1
ξ
c = 0
c = 10−4
c = 10−3
c = 10−2
c = 3 · 10−2
Figure 2: Solutions to (24) for diﬀerent values of c. Solid lines correspond to stable equilibrium
conﬁgurations in the case of in-plane strong anchoring (see section 4.2). The dashed lines correspond
instead to unstable equilibria.
in the absence of the nematic order, the equilibrium shape is a catenoid. On the contrary, in the
limit as c tending to inﬁnity, that is when the eﬀects due to the nematic elasticity are dominant,
the equilibrium shape tends to a portion of a sphere. This result has an intuitive explanation.
At equilibrium, the molecules of the nematics are aligned along circles whose radii is as large as
possible to diminish the bending energy. This eﬀect is in competition with the boundary conditions,
which ﬁx the radius of the boundary circles, and the surface tension, which pushes the nematic ﬁlm
to minimize its area and then towards the catenoidal conﬁguration. Thus, whenever the nematic
elasticity represents the dominant contribution to the energy of the nematic ﬁlm the circles far from
the boundaries have larger radii, which lends the equilibrium conﬁguration a bulgy shape.
3.2
Director ﬁeld aligned along the meridians
When the molecules of the nematics are oriented along the meridians, the free energy density
depends on ̺′′ and, as mentioned above, the associated shape equation is a fourth-order ODE. The
related BVP ((16)–(19)) can be solved only numerically. In addition, only the natural anchoring
boundary conditions α′(±1) are compatible with this homogeneous alignment.
As in the previous case, when c vanishes the equilibrium shape is catenoidal. For greater c
the nematic elasticity is more signiﬁcant and the equilibrium shape departs from the catenoid
maintaining an inward concavity (and hence the negativeness of the Gaussian curvature), though.
Also in the case α ≡αm our results are in good agreement with the physical intuition. In fact,
since the ﬂux lines of the director ﬁeld are open curves (the meridians), the bending energy attains
the absolute minimum when the ﬂux lines are straight.
On the other hand, the eﬀect of the
8


## Page 9


Figure 3: Equilibrium conﬁgurations with the molecules of the nematics oriented along parallels for
diﬀerent values of c.
surface tension encourages the meridians to be catenaries with inward concavity. The equilibrium
conﬁgurations in Figure 4 result then from the competition of these two eﬀects. In the limiting
case as c →+∞the dominant nematic elasticity lends the equilibrium conﬁguration the cylindrical
shape.
4
Stability
Let us denote Sp and Sm the shapes corresponding to the homogeneous alignments α ≡αp and α =
αm, respectively, and let (Sp, αp) and (Sm, αm) denote the two resulting equilibrium conﬁgurations.
We now discuss the stability of the two equilibrium conﬁgurations under natural and in-plane strong
anchoring boundary conditions.
4.1
Natural anchoring boundary conditions
Both the classes of equilibrium shape analysed in section 3 are compatible with the natural anchoring
boundary conditions. The direct calculation of the energy of the two equilibria shows that (Sm, αm)
requires less energy than (Sp, αp) for any values of the dimensionless parameters c and ξ. On the
other hand, the study of the positive deﬁniteness of the second variations at the two equilibria
reveals that (Sm, αm) is stable, that is the conﬁguration (Sm, αm) is a local minimizer of the energy
functional (14)–(15), whereas (Sp, αp) is unstable.
For the sake of brevity and simplicity of presentation we omit the details regarding the positive
deﬁniteness of the second variation of the energy functional at (Sm, αm). We instead focus on the
9


## Page 10


Figure 4: Equilibrium conﬁgurations with the molecules of the nematics oriented along the meridians
for diﬀerent values of c.
equilibrium conﬁguration (Sp, αp). After some manipulations, the second variation of the energy
functional (14)–(15) at (Sp, αp) can be written as
δ2W[u, ϑ] = ξ2
2
Z 1
−1

u′2 + 2ξ2(3c −̺2
±)
(̺2
± + c)2
u2

dζ
|
{z
}
≡δ2
shW[u]
(25)
+
Z 1
−1
c̺±
q
̺′2
± + ξ2

ϑ′2 −
4cξ2
(̺2
± + c)2 ϑ2

dζ
|
{z
}
≡δ2
naW[ϑ]
,
where u ∈H1
0([−1, 1]) ≡{f ∈H1([−1, 1]) : f(±1) = 0}, with H1([−1, 1]) being the Hilbert space
of functions deﬁned in [−1, 1] whose square is integrable together with the square of its weak ﬁrst
derivative, ϑ ∈X ≡{f ∈H1([−1, 1]) : f ′(±1) = 0}, and ̺± is given by (23). As an immediate
consequence of (25) we deduce that (Sp, αp) is stable if and only if the quadratic functionals δ2
shW[u]
and δ2
naW[ϑ] are both positive deﬁnite. But, obviously, δ2
naW[ϑc] < 0 for any non-zero constant
ϑc. This implies that δ2
naW[ϑ] is not positive deﬁnite and thus (Sp, αp) is an unstable equilibrium
conﬁguration.
4.2
In-plane strong anchoring boundary conditions
We now assume that the molecules of the nematics are constrained to align themselves tangentially
to the boundaries. We then consider the Dirichlet boundary conditions (21). As mentioned be-
10


## Page 11


fore, the only homogeneous alignment compatible with these boundary conditions is that with the
molecules oriented along the parallels.
In contrast to the case of natural boundary conditions, in the case at issue the equilibrium
conﬁguration (Sp, αp) may be stable for some values of c and ξ. To validate such a claim, we see
that, setting
θ = ϑ
v
u
u
t
̺±
q
̺′2
± + ξ2
,
(26)
the second variation at (Sp, αp) can be rewritten as δ2W[u, θ] = δ2
sh[u] + δ2
sa[θ], with δ2
sh[u] as in
(25),
δ2
saW[θ] = c
Z 1
−1

θ′2 −c[(2̺2
± + c)(̺′2
± + ξ2) + ξ2̺2
±]
̺2
±(̺2
± + c)2
θ2

dζ,
(27)
and u, θ ∈H1
0([−1, 1]). As in the case of natural anchoring boundary conditions, (Sp, αp) is stable
if and only if δ2
shW[u] and δ2
saW[θ] are positive-deﬁnite quadratic functionals.
Following standard arguments in calculus of variations, a necessary and suﬃcient condition for
δ2
shW[u] to be positive-deﬁnite is that the interval [−1, 1] contains no interior points conjugate to
−1 (see, for instance, [6] page 111). For each c > 0 we then determine the least positive value of ξ,
say ξ(sh)
cr
(c), such that both the boundary value problem





u′′ −2ξ2(3c2 −̺2
±)
(̺2
± + c)2
u = 0,
u(−1) = 0,
u(1) = 0,
(28)
and the normalization condition u′(−1) = 1 (see [6] page 106) are satisﬁed. Clearly, for ξ < ξ(sh)
cr
(c),
the boundary value problem (28) admits only the trivial solution. Thus, the interval [−1, 1] contains
no interior points conjugate to −1 and, consequently, δ2
shW[u] is positive-deﬁnite.
Following similar arguments one can determine a necessary and suﬃcient condition for the
positive-deﬁniteness of δ2
saW[θ].
Speciﬁcally, denoting ξ(sa)
cr
(c) the least positive value of ξ for
which both the boundary value problem





θ′′ + c[(2̺2
± + c)(̺′2
± + ξ2) + ξ2̺2
±]
̺2
±(̺2
± + c)2
θ = 0,
θ(−1) = 0,
θ(1) = 0,
(29)
and the normalization condition θ′(−1) = 1 are satisﬁed, δ2
saW[θ] is positive-deﬁnite if and only if
ξ < ξ(sa)
cr
(c).
We now observe that δ2
shW[u] and δ2
saW[θ] are both positive-deﬁnite, and hence δ2W[u, ϑ] is
positive-deﬁnite, if and only if ξ < ξcr(c) ≡min{ξ(sh)
cr
(c), ξ(sa)
cr
(c)}.
The critical curve ξ = ξcr(c) displayed in Figure 5 has been determined numerically by using
Matlab bvp4c solver. When the molecules of the liquid crystal are anchored tangentially at the
boundaries, the equilibrium conﬁguration (Sp, αp) is locally stable if and only if ξ < ξcr(c). Beyond
this critical threshold, (Sp, αp) is no longer a local minimizer of the energy functional (14)–(15) and
the equilibrium solutions bifurcate to conﬁgurations with non-homogeneous alignments as depicted
in Figure 5.
11


## Page 12


0
0, 5
1
1, 5
2
ξ
0
0, 5
1
1, 5
2
c
0, 7
0, 75
0, 8
ξ
0
0, 02
0, 04
c
Figure 5: Critical threshold for the stability of (Sp, αp) as a function of c. The equilibrium conﬁgu-
ration (Sp, αp) is stable if and only if ξ ≤ξcr(c). Beyond this critical value, at a stable equilibrium
conﬁguration, the alignment of the molecules must be inhomogeneous.
5
Conclusions
In summary, we have investigated the equilibrium problem of ﬂuid ﬁlms endowed with nematic order.
We have showed that, as a result of the competing eﬀects due to surface tension and orientational
order, the equilibrium shape of the nematic ﬁlm may have positive, vanishing or negative Gaussian
curvature.
We have presented the case of a surface bounded by two coaxial parallel rims and
studied the existence, uniqueness and stability of the equilibrium conﬁgurations with homogeneous
alignments of the molecules of the nematics. Speciﬁcally, we have considered two diﬀerent sets of
boundary conditions on the director ﬁeld: natural and in-plane strong anchoring. In both cases we
have determined locally stable equilibria, i.e. local minimizers of the energy functional.
Our analysis, though not exhaustive, shows that the inclusion of terms accounting for the ex-
trinsic curvature in the energy functional renders the equilibrium problem of nematic ﬁlms complex
and intriguing at the same time. Existence and uniqueness of solutions to the equilibrium equa-
tions corresponding to non-uniform alignments of the molecules of the nematics and the search for
global minimisers of the energy functional represent challenges for future analytical and numerical
investigations. Another problem worth of investigation is the generalisation of this problem in the
framework of the two-dimensional Frank’s formula (2), relaxing then the one constant approxima-
12


## Page 13


tion. Motivated by the recent results by Sonnet and Virga [23], we think that such a generalisation
leads to a more intricate scenario in the energy landscape.
Finally, our study lays the foundations for the design of devices capable to control the shape
of nematic ﬁlms. To this aim, note the analogy of the nematic ﬁlms studied here with the soft
elastic sheets where surfaces with both positive, vanishing or negative Gaussian curvature can be
produced by tuning the amount of local growth or swelling [9]. In the case of nematic ﬁlms, an
external electric or magnetic ﬁeld may control the curvatures of the equilibrium shapes.
Acknowledgements
LV gratefully acknowledges the ﬁnancial support from the Italian National Group of Mathematical
Physics (GNFM-INdAM) within the Young Researchers Project “Gusci nematici sferici”.
The authors thank David MacTaggart for the discussions during the preparation of the manuscript.
A
Surface diﬀerential operators
A.1
Notation
We ﬁrst introduce the terminology and notation adopted throughout the paper. Let E be a three-
dimensional Euclidean point space and V be the Euclidean vector space associated to E.
The
elements of V are three-dimensional vectors which are here denoted by lower-case boldface letters.
The scalar, vector and tensor products of two vectors u and v are denoted u · v, u × v and u ⊗v,
respectively. In components, adopting the Einstein summation convention, we have u · v = uivi,
(u × v)i = εijkujvk, (u ⊗v)ij = uivj, with εijk being the alternating symbol.
Second-order tensors are linear maps from V to V itself and are denoted by capital boldface
letters. The set of all second-order tensors is denoted Lin(V). The composition of two second-order
tensors A, B is the tensor AB with components (AB)ij = AihBhj. Once again, sum over repeated
indices is understood. The trace is the linear operator tr : Lin(V) →R which assigns to a second-
order tensor A the scalar obtained by saturation of the two indices of A, viz trA ≡Aii. The
superscript suﬃx T to a second-order tensor indicates transposition: the transpose of A ∈Lin(V)
is the second-order tensor AT with components (AT )ij = Aji. Thanks to the deﬁnitions of trace
and transposition the bilinear map which assigns to two second-order tensors A and B the quantity
A · B ≡tr(AT B) = AijBij is a scalar product in Lin(V).
Tensors of order n > 2 are multilinear maps from Vn to R. However, in this paper we consider
only one tensor of order greater than 2: the Ricci alternator ε, which is a third-order tensor with
components εijk. Finally, in composing tensors of diﬀerent orders we agree to write the lower order
tensor on the right and saturate all its indices. As examples of this convention, regarding vectors
as tensors of order one, Av is a vector with components (Av)i = Aijvj, εA is a vector with
components (εA)i = εijkAjk, and εv is a second-order tensor with components (εv)ij = εijkvk.
A.2
Diﬀerential operators on S. The extrinsic curvature tensor.
The nematic ﬁlm is represented by a regular oriented surface S of E. Scalar, vector and tensor
ﬁelds are functions deﬁned on S which assigns to each point p ∈S an element of R, V or Lin(V),
respectively.
13


## Page 14


At each point p, S is endowed with a 2-dimensional linear space Tp called the tangent space of S
at p. The normal ν(p) at p ∈S is one of the two unit vectors spanning the orthogonal complement of
the tangent space. Since S is orientable, at each point p we can choose an orientation of the normal
so that the resulting unit vector ﬁeld ν : S →V is diﬀerentiable. The perpendicular projection
onto the tangent plane, P ≡I −ν ⊗ν, with I being the identity tensor, is then a diﬀerentiable
tensor ﬁeld.
A vector ﬁeld v on S is tangential if v(p) ∈Tp for all p ∈S. A tensor ﬁeld A on S is tangential
if, at each point p ∈S, A(p)w ∈Tp for all w ∈V, and A(p)ν(p) = 0.
Let φ be a diﬀerentiable scalar ﬁeld on S. The surface gradient of φ is the tangential vector
ﬁeld ∇sφ ≡P∇φ. Similarly, the surface gradient of a diﬀerentiable vector ﬁeld v is the tensor ﬁeld
∇sv ≡(∇v)P. The trace of ∇sv gives the surface divergence of v, i.e.
divsv ≡tr(∇sv) = ∇v · P,
(30)
while twice the axial vector corresponding to the skew-symmetric part of ∇sv gives the surface curl
of v, i.e.
curlsv ≡−ε∇sv.
(31)
The tensor ﬁeld L ≡−∇sν is symmetric and tangential. At each point p ∈S, we may then
regard L(p) as a linear map from Tp to the tangent plane at p itself whose eigenvalues c1 and c2
and corresponding unit eigenvectors e1 and e2 are the principal curvatures and directions at p,
respectively. The ﬁrst two principal scalar invariants of L,
2H ≡tr(L) = −divsν = c1 + c2,
(32)
and
K ≡1
2[(trL)2 −trL2] = c1c2,
(33)
are the mean and Gaussian curvatures of S, respectively. Since L is a tangential tensor ﬁeld, the
Cayley-Hamilton theorem implies that
L2 −2HL + KP = 0.
(34)
Let n be a tangent unit vector ﬁeld. The normal curvature and the geodesic torsion along n are
deﬁned, respectively, as
cn ≡n · Ln
and
τn ≡−t · Ln,
(35)
where t = ν × n. Similarly, ct ≡Lt · t is the normal curvature along t. From this deﬁnition and
(35) the extrinsic curvature tensor L can be written as
L = cnn ⊗n −τn(n ⊗t + t ⊗n) + ctt ⊗t,
(36)
by which we readily deduce that
cn + ct = 2H
and
cnct −τ 2
n = K.
(37)
We conclude this section by reporting some identities that will be useful in deriving the equilib-
rium equations. Let f, u, w and S be diﬀerentiable ﬁelds on S, with f being scalar valued, u and
w vector valued, and S tensor valued. The following identities hold
∇s(fu) = u ⊗∇sf + f∇su,
(38a)
14


## Page 15


divs(fS) = S∇sf + fdivsS,
(38b)
divs(ST u) = (divsS) · u + S · ∇su,
(38c)
divs(u ⊗w) = (∇su)w + (divsw)u,
(38d)
(∇su)u = curlsu × u + 1
2∇s
 |u|2
,
(38e)
curls(fu) = ∇sf × u + fcurlsu,
(38f)
curls∇sf = −ν × L∇sf.
(38g)
B
Derivation of the equilibrium equations
In [15] we proved that the surface gradients of the principal directions are given as follows
∇se1 = k1e2 ⊗e1 + k2e2 ⊗e2 + c1ν ⊗e1,
(39a)
∇se2 = −k1e1 ⊗e1 −k2e1 ⊗e2 + c2ν ⊗e2,
(39b)
where k1 and k2 are the geodesic curvatures of the curvature lines of S, i.e. the integral curves
of the principal directions on S. Then combining (6), (38a) and (39) the surface gradients of the
director and conormal ﬁelds are, respectively,
∇sn = t ⊗(∇sα −ω) + ν ⊗Ln,
(40a)
∇st = −n ⊗(∇sα −ω) + ν ⊗Lt,
(40b)
where ω = −k1e1 −k2e2 is the vector parametrising the spin connection on S. From (40), we
readily deduce that
curlsn = (∇sα −ω) × t −ν × Ln,
(41a)
curlst = −(∇sα −ω) × n −ν × Lt,
(41b)
and
|∇sn|2 = |∇sα −ω|2 + |Ln|2.
(42)
From (38f) and (39) the surface curl of the vector parametrising the spin connection is found to
be
curlsω = −curls(k1e1 + k2e2)
(43)
= −(∇sk1 × e1 + ∇sk2 × e2)
−|ω|2ν + k1c1e2 −k2c2e1
= −(∇sk2 · e1 −∇sk1 · e2 + |ω|2)ν
+ (e2 ⊗e1 −e1 ⊗e2)Lω
= −ν × Lω + Kν,
where the identity
−(∇sk2 · e1 −∇sk1 · e2 + |ω|2) = ν · curlsω = K
(44)
15


## Page 16


has been used. We refer the reader to Appendix C in [15] for the proof of (44). Finally, with the
aid of (38g) and (43) we conclude that
curls(∇sα −ω) = −ν × L(∇sα −ω) −Kν.
(45)
Next, on using (38c), (34), (40) and the deﬁnition of the extrinsic curvature tensor we deduce
that
n · ∆sn = n · divs(∇sn)
(46)
= divs[(∇sn)T n] −∇sn · ∇sn = −|∇sn|2,
t · ∆sn = t · divs(∇sn)
(47)
= divs[(∇sn)T t] −∇sn · ∇st
= divs(∇sα −ω) −Ln · Lt
= ∆sα −divsω + 2Hτn,
thanks to which the director equation (5) can be rewritten as (7), and
ν · ∆sn = ν · divs(∇sn)
(48)
= divs[(∇sn)T ν] + ∇sn · L
= divs(Ln) + Lt · (∇sα −ω).
We now report the identity
divsL = 2

∇sH + (2H2 −K)ν

,
(49)
the proof of which is contained in Appendix A of [13]. As a consequence (38c), (40b), (49) and the
symmetry of the extrinsic curvature tensor L, we have
divs(Lt) = divsL · t + L · ∇st
(50)
= 2∇sH · t −Ln · (∇sα −ω).
On the other hand, from (36), (37)1, (38b), and (40) we have
divs(Lt) = divs(−τnn + ctt)
(51)
= −∇sτn · n + ∇sct · t
−(ctn + τnt) · (∇sα −ω)
= 2∇sH · t −∇sτn · n −∇scn · t
+ (ν × Lt) · (∇sα −ω).
Then, combining (50) and (51) yields
∇sτn · n + ∇scn · t = (Ln + ν × Lt) · (∇sα −ω).
(52)
16


## Page 17


From (34), (36), (38f), (41) and (52) we obtain
curls(Ln) = ∇scn × n + cncurlsn
(53)
−∇sτn × t −τncurlst
= −(∇scn · t + ∇sτn · n)ν
+ (∇sα −ω) × (ν × Ln) −ν × L2n
= −[(ν × Lt) · (∇sα −ω)]ν −2Hν × Ln + Kt.
We are now in position to derive the equilibrium equations (8) and (9). We ﬁrst project (3a),
with σ as in (4a), along the normal ν and obtain
0 = ν · divsσ = divs(σT ν) + σ · L
(54)
= −kdivs[(ν · ∆sn)n] + 2H

γ + k
2 |∇sn|2

−k(∇sn)T (∇sn) · L,
that is equation (8). Next, since from (32) and (38d) one deduces that
divs

γ + k
2|∇sn|2

P

= 2H

γ + k
2 |∇sn|2

ν
(55)
+ k
2 ∇s
 |∇sn|2
,
on using (38d), (38e), (42), (45), (48) and (53), the projection of (3a), with σ as in (4a), onto the
tangent plane yields
0 = Pdivs

(∇sn)T (∇sn) + (ν · ∆sn)ν ⊗n

(56)
−1
2∇s(|∇sn|2)
= Pdivs [(∇sα −ω) ⊗(∇sα −ω) + Ln ⊗Ln]
−(ν · ∆sn)Ln −1
2∇s(|∇sn|2)
= P
h
curls(∇sα −ω) × (∇sα −ω) + curls(Ln) × Ln
i
+ 1
2∇s

|∇sα −ω|2 + |Ln|2 −|∇sn|2
+ (∆sα −divsω)(∇sα −ω) +
h
divs(Ln) −ν · ∆sn
i
Ln
= −Kν × (∇sα −ω) + (∆sα −divsω)(∇sα −ω)
−[(ν × Lt) · (∇sα −ω)]ν × Ln −[Lt · (∇sα −ω)]Ln
= (∆sα −divsω + 2Hτn)(∇sα −ω),
17


## Page 18


where the last equality is a consequence of the fact that, in the light of (36) and (37),
[(ν × Lt) · (∇sα −ωs)]ν × Ln
(57)
+ [Lt · (∇sα −ωs)]Ln
= −[n · (∇sα −ω)][(cn + ct)τnn + (cnct −τ 2
n)t]
+ [t · (∇sα −ω)][(cnct −τ2
n)n −(cn + ct)τnt]
= −2Hτn(∇sα −ω) −Kν × (∇sα −ω).
The derivation of (9) is then complete.
Observe now that the stress tensor (4a) is not symmetric and, in view of (48) and the symmetry
of L, twice the axial vector corresponding to the skew-symmetric part of σ is
εσ = −k(ν · ∆sn)t
(58)
= −k
h
divs(Ln) + L(∇sα −ω) · t
i
t.
On the other hand, from (38d), (40), (34), (36) and, again, the symmetry of the extrinsic curvature
tensor L, the surface divergence of the macro torque tensor (4b) reads
divsT = −kL(∇sn)T t + kdivs[(∇sn)T t]ν
(59)
−k(∇st)Ln −kdivs(Ln)t
= −kL(∇sα −ω) + k(∆sα −divsω)ν
+ k
h
L(∇sα −ω) · n
i
n −k(L2n · t)ν −kdivs(Ln)t
= k(∆sα −divsω + 2Hτn)ν
−k
h
divs(Ln) + L(∇sα −ω) · t
i
t.
Thus, in the light of (7), (58) and (59) the equation of balance of macro torques is identically
satisﬁed.
References
[1] G. Barrientos, G. Chacón-Acosta, O. González-Gaxiola, and J. A. Santiago. Forces on mem-
branes with in-plane order. Journal of Physics Communications, 1(4):045017, 2017.
[2] B. G. Chen and R. D. Kamien. Nematic ﬁlms and radially anisotropic delaunay surfaces. Eur.
Phys. J. E, 28(3):315– 329, 2009.
[3] M. P. do Carmo. Diﬀerential Geometry of Curves and Surfaces. Prentice-Hall, Englewood
Cliﬀs, NJ, 1976.
[4] X. Duan and Z. Yao. Curvature-driven stability of defects in nematic textures over spherical
disks. Phys. Rev. E, 95(6):062706–, 06 2017.
[5] Y. Gaididei, A. Goussev, V. P. Kravchuk, O. V. Pylypovskyi, J. M. Robbins, D. D. Sheka,
V. Slastikov, and S. Vasylkevych. Magnetization in narrow ribbons: curvature eﬀects. Journal
of Physics A: Mathematical and Theoretical, 50(38):385401, 2017.
18


## Page 19


[6] I. Gel’fand and S. Fomin. Calculus of variations. Selected Russian publications in the mathe-
matical sciences. Prentice-Hall, 1963.
[7] L. Giomi. Hyperbolic interfaces. Phys. Rev. Lett., 109(13):136101–, 2012.
[8] D. Jesenek, S. Kralj, R. Rosso, and E. G. Virga. Defect unbinding on a toroidal nematic shell.
Soft Matter, 11(12):2434–2444, 2015.
[9] Y. Klein, E. Efrati, and E. Sharon. Shaping of elastic sheets by prescription of non-euclidean
metrics. Science, 315(5815):1116–1120, 2007.
[10] V. Koning, T. Lopez-Leon, A. Darmon, A. Fernandez-Nieves, and V. Vitelli. Spherical nematic
shells with a threefold valence. Physical Review E, 94(1):012703–, 07 2016.
[11] B. L. Mbanga, G. M. Grason, and C. D. Santangelo. Frustrated order on extrinsic geometries.
Phys. Rev. Lett., 108(1):017801–, 01 2012.
[12] L. Mesarec and W. G. A. I. S. Kralj. Impact of curvature on topological defects. Journal of
Physics: Conference Series, 780(1):012015, 2017.
[13] G. Napoli and L. Vergori.
Equilibrium of nematic vesicles.
J. Phys. A: Math. Theor.,
43(44):445207, 2010.
[14] G. Napoli and L. Vergori. Extrinsic curvature eﬀects on nematic shells. Phys. Rev. Lett.,
108(20):207803–, 05 2012.
[15] G. Napoli and L. Vergori. Surface free energies for nematic shells. Phys. Rev. E, 85(6):061701–,
06 2012.
[16] G. Napoli and L. Vergori. Eﬀective free energies for cholesteric shells. Soft Matter, 9:8378–8387,
2013.
[17] G. Napoli and L. Vergori. Hydrodynamic theory for nematic shells: The interplay among
curvature, ﬂow, and alignment. Phys. Rev. E, 94(2):020701–, 08 2016.
[18] M. Nestler, I. Nitschke, S. Praetorius, and A. Voigt. Orientational order on surfaces: The
coupling of topology, geometry, and dynamics. Journal of Nonlinear Science, 2017.
[19] T.-S. Nguyen, J. Geng, R. L. B. Selinger, and J. V. Selinger. Nematic order on a deformable
vesicle: theory and simulation. Soft Matter, 9(34):8314–8326, 2013.
[20] R. Rosso, E. G. Virga, and S. Kralj. Parallel transport and defects on nematic shells. Contin-
uum Mechanics and Thermodynamics, 24(4):643–664, 2012.
[21] A. Segatti, M. Snarski, and M. Veneroni. Equilibrium conﬁgurations of nematic liquid crystals
on a torus. Phys. Rev. E, 90(1):012501–, 07 2014.
[22] A. Segatti, M. Snarski, and M. Veneroni. Analysis of a variational model for nematic shells.
Mathematical Models and Methods in Applied Sciences, 26(10):1865–1918, 2016.
[23] A. M. Sonnet and E. G. Virga. Bistable curvature potential at hyperbolic points of nematic
shells. Soft Matter, 13:6792–6802, 2017.
19


## Page 20


[24] J. Zhang, X.-F. Chen, H.-B. Wei, and X.-H. Wan. Tunable assembly of amphiphilic rod-coil
block copolymers in solution. Chem. Soc. Rev., 42(23):9127–9154, 2013.
20

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
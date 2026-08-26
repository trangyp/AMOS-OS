---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1508.07872
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1508.07872_On_the_existence_of_rigid_spheres_in_four-dimensional_spacetime_manifolds

> Source: 1508.07872_On_the_existence_of_rigid_spheres_in_four-dimensional_spacetime_manifolds.pdf

> Pages: 24

---


## Page 1


arXiv:1508.07872v2  [gr-qc]  25 Oct 2016
On the existence of rigid spheres in
four-dimensional spacetime manifolds
Hans-Peter Gittel ∗
Department of Mathematics, University of Leipzig,
Augustusplatz 10, 04109 Leipzig, Germany
Jacek Jezierski †
Department of Mathematical Methods in Physics,
University of Warsaw, ul. Pasteura 5, 02-093 Warszawa, Poland
Jerzy Kijowski ‡
Centrum Fizyki Teoretycznej PAN,
Aleja Lotników 32/46, 02-668 Warsaw, Poland
August 30, 2018
Dedicated to Professor Dr. Eberhard Zeidler
on the occasion of his 75th birthday
∗E-mail: gittel@math.uni-leipzig.de
†E-mail: Jacek.Jezierski@fuw.edu.pl
‡E-mail: kijowski@cft.edu.pl
1


## Page 2


Abstract
This paper deals with the generalization of usual round spheres in the
ﬂat Minkowski spacetime to the case of a generic four-dimensional space-
time manifold M. We consider geometric properties of sphere-like subman-
ifolds in M and impose conditions on its extrinsic geometry, which lead to
a deﬁnition of a rigid sphere. The main result is a local existence theorem
concernig such spheres. For this purpose we apply the surjective implicit
function theorem.
The proof is based on a detailed analysis of the lin-
earized problem and leads to an eight-parameter family of solutions in case
when the metric tensor g of M is from a certain neighbourhood of the ﬂat
Minkowski metric. This contribution continues the study of rigid spheres
in [2].
1
Introduction
In [2] we have introduced the concept of “rigidity” of spheres in generic Rieman-
nian three-manifolds and gave a short outline for four-dimensional Lorentzian
spacetimes (cf. [2, Subsection 2.5]). This paper presents geometrical considera-
tions which lead to the deﬁnition of rigid spheres in this case and proves a local
existence result concerning such spheres.
Let M0 be the ﬂat Minkowski spacetime, i.e. the space R4 parameterized by
the Lorentzian coordinates (xα) = (x0, . . . , x3) and equipped with the metric
η = (ηαβ) = diag(−1, 1, 1, 1) (greek indices run always from 0 to 3).
Consider in M0 a round sphere, i.e. the two-dimensional submanifold deﬁned by
ST,R :=
n
x ∈R4  x0 = T ,
3
X
i=1
(xi)2 = R2o
,
where the time T ∈R and the sphere’s radius R > 0 are ﬁxed. It may be easily
veriﬁed (cf. Subsection 3.1) that the submanifold fulﬁlls the following conditions:
∥k∥= 2
R = ⟨∥k∥⟩= const ,
where ∥k∥=
p
ηαβkαkβ, and k = (kα) denotes the extrinsic curvature vector
of ST,R which is orthogonal to ST,R (cf. Deﬁnition 2.1). Throughout the paper,
⟨f⟩is the abbreviation of the mean value of a function f over its domain (here:
ST,R). Moreover, the extrinsic torsion (cf. Deﬁnition 2.1) of ST,R vanishes:
t = 0 .
2


## Page 3


Because of similarity in M0, there is an eight-parameter family of such spheres
(cf. [2, Subsection 2.5]).
Two-dimensional round spheres in M0 may be used as building blocks to
generate important geometric objects like three-hyperplanes, light cones, hyper-
boloids etc. These objects are necessary in the hamiltonian description of the
ﬁeld evolution in the special relativity, cf. [1].
In General Relativity Theory, the choice of a Cauchy hypersurface plays the
role of a speciﬁc gauge condition imposed on the hamiltonian description of the
ﬁeld evolution. An intelligent use of gauge may simplify considerably the analysis
of a physical problem (like e.g. maximal gauge in the proof of the positivity of
gravitational energy or the Bondi condition in the analysis of the radiation on
the Scri hypersurface).
A long experience supports the conjecture that the “good” hypersurface is
often a collection of “good” two-spheres (cf. [6, 8] in connection with description of
gravitational energy). This problem is important especially for an asymptotically
ﬂat spacetime, where the use of such intrinsically deﬁned surfaces could help us
to construct a “privileged” parametrization, at least far away from gravitational
sources. It would serve as a tool of a deep analysis of the structure of gravitational
radiation at inﬁnity.
Therefore a question arises, whether or not geometric conditions may be used
in case of a generic spacetime M, equipped with a non-ﬂat metric structure g, to
select a family of privileged two-surfaces.
Unfortunately, the conditions: ∥k∥−⟨∥k∥⟩= 0 and t = 0 form, in general,
an over-determined system of equations which may admit no solution. The ex-
istence of an eight-parameter family of two-surfaces fulﬁlling these equations in
the Minkowski spacetime is not a generic phenomenon but is a mere coincidence
due to the maximal symmetry of M0. In the present paper, we show how to relax
the above conditions in such a way that:
1) they admit generically an eight-parameter family of solutions and, moreover,
2) in case of the Minkowski space, the solutions are the same as before.
By analogy with the ﬂat Minkowski geometry, a generic surface satisfying our
improved condition will be called a rigid sphere.
The paper is organized as described below. In the next section, we recall some
geometric properties (extrinsic curvature and torsion, projections) of sphere-like
submanifolds in a generic four-dimensional spacetime and give the deﬁnition of
rigid spheres. The existence of such spheres is a highly nonlinear problem which
3


## Page 4


is locally solved by application of an implicit function theorem from functional
analysis. For this purpose it is necessary to analyze the linearized problem in
detail. The linearization of the nonlinear problem is carried out in Section 3
whereas Section 4 contains the derivation of crucial properties of the linearized
operator using Sobolev spaces Hk. Our main result is presented in the last section.
2
Spheres in a generic spacetime
2.1
Topological spheres
Let us consider now a generic four-dimensional spacetime manifold M with
the metric tensor g of signature (−, +, +, +). Any choice of local coordinates
(x0, . . . , x3) induces the natural basis
eα :=
∂
∂xα ,
α = 0, . . . 3
in ﬁbers of the tangent bundle TM. If v = vαeα and w = wαeα, then1 the inner
product g(v, w) on M is given by g(v, w) = gαβvαwβ, where gαβ := g(eα, eβ).
Moreover, let S ⊂M be a topological sphere, i.e. a two-dimensional subman-
ifold diﬀeomorphic to the standard unit sphere S2 ⊂R3. The diﬀeomorphism in
question F : S2 →M, it is locally described by four functions
F : (u2, u3) 7→x = (xα) ∈M , xα = xα(u2, u3) ,
(2.1)
where (uA) = (u2, u3) = (θ, φ) are standard spherical coordinates2 on S2. Using
parametrization (2.1) we may take vectors
bA = ∂Ax := ∂x
∂uA = ∂xα
∂uAeα
(2.2)
as a basis in each tangent space TxS. Consequently, the induced metric s = F ∗g
on S is represented by the metric tensor
sAB = g(bA, bB) = ∂xα
∂uA gαβ
∂xβ
∂uB .
(2.3)
Associated with metric s = (sAB), the covariant derivative
s
∇A and the Laplace-
Beltrami operator
s
∆:=
s
∇A s
∇A = sAB s
∇A
s
∇B on S are given. As usual, (sAB) is
the inverse matrix of s := (sAB).
1Einstein summation convention over repeated lower and upper indices is always assumed.
2Throughout the paper, capital letters A, B, . . .∈{2, 3}, whereas small letters a, b, . . .∈{0, 1}.
4


## Page 5


As an example of the settings above, we may take the system of spherical
coordinates in the Minkowski spacetime:
x0 = t , x1 = r sin θ cos φ , x2 = r sin θ sin φ , x3 = r cos θ ,
(2.4)
where t ∈R , r ∈[0, ∞) , θ ∈[0, π] , φ ∈[0, 2π) ,
(2.5)
and the round sphere ST,R = {t = T, r = R}. In these coordinates, Minkowski
metric reads as
ηαβdxαdxβ = −(dt)2 + (dr)2 + r2  (dθ)2 + sin2 θ(dφ)2
.
(2.6)
This formula implies that the induced metric sAB on ST,R is proportional to the
standard round metric
◦ηAB on the unit sphere S2:
sABduAduB = R2  (dθ)2 + sin2 θ(dφ)2
,
or, equivalently, sAB = R2 ◦ηAB, where
◦ηAB

:=
 
1
0
0
sin2 θ
!
.
(2.7)
2.2
Extrinsic geometry of a topological sphere
Let S ⊂M be a topological sphere. Then the extrinsic curvature tensor KAB of
S is deﬁned as the orthogonal (with respect to S) part of the covariant derivative
of the tangent vector ﬁeld bB in direction of another tangent vector bA:
KAB :=
 g
∇bAbB
⊥
∈TS⊥.
(2.8)
Especially convenient expression for the components of KAB is obtained if we
choose coordinates (xα) in a neighbourhood of S in such a way that the transversal
coordinates x0, x1 are constant on S, consequently, e2, e3 are tangent to S and
(xA) = (uA). Such coordinate system will be called adapted to S. Hence, bA = eA
and
g
∇bAbB = Gα
ABeα = Ga
ABea + GC
ABeC ,
(2.9)
with the Christoﬀel symbols Gα
βγ of metric g. Using the projection “⊥” we have
ba := e⊥
a = ea −n C
a eC ,
where
n C
a
= gaB sBC ,
(2.10)
as basis of the normal bundle TS⊥and we obtain the following formula for the
components Ka
AB of the vector KAB = Ka
ABba, valid in adapted coordinates:
Ka
AB = Ga
AB .
(2.11)
5


## Page 6


Deﬁnition 2.1. The extrinsic curvature vector k of S is deﬁned by
k = sABKAB ∈TS⊥,
(2.12)
Moreover, we consider its extrinsic torsion at the point x:
tA := g
 m,
g
∇An

,
t(x) = tAduA ∈T ∗
xS
(2.13)
where
n :=
k
∥k∥
(ﬁrst orthonormal vector),
(2.14)
∥k∥=
p
kagabkb provided k is space-like (∥k∥2 := g(k,k) > 0), and m denotes
the second orthonormal vector, i.e. the unit vector orthogonal to both k and S.
Remark 2.2. Geometrically, tA represents the connection in the bundle of or-
thonormal vectors over S. For any curve in S which is geodesic with respect to
its intrinsic geometry sAB, one might consider its “Dreibein” (v, n, m), where v
is the tangent vector to the curve. Then g(t, v) describes the angular velocity
of rotation of the “Zweibein” (n, m).
By analogy with classical Frenet-Serret
formulae, we call t the extrinsic torsion of S, which shortens considerably our
terminology.
Remark 2.3. Using adapted coordinates and setting k = kaba,
ka := sABGa
AB .
(2.15)
follows. If n = naba, we get m = maba with
ma = sabεbcnc .
(2.16)
Here, (sab) is the two-dimensional inverse to the metric (sab), which is given by
sab := g(ba, bb) = gab −n A
a n B
b gAB
(2.17)
(cf. (2.10)), and εab = |det(scd)|1/2 Eab indicates the Levi-Civita tensor for (scd)
with Eab being the sign of the permutation ( 0 1
a b ) . Of course, it is always possible
to choose an extension xA of coordinates uA from S to its neighbourhood in such
a way that ea are orthogonal to S. In this case, n A
a = 0, sab = gab, and the above
formulae simplify substantially.
6


## Page 7


Given a surface S ⊂M and a system of adapted coordinates xα, every other
surface lying suﬃciently close to S may be uniquely described by two functions
x0 = f 0(u2, u3) and x1 = f 1(u2, u3) living on S2. Any geometric condition im-
posed on a topological sphere may, therefore, be translated into a condition for
these two functions. Especially, we are going to formulate these conditions in
terms of two scalar functions, namely: the norm of the extrinsic curvature k and
the two-dimensional divergence of the extrinsic torsion t. However, mimicking
strictly the situation in the ﬂat Minkowski space, where the round spheres satisfy
two conditions: 1) ∥k∥−⟨∥k∥⟩= 0 and3 2) div t = 0, does not lead to a satisfac-
tory formulation of the problem Indeed, the above conditions are too restrictive
as it will be seen in the sequel. The main problem arises from the fact that these
conditions imply two (elliptic) diﬀerential equations for f a which, in general, do
not admit an eight-parameter family of solutions. It turns out that the correct
relaxation of these conditions, valid not only in the Minkowski geometry but also
in a generic geometry g, consists in vanishing a certain projection of the above
two characteristic functions. We deﬁne these projections in the next subsection.
2.3
Projections to eigenspaces
Let
◦
∆=
◦
∇A ◦
∇A be the standard Laplace-Beltrami operator on S2 and M3 be its
eigenspace associated to eigenvalue −2. Then M3 is a three-dimensional space
and spanned by the linear coordinate functions (2.4) on R3 restricted to S2, i.e.
M3:= span{λ1, λ2, λ3}:= span
q
3
4π sin θ cos φ,
q
3
4π sin θ sin φ,
q
3
4π cos θ

. (2.18)
Here, λ1, λ2, λ3 are spherical harmonics of degree 1 on S2 (cf. [3, 5, 10]) and
satisfy the equation
◦
∆λi = −2λi .
(2.19)
Moreover, they are normalized to form an orthonormal basis of M3 in the Hilbert
space L2(S2, do) with respect to the standard measure
do :=
q
det
◦η d2u .
(2.20)
By li = (F −1)∗(λi) we get the corresponding eigenfunctions of ∆:=
σ
∆on S =
im(F) and the corresponding space
L3(S) :=
 F −1∗(M3)
(2.21)
3By ⟨f⟩we denote the mean value of the function f over S.
7


## Page 8


where
σ :=
 F −1∗◦η
(round sphere metric),
(2.22)
dµ :=
√
det σ d2u
(round sphere measure).
(2.23)
In [2, Subsection 2.4], several projections to eigenspaces of ∆are deﬁned. They
will be applied in the next subsection.
Deﬁnition 2.4. Let f ∈L2(S, dµ).
f m := Pm(f) := 1
4π
Z
S
f dµ ∈span{1}
(monopole part) ,
(2.24)
f d := Pd(f) :=
3
X
i=1
li
Z
S
lif dµ ∈L3(S)
(dipole part) ,
(2.25)
f md := Pmd(f) := Pm(f) + Pd(f) ∈L4(S)
(mono-dipole part) ,
(2.26)
f w := (I −Pmd)(f) := f −f m −f d
(wave part) .
(2.27)
Here we set
L4(S) := span{1} ⊕L3(S) = span{1, l1, l2, l3} =
 F −1∗(M4) .
(2.28)
with M4 := span{1} ⊕M3 = span{1, λ1, λ2, λ3} being the collection of all aﬃne
functions on R3 restricted to S2.
All these expressions along with the linear functions li = (F −1)∗(λi) are
intrinsically deﬁned on S ⊂M if we use the privileged family of equilibrated,
conformally spherical isomorphisms F : S2 →M.
Such parametrizations are
constructed in [2, Subsections 2.1–2.3] and possess the following properties:
i) The metric tensor sAB on S is conformally equivalent to
◦ηAB, i.e. sAB =
p ·
◦ηAB , with a (suﬃciently smooth) positive function p on S.
ii) The dipole part of the conformal factor p vanishes, i.e. Pd(p) = 0 .
By [2, Theorem 1], each topological sphere S ⊂M admits a unique (up to
rotations) equilibrated spherical system.
Remark 2.5. Let us formulate conditions i) and ii) for the isomorphism F in dif-
ferent ways: Denoting the trace tr M and the traceless part
0
tr MAB of a covariant
tensor M = (MAB) deﬁned on S2 by
tr M :=
◦ηABMAB
and
0
tr MAB := MAB −1
2
◦ηAB tr M ,
(2.29)
8


## Page 9


respectively, we obtain p = 1
2 tr s in i). Hence, this condition is equivalent to
0
tr sAB = 0 .
(2.30)
Since all coeﬃcients in Pd(p) = 0 have to vanish, the condition ii) can be equiv-
alently rewritten in the form:
X :=
 
l1
,

l2
,

l3
= 0
(equilibration condition) .
(2.31)
As usual, the mean value of a function h on S is given by
⟨h⟩:=
Z
S
√
det s d2u
−1
·
Z
S
h
√
det s d2u .
(2.32)
We want to point out that the mean values of li with respect to another measure
vanish, too. These relations can be expressed by ⟨p−1li⟩= 0 which follows from
(2.20), (2.22), (2.23), (2.30), and
Pm(li) = 1
4π
Z
S
li dµ = 1
4π
Z
S2 λi do = 0
(2.33)
2.4
Rigid spheres
Now, we are ready to formulate our geometric conditions which we are going to
impose on two geometric scalar objects of a topological sphere S:
1) the length k := ∥k∥=
√
kasabkb of the extrinsic curvature vector, and
2) the “divergence” of the extrinsic torsion
q = div t := ∂A
√
det s sAB tB

.
(2.34)
We stress that the above quantity does not depend upon the choice of the metric
on S, within the same conformal class. Indeed, when ˜sAB = fsAB, then we have
√
det ˜s ˜sAB =
√
det s sAB. Hence, we may replace the induced metric s in the
above formula by the round sphere metric σ. The quantity q is a scalar density
which is converted into a scalar by
q :=
1
√
det σ
q ,
i.e.
q =
σ
∇AtA .
(2.35)
Deﬁnition 2.6. A topological sphere S ⊂M will be called a rigid sphere if it
possesses an equilibrated spherical parameterization F such that the curvature
vector k of S is space-like and that its both scalars k and q contain only the
9


## Page 10


mono-dipole part, i.e. if S = F(S2), where (2.30), (2.31) and the two following
equations are satisﬁed:
kw = (I −Pmd) k = 0
(curvature condition) ,
(2.36)
qw = (I −Pmd) q = 0
(torsion condition) .
(2.37)
Remark 2.7. Observe that the torsion scalar q satisﬁes the identity Pm(q) =
R
S q dµ = 0 , as a consequence of the deﬁnition (2.35). This implies that the
operator Pmd in (2.37) can be replaced by Pd. Moreover, (2.36) and (2.37) are
equivalent to
k = ∥k∥∈M4 and
q =
σ
∇AtA ∈M3 ,
respectively.4 These relations can be considered as “gauge conditions” for extrinsic
curvature and torsion. They are discussed for the linear case in [4, Appendix A].
Both conditions, (2.36) and (2.37), are fulﬁlled by the eight-parameter family
of round spheres in Minkowski space. We are going to prove in the sequel that
these are the only solutions and, moreover, that (2.36) and (2.37) admit always
an eight-parameter family of solutions if the space-time metric does not diﬀer too
much from the ﬂat Minkowski metric.
3
The linearized problem
3.1
Minkowski case
In case of the Minkowski metric g = η, the solution to our nonlinear problem
(2.30), (2.31), (2.36), and (2.37) is obvious since the round spheres S = ST,R are
rigid for all T ∈R and R > 0. To see this analytically, we set
ξ = ξ(t, r, θ, φ) = (t, r sin θ cos φ, r sin θ sin φ, r cos θ) ,
where t, r, θ, φ vary within the ranges given by (2.5). Then, for ﬁxed T, R, it is
easy to check that
the transformation
x(θ, φ) = ξ(T, R, θ, φ)
(3.1)
yields an equilibrated spherical coordinate system. Moreover,
the curvatures
κa := ηABΓa
AB
(3.2)
4Hence, Deﬁnition 2.6 coincides with [2, Deﬁnition 4].
10


## Page 11


solve equations (2.36) and (2.37) at x ∈S. Here, Γα
βγ are the Christoﬀel symbols
with respect to the basis βα := ∂αξ where
∂0ξ = ∂ξ
∂t = (1, 0, 0, 0) ,
∂1ξ = ∂ξ
∂r = (0, sin θ cos φ, sin θ sin φ, cos θ) ,
∂2ξ = ∂ξ
∂θ = (0, R cos θ cos φ, R cos θ sin φ, −R sin θ) ,
∂3ξ = ∂ξ
∂φ = (0, −R sin θ sin φ, R sin θ cos φ, 0)
(3.3)
and η(βα, βγ) = ηαγ. Hence, the induced metric of S equals to ηAB = R2 ◦ηAB.
Recall that the nonvanishing components of the Christoﬀel symbols on S are
Γ1
22 = Γr
θθ = −R , Γ1
33 = Γr
φφ = −R sin2 θ ,
Γ2
12 = Γθ
rθ = 1/R , Γ3
13 = Γφ
rφ = 1/R ,
Γ2
33 = Γθ
φφ = −sin θ cos θ , Γ3
23 = Γφ
θφ = cot θ.
(3.4)
Therefore, we have the relations:
Γ1
AB = −R
◦ηAB , ΓA
1B = 1
RδA
B .
(3.5)
By (2.15), the coordinates κa of the extrinsic curvature vector of S are given and
κ0 = 0 , κ1 = −2
R ,
p
κaηabκb = 2
R , ∇Aκa = 0 .
(3.6)
Deﬁnition 2.1 implies that, in this case, the ﬁrst orthonormal vector of S equals
to β1, the second one equals to β0, and the extrinsic torsion vector t vanishes.
Consequently, equations (2.36) and (2.37) are fulﬁlled (cf. [2, Example 3]).
To solve the nonlinear problem (2.30), (2.31), (2.36), and (2.37) in general
case of a spacetime manifold M, equipped with the metric tensor g, we apply the
implicit function theorem (cf., e.g., [11, Vol. 1]). For this purpose, it is useful to
represent these equations in the compact form
F(x, g, T, R) :=

0
tr sAB, X, kw, qw

= 0 .
(3.7)
Here, x = x(θ, φ), (θ, φ) ∈[0, π]×[0, 2π), encodes our unknown, i.e. a mapping
F : S2 →M. In a local coordinate system (xα), F is described by four functions
xα = xα(θ, φ) which belong to an appropriate function space speciﬁed later. The
nonlinear operator F acting on this space represents our conditions which ensure
that the resulting image F(S2) ⊂M is, indeed, a rigid sphere in the sense of
Deﬁnition 2.6. We are going to solve the system of equations in (3.7) separately,
for any given values of the parameters T and R > 0 (cf. Subsection 5.1).
11


## Page 12


Remark 3.1. The operator equation (3.7) consists of three algebraic equations
X = 0 and of four partial diﬀerential equations for the unknowns xα, α = 0, . . . , 3,
deﬁned on the standard sphere S2 ⊂R3.
In particular, the two equations:
0
tr sAB = 0 are of the ﬁrst diﬀerential order. The curvature equation kw = 0
is of the second order, whereas the torsion equation qw = 0 is of the fourth one.
3.2
Linearization of the conformity and equilibration con-
ditions
We will linearize the operator F in (3.7) with respect to the variable x at the
point (x, g, T, R) := (ξ, η, T, R), where ξ = ξ(T, R, θ, φ) is given by formula (3.1)
for an arbitrary value of T and η is the ﬂat Minkowski metric. Setting x = ξ +δx,
we derive explicit expressions of the (partial) Fréchet derivative
DxF(ξ, η, T, R)[δx] .
It is convenient to represent all the terms at a point x = x(θ, φ) ∈S = S(g, T, R),
with respect to the given basis β0(ξ), β1(ξ), β2(ξ), β3(ξ), βα := ∂αξ, ξ ∈S. In
particular, for δx we make the ansatz
δx = ψαβα, i.e. x = ξ + ψα(θ, φ)βα(ξ) .
(3.8)
Hence, from (3.8), (3.4), and (3.5), we get the following expression of the basis
vectors b2, b3 of the tangent space TxS:
bA(x) = ∂Ax = βA(ξ) + ∇Aψαβα(ξ)
=

1 + ψ1
R

βA +
◦
∇Aψaβa +
◦
∇AψBβB −R
◦ηABψBβ1 .
(3.9)
In the last formula, we have introduced the two-dimensional covariant derivative
◦
∇A which we apply to a vector ﬁeld (ω0, ω1, ω2, ω3) deﬁned on S2 in a splitted
way
◦
∇AωB := ∂AωB + ΓB
ACωC ,
◦
∇Aωa := ∂Aωa .
(3.10)
This means that the tangent part (ωA) of the above ﬁeld is treated as a gen-
uine vector on S2, whereas its transversal components ω0 and ω1 are treated as
“scalars”. The reason for this choice is that the “tangent-transversal” and the
“transversal-transversal” components of the four-dimensional connection will be
12


## Page 13


explicitly described in terms of the extrinsic curvature k and the extrinsic tor-
sion t. Here, we take into account only its remaining “tangent-tangent” part.
Let us notice that the Christoﬀel symbols ΓC
AB listed in (3.4) are the same as
for the standard sphere S2 equipped by the canonical metric
◦ηAB. Relation (3.9)
implies the representation of the induced metric s given by (2.3):
sAB = η(bA, bB) = ∂xα
∂uA ηαβ
∂xβ
∂uB
= R2

◦ηAB + 2ψ1
R
◦ηAB +
◦
∇AψB +
◦
∇BψA

+ O(δ2) .
(3.11)
Here and in the following, O(δ2) denotes the collection of all terms quadratic in
δx or their derivatives. If the tensor (sAB) in (3.11) is associated to a point x ∈S,
we obtain
sAB(x) = sAB(ξ) + ψα∂αsAB(ξ) + O(δ2) = sAB(ξ) + ψα∂αηAB(ξ) + O(δ2)
= R2

◦ηAB + 4ψ1
R
◦ηAB + ψC∂C
◦ηAB +
◦
∇AψB +
◦
∇BψA

+ O(δ2) , (3.12)
and immediately deduce the expansion of
0
tr sAB in conformity condition (2.30).
Proposition 3.2. The linearization (in x) of
0
tr sAB(x) = sAB(x)−1
2
◦ηAB
◦ηCDsCD

(x),
x ∈S equals to
R2
 ◦
∇AψB +
◦
∇BψA −
◦ηAB
◦
∇CψC

.
Proof. By (3.12) and
◦ηAB(x) =
◦ηAB(ξ) + ψC∂C
◦ηAB(ξ) + O(δ2), all terms in the
above expansion are obvious since
0
tr ∂C
◦ηAB(ξ) vanishes up to ﬁrst order. To see
this, observe
◦ηAB(x) =
◦ηAB(ξ) −
◦ηAD ◦ηBEψC∂C
◦ηDE

(ξ) + O(δ2) .
To linearize the average ⟨li⟩in the equilibration condition (2.31), we use the
abbreviation ⟨h⟩◦for the average of a function h deﬁned on S2, i.e.
⟨h⟩◦:= 1
4π
Z
S2 h do .
(3.13)
Proposition 3.3. The linearization (in x) of ⟨li⟩equals to

λi( 4
Rψ1 + ∂AψA)
◦.
13


## Page 14


Proof. We ﬁrst use (3.12) to get
det s(x) = R4
 
1 + 4ψ1
R
2
det
◦η + ψA∂A det
◦η + 2
◦η22
◦
∇3ψ3 + 2
◦η33
◦
∇2ψ2
!
(ξ) + O(δ2)
= R4

1 + 8ψ1
R + 2ψAΓB
AB + 2
◦
∇AψA

det
◦η + O(δ2) ,
since
◦η22 =
◦η33 det
◦η,
◦η33 =
◦η22 det
◦η, and ∂A det
◦η = 2ΓB
AB det
◦η. Expansion of
the square root yields
p
det s(x) = R2

1 + 4ψ1
R + ∂AψA
 q
det
◦η + O(δ2) ,
and hence
Z
S
li√
det s d2u = R2
Z
S2 λi

4ψ1
R + ∂AψA
 q
det
◦η d2u + O(δ2) .
In the derivation of the last formula, relations (2.22), (2.23), and (2.33) have to
be observed. Finally, by (2.32) and (3.13), the assertion follows.
3.3
Linearization of the curvature and torsion conditions
To get the linearized expression of the extrinsic curvature vector (2.12) at g =
η, we use adapted coordinates and the transformation rule for the Christoﬀel
symbols Γα
βγ(ξ), if we pass from the natural basis βα(ξ) to the basis bα(x). Let
bα = (δγ
α + bγ
α)βγ
and
βα = (δγ
α + βγ
α)bγ
(3.14)
then bγ
A follows from (3.9). To calculate bγ
a, we recall (2.10) and notice
ba = β⊥
a = βa −η(βa, bB)sBCbC = βa −∇BψaηBCβC + O(δ2)
(3.15)
by (3.9), (3.12). Hence,
bC
A =
◦
∇AψC + ψ1
R δC
A ,
bc
A =
◦
∇Aψc −R
◦ηABψBδc
1 ,
bC
a = −1
R2
◦
∇Cψbηab + ψC
R δ1
a ,
bc
a = 0 , and
βγ
α = −bγ
α + O(δ2)
in (3.14). Note (δµ
α + bµ
α)(δγ
µ + βγ
µ) = δγ
α. If Gα
βγ are the Christoﬀel symbols of the
metric η with respect to the basis bα associated to ξ ∈S, we get
Gα
βγ = (δα
λ + βα
λ)
 δµ
β + bµ
β
  δν
γ + bν
γ

Γλ
µν + (δα
ν + βα
ν ) ∂β
 δν
γ + bν
γ

.
14


## Page 15


Especially
Ga
AB(ξ) = Γa
AB + βa
CΓC
AB + bC
AΓa
CB + bC
BΓa
AC + ∂Aba
B + O(δ2)
=

1 + 2ψ1
R

Γa
AB(ξ) +
◦
∇A
◦
∇Bψa −R

2
◦
∇AψB +
◦
∇BψA

δa
1 + O(δ2) ,
(3.16)
Ga
Ac(ξ) = βa
BΓB
Ac(ξ) + bB
c Γa
AB(ξ) + O(δ2)
=

−
◦
∇Bψa + RψBδa
1

ΓB
Ac +

−1
R2
◦
∇Bψc + ψB
R δ1
c

Γa
AB + O(δ2)
= 1
R
 ◦
∇Aψcδa
1 −
◦
∇Aψaδ1
c

+ O(δ2) .
(3.17)
Here, the representation of Γα
βγ in (3.4), (3.5) and the deﬁnition (3.10) have been
exploited. Finally, we deduce
Proposition 3.4. The linearization (in x) of k(x) =
p
kasabkb(x) equals to
−1
R2(
◦
∆+ 2)ψ1 + 1
R
◦
∇AψA .
Proof. Let x ∈S. Then Ga
AB(x) expands to
Ga
AB(x) = Ga
AB(ξ) + ψα∂αGa
AB(ξ) + O(δ2) = Ga
AB + ψα∂αΓa
AB + O(δ2)
=

1 + 3ψ1
R

Γa
AB −R

ψC∂C
◦ηAB + 2
◦
∇AψB +
◦
∇BψA

δa
1 +
◦
∇A
◦
∇Bψa + O(δ2)
= −1
R

sAB(x) −Rψ1 ◦ηAB + R2 ◦
∇AψB

δa
1 +
◦
∇A
◦
∇Bψa + O(δ2)
by (3.5), (3.12), and (3.16). Use the expression of the inverse
 sAB
to matrix
(sAB) in formula (2.15) to obtain
k0(x) = 1
R2
◦
∆ψ0 + O(δ2) ,
k1(x) = −2
R + 1
R2
 ◦
∆+ 2

ψ1 −1
R
◦
∇AψA + O(δ2) .
(3.18)
Since sac = η(ba, bc) = ηac + O(δ2) by (2.17) and (3.15), we get
sac(x) = ηac(ξ) + ψα∂αsac(ξ) + O(δ2) = ηac + O(δ2)
(3.19)
and
kasabkb(x) = 4
R2

1 −1
R(
◦
∆+ 2)ψ1 +
◦
∇AψA

+ O(δ2) .
(3.20)
Taylor expansion of the square root function gives the assertion.
15


## Page 16


Proposition 3.5. The linearization (in x) of q(x) =
σ
∇AtA(x), x ∈S, equals to
−1
2R
◦
∆(
◦
∆+ 2)ψ0 .
Proof. Recall the deﬁnitions (2.14) and (2.16) of the ﬁrst and second orthonormal
vectors n, m and the relation ∥k∥= |k1| + O(δ2) by (3.18), (3.20) to derive
m0 = −n1 + O(δ2) = 1 + O(δ2) , m1 = −n0 + O(δ2) = −1
2R
◦
∆ψ0 + O(δ2) ,
g
∇An =
η
∇A (naba) =
 ∂Ana + Ga
Abnb
ba = 1
2R
 ◦
∇A
◦
∆ψ0 + 2
◦
∇Aψ0

β0 + O(δ2) .
Here, the representations of the basis ba and of the associated Christoﬀel symbols
Ga
Ab in (3.15) and (3.17), respectively, are used. From (2.13)
q =
σ
∇A

◦η
ABη(m,
g
∇Bn)

= −1
2R
◦
∇
A
m0
 ◦
∇A
◦
∆ψ0 + 2
◦
∇Aψ0

+ O(δ2) = −1
2R
◦
∆(
◦
∆+ 2)ψ0 + O(δ2)
follows. Omitting the terms in O(δ2), we ﬁnd the desired linearization.
4
Analysis of the linearized operator
4.1
The linearized operator
The propositions derived in the previous section immediately yield the Fréchet
derivative A := DxF(ξ, η, T, R) of the nonlinear operator F deﬁned in (3.7). It
is convenient to represent the operator A in the form
A = (AAB, Ai, Acurv, Ators) ,
A, B = 2, 3; i = 1, 2, 3 ,
(4.1)
where its components correspond to those ones of F in (3.7).
Theorem 4.1. Let the parameters T ∈R and R > 0 be ﬁxed and let
◦
P md (
◦
P m,
resp.
◦
P d) denote the projections Pmd (Pm, resp. Pd) transformed to S2. Then
i)
AAB[ψ]
= R2
 ◦
∇AψB +
◦
∇BψA −
◦ηAB
◦
∇CψC

on S2 ,
ii)
Ai[ψ]
=

λi( 4
Rψ1 + ∂AψA)
◦,
iii)
Acurv[ψ]
= −1
R2(
◦
∆+ 2 −2
◦
P m)ψ1 + 1
R(I −
◦
P md)
◦
∇AψA
on S2 ,
iv)
Ators[ψ]
= −1
2R
◦
∆(
◦
∆+ 2)ψ0
on S2 .
16


## Page 17


Proof. All relations are obvious. Only iii) and iv) require some comments. The
linearity of the projection I −Pmd and Proposition 3.4 imply the expression
−1
R2(I −
◦
P md)(
◦
∆+ 2)ψ1 + 1
R(I −
◦
P md)
◦
∇AψA
for the linearization of kw. Observe that, by (2.24) and (2.25),
◦
P m(f) = 1
4π
Z
S2 f do ,
◦
P d(f) =
3
X
i=1
λi
Z
S2 λif do
(4.2)
for a function f ∈L2(S2, do).
Since 1 (resp.
λi) is an eigenfunction to the
eigenvalue 0 (resp. −2 ) of the operator
◦
∆(see (2.19)), we have
◦
P m
◦
∆=
◦
∆
◦
P m = 0 ,
◦
P d
◦
∆=
◦
∆
◦
P d = −2
◦
P d .
(4.3)
Analogously, the linearization of qw follows from Proposition 3.5.
In preparation of the next section, we analyze some basic features of the
linear operator A given by (4.1). In particular, the kernel of this linear operator
is needed. For this purpose, let us solve the homogeneous linearized problem
A[ψ] = 0 by decoupling the components.
4.2
Solution of the homogeneous linearized problem
To determine the solution of A[ψ] = 0, we start with the last component Ators[ψ] =
0 which is equivalent to
(
◦
∆+ 2)
◦
∆ψ0 = 0 .
(4.4)
This says that
◦
∆ψ0 has to be an eigenfunction to the eigenvalue −2 of the operator
◦
∆, i.e.
◦
∆ψ0 ∈M3 ⊂L2(S2, do). Since f ∈L2(S2, do) is constant iﬀ
◦
∆f = 0, we
deduce
ψ0 ∈M4 .
(4.5)
The same argument is used to solve AAB[ψ] = 0 and yields the tangent part (ψA)
of the vector ﬁeld ψ. If we apply
◦
∇A to
◦
∇AψB +
◦
∇BψA −
◦ηAB
◦
∇CψC = 0 ,
(4.6)
we get
◦
∇A ◦
∇AψB + ψB = 0 .
(4.7)
17


## Page 18


Here, the covariant derivatives
◦
∇A ◦
∇B were commuted and hence the values of
curvature tensor
◦
RABCD as well as the thoses ones of Ricci tensor
◦
RAB on the
standard sphere S2 have to be observed (
◦
RAB =
◦ηAB). Due to Hodge decompo-
sition we have the representation (cf. [2, Relation (A.1)]
ψA = ∂Af (1) +
◦εA
B∂Bf (2) ,
(4.8)
where f (i), i = 1, 2, are smooth periodic functions and
◦εAB =
q
det
◦η EAB is the
Levi-Civita tensor for
◦η on S2. Using this in (4.7) and diﬀerentiating again, a
short calculation leads to the two equations
(
◦
∆+ 2)
◦
∆f (i) = 0 .
(4.9)
They are the same as (4.4) and the analogon of (4.5) says f (i) ∈M4. The result
for ψA can be written symbolically in the form
ψA ∈dM3 ⊕∗dM3
(4.10)
according to the decomposition (4.8). Let us notice that
◦
∇AψA =
◦
∆f (1) ∈M4.
Consequently, the term (I −
◦
P md)
◦
∇AψA vanishes in the equation Acurv[ψ] = 0
and
(
◦
∆+ 2 −2
◦
P m)ψ1 = 0
(4.11)
remains left. Applying
◦
∆to the both sides of (4.11), we deduce equation (4.4)
for ψ1 (instead of ψ0), and hence,
ψ1 ∈M4
(4.12)
by (4.5). Here, the ﬁrst relation of (4.3) has to be observed.
Remark 4.2. The above results (4.5), (4.10), and (4.12) show that the solutions
ψ of the homogeneous linearized problem A[ψ] = 0 generate a fourteen-parameter
family. Each component ψα is a linear combination of the spherical harmonics
λ1, λ2, λ3, and 1 or their derivatives. Altogether they contain fourteen real con-
stants independent of R, T. But, due to the three linear equations Ai[ψ] = 0,
i = 1, 2, 3, some of the constants are coupled, as we will see in the sequel. Hence,
there are eleven free parameters in the solution ψ. They can be interpreted in
the way described below.
18


## Page 19


The three parameters contained in the dipole part of
◦
∇A(
◦εABψB) represent pos-
sible rotations of the original sphere. They keep the sphere unchanged.
The
remaining eight parameters describe its possible deformations. In particular, the
monopole part of ψ1 describes change of its size due to dilation. The dipole part of
◦
∇AψA generates uniquely the dipole part of ψ1. The corresponding three param-
eters describe possible space translations of the original sphere. The monopole
part of ψ0 describes its time translation. Finally, the three parameters contained
in the dipole part of ψ0 describe its boost transformations in Minkowski space.
To solve Ai[ψ] =

λi( 4
Rψ1 + ∂AψA)
◦= 0, we exploit the representation of
the radial part ψ1 given by (4.12). Let ψ1 = c + P3
i=1 ciλi with real constants
c, c1, c2, c3. Then ⟨λiψ1⟩◦=
1
4πci since λ1, λ2, λ3 form an orthonormal system in
L2(S2, do) and ⟨λi⟩
◦= 0 by (2.33). Therefore, only the constant c is free whereas
ci = −πR

λi∂AψA◦. This and the deﬁnitions (3.13), (4.2) imply
ψ1 = c −R
4
◦
P d(∂AψA) .
(4.13)
Remark 4.3. The above calculations also show that, within the subspace M4,
the function
h = c −R
4
◦
P d(∂AψA) + πR
3
X
i=1
riλi , c ∈R ,
(4.14)
is the general solution of the inhomogeneous linear system

λi( 4
Rh + ∂AψA)
◦= ri , i = 1, 2, 3 .
(4.15)
Here, the constants ri and the ﬁeld (ψA) are given.
4.3
Properties of the linearized operator
Up to now, all unknowns in the preceding relations are assumed to be suﬃciently
smooth functions deﬁned on S2. Naturally, we may consider A as a mapping
between diﬀerent Sobolev spaces Hn := W 2,n(S2, do), n = 0, 1, . . . , which are the
collections of all functions f : S2 →R possessing generalized partial derivatives
Dβf ∈L2(S2, do) for each multiindex β with |β| ≤n. Note that Hn is a Hilbert
space with scalar product
⟨f1, f2⟩Hn =
X
|β|≤n
Z
S2 Dβf1Dβf2 do
for f1, f2 ∈Hn ,
19


## Page 20


and that the space of smooth functions is dense in each Hn with respect to the
corresponding norm. Moreover, Hn+2 is compactly imbedded in the Hölder space
Cn,ν(S2), ν ∈(0, 1), and constitutes an algebra of functions (cf., e.g., [9, Vol. 1,
pp 281]).5
In association with Hn we introduce the space T n of two-fold covariant sym-
metric traceless tensor ﬁelds living on the standard sphere S2
T n := {Z = (ZAB) |ZAB = ZBA ∈Hn for A, B ∈{2, 3}, tr Z = 0} .
(4.16)
We summarize the essential properties concerning A in the following theorem.
Theorem 4.4. Let the operator A be deﬁned by (4.1) and let D(A), N(A), R(A)
denote its domain, null space and range, respectively.
If D(A) = (H7)4, then
a)
N(A) = {ψ = (ψα)| ψ0 ∈M4, ψA ∈dM3 ⊕∗dM3, ψ1 ∈−R
4
◦
P d(∂AψA) + span{1}} .
b)
N(A) is an eleven-dimensional subspace of D(A) .
c)
R(A) = T 6 × R3 × (I −
◦
P md)H5 × (I −
◦
P md)H3 ,
where (I −
◦
P md)Hn is the L2-orthogonal complement of M4 in the subspace
Hn ⊂L2(S2, do) .
d)
A is a Fredholm operator of index 0.
Proof. Ad a),b) The assertions follows from (4.5), (4.10), (4.13) and Remark 4.2.
Ad c),d) Step 1. We follow the lines of the considerations in Subsection 4.2
which give the solution of the homogeneous problem. The arguments are based
on the properties of the operator −
◦
∆. It is non-negative, selfadjoint, and the
Fredholm alternative holds. Hence, the equation
(
◦
∆+ 2)h = f
 ◦
∆h = f

possesses a solution h ∈Hn+2 iﬀf is from Hn and is L2-orthogonal to all eigen-
functions of
◦
∆to the eigenvalue −2 (resp. 0), i.e. L2-orthogonal to λ1, λ2, λ3
(resp. to 1). This is equivalent to f ∈(I −
◦
P d)Hn (resp. f ∈(I −
◦
P m)Hn).
Hence, the assertions on the component Ators are obvious.
5Observe that [2, Theorem 2] on the existence of a unique equilibrated spherical system on a
topological sphere S2 is also valid within Sobolev framework (substitute Ck,α(S2) with Hk+2,
k ≥1).
20


## Page 21


Step 2. To see that R(AAB) = T 6, we refer to [2, Appendix A.2]. There it
is shown that the diﬀerential operator deﬁning AAB represents an isomorphism
between covector ﬁelds and symmetric traceless tensors living on S2. Only the
slight modifaction of using Sobolev spaces instead Hölder ones is necessary.
Step 3. We consider the remaining components Ai, Acurv of the operator A
and solve Ai[ψ] = si, Acurv[ψ] = g for the radial part ψ1 provided s1, s2, s3 ∈R
and g ∈(I −
◦
P md)H5 are given. The last relation reduces to
(
◦
∆+ 2 −2
◦
P m)ψ1 = f
(4.17)
or, equivalently,
◦
∆(
◦
∆+ 2)ψ1 =
◦
∆f with f ∈(I −
◦
P md)H5 .
(4.18)
Observe that
◦
P mf = 0. Step 1 implies that (4.18) has a solution ψ1 ∈H7 iﬀ
◦
∆f ∈(I −
◦
P md)H3. This condition is fulﬁlled for any f ∈(I −
◦
P md)H5 since
◦
P md
◦
∆f = −2
◦
P df = 0
by (4.3). We notice that ψ1 is not uniquely determined. In fact, if h ∈M4 , the
function ψ1 + h solves the original equation (4.17), too. Put ri = si −4
R ⟨λiψ1⟩◦
in relation (4.15) and apply Remark 4.3. Using the corresponding h from (4.14),
we obtain a solution ψ1 + h of the linear system Ai[ψ] = si, i = 1, 2, 3.
5
The nonlinear problem
5.1
Application of the implicit function theorem
The properties of the linearized operator A listed in the fundamental Theorem 4.4
enable us to apply a variant of the implicit function theorem, namely the surjec-
tive implicit function theorem (cf. [11, Vol. 1, pp 176)]. We consider the nonlinear
operator F in (3.7) as a mapping which acts on the coordinates xα ∈H7, on the
coordinates gαβ ∈H6 of the metric tensor g, and on the parameters T, R.
Theorem 5.1. There is a constant ε > 0 such that, for each metric g of M
with ∥g −η∥H6 < ε and each T ∈R, R > 0, rigid spheres S in the sense of
Deﬁnition 2.6 exist. These spheres are pertubations of the round sphere ST,R and
depend on additional eight parameters.
21


## Page 22


Proof. a) We show that the nonlinear equation (3.7) possesses a solution of the
form x = ξ + ψαβα(ξ) due to (3.8) and apply Theorem 4.H from [11, Vol. 1, pp
176]. To check the assumptions of this theorem, let the operator F be deﬁned on
the Hilbert space (H7)4 × (H6)10 × R2. Then F maps this space into the closed
subspace
H := T 6 × R3 × (I −
◦
P md)H5 × (I −
◦
P md)H3
of (H6)2 × R3 × H5 × H3. This follows from the deﬁnition of F in (3.7).
b) The crucial point is the surjectivity of A : D(A) →H by Theorem 4.4c)
and the splitting property of N(A), i.e.
D(A) = N(A) ⊕N(A)⊥.
According to this decomposition, we have
ψ = ρ + χ ,
where
ρ = (ρα) ∈N(A) , χ = (χα) ∈N(A)⊥.
(5.1)
The cited Theorem 4.H yields the existence of a solution χ of
F (ξ + ραβα(ξ) + χαβα(ξ), g, T, R) = 0 .
(5.2)
The solution depends on ρ, g, T, R and is deﬁned on a neighbourhood of (0, η, T, R).
Moreover, at this point, the vector ﬁeld χ vanishes.
Remark 5.2. The idea of application of the surjective implicit function theorem
to prove our main theorem is equivalent to the considerations in [2, Subsection
3.3], where Hölder spaces are substituted with appropriate Sobolev spaces. We
point out that an analogous result to Theorem 5.1 does also hold within Hölder
framework.
5.2
Approximation of the solution
For the readers convenience let us sketch how to construct a solution to the nonlin-
ear operator equation (3.7). This procedure also yields a method to approximate
this solution successively. It is the so-called Newton’s simpliﬁed method for (5.2),
which produces solutions of the form (5.1).
Let a metric g of M with ∥g −η∥H6 < ε be given, ﬁx T ∈R, R > 0 and
ρ ∈N(A).
Denote the approximation of the solution χ of (5.2) in the n-th
iteration step by χ(n). Then, it is recursively deﬁned by
χ(n+1) := χ(n) −B−1F
 ξ + ρ + χ(n), g, T, R

for n = 0, 1, . . . ; χ(0) = 0 , (5.3)
22


## Page 23


where B is the restriction of the linearized operator A to the orthogonal comple-
ment N(A)⊥in D(A). Since χ(n) ∈N(A)⊥, relation (5.3) is equivalent to
A

χ(n+1) −χ(n)
= B

χ(n+1) −χ(n)
= F
 ξ + ρ + χ(n), g, T, R

.
Hence, we determine a solution δ(n) of the inhomogeneous problem A[δ(n)] = F (n)
from the Hilbert space (H7)4, i.e., in each iteration step we solve the same linear
equations on S2 with diﬀerent right-hand sides
F (n) =

0
tr s(n)
AB, X(n), (I −
◦
P md)k(n), (I −
◦
P md)q(n)

:= F
 ξ + ρ + χ(n), g, T, R

.
This can be carried out by the calculations described in Subsection 4.2 and in
the proof of Theorem 4.4c). Explicitly, we get
ﬁrst δ(n)0 from
Ators[δ(n)] = (I −
◦
P md)q(n) ,
then δ(n)A from
AAB[δ(n)] =
0
tr s(n)
AB , A, B = 2, 3 ,
ﬁnally δ(n)1 from
Acurv[δ(n)] = (I −
◦
P md)k(n) ,
and
Ai[δ(n)] = X(n)i , i = 1, 2, 3 .
Note that, due to Theorem 4.4b), the general solution δ(n) contains eleven free
parameters. With δ(n) we obtain the next correction of approximation χ(n) deﬁned
in (5.3) by
χ(n+1) = χ(n) + (I −PN(A))δ(n) ,
where PN(A) denotes the projection to the null space N(A) in the domain D(A)
of the linearized operator A.
This projection rules out the ambiguity in the
parameters and χ(n+1) is uniquely determined.
Remark 5.3. The convergence of the approximating sequence χ(n) to a solution
χ of (5.2) follows from Problem 5.1 in [11, Vol. 1, p. 214] and is based on the
Banach ﬁxed point theorem.
Remark 5.4. In the eleven-dimensional space of solutions, there is a three-
dimensional subspace corresponding to pure rotations. Hence, the space of dif-
ferent rigid spheres is eight-dimensional.
Acknowledgement.
We are deeply indebted to Eberhard Zeidler, Max-Planck-
Institute for Mathematics in the Sciences, Leipzig, for fruitful discussions and
valuable help. This work was supported in part by Narodowe Centrum Nauki
(Poland) under Grant No. DEC-2011/03/B/ST1/02625.
23


## Page 24


References
[1] Chruściel, T.P., Jezierski, J., and J. Kijowski: Hamiltonian Field Theory
in the Radiating Regime. Lecture Notes in Physics. Monographs 70. Berlin:
Springer 2001
[2] Gittel, H.-P., Jezierski, J., J. Kijowski, and S.Łęski:
Rigid Spheres
in
Riemannian
Spaces.
Class.
Quantum
Grav.
30
(2013),
175010,
doi:10.1088/0264-9381/30/17/175010, 18 pp.
[3] Erdèlyi, A., Magnus, W., Oberhettinger, F., and F.G. Tricomi: Higher Tran-
scendental Functions. Vol. 3. New York: McGraw-Hill 1953
[4] Jezierski, J.: Energy and Angular Momentum of the Weak Gravitational
Waves on the Schwarzschild Background – Quasilocal Gauge-invariant For-
mulation. Gen. Rel. Grav. 31 (1999), 1855–1890
[5] Jezierski, J.: “Peeling Property” for Linearized Gravity in Null Coordinates.
Class. Quantum Grav. 19 (2002), 2463–2490
[6] Kijowski, J.: A Simple Derivation of Canonical Structure and Quasi-local
Hamiltonians in General Relativity. Gen. Rel. Grav. 29 (1997), 307–343
[7] Klainerman, S. and F. Nicolò: The Evolution Problem in General Relativity.
Birkhäuser 2003
[8] Szabados, L.: Quasi-local Energy-momentum and Angular Momentum in
GR, A Review Article. Living Rev, Relativity 7 (2004), 4
(available on the Web: http://www.livingreviews.org/lrr-2004-4)
[9] Taylor, M.E.: Partial Diﬀerential Equations. Vols. 1–3. New York: Springer
1996
[10] Triebel, H.: Höhere Analysis. Berlin: Deutscher Verlag der Wissenschaften
1972
[11] Zeidler, E.: Nonlinear Functional Analysis and Its Applications. Vols. 1–4.
New York: Springer 1988
24

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1508_07872_on_the_existence_of_rigid_spheres_in_four_dimensional_spacetime_manifolds
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2015/1508_07872_ON_THE_EXISTENCE_OF_RIGID_SPHERES_IN_FOUR_DIMENSIONAL_SPACETIME_MANIFOLDS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

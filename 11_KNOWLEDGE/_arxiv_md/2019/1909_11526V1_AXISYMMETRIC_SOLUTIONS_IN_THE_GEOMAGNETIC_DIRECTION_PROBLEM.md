---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.11526v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1909.11526v1_Axisymmetric_solutions_in_the_geomagnetic_direction_problem

> Source: 1909.11526v1_Axisymmetric_solutions_in_the_geomagnetic_direction_problem.pdf

> Pages: 67

---


## Page 1


arXiv:1909.11526v1  [math.AP]  25 Sep 2019
Axisymmetric solutions in the geomagnetic
direction problem
Ralf Kaiser+ and Tobias Ramming#
+ Fakult¨at f¨ur Mathematik und Physik, Universit¨at Bayreuth, D-95440 Bayreuth, Germany
# TNG Technology Consulting, D-85774 Unterf¨ohring, Germany
ralf.kaiser@uni-bayreuth.de, tobias.ramming@gmx.net
July, 2019
Abstract
The magnetic ﬁeld outside the earth is in good approximation a harmonic vector
ﬁeld determined by its values at the earth’s surface.
The direction problem seeks to
determine harmonic vector ﬁelds vanishing at inﬁnity and with prescribed direction of the
ﬁeld vector at the surface. In general this type of data does neither guarantee existence
nor uniqueness of solutions of the corresponding nonlinear boundary value problem. To
determine conditions for existence, to specify the non-uniqueness, and to identify cases
of uniqueness is of particular interest when modeling the earth’s (or any other celestial
body’s) magnetic ﬁeld from these data.
Here we consider the case of axisymmetric harmonic ﬁelds B outside the sphere S2 ⊂
R3. We introduce a rotation number ̺ ∈Z along a meridian of S2 for any axisymmetric
H¨older continuous direction ﬁeld D ̸= 0 on S2 and, moreover, the (exact) decay order
3 ≤δ ∈Z of any axisymmetric harmonic ﬁeld B at inﬁnity. Fixing a meridional plane
and in this plane ̺ −δ + 1 ≥0 points zn (symmetric with respect to the symmetry axis
and with |zn| > 1, n = 1, . . . , ρ −δ + 1), we prove the existence of an (up to a positive
constant factor) unique harmonic ﬁeld B vanishing at zn and nowhere else, with decay
order δ at inﬁnity, and with direction D at S2. The proof is based on the global solution
of a nonlinear elliptic boundary value problem, which arises from a complex analytic
ansatz for the axisymmetric harmonic ﬁeld in the meridional plane. The coeﬃcients of
the elliptic equation are discontinuous and singular at the symmetry axis, which requires
solution techniques that are adapted to this special situation.
Keywords: Nonlinear boundary value problem, geomagnetism, direction problem.
MSC-Classiﬁcation (2010): 35J65, 86A25.
1
Introduction
The standard boundary value problems for harmonic vector ﬁelds in exterior domains pre-
scribe besides asymptotic conditions at inﬁnity either the normal components or the tangential
components of the sought-after ﬁeld at the boundary. Well-posedness of these problems, so-
lution methods, and corresponding results on existence and uniqueness are well-known (see
e.g. Martensen 1968). Concerning the geomagnetic ﬁeld, however, these types of data are not
always available or expensive to provide. In fact, archaeomagnetic, palaeomagnetic, and even
1


## Page 2


Figure 1.1: Example of an axisymmetric direction ﬁeld (shown along two meridians on a
transparent sphere) with rotation number ̺ = 3.
historical magnetic data sets up to the 19th century contain either exclusively information
about the direction of the magnetic ﬁeld vector or provide the directional information more
reliably than information about the magnitude of the ﬁeld vector (for more information about
the signiﬁcance of the direction problem for geomagnetism, we refer to Merrill & McElhinny
1983, Proctor & Gubbins 1990, Gubbins & Herrero-Bervera 2007 and references therein). In
view of the (meanwhile well-established) fact that the geomagnetic ﬁeld diﬀered in its history
drastically from its present form (especially during “pole reversals”), a general solution theory
for large data of the direction problem would be of considerable interest.
When accepting some simpliﬁcations such as approximating the earth’s surface by the unit
sphere S2, neglecting additional sources of the harmonic ﬁeld in the exterior space E ⊂R3 of
the unit ball, and assuming discrete boundary data to be continuously interpolated all over
S2, the essence of the direction problem may be formalized as follows: Let D : S2 →R3
be a nonvanishing continuous vector ﬁeld (the “direction ﬁeld”) and δ ∈N \ {1, 2} (the
“decay order” of the harmonic ﬁeld at inﬁnity). Given a direction ﬁeld and a decay order,
the direction problem PD asks for all vector ﬁelds B ∈C1(E) ∩C(E) for which a positive
continuous function a : S2 →R+ (the “amplitude function”) exists such that the conditions
∇× B = 0,
∇· B = 0
in E,
|B(x)| = O(|x|−δ)
for |x| →∞,
B = a D
on S2





(1.1)
are satisﬁed. The decay order δ is called “exact” if |B(x)| = O(|x|−δ) but not |B(x)| =
O(|x|−(δ+1)) for |x| →∞; it will play a crucial role in the classiﬁcation of solutions. Note,
however, that usually the exact decay order is not part of the data in the direction problem
and PD is formulated with δ = 3, which is the lowest possible decay order for magnetic ﬁelds
vanishing at inﬁnity.
As is obvious from (1.1)3 the direction problem is nonlinear in the sense that there is
2


## Page 3


no linear relation between solution B and boundary data D, which means that the usual
solution techniques for the above-mentioned standard boundary value problems are not at
our disposal and, moreover, that the solution set SD for a given direction ﬁeld D is not a
linear space.
However, the problem can be slightly relaxed so that the enlarged solution
set becomes a linear space: dropping the positivity of the amplitude function deﬁnes the
“unsigned” direction problem P u
D with solution space LD ⊃SD.1
The boundary condition (1.1)3 resembles a well-investigated boundary condition, viz.,
D · B = b
on S2
with given direction ﬁeld D and scalar ﬁeld b on S2. The “oblique” case, i.e., D is nowhere
tangential to the boundary surface, is well understood and has much in common with the
standard boundary value problems (see, e.g., Lieberman 2013). For the “Poincar´e problem”,
where the obliqueness condition is violated in some part of the boundary, only partial results
are so far available and the problem seems not yet to be well understood (see, e.g., Paneah
2000). Only in two dimensions, where the Poincar´e problem for harmonic ﬁelds is known as
“Riemann-Hilbert problem”, there is a close relationship to the (unsigned) 2D-analogue of
(1.1) (see Kaiser 2010).
So far, for both, the signed and the unsigned, versions of (1.1) there are only a few results
concerning existence and uniqueness of solutions: non-uniqueness is known by examples for
the (signed and unsigned) direction problem in the axisymmetric case (Proctor & Gubbins
1990) and in the non-axisymmetric case (Kaiser 2012). For the unsigned direction problem
there is, furthermore, an upper bound on the dimension of the solution space LD in terms
of the number lD of “poles” of the direction ﬁeld D (loci on S2 with vanishing tangential
components):
dim LD ≤lD −1
(Hulot et al. 1997); in general, however, this bound is not sharp (Kaiser 2012).
In the
axisymmetric situation a better bound has been formulated in terms of rotation number and
decay order (Kaiser 2010), and that this bound is sharp will be a corollary of the present
work. Concerning the existence of solutions there is a small-data result in the axisymmetric
case (Kaiser 2010, see below) and some results for special direction ﬁelds (Kaiser & Neudert
2004). The approach in this latter reference is based on L2-expansions in spherical harmonics,
a method, which works well if the direction ﬁeld is itself a single spherical harmonic.
The present paper provides a complete solution of the axisymmetric direction problem.
The method is inspired by the solution of the two-dimensional version of this problem (Proctor
& Gubbins 1990, Kaiser 2010), which used methods of complex analysis. Axisymmetry leads -
in cylindrical coordinates ρ, ζ in a meridional plane θ = const - likewise to a two-dimensional
problem, which, although complicated by the coordinate singularity at ρ = 0, is amenable to a
complex formulation and corresponding ans¨atze. With (Bζ, Bρ) representing the nonvanishing
components of the axisymmetric harmonic ﬁeld we make the ansatz
Bζ(ζ, ρ) + i Bρ(ζ, ρ) = h(ζ + iρ) exp
1
2
 p(ζ, ρ) + i q(ζ, ρ)

(1.2)
with the given holomorphic (≜complex analytic) function h representing the zeroes and
the asymptotic behaviour of the harmonic ﬁeld, and the “correction functions” p and q.
1Sometimes, if the distinction between “signed” and “unsigned” direction problem is to be stressed, we use
the notation PD = P s
D as opposed to P u
D.
3


## Page 4


Contrary to the two-dimensional case the axisymmetric problem then requires the solution of
the following boundary value problem for the (angle-type) variable q in A∞:= {(ζ, ρ) ∈R2 :
ζ2 + ρ2 > 1} ⊂R2:
−∆q = −∂ζ
1
ρ cos(q −Ψ)

+ ∂ρ
1
ρ sin(q −Ψ)

in A∞,
q = φ
on S1,



(1.3)
where the bounded but discontinuous (angle-type) function Ψ is derived from h.
Ψ, the
boundary function φ, and the (weak) solution q are assumed to be antisymmetric with respect
to the variable ρ. The key problem with (1.3), which prevents the application of more or
less standard solution methods, is clearly the singular coeﬃcients on the right-hand side of
(1.3)1. In particular the second term on the right-hand side behaves near the symmetry axis
{ρ = 0} like a second order derivative, which has to be controlled by the left-hand side. In
(Kaiser 2010) this problem could be bypassed by a suitable embedding of the problem in
R5 that eliminated the coordinate singularity; however, at the price of a then unbounded
nonlinearity. Accordingly only a small data result could be achieved (by the Banach ﬁxed
point principle).
Unfortunately, the smallness assumptions were depending on constants
whose numerical values are unknown; so, the compatibiliy of these assumptions with the
physical data of the problem (direction ﬁeld and decay order) remained an open question.
In this paper the two-dimensional, singular, but nonlinearly bounded problem (1.3) is
directly attacked via Schauder’s ﬁxed point principle. Without smallness assumptions the
structure of the nonlinear terms must now more carefully be utilized. Key to success is a
suitable choice of auxiliarily introduced parameters at the linear as well as at the nonlinear
level of the solution procedure. At the linear level weighted Hardy-type inequalities of the
form
Z
R×R+
f
ρ

2 dζdρ
ργ
≤

2
1 + γ
2 Z
R×R+
|∂ρf|2 dζdρ
ργ
,
f ∈C∞
0 (R × R+) , γ ̸= −1
(1.4)
allow the control of the right-hand side in (1.3)1 by the left-hand side. The solution of a
linearized version of (1.3) then proceeds by a weighted Lax-Milgram-type solution criterion,
whose applicability depends on two coercivity-type constants which in turn depend on the
weight. The optimal constants are determined by min-max problems depending on γ and
further parameters. Assisted by numerical computations we derive rigorous lower bounds on
these constants with the result that the criterion works but only in a small “window” of γ-
values. At the nonlinear level, the crucial point is to devise a space large enough to comprise
the solutions of the linearized problem but not too large in order not to loose control of the
nonlinear terms. Here we make use of a weighted Lp-space and, again, only the subtle balance
between p and the weight makes Schauder’s principle work.
In a ﬁrst step, this program is carried out in the bounded regions An := {(ζ, ρ) ∈R2 :
1 < ζ2 + ρ2 < n2}, n ∈N \ {1} with artiﬁcial conditions at the exterior boundaries. The
corresponding sequence of solutions turns out to be uniformly bounded; so, in a second step, by
means of a “diagonal argument”, one then obtains a solution of (1.3) in the unbounded region
A∞. Finally, the function p is determined from q up to a constant p0, and by substitution into
(1.2) one obtains the complete set of solutions of the (signed as well as unsigned) direction
problem (1.1).
4


## Page 5


Figure 2.1: Various coordinates in the meridional cross section AR.
2
Reformulation of the problem, results, and sketch of proof
This section provides the mathematical framework for our treatment of the direction problem,
we review results from (Kaiser 2010) as far as they are relevant for the following, reduce
problem (1.1) to (1.3), and present our results in the theorems 2.1 – 2.5. Finally, we give an
outline of the proofs.
Axisymmetric harmonic vector ﬁelds B, expressed in cylindrical coordinates (ρ, θ, ζ), have
just two nontrivial components Bρ and Bζ, depending on ρ and ζ, which satisfy the system
∂ζBρ −∂ρBζ = 0,
∂ζBζ + ∂ρBρ + 1
ρ Bρ = 0.



(2.1)
So far, B is deﬁned on the half-plane H = {(ζ, ρ) ∈R2 : ρ > 0} bounded by the symme-
try axis {ρ = 0}. It is convenient, however, to extend the domain of deﬁnition to R2 by
(anti)symmetric continuation:
Bζ(ζ, −ρ) := Bζ(ζ, ρ),
Bρ(ζ, −ρ) := −Bρ(ζ, ρ)
)
(ζ, ρ) ∈H.
(2.2)
Note that (2.1)2 implies (if deﬁned) Bρ(ζ, 0) = 0.
On R2 also polar coordinates (r, ϕ) ∈
(0, ∞) × (−π, π] with basis vectors er and eϕ are useful. They are related to (ζ, ρ) by
ζ = r cos ϕ ,
ρ = r sin ϕ
(2.3)
(see Fig. 2.1). In these coordinates condition (2.2) takes the form
eBζ(r, −ϕ) = eBζ(r, ϕ),
eBρ(r, −ϕ) = −eBρ(r, ϕ),
)
(2.4)
5


## Page 6


where B(r cos ϕ, r sin ϕ) =: eB(r, ϕ). Harmonic ﬁelds are associated with harmonic potentials
Υ(r, ϕ) by
eB = ∇Υ = ∂rΥ er + 1
r ∂ϕΥ eϕ,
and these potentials have well-known series representations in A∞, which is a cross-section of
the exterior space E through the symmetry axis:
Υ(r, ϕ) =
∞
X
n=˜δ−2
cn
rn+1 Pn(cos ϕ) ,
c˜δ−2 ̸= 0 ,
˜δ ∈N \ {1, 2}
(see, e.g., Folland 1995, p. 144). Here Pn is the Legendre polynomial of order n and ˜δ ∈
N \ {1, 2} is the exact decay order of the associated magnetic ﬁeld:2
eB(r, ϕ) = eB˜δ(r, ϕ) = ∇Υ(r, ϕ) = −
∞
X
n=˜δ−2
cn
rn+2 Dn(ϕ)
= −
c˜δ−2
r˜δ
D
˜δ−2(ϕ) + O(r−(˜δ+1))
for r →∞,
(2.5)
where
Dn(ϕ) := (n + 1)Pn(cos ϕ) er + P ′
n(cos ϕ) sin ϕ eϕ
is the exterior axisymmetric 2n-pole ﬁeld restricted to the unit circle. These series are con-
verging uniformly and absolutely for any r > 1.
Axisymmetric harmonic ﬁelds have only a ﬁnite number of isolated zeroes with ﬁnite
negative indices (“x-points”) in A∞. Let these zeroes be contained in the annulus AR :=
{(ζ, ρ) ∈R : 1 < ζ2 + ρ2 < R2} ⊂A∞, then its number ν(B, AR) can be computed by
ν = ν(B, AR) = ̺ −b̺ ,
(2.6)
where ̺ and b̺ mean the rotation numbers of B along the circles S1 and SR of radii 1 and R,
respectively.3 The rotation number ̺ ∈Z counts the number of turns, the ﬁeld vector makes
when circling once around S1. In ν zeroes are counted as often as indicated by its index.
Equation (2.6) is clearly an analogue of the argument principle in complex analysis and it has
likewise some invariance properties with respect to continuous deformations (see section 9);
in particular, b̺ is constant in the limit R →∞, which yields for A∞the relation
ν = ν(B, A∞) = ̺ −˜δ + 1 .
(2.7)
As in the two-dimensional case a complex formulation of the (signed) axisymmetric direc-
tion problem is promising as it allows to view the direction of B as the argument of a complex
function f. With the identiﬁcations
ℜz := ζ ,
ℑz := ρ ,
ℜf := Bζ ,
ℑf := −Bρ ,
(2.8)
eqs. (2.1) then take the form
∂zf −1
2
f −f
z −z = 0
(2.9)
2 Exact decay orders are often denoted by ˜δ as opposed to δ for decay orders in general.
3 We skip henceforth the upper index 1 at S indicating the dimension of the “sphere”.
6


## Page 7


and the symmetry condition (2.2) amounts to
f(z, z) = f(z, z) .
(2.10)
We made there use of the Wirtinger derivatives ∂z := 1
2(∂ζ −i∂ρ) and ∂z := 1
2(∂ζ +i∂ρ) acting
on functions f : C × C →C, (z, z) 7→f(z, z). Other than in two dimensions, where harmonic
ﬁelds satisfy ∂zf = 0 (i.e., f is an analytic function), we are here left with the solution of the
singular equation (2.9).
Direction ﬁelds D : S1 →R2, ϕ 7→D(ϕ) are called symmetric, if
Dζ(ϕ) = Dζ(−ϕ) ,
Dρ(ϕ) = −Dρ(−ϕ) ,
(2.11)
and ﬁelds B and functions f are called symmetric, if they satisfy (2.2) and (2.10), respectively.
Symmetry implies obviously Dρ(0) = Dρ(π) = 0 and hence, as D ̸= 0, Dζ(0) > 0 or Dζ(0) <
0. The condition Dζ(0) > 0 is no restriction in problem (1.1) and is henceforth considered as
implied by symmetry. The axisymmetric direction problem PD = PD(A∞) then reads:
Problem PD(A∞): Let D ∈C(S1, R2) be a symmetric direction ﬁeld and δ ∈N \ {1, 2}.
Determine all symmetric solutions B ∈C1(A∞) ∩C(A∞) of (2.1) with decay order δ and
boundary condition
∃a ∈C(S1, R+) : B

S1 = a D .
(2.12)
Equivalent is the following complex formulation:
Problem P c
D(A∞): Let D ∈C(S1, R2) be a symmetric direction ﬁeld and δ ∈N \ {1, 2}.
Determine all symmetric solutions f ∈C1(A∞) ∩C(A∞) of (2.9) with decay order δ and
boundary condition
arg f

S1 = arg Dc ,
(2.13)
where Dc := Dζ −iDρ.4
The ambiguity in the arg-function is removed by the condition that ϕ 7→arg Dc is continuous
on (−π, π). We then have arg Dc(0) = 0 and arg Dc(±π) = ∓̺ π.
A bounded version of the problem reads as follows:
Problem P c
D, bD(AR): Let D ∈C(S1, R2) and bD ∈C(SR, R2) be symmetric direction ﬁelds.
Determine all symmetric solutions f ∈C1(AR) ∩C(AR) of (2.9) with boundary conditions
arg f

S1 = arg Dc ,
arg f

SR = arg bDc ,
(2.14)
where Dc := Dζ −iDρ and bDc := bDζ −i bDρ .
The basic idea to solve the direction problem is to extend the direction ﬁeld from the
boundary to the entire annulus and to replace the boundary value problem for the harmonic
ﬁeld by one for the direction ﬁeld. The direction ﬁeld, however, is in general multivalued
and not well-deﬁned at the zeroes of the harmonic ﬁeld. This suggests for the harmonic ﬁeld
4Note that the deﬁnitions of Dc here and in ref. (Kaiser 2010) diﬀer by complex conjugation.
7


## Page 8


an ansatz with a given ﬁeld describing the zeroes and by (2.6) the rotation numbers at the
boundaries, and a further zero-free ﬁeld with well-deﬁned directions on the entire annulus.
For the bounded complex problem P c
D, bD(AR) such an ansatz is
f(z, z) = h(z) eg(z,z)
(2.15)
with the analytic function
h(z) :=
̺−b̺
Y
n=1
(z −zn) z−̺
(2.16)
and the exponential function eg with well-deﬁned argument function ℑg on AR. Note that for
given direction ﬁelds D and bD and hence rotation numbers ̺ and b̺, the number of zeroes in
AR is ﬁxed by (2.6), so that the ansatz (2.15) does not restrict the solution set of P c
D, bD(AR).
However, there is a (preliminary) restriction: in order that h(z) is a symmetric function, the
set S of zeroes must be symmetric, i.e. z ∈S implies z ∈S. If zeroes on the symmetry axis
are not allowed (as it will be the case in the subsequent solution procedure), ̺ −b̺ must be
an even number (a restriction that is lifted in section 9).
When inserting (2.15) into (2.9) one obtains
−∂z g = 1
2
1
z −z
h
h e−2iℑg −1

,
(2.17)
which by further diﬀerentiation can be reduced to a semilinear elliptic equation in the variable
2ℑg =: q alone:
−∂z∂z q = ℑ
(
∂z
h
1
z −z
h
h e−iq −1
i)
.
(2.18)
As |h/h| = 1, an angle-type variable Ψ may be introduced by h/h =: eiΨ, where Ψ is a
bounded but discontinuous function on AR (see appendix A). Using the real variables (ζ, ρ)
in AR, eq. (2.18) then takes the real form
∆q −∂ζ
1
ρ
 cos(q −Ψ) −1

+ ∂ρ
1
ρ sin(q −Ψ)

= 0 ,
(2.19)
where ∆:= ∂2
ζ + ∂2
ρ. Boundary values for q on S1 arise from (2.14)–(2.16):
arg Dc = arg f|S1 =
 ̺−b̺
X
n=1
arg(z −zn) −̺ arg z + ℑg

S1
,
which give rise to the deﬁnition5
φ(ϕ) := ˜q(1, ϕ) = 2

̺ ϕ −
̺−b̺
X
n=1
arg
 eiϕ −zn

+ arg Dc(ϕ)

,
(2.20)
and analogously on SR:
bφ(ϕ) := ˜q(R, ϕ) = 2

̺ ϕ −
̺−b̺
X
n=1
arg
 R eiϕ −zn

+ arg bDc(ϕ)

.
(2.21)
5The tilde denotes again dependence on polar coordinates: ˜q(r, ϕ) := q(r cos ϕ, r sin ϕ).
8


## Page 9


Note that by construction φ(π) = φ(−π) = bφ(π) = bφ(−π) = 0, i.e. Dc ∈C(S1) implies
φ ∈C(S1), and analogously for bφ.
Once q is determined, the real part p := 2ℜg of g is given by the other half of eq. (2.17)
up to a constant p0:
−∂z p = i∂z q +
1
z −z
 e−i(q−Ψ) −1

.
(2.22)
It is useful, in particular for a weak formulation of the problem, to transform to zero
boundary conditions. To this end let Φ be a harmonic interpolation of the boundary functions,
i.e. a solution of the (standard) boundary value problem
∆Φ = 0
in AR ,
Φ

S1 = φ ,
Φ

SR = bφ ,
)
(2.23)
and deﬁne u := q −Φ, Ω:= Ψ −Φ. In these variables eq. (2.19) takes the form
∆u + ∂ζ
1
ρ
 1 −cos(u −Ω)

+ ∂ρ
1
ρ sin(u −Ω)

= 0
(2.24)
or
∇·

∇u + a[u −Ω] u
ρ

= ∇·

a[u −Ω] Ω
ρ

(2.25)
with
aζ[x] := 1 −cos x
x
,
aρ[x] := sin x
x
(2.26)
and
u

∂AR = 0 .
(2.27)
Symmetry of f and h implies
p(ζ, −ρ) = p(ζ, ρ) ,
q(ζ, −ρ) = −q(ζ, ρ) ,
(2.28)
and by (2.20), (2.21), φ(−ϕ) = −φ(ϕ), bφ(−ϕ) = −bφ(ϕ), and hence (see appendix B),
Φ(ζ, −ρ) = −Φ(ζ, ρ) ,
Ψ(ζ, −ρ) = −Ψ(ζ, ρ) ,
(2.29)
which implies, ﬁnally,
u(ζ, −ρ) = −u(ζ, ρ) ,
Ω(ζ, −ρ) = −Ω(ζ, ρ) .
(2.30)
The boundary value problem (2.25)–(2.27), and (2.30) for u with given Ωis henceforth called
problem PΩ(AR).
The divergence structure of eq. (2.25) and its non-smooth coeﬃcients suggest a weak
formulation of PΩ(AR): a function u ∈H1
0,as(AR) is called weak solution of PΩ(AR), if u
satisﬁes
Z
AR
∇u · ∇ψ dζdρ +
Z
AR
u
ρ a[u −Ω] · ∇ψ dζdρ =
Z
AR
Ω
ρ a[u −Ω] · ∇ψ dζdρ
(2.31)
for all antisymmetric testfunctions ψ ∈C∞
0,as(AR), where
C∞
0,as(AR) =

ψ ∈C∞
0 (AR) : ψ(ζ, −ρ) = −ψ(ζ, ρ)
	
9


## Page 10


and
H1
0,as(AR) = clos
 C∞
0,as(AR) , ∥∇· ∥L2(AR)

.
Note that in the bounded domain AR by (1.4) ∥∇· ∥L2 is equivalent to the usual H1-norm
∥· ∥2
H1 = ∥· ∥2
L2 + ∥∇· ∥2
L2; C∞
0 (AR) denotes as usual the space of inﬁnitely diﬀerentiable
functions compactly supported in AR. In the unbounded case a function u ∈H1
loc,as(A∞)
with trace u|S1 = 0 is called a weak solution of problem PΩ(A∞), if u satisﬁes (2.31) (with
AR replaced by A∞) for every test function ψ ∈C∞
0,as(A∞). The following theorems assert
the existence of unique weak solutions in bounded annuli AR and in the exterior plane A∞.
Theorem 2.1 Let R > 1 and Ω∈L∞(AR) with bound
|eΩ(·, ϕ)| ≤K | sin ϕ|
in AR
(2.32)
for some constant K > 0, then problem PΩ(AR) has a unique weak (in the sense of eq. (2.31))
solution u ∈H1
0,as(AR) with bound
Z
AR
|∇u|2 ρ−β dζdρ ≤C ,
(2.33)
where β = 1/5 and C is some constant that depends on K, but does not depend on R.
Theorem 2.2 Let Ω∈L∞(A∞) with bound
|eΩ(·, ϕ)| ≤K | sin ϕ|
in A∞
(2.34)
for some constant K > 0, then problem PΩ(A∞) has a unique weak solution u ∈H1
loc,as(A∞)
with trace u

S1 = 0 and the bound
Z
A∞
|∇u|2 ρ−β dζdρ ≤C
(2.35)
with β = 1/5 and some constant C > 0.
Based on these results the subsequent theorems (2.3)–(2.5) give answers to the direction
problems P c
D, bD(AR), PD(AR), and P u
D(A∞), respectively.
To this end recall that for any
continuous, symmetric direction ﬁeld the ρ-component vanishes by (2.11)2 at the symmetry
axis. The more precise condition
Dρ(ϕ) = O(ϕ)
for ϕ →0 ,
Dρ(ϕ) = O(π −ϕ)
for ϕ ր π
(2.36)
or, equivalently with Dc = Dζ −iDρ,
arg Dc(ϕ) = O(ϕ)
for ϕ →0 ,
arg Dc(ϕ) + ̺ π = O(π −ϕ)
for ϕ ր π
(2.37)
turns out to be more appropriate in the following. Moreover, H¨older continuity of D will help
to establish continuity of the solution up to the boundary.
Theorem 2.3 Let D and bD be H¨older continuous, symmetric direction ﬁelds with rotation
numbers ̺ and b̺ ∈N \ {1}, respectively, ̺ −b̺ ≥0 and even, and satisfying condition (2.36)
at the symmetry axis. Let, furthermore, {z1, . . . , z̺−b̺} be a symmetric set of points in AR.
Then, problem P c
D, bD(AR) has a unique solution f = Bζ −iBρ ≜B vanishing at z1, . . . , z̺−b̺
and nowhere else.
10


## Page 11


Theorem 2.4 Let D be a H¨older continuous, symmetric direction ﬁeld with rotation number
̺ ∈N \ {1} and satisfying condition (2.36) at the symmetry axis. Let, furthermore, ˜δ ∈
N\{1, 2}, ˜δ ≤̺+1, and {z1, . . . , z̺−˜δ+1} be a symmetric set of points in A∞. Then, problem
P c
D(A∞) has a unique solution f ≜B with exact decay order ˜δ vanishing at z1, . . . , z̺−˜δ+1
and nowhere else.
When the zeroes of a solution do not matter, the total set of solutions (with unspeciﬁed
zeroes) of the signed direction problem can best be
“counted” by means of the unsigned
problem. Let D be a H¨older continuous, symmetric direction ﬁeld with rotation number ̺
satisfying the axis-condition (2.36) and let S˜δ
D and Cδ
D be the solution sets of the signed
direction problem P s
D(A∞) with exact decay order ˜δ and (not necessarily exact) order δ,
respectively. Let furthermore, Lδ
D be the set of solutions of the unsigned problem P u
D(A∞),
then we clearly have
S
˜δ
D ⊂Cδ
D ⊂Lδ
D ,
Cδ
D =
[
δ≤˜δ≤̺+1
S
˜δ
D ,
where 3 ≤δ ≤˜δ ≤̺ + 1. Moreover, Lδ
D is a linear space, whose dimension is determined by
̺ and δ. More precisesly the following theorem holds:
Theorem 2.5 Let Sδ
D, Cδ
D, and Lδ
D be the solution sets of the signed direction problem with
exact decay order δ, of the signed problem with decay order δ, and of the unsigned problem
with decay order δ, respectively. If 3 ≤δ ≤̺ + 1, we have
Lδ
D = ⟨Cδ
D⟩= ⟨Sδ
D⟩,
(2.38)
dim Lδ
D = ̺ −δ + 2 ,
(2.39)
where ̺ is the rotation number of D and ⟨S⟩denotes the real linear span of the set S. If
δ > ̺ + 1 we have Lδ
D = {0}.
Some comments are in order:
1. Theorems 2.1 and 2.2 are robust in the sense that the theorems still hold for weights
β that vary in some interval around 1/5.
2. The restriction to an even number of zeroes in theorem 2.3 can supposedly be removed.
The physically relevant case, however, is the unbounded one, where this restriction does not
apply, and we saved us this eﬀort.
3. In view of the regularity of the data Ω(see appendix A), much more regularity than
u ∈H1
loc can not be expected.6 However, when inserting q = u + Φ into (1.2) the result will
be more regular (by exponentiation of q and by multiplication by the zeroes of h). In fact,
the harmonic vector ﬁeld B is known to be analytic in the exterior space E.
4.
According to theorems 2.3 and 2.4, all the nonuniqueness of the signed direction
problem is encoded in the arbitrary positions of the zeroes. Uniqueness (up to a positive
constant factor) in A∞is thus only guaranteed if δ = ˜δ = ̺ + 1; if the direction ﬁeld is the
only data (and hence δ = 3) this requires ̺ = 2, which holds, e.g., for “dipole-type” direction
ﬁelds.
5. The unsigned direction problem prescribes the direction of the ﬁeld vector only up to a
sign at S1. Arbitrary linear combinations of diﬀerent solutions for the same direction ﬁeld D
6 H¨older continuity of u, q, and p is shown in section 9.
11


## Page 12


-1
-0.5
0
0.5
1
-20
-10
0
10
20
aζ
x
-1
-0.5
0
0.5
1
-20
-10
0
10
20
a̺
x
Figure 2.2: Graphs of the functions aζ : x 7→(1 −cos x)/x and a̺ : x 7→sin x/x.
are thus again solutions for D, forming the linear space Lδ
D. As to the signed problem only
positive linear combinations are admissible, i.e. Cδ
D has the representation
Cδ
D =
n N
X
n=1
λn Bn : Bn ∈Cδ
D , λn > 0 , n = 1, . . . , N , N ∈N
o
,
(2.40)
which is a cone in Lδ
D.
As to the solution of problem PΩ(AR) note that it does neither have a variational form
nor does it have (obvious) monotonicity properties, but a favourable feature clearly is the
boundedness of the nonlinear term. The method of choice to obtain global solutions of PΩ(AR)
is thus to solve a suitably linearized version and to deﬁne thereby a compact mapping to which
Schauder’s ﬁxpoint principle applies. In the weak setting of eq. (2.31), linearized by replacing
a[u−Ω] by a[w−Ω] with given function w , the Lax-Milgram criterion provides easily general
solvability, if only (besides boundedness) some coercivity condition is satisﬁed. This latter
condition amounts to

Z
AR
u
ρ a · ∇u dζdρ
 ≤C ∥∇u∥2
L2(AR)
for some C < 1.
A superﬁcial estimate of the left-hand side by (1.4) with γ = 0 and
|aζ| ≤0.73, |aρ| ≤1 (see Fig. 2.2), however, fails:

Z
AR
u
ρ a · ∇u dζdρ
 ≤2

0.73 ∥∂ζu∥L2(AR)∥∂ρu∥L2(AR) + ∥∂ρu∥2
L2(AR)

.
(2.41)
A great deal of the present work is devoted to overcoming this problem by the combined eﬀect
of three measures:
(i) We introduce the variable v := ραu with suitable α > 0, which has the eﬀect that aρ is
shifted by α and allows a bound better than 1.
(ii) A ρ-dependent weight can improve the optimal constant in the Hardy inequality (1.4).
But this requires a generalized (ρ-weighted) version of the Lax-Milgram criterion.
(iii) ∂ζu and ∂ρu do not appear symmetrically in inequality (2.41).
A weighted gradient
∇d := d eζ ∂ζ + eρ ∂ρ, d > 0 can exploit this for further improvement.
12


## Page 13


Unfortunately, in the generalized Lax-Milgram criterion the coercivity condition is now
governed by constants Cc and eCc, which are deﬁned by min-max problems, viz.
Cc := inf
v sup
ψ
R
AR ∇v · ∇ψ ρ−α dζdρ
 R
AR |∇d v|2 ρ−α−γ dζdρ
1/2 R
AR |∇e ψ|2 ρ−α+γ dζdρ
1/2
(2.42)
and similarly for eCc. v and ψ vary here in diﬀerently weighted versions of H1
0(AR). The case
γ = 0, d = e = 1 corresponds to the ordinary coercivity constant Cc = 1; increasing γ leads
to decreasing Cc-values thus strengthening the coercivity condition. It needs a subtle balance
of all involved parameters (α, γ, d, and e) to meet, ﬁnally, the coercivity condition of the
generalized Lax-Milgram criterion.
To obtain suﬃciently sharp lower bounds on Cc we proceed as follows. Firstly the annular
region AR is replaced by a rectangle Q, which allows us to split the two-dimensional problem
in a sequence of one-dimensional problems in the variable ρ. The Euler-Lagrange equations for
these problems amount to low-dimensional systems of ordinary linear diﬀerential equations,
which constitute eigenvalue problems whose minimum eigenvalue bounds Cc. The numerical
solution of these equations has heuristic value in that it allows us to identify appropriate values
of the above parameters. A special case can be solved fully analytically and this solution hints
to the kind of test function that, ﬁnally, yields rigorous lower bounds on Cc suﬃcient for our
needs.
Once the solution of the linearized problem is established, a successful iteration depends
crucially on the underlying space, which is here an Lp-space that is again suitably weighted
by some power of ρ. Lp-generalizations of (1.4) of the form



 f
ρδ



2
Lp(AR) ≤C
Z
AR
|∇d f|2 dζdρ
ρβ
with as large as possible values of p and δ for given β play here a major role.
Optimal
estimates of this type in two dimensions for “small” and “large” values of p are the key to
prove continuity of the nonlinear iteration mapping. Compactness of the mapping then is a
comparatively easy consequence of well-known embedding theorems.
Schauder’s ﬁxed point principle does not provide uniqueness; so, this issue has to be faced
separately. A heuristic consideration exploiting the divergence-character of eq. (2.25) suggests
the kind of test function that would exclude nontrivial solutions of the corresponding equation
for the diﬀerence of two solutions. In fact, in order to prove rigorously uniqueness in H1
0(AR) it
takes a whole sequence of test functions and special attention has to be given to the behaviour
at the symmetry axis. In A∞the weight ̺−β in (2.35) cannot be neglegted. Starting point
is now a formulation of eq. (2.25) that incorporates the weight while keeping the divergence
structure. The proof then proceeds quite analogously to the bounded case providing, ﬁnally,
uniqueness for functions in H1
loc,as(A∞) satisfying the bound (2.35) for 0 < β < 1. Recall that
all the nonuniqueness that is typical for the solutions B of the direction problem is encoded
in the zero-positions angle Ψ, which is part of the data in eq. (2.25).
The transition from AR to the unbounded region A∞proceeds by a suitable sequence of
solutions (un) deﬁned on An with boundary values on Sn that are obtained from the exterior
harmonic potential with boundary function φ on S1. Restricting un on Am, m ≤n yields
actually a double sequence (um,n) with uniform bound (2.33). A suitably deﬁned diagonal
sequence (u(k)) then has the favourable property that u(k+1) extends u(k) deﬁned on Ak onto
13


## Page 14


Ak+1. Thus (u(k)) allows the deﬁnition of a function u on A∞that satisﬁes the bound (2.35)
and that is in fact a weak solution of PΩ(A∞). Once u and hence q are known, p is determined
by (2.22) up to a constant p0. By substitution into the ansatz (2.15) one obtains, ﬁnally, f,
which corresponds to a weakly harmonic ﬁeld B. Higher interior regularity then follows from
standard elliptic regularity theory, whereas continuity up to the boundary requires some more
subtle arguments depending on the H¨older continuity of the boundary data.
So far zeroes on the symmetry axis are not allowed mainly for the technical reason not
to loose favourable properties of the zero-positions angle Ψ at the symmetry axis. So the
number of zeroes in AR must be even, which means, e.g. for δ = 3, a restriction of possible
direction ﬁelds to those with even rotation numbers (see (2.7)).
This limitation can be
overcome by taking suitable linear combinations of “even solutions”. The coeﬃcients of a
linear combination can be viewed as “deformation parameters” that govern the positions of
the zeroes. Based on invariance properties of the degree of mapping with respect to continuous
deformations (which are recalled in this context), single zeroes can be eliminated from A∞
by “pushing” them to inﬁnity. A crucial point is here to keep control over the other zeroes,
which will move but which had to avoid the boundary.
Finally, we characterize and, in particular, determine the dimension of the solution space
of the unsigned direction problem. The presentation follows here largely the corresponding
one in the two-dimensional case in (Kaiser 2010). The basic result is that Lδ
D is generated by
an arbitrary set of ̺ −δ + 2 solutions of the signed problem with precisely 0, 1, . . . , ̺ −δ + 1
zeroes. In this sense no fundamentally new solutions appear in the unsigned problem and Lδ
D
can be viewed as a convenient way to quantify the nonuniqueness of the direction problem.
The material just described is organized in the following sections: section 3 collects the
various Hardy-type inequalities we make use of in the course of the proof. Uniqueness in the
problem PΩ, an issue that is independent of the rest of the paper, is proved in section 4.
Sections 5 and 6 are devoted to the linearized problem and, as an essential part of it, to the
min-max problem. Sections 7 and 8 present solutions of PΩin annuli AR and in the exterior
plane A∞, respectively. The direction problem itself, again in AR and in A∞, is solved in
section 9 under the restriction that no zeroes are lying on the symmetry axis. Zeroes on the
symmetry axis are discussed in section 10 and the unsigned problem in section 11. Some
more technical estimates and some additional material are deferred to a number of appen-
dices: appendices A and B contain estimates of the zero-positions angle Ψ and of the boundary
function Φ, respectively. Appendix C contains a proof of the generalized Lax-Milgram crite-
rion. Appendices D and E contain the analytic solution of a special one-dimensional min-max
problem and numerical solutions of the general one-dimensional problem, respectively. Fi-
nally, appendix F contains an explicit exemplary solution of the 2D-direction problem that
illustrates the migration of a zero.
3
Hardy-type inequalities
The results 3.1 – 3.3 are formulated for (not necessarily bounded) domains G in the n + 1-
dimensional half-space
H(n+1) := {(x1, . . . , xn, y) ∈Rn+1 : y > 0} ,
n ∈N ,
without causing additional eﬀort. All other results hold for bounded domains G ⊂H with
H := H(2) = {(x, y) ∈R2 : y > 0} .
14


## Page 15


Note for subsequent applications the correspondence (x, y) ≜(ζ, ρ).
yγ-weighted Lp-norms, especially with p = 2, play in this paper a dominant role. The
following notation is here useful:
∥· ∥p,γ :=
 Z
G
| · |p dµγ
1/p
,
dµγ := y−γdx1 . . . dxndy
(3.1)
with given domain G ⊂H(n+1), p ≥1, and γ ∈R. For p = 2 we use the simpliﬁed notation:
∥·∥2,γ =: ∥·∥γ, and for p = ∞: ∥·∥∞,0 =: ∥·∥∞. The following function spaces are associated
to these norms:
H(c)
p,γ(G) := clos
 C∞
0 (G) , ∥∇c · ∥p,γ

,
H(c)
γ (G) := H(c)
2,γ(G)
(3.2)
where
∇c := (c ∇x , ∂y) ,
c ≥0 .
For bounded G ⊂H(n+1) we have the well-known inclusion
H(c)
p,γ(G) ⊂H(c)
q,γ(G)
for p ≥q ,
as well as
H(c)
p,γ(G) ⊂H(c)
p,δ(G)
for γ ≥δ ,
(3.3)
where the latter inclusion is in fact an equivalence in the case G ⋐H, i.e. that G is compactly
contained in H. With respect to c only the diﬀerence between c = 0 and c > 0 matters:7
H(c)
p,γ(G) = H(d)
p,γ(G) ⊂H(0)
p,γ(G) ,
c, d > 0 .
The following proposition is a weighted Lp-version of Hardy’s inequality (see Hardy et al.
1952, p. 175) suitable to our needs.
Proposition 3.1 Let G ⊂H(n+1) be a domain and f ∈H(c)
p,γ(G) with γ ̸= 1 −p and p ≥1.
Then, the following inequalities hold:



f
y



p,γ ≤
p
|p + γ −1| ∥∂yf∥p,γ
(3.4)
and, especially for p = 2,



f
y



γ ≤
2
|1 + γ| ∥∂yf∥γ .
(3.5)
Proof: Let ψ ∈C∞
0 (G) ⊂C∞
0 (H) and let us deﬁne eψ ∈C∞
0 (R+) by ﬁxing (x1, . . . , xn) =
x ∈Rn in ψ:
eψ = eψx : R+ →R ,
y 7→ψ(x, y) .
Integrating by parts then yields
Z
R+
| eψ|p
yp+γ dy =
−1
p + γ −1
Z
R+
| eψ|p
1
yp+γ−1
′
dy
=
p
p + γ −1
Z
R+
| eψ|p−2 eψ eψ′
1
yp+γ−1 dy ≤
p
|p + γ −1|
Z
R+
| eψ|p−1
y(p+γ)(p−1)/p
| eψ′|
yγ/p dy
≤
p
|p + γ −1|
 Z
R+
| eψ|p
yp+γ dy
 p−1
p  Z
R+
| eψ′|p
yγ
dy
 1
p
,
7To simplify the notation we sometimes omit the upper index c, which means that c > 0, or omit the
indication of G if the underlying domain is clear from the context.
15


## Page 16


where in the last line we applied H¨older’s inequality. By cancellation one obtains
Z
R+

eψ
y

p
y−γ dy ≤

p
|p + γ −1|
p Z
R+
| eψ′|p y−γ dy .
Finally, applying Fubini’s theorem in the form
Z
H
χ(x, y) dx1 . . . dxndy =
Z
Rn
 Z
R+
eχx(y) dy

dx1 . . . dxn
yields the assertion for ψ ∈C∞
0 (G) and by approximation for f ∈H(c)
p,γ.
✷
Remark: In the case that G is contained in the half-ball B+
R ⊂H(n+1) of radius R centered
at the origin, inequality (3.4) provides immediately a Poincar´e-type inequality:
∥f∥p,γ ≤R
p
|p + γ −1| ∥∂yf∥p,γ ≤R
p
|p + γ −1| ∥∇c f∥p,γ .
(3.6)
The following lemma demonstrates that the constant in inequality (3.5) cannot be im-
proved in the case that G contains a box that touches the symmetry axis.
Lemma 3.2 (box-criterion) Let G ⊂H(n+1) be a domain and Q ⊂G a box of the form
Q = Q(n) × (a, b) ⊂Rn × R+ with 0 < a < b. Then, any admissible constant c in inequality
(3.5) satisﬁes
c ≥
1 + γ
2
2
+

π
ln(b/a)
2−1/2
.
(3.7)
In particular, if G contains a box of the form Q(n)×(0, b), the constant in (3.5) is the smallest
possible.
Proof: The smallest constant cmin in (3.5) is associated to a variational problem, viz.,
c−2
min =
inf
ψ∈C∞
0 (G)
R
G |∂yψ|2 dµγ
R
G |ψ/y|2 dµγ
.
(3.8)
It suﬃces for our purposes to consider the following simpler, one-dimensional version:
inf
f∈H1
0((a,b))
R b
a f ′2 y−γ dy
R b
a (f/y)2 y−γ dy
=: λmin .
(3.9)
Problem (3.9) is in fact a standard problem in the calculus of variation.
The associated
Euler-Lagrange equations,
f ′′ −γ
y f ′ + λ
y2 f = 0
in (a, b) ,
f = 0
at {a, b} ,
constitute an eigenvalue problem in λ, which can explicitly be solved. The minimizer in (3.9)
is the eigenfunction with smallest eigenvalue:
fmin(y) = y(1+γ)/2 sin

π ln(y/a)
ln(b/a)

,
λmin =
1 + γ
2
2
+

π
ln(b/a)
2
.
16


## Page 17


Let now eQ := eQ(n) × (a, b) be an extension of Q := Q(n) × (a, b) such that Q(n) ⋐eQ(n)
and | eQ \ Q| < ǫ. Let, furthermore, f : Q →R be given by f(·, y) = fmin(y) and ˜f be a
C1-extension onto eQ such that ˜f|∂e
Q = 0 and
max
e
Q
|∂y ˜f| ≤max
Q |∂yf| = max
[a,b] |f ′
min| .
For ˜f we then have the estimate
R
e
Q |∂y ˜f|2 dµγ
R
e
Q | ˜f/y|2 dµγ
≤
R
Q |∂yf|2 dµγ +
R
e
Q\Q |∂y ˜f|2dµγ
R
Q |f/y|2 dµγ
≤
R b
a f ′ 2
min y−γ dy
R b
a (fmin/y)2 y−γ dy
+ ǫ max[a,b]{f ′ 2
min y−γ}
R
Q |f/y|2 dµγ
≤λmin + ǫ b2(b/a)γ
|Q(n)|
max[a,b] f ′ 2
min
R b
a f 2
min dy
.
(3.10)
As C∞
0 ( eQ) is dense in H1
0( eQ) we can approximate ˜f on the left-hand side of (3.10) by ψ ∈
C∞
0 ( eQ) ⊂C∞
0 (G) and ﬁnd the inﬁmum in (3.8) be bounded from above by the right-hand
side in (3.10). As ǫ > 0 is arbitrary we thus obtain
c−2
min ≤λmin ,
which is (3.7).
If G contains a box of the form Q(n) × (0, b), the ﬁrst assertion holds for any a ∈(0, b),
i.e.
2
|1 + γ| ≤cmin ≤
2
|1 + γ| ,
which is the second assertion of the box-criterion.
✷
Inequality (3.5) allows some alternative characterizations of H(c)
γ (G), which will be useful
when dealing with the min-max problem.
Lemma 3.3 Let G ⊂H(n+1) be a domain and −1 ̸= γ ∈R. On H(c)
γ (G) we then have the
equivalence of norms
eCγ ∥∇c · ∥γ ≤∥∇c (y−γ/2 · )∥0 ≤Cγ ∥∇c · ∥γ
(3.11)
with constants
Cγ := 1 +

γ
1 + γ
 ,
eCγ := min
n
1 ,
1
|1 + γ|
o
.
Proof: By
|∂y(y−γ/2ψ)|2 =
h
|∂yψ|2 −γ ψ
y ∂yψ + γ2
4
ψ
y
2 i
y−γ,
and repeated use of (3.5) one obtains for ψ ∈C∞
0 (G):
∥∇c(y−γ/2ψ)∥2
0 ≤∥∇c ψ∥2
γ + |γ|



ψ
y



γ∥∂yψ∥γ + γ2
4



ψ
y



2
γ
≤

1 +
2 |γ|
|1 + γ| +
γ2
(1 + γ)2

∥∇c ψ∥2
γ =

1 +
|γ|
|1 + γ|
2
∥∇c ψ∥2
γ .
17


## Page 18


Similarly, by
−γ
Z
G
ψ ∂yψ y−(γ+1)dydx1 . . . dxn = −1
2 γ(γ + 1)
Z
G
ψ2y−(γ+2)dydx1 . . . dxn
and again by (3.5) one obtains
∥∇c(y−γ/2ψ)∥2
0 =
Z
G

c2|∇x ψ|2 +
1
(1 + γ)2 |∂yψ|2
y−γdx1 . . . dxndy
+

1 −
1
(1 + γ)2

∥∂yψ∥2
γ −1
2 γ(γ + 1)



ψ
y



2
γ + γ2
4



ψ
y



2
γ
≥min

1 , (1 + γ)−2	
∥∇c ψ∥2
γ + 1
4
 (1 + γ)2 −1 −2 γ(γ + 1) + γ2


ψ
y



2
γ
= min

1 , (1 + γ)−2	
∥∇c ψ∥2
γ .
✷
H1
0(G) denotes the usual Sobolev space clos
 C∞
0 (G), ∥· ∥H1

with
∥ψ∥2
H1 =
Z
G
 |ψ|2 + |∇x ψ|2 + |∂yψ|2
dx1 . . . dxndy .
By (3.6) we have thus the norm equivalence ∥· ∥H1 ∼∥∇c · ∥0 and hence the identity
H1
0(G) = H(c)
0 (G) ,
provided that G is bounded and that c > 0. More generally, for γ ̸= −1, (3.6) and (3.11)
imply under these conditions:
H(c)
γ (G) = clos
 C∞
0 (G) , ∥y−γ/2 · ∥H1

=

ψ : y−γ/2ψ ∈H1
0(G)
	
=

yγ/2χ : χ ∈H1
0(G)
	
,
(3.12)
and (3.3) implies
H(c)
γ (G) ⊂H1
0(G)
for γ ≥0 .
(3.13)
Note, ﬁnally, that H(c)
γ (G), c > 0 equipped with the scalar product
(ψ, χ) 7→
Z
G
∇c ψ · ∇c χ y−γdx1 . . . dxndy
(3.14)
is a Hilbert space, which implies in particular that H(c)
γ (G) is a reﬂexive space.
The rest of this section is devoted to inequalities of type



 f
yδ



p,0 ≤C ∥∇c f∥q,β ,
(3.15)
which will be necessary in section 7. G is now a bounded domain contained in some half-ball
B+
R ⊂H ⊂R2 and we suppose c > 0. The focus is now on “optimal values” of p and δ for
given values of q, especially for q = 2, and β.
18


## Page 19


We start with some one-dimensional inequalities, which are comparatively easy to derive.
Let f ∈H1((0, R)) with f(0) = 0. By the fundamental theorem of calculus and by H¨older’s
inequality one obtains:
|f(y)| ≤
Z y
0
|f ′| dz ≤
 Z y
0
zβ/(q−1) dz
1−1
q  Z y
0
|f ′|q z−βdz
 1
q
≤

1 +
β
q −1
 1
q −1
y1+ β−1
q
 Z y
0
|f ′|q z−βdz
 1
q
,
i.e.



 f
yδ



∞,0 ≤

1 +
β
q −1
−
 1−1
q

∥f ′∥q,β ,
(3.16)
where
δ = 1 + β −1
q
,
1 < q < ∞,
β > 1 −q .
Inequality (3.16) contains the special case
∥f y−(1+β)/2∥∞,0 ≤(1 + β)−1/2 ∥f ′∥β ,
β > −1 ,
(3.17)
and (formally) the limit cases:
∥f/y∥∞,0 ≤∥f ′∥∞,0 ,
∥f/yβ∥∞,0 ≤∥f ′∥1,β .
(3.18)
Inequality (3.18) is clear for β = 0. Otherwise we have
f(y) y−β =
Z y
0
f ′z−βdz −β
Z y
0
f z−1−βdz ,
f(y) y−β = −
Z R
y
f ′z−βdz + β
Z R
y
f z−1−βdz .
Thus, by summation and using (3.4) with p = 1 one obtains
2 |f(y)| y−β ≤
Z R
0
|f ′| z−βdz + |β|
Z R
0
(|f|/z) z−βdz ≤2
Z R
0
|f ′| z−βdz ,
which is (3.18). Finally, interpolation between (3.17) and (3.5)8 yields a (one-dimensional)
inequality of type (3.15):
Z R
0
|f/yδ|p dy =
Z R
0
f y−(1+β)/2p−2 |f/y|2 y−βdy ≤
≤∥f y−(1+β)/2∥p−2
∞,0 ∥f/y∥2
β ≤(1 + β)
2−p
2 22(1 + β)−2 ∥f ′∥p
β ,
δ := (1 + β)/2 + 1/p ,
i.e.



 f
yδ



p,0 ≤2
2
p

1
1 + β
 p+2
2p ∥f ′∥β
(3.19)
8Note that the proof of proposition 3.1 works as well for functions f : (0, R) →R without zero-boundary-
condition at R.
19


## Page 20


with
δ = 1 + β
2
+ 1
p ,
2 ≤p ≤∞,
β > −1 .
Inequalities (3.16) and (3.19) are optimal in the sense that δ cannot be enlarged as can easily
be seen by testing the inequalities with f(y) = yα.
In 2 dimensions we must proceed diﬀerently since a result of type (3.16) with q = 2 cannot
be achieved (not even for δ = β = 0). We thus assume p < ∞and distinguish, moreover,
between “small p” and “large p”.
Proposition 3.4 (small-p-case) Let G be a domain contained in B+
R ⊂H ⊂R2 and f ∈
H(c)
β (G) with β > −1. Then, the following inequality holds



 f
yδ



p,0 ≤

2
1 + β
 6−p
2p  R
c2
 p−2
2p ∥∇c f∥β
(3.20)
with
δ = β
2 + 6 −p
2p
,
2 ≤p ≤4 ,
β > −1 .
Proof: It is suﬃcient to prove (3.20) for functions ψ ∈C∞
0 (G). By (3.17) we have
|ψ(x, y)|2 y−(1+β) ≤(1 + β)−1
Z R
0
|∂yψ|2 y−βdy
and by the fundamental theorem
|ψ(x, y)|2 ≤2R
c2
Z R
−R
|c ∂xψ|2 dx .
With these estimates one obtains
Z
G
|ψ|4 y−(1+β)dµβ =
Z R
0
Z R
−R
|ψ|4 y−(1+2β)dxdy
≤
Z R
−R
sup
y

|ψ(x, y)|2 y−(1+β)	
dx ×
Z R
0
sup
x |ψ(x, y)|2 y−βdy
≤
1
1 + β
Z R
−R
Z R
0
|∂yψ|2 y−β dydx × 2R
c2
Z R
0
Z R
−R
|c ∂xψ|2 y−βdxdy
≤
2R
(1 + β)c2
 Z R
0
Z R
−R
|∇c ψ|2 y−βdxdy
2
=
2R
(1 + β)c2
 Z
G
|∇c ψ|2 dµβ
2
.
Interpolation with (3.5) then yields
Z
G
|ψ/yδ|p dxdy =
Z
G
ψ y−(1+β)/42(p−2) |ψ/y|4−p dµβ
≤
 Z
G
|ψ|4 y−(1+β)dµβ
 p−2
2  Z
G
|ψ/y|2 dµβ
 4−p
2
≤

2R
(1 + β)c2
 p−2
2 
2
1 + β
4−p Z
G
|∇c ψ|2 dµβ
 p
2
,
where we set δ := β/2 + (6 −p)/2p and made use of H¨older’s inequality in the second line.
This is (3.20).
✷
20


## Page 21


Proposition 3.5 (large-p-case) Let G be a domain contained in B+
R ⊂H ⊂R2 and f ∈
H(c)
2p
2+p , ˜β(G) with p ≥2 and ˜β > 0. Then, the following inequality holds



 f
y˜δ



p,0 ≤
p
2√c ∥∇c f∥2p
2+p , ˜β
(3.21)
with
˜δ = ˜β 2 + p
2p
,
p ≥2 ,
˜β > 0 .
Moreover, for f ∈H(c)
β (G) with β > −2/p holds



 f
yδ



p,0 ≤
p
2√c
2
ǫ R1+ǫ 1
p ∥∇c f∥β
(3.22)
with
δ = β
2 + 1 −ǫ
p
,
p ≥2 ,
β > −2
p ,
ǫ > 0 .
Proof: Let ψ ∈C∞
0 (G). We proceed similarly as in the proof of proposition 3.4, starting
this time, however, with (3.18), i.e.
|ψ(x, y)| y−β ≤
Z R
0
|∂yψ| y−βdy
and
|ψ(x, y)| ≤
Z R
−R
|∂xψ| dx .
We then obtain
Z
G
|ψ|2 y−βdµβ =
Z R
0
Z R
−R
|ψ|2 y−2βdxdy
≤
Z R
−R
sup
y

|ψ(x, y)| y−β	
dx ×
Z R
0
sup
x |ψ(x, y)| y−βdy
≤
Z R
−R
Z R
0
|∂yψ| y−β dydx × 1
c
Z R
0
Z R
−R
|c ∂xψ| y−βdxdy
≤1
c
 Z
G
|∇c ψ| dµβ
2
.
(3.23)
By approximation inequality (3.23) holds for any g ∈H(c)
1,β(G). Inserting g =: |f|p/2 and
2β =: ˜β(p/2 + 1), and using H¨older’s inequality we obtain further
 Z
G
f y−˜β/2p dµ ˜β
 1
2
≤1
√c
Z
G
∇c |f|p/22 y−(˜β/2)(p/2−1) dµ ˜β
≤
p
2√c
Z
G
f y−˜β/2p/2−1|∇c f| dµ ˜β
≤
p
2√c
 Z
G
f y−˜β/2p dµ ˜β
 p−2
2p  Z
G
|∇c f|
2p
2+p dµ ˜β
 2+p
2p
.
21


## Page 22


After cancellation we have
 Z
G
f y−˜β 2+p
2p p dxdy
 1
p
≤
p
2√c
 Z
G
|∇c f|
2p
2+p dµ ˜β
 2+p
2p
,
which is (3.21).
Using once more H¨older’s inequality the right-hand side in (3.21) can be linked up with
the L2-norm:
∥∇c f∥2p
2+p , ˜β =
 Z
G
|∇c f|
2p
2+p y−˜β dxdy
 2+p
2p
≤
 Z
G
y−(1−ǫ) dxdy
 1
p  Z
G
|∇c f|2 y−β dxdy
 1
2
≤
2R Rǫ
ǫ
 1
p ∥∇c f∥β
(3.24)
with ǫ := 1−β+(2+p)(β−˜β)/2. The necessary condition ǫ > 0 implies ˜β < β+2(1−β)/(2+p),
which in turn by ˜β > 0 implies β > −2/p. Combining (3.21) with (3.24) yields, ﬁnally, (3.22)
with δ := β/2 + (1 −ǫ)/p.
✷
4
Uniqueness in the problems PΩ(AR) and PΩ(A∞)
Uniqueness for ﬁxed function Ωmeans, in particular, uniqueness for ﬁxed boundary values
represented by the harmonic function Φ and ﬁxed set of zero-positions represented by the
angle Ψ. Together with the (up to a constant p0) unique solution of (2.22) for given q, this
implies by (2.15) an (up to a positive constant factor) unique solution f of the direction
problem.
Let u1 and u2 be weak solutions of PΩ(AR), R > 1. Then, δu := u1 −u2 satisﬁes weakly
the following “perturbation equation”:
∇·

∇δu + a′ δu
ρ

= 0
in AR ,
δu

∂AR = 0
(4.1)
with
a′
ζ := −cos(u1 −Ω) + cos(u2 −Ω) = sin
1
2 (u1 + u2) −Ω
 sin
 (u1 −u2)/2

(u1 −u2)/2
,
a′
ρ := sin(u1 −Ω) −sin(u2 −Ω) = cos
1
2 (u1 + u2) −Ω
 sin
 (u1 −u2)/2

(u1 −u2)/2
.









(4.2)
Note that given u1 and u2, a′ is here considered as a given (bounded) vector ﬁeld on AR and
(4.1) is thus a linear equation in δu.
Proposition 4.1 Let u1, u2 ∈H1
0,as(AR) be weak solutions of problem PΩ(AR) with R > 1
and Ω∈L∞(AR) satisfying the bound (2.32). Then
u1 = u2
a. e. in AR .
Proof: For functions f ∈H1
0,as(AR) we have by deﬁnition trace f

{ρ=0} = 0; it is thus
suﬃcient to consider functions f ∈H1
0(A+
R), where A+
R := AR ∩{ρ > 0} ⊂H.
22


## Page 23


Let us start with a heuristic consideration that motivates the choice of test functions we
will make use of in the following. Let δu+ := max{δu, 0} and integrate (4.1) over supp δu+:
Z
supp δu+ ∇·

∇δu+ + a′ δu+
ρ

dζdρ = 0 .
(4.3)
On the assumption that δu+ and supp δu+ are such that Gauss’ theorem is applicable one
obtains
Z
∂(supp δu+)
n · ∇δu+ds +
Z
∂(supp δu+)
n · a′ δu+
ρ ds = 0 ,
(4.4)
Where n denotes the exterior normal at ∂(supp δu+). By deﬁnition we have δu+
∂(supp δu+) = 0
and n · ∇δu+
∂(supp δu+) ≤0 and thus from (4.4) we conclude:
δu+ = ∇δu+ = 0
on ∂(supp δu+) .
(4.5)
This conclusion continues even in the case that ∂(supp δu+) ∩{ρ = 0} ̸= ∅. On that portion
of {ρ = 0} the second term in (4.4) need not vanish, but it exhibits a sign that ﬁts to that of
the ﬁrst term:
lim
ρ→0 n · a′ δu+
ρ
= −a′
ρ

ρ=0 ∂ρδu+
ρ=0 = −∂ρδu+
ρ=0 ≤0 .
At least in the real-analytic framework, (4.5) then implies by Cauchy-Kovalevskaya’s theorem
δu+ ≡0 (end of the heuristics).
Equation (4.3) suggests a test function that is constant on supp δu+. The sequence
(ψn) :=

n δu+
n δu++ 1

=

δu+
δu++ 1/n

approximates for n →∞such a test function. Note that with δu ∈H1
0(A+
R) we also have δu+
and ψn ∈H1
0(A+
R) (see, e.g., Gilbarg and Trudinger 1998, p. 152f). Testing of (4.1) by ψn
yields
0 =
Z
A+
R

∇δu + a′
ζ
δu
ρ eζ + a′
ρ
δu
ρ eρ

· ∇ψn dζdρ
= 1
n
Z
A+
R

|∇δu+|2
(δu++ 1/n)2 +
a′
ζ
ρ
δu+ ∂ζδu+
(δu++ 1/n)2 +
a′
ρ −1
ρ
+ 1
ρ
 δu+ ∂ρδu+
(δu++ 1/n)2

dζdρ ,
(4.6)
where we made use of
∇ψn =





1
n
∇δu+
(δu++ 1/n)2
on supp δu+ ,
0
else .
By rearrangement, use of Cauchy-Schwarz’s inequality and some more estimates, (4.6) takes
the form
Z
A+
R
|∇δu+|2
(δu++ 1/n)2 dζdρ +
Z
A+
R
1
ρ
δu+ ∂ρδu+
(δu++ 1/n)2 dζdρ
≤
 Z
A+
R
a′
ζ
ρ
2
dζdρ
 1
2
+
 Z
A+
R
a′
ρ −1
ρ
2
dζdρ
 1
2  Z
A+
R
|∇δu+|2
(δu++ 1/n)2 dζdρ
 1
2
.
(4.7)
23


## Page 24


0
0.2
0.4
0.6
0.8
1
0
1
2
3
4
5
f
x
∼ln x
Figure 4.1: Graph of the function f : x 7→ln(1 + x) −x/(x + 1), x ≥0.
By (4.2), (3.5), (A.7), and (B.4) the a′-related terms have the n-independent bound:
Z
A+
R
a′
ζ
ρ
2
dζdρ ≤
Z
A+
R
h1
ρ sin
1
2 (u1 + u2) −Ω
i2
dζdρ
≤
Z
A+
R
1
ρ2
1
2 (u1 + u2) −Ω
2
dζdρ ≤
Z
A+
R
hu1
ρ
2
+
u2
ρ
2i
dζdρ + 2
Z
A+
R
Ω
ρ
2
dζdρ
≤4
Z
A+
R
 |∇u1|2 + |∇u2|2
dζdρ + 4 π K2R2 =: Ca′
and similarly
Z
A+
R
a′
ρ −1
ρ
2
dζdρ ≤
Z
A+
R
1
ρ2

1 −cos
1
2 (u1 + u2) −Ω
sin
 (u1 −u2)/2

(u1 −u2)/2
2
dζdρ
≤
Z
A+
R
1
ρ2

1 −cos
1
2 (u1 + u2) −Ω

+ cos
1
2 (u1 + u2) −Ω

1 −sin
 (u1 −u2)/2

(u1 −u2)/2
2
dζdρ
≤
Z
A+
R
2
ρ2
h1
2 (u1 + u2) −Ω
2
+ 1
4(u1 −u2)2i
dζdρ ≤3 Ca′ .
The second term on the left-hand side of (4.7) is ﬁnite by (4.2) for any n ∈N,
Z
A+
R
1
ρ
δu+ ∂ρδu+
(δu++ 1/n)2 dζdρ ≤2n2
Z
A+
R
|∇δu+|2dζdρ < ∞,
and, moreover, by integrating by parts, turns out to be nonnegative (see Fig. 4.1):
Z
A+
R
1
ρ
δu+ ∂ρδu+
(δu++ 1/n)2 dζdρ =
Z
A+
R
1
ρ ∂ρ
h
1/n
δu++ 1/n −1 + ln

δu++ 1
n

−ln 1
n
i
dζdρ
=
Z
A+
R
1
ρ2
h
ln
 n δu++ 1

−
n δu+
n δu++ 1
i
dζdρ ≥0 .
(4.8)
24


## Page 25


We conclude therefore from (4.7)
Z
A+
R
|∇δu+|2
(δu++ 1/n)2 dζdρ ≤3
p
Ca′
 Z
A+
R
|∇δu+|2
(δu++ 1/n)2 dζdρ
 1
2
,
and, furthermore by (3.6):
9 Ca′ ≥
Z
A+
R
|∇δu+|2
(δu++ 1/n)2 dζdρ ≥
Z
A+
R
∇ln(1 + n δu+)
2dζdρ
≥
1
4R2
Z
A+
R
 ln(1 + n δu+)
2dζdρ .
(4.9)
The monotonically increasing sequence
 ln(1 + n δu+)

n∈N thus has a bounded sequence of
integrals, and Levi’s theorem implies convergence a.e., which in turn means δu+ = 0 a.e. This
argument works for −δu−:= −min{δu, 0} as well, which completes the proof.
✷
In the unbounded case we deal with solutions u ∈H1
loc,as(A∞) of the problem PΩ(A∞)
that satisfy a bound of the form
∥∇u∥2
β =
Z
A∞
|∇u|2ρ−β dζdρ ≤C ,
0 < β < 1
(4.10)
with weight ρ−β that cannot be neglected.
To incorporate the weight while keeping the
divergence-character of the governing equation, we rewrite eq. (2.24) in the variable v := ρβu:
∇·
 ρ−β ∇v

+ ∂ζ
h1
ρ
 1 −cos(ρ−βv −Ω)
i
+ ∂ρ
h1
ρ

sin(ρ−βv −Ω) −β ρ−βv
i
= 0 .
(4.11)
From (4.11) follows a perturbation equation for δv := v1 −v2 analogous to (4.1):
∇·
h
ρ−β
∇δv +
 a′
ζ eζ + (a′
ρ −β) eρ
δv
ρ
i
= 0
in A∞,
δv

∂A∞= 0
(4.12)
with a′ given by (4.2) and again considered as a given vector ﬁeld on A∞.
Proposition 4.2 Let u1, u2 ∈H1
loc,as(A∞) be weak solutions of problem PΩ(A∞) with van-
ishing trace on S1 and bound (4.10); let Ω∈L∞(A∞) satisfy the bound (2.34). Then
u1 = u2
a. e. in A∞.
Proof: Based on eq. (4.12) the proof proceeds quite analogously to that of proposition 4.1;
we skip thus the details. With the sequence of test functions
(ψn) :=

δv+
δv++ 1/n

one obtains instead of (4.6)
0 =
Z
A+
R

|∇δv+|2
(δv++ 1/n)2 +
a′
ζ
ρ
δv+ ∂ζδv+
(δv++ 1/n)2 +
a′
ρ −1
ρ
+ 1 −β
ρ
 δv+ ∂ρδv+
(δv++ 1/n)2

dµβ .
(4.13)
25


## Page 26


The a′-related estimates are now done by (A.8) and (B.5):
Z
A+
∞
a′
ζ
ρ
2
dµβ ≤
Z
A+
∞
hu1
ρ
2
+
u2
ρ
2i
dµβ + 2
Z
A+
R
Ω
ρ
2
dµβ
≤

2
1 + β
2 ∥∇u1∥2
β + ∥∇u2∥2
β

+
4 π K2
β(1 −β) =: eCea′ ,
and analogously for a′
ρ. The fourth term in (4.13) is still nonnegative,
(1 −β)
Z
A+
∞
1
ρ
δv+ ∂ρδv+
(δv++ 1/n)2 dµβ = (1 −β)(1 + β)
Z
A+
∞
1
ρ2 f(n δv+) dµβ ≥0 ,
and (4.9) takes the form
9 eCea′ ≥
Z
A+
∞
|∇δv+|2
(δv++ 1/n)2 dµβ ≥
Z
A+
R
∇ln(1 + n δv+)
2dµβ
≥(1 + β)2
4R2
Z
A+
R
 ln(1 + n δv+)
2dµβ
with arbitrary R > 1. By n →∞we can thus again conclude that δv+ = 0 and hence δu+ = 0
a.e. in A+
R for any R > 1.
✷
5
The linearized problem
This section is devoted to the solution of eq. (2.31) for given right-hand side and given co-
eﬃcients aζ[·] and aρ[·] of type (2.26) with measurable but otherwise not further speciﬁed
argument. Let us start with the observation that by antisymmetry it is suﬃcient to consider
(2.31) in A+
R = AR ∩{ρ > 0}. Given Ω, u ∈H1
0(A+
R) is called a weak solution of the problem
PΩ(A+
R) if u satisﬁes (2.31), with AR replaced by A+
R, for any test function ψ ∈C∞
0 (A+
R).
The equivalence with PΩ(AR) is clear when observing the one-to-one correspondence between
elements of H1
0(A+
R) and H1
0,as(AR) (by antisymmetric continuation and restriction, respec-
tively).
The general solution strategy for equations of type
Z
A+
R
∇u · ∇ψ dζdρ +
Z
A+
R
u
ρ a · ∇ψ dζdρ =
Z
A+
R
Ω
ρ a · ∇ψ dζdρ ,
(5.1)
where a abbreviates a[f] with some measurable function f : A+
R →R, is to apply a Lax-
Milgram type criterion, which requires, in particular, coerciveness of the bilinear form on the
left-hand side of (5.1). In this situation as sharp as possible bounds on a play a crucial role.
A ﬁrst step in this direction is to introduce the variable v := ραu that allows us to shift aρ
by α and thus to take advantage of the asymmetry between upper and lower bounds on aρ
(see Fig. 2.2). In fact, expressing (5.1) by v one obtains
Z
A+
R
∇v · ∇ψ dµα +
Z
A+
R
v
ρ aα· ∇ψ dµα =
Z
A+
R
Ω
ρ a · ∇ψ dζdρ
(5.2)
26


## Page 27


with dµα = ρ−αdζdρ and aα := (aζ, aρ −α). Proper choice of α “centers” aρ with the eﬀect
of an improved bound:
∥aα
ρ ∥∞= ∥aρ −α∥∞≤0.61
for α = 0.39 .
(5.3)
Obviously the bound
∥aζ∥∞≤0.73
(5.4)
on the antisymmetric function aζ cannot be improved this way.
In a second step we want to take advantage of the improved constant in the Hardy in-
equality (3.5) when weighted by a factor ρ−γ, γ > 0. Note that by the box criterion 3.2 this
constant is optimal in A+
R. The Lax-Milgram criterion must now be adapted to this weighted
situation. A suitable version is given in the following proposition whose proof is deferred to
appendix C.
Proposition 5.1 (generalized Lax-Milgram criterion) Let B and eB be reﬂexive Banach
spaces and B : B × eB →R be a continuous bilinear form, i.e. for some K > 0 holds
B(u, ˜u) ≤K ∥u∥B∥˜u∥e
B
for all u ∈B , ˜u ∈eB .
(5.5)
Let, furthermore, eB′ be the dual space of eB with norm
∥w∥e
B′ := sup
0̸=˜u∈e
B
⟨w, ˜u⟩
∥˜u∥e
B
,
(5.6)
where ⟨·, ·⟩denotes the dual pairing between eB and eB′.
Let, ﬁnally, c > 0 and ˜c > 0 be
constants such that
sup
0̸=˜u∈e
B
B(u, ˜u)
∥˜u∥e
B
≥c ∥u∥B
for all u ∈B ,
(5.7)
sup
0̸=u∈B
B(u, ˜u)
∥u∥B
≥˜c ∥˜u∥e
B
for all ˜u ∈eB .
(5.8)
Then, the equation
B(u, ˜u) = ⟨w, ˜u⟩
for all ˜u ∈eB
(5.9)
with w ∈eB′ has a unique solution u ∈B with bound
∥u∥B ≤1
c ∥w∥e
B′ .
(5.10)
Obviously, conditions (5.7) and (5.8) replace the coercivity condition B(u, u) ≥c ∥u∥2 of the
ordinary Lax-Milgram criterion for a single (Hilbert) space.
To apply the criterion we set
B := H(d)
α+γ(A+
R) ,
eB := H(e)
α−γ(A+
R) ,
with H(c)
β (G) deﬁned in (3.2) and with parameters
α ≥0 ,
γ ≥α ,
0 < d ≤1 ,
e ≥1
(5.11)
27


## Page 28


yet to be ﬁxed. The bilinear form B is given by
B[v, ψ] := B0[v, ψ] + B1[v, ψ] :=
Z
A+
R
∇v · ∇ψ dµα +
Z
A+
R
v
ρ aα · ∇ψ dµα
(5.12)
with
v ∈H(d)
α+γ(A+
R) ⊂H2α(A+
R) ⊂H1
0(A+
R) ,
ψ ∈H(e)
α−γ(A+
R) ⊃H1
0(A+
R) .
(5.13)
Condition (5.5) may easily be checked by Cauchy-Schwarz’s inequality and (3.5):
|B[v, ψ]| ≤
Z
A+
R
|∇v| ρ−(α+γ)/2 |∇ψ| ρ−(α−γ)/2 dζdρ
+
Z
A+
R
|v/ρ| ρ−(α+γ)/2 √
2 |∇ψ| ρ−(α−γ)/2 dζdρ
≤∥∇v∥α+γ ∥∇ψ∥α−γ +
√
2 ∥v/ρ∥α+γ ∥∇ψ∥α−γ
≤
1
d +
2
√
2
1 + α + γ

∥∇d v∥α+γ ∥∇eψ∥α−γ .
(5.14)
As to conditions (5.7), (5.8) note that there is no useful information about aα other than the
bounds (5.3), (5.4). In (5.12), B1 is thus considered as a perturbation of B0. The optimal
(≜largest possible) constants in (5.7), (5.8) with respect to B0 then are determined by the
following min-max problems:
inf
0̸=v∈H(d)
α+γ(A+
R)
sup
0̸=ψ∈H(e)
α−γ(A+
R)
R
A+
R ∇v · ∇ψ dµα
∥∇d v∥α+γ ∥∇e ψ∥α−γ
=: Cc ,
(5.15)
inf
0̸=ψ∈H(e)
α−γ(A+
R)
sup
0̸=v∈H(d)
α+γ(A+
R)
R
A+
R ∇v · ∇ψ dµα
∥∇d v∥α+γ ∥∇e ψ∥α−γ
=: eCc .
(5.16)
On the other side, B1 may be estimated similarly as in (5.14):

Z
A+
R
v
ρ aα· ∇ψ dµα
 ≤∥aα
ρ ∥∞
Z
A+
R
v
ρ
 ρ−(α+γ)/2  |e ∂ζψ| + |∂ρψ|

ρ−(α−γ)/2 dζdρ
≤∥aα
ρ ∥∞
2
1 + α + γ ∥∂ρv∥α+γ
√
2 ∥∇eψ∥α−γ
≤2
√
2 ∥aα
ρ ∥∞
1 + α + γ ∥∇d v∥α+γ ∥∇eψ∥α−γ ,
(5.17)
where we have set
e := ∥aζ∥∞
∥aαρ ∥∞
.
(5.18)
It is this estimate that proﬁts by the introduction of the parameters d and e; note that
any d > 0 is allowed in (5.17). Combining (5.12), (5.15), and (5.17) one obtains for any
28


## Page 29


v ∈H(d)
α+γ(A+
R):
sup
0̸=ψ∈H(e)
α−γ(A+
R)
B[v, ψ]
∥∇eψ∥α−γ
≥
sup
0̸=ψ∈H(e)
α−γ(A+
R)
 B0[v, ψ]
∥∇eψ∥α−γ
−2
√
2 ∥aα
ρ ∥∞
1 + α + γ ∥∇d v∥α+γ

≥

Cc −2
√
2 ∥aα
ρ ∥∞
1 + α + γ

∥∇d v∥α+γ ,
(5.19)
which is condition (5.7), provided that
Cc > 2
√
2 ∥aα
ρ ∥∞
1 + α + γ .
(5.20)
An analogous estimate yields
sup
0̸=v∈H(d)
α+γ(A+
R)
B[v, ψ]
∥∇d v∥α+γ
≥

eCc −2
√
2 ∥aα
ρ ∥∞
1 + α + γ

∥∇eψ∥α−γ ,
which is (5.8), provided that
eCc > 2
√
2 ∥aα
ρ ∥∞
1 + α + γ .
(5.21)
By (5.20) and (5.21) the generalized Lax-Milgram criterion 5.1 provides a solution v ∈
H(d)
α+γ(A+
R) of eq. (5.2), which by (5.6) and (5.10) satisﬁes the bound
∥∇v∥α+γ ≤1
d ∥∇d v∥α+γ ≤1
d
1
∆
sup
0̸=ψ∈H(e)
α−γ(A+
R)
R
A+
R
Ω
ρ aα· ∇ψ dζdρ
∥∇eψ∥α−γ
≤1
d
1
∆



Ω
ρ aα


γ−α ≤
√
2
∆d ∥Ω∥2+γ−α
with
∆:= Cc −2
√
2 ∥aα
ρ ∥∞
1 + α + γ .
(5.22)
Having in mind problem PΩ(A+
R) we call a function v ∈H2α(A+
R) solution of eq. (5.2) with
given measurable functions aζ, aα
ρ, Ω: A+
R →R, if v satisﬁes (5.2) for any ψ ∈C∞
0 (A+
R). By
(5.13), proposition 5.1 obviously provides a solution of this type. We summarize these results
in the following proposition.
Proposition 5.2 Let aζ, aα
ρ be bounded, measurable functions on A+
R, satisfying (5.3) and
(5.4), and let α, γ, d, e, and R be such that conditions (5.11), (5.20), and (5.21) are satisﬁed,
where Cc and eCc are given by (5.15) and (5.16), respectively. Let, furthermore, Ω: A+
R →R
be such that ∥Ω∥2+γ−α < ∞. Then, eq. (5.2) has a unique solution v ∈H(d)
α+γ(A+
R) ⊂H2α(A+
R)
satisfying the bound
∥∇d v∥α+γ ≤
√
2
∆d ∥Ω∥2+γ−α
(5.23)
with ∆given by (5.22).
29


## Page 30


By lemma 3.2 the grad-norms of u and v are related by
eCγ+α
Cγ−α
∥∇v∥α+γ ≤∥∇u∥γ−α ≤Cγ+α
eCγ−α
∥∇v∥α+γ .
(5.24)
The following corollary is thus an immediate consequence of the preceeding proposition.
Corollary 5.3 Under the conditions of proposition 5.2, eq. (5.1) has a unique solution u ∈
H1
0(A+
R) with bound
∥∇u∥γ−α ≤bC ∥Ω∥2+γ−α ,
(5.25)
where the constant bC depends on α, γ, d, e, and R.
Remark: Inequality (3.4) oﬀers yet another possibility to improve the Hardy constant: higher
Lp-spaces. The generalized Lax-Milgram criterion then is applied to conjugate Lp-spaces (see
Kaiser 2010). However, the determination of the constants corresponding to (5.15) and (5.16)
requires now the solution of systems of nonlinear partial diﬀerential equations as opposed to
the linear systems associated to (5.15) and (5.16), which are considered and solved in section
6.
6
A minimum-maximum problem
In this section the min-max problems (5.15) and (5.16) are studied in some detail with the
goal to establish parameter sets {α, γ, d, e} that satisfy the suﬃcient conditions (5.20) and
(5.21) for solvability of the linearized equation (5.2). Proposition 6.1 allows us to relate the
problem posed in A+
∞to one posed in some ﬁnite rectangle Q ⊂H. The rectangular geometry
then allows the reduction of the two-dimensional problem to a sequence of one-dimensional
ones (proposition 6.3). We determine the Euler-Lagrange equations for the two-dimensional
as well as for the one-dimensional problems and ﬁnd a common lower bound on Cc and eCc in
terms of the minimum eigenvalue associated to these equations (proposition 6.2). The analytic
solution of even the one-dimensional problems succeeds only in a special (the x-independent)
case either directly (see appendix D) or via Euler-Lagrange equations (see subsection 6.3).
Finally, based on the analytic solution, we derive explicit rigorous lower bounds on Cc and
eCc (proposition 6.4), which are corroborated by the numerical solution of the general one-
dimensional equations (see Appendix E).
Let us start with some simple observations. Using the notation
F[v, ψ] := F[v, ψ; G] :=
R
G ∇v · ∇ψ dµα
∥∇d v∥α+γ∥∇eψ∥α−γ
=
Z
G
 ∂xv ∂xψ + ∂yv ∂yψ

y−α dxdy
 Z
G
 (d ∂xv)2 + (∂yv)2
y−(α+γ)dxdy
1/2 Z
G
 (e ∂xψ)2 + (∂yψ)2
y−(α−γ)dxdy
1/2
(6.1)
and
Cc := Cc(G) := Cc(G; α, γ, d, e) :=
inf
0̸=v∈H(d)
α+γ(G)
sup
0̸=ψ∈H(e)
α−γ(G)
F[v, ψ; G] ,
(6.2)
30


## Page 31


eCc := eCc(G) := eCc(G; α, γ, d, e) :=
inf
0̸=ψ∈H(e)
α−γ(G)
sup
0̸=v∈H(d)
α+γ(G)
F[v, ψ; G] ,
(6.3)
where G ⊂H and α, γ, d, and e satisfy (5.11), one obtains by Cauchy-Schwarz’s inequality:
F[v, ψ] ≤∥∇1/e v∥α+γ ∥∇eψ∥α−γ
∥∇d v∥α+γ ∥∇eψ∥α−γ
= ∥∇1/e v∥α+γ
∥∇d v∥α+γ
.
(6.4)
Let Ix × Iy ⊂G some rectangle, β ∈R, 0 ̸≡χx ∈C∞
0 (Ix), and (χn) ⊂C∞
0 (Iy) a sequence of
test functions with
Z
Iy
χ2
n y−βdy = 1 ,
lim
n→∞
Z
Iy
χ′
n
2 y−βdy = ∞.
Setting vn(x, y) := χx(x) χn(y) ∈C∞
0 (G) and β := α + γ we ﬁnd
lim
n→∞
∥∇1/e vn∥α+γ
∥∇d vn∥α+γ
= 1 ,
(6.5)
which implies Cc ≤1. The lower bound Cc ≥0 follows for given v and ψ by proper choice of
the relative sign.
In the case γ = 0 by the choice ψ := v we obtain the lower bound
C2
c ≥
inf
0̸=v∈Hα(G)
 R
G
 (∂xv)2 + (∂yv)2
dµα
2
R
G
 (d ∂xv)2 + (∂yv)2
dµα
R
G
 (e ∂xv)2 + (∂yv)2
dµα
≥
inf
0≤s<∞
(1 + s)2
(d2 + s)(e2 + s) ,
where s denotes the ratio
R
G(∂yv)2dµα/
R
G(∂xv)2dµα. By the condition
e2d2 < d2 + e2
2
< 1
(6.6)
it is easily checked that Cc ≥1 and hence Cc(G; α, 0, d, e) = 1.
Concerning G the following scaling property of F plays an important role. Let Gλ :=
{(λx, λy) ∈H : (x, y) ∈G} and
Sλ : Hβ(G) →Hβ(Gλ) ,
f 7→fλ := f(λ−1 · ) ,
λ > 0 .
(6.7)
Obviously we then have
F[v, ψ; G] = F[vλ, ψλ; Gλ]
(6.8)
and hence Cc(G) = Cc(Gλ). In particular, applying Sλ on B+
R and A+
r0,∞:= {(x, y) ∈H :
x2 + y2 > r2
0} we ﬁnd in the limits λ →∞and λ →0, respectively,
Cc(B+
R) = Cc(H) = Cc(A+
r0,∞)
(6.9)
for any R > 0, r0 ≥0. Similary, for any rectangle Q := (−a, a) × (0, b) ⊂H holds
Cc(Q) = Cc(H) .
(6.10)
The same or similar arguments apply to eCc with identical results. We summarize these results
in the following proposition.
31


## Page 32


Proposition 6.1 Let G ⊂H and let α, γ, d, and e satisfy the conditions (5.11) and (6.6).
Then, the variational constants Cc and eCc given by (6.1)–(6.3) satisfy the bounds
0 ≤Cc ≤1 ,
0 ≤eCc ≤1 .
(6.11)
For γ = 0 holds
Cc(G; α, 0, d, e) = 1 = eCc(G; α, 0, d, e) ,
(6.12)
and Cc(H) and eCc(H) coincide with Cc and eCc, respectively, for some (bounded and un-
bounded) standard domains such as Q, B+
R, or A+
r0,∞.
6.1
Euler-Lagrange equations
Critical points of the variational expression (6.1) are (weak) solutions of the associated Euler-
Lagrange equations. We derive these equations in two steps. First we ﬁx v ∈Hα+γ(G) and
vary the functional
Z
G
∇v · ∇ψ y−α dxdy
(6.13)
with respect to ψ under the constraint ∥∇eψ∥α−γ = ∥∇d v∥α+γ. Introducing the Lagrange
parameter λ ∈R, this is equivalent to the variation of the extended functional
Z
G
∇v · ∇ψ y−α dxdy −λ
 ∥∇eψ∥2
α−γ −∥∇d v∥2
α+γ

with respect to ψ and λ (see, e.g., Courant and Hilbert 1953, vol. I, p. 216 ﬀ). Setting this
variation to zero one obtains
∇· (y−α∇v) −2 λ∇e · (y−(α−γ)∇eψ) = 0 ,
∥∇eψ∥α−γ = ∥∇d v∥α+γ .



(6.14)
In the second step we vary (6.13) under the diﬀerential constraint (6.14)1 and ∥∇d v∥α+γ = 1
with respect to v and ψ. Introducing the Lagrange multipliers p, where y−(α−γ)/2 p ∈H1(G),
and µ ∈R, this is equivalent to the variation of the extended functional
Z
G
∇v · ∇ψ y−α dxdy +
Z
G
∇p · ∇v y−α −2 λ∇e p · ∇eψ y−(α−γ) dxdy
−µ
 ∥∇d v∥2
α+γ −1

(6.15)
with respect to v, ψ, p, and µ. Setting again the variation to zero one obtains together with
(6.14)2:
∇· (y−α∇ψ) −2 µ∇d · (y−(α+γ)∇d v) + ∇· (y−α ∇p) = 0 ,
∇· (y−α∇v) −2 λ∇e · (y−(α−γ)∇e p) = 0 ,
∇· (y−α∇v) −2 λ∇e · (y−(α−γ)∇eψ) = 0 ,
y−(α−γ)/2 p

∂G = 0 ,
∥∇eψ∥α−γ = ∥∇d v∥α+γ = 1 .























(6.16)
32


## Page 33


This system is yet somewhat redundant.
By (6.16)4 and (3.12) one ﬁnds p ∈Hα−γ(G);
setting thus p := ψ makes eqs. (6.16)2,3 equivalent. Furthermore, multiplying (6.16)1 by v
and (6.16)3 by ψ and integrating over G one ﬁnds by (6.16)5 that µ = 2 λ. Finally, when
discarding conditions (6.16)5, we end up with the eigenvalue problem
∇· (y−α∇ψ) −µ∇d · (y−(α+γ)∇d v) = 0 ,
∇· (y−α∇v) −µ∇e · (y−(α−γ)∇eψ) = 0 ,



(6.17)
whose eigenvalue µ is related to the critical point (v, ψ) by
µ =
R
G ∇v · ∇ψ y−α dxdy
∥∇d v∥α+γ∥∇eψ∥α−γ
.
(6.18)
Note that stationarity of the functional (6.1) is only a necessary condition for min-max-points.
Comparing (6.18) with (5.15) we can thus only conclude that
Cc ≥µmin
where
µmin := inf { µ : µ eigenvalue of (6.17) } .
(6.19)
Repeating this procedure with v and ψ interchanged yields instead of (6.14)
∇· (y−α∇ψ) −2 λ∇d · (y−(α+γ)∇d v) = 0 ,
∥∇d v∥α+γ = ∥∇eψ∥α−γ .



(6.20)
Therefore, in the second step we vary instead of (6.15) the functional
Z
G
∇v · ∇ψ y−α dxdy +
Z
G
∇p · ∇ψ y−α −2 λ∇d p · ∇d v y−(α+γ) dxdy
−µ
 ∥∇eψ∥2
α−γ −1

(6.21)
with respect to v, ψ, p, and µ. Instead of (6.16) one obtains
∇· (y−α∇ψ) −2 λ∇d · (y−(α+γ)∇d p) = 0 ,
∇· (y−α∇v) −2 µ∇e · (y−(α−γ)∇eψ) −∇· (y−α∇p) = 0 ,
∇· (y−α∇ψ) −2 λ∇d · (y−(α+γ)∇d v) = 0 ,
y−(α+γ)/2 p

∂G = 0 ,
∥∇d v∥α+γ = ∥∇eψ∥α−γ = 1 .























(6.22)
Here, p ∈Hα+γ(G) and setting p := v makes (6.22)1,3 equivalent. As before we ﬁnd µ = 2 λ
with the result that v, ψ, and µ satisfy precisely the eqs. (6.17). We summarize these ﬁndings
in the following proposition.
33


## Page 34


Figure 6.1: The rectangle Q in the half space H.
Proposition 6.2 Let (6.15) and (6.21) be the extended functionals associated to the varia-
tional problems (5.15) and (5.16), respectively. Then both functionals share the same set of
critical points and their min-max-related critical values Cc and eCc satisfy the common lower
bound
Cc ≥µmin ,
eCc ≥µmin
(6.23)
with µmin given by (6.19). In the case of a unique critical value µ we have
Cc = µ = eCc .
(6.24)
6.2
One-dimensional min-max problems
Let us now specialize to the rectangular domain Q = (−a, a) × (0, b) (see Fig. 6.1), which
suggests the following product ansatz for the variational functions v and ψ:
v(x, y) = sn(x) vn(y)
ψ(x, y) = sn(x) ψn(y)
(6.25)
with
sn(x) :=
1
√a sin kn(x + a) ,
kn := n π
2a ,
n ∈N .
(6.26)
Note that sn obeys the boundary conditions sn(±a) = 0. Inserting (6.25) into the two-
dimensional variational expression (6.1) yields a sequence of one-dimensional expressions.
The following proposition relates the associated min-max problems with each other.
Proposition 6.3 Let sn as in (6.26) and let vn, ψn : (0, b) →R such that snvn ∈Hα+γ(Q),
snψn ∈Hα−γ(Q) for any n ∈N. Let, furthermore, F[v, ψ; G], Cc, and eCc as given in (6.1)–
(6.3). Then
Cc(Q) = inf
n∈N
inf
snvn∈Hα+γ(Q)
sup
snψn∈Hα−γ(Q)
F[snvn, snψn; Q] ,
(6.27)
eCc(Q) = inf
n∈N
inf
snψn∈Hα−γ(Q)
sup
snvn∈Hα+γ(Q)
F[snvn, snψn; Q] .
(6.28)
34


## Page 35


Proof: Let us start with the observation that {sn : n ∈N} is a complete orthonormal
set in L2((−a, a)). We may thus assume for v and ψ L2–expansions in the variable x with
coeﬃcients vn(y) and ψn(y), respectively:
v(x, y) =
∞
X
n=1
sn(x) vn(y) ,
ψ(x, y) =
∞
X
n=1
sn(x) ψn(y) .
(6.29)
Inserting (6.29) into F[v, ψ] and performing the x–integration one obtains
F[v, ψ] =
∞
X
n=1
Nn[vn, ψn]
 ∞
X
n=1
 D+
n [vn]
21/2 ∞
X
n=1
 D−
n [ψn]
21/2
(6.30)
with
Nn[vn, ψn] :=
Z b
0
 v′
nψ′
n + k2
n vnψn

y−αdy ,
D+
n [vn] :=
 Z b
0
 v′
n
2 + d2k2
n v2
n

y−(α+γ)dy
 1
2
,
D−
n [ψn] :=
 Z b
0
 ψ′
n
2 + e2k2
n ψ2
n

y−(α−γ)dy
 1
2
.
Fixing v(x, y), i.e. now ﬁxing {vn(y) : n ∈N}, and using Cauchy-Schwarz’s inequality in the
form
∞
X
n=1
an
 ∞
X
n=1
b2
n
1/2 ≤
 ∞
X
n=1
an
bn
21/2
,
bn > 0 ,
n ∈N
we may estimate:
sup
{ψn: n∈N}
∞
X
n=1
Nn[vn, ψn]
 ∞
X
n=1
 D−
n [ψn]
21/2 ≤
 ∞
X
n=1

sup
ψn
Nn[vn, ψn]
D−
n [ψn]
2!1/2
.
(6.31)
Inequality (6.31) is in fact an equality as can be seen by a more careful consideration that
makes use of an optimal choice of the relative amplitudes of the ψn. Let us demonstrate this
by just two terms. Replacing ψ2 by λ ψ2 one obtains
sup
{ψ1,ψ2}
sup
λ∈R
N1[v1, ψ1] + N2[v2, λ ψ2]
 D−
1 [ψ1]
2 +
 D−
2 [λ ψ2]
21/2 =
sup
{ψ1,ψ2}
sup
λ∈R
N1[v1, ψ1] + λ N2[v2, ψ2]
 D−
1 [ψ1]
2 + λ2 D−
2 [ψ2]
21/2
=
 
sup
ψ1
N1[v1, ψ1]
D−
1 [ψ1]
2
+ sup
ψ2
N2[v2, ψ2]
D−
2 [ψ2]
2!1/2
,
35


## Page 36


as
sup
λ∈R
a1 + λ a2
 b2
1 + λ b2
2
1/2 =
a1
b1
2
+
a2
b2
21/2
,
where w.l.o.g. we may assume a1 > 0, a2 > 0, b1 > 0, b2 > 0. Iterating this argument yields
(6.31) as equality.
Applying (6.31) as equality to (6.30) yields
inf
v∈Hα+γ(Q)
sup
ψ∈Hα−γ(Q)
F[v, ψ]
=
inf
{vn: n∈N}
1
 ∞
X
n=1
 D+
n [vn]
21/2
sup
{ψn: n∈N}
∞
X
n=1
Nn[vn, ψn]
 ∞
X
n=1
 D−
n [ψn]
21/2
=
inf
{vn: n∈N}
 ∞
X
n=1
 D+
n [vn]
2
∞
X
m=1
 D+
m[vm]
2

sup
ψn
Nn[vn, ψn]
D+
n [vn] D−
n [ψn]
2!1/2
≥inf
n∈N inf
vn sup
ψn
Nn[vn, ψn]
D+
n [vn] D−
n [ψn] .
(6.32)
On the other hand, let
 (vn, ψn)

n∈N be an optimizing sequence for the right-hand side of
(6.32). The sequence
 (snvn, snψn)

n∈N, when inserted into F[· , ·], clearly satisﬁes
F[snvn, snψn] = sup
ψ
F[snvn, ψ] ,
and hence demonstrates that
inf
v sup
ψ
F[v, ψ] ≤inf
n∈N inf
vn sup
ψn
Nn[vn, ψn]
D+
n [vn] D−
n [ψn] .
Inequality (6.32) is thus an equality, too. By (6.2) this is the assertion (6.27). With obvious
modiﬁcations these arguments apply to (6.28) as well.
✷
6.3
A one-dimensional analytical test case
An especially simple one-dimensional problem is the x-independent case. It allows a direct an-
alytic solution of the min-max problem (see appendix D). Here we consider the corresponding
Euler-Lagrange equations, which allow likewise an analytic solution. This solution is useful
to estimate the min-max value and its dependence on the parameters also in the general case
and, even more important, it gives the decisive clue how to obtain the suﬃcient lower bounds
in subsection 6.4.
Let us introduce new variables, viz.,
w := y−β+v := y−(α+γ)/2 v ,
χ := y−β−ψ := y−(α−γ)/2 ψ ,
(6.33)
36


## Page 37


which by (3.12) have the advantage to be both in H1
0. In the x-independent case system
(6.17) then takes the form
χ′′
0 −β+ −β−
y
χ′
0 −(β+ + 1)β−
y2
χ0 = µ0
h
w′′
0 −(β+ + 1)β+
y2
w0
i
,
w′′
0 + β+ −β−
y
w′
0 −(β−+ 1)β+
y2
w0 = µ0
h
χ′′
0 −(β−+ 1)β−
y2
χ0
i
.









(6.34)
A power ansatz of type
 w0
χ0

=
 a
b

yδ,
a, b, δ ∈R
is here successful and yields without diﬃculty 4 linear independent solutions:
 1
0

y−β+ ,
 0
1

y−β−,

µ0 β0
2 β+ + 1

yβ++1 ,
 2 β−+ 1
µ0 β0

yβ−+1 ,
where β0 := β+ + β−+ 1. Implementing the boundary conditions
w0(b0) = χ0(b0) = 0 ,
w0(b1) = χ0(b1) = 0 ,
0 ≤b0 < b1
yields a homogeneous 4 × 4 system in the amplitudes, whose determinant must vanish:

b−β+
0
0
µ0 β0 bβ++1
0
(2 β−+ 1) bβ−+1
0
0
b−β−
0
(2 β+ + 1) bβ++1
0
µ0 β0 bβ−+1
0
b−β+
1
0
µ0 β0 bβ++1
1
(2 β−+ 1) bβ−+1
1
0
b−β−
1
(2 β+ + 1) bβ++1
1
µ0 β0 bβ−+1
1

= 0 .
(6.35)
Equation (6.35) determines a unique nonnegative eigenvalue µ0, viz.
µ2
0 =

1 −

β+ −β−
β+ + β−+ 1
2
 1 −(b0/b1)β++β−+12
 1 −(b0/b1)2 β++1 1 −(b0/b1)2 β−+1
=

1 −

γ
1 + α
2  1 −(b0/b1)1+α
 1 −(b0/b1)1+α+γ
 1 −(b0/b1)1+α
 1 −(b0/b1)1+α−γ
= (1 + eγ)(1 −B)
1 −B1+eγ
(1 −eγ)(1 −B)
1 −B1−eγ
,
(6.36)
where in the last line we have set
eγ :=
γ
1 + α ,
B :=
b0
b1
1+α
.
As can be read oﬀ(6.36), µ0 depends only on the ratio b0/b1, which is in accordance with
the scaling property (6.8); B 7→µ0 is a monotonically increasing function on [0, 1] taking
its minimum value (1 −eγ2)1/2 at B = 0, which corresponds to an interval that touches the
origin or stretches up to inﬁnity. eγ 7→µ0 is a monotonically decreasing function on [0, ∞)
37


## Page 38


0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.5
1
1.5
2
µ0
γ
Figure 6.2: µ0 versus γ for α = 0.39 and b0/b1 = 0, 10−6, 10−4, 10−2 (from bottom to top).
with µ0 = 1 at eγ = 0 in accordance with (6.12). Figure 6.2 shows curves µ0 versus γ for some
ratios b0/b1; note that γ > 1 + α makes sense in the case that b0/b1 > 0.
Computing w0 and χ0 explicitly we ﬁnd up to positive factors and a global sign the unique
optimal pair
w0 = (1 −B)
 y
b1
1+(α+γ)/2
−
 1 −B1+eγ y
b1
1+(α−γ)/2
+ B
 1 −Beγ y
b1
−(α+γ)/2
,
χ0 =
 1 −B1−eγ y
b1
1+(α+γ)/2
−(1 −B)
 y
b1
1+(α−γ)/2
−B
 1 −B−eγ y
b1
−(α−γ)/2
with the remarkable property that w0 and χ0 conicide in the limit B = 0:
w0 =
 y
b1
1+(α+γ)/2
−
 y
b1
1+(α−γ)/2
= χ0
on (0, b1) .
(6.37)
Note, by the way, that the uniqueness of the solution according to (6.24) implies Cc = µ0 = eCc
for the x-independent versions of problems (6.2) and (6.3).
6.4
Lower bounds on Cc and eCc
Lower bounds on Cc and eCc are obtained by replacing the maximizing function by a test func-
tion leaving us with a pure minimization problem. When using the “symmetrical” variables
w and χ, the test case of the preceeding subsection suggests the kind of test function that
yields sharp bounds – at least for large domains. Note, moreover, that diﬀerently to min-max
values a pure minimum has the advantage to depend monotonically on the domain.
38


## Page 39


Let us start with rewriting the functional (6.1) in the variables (6.33).
The v-related
denominator then takes the form
D+[v] :=
 Z
G
 (d ∂xv)2 + (∂yv)2
y−(α+γ)dxdy
1/2
=
 Z
G

(d ∂xw)2 +

∂yw + β+
w
y
2 
dxdy
1/2
=
 Z
G

|∇d w|2 + δ+
w
y
2 
dxdy
1/2
=: eD+[w] ,
where we made use of the notation β± := (α ± γ)/2 and δ± := β±(β± + 1). In the last line
we applied integration by parts. Similarly one obtains
D−[ψ] :=
 Z
G
 (e ∂xψ)2 + (∂yψ)2
y−(α−γ)dxdy
1/2
=
 Z
G

|∇e χ|2 + δ−
χ
y
2 
dxdy
1/2
=: eD−[χ] ,
N[v, ψ] :=
Z
G
 ∂xv ∂xψ + ∂yv ∂yψ

dxdy
=
Z
G

∂xw ∂xχ +

∂yw + β+
w
y

∂yχ + β−
χ
y

dxdy =: e
N[w, χ] ,
and hence
F[v, ψ; G] =
e
N[w, χ]
eD+[w] eD−[χ]
=: eF[w, χ; G] .
In view of (6.37) we now replace χ by w and obtain thus a lower bound on Cc:
Cc(A+
R) =
inf
w∈H1
0(A+
R)
sup
χ∈H1
0(A+
R)
eF[w, χ; A+
R]
≥
inf
w∈H1
0(A+
R)
eF[w, w; A+
R] ≥
inf
w∈H1
0(A+
∞)
eF[w, w; A+
∞]
=
inf
w∈H1
0(H)
eF[w, w; H] =
inf
w∈H1
0(Q)
eF[w, w; Q] ,
(6.38)
where in the last line we made use of the scaling property (6.8). As in subsection 6.2 the
two-dimensional variational problem can be reduced to one dimension by expanding w into
the complete orthonormal system {sn(x) : n ∈N} with sn(x) given by (6.26):
w(x, y) =
∞
X
n=1
sn(x) wn(y) .
(6.39)
39


## Page 40


Inserting (6.39) into eD+[w] yields
eD+[w] =
 ∞
X
n=1
Z b
0

d2k2
n w2
n + w′
n
2 + δ+
wn
y
2 
dy
1/2
=
 ∞
X
n=1
kn
Z knb
0

d2 ew2
n + ew′
n
2 + δ+
 ewn
z
2 
dz
1/2
=:
 ∞
X
n=1
kn

eD+
n [ ewn]
21/2
,
where we have introduced the variables z := kny and ewn(z) := wn(y). An analogous calcula-
tion holds for eD−[w], whereas e
N[w, w] can be further simpliﬁed by integration by parts:
e
N[w, w] =
∞
X
n=1
Z b
0

k2
n w2
n +

w′
n + β+
wn
y

w′
n + β−
wn
y

dy
=
∞
X
n=1
Z b
0

k2
n w2
n + w′
n
2 + δ0
wn
y
2 
dy
=
∞
X
n=1
kn
Z knb
0

ew2
n + ew′
n
2 + δ0
 ewn
z
2 
dz
=:
∞
X
n=1
kn e
Nn[ ewn]
with the abbreviation δ0 := β+β−+ (β+ + β−)/2. Using the elementary inequality
∞
X
n=1
an
 ∞
X
n=1
b2
n
1/2 ∞
X
n=1
c2
n
1/2 ≥inf
 an
bn cn
: n ∈N

,
an ≥0 , bn > 0 , cn > 0 ,
(6.38) can thus be further estimated as follows
Cc(A+
R) ≥
inf
w∈H1
0(Q)
e
N[w, w]
eD+[w] eD−[w]
≥inf
n∈N
inf
ewn∈H1
0((0,knb))
e
Nn[ ewn]
eD+
n [ ewn] eD−
n [ ewn]
≥
inf
ew∈H1
0((0,∞))
e
N∞[ ew]
eD+
∞[ ew] eD−
∞[ ew]
,
where the index “∞” indicates the interval (0, ∞) of integration. Introducing the ratios
s :=
Z ∞
0
ew2 dz
Z ∞
0
ew′2 dz
,
t := 1
4
Z ∞
0
 ew
z
2
dz
Z ∞
0
ew′2 dz
we obtain the ﬁnal lower bound on Cc(A+
R):
Cc(A+
R) ≥
inf
0 ≤s < ∞
0 ≤t ≤1
f(s, t)
(6.40)
40


## Page 41


0.2
0.4
0.6
0.8
1
1.2
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
γ
Figure 6.3: The lower bound LB(α, γ, d, e) with e = 1.2 and d = 1 (dashed line) or d = 0.1
(solid thin line) together with the comparison function CF(α, γ) (solid thick line) and the
exact x-independent curve µ0 =
 1 −(γ/(1 + α))21/2 (dotted line). α = 0.39 has been set
throughout.
with
f(s, t) :=
1 + s + 4 δ0 t
(1 + d2s + 4 δ+ t)1/2(1 + e2s + 4 δ−t)1/2
and
δ± = (α + 1 ± γ)2 −1 ,
δ0 = (α + 1)2 −γ2 −1 .
Note that the range of t is restricted by inequality (3.5).
The minimization in (6.40) is
elementary with minima obtained either at s = 0 or t = 1 (depending on the parameters α,
γ, d, and e). Denoting this lower bound by LB = LB(α, γ, d, e), it obviously holds for eCc(A+
R)
as well and, moreover, for any R > 1.
According to (5.20), (5.21) this bound has to be compared with the “comparison function”
CF(α, γ) := 2
√
2 ∥aρ −α∥∞
1 + α + γ
.
Figure 6.3 displays the curves γ 7→LB(0.39, γ, d, 1.2) for d = 1 and 0.1 together with γ 7→
CF(0.39, γ), where α and e have been ﬁxed according to (5.3), (5.4), and (5.18). For d = 1
the bounding curve lies strictly below the comparison function, for d = 0.1, however, a “γ-
window”opens up, where the lower bound LB on Cc(A+
R) and eCc(A+
R) clearly exceeds its
comparison values. Further lowering of d does not improve LB in a signiﬁcant way. Also
shown in Fig. 6.3 is the exact x-independent curve γ 7→µ0 in the limit B = 0, which coincides
41


## Page 42


with LB(0.39, γ, 0.1, 1.2) up to γ ≈0.56; this is in accordance with the fact that up to this
value the minimum in (6.40) is taken at s = 0 and
inf
0≤t≤1 f(0, t) =

1 −

γ
1 + α
2 1/2
.
Above γ ≈0.56 the minimum is located at t = 1.
To be deﬁnite let us ﬁx γ = 0.6 and d = 0.1. We then have the proposition:
Proposition 6.4 Let
(α, γ, d, e) = (0.39, 0.6, 0.1, 1.2) ,
(6.41)
then inequalities (5.20) and (5.21) are satisﬁed for any R > 1 and for the quantity ∆from
(5.22) holds the lower bound
∆≥0.027 > 0 .
(6.42)
Better lower bounds on Cc, eCc can be obtained according to proposition 6.2 by a numerical
evaluation of the Euler-Lagrange equations (6.17) (see appendix E) corroborating on one side
the lower bound LB and demonstrating on the other side that LB generally is not sharp.
7
Solution of PΩin annuli
This section contains the proof of theorem 2.1 based on Schauder’s ﬁxed point principle and
the general solution of the linearized problem in section 5.
The following proposition provides a suitable version of the Leray-Schauder theorem (see
Gilbarg and Trudinger 1998, p. 280, theorem 11.3).
Proposition 7.1 (ﬁxed point principle) Let T : B →B be a continuous, compact (or
completely continuous) mapping of the Banach space B into itself and let the set

u ∈B : u = λ Tu for some λ ∈[0, 1]
	
(7.1)
be bounded. Then, T has a ﬁxed point u0 ∈B, i.e.
Tu0 = u0 .
(7.2)
In order to ﬁnd a (nonlinear) mapping T suitable for our purpose let us ﬁx the parameters α,
γ, d, and e according to proposition 6.4 such that conditions (5.11), (6.6), (5.20), and (5.21)
are satisﬁed for any R > 1. Let B := Lp,δ(A+
R) with
Lp,δ(G) := clos
 C∞
0 (G) , ∥· y−δ∥p,0

,
G ⊂H
and p and δ yet to be ﬁxed. With w ∈Lp,δ(A+
R) and
aα :=
 aζ[wρ−α −Ω] , aρ[wρ−α −Ω] −α

,
(7.3)
where aζ[·] and aρ[·] are given by (2.26), we solve eq. (5.2) and obtain by proposition 5.2 a
solution v ∈H(d)
α+γ(A+
R) with bound
∥∇d v∥α+γ ≤
√
2
∆d ∥Ω∥2+γ−α ≤

4 π
(γ −α)(1 + α −γ)
1
2 K
∆d .
(7.4)
42


## Page 43


The last inequality in (7.4) follows by condition (2.32) as in lemma A.1. Supposing that
δ < α + γ
2
+ 1
p ,
(7.5)
we ﬁnd by (3.22) that
H(d)
α+γ(A+
R) ⊂Lp,δ(A+
R)
for any p ≥2 .
(7.6)
The mapping
T : Lp,δ(A+
R) →Lp,δ(A+
R) ,
w 7→v
(7.7)
is thus well deﬁned and, moreover, continuous and compact.
To see the continuity of T let v and ˜v be two solutions of eq. (5.2) with (7.3) and
eaα :=
 aζ[ ewρ−α −Ω] , aρ[ ewρ−α −Ω] −α

,
respectively, w and ew ∈Lp,δ(A+
R), ψ ∈C∞
0 (A+
R), and Ω= eΩ∈H2+γ−α(A+
R). The diﬀerence
of (5.2) for v and ˜v reads
Z
A+
R
∇(v −˜v) · ∇ψ dµα +
Z
A+
R
v
ρ aα[wρ−α −Ω] −˜v
ρ aα[ ewρ−α −Ω]

· ∇ψ dµα
=
Z
A+
R
Ω
ρ

a[wρ−α −Ω] −a[ ewρ−α −Ω]

· ∇ψ dζdρ ,
or, after some rearrangement,
Z
A+
R

∇(v −˜v) + v −˜v
ρ
aα[wρ−α −Ω]

· ∇ψ dµα
= −
Z
A+
R
˜v
ρ −Ω
ρ ρα a[wρ−α −Ω] −a[ ewρ−α −Ω]

· ∇ψ dµα .
Using (5.12) on the left-hand side and estimating the right-hand side by Cauchy-Schwarz’s
and H¨older’s inequality one obtains
B[v −˜v, ψ] ≤
Z
A+
R
L |w −ew| |˜v/ρ1+α −Ω/ρ| |∇ψ| dµα
≤L


|w −ew| |˜v/ρ1+α −Ω/ρ|


α+γ ∥∇ψ∥α−γ
≤∥(w −ew)ρ−(α+γ)/2∥p,0
 ∥˜v/ρ1+α∥q,0 + ∥Ω/ρ∥q,0

∥∇eψ∥α−γ ,
(7.8)
where 1
p + 1
q = 1
2 and L ≤1 is some Lipschitz constant for a[·]. The critical step is to ﬁnd a
bound on the parantheses in the last line. A bound on Ωis easy by (2.32):



Ω
ρ



q,0 ≤|A+
R|
1
q



Ω
ρ



∞≤|A+
R|
p−2
2p K .
(7.9)
A bound on ˜v, however, requires the reﬁned inequality (3.20) for “small q”:



˜v
ρ1+α



q,0 ≤C ∥∇d ˜v∥α+γ
(7.10)
43


## Page 44


provided that
1 + α ≤α + γ
2
+ 6 −q
2q
⇐⇒
1
q ≥1
2 −γ −α
6
⇐⇒
p ≥
6
γ −α ,
which means for the parameter set (6.41) that
p ≥29 .
(7.11)
By (7.4), inequality (7.8) may thus be rewritten as
B[v −˜v, ψ]
∥∇eψ∥α−γ
≤˘C K ∥(w −ew)ρ−(α+γ)/2∥p,0 ,
(7.12)
where ˘C denotes a constant depending on p, α, γ, d, e, and R. By approximation (7.12) holds
for any ψ ∈H(e)
α−γ(A+
R). In view of (7.12) and (7.5) we choose δ := (α + γ)/2 in (7.6) and ﬁnd
by combination of (3.22), (5.19) with (5.22), and (7.12):
∥(v −˜v)ρ−(α+γ)/2∥p,0 ≤bC ∥∇d (v −˜v)∥α+γ
≤
bC
∆sup
ψ̸=0
B[v −˜v, ψ]
∥∇eψ∥α−γ
≤
bC ˘CK
∆
∥(w −ew)ρ−(α+γ)/2∥p,0 ,
which implies continuity of T in Lp,(α+γ)/2 (A+
R).
To see the compactness of T it is suﬃcient to prove compactness of the embedding (7.6).
This, however, is equivalent to the well-known compact emdedding H1
0(G) ⋐Lp(G) for
bounded G ⊂R2 and 1 ≤p < ∞. In fact, by (3.12) we can conclude that a bounded sequence
(vn) ⊂Hβ(A+
R) implies boundedness of the sequence (vn ρ−β/2) ⊂H1
0(A+
R) and convergence
of a sequence (vm ρ−β/2) ⊂Lp(A+
R) is equivalent to convergence of (vm) ⊂Lp,β/2 (A+
R).
Finally, boundedness of the set (7.1) is immediate by (3.22) and (7.4):
∥wρ−(α+γ)/2∥p,0 ≤bC ∥∇d w∥α+γ = bC ∥∇d(λ Tw)∥α+γ
≤bC ∥∇d v∥α+γ ≤

4 π
(γ −α)(1 + α −γ)
1
2 bC K
∆d
for any w ∈Lp,(α+γ)/2 (A+
R) satisfying w = λ Tw for some λ ∈[0, 1].
The ﬁxed point v0 = w0 according to proposition 7.1 is a solution of eq. (5.2) with
aα :=
 aζ[v0ρ−α −Ω] , aρ[v0ρ−α −Ω] −α

,
hence u0 := v0ρ−α is a solution of the (nonlinear) equation (2.31) in A+
R, and by antisymmetric
continuation in AR.
The bound (2.33) follows by (5.24), (6.41), (6.42), and (7.4). Note that this bound depends
(besides the in (6.41) ﬁxed parameters) on K but not on R. This together with proposition
4.1 concludes the proof of theorem 2.1.
44


## Page 45


8
Solution of PΩin the exterior plane
The construction of solutions in the last section heavily depended on estimates that involved
the diameter R of the underlying domain, the bound (2.33), however, does not. This allows us
to construct the solution of problem PΩ(A∞) by suitably manipulating a sequence of solutions
on AR with R →∞, and to prove this way theorem 2.2.
More precisely let Ωn := Ω

An for n ∈N \ {1} and Ω∈L∞(A∞) satisfying the bound
(2.32) for some K > 0. By theorem 2.1 we then have a sequence of solutions (un) ⊂H1
0,as(An)
of the problems PΩn(An), n ∈N \ {1}, with bounds
∥∇un∥β ≤
√
C ,
n ∈N \ {1} .
(8.1)
Restricting un onto A2, the sequence (un|A2)n∈N\{1} is bounded by (8.1).
There is thus
a subsequence (n(1)) ⊂N such that
 un(1)
i |A2

i∈N coverges weakly to some u(1) ∈Hβ(A2)
with bound ∥∇u(1)∥β ≤
√
C.
Applying this argument to the sequence
 un(1)
i |A3

i∈N one
obtains a further subsequence (n(2)) ⊂(n(1)) such that
 un(2)
i |A3

i∈N converges weakly to
some u(2) ∈Hβ(A3) with bound ∥∇u(2)∥β ≤
√
C.
Repeating this process one obtains a
sequence
 (n(k))

k∈N of sequences with each element being a subsequence of its predecessor.
Let n(k)
k
denote the kth element of the subsequence (n(k)) and (n(k)
k )k∈N =: n∗the diagonal
sequence. By construction we have (n∗
i )i≥k ⊂(n(k)) and hence
un∗
i

A1+k
∥∇· ∥β
−−−−⇀
i →∞u(k) ∈Hβ(A1+k)
for any k ∈N
(8.2)
with
∥∇u(k)∥β ≤
√
C ,
k ∈N .
(8.3)
As u(k)|A1+l = u(l) for any l ≤k, the deﬁnition
u : A∞→R ,
u|A1+k := u(k) ,
k ∈N
is unique and yields by (8.3) a function ∈Hβ(A∞) ⊂H1
loc,as(A∞) with bound (2.35).
In order to see that u satisﬁes eq. (2.31) in A∞recall that by antisymmetry it is enough
to satisfy (2.31) in A+
∞. So, let ψ ∈C∞
0 (A+
∞) and l ∈N \ {1} such that in fact ψ ∈C∞
0 (A+
l ).
For un∗
i then holds
Z
A+
l
∇un∗
i · ∇ψ dζdρ +
Z
A+
l
un∗
i
ρ a[un∗
i −Ω] · ∇ψ dζdρ =
Z
A+
l
Ω
ρ a[un∗
i −Ω] · ∇ψ dζdρ . (8.4)
Letting i →∞the passage to u in the ﬁrst term on the left-hand side of (8.4) is justiﬁed by
weak convergence. For the other two terms recall that by compactness weak convergence in
H1
0(A+
l ) implies strong convergence in L2(A+
l ). Therefore, by the estimate

Z
A+
l
un∗
i
ρ a[un∗
i −Ω] −u
ρ a[u −Ω]

· ∇ψ dζdρ

≤
Z
A+
l

|un∗
i |
a[un∗
i −Ω] −a[u −Ω]
 + |a[u −Ω]| |un∗
i −u|
∇ψ
ρ
 dζdρ
≤M L ∥un∗
i ∥0 ∥un∗
i −u∥0 + M
√
2 |A+
l |1/2∥un∗
i −u∥0 ,
45


## Page 46


where L denotes a Lipschitz constant for a[·] and M a bound on |∇ψ/ρ| in supp ψ ⋐A+
l , the
passage to u in the second term on the left-hand side is justiﬁed, too, and a similar argument
applies to the right-hand side.
This together with proposition 4.2 concludes the proof of
theorem 2.2.
9
Solution of the signed direction problem without zeroes on
the symmetry axis
In this section we prove theorems 2.3 and 2.4 (with the stated restriction), which contain the
solution of the axisymmetric signed direction problem (1.1) in large spherical shells and in
exterior space, respectively, by applying the results gathered so far and formulated essentially
in theorems 1.1 and 1.2 and the appendices A and B. This application is straight forward;
only to establish continuity of the solution up to the boundary requires some additional
considerations.
To apply theorem 2.1 let R > R0 and let D and bD be continuous symmetric direction
ﬁelds with rotation numbers ̺ and b̺ along the boundaries S1 and SR of the annulus AR,
respectively. Let ̺ ≥b̺ ≥2 and ̺ −b̺ be an even number (including zero). Let, furthermore,
{z1, . . . , z̺−b̺} be a symmetric set of points in AR, which do not lie on the symmetry axis.9
By (A.6) the associated zero-positions angle Ψ then satisﬁes condition (2.32). By (2.20) and
(2.21), direction ﬁelds D and bD, which satisfy the axis condition (2.36) give rise to boundary
functions φ and bφ, respectively, that satisfy (B.1).
By (B.3) the harmonic interpolation
Φ then satisﬁes condition (2.32) as well. By theorem 2.1 we thus obtain a weak solution
u ∈H1
0,as(AR) of eq. (2.24), which implies a weak solution q = u+Φ ∈H1
as(AR) of eq. (2.19).
Given q, the function p is determined by (2.22) up to a constant p0. In fact, writing (2.22) in
Cartesian coordinates in the form
∂ζ p = ∂ρ q + sin(q −Ψ)
q −Ψ
q −Ψ
ρ
,
∂ρ p = −∂ζ q + cos(q −Ψ) −1
q −Ψ
q −Ψ
ρ
(9.1)
we ﬁnd by (3.5) the right-hand side in L2(AR). The integrability condition for (9.1) is just
(2.19), which takes the weak form
Z
AR
h
∂ζ q −cos(q −Ψ) −1
q −Ψ
q −Ψ
ρ
i
∂ζψ +
h
∂ρ q + sin(q −Ψ)
q −Ψ
q −Ψ
ρ
i
∂ρψ

dζdρ = 0
for any ψ ∈C∞
0 (AR). We obtain thus a symmetric function p ∈H1(AR) that solves (2.22)
(see, e.g., Galdi 94, lemma 1.1, p. 101, and corollary 4.1, p. 53). Inserting h as given by (2.16)
and g = (p + iq)/2 into (2.15) then yields a symmetric weak solution f ∈H1(AR) of eq. (2.9)
with boundary condition (2.14), which by (2.8) is equivalent to an axisymmetric magnetic
ﬁeld (Bρ, Bζ) satisfying (2.1) a.e. in AR. To obtain higher (interior) regularity let us switch
from cylindrical to Cartesian coordinates in R3. The ﬁeld
BC := (B1, B2, B3) := (Bρ cos θ, Bρ sin θ, Bζ) ∈
 H1(SSR)
3
9In the case ̺ −b̺ = 0 the set is empty.
46


## Page 47


Figure 9.1: A+
R,ǫ and the curved boundary components S+
1,ǫ and S+
R,ǫ.
then satisﬁes the system
∇× BC = 0 ,
∇· BC = 0
a.e. in SSR ,
where SSR denotes the spherical shell BR \B1 ⊂R3 corresponding to AR ⊂R2. By the vector
analysis identity
Z
D
∇× BC · ∇× ψ dv +
Z
D
∇· BC ∇· ψ dv =
3
X
i=1
Z
D
∇Bi · ∇ψi dv ,
where ψ = (ψ1, ψ2, ψ3) ∈(C∞
0 (D))3, one ﬁnds each component to be a weakly harmonic and
hence harmonic function in SSR. Bi and hence Bζ and Bρ are thus smooth functions in their
respective domains.
Improved boundary regularity, in particular B ∈C(AR), needs some more subtle argu-
ments, which in part are speciﬁc for two dimensions.
As to the variable q we rely on a
boundary-regularity theorem asserting H¨older continuity of a weak solution up to the bound-
ary provided that the boundary values themselves satisfy a H¨older condition (Ladyzhenskaya
and Ural’tseva 1968, theorem 14.1, p. 201f.). For this purpose let us write eq. (2.19) in the
form
∆q = ∂ζ
1
ρ
 cos(q −Ψ) −1

−∂ρ
1
ρ sin(q −Ψ)

=: ∂ζFζ + ∂ρFρ
with bounded F on A+
R,ǫ:
|Fζ| < 2
ǫ ,
|Fρ| < 1
ǫ .
Here, A+
R,ǫ := A+
r ∩{ρ > ǫ} denotes that part of A+
R, which has a distance ǫ > 0 to the
symmetry axis, and S+
1,ǫ and S+
R,ǫ denote the corresponding curved boundary components
(see Fig. 9.1).
47


## Page 48


The direction ﬁelds D and bD are now assumed to be of H¨older class C0,β(S1) and C0,β(SR),
respectively, for some 0 < β ≤1, which implies the boundary functions φ and bφ to be of the
same class. By q −Φ ∈H1
0(AR) we thus have
trace q|S+
1,ǫ = φ|S+
1,ǫ ,
trace q|S+
R,ǫ = bφ|S+
R,ǫ .
To this situation the boundary-regularity theorem may be applied asserting q ∈C0,α(A+
R,ǫ)
for some 0 < α ≤1, which depends on ǫ, R, ∥q∥0, and β, ∥φ∥C0,β, ∥bφ∥C0,β. This implies, in
particular, continuous assumption of the boundary values on S+
1,ǫ ∪S+
R,ǫ for any ǫ > 0, and
hence on S+
1 ∪S+
R.
This argument does not apply to p since a-priori no boundary values are prescribed for
this quantity. However, according to the governing equations for p, eqs. (9.1), the variables
p and q are complex conjugate variables up to a (in A+
R,ǫ) bounded “perturbation”. Without
this perturbation Privaloﬀ’s theorem guarantees uniform H¨older continuity of both variables
in a disc if only one variable takes continuously boundary values that are in some H¨older
class at the boundary (see Bers et al. 1964, p. 279 or Kaiser 2010, lemma 2.4). In order to
take advantage of Privaloﬀ’s theorem the following representation theorem (slightly adapted
to our needs) is useful (see Bers and Nirenberg 1954 or Bers et al. 1964, p. 259).
Theorem 9.1 (Bers and Nirenberg) Let G ⊂BR ⊂C and let w ∈H1(G) be a solution
of the equation
∂z w = γ
a.e. in G
(9.2)
with γ ∈L∞(G). Then w has the representation
w(z, z) = f(z) + s0(z, z)
in G ,
(9.3)
where f is complex analytic in G and where s0 is uniformly H¨older continuous in BR and real
on SR.
With
ℜz := ζ ,
ℑz := ρ ,
ℜw := p ,
ℑw := q ,
ℜγ := Fρ ,
ℑγ := Fζ ,
eqs. (9.1) are clearly of type (9.2) in G := A+
R,ǫ/2; (9.3) then yields on S+
R,ǫ:
q|S+
R,ǫ = ℑw|S+
R,ǫ = ℑf|S+
R,ǫ.
ℑf is thus of class C0,α on S+
R,ǫ and even analytic on (say) ∂( e
A+
R,ǫ) \ S+
R,ǫ, where
eA+
R,ǫ :=

(ζ, ρ) ∈H : (1 + ǫ)2 < ζ2 + ρ2 < R2, ρ > ǫ
	
.
Applying Privaloﬀ’s theorem on f in the Lipschitz-domain10 eA+
R,ǫ yields f ∈C0,α( eA+
R,ǫ),
which implies, in particular,
p = ℜw = ℜf + ℜs0
10By a conformal transformation with Lipschitz-continuous extension on the boundary, e
A+
R,ǫ is equivalent
to a disc.
48


## Page 49


to be H¨older continuous up to the boundary component S+
R,ǫ. To see continuity up to the
other boundary component S+
1,ǫ let us apply the inversion z 7→1
z to (9.2), which yields an
equation of the same type in the inverted half-annulus
eA−
1/R ,1 :=

(ζ, ρ) ∈H : (1/R2 < ζ2 + ρ2 < 1, ρ < 0
	
with outer boundary S−
1 . The above argument can thus be repeated establishing, ﬁnally,
continuity of p up to the boundary S+
1 ∪S+
R.
Concerning uniqueness let us remind that the number of zeroes is ﬁxed by (2.6) for any
solution f of problem P c
D, bD(AR). Two solutions f1 and f2 with the same boundary direction
ﬁelds Dc and bDc and the same set of zeroes are thus represented by u1 = q1−Φ and u2 = q2−Φ
satisfying (2.25) with the same boundary function Φ and zero-positions angle Ψ, and hence the
same Ω= Ψ −Φ. According to proposition 4.1 there is u1 = u2 and the only nonuniqueness
left is due to p0, which in (9.1) remains free. Therefore, f1 and f2 diﬀer by the positive factor
ep0/2. This proves theorem 2.3 in the case of no zeroes lying on the symmetry axis.
With some obvious modiﬁcations all these arguments work in the unbounded case as well:
b̺ + 1 has to be replaced by the exact decay order ˜δ, bD and bφ can be discarded, and H1
as(AR)
is replaced by H1
loc,as(A∞), existence and uniqueness of q then follow from theorem 2.2 and
proposition 4.2, p is again determined by eqs. (9.1), and all the regularity arguments, local
in character, apply to the unbounded case as well. This proves theorem 2.4 (again with the
mentioned restriction on the zeroes).
10
Zeroes on the symmetry axis
Zeroes on the symmetry axis are so far excluded. Overcoming this restriction by continuous
deformation of known solutions is the subject of this section.
Let us start with a lemma on a general invariance property of the rotation number that
is tailored to our needs (see, e.g., Heinz 1959, theorem 3 or Kaiser 2010, lemma 3.2).
Lemma 10.1 (deformation invariance) Let Bλ be a continuous vector ﬁeld on AR × I,
where λ varies in the closed interval I. Let Bλ ̸= 0 on S eR × I, 1 ≤eR ≤R, and let e̺λ be the
rotation number of Bλ along S eR. Then, e̺λ = const =: e̺ for any λ ∈I.
In the case that Bλ is a harmonic vector ﬁeld in AR or A∞, by (2.6) and (2.7) we can draw
from lemma 10.1 some consequences, which in a somewhat lax formulation can be summarized
as follows:
(i) In the case that B|(S1∪SR)×I ̸= 0, zeroes of Bλ can shift with λ, can split or coalesce,
but they can never spring up or vanish in AR.
(ii) If a zero with index −n, n ∈N, crosses S eR, 1 < eR < R, at (say) λ = λ0, according to
(2.6), e̺λ jumps at λ0 by +n in the case of “emigration” and by −n in the case of “immigration”
into A eR.
(iii) In A∞zeroes can vanish at inﬁnity or originate from inﬁnity at (say) λ = λ0; according
to (2.7) the exact decay order ˜δ increases or decreases at λ0 according to the index of the
zero.
(iv) If e̺ is ﬁxed (as is the case in the direction problem for ̺ along S1 and b̺ along SR),
zeroes cannot cross S eR (cannot originate or vanish at S1 or SR). However, zeroes can migrate
from AR onto S1 (or SR), split there and migrate as “border zeroes” along S1 (or SR), and
49


## Page 50


they can coalesce again and reenter into AR (see appendix E for a (two-dimensional) example
of this behaviour).
In the following we denote by
B = B
˜δ = B
˜δ[z1, . . . , z̺−˜δ+1]
the unique solutions of problem PD(A∞) according to theorem 2.4 with rotation number ̺,
exact decay order ˜δ, and zeroes z1, . . . , z̺−˜δ+1, which do not lie on the symmetry axis. In
particular, let
B
˜δ[. . . , z, z] ,
eB
˜δ[. . . , ˜z, ˜z] ,
B
˜δ+2[. . .]
be three solutions of PD(A∞) with ̺−˜δ−1 common zeroes indicated by “. . .” and, additionally,
the simple zeroes z, z in the ﬁrst case and ˜z, ˜z in the second case. Let Bλ = B(λ,˜λ,ˆλ) be the
linear combination
Bλ := λ B
˜δ + ˜λ eB
˜δ + ˆλ B
˜δ+2 ;
let, furthermore, zS = ζS and ˜zS = ˜ζS be two positions on the symmetry axis in A∞, and let
c˜δ−2 and ˜c˜δ−2 be the leading coeﬃcients in the representation (2.5) of B˜δ and eB˜δ, respectively.
For z ̸= ˜z the ﬁelds B˜δ, eB˜δ, and B˜δ+2 are clearly linearly independent and the linear
systems (in the variables λ, ˜λ, ˆλ)
Bζ,λ(ζS, 0) = 0 ,
λ c˜δ−2 + ˜λ ˜c˜δ−2 = 0
(10.1)
and
Bζ,λ(ζS, 0) = 0 ,
Bζ,λ(˜ζS, 0) = 0
(10.2)
have each up to (for the present arbitrary) factors unique solutions λ1 and λ2 such that Bλ1
has the ̺ −˜δ −1 common zeroes outside the symmetry axis and the simple zero zS on the
symmetry axis, and Bλ2 has, besides the common zeroes, the simple zeroes zS and ˜zS on the
symmetry axis. Note that by (10.1)b Bλ1 has the decay order ˜δ + 1, and by (10.1)a and (2.7)
this decay order is exact.
There is one question left open: Do Bλ1,2 satisfy the boundary condition Bλ1,2|S1 = a1,2 D
for some positive amplitudes a1,2? A-priori the linear combinations Bλ1,2 can have additional
zeroes on S1. To refute this presumption let µ 7→λ(µ), µ ∈[0, 1] be a continuous path in λ-
space connecting λ = (1, 0, 0) with λ1; µ 7→Bλ(µ) is thus a continuous deformation of Bλ(0) =
B˜δ[. . . , z, z] with ﬁnal state Bλ(1) = B
˜δ+1
λ1 [. . . , zS]. During the deformation the common zeroes
remain ﬁxed, whereas z, z will move. They can possibly enter S1 and leave again; ﬁnally,
however, one zero migrates to zS, whereas the other vanishes at inﬁnity. Additional zeroes
cannot emerge, neither from S1 (see (iv)) nor from inﬁnity (see (iii)11). Therefore, Bλ1|S1 ̸= 0,
i.e., Bλ1 is a signed solution of the direction problem. A similar argument applies to Bλ2,
which is thus a signed solution of the direction problem, too.
Further zeroes can be shifted to the symmetry axis just by repeating the procedure with
solutions, which possess already common zeroes on the symmetry axis.
In the case that
̺−˜δ +1 = ν is even, this way all zeroes can be shifted to arbitrary positions at the symmetry
axis. In the case that ̺ −˜δ + 1 = ν is odd, one simply solves the direction problem with ˜δ −1
instead of ˜δ; we are then again in the even case and solution of the system (10.1) provides us
11Observe that by construction the decay order of Bλ(µ) cannot fall below ˜δ.
50


## Page 51


with a ﬁeld that has an odd number of zeroes on the symmetry axis, an even number ≥0 of
zeroes outside, and the original exact decay order ˜δ.
In the case of a bounded domain AR, solutions of type (10.2) still exist, i.e., an even number
of zeroes can likewise be shifted to the symmetry axis; (10.1), however, does no longer work:
zeroes cannot be expelled from AR with its ﬁxed direction ﬁelds at the boundaries S1 and SR
(see (iv)).
In conclusion these remarks remove the limitation in theorems 2.3 and 2.4 we had to
impose in section 9.
11
The unsigned direction problem
This concluding section discusses the unsigned direction problem, its relation to the signed
problem, and proves, in particular, theorem 2.5.
Let us start with recalling some deﬁnitions given in section 2: S˜δ
D means the set of all
solutions of the signed direction problem P s
D(A∞) with direction ﬁeld D and exact decay
order ˜δ, and Lδ
D means the linear space of all solutions of the unsigned problem P u
D(A∞) with
decay order δ. Taking arbitrary linear combinations does clearly not respect the positivity of
the amplitude function nor the exact decay order, but it respects the boundary condition up
to a (locally varying) sign and the decay order. When taking only positive linear combina-
tions, which deﬁnes a cone in Lδ
D, positivity of the amplitude and decay order are preserved,
exactness of the decay order, however, can get lost. The set Cδ
D of all solutions of P s
D(A∞)
with decay order δ is of this type.
The proof of theorem 2.5 is based on the following relations between these sets:
Cδ
D =
[
δ≤˜δ≤̺+1
S
˜δ
D ,
(11.1)
Lδ
D =
(
⟨Cδ
D⟩
if ̺ ≥δ −1
{0}
if 2 ≤̺ < δ −1
,
(11.2)
S
˜δ
D ⊂⟨Sδ
D⟩
for 3 ≤δ ≤˜δ ≤̺ + 1 ,
(11.3)
dim ⟨Sδ
D⟩= ̺ −δ + 2
if 3 ≤δ ≤̺ + 1 .
(11.4)
Here ̺ denotes again the rotation number of D and ⟨S⟩the real linear span of the set S.
(11.1) is obvious by deﬁnition and (2.7).
As to (11.2): Let ̺ ≥δ−1. To prove the nontrivial inclusion Lδ
D ⊂⟨Cδ
D⟩, let B ∈Lδ
D with
B|S1 = a D and a ∈C(S1). By theorem 2.4 we have Cδ
D ̸= ∅. Let eB ∈Cδ
D with eB|S1 = ˜a D
and continuous ˜a > 0. Choosing λ > 0 such that a + λ˜a > 0 on S1, we have
Bλ := B + λ eB ∈Cδ
D ,
which implies for B the representation
B = Bλ −λ eB ,
i.e., B ∈⟨Cδ
D⟩.
51


## Page 52


In the case 2 ≤̺ < δ −1 let B ∈Lδ
D and let eB̺+1 be the unique solution ∈S̺+1
D
. Choose
as above λ > 0 such that a + λ˜a > 0 on S1. Then, by ̺ + 1 < δ the linear combination
B + λ eB̺+1 =: B̺+1
λ
has exact decay order ̺ + 1, i.e., we ﬁnd B̺+1
λ
∈S̺+1
D
as well.
By uniqueness we have
B̺+1
λ
= µ eB̺+1 for some µ > 0, which implies B = (µ−λ)eB̺+1. Thus, either B has the exact
decay order ̺ + 1, which contradicts B ∈Lδ
D with δ > ̺ + 1, or B ≡0, hence Lδ
D = {0}.
As to (11.3): Choose arbitrary Bi ∈Si
D, i = δ, . . . , ̺ + 1; then, the set S := {Bi : δ ≤
i ≤̺ + 1} is linearly independent as the Bi diﬀer pairwise by their asymptotic terms in the
representation (2.5). Deﬁning
eBδ
i := Bi + Bδ ,
the set eS := {eBi : δ ≤i ≤̺ + 1} is likewise linearly independent and, moreover, we have
eS ⊂Sδ
D. To prove (11.3) we show that any B˜δ ∈S˜δ
D for any δ ≤˜δ ≤̺+1 has a representation
in eS:
B
˜δ =
̺+1
X
i=δ
λi eBδ
i ,
λi ∈R .
(11.5)
As B˜δ has exact decay order ˜δ and precisely ̺ −˜δ + 1 zeroes, say z1, . . . , z̺−˜δ+1, the λi have
to satisfy the following linear system of equations:
̺+1
X
i=δ
λi eBδ
i (zn) = 0 ,
n = 1, . . . , ̺ −˜δ + 1 ,
̺+1
X
i=δ
λi ˜ci,n = 0 ,
δ ≤n ≤˜δ −1 ,
where ˜ci,n is the coeﬁcient cn in the representation (2.5) of eBδ
i . These (̺ −˜δ + 1) + (˜δ −
δ) = ̺ −δ + 1 equations for ̺ −δ + 2 unknowns have always a nontrivial solution, say
{µi : δ ≤i ≤̺ + 1}. Let
bB
˜δ :=
̺+1
X
i=δ
µi eBδ
i .
If bB˜δ|S1 ̸= 0 either bB˜δ or −bB˜δ belongs to S˜δ
D and has, moreover, the same zeroes as B˜δ. By
uniqueness we thus have Bδ = µ bB˜δ with µ ̸= 0, i.e., (11.5) holds. If bB˜δ has zeroes on S1
consider
˘B
˜δ := bB
˜δ + λ B
˜δ
with λ > 0 such that ˘B˜δ|S1 ̸= 0, i.e., ˘B˜δ ∈S˜δ
D. Again by uniqueness we ﬁnd
B
˜δ = µ ˘B
˜δ ⇐⇒(1 −µλ)B
˜δ = µ bB
˜δ
with µ > 0 and hence 1 −µλ ̸= 0, i.e., (11.5) holds again.
As to (11.4): This is an immediate consequence of the preceeding arguments: the set eS
is linearly independent by construction and generates Sδ
D according to (11.5).
eS with its
̺ −δ + 2 elements is thus a basis of Sδ
D.
52


## Page 53


The proof of theorem 2.5 now follows by (11.1)–(11.4) and the following concluding remark.
Remark: In the “trivial case” δ > ̺ + 1, the condition ̺ ≥2 as stated in (11.2)2 is not
necessary; the argument given there, however, must be altered. Equation (2.7) holds in fact
for any ̺ ∈Z, which implies immediately Sδ
D = ∅. To prove Lδ
D = ∅assume 0 ̸≡B ∈Lδ
D,
which then has necessarily zeroes on S1. Let ǫ > 0 such that B ̸= 0 on B1+ǫ \B1 and compare
̺ with the rotation number ̺ǫ of B along S1+ǫ. For ǫ →0, ̺ǫ remains constant; however,
it will diﬀer from ̺ by −1
2× number of sign reversals of B along S1 (for an illustration see
Fig. E.2). Thus, ̺ǫ < ̺ and applying (2.7) on B in R2 \ B1+ǫ yields a contradiction. The
assumption B ̸≡0 has thus to be dismissed.
A
The zero-positions angle Ψ
Let us write the analytic function (2.16) in the form
h(z) = z−̺
N
Y
n=1
(z −zn)(z −zn) = z−b̺
N
Y
n=1

1 −zn
z

1 −zn
z

,
̺ −b̺ = 2 N , N ∈N0 (A.1)
with points {z1, . . . , zN} ⊂A+
∞, which satisfy, in particular, ℑzn = ρn > 0. Decomposing h/h
into real and imaginary parts one obtains
h
h = v(ζ, ρ) + i w(ζ, ρ) ,
(ζ, ρ) ∈A∞
(A.2)
with
v = h
2 + h2
2 |h|2
,
w = h
2 −h2
2i |h|2 ,
v2 + w2 = 1 .
(A.3)
We now deﬁne
Ψ(ζ, ρ) := arctan w(ζ, ρ)
v(ζ, ρ) ,
(A.4)
where arctan means the principal branch of the inverse tan function with arctan 0 = 0. This
deﬁnition resolves the ambiguity in the choice of Ψ and ﬁxes the discontinuities of Ψ at the
zeroes of v. Let us illustrate this by the special case h0 = z−̺. With z = reiϕ one obtains
h0
h0
= e2i̺ϕ = cos 2̺ ϕ + i sin 2̺ ϕ
and hence12
eΨ0 = arctan(tan 2̺ ϕ) ;
eΨ0 jumps by π along all rays with angles ϕν =
π
4̺ (1 + 2ν), where ν is an integer and
ϕν ∈(−π, π) (see Fig. A.1). Moreover, by the reﬂection symmetry eΨ0(·, π −ϕ) = −eΨ0(·, ϕ)
and the estimate ϕ ≤π
2 sin ϕ on [0, π/2], one ﬁnds the estimate
|eΨ0(·, ϕ)| ≤π̺ | sin ϕ|
in AR .
(A.5)
According to the following lemma inequality (A.5) (and some consequences) hold for general
Ψ.
12Recall that tilde denotes dependence on polar coordinates: eΨ(r, ϕ) := Ψ(r cos ϕ, r sin ϕ).
53


## Page 54


Figure A.1: Lines of discontinuity of Ψ for ̺ = b̺ = 2.
Lemma A.1 Let Ψ as given by (A.1) – (A.4). Then the following inequalities hold:
|eΨ(·, ϕ)| ≤K | sin ϕ|
in A∞,
(A.6)
|Ψ(·, ρ)/ρ| ≤K
in A∞,
(A.7)
Z
A∞
Ψ2 ρ−(2+β) dζdρ ≤
2πK2
β(1 −β) ,
0 < β < 1
(A.8)
for some K > 0.
Proof: Inequality (A.7) is an immediate consequence of (A.6):
|Ψ(·, ρ)/ρ| = |eΨ(r, ϕ)/r sin ϕ| ≤K/r ≤K
in A∞,
and (A.8) follows by integration:
Z
A∞
Ψ2 ρ−(2+β) dζdρ = 2
Z π
0
Z ∞
1
eΨ2(r, ϕ)
r2+β | sin ϕ|2+β r drdϕ
≤4K2
Z ∞
1
r−(1+β) dr
Z π/2
0
| sin ϕ|−βdϕ ≤
2πK2
β(1 −β) ,
where we made use of sin ϕ ≥2ϕ/π on [0, π/2].
It remains to prove (A.6). For this purpose we decompose A+
∞into wedge-type components
A1 ∪A2 ∪A3 with
A1 :=

(r, ϕ) : 1 < r < ∞, ϕ0 ≤ϕ ≤π −ϕ0
	
,
A2 :=

(r, ϕ) : 1 < r < eR , 0 < sin ϕ < sin ϕ0
	
,
A3 :=

(r, ϕ) : r ≥eR , 0 < sin ϕ < sin ϕ0
	
(see Fig. A.2). Here eR (and ǫ) are chosen such that
54


## Page 55


Figure A.2: The decomposition A+
∞= A1 ∪A2 ∪A3.
eR > 1
ǫ max
1≤n≤N |zn| ,
8ǫ
1 −3ǫ <
1
2C(N) < 1 ,
(A.9)
where C(N) is some combinatorial constant that appears in inequality (A.12). Note that by
(A.3) v(ζ, ρ) and w(ζ, ρ) are real analytic functions in a neighbourhood of the symmetry axis
{ρ = 0} with v(·, 0) = 1 and w(·, 0) = 0. ϕ0 can thus be chosen such that v ≥1/2 and
|w| ≤c ρ in A2 for some c > 0. Moreover, it is assumed that
ϕ0 < π
8 b̺ .
(A.10)
Under these conditions inequality (A.6) then holds trivially in A1 ∪A2:
|eΨ(·, ϕ)| ≤
π
2 sin ϕ0
sin ϕ
in A1 ,
|eΨ(·, ϕ)| ≤w
v ≤2c eR sin ϕ
in A2 .
For A3 we need a more careful consideration. Let
gn :=
 1 −(zn/z)
 1 −(zn/z)

 1 −(zn/z)
 1 −(zn/z)
 ,
n = 1, . . . , N .
By z = reiϕ, zn = rn eiϕn, gn may be expressed as
gn =
1 −2 (rn/r) eiϕ cos ϕn + (rn/r)2 e2iϕ
1 −2 (rn/r) e−iϕ cos ϕn + (rn/r)2 e−2iϕ = 1+i −4 (rn/r) sin ϕ cos ϕn + 2(rn/r)2 sin 2ϕ
1 −2 (rn/r) e−iϕ cos ϕn + (rn/r)2 e−2iϕ ,
which allows by (A.9) the estimate
55


## Page 56


|gn −1| ≤
8ǫ
1 −3ǫ sin ϕ = η sin ϕ .
(A.11)
By (A.11) and the abbreviation 8ǫ/(1 −3ǫ) =: η it follows for gN := QN
n=1 gn:
g2
N −1
 =

N
Y
n=1
g2
n −1
 =

N
Y
n=1
 (gn −1)(gn + 1) + 1

−1

≤(3η sin ϕ + 1)N −1 ≤C(N) η sin ϕ < 1
2 sin ϕ ≤1
2
(A.12)
and, furthermore,

g2
N −1
g2
N + 1
 ≤(1/2) sin ϕ
2 −1/2
= 1
3 sin ϕ ≤1
3 .
(A.13)
Expressing now w/v by gN, using at that (A.1) and (A.3), one obtains
w
v = −i (h/h)2 −1
(h/h)2 + 1 = −i e4ib̺ ϕg2
N −1
e4ib̺ ϕg2
N + 1
= (g2
N + 1) sin 2b̺ ϕ −i (g2
N −1) cos 2b̺ ϕ
(g2
N + 1) cos 2b̺ ϕ + i (g2
N −1) sin 2b̺ ϕ = tan 2b̺ ϕ −i (g2
N −1)/(g2
N + 1)
1 + i tan 2b̺ ϕ (g2
N −1)/(g2
N + 1) .
(A.14)
Combining (A.4), (A.13), and (A.14) yields, ﬁnally, the desired estimate for Ψ in A3:
|Ψ| ≤
w
v
 ≤tan 2b̺ ϕ + (1/3) sin ϕ
1 −(1/3) tan 2b̺ ϕ
≤3
2

2
√
2 b̺ + 1
3

sin ϕ ,
where in the last estimate we made use of (A.10).
✷
B
Harmonic interpolation of the boundary data
The solution of the Dirichlet problem in bounded domains with regular boundary for con-
tinuous boundary data is a standard problem (see, e.g., Gilbarg and Trudinger 1998, p. 26).
The only not quite standard issue is antisymmetry and some estimates related to it. We
summarize useful properties in the following proposition.
Proposition B.1 Let φ and bφ : [−π, π] →R be continuous, antisymmetric functions with
φ(−π) = φ(π) and axis condition
φ(ϕ) = O(ϕ)
for ϕ →0 ,
φ(π −ϕ) = O(ϕ)
for ϕ ց 0 ,
(B.1)
and analogously for bφ. Then there is a unique antisymmetric solution Φ ∈C2(AR) ∩C(AR)
of the Dirichlet problem13
∆Φ = 0
in AR ,
eΦ(1, ·) = φ ,
eΦ(R, ·) = bφ ,
)
(B.2)
13Recall that tilde denotes dependence on polar coordinates: eΦ(r, ϕ) := Φ(r cos ϕ, r sin ϕ).
56


## Page 57


which, moreover, satisﬁes the estimates
|eΦ(·, ϕ)| ≤K | sin ϕ|
in AR ,
(B.3)
|Φ(·, ρ)/ρ| ≤K
in AR ,
(B.4)
Z
AR
Φ2 ρ−(2+β) dζdρ ≤
2πK2
β(1 −β) ,
0 < β < 1
(B.5)
for some K > 0, which does not depend on R.
Proof: Let Φ+ be the unique solution of the Dirichlet problem
∆Φ+ = 0
in A+
R ,
eΦ+(1, ϕ) = φ(ϕ) ,
eΦ+(R, ϕ) = bφ(ϕ)
for 0 ≤ϕ ≤π ,
eΦ+(r, 0) = eΦ+(r, π) = 0
for 1 ≤r ≤R
in the half-annulus A+
R := AR∩{ρ > 0} with continuous boundary data on the regular bound-
ary ∂A+
R. By antisymmetric continuation onto AR one obtains a function that is harmonic in
A+
R ∪A−
R and, by means of the mean-value characterization of harmonic functions, in fact in
AR. This is the asserted antisymmetric solution of (B.2).
The bound (B.3) holds by (B.1) on the boundaries S1 and SR with some constant K > 0.
To extend this bound onto AR consider the comparison function
Φ
+(r, ϕ) :=
K
1 + R

r + R
r

sin ϕ ,
which satisﬁes the Dirichlet problem
∆Φ
+ = 0
in A+
R ,
Φ
+(1, ϕ) = Φ
+(R, ϕ) = K sin ϕ
for 0 ≤ϕ ≤π ,
Φ
+(r, 0) = Φ
+(r, π) = 0
for 1 ≤r ≤R .
Applying the maximum principle to eΦ+ ∓Φ
+ then yields
|eΦ+(r, ϕ)| ≤
K
1 + R

r + R
r

sin ϕ ≤K sin ϕ
in A+
R ,
which is (B.3). (B.4) and (B.5) follow from (B.3) as in appendix A.
✷
Analogous results hold in the unbounded case, which by Kelvin’s transformation (see, e.g.,
Axler et al., p. 54f) can be reduced to a bounded problem.
Proposition B.2 Let φ : [−π, π] →R be a continuous, antisymmetric function with φ(−π) =
φ(π) and axis condition (B.1). Then there is a unique antisymmetric solution Φ ∈C2(A∞) ∩
C(A∞) of the exterior Dirichlet problem
∆Φ = 0
in A∞,
eΦ(1, ·) = φ ,
|eΦ(r, ·)| →0
for r →∞,
which, moreover, satisﬁes the estimates (B.3) – (B.5) (with AR replaced by A∞) for some
K > 0.
57


## Page 58


Proof: The most simple way to obtain a solution of the asserted kind is to solve again a
bounded problem, viz.,
∆Φ′+ = 0
in B+
1 ,
eΦ′+(1, ϕ) = −φ(ϕ)
for 0 ≤ϕ ≤π ,
eΦ′+(r, 0) = eΦ′+(r, π) = 0
for 0 ≤r ≤1 ,
to continue the solution Φ′+ antisymmetrically onto B1, and to reﬂect Φ′ by Kelvin’s trans-
formation into A∞. The estimates (B.3) – (B.5) are proved as in the bounded case, where
Φ
′+ := (K/r) sin ϕ is a suitable comparison function in A+
∞.
✷
C
Proof of the generalized Lax-Milgram criterion
The proof of proposition 5.1 is an exercise in standard functional analysis and is given here
for completeness.
Fixing some u ∈B in the bilinear form B(·, ·) yields a linear form on eB. The mapping
A : B →eB′ ,
u 7→B(u, ·)
is thus well deﬁned with Au acting on eB according to
⟨Au, ˜u⟩= B(u, ˜u)
for any ˜u ∈eB .
(C.1)
This mapping is bounded by (C.1), (5.6), and (5.5):
∥Au∥e
B′ = sup
0̸=˜u∈e
B
B(u, ˜u)
∥˜u∥e
B
≤K ∥u∥B ,
and injective by (5.7):
∥Au∥e
B′ = sup
0̸=˜u∈e
B
B(u, ˜u)
∥˜u∥e
B
≥c ∥u∥B .
(C.2)
The range A(B) of A is thus a closed set.
In order to prove A(B) = eB′ let us assume A(B) ⫋eB′.
According to a well-known
consequence of Hahn-Banach’s principle there is a nontrivial functional F0 ∈( eB′)′ vanishing
on A(B) (see, e.g., Kato 1976, p. 135). By reﬂexivity of eB, F0 is associated to some ˜u0 ∈eB
such that
⟨F0, f⟩= ⟨f, ˜u0⟩
for any f ∈eB′ .
(C.3)
By ∥F0∥e
B′′ ̸= 0 and (C.3) we ﬁnd for ˜u0:
0 < ∥F0∥e
B′′ =
sup
0̸=f∈e
B′
⟨F0, f⟩
∥f∥e
B′
=
sup
0̸=f∈e
B′
⟨f, ˜u0⟩
∥f∥e
B′
≤∥˜u0∥e
B .
(C.4)
On the other hand, by F0

A(B) = 0 and (C.1) we have for any u ∈B:
0 = ⟨F0, Au⟩= ⟨Au, ˜u0⟩= B(u, ˜u0) ,
58


## Page 59


and hence by (5.8):
∥˜u0∥e
B = 0 ,
which contradicts (C.4).
A : B →eB′ is thus an isomorphism, which guarantees the unique solvability of the equation
Au = f ,
which by (C.1) is equivalent to eq. (5.9). Finally, the estimate (5.10) follows from (C.2).
✷
D
The x-independent min-max problem
We give here a direct (i.e. without use of Euler-Lagrange techniques) solution of the min-max
problem (6.1), (6.2) corroborating the result (6.36).
In the x-independent case problem (6.1), (6.2) in the interval (b0, b1) reads
inf
v̸=0 sup
ψ̸=0
F0[v, ψ] =: µ0
(D.1)
with
F0[v, ψ] :=
Z b1
b0
v′ ψ′ y−α dy
 Z b1
b0
v′ 2 y−(α+γ) dy
1/2 Z b1
b0
ψ′ 2 y−(α−γ) dy
1/2
(D.2)
and
y−(α+γ)/2 v ∈H1
0((b0, b1)) ,
y−(α−γ)/2 ψ ∈H1
0((b0, b1)) .
(D.3)
(D.2) may be simpliﬁed by the substitution (y/b1)1+α =: z; F0 then takes the form
eF0[v, ψ] :=
Z 1
B
v′ ψ′ dz
 Z 1
B
v′ 2 z−eγ dz
1/2 Z 1
B
ψ′ 2 zeγ dz
1/2
(D.4)
with eγ := γ/(1 + α) and B := (b0/b1)1+α, and prime denoting derivation with respect to z.
To determine the maximizing ψ for given v let us estimate the numerator in (D.4) in the
form
Z 1
B
v′ψ′ dz =
Z 1
B
(v′ + C) ψ′ dz ≤
 Z 1
B
(v′ + C)2 z−eγ dz
 1
2  Z 1
B
ψ′ 2 zeγ dz
 1
2
,
(D.5)
where we made use of the boundary conditions on ψ. The maximum is reached if (D.5) is an
equality, i.e.
zeγ/2 ψ′ = λ z−eγ/2(v′ + C)
with some λ ∈R. Given v with z−eγ/2 v ∈H1
0((B, 1)), which corresponds to (D.3)a, the choice
ψ[v](z) := λ
Z 1
z
(v′ + C) ˜z−eγ d˜z ,
C := −
1 −eγ
1 −B1−eγ
Z 1
B
v′z−eγ dz
(D.6)
59


## Page 60


is admissible, i.e. zeγ/2 ψ[v] ∈H1
0((B, 1)).14 Inserting (D.6) into (D.5) yields
sup
ψ̸=0
Z 1
B
v′ψ′ dz
 Z 1
B
ψ′ 2 zeγ dz
1/2 =
Z 1
B
v′ψ[v]′ dz
 Z 1
B
ψ[v]′ 2 zeγ dz
1/2 =
 Z 1
B
(v′ + C)2 z−eγ dz
 1
2
=
 Z 1
B
v′ 2z−eγ dz −
1 −eγ
1 −B1−eγ
 Z 1
B
v′z−eγ dz
2 1
2
and hence
inf
v̸=0 sup
ψ̸=0
eF0[v, ψ] = inf
v̸=0
 
1 −
1 −eγ
1 −B1−eγ
 Z 1
B
v′z−eγ dz
2
Z 1
B
v′ 2z−eγ dz
! 1
2
=
 
1 −
1 −eγ
1 −B1−eγ sup
v̸=0
 Z 1
B
v′z−eγ dz
2
Z 1
B
v′ 2z−eγ dz
! 1
2
.
(D.7)
Similarly, using the boundary conditions on v we can estimate
Z 1
B
v′z−eγ dz =
Z 1
B
v′z−eγ/2 z−eγ/2 −C zeγ/2
dz
≤
 Z 1
B
v′ 2z−eγ dz
 1
2 1 −B1−eγ
1 −eγ
−2C(1 −B) + C2 1 −B1+eγ
1 + eγ
 1
2
.
(D.8)
Choosing C := (1 −B)(1 + eγ)/(1 −B1−eγ), (D.8) implies
sup
v̸=0
 Z 1
B
v′z−eγ dz
2
Z 1
B
v′ 2z−eγ dz
≤1 −B1−eγ
1 −eγ
−(1 −B)2
1 + eγ
1 −B1+eγ ,
(D.9)
and the admissible function
v0 := 1 −z −
1 −B
1 −B1+eγ (1 −z)1+eγ
demonstrates that inequality (D.9) is in fact an equality. Combining (D.1), (D.7), and (D.9)
we thus obtain
µ2
0 = 1 −
1 −eγ
1 −B1−eγ
1 −B1−eγ
1 −eγ
−(1 −B)2
1 + eγ
1 −B1+eγ

= (1 −B)2
1 −eγ
1 −B1−eγ
1 + eγ
1 −B1+eγ ,
which is (6.34).
14In the case that B = 0, eγ < 1 is assumed.
60


## Page 61


E
Numerical solution of the Euler-Lagrange equations associ-
ated to the min-max problem
In subsection 6.2 the product ansatz (6.25), (6.26) in the rectangular domain Q allowed the
reduction of the two-dimensional min-max problem to a sequence of one-dimensional problems
labeled by the index n ∈N. The corresponding one-dimensional Euler-Lagrange equations
are obtained by inserting (6.25) into (6.17). Using, moreover, the symmmetric variables w
and χ as given by (6.33) one obtains the following second-order system of ordinary diﬀerential
equations on the interval (0, b):
χ′′
n −γ
y χ′
n −
(α + γ + 2)(α −γ)
4 y2
+ k2
n

χn
−µn
h
w′′
n −
(α + γ + 2)(α + γ)
4 y2
+ d2k2
n

wn
i
= 0 ,
w′′
n + γ
y w′
n −
(α −γ + 2)(α + γ)
4 y2
+ k2
n

wn
−µn
h
χ′′
n −
(α −γ + 2)(α −γ)
4 y2
+ e2k2
n

χn
i
= 0



























(E.1)
together with the boundary conditions
wn(0) = χn(0) = 0 ,
wn(b) = χn(b) = 0
(E.2)
and eigenvalue µn.
For a numerical treatment of system (E.1) two more transformations are appropriate.
Introducing the variable z := kny yields the system
χ′′ −γ
z χ′ −
(α + γ + 2)(α −γ)
4 z2
+ 1

χ
−µ
h
w′′ −
(α + γ + 2)(α + γ)
4 z2
+ d2
w
i
= 0 ,
w′′ + γ
z w′ −
(α −γ + 2)(α + γ)
4 z2
+ 1

w
−µ
h
χ′′ −
(α −γ + 2)(α −γ)
4 z2
+ e2
χ
i
= 0 ,

























(E.3)
where we omitted the index n at χ, w, and µ and where prime denotes diﬀerentiation with
respect to the variable z ∈[0, knb]. Note that the parameters a, b, and n are now combined
into the single parameter
˜b := knb = n π
2
b
a ,
which limits the interval [0,˜b] of integration in (E.3). Finally, the change of variables f± :=
61


## Page 62


w ± χ separates the highest (≜second) derivatives; in these variables (E.3) takes the form
(1 −µ)f ′′
+ = (1 −µ) α(α + 2)
4 z2
f+ −(1 + µ) γ2
4 z2 f+ +

1 −µ
2 (d2 + e2)

f+
−γ
z f ′
−+
 1 −µ(α + 1)
 γ
2 z2 f−−µ
2 (d2 −e2)f−,
(1 + µ)f ′′
−= (1 + µ) α(α + 2)
4 z2
f−−(1 −µ) γ2
4 z2 f−+

1 + µ
2 (d2 + e2)

f−
−γ
z f ′
+ +
 1 + µ(α + 1)
 γ
2 z2 f+ + µ
2 (d2 −e2)f+ .























(E.4)
Equations (E.4) together with the boundary conditions
f±(b0) = f±(˜b) = 0
(E.5)
are solved in the interval [b0,˜b] by a shooting method. To this end trajectories are calculated
starting from both ends of the interval towards the center for a given value of µ. The integra-
tion is done with the standard Runge-Kutta-Fehlberg method, consisting of a fourth-order
Runge-Kutta solver with ﬁfth-order error prediction to control the stepsize. The matching
of the trajectories at the center of the interval amounts to the vanishing of a 4 × 4 determi-
nant computed from the trajectories at the center. The search for zeroes of this determinant
depending on µ is done by an interval method with respect to µ: we scan systematically
the interval [ε, 1] for subintervals exhibiting a sign change at the endpoints and reﬁne in the
positive case the subinterval subsequently. In order not to miss higher-order zeroes we looked,
additionally, for minima of the modulus of the determinant. These zeroes correspond to the
eigenvalues of µ and, in particular, the lowest one corresponds to µmin.
To validate the numerical code let us ﬁrst consider the x-independent case as described by
eqs. (6.34). These can be obtained from (E.4) just by dropping the coeﬃcients 1 ∓µ
2(d2 + e2)
and µ
2(d2 −e2). Figure E.1 demonstrates good agreement of this way numerically determined
points in a γ–µ0–diagram with curves γ 7→µ0 as described by the analytical result (6.36)
for α = 0.39 and three representative ratios b0/b1. For all three ratios the deviation of the
numerical data from the analytical curve is beyond the resolution of the plot.
The full equations (E.4) with boundary conditions (E.5) have been run with α = 0.39,
e = 1.2, and a variety of values for d, b0, and ˜b.
With respect to ˜b we ﬁnd µmin to be
a monotonically decreasing function. Figure E.2 displays results in a γ–µmin–diagram for
d = 0.1, b0 = 10−3, and ˜b = 102 together with the comparison function CF(0.39, γ) and the
lower bound LB(0.39, γ, 0.1, 1.2). For γ ≳0.6, µmin is above LB, which means an improvement
of the lower bound LB.
Further decreasing b0 or increasing ˜b does not lower µmin in a
signiﬁcant way, which indicates that (10−3, 102) is a suﬃcient approximation of the interval
(0, ∞). For 0.5 ≲µmin ≲0.6, µmin and LB coincide within numerical accuracy. No results
are shown for γ below 0.5 because of numerical instability of our code in this range (a problem
that we did not further pursue).
Let us ﬁnally recall that in the case that µmin is unique, which holds in the x-independent
case but has not been proven in the general case, µmin represents the (in the limits of numerical
accuracy) exact value Cc = eCc of the min-max problem.
62


## Page 63


0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
µ0
γ
Figure E.1: µ0 versus γ for α = 0.39 and b0/b1 = 0, 10−6 (cross), 10−4 (square), 10−2
(asterisk). Solid lines denote analytical curves, symbols denote numerical values.
0.6
0.7
0.8
0.9
1
1.1
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
1.1
µmin
γ
Figure E.2: µmin versus γ (crosses) together with the comparison function CF(α, γ) (thick
line) and the lower bound LB(α, γ, d, e) (thin line) for α = 0.39, d = 0.1, e = 1.2, b0 = 10−3,
and ˜b = 102.
63


## Page 64


Figure F.1: The two-dimensional direction ﬁeld (F.1) with rotation number ̺ = 3.
F
An analytic solution with single zero in two dimensions
This appendix presents the explicit solution of the direction problem for a simple direction
ﬁeld in two dimensions.15 The solution contains a single zero, whose position is governed by a
parameter λ. The example illustrates the migration of this position with λ and, in particular,
the splitting of the zero when hitting the boundary. Let (r, φ) be polar coordinates in R2
with basis vectors er and eϕ, and A∞the exterior plane with boundary S1. Furthermore, let
D := cos 2ϕ er + sin 2ϕ eϕ
(F.1)
be a (symmetric) direction ﬁeld on S1 (see Fig. F.1) and
eBλ(r, ϕ) := ∇Υλ(r, ϕ) := ∇

3λ cos 2ϕ
2r2
−(1 −λ2)
cos ϕ
r
+ cos 3ϕ
3r3

=
h
(1 −λ2)
cos ϕ
r2
+ cos 3ϕ
r4

−3λ cos 2ϕ
r3
i
er
+
h
(1 −λ2)
sin ϕ
r2
+ sin 3ϕ
r4

−3λ sin 2ϕ
r3
i
eϕ
(F.2)
a vector ﬁeld on A∞.
An elementary calculation shows that
∆Υλ = 0
in A∞
15The two-dimensional ﬁeld mimics an axisymmetric ﬁeld in three dimensions, where polynomial solutions
of type (F.2) are not at our disposal.
64


## Page 65


Figure F.2: Zeroes of eBλ for 5 diﬀerent values of λ. Arrows at the zeroes indicate in- and
outgoing ﬁeld lines.
and
eBλ(1, ϕ) =

(1 −λ2)(cos ϕ + cos 3ϕ) −3λ cos 2ϕ

er
+

(1 −λ2)(sin ϕ + sin 3ϕ) −3λ sin 2ϕ

eϕ
=

2(1 −λ2) cos ϕ cos 2ϕ −3λ cos 2ϕ

er +

2(1 −λ2) cos ϕ sin 2ϕ −3λ sin 2ϕ

eϕ
=
 2(1 −λ2) cos ϕ −3λ

D =: aλ(ϕ) D .
eBλ is thus a harmonic vector ﬁeld in A∞that solves the (unsigned) direction problem.
Let us consider the parameter range λ ∈(−1, 1) , where eBλ has the exact decay order
˜δ = 2. As long as aλ ̸= 0 the 2D-analogue of eq. (2.7) predicts ̺ −˜δ = 3 −2 = 1 zero of
eBλ in A∞, where ̺ is the rotation number of D (see Kaiser 2010). From (F.2) one obtains
explicitly for z0 = x0 + iy0 = r0(cos ϕ0 + i sin ϕ0):
(r0, ϕ0) =







(µ +
p
µ2 −1 , 0)
µ > 1
(1 , arccos µ)
−1 ≤µ ≤1
(−µ +
p
µ2 −1 , π)
µ < −1
,
where µ := 3λ/(2 −2λ2). With λ running through the interval [−1, 1] from 1 to −1 one
ﬁnds the following behaviour of z0 (see Fig. F.2): z0 moves from +∞(λ = 1) along the
x-axis, hits the boundary at x = 1 (λ = 1/2), splits into two “boundary-zeroes”, which move
symmetrically along S1 and coalesce again at x = −1 (λ = −1/2); for λ < −1/2, z0 enters
again A∞and moves along the negative x-axis up to −∞(λ = −1).
65


## Page 66


Note that eq. (2.7) remains valid in the presence of boundary-zeroes, if these are included
on the left-hand side, however weighted by a factor 1/2.
Acknowledgement
The authors would like to thank A. Tilgner for substantial help in preparing the numerical
code for the computations in appendix E.
References
Axler, S., Bourdon, P., Ramey, W., Harmonic function theory. Springer, New York 1992.
Bers, L., John, F., Schechter, M., Partial Diﬀerential Equations. Interscience Publishers, New
York 1964.
Bers, L., Nirenberg, L., On a representation theorem for linear elliptic systems with discon-
tinuous coeﬃcients and its applications. Atti del convegno internazionale sulle equazioni alle
derivate parzialli, pp. 111–140, Trieste 1954.
Courant, R., Hilbert, D., Methods of mathematical physics vol. I. Interscience, New York
1953.
Folland, G. B., Introduction To Partial Diﬀerential Equations. Princeton University Press,
Princeton, N.Y. 1995.
Galdi, G. P., An Introduction to the Mathematical Theory of the Navier-Stokes Equations
Vol. I. Linearized Steady Problems. Springer Tracts in Natural Philosophy Vol. 38, Springer-
Verlag, Berlin, Heidelberg, New York 1994.
Gilbarg, D., Trudinger, N. S., Elliptic Partial Diﬀerential Equations of Second Order. Springer,
Berlin, Heidelberg, New York 2nd edition 1998.
Gubbins, D., Herrero-Bervera, E. (Eds.), Encyclopedia of geomagnetism and paleomagnetism,
p. 466f and p. 679f. Springer, Berlin, Heidelberg, New York 2007.
Hardy, G. H., Littlewood, J. E. and P´olya, G., Inequalities. Cambridge University Press 1973.
Heinz, E., An elementary analytic theory of the degree of mapping in n-dimensional space.
Journal of Mathematics and Mechanics 8, 231–247 (1959).
Hulot, G., Khokhlov, A., Le Mou¨el, J.L., Uniqueness of mainly dipolar magnetic ﬁelds recov-
ered from directional data. Geophys. J. Int. 129, 347–354 (1997).
Kaiser, R., The geomagnetic direction problem: the two-dimensional and the three-dimensional
axisymmetric cases. SIAM J. Math. Anal. 42, 701-728 (2010).
Kaiser, R., Uniqueness and non-uniqueness in the non-axisymmetric direction problem. Q.
Jl. Mech. Appl. Math. 65, 347-360 (2012).
Kaiser, R., Neudert, M., A non-standard boundary value problem related to geomagnetism.
Quarterly of Applied Mathematics 62, 423–457 (2004).
Kato, T., Perturbation Theory for Linear Operators. Springer, Berlin, Heidelberg, New York
2nd edition 1976.
Ladyzhenskaya, O. A., Ural’tseva, N. N., Linear and Quasilinear Elliptic Equations. Aca-
66


## Page 67


demic Press, New York, London 1968.
Lieberman, G. M., Oblique Derivative Problems for Elliptic Equations. World Scientiﬁc, Sin-
gapore 2013.
Martensen, E., Potentialtheorie. Teubner-Verlag, Stuttgart 1968.
Merrill, R. T., McElhinny, M. W., The Earth’s Magnetic Field (Its History, Origin and Plan-
etary Perspective). Academic Press, London 1983.
Paneah, B. P., The Oblique Derivative Problem. The Poincar´e Problem. Mathematical Top-
ics, vol. 17. Wiley-VCH-Verlag, Berlin 2000.
Proctor, M. R. E., Gubbins, D., Analysis of geomagnetic directional data. Geophys. J. Int.
100, 69–77 (1990).
67

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
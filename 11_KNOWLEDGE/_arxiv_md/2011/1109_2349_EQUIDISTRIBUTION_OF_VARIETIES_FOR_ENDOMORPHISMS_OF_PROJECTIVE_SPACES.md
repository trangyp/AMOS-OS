---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1109.2349
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1109.2349_Equidistribution_of_varieties_for_endomorphisms_of_projective_spaces

> Source: 1109.2349_Equidistribution_of_varieties_for_endomorphisms_of_projective_spaces.pdf

> Pages: 11

---


## Page 1


arXiv:1109.2349v1  [math.DS]  11 Sep 2011
Equidistribution of varieties for endomorphisms
of projective spaces
Tien-Cuong Dinh and Nessim Sibony
Dedicated to Professor Ha Huy Khoai
Abstract
Let f be a non-invertible holomorphic endomorphism of the complex
projective space Pk and f n its iterate of order n. Let V be an algebraic
subvariety of Pk which is generic in the Zariski sense. We give here a survey
on the asymptotic equidistribution of the sequence f −n(V ) when n goes
to inﬁnity.
AMS classiﬁcation : 37F, 32H.
Key-words : equilibrium measure, Green currents, exceptional sets, equidistri-
bution, speed of convergence.
1
Introduction
Let Pk denote the complex projective space of dimension k. Consider an endo-
morphism f : Pk →Pk which is holomorphic and non-constant. Such a map is
always induced by a polynomial map F = (F0, . . . , Fk) from Ck+1 to Ck+1 where
the Fi are homogeneous polynomials of the same degree such that F −1(0) = {0}.
Indeed, if π : Ck+1 \ {0} →Pk is the canonical projection, the map f is deﬁned
by the relation f ◦π = π ◦F. We refer to [13, 15, 23] for the basic properties of
these endomorphisms.
From now on, we assume that the algebraic degree of f, i.e. the common
degree d of the Fi, is at least 2. Otherwise, f corresponds to an invertible matrix
and its dynamics is easy to study. The parameter space for these endomorphisms
with a given algebraic degree d is a Zariski open set of a projective space PN that
we denote by Hd(Pk). Using the B´ezout theorem, it is not diﬃcult to see that
an endomorphism f as above deﬁnes a ramiﬁed covering of degree dk over Pk. In
other words, f −1(a) contains exactly dk points counted with multiplicity.
Let ωFS denote the Fubini-Study form on Pk normalized so that ωk
FS is a
probability measure. Let f n := f◦· · ·◦f (n times) be the iterate of order n of f. It
is well-known that the sequence of probability measures d−kn(f n)∗(ωk
FS) converges
1


## Page 2


to a probability measure µ which is totally invariant: d−kf ∗(µ) = f∗(µ) = µ. It
is called the equilibrium measure or the Green measure of f, see e.g. [13].
Consider a point a in Pk. We are interested in the asymptotic distribution
of the ﬁbers f −n(a) of a when n goes to inﬁnity. We will survey results on the
equidistribution of these sets.
The proof for the main results in this section
was given in [12]. We will sketch it in Section 2 with some simpliﬁcation of the
arguments. Equidistribution for higher dimension subvarieties will be discussed
in Section 3. We also refer to Yuan [26] for analogous equidistribution problems
in number theory.
We have the following result which was proved in [8], see also [6].
Theorem 1.1. Let f be a non-invertible holomorphic endomorphism of Pk. Then,
there is a ﬁnite number of algebraic subsets E ⊂Pk which are totally invariant,
i.e. f −1(E) = E = f(E). In particular, there is a maximal proper algebraic
subset E, possibly empty, which is totally invariant.
Note that E is totally invariant if and only if f −1(E) ⊂E. We do not assume
here that E is irreducible nor of pure dimension. The set E is in fact the union
of all totally invariant proper algebraic sets of f. These sets are a posteriori of
bounded degree and we can construct them explicitly. However, they are far from
being understood. The following folklore conjecture is still open in dimension
k ≥3, see [17, 4] for the dimension 2 case.
Conjecture 1.2. Any totally invariant algebraic subset for a map f as above is
a union of linear projective subspaces.
One also expects that the degrees of these totally invariant sets are bounded
by a constant which depends only on k. This is known for the case where the
codimension of E is 1 or 2 or in some others situations, see [1, 8, 13, 17]. In
dimension 1, E contains 0,1 or 2 points, e.g. if f(z) = z±d then E = {0, ∞}.
Denote by δa the Dirac mass at a and µa
n := d−kn(f n)∗(δa) the probability
measure which is equidistributed on the ﬁber f −n(a). The points in f −n(a) are
counted with multiplicity. Here is the ﬁrst main result [12].
Theorem 1.3. Let f, µ and E be as above. There is a constant λ > 1 such that
if a is a point out of E, then µa
n converges to µ exponentially fast, that is, if ϕ is
a Cα function on Pk with 0 < α ≤2, we have
|⟨µa
n −µ, ϕ⟩| ≤A
h
1 + log+
1
dist(a, E)
iα/2
∥ϕ∥Cαλ−αn/2,
where A > 0 is a constant independent of n, a and ϕ.
Here, we use the notation
⟨µ, ϕ⟩:=
Z
ϕdµ.
2


## Page 3


The simple convergence µa
n →µ is equivalent to the convergence of the integral
⟨µa
n−µ, ϕ⟩to 0. The above theorem gives us the exponential speed of convergence.
Note that the distance dist(a, E) is with respect to the Fubini-Study metric
on Pk. When E is empty (this is the case for generic f), by convention, this
distance is the diameter of Pk which is a ﬁnite number. A priori, the constant A
depends on λ and α. Note also that we have the estimate
A
h
1 + log+
1
dist(a, E)
iα/2
≤A
h
1 + log+
1
dist(a, E)
i
for 0 < α ≤2.
It is known that the measure µ has no mass on algebraic sets, in particular,
on E. So, the above result is optimal in the sense that µa
n does not converge
to µ when a ∈E.
We can show that there is a ﬁnite family of probability
measures, independent of a, such that any limit value of µa
n is an element of this
family. However, the choice of the limit measures depends on a. For example, in
dimension k = 1, if f(z) = z−d, we have E = {0, ∞}, µ is the Haar measure on
the unit circle and the above family contains three measures: µ, the Dirac mass
at 0 and the Dirac mass at ∞.
We also deduce from the above theorem that µa
n converges to µ locally uni-
formly for a ∈Pk \ E.
The simple convergence without speed estimate was
obtained in dimension 1 by Brolin [3] for polynomials, by Lyubich [21], Freire-
Lopes-Ma˜n´e [19] for general maps and in higher dimension by Fornæss-Sibony
[16], Briend-Duval [2] and Dinh-Sibony [8].
The following corollary gives us a geometric interpretation of the above result.
Corollary 1.4. Let U be an open subset of Pk such that µ has no mass on the
boundary of U. Then, if a is a point outside E, we have
#(f −n(a) ∩U) = µ(U)dkn + o(dkn).
So, if µ(U) > 0, a, b are two generic points and n is large enough, the number
of points of f −n(a) in U is almost equal to the same quantity associated to b, i.e.
lim
n→∞
#(f −n(a) ∩U)
#(f −n(b) ∩U) = 1.
We have the following version of Theorem 1.3 which is in our opinion more
important.
Theorem 1.5. Let f, µ and µa
n be as above. Let 1 < λ < d be a ﬁxed constant.
There is an invariant proper algebraic subset Eλ, possibly empty, of Pk such that
if a is a point out of Eλ and if ϕ is a Cα function on Pk with 0 < α ≤2, then
|⟨µa
n −µ, ϕ⟩| ≤A
h
1 + log+
1
dist(a, Eλ)
iα/2
∥ϕ∥Cαλ−αn/2,
where A > 0 is a constant independent of n, a, ϕ.
3


## Page 4


From Theorem 1.5, we can deduce several fundamental statistical properties
of the measure µ. Recall that locally this measure can be written as a Monge-
Amp`ere measure with H¨older continuous potential. It is shown by Nguyen and
the authors in [7] that µ is moderate, i.e. it satisﬁes some exponential estimate
for plurisubharmonic functions `a la H¨ormander as in Lemma 2.1 where we replace
ωk
FS by µ and |ϕ| by a constant times |ϕ|. Therefore, in our setting, we can work
with µ as if it were the Lebesgue measure.
Theorem 1.5 implies a slightly weaker estimate than the following exponential
mixing of µ which were proved in [8, 16] : if ϕ is a test Cα function with 0 < α ≤2
and ψ is a function in L∞(µ) then
⟨µ, ϕ(ψ ◦f n)⟩−⟨µ, ϕ⟩⟨µ, ψ⟩
 ≤A∥ϕ∥Cα∥ψ∥∞d−αn/2.
The mixing implies the ergodicity and then, by Birkhoﬀ’s theorem, if a is a
µ-generic point in Pk, the orbit of a is equidistributed in the support of µ. More
precisely, we have
1
n
 δa + δf(a) + · · · + δfn−1(a)

→µ.
We can also deduce more precise informations about this convergence, namely,
it is possible to obtain the central limit theorem and the large deviations theorem
which were proved in [7, 13].
2
Sketch of the proof of Theorem 1.5
The use of Proposition 2.2 below is new and it simpliﬁes the original proof of
Theorem 1.5. Note also that Theorem 1.3 is a consequence of the last one. For
the details, we refer to [12]. The main tool we use is pluripotential theory. We
recall here some results and refer to [5, 13, 20] for the details.
Let ϕ : X →R ∪{∞} be a function on a connected complex manifold X
which is not identically −∞. It is called plurisubharmonic (p.s.h. for short) if
its restriction to any holomorphic disc is either subharmonic or equal to −∞.
It is called quasi-p.s.h. if it is locally the diﬀerence of a p.s.h. function with a
smooth function. So, C2 functions are quasi-p.s.h. A set E in Pk is pluripolar if
it is contained in the pole set {ϕ = −∞} of a quasi-p.s.h. function ϕ.
Recall that a function ϕ on Pk, deﬁned out of a pluripolar set, is d.s.h. if it
is equal to the diﬀerence of two quasi-p.s.h. functions. We identify two d.s.h.
functions if they are equal outside of a pluripolar set. We summarize here some
properties of these functions, see [13] for details. If ϕ is d.s.h., there are two
positive closed (1, 1)-currents S± of the same mass such that ddcϕ = S+ −S−.
Conversely, if S± are positive closed (1, 1)-currents of the same mass, there is a
d.s.h. function ϕ, unique up to a constant, such that ddcϕ = S+ −S−.
In what follows, we only consider the space F of d.s.h. functions ϕ such that
⟨µ, ϕ⟩= 0, where µ is the equilibrium measure of f. This space is endowed with
4


## Page 5


the following norm
∥ϕ∥:= inf

∥S±∥,
S± positive closed (1, 1)-currents such that ddcϕ = S+−S−	
.
The classical exponential estimate for p.s.h functions implies the following.
Lemma 2.1. There is a positive constant C such that if ϕ is a function in F
with ∥ϕ∥≤1, then
⟨ωk
FS, e|ϕ|⟩≤C.
The following consequence is crucial in the proof of Theorem 1.5. It is already
interesting when U = Pk. The estimate can be extended to ϕ in any compact
family of d.s.h. functions. It is important to observe that we get a pointwise
estimate and this allows us to get an analog in the inﬁnite dimensional case, i.e.
for super-potentials.
Proposition 2.2. Let ϕ be a function in F such that ∥ϕ∥≤1. Assume that ϕ
is H¨older continuous on an open set U: |ϕ(x) −ϕ(y)| ≤M dist(x, y)β for some
constants M ≥1, 0 < β ≤1 and for x, y in U. Then, there is a constant A0 > 0
independent of ϕ, U, M and β such that
|ϕ(a)| ≤A0β−1(1 + log M)
for every point a such that dist(a, Pk \ U) ≥M−1/β.
Proof. Let A0 > 2 be a constant large enough. If the above estimate were false,
then there is a function ϕ and a point a as above such that |ϕ(a)| ≥A0β−1(1 +
log M). So, the ball B of center a and of radius M−1/β is contained in U. We
deduce from the H¨older continuity of ϕ that for every b ∈B
|ϕ(b)| ≥A0β−1(1 + log M) −1 ≥1
2A0β−1(1 + log M) ≥1
2A0 + 1
2A0β−1 log M.
This contradicts the exponential estimate in the previous lemma.
The mass of a positive closed (1, 1)-current S in Pk is deﬁned by ∥S∥:=
⟨S, ωk−1
FS ⟩. It depends only on the cohomology class of S in H1,1(Pk, C) ≃C. Using
the B´ezout theorem, we can show that f∗acts on H1,1(Pk, C) as multiplication
by dk−1. We can deduce from these properties and the total invariance of the
measure µ the following lemma.
Lemma 2.3. The endomorphism f induces a linear operator f∗: F →F such
that ∥f∗∥≤dk−1.
Recall that if ϕ is a function on Pk then the function f∗(ϕ) is deﬁned by
f∗(ϕ)(a) :=
X
b∈f−1(a)
ϕ(b),
5


## Page 6


where the points in f −1(a) are counted with multiplicity.
For ϕ continuous,
f∗(ϕ) is continuous. If ϕ is an L1 function and ν is the Radon measure given by
a smooth volume form, we have
⟨ν, f∗(ϕ)⟩= ⟨f ∗(ν), ϕ⟩.
For a general Radon measure ν, we can deﬁne another Radon measure f ∗(ν)
using the same identity with ϕ continuous.
We now deﬁne the exceptional set Eλ. Let κn(x) denote the multiplicity of
f n at x, i.e. the local topological degree of f n at x, for n ≥0. More precisely,
for z generic near f n(x), f −n(z) has κn(x) points near x. Deﬁne
κ−n(x) :=
max
y∈f−n(x) κn(y).
It was shown in [6] that the sequence κ1/n
−n converges to a function κ−which is
upper semi-continuous with respect to the Zariski topology.
Moreover, for any δ > 1, the level set {κ−≥δ} is an invariant proper algebraic
subset of Pk. Deﬁne Eλ := {κ−≥d/λ}. So, there is a constant 1 < δ0 < d/λ
such that κn0 < δn0
0
outside f −n0(Eλ) for a ﬁxed integer N0 large enough. In
what follows, without loss of generality, we replace f, d, λ, δ0 by f n, dn, λn, δn
0 for
n large enough in order to assume that the multiplicity of f at any point outside
f −1(Eλ) is smaller than δ0 and that 20k2δ0 < d/λ.
The previous property of multiplicity allows us to prove a version of the
classical Lojasiewicz inequality adapted to our situation. Denote by Vt the t-
neighbourhood of Eλ.
Proposition 2.4. There is an integer N ≥1 and a constant A1 ≥1 such that if
0 < t < 1 is a constant and if x, y are two points outside Vt, then we can write
f −1(x) = {x1, . . . , xdk}
and
f −1(y) = {y1, . . . , ydk}
with dist(xi, yi) ≤A1t−N dist(x, y)1/δ0.
Finally, we have the following proposition where we assume that ϕ is a function
in F such that ∥ϕ∥C2 ≤1. Deﬁne Λ := d1−kf∗.
Proposition 2.5. The function Λn(ϕ) is H¨older continuous on Pk \ Eλ. More-
over, there is a constant A2 ≥1 such that for every n ≥0 and 0 < t ≤1
|Λnϕ(x) −Λnϕ(y)| ≤ANn2
2
t−Nn dist(x, y)δ−n
0
for x, y out of Vt.
Proof. Since Eλ is invariant, it is not diﬃcult to see that for a constant c > 0
small enough, we have
dist(f −1(x), Eλ) ≥c dist(x, Eλ).
6


## Page 7


Deﬁne A2 := dA1/c. The proof is by induction on n. The case n = 0 is clear.
Assume that the proposition holds for n. We show it for n + 1. Let x, y be two
points out of Vt. By Proposition 2.4, we can write
f −1(x) = {x1, . . . , xdk}
and
f −1(y) = {y1, . . . , ydk}
so that dist(xi, yi) ≤A1t−N dist(x, y)1/δ0. Observe that xi and yi are out of Vct.
We deduce from the deﬁnition of Λ and the induction hypothesis that
|Λn+1ϕ(x) −Λn+1ϕ(y)|
≤
d1−k X
|Λnϕ(xi) −Λnϕ(yi)|
≤
d1−kANn2
2
(ct)−Nn X
dist(xi, yi)δ−n
0
≤
dANn2
2
c−Nnt−NnA
δ−n
0
1
t−Nδ−n
0
dist(x, y)δ−n−1
0
≤
AN(n+1)2
2
t−N(n+1) dist(x, y)δ−n−1
0
.
This completes the proof.
End of the proof of Theorem 1.5. First observe that from the theory of
interpolation between Banach spaces (in our case between C0 and C2), it is enough
to consider the case α = 2. Indeed, if L is a continuous linear form on the space
of continuous functions on Pk, it deﬁnes also a continuous linear form on Cα and
we have the inequality
∥L∥Cα ≤A∥L∥1−α/2
∞
∥L∥α/2
C2 ,
where A > 0 is a constant independent of L, see [25] for details. In our situation,
it is enough to apply this inequality to the Radon measures d−kn(f n)∗(δa) −µ.
So, assume that α = 2 and ϕ is a function of class C2. Since the theorem
is clear for constant test functions, subtracting from ϕ a constant allows us to
assume that ϕ is a function in F. Moreover, by linearity, we can assume that
∥ϕ∥≤1 and ∥ϕ∥C2 is bounded. We use here that ∥∥≲∥∥C2. By Lemma 2.3,
we have ∥Λn(ϕ)∥≤1.
We also obtain from the deﬁnition of Λ that
⟨d−kn(f n)∗(δa), ϕ⟩= d−nΛnϕ(a).
Deﬁne
l := 1 + log+
1
dist(a, Eλ)·
We need to show that |Λnϕ(a)| ≤Alλ−ndn for some constant A > 0 and for
n ≥1. Deﬁne t := e−l. Observe that dist(a, Vt) ≥t. Therefore, Propositions 2.5
and 2.2 yields
|Λnϕ(a)| ≤A0δn
0

1 + log(ANn2
2
t−Nn)

≲lλ−ndn
since δ0 < d/λ and l ≥1.
□
7


## Page 8


3
Equidistribution of varieties
In this section we survey the results on equidistribution of varieties. Recall that
the sequence d−n(f n)∗(ωFS) converges to a canonical invariant positive closed
(1, 1)-current T of mass 1. We call it the Green current of f. For any integer
1 ≤p ≤k, the sequence d−pn(f n)∗(ωp
FS) converges to the positive closed (p, p)-
current T p := T ∧. . . ∧T (p times) that we call the Green current of order p or
the Green (p, p)-current of f, see e.g. [13]. When p = k we obtain the equilibrium
measure µ = T k considered above.
Note that the operators f∗and f ∗are well-deﬁned on positive closed currents
[9]. If S is a positive closed (p, p)-current on Pk, we have ∥f ∗(S)∥= dp∥S∥and
∥f∗(S)∥= dk−p∥S∥. If V is an algebraic set of pure codimension p, the integration
on its regular part deﬁnes a positive closed (p, p)-current [V ]. The mass of [V ] is
equal to the degree of V . We conjecture the following.
Conjecture 3.1. Let V be generic in the Zariski sense among algebraic sets of
pure codimension p and of a given degree. Then, deg(V )−1d−pn(f n)∗[V ] converge
to T p in the sense of currents when n goes to inﬁnity. Moreover, the convergence
is exponentially fast.
Fix a constant 1 < λ < d. We expect a much stronger property: there is a
ﬁnite family of algebraic sets E1
λ, . . . , Em
λ such that if V intersects Ei
λ properly, i.e.
the intersection is empty when dim Ei
λ < p and the intersection is of dimension
dim Ei
λ −p otherwise, then
⟨deg(V )−1d−pn(f n)∗[V ] −T p, Φ⟩
 ≲∥Φ∥Cαλ−nα/2
for any test form Φ of class Cα with 0 < α ≤2.
If we replace the family of Ei
λ by the family of all totally invariant algebraic
sets, we also expect the exponential convergence with rate λ−nα/2 for some λ > 1.
The conjecture says in particular that if U is an open set such that T p has
positive mass on U but no mass on ∂U and if V, V ′ are two generic algebraic
sets of codimension p, of the same degree, then the volume of f −n(V ) ∩U is
almost equal to the one of f −n(V ′) ∩U when n is large enough. Here, by volume
we mean the Hausdorﬀ2(k −p)-dimensional measure with respect to a ﬁxed
Hermitian metric on Pk.
We have seen that the conjecture holds for the case of points, i.e. p = k. The
conjecture was recently conﬁrmed in the case of hypersurfaces, i.e. p = 1, by
Taﬂin in [24]. Taﬂin’s theorem is as follows.
Theorem 3.2. Let λ be a constant such that 1 < λ < d.
There is a ﬁnite
family of algebraic sets E1
λ, . . . , Em
λ satisfying the following property. If V is a
hypersurface which does not contain any Ei
λ, then
⟨deg(V )−1d−n(f n)∗[V ] −T, Φ⟩
 ≤C∥Φ∥Cαλ−nα/2,
8


## Page 9


for every test form Φ of class Cα with 0 < α ≤2, where C > 0 is a constant
depending on f, λ, V and α.
We refer to the original paper by Taﬂin for the explicit construction of Ei
λ.
Note that the convergence without speed was proved by Fornæss-Sibony [18] and
Favre-Jonsson [14] in dimension k = 2 and by Dinh-Sibony [10] in any dimension.
In this case, we can replace the family of Ei
λ by the family of minimal totally
invariant algebraic sets, see also Para [22].
A key point in the proof is to write, in a unique way,
deg(V )−1[V ] −T = ddcu
with u a function in F. The uniqueness of the solution of such an equation and
the total invariance of T imply that
deg(V )−1d−n(f n)∗[V ] −T = ddc(d−nu ◦f n).
So, the problem is reduced to prove the convergence of the sequence of functions
d−nu ◦f n to 0 in a weak sense and to estimate the speed of convergence.
Taﬂin proved and used some version of exponential estimates for non-compact
families of d.s.h. functions. Moreover, the proof contains an induction on the
dimension, that is, he has to check the convergence on some algebraic subsets of
Pk which may be singular. This requires precise versions of Lojasiewicz inequality
in order to handle diﬀerent technical diﬃculties.
The above conjecture is still open in the general case. We have nevertheless
the following result [11] which proves the conjecture for generic maps1. Recall
that the parameter space for holomorphic endomorphisms of algebraic degree d
is a connected complex quasi-projective manifold Hd(Pk).
Theorem 3.3. Let 1 < λ < d be a constant. There is a non-empty Zariski
open set Hλ
d(Pk) of Hd(Pk) such that if f is an element in this open set, then
deg(V )−1d−pn(f n)∗[V ] converge to T p in the sense of currents for any algebraic
set V of pure codimension p. Moreover, we have
⟨deg(V )−1d−pn(f n)∗[V ] −T p, Φ⟩
 ≤C∥Φ∥Cαλ−nα/2,
for every test form Φ of class Cα with 0 < α ≤2. Here, C is a positive constant
independent of V .
The set Hλ
d(Pk) is deﬁned as a set of maps where the local multiplicity is not
too big.
A main diﬃculty is that the above theory of plurisubharmonic functions is not
enough to handle algebraic cycles of arbitrary dimension. So, for this purpose, we
introduced and developed a theory of super-potentials for positive closed currents
1The speed of convergence is not precisely stated in [11], but the proof gives Theorem 3.3.
9


## Page 10


and we applied it in the dynamical setting. Roughly speaking, this is a theory
of quasi-p.s.h. functions in inﬁnite dimension. We are able for example to get
a version of the exponential estimate in Proposition 2.2.
In order to obtain
the solution of Conjecture 3.1, we still have to get a version of the Lojasiewicz
inequality which seems to be a diﬃcult problem.
References
[1] Amerik E. and Campana F., Exceptional points of an endomorphism of the pro-
jective plane, Math. Z., 249 (2005), no. 4, 741-754.
[2] Briend J.-Y. and Duval J., Deux caract´erisations de la mesure d’´equilibre d’un
endomorphisme de Pk(C), Publ. Math. Inst. Hautes ´Etudes Sci., 93 (2001), 145-
159.
[3] Brolin H., Invariant sets under iteration of rational functions, Ark. Mat., 6 (1965),
103-144.
[4] Cerveau D. and Lins Neto A., Hypersurfaces exceptionnelles des endomorphismes
de CP(n), Bol. Soc. Brasil. Mat. (N.S.), 31 (2000), no. 2, 155-161.
[5] Demailly J.-P., Complex analytic and diﬀerential geometry, available at
www.fourier.ujf-grenoble.fr/∼demailly.
[6] Dinh T.-C., Analytic multiplicative cocycles over holomorphic dynamical systems,
special issue of Complex Variables and Elliptic Equations, 54 (2009), no. 3-4, 243-
251.
[7] Dinh T.-C., Nguyen V.-A. and Sibony N., Exponential estimates for plurisubhar-
monic functions and stochastic dynamics, J. Diﬀerential Geom., 84 (2010), no. 3,
465-488.
[8] Dinh T.-C. and Sibony N., Dynamique des applications d’allure polynomiale, J.
Math. Pures Appl., 82 (2003), 367-423.
[9] ——, Pull-back of currents by holomorphic maps, Manuscripta Math., 123 (2007),
357-371.
[10] ——, Equidistribution towards the Green current for holomorphic maps, Ann. Sci.
´Ecole Norm. Sup., 41 (2008), 307-336.
[11] ——, Super-potentials of positive closed currents, intersection theory and dynam-
ics, Acta Math., 203 (2009), no. 1, 1-82.
[12] ——, Equidistribution speed for endomorphisms of projective spaces, Math. Ann.,
347 (2010), no. 3, 613-626.
[13] ——, Dynamics in several complex variables: endomorphisms of projective spaces
and polynomial-like mappings, 165-294, Lecture Notes in Math., 1998, Springer,
Berlin, 2010.
10


## Page 11


[14] Favre C. and Jonsson M., Brolin’s theorem for curves in two complex dimensions,
Ann. Inst. Fourier (Grenoble), 53 (2003), no. 5, 1461-1501.
[15] Fornæss J.-E., Dynamics in several complex variables, CBMS Regional Conference
Series in Mathematics, 87, American Mathematical Society, Providence, RI, 1996.
[16] Fornæss J.-E. and Sibony N., Complex dynamics in higher dimensions. Notes
partially written by Estela A. Gavosto, NATO Adv. Sci. Inst. Ser. C Math. Phys.
Sci., 439, Complex potential theory (Montreal, PQ, 1993), 131-186, Kluwer Acad.
Publ., Dordrecht, 1994.
[17] ——, Complex dynamics in higher dimension. I. Complex analytic methods in
dynamical systems (Rio de Janeiro, 1992), Ast´erisque, 222 (1994), 5, 201-231.
[18] ——, Complex dynamics in higher dimension. II. Modern methods in complex
analysis (Princeton, NJ, 1992), 135-182, Ann. of Math. Stud., 137, Princeton
Univ. Press, Princeton, NJ, 1995.
[19] Freire A., Lopes A. and Ma˜n´e R., An invariant measure for rational maps, Bol.
Soc. Brasil. Mat., 14 (1983), no. 1, 45-62.
[20] H¨ormander L., An introduction to complex analysis in several variables, Third
edition, North-Holland Mathematical Library, 7, North-Holland Publishing Co.,
Amsterdam, 1990.
[21] Lyubich M. Ju., Entropy properties of rational endomorphisms of the Riemann
sphere, Ergodic Theory Dynam. Systems, 3 (1983), no. 3, 351-385.
[22] Para M.R., The Jacobian cocycle and equidistribution towards the Green current,
preprint, 2011. arXiv:1103.4633v1
[23] Sibony N.,
Dynamique des applications rationnelles de Pk,
Panoramas et
Synth`eses, 8 (1999), 97-185.
[24] Taﬂin J., Equidistribution speed towards the Green current for endomorphisms of
Pk, Advances in Math., to appear. arXiv:1011.0641
[25] Triebel H., Interpolation theory, function spaces, diﬀerential operators, North-
Holland, 1978.
[26] Yuan X., Algebraic Dynamics, Canonical Heights and Arakelov Geometry,
preprint, 2011.
T.-C. Dinh, UPMC Univ Paris 06, UMR 7586, Institut de Math´ematiques de Jussieu, F-
75005 Paris, France. dinh@math.jussieu.fr, http://www.math.jussieu.fr/∼dinh
N. Sibony, Universit´e Paris-Sud, Math´ematique - Bˆatiment 425, 91405 Orsay, France.
nessim.sibony@math.u-psud.fr
11

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
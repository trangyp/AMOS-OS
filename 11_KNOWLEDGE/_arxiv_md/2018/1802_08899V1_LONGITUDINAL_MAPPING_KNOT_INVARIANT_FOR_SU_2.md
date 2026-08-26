---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1802.08899v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1802.08899v1_Longitudinal_Mapping_Knot_Invariant_for_SU_2_

> Source: 1802.08899v1_Longitudinal_Mapping_Knot_Invariant_for_SU_2_.pdf

> Pages: 20

---


## Page 1


Longitudinal Mapping Knot Invariant for SU(2)
W. Edwin Clark, Masahico Saito
Department of Mathematics and Statistics
University of South Florida
Abstract
The knot coloring polynomial deﬁned by Eisermann for a ﬁnite pointed group is generalized
to an inﬁnite pointed group as the longitudinal mapping invariant of a knot. In turn this can be
thought of as a generalization of the quandle 2-cocycle invariant for ﬁnite quandles. If the group
is a topological group then this invariant can be thought of a topological generalization of the
2-cocycle invariant. The longitudinal mapping invariant is based on a meridian-longitude pair
in the knot group. We also give an interpretation of the invariant in terms of quandle colorings
of a 1-tangle for generalized Alexander quandles without use of a meridian-longitude pair in
the knot group. The invariant values are concretely evaluated for the torus knots T(2, n), their
mirror images, and the ﬁgure eight knot for the group SU(2).
1
Introduction
In this paper all knots will be oriented and we write equality for orientation preserving ambient
isotopy. For a knot K we write r(K) for K with orientation reversed and m(K) for the mirror
image of K. It is known that the knot quandle Q(K) distinguishes distinct oriented knots K1 and
K2 if and only if K2 ̸= rm(K1) ( [13, 17] ). The knot group πK cannot distinguish K from s(K)
for any s ∈{r, m, rm} (see, e.g., [2]). It follows that neither the set of (quandle) homomorphisms
HomQnd(Q(K), Q) from Q(K) to a quandle Q nor the set HomGp(πK, G) of (group) homomorphisms
from πK to a group G is a complete invariant of oriented knots.
In the case of quandles a stronger invariant (the 2-cocyle invariant or 2-cocycle state-sum in-
variant) was obtained in [3] using a 2-cocycle ϕ for a ﬁnite quandle Q with coeﬃcients in an abelian
group Λ. One deﬁnes a mapping
Bϕ : HomQnd(Q(K), Q) →Λ :
ρ 7→Bϕ(ρ)
whose ﬁbers determine a partition of HomQnd(Q(K), Q) indexed by Λ. Since Q is ﬁnite this partition
can be expressed as an element Φϕ
Q(K) of the group ring Z[Λ]. See [5] for evidence that the 2-cocyle
invariant might be a complete invariant for oriented knots.
In the case of groups the knot group peripheral system (πK, mK, lK), where (mK, lk) is a
meridian-longitude pair, is a complete invariant of oriented knots (see [2]).
Using this, Eiser-
mann [9] deﬁned the knot coloring polynomial for a pointed ﬁnite group (G, x) corresponding to a
peripheral system (πK, mK, lK) as
P x
G(K) =
X
ρ
ρ(lK)
1
arXiv:1802.08899v1  [math.GT]  24 Feb 2018


## Page 2


where the sum is taken over all homomorphism ρ : πK →G with ρ(mK) = x. It turns out that
longitude images lie in Λ = C(x) ∩G′ and hence P x
G(K) is an element of the group ring Z[Λ].
Eisermann shows in [9] that when G is ﬁnite and Λ is abelian a knot coloring polynomial can be
expresssed as a 2-cocycle invariant over the conjugation quandle xG and conversely a 2-cocycle
invariant for a ﬁnite quandle Q is a specializations of a knot coloring polynomial for G = Inn( ˜Q)
where ˜Q is the abelian extension corresponding to the given 2-cocycle. In particular, any knots
distinguishable by 2-cocycle invariants are distinguishable by knot coloring polynomials. We note
however that in general the price one pays for this is a group much larger than the quandle.
In case G is inﬁnite the coeﬃcients of P x
G(K) may be inﬁnite, then we replace it by the longit-
udinal mapping
Lx
G(K) : HomGp(πK, mK; G, x) →Λ,
ρ 7→ρ(lK),
where HomGp(πK, mK; G, x) is the set of homomorphisms ρ : πK →G with ρ(mK) = x. If G is a
topological group, Lx
G(K) may be thought of as a topological analogue of the 2-cocycle invariant
or the knot coloring polynomial. This is the invariant we examine for the case G = SU(2) in this
paper. We ﬁnd Lx
G(K) when K is a torus knot T(2, n) for odd n ≥3 and when K is the ﬁgure
eight knot 41.
Let Q be any quandle (possibly inﬁnite) and let T be a 1-tangle diagram whose closure is the
knot K. Denote the initial arc of T by 0 and the terminal arc by n. For arbitrary ﬁxed e ∈Q let
Cole
Q(T) denote the set of colorings of T by quandle Q such that C(0) = e. Furthermore, by Lemma
2.2 in [5], for C ∈Cole
Q(T), b = C(n) satisﬁes Rb = Re. That is, b lies the the ﬁber Fe = inn−1(Re).
We deﬁne the mapping
Ψe
Q(K) : Cole
Q(T) →Fe,
C 7→C(n).
In the appendix we show that if Q is the generalized Alexander Quandle GAlex(G′, fx) constructed
from the pointed group (G, x) where fx(u) = x−1ux, then Lx
G(K) is equivalent to Ψe
Q(K) where
e = 1. This gives a way to construct the longitudinal mapping without use of a meridian-longitude
pair.
2
Basic Deﬁnitions
In this section we brieﬂy review some deﬁnitions and examples. More details can be found, for
example, in [4].
If X is a set with a binary operation ∗the right translation Ra : X →X, by a ∈X, is deﬁned
by Ra(x) = x ∗a for x ∈X. The magma (X, ∗) is a quandle if each right translation Ra is an
automorphism of (X, ∗) and every element of X is idempotent. A quandle homomorphism between
two quandles X, Y is a map f : X →Y such that f(x ∗X y) = f(x) ∗Y f(y), where ∗X and
∗Y denote the quandle operations of X and Y , respectively. A quandle isomorphism is a bijective
quandle homomorphism, and two quandles are isomorphic if there is a quandle isomorphism between
them. The set of quandle homomorphisms from X to Y is denoted by HomQnd(X, Y ). A quandle
epimorphism f : X →Y is a covering [10] if f(x) = f(y) implies a ∗x = a ∗y for all a, x, y ∈X.
For a quandle (X, ∗), since Ra for each a ∈X is an automorphism, one may deﬁne the binary
operation ¯∗by x ¯∗y = R−1
y (x). This gives a quandle structure on X, called the dual quandle. The
subgroup of Sym(X) generated by the permutations Ra, a ∈X, is called the inner automorphism
2


## Page 3


group of X, and is denoted by Inn(X).
The map inn : X →inn(X) ⊂Inn(X) (which is a
quandle under conjugation) deﬁned by inn(x) = Rx is called the inner representation. An inner
representation is a covering.
A quandle is indecomposable if Inn(X) acts transitively on X. We use indecomposable here
rather than connected to avoid confusion with the topological sense of the word. A quandle is
faithful if the mapping inn : X →Inn(X) is an injection.
As in Joyce [13], given a group G and and f ∈Aut(G), a quandle operation is deﬁned on G by
x ∗y = f(xy−1)y, x, y ∈G. We call such a quandle a generalized Alexander quandle and denote
it by GAlex(G, f). If G is abelian, such a quandle is known as an Alexander quandle or aﬃne
quandle.
b
*
a
b
c = 
ε =
1
*
a
b
c = 
b
a
ε =
1
a
Figure 1: Colored crossings, positive (left) and negative (right)
Let D be a diagram of a knot K, and A(D) be the set of arcs of D. A coloring of a knot
diagram D by a quandle X is a map C : A(D) →X satisfying the condition depicted in Figure 1
at every positive (left) and negative (right) crossing. respectively. The set of colorings of D by X
is denoted by ColX(D). There is a bijection from HomQnd(Q(K), X) to ColX(D). The cardinality
|ColX(D)| is a knot invariant (e.g. see [4]).
A 1-tangle, or a long knot, is a properly embedded arc in a 3-ball, and the equivalence of long
knots is deﬁned by ambient isotopies of the 3-ball ﬁxing the boundary. A diagram of a 1-tangle is
deﬁned in a manner similar to a knot diagram, from a regular projection to a disk by specifying
crossing information. An orientation of a 1-tangle is speciﬁed by an arrow on a diagram. A knot
diagram is obtained from a 1-tangle diagram by closing the end points by a trivial arc outside of a
disk. This procedure is called the closure of a 1-tangle. If a 1-tangle is oriented, then the closure
inherits the orientation. Two diagrams of the same 1-tangle are related by Reidemeister moves.
There is a bijection between knots and 1-tangles for classical knots, and invariants of 1-tangles give
rise to invariants of knots, see, for example, [10,18].
A quandle coloring of an oriented 1-tangle diagram is deﬁned in a manner similar to those for
knots. We do not require that the end points receive the same color for a quandle coloring of
1-tangle diagrams. However this will be the case for a conjugation quandle. For a quandle Q and
x ∈Q, denote by Colx
Q(T) the set of colorings of a 1-tangle T by Q with the initial arc colored by
x.
3
Computation of the Longitudinal Mapping
For convenience we often identify the diagram of a tangle T with the tangle itself.
3


## Page 4


Deﬁnition 3.1. (Wirtinger code
Eisermann [10]) Label the arcs of a 1-tangle T by integers,
A(T) = {0, . . . , n}, such that 0 and n are the initial and terminal arcs, respectively, and the
remaining arcs are labeled in order when traveled along the tangle from 0 to n. At the end of arc
number i −1, we undercross arc κ(i) = κi and continue on arc number i. Let ϵ(i) = ϵi be the sign
of crossing i. Note that these are maps κ : {1, . . . , n} →{0, . . . , n} and ϵ : {1, . . . , n} →{1, −1}.
The pair (κ, ϵ) is called the Wirtinger code of the diagram T.
The 1-tangle group πT with diagram T and Wirtinger code (κ, ϵ) allows the presentation
πT = ⟨x0, x1, . . . , xn | r1, . . . , rn⟩, where ri is the relation xi = x−ϵi
κi xi−1xϵi
κi.
As in [9] we choose the meridian
mT = x0
and the (preferred) longitude
lT = x−w(T)
0
xϵ1
κ1xϵ2
κ2 · · · xϵn
κn.
See Remark 3.13 of [2] for this form of the longitude. The knot group πK is isomorphic to πT .
For a pointed ﬁnite group (G, x), Eisermann deﬁned the knot coloring polynomial of K to be
P x
G(K) =
X
ρ
ρ(lT ),
where the sum is taken over all homomorphisms ρ : πT →G with ρ(mT ) = x. It turns out (see [9])
that the values ρ(lT ) lie in the longitudinal group Λ = C(x) ∩G′ where C(x) is the centralizer of x
and G′ is the commutator subgroup of G. Thus P x
G(K) lies in the group ring Z[Λ].
Let Repx
G(T) be the set of homomorphisms ρ : πT →G with ρ(mT ) = x, and Colx
Q(T) be the
set of colorings C by a quandle Q such that C(0) = x, where 0 is the initial arc of T. There is a
bijection between Repx
G(T) and Colx
Q(T) where Q is the conjugacy class xG of x under the product
a ∗b = b−1ab.
We wish to extend Eisermann’s knot coloring polynomial to groups not necessarily ﬁnite.
Deﬁnition 3.2. Let (G, x) be any pointed group. Let K be a knot and T be a 1-tangle corres-
ponding to K. We deﬁne the knot invariant
Lx
G(K) : Repx
G(T) →Λ,
ρ 7→ρ(lT ).
We call it the longitudinal mapping. When there is no chance of confusion we write L in place
of Lx
G(K).
We shall say that two such longitudinal mappings L1 : Repx
G(T1) →Λ and L2 :
Repx
G(T2) →Λ are equivalent if there is a bijection β : Repx
G(T1) →Repx
G(T2) such that L1 = L2β.
Clearly the longitudinal mapping L : Repx
G(T) →Λ is a knot invariant up to equivalence of
mappings and if G is a topological group L is continuous. In this case β must be a homeomorphism.
See Rubinsztein [20] for the topology on ColQ(T).
Remark 3.3. See the appendix for a deﬁnition of L that doesn’t depend on the meridian-longitude
pair (mT , lT ).
4


## Page 5


For a ﬁnite group G the knot coloring polynomial is P x
G(K) = P
v∈Λ |L−1(v)|v. Thus L can
be seen as an analogue of the knot coloring polynomial deﬁned for topological quandles. Since the
knot coloring polynomial is a generalization of the quandle 2-cocycle invariant (see Theorem 3.24
in [9]), the invariant L is a generalization of the quandle 2-cocycle invariant. See [5, 9] for more
details of relations among these invariants. A similar but diﬀerent invariant using longitudes was
considered in [18].
Remark 3.4. Note that the group Λ acts on the set of homomorphisms ρ : πK →G with ρ(mK) =
x by setting ρg(a) = g−1ρ(a)g for a ∈G. Since g ∈C(x) it follows that ρg(mK) = x. Hence if Λ is
abelian, then L is constant on the orbits of this action by Λ. In our application, Λ is abelian. Thus
for example for a two-bridge knot with diagram T, suppose the arcs x0 and x1 in the above notation
are the two bridges. Then L(ρ) is completely determined by the values ρ(x0) = ρ(mK) = x ∈G
and the values of ρ(x1).
Proposition 3.5. Lx
G(rm(K))(ρ) = Lx
G(K)(ρ)−1 for all ρ ∈Repx
G(T).
Proof. This is immediate from the fact that if (πK, mK, lK) is a peripheral system for knot K then
(πK, mK, lK−1) is a peripheral system for the knot rm(K) ( [14], Chapter 6).
4
Background for SU(2)
For the remainder of the paper, we examine the invariant L for (G, x) = (SU(2), x) with various
choices of x. We represent SU(2) by the group of unit quaternions, that is,
SU(2) = {a + bi + cj + dk : a2 + b2 + c2 + d2 = 1}.
The group SO(3) will also be of use. Elements of SO(3) will be denoted by Rotθ(v), θ ∈R,
v ∈S2. If u ∈R3, uRotθ(v) is the vector obtained by rotating u about v by θ radians using the
right-hand rule.
We represent elements of R3 as pure quaternions u = u1i + u2j + u3k and we identify the set of
pure unit quaternions with the sphere S2. Then each element of SU(2) can be represented the form
eθu = cos(θ) + sin(θ)u,
u ∈S2,
0 ≤θ < 2π.
Note that a pure quaternion u satisﬁes u2 = −1 and hence the quaternions eθu for ﬁxed u
behave just like complex numbers eθi = cos(θ) + sin(θ)i.
From [7] (Section 1.2) the conjugacy classes of SU(2) are given by
˜Cθ = {eθu : u ∈S2},
for 0 ≤θ ≤π. In this case ˜C0 = {1}, ˜Cπ = {−1} and for 0 < θ < π, ˜Cθ is a sphere. This also
follows from Lemma 4.1 below.
It is known (see for example [16], Theorem 5.1) that for u, v ∈S2 and θ ∈R that
eθuve−θu = vRot2θ(u).
The double covering homomorphism φ : SU(2) →SO(3) may be deﬁned by
vφ(q) = q−1vq.
5


## Page 6


In this case if q = eθu, then φ(q) = Rot−2θ(u), the rotation by −2θ radians about the unit vector
u. We must take φ(q) to be q−1vq instead of qvq−1 since we write the rotation operator on the
right of the argument.
Lemma 4.1. For ﬁxed θ, β ∈R and u, v ∈S2 we have
e−βveθueβv = eθw.
where w = uRot−2β(v).
Proof. We compute:
e−βveθueβv
=
e−βv(cos(θ) + sin(θ)u)eβv
=
cos(θ) + sin(θ)e−βvueβv
=
cos(θ) + sin(θ)uRot−2β(v)
=
eθw,
where w = uRot−2β(v).
Since SO(3) acts transitively on S2 from Lemma 4.1 we have:
Corollary 4.2. The conjugacy class of x = eθu has the form
xSU(2) = {eθv : v ∈S2}.
Deﬁnition 4.3. For 0 < ψ < 2π we denote by S2
ψ the quandle with underlying set S2 and product
u ∗v = uRotψ(v), for u, v ∈S2. We call this a spherical quandle.
Lemma 4.4. For 0 < θ < π the mapping u 7→eθu is an isomorphism from quandle S2
ψ with
ψ = 2π−2θ to the conjugacy class ˜Cθ = {eθu : u ∈S2} considered as a quandle under conjugation:
p ∗q = q−1pq.
Proof. The result follows from Lemma 4.1 by taking β = θ.
Lemma 4.5. SU(2) is a perfect group, that is, it is its own commutator subgroup.
Proof. By [19], Prop. 10.24 every unit quaternion q has the form q = aba−1b−1 for non-zero
quaternions a and b. The same holds if we normalize a and b.
Lemma 4.6. If x = eθu for 0 < θ < π then the centralizer C(x) is the circle group:
{eβu : 0 ≤β < 2π}.
Hence, the longitudinal group for (SU(2), x) is given by
Λ = C(x) ∩SU(2)′ = C(x) = {eβu : 0 ≤β < 2π}.
Proof. This follows from Lemma 4.1 and the fact that for 0 < β < π, uRotβ(v) = u, with u, v ∈S2
if and only if v = ±u together with the fact that
{eβu : 0 ≤β < 2π} = {eβ(−u) : 0 ≤β < 2π}.
6


## Page 7


Remark 4.7. It is easy to see that for x = eθu the conjugacy classes xSU(2) = ˜Cθ and (−x)SU(2) =
˜Cθ+π are isomorphic via q 7→−q as conjugation quandles. Note also that u 7→−u leaves the
longitude invariant. Thus for our purposes it suﬃces to consider only those x = eθu for 0 < θ < π.
Note that Rotψ(v) = Rot−ψ(−v). It follows that S2
ψ is isomorphic to S2
−ψ via u 7→−u. Thus when
coloring knots by the family of quandles S2
ψ we may restrict ψ to the interval (0, π]. And for the
quandles ˜Cθ we may restrict θ to the interval [π/2, π).
Fix θ ∈(0, π) and x = xθ = eθi where i = (1, 0, 0) we are interested in computing Lθ = Lxθ
SU(2).
5
Knot Colorings by the Spherical Quandles S2
ψ
Knot group representations in SU(2) were studied in Klassen [15], in particular for all torus knots
and twist knots. We present explicit colorings of torus knots T(2, n) and the ﬁgure eight knot in
this section and we compute the longitudinal mappings of these knots in the next section.
Fix ψ ∈[0, 2π) and as above denote by Rotψ(v) the rotation by ψ about v. Then the quandle
structure on Q = S2
ψ is as deﬁned in Deﬁniton 4.3, for u, v ∈S2, by u ∗v = uRotψ(v) with
right action of the rotation. Denote by ⟨u, v⟩the inner product of u, v in R3, so that S2
ψ = {u ∈
R3 | ⟨u, u⟩= 1}. We also denote the length of the shortest spherical geodesic segment between
u, v ∈S2
ψ by d(u, v) = arccos(⟨u, v⟩), and we denote the (directed) spherical angle at a vertex v
formed by three unit vectors u, v, w ∈S2
ψ by ∠(uvw) = ψ if w = uRotψ(v) and 0 ≤ψ < 2π.
Let κ : {1, . . . , n} →{0, . . . , n} and ϵ : {1, . . . , n} →{1, −1} be the Wirtinger code of a tangle
diagram T as described in Deﬁnition 3.1.
We observe that the coloring condition depicted in
Figure 1 is formulated as follows. Let Q = S2
ψ. Then a coloring ρ ∈Colx
Q(T) corresponds to a
sequence of points
(ρ(0), . . . , ρ(n)) ∈(S2
ψ)
n+1
satisfying
ρ(i) = ρ(i −1)Rotψ(ρ(κ(i)))ϵ(i),
i ∈{1, . . . , n}.
Thus we have the following, as stated in [15]:
Lemma 5.1. For a coloring of a knot diagram by Q = S2
ψ, consider a crossing with the colors
(a, b) as depicted in Figure 1. Then c = a ∗b if and only if d(a, b) = d(b, c) and ∠(abc) = ψ. In
particular, any orientation preserving isometry of the sphere takes a coloring to a coloring.
Corollary 5.2. For any coloring ρ ∈Colx
Q(T) such that (ρ(0), . . . , ρ(n)) ∈(S2
ψ)n+1,
(ρ(0)Rotφ(x), . . . , ρ(n)Rotφ(x))
deﬁnes a coloring in Colx
Q(T) for all φ ∈[0, 2π).
Remark 5.3. As ψ varies, we have a continuous family {S2
ψ : ψ ∈(0, 2π)} of quandles. This
leads to continuous family of knot colorings by ˜Cθ, where θ = π −ψ/2. The longitudinal mapping
invariant, then, can be seen as a continuous family of invariants Lxθ
SU(2) over θ.
7


## Page 8


Let T be a tangle corresponding to a 2-bridge knot K. Then we may choose a diagram of T to
be a diagram with two bridges, i.e., there are two arcs x0 and x1 such that x0 is the initial arc of
T, and the colors of x0 and x1 uniquely determine a color of all arcs of T.
Let Q = S2
ψ, and we ﬁx x = i = (1, 0, 0). Thus for all elements ρ ∈Colx
Q(T), we have ρ(x0) = x
as x0 is the initial arc of T. Let E ⊂S2
ψ be half of the equator,
E = {(cos φ, sin φ, 0) : 0 ≤φ ≤π}.
Lemma 5.4. Let Q = S2
ψ and let x ∈SU(2), T, x0, and x1 be as above. Suppose that the number
h of elements ρ ∈Colx
Q(T) such that ρ(x1) ∈E and ρ(x1) ̸= ρ(x0) is ﬁnite. Then Colx
Q(T) is
homeomorphic to h copies of S1.
Proof. This follows from Corollary 5.2.
Remark 5.5. In [15], non-abelian representations of knot groups in SU(2) for torus knots and twist
knots up to conjugation action were determined by Klassen. For each ψ, Colx
Q(T) ∩E, Q = S2
ψ
corresponds to Klassen’s representation. Thus the sets Colx
Q(T) are known from the paper [15].
We determine explicit colorings of T(2, n) and the ﬁgure 8 knot by S2
ψ in the next two subsections
and compute the longitudinal mappings for these knots in the next section.
5.1
Colorings of the torus knots T(2, n) by S2
ψ
Let n = 2k + 1 and we label the arcs of T(2, n) by ui as in Figure 2. For later convenience in
computing the longitude, we use the notation ui = q2i and uk+i = q2i−1 for i = 0, . . . , k as depicted
in Figure 2. Note that the subscripts on the u’s correspond to the labeling of the Wirtinger code
(Deﬁnition 3.1).
4
n
n−1
q
0
u
0
q
uk+1
uk+2
u1
u2
uk
n
u
1
q
q
2
3
q
q
q
Figure 2: Arc labeling diagram for T(2, n)
Let pi, i = 0, . . . , n −1 (subscripts taken modulo n), be a set of points on S2 that are the
vertices of a spherical regular n-gon arranged in counterclockwise order, for example,
pi = (
p
1 −r2 cos((2π/n)i),
p
1 −r2 sin((2π/n)i), r)
where r ∈(−1, 1). Then the side lengths d(pi, pi+1) and the angles ∠pi−1pipi+1 are constant.
Lemma 5.6. Let n = 2k + 1. Let Ch be the map A(T(2, n)) →S2
ψ deﬁned by Ch(qi) = phi where
the subscripts are taken modulo n. If ψ = ∠p(i−1)hpihp(i+1)h, then Ch deﬁnes a coloring of T(2, n).
Proof. From Figure 2, Ch(qi), i = 0, . . . , n −1, gives rise to a non-trivial coloring if the following
equations are satisﬁed: Ch(qi−1)∗Ch(qi) = Ch(qi+1) for all i, where the subscripts are taken modulo
n. Since the lengths d(pih, p(i+1)h) and the angles ∠p(i−1)hpihp(i+1)h are constant, the conditions
for a coloring in Lemma 5.1 are satisﬁed.
8


## Page 9


Figure 3: Spherical regular star polygons for n = 7
Example 5.7. For n = 7 and h = 1, 2, 3 respectively, the points corresponding to the colorings
are illustrated in Figure 3. For each h = 1, 2, 3, the ranges of ψ are computed from Lemma 5.8
below as (5/7)π < ψ < (9/7)π , (3/7)π < ψ < (11/7)π, and (1/7)π < ψ < (13/7)π.
Lemma 5.8. Let n = 2k + 1. For h = 1, . . . , k, there exists a regular star n-gon with vertices pih,
i = 1, . . . , n −1, with ψ = ∠p(i−1)hpihp(i+1)h if and only if
(n −2h)π/n < ψ < (n + 2h)π/n.
Proof. Assume that there exists such a regular star n-gon with ψ = ∠p(i−1)hpihp(i+1)h. The angle
∠p(i−1)hpihp(i+1)h is smaller as the length d(pih, p(i+1)h) is smaller, and hence the lower bound of
such ψ is computed as the corresponding angle ∠p(i−1)hpihp(i+1)h for a planar, inﬁnitesimal regular
n-gon formed by pih.
For the planar regular n-gon with vertices pi, i = 0, . . . , n −1 in this cyclic order, the angle
∠pi−1pipi+1 equals [(n −2)/n]π since there are n −2 triangles in a regular n-gon. This angle
∠p0−1p0p1 at p0 is equally divided to the angle ∠pip0pi+1 inscribed by pi and pi+1 for each i,
hence ∠pip0pi+1 = π/n. The angle ∠p1p0ph and ∠pkhp0pn−1 consist of (h −1) parts of π/n.
Hence the lower bound is computed as
∠php0pkh = ∠pn−1p0p1 −(∠p1p0ph + ∠pkhp0pn−1) = [ (n −2) −2(h −1) ]π/n = (n −2h)π/n.
See Figure 4. Since the bounds are symmetric about π, we obtain the upper bound of
π + (π −(n −2h)π/n) = (n + 2h)π/n
as desired.
Corollary 5.9. For n = 2k + 1 there is a non-trivial coloring of T(2, n) by S2
ψ if and only if
(n −2h)π/n < ψ < (n + 2h)π/n,
for some h = 1, . . . , k.
9


## Page 10


p
0
p
h
p
kh
p
n−1
p
p2
pn−2
1
Figure 4: Angles of Ch
Proof. Immediate from Lemma 5.6 and Lemma 5.8.
Remark 5.10. For ﬁxed n and h as ψ ranges over the interval ( (n −2h)π/n, π ] continuously, the
polygons formed by the lengths d(pih, p(i+1)h) continuously change from an inﬁnitesimal polygon
to a polygon on the equator. As ψ approaches the lower bound (n−2h)π/n, the polygon converges
to a planar polygon.
The coloring condition holds for the Euclidean rotational quandles investigated in [12], in which
Inoue proved that there exists a non-trivial coloring by planar rotational quandles if and only if the
Alexander polynomial has a root on the unit circle S1 ⊂C. The Alexander polynomial of T(2, n)
is a factor of x2n −1.
Remark 5.11. In [15], SU(2) representations up to conjugacy are studied. Furthermore, in [11],
under certain conditions satisﬁed by T(2, n) and twist knots, the representations are deformations
of dihedral representations at ψ = π.
These results are seen in the above continuous family of star polygons. They start from inﬁnites-
imal planar polygons and converge to the equatorial “polygons” that correspond to Fox colorings
by dihedral quandles.
Proposition 5.12. Let Q = S2
ψ and T be a tangle of T(2, n) as depicted in Figure 2. For n = 2k+1
and h = 1, . . . , k, if (n −2h)π/n < ψ ≤(n −2h + 2)π/n then
Colx
Q(T) = ⊔hS1,
h copies of disjoint circles.
Proof. By Lemma 5.8, if ψ is in the stated range, then for any h′ ≤h, h′ satisﬁes the condition
stated in Lemma 5.8.
In Figure 2, the arcs q0 and q1 are taken as x0 and x1 in Lemma 5.4.
Hence in the notation in Lemma 5.4, Colx
Q(T) ∩E consists of h points, and the result follows from
Lemma 5.4.
5.2
Colorings of the ﬁgure eight knot by S2
ψ
In this subsection we describe the colorings of a ﬁgure eight knot by the spherical quandle S2
ψ.
Lemma 5.13. A sequence U = (u0, u1, u2, u3) deﬁnes a coloring if and only if the following
conditions are satisﬁed in S2
ψ: d(u1, u2) = d(u2, u0) = d(u0, u3), d(u0, u1) = d(u1, u3) = d(u3, u2),
and ∠(u0u2u1) = ∠(u0u1u3) = ∠(u2u3u1) = ∠(u2u0u3) = ψ.
10


## Page 11


Proof. Direct inspection of Figure 5 gives the following:
u0 ∗u2 = u1, u0 ∗u1 = u3, u2 ∗u3 = u1, u2 ∗u0 = u3,
where u4 = u0 and the equalities are derived from the crossings. By Lemma 5.1 the statement
follows.
1
u4
u0
u3
u2
u
Figure 5: Colorings of the ﬁgure eight knot
Lemma 5.14. For ψ = 2π/3 and ψ = 4π/3 there is a unique solution U to the equations in
Lemma 5.13 such that
u0 = xψ = (1, 0, 0) = i and u2 = (cos(β), sin(β), 0).
The solution U forms a regular spherical tetrahedron. In this case β = arccos (−1/3) .
For 2π/3 < ψ < 4π/3, there are two nontrivial solutions U to the equations in Lemma 5.13
such that
u0 = xψ = (1, 0, 0) = i and u2 = (cos(β), sin(β), 0).
The solutions are determined by the two values of u2, u2 = (cos(βi), sin(βi), 0), where for i = 1, 2,
β1
=
π −arccos( −1 +
p
4 cos2(ψ) −4 cos(ψ) −3)/2 (cos(ψ) −1),
β2
=
arccos( 1 +
p
4 cos2(ψ) −4 cos(ψ) −3)/2 (cos(ψ) −1).
Proof. This comes directly from Maple computations.
The Maple worksheets can be found at
[6].
Remark 5.15. Note that by Lemma 5.2 it suﬃces to restrict β to the interval (0, π].
Remark 5.16. Maple computations give the above exact solutions. It was also pointed out by
Shin Satoh (via personal communication) that the spherical laws of sine and cosine, together with
the area formula that a spherical triangle with angles α, β, γ has area α + β + γ −π, yield the
solutions.
Remark 5.17. The solutions for βi for i = 1, 2 in Lemma 5.14 are plotted in Figure 6 for ψ ∈
[2π/3, 4π/3]. Each angle βi is 0 outside of this interval. Hence the colorings are trivial for ψ outside
this interval.
11


## Page 12


Figure 6: The graphs of βi, i = 1, 2, representing colorings of the ﬁgure eight knot
Remark 5.18. The solutions U in Lemma 5.14 for ψ = 2π/3, 7π/9, 19π/20 and π form vertices of
spherical tetrahedra as depicted in Figure 7.
We recall that the ﬁgure eight knot is non-trivially colorable by the tetrahedral quandle (the
solution U at ψ = 2π/3) and the dihedral quandle R5 (Fox 5-colorable). Note also that since the
minimal diagram in Figure 5 has only four arcs, four colors in R5 are used for non-trivial colorings.
Up to mirror symmetry, there are two choices of elements of u2 from R5 for a ﬁxed element for
u0. As in Remark 5.11, there are continuous family of solutions as ψ varies from 2π/3 to π. A
single regular tetrahedral coloring bifurcates to two branches of solutions as in Lemma 5.14, and
converges to the two solutions of Fox colorings, as described in [11]. Animations of this situation
can be found at http://shell.cas.usf.edu/~saito/SphericalQuandle/.
Remark 5.19. More generally, Klassen [15] described the representations of knot groups in SU(2)
for twist knots Twm, m > 0, and proved that up to conjugation it consists of m/2 circles if m is
even, and ⌊m/2⌋circles and a single open arc if m is odd. The cases m = 1 and m = 2 correspond
to the trefoil and the ﬁgure eight knot, respectively.
Remark 5.20. It is well known that the Alexander polynomial of Twm for odd m is given by
∆Twm(t) = (m+1)t2 −2mt+(m+1). Direct calculations show that ∆Twm(t) has roots on S1 ⊂C,
and by [12], there is a nontrivial coloring by planar rotational quandle for ψ = arg(α), where α is
its root. Let α be the root with smaller argument. Then for odd m there is a non-trivial coloring
of Twm by S2
ψ for arg(α) < ψ < arg(¯α).
6
Longitudinal Mapping Invariant Values
In this section we determine the invariant values Lθ for the torus knots T(2, n) and the ﬁgure eight
knot.
12


## Page 13


Figure 7: Colorings for the ﬁgure eight knot by S2
ψ for ψ = 2π/3, 7π/9, 19π/20 and π.
6.1
Torus knots T(2, n)
We used the labeling of the diagram of T(2, n) in Figure 2, where n = 2k + 1 is odd.
Lemma 6.1. for n = 2k + 1 and h = 1, . . . , k, T(2, n) is non-trivially colored by ˜Cθ if and only if
(n −2h) π
2n
< θ < (n + 2h) π
2n
.
Proof. By Lemma 4.4 for 0 < θ < π the quandle S2
ψ, ψ = 2π −2θ, is isomorphic to the conjugacy
class ˜Cθ = {eθu : u ∈S2} considered as a quandle under conjugation: p ∗q = q−1pq. Clearly
the isomorphism u 7→eθu takes a coloring to a coloring. By Corollary 5.9 for n = 2k + 1 there is a
non-trivial coloring of T(2, n) by S2
ψ if and only if for some h = 1, . . . , k we have
(n −2h)π/n < ψ < (n + 2h)π/n,
since ψ = 2π −2θ this is equivalent to
(n −2h) π
2n
< θ < (n + 2h) π
2n
.
13


## Page 14


Lemma 6.2. Let n = 2k + 1, k ≥1. Let G be a group. Let qi, i = 0, 1, . . . , n −1, be the colors of
the arcs, as depicted in Figure 2, of a coloring of the diagram by G. Then qi satisfy qi+1 = q−1
i
qi−1qi
for i = 1, . . . , n −1 and qn = q0.
We thank Razvan Teodorescu for the idea of the following proof.
Lemma 6.3. Let n = 2k + 1, k ≥1, and G be a group. For a coloring C of the diagram of T(2, n)
in Lemma 6.2, let q = q0q1. Then the longitude is given by L(C) = q−2n
0
qn.
Proof. By Lemma 6.2, we have qiqi+1 = qi+1qi+2 for i = 0, . . . , n −2, and qn−1q0 = q0q1. Note that
q = qiqi+1 for all i.
For any coloring C, from Figure 2, we compute the longitude as
L(C) = q−n
0
(q1q3 · · · q2k−3) (q0q2 · · · q2k).
To evaluate this, we compute
q2n
0 L(C) = qn
0 (q1q3 · · · q2k−3) (q0q2 · · · q2k).
Since q0q1 = q1q2, we have
q2n
0 L(C)
=
(q0 · · · q0) (q0q1) (q3 · · · q2k−3) (q0q2 · · · q2k)
=
(q0 · · · q0) (q1q2) (q3 · · · q2k−3) (q0q2 · · · q2k).
Further applying q0q1 = q1q2 and q2q3 = q3q4, we obtain
=
(q0 · · · q0) (q0q1) (q2q3) (q5 · · · q2k−3) (q0q2 · · · q2k)
=
(q0 · · · q0) (q1q2) (q3q4) (q5 · · · q2k−3) (q0q2 · · · q2k).
Inductively we obtain
(q0 · · · q0) (q1q2q3q4 · · · q2k) (q0q2 · · · q2k).
There are k + 1 copies of q0 in the ﬁrst factor, (qi)2k
i=1 in the second factor, and consecutive even
terms in the third factor. Then we continue with
=
(q0 · · · q0) (q1q2q3q4 · · · q2k−1) (q2kq0) (q2 · · · q2k)
=
(q0 · · · q0) (q1q2q3q4 · · · q2k−1) (q0q1) (q2 · · · q2k)
=
(q0 · · · q0) (q1q2q3q4 · · · q2k−1) (q0q1q2) (q3 · · · q2k) · · · .
In the last line, the left consecutive sequence keeps shifting to the left, as the middle pair (q0q1)
shifts to the left. Inductively, we obtain q2n
0 L(C) = (Qn−1
i=0 qi)2 = qn. Hence we obtain L(C) =
q−2n
0
qn.
Remark 6.4. In the proof of Lemma 6.3, once the computation of L(C) = q−2n
0
(Qn−1
i=0 qi)2 is
obtained, we found a diagrammatic method of obtaining the same formula. Speciﬁcally, from the
diagram in Figure 8, we can read oﬀthe longitude directly as q2n
0 L(C) = (Qn−1
i=0 qi)2.
It is noteworthy that in the following theorem, the longitudinal mapping depends only on θ,
and not on the diﬀerent colorings C corresponding to θ.
14


## Page 15


q
n
n−1
q
1
q
2
3
1
q
q
q
0
q
Figure 8: Colored diagram for T(2, n) with loops
Theorem 6.5. For any non-trivial coloring C of T(2, n), the value of the longitudinal mapping for
(SU(2), x) where x = eθi is given by
L(C) = e(π−2nθ)i = −cos(2nθ) + sin(2nθ)i.
and for the mirror image m(T(2, n)) the value of the longitudinal mapping is given by
L(C) = e(2nθ−π)i = −cos(2nθ) −sin(2nθ)i.
Proof. In the case of G = SU(2) in Lemma 6.3, we show that qn = −1, where q = q0q1 = qiqi+1
for all i. Since
q−1qiq = (qiqi+1)−1qi(qiqi+1) = qi+2,
we have q−nqiqn = qi for every i. Then qn is in C(qi) for every i. For a non-trivial coloring, there
are at least two qi and qj that do not commute, hence by Lemma 4.6, C(qi) ∩C(qj) = {±1}, so
that qn = ±1.
For each θ, we have qn = ±1, and qn is continuous with respect to θ. By Corollary 4.2, for
θ = π/2, we have S2
π isomorphic to the conjugacy class ˜Cπ/2. In this case, the colorings by S2
π up
to the action of rotations about x (cf. Corollary 5.2) are equivalent to Fox colorings by a dihedral
quandle Rm for some m. In [15], it was shown that the non-abelian representations of knot groups
of torus knots T(r, s) up to conjugacy consist of (r −1)(s −1)/2 open arcs. In our case the result
implies that the set of non-trivial colorings of T(2, n) consists of n −1 open arcs each of which
contains a coloring by the dihedral quandle Rn. Hence the fact qn = −1 follows if it is proved for
colorings by ˜Cπ/2.
Let θ = π/2, then q0 = e
π
2 i = i. In this case q1 = cos(2πm/n)i + sin(2πm/n)j for some m.
Then we compute
q = q0q1 = −cos(2πm/n) + sin(2πm/n)k = e(π−2πm/n)k.
Hence we obtain
qn = e(π−2πm/n)nk = eπ(n−2m)k = −1
since n is odd, as desired.
The resullt for m(T(2, n)) follows immediately from the result for T(2, n) via Proposition 3.5
and the known fact that r(T(2, n)) = T(2, n).
6.2
Figure eight knot
The following Lemma is immediate from Lemma 5.14 and the fact that S2
ψ is isomorphic to ˜Cθ
when ψ = 2π −2θ and the fact that the isomorphism u 7→eθu takes a coloring to a coloring.
15


## Page 16


Lemma 6.6. The ﬁgure 8 knot is non-trivially colored by ˜Cθ if and only if
π
3 ≤θ ≤2π
3 .
In which case there are two solutions for each θ ∈(π
3 , 2π
3 ), corresponding to the values of β1 and β2
in Lemma 5.14. The colorings for θ = π
3 and θ = 2π
3 are the same.
Let C(i) = ui be a coloring for the ﬁgure 8 knot by ˜Cθ for θ ∈[π/3, 2π/3], as shown in Figure 5.
Then from the deﬁnition of the longitude we obtain the following.
Lemma 6.7. Lθ(C) = u2u−1
3 u0u−1
1 .
Maple computations give the following.
Proposition 6.8. If C is a coloring of the ﬁgure 8 knot by ˜Cθ then
Lθ(C) = (cos (4 θ) −cos (2 θ) −1) ±
p
−1 + 2 cos (4 θ) −4 cos (2 θ) (sin (2 θ)) i.
The sign ± depends on the choice of βi, i = 1, 2, in Lemma 5.14.
The longitude Lθ(C) may be written as eφi where φ is given in terms of the two argument
arctan by
φ = arctan

±
q
4 (cos (2 θ))2 −4 cos (2 θ) −3 (sin (2 θ)) , 2 (cos (2 θ))2 −cos (2 θ) −2

The graph of φ as a function of θ is given in Figure 9.
Figure 9: The graph of φ where Lθ(C) = eφi for the ﬁgure 8 knot.
16


## Page 17


7
Concluding Remarks
In this paper, the knot coloring polynomial deﬁned by Eisermann [9] with ﬁnite quandles is gener-
alized to topological quandles as the longitudinal mapping invariant of long knots, which in turn
can be thought of as a generalization of the quandle 2-cocycle invariant deﬁned in [3] for ﬁnite
quandles. Such generalizations for topological quandles have long been called for, and we propose
one in this paper. The invariant values are concretely evaluated for torus knots of closed 2-braids
T(2, n) and the ﬁgure eight knot.
The following questions, for example, remain to be investigated: determine the coloring spaces
for other knots, in particular knots with more than 2 bridges; determine the θ-values with non-
trivial colorings; determine the invariant values; relations to other invariants; investigate continuous
cohomology theories of topological quandles, and relate it to the invariant discussed in this paper.
APPENDICES
A
Eisermann quandles and generalized Alexander quandles
For an alternative description of the invariant L, we focus on the following quandles found in
Lemma 25 and Remark 27 of [10].
Deﬁnition A.1. Let G be a group and x ∈G such that conjugacy class xG generates G. The
conjugacy class xG is a quandle under conjugation a ∗b = b−1ab and a ¯∗b = bab−1. Let G′ be the
commutator subgroup of G. Deﬁne the set
Eis(G, x) = {(a, g) ∈xG × G′ | a = xg}.
This set becomes an indecomposable quandle under the operations
(a, g) ∗(b, h) = (a ∗b, x−1gb),
(a, g) ¯∗(b, h) = (a ¯∗b, xgb−1),
We call this the Eisermann quandle given by the pair (G, x). We write
p : Eis(G, x) →xG,
(a, g) 7→a,
for the projection onto xG.
Eisermann [10] wrote ˜Q(G, x) for what we call here Eis(G, x). Furthermore as he pointed out
that this deﬁnition is tailor-made to capture the longitude information we need for the proof of
Lemma B.3.
Lemma A.2. If G is a group that is generated by the conjugacy class xG then xG′ = xG, Eis(G, x)
is an indecomposable quandle and the projection
p : Eis(G, x) →xG,
(a, g) 7→a
is a quandle epimorphism that is equivalent to
inn : Eis(G, x) →inn(Eis(G, x)).
The ﬁber p−1(x) is C(x) ∩G′ where C(x) is the centralizer of x in G. If C(x) ∩G′ is abelian then
p : Eis(G, x) →xG is an abelian extension.
17


## Page 18


Proof. See Lemma 25 in [10] and Appendix B in [5].
As noted by Eisermann, Eis(G, x) has an alternative description as a generalized Alexander
quandle GAlex(G′, fx) where fx is the inner automorphism fx(g) = x−1gx, g ∈G. Since G′ is a
normal subgroup, fx is an automorphism of G′ and so GAlex(G′, fx) is well-deﬁned.
Lemma A.3. For x an element of a group G the quandles Eis(G, x) and GAlex(G′, fx) are iso-
morphic.
Proof. It is easy to check that the mapping : (a, g) 7→g is the desired isomorphism.
Remark A.4. The Eisermann quandle Eis(G, x) does not determine G since there are many
groups in general with the same commutator subgroup. On the other hand every indecomposable
generalized Alexander quandle Q = GAlex(G, f) determines the group G, namely G = Inn(Q)′,
and determines the automorphism f ∈Aut(G) up to conjugacy in Aut(G).
Moreover if Q =
GAlex(G, f) is indecomposable and e ∈Inn(Q) then Q ∼= Eis(Inn(Q), Re) as noted in Corollary
B.3 of [5].
B
Alternative interpretation of L for Eisermann and Alexander
quandles
We recall the following two lemmas.
Lemma B.1 (Eisermann [10], Theorem 30). Let p : ˜Q →Q be a covering such that p(q) = x,
q ∈˜Q, and let T be a 1-tangle diagram. Then the mapping ˜C 7→p ˜C is a bijection from Colq
˜Q(T)
to Colx
Q(T).
Lemma B.2 ( [5] ). Let C : A(T) →Y be a coloring of a 1-tangle diagram T by a quandle X.
For the initial and terminal arcs 0 and n of T, respectively, let x0 = C(0) and x1 = C(n). Then
inn(x0) = Rx0 = Rx1 = inn(x1).
Now let ˜Q = Eis(G, x) and Q = xG and p : ˜Q →Q as in Lemma A.2, so that p(x, 1) = x. Let
˜C ∈Col(x,1)
˜Q
and C = p ˜C as in Lemma B.1. Let L(C) be as deﬁned above.
Proposition B.3. In the notation above let ˜C be the unique lifting of the coloring C ∈Colx
Q(T)
to Col(x,1)
˜Q
(T). Then ˜C(n) = (x, L(C)).
Proof. Let w(i) = Pi
h=1 ϵ(h) be the writhe counted along the tangle from the initial arc 0 along the
tangle up until one reaches at the arc i. By Lemma B.1 we know that the coloring C ∈Colx
Q(T) lifts
to a unique coloring ˜C ∈Col(x,1)
˜Q
(T). Write ui = C(i) for i = 0, . . . , n. Thus we have ˜C(i) = (ui, gi)
for i = 0, . . . , n. By Lemma B.2, we have un = x. Assume inductively that gi = x−w(i) Qi
h=1 uϵ(h)
κ(h).
One computes using ∗= ∗1 and ¯∗= ∗−1:
18


## Page 19


˜C(i + 1)
=
(ui+1, gi+1)
=
(ui, gi) ∗ϵ(i+1) (uκ(i+1), gκ(i+1))
=
(ui+1, x−ϵ(i+1)giuϵ(i+1)
κ(i+1))
=
(ui+1, x−ϵ(i+1)x−w(i) (
iY
h=1
uϵ(h)
κ(h)) uϵ(i+1)
κ(i+1) )
=
(ui+1, gi+1).
Taking i = n we see that the Proposition holds.
Theorem B.4. In the notation above and let ¯C be the unique lifting of the coloring C ∈Colx
Q(T)
to Col1
GAlex(G′,fx)(T). Then ¯C(n) = L(C).
Remark B.5. Each element of SU(2) is a commutator ( [19] Prop. 10.24 ) so SU(2) is equal to
its own commutator subgroup. Since SO(3) is a simple group ( [1] ), and the center of SU(2) is
{1, −1} it follows that if x ̸= ±1 then the conjugacy class xSU(2) generates SU(2). Thus given any
x ∈SU(2) with x ̸= ±1 we may apply the results of Appendix A to (G, x) = (SU(2), x).
Acknowledgements
We thank Shin Satoh and Razvan Teodorescu for valuable comments. MS was partially supported
by NIH R01GM109459.
References
[1] Artin, E., Geometric Algebra, Wiley Classics Library Edition, 1988.
[2] Burde, B.; Zieschang, H., Knots, de Gruyter Studies in Mathematics, vol. 5, Walter de Gruyter
and Co. Berlin, 1985.
[3] Carter, J.S.; Jelsovsky, D.; Kamada, S.; Langford, L.; Saito, M., Quandle cohomology and
state-sum invariants of knotted curves and surfaces, Trans. Amer. Math. Soc., 355 (2003)
3947–3989.
[4] Carter, J.S.; Kamada, S.; Saito, M., Surfaces in 4-space, Encyclopaedia of Mathematical
Sciences, Vol. 142, Springer Verlag, 2004.
[5] Clark, W.E.; Dunning, L.A.; Saito, M., Quandle 2-cocycle knot invariants without explicit
2-cocycles, Journal of Knot Theory and Its Ramiﬁcations 26 (2017), no.7, 1750035, 22 pp.
[6] Clark, W.E., Maple Worksheets, http://shell.cas.usf.edu/~saito/SphericalQuandle/
Maple-Files-TopQ/
[7] Duistermatt, J.J.; Kolk, J.A.C., Lie Groups, Springer-Verlag, 2000.
[8] Eisermann, M., Quandle coverings and their galois correspondence, Fund. Math. 225 (2007)
103–167.
[9] Eisermann, M., Knot colouring polynomials, Paciﬁc J. Math., 231 (2007) 305–336.
19


## Page 20


[10] Eisermann, M., Homological characterization of the unknot, J. Pure Appl. Algebra, 177 (2003)
131–157.
[11] Heusener, M.; Klassen, E., Deformations of dihedral representations, Proc. Amer. Math. Soc.
123 (1997) 3039–3047.
[12] Inoue, A., On colorability of knots by rotations, torus knot and PL trochoid, Topology Appl.
183 (2015) 36–44.
[13] Joyce, D., A classifying invariant of knots, the knot quandle, J. Pure Appl. Alg., 23 (1983)
37–65.
[14] Kawauchi, A., A survey of knot theory, Birkhauser-Verlag, 1996.
[15] Klassen, E.P., Representations of Knot Groups in SU(2), Trans. Amer. Math. Soc., 326(2)
(1991) 795–828.
[16] Kuipers, J.B., Quaternions and Rotation Sequences, Princeton University Press, 1999.
[17] Matveev, S., Distributive groupoids in knot theory. (Russian) Mat. Sb. (N.S.) 119(161) (1982)
78–88 (160).
[18] Niebrzydowski, M., On colored quandle longitudes and its applications to tangle embeddings
and virtual knots, J. Knot Theory Ramiﬁcations, 15 (2006) 1049–1059.
[19] Porteous, I.R., Topological Geometry, Cambridge University Press, 2nd edition, 1969.
[20] Rubinsztein, R., Topological invariants and invariants of links, J. Knot Theory Ramiﬁcations,
16 (2007) 789–808.
20

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
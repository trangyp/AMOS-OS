---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1804.00886v3
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1804.00886v3_Bordered_Floer_Homology_and_a_Meridional_Class_of_Knot

> Source: 1804.00886v3_Bordered_Floer_Homology_and_a_Meridional_Class_of_Knot.pdf

> Pages: 42

---


## Page 1


Bordered Floer homology and a meridional class of
knot
Jaepil Lee
November 29, 2018
Abstract
For a knot K and its knot Floer complex CFK−(K), we introduce an algorithm
to compute the bordered Floer bimodule of the complement of the knot and its
meridian. The grading of the module computes spinc-summands of \
HFK(S3
−n(K), µK),
which can be also extended to arbitrary framing n.
1
Introduction
The classical Heegaard Floer homology package, introduced by Ozsv´ath and Szab´o [14],
provides a 3+1 dimensional topological quantum ﬁeld theory(TQFT) type invariants.
These invariants were proven to be equivalent to 3-dimensional Seiberg-Witten invari-
ants by Kutluhan, Lee, Taubes in [9] and its four sequels, thus leading breakthrough
in low-dimensional topology. The Heegaard Floer theory is also used to deﬁne knot
and link invariants [13, 15], and especially the knot Floer homology can be used to ﬁnd
the Heegaard Floer homology of three-manifold obtained by an integral surgery on a
knot [16].
The bordered Heegaard Floer homology was ﬁrst introduced by Lipshitz, Ozsv´ath, and
Thurston in [12], and this package deﬁnes an invariant for three-manifold with a single
boundary component. In particular, the boundary of three-manifold can be associated to
a diﬀerential graded algebra, and the three-manifold can be associated to a module called
a type-D module with the dg-algebra acting on the module. The torus boundary case
was extensively studied because it was directly related to the knot Floer homology. In
fact, the explicit algorithm has introduced in [12, Chapter 11], which enables to ﬁnd the
structure of a dg-module of the knot complement from the knot Floer complex CFK−.
This technique was useful not only for the computation of d
HF of a three-manifold of
arbitrary integral Dehn surgery; but also the computation of the knot concordance in-
variant τ of cable knots [7] and the concordance genus [8], and L-space classiﬁcation
problems [6]. There is a variant of this module named type-DD module, invented for a
1
arXiv:1804.00886v3  [math.GT]  28 Nov 2018


## Page 2


manifold with two boundary components, also by Lipshitz, Ozsv´ath and Thurston in [11].
On the other hand, the knot Floer homology on a knot embedded other than S3 has
drawn a particular interest. For a given knot K ⊂S3, the knot Floer homology of merid-
ian in integral Dehn surgery manifold S3
−n(K) for suﬃciently large integer n attracted
interests. In particular, Hedden studied the hat-version of knot Floer complex of merid-
ian in the Dehn surgery manifold [3, Theorem 4.1] to compute the knot Floer homology
of Whitehead double of a knot, and the inﬁnity-version is given in [4, Theorem 4.2].
Both results only works for suﬃciently large framing. Hedden, Kim, and Park recently
studied some small framing cases [5] as a part of the study on irreducible three-manifolds.
Inspired by these work, the main result of our paper enables the computation of the
type-D module of meridional class complement in S3
−n(K) from the knot Floer chain
complex CFK−. In what follows we shall outline the procedure to compute the type-
DD module of a link LK complement, where link L is comprised of a knot K ⊂S3 and
its meridian.
In order to describe the procedure, we will need to carefully choose sets of bases for
CFK−(K). In fact, we have a horizontally or vertically simpliﬁed basis of CFK−(K) [12,
Deﬁnition 11.23], such that the diﬀerential of every basis element is either zero or strictly
drops Alexander ﬁltration or U-ﬁltration. For either basis, we can deﬁne a horizontal
complex or a vertical complex; these complexes are obtained by disregarding vertical
arrows or horizontal arrows from CFK−(K), respectively. Then each complex has a
unique distinguished element, which is a generator of d
HF(S3). Then we have the fol-
lowing result.
Theorem 1. Let CFK−(K) be a model for a reduced chain complex for a knot K ⊂S3.
Then for a suﬃciently large integer n, the type-DD module of S3\LK with framing −n
can be derived from CFK−(K) by the following procedure.
Let {xk} be a vertically simpliﬁed basis with x0 being the distinguished element. For a
vertical arrow of length l from xj to xj+1, the diﬀerential between the associated elements
is
xj
0
ρ1σ3+ρ123σ123/ xj
∞
σ2
* xj
1
σ12 *
ρ23σ1
k
· · ·
σ12 *
ρ23
j
xj
l
σ1 ,
ρ23
j
xj+1
∞
ρ23σ2
j
xj+1
0
.
ρ1σ3+ρ123σ123
o
On the other hand, let {yk} be a horizontally simpliﬁed basis with y0 being the distin-
guished element. For a horizontal arrow of length l from yj to yj+1, the diﬀerential
between the associated elements is
yj
∞
yj
0
ρ1σ3+ρ123σ123
o
ρ3 + yj
−1
ρ23 *
ρ2σ12
j
· · ·
ρ23 +
σ12
k
yj
−l
ρ2 ,
σ12
j
yj+1
0
ρ3σ12
k
ρ1σ3+ρ123σ123/ yj+1
∞.
2


## Page 3


Lastly, the unstable chain between the two distinguished elements is as follows.
x0
∞
x0
0
ρ1σ3+ρ123σ123
o
ρ3
) γ1
ρ2σ12
j
ρ23 * · · ·
σ12
j
ρ23 * γm
σ12
j
ρ23σ1+ y0
∞
σ2
j
y0
0,
ρ1σ3+ρ123σ123
o
where m = n + 2τ(K).
It is crucial to mention that the same result can be achieved by Hanselman’s versatile
trimodule introduced in [1]. This trimodule is basically the bordered Floer invariant
of the 3-link complement, where the link has three unknot components U1, U2, U3 such
that lk(U1, U2) = lk(U2, U3) = 1 and lk(U1, U3) = 0. The derived tensor product with
the trimodule and knot complement (using the trick introduced in [6, Section 2.3] or [2,
Section 2.3]) will produce the quasi-isomorphic bimodule but a diﬀerent orientation and
labelling from the convention used in this paper. However, the method used in this
paper has the following advantage.
First, our bimodule is reduced; i.e., there is no
diﬀerential with algebra element 1. Second, the number of generators of the bimodule
obtained by the algorithm is almost one third of the number of generators of the bi-
module obtained from the trimodule; therefore the diﬀerential is less complicated. (The
bimodule obtained from the trimodule has more generators, even after reducing all dif-
ferentials of algebra element 1.) Third, the computation uses the pairing technique of
the bordered Floer theory in a much relaxed condition. Recall that the original pairing
theorem of [12] dealt with the pairing of two domains satisfying certain conditions on the
boundary chords [12, Chapter 3, Chapter 5]. However, the computation in this paper
shows how these conditions can be dropped for certain cases. Especially, the moduli
space of a boundary degeneration is paired with other domains, which was not used in
the pairing of the original bordered Floer package.
More importantly, having a simpliﬁed type-DD module also allows to sort the generators
of a bimodule, and it may recover the ﬁltration information of the knot Floer homology
of non-classical knots; i.e., a knot embedded in three-manifold other than S3. Taking
the derived tensor product with the above type-DD module and A∞-module associated
to the 0-surgery gives us the \
CFD of meridian complement in S3
−n(K). Since the type-
D module is equipped with a grading depending on spinc-structure, sorting the module
according to the grading reproves [3, Theorem 4.1]. Recall that the knot Floer homology
\
CFK(K) ∼= d
CF(S3) and is endowed with the Alexander ﬁltration F(K, m).
Theorem 2. Let K ⊂S3 be a knot with its meridian µK, and let n be a suﬃciently large
integer. Then, knot Floer homology \
HFK∗(S3
−n(K), µK) can be decomposed as follows.
\
HFK∗(S3
−n, µK) =
n
2 −1
M
m=−n
2
 
H∗
 d
CF(S3)
F(K, m)
!
⊕H∗
 
d
CF(S3)
F(K, −m −1)
!!
.
(Here we are implicitly assuming n is even; in the case n is odd, the summation should
be from −⌊n
2⌋to ⌊n
2⌋.)
3


## Page 4


Although the result was stated for an arbitrary large negative framing −n, the compu-
tation used in this paper can be easily generalized to any integral framing by taking a
derived tensor product with the type-DA module of the toroidal mapping class group
element τ±1 given in [11, Section 10.2]. Tensoring with this module increases/decreases
the framing by one, and eventually the type-D module of a meridian complement in
S3
−n(K) can be computed for any framing integer. Sorting out generators of the mod-
ule by spinc-structure grading will allow us to compute \
HFK(S3
n(K), µK) for arbitrary
integer n. In particular, if n = ±1, then S3
±1 is an integral homology sphere and µK is
null-homologous, so the Alexander grading A of the knot Floer complex is well-deﬁned.
Corollary 3. Let T be the left-handed trefoil knot.
The knot Floer chain complex
\
CFK(S3
−1(T), µT) consists of three generators x, y and z such that A(x) −A(y) =
A(y) −A(z) = 1.
The example calculation in Section 6 shows that it recovers not only the Alexander
ﬁltration of µT but also the U-ﬁltration of µT. Since the Kunnuth formula holds for the
knot connected sum, this can lead to the double ﬁltration information of a knot in the
Poincare sphere S3
−1(T) and general integral homology spheres as well.
Organization
In Section 2 we overview the bordered Floer package for the torus boundary and discuss
the algorithm to extract type-D module of a knot complement from the knot Floer
chain complex. Section 3 considers the doubly bordered Heegaard diagram of a knot
and its meridian complement, and Section 4 computes the moduli space of holomorphic
curves and proves Theorem 1. Section 5 computes the type-D module of a merdian
complement in S3
−n(K) and we see the collection of generators of the module with the
same spinc-grading is identical to the quotient of the knot Floer homology, thus proving
Theorem 2. In Section 6 we prove Corollary 3 with a model computation and discuss
how to recover the knot ﬁltration of a knot in an integral homology sphere.
Acknowledgement
The author would like to thank Kyungbae Park for the helpful discussion. Also thanks
to Robert Lipshitz for pointing out the relation between this work and Hanselman’s
trimodule [1]. Byungdo Park greatly helped revising the earlier version of this paper.
Lastly, I would like to thank my advisor, Olga Plamenevskaya.
4


## Page 5


2
A brief introduction of bordered Heegaard Floer
homology
In this section we quickly recall deﬁnitions and properties of bordered Floer homology
developed by Lipshitz, Ozsv´ath, and Thurston. A more comprehensive account of the
theory can be found in [12, 11].
A more accessible introduction can also be found
in [10]. We will merely list the essential part of their work which will be necessary for
our purpose.
2.1
Algebraic deﬁnitions
Let (A, d) be a unital diﬀerential algebra over F2 with the subalgebra of idempotents
I ⊂A. I has a basis {ıi}, such that ıi · ıj = δij and P ıi = 1 ∈A.
A (left) type-D structure over A is an F2-module N with left action of I and a map
δ1 : N →A ⊗I N
satisfying the relation
(µ ⊗idN) ◦(idA ⊗δ1) ◦δ1 + (d ⊗idN) ◦δ1 = 0,
where µ : A ⊗A →A is the multiplication of A.
The above relation lets the tensor product A ⊗I N be a diﬀerential graded A-module
endowed with a structure a · (b ⊗x) = ab ⊗x and ∂(a ⊗x) = a · δ1(x) + d(a) ⊗x. This
module is called a type-D module over A.
The map δ1 : N →A ⊗I N can be extended to
δk : N →A⊗k ⊗N
deﬁned by δk = (idA⊗k−1 ⊗δ1) ◦δk−1. If k = 0, we let δ0 := idN. The type-D structure
is called bounded if δk = 0 for suﬃciently large k.
An A∞-module over A, or type-A module is an F2-module M with a right action of I
and family of maps
mi+1 : M ⊗I A⊗i →M
5


## Page 6


satisfying the A∞relations
0
=
n
X
i=0
mn−i+1(mi+1(x ⊗a1 ⊗· · · ⊗ai) ⊗ai+1 ⊗· · · ⊗an)
+
n−1
X
i=1
mn(x ⊗a1 ⊗· · · ⊗ai−1 ⊗µ(ai, ai+1) ⊗ai+1 ⊗· · · ⊗an)
+
n
X
i=1
mi+1(x ⊗a1 ⊗· · · ⊗ai−1 ⊗d(ai) ⊗ai+1 ⊗· · · ⊗an).
and unital conditions
m2(x, 1)
=
x
mi(x, · · · , 1, · · · )
=
0,
i > 2.
If mk = 0 for suﬃciently large k, we say the A∞-module M is bounded. From now on,
every module in this paper will be assumed to be bounded.
We will also need type-A or type-D modules of multiple right or left actions. In this
paper we will focus on modules with two actions in the following sense. Let (A1, d1) and
(A2, d2) be unital diﬀerential algebras over F2, with subalgebra of idempotents I1 and
I2, respectively. A (left) type-DD structure over A is an F2-module N with left actions
of I1 and I2, equipped with a map
δ1 : N →(A1 ⊗A2) ⊗I1⊗I2 N
satisfying a similar relation, so that the tensor product (A1 ⊗A2) ⊗I1⊗I2 N becomes a
diﬀerential module. This module is called a type-DD bimodule over A1 ⊗A2. Likewise,
we say an F2-module M is a (right) A∞-bimodule over A1 ⊗A2 if M is equipped with
a right action of I1 ⊗I2 and family of maps
m1+i1+i2 : M
O
I1⊗I2
A⊗i1
1
⊗A⊗i2
2
→M
satisfying the similar relation of A∞-module. We remark that, for any given input, the
relation should satisfy the sum of all terms which have a composition of two of m, µ and
d equal to zero. and refer the reader to [11] for the explicit formulation of the relation.
In [11] authors also have deﬁned type-DA module, and the deﬁnition is similar to the
type-DD and type-AA modules. A further generalization to a multimodule is found
in [1].
2.2
Torus algebra
The bordered Floer homology package associates a boundary of a three-manifold to an
algebra called strands algebra. In particular, if the three-manifold has a torus boundary,
6


## Page 7


then the algebra is called a torus algebra, is written as A(T 2). The torus algebra is an
F2-module generated by
ı1, ı2, ρ1, ρ2, ρ3, ρ12, ρ23, ρ123.
ı1 and ı2 are the idempotents generating I, such that ı1 + ı2 = 1 is the identity. These
generators satisfy the following relations:
ı1ρ1 = ρ1ı2 = ρ1,
ı2ρ2 = ρ2ı1 = ρ2,
ı1ρ3 = ρ3ı2 = ρ3,
ı1ρ12 = ρ12ı1 = ρ12,
ı2ρ23 = ρ23ı2 = ρ23,
ı1ρ123 = ρ123ı2 = ρ123,
and
ρ1ρ2 = ρ12,
ρ2ρ3 = ρ23,
ρ1ρ23 = ρ12ρ3 = ρ123.
In general, a strands algebra has a nontrivial diﬀerential, but the torus algebra has van-
ishing diﬀerential.
Every strands algebra will hereafter refer to the torus algebra, thus A(T 2) will be ab-
breviated to A.
2.3
Bordered Heegaard diagram
A bordered Heegaard diagram for a three-manifold Y with ∂Y = T 2 is a tuple H =
(Σ, α, β, z) consisting of the following:
• a compact oriented surface Σ of genus g with a single boundary ∂Σ;
• α = {αc
1, · · · , αc
g−1, αa
1, αa
2}, where αc
i are pairwise disjoint circles in the interior of
Σ, and αa
i are disjoint arcs on Σ away from αc
i with endpoints on ∂Σ;
• a g-tuple of pairwise disjoint circles = {β1, · · · , βg} in the interior of Σ;
• a basepoint z on ∂Σ, away from (∂αa
1) ∪(∂αa
2).
We require every intersection between α-curve and β-curve to be transverse, and Σ\α
and Σ\β to be connected. From the diagram H, we get a three-manifold with boundary
by attaching a three-dimensional two-handle to Σ × I along the α- and β-circles. Then
the α-arcs have the parametrization of the torus boundary.
The torus algebra is given by the boundary of the diagram. The boundary ∂Σ has a
point z, and four other points of the ∂αa
1 and ∂αa
2. Then ∂Σ is an oriented circle, which
has three intervals that do not contain z. Label these intervals 1,2 and 3, respecting
the orientation of ∂Σ. A Reeb chord on ∂Σ that starts and end on the αa
i corresponds
to the algebra element ρI, where I ∈{1, 2, 3, 12, 23, 123} is determined by the intervals
travelled by the chord. If we regard the idempotents ıi as the sum of constant chords at
∂αa
i , then the multiplication rule can be regarded as a concatenation of chords.
7


## Page 8


2.4
Moduli spaces of curves
Let Σ be a bordered Heegaard surface without compactiﬁcation. Also let S(H) be the
set of unordered g-tuples x = {x1, · · · , xg} which contains exactly one point on each β-
curve and exactly one point on each α-curve, and at most one point on each α-arc. Then
we consider the J-holomorphic curves from Riemann surfaces with boundary punctures
to Σ × [0, 1] × R satisfying appropriate boundary conditions [12, Chapter 5]. Brieﬂy, let
J be an admissible almost complex structure on Σ × [0, 1] × R [12, Deﬁnition 5.1] such
that the projection map Σ × [0, 1] × R →Σ is holomorphic (Σ as a Riemann surface).
Then we discuss J-holomorphic curves
u : (S, ∂S) →(Σ × [0, 1] × R, (α × {1} × R) ∪(β × {1} × R)),
where S is a Riemann surface with boundary punctures.
There are three diﬀerent types of boundary punctures in ∂S; namely +, −and e. These
names are given by the asymptotic behavior of u near the punctures. Let t : Σ × [0, 1] ×
R →R be the projection. Then the t-coordinate at a boundary puncture p is asymptotic
to one of the following: +∞, −∞and some real number. Then p is called +, −and e
puncture, respectively. Observe that for a projection πΣ : Σ × [0, 1] × R →Σ,
• the image of a + or −puncture under πΣ is on the intersection between α- and
β- curves;
• the image of an e puncture under πΣ is a sequence of (ordered set of) Reeb chords
−→
ρ := (ρI1, · · · ρIk) on ∂Σ. (In fact, each ρIi ∈−→
ρ can be also a set of Reeb chords.
However, in this paper, ρIi is always considered as a singleton set of chord.)
In this sense, for x, y ∈S(H), if a curve u is asymptotic to points corresponding to
{x1, · · · , xg} = x at −puncture and asymptotic to points corresponding to {y1, · · · , yg} =
y at + puncture, then we say the curve u is connecting from x to y (possibly adjacent
to Reeb chords represented by −→
ρ ).
For x, y ∈S(H), let π2(x, y) denote the homology class of such curves that connects
x to y. For a homology class B ∈π2(x, y), f
MB(x, y) denotes the moduli space of
holomorphic curves in B. If B is adjacent to a sequence of Reeb chords −→
ρ , then we write
f
MB(x, y; −→
ρ ). Just as the standard Floer theory, there is an R-action on Σ × [0, 1] × R
by translation on the t-coordinate. Taking quotient of the action, the reduced moduli
space is written as
MB(x, y; −→
ρ ) := f
MB(x, y; −→
ρ )/R.
Discussing the expected dimension and modulo two count of a moduli space is usually
not easy; but in some cases they are well-understood just by studying the image of a
holomorphic curve under the projection πΣ : Σ × [0, 1] × R →Σ. A region of H is a
connected component of Σ\(α ∪β). A domain is a linear combination of regions with
8


## Page 9


integral coeﬃcient. Then under the projection Σ×[0, 1]×R →Σ, a curve of a homology
class B ∈π2(x, y) gives a domain D. In particular, if u is a holomorphic curve, then
the coeﬃcient of its domain must be nonnegative. The domain D may be adjacent to
∂Σ; in that case we have a nonempty sequence of Reeb chords −→
ρ .
A quadrilateral or rectangular domain will refer to the domain whose coeﬃcients are all
0 or 1, and the shape of regions with nonzero coeﬃcient is quadrilateral or rectangular.
Likewise, an annular domain is a domain with coeﬃcients that are all 0 and 1, and the
shape of the regions with nonzero coeﬃcients is an annulus. A provincial domain is a
domain that is not adjacent to the boundary. A periodic domain is a domain that does
not have a corner between α- and β- curves (but it may have a corner between α-curves
and ∂Σ). The space of periodic domain is denoted by π2(x, x).
For a homology class B ∈π2(x, y) and a sequence of Reeb chords −→
ρ , the expected di-
mension ind(B, −→
ρ ) of the moduli space f
MB(x, y; −→
ρ ) can be deduced from the following
formula in [12, Deﬁnition 5.61].
ind(B, −→
ρ ) = e(B) + nx(B) + ny(B) + |−
→
ρ | + ι(−→
ρ ).
The terms appearing in the above formula are explained below.
• e(B) is the Euler measure of the domain B. The Euler measure of a region is
deﬁned as its Euler characteristic minus 1/4 the number of its corners (intersections
between α-curves and β-curves, and α-curves and ∂Σ), and additive under union.
• Let x ∈S(H). nx is the sum of average multiplicity of four regions of each xi ∈x.
• |−
→
ρ | + ι(−→
ρ ) is quite complicated in general, but this quantity is simpliﬁed for the
torus algebra. Let −→
ρ = (ρI1, · · · , ρIk). Then the quantity is
1
2k +
X
s<t
L(ρIs, ρIt),
where L(ρIs, ρIt) equals
L(ρIs, ρIt) =
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
1/2
if (Is, It) = (1, 2), (2, 3), (12, 3), (1, 23)
−1/2
if (Is, It) = (2, 1), (3, 2), (3, 12), (23, 1)
1
if (Is, It) = (12, 23)
−1
if (Is, It) = (23, 12)
0
otherwise
We now deﬁne the type-D module \
CFD(H). Let X(H) be a F2-module spanned by
S(H), then
\
CFD(H) := A ⊗I X(H),
9


## Page 10


with a · (b ⊗x) := (a · b) ⊗x. Recall that the idempotent ıi ∈I is associated to the arc
αa
i . The idempotent action is deﬁned as
ıi · x :=
 x
if x is not occupying αa
i
0
if x is occupying αa
i .
If a source of holomorphic curve u having an e puncture, we need to consider the contri-
bution of the element of A to the diﬀerential of the type-D module. Thus, for a sequence
−→
ρ = (ρI1, · · · , ρIk), we let
a(−→
ρ ) := ρI1 · · · ρIk.
In other words, a(−→
ρ ) is merely a multiplication of all Reeb chords appearing in the
sequence −→
ρ . We also need to consider the case where the orientation of the boundary
being reversed from the induced orientation which we will write −−→
ρ := (ρI1, · · · , ρIk).
Here ρIi is the same Reeb chord as ρIi but with a reversed orientation regarded as a
chord in −∂Σ. For example, ρ1 = ρ3, ρ2 = ρ2, ρ3 = ρ1, ρ12 = ρ23 and so on.
The diﬀerential of \
CFD(H) is deﬁned by counting number of points of a reduced moduli
space whose multiplicity of the region containing z equals zero. Precisely,
∂(x) :=
X
y∈S(H)
X
B∈π2(x,y)
{−
→
ρ |ind(B,−
→
ρ )=1}
#MB(x, y; −→
ρ )a(−−→
ρ ) · y,
where the multiplicity of the domain of B at z equals zero.
Type-A module [
CFA(H) is deﬁned similarly. It is a F2-module with the same generating
set S(H) endowed with the idempotent action
x · ıi :=
 x
if x is occupying αa
i
0
if x is not occupying αa
i ,
We have a A∞-relation on [
CFA(H) such that
m(x, ρI1, · · · , ρIk) :=
X
y∈S(H)
X
B∈π2(x,y)
{−
→
ρ |ind(B,−
→
ρ )=1}
 #MB(x, y; −→
ρ )

y.
Again, the multiplicity of the domain of B at z equals zero.
Having two modules [
CFA(H1) and \
CFD(H2), the bordered Floer theory computes the
classical hat-version of the Heegaard Floer homology as follows. Let H1 ∪H2 be the the
boundary sum of two bordered Heegaard diagrams H1 and H2, such that α-arcs with
the same labellings are paired on the boundary of the diagrams. Then d
CF(H1 ∪H2) is
10


## Page 11


a chain complex generated by generators in [
CFA(H1) ⊗I \
CFD(H2), with diﬀerential
∂⊠deﬁned by
x ⊗y 7→
∞
X
k=0
(mk+1 ⊗id)(x ⊗δk(y)).
In fact, this chain complex is quasi-isomorphic to the Heegaard Floer complex of three-
manifold represented by Heegaard diagram H1 ∪H2 [12, Theorem 1.3]. This paring is
called the derived tensor product, and in general a derived tensor product of a type-A
module M and a type-D module N is denoted by (M ⊠N, ∂⊠).
In [11] bordered Heegaard package has been generalized to three-manifolds with two
boundaries. Each boundary can be associated to either type-A or type-D structures,
thus resulting in type-DD, DA and AA modules. The deﬁnitions are almost identical to
the single boundary case, except there exists two diﬀerent algebras called left and right
torus algebra (they are the same torus algebra with diﬀerent names) and they have the
same action as described above. See [11, Chapter 2].
2.5
Simpliﬁed bases for the knot Floer complex
This subsection provides a brief survey on the classical knot Floer homology. The de-
tailed explanation is found in [12, Chapter 11], but this subsection follows the concise
description in [7, Section 2]. The special basis of the knot Floer complex called simpliﬁed
basis. An advantage of the simpliﬁed basis is that it enables one to easily extract the
type-D module of a knot complement from the knot Floer chain complex.
Let HK := (Σ0, α0, β0, z, w) be the classical doubly pointed genus g Heegaard diagram
of a knot K in S3. Let SK be a set of g-tuples of intersection points between α and β
circles where each α and β circles are used exactly once. The chain complex CFK−(K)
is freely generated by the generator set SK over F2[U]. The diﬀerential is deﬁned as
∂x :=
X
y∈SK
X
φ∈π2(x,y)
ind(φ)=1
#M(φ)U nw(φ) · y.
This complex has a homological Z-grading, called the Maslov grading M, and a Z-
ﬁltration called the Alexander ﬁltration A. The relative Maslov grading and the Alexan-
der ﬁltration is deﬁned as follows:
M(x) −M(y) = ind(φ) −2nw(φ)
and
A(x) −A(y) = nz(φ) −nw(φ),
where φ ∈π2(x, y). Multiplication by U shifts the Maslov grading and the Alexander
ﬁltration as follows:
M(U · x) = M(x) −2
and
A(U · x) = A(x) −1.
11


## Page 12


As usual, we let \
CFK(K) := CFK−(K)/(U = 0). The Maslov grading is normalized
so that the generator of H∗(\
CFK(K)) ∼= d
HF(S3) ∼= F2 is supported in Maslov grading
zero. Alexander ﬁltration carries over to \
CFK(K) and conventionally the subgroup of
\
CFK(K) generated by Alexander ﬁltration less than equal to m will be denoted by
F(K, m).
The Alexander grading A is given as follows: The homology \
HFK(K) of \
CFK(K) has
a decomposition
\
HFK(K) =
M
s
\
HFK(K, s)
where s is the Alexander grading induced by the ﬁltration. Here we use the normalize
Alexander grading deﬁned by the following relation:
min{s|\
HFK(K, s) ̸= 0} = −max{s|\
HFK(K, s) ̸= 0}.
Finally, the complex CFK∞(K) := CFK−(K) ⊗F2[U] F2[U, U −1] is naturally a Z ⊗Z-
ﬁltered complex, with one ﬁltration given by the (−U)-exponent and the other by the
Alexander ﬁltration. Traditionally, each element of the complex CFK∞(K) is plotted
on the (i, j)-plane, where the i-th coordinate is the (−U)-exponent and the j-th coor-
dinate the Alexander grading; i.e., the element U i · x will be plotted at the coordinate
(−i, A(U i · x)). Thus the diﬀerential ∂of the complex is depicted as an arrow pointing
(non-strictly) downwards and to the left.
The complex of CFK∞(K) has a Z⊕Z-ﬁltration, and a subset S of Z⊕Z may be used to
describe a subcomplex of CFK∞(K). Let C(S) ⊂CFK∞(K) consists of points whose
(i, j)-coordinates are in S. Although not every C(S) is a subcomplex of CFK∞(K), but
for some appropriate S, C(S) may inherit the quotient complex structure. For instance,
C(i = 0) can be identiﬁed to \
CFK(K).
In [17], the smooth concordance invariant τ(K) is deﬁned as follows.
τ(K) := min{s | ı : C(i = 0, j ≤s) →C(i = 0) induces a nontrivial map on homology}
Although [12, Theorem 11.36] is originally stated in basis-free version, for our purpose
we choose a speciﬁc basis for CFK∞(K). Let Ch := C(j = 0) be a complex equipped
with a diﬀerential ∂h, which is called a horizontal complex. We view this complex as a
subquotient complex of CFK∞(K) consisting of elements with j-coordinates equal to
zero, with diﬀerential pointing towards (non-strictly) to the left. The horizontal com-
plex inherits the Z-ﬁltration from CFK∞(K) by (−U)-exponents. Likewise, we deﬁne
Cv := C(i = 0) equipped with a diﬀerential ∂v, called a vertical complex. The vertical
complex also inherits the Z-ﬁltration structure from CFK∞(K) by the Alexander ﬁl-
tration.
12


## Page 13


CFK∞(K) is called reduced if the diﬀerential ∂of CFK∞(K) strictly drops either the
Alexander ﬁltration or (−U)-exponents ﬁltration. It is known that every ﬁltered chain
complex is ﬁltered chain homotopic to a reduced complex.
Deﬁnition 2.1. A basis {xi} for a ﬁltered chain complex (C, ∂) is called a ﬁltered basis
if the set {xi |xi ∈CS} is a basis for a ﬁltered subcomplex CS ⊂C.
Now we are able to deﬁne two diﬀerent simpliﬁed bases for CFK∞(K).
Deﬁnition 2.2. A ﬁltered basis {xi} over F2[U] for the reduced complex CFK∞(K) is
vertically simpliﬁed if for each basis element xi, exactly one of the following holds:
• xi is in the image of ∂v and there exists a unique basis element xi−1 such that
∂vxi−1 = xi.
• xi is in the kernel, but not in the image of ∂v.
• xi is not in the kernel, and ∂vxi = xi+1.
If ∂vxi = xi+1, then we say that there is a vertical arrow from xi to xi+1 and the length
of the arrow is A(xi) −A(xi+1). Since H∗(Cv) ∼= F2, there is a distinguished element
that generates the homology. By reordering, we let x0 denote the element.
Let {xi} be a ﬁltered basis for the reduced complex CFK∞(K). Note that the set of
elements {U mi · xi}, where mi := A(xi), induces a basis for Ch.
Deﬁnition 2.3. A ﬁltered basis {xi} over F2[U] for the reduced complex CFK∞(K) is
horizontally simpliﬁed if each xi satisﬁes exactly one of the following:
• U mixi is in the image of ∂h and there exists a unique basis element xi−1 such that
∂hU mi−1xi−1 = U mixi.
• U mixi is in the kernel, but not in the image of ∂h.
• U mixi is not in the kernel of ∂h, and ∂hU mixi = U mi+1xi+1.
Again, if ∂hU mixi = U mi+1xi+1, we say there is a horizontal arrow from xi to xi+1,
and the length of the arrow is A(xi) −A(xi+1). Also we let x0 denote the element that
generates the homology H∗(Ch).
2.6
Bordered Heegaard diagram of the knot complement
For a doubly pointed Heegaard diagram HK = (Σ0, α0, β0, z, w) of a knot K, the bor-
dered Heegaard diagram H(n) of the knot K complement is obtained by attaching a
two-dimensional one-handle to Σ0 with one foot close to z and the other foot close to
w. Let Σ denote the resulting genus g surface and m be a meridional circle on Σ. Then
introduce a circle αg in the two-dimensional one-handle parallel to the meridian m of
13


## Page 14


αg
βg
α
λ
x0
x1
x2
x-1
x-2
x-3
1
0
2
3
Figure 1: The ﬁgure describes the winding region W. The top bold line is identiﬁed to
the bottom bold line so that it forms the two-dimensional one-handle. Our convention
is that the left-end of W is attached to the region of Σ0 near w and the right-end is
attached near z. The basepoint of the bordered Heegaard diagram is put on the region
labelled 0.
K, and a circle βg which transversely intersects αg once and disjoint from other β circles.
Let λ be a circle in Σ, being a circle in Σ a zero-framed longitude with respect to the
Seifert framing and intersecting αg once transversely and disjoint from other α circles.
Now for a tubular neighborhood W of αg in the two-dimensional one-handle, apply
the Dehn twist on λ along αg inside W n-times, as in Figure 1. Finally, puncture the
intersection of λ and αg, and label the four regions around the puncture 0, 1, 2, and 3 in
a counterclockwise direction so that the αg is dividing the regions 0, 1 and the regions
2, 3. On the punctured Σ, we let αa
1 := λ and αa
2 := αg. Thus we deﬁne the bordered
Heegaard diagram of the knot K complement to be
H(n) := (Σ, {αa
1, αa
2} ∪α0, {βg} ∪β0)
Inside W, the intersection point of αa
2 and βg will be called x0. Then we label the in-
tersection points of α2
1 and βg as follows. As travelling along the arc αa
1 in W between
the region 2 and 3, the intersections points of α2
1 and βg will be labelled x−1, x−2, · · ·
in order. Likewise, the intersection points on the opposite side of αa
2 will be labelled
x+1, x+2, · · · and so on. For simplicity, from now on we assume there are n + 1 intersec-
tion points in W labelled as x−n
2 , · · · , x+ n
2 . Recall that SK denote the set of generators
of \
CFK(HK). We let S(n) denote the set of generators of \
CFD(H(n)). Then for each
generator x ∈SK, there are n + 1 generators {xi} in S(n), where the generator xi
is obtained by adding the point xi ∈W to x. Note that for suﬃciently large n, most
generators in S(n) can be written xi for some x ∈SK. The generators in S(n) that
cannot be written in the form of xi for some x ∈SK are called exterior generators.
14


## Page 15


[12, Lemma 11.41] and [12, Lemma 11.43] assert that there is a function S : S(n) →1
2Z
satisfying the following:
• Let A : SK →Z be the (normalized) Alexander grading of elements in SK. Then
S(xk) = A(x) −k +
(n + 1) · sgn(k)
2

,
where sgn(k) = −1, 0, or 1 if k < 0, k = 0 or k > 0 respectively. In particular,
S(x0) = A(x).
• There exists a constant c satisfying the following: let y ∈S(n) with |S(y)| ≥c.
Then y is not an exterior generator, i.e, there exists x ∈SK such that y = xi for
some i ∈Z. Moreover, the sign of S(y) agrees with the sign of i.
2.7
Coeﬃcient maps and their domains
Let n be a suﬃciently large integer. [12, Theorem 11.36] gives the algorithm to compute
the homotopy type of \
CFD(H(n)) of knot complement with framing −n from the knot
Floer complex CFK−(K). Let {ξi} be a vertically simpliﬁed basis. Then we may regard
{ξi} to be a basis of ı1\
CFD(H(n)). For each arrow of length l from ξi to ξi+1, then we
have basis elements κi
1, · · · , κi
k ∈ı2\
CFD(H(n)) that form the following sequence:
ξi
ρ1 / κi
1
· · ·
ρ23
o
κi
k
ρ23
o
κi
k+1
ρ23
o
· · ·
ρ23
o
κi
l
ρ23
o
ξi+1.
ρ123
o
Similarly, let {ηi} be a set of horizontally simpliﬁed basis for CFK−(K). For an arrow
of length l from ηi to ηi+1, we also have basis elements λi
1, · · · , λi
k ∈ı2\
CFD(H(n)).
Again these form the following sequence:
ηi
ρ3 / λi
1
ρ23 / · · ·
ρ23 / λi
k
ρ23 / λi
k+1
ρ23
/ · · ·
ρ23 / λi
l
ρ2 / ηi+1.
Recall that there are two distinguished basis elements ξ0 and η0, which generate ho-
mologies H∗(Cv) and H∗(Ch) respectively. The unstable chain is a string of elements
µ1, · · · , µm ∈ı2\
CFD(H(n)) connecting ξ0 and η0 as follows:
ξ0
ρ1 / µ1
µ2
ρ23
o
· · ·
ρ23
o
µm
ρ23
o
η0,
ρ3
o
where m = n + 2τ(K).
Moreover, if the framing equals two times of the smooth concordance invariant τ(K),
then the unstable chain reduces to
ξ0
ρ12 / η0.
15


## Page 16


w
z
Σ
0
1
2
3
Figure 2: The top ﬁgure represents the bordered Heegaard surface Σ after attaching
the winding region. Six diagrams with shaded regions depict examples of domains used
in [12, Theorem 11.36]. These ﬁgures, beginning from the top right ﬁgure and in clock-
wise direction, represent type 1, type 2, type 3, type 4, type 5 and type 6 domains.
16


## Page 17


In the rest of this subsection, we will focus on the domains of the diagram H(n) that
contributes to the diﬀerentials δ1 of \
CFD(H(n)).
The coeﬃcient map DI : S(n) →S(n), indexed by an increasing sequence of consecutive
integers I = {i0, · · · , in} ⊂{1, 2, 3} (including the empty sequence ∅), satisﬁes the
following relation
δ1 = 1 ⊗D∅+
X
i
ρi ⊗Di +
X
{i,j|j=i+1}
ρij ⊗Dij + ρ123 ⊗D123.
The existence of a coeﬃcient map DI implies there is a domain in H(n) between the
associated elements adjacent to the boundary of H(n) labelled as I. In general, I can
be any interval in {0, 1, 2, 3} with respect to the cyclic ordering, including the empty in-
terval; e.g., I = 01 or 30 are possible. However, any coeﬃcient map of interval including
0 will not have contribution towards the diﬀerential δ1.
First, recall that for any generator x ∈SK corresponds to xk ∈\
CFD(H(n)), k =
−n
2, · · · , n
2.
Then the domains between these elements, whose modulo two count of
index one moduli space equals one, can be described as below.
· · ·
x−3
D23
o
x−2
D23
o
x−1
D23
o
x0
D3
o
D1 / x1
D01 / x2
D01 / x3
D01 / · · ·
From the above sequence, the domains associated to the coeﬃcient map DI, I = 3 and
23, will be called type 1 domains in this paper. The homology class of the domain of
the coeﬃcient map D23 : x−i →x−i−1, i ≥1, will be written as φi ∈π2(x−i, x−i−1),
and the homology class of the domain of the coeﬃcient map D3 : x0 →x−1 will also
be written as φ0 ∈π2(x0, x−1). Likewise, the homology classes of the domains of the
coeﬃcient map D1 : x0 →x1 and D01 : xi →xi+1 will be written as φ0 and φi, respec-
tively. In this paper, these two kinds of domains are called type 2 domains. See Figure 2.
There are coeﬃcient maps D23 : xi →xi−1, i ≥2. The domain of this map can be
understood as the entire surface Σ minus the domain of the homology class φi. The
homology class of this coeﬃcient map will be denoted by ψi. By taking advantage of the
symmetry of the diagram, there are coeﬃcient maps D01 : x−i →x−i+1, i ≥2. Again the
homology classes associated to these coeﬃcient maps are denoted by ψi, whose domains
can be graphically depicted as Σ minus the domain of the homology class φi−1. We will
call the domains of the homology classes ψi and ψi type 3 domains and type 4 domains,
respectively.
Lastly, there is a coeﬃcient map DI of the empty interval I = ∅. These maps appear
if there is a vertical or horizontal arrow between simpliﬁed bases. Suppose there is a
vertical arrow x →y of length l. Then we have a coeﬃcient map D∅: xi →yi−l,
i > l. To describe the domain, we need to consider the winding region W detached
17


## Page 18


0
1
x0
0
1
x0
x1
x2
x3
x4
x1
x2
x3
x4
Figure 3: We illustrate the domains of homology class ζ2 ∈eπ2(x2, x1) on the right, and
the domain of ζ4 ∗ζ3 ∗ζ2 on the left. Note that the shading of each region is darker as
the multiplicity of the region increases. The middle black dot in each diagram should
be attached near point z ∈Σ0.
from Σ. Then it is S2 minus two punctures, with each puncture previously attached to
the points z or w. Cutting open the winding region along the circle αg, we obtain two
annuli. For the annulus that contains the region labelled as 0 and 1, the interior of the
annulus has a part of βg and λ = αa
1, and its outer boundary is identiﬁed to αg. Then
the interior has intersection points x1, x2, · · · , and between them we have a homology
class ζi ∈eπ2(xi, xi−1) (thought as a homology class in the winding region, see Figure 3).
Consider the homology class ζi ∗ζi−1 ∗· · · ∗ζi−l+1. The domain of this homology class
has multiplicity l near the puncture. The gluing of this domain with the domain of the
homology class between x and y as in CFK−(K), which has multiplicity l near z as
well, gives the domain of the homology class ϕi ∈π2(xi, yi−l), i > l. (If i = l, there is
a coeﬃcient map D0 : xl →y0.) The domains of the homology classes ϕi, i ≥l will be
called type 5 domains. Likewise, the symmetry of the diagram will give coeﬃcient maps
D∅: x−i →y−i+l, i > l for a horizontal arrow x →y of length l. (Again, there is a
coeﬃcient map D2 : x−l →y0 if i = l.) The homology classes of these coeﬃcient maps
are written ϕi ∈π2(x−i, y−i+l), i ≥l. The domains of ϕi will be called type 6 domains.
Remark 2.4. The coeﬃcient map of the interval 123 only appears whenever there is a
horizontal arrow x →y of length one. In this case, the map is
D123 : x0 →y1.
[12, Figure 11.13] illustrates the type-D module \
CFD(H(n)) obtained by the domains
considered above. The complex is quite involved, but collapsing coeﬃcient maps D∅will
result in the simpliﬁed complex as stated in the beginning of this subsection.
18


## Page 19


2.8
Gradings
The bordered Floer package of torus algebra is also endowed with relative grading group
G. Here we describe the grading group of a single boundary case. Let G be generated
by triples (j; p, q), j, p, q ∈1
2Z. The multiplication is deﬁned as
(j1; p1, q1) · (j2; p2, q2) =

j1 + j2 +

p1
q1
p2
q2
 ; p1 + p2, q1 + q2

.
The distinguished central element (1; 0, 0) is written as λ.
For each element in the torus algebra A, the grading is given by the following rule. For
ρi, i = 1, 2, 3, we deﬁne the grading gr(ρi) ∈G as follows.
gr(ρ1)
=

−1
2; 1
2, −1
2

gr(ρ2)
=

−1
2; 1
2, 1
2

gr(ρ3)
=

−1
2; −1
2, 1
2

;
and we let the grading respects the multiplication so that gr(ρI · ρJ) = gr(ρI) · gr(ρJ).
For a Heegaard diagram H, suppose that there is a homology class B ∈π2(x, y), possibly
adjacent to the boundary ∂H. If so, the boundary adjacency can be written as c1 · ρ1 +
c2 · ρ2 + c3 · ρ3. Then the grading gr(B) of B is deﬁned as
gr(B) := (−e(B) −nx(B) −ny(B); c1 + c2 −c3
2
, −c1 + c2 + c3
2
).
Then we deﬁne gr(y) := gr(x)gr(B). Of course this grading is not well-deﬁned, but we
can remove the uncertainty of the grading by taking the grading set not on G, but on
G/P, where P := {gr(B)|B ∈π2(x, x)} is the subgroup of G. Under this setting, the
grading of type-D module \
CFD(H) is known to be
gr(∂x) = λ−1gr(x).
In terms of coeﬃcient map, DI : x →y enables to track the grading diﬀerence between
x and y; speciﬁcally,
λ−1gr(x) = gr(∂x) = gr(ρIy) = gr(ρI)gr(y)
and this leads to
gr(y) = λ−1gr(ρI)−1gr(x).
19


## Page 20


For (j; a, b) ∈G, j is called the Maslov component and (a, b) is called the spinc-
component.
Lastly, the grading set of [
CFA(H1) ⊠\
CFD(H2) is the double quotient group P1\G/P2,
where Pi is the subgroup of G generated by gradings of periodic domains in Hi.
3
Heegaard diagram of connected sum
Let L1 and L2 be two components of Hopf link L ⊂S3. For a knot K in S3, taking
connected sum of K and L1 will result in a 2-link LK consisting of the knot K and its
meridian L2.
The Heegaard diagram of a connected sum of two knots has been explained in [13, Section
7], and we will draw the doubly bordered Heegaard diagram of S3\ν(LK) by applying
the same procedure. First note the doubly bordered Heegaard diagram of the Hopf link
L complement in S3 is the same as the diagram of the identity bimodule as in [11, Figure
13]. See the top ﬁgure of Figure 4. The diagram will be written as ΣL. For convenience,
the two punctures of ΣL will be referred to the “left” and “right” punctures. ΣL has four
α-curves, namely eαa,L
1 , eαa,L
2 , eαa,R
1
, and eαa,L
2 . It also has two β-circles called eβ1 and eβ2,
and an arc ez connecting two punctures as well. Regard eαa,L
1
and eαa,R
1
as the longitudinal
curves of left and right knot components of L; thus eαa,L
2
and eαa,R
2
are the meridional ones.
We modify the diagram to get the doubly bordered Heegaard diagram of LK complement.
First, make a hole C on eαa,L
1
near the left puncture of the diagram ΣL. Then draw a curve
eαs whose ends are lying on ∂C, parallel to eαa,L
2 . Then the diagram has ﬁve intersection
points deﬁned as
a := eαa,L
2
∩eβ1,
b := eαa,R
1
∩eβ1,
c := eαa,L
1
∩eβ2,
d := eαa,R
2
∩eβ2,
as := eαs ∩eβ1.
Now, for a bordered Heegaard diagram {ΣK, αK, βK, zK} of a knot K complement (with
suﬃciently large negative framing), we identify the puncture of ΣK to C. Precisely, the
identiﬁcation is made so that
• the ends of meridional curve m ∈αK is connected to the ends of eαs, and the ends
of longitudinal curve λ ∈αK to the ends of eαa,L
1 ;
• the region of ΣK labelled as 2 is glued to the region of ΣL labelled as 2 adjacent
to the left puncture; and
• the region of ΣK labelled as 3 is glued to the region of ΣL labelled as 3 adjacent
to the left puncture.
Therefore, the region labelled as 1 is glued to the region of ΣL labelled as 2 adjacent to
the right puncture. The resulting diagram will be henceforth called Σ. Note that Σ has
20


## Page 21


two punctures, again called left and right punctures.
Then the resulting diagram has the following data that gives the doubly bordered Hee-
gaard diagram HLK(n) := {Σ, α, β, z} of link LK = K ` L2 complement, such that K
has framing −n and the meridian L2 has framing zero.
• The surface Σ with two boundary components ∂LΣ and ∂RΣ, which are the bound-
aries of left and right punctures, respectively.
• Let αa,L
1
be the curve obtained by connecting λ and eαa,L
1 , and αs be a circle obtained
by connecting eαs and m. The set of α-curves α is deﬁned as
α := (αK\{m, λ}) ∪{eαa,R
1
, eαa,R
2
, αa,L
1 , eαa,L
2 } ∪{αs}.
By rearranging indices, we let αa,R
1
:= eαa,R
1
, αa,R
2
:= eαa,R
2
, and αa,L
2
:= eαa,L
2 .
• The set of β-circles β carries over; i.e., β := βK ∪{eβ1, eβ2}.
Again, we write
β1 := eβ1 and β2 := eβ2 for notational simplicity.
• The arc z is the same as ez.
This diagram has two boundary components; the left (respectively, right) boundary al-
gebra is labelled ρI (respectively σI), where I = {1, 2, 3, 12, 23, 123}.
A reader may observe that for xk ∈S(n), we can associate generators of \
CFDD(HLK(n))
to xk, as described below.
• If k ̸= 0, xkasd is a tuple of intersection points between α and β consisting of in-
tersection points of xk and as, d. These generators belong to ı21 \
CFDD(HLK(n)).
• If k = 0, x0ad and x0 ⊗bc are tuples of intersection points consisting of x0
and a, d (respectively, b, c).
The generators x0ad ∈ı11 \
CFDD(HLK(n)) and
x0bc ∈ı22 \
CFDD(HLK(n)).
We have F2-vector space isomorphisms ı11M ∼= CFK−(K) and ı22M ∼= CFK−(K).
4
Holomorphic curves of domains obtained by glu-
ing
In this section, we compute the diﬀerential δ1 : M →AL ⊗AR ⊗M of the type-DD
module M := \
CFDD(HLK(n)).
The strategy of the computation is as follows: The bordered Heegaard surface Σ is
basically obtained by gluing two surfaces ΣK and ΣL. Every non-provincial domain of
21


## Page 22


x0
x-1
x-2
x1
x2
1
2 3
z
C
as
a
a
b
c
d
A
B
A
B
1
2 3
z
1
2
3
z
a
b
c
d
A
B
A
B
1
2 3
z
1
2
3
z
as
C
αa,L
1
~
αa,L
2
~
αa,L
1
~
αa,R
2
~
αs
~
β2
~
β1
~
λ3
λ2
λ1
λ0
R20
R30
R13
R02
R01
R00
Figure 4: The top ﬁgure is the doubly bordered Heegaard diagram ΣL of Hopf link
complement, by identifying two pairs of circles labelled A and B.
The labelling of
curves and intersection points are written as above. The two black dots represent the
left and right boundaries of Σ. The middle ﬁgure shows the modiﬁed diagram after
making a hole C and drawing a curve eαs. The bottom ﬁgure shows the region near C
of the resulting diagram after the modiﬁcation.
22


## Page 23


ΣK must be are glued to appropriate regions of ΣL minus the hole C. Note that there
are six of such regions in ΣL\C, and we will name them as below (see the middle of
Figure 4):
• R20, the region adjacent to the left boundary labelled 2;
• R30, the region adjacent to the left boundary labelled 3;
• R13, the region adjacent to the left boundary labelled 1 and the right boundary
labelled 3;
• R02, the region adjacent to the right boundary labelled 2;
• R01, the region adjacent to the right boundary labelled 1;
• R00, the region contains the arc z;
As explained above, all non-provincial domains of ΣK can be classiﬁed into six types,
and the domains of each type will be glued to one (or more) of the above regions listed.
The resulting domains will possibly contribute to the diﬀerential δ1, as long as the ex-
pected dimension equals one.
Type 1 domain. We investigate domains obtained by gluing type 1 domain of ΣK to
region in ΣL\C with Maslov index one. Let x ∈SK. Then there are following domains
to consider:
• The domain of φi ∈π2(x−i, x−i−1), i ≥1, glued to R20 + R30;
• The domain of φ0 ∈π2(x0, x−1) glued to R30.
The second domain listed above is rectangular, thus the holomorphic representative of
φ0 ∈π2(x0, x−1) results #M(x0ad, x−1asd; ρ3) = 1. So it remains to investigate the
ﬁrst domain.
Lemma 4.1. For x ∈SK, the moduli space M(x−iasd, x−i−1asd; (ρ2, ρ3)), i ≥1, has
modulo two count one.
Proof. We will apply the pairing theorem and use notations introduced in [12, Chapter
9]. Let us consider a domain of φi ∈π2(x−i, x−i−1), i ≥1, glued to R20 + R30. In this
proof, this domain will be called D. The domain D is divided by ∂C. We then have
two Reeb chords on ∂C ∩D, which will be labelled λ2 and λ3 so that λj is lying on
the region adjacent to ρi, j = 1, 2. See Figure 5 for the illustration. Recall that for the
holomorphic representative of φi ∈π2(x−i, x−i−1), i ≥1, the only valid interpretation
was M(x−i, x−i−1; (λ2, λ3)), which is basically a bigon [12, Lemma 11.46]. This implies
M(x−1, x−i−1; (λ2, λ3)) has a single curve u. Then the height diﬀerence between these
two chords is written as
evλ2,λ3 = evλ2(u) −evλ3(u),
23


## Page 24


ρ
x0
x-1
x-2
x-3
x-4
a
a
s
2
ρ3
λ2
λ3
R20
R30
Figure 5: The right ﬁgure shows the labelling of Lemma 4.1. The dashed line represents
∂C. The upper left part of ∂C will play a role of type-A and the bottom right part
type-D. The left ﬁgure implies that the domain D can be regarded as an annulus.
which is a ﬁxed real number, say t0.
On the other hand, let us consider the domains R20 and R30.
The relevant moduli
space M(as, as; R20 + R30), in order for the pairing theorem, has a pair of curves v1
and v2, where v1 is associated to the moduli space M(as, a; R20) and where v2 is to
M(a, as; R30). Then the moduli space of T-matched pairs is
^
MM(T; x−i, x−i−1; as, as) = f
M(x−i, x−i−1) ×T·ev1=ev2 f
M(as, as).
Then the moduli space
MM(T; x−i, x−i−1; as, as) := ^
MM(T; x−i, x−i−1; as, as)/R
consists of the curve u and a pair of disks from R20 and R30 with height diﬀerence T · t0.
The modulo two count of this moduli space is unchanged for the suﬃciently large T,
thus letting T →∞the height diﬀerence is going to ∞, so it proves the moduli space
of the ﬁbered product
M(x−ias, x−i−1as; (ρ2, ρ3))
has modulo two count one, as desired.
Remark 4.2. The domain D can be regarded as an annulus, whose inner boundary
consists of α-curves and a segment of β-curve on the winding region of the ΣK part
of the diagram. On the other hand, the outer boundary solely consists of α-curves.
However, when making a cut along β-curve from as, we obtain a holomorphic involution
of D interchanging the inner and outer boundaries of the annulus. This also proves
Lemma 4.1.
24


## Page 25


Type 2 domain. We study the following domains. For x ∈SK,
• the domains of φi ∈π2(xi, xi+1), i ≥1, glued to R01 + R02;
• the domain of φ0 ∈π2(x0, x1) glued to R02;
• the domain of φ0 ∈π2(x0, x1) glued to R02 + R13.
The second domain is rectangular, therefore we have #M(x0bc, x1asd; σ2) = 1. The
third domain could possibly contribute to the term ρ1σ23 · x1asd in δ1(x0ad), but the
idempotent rule does not allow this term to exist. Thus, we only need to study the ﬁrst
domain.
Lemma 4.3. For x ∈SK, the moduli space M(xiasd, xi+1asd; (σ1, σ2)), i ≥1, has
modulo two count one.
Proof. The proof of this lemma also follows the same trick that we have used in Lemma 4.1.
For a homology class φi ∈π2(xi, xi+1), the domain of φi glued to R01 + R02 will be de-
noted by D. Again, divide D along ∂C ∩D and we have two Reeb chords λ0 and λ1 on
∂C ∩D. See the illustration in Figure 6. Then the domain D is decomposed into
• the domain of φ, whose only valid interpretation is a bigon with moduli space
M(xi, xi+1; (λ0, λ1))
• the rectangular domain R01 with moduli space M(asd, bc; λ0)
• the rectangular domain R02 with moduli space M(bc, asd; λ1).
Again the same argument in Lemma 4.1 proves that the moduli space of the ﬁbered
product has a unique point.
Type 3 domain. The domains for consideration are
• the domain of ψi ∈π2(xi, xi−1), i ≥2, glued to R20 + R30
• the domain of ψ1 ∈π2(x1, x0), glued to R20 + R30 + R01
• the domain of ψ1 ∈π2(x1, x0), glued to R20 + R30 + R01 + R02
We will study the ﬁrst domains. First recall that #M(xi, xi−1; (λ2, λ3)) = 1, by [12,
Lemma 11.48].
Then by the same argument in Lemma 4.1, we can easily observe
#M(xiasd, xi−1asd; (ρ2, ρ3)) = 1 for i ≥2.
The second domain is dealt in the following Lemma.
Lemma 4.4. Let D be the domain obtained by gluing ψ2 ∈π2(x2, x1) and R20+R30+R01.
Then the moduli space M(x1asd, x0bc; (ρ2, ρ3, σ1)) of the domains has modulo two count
one.
25


## Page 26


x0
x2
x3
x4
x1
λ1
λ0
d
c
as
b
2
1
σ
σ
Figure 6: The domain of φi ∈π2(xi, xi+1) glued to R01 + R02. Again, the dashed line
represents a part of ∂C.
Proof. Cutting Σ along ∂C, we have two diagrams, ΣK and its complement. On ΣK,
we let eD denote a rectangular region that connects x0 and x1 adjacent to the chord λ1.
Consider ΣK\ eD. This domain has not been considered in the proof of [12, Theorem
11.36], since in their convention the domain contained the distinguished point z. How-
ever, by the parallel analysis in [12, Lemma 11.49], the only valid interpretation of this
domain is M(x1, x0; (λ2, λ3, λ0)) and its modulo two count is one. Then we glue the
domain ΣK\ eD to R20 + R30 + R01. The domains R20, R30 and R01 are all rectangular;
therefore we have three moduli spaces
M(asd, ad; R20),
M(ad, asd; R30),
and M(asd, bc; R01).
Each of these moduli spaces has a unique point, and by the same trick used in Lemma 4.1,
the claim is proved.
The last domain is a periodic domain, and the domain does not have an appropriate
interpretation of expected dimension one.
Type 4 domain. We will consider the following domains.
• the domain of ψi ∈π2(x−i, x−i+1), i ≥2, glued to R01 + R02
• the domain of ψ1 ∈π2(x−1, x0), glued to R20 + R01 + R02
• the domain of ψ1 ∈π2(x−1, x0), glued to +R13 + R20 + R01 + R02.
26


## Page 27


The ﬁrst domain has a moduli space M(x−iasd, x−i+1asd; σ1, σ2), and by the same con-
sideration of Lemma 4.3, its modulo two count is one. The second domain has a moduli
space M(x−1asd, x0ad; ρ2, σ1, σ2), and it has modulo two count is one again by the
same argument of Lemma 4.4. The last domain does not count due to the idempotent
restriction.
Type 5 domain. For x, y ∈SK, let us suppose there exists a domain B of the doubly
pointed Heegaard diagram HK from x to y, such that nz(B) = l nw(B) = 0. Then for
a homology class ϕi ∈π2(xi, yi−l), we consider the following domains.
• the domain of ϕi ∈π2(xi, yi−l), i > l
• the domain of ϕl ∈π2(xl, y0), glued to R01
• the domain of ϕl ∈π2(xl, y0), glued to R01+R02 and the domain of φ0 ∈π2(x0, x1)
• the domain of ϕl ∈π2(xl, y0), glued to R01 + R02 + R13 and the domain of φ0 ∈
π2(x0, x1)
The ﬁrst domain is the exactly same domain considered in [12, Lemma 11.48], so it con-
tributes to the coeﬃcient domain D∅: xiasd →xi−lasd. The second domain is divided
into the domain of ϕl and R01, and by the standard pairing argument of Lemma 4.1, it
results a moduli space M(x1asd, y0bc; σ1). The third domain is a valid domain only
when the length l of the arrow equals one, otherwise it would connect invalid generators.
We will study this domain in the following Lemma.
Lemma 4.5. If l = 1, then the moduli space M(x0bc, y0bc; σ12) has modulo two count
one.
Proof. We dualize the module M in order to take advantage of the A∞-relation. In
particular, the orientation of the boundary of Σ is reversed. We decompose the domain
into two: the domain of ϕl glued to R01, and the domain of φ0 glued to R02. Each
domain corresponds to the A∞-relation
m(x0bc, σ2) = x1asd,
m(x1asd, σ3) = y0bc.
(Here the algebra elements with overlines emphasize reversed orientation.)
The A∞
relation of type-AA module gives
0
=
m2(x0bc, σ2, σ3) = m(x1asd, σ3) + m(x0bc, σ23)
=
y0bc + m(x0bc, σ23).
Reversing σ23 will give σ12, which proves the claim.
However, the idempotent rule prohibits the above moduli space from contributing to δ1.
The fourth domain is studied in a similar manner.
27


## Page 28


Lemma 4.6. If l = 1, then M(x0ad, y0bc; ρ1, σ123) has modulo two count one.
Proof. Again, we dualize the module. Then there are following correspondences between
moduli spaces and A∞-relations.
• M(x0ad, x0bc; ρ1, σ3), obtained by the obvious rectangular domain in ΣL\C, cor-
responding to m(x0ad, ρ3, σ1) = x0bc
• M(x0bc, x1asd; σ2), corresponding to m(x0bc, σ2) = x1asd
• M(x1asd, y0bc; σ1), corresponding to m(x1asd, σ3) = y0bc
Through the combination of the above A∞-relation and by reversing the boundary ori-
entation, we prove the claim.
Type 6 domain. Similarly, for x, y ∈SK let us suppose there exists a domain B of
the doubly pointed Heegaard diagram HK from x to y such that nz(B) = 0 nw(B) = l.
Then we have homology classes ϕi ∈π2(x−i, y−i+l), i > l. Then these domains result
the following domains Σ by appropriate gluing.
• the domain of ϕi ∈π2(x−i, y−i+l), i > l
• the domain of ϕl ∈π2(xl, y0), glued to R20
• the domain of ϕl ∈π2(xl, y0), glued to R20+R30 and the domain of φ0 ∈π2(x0, x−1)
• the domain of ϕl ∈π2(xl, y0), glued to R20 + R30 + R13 and the domain of φ0 ∈
π2(x0, x−1)
The analysis of type 5 domains are similar to the type 5 domains, thus we only list the
moduli spaces of modulo two count one instead of repeating the same argument again.
• M(x−1asd, y−i+lasd), i > l
• M(xlasd, y0ad; ρ2)
• M(x0ad, y0bc; ρ123σ3), if l = 1
Other domains. There are two other domains that are not included in the discussion
above. The easier one is the domain R13, which is rectangular and has an moduli space
M(x0ad, x0bc; ρ1, σ3) of modulo two count one.
Then we turn to the domain that contributes to the algebra element ρ123σ123. Let D
be a domain of Σ which has multiplicity one on all regions but the domain contains the
arc z. Obviously the domain contributes to the diﬀerential from x0ad to x0bc for each
x ∈SK. The domain D has the following three interpretations.
• M(x0ad, x0bc; ρ123, σ1, σ2, σ3)
28


## Page 29


• M(x0ad, x0bc; ρ1, ρ2, ρ3, σ123)
• M(x0ad, x0bc; ρ1, ρ2, ρ3, σ1, σ2, σ3)
We claim that all of these moduli spaces have modulo two count one, and this proves
the existence of the term ρ123σ123x0bc in δ1x0asd.
The moduli spaces of the ﬁrst two domains can be dealt within the A∞-relation by the
dualizing technique. Explicitly, the combination of moduli spaces
M(x0ad, x−1asd; ρ1), M(x−1asd, x0ad; ρ2, σ3, σ2), M(x0ad, x0bc; ρ3, σ1)
(note that the ﬁrst one is considered in type 1 domain, the second in type 4 domains,
and the last one in the paragraph above) will result
#M(x0ad, x0bc; ρ123, σ1, σ2, σ3) = 1
modulo two. Similarly, the moduli space
M(x0ad, x0bc; ρ3, σ1), M(x0bc, x1asd; σ2), M(x1asd, x0bc; ρ2, ρ1, σ3)
(the second moduli space is considered in type 2 domain, and the last moduli space in
type 3 domain) will give us
#M(x0ad, x0bc; ρ1, ρ2, ρ3, σ123) = 1
modulo two.
Now, we turn to the moduli space M(x0ad, x0bc; ρ1, ρ2, ρ3, σ1, σ2, σ3). First, let us cut
open the domain D along the curve C. Then we get two components ΣK and B of D.
Recall that ΣK is the standard bordered Heegaard diagram of the knot K complement
with framing −n, thus B can be considered as a complement of ΣK in D. Considering
the domain B as a domain in the diagram ΣL (see Figure 4), we can again decompose
B into three smaller domains, say,
B1 := R13,
B2 := R20 + R02,
and
B3 := R30 + R01.
Each rectangular domain Bi can be associated to the following moduli spaces;
M(ad, bc; B1)
=
M(ad, bc; ρ1, σ3),
M(bc, ad; B2)
=
M(bc, ad; ρ2, σ2, λ12),
M(ad, bc; B3)
=
M(ad, bc; ρ3, σ1, λ30).
Then observe the domain B1 + B2 has a moduli space
M(bc, bc; B1 + B2) = M(bc, bc; ρ1, ρ2, σ2, σ3, λ12).
29


## Page 30


This moduli space can be interpreted as an annulus, whose outer boundary consists of
α and β curves and inner boundary consists of α curve only. By making a cut along eβ2
from c, it follows that the moduli space is transversely cut out and has an odd number
of points.
On the other hand, the domain ΣK cannot have any corner in its interior, and it can
be regarded as a boundary degeneration which was introduced in [12, Chapter 11]. By
the tautological correspondence, for a sequence −→λ = (λ12, λ30) we may consider a J-
holomorphic map
φ : H\{t1, t2} →Symg−1(ΣK).
where H be the upper half-plane, and φ is asymptotic to x at ∞and to a chord
λ12 at t1, λ30 at t2. Then by [12, Proposition 11.34], the moduli space M[ΣK](x; −→λ )
that contains φ is transversely cut out and have an odd number of points. Abusing
the notation, for a holomorphic curve (in cylindrical setting) φ ∈M[ΣK](x; −→λ ), the
height diﬀerence between two chords evλ12,λ30 is a positive real number t0.
Choose
representatives v1 ∈M(ad, bc; ρ3, σ1, λ30) and v2 ∈M(bc, bc; ρ1, ρ2, σ2, σ3, λ12), and
move these curves so that the diﬀerence of the R-coordinates of v1 and v2 is t0. By
the standard pairing theorem argument with the time dilation, we can conclude that
M(x0ad, x0bc; ρ1, ρ2, ρ3, σ1, σ2, σ3) also has modulo two count one.
We close this section by summarizing the discussion so far, in terms of the simpliﬁed
bases. For aesthetic reasons we write x0 := x0ad, xi := xiasd for i ̸= 0, and x∞:= x0bc.
The length of the unstable chain is deduced completely analogous to the [12, Theorem
11.26].
Proposition 4.7. Let CFK−(K) be a model for a reduced chain complex for a knot K ⊂
S3. Then for suﬃciently large interger n, the type-DD module M = \
CFDD(HLK(n))
can be derived from CFK−(K) by the following procedure.
For each x ∈CFK−(K), we have the following elements:
• x0 ∈ı11M and x∞∈ı22M
• xi ∈ı21M, i = −n/2, · · · , −1, 1, · · · , n/2.
• The diﬀerential between these elements is
· · ·
σ12 + x−2
σ12 +
ρ23
j
x−1
ρ2σ12 *
ρ23
k
x0
ρ1σ3+ρ123σ123/
ρ3
k
x∞
σ2 * x1
σ12 *
ρ23σ1
k
x2
σ12 *
ρ23
j
· · ·
ρ23
j
Let {xk} be a vertically simpliﬁed basis with x0 being the distinguished element. For the
vertical arrow of length l from xj to xj+1, the diﬀerential between the associated elements
30


## Page 31


is
xj
0
ρ1σ3+ρ123σ123/ xj
∞
σ2
* xj
1
σ12
*
ρ23σ1
k
· · ·
σ12
*
ρ23
j
xj
l
σ12 +
ρ23
j
σ1

xj
l+1
σ12
*
ρ23
j
1

· · ·
ρ23
l
xj+1
0
ρ1σ3+ρ123σ123 / xj+1
∞
σ2 , xj+1
1
σ12 ,
ρ23σ1
l
· · · .
ρ23
l
In particular, if l = 1, then there exists an additional diﬀerential xj
0
ρ1σ123/ xj+1
∞
.
On the other hand, let {yk} be a horizontally simpliﬁed basis with y0 being the distin-
guished element. For the horizontal arrow of length l from yj to yj+1, the diﬀerential
between the associated elements is
yj
∞
yj
0
ρ1σ3+ρ123σ123
o
ρ3 + yj
−1
ρ23
*
ρ2σ12
j
· · ·
ρ23 +
σ12
k
yj
−l
ρ23 ,
σ12
j
ρ2

yj
−l−1
ρ23
+
σ12
k
1

· · ·
σ12
l
yj+1
∞
yj+1
0
ρ1σ3+ρ123σ123
o
ρ3
, yj+1
−1
ρ23
,
ρ2σ12
l
· · · .
σ12
l
In particular, if l = 1, then there exists an additional diﬀerential yj
0
ρ123σ3/ yj+1
∞
.
Lastly, the unstable chain between the two distinguished elements is as follows.
x0
∞
x0
0
ρ1σ3+ρ123σ123
o
ρ3
) γ1
ρ2σ12
j
ρ23 * · · ·
σ12
j
ρ23 * γm
σ12
j
ρ23σ1+ y0
∞
σ2
j
y0
0,
ρ1σ3+ρ123σ123
o
where γi ∈ı21M, and m = n + 2τ(K).
Proof of Theorem 1. It remains to ﬁnd the homotopy equivalent model without the al-
gebra element 1 of chains introduced in Proposition 4.7. The undesirable cancelling pairs
can easily be removed by the tricks used in the proof of [12, Theorem 11.26]. Thus, the
chain
xj
0
ρ1σ3+ρ123σ123/ xj
∞
σ2
* xj
1
σ12
*
ρ23σ1
k
· · ·
σ12
*
ρ23
j
xj
l
σ12 +
ρ23
j
σ1

xj
l+1
σ12
*
ρ23
j
1

· · ·
ρ23
l
xj+1
0
ρ1σ3+ρ123σ123 / xj+1
∞
σ2 , xj+1
1
σ12 ,
ρ23σ1
l
· · · .
ρ23
l
is homotopy equivalent to
xj
0
ρ1σ3+ρ123σ123/ xj
∞
σ2
* xj
1
σ12 *
ρ23σ1
k
· · ·
σ12 *
ρ23
j
xj
l
σ1 ,
ρ23
j
xj+1
∞
ρ23σ2
j
xj+1
0
,
ρ1σ3+ρ123σ123
o
31


## Page 32


and the chain
yj
∞
yj
0
ρ1σ3+ρ123σ123
o
ρ3 + yj
−1
ρ23
*
ρ2σ12
j
· · ·
ρ23 +
σ12
k
yj
−l
ρ23 ,
σ12
j
ρ2

yj
−l−1
ρ23
+
σ12
k
1

· · ·
σ12
l
yj+1
∞
yj+1
0
ρ1σ3+ρ123σ123
o
ρ3
, yj+1
−1
ρ23
,
ρ2σ12
l
· · · .
σ12
l
is homotopy equivalent to
yj
∞
yj
0
ρ1σ3+ρ123σ123
o
ρ3 + yj
−1
ρ23 *
ρ2σ12
j
· · ·
ρ23 +
σ12
k
yj
−l
ρ2 ,
σ12
j
yj+1
0
ρ3σ12
k
ρ1σ3+ρ123σ123/ yj+1
∞.
These reductions both hold even if the length of the horizontal or vertical arrow l equals
one, again by the similar trick. For example, if a horizontal arrow has length one, replace
yj
−1 by eyj
−1 := yj
−1 + ρ23 · yj
∞. The statement on the unstable chain carries over from
Proposition 4.7, thus proving the claim.
5
Grading of the meridian complement
For a suﬃciently large positive integer n, the type-D structure of the meridian com-
plement in the integral Dehn surgery manifold S3
−n(K) is easily obtained by taking the
0-surgery on the left boundary component. The associated type-A module [
CFA(H0) of
the 0-surgery has a single generator t satisfying the following structure.
mk+1(t, ρ2, ρ12, · · · , ρ12, ρ1) = t.
Obviously t cannot be tensored with generators in ı11 \
CFDD(HLK(n)). The derived
tensor product of the 0-surgery type-A module with
\
CFDD(HLK(n)) is a straight-
forward computation, so we merely state the result in the following proposition. We
omitted tensor with t from the statement for cosmetic reasons.
Proposition 5.1. Under the same assumption in Theorem 1, the type-D module \
CFD(S3
−n(K)\µK)
can be derived from CFK−(K) by the following procedure.
Let {xk} be a vertically simpliﬁed basis. For a vertical arrow of length l from xj to xj+1,
the diﬀerential between the associated elements is
xj
∞
σ2
/ xj
1
σ12 / · · ·
σ12 / xj
l
σ1 / xj+1
∞.
Let {yk} be a horizontally simpliﬁed basis. For a horizontal arrow of length l from yj to
yj+1, the diﬀerential between the associated elements is
yj
∞
yj
−1
σ123
o
· · ·
σ12
o
yj
−l
σ3 /
σ12
o
yj+1
∞.
32


## Page 33


x
y
o

...
σ12

...
σ12

1
}
z
x−2
ρ23
O
σ12

y−2
ρ23
O
σ12
 1
|
x−1
ρ23
O
ρ2σ12

y−1
ρ23
O
ρ2σ12

ρ2
{
x0
ρ3
O
ρ1σ3+ρ123σ123
|
y0
ρ3
O
ρ1σ3+ρ123σ123
"
ρ123σ3
o
ρ1σ123

x∞
σ2
}
y∞
σ2
!
· · ·
ρ23
"x2
σ12
o
ρ23
"x1
σ12
o
ρ23σ1
2
y1
σ12 /
ρ23σ1
l
σ1

y2
σ12 /
ρ23
}
1
}
· · ·
ρ23
|
1
}
z1
σ12 /
ρ23σ1
r
z2
σ12 /
ρ23
d
· · ·
ρ23
d
z∞
σ2
=
z0
ρ1σ3+ρ123σ123
<
ρ3
z−1
ρ23

ρ2σ12
C
z−2
ρ23

σ12
D
...
σ12
D
Figure 7: The diagram describes the type-DD module structure of
\
CFDD(HLK(n))
obtained directly from Proposition 4.7, where K is the right-handed trefoil knot. The
standard model of CFK−(K) that is used to derive this module is drawn on the top left
corner. The elements of the unstable chain are zi, i < 0, and xj, j > 0.
33


## Page 34


x0
ρ1σ3+ρ123σ123
|
ρ3σ12
"y−1
ρ2σ12
"
ρ2
o
y0
ρ3
o
ρ1σ3+ρ123σ123
!
x∞
σ2

y∞
σ2

z−m
σ12

ρ23σ1
O
y1
σ1

ρ23σ1
[
...
ρ23
O
z∞
ρ23σ2
Z
· · ·
σ12
8 z−1
ρ2σ12
:
ρ23
o
z0
ρ3
o
ρ1σ3+ρ123σ123
?
Figure 8: A diagram obtained after removing all of the algebra element 1 from Figure 7.
The unstable chain between the two distinguished elements is as follows.
x0
∞
γ1
σ123
o
· · ·
σ12
o
γm
σ12
o
y0
∞,
σ2
o
where m = n + 2τ(K).
For simplicity, we will assume that n is an even integer without loss of generality.
We often regard the complex CFK−(K) as a directed graph on a plane with vertices on
integral lattice, such that every arrow is pointing either left or downward (disregarding
diagonal arrows as in the standard bordered Floer theory). Viewing the type-D module
as a directed graph would help understand the structure of a meridional knot in the Dehn
surgery manifold, just like the classical knot Floer complex. In case CFK−(K) has a
horizontally and vertically simpliﬁed basis, we will view \
CFD(S3
−n(K)\µK) as a directed
graph on (q, r)-plane such that each arrow is labelled as σI, I ∈{1, 2, 3, 12, 23, 123}. We
let the coordinates of generators on the plane obey the following rule.
• The coordinates of generators in 2\
CFD(S3
−n(K)\µK) are determined as follows.
Since there is a one-to-one correspondence between CFK−(K) and 2\
CFD(S3
−n(K)\µK)
(the ∞-labelled generators), put x∞so that the (q, r)-coordinates of x∞and the
corresponding x ∈CFK−(K) agree.
• Suppose xj, xj+1 ∈CFK−(K) have coordinates (q, r) and (q, r −l) and have a
vertical arrow of length l between them, then
– put xj
1 on (q, r −1
2);
34


## Page 35


– put xj
m so that xj
m−1 and xj
m have the same q-coordinates but r-coordinate
of xj
m is one less than that of xj
m−1.
• Suppose yj, yj+1 ∈CFK−(K) have coordinates (q, r) and (q −l, r) and have a
horizontal arrow of length l between them, then
– put yj
−1 on (q −1
2, r);
– put yj
−m so that yj
−(m−1) and yj
−m have the same r-coordinates but q-coordinate
of yj
−m is one less than that of yj
−(m−1).
• Recall that there are two distinguished elements x0 and y0, which generate homolo-
gies H∗(Ch) and H∗(Cv) respectively. If the distinguished element x0 ∈CFK−(K)
is on (q0, r0), then let the (q, r)-coordinates of γµ, µ ≤1
2m be (q0 −1
2 −(µ −1), r0).
Similarly, if the distinguished element y0 ∈CFK−(K) is on (r0, q0), then let the
(q, r)-coordinates of γµ, µ > 1
2m be (r0, q0 −1
2 −(m −µ)).
See Figure 9 for some examples.
Recall that the type-A module [
CFA(H∞) associated to the ∞-surgery is generated by
a single generator u with the relation
mk+1(u, σ3, σ23, · · · , σ23, σ2) = u.
The derived tensor product of [
CFA(H∞) with \
CFD(S3
−n(K)\µK) will be graded by
P1\G/P2, where P1 and P2 are subgroups of G generated by gradings of the periodic
domains of Heegaard diagrams of \
CFD(S3
−n(K)\µK) and [
CFA(H∞) respectively. More
precisely, P1 is spanned by (v; −n, −1) for some v and P2 is spanned by ( 3
2; 0, 1). We will
be focusing on the spinc-component of the grading, and the quotient by the action of
the Maslov component of this double-coset space will be denoted by eG := (P1\G/P2)/Z.
We have the following decomposition
[
CFA(H∞) ⊠\
CFD(S3
−n(K)\µK)
∼= \
HFK∗(S3
n(K), µK) =
M
sk∈Spinc(S3
−n(K))
\
HFK∗(S3
n(K), µK, sk).
Then, generators in [
CFA(H∞) ⊠\
CFD(S3
−n(K)\µK) that share the same grading in eG
belong to the same spinc-summand.
Note that the generators in [
CFA(H∞)⊠\
CFD(S3
−n(K)\µK) have a bijective correspon-
dence to the generators in 1\
CFD(S3
−n(K)\µK). In the following Lemma, we blur the
diﬀerence between these spaces.
35


## Page 36


Figure 9: From top to bottom, the ﬁgures on the left column are the knot Floer complexes
of the right-handed trefoil, left-handed (3,4)-torus knot, and the ﬁgure-eight knot. The
ﬁgures on the right column illustrate the type-D module of the meridian complement in
the Dehn surgery manifold; the black dots represent generators in 2-idempotent and the
white dots represent 1-idempotent. Each arrow is implicitly labelled with σI according
to Proposition 5.1. The unstable chain is colored in red.
36


## Page 37


Lemma 5.2. Consider \
CFD(S3
−n(K)\µK) as a directed, σI-labelled graph on (q, r)-
plane. Then for any integer k, the generators in 1\
CFD(S3
−n(K)\µK) that lie on the
line −q + r = k + 1
2 have the same grading in eG.
Proof. Suppose that generators a, b ∈\
CFD(S3
−n(K)\µK) are connected by a directed
edge a
σI
/ b . For simplicity, let egr(a) = (0, 0). Then the egr(b) is,
egr(b) =















(−1/2, 1/2)
if I = 1
(−1/2, −1/2)
if I = 2
(1/2, −1/2)
if I = 3
(−1, 0)
if I = 12
(0, −1)
if I = 23
(−1/2, −1/2)
if I = 123
To prove the claim, it suﬃces to keep track of the grading changes in the horizontal
and vertical sequences. If yj, yj+1 ∈CFK−(K) have a horizontal arrow of length l
yj+1
yj
o
, then the corresponding sequence in \
CFD(S3
−n(K)\µK) is
yj+1
∞
yj
−l
σ3
o
σ12 / yj
−l+1
σ12
/ · · ·
σ12 / yj
−1
σ123 / yj
∞
and it is clear that the ﬁrst factors of the eG-grading of 1-idempotent generators are
‘increasing’ by one from right to left. By similar observation, the ﬁrst factors of the eG-
grading of 1-idempotent generators in a vertical sequence are ’decreasing’ by one from
top to bottom.
The proof can be completed by considering the following four cases.
• A vertical sequence follows a horizontal sequence
• A horizontal sequence follows a vertical sequence
• A horizontal and a vertical sequence start at a generator
• A horizontal and a vertical sequence end at a generator
The ﬁgure below illustrates the respective corresponding sequence in the type-D module
37


## Page 38


\
CFD(S3
−n(K)\µK).
•
σ2

a
σ3
o
σ12 / · · ·
...
σ12

b
σ12

d
σ1

...
· · ·
σ12
/ c
σ123 / •
· · ·
σ12
/ e
σ123 / •
σ2

...
σ12

f
σ12

g
σ1

...
•
h
σ3
o
σ12 / · · ·
The G-grading diﬀerence between a and b is ±(0, 1) ∈P2, thus they are in the same
eG-grading. Likewise c and d have the same eG-grading, too. The eG-grading diﬀerence
between e and f (and g and h) are precisely (1, 0). This completes the proof.
Theorem 5.3. Let k ∈Z. Viewing \
CFD(S3
−n(K)\µK) as a graph on (q, r)-plane, the
vector space generated by vertices on the line Lk := {(q, r)|−q+r = k+ 1
2} is isomorphic
to
H∗
 d
CF(S3)
F(K, k)
!
⊕H∗
 
d
CF(S3)
F(K, −k −1)
!
.
Proof. The line Lk can intersect with horizontal or vertical sequences; if Lk intersects
with the vertical sequence, then this implies there is a 2-idempotent generator yj
∞
endowed with the sequence
yj
∞
σ2
/ yj
1
σ12 / yj
2
σ12 / · · · .
Recall that we have a bijective correspondence between generators in CFK−(K) and
2\
CFD(S3
−n(K)\µK). If the corresponding element yj ∈CFK−(K) of yj
∞is not the
distinguished element in the vertical complex, then there should be yj+1 ∈CFK−(K)
with ∂v(yj) = yj+1. Observe that the Alexander ﬁltration of yj is greater than k and
yj+1 is less than or equal to k. Thus, the existence of the intersection of Lk and the
vertical sequence imply yj ∈H∗(d
CF(S3)/F(K, k). If yj is the distinguished element in
the vertical complex, i.e., j = 0, then the Alexander ﬁltration level of y0 is again greater
than k and y0 ∈H∗(d
CF(S3)/F(K, k).
38


## Page 39


L0
L-1
Figure 10: The ﬁgure illustrates the type-D module of the meridian complement in large
integral surgery manifold along the right-handed trefoil. An intersection with Lk and the
horizontal sequence of the graph (blue dot) corresponds to a generator in the quotient
complex Ch/F(K, −k −1) (on the bottom left line, dots on the right of the dashed line
Lk). Also, an intersection point in the vertical sequence (yellow dot) corresponds to a
generator in Cv/F(K, k) (on the top right line, dots above the dashed line Lk).
Similarly, the existence of the intersection of Lk and the horizontal sequence starting at
xj
∞imply xj ∈CFK−(K) has the Alexander ﬁltration greater than −k −1 and ∂h(xj)
has a ﬁltration level less than or equal to −k −1.
Proof of Theorem 2. It remains to ﬁnd k values that admit nonempty intersections be-
tween the graph and line Lk. Let x0 and y0 be the distinguished generators that generate
H∗(Ch) and H∗(Cv) respectively. Observe that if x0 lies on (q0, r0), then y0 is on (r0, q0)
and τ(K) = q0 −r0. The generators of the unstable sequence, which have been hori-
zontally placed, end at (q0 −1
2m + 1
2, r0); and the vertical unstable sequence generators
end at (r0, q0 −1
2m + 1
2). Since m = n + 2τ(K), this implies the line Lk has a nonempty
intersection if −1
2n ≤k ≤1
2n −1.
6
Example: Poincare sphere and meridional class
Recall that an integral homology sphere is obtained by a (sequence of) knot with surgery
coeﬃcient ±1. Hence, we ﬁrst need to extend Theorem 1 to arbitrary framing.
Proposition 6.1. Let CFK−(K) be a reduced chain complex of a knot K in S3. For an
arbitrary integer n, the type-DD module of S3\LK with framing n can be derived from
39


## Page 40


the algorithm in Theorem 1 except for the unstable chain. The unstable chain has the
following structure, depending on the framing n.
• If n < 2τ(K)
x0
∞
x0
0
ρ1σ3+ρ123σ123
o
ρ3
) γ1
ρ2σ12
j
ρ23 * · · ·
σ12
j
ρ23 * γm
σ12
j
ρ23σ1+ y0
∞
σ2
j
y0
0,
ρ1σ3+ρ123σ123
o
where m = 2τ(K) −n.
• If n = 2τ(K)
x0
∞
x0
0
ρ1σ3+ρ123σ123
o
ρ3σ1 + y0
∞
ρ2σ2
j
y0
0.
ρ1σ3+ρ123σ123
o
• If n > 2τ(K)
x0
∞
x0
0
ρ1σ3+ρ123σ123
o
ρ3σ12 ) γ1
ρ2
j
σ12 * · · ·
ρ23
j
σ12 * γm
ρ23
j
σ1 + y0
∞
ρ23σ2
j
y0
0,
ρ1σ3+ρ123σ123
o
where m = n −2τ(K).
Proof. The statement is easily proved by taking the derived tensor product of the un-
stable chain of a suﬃciently large negative framing parameter with the type-DA module
associated to τ+1 [12, Figure A.3].
Recall that the Poincare sphere can be obtained by the Dehn surgery of the left-handed
trefoil T with the framing parameter −1. In order to obtain the type-D module of
the meridian complement in the Poincare sphere, ﬁrst we need to have the type-DD
module of T and its meridian complement with the framing parameter n = −1 (note
that τ(T) = −1). Its structure is written below.
z0
ρ1σ3+ρ123σ123
}
ρ3σ12

z∞
σ2

γ1
ρ2
_
σ1

z1
σ1

ρ23σ1
C
x∞
ρ23σ2
C
y∞
ρ23σ2
P
x0
ρ1σ3+ρ123σ123
a
ρ3σ12
8 y−1
ρ2
o
ρ2σ12
: y0
ρ3
o
ρ1σ3+ρ123σ123
=
40


## Page 41


Taking the type-A module [
CFA(H0) of zero surgery produces the type-D module of the
meridian complement in the Poincare sphere as follows.
z∞
σ2

γ1
σ3
o
σ1

z1
σ1
x∞
y−1
σ3
o
σ123 / y∞
Due to the bijection between generators of \
CFK(S3
−1(T), µT) and 2\
CFD(S3
−1(T)\µT),
we can assume γ1, z1 and y1 generate \
CFK(S3
−1(T), µT). On the other hand, the type-D
module of µT complement in S3
−1(T) can be computed from the doubly pointed Heegaard
diagram representing µT in S3
−1(T) by attaching the winding region near the two points
z and w. Recall that the grading is a homotopy invariance and is independent from the
choice of the bordered Heegaard diagram. Then, it is clear that the sequence
z1
z∞
σ2
o
γ1
σ3
o
exists only when there is a domain connecting from γ1 to z1 with nw = 1. Likewise, the
sequence
γ1
σ1 / y∞
y−1
σ123
o
exists only when there is a domain connecting from γ1 to y−1 with nz = 1. This proves
Corollary 3.
References
[1] Jonathan Hanselman. Bordered Heegaard Floer homology an graph manifolds. Al-
gebr. Geom. Topol. 16.6 (2016), pp. 3103-3166.
[2] Jonathan Hanselman, Jacob Rasmussen, and Liam Watson. Bordered Floer homol-
ogy for manifolds with torus boundary via immersed curves. arXiv:1604.03466. 2016.
[3] Matthew Hedden, Knot Floer homology of Whitehead doubles, Geom. Topol. 11.4
(2007), 2277-2338.
[4] Matthew Hedden, Se-goo Kim, and Charles Livingston. Topologically slice knots of
smooth concordance order two. arXiv:1212.6628. 2012.
[5] Matthew Hedden, Min Hoon Kim, Kyungbae Park. Irreducible 3-manifolds that
cannot be obtained by 0-surgery on a knot. Ongoing work.
41


## Page 42


[6] Matthew Hedden and Adam Simon Levine. Splicing knot complement and bordered
Floer homology. (to appear) J. Reine Angew. Math. arXiv:1210.7055. 2012.
[7] Jennifer Hom. Bordered Floer homology and the tau-invariant of cable knots. Journal
of Topology. 7.2 (2014), pp. 287-326.
[8]
. On the concordance genus of topologically slice knots. International
Mathematics Research Notices 2015.5 (2013), pp. 1295-1314.
[9] Cagatay Kutluhan, Yi-Jen Lee, Cliﬀord Henry Taubes. HF=HM I : Heegaard Floer
homology and Seiberg–Witten Floer homology. arXiv:1007.1979. 2010.
[10] Robert Lipshitz, Peter Ozsv´ath, and Dylan Thurston. A tour of bordered Floer
theory. Proc. Natl. Acad. Sci 108.20 (2011), pp. 2547-2681.
[11]
. Bimodules in bordered Heegaard Floer homology. Geom. Topol. 19.2
(2015), pp. 525-724.
[12]
Bordered Floer Homology: Invariance and pairing. arXiv:0810.0687.
2008.
[13] Peter Ozsv´ath and Zolt´an Szab´o. Holomorphic disks and knot invariants. Adv.
Math. 186.1 (2004), pp. 58-116.
[14]
Holomorphic disks and topological invariants for closed three-
manifolds. Ann. of Math. 159.3 (2004), pp. 1027-1158.
[15]
Holomorphic disks, link invariants, and the multi-variable Alexander
Polynomial. Alg. Geom. Topol. 8.2 (2008), pp. 615-692.
[16]
Knot Floer homology and integer surgeries. Alg. Geom. Topol. 8.1
(2008), pp. 101-153.
[17]
Knot Floer homology and the four-ball genus. Geom, Topol. 7 (2003),
pp. 615-639.
42

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
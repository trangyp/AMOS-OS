# 9703025v3_Wheels__Wheeling__and_the_Kontsevich_Integral_of_the_Unknot

> Source: 9703025v3_Wheels__Wheeling__and_the_Kontsevich_Integral_of_the_Unknot.pdf

> Pages: 13

---


## Page 1


arXiv:q-alg/9703025v3  26 Apr 1998
WHEELS, WHEELING, AND THE KONTSEVICH INTEGRAL OF THE
UNKNOT
DROR BAR-NATAN, STAVROS GAROUFALIDIS, LEV ROZANSKY, AND DYLAN P. THURSTON
This is a preprint. Your comments are welcome.
Abstract. We conjecture an exact formula for the Kontsevich integral of the unknot, and
also conjecture a formula (also conjectured independently by Deligne [De]) for the relation
between the two natural products on the space of Chinese characters. The two formulas
use the related notions of “Wheels” and “Wheeling”. We prove these formulas ‘on the level
of Lie algebras’ using standard techniques from the theory of Vassiliev invariants and the
theory of Lie algebras.
Contents
1.
Introduction
1
1.1.
The conjectures
1
1.2.
The plan
6
1.3.
Postscript
7
1.4.
Acknowledgement
7
2.
The monster diagram
7
2.1.
The vertices
7
2.2.
The edges
7
2.3.
The faces
9
3.
Proof of Theorem 1
10
References
11
1. Introduction
1.1. The conjectures. Let us start with the statements of our conjectures; the rest of
the paper is concerned with motivating and justifying them. We assume some familiarity
with the theory of Vassiliev invariants. See e.g. [B-N1, Bi, BL, Go1, Go2, Ko1, Vas1, Vas2]
and [B-N2].
Very brieﬂy, recall that any complex-valued knot invariant V can be extended to an
invariant of knots with double points (singular knots) via the formula V (
) = V (
) −
V (
). An invariant of knots (or framed knots) is called a Vassiliev invariant, or a ﬁnite
type invariant of type m, if its extension to singular knots vanishes whenever evaluated
on a singular knot that has more than m double points. Vassiliev invariants are in some
Date: This edition: Apr. 26, 1998;
First edition: Mar. 13, 1997.
This preprint is available electronically at http://www.ma.huji.ac.il/~drorbn, at
http://jacobi.math.brown.edu/~stavrosg, and at http://xxx.lanl.gov/abs/q-alg/9703025.
1


## Page 2


2
BAR-NATAN, GAROUFALIDIS, ROZANSKY, AND THURSTON
senses analogues to polynomials (on the space of all knots), and one may hope that they
separate knots. While this is an open problem and the precise power of the Vassiliev theory
is yet unknown, it is known (see [Vo]) that Vassiliev invariants are strictly stronger than the
Reshetikhin-Turaev invariants ([RT]), and in particular they are strictly stronger than the
Alexander-Conway, Jones, HOMFLY, and Kauﬀman invariants. Hence one is interested in
a detailed understanding of the theory of Vassiliev invariants.
The set V of all Vassiliev invariants of framed knots is a linear space, ﬁltered by the “type”
of an invariant. The fundamental theorem of Vassiliev invariants, due to Kontsevich [Ko1],
says that the associated graded space gr V of V can be identiﬁed with the graded dual A⋆
of a certain completed graded space A of formal linear combinations of certain diagrams,
modulo certain linear relations. The “diagrams” in A are connected graphs made of a single
distinguished directed line (the “skeleton”), some number of undirected “internal edges”,
some number of trivalent “external vertices” in which an internal edge ends on the skeleton,
and some number of trivalent “internal vertices” in which three internal edges meet. It is
further assumed that the internal vertices are “oriented”; that for each internal vertices one
of the two possible cyclic orderings of the edges emanating from it is speciﬁed. An example
of a diagram in A is in ﬁgure 1. The linear relations in the deﬁnition of A are the well-known
AS, IHX, and STU relations, also shown in ﬁgure 1. The space A is graded by half the
total number of trivalent vertices in a given diagram.
degree=3
degree=7
AS:
IHX:
STU:
=
=
=0
+
−
−
Figure 1.
A diagram in A, a diagram in B (a Chinese character), and the AS, IHX, and
STU relations. All internal vertices shown are oriented counterclockwise.
The most diﬃcult part of the currently known proofs of the isomorphism gr V ∼= A⋆is
the construction of a “universal Vassiliev invariant”; an A-valued framed-knot invariant that
satisﬁes a certain universality property. Such a “universal Vassiliev invariant” is not unique;
the set of universal Vassiliev invariants is in a bijective correspondence with the set of all
ﬁltration-respecting maps V →gr V that induce the identity map gr V →gr V. But it is a
noteworthy and not terribly well understood fact that all known constructions of a universal
Vassiliev invariant are either known to give the same answer or are conjectured to give the
same answer as the original “framed Kontsevich integral” Z (see Section 2.2). Furthermore,
the Kontsevich integral is well behaved in several senses, as shown in [B-N1, B-NG, Kas,
Ko1, LMMO, LM1, LM2].
Thus it seems that Z is a canonical and not an accidental object. It is therefore surprising
how little we know about it. While there are several formulas for computing Z, they are all
of limited use beyond the ﬁrst few degrees. Presently, we do not know how to compute Z
for any knot; not even the unknot!
Our ﬁrst conjecture is about the value of the Kontsevich integral of the unknot.
We
conjecture a completely explicit formula, written in terms of an alternative realization of
the space A, the space B of “Chinese characters” (see [B-N1]).
The space B is also a
completed graded space of formal linear combinations of diagrams modulo linear relations:


## Page 3


WHEELS, WHEELING, AND THE KONTSEVICH INTEGRAL OF THE UNKNOT
3
the diagrams are the so-called Chinese characters, which are the same as the diagrams in
A except that a skeleton is not present, and instead a certain number of univalent vertices
are allowed (the connectivity requirement is dropped, but one insists that every connected
component of a Chinese character would have at least one univalent vertex). An example of
a Chinese character is in ﬁgure 1. The relations are the AS and IHX relations that appear
in the same ﬁgure (but not the STU relation, which involves the skeleton). The degree of
a Chinese character is half the total number of its vertices. There is a natural isomorphism
χ : B →A which maps every Chinese character to the average of all possible ways of placing
its univalent vertices along a skeleton line. In a sense that we will recall below, the fact that
χ is an isomorphism is an analog of the Poincare-Birkhoﬀ-Witt (PBW) theorem. We note
that the inverse map σ of χ is more diﬃcult to construct and manipulate.
Conjecture 1. (Wheels) The framed Kontsevich integral of the unknot, Z(⃝), expressed in
terms of Chinese characters, is equal to
Ω= exp ·∪
∞
X
n=1
b2nω2n.
(1)
The notation in (1) means:
• The ‘modiﬁed Bernoulli numbers’ b2n are deﬁned by the power series expansion
∞
X
n=0
b2nx2n = 1
2 log sinh x/2
x/2
.
(2)
These numbers are related to the usual Bernoulli numbers B2n and to the values of the
Riemann ζ-function on the even integers via (see e.g. [Ap, Section 12.12])
b2n =
B2n
4n(2n)! = (−1)n+1
2n(2π)2nζ(2n).
The ﬁrst three modiﬁed Bernoulli numbers are b2 = 1/48, b4 = −1/5760, and b6 =
1/362880.
• The ‘2n-wheel’ ω2n is the degree 2n Chinese character made of a 2n-gon with 2n legs:
ω2 =
,
ω4 =
,
ω6 =
,
. . . ,
(with all vertices oriented counterclockwise).1
• exp ·∪means ‘exponential in the disjoint union sense’; that is, it is the formal-sum expo-
nential of a linear combination of Chinese characters, with the product being the disjoint
union product.
Let us explain why we believe the Wheels Conjecture (Conjecture 1). Recall ([B-N1]) that
there is a parallelism between the space A (and various variations thereof) and a certain
part of the theory of Lie algebras. Speciﬁcally, given a metrized Lie algebra g, there exists
1 Wheels have appeared in several noteworthy places before: [Ch, CV, KSA, Vai]. Similar but slightly
diﬀerent objects appear in Ng’s beautiful work on ribbon knots [Ng].


## Page 4


4
BAR-NATAN, GAROUFALIDIS, ROZANSKY, AND THURSTON
a commutative square (a reﬁned version is in Theorem 3 below)
χ
Tg
Tg
B
βg
A
the g-invariant part of the completed
universal enveloping algebra of g

the g-invariant part of the com-
pleted symmetric algebra of g

Ug(g)
Sg(g)
in which the left column is the above mentioned formal PBW isomorphism χ, and the right
column is the symmetrization map βg : S(g) →U(g), sending an unordered word of length
n to the average of the n! ways of ordering its letters and reading them as a product in
U(g). The map βg is an isomorphism by the honest PBW theorem. The left-to-right maps
Tg are deﬁned as in [B-N1] by contracting copies of the structure constants tensor, one for
each vertex of any given diagram, using the standard invariant form (·, ·) on g (see citations
in section 2.2 below). The maps Tg seem to ‘forget’ some information (some high-degree
elements on the left get mapped to 0 on the right no matter what the algebra g is, see [Vo]),
but at least up to degree 12 it is faithful (for some Lie algebras); see [Kn].
Theorem 1. Conjecture 1 is “true on the level of semi-simple Lie algebras”. Namely,
TgΩ= Tgχ−1Z(⃝).
We now formulate our second conjecture. Let B′ = span
n
o
/(AS, IHX) be the
same as B, only dropping the connectivity requirement (so that we also allow connected
components that have no univalent vertices). The space B′ has two diﬀerent products, and
thus is an algebra in two diﬀerent ways:
• The disjoint union C1 ·∪C2 of two Chinese characters C1,2 is again a Chinese character.
The obvious bilinear extension of ·∪is a well deﬁned product B′ × B′ →B′, which turns
B′ into an algebra. For emphasis we will call this algebra B′
·∪.
• B′ is isomorphic (as a vector space) to the space A′ = span

	
/(AS, IHX, STU)
of diagrams whose skeleton is a single oriented interval (like A, only that here we also
allow non-connected diagrams). The isomorphism is the map χ : B′ →A′ that maps
a Chinese character with k “legs” (univalent vertices) to the average of the k! ways of
arranging them along an oriented interval (in [B-N1] the sum was used instead of the
average). A′ has a well known “juxtaposition” product ×, related to the “connect sum”
operation on knots:
×
=
.
The algebra structure on A′ deﬁnes another algebra structure on B′. For emphasis we
will call this algebra B′
×.
As before, A′ is graded by half the number of trivalent vertices in a diagram, B′ is graded
by half the total number of vertices in a diagram, and the isomorphism χ as well as the two
products respect these gradings.


## Page 5


WHEELS, WHEELING, AND THE KONTSEVICH INTEGRAL OF THE UNKNOT
5
Deﬁnition 1.1. If C is a Chinese character, let ˆC : B′ →B′ be the operator deﬁned by
ˆC(C′) =



0
if C has more legs than C′,
the sum of all ways of gluing all the
legs of C to some (or all) legs of C′
otherwise.
For example,
c
ω4(ω2) = 0;
c
ω2(ω4) = 8
+ 4
.
If C has k legs and total degree m, then ˆC is an operator of degree m −k.
By linear
extension, we ﬁnd that every C ∈B′ deﬁnes an operator ˆC : B′ →B′, and in fact, even
inﬁnite linear combinations of Chinese characters with an increasing number of legs deﬁne
operators B′ →B′.
As Ωis made of wheels, we call the action of the (degree 0) operator ˆΩ“wheeling”. As
Ωbegins with 1, the wheeling map is invertible. We argue below that ˆΩis a diagrammatic
analog of the Duﬂo isomorphism Sg(g) →Sg(g) (see [Du] and see below). The Duﬂo isomor-
phism intertwines the two algebra structures that Sg(g) has: the structure it inherits from
the symmetric algebra and the structure it inherits from Ug(g) via the PBW isomorphism.
One may hope that ˆΩhas the parallel property:
Conjecture 2. (Wheeling2) Wheeling intertwines the two products on Chinese characters.
More precisely, the map ˆΩ: B′
·∪→B′
× is an algebra isomorphism.
There are several good reasons to hope that Conjecture 2 is true. If it is true, one would be
able to use it along with Conjecture 1 and known properties of the Kontsevich integral (such
as its behavior the operations of change of framing, connected sum, and taking the parallel
of a component as in [LM2]) to get explicit formulas for the Kontsevich integral of several
other knots and links. Note that change of framing and connect sum act on the Kontsevich
integral multiplicatively using the product in A, but the conjectured formula we have for
the Kontsevich integral of the unknot is in B. Using Conjecture 2 it should be possible to
perform all operations in B.
Perhaps a more important reason is that in essence, A and B capture that part of the
information about U(g) and S(g) that can be described entirely in terms of the bracket and
the structure constants. Thus a proof of Conjecture 2 would yield an elementary proof of
the intertwining property of the Duﬂo isomorphism, whose current proofs use representation
theory and are quite involved. We feel that the knowledge missing to give an elementary
proof of the intertwining property of the Duﬂo isomorphism is the same knowledge that is
missing for giving a proof of the Kashiwara-Vergne conjecture ([KV]).
Theorem 2. Conjecture 2 is “true on the level of semi-simple Lie algebras”. A precise
statement is in Proposition 2.1 and the remark following it.
Remark 1.2. As semi-simple Lie algebras “see” all of the Vassiliev theory at least up to
degree 12 [B-N1, Kn], Theorems 1 and 2 imply Conjectures 1 and 2 up to that degree. It
should be noted that semi-simple Lie algebras do not “see” the whole Vassiliev theory at
high degrees, see [Vo].
2Conjectured independently by Deligne [De].


## Page 6


6
BAR-NATAN, GAROUFALIDIS, ROZANSKY, AND THURSTON
Remark 1.3. As the Duﬂo isomorphism has no known elementary proof, the Lie algebra
techniques used in this paper are unlikely to give full proofs of Conjectures 1 and 2.
Remark 1.4. We’ve chosen to work over the complex numbers to allow for some analytical
arguments below. The rationality of the Kontsevich integral [LM1] and the uniform classi-
ﬁcation of semi-simple Lie algebras over ﬁelds of characteristic 0 implies that Conjectures 1
and 2 and Theorems 1 and 2 are independent of the (characteristic 0) ground ﬁeld.
1.2. The plan. Theorem 1 and Theorem 2 both follow from a delicate assembly of widely
known facts about Lie algebras and related objects; the main novelty in this paper is the
realization that these known facts can be brought together and used to prove Theorems 1
and 2 and make Conjectures 1 and 2. The facts we use about Lie-algebras amount to the
commutativity of a certain monstrous diagram. In Section 2 below we will explain everything
that appears in that diagram, prove its commutativity, and prove Theorem 2. In Section 3 we
will show how that commutativity implies Theorem 1 as well. We conclude this introductory
section with a picture of the monster itself:
Theorem 3. (deﬁnitions and proof in Section 2) The following monster diagram is commu-
tative:
KF
χ
A′
RTg
T ℏ
g
T ℏ
g
T ℏ
g
Z
ˆΩ
Sg
1
2
3
4
5
B′
×
B′
·∪
U(g)g[[ℏ]]
S(g)g
×[[ℏ]]
S(g)g
·∪[[ℏ]]
P(g⋆)g[[ℏ]]
P(g⋆)g[[ℏ]]
P(h⋆)W[[ℏ]]
ψg
βg
ιg
D(j1/2
g )
Remark 1.5. Our two conjectures ought to be related—one talks about Ω, and another is
about an operator ˆΩmade out of Ω, and the proofs of Theorems 1 and 2 both use the Duﬂo
map (D(j1/2
g ) in the above diagram). But looking more closely at the proofs below, the
relationship seems to disappear. The proof of Theorem 2 uses only the commutativity of the
face labeled
4
, while the proof of Theorem 1 uses the commutativity of all faces but
4
. No further relations between the conjectures are seen in the proofs of our theorems.
We are still missing the deep relation that ought to exist between ‘Wheels’ and ‘Wheeling’.
Why is it that the same strange combination of Chinese characters Ωplays a role in these
two seemingly unrelated aﬀairs?


## Page 7


WHEELS, WHEELING, AND THE KONTSEVICH INTEGRAL OF THE UNKNOT
7
1.3. Postscript. According to Kontsevich [Ko2], Conjecture 2 seems to follow from the
results he proves in Section 8.3 of that paper, but a full proof of the conjecture is not given
there. [LT] have shown that Conjecture 2 implies Conjecture 1, but unfortunately their
proof does not shed light on the fundamental relationship that ought to exist between the
two conjectures.
1.4. Acknowledgement. Much of this work was done when the four of us were visiting
˚Arhus, Denmark, for a special semester on geometry and physics, in August 1995. We wish to
thank the organizers, J. Dupont, H. Pedersen, A. Swann and especially J. Andersen for their
hospitality and for the stimulating atmosphere they created. We wish to thank the Institute
for Advanced Studies for their hospitality, and P. Deligne for listening to our thoughts and
sharing his. His letter [De] introduced us to the Duﬂo isomorphism; initially our proofs
relied more heavily on the Kirillov character formula. A. Others made some very valuable
suggestions; we thank them and also thank J. Birman, A. Haviv, A. Joseph, G. Perets,
J. D. Rogawski, M. Vergne and S. Willerton for additional remarks and suggestions.
2. The monster diagram
2.1. The vertices. Let gR be the (semi-simple) Lie-algebra of some compact Lie group G,
let g = gR ⊗C, let h ⊂igR be a Cartan subalgebra of g, and let W be the Weyl group of
h in g. Let ∆+ ⊂h⋆be a set of positive roots of g, and let ρ ∈ig⋆
R be half the sum of the
positive roots. Let ℏbe an indeterminate, and let C[[ℏ]] be the ring of formal power series
in ℏwith coeﬃcients in C.
• KF is the set of all framed knots in R3.
• A′ is the algebra of not-necessarily-connected chord diagrams, as in page 2.
• B′
× and B′
·∪denote the space of Chinese characters (allowing connected components that
have no univalent vertices), as in page 4, taken with its two algebra structures.
• U(g)g[[ℏ]] is the g-invariant part of the universal enveloping algebra U(g) of g, with the
coeﬃcient ring extended to be C[[ℏ]].
• S(g)g
×[[ℏ]] and S(g)g
·∪[[ℏ]] denote the g-invariant part of the symmetric algebra S(g) of g,
with the coeﬃcient ring extended to be C[[ℏ]]. In S(g)g
·∪[[ℏ]] we take the algebra struc-
ture induced from the natural algebra structure of the symmetric algebra. In S(g)g
×[[ℏ]]
we take the algebra structure induced from the algebra structure of U(g)g[[ℏ]] by the
symmetrization map βg : S(g)g
×[[ℏ]] →U(g)g[[ℏ]], which is a linear isomorphism by the
Poincare-Birkhoﬀ-Witt theorem.
• P(h⋆)W[[ℏ]] is the space of Weyl-invariant polynomial functions on h⋆, with coeﬃcients
in C[[ℏ]].
• P(g⋆)g[[ℏ]] is the space of ad-invariant polynomial functions on g⋆, with coeﬃcients in
C[[ℏ]].
2.2. The edges.
• Z is the framed version of the Kontsevich integral for knots as deﬁned in [LM1]. A simpler
(and equal) deﬁnition for a framed knot K is
Z(K) = eΘ·writhe(K)/2 · S

˜Z(K)

∈A ⊂A′,


## Page 8


8
BAR-NATAN, GAROUFALIDIS, ROZANSKY, AND THURSTON
where Θ is the chord diagram
, S is the standard algebra map Ar = A/ < Θ >→
A deﬁned by mapping Θ to 0 and leaving all other primitives of A in place, and ˜Z is the
Kontsevich integral as in [Ko1].
• χ is the symmetrization map B′
× →A′, as on page 3.
It is an algebra isomorphism
by [B-N1] and the deﬁnition of ×.
• ˆΩis the wheeling map as in page 5. We argue that it should be an algebra (iso-)morphism
(Conjecture 2).
• RTg denotes the Reshetikhin-Turaev knot invariant associated with the Lie algebra g [Re1,
Re2, RT, Tu].
• T ℏ
g (in all three instances) is the usual “diagrams to Lie algebras” map, as in [B-N1,
Section 2.4 and exercise 5.1]. The only variation we make is that we multiply the image
of a degree m element of A′ (or B′
× or B′
·∪) by ℏm. In the construction of T ℏ
g an invariant
bilinear form on g is needed. We use the standard form (·, ·) used in [RT] and in [CP,
Appendix]. See also [Kac, Chapter 2].
• The isomorphism βg was already discussed when S(g)g
×[[ℏ]] was deﬁned on page 7.
• The deﬁnition of the “Duﬂo map” D(j1/2
g ) requires some preliminaries. If V is a vector
space, there is an algebra map D : P(V ) →Diﬀ(V ⋆) between the algebra P(V ) of
polynomial functions on V and the algebra Diﬀ(V ⋆) of constant coeﬃcients diﬀerential
operators on the symmetric algebra S(V ). D is deﬁned on generators as follows: If α ∈V ⋆
is a degree 1 polynomial on V , set D(α)(v) = α(v) for v ∈V ⊂S(V ), and extend D(α)
to all of S(V ) using the Leibnitz law. A diﬀerent (but less precise) way of deﬁning D is
via the Fourier transform: Identify S(V ) with the space of functions on V ⋆. A polynomial
function on V becomes a diﬀerential operator on V ⋆after taking the Fourier transform,
and this deﬁnes our map D. Either way, if j ∈P(V ) is homogeneous of degree k, the
diﬀerential operator D(j) lowers degrees by k and thus vanishes on the low degrees of
S(V ). Hence D(j) makes sense even when j is a power series instead of a polynomial.
This deﬁnition has a natural extension to the case when the spaces involved are extended
by C[[ℏ]], or even C((ℏ)), the algebra of Laurent polynomials in ℏ.
Now use this deﬁnition of D with V = g to deﬁne the Duﬂo map D(j1/2
g ), where jg(X)
is deﬁned for X ∈g by
jg(X) = det
sinh ad X/2
ad X/2

.
The square root j1/2
g
of jg is deﬁned as in [Du] or [BGV, Section 8.2], and is a power
series in X that begins with 1. We note that by Kirillov’s formula for the character of
the trivial representation (see e.g. [BGV, Theorem 8.4 with λ = iρ]), j1/2
g
is the Fourier
transform of the symplectic measure on Miρ, where Miρ is the co-adjoint orbit of iρ in
g⋆
R (see e.g. [BGV, Section 7.5]):
j1/2
g (X) =
Z
r∈Miρ
eir(X)dr.
(3)
(We consider the symplectic measure as a measure on g⋆
R, whose support is the subset
Miρ of g⋆
R. Its Fourier transform is a function on gR that can be computed via integration
on the support Miρ ⊂g⋆
R of the symplectic measure.) Duﬂo [Du, th´eor`eme V.2] proved
that D(j1/2
g ) is an algebra isomorphism.


## Page 9


WHEELS, WHEELING, AND THE KONTSEVICH INTEGRAL OF THE UNKNOT
9
• ψg is the Harish-Chandra isomorphism U(g)g →P(h⋆)W extended by ℏ. Using the rep-
resentation theory of g, it is deﬁned as follows. If z is in U(g)g and λ ∈h⋆is a positive
integral weight, we set ψg(z)(λ) to be the scalar by which z acts on the irreducible repre-
sentation of g whose heighest weight is λ−ρ. It is well known (see e.g. [Hu, Section 23.3])
that this partial deﬁnition of ψg(z) extends uniquely to a Weyl-invariant polynomial (also
denoted ψg(z)) on h⋆, and that the resulting map ψg : U(g)g →P(h⋆)W is an isomorphism.
• The two equalities at the lower right quarter of the monster diagram need no explanation.
We note though that if the space of polynomials P(g⋆)g[[ℏ]] is endowed with its obvious
algebra structure, only the lower equality is in fact an equality of algebras.
• ιg is the restriction map induced by the identiﬁcation of h⋆with a subspace of g⋆deﬁned
using the form (·, ·) of g. The map ιg is an isomorphism by Chevalley’s theorem (see
e.g. [Hu, Section 23.1] and [BtD, Section VI-2]).
• Sg is the extension by ℏof an integral operator. If p(λ) is an invariant polynomial of
λ ∈g⋆, then
Sg(p)(λ) =
Z
r∈Miρ
p(λ −ir)dr.
Sg can also be viewed as a convolution operator (with a measure concentrated on Mρ),
and like all convolution operators, it maps polynomials to polynomials.
2.3. The faces.
• The commutativity of the face labeled
1
was proven by Kassel [Kas] and Le and
Murakami [LM1] following Drinfel’d [Dr1, Dr2]. We comment that it is this commutativity
that makes the notion of “canonical Vassiliev invariants” [B-NG] interesting.
• The commutativity of the face labeled
2
is immediate from the deﬁnitions, and was
already noted in [B-N1].
• The commutativity of the face labeled
3
(notice that this face fully encloses the one
labeled
5
) is due to Duﬂo [Du, th´eor`eme V.1].
Proposition 2.1. The face labeled
4
is commutative.
Remark 2.2. Recalling that D(j1/2
g ) is an algebra isomorphism, Proposition 2.1 becomes the
precise formulation of Theorem 2.
Proof of Proposition 2.1. Follows immediately from the following two lemmas, taking C = Ω
in (4).
Lemma 2.3. Let κ : g →g⋆be the identiﬁcation induced by the standard bilinear form (·, ·)
of g. Extend κ to all symmetric powers of g, and let κℏ: S(g)g[[ℏ]] →S(g⋆)((ℏ)) be deﬁned
for a homogeneous s ∈S(g)g[[ℏ]] (relative to the grading of S(g)) by κℏ(s) = ℏ−deg sκ(s).
If C ∈B′ is a Chinese character, ˆC : B′ →B′ is the operator corresponding to C as in
Deﬁnition 1.1, and C′ ∈B′ is another Chinese character, then
T ℏ
g ˆC(C′) = D(κℏT ℏ
g C)T ℏ
g C′.
(4)


## Page 10


10
BAR-NATAN, GAROUFALIDIS, ROZANSKY, AND THURSTON
Proof. If κj is a tensor in Sk(g⋆) ⊂g⋆⊗k, the k’th symmetric tensor power of g⋆, and j′ is a
tensor in Sk′(g) ⊂g⊗k′, then
D(κj)(j′) =





0
if k > k′,
the sum of all ways of contracting all
the tensor components of j with some
(or all) tensor components of j′
otherwise.
(5)
By deﬁnition, the “diagrams to Lie algebras” map carries gluing to contraction, and hence
carries the operation in Deﬁnition 1.1 to the operation in (5), namely, to D. Counting powers
of ℏ, this proves (4).
Lemma 2.4. κℏT ℏ
g Ω= j1/2
g .
Proof. It follows easily from the deﬁnition of T ℏ
g and κh that (κℏT ℏ
g ωn)(X) = tr(ad X)n for
any X ∈g. Hence, using the fact that κℏ◦T ℏ
g is an algebra morphism if B′ is taken with
the disjoint union product,
(κℏT ℏ
g Ω)(X) = exp
∞
X
n=1
b2n(κℏT ℏ
g ω2n)(X) = exp
∞
X
n=1
b2n tr(ad X)2n = det exp
∞
X
n=1
b2n(ad X)2n.
By the deﬁnition of the modiﬁed Bernoulli numbers (2), this is
det exp 1
2 log sinh ad X/2
ad X/2
= det
sinh ad X/2
ad X/2
1/2
= j1/2
g (X).
Proposition 2.5. The face labeled
5
is commutative.
Proof. According to M. Vergne (private communication), this is a well known fact.
We
could not ﬁnd a reference, so here’s the gist of the proof.
Forgetting about powers of
ℏand g-invariance and taking the Fourier transform (over gR), the diﬀerential operator
D(j1/2
g ) becomes the operator of multiplication by j1/2
g (iX) on S(g). Taking the inverse
Fourier transform, we see that D(j1/2
g ) is the operator of convolution with the inverse Fourier
transform of j1/2
g (iX), which is the symplectic measure on Mρ (see (3)).
So D(j1/2
g ) is
convolution with that measure, as required.
3. Proof of Theorem 1
We prove the slightly stronger equality
T ℏ
g Ω= T ℏ
g χ−1Z(⃝).
(6)
Proof. We compute the right hand side of (6) by computing Sgιg−1ψgRTg(⃝) and using the
commutativity of the monster diagram. It is known (see e.g. [CP, example 11.3.10]) that if
λ −ρ ∈h⋆is the highest weight of some irreducible representation Rλ−ρ of g, then
(ψgRTg(⃝))(λ) =
1
dim Rλ−ρ
Y
α∈∆+
sinh ℏ(λ, α)/2
sinh ℏ(ρ, α)/2,


## Page 11


WHEELS, WHEELING, AND THE KONTSEVICH INTEGRAL OF THE UNKNOT
11
where ∆+ is the set of positive roots of g and (·, ·) is the standard invariant bilinear form
on g. By the Weyl dimension formula and some minor arithmetic, we get (see also [LM2,
section 7])
(ψgRTg(⃝))(λ) =
Y
α∈∆+
ℏ(ρ, α)/2
sinh ℏ(ρ, α)/2 · sinh ℏ(λ, α)/2
ℏ(λ, α)/2
.
(7)
We can identify g and g⋆using the form (·, ·), and then expressions like ‘ad λ’ makes sense.
By deﬁnition, if gα is the weight space of the root α, then ad λ acts as multiplication by
(λ, α) on gα, while acting trivially on h. From this and (7) we get
(ψgRTg(⃝))(λ) = det

ad ℏρ/2
sinh ad ℏρ/2
1/2
· det
sinh ad ℏλ/2
ad ℏλ/2
1/2
= j−1/2
g
(ℏρ) · j1/2
g (ℏλ).
The above expression (call it Z(λ)) makes sense for all λ ∈g⋆, and hence it is also
ιg−1ψgRTg(⃝). So we’re only left with computing SgZ(λ):
SgZ(λ) =
Z
r∈Miρ
dr Z(λ −ir) = j−1/2
g
(ℏρ)
Z
r∈Miρ
dr j1/2
g (ℏ(λ −ir)).
By (3), this is
j−1/2
g
(ℏρ)
Z
r∈Miρ
dr
Z
r′∈Miρ
dr′ eiℏ(r′,λ−ir) = j−1/2
g
(ℏρ)
Z
r′∈Miρ
dr′ eiℏ(r′,λ)
Z
r∈Miρ
dr eiℏ(−ir′,r).
Using (3) again, we ﬁnd that the inner-most integral is equal to j1/2
g (ℏρ) independently of
r′, and hence
SgZ(λ) =
Z
r′∈Miρ
dr′ eiℏ(r′,λ),
and using (3) one last time we ﬁnd that
SgZ(λ) = j1/2
g (ℏλ).
(8)
The left hand side of (6) was already computed (up to duality and powers of ℏ) in
Lemma 2.4. Undoing the eﬀect of κℏthere, we get the same answer as in (8).
References
[Ap]
T. M. Apostol, Introduction to analytic number theory, Springer-Verlag New York 1976.
[B-N1]
D. Bar-Natan, On the Vassiliev knot invariants, Topology 34 423–472 (1995).
[B-N2]
, Bibliography of Vassiliev Invariants, http://www.ma.huji.ac.il/~drorbn.
[B-NG]
and S. Garoufalidis, On the Melvin-Morton-Rozansky conjecture, Invent. Math. 125 (1996)
103–133.


## Page 12


12
BAR-NATAN, GAROUFALIDIS, ROZANSKY, AND THURSTON
[BGV]
N. Berline, E. Getzler and M. Vergne, Heat kernels and Dirac operators, Grundlehren der mathe-
matischen wissenschaften 298, Springer-Verlag Berlin Heidelberg 1992.
[Bi]
J. S. Birman, New points of view in knot theory, Bull. Amer. Math. Soc. 28 (1993) 253–287.
[BL]
and X-S. Lin, Knot polynomials and Vassiliev’s invariants, Inv. Math. 111 (1993) 225–270.
[BtD]
T. Br¨ocker and T. tom Dieck, Representations of compact Lie groups, Springer-Verlag GTM 98,
New York 1985.
[CP]
V. Chari and A. Pressley, Quantum groups, Cambridge University Press, Cambridge 1994.
[Ch]
S. V. Chmutov, Combinatorial analog of the Melvin-Morton conjecture, Program System Institute
(Pereslavl-Zalessky, Russia) preprint, September 1996.
[CV]
and A. N. Varchenko, Remarks on the Vassilliev knot invariants coming from sl2, Topology,
to appear.
[De]
P. Deligne, letter to D. Bar-Natan, Jan. 25, 1996, http://www.ma.huji.ac.il/~drorbn/Deligne/.
[Dr1]
V. G. Drinfel’d, Quasi-Hopf algebras, Leningrad Math. J. 1 (1990) 1419–1457.
[Dr2]
, On quasitriangular Quasi-Hopf algebras and a group closely connected with Gal(¯Q/Q),
Leningrad Math. J. 2 (1991) 829–860.
[Du]
M. Duﬂo, Caract`eres des groupes et des alg`ebres de Lie r´esolubles, Ann. scient. ´Ec. Norm. Sup. 4(3)
(1970) 23–74.
[Go1]
M. Goussarov, A new form of the Conway-Jones polynomial of oriented links, in Topology of man-
ifolds and varieties (O. Viro, editor), Amer. Math. Soc., Providence 1994, 167–172.
[Go2]
, On n-equivalence of knots and invariants of ﬁnite degree, in Topology of manifolds and
varieties (O. Viro, editor), Amer. Math. Soc., Providence 1994, 173–192.
[Hu]
J. E. Humphreys, Introduction to Lie algebras and representation theory, Springer-Verlag GTM 9,
New York 1972.
[Kac]
V. G. Kac, Inﬁnite dimensional Lie algebras, Cambridge University Press, 1990.
[KV]
M. Kashiwara and M. Vergne, The Cmpbell-Hausdorﬀformula and invariant hyperfunctions, Invent.
Math. 47 (1978) 249–272.
[Kas]
C. Kassel, Quantum groups, Springer-Verlag GTM 155, Heidelberg 1994.
[Kn]
J. A. Kneissler, The number of primitive Vassiliev invariants up to degree twelve, University of Bonn
preprint, June 1997. See also q-alg/9706022.
[Ko1]
M. Kontsevich, Vassiliev’s knot invariants, Adv. in Sov. Math., 16(2) (1993) 137–150.
[Ko2]
, Deformation quantization of Poisson manifolds, I.H.E.S. preprint, September 1997. See
also q-alg/9709040.
[KSA]
A. Kricker, B. Spence, and I. Aitchison, Cabling the Vassiliev invariants, Jour. of Knot Theory and
its Ramiﬁcations 6 (1997) 327–358. See also q-alg/9511024.
[LMMO] T. Q. T. Le, H. Murakami, J. Murakami, and T. Ohtsuki, A three-manifold invariant via the
Kontsevich integral, Max-Planck-Institut Bonn preprint, 1995.
[LM1]
and J. Murakami, The universal Vassiliev-Kontsevich invariant for framed oriented links,
Compositio Math. 102 (1996), 42–64. See also hep-th/9401016.
[LM2]
and
, Parallel version of the universal Vassiliev-Kontsevich invariant, J. Pure and
Appl. Algebra 121 (1997) 271–291.
[LT]
and D. P. Thurston, unpublished.
[MM]
P. M. Melvin and H. R. Morton, The coloured Jones function, Commun. Math. Phys. 169 (1995)
501–520.
[Ng]
K. Y. Ng, Groups of ribbon knots, Topology 37 (1998) 441–458. See also q-alg/9502017.
[Re1]
N. Yu. Reshetikhin, Quantized universal enveloping algebras, the Yang-Baxter equation and invari-
ants of links (I & II), LOMI preprints E-4-87 & E-17-87, Leningrad 1988.
[Re2]
, Quasitriangle Hopf algebras and invariants of tangles, Leningrad Math. J. 1 (1990) 491–513.
[RT]
and V. G. Turaev, Ribbon graphs and their invariants derived from quantum groups, Com-
mun. Math. Phys. 127 (1990) 1–26.
[Tu]
V. G. Turaev, The Yang-Baxter equation and invariants of links, Invent. Math. 92 (1988) 527–553.
[Vai]
A. Vaintrob, Melvin-Morton conjecture and primitive Feynman diagrams, University of Utah
preprint, May 1996.


## Page 13


WHEELS, WHEELING, AND THE KONTSEVICH INTEGRAL OF THE UNKNOT
13
[Vas1]
V. A. Vassiliev, Cohomology of knot spaces, Theory of Singularities and its Applications (Providence)
(V. I. Arnold, ed.), Amer. Math. Soc., Providence, 1990.
[Vas2]
, Complements of discriminants of smooth maps: topology and applications, Trans. of Math.
Mono. 98, Amer. Math. Soc., Providence, 1992.
[Vo]
P. Vogel, Algebraic structures on modules of diagrams, Universit´e Paris VII preprint, July 1995.
Institute of Mathematics, The Hebrew University, Giv’at-Ram, Jerusalem 91904, Israel
E-mail address: drorbn@math.huji.ac.il
Department of Mathematics, Harvard University, Cambridge MA 02138, USA
E-mail address: stavros@math.harvard.edu
Department of Mathematics, Statistics, and Computer Science, University of Illinois at
Chicago, Chicago IL 60607-7045, USA
E-mail address: rozansky@math.uic.edu
Department of Mathematics, University of California at Berkeley, Berkeley CA 94720-
3840, USA
E-mail address: dpt@math.berkeley.edu

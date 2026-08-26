# 0204311v3_Two_applications_of_elementary_knot_theory_to_Lie_algebras_and_Vassiliev_invaria

> Source: 0204311v3_Two_applications_of_elementary_knot_theory_to_Lie_algebras_and_Vassiliev_invaria.pdf

> Pages: 31

---


## Page 1


ISSN 1364-0380 (on line) 1465-3060 (printed)
1
Geometry & Topology
G
G
G
GG
GGG G GGGG
G
G
T TTTT
T
T
T
T
T
T
T
T
TT
Volume 7 (2003) 1–31
Published: 23 January 2003
Two applications of elementary knot theory to
Lie algebras and Vassiliev invariants
Dror Bar-Natan
Thang T Q Le
Dylan P Thurston
Dept of Mathematics
University of Toronto
Toronto ON M5S 3G3
Canada
Dept of Mathematics
SUNY at Buﬀalo
Buﬀalo NY 14214
USA
Dept of Mathematics
Harvard University
Cambridge, MA 02138
USA
drorbn@math.toronto.edu
letu@math.buffalo.edu
dpt@math.harvard.edu
http://www.math.toronto.edu/~drorbn buffalo.edu/~letu harvard.edu/~dpt
Abstract
Using elementary equalities between various cables of the unknot and the Hopf
link, we prove the Wheels and Wheeling conjectures of [5, 9], which give, re-
spectively, the exact Kontsevich integral of the unknot and a map intertwining
two natural products on a space of diagrams. It turns out that the Wheeling
map is given by the Kontsevich integral of a cut Hopf link (a bead on a wire),
and its intertwining property is analogous to the computation of 1 + 1 = 2
on an abacus. The Wheels conjecture is proved from the fact that the k-fold
connected cover of the unknot is the unknot for all k.
Along the way, we ﬁnd a formula for the invariant of the general (k, l) cable of a
knot. Our results can also be interpreted as a new proof of the multiplicativity
of the Duﬂo–Kirillov map S(g) →U(g) for metrized Lie (super-)algebras g.
AMS Classiﬁcation numbers
Primary:
57M27
Secondary:
17B20, 17B37
Keywords
Wheels, Wheeling, Vassiliev invariants, Hopf link, 1+1 = 2, Duﬂo
isomorphism, cabling
Proposed: Vaughan Jones
Received: 9 May 2002
Seconded: Yasha Eliashberg, Joan Birman
Accepted: 8 November 2002
c⃝Geometry & Topology Publications


## Page 2


2
Bar-Natan, Le and Thurston
1
Introduction
1.1
The Duﬂo–Kirillov isomorphism
The Duﬂo–Kirillov isomorphism is an algebra isomorphism between the invari-
ant part of the symmetric algebra and the center of the universal enveloping
algebra for any Lie algebra g. This isomorphism was ﬁrst described for semi-
simple Lie algebras by Harish-Chandra.
Kirillov gave a formulation of the
Harish-Chandra map that has meaning for all ﬁnite-dimensional Lie algebras,
and conjectured that it is always an algebra isomorphism. The conjecture was
proved by Duﬂo [11]. Although the Kirillov–Duﬂo map can be formulated in
a very explicit way as a linear map between two pretty simple algebras (with
very explicit structure), all known proofs of the Duﬂo theorem were diﬃcult: In
the book of Dixmier [10], the proof is given only in the last chapter and it uti-
lizes most of results developed in the whole book, including many classiﬁcation
results (a situation Godement [12] called “scandalous”). As discussed below,
there have been several recent proofs that do not use classiﬁcation results, but
they all use tools from well outside the natural domain of the problem.
Let us review brieﬂy the Duﬂo theorem.
The Poincar´e–Birkhoﬀ–Witt map
between the symmetric algebra and the universal enveloping algebra of a Lie
algebra g,
χ : S(g) −→U(g),
given by taking a monomial x1 . . . xn in S(g) and averaging over the product
(in U(g)) of the xi in all possible orders, is an isomorphism of vector spaces and
g-modules. Since S(g) is abelian and U(g) is generally not, χ is clearly not
an algebra isomorphism. Even restricting to the invariant subspaces on both
sides,
χ : S(g)g −→U(g)g = center of U(g),
χ is still not an isomorphism of algebras.
The Duﬂo theorem says that the combination χ◦∂j
1
2 , with ∂j
1
2 : S(g) −→S(g)
deﬁned below, is an algebra isomorphism between S(g)g and U(g)g.
Here j
1
2 (x) is a formal power series (beginning with 1) on g , deﬁned by
j
1
2(x) = det
1
2
 
sinh(1
2 ad x)
1
2 ad x
!
.
The operator ∂j
1
2 is obtained by plugging the (commuting) vector ﬁelds ∂/∂x∗
(on g∗) in the power series j
1
2 . (Note that for x∗∈g∗, ∂/∂x∗transforms like
Geometry & Topology, Volume 7 (2003)


## Page 3


Applications of knot theory to Lie algebras and Vassiliev invariants
3
an element of g). The result is an inﬁnite-order diﬀerential operator on g∗,
which we can then apply to a polynomial on g∗(≡an element of S(g)). For
details, see [11]. The function j
1
2 (x) plays an important role in Lie theory. Its
square, j(x), is the Jacobian of the exponential mapping from g to the Lie
group G. The operator ∂j
1
2 is called the strange isomorphism by Kontsevich
[16].
1.2
Elementary knot theory
We will touch upon two simple facts in knot theory that have deep consequences
for Lie algebras and Vassiliev invariants. The two facts can be summarized by
the catch phrases “1 + 1 = 2” and “n · 0 = 0.”
• “1 + 1 = 2.” This refers to a fact in “abacus arithmetic.” On an abacus,
the number 1 is naturally represented by a single bead on a wire, as in
Figure 1(a), which we think of as a tangle. The fact that 1 + 1 = 2 then
becomes the equality of the two tangles in Figure 1(b). On the left side of
the ﬁgure, “1 + 1”, the two beads are well separated, as for connect sum
of links or multiplication of tangles; on the right side, “2”, we instead
start with a single bead and double it, so the two beads are very close
together.
In other terms, the connected sum of two Hopf links is the same as dou-
bling one component of a single Hopf link, as in Figure 1(c).
(a) The link “1”
(b) “1 + 1 = 2”
(c) An alternate version of
“1 + 1 = 2”
Figure 1: Elementary knot theory, part 1
• “n · 0 = 0.” In the spirit of abacus arithmetic, 0 is represented as just
a single vertical strand. We prefer to close it oﬀ, yielding the knot in
Figure 2(a). The knot n · 0 is then this knot repeated n times, as in
Figure 2(b).The two knots are clearly the same, up to framing.
Geometry & Topology, Volume 7 (2003)


## Page 4


4
Bar-Natan, Le and Thurston
(a) The knot “0”
(b) The knot “n · 0,”
shown here for n = 3
Figure 2: Elementary knot theory, part 2
1.3
Wheels and wheeling: main results
The bridges between the knot theory of Section 1.2 and the seemingly quite
disparate Lie algebra theory of Section 1.1 are a certain spaces of uni-trivalent
diagrams (called Jacobi diagrams) modulo local relations. (See Section 2.1, the
1-valent vertices are called the “legs” of the diagram.) On the one hand, such
diagrams give elements of U(g) or S(g) for every metrized Lie algebra g in
a uniform way; on the other hand, they occur naturally in the study of ﬁnite
type invariants of knots [3, 15]. Like the associative algebras S(g) and U(g)
associated to Lie algebras, these diagrams appear in two diﬀerent varieties: A,
in which the legs have a linear order, as in Figure 3(a), and B, in which the legs
are unordered, as in Figure 3(b). As for Lie algebras, they each have a natural
algebra structure (concatenation and disjoint union, respectively); and there is
an isomorphism χ : B →A between the two (averaging over all possible orders
of the legs).
(a) A sample element of A
(b) A sample element of B
Figure 3: Examples of Jacobi diagrams
There is one element of the algebra B that will be particularly important for
us: the “wheels” element. It is the diagrammatic analogue of the function j
1
2
above:
Ω= exp
∞
X
n=1
b2nω2n ∈B,
(1)
Geometry & Topology, Volume 7 (2003)


## Page 5


Applications of knot theory to Lie algebras and Vassiliev invariants
5
where:
• The ‘modiﬁed Bernoulli numbers’ b2n are deﬁned by the power series
expansion
∞
X
n=0
b2nx2n = 1
2 log sinh x/2
x/2
.
(2)
These numbers are related to the usual Bernoulli numbers B2n = 4n ·
(2n)! · b2n and to the values of the Riemann ζ-function on the even
integers.
The ﬁrst three modiﬁed Bernoulli numbers are b2 = 1/48,
b4 = −1/5760, and b6 = 1/362880.
• The ‘2n-wheel’ ω2n is the degree 2n Jacobi diagram made of a 2n-gon
with 2n legs:
ω2 =
,
ω4 =
,
ω6 =
,
. . . .
(3)
Let ∂Ωbe the operation of applying Ωas a diﬀerential operator, which takes a
diagram D and attaches some of its legs to all the legs of Ω. (See Section 2.5
for the precise deﬁnition.)
The ﬁrst main result of this paper is the following analog of the Duﬂo theorem.
Wheeling Theorem The map Υ = χ ◦∂Ω: B →A is an algebra isomor-
phism.
Although the Wheeling theorem was motivated by Lie algebra considerations
when it was ﬁrst conjectured [5, 9], the proof we will give, based on the equation
“1 + 1 = 2” from Section 1.2, is entirely independent of Lie algebras and is
natural from the point of view of knot theory. In particular, we obtain a new
proof of the Duﬂo theorem for metrized Lie algebras, with some advantages
over the original proofs by Harish-Chandra, Duﬂo, and Cartan: our proof does
not require any detailed analysis of Lie algebras, and so works in other contexts
in which there is a Jacobi relation. For instance, our proof works for super Lie
algebras with no modiﬁcation.
The Wheeling theorem has already seen several applications. We will use it to
compute the Kontsevich integral of the unknot, using our second elementary
knot theory identity “n · 0 = 0”.
Wheels Theorem The Kontsevich integral of the unknot is
Z(⃝) = Ω∈B.
Geometry & Topology, Volume 7 (2003)


## Page 6


6
Bar-Natan, Le and Thurston
The Wheeling theorem was ﬁrst conjectured by Deligne [9] and by Bar-Natan,
Garoufalidis, Rozansky and Thurston [5], who also conjectured the Wheels
theorem.
Along the way we also ﬁnd a formula describing the behaviour of the Kontsevich
integral under connected cabling of knots. We also compute the Kontsevich
integral of the Hopf link
); which is intimately related to the map Υ above.
Further computations for a sizeable class of knots, links, and 3-manifolds (in-
cluding all torus knots and Seifert-ﬁber homology spheres) have been done by
Bar-Natan and Lawrence [7]. Hitchin and Sawon [14] have used the Wheeling
theorem to prove an identity expressing the L2 norm of the curvature tensor of
a hyperk¨ahler manifold in terms of Pontryagin classes. In a future paper [25]
one of us (DPT) will show how to write simple formulas for the action of sl2(Z)
on the vector space associated to a torus in the perturbative TQFT of Mu-
rakami and Ohtsuki [24]. Our connected cabling formula also ﬁnds application
in recent work of Roberts and Willerton on the “total Chern class” invariant of
knots.
There are two other recent proofs of the Wheeling theorem.
One is due to
Kontsevich [16, Section 8], as expanded by [2, 13, 23]. Kontsevich’s proof is
already at a diagrammatic level, similar to the one in this paper, although it
is more general: it works for all Lie algebras, not just metrized ones. His proof
again uses a transcendental integral, similar in spirit to the “Kontsevich inte-
gral” in the theory of Vassiliev invariants [15]. Another proof is due to Alekseev
and Meinrenken [1]. The Alekseev and Meinrenken paper is not written in dia-
grammatic language, but seems to extend to the diagrammatic context without
problems. Their proof does not involve transcendental integrals: the only inte-
gral in their proof is in the proof of the Poincar´e lemma (the homology of Rn
is trivial in dimension > 0).
1.4
Plan of the paper
In the ﬁrst section we review the theory of Jacobi diagrams. Section 3 is devoted
to cabling formulas of the Kontsevich integral which are crucial in the proofs
of main theorems.
In Sections 4 and 5 we prove the Wheeling and Wheels
theorems. In Section 6 we calculate the values of the Kontsevich integral of the
Hopf link. In the Appendix we give a self-contained method to determine the
coeﬃcients of the wheels element.
Geometry & Topology, Volume 7 (2003)


## Page 7


Applications of knot theory to Lie algebras and Vassiliev invariants
7
1.5
Acknowledgement
Research by the authors DBN and DPT was supported in part by BSF grant
#1998-119. The author TTQL was partially supported by NSF grant DMS-
9626404 and a postdoc fellowship at the Mathematical Sciences Research In-
stitute in Berkeley in 1996–1997. Research at MSRI was supported in part by
NSF grant DMS-9022140. The author DPT was supported by an NSF Gradu-
ate Student Fellowship, a Sloan Dissertation Fellowship, and an NSF Postdoc-
toral Research Fellowship. In addition we wish to thank A Haviv, J Lieberum,
A Referee and J Roberts for their comments and suggestions.
2
Preliminaries on Jacobi diagrams
We recall basic deﬁnitions and some known properties of Jacobi diagrams in
this section. For details, see [3].
2.1
Jacobi diagrams
An open Jacobi diagram (sometimes called a Chinese Character, uni-trivalent
graph, or web diagram) is a vertex-oriented uni-trivalent graph, ie, a graph
with univalent and trivalent vertices together with a cyclic ordering of the edges
incident to the trivalent vertices. Self-loops and multiple edges are allowed. A
univalent vertex is called a leg, and trivalent vertex is also called an internal
vertex. In planar pictures, the orientation on the edges incident on a vertex
is the clockwise orientation, unless otherwise stated. The degree of an open
Jacobi diagram is half the number of vertices (trivalent and univalent). Some
examples are shown in Figure 3(b).
Suppose X is a compact oriented 1-manifold (possibly with boundary, often
with labeled components) and Y a ﬁnite set of (labeled) asterisks, symbols of
the form ∗x, ∗y , etc.. A Jacobi diagram based on X ∪Y is a graph D together
with a decomposition D = X ∪Γ, where Γ is an open Jacobi diagram with
some legs labeled by elements of Y , such that D is the result of gluing all the
non-labeled legs of Γ to distinct interior points of X . Note that repetition
of labels is allowed, and not all labels have to be used. The degree of D, by
deﬁnition, is the degree of Γ. Usually X is called the skeleton of D, and in
picture is depicted by bold lines.
Suppose φ : X′ →X is a covering map between compact oriented 1-manifolds,
and D = X ∪Γ is a Jacobi diagram based on X ∪Y . The pull-back φ∗(D) is
Geometry & Topology, Volume 7 (2003)


## Page 8


8
Bar-Natan, Le and Thurston
the sum over all Jacobi diagrams D′ based on X′ ∪Y such that φ(D′) = D.
Here φ(D′) = D means D′ = X′ ∪Γ and φ can be extended to D′ so that it
is identity on Γ.
The space Af(X∪Y ), X and Y as above, is the space of Jacobi diagrams based
on X ∪Y modulo the usual antisymmetry, IHX and STU relations (see [3]).
The completion of Af(X ∪Y ) with respect to degree is denoted by A(X ∪Y ).
When φ : X′ →X is a cover, the pull-back φ∗descends to a well-deﬁned map
from A(X ∪Y ) to A(X′∪Y ). An example of pull-backs is the Adams operation
in [3].
Let Abc(X ∪Y ) be the subspace of A(X ∪Y ) spanned by boundary-connected
Jacobi diagrams: diagrams with no connected components that are disjoint
from the skeleton X .
There is a natural map from A(↑∪X) to A(⟳∪X) given by attaching the
two endpoints of the interval ↑. If X is a closed 1-manifold, then this map is
an isomorphism. In particular, when X = ∅, the spaces A(↑) and A(⟳) are
canonically isomorphic. But this is not true if X has an interval component.
Explicitly, A(↑↑) ̸≃A(↑⟳) ≃A(⟳⟳).
An open Jacobi diagram is strutless if it does not have a connected component
homeomorphic to a strut ⌢, ie an interval. A strutless element of A(Y ), where
Y is a set of asterisks, is a linear combination of strutless diagrams.
2.2
Special interesting cases
Of special interest are the following A(X ∪Y ).
For X = ∅and Y has one element, the space A(X ∪Y ) is denoted by B. Note
that all the labels of legs of diagrams in B are the same, and we often forget
the labels. There is a natural product in B deﬁned by taking disjoint union
of diagrams. With this product B is a commutative algebra. The wheels ω2n
introduced in the introduction belongs to B.
For X = ⟳, the oriented circle, and Y = ∅, the space A(⟳), also denoted
simply by A, is the space in which lie the values of the Kontsevich integral
of a knot. There is a natural product in A deﬁned by taking connected sums
of diagrams based on ⟳. With this product A is a commutative algebra. As
noted before, A is canonically isomorphic to A(↑), and we will often identify
these vector spaces. Note that the space A of [3, 20] is equal to our Abc(⟳),
the boundary-connected part.
Geometry & Topology, Volume 7 (2003)


## Page 9


Applications of knot theory to Lie algebras and Vassiliev invariants
9
Suppose X = Y = ∅. The space A(∅) is the space in which lie the values of
the LMO invariants of 3-manifolds [21]. With disjoint union as the product,
A(∅) becomes a commutative algebra, and all other A(X ∪Y ) have a natural
A(∅)-module structure.
It is known that for any metrized Lie algebra g, there are the weight maps, which
are algebra homomorphisms, Wg: Bf →S(g)g and Wg: Af(⟳) →U(g)g,
see [3]. Here S(g) and U(g) are respectively the symmetric algebra and the
universal enveloping algebra of g, and Mg is the invariant subspace of the g-
module M . Thus U(g)g is the center of U(g). In some sense, one can think of
A and B as being related to a “universal (metrized) Lie algebra”, incorporating
information about all Lie algebras at once. But B and A are both bigger and
smaller than that. For example, the map from B to the product of S(g)g for
all metrized Lie algebras is neither injective nor surjective: There are elements
of B that are non-zero but become zero when evaluated in any metrized Lie
algebra [26, 22]1. Not all elements of S(g)g are in the image of the map Wg.
(For instance, the image of Wg consists of polynomials of even order only.)
2.3
Symmetrization maps
One can deﬁne an analog of the Poincare–Birkhoﬀ–Witt isomorphism for dia-
grams as follows.
Suppose X is a collection of compact oriented 1-manifolds and asterisks. The
symmetrization map χx : A(∗x ∪X) →A(↑x ∪X) is a linear map deﬁned on
a diagram D by taking the average over all possible ways of ordering the legs
labeled by x and attach them to an oriented interval. It is known that χx is a
vector space isomorphism [3].
In particular, the symmetrization map χ : B →A(↑) ≡A(⟳) is an isomorphism
of vector spaces, but it is not an algebra isomorphism. We drop the label here.
The two products, disjoint union and connected sum, live on isomorphic spaces
B and A, and may be confused. We usually write out the product in cases of
ambiguity.
1These references only deal with semi-simple Lie (super-) algebras, but according
to Vogel and Lieberum (via private communications), Vogel’s results extend to all
metrized Lie (super-) algebras.
Geometry & Topology, Volume 7 (2003)


## Page 10


10
Bar-Natan, Le and Thurston
2.4
Symmetrization for closed components of the skeleton
We have seen that, using the symmetrization map, one can trade an oriented
interval in X with an asterisk. We want to do the same with closed component
in X . For this we need the link relations.
Suppose ∗y is an element of Y . If a leg of a diagram is labeled y, then the
edge having this leg as an end is called a y-edge. In A(X ∪Y ), link relations
on y are parametrized by Jacobi diagrams based on X ∪Y in which one of the
y-labeled legs is distinguished. The corresponding link relation is the sum of
all ways of attaching the distinguished leg to all the other y-edges:
D
Other legs
y y
y
*y
7→
D
y y
y
Other legs
=
D
y y
y
Other legs
+
D
y y
y
Other legs
+ · · · +
D
y y
y
Other legs
.
Suppose X is a compact oriented 1-manifold, Y is a set of asterisks ∗, and Y ′ is
a set of circled asterisks, symbols of the form ⊛x, ⊛y, etc. Deﬁne A(X ∪Y ∪Y ′)
as the space of Jacobi diagrams based on X ∪Y ∪Y ′ modulo the anti-symmetry,
IHX, and STU relations as before and, in addition, link relations on each label
in Y ′.
Suppose a circled asterisk ⊛y is not in Y ′. The symmetrization map χx : A(⊛y∪
X ∪Y ∪Y ′) →A(⟳y ∪X ∪Y ∪Y ′) is the linear map deﬁned on a diagram D
by taking the average over all possible ways of cyclic-ordering the legs labeled
by y and attach them to the circle ⟳y. It is known that χy is a vector space
isomorphism [6].
2.5
Diagrammatic Diﬀerential Operators
For a strutless diagram C ∈B, the operation of applying C as a diﬀerential
operator, denoted ∂C : B →B, is deﬁned to be
∂C(D) =







0
if C has more legs than D,
the sum of all ways of gluing all
the legs of C to some (or all) legs
of D
otherwise.
For example,
∂ω4(ω2) = 0;
∂ω2(ω4) = 8
+ 4
.
Geometry & Topology, Volume 7 (2003)


## Page 11


Applications of knot theory to Lie algebras and Vassiliev invariants
11
One might think of D as a monomial of degree equal to the number of legs. If
C has k legs and degree m, then ∂C is an operator of degree m −k. By linear
extension, we ﬁnd that every strutless C ∈B deﬁnes an operator ∂C : B →B.
(We restrict to diagrams without struts to avoid circles arising from the pairing
of two struts and to guarantee convergence: gluing with a strut lowers the
degree of a diagram, and so the pairing would not extend from Bf to B.)
In some sense, ∂C is a diagrammatic analogue of a constant coeﬃcient diﬀer-
ential operator. For instance, one has:
• A diagram C with k legs reduces the number of legs by k, corresponding
to a diﬀerential operator of order k.
• If k = 1 (C has only one leg), we have a Leibniz rule like that for linear
diﬀerential operators:
∂C(D1 ⊔D2) = ∂C(D1) ⊔D2 + D1 ⊔∂C(D2).
(Actually, all diagrams with only one leg are 0 in B, so we have to extend
our space of diagrams slightly for this equation to be non-empty. Adding
some extra vertices of valence 1 satisfying no relations is suﬃcient.)
• Multiplication on the diﬀerential operator side is the same thing as com-
position:
∂C1⊔C2 = ∂C1 ◦∂C2.
(4)
3
Cabling
The behaviour of cabling will be crucial to the proofs of all of the Theorems of
this paper. In this section, we will review some results of [20] on disconnected
cabling and prove a new result on connected cabling.
3.1
Tangles, framed tangles, and the Kontsevich integral
Suppose X is a compact oriented 1-manifold.
A tangle with skeleton X is
a smooth proper embedding of X into R × R × [0, 1] ⊂R3, considered up to
isotopy relative to the boundary. The Kontsevich of such a tangle takes value in
the space A′(X), obtained from A(X) by dividing by the framing independence
relation which says that a diagram containing an isolated chord is equal to 0
(see [3], we will not need A′(X) in the future). When X does not have any
circle component, there is a canonical embedding from A′(X) into A(X), and
the Kontsevich integral can be considered valued in A(X).
Geometry & Topology, Volume 7 (2003)


## Page 12


12
Bar-Natan, Le and Thurston
The framed Kontsevich integral of a framed tangle with skeleton X takes value
in A(X) (no framing independence relation here). For technical reasons we will
deﬁne a framed tangle as a tangle: (a) with boundary lying on two lines, the
upper one R × {0} × {1} and the lower one R × {0} × {0}, and (b) equipped
with a non-zero normal vector ﬁeld which is standard (0, 1, 0) at every boundary
point. Framed tangles are considered up to isotopy as usual. In R3 the set of
framing of each component can be canonically identiﬁed with Z. The framed
Kontsevich integral of a framed tangle L is denoted by Z(L). (For details, see
[3, 4, 19, 20]. In [19, 20], Z(L) is denoted by ˆZf(L).)
If a framed tangle L′ is obtained from another L by increasing the framing of
a component labeled x by 1, then we have the following framing formula:
Z(L′) = Z(L) # exp
1
2
%

.
(5)
where the connected sum is done on the component labeled x and
% ∈A(↑) ≡
A(⟳) is the Jacobi diagram based on ⟳with one strut.
The framed Kontsevich integral depends on the positions of the boundary
points.
To get rid of this dependence one has to choose standard positions
for the boundary points. It turns out that the best “positions” are in a limit,
when all the boundary points go to one ﬁxed point. (One has to regularize the
Kontsevich integral in the limit.) In the limit one has to keep track of the order
in which the boundary points go to the ﬁxed point. This leads to the notion
of parenthesized framed tangle, or q-tangle in [19], – a framed tangle with a
non-associative structure on each of the two sequences of boundary points on
the upper and lower lines. For details, see [4, 19].
In all framed tangles in this paper, we assume that a non-associative structure
is ﬁxed.
In many cases, there is only one non-associative structure, or the
non-associative structure is clear from the context.
3.2
Coproduct and Sliding property
Let
∆x
x1...xn : A(↑x ∪X) →A(↑x1 ∪· · · ∪↑xn ∪X)
or
∆x
x1...xn : A(⟳x ∪X) →A(⟳x1 ∪· · · ∪⟳xn ∪X)
be the pull-back of the n-fold disconnected cover of the component labeled x.
When we do not care about the labels on the result, an alternate notation is
∆(n)
x .
Geometry & Topology, Volume 7 (2003)


## Page 13


Applications of knot theory to Lie algebras and Vassiliev invariants
13
Suppose D ∈A(↑x1 ∪· · · ∪↑xn) and D′ ∈A(↑x1 ∪· · · ∪↑xn ∪X). We deﬁne
D · D′ ∈A(↑x1 ∪· · · ∪↑xn ∪X) as the element obtained by placing D on top
of D′, ie, identifying the lower endpoint of ↑xi in D with the upper endpoint
of ↑xi in D′, for i = 1, . . . , n. Similarly, D′ · D ∈A(↑x1 ∪· · · ∪↑xn ∪X) is
obtained by placing D′ on top of D.
In general D·D′ ̸= D′·D. The following is a special case when one has equality
(see, for example, [20, Lemma 8.1]):
Lemma 3.1
(Sliding property) The image of ∆(n)
x
commutes with A(↑x1
∪· · · ∪↑xn), ie, for every D ∈A(↑x1 ∪· · · ∪↑xn) and D′ ∈A(↑x ∪X), we have
that D · ∆(n)
x (D′) = ∆(n)
x (D′) · D.
With the above product, A(↑x1 ∪· · · ∪↑xn) is an algebra. There is also a co-
product on A(↑x1 ∪· · · ∪↑xn) which gives us a structure of a Hopf algebra, and
A(↑x1 ∪· · · ∪↑xn) is a (completed) polynomial algebra generated by primitive
elements. The isolated chord diagrams are among primitive elements. This is
the reason why there is a canonical algebra embedding from A′(↑x1 ∪· · · ∪↑xn)
into A(↑x1 ∪· · · ∪↑xn).
3.3
Disconnected cabling
Suppose L is a framed tangle, with one of its components labeled x. The n-fold
disconnected cabling of L along x, denoted by ∆(n)
x (L), is the tangle obtained
from L by replacing the component labeled x with n of its parallels. Here the
parallels are determined by the framing, and each inherits a natural framing
from that of component x.
The following proposition, proved in [20], describes the behaviour of the Kont-
sevich integral under disconnected cabling.
Proposition 3.2 Suppose that a component labeled x in a framed tangle L
is either closed or has one upper and one lower boundary points. Then
Z(∆(n)
x L) = ∆(n)
x (Z(L)).
(6)
Since Z(∆(n)
x L) depends on the positions of the boundary points, one has to
be careful about the boundary points of the new components (ie parallels) in
∆(n)
x L when the components label x is not closed. The correct choice is the
one in which the distances between the boundary points of the parallels are
Geometry & Topology, Volume 7 (2003)


## Page 14


14
Bar-Natan, Le and Thurston
inﬁnitesimally small compared to the distance between any of these points and
any other boundary point. In the language of parenthesized framed tangles
(or q-tangles), this means the boundary points of the parallels must form an
innermost structure in the overall non-associative structure of the tangle L′,
and the non-associative structure among the boundary points of the parallels
on the upper line must be the same as that among the boundary points of the
parallels on the lower line.
Remark 3.3 In general, the disconnected cabling formula (6) does not hold
true if the x component has both boundary points on the same upper or lower
line. However, it would hold true if the framed Kontsevich integral is modiﬁed
by using a good enough associator [20].
3.4
Connected cabling
Let us deﬁne
ψ(n)
x
: A(⟳x ∪X) →A(⟳x ∪X)
as the pull-back of the n-fold connected cover of the circle labeled x.
Suppose L is a framed tangle, with one of its closed components labeled by x.
The n-fold connected cabling of L along x, denoted by C∆(n)
x (L), is deﬁned as
follows. On the torus boundary of a small tubular neighborhood of component
x there are the preferred longitude and meridian. Replace the component x
with a closed curve on the torus boundary whose homology class is equal to
that of the meridian plus n times the longitude. The result is C∆(n)
x (L). The
new component inherits the orientation and framing from the old one.
The following theorem describes the behaviour of the Kontsevich integral under
connected cabling.
Theorem 1 Suppose a component labeled x in a framed tangle L is closed
(ie a knot). Then
Z(C∆(n)
x (L)) =

ψ(n)
x (Z(L) #x exp( 1
2n
%))

# exp(−1
2
%).
Proof We will prove the theorem in the case when L is a knot. The case of
an arbitrary tangle is quite similar.
The diﬀerence between the connected cabling and the disconnected cabling is
the extra 1/n twist Tn inserted at one point:
Tn =
.
Geometry & Topology, Volume 7 (2003)


## Page 15


Applications of knot theory to Lie algebras and Vassiliev invariants
15
By isotopy we can assume that this twist occurs in a horizontal slice where all
the other strands are vertical. We can apply (6) on the (n, n) “tangle” obtained
by excising Tn. (This object is not properly a tangle, since there is a little piece
cut out of it. But we can still compute its Kontsevich integral.) To complete
the computation, we need to compute a := Z(Tn).
Repeating Tn n times, we get a full twist which we can compute using the
framing and the disconnected cabling formulas (5), (6):
Z





= Z














= ∆(n)

exp(1
2
%)

· exp(−1
2
%)⊗n =: b.
The notation exp(−1
2
%)⊗n means n copies of the framing change element
exp(−1
2
%), one on on each of the n strands, and the product · is the product
in A(↑∪· · · ∪↑).
The n copies of Tn that appear are not quite the same: they diﬀer by cyclic
permutations of the strands. If we could arrange the n strands at the top and
bottom of Tn to be at the vertices of a regular n-gon, the strands would be
symmetric and an = b or
a = b
1
n = ∆(n)

exp( 1
2n
%)

exp(−1
2n
%)⊗n.
In reality, a is not symmetric, ie, σ(a) ̸= a, where σ is the automorphism of
A(↑x1 . . . ↑xn) which rotates the strands by xi 7→xi−1. We have
Z





= a · σ(a) · σ2(a) . . . σn−1(a).
We can conjugate Tn by some tangle C to get the strands symmetric: Tn =
CT ′
nC−1, with T ′
n symmetric. From the deﬁnition of the framed Kontsevich
integral [19], it follows that a = c · a′ · σ(c−1), where a′ = Z′(T ′
n) is the usual
Kontsevich integral of T ′
n, and c = Z(C) ∈A(↑x1 ∪· · · ∪↑xn). Thus
a · σ(a) · σ2(a) . . . σn−1(a) = c(a′)nc−1.
And hence
a = c · b
1
n · c−1
= c · ∆(n)

exp( 1
2n
%)

· exp(−1
2n
%)⊗n · c−1.
Geometry & Topology, Volume 7 (2003)


## Page 16


16
Bar-Natan, Le and Thurston
By the above computations, the invariant of the connected cable of a knot
L is ∆(n)(Z(L)), multiplied by a = Z(Tn), and close up with a twist. The
conjugating elements c and c−1 can be swept through the knot, using the sliding
property of Lemma 3.1, and cancel each other. The factor ∆(n)(exp(%/2n)) in
a can be combined with Z(L) so that we apply ∆(n) to Z(L)#exp(%/2n). The
twisted closure turns ∆(n) into ψ(n). The remaining n factors of exp(−%/2n)
in a can be slid around the knot and combined to give
Z(C∆n(L)) =

ψ(n)

Z(L) # exp( 1
2n
%)

# exp(−1
2
%).
Remark 3.4 Suppose C∆(n|m)
x
(L) is the connected (n, m)-cabling of a framed
tangle L along a closed component labeled x, where n and m are co-prime in-
teger with n > 0, ie, C∆(n|m)
x
(L) is obtained by replacing the x component
with a closed curve on the torus boundary of the regular neighborhood which
represents the homology class of m times the meridian plus n times the longi-
tude. Let ψ(n|m) denotes the corresponding pull-back of Jacobi diagrams. Then
the proof of Theorem 1 also gives:
Z(C∆(n|m)(L)) =
h
ψ(n|m) 
Z(L) # exp( m
2n
%)
i
# exp(−m
2
%).
3.5
Operators ∆, ψ and symmetrized diagrams
One reason to introduce symmetrized diagrams is that the operations ∆and ψ
above become very simple in B. Using the symmetrization map one can trade
an interval in the skeleton with an asterisk, and a circle with a circled asterisk.
The map ∆x and ψx can be carried over to the new spaces. The following
lemmas are well-known (and easy to check).
Lemma 3.5 The map
∆x
x1...xn : A(∗x ∪X) →A(∗x1 ∪· · · ∪∗xn ∪X)
is the sum over all ways of replacing each x leg by one of the xi.
Remark 3.6
∆is similar to a coassociative, cocommutative coproduct in a
coalgebra, except that it does not take values in A ⊗A.
The operation ∆in Lemma 3.5 is analogous to a change of variables x 7→
x1 + · · · + xn for ordinary functions f(x). We will use a suggestive notation:
a leg labeled by a linear combination of variables means the sum over all ways
Geometry & Topology, Volume 7 (2003)


## Page 17


Applications of knot theory to Lie algebras and Vassiliev invariants
17
of picking a variable from the linear combination. If D(x) is a diagram with
some legs labeled x, ∆(n)(D(x)) = D(x1 + · · · + xn) is the diagram with the
same legs labeled x1 + · · · + xn.
Lemma 3.7 (See [17]) The map
ψ(n)
x
: A(⊛x ∪X) →A(⊛x ∪X)
is multiplication by nk on diagrams with k legs labeled x.
This operation is related to the change of variables x 7→nx.
4
The Wheeling Theorem
The operator ∂Ω: B →B, where Ωis the wheels element of the Introduction,
is called the “wheeling” map. The proof of the following theorem will occupy
the rest of this section.
Theorem 2 (Wheeling) The map Υ = χ ◦∂Ω: B →A is an algebra isomor-
phism.
The map Υ is the diagrammatic analogue of the Duﬂo–Kirillov map. Note that
by (4), ∂Ω∂Ω−1 = id, hence ∂Ωis a vector space isomorphism. Since χ is also
a vector space isomorphism, Υ is automatically bijective.
4.1
An inner product
Suppose C, C′ ∈B are diagrams such that C has no struts. If C and C′ have
the same number of legs, then the inner product ⟨C, C′⟩is the sum of all ways
of gluing all the legs of C to all legs of C′. If C and C′ do not have the same
number of legs, then deﬁne ⟨C, C′⟩= 0. The restriction that C not have struts
is to guarantee convergence and avoid closed circles.
We will sometimes want to ﬁx C and consider ⟨C , ·⟩as a map from B to
A(∅); we will denote this map ι(C). This deﬁnition works equally well in the
presence of other skeleton components or to glue several components. We will
use subscripts to indicate which ends are glued.
There are two dualities relating ⟨· , ·⟩with other operations we have deﬁned.
Geometry & Topology, Volume 7 (2003)


## Page 18


18
Bar-Natan, Le and Thurston
Lemma 4.1 Multiplication and comultiplication in B are dual in the sense
that
⟨C, D1 ⊔D2⟩= ⟨∆xyC, (D1)x ⊗(D2)y⟩xy.
Similar statements hold in the presence of other ends.
Proof The glued diagrams are the same on the two sides; we either combine
the legs of D1 and D2 into one set and then glue with C, or we split the legs
of C into two pieces which are then glued with D1 and D2. (Note that there
are no combinatorial factors to worry about: in both cases, we take the sum
over all possibilities.)
Lemma 4.2 Multiplication by a diagram B ∈B and applying B as a dia-
grammatic diﬀerential operator are adjoint in the sense that
⟨A ⊔B, C⟩= ⟨A, ∂B(C)⟩.
Proof As before, the diagrams are the same on both sides.
4.2
The map Φ
Let
Az
x be the tangle in Figure 1(a), which is a bead (labeled x here) on a
wire (labeled z here). Its Kontsevich integral Z(Az
x) takes values in A(↑z, ⟳x).
Symmetrizing the legs attached to the bead x as explained in 2.4, we get
χ−1
x Z(Az
x) ∈A(↑z, ⊛x).
Finally, we use the inner product operation along the legs x to get a map from
B to A:
Φ = ιxχ−1
x Z(Az
x) : B →A
In this last step, there are two things we have to check. First, we must see that
χ−1Z(A) has no struts. This follows from the fact that we took the bead with
the zero framing. Second, we need to check that the inner product descends
modulo the link relations on x in A(↑z, ⊛x).
Lemma 4.3 The inner product ⟨· , ·⟩x : A(∗x ∪X) ⊗A(∗x) →A(X) descends
to a map ⟨· , ·⟩x : A(⊛x ∪X) ⊗A(∗x) →A(X).
Proof Link relations in A(⊛x ⊔X) can be slid over diagrams in A(∗x), as
shown in Figure 4. (See similar arguments in [3]).
Geometry & Topology, Volume 7 (2003)


## Page 19


Applications of knot theory to Lie algebras and Vassiliev invariants
19
Z( A)
D
glue
slide
=
Z( A)
glue
D
= 0.
Figure 4: The proof that Φ(D) is well-deﬁned modulo link relations on Z(A): link
relations in Z(A) can be slid over D.
4.3
Multiplicativity of Φ
We now come to the key lemma in the proof of the wheeling theorem.
Lemma 4.4 The map Φ : B →A is an algebra map.
Proof As advertised, we use the equality of links “1 + 1 = 2”. Let us see
what this equality of links says about the Kontsevich integral of the Hopf link.
On the “1 + 1” side, we see the connected sum of two open Hopf links. It is
known that the invariant of the connected sum is the connected sum of the
invariants. To write this conveniently, let H(z; x) be Z(A) ∈A(↑z, ⊛x), with
the wire labeled by z and the bead labeled by x. Then
Z(A #
A) = H(z; x1) #z H(z; x2) ∈A(↑z, ⊛x1, ⊛x2).
On the “2” side, we see the disconnected cable of a Hopf link. By the discon-
nected cabling formula (6), this becomes the coproduct ∆:
Z(∆(2)
x (A)) = ∆x
x1x2H(z; x) ∈A(↑z, ⊛x1, ⊛x2).
Since the two tangles are isotopic, we have
H(z; x1, x2) def
= H(z; x1) #z H(z; x2) = ∆x
x1x2H(z; x) ∈A(↑z, ⊛x1, ⊛x2).
(7)
Now consider the map
Ξ = ιx1ιx2H(z; x1, x2) : B ⊗B →A;
in other words, in Ξ(D1 ⊗D2) glue the x1 and x2 legs of H(z; x1, x2) to D1
and D2 respectively. This descends modulo the two diﬀerent link relations in
A(↑, ⊛, ⊛) by the argument of Figure 4, applied to D1 and D2 separately. We
have two diﬀerent expressions for this map from the two diﬀerent expressions
Geometry & Topology, Volume 7 (2003)


## Page 20


20
Bar-Natan, Le and Thurston
for H(z; x1, x2). On the “1 + 1” side, the gluing does not interact with the
connected sum and we have
Ξ(D1, D2) = Φ(D1) # Φ(D2),
see Figure 5.
Z( A)
glue
Z( A)
glue
D1
D2
Figure 5: Gluing Z(A #
A) to D1 ⊗D2
For the “2” side, we use Lemma 4.1 to see that
Ξ(D1, D2) = ⟨∆xH(z; x), D1 ⊗D2⟩
(8)
= ⟨H(z; x), D1 ⊔D2⟩
(9)
= Φ(D1 ⊔D2),
(10)
see Figure 6.
Z( A)
glue
split ↑
glue
D1
D2
=
Z( A)
merge ↓
glue
D1
D2
Figure 6: Gluing Z(∆(2)
x (A)) to D1 ⊗D2 in two equivalent ways
Combining the two, we ﬁnd
Φ(D1) # Φ(D2) = Φ(D1 ⊔D2).
Geometry & Topology, Volume 7 (2003)


## Page 21


Applications of knot theory to Lie algebras and Vassiliev invariants
21
4.4
Mapping degrees and the Duﬂo–Kirillov isomorphism
We have successfully constructed a multiplicative map from B to A. We will
see later that this map Φ is the same as Υ, but we cannot yet see this. Instead
we will consider the lowest degree term Φ0 of Φ.
The mapping degree of a diagram D ∈A(↑z, ⊛x) with respect to x is the
amount ιxD : B →A shifts the degree. Explicitly, it is the degree of D minus
the number of x legs of D.
Since there are no x-x struts in H(z; x), every x leg of H must be attached
to another vertex (either internal or on the interval z). Furthermore, if two
x legs are attached to the same internal vertex, the diagram vanishes by anti-
symmetry. Therefore there are at least as many other vertices as x legs in H
and the mapping degree is ≥0.
Let H0(z; x) be the part of H(z; x) of mapping degree 0 with respect to x,
and Φ0 : B →A be ιxH0(z; x). The map Φ0 is still multiplicative, since the
multiplications in A and B both preserve degrees. (For homogeneous diagrams
D1 and D2 of degrees n1 and n2, Φ0(D1 ⊔D2) is the piece of Φ(D1 ⊔D2) of
degree n1 + n2 and likewise for Φ0(D1) # Φ0(D2).)
x
x x
x x
x
z
x
Figure 7: The only diagrams in A(↑z, ⊛x) of mapping degree 0 with respect to x are
wheels and struts.
The diagrams that appear in H0 are very restricted, since every vertex that is
not an x leg must connect to an x leg. The possible diagrams are x wheels and
x −z struts, as shown in Figure 7. The linking number between the bead and
the wire in the link
A is 1, so the coeﬃcient of the x-z strut is 1. Combined
with the fact that the Kontsevich integral is grouplike [20], we ﬁnd that
H0(z; x) = exp(
x
|
z
) ⊔Ω′,
where
Ω′ = exp⊔(
X
n
a2nω2n)
for some coeﬃcients a2n. Note that the right hand side is written in A(↑, ∗)
(with a strange mixed product), since there is no algebra structure on A(↑, ⊛).
Geometry & Topology, Volume 7 (2003)


## Page 22


22
Bar-Natan, Le and Thurston
By the following lemma, we now have a multiplicative map very similar to our
desired map Υ.
Lemma 4.5 One has that Φ0 = χ ◦∂Ω′ .
Proof Using Lemma 4.2 and noting that gluing with exp(|x
z) takes the legs of
a diagram in B and averages over all ways of ordering them, as in the deﬁnition
of χ, we see that
Φ0(D) = ⟨exp(
x
|
z
⊔Ω′, D⟩= ⟨exp(
x
|
z
, ∂′
Ω(D)⟩= χ(∂′
Ω(D)).
4.5
Identifying Φ0 with Υ
To complete the proof of the wheeling theorem, one needs only to show that
Ω= Ω′, or an = bn for n = 2, 4, 6, . . . . This can be proved as follows.
First of all, a calculation of the degree 2 part of the Kontsevich integral of the
Hopf link will show that a2 = b2. Thus if Ω̸= Ω′, then for some n > 1,
Ω−1Ω′ = 1 + (a2n −b2n)ω2n + higher order terms.
Second, the map Υ = χ ◦∂Ωis known to be an algebra isomorphism on the
level of simple Lie algebras [5]. Thus for a simple Lie algebra g, the map ∂Ω−1Ω′
is an algebra automorphism of S(g)g. When g = sl2, the algebra S(g)g is a
polynomial algebra on one generator, which is the image of the strut ⌢. On
the strut ∂Ω−1Ω′ acts as the identity (since there is no non-trivial diagram with
less than 3 legs), hence ∂Ω−1Ω′ acts as the identity on the whole algebra S(g)g.
Third, the action of ω2n on S(g)g is non-trivial.
Explicitly, ∂ω2n[( ⌢)n] =
2(2n + 1)! in sl2, which can be proved easily by induction. Thus, if a2n ̸= b2n,
then ∂Ω−1Ω′ cannot act as identity on S(g)g.
We conclude that Ω= Ω′, and this completes the proof of the wheeling theorem.
For another proof of Ω= Ω′, more detailed and without using the result of [5],
see the Appendix.
4.6
Back to the Duﬂo–Kirillov isomorphism
We note that the wheeling theorem implies the multiplicative property of the
Duﬂo–Kirillov isomorphism for a metrized Lie (super-) algebra g. Indeed, using
the standard maps Wg from spaces of diagrams into spaces of tensors, we set
Geometry & Topology, Volume 7 (2003)


## Page 23


Applications of knot theory to Lie algebras and Vassiliev invariants
23
J = Wg(H(z; x)) ∈U(g) ⊗S(g)g. Here S(g)g denotes the space of coinvariants
of the g action on S(g) — the link relation dictates the descent to this quotient
of S(g).
Also, strictly speaking J lives in the completion of U(g) ⊗S(g)g
induced by the grading on S(g)g. Equation (7) and the compatibility between
Wg and multiplication and comultiplication imply now that J satisﬁes
J # J = (1 ⊗∆)J
in
U(g) ⊗S(g)g ⊗S(g)g,
(11)
where J #J denotes the result of multiplying two copies of J using the product
of U(g), so that the result is in (the appropriate completion of) U(g)⊗S(g)g⊗
S(g)g. Now use the metric of g to identify the space of coinvariants in S(g)
as the dual of the space S(g)g of invariants and hence to re-interpret J as
an element of U(g) ⊗(S(g)g)⋆and hence as a map WJ : S(g)g →U(g). One
easily veriﬁes that equation (11) implies that WJ is multiplicative. It remains
to see that WJ is equal to the Duﬂo–Kirillov map χ ◦∂j
1
2 . This follows from
the computation of H(z; x) in terms of the diagrammatic analogue Ωof j
1
2 in
Section 6.
5
The Wheels Theorem. The Kontsevich integral of
the unknot
This section is devoted to the proof of the Wheels theorem.
Theorem 3 (Wheels) The framed Kontsevich integral of the unknot is the
wheels element:
Z(⟳) = χ(Ω).
We will denote ν = Z(⟳) ∈A = A(↑) ≡A(⟳).
5.1
Useful facts
We will ﬁrst derive some nice properties the wheels element Ω. Set H0(z; x) =
Ωx exp( x⌢z) and start from the basic equality proved in the Wheeling theorem,
∆x
x1x2H0(z; x) = H0(z; x1) #z H0(z; x2) ∈A(↑z ⊛x1⊛x2).
Now consider dropping the strand z, ie, mapping all diagrams with a z vertex
to 0. (Knot-theoretically, this corresponds to dropping the central strand in the
equation “1 + 1 = 2”.) We ﬁnd
∆Ω= Ω⊗Ω∈A(⊛⊛).
(12)
Note that this equality is not true inside A(∗∗).
Geometry & Topology, Volume 7 (2003)


## Page 24


24
Bar-Natan, Le and Thurston
Lemma 5.1 (Pseudo-linearity of log Ω, see also [7]) For any D ∈B,
∂D(Ω) = ⟨D, Ω⟩Ω.
Proof
∂D(Ω)x = ⟨Dy, Ωx+y⟩y = ⟨Dy, ΩxΩy⟩y = ⟨Dy, Ωy⟩yΩx.
In the second equality, we use Equation (12). This is allowed, since the con-
traction descends to A(⊛⊛) ≃A(⊛↑) by the argument of Lemma 4.3.
Remark 5.2 Compare this lemma with standard calculus: if D is any diﬀer-
ential operator and f is a linear function, then Def = (Df)(0)ef . The preﬁx
“pseudo” is written above because Lemma 5.1 does not hold for every D, but
only for x-invariant D’s, ie, for D with link relations on x-legs.
Although we are interested in knots and links in S3, for which the appropri-
ate space of diagrams is the boundary connected part Abc, vacuum diagrams
(elements of A(∅)) appear at various points. Notably, the wheeling map Υ
does not preserve the subspace of boundary connected diagrams. Although the
resulting vacuum components can be computed explicitly,2 they are almost al-
ways irrelevant for us and it would just complicate the formulas to keep track
of them. To avoid this, we will introduce the boundary-connected projection
πbc : A →Abc which maps any diagram containing vacuum components to 0
and is otherwise the identity. Note that πbc is multiplicative. There are similar
projections, which will also be called πbc, for other spaces A(X).
If we compose Lemma 5.1 with πbc, we ﬁnd, for a diagram D ∈B,
πbc∂DΩ=
(
Ω
D is the empty diagram
0
otherwise.
(13)
5.2
A lemma on the bound of numbers of legs
Lemma 5.3 For any elements x1, . . . , xk ∈A(↑) with at least one leg on the
interval ↑, χ−1(x1 # · · · # xk) ∈B has at least k legs.
Proof First note that any vacuum diagrams that appear in the xi’s pass
through unchanged to the result; let us assume that there are none, so that
2D. Bar-Natan and R. Lawrence [7] have done these computations
Geometry & Topology, Volume 7 (2003)


## Page 25


Applications of knot theory to Lie algebras and Vassiliev invariants
25
we can use the vacuum projection πbc without changing the result. By the
wheeling theorem,
πbcχ−1(x1 # . . . # xn) = πbc∂Ω(Υ−1(x1) ⊔· · · ⊔Υ−1(xk)).
Let yi = πbcΥ−1(xi). Each yi has at least one leg, since if the ∂−1
Ω
of Υ−1 =
∂−1
Ωχ−1 eats all the legs of χ−1xi, it also creates a vacuum diagram which is
killed by πbc. Then
πbc∂Ω(y1 . . . yk) = πbc⟨Ωa, ∆ab(y1 . . . yk)⟩a.
Let ∆abyi = (yi)a + zi; diagrams in z1 have at least one b leg. We see that
πbc⟨Ωa, (y1)a∆ab(y2 . . . yn)⟩a = πbc⟨(∂y1Ω)a, ∆ab(y2 . . . yk)⟩a
by Lemma 4.2
= 0
by Equation 13.
Therefore
πbc∂Ω(y1 . . . yk) = πbc(⟨Ωa, (y1)a∆ab(y2 . . . yk)⟩a + ⟨Ωa, z1∆ab(y2 . . . yk)⟩a)
= πbc⟨Ωa, z1∆ab(y2 . . . yk)⟩a
= · · ·
= πbc⟨Ωa, z1 . . . zk⟩a.
Each zi has at least one leg labeled b, so the product has at least k legs labeled
b which are the legs in the result.
5.3
Coiling the unknot. Proof of the Wheels theorem
The basic equation we will use to identify ν = Z(⟳) is “n · 0 = 0” from the
introduction: the n-fold connected cable of the unknot is the unknot with a
new framing. The connected cabling formula of Theorem 1 implies that
ψ(n)(ν # exp#( 1
2n
%)) = ν # exp#(n
2
%).
(14)
This equation is true for all n ∈Z, n > 0.
In each degree, each side is a
Laurent polynomial in n of bounded degree; therefore, the two sides are equal
as Laurent polynomials.
The RHS is a polynomial in n, so both sides are
polynomials (ie, have no negative powers of n.) Let us evaluate both sides at
n = 0. On the RHS, we get just ν. For the LHS, recall how ψ(n) acts in the
space B: it multiplies a diagram with k legs by nk (see Lemma 3.7).
Consider expanding the exponential exp#(%/2n) in the LHS of Equation 14.
In the term with (%)k , there is a factor of 1/nk from the coeﬃcient 1/2n. On
Geometry & Topology, Volume 7 (2003)


## Page 26


26
Bar-Natan, Le and Thurston
the other hand, by Lemma 5.3, the product has at least k legs, or k +1 if there
is a non-trivial contribution from ν. Since the overall power of n is n# legs−k,
when we evaluate at n = 0 the term ν does not contribute at all. Hence
ψ(n)(ν # exp#( 1
2n
%))|n=0 = ψ(n)(exp#( 1
2n
%))|n=0.
Now we want to pick out the term from (%)#k with exactly k legs. We can
do this computation explicitly using the wheeling map Υ. Alternatively, the
result must be a diagram of degree k and with k legs, hence ν = ν0, the part
of mapping degree 0. It was shown in Section 4 that the part of of mapping
degree 0 of Z(A) is Ωx ⊔exp⊔(|z
x). Dropping the central strand from
A leaves an
unknot, so Ω= ν0 = ν. This completes the proof of the Wheels theorem.
Exercise 5.4 Do the computation suggested above. Show that
χ−1(exp#(1
2
%)) = Ω⊔exp⊔(1
2 ⌢).
Hint 5.5 Use Lemma 6.3.
6
From the unknot to the Hopf link
By changing the framing on the unknot and cabling it, we can construct a Hopf
link. Using the results of Section 3 and the value of Z(⃝), we can compute the
invariant of the Hopf link from the invariant of the unknot. There are several
good formulas for the answer. An alternative exposition of the results of this
section can be found in [7].
Theorem 4 The framed Kontsevich integral of the Hopf link can be expressed
in the following equivalent ways:
Z( x
)y) =
(
Υx ◦Υy(exp( y⌢x))) · (Vacuum)
Υx(exp⊔( y⌢x)Ωx) · (Vacuum)
Z(Ay
x) = exp( y⌢x) ⊔Ωy,
for some elements (Vacuum) ∈A(∅).
In the last expression,
Ay
x is the (1, 1) tangle whose closure is the Hopf link,
with the bead labeled by y and the wire labeled by x. From this last equality
in Theorem 4, we can see exactly the map Φ from Section 4.
Geometry & Topology, Volume 7 (2003)


## Page 27


Applications of knot theory to Lie algebras and Vassiliev invariants
27
Corollary 6.1
Φ = Φ0 = χ ◦∂Ω.
Proof (of Theorem 4) We start by computing the Kontsevich integral of the
+1 framed unknot. In what follows we identify B and A using χ, and use ⊔
and # to denote the two diﬀerent products on B.
Z(⃝+1) = ν # exp#(1
2
%)
= ∂Ω
 ∂−1
Ω(Ω) ⊔exp⊔(∂−1
Ω( ⌢))

by Theorem 2
= πbc∂Ω(Ω⊔exp( ⌢)) .
by Equation 13
To pass to the Hopf link, we double Z(⃝+1). The following lemma, which is
obvious from the deﬁnition, tells us how ∂Ωinteracts with doubling. We use
ˆD as an alternate notation for ∂D so that we can use a subscript to indicate
which variable the diﬀerential operator acts on.
Lemma 6.2 For C, D ∈B with C strutless,
∆xy ˆC(D) = ˆCx(∆xyD) = ˆCy(∆xyD).
If we want to apply ∂−1
Ω
to both components of the Hopf link, we can compute
∂−2
Ω(Z(⃝+1)).
Lemma 6.3
πbc∂Ω(exp 1
2 ⌢) = Ω⊔exp(1
2 ⌢).
Proof
πbc∂Ω(exp(1
2 ⌢)) = πbc⟨Ωy, exp(1
2
x+y⌢x+y)⟩y
= πbc⟨Ωy, exp(1
2
x⌢x) exp( y⌢x) exp(1
2
y⌢y)⟩y
= πbc⟨∂exp( 1
2⌢)(Ω)y, exp( x⌢y)⟩y ⊔exp(1
2
x⌢x)
by Lemma 4.2
= πbc⟨Ωy, exp( y⌢x)⟩y ⊔exp(1
2
x⌢x)
by Equation 13
= Ω⊔exp(1
2 ⌢).
As a corollary, we see that
πbc∂−2
Ω(Z(⃝+1)) = exp(1
2 ⌢).
(15)
Geometry & Topology, Volume 7 (2003)


## Page 28


28
Bar-Natan, Le and Thurston
We now compute.
πbc∆xy(ˆΩ−2Z(⃝+2)) = πbc ˆΩ−1
x ˆΩ−1
y Z( +1
x
)+1
y )
by Lemma 6.2 and
formula (6)
= πbc∆xy(exp(1
2 ⌢))
by Equation 15
= exp( x⌢y) exp(1
2
x⌢x) exp(1
2
y⌢y).
Apply Υx ◦Υy to both sides. We see that
Z( +1
x
)+1
y ) = πbcZ( +1
x
)+1
y )
= πbcΥx ◦Υy(exp( x⌢y) ⊔exp(1
2
x⌢x) ⊔exp(1
2
y⌢y))
= πbcΥx ◦Υy(exp( x⌢y)) # exp#(1
2
%x) # exp#(1
2
%y)
so
Z( x
)y) = πbcΥx ◦Υy(exp( x⌢y)).
This is the ﬁrst equality of Theorem 4. For the second equality,
ˆΩy(exp( x⌢y)) = Ωx ⊔exp( x⌢y).
so
Z( x
)y) = πbcΥx(exp( y⌢x)Ωx).
For the last equality of the theorem, multiplicativity of Υ implies that
πbcΥx(exp( y⌢x)Ωx) = πbc(Υx(exp( y⌢x)) # Υx(Ωx))
= πbc(Υx(exp( y⌢x))) # χ(Ωx)
= χ(exp( y⌢x) ⊔Ωy) # χ(Ωx).
Hence we have
Z(Ay
x ) = Z( x
)y) # Ω−1
x
= exp( y⌢x) ⊔Ωy.
This completes the proof of Theorem 4.
Appendix
To show that Ω′ = Ω, one can use the following “Sawon’s identity [14]”:
⟨Ω′, ( ⌢)n⟩= ( 1
24
C)n.
(16)
Geometry & Topology, Volume 7 (2003)


## Page 29


Applications of knot theory to Lie algebras and Vassiliev invariants
29
Proof Proceed by induction on n. The result is trivial for n = 0.
⟨Ω′, ( ⌢)n⟩= ⟨Ω′, ⌢⊔( ⌢)n−1⟩
= ⟨∂⌣(Ω′), ( ⌢)n−1⟩
by Lemma 4.2
= 1
24
C ⟨Ω′, ( ⌢)n−1⟩
by Lemma 5.1 and explicit computation
=
 1
24
C
n
by induction
The following is well-known, see eg [8].
Lemma 6.4 In the Lie algebra sl2, with the invariant inner product ⟨x, y⟩=
−tr(xy), where the trace is taken in the adjoint representation, we have the
following relations:
⃝≡3
D ≡
H −
G
For example, apply the sl2 relations, we ﬁnd that that
C ≡6.
Lemma 6.5 Modulo the sl2 relations, ω2n ≡2( ⌢)n.
Proof Proceed by induction. This is a straightforward computation for n = 1.
For n > 1, compute as follows:
ω2n =
=
−
= ⌢⊔
= ⌢⊔ω2n−2.
Lemma 6.6 Modulo the sl2 relations, ⟨( ⌢)n, ( ⌢)n⟩= (2n + 1)!.
Proof Proceed by induction. The statement is trivial for n = 0. For n > 0,
the two ends of the ﬁrst strut on the left hand side can either connect to the
two ends of a single right hand strut or they can connect to two diﬀerent struts.
These happen in 2n and 2n · (2n −2) ways, respectively. (Note that there are
2n · (2n −1) ways in all of gluing these two legs.) We therefore have
= 2n ·
+ 2n · (2n −2) ·
and

(⌢)n, (⌢)n
=
 2n ⃝+2n · (2n −2)

(⌢n−1, (⌢)n−1
≡2n · (2n + 1)

(⌢n−1, (⌢)n−1
≡(2n + 1)!
by induction.
Geometry & Topology, Volume 7 (2003)


## Page 30


30
Bar-Natan, Le and Thurston
Proposition 6.7 One has Ω′ = Ω.
Proof By Lemma 6.5, we ﬁnd
Ω′ = exp(
X
n
a2nω2n) ≡exp(
X
n
2a2n(⌢)n).
Set f(x) = exp(2 P a2nxn) = P fnxn. Then by Lemma 6.6,
⟨Ω′, (⌢)n⟩≡⟨f(⌢), (⌢)n⟩= ⟨fn(⌢)n, (⌢)n⟩≡fn(2n + 1)!
=
 1
24
C
n
≡1
4n .
so
fn =
1
4n(2n + 1)!
f(x) = sinh(√x/2)
√x/2
exp
 
2
X
n
anxn
!
= sinh(x/2)
x/2
X
n
anxn = 1
2 log sinh(x/2)
x/2
.
References
[1]
Anton Alekseev, Eckhard Meinrenken, The non-commutative Weil alge-
bra, Invent. Math. 139 (2000) 135–172, arXiv:math.DG/9903052
[2]
Martin Andler, Alexander Dvorsky, Siddhartha Sahi, Kontsevich quan-
tization and invariant distributions on Lie groups, arXiv:math.QA/9910104
[3]
Dror Bar-Natan, On the Vassiliev knot invariants, Topology 34 (1995) 423–
472
[4]
Dror
Bar-Natan,
Non-associative tangles,
from:
“Geometric topology
(Athens, GA, 1993)”, AMS/IP Stud. Adv. Math. 2.1, Amer. Math. Soc. Provi-
dence, RI (1997) 139–183
[5]
Dror Bar-Natan, Stavros Garoufalidis, Lev Rozansky, Dylan P Thurs-
ton, Wheels, wheeling, and the Kontsevich integral of the unknot, Israel J. Math.
119 (2000) 217–237, arXiv:q-alg/9703025
[6]
Dror
Bar-Natan,
Stavros
Garoufalidis, Lev
Rozansky,
Dylan
P
Thurston, The Aarhus integral of rational homology 3-spheres II: Invari-
ance and universality, Selecta Mathematica, New Series, 8 (2002) 341–371,
arXiv:math.QA/9801049
Geometry & Topology, Volume 7 (2003)


## Page 31


Applications of knot theory to Lie algebras and Vassiliev invariants
31
[7]
Dror Bar-Natan, Ruth Lawrence, A rational surgery formula for the LMO
invariant, to appear in Israel J. Math. arXiv:math.GT/0007045
[8]
Sergei V Chmutov, Alexander N Varchenko, Remarks on the Vassiliev
knot invariants coming from sl2, Topology 36 (1997) 153–178
[9]
Pierre Deligne, letter to Dror Bar-Natan, (January 1996)
http://www.ma.huji.ac.il/~drorbn/Deligne/
[10]
Jacques Dixmier, Enveloping algebras, Graduate Studies in Mathematics 11,
Amer. Math. Soc. Providence, RI (1996)
[11]
Michel Duﬂo, Op´erateurs diﬀ´erentiels bi-invariants sur un groupe de Lie, Ann.
Scient. ´Ecole Norm. Sup. 10 (1977) 265–288
[12]
Roger Godement, Introduction `a la th´eorie des groupes de Lie, Publications
Math´ematiques de l’Universit´e Paris VII, Universit´e de Paris VII, U.E.R. de
Math´ematiques, Paris, (1982)
[13]
Vladimir Hinich, Arkady Vaintrob, Cyclic operads and algebra of chord
diagrams, arXiv:math.QA/0005197
[14]
Nigel Hitchin, Justin Sawon, Curvature and characteristic numbers of hy-
perk¨ahler manifolds, Duke Math. J. 106 (2001) 599–615
[15]
Maxim Kontsevich, Vassiliev’s knot invariants, Advances in Soviet Mathe-
matics 16 (1993) 137–150
[16]
Maxim Kontsevich, Deformation quantization of Poisson manifolds, I,
arXiv:q-alg/9709040
[17]
Andrew Kricker, Bill Spence, Ian Aitchison, Cabling the vassiliev invari-
ants, J. of Knot Theory and its Ramiﬁcations 5 (1996) 779–803
[18]
Thang T Q Le, Jun Murakami, Representations of the category of tangles
by Kontsevich’s iterated integral, Commun. Math. Phys. 168 (1995) 535–562
[19]
Thang T Q Le, Jun Murakami, The universal Vassiliev-Kontsevich invariant
for framed oriented links, Compositio Math. 102 (1996) 41–64
[20]
Thang T Q Le, Jun Murakami, Parallel version of the universal Kontsevich-
Vassiliev invariant, J. Pure and Appl. Alg. 212 (1997) 271–291
[21]
Thang T Q Le, Jun Murakami, Tomotada Ohtsuki, On a universal per-
turbative invariant of 3-manifolds, Topology 37-3 (1998) 539–574
[22]
Jens
Lieberum,
On Vassiliev invariants not coming from semisimple
Lie algebras, J. of Knot Theory and its Ramiﬁcations 5 (2000) 275–299,
arXiv:math.QA/9806064
[23]
Takuro Mochizuki, On the morphism of Duﬂo–Kirillov type, J. Geom. Phys.
41 (2002) 73–113
[24]
Jun Murakami, Tomotada Ohtsuki, Topological quantum ﬁeld theory for
the universal quantum invariant, Commun. Math. Phs. 188 (1997) 501–520
[25]
Dylan Thurston, Torus actions for the LMO invariant, in preparation
[26]
Pierre Vogel, Algebraic structures on modules of diagrams, Tech. report, Uni-
versit´e Paris VII (July 1995)
Geometry & Topology, Volume 7 (2003)

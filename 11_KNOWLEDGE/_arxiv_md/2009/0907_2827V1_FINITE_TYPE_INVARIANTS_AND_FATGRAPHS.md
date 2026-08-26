---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0907.2827v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 0907.2827v1_Finite_type_invariants_and_fatgraphs

> Source: 0907.2827v1_Finite_type_invariants_and_fatgraphs.pdf

> Pages: 39

---


## Page 1


arXiv:0907.2827v1  [math.GT]  16 Jul 2009
FINITE TYPE INVARIANTS AND FATGRAPHS
JØRGEN ELLEGAARD ANDERSEN, ALEX JAMES BENE, JEAN-BAPTISTE MEILHAN,
AND R. C. PENNER
Abstract. We deﬁne an invariant ∇G(M) of pairs M, G, where M is a 3-
manifold obtained by surgery on some framed link in the cylinder Σ×I, Σ is a
connected surface with at least one boundary component, and G is a fatgraph
spine of Σ. In eﬀect, ∇G is the composition with the ιn maps of Le-Murakami-
Ohtsuki of the link invariant of Andersen-Mattes-Reshetikhin computed rela-
tive to choices determined by the fatgraph G; this provides a basic connection
between 2d geometry and 3d quantum topology. For each ﬁxed G, this in-
variant is shown to be universal for homology cylinders, i.e., ∇G establishes
an isomorphism from an appropriate vector space H of homology cylinders
to a certain algebra of Jacobi diagrams. Via composition ∇G′ ◦∇−1
G
for any
pair of fatgraph spines G, G′ of Σ, we derive a representation of the Ptolemy
groupoid, i.e., the combinatorial model for the fundamental path groupoid of
Teichm¨uller space, as a group of automorphisms of this algebra. The space
H comes equipped with a geometrically natural product induced by stacking
cylinders on top of one another and furthermore supports related operations
which arise by gluing a homology handlebody to one end of a cylinder or to
another homology handlebody. We compute how ∇G interacts with all three
operations explicitly in terms of natural products on Jacobi diagrams and cer-
tain diagrammatic constants. Our main result gives an explicit extension of
the LMO invariant of 3-manifolds to the Ptolemy groupoid in terms of these
operations, and this groupoid extension nearly ﬁts the paradigm of a TQFT.
We ﬁnally re-derive the Morita-Penner cocycle representing the ﬁrst Johnson
homomorphism using a variant/generalization of ∇G.
1. Introduction
In [21], Le, Murakami and Ohtsuki constructed an invariant ZLMO(M) of a
closed oriented 3-manifold M from the Kontsevich integral Z (see §2.2) of a framed
link with k components, where Z takes values in the space A(
k) of Jacobi dia-
grams with core
k, a collection of k oriented circles (see §2.1.1). The Kontsevich
integral Z is universal among rational-valued Vassiliev invariants, i.e., any other
factors through it. The LMO invariant ZLMO(M) ∈A(∅) takes values in Jacobi
diagrams with empty core and arises as a suitably normalized post-composition of
Z with mappings
ιn : A(
k)→A(∅),
which are of key importance for LMO and eﬀectively “replace circles by sums of
trees” (see §3.1.1). The LMO invariant is universal among rational-valued ﬁnite
type invariants of integral and of rational homology spheres.
In [2], Mattes, Reshetikhin and the ﬁrst-named author deﬁned a universal Vas-
siliev invariant of links (see §2.5 for a partial review) in the product manifold Σ×I,
where Σ = Σg,n is a ﬁxed oriented surface of genus g ≥0 with n ≥1 boundary
components and I is the closed unit interval, which generalizes the Kontsevich in-
tegral. Actually, the determination of this AMR invariant depends on a certain
decomposition of the surface Σ into polygons.
1


## Page 2


2
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
In [30, 31, 32], the last-named author described an ideal cell decomposition of the
decorated Teichm¨uller space of a bordered surface in terms of marked fatgraphs G
embedded in Σ (see §2.3 for the deﬁnitions) and introduced the Ptolemy groupoid
Pt(Σ) and its canonical presentation in terms of Whitehead moves (see §5.2 for both
the moves and the presentation). A key point is that the natural quotient of Pt(Σ)
contains the mapping class group MC(Σ) of Σ as the stabilizer of any object.
A more speculative point (discussed further in §6) is that the Whitehead moves
which generate Pt(Σ) may themselves be interpreted as triangulated cobordisms of
triangulated surfaces
In fact, the speciﬁcation of a marked fatgraph G in Σ suﬃces to determine a
polygonal decomposition (see §2.4 for this construction) as required for the deﬁ-
nition of the AMR invariant. This is a basic connection between decorated Te-
ichm¨uller theory and ﬁnite type invariants which we exploit here.
Indeed, we deﬁne an invariant ∇G (see §3.1 for the deﬁnition and Theorem 3.1 for
its invariance) taking values in the space Ah of h-labeled Jacobi diagrams without
strut components (see §2.1.1 for the deﬁnitions), where h = 2g +n−1 is the rank of
the ﬁrst homology group of Σ if Σ = Σg,n has genus g and n boundary components.
Speciﬁcally, our invariant is deﬁned for any “cobordism” M, i.e., ∇G(M) is deﬁned
for any 3-manifold M = (Σ × I)L arising from Dehn surgery on a framed link
L ⊂Σ × I and for any marked fatgraph G in Σ. In fact, the fatgraph G determines
not only the polygonal decomposition necessary for an AMR invariant but also
other choices which are required for our new invariant (see §2.6 for these other
choices called systems of “latches” and “linking pairs”).
The invariant ∇G is deﬁned in analogy to ZLMO in the sense that it arises as a
suitably normalized post-composition of the AMR invariant determined by G with
ιn, so the AMR invariant (actually, a weakened forgetful version of it) plays for
us the role of the Kontsevich integral in LMO. We show (see Theorem 3.2) that
∇G is universal for so-called “homology cylinders”, which arise for surgeries along
a particular class of links called claspers (see §3.2 for the deﬁnitions of homology
cylinders and claspers).
Since ∇G is universal for homology cylinders, it induces an isomorphism
∇G : HΣ→Ah,
where HΣ is a quotient of the vector space freely generated by homology cylinders
over Σ (see §3.2.1 for the precise deﬁnition of HΣ).
It is this manifestation of
universality that has useful consequences for the Ptolemy groupoid Pt(Σ) since
given two marked fatgraphs G and G′ in Σ, there is the composition
∇G′ ◦∇−1
G : Ah →Ah.
For essentially formal reasons, this turns out to give a representation
ξ : Pt(Σg,1) →Aut(Ah)
of the Ptolemy groupoid in the algebra automorphism group of Ah.
There are several well-known and geometrically natural operations on H. Firstly,
there is the “stacking” induced by gluing homology cylinders top-to-bottom. Sec-
ondly, given a homology cylinder over the once-bordered surface Σg,1 and a genus
g homology handlebody (see §4.1.1 for the deﬁnition), we can take their “shelling
product” by identifying the boundary of the latter with the bottom of the former.
Thirdly and ﬁnally, we can glue two homology handlebodies along their boundaries
to get a closed 3-manifold in the spirit of Heegaard decompositions which is called
the “pairing” between the homology handlebodies (see §4.1.2 for details on all three
operations).


## Page 3


FINITE TYPE INVARIANTS AND FATGRAPHS
3
In §4.3 we explicitly deﬁne three algebraic maps
• : A2g × A2g→A2g, ⋆: A2g × Ag→Ag, and ⟨, ⟩: Ag × Ag→A(∅),
which respectively correspond (under conjugation with a normalized version of ∇G
explained in §3.3) to the stacking product, the shelling product, and the pairing (as
proved in Theorem 4.4). Furthermore, these operations are computed in terms of a
basic “concatenation product” ⊙(see §4.2) with three particular tangles Tg, Rg, Sg
(see §4.3 and Figure 4.5 for the deﬁnitions of these tangles) respectively corre-
sponding to the three operations; this gives a purely diagrammatic interpretation
and scheme of computation for each operation.
Our penultimate result relies on a groupoid representation
ρ : Pt(Σg,1)→A2g,
deﬁned by combining our invariant with a representation from [1], to extend the
LMO invariant of integral homology spheres to the Ptolemy groupoid in the follow-
ing sense. Let f be an element of the Torelli group of Σg,1 and let
G
W1
−−→G1
W2
−−→...
Wk
−−→Gk = f(G)
be a sequence of Whitehead moves representing f in the sense of decorated Te-
ichm¨uller theory (see §5.2). Our result then states that the LMO invariant of the
integral homology 3-sphere S3
f obtained by the Heegaard construction via f is given
by
ZLMO(S3
f) = ⟨v0, (ρ(W1) • ρ(W2) • · · · • ρ(Wk)) ⋆v0⟩∈A(∅),
where v0 is an explicit diagrammatic constant (see Theorem 5.4 for the precise
statement) and the operations are fully determined diagrammatically as discussed
before. This formalism shows the sense in which the LMO invariant extends to the
Ptolemy groupoid as a kind of weakened version of TQFT; whereas the Ptolemy
groupoid has not made contact with the LMO invariant previously, similar TQFT
phenomena and remarks are reported in [27, 9].
Finally (in §5.6), we use our invariant (actually, a variation/generalization ∇Ig
G
of ∇G, which takes values in Jacobi diagrams with core 2g intervals and depends
upon a “general system of latches” Ig, in order to associate to the Whitehead
move G
W
−→G′ the quotient J (W) = ∇Ig
G (Σg,1 × I)/∇Ig
G′(Σg,1 × I)) and deﬁne a
representation
J Y : Pt(Σg,1)→Λ3H1(Σg,1; Q)
which coincides with that deﬁned by Morita and Penner [26] to give a canonical
cocycle extension of the ﬁrst Johnson homomorphism [16]; see [7] for analogous
cocycles extending all of the higher Johnson homomorphisms. It thus seems rea-
sonable to expect that higher-order calculations should provide a corresponding
formula for the second Johnson homomorphism and, in light of [25], also for the
Casson invariant. In fact, one motivation for the present work was to investigate
whether the known extensions to the Ptolemy groupoid of the Johnson homomor-
phisms [26, 1, 7] might be special cases of a more general extension of ZLMO, cf.
[12, 14, 23].
We have learned here that ZLMO indeed extends to the Ptolemy groupoid, and in
particular have derived an explicit purely diagrammatic extension of ZLMO which
is “nearly a TQFT, ” but whose formulas are not particularly simple or natural
largely owing to their dependence upon certain combinatorial algorithms from [1].
On the other hand by a related construction (in §5.6.1), we have in the context
of ﬁnite type invariants derived an elegant and natural Ptolemy groupoid repre-
sentation which may give a simpler extension of ZLMO. We expect that there is
a precursor for this in the early days of development of [26, 1, 7], where explicit


## Page 4


4
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
unpleasant formulas were ultimately replaced by simpler and more conceptual ones;
see §6 for a further discussion.
Standard Notation. We shall ﬁx a compact connected and oriented surface Σ = Σg,n
of genus g ≥0 with n ≥1 boundary components, ﬁx a basepoint p ∈∂Σ and let
h := 2g + n −1 denote the rank of H1(Σ; Z). We shall often write 1Σ = Σ × I,
where I = [0, 1].
2. Definitions
2.1. Jacobi diagrams. We ﬁrst recall the spaces of diagrams in which the Kont-
sevich, LMO and our new invariants take values.
2.1.1. Deﬁnitions. A Jacobi diagram is a ﬁnite graph with only univalent and triva-
lent vertices, or a so-called “uni-trivalent” graph, such that each trivalent vertex
is equipped with a cyclic ordering of its three incident half-edges. In other words,
a Jacobi diagram is exactly a uni-trivalent “fatgraph” as discussed separately in
§2.3. The Jacobi degree or simply J-degree of a Jacobi diagram is half its number
of vertices.
Let S = {s1, ..., sm} be some ﬁnite linearly ordered set and be X a 1-manifold,
where we tacitly assume that X is compact and oriented and that its components
come equipped with a linear ordering. A Jacobi diagram G lies on (X, S) if the set
of univalent vertices of G partitions into two disjoint sets, where elements of one
of these sets are labeled by elements of S, and elements of the other are disjointly
embedded in X; X is called the core of the Jacobi diagram. As usual [3, 29] for
ﬁgures, we use bold lines to depict the 1-manifold X and dashed ones to depict
the Jacobi diagram (though fatgraphs will sometimes also be depicted with bold
lines), and we take the cyclic ordering at a vertex given by the counter-clockwise
orientation in the plane of the ﬁgure, which is used to determine the “blackboard
framing”.
Let A(X, S) denote the Q-vector space generated by Jacobi diagrams on (X, S),
subject to the AS, IHX and STU relations depicted in Figure 2.1. Consider the
=
−
IHX
+
AS
= 0
−
STU
=
Figure 2.1. The relations AS, IHX and STU.
respective vector subspaces Ak(X, S) and A≤k(X, S) generated by Jacobi diagrams
lying on (X, S) of J-degree k and ≤k, with respective projections of x ∈A(X, S)
denoted xk and x≤k. Abusing notation slightly, let A(X, S) furthermore denote
the J-degree completion of A(X, S) with its analogous projections to Ak(X, S) and
A≤k(X, S). The empty diagram in A(X, S) is often denoted simply 1.
We shall primarily be interested in certain specializations of this vector space:
• When S = ∅, we write simply A(X) = A(X, ∅). If X is the disjoint union
of m copies of S1, respectively, m copies of the unit interval, then A(X) is
also respectively denoted by A(
m) and A(↑m). There is an obvious surjective
“closing map”
π : A(↑m) →A(
m)
which identiﬁes to a distinct point the boundary of each component of X.


## Page 5


FINITE TYPE INVARIANTS AND FATGRAPHS
5
• When X = ∅, we write simply B(S) = A(∅, S), called the vector space of
S-colored Jacobi diagrams, and when S = {1, ..., m}, we write B(m) = B(S),
called the space of m-colored Jacobi diagrams.
In fact, A(X, S) has the structure of a Hopf algebra provided X = ∅,
, or ↑m, cf.
the next section.
When S = {s1, . . . , sm} is a linearly ordered set with cardinality m, there is a
standard [3] graded isomorphism
χS : B(S) →A(↑m),
called the Poincar´e–Birkhoﬀ–Witt isomorphism, which maps a diagram to the aver-
age of all possible combinatorially distinct ways of attaching its si-colored vertices
to the ith interval, for i = 1, . . . , m. When S = {1, ..., m}, we simply write χ = χS;
more generally, given a 1-manifold X with a submanifold X′ ⊂X which is isomor-
phic to and identiﬁed with ↑m, we have the isomorphism
χX′,S : A(X −X′, S) →A(X),
which arises by applying χS only to the S-labeled vertices.
The internal degree or i-degree of a Jacobi diagram is its number of trivalent
vertices. We call a connected Jacobi diagram of i-degree zero a strut, and we denote
by BY(m) the vector space generated by m-colored Jacobi diagrams without strut
components modulo the AS and the IHX relations. As these two relations (unlike
STU) are homogeneous with respect to the internal degree, BY(m) is graded by
the i-degree. The i-degree completion is also denoted BY(m) and is canonically
isomorphic to the J-degree completion.
In the rest of this paper, we shall use the simpliﬁed notation Am = BY(m).
2.1.2. Operations on Jacobi diagrams. There are several basic operations [3] on
Jacobi diagrams as follows:
First of all, disjoint union of 1-manifolds X1 and X2 gives a tensor product
⊗: A(X1) × A(X2)→A(X1 ⊔X2),
where the linear ordering on the components of X1 ⊔X2 is the lexicographic one
with components of X1 preceding those of X2. Secondly, if Vi ⊆∂Xi for i = 1, 2,
and V1 is identiﬁed with the reversal of V2 as linearly ordered sets of points to form
a new 1-manifold X from X1 and X2, then the stacking product
·: A(X1) × A(X2)→A(X)
arises by gluing together pairs of identiﬁed points and combining Jacobi diagrams
in the natural way.
Suppose that Y
⊆X is a connected component of a 1-manifold X.
Y (n)
denotes the union of n ordered parallel copies of Y .
The comultiplication map
∆Y : A(X) →A(Y (2) ∪X −Y ) is deﬁned as follows. Given a diagram D ∈A(X)
with c univalent vertices on Y , replace Y by Y (2) and take the sum of all 2c possible
ways of distributing these c vertices to the components of Y (2). More generally, we
can recursively deﬁne maps
∆(n)
Y
: A(X) →A(Y (n) ∪X −Y )
by ∆(n)
Y
= ∆Y (n−1)
1
◦∆(n−1)
Y
, where Y (n−1)
1
denotes the ﬁrst copy of Y in Y (n−1).
If Y ⊆X is a union of components, let Y denote the result of reversing the
orientation on Y . The antipode map
SY : A(X) →A(Y ∪X −Y )


## Page 6


6
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
is deﬁned by SY (D) = (−1)cD, where the diagram D ∈A(X) contains c univalent
vertices attached to Y , and D arises from D by reversing the orientation of Y .
2.2. The Kontsevich integral of framed tangles. Let M be a compact con-
nected oriented 3-manifold whose boundary is endowed with an identiﬁcation to
the boundary of the standard cube C := [0, 1]3, and let X be a 1-manifold possibly
with boundary. A tangle with core X in M is a proper embedding of X in M such
that all boundary points of X lie on the segments [0, 1] × 1
2 in the upper and lower
squares [0, 1]2 × {1} and [0, 1]2 × {0} of C. We shall identify such an embedding
with the (isotopy class relative to the boundary) of its image. A framed tangle is
a tangle together with a non-vanishing normal vector ﬁeld. A q-tangle is a framed
tangle enhanced with a “bracketing”, i.e., a consistent collection of parentheses
on each of the naturally linearly ordered sets of boundary points in the segments
[0, 1] × { 1
2} × {ε}; ε = 0, 1.
We deﬁne two operations on q-tangles in C as follows.
The tensor product
T ⊗T ′ of two q-tangles T and T ′ is obtained by horizontal juxtaposition and
natural bracketing, with T to the left of T ′ (and reparametrization of the ambient
cube). If the upper end of T coincides with the lower end of T ′, i.e., they coincide
as bracketed sets of dots, then the composition T · T ′ is obtained by stacking T ′ on
top of T (and reparameterizing the ambient cube).
A fundamental fact [29] is that any q-tangle in C can be (non-uniquely) de-
composed as a composition of tensor products of (oriented) copies of the elemen-
tary q-tangles I, X±, C± and Λ± of Figure 2.2 together with those obtained by
orientation-reversal on certain components.
(
)
(
(
)
)
(
)
X+
C+
C−
I
X−
Λ+
Λ−
Figure 2.2. The elementary q-tangles I, C±, X± and Λ±.
The framed Kontsevich integral Z(T ) of a q-tangle T with core X in the standard
cube C lies in the space A(X) of Jacobi diagrams [3, 29]. Insofar as Z(T · T ′) =
Z(T )·Z(T ′) and Z(T ⊗T ′) = Z(T )⊗Z(T ′), for any two tangles T, T ′, it is enough
to determine Z on any tangle by specifying its values on the elementary q-tangles
of Figure 2.2 by the fundamental fact. We set Z(I) = 1 ∈A(↑), and
(2.1)
Z(C±) = √ν,
where ν ∈A(
) ≃A(↑) is the Kontsevich integral of the 0-framed unknot (com-
puted in [5]).
Recall that ν is invariant under the antipode map and that projecting away the
non-strut components of χ(ν) produces zero.
Deﬁne
(2.2)
Z(X±) = exp
 ±1
2

= 1 +
∞
X
k=1
(±1)k
2kk!
 k,
where the kth power on the right-hand side denotes the diagram with k parallel
dashed chords. and set
(2.3)
Z(Λ±) = Φ±1,
where Φ ∈A(↑3) is the choice of an associator (see for example [29, Appendix D]).


## Page 7


FINITE TYPE INVARIANTS AND FATGRAPHS
7
While there are many associators that one may choose to deﬁne the Kontse-
vich integral, we shall restrict our choice to an even associator (see [20, §3] for a
deﬁnition), which necessarily satisﬁes
(2.4)
Z (r(T )) = r (Z(T )) ,
for any q-tangle T and for any mirror reﬂection r of its planar projection with
respect to any horizontal or vertical line [20]; moreover, if T (k)
i
is obtained by
taking k parallel copies of the ith component of a q-tangle T , then we have
(2.5)
Z(T (k)
i
) = ∆(k)
i
(Z(T )).
2.3. Fatgraphs. A fatgraph is a ﬁnite graph endowed with a “fattening”, i.e., a
cyclic ordering on each set of half-edges incident on a common vertex.
When
depicting a fatgraph in a ﬁgure, the fattening is given by the counter-clockwise
orientation in the plane of the ﬁgure. A fatgraph G determines a corresponding
“skinny surface” with boundary in the natural way, where polygons of 2k sides
corresponding to k-valent vertices of G have alternating bounding arcs identiﬁed
in pairs as determined by the edges of G. We shall be primarily concerned with
the case where such graphs are connected and uni-trivalent with only one univalent
vertex, and by a slight abuse of terminology, we shall call such a fatgraph a bordered
fatgraph. The edge incident on the uni-valent vertex of a bordered fatgraph is called
the tail.
Suppose that e is an oriented edge that points towards the vertex v of G. There
is a succeeding oriented edge e′ gotten by taking the oriented edge pointing away
from v whose initial half edge follows the terminal half edge of e. A sequence of
iterated successors gives an ordered collection of oriented edges starting from any
oriented edge called a boundary cycle of G, which we take to be cyclically ordered
and evidently corresponds to a boundary component of the associated skinny sur-
face. We shall call any subsequence of a boundary cycle of G a sector. By a once
bordered fatgraph, we mean a bordered fatgraph with only one boundary cycle,
which canonically begins from the tail.
Thus, the oriented edges of any once bordered fatgraph G come in a natural
linear ordering, namely, in the order of appearance in the boundary cycle starting
from the tail. For a connected bordered fatgraph G, we can also linearly order
the oriented edges by deﬁning the total boundary cycle as follows. Let the total
boundary cycle begin at the tail and continue until it returns again to the tail. If
every oriented edge has not yet been traversed, then there is a ﬁrst oriented edge e
in this sequence such that the oppositely oriented edge ¯e has not yet been traversed
by connectivity. We then extend the total boundary cycle by beginning again at
¯e and continuing as before until the boundary cycle containing ¯e has been fully
traversed. By iterating this procedure, we eventually traverse every oriented edge
of G exactly once. According to our conventions for ﬁgures, the total boundary
cycle is oriented with G on its left.
Finally, a marking of a bordered fatgraph G in a surface Σ = Σg,n of genus g
with n > 0 boundary components with basepoint p in its boundary, is a homotopy
class of embeddings G ֒→Σ such that the tail of G maps to a point q ̸= p on the
same component of the boundary of Σg,n as p and the complement Σ −G consists
of a disc (corresponding to the boundary component containing p) and n−1 annuli
(corresponding to the remaining boundary components). The relative version [32]
of decorated Teichm¨uller theory [30] shows that the natural space of all marked
fatgraphs in a ﬁxed bordered surface is identiﬁed with a trivial bundle over its
Teichm¨uller space.


## Page 8


8
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
2.4. The polygonal decomposition associated to a fatgraph. By a bigon,
square or hexagon in a surface Σ with boundary, we mean a (topologically) embed-
ded closed disc D2 ֒→Σ such that the intersection D2 ∩∂Σ is the union of one,
two or three disjoint closed intervals, respectively, called the bounding edges; the
closures of the components of the remainder of ∂D2 are called the cutting edges.
Given a marked bordered fatgraph G ֒→Σ, its corresponding skinny surface is
naturally diﬀeomorphic to Σ itself thus providing a polygonal decomposition
Σ = B ∪(∪iSi) ∪(∪jHj),
where each trivalent vertex corresponds to a hexagon Hj, each non-tail edge cor-
responds to a square Si, and the tail corresponds to a bigon B, such that the
intersection of any two of these components consists of a (possibly empty) union
of cutting edges. We refer to any Si × I or B × I as a box and to the box B × I
associated to the the tail of G as the preferred box. The faces of the boxes cor-
responding to cutting edges are called the cutting faces. This decomposition of Σ
is the polygonal decomposition associated to the fatgraph G marking in Σ and is
denoted PG.
Such a decomposition PG of Σ into 2-, 4-, and 6-gons, together with a speciﬁca-
tion of one bounding edge for each hexagon, provides suﬃcient data to deﬁne the
AMR invariant of [2], which is discussed in the next section. We call the speciﬁed
bounding edge of each hexagon (as well as the corresponding sector of G) its for-
bidden sector. One can check that for any choice of forbidden sectors for PG, any
framed link L in 1Σ can be isotoped in 1Σ and endowed with a bracketing of its
intersection with the cutting faces so that:
• For each square Si, the tangle LS
i := L ∩(Si × I) is a q-tangle in the cube
Si × I ∼= C as in §2.2. Similarly, the tangle LB := L ∩(B × I) is a q-tangle
in B × I.
• For each hexagon Hj, the tangle LH
j
:= L ∩(Hj × I) is a “trivial” q-
tangle in the sense that: there are no crossings of strands of LH
j ; no strand
of LH
j
connects the two edges of ∂Hj adjacent to the forbidden sector;
the bracketing of the intersection of L with the cutting face opposite the
forbidden sector is the concatenation of the bracketings for the other two
cutting faces in the natural way, cf. Figure 2.3.
• Pairs of bracketings corresponding to the two sides of a single cutting face
must coincide (as follows from their deﬁnition).
If a link satisﬁes these conditions, then we say that it is in admissible position
with respect to the polygonal decomposition PG associated to the marked fatgraph
G in Σ. An example is given in Figure 2.3, where we have labeled each forbidden
sector by ∗.
In fact, a marked fatgraph G in a surface Σ not only determines the required
polygonal decomposition PG of Σ as already discussed, it furthermore determines
a collection of forbidden sectors as follows.
By the greedy algorithm of [1], there is a canonical maximal tree τG in G built
by traversing the total boundary cycle of G starting from the tail and “greedily”
adding every traversed edge to τG provided the resulting graph is simply connected.
See Figure 2.3. Note that during this process, the corresponding subset of τG is
always a connected tree, and that the tail and all vertices of G are included in τG.
See [1, §3] for a detailed exposition of the greedy algorithm as well as its other
manifestations and applications.
Given a bordered fatgraph G, its generators are the edges in the complement
XG = G −τG of the maximal tree τG. Note that there is a natural linear ordering
on the set of generators, and each generator comes equipped with an orientation,


## Page 9


FINITE TYPE INVARIANTS AND FATGRAPHS
9
*
*
*
*
*
(
)
(
)
(
(
)
)
(
)
)
(
(
)
*
*
*
*
*
TG
G
PG
Figure 2.3. A fatgraph G marked in the twice-punctured torus
Σ1,2, the maximal tree τG, and a knot in admissible position with
respect to the polygonal decomposition PG.
where the ordering and orientation are determined as the ﬁrst encountered during
the traversal of the total boundary cycle.
By general principles about maximal trees, each vertex v of G is connected to
the tail by a unique embedded path in τG, and this path contains a unique edge
of G incident to v. As each hexagon of the decomposition of Σ corresponds to a
vertex of G, we may deﬁne the forbidden sector of a hexagon to be the one opposite
the edge contained in the path initiating from the corresponding vertex. See Figure
2.3.
Lemma 2.1. For any marked fatgraph G in Σ, the speciﬁed forbidden sectors and
the corresponding polygonal decomposition PG have the property that any link L in
Σ × I can be isotoped so that it intersects each box except the preferred one in a
trivial q-tangle.
Proof. For the purposes of this proof, we distinguish between the T-boxes, coming
from the edges of τG, and the G-boxes, coming from the edges of XG. To begin
the isotopy, for any G-box Sx containing a non-trivial tangle LS
x, isotope LS
x out
of Sx in either direction through the adjacent hexagon and then into an adjacent
T-box in a way which avoids producing arcs parallel to the forbidden sector of the
hexagon. This results in a link which is trivial in all G-boxes. Next, for any T-box
St containing a non-trivial tangle LS
t , similarly isotope LS
t into a neighboring T-box
which is closer to the tail via the path in the maximal tree τG. Note that such an
isotopy can be performed by our choice of forbidden sectors. Repeated application
of this last step results in a link which is trivial in all boxes except the preferred
one.
□
2.5. The AMR invariant. Andersen, Mattes and Reshetikhin [2] deﬁned a uni-
versal Vassiliev invariant of links in 1Σ = Σ × I, for Σ a surface with boundary,
which generalizes the Kontsevich integral; we shall only require a weak version
of their more general construction in this paper. These invariants depend on the
choice of a polygonal decomposition of the surface Σ together with other essentially
combinatorial choices in order to decompose the link into suitable sub-links (as for
the Kontsevich integral), and these choices (and more) are provided by a marked
fatgraph G in Σ as discussed in the previous section.


## Page 10


10
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
Let L(Σ; m) be the set of isotopy classes of oriented framed m-component links
in the thickened surface 1Σ. Fixing an even associator Φ ∈A(↑3) for the Kontsevich
integral Z once and for all and choosing a fatgraph G marking in Σ, we deﬁne the
AMR invariant
VG : L(Σ; m) →A(
m)
as follows. Given a link L ∈L(Σ; m) in admissible position, we apply Z to each q-
tangle LB and LS
i and map each trivial q-tangle LH
j to the empty Jacobi diagram in
A(↑|LH
j |), where |LH
j | is the number of connected components of LH
j . By choosing
an even associator, we do not need to distinguish between the top and the bottom
of the tangles LB and LS
i . We ﬁnally compose the resulting Jacobi diagrams as
prescribed by the polygonal decomposition PG associated to G to produce the
desired VG(L) ∈A(
m). The invariant depends on the choice of associator and
the fatgraph G. We shall also make use of natural extensions of this invariant to
certain framed tangles in 1Σ with endpoints on (∂Σ) × { 1
2}.
Our deﬁnition of VG diﬀers from [2] insofar as the original invariant takes values
in sums of diagrams on the surface, and we are post-composing with the map that
forgets the homotopy data of how these diagrams lie in the surface. This is of
course a dramatic loss of information, and we wonder what would be the induced
equivalence relation on L(Σ, m) assuming faithfulness of the original invariant [2],
which gives not only an isotopy invariant but also a universal Vassiliev invariant of
links in 1Σ. See §6 for a further discussion.
2.6. Linking pairs and latches. It is a satisfying point that a marked fatgraph G
suﬃces to conveniently determine the choices required to deﬁne the AMR invariant
VG(L) ∈A(
m) of an m component link L. The fatgraph furthermore determines
several other ingredients required for the deﬁnition of our new invariants as we
ﬁnally describe.
Let M be a closed 3-manifold, possibly with boundary. A linking pair in M
is a 2-component link K arising from an embedding of a standard torus into M,
where the ﬁrst component of K is the core of the torus, called the “longitude” of
the pair, and the second is a small null-homotopic 0-framed meridian of it, called
the “meridian” of the pair. We say a link L is disjoint from a linking pair K in M
if K is a linking pair in M −L.
In particular in S3, any two framed links L and L′ = L ⊔K, with K a linking
pair and L disjoint from K, are related by Kirby I and Kirby II moves. However,
this is no longer the case for 3-manifolds with boundary, and one must introduce a
third move, called Kirby III, where a linking pair may be added or removed from
a surgery link without changing the resulting 3-manifold. The precise statement
of the theorem of [33] is that surgery on two framed links in a 3-manifold with
boundary determine homeomorphic 3-manifolds if and only if the two links are
related by a ﬁnite composition of the three Kirby moves, which are sometimes
denoted simply KI-III.
Consider the ordered set of generators XG = {x1, ..., xh} of G. For each xi ∈XG,
the two paths from its endpoints to the tail in τG combine with xi to form a closed
loop based at the tail.
By construction, these based loops comprise a (linearly
ordered) set of generators for the fundamental group of Σ. Let li denote a simple
closed curve, representing the free homotopy classes of the ith loop, framed along
Σ × {1} and pushed oﬀin the I direction in 1Σ = Σ × I to height 1 −iǫ, for some
small ǫ > 0 ﬁxed independently of i, and pick a small 0-framed meridian mi of li.
This provides a collection of linking pairs
KG := ∪i(li ∪mi) ⊂1Σ,


## Page 11


FINITE TYPE INVARIANTS AND FATGRAPHS
11
called the system of linking pairs for 1Σ determined by the fatgraph G.
Lemma 2.2. Let G be a marked fatgraph in Σ and let L ⊂1Σ be a framed link
disjoint from KG. There exists a (non-unique) framed link L0 in 1Σ−KG contained
in the preferred box of PG, such that L ∪KG is equivalent under isotopy and Kirby
II moves to L0 ∪KG in 1Σ.
Such a representative for a framed link as in the previous lemma is called a reduced
representative.
Proof. By an isotopy supported in a neighborhood of the longitudes of KG, we
may arrange that the meridians are all contained in the preferred box. According
to Lemma 2.1, we may assume that L is admissible for G and intersects each
box except the preferred one in a trivial q-tangle. By Kirby II moves along the
meridians, we may arrange that each component of L lies in a diﬀerent slice of Σ×I
than the longitudes. We may furthermore arrange that the link does not meet the
box corresponding to any generator XG of G by sequentially, one generator at a
time, performing Kirby II moves along the longitudes of KG. Each Kirby II move
discussed thus far can and furthermore will be performed using bands for the slides
that lie within a single box. A ﬁnal isotopy of the resulting link produces the desired
link L0, and L ∪KG is equivalent under Kirby II and isotopy to L0 ∪KG in 1Σ by
construction.
□
One ﬁnal ingredient, which will serve as the core of the space A(↑h) in which
our invariant takes its values, is also determined by the generators of the fatgraph
G. In each box corresponding to a generator of G, consider an embedded arc in the
boundary of 1Σ as depicted in Figure 2.4. Such an arc, called a latch, is uniquely
Σ × {1}
S
S
Σ × {0}
Figure 2.4. A latch based at the box S in 1Σ. The right-hand
side is a projection in the I direction of Σ × I.
determined up to relative homotopy by which side of the box contains its endpoints,
and we determine this side as that corresponding to the ﬁrst oriented edge traversed
by the total boundary cycle of G. This collection of latches, one for each generator
of G, is called the system of latches IG determined by G, and they occur in a natural
orientation and linear order as before. (These standard latches determined by the
fatgraph admit a natural generalization given in §5.6.1, which is equally well-suited
to the construction given in the next section.)
3. The invariant ∇G
By a cobordism over Σ, we mean a 3-manifold (Σ × I)L obtained by surgery
on some framed link L in 1Σ. In particular, a cobordism over Σ comes equipped
with an identiﬁcation ∂(Σ × I) ≈∂(Σ × I)L, and two cobordisms are regarded as
equivalent if there is a diﬀeomorphism between them that is equivariant for this
identiﬁcation. Denote by C(Σ) the set of equivalence classes of cobordisms over Σ.


## Page 12


12
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
3.1. The invariant ∇G of cobordisms. Our construction of ∇G is modeled on
the LMO invariant ZLMO, where the role of the Kontsevich integral is now played
by the AMR invariant deﬁned in the previous section, and it relies on the LMO
maps ιn, which we next recall and slightly extend.
3.1.1. The map ιn. This map is a key tool for LMO and for us as well. It “re-
places circles by sums of trees” in the rough sense that a core circle component can
be erased by suitably summing over all trees spanning the endpoints of a Jacobi
diagram in that component.
More precisely, for any pair (m, n) of positive integers, any 1-manifold X with-
out circle components and any linearly ordered S = {s1, ..., sm}, ﬁrst deﬁne the
auxiliary map
jn : A(X, S) →A(X)
jn(D) =

On(< D >)
if D has exactly 2n vertices labeled with each color,
0
otherwise,
where < D > is the sum of all possible Jacobi diagrams obtained by pairwise
identifying univalent vertices of D having the same color, and On serially removes
all isolated loops, one at a time and each with a compensatory factor (−2n).
Given x ∈A(X ⊔
m), where X has no circle components and those of
m are
labeled by S = {1, . . . , m} in the natural way, choose an element y ∈A(X⊔↑m)
such that π(y) = x, and consider χ−1(y) ∈A(X, S), where χ is the Poincar´e–
Birkhoﬀ–Witt isomorphism.
The assignment ιn(x) :=
 jn(χ−1(y))

≤n yields a
well-deﬁned map
ιn : A(X ⊔
m) →A≤n(X).
Note that the deﬁnition given here is small reformulation of a simpliﬁed version
[18] of the original [21].
3.1.2. Deﬁnition of the invariant b∇G. Let M be a cobordism over Σ and let G be
a marked bordered fatgraph in Σ. G determines the polygonal decomposition PG
of Σ with its forbidden sectors, the system KG of linking pairs and the system IG
of latches in 1Σ, as well as the maximal tree τG and the system XG of generators.
Take a representative link L ⊂1Σ for M which is disjoint from IG and KG, so
that M = (1Σ)L = (1Σ)L∪KG. The linking number of two oriented components
K1, K2 of L in generic position is deﬁned as follows: project K1, K2 to Σ ≈Σ×{0}
and sum over all crossings of the projections a sign ±1 associated to each crossing,
where the sign is positive if and only if the projections of the tangent vectors to the
over- and under-crossing in this order agree with the given orientation on Σ. For
an arbitrary orientation on the link L ∪KG, we denote by σL∪KG
+
, and σL∪KG
−
, the
respective number of positive and negative eigenvalues of its linking matrix, which
are well-deﬁned independent of choices of orientation on components of L ∪KG.
Denote by VG the AMR invariant determined by PG and our choice of even
associator. Set
(3.1)
b∇G
n (L) :=
ιn( ˇVG(L ∪KG ∪IG))
ιn( ˇVG(U+))σ
L∪KG
+
ιn( ˇVG(U−))σ
L∪KG
−
∈A≤n(↑h),
where U± denotes the ±1-framed unknot in 1Σ, and ˇVG(γ) arises from VG(γ) for
any framed tangle γ by taking connected sum with ν on each closed component,
here using that {1, . . . , h} is in canonical bijection with XG.
Theorem 3.1. For each n ≥1, the quantity b∇G
n (L) deﬁned in (3.1) does not
change under Kirby moves KI-III and does not depend on the orientation of L.
Thus, b∇G
n (L) is an invariant of the cobordism (1Σ)L.


## Page 13


FINITE TYPE INVARIANTS AND FATGRAPHS
13
Proof. The invariance under Kirby I holds for the usual [29] reason: the change in
ιn
  ˇVG(L ∪KG ∪IG)

under introduction or removal of a ±1 framed unknot cancels
the change in the denominator from σL∪KG
±
.
The invariance under KII follows from precisely the same argument as for the
LMO invariant, which follows: First observe that an analogue of [21, Proposition
1.3] holds for the AMR invariant: if two links L and L′ in 1Σ diﬀer by a KII move,
then ˇVG(L) and ˇVG(L′) are related by a chord KII move, which is the move shown
in [21, Figure 6]. This is true because on one hand, ˇVG satisﬁes (2.5) since we have
chosen to work with an even associator, and on the other hand, we can always
assume (up to isotopy of the link) that each handleslide occurs along a band whose
projection to Σ is contained in a square Si in the polygonal decomposition PG. The
invariance under KII is then shown purely at the diagrammatic level, and comes as
a consequent property of the map ιn, whose construction is precisely motivated by
its behavior under a chord KII move; see [21, §3.1].
We note that using KII moves on the meridian components of KG, we can alter
any crossing of a longitude with any other link component, whence the value of the
invariant does not depend on the particular embedding of KG in M as long as L is
disjoint from KG and the homotopy classes of the longitudes of KG are preserved.
We ﬁnally show that invariance under KIII is guaranteed by the presence of the
system KG of linking pairs. Let L′ be obtained by adding a linking pair l ∪m to
the link L, where m is a 0-framed meridian of the knot l. Using the fact that the
set of homotopy classes provided by the longitudes of KG can be represented by
a system of generating loops for π1(Σ), we use KII moves to successively slide l
along longitude components of KG until we obtain a linking pair with longitude
null homotopic in 1Σ and possibly linked with meridians in KG. We can arrange by
isotopy that this linking pair is contained in a 3-ball in 1Σ and can assume by KII
moves that it is unlinked with the meridians of KG in that 3-ball; as noted earlier,
any such linking pair in a 3-ball can be removed using Kirby KI-II moves.
Independence from the choice of orientation on L follows from properties of the
map ιn just as for the LMO invariant; see [21, §3.1].
□
Also just as for the LMO invariant, we unify the series b∇G
n into a power series
invariant by setting
(3.2)
b∇G(M) := 1 +

b∇G
1 (L)

1 +

b∇G
2 (L)

2 + · · · ∈A(↑h)
in order to deﬁne a map
b∇G : C(Σ)→A(↑h).
In the case of a 2-disc Σ0,1 with the convention that a single edge for the tail is
allowed to be a fatgraph G, PG is a disk, and both KG and IG are empty, then the
invariant b∇G exactly coincides with the LMO invariant.
Recall that the space of Jacobi diagrams A(↑h) on h intervals is isomorphic
to the space B(h) of h-colored Jacobi diagrams via the Poincar´e–Birkhoﬀ–Witt
isomorphism. Furthermore, there is the projection of B(h) onto Ah := BY(h), and
we shall be equally interested in the value our invariant takes in the target space
Ah and hence deﬁne
∇G : C(Σ)→Ah,
where ∇G is the composition of b∇G with the projection A(↑h) ∼= B(h)→Ah. We
wonder whether the strut part of ˆ∇G(M) is related to the homology type of M.
3.2. Universality of ∇G for homology cylinders. Homology cylinders are a
special class of cobordisms which are important in the theory of ﬁnite type invari-
ants, cf. [15, 13]. In this section, we show that for any marked bordered fatgraph G


## Page 14


14
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
in the surface Σ, the invariant ∇G of cobordisms is universal among rational-valued
ﬁnite type invariants of homology cylinders over Σ in the sense of Goussarov and
Habiro [15, 13]. We ﬁrst recall the deﬁnition of these objects and review the theory
of ﬁnite type invariants before stating our universality result.
3.2.1. Claspers and ﬁnite type invariants of homology cylinders. In this section, we
brieﬂy review the Goussarov-Habiro theory of ﬁnite type invariants for compact
oriented 3-manifolds [13, 11, 15], which essentially generalizes Ohtsuki’s theory [28]
for integral homology spheres.
A clasper C in a 3-manifold M is an embedding in M of the skinny surface of
a (possibly disconnected) Jacobi diagram having a framed copy of S1 attached to
each univalent vertex. The copies of S1 are called the leaves of C, the trivalent
vertices are called the nodes of C, and we still call the 4-gons associated to the edges
of the graph the edges of C. We tacitly demand that each connected component of
a clasper contains at least one node. The number of connected components of C
is denoted |C|, and its degree is the total number of nodes. A connected clasper of
degree 1 is often called a Y-graph.
A clasper C of degree k in M determines a framed link L(C) in M, and surgery
along C means surgery along L(C). To construct L(C) from C, ﬁrst apply the edge
splitting rule shown in the left-hand side of Figure 3.1 until C becomes a disjoint
union of k Y -graphs. Next in a regular neighborhood, replace each Y -graph by a
6-component framed link as shown in the right-hand side of Figure 3.1.
;
Figure 3.1. The edge splitting rule and the surgery link associ-
ated to a Y -graph.
The link L(C) (that we sometimes also call a clasper) has 6k components if
C has degree k.
The 3k components coming from the k nodes are called the
Borromean components of L(C), and the remaining 3k components are called the
leaf components. We may also sometimes write simply MC for the surgery MC(L).
A homology cylinder over a compact surface Σ is a 3-manifold M = (1Σ)C that
arises from surgery on some clasper C in 1Σ. Note that 1Σ = Σ × I and hence
M = (1Σ)C comes equipped with embeddings i± : Σ →M with respective images
Σ±, such that:
(i) i+|∂Σ = i−|∂Σ;
(ii) ∂M = Σ+ ∪(−Σ−) and Σ+ ∩(−Σ−) = ±∂Σ±, where −Σ denotes reversal
of orientation on Σ;
(iii) i±
∗: H1(Σ; Z) →H1(M; Z) are identical isomorphisms.
In the special case where Σ has at most one boundary component, such a triple
(M, i+, i−) satisfying i-iii) conversely always arises from clasper surgery in 1Σ, cf.
[24].
The set of homology cylinders over Σ up to orientation-preserving diﬀeomor-
phism is denoted HC(Σ). There is a natural stacking product on HC(Σ) that arises
by identifying the top of one homology cylinder with the bottom of another and
reparametrizing the interval, i.e., by stacking one clasper on top of another. This
induces a monoid structure on HC(Σ) with 1Σ as unit element.


## Page 15


FINITE TYPE INVARIANTS AND FATGRAPHS
15
Let HΣ be the Q-vector space freely generated by elements of HC(Σ) with its
descending Goussarov-Habiro ﬁltration given by
(3.3)
HΣ ⊃F1(Σ) ⊃F2(Σ) ⊃...
where for k ≥1, Fk(Σ) denotes the subspace generated by elements
[M; C] :=
X
C′⊆C
(−1)|C′|MC′,
with M ∈HC(Σ), C a degree ≥k clasper in M, and the sum running over all
subsets C′ of the set of connected components of C.
A ﬁnite type invariant of degree ≤k is a map f : HC(Σ)→V , where V is a
Q-vector space, whose natural extension to HΣ vanishes on Fk+1(Σ). Denote by
Gk(Σ) the graded quotient Fk(Σ)/Fk+1(Σ) and let
HΣ := (degree completion of HΣ)/(∩kFk(Σ)).
A fundamental open question is whether ∩kFk(Σ) is trivial.
3.2.2. Universality of the invariant ∇G. It is known that the LMO invariant is
a universal invariant for homology spheres, i.e., every rational-valued ﬁnite type
invariant of homology spheres factors through it [19]. As noted in §3.1, our invariant
∇G coincides with the LMO invariant for Σ = Σ0,1, and in this section, we prove
the following generalization of the universality of LMO.
Theorem 3.2. Let Σ be a compact connected oriented surface with boundary and
G be a marked bordered fatgraph in Σ. Then the invariant ∇G is a universal ﬁnite
type invariant of homology cylinders over Σ.
As an immediate consequence we have
Corollary 3.3. For each marked fatgraph G in the surface Σ, there is a ﬁltered
isomorphism HΣ
∼
=
−→Ah induced by the universal invariant ∇G, where h = 2g +
n −1.
Indeed, the corollary is simply a re-statement of the theorem, and our proof will
proceed by exhibiting and checking the isomorphism in Corollary 3.3. This will
occupy the remainder of the section and begins with the deﬁnition of the inverse
map to ∇G.
3.2.3. The surgery map. The graded quotient Gk(Σ) is generated by elements [1Σ; C],
where C is a degree k clasper in 1Σ since
[M; C ∪C′] = [M; C] −[MC′; C],
where M ∈HC(Σ) and C∪C′ is a disjoint union of claspers in M with C′ connected.
Deﬁne a ﬁltration
Gk(Σ) = Fk,3k(Σ) ⊃Fk,3k−1(Σ) ⊃... ⊃Fk,1(Σ) ⊃Fk,0(Σ),
where Fk,l(Σ) is generated by elements [1Σ; C] with C a degree k clasper in M
having ≤l leaves. We also set
Gk,l(Σ) := Fk,l(Σ)/Fk,l−1(Σ).
Denote by BY
k (h) the i-degree k part of Ah = BY(h) and denote by BY
k,l(h) the
subspace generated by Jacobi diagrams of i-degree k with l univalent vertices. Note
that BY
k (h) = L
0≤l≤3k BY
k,l(h).
For any marked fatgraph G ֒→Σ and for any pair k, l of integers with k ≥1 and
0 ≤l ≤3k, we deﬁne a surgery map φG
k,l using claspers as follows. Let D ∈BY
k,l(h)
be some Jacobi diagram. For each univalent vertex v of D labeled by i, consider an
oriented framed knot in 1Σ which is a parallel copy of the longitude li of the system


## Page 16


16
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
KG of linking pairs. For each trivalent vertex of D, consider an embedded oriented
disk in 1Σ. These choices are made subject to the constraint that the resulting
annuli and disks are pairwise disjoint in 1Σ.
Connect these various embedded
annuli and disks by disjoint bands as prescribed by the diagram D in a way which
is compatible with their orientations and such that the cyclic order of the three
attached bands (given by the orientation) at each disk agrees with the cyclic order
at the corresponding trivalent vertex of D.
The resulting surface is a degree k
clasper with l leaves in 1Σ denoted C(D), and we set
φG
k,l(D) := [1Σ; C(D)] ∈Gk,l(Σ).
It follows from [10, Theorem 1] (see also [14]) that this assignment yields a
well-deﬁned surjection
φG
k,l : BY
k,l(h) →Gk,l(Σ).
The proof makes use of the calculus of claspers ; see [8, 11, 15, 29] for similar results.
3.2.4. Proof of Theorem 3.2. We need to prove the following two facts:
Fact (1) The i-degree ≤k part of ∇G is a ﬁnite type invariant of degree k.
Fact (2) For each pair (k, l) with k ≥1 and 0 ≤l ≤3k, the invariant ∇G induces
the inverse to the surgery map φG
k,l. More precisely, given a Jacobi diagram
D ∈BY
k,l(h), we have
(3.4)
∇G
k,l(φG
k,l(D)) = (−1)kD ∈BY
k,l(h),
where ∇G
k,l denotes the composition of ∇G with the projection onto BY
k,l(h).
In order to prove Fact (1), it is enough to consider an element [1Σ; C], where C
is a disjoint union of k Y-graphs in 1Σ (by construction using the edge splitting
rule) and prove that the minimal i-degree of ∇G([1Σ; C]) is k. To this end, we may
up to isotopy assume that there are k disjoint 3-balls contained in the boxes of the
polygonal decomposition PG corresponding to G which intersect C(D) as depicted
on the left-hand side of Figure 3.2. Note that
[1Σ; C] =
X
C′⊆C
(−1)|C′|(1Σ)C′ =
X
C′⊆C
(−1)|C′|(1Σ)L0(C′),
where L0(C′) is obtained from the link L(C) by replacing each Borromean linking
corresponding to a node of C −C′ by a trivial linking, so in particular L0(C′) is
Kirby equivalent to L(C′). In the computation of ∇G([1Σ; C]) at lowest i-degree, we
thus obtain for each node of C a trivalent vertex attached to the three corresponding
core components. This follows [29] from the property
Z(
) −Z(
) =
+terms with i-degree ≥2
(⋆)
of the Kontsevich integral and implies that the minimal i-degree of ∇G([1Σ; C]) is
k as required to prove (1).
Turning our attention now to (2), let D ∈BY
k,l(h) be a Jacobi diagram of i-
degree k with l univalent vertices and consider φG
k,l(D) = [1Σ; C(D)]. Denote by
J = 1
2(k + l) the Jacobi degree of D. As before, we can assume that there are k
disjoint 3-balls in the boxes of PG each of which intersects C(D) as depicted on the
left-hand side of Figure 3.2, and we can assume that there are a further h disjoint
3-balls that intersect the system KG of linking pairs as illustrated on the right-hand
side of the same ﬁgure.
Let us now compute the (relevant part of the) AMR invariant ˇVG of the al-
ternating sum φG
k,l(D). Since we are only computing the lowest i-degree part, the
contributions of all associators and ν’s can be ignored, see (5.6) and [5] respectively.


## Page 17


FINITE TYPE INVARIANTS AND FATGRAPHS
17
G
K
C(D)
Figure 3.2. Convenient positions for C(D) and KG.
In fact, we shall only need to consider the contributions arising from the trivalent
vertices (⋆) and struts coming from crossings, cf. (⋆⋆). Since the value of ∇G
k,l is of
J-degree J = k+l
2 , we must post-compose ˇVG

φG
k,l(D)

with the map ιJ to estab-
lish the formula in Fact (2). We need only focus on those terms of A(
6k+2h⊔↑h)
having exactly 2J vertices on each copy of S1 by deﬁnition of ιJ since only those
terms can contribute to the lowest i-degree part of ∇G(φG
k,l(D)).
We call the core components corresponding to Borromean (leaf, meridian, longi-
tude, latch respectively) components of L (C(D)) ∪KG ∪IG the Borromean (leaf,
meridian, longitude, latch respectively) cores of the Jacobi diagrams in the AMR
invariant ˇVG(L (C(D)) ∪KG ∪IG).
We ﬁrst consider contributions of the linking pairs and recall [29] that
...
i
Z(
) = exp(
) = P
i
1
i!
(⋆⋆)
.
Since the meridian component of a linking pair is isolated from every component
other than its corresponding longitude, it follows that all 2J vertices on the meridian
core must be the ends of distinct struts arising from the linking with this longitude.
The resulting connected diagram, which arises from (⋆⋆) with a coeﬃcient
1
(2J)!, is
called a Siamese diagram; see Figure 3.3.
Each Borromean component of L (C(D)) on the one hand forms a Borromean
linking with two other such components and, on the other hand links a leaf, cf.
Figure 3.2. On each Borromean core there is thus one vertex arising from (⋆), and
the remaining (2J −1) vertices are the ends of parallel struts arising from (⋆⋆) with
their opposite ends on a leaf core.
On each leaf core, there is thus only room for one additional vertex. Furthermore,
there is the following dichotomy on leaves of C(D):
(a) the leaf forms a positive Hopf link with another leaf of C(D) as in the
left-hand side of Figure 3.1;
(b) the leaf is a parallel copy of a longitude component li of KG, pushed oﬀso
that it is unlinked from the meridian mi, for some 1 ≤i ≤h.
For a type (a) leaf, the only possible contribution is the linking with another type
(a) leaf, which produces a strut by (⋆⋆). For a type (b) leaf, we must consider
several cases: either the strut comes from a crossing with another type (b) leaf, or
it comes from a crossing with a component of IG (since a crossing with the longitude
components of KG cannot contribute, as we have noted previously). In the ﬁrst
case, we thus have a strut joining two type (b) leaf cores, and we say that a Jacobi
diagram with such a strut is looped. In the second case, we have a strut joining the
leaf core to a latch core. A typical example is (partially) represented in Figure 3.3.
By construction, each type (b) leaf has linking number 1 with exactly one com-
ponent of IG and 0 with all others. The lowest i-degree terms in ˇVG([1Σ; C(D)])


## Page 18


18
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
meridian core
longitude core
siamese diagram
type (a) leaf cores
Borromean cores
latch core
type (b) leaf core
Figure 3.3. Typical lowest i-degree term.
are therefore a sum of looped diagrams plus a single Jacobi diagram with each type
(b) leaf core connected by a strut to a latch core.
We can now apply the map ιJ, and a computation shows that
...
ιk(
) = (−1)k−1(2k −1)!
2k −1
.
We ﬁnd two (and one respectively) such conﬁgurations for each edge incident
(and not incident) on a univalent vertex of D, and each comes from (⋆⋆) with a
coeﬃcient
1
(2J−1)!. This formula also shows that ιJ maps each Siamese diagram to
a factor (−1)J(2J)!, and there are h = 2g + n −1 such diagrams. We obtain that
ιJ

ˇVJ(φG
k,l(D)

is given by
(−1)(J−1)l+JhD +
 terms of i-degree k with less than l univalent vertices
terms of i-degree > k,
where the terms of i-degree k with less than l univalent vertices arise from the
looped Jacobi diagrams.
To conclude the computation, observe that the surgery link L (C(D)) ∪KG
satisﬁes σL(C(D))∪KG
+
= σL(C(D))∪KG
−
= 3k + h.
Since ιJ( ˇZ(U±)) = (∓1)J +
terms of i-degree ≥1, we therefore ﬁnd
ιJ( ˇVP (U+))σ
L(C(D))∪KG
+
ιJ( ˇVP (U−))σ
L(C(D))∪KG
−
= (−1)Jk+Jh+ terms of i-degree ≥1.
It follows that
∇G
k,l(φG
k,l(D)) = (−1)kD,
which concludes the proof of Theorem 3.2.
3.3. The rigid ∇r
G invariant. In this section, we introduce a modiﬁed “rigid”
version ∇r
G of our invariant ∇G, which is formulated in terms of the LMO invariant
of tangles and again depends on the choice of a marked fatgraph for Σ. In this
incarnation, ∇r
G shares properties with the invariant deﬁned in [8], which gives an
extension of the LMO invariant to so-called Lagrangian cobordisms between once-
bordered and closed surfaces. The invariant in [8] depends upon choices similar to
certain of those determined by a fatgraph discussed here, and it induces a universal
invariant for homology cylinders.
Roughly, it is deﬁned by ﬁrst “capping oﬀ”
a cobordism by attaching 2-handles along the boundary producing a tangle in a
homology ball and then computing the LMO invariant (actually, the equivalent
˚Arhus integral) of this tangle.


## Page 19


FINITE TYPE INVARIANTS AND FATGRAPHS
19
3.3.1. The rigid ∇r
G invariant for homology cylinders. Let G be a marked fatgraph
in the bordered surface Σ. Recall that the bigon B in the polygonal decomposition
PG of §2.4 gives rise to the preferred box in 1Σ, which is identiﬁed with the standard
cube C = [0, 1]3 so that the upper face f = [0, 1]2 × {1} is the cutting face. Denote
by F a collar neighbourhood f × [0, ε] of f in (1Σ −C), where f is identiﬁed with
f × {0}, and ﬁx the standard points si :=
i
2h+1 ∈[0, 1], for 1 ≤i ≤2h.
Consider in 1Σ the system of linking pairs KG = ⊔h
i=1(li ⊔mi) determined by G
as in §2.6. We assume that each li lies in the surface Σ×{
i
h+1} ⊂1Σ, for 1 ≤i ≤h
and meets ∂F only at the points sj ×{
i
h+1}×{ε}, for j = i, i+1, that each meridian
mi intersects ∂F only at the points sj × { 1
2} × {0}, again for j = i, i + 1, and that
(mi ∪li) ∩(F ∪C) is in the standard position depicted in Figure 3.4 up to isotopy.
We say that KG is in rigid position in 1Σ in this case.
f = f × {ε}
f × {0}
si+1 × 1
2
li
mi
si × 1
2
[0, 1] × 1
2
si+1 ×
i
h+1
si ×
i
h+1
f × [0, ε]
[0, 1] ×
i
h+1
li
mi
si
si+1
si+1
si
C
F
Figure 3.4. System of linking pairs in rigid position.
Suppose that M = (1Σ)L is a cobordism over Σ for some framed link L in 1Σ. By
Lemma 2.2, we can use the system of linking pairs KG in rigid position to obtain
a reduced representative L0 which lies in the preferred box C.
Letting IG denote the system of latches determined by G (cf. §2.6), cut 1Σ along
f in order to split IG ∪KG ∪L0 into two q-tangles
(3.5)
TG := (IG) ∪(KG ∩(1Σ −C))
and
(KG ∩C) ∪(L0),
where the bracketing (••)

(••)
 (••) · · · ((••)(••)) · · ·

is taken on both sets of
boundary points. Set
(3.6)
b∇G,r
n
(L) :=
ιn( ˇZ((KG ∩C) ∪L0))
ιn( ˇZ(U+))σL
+ιn( ˇZ(U−))σL
−∈A≤n(↑h),
where we make use of the same notation as for (3.1), and deﬁne the rigid b∇r
G
invariant of M to be
(3.7)
b∇r
G(M) := 1 +
 b∇G,r
1
(L)

1 +
 b∇G,r
2
(L)

2 + · · · ∈A(↑h).
As before, we deﬁne the corresponding rigid ∇r
G invariant as the composition of
b∇r
G with the projection A(↑h)→Ah.
In the next section, we prove the following:
Theorem 3.4. ∇r
G is an invariant of homology cylinders and induces a graded
isomorphism
∇r
G : HΣ →Ah
for any marked fatgraph G in Σ.
Though ∇r
G is deﬁned for any cobordism over Σ, we can at present only prove it is
an invariant of homology cylinders; cf. the next section.


## Page 20


20
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
Remark 3.5. Recall that the LMO invariant extends naturally to q-tangles in homol-
ogy balls. This is done in a similar manner to the extension to links in 3-manifolds
[21], and more generally to framed graphs in 3-manifolds [27], via a formula similar
to (3.6). Using this extension, we can reformulate (3.7) as
b∇r
G(M) := ZLMO(BM, γM) ∈A(↑h),
where (BM, γM) denotes the result of surgery on (C, KG ∩C) along the link L0.
Note that BM is indeed a homology ball since M is a homology cylinder.
3.3.2. Proof of Theorem 3.4. For h ≥1, let Th,0 = N
h C+ be the q-tangle in C
obtained by horizontal juxtaposition of h copies of the q-tangle C+ of Figure 2.2,
with bracketing of the form (••)

(••)
 (••) · · · ((••)(••)) · · ·

. See Figure 4.2 and
set
T (h) := {(C, Th,0)Γ : Γ is a clasper in C disjoint from Th,0}.
Let QT (h) denote the vector space freely generated by elements of T (h). In analogy
to (3.3), we have the Goussarov-Habiro ﬁltration
QT (h) ⊃F1(h) ⊃F2(h) ⊃...
where Fk(h) denotes the subspace generated by elements [(B, γ); Γ] with (B, γ) ∈
T (h) and with Γ a degree ≥k clasper in B disjoint from γ, for k ≥1. This ﬁltration
serves to deﬁne a notion of ﬁnite type invariants for these objects as in §3.2.1.
Proposition 3.6. For any h ≥1, the LMO invariant induces a universal ﬁnite
type invariant for tangles in T (h).
Proof. The proof follows closely that of Theorem 3.2. In particular as in §3.2.3,
we deﬁne for each pair (k, l) with k ≥1 and 0 ≤l ≤3k a surgery map φr
k,l as
follows. Let D ∈BY
k,l(h). For each i-labeled univalent vertex, pick a parallel copy
of a small 0-framed meridian of the ith component of Th,0, and for each trivalent
vertex of D, pick an embedded oriented disk in C. Connect these meridians and
disks by disjoint bands as prescribed by the diagram D to obtain a degree k clasper
with l leaves denoted Cr(D). The assignment φr
k,l(D) := [(C, Th,0); Cr(D)] yields
a well-deﬁned surjective map
φr
k,l : BY
k,l(h) →Gk,l(h),
where Gk,l(h) is deﬁned as in §3.2.3. The rest of the proof follows from the analogues
of facts (1) and (2) of §3.2.4, which hold according to exactly the same arguments.
□
As a consequence, we have a graded isomorphism
ZLMO : T (h)
∼
=
−→Ah
induced by the LMO invariant, where T (h) denotes the quotient
 degree completion of QT (h)

/ (∩k≥1Fk(h)) .
The inverse isomorphism, denoted φr, is induced by the surgery maps φr
k,l.
We can now proceed with the proof of Theorem 3.4. For any marked fatgraph
G in Σ, deﬁne a map
JG : T (h) →HC(Σ)
as follows. If (B, γ) = (C, Th,0)Γ ∈T (h), where Γ is some clasper in C disjoint from
Th,0, then JG(B, γ) is the homology cylinder obtained by stacking the tangle TG
deﬁned in (3.5) above (B, γ) and performing surgery along the 2h-component link
resulting from this stacking. We shall give in Remark 4.3 a purely diagrammatic
version of the map JG for any marked bordered fatgraph G. As a generalization of
the Milnor-Johnson correspondence of Habegger [14], we wonder if JG is invertible;


## Page 21


FINITE TYPE INVARIANTS AND FATGRAPHS
21
if so, then it would follow that the rigid invariant ∇r
G is indeed an invariant not
just of homology cylinders but also of general cobordisms over Σ.
Since JG(∩k≥1Fk(h)) ⊂(∩kFk(Σ)), there is an induced map
JG : T (h) →HΣ,
which is surjective according to Lemma 2.2.
Lemma 3.7. The map JG is a graded isomorphism.
This implies Theorem 3.4 since (3.7) can thus be rewritten as ∇r
G = ZLMO◦(JG)−1.
Proof of Lemma 3.7. For each pair (k, l) with k ≥1 and 0 ≤l ≤3k, consider the
surjective map Jk,l
G
: Gk,l(h) →Gk,l(Σ) induced by JG. It suﬃces to show that
Jk,l
G
is a graded isomorphism, which follows from commutativity of the following
diagram:
BY
k,l(h)
φr
k,l

φG
k,l
$J
J
J
J
J
J
J
J
J
Gk,l(h)
Jk,l
G
/ Gk,l(Σ).
To see that this diagram is in fact commutative, let D ∈BY
k,l(h) and Cr(D) ⊂C be
the clasper obtained by the construction explained in the proof of Proposition 3.6,
whence φr
k,l(D) = [(C, Th,0); Cr(D)]. Applying Jk,l
G amounts to stacking the tangle
TG on (Th,0 ∪Cr(D)) ⊂C. The result of this stacking is the system of linking pairs
KG in rigid position, together with a clasper with l leaves in 1Σ, each leaf being a
disjoint copy of a 0-framed meridian of the component mi of KG, for some i. By a
Kirby KII move, we can slide each of these leaves along the corresponding longitude
component li of KG and denote by Γ the resulting clasper in 1Σ. It follows from
the deﬁnition of the surgery map φk,l (see §3.2.3) that [1Σ; Γ] = φk,l(D) in Gk,l(Σ)
as required.
□
4. Diagrammatic formulations of topological gluings
Throughout this section, ﬁx a non-negative integer g as well as a closed genus g
surface Σg which we identify with the boundary of the standard genus g handlebody
Hg := Σ0,g+1 × I, where Σ0,g+1 is a ﬁxed disc in the plane with basepoint on its
boundary having g holes ordered and arranged from left to right. We also ﬁx a
genus g surface with one boundary component Σg,1 and identify Σg = Σg,1 ∪D2
with the closed surface obtained by capping oﬀΣg,1 with a disc D2, so that ∂Σg,1 ⊂
(∂Σ0,g+1) × I.
4.1. Topological operations.
4.1.1. Homology handlebodies. A genus g homology handlebody is a 3-manifold M
with boundary a closed genus g surface Σ such that the inclusion Σ ֒→M induces a
surjection in integral homology with kernel a maximal integral isotropic subgroup
Λ ⊂H1(Σg; Z); in this deﬁnition, we always require an identiﬁcation of the bound-
ary Σ of M with the ﬁxed surface Σg and call Λ the Lagrangian of the handlebody.
For example, Hg is a homology handlebody, whose associated Lagrangian subspace
Λst we call the standard Lagrangian of Σg.
We consider two homology handlebodies v1 and v2 equivalent if there is a diﬀeo-
morphism of v1 to v2 which restricts to the identity on Σg under the corresponding
identiﬁcations. Denote by V (Σg, Λ) the set of equivalence classes of homology han-
dlebodies with Lagrangian Λ.


## Page 22


22
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
By a result of Habegger [14], any two homology handlebodies are related by
clasper surgeries if and only if they have the same induced Lagrangian. In partic-
ular, any genus g homology handlebody with Lagrangian Λst can be obtained by
clasper surgery in Hg. In other words, we have
V (Σg, Λst) = HC(Σ0,g+1).
4.1.2. Stacking, shelling and pairing. We have already deﬁned in (§3.2.1) the nat-
ural stacking product for homology cylinders, which induces a map
·: HΣg,1 × HΣg,1 →HΣg,1,
and we next similarly introduce two further products
∪ι : HΣ0,g+1 × HΣ0,g+1→HΣ0,1,
∗: HΣg,1 × HΣ0,g+1 →HΣ0,g+1.
The pairing ∪ι on the vector space HΣ0,g+1 is deﬁned as follows. Consider the
standard orientation-reversing map ι: Σg→Σg which “takes longitudes to merid-
ians” and vice versa so that gluing two copies of Hg along their boundaries via
ι produces the standard 3-sphere S3. By gluing two arbitrary handlebodies with
boundary Σg along this map (i.e., their adjunction space collapsing ﬁbers to points),
we obtain a closed 3-manifold and refer to this operation as their pairing. Observe
that the pairing of two homology handlebodies in HΣ0,g+1 is an integral homology
3-sphere, or equivalently, a homology cylinder over Σ0,1, as required.
The shelling product ∗is deﬁned as follows. Given a genus g homology handle-
body H and a homology cylinder (N, i+, i−) over Σg in the notation of §reffti, we
can glue the boundaries via the identiﬁcation ∂H = i−(Σg) ⊂∂N to obtain a new
genus g homology handlebody with boundary i+(Σg). Similarly, given the identiﬁ-
cation Σg = Σg,1∪D2, we can glue a homology cylinder M over Σg,1 to the homology
handlebody H to obtain a 3-manifold with boundary i+(Σg,1) ∪(S1 × I) ∪D2. By
gluing a cylinder D2 × I along (S1 × I) ∪D2 in the standard way, we obtain a new
genus g homology handlebody M ∗H.
To illustrate the shelling product, let {ai, bi}g
i=1, respectively, {hi}g
i=1, be the
collection of disjoint loops in Σg,1 × I, respectively, in the genus g handlebody Hg,
shown in Figure 4.1. Note that each collection induces a basis for the ﬁrst homology
group of the corresponding 3-manifold. The images of these loops under the shelling
product Hg = (Σg,1 × I) ∗Hg, which we still denote by ai, bi and hi, are shown on
the right-hand side of the ﬁgure. In particular, note that each bi is null-homotopic
in Hg, and satisﬁes |lk(bi, hi)| = 1.
a1
b1
h1
a1
b1
h1
Hg
Σg,1 × I
Figure 4.1. The shelling (Σg,1 × I) ∗Hg and the curves ai, bi, hi.
The main goal of this section is to provide explicit diagrammatic formulas in
§4.3 for these three topological operations.


## Page 23


FINITE TYPE INVARIANTS AND FATGRAPHS
23
4.2. A general gluing formula. We now introduce another more basic operation,
which is a key tool for manipulating our diagrammatic formulas.
4.2.1. The contraction ◦of labeled Jacobi diagrams. Let D ∈B(S) and D′ ∈B(S′)
be diagrams, for some ﬁnite sets S and S′, and let R ⊆S∩S′. Deﬁne the contraction
product D ◦R D′ ∈B ((S ∪S′) −R), as follows. If R = ∅or if for some x ∈R the
number of x-colored vertices of D and D′ is not the same, then set D◦RD′ = 0, and
otherwise, D ◦R D′ is deﬁned to be the sum of all possible ways of gluing pairwise
the univalent vertices of D and D′ labeled by the same element of R. By linear
extension, this deﬁnes a contraction map
◦R : B(S) × B(S′) →B ((S ∪S′) −R) ,
which we will call the contraction over R.
Let −s ∈A (↑, {s}) be the Jacobi diagram consisting of a single strut with one
vertex on ↑and one vertex colored by s. Set
λ(s, u, v) := χ−1
{v} (exp(−s) · exp(−u)) ∈B({s, u, v}),
where the exponential is with respect to the stacking product of Jacobi diagrams.1
If S, U and V respectively denote the sets {s1, ..., sn}, {u1, ..., un} and {v1, ..., vn},
then deﬁne
Λn(S, U, V ) := ⊔n
i=1λ(si, ui, vi) ∈B(S ∪U ∪V ).
Proposition 4.1. [4, Proposition 5.4] (see also [8, Claim 5.6]) For n ≥1, let
D ∈A(X∪↑n) and E ∈A(X′∪↑n), where X and X′ are two (possibly empty)
1-manifolds. Let D · E ∈A(X ∪X′∪↑n) be obtained from the stacking product of
A(↑n). Then
χ−1
↑n,V (D · E) = Λn(S, U, V ) ◦S∪U

χ−1
↑n,S(D) ⊔χ−1
↑n,U(E)

= χ−1
↑n,S(D) ◦S Λn(S, U, V ) ◦U χ−1
↑n,U(E)
∈A(X ∪X′, V ).
4.2.2. A gluing formula for the LMO invariant of tangles. For m, n ≥0, denote by
Tm,n the q-tangle in C represented in Figure 4.2. In the natural way, we consider
the tangles Tm,0 and T0,n as subtangles of Tm,n.
...
...
C
n+1
n+m
1
2
n
Figure 4.2. The q-tangle Tm,n, where the bracketing on both sets
of
boundary
points
is
of
the
form
(••)

(••)
 (••) · · · ((••)(••)) · · ·

.
Consider the q-tangle γ′ = Tm,n ∪L′ in C, where L′ is some framed link disjoint
from Tm,n. For any element D ∈A(↑n), deﬁne
(4.1)
D
k⊙γ′ = χ−1
S D ◦S
ιkjV
k

Λn(S, U, V ) ◦U χ−1
T0,n,U ˆZ(C, γ′)

ιk( ˇZ(U+))σ+(γ′)ιk( ˇZ(U−))σ−(γ′)
∈A(↑m),
1 As explained in [4, Proposition 5.4] and [8, Remark 4.8], λ(s, u, v) can also be deﬁned in
terms of the Baker-Cambell-Hausdorﬀseries.


## Page 24


24
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
and set
(4.2)
D ⊙γ′ := 1 +
X
k≥1
(D
k⊙γ′)k ∈A(↑m),
where
• ˆZ(C, γ′) is obtained from ˇZ(C, γ′) by taking connected sum of ν with each
component of T0,n ⊂γ′.
• σ±(γ′) := σL′∪T0,n
±
denotes the number of positive and negative eigenvalues
of the linking matrix of the tangle (T0,n ∪L′) ⊂γ′.
• The map jV
k : B(S ∪V ) →B(S) is deﬁned by applying jk to the V -colored
vertices, as in the deﬁnition of §3.1.1, and leaving the S-colored vertices
unchanged.
It will be useful to deﬁne an analogous product for n-colored Jacobi diagrams,
still denoted by ⊙. For E ∈B(n), we set
(4.3)
E ⊙γ′ := χ−1 (χ(E) ⊙γ′) ∈B(m).
We now use this product to give a gluing formula for the LMO invariant. Let
γ = Tn,0 ∪L be a q-tangle in C, where L is a framed link disjoint from Tn,0 so
that b = CL is an integral homology ball (in particular, L can be chosen to be a
clasper); see Figure 4.3. Set
(b, t) = (C, Tn,0)L ∈T (n).
L
L’
1
...
m
n
1
...
...
1
n
L’
1
...
m
...
1
n
L
glue
γ
γ
’
Figure 4.3. The tangles γ and γ′, and their composition.
Let On denote the n component link arising as the composition of Tn,0 and T0,n,
so that γ · γ′ = L′ ∪On ∪L ∪Tm,0.
Lemma 4.2. Let γ and γ′ be two q-tangles as decribed above.
Then the LMO
invariant of
(B, T ) := (C, Tm,0)L∪On∪L′
is given by
ZLMO(B, T ) = ZLMO(b, t) ⊙γ′ ∈A(↑m).
Proof. Let δ denote the tangle in b obtained from γ · γ′ by surgery along the link
L. By deﬁnition, the degree k part of ZLMO(B, T ) is given by
ZLMO
k
(B, T ) =
 
ιL′
k ιOn
k ιL
k
  ˇZ(C, γ · γ′)

(ιk( ˇZ(U+))σL′∪On∪L
+
(ιk( ˇZ(U−))σL′∪On∪L
−
!
k
,
where ιOn
k , respectively, ιL′
k and ιL
k , denote the map ιk applied only to the copies of
S1 corresponding to On ⊂γ · γ′, respectively, to L′, L ⊂γ · γ′, as in the deﬁnition
of §3.1.1.


## Page 25


FINITE TYPE INVARIANTS AND FATGRAPHS
25
By following (the proof of) [21, Theorem 6.6], we have
ZLMO
k
(B, T ) =
 
ιL′
k ιOn
k
 ZLMO(b, δ)

(ιk( ˇZ(U+))σL′∪On
+
(ιk( ˇZ(U−))σL′∪On
−
!
k
,
and
ιL′
k ιOn
k
 ZLMO(b, δ)

=

ιL′
k jV
k χ−1
On,V
 ZLMO(b, δ

≤k
from the deﬁnition of ιk. By Proposition 4.1,
χ−1
On,V
 ZLMO(b, δ)

= χ−1
S ZLMO(b, t) ◦S Λn(S, U, V ) ◦U χ−1
T0,n,U ˆZ(C, γ′).
Note that the only copies of S1 in the core of the above quantity are those corre-
sponding to the link L′, so that applying ιL′
k just amounts to applying the map ιk
of §3.1.1. Finally, note that by our assumption on the link L, the linking matrix of
L′ ∪On is just the linking matrix of the tangle (T0,n ∪L′) ⊂γ′, so σL′∪On
±
= σ±(γ′)
as required.
□
Remark 4.3. A similar formula holds in general for the invariant ∇G of q-tangles in
cobordisms over Σ. The only requirement is that such a tangle decomposes as the
stacking of some q-tangle with an element of T (n), for some integer n (such as γ
in Lemma 4.2). In this case, there is a formula similar to (4.1), but the Kontsevich
integral is replaced with the AMR invariant VG.
To illustrate, we give a diagrammatic version of the map JG of §3.3.2, which
allows us to express ∇G(M) in terms of ∇r
G(M) for a homology cylinder M. Recall
that TG denotes the tangle IG ∪(KG ∩(1Σ −C)) in 1Σ −C, cf. (3.5). The subtangle
mi ∩(1Σ −C) ⊂TG is just a copy of the tangle T0,h, and we have the formula
(4.4)
∇G(M) = ∇r
G(M) ⊙TG ∈Ah,
for any homology cylinder M over Σ.
Though it is deﬁned more generally for
cobordisms, this expresses our universal invariant ∇G for homology cylinders in
terms of LMO since ∇r
G(M) can be computed in terms of the the LMO invariant
of a q-tangle in a homology ball as in Equation 3.6.
4.3. Diagrammatic formulas for the topological gluings. In this section, we
ﬁnally give the explicit formulas for the pairing, stacking and shelling products.
4.3.1. Model for preferred structures. We begin by choosing preferred marked bor-
dered fatgraphs in each of the surfaces Σg,1 and Σ0,g+1. The speciﬁed fatgraphs
each have the property that the greedy algorithm produces a line segment as max-
imal tree; such “linear chord diagrams” are studied in [6]. The ﬁrst, denoted Cg,
consists of g edges attached along the line interval TCg, creating g isolated humps
as shown in Figure 4.4. The second fatgraph, which we call a genus g symplectic
fatgraph2 and denote by Cg, consists of 2g edges which appear along the interval
TCg in g isolated overlapping pairs as illustrated in Figure 4.4; see Figures 4.6 and
4.7 for the skinny surfaces respectively associated to C2 and C1. We choose the
Cg
Cg
α1
β1
βg
αg
α1
αg
Figure 4.4. Preferred marked fatgraphs Cg ֒→Σ0,g+1 and Cg ֒→Σg,1.
2Note that this notation diﬀers from that used in [7].


## Page 26


26
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
standard markings of Cg in Σg,1 and Cg in Σ0,g+1 as shown in Figure 4.4, where we
have the identiﬁcation of Σg = Σg,1 ∪D2 with the boundary of Hg = Σ0,g+1 × I.
4.3.2. Diagrammatic pairing, stacking and shelling. Let g ≥1 be an integer and
deﬁne the three q-tangles in C
Tg = T0,2g ∪LT ,
Sg = T2g,4g ∪LS
and
Rg = Tg,3g ∪LR,
where LT , LS and LR are framed links as shown Figure 4.5.
...
...
...
LT
LS
Tg
R g
S g
LR
Figure 4.5. The q-tangles Tg, Sg and Rg.
Given Jacobi diagrams D, D′ ∈Ag and E, E′ ∈A2g, deﬁne
⟨, ⟩: Ag × Ag →A(∅),
• : A2g × A2g →A2g,
⋆: A2g × Ag →Ag
by
⟨D, D′⟩:= (D ⊗D′) ⊙Tg,
E • E′ := (E ⊗E′) ⊙Sg ,
E ⋆D := (E ⊗D) ⊙Rg.
Theorem 4.4. Let H and H′ be two genus g homology handlebodies, and let M, M ′
be two homology cylinders over Σg,1. Then
ZLMO(H ∪ι H′) = ⟨∇r
Cg(H), ∇r
Cg(H′)⟩,
(4.5)
∇r
Cg(M · M ′) = ∇r
Cg(M) • ∇r
Cg(M ′),
(4.6)
∇r
Cg(M ∗H) = ∇r
Cg(M) ⋆∇r
Cg(H).
(4.7)


## Page 27


FINITE TYPE INVARIANTS AND FATGRAPHS
27
Proof. Let K, K′ be framed links in 1Σ0,g+1 such that H = (1Σ0,g+1)K and H′ =
(1Σ0,g+1)K′, and let L, L′ be framed links in 1Σg,1 such that M = (1Σg,1)L and
M ′ = (1Σg,1)L′.
Denote by Kg and Kg, the system of linking pairs in rigid position in 1Σ0,g+1 and
1Σg,1, respectively, induced by the preferred marked bordered fatgraphs Cg and Cg
deﬁned in §4.3.1. Let K0, K′
0, L0, and L′
0 be the reduced representatives of K,
K′, L and L′ respectively with respect to the linking pairs Kg and Kg as provided
by Lemma 2.2. See the left-hand side of Figures 4.6 and 4.8. Note that surgery
along these links in the preferred box always gives a homology ball since we are
considering homology cylinders.
As to Equation (4.5), it follows from straightforward Kirby calculus that the
integral homology sphere H ∪ι H′ is obtained from S3 by surgery along the framed
link depicted on the right-hand side of Figure 4.6. We see that this link can be
...
T
T
0
K
K’0
0
K
K’0
H
H’
H
H’
g
Kg
K
Figure 4.6. Links for the pairing in the case g = 2.
decomposed as (TH ⊗TH′) · Tg, where TH and TH′ are the q-tangles in C deﬁned
in (3.5). The tangles γ = TH ⊗TH′ and γ′ = Tg indeed satisfy the hypotheses of
Lemma 4.2, from which the result follows.
As to Equation (4.6), the stacking product M · M ′ is obtained from 1Σg,1 by
surgery along L∪L′, where L and L′ respectively occur in the lower and upper half
of 1Σg,1. By Lemma 2.2, we can use the system of linking pairs Kg in rigid position
to obtain a reduced representative, as shown in the left-hand side of Figure 4.7.
g
S
T M M’
.
T M M’
.
L’0
0
L
T
T
0
L
L’0
Kg
M
M’
Figure 4.7. Link and tangle for the stacking product in the case
g = 1.
Following (3.5), denote by TM·M′ the q-tangle in C obtained by cutting 1Σg,1 along
the cutting face of the preferred box. This tangle, shown on the left-hand side of
Figure 4.7, is Kirby equivalent to the tangle shown on the right-hand side of the
ﬁgure, which can be decomposed as (TM ⊗ˇTM′) · Sg. The result then follows from
Lemma 4.2 with γ = TM ⊗ˇTM′ and γ′ = Sg.


## Page 28


28
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
Finally for Equation (4.7), consider the link in 1Σ0,g+1 obtained from L and K
under the shelling product 1Σg,1 ⋆1Σ0,g+1.
As in the previous case, we can use
Lemma 2.2 and the system of linking pairs Kg in 1Σ0,g+1 to to obtain a reduced
representative. One can check using Figure 4.1 and Kirby calculus that the tangle
TM∗H obtained by cutting 1Σ0,g+1 along the cutting face of the preferred box is the
tangle represented on the right-hand side of Figure 4.8. Since the latter decomposes
T
TM*H
TM
g
R
L0
K0
K0
L0
M
H
H
Kg
Kg
Figure 4.8. Link and tangle for the shelling product in the case
g = 1.
as (TM ⊗TH)·Rg, and γ = TM ⊗TH and γ′ = Rg satisfy the hypotheses of Lemma
4.2, the result follows.
□
Remark 4.5. We can use (4.6) to deﬁne a multiplicative version of the rigid ∇r
G
invariant. This is done by renormalizing the invariant by a factor which uses the
tangle Rg and a relative version of the contraction product ⊙. A similar renormal-
ization appears in §4.4 of [8].
5. Ptolemy Groupoid Representations
In this section, we exploit the dependence of our invariant ∇G on the fatgraph
G to construct representations of mapping class groups and their subgroups.
5.1. Classical actions of subgroups of the mapping class group. The map-
ping class group MC(Σ) of a compact orientable surface Σ, possibly with boundary
∂Σ non-empty, is the group of isotopy classes relative to ∂Σ of orientation-preserving
self-diﬀeomorphisms of Σ which ﬁx ∂Σ pointwise. MC(Σ) acts naturally on the
integral homology groups of Σ, and we deﬁne the Torelli group I(Σ) of Σ to be the
subgroup of MC(Σ) acting trivially. Given a Lagrangian subspace Λ ⊂H1(Σg; Q)
for a closed surface Σg, we deﬁne the Lagrangian preserving mapping class group
MC(Λ) = {ϕ ∈MC(Σg) : ϕ∗(Λ) = Λ}. In particular, it is not diﬃcult to see that
the Torelli group is the intersection of all the Lagrangian preserving mapping class
groups.
Consider the standard Heegaard decomposition of S3 = Hg ∪ι Hg, where ι is
the orientation-reversing involution. Any mapping class f ∈I(Σg,1) gives rise to
a corresponding mapping class f ∈I(Σg) by capping oﬀand extending by the
identity. We may construct the homology sphere S3
f = Hg ∪ι◦f Hg by re-gluing
the handlebodies using ι ◦f. More generally for any Heegaard decomposition of
a homology 3-sphere M = H ∪ι H′ into two genus g homology handlebodies, we
obtain a similar map
(5.1)
f 7→Mf = H ∪ι◦f H′.


## Page 29


FINITE TYPE INVARIANTS AND FATGRAPHS
29
Composing with the LMO invariant of the resulting homology 3-sphere Mf, we
obtain a map I(Σg,1)→A(∅), which is of some importance [25].
This kind of action of the Torelli group on the set of integral homology spheres
with Heegaard splitting can equivalently be described in the context of homol-
ogy cylinders via the mapping cylinder construction and the topological products
described in Section 4.1.2.
Indeed, the mapping cylinder of ϕ ∈MC(Σ), de-
noted C(ϕ) = (1Σ, ϕ, Id), is a special case of cobordism over Σ, and restricting to
ϕ ∈I(Σ), we obtain a homomorphism of monoids
(5.2)
I(Σ)→HC(Σ),
ϕ 7→C(ϕ).
Using this construction, we may reformulate (5.1) as f 7→Mf = H ∪ι (C(f) ∗H′),
thus making precise the sense in which (5.2) describes an action on the set of integral
homology spheres.
More generally, we can view the homomorphism (5.2) as an action of I(Σ) on
the vector space generated by homology cylinders over Σ by stacking, i.e.,
M 7→M · C(ϕ)
for M ∈HC(Σ) and ϕ ∈I(Σ). Similarly, we have the conjugation action
M 7→C(ϕ) · M · C(ϕ−1)
of ϕ ∈MC(Σ) on homology cylinders over Σ, where if M = (1Σ)L is a homology
cylinder over Σ, then
(5.3) C(ϕ) · (1Σ)L · C(ϕ−1) = C(ϕ) · C(ϕ−1) · (1Σ)ϕ−1(L) = (1Σ)ϕ−1(L) ∈HC(Σ).
Analogously, we have a shelling action
H 7→C(ϕ) ∗H
of the Lagrangian preserving subgroup MC(Λ) on the set V (Σg, Λ) of genus g
homology handlebodies with Lagrangian Λ.
Recall that the preferred marked bordered fatgraphs Cg and Cg deﬁned in §4.3.1
induce isomorphisms
∇Cg : HΣg,1
∼
=
−→A2g
and
∇Cg : V (Σg, Λst) = HΣ0,g+1
∼
=
−→Ag,
and using these, we thus obtain representations
ξ : MC(Σg,1)→Aut(A2g)
and
ζ : MC(Λst)→Aut(Ag)
respectively induced by conjugation and the shelling action. This section relies on
the fundamental relationship between fatgraphs and mapping class groups provided
by the Ptolemy groupoid of decorated Teichm¨uller theory to describe these various
actions in a purely combinatorial way.
5.2. Ptolemy Groupoid. We shall restrict for convenience to surfaces with only
one boundary component.
Given a bordered fatgraph G, deﬁne the Whitehead
move W on a non-tail edge e of the uni-trivalent fatgraph G to be the modiﬁcation
that collapses e to a vertex of valence four and then expands this vertex in the
unique distinct way to produce the uni-trivalent fatgraph G′; see Figure 5.1. We
shall write either W : G→G′ or G
W
−→G′ under these circumstances.
Not only do markings of fatgraphs evolve in a natural way under Whitehead
moves, so that we can unambiguously speak of Whitehead moves on marked fat-
graphs, but also there is a natural identiﬁcation of the edges of G and G′. Fur-
thermore, there are three families of ﬁnite sequences of Whitehead moves, called
the involutivity, commutativity, and pentagon relations, which leave invariant each
marked fatgraph G, cf. [31, 26].


## Page 30


30
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
Figure 5.1. A Whitehead move of a fatgraph superimposed on
top of the diagonal exchange of its dual triangulation.
The Ptolemy groupoid Pt(Σ) of a surface Σ with boundary is deﬁned as the
groupoid with objects given by marked bordered uni-trivalent fatgraphs G ֒→Σ
and morphisms given by sequences of Whitehead moves modulo the involutivity,
commutativity, and pentagon relations.3
Pt(Σ) provides a MC(Σ)-equivariant combinatorial model of the fundamental
path groupoid of the decorated Teichm¨uller space of Σ, cf. [30, 31, 32]. As such,
given any “point” in Pt(Σ), i.e., any marked bordered fatgraph G ֒→Σ, each
mapping class ϕ ∈MC(Σ) is represented by a unique morphism from G to ϕ(G)
in Pt(Σ), where ϕ(G) is the marked fatgraph that arises by postcomposing the
marking G ֒→Σ of G with ϕ.
For any marked bordered fatgraph G ֒→Σ, we may thus think of MC(Σ) as being
a set of equivalence classes of paths beginning at the point G ֒→Σ and ending at a
fatgraph combinatorially equivalent to G but potentially with a diﬀerent marking
in Σ. In this way, we get a presentation of the mapping class group of Σ:
Theorem 5.1 ([32]). For a surface Σ with boundary, the mapping class group
MC(Σ) has a presentation with generators given by sequences of Whitehead moves
on marked fatgraphs in Σ beginning and ending at combinatorially isomorphic fat-
graphs. The relations in this groupoid are given by identifying two sequences if they
diﬀer by a ﬁnite number of insertions or deletions of involutivity, commutativity,
and pentagon relations.
In a similar way, the Torelli group I(Σ) (and indeed each term of the Johnson
ﬁltration [16]) likewise admits an analogous combinatorial presentation as in [26].
By a representation Pt(Σ) →K of the Ptolemy groupoid in some group K,
we mean a composition-preserving map Mor(Pt(Σ))→K from the morphisms of
Pt(Σ). In other words, a representation of Pt(Σ) is a morphism that assigns an
element of K to each Whitehead move such that the composition is trivial for the
involutivity, commutativity, and pentagon relations.
5.3. The explicit Ptolemy action on Ah. Our ﬁrst representation of Pt(Σ)
captures the dependence of ∇G on the choice of marked bordered fatgraph G ֒→
Σ giving a representation as automorphisms of an appropriate space of Jacobi
diagrams extending the conjugation action of the mapping class group on homology
cylinders.
Recall from Corollary 3.3 that for a genus g surface Σ with n ≥1
boundary components, any marked bordered fatgraph G ֒→Σ provides a graded
isomorphism
∇G : HΣ
∼
=
−→Ah,
where h = 2g + n −1, as a consequence of the universality of the invariant ∇G.
Thus, for any marked bordered fatgraphs G and G′, we get isomorphisms ∇G and
3The term “Ptolemy groupoid” is sometimes used to refer to the groupoid whose objects are
MC(Σ)-orbits of uni-trivalent fatgraphs and whose morphisms are MC(Σ)-orbits of pairs of such
with the natural composition. We prefer to call this the mapping class groupoid since it gives a
combinatorial model for the fundamental path groupoid of Riemann’s moduli space.


## Page 31


FINITE TYPE INVARIANTS AND FATGRAPHS
31
∇G′ of HΣ with Ah. As a formal consequence, we obtain an explicit representation
of the Ptolemy groupoid:
Theorem 5.2. The map
(G
W
−→G′) 7→∇G′ ◦∇G
−1.
deﬁnes a representation of the Ptolemy groupoid acting on Ah
ˆξ : Pt(Σ)→Aut(Ah).
For Σ = Σg,1, this representation extends the representation ξ : MC(Σg,1)→Aut(A2g)
induced by the conjugation action in the sense that for any sequence of Whitehead
moves Cg
W1
−−→· · ·
Wk
−−→ϕ(Cg) representing ϕ ∈MC(Σg,1), we have the identity
ˆξ(W1) ◦· · · ◦ˆξ(Wk) = ξ(ϕ).
Before giving the proof, we ﬁrst give the following topological interpretation of
the automorphism associated to a morphism from G to G′ in Pt(Σ). Given an
element in Ah, we can pull it back via ∇G−1 to an element of HΣ, represented
by a formal series L of framed links in 1Σ in admissible position with respect to
the polygonal decomposition PG. We then evolve G by a sequence of Whitehead
moves to a new marked fatgraph G′, and isotope the links in L accordingly to put
them in admissible position with respect to the new polygonal decomposition PG′.
Evaluating ∇G′ on the resulting series of links then provides a new element of Ah.
Proof. The fact that the above action deﬁnes a representation of the Ptolemy
groupoid follows easily since any sequence of Whitehead moves representing a triv-
ial morphism of Pt(Σ) begins and ends at identical marked fatgraphs and thus must
give the trivial action.
For any link L ⊂1Σ, we have ∇G
n (L) = ∇ϕ(G)
n
(ϕ(L)) by construction, so that
∇ϕ(G)((1Σ)L) = ∇G((1Σ)ϕ−1(L)).
Thus by (5.3) for any M ∈HΣ, we have
ξ(ϕ)(∇G(M)) = ∇G(C(ϕ) · M · C(ϕ−1)) = ∇ϕ(G)(M),
and setting G = Cg, the result follows.
□
5.4. The Ptolemy groupoid action on handlebodies. A similar extension of
the shelling action ζ arises as follows. By Lemma 7.4 of [1], there is an algorithm
which produces a representation
Pt(Σg,1)→MC(Λst)
of the Ptolemy groupoid extending the identity on MC(Λst). Thus, we obtain:
Proposition 5.3. Let Σg be a closed genus g surface. Fix a disc in Σg and let Σg,1
be its complement. Then we have an explicit algorithmically deﬁned representation
ˆζ : Pt(Σg,1)→Aut(Ag)
which extends the shelling action ζ : MC(Λst)→Aut(Ag).
Owing to its dependence on the complicated algorithms in [1], the action on Ag
obtained in this way is more complicated than the action on Ah described in the
previous section.


## Page 32


32
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
5.5. Extension of the LMO invariant to the Ptolemy groupoid. In this
section, we give a kind of Ptolemy groupoid action on ﬁnite type invariants of
integral homology spheres which extends the usual action of the Torelli group via
Heegaard decomposition. More precisely, we give a Ptolemy groupoid action on
ﬁnite type invariants of homology cylinders over Σ which extends the stacking
action of I(Σ) on HΣ, and which in the case of Σ = Σg,1 induces a map from
Pt(Σg,1) to A(∅) extending the analogous map of the Torelli group I(Σg,1).
We begin by recalling Corollary 7.1 and Theorem 8.1 of [1], which together give4
that any choice of a marked bordered fatgraph G ֒→Σg,1 determines a representa-
tion
ˆidG : Pt(Σg,1)→I(Σg,1)
of the Ptolemy groupoid which extends the identity homomorphism of I(Σg,1).
Let ˆid = ˆidCg be the representation provided by the marked fatgraph Cg ֒→Σg,1
deﬁned in §4.3.1. Deﬁne a representation of the Ptolemy groupoid of Σg,1
ρ : Pt(Σg,1)→A2g,
to be a composition-preserving map, where the target space is imbued with the
stacking product •, by setting
ρ(W) := ∇r
Cg

C( ˆid(W))

.
Theorem 5.4. The representation ρ : Pt(Σg,1)→A2g of the Ptolemy groupoid of
Σg,1 provides an extension of the LMO invariant of integral homology spheres to
the Ptolemy groupoid in the following sense: Let f ∈Ig,1 and let
G
W1
−−→G1
W2
−−→...
Wk
−−→Gk = f(G)
be a sequence of Whitehead moves representing f. Let M = H ∪ι H′ be a genus g
Heegaard splitting of an integral homology sphere M. Then the LMO invariant of
the integral homology 3-sphere Mf = H ∪ι◦f H′ is given by
ZLMO(Mf) = ⟨v, (ρ(W1) • ρ(W2) • · · · • ρ(Wk)) ⋆v′⟩,
where v = ∇r
Cg(H) ∈Ag and v′ = ∇r
Cg(H′) ∈Ag.
Proof. Since ˆid extends the identity homomorphism of I(Σg,1), we therefore have
ˆid(W1) ◦ˆid(W2) ◦... ◦ˆid(Wk) = f, hence MW1 · MW2 · ... · MWk = C(f), where
MW denotes C( ˆid(W)). Since Mf = H ∪ι (C(f) ∗H′), the formula follows from
Theorem 4.4.
□
Considering the map f 7→S3
f induced by the standard Heegaard decomposition
of S3, Theorem 5.4 shows that for a sequence G
W1
−−→G1
W2
−−→...
Wk
−−→Gk = f(G) of
Whitehead moves representing f, we have
ZLMO((S3)f) = ⟨v0, (ρ(W1) • ρ(W2) • · · · • ρ(Wk)) ⋆v0⟩,
where the diagrammatic constant v0 = ∇r
Cg(Hg) ∈Ag can easily be computed
as follows. By deﬁnition, we have ∇r
Cg(Hg) = ZLMO(C, Tg,0), where Tg,0 is the
q-tangle of Figure 4.2. By (2.1), the Kontsevich integral Z(Tg,0) ∈A(↑g) of this
tangle is thus given by including a √ν on each copy of ↑. It follows that
v0 = ⊔g
i=1(χ−1
{i}
√ν) ∈Ag,
where an explicit formula for ν is given in [5].
4The proof in [1] relies on a sequence of algorithms, beginning with the greedy algorithm, which
produces a sequence of Whitehead moves taking a given fatgraph to a symplectic one, followed
by an algorithm which manipulates the homological information associated to each edge of the
symplectic fatgraph; this last algorithm apparently has a paradigm in K-theory.


## Page 33


FINITE TYPE INVARIANTS AND FATGRAPHS
33
5.6. Extension of the ﬁrst Johnson homomorphism. In [26], a representation
of the Ptolemy groupoid was introduced using the notion of an H-marking of a
fatgraph G and shown to be an extension of the ﬁrst Johnson homomorphism τ1
to the Ptolemy groupoid. In this section, we show how a variation of the invariant
∇G can be used to realize this extension.
5.6.1. General latches. Let G ֒→Σ be a marked bordered fatgraph in a surface Σ.
We begin by introducing a generalized notion of a system of latches in 1Σ and thus
of the invariant ∇G. In fact, the main property of the system of latches IG we used
so far in this paper, besides the fact that it is determined by the fatgraph G, is that
it provides a dual basis in homology.
We deﬁne a general latch for G as an embedded interval in the boundary of
Σ×I with endpoints lying in (∂Σ)×{ 1
2} such that it can be isotoped relative to its
boundary to be in admissible position with respect to the polygonal decomposition
PG. A collection of h disjoint latches in the boundary of 1Σ whose homotopy class
relative to the boundary induces a free basis for H1(1Σ, ∂1Σ; Q) is a general system
of latches for G.
It is clear that substituting for IG in (3.1) any general system of latches yields
an invariant of cobordisms. In fact, such an invariant is also universal for homology
cylinders. We shall not make use of this result and omit the proof, which essentially
follows §3.2.2 (the main diﬀerence being in the deﬁnition of the surgery map).
5.6.2. Extending τ1 via the invariant ∇. We restrict our attention to the once-
bordered surface Σ = Σg,1 of genus g, set H = H1(Σg,1; Z) and HQ = H ⊗Q.
Recall [16] that the ﬁrst Johnson homomorphism
τ1 : I(Σg,1)→Λ3H
takes its values in the third exterior power of H.
Denote by Ig the 2g-component q-tangle in Σg,1 × I represented below.
(
)
(
(
(
(
(
)) )))
(
...
... )
1
2
2g−1
2g
Note that by isotoping Ig so that it is contained in (Σg,1 × {1}) ∪(∂Σg,1 × I), we
may consider Ig as a general system of latches for any choice of marked bordered
fatgraph G in Σg,1. Indeed, one can unambiguously arrange the endpoints of Ig
so that under the projection of Σg,1 × I to Σg,1 they lie in a neighborhood of the
ﬁxed point q where the tail of G is attached, so that ∂Ig lies on the boundary of
the preferred box in the polygonal decomposition PG.
Let G be a marked bordered fatgraph in Σg,1 and let L be a framed link in
Σg,1 × I which is disjoint from both KG and Ig. Set
(5.4)
∇G,Ig
n
(L) :=
ιn( ˇVG(L ∪KG ∪Ig))
ιn( ˇVG(U+))σ
L∪KG
+
ιn( ˇVG(U−))σ
L∪KG
−
∈A≤n(↑2g),
where we make use of the notation of (3.1). This quantity is an invariant of the
surgered manifold M = (Σg,1 × I)L, and following (3.2), we set
∇Ig
G (M) := 1 +
 ∇G,Ig
1
(L)

1 + ... +
 ∇G,Ig
n
(L)

n + ... ∈A(↑2g).
Next, consider a Whitehead move W : G 7→G′. We can then compare the value
of the invariants ∇Ig
G and ∇Ig
G′ on the trivial element 1Σg,1 and assign the quotient


## Page 34


34
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
to the Whitehead move W to deﬁne a map
J (W) = ∇Ig
G′(1Σg,1)/∇Ig
G (1Σg,1) ∈A(↑2g).
More generally, for any two marked fatgraphs in Σg,1, not necessarily related by a
Whitehead move, we can similarly take the quotient, and in the case that these two
fatgraphs are equal, we get a trivial contribution by deﬁnition. This guarantees
that this map J is the identity for the involutivity, commutativity, and pentagon
relations, and hence we obtain a representation
J : Pt(Σg,1)→A(↑2g).
Recall that the groups H1(Σg,1; Q) and H1(Σg,1, ∂Σg,1; Q) are isomorphic via
Poincar´e duality. Deﬁne a map h : {1, ..., 2g} →H by taking i to the element of H
dual to the class of the ith component of Ig in H1(Σg,1, ∂Σg,1; Z). More concretely,
if we let {Ai, Bi}2g
i=1 denote the standard symplectic basis of Σg,1 with Ai ·Bj = δij,
then
h(2k) = Ak,
h(2k −1) = Bk
for k = 1, ..., g.
Also recall that BY
1 (2g) = BY
1,3(2g) is the space of 2g-colored Y-shaped Jacobi
diagrams and that we have the well-known and elementary isomorphism BY
1 (2g) ∼=
Λ3HQ deﬁned by sending a Y-shaped diagram colored by i, j, k (following the vertex-
orientation) to h(i) ∧h(j) ∧h(k) ∈Λ3H.
In order to extend the ﬁrst Johnson homomorphism τ1, we restrict the target of
our representation J by composing it with the series of maps given by
(5.5)
Y : A(↑2g)→B(2g)→BY(2g)→BY
1 (2g) ∼= Λ3HQ.
From this, we to obtain a representation of the Ptolemy groupoid
J Y : Pt(Σg,1)→Λ3HQ.
The ﬁrst map in (5.5) is the inverse χ−1 of the Poincar´e–Birkhoﬀ–Witt isomor-
phism, and the second and third maps are the natural projections.
Theorem 5.5. The representation J Y extends the ﬁrst Johnson homomorphism
τ1 to the Ptolemy groupoid. More precisely, given a sequence
G
W1
−−→G1
W2
−−→...
Wk
−−→Gk = ϕ(G)
of Whitehead moves representing ϕ ∈Ig,1, we have τ1(ϕ) = 4 Pk
i=1 J Y(Wi).
5.6.3. Proof of Theorem 5.5. The computation of the invariant J Y is considerably
simpliﬁed by the following observation.
Lemma 5.6. For any marked bordered fatgraph G in Σg,1, we have
Y

∇Ig
G (1Σg,1)

= Y
  ˇVG(Ig)

∈Λ3HQ,
where Y is the sequence of maps in (5.5).
In other words, the Y-shaped part of ∇Ig
G (1Σg,1) comes purely from the tangle Ig,
and the system of linking pairs KG can simply be ignored in the computation.
Proof. We shall freely make use of the terminology introduced in the proof of The-
orem 3.2. In computing ∇Ig
G (1Σg,1), we can choose L to be empty in (5.4). By [29,
pp. 283], we have that ι2( ˇZ(U±)) = 1+terms of i-degree ≥2, and it follows that
Y

∇Ig
G (1Σg,1)

= Y
 ι2( ˇVG(KG ∪Ig))

.
We now consider the linking pairs KG. We may assume that there are 2g disjoint
3-balls in 1Σg,1 that intersect the system KG of linking pairs as illustrated on the
right-hand side of Figure 3.2. The Kontsevich integral of the tangle contained in


## Page 35


FINITE TYPE INVARIANTS AND FATGRAPHS
35
these balls is computed in [5, Theorem 4], from which it follows that the only terms
in ˇVG(KG ∪Ig) that can contribute to Y

∇Ig
G (1Σg,1)

have exactly 4 vertices on
each meridian core, which are the ends of 4 parallel struts connecting each to the
corresponding longitude core.
Suppose that some longitude core has k additional vertices attached. It follows
from the deﬁnition that applying the map ι2 produces ≥k univalent vertices, which
imposes the constraint that k ≤1. For k = 1, the diagram is also sent to zero by the
map ι2 since we obtain a sum of Jacobi diagrams each having a looped edge, which
vanish by the AS relation. Thus, the only terms which can possibly contribute are
Siamese diagrams with 4 struts, cf. Figure 3.3, which come with a coeﬃcient 1
4!. As
seen in §3.2.4, ι2 maps each Siamese diagram to a factor (−1)24! as required.
□
We can now proceed with the proof of Theorem 5.5 and calculate the representa-
tion J Y on a Whitehead move W. To this end, for any marked fatgraph G in Σg,1,
we can assume by Lemma 2.1 that the q-tangle Ig is in admissible position and
intersects each box except the preferred one in a trivial q-tangle. For each oriented
edge of G, we may equip each strand of the trivial q-tangle in the corresponding
box with a sign, according to whether its orientation agrees (plus sign) or disagrees
(minus sign) with the speciﬁed one. For each oriented edge of G, assign an element
of H to each box except the preferred one as follows: use the map h to label all the
strands of Ig intersecting the box by elements of the symplectic basis {Ai, Bi}2g
i=1
and take the signed sum of these labels in H. We remark that this assignment is
precisely an H-marking as described in [26, 7].
Thus, we have a situation as in the upper part of Figure 5.2, where each of the
three strands depicted there represents a collection of parallel strands of Ig ∪KG
and where A, B, C ∈H are the labels of the box as just explained. Note that
the bracketing (C, (B, A)) in the bottom-left box is imposed by the condition on
hexagons, see §2.4. After the Whitehead move, we have one of the three situations
(     )
(     )
*
*
A
A
A
C
C
C
B
B
B
*
*
*
*
or
or
(     )
(     )
*
*
C
B
A
Figure 5.2. The three possible evolutions of the forbidden sectors
under a Whitehead move.
represented in the lower part of Figure 5.2 depending on the ordering of the sectors
associated to the edge on which the move has been performed. In each case, we


## Page 36


36
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
see that the bracketing of the three strands in the bottom left box is changed to
((C, B), A). Also, in the last two cases, we get an extra cap or cup due to the
evolution of the forbiden sectors, and these are the only changes; in particular,
there are no crossing changes.
It follows from the computation [5] of ν that a cup or a cap cannot contribute
to J Y, so in all three cases, we get the same value for J Y(W) coming from the
evolution in the bracketing, i.e., from the associator. Recall that an even associator
is always of the form
(5.6)
Φ = 1 + 1
24
+ terms of J-degree > 3.
Furthermore, the value of the Kontsevich integral on a q-tangle obtained from Λ+
(see Figure 2.2) by taking parallel copies of each strand with arbitrary orientation
is obtained from Φ by the comultiplication and antipode maps deﬁned in §2.1.2.
By Lemma 5.6 and Equation 5.6, we ﬁnd J Y(W) =
1
24A ∧B ∧C ∈Λ3HQ, and
this formula coincides with one fourth of the Morita-Penner extension of the ﬁrst
Johnson homomorphism τ1. The fact that it indeed is a multiple of an extension of
τ1 follows as in [26], upon which our determination of the factor 4 currently relies,
and completes the proof of Theorem 5.5.
6. Concluding remarks and questions
There are several obvious questions regarding the Ptolemy representations de-
rived in Section 5. Most notably, one may ask for a geometric interpretation of the
mapping class group action arising from the representation J . In particular, does
J provide an extension of the full LMO invariant in the same TQFT spirit as in
Theorem 5.4?
Also, a natural and interesting issue is the faithfulness of the action of the map-
ping class group MC(Σg,1) on A2g induced by J . As the groupoid formulas for
these representations seem simpler to analyze than their corresponding mapping
class group expressions, our techniques here may prove pivotal in providing such an
answer. The facts that the pronilpotent representation of an automorphism of a free
group is faithful and that the Johnson theory presumably corresponds to the tree-
like part of LMO by [12, 14, 23] together suggest that the induced representation
of the mapping class group may be faithful.
6.1. Magnus expansions and Johnson homomorphisms. In recent beautiful
work, Gw´ena¨el Massuyeau [23] has introduced the notion of symplectic Magnus ex-
pansions and proved their existence by giving explicit formulas in terms of the LMO
invariant. Nariya Kawazumi [17] has asked the interesting question if such Magnus
expansions might be computed directly in terms of suitably marked fatgraphs as in
[7]. Our computation here of the LMO invariant provides such a formula but again
a very complicated one. Moreover, it seems likely that a construction analogous
to Massuyeau’s using our invariants ∇G or ∇Ig
G will lead to a directly computable
version, and it would be an interesting prospect to derive formulas for the various
Johnson homomorphisms in terms of such a symplectic Magnus expansion.
6.2. Relation to triangulations of 3-manifolds. The dual in a surface Σ of
a marked uni-trivalent fatgraph G is a triangulation ∆G of the surface Σ, where
a k-valent vertex of G gives rise to a 2k-gon whose alternating sides correspond
to incident half-edges and whose complementary sides correspond to arcs in the
boundary, cf. [30, 32]. The dual of a Whitehead move on a uni-trivalent fatgraph
corresponds to a diagonal exchange on its dual ideal triangulation as illustrated
in Figure 5.1.
We may imagine this diagonal ﬂip as exchanging the front and


## Page 37


FINITE TYPE INVARIANTS AND FATGRAPHS
37
the back pair of faces of a tetrahedron in the obvious way. It is thus natural to
regard a morphism in the Ptolemy groupoid as a sequence of adjoined tetrahedra
starting from the corresponding ﬁxed ideal triangulation ∆of the surface, i.e.,
a morphism provides a triangulated cobordism between one copy of the surface
with triangulation ∆and another copy of the surface with potentially another
triangulation. This is especially natural for a mapping cylinder, where the Ptolemy
morphism connects ∆to its image under the corresponding mapping class; this has
indeed been the point of view in [26, 7].
Conversely, suppose that we have ideal triangulations of two bordered surfaces
Σ and Σ′ and suppose that M is a 3-manifold whose boundary contains Σ ⊔Σ′.
We may ask for a triangulation of M extending those given on the boundary all of
whose vertices lie in Σ⊔Σ′. In the spirit of a TQFT, we are led to the following ques-
tions. Do ﬁnite compositions of Whitehead moves acting as before on triangulated
cobordisms in fact act transitively on such triangulations of M? Which 3-manifold
invariants can be computed that depend upon the ideal triangulations of Σ⊔Σ′ but
not the triangulation of M? What type of state-sum model corresponds to this?
6.3. The original AMR invariant. As pointed out in §2.5, the AMR invariant
VG employed in the construction of ∇G is actually only a weak version of the one
in [2]. Indeed, we are post-composing the original invariant with the map that
forgets the homotopy class of chord diagrams on surfaces.
It is a natural and
important problem to try to build a 3-manifold invariant from the full Andersen-
Mattes-Reshetikhin invariant that would retain this homotopy information and thus
non-trivially extend ﬁnite type invariants to all 3-manifolds. We shall return to this
study in a forthcoming paper, where we also discuss how constructions inspired by
those in this paper can be used to deﬁne universal perturbative invariants of closed
3-manifolds and more generally universal perturbative TQFTs.
Finally note that in the proof of Theorem 5.5, computations were made amenable
by Lemma 5.6 in avoiding the complex maps ιn from LMO theory, i.e., our calcu-
lation of τ1 is performed at the “AMR level” rather than at the “LMO level”, cf.
[14]. The AMR-valued version of our invariant, or its homotopy analogue just dis-
cussed, may be suited to other explicit computations as well. Indeed, the original
AMR invariant provides a graded isomorphism between the Vassiliev-ﬁltered free
vector space generated by links in the cylinder over a surface with a non-empty
boundary and the algebra of chord diagrams on the surface [2], and this isomor-
phism is determined once a suitable fatgraph is chosen in the surface as discussed
here. We therefore get an action of the Ptolemy groupoid on the algebra of chord
diagrams on any surface with non-empty boundary just as in §5.3. We shall study
this representation of the Ptolemy groupoid in a forthcoming publication.
References
[1] J. E. Andersen, A. J. Bene and R. C. Penner, Groupoid extensions of mapping class repre-
sentations for bordered surfaces, preprint (2007), arXiv:0710.2651, to appear Top. Applns.
[2] J. E. Andersen, J. Mattes and N. Reshetikhin, Quantization of the algebra of chord diagrams,
Math. Proc. Camb. Phil. Soc. 124 (1998), 451–467.
[3] D. Bar-Natan, On the Vassiliev knot invariants, Topology 34 (1995), no. 2, 423–472.
[4] D. Bar-Natan, S. Garoufalidis, L. Rozansky, D.P. Thurston, The ˚
Arhus integral of rational
homology 3-spheres II. Invariance and universality, Selecta Math. (N.S.) 8 (2002), no. 3,
341–371.
[5] D. Bar-Natan, T.T.Q. Le, D.P. Thurston, Two applications of elementary knot theory to Lie
algebras and Vassiliev invariants, Geom. Topol. 7 (2003), 1–31.
[6] A. J. Bene, “A Chord Diagrammatic Presentation of the Mapping Class Group of a Once
Bordered Surface”, to appear Geom. Ded., arXiv:0802.2747.
[7] A. J. Bene, N. Kawazumi and R. C. Penner, Canonical extensios of the Johnson homomor-
phisms to the Torelli groupoid, Advances Math. 221 (2009), 627–659.


## Page 38


38
J.E. ANDERSEN, A.J. BENE, J.B. MEILHAN, AND R.C. PENNER
[8] D. Cheptea, K. Habiro and G. Massuyeau, A functorial LMO invariant for Lagrangian cobor-
disms, Geom. Topol. 12, No. 2 (2008), 1091–1170.
[9] D. Cheptea, T.T.Q. Le, A TQFT associated to the LMO invariant of three-dimensional
manifolds, Comm. Math. Phys. 272 (2007), no. 3, 601–634.
[10] S. Garoufalidis, The mystery of the brane relation, J. Knot Theory Ram. 11 (2002), no. 5,
725–737.
[11] S. Garoufalidis, M. Goussarov, M. Polyak, Calculus of clovers and ﬁnite type invariants of
3-manifolds, Geom. Topol. 5 (2001), 75–108.
[12] S. Garoufalidis, J. Levine, Tree-level invariants of three-manifolds, Massey products and the
Johnson homomorphism, In: Graphs and Patterns in Mathematics and Theoretical Physics.
Proc. Sympos. Pure Math., vol. 3, pp. 173–203. Am. Math. Soc., Providence, RI (2005)
[13] M. Goussarov, Finite type invariants and n-equivalence of 3-manifolds, Compt. Rend. Acad.
Sc. Paris, 329 S´erie I (1999), 517–522.
[14] N. Habegger, Milnor, Johnson and tree-level perturbative invariants, preprint (2000).
[15] K. Habiro, Claspers and ﬁnite type invariants of links, Geom. Topol. 4 (2000), 1–83.
[16] D. Johnson, An Abelian quotient of the mapping class group Tg, Math. Ann. 249 (1980),
225–242.
[17] N. Kawazumi, private communication.
[18] T.T.Q. Le, On denominators of the Kontsevich integral and the universal perturbative in-
variant of 3-manifolds, Invent. Math. 135 (1999), 689–722.
[19] T.T.Q. Le, An invariant of integral homology 3-spheres which is universal for all ﬁnite type
invariants, in “Solitons, geometry an topology: on the crossroad”, (V. Buchstaber and S.
Novikov, eds.) AMS Translations Series 2 179 (1997), 75–100.
[20] T.T.Q. Le, J. Murakami, Parallel version of the universal Vassiliev-Kontsevich invariant, J.
Pure Appl. Algebra 121 (1997), no. 3, 271–291.
[21] T.T.Q. Le, J. Murakami and T. Ohtsuki, On a universal perturbative quantum invariant of
3-manifolds, Topology 37 (1998) 539–574.
[22] J. Levine, Homology cylinders: an enlargement of the mapping class group, Alg. Geom.
Topol. 1 (2001), 243–270.
[23] G. Massuyeau, Inﬁnitesimal Morita homomorphisms and the tree-level of the LMO invariant,
preprint (2008), arXiv:0809.4629.
[24] G. Massuyeau, J.B. Meilhan, Characterization of Y2-equivalence for homology cylinders, J.
Knot Theory Ram. 12 (2003), No. 4, 493-522.
[25] S. Morita, Casson’s invariant for homology 3-spheres and characteristic classes of surface
bundles I, Topology 28 (1989), 305–323.
[26] S. Morita, R.C. Penner, Torelli groups, extended Johnson homomorphisms, and new cycles
on the moduli space of curves, Math. Proc. Camb. Philos. Soc. 144, No. 3 (2008), 651–671.
[27] J. Murakami, T. Ohtsuki, Topological quantum ﬁeld theory for the universal quantum invari-
ant, Comm. Math. Phys. 188 (1997), no. 3, 501–520.
[28] T. Ohtsuki, Finite type invariants of integral homolgy spheres, J. Knot Theory Ram. 5 (1996),
101-115.
[29] T. Ohtsuki, Quantum invariants. A study of knots, 3-manifolds, and their sets, Series on
Knots and Everything, 29, World Scientiﬁc, 2002.
[30] R. C. Penner, The decorated Teichm¨uller space of punctured surfaces, Comm. Math. Phys.
113 (1987), 299–339.
[31] R. C. Penner, Universal constructions in Teichm¨uller theory,
Adv. Math. 98 (1993), 143–
215.
[32] R. C. Penner, Decorated Teichm¨uller theory of bordered surfaces, Comm. Anal. Geom. 12
(2004), 793-820.
[33] J. Roberts, Kirby calculus in manifolds with boundary, Turkish J. Math. 21 (1997), no. 1,
111–117.


## Page 39


FINITE TYPE INVARIANTS AND FATGRAPHS
39
Center for the Topology and Quantization of Moduli Spaces, Department of Math-
ematics, Aarhus University, DK-8000 Aarhus C, Denmark,
E-mail address: andersen@imf.au.dk
Departments of Mathematics, University of Southern California, Los Angeles, CA
90089, USA,
E-mail address: bene@usc.edu
Institut Fourier, Universit´e Grenoble 1, 38402 St Martin d’H`eres, France
E-mail address: jean-baptiste.meilhan@ujf-grenoble.fr
Departments of Mathematics and Physics/Astronomy, University of Southern Cal-
ifornia, Los Angeles, CA 90089, USA, and Center for the Topology and Quantization
of Moduli Spaces, Department of Mathematics, Aarhus University, DK-8000 Aarhus C,
Denmark,
E-mail address: rpenner@math.usc.edu

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]

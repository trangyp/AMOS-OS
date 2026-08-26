---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1810.01759v3
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1810.01759v3__Q_-Series_and_Quantum_Spin_Networks

> Source: 1810.01759v3__Q_-Series_and_Quantum_Spin_Networks.pdf

> Pages: 14

---


## Page 1


Q-SERIES AND QUANTUM SPIN NETWORKS
MOHAMED ELHAMDADI, MUSTAFA HAJIJ, AND JESSE S F LEVITT
Abstract. The tail of a quantum spin network in the two-sphere is a q-series associated to the
network. We study the existence of the head and tail functions of quantum spin networks colored by
2n. We compute the q-series for an inﬁnite family of quantum spin networks and give the relation
between the tail of these networks and the tail of the colored Jones polynomial. Finally, we show
that the family of quantum spin networks under study satisﬁes a natural product structure, making
these networks satisfy a natural product structure.
1. Introduction
The colored Jones polynomial assigns to every link L a sequence of Laurent polynomials {Jn,L}n∈N
where the positive integer n is called the color, see [16]. Recent advances in the study of this poly-
nomial showed that for alternating and adequate knots, certain coeﬃcients of Jn,L stabilize as n
increases [2, 4, 6–9, 11]. More precisely, for any alternating link L the ﬁrst (n + 1)-coeﬃcients of
Jn,L agree with the initial (n + 1)-coeﬃcients of Jn+1,L. This gives rise to a q-series called the tail
of the colored Jones polynomial. The highest degree coeﬃcients of the colored Jones polynomial
have similar stability properties and this induced power series is instead called the head of the
colored Jones polynomial. This behavior was ﬁrst observed by Dasbach and Lin [5] and was proved
by Armond [2] for adequate links and independently by Garoufalidis and Lˆe [9] who also showed
higher order coeﬃcient stability. One of the interesting aspects of the q-series coming from the col-
ored Jones polynomial is their relation to the Ramanujan theta and false theta functions. Armond
and Dasbach [3] used the properties of the colored Jones polynomial to prove the Andrew-Gordan
identity for theta functions [1]. A corresponding identity for the false theta functions was given by
the second author [11]. The stability of the coeﬃcients of other quantum invariants have also been
studied recently. For instance, in [17] the coeﬃcients of the sl3(C)-colored Jones polynomial were
used to give a generalization for the identity given by the second author in [10].
Let D be a planar trivalent graph in the 2-sphere S2. Fix a positive integer n and label every
edge in D by n or 2n such that we obtain an admissible quantum spin network Dn (see the precise
deﬁnition in Section 2). This deﬁnes a sequence of quantum spin networks D = {Dn}n∈N. In [10]
the second author initiated a study of the stability of the coeﬃcients of the evaluations of the
sequence elements of D, a study which arises naturally when one considers the tail of colored
Jones polynomial [2].
Previous work [11] has shown that the quantum spin networks (QSNs)
corresponding to adequate skein elements admit a well-deﬁned tail. However, it was also found
that the tail might exist for QSNs whose skein elements are not adequate.
In this paper we focus on quantum spin networks with all edges colored 2n. We show that the
tail of such networks always exist and show how to compute the tail of such networks on an inﬁnite
family of graphs. Additionally, these networks satisfy a natural product structure. We further
illustrate the relationship of the tail of these graphs to the tail of the colored Jones polynomial of
alternating links. Finally, we demonstrate how the tail of an inﬁnite family of alternating links can
be computed by considering the tail of a single QSN.
The paper is organized as follows. In section 2, we recall the necessary background needed for the
paper. Section 3 deﬁnes the admissibility of a QSN and discusses the Kauﬀman bracket evaluation.
In section 4, we recall the deﬁnition of the tail of a QSN and show that the tail of any QSN whose
1
arXiv:1810.01759v3  [math.GT]  18 Sep 2019


## Page 2


Q-SERIES AND QUANTUM SPIN NETWORKS
2
edges are all labeled by 2n exists. Section 5 covers a connection of the tail of a QSN to the tail of
related colored Jones polynomial. While section 6 deals with the product structure on the tail of
two QSNs. As in the case of the colored Jones polynomial, the tail of quantum spin networks with
edges colored 2n satisﬁes a natural product structure. In section 7 we give the tail of the theta and
tetrahedron graphs with edges colored 2n. We then use this and the theta and tetrahedron graphs
to compute the tail of inﬁnite families of other graphs.
2. Background
Let F be a connected oriented surface, with boundary denoted ∂F. When the boundary ∂F
is non-empty and a ﬁnite set of marked points are chosen on it, a link diagram in F is a ﬁnite
collection of arcs and simple closed curves in F that meet ∂F orthogonally at the marked points.
As in the case of standard link diagrams, the link diagram in F will be assumed to have a ﬁnite
number of crossing points. Moreover, at crossings we will distinguish the strands using the usual
convention of upper-strand and lower-strand. We will work over R = Q(A), the ﬁeld generated by
the indeterminate A over the rational numbers. Furthermore set A4 = q.
Deﬁnition 2.1. Let D(F) be the free R-module of link diagrams in F. The linear skein S(F) of
F is the quotient of the module D(F) by the relations:
(1)
−A
−A−1
,
(2) L ⊔
+ (A2 + A−2)L.
where L ⊔
consists of a link L in F and a disjoint simple connected curve
that is
null-homotopic in F.
The linear skein space is also called the Kauﬀman bracket skein module [14,15]. The two main
linear skein spaces needed in this paper are the linear skein of the 2-sphere and the linear skein
of the disk with some marked points on the boundary.
The linear skein module of the sphere
S2 is isomorphic to the ring Q(A). To describe the linear skein space of the disk with boundary
and marked points, ﬁrst let E = I × I where I = [0, 1] and then ﬁx 2n marked points on the
boundary of E, with precisely n points on the top and n points on the bottom of E. We then
denote by S(E, 2n) the linear skein module of the disk E with 2n marked points. We make this
into an associative algebra over Q(A) by the natural vertical juxtaposition of diagrams known as
the nth Temperley-Lieb algebra TLn. The Jones-Wenzl idempotent (projector), denoted f(n), is an
idempotent in TLn. The graphical depiction for this projector appears as a box labelled with one
strand entering the box from one side and one strand leaving the box from the other side of the
box. The label n is usually drawn next to the box to indicate label of the projector.
The projector can be characterized completely by the ﬁrst two axioms in 2.1, with the latter two
relations following as a consequence. For more information about these important idempotents,
including a useful recursive relation, we recommend Wenzl’s critical paper [18].
n
=
n
,
n −i −2
1
i
n
= 0 and
n
= ∆n,
n
m
m + n
=
m + n
(2.1)


## Page 3


Q-SERIES AND QUANTUM SPIN NETWORKS
3
where
∆n = (−1)n
 
q(n+1)/2 −q−(n+1)/2
q1/2 −q−1/2
!
.
and the element ∆n is related to the (n+1)th quantum integer, denoted by [n+1]q, via the equation
∆n = (−1)n[n + 1]q.
We use this idempotent f(n) to deﬁne useful submodules of the Kauﬀman bracket skein module
of the disk with marked points on its boundary as follows. Let E be a disk with m marked points
on its boundary. Partitioning this set of points into k clusters of si (1 ≤i ≤k) marked points
each, with m = s1 + s2 + . . . + sk, we consider the skein submodule of the skein module of the disk
with m marked points obtained by placing idempotents f(si) on each cluster of si points following
clockwise around the disk. The submodule is thus obtained by taking any diagram D in S(E, m)
and mapping it into the same diagram with the idempotents, f(si), placed on the clusters of marked
points si. We will denote this skein module by Ys1,...,sk. Figure 1 illustrates an example of elements
in the skein module of S(E, 12) mapping to elements in the submodule Y4,3,4,1.
Figure 1.
An element in the skein module of the disk with 4 + 3 + 4 + 1 marked
points on the boundary and the corresponding element in the space Y4,3,4,1.
The space Ya is zero dimensional as is Ya,b when a ̸= b, while Ya,b is one dimensional and generated
by f(a) when a = b. This follows from the basic properties of the idempotent in 2.1. Similarly, the
space Ya,b,c is either zero dimensional or one dimensional. It is one dimensional when a + b + c is
even and a + b ≥c ≥|a −b|. Such a triple (a, b, c) is called admissible. When (a, b, c) is admissible
the space Ya,b,c is generated by the skein element τa,b,c in Figure 2. This element exists if and only
if the following three equations are satisﬁed:
a = x + y, b = x + z, c = y + z
for x, y, z ∈N.
(2.2)
b
a
x
y
z
c
Figure 2. The skein element τa,b,c in the space Ya,b,c
3. Quantum Spin Networks
A quantum spin network (QSN) is a planar trivalent graph with edges labeled by non-negative
integers. A zero-labeled edge corresponds to deleting that edge. We say that a QSN is admissible if
the three labels at every vertex satisfy the admissibility conditions 2.2, otherwise it is inadmissible.
See Figure 3 for an example and non-example of an admissible quantum spin network.
If D is a quantum spin network in S2 then the Kauﬀman bracket evaluation of D, denoted ⟨D⟩
where ⟨·⟩: S(S2) →Q(A) is deﬁned to be the evaluation of D as an element in S(S2) after replacing


## Page 4


Q-SERIES AND QUANTUM SPIN NETWORKS
4
4
3
3
2
5
3
5
3
1
3
4
8
Figure 3. On the left, an example of a inadmissible quantum spin network. On
the right, an example of an admissible quantum spin network.
any edge colored n by f(n) and each vertex colored (a, b, c) by the skein element τa,b,c, as in Figure 4.
If D is inadmissible then we deﬁne ⟨D⟩= 0. Often in this paper we will not distinguish between
the QSN in S2 and its evaluation as a linear skein of S2. Finally, when we work with QSNs in
other skein modules that are not necessarily S2, one often needs to switch between the QSN and
the corresponding skein element as illustrated in Figure 4. We will denote by ⟨D⟩to skein element
that corresponds to the quantum spin network D.
b
a
x
y
z
c
b
a
c
n
n
Figure 4. The evaluation of a quantum spin network in the linear skein of S2 is
obtained by the above local replacement rules.
4. The Tail of Quantum Spin Networks
Let D be a planar trivalent graph in S2. We label every edge in D by n or 2n where n ∈N
such that we obtain an admissible quantum spin network Dn. This way we construct a sequence of
quantum spin networks D = {Dn}n∈N. In this paper we are concerned with the stability properties
associated to the coeﬃcients of such a sequence D. We will show that if the sequence of quantum
spin networks D satisﬁes a natural condition, then the ﬁrst n coeﬃcients of ⟨Dn⟩are identical to
the ﬁrst n coeﬃcients of ⟨Dn+1⟩up to a common sign. This stability gives rise to a q-series called
the tail of the quantum spin network D. The tail of such sequences were studied by the second
author in [10]. An investigation of QSNs follows organically from considering the tail of the colored
Jones polynomial (see for example [2]). The relationship between the colored Jones polynomial and
Rogers-Ramanujan identities is also studied in [3]. In this section we constrain ourselves to study
the stability of admissible QSNs whose edges are all colored 2n and show that in this case the tail
always exists.
Let P1(q) and P2(q) be non-zero power series in Z[q−1][[q]]. For a positive integer n, we say
that P1 and P2 are n-equivalent and write P1(q) .=n P2(q), if their ﬁrst n coeﬃcients agree up to a
common sign. For instance, −q−4 + 15q−3 −6 + 11q .=5 1 −15q + 6q4. When P1(q) .=n P2(q) for
every integer n ≥0, we will simply write P1(q) .= P2(q). We will denote the minimal degree of an
element f ∈Z[q−1][[q]] by deg(f). We now give the deﬁnition of the tail of sequence of elements in
Z[q−1][[q]].
Deﬁnition 4.1. Let P = {Pn(q)}n∈N be a sequence of formal power series in Z[q−1][[q]]. A tail (if
it exists) of the sequence P is a formal power series TP(q) in Z[q−1][[q]] with:
TP(q) .=n Pn(q), for all n ∈N.
Remark 4.2. One can immediately see from this deﬁnition that the sequence P = {Pn(q)}n∈N
admits a tail if and if only if Pn(q) .=n Pn+1(q) for all n.


## Page 5


Q-SERIES AND QUANTUM SPIN NETWORKS
5
Remark 4.3. A tail of a sequence P described in Deﬁnition 4.1, when it exists, is not unique.
Namely, if P = {Pn(q)}n∈N is a sequence with a tail T ′(P), then qa · T ′(P) will also be a tail of P
for any a ∈Z. Given any tail T ′(P) we can always choose an a such that deg(T(P)) = 0, when
T(P) = qa · T ′(P). By convention we will refer to the tail of the sequence P as the power series
T(P) satisfying this condition, noting that T(P) ∈Z[[q]]. However, in calculating the tail of a
sequence, it will be convenient to consider tails of P where deg(T ′(P)) ̸= 0.
The evaluation of a quantum spin network in S(S2) yields an rational function in Q(A). Following
Armond [2] we need to express a rational function as Laurant series in such a way that this Laurent
series has a minimum degree. In other words every element in Q(A) is identiﬁed with a unique
element in Z[A−1][[A]]. Hence the evaluation of any admissible quantum spin network in S(S2)
can be uniquely identiﬁed with a power series in Z[A−1][[A]]. We will use this identiﬁcation to
apply the previous equivalence relation, .=n, to quantum spin networks. We will call this element in
Z[A−1][[A]] the power series evaluation of a quantum spin network. Moreover when working with
the tail of such networks one often uses the variable q instead of the variable A (recall that q = A4).
In this case the power series evaluation of a quantum spin network is normalized, by multiplying
by a qa for some power a, so that ﬁnal power series is an element in Z[q−1][[q]]. We will assume
this identiﬁcation and normalization in what follows.
Now let D be a trivalent graph and denote by E(D) its edge set. Let F = {fn : E(D) −→N}n∈N
be a sequence of label assignments on the edges of D such that the resulting QSN is admissible for
every n ∈N. We will denote a quantum spin network D labeled with fn by Dfn or simply by Dn
(when there is no confusion).
The tail of the sequence {Dn}n∈N, denoted by T(D), is a series in Z[q−1][[q]] that is n-equivalent
to Dn for each n ∈N.
The following two lemmas have straightforward proofs and will be useful when trying to compute
tails.
Lemma 4.4. Let P1, P2, Q1, Q2 be non-zero power series in Z[q−1][[q]] with P1(q) .=n P2(q) and
Q1(q) .=n Q2(q), then
(1) P1Q1 .=n P2Q2.
(2) If deg(Q1) = deg(P1) + a where a > n, then P1 ± Q1 .=n P1.
(3) If deg(P1) = deg(P2) and deg(Q1) = deg(Q2), then P1 + Q1 .=n P2 + Q2.
Let R be an element in Q(q) of the form 1/P where P is a Laurent polynomial. Then as we
mentioned earlier we can write R as an element in Z[q−1][[q]]. Using this convention and part (1)
of 4.4 we also obtain the following Lemma.
Lemma 4.5. Let P1, Q1, Q2 be non-zero power series in Z[q−1][[q]] and let P2 = 1/P ∈Q(q) for
P ∈Z[q, q−1]. Furthermore, suppose that P1(q) .=n P2(q) and Q1(q) .=n Q2(q), then P1Q1 .=n P2Q2.
4.1. Adequate Quantum Spin Networks. Let D be a skein element in S(S2) consisting of
arcs and circles labeled by Jones-Wenzl idempotents of color n or 2n. Let D denote the diagram
obtained from D by replacing each n-labeled arc with the idempotent f(n) by n parallel arcs passing
under it. We say that the skein D is adequate if in D each continuous arc passes at most once
under any idempotent f(n). Figures 5 and 6 show examples of adequate and non-adequate skein
elements. Each circle in the Figures bounds a disk, a result of our restriction of fn(e) ∈{n, 2n}. In
Figure 5 each unlabeled arc represents n parallel strands. On the left, each strand passes multiple
idempotents, but only passes under any individual idempotent once, while on the right, each arc
passes under each idempotent twice. A quantum spin network is adequate if its corresponding skein
element is adequate, hence any adequate QSN must also be admissible. The following theorem is
due to [2,11].


## Page 6


Q-SERIES AND QUANTUM SPIN NETWORKS
6
2n
2n
Figure 5.
All arcs in the skein elements are labeled by n. Left: An adequate
quantum spin network (all edges in the graph have label 2n). Right: A non-adequate
quantum spin network (all non-labeled edges in the graph have label n).
Theorem 4.6. Let D be a trivalent graph, with a sequence of label assignment functions
F = {fn : E(D) →N | fn(e) is equal to n or 2n for all e ∈E(D)}n∈N
on the edges of D such that Dfn is an adequate quantum spin network for every n. Then the tail
of {Dfn}n∈N exists.
Remark 4.7. It is worth mentioning here that the tail of non-adequate QSNs may exist. For instance,
the tail of the non-adequate QSN shown on the right of Figure 5 has been computed [11, Example
4.17].
In this paper we will focus on sequences of quantum spin networks where the edges are all labeled
2n. The tail of such networks always exist, thanks to the following proposition.
Proposition 4.8. Let D be a trivalent graph, and let {fn : E(D) →N}n∈N be a sequence of label
assignments deﬁned by fn(e) = 2n for every e ∈E(D) and for every n ∈N. Then the tail of
{Dfn}n∈N exists.
Proof. Let F be an arbitrary face in D. Since edges are labeled by 2n everywhere then the skein
element that corresponds to Dfn appears around F as illustrated in Figure 6. Every such face has
an equivalent skein element as illustrated in Figure 6 on the right. If we replace each idempotent in
D by 2n parallel strands then we obtain n parallel circles within this polygon such that each circle
passes at most once under each former idempotent. This proves that Dfn is adequate for every n
and each fn(e) is linear. Hence by Theorem 4.6 the tail of {Dfn} exists.
□
n
n
n
F
2n
2n
2n
F
Figure 6. A local picture of any face, F, of a quantum spin network whose edges
are labeled by 2n, on the left, and its corresponding skein element on the right.
5. Connections to the tail of the colored Jones polynomial
In this section we relate the tail of a quantum spin network to the tail of the colored Jones
polynomial ﬁrst discussed by Dasbach and Lin in [5]. We show that the tail of trivalent graphs
that are colored by 2n can be realized as the tail of an alternating link.
The Jones polynomial knot invariant is given by a Laurent polynomial in the variable q with
integer coeﬃcients. The Jones polynomial generalizes to an invariant Jg
K,V (q) ∈Z[q±1] of a zero-
framed knot K colored by a representation V of a simple Lie algebra g, and normalized so that


## Page 7


Q-SERIES AND QUANTUM SPIN NETWORKS
7
Jg
O,V (q) = 1, where O denotes the zero-framed unknot. The invariant Jg
K,V (q) is called the quantum
invariant of the knot K associated with the simple Lie algebra g and the representation V . The
Jones polynomial corresponds to the second dimensional irreducible representation of sl(2, C) and
the n-th colored Jones polynomial, denoted by Jn,K(q), is the quantum invariant associated with
the n + 1-dimensional irreducible representation of sl(2, C).
Dasbach and Lin observed in [5] that, up to a common sign change, the ﬁrst n coeﬃcients of
Jn,L(q) agree with the ﬁrst n coeﬃcients of Jn+1,L(q) for an alternating link L. As seen in the
following example:
Example 5.1. The colored Jones polynomial of the knot 62, up to multiplication with a suitable
power q±an for some integer an, is given in the following table:
n = 1 1
n = 2 1 −2q +2q2 −2q3 +2q4 −q5 + q6
n = 3 1 −2q
+4q3 −5q4
+6q6 −6q7 + · · ·
n = 4 1 −2q
+2q3 + q4 −4q5 −2q6 +7q7 + · · ·
n = 5 1 −2q
+2q3 −q4 +2q5 −6q6 +2q7 + · · ·
n = 6 1 −2q
+2q3 −q4
−2q7 + · · ·
n = 7 1 −2q
+2q3 −q4
−2q6 +4q7 + · · ·
n = 8 1 −2q
+2q3 −q4
−2q6 +2q7 + · · ·
hence the tail of the colored Jones polynomial of the knot 62 is given by
T62(q) = 1 −2q + 0q2 + 2q3 −q4 + 0q5 −2q6 + 2q7 + · · ·
In [2] Armond reduced the study of the tail of the colored Jones polynomial of an alternating
link L to a simpler sequence of skein elements in S(S2) obtained from an alternating diagram of
L. We recall Armond’s result in detail here.
Let D be a diagram of a link L in S2. Any crossing of D can be smoothed in two ways, either by
the A-smoothing or by the B-smoothing illustrated in Figure 7. By applying an A-smoothing or a
B-smoothing to every crossing in D, one obtains a collection of circles called a Kauﬀman state of
the diagram D. Let c(D) be the crossing number of the diagram D, thus there are 2c(D) Kauﬀman
states. Among these states, two particular states are important to us, namely, the all-A smoothing
(the state in which all crossings were replaced by the A-smoothing) denoted by SA(D), and the
all-B smoothing denoted by SB(D).
A
B
Figure 7. The A-smoothing and the B-smoothing of a crossing.
For an alternating reduced diagram D of a link L, a result of Kauﬀman [12] states that the highest
and lowest coeﬃcients of the Kauﬀman bracket evaluation of such a diagram D are equal to the
highest and lowest coeﬃcients of the SA(D) and SB(D) respectively. An analogue of this result
was proven for adequate links by Armond [2]. Starting with SB(D), consider the skein element
obtained by decorating each circle in SB(D) with the nth Jones-Wenzl idempotent and replacing
each dashed line in SB(D) with the (2n)th Jones-Wenzl idempotent. Denoting this skein element
S n
B(D) (see Figure 10 for an example), the following result holds.
Theorem 5.2. (Armond [2]) Let L be a link in S3 with reduced alternating knot diagram D. Then
Jn,L(q) .=(n+1) S n
B(D).
By this theorem, the tail of the colored Jones polynomial is determined by the sequence {S n
B(D)}n∈N.
Now, for every n, the skein element S n
B(D) can be written as a trivalent graph in S(S2). The element
S n
B(D) can be written as quantum spin network by using the following simple identity :


## Page 8


Q-SERIES AND QUANTUM SPIN NETWORKS
8
* n
n
n
n
2n
+
=
n
n
(5.1)
The following identity can also be useful to simplify the ﬁnal QSN:
*
2n
2n
2n
n
n
n
+
=
2n
2n
2n
=
*
2n
2n
2n
+
(5.2)
The left equality comes from equation 5.1 applied at each vertex, while the right equality was
illustrated at the right of Figure 4.
Consider the trefoil T appearing in Figure 8 on the left, the skein element S n
B(T ) appears on in
the middle of the ﬁgure. Using identity 5.1 we can obtain the trivalent graph equivalent to S n
B(T )
shown on the right of Figure 8. Under identity 5.2 this has the same tail as the Theta graph which
will be calculated in section 7.
2n
2n
2n
Figure 8. From left to right: The trefoil T , the skein element S n
B(T ) and the
corresponding trivalent graph of S n
B(T ) obtained using identity 5.1. All unlabeled
edges in the trivalent graph are colored with n. All arcs in the skein element S n
B(T )
are labeled n.
In fact, given any trivalent graph G corresponding to a quantum spin network with edges colored
2n we can construct an alternating link diagram D such that the tail of the colored Jones polynomial
of D is equal to the tail of the sequence {G2n}n∈N as we will explain in the following subsection.
5.1. Going From Trivalent Graphs to Link Diagrams. Given a trivalent graph G, the corre-
spondence appearing in Figure 9 can always be used to obtain an alternating link diagram L(G).
In this paper we use the convention that all edges in trivalent graphs are replaced by negative twist
regions as illustrated in the right of Figure 9.
Figure 9. Obtaining a link diagram from a trivalent graph.
The tail of Jn,L(G) can be seen to be equivalent to the tail of the trivalent graph sequence
{G2n}n∈N by observing that each skein element S n
B(L(G)) corresponds precisely to the graph G2n
under identities 5.1 and 5.2. It then follows from Theorem 5.2 that the tail of the quantum spin
network sequence {G2n} is equivalent to the tail of Jn,L(G). The correspondence given in Figure 9


## Page 9


Q-SERIES AND QUANTUM SPIN NETWORKS
9
thus allows for the tail of any family of link diagrams corresponding to L(G) for any trivalent graph
G to be computed.
5.2. Reduced Graphs and the tail of the Colored Jones Polynomial. The sequence {S n
B(D)}n∈N
depends on a simple planar graph obtained from the knot diagram D. We review this fact here.
To each Kauﬀman state S(D) of a link diagram D, one can associate a graph GS(D) obtained by
replacing each circle of S(D) by a vertex and each dashed line by an edge. See Figure 10. In par-
ticular the B-graph, denoted by GB(D), is the graph obtained from the all B-state in this manner.
The reduced B−graph, denoted by G′
B(D), is obtained from the B-graph by keeping the same set
of vertices of B(D) and replacing parallel edges by a single edge. See Figure 10 for an example.
Figure 10. From left to right: A knot diagram D, its B-state, the B-graph GB(D)
of D, the reduced B-graph G′
B(D) of D and the skein element S n
B(D).
Using this deﬁnition of reduced B-graph, Theorem 5.2 implies that the tail of colored Jones
polynomial depends only on the reduced B-graph of D. Thus we will deﬁne the tail of a reduced
graph G to be the tail of the colored Jones polynomial of a link D whose reduced B-graph is G.
The reader is reminded that we are working with two kinds of graphs now: the trivalent graphs,
denoted by G, and the B-graphs, denoted by G. Using Theorem 5.2 we can meaningfully talk about
the tail of colored Jones polynomial and its reduced graph. Furthermore, since the reduced graph
corresponds to skein element which in turn corresponds to a trivalent graph we may also refer to
the tail of the colored Jones polynomial via its corresponding trivalent graph. This correspondence
between various graphs is illustrated in Figure 11.
Figure 11. Correspondence between trivalent graphs (left), link diagrams (middle)
and reduced graphs (right).
6. The Product Structure on Tails
Armond and Dasbach proved in [3] that the tail of the edge connect sum of two graphs, Gi is
equal to the multiplication of the tails of these two graphs. We recall this product structure result
before giving the natural analogue for it on the tail of quantum spin networks with edges colored
2n. The multiplication of two graphs is deﬁned in Figure 12.
Theorem 6.1. Let D1 and D2 be two reduced link diagrams. Then TG′(D1)TG′(D2) = TG′(D1)∗G′(D2).
Now for our consideration, let G1 and G2 be trivalent graphs in S(S2). Suppose that each of G1
and G2 contains the trivalent graph τ2n,2n,2n as in Figure 13.
Deﬁne the map <, >: S(S2)×S(S2) −→S(S2) by the wiring illustrated in Figure 14. The theta
graph provides a natural identity for this multiplication.
The set of tails of the trivalent graphs with edges colored 2n behaves well under the product of
Figure 14 as described in the following theorem.


## Page 10


Q-SERIES AND QUANTUM SPIN NETWORKS
10
G′(D2)
G′(D1)
G′(D1) ∗G′(D2)
Figure 12. Two reduced graphs and their product.
2n
2n
2n
Figure 13. The graph G with a trivalent graph τ2n,2n,2n
G2
G1
< G1, G2 >
Figure 14. The product < G1, G2 >
Theorem 6.2. Let G1 and G2 be as deﬁned above. Then
T<G1,G2> =
1
(q2; q)∞
TG1TG2
Proof. The skein space Y2n,2n,2n is one dimensional and generated by the skein element τ2n,2n,2n.
Hence we can write
Gi = Ri(q)Θ(2n, 2n, 2n),
for some Ri(q) ∈Q(q) for i = 1, 2. Moreover, by applying the same fact to the diagram < G1, G2 >,
one graph at a time, we have:
< G1, G2 >= R1(q)R2(q)Θ(2n, 2n, 2n).
By our assumption that G1 and G2 are trivalent graphs with edges colored 2n, proposition 4.8
ensures that we have
TGi
.=n Ri(q)Θ(2n, 2n, 2n)
for i = 1, 2. Now, TΘ(2n,2n,2n) = (q;q)∞
1−q
as will be shown in Proposition 7.3. Thus,
< G1, G2 >
.=n
TG1
TG2
Θ(2n, 2n, 2n)
.=n
1
(q2; q)n
TG1TG2.
The result follows.
□
Returning to the case where every edge is labeled 2n. Observe that the multiplication deﬁned
by the wiring in Figure 14 does not depend on the choice of the trivalent vertex. We now have the
following immediate result.
Corollary 6.3. Let G be any 2n-colored trivalent graph in S(S2), then T<Θ2n,G> = TG.
By the virtue of Proposition 4.8 we can meaningfully speak about the set of tails of trivalent
graphs with edges colored 2n. Denote this set by G. Let G1 and G2 be two elements in G. Deﬁne
on the set G the product ∗by
T(G1) ∗T(G2) = (q2; q)∞T<G1,G2>.


## Page 11


Q-SERIES AND QUANTUM SPIN NETWORKS
11
In other words the multiplication of the of tails T(G1) and T(G2) is equal, up to a factor, to the
tail of graph multiplications < G1, G2 >.
7. Computing the tail of the Theta and Tetrahedron graphs
In this section we investigate the tail of the theta and tetrahedron graphs with edges colored 2n.
These graphs can be used to compute the tail of inﬁnite families of other graphs using both the
product, < ·, · >, and other techniques as we will demonstrate. We start with the following useful
Lemma.
Lemma 7.1. Let n be a positive integer and let F(q, n) be a rational function of the form:
F(q, n) =
n
X
i=0
P(q, n, i)
(7.1)
where P(q, n, i) is an element in Q(q) of the form P(q, n, i) =
(q;q)n
(q;q)n−i Q(q, n, i) for some Q(q, n, i) ∈
Q(q). Suppose further that deg(P(q, n, i)) + i < deg(P(q, n, i + 1)) for all positive integers n, i with
i ≤n. Then F(q, n) .=n
Pn
i=0 Q(q, n, i).
Proof. Beginning with the relation
(q; q)n
(q; q)n−i
= 1 −qn−i+1 + O(n −i + 2),
(7.2)
we have that deg(P(q, n, i)) = deg(Q(q, n, i)) for all positive integers n, i. To simplify notation, we
will denote deg(P(q, n, i)) by dn,i.
Now, for all i ≥0, it follows from the assumptions and equation 7.2 that
P(q, n, i) + P(q, n, i + 1) .=n P(q, n, i) + Q(q, n, i + 1)
(7.3)
as
P(q, n, i) + P(q, n, i + 1)
=
P(q, n, i) +
(q; q)n
(q; q)n−i−1
Q(q, n, i + 1)
=
P(q, n, i) + (1 −qn−i + O(n −i + 1))Q(q, n, i + 1)
=
P(q, n, i) + Q(q, n, i + 1) −qn−iQ(q, n, i + 1) + O(n −i + 1 + dn,i+1)
and thus that deg(P(q, n, i) + P(q, n, i + 1)) = deg(P(q, n, i) + Q(q, n, i + 1)). Moreover, since
dn,i+1 > dn,i + i we have:
deg(−qn−iQ(q, n, i + 1)) = n −i + dn,i+1 > n −i + dn,i + i = dn,i + n.
Thus, the ﬁrst n coeﬃcients of the terms −qn−iQ(q, n, i + 1) + O(n −i + 1 + dn,i+1) do not
contribute to the ﬁrst n coeﬃcients of P(q, n, i) + P(q, n, i + 1) hence equation 7.3 holds. Now by
applying 7.3 inductively to equation 7.1, we obtain:
n
X
i=0
P(q, n, i) .=n P(q, n, 0) +
n
X
i=1
Q(q, n, i)
Since P(q, n, 0) = Q(q, n, 0) the results follows.
□
In order to compute the tail of the theta and tetrahedron graphs we now recall a few identities
from the skein theory associated to the Kauﬀman bracket. The exact formula of the tetrahedron
and theta coeﬃcients can be found in [13] and we shall not repeat them in full here. Using the
following identity from [6]:
jY
i=0
[n −i]q = q(2+3j+j2−2n−2jn)/4(1 −q)−1−j
(q; q)n
(q; q)n−j−1


## Page 12


Q-SERIES AND QUANTUM SPIN NETWORKS
12
and the formula of the tetrahedron and theta graphs from [13], we obtain, after simpliﬁcation, the
following two identities:
Θ(2n, 2n, 2n) = (−1)nq−3n/2 (q; q)3
n(q; q)3n+1
(1 −q)(q; q)3
2n
.
(7.4)
and
Tet

2n
2n
2n
2n
2n
2n

=
q−2n(q; q)12
n
(1 −q)(q; q)6
2n
n
X
i=0
(−1)iq(i+3i2)/2(q; q)4n−i
(q; q)4
n−i(q; q)3
i
.
(7.5)
We now compute the tail of the theta and tetrahedron graphs. For simplicity of the notation we
will denote Θ(2n, 2n, 2n) by Θ2n and Tet

2n
2n
2n
2n
2n
2n

by H2n.
Remark 7.2. Proposition 7.3 part (1) computes the tail of the theta graph which, following The-
orem 5.2 and the discussion of Figure 8, is equivalent to computing the tail of the trefoil. This
provides an alternative method to earlier computations [2,11].
Proposition 7.3. The tails of the theta and tetrahedron graphs are given by:
(1) T(Θ2n) = (q;q)∞
1−q
(2) T(H2n) = (q;q)3
∞
(1−q)
∞
P
i=0
(−1)iq(i+3i2)/2
(q;q)3
i
Proof.
(1) First observe that
(q; q)n
(q; q)2n
=
n−1
Y
k=0
(1 −qk+1)
2n−1
Y
k=0
(1 −qk+1)
=
1
2n−1
Y
k=n
(1 −qk+1)
=
n−1
Y
k=0
1
(1 −qn+k+1)
.=n 1.
(7.6)
Moreover,
(q; q)3n+1 .=n (q; q)∞.
Then the result follows directly from equation 7.4.
(2) Starting from 7.5, and applying the equivalence 7.6 using Lemma 4.4 implies that:
q−2n(q; q)12
n
(1 −q)(q; q)6
2n
n
X
i=0
(−1)iq(i+3i2)/2(q; q)4n−i
(q; q)4
n−i(q; q)3
i
.=n (q; q)6
n
n
X
i=0
(−1)iq(i+3i2)/2(q; q)4n−i
(1 −q)(q; q)4
n−i(q; q)3
i
.
Now consider:
F(n, q) = (q; q)2
n
n
X
i=0
P(q, n, i),
where
P(q, n, i) = (−1)iq(i+3i2)/2(q; q)4n−i(q; q)4
n
(1 −q)(q; q)4
n−i(q; q)3
i
.
Observe that deg(P(q, n, i)) = (i+3i2)/2, and hence deg(P(q, n, i))+i > deg(P(q, n, i+1)).
Then Lemma 7.1 implies:
F(n, q) .=n (q; q)2
n
n
X
i=0
(−1)iq(i+3i2)/2(q; q)4n−i
(1 −q)(q; q)3
i
.=n
(q; q)3
n
(1 −q)
n
X
i=0
(−1)iq(i+3i2)/2
(q; q)3
i
.
The result thus follows.
□


## Page 13


Q-SERIES AND QUANTUM SPIN NETWORKS
13
We usually work with the normalized colored Jones polynomial, hence it is more natural to also
work with the normalized tail. The normalizing is done by dividing the tail by ∆n. To this end,
we compute the the tail of ∆n.
∆n .=n [n + 1]q = q(n+1)/2 −q−(n+1)/2
q1/2 −q−1/2
=
−1
q−1/2 × q(n+1)/2 −q−(n+1)/2
1 −q
.=n(q(n+1)/2 −q−(n+1)/2)
∞
X
i=0
qi .=n
∞
X
i=0
qi =
1
1 −q
This can be used to simplify the fraction
1
1−q in the formulas obtained in Proposition 7.3. The
product of Theorem 6.2 and these results provide the building blocks to compute the tails of
useful formulae and inﬁnite families of alternating links as well. We illustrate an example of such
computations below.
Given any 2n-colored trivalent graph whose tail we know, we can either add or contract triangular
faces. From [13] we have the following equality:
*
2n
2n
2n
2n
2n
2n
+
=
σ(n)
*
2n
2n
2n
Y
+
,
where
σ(n) = H2n
Θ2n
.
(7.7)
Example 7.4. Consider the multiplication of the two graphs given on the left hand side of Fig-
ure 15. We know from Lemma 7.3 that the tail of H2n is given by TH2n(q). Hence the tail of the
graph given on the right hand side of Figure 15, which we will denote Γ2n, is
T<H2n,H2n> =
1
(q2; q)∞
TH2n(q)2
.
Figure 15. An example of the product <, > on two trivalent graphs, creating Γn.
Alternatively, we could have made use of the identity 7.7 and applied it twice to contract the
graph Γ2n. The evaluation of the Γ2n graph is then given by:
Γ2n =
H2n
Θ2n
2
Θ2n = H2
2n
Θ2n
.
Then, using Proposition 7.3 we could again obtain the tail of the graph Γ2n. Using the correspon-
dence illustrated in Figure 11, these techniques give the tail of the inﬁnite family of alternating
links depicted in Figure 16.
References
[1] George E. Andrews and Bruce C. Berndt, Ramanujan’s lost notebook. Part I, Springer, New York, 2005.
MR2135178 (2005m:11001)
[2] Cody W. Armond, The head and tail conjecture for alternating knots, Algebr. Geom. Topol. 13 (2013), no. 5,
2809–2826. MR3116304


## Page 14


Q-SERIES AND QUANTUM SPIN NETWORKS
14
Figure 16. The tail of the graph Γn appearing on the left is equivalent to the tail
of the colored Jones polynomial of the family appearing on the right.
[3] Cody W. Armond and Oliver T. Dasbach, Rogers-Ramanujan type identities and the head and tail of the colored
Jones polynomial, arXiv:1106.3948 (2011).
[4] Khaled Bataineh, Mohamed Elhamdadi, and Mustafa Hajij, The colored Jones polynomial of singular knots, New
York J. Math. 22 (2016), 1439–1456. MR3603072
[5] Oliver T. Dasbach and Xiao-Song Lin, On the head and the tail of the colored Jones polynomial, Compos. Math.
142 (2006), no. 5, 1332–1342, doi: 10.1112/S0010437X06002296. MR2264669
[6] Mohamed Elhamdadi and Mustafa Hajij, Pretzel knots and q-series, Osaka J. Math. 54 (2017), no. 2, 363–381.
MR3657236
[7]
, Foundations of the colored Jones polynomial of singular knots, Bull. Korean Math. Soc. 55 (2018), no. 3,
937–956. MR3809678
[8] Mohamed Elhamdadi, Mustafa Hajij, and Masahico Saito, Twist regions and coeﬃcients stability of the colored
Jones polynomial, Trans. Amer. Math. Soc. 370 (2018), no. 7, 5155–5177, doi: 10.1090/tran/7128. MR3812106
[9] Stavros Garoufalidis and Thang T. Q. Lˆe, Nahm sums, stability and the colored Jones polynomial, Res. Math. Sci.
2 (2015), Art. 1, 55, doi: 10.1186/2197-9847-2-1. MR3375651
[10] Mustafa Hajij, The Bubble skein element and applications, J. Knot Theory Ramiﬁcations 23 (2014), no. 14,
1450076, 30. MR3312619
[11]
, The tail of a quantum spin network, Ramanujan J. Vol 40 (2016), no. 1, pp 135–176.
[12] Louis H. Kauﬀman, State models and the Jones polynomial, Topology 26 (1987), no. 3, 395–407. MR899057
[13] G. Masbaum and P. Vogel, 3-valent graphs and the Kauﬀman bracket, Paciﬁc J. Math. 164 (1994), no. 2, 361–381.
MR1272656
[14] J´ozef H. Przytycki, Fundamentals of Kauﬀman bracket skein modules, Kobe J. Math. 16 (1999), no. 1, 45–66.
MR1723531
[15] N. Reshetikhin and V. G. Turaev, Invariants of 3-manifolds via link polynomials and quantum groups, Invent.
Math. 103 (1991), no. 3, 547–597. MR1091619
[16] V. Turaev and H. Wenzl, Quantum invariants of 3-manifolds associated with classical simple Lie algebras, Inter-
nat. J. Math. 4 (1993), no. 2, 323–358. MR1217386
[17] Wataru Yuasa, A q-series identity via the sl3 colored Jones polynomials for the (2, 2m)-torus link, Proc. Amer.
Math. Soc. 146 (2018), no. 7, 3153–3166, doi: 10.1090/proc/13907. MR3787374
[18] Hans Wenzl, On sequences of projections, C. R. Math. Rep. Acad. Sci. Canada 9 (1987), no. 1, 5–9. MR873400
(88k:46070)
Department of Mathematics, University of South Florida, Tampa, FL USA
E-mail address: emohamed@mail.usf.edu
Department of Computer Science and Engineering, Ohio State University, Columbus, Ohio USA
E-mail address: hajij.1@osu.edu
Department of Mathematics, University Of Southern California, Los Angeles, CA USA
E-mail address: jslevitt@usc.edu

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
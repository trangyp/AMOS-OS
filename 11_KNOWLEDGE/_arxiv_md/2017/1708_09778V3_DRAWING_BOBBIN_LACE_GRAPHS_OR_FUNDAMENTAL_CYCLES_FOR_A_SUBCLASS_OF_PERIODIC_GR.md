---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1708.09778v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1708.09778v3_Drawing_bobbin_lace_graphs__or__Fundamental_cycles_for_a_subclass_of_periodic_gr

> Source: 1708.09778v3_Drawing_bobbin_lace_graphs__or__Fundamental_cycles_for_a_subclass_of_periodic_gr.pdf

> Pages: 18

---


## Page 1


Drawing bobbin lace graphs, or, Fundamental
cycles for a subclass of periodic graphs
Therese Biedl and Veronika Irvine ⋆
David R. Cheriton School of Computer Science, University of Waterloo
Abstract. In this paper, we study a class of graph drawings that arise
from bobbin lace patterns. The drawings are periodic and require a
combinatorial embedding with speciﬁc properties which we outline and
demonstrate can be veriﬁed in linear time. In addition, a lace graph draw-
ing has a topological requirement: it contains a set of non-contractible
directed cycles which must be homotopic to (1, 0), that is, when drawn
on a torus, each cycle wraps once around the minor meridian axis and
zero times around the major longitude axis. We provide an algorithm
for ﬁnding the two fundamental cycles of a canonical rectangular schema
in a supergraph that enforces this topological constraint. The polygo-
nal schema is then used to produce a straight-line drawing of the lace
graph inside a rectangular frame. We argue that such a polygonal schema
always exists for combinatorial embeddings satisfying the conditions of
bobbin lace patterns, and that we can therefore create a pattern, given
a graph with a ﬁxed combinatorial embedding of genus one.
1
Introduction
Bobbin lace is a 500-year-old ﬁbre art-form created by braiding threads together
in complex patterns. See Figure 1. Bobbin lace can depict landscapes, ﬁgures,
ﬂowers, as well geometric and abstract designs. Common to all bobbin lace com-
positions is the use of doubly periodic patterns to ﬁll regions of any shape or
size. It is the study of these periodic patterns that we pursue here. To create
bobbin lace, threads, which are wound around wooden bobbins to facilitate han-
dling, are arranged left to right in linear order t1, t2, . . . t2n−1, t2n. The lacemaker
selects four consecutive threads, starting at an odd index, and crosses the four
threads over and under each other to form an alternating braid. After one or
several crossings are made in this manner, the four threads are set aside and an-
other set of four (not the same four, but possibly using a subset of the original
four) is selected, again starting at an odd index, and braided. Since the selected
threads are consecutive starting at an odd index, we can describe the pattern
by tracking the movement of pairs of threads rather than individual strands.
The application of mathematics to the study of ﬁbre arts dates back to the
beginnings of computer science. A survey of various areas, including knitting and
weaving, is presented by Belcastro and Yackel [3]. Grishanov et al. take a deep
⋆Research supported by NSERC. Thank you to Anna Lubiw for helpful input.
arXiv:1708.09778v3  [cs.CG]  7 Sep 2017


## Page 2


(a)
(b)
(c)
Fig. 1. Bobbin lace. (a) Pattern, (b) Lace with two diﬀerent ζ(v) mappings, (c) Periodic
graph drawing. Four osculating circuits distinguished using black and gray.
look into knot theory and its relevance to the topology of textiles [6]. The second
author and Ruskey [7] were the ﬁrst to develop a mathematical model for bobbin
lace and express its patterns using graph drawings. Speciﬁcally, a lace pattern
can be represented as (Γ(G), ζ(v)) where G is a combinatorial embedding that
captures the ﬂow of pairs of threads from one grouping of four to another, Γ(G)
gives a speciﬁc drawing of G which assigns a geometry to the position of the
braids, and ζ(v) is a mapping from each node v ∈V (G) to a mathematical
braid word which speciﬁes the over and under crossings performed on the subset
of four threads that meet at v. A systematic exploration of diﬀerent ζ(v) map-
pings is straight-forward, although time consuming, and has been undertaken by
lacemakers for several traditional patterns; see [7] for more details. Discovering
which pairs of threads can be successfully combined, as represented by Γ(G), is
a much harder task and is therefore the focus of this paper.
The main question investigated in this paper is to decide, for a directed
graph with a ﬁxed rotation system, whether we can construct a straight-line
drawing that is a lace pattern. We argue that recognizing such graphs can be
done in linear time and depends only on their combinatorial structure (some of
these results were reported earlier [7]). Lace patterns are doubly periodic. As
a result, a lace graph can be drawn on the surface of a torus and lifted to its
universal cover, an inﬁnite, periodic, planar graph. A toroidal embedding can
be drawn as a straight-line planar graph drawing with a rectangular outer face
by choosing a canonical rectangular schema [1],[4]. The challenge is to ﬁnd two
fundamental cycles to serve as the borders of the rectangle under the constraints
of the topological requirements of the lace pattern and restrictions imposed by
the drawing algorithm itself. We show how to ﬁnd a suitable polygonal schema
for any valid combinatorial embedding.
2
Mathematical model of bobbin lace
We assume familiarity with graphs and combinatorial embeddings; see for exam-
ple [8]. Throughout this paper, G = (V, E) is a directed graph that comes with
a rotation system, i.e., a clockwise order of edges around each vertex. We will
assume that the rotation system describes a cellular combinatorial embedding
on an orientable surface (i.e., the complement of G on the orientable surface is a
collection of open topological disks). The genus of the cellular embedding can be


## Page 3


determined from the rotation system by computing the facial walk consisting of
edges and vertices incident to each face in order while walking around the face.
All embeddings of interest here have an Euler characteristic of 0.
A circuit is a closed path in which a vertex may be visited more than once
but no edges are repeated. A cycle is a closed path in which each vertex and
edge is only visited once. A contractible cycle is a cycle that can be continuously
retracted to a point. A canonical rectangular representation of a torus is bounded
by a pair of non-contractible cycles, also referred to as fundamental cycles, that
have only one vertex in common, their point of intersection.
2.1
Conditions on lace pattern graph embeddings
In a lace pattern graph, every vertex v must have exactly two incoming and
two outgoing edges, corresponding to two pairs of threads that meet at v, are
braided together and then separate. We call such a graph a 2-2-regular digraph.
Lace patterns are doubly periodic, i.e., they can tile the plane by translation
in two non-parallel directions. One “tile” of the repeat can be drawn using a
canonical rectangular schema in which the position of a thread intersecting the
horizontal boundaries of the schema has the same abscissa top and bottom and a
thread intersecting the vertical boundaries of the schema has the same ordinate
value left and right. In graph drawing this is called periodic.
We do not want lace created from a pattern to “fall apart”, i.e., the graph
needs to be suitably connected. In graph-theoretical terms, this means G must
be a cellular embedding.
For a lace pattern to be workable, there must exist a partial ordering of the
vertices such that, for any directed edge, the braid mapped to the tail vertex
is worked before that of the head. The pattern, when repeated over the inﬁnite
plane, cannot contain directed cycles, or equivalently, the associated graph on
the torus must be free from contractible directed circuits.
The graph may have loops but they must be non-contractible. Parallel edges
with the same orientation do not represent a change in the four threads being
braided and therefore do not appear in a lace graph. Parallel edges with opposite
orientation must form a non-contractible directed cycle. In other words, a lace
graph may be a multigraph but no loop or parallel edge can be a face.
In summary, the following three conditions are required for the combinatorial
embedding of any lace pattern graph G:
C1. G is a directed 2-2-regular digraph.
C2. The rotation system of G describes a toroidal cellular embedding in which
all facial walks contain at least 3 edges.
C3. All directed circuits of G are non-contractible.
It is easy to check in linear time whether (C1) holds. To test (C2), we ﬁrst
compute the facial walks to ascertain the number of faces, and can then de-
termine whether the embedding is toroidal since, by Euler’s formula, such an
embedding with n vertices and 2n edges must have exactly n faces.


## Page 4


To test (C3) in linear time, we take advantage of the regular structure of our
digraph via the following lemma:
Lemma 1. Presume a 2, 2-regular digraph has a toroidal cellular embedding G.
If G has a contractible directed circuit C, then G will have at least one face
bounded by a contractible directed circuit.
Proof. (Sketch) Arbitrarily declare one face to contain the origin so that “inside”
and “outside” are well-deﬁned for any contractible directed circuit C. Let OC
and IC be the number of faces outside and inside C, and consider a directed
contractible circuit C that maximizes |OC −IC|. Prove, by contradiction, that a
directed cycle containing an edge in its interior cannot maximize |OC −IC| and
therefore the inside of C is a face as required. Details are in the appendix.
⊓⊔
It follows that to verify condition (C3), we simply test whether any facial
walk is a directed circuit. Clearly this takes linear time.
There is one more important restriction for a workable bobbin lace pattern.
The threads in the periodic pattern are continuous; threads are neither removed
(by cutting) nor added (by knotting or weaving in). In other words, to ﬁll a
rectangle of ﬁxed width and undetermined height, a ﬁxed set of threads starts
at the top of the rectangle and the same set of threads terminates (not necessarily
in the same order) at the bottom of the rectangle. To achieve this, the threads
in one repeat of the pattern must not have a net drift to the right or left. See
[7] for a more detailed discussion of this thread conservation property.
To formulate the thread conservation property in a mathematically precise
way, we require additional terminology and some observations resulting from
(C1,C2,C3) which we will describe in the next section.
2.2
Osculating circuits and thread conservation
Fix a digraph G with a combinatorial embedding such that (C1,C2,C3) hold.
There are two ways in which edges can be arranged at a vertex v with indeg(v) =
outdeg(v) = 2: Either rotationally alternating in which edges alternate between
incoming and outgoing directions or rotationally consecutive with edges in the
order incoming, incoming, outgoing, outgoing. Irvine and Ruskey [7] showed that
the following condition is necessary for (C3):
C3′. At all vertices of G, the outgoing arcs are rotationally consecutive.
Under (C3′), we deﬁne the left/right incoming/outgoing edges of v as follows:
going in clockwise order around v, we encounter ﬁrst the left outgoing edge,
then the right outgoing edge, then the right incoming edge and ﬁnally the left
incoming edge. Consider two edge-disjoint directed circuits C1, C2 that have a
vertex v in common. There are two possible ways in which C1 and C2 can meet
at v. In an osculating intersection these circuits only touch (“kiss”), i.e., both
incoming and outgoing edges of C1 are on the left side of v and the edges of C2
are on the right side of v (or vice versa). In contrast, at a transverse intersection
the circuits truly cross, i.e., C1 enters from the left side of v and exits from the
right, C2 enters from the right and exits from the left (or vice versa).


## Page 5


Lemma 2. Presume (C1,C2,C3′) hold. The edges of G can be partitioned into
a set P(G) of disjoint directed circuits such that no two circuits in P(G) have a
transverse intersection. Furthermore, this partition is unique and can be found
in linear time.
Proof. Arbitrarily select an edge e1 of G as the start of a circuit P1. If this edge
is left incoming at its head v, then let e2 be the left outgoing edge at v, else let
e2 be the right outgoing edge at v. Put diﬀerently, e1 and e2 are on the “same
side” of v. Append e2 to P1 and repeat the operation at the head of e2. Since the
graph is ﬁnite, we eventually must close the circuit P1; this is the ﬁrst element
of the partition P(G). In fact, circuit P1 must exactly ﬁnish at edge e1, because
for any edge the rule of “stay on the same side” uniquely determines the edge
before and after in the circuit.
Now select some edge f1 of G that was not in P1, and repeat the process
starting at f1. The new circuit P2 will not contain an edge of P1 by the same
“stay on the same side” rule. Thus we obtain the next circuit in the partition.
Repeat until all edges belong to some circuit. Since there is never a choice about
which next edge to take, the partition is unique. Each edge is visited exactly
once resulting in a linear runtime.
⊓⊔
We call the circuits in P(G) the osculating circuits of G, see also Figure 1(c). We
distinguish two cases of P(G) based on whether or not the osculating circuits
are simple directed cycles. It turns out that when a circuit visits a vertex twice,
P(G) has a trivial structure.
Lemma 3. Presume (C1-C3) hold. If some osculating circuit P ∈P(G) visits
a vertex twice, then P is the only element in P(G).
Proof. Follow P1 ∈P(G), a non-simple osculating directed circuit, until the ﬁrst
time a vertex v ∈P1 is reached for the second time. P1 can be partitioned into
a simple directed cycle C′ (by taking the part from v to v that we just followed)
and a directed circuit C′′ (the rest of P1). Both C′ and C′′ are incident to v.
Fix an arbitrary drawing of G on the torus T . By (C3) C′ is non-contractible,
so cutting T along C′ produces a cylinder. The cut will split v into two vertices,
v′ and v′′, one on each boundary of the cylinder.
Because of the osculating construction of P1, C′ and C′′ must intersect trans-
versely at v (otherwise, P1 would have terminated the ﬁrst time it returned to
v). Thus C′′ contains an incident edge at each of the two copies, v′ and v′′, of v.
Taking the subpath D of C′′ between v′ and v′′, we obtain a path that travels
on the cylinder from one boundary to the other. Cutting along D will cut the
cylinder into one or more disks.
Now consider some other circuit Pi ∈P(G), Pi ̸= P1. It cannot have a trans-
verse crossing with either C′ or C′′, because P1 and Pi are osculating circuits.
Therefore, it intersects neither C′ nor D and we can conclude that Pi resides
entirely within (or on the boundary) of one of the disks of T −C′ −D. But
then Pi is a contractible directed circuit, a contradiction. So P(G) contains no
osculating circuits other than P1.
⊓⊔


## Page 6


The osculating partition can contain more than one element, see Figure 1(c).
It follows from the previous lemma that if |P(G)| > 1, then all circuits in P(G)
must be simple directed cycles.
In a transverse intersection under (C3′), if C1 uses the left incoming (and
right outgoing) edge of v we say that C1 crosses C2 left-to-right at v. Summing
over all shared vertices, we deﬁne the algebraic crossing number of two circuits
C1 and C2 to be:
ˆi(C1, C2) = #{C1 crosses C2 left-to-right} −#{C1 crosses C2 right-to-left}
Finally, using the following well known lemma, we can make a statement
about the homotopy class of the osculating circuits in P(G):
Lemma 4. [9, p. 209] Two closed simple curves C, C′ have ˆi(C, C′) = 0 if and
only if they belong to the same homotopy class.
Lemma 5. If (C1-C3) hold, then all directed cycles Pi ∈P(G) belong to the
same homotopy class.
Proof. If P(G) contains a non-simple circuit then, by Lemma 3, it is the only
member of P(G) and the claim holds trivially. Otherwise, the osculating circuits
of P(G) are all simple closed curves. None of them intersect transversally, which
means that ˆi(Pi, Pj) = 0 for all pairs of osculating circuits i ̸= j. This proves
the result by Lemma 4.
⊓⊔
A (canonical) polygonal schema for a toroidal graph consists of two funda-
mental cycles (called the meridian M and the longitude L ) such that M and L
intersect in exactly one point. Cutting G along the edges of M ∪L will result in
a topological disk. A circuit C belongs to homotopy class (m, ℓ) (with respect to
a ﬁxed polygonal schema) if ˆi(C, L) = m and ˆi(C, M) = ℓ.
With these terms in place, we can now state the thread conservation property
via the following constraint:
C4. There exists a meridian M, a longitude L and a partition P(G) of edges into
osculating directed circuits such that each circuit in the partition is in the
(1, 0)-homotopy class.
Fig. 2. A Dehn twist changes a valid lace graph on left into an invalid one on right.


## Page 7


The (1, 0)-homotopy class restriction ensures that at each upward repeat all
thread pairs return to the same left-right starting position. The thread conser-
vation property is impossible to formulate as a condition of the combinatorial
embedding because the homotopy class is aﬀected by how the graph is drawn
on the torus. In particular, consider Figure 2 which shows two drawings of the
same graph on the torus diﬀering by a homeomorphism known as a Dehn twist.
Both drawings have the same combinatorial embedding, yet on the left side of
Figure 2 the red (bold) osculating circuit returns to its starting point while on
the right side of the ﬁgure the osculating circuit drifts to the right.
Clearly, thread conservation demands that we ﬁx more than the combinato-
rial embedding of the graph. However, based only on the combinatorial embed-
ding, we can make a statement about the existence of a suitable graph drawing:
Lemma 6. Given a digraph G that satisﬁes (C1-C3), there exists a drawing of
G for which (C4) holds.
Proof. By the Dehn-Lickorish theorem (see e.g. [5]) there exists a homeomor-
phism that maps any simple, non-contractible cycle to the (1, 0) homotopy class
of the torus. By Lemma 5, such a homeomorphism will map all elements in P(G)
to the desired homotopy class.
⊓⊔
The main contribution of this paper is a linear time algorithm for ﬁnding such
a drawing:
Theorem 1. Given a digraph G that satisﬁes (C1-C3), we can draw a lace
pattern in linear time. The drawing resides in an O(n4) × O(n4)-grid.
Proof. In Section 3, we provide an algorithm for ﬁnding a polygonal schema
to satisfy (C4) for any digraph G that satisﬁes (C1-C3). We then use known
algorithms ([4], [1]) for straight-line rectangular-frame drawings to create a lace
pattern in the required time and space.
⊓⊔
3
Finding a polygonal schema
In general, ﬁnding a polygonal schema with vertex-disjoint interiors is NP-
hard [4]. However, for the purpose of drawing the lace-pattern, we do not need to
ﬁnd a polygonal schema within the given graph; it suﬃces (and in fact, is prefer-
able) to add vertices and edges to the graph and ﬁnd a polygonal schema within
the additions. In this manner, the original edges of G are not on the schema
boundary giving more freedom to where they can be placed. In this section we
describe how to ﬁnd such a supergraph with O(n) nodes.
DrawLacePattern Algorithm
A. Partition G into a set P(G) of osculating circuits and select one directed
circuit P ∗from the set.


## Page 8


B. Create the oﬀset graph O(G).
C. Find a simple cycle M in O(G) such that ˆi(M, P ∗) = 0 and M intersects
every edge of G at most once.
D. Find a simple cycle L in O(G) such that ˆi(L, P ∗) = ±1, M and L
intersect exactly once, and L intersects every edge of G at most once.
E. Use existing torus-drawing techniques to draw G on a rectangle with
meridian M and longitude L.
All steps are linear or constant time, and step E. will create a drawing of the
required size, proving the theorem. Step A. was explained in Section 2.2 already;
all other steps are explained below.
Creating the oﬀset graph: We ﬁrst create an oﬀset graph O(G) in which
we will choose a suitable meridian M and longitude L. Roughly speaking, O(G)
is obtained by creating two copies of every osculating circuit P in P(G), which
we will represent as ....
P (used to ﬁnd M) and P (used to ﬁnd L). In each copy,
the circuits are separated (they do not share vertices as they do in G) and are
simple cycles. The copies lie on top of G introducing crossings which we remove
by inserting dummy vertices. Finally, for the simple cycles of P, we connect the
two halves of each vertex, split in the process of separating osculating paths, by
introducing “crossover-edges”.
(b)
(a)
(c)
v
....
vℓ
vℓ
....
vr
vr
vc
Fig. 3. Create oﬀset graph. (a) Close-up near a vertex showing ....
P (thick, dashed,
square, orange), P (thick, solid, triangle, green), crossover-edges (thin, solid, purple)
and shortcut-edges (thin, dotted, blue). (b) Oﬀset graph of non-simple osculating cir-
cuit. (c) Oﬀset graph with multiple simple osculating cycles.
Figure 3 illustrates two such toroidal graph embeddings O(G), with O(n)
vertices and edges, which we will now deﬁne formally. The left-face of a directed
edge v →w is the face to the left of it while walking from v to w. For each
vertex in O(G) we deﬁne fℓ(v) to be the left-face of the left incoming and left
outgoing edges of v, fr(v) to be the right-face of the right incoming and right
outgoing edges of v, and fc(v) to be the face incident to the left incoming and
right incoming edges of v.
– Initially, O(G) contains all vertices and edges of G, embedded as in G.
– For every vertex v ∈V (G), add four new vertices ....
vℓ, vℓ, ....
vr , vr. Place ....
vℓ, vℓ
in fℓ(v) such that vℓis closer to the left incoming edge than ....
vℓ. Place ....
vr , vr
in fr(v) such that ....
vr is closer to the right incoming edge than vr.


## Page 9


– For every edge e = v →w ∈E(G), we add two new edges ....e and e. If e is
left outgoing at v, then ....e starts at ....
vℓand e starts at vℓ. else ....e starts at
....
vr and e starts at vr, If e is left incoming at w, then ....e ends at ....
wℓand e
ends at wℓ, else ....e ends at ....
wr and e ends at wr.
– Note that edge e ∈E(G) may be intersected by its copies ....e and e. This
occurs, for example, when e is right outgoing at its tail and left incoming
at its head. We remove these crossings (so that we again have a toroidal
embedding) in the standard way by inserting dummy vertices that subdivide
e, ....e , e. (In the following descriptions, we will ignore these dummy-vertices,
and speak of an edge e, even though it has become a path with 3 edges.)
– For every osculating circuit P there are now two circuits ....
P and P, using
for each edge e ∈P the corresponding edges ....e and e. Note that ....
P and
P are simple, even if P is not. When P visits a vertex v twice, once via
the incoming left and outgoing left edges of v and once via the incoming
right and outgoing right edges of v, the corresponding ....
P visits ....
vℓand ....
vr
respectively and similarly P visits vℓand vr. Due to the order of the copies
near v, ....
P and P do not cross.
– Next add the crossover-edge ev = (vℓ, vr) for each vertex v ∈V . To obtain
a toroidal embedding, route this edge so that it crosses three edges: the two
incoming edges of G at v and the edge ....e that is incoming to ....
vr . These
crossings are again replaced by dummy-vertices. In the crossover-edge insert
a vertex vc in the face fc(v).
– For a straight-line drawing, an edge e in E(G) must not cross the rectangular
frame twice. Consider an edge e that crosses e = v →w where e originates
inside the face fc(w), say e = vr →wℓ. It may happen that the chosen
longitude L contains e followed by the crossover-edge ew = (wℓ, wr) resulting
in a double crossing of e by L. To avoid this situation, we add a shortcut-
edge to O(G) that connects a point on e inside fc(w) to wc. Note that any
circuit using e ew acts the same (with respect to algebraic crossing numbers)
as a circuit shortened via the shortcut-edge, since all other crossings are
unaﬀected.
Finding the meridian: In step A. we selected an osculating circuit P ∗.
Deﬁne M to be the copy
....
P ∗of circuit P ∗in the oﬀset graph. M is a simple
cycle. It may cross P ∗repeatedly but it does so only by switching back and
forth between being left of P ∗and right of P ∗. In other words, ˆi(P ∗, M) = 0 as
desired. Finally M intersects every edge of G at most once by construction of
....
P .
Finding the longitude: Deﬁne L(G) to be the subgraph of O(G) taking
only the copies P of osculating circuits, the crossover-edges, and the shortcut-
edges. We claim that we can ﬁnd a suitable longitude in L(G). The algorithm is
quite simple (ﬁnd a shortest path within L(G), with some edges removed), but
arguing that it works is not.
Case 1) Circuit P ∗: First consider the easier case in which P ∗is not simple
and is therefore, by Lemma 3, the only element in P(G). Let v be a vertex visited
twice by P ∗, hence vℓand vr both belong to P ∗. Deﬁne L∗to be a subpath of


## Page 10


P ∗between vℓand vr and ˆL to be L∗plus the crossover-edge (vr, vℓ). We have
constructed P ∗such that it does not intersect
....
P ∗. So L∗does not intersect M.
The crossover-edge (vr, vℓ) intersects M exactly once. Therefore, ˆL intersects M
exactly once as desired.
L∗and P ∗may intersect numerous times between vℓand vr. But vℓis to
the left of P ∗while vr is to the right, so in total L∗has one more left-to-right
intersection than right-to-left-intersection. The crossover-edge (vr, vℓ) intersects
both incoming edges at v, and both of these edges belong to P ∗. This adds two
more right-to-left intersections, and so in total ˆi(ˆL, P ∗) = −1 as desired.
Case 2) Simple P ∗: If P ∗is simple then we ﬁnd L using a path that
connects “both sides” of P ∗without crossing P ∗. The existence of such a path
is non-trivial, and crucially needs condition (C2), i.e., that the embedding is
cellular. Speciﬁcally, we show:
Lemma 7. Presume (C1-C3) hold. Let P be a directed osculating cycle. Then
there exists a directed walk W in G that starts at a vertex v ∈P with a left
outgoing edge e1 ̸∈P, ends at a vertex w ∈P with a right incoming edge ek ̸∈P,
and has no transverse intersection or shared edges with P.
Proof. (Sketch) The edge e1 must exist otherwise the directed cycle P would
bound a face, contradicting (C2) or (C3). One can now argue that starting from
e1 and always taking the left outgoing edge, we must reach such an edge ek or
ﬁnd a contradiction to (C2). Details are in the appendix.
⊓⊔
Let Q be such a walk in G from v ∈P ∗to w ∈P ∗, shortened by eliminating
directed cycles (if any) so that it becomes a simple path. We obtain the longitude
L by “translating” Q into L(G) and adding a subpath of P ∗.
Note that the directed edges of Q need not be rotationally consecutive. For ex-
ample, ei ∈E(Q) may be right incoming at its head vertex x while ei+1 ∈E(Q)
may be left outgoing at its tail vertex x. If x ̸∈P ∗then we can can add the
crossover-edge (xℓ, xr) to connect ei and ei+1 without crossing M =
....
P ∗. If
x ∈P ∗but ei ̸∈P ∗and ei+1 ̸∈P ∗then no crossover-edge is required because ei
and ei+1 are rotationally consecutive. It is not possible to have x ∈P ∗and only
one of ei ∈P ∗or ei+1 ∈P ∗because of the way in which Q is deﬁned.
Formally, let Q = e1, . . . , ek be a simple path in G −E(P ∗) from v ∈P ∗to
w ∈P ∗and let L−= e1, . . . , ek be a simple path using the corresponding edges
in L(G) and crossover-edges as needed. L−begins at vℓsince e1 is left outgoing
and ends at wr since ek is right incoming. Deﬁne L∗to be the subpath of P ∗
connecting wℓto vr. Finally, deﬁne ˆL to be the simple cycle consisting of L−,
crossover-edge (wr, wℓ), L∗and crossover-edge (vr, vℓ).
Note that L−and L∗never cross the meridian M =
....
P ∗. The only place
where ˆL can intersect M is at the two crossover-edges (vr, vℓ) and (wr, wℓ). We
claim that exactly one of them intersects
....
P ∗. To see this, recall that P ∗uses the
right incoming and outgoing edge at v and the left incoming and outgoing edge
at w. The order of vertices in the vicinity of v is ....
vℓ, vℓ, v, ....
vr , vr, and
....
P ∗uses ....
vr ,
so (vr, vℓ) crosses
....
P ∗. On the other hand the order of vertices in the vicinity of


## Page 11


w is ....
wℓ, wℓ, w, ....
wr, wr, and
....
P ∗uses ....
wℓ, so (wr, wℓ) does not cross
....
P ∗. Therefore,
L and M cross exactly once as desired.
To see that ˆi(ˆL, P ∗) = ±1, observe that L−has no transverse intersections
with P ∗and so contributes nothing. L∗may intersect P ∗repeatedly, alternat-
ingly from left to right and from right to left, however, L∗starts on the left side
of P ∗at wℓand ends on the right side of P ∗at vr, so it has a net of one left
to right crossing. The crossover-edges (wr, wℓ) and (vr, vℓ) are both right to left
crossings. Thus ˆL has one more crossing from right to left than it has crossings
from left to right, yielding ˆi(ˆL, P ∗) = −1 as desired.
P ∗
v
w
M
v
w
L
M
v
vℓ
e1
w
ek
wr
M
(a)
(b)
(c)
Fig. 4. (a) M is a shifted copy of P ∗. (b) L exits from the left side of M at e1 and
returns on the right side of M at ek. Loops where shortcuts are required are shaded
purple. (c) Connect e1 to ek following P ∗.
Applying shortcuts: As desired, the simple cycle ˆL intersects M once and
has ˆi(ˆL, P ∗) = ±1. However, ˆL may intersect an edge e of G repeatedly. This
happens only when e transversely crosses e, and a crossover-edge at the tail
of e follows immediately after. Let L be the simple cycle obtained from ˆL by
substituting the shortcut-edge at any such edge e. This has the same algebraic
crossing number with P ∗, still crosses M exactly once, and is a suitable longitude.
We ﬁnally remark that the simplest way to ﬁnd L is as follows. Start with
graph L(G) and remove all dummy-vertices that lie on
....
P ∗. This eﬀectively dis-
allows any path in L(G) that crosses M. Pick any vertex v ∈P ∗and, in what
remains of L(G), ﬁnd a shortest path L−from vℓto vc (the vertex within the
crossover-edge (vr, vℓ)). Finally add the edge (vc, vℓ) to close the cycle into a
suitable longitude L.
Drawing the graph: Let T (G) be the graph obtained from O(G) by re-
moving all edges that do not belong to G, M or L and smoothing any degree-2
vertices. T (G) has a natural embedding on a torus with a well deﬁned merid-
ian and longitude. Cut T (G) along L to form graph C(G) which has a natural
embedding on a cylinder with top and bottom boundaries Lt and Lb. Cut C(G)
along M to obtain a planar graph R(G) with a natural embedding on a rect-
angle whose top/right/bottom/left sides are formed by the four boundary-paths
Lt/Mr/Lb/Mℓ. Figure 8 in the appendix illustrates this process.


## Page 12


In our construction, we have been careful to ensure that boundary-cycles
do not cross an edge of G more than once. As a consequence, we can now ap-
ply known algorithms for straight-line rectangular-frame drawings to R(G). The
ﬁrst such algorithm was given by Duncan et al. [4] and creates a drawing in an
O(n) × O(n2)-grid in linear time. Unfortunately, the algorithm does not neces-
sarily produce a periodic drawing. We therefore turn to the drawing algorithm
of Aleardi et al. [2], a modiﬁcation of the algorithm of Duncan et al. which en-
sures periodic drawings. This is still achieved in linear time but at the cost of
increasing the grid-size to O(n4) × O(n4)-grid. This proves Theorem 1.
4
Discussion and open problems
In this paper we provide an algorithm to generate a lace pattern given a directed
graph and a ﬁxed combinatorial embedding that satisfy the conditions (C1-C3).
Our main challenge was to produce a graph drawing such that the threads in the
pattern weave back and forth within a ﬁxed width (follow a directed circuit that
wraps once around the minor meridian axis and zero times around the major
longitude axis). It turns out that if (C1-C3) are satisﬁed we can easily deﬁne a
supergraph of linear size supporting a suitable rectangular schema and extract
the schema in linear time. With care, we can sure that neither the meridian nor
longitude of the schema intersects an edge of the graph twice, allowing us to
reuse existing graph drawing techniques.
Our drawings are still somewhat unsatisfying for use as lace patterns. Con-
sider an edge e ∈E(G) that crosses the rectangular schema, say the horizontal
border L. The edge is broken into two parts et and eb, where et intersects the top
of the rectangle along Lt and eb intersects the bottom along Lb. The algorithm
of Aleardi et al. [2] ensures that the end points of et and eb on L have the same
x-coordinate but for e to be truly seen as “one edge”, et and eb should also have
the same slope. The bend is clearly visible when viewing several tiled repeats
of the pattern as shown in Figure 5. At the current time, we cannot see a way
to simultaneously satisfy the topological (1, 0) homotopy constraint enforced by
the rectangular representation and provide smooth continuity of edges across
this rectangular boundary.
(a)
(b)
Fig. 5. Unwanted bends along border. (a) Result of algorithm. (b) Desired result.


## Page 13


References
1. Aleardi, L.C., Devillers, O., Fusy, ´E.: Canonical ordering for triangulations on the
cylinder, with applications to periodic straight-line drawings. In: Proceedings of
the 20th International Symposium on Graph Drawing (GD). pp. 376–387. Springer
(2012)
2. Aleardi, L.C., Fusy, ´E., Kostrygin, A.: Periodic planar straight-frame drawings with
polynomial resolution. In: Latin American Symposium on Theoretical Informatics.
pp. 168–179. Springer (2014)
3. Belcastro, S.M., Yackel, C.: Making mathematics with needlework: ten papers and
ten projects. AK Peters (2008)
4. Duncan, C.A., Goodrich, M.T., Kobourov, S.G.: Planar drawings of higher-genus
graphs. J. Graph Algorithms Appl. 15(1), 7–32 (2011)
5. Farb, B., Margalit, D.: A Primer on Mapping Class Groups. Princeton University
Press (2011)
6. Grishanov, S., Meshkov, V., Omelchenko, A.: A topological study of textile struc-
tures. part i: An introduction to topological methods. Textile Research Journal
79(8), 702–713 (2009)
7. Irvine, V., Ruskey, F.: Developing a mathematical model for bobbin lace. Journal
of Mathematics and the Arts 8(3–4), 95–110 (2014)
8. Mohar, B., Thomassen, C.: Graphs on surfaces. John Hopkins University Press
(2001)
9. Stillwell, J.: Classical topology and combinatorial group theory, Graduate Texts in
Mathematics, vol. 72. Springer-Verlag (1980)


## Page 14


Appendix A: Introduction to bobbin lace
Perhaps the easiest way to understand bobbin lace is to look at the six step
process by which it is made.
Fig. 6. Pattern in progress on lace pillow.
Step 1) Prepare the threads. To manage many long threads without
creating a tangled mess, each end of a thread is wound onto one of a pair of
bobbins. A bobbin, commonly made from wood, is about 10cm in length. One
end is ﬂanged to hold a length of thread and the other end, usually thicker and
sometimes weighted with beads, is the handle.
Step 2) Prepare the pattern. The lace is worked on top of a ﬁrm pillow
stuﬀed with material that can hold pins (such as styrofoam or sawdust). As
threads are braided together, they are held in place by pins pushed into the
pillow. To start a piece of lace, a pattern is copied onto stiﬀmaterial such
as card stock. Black dots in the pattern represent the position of pins. Before
starting to make the lace, all of these dots are pricked through to make small
holes. The pattern is then pinned to the pillow.
Step 3) Hang the bobbins. The middle of each thread is draped around
an anchoring pin at the top of the pattern with the pair of bobbins hanging down
on either side. Often the ﬁrst row of the pattern is a simple weave to anchor the
threads.
Step 4) Braid and pin. The lacemaker braids the threads working with
four consecutive threads at a time. During a sequence of braiding actions, the
lacemaker may insert a pin to hold the braid in place. The pin provides resis-
tance so that the lacemaker can apply tension to an individual thread without
distorting its neighbours.
Step 5) Advance to next set. Once four threads have been braided and
pinned, the lace maker moves on to braid another set of four consecutive threads.
This new set of threads may include two threads from the previous set but it may
also be formed from four completely new threads. Which four threads comprise
the next set depends on the pattern.
Steps 4 and 5 are repeated until the lace pattern is completed.
Step 6) Finish. The threads are secured (sometimes with a knot, sometimes
by weaving them back into the lace) and trimmed oﬀ. The pins are removed and


## Page 15


the lace may be lifted oﬀthe pillow. The ﬁnished lace is held together by the
over and under crossings of the threads and friction.
Appendix B: Proof of Lemma 1
Lemma 1. Presume a 2, 2-regular digraph has a toroidal cellular embedding G.
If G has a contractible directed circuit C, then G will have at least one face
bounded by a contractible directed circuit.
(b)
(c)
×
C
C′
v
w
×
C
C′
v
w
(a)
C
C′
v
w
Fig. 7. Three cases in proof of Lemma 1. Origin is represented by ×. (a) C′ stays inside
C throughout (b) Origin inside C′. (b) Origin outside C′.
Proof. Arbitrarily declare one face to contain the origin so that “inside” and
“outside” are well-deﬁned for any contractible directed cycle C. Let OC and IC
be the number of faces outside and inside C, and consider a directed contractible
cycle C that maximizes |OC −IC|.
Assume that C is not a face and therefore there exists some vertex v ∈C
with an incident edge e that is not on C and belongs to the inside of C. Follow a
directed path P starting with e while staying inside C until we reach a vertex w
where either (a) P returns to a vertex on P for the ﬁrst time, or (b) P reaches
another vertex on C for the ﬁrst time. Because G is a 2, 2-regular digraph with
a ﬁnite number of vertices, one of these two cases must eventually occur. (Note:
if v is the head endpoint of e, P follows the edges in reverse direction).
If w ∈P, then the path from w to w along P has formed another directed
cycle C′ that stays inside C throughout and therefore is also contractible (see
Figure 7(a)).
If w ∈C,then we can ﬁnd a directed cycle C′ by taking P from v to w and
then C from w to v.
Consider the case where OC ≥IC (the other case is symmetric). Examine
|OC′ −IC′|. If the origin is inside C′ (see Figure 7(b)), then IC′ < IC and
OC′ > OC, therefore |OC′ −IC′| ≥OC′ −IC′ > OC −IC = |OC −IC|, a
contradiction. If the origin is outside C′ (see Figure 7(c)) then the outside of
C′ is strictly inside the inside of C, so OC′ < IC and IC′ > OC, which implies
|OC′ −IC′| = |IC′ −OC′| ≥IC′ −OC′ > OC −IC = |OC −IC|, a contradiction
to the choice of C.
We therefore conclude that no vertex on C has an incident edge strictly inside
C and therefore the inside of C is a face as required.


## Page 16


We can easily extend this proof to the case where C is a contractible directed
circuit by noting that any transverse intersection in C can be replaced by an
osculating intersection thus dividing C into two or more smaller circuits. We
therefore assume that any time C visits a vertex v twice, it does not cross
itself transversely. We can very closely approximate a circuit C that is free of
transverse crossings by duplicating any repeated vertex v and moving the two
copies slightly apart. The result is a simple directed cycle.
⊓⊔
Appendix C: Proof of Lemma 7
Before we can prove Lemma 7, we need a few deﬁnitions and observations. We
will call a simple directed circuit C a leftmost circuit if all edges of C are left
outgoing at their respective tails. Observe that any leftmost circuit C in a 2-2-
regular digraph is actually a cycle, because no vertex can have two left outgoing
edges incident to it.
Consider two simple cycles P, Q. We already deﬁned the algebraic crossing
number ˆi(P, Q) if P and Q meet in a ﬁnite number of points. However, we need
a similar concept even if P and Q share one or more edges. To deﬁne this,
replace P and Q by cycles P ′ and Q′ that are arbitrarily close to P and Q in
such a way that P ′ and Q′ intersect in a ﬁnite number of points, and deﬁne
ˆi(P, Q) := ˆi(P ′, Q′). It is not hard to verify that this number is independent of
the choice of P ′ and Q′ since we use the algebraic crossing number (rather than
the geometric one).
Now we can make the following observation of leftmost cycles:
Lemma 8. Presume (C1-C3) hold. Let C be a leftmost cycle. Then C does not
bound a face, and ˆi(C, P) ̸= 0 for all osculating circuits P ∈P(G).
Proof. C cannot possibly bound a face, because it is a directed circuit (hence
non-contractible by (C3)) while facial circuits are contractible by (C2). There-
fore, there must be some edge eℓon the left side of C that shares a vertex v with
C, but does not belong to C. Since C uses only left outgoing edges, eℓis neces-
sarily a left incoming edge. Let Pℓbe the osculating circuit containing eℓ. This
circuit continues from eℓalong C for possibly some time, but eventually must
leave C again to return back to eℓ. Pℓcan leave C only at a right outgoing edge,
because the left outgoing edges always belong to C. Therefore in this stretch Pℓ
has crossed C going from left to right.
Note that Pℓcan never cross C from right to left, because all left outgoing
edges incident to a vertex in C belong to C. Therefore ˆi(Pℓ, C) ̸= 0.
Following from Lemma 4, Pℓand C do not belong to the same homotopy
class. From Lemma 5, we know that all P ∈P(G) belong to the same homotopy
class so we can conclude ˆi(P, C) ̸= 0 for all P ∈P(G).
⊓⊔
Now we can prove our main theorem:
Lemma 7. Presume (C1-C3) hold. Let P be a simple osculating cycle. Then
there exists a directed walk W in G that starts at a vertex v ∈P with a left


## Page 17


outgoing edge e1 ̸∈P, ends at a vertex w ∈P with a right incoming edge ek ̸∈P,
and has no transverse intersection or shared edges with P.
Proof. Since P is a directed cycle, it is non-contractible by (C3) and does not
bound a face by (C2). Therefore, there must be some edge on the left side of P
that shares a vertex v with P, but does not belong to P. If, say, the left incoming
edge of v is not in P, then P uses the right incoming and right outgoing edge
at v (because P follows rotationally consecutive edges), and so the left outgoing
edge of v is also not in P. Therefore edge e1 exists.
Now create a leftmost walk Wℓstarting with e1, then taking the left outgoing
edge at its head, and continue taking left outgoing edges until one of the following
happens:
1. We reach a vertex w ∈P via a right incoming edge. In this case we have found
the required path W and stop. Since we stop as soon as the head vertex w of
a right incoming edge ek of Wℓis also a vertex of P, we can conclude that,
before arriving at w, if we visited any other vertices in P, then these vertices
were reached from a left incoming edge, ei, 1 ≤i < k. Since Wℓalways
follows the left outgoing edge and P always follows rotationally consecutive
edges, we can conclude that the left incoming edge ei and left outgoing edge
ei+1 were not edges in P and the meeting of Wℓand P was an osculating
intersection rather than a transverse intersection.
2. Wℓrepeats a vertex, and the resulting directed cycle C does not contain
vertices of P. Then ˆi(C, P) = 0, which contradicts Lemma 8. This case
cannot happen.
3. Wℓrepeats a vertex, and the resulting directed cycle C contains vertices of
P. Since we did not stop with Case 1, all such vertices of C reach P from
the left. Following the same argument used in Case 1, all meetings of C with
P are osculating resulting in ˆi(C, P) = 0. This again contradicts Lemma 8
so this case cannot happen.
The graph is ﬁnite and neither Case 2 nor 3 can happen, therefore Case 1 even-
tually must happen and we have found W.
⊓⊔
Appendix D: An example of the meridian and longitude
Figure 8 illustrates how the graph G (of Figure 3(b)) is converted into a rect-
angular representation. We consider two diﬀerent choices for L. Note that while
both of them are perfectly ﬁne longitudes, the left one is more visually appealing,
principally because L and G have signiﬁcantly fewer crossings. To minimize the
number of times L crosses G, assign a weight to the edges of L(G) according to
the number of endpoints the edge has that are also a vertex or dummy vertex
of an edge in G.


## Page 18


(a)
(b)
(c)
(d)
0
1
1
0
0
0
0
1
1
1
1
0
0
1
1
Fig. 8. Find rectangular representation. (a) Shortest path L. (b) Alternate L. (c) Draw
graph with polygonal schema deﬁned in (a). (d)Draw graph with polygonal schema
deﬁned in (b).

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
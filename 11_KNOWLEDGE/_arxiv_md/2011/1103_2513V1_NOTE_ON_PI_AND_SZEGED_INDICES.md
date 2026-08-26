---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1103.2513v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1103.2513v1_Note_on_PI_and_Szeged_indices

> Source: 1103.2513v1_Note_on_PI_and_Szeged_indices.pdf

> Pages: 10

---


## Page 1


arXiv:1103.2513v1  [math.CO]  13 Mar 2011
Note on PI and Szeged indices
Aleksandar Ili´c
Faculty of Sciences and Mathematics
University of Niˇs, Serbia
e-mail: aleksandari@gmail.com
November 26, 2024
Abstract
In theoretical chemistry molecular structure descriptors are used for modeling physico-
chemical, pharmacologic, toxicologic, biological and other properties of chemical com-
pounds. In this paper we study distance-based graph invariants and present some im-
proved and corrected sharp inequalities for PI, vertex PI, Szeged and edge Szeged topo-
logical indices, involving the number of vertices and edges, the diameter, the number of
triangles and the Zagreb indices. In addition, we give a complete characterization of the
extremal graphs.
Key words: Molecular descriptors; PI index; Szeged index; Zagreb index; Distance in
graphs.
AMS Classiﬁcations: 05C12, 92E10.
1
Introduction
Let G = (V, E) be a connected simple graph with n = |V | vertices and m = |E| edges.
For vertices u, v ∈V , the distance d(u, v) is deﬁned as the length of the shortest path
between u and v in G. The diameter diam(G) is the greatest distance between two vertices
of G.
The distance between the vertex w and the edge e = uv is deﬁned as d′(w, e) =
min(d(w, u), d(w, v)).
In theoretical chemistry molecular structure descriptors (also called topological indices)
are used for modeling physico-chemical, pharmacologic, toxicologic, biological and other prop-
erties of chemical compounds [6]. There exist several types of such indices, especially those
based on vertex and edge distances. Arguably the best known of these indices is the Wiener
index W, deﬁned as the sum of distances between all pairs of vertices of the molecular graph
[4, 24],
W(G) =
X
u,v∈V
d(u, v).
Besides of use in chemistry, it was independently studied due to its relevance in social
science, architecture and graph theory. With considerable success in chemical graph theory,
various extensions and generalizations of the Wiener index are recently put forward [19, 25].
Let e = uv be an edge of the graph G. The number of vertices of G whose distance to the
vertex u is smaller than the distance to the vertex v is denoted by nu(e). Analogously, nv(e)
is the number of vertices of G whose distance to the vertex v is smaller than the distance to
1


## Page 2


the vertex u. Similarly, mu(e) denotes the number of edges of G whose distance to the vertex
u is smaller than the distance to the vertex v. We now deﬁne four topological indices: PI,
vertex PI, Szeged and edge Szeged indices of G as follows
PI(G)
=
X
e∈E
mu(e) + mv(e)
[8, 13, 15]
PIv(G)
=
X
e∈E
nu(e) + nv(e)
[2, 9, 16, 21, 22]
Sz(G)
=
X
e∈E
nu(e) · nv(e)
[3, 7, 11, 17]
Sze(G)
=
X
e∈E
mu(e) · mv(e)
[1, 5, 14].
Notice that for trees W(G) = Sz(G) and for bipartite graphs PIv(G) = nm.
The paper is organized as follows. In Section 2 we present two improved inequalities on
PIv, PI, Sz and Sze indices, and completely describe the extremal graphs. In Section 3 we
prove sharp lower bounds on the vertex PI and Szeged index involving Zagreb indices and
correct the equality cases for the upper bound involving the number of triangles. In Section 4
we correct the equality case regarding PI and edge Szeged index and present new sharp bound
using P´olya–Szeg¨o inequality.
2
Improved inequalities for PI and Szeged indices
Let Xn be the set of graphs on n vertices, such that for every edge e = uv ∈E(G) it holds
min(nv(e), nu(e)) = 1. It is obvious that the complete graph Kn belongs to Xn, and we
will exclude Kn in the sequel. By simple calculation, PIv(Kn) = 2|E(Kn)| = n(n −1) and
Sz(G) = |E(Kn)| = n(n−1)
2
.
A chordal graph is a simple graph such that each of its cycles of four or more vertices has
a chord, which is an edge joining two vertices that are not adjacent in the cycle.
In [5] the authors stated that a graph G from Xn must be a complete graph or a chordal
graph of diameter 2. It follows that the set Xn is composed of the graphs with diameter 2 such
that there are no induced path P4 or cycle C4 in the graph G. This is the full characterization
of graphs from Xn.
Namely, let G be a graph with no induced P4 or C4. It follows that diameter of G is less
than or equal to two. Since Kn is the unique graph with diameter one, we can assume that
diameter of G is equal to 2. Consider an arbitrary edge e = uv. Since G does not contain
induced P4 or C4, there are no two vertices u′ and v′ such that u′ is a neighbor of u, v′ is
a neighbor of v, d(v, u′) > 1 and d(u, v′) > 1. Since diam(G) = 2, for the vertices w that
are not adjacent with u or v, it holds d(v, w) = d(u, w) = 2. Finally, either nv(e) = 1 or
nu(e) = 1.
Theorem 2.1 Let G be a connected graph with n vertices and m edges. Then
PIv(G) ≤Sz(G) + m,
with equality if and only if G ∈Xn.
2


## Page 3


Proof. For an arbitrary edge e = uv, we have the following inequality
nv(e) + nu(e) ≤nv(e) · nu(e) + 1,
which is equivalent with (nv(e) −1)(nu(e) −1) ≥0. By adding similar inequalities for all
edges e ∈E(G), we get PIv(G) ≤Sz(G) + m. The equality holds if and only if nv(e) = 1 or
nu(e) = 1 for all edges e ∈E(G), i.e. G ∈Xn.
■
Remark 2.2 The authors in [5] proved the inequality PIv(G) ≤2Sz(G). The inequality
from Theorem 2.1 is stronger, since Sz(G) ≥m.
Remark 2.3 Let G be an arbitrary graph from Xn. It can be observed that G contains a
vertex with degree n−1. Namely, consider a vertex v with the maximum degree k < n−1. Let
v1, v2, . . . , vk be the neighbors of v, and assume that u is not adjacent to v. Since the diameter
of G is equal to 2, some of the neighbors of v are adjacent to u – and let one such vertex be
vi. In this case, for e = vvi it follows 1 = d(vi, u) < d(v, u) = 2, and nvi(e) ≥2. Therefore,
vi must be adjacent to all vertices v1, v2, . . . , vp, which implies that deg(vi) > deg(v) = k.
This is impossible, and it follows that v is adjacent to all vertices from G.
Let Yn be the set of graphs on n vertices, such that for every edge e = uv ∈E(G) it holds
min(mv(e), mu(e)) = 1. It is obvious that no graph from Yn contains pendent vertex (for a
pendent vertex v with the only neighbor u it holds mv(uv) = 0). Therefore, the minimum
vertex degree of graphs from Yn is greater than or equal to 2. If all vertices have degree 2,
then G ∼= Cn and it can be easily seen that only C3 and C4 belong to Yn.
The vertex v is called branching if deg(v) > 2. Let G be an arbitrary graph from Yn and
let v be an arbitrary branching vertex. For the edge vu we have mv(e) ≥2, and it follows
that mu(e) = 1. Therefore, all neighbors of the branching vertices have degree two. If G
contains exactly one branching vertex v, then G is composed of the union of cycles C3 and
C4 having the vertex v in common.
Now assume that G contains at least two branching vertices. Let Pd = w0w1 . . . wd be
the shortest path connecting vertices v and u, such that w0 = v, wd = u, deg(v) ≥3 and
deg(u) ≥3. If d > 2, for the edge e = vw1 we have mv(e) ≥2 and mw1 ≥2 (since the edge
w2w3 is closer to u than to v). Therefore, the distance between any two branching vertices
is equal to two. If G contains at least three branching vertices, the contradiction follows by
considering the edge e = vu′ on Fig. 1 (red edges are closer to u′ than to v). Finally, in this
case G contains exactly two branching vertices connected by paths of length two.
The set Y12 is presented on Fig. 2.
It can be easily proved by mathematical induction that the number of graphs in Yn is
equal to
|Yn| =







0
n = 1, 2
1
n = 3, 4
⌊n−1
6 ⌋+ 1,
n ≡2
(mod 6),
⌊n−1
6 ⌋+ 2,
otherwise.
Remark 2.4 The authors in [5] wrongly stated in Theorem 2 that if min(mu(e), mv(e)) = 1
then G is a cycle of length ≤4.
Let δ(G) denote the minimal vertex degree in the graph G.
3


## Page 4


Figure 1:
Contradiction with three branching vertices.
Figure 2:
The set Y12.
Theorem 2.5 Let G be a connected graph with n vertices, m edges and δ(G) ≥2. Then
PI(G) ≤Sze(G) + m,
with equality if and only if G ∈Yn.
Proof. The proof is similar to those of Theorem 2.1.
The equality holds if and only if
mv(e) = 1 or mu(e) = 1 holds for all edges e ∈E(G), or equivalently G ∈Yn.
■
3
Sharp bounds involving Zagreb indices and number of tri-
angles
One of the oldest graph invariants are the ﬁrst and the second Zagreb indices [6, 10], deﬁned
as follows
M1(G)
=
X
u∈V (G)
deg(v)2
M2(G)
=
X
uv∈E(G)
deg(u)deg(v).
Let t(G) denote the number of triangles K3 in the graph G.
Proposition 3.1 Let G be a connected graph with diameter 2. Then,
PIv(G) = M1(G) −6t(G).
4


## Page 5


Proof. Let e = uv be an arbitrary edge, such that it belongs to exactly t(e) triangles.
Adjacent vertices of v that are not neighbors of u are closer to v than u, and vice versa. For
the vertices w that are not neighbors of u or v, it holds d(v, w) = d(u, w) = 2. Therefore,
PIv(G)
=
X
e∈E(G)
nv(e) + nu(e)
=
X
e∈E(G)
deg(v) + deg(u) −2t(e)
=
X
v∈V (G)
deg2(v) −2
X
e∈E(G)
t(e)
=
M1(G) −6t(G),
since we counted each triangle three times. This completes the proof.
■
Remark 3.2 In [21], the authors stated that
nu(e) + nv(e) ≥deg(u) + deg(v) −t,
where t is a number such that every edge of G lie in exactly t triangles of G. Similarly as in
Proposition 3.1, this should be corrected to
nu(e) + nv(e) ≥deg(u) + deg(v) −2t(e).
After summing over all edges of G, we get
Pv(G) ≥M1(G) −6t(G).
Similarly, we have the following
Proposition 3.3 Let G be a connected graph with diameter 2, such that every edge belongs
to exactly t triangles. Then,
Sz(G) = M2(G) −t · M1(G) + m · t2.
A graph G = SRG(v, k, λ, µ) is strongly regular if G is k-regular v-vertex graph such that
every two adjacent vertices have λ common neighbors, while every two non-adjacent vertices
have µ common neighbors. A simple corollary of Proposition 3.1 and Proposition 3.3 is [5]
PIv(SRG(v, k, λ, µ))
=
vk2 −kvλ
Sz(SRG(v, k, λ, µ))
=
mk2 −2mkλ + mλ2.
The following upper bound on the vertex PI index was proved in [2].
Theorem 3.4 Let G be a connected graph with n vertices and m edges. Then,
PIv(G) ≤nm −3t(G).
5


## Page 6


The authors moreover claimed, that the equality holds if an only if G is a bipartite graph
or G ∼= K3. But this is not true. Namely, the equality holds if and only if for every edge
e = uv from G holds nu(e) + nv(e) = n −t(e). If t(G) = 0, then PIv(G) ≤nm if and only
if G is a bipartite graph. Otherwise, the extremal graph must contain a triangle. For the
complete graph it holds
n(n −1) = PIv(Kn) = n ·
n
2

−3
n
3

.
We checked all graphs on 3 ≤n ≤10 vertices with the help of Nauty [20], and the
computational results are presented in Table 1, while the extremal graphs with n = 4, 5, 6
vertices are presented on Fig. 3. It is interesting that the diameter of all extremal graphs
(except Kn) is two.
n
3
4
5
6
7
8
9
10
count
1
2
4
7
11
17
25
36
Table 1: The number of extremal non-bipartite small graphs.
Figure 3:
Non-bipartite extremal graphs for n = 4, 5, 6 with PIv values.
In addition, every extremal graph does not contain induced graph C′
3, composed of a
triangle with a pendent edge attached to one vertex of a triangle (otherwise the equality
nu(e) + nv(e) = n −t(e) does not hold).
A graph is odd-hole-free if it has no induced subgraph that is a cycle of odd length greater
than 3. Note that the equality holds in Theorem 3.4 for odd-hole-free graphs.
A graph G is a complete k-partite graph if there is a partition V1 ∪V2 ∪. . . ∪Vk = V (G)
of the vertex set, such that uv ∈E(G) iﬀu and v are in diﬀerent parts of the partition. If
|Vi| = ni, then G is denoted by Kn1,n2,...,nk. It can be easily proved that the equality also holds
in Theorem 3.4 for complete k-partite graphs Kn1,n2,...,nk. Namely, consider an arbitrary edge
e = vivj that connects parts Vi and Vj. The number of triangles that contain the edge e is
n −ni −nj, while nvi(e) = nj and nvj(e) = ni, and the relation nvi(e) + nvj(e) = n −t(e)
holds.
For the completeness, we state the similar result for the Szeged index [3].
6


## Page 7


Theorem 3.5 Let G be a connected graph with n vertices, m edges and t(G) triangles. Then,
Sz(G) ≤1
4n2m −3t(G).
(1)
If equality holds in (1), then G is bipartite (so in particular t(G) = 0), regular, n is even and
the minimum vertex degree is greater than 1.
A graph G is distance-balanced if |nv(e)| = |nu(e)| holds for any edge e = uv of G (see
[12, 18]). In [11] it was proven that a connected bipartite graph G is distance-balanced if and
only if Sz(G) = 1
4n2m. Recently in [1] the authors presented a simple proof of the conjecture
from [17] that the complete balanced bipartite graph K⌊n/2⌋,⌈n/2⌉has maximum Szeged index
among all connected graphs with n vertices.
Theorem 3.6 Let G be a connected triangle-free graph with n ≥3 vertices. Then,
Sz(G) ≥M2(G),
with equality if and only if G has diameter 2.
Proof. Let e = uv be an arbitrary edge of G. Since G is a triangle-free graph, it follows
nv(e) · nu(e) ≥deg(v) · deg(u).
Therefore,
Sz(G) =
X
e∈E(G)
nv(e) · nu(e) ≥
X
e∈E(G)
deg(v) · deg(u) = M2(G).
Let G be a triangle-tree graph such that Sz(G) = M2(G). Since G ̸∼= Kn, the diameter of G
is greater than or equal to 2. On the other side, if diameter is greater than 2, we can consider
induced path P4 = w0w1w2w3 and for the edge e = w0w1 it follows that nw1(e) > deg(w1)
since d(w1, w3) = 2 < 3 = d(w0, w3). Therefore, diam(G) = 2. In this case, for all vertices w
that are on distance greater than one from the vertices v and u holds d(v, w) = d(u, w) = 2
and ﬁnally nv(e) · nu(e) = deg(v) · deg(u). This completes the proof.
■
4
Further relations
Theorem 4.1 Let G be a connected graph with n vertices and m edges. Then,
PI(G) ≥
4
m −1SZe(G),
with equality if and only if m is odd and G ∼= Cn.
Proof. Let e = uv be an an arbitrary edge of G.
Using the arithmetic-geometric mean
inequality, we have (mu(e) + mv(e))2 ≥4mu(e)mv(e). Therefore,
(m −1)PI(G)
=
X
e∈E(G)
(m −1)(mu(e) + mv(e))
≥
X
e∈E(G)
(mu(e) + mv(e))2
≥
X
e∈E(G)
4mu(e)mv(e) = 4Sze(G).
7


## Page 8


The equality holds if and only if mu(e) = mv(e) = m−1
2
for every e ∈E(G). It follows that G
does not have pendent vertices, and therefore G is not a tree. Finally, G must contain a cycle,
and let C = v1v2 . . . vk be the shortest cycle contained in G. If k is even, by considering the
opposite edges we simply get mvi(e)+mvi+1(e) < m−1. If k is odd and G ̸∼= Cn, there exist a
vertex u not belonging to C, and without loss of generality suppose that u is a neighbor of v1.
In this case d(v(k+1)/2, u1v) = d(v(k+3)/2, u1v) = k−1
2 , and for the edge e = v(k+1)/2v(k+3)/2
we get mv(k+1)/2(e) + mv(k+3)/2(e) < m −1. Therefore, k = n is odd number and G ∼= Cn. ■
Remark 4.2 In [5], the authors stated in Theorem 4 (b) that PI(G) ≥
4
m−1SZe(G) with
equality if and only if m −1 is even and G is a tree with an odd number of vertices or a cycle
of odd length.
We will establish another relation between Szeged and vertex PI index, using the following
P´olya–Szeg¨o inequality [23].
Theorem 4.3 Let a1, a2, . . . , an and b1, b2, . . . , bn be positive real numbers such that for 1 ≤
i ≤n holds a ≤ai ≤A and b ≤bi ≤B, with a < A and b < B. Then,
 n
X
i=1
a2
i
!
·
 n
X
i=1
b2
i
!
≤1
4
 r
AB
ab +
r
ab
AB
!2
·
 n
X
i=1
aibi
!2
.
The equality holds if and only if the numbers
p =
A
a
A
a + B
b
· n
and
q =
B
b
A
a + B
b
· n
are integers, a1 = a2 = . . . = ap = a, ap+1 = ap+2 = . . . = an = A, b1 = b2 = . . . = bp = B
and bq+1 = bq+2 = . . . = bn = b.
Remark 4.4 By extending the proof of Theorem 4.3, if we allow a = A or b = B, the equality
holds also if AB = ab, i. e. a1 = a2 = . . . = an = a = A and b1 = b2 = . . . = bn = b = B.
Theorem 4.5 Let G be a simple graph with n vertices and m edges. Then
32mn · Sz(G) ≤(n + 2)2 · PI2
v(G),
with equality if and only if m = 0 or n = 2.
Proof.
Using the arithmetic-geometric mean inequality, it follows
4
X
e∈E(G)
nu(e)nv(e) ≤
X
e∈E(G)
(nu(e) + nv(e))2.
(2)
By setting in Theorem 4.3 the values ai = 1 and bi = nu(ei) + nv(ei) for i = 1, 2, . . . , m, we
have
m
X
i=1
12 ·
X
e∈E(G)
(nu(e) + nv(e))2 ≤(AB + ab)2
4ABab
·

X
e∈E(G)
nu(e) + nv(e)


2
.
8


## Page 9


Since A = a = 1, we need to estimate upper and lower bounds for bi, b = mine∈E(G) nu(e) +
nv(e) ≥2 and B = maxe∈E(G) nu(e) + nv(e) ≤n. By analyzing the function x + 1
x it follows
(B + b)2
4Bb
= 1
4
B
b + b
B

+ 1
2 ≤(n + 2)2
8n
.
Finally, we get
m ·
X
e∈E(G)
(nu(e) + nv(e))2 ≤(n + 2)2
8n
·

X
e∈E(G)
nu(e) + nv(e)


2
.
(3)
Combining Equations (2) and (3), we complete the proof. The equality holds if and only if
p =
n
1+ n
2 =
2n
n+2 is integer or b = B, which is possible only for n = 2. Therefore, the equality
holds if and only if m = 0 (in this case Sz(G) = PIv(G) = 0) or n = 2.
Acknowledgement.
This work was supported by Research Grant 144007 of Serbian
Ministry of Science.
The author is grateful to Professor Sandi Klavˇzar for his generous
help and valuable suggestions that improved this article. The author is also thankful to the
anonymous referees for their remarks, which have improved the presentation of this paper.
References
[1] E. Chiniforooshan, B. Wu, Maximum values of Szeged index and edge-Szeged index of
graphs, Electron. Notes Discrete Math. 34 (2009) 405–409.
[2] K. C. Das, I. Gutman, Estimating the vertex PI index, Z. Naturforsch. 65a (2010) 240–
244.
[3] K. C. Das, I. Gutman, Estimating the Szeged index, Appl. Math. Lett. 22 (2009) 1680–
1684.
[4] A. Dobrynin, R. Entringer, I. Gutman, Wiener index of trees: theory and applications,
Acta Appl. Math. 66 (2001) 211–249.
[5] G. H. Fath-Tabar, M. J. Nadjaﬁ-Arani, M. Mogharrab, A. R. Ashraﬁ, Some Inequalities
for Szeged-Like Topological Indices of Graphs, MATCH Commun. Math. Comput. Chem.
63 (2010) 145–150.
[6] I. Gutman, O. E. Polansky, Mathematical Concepts in Organic Chemistry, Springer–
Verlag, Berlin, 1986.
[7] I. Gutman, A. Dobrynin, The Szeged index – a success story, Graph Theory Notes N.
Y. 34 (1998) 37–44.
[8] J. Hao, Some graphs with extremal PI index, MATCH Commun. Math. Comput. Chem.
63 (2010) 211–216.
[9] A. Ili´c, On the extremal graphs with respect to the vertex PI index, Appl. Math. Lett.,
in press.
9


## Page 10


[10] A. Ili´c, D. Stevanovi´c, On Comparing Zagreb Indices, MATCH Commun. Math. Comput.
Chem. 62 (2009) 681–687.
[11] A. Ili´c, S. Klavˇzar, M. Milanovi´c, On distance-balanced graphs, European J. Combin. 31
(2010) 733–737.
[12] J. Jerebic, S. Klavˇzar, D. F. Rall, Distance-balanced graphs, Ann. Combin. 12 (2008)
71–79.
[13] P. V. Khadikar, S. Karmarkar, V. K. Agrawal, Relationships and relative correlation
potential of the Wiener, Szeged and PI indices, Nat. Acad. Sci. Lett. 23 (2000) 165–170.
[14] M. H. Khalifeh, H. Youseﬁ-Azari, A. R. Ashraﬁ, S. G. Wagner, Some new results on
distance-based graph invariants, European J. Combin. 30 (2009) 1149–1163.
[15] M. H. Khalifeh, H. Youseﬁ-Azari, A. R. Ashraﬁ, Vertex and Edge PI Indices of Cartesian
Product Graphs, Discrete Appl. Math. 156 (2008) 1780–1789.
[16] M. H. Khalifeh, H. Youseﬁ-Azari, A. R. Ashraﬁ, A matrix method for computing Szeged
and vertex PI indices of join and composition of graphs, Linear Algebra Appl. 429 (2008)
2702–2709.
[17] S. Klavˇzar, A. Rajapake, I. Gutman, The Szeged and the Wiener index of graphs, Appl.
Math. Lett. 9 (1996) 45–49.
[18] K. Kutnar, A. Malniˇc, D. Maruˇsiˇc, ˇS. Miklaviˇc, Distance-balanced graphs: Symmetry
conditions, Discrete Math. 306 (2006) 1881–1894.
[19] W. Luo, B. Zhou, On ordinary and reverse Wiener indices of non-caterpillars, Math.
Comput. Model. 50 (2009) 188–193.
[20] B. McKay, Nauty, http://cs.anu.edu.au/∼bdm/nauty/
[21] M. Mogharrab, H. R. Maimani, A. R. Ashraﬁ, A note on the vertex PI index of graphs,
J. Adv. Math. Studies 2 (2009) 53–56.
[22] M. J. Nadjaﬁ-Arani, G. H. Fath-Tabar, A. R. Ashraﬁ, Extremal graphs with respect to
the vertex PI index, Appl. Math. Lett. 22 (2009) 1838–1840.
[23] G. P´olya, G. Szeg¨o, Problems and Theorems in Analysis I: Series, Integral Calculus,
Theory of Functions, New York, Springer-Verlag, 1998.
[24] D. H. Rouvray, The rich legacy of half a century of the Wiener index, in: D. H. Rouvray
and R. B. King (Editors), Topology in Chemistry-Discrete Mathematics of Molecules,
Horwood, Chichester (2002) 16–37.
[25] R. Todeschini, V. Consonni, Handbook of Molecular Descriptors, Wiley – VCH, Wein-
heim, 2000.
10

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.11565v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1909.11565v1_Curvatures__graph_products_and_Ricci_flatness

> Source: 1909.11565v1_Curvatures__graph_products_and_Ricci_flatness.pdf

> Pages: 35

---


## Page 1


CURVATURES, GRAPH PRODUCTS AND RICCI
FLATNESS
DAVID CUSHING, SUPANAT KAMTUE, RIIKKA KANGASLAMPI,
SHIPING LIU, AND NORBERT PEYERIMHOFF
Abstract. In this paper, we compare Ollivier Ricci curvature and
Bakry-´Emery curvature notions on combinatorial graphs and dis-
cuss connections to various types of Ricci ﬂatness. We show that
non-negativity of Ollivier Ricci curvature implies non-negativity of
Bakry-´Emery curvature under triangle-freeness and an additional
in-degree condition. We also provide examples that both condi-
tions of this result are necessary. We investigate relations to graph
products and show that Ricci ﬂatness is preserved under all natural
products. While non-negativity of both curvatures are preserved
under Cartesian products, we show that in the case of strong prod-
ucts, non-negativity of Ollivier Ricci curvature is only preserved
for horizontal and vertical edges. We also prove that all distance-
regular graphs of girth 4 attain their maximal possible curvature
values.
1. Introduction
1.1. Motivation of the paper. Curvature is a fundamental notion in
the setting of smooth Riemannian manifolds. There is no unique choice
of an analogue of curvature in the setting of combinatorial graphs. Two
possibilities are Ollivier Ricci curvature and Bakry-´Emery curvature
which are both motivated by speciﬁc curvature properties of Riemann-
ian manifolds. Ollivier Ricci curvature, introduced in [16], is based
on the observation that, in the case of positive/negative Ricci cur-
vature, average distances between corresponding point in two nearby
small balls in Riemannian manifolds are smaller/larger than the dis-
tance between their centres. This fact is reinterpreted using the theory
of Optimal Transportation of probability measures representing these
balls. Bakry-´Emery curvature, introduced in [1], is based on the so-
called curvature-dimension inequality which reads for n-dimensional
Riemannian manifolds (M, g) as follows:
(1)
1
2∆∥gradf∥2(x) ≥⟨∇f(x), ∇∆f(x)⟩+ 1
n(∆f(x))2 + Ric(∇f, ∇f)(x)
for all f ∈C∞(M) and x ∈M. Here, Ric(v, w) for tangent vectors v, w
at x stands for the Ricci curvature of the manifold. This formula is a
Date: September 26, 2019.
1
arXiv:1909.11565v1  [math.CO]  25 Sep 2019


## Page 2


2
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
straightforward implication of Bochner’s identity, a fundamental fact
in Riemannian Geometry with many important consequences. Both
curvature notions have been further discussed in the setting of graphs
in several literatures (see, e.g., [14] for Ollivier Ricci curvature and
[11, 15, 18] for Bakry-´Emery curvature). For the precise deﬁnitions of
both notions in this paper, we refer to Section 2.
While there are many special cases in which these two discrete cur-
vature notions are related, it is a challenging problem to develop a
satisfactory general understanding of the agreements and diﬀerences of
these two curvature notions.
One special family of graphs which have both non-negative Ollivier
Ricci curvature and non-negative Bakry-´Emery curvature was intro-
duced by F.R.K. Chung and S.-T. Yau [6], namely Ricci ﬂat graphs.
The notion of Ricci ﬂatness was motivated by the structure of the d-
dimensional grid Zd (with vanishing Ollivier Ricci and Bakry-´Emery
curvature) and the class of Ricci ﬂat graphs contains all abelian Cayley
graphs as a subset.
The motivation of this paper is to investigate various relations be-
tween these two curvature notions and the property of Ricci ﬂatness
with special focus on triangle-free graphs.
We also present explicit
examples of graphs related to our results. The curvatures of these ex-
amples were calculated numerically via the interactive web-application
at
https://www.mas.ncl.ac.uk/graph-curvature/
For more details about this very useful tool we refer the readers to [8].
1.2. Statement of results. Let G = (V, E) be a regular graph. Ol-
livier Ricci curvature κp(x, y) is deﬁned on edges {x, y} ∈E and there
is an idleness parameter p ∈[0, 1] involved. Lin, Lu, and Yau intro-
duced in [14] a modiﬁed notion of Ollivier Ricci curvature, denoted by
κLLY (x, y). Both notions are introduced in Deﬁnition 2.3. While it is
known that κ0 ≤κLLY , our ﬁrst result shows in Subsection 2.1 that
positive κLLY -curvature implies non-negativity of κ0-curvature:
Theorem 1.1. Let G = (V, E) be a regular graph. Then we have the
following implication for all edges {x, y} ∈E:
κLLY (x, y) > 0
=⇒
κ0(x, y) ≥0.
The Bakry-´Emery curvature is deﬁned on vertices and the above
inequality (1) involves a dimension parameter n. Since graphs do not
have a well-deﬁned dimension, a natural choice simplifying this inequal-
ity is n = ∞. The induced Bakry-´Emery curvature value at a vertex x
is then denoted by K∞(x) (see Deﬁnition 2.8).
Let us now turn to the above mentioned notion of Ricci ﬂatness.
Ricci ﬂatness is deﬁned locally for individual vertices. In this paper


## Page 3


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
3
we also introduce stronger types of Ricci ﬂatness, namely (R)-, (S)-
and (RS)-Ricci ﬂatness (see Deﬁnition 3.1 below).
A fundamental
consequence of Ricci ﬂatness is that it implies both non-negativity of
Ollivier Ricci and Bakry-´Emery curvatures; the stronger property of
(R)-Ricci ﬂatness implies even strict positivity of these two curvatures
(see Theorems 3.4 and 3.5).
Another basic property of Ricci ﬂatness is that it is preserved under
natural graph products (see Theorem 5.2). The graph products under
consideration namely, Cartesian product (involving horizontal and ver-
tical edges), tensorial product (involving only diagonal edges), and the
strong product (involving all three types of edges), are introduced in
Deﬁnition 5.1 below. While Cartesian products preserve non-negativity
of both Ollivier Ricci curvature and Bakry-´Emery curvature, in the
case of strong products, non-negative Ollivier Ricci curvature is only
preserved for horizontal and vertical edges (see Corollary 5.4).
We also consider the case of graphs which contain no triangles. In
Section 4, we present our main result of this paper relating the two
curvature notions. P. Ralli [17] gave an interesting criterion for curva-
ture sign agreement of both curvature notions for triangle-free graphs
which do not contain the complete bipartite graph K2,3 as a subgraph.
He mentions that the situation is much more unclear if one restricts to
general triangle-free graphs. Our result requires triangle-freeness at a
vertex x and the additional assumption that the in-degrees of vertices
in the 2-sphere S2(x) are smaller or equal to 2. This assumption is
weaker than non-existence of K2,3 as a subgraph.
Theorem 1.2. Given a regular graph G = (V, E), let x ∈V be a vertex
not contained in a triangle and satisfying d−
x (z) ≤2 for all z ∈S2(x).
Then we have the following:
(a) κ0(x, y) = 0 for all y ∈S1(x) implies K∞(x) ≥0.
(b) κLLY (x, y) = 2
d for all y ∈S1(x) implies K∞(x) = 2.
It is an important remark here that κ0(x, y) = 0, κLLY (x, y) = 2
d,
and K∞(x) = 2 are the maximum possible values of curvature for a
vertex x not contained in a triangle. This curvature comparison result
is proved by employing Ricci ﬂatness, see Section 4. At the end of the
section, we provide also examples to show that all conditions of the
theorem are necessary.
In the ﬁnal Section 6, we show that the curvatures of all distance-
regular graphs of girth 4 and vertex degree d satisfy κ0 = 0, κLLY = 2
d
and K∞= 2 (see Theorem 6.2). In other words, all curvatures attain
their maximal possible values for this interesting family of triangle-free
graphs.


## Page 4


4
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
2. Curvature notions
All graphs G = (V, E) with vertex set V and edge set E in this paper
are simple (that is, without loops and multiple edges), undirected and
connected, and we assume that the vertex degrees dx of all vertices
x ∈V are ﬁnite. Moreover, all our graphs are regular (that is dx = d
for all x ∈V ) unless stated otherwise. Balls and spheres are denoted
by
Bk(x)
:=
{z ∈V : d(x, z) ≤k},
Sk(x)
:=
{z ∈V : d(x, z) = k},
where d : V × V →N ∪{0} is the combinatorial distance function.
2.1. Ollivier Ricci curvature. We deﬁne the following probability
distributions µp
x for any x ∈V, p ∈[0, 1]:
µp
x(z) =





p,
if z = x,
1−p
dx ,
if z ∼x,
0,
otherwise.
Deﬁnition 2.1 (Transport plan and Wasserstein distance). Given G =
(V, E), let µ1, µ2 be two probability measures on V . A transport plan
π transporting µ1 to µ2 is a function π : V × V →[0, ∞) satisfying the
following marginal constraints
(2)
µ1(x) =
X
y∈V
π(x, y),
µ2(y) =
X
x∈V
π(x, y).
The cost of a transport plan π is given by
cost(π) =
X
y∈V
X
x∈V
d(x, y)π(x, y).
The set of all transport plans satisfying (2) is denoted by Π(µ1, µ2).
The Wasserstein distance W1(µ1, µ2) between µ1 and µ2 is then de-
ﬁned as
(3)
W1(µ1, µ2) := inf
π cost(π) = inf
π
X
y∈V
X
x∈V
d(x, y)π(x, y),
where the inﬁmum runs over all transport plans π ∈Π(µ1, µ2).
Remark 2.2. Note that every π ∈Π(µ1, µ2) satisﬁes π(x, y) = 0 if
x ̸∈supp(µ1) or y ̸∈supp(µ2). Therefore (3) can be rewritten as
W1(µ1, µ2) = inf
π
X
y∈supp(µ2)
X
x∈supp(µ1)
d(x, y)π(x, y).
In other words, a transport plan π moves a mass distribution given
by µ1 into a mass distribution given by µ2, and W1(µ1, µ2) is a measure
for the minimal eﬀort which is required for such a transition.


## Page 5


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
5
If µ1 and µ2 have ﬁnite supports, then there exists π which attains the
inﬁmum in (3). We call such π an optimal transport plan transporting
µ1 to µ2.
Deﬁnition 2.3 (Ollivier Ricci curvature). The p-Ollivier Ricci curva-
ture [16] on an edge {x, y} ∈E is
κp(x, y) = 1 −W1(µp
x, µp
y),
where p ∈[0, 1] is called the idleness parameter.
The Ollivier Ricci curvature introduced by Lin, Lu, and Yau [14], is
deﬁned as
κLLY (x, y) = lim
p→1
κp(x, y)
1 −p .
It was shown in [14, Lemma 2.1] that the function p 7→κp(x, y) is
concave, which implies
(4)
κp(x, y) ≤κLLY (x, y)
for all p ∈[0, 1].
Moreover, we have the following relation for edges {x, y} with dx =
dy = d (see [3]):
(5)
κLLY (x, y) = d + 1
d
κ
1
d+1(x, y).
From the deﬁnition of the Wasserstein metric we can get an upper
bound for W1 by choosing a suitable transport plan. Using Kantorovich
duality (see e.g. [20, Ch. 5]), a fundamental concept in the optimal
transport theory, we can approximate the opposite direction:
Theorem 2.4 (Kantorovich duality). Given G = (V, E), let µ1, µ2 be
two probability measures on V . Then
W1(µ1, µ2) = sup
φ:V →R
φ∈1-Lip
X
x∈V
φ(x)(µ1(x) −µ2(x)),
where 1-Lip denotes the set of all 1-Lipschitz functions.
If φ ∈1-
Lip attains the supremum we call it an optimal Kantorovich potential
transporting µ1 to µ2.
Note that both curvatures κ0(x, y) and κLLY (x, y) of an edge {x, y}
are already determined by the combinatorial structure of the induced
subgraph B2(x).
(In fact, by symmetry reasons, the combinatorial
structure of the induced subgraph B2(x) ∩B2(y) is suﬃcient.)
As the relation κ0 ≤κLLY is known from (4), now we will prove the
surprising fact that strict positivity of κLLY implies non-negativity of
κ0 (as stated in Theorem 1.1 from the Introduction).
Proof of Theorem 1.1. Let G = (V, E) be d-regular. Using the relation
(5), it suﬃces to prove
κ
1
d+1(x, y) > 0
=⇒
κ0(x, y) ≥0.


## Page 6


6
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
Let {x, y} ∈E be an edge with κ
1
d+1(x, y) > 0. We deﬁne the following
sets:
Txy
:=
S1(x) ∩S1(y),
Vx
:=
S1(x)\B1(y),
Vy
:=
S1(y)\B1(x).
In other words, Txy is the set of common neighbours of x and y, Vx is
the set of neighbours of x which have distance 2 to y and, similarly, Vy
is the set of neighbours of y which have distance 2 to x.
We can choose an optimal transport plan πopt ∈Π(µ
1
d+1
x
, µ
1
d+1
y
) with
i) if u ∈Txy ∪{x} ∪{y}, then πopt(u, u) =
1
d+1,
ii) if u ∈Vx, then πopt(u, v) =
1
d+1 for exactly one v ∈Vy and 0 for
others,
iii) if u /∈B1(x), then πopt(u, v) = 0 for v ∈V .
The existence of an optimal transport plan satisfying (ii) (that is, with-
out splitting mass), follows from [4, Theorem 1.1] (see also [19, p. 5]).
Moreover, this transport plan can be chosen to satisfy (i) by [3, Lemma
4.1]. Note that (iii) holds for any transport plan in Π(µ
1
d+1
x
, µ
1
d+1
y
).
In other words, the optimal transport plan does not move the mass
distributions at x, y or Txy, and for the vertices in Vx it moves the mass
distribution from one vertex completely to one vertex in Vy. Thus the
optimal transport plan pairs the vertices at Vx and Vy. Let u ∈Vx and
denote by ˜u the unique vertex in Vy for which πopt(u, ˜u) =
1
d+1.
Let us then consider the Wasserstein distance. Using the optimal
transport plan we can write
(6)
1 > 1 −κ
1
d+1(x, y) = W1(µ
1
d+1
x
, µ
1
d+1
y
) =
1
d + 1
X
u∈Vx
d(u, ˜u).
Note that 1 ≤d(uj, ˜uj) ≤3 for all uj ∈Vx. Let
Ni := |{u ∈Vx : d(u, ˜u) = i}|
for i ∈{1, 2, 3}.
It follows from (6) that d+1 > P
u∈Vx d(u, ˜u) = N1 +2N2 +3N3, which
implies
(7)
d ≥N1 + 2N2 + 3N3.
Now we distinguish three cases.
Assume that N3 > 0. Then there exists at least one vertex w ∈Vx
satisfying d(w, ˜w) = 3. Let π be a transport plan from µ0
x to µ0
y such
that π(w, x) = 1
d, π(y, ˜w) = 1
d and π(u, ˜u) = 1
d for all other pairs (u, ˜u)
on the support of πopt except (w, ˜w). Using this transport plan and


## Page 7


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
7
(7), we have
W1(µ0
x, µ0
y)
≤
1
d (2 + N1 + 2N2 + 3(N3 −1))
≤
d −1
d
< 1.
Thus κ0(x, y) > 0.
Next, we assume N3 = 0 and N2 > 0. Then there exists at least
one vertex w ∈Vx satisfying d(w, ˜w) = 2, and we obtain, similarly as
above,
W1(µ0
x, µ0
y)
≤
1
d(2 + N1 + 2(N2 −1))
≤
1
d(N1 + 2N2 + 3N3) ≤1,
and therefore κ0(x, y) ≥0.
Finally, if N2 = N3 = 0, the optimal transport plan πopt deﬁnes a
perfect matching between the sets Vx and Vy, and therefore
W1(µ0
x, µ0
y) ≤2 + (N1 −1)
d
= N1 + 1
d
≤1,
since N1 = |Vx| ≤d −1, and again, κ0(x, y) ≥0, with equality if and
only if N1 = d −1, which means Txy = ∅.
□
(a) The triplex
(b) The icosidodecahedral graph
Figure 1. Examples of graphs with κLLY = 0
Remark 2.5.
(a) The proof shows that κLLY (x, y) > 0 implies κ0(x, y) > 0 in the
following cases:
(i) N3 > 0 or
(ii) N3 = N2 = 0 and {x, y} is contained in a triangle.


## Page 8


8
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
(b) The hypercubes Qd satisfy κLLY (x, y) = 2
d > 0 and κ0(x, y) = 0 for
all edges {x, y} ∈E.
(c) The triplex (see Figure 1a) satisﬁes κLLY (x, y) = 0 and κ0(x, y) =
−1
3 < 0 for all edges {x, y} ∈E.
(d) The icosidodecahedral graph (see Figure 1b) satisﬁes κLLY (x, y) = 0
and κ0(x, y) = 0 for all edges {x, y} ∈E. This implies that κp(x, y) = 0
for all p ∈[0, 1]. Graphs with this property in all edges are called bone-
idle (this notion was introduced in [3]).
The examples (b) and (c) show that the result in the theorem is sharp.
We ﬁnish this subsection with the following upper curvature bounds
for κ0 and κLLY :
Theorem 2.6 (see [13, Theorem 4] and [7, Proposition 2.7]). Let G =
(V, E) be d-regular and {x, y} ∈E. Then
κ0(x, y) ≤#∆(x, y)
d
,
and
κLLY (x, y) ≤2 + #∆(x, y)
d
,
where #∆(x, y) is the number of triangles containing {x, y}.
2.2. Bakry-´Emery curvature. This curvature notion was ﬁrst in-
troduced by Bakry and ´Emery in [1] and was applied on graphs in
[11, 15, 18]. The deﬁnition of this curvature is based on the curvature-
dimension inequality (1), which is equivalently rewritten as (8) below
with the help of the following Γ-calculus.
For any function f : V →R and any vertex x ∈V , the (non-
normalized) Laplacian ∆is deﬁned via
∆f(x) :=
X
y:y∼x
(f(y) −f(x)).
Deﬁnition 2.7 (Γ and Γ2 operators). Given G = (V, E), we deﬁne for
two functions f, g : V →R
2Γ(f, g) := ∆(fg) −f∆g −g∆f;
2Γ2(f, g) := ∆Γ(f, g) −Γ(f, ∆g) −Γ(∆f, g).
We write Γ(f) := Γ(f, f) and Γ2(f, f) := Γ2(f), for short.
Deﬁnition 2.8 (Bakry-´Emery curvature). Given G = (V, E), K ∈R
and N ∈(0, ∞]. We say that a vertex x ∈V satisﬁes the curvature-
dimension inequality CD(K, N), if for any f : V →R, we have
(8)
Γ2(f)(x) ≥1
N (∆f(x))2 + KΓ(f)(x)
for all x ∈V .
We call K a lower Ricci curvature bound of x, and N a dimension
parameter. The graph G = (V, E) satisﬁes CD(K, N) (globally), if all


## Page 9


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
9
its vertices satisfy CD(K, N). At a vertex x ∈V , let K(x, N) be the
largest K such that (8) holds for all functions f at x for a given N. We
call K(x, ·) the Bakry-´Emery curvature function of x and we deﬁne
K∞(x) := lim
N→∞K(x, N).
In this paper, we will restrict our considerations to the curvature at
∞-dimension K∞: V →R. Note that for the deﬁnition of K∞(x), the
formula (8) simpliﬁes to
Γ2(f)(x) ≥KΓ(f)(x)
for all x ∈V .
The quadratic forms Γ(·, ·)(x) and Γ2(·, ·)(x) can be represented by
matrices Γ(x) and Γ2(x) as follows
Γ(f, g)(x)
=
fΓ(x)g⊤,
Γ2(f, g)(x)
=
fΓ2(x)g⊤,
where f, g are the vector representations of f and g. The matrices
Γ(x), Γ2(x) are symmetric with non-zero entries only in B1(x) and
B2(x), respectively.
So we can view them as local matrices by dis-
regarding the vertices outside B2(x). For the explicit matrix entries of
Γ(x) and Γ2(x) see [9, Subsections 2.2 and 2.3]. Note that these en-
tries are already fully determined by the combinatorial structure of the
incomplete 2-ball around x, denoted by Binc
2 (x), which is the induced
subgraph of B2(x) with all edges within S2(x) removed.
We have the following general upper curvature bound similar to The-
orem 2.6:
Theorem 2.9 (see [9, Corollary 3.3]). Let G = (V, E) be d-regular and
x ∈V . Then
K∞(x) ≤2 + #∆(x)
d
,
where #∆(x) is the number of triangles containing x.
Let us ﬁnally return to the examples from the previous subsection.
Remark 2.10. The examples in Remark 2.5 have the following Bakry-
´Emery and Ollivier Ricci curvatures:
κ0(x, y)
κLLY (x, y)
K∞(x)
Hypercube Qd
0
2
d
2
Triplex
−1
3
0
−1
Icosidodecahedral graph
0
0
−3
2
None of the regular graphs in the above table have curvature with
opposite signs. We are not aware of any such examples and it would
be interesting to ﬁnd such graphs.


## Page 10


10
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
3. Ricci flat graphs
The notion of Ricci ﬂat graphs was introduced in 1996 by Chung
and Yau [6] in connection to a logarithmic Harnack inequality and
is motivated by the structure of the d-dimensional grid Zd. Abelian
Cayley graphs are prominent examples of Ricci ﬂat graphs.
Deﬁnition 3.1. Let G = (V, E) be a d-regular graph. We say that
x ∈V is Ricci ﬂat if there exist maps ηi : B1(x) →V for 1 ≤i ≤d
with the following properties:
(i) ηi(u) ∼u for all u ∈B1(x),
(ii) ηi(u) ̸= ηj(u) if i ̸= j,
(iii) S
j ηj(ηix)) = S
j ηi(ηjx) for all i.
We also consider the following additional properties of the maps ηi:
(R) Reﬂexivity: η2
i (x) = x for all i,
(S) Symmetry: ηj(ηix) = ηi(ηjx) for all i, j.
If there exists a family of maps ηi for a given vertex x ∈V satisfying
property (R) or property (S) in addition to (i)-(iii), we say that x is
(R)-Ricci ﬂat or (S)-Ricci ﬂat, respectively. If there exists a family of
maps ηi satisfying (i)-(iii) and (R) and (S) simultaneously, we say that
x is (RS)-Ricci ﬂat.
The d-dimensional grid Zd is Ricci ﬂat with the choices ηi(x) = x+ei.
The following lemma is a useful observation for the study of Ricci
ﬂatness of concrete examples.
Lemma 3.2. Assume a family of maps ηi : B1(x) →V satisﬁes (i)-
(iii) of the above deﬁnition. Then each of these maps ηi is a bijective
map between B1(x) and B1(ηix).
Proof. Assume that the family ηi satisﬁes (i)-(iii). It follows immedi-
ately from (i) and (ii) and regularity that
[
j
ηj(u) = S1(u)
for all u ∈B1(x).
This implies that (iii) is equivalent to
S1(ηix) = ηi(S1(x))
for all i,
which, in turn, implies
(9)
B1(ηix) = S1(ηix) ∪{ηix} = ηi(S1(x)) ∪ηi({x}) = ηi(B1(x)).
Therefore, each map ηi must be injective, since
|ηi(B1(x))| = |B1(ηix)| = |B1(x)|.
Bijectivity from B1(x) to B1(ηx) follows immediately from (9).
□
Note that all Ricci ﬂatness properties at a vertex x can be deter-
mined from the combinatorial structure of the incomplete 2-ball Binc
2 (x)
around x, which was introduced in Subsection 2.2.


## Page 11


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
11
Example 3.3. To help readers familiarize with the notion of Ricci
ﬂatness, we provide three examples of graphs and check whether each
of them is Ricci ﬂat.
(a) The incomplete 2-ball in Figure 2 with S1(x) = {v1, v2, v3}, v1 ∼
v2 and S2(x) = {v4, v5, v6}, v4 ∼v1, v5 ∼v2, v3 and v6 ∼v3 is
not Ricci ﬂat:
x
v1
v2
v3
v4
v5
v6
Figure 2. Graph that is not Ricci ﬂat
We show this by contradiction.
Assume ηi : B1(x) →V
with properties (i)-(iii) exist. Without loss of generality, we can
assume ηi(x) = vi. Note that we must have ηi(vj) ∈S1(vi) ∩
S1(vj) for 1 ≤i, j ≤d. This implies that we have the following
choices for our maps ηj:
x
v1
v2
v3
η1
v1
x, v2, v4
x
x
η2
v2
x
x, v1, v5
x, v5
η3
v3
x
x, v5
x, v5, v6
Such a table can be presented concisely with the help of a d × d
matrix A, namely, A = (Aij) deﬁned as follows: Let S1(x) =
{v1, . . . , vd} where vj := ηj(x), and S2(x) =: {vd+1, . . . , vt} and,
furthermore, v0 := x. Then the entries Aij ∈{0, 1, . . . , t} of A
are given via the relation
vAij = ηi(vj).
Then the table translates into the following possibilities for the
entries of A:


0, 2, 4
0
0
0
0, 1, 5
0, 5
0
0, 5
0, 5, 6

.
The conditions (i)-(iii) require that all columns and rows of A
have non repeating entries. Obviously, this is not possible in this
case. Henceforth, we will use this matrix notation to simplify
matters.


## Page 12


12
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
(b) The graph K3,3: Let S1(x) = {v1, v2, v3} and S2(x) = {v4, v5}
with v4, v5 ∼v1, v2, v3. We have the following possibilities for
the entries of the associated matrix A:


0, 4, 5
0, 4, 5
0, 4, 5
0, 4, 5
0, 4, 5
0, 4, 5
0, 4, 5
0, 4, 5
0, 4, 5

.
Note that (R)-Ricci ﬂatness requires existence of an associated
matrix A with vanishing diagonal and (S)-Ricci ﬂatness requires
existence of a symmetric matrix A. Therefore, x is (R)- and
(S)-Ricci ﬂat by the following matrix choices:
AR =


0
4
5
5
0
4
4
5
0

,
AS =


0
4
5
4
5
0
5
0
4

.
Note that x is not (RS)-Ricci ﬂat since both properties (van-
ishing diagonal and symmetry) cannot be satisﬁed at the same
time. In fact, the complete bipartite graphs Kd,d are both (R)-
and (S)-Ricci ﬂat for all d, and (RS)-Ricci ﬂat if and only if d
is even (see the Appendix).
(c) Shrikhande graph: Cayley graph Z4 × Z4 with the generator set
{±(0, 1), ±(1, 0), ±(1, 1)}.
It is a strongly regular graph (see
[5, pp. 125]). The structure of the incomplete 2-ball Binc
2 (x)
around any vertex x is given in Figure 3. We have the following
possibilities for the entries of the associated matrix A:





0, 2, 6, 7, 12, 15
0, 7
0, 2
0, 12
0, 6
0, 15
0, 7
0, 1, 3, 7, 8, 13
0, 8
0, 3
0, 13
0, 1
0, 2
0, 8
0, 2, 4, 8, 9, 14
0, 9
0, 4
0, 14
0, 12
0, 3
0, 9
0, 3, 5, 9, 10, 12
0, 10
0, 5
0, 6
0, 13
0, 4
0, 10
0, 4, 6, 10, 11, 13
0, 11
0, 15
0, 1
0, 14
0, 5
0, 11
0, 1, 5, 11, 14, 15




.
Choosing 0 for diagonal entries ﬁxes all other entries of the ma-
trix. Moreover, this choice leads to a symmetric matrix, which
shows that x is (RS)-Ricci ﬂat.
3.1. Ricci ﬂatness and Ollivier Ricci curvature. With regards to
Ollivier Ricci curvature we have the following general implications:
Theorem 3.4. Let G = (V, E) be d-regular.
(a) If x ∈V is Ricci ﬂat then κ0(x, y) ≥0 for all edges {x, y} ∈E.
(b) If x ∈V is (R)-Ricci ﬂat then κLLY (x, y) ≥
2
d for all edges
{x, y} ∈E.
Proof. For the proof of (a) we assume Ricci ﬂatness at x with corre-
sponding maps ηi : B1(x) →V . Let y ∈S1(x). Recall that
S1(x) = {η1(x), . . . , ηd(x)}.


## Page 13


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
13
x
v1
v2
v3
v4
v5
v6
v7
v8
v9
v10
v11
v12
v13
v14
v15
Figure
3. The
incomplete
2-ball
Binc
2 (x)
of
the
Shrikhande graph
Therefore, we have y = ηi(x) for some i ∈{1, . . . , d}. We choose the
following transport plan:
π(u, ηi(u)) = 1
d
for all u ∈S1(x),
and π(u, v) = 0 for all other combinations. This implies
X
v∈V
π(u, v) = π(u, ηi(u)) = 1
d = µ0
x(u)
for all u ∈S1(x),
and (using Lemma 3.2)
X
u∈V
π(u, v) = π(η−1
i (v), v) = 1
d = µ0
y(v)
for all v ∈S1(y),
which shows that π ∈Π(µ0
x, µ0
y). This leads to
W1(µ0
x, µ0
y) ≤cost(π) =
X
u∈S1(x)
π(u, ηi(u)) = 1,
which implies κ0(x, y) ≥0.
We prove (b) similarly. Assume x is (R)-Ricci ﬂat with correspond-
ing maps ηi and y = ηi(x).
Note that we have ηi(y) = x from
reﬂexivity.
This time, we choose the following transport plan π ∈
Π(µ1/(d+1)
x
, µ1/(d+1)
y
):
π(u, ηi(u)) =
1
d + 1
for all u ∈S1(x)\{y},
π(x, x) = π(y, y) =
1
d+1, and π(u, v) = 0 for all other combinations.
This leads to
W1(µ1/(d+1)
x
, µ1/(d+1)
y
) ≤cost(π) =
X
u∈S1(x)\{y}
π(u, ηi(u)) = d −1
d + 1,


## Page 14


14
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
which implies κ1/(d+1)(x, y) ≥
2
d+1 and
κLLY (x, y) = d + 1
d
κ1/(d+1)(x, y) ≥2
d.
□
3.2. Ricci ﬂatness and Bakry-´Emery curvature. With regards to
Bakry-´Emery curvature we have the following general implications:
Theorem 3.5. Let G = (V, E) be d-regular.
(a) If x ∈V is Ricci ﬂat then K∞(x) ≥0.
(b) If x ∈V is (R)-Ricci ﬂat then K∞(x) ≥2.
Proof. The proof of statement (a) was already explained in [6] and
[15]. This proof stategy can also be applied to prove statement (b).
We present these proofs for the reader’s convenience.
Recall from the deﬁnition that
(10)
2Γ2(f, f)(x) = ∆Γ(f, f)(x) −2Γ(f, ∆f)(x).
and
2Γ(f, g)(x) = ∆(fg)(x) −f(x)∆g(x) −g(x)∆f(x).
A useful identity to compute Γ(f, g) is
2Γ(f, g)(x) =
X
y:y∼x
(f(y) −f(x))(g(y) −g(x)).
Let us now consider the ﬁrst term on the RHS in (10) and use the
identity A2 −B2 = (A −B)2 + 2B(A −B):
∆Γ(f, f)(x)
=
d
X
i=1
(Γ(f, f)(ηix) −Γ(f, f)(x))
=
1
2
d
X
i=1
"
d
X
j=1
(f(ηjηix) −f(ηix))2 −
d
X
j=1
(f(ηjx) −f(x))2
#
=
d
X
i=1
d
X
j=1
(f(ηjηix) −f(ηix) −f(ηjx) + f(x))2
+
d
X
i=1
d
X
j=1
(f(ηjx) −f(x)) (f(ηjηix) −f(ηix) −f(ηjx) + f(x)) .


## Page 15


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
15
On the other hand, we have for the second term on the RHS of (10),
using Ricci ﬂatness,
−2Γ(f, ∆f)(x)
=
−
d
X
j=1
(f(ηjx) −f(x)) (∆f(ηjx) −∆f(x))
=
−
d
X
j=1
d
X
i=1
(f(ηjx) −f(x)) (f(ηiηjx) −f(ηjx) −f(ηix) + f(x))
=
−
d
X
j=1
d
X
i=1
(f(ηjx) −f(x)) (f(ηjηix) −f(ηix) −f(ηjx) + f(x)) .
Adding both terms, we end up with
2Γ2(f, f)(x) =
d
X
i=1
d
X
j=1
(f(ηjηix) −f(ηix) −f(ηjx) + f(x))2 ≥0,
showing K∞(x) ≥0. Under the stronger condition of (R)-Ricci ﬂatness,
we can estimate 2Γ2(f, f)(x) from below as follows:
2Γ2(f, f)(x)
=
d
X
i=1
d
X
j=1
(f(ηjηix) −f(ηix) −f(ηjx) + f(x))2
≥
d
X
i=1
(f(ηiηix) −f(ηix) −f(ηix) + f(x))2
=
d
X
i=1
(2f(x) −2f(ηix))2 = 4Γ(f, f)(x).
This shows that Γ2(f, f)(x) ≥2Γ(f, f)(x), which means that we have
K∞(x) ≥2.
□
4. Triangle-free graphs
In this section we focus on curvature comparison results for graphs
without triangles. Our main result states that non-negativity of Ollivier
Ricci curvature implies non-negativity of Bakry-´Emery curvature under
a certain in-degree condition (see Corollary 1.2). This result is derived
via Ricci ﬂatness properties.
We start with particular upper curvature bounds in case of triangle-
freeness:
Proposition 4.1. Let G = (V, E) be d-regular.
Then we have the
following upper curvature bounds:
(i) κ0(x, y) ≤0 for all edges {x, y} ∈E not contained in a triangle,
(ii) κLLY (x, y) ≤
2
d for all edges {x, y} ∈E not contained in a
triangle,
(iii) K∞(x) ≤2 for all x ∈V not contained in a triangle.


## Page 16


16
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
Remark 4.2. Combining the proposition with the lower curvature bounds
for Ricci ﬂatness (Theorems 3.4 and 3.5), we obtain the following cur-
vature equalities:
• If x is Ricci ﬂat and the egde {x, y} ∈E is not contained in
any triangle then κ0(x, y) = 0.
• If x is (R)-Ricci ﬂat and the egde {x, y} ∈E is not contained
in any triangle then κLLY (x, y) = 2
d.
• If x is (R)-Ricci ﬂat and not contained in any triangle then
K∞(x) = 2.
Proof of Proposition 4.1. Although Statements (i) and (ii) are an im-
plication from Theorem 2.6, we provide their proof here which presents
a useful idea for the following remark.
Statement (i) follows from
W1(µ0
x, µ0
y)
=
X
u∈S1(x)
X
v∈S1(y)
d(u, v)πopt(u, v)
≥
X
u∈S1(x)
X
v∈S1(y)
πopt(u, v) = 1,
(11)
since S1(x) ∩S1(y) = ∅.
Here πopt is an optimal transport plan in
Π(µ0
x, µ0
y).
For the proof of (ii), we only need to show
κ
1
d+1(x, y) ≤
2
d + 1,
by (5). This follows from
W1(µ1/(d+1)
x
, µ1/(d+1)
y
)
=
X
u∈B1(x)
X
v∈B1(y)
d(u, v)πopt(u, v)
≥

X
u∈B1(x)
X
v∈B1(y)
πopt(u, v)

−πopt(x, x) −πopt(y, y)
≥
1 −
2
d + 1,
(12)
since B1(x) ∩B1(y) = {x, y} and πopt(u, u) ≤µ1/(d+1)
x
(u) ≤
1
d+1. Here
πopt is an optimal transport plan in Π(µ1/(d+1)
x
, µ1/(d+1)
y
).
Statement (iii) is an implication from Theorem 2.9.
□
Remark 4.3. Note that in Proposition 4.1, (ii) implies (i) by Theorem
1.1. Moreover, it follows from the above proof that sharpness of the
bounds in (i) and (ii) has the following combinatorial interpretation in
the triangle-free case:
(a) κ0(x, y) = 0 is equivalent that there is a perfect matching be-
tween S1(x) and S1(y).


## Page 17


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
17
(b) κLLY (x, y) =
2
d is equivalent that there is a perfect matching
between S1(x)\{y} and S1(y)\{x}.
A natural class of examples where all three upper bounds of Proposi-
tion 4.1 are attained are distance-regular graphs of girth 4 (see Section
6 below). To motivate our next result, let us focus on one particular
example:
Example 4.4. Let S1(x) = {v1, . . . , vd} and S2(x) = {vij | 1 ≤i <
j ≤d} with vi, vj ∼vij. In fact this is the 2-ball of the d-dimensional
hypercube Qd and we have the following curvatures (see Remark 2.10):
κ0(x, vi) = 0,
κLLY (x, vi) = 2
d,
K∞(x) = 2.
We also like to mention that the vertex x in this example is (RS)-Ricci
ﬂat and that we have d−
x (z) = 2 for all z ∈S2(x).
Theorem 4.5. Given a regular graph G = (V, E), let x ∈V be a vertex
not contained in a triangle and satisfying d−
x (z) ≤2 for all z ∈S2(x).
Then we have the following:
(a) κ0(x, y) = 0 for all y ∈S1(x) is equivalent to x being (S)-Ricci
ﬂat.
(b) κLLY (x, y) = 2
d for all y ∈S1(x) is equivalent to x being (RS)-
Ricci ﬂat.
This result, together with Theorem 3.5, implies our main curvature
comparison result in Theorem 1.2 from the Introduction:
Proof of Theorem 1.2. Under the assumptions of Theorem 4.5, we ﬁrst
assume that κ0(x, y) = 0 for all y ∈S1(x). This implies that x is Ricci
ﬂat and, by Theorem 3.5(a), that K∞(x) ≥0.
Similarly, assuming κLLY (x, y) = 2
d for all y ∈S1(x), we know that x
is (R)-Ricci ﬂat, and Theorem 3.5(b) implies that K∞(x) ≥2. Since x
is not contained in a triangle, this leads to K∞(x) = 2 by Proposition
4.1(iii).
□
Before we start with the proof of Theorem 4.5, let us introduce the
following notion and discuss relations to existing results.
Deﬁnition 4.6. Let G = (V, E) be a regular triangle-free graph and
x ∈V . We say that y1, y2 ∈S1(x) are linked by z ∈S2(x) if we have
y1 ∼z ∼y2. We refer to z as a link of y1 and y2.
P. Ralli [17] investigated curvature implications for regular graphs
without K3 and K3,2 as subgraphs. It is easy to check that this condi-
tion is equivalent to the following properties at all vertices x:
(i) x is not contained in a triangle,
(ii) d−
x (z) ≤2 for all z ∈S2(x),
(iii) Any pair y1, y2 ∈S1(x) has at most one link.


## Page 18


18
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
A consequence of his results is that conditions (i),(ii),(iii) imply K∞(x) ≤
0 or K∞(x) = 2. Under these conditions, Ralli has the following equiv-
alence:
κ0(x, y) = 0 for all y ∈S1(x) ⇐⇒K∞(x) ≥0.
Our theorem implies that the implication ”=⇒” holds already under
conditions (i) and (ii) and we have an example that the implication
”⇐=” is no longer true if one drops condition (iii).
Proof of Theorem 4.5. The implications ⇐= in (a) and (b) follow im-
mediately from Theorem 3.4 and Proposition 4.1.
Let us now prove the forward implication in (a). Let x ∈V be given
with d = dx and S1(x) = {y1, . . . , yd}. The property κ0(x, y) = 0 for all
y ∈S1(x) implies that we have perfect matchings σi : S1(x) →S1(yi)
for all 1 ≤i ≤d. In particular, we can assume that these perfect
matchings σi satisfy the following property:
Property (P): If there exists a perfect matching between S1(x)\{yi}
and S1(yi)\{x} then σi(yi) = x.
Our goal is to show that we can modify these perfect matchings in
such a way that σi(yj) = σj(yi) for all i ̸= j. Deﬁning then ηi : B1(x) →
B1(yi) as ηi(x) = yi and ηi(y) = σi(y) for y ∈S1(x) provide (S)-Ricci
ﬂatness.
We ﬁrst prove the following crucial fact:
Fact: Let i ̸= j. We have σi(yj) = x if and only if yi and yj are not
linked.
This fact can be shown as follows: We ﬁrst prove the easier ”⇐=”
implication. Assume yi and yj are not linked. Then σi(yj) ∼yi, yj
cannot be in S2(x) and we must have therefore σi(yj) = x. For the
”=⇒” implication, we provide an indirect proof: If yi and yj were
linked by z ∈S2(x), then the σi-preimage of z ∈S1(yi) must be in
{yi, yj} but we know that σi(yj) = x. Therefore σi(yi) = yj. Deﬁning
then the map ˜σi : S1(x) →S1(yi) via
˜σi(yk) =





σi(yk)
if k ̸= i, j,
z
if k = j,
x
if k = i,
induces a perfect matching between S1(x)\{yi} and S1(yi)\{x}. This
would imply σi(yi) = x contradicting to σi(yj) = x.
Now we prove our goal.
We ﬁrst show that σi(yj) = x implies σj(yi) = x: Since σi(yj) = x,
yi and yj are not linked by our Fact which, in turn, implies σj(yi) = x
by our Fact, again.
We deal with all other pairs (i, j), i ̸= j as follows: If σi(yj) = σj(yi),
we do not change the assignments σi(yi), σi(yj), σj(yi), σj(yj). Now we


## Page 19


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
19
assume that σi(yj) =: z ̸= σj(yi) := z′. Note that z, z′ ∈S2(x) and
they both are links of yi and yj. Since z ∈S1(yj) and d−
x (z) ≤2, we
must have σ−1
j (z) ∈{yi, yj}. Since σj is injective and σj(yi) = z′, we
must have σ−1
j (z) = yj. So we must have
(13)
σj(yj) = z.
Similarly, we conclude that σi(yi) = z′. Now we modify σi as follows:
σi(yi) = z and σi(yj) = z′. This preserves property (P) of the perfect
matching σi and establishes σi(yj) = σj(yi) for this pair of indices (i, j).
Note that if (i, j) and (k, l) are two diﬀerent pairs with σi(yj) ̸= σj(yi)
and σk(yl) ̸= σl(yk) then {i, j}∩{k, l} = ∅for, otherwise, if k = i, there
is no perfect matching between S1(x) and S1(yi) since the four links
between yi, yj and yi, yl can only have three possible preimages under
σi. This guarantees that we can repeat this process for all such pairs
(i, j) simultaneously and we will end up with the required symmetric
arrangement.
Finally, it remains to prove the forward implication of (b).
The
assumption κLLY (x, y) = 2
d for all y ∈S1(x) implies κ0(x, y) = 0 by
Theorem 1.1. The existence of perfect matchings between S1(x)\{yi}
and S1(yi)\{x} for all 1 ≤i ≤d from Remark 4.3 further imply that
our chosen maps σi satisfy σi(yi) = x for all i. In this situation, we can
disregard the above possibility of z = σi(yj) ̸= σj(yi) = z′ with z, z′ ∈
S2(x), since this would imply (13), which contradicts to σj(yj) = x.
Therefore, the maps σi do not need to be modiﬁed and the induced
maps ηi : B1(x) →V satisfy both symmetry and reﬂexivity.
□
Remark 4.7.
(a) The reverse of the implication in Theorem 1.2(a) is not true since
we have a triangle-free 2-ball in Figure 4 with K∞(x) = 0, d−
x (z) = 2 for
all z ∈S2(x) and κ0(x, y) < 0 for all y ∈S1(x) as a counterexample.
Note that S1(x) = {v1, . . . , v6}.
(b) All conditions in Theorem 4.5(a) are necessary:
(i) If x is contained in a triangle, we have the icosidodecahedral
graph (see Figure 1b) as a counterexample with κ0(x, y) = 0 for
all edges {x, y} but K∞(x) < 0 for all vertices x, which means
that x cannot be Ricci ﬂat by Theorem 3.5.
(ii) If we drop d−
x (z) ≤2 for all z ∈S2(x), Figure 5 provides a
counterexample with κ0(x, y) = 0 for all y ∈S1(x) and K∞(x) <
0.
(c) All conditions in Theorem 4.5(b) are necessary. Since in the case
of triangles we have the following upper bound
κLLY (x, y) ≤2 + #∆(x, y)
d
,


## Page 20


20
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
x
v1
v6
v5
v4
v3
v2
x
v1
v6
v5
v4
v3
v2
x
v1
v6
v5
v4
v3
v2
x
v1
v6
v5
v4
v3
v2
x
v1
v6
v5
v4
v3
v2
x
v1
v6
v5
v4
v3
v2
v23
v16
v45
v14
v25
v36
v′
14
v′
25
v′
36
v12
v′
12
v56
v′
56
v34
v′
34
v23
v16
v45
v14
v25
v36
v′
14
v′
25
v′
36
v12
v′
12
v56
v′
56
v34
v′
34
v23
v16
v45
v14
v25
v36
v′
14
v′
25
v′
36
v12
v′
12
v56
v′
56
v34
v′
34
Figure 4. Example with K∞(x) = 0, d−
x (z) = 2 for all
z ∈S2(x) and κ0(x, vi) = −1
3.
x
Figure 5. Example with K∞(x) = −0.194 < 0 and
κp(x, y) = 0 ∀p ∈[0, 1], y ∼x.
a natural generalization of the equivalence in the case of triangles would
be the following statement:
κLLY (x, y) = 2 + #∆(x, y)
d
for all y ∈S1(x) is equivalent to x being (RS)-Ricci ﬂat.


## Page 21


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
21
(i) If x is contained in a triangle, we have K3 × K3 with d = 4 as
a counterexample:
κLLY (x, y) = 3
4 = 2 + #∆(x, y)
d
for all edges {x, y}, but no vertex of K3 ×K3 is (RS)-Ricci ﬂat.
(ii) If we drop d−
x (z) ≤2 for all z ∈S2(x), the 6-regular inci-
dence graph of the (11, 6, 3)-design provides a counterexample
with κLLY (x, y) = 1
3 for all y ∈S1(x), but x is not (RS)-Ricci
ﬂat (see Example 6.3).
5. Graph products
This section is concerned with three natural products of two graphs
G and H: the tensor product G⊗H, the Cartesian product G×H, and
the strong product G ⊠H. We will see that Ricci ﬂatness is preserved
under all three products. However, while Cartesian products preserve
non-negativity of both Bakry-´Emery and Ollivier Ricci curvature, we
will see that this property fails to be true in the case of strong products.
Let us start with the deﬁnitions of these graph products:
Deﬁnition 5.1. Let G = (VG, EG) and H = (VH, EH) be two graphs.
The vertex set of each of the three products G ⊗H ( tensor product),
G × H ( Cartesian product) and G ⊠H ( strong product) is given by
VG × VH. To deﬁne the edge sets for each of these products, let
Ehor
:=
{{(x1, y), (x2, y)} | x1
G∼x2},
Evert
:=
{{(x, y1), (x, y2)} | y1
H∼y2},
Ediag
:=
{{(x1, y1), (x2, y2)} | x1
G∼x2 and y1
H∼y2}
denote the set of horizontal, vertical and diagonal edges. Then
G ⊗H
:=
(VG × VH, Ediag),
G × H
:=
(VG × VH, Ehor ∪Evert),
G ⊠H
:=
(VG × VH, Ehor ∪Evert ∪Ediag).
Note that, in the case of a dG-regular graph G and a dH-regular
graph H, the products G ⊗H, G × H and G ⊠H are (dGdH)-regular,
(dG + dH)-regular and (dG + dH + dgdH)-regular, respectively.
Our ﬁrst result is concerned with preservance of Ricci ﬂatness:
Theorem 5.2. Let G, H be two Ricci ﬂat graphs.
Then the graph
products G ⊗H, G × H and G ⊠H are again Ricci ﬂat. Similarly, all
three graph products preserve also (R)-Ricci ﬂatness, (S)-Ricci ﬂatness
and (RS)-Ricci ﬂatness.
Proof. Assume that G and H are Ricci ﬂat at x ∈VG and at y ∈VH,
respectively, that is, there exist maps ηG
i : B1(x) →VG (1 ≤i ≤dG)


## Page 22


22
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
and ηH
k : B1(y) →VH (1 ≤k ≤dH) satisfying the conditions (i),(ii),(iii)
in Deﬁnition 3.1.
Note that we have the inclusions
BG×H
1
(x, y), BG⊗H
1
(x, y) ⊂BG⊠H
1
(x, y).
We deﬁne the following maps η′
i, η′′
k, η⊗
jl : BG⊠H
1
(x, y) →VG × VH (for
1 ≤i, j ≤dG, 1 ≤k, l ≤dH):
η′
i(u, v)
:=
(ηG
i (u), v),
η′′
k(u, v)
:=
(u, ηH
k (v)),
η⊗
jl(u, v)
:=
(ηG
j (u), ηH
l (v)).
Note that
η⊗
jl = η′
j ◦η′′
l = η′′
l ◦η′
j.
We only consider the strong product case here, since all other products
can be dealt with similarly by restrictions of the relevant η-maps to
the corresponding 1-balls. We now check properties (i), (ii) and (iii) of
Deﬁnition 3.1 for these maps on BG⊠H
1
(x, y).
To verify (i), we observe that (u, v) ∼η′
i(u, v) represents a horizontal
edge in G ⊠H, (u, v) ∼η′′
k(u, v) represents a vertical edge and (u, v) ∼
η⊗
jl(u, v) represents a diagonal edge.
Next, we verify (ii): The above observation implies that η′
i(u, v), η′′
k(u, v)
and η⊗
jl(u, v) are mutually distinct for any choices of i, j, k, l. Moreover,
it is easy to check that
η′
i(u, v) ̸= η′
j(u, v),
η′′
k(u, v) ̸= η′′
l (u, v),
η⊗
ik(u, v) ̸= η⊗
jl(u, v)
for any choice of i ̸= j and k ̸= l.
Now we verify (iii): We have
[
j,l
η⊗
jl(η⊗
ik(x, y))
=
[
j
ηG
j ηG
i x ×
[
l
ηH
l ηH
k y
=
[
j
ηG
i ηG
j x ×
[
l
ηH
k ηH
l y
=
[
j,l
η⊗
ik(η⊗
jl(x, y)).
Similar commutation properties holds for the other families of η-maps,
that is, we have
[
∗
η∗η∗∗(x, y) =
[
∗
η∗∗η∗(x, y)


## Page 23


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
23
where η∗and η∗∗are maps within the families η′
i, η′′
k and η⊗
jl. Combining
these results, we obtain
[
j
η′
j(η⊗
ik(x, y)) ∪
[
l
η′′
l (η⊗
ik(x, y)) ∪
[
j,l
η⊗
jl(η⊗
ik(x, y))
=
[
j
η⊗
ik(η′
j(x, y)) ∪
[
j
η⊗
ik(η′
j(x, y)) ∪
[
j,l
η⊗
ik(η⊗
jl(x, y))
and
[
j
η′
j(η′
i(x, y)) ∪
[
l
η′′
l (η′
i(x, y)) ∪
[
j,l
η⊗
jl(η′
i(x, y))
=
[
j
η′
i(η′
j(x, y)) ∪
[
l
η′
i(η′′
l (x, y)) ∪
[
j,l
η′
i(η⊗
jl(x, y))
and
[
j
η′
j(η′′
k(x, y)) ∪
[
l
η′′
l (η′′
k(x, y)) ∪
[
j,l
η⊗
jl(η′′
k(x, y))
=
[
j
η′′
k(η′
j(x, y)) ∪
[
l
η′′
k(η′′
l (x, y)) ∪
[
j,l
η′′
k(η⊗
jl(x, y)).
In conclusion, Ricci ﬂatness is preserved for all three graph products.
Finally, we verify preservance of (R)-, (S)- and (RS)-Ricci ﬂatness.
Assume (R)-Ricci ﬂatness at x ∈VG and y ∈Vh. (R)-Ricci ﬂatness at
(x, y) follows now from
 η⊗
jl
2 (x, y) = (
 ηG
j
2 (x),
 ηH
l
2 (y)) = (x, y),
and (η′
i)2(x, y) = (η′′
k)2(x, y) = (x, y) can be checked similarly. Preser-
vance of (S)-Ricci ﬂatness follows from
η∗η∗∗(x, y) = η∗∗η∗(x, y)
where η∗and η∗∗are maps within the families η′
i, η′′
k and η⊗
jl.
□
In the case of Cartesian products of two regular graphs G, H, there
are explicit curvature formulas in terms of curvatures of the factors:
Bakry-´Emery curvature KG×H
∞
(x, y) = min{KG
∞(x), KH
∞(y)} can be found
in [9, Corollary 7.13] and Ollivier Ricci curvature κG×H
0
(x, y) and κG×H
LLY (x, y)
can be found in [14, Claim 1 and 2 in Proof of Theorem 3.1]. In par-
ticular, non-negativity of each of these curvature notions is preserved
under Cartesian products. In our next result, we provide lower cur-
vature bounds for horizontal and vertical edges of the strong product
G ⊠H:
Theorem 5.3. Let G and H be two regular graphs with vertex de-
grees dG and dH, respectively. Lower Ollivier Ricci curvature bounds


## Page 24


24
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
on horizontal edges and vertical edges are given by
κ∗((x1, y1), (x2, y1))
≥
dG(dH + 1)
dG⊠H
κG
∗(x1, x2),
κ∗((x1, y1), (x1, y2))
≥
dH(dG + 1)
dG⊠H
κH
∗(y1, y2),
where κ∗may refer to κ0 or κLLY and dG⊠H = dG + dH + dGdH is the
vertex degree of G ⊠H.
Proof of Theorem 5.3. Let us consider a horizontal edge (x1, y1) ∼(x2, y1)
where x1
G∼x2. We will prove this argument for Lin-Lu-Yau curvature
ﬁrst. Let πG ∈Π(µ1/(1+dG)
x1
, µ1/(1+dG)
x2
) be an optimal transport plan, i.e.,
its cost is equal to W G
1 (µ1/(1+dG)
x1
, µ1/(1+dG)
x2
). Now we deﬁne a function
π : (VG × VH)2 →[0, ∞) as follows:
π ((w1, z1), (w2, z2)) :=
(
1+dG
1+dG⊠H πG(w1, w2),
if z1 = z2 ∈B1(y1),
0,
otherwise.
Now we verify the following marginal constraints showing that π is in-
deed a transport plan π ∈Π(µ1/(1+dG⊠H)
(x1,y1)
, µ1/(1+dG⊠H)
(x2,y2)
): for ﬁxed (w1, z1) ∈
VG × VH,
X
w2,z2
π((w1, z1), (w2, z2))
=
1 + dG
1 + dG⊠H
· 1B1(y1)(z1)
X
w2
πG(w1, w2)
=
1 + dG
1 + dG⊠H
· 1B1(y1)(z1) · µ1/(1+dG)
x1
(w1)
=
1
1 + dG⊠H
· 1B1(y1)(z1) · 1B1(x1)(w1)
=
1
1 + dG⊠H
· 1B1(x1,y1)(w1, z1)
=
µ1/(1+dG⊠H)
(x1,y1)
(w1, z1),
and, similarly,
X
w1,z1
π((w1, z1), (w2, z2)) = µ1/(1+dG⊠H)
(x2,y1)
(w2, z2).
The cost of this transport plan can then be calculated as
cost(π)
=
X
(w2,z2)
X
(w1,z1)
distG⊠H ((w1, z1), (w2, z2)) π((w1, z1), (w2, z2))
=
X
z1∈B1(y1)
X
w1,w2
distG(w1, w2) 1 + dG
1 + dG⊠H
πG(w1, w2)
=
(1 + dH)(1 + dG)
1 + dG⊠H
X
w1,w2
distG(w1, w2)πG(w1, w2)
=
cost(πG).


## Page 25


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
25
Recall that πG is assumed to be an optimal transport plan and, there-
fore,
W G⊠H
1

µ1/(1+dG⊠H)
(x1,y1)
, µ1/(1+dG⊠H)
(x2,y1)

≤cost(π)
= cost(πG) = W G
1 (µ1/(1+dG)
x1
, µ1/(1+dG)
x2
).
This inequality translates via Deﬁnition 2.3 and relation (5) into:
κLLY ((x1, y1), (x2, y1)) ≥dG(dH + 1)
dG⊠H
κG
LLY (x1, x2),
which gives the desired lower bound for κLLY on the horizontal edge
(x1, y1) ∼(x2, y1).
Now we prove a similar lower bound for κ0. Let π0
G ∈Π(µ0
x1, µ0
x2) be
an optimal transport plan, whose cost is
cost(π0
G) =
X
w1,w2∈VG
(w1,w2)̸=(x1,x2)
distG(w1, w2)π0
G(w1, w2),
where the condition (w1, w2) ̸= (x1, x2) on the summation can be im-
posed because π0
G(x1, x2) = 0 due to marginal constraints of π0
G.
Deﬁne a function π0 : (VG × VH)2 →[0, ∞) as follows:
π0 ((w1, z1), (w2, z2))
:=





dG
dG⊠H π0
G(w1, w2),
if z1 = z2 ∈B1(y1) and (w1, w2) ̸= (x1, x2),
1
dG⊠H ,
if z1 = z2 ∈S1(y1) and (w1, w2) = (x1, x2),
0,
otherwise.
Now we verify that π0 ∈Π(µ0
(x1,y1), µ0
(x2,y1)): Let (w1, z1) ∈VG × VH.
We distinguish two cases:
(1) If w1 ̸= x1 we have
X
w2,z2
π0((w1, z1), (w2, z2))
=
dG
dG⊠H
· 1B1(y1)(z1)
X
w2
π0
G(w1, w2)
=
dG
dG⊠H
· 1B1(y1)(z1) · µ0
x1(w1)
=
1
dG⊠H
· 1B1(y1)(z1) · 1S1(x1)(w1)
=
µ0
(x1,y1)(w1, z1).
The last equality follows from the fact that w1 ̸= x1 implies
1B1(y1)(z1) · 1S1(x1)(w1) = 1B1(y1)(z1) · 1B1(x1)(w1)
= 1B1(x1,y1)(w1, z1) = 1S1(x1,y1)(w1, z1).


## Page 26


26
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
(2) If w1 = x1 we have
X
w2,z2
π0((x1, z1), (w2, z2))
= 1S1(y1)(z1)
1
dG⊠H
+ 1B1(y1)(z1) dG
dG⊠H
X
w2̸=x2
π0
G(x1, w2)
|
{z
}
=0
=
1
dG⊠H
1S1(y1)(z1) = µ0
(x1,y1)(x1, z1).
The veriﬁcation of
X
w1,z1
π0((w1, z1), (w2, z2)) = µ0
(x2,y1)(w2, z2)
is done similarly. The cost of π0 can then be calculated as
cost(π0)
=
X
(w2,z2)
X
(w1,z1)
distG⊠H ((w1, z1), (w2, z2)) π0((w1, z1), (w2, z2))
=
X
z1∈B1(y1)
X
(w1,w2)̸=(x1,x2)
distG(w1, w2) dG
dG⊠H
π0
G(w1, w2)
+
X
z1∈S1(y1)
distG(x1, x2)
1
dG⊠H
=
(1 + dH)dG
dG⊠H
cost(π0
G) +
dH
dG⊠H
.
Therefore, we have
W G⊠H
1
 µ0
(x1,y1), µ0
(x2,y1)

≤cost(π0) = (1 + dH)dG
dG⊠H
W G
1 (µ0
x1, µ0
x2)+ dH
dG⊠H
,
or equivalently
κ0((x1, y1), (x2, y1)) ≥dG(dH + 1)
dG⊠H
κG
0 (x1, x2),
which gives the desired lower bound for κ0.
In the same way we obtain analogous results for vertical edges:
κ∗((x1, y1), (x1, y2)) ≥dH(dG + 1)
dG⊠H
κH
∗(y1, y2).
□
Corollary 5.4. Let G and H be two regular graphs with non-negative
κ0 (or κLLY ). Then all horizontal and vertical edges of G ⊠H have
also non-negative κ0 (or κLLY ).
It turns out, however, that the statement of Corollary 5.4 is no longer
true for diagonal edges, as the following example shows.


## Page 27


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
27
Figure 6. Induced 2-ball of a quartic graph with
K∞(v0) = 0.013 and κLLY (v0, v1) = 2κ0(v0, v1) = 1,
κLLY (v0, v2) = 2κ0(v0, v2) = 0.5 and κLLY (v0, v3) =
κ0(v0, v3) = κLLY (v0, v4) = κ0(v0, v4) = 0.
Example 5.5. Let G be a 4-regular graph with an induced 2-ball B2(v0) =
{v0, . . . , v9} as shown in Figure 6. Then κ0(v0, vi) ≥0 for 1 ≤i ≤4
and K∞(v0) > 0. Let H = P∞be the bi-inﬁnite paths with vertices wj,
j ∈Z. Then κ0(w0, w±1) = κLLY (w0, w±1) = 0 and K∞(w0) = 0.
v0
v1
v2
v3
v4
v5
v6
v7
v8
v9
(v0, w2)
(v0, w1)
(v0, w0)
(v0, w−1)
(v0, w−2)
(v3, w1)
Figure 7. Local Ollivier Ricci curvatures κLLY of G and
G⊠P∞at edges incident to v0 and (v0, w0), respectively.
Positive/negative/zero curvatures of edges is represented
by the colours red/blue/grey. Every horizontal line of the
lower graph represents a projection of G.
However, the strong product G ⊠H has negative Ollivier Ricci cur-
vatures on the following diagonal edges (see Figure 7):
κ0((v0, w0), (v3, w±1) = κLLY ((v0, w0), (v3, w±1) = −0.071,


## Page 28


28
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
and negative Bakry-´Emery curvature at (v0, w0) (see Figure 8):
K∞(v0, w0) = −0.062.
Figure 8. Local Bakry-´Emery curvatures of G and G⊠
P∞at v0 and (v0, w0). Positive/negative curvatures of
vertices is represented by the colours red/blue. Every
horizontal line of the lower graph represents a projection
of G.
Remark 5.6. The previous example shows for strong products that
non-negativity of curvatures is generally not preserved for diagonal
edges. The same example can be used to show that this phenomenen
appears also in the case of tensor products, where only diagonal edges
are present.
Another interesting question about graphs products is the following:
In the case of Cartesian products, the full curvature function (as func-
tion of the dimension N) at a vertex (x, y) is completely determined by
the curvature functions of the factors at the vertices x and y (see [9,
Theorem 7.9]):
KG×H
(x,y) = KG
x ∗KH
y ,
where ∗is a special operation deﬁned in [9, Deﬁnition 7.1]. We would
like to know whether a similar formula (with a suitably deﬁned opera-
tion) can be proved for tensor products and strong products.


## Page 29


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
29
6. Distance-regular graphs
In this section we turn our focus on distance-regular graphs of girth
4, which is an interesting family of triangle-free graphs with maximal
curvature values for κ0, κLLY and K∞.
Distance-regular graphs are
deﬁned as follows:
Deﬁnition 6.1. A regular graph G = (V, E) is called distance-regular
if, for any pair x, y ∈V of vertices and any r, t ≥0 the cardinality of
Sr(x) ∩St(y) depends only on r, t, d(x, y).
The intersection array of a distance-regular graph G = (V, E) of
vertex degree d is deﬁned as an array of integers:
{b0, b1, . . . , bd−1; c1, . . . , cd},
deﬁned as follows: Fix x ∈V . Then, for 0 ≤i ≤d −1 and 1 ≤j ≤d,
we set bi = d+
x (z) for every z ∈Si(x) and cj = d−
x (z) for every z ∈
Sj(x).
Theorem 6.2. Let G = (V, E) be a distance-regular graph of vertex
degree d and girth 4. Then we have
(14)
κ0(x, y) = 0 and κLLY (x, y) = 2
d for all {x, y} ∈E,
and
(15)
K∞(x) = 2 for all x ∈V .
Note that the curvature values in (14) and (15) are upper curvature
bounds for any triangle-free d-regular graph by Proposition 4.1.
Theorem 6.2 is a generalization of [2, Theorem 4.10] and [9, Corollary
11.7(i) in the arXiv version], which are both concerned with the special
case of strongly regular graphs. Even though the proofs for this special
case carry over to the much larger class of distance-regular graphs, we
present them here for the reader’s convenience.
Proof. Let G = (V, E) be a distance-regular graph of vertex degree d
and girth 4 and {x, y} ∈E. By Remark 4.3(b), it suﬃces to show the
existence of a perfect matching between S1(x)\{y} and S1(y)\{x} to
conclude
(16)
κLLY (x, y) = 2
d.
Let H be the induced subgraph of the union of S1(x)\{y} and S1(y)\{x}.
Note that H is bipartite since G is triangle-free. Let X ⊂S1(x)\{y}
and Y be the set of neighbours of X in S1(y)\{x}.
The set Y is
nonempty due to the girth 4 assumption. Then we have the following
double-counting of the edges between X and Y :
(17)
X
w∈X
dH
w = |E(X, Y )| ≤
X
z∈Y
dH
z ,


## Page 30


30
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
where dH
w is the vertex degree of w in H. Using distance-regularity, we
obtain dH
w = dH
z = c2−1 and (17) implies |X| ≤|Y |. We can now apply
Hall’s Marriage Theorem to conclude that there is a perfect matching
between S1(x)\{y} and S1(y)\{x}.
By Theorem 1.1, (16) implies κ0(x, y) ≥0. Combining this with
Proposition 4.1(i), we conclude κ0(x, y) = 0.
For the calculation of the Bakry-´Emery curvature we employ the
method presented at the beginning of Section 8 of [9] and the notation
introduced there. In view of Theorem 8.1(i) in [9], we only need to
verify that λ1 = λ1(∆S′′
1 (x)) ≥d
2, since then
K∞(x) = 3 + d −av+
1 (x)
2
= 3 + d −(d −1)
2
= 2.
Triangle-freeness of G implies
∆S′′
1 (x) = ∆S1(x) + ∆S′
1(x) = ∆S′
1(x),
where ∆S′
1(x) is the weighted Laplacian on the 1-sphere S1(x) with the
following weights:
w′
y1y2 =
X
z∈S2(x)
y1∼z∼y2
1
d−
x (z) for all y1, y2 ∈S1(x), y1 ̸= y2.
Since G is distance-regular, we obtain d−
x (z) = c2 and
|{z ∈S2(x) : y1 ∼z ∼y2}| = c2 −1.
This implies w′
y1y2 = c2−1
c2
and, therefore, the Laplacian ∆S′
1(x) is c2−1
c2 ∆Kd,
where ∆Kd is the non-normalized Laplacian of the complete graph Kd.
Consequently, we have
λ1(∆S′
1(x)) = c2 −1
c2
λ1(∆Kd) = c2 −1
c2
d ≥d
2,
since c2 ≥2 because G has girth 4.
□
It is tempting to assume that distance-regular graphs of girth 4 are
always (R)-Ricci ﬂat and then using Theorems 3.4 and 3.5(b) to con-
clude the statement of Theorem 6.2. However, the following example
shows that this assumption is not always true. It remains an open
question, however, whether every distance-regular graph of girth 4 is
Ricci ﬂat.
Example 6.3 (Incidence graph of (11, 6, 3)-design). This is a distance-
regular graph with intersection array {6, 5, 3; 1, 3, 6} (see [10]).


## Page 31


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
31
The structure of the incomplete 2-ball around a vertex x is given by:
S1(x)
=
{v1, ..., v6}
and
S2(x) = {v7, ..., v16}
v1
∼
v8, v11, v13, v14, v15
v2
∼
v7, v10, v11, v12, v13
v3
∼
v9, v10, v11, v15, v16
v4
∼
v7, v8, v10, v14, v16
v5
∼
v8, v9, v12, v13, v16
v6
∼
v7, v9, v12, v14, v15
We give an indirect prove that this graph is not (R)-Ricci ﬂat. As-
sume otherwise, i.e., there exists an associated matrix A with only 0
entries on diagonal. The other possible entries of A listed as below:










1
2
3
4
5
6
1
0
11, 13
11, 15
8, 14
8, 13
14, 15
2
11, 13
0
10, 11
7, 10
12, 13
7, 12
3
11, 15
10, 11
0
10, 16
9, 16
9, 15
4
8, 14
7, 10
10, 16
0
8, 16
7, 14
5
8, 13
12, 13
9, 16
8, 16
0
9, 12
6
14, 15
7, 12
9, 15
7, 14
9, 12
0










,








0
11, 13
11, 15
8, 14
8, 13
14, 15
11, 13
0
10, 11
7, 10
12, 13
7, 12
11, 15
10, 11
0
10, 16
9, 16
9, 15
8, 14
7, 10
10, 16
0
8, 16
7, 14
8, 13
12, 13
9, 16
8, 16
0
9, 12
14, 15
7, 12
9, 15
7, 14
9, 12
0








,
Recall that the matrix A cannot have repeated entries in any row and
column. If the entry of A12 is chosen to be 11, then all entries for the
ﬁrst three rows are uniquely determined as the numbers in red. Then
the entry of A46 cannot be either 7 or 14, due to appearance of them in
the sixth column. Contradiction!
Similarly, if the entry of A12 is chosen to be 13, then all entries for
the ﬁrst three rows must be the numbers in blue. Then the entry of A45
cannot be either 8 or 16 due to the ﬁfth column. Contradiction!
In conclusion, the Incidence graph of (10, 6, 3)-design is not (R)-
Ricci ﬂat, even though it is triangle-free and has both maximum possi-
ble Bakry-´Emery curvature K∞(x) = 2 and maximum possible Olliver
Ricci curvature κLLY (x, y) = 2
d.


## Page 32


32
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
However, the vertices of this graph are Ricci ﬂat via the following
matrix choice for A:







11
0
15
8
13
14
13
12
11
10
0
7
0
11
10
16
9
15
14
10
16
7
8
0
8
13
9
0
16
12
15
7
0
14
12
9







.
Appendix: The complete bipartite graphs Kd,d
We will show the following facts:
(1) Kd,d is (R)-Ricci ﬂat for all d,
(2) Kd,d is (S)-Ricci ﬂat for all d,
(3) Kd,d is (RS)-Ricci ﬂat if and only if d is even.
As before, we translate Ricci ﬂatness properties at a vertex x, given
by the maps ηi, into properties of the associated d × d-matrix A =
(Aij). Since Kd,d is triangle-free, we use a slightly diﬀerent enumeration
system for the matrix A: Let S1(x) = {y1, . . . , yd} where yj := ηj(x),
and S2(x) =: {z1, . . . , zt} and, furthermore, z0 := x. Then the entries
Aij ∈{0, 1, . . . , t} of A are given via the relation
zAij = ηi(yj)
and we have the following correspondences:
(a) ηi is injective corresponds to Aij ̸= Aik for all j ̸= k,
(b) ηi(yk) ̸= ηj(yk) corresponds to Aik ̸= Ajk for all i ̸= j,
(c) η2
i (x) = x corresponds to Aii = 0,
(d) ηj(ηix) = ηi(ηjx) corresponds to Aji = Aij.
In other words, (a) corresponds to the property that A has no repeated
entries in the i-th row and (b) correspond to the property that A has
no repeated entries in the k-th column. Moreover, (R)-Ricci ﬂatness
requires in addition that the matrix A has only the entry 0 on the
diagonal, (S)-Ricci ﬂatness requires that A is symmetric, and (RS)-
Ricci ﬂatness requires both additional properties of the matrix A. Note
the general fact:
(e) The number of occurrences of the entry m ∈{0, . . . , t} in the
matrix A is equal to d−
x (zm).
(1)-(3) can now be shown by providing suitable matrices A.
Proof of (1):
A =






0
1
2
· · ·
d −1
d −1
0
1
· · ·
d −2
d −2
d −1
0
· · ·
d −3
...
...
...
...
...
1
2
3
· · ·
0






.


## Page 33


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
33
Note that the ﬁrst row of A is ﬁxed and the following rows are obtained
by a right shift of the previous row.
Proof of (2):
A =






0
1
2
· · ·
d −1
1
2
3
· · ·
0
2
3
4
· · ·
1
...
...
...
...
...
d −1
0
1
· · ·
d −2






.
Note that the ﬁrst row of A is ﬁxed and the following rows are obtained
by a left shift of the previous row.
Proof of (3): Assume d = 2n even. Then we can choose A to be





















0
1
2
3
· · ·
n −1
n
n + 1
· · ·
2n −3
2n −2
2n −1
1
0
3
4
n
n + 1
2n −1
2
2
3
0
...
...
1
4
3
4
...
2
6
...
...
...
n −1
n
...
0
2n −1
1
n −2
2n −2
n
n + 1
2n −1
0
2
n −1
1
n + 1
...
1
2
...
n
3
...
2
...
...
...
...
...
...
...
2n −2
2n −1
1
2
n −2
n −1
n
0
2n −3
2n −1
2
4
6
· · ·
2n −2
1
3
· · ·
· · ·
2n −3
0





















,
constructed as follows:
• Aii = 0 for all 1 ≤i ≤2n,
• Aij = i + j −2 for i ̸= j and i + j ≤2n + 1,
• Aij = i + j −2n −1 for i ̸= j, i + j ≥2n + 2 and i, j ≤2n,
• Ai,2n = A2n,i = 2(i −1) for 1 ≤i ≤n,
• Ai,2n = A2n,i = 2(i −n) −1 for n + 1 ≤i ≤2n −1.
Finally, assume that d is odd and x is (RS)-Ricci ﬂat with associated
symmetric matrix A with vanishing diagonal. Since d−
x (zm) = d for all
m ∈{0, . . . , t}, each entry m appears exactly d times in the matrix
A by (e) above. Since d is odd and A symmetric, every entry must
appear at least once on the diagonal, contradicting to the assumption
of a vanishing diagonal.
References
[1] D. Bakry and M. ´Emery, Diﬀusions hypercontractives (French) [Hypercontrac-
tive diﬀusions], S´eminaire de probabilit´es, XIX, 1983/84, Lecture Notes in Math.
1123, J. Az´ema and M. Yor (Editors), Springer, Berlin, 1985, 177–206.
[2] V. Bonini, C. Carroll, U. Dinh, S. Dye, J. Frederick and E. Pearse, Condensed
Ricci Curvature of Complete and Strongly Regular Graphs, arXiv:1907.06733.


## Page 34


34
CUSHING, KAMTUE, KANGASLAMPI, LIU, AND PEYERIMHOFF
[3] D. Bourne, D. Cushing, S. Liu, F. M¨unch and N. Peyerimhoﬀ, Ollivier-Ricci
idleness functions on graphs, SIAM J. Discrete Math. 32(2) (2018), 1408–1424.
[4] H. Brezis, Remarks on the Monge-Kantorovich problem in the discrete setting,
C. R. Math. Acad. Sci. Paris 356(2) (2018), 207–213.
[5] A. E. Brouwer and W. H. Haemers, Spectra of graphs, Universitext, Springer,
New York, 2012.
[6] F. R. K. Chung and S.-T. Yau, Logarithmic Harnack inequalities, Math. Res.
Lett. 3(6) (1996), 793–812.
[7] D. Cushing, S. Kamtue, J. Koolen, S. Liu, F. M¨unch and N. Peyerimhoﬀ, Rigid-
ity of the Bonnet-Myers inequality for graphs with respect to Ollivier Ricci cur-
vature, arXiv:1807.02384.
[8] D. Cushing, R. Kangaslampi, V. Lipi¨ainen, S. Liu and G. W. Stagg, The Graph
Curvature Calculator and the curvatures of cubic graphs, Exp. Math. (2019),
1–13, doi.org/10.1080/10586458.2019.1660740.
[9] D. Cushing, S. Liu, and N. Peyerimhoﬀ, Bakry-´Emery Curvature Functions
on Graphs, Canad. J. Math. (2019), 1–55, doi.org/10.4153/CJM-2018-015-4,
arXiv:1606.01496.
[10] Online
repository
of
distance-regular
graphs
at
https://www.
distanceregular.org/
[11] K. D. Elworthy, Manifolds and graphs with mostly positive curvatures, Sto-
chastic Analysis and Applications, Progr. Probab. 26 (1991), 96–110.
[12] F. Gurr and L. W. May, Incomplete 2-Balls with Non-negative Curved Centre
for Quartic Graphs, Ancillary ﬁle ”non-negative-classiﬁcation.pdf” of D. Cush-
ing, S. Kamtue, N. Peyerimhoﬀ, L. Watson May: Quartic graphs which are
Bakry-´Emery curvature sharp, arXiv:1903.10665.
[13] J. Jost and S. Liu, Olliviers Ricci curvature, local clustering and curvature-
dimension inequalities on graphs, Discrete Comput. Geom. 51 (2014), 300-322.
[14] Y. Lin, L. Lu and S.-T. Tau, Ricci curvature of graphs, Tohoku Math. J. (2)
63(4) (2011), 605–627.
[15] Y. Lin and S.-T. Yau, Ricci curvature and eigenvalue estimate on locally ﬁnite
graphs, Math. Res. Lett. 17(2) (2010), 343–356.
[16] Y. Ollivier, Ricci curvature of Markov chains on metric spaces, J. Funct. Anal.
256 (2009), 810–864.
[17] Peter Ralli, Bounds on curvature in regular graphs, arXiv:1701.08205.
[18] M. Schmuckenschl¨ager, Curvature of nonlocal Markov generators, in Convex
geometric analysis (Berkeley, CA, 1996), Math. Sci. Res. Inst. Publ. 34, Cam-
bridge Univ. Press, Cambridge, 1999, 189–197.
[19] C. Villani, Topics in optimal transportation, Graduate Studies in Mathematics
58, American Mathematical Society, Providence, RI, 2003.
[20] C. Villani, Optimal transport, old and new, Grundlehren der Mathematischen
Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 338,
Springer-Verlag, Berlin, 2009.


## Page 35


CURVATURES, GRAPH PRODUCTS AND RICCI FLATNESS
35
D. Cushing, Department of Mathematical Sciences, Durham Univer-
sity, Durham DH1 3LE, United Kingdom
E-mail address: davidcushing1024@gmail.com
S. Kamtue, Department of Mathematical Sciences, Durham Univer-
sity, Durham DH1 3LE, United Kingdom
E-mail address: supanat.kamtue@durham.ac.uk
R. Kangaslampi, Unit of Computing Sciences, Tampere University
33014, Tampere 33014, Finland
E-mail address: riikka.kangaslampi@tuni.fi
S. Liu, School of Mathematical Sciences, University of Science and
Technology of China, Hefei 230026, China
E-mail address: spliu@ustc.edu.cn
N. Peyerimhoff, Department of Mathematical Sciences, Durham Uni-
versity, Durham DH1 3LE, United Kingdom
E-mail address: norbert.peyerimhoff@durham.ac.uk

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
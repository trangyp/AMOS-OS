---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1103.1264v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1103.1264v1_Polynomial_cases_of_the_Discretizable_Molecular_Distance_Geometry_Problem

> Source: 1103.1264v1_Polynomial_cases_of_the_Discretizable_Molecular_Distance_Geometry_Problem.pdf

> Pages: 12

---


## Page 1


arXiv:1103.1264v1  [cs.CG]  7 Mar 2011
Polynomial cases of the Discretizable Molecular Distance
Geometry Problem
Leo Liberti1, Carlile Lavor2, Benoˆıt Masson3, Antonio Mucherino4
1 LIX, ´Ecole Polytechnique, 91128 Palaiseau, France
Email:liberti@lix.polytechnique.fr
2 Dept. of Applied Maths (IME-UNICAMP), State Univ. of Campinas, 13081-970, Campinas - SP,
Brazil
Email: clavor@ime.unicamp.br
3 IRISA, INRIA, Campus de Beaulieu, 35042 Rennes, France
Email: benoit.masson@inria.fr
4 CERFACS, Toulouse, France
Email: antonio.mucherino@cerfacs.fr
October 26, 2018
Abstract
An important application of distance geometry to biochemistry studies the embeddings of the
vertices of a weighted graph in the three-dimensional Euclidean space such that the edge weights are
equal to the Euclidean distances between corresponding point pairs. When the graph represents the
backbone of a protein, one can exploit the natural vertex order to show that the search space for
feasible embeddings is discrete. The corresponding decision problem can be solved using a binary
tree based search procedure which is exponential in the worst case. We discuss assumptions that
bound the search tree width to a polynomial size.
Keywords: Branch-and-Prune, symmetry, distance geometry.
1
Introduction
We study the following decision problem [5]:
Discretizable Molecular Distance Geometry Problem (DMDGP). Given a simple
undirected weighted graph G = (V, E, d) where d : E →R+, V is ordered so that V = [n] =
{1, . . ., n}, and the following assumptions hold:
1. for all v > 3 and u ∈V with 1 ≤v −u ≤3, {u, v} ∈E (Discretization)
2. for all v > 3, E contains all edges {u, w} with u ̸= w ∈Uv = {u ∈V | 1 ≤v −u ≤3},
and the distances duw with u ̸= w ∈Uv obey the strict simplex inequalities [1] (Strict
Simplex Inequalities),
and given an embedding x′ : [3] →R3, is there an embedding x : V →R3 extending x′, such
that
∀{u, v} ∈E
∥xu −xv∥= duv ?
(1)
Note that the strict simplex inequalities in R3 reduce to the strict triangular inequalities dv−3,v−1 <
dv−3,v−2 + dv−2,v−1. An embedding x extends an embedding x′ if x′ is a restriction of x; an embedding
is feasible if it satisﬁes (1). We also consider the following problem variants:


## Page 2


2
THE BP ALGORITHM
2
• DMDGPK, i.e. the family of decision problems (parametrized by the positive integer K) obtained
by replacing each symbol ‘3’ in the DMDGP deﬁnition by the symbol ‘K’;
• the KDMDGP, where K is given as part of the input (rather than being a ﬁxed constant as in the
DMDGPK).
We remark that DMDGP=DMDGP3. Other related problems also exist in the literature, such as the
Discretizable Distance Geometry Problem (DDGP) [13], where the Discretization axiom is
relaxed to require that each vertex v > K has at least K adjacent predecessors. The original results in
this paper, however, only refer to the DMDGP and its variants.
The Discretization axiom guarantees that the locus of the points embedding v in R3 is the intersec-
tion of the three spheres centered at v −3, v −2, v −1 with radii dv−3,v, dv−2,v, dv−1,v. If this intersection
is non-empty, then it contains two points apart from a set of Lebesgue measure 0 where it may contain
either one point or inﬁnitely many. The role of the Strict Simplex Inequalities axiom is to prevent
the latter case of inﬁnitely many points. As such we might actually dispense with this axiom altogether
and simply discuss results that occur with probability 1. We remark that if the intersection of the three
spheres is empty, then the instance is a NO one. The Discretization axiom allows the solution of
DMDGP instances using a recursive algorithm called Branch-and-Prune (BP) [9]: at level v, the search
is branched according to the (at most two) possible positions for v. The BP generates a (partial) binary
search tree of height n, each full branch of which represents a feasible embedding for the given graph.
The DMDGP and its variants are related to the Molecular Distance Geometry Problem
(MDGP), which asks to ﬁnd an embedding in R3 of a given weighted undirected graph. We denote
the generalization of the MDGP to embeddings in RK where K is part of the input by Distance Ge-
ometry Problem (DGP), and the variants with ﬁxed K by DGPK. The MDGP is a good model for
determining the structure of molecules given a set of inter-atomic distances [10, 8]. Such distances can
usually be found using Nuclear Magnetic Resonance (NMR) experiments [17], a technique which allows
the detection of inter-atomic distances below 5˚A. The DGP has applications in wireless sensor networks
[4] and graph drawing. In general, the MDGP and DGP implicitly require a search in a continuous
Euclidean space [10].
The DMDGP is a model for protein backbones. For any atom v ∈V , the distances dv−1,v and dv−2,v−1
are known because they refer to covalent bonds. Furthermore, the angle between v −2, v −1 and v is
known because it is adjacent to two covalent bonds, which implies that dv−2,v is also known by triangular
geometry. In general, the distance dv−3,v is smaller than 5˚A and can therefore be assumed to be known
by NMR experiments; in practice, there are ways to ﬁnd atomic orders which ensure that dv−3,v is known
[7]. There is currently no known protein with dv−3,v−1 being exactly equal to dv−3,v−2 + dv−2,v−1 [9].
The rest of this paper is organized as follows. In Sect. 2 we describe the BP algorithm. In Sect. 3
we discuss complexity issues. Sect. 4 describes some polynomial DMDGP subclasses. We make several
important contributions: an NP-hardness proof for the KDMDGP and the DMDGPK (for K > 2), a
new proof that the number of feasible embeddings of DMDGP instances is a power of two, and some
practically relevant polynomial cases of the DMDGP.
2
The BP algorithm
For all v ∈V we let N(v) = {u ∈V | {u, v} ∈E} be the set of vertices adjacent to v. An embedding
of a subgraph of G is called a partial embedding of G. We denote by X the set of embeddings (modulo
congruences) solving a DMDGPK (or KDMDGP) instance.
The BP algorithm exploits the edges guaranteed by the Discretization axiom in order to search
a discrete set: vertex v can be placed in at most two possible positions (the intersection of K spheres
in RK). Each is tested in turn and the procedure called recursively for each feasible positions. The


## Page 3


3
COMPLEXITY
3
BP exploits all other edges in the graph in order to prune some branches: a position might be feasible
with respect to the distances to the K immediate predecessors v −1, . . . , v −K, but not necessarily with
distances to other adjacent predecessors.
For a partial embedding ¯x of G and {u, v} ∈E let S ¯x
uv be the sphere centered at xu with radius duv.
The BP algorithm, used for solving the DMDGP and its variants, is BP(K + 1, x′, ∅) (see Alg. 1), where
Algorithm 1 BP(v, ¯x, X)
Require: A vtx. v ∈V ∖[K], a partial embedding ¯x = (x1, . . . , xv−1), a set X.
1: P =
T
u∈N(v)
u<v
S ¯x
uv;
2: ∀p ∈P ( (x ←(¯x, p)); if (v = n) X ←X ∪{x} else BP(v + 1, x, X) ).
x′ is the initial embedding of the ﬁrst K vertices mentioned in the DMDGP deﬁnition. By the DMDGP
axioms, |P| ≤2. At termination, X contains all embeddings (modulo congruences) extending x′ [9, 5].
Embeddings x ∈X can be represented by sequences χ(x) ∈{−1, 1}n with: (i) χ(x)i = 1 for all i ≤K;
(ii) for all i > K, χ(x)i = −1 if axi < a0 and χ(x)i = 1 if axi ≥a0, where ax = a0 is the equation of the
hyperplane through xi−K, . . . , xi−1. For an embedding x ∈X, χ(x) is the chirality of x [2] (the formal
deﬁnition of chirality actually states χ(x)0 = 0 if axi = a0, but since this event has probability 0, we do
not consider it here).
The BP (Alg. 1) can be run to termination to ﬁnd all possible embeddings of G, or stopped after the
ﬁrst leaf node at level n is reached, in order to ﬁnd just one embedding of G. In the last few years we
have conceived and described several BP variants targeting diﬀerent problems [6], including, very recently,
problems with interval-type uncertainties on some of the distance values [7]. Compared to continuous
search algorithms (e.g. [12]), the performance of the BP algorithm is impressive from the point of view
of both eﬃciency and reliability. The BP algorithm, moreover, is currently the only method able to ﬁnd
all embeddings for a given protein backbone.
3
Complexity
Any class of YES instances where each vertex v only has distances to the K immediate predecessors
provides a full BP binary search tree (after level K), and therefore shows that the BP is an exponential-
time algorithm in the worst case. One remarkable feature of the computational experiments conducted
on our BP implementation [15] on protein instances is that the exponential-time behaviour of the BP
algorithm was never noticed empirically. When we were able to embed protein backbones of ten thousand
atoms in just over 13 seconds of CPU time (on a single core) [14], we started to suspect that protein
instances might have some special properties ensuring that the BP ran in polynomial time. Speciﬁcally,
using the particular structure of the protein graph, we argue in Sect. 4 that it is reasonable to expect
that the BP will yield a search tree of bounded width.
Restricting d to only take integer values, the DGP1 is NP-complete by reduction from Subset-Sum,
the DGPK is (strongly) NP-hard by reduction from 3-SAT, and the DGP is (strongly) NP-hard by
induction on K [16]. Only the DGP1 is NP-complete because if d is integer then the YES-certiﬁcate
x (the embedding) can be chosen to have integer values. It is currently not known whether there is a
polynomial length encoding of the algebraic numbers that can be used to show that DGP is in NP.
The DMDGP is NP-hard by reduction from Subset-Sum (Thm. 3 in [5]). We generalize that proof
to the DMDGPK. Intuitively, we exploit the fact that a subset sum instance a1, . . . , aN with solution
s1, . . . , sN ∈{−1, 1} has P
ℓ≤N sℓaℓ= 0 (the zero-sum property) to construct a DMDGP instance with
KN +1 points, where the zero-th point is at the origin and the ℓ-th set of K successive points is associated
to aℓ; the j-th point in the ℓ-th set adds sℓaℓto its j-th coordinate, so that the last point is again the
origin (all coordinates satisfy the Subset-Sum’s zero-sum property).


## Page 4


4
BP SEARCH TREES WITH BOUNDED WIDTH
4
3.1 Theorem
The DMDGPK is NP-hard for all K ≥2.
Proof.
Let a = (a1, . . . , aN) be an instance of Subset-Sum consisting of positive integers, and deﬁne
an instance of DMDGPK where V = {0, . . . , KN}, E includes {i, i + j} for all j ∈{1, . . . , K} and
i ∈{0, . . . , KN −j}, and:
∀i ∈{0, . . . , KN −1}
di,i+1
=
a⌊i/K⌋
(2)
∀j ∈{2, . . . , K}, i ∈{0, . . ., KN −j}
di,i+j
=
v
u
u
t
j
X
ℓ=1
d2
i+ℓ−1,i+ℓ
(3)
d0,KN
=
0.
(4)
Let s ∈{−1, 1}N be a solution of the Subset-Sum instance a. We let x0 = 0 and for all i = K(ℓ−1)+j >
0 we let xi = xi−1 +sℓaℓej, where ej is the vector with a one in component j and zero elsewhere. Because
P
ℓ≤N sℓaℓ= 0, if s solves the Subset-Sum instance a then, by inspection, x solves the corresponding
DMDGP instance (2)-(4).
Conversely, let x be an embedding that solves (2)-(4), where we assume
without loss of generality that x0 = 0. Then (3) ensures that the line through xi, xi−1 is orthogonal
to the line through xi−1, xi−2 for all i > 1, and again we assume without loss of generality that, for
all j ∈{1, . . . , K}, the lines through xj−1, xj are parallel to the i-th coordinate axis. Now consider the
chirality χ of x: because all distance segments are orthogonal, for each j ≤K the j-th coordinate is given
by xKN,j =
P
i mod K=j
χia⌊i/K⌋. Since d0,KN = 0, for all j ≤K we have 0 = xKN,j = P
ℓ≤N χK(ℓ−1)+jaℓ,
which implies that, for all j ≤K, sj = (χK(ℓ−1)+j | 1 ≤ℓ≤N) is a solution for the Subset-Sum
instance a.
✷
3.2 Corollary
The KDMDGP is NP-hard.
Proof. Every speciﬁc instance of the KDMDGP speciﬁes a ﬁxed value for K and hence belongs to the
DMDGPK. Hence the result follows by inclusion.
✷
4
BP search trees with bounded width
We partition E into the sets ED = {{u, v} | |v−u| ≤K} and EP = E∖ED. We call ED the discretization
edges and EP the pruning edges. Discretization edges guarantee that a DGP instance is in the KDMDGP.
Pruning edges are used to reduce the BP search space by pruning its tree. In practice, pruning edges
might make the set P in Alg. 1 have cardinality 0 or 1 instead of 2. We assume G is a YES instance of
the KDMDGP.
4.1
The discretization group
Let GD = (V, ED, d) and XD be the set of embeddings of GD; since GD has no pruning edges, the
BP search tree for GD is a full binary tree and |XD| = 2n−K. The discretization edges arrange the
embeddings so that, at level ℓ, there are 2ℓ−K possible embeddings xv for the vertex v with rank ℓ. We
assume that |P| = 2 at each level v of the BP tree, an event which, in absence of pruning edges, happens
with probability 1 — thus many results in this section are stated with probability 1. Let xv, x′
v the
possible embeddings of v at level v of the tree; then by elementary spherical geometry considerations, x′
v
is the reﬂection of xv through the hyperplane deﬁned by xv−K, . . . , xv−1. Denote this reﬂection by Rv
x.


## Page 5


4
BP SEARCH TREES WITH BOUNDED WIDTH
5
4.1 Theorem (Cor. 4.5 and Thm. 4.8 in [11])
With probability 1, for all v > K and u < v −K there is a set Huv, with |Huv| = 2v−u−K, of real
positive values such that for each x ∈X we have ∥xv −xu∥∈Huv. Furthermore, ∀x ∈X ∥xv −xu∥=
∥Ru+K
x
(xv) −xu∥and ∀x′ ∈X, if x′
v ̸∈{xv, Ru+K
x
(xv)} then ∥xv −xu∦= ∥x′
v −xu∥.
Proof. Sketched in Fig. 1 for K = 2; the circles mark equidistant levels from 1. Intuitively, two branches
from level 1 to level 4 or 5 will have equal segments but diﬀerent angles, which will cause the end dots
to be at diﬀerent distances from level 1. The formal proof is by induction on the level distance.
✷
ν1
ν2
1
2
5
3
4
ν3
ν4
ν5
ν6
ν7
ν8
ν9
ν10
ν11
ν12
ν13
ν14
ν15
ν16
Figure 1: A pruning edge {1, 4} prunes either ν6, ν7 or ν5, ν8.
We now deﬁne partial reﬂection operators:
gv(x) = (x1, . . . , xv−1, Rv
x(xv), . . . , Rv
x(xn)).
(5)
The gv’s map an embedding x to its partial reﬂection with ﬁrst branch at v. It is evident that the gv’s
are injective with probability 1 and idempotent.
4.2 Lemma
For u, v ∈V such that u, v > K, gugv(x) = gvgu(x).
Proof. Assume without loss of generality u < v. Then:
gugv(x)
=
gu(x1, . . . , xv−1, Rv
x(xv), . . . , Rv
x(xn))
=
(x1 . . . , xu−1, Ru
gv(x)(xu), . . . , Ru
gv(x)Rv
x(xv), . . . , Ru
gv(x)Rv
x(xn))
=
(x1 . . . , xu−1, Ru
x(xu), . . . , Rv
gu(x)Ru
x(xv), . . . , Rv
gu(x)Ru
x(xn))
=
gv(x1, . . . , xu−1, Ru
x(xu), . . . , Ru
x(xn))
=
gvgu(x),
where Ru
gv(x)Rv
x(xw) = Rv
gu(x)Ru
x(xw) for each w ≥v by Lemma 4.2 in [11].
✷
We deﬁne the discretization group to be the group GD = ⟨gv | v > K⟩generated by the gv’s


## Page 6


4
BP SEARCH TREES WITH BOUNDED WIDTH
6
4.3 Corollary
With probability 1, GD is an Abelian group isomorphic to Cn−K
2
.
For all v > K let γv = (1, . . . , 1, −1v, . . . , −1) be the vector consisting of one’s in the ﬁrst v−1 components
and −1 in the last components. Then the gv actions are directly mapped onto the chirality functions.
4.4 Lemma
For all x ∈X, χ(gv(x)) = χ(x) ⊙γv, where ⊙is the componentwise vector multiplication.
Proof. This follows by deﬁnition of gv and of chirality of an embedding.
✷
Because, by Alg. 1, each x ∈X has a diﬀerent chirality, for all x, x′ ∈X there is g ∈GD such
that x′ = g(x), i.e. the action of GD on X is transitive. By Thm. 4.1, the distances associated to the
discretization edges are invariant with respect to the discretization group.
4.2
The pruning group
Consider a pruning edge {u, v} ∈EP . By Thm. 4.1, with probability 1 we have duv ∈Huv, otherwise
the instance could not be a YES one. Also, again by Thm. 4.1, duv = ∥xu −xv∦= ∥gw(x)u −gw(x)v∥for
all w ∈{u + K, . . . , v} (note that distance ∥ν1 −ν9∥in Fig. 1 is diﬀerent from all its reﬂections ∥ν1 −νh∥
with h ∈{10, 11, 13} w.r.t. g4, g5). We therefore deﬁne the pruning group GP = ⟨gw | w > K ∧∀{u, v} ∈
EP (w ̸∈{u + K, . . . , v})⟩. It is easy to show that GP ≤GD. By deﬁnition, the distances associated with
the pruning edges are invariant with respect to GP .
4.5 Theorem (Thm. 5.4 in [11])
The action of GP on X is transitive.
|X| was shown to be a power of two with probability 1 in the unpublished technical report [11]. We
provide an shorter and clearer proof.
4.6 Theorem
With probability 1, ∃ℓ∈N |X| = 2ℓ.
Proof. Since GD ∼= Cn−K
2
, |GD| = 2n−K. Since GP ≤GD, |GP | divides the order of |GD|, which implies
that there is an integer ℓwith |GP | = 2ℓ. By Thm. 4.5, the action of GP on X only has one orbit,
i.e. GP x = X for any x ∈X. By idempotency, for g, g′ ∈GP , if gx = g′x then g = g′. This implies
|GP x| = |GP |. Thus, for any x ∈X, |X| = |GP x| = |GP | = 2ℓ.
✷
4.3
The number of nodes in function of pruning edges
Fig. 2 shows a Directed Acyclic Graph (DAG) Duv that we use to compute the number of valid nodes in
function of pruning edges between two vertices u, v ∈V such that v > K and u < v −K. The ﬁrst line
shows diﬀerent values for the rank of v w.r.t. u; an arc labelled with an integer i implies the existence of
a pruning edge {u + i, v} (arcs with ∨-expressions replace parallel arcs with diﬀerent labels). An arc is
unlabelled if there is no pruning edge {w, v} for any w ∈{u, . . ., v −K −1}. The vertices of the DAG
are arranged vertically by BP search tree level, and are labelled with the number of BP nodes at a given
level, which is always a power of two by Thm. 4.6. A path in this DAG represents the set of pruning
edges between u and v, and its incident vertices show the number of valid nodes at the corresponding
levels. For example, following unlabelled arcs corresponds to no pruning edge between u and v and leads
to a full binary BP search tree with 2v−K nodes at level v.


## Page 7


4
BP SEARCH TREES WITH BOUNDED WIDTH
7
1
1
1
1
1
1
2
2
2
2
2
4
4
4
4
8
8
8
16
16
32
v
u+K−1
u+K
u+K+1
u+K+2
u+K+3
u+K+4
0
0
0
0
0
0
0
0
0
0
0
1
1
1
1
1
1
1
2
2
2
2
3
3
4
0 ∨1
1 ∨2
2 ∨3
3 ∨4
0 ∨1 ∨2
1 ∨2 ∨3
2∨3∨4
0 ∨. . . ∨3
1 ∨. . . ∨4
0 ∨. . . ∨4
Figure 2: Number of valid BP nodes (vertex label) at level u + K + ℓ(column) in function of the pruning
edges (path spanning all columns).
4.4
Polynomial DMDGP cases
For a given GD, each possible pruning edge set EP corresponds to a path spanning all columns in D1n.
Instances with diagonal (Prop. 4.7) or below-diagonal (Prop. 4.8) EP paths yield BP trees with constant
width.
4.7 Proposition
If ∃v0 > K s.t. ∀v > v0 ∃!u < v −K with {u, v} ∈EP then the BP search tree width is bounded by
2v0−K.
Proof. This corresponds to a path p0 = (1, 2, . . . , 2v0−K, . . . , 2v0−K) that follows unlabelled arcs up to
level v0 and then arcs labelled v0 −K −1, v0 −K −1 ∨v0 −K, and so on, leading to nodes that are all
labelled with 2v0−K (Fig. 3, left).
✷
4.8 Proposition
If ∃v0 > K such that every subsequence s of consecutive vertices >v0 with no incident pruning edge is
preceded by a vertex vs such that ∃us < vs (vs −us ≥|s|∧{us, vs} ∈EP ), then the BP search tree width
is bounded by 2v0−K.
Proof. (Sketch) This situation corresponds to a below-diagonal path, Fig. 3 (right).
✷
In general, for those instances for which the BP search tree width has a O(log n) bound, the BP has
a polynomial worst-case running time O(L2log n) = O(Ln), where L is the complexity of computing P.
Since L is typically constant in n [3], for such cases the BP runs in linear time O(n).
Let V ′ = {v ∈V | ∃ℓ∈N (v = 2ℓ)}.
4.9 Proposition
If ∃v0 > K s.t. for all v ∈V ∖V ′ with v > v0 there is u < v −K with {u, v} ∈EP then the BP search
tree width at level n is bounded by 2v0n.


## Page 8


5
CONCLUSION
8
1
1
1
1
1
1
2
2
2
2
2
4
4
4
4
8
8
8
16
16
32
1
1
1
1
1
1
2
2
2
2
2
4
4
4
4
8
8
8
16
16
32
Figure 3: A path p0 with treewidth 8 (left) and another path below p0 (right).
Proof. This corresponds to a path along the diagonal 2v0 apart from logarithmically many vertices in V
(those in V ′), at which levels the BP doubles the number of search nodes (Fig. 4).
✷
1
2
4
8
16
32
64
128
1
2
4
8
16
32
64
1
2
4
8
16
32
1
2
4
8
16
1
2
4
8
1
2
4
1
2
4
8
16
32
64
128
256
512
256
128
64
32
16
8
1
2
3
4
5
6
7
8
9
10
Figure 4: A path with treewidth O(n).
For a pruning edge set EP as in Prop. 4.9, or yielding a path below it, the BP runs in quadratic time
O(n(n + 1)/2) = O(n2).
4.5
Empirical veriﬁcation
On a set of sixteen protein instances from the Protein Data Bank (PDB), twelve satisfy Prop. 4.7, and four
Prop. 4.8, all with v0 = 4. This is consistent with the computational insight [5] that BP has polynomial
complexity on real proteins.
5
Conclusion
We exploit some geometrical properties of an NP-hard distance geometry problem with a speciﬁc vertex
order to derive some polynomial cases. Empirically, proteins backbones seem to fall in these cases; this
provides an explanation for the practical eﬃciency of a well-known embedding algorithm called Branch-
and-Prune.


## Page 9


REFERENCES
9
References
[1] L. Blumenthal. Theory and Applications of Distance Geometry. Oxford University Press, Oxford,
1953.
[2] G.M. Crippen and T.F. Havel. Distance Geometry and Molecular Conformation. Wiley, New York,
1988.
[3] Q. Dong and Z. Wu. A geometric build-up algorithm for solving the molecular distance geometry
problem with sparse distance data. Journal of Global Optimization, 26:321–333, 2003.
[4] T. Eren, D.K. Goldenberg, W. Whiteley, Y.R. Yang, A.S. Morse, B.D.O. Anderson, and P.N. Bel-
humeur. Rigidity, computation, and randomization in network localization. IEEE Infocom Proceed-
ings, pages 2673–2684, 2004.
[5] C. Lavor, L. Liberti, N. Maculan, and A. Mucherino. The discretizable molecular distance geometry
problem. Computational Optimization and Applications, in revision.
[6] C. Lavor, L. Liberti, N. Maculan, and A. Mucherino. Recent advances on the discretizable molecular
distance geometry problem. European Journal of Operational Research, submitted (invited survey).
[7] C. Lavor, A. Mucherino, L. Liberti, and N. Maculan. On the solution of molecular distance geom-
etry problems with interval data. In Proceedings of the International Workshop on Computational
Proteomics, Hong Kong, 2010. IEEE.
[8] C. Lavor, A. Mucherino, L. Liberti, and N. Maculan. On the computation of protein backbones by
using artiﬁcial backbones of hydrogens. Journal of Global Optimization, accepted.
[9] L. Liberti, C. Lavor, and N. Maculan. A branch-and-prune algorithm for the molecular distance
geometry problem. International Transactions in Operational Research, 15:1–17, 2008.
[10] L. Liberti, C. Lavor, A. Mucherino, and N. Maculan. Molecular distance geometry methods: from
continuous to discrete. International Transactions in Operational Research, 18:33–51, 2010.
[11] L. Liberti, B. Masson, C. Lavor, J. Lee, and A. Mucherino. On the number of solutions of the
discretizable molecular distance geometry problem. Technical Report 1010.1834v1[cs.DM], arXiv,
2010.
[12] J.J. Mor´e and Z. Wu.
Global continuation for distance geometry problems.
SIAM Journal of
Optimization, 7(3):814–846, 1997.
[13] A. Mucherino, C. Lavor, and L. Liberti. The discretizable distance geometry problem. Optimization
Letters, in revision.
[14] A. Mucherino, C. Lavor, L. Liberti, and E-G. Talbi.
A parallel version of the branch & prune
algorithm for the molecular distance geometry problem. In ACS/IEEE International Conference
on Computer Systems and Applications (AICCSA10), Hammamet, Tunisia, 2010. IEEE conference
proceedings.
[15] A. Mucherino, L. Liberti, and C. Lavor.
MD-jeep: an implementation of a branch-and-prune
algorithm for distance geometry problems.
In K. Fukuda, J. van der Hoeven, M. Joswig, and
N. Takayama, editors, Mathematical Software, volume 6327 of LNCS, pages 186–197, New York,
2010. Springer.
[16] J.B. Saxe. Embeddability of weighted graphs in k-space is strongly NP-hard. Proceedings of 17th
Allerton Conference in Communications, Control and Computing, pages 480–489, 1979.
[17] T. Schlick. Molecular modelling and simulation: an interdisciplinary guide. Springer, New York,
2002.


## Page 10


0
2
2
2
2
2
4
4
4
4
4
8
8
8
8
16
16
16
32
32
64


## Page 11


4
8
16
32
64
2
2
4
8
16
32
2
4
8
16
2
4
8
2
4
2


## Page 12


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
r
r
r
r
b
b
g

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
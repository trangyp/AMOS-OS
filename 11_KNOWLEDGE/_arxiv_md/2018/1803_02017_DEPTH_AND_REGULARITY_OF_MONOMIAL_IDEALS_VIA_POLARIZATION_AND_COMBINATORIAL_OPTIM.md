---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1803.02017
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1803.02017_Depth_and_regularity_of_monomial_ideals_via_polarization_and_combinatorial_optim

> Source: 1803.02017_Depth_and_regularity_of_monomial_ideals_via_polarization_and_combinatorial_optim.pdf

> Pages: 24

---


## Page 1


arXiv:1803.02017v2  [math.AC]  18 Oct 2018
DEPTH AND REGULARITY OF MONOMIAL IDEALS VIA
POLARIZATION AND COMBINATORIAL OPTIMIZATION
JOS´E MART´INEZ-BERNAL, SUSAN MOREY, RAFAEL H. VILLARREAL, AND CARLOS E. VIVARES
Abstract. In this paper we use polarization to study the behavior of the depth and regularity
of a monomial ideal I, locally at a variable xi, when we lower the degree of all the highest
powers of the variable xi occurring in the minimal generating set of I, and examine the depth
and regularity of powers of edge ideals of clutters using combinatorial optimization techniques.
If I is the edge ideal of an unmixed clutter with the max-ﬂow min-cut property, we show that
the powers of I have non-increasing depth and non-decreasing regularity. In particular edge
ideals of unmixed bipartite graphs have non-decreasing regularity. We are able to show that
the symbolic powers of the ideal of covers of the clique clutter of a strongly perfect graph have
non-increasing depth. A similar result holds for the ideal of covers of a uniform ideal clutter.
1. Introduction
Let R = K[x1, . . . , xn] be a polynomial ring over a ﬁeld K, let f be a monomial of R, and let
I ⊂R be a monomial ideal. The following two inequalities were shown in [3, Theorem 3.1]:
(A) depth(R/(I : f)) ≥depth(R/I),
(B) reg(R/I) ≥reg(R/(I : f)),
where depth(R/I) and reg(R/I) are the depth and regularity of the quotient ring R/I and
(I : f) = {g ∈R|gf ∈I} is referred to as a colon ideal. If I and f are squarefree, we show that
(A) and (B) are equivalent using a duality theorem of Terai [58] (Theorem 2.7) and some duality
formulas for edge ideals of clutters (Lemma 2.6), that is, (A) and (B) are dual statements in the
squarefree case (Proposition 2.8).
We introduce a formula expressing depth(R/(I, f))−depth(R/I), reg(R/I) and reg(R/(f, I))
in terms of the depth and regularity of polarizations (Proposition 2.11). Then, as an application,
we give an alternate proof of (A) and (B), and show some other known inequalities about depth
and regularity (Corollary 2.12). If in≺(I +f) = I +in≺(f) for some monomial order ≺and some
homogeneous polynomial f, we show that (A) and (B) hold (Corollary 2.13).
The aim of this paper is to use these results to study the behavior of the depth and regularity
of R/I, locally at a variable xi, when we lower the degree of all the highest powers of the
variable xi occurring in the minimal generating set of I and, furthermore, to examine the depth
and regularity of powers and symbolic powers of edge ideals of clutters and graphs, and their
ideals of covers, using combinatorial optimization techniques.
Fix a variable xi that occurs in the minimal generating set G(I) of I. Let q be the maximum
of the degrees in xi of the monomials of G(I), let Bi be the set of all monomials of G(I) of
2010 Mathematics Subject Classiﬁcation. Primary 13F20; Secondary 05C22, 05E40, 13H10.
Key words and phrases. Depth, regularity, max-ﬂow min-cut, clutter, edge ideal, monomial ideal, polarization.
The ﬁrst and third authors were partially supported by SNI. The fourth author was supported by a scholarship
from CONACYT.
1


## Page 2


2
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
degree q in xi, let p be the maximum of the degrees in xi of the monomials of Ai = G(I) \ Bi,
and consider the ideal L = ({xa/xi| xa ∈Bi} ∪Ai}).
One of our main results shows that the depth is locally non-decreasing at each variable xi
when lowering the top degree.
Note that if p = 0, that is, if all generators of I that are
divisible by xi have degree q in xi, then L = (I : xi). Thus when p = 0 we have from (A)
that depth(R/L) = depth(R/(I : xi)) ≥depth(R/I). This theorem allow control over the depth
when the degrees in xi of the generators varies.
Theorem 3.1 (a) If p ≥1 and q −p ≥2, then depth(R/I) = depth(R/L).
(b) If p ≥0 and q −p = 1, then depth(R/L) ≥depth(R/I).
(c) If p = 0 and q ≥2, then depth(R/I) = depth(R/({xa/xq−1
i
| xa ∈Bi} ∪Ai})).
There are similar results for regularity (Theorem 3.7). As a consequence one recovers a result
of Herzog, Takayama and Terai [32] showing that depth(R/rad(I)) ≥depth(R/I) and a result of
Ravi [46] showing that reg(R/rad(I)) ≤reg(R/I) (Corollaries 3.3 and 3.8). The result can also
be used to show that the Cohen–Macaulay property of a vertex-weighted digraph is dependent
only on knowing which vertices have weight greater than one and not on the actual weights used
(Corollary 3.2).
There are some classes of monomial ideals whose powers have non-increasing depth and non-
decreasing regularity [3, 5, 26, 27, 52, 54]. A natural way to show these properties for a monomial
ideal I is to prove the existence of a monomial f such that (Ik+1 : f) = Ik for k ≥1. This was
exploited in [3, 43] and in [24, Corollary 3.11] in connection to normally torsion-free ideals.
Since any squarefree monomial ideal is the edge ideal I(C) of a clutter C, we will study the
depth and regularity of powers and symbolic powers of edge ideals of clutters and graphs–and
their ideals of covers—that have nice combinatorial optimization properties (e.g., max-ﬂow min-
cut, ideal, uniform, and unmixed clutters, strongly perfect and very well-covered graphs). The
k-th symbolic power of an ideal I is denoted by I(k) (Deﬁnition 4.2). The ideal of covers of a
clutter C, denoted I(C)∨, is the edge ideal of C∨, the clutter of minimal vertex covers of C.
If I(C) is the edge ideal of a clutter C which has a good leaf, then the powers of I(C) have
non-increasing depth and non-decreasing regularity [3, Theorem 5.1]. In particular edge ideals
of forests or simplicial trees have these properties. Our next result gives a wide family of ideals
with these properties.
Theorem 4.9 If I = I(C) is the edge ideal of an unmixed clutter C with the max-ﬂow min-cut
property, then
(a) depth(R/Ik) ≥depth(R/Ik+1) for k ≥1, and
(b) reg(R/Ik) ≤reg(R/Ik+1) for k ≥1.
Let G be a graph with vertex set V (G) = {x1, . . . , xn} and edge set E(G). A result of T. N.
Trung [61] shows that for k ≫0 one has
depth(R/I(G)k) = |isol(G)| + c0(G),
where isol(G) is the set of isolated vertices of G and c0(G) is the number of non-trivial bipartite
components of G. We complement this fact by observing that dim(R) −ℓ(I(G)) is equal to
|isol(G)| + c0(G), where ℓ(I(G)) is the analytic spread of I(G), and by showing the inequality
depth(R/(I(G)k : xk
i )) ≤depth(R/(I(G \ NG(xi))k, NG(xi)))
for k ≥1 and i = 1, . . . , n (Proposition 5.1), where NG(xi) is the neighbor set of xi. For k = 1
this inequality follows from the fact that (I(G): xi) is equal to (I(G \ NG(xi)), NG(xi)) [66, p.


## Page 3


DEPTH AND REGULARITY OF MONOMIAL IDEALS
3
293] and using the inequality depth(R/(I(G): xi)) ≥depth(R/I(G)). The general case follows
by successively applying Theorem 3.1 locally at each variable.
It is an open problem whether or not the powers of the edge ideal of a graph have non-
increasing depth. To the best of our knowledge this is open even for bipartite graphs. Our
next application extends the fact that the powers of I(G)∨, the ideal of covers of G, have
non-increasing depth if G is bipartite [5, 26, 27].
Corollary 5.3 Let G be a bipartite graph. The following hold.
(a) [39, Corollary 5.3] If G is unmixed, then I(G) has non-increasing depth.
(b) ([5, Theorem 3.2], [26], [27, Corollary 2.4]) I(G)∨has non-increasing depth.
(c) I(G)∨has non-decreasing regularity.
An interesting example due to Kaiser, Stehl´ık, and ˇSkrekovski [38] shows that the powers of
the ideal of covers of a graph does not always have non-increasing depth (Example 5.4), that is,
part (b) of Corollary 5.3 fails for non-bipartite graphs. A nice result of L. T. Hoa, K. Kimura, N.
Terai and T. N. Trung [33, Theorem 3.2] shows that the symbolic powers of the ideal of covers
of a graph have non-increasing depth. A similar result holds for the ideal of covers of a uniform
ideal clutter (Corollary 4.10).
If G is a very well-covered graph, then the depths of symbolic powers of I(G)∨form a non-
increasing sequence [52] (cf. [33, Theorem 3.2]) and also the depths of symbolic powers of I(G)
form a non-increasing sequence [39, Theorem 5.2]. In this case we show that the symbolic powers
of I(G) have non-decreasing regularity (Proposition 5.6).
We will give another family of squarefree monomial ideals whose symbolic powers have non-
increasing depth and non-decreasing regularity. A clique of a graph G is a set of vertices inducing
a complete subgraph. The clique clutter of G, denoted by cl(G), is the clutter on V (G) whose
edges are the maximal cliques of G.
Proposition 5.8 Let G be a strongly perfect graph and let cl(G) be its clique clutter. If J is the
ideal of covers of cl(G), then
(a) depth(R/J(k)) ≥depth(R/J(k+1)) for k ≥1, and
(b) reg(R/J(k)) ≤depth(R/J(k+1)) for k ≥1.
Bipartite graphs, chordal graphs, comparability graphs, and Meyniel graphs are strongly
perfect (see [47] and the references therein). Thus this result generalizes Corollary 5.3(b) because
if G is a bipartite graph, then cl(G) = G and I(G∨)(k) = I(G∨)k for k ≥1 [18].
For edge ideals of clutters the Cohen–Macaulay property of its k-th ordinary or symbolic
power is well understood if k ≥3. By a result of N. Terai and N. V. Trung [59], if I(C) is the
edge ideal of a clutter C, then I(C)k (resp. I(C)(k)) is Cohen–Macaulay for some k ≥3 if and
only if I(C) is a complete intersection (resp. the independence complex ∆C of C is a matroid).
The case when G is a graph and k = 2 is treated in [7, 35, 36, 60]. The Cohen–Macaulay
property of the square of an edge ideal can be expressed in terms of its connected components
[25, 48] (Corollary 5.10). Edge ideals of graphs whose square is Cohen–Macaulay have a rich
combinatorial structure and have been classiﬁed combinatorially by D. T. Hoang, N. C. Minh
and T. N. Trung [35, 36]. The Cohen-Macaulay property of I(G)2 is also studied in [60] in terms
of simplicial complexes.
As an application we recover the following fact.
Corollary 5.14 ([7, Theorem 2.7], [35, Proposition 4.2])
Let G be a bipartite graph without
isolated vertices. Then I(G)2 is Cohen-Macaulay if and only if G is a disjoint union of edges.


## Page 4


4
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
For all unexplained terminology and additional information we refer to [11, 42] (for com-
mutative algebra), [6, 50, 51] (for combinatorial optimization), [28] (for graph theory), and
[15, 21, 31, 62, 66] (for the theory of powers of edge ideals of clutters and monomial ideals).
2. Depth and regularity of monomial ideals via polarization
Let R = K[x1, . . . , xn] be a polynomial ring over a ﬁeld K and let I be a monomial ideal. The
unique minimal set of generators of I consisting of monomials is denoted by G(I). The goal of
this section is to use polarization to control the depth and regularity of R/I when the powers
of a variable appearing in G(I) are reduced. To do so, we ﬁrst recall some known results, then
show a series of equivalent conditions that will allow us to study the behavior of the depth and
the regularity of R/I.
In [9, Lemma 5.1] it was shown that depth(R/(I : xi)) ≥depth(R/I) for all i. By noting
that a generating set for (I : xi) can be found from G(I) by reducing all powers of xi by one,
this can be viewed as the ﬁrst step in reaching the goal. The result was recently generalized in
[3, Theorem 3.1] to any monomial ideal. We provide an alternate proof using polarization. We
begin by treating the squarefree case using Stanley-Reisner complexes.
Recall that if ∆is a simplicial complex with vertices x1, . . . , xn, the Stanley-Reisner ideal
of ∆, denoted by I∆, is the ideal of R whose squarefree monomial generators correspond to
non-faces of ∆. That is,
I∆= (xi1 · · · xit|{xi1, . . . , xit} ̸∈∆).
The following result shows how the structure of the simplicial complex can be used to ﬁnd
the depth of the associated ideal.
Theorem 2.1. [56] Let ∆be a simplicial complex with vertex set V = {x1, . . . , xn}, let I∆be
its Stanley–Reisner ideal, and K[∆] = R/I∆. Then
depth(R/I∆) = 1 + max{i | K[∆i] is Cohen–Macaulay},
where ∆i = {F ∈∆| dim(F) ≤i} is the i-skeleton and −1 ≤i ≤dim(∆).
The star of a face σ in a simplicial complex ∆, denoted star∆(σ), is deﬁned to be the sub-
complex of ∆generated by all facets of ∆that contain σ.
Lemma 2.2. [3, Theorem 3.1] Let I ⊂R be a squarefree monomial ideal and let f be a squarefree
monomial. Then depth(R/(I : f)) ≥depth(R/I).
Proof. Let σ = supp(f) be the set of all variables that occur in f. We may assume that f is
a zero divisor of R/I because otherwise (I : f) = I and there is nothing to prove. We may
also assume that f is not in all minimal primes of I because in this case (I : f) = R and
depth(0) = ∞. Let ∆and ∆′ be the Stanley–Reisner complexes of I and (I : f), respectively.
Setting d = dim(∆), d′ = dim(∆′), one has d′ ≤d. Assume that ∆i is Cohen–Macaulay for
some i ≤d. We claim that i ≤d′. If i > d′, take a facet F of ∆′ of dimension d′, that is, F is a
facet of ∆of dimension d′ containing σ. As F is a face of ∆i and this complex is pure, we get
that F is properly contained in a face of ∆of dimension i, a contradiction. Hence i ≤d′. The
simplicial complex ∆′ is equal to star∆(σ). Therefore, from the equalities
(∆′)i = (star∆(σ))i = star∆i(σ),
and using that the star of a face of a Cohen–Macaulay complex is again Cohen–Macaulay [66,
p. 224], we get that (∆′)i is Cohen–Macaulay. Hence, by Theorem 2.1, it follows that the depth
of R/(I : f) is greater than or equal to depth(R/I).
□


## Page 5


DEPTH AND REGULARITY OF MONOMIAL IDEALS
5
A common technique in commutative algebra is to start with a short exact sequence of the
form
0 −→R/(I : f)[−k]
f
−→R/I −→R/(I, f) −→0,
where I ⊂R is a graded ideal and f is a homogeneous polynomial of degree k, and use infor-
mation about two of the terms to glean desired information about the third. Both depth and
regularity are known to behave well relative to short exact sequences. There are several versions
of the depth lemma that appear in the literature. The following lemmas provide the information
relating the depths and regularity of the terms of a short exact sequence in a format that will
be particularly useful in the remainder of this paper.
Lemma 2.3. Let 0 →N →M →L →0 be a short exact sequence of modules over a local ring
R. The following conditions are equivalent.
(a) depth(N) ≥depth(M).
(b) depth(M) = depth(N) or depth(M) = depth(L).
(c) depth(L) ≥depth(M) −1.
Proof. It follows from the depth lemma [66, Lemma 2.3.9].
□
There is a similar statement for the regularity.
Lemma 2.4. Let 0 →N →M →L →0 be a short exact sequence of graded ﬁnitely generated
R-modules. The following conditions are equivalent.
(a) reg(M) ≥reg(N) −1.
(b) reg(M) = reg(N) or reg(M) = reg(L).
(c) reg(M) ≥reg(L).
Proof. It follows from [11, Corollary 20.19].
□
Lemma 2.5. Let 0 →N →M →L →0 be an exact sequence of graded ﬁnitely generated
R-modules with homomorphisms of degree 0 and k ≥1 an integer. The following are equivalent.
(a) reg(N) ≤reg(M) + k.
(b) reg(L) ≤reg(M) + k −1.
Proof. (a) ⇒(b): We may assume reg(M) ≤reg(L) −1, otherwise there is nothing to prove.
Hence, by [11, Corollary 20.19], we get
reg(L) ≤max(reg(N) −1, reg(M)) ≤reg(M) + k −1.
(b) ⇒(a): As reg(L) + 1 ≤reg(M) + k, by [11, Corollary 20.19], we get
reg(N) ≤max(reg(M), reg(L) + 1) ≤reg(M) + k.
✷
Let C be a clutter with vertex set X = {x1, . . . , xn}, that is, C consists of a family of subsets
of X, called edges, none of which is included in another. The sets of vertices and edges of C are
denoted by V (C) and E(C), respectively. If V ⊂X, the clutter obtained from C by deleting all
edges of C that intersect V will be denoted by C \ V . The edge ideal of C, denoted I(C), is the
ideal of R generated by all squarefree monomials xe = Q
xi∈e xi such that e ∈E(C). The ideal of
covers I(C)∨of C is the edge ideal of C∨, the clutter of minimal vertex covers of C [66, p. 221].
The ideal I(C)∨is also called the Alexander dual of I(C) or simply the cover ideal of C.
Lemma 2.6. Let I(C) ⊂R be the edge ideal of a clutter C and let f = xi1 · · · xik be a squarefree
monomial of R. The following hold.


## Page 6


6
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
(i) (I(C)∨: f)∨= I(C \ {xi1, . . . , xik}).
(ii) (I(C): f)∨= I(C∨\ {xi1, . . . , xik}).
(iii) If xi is a variable, then (I(C), xi)∨= xiI(C \ {xi})∨.
Proof. (i): Let E(C) be the set of edges of C. We set V = {xi1, . . . , xik} and I = I(C). Then
(I∨: f)∨=

\
e∈E(C)
(e): f


∨
=


\
e∈E(C\V )
(e)


∨
= (I(C \ V )∨)∨= I(C \ V ).
(ii): Notice the equalities I(C∨)∨= (I(C)∨)∨= I(C).
Thus this part follows from (i) by
replacing C with C∨.
(iii): Setting L = (I(C), xi) and J = I(C \ {xi}), it follows readily that
L = (I(C \ {xi}), xi) = (J, xi) =
\
p∈Ass(R/J)
(xi, p).
Hence, by duality [66, Theorem 6.3.39], one has (I(C), xi)∨= xiI(C \ {xi})∨.
□
Our interest in the duality results above is partially motivated by the following result relating
regularity and projective dimension, and thus depth, when passing to the dual.
Theorem 2.7. (Terai [58]) If I ⊂R is a squarefree monomial ideal, then
reg(I) = 1 + reg(R/I) = pd(R/I∨).
In [3, Theorem 3.1] it is shown that conditions (ii) and (iv) of the next result hold (cf. [9,
Lemmas 5.1 and 2.10]). For squarefree monomial ideals—using the above duality theorem of
Terai [58]—we show that these conditions are in fact equivalent (cf. Remark 2.9). Roughly
speaking the inequalities of (ii) and (iv) are dual of each other via the duality theorem of Terai.
Proposition 2.8. Let I ⊂R be a squarefree monomial ideal and let f = xi1 · · · xik be a squarefree
monomial of R of degree k. Then any of the following equivalent conditions hold.
(i) depth(R/(f, I)) ≥depth(R/I) −1.
(ii) [3, Theorem 3.1] depth(R/I) ≤depth(R/(I : f)).
(iii) depth(R/(xi1, . . . , xik, I)) ≥depth(R/I) −k.
(iv) [3, Theorem 3.1] reg(R/I) ≥reg(R/(I : f)).
(v) reg(R/(f, I)) ≤reg(R/I) + k −1.
Proof. By Lemma 2.2, condition (ii) holds for any squarefree monomial ideal I and for any
squarefree monomial f. Thus it suﬃces to show that (i) and (ii) are equivalent and that (i) and
(iii)–(v) are equivalent conditions. Since I is squarefree, there is a clutter C such that I = I(C).
(i) ⇔(ii): This follows from applying Lemma 2.3 to the short exact sequence
(2.1)
0 −→R/(I : f)[−k]
f
−→R/I −→R/(I, f) −→0.
(i) ⇒(iii): This follows directly by induction on k.
(iii) ⇒(iv): As (iii) holds for squarefree monomials, applying (iii) to I(C∨), we get
k + depth(R/(xi1, . . . , xik, I(C∨))) ≥depth(R/I(C∨)).
Therefore, setting V = {xi1, . . . , xik} and X = {x1, . . . , xn}, we get
depth(R/I(C∨\ V ))
=
k + depth(K[X \ V ]/I(C∨\ V ))
=
k + depth(R/(V, I(C∨))) ≥depth(R/I(C∨)),


## Page 7


DEPTH AND REGULARITY OF MONOMIAL IDEALS
7
that is, depth(R/I(C∨\ V )) ≥depth(R/I(C∨)), where I(C∨) = I(C)∨. Hence, applying the
Auslander–Buchsbaum formula [66, Theorem 3.5.13] to both sides of this inequality and then
using Terai’s formula of Theorem 2.7, we get
reg(R/I(C)) ≥reg(R/I(C∨\ V )∨).
By Lemma 2.6(ii) one has I(C∨\ V ) = (I(C): f)∨. Thus, by duality, I(C∨\ V )∨= (I(C): f),
and the required inequality follows.
(iv) ⇒(iii): As (iv) holds for squarefree monomials, applying (iv) to I(C∨), we get
reg(R/I(C∨)) ≥reg(R/(I(C∨): f)).
Therefore, applying Terai’s formula of Theorem 2.7 and Lemma 2.6(i), we get
pdR(R/I(C)) ≥pdR(R/I(C \ V )).
Hence, applying the Auslander–Buchsbaum formula [66, Theorem 3.5.13] to both sides of this
inequality and using depth properties, we obtain
k + depth(R/(V, I(C)))
=
k + depth(K[X \ V ]/I(C \ V ))
=
depth(R/I(C \ V )) ≥depth(R/I(C)).
(iv) ⇔(v): Since reg((R/(I : f))[−k]) = k + reg(R/(I : f)), the equivalence between (iv) and
(v) follows applying Lemma 2.5 to the exact sequence of Eq. (2.1).
□
In [3, Corollary 3.3] it is shown that condition (vii) below holds (cf. [9, Lemma 2.10]).
Remark 2.9. (A) Conditions (i)–(v) are equivalent to
(vi) depth(R/I) = depth(R/(I : f)) or depth(R/I) = depth(R/(f, I)).
(B) For k = deg(f) = 1 conditions (i)–(vi) are equivalent to:
(vii) reg(R/I) = reg(R/(I : f)) + 1 or reg(R/I) = reg(R/(f, I)).
This follows applying Lemmas 2.3 and 2.4 to the exact sequence given in Eq. (2.1).
Depth and regularity via polarization. In what follows we will use the polarization tech-
nique due to Fr¨oberg that we brieﬂy recall now (see [66, p. 203] and the references therein). Note
that alternate labelings of polarizations and partial polarizations exist in the literature (see, for
example, [14, 31, 45]); however, the notation used here will prove beneﬁcial in Section 3.
Let J ⊂R be a monomial ideal minimally generated by G(J) = {g1, . . . , gs}. We set γi equal
to max{degxi(g)| g ∈G(J)}. To polarize J we use the set of new variables
XJ = ∪n
i=1{xi,2, . . . , xi,γi},
where {xi,2, . . . , xi,γi} is empty if γi = 0 or γi = 1. It is convenient to identify the variable xi
with xi,1 for all i. Recall that a power xci
i of a variable xi, 1 ≤ci ≤γi, polarizes to (xci
i )pol = xi
if γi = 1, to (xci
i )pol = xi,2 · · · xi,ci+1 if ci < γi, and to (xci
i )pol = xi,2 · · · xi,γixi if ci = γi. This
induces a polarization gpol
i
of gi for i = 1, . . . , s. The full polarization Jpol of J is the ideal of
R[XJ] generated by gpol
1 , . . . , gpol
s . The next lemma is well known.
Lemma 2.10. Let J be a monomial ideal of R. Then
(a) (Fr¨oberg [16]) depth(R[XJ]/Jpol) = |XJ| + depth(R/J) = depth(R[XJ]/J).
(b) pd(R/J) = pd(R[XJ]/Jpol).
(c) pd(R/J) = reg(R[XJ]/(Jpol)∨) + 1.
(d) [31, Corollary 1.6.3] reg(R/J) = reg(R[XJ]/Jpol).


## Page 8


8
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
Proof. Part (b) follows applying the Auslander–Buchsbaum formula [66, Theorem 3.5.13] to part
(a). Part (c) follows from Theorem 2.7 and part (b).
□
Let I ⊂R be a monomial ideal and let f be a monomial. Using polarization, one can extend
Proposition 2.8 and Remark 2.9 to general monomial ideals. The following result will be needed
when relating the depth and the regularity of a monomial ring R/I with those of the ring
R[XL]/Ipol, where L is the ideal (f, I) and Ipol is the polarization of I with respect to R[XL]
(cf. Lemma 2.10).
Proposition 2.11. Let I ⊂R be a monomial ideal and let f be a monomial. If L = (f, I) and
XL is the set of new variables that are needed to polarize L, then
(i) depth(R[XL]/Lpol) −depth(R[XL]/(f pol
1
, . . . , f pol
r
)) = depth(R/L) −depth(R/I),
(ii) reg(R[XL]/Lpol) = reg(R/L) and reg(R[XL]/(f pol
1
, . . . , f pol
r
)) = reg(R/I),
where G(I) = {f1, . . . , fr}, and f pol
i
is the polarization of fi in R[XL].
Proof. (i): We may assume f is not in I, otherwise there is nothing to prove. Let Lpol ⊂R[XL] be
the full polarization of L. For use below we set δi = max{degi(g)| g ∈G(I)} and f = xa1
1 · · · xan
n .
The set of variables of R is denoted by X = {x1, . . . , xn}.
Subcase (i.a): ai > δi for some i. Then G(L) = {f, f1, . . . , fr}. For simplicity of notation we
assume there is an integer k such that a1 > δ1, . . . , ak > δk and ai ≤δi for i > k. If δi = 0 for
some i > k, then the variable xi does not occur in any element of G(L) because ai = 0. Hence
we can replace R by K[X \ {xi}]. Thus we may assume that δi ≥1 for i > k. To polarize L we
use the set of variables
XL = (∪k
i=1{xi,2, . . . , xi,δi, xi,δi+1, . . . , xi,ai}) ∪(∪n
i=k+1{xi,2, . . . , xi,δi}),
where {xi,2, . . . , xi,c} is the empty set if c = 0 or c = 1. It is convenient to identify xi with xi,1
for all i. In this setting the monomial xai
i
polarizes to (xai
i )pol = xi,2 · · · xi,aixi for i = 1, . . . , k
and the monomial xδi
i polarizes to (xδi
i )pol = xi,2 · · · xi,δixi for i > k. Let f pol and f pol
i
be the
polarizations in R[XL] of f and fi (see Example 2.14). By Lemma 2.10 one has
(2.2)
depth(R[XL]/Lpol) = |XL| + depth(R/L) =
k
X
i=1
(ai −1) +
n
X
i=k+1
(δi −1) + depth(R/L).
Next we relate the depth of R[XL]/(f pol
1
, . . . , f pol
r
)) to the depth of R/I. For this consider
the polynomial ring R′ = K[X′], where X′ = (X \ {xi}k
i=1) ∪{x1,δi+1}k
i=1, and let f ′
i be the
polynomial of R′ obtained from fi by replacing xi with xi,δi+1 for i = 1, . . . , k. If I′ is the ideal
of R′ generated by f ′
1, . . . , f ′
r, then K[X]/I and K[X′]/I′ are isomorphic and have the same
depth. By polarizing f ′
i with respect to
XI′ = ∪n
i=1{xi,2, . . . , xi,δi}
we obtain that (f ′
i)pol is equal to f pol
i
, the polarization of fi with respect to XL.
The full
polarization of I′ is (I′)pol = ((f ′
1)pol, . . . , (f ′
r)pol). Therefore, by Lemma 2.10, one has
depth(R[XL]/(f pol
1
, . . . , f pol
r
))
=
depth(R[XL]/((f ′
1)pol, . . . , (f ′
r)pol)),
(2.3)
depth(R′[XI′]/((f ′
1)pol, . . . , (f ′
r)pol))
=
|XI′| + depth(R′/I′) = |XI′| + depth(R/I).
(2.4)


## Page 9


DEPTH AND REGULARITY OF MONOMIAL IDEALS
9
As |X ∪XL| = Pk
i=1 ai + Pn
i=k+1 δi and |X′ ∪XI′| = Pn
i=1 δi, we get
|(X ∪XL) \ (X′ ∪XI′)| =
k
X
i=1
(ai −δi),
that is, the number of variables of R[XL] that do not occur in R′[XI′] is Pk
i=1(ai−δi). Therefore
from Eqs. (2.3) and (2.4), and using that |XI′| = Pn
i=1(δi −1), we get
depth(R[XL]/(f pol
1
, . . . , f pol
r
))
=
k
X
i=1
(ai −δi) + depth(R′[XI′]/((f ′
1)pol, . . . , (f ′
r)pol))
=
k
X
i=1
(ai −1) +
n
X
i=k+1
(δi −1) + depth(R/I).
(2.5)
Using Eqs. (2.2) and (2.5) the required equality follows.
Subcase (i.b): ai ≤δi for all i. This case follows adapting the arguments of Subcase (i.a),
noting that k = 0 in this case.
(ii): To prove this part we keep the notation of part (i).
Subcase (ii.a): Assume that ai > δi for some i.
The ﬁrst equality follows at once from
Lemma 2.10. As R′[XI′] is a subring of R[XL], the regularity of (I′)polR′[XI′] is equal to that
of (I′)polR[XL]. Hence, by Lemma 2.10, we get
reg(R[XL]/(I′)pol) = reg(R′[XI′]/(I′)pol) = reg(R′/I′) = reg(R/I).
Subcase (ii.b): ai ≤δi for all i. This case follows adapting the arguments of Subcase (ii.a).
□
The following corollary extends Proposition 2.8 and Remark 2.9 from squarefree monomial
ideals to arbitrary monomial ideals using polarization. It will be used throughout the paper
(e.g., Lemma 3.6, Theorem 4.9, Proposition 5.6). This result is later extended using Gr¨obner
bases (Corollary 2.13).
Corollary 2.12. Let I ⊂R be a monomial ideal, let f be a monomial of degree k, and let
xi1, . . . , xik be a set of distinct variables of R. The following hold.
(i) depth(R/(f, I)) ≥depth(R/I) −1.
(ii) [3, Theorem 3.1] depth(R/I) ≤depth(R/(I : f)).
(iii) depth(R/(xi1, . . . , xik, I)) ≥depth(R/I) −k.
(iv) [3, Theorem 3.1] reg(R/I) ≥reg(R/(I : f)).
(v) reg(R/(f, I)) ≤reg(R/I) + k −1.
(vi) depth(R/I) = depth(R/(I : f)) or depth(R/I) = depth(R/(f, I)).
(vii) [3, 9] If k = 1, then reg(R/I) = reg(R/(I : f)) + 1 or reg(R/I) = reg(R/(f, I)).
Proof. If I and f are squarefree, the result holds true. Indeed, by Lemma 2.2, one has the
inequality depth(R/(I : f)) ≥depth(R/I). Then by Proposition 2.8 and Remark 2.9 the state-
ments all hold. To show the general case we will use the polarization technique.
(i) One may assume that f /∈I. We set G(I) = {f1, . . . , fr} and L = (f, I). Let XL be the
set of new variables needed to polarize L and let f pol, f pol
i
be the polarizations in R[XL] of f,
fi, respectively. As these polarizations are squarefree, by Proposition 2.8 one has
depth(R[XL]/(f pol, f pol
1
, . . . , f pol
r
)) ≥depth(R[XL]/(f pol
1
, . . . , f pol
r
)) −1,
where Lpol = (f pol, f pol
1
, . . . , f pol
r
). Hence, by Proposition 2.11, depth(R/L) ≥depth(R/I) −1.


## Page 10


10
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
(ii): According to Lemma 2.3 parts (ii) and (i) are equivalent.
(iii): It follows from part (i) using induction on k.
(iv)–(v): Setting N = (R/(I : f))[−k], M = R/I and L = R/(I, f), and noticing that
reg(N) = k + reg(R/(I : f)), from Lemma 2.5 it follows that (iv) and (v) are equivalent. Since
f pol, f pol
1
, . . . , f pol
r
are squarefree, by Proposition 2.8 one has
reg(R[XL]/Lpol) −reg(R[XL]/(f pol
1
, . . . , f pol
r
)) ≤k −1.
Hence, by Proposition 2.11, one has reg(R/L) −reg(R/I) ≤k −1. Thus (v) and (iv) hold.
(vi): This condition is equivalent to (i).
This follows applying Lemma 2.3 to the exact
sequence
0 −→R/(I : f)[−k]
f
−→R/I −→R/(I, f) −→0.
(vii): Recall that reg(R/(I : f))[−k] = k+reg(R/(I : f)). If k = 1, using Lemma 2.4 it follows
that conditions (vii) and (iv) are equivalent.
□
Corollary 2.13. Let I ⊂R be a monomial ideal and let f be a homogeneous polynomial of
degree k. If there exists a monomial order ≺on R such that in≺(I, f) = I + (in≺(f)), then
(a) depth(R/(I : f)) ≥depth(R/I),
(b) reg(R/(I, f)) ≤reg(R/I) + k −1, and
(c) reg(R/I) ≥reg(R/(I : f)).
Proof. (a): We proceed by contradiction assuming that depth(R/I) > depth(R/(I : f)). From
the exact sequence
0 −→R/(I : f)[−k]
f
−→R/I −→R/(I, f) −→0,
using the depth lemma [66, Lemma 2.3.9] and the fact that the depth of R/(I, f) is greater than
or equal to the depth of R/in≺(I, f) [31, Theorem 3.3.4(d)], we get
depth(R/(I : f)) = depth(R/(I, f)) + 1 ≥depth(R/(I + in≺(f))) + 1.
By Corollary 2.12(i), we have depth(R/(I + in≺(f))) ≥depth(R/I) −1. Hence we obtain
depth(R/(I : f)) ≥depth(R/I), a contradiction.
(b): Using that the regularity of R/(I, f) is less than or equal to the regularity of R/in≺(I, f)
[31, Theorem 3.3.4(c)] and Corollary 2.12(v), we get
reg(R/(I, f)) ≤reg(R/in≺(I, f)) = reg(R/(I + in≺(f))) ≤reg(R/I) + k −1.
(c): Setting N = R/(I : f)[−k], M = R/I, and L = R/(I, f), we proceed by contradiction
assuming reg(R/(I : f)) > reg(R/I), that is, reg(N) ≥reg(M) + k + 1. On the other hand, by
part (b), one has reg(L) ≤reg(N) −2. According to [11, Corollary 20.19](a), one has either
reg(N) ≤reg(M) or reg(N) ≤reg(L) + 1, a contradiction.
□
The next example illustrates the polarizations used in the proof of Proposition 2.11. For
convenience we use the notation of that proof.
Example 2.14. Let f = x3
1x3
2, f1 = x2
1x3, f2 = x1x2
3, f3 = x2
2x3 be monomials in the polynomial
ring R = K[x1, x2, x3] and set I = (f1, f2, f3) and L = (f, I). Setting
f pol = x1,2x1,3x1x2,2x2,3x2, f pol
1
= x1,2x1,3x3,2, f pol
2
= x1,2x3,2x3, f pol
3
= x2,2x2,3x3,2,
and XL = {x1,2, x1,3} ∪{x2,2, x2,3} ∪{x3,2}, the full polarization of L is
Lpol = (f pol, f pol
1
, f pol
2
, f pol
3
) ⊂R[XL].


## Page 11


DEPTH AND REGULARITY OF MONOMIAL IDEALS
11
Making the change of variables x1 →x1,3, x2 →x2,3 in I and setting
f ′
1 = x2
1,3x3, f ′
2 = x1,3x2
3, f ′
3 = x2
2,3x3, I′ = (f ′
1, f ′
2, f ′
3),
XI′ = {x1,2} ∪{x2,2} ∪{x3,2}, R′ = K[x1,3, x2,3, x3], the full polarization of I′ is
(I′)pol = ((f ′
1)pol, (f ′
2)pol, (f ′
3)pol) ⊂R′[XI′],
where (f ′
1)pol = x1,2x1,3x3,2, (f ′
2)pol = x1,2x3,2x3, (f ′
3)pol = x2,2x2,3x3,2. Thus f pol
i
is equal to
(f ′
i)pol for i = 1, 2, 3. Setting XI = {x1,2, x2,2, x3,2} the full polarization of I is generated by the
monomials x1,2x1x3,2, x1,2x3,2x3, x2,2x2x3,2.
3. Depth and regularity locally at each variable
In this section we use polarization to study the behavior of the depth and regularity of a
monomial ideal locally at each variable when lowering the top degree.
Let R = K[x1, . . . , xn] be a polynomial ring over a ﬁeld K, let I be a monomial ideal of R
and let xi be a ﬁxed variable that occurs in G(I). Given a monomial xa = xa1
1 · · · xan
n , we set
degxi(xa) = ai. Consider the integer
q := max{degxi(xa)| xa ∈G(I)},
and the corresponding set Bi := {xa| degxi(xa) = q}∩G(I). That is, Bi is the set of all monomial
of G(I) of highest degree in xi. Setting
Ai := {xa| degxi(xa) < q} ∩G(I) = G(I) \ Bi,
p := max{degxi(xa)| xa ∈Ai} and L := ({xa/xi| xa ∈Bi}∪Ai}), we are interested in comparing
the depth (resp. regularity) of R/I with the depth (resp. regularity) of R/L.
One of the main results of this section shows that the depth is locally non-decreasing at each
variable xi when lowering the top degree:
Theorem 3.1. Let I be a monomial ideal of R and let xi be a variable. The following hold.
(a) If p ≥1 and q −p ≥2, then depth(R/I) = depth(R/L).
(b) If p ≥0 and q −p = 1, then depth(R/L) ≥depth(R/I).
(c) If p = 0 and q ≥2, then depth(R/I) = depth(R/({xa/xq−1
i
| xa ∈Bi} ∪Ai})).
Proof. (a): To simplify notation we set i = 1. We may assume that G(I) = {f1, . . . , fr}, where
{f1, . . . , fm} is the set of all elements of G(I) that contain xq
1 and {fm+1, . . . , fs} is the set of
all elements of G(I) that contain some positive power xℓ
1 of x1 for some 1 ≤ℓ< q. Making
a partial polarization of xq
1 with respect to the new variables x1,2, . . . , x1,q−1 [66, p. 203], gives
that fj polarizes to f pol
j
= x1,2 · · · x1,q−1x2
1f ′
j for j = 1, . . . , m, where f ′
1, . . . , f ′
m are monomials
that do not contain x1 and fj = xq
1f ′
j for j = 1, . . . , m. Hence, using that q −p ≥2, one has the
partial polarization
Ipol = (x1,2 · · · x1,q−1x2
1f ′
1, . . . , x1,2 · · · x1,q−1x2
1f ′
m, f pol
m+1, . . . , f pol
s
, fs+1, . . . , fr),
where f pol
m+1, . . . , f pol
s
do not contain x1 and Ipol is an ideal of Rpol = R[x1,2, . . . , x1,q−1]. On the
other hand, from the equality
G(L) = {f1/x1, . . . , fm/x1, fm+1, . . . , fr},
one has the partial polarization
Lpol = (x1,2 · · · x1,q−1x1f ′
1, . . . , x1,2 · · · x1,q−1x1f ′
m, f pol
m+1, . . . , f pol
s
, fs+1, . . . , fr).


## Page 12


12
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
By making the substitution x2
1 →x1 in each element of G(Ipol) this will not aﬀect the depth
of Rpol/Ipol (see [44, Lemmas 3.3 and 3.5]). Thus
q −2 + depth(R/I) = depth(Rpol/Ipol) = depth(Rpol/Lpol) = q −2 + depth(R/L),
and consequently depth(R/I) = depth(R/L).
(b): To simplify notation we set i = 1. Assume p = 0, then q = 1. Note that the ring
R/L is equal to R/(I : x1).
Hence, by Corollary 2.12, its depth is greater than or equal to
depth(R/I). Thus we may assume that p ≥1. We may also assume that G(I) = {f1, . . . , fr},
where f1, . . . , fm is the set of all elements of G(I) that contain xq
1, and fm+1, . . . , ft is the set of
all elements of G(I) that contain xq−1
1
but not xq
1, and ft+1, . . . , fs is the set of all elements of
G(I) that contain some power xℓ
1, with 1 ≤ℓ< q −1, but not xℓ+1
1
. Let R′ be the polynomial
ring K[x1,q, x2, . . . , xn], with x1,q a new variable, and let L′ be the ideal of R′ obtained from L
by making the change of variable x1 →x1,q in each element of G(L). Clearly
depth(R/L) = depth(R′/L′) = depth(R′[x1]/L′) −1.
The partial polarization of I with respect to x1 using the variables x1,2, . . . , x1,q is given by
Ipol = (x1,2 · · · x1,qx1f ′
1, . . . , x1,2 · · · x1,qx1f ′
m,
x1,2 · · · x1,qf ′
m+1, . . . , x1,2 · · · x1,qf ′
t,
f pol
t+1, . . . , f pol
s
, fs+1, . . . , fr),
where f ′
1, . . . , f ′
t, f pol
t+1, . . . , f pol
s
, fs+1, . . . , fr do not contain x1 and Ipol is an ideal of the ring
Rpol = R[x1,2, . . . , x1,q]. Therefore
(Ipol : x1) = (x1,2 · · · x1,qf ′
1, . . . , x1,2 · · · x1,qf ′
m,
x1,2 · · · x1,qf ′
m+1, . . . , x1,2 · · · x1,qf ′
t, f pol
t+1, . . . , f pol
s
, fs+1, . . . , fr).
The following is a generating set for L′, which is not necessarily minimal:
L′ = (xq−1
1,q f ′
1, . . . , xq−1
1,q f ′
m, xq−1
1,q f ′
m+1, . . . , xq−1
1,q f ′
t,
xat+1
1,q f ′
t+1, . . . , xas
1,qf ′
s, fs+1, . . . , fr),
where 1 ≤ai < q −1 for i = t + 1, . . . , s. Hence, it is seen that, (Ipol : x1) is equal to (L′)pol, the
polarization of L′ with respect to the variable x1,q using the variables x1,2, . . . , x1,q−1. Therefore,
using Lemma 2.2, we get
(q −1) + depth(R/L)
=
1 + ((q −2) + depth(R′/L′))
=
1 + depth((R′)pol/(L′)pol) = depth((R′[x1])pol/(L′)pol)
=
depth(Rpol/(L′)pol) = depth(Rpol/(Ipol : x1))
≥
depth(Rpol/Ipol) = (q −1) + depth(R/I).
Thus depth(R/L) ≥depth(R/I).
(c): It suﬃces to notice that by making the substitution xq
i →xi in each element of G(I) this
will not aﬀect the depth of R/I (see [44, Lemmas 3.3 and 3.5]).
□
Let D be a vertex-weighted digraph, that is, D consists of a ﬁnite set V (D) = {x1, . . . , xn} of
vertices, a prescribed collection E(D) of ordered pairs of distinct points called edges or arrows,


## Page 13


DEPTH AND REGULARITY OF MONOMIAL IDEALS
13
and D is endowed with a function d: V (D) →N+, where N+ := {1, 2, . . .}. The weight d(xi) of
xi is denoted simply by di. The edge ideal of D, denoted I(D), is the ideal of R given by
I(D) := (xixdj
j | (xi, xj) ∈E(D)).
Edge ideals of vertex-weighted digraphs occur in the theory of Reed-Muller-type codes as
initial ideals of vanishing ideals of projective spaces over a ﬁnite ﬁeld [23, 41, 57].
Corollary 3.2. [17, Corollary 6] Let I = I(D) be the edge ideal of a vertex-weighted digraph
with vertices x1, . . . , xn and let di be the weight of xi. If U is the digraph obtained from D by
assigning weight 2 to every vertex xi with di ≥2, then I is Cohen–Macaulay if and only if I(U)
is Cohen–Macaulay.
Proof. By applying Theorem 3.1 to each vertex xi of D of weight at least 3, we obtain that the
depth of R/I(D) is equal to the depth of R/I(U). Since I(D) and I(U) have the same height,
then I(D) is Cohen–Macaulay if and only if I(U) is Cohen–Macaulay.
□
Corollary 3.3. [32] If I is a monomial ideal, then depth(R/rad(I)) ≥depth(R/I). In particular
if I is Cohen–Macaulay, then rad(I) is Cohen–Macaulay.
Proof. It follows by applying Theorem 3.1 to every vertex xi as many times as necessary.
□
As a consequence if I is squarefree, then depth(R/I) ≥depth(R/Ik) for all k ≥1.
Remark 3.4. Let L ⊂R be a monomial ideal. If xk
i is in G(L) for some k ≥1, 1 ≤i ≤n and L′
is the ideal of R generated by all elements of G(I) that do not contain xi, then (L, xi) = (L′, xi)
and by a repeated application of Theorem 3.1 one has
depth(R/L) ≤depth(R/(L′, xi)) = depth(R/L′) −1.
Before proving an analog of Theorem 3.1 for regularity, we ﬁrst provide a basic fact regarding
the eﬀect of a change of variables on the resolution of an ideal.
Lemma 3.5. Let I be a homogeneous ideal of R, let d1 be a positive integer, and deﬁne φ: R →R
by φ(x1) = xd1
1 and φ(xi) = xi for 2 ≤i ≤n. If φ(I) is homogeneous, then a minimal resolution
of φ(I) over R can be obtained by applying φ to a minimal resolution of I.
Moreover, the
(non-graded) Betti numbers of I and φ(I) will be equal and reg(φ(I)) ≥reg I.
Proof. Deﬁne S = K[x1, . . . , xn] to be a polynomial ring with the non-standard grading d(x1) =
d1 and d(xi) = 1 for 2 ≤i ≤n. Note that the map φ factors through S. Write φ = ψσ,
where σ: R →S is given by σ(xi) = xi for all i and ψ: S →R is given by ψ(x1) = xd1
1
and
ψ(xi) = xi for 2 ≤i ≤n. Then, by assumption, I is a homogeneous ideal of R and σ(I) is again
homogeneous in S. Applying σ to a minimal resolution of I yields a minimal resolution of σ(I),
where the modules and maps are unchanged except that the degrees of some of the maps, and
thus the shifts in the resolution, may have increased, showing reg(σ(I)) ≥reg(I). Now the map
ψ is precisely the map used in [44, Lemma 3.5 and Theorem 3.6(b)]. The result follows from
combining these results.
□
Lemma 3.6. Let I and J be monomial ideals of R and let xi be a variable. If (I : xi) = J and
(I, xi) = (J, xi), then
(i) reg(R/J) ≤reg(R/I) ≤reg(R/J) + 1, and
(ii) depth(R/J) −1 ≤depth(R/I) ≤depth(R/J).


## Page 14


14
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
Proof. (i):
By Corollary 2.12(v), we have reg(R/(I, xi)) ≤reg(R/I) and reg(R/(J, xi)) ≤
reg(R/J), and by Corollary 2.12(vii), we have either reg(R/I) = reg(R/(I : xi))+1 = reg(R/J)+
1 or reg(R/I) = reg(R/(I, xi)) = reg(R/(J, xi)) ≤reg(R/J).
In the latter case one has
reg(R/I) = reg(R/J) because by Corollary 2.12(iv), one has reg(R/J) ≤reg(R/I). Combining
these facts yields reg(R/J) ≤reg(R/I) ≤reg(R/J) + 1.
(ii): By Corollary 2.12(vi), we have either depth(R/I) = depth(R/J) or depth(R/I) =
depth(R/(I, xi)). In the latter case one has
depth(R/J) ≥depth(R/I) = depth(R/(I, xi)) = depth(R/(J, xi)) ≥depth(R/J) −1
because by parts (ii) and (i) of Corollary 2.12 one has the inequalities depth(R/J) ≥depth(R/I)
and depth(R/(J, xi)) ≥depth(R/J) −1, respectively.
□
Using the notation introduced for Theorem 3.1 we are now able to control regularity when
lowering the degrees of the generators of a monomial ideal.
Theorem 3.7. Let I be a monomial ideal and let L′ be the ideal ({xa/xq−1
i
| xa ∈Bi} ∪Ai}),
where xi is a variable. The following hold.
(a) If p ≥1 and q −p ≥2, then reg(R/L) ≤reg(R/I) ≤reg(R/L) + 1.
(b) If p ≥0 and q −p = 1, then reg(R/L) ≤reg(R/I).
(c) If p = 0 and q ≥2, then reg(R/L′) ≤reg(R/I) ≤reg(R/L′) + q −1.
Proof. (a): As in Theorem 3.1, we assume i = 1. Forming a partial polarization of xq
1 with
respect to new variables x1,2, . . . , x1,q−1 will not change the regularity by Lemma 2.10 (d). By the
same argument, forming a full polarization of x2, . . . , xn will also not change the regularity. Thus
we may assume that I = (x2
1h1, . . . , x2
1hm, hm+1, . . . , hr) and L = (x1h1, . . . , x1hm, hm+1, . . . , hr)
where hj are squarefree monomials and x1 does not divide hj for all j. Note that (I, x1) = (L, x1)
and (I : x1) = L.
Thus, by Lemma 3.6, we have reg(R/I) = reg(R/L) + 1 or reg(R/I) =
reg(R/L) as claimed.
(b): This part follows from the proof of Theorem 3.1(b) and Lemma 2.10(d).
(c): We proceed by induction on q ≥2. There are monomials h1, . . . , hr not containing x1
such that
I = (xq
1h1, . . . , xq
1hm, hm+1, . . . , hr) and L = (xq−1
1
h1, . . . , xq−1
1
hm, hm+1, . . . , hr).
Note that (I, x1) = (L, x1) and L = (I : x1). Then, applying Lemma 3.6 to I and L, one has
reg(R/L) ≤reg(R/I) ≤reg(R/L) + 1. In particular the required inequality holds for q = 2. If
q > 3, applying induction to L, the inequality follows.
□
Corollary 3.8. Let I be a monomial ideal of R and let J be its radical. The following hold.
(i) [46] reg(R/J) ≤reg(R/I).
(ii) If I is Cohen–Macaulay, then a(R/J) ≤a(R/I), where a(·) is the a-invariant.
Proof. (i): It follows by applying Theorem 3.7 to every vertex xi as many times as necessary.
(ii): By Corollary 3.3, J is Cohen–Macaulay. Hence, by [64, Corollary B.4.1], one has a(M) =
reg(M) −depth(M) for M = R/I and M = R/J. As dim(R/I) = dim(R/J) = depth(R/I) =
depth(R/J), the inequality follows from part (i).
□
Remark 3.9. Let I ⊂R be a monomial ideal and let f be a monomial which is a non-zero
divisor of R/I. Then reg(R/fI) = reg(R/I)+deg(f) and reg(R/(I, f)) = reg(R/I)+deg(f)−1.
This follows from Proposition 5.9. Thus the upper bound of Theorem 3.7(c) is tight.


## Page 15


DEPTH AND REGULARITY OF MONOMIAL IDEALS
15
Example 3.10. The ideals I = (x2
1x2x2
3, x2
3x4, x3
4x5) and J = (x1x2x2
3, x2
3x4, x3
4x5) have regu-
larity 5. Thus the lower bound of Theorem 3.7(c) is also tight.
Example 3.11. The ideals I = (x7
1x2x2
3, x7
1x3
5, x6
1x2
3x4, x2x7
5), L = (x6
1x2x2
3, x6
1x3
5, x6
1x2
3x4, x2x7
5)
have regularity 16 and 13, respectively. Thus in Theorem 3.7(b), reg(R/L) + 1 is not an upper
bound for reg(R/I).
4. Edge ideals of clutters with non-increasing depth
Let C be a clutter with vertex set X = {x1, . . . , xn} and let {xv1, . . . , xvr} be the minimal
generating set of I(C). The matrix A whose column vectors are v⊤
1 , . . . , v⊤
r is called the incidence
matrix of C. The set covering polyhedron of C is given by:
Q(A) := {x ∈Rn| x ≥0; xA ≥1},
where 1 = (1, . . . , 1). The rational polyhedron Q(A) is called integral if it has only integral
vertices.
A clutter is called uniform (resp.
unmixed) if all its edges (resp.
minimal vertex
covers) have the same cardinality. A clutter is ideal if its set covering polyhedron is integral [6].
Deﬁnition 4.1. A clutter C, with incidence matrix A, has the max-ﬂow min-cut (MFMC)
property if both sides of the LP-duality equation
(4.1)
min{⟨α, x⟩| x ≥0; xA ≥1} = max{⟨y, 1⟩| y ≥0; Ay ≤α}
have integral optimum solutions x, y for each nonnegative integral vector α.
Deﬁnition 4.2. Let I be a squarefree monomial ideal of R and let p1, . . . , pr be the associated
primes of I. Given an integer k ≥1, we deﬁne the k-th symbolic power of I to be the ideal
I(k) :=
r\
i=1
(IkRpi ∩R) = pk
1 ∩· · · ∩pk
r.
An ideal I of R is called normally torsion-free if Ass(R/Ik) is contained in Ass(R/I) for
all k ≥1. Notice that if I is a squarefree monomial ideal, then I is normally torsion-free if and
only if Ik = I(k) for all k ≥1. A major result of [18, 20] shows that a clutter C has the max-ﬂow
min-cut property if and only if I(C) is normally torsion-free (cf. [13, Proposition 3.4]).
Lemma 4.3. ([18, Lemma 5.6], [10, Lemma 2.1]) If C is a uniform clutter and Q(A) is integral,
then there exists a minimal vertex cover of C intersecting every edge of C in exactly one vertex.
Theorem 4.4. [6, Theorem 1.17] If Q(A) is integral and B is the incidence matrix of the clutter
C∨of minimal vertex covers of C, then Q(B) is integral.
Lemma 4.5. If C is an unmixed clutter and Q(A) is integral, then there exists an edge of C
intersecting every minimal vertex cover of C in exactly one vertex.
Proof. By duality [66, Theorem 6.3.39] the minimal vertex covers of C∨(resp. edges of C∨) are
the edges of C (resp. minimal vertex covers of C). Let B be the incidence matrix of C∨. As
Q(A) is integral and C is unmixed, by Lemma 4.4, Q(B) is also integral and C∨is uniform. Thus
applying Lemma 4.3 to C∨, there exists a minimal vertex cover of C∨intersecting every edge of
C∨in exactly one vertex. Hence by duality the result follows.
□
Let I ⊂R be a homogeneous ideal and let m = (x1, . . . , xn) be the maximal irrelevant ideal
of R. Recall that the analytic spread of I, denoted by ℓ(I), is given by
ℓ(I) = dim R[It]/mR[It].


## Page 16


16
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
This number satisﬁes ht(I) ≤ℓ(I) ≤dim(R) [63, Corollary 5.1.4].
Theorem 4.6. [2, 12] infi{depth(R/Ii)} ≤dim(R)−ℓ(I), with equality if the associated graded
ring grI(R) is Cohen–Macaulay.
Brodmann [1] improved this inequality by showing that depth(R/Ik) is constant for k ≫0
and that this constant value is bounded from above by dim(R) −ℓ(I). For a generalization of
these results to other ideal ﬁltrations see [30, Theorem 1.1]. The constant value of depth(R/Ik)
for k ≫0 is called the limit depth of I and is denoted by limk→∞depth(R/Ik).
Deﬁnition 4.7. A homogeneous ideal I ⊂R has non-increasing depth if
depth(R/Ik) ≥depth(R/Ik+1) ∀k ≥1,
and I has non-decreasing regularity if reg(R/Ik) ≤reg(R/Ik+1) for all k ≥1. The ideal I has
the persistence property if Ass(R/Ik) ⊂Ass(R/Ik+1) for k ≥1.
There are some classes of monomial ideals with non-increasing depth and non-decreasing
regularity [3, 5, 26, 27, 52]. A natural way to show these properties for a monomial ideal I is to
prove the existence of a monomial f such that (Ik+1 : f) = Ik for k ≥1. This was exploited in
[3, 43] and in [24, Corollary 3.11] in connection to normally torsion-free ideals.
Theorem 4.8. [3, Theorem 5.1] If I(C) is the edge ideal of a clutter C which has a good leaf,
then I(C) has non-increasing depth and non-decreasing regularity.
In particular edge ideals of forests or simplicial trees have non-increasing depth and non-
decreasing regularity. Our next result gives another wide family of ideals with these properties.
Theorem 4.9. Let C be a clutter and let I = I(C) be its edge ideal. If C is unmixed and satisﬁes
the max-ﬂow min-cut property, then
(a) depth(R/Ik) ≥depth(R/Ik+1) for k ≥1, and
(b) reg(R/Ik) ≤reg(R/Ik+1) for k ≥1.
Proof. Let C1, . . . , Cs be the minimal vertex covers of C. If pi is the ideal of R generated by Ci
for i = 1, . . . , s, then p1, . . . , ps are the minimal primes of I [66, Theorem 6.3.39]. As C has the
max-ﬂow min-cut property, by [50, Corollary 22.1c], Q(A) is integral. Therefore, by Lemma 4.5,
there exists an edge e of C intersecting every Ci in exactly one vertex. Thus |e ∩pi| = 1 for
i = 1, . . . , s. We claim that (Ik+1 : xe) = Ik for k ≥1, where xe = Q
xi∈e xi. The k-th symbolic
power of I is given by
(4.2)
I(k) = pk
1 ∩· · · ∩pk
s,
and by [20, Corollary 3.14], Ik = I(k) for k ≥1. Clearly Ik is contained in (Ik+1 : xe) because
xe is in I. To show the other inclusion take xa in (Ik+1 : xe). Fix any 1 ≤i ≤s. Then xaxe is
in Ik+1 ⊂pk+1
i
. Thus there are xj1, . . . , xjk+1 in pi with j1 ≤· · · ≤jk+1 such that
xaxe = xj1 · · · xjk+1xb,
for some xb. Since |e ∩pi| = 1 from this equality, we get that with one possible exception all
variables that occur in xe divide xb. Thus xa ∈pk
i . As 1 ≤i ≤s was an arbitrary ﬁxed integer,
using Eq. (4.2), we get xa ∈I(k) = Ik. Thus (Ik+1 : xe) = Ik, as claimed. To prove parts (a)
and (b) note that, by Corollary 2.12(ii), one has
depth(R/Ik) = depth(R/(Ik+1 : xe)) ≥depth(R/Ik+1),
and by Corollary 2.12(iv), one has reg(R/Ik) = reg(R/(Ik+1 : xe)) ≤reg(R/Ik+1).
□


## Page 17


DEPTH AND REGULARITY OF MONOMIAL IDEALS
17
Corollary 4.10. Let C be a clutter and let J = I(C)∨be its ideal of covers. If C is uniform and
its set covering polyhedron is integral, then
(a) depth(R/J(k)) ≥depth(R/J(k+1)) for k ≥1, and
(b) reg(R/J(k)) ≤reg(R/J(k+1)) for k ≥1.
Proof. This follows using duality and adapting the proof of Theorem 4.9.
□
5. Edge ideals of graphs
Let G be a graph with vertex set V (G) = {x1, . . . , xn}. A connected component of G with at
least two vertices is called non-trivial. We denote the set of isolated vertices of G by isol(G) and
the number of non-trivial bipartite components of G by c0(G). The neighbor set of xi, denoted
NG(xi), is the set of all xj ∈V (G) such that {xi, xj} is an edge of G.
Proposition 5.1. Let I(G) be the edge ideal of G. The following hold for k ≥1 and i = 1, . . . , n.
(a) depth(R/(I(G)k : xk
i )) ≤depth(R/(I(G \ NG(xi))k, NG(xi))).
(b) [66, p. 293] (I(G): xi) = (I(G \ NG(xi)), NG(xi)).
(c) dim(R) −ℓ(I(G)) = |isol(G)| + c0(G).
(d) [61, Theorem 4.4(1)] limk→∞depth(R/I(G)k) = |isol(G)| + c0(G).
(e) If H = G \ NG(xi), then limk→∞depth(R/(I(H)k, NG(xi))) = |isol(H)| + c0(H).
Proof. (a): Clearly xk
j ∈(I(G)k : xk
i ) for xj ∈NG(xi). Setting H = G \ NG(xi), it is not hard
to see that xk
j is a minimal generator of the ideal (I(G)k : xk
i ) for xj ∈NG(xi) and that any
minimal generator of I(H)k is a minimal generator of (I(G)k : xk
i ). The colon ideal (I(G)k : xk
i )
is minimally generated by
{xk
j | xj ∈NG(xi)} ∪G(I(H)k) ∪{xα1, . . . , xαr},
for some monomials xα1, . . . , xαr such that each xαi contains at least one variable in NG(xi).
One has the equality
(NG(xi), (I(G)k : xk
i )) = (NG(xi), I(H)k).
Therefore, starting with the ideal (I(G)k : xk
i ) and any variable xj in NG(xi), and successively
applying Theorem 3.1, the required inequality follows.
(c): Let G1, . . . , Gm be the non-trivial connected components of G. The analytic spread of
I(Gi) is equal to |V (Gi)| if Gi is non-bipartite and is equal to |V (Gi)| −1 otherwise (see [66,
Corollary 10.1.21 and Proposition 14.2.12]). Hence the equality follows from the fact that the
analytic spread is additive in the sense of [40, Lemma 3.4].
(e): This follows at once from part (d).
□
Lemma 5.2. Let G be a bipartite graph with vertices x1, . . . , xn, let I(G) be its edge ideal, and
let k ≥1, 1 ≤i ≤n be integers. The following hold.
(a) (I(G): xi)k = (I(G): xi)(k).
(b) (I(G)k : xk
i ) = (I(G): xi)k.
Proof. (a): The graph G \ NG(xi) is bipartite.
Hence, according to [55, Theorem 5.9], the
ideal I(G \ NG(xi)) is normally torsion-free and so is the ideal (NG(xi)) generated by NG(xi).
Therefore, by [55, Corollary 5.6], the ideal (I(G\NG(xi)), NG(xi)) is normally torsion-free. Thus
it suﬃces to observe that (I(G): xi) is equal to (I(G \ NG(xi)), NG(xi)) (see [66, p. 293]).


## Page 18


18
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
(b): Let p1, . . . , ps be the associated primes of I(G). Since G is bipartite, its edge ideal is
normally torsion-free [55, Theorem 5.9]. Therefore, using part (a) and noticing that the primary
decomposition of (I(G): xi) is ∩xi /∈pjpj, we get
(I(G)k : xk
i )
=





s\
j=1
pj


k
: xk
i


=




s\
j=1
pk
j

: xk
i

=
\
xi /∈pj
pk
j
=
(I(G): xi)(k) = (I(G): xi)k. ✷
The regularity of powers of the cover ideal of a bipartite graph was studied in [37] and the
depth of symbolic powers of cover ideals of graphs was examined in [33, 53].
Corollary 5.3. Let G be a bipartite graph. The following hold.
(a) [39, Corollary 5.3] If G is unmixed, then I(G) has non-increasing depth.
(b) ([5, Theorem 3.2], [26], [27, Corollary 2.4]) I(G)∨has non-increasing depth.
(c) I(G)∨has non-decreasing regularity.
Proof. (a): By [18, Theorem 4.6 and Proposition 4.27], the graph G has the max-ﬂow min-cut
property and since G is unmixed the result follows at once from Theorem 4.9.
(b)–(c): By [18, Theorem 4.6 and Corollary 4.28], G∨has the max-ﬂow min-cut property, and
G∨is unmixed because its minimal vertex covers are the edges of G. Thus by Theorem 4.9 the
ideal I(G∨) = I(G)∨has non-increasing depth and non-decreasing regularity.
□
The next interesting example is due to Kaiser, Stehl´ık, and ˇSkrekovski [38]. It shows that the
Alexander dual of a graph does not always has the persistence property for associated primes.
This example also shows that part (b) of Corollary 5.3 fails for non-bipartite graphs.
Example 5.4. [38] Let J = I∨be the Alexander dual of the edge ideal
I =
(x1x2, x2x3, x3x4, x4x5, x5x6, x6x7, x7x8, x8x9, x9x10, x1x10, x2x11, x8x11,
x3x12, x7x12, x1x9, x2x8, x3x7, x4x6, x1x6, x4x9, x5x10, x10x11, x11x12, x5x12).
Using Macaulay2 [22], it is seen that the values of depth(R/Ji), for i = 1, . . . , 4 are 8, 5, 0, 4,
respectively.
Deﬁnition 5.5. Let I ⊂R be a squarefree monomial ideal. The symbolic powers of I have
non-increasing depth if
depth(R/I(k)) ≥depth(R/I(k+1)) ∀k ≥1,
and have non-decreasing regularity if reg(R/I(k)) ≤reg(R/I(k+1)) for all k ≥1.
If G is a very well-covered graph (i.e., G is unmixed, has no isolated vertices and |V (G)| is
equal to 2ht(I(G))), then the symbolic powers of I(G)∨have non-increasing depth [52] (cf. [33,
Theorem 3.2]) and the symbolic powers of I(G) have non-increasing depth [39, Theorem 5.2].
The next result complements these facts.
Proposition 5.6. If G is a very well-covered graph, then the symbolic powers of I(G) have
non-decreasing regularity.
Proof. The graph G has a perfect matching by [19, Corollary 3.7(ii)]. Pick an edge e in a perfect
matching of G and set xe = Q
xi∈e xi. Note that any minimal vertex cover of G intersects e in


## Page 19


DEPTH AND REGULARITY OF MONOMIAL IDEALS
19
exactly one vertex because G is unmixed. Therefore (I(k+1) : xe) = I(k) for k ≥1. Thus the
result follows from part (iv) of Corollary 2.12.
□
We will give another family of squarefree monomial ideals whose symbolic powers have non-
increasing depth. A clique of a graph G is a set of vertices inducing a complete subgraph. The
clique clutter of G, denoted by cl(G), is the clutter on V (G) whose edges are the maximal cliques
of G (maximal with respect to inclusion).
Deﬁnition 5.7. A graph G is called strongly perfect if every induced subgraph H of G has a
maximal independent set of vertices C such that |C ∩e| = 1 for any maximal clique e of H.
Proposition 5.8. If G is a strongly perfect graph and J = I(cl(G)∨), then
(a) depth(R/J(k)) ≥depth(R/J(k+1)) for k ≥1, and
(b) reg(R/J(k)) ≤depth(R/J(k+1)) for k ≥1.
Proof. Let p1, . . . , ps be the set of all ideals (e) such that e ∈E(cl(G)). From the equality
J = I(cl(G)∨) = I(cl(G))∨=
\
e∈E(cl(G))
(e) =
s\
i=1
pi,
we get J(k) = ∩s
i=1pk
i for k ≥1. As G is strongly perfect, G has a maximal independent set of
vertices C such that |C ∩e| = 1 for any e ∈cl(G), that is, |C ∩pi| = 1 for i = 1, . . . , s. Hence,
setting f = Q
xi∈C xi, one has the equalities
(J(k+1) : f) =
 s\
i=1
pik+1 : f
!
=
s\
i=1
(pk+1
i
: f) =
s\
i=1
pk
i = J(k) for k ≥1.
Therefore, by parts (ii) and (iv) of Corollary 2.12, one has
depth(R/J(k)) = depth(R/(J(k+1) : f)) ≥depth(R/J(k+1)),
and reg(R/J(k)) = reg(R/(J(k+1) : f)) ≤reg(R/J(k+1)).
□
Proposition 5.9. Let A = K[X] and B = K[Y ] be polynomial rings over a ﬁeld K in disjoint
sets of variables, let I and J be nonzero homogeneous proper ideals of A and B respectively, and
let R = K[X, Y ]. The following hold.
(a) [25, Proposition 3.7] R/(I + J)i is Cohen–Macaulay for all i ≤k if and only if A/Ii and
B/Ji are Cohen–Macaulay for all i ≤k.
(b) [34, Lemma 3.2] reg(R/(I + J)) = reg(A/I) + reg(B/J).
(c) [34, Lemma 3.2] reg(R/IJ) = reg(A/I) + reg(B/J) + 1.
The Cohen–Macaulay property of the square of an edge ideal can be expressed in terms of its
connected components (cf. [65, Lemma 4.1]). For additional results on the depth of powers of
sums of ideals see [25] and the references therein.
Corollary 5.10. [48, Corollary 4.9] Let G be a graph with connected components G1, . . . , Gm.
Then I(G)2 is Cohen–Macaulay if and only if I(Gi)2 is Cohen–Macaulay for i = 1, . . . , m.
Proof. Since the radical of a Cohen–Macaulay monomial ideal is Cohen–Macaulay [32] (see
Corollary 3.3), the results follows from Proposition 5.9.
□


## Page 20


20
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
Example 5.11. Let A = K[x1, x2, x3] and B = K[y1, y2, y3] be polynomial rings over a ﬁeld
K, let I = (x1x2, x2x3, x1x3) and J = (y1y2, y2y3, y1y3) be ideals of A and B respectively, and
let R = K[X, Y ]. Then A/I2 and B/I2 have depth 0 but R/(I + J)2 has depth 1, that is, the
depth of squares of monomial ideals is not additive on disjoint sets of variables.
Lemma 5.12. Let G be a graph without isolated vertices. The following hold.
(a) If R/I(G)2 is Cohen–Macaulay, then R/(I(G \ NG(xi))2 is Cohen–Macaulay for any xi.
(b) depth(R/I(G)2) = 0 if and only if G has a triangle C3 that intersects NG(xi) for any xi
outside C3. In particular if the depth of R/I(G)2 is 0, then G is connected.
Proof. (a): Using Proposition 5.1(a) and Corollary 2.12(ii), we get
depth(R/(I(G \ NG(xi))2, NG(xi))) ≥depth(R/(I(G)2 : x2
i )) ≥depth(R/I(G)2)
for all i. Thus R/(I(G \ NG(xi))2 is Cohen–Macaulay for all i.
(b) (⇒): As m = (x1, . . . , xn) is an associated prime of I(G)2, there is xa = xa1
1 · · · xan
n
such
that (I(G)2 : xa) = m. Thus xixa ∈I(G)2 for all i and xa /∈I(G)2. Note that xa is squarefree.
Indeed if ak ≥2 for some k, then xkxa = xbfifj for some monomial xb and some minimal
generators fi, fj of I(G), which is impossible because fi, fj are squarefree monomials of degree
2 and xa /∈I(G)2. Thus we may assume that xa = x1 · · · xr, for some r ≥3, and x1x2 ∈I(G).
Then x3xa = xbfifj for some xb and some minimal generators fi, fj of I(G). One can write
fi = x3xk and fj = x3xℓ, k ̸= ℓ, k ̸= 3, ℓ̸= 3. Clearly either xk = x1 or xk = x2 and either
xℓ= x1 or xℓ= x2 because xa is not in I(G)2. Thus x1, x2, x3 are the vertices of a triangle of G
that we denote by C3. Since xrxa ∈I(G)2, it follows that r = 3. Take any vertex xk not in C3.
As xkxa = xk(x1x2x3) and xkxa is in I(G)2, we get that xk is adjacent to some vertex of C3.
(b) (⇐): Pick a triangle C3 of G such that any vertex outside C3 is adjacent to a vertex of
C3. Setting xa = Q
xi∈V (C3) xi, we get that (I(G)2 : xa) is the maximal ideal m = (x1, . . . , xn).
Thus m is an associated prime of I(G)2, that is, depth(R/I(G)2) = 0. This part could also
follow from a general construction of [4].
□
In [35, 36] the Cohen–Macaulay property of the square of the edge ideal of a graph is classiﬁed.
Theorem 5.13. [36, Theorem 4.4] Let G be a graph with vertex set V (G) = {x1, . . . , xn} and
without isolated vertices. Then I(G)2 is Cohen–Macaulay if and only if G is a triangle-free
unmixed graph and G \ {xi} is unmixed for all i.
As an application we recover the following facts.
Corollary 5.14. ([7, Theorem 2.7], [35, Proposition 4.2]) Let G be a bipartite graph without
isolated vertices. Then I(G)2 is Cohen–Macaulay if and only if I(G) is a complete intersection,
i.e., G is a disjoint union of edges.
Proof. ⇒): Since I(G) is the radical of I(G)2, by Corollary 3.3, the ideal I(G) is Cohen–
Macaulay. Hence, according to a structure theorem for Cohen–Macaulay bipartite graphs [29,
Theorem 3.4], there is a bipartition V1 = {x1, . . . , xg}, V2 = {y1, . . . , yg} of G such that:
(i) {xi, yi} ∈E(G) for all i,
(ii) if {xi, yj} ∈E(G), then i ≤j, and
(iii) if {xi, yj}, {xj, yk} are in E(G) and i < j < k, then {xi, yk} ∈E(G).
We proceed by induction on g. If g = 1, I(G) is clearly a complete intersection. Using the
connected components of G together with Corollaries 3.3 and 5.10, and Proposition 5.9, we may


## Page 21


DEPTH AND REGULARITY OF MONOMIAL IDEALS
21
assume that I(G)2 is Cohen–Macaulay and that G is a Cohen–Macaulay connected bipartite
graph. Consider the graph H = G \ NG(y1). We set R = K[V1 ∪V2]. Note that NG(y1) = {x1}.
Hence, by Lemma 5.12(a), I(G \ {x1})2 is Cohen–Macaulay and so is I(G \ {x1}). Therefore
by induction I(G \ {x1}) is generated by x2y2, . . . , xgyg. As G is connected, using (i)–(iii), it is
seen that the edges of G are the edges of the perfect matching and all edges of the form {x1, yi},
i ≥1. It is not hard to see (by a separate induction procedure) that the square of I(G) is not
Cohen–Macaulay if g ≥2. Thus g = 1.
⇐): If I(G) is a complete intersection, it is well known that all powers of I(G) are Cohen–
Macaulay [42, 17.4, p. 139].
□
Let G be a graph. The next corollary follows from the result that “I(G)2 = I(G)(2) if and
only if G has no triangles”. This result originated in [55] implicitly, written explicitly in [49,
Lemma 3.1]. Fix an integer t ≥2. This lemma shows that I(G)t = I(G)(t) if and only if G
contains no odd cycles of length 2s −1 for any 2 ≤s ≤t (cf. [8, Theorem 4.13]).
Corollary 5.15. Let G be a graph without isolated vertices. If I(G)2 is Cohen–Macaulay, then
G has no triangles.
Proof. Let V (G) = {x1, . . . , xn} be the vertex set of G and let R be the polynomial ring K[V (G)].
We proceed by induction on n. The result is clear for n = 1, 2, 3. Assume n ≥4. We proceed by
contradiction assuming that G has a triangle C3. Using the connected components of G together
with Corollaries 3.3 and 5.10, and Proposition 5.9, we may assume that I(G)2 is Cohen–Macaulay
and G is connected. Thus, by Lemma 5.12(a), I(G \ NG(xi))2 is Cohen–Macaulay for all i. If G
has a vertex xi not in C3 such that NG(xi) do not intersect the vertex set V (C3) of C3, then C3
is a triangle of G \ NG(xi), a contradiction. Thus any vertex outside C3 is adjacent to a vertex
of C3. Hence, by Lemma 5.12(b), we get depth(R/I(G)2) = 0, a contradiction. This part could
also follow from a general construction of [4].
□
Example 5.16. [36, 48] The square of the edge ideal of the graph G of Fig. 1 is Cohen–Macaulay
and I(G) is Gorenstein. This can be veriﬁed using Macaulay2 [22]. This example appears as a
special case of [48, Conjecture 5.7]. A result of Hoang and Trung [36, Theorem 4.4] shows that
for a graph G without isolated vertices I(G)2 is Cohen–Macaulay if and only if G is triangle-
free and Gorenstein. The Cohen-Macaulay property of I(G)2 is also studied in [60] in terms of
simplicial complexes.
x1
x5
x4
x3
x2
x8
x7
x6
Figure 1. Gorenstein Graph G.


## Page 22


22
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
References
[1] M. Brodmann, The asymptotic nature of the analytic spread, Math. Proc. Cambridge Philos. Soc. 86 (1979),
35–39.
[2] L. Burch, Codimension and analytic spread, Proc. Camb. Phil. Soc. 72 (1972), 369–373.
[3] G. Caviglia, H. T. H`a, J. Herzog, M. Kummini, N. Terai and N. V. Trung, Depth and regularity modulo a
principal ideal, J. Algebraic Combin., to appear.
[4] J. Chen, S. Morey and A. Sung, The stable set of associated primes of the ideal of a graph, Rocky Mountain
J. Math. 32 (2002), 71–89.
[5] A. Constantinescu, M. R. Pournaki, S. A. Seyed Fakhari, N. Terai and S. Yassemi, Cohen-Macaulayness and
limit behavior of depth for powers of cover ideals, Comm. Algebra 43 (2015), no. 1, 143–157.
[6] G. Cornu´ejols, Combinatorial Optimization: Packing and Covering, CBMS-NSF Regional Conference Series
in Applied Mathematics 74, SIAM (2001).
[7] M. Crupi, G. Rinaldo, N. Terai and K. Yoshida, Eﬀective Cowsik–Nori theorem for edge ideals, Comm.
Algebra 38 (2010), no. 9, 3347–3357.
[8] H. Dao, A. De Stefani, E. Grifo, C. Huneke and L. N´u˜nez-Betancourt, Symbolic powers of ideals, Singularities
and foliations, geometry, topology and applications, 387–432, Springer Proc. Math. Stat., 222, Springer,
Cham, 2018.
[9] H. Dao, C. Huneke and J. Schweig, Bounds on the regularity and projective dimension of ideals associated
to graphs, J. Algebraic Combin. 38 (2013), no. 1, 37–55.
[10] L. A. Dupont and R. H. Villarreal, Algebraic and combinatorial properties of ideals and algebras of uniform
clutters of TDI systems, J. Comb. Optim. 21 (2011), no. 3, 269–292.
[11] D. Eisenbud, Commutative Algebra with a view toward Algebraic Geometry, Graduate Texts in Mathematics
150, Springer-Verlag, 1995.
[12] D. Eisenbud and C. Huneke, Cohen–Macaulay Rees algebras and their specialization, J. Algebra 81 (1983),
202–224.
[13] C. Escobar, R. H. Villarreal and Y. Yoshino, Torsion freeness and normality of blowup rings of monomial
ideals, Commutative Algebra, Lect. Notes Pure Appl. Math. 244, Chapman & Hall/CRC, Boca Raton, FL,
2006, pp. 69–84.
[14] S. Faridi, Monomial ideals via square-free monomial ideals, Lecture Notes in Pure and Applied Math. 244,
Taylor & Francis, Philadelphia, 2005, pp. 85–114.
[15] C. Francisco, H. T. H`a and J. Mermin, Powers of square-free monomial ideals and combinatorics, Commu-
tative algebra, 373–392, Springer, New York, 2013.
[16] R. Fr¨oberg, A study of graded extremal rings and of monomial rings, Math. Scand. 51 (1982), 22–34.
[17] P. Gimenez, J. Mart´ınez-Bernal, A. Simis, R. H. Villarreal and C. E. Vivares, Symbolic powers of monomial
ideals and Cohen-Macaulay vertex-weighted digraphs, in Singularities, Algebraic Geometry, Commutative
Algebra, and Related Topics (G. M. Greuel, et.al. Eds), Springer, Cham, pp. 491–510.
[18] I. Gitler, E. Reyes and R. H. Villarreal, Blowup algebras of square-free monomial ideals and some links to
combinatorial optimization problems, Rocky Mountain J. Math. 39 (2009), no. 1, 71–102.
[19] I. Gitler and C. E. Valencia, On bounds for some graph invariants, Bol. Soc. Mat. Mexicana (3)16 (2010),
no. 2, 73–94.
[20] I. Gitler, C. Valencia and R. H. Villarreal, A note on Rees algebras and the MFMC property, Beitr¨age
Algebra Geom. 48 (2007), no. 1, 141–150.
[21] I. Gitler and R. H. Villarreal, Graphs, Rings and Polyhedra, Aportaciones Mat. Textos, 35, Soc. Mat.
Mexicana, M´exico, 2011.
[22] D. Grayson and M. Stillman, Macaulay2, 1996. Available via anonymous ftp from math.uiuc.edu.
[23] H. T. H`a, K.-N Lin, S. Morey, E. Reyes and R. H. Villarreal, Edge ideals of oriented graphs. Preprint, 2018,
arXiv:1805.04167.
[24] H. T. H`a and S. Morey, Embedded associated primes of powers of square-free monomial ideals, J. Pure Appl.
Algebra 214 (2010), no. 4, 301–308.
[25] H. T. H`a, N. V. Trung and T. N. Trung, Depth and regularity of powers of sums of ideals, Math. Z. 282
(2016), no. 3-4, 819–838.
[26] N. T. Hang, Stability of depth functions of cover ideals of balanced hypergraphs. Preprint, 2017,
arXiv:1711.09178.
[27] N. T. Hang and T. N. Trung, The behavior of depth functions of cover ideals of unimodular hypergraphs,
Ark. Mat. 55 (2017), no. 1, 89–104.
[28] F. Harary, Graph Theory, Addison-Wesley, Reading, MA, 1972.


## Page 23


DEPTH AND REGULARITY OF MONOMIAL IDEALS
23
[29] J. Herzog and T. Hibi, Distributive lattices, bipartite graphs and Alexander duality, J. Algebraic Combin.
22 (2005), no. 3, 289–302.
[30] J. Herzog and T. Hibi, The depth of powers of an ideal, J. Algebra 291 (2005), 534–550.
[31] J. Herzog and T. Hibi, Monomial Ideals, Graduate Texts in Mathematics 260, Springer, 2011.
[32] J. Herzog, Y. Takayama and N. Terai, On the radical of a monomial ideal, Arch. Math. 85 (2005), 397–408.
[33] L. T. Hoa, K. Kimura, N. Terai and T. N. Trung, Stability of depths of symbolic powers of Stanley-Reisner
ideals, J. Algebra 473 (2017), 307–323.
[34] L. T. Hoa and N. D. Tam, On some invariants of a mixed product of ideals. Arch. Math. (Basel) 94 (2010),
no. 4, 327–337.
[35] D. T. Hoang, N. C. Minh and T. N. Trung, Combinatorial characterizations of the Cohen-Macaulayness of
the second power of edge ideals, J. Combin. Theory Ser. A 120 (2013), no. 5, 1073–1086.
[36] D. T. Hoang and T. N. Trung, A characterization of triangle-free Gorenstein graphs and Cohen-Macaulayness
of second powers of edge ideals, J. Algebraic Combin. 43 (2016), no. 2, 325–338.
[37] A. V. Jayanthan, N. Narayanan and S. Selvaraja, Regularity of powers of bipartite graphs, J. Algebraic
Combin. 47 (2018), no. 1, 17–38.
[38] T. Kaiser, M. Stehl´ık and R. ˇSkrekovski, Replication in critical graphs and the persistence of monomial
ideals, J. Combin. Theory Ser. A 123 (2014), no. 1, 239–251.
[39] K. Kimura, N. Terai and S. Yassemi, The projective dimension of the edge ideal of a very well-covered graph,
Nagoya Math. J. 230 (2018), 160–179.
[40] J. Mart´ınez-Bernal, S. Morey and R. H. Villarreal, Associated primes of powers of edge ideals, Collect. Math.
63 (2012), no. 3, 361–374.
[41] J. Mart´ınez-Bernal, Y. Pitones and R. H. Villarreal, Minimum distance functions of graded ideals and Reed-
Muller-type codes, J. Pure Appl. Algebra 221 (2017), 251–275.
[42] H. Matsumura, Commutative Ring Theory, Cambridge Studies in Advanced Mathematics 8, Cambridge
University Press, 1986.
[43] S. Morey and R. H. Villarreal, Edge ideals: algebraic and combinatorial properties, in Progress in Commu-
tative Algebra, Combinatorics and Homology, Vol. 1 (C. Francisco, L. C. Klingler, S. Sather-Wagstaﬀ, and
J. C. Vassilev, Eds.), De Gruyter, Berlin, 2012, pp. 85–126.
[44] J. Neves, M. Vaz Pinto and R. H. Villarreal, Regularity and algebraic properties of certain lattice ideals ,
Bull. Braz. Math. Soc. (N.S.) 45 (2014), 777–806.
[45] I. Peeva, Graded Syzygies, Algebra and Applications 14, Springer, 2011.
[46] M. S. Ravi, Regularity of ideals and their radicals, Manuscripta Math. 68 (1990), no. 1, 77–87.
[47] G. Ravindra, Some classes of strongly perfect graphs, Discrete Math. 206 (1999), no. 1-3, 197–203.
[48] G. Rinaldo, N. Terai and K. Yoshida, On the second powers of Stanley-Reisner ideals, J. Commut. Algebra
3 (2011), no. 3, 405–430.
[49] G. Rinaldo, N. Terai and Y. Yoshida, Cohen-Macaulayness for symbolic power ideals of edge ideals, J. Algebra
347 (2011), 1–22.
[50] A. Schrijver, Theory of Linear and Integer Programming, John Wiley & Sons, New York, 1986.
[51] A. Schrijver, Combinatorial Optimization, Algorithms and Combinatorics 24, Springer-Verlag, Berlin, 2003.
[52] S. A. Seyed Fakhari, Symbolic powers of cover ideal of very well-covered and bipartite graphs. Preprint, 2016,
arXiv:1604.00654v1.
[53] S. A. Seyed Fakhari, Depth and Stanley depth of symbolic powers of cover ideals of graphs, J. Algebra 492
(2017), 402–413.
[54] S. A. Seyed Fakhari, Symbolic powers of cover ideal of very well-covered and bipartite graphs, Proc. Amer.
Math. Soc. 146 (2018), no. 1, 97–110.
[55] A. Simis, W. V. Vasconcelos and R. H. Villarreal, On the ideal theory of graphs, J. Algebra 167 (1994),
389–416.
[56] D. E. Smith, On the Cohen–Macaulay property in commutative algebra and simplicial topology, Paciﬁc J.
Math. 141 (1990), 165–196.
[57] A. Sørensen, Projective Reed-Muller codes, IEEE Trans. Inform. Theory 37 (1991), no. 6, 1567–1576.
[58] N. Terai, Alexander duality theorem and Stanley–Reisner rings, S¯urikaisekikenky¯usho K¯oky¯uroku 1078
(1999), 174–184.
[59] N. Terai and N. V. Trung, Cohen-Macaulayness of large powers of Stanley-Reisner ideals, Adv. Math. 229
(2012), no. 2, 711–730.
[60] N. V. Trung and T. M. Tuan, Equality of ordinary and symbolic powers of Stanley-Reisner ideals, J. Algebra
328 (2011), 77–93.


## Page 24


24
J. MART´INEZ-BERNAL, S. MOREY, R. H. VILLARREAL, AND C. VIVARES
[61] T. N. Trung, Stability of depths of powers of edge ideals, J. Algebra 452 (2016), 157–187.
[62] A. Van Tuyl, A Beginner’s Guide to Edge and Cover Ideals, in Monomial Ideals, Computations and Appli-
cations, Lecture Notes in Mathematics 2083, Springer, 2013, pp. 63–94.
[63] W. V. Vasconcelos, Arithmetic of Blowup Algebras, London Math. Soc., Lecture Note Series 195, Cambridge
University Press, Cambridge, 1994.
[64] W. V. Vasconcelos, Computational Methods in Commutative Algebra and Algebraic Geometry, Springer-
Verlag, 1998.
[65] R. H. Villarreal, Cohen–Macaulay graphs, Manuscripta Math. 66 (1990), 277–293.
[66] R. H. Villarreal, Monomial Algebras, Second Edition, Monographs and Research Notes in Mathematics,
Chapman and Hall/CRC, 2015.
Departamento de Matem´aticas, Centro de Investigaci´on y de Estudios Avanzados del IPN,
Apartado Postal 14–740, 07000 Mexico City, D.F.
E-mail address: jmb@math.cinvestav.mx
Department of Mathematics, Texas State University, San Marcos, TX 78666
E-mail address: morey@txstate.edu
Departamento de Matem´aticas, Centro de Investigaci´on y de Estudios Avanzados del IPN,
Apartado Postal 14–740, 07000 Mexico City, D.F.
E-mail address: vila@math.cinvestav.mx
Departamento de Matem´aticas, Centro de Investigaci´on y de Estudios Avanzados del IPN,
Apartado Postal 14–740, 07000 Mexico City, D.F.
E-mail address: cevivares@math.cinvestav.mx

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
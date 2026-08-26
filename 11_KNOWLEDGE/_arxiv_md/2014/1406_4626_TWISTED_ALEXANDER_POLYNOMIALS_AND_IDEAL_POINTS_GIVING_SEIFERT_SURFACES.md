---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1406.4626
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1406.4626_Twisted_Alexander_polynomials_and_ideal_points_giving_Seifert_surfaces

> Source: 1406.4626_Twisted_Alexander_polynomials_and_ideal_points_giving_Seifert_surfaces.pdf

> Pages: 7

---


## Page 1


arXiv:1406.4626v1  [math.GT]  18 Jun 2014
TWISTED ALEXANDER POLYNOMIALS AND IDEAL POINTS GIVING SEIFERT
SURFACES
TAKAHIRO KITAYAMA
Abstract. The coeﬃcients of twisted Alexander polynomials of a knot induce regular functions
of the S L2(C)-character variety. We prove that the function of the highest degree has a ﬁnite
value at an ideal point which gives a minimal genus Seifert surface by Culler-Shalen theory. It
implies a partial aﬃrmative answer to a conjecture by Dunﬁeld, Friedl and Jackson.
1. Introduction
The aim of this paper is to present an application of twisted Alexander polynomials to Culler-
Shalen theory for knots, following a conjecture by Dunﬁeld, Friedl and Jackson [DFJ, Conjec-
ture 8.9].
In the notable work [CS] Culler and Shalen established a method to construct essential sur-
faces in a 3-manifold from an ideal point of the S L2(C)-character variety. Their theory ap-
plies Bass-Serre theory [Se1, Se2] to the functional ﬁeld of the representation variety. Twisted
Alexander polynomials [Li, W], which are known to be essentially equal to certain Reidemeis-
ter torsion [KL, Kitan], are invariants of a 3-manifold associated to linear representations of the
fundamental group. The torsion invariants generalize many properties of the Alexander polyno-
mial, and were shown by Friedl and Vidussi [FV1, FV3] to detect ﬁberedness for 3-manifolds
and the Thurston norms of irreducible ones which are not closed graph manifolds. We refer
the reader to the expositions [Sh] and [FV2] for literature and related topics on Culler-Shalen
theory and twisted Alexander polynomials respectively.
Let K be a null-homologous knot in a rational homology 3-sphere. We denote by Xirr(K)
the Zariski closure of the S L2(C)-character variety of K. Dunﬁeld, Friedl and Jackson [DFJ]
showed that for each irreducible component X0 in Xirr(K) certain normalizations of twisted
Alexander polynomials induce an invariant T X0
K
∈C[X0][t, t−1] called the torsion polynomial
function of K. The invariant T X0
K satisﬁes that deg T X0
K
≤4g(K) −2 and that T X0
K (χ)(t−1) =
T X0
K (χ)(t) for χ ∈X0, where g(K) is the genus of K (cf. [FK1, Theorem 1.1], [FKK, Theorem
1.5]). For a curve C in X0 we denote by T C
K ∈C[C][t, t−1] the restriction of T X0
K to C, and by
c(T C
K ) ∈C[C] the coeﬃcient function in T C
K of the highest degree 2g(K) −1. It is known that if
K is a ﬁbered knot, then c(T C
K ) is the constant function with value 1 (cf. [C, FK1, GKM]).
Conjecture 1.1 ([DFJ, Conjecture 8.9]). If an ideal point χ of a curve C in Xirr(K) gives a
Seifert surface of K, then the leading coeﬃcient of T C
K has a ﬁnite value at χ.
In this paper we give a partial aﬃrmative answer to Conjecture 1.1. The main theorem of this
paper is as follows:
2010 Mathematics Subject Classiﬁcation. Primary 57M27, Secondary 57Q10.
Key words and phrases. twisted Alexander polynomial, Reidemeister torsion, character variety.
1


## Page 2


2
T. KITAYAMA
Theorem 1.2. If an ideal point χ of a curve C in Xirr(K) gives a minimal genus Seifert surface
of K, then c(T C
K )(χ) is ﬁnite.
The statement of Theorem 1.2 is actually weaker than that of Conjecture 1.1 on the following
two points:
(1) An essential Seifert surface is not necessarily of minimal genus.
(2) If deg T C
K < 4g(K) −2, then c(T C
K )(χ) = 0 but the leading coeﬃcient of T C
K (χ) is not
necessarily ﬁnite.
Concerning (1) it should be remarked that classes of knots with a unique isotopy class of es-
sential Seifert surfaces are known. For instance, Lyon [Ly, Theorem 2 and Corollary 2.1] con-
structed such a class of non-ﬁbered knots containing p-twist knots with |p| > 1.
A generalization of Theorem 1.2 for general 3-manifolds will be discussed in a successive
work [Kitay]. See [KKM, KM, Mo] for recent works on other conjectures by Dunﬁeld-Friedl-
Jackson.
This paper is organized as follows. Section 2 sets up notation and terminology, and provides
a brief overview of Culler-Shalen theory. In particular, the precise meaning of ‘an ideal point
giving a surface’ is described. In Section 3 we review some basics of Reidemeister torsion, and
recalls properties of torsion polynomial functions. In this paper we mainly work with Reide-
meister torsion rather than twisted Alexander polynomials, based on the equivalence. Finally,
in Section 4 we prove Theorem 1.2.
Acknowledgment. This article is prepared for the proceedings of the conference “The Quan-
tum Topology and Hyperbolic Geometry” (Nha Trang, Vietnam, May 13-17, 2013). The author
gratefully acknowledges the organizers’ hospitality. The author would like to thank Stefan
Friedl and Takayuki Morifuji for valuable discussions and helpful comments. The author also
wishes to express his thanks to the anonymous referee for several useful comments in revising
the manuscript.
2. Culler-Shalen theory
We begin with brieﬂy reviewing Culler-Shalen theory [CS, Sh]. For more details on character
varieties we refer the reader to [LM].
2.1. Character varieties and ideal points. Let M be a compact orientable 3-manifold. The
algebraic group S L2(C) acts on the aﬃne algebraic set Hom(π1M, S L2(C)) by conjugation. The
algebro-geometric quotient X(M) of the action is called the S L2(C)-character variety of M. We
denote by t: Hom(π1M, S L2(C)) →X(M) the quotient map. For a representation ρ: π1M →
S L2(C) its character χρ : π1M →C is given by χρ(γ) = tr ρ(γ) for γ ∈π1M. The character
variety X(M) is known to be realized by the set of the characters χρ of S L2(C)-representations
ρ, and t(ρ) = χρ under the identiﬁcation. For γ ∈π1M a trace function Iγ : X(M) →C is deﬁned
by Iγ(χρ) = tr ρ(γ) for a representation ρ: π1M →S L2(C), and it is known that the coordinate
ring of X(M) is generated by {Iγ}γ∈π1M.
Let C be a curve in X(M) which is not necessarily irreducible, and let b
C be its smooth projec-
tive model. The points where the rational map b
C →C is undeﬁned are called the ideal points
of C.


## Page 3


TWISTED ALEXANDER POLYNOMIALS AND IDEAL POINTS GIVING SEIFERT SURFACES
3
Let K be a knot in a rational homology 3-sphere, and we denote by E its exterior. In the
following we set X(K) = X(E) and denote by Xirr(K) the Zariski closure of the subset of X(K)
consisting of the characters of irreducible representations.
2.2. Essential surfaces given by ideal points. A non-empty properly embedded compact ori-
entable surface S in M is called essential if for any component S 0 of S the homomorphism
π1S 0 →π1M induced by the natural inclusion map is injective, and if no component of S is
homeomorphic to S 2 or boundary parallel.
Let χ be an ideal point of a curve C in X(M). There exists a curve D in t−1(C) such that t|D is
not a constant map, and that t|D extends to a regular map bD →b
C between the smooth projective
models. We take a point ˜χ of bD in the preimage of χ. Associated to the valuation of C(D)
at ˜χ Bass-Serre theory [Se1, Se2] gives a canonical action of S L2(C(D)) on a tree T ˜χ without
inversions. Pulling back the action by the tautological representation π1M →S L2(C(D)), we
have an action of π1M on T ˜χ. Culler and Shalen [CS, Theorem 2.2.1] showed that the action
is non-trivial, i.e., for any vertex of T ˜χ the stabilizer of the action is not whole the group π1M.
Now essentially due to Stallings, Epstein and Waldhausen, there exists a map f : M →T ˜χ/π1M
such that f −1(P) is an essential surface, where P is the set of the middle points of edges. We say
that χ gives an essential surface S if S = f −1(P) for some f as above.
3. Torsion invariants
We review basics of Reidemeister torsion and recall torsion polynomial functions introduced
by Dunﬁeld, Friedl and Jackson [DFJ]. For more details on torsion invariants we refer the reader
to the expositions [Mi, N, T1, T2].
3.1. Reidemeister torsion. Let C∗= (Cn
∂n
−→Cn−1 →· · · →C0) be a ﬁnite dimensional chain
complex over a commutative ﬁeld F, and let c = {ci} and h = {hi} be bases of C∗and H∗(C∗)
respectively. Choose bases bi of Im ∂i+1 for each i = 0, 1, . . .n, and take a basis bihibi−1 of Ci for
each i as follows. Picking a lift of hi in Ker ∂i and combining it with bi, we ﬁrst obtain a basis
bihi of Ci. Then picking a lift of bi−1 in Ci and combining it with bihi, we obtain a basis bihibi−1
of Ci. The algebraic torsion τ(C∗, c, h) is deﬁned as:
τ(C∗, c, h) :=
n
Y
i=0
[bihibi−1/ci](−1)i+1 ∈F×,
where [bihibi−1/ci] is the determinant of the base change matrix from ci to bihibi−1. If C∗is
acyclic, then we write τ(C∗, c). It can be easily checked that τ(C∗, c, h) does not depend on the
choice of bi and bihibi−1.
Let (Y, Z) be a ﬁnite CW-pair. In the following when we write C∗(eY, eZ), eY stands for the
universal cover of Y and eZ the pullback of Z by the universal covering map eY →Y. For a
representation ρ: π1Y →GL(V) over a commutative ﬁeld F we deﬁne the twisted homology
group as:
Hρ
i (Y, Z; V) := Hi(C∗(eY, eZ) ⊗Z[π1Y] V).
If Z is empty, then we write Hρ
i (Y; V).
For an n-dimensional representation ρ: π1Y →GL(V) and a basis h of Hρ
∗(Y, Z; V) the Rei-
demeister torsion τρ(Y, Z; h) associated to ρ and h is deﬁned as follows. We choose a lift ˜e in eY


## Page 4


4
T. KITAYAMA
for each cell e ⊂Y \ Z. Then
τρ(Y, Z; h) := τ(C∗(eY, eZ) ⊗Z[π1Y] V, ⟨˜e ⊗1⟩e, h) ∈F×/(−1)n det ρ(π1Y).
If Z is empty or if Hρ
∗(Y, Z; V) = 0, then we drop Z or h in the notation τρ(Y, Z; h). It can be easily
checked that τρ(Y, Z; h) does not depend on the choice of ˜e and is invariant under conjugation of
representations. It is known that Reidemeister torsion is a simple homotopy invariant.
3.2. Torsion polynomial functions. Let K be a null-homologous knot in a rational homology
3-sphere. We take an epimorphism α: π1E →⟨t⟩, where ⟨t⟩is the inﬁnite cyclic group generated
by the indeterminate t. For a representation ρ: π1E →GLn(F) we deﬁne a representation
α ⊗ρ: π1E →GLn(F(t)) by α ⊗ρ(γ) = α(γ)ρ(γ) for γ ∈π1E. If Hα⊗ρ
∗
(E; F(t)n) = 0, then
the Reidemeister torsion τα⊗ρ(E) is deﬁned, and is known by Kirk and Livingston [KL], and
Kitano [Kitan] to be essentially equal to the twisted Alexander polynomial associated to α and
ρ. Friedl and Kim [FK1, Theorem 1.1] showed that
deg τα⊗ρ(E) ≤n(2g(K) −1)
(See also [FK2]). It is known by Cha [C], Friedl and Kim [FK1], and Goda, Kitano and Morifuji
[GKM] that if K is a ﬁbered knot, then
deg τα⊗ρ(E) = n(2g(K) −1)
and τα⊗ρ(E) is represented by a fraction of monic polynomials in F[t, t−1]. See [FV2] for details
on twisted Alexander polynomials and their precise relation with Reidemeister torsion.
Let X0 be an irreducible component of Xirr(K). Dunﬁeld, Friedl and Jackson [DFJ, Theorem
1.5] showed that there exists an invariant T X0
K
∈C[X0][t, t−1] called the torsion polynomial
function of X0 such that the following are satisﬁed for χρ ∈X0:
(i) If Hα⊗ρ
∗
(E; C(t)2) = 0 then, T X0
K (χρ) = τα⊗ρ(E) ∈C(t)/⟨t⟩.
(ii) If Hα⊗ρ
∗
(E; C(t)2) , 0 then, T X0
K (χρ) = 0.
(iii) T X0
K (χρ)(t−1) = T X0
K (χρ)(t).
For a curve C in X0 we denote by T C
K ∈C[X0][t, t−1] the restriction of T X0
K to C, and by c(T C
K ) ∈
C[C] the coeﬃcient function in T C
K of the highest degree 2g(K) −1.
4. Main theorem
Now we prove Theorem 1.2. We ﬁrst prepare key lemmas for the proof.
4.1. Lemmas. Let K be a null-homologous knot in a rational homology 3-sphere and let S be a
minimal genus Seifert surface of K. A tubular neighborhood of S is identiﬁed with S × [−1, 1].
We set N := E \ S × (−1, 1), and denote by ι± : S →N the natural homeomorphisms such that
ι±(S ) = S × (±1). Since the homomorphisms π1S →π1E and π1N →π1E induced by the
natural inclusion maps are injective, in the following we regard π1S and π1N as subgroups of
π1E.
Lemma 4.1. Let ρ: π1E →GLn(F) be an irreducible representation with n > 1 such that
Hα⊗ρ
∗
(E; F(t)n) = 0. Then the following hold:
(i) Hρ
0(S ; Fn) = Hρ
0(N; Fn) = Hρ
2(N; Fn) = 0.
(ii) If deg τα⊗ρ(E) = n(2g(K) −1), then (ι±)∗: Hρ
1(S ; Fn) →Hρ
1(N; Fn) are isomorphisms.


## Page 5


TWISTED ALEXANDER POLYNOMIALS AND IDEAL POINTS GIVING SEIFERT SURFACES
5
Proof. This lemma is proved by techniques developed in [FK1] together with [FKK, Proposition
A.3] in terms of twisted Alexander polynomials. We give only the main steps of the proof with
corresponding parts in the references, and the details are left to the reader.
It follows from [FK1, Proposition 3.5] and [FKK, Proposition A.3] that Hρ
0(S ; Fn) = 0. Since
Hα⊗ρ
∗
(E; F(t)n) = 0, the long exact sequence in [FK1, Proposition 3.2] implies that
Hρ
i (N; Fn) = Hρ
i (S ; Fn) = 0
for i = 0, 2, which proves (i).
It follows from Proof of [FK1, Theorem 1.1] that if deg τα⊗ρ(E) = n(2g(K) −1), then the
inequalities in [FK1, Proposition 3.3] turn into equalities. Now (ii) follows from the proof of
[FK1, Proposition 3.3].
□
Lemma 4.2. Let ρ: π1E →GLn(F) be an irreducible representation such that Hα⊗ρ
∗
(E; F(t)n) =
0. If deg τα⊗ρ(E) = n(2g(K) −1), then
τα⊗ρ(E) = τρ(N, S × 1) det(t · id −(ι+)−1
∗◦(ι−)∗),
where (ι±)∗are the isomorphisms Hρ
1(S ; Fn) →Hρ
1(N; Fn).
Proof. We pick a basis h of Hρ
1(S ; Fn).
Since Hα⊗ρ
1
(S ; F(t)n)
=
Hρ
1(S ; Fn) ⊗F(t) and
Hα⊗ρ
1
(N; F(t)n) = Hρ
1(N; Fn) ⊗F(t), h and (ι+)∗(h) can be seen also as bases of Hα⊗ρ
1
(S ; F(t)n)
and Hα⊗ρ
1
(N; F(t)n) respectively. Taking appropriate triangulations of E, N and S and lift of
simplices in the universal covers, we have the following exact sequences:
0 →C∗(eS ) ⊗F(t)n t(ι+)∗−(ι−)
−−−−−−−→C∗(eN) ⊗F(t)n →C∗(eE) ⊗F(t)n →0,
0 →C∗(eS ) ⊗Fn (ι+)∗
−−−→C∗(eN) ⊗Fn →C∗(eN, ]
S × 1) ⊗Fn →0,
where the local coeﬃcients in the ﬁrst and second sequences are understood to be induced by
α ⊗ρ and ρ respectively. By the multiplicativity of Reidemeister torsion [Mi, Theorem 3.1] and
Lemma 4.1 we have
τα⊗ρ(N; (ι+)∗(h)) det(t · id −(ι+)−1
∗◦(ι−)∗) = τα⊗ρ(S ; h)τα⊗ρ(E),
τρ(N; (ι+)∗(h)) = τρ(S ; h)τρ(N, S × 1).
By the functoriality of Reidemeister torsion [T1, Proposition 3.6] we have
τα⊗ρ(N; (ι+)∗(h)) = τρ(N; (ι+)∗(h)),
τα⊗ρ(S ; h) = τρ(S ; h).
The desired formula now follows from the above equalities.
□
Lemma 4.3. There exists a regular function f of X(N) such that
f (χρ) = τρ(N, S × 1)
for a representation ρ: π1N →GLn(F) satisfying that Hρ
∗(N, S × 1; Fn) = 0.
Proof. Let ρ: π1N →GLn(F) be a representation such that Hρ
∗(N, S × 1; Fn) = 0. We take a
ﬁnite 2-dimensional CW-pair (V, W) with C0(V, W) = 0 which is simple homotopy equivalent
to (N, S × 1). The diﬀerential map
C2(eV, eW) ⊗F[π1V] Fn →C1(eV, eW) ⊗F[π1V] Fn


## Page 6


6
T. KITAYAMA
is represented by the matrix ρ(A) obtained as follows from a matrix A in Z[π1V]. We ﬁrst
consider the matrix whose (i, j)-entries are the image of that of A by ρ. Then we naturally
forget the matrix structures of the entries to get a matrix ρ(A) in C. By the simple homotopy
invariance and the deﬁnition of Reidemeister torsion we have
τρ(N, S × 1) = τρ(V, W) = det ρ(A).
It follows from basics of Linear algebra that det ρ(A) is written as a polynomial in {tr ρ(A)i}i∈Z,
and that tr ρ(A)i is as one in {tr ρ(γ)}γ∈π1V, which proves the lemma.
□
The following lemma is a direct corollary of [CS, Theorem 2.2.1] and [CS, Proposition 2.3.1].
Lemma 4.4. Suppose that an ideal point χ of a curve in Xirr(K) gives an essential surface S .
Then Iγ(χ) ∈C for γ ∈π1E represented by a loop in the complement of S .
4.2. Proof of the main theorem.
Proof of Theorem 1.2. Let χ be an ideal point of a curve C in Xirr(K) which gives a minimal
genus Seifert surface S of K, and let ρ: π1E →S L2(C) be an irreducible representation such
that χρ ∈C. If Hα⊗ρ
∗
(E; C(t)2) = 0 and if deg τα⊗ρ(E) = 4g(K) −2, then by Lemma 4.2 we have
c(T C
K )(χρ) = τρ(N, S × 1),
and so it follows from Lemma 4.3 that the function c(T C
K ) is in the subring of C[C] generated
by Iγ for γ ∈π1N. Since it follows from Lemma 4.4 that Iγ(χ) ∈C for γ ∈π1N, we obtain
c(T C
K )(χ) ∈C, which completes the proof.
□
References
[C]
J. C. Cha, Fibred knots and twisted Alexander invariants, Trans. Amer. Math. Soc. 355 (2003), no. 10,
4187–4200.
[CS]
M. Culler and P. B. Shalen, Varieties of group representations and splittings of 3-manifolds, Ann. of Math.
(2) 117 (1983), no. 1, 109–146.
[DFJ]
N. M. Dunﬁeld, S. Friedl and N. Jackson, Twisted Alexander polynomials of hyperbolic knots, Experiment.
Math. 21 (2012), 329–352.
[FK1]
S. Friedl and T. Kim, The Thurston norm, ﬁbered manifolds and twisted Alexander polynomials, Topology
45 (2006), no. 6, 929–953.
[FK2]
S. Friedl and T. Kim, Twisted Alexander norms give lower bounds on the Thurston norm, Trans. Amer.
Math. Soc. 360 (2008), no. 9, 4597–4618.
[FKK]
S. Friedl, T. Kim and T. Kitayama, Poincar´e duality and degrees of twisted Alexander polynomials, Indiana
Univ. Math. J. 61 (2012), 147–192.
[FV1]
S. Friedl and S. Vidussi, Twisted Alexander polynomials detect ﬁbered 3-manifolds, Ann. of Math. (2) 173
(2011), no. 3, 1587–1643.
[FV2]
S. Friedl and S. Vidussi, A survey of twisted Alexander polynomials, The mathematics of knots, 45–94,
Contrib. Math. Comput. Sci., 1, Springer, Heidelberg, 2011.
[FV3]
S. Friedl and S. Vidussi, The Thurston norm and twisted Alexander polynomials, to appear in J. Reine
Angew. Math., arXiv:1204.6456.
[GKM] H. Goda, T. Kitano and T. Morifuji, Reidemeister torsion, twisted Alexander polynomial and ﬁbered knots,
Comment. Math. Helv. 80 (2005), no. 1, 51–61.
[KKM] T. Kim, T. Kitayama and T. Morifuji, Twisted Alexander polynomials on curves in character varieties of
knot groups, Internat. J. Math. 24 (2013), no. 3, 1350022, 16 pp.
[KM]
T. Kim and T. Morifuji, Twisted Alexander polynomials and character varieties of 2-bridge knot groups,
Internat. J. Math. 23 (2012), no. 6, 1250022, 24 pp.
[KL]
P. Kirk and C. Livingston, Twisted Alexander invariants, Reidemeister torsion, and Casson-Gordon in-
variants, Topology 38 (1999), no. 3, 635–661.


## Page 7


TWISTED ALEXANDER POLYNOMIALS AND IDEAL POINTS GIVING SEIFERT SURFACES
7
[Kitan] T. Kitano, Twisted Alexander polynomial and Reidemeister torsion, Paciﬁc J. Math. 174 (1996), no. 2,
431–442.
[Kitay] T. Kitayama, Twisted Alexander polynomials and incompressible surfaces given by ideal points, in prepa-
ration.
[Li]
X. S. Lin, Representations of knot groups and twisted Alexander polynomials, Acta Math. Sin. (Engl. Ser.)
17 (2001), no. 3, 361–380.
[LM]
A. Lubotzky and A. R. Magid, Varieties of representations of ﬁnitely generated groups, Mem. Amer.
Math. Soc. 58 (1985), no. 336, xi+117 pp.
[Ly]
H. C. Lyon, Simple knots with unique spanning surfaces, Topology 13 (1974), 275–279.
[Mi]
J. Milnor, Whitehead torsion, Bull. Amer. Math. Soc. 72 (1966) 358–426.
[Mo]
T. Morifuji, On a conjecture of Dunﬁeld, Friedl and Jackson, C. R. Math. Acad. Sci. Paris 350 (2012), no.
19-20, 921–924.
[N]
L. I. Nicolaescu, The Reidemeister torsion of 3-manifolds, de Gruyter Studies in Mathematics, 30, Walter
de Gruyter & Co., Berlin, 2003. xiv+249 pp.
[Se1]
J.-P. Serre, Arbres, amalgames, S L2 (French), Avec un sommaire anglais, R´edig´e avec la collaboration de
Hyman Bass, Ast´erisque, No. 46, Soci´et´e Mathematique de France, Paris, 1977, 189 pp, (1 plate).
[Se2]
J.-P. Serre, Trees, Translated from the French by John Stillwell, Springer-Verlag, Berlin-New York, 1980.
ix+142 pp.
[Sh]
P. B. Shalen, Representations of 3-manifold groups, Handbook of geometric topology, 955–1044, North-
Holland, Amsterdam, 2002.
[T1]
V. Turaev, Introduction to combinatorial torsions, Notes taken by Felix Schlenk, Lectures in Mathematics
ETH Zurich, Birkhauser Verlag, Basel, 2001. viii+123 pp.
[T2]
V. Turaev, Torsions of 3-dimensional manifolds, Progress in Mathematics, 208, Birkhauser Verlag, Basel,
2002, x+196 pp.
[W]
M. Wada, Twisted Alexander polynomial for ﬁnitely presentable groups, Topology 33 (1994), no. 2, 241–
256.
Department of Mathematics, Tokyo Institute of Technology, 2-12-1 Ookayama, Meguro-ku, Tokyo 152-8551,
Japan
E-mail address: kitayama@math.titech.ac.jp

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
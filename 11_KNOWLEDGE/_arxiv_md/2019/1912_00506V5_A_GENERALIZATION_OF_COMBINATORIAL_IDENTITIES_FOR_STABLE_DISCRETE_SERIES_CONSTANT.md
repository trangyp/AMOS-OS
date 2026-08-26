---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.00506v5
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1912.00506v5_A_generalization_of_combinatorial_identities_for_stable_discrete_series_constant

> Source: 1912.00506v5_A_generalization_of_combinatorial_identities_for_stable_discrete_series_constant.pdf

> Pages: 58

---


## Page 1


arXiv:1912.00506v5  [math.CO]  9 Feb 2022
A generalization of combinatorial identities
for stable discrete series constants
Richard EHRENBORG∗, Sophie MOREL†and Margaret READDY‡
February 11, 2022.
Abstract
This article is concerned with the constants that appear in Harish-Chandra’s character for-
mula for stable discrete series of real reductive groups, although it does not require any knowl-
edge about real reductive groups or discrete series. In Harish-Chandra’s work the only infor-
mation we have about these constants is that they are uniquely determined by an inductive
property. Later Goresky–Kottwitz–MacPherson and Herb gave diﬀerent formulas for these con-
stants; see [GKM97, Theorem 3.1] and [Her00, Theorem 4.2]. In this article we generalize these
formulas to the case of arbitrary ﬁnite Coxeter groups (in this setting, discrete series no longer
make sense), and give a direct proof that the two formulas agree. We actually prove a slightly
more general identity that also implies the combinatorial identity underlying the discrete series
character identities of Morel [Mor11, Proposition 3.3.1]. We deduce this identity from a general
abstract theorem giving a way to calculate the alternating sum of the values of a valuation on
the chambers of a Coxeter arrangement. We also introduce a ring structure on the set of valua-
tions on polyhedral cones in Euclidean space with values in a ﬁxed ring. This gives a theoretical
framework for the valuation appearing in [GKM97, Appendix A]. In Appendix B we extend the
notion of 2-structures (due to Herb) to pseudo-root systems. 1
Contents
1
Introduction
2
2
Hyperplane arrangements
5
2.1
Background material . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.2
Coxeter arrangements
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3
The abstract pizza quantity
9
3.1
2-structures and signs
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
3.2
Calculating the abstract pizza quantity with 2-structures . . . . . . . . . . . . . . . .
11
3.3
Proof of Theorem 3.2.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
∗University of Kentucky, Department of Mathematics, Lexington, KY 40506, USA.
richard.ehrenborg@uky.edu.
†UMPA UMR 5669 CNRS, ENS de Lyon site Monod, 46, all´ee d’Italie, 69364 Lyon Cedex 07, France.
sophie.morel@ens-lyon.fr.
‡University of Kentucky, Department of Mathematics, Lexington, KY 40506, USA.
margaret.readdy@uky.edu.
12020 MSC classiﬁcation: Primary 20F55, 17B22, 52C35; Secondary 52B45, 14G35, 14F43, 05E45, 06A07, 52B22.
1


## Page 2


4
The weighted sum
16
4.1
The weighted complex and the weighted sum
. . . . . . . . . . . . . . . . . . . . . .
16
4.2
Calculating the weighted sum for some arrangements with many symmetries . . . . .
19
4.3
First application: the case of Coxeter arrangements . . . . . . . . . . . . . . . . . . .
20
4.4
Second application: the type A identity involving ordered set partitions
. . . . . . .
21
4.5
Proof of Theorem 4.2.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
5
Properties of the weighted complex
27
5.1
Shellable polytopal complexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
5.2
A condition on hyperplane arrangements . . . . . . . . . . . . . . . . . . . . . . . . .
29
5.3
The case of Coxeter arrangements
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
6
Concluding remarks
31
A Extending the construction of a valuation by Goresky, Kottwitz and MacPherson 32
A.1 The ring of valuations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
A.2 Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
B Review of 2-structures
40
B.1
Pseudo-root systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
B.2
2-structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
42
B.3
Orthogonal sets of pseudo-roots and 2-structures . . . . . . . . . . . . . . . . . . . .
49
B.4
2-structures in the irreducible types
. . . . . . . . . . . . . . . . . . . . . . . . . . .
51
C Relationship with locally symmetric spaces
53
1
Introduction
Although this paper deals exclusively with the combinatorics of real hyperplane arrangements
and Coxeter complexes, it has its origin in the representation theory of real reductive groups and
its connections with the cohomology of locally symmetric spaces, and in particular, of Shimura
varieties. We start by explaining some of this background. This explanation can be safely skipped
by the reader not interested in Shimura varieties.
Let G be an algebraic group over Q. To simplify the exposition, we assume that G is connected
and semisimple. Let K8 be a maximal compact subgroup of GpRq and K be an open compact
subgroup of GpA8q, where A8 “ pZ bZ Q is the ring of ﬁnite ad`eles of Q. We consider the double
quotient XK “ GpQqzpGpRqˆGpA8qq{pK8ˆKq. This is a real analytic variety for K small enough,
and the projective system pXKqKĂGpA8q has an action of GpA8q by Hecke correspondences that
induces an action of the Hecke algebra at level K on the cohomology of XK for any reasonable
cohomology theory.
We restrict our attention further to the case where the real Lie group GpRq has a discrete series.
This is the so-called “equal rank case” because it occurs if and only if the groups GpRq and K8
have the same rank. Then the L2-cohomology H˚
p2qpXKq is ﬁnite-dimensional, and Matsushima’s
formula, proved in this generality by Borel and Casselman [BC83], gives a description of this
cohomology and of its Hecke algebra action in terms of discrete automorphic representations of G
2


## Page 3


whose inﬁnite component is a cohomological representation of GpRq, and in particular, either a
discrete series or a special type of non-tempered representation.
Another cohomology of interest in this case is the intersection cohomology IH˚pXKq of the
minimal Satake compactiﬁcation XK of XK. In order to study this cohomology, Goresky, Harder
and MacPherson introduced in [GHM94] a family of cohomology theories called “weighted coho-
mologies” and showed that the two middle weighted cohomologies agree with IH˚pXKq if XK has
the structure of a complex algebraic variety. This result was later generalized by Saper in [Sap18].
All the cohomology theories that we discussed have actions of the Hecke algebra, and the
isomorphism of the previous paragraph is equivariant for this action. Zucker conjectured that there
should be a Hecke-equivariant isomorphism between H˚
p2qpXKq and IHpXKq. This conjecture was
proved by Looijenga [Loo88], Looijenga–Rapoport [LR91] and Saper–Stern [SS90] if XK has the
structure of a complex algebraic variety and by Saper [Sap18] in general. In particular, by comparing
the formulas for the action of a Hecke operator on weighted cohomology (this was calculated by
Goresky and MacPherson using topological methods in [GM03]) and on L2-cohomology (this was
calculated by Arthur using the Arthur–Selberg trace formula in [Art89]), one can obtain a formula
for averaged discrete series characters of the group GpRq. One of the goals of the paper [GKM97]
of Goresky–Kottwitz–MacPherson was to prove this identity directly.
If moreover the space XK is the set of complex points of a Shimura variety, then it descends to
an algebraic variety over an explicit number ﬁeld E known as the reﬂex ﬁeld, as does the minimal
Satake compactiﬁcation, and so the intersection cohomology has a natural action of the absolute
Galois group GalpE{Eq. We can further complicate the calculation by trying to calculate the trace
on IH˚pXKq of Hecke operators twisted by elements of the group GalpE{Eq, for example, powers
of Frobenius maps. In the case where XK is a Siegel modular variety, this was done by the second
author in [Mor11]. It requires a slightly diﬀerent character identity for averaged discrete series
characters of GpRq, also involving discrete series characters of the endoscopic groups of G, and
whose relationship with the Goresky–Kottwitz–MacPherson identity was not clear.
For the specialists, we give a more detailed explanation of the relevance of our main results to
cohomology calculations in Appendix C. Let us return here to a discussion of the current article.
In a previous article of the authors [EMR19], we investigate the character identity of Morel [Mor11].
In particular we relate it to the geometry of the Coxeter complex of the symmetric group and give a
simpler and more natural proof than the brute force calculation in the appendix of [Mor11]. The goal
of the present article is to generalize the approach of [EMR19] and to prove a combinatorial identity
(Theorem 4.2.2) that implies the character formulas of Goresky–Kottwitz–MacPherson [GKM97]
and of Morel [Mor11] (see Subsections 4.3 and 4.4). To obtain the character formula of [GKM97]
from our results, we need to use Herb’s formula for averaged discrete series characters (see for ex-
ample [Her79] and [Her00]). We also generalize, in Corollary 5.2.3 and Lemma 5.3.1, the geometric
result of [EMR19] (see Theorem 4.3 of that article). In fact, we prove an identity that holds not
just for root systems that are generated by strongly orthogonal roots, but for all Coxeter systems
with ﬁnite Coxeter group. The representation-theoretic interpretation of our identity in the general
case is still unclear.
We now describe in more detail the diﬀerent sections of the article.
3


## Page 4


In Section 2 we review some background material about real hyperplane arrangements and
Coxeter arrangements.
In Section 3 we prove our ﬁrst main theorem (Theorem 3.2.1) that concerns the calculation over
the chambers T of a Coxeter arrangement H of the alternating sum of quantities fpTq, where f is
a valuation deﬁned on closed convex polyhedral cones. More precisely, Theorem 3.2.1 reduces this
calculation to a similar calculation for simpler subarrangements of H and it is the main ingredient
in the proof of our second main theorem (Theorem 4.2.2). The original proof of Theorem 4.2.2
used an induction similar to the ones used in the proofs of the character identities of [GKM97,
Theorem 3.1] and [Her00, Theorem 4.2], but we later realized that Theorem 4.2.2 was a particular
case of the more general identity of Theorem 3.2.1.
In Section 4 we state and prove our second main theorem (Theorem 4.2.2). We ﬁrst introduce
in Subsection 4.1 our main geometric construction, which we call the weighted complex, that allows
us to deﬁne the weighted sum; see Remark 4.1.6 for an explanation of these names. The weighted
complex is the set of all the faces of a ﬁxed hyperplane arrangement that are on the nonnegative side
of an auxiliary hyperplane Hλ. It contains what is known as the bounded complex in the theory of
aﬃne oriented matroids, and coincides with it if Hλ is in general position. We state Theorem 4.2.2 in
Subsection 4.2 and prove it in Subsection 4.5. The proof is straightforward: Using Corollary A.1.8,
which generalizes [GKM97, Proposition A.4], to reinterpret the weighted sum as an alternating
sum on the chambers of the arrangement of the value of a particular valuation, we are able to show
that Theorem 4.2.2 is a particular case of Theorem 3.2.1. In Subsections 4.3 and 4.4 we explain
how Theorem 4.2.2 implies the identities of [GKM97, Theorem 3.1] and of [EMR19, Theorem 6.4].
In Section 5, we study the geometric properties of the weighted complex. We prove in particular
that, under a hypothesis about the dihedral angles between the hyperplanes of the arrangement
(Condition (A) in Subsection 5.2, which always holds in the Coxeter case), the weighted complex
is shellable; see Corollary 5.2.3, which generalizes Theorem 4.3 of [EMR19].
We consider the
case of Coxeter arrangements in Subsection 5.3. These geometric results were originally needed in
the proof of Theorem 4.2.2, but the new proof via Theorem 3.2.1 allows us to circumvent them.
We nevertheless decided to keep them in the article because we thought that they could be of
independent interest.
In Section 6 we include concluding remarks.
We ﬁnish with three appendices. Each of the ﬁrst two appendices can be read independently
from the rest of the article (except that a proof in Appendix A uses Lemma 2.1.3). The goal of
our Appendix A is to generalize [GKM97, Proposition A.4], which is a key part in the proof of our
main theorem. In Appendix A of their article [GKM97], Goresky–Kottwitz–MacPherson show that
a certain function, which they call ψCpx, λq, is a valuation (see Deﬁnition A.1.3) on closed convex
polyhedral cones, although they do not phrase it in these terms. We show that their function is
a special case of a general construction that takes two valuations and produces a third one, and
that this operation makes the set of valuations on closed convex polyhedral cones into a ring. See
Theorem A.1.6 and its corollaries for the precise deﬁnition of this operation.
In Appendix B we review the theory of 2-structures, due to Herb; see for example Herb’s review
article [Her00]. We believe that this will be useful to the reader for a number of reasons. The proofs
of the fundamental results of this theory are somewhat scattered in the literature and sometimes
left as exercises. Furthermore, we needed to slightly adapt a number of results so that they continue
to hold for Coxeter systems that do not necessarily arise from a (crystallographic) root system.
Finally, Appendix C is a continuation of the ﬁrst part of the introduction, and is intended to give
4


## Page 5


specialists more information about the way the weighted sum of Deﬁnition 4.1.5 and Theorem 4.2.2
appear in the calculation of the cohomology of locally symmetric varieties.
2
Hyperplane arrangements
2.1
Background material
We ﬁx a ﬁnite-dimensional R-vector space V with an inner product p¨, ¨q. If α P V , we write
Hα “ tx P V : pα, xq “ 0u,
H`
α “ tx P V : pα, xq ą 0u,
H´
α “ tx P V : pα, xq ă 0u.
We also denote by sα the (orthogonal) reﬂection across the hyperplane Hα.
Let pαeqePE be a ﬁnite family of nonzero vectors in V . The corresponding (central) hyperplane
arrangement is the family of hyperplanes H “ pHαeqePE. Let V0 be the intersection of all the
hyperplanes, that is, V0 “ Ş
ePE Hαe. We say that the arrangement H is essential if V0 “ t0u,
which means that the family pαeqePE spans V .
Consider the map s : V ÝÑ t`, ´, 0uE sending x P V to the family psignppαe, xqqqePE, where
sign : R ÝÑ t`, ´, 0u is the map sending positive numbers to `, negative numbers to ´ and zero
to 0.
Remark 2.1.1. The image of the map s : V ÝÑ t`, ´, 0uE is the set of covectors of an oriented
matroid (see for example [Bj¨o+99, Deﬁnition 4.1.1]). This is the oriented matroid corresponding to
the hyperplane arrangement. In fact, some of our results extend to general oriented matroids. In
this article we have chosen to concentrate on hyperplane arrangements to keep the exposition more
concrete. In particular, we do not assume that the reader knows what an oriented matroid is.
We denote by L pHq or just L the set of nonempty subsets of V of the form C “ s´1pXq,
for a sign vector X P t`, ´, 0uE. The elements of L are called faces of the arrangement. The
set L has a natural partial order given by C ď D if and only if C Ď D. The relation C ď D
is equivalent to the fact that for every e P E we have spCqe “ 0 or spCqe “ spDqe. The set L
with this partial order is called the face poset of the arrangement. Note that V0 is the minimal
element of L . When we adjoin a maximal element p1 to the poset L , we obtain a lattice L Y tp1u
known as the face lattice.
Note that under our convention faces other than V0 are not closed
subsets of V : for every C P L , the closure C is a closed convex polyhedral cone in V , and it is an
intersection of closed half-spaces H˘
αe. The poset L is graded with the rank of a face C P L given
by ρpCq “ dimpCq ´ dimpV0q, where we write dimpCq for dimpSpanpCqq.
We denote by T pHq or just T the set of maximal faces of L . These elements are often called
chambers, regions or topes, and are the connected components of V ´ Ť
ePE Hαe. If T P T then T
is an open subset of V , and its closure is a closed convex polyhedral cone of dimension dimpV q.
If X, Y P t`, ´, 0uE, their composition X ˝ Y is the sign vector deﬁned by
pX ˝ Y qe “
#
Xe
if Xe ‰ 0,
Ye
otherwise.
If C, D P L then spCq ˝ spDq is also the image of a face of L , and we denote this face by C ˝ D.
This is the unique face of L that contains all vectors of V of the form x ` εy, with x P C, y P D
and ε ą 0 suﬃciently small (relative to x and y). Deﬁne the separation set of C and D to be the
set
SpC, Dq “ te P E : spCqe “ ´spDqe ‰ 0u.
5


## Page 6


This is the set of e P E such that C and D are on diﬀerent sides of the hyperplane Hαe.
Fix a chamber B P T . We can then deﬁne a partial order ĺB on T by declaring that T ĺB T 1 if
and only if SpB, Tq Ď SpB, T 1q. The resulting poset is called the chamber poset with base chamber B.
We will denote it by TB. It is a poset with minimal element B and maximal element ´B. When
all the hyperplanes are distinct, this poset is also graded with the rank function ρpTq “ |SpB, Tq|;
see [Bj¨o+99, Proposition 4.2.10].
If the choice of the base chamber B is understood, we write, for every face C of the arrangement,
p´1qC “ p´1q|SpB,C˝Bq|.
We also consider the graph with vertex set T , where two chambers T, T 1 P T are connected
by an edge if and only if T X T
1 spans a hyperplane (necessarily one of the hyperplanes Hαe). In
this situation, we say that this hyperplane is a wall of the chambers T and T 1. This graph is called
the chamber graph. In the case when all the hyperplanes of the arrangement H are distinct, the
distance between two chambers T and T 1 in this graph is |SpT, T 1q|; see [Bj¨o+99, Proposition 4.2.3].
Consider the sphere S of center 0 and radius 1 in V {V0. The intersections C X S, for C P L ,
form a regular cell decomposition ΣpL q of S, and we will identify L with the face poset of this
regular cell decomposition.
Finally, we recall the deﬁnition of the star of a face in L .
Deﬁnition 2.1.2. Let C P L . The star of C in L is tD P L : C ď Du. Geometrically it is the
set of faces of L whose closure contains C. We will denote it by LěC.
Lemma 2.1.3. Let C P L and let EpCq “ te P E : C Ă Hαeu. Consider the hyperplane arrange-
ment HpCq “ pHαeqePEpCq and let LHpCq be its face poset. Then the following four statements
hold:
(i) Each face D of L is contained in a unique face D1 of LHpCq, and the map D ÞÝÑ D1 induces
an isomorphism of posets ιC : LěC
„
ÝÑ LHpCq.
In particular, it sends the chambers of
T X LěC to the chambers of LHpCq.
(ii) The isomorphism ιC of (i) sends a face D ě C of H to the relative interior of the closed
convex polyhedral cone D ` SpanpCq. Let CC “ Ş
ePE´EpCq Hǫe
e , where ǫe “ spCqe.
The
inverse of the isomorphism ιC sends a face D1 of HpCq to the intersection D1 X CC.
(iii) If D1, D2 P LěC then the inclusion SpD1, D2q Ă EpCq holds. In particular, we have the
equality SpD1, D2q “ SpιCpD1q, ιCpD2qq, where the isomorphism ιC is as in (i).
(iv) The isomorphism ιC : LěC
„
ÝÑ LHpCq preserves composition and dimension, that is, for all
D, D1 P LěC, the identities ιCpD ˝ D1q “ ιCpDq ˝ ιCpD1q and dimpιCpDqq “ dimpDq hold.
In particular, LěC is also isomorphic to the face poset of a regular cell decomposition of the
unit sphere in V { Ş
ePEpCq Hαe that we denote by ΣpLěCq.
Proof of Lemma 2.1.3. Statement (i) is clear.
We prove statement (ii). Let D P LěC and let D1 “ ιCpDq. As C ď D, we have spDqe “ spCqe
for every e P E ´ EpCq, and so D Ă CC. As D Ă D1, we deduce that D1 X CC Ą D. As D1 is a
face of HpCq, hence an intersection Ş
ePEpCq Hse
αe with se P t0, `, ´u, the intersection D1 X CC is
either empty or a face of H. We have just proved that this intersection contains D, so it is not
6


## Page 7


empty and hence is equal to the face D of H. It remains to prove that D1 is the relative interior of
D`SpanpCq. We write D “ Ş
ePE0 Hα0XŞ
ePE` H`
αeXŞ
ePE´ H´
αe, with E “ E0\E`\E´. We then
have E0 Ă EpCq, and D1 is equal to Ş
ePE0 Hα0 XŞ
ePE`XEpCq H`
αe XŞ
ePE´XEpCq H´
αe. So it suﬃces
to show that D`SpanpCq “ K, where K “ Ş
ePE0 Hα0 XŞ
ePE`XEpCq H
`
αe XŞ
ePE´XEpCq CH´
αe. We
clearly have D Ă K and SpanpCq Ă K, so D ` SpanpCq Ă K. Conversely, let x P K and let y P C.
Then pαe, yq ‰ 0 for every e P E ´ EpCq, so there exists λ ą 0 such that pαe, λyq ` pαe, xq has the
same sign as pαe, yq for every e P E ´ EpCq. We then have λx ` y P D, and so x P D ` SpanpCq.
We prove (iii). Let D1, D2 P LěC, and let e P SpD1, D2q. Suppose for example that spD1qe “ `
and spD2qe “ ´. (The other case is similar.) Then D1 Ă H`
αe and D2 Ă H´
αe, so C Ă D1 X D2 Ă
H`
αe X H´
αe “ Hαe, which implies that e P EpCq.
The ﬁrst statement of (iv) follows easily from the deﬁnitions: the composition D ˝ D1 is deﬁned
on the sign vectors of D and D1, and the isomorphism ιC just forgets the coordinates outside
of EpCq in these sign vectors.
We prove the second statement of (iv). Let D P LěC, and let D1 be the unique face of LHpCq
containing D. We clearly have dimpDq ď dimpD1q. If dimpD1q ą dimpDq then there exists e P E
such that D Ă Hαe and D1 Ć Hαe. But C Ă D, so this implies that e P EpCq. As D1 is not
included in Hαe, it must be contained in one of the open half-spaces H˘
αe, contradicting the fact
that D1 contains D.
Remark 2.1.4. Let C P L and let F 1 “ te P E : C Ć Hαeu. Then the set T X LěC is equal
to tT P T : @e P F 1 spTqe “ spCqeu, so it is a T-convex subset of T in the sense of [Bj¨o+99,
Deﬁnition 4.2.5]; see [Bj¨o+99, Proposition 4.2.6]. In other words, it contains every shortest path
in the chamber graph between any two of its elements, so it is a lower order ideal in TB for every
choice of base chamber B P T X LěC.
2.2
Coxeter arrangements
Let pW, Sq be a Coxeter system, that is, W is the group generated by the set S and the relations
between the generators are of the form pstqms,t “ 1 where ms,s “ 1 and ms,t ě 2 for s ‰ t;
see [BB05, Section 1.1]. The corresponding Coxeter graph has vertex set S, and two generators s
and t are connected with an edge if ms,t ě 3. If ms,t ě 4 it is customary to label the edge by the
integer ms,t.
There are three natural partial orders on the elements of the Coxeter group W. First the strong
Bruhat order is deﬁned by the following cover relation: z ă w if there exists s P S and u P W such
that pusu´1qz “ w and ℓpzq`1 “ ℓpwq where ℓis the length function on W; see for example [BB05,
Deﬁnition 2.1.1]. Next, we have the right (respectively left) weak Bruhat order, where the cover
relation is z ă w if there exists s P S such that z ¨s “ w (respectively s¨z “ w) and ℓpzq`1 “ ℓpwq.
The strong Bruhat order reﬁnes both the left and right weak Bruhat orders.
Let V “ À
sPS Res, with the symmetric bilinear form p¨, ¨q deﬁned by
pes, etq “ ´ cos pπ{ms,tq .
In particular, pes, esq “ 1. The canonical representation of pW, Sq is the representation of W on V
given by
spvq “ v ´ 2 ¨ pes, vq ¨ es,
(2.1)
7


## Page 8


for every s P S and every v P V . Note that this formula deﬁnes an orthogonal isomorphism of V for
the symmetric bilinear form p¨, ¨q. We refer the reader to [Bou68, Chapitre V, § 4, №8, Th´eor`eme 2
p. 98] for the next result.
Theorem 2.2.1. Equation (2.1) deﬁnes a faithful representation of W on V , and the form p¨, ¨q is
positive deﬁnite if and only if W is ﬁnite.
From now on, we assume that W is ﬁnite, and we write Φ “ twpesq : w P W, s P Su and
Φ` “ Φ X ř
sPS Rě0es. The set Φ is a pseudo-root system, its subset Φ` is a set of positive pseudo-
roots, and the set Φ´ “ ´Φ` “ Φ ´ Φ` is the corresponding set of negative pseudo-roots; see
Deﬁnitions B.1.1 and B.1.4. Then H “ pHαqαPΦ` is an essential hyperplane arrangement on V .
The set of chambers T of this arrangement is in canonical bijection with W: the unit element
1 P W corresponds to the chamber B “ Ş
αPΦ` H`
α “ Ş
sPS H`
es, and an arbitrary element w of W
corresponds to the chamber wpBq.
More generally, a parabolic subgroup of W is a subgroup WI generated by a subset I of S, and
the left cosets of parabolic subgroups of W are called standard cosets. The Coxeter complex ΣpWq
of W is the set of standard cosets of W ordered by reverse inclusion. It is a simplicial complex,
and we have an isomorphism of posets from ΣpWq to the face poset L of H sending a standard
coset wWI to the cone tx P V : @s P I px, wpesqq “ 0 and @s P S ´ I px, wpesqq ą 0u. The fact that
this is an isomorphism is proved in [Bou68, Chapitre V § 4 №6 pp. 96–97], since the representation
of W on V _ is isomorphic to its canonical representation on V by Theorem 2.2.1. The fact that
ΣpWq is a simplicial complex then follows from [Bou68, Chapitre V § 3 №3 Proposition 7 p. 85].
The deﬁnitions of B and of the isomorphism T » W imply that, if w, w1 P W and Tw, Tw1 P T
are the corresponding chambers, then
SpTw, Tw1q “ tα P Φ` : w´1pαq P Φ` and w1´1pαq P Φ´u
Y tα P Φ` : w´1pαq P Φ´ and w1´1pαq P Φ`u,
and in particular
SpB, Twq “ tα P Φ` : w´1pαq P Φ´u,
hence, by [BB05, Proposition 4.4.4],
p´1qTw “ p´1q|SpB,Twq| “ detpwq.
By [BB05, Propositions 3.1.3 and 4.4.6] this also implies that the isomorphism T » W sends the
partial order ĺB to the right weak Bruhat order on W.
Deﬁnition 2.2.2. Let H “ pHαeqePE be a ﬁnite hyperplane arrangement on a ﬁnite-dimensional
real inner product space V , with inner product denoted by p¨, ¨q.
We say that H is a Coxeter
arrangement if αe R Rαf for distinct e, f P E and if for every e P E the family of hyperplanes H is
stable by the (orthogonal) reﬂection sαe across Hαe.
Theorem 2.2.3. The hyperplane arrangement associated to a Coxeter system with ﬁnite Coxeter
group is a Coxeter arrangement.
Conversely, suppose that H is a Coxeter arrangement on an
inner product space V , and that there exists a chamber B of H that is on the positive side of each
hyperplane in H. Let W be the subgroup of GLpV q generated by the set tsαe : e P Eu, let F be the
set of e P E such that B X Hαe is a facet of B and let S “ tsαf : f P Fu. Then pW, Sq is a Coxeter
system, the group W is ﬁnite, and the hyperplane arrangement induced by H on V { Ş
ePE Hαe is
isomorphic to the arrangement associated to the Coxeter system pW, Sq.
8


## Page 9


Proof. The ﬁrst statement is an immediate consequence of the deﬁnition of the arrangement asso-
ciated to a Coxeter system. The second and fourth statements follow from [Bou68, Chapitre V § 3
№2 Th´eor`eme 1 p. 74]. The statement that W is ﬁnite follows from [Bou68, Chapitre V § 3 №7
Proposition 4 p. 80] and from the fact that the arrangement H is central.
3
The abstract pizza quantity
3.1
2-structures and signs
Let Φ Ă V be a pseudo-root system (see Deﬁnition B.1.1) with Coxeter group W (see Proposi-
tion B.1.6) and Φ` Ă Φ be a system of positive pseudo-roots (see Deﬁnition B.1.4). Recall the
deﬁnition of 2-structures from Subsection B.2: A 2-structure for Φ is a subset ϕ Ď Φ such that:
(a) ϕ is a pseudo-root system whose irreducible components are all of type A1, B2 or I2p2kq with
k ě 3;
(b) for every w P W such that wpϕ X Φ`q “ ϕ X Φ`, we have detpwq “ 1.
Recall that T pΦq is the set of 2-structures for Φ. By Proposition B.2.4, the group W acts
transitively on T pΦq. In Deﬁnition B.2.8 we deﬁne the sign ǫpϕq “ ǫpϕ, Φ`q of any 2-structure
ϕ P T pΦq. If ϕ P T pΦq, we write ϕ` “ ϕ X Φ`.
We have the following proposition that extends [Her01, Theorem 5.3] to the case of Coxeter
systems. Note that our proof is a simple adaptation of Herb’s proof.
Proposition 3.1.1. The sum of the signs of all 2-structures of a pseudo-root system is equal to 1,
that is,
ÿ
ϕPT pΦq
ǫpϕq “ 1.
Proof. We prove the result by induction on |Φ|. It is clear if Φ “ ∅, because then T pΦq “ t∅u and
the sign of ∅is 1. Suppose that |Φ| ě 1 and that we know the result for all pseudo-root systems
of smaller cardinality. Let α P Φ, and set Φα “ αK X Φ; this is a pseudo-root system with positive
system αK X Φ`.
Let T 2 “ tϕ P T pΦq : sαpϕq “ ϕu. By statement (0) of Lemma B.2.11, we have T 2 “ tϕ P
T pΦq : α P ϕu. If ϕ R T 2, then ϕ` Ă Φ` ´ tαu, so sαpϕ`q Ă Φ` by Lemma 4.4.3 of [BB05], hence
ǫpsαpϕqq “ ´ǫpϕq by Lemma B.2.10. This implies that ř
ϕPT pΦq´T 2 ǫpϕq “ 0.
We deﬁne subsets T 2
1 and T 2
2 of T 2 by
T 2
1 “ tϕ P T pΦq : ϕ X Φα P T pΦαqu,
T 2
2 “ T 2 ´ T 2
1 .
By (3) of Lemma B.2.11, there exists an involution ι of T 2
2 such that, for every ϕ P T 2
2 , we have
that ιpϕq X Φα “ ϕ X Φα and ǫpιpϕqq “ ´ǫpϕq. This implies that
ÿ
ϕPT 2
2
ǫpϕq “ 0,
9


## Page 10


and so
ÿ
ϕPT pΦq
ǫpϕq “
ÿ
ϕPT 2
1
ǫpϕq.
Finally, by (1) and (2) of Lemma B.2.11, the map ϕ ÞÝÑ ϕ X Φα induces a bijection from T 2
1
to T pΦαq, and we have ǫpϕq “ ǫpϕ X Φαq for every ϕ P T 2
1 . Hence we obtain
ÿ
ϕPT 2
1
ǫpϕq “
ÿ
ϕ0PT pΦαq
ǫpϕ0q,
and this last sum is equal to 1 by the induction hypothesis.
Remark 3.1.2. As we are using the deﬁnition of the sign of a 2-structure from [Her83], our formula
looks a bit diﬀerent from the one of [Her01, Theorem 5.3]. This is explained in [Her01, Remark 5.1],
and we generalize the comparison between the two deﬁnitions of the sign in Corollary 3.1.3 below.
Corollary 3.1.3. Let ϕ P T pΦq, Wpϕ, Φ`q “ tw P W : wpϕ`q Ă Φ`u and W1pϕ, Φ`q “ tw P W :
wpϕ`q Ă ϕ`u. Then the sign ǫpϕ, Φ`q is given by
ǫpϕ, Φ`q “
1
|W1pϕ, Φ`q|
ÿ
wPW pϕ,Φ`q
detpwq.
Proof. By Corollary B.2.5 we have a bijection Wpϕ, Φ`q{W1pϕ, Φ`q ÝÑ T pΦq, w ÞÝÑ wpϕq. By
Proposition 3.1.1 and Lemma B.2.10, we obtain
1 “
1
|W1pϕ, Φ`q|
ÿ
wPW pϕ,Φ`q
ǫpwpϕq, Φ`q “ ǫpϕ, Φ`q
1
|W1pϕ, Φ`q|
ÿ
wPW pϕ,Φ`q
detpwq.
We consider the hyperplane arrangement H “ pHαqαPΦ` corresponding to Φ, with base chamber
B “ Ş
αPΦ` H`
α . For every 2-structure ϕ P T pΦq, we denote by Hϕ the hyperplane arrangement
pHαqαPϕ`, with base chamber Bϕ “ Ş
αPϕ` H`
α . If T is a chamber of H, we denote by ZϕpTq the
unique chamber of Hϕ containing T; as ϕ` Ă Φ`, we have ZϕpBq “ Bϕ.
Corollary 3.1.4. For every chamber T of H, we have
p´1qT “
ÿ
ϕPT pΦq
p´1qZϕpTqǫpϕq.
Recall that p´1qT “ p´1q|SpB,Tq| for every T P T pHq, and similarly for T P T pHϕq.
Proof of Corollary 3.1.4. For every ϕ P T pΦq, we denote the Coxeter group of ϕ by Wpϕq. We also
use the notation of Lemma B.2.10. Let w be the unique element of W such that T “ w´1pBq. Let
ϕ P T pΦq. Then ϕ X wpΦ`q is a system of positive pseudo-roots in ϕ, so there exists a unique v P
Wpϕq such that vpϕ`q “ ϕXwpΦ`q; we write v “ vϕpwq. As T “ tx P V : @α P wpΦ`qpx, αq ą 0u,
we have
ZϕpTq “ tx P V : @α P wpΦ`q X ϕ px, αq ą 0u
“ tx P V : @α P vϕpwqpϕq px, αq ą 0u,
10


## Page 11


and so vϕpwq is the element of Wpϕq corresponding to ZϕpTq by the bijection from Wpϕq to the
set of chambers of Hϕ sending v to v´1pZϕpBqq.
For a 2-structure ϕ P T pΦq we have that w´1vϕpwqpϕ`q “ w´1pϕ X wpΦ`qq Ă Φ`, so by
Lemma B.2.10 (and the fact that vϕpwqpϕq “ ϕ), we obtain that
ǫpw´1pϕqq “ detpw´1vϕpwqqǫpϕq.
Hence we have
ÿ
ϕPT pΦq
p´1qZϕpTqǫpϕq “
ÿ
ϕPT pΦq
detpvϕpwqqǫpϕq
“ detpwq ¨
ÿ
ϕPT pΦq
ǫpw´1pϕqq
“ detpwq ¨
ÿ
ϕPT pΦq
ǫpϕq,
where in the last step we used that the map ϕ ÞÝÑ w´1pϕq on the set T pΦq is bijective. The result
now follows by Proposition 3.1.1.
3.2
Calculating the abstract pizza quantity with 2-structures
We use the notation of Appendix A. In particular, if K is a closed convex polyhedral cone in V , we
denote the set of its closed faces by FpKq (we include K itself in the set of its faces). The dimension
dim K of K is by deﬁnition the dimension of its span SpanpKq, and the relative interior ˚
K of K
is the interior of K in SpanpKq. We say that K is degenerate if SpanpKq is strictly included in V ,
equivalently, if K has empty interior.
Let H be a central hyperplane arrangement on V with ﬁxed base chamber B. Let CHpV q be
the set of closed convex polyhedral cones in V that are intersections of closed half-spaces bounded
by hyperplanes H where H P H. Denote the free abelian group on CHpV q by À
KPCHpV q ZrKs and
let KHpV q be its quotient by the relations rKs ` rK1s “ rK Y K1s ` rK X K1s for all K, K1 P CHpV q
such that K Y K1 P CHpV q. For K P CHpV q, we still denote the image of K in KHpV q by rKs. For
the relative interior ˚
K we also deﬁne a class r˚
Ks P KHpV q by
r˚
Ks “ p´1qdim K
ÿ
F PFpKq
p´1qdim FrFs.
We then have
rKs “
ÿ
F PFpKq
r˚
Fs
by formula (A.4) on page 543 of [GKM97].
Recall that L pHq and T pHq are the set of faces and chambers of the arrangement H as in
Subsection 2.1. Each C P L pHq is the relative interior of its closure and, if T P T pHq, then
FpTq “ tC : C P L pHq, C ď Tu. We have V “ š
CPL pHq C, and the family prCsqCPL pHq is a Z-
basis of KHpV q. As in Section 2.1, the sign of a face C P FpHq is deﬁned by p´1qC “ p´1q|SpB,C˝Bq|.
We consider the following quantity:
ΠpHq “
ÿ
CPL pHq
p´1qCrCs P KHpV q.
11


## Page 12


Let A be an abelian group. We say that a function ν : CHpV q ÝÑ A is a valuation on CHpV q if,
for all K, K1 P CHpV q such that K Y K1 P CHpV q we have νpK Y K1q ` νpK X K1q “ νpKq ` νpK1q.
Such a valuation ν deﬁnes a morphism of abelian groups KHpV q ÝÑ A sending rKs to νpKq for
every K P CHpV q, and we still denote this morphism by ν : KHpV q ÝÑ A. We set
ΠpH, νq “ νpΠpHqq P A.
If ν vanishes on degenerate cones then we have
ΠpH, νq “
ÿ
TPT pHq
p´1qT νpTq “
ÿ
TPT pHq
p´1qT νpTq P A.
(3.1)
The ﬁrst main theorem of this article is the following. For Coxeter arrangements we can express
the quantity ΠpHq in terms of the quantities ΠpHϕq for the arrangements Hϕ associated to the
2-structures of the arrangement.
Theorem 3.2.1. Let Φ Ă V be a pseudo-root system. Choose a system of positive pseudo-roots
Φ` Ă Φ and let H be the hyperplane arrangement pHαqαPΦ` on V .
(i) We have the identity
ΠpHq “
ÿ
ϕPT pΦq
ǫpϕqΠpHϕq
in the quotient KHpV q, where Hϕ is as before the arrangement pHαqαPϕXΦ` for every ϕ P
T pΦq.
(ii) If ν : CHpV q ÝÑ A is a valuation, we have
ΠpH, νq “
ÿ
ϕPT pΦq
ǫpϕqΠpHϕ, νq.
If ϕ P T pΦq then the faces of Hϕ are relative interiors of elements of CHpV q, so ΠpHϕq makes
sense as an element of KHpV q.
Remark 3.2.2. This theorem is useful in the following situation. Suppose that we have a function f
on closed convex polyhedral cones and that we wish to calculate the alternating sum over the
chambers T of a hyperplane arrangement H of the values fpTq. If H is a Coxeter arrangement and
the function f is a valuation that vanishes on cones contained in hyperplanes of H, then the theorem
says that we can reduce the problem to a similar calculation for very simple subarrangements of H
that are products of rank 1 and rank 2 Coxeter arrangements.
Here are two situations when we wish to calculate alternating sums of fpTq for such a valua-
tion f:
(a) The weighed sums of Section 4. These sums appear in the calculation of weighted cohomology
of locally symmetric spaces and Shimura varieties (see Appendix C for additional details and
references).
We want to relate them to stable discrete series constants to get a spectral
description of that cohomology.
12


## Page 13


(b) The pizza problem (see for example the paper [EMR21b]). In this setting, we ﬁx a measurable
subset K of V with ﬁnite volume, and the function f sends a cone C to the volume of C XK.
We are interested in “the pizza quantity”, that is, the alternating sum of the volumes fpKXTq.
In particular we would like to know when this alternating sum vanishes, which is to say that
the “pizza” K has been evenly divided among the two participants, ` and ´. This problem is
approached by analytic methods in [EMR21b]. Theorems 1.1 and 1.2 in [EMR21b] give general
suﬃcient conditions to guarantee that the pizza quantity vanishes. Using Theorem 3.2.1 we
can give a dissection proof; see [EMR21a].
When f is a valuation that does not vanish on cones contained in hyperplanes of H, we have
to decide how to count the contributions of lower-dimensional faces of H. One possibility is given
in Theorem 3.2.1, and another in Corollary 3.2.4. In both cases, if H is a Coxeter arrangement,
then we can again reduce the calculation to the case of simpler subarrangements of H. This is not
needed in situation (a), but in situation (b) it allows us to obtain versions of the pizza theorem
that hold for all the intrinsic volumes. See [EMR21a] for this.
We will provide a proof of Theorem 3.2.1 in Subsection 3.3. First we state and prove a corollary.
For H a central hyperplane arrangement on V with a ﬁxed base chamber, we deﬁne
PpHq “
ÿ
TPT pHq
p´1qT rTs P KHpV q,
P0pHq “
ÿ
TPT pHq
p´1qT rTs P KHpV q.
Analogous to the pizza quantity deﬁned in Section 2 of [EMR21b], we call PpHq the abstract pizza
quantity of the arrangement H.
Lemma 3.2.3. For H a central hyperplane arrangement on V , we have
P0pHq “ PpHq.
Proof. If T P T pHq then we have
rTs “ rTs `
ÿ
F PL pHq
F ăT
rFs.
Summing over all chambers T of H yields
ÿ
TPT pHq
p´1qT rTs “
ÿ
TPT pHq
p´1qT
¨
˚
˚
˝rTs `
ÿ
F PL pHq
F ăT
rFs
˛
‹‹‚
“
ÿ
TPT pHq
p´1qT rTs `
ÿ
F PL pHq´T pHq
rFs
ÿ
TPT pHq
TąF
p´1qT .
The last inner sum is equal to zero, yielding the result.
13


## Page 14


Corollary 3.2.4. If Φ and H are as in Theorem 3.2.1, we have
PpHq “
ÿ
ϕPT pΦq
ǫpϕqPpHϕq.
Proof. By Lemma 3.2.3, it suﬃces to prove that
P0pHq “
ÿ
ϕPT pΦq
ǫpϕqP0pHϕq,
where P0pHq “ ř
TPT pHqp´1qT rTs and P0pHϕq is deﬁned similarly. For every x P V and every
ϕ P T pΦq, let aϕpxq equal p´1qZ if there exists a chamber Z of ϕ such that x P Z, and 0 otherwise.
We need to show that ř
ϕPT pΦq ǫpϕqaϕpxq is equal to p´1qT if there exists a chamber T of H such
that x P T, and otherwise is zero.
Consider the valuation ν : CHpV q Ñ KHpV q sending a cone C P CHpV q to ř
TPT pHq, TĂCrTs P
KHpV q. This valuation corresponds to the endomorphism of KHpV q sending the class of T to itself
if T P T pHq, and the class of F to 0 if F P FpHq ´ T pHq. The valuation ν vanishes on degenerate
cones, so by statement (ii) of Theorem 3.2.1 and equation (3.1), we have that if T is a chamber
of H and x P T then ř
ϕPT pΦq ǫpϕqaϕpxq “ p´1qT .
Now let x P V ´ Ť
TPT pHq T, and let F be the unique face of H such that x P F. For each
ϕ P T pΦq, there is at most one chamber of ϕ that contains x. We denote by X the set of pairs pϕ, Zq,
where ϕ P T pΦq and Z is a chamber of ϕ such that x P Z. As F is not a chamber, there exists e P E
such that F Ă He. We denote by s the orthogonal reﬂection in the hyperplane He. As spxq “ x,
we can make s act on X by sending pϕ, Zq to pspϕq, spZqq. This is a ﬁxed-point free involution.
Indeed, if ϕ is a 2-structure such that spϕq “ ϕ, then e P ϕ by statement (0) of Lemma B.2.11,
so He is a hyperplane of Hϕ, which is impossible because x is both in He and in a chamber of ϕ.
To prove that ř
ϕPT pΦq ǫpϕqaϕpxq “ ř
pϕ,ZqPX ǫpϕqp´1qZ is equal to 0, it suﬃces to show that for
every pϕ, Zq P X we have ǫpϕqp´1qZ “ ´ǫpspϕqqp´1qspZq. After applying an element of W to the
whole situation, we may assume that x is in the base chamber of H. Then Z, respectively spZq,
is the base chamber of ϕ, respectively spϕq, so p´1qZ “ p´1qspZq “ 1. Also, as the reﬂection s
sends the base chamber of ϕ to that of spϕq, we have spϕ`q Ă Φ`, and so ǫpspϕqq “ ´ǫpϕq by
Lemma B.2.10.
3.3
Proof of Theorem 3.2.1
In this subsection we prove Theorem 3.2.1. We begin by stating and proving a lemma.
Lemma 3.3.1. Let H be a central hyperplane arrangement on V , let C be a face of H and let
x P V . We denote by C0 the unique face of H containing x. Then for D ď C a face of H the
following three conditions are equivalent:
(a) x P C ` SpanpDq “ C ` SpanpDq;
(b) ψxpD
K,Cq “ 1, where D
K,C “ D
K X C
˚ as in Subsection A.1;
(c) D ˝ C0 ď C.
14


## Page 15


Moreover, if C0 is a chamber then these conditions can only hold if C is also a chamber, and they
are equivalent to the following condition:
(d) D ˝ C0 “ C.
Proof. We ﬁrst note that SpanpDq “ SpanpDq because SpanpDq is a ﬁnite-dimensional subspace
of V , hence it is closed and so contains D. This explains the equality in condition (a).
To prove that conditions (a) and (b) are equivalent, we note that by the deﬁnition of the
valuation ψx in Lemma A.1.10 we have ψxpD
K,Cq “ 1 if and only if x P pD
K,Cq˚. As D
K,C “ D
KXC
˚
by deﬁnition, we have pD
K,Cq˚ “ SpanpDq ` C, so condition (b) is equivalent to the fact that
x P SpanpDq ` C, which is condition (a).
We prove that (c) implies (a). Let y P D. If ε ą 0 then y ` εx P D ˝ C0, so y ` εx P C by (c).
Thus x “ 1
εpy ` εx ´ yq P C ` SpanpDq, which is condition (a).
We prove that (a) implies (c). By condition (a) we can write x “ x1 ` x2, with x1 P C and
x2 P SpanpDq. Let y P D. If ε ą 0 is small enough then y`εx2 P D, so y`εx “ py`εx2q`εx1 P C.
As y ` εx P D ˝ C0 for ε ą 0 small enough, this shows that D ˝ C0 Ă C, that is, D ˝ C0 ď C, which
is condition (a).
Finally, suppose that C0 is a chamber. Then D ˝ C0 is a chamber, so condition (c) can only
hold if C is also a chamber, and it is equivalent to condition (d) because chambers are maximal
faces.
Proof of Theorem 3.2.1. We ﬁrst prove statement (ii) of Theorem 3.2.1 for a valuation ν : CHpV q ÝÑ
A that vanishes on degenerate cones. For every ϕ P T pΦq, we have by equation (3.1):
ΠpHϕ, νq “
ÿ
ZPT pHϕq
p´1qZνpZq “
ÿ
ZPT pHϕq
p´1qZ
ÿ
TPT pHq
TĂZ
νpTq.
Hence
ÿ
ϕPT pΦq
ǫpϕqΠpHϕ, νq “
ÿ
ϕPT pΦq
ǫpϕq
ÿ
ZPT pHϕq
p´1qZ
ÿ
TPT pHq
TĂZ
νpTq
“
ÿ
TPT pHq
νpTq
ÿ
ϕPT pΦq
ǫpϕqp´1qZϕpTq.
As ř
ϕPT pΦq ǫpϕqp´1qZϕpTq “ p´1qT for every T P T pHq by Corollary 3.1.4, the statement follows.
We now prove statement (i) of Theorem 3.2.1. Fix a point x in the base chamber B of H. For
every closed convex polyhedral cone K Ă V , let FxpKq be the set of closed faces F of K such that
x P K ` SpanpFq. Consider the function ψ : CHpV q ÝÑ KHpV q deﬁned by
ψpKq “
ÿ
F PFxpKq
p´1qdim F rFs.
This is the ‹-product in the sense of Corollary A.1.8 (see also Remark A.1.9) of the valuations
CHpV q ÝÑ KHpV q, K ÞÝÑ rKs and ψx : CpV _q ÝÑ Z, where V _ is the dual of V and ψx is the
valuation of Lemma A.1.10. More explicitly, for K Ă V _ a nonempty closed convex polyhedral
cone, we have ψxpKq “ 1 if and only if x P K˚. Indeed, with the notation of that deﬁnition, we have
15


## Page 16


pF K,Kq˚ “ K ` SpanpFq for every K P CHpV q and every closed face F of K. By Corollary A.1.8,
the function ψ is a valuation, so it induces a morphism ψ : KHpV q ÝÑ KHpV q. Moreover, the
valuation ψ vanishes on degenerate cones in CHpV q.
Indeed, if K P CHpV q is contained in a
hyperplane H of H, then K ` SpanpFq Ă H for every F P FpKq, so FxpKq “ ∅because x is not
on any hyperplane of H. Hence we can apply statement (i) that we just proved to ψ.
Let H1 be a subarrangement of H, and let B1 be the unique chamber of H1 containing B. If
T P T pH1q, we write F0pTq “ tC P L pH1q : C ď T and C ˝ B1 “ Tu. As x P B Ă B1, we have
FxpTq “ tC : C P F0pTqu by Lemma 3.3.1. We deduce that
ΠpH1, ψq “
ÿ
TPT pH1q
p´1qT ψpTq
“
ÿ
TPT pH1q
p´1qT
ÿ
F PFxpTq
p´1qdim F rFs
“
ÿ
TPT pH1q
p´1qT
ÿ
CPL pH1q, C˝B1“T
p´1qdim CrCs
“
ÿ
CPL pH1q
p´1qCp´1qdim CrCs.
Using statement (i) for the valuation ψ, we get that
ÿ
CPL pHq
p´1qCp´1qdim CrCs “
ÿ
ϕPT pΦq
ǫpϕq
ÿ
CPL pHϕq
p´1qCp´1qdim CrCs.
(3.2)
By the top of page 544 of [GKM97], there exists an endomorphism of KHpV q sending rKs to
p´1qdim Kr˚
Ks, for every K P CHpV q.
Applying this endomorphism to the identity (3.2) yields
statement (i).
Finally, the general case of statement (ii) immediately follows from applying the morphism
ν : KHpV q ÝÑ A to both sides of the identity of statement (i).
4
The weighted sum
4.1
The weighted complex and the weighted sum
We return to the situation of Subsection 2.1. In particular, we ﬁx a ﬁnite-dimensional real inner
product space V and a central hyperplane arrangement H “ pHαeqePE on V , and we denote by L
and T the sets of faces and chambers of H.
Deﬁnition 4.1.1. Let λ P V . We consider the following subset of the face poset L :
Lλ “ tC P L : C Ď H`
λ u.
In other words, the set Lλ is the collection of faces on the nonnegative side of the hyperplane Hλ.
More generally, if C0 is a ﬁxed face of L , we also consider the intersection
Lλ,ěC0 “ Lλ X LěC0.
16


## Page 17


Remark 4.1.2. (See [Bj¨o+99, Section 4.5] for deﬁnitions.) If λ ‰ 0 then the hyperplane arrangement
tHλu Y tHαe : e P Eu deﬁnes an aﬃne oriented matroid with distinguished hyperplane Hλ. If Hλ
is in general position relative to the Hαe, that is, if λ is not in the span of any family pαeqePF for
|F| ď dimpV q ´ 1, then Lλ coincides with the bounded complex of this aﬃne oriented matroid. In
general, Lλ is larger.
The basic properties of the subsets Lλ and Lλ,ěC0 are given in the following proposition.
Proposition 4.1.3. The following two statements hold:
(i) For a ﬁxed face C0 of L the set Lλ,ěC0 is a lower order ideal in LěC0.
(ii) Let C P Lλ. Then there exists T P T X Lλ such that C ď T.
Proof. It suﬃces to prove (i) when C0 is the minimal face of L . Let C, D P L such that C ď D
and D P Lλ. The hypothesis implies that C Ă D and D Ă H`
λ . As H`
λ is closed, this immediately
gives C Ă H`
λ , hence C P Lλ.
To show (ii) let D1, D2, . . . , Dp be the chambers of T that are larger than C with respect to
the partial order ď. If one of them is contained in H`
λ , then we are done. Otherwise, for every
1 ď i ď p, we can ﬁnd a point xi P Di such that pλ, xiq ă 0. Let H1 be the subarrangement
of H where we remove all the hyperplanes of H that contain the cone C. In the arrangement H1
all the points xi are contained in the same chamber C1. In particular, the convex hull P of the
points x1, x2, . . . , xp is contained in C1. The convex hull P intersects the linear span of the cone C
in a point x. Since all the points xi are in the open half-space H´
λ , so is the point x, that is,
pλ, xq ă 0. By inserting the hyperplanes of H that contain the cone C back in the arrangement H1,
we subdivide the region C1 into regions C1, C2, . . . , Cp. But the point x belongs to the closure of
each region Ci, thus the point x belongs to the cone C. This is a contradiction since C is contained
in the half-space H`
λ , so pλ, xq ě 0.
Deﬁnition 4.1.4. The subcomplex of the cell decomposition ΣpL q, respectively ΣpLěC0q, whose
face poset is the lower order ideal Lλ, respectively Lλ,ěC0, is called the weighted complex and
denoted by ΣpLλq, respectively ΣpLλ,ěC0q. By Proposition 4.1.3 it is pure of the same dimension
as ΣpLλq, respectively ΣpLλ,ěC0q.
We are interested in the following quantity.
Deﬁnition 4.1.5. Let λ be a vector in V and B a chamber of H, that is, B P T . The weighted
sum is deﬁned to be
ψHpB, λq “
ÿ
DPLλ
p´1qdimpDq ¨ p´1q|SpB,D˝Bq|.
(4.1)
More generally, if C is a face of the arrangement H, that is, C P L , and if B is a chamber whose
closure contains the face C, that is, B P T X LěC, we deﬁne the weighted sum to be
ψH{CpB, λq “
ÿ
DPLλ,ěC
p´1qdimpDq ¨ p´1q|SpB,D˝Bq|.
(4.2)
17


## Page 18


Remark 4.1.6. This deﬁnition seems very arbitrary and mysterious. We try to give some context
for it in Appendix C. Without getting into too much detail here, the weighted sum (in the situation
of Example 4.2.1) plays a role in the calculation of the trace of Hecke operators on the weighted
cohomology of locally symmetric varieties that is very similar to the role played by stable discrete
constants (see for example pages 493 and 498–500 of [GKM97]) in the calculation of the trace
of Hecke operators on L2 cohomology of these varieties. It is because of this that we chose the
names “weighted complex” and “weighted sum”. In fact, in that situation we only really need
the “absolute” version where C is the minimal face of H. The “relative” version, where C is not
minimal anymore, appears when the locally symmetric variety is a Shimura variety deﬁned over a
number ﬁeld E and we are considering the trace of a Hecke operator multiplied by an element of
the absolute Galois group of E.
Remark 4.1.7. In our previous paper, we used the notation Spλq (see [EMR19, Equation (6.1)]) to
denote what turns out to be a particular case of the sum in equation (4.2) in the type B Coxeter
case; see equation (4.3) in Subsection 4.4 for the precise relation between the two. In this paper,
we decided to follow the notation of [GKM97] in order to avoid overuse of the letter S.
We state the following lemma. It reduces the calculation of ψH{CpB, λq to the case of an essential
arrangement.
Lemma 4.1.8. Let V0 be the intersection of all the hyperplanes of H, that is, V0 “ Ş
ePE Hαe.
Let π denote the projection V ÝÑ V {V0. Let H{V0 be the hyperplane arrangement pHαe{V0qePE
on V {V0. Note that π induces an isomorphism between the face poset of H and H{V0. Let C P L ,
let B be a chamber of H such that B P LěC and let λ P V . Then the following identity holds:
ψH{CpB, λq “
#
p´1qdimpV0q ¨ ψpH{V0q{πpCqpπpBq, πpλqq
if λ P V K
0 ,
0
if λ R V K
0 .
Proof. Note that λ P V K
0
if and only if V0 Ă Hλ. If λ R V K
0
then the linear functional pλ, ¨q takes
both positive and negative values on V0. As V0 Ă D for every D P L , this linear functional also
takes both positive and negative values on D, so D R Lλ. This shows that Lλ “ ∅if λ R V K
0
and gives the second case. Now suppose that λ P V K
0 . Then V0 Ă Hλ, and it is easy to see that
D P Lλ, respectively D P LěC, if and only if πpDq Ă H`
πpλq, respectively πpDq ě πpCq, and that
dimpπpDqq “ dimpDq ´ dimpV0q. This yields the ﬁrst case.
Suppose that V “ V1 ˆ ¨ ¨ ¨ ˆ Vr with the Vi mutually orthogonal subspaces of V and that H
also decomposes as a product H1 ˆ ¨ ¨ ¨ ˆ Hr. By this, we mean that there is a decomposition
E “ E1 \ ¨ ¨ ¨ \ Er such that, for 1 ď i ď r and every e P Ei, we have αe P Vi. The arrangement
Hi “ pVi X HαeqePEi is a hyperplane arrangement on the subspace Vi, and each hyperplane of H is
of the form H ˆ ś
j‰i Vj, where 1 ď i ď r and H is one of the hyperplanes of Hi.
Let Li be the face poset of Hi for 1 ď i ď r. Then the faces of L are exactly the products
C1ˆ¨ ¨ ¨ˆCr where Ci P Li, and the order on L is the product order. In particular, C is a chamber
in L if and only if all the Ci are chambers in Li.
Lemma 4.1.9. Assume that the arrangement H factors as H1 ˆ ¨ ¨ ¨ ˆ Hr as described in the two
previous paragraphs. Let C “ C1 ˆ¨ ¨ ¨ ˆCr be a face in L , and let B “ B1 ˆ¨ ¨ ¨ ˆBr be a chamber
18


## Page 19


in LěC. Finally, let λ P V . Then
ψH{CpB, λq “
r
ź
i“1
ψHi{CipBi, λiq,
where, for 1 ď i ď r, λi is the orthogonal projection of λ on Vi.
Proof. The expression for ψH{CpB, λq follows from the fact that L “ L1 ˆ ¨ ¨ ¨ ˆ Lr as posets once
we prove the following statement: Let D “ D1 ˆ ¨ ¨ ¨ ˆ Dr P L , with Di P Li. Then D P Lλ if and
only if Di P Li,λi for 1 ď i ď r.
We prove this last fact. Note that λ “ pλ1, . . . , λrq in V1 ˆ ¨ ¨ ¨ ˆ Vr “ V because the Vi are
pairwise orthogonal. If Di P Li,λi for every 1 ď i ď r then for every x “ px1, . . . , xrq P V we
have pλ, xq “ řr
i“1pλi, xiq ě 0. Conversely, suppose that D P Lλ. Let xj P Dj for 1 ď j ď r.
As all the Dj are cones, for every ε ą 0 the element εxj is in Dj. Fix 1 ď i ď r and consider
the element xε “ pεx1, . . . , εxi´1, xi, εxi`1, . . . , εxrq. Then xε is in D. Thus we have the inequality
0 ď pλ, xεq “ pλi, xiq ` ε ř
j‰ipλj, xjq.
Letting ε tend to 0, we obtain pλi, xiq ě 0 and hence
Di P Li,λi.
4.2
Calculating the weighted sum for some arrangements with many symme-
tries
We continue to use the notation of Subsections 2.1 and 2.2. Suppose that E “ Ep1q \ Ep2q, with
Hp1q “ pHαeqePEp1q a Coxeter arrangement whose Coxeter group W stabilizes Hp2q “ pHαeqePEp2q,
and that C “ pŞ
ePEp1q Hαeq X pŞ
ePEp2q H`
αeq, so that EpCq “ te P E : C Ă Hαeu “ Ep1q. To
simplify some of the notation, without loss of generality we may assume that the vectors αe, where
e P E, are all unit vectors. We assume that there exists a chamber B of H that is on the positive
side of every hyperplane of H (not just Hp1q); in particular, we have C ď B. This also deﬁnes a
chamber of the arrangement Hp1q, and we denote by pW, Sq the associated Coxeter system, as in
Theorem 2.2.3.
The set Φ “ t˘αe : e P Ep1qu is a normalized pseudo-root system (see Deﬁnition B.1.1), the
subset Φ` “ tαe : e P Ep1qu is a system of positive pseudo-roots in Φ (see Deﬁnition B.1.4), and
pW, Sq is the corresponding Coxeter system. See Proposition B.1.6.
Our main example of such arrangements is the following.
Example 4.2.1. Let pW, Sq be a Coxeter system, let V be the canonical representation of W, and
let H “ pHαqαPΦ` be the associated hyperplane arrangement on V as in Section 2.2. Let I be a
subset of S, set Φp1q “ Φ` X
`ř
αPI Rα
˘
and Φp2q “ Φ` ´Φp1q. Then Hp1q “ pHαqαPΦp1q is a Coxeter
arrangement with associated Coxeter system pWI, Iq, where WI is the subgroup of W generated
by I, and WI preserves the arrangement Hp2q “ pHαqαPΦp2q. If C “ pŞ
αPΦp1q Hαq X pŞ
αPΦp2q H`
α q
as before, then the chamber B corresponding to 1 P W is in LěC.
We use again the notion of 2-structures for Φ; see Subsection 3.1.
If ϕ P T pΦq we write
ϕ` “ ϕ X Φ`, and we denote by Hϕ the hyperplane arrangement pHαqαPϕ`\Ep2q and by Bϕ,
respectively Cϕ, the unique chamber of Hϕ containing B, respectively C. By the choice of B, the
chamber Bϕ is also the unique chamber on the positive side of every hyperplane in Hϕ.
Theorem 4.2.2. Let H “ Hp1q \ Hp2q be an arrangement in V with base chamber B. Assume that
the subarrangement Hp1q is a Coxeter arrangement with pseudo root system Φ and its Coxeter group
19


## Page 20


stabilizes H. Let C be the intersection of the base chamber of Hp2q and the hyperplanes in Hp1q.
Then for every λ P V we have
ψH{CpB, λq “
ÿ
ϕPT pΦq
ǫpϕq ¨ ψHϕ{CϕpBϕ, λq.
This is the second main theorem of this article. It will be proved in Subsection 4.5. See Deﬁni-
tion 4.1.5 for the description of the terms and Remark 4.1.6 for an explanation of their signiﬁcance.
Theorem 4.2.2 states that the weighted sum for a Coxeter arrangement can be expressed as an
alternating sum of weighted sums for much simpler subarrangements (the 2-structures) that are
direct products of rank one and rank two Coxeter arrangements. As weighted sums for these sub-
arrangements can be calculated directly (see Corollary 4.3.1 and Proposition 4.3.2 for the case
where C is the minimal face), this gives a way to calculate the weighted sum for the original Cox-
eter arrangement, and thus, as explained in Appendix C, to relate weighted cohomology of locally
symmetric varieties to the spectral side of the Arthur-Selberg trace formula.
We ﬁrst give some applications of Theorem 4.2.2.
4.3
First application: the case of Coxeter arrangements
We specialize Theorem 4.2.2 to the case where H “ Hp1q is a Coxeter arrangement. In particular,
C is the minimal face of L , so ψH{CpB, λq “ ψHpB, λq for every λ P V .
Let ϕ P T pΦq, and let ϕ “ ϕ1 \ ϕ2 \ ¨ ¨ ¨ \ ϕr be the decomposition of ϕ into irreducible
pseudo-root systems. Let Vi,ϕ “ Spanpϕiq for 1 ď i ď r. Then V “ V0,ϕ ˆ V1,ϕ ˆ ¨ ¨ ¨ ˆ Vr,ϕ,
where V0,ϕ “ ϕK. The dimension of V0,ϕ is equal to dimpV q ´ rankpϕq, so it is independent of ϕ
by Proposition B.2.4. Let Hi,ϕ be the hyperplane arrangement given by ϕi X Φ` on Vi,ϕ where
1 ď i ď r. For a ﬁxed index i let Bi,ϕ be the chamber of the arrangement Hi,ϕ that is on the
positive side of every hyperplane, and let λi,ϕ be the orthogonal projection of λ on Vi,ϕ.
Combining Theorem 4.2.2 with Lemmas 4.1.8 and 4.1.9, we obtain:
Corollary 4.3.1. For every λ P V , we have
ψHpB, λq “ p´1qdimpV q´R ¨
ÿ
ϕPT pΦq
λPSpanpϕq
ǫpϕq ¨
r
ź
i“1
ψHi,ϕpBi,ϕ, λi,ϕq,
where R is the rank of any ϕ P T pΦq.
To ﬁnish the calculation of ψHpB, λq in this case, we use the following proposition, whose proof
is a straightforward calculation.
Proposition 4.3.2. In types A1, B2 “ I2p4q and I2p2kq for k ě 3, the function ψ is given by the
following expressions:
(1) Type A1: Suppose that V “ Re1 and that Φ` “ te1u. Then ψ is given by
ψHpB, ce1q “
$
’
&
’
%
0
if c ą 0,
1
if c “ 0,
2
if c ă 0.
20


## Page 21


2
2
2
2
2
2
2
2
4
4
4
4
e1
e2
Figure 1: The function ψHpB, λq in the dihedral pseudo-root system I2p8q. The origin is assigned
the value 1 and the unmarked faces are assigned the value 0.
(2) Type I2p2kq, where k ě 2: Let V “ Re1 ‘ Re2 with the usual inner product.
For every
v P V ´ t0u, let θpvq P r0, 2πq be the angle from e1 to v. Suppose that Φ is the set of unit
vectors that have an angle of rπ{2k with e1, where r P Z, and that B is the set of nonzero
vectors v P V such that 0 ă θpvq ă π{2k. Then ψ is given by
ψHpB, λq “
$
’
’
’
’
’
’
&
’
’
’
’
’
’
%
1
if λ “ 0,
2
if λ ‰ 0 and θpλq “ rπ{2k with 2k´1 ` 1 ď r ď 3 ¨ 2k´1,
4
if λ ‰ 0 and rπ{2k ă θpλq ă pr ` 1qπ{2k
with r odd and 2k´1 ` 1 ď r ď 3 ¨ 2k´1 ´ 1,
0
otherwise.
Remark 4.3.3. If pW, Sq arises from a root system Φ and ´1 is an element of W (or, equivalently, the
root system is generated by strongly orthogonal roots), then Goresky–Kottwitz–MacPherson [GKM97,
Theorem 3.1] and Herb [Her00, Theorem 4.2] give two diﬀerent expressions for the coeﬃcients ap-
pearing in the formula for the averaged discrete series characters of a real reductive group with
root system Φ. Corollary 4.3.1 asserts the equality of these two formulas. In general, although
there no longer exist discrete series in this setting, the formulas of Goresky–Kottwitz–MacPherson
and Herb still make sense, and Corollary 4.3.1 says that they are still equal. Also, Corollary 4.3.1
implies that ψHpB, λq “ 0 if λ is not in the span of any 2-structure for Φ, so it implies [GKM97,
Theorem 5.3]. It is not clear whether this is an easier proof than the one given in [GKM97].
4.4
Second application: the type A identity involving ordered set partitions
We now show how to deduce [EMR19, Theorem 6.4]2 from Theorem 4.2.2. We take V “ Rn with
the usual inner product, and we denote by pe1, . . . , enq the standard basis of V . We consider the
2This is a reformulation of [Mor11, Proposition A.4].
21


## Page 22


hyperplane arrangement H of type Bn on V , that is, H “ pHαqαPΦ`
B, where Φ`
B “ tei ˘ ej : 1 ď
i ă j ď nu Y te1, . . . , enu. We write Φ`
B “ Φp1q \ Φp2q, where Φp1q “ tei ´ ej : 1 ď i ă j ď nu,
and we denote by H “ Hp1q \ Hp2q the corresponding decomposition of H. The arrangement Hp1q
is a Coxeter arrangement of type An´1, and we denote by Φ “ Φp1q Y p´Φp1qq the associated
root system. Let C be the intersection pŞ
αPΦp1q Hαq X pŞ
αPΦp2q H`
α q. Then C is the open ray
Rą0 ¨ pe1 ` e2 ` ¨ ¨ ¨ ` enq.
Recall that L is the face poset of H. We will now give a description of L in terms of signed
ordered partitions. See also [ER99, Section 5] for this description. A signed block is a nonempty
subset rB of t˘1, . . . , ˘nu such that, for every i P t1, . . . , nu, at most one of ˘i is in rB. We then
denote by B the subset of t1, . . . , nu deﬁned by B “ t|i| : i P rBu. A signed ordered partition of
a subset I of t1, . . . , nu is a list p rB1, . . . , rBrq of signed blocks such that pB1, . . . , Brq is an ordered
partition of I.
We consider the poset Πord,B
n
whose elements are pairs π “ prπ, Zq, where Z Ď t1, . . . , nu and rπ
is a signed ordered partition of t1, . . . , nu ´ Z, and the cover relation is given by the following two
rules:
pp rB1, . . . , rBrq, Zq ă pp rB1, . . . , rBr´1q, Br Y Zq,
pp rB1, . . . , rBrq, Zq ă pp rB1, . . . , rBi´1, rBi Y rBi`1, rBi`2, . . . , rBrq, Zq.
The set Z is usually called the zero block of π.
Let π “ prπ, Zq be an element of Πord,B
n
, with rπ “ p rB1, . . . , rBrq. We deﬁne the cone Cπ to be
the set of px1, . . . , xnq P V such that (with the convention that x´i “ ´xi for 1 ď i ď n):
(i) if Z “ ti1, . . . , imu then the equalities xi1 “ ¨ ¨ ¨ “ xim “ 0 hold;
(ii) for every block rB “ ti1, . . . , imu in rπ, the equalities and inequality xi1 “ ¨ ¨ ¨ “ xim ą 0 hold;
(iii) for every two consecutive blocks rBs and rBs`1 in rπ with i P rBs and j P rBs`1, the inequality
|xi| ą |xj| holds.
It is easy to see that the map ϕ : Πord,B
n
ÝÑ L sending π to Cπ is a bijection, and that it induces
an order-reversing isomorphism between the poset Πord,B
n
and the face poset L . The inverse image
of the ray C “ Rą0¨pe1`e2`¨ ¨ ¨`enq by this bijection is the element π0 “ ppt1, . . . , nuq, ∅q of Πord,B
n
,
so the elements of LěC correspond exactly to the (unsigned) ordered partitions of t1, . . . , nu. In
other words, the bijection ϕ induces an order-reversing isomorphism between the poset Πord
n
of
ordered partitions of t1, . . . , nu deﬁned in [EMR19, Section 2] and the poset LěC.
Let λ “ pλ1, . . . , λnq P Rn. For a signed block rB, we set λ rB “ ř
iPB λi, with the convention
that λ´i “ ´λi for 1 ď i ď n. Deﬁne the subset Πord,B
n
pλq of Πord,B
n
by
Πord,B
n
pλq “
#
pp rB1, rB2, . . . , rBrq, Zq P Πord,B
n
:
sÿ
i“1
λ rBi ě 0 for 1 ď s ď r
+
.
Then an element π of Πord,B
n
is in Πord,B
n
pλq if and only if Cπ is in Lλ. Moreover, the subset Lλ,ěC
corresponds to the set Πord
n pλq of ordered partitions pB1, . . . , Brq of t1, . . . , nu such that, for every
1 ď s ď r, we have řs
i“1 λBi ě 0. This is almost the set Ppλq of [EMR19, Section 3]; the only
diﬀerence is that the inequalities deﬁning Ppλq are strict. We can give the following identity relating
22


## Page 23


these two sets: For every ε P R, let λε “ pλ1 ´ ε, . . . , λn ´ εq. Then if ε ą 0 is suﬃciently small, we
have Πord
n pλεq “ Ppλq.
Let B be the unique chamber of L that is on the positive side of every hyperplane, that is,
B “ tx1 ą x2 ą ¨ ¨ ¨ ą xn ą 0u. As we already observed, LěC is isomorphic to the face poset of
the arrangement Hp1q, which is a Coxeter arrangement of type An´1. The unique chamber of this
arrangement containing B corresponds to the identity element in the symmetric group Sn. It then
follows from Proposition 5.1.4 that the function fB : LěC ÝÑ T X LěC sending C1 P LěC to
C ˝ B corresponds via ϕ : Πord
n
„
ÝÑ LěC to the function f : Πord
n
ÝÑ Sn of [EMR19, Section 4].
We obtain the equality:
ψH{CpB, λq “
ÿ
πPΠord
n
pλq
p´1q|π| ¨ p´1qfpπq,
where |π| denotes the number of blocks of the ordered partition π “ pB1, . . . , Brq, in other words,
|π| “ r. Let λ denote the reverse of λ, that is, λ “ pλn, . . . , λ1q. For ε real we let λε be pλn ´
ε, . . . , λ1 ´ εq. By [EMR19, Lemma 7.1], we have
ψH{CpB, λq “ p´1qpn
2q ¨
ÿ
πPΠord
n
pλq
p´1q|π| ¨ p´1qgpπq,
where g : Πord
n
ÝÑ Sn is the function deﬁned at the beginning of [EMR19, Section 6].3 Finally,
using the fact that Πord
n pλεq “ Ppλq for suﬃciently small ε ą 0, then the sum Spλq of [EMR19,
Section 6] is given by the expression:
Spλq “ p´1qpn
2q ¨ ψH{CpB, λεq
(4.3)
for any suﬃciently small ε ą 0.
We now ﬁnd an expression for the sum Tpλq of [EMR19, Section 6] in terms of 2-structures.
As in [EMR19], we denote by Mn the set of maximal matchings on t1, 2, . . . , nu. Then we have
a bijection Mn
„
ÝÑ T pΦq sending a matching p “ tp1, . . . , pmu, where p1 “ ti1 ă j1u, . . . , pm “
tim ă jmu are the edges of p, to the 2-structure ϕp “ t˘pei1 ´ej1q, . . . , ˘peim ´ejmqu. Moreover, we
have p´1qp “ ǫpϕpq. We can calculate ψHϕp{CϕppBϕp, λq using Lemma 4.1.9 for the decomposition
V “ V0 ˆ V1 ˆ ¨ ¨ ¨ ˆ Vm, where Vk “ Reik ` Rejk for 1 ď k ď m, V0 “ t0u if n is even, and V0 “ Rei
if n is odd and i is the unique unmatched element of t1, . . . , nu. By Lemma 4.1.9 we have
ψHϕp{CϕppBϕp, λq “
m
ź
k“1
d2pλik, λjkq ¨
#
1
if n is even,
d1pλiq
if n is odd,
where:
(a) The function d1 : R ÝÑ R is deﬁned by d1paq “ ψH1{C1pB1, aq, where H1 is the hyperplane
arrangement pHeq on Re and B1 “ C1 “ Rą0e.
(b) The function d2 : R2 ÝÑ R is deﬁned by d2pa, bq “ ψH2{C2pB2, pa, bqq, where H2 is the
hyperplane arrangement pHe, Hf, He´f, He`fq on Re ‘ Rf, C2 “ tαe ` βf : α “ β ą 0u and
B2 “ tαe ` βf : α ą β ą 0u.
3The map f : Πord
n
ÝÑ Sn takes an ordered partition, orders the elements in each block in increasing order and
then maps them to the permutation formed by reading the elements from left to right. The map g is similarly deﬁned,
except the elements in each block are reordered in decreasing order.
23


## Page 24


In other words, the functions d1 and d2 are precisely the function ψH{CpB, λq that we are trying to
determine in the cases n “ 1 and n “ 2. A direct calculation yields:
d1paq “
#
´1
if a ě 0,
0
if a ă 0,
and
d2pa, bq “
$
’
&
’
%
´1
if a, b ě 0,
´2
if b ě ´a ą 0,
0
otherwise.
Comparing this with the formula deﬁning cpp, λq in [EMR19, Section 6], we see that, for all a, b P R,
if ε ą 0 is suﬃciently small relative to a and b, we have d1pa ´ εq “ ´c1paq and d2pa ´ ε, b ´ εq “
´c2pb, aq, and hence
ψHϕp{CϕppBϕp, λεq “ cpp, λq ¨
#
p´1qn{2
if n is even,
p´1qpn`1q{2
if n is odd
“ p´1qn ¨ p´1qpn
2q ¨ cpp, λq,
if ε ą 0 is suﬃciently small relative to the λi. Combining all these calculations, we see that if ε ą 0
is suﬃciently small, then
ÿ
ϕPT pΦq
ǫpϕq ¨ ψHϕ{CϕpBϕ, λεq “ p´1qn ¨ p´1qpn
2q ¨
ÿ
pPMn
p´1qp ¨ cpp, λq “ p´1qn ¨ p´1qpn
2q ¨ Tpλq.
The identity Spλq “ p´1qn¨Tpλq in [EMR19, Theorem 6.4] now follows from Theorem 4.2.2, applied
to λε for ε ą 0 suﬃciently small.
4.5
Proof of Theorem 4.2.2
We assume for now that H “ pHαeqePE is an arbitrary central hyperplane arrangement on V . The
following deﬁnition will be useful.
Deﬁnition 4.5.1. Let C P L and λ P V . If D, D1 P LěC, we deﬁne ψD{CpD1, λq by the sum
ψD{CpD1, λq “
ÿ
C1PLλ,ěC
C1˝D1ďD
p´1qdimpC1q,
where Lěλ,C “ Lλ X LěC.
Remark 4.5.2. Suppose that D1 is a chamber. Then C1 ˝ D1 is a chamber for every C1 P L , so
ψD{CpD1, λq “ 0 unless D is also a chamber. If D is a chamber, we have
ψD{CpD1, λq “
ÿ
C1PLλ,ěC
C1˝D1“D
p´1qdimpC1q.
The functions ψD{CpD1, λq are related to ψH{CpB, λq by the following lemma.
Lemma 4.5.3. Let C P L and B P T X LěC. Then for every λ P V the following identity holds:
ψH{CpB, λq “
ÿ
TPT XLěC
p´1q|SpB,Tq| ¨ ψT{CpB, λq.
24


## Page 25


Proof. Indeed, if D P LěC then the chamber D ˝ B is also in LěC. Hence, using equation (4.2) in
Deﬁnition 4.1.5 and Remark 4.5.2, we obtain:
ψH{CpB, λq “
ÿ
TPT XLěC
p´1q|SpB,Tq| ¨
ÿ
DPLλ,ěC
D˝B“T
p´1qdimpDq “
ÿ
TPT XLěC
p´1q|SpB,Tq| ¨ ψT{CpB, λq.
Before Corollary A.1.11 of Appendix A, we deﬁne, for K a closed convex polyhedral cone in V ,
a function ψK : V ˆ V _ ÝÑ R. For ﬁxed px, ℓq P V ˆ V _, the function K ÞÝÑ ψKpx, ℓq is a
valuation on the set of closed convex polyhedral cones in V (see Deﬁnition A.1.3). This function is
related to the functions ψD{CpD1, λq in the following way.
Lemma 4.5.4. Let C P L , let D P LěC and let λ P V . Denote by ℓP V _ the linear func-
tional p¨, λq. Then for every D1 P LěC the following identity holds:
ψD{CpD1, λq “ ψDpx, ℓq,
where x is any point in D1
1 “ p´Cq ˝ D1.
Proof. As before we write EpCq “ te P E : C Ă Hαeu. Note that spD1
1qe “ spD1qe for e P EpCq,
and spD1
1q “ ´spCqe ‰ 0 for e P E´EpCq. Also, by deﬁnition of LěC, if e is any index of E´EpCq
and C1 P LěC then spCqe “ spC1qe ‰ 0.
We claim that for every C1 P L we have C1 ˝ D1
1 ď D if and only if C1 P LěC and C1 ˝
D1 ď D.
Suppose ﬁrst that C1 P LěC and C1 ˝ D1 ď D.
Then for every e P EpCq we have
spC1 ˝ D1
1qe “ spC1 ˝ D1qe ď spDqe. Moreover, if e P E ´ EpCq then spC1qe “ spCqe “ spDqe ‰ 0, so
spC1 ˝ D1
1qe “ spC1qe “ spDqe. This shows that C1 ˝ D1
1 ď D. Conversely, suppose that C1 is a face
of L such that C1 ˝ D1
1 ď D. If e P E ´ EpCq then 0 ‰ spCqe “ spDqe “ ´spD1
1qe, thus spC1qe ‰ 0,
and so spC1qe “ spC1 ˝ D1
1qe “ spDqe. This implies that C1 P LěC. Moreover, if e P EpCq we have
spD1
1qe “ spD1qe, thus spC1 ˝ D1qe “ spC1 ˝ D1
1qe ď spDqe. Hence we conclude that C1 ˝ D1 ď D.
By the claim, we obtain
ψD{CpD1, λq “
ÿ
C1PLλ
C1˝D1
1ďD
p´1qdimpC1q “ ψDpD1
1, λq.
We wish to show that this is equal to ψDpx, ℓq, if x P D1
1. As in Appendix A, we denote by FpDq the
set of closed faces of the closed convex polyhedral cone D. We have FpDq “ tC1 : C1 P L , C1 ď Du,
and the set tC1 P L : C1 ˝D1
1 ď Du is included in the set tC1 P L : C1 ď Du. To prove the equality
above, it suﬃces to show that the two following statements hold for C1 P L such that C1 ď D (see
Lemma A.1.10 for the deﬁnition of ψx and ψℓ, and the beginning of Section A.1 for the notation
C1K,D):
(a) The face C1 belongs to Lλ if and only ψℓpC1q “ 1.
(b) The inequality C1 ˝ D1
1 ď D holds if and only if ψx
ˆ
C1K,D
˙
“ 1.
Statement (a) is just a direct translation of the deﬁnition of Lλ, and statement (b) is proved
in Lemma 3.3.1.
25


## Page 26


We are now ready to prove Theorem 4.2.2, so we assume that we are in the situation of that
theorem.
Let ℓbe the linear functional p¨, λq on V , let x P p´Cq ˝ B, and consider the valuation ν
on the set of closed convex polyhedral cones in V sending such a cone K to ψKXCpx, ℓq, where
C “ CC “ Ş
ePEp2q H`
αe.
The function K ÞÝÑ ψKpx, ℓq is a priori deﬁned only on the set of
closed convex polyhedral cones. However, as it is a valuation, we can extend it to the set of all
ﬁnite intersections of closed and open half-spaces in V . See Remark A.1.13. As x is not on any
hyperplane of H, the valuation ψx vanishes on any cone contained in a hyperplane of H. It follows
from the deﬁnition of the function K ÞÝÑ ψKpx, ℓq in the discussion before Corollary A.1.11 that
we have ψKpx, ℓq “ 0 if K is contained in a hyperplane of H. In particular, for D a face of H, we
have νpDq “ 0 unless D is a chamber, and if D is a chamber then νpDq “ νpDq.
Let ϕ Ă Φ be a pseudo-root system (we do not assume that ϕ is a 2-structure), let ϕ` “ ϕXΦ`
and Hϕ “ pHαeqePϕ`\Ep2q, and denote by Bϕ and Cϕ the unique faces of Hϕ containing B and C.
We have Cϕ “ Ş
ePϕ` Hαe X Ş
ePEp2q H`
αe.
We also set Hp1q
ϕ
“ pHαeqePϕ`, Lϕ “ L pHϕq and
Tϕ “ T pHϕq.
As in statement (i) of Lemma 2.1.3, we denote by ι : Lϕ,ěCϕ ÝÑ L pHp1q
ϕ q the map sending a
face D ě Cϕ of Hϕ to the unique face of Hp1q
ϕ
that contains it. By the lemma we just cited, we know
that this is an order-preserving bijection, and that its inverse sends a face Dp1q of Hp1q
ϕ
to Dp1q X C,
where C “ Ş
ePEp2q H`
αe as before. We claim that, if Dp1q is a face of Hp1q
ϕ , then Dp1q X C “ Dp1q XC.
Indeed, let s P t`, ´, 0uϕ` be the sign vector of Dp1q. Then the sign vector t P t`, ´, 0uE of Dp1qXC
is given by te “ se if e P ϕ`, and te “ ` if e P Ep2q. We set R` “ Rě0, R´ “ Rď0 and R0 “ t0u.
Let y P V . Then y P Dp1q if and only if pαe, yq P Rse for every e P ϕ`, while y P Dp1q X C if and
only pαe, yq P Rte for every e P E and y P C if and only if pαe, yq ě 0 for every e P Ep2q. This
immediately implies the claim.
Let Dp1q be a face of Hp1q
ϕ . By Lemma 4.5.4 we have
ψι´1pDp1qq{CϕpBϕ, λq “ ψDp1qXCpx, ℓq “ ψDp1qXCpx, ℓq “ νpDp1qq,
because x P p´Cq ˝ B Ă p´Cϕq ˝ Bϕ. Moreover, by Lemma 4.5.3, we have
ψHϕ{CϕpBϕ, λq “
ÿ
TPTϕXLϕ,ěCϕ
p´1q|SpBϕ,Tq| ¨ ψT{CϕpBϕ, λq.
So, using statements (i) and (iii) of Lemma 2.1.3, we get that
ψHϕ{CϕpBϕ, λq “
ÿ
T p1qPT pHp1q
ϕ q
p´1q|SpιpBϕq,T p1qq|ψι´1pT p1qq{CϕpBϕ, λq
“
ÿ
T p1qPT pHp1q
ϕ q
p´1q|SpιpBϕq,T p1qq|νpT p1qq
“
ÿ
Cp1qPT pHp1q
ϕ q
p´1q|SpιpBϕq,Cp1q˝ιpBϕqq|νpCp1qq.
In other words, using the notation of Subsection 3.2, we obtain
ψHϕ{CϕpBϕ, λq “ ΠpHϕ, νq.
(4.4)
26


## Page 27


Applying this identity to ϕ “ Φ, we have ψH{CpB, λq “ ΠpH, νq. By Theorem 3.2.1, we deduce
that
ψH{CpB, λq “
ÿ
ϕPT pΦq
ǫpϕqΠpHϕ, νq.
The conclusion of Theorem 4.2.2 follows from this equality and from equation (4.4) for all ϕ P T pΦq.
5
Properties of the weighted complex
This section is independent of Sections 3 and 4, except for Deﬁnition 4.1.1 and Remark 4.1.2.
We prove that the weighted complex is shellable for Coxeter arrangements, or more generally for
arrangements satisfying some condition on the dihedral angles between their hyperplanes (Condi-
tion (A)). This implies that the weighted complex is a PL ball for arrangements satisfying Condi-
tion (A).
5.1
Shellable polytopal complexes
We introduce the following deﬁnition. For instance, see [Bj¨o+99, Deﬁnition 4.7.14].
Deﬁnition 5.1.1. A pure n-dimensional polytopal complex ∆is shellable if it is 0-dimensional
(and hence a collection of a ﬁnite number of points), or if there is a linear order of the facets
F1, F2, . . . , Fk of ∆, called a shelling order, such that:
(i) The boundary complex of F1 is shellable.
(ii) For 1 ă j ď k the intersection of Fj with the union of the closures of the previous facets is
nonempty and is the beginning of a shelling of the pn ´ 1q-dimensional boundary complex
of Fj, that is,
Fj X pF1 Y F2 Y ¨ ¨ ¨ Y Fj´1q “ G1 Y G2 Y ¨ ¨ ¨ Y Gr,
where G1, G2, . . . , Gr, . . . , Gt is a shelling order of BFj and r ě 1.
We then have the following result.
Theorem 5.1.2. ([Bj¨o+99, Theorem 4.3.3].) Let H be a central hyperplane arrangement on V ,
let L “ L pHq and T “ T pHq, and let B be a chamber in T . Then any linear extension of the
chamber poset with base chamber B is a shelling order on the facets of ΣpL q.
Let H be a central hyperplane arrangement on V . We write L “ L pHq and T “ T pHq. Let
B P T , and let B “ T1, T2, . . . , Tr “ ´B be a linear ordering of T reﬁning the partial order ĺB.
By Theorem 5.1.2 the linear order T1, T2, . . . , Tr is a shelling order of the chambers of ΣpL q. In
particular, the shelling order deﬁnes a partition of the faces of ΣpL q:
L “
r
ž
i“1
tC P L : C ď Ti and C ę Tj for 1 ď j ă iu.
We will give a formula for the blocks of this partition (see Proposition 5.1.5) which implies in
particular that the partition is independent of the linear reﬁnement of ĺB.
27


## Page 28


Deﬁnition 5.1.3. Given a chamber B P T , we deﬁne a function fB from the face poset L to the
set of chambers T by fBpCq “ C ˝ B.
The next proposition gives some basic properties of the function fB.
Proposition 5.1.4. The following two statements hold:
(i) Fix a face C P L and consider the poset isomorphism ιC : LěC
„
ÝÑ LHpCq of Lemma 2.1.3.
If B P T X LěC then for every D P LěC we have ιCpfBpDqq “ fιCpBqpιCpDqq.
(ii) Suppose that H is a Coxeter arrangement with a chamber B that is on the positive side
of every hyperplane, and let pW, Sq be the associated Coxeter system. Identify L with the
Coxeter complex ΣpWq as in Subsection 2.2. If the face C P L corresponds to a standard
coset c Ă W, then the element w P W corresponding to the chamber fBpCq is the shortest
element of c and also the minimal element of the coset c in the right weak Bruhat order.
In particular, part (ii) implies that, for the type A Coxeter complex, the function fB deﬁned
here (for B the chamber corresponding to 1 P W) is equal to the function f deﬁned at the beginning
of [EMR19, Section 4]. Note that the existence of a minimal element in every standard coset is
proved in [BB05, Proposition 2.4.4].
Proof of Proposition 5.1.4. Statement (i) follows immediately from Lemma 2.1.3.
We now prove (ii). By deﬁnition of the composition ˝, the chamber fBpCq “ C ˝ B is the
element of T X LěC closest to B in the chamber graph; in other words, it is the minimal element
of T X LěC for the order ĺB; see Subsection 2.1. As we know that ĺB corresponds to the right
weak Bruhat order on W (see the discussion after Theorem 2.2.1), and as the elements of W
corresponding to the chambers of T X LěC are the elements of the coset c, the result follows.
The link between the function fB and the shellings of Theorem 5.1.2 is established in the
following proposition. For the type A Coxeter complex, this result appeared implicitly in the proof
of [EMR19, Proposition 4.1].
Proposition 5.1.5. Let B P T , and let B “ T1, T2, . . . , Tr “ ´B be a linear ordering of T reﬁning
the partial order ĺB. Then for every index 1 ď i ď r the ﬁber of fB over Ti is given by
f ´1
B pTiq “ tC P L : C Ă T i ´ pT 1 Y T 2 Y ¨ ¨ ¨ Y T i´1qu
(5.1)
“ tC P L : C ď Ti and C ę Tj for 1 ď j ă iu.
(5.2)
Proof. The equivalence between equalities (5.1) and (5.2) is an immediate consequence of the
deﬁnition of the order ď on L . Let us prove equality (5.2).
Let C P f ´1
B pTiq, that is, C ˝ B “ Ti. In particular, we have C ď C ˝ B “ Ti. Suppose that
T P T is another chamber such that C ď T. Then for every e P SpB, Tiq we have spTiqe ‰ spBqe,
but spC ˝ Bqe “ spTiqe, so 0 ‰ spCqe “ spTiqe. As C ď T, this implies that spTqe “ spCqe “
spTiqe ‰ spBqe, hence that e P SpB, Tq. So we have proved that SpB, Tiq Ď SpB, Tq, which means
that Ti ĺB T. In particular, if 1 ď j ď i ´ 1 then C ę Tj.
Conversely, let C P L be such that C ď Ti and C ę Tj for 1 ď j ă i, and let T “ C ˝ B. If
e P SpB, Tq then 0 ‰ spCqe “ spTqe. As C ď Ti, this implies that spCqe “ spTiqe, so spTiqe “
spCqe “ spTqe ‰ spBqe, that is, e P SpB, Tiq. So we have proved that SpB, Tq Ď SpB, Tiq, which
means that T ĺB Ti. Hence there exists an index 1 ď i1 ď i such that T “ Ti1. As C ď T and
C ę Tj for 1 ď j ă i, we must have i1 “ i, that is, fBpCq “ C ˝ B “ T “ Ti.
28


## Page 29


5.2
A condition on hyperplane arrangements
We now introduce a geometric condition on the hyperplane arrangement H that will imply the
shellability of the weighted complex.
Condition (A). Denote by (A) the following condition on the family pαeqePE (or the corresponding
arrangement): For every T P T and for every e P E such that S “ T X Hαe is of dimension
dimpV q ´ 1, that is, S is a facet of the convex cone T, the following inclusions hold:
T Ď ˚S ` Rą0αe if T Ď H`
αe,
T Ď ˚S ` Ră0αe if T Ď H´
αe,
where ˚S is the relative interior of the cone S, that is, the interior of S in SpanpSq.
Geometrically, Condition (A) means that if T P T then the dihedral angle between any two
adjacent facets (facets whose intersection is a face of dimension dimpV q´2) of the convex polyhedral
cone T is acute, that is, less than or equal to π{2.
Proposition 5.2.1. Suppose that the arrangement H satisﬁes Condition (A). Let T, T 1 P T and
e P E such that SpT, T 1q “ teu, the inner product pαe, λq is nonnegative and the inclusion T 1 Ă H´
αe
holds. Then T 1 P Lλ implies that T P Lλ.
Proof. The hypothesis implies that T XT
1 “ T XHαe “ T
1XHαe. We denote this intersection by S.
It is a facet of both T and T
1. By Condition (A), we have T Ă ˚S ` Rą0αe and T 1 Ă ˚S ` Ră0αe.
In particular, if x P T then there exists c ą 0 such that x ´ c ¨ αe P T 1. Then we have px, λq “
px ´ c ¨ αe, λq ` c ¨ pαe, λq ě 0. This implies that T Ă H`
λ , that is, T P Lλ.
Corollary 5.2.2. Suppose that the arrangement H satisﬁes Condition (A). If pλ, αeq ě 0 for every
e P E and if there exists B P T such that B Ă H`
αe for every e P E, then T X Lλ is a lower order
ideal in TB. More generally, if C P L and EpCq “ te P E : C Ă Hαeu, if pλ, αfq ě 0 for every
f P EpCq and if there exists B P T XLěC such that B Ă H`
αf for every f P EpCq, then T XLλ,ěC
is a lower order ideal in TB.
Proof. It suﬃces to prove the second statement. Let T, T 1 be such that SpB, Tq Ă SpB, T 1q and
T 1 P Lλ,ěC. We want to show that T P Lλ,ěC. As TB is a graded poset and the intersection
T X LěC is a lower order ideal in TB (see Remark 2.1.4), we know that T P T X LěC, and it
suﬃces to treat the case where SpT 1, Bq ´ SpT, Bq is a singleton. Let f be the single index of
SpB, T 1q ´ SpB, Tq. As B, T 1 P T X LěC, we have f P EpCq by Lemma 2.1.3(iii), so B Ă H`
αf . As
f P SpB, T 1q ´ SpB, Tq, we have T 1 Ă H´
αf and T Ă H`
αf . Also, as f P EpCq, we have pλ, αfq ě 0.
So we may apply Proposition 5.2.1, and we obtain that T P Lλ.
Corollary 5.2.3. Suppose that the arrangement H satisﬁes Condition (A). Then the complex ΣpLλq
is shellable. Moreover, there exists a shelling order on its chambers which is an initial shelling
of ΣpL q. In particular, if λ ‰ 0 then ΣpLλq is a shellable PL ball of dimension dimpV {V0q ´ 1.
Proof. If λ “ 0 then Lλ “ L and ΣpLλq “ ΣpL q, and the corollary is just Theorem 5.1.2.
We now assume that λ ‰ 0. By Theorem 5.1.2 and Corollary 5.2.2, it suﬃces to ﬁnd a family
of signs pεeq P t˘1uE such that:
29


## Page 30


– for every e P E, we have pλ, εeαeq ě 0;
– there exists a chamber B P Lλ with B Ă H`
εeαe for every e P E.
Indeed, Corollary 5.2.2 will then imply that T X Lλ is a lower order ideal in TB, so it will be an
initial segment for at least one linear extension of ĺB.
Let F “ te P E : pλ, αeq ‰ 0u. For every e P F, we choose εe P t˘1u such that pλ, εeαeq ą 0.
Let x0 be a point in V not on any hyperplane of H, that is, x0 P V ´ Ť
ePE Hαe. Then for every
e P F, the inner product px0 ` c ¨ λ, εeαeq “ px0, εeαeq ` c ¨ pλ, εeαeq tends to `8 as c tends to `8,
so it is positive for c large enough. Similarly, the inner product px0 ` c ¨ λ, λq “ px0, λq ` c ¨ pλ, λq
is positive for c large enough. On the other hand, if e P E ´ F, then px0 ` c ¨ λ, αeq “ px0, αeq ‰ 0
for every c P R. So, if c P R is large enough, then x “ x0 ` c ¨ λ P V ´ Ť
ePE Hαe, and x is in H`
εeαe
for every e P F and in H`
λ . In particular, there exists a chamber B P T such that x P B, and B
is included in H`
εeαe for every e P F and in H`
λ . Now, if e P E ´ F, we choose εe P t˘1u such that
B Ă H`
εeαe. As pλ, αeq “ 0, we clearly have pλ, εeαeq ě 0.
5.3
The case of Coxeter arrangements
Lemma 5.3.1. Every Coxeter arrangement H satisﬁes Condition (A).
Proof. In a Coxeter arrangement, the dihedral angle between any two adjacent facets is π{n, with
n ě 2.
In particular, Corollaries 5.2.2 and 5.2.3 apply to Coxeter arrangements. But we can actually
prove a stronger result in this case.
We ﬁx a Coxeter arrangement H on an inner product space V , and we use the notation intro-
duced above. We say that a vector λ P V is dominant if pλ, αq ě 0 for every α P Φ`.
Lemma 5.3.2. Suppose that λ P V is dominant. Denote by B the chamber of H corresponding to
1 P W. Let z, w P W such that z ď w in the strong Bruhat order of W. Then for every x P B the
following inequality holds:
pz´1pλq, xq ě pw´1pλq, xq.
Proof. We may assume that w covers z, so that there exists s P S and u P W such that w “
pusu´1qz. Let α be the unique pseudo-root of Φ` such that upesq is a multiple (positive or negative)
of α. If sα is the reﬂection across Hα, we have usu´1 “ sα, and so w “ sαz and sαw “ z. Since
the elements of Φ` are unit vectors, sα is given by the following formula: sαpµq “ µ ´ 2 ¨ pµ, αq ¨ α
for µ P V . Hence
psαwq´1pλq “ pw´1sαqpλq “ w´1pλq ´ 2 ¨ pλ, αq ¨ w´1pαq,
and so, if x P B,
ppsαwq´1λ, xq “ pw´1pλq, xq ´ 2 ¨ pλ, αq ¨ pw´1pαq, xq.
As λ is dominant, we have pλ, αq ě 0.
By [BB05, Equation (4.25)], we have the equivalence
w´1pαq P Φ` ðñ ℓpw´1sαq ą ℓpw´1q, and [BB05, Proposition 1.4.2(iv)] states that ℓpv´1q “ ℓpvq
for every v P W. Using these two facts and the condition ℓpsαwq ă ℓpwq, we see that w´1pαq P Φ´.
Thus pw´1pαq, xq ă 0 by deﬁnition of B. Hence the term ´2 ¨ pλ, αq ¨ pw´1pαq, xq is nonnegative,
that is, pz´1pλq, xq “ ppsαwq´1pλq, xq ě pw´1pλq, xq.
30


## Page 31


Proposition 5.3.3. Let pW, Sq be a Coxeter system, and let H “ pHαqαPΦ` be the associated
hyperplane arrangement on the space V of the canonical representation of pW, Sq. Let λ P V be
a dominant vector. Then the set Wλ of w P W such that the corresponding chamber of H is in
T X Lλ is a lower order ideal with respect to the strong Bruhat order on W.
Proof. We denote by B the chamber of H corresponding to 1 P W.
By deﬁnition of Wλ, an
element w of W is in Wλ if and only if for every x P B we have pλ, wpxqq “ pw´1pλq, xq ě 0. By
Lemma 5.3.2, if z, w P W and w is greater than z in the strong Bruhat order then for every x P B,
we have pz´1pλq, xq ě pw´1pλq, xq. If moreover w P Wλ, this immediately implies that z P Wλ.
6
Concluding remarks
As mentioned in the introduction, we are not aware of whether there is a representation-theoretic
interpretation of the identity in Theorem 4.2.2 in general. More precisely, what is the meaning of
the constants ψH{CpB, λq for diﬀerent values of λ?
The main results in this paper are in the setting of Coxeter arrangements.
However, the
sum ψH makes sense for general hyperplane arrangements, our original proof of Theorem 4.2.2
used an induction formula that linked the sum ψH to similar sums for subarrangements of the
restricted arrangements on the hyperplanes of H, and this induction formula is valid for general
hyperplane arrangements, and with some adaptions, for oriented matroids. In the paper [EMR21b],
we use a similar type of induction argument, this time to calculate the alternating sum of another
valuation on the chambers of a hyperplane arrangement, that is, the volume of the intersection
of the chamber with some set of ﬁnite volume. Is there is some analogue of 2-structures for more
general hyperplane arrangements?
It is natural to ask is there some analogue of Theorem 3.2.1 for Coxeter systems with possible
inﬁnite Coxeter groups?
In Section 5 we prove that the weighted complexes of a hyperplane arrangement are shellable
under a geometric condition on the arrangement that we call Condition (A). This implies that
the weighted complexes are PL balls for arrangements satisfying Condition (A). Are the weighted
complexes always PL balls? By Remark 4.1.2, this extends a conjecture of Zaslavsky (see [Zas75,
Chapter I, Section 3C, p. 33]) that the bounded complex of a simple hyperplane arrangement is
always a PL ball. As a consequence to Corollary 5.2.3, we have the following result.
Corollary 6.1. Zaslavsky’s conjecture holds for aﬃne arrangements obtained by intersecting an
aﬃne hyperplane with an arrangement satisfying Condition (A).
In a paper of Dong (see [Don08]) he claims to have proven Zaslavsky’s conjecture. However,
we do not understand the proof of the crucial Lemma 4.7 in that paper: In the second paragraph
of case 2, Dong chooses a linear extension ď of T pL {g, diq such that rdi, djs is an initial segment.
This linear extension is a shelling order, and Dong deduces that there exists dk P rdi, djq such that
dk ^ dj Ì dj. But the only thing that we can deduce from the fact that we have a shelling order
is that di ď dk ă dj, which does not imply that dk P rdi, djq for the order on T pL {g, diq. If we do
not know that dk P rdi, djq, the rest of the argument fails.
In Appendix A we construct a ring structure on the set of valuations on convex closed polyhedral
cones with values in a ﬁxed ring. Are there other products of valuations that also yield valuations?
For instance, can the ring structure of Corollary A.1.7 be extended to valuations on (not necessarily
polyhedral) cones in Euclidean space?
31


## Page 32


In Appendix B the proof of Proposition B.2.4 that the group W acts transitively on the set of
2-structures T consists of verifying the result for all irreducible pseudo-root systems. Is there a
general proof that does not use the classiﬁcation of irreducible pseudo-root systems?
A
Extending the construction of a valuation by Goresky, Kottwitz
and MacPherson
We introduce a ring structure on the set of valuations deﬁned on closed convex polyhedral cones
in a ﬁnite-dimensional real vector space with values in a ﬁxed ring. As a special case we obtain
in Corollary A.1.11 a valuation due to Goresky, Kottwitz and MacPherson; see [GKM97, Proposi-
tion A.4].
Subsection A.1 of this appendix contains deﬁnitions and statements of results. The proofs are
relegated to Subsection A.2.
A.1
The ring of valuations
Let V be a ﬁnite-dimensional real vector space and V _ its dual. A closed convex polyhedral cone
in V is a nonempty subset of the form Rě0v1 ` Rě0v2 ` ¨ ¨ ¨ ` Rě0vk, where v1, v2, . . . , vk P V and
k ě 0.
For a subset X of the space V , deﬁne XK “ tα P V _ : @x P X xα, xy “ 0u and X˚ “ tα P
V _ : @x P X xα, xy ě 0u. Note that XK is a subspace of V _ and depends only on the linear span
of X, and that X˚ is a convex cone in V _ and depends only on the closed convex polyhedral cone
generated by X.
For F a face4 of a closed convex polyhedral cone K, deﬁne F K,K “ F K X K˚.
The map
F ÞÝÑ F K,K is an order-reversing bijection from the set FpKq of faces of K to the set of faces
of K˚. This statement and other basic properties of closed convex polyhedral cones are proved
in [Ful93, Section 1.2].
Remark A.1.1. For two closed convex cones X1 and X2 such that X1 Y X2 is convex then the set
X˚
1 Y X˚
2 is also convex and we have the two identities
pX1 Y X2q˚ “ X˚
1 X X˚
2
and
pX1 X X2q˚ “ X˚
1 Y X˚
2 .
Deﬁnition A.1.2. We denote by CpV q the set of closed convex polyhedral cones in V . Denote
the free abelian group on CpV q by À
KPCpV q ZrKs and let KpV q be its quotient by the relations
rK Y K1s ` rK X K1s “ rKs ` rK1s for all K, K1 P CpV q such that K Y K1. For K P CpV q, we still
denote its image in KpV q by rKs.
For λ P V _, we deﬁne the hyperplane Hλ and the two open half-spaces H`
λ and H´
λ by
Hλ “ tx P V : xλ, xy “ 0u,
H`
λ “ tx P V : xλ, xy ą 0u
and
H´
λ “ tx P V : xλ, xy ă 0u.
The closed half-spaces are given by H`
λ “ tx P V : xλ, xy ě 0u and H´
λ “ tx P V : xλ, xy ď 0u.
4In this appendix, we take all faces to be closed faces, unlike in the rest of the article.
32


## Page 33


Deﬁnition A.1.3. A valuation on CpV q with values in an abelian group A is a function f :
CpV q ÝÑ A such that fp∅q “ 0 and that for any K, K1 P CpV q such that K Y K1 P CpV q, we have
fpK Y K1q ` fpK X K1q “ fpKq ` fpK1q.
(A.1)
By the deﬁnition of KpV q, saying that a function f : CpV q ÝÑ A is a valuation is equivalent
to saying that there exists a morphism (necessarily unique) KpV q ÝÑ A sending rKs to fpKq for
every K P CpV q. We also denote this morphism KpV q ÝÑ A by f.
Example A.1.4. By Remark A.1.1, the function δ : CpV q ÝÑ KpV _q sending K P CpV q to rK˚s is
a valuation. Thus it induces a morphism δ : KpV q ÝÑ KpV ˚q.
We have the following criterion for recognizing valuations on closed convex polyhedral cones.
This is known as Groemer’s ﬁrst extension theorem and is proved in [Gro78, Theorem 2].
Theorem A.1.5 (Groemer). Let A be an abelian group and f : CpV q ÝÑ A be a function such
that fp∅q “ 0. Suppose that for every K P CpV q and every µ P V _ the following holds:
fpKq ` fpK X Hµq “ f
`
K X H`
µ
˘
` f
`
K X H´
µ
˘
.
(A.2)
Then the function f is a valuation.
The main result of this appendix is the following theorem whose proof is in Subsection A.2.
To make the notation more compact in this appendix, we denote the linear span of a subset S of
vector space by xSy.
Theorem A.1.6.
(i) Consider the function ∆: CpV q ÝÑ KpV q bZ KpV q deﬁned by
∆pKq “
ÿ
F PFpKq
p´1qdim FrFs b rxFy ` Ks,
for every K P CpV q.
Then ∆is a valuation and it induces a morphism ∆: KpV q ÝÑ
KpV q bZ KpV q. Moreover this morphism ∆is coassociative, that is, we have
p∆b idKpV qq ˝ ∆“ pidKpV q b∆q ˝ ∆.
(ii) Consider the function ε : CpV q ÝÑ Z deﬁned by εpKq “ p´1qdim K if K is a vector subspace
of V and εpKq “ 0 otherwise. Then ε is a valuation and it induces a morphism ε : KpV q ÝÑ
Z. This morphism is a counit of ∆, in other words, we have
pε b idKpV qq ˝ ∆“ idKpV q “ pidKpV q bεq ˝ ∆.
In short, Theorem A.1.6 says that the morphisms ∆: KpV q ÝÑ KpV q bZ KpV q and ε :
KpV q ÝÑ Z are well-deﬁned and make KpV q into a Z-coalgebra.
Corollary A.1.7. Let A be a ring. Let f1, f2 : CpV q ÝÑ A be two valuations. Then the function
f1 ˚ f2 : CpV q ÝÑ A deﬁned by
pf1 ˚ f2qpKq “
ÿ
F PFpKq
p´1qdim Ff1pFqf2pxFy ` Kq
is also a valuation. This operation ˚ makes the group of valuations CpV q ÝÑ A into a ring. The
unit element of this ring is the composition of ε : CpV q ÝÑ Z and the canonical ring morphism
Z ÝÑ A.
33


## Page 34


Proof. The valuations f1 and f2 induce two morphisms f1, f2 : KpV q ÝÑ A, hence a morphism
f1 b f2 : KpV q bZ KpV q ÝÑ A, x b y ÞÑ f1pxq b f2pyq. As we have
pf1 ˚ f2qpKq “ pf1 b f2qp∆prKsqq
for every K P CpV q, this shows that f1 ˚ f2 descends to a morphism KpV q ÝÑ A, hence is a
valuation.
The operation ˚ is clearly linear in each variable, and it is associative by the coassociativity
of ∆. The last statement follows immediately from the fact that ε is a counit of ∆.
Corollary A.1.8. Let A be a ring, and let f1 : CpV q ÝÑ A and g2 : CpV _q ÝÑ A be valuations.
Then the function f1 ‹ g2 : CpV q ÝÑ A deﬁned by
pf1 ‹ g2qpKq “
ÿ
F PFpKq
p´1qdim F f1pFqg2pF K,Kq
is also a valuation.
Proof. Consider the valuation δ : CpV q ÝÑ KpV _q of Example A.1.4. Then the map f2 “ g2 ˝ δ :
CpV q ÝÑ A is also a valuation. As F K,K “ pxFy ` Kq˚ for every K P CpV q and every face F of K,
we have f1 ‹ g2 “ f1 ˚ f2, so the statement follows from Corollary A.1.7.
Remark A.1.9. Let H be a central hyperplane arrangement on V , let CHpV q be the set of closed
convex polyhedral cones that are intersections of closed half-spaces bounded by hyperplanes of H,
and let KHpV q be the quotient of the free abelian group À
KPCHpV q ZrKs on CHpV q by the relations
r∅s “ 0 and rKs`rK1s “ rKYK1s`rKXK1s for all K, K1 P CHpV q such that KYK1 P CHpV q. Then
the formulas of Theorem A.1.6 also deﬁne a coalgebra structure on KHpV q. Indeed, if K P CHpKq
and F P FpKq, then F and xFy ` K are also in CHpV q.
In particular, the products in Corollaries A.1.7 and A.1.8 also make sense if the ﬁrst valuation
is only deﬁned on CHpV q.
We now explain how to use Corollary A.1.8 to recover [GKM97, Proposition A.4].
Lemma A.1.10. Let X be a subset of V such that the complement V ´ X is convex. Then the
function φX : CpV q ÝÑ Z deﬁned by
φXpKq “
#
1
if H Ĺ K Ď X,
0
otherwise,
is a valuation. In particular, if λ P V _ then the function ψλ “ φH`
λ is a valuation.
Proof. Let K P CpV q be nonempty and let µ P V _. Let K0 “ K X Hµ, K` “ K X H`
µ and
K´ “ K X H´
µ . We must check Criterion (A.2) in Theorem A.1.5, that is, φXpKq ` φXpK0q “
φXpK`q ` φXpK´q.
If K Ď X then K0, K` and K´ are also included in X, and the equality above is clear. If
K` Ď X but K´ Ę X, then K0 Ď X and K Ę X, so again the desired equality holds. The case
where K´ Ď X and K` Ę X is symmetric. Finally, suppose that K`, K´ Ę X. Then K Ę X, and
so we must show that K0 Ę X. Take x P K` ´ X and y P K´ ´ X. Then the segment rx, ys is
contained in the convex set V ´ X. As this segment intersects K0, this shows that K0 Ę X.
34


## Page 35


Given x P V and λ P V _, we have two valuations ψλ : CpV q ÝÑ Z and ψx : CpV _q ÝÑ Z
deﬁned in Lemma A.1.10. Let K ÞÝÑ ψKpx, λq be the function deﬁned by
ψKpx, λq “ pψλ ‹ ψxqpKq
for every K P CpV q. This function is deﬁned in [GKM97, Appendix A] (at the top of page 540).
Corollary A.1.11. For every x P V and every λ P V _, the function K ÞÝÑ ψKpx, λq from CpV q
to R is a valuation.
Since any valuation satisﬁes the additivity property, we obtain the next corollary [GKM97,
Proposition A.4].
Corollary A.1.12 (Goresky–Kottwitz–MacPherson). Let K be a closed convex polyhedral cone.
Suppose that its relative interior K˝ is the disjoint union of the relative interiors K˝
1, K˝
2, . . . , K˝
r
of r closed convex polyhedral cones K1, K2, . . . , Kr. Then for every x P V and every λ P V _
ψKpx, λq “
rÿ
i“1
p´1qdimpKq´dimpKiq ¨ ψKipx, λq.
Remark A.1.13. Valuations on CpV q can be extended to relatively open cones as well. Let G be a
collection of sets that is closed under ﬁnite intersections. Deﬁne BpGq to be the Boolean algebra
generated by G, that is, the smallest collection of sets that contains G and is closed under ﬁnite
unions, ﬁnite intersections and complements. Groemer’s Integral Theorem states that a valuation
on G can be extended to a valuation on the Boolean algebra BpGq; see [Gro78] and also [KR97,
Chapter 2]. In the case where G “ CpV q, that is, the collection of closed convex polyhedral cones
in E, the associated Boolean algebra BpCpV qq contains all cones that are obtained by intersecting
closed and open half-spaces.
Remark A.1.14. The results of this appendix extend to oriented matroids without much change.
Let E be a ﬁnite set and consider an oriented matroid M on E with set of covectors L Ď t`, ´, 0uE.
This set of covectors forms a graded poset with the partial order given by componentwise comparing
the entries by 0 ă ` and 0 ă ´. We denote its rank function by ρ. For every F Ď E and every
s P t`, ´, 0uF , we write Lďs “ tx P L : x|F ď su. Let K be the set of lower order ideals of L
of the form Lďs. We order K by inclusion. If L is the oriented matroid corresponding to a
central hyperplane arrangement H on V , then K is the set cones obtained by intersecting closed
half-spaces bounded by hyperplanes of H. In general, every element of K is of the form Lďx|F for
some x P L and F Ď E.
We say that an element a of K is a vector subspace if a ‰ ∅and a is of the form Lďx|F , for
some x P L and some F Ď E such that xe “ 0 for every e P F.
A valuation on K with values in an abelian group A is a function f : K ÝÑ A such that
fp∅q “ 0 and, for all a, b P K such that a Y b P K , we have fpa Y bq ` fpa X bq “ fpaq ` fpbq.
Giving such a valuation is equivalent to giving a function w : L ÝÑ A; the corresponding valuation
then sends a P K to ř
xPa wpxq.
The analogue of KpV q is the quotient of the free abelian group À
aPK Zras by the relations
r∅s “ 0 and ra Y bs ` ra X bs “ ras ` rbs if a Y b P K . We denote this group by KpL q. We have
an isomorphism KpL q
„
ÝÑ À
xPL Zrxs sending ras to ř
xParxs.
35


## Page 36


Let F Ď E. We denote the set of covectors of the deletion M ´ pE ´ Fq by LF and the rank
function of LF by ρF . Let y P LF . If Fpyq “ te P F : ye “ 0u, then we have an order-preserving
bijection LF,ěy
„
ÝÑ LF pyq sending any z ě y in LF to z|F pyq. This is the analogue of Lemma 2.1.3.
We deﬁne the comultiplication ∆: KpL q ÝÑ KpL q bZ KpL q by sending rLďx|F s to
∆prLďx|F sq “
ÿ
yPLF,ďx|F
p´1qρF pyqrLďys b rLďx|F pyqs.
Let a P L . The counit ε sends ras to 0 if a is not a vector subspace. If a “ Lďx|F , with x P L
and F Ď E such that xe “ 0 for every e P F, then we set εprasq “ p´1qρF px|F q.
Remark A.1.15. Let K “ À
ně0 KpRnq. We make K into a coalgebra using the direct sum of the
morphisms ∆and ǫ of Theorem A.1.6. There is a product on K deﬁned by rKs ¨ rLs “ rK ˆ Ls if
K P CpRnq and L P CpRmq, where we identity Rn ˆ Rm and Rn`m in the usual way. This product
is associative, and the class of the cone t0u P CpR0q is a unit. It is then straightforward to see that
K is actually a bialgebra. However, it is not a Hopf algebra because if V is a vector subspace of Rn
with n ě 1, then the element p´1qdim V rV s of K is group-like but not invertible.
If K P CpRnq and F is a face of K, then the poset of faces of xFy ` K is isomorphic to the
interval rF, Ks in the poset of faces of K. So the bialgebra K is related to the incidence Hopf
algebras deﬁned by Joni and Rota in [JR79] and further studied by Schmitt in [Sch94], although,
unlike those Hopf algebras, it has signs in the deﬁnition of its coproduct. Let us make this relation
more precise. For every n ě 0, we denote by KfpRnq the free abelian group on the set of closed
convex polyhedral cones in Rn; if K P CpRnq, we denote its class in KfpRnq by rKsf. The formulas
for ∆and ǫ also deﬁne a coalgebra structure on KfpRnq and, if we set Kf “ À
ně0 KfpRnq, then
the product on Kf deﬁned by rKsf ¨ rLsf “ rK ˆ Lsf makes Kf into a coalgebra. Let P be the
set of isomorphism classes of ﬁnite posets, and let ZrPs be the free abelian group on P equipped
with the Hopf algebra structure deﬁned in Sections 3 and 4 of [Sch94]. Then we have bialgebra
morphisms π1 : Kf ÝÑ K and π2 : Kf ÝÑ ZrPs deﬁned as follows: if K P CpRnq then π1 sends
rKsf to rKs and π2 sends rKsf to p´1qd times the class of the poset of faces of K, where d is the
dimension of the largest vector subspace contained in K.
A.2
Proofs
Before proving Theorem A.1.6, we state and prove the following lemma.
Lemma A.2.1. Let K Ď V be a closed convex polyhedral cone, let F be a closed face of the cone K
and let µ P V _. We write K0 “ K X Hµ, K` “ K X H`
µ and K´ “ K X H´
µ .
(a) Assume that F Ď H`
µ but F Ę Hµ, that is, F is a face of K` but not of K0. Then the equality
xFy ` K “ xFy ` K` holds.
(b) Assume that F X H`
µ ‰ ∅and F X H´
µ ‰ ∅, in other words, the hyperplane Hµ cuts the face
F in two. Then the equality xFy ` K “ xFy ` K0 holds.
(c) In the situation of (b), let F0 “ F X Hµ. Then the equality xF0y ` K “ xFy ` K holds.
(d) Let X be a subset of V . Then X ` K “ pX ` K`q Y pX ` K´q. If moreover X Ď Hµ, we
also have X ` K0 “ pX ` K`q X pX ` K´q.
36


## Page 37


(a)
Hµ
K`
K0
K´
(b)
Spiq
Spiiiq
1st term of Spivq
3rd term of Spivq
Figure 2: A two-dimensional representation of a ﬁve-sided three-dimensional cone K. In (b) the
four diﬀerent contributions to gpK`q are marked.
Proof. We ﬁrst prove (a). The inclusion xFy`K` Ď xFy`K clearly holds, so we just need to show
the reverse inclusion. Let x P xFy ` K, and write x “ y ` z, with y P xFy and z P K. As F Ę Hµ,
there exists y1 P F such that xµ, y1y ą 0. Then for a P Rą0 large enough we have xµ, ay1 ` zy ě 0,
hence ay1 ` z P K`. As x “ py ´ ay1q ` pay1 ` zq, this shows that x P xFy ` K`.
We now prove (b). The inclusion xFy ` K0 Ď xFy ` K clearly holds, so we just need to verify
the reverse inclusion. Let x P xFy ` K, and write x “ y ` z with y P xFy and z P K. By the
assumption on F, the image of F by µ is not contained in Rě0 or in Rď0; as this image is a cone
in R, we conclude that it is equal to R. In particular, we can ﬁnd y1 P F such that xµ, y1y “ ´xµ, zy.
Then x “ py ´ y1q ` py1 ` zq with y ´ y1 P xFy, y1 ` z P K and xµ, y1 ` zy “ 0, hence x P xFy ` K0.
We prove (c). The inclusion xF0y ` K Ď xFy ` K is clear, so we need to show the reverse
inclusion. By the proof of (b), the image of F by µ is equal to R, so we can ﬁnd y1 P F such that
xµ, y1y “ xµ, yy. Then x “ py ´ y1q ` py1 ` zq with y ´ y1 P xFy, y1 ` z P K and xµ, y ´ y1y “ 0, hence
x P xF0y ` K.
Finally, we prove (d). The inclusion pX ` K`q Y pX ` K´q Ď X ` K is clear. Conversely, let
x P X`K, and write x “ y`z with y P X and z P K. Then either z P K`, in which case x P X`K`,
or z P K´, in which case x P X ` K´. The inclusion X ` K0 Ď pX ` K`q X pX ` K´q is also clear
and holds without any condition on X. Assume that X Ď Hµ, and let x P pX ` K`q X pX ` K´q.
Write x “ y1 ` z1 “ y2 ` z2, with y1, y2 P X, z1 P K` and z2 P K´. Then xµ, y1y “ xµ, y2y “ 0, so
xµ, z1y “ xµ, xy ´ xµ, y1y “ xµ, xy ´ xµ, y2y “ xµ, z2y.
As xµ, z1y ě 0 and xµ, z2y ď 0, this implies that xµ, z1y “ xµ, z2y “ 0, hence that z1, z2 P K0, and
so x P X ` K0.
Proof of Theorem A.1.6. We ﬁrst show that ∆: CpV q ÝÑ KpV q bZ KpV q and ε are valuations.
We check the criterion of Theorem A.1.5. Let K P CpV q and let µ P V _. We deﬁne as before three
closed convex polyhedral cones K` “ K X H`
µ , K´ “ K X H´
µ , K0 “ K X Hµ. We show that
εpKq ` εpK0q “ εpK`q ` εpK´q.
(A.3)
37


## Page 38


If K` “ K0 then K “ K´ so equation (A.3) is clear. The case where K´ “ K0 is similar. Suppose
that K` ‰ K0 and K´ ‰ K0. Then the image of K` by µ is Rě0, so K` cannot be a vector subspace
of V , and similarly K´ cannot be a vector subspace of V . This implies that εpK`q “ εpK´q “ 0,
so equation (A.3) holds if and only if εpKq “ ´εpK0q. As K0 is strictly included in K, we have
dimpK0q “ dimpKq ´ 1, so we need to prove that K is a vector subspace if and only if K0 is. If K
is a vector subspace of V then so is K0. Suppose that K0 is a vector subspace of V . We want
to prove that K also is a vector subspace of V . Without loss of generality we may assume that
xKy “ V . As K` ‰ K0 and K´ ‰ K0, the hyperplane Hµ meets the relative interior of K, and so
xK0y “ Hµ, hence Hµ “ K0 Ď K. As K contains points in both open half-spaces cut out by Hµ,
this implies that K “ V .
We now treat the case of ∆. The faces F of the cone K come in four disjoint categories. For
each category, we consider the contribution to the sum deﬁning ∆pKq.
(i) F is a face of K`, but not of K0, that is, F ˝ Ď H`
µ . Then by Lemma A.2.1(a) we have
xFy ` K “ xFy ` K`. Hence the contribution is
Spiq “
ÿ
F PFpKqXFpK`q
F RFpK0q
p´1qdimpF q ¨ rFs b rxFy ` Ks
“
ÿ
F PpFpK`qXFpKqq´FpK0q
p´1qdimpF q ¨ rFs b rxFy ` K`s
(ii) F is a face of K´, but not of K0, that is, F ˝ Ď H´
µ . As in case (i), we have xFy`K “ xFy`K´,
and the contribution is
Spiiq “
ÿ
F PFpKqXFpK´q
F RFpK0q
p´1qdimpF q ¨ rFs b rxFy ` Ks
“
ÿ
F PpFpK´qXFpKqq´FpK0q
p´1qdimpF q ¨ rFs b rxFy ` K´s
(iii) F is a face of all three cones K`, K´ and K0, that is, we have F Ď Hµ. Here the contribution
is
Spiiiq “
ÿ
F PFpKq
F ĎHµ
p´1qdimpF q ¨ rFs b rxFy ` Ks
“
ÿ
F PFpK`qXFpK´qXFpK0q
p´1qdimpF q ¨ rFs b
`
rxFy ` K`s ` rxFy ` K´s ´ rxFy ` K0sq
˘
,
since xFy ` K “ pxFy ` K`q Y pxFy ` K´q and xFy ` K0 “ pxFy ` K`q X pxFy ` K´q by
Lemma A.2.1(d).
(iv) The face F gets cut into three faces: F` “ F X K` in K`, F´ “ F X K´ in K´ and
F0 “ F X K0 in K0. Then we have xFy “ xF`y “ xF´y. By Lemma A.2.1(b), we have
xFy ` K “ xFy ` K0, and so
xFy ` K “ xF`y ` K` “ xF´y ` K´ “ xFy ` K0.
38


## Page 39


By Lemma A.2.1(c), we also have xFy ` K “ xF0y ` K, and by Lemma A.2.1(d) we have
rxF0y ` Ks “ rxF0y ` K`s ` rxF0y ` K´s ´ rxF0y ` K0s. So the contribution is
Spivq “
ÿ
F PFpKq
F being cut
p´1qdimpF q ¨ rFs b rxFy ` Ks
“
ÿ
F PFpKq
F being cut
p´1qdimpF q ¨ prF`s ` rF´s ´ rF0sq b rxFy ` Ks
“
ÿ
F PFpKq
F being cut
p´1qdimpF q ¨ prF`s b rxF`y ` K`s ` rF´s b rxF´y ` K´s ´ rF0s b rxF0y ` Ksq
“
ÿ
F PFpKq
F being cut
p´1qdimpF q ¨
ˆ
rF`s b rxF`y ` K`s ` rF´s b rxF´y ` K´s
´ rF0s b rxF0y ` K`s ´ rF0s b rxF0y ` K´s ` rF0s b rxF0y ` K0s
˙
.
Now expand ∆pKq as Spiq `Spiiq `Spiiiq`Spivq. We use use the fact that p´1qdimpF q “ ´p´1qdimpF0q
in the third, fourth and ﬁfth terms of Spivq. The contributions to ∆pK`q, respectively ∆pK´q, are
given by the sum Spiq, respectively Spiiq, the ﬁrst term in the sum Spiiiq, respectively the second
term, and the ﬁrst and third terms in the sum Spivq, respectively the second and fourth terms. See
Figure 2 (b). Finally, the third term of the sum Spiiiq and the ﬁfth term of the sum Spivq yield the
sum for ´∆pK0q, which proves that ∆pKq “ ∆pK`q ` ∆pK´q ´ ∆pK0q.
We now prove that ∆is coassociative. Let K P CpV q. Then
p∆b idKpV qqp∆pKqq “ p∆b idKpV qq
¨
˝
ÿ
F PFpKq
p´1qdim F rFs b rxFy ` Ks
˛
‚
“
ÿ
F PFpKq
ÿ
GPFpF q
p´1qdim F `dim GrGs b rxGy ` Fs b rxFy ` Ks.
We want to compare this expression with pidKpV q b∆qp∆prKsqq. To calculate this last expression,
we need a description of the faces of the cone xGy ` K, where G is a face of K. Let H be the
collection of hyperplanes containing a facet of K. Then H is a ﬁnite central hyperplane arrangement
on V and, as in Subsection 2.1, we write L “ L pHq and T “ T pHq. Let C and T be the relative
interiors of G and K respectively. We have C P L and T P T X LěC, and there is a bijection
tD P LěC : D ď Tu
„
ÝÑ tF P FpKq : G Ď Fu sending D to D. Let HpCq be the subarrangement
of H whose hyperplanes are the ones containing C (or equivalently G). By Lemma 2.1.3, the cone
xGy ` K is the closure of the unique chamber of HpCq containing T, and there is a bijection from
the set tD P LěC : D ď Tu to the set of faces of xGy ` K sending D to xGy ` D. We deduce
that there is a bijection from the set tF P FpKq : G Ď Fu to FpxGy ` Kq sending F to xGy ` F.
39


## Page 40


Moreover, Lemma 2.1.3(iv) states that this bijection preserves dimensions. Thus we obtain
pidKpV q b∆qp∆pKqq “ pidKpV q b∆q
¨
˝
ÿ
GPFpKq
p´1qdim GrGs b rxGy ` Ks
˛
‚
“
ÿ
GPFpKq
ÿ
F 1PFpxGy`Kq
p´1qdim F 1`dim GrGs b rF 1s b rxF 1y ` Ks
“
ÿ
GPFpKq
ÿ
F PFpKq:GĎF
p´1qdim F `dim GrGs b rxGy ` Fs b rxFy ` Ks
“ p∆b idKpV qqp∆pKqq.
This completes the proof of the coassociativity of ∆.
We ﬁnally prove that ε is a counit of ∆. Let K P CpV q. Suppose ﬁrst that K is not a vector
subspace of V . Then the only face of K that is a vector subspace is t0u, and the only face F such
that xFy ` K is a vector subspace is K. Hence
pidKpV q bεqp∆pKqq “
ÿ
F PFpKq
p´1qdim F rFs b εprxFy ` Ksq
“ p´1qdim KrKs b εprxKysq
“ p´1qdim Kp´1qdimxKyrKs b 1 “ rKs
and
pε b idKpV qqp∆pKqq “
ÿ
F PFpKq
p´1qdim FεprFsq b rxFy ` Ks
“ p´1q0εprt0us b rKs “ rKs.
If K is a vector subspace of V then the only face of K is K itself, so ∆pKq “ p´1qdim KrKs b rKs,
and we clearly have
pidKpV q bεqp∆pKqq “ pidKpV q bεqp∆pKqq “ rKs.
B
Review of 2-structures
The concept of 2-structure for a root system was introduced by Herb to calculate discrete series
characters on real reductive groups. See for example Section 5 of [Her01] or Section 4 of the review
article [Her00]. In this section we review Herb’s constructions and adapt them so that they work
for an arbitrary Coxeter system having ﬁnite Coxeter group. We also adapt some of heer results
to this setting and give detailed elementary proofs of these results. Although this is not strictly
necessary, we think that it might be valiable, as the proofs of these results in the literature can be
very hard to follow for people not already immersed in the representation theory of real groups.
We ﬁx a ﬁnite-dimensional R-vector space V and an inner product p¨, ¨q on V .
For every
v P V ´ t0u, we denote by sv the (orthogonal) reﬂection across the hyperplane vK.
Whenever we need to describe the irreducible root systems, we use the description given in the
tables at the end of [Bou68], except that we write pe1, . . . , enq for the canonical basis of Rn. When
we need a system of positive roots in these root systems, we also use the ones given in these tables.
40


## Page 41


This appendix is organized as follows. Subsections B.1 and B.2 contain the deﬁnitions and
results respectively. Subsections B.3 and B.4 contain the technical proofs. The veriﬁcation that the
Coxeter group W acts transitively on the set of 2-structures takes place in the fourth subsection.
B.1
Pseudo-root systems
Deﬁnition B.1.1. A ﬁnite subset Φ of V ´ t0u is called a pseudo-root system if it satisﬁes the
following conditions:
(a) for every α P Φ, we have Φ X Rα “ t˘αu;
(b) for every α, β P Φ, the reﬂection sα sends β to a vector of the form cγ, with c P Rą0 and
γ P Φ.
If all the elements of Φ are unit vectors, we call Φ a normalized pseudo-root system. In that case,
condition (b) become “sαpβq P Φ”.
Remark B.1.2. We use this deﬁnition because it is convenient in the context of Coxeter systems. A
root system (in the usual sense) is a pseudo-root system, which is not normalized in general. The
converse is not true, even if we allow ourselves to replace the elements of Φ by scalar multiples,
because of the existence of non-crystallographic Coxeter systems (see Proposition B.1.6).
Pseudo-root systems are called “root systems” in [Hum90, Section 1.2] and [BB05, Section 4.4].
We avoid this terminology because it is not compatible with the established deﬁnition of root
systems in representation theory.
Remark B.1.3. If Φ is normalized or an actual root system then the group W preserves Φ, so the
action of W on V restricts to an action of W on Φ. In general, we can still make W act on Φ by
declaring that if w P W and α P Φ then w ¨ α is the unique element β of Φ such that wpαq P Rą0β.
This reduces to the previous action if Φ is normalized or an actual root system. Whenever we write
an element of W acting on an element of Φ, this is the action that we mean.
Deﬁnition B.1.4. Let Φ Ă V be a pseudo-root system. A subset ∆of Φ is called a system of
simple pseudo-roots if
(a) The set ∆is a vector space basis for the linear span of Φ.
(b) For every α P Φ, we can write α “ ř
βP∆nββ, where the coeﬃcients nβ are in R and they are
either all nonnegative or all nonpositive.
The corresponding system of positive pseudo-roots is then
Φ` “ Φ X
" ÿ
βP∆
nββ : nβ P Rě0 @β P ∆
*
.
We also write Φ´ “ ´Φ`.
Deﬁnition B.1.5. Let Φ Ă V be a pseudo-root system. We say that Φ is irreducible if there is no
partition Φ “ Φ1 \ Φ2, with Φ1 and Φ2 nonempty pseudo-root systems such that pα1, α2q “ 0 for
every α1 P Φ1 and every α2 P Φ2.
Proposition B.1.6. The following two statements hold:
41


## Page 42


(i) ([Hum90, Section 1.9] and [Hum90, Section 1.4].) Let Φ Ă V be a pseudo-root system and
∆Ă Φ be a system of simple pseudo-roots.
Let W “ WpΦq be the subgroup of GLpV q
generated by the reﬂections sα for α P Φ, and let S “ tsα : α P ∆u. Then pW, Sq is a Coxeter
system where W is ﬁnite, and the Coxeter graph of pW, Sq is connected if and only if Φ is
irreducible.
Moreover, W acts transitively on the set of systems of positive pseudo-roots if we use the
action of Remark B.1.3.
(ii) ([Hum90, Section 5.4].) Conversely, let pW, Sq be a Coxeter system with W ﬁnite, and let
ρ : W ÝÑ GLpV q be its canonical representation on V “ À
sPS Res (see the beginning of
Subsection 2.2). Then Φ “ tρpwqpesq : w P W, s P Su is a normalized pseudo-root system
and ∆“ tes : s P Su is a system of simple pseudo-roots in Φ.
Deﬁnition B.1.7. Let Φ Ă V be an irreducible pseudo-root system. We say that Φ is of type An,
respectively Bn, Dn, E6, E7, E8, F4, H3, H4, I2pmq with m ě 3, if the corresponding Coxeter
system is of that type.
Here we use the classiﬁcation of simple ﬁnite Coxeter systems proved
in [GB85, Chapter 5]. See Table 1 in [BB05, Appendix A].
Remark B.1.8. The Coxeter group of type I2pmq is the dihedral group of order 2m. Note that
types I2p3q and A2 are isomorphic, types I2p4q and B2 are isomorphic, and types I2p6q and G2 are
isomorphic. We did not include I2p2q in the list of irreducible types, because the corresponding
Coxeter system is not irreducible, as it is isomorphic to A1 ˆ A1.
We will use the following lemma when introducing the sign associated to a 2-structure in Propo-
sition B.2.7. Recall that, if r ě 1, then the lexicographic order on Rr is deﬁned by px1, . . . , xrq ă
py1, . . . , yrq if there exists 1 ď i ď r such that xi ă yi and that xj “ yj for 1 ď j ď i ´ 1. It is a
total order. Furthermore we say that a vector x is positive if x ą p0, 0, . . . , 0q.
Lemma B.1.9. Let Φ Ă V be a pseudo-root system.
Let v1, v2, . . . , vr be linearly independent
elements of V such that no element of Φ is orthogonal to every vi. Deﬁne Φ` to be the set of α P Φ
such that the element ppα, v1q, pα, v2q, . . . , pα, vrqq of Rr is positive with respect to the lexicographic
order on Rr. Then Φ` is a system of positive pseudo-roots.
Proof. We complete pv1, . . . , vrq to a basis pv1, . . . , vnq of V , where n is the dimension of V . If
v, w P V , we say that v ă w if ppv, v1q, . . . , pv, vnqq ă ppw, v1q, . . . , pw, vnqq in the lexicographic
order on Rn. This deﬁnes a total order on V in the sense of [Hum90, Section 1.3], and Φ` is the
corresponding positive system in Φ. By the theorem in [Hum90, Section 1.3], Φ` is a system of
positive pseudo-roots in the sense of Deﬁnition B.1.4.
Deﬁnition B.1.10. If θ “ pv1, . . . , vrq is a sequence of linearly independent elements of V such
that θK X Φ “ ∅, we denote the system of positive pseudo-roots of Lemma B.1.9 by Φ`
θ .
B.2
2-structures
We deﬁne 2-structures, generalizing a notion introduced by Herb for root systems; see for example
the beginning of [Her00, Section 4]. We also generalize some of the results of [Her01, Section 5] to
Coxeter systems with ﬁnite Coxeter groups.
We ﬁx a pseudo-root system Φ in V and a system of positive pseudo-roots Φ` Ă Φ. We denote
by pW, Sq the corresponding Coxeter system (see Proposition B.1.6).
42


## Page 43


Deﬁnition B.2.1. A 2-structure for Φ is a subset ϕ of Φ, that is, a pseudo-root system in V
satisfying the following properties:
(a) The subset ϕ is a disjoint union ϕ “ ϕ1 \ ϕ2 \ ¨ ¨ ¨ \ ϕr, where the ϕi are pairwise orthogonal
subsets of ϕ and each of them is an irreducible pseudo-root system in V of type A1, B2 or
I2p2nq, for n ě 3.
(b) Let ϕ` “ ϕ X Φ`. If w P W is such that wpϕ`q “ ϕ` then detpwq “ 1.
Remark B.2.2. Although condition (b) involves the set of positive pseudo-roots ϕ` in ϕ, it does
not actually depend on the choice of ϕ`, because the Coxeter group of ϕ acts transitively on sets
of positive pseudo-roots in ϕ.
Remark B.2.3. If ϕ Ď Φ is a 2-structure then there is no α P Φ that is orthogonal to every element
of ϕ. Indeed, if such an α existed then the associated reﬂection sα would ﬁx every element of ϕ,
and in particular send ϕ` to itself, which would contradict condition (b) of Deﬁnition B.2.1.
Let T pΦq Ď 2Φ be the set of all 2-structures for the pseudo-root system Φ. The following propo-
sition is proved in Subsection B.4, where we also show that each irreducible pseudo-root system
contains a 2-structure and give the type of this 2-structure. This introduces no circularity in the
arguments: the only results in this appendix that depend on Proposition B.2.4 are Lemmas B.2.11
and B.2.12, and these lemmas are not used in Subsections B.3 and B.4.
Proposition B.2.4. The group W acts transitively on the collection of 2-structures T pΦq.
Let ϕ P T pΦq. We write ϕ` “ ϕ X Φ` and ϕ´ “ ϕ X Φ´, and we deﬁne
Wpϕ, Φ`q “ tw P W : wpϕ`q Ă Φ`u,
W1pϕ, Φ`q “ tw P W : wpϕ`q Ă ϕ`u “ tw P W : wpϕ`q “ ϕ`u.
Note that W1pϕ, Φ`q is a subgroup of W, and that the subset Wpϕ, Φ`q of W is stable by right
translations by elements of W1pϕ, Φ`q.
Corollary B.2.5. Let ϕ P T pΦq. Then the map W ÝÑ T pΦq, w ÞÝÑ wpϕq induces a bijection
Wpϕ, Φ`q{W1pϕ, Φ`q
„
ÝÑ T pΦq.
Proof. We denote by f : W ÝÑ T pΦq the map deﬁned by fpwq “ wpϕq.
If u P W1pϕ, Φ`q, then upϕq “ ϕ, so fpwuq “ fpwq for every w P W. So the map f does induce
a map from Wpϕ, Φ`q{W1pϕ, Φ`q to T pΦq, that we denote by f.
We show that f is surjective. Let ϕ1 P T pΦq. By Proposition B.2.4, there exists w P W such
that wpϕq “ ϕ1. By the theorem in [Hum90, Section 1.3], the set w´1pΦ`qXϕ is a system of positive
pseudo-roots in ϕ, so, by Proposition B.1.6, there exists v P Wpϕq, where Wpϕq is the Coxeter
group of ϕ, such that vpϕ`q “ w´1pΦ`qXϕ. Then wvpϕ`q “ Φ` Xwpϕq Ă Φ`, so wv P Wpϕ, Φ`q,
and wvpϕq “ wpϕq “ ϕ1, that is, fpwvq “ ϕ1.
We show that f is injective. Let w, w1 P Wpϕ, Φ`q such that wpϕq “ w1pϕq. Then we have
w´1w1pϕq “ ϕ, and, again by the theorem in [Hum90, Section 1.3], the set w´1w1pϕ`q is a system
of positive pseudo-roots in ϕ, so there exists v P Wpϕq such that v´1w´1w1pϕ`q “ ϕ`. This means
43


## Page 44


Φ`
α
α1
Φ`
α
α1
Figure 3: The dihedral pseudo-root system I2p8q with the two choices of θ “
`
α, α1˘
.
that we have w1 “ wvu with u P W1pϕ, Φ`q. So we will be done if we show that v “ 1. Note
that wvpϕ`q “ wvupϕ`q “ w1pϕ`q Ă Φ`. Suppose that v ‰ 1; then there exists α P ϕ` such that
vpαq P ϕ´, and then wvpαq “ ´wp´vpαqq P Φ´ (because w P Wpϕ, Φ`q), contradicting the fact
that wvpϕ`q Ă Φ`. So v “ 1.
The following proposition, which follows immediately from Lemma 5.6 of [Her01] for root sys-
tems, can be proved via a direct calculation for the remaining irreducible types. We will not need
this result, so we do not go into details.
Proposition B.2.6. Let TpaqpΦq be the set of ϕ Ď Φ that satisfy condition (a) of Deﬁnition B.2.1.
Then T pΦq is exactly the set of elements of TpaqpΦq that are maximal with respect to inclusion.
Proposition B.2.7. Let ϕ Ď Φ be a 2-structure. Deﬁne an ordered subset θ of ϕ as follows. Select
a linear order of the irreducible components ϕ1, ϕ2, . . . , ϕr of ϕ. If ϕi is a pseudo-root system of
type A1, let θi be the singleton ϕi X ϕ`. If ϕi is a pseudo-root system of type B2 or I2p2kq for
k ě 3, pick two orthogonal elements α and α1 from ϕi X ϕ` such that ϕi X ϕ` “ ϕ`
i,pα,α1q, that is,
such that an element β of ϕi is in ϕ` if and only if either pβ, αq ą 0, or pβ, αq “ 0 and pβ, α1q ą 0.
Let θi be the sequence pα, α1q. Finally let θ be the concatenation of the sequences θ1, θ2, . . . , θr.
Let Φ`
θ be the system of positive pseudo-roots deﬁned by the sequence θ as in Lemma B.1.9, and
let wθ be the unique element of W such that wθ ¨ Φ` “ Φ`
θ . Then the sign detpwθq depends only
on ϕ and not on the choices made to form θ.
Note that there are several choices when producing the ordered set θ. First we have to select
an order ϕ1, ϕ2, . . . , ϕr. There are r! ways to do this. Second, if ϕi is of type B2 or of type I2p2kq,
there are two possible choices for the pseudo-roots α and α1; see Figure 3. These selections do not
inﬂuence the sign of wθ, although they do of course aﬀect the set Φ`
θ .
Proof of Proposition B.2.7. Let θ and θ1 be the results of two possible sequences of choices. For
an element w in W, recall that its length ℓpwq 5 is also given by the cardinality of the intersection
5By deﬁnition, this is the minimal number of factors in an expression of w as a product of reﬂections corresponding
to simple pseudo-roots.
44


## Page 45


w ¨ Φ` X Φ´; see [BB05, Proposition 4.4.4]. Note that Φ`
θ X Φ´
θ1 “ wθ ¨ Φ` X wθ1 ¨ Φ´ “ wθ1 ¨
pw´1
θ1 wθ ¨ Φ` X Φ´q which has cardinality ℓpw´1
θ1 wθq. Hence to prove that the signs agree, that is,
that detpwθq “ detpwθ1q, it suﬃces to show that the set Φ`
θ X Φ´
θ1 has an even number of elements.
We can reduce to the following two cases:
(a) there exists 1 ď i ď r such that θ and θ1 diﬀer only by the choice of the two pseudo-roots in
the factor ϕi;
(b) there exists 1 ď i ď r ´ 1 such that θi “ θ1
i`1, θi`1 “ θ1
i and θj “ θ1
j if j ‰ i, i ` 1.
We begin by treating case (a). We write θi “ pα, α1q and θ1
i “ pβ, β1q. Let γ P Φ`
θ X Φ´
θ1.
Then γ is orthogonal to ϕ1, . . . , ϕi´1, and it is not orthogonal to ϕi. Also, as the sets of positive
pseudo-roots in ϕi deﬁned by θi and θ1
i are equal by assumption, we cannot have γ P ϕi. Write
γ “ cα ` c1α1 ` λ, with λ P ϕK
1 X ¨ ¨ ¨ X ϕK
i . By the previous sentence, we have λ ‰ 0. The vector
ιpγq “ ´psαsα1qpγq “ cα ` c1α1 ´ λ is also in Φ. It is not equal to γ because λ ‰ 0, and it is in
Φ`
θ X Φ´
θ1 because γ and ιpγq have the same inner product with any element of the set tα, α1, β, β1u.
Note that we clearly have ιpιpγqq “ γ. We have constructed a ﬁxed-point free involution ι on the
set Φ`
θ X Φ´
θ1, which proves that this set has even cardinality.
We treat case (b). Suppose ﬁrst that ϕi and ϕi`1 are both of type A1, so we can write θi “ pαiq
and θi`1 “ pαi`1q. Let Φ1 be the pseudo-root system Φ X pRαi ` Rαi`1q. If Φ1 is of type I2pmq
with m ě 3, then m must be even because Φ1 contains two orthogonal pseudo-roots. But then
Φ1 contains a multiple β of αi ´ αi`1, and the reﬂection sβ sends ϕ` to ϕ` because it ﬁxes every
element of ϕj for j “ i, i`1 and exchanges αi and αi`1, contradicting the deﬁnition of a 2-structure.
Hence Φ1 is of type A1 ˆ A1, and then the fact that |Φ`
θ X Φ´
θ1| is even follows from Lemma B.3.2.
Suppose that ϕi is of type A1 and ϕi`1 is of type I2p2mq with m ě 2. Then we can write θi “ pαiq
and θi`1 “ pαi`1, α1
i`1q. Let Φ1, respectively Φ2, be the pseudo-root system Φ X pRαi ` Rαi`1q,
respectively Φ X pRαi ` Rα1
i`1q, and let θ2 be the sequence that we obtain from θ by switching
αi and αi`1. As ϕi`1 is of type I2p2mq, it (and hence Φ) contains a pseudo-root β proportional
to αi`1 ´ α1
i`1, and then sβpΦ1q “ Φ2, so Φ1 and Φ2 are of the same type. By Lemma B.3.2, the
cardinalities of the sets Φ`
θ X Φ´
θ2 and Φ`
θ2 X Φ´
θ1 have the same parity, and so |Φ`
θ X Φ´
θ1| is even.
The case where ϕi is of rank 2 and ϕi`1 of rank 1 follows from the previous case by switching the
roles of ϕi and ϕi`1.
Finally, suppose that both ϕi and ϕi`1 are of rank 2. Then we can write θi “ pαi, α1
iq and
θi`1 “ pαi`1, α1
i`1q. We move from θ to θ1 by the following sequence of operations:
(1) We switch α1
i and αi`1. By Lemma B.3.2 and Remark B.3.3, this changes the sign of wθ by
p´1qm1{2´1, where the pseudo-root system Φ1 “ Φ X pRα1
i ` Rαi`1q is of type I2pm1q.
(2) We switch α1
i and α1
i`1. By the same lemma and remark, this changes the sign by p´1qm2{2´1,
where the pseudo-root system Φ2 “ Φ X pRα1
i ` Rα1
i`1q is of type I2pm2q.
(3) We switch αi and αi`1. By the same lemma and remark, this changes the sign by p´1qm3{2´1,
where the pseudo-root system Φ3 “ Φ X pRαi ` Rαi`1q is of type I2pm3q.
(4) We switch αi and α1
i`1. By the same lemma and remark, this changes the sign by p´1qm4{2´1,
where the pseudo-root system Φ4 “ Φ X pRαi ` Rα1
i`1q is of type I2pm4q.
The reﬂections si “ sαi´α1
i and si`1 “ sαi`1´α1
i`1 are both in W because ϕi contains a multiple of
αi ´ α1
i and ϕi`1 contains a multiple of αi`1 ´ α1
i`1. Observe now that sipΦ1q “ Φ3, sipΦ2q “ Φ4,
45


## Page 46


si`1pΦ1q “ Φ2 and si`1pΦ3q “ Φ4. Thus the four pseudo-root systems Φ1, Φ2, Φ3 and Φ4 are
isomorphic and hence m1 “ m2 “ m3 “ m4. Hence performing operations (1) to (4) changes the
sign by pp´1qm1{2´1q4 “ 1, that is, detpwθq “ detpwθ1q.
Deﬁnition B.2.8. Let ϕ Ď Φ be a 2-structure, and let wθ be as in Proposition B.2.7. Then the
sign p´1qr`r1 detpwθq, where r is the number of irreducible factors of Φ of type A2n with n odd and
r1 is the number of irreducible factors of Φ of type I2p2n1 ` 1q with n1 ě 3 odd, is called the sign
of ϕ and denoted by ǫpϕ, Φ`q, or by ǫpϕq if the system of positive pseudo-roots Φ` is understood.
Remark B.2.9. For a root system, this coincides with the deﬁnition of the sign of ϕ from Herb’s
paper [Her83], and it diﬀers from the deﬁnition in Section 5 of Herb’s paper [Her01]; see Remark 5.1
of [Her01] and Corollary 3.1.3.
Lemma B.2.10. Let ϕ Ď Φ be a 2-structure, that is, ϕ P T pΦq.
(i) For every w P W, the identity ǫpwpϕq, wpΦ`qq “ ǫpϕ, Φ`q holds.
(ii) Let w P W be such that wpϕ`q Ď Φ`. Then the identity ǫpwpϕq, Φ`q “ detpwq ¨ ǫpϕ, Φ`q
holds.
Proof. Both identities follow easily from the deﬁnition of ǫpϕ, Φ`q. Indeed, let θ be a subset of ϕ
chosen as in Proposition B.2.7. For every w P W, wpϕq is a 2-structure for Φ and its subset wpθq
satisﬁes the same conditions for the system of positive pseudo-roots wpΦ`q, and also for the system
of positive pseudo-roots Φ` if wpϕ`q Ă Φ`. Also, we have Φ`
w¨θ “ w ¨ Φ`
θ . This immediately
yields (i) and (ii).
Lemma B.2.11. Let α0 P Φ be a simple pseudo-root, let s0 be the simple reﬂection deﬁned by α0,
let Φ0 “ αK
0 X Φ and Φ`
0 “ Φ0 X Φ`. Let T 2 be the set of ϕ P T pΦq such that s0pϕq “ ϕ; we
also consider the subsets T 2
1 “ tϕ P T 2 : ϕ X Φ0 P T pΦ0qu and T 2
2 “ T 2 ´ T 2
1 . Then the following
statements hold:
(0) Let ϕ be a 2-structure for Φ. Then s0pϕq “ ϕ, that is, the 2-structure ϕ is in T 2, if and only
if α0 P ϕ.
(1) The map T 2
1 ÝÑ T pΦ0q, ϕ ÞÝÑ ϕ X Φ0 is bijective.
(2) For every ϕ P T 2
1 , we have ǫpϕ, Φ`q “ ǫpϕ X Φ0, Φ`
0 q.
(3) There exists an involution ι of T 2
2 such that, for every ϕ P T 2
2 , we have ϕ X Φ0 “ ιpϕq X Φ0
and ǫpιpϕq, Φ`q “ ´ǫpϕ, Φ`q.
Proof. We prove (0). If α0 P ϕ, then s0 is in the Coxeter group of ϕ, so s0pϕq “ ϕ. Conversely,
we have sα0pΦ` ´ tα0uq Ă Φ` by [BB05, Lemma 4.4.3], so, if ϕ P T 2 and α0 R ϕ, then s0pϕ`q Ď
Φ` X ϕ “ ϕ`, contradicting condition (b) in the deﬁnition of a 2-structure. Note also that the
subset ϕ X Φ0 of Φ0 always satisﬁes condition (a) in the deﬁnition of a 2-structure, but it does not
always satisfy condition (b).
We prove (1). We may assume that Φ is irreducible, and we will freely use the explicit description
of 2-structures given in Subsection B.4. If 2-structures for Φ are all of type As
1 for some s, which
happens in types An, Dn, E6, E7, E8, H3, H4 and I2pmq for m odd, then ϕ X Φ0 P T pΦ0q for every
46


## Page 47


ϕ P T pΦq, that is, T 2
1 “ T 2, and we see in the explicit description of 2-structures that the map of
statement (1) is a bijection. It is easy to check that the same statement holds in type I2pmq for m
even.
We now suppose that Φ is of type Bn or F4. (Recall that from the point of view of Coxeter
systems types Bn and Cn are isomorphic.) For convenience, in this case, we take Φ to be the actual
root system, with possibly non-normalized roots; this does not aﬀect any of the deﬁnitions that we
made before. To study the map of (1), we may assume that α0 “ en or α0 “ e1 ´ e2. Suppose ﬁrst
that α0 “ e1´e2. Then Φ0 is reducible. Furthermore, it is of type A1 ˆBn´2 if Φ is of type Bn, and
of type A1 ˆ B2 if Φ is of type F4, where the A1 factor is t˘pe1 ` e2qu. In both cases, it is easy to
see that T 2
1 “ T 2 and that (1) holds. Suppose that α0 “ en. Then Φ0 is irreducible. Furthermore,
it is of type Bn´1 if Φ is of type Bn, and of type B3 if Φ is of type F4. If Φ is of type F4 or Bn
with n even then again it is easy to see that T 2
1 “ T 2 and that (1) holds.
Finally, suppose that Φ is of type Bn with n odd and that α0 “ en. If ϕ P T 2 then we have
ϕ P T 2
1 if and only if t˘enu is an irreducible component of ϕ. The map sending ϕ0 P T pΦ0q to
ϕ0 \ t˘enu is thus an inverse to the map of (1), so statement (1) holds.
We now prove (3). We have seen in the proof of (1) that T 2
2 “ ∅unless Φ is of type Bn with n
odd and α0 is the short simple root. Assume that we are in this case, which means that α0 “ en.
Let ϕ P T 2
2 . Then there exists 2 ď i ď n such that ϕ1 “ t˘en, ˘ei, ˘en ˘ eiu is an irreducible
component of ϕ. Write ϕ “ ϕ1 \ ϕ2 \ ¨ ¨ ¨ \ ϕr, where the ϕk are irreducible and ϕ2 “ t˘eju is the
unique rank 1 component of ϕ. Set ιpϕq “ t˘en, ˘ej, ˘en ˘ eju \ t˘eiu \ ϕ3 \ ¨ ¨ ¨ \ ϕr. This map
switches the roles of ei and ej. Then ιpϕq is also in T 2
2 , it is not equal to ϕ, we have ιpϕqXΦ0 “ ϕXΦ0
and ιpιpϕqq “ ϕ. To ﬁnish the proof of (3), it suﬃces to show that ǫpιpϕq, Φ`q “ ´ǫpϕ, Φ`q for
every ϕ P T 2
2 . But this follows immediately from the deﬁnition of ιpϕq and from Lemma B.3.2.
We ﬁnally prove (2).
Let ϕ P T 2
1 .
Choose an ordered subset θ “ tα1, . . . , αru of ϕ as in
Proposition B.2.7. We may assume that α0 P θ. If α0 is in an irreducible component of ϕ of
type A1, we may assume that α0 “ α1. If α0 is in an irreducible component of ϕ of rank 2, then,
as it is a simple pseudo-root, it cannot be the ﬁrst element of θ coming from this rank 2 factor of ϕ
(see Figure 3 for an illustration in the case of I2p8q, the general case is similar), so we may assume
that α0 “ αr.
Suppose ﬁrst that α0 is in an irreducible component of ϕ of rank 2 and that α0 “ αr. By
the description of 2-structures in Subsection B.4, this can only happen if Φ is of type Bn, F4 or
I2pmq with m even. The set tα1, . . . , αr´1u is an ordered subset of ϕ0 satisfying the conditions
of Proposition B.2.7, and Φ`
0,θ0 “ Φ`
θ X Φ0. So the statement of (2) will follow if we can show
that X “ pΦ`
θ ´ Φ`
0,θ0q X Φ´ has even cardinality.
Let s “ sαr.
We claim that spXq “ X
and that s has no ﬁxed points in X, which implies that X has even cardinality because s2 “ 1.
The fact that s has no ﬁxed point in X follows from the facts that the ﬁxed points of s are
the elements of αK
r , that Φ X αK
r “ Φ0 and that X X Φ0 “ ∅.
As αr R Φ´ and ´αr R Φ`
θ ,
we have X “ pΦ´ ´ t´αruq X pΦ`
θ ´ pΦ`
0,θ0 Y tαruqq.
As αr is a simple pseudo-root, we have
spΦ´ ´ t´αruq Ă Φ´ ´ t´αru by [BB05, Lemma 4.4.3]. So it suﬃces to prove that s preserves
Φ`
θ ´ pΦ`
0,θ0 Y tαruq. If β P Φ`
θ ´ Φ`
0,θ0 is such that β ‰ αr, then we cannot have pβ, αiq “ 0 for
every i P t1, . . . , r´1u; indeed, as Φ is of type Bn, F4 or I2pmq with m even, the family pα1, . . . , αrq
is an orthonormal basis of V , so the only element of Φ`
θ that is orthogonal to α1, . . . , αr´1 is αr.
So Φ`
θ ´ pΦ`
0,θ0 Y tαruq is the set pseudo-roots β P Φ such that ppβ, α1q, . . . , pβ, αr´1qq ą 0 (for the
lexicographic order on Rr´1) and that pβ, αrq ‰ 0. This set is stable by s, because, for every β P V ,
we have pspβq, αiq “ pβ, spαiqq “ pβ, αiq if 1 ď i ď r ´ 1 and pspβq, αrq “ pβ, spαrqq “ ´pβ, αrq.
47


## Page 48


Now we suppose that α0 is in an irreducible component of ϕ of rank 1 and that α0 “ α1. Then
θ0 “ tα2, . . . , αru is an ordered subset of ϕ0 satisfying the conditions of Proposition B.2.7, and
Φ`
0,θ0 “ Φ0 X Φ`
θ , so Φ`
θ ´ Φ`
0,θ0 “ tβ P Φ : pβ, α1q ą 0u. Statement (2) will follow if we can show
that
X “ pΦ`
θ ´ Φ`
0,θ0q X Φ´ “ tβ P Φ´ : pβ, α1q ą 0u
has even cardinality if Φ is not of type A2n or I2p2n1`1q with n1 odd, and odd cardinality otherwise.
As ϕ has an irreducible component of rank 1, we cannot be in type F4. We can check that X has
even cardinality by a computer calculation in the exceptional types E, G and H.
We now go through the remaining types one by one (in cases A, B and D, we use the description
of the roots from the tables at the end of [Bou68], and not the normalized pseudo-root system):
‚ Type I2pmq: If m is even, then ϕ is a rank 2 pseudo-root system; so m must be odd, and
then ϕ0 is empty and ǫpϕ0q “ 1. There are exactly m pseudo-roots β such that pβ, α1q ą 0,
and pm ´ 1q{2 of these are in Φ´. So ǫpϕq “ p´1qpm´1q{2p´1qpm´1q{2 “ 1, which is what we
wanted.
‚ Type An: We write α0 “ ei ´ ei`1, with 1 ď i ď n. Then
X “ tej ´ ek : 1 ď k ă j “ i or i ` 1 “ k ă j ď n ` 1u
has cardinality n ´ 1, that is, even if and only if n is odd.
‚ Type Bn: As ϕ has an irreducible component of rank 1, the integer n must be odd and α0 is
the short simple root, that is, α0 “ en. Then
X “ t´ei ` en : 1 ď i ď nu
has cardinality n ´ 1, which is even.
‚ Type Dn: If α0 “ ei ´ ei`1 with 1 ď i ď n ´ 1, then
X “tej ´ ek : 1 ď k ă j “ i or i ` 1 “ k ă j ď nu
Y t´pej ` ekq : i ` 1 “ j ă k ď n or i ‰ j ă k “ i ` 1u
has cardinality 2n ´ 4. If α0 “ en´1 ` en, then
X “ tej ´ ek : n “ j ą k ‰ n ´ 1 or j “ n ´ 1 ą ku
also has cardinality 2n ´ 4.
Lemma B.2.12. Let ϕ Ď Φ be a 2-structure. Then |Φ` ´ ϕ`| is an even integer. More precisely,
if Φ is irreducible, we have
|Φ` ´ ϕ`| “
$
’
&
’
%
2n mod 4
if Φ is of type A2n,
0 mod 4
if Φ is of type A2n`1, B, D, E, F4, G2, or H,
2rpm ´ 1q
if Φ is of type I2p2rmq with m odd.
Proof. This follows from the explicit description of 2-structures for the irreducible types in Subsec-
tion B.4.
48


## Page 49


B.3
Orthogonal sets of pseudo-roots and 2-structures
For Φ a root system (not just a pseudo-root system), let OpΦq be the set of all ﬁnite sequences
pα1, α2, . . . , αrq of elements of Φ which are pairwise orthogonal and such that their entries all have
the same length, that is, the following two conditions hold:
(a) pαi, αjq “ 0 for all 1 ď i ă j ď r;
(b) }α1} “ }α2} “ ¨ ¨ ¨ “ }αr}.
Lemma B.3.1. Suppose that Φ is a root system. Let θ “ pα1, . . . , αrq and θ1 “ pβ1, . . . , βsq be
elements of OpΦq, and suppose that θK X Φ “ pθ1qK X Φ “ ∅and that the elements of θ and θ1
have the same length. Then there exists w P W such that tα1, . . . , αru “ twpβ1q, . . . , wpβsqu. In
particular, r “ s holds.
Proof. Let Φ`
θ , respectively Φ`
θ1, be the system of positive roots deﬁned by θ, respectively θ1, as in
Deﬁnition B.1.10. As W acts transitively on the set of systems of positive roots, there exists w P W
such that wpΦ`
θ1q “ Φ`
θ . As wpΦ`
θ1q “ Φ`
wpβ1q,...,wpβsq, we may assume that Φ`
θ “ Φ`
θ1. We then wish
to prove that θ and θ1 are equal up to reordering their entries. We proceed by induction on the length
of θ. If θ is empty then Φ is also empty because of the condition ΦXθK “ ∅, so θ1 is empty and we are
done. Suppose that r ě 1. Let j0 be the smallest index j such that pα1, βjq ‰ 0. Since ΦXpθ1qK “ ∅,
this minimum exists. As βj0 P Φ`
θ1 “ Φ`
θ , we cannot have pα1, βj0q ă 0, so pα1, βj0q ą 0. As Φ
is a root system and not just a pseudo-root system, the corollary after [Bou68, Chapitre VI, § 1,
№3, Th´eor`eme 1] implies that the diﬀerence γ “ α1 ´ βj0 is an element of Φ Y t0u. Suppose that
γ P Φ`
θ1. As pγ, βjq “ 0 for 1 ď j ă j0, we must then have 0 ď pγ, βj0q “ pα1, βj0q ´ pβj0, βj0q.
The hypothesis states that }α1} “ }βj0} and hence we deduce that pα1, βj0q ě }βj0}2 “ }α1} ¨ }βj0}.
This inequality implies that α1 “ βj0, contradicting the fact that γ is nonzero.
Suppose that
γ P Φ´
θ . Then 0 ď pα1, ´γq “ pα1, βj0q ´ pα1, α1q, so pα1, βj0q ě }α1}2, and again this implies that
α1 “ βj0 and contradicts the assumption. Hence we conclude that γ “ 0, that is, α1 “ βj0. Let
Φ0 “ αK
1 X Φ “ βK
j0 X Φ, θ0 “ pα2, . . . , αrq and θ1
0 “ pβ1, . . . , x
βj0, . . . , βsq. Then Φ0 is a root system,
θ0 and θ1
0 are in OpΦ0q, θK
0 X Φ0 “ pθ1
0qK X Φ0 “ H, and Φ`
0,θ0 “ Φ`
θ X Φ0 “ Φ`
θ1 X Φ0 “ Φ`
0,θ1
0. We
can apply the induction hypothesis to conclude that tα2, . . . , αru “ tβ1, . . . , x
βj0, . . . , βsu, and this
immediately implies that tα1, . . . , αru “ tβ1, . . . , βsu.
Lemma B.3.2. Let Φ be a normalized pseudo-root system, let θ “ pα1, . . . , αrq be a sequence of
pairwise orthogonal elements of Φ such that θK X Φ “ ∅, and let θ1 be the sequence obtained from θ
by exchanging αi and αi`1. Consider the subroot system Φ1 “ Φ X pRαi ` Rαi`1q. Then Φ1 is of
type A1 ˆ A1 or I2pmq with m ě 4 even, and the parity of the cardinality of Φ`
θ X Φ´
θ1 is given by
|Φ`
θ X Φ´
θ1|
” 0 mod 2
if Φ1 “ A1 ˆ A1,
|Φ`
θ X Φ´
θ1|
” m{2 ´ 1 mod 2
if Φ1 “ I2pmq.
Proof. As Φ1 is a pseudo-root system of rank 2 (because it is contained in a 2-dimensional vector
space and contains the two linearly independent pseudo-roots αi and αi`1), it is of type A1 ˆ A1
or I2pmq with m ě 3.
Moreover, Φ1 contains two orthogonal pseudo-roots, so it cannot be of
type I2pmq with m odd.
49


## Page 50


Table 1: The number of orthogonal sets of roots or pseudo-roots of size k where the elements
all have the same length in the exceptional/sporadic reﬂection arrangements.
Note the double
occurrence of 10! in the E8 column. The equality of the columns in type F4 comes from the fact
that there is an automorphism of the underlying vector space that preserves angles, sends short
roots to long roots, and sends long roots to doubles of short roots (for instance, the automorphism
given by e1 ÞÝÑ e1 ` e2, e2 ÞÝÑ e1 ´ e2, e3 ÞÝÑ e3 ` e4 and e4 ÞÝÑ e3 ´ e4).
k
E6
E7
E8
F4
F4
H3
H4
short
long
1
72
126
240
24
24
30
120
2
1080
3780
15120
72
72
60
1800
3
4320
32760
302400
96
96
40
2400
4
2160
75600
1965600
48
48
1200
5
90720
3628800
6
60480
3628800
7
17280
2073600
8
518400
We now set C “ Φ`
θ X Φ´
θ1 and calculate the parity of |C|. Let γ P C. Then γ is orthogonal to
α1, . . . , αi´1, so we can write γ “ cαi `dαi`1`λ with λ P Spanpα1, . . . , αi`1qK and cαi`dαi`1 ‰ 0.
Set ιpγq “ ´sαisαi`1pγq. Then ιpγq P Φ and ιpγq “ cαi ` dαi`1 ´ λ, so ιpγq P C. Also, we clearly
have ιpιpγqq “ γ, and ιpγq is equal to γ if and only if λ “ 0, that is, if and only if γ P Φ1. We have
deﬁned an involution ι of C, and we conclude that |C| ” |C0| mod 2, where C0 “ Φ1 X C is the
set of ﬁxed points of ι in C. If Φ1 is of type A1 ˆ A1 then we easily see that C0 is empty, so we
are done. Suppose that Φ1 is of type I2pmq with m even. Let γ “ cαi ` dαi`1 P Φ1, with c, d P R.
Then γ P C if and only if c ą 0 and d ă 0. The set C0 contains exactly one quarter of the elements
of Φ1 ´ t˘αi, ˘αi`1u, that is, |C0| “ p2m ´ 4q{4 “ m{2 ´ 1.
Remark B.3.3. If we view the root system A1 ˆ A1 as the dihedral pseudo-root system I2p2q then
the conclusion of Lemma B.3.2 is that |Φ`
θ X Φ´
θ1| ” m{2 ´ 1 mod 2 if Φ1 “ I2pmq with m even and
m ě 2.
Lemma B.3.4. Suppose that Φ is an irreducible root system (not just a pseudo-root system) and
not of type G2. Let Φ` be a system of positive roots of Φ and let ϕ Ď Φ be a 2-structure. Deﬁne
a subset θ of ϕ as in Proposition B.2.7. Then there is a choice of the sequences θi for which θ is
an element of OpΦq. Moreover, if Φ is of type Bn or F4 we can choose θ to consist of short roots.
Similarly, if Φ is of type Cn or F4 we can choose θ to consist of long roots.
Proof. By Remark B.2.3 we have θK X Φ “ ∅. We use the notation of Proposition B.2.7. If all
the roots of Φ have the same length (which is the case for An, Dn, E6, E7 and E8), then there is
nothing to prove. Note also that if ϕi is an actual root system of type B2 (that is, with the correct
root lengths), then the two possible choices for θi are the set of short positive roots and the set of
long positive roots.
Suppose that Φ is of type Bn. If ϕ has no irreducible component of type A1, then we choose
the two short positive roots in each ϕi. Suppose that ϕ has a factor of type A1. We show that
50


## Page 51


Table 2: The 2-structures in types A, D and E where m “ tpn ` 1q{2u in type A and m “ tn{2u in
type D.
Type of root
Type of
system Φ
2-structures are isomorphic to
2-structure
An
t˘pe1 ´ e2q,
˘pe3 ´ e4q,
. . . ,
˘pe2m´1 ´ e2mqu
Am
1
Dn
t˘e1 ˘ e2,
˘e3 ˘ e4,
. . . ,
˘e2m´1 ˘ e2mu
A2m
1
E6
t˘e1 ˘ e2,
˘e3 ˘ e4u
A4
1
E7
t˘e1 ˘ e2,
˘e3 ˘ e4,
˘e5 ˘ e6,
˘pe7 ´ e8qu
A7
1
E8
t˘e1 ˘ e2,
˘e3 ˘ e4,
˘e5 ˘ e6,
˘e7 ˘ e8u
A8
1
this factor cannot contain long roots. Suppose on the contrary that this occurs. Without loss of
generality, we may assume that ϕ1 “ t˘pe1 ` e2qu. The rank 2 factors of ϕ cannot contain e1 ´ e2,
so they are all in eK
1 XeK
2 . All the rank 1 factors that do not contain e1 ´e2 must also be in eK
1 XeK
2 .
If e1 ´e2 were not in ϕ then the reﬂection se1´e2 would act as the identity on all the elements on ϕ,
which contradicts the deﬁnition of a 2-structure. Hence t˘pe1 ´ e2qu is another rank 1 factor of ϕ.
But then the reﬂection se1 preserves ϕ`, which is impossible. Hence all the A1 factors of ϕ contain
only short roots, and we choose the θi in the B2 factors to contain the two short positive roots.
The case of Cn is similar, with the roles of short and long roots uniformly exchanged.
Finally suppose that Φ “ F4. In this case we can similarly show that the 2-structure ϕ has
type B2
2, allowing us to pick either short or long roots in each factor.
B.4
2-structures in the irreducible types
In this subsection we prove Proposition B.2.4, that is, the fact that the group W acts transitively
on the collection of 2-structures T pΦq. It is enough to prove this result for irreducible pseudo-root
systems. We proceed by a case by case analysis.
Types An, Dn, E6, E7 and E8
Suppose that Φ is a root system of type An, Dn or Em with m P t6, 7, 8u. As all the roots of Φ have
the same length and as Φ contains no B2 root system, the 2-structures for Φ are exactly the maximal
sets ϕ “ t˘α1, . . . , ˘αru such that pα1, . . . , αrq P OpΦq. By Lemma B.3.1, for any pα1, . . . , αrq and
pβ1, . . . , βsq on OpΦq, there exists w P W such that tα1, . . . , αru “ twpβ1q, . . . , wpβsqu. Hence the
group W acts transitively on T pΦq. In particular, all the 2-structures for Φ are isomorphic, so we
can determine their type. See Table 2.
Types Bn and Cn
Suppose that Φ is a root system of type Bn. This will also give the type Cn case, since Bn and Cn
correspond to the same Coxeter system. We claim that W acts transitively on T pΦq. In particular,
all the 2-structures for Φ are isomorphic to
ϕ0 “
#
t˘e1, ˘e2, ˘e1 ˘ e2u \ ¨ ¨ ¨ \ t˘e2m´1, ˘e2m, ˘e2m´1 ˘ e2mu
if n “ 2m,
t˘e1, ˘e2, ˘e1 ˘ e2u \ ¨ ¨ ¨ \ t˘e2m´1, ˘e2m, ˘e2m´1 ˘ e2mu \ t˘e2m`1u if n “ 2m ` 1,
51


## Page 52


so they are of type Bm
2 if n “ 2m is even, and of type Bm
2 ˆ A1 if n “ 2m ` 1 is odd.
We prove the claim by induction on n. The case n “ 1 is clear. Suppose that n ě 2. Let
ϕ, ϕ1 P Φ. By Lemma B.3.4, we can choose sequences θ of ϕ and θ1 of ϕ1 as in Proposition B.2.7
such that θ, θ1 P OpΦq and that these subsets contain only short roots. By Lemma B.3.1, we may
assume that θ and θ1 coincide up to the order of their elements. Denote by ϕ “ ϕ1 \ ¨ ¨ ¨ \ ϕs and
ϕ1 “ ϕ1
1 \ ¨ ¨ ¨ \ ϕ1
t the decomposition into irreducible systems that gave rise to θ and θ1. We can
always change the order on the ϕi and the ϕ1
j.
Suppose that ϕ1 is of rank 1, so that ϕ1 “ t˘α1u. We may assume that α1 P ϕ1
1. If ϕ1
1 is of
rank 1 then ϕ1
1 “ ϕ1. As Φ X ϕK
1 is an irreducible root system of type Bn´1, the conclusion follows
by the induction hypothesis.
If ϕ1
1 is of rank 2 then ϕ1
1 is a B2 root system whose short positive roots are α1 and some α2,
and we may assume that α2 P ϕ2. In particular, β “ α1 ´ α2 P Φ. If ϕ2 “ t˘α2u then the
reﬂection sβ preserves ϕ`, which is not possible. So ϕ2 is of rank 2 (in particular, n ě 3), which
means that it is a B2 root system whose short roots are α2 and some α3. We may assume that
α3 P ϕ1
2. In particular, α2 ´ α3 P Φ, so γ “ sβpα2 ´ α3q “ α1 ´ α3 is also a root. The irreducible
components of sγpϕq are ϕ1
1, t˘α3u, ϕ3, . . . , ϕs. As Φ X pϕ1
1qK is a root system of type Bn´2, the
induction hypothesis implies that there is a w P W such that wpϕ1q “ sγpϕq, which ﬁnishes the
proof in this case.
Suppose that ϕ1 is of rank 2, and call its other short positive root α2. We may assume that
α1 P ϕ1
1. If ϕ1
1 is of rank 1 then ϕ1
1 “ t˘α1u, and we can repeat the reasoning of the previous
paragraph with the roles of ϕ and ϕ1 exchanged. If ϕ1
1 “ ϕ1 then the conclusion follows from the
induction hypothesis applied to the Bn´2 root system ϕK
1 XΦ. Finally, suppose that ϕ1
1 is of rank 2
and ϕ1
1 ‰ ϕ1. Let α3 be the other short positive root of ϕ1
1. As α2 and α3 are both short roots,
β “ α2 ´ α3 P Φ. Note that the irreducible components of sβpϕq are ϕ1
1, sβpϕ2q, . . . , sβpϕsq, so
again the induction hypothesis implies that there exists w P W such that sβpϕq “ wpϕ1q, and we
are done.
Type F4
Suppose that Φ is a root system of type F4. Then we can show that W acts transitively on T pΦq
exactly as in type Bn. In particular, any 2-structure is isomorphic to ϕ0 “ t˘e1, ˘e2, ˘e1 ˘ e2u \
t˘e3, ˘e4, ˘e3 ˘ e4u, so it is of type B2
2.
Dihedral types
Suppose that Φ is a pseudo-root system of type I2pmq with m ě 5 (this includes the type G2 root
system). It is straightforward to see that W acts transitively on T pΦq. If m is odd then all the
2-structures for Φ are isomorphic to ϕ0 “ t˘e1u, and in particular of type A1. If m is even then
all the 2-structures for Φ are of type I2p2rq, where 2r is the largest power of 2 dividing m.
Types H3 and H4
Suppose that Φ is of type H3 or H4.
We use the description of the pseudo-root systems H3
and H4 given in [GB85, Table 5.2] where they are called I3 and I4. In particular, we choose Φ
to be normalized. We claim that W acts transitively on T pΦq, and so every 2-structure for Φ is
52


## Page 53


isomorphic to
ϕ0 “
#
t˘e1, ˘e2, ˘e3u
if Φ “ H3,
t˘e1, ˘e2, ˘e3, ˘e4u
if Φ “ H4,
(B.1)
and in particular it is of type A3
1 if Φ “ H3 and of type A4
1 if Φ “ H4.
It is clear by the chosen description of Φ that all of the inner products of elements of Φ are
in Qr
?
5s, and in particular 1{
?
2 never appears. So there are no pseudo-roots in Φ with an angle
of π{4 between them, which implies that Φ does not contain any pseudo-root system of type I2pmq
with m a multiple of 4, and so 2-structures for Φ (if they exist) can only have irreducible components
of type A1.
We check easily that the set ϕ0 given in equation (B.1) is a 2-structure, so it remains to show
that all the maximal sets of pairwise orthogonal pseudo-roots are conjugate under W to ζ0, where
ζ0 “ te1, e2, e3u if Φ “ H3 and ζ0 “ te1, e2, e3, e4u if Φ “ H4. Any element of the stabilizer W0 of ζ0
in W must act on SpanpΦq by a permutation of the coordinates, and it must be an even permutation
to be in W. This implies that the cardinality of W0 is 3 for Φ “ H3 and 12 for Φ “ H4. Using a
computer, it is not hard to count all the maximal sets of pairwise orthogonal pseudo-roots in H3
and H4 (see Table 1). We ﬁnd that there are 40 such sets for H3 and 1200 such sets for H4. In
both cases, this number is equal to |W|{|W0|, so W does act transitively on the set of maximal sets
of pairwise orthogonal pseudo-roots, and hence also on T pΦq.
C
Relationship with locally symmetric spaces
In this appendix, aimed at specialists of Shimura varieties, we give more details about the con-
nection between some of the objects introduced in this article and the calculation of the weighted
cohomology of locally symmetric spaces.
This is a continuation of the discussion in the ﬁrst part of the introduction, and we return to the
notation of this discussion. We do not suppose yet that the group GpRq has a discrete series. In the
introduction, we only considered cohomology of XK with constant coeﬃcients, but now we need to
introduce a coeﬃcient system. Let F be an irreducible algebraic representation of G. Then, via the
GpQq-covering pGpRq ˆ GpA8qq{pK8 ˆ Kq Ñ XK and the action of GpQq on F, we get a locally
constant sheaf LF on XK, and we will write H˚pXK, Fq instead of H˚pX, LF q for every reasonable
cohomology theory H˚. 6 If T Ă B are a maximal torus and a Borel subgroup of GC respectively,
then the representation F has a highest weight λB in the Lie algebra of T that is dominant with
respect to B. 7 The space V of the article will typically be this Lie algebra with the inner product
coming from the Killing form of the Lie algebra of G in the usual way. The pseudo-root system Φ
that deﬁnes the hyperplane arrangement will be the root system of T in the Lie algebra of G, with
the positive system determined by B; sometimes T will be deﬁned over R, and Φ will be the real
root system of T.
The ﬁrst cohomology theory that we consider is weighted cohomology, from which the weighted
complex and the weighted sum get their names. Weighted cohomology was introduced by Goresky–
Harder–MacPherson in the paper [GHM94]. It depends on an auxiliary parameter called a “weight
6We need a diﬀerent construction of LF if XK is the set of complex points of a Shimura variety and H˚ is ´etale
(intersection) cohomology, but this is not the point of this appendix.
7The representation F might not stay irreducible when seen as a representation of GC, but we ignore this technical
complication.
53


## Page 54


proﬁle” and is the cohomology of a sheaf of truncated diﬀerential forms on the reductive Borel-Serre
compactiﬁcation of XK, where the truncation depends on the weight proﬁle. The Hecke algebra
acts on the weighted cohomology groups, and they are explicit enough to make the calculation of
the traces of Hecke operators possible; see the paper [GM03] of Goresky and MacPherson. Also,
there are two “middle” weight proﬁles for any group G and, if XK is a Shimura variety, then the
two middle weighted cohomology groups are both isomorphic to the intersection cohomology of the
Baily-Borel compactiﬁcation of XK. What we call the “weighted sum” in this article appears in the
calculation of the trace of a Hecke operator on the weighted cohomology groups, hence the name.
This calculation is carried out in [GM03] and summarized in Section 7 of [GKM97]. Very roughly,
the trace of a Hecke operator on a weighted cohomology group is a sum over conjugacy classes of
rational Levi subgroups M of G and certain conjugacy classes of γ P MpQq of the product of:
– a normalizing factor;
– an orbital integral on the conjugacy class of γ in MpA8q that depends on the Hecke operator
but not on the weight proﬁle or on the coeﬃcient system;
– a “term at inﬁnity” LMpγq that depends on the weight proﬁle and the coeﬃcient system but
not on the Hecke operator.
See formula (7.14.7) of [GKM97].
Goresky, Kottwitz and MacPherson then introduce a stable
virtual character Θ on GpRq (this notion is deﬁned on page 495 of [GKM97]) that depends on
the coeﬃcient system via the highest weight of F and on the weight proﬁle. We can recover the
function LM as the restriction of Θ to M up to chasing some denominators depending on M;
this last statement is Theorem 5.1 of [GKM97], and it works for any weight proﬁle. While the
expression for the function LM involves “relative” weighted sums ψH{C where we are in the situation
of Example 4.2.1 (see pages 504–505 of [GKM97]), the virtual character Θ only involves the simpler
weighted sums ψH, where we are in the situation of Subsection 4.3. In both cases, the space V
is the real Lie algebra of a maximal torus T of G, the pseudo-root system is the set of real roots
of T in G, and the element λ of V is, up to a shift depending on the weight proﬁle, of the form
wpλB ` ρBq ´ ρB, where B Ą T is a Borel subgroup (deﬁned over C), λB is the highest weight of F
corresponding to B, ρB is half the sum of the positive roots and w is an element of the Weyl group.
We now assume that the weight proﬁle is one of the middle proﬁles and that XK is a Shimura
variety. Then, as explained in the introduction, we know that weighted cohomology is isomorphic
to L2 cohomology, for which we have a spectral description known as Matsushima’s formula (even
though it was proved by Borel and Casselman in this generality). This implies in particular that
the virtual character Θ is equal to the stable discrete series character corresponding to the dual
of the representation F, hence that the weighted sum ψH is equal to what are known as stable
discrete series constants; see for example pages 493 and 498–500 of [GKM97] for a quick review
of these constants. The ﬁrst statement of the previous sentence is proved directly in Theorem 5.2
of [GKM97], and the second statement is proved directly in Theorem 3.1 of the same paper. The
stable discrete series constants can be expressed in terms of 2-structures by the work of Herb (see
for example [Her00, Theorem 4.2]), and this is the expression on the right-hand side of the identity
of Corollary 4.3.1.
We can go further and relate the traces of Hecke operators on L2 cohomology to the Arthur-
Selberg trace formula for a particular test function. This is done in Arthur’s paper [Art89]. The
resulting trace formula can then be stabilized. Although this is a very complicated process in the
54


## Page 55


general case, it is slightly less involved for our test function, by the work of Kottwitz (unpublished)
and Zhifeng Peng ([Pen19]). Thus we get character formulas relating the virtual character Θ and
stable discrete series characters on endoscopic groups of G. However, when we express everything
in terms of 2-structures, the distinction between G and its endoscopic groups disappears. Indeed,
endoscopic groups of G have root systems that are subsystems of the root system of G, and 2-
structures, being very small root systems, can be shared between G and its endoscopic groups.
(We are summarily ignoring many complications, due in particular to the appearance of transfer
factors in the character identities.)
We ﬁnally come to the case where XK is a Shimura variety deﬁned over some number ﬁeld E
and we are interested, not just in the action of the Hecke algebra on the intersection cohomology
IH˚pXK, Fq of its Baily-Borel compactiﬁcation XK, but also in the action of the absolute Galois
group of E. There is a calculation of the trace of a Hecke operator times a power of the Frobenius
morphism (at at unramiﬁed place p) that parallels the calculation of [GM03]: see [Mor08] for the
algebraic version of weighted cohomology, the papers [Mor10] and [Mor11] for the trace calculation
in the cases of unitary and symplectic groups (over Q), and [Zhu17] for the trace calculation in
the case of orthogonal groups. We obtain an expression for this trace that is reminiscent of for-
mula (7.14.7) of [GKM97], that we quickly described above, except that the orbital integral at p is
twisted and that the terms LMpγq are slightly diﬀerent. Nevertheless, by using techniques similar
to those of the proof of Theorem 5.1 of [GKM97], in particular the Weyl character formula and
Kostant’s theorem, we can still relate LMpγq to the relative weighted sum ψH{C in the situation
of Example 4.2.1. For symplectic groups over Q, this calculation is done in the proof of Proposi-
tion 3.3.1 of [Mor11]. The diﬀerence with the situation of [GKM97] is that L2 cohomology does
not have an action of the absolute Galois of E, so we do not have a nice spectral expression for
our trace, and in particular we do not know if there is a stable virtual character “interpolating”
the function LM as in Theorem 5.1 of [GKM97]. Fortunately, we are still able to relate our trace
expression directly to a sum of stable trace formulas for well-chosen test functions on endoscopic
groups of G, and this is where Theorem 4.2.2 comes into play: We must express the function LM
in terms of stable discrete series constants for endoscopic groups of G. Via Herb’s formula, this
reduces to giving a formula for LM involving 2-structures for the root systems of these endoscopic
groups, but, as we explained above, these 2-structures can also be seen as 2-structures for the root
system of G. Again, we are sweeping many technical complications under the rug, and the story is
by no means ﬁnished once we have Theorem 4.2.2.
Acknowledgements
We thank the anonymous referees for their helpful comments. The greatest part of this work was
written while the second author was a professor at Princeton University.
It was also partially
supported by the LABEX MILYON (ANR-10-LABX-0070) of Universit´e de Lyon, within the pro-
gram “Investissements d’Avenir” (ANR-11-IDEX-0007) operated by the French National Research
Agency (ANR). More precisely, the authors would like to thank the ´Ecole Normale Sup´erieure de
Lyon (´ENS de Lyon) for its hospitality and support to the second author during the academic year
2017–2018, and to the ﬁrst and third author during one week visits. The ﬁrst and third authors also
thank Princeton University for hosting four one-week visits during the academic year 2018–2019,
and the Institute for Advanced Study for hosting a research visit Summer 2019, and the second
author thanks the University of Kentucky for its hospitality during a one-week visit in the Fall of
55


## Page 56


2019. This work was also partially supported by grants from the Simons Foundation (#429370 to
Richard Ehrenborg and #422467 to Margaret Readdy).
Finally, we used SageMath and Maple for innumerable root system computations.
References
[Art89]
James Arthur. “The L2-Lefschetz numbers of Hecke operators”. Invent. Math. 97.2
(1989), pp. 257–290.
[BB05]
Anders Bj¨orner and Francesco Brenti. Combinatorics of Coxeter groups. Vol. 231.
Graduate Texts in Mathematics. Springer, New York, 2005, pp. xiv+363.
[Bj¨o+99]
Anders Bj¨orner, Michel Las Vergnas, Bernd Sturmfels, Neil White and G¨unter M.
Ziegler. Oriented matroids. Second. Vol. 46. Encyclopedia of Mathematics and its Ap-
plications. Cambridge University Press, Cambridge, 1999, pp. xii+548.
[BC83]
Armand Borel and William Casselman. “L2-cohomology of locally symmetric manifolds
of ﬁnite volume”. Duke Math. J. 50.3 (1983), pp. 625–647.
[Bou68]
Nicolas Bourbaki. ´El´ements de math´ematique. Fasc. XXXIV. Groupes et alg`ebres de
Lie. Chapitre IV: Groupes de Coxeter et syst`emes de Tits. Chapitre V: Groupes en-
gendr´es par des r´eﬂexions. Chapitre VI: syst`emes de racines. Actualit´es Scientiﬁques
et Industrielles, No. 1337. Hermann, Paris, 1968, 288 pp.
[Don08]
Xun Dong. “The bounded complex of a uniform aﬃne oriented matroid is a ball”. J.
Combin. Theory Ser. A 115.4 (2008), pp. 651–661.
[EMR19]
Richard Ehrenborg, Sophie Morel and Margaret Readdy. “Some combinatorial identi-
ties appearing in the calculation of the cohomology of Siegel modular varieties”. Algebr.
Comb. 2.5 (2019), pp. 863–878.
[EMR21a]
Richard Ehrenborg, Sophie Morel and Margaret Readdy. Pizza and 2-structures. https://arxiv.org/
2021.
[EMR21b]
Richard Ehrenborg, Sophie Morel and Margaret Readdy. Sharing pizza in n dimen-
sions. https://arxiv.org/abs/2102.06649. 2021.
[ER99]
Richard Ehrenborg and Margaret A. Readdy. “On ﬂag vectors, the Dowling lattice,
and braid arrangements”. Discrete Comput. Geom. 21.3 (1999), pp. 389–403.
[Ful93]
William Fulton. Introduction to toric varieties. Vol. 131. Annals of Mathematics Stud-
ies. The William H. Roever Lectures in Geometry. Princeton University Press, Prince-
ton, NJ, 1993, pp. xii+157.
[GHM94]
Mark Goresky, G¨unter Harder and Robert MacPherson. “Weighted cohomology”. In-
vent. Math. 116.1-3 (1994), pp. 139–213.
[GKM97]
Mark Goresky, Robert Kottwitz and Robert MacPherson. “Discrete series characters
and the Lefschetz formula for Hecke operators”. Duke Math. J. 89.3 (1997), pp. 477–
554.
[GM03]
Mark Goresky and Robert MacPherson. “The topological trace formula”. J. Reine
Angew. Math. 560 (2003), pp. 77–150.
56


## Page 57


[Gro78]
Helmut Groemer. “On the extension of additive functionals on classes of convex sets”.
Paciﬁc J. Math. 75.2 (1978), pp. 397–410.
[GB85]
Larry C. Grove and Clark T. Benson. Finite reﬂection groups. Second. Vol. 99. Grad-
uate Texts in Mathematics. Springer-Verlag, New York, 1985, pp. x+133.
[Her79]
Rebecca A. Herb. “Characters of averaged discrete series on semisimple real Lie groups”.
Paciﬁc J. Math. 80.1 (1979), pp. 169–177.
[Her83]
Rebecca A. Herb. “The Plancherel theorem for semisimple Lie groups without compact
Cartan subgroups”. In Noncommutative harmonic analysis and Lie groups (Marseille,
1982). Vol. 1020. Lecture Notes in Math. Springer, Berlin, 1983, pp. 73–79.
[Her00]
Rebecca A. Herb. “Two-structures and discrete series character formulas”. In The
mathematical legacy of Harish-Chandra (Baltimore, MD, 1998). Vol. 68. Proc. Sympos.
Pure Math. Amer. Math. Soc., Providence, RI, 2000, pp. 285–319.
[Her01]
Rebecca A. Herb. “Discrete series characters as lifts from two-structure groups”. Trans.
Amer. Math. Soc. 353.7 (2001), pp. 2557–2599.
[Hum90]
James E. Humphreys. Reﬂection groups and Coxeter groups. Vol. 29. Cambridge Stud-
ies in Advanced Mathematics. Cambridge University Press, Cambridge, 1990, pp. xii+204.
[JR79]
S. A. Joni and G.-C. Rota. “Coalgebras and bialgebras in combinatorics”. Stud. Appl.
Math. 61.2 (1979), pp. 93–139.
[KR97]
Daniel A. Klain and Gian-Carlo Rota. Introduction to geometric probability. Lezioni
Lincee. [Lincei Lectures]. Cambridge University Press, Cambridge, 1997, pp. xiv+178.
[Loo88]
Eduard Looijenga. “L2-cohomology of locally symmetric varieties”. Compositio Math.
67.1 (1988), pp. 3–20.
[LR91]
Eduard Looijenga and Michael Rapoport. “Weights in the local cohomology of a Baily-
Borel compactiﬁcation”. In Complex geometry and Lie theory (Sundance, UT, 1989).
Vol. 53. Proc. Sympos. Pure Math. Amer. Math. Soc., Providence, RI, 1991, pp. 223–
260.
[Mor08]
Sophie Morel. “Complexes pond´er´es sur les compactiﬁcations de Baily-Borel: le cas des
vari´et´es de Siegel”. J. Amer. Math. Soc. 21.1 (2008), pp. 23–61.
[Mor10]
Sophie Morel. On the cohomology of certain noncompact Shimura varieties. Vol. 173.
Annals of Mathematics Studies. With an appendix by Robert Kottwitz. Princeton
University Press, Princeton, NJ, 2010, pp. xii+217.
[Mor11]
Sophie Morel. “Cohomologie d’intersection des vari´et´es modulaires de Siegel, suite”.
Compos. Math. 147.6 (2011), pp. 1671–1740.
[Pen19]
Zhifeng Peng. “Multiplicity formula and stable trace formula”. Amer. J. Math. 141.4
(2019), pp. 1037–1085.
[Sap18]
Leslie Saper. L-modules and microsupport (to appear in Annals of Mathematics).
https://arxiv.org/abs/math/0112251. 2018.
[SS90]
Leslie Saper and Mark Stern. “L2-cohomology of arithmetic varieties”. Ann. of Math.
(2) 132.1 (1990), pp. 1–69.
[Sch94]
William R. Schmitt. “Incidence Hopf algebras”. J. Pure Appl. Algebra 96.3 (1994),
pp. 299–330.
57


## Page 58


[Zas75]
Thomas Zaslavsky. “Facing up to arrangements: face-count formulas for partitions of
space by hyperplanes”. Mem. Amer. Math. Soc. 1.issue 1, 154 (1975), pp. vii+102.
[Zhu17]
Yihang Zhu. The Stabilization of the Frobenius-Hecke Traces on the Intersection Coho-
mology of Orthogonal Shimura Varieties. Thesis (Ph.D.)–Harvard University. ProQuest
LLC, Ann Arbor, MI, 2017, p. 270.
58

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1912_00506v5_a_generalization_of_combinatorial_identities_for_stable_discrete_series_constant
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1912_00506V5_A_GENERALIZATION_OF_COMBINATORIAL_IDENTITIES_FOR_STABLE_DISCRETE_SERIES_CONSTANT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

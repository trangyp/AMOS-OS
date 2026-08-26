---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.07000v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1811.07000v2_A_sheaf-theoretic_SL_2_C__Floer_homology_for_knots

> Source: 1811.07000v2_A_sheaf-theoretic_SL_2_C__Floer_homology_for_knots.pdf

> Pages: 47

---


## Page 1


arXiv:1811.07000v2  [math.GT]  13 May 2019
A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
LAURENT CˆOT´E AND CIPRIAN MANOLESCU
Abstract. Using the theory of perverse sheaves of vanishing cycles, we deﬁne a homological in-
variant of knots in three-manifolds, similar to the three-manifold invariant constructed by Abouzaid
and the second author. We use spaces of SL(2, C) ﬂat connections with ﬁxed holonomy around the
meridian of the knot. Thus, our invariant is a sheaf-theoretic SL(2, C) analogue of the singular knot
instanton homology of Kronheimer and Mrowka. We prove that for two-bridge and torus knots,
the SL(2, C) invariant is determined by the l-degree of the b
A-polynomial. However, this is not true
in general, as can be shown by considering connected sums of knots.
1. Introduction
Floer’s instanton homology [Flo88] is an important gauge-theoretic invariant of homology 3-
spheres, deﬁned using SU(2) connections in the trivial bundle.
It was later extended to other
bundles over 3-manifolds; see [Flo90,Don02]. Moreover, Kronheimer and Mrowka [KM11b] devel-
oped a similar invariant for knots in three-manifolds, which they called singular instanton homology.
Their construction uses SU(2) connections on the three-manifold that are singular along the knot,
having traceless holonomy around the meridian. (The trace zero condition is needed to ensure
monotonicity, so that an index bound on the moduli spaces of Floer trajectories gives an energy
bound.) The singular instanton homology of knots can be used to derive lower bounds for the slice
genus of knots [KM13], and was notably used in the proof that Khovanov homology detects the
unknot [KM11a].
In [AM], motivated by Witten’s work on Khovanov homology [Wit12], Abouzaid and the second
author deﬁned a homological invariant of three-manifolds using SL(2, C) instead of SU(2) con-
nections. When working with complex gauge groups, deﬁning Floer homology in the usual way
is diﬃcult because of noncompactness issues. However, one also expects no trajectories between
diﬀerent components of the space of SL(2, C) connections, which should make things easier. In-
deed, the construction in [AM] uses only sheaf theory, and none of the analysis characteristic of
gauge theory. The resulting invariant, denoted HP∗(Y ), is called the sheaf-theoretic SL(2, C) Floer
cohomology of the three-manifold Y .
The purpose of this paper is to construct an invariant similar to HP∗for knots in three-manifolds.
In the spirit of Kronheimer and Mrowka’s deﬁnition of singular instanton homology, we use SL(2, C)
connections on the knot complement for which the trace of the holonomy around the meridian of
the knot is ﬁxed to be some value τ ∈(−2, 2). Note that, since we do not work with moduli spaces
of trajectories, we do not have to worry about monotonicity. Also, for simplicity, we will restrict
our attention to irreducible connections (unlike in the work of Kronheimer and Mrowka).
Here is a sketch of the construction. Consider a doubly-pointed knot K ⊂Y , that is, a knot
with two distinct points ﬁxed on it. We choose a Heegaard decomposition of Y of genus g ≥6, such
that the Heegaard surface Σ intersects K transversely in the two points. We consider the relative
character variety Xτ
irr(Σ), made of irreducible SL(2, C) connections on Σ with holonomy trace τ
around the two points. This is a complex symplectic manifold, which can be identiﬁed with a
space of parabolic Higgs bundles on the surface. The two handlebodies yield complex Lagrangians
LC was supported by a Stanford University Benchmark Graduate Fellowship.
CM was supported by NSF grant DMS-1708320.
1


## Page 2


2
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
L0, L1 ⊂Xτ
irr(Σ), which can be equipped with spin structures. The intersection L0 ∩L1 is an
oriented d-critical locus in the sense of Joyce [Joy15]. Applying the work of Bussi [Bus], we obtain
from here a perverse sheaf of vanishing cycles, P •
L0,L1, on L0 ∩L1. Observe that L0 ∩L1 is the
relative character variety Xτ
irr(Y ) associated to Y , deﬁned by asking the holonomy around the knot
meridian to have trace τ.
Theorem 1.1. Let Y be a closed, connected, oriented three-manifold, and K ⊂Y a doubly-pointed
knot. Then, the object P •
τ (K) := P •
L0,L1 is an invariant of Y and K, up to canonical isomorphism
in a category Perv′(Xτ
irr(Y )) of perverse sheaves on Xτ
irr(Y ).
As a consequence, its hypercohomology
HP∗
τ(K) := H∗(P •
τ (K))
is also an invariant of Y and K, well-deﬁned up to canonical isomorphism in the category of
Z-graded Abelian groups.
We refer to Section 3.4 for an exact deﬁnition of the category Perv′(Xτ
irr(Y )).
The proof of Theorem 1.1 goes along the same lines as the proof of the corresponding result for
closed three-manifolds in [AM]. It involves checking invariance under stabilization, and naturality.
In the process we have to establish certain properties of relative character varieties (e.g. simple
connectivity) that were not immediately available in the literature.
We will refer to HP∗
τ(K) as the τ-weighted sheaf-theoretic SL(2, C)-Floer cohomology of the knot
K ⊂Y . When computing HP∗
τ for various knots, we will write M(k) for an Abelian group M
supported in degree k.
By analogy with the signed count of ﬂat connections with ﬁxed meridian trace in the SU(2) case
(cf. [Lin92] and [Her97]), we make the following deﬁnition.
Deﬁnition 1.2. We let the (τ-weighted, sheaf-theoretic) SL(2, C) Casson-Lin invariant of K be
the Euler characteristic of HP∗
τ(K), denoted χτ(K) ∈Z.
Let us now assume that Y is an integral homology sphere. For a knot K ⊂Y , consider the
character variety of the complement Y −nbhd(K) and its image in the character variety of the
boundary torus, X(T 2) ∼= (C∗× C∗)/Z2.
The one-dimensional components of this image are
(roughly) the zero set of a polynomial in two variables, m and l, corresponding to the meridian and
the longitude of the knot. This is the A-polynomial of the knot, introduced in [CCG+94]. Boyer
and Zhang [BZ01] have a variant called the bA-polynomial, bA(m, l), which also keeps track of the
degrees of the maps between the one-dimensional components of X(Y −nbhd(K)) and X(T 2).
In simple cases, the relative character variety Xτ
irr(Y ) is a ﬁnite number of points, obtained by
intersecting X(Y −nbhd(K)) with the preimage of the hyperplane
({τ} × C∗)/Z2 ⊂(C∗× C∗)/Z2 ∼= X(T 2).
If so, we expect HP∗
τ(K) to be isomorphic to several copies of Z, all in degree zero, and the number
of copies to be given by the l-degree of the bA-polynomial. We prove that this is the case in the
following situation.
Theorem 1.3. Suppose that Y is an integral homology sphere and K ⊂Y is a knot such that
the character scheme X τ(Y −K) is reduced and one-dimensional. Then, for all but ﬁnitely many
τ ∈(−2, 2), we have that
(1.1)
HP∗
τ(K) = Zd
(0),
where d = degl bA(m, l).
In fact, in Section 5 we derive precise conditions on the values of τ for which we can guarantee
that (1.1) holds.


## Page 3


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
3
To be able to use Theorem 1.3, we need to identify classes of knots K that satisfy the hypotheses.
There are geometric conditions that ensure that the character scheme is one-dimensional.
For
example, it suﬃces for the knot K to be either
• small, i.e., such that Y −K does not contain a closed, orientable, essential surface; or
• slim, i.e., hyperbolic and such that every component of Xτ(Y −K) which contains an
irreducible representation also contains a discrete, faithful representation.
When one of these conditions is satisﬁed, one still needs to check by hand whether the character
scheme is reduced. This can be done in practice, for example, for two-bridge knots, torus knots,
and some pretzel knots.
Theorem 1.4. Suppose that K ⊂S3 is a two-bridge knot, a torus knot, or a (−2, 3, 2n+1) pretzel
knot where n ̸= 0, 1, 2 and 2n + 1 is not divisible by 3. Then, for all but ﬁnitely many τ ∈(−2, 2),
the equality (1.1) is satisﬁed.
For speciﬁc knots, we can study the character scheme in more detail and calculate the sheaf-
theoretic Floer cohomology HP∗
τ(K) even for non-generic τ. For example, when K = 31 is the
trefoil, we ﬁnd that
HP∗
τ(31) =
(
Z(0)
if τ ∈(−2, 2) \ {
√
3, −
√
3},
0
if τ ∈{
√
3, −
√
3}.
On the other hand, for the ﬁgure-eight knot K = 41, we have
HP∗
τ(41) = Z2
(0),
for all τ ∈(−2, 2).
In general, the invariant HP∗
τ(K) does not always have to be supported in degree zero. An
example of this is given by considering connected sums of knots in S3, which may have higher-
dimensional character varieties.
Theorem 1.5. For i = 1, 2, suppose that Ki ⊂S3 is a two-bridge knot, a torus knot, or a
(−2, 3, 2n + 1) pretzel knot where n ̸= 0, 1, 2 and 2n + 1 is not divisible by 3. Let K = K1#K2.
Then, for all but ﬁnitely many τ ∈(−2, 2), we have that HP∗
τ(K) is supported in degrees −1 and 0
and, in fact,
HP∗
τ(K) = Z(degl b
A(K1))·(degl b
A(K2))
(−1)
⊕Z(degl b
A(K1))+(degl b
A(K2))+(degl b
A(K1))·(degl b
A(K2))
(0)
.
We remark that in this paper we only considered the case τ ∈(−2, 2), so that the holonomy
around the knot meridian is an elliptic element of SL(2, C).
However, we expect that similar
invariants exist for any τ ∈C∗\ {−2, 2}, and that they have similar properties. The only diﬃculty
in carrying out the same constructions is that the topology of the spaces Xτ
irr(Σ) is less understood
for τ ̸∈(−2, 2). Speciﬁcally, one would need to extend the results in Appendix I by showing that
certain moduli spaces of stable K(D)-pairs (in the terminology of [BY96]) are connected and simply
connected.
We also expect that one can deﬁne framed versions of P •
τ (K) and HP∗
τ(K), similar to the framed
invariants P •
#(Y ) and HP∗
#(Y ) of closed three-manifolds from [AM]. These would take into account
the reducible connections in addition to the irreducibles. Such a construction would be in fact closer
to Kronheimer and Mrowka’s singular knot instanton homology.
We end by raising a few questions for further investigation.
Question 1.6. For an arbitrary knot K ⊂Y , is HP∗
τ(K) independent of τ (up to isomorphism),
for generic τ ∈(−2, 2)?
Question 1.7. Is the SL(2, C) Casson-Lin invariant additive, i.e., do we have χτ(K1#K2) =
χτ(K1) + χτ(K2) for any K1, K2 ⊂S3 and τ ∈(−2, 2)? (See Theorem 7.19 for a partial result in
this direction.)


## Page 4


4
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
Question 1.8. If a knot K ⊂S3 satisﬁes HP∗
τ(K) = 0 for all τ ∈(−2, 2), is K the unknot?
The paper is organized as follows. Section 2 contains some background about relative character
schemes and parabolic group cohomology. Section 3 contains the deﬁnition of the knot invariants
P •
τ (K) and HP∗
τ(K), and the proof of Theorem 1.1. In Section 4 we develop some general tools
for computing perverse sheaves of vanishing cycles. In Section 5 we apply these tools to relate
our knot invariants to the bA-polynomial; in particular, we prove Theorem 1.3. Section 6 contains
concrete calculations for various small and slim knots; it is here where we prove Theorem 1.4. In
Section 7 we study the invariants for connected sums of knots, and prove Theorem 1.5. Finally, in
the appendix (Section 8), we establish a few facts about the topology of relative character varieties,
which are used in Section 3.
Acknowledgements.
We would like to thank Hans Boden, Julian Chaidez, Brian Conrad,
Yasha Eliashberg, Tony Feng, Maxim Jeﬀs, Michael Kapovich, Nikolas Kuhn, Aaron Landesman,
Ben Lim, Ikshu Neithalath, Dat Nguyen, Jacob Rasmussen, and Semon Rezchikov for helpful
conversations during the preparation of this paper. We also thank the referee for comments on a
previous version.
2. Preparatory material
This preparatory section introduces some material from algebraic geometry that will be needed
throughout the paper. In particular, we introduce relative versions of representation and character
schemes. We also discuss parabolic group cohomology, which is a variant of ordinary group coho-
mology. All of these objects have previously appeared in the literature (see e.g. [Kap15]), although
they seem to have been mostly considered implicitly.
The material in this section is technical and the proofs will not be used in the remainder of the
paper. The reader may therefore wish to treat this section as a reference once she has acquainted
herself with the main deﬁnitions.
2.1. Representation varieties and their relative counterparts. Let Γ = ⟨g1, . . . , gk | r1, . . . , rl⟩
be a ﬁnitely-presented group. The SL(2, C)-representation variety of Γ is the set of group homo-
morphisms
R(Γ) = Hom(Γ, SL(2, C)).
If we view SL(2, C) as an algebraic subset of C4, then R(Γ) can naturally be viewed as an
algebraic subset of C4k. Indeed, the condition that each gi ∈Γ maps to a matrix of determinant
1 is described by a set of polynomial equations f1, . . . , fk. The relations r1, . . . , rl then impose
additional equations fk+1, . . . , fk+l.
We can also consider the representation scheme
(2.1)
R(Γ) = Spec (C[x1, . . . , x4k]/(f1, . . . , fk+l)) .
In the language of scheme theory, the representation variety R(Γ) ⊂R(Γ) can be viewed as the
reduced subscheme associated to R(Γ).
Representation varieties play an important role in the work of Abouzaid and the second au-
thor [AM]. In the present paper, we need to consider certain generalizations which we call relative
representation varieties. Relative representation varieties are just subvarieties of ordinary repre-
sentation varieties which parametrize representations Γ →SL(2, C) with ﬁxed trace on certain
conjugacy classes of Γ. In order to deﬁne these objects precisely, however, it is useful to take a
more abstract perspective.
We begin by considering the following enlargement of the category of groups.
Deﬁnition 2.1. Let Gp+ be the category whose objects consist of a ﬁnitely-presented group Γ
along with a set of distinct conjugacy classes c1, . . . , cn (where n ≥0 depends on the particular


## Page 5


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
5
object). If n = 0 the set of conjugacy classes is empty. An arrow (Γ; c1, . . . , cn) →(Γ′; c′
1, . . . , c′
m)
is simply a morphism of groups which sends S
i ci into S
j c′
j.
Observe that Gp+ contains the ordinary category of groups as a subcategory.
Let C-alg denote the category of commutative algebras over the complex numbers. Given an
object (Γ; c1, . . . , cn) ∈Gp+ and a parameter τ ∈C, we can consider the functor
Rτ(Γ; c1, . . . , cn) : C-alg →Sets
taking A 7→{ρ : Γ →SL(2, A) | Tr(ρ(h)) = τ for all h ∈S
i ci}.
To lighten the notation, we will usually write Rτ(Γ) in place of Rτ(Γ; c1, . . . , cn) unless we want
to keep track of the conjugacy classes. If n = 0, the choice of τ is irrelevant. In this case, we write
R(Γ) instead of Rτ(Γ). This notation will be clariﬁed by following proposition; cf. Remark 2.3.
Proposition 2.2. The functor Rτ(Γ) : C-alg →Sets is representable, i.e., there exists a C-algebra
Aτ(Γ) such that
Rτ(Γ) = HomC-alg(Aτ(Γ), –).
Proof. We ﬁrst consider the case n = 0. It is not hard to verify that R(Γ) is in fact represented
by the C-algebra C[x1, . . . , x4k]/(f1, . . . , fk+l) introduced in (2.1). Let us call this C-algebra A(Γ).
It follows from general facts of category theory that A(Γ) is the unique representative, up to
canonical isomorphism. In particular, it is independent of the presentation of Γ. We refer the
reader to [LM85, Prop. 1.2] for a detailed exposition of these arguments.
If n > 0, we choose a group element ci ∈ci for i = 1, . . . , n. The condition Tr(ρ(ci)) = τ now
imposes additional polynomial equations fk+l+1, . . . , fk+l+n. It can then be shown as in the n = 0
case that
Aτ(Γ) := A(Γ)/(fk+l+1, . . . , fk+l+n)
represents the functor Rτ(Γ). The representative Aτ(Γ) is again unique up to canonical isomor-
phism, and in particular independent of the choice of ci ∈ci.
□
Generalizing (2.1), we deﬁne
Rτ(Γ) := Spec Aτ(Γ).
We say that Rτ(Γ) is the relative representation scheme associated to the parameter τ ∈C and to
the object (Γ; c1, . . . , cn) ∈Gp+. In general Rτ(Γ) may be singular and non-reduced. The relative
representation variety Rτ(Γ) ⊂Rτ(Γ) is the reduced subscheme associated to Rτ(Γ).
Remark 2.3. If A is a C-algebra, then its image under the functor Rτ(Γ) is the set Rτ(Γ)(A). It
follows from Proposition 2.2 that this set coincides with the set of A-valued points of the scheme
Rτ(Γ). This explains why we use the same notation to refer to a functor and to a scheme.
Example 2.4. Suppose that Γ = ⟨a1, . . . , ag, b1, . . . , bg, c1, c2 | r1, . . . , rm⟩. Let c1 = Conj(c1) and
c2 = Conj(c2). Then A(Γ) is the C-algebra formed from the polynomial algebra
C[xa1
11, xa1
12, xa1
21, xa1
22, . . . , xc2
11, xc2
12, xc2
21, xc2
22]
by ﬁrst modding out by the relations {xα
11xα
22 −xα
12xα
21 −1 = 0} where α ranges over the generators
of Γ, and then modding out by the relations coming from r1, . . . , rm. To obtain Aτ(Γ), one simply
adds the relations xc1
11 + xc1
22 −τ = 0 and xc2
11 + xc2
22 −τ = 0. This example will be important in the
sequel.
The algebraic group SL2 acts by conjugation on Rτ(Γ). We deﬁne the relative character scheme
X τ(Γ) to be the GIT quotient of this action. The relative character variety Xτ(Γ) ⊂X τ(Γ) is
the reduced subscheme associated to X τ(Γ). We let Rτ
irr(Γ) ⊂Rτ(Γ) be the open subscheme
corresponding to irreducible representations, and we deﬁne Rτ
irr(Γ), X τ
irr(Γ) and Xτ
irr(Γ) similarly.
As in the case of ordinary representation and character schemes, it can be shown that a morphism
(Γ; c1, . . . , cn) →(Γ′; c′
1, . . . , c′
m) in Gp+ induces morphisms Rτ(Γ′) →Rτ(Γ) and X τ(Γ′) →


## Page 6


6
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
X τ(Γ).
This is explained in [LM85, p. 6] for ordinary character schemes, and the arguments
generalize to the relative case.
2.2. Fiber products. Suppose that G, H0, H1, J are objects of Gp+ whose underlying groups
are Γ, Π0, Π1 and Π0 ∗Γ Π1 respectively. Suppose moreover that the following pushout diagram of
groups is induced by arrows in Gp+:
(2.2)
Γ
Π1
Π0
Π0 ∗Γ Π1.
Lemma 2.5. There is a canonical isomorphism of schemes Rτ(Π0∗ΓΠ1) ∼
−→Rτ(Π0)×Rτ (Γ)Rτ(Π1).
Proof. We will show that both schemes are spectra of C-algebras which represent the same same
functor. Indeed, one has:
Rτ(Π0) ×Rτ (Γ) Rτ(Π1) = HomC-alg(Aτ(Π0) ⊗Aτ (Γ) Aτ(Π1), −)
= HomC-alg(Aτ(Π0), −) ×HomC-alg(Aτ (Γ),−) HomC-alg(A(Π1)τ, −)
= HomGp+(Π0, SL2(−)) ×HomGp+(Γ,SL2(−)) HomGp+(Π1, SL2(−))
= HomGp+(Π0 ∗Γ Π1, SL2(−))
= Rτ(Π0 ∗Γ Π1).
It now follows by Yoneda’s lemma that there is a unique isomorphism Rτ(Π0∗ΓΠ1) ∼
−→Rτ(Π0)×Rτ (Γ)
Rτ(Π1).
□
Proposition 2.6 (cf. Prop 2.10 in [Mar15]). Suppose that the group homomorphisms Γ →Π0 and
Γ →Π1 in (2.2) are surjective. Then there is a unique isomorphism of schemes
(2.3)
X τ(Π0 ∗Γ Π1) ∼
−→X τ(Π0) ×X τ (Γ) X τ(Π1).
Proof. The surjectivity of the morphisms Γ →Πi implies that Rτ(Πi) →Rτ(Γ) is a closed embed-
ding of aﬃne schemes. Hence there is a surjective morphism Aτ(Γ) →Aτ(Πi). We let Ii ⊂Aτ(Γ)
be the kernel of this morphism.
According to Lemma 2.5 we have a canonical isomorphism
Aτ(Π0 ∗Γ Π1) ∼
−→Aτ(Π0) ⊗Aτ (Γ) Aτ(Π1) = Aτ(Γ)/I0 ⊗Aτ (Γ) Aτ(Γ)/I1.
We now take invariants under the action of SL2 by conjugation. By standard algebraic manipula-
tions, we have
 Aτ(Γ)/I0 ⊗Aτ (Γ) Aτ(Γ)/I1
SL2 = (Aτ(Γ)/(I0 + I1))SL2 = (Aτ(Γ))SL2/(I0 + I1)SL2.
For the last equality, we used the fact that SL2 is linearly reductive, which implies that the functor
of invariants M →MSL2 on SL2-modules is exact; see for example [Muk03, Proposition 4.37].
Next, we will need the following fact.
Fact 2.7. Let A be a C-algebra with an action of a linearly reductive group G and suppose that
I, J are ideals of A. Then (I + J)G = IG + JG.
Proof. Consider the short exact sequence
0 −→I ∩J −→I ⊕J −→I + J −→0.
Using again the exactness of the functor of invariants, we get a short exact sequence
0 −→(I ∩J)G −→(I ⊕J)G −→(I + J)G −→0.
On the other hand, we clearly have (I ∩J)G = IG ∩JG and (I ⊕J)G = IG ⊕JG, and the cokernel
of the map between them can be identiﬁed with IG + JG.
□


## Page 7


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
7
Applying this fact for G = SL2, we can now write:
(Aτ(Γ))SL2/(I0 + I1)SL2 = (Aτ(Γ))SL2/(ISL2
0
+ ISL2
1
)
= (Aτ(Γ))SL2/ISL2
0
⊗(Aτ (Γ))SL2 (Aτ(Γ))SL2/ISL2
1
= (Aτ(Γ)/I0)SL2 ⊗(Aτ (Γ))SL2 (Aτ(Γ)/I1)SL2.
It follows that
 Aτ(Γ)/I0 ⊗Aτ (Γ) Aτ(G)/I1
SL2 = (Aτ(Γ)/I0)SL2⊗(Aτ (Γ))SL2 (Aτ(Γ)/I1)SL2, which
is equivalent to (2.3).
□
Proposition 2.8. Under the hypotheses of Proposition 2.6, there is a unique isomorphism of
schemes
(2.4)
X τ
irr(Π0 ∗Γ Π1) ∼
−→X τ
irr(Π0) ×X τ
irr(Γ) X τ
irr(Π1).
Proof. It follows from general properties of the ﬁber product of schemes that there is an open embed-
ding X τ
irr(Π0)×X τ
irr(Γ)X τ
irr(Π1) →X τ(Π0)×X τ (Γ)X τ(Π1) ≃X τ
irr(Π0∗ΓΠ1). Since X τ
irr(Π0∗ΓΠ1)
is also an open subscheme of X τ
irr(Π0 ∗Γ Π1), it suﬃces to show that it has the same closed points
as X τ
irr(Π0) ×X τ
irr(Γ) X τ
irr(Π1). This can readily be checked by observing that, since Γ →Πi is
surjective, a representation ρi : Πi →SL(2, C) is irreducible if and only if it pulls back to an
irreducible representation of Γ →SL(2, C).
□
2.3. Parabolic group cohomology. We make a brief digression from our discussion of relative
representation and character schemes. As above, let Γ be a ﬁnitely-presented group. Let G be
a complex-algebraic group and let g be its Lie algebra. In the sequel, we only need to consider
G = SL(2, C) and g = sl(2, C), but there is no reason to restrict the following discussion to this
particular case.
Let us brieﬂy recall the co-cycle construction of the group cohomology of Γ with coeﬃcients in
the representation Ad ◦ρ : Γ →Aut(g). Here Ad : G →Aut(g) is the adjoint representation, given
by Ad(g) : ξ 7→gξg−1.
Consider the abelian groups
Cn(Γ; Ad ρ) := {functions : Γ →g},
where the group structure is given by addition of functions. One can deﬁne chain maps
dn+1 : Cn(Γ, Ad ρ) →Cn+1(Γ, Ad ρ)
by a standard formula; see [Bro94, p. 59]. In the case n = 1 which is the only one which we will
use, we have that
d2(φ)(g1, g2) = Ad ρ(g1)φ(g2) −φ(g1g2) + φ(g1),
for g1, g2 ∈Γ.
The subgroup of elements Zn(Γ; Ad ρ) = ker dn+1 are said to be n-cocycles, while the subgroup
of elements Bn(Γ; Ad ρ) = im dn are n-coboundaries. The group
Hn(Γ; Ad ρ) = Zn(Γ; Ad ρ)/Bn(Γ; Ad ρ)
is the n-th cohomology group of Γ with coeﬃcients in the representation Ad ρ : Γ →g.
We now consider the data of an object (Γ; c1, . . . , cn) of Gp+.
We let
Z1
par((Γ; c1, . . . , cn); Ad ρ) ⊂Z1(Γ; Ad ρ)
to be the set of 1-cocycles whose restriction to any element of S
i ci is a boundary. Said diﬀerently,
an element φ ∈Z1(Γ; Ad ρ) is contained in the subset Z1
par((Γ; c1, . . . , cn); Ad ρ) if, for all g ∈S
i ci,
there exists µ ∈g such that φ(g) = µ −Adρ(g)µ. The elements of Z1
par((Γ; c1, . . . , cn); Ad ρ) are
said to be parabolic 1-cocycles.


## Page 8


8
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
The quotient
H1
par((Γ; c1, . . . , cn); Ad ρ) := Z1
par((Γ; c1, . . . , cn); Ad ρ)/B1(Γ; Ad ρ)
is called the ﬁrst parabolic cohomology group of Γ with coeﬃcients in Ad ρ : Γ →g. If the set of
conjugacy classes is empty, this recovers the ordinary notion of group cohomology. There is also a
notion of parabolic group cohomology in higher degrees. Since we will not use it in this paper, we
refer the interested reader to [Hid93, p. 347].
For future reference, note that an arrow φ : (Γ; c1, . . . , cn) →(Γ′; c′
1, . . . , c′
m) induces a map of
abelian groups H1
par((Γ′; c′
1, . . . , c′
n); Ad ρ) →H1
par((Γ; c1, . . . , cn); Ad ρ ◦φ).
Remark 2.9. To lighten the notation, we will often write H1
par(Γ; Ad ρ) and Z1
par(Γ; Ad ρ) when the
conjugacy classes are understood from the context.
2.4. Tangent spaces. The relevance of parabolic group cohomology to our discussion of relative
representation and character schemes is evidenced by the following proposition.
Proposition 2.10. Let (Γ; c1, . . . , cn) ∈Gp+ and suppose that ρ ∈Rτ(Γ) for some τ ̸= ±2. We
then have:
(1) TρRτ(Γ) ≃Z1
par(Γ; Ad ρ).
(2) T[ρ]X τ
irr(Γ) ≃H1
par(Γ; Ad ρ).
In order to prove the ﬁrst statement, it is convenient to introduce the set TρRτ(Γ). This is
deﬁned as the set of all maps ρ : Γ →SL(2, C[ǫ]/(ǫ2)) satisfying the conditions:
(i) Tr(ρ(h)) = τ for all h ∈S
i ci
(ii) The composition Γ →SL(2, C[ǫ]/(ǫ2)) →SL(2, C) agrees with ρ, where SL(2, C[ǫ])/(ǫ2) →
SL(2, C) is the map induced by the C-algebra morphism C[ǫ]/(ǫ2) →C mapping ǫ →0.
The set TρRτ(Γ) can be canonically identiﬁed with the tangent space TρRτ(Γ); see [Sik12, p. 14].
This identiﬁcation is a general consequence of the fact that Rτ(Γ) represents a functor C-alg →
Sets, and turns out to be convenient for the purpose of proving Proposition 2.10.
Proof of Proposition 2.10 (1). By the previous discussion, it is enough to show that there is a
bijection Z1
par(Γ; Ad(ρ)) →TρRτ(Γ). As in [Sik12], consider the map
Z1
par(Γ; Ad ρ) →TρRτ(Γ)
σ →(γ ∈Γ 7→(I + σ(γ)ǫ)ρ(γ)).
Let us ﬁrst check that this map is well deﬁned, i.e. that the image satisﬁes conditions (i) and
(ii) above. Condition (ii) is clearly satisﬁed. To check condition (i), suppose that h ∈S
i ci. Then
Tr((I + σ(h)ǫ)ρ(h)) = Tr(ρ(h)) + ǫ Tr(σ(h)ρ(h)) = τ + ǫ Tr(σ(h)ρ(h)). But since σ ∈Z1
par(Γ; Ad ρ),
it follows that σ(h) = β −ρ(h)βρ(h)−1 for some β ∈g depending on h. Hence Tr(σ(h)ρ(h)) = 0 as
desired.
Injectivity follows from the analogous statement on [Sik12, page 15]. To show surjectivity, we
note that [Sik12, page 15] shows that every element of TρRτ(Γ) can be written in the form (γ 7→
(I + σ(γ)ǫ)ρ(γ)) for some σ ∈Z1(Γ; Ad(ρ)). Hence it suﬃces to check that σ ∈Z1
par(Γ; Ad(ρ)) ⊂
Z1(Γ; Ad(ρ)).
In other words, given h ∈Γ with Tr(ρ(h)) = τ ̸= ±2, we must check that Tr((I +σ(h)ǫ)(ρ(h))) =
τ ⇔Tr(σ(h)ρ(h)) = 0 ⇔σ(h) = β −ρ(h)βρ−1(h), for some β ∈g. This follows from the following
linear algebra fact.
□
Fact 2.11. Let B ∈SL(2, C) and A ∈sl(2, C) such that Tr(B) ̸= ±2 and Tr(AB) = 0. Then there
exists C ∈sl(2, C) such that A = C −BCB−1.


## Page 9


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
9
Proof. Fixing B, evidently we have {C −BCB−1 | C ∈sl(2, C)} ⊂{A ∈sl(2, C) | Tr(AB) = 0}.
By direct computation, one can check that both the left hand side and the right hand side are two
dimensional, which gives the desired equality.
□
The proof of Proposition 2.10 (2) is essentially identical to that of [Sik12, Theorem 53], except
that one considers the relative representation and character schemes Rτ
irr(Γ) and X τ
irr(Γ) in place
of the ordinary representation and character schemes (which are denoted by Hom(Γ, G) and XG(Γ)
in Sikora’s notation).
The key tool from algebraic geometry is the Luna Slice Theorem; see for example [Dr´e04]. If ρ is
an irreducible representation, its orbit in Rτ(Γ) can be shown to be closed. Since ρ is irreducible,
its stabilizer Sρ = {±I} is precisely the center of G = SL(2, C). The Luna Slice Theorem then
implies that there exists a closed subscheme S ⊂Rτ(Γ), usually called an
´etale slice, with the
following properties. We have [ρ] ∈S and there is a natural map (G/Sρ) × S →X τ(Γ) sending
(g, s) 7→gs which is ´etale. Similarly, the projection map S →X τ(Γ) is ´etale.
One useful consequence of the existence of ´etale slices which will be used later on is the fact that
Rτ
irr(Γ) is a Gad-bundle over Xτ
irr(Γ); see [Sch08, Ex. 2.1.1.4.(iii)]. Here Gad := G/Z(G) = G/Sρ.
Proof of Proposition 2.10 (2). The inclusion X τ
irr(Γ) →Rτ
irr(Γ) induces a surjective morphism of
tangent spaces
TρRτ
irr(Γ) →T[ρ]X τ
irr(Γ).
We saw in (1) that TρRτ
irr(Γ) = Z(Γ; Ad ρ), so it only remains to show that the kernel is B1(Γ; Ad ρ).
This can be done as in the proof of [Sik12, Theorem 53] by appealing to the existence of an ´etale
slice as discussed above, along with the fact that Sρ = Z(G) necessarily acts trivially on this
slice.
□
Deﬁnition 2.12. A representation ρ ∈Rτ(Γ) is said to be regular if the scheme Rτ(Γ) is regular
at [ρ]. It is said to be reduced if Rτ(Γ) is reduced at [ρ].
We end this section by recording the following proposition, which is an analog of Proposition
2.3 and Lemma 2.4 in [AM]. It can be proved by modifying the arguments provided in [AM] and
[Sik12, Corollary 55] but we omit the details.
Proposition 2.13. An irreducible representation ρ ∈Rτ(Γ) is regular (reduced) if and only if the
scheme X τ(Γ) is regular (reduced) at [ρ].
3. Definition of the knot invariant
We now pass to the construction of our knot invariant. The general scheme is similar to that of
[AM, Sec. 7.1]. Starting from a Heegaard splitting Y = U0 ∪ΣU1, we get complex Lagrangians L0 =
Xτ
irr(U0) and L1 = Xτ
irr(U1) in the relative character variety Xτ
irr(Σ). Appealing to a construction
of Bussi in [Bus], we deﬁne a perverse sheaf P •
L0,L1 on the intersection L0 ∩L1 = Xτ
irr(Y ). We
then show that P •
L0,L1 is suitably independent of the choice of Heegaard splitting and thus deﬁnes
a topological invariant. This will prove Theorem 1.1.
3.1. Preliminary deﬁnitions. Although the basic strategy for deﬁning our invariant mirrors that
of [AM, Sec. 7.1], some technicalities occur in our setting which were not present in the original
construction. These are mainly due to working with manifolds with boundary. In particular, we
eventually wish to appeal to work of Juh´asz, D. Thurston and Zemke in order to prove the naturality
of our invariant. This leads us to use the language of sutured manifolds and to introduce certain
auxiliary categories.
Deﬁnition 3.1. A sutured manifold (M, γ) is the data of a compact, oriented 3-manifold M with
nonempty boundary, along with a disjoint union of oriented simple closed curves γ = S
i γi ⊂∂M.


## Page 10


10
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
One requires that γ separates ∂M into two components R+(γ) and R−(γ), where R+(γ)∪R−(γ) =
∂M and ∂R+(γ) = γ, ∂R−(γ) = −γ.
The set of sutured manifolds naturally forms a category whose arrows are diﬀeomorphisms
(M, γ) →(M′, γ′) sending R+(γ) to R+(γ′) and R−(γ) to R−(γ′).
Let us also introduce the category Knot∗∗of doubly-pointed knots. An object (Y, K, p, q) of
Knot∗∗consists of an oriented 3-manifold Y , an oriented knot K ⊂Y , and an ordered pair of
basepoints p, q ∈K ⊂Y . A morphism (Y, K, p, q) →(Y ′, K′, p′, q′) is an orientation-preserving
diﬀeomorphism Y →Y ′ which sends K, p, q to K′, p′, q′ respectively.
There is a functor from Knot∗∗to the category of sutured manifolds which will be very important
to us and which we refer to as the (spherical) blowup. This was also considered by Juh´asz, Thurston
and Zemke in [JTZ18, Deﬁnition 2.5]. Given a doubly-pointed knot (Y, K, p, q), for every x ∈K,
let NxK = TxY/TxK be the ﬁber of the normal bundle of K over x, and let cx := UNxK =
(NxK \ {0})/R+ be the ﬁber of the unit normal bundle to K over x.
The blowup (EK, γ) of
(Y, K, p, q) is obtained by replacing x with cx for all x ∈K and letting γ = cp ∪cq. Note that the
interior of EK is diﬀeomorphic to the knot exterior of K ⊂Y .
The orientations on Y and on K induce an orientation on NK and hence on ∂EK. This orien-
tation is compatible with the boundary orientation of ∂EK inherited from the orientation of EK
(which is itself inherited from the orientation of Y ). We orient cp coherently with respect to the
orientation of NpK and cq incoherently with respect to the orientation of NqK. This uniquely
determines R+(γ) and R−(γ).
A detailed construction of the blowup functor is provided in [AK10]. It is shown in particular
that a morphism (Y, K, p, q) →(Y ′, K′, p′, q′) induces a morphism (EK, γ) →(EK′, γ′). The image
of Knot∗∗under the blowup functor forms a subcategory of the category of sutured manifolds. We
call this subcategory SutKnot. In the sequel, we will view the blowup as a functor Bl : Knot∗∗→
SutKnot taking (Y, K, p, q) 7→(EK, γ).
Given a surface Σ with nonempty boundary, an attaching set is the data of a disjoint union
α = S
i αi of pairwise disjoint simple closed curves such that each component of Σ −S
i αi contains
a component of ∂Σ. An attaching set is said to be maximal if it is not contained in a strictly larger
attaching set, i.e. if the collection of curves is maximal.
Deﬁnition 3.2. Given (EK, γ) ∈SutKnot, a Heegaard splitting H consists in a decomposition
EK = U0 ∪U1 into handlebodies, where U0 ∩U1 = Σ is a surface with boundary ∂Σ = cp ∪cq.
We require moreover that there exist maximal attaching sets α, β ⊂Σ, where the αi and βi bound
disks in U0 and U1 respectively.
It is shown in [JTZ18, Lem. 2.15] that any sutured manifold, so in particular every object of
SutKnot, admits a Heegaard splitting.
3.2. Geometric setup. Let us now ﬁx an object (Y, K, p, q) of Knot∗∗and let (EK, γ) be its
blowup. We ﬁx a Heegaard splitting H = (Σ, U0, U1) for (EK, γ) and choose a basepoint x0 ∈cp.
Such data determines the following commutative diagram in the category Gp+:
(3.1)
(π1(Σ, x0); Conj([cp]), Conj([cq]))
(π1(U1, x0); Conj([cp]))
(π1(U0, x0); Conj([cp]))
(π1(EK, x0); Conj([cp])).
It follows from the existence of two maximal attaching sets bounding disks that the inclusions
ιi : Σ →Ui induce surjective maps (ιi)∗: π1(Σ, x0) →π1(Ui, x0). By van Kampen’s theorem, the
underlying diagram of groups is isomorphic to a pushout diagram of the form (2.2).
It now follows by Proposition 2.8 that there is a unique isomorphism
(3.2)
X τ
irr(π1(EK, x0)) ≃X τ
irr(π1(U0, x0)) ×X τ
irr(π1(Σ,x0)) X τ
irr(π1(U1, x0)).


## Page 11


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
11
In other words, the scheme-theoretic intersection of X τ
irr(π1(U0, x0)) and X τ
irr(π1(U1, x0)) can be
identiﬁed with X τ
irr(π1(EK, x0)).
Proposition 3.3. For τ ̸= ±2, the relative character scheme X τ
irr(π1(Σ, x0)) is a smooth scheme
of dimension 6g −2. It follows that X τ
irr(π1(Σ, x0)) = Xτ
irr(π1(Σ, x0)) and that the set of closed
points of Xτ
irr(π1(Σ, x0)) forms a smooth complex manifold of dimension 6g −2.
Proof. We will show in Appendix I (see Theorem 8.4 and Theorem 8.7) that the character vari-
ety Xτ
irr(π1(Σ, x0)) is smooth and of dimension 6g −2. According to [Wei64, p. 156], the group
H1
par(π1(Σ, x0); Ad ρ) also has dimension 6g −2. Since T[ρ]X τ
irr(Σ) ≃H1
par(π1(Σ, x0); Ad ρ) by
Proposition 2.10, this implies that X τ
irr(π1(Σ, x0)) is a smooth scheme.
□
Proposition 3.4. For τ ̸= ±2, the character scheme X τ
irr(π1(Ui, x0)) is smooth of dimension
3g −1.
Proof. Note that π1(Ui, x0) = Fg+1.
If we ﬁx a generating set a0, a1, . . . , ag, then the relative
representation scheme is isomorphic to g copies of the scheme SL2 and one copy of the scheme
Spec Aτ for Aτ = k[x1, x2, x3, x4]/(x1x4 −x2x3 −1, x1 + x4 −τ). One can check that SpecAτ is a
smooth scheme provided that τ ̸= ±2. It follows that Rτ(π1(Ui, x0)) is a smooth scheme.
Proposition 2.13 now implies that X τ
irr(π1(Ui, x0)) is also a smooth scheme, which therefore
has the same dimension as Xτ
irr(π1(Ui, x0)). To compute this dimension, note that SL(2, C) has
dimension 3 while the conjugacy class of elements of trace τ has dimension 2 when τ ̸= ±2. Hence
dim Rτ
irr(π1(Ui, x0)) = 3g + 2 and so dim Xτ
irr(π1(Ui, x0)) = 3g + 2 −3 = 3g −1.
□
The relative character varieties which arise from the Heegaard splitting (Σ, U0, U1) can be iden-
tiﬁed with certain moduli spaces of ﬂat connections. Let us ﬁrst describe this identiﬁcation in the
case of Xτ
irr(EK). We let G = SL(2, C) and consider the trivial G-bundle EK ×G. A ﬂat connection
A on EK × G gives rise to a holonomy representation π1(EK, x0) →G by parallel transporting
the ﬁber at x0. One can check that the action of the gauge group corresponds precisely to con-
jugation in G. If A has the property that its holonomy along cp has trace τ, then the associated
representation deﬁnes a point of Xτ(EK).
It can be shown that this map (or rather its inverse) deﬁnes a bijection between Xτ(π1(EK, x0))
and the moduli space of ﬂat connections on EK × G whose holonomy has trace τ along cp. This
moduli space can be given the structure of a complex-analytic space, with respect to which the
above bijection becomes an isomorphism of complex-analytic spaces. An analogous identiﬁcation
works if we replace EK with the Ui or Σ. In the latter case, we need to consider representations
whose holonomy has trace τ along both cp and cq.
We will refer to the moduli space of ﬂat connections described above as providing an analytic
model for Xτ(π1(EK, x0)). In contrast, we think of the relative character variety as deﬁned in
Section 2.1 as the algebraic model.
Observe that the analytic model is deﬁned independently
of any choice of basepoint, while the algebraic model uses the basepoint x0. (The identiﬁcation
between the algebraic and analytic model, described above, commutes with the natural isomorphism
of algebraic models induced by changing the basepoint.) We will therefore write Xτ(EK) in place
of Xτ(π1(EK, x0)) when we wish to consider the analytic model, and similarly for the Ui and Σ.
The equivalence between analytic and algebraic models also induces an identiﬁcation of tangent
spaces. This is the content of Proposition 3.5, as we now explain. For notational simplicity, let
M be either EK, Ui, Σ. We deﬁne Hk
Aρ(M; g) to be the k-th de Rham cohomology group of M
with twisted coeﬃcients in the (restriction of the) vector bundle EK × G ×Ad g with respect to
the irreducible connection Aρ on EK × G. Let ρ : π1(M, x0) →G be the holonomy representation
induced by Aρ. We now consider the following diagram, where the horizontal arrows come from the
Mayer-Vietoris sequence for cohomology with local coeﬃcients and the vertical arrows are induced
by the inclusion maps.


## Page 12


12
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
(3.3)
H0
Aρ(Σ; g)
H1
Aρ(EK; g)
H1
Aρ(U0; g) ⊕H1
Aρ(U1; g)
H1
Aρ(Σ; g)
H1
Aρ(cp; g)
H1
Aρ(cp; g) ⊕H1
Aρ(cp; g)
H1
Aρ(cp; g) ⊕H1
Aρ(cq; g)
a
b0 b1
c
We have the following proposition, which is proved in Section 3.3.
Proposition 3.5. The following groups are canonically isomorphic:
• ker(a) ≃H1
par((π1(EK, x0); Conj(cp)); Ad ρ),
• ker(b0) ≃H1
par((π1(U0, x0); Conj(cp)); Ad ρ),
• ker(b1) ≃H1
par((π1(U1, x0); Conj(cp)); Ad ρ),
• ker(c) ≃H1
par((π1(Σ, x0); Conj(cp), Conj(cq)); Ad ρ).
Proposition 3.5 expresses the isomorphism of tangent space between analytic and algebraic mod-
els. Indeed, again letting M be EK, Ui, Σ, the reader may verify that the left hand side is the
tangent space at the irreducible ﬂat connection Aρ in the analytic model of Xτ
irr(M); cf. the dis-
cussion following [Mon16, Prop. 2.11]. The right hand side is the algebraic tangent space at the
representation ρ, as we saw in Proposition 2.10. Observe that the right hand side of course depends
on the basepoint (up to canonical isomorphism), while the left hand side does not.
As a consequence of the above discussion, observe that TρXτ
irr(Σ) can be viewed naturally as
a subspace of H1
Aρ(Σ; g). As shown for instance in [BG93], the variety Xτ
irr(Σ) carries a natural
holomorphic symplectic form (i.e. a global section of the bundle Ω2,0(Xτ
irr(Σ)) of (2, 0)-forms). If
[α], [β] ∈TρXτ
irr(Σ) ⊂H1
Aρ(Σ; g) for α1, α2 ∈Ω1(Σ; g), then
(3.4)
ωC(α, β) =
Z
Σ
Tr(α1 ∧α2).
We have the following important fact.
Proposition 3.6. For i = 1, 2, the natural embeddings Xτ
irr(Ui) →Xτ
irr(Σ) are Lagrangian with
respect to ωC.
Proof. It follows by combining Proposition 3.3 and Proposition 3.4 that Xτ
irr(Ui) is half-dimensional.
The inclusion of tangent spaces TρXτ
irr(Ui) →TρXτ
irr(Σ) corresponds to the restriction map ι∗
i :
Ω1
Aρ(Ui) →Ω1
Aρ(Σ).
Since α, β represent classes in H1
Aρ(Ui; g), it follows that they are exact in a neighborhood of
∂Ui.
By Stokes’ theorem (for manifolds with corners; see [Lee13, p. 415]), we have
ωC(α, β) =
Z
Σ
Tr(α ∧β) =
Z
∂Ui
d Tr(α ∧β) =
Z
Ui
Tr(dα ∧β) + Tr(a ∧dβ) = 0.
This concludes the proof.
□
Following Proposition 3.6, it will be convenient to write Lτ
i = Xτ
irr(Ui) ⊂Xτ
irr(Σ).
3.3. Identiﬁcation of the tangent spaces. We now prove Proposition 3.5. We will treat only
the ﬁrst three isomorphisms since the last one appears already in [BG93]. However, our argument
will easily generalize to also cover the last case. For the remainder of this section, we drop the
conjugacy classes from our notation for the parabolic cohomology groups; cf. Remark 2.9.
In the remainder of this section, let M be either of the three manifolds EK, U0 or U1. We set
Γ = π1(M, x0). The inclusion i : cp ֒→M induces a map i∗: π1(cp, x0) = Z →Γ. This in turn
induces maps i∗: Z1(Γ; Ad ρ) →Z1(π1(cp); Ad ρ) →H1(π1(cp); Ad ρ).


## Page 13


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
13
The following technical lemma is an important ingredient in the proof of Proposition 3.5. To
ﬁx some terminology, we will say that a 1-cocyle φ : Γ →g restricts to a boundary on an element
g ∈G if φ(g) = µ −Adg µ, for some µ ∈g.
Proposition 3.7. Let φ ∈Z1(Γ; Ad ρ) be a 1-cocycle. Then φ restricts to a boundary on g ∈Γ if
and only if φ restricts to a boundary on all gi ∈Conj(g).
Proof. Suppose that φ(g) = µ −Adg µ, for some µ ∈g. Given h ∈G = SL(2, C), we wish to show
that there exists some ˜µ ∈g such that φ(hgh−1) = ˜µ −Adhgh−1 ˜µ.
By Fact 2.11, it is enough to show that φ(hgh−1)hgh−1 is trace-free. Since φ ∈Z1(Γ; Ad ρ),
we have φ(hgh−1) = φ(h) + Adh(φ(g) + Adg φ(h−1)) = φ(h) + Adh φ(g) + Adhg φ(h−1). Hence
φ(hgh−1)hgh−1 = φ(h)hgh−1 + hφ(g)gh−1 + hgφ(h−1)h−1.
Observe ﬁrst of all that Tr(hφ(g)gh−1) = Tr(φ(g)g) = Tr(µg −gµ) = 0. Hence it is enough to
show that Tr
 φ(h)hgh−1 + hgφ(h−1)h−1
= 0.
Observe now that we have φ(h) = φ(he) = φ(h) + Adh φ(e). Hence Adh φ(e) = 0, which implies
φ(e) = 0. It follows that φ(h−1) = −h−1φ(h)h. Hence Tr(hgφ(h−1)h−1) = −Tr(hgh−1φ(h)) =
−Tr(φ(h)hgh−1). This completes the proof.
□
Corollary 3.8. We have ker i∗= Z1
par(Γ; Ad ρ). It follows that the kernel of the natural map
H1(Γ; Ad ρ) →H1(π1(cp); Ad ρ)
is precisely the group H1
par(Γ; Ad ρ).
Proof. If ψ ∈ker i∗, then φ([cp]) = µ −Ad[cp] µ for some µ ∈g. It now follows from Proposition 3.7
that φ ∈Z1
par(Γ; Ad ρ). The reverse direction is obvious.
□
Let H∗
sing denote singular cohomology. The ﬁrst three cases of Proposition 3.5 can now be seen
to follow from existence of the following commutative diagram:
(3.5)
H1
Aρ(M; g)
H1
sing(M; Ad ρ)
H1(π1(M, x0); Ad ρ)
H1
Aρ(cp; g)
H1
sing(cp; Ad ρ)
H1(Z; Ad ρ)
∼
∼
∼
∼
The two leftmost isomorphisms come from the fact that the complexes of abelian groups Γ(Ω∗(M; g))
and C∗(M) ⊗Z[π1(M,x0)] g both arise as the global sections of ﬂasque resolutions of the same local
system. The local system in question consists in the sections of M × G ×Ad g which are ﬂat with
respect to Aρ. See [War83, chapter 5] for details.
The two rightmost isomorphisms can be taken as a deﬁnition if M is an Eilenberg-MacLane
space. In general, the ﬁbration ˜
M →M →B(π1(M, x0)) gives rise to a spectral sequence
Hp(π1(M, x0); H1( ˜
M; g)) = Ep,q
2
⇒Hp+q(M; Ad ρ).
Consider the induced exact sequence in low-degrees 0 →E1,0
2
→H1(M; Ad ρ) →E0,1
2 . In our
case, E0,1
2
= 0 since H1( ˜
M; g) = 0. This implies H1(π1(M); g) →H1(M; Ad ρ) is an isomorphism.
3.4. Deﬁnition of the invariant. Like Heegaard Floer homology and the sheaf-theoretic SL(2, C)-
homology of [AM], our knot invariant is built from a Heegaard splitting. As in [AM], the class of
objects which we associate to Heegaard splittings are perverse sheaves. It will be important to
deﬁne precisely the category in which they live.
Let us therefore introduce the category PSh. The objects of this category are triples
(EK, γ, F)


## Page 14


14
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
where (EK, γ) is an object of SutKnot and F is a perverse sheaf on Xτ
irr(EK). For simplicity,
when the underlying sutured manifold is understood from the context, we will write F for the whole
triple.
Let (EK, γ, F) and (EK′, γ′, G) be two objects of PSh. A morphism f between them is deﬁned
to be a pair (f ∗, φ) where f ∗is the pullback induced by a diﬀeomorphism f : (EK, γ) →(EK′, γ′)
and φ : f ∗G →F is a morphism of perverse sheaves on Xτ
irr(EK). Morphisms compose according
to the rule (g∗, ψ)◦(f ∗, φ) = (f ∗g∗, φ◦f ∗(ψ)), and one can check that this rule satisﬁes the required
axioms.
Finally, we note that the category Perv(Xτ
irr(EK)) of perverse sheaves on Xτ
irr(EK) is a sub-
category of PSh. However, it is not a full subcategory, as it only includes morphisms for which f
is the identity diﬀeomorphism of (EK, γ). We denote by Perv′(Xτ
irr(EK)) the full subcategory of
PSh where the objects are (EK, γ, F) with ﬁxed (EK, γ). The morphisms in this subcategory may
involve non-trivial self-diﬀeomorphisms of (EK, γ).
For a doubly-pointed knot (Y, K, p, q), we will consider Heegaard splittings of the blowup (EK, γ).
To each such splitting H, we will associate an object P(H) ∈PSh. The construction goes as follows;
cf. [AM, Sec. 7.1].
Recall from the previous section that (Xτ
irr(Σ), ωC) is a complex symplectic manifold (i.e. ωC
is a holomorphic symplectic form). The submanifolds Lj = Xτ
irr(Uj) are complex Lagrangians
(i.e. they are complex, and the restriction of ωC to Lj vanishes). Their intersection L0 ∩L1 can
be identiﬁed as a complex analytic space with Xτ
irr(EK). We will show in the next section (see
Proposition 3.14) that the Lj carry unique spin structures. It then follows from [Bus, Thm. 2.1]
that we can associate to the above data a perverse sheaf P •
L0,L1 on Xτ
irr(EK), which is unique up to
canonical isomorphism in the category of perverse sheaves on Xτ
irr(EK). We write P(H) = P •
L0,L1
and view P(H) as an object of PSh.
We now wish to consider certain standard operations on Heegaard splittings. The three opera-
tions are diﬀeomorphism, stabilization and destabilization, and we refer to these as Heegaard moves.
We will now show that Heegaard moves induce isomorphisms of the associated objects in PSh.
Given (EK, γ), (EK′, γ′) ∈SutKnot, a diﬀeomorphism between two Heegaard splittings H =
(Σ, U0, U1) and H′ = (Σ′, U ′
0, U ′
1) is a diﬀeomorphism f : (EK, γ) →(EK′, γ′) such that Σ →Σ′ and
Ui →U ′
i. Let ZΣ and ZΣ′ be the constant sheaf on Xτ
irr(Σ) and Xτ
irr(Σ′) respectively, and note that
there is a canonical isomorphism φ : f ∗ZX′ →ZX. The perverse sheaf P •
L0,L1 is built locally by
applying the nearby cycle functor to ZX and gluing the resulting perverse sheaves (suitably twisted
by a bundle parametrizing spin strucutres). It can then be shown that φ induces an isomorphism
f ∗PL′
0,L′
1 →P •
L0,L1, which we also denote by φ by abuse of notation.
Thus, if H and H′ are Heegaard splittings of EK which are related by a diﬀeomorphism f :
(EK, γ) →(EK, γ), then there is an induced isomorphism P(H) →P(H′) given by the pair (f ∗, φ).
Next, we consider the operation of stabilization. Since it is described in [AM, Sec. 7.2], we will
only give a brief review. Given a Heegaard splitting H = (Σ, U0, U1), one drills out a solid torus
S from U1, in such a way that the boundary of S intersects Σ in a disk. This gives rise to a new
Heegaard splitting H′ = (Σ′, U ′
0, U ′
1) where Σ′ = Σ∪∂S, U ′
0 = U0∪S and U ′
1 = U1−S. The splitting
H′ is said to be obtained from H by stabillization, and we write H →H′.
Following [AM, Prop. 7.3], we claim that a stabilization H →H′ induces an isomorphism
P •
L0,L1 →P •
L′
0,L′
0 of the associated perverse sheaves in PSh. This is the content of the follow-
ing proposition.
Proposition 3.9. Suppose that H′ is obtained from H by a stabilization and that L0, L1 and
L′
0, L′
1 are the complex Lagrangians arising from H, H′ respectively. Then there is an isomorphism
of perverse sheaves P •
L′
0,L′
1 →P •
L0,L1.


## Page 15


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
15
Proof. One can essentially repeat the proof of Proposition 7.3 in [AM], replacing Y with EK and
replacing all character varieties with their relative counterparts. Two ingredients of the original
argument in [AM] need some care. First of all, the original argument uses the fact Xirr(Ui) admits
a unique spin structure. We will establish in Proposition 3.14 that this remains true for Xτ
irr(Ui).
Secondly, the argument of [AM] uses the fact Xirr(Σ) is connected and simply-connected. This
also remains true for Xτ
irr(Σ) and will be established in Appendix I.
□
If H′ is obtained from H by a stabilization, then we say that H is obtained from H′ by a desta-
bilization. We may thus associate to each destabilization an isomorphism of associated perverse
sheaves, which is just the inverse of the isomorphism induced by the opposite stabilization.
In order to extract a 3-manifold invariant from our construction, we need the following version
of the Reidemeister-Singer theorem.
Proposition 3.10. Suppose that H and H′ are Heegaard splittings for EK of genus at least 6.
Then they can be related by a sequence of stabilizations and destabilizations. We may assume that
the genus of the Heegaard splitting never drops below six in this sequence.
Proof. First of all, note by [AM, Remark 7.2] that one can replace an isotopy by a sequence of
stabilizations and destabilizations. Since each stabilization is followed by a destabilization, this
does not cause the genus to drop.
We now appeal to [Juh06, Prop. 2.15].
Up to isotopy, the Heegaard splittings H0 and H1
are induced by self-indexing Morse functions f0 and f1.
The basic idea is to argue that there
is 1-parameter family ft which is Morse for all t aside from 0 < t1 < · · · < tn < 1 where the
family has a birth-death critical point. Translating from the language of functions to the language
of handlebody decompositions, this means precisely that the Heegaard splittings can related by
stabilizations, destabilizations and isotopies. To ensure that the genus never drops below 6, one
can appeal to standard arguments of Cerf theory [Lau14, Lem. 2.5(1)] to ensure that the birth
times happen before the death times.
□
As a corollary to Propositions 3.9 and 3.10, we ﬁnd that the isomorphism class of P(H) de-
pends only on (EK, γ). Since every object (EK, γ) ∈SutKnot is the blowup of a doubly-pointed
knot (Y, K, p, q) ∈Knot∗∗, we conclude that the isomorphism class of P(H) depends only on the
underlying doubly-pointed knot. This will be strengthened in the next section.
3.5. Naturality. If H and H′ are Heegaard splittings for (EK, γ) ∈SutKnot which are related
a sequence of stabilizations and destabilizations, the induced morphism P(H) →P(H′) which we
introduced in the previous section could in principle depend on the choice of sequence. We will
now argue that this morphism is in fact independent of the choice of sequence. We refer to this
property as naturality.
The naturality of the original sheaf-theoretic invariant of Abouzaid and the second author was
established in [AM, Sec. 7.3]. Their arguments apply in our setting with no essential modiﬁcations,
so we give only a brief summary of the main steps.
The naturality of 3-manifold invariants built from Heegaard-type decompositions was studied
in a general context by J´uhasz, Thurston and Zemke [JTZ18]. Applied to our setting, their work
implies that our invariant is indeed natural provided that the morphisms associated to the three
Heegaard moves satisfy a list of axioms. (The most interesting of these axioms is invariance under
a move called handleswap.) Thus, checking naturality of the invariant boils down to checking that
these axioms are satisﬁed. This was done in [AM, Sec. 7.3] for the original sheaf-theoretic invariant
on which our construction is based. In our setting, the axioms and their veriﬁcation are essentially
the same; cf. [AM, Thm. 7.5 and 7.8].
Remark 3.11. The results of J´uhasz, Thurston and Zemke are phrased in the language of sutured
manifolds. This explains why sutured manifolds have also appeared in our construction. In contrast,


## Page 16


16
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
there was no need for sutured manifolds in the original work of [AM] since the manifolds under
consideration were closed.
As a consequence of naturality, it now makes sense to deﬁne
P •
τ (K) := P(H) = P •
L0,L1,
where H is any Heegaard splitting of (EK, γ) and L0, L1 are the Lagrangians associated to H.
Observe that P •
τ (K) is well-deﬁned in the usual category-theoretic sense: if we had chosen a
diﬀerent Heegaard splitting, we could relate P(H) and P(H) by a unique isomorphism in PSh.
A morphism (EK, γ) →(EK′, γ′) in SutKnot induces a diﬀeomorphism of Heegaard splittings
H = (Σ, U0, U1) →H′ = (Σ′, U ′
0, U ′
1).
One can check that the induced map P(H) →P(H′)
commutes with stabilization – in the case where (EK, γ) = (EK′, γ′), this is one of the axioms of
[JTZ18]; see [AM, Thm. 7.5, 2(ii)]. Hence, we get an isomorphism P •
τ (K) →P •
τ (K′) in PSh.
In summary, we have assigned to every object (EK, γ) ∈SutKnot a perverse sheaf
P •
τ (K) ∈Perv′(Xτ
irr(EK)) ⊂PSh
and to each morphism (EK, γ) →(EK′, γ′) a morphism P •
τ (K) →P •
τ (K′) in PSh. One can check
that this assignment satisﬁes the axioms of a functor. We can then obtain an invariant of doubly-
pointed knots simply by precomposing this functor SutKnot →PSh with the blowup functor
Knot∗∗→SutKnot. The resulting composition associates to a doubly-pointed knot (Y, K, p, q)
the perverse sheaf P •
τ (K). Of course, this depends on the full data (Y, K, p, q), as well as on the
choice of τ ∈(−2, 2).
One can also get a functor Knot∗∗→Gp by passing to hypercohomology, i.e. by post-composing
the above functor Knot∗∗→PSh with the hypercohomology functor PSh →Gp. As explained
in [AM, p. 2], if we ﬁx a Heegaard splitting H = (Σ, U0, U1) so that P •
τ (K) = P(H) = P •
L0,L1, then
HP∗
τ(K) should correspond to the ordinary Lagrangian Floer cohomology of L0, L1 – provided that
the Floer cohomology can be deﬁned. We therefore call
HP∗
τ(K) := H∗(P •
τ (K))
the τ-weighted sheaf-theoretic SL(2, C)-Floer cohomology of the doubly-pointed knot (Y, K, p, q).
This completes the proof of Theorem 1.1.
Observe that any pair of doubly-pointed knots (Y, K, p, q) and (Y, K, p′, q′) which share the
same underlying knot are of course isomorphic objects in Knot∗∗. It follows that the associated
τ-weighted sheaf-theoretic SL(2, C)-Floer cohomology groups are isomorphic. It therefore makes
sense to think of these groups as knot invariants, provided that one only considers them up to
isomorphism (not canonical isomorphism).
Let us mention a couple of basic properties of the invariants we just deﬁned.
Proposition 3.12. The perverse sheaf P •
τ (K) is Verdier self-dual.
Proposition 3.13. If −Y denotes Y with the opposite orientation, then the perverse sheaves P •
τ
associated to K ⊂Y and K ⊂−Y are isomorphic. In particular, for Y = S3, if we let m(K)
denote the mirror of K ⊂S3, then P •
τ (K) ∼= P •
τ (m(K)).
The proofs of these propositions are entirely similar to those of the corresponding results in the
closed case; cf. Propositions 8.1 and 8.2 in [AM].
3.6. Spin structures. We will now establish Proposition 3.14, which was postponed from the
previous section. This proposition explains why we need to assume that our Heegaard splitting has
genus at least 6. The arguments of this section will not be used subsequently, so the reader may
freely pass to the next section.
Proposition 3.14. Suppose that Σ has genus g ≥6. Then Xτ
irr(Ui) admits a unique spin structure.


## Page 17


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
17
We begin with some preparatory remarks before proving Proposition 3.14.
Let ˜Ui be the handlebody of genus g obatined from Ui by blowing down around the knot K, i.e.
ﬁlling in a cylinder with boundaries bl(p) and bl(q).
Let Cτ ⊂SL(2, C) be the conjugacy class of elements having trace τ. By [AM, Sec. 2.1(d)], Cτ is
diﬀeomorphic to TS2. Let Rirr( ˜Ui) ⊂R( ˜Ui) denote the open subvariety of irreducible representa-
tions of π1( ˜Ui, x0). Let Xirr( ˜Ui) ⊂Xirr( ˜Ui) be deﬁned analogously.
Observe that π1( ˜Ui, x0) = Fg, where Fg is the free group on g generators. By [AM, Lem. 2.6],
we have that π1(Xirr( ˜Ui)) = 0 while π2(Xirr( ˜Ui)) = Z/2. It follows that π1(Xirr( ˜Ui) × Cτ) = 0 and
π2(Xirr( ˜Ui) × Cτ) = π2(Xirr( ˜Ui)) ⊕π2(Cτ) = Z/2 ⊕Z.
Let us now consider the space (Rirr( ˜Ui) × Cτ)/Gad, where Gad = SL(2, C)/Z(SL(2, C)) =
PSL(2, C).
Lemma 3.15. The space Q := (Rirr( ˜Ui) × Cτ)/Gad admits a spin structure.
Proof. Since Gad acts freely on Rirr( ˜Ui), we see that Q is a Cτ-bundle over
(3.6)
Xirr( ˜Ui) = Rirr( ˜Ui)/Gad.
Since π1(Xirr( ˜Ui)) = 0 and π2(Xirr( ˜Ui)) = Z/2, it follows by the Hurewicz and universal coeﬃ-
cients theorem that H1(Xirr( ˜Ui), Z) = H2(Xirr( ˜Ui), Z) = 0. Let i : Cτ ֒→Q be the inclusion of a
ﬁber. The Leray-Serre spectral sequence implies that there is an isomorphism
(3.7)
i∗: H2(Q; Z)
∼
=
−→H2(Cτ; Z).
By naturality of Chern classes, we also have
i∗c1(Q) = c1(Cτ).
We now argue that w2(Cτ) = 0. Indeed, recall that Cτ ∼= TS2. We have T(TS2) = π∗(TS2) ⊕
π∗(TS2). Since S2 admits a spin structure and H1(S2, Z/2) = 0, it follows from the Whitney
product formula that 0 = w1(TS2) = w2(TS2).
Next, we consider the short exact sequence of coeﬃcients
0 →Z →Z →Z/2 →0,
which induces a long exact sequence in cohomology
(3.8)
· · · →H2(Cτ; Z) →H2(Cτ; Z) →H2(Cτ; Z) →H3(Cτ; Z) = 0.
Since w2(Cτ) is the mod 2 reduction of c1(Cτ), it follows that c1(Cτ) is divisible by 2 in H2(Cτ; Z).
Hence c1(Q) is also divisible by 2 in H2(Q; Z) by (3.7). Hence w2(Q) = 0. Since Q is a complex
manifold, it is orientable. It follows from the vanishing of w2(Q) that Q admits a spin structure.
(Indeed, an orientable manifold admits a spin structure if and only if the classifying map to BSO(n)
can be lifted to BSpin(n). The second Stiefel-Whitney class is precisely the obstruction to such a
lift; see [Coh, Thm. 4.38].)
□
Proof of Proposition 3.14. Observe that there is a natural inclusion Rirr( ˜Ui) × Cτ →Rτ
irr(Ui).
Taking quotients by the Gad action gives the inclusion Q = (Rirr( ˜Ui) × Cτ)/Gad ֒→Xτ
irr(Ui).
The residual set Xτ
irr(Ui) −Q consists of irreducible representations and has dimension at most
dim Rred( ˜Ui) + dim Cτ, where Rred( ˜Ui) := R( ˜Ui) −Rirr( ˜Ui). But Rred( ˜Ui) has complex dimension
2g + 1 [AM, proof of Lem. 2.6]. Hence Xτ
irr(Ui) −Q has complex dimension at most 2g + 3.
But Xτ
irr(Ui) has complex dimension 3g −1. Hence we ﬁnd that Xτ
irr(Ui) −Q has complex
codimension 3g −1 −(2g + 3) = g −4.
Recall that the second Stiefel-Whitney class of an n-dimensional manifold is the obstruction to
ﬁnding n −1 linearly independent sections of the tangent bundle on the 2-skeleton; see [MS74, p.
140]. This obstruction vanishes if it vanishes in the complement of a subset of complex codimension


## Page 18


18
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
≥2. We conclude that w2(Xτ
irr(Ui)) = 0 provided that g ≥6. It follows that Xτ
irr(Ui) = Lτ
i admits
a spin structure.
It remains to verify that this spin structure is unique. To this end, recall from the proof of
Lemma 3.15 that Q is a TS2-bundle over a simply connected space, hence it is simply connected
itself. Assuming still that g ≥6, it follows from an analogous dimension count that Xτ
irr(Ui) is also
simply connected. Because spin structures form an aﬃne space over the ﬁrst cohomology with Z/2
coeﬃcients, we conclude that the spin structure of Xτ
irr(Ui) = Lτ
i is unique.
□
4. Computational tools
This section is intended to collect some auxiliary results which will be useful in computing P •
τ (K)
for various examples later on. Fix a doubly-pointed knot (Y, K, p, q) and a parameter τ ∈(−2, 2).
Let EK be the blowup and ﬁx a Heegaard splitting H = (Σ, U0, U1) for EK.
We will consider two situations. First, we will show that P •
τ (K) = P •
L0,L1 is a local system if
X τ
irr(EK) is a smooth scheme. This fact relies crucially on our description of the tangent space
to relative representation schemes in Proposition 2.10. Next, we will describe P •
τ (K) in the case
where X τ
irr(EK) = Spec R, for R = C[ǫ1]
ǫn1 × . . . × C[ǫk]
ǫ
nk
k
. Such a scheme of course fails to be smooth
unless all ni = 1.
4.1. The smooth case. The following proposition is an analog of [AM, Lem. 3.4] for parabolic
group cohomology.
Proposition 4.1. Suppose that ρ : π1(EK, x0) →SL(2, C) is an irreducible representation. Then
there is an exact sequence
0 →H1
par(π1(EK, x0); Ad ρ) →H1
par(π1(U0, x0); Ad ρ) ⊕H1
par(π1(U1, x0); Ad ρ)
→H1
par(π1(Σ, x0); Ad ρ).
Note that we have dropped the conjugacy classes from our notation for the parabolic cohomology
groups; cf. Remark 2.9.
Proof. We refer the reader to the diagram (3.3). Since ρ is irreducible, it follows that H0
Aρ(Σ; g) = 0.
It can then be veriﬁed by a straightforward diagram chase that there is an exact sequence
(4.1)
0 →ker a →ker b0 ⊕ker b1 →ker c.
The claim now follows from Proposition 3.5.
□
Lemma 4.2. The Lagrangian submanifolds L0 ⊂Xτ
irr(Σ) and L1 ⊂Xτ
irr(Σ) intersect cleanly at ρ
if and only if ρ is a regular point of X τ(EK).
Proof. By combining Proposition 4.1 with Proposition 2.10, we can apply exactly the same argu-
ment as in the proof of Lemma 3.4 in [AM].
□
The following proposition is our main tool for computing P •
L0,L1.
Proposition 4.3. If X τ
irr(EK) is a smooth scheme, then P •
L0,L1 is a local system on Xτ
irr(EK).
The stalks of P •
L0,L1 on each component of Xτ
irr(EK) of complex dimension k are isomorphic to Z,
supported in degree −k.
Proof. If L0 and L1 intersect cleanly, then it was shown in [AM, Prop 6.2] that P •
L0,L1 is a local
system with stalks isomorphic to Z in degree −k on k-dimensional components. But it follows from
Lemma 4.2 that L0 and L1 intersect cleanly if and only if X τ
irr(EK) is smooth as a scheme.
□


## Page 19


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
19
4.2. A non-reduced setting. Another situation where we are able to compute P •
L0,L1 is the
following.
Proposition 4.4. Suppose that X τ
irr(EK) consists of k points of multiplicities n1, . . . , nk; i.e., it
equals Spec R, where
R = C[ǫ1]
ǫn1
× . . . × C[ǫk]
ǫnk
k
.
Then P •
L0,L1 is a sheaf concentrated in degree 0, with stalk Zni over the ith point.
Proposition 4.4 is a consequence of the following general lemma, which appeals to theory of
d-critical loci introduced by Joyce in [Joy15]. A (complex-analytic) d-critical locus is a complex-
analytic space X along with a section s of a certain sheaf S0
X which locally parametrizes diﬀerent
ways of writing X as the critical locus of a holomorphic function; see [Joy15, Def. 2.5].
Lemma 4.5. Consider two complex spin Lagrangians L0, L1 in a complex symplectic manifold M.
Let X = {x} ∈L0 ∩L1 be an isolated intersection point, such that, as a complex analytic space, X
is nonreduced of order n ≥2. Then the stalk of the perverse sheaf P •
L0,L1 over x is Zn in degree
zero.
Proof. Let O = OC be the space of holomorphic functions in one variable z. By hypothesis, the
analytic space X under consideration is isomorphic to O/(zn).
We know that locally, the Lagrangian L1 is the graph of df, for some holomorphic function
f : U →C, where U is a neighborhood of x in L0. This turns X into a d-critical locus in the sense
of [Joy15, Def. 2.5]. In our case, the sheaf S0
X is computed in [Joy15, Example 2.16] in the algebraic
setting, but the same calculation applies in the complex analytic setting: the sections s of S0
X are
elements of the module (zn+1)/(z2n) over O/(zn):
s = an+1zn+1 + an+2zn+2 + · · · + a2n−1z2n−1 + (z2n).
Such a section s speciﬁes the structure of X as a d-critical locus (provided that an+1 ̸= 0). Once
this structure is determined, by Proposition 2.22 in [Joy15], we ﬁnd that, if m denotes the complex
dimension of L0, then there are local holomorphic coordinates z1, . . . , zm near x ∈L0 in which we
can write
f(z1, . . . , zm) = s(z1) + z2
2 + · · · + z2
m.
The perverse sheaf P •
L0,L1|X is Zµ−1 in degree 0, where µ is the Milnor number of f. Regardless
of the values of an+1 ̸= 0, an+2, . . . , a2n−1, the Milnor number is n + 1, and the claim follows.
□
5. Relation to the bA-polynomial
In this section, we will relate P •
τ (K) to a knot invariant known as the bA-polynomial, which is
a close cousin of the better-known A-polynomial. For knots in integral homology 3-spheres whose
SL(2, C)-character variety is 1-dimensional, we will show under certain technical assumptions that
HP∗
τ(K) simply recovers the l-degree of the bA-polynomial.
This relationship breaks down for
general knots, as we will see in Section 7 when considering certain connected sums of knots. The
bA-polynomial is computable in many situations.
In Section 6, we will leverage some of these
computations to determine HP∗
τ(K) for various classes of prime knots.
5.1. Preparations. Let us consider a doubly-pointed knot (Y, K, p, q) ∈Knot∗∗and its blowup
(EK, γ) ∈SutKnot. From now on, we will always assume that the manifold Y is an integral
homology 3-sphere. This assumption will allow us to talk about the Alexander polynomial (in
Assumption B.3 below) and the A- and bA-polynomials (in Section 5.5).
We ﬁx a basepoint x0 ∈cp and let
(5.1)
Γ = π1(EK, x0) = ⟨g1, . . . , gn | r1, . . . , rl⟩


## Page 20


20
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
We ﬁx τ ∈(−2, 2) and let c = Conj([cp]). We will also assume that the presentation of Γ which
we have chosen has the property that Conj(g1) = c.
We will rely throughout this section on the deﬁnitions and notation introduced in Section 2.1. In
particular, we remind the reader that A(Γ) is the coordinate ring of the representation scheme R(Γ).
Similarly, Aτ(Γ) is the coordinate ring of the relative representation scheme Rτ(Γ) = Rτ(Γ; c).
These coordinate rings are well-deﬁned up to unique isomorphism.
As described in Example 2.4, one can construct a model for A(Γ) by associating to each generator
gi ∈Γ the formal variables xgi
11, xgi
12, xgi
21, xgi
22 and modding out the free k-algebra k[xg1
11, xg1
12, . . . , xgn
22]
by the appropriate relations. One can then construct Aτ(Γ) by setting
(5.2)
Aτ(Γ) = A(Γ)/(xg1
11 + xg1
22 −τ).
It will be convenient to write A0(Γ) := A(Γ)/ nil(A(Γ)), where nil(A(Γ)) is the nilradical of
A(Γ). Since SL2 is linearly reductive, we have
(5.3)
A(Γ)SL2/ nil(A(Γ)SL2) = A(Γ)SL2/ nil(A(Γ))SL2 = (A(Γ)/ nil(A(Γ)))SL2 = A0(Γ)SL2.
Hence the character variety X(Γ) is just the spectrum of A0(Γ)SL2. For g ∈Γ, one can deﬁne
an element τg ∈A0(Γ)SL2 called the character of g.
For a closed point [ρ] ∈X(Γ), we have
τg(ρ) = Tr(ρ(g)). Using the well-known identity
τgτh = τgh + τgh−1,
it can be shown that the N = 2n −1 functions
τgi1...gik, 1 ≤k ≤n, 1 ≤i1 < · · · < ik ≤n
in fact generate A0(Γ)SL2.
In particular, there is a surjective ring map
(5.4)
φ : k[x1, . . . , xN] →A0(Γ)SL2
where we can assume that x1 7→τg1 = xg1
11 + xg1
22. Letting I = ker φ, we can use (5.4) to identify
(5.5)
k[x1, . . . , xN]/I = A0(Γ)SL2.
It will be convenient later on to write
(5.6)
A := k[x1, . . . , xN]/I = A0(Γ)SL2.
Finally, we let
Hτ ֒→AN
be the closed embedding corresponding to the ring map k[x1, . . . , xN] →k[x1, . . . , xN]/(x1 −τ).
We let πn : AN →A be the projection map (x1, . . . , xN) 7→xn.
5.2. Some assumptions on the character variety. Throughout this section, we limit our at-
tention to knots whose SL(2, C)-character variety is 1-dimensional. We usually also need to assume
that the character scheme is reduced. We wish to keep track of how the statements proved in this
section depend on these assumptions. It will therefore be convenient to label them separately.
Assumption A.1. The character scheme X (Γ) is of dimension at most 1.
Assumption A.2. The character scheme X (Γ) is reduced.
We will see in Section 6 that A.1 is satisﬁed for many familiar examples of prime knots, including
all two-bridge knots, torus knots and certain hyperbolic pretzel knots. However, it fails for simple
examples of composite knots, as we will see in Section 7. A.2 has also been veriﬁed for two-bridge
knots, torus knots and many pretzel knots. Moreover, there are no examples of knots for which
A.2 is known to fail and it has been conjectured by Le and Tran (see [LT15, Conjecture 2]) that
A.2 is true for all knots.


## Page 21


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
21
It will also be useful to consider some assumptions on a complex parameter τ ∈C. Since P •
τ (K)
is only deﬁned for τ ∈(−2, 2), we will sometimes need to restrict τ to the real interval (−2, 2) ⊂C.
However, it is in general more convenient to allow τ to take arbitrary complex values in this section.
Assumption B.1. The analytic space Hτ = {x1 = τ} does not contain any component of
π−1(−2, 2) ∩X(Γ).
Assumption B.2. There is an analytic neighborhood of Hτ ∩X(Γ) ⊂X(Γ) on which X(Γ) is
smooth.
Assumption B.3. If x ∈[0, 1] has the property that e4πix is a root of the Alexander polynomial
of K, then τ ̸= 2 cos(2πx).
Assumption B.4. There is an analytic neighborhood of Hτ ∩X(Γ) ⊂X(Γ) on which the projection
π1 : X(Γ) →C is proper.
In practice, these assumptions may be diﬃcult to verify for a given knot K ⊂Y without explicit
knowledge of its character variety. However, the following proposition shows that they are satisﬁed
on a coﬁnite subset of C whenever A.1 holds.
Proposition 5.1. Suppose that the character variety of K ⊂Y satisﬁes A.1. Then B.1–B.4 are
satisﬁed for all but ﬁnitely many choices of τ ∈C.
Proof. Since Γ is a ﬁnitely-generated group, A(Γ) is a Noetherian ring. This means that X(Γ)
is a Noetherian scheme. It is a general fact that Noetherian schemes have at most ﬁnitely many
irreducible components. Since Hτ ∩Hτ ′ = ∅if τ ̸= τ ′, it follows that B.1 holds for all but ﬁnitely
many τ ∈(−2, 2).
The singular locus of a complex algebraic variety is Zariski closed and of complex codimension
at least 1. Since X(Γ) is 1-dimensional by A.1, it follows that X(Γ) has a 0-dimensional set of
singularities which is therefore ﬁnite. Hence B.2 holds on a coﬁnite subset of C.
It’s clear that B.3 holds in a coﬁnite subset of C. Finally, the fact that B.4 holds for all but
ﬁnitely many τ ∈C is the content of Lemma 5.12, whose proof is posponed to Section 5.4.
□
5.3. Relating the ﬁber product to the quotient. In (5.4), we considered an embedding of
X(Γ) into CN. The coordinate functions on CN pull back under this embedding to the characters
of certain products of generators of Γ, and we assumed in particular that x1 pulls back to xg1
11 +xg1
22.
This suggests that the relative character scheme X τ(Γ) should be obtained by intersecting the
image of the ordinary character variety X(Γ) with the hyperplane Hτ = {x1 = τ}. The purpose of
this section is to make this precise.
Recall from (5.6) that we have
A := k[x1, . . . , xN]/I = A0(Γ)SL2.
We let fτ = (x1 −τ) ∈k[x1, . . . , xN]. By abuse of notation, we will also view fτ as an element of
A0(Γ)SL2 ⊂A0(Γ) via (5.4), as well as an element of A via the quotient projection.
Let us consider the quotient map
A0(Γ) →A0(Γ)/(fτA0(Γ)).
The SL2 action on A0(Γ) induces a surjective map on the ring of invariants
A →(A0(Γ)/(fτA0(Γ)))SL2 = A0(Γ)SL2/(fτA0(Γ))SL2.
Observe that the ideal (fτ) ⊂A is in the kernel of this map. Thus we obtain a surjection
(5.7)
A/(fτ) →A0(Γ)SL2/(fτA0(Γ))SL2.
Lemma 5.2. Suppose that K ⊂Y satisﬁes A.2. It then follows that
(5.8)
A0(Γ)SL2/(fτA0(Γ))SL2 = A(Γ)SL2/(fτA(Γ))SL2 = (A(Γ)/(fτA(Γ)))SL2 .


## Page 22


22
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
Proof. According to A.2, we have nil(A(Γ)SL2) = 0. It then follows from (5.3) that A(Γ)SL2 =
A0(Γ)SL2. Note next that
(fτA0(Γ))SL2 = (fτA(Γ))SL2/(fτA(Γ) ∩nil A(Γ))SL2.
Since (fτA(Γ) ∩nil(A))SL2 ⊂nil(A(Γ)SL2 = ∅, we conclude that (fτA0(Γ))SL2 = (fτA(Γ))SL2. The
conclusion follows.
□
Observe that (A(Γ)/(fτA(Γ)))SL2 is the coordinate ring of X τ(Γ). Under the hypotheses of
Lemma 5.2, it follows that the map (5.7) induces a closed embedding of schemes
(5.9)
X τ(Γ) →(Hτ ∩X(Γ)).
It is easy to see that the underlying embedding of varieties is an isomorphism. We would like to
show that this is also true for schemes.
Proposition 5.3. Suppose that K ⊂Y satisﬁed A.1–A.2 and that τ ∈C satisﬁes B.1. Then the
closed embedding (5.9) is an isomorphism.
Proof. Let R be the coordinate ring of the group scheme SL2. Let µ : A0(Γ) →A0(Γ) ⊗R be the
map of C-algebras which induces the SL2-action on Spec A0(Γ) = R(Γ). Note that µ(f) = f ⊗1
for f ∈A0(Γ)SL2.
It is equivalent for (5.9) and for (5.7) to be isomorphisms. Since we know that (5.7) is surjective,
we will show that it is injective.
To this end, we need to show that (fτA0(Γ))SL2 ⊂fτA0(Γ)SL2.
So suppose that (fτg) ∈
(fτA0(Γ))SL2 while g /∈A0(Γ)SL2. This implies that
0 = µ(fτg) −µ(fτ)µ(g) = (fτg) ⊗1 −(fτ ⊗1)µ(g) = (fτ ⊗1)(g ⊗1) −(fτ ⊗1)µ(g)
= (fτ ⊗1)(g ⊗1 −µ(g)).
(5.10)
Given a closed point x ∈SpecMax R, there is an evaluation map evx : A0(Γ)⊗R →A0(Γ). Since
A0(Γ) and R are reduced C-algebras (i.e. the associated schemes are reduced), it can be shown
that g ⊗1 and µ(g) are equal if and only if they are equal at all closed points.1 Since g ̸∈A0(Γ)SL2,
we see that there exists x0 ∈SpecMax R such that evx0(g ⊗1) ̸= evx0(µ(g)).
Let us now apply evx0 to (5.10) to obtain
(5.11)
0 = evx0(fτ ⊗1) evx0(g ⊗1 −µ(g)) = fτ evx0(g ⊗1 −µ(g)).
We conclude that fτ ∈A0(Γ) is a zero divisor.
But since A0(Γ) is reduced, it follows that
fτ vanishes on an irreducible component C ⊂Spec A0(Γ) = R(Γ) (see [Man75, 1.4.8(2)]).
Let
π : R(Γ) →X(Γ) be the natural projection. Observe that π(C) ⊂Hτ. We wish to show that π(C)
is a 1-dimensional component of X(Γ).
Let’s ﬁrst show that π(C) is not zero-dimensional. If it were, then it would consist of a single
point [ρ]. Since we can always ﬁnd an abelian representation with trace τ, it follows that [ρ] must
be abelian.
But one can then directly verify that π−1(π(C)) = π−1([ρ]) does not contain any
irreducible components of X(Γ). Indeed, if ρ′ ∈π−1(π(C)), then ρ′ is abelian and hence can be
deformed through abelian representations. Hence π(C) is at least one-dimensional. Therefore it is
exactly one-dimensional by A.1. This is a contradiction in view of B.1.
□
Deﬁnition 5.4. Let X0(Γ) ⊂X(Γ) be the open subscheme obtained from X(Γ) by removing all
components which do not contain an irreducible representation.
Proposition 5.5. Suppose that K ⊂Y satisﬁes A.1–A.2 and τ ∈C satisﬁes B.1 and B.3. Then
there is an isomorphism X τ
irr(Γ) →Hτ ∩X0(Γ).
1At the cost of slightly complicating the argument, we could avoid appealing to the fact that A0(Γ) is reduced;
see [Gul, Sec. 3, Rmk. 2.4].


## Page 23


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
23
Proof. Since X τ
irr(Γ) ֒→X τ(Γ) is an open subscheme, it follows from the previous proposition that
there is an open embedding X τ
irr(Γ) ֒→X τ(Γ) →Hτ ∩X(Γ). Observe that the image of this map
lands inside Hτ ∩X0(Γ). It suﬃces to verify that X τ
irr(Γ) →X0(Γ) is surjective on closed points
to obtain the desired claim.
If ρ is irreducible, then [ρ] ∈Hτ ∩X0(Γ) is in the image of the above map. If ρ is reducible,
then note by the deﬁnition of X0(Γ) that [ρ] ∈X(Γ) cannot belong to the component of abelian
representations. It follows from [CCG+94, Prop. 6.2] that τ = 2 cos(2πx) where e4πix is a root of
the Alexander polynomial of K. This contradicts B.3.
□
We now analyze the structure of Hτ ∩X0(Γ).
Proposition 5.6. Suppose that K ⊂Y satisﬁes A.1–A.2 and that τ ∈C satisﬁes B.1–B.2. Then
we can write Hτ ∩X0(Γ) = Spec Rτ, where
Rτ = C[ǫ1]
ǫn1
1
× . . . × C[ǫk]
ǫnk
k
for some values n1, . . . , nk ≥1.
Proof. It follows from A.1 and B.1 that Hτ ∩X(Γ) and hence Hτ ∩X0(Γ) is zero-dimensional. Using
A.1 and B.2, we ﬁnd that Hτ ∩X0(Γ) embeds into a smooth ﬁnite-type C-scheme of dimension 1.
The claim then results from Lemma 5.7 below.
□
Lemma 5.7. Let Z ⊂S be an embedding of a zero-dimensional C-scheme of ﬁnite type into a
smooth, one-dimensional C-scheme of ﬁnite type. Then Z = Spec B for B = C[ǫ1]
ǫn1
1
× . . . × C[ǫk]
ǫ
nk
k
.
Proof. We can easily reduce to the case where Z = SpecB is connected and hence l = 1. Then the
closed embedding Z ⊂S is induced by a surjective ring map A →B. Since SpecB is connected
and of dimension 0, it follows that B is a local ring with maximal ideal m. Let p be the kernel of
the composition A →B →B/m. Then we have a surjection Ap →Bm = B.
Note that B is a Noetherian ring of dimension 0. It follows that B is an Artinian ring, and hence
complete. Hence we have a surjection bAp →bB = B. But Ap is a discrete valuation ring since S is
smooth. Hence bAp ≃C[[t]]. Since the ideals of C[[t]] are all of the form (tn) for n ≥0, we conclude
that B ≃C[[t]](tn) = C[t]/(tn).
□
Corollary 5.8. Suppose that K ⊂Y satisﬁes A.1–A.2 and that τ ∈(−2, 2) satisﬁes B.1, B.2
and B.3. Let Rτ be as in Proposition 5.6. Then P •
τ (K) is supported in degree 0 and we have
HP0
τ(K) = Zd, where d = Pl
1 ni.
Proof. Apply Propositions 5.5 and 5.6. If ni = 1 for all i, then Spec Rτ is a smooth scheme of
dimension 0.
It follows from Proposition 4.3 that P •
τ (K) consists of a copy of Z supported in
degree 0 over each point.
If nj > 1 for some j, then Spec Rτ is not smooth. However, we can apply Proposition 4.4, which
implies that P •
τ (K) is still supported in degree 0, with stalks isomorphic to Znj over each point of
multiplicity nj.
□
5.4. Independence of parameters. We now move to analyzing the dependence of HP∗
τ(K) on
the parameter τ. If K ⊂Y satisﬁes A.1–A.2, we will show that HP∗
τ(K) is constant over all values
of τ which satisfy B.1–B.4.
Recall that in (5.1) we chose a set of generators for Γ. This gives embeddings of X0(Γ) and
X(Γ) in some aﬃne space Cn. Let X0(Γ) ⊂CPn and X(Γ) ⊂CPn denote the projective closures
of X0(Γ) and X(Γ) respectively.
We endow X0(Γ) and X(Γ) with the unique reduced scheme
structure, which ensures that they are well-deﬁned as (possibly singular) schemes. We also let
Dτ ⊂CPn be the projective closure of Hτ, i.e. Dτ = CPn−1 ⊂CPn is a hyperplane.


## Page 24


24
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
If X ⊂CPn is a projective scheme of dimension n, we let pX(m) ∈Z[m] be the Hilbert polynomial
of X. Recall that the degree of X is the leading coeﬃcient of pX times n!.
We then have the following version of B´ezout’s theorem.
Theorem 5.9 (18.6.K [Vak]). Let X ⊂CPn be a reduced projective subscheme of dimension at
least 1 and let D be a hypersurface. Suppose that D does not contain any components of X. Then
deg(D ∩X) = deg(D) deg(X).
Corollary 5.10. If τ ∈C satisﬁes B.1, then we have deg(Dτ ∩X0(Γ)) = deg(Dτ) deg(X0(Γ)) =
deg(X0(Γ)).
The following technical lemma will be useful.
Lemma 5.11. Assume that K ⊂Y satisﬁes A.1–A.2. Let U1 ⊂C be the Zariski open subset of
τ ∈C that satisfy B.1. Then, over τ ∈U1, the subset of intersection points {Dτ ∩X0(Γ)} ⊂CPn
varies continuously in τ with respect to the Euclidean topology.
Proof. Let Hilbd(n) be the Hilbert scheme parametrizing all subschemes of CPn whose Hilbert
polynomial is the positive integer d. Topologically, we can think of Hilbd(n) as the set of d-tuples
of unordered, not necessarily distinct points of CPn.
By deﬁnition, for τ ∈U1, the hypersurface Hτ does not contain any component of X(Γ). Since
the intersection Dτ ∩X0(Γ) has degree d, there is an induced map h : U1 →Hilbd(n) given by
h(τ) = X0(Γ) ∩Dτ. Since h is in particular continuous with respect to the Euclidean topology, the
lemma follows.
□
Lemma 5.11 leads us to a useful reformulation of B.4.
Let us deﬁne L∞⊂CPn to be the
hyperplane at inﬁnity associated to the projective closure X0(Γ) ⊂X0(Γ) ⊂CPn = An ∪L∞.
Under the hypothesis that τ ∈C satisﬁes A.2 and B.1, we have
(5.12)
deg(Dτ ∩X0(Γ)) + deg(Dτ ∩(X0(Γ) ∩L∞)) = deg(Dτ ∩X0(Γ)).
Now Corollary 5.10 implies that the right hand side of (5.12) is constant.
It then follows by
Lemma 5.11 that B.4 fails precisely at those points where deg(Dτ ∩(X0(Γ) ∩L∞)) jumps.
We can now prove a lemma which was already promised in the proof of Proposition 5.1.
Lemma 5.12. Assume that K ⊂Y satisﬁes A.1–A.2. Then B.4 holds for all but ﬁnitely many
choices of τ ∈C.
Proof. As in Lemma 5.11, let U1 ⊂C be the coﬁnite set on which B.1 is satisﬁed. By our previous
discussion, it is enough to check that the degree of Dτ ∩(X0(Γ)∩L∞) jumps at ﬁnitely many points
of U1.
For τ ∈U1, note that (Dτ ∩X0(Γ) ∩L∞) = (Dτ ∩L∞) ∩(X0(Γ) ∩L∞), where equality holds
both as topological spaces and as schemes. Now (X0(Γ) ∩L∞) is a zero-dimensional scheme, i.e.
topologically a disjoint union of points p1, . . . , pl. We can think of (Dτ ∩L∞) = CPn−2 as a family
of hyperplanes in CPn−1.
The key algebro-geometric fact is that, for any positive integer m ≥1, the condition for (Dτ ∩L∞)
to intersect a point pi with multiplicity m is Zariski closed. This implies that the jumps occur in
a Zariski closed subset of U1 ⊂C, i.e. at a ﬁnite set of points. Since U1 ⊂C is coﬁnite, this proves
the lemma.
□
Corollary 5.13. Suppose that K ⊂Y satisﬁes A.1–A.2 and let U14 ⊂C be the Zariski open subset
of τ ∈C that satisfy B.1 and B.4. Then deg(Hτ ∩X0(Γ)) is independent of τ ∈U14.
Proof. We know that deg(Dτ ∩X0(Γ)) and deg(Dτ ∩(X0(Γ) ∩L∞)) are constant on U14 by Corol-
lary 5.10 and the discussion following Lemma 5.11. The conclusion now follows from (5.12).
□


## Page 25


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
25
Corollary 5.14. Suppose that K ⊂Y satisﬁes A.1–A.2. Let U ⊂C be the Zariski open subset of
τ ∈C that satisfy the four assumptions B.1–B.4; cf. Proposition 5.1. Then, for τ ∈(−2, 2) ∩U,
the hypercohomology HP∗
τ(K) is supported in degree 0 and is independent of τ.
Proof. We just saw in Corollary 5.13 that deg(Hτ ∩X0(Γ)) is constant for τ ∈U. Let us then set
d = deg(Hτ ∩X0(Γ)) for τ ∈U.
According to Proposition 5.6, we have Hτ ∩X0(Γ) = Spec Rτ where Rτ = C[ǫ1]
ǫn1
1
× . . . × C[ǫk]
ǫ
nk
l
.
One can verify using the deﬁnition of degree that deg(Spec Rτ) = Pk
i=1 ni. Hence d = deg(Hτ ∩
X0(Γ)) = Pk
i=1 ni. It now follows from Corollary 5.8 that HP∗
τ(K) is supported in degree 0 with
HP∗
τ(K) = Zd.
□
5.5. Relation to the bA-polynomial. Let us choose a pair of loops µ, λ ⊂∂EK so that (µ, λ) is
a basis for π1(∂EK, x0) = Z ⊕Z and λ is nullhomologous in EK. These loops are unique up to
orientation and isotopy in EK.
Let us now outline the deﬁnition of the A- and bA-polynomials. These are polynomials in two
complex variables m, l which are built from the SL(2, C)-character variety of a knot in a homology
3-sphere. The A-polynomial was introduced in [CCG+94] and has been extensively studied since
then.
The bA-polynomial is a close relative; it was deﬁned by Boyer–Zhang [BZ01] and it also
appears in the work of Boden and Curtis [BC16] from which we draw our exposition.
To deﬁne these polynomial invariants, we consider the inclusion ∂EK →EK which induces a
map i∗: π1(∂EK, x0) →π1(EK, x0) = Γ. Let r : X(EK) →X(∂EK) be the induced map on
character varieties. Referring to (5.1), we may assume that i∗(µ) = g1.
It is a general fact that points on the character variety X(∂EK) are in bijective correspondence
with completely reducible representations π1(∂EK, x0) →SL(2, C).
Since π1(∂EK, x0) = Z ⊕
Z is abelian, the set of completely reducible representations coincides with the set of diagonal
representations.
We may thus deﬁne a map t : C∗× C∗→X(∂M) by sending a pair (x, y) ∈C∗× C∗to the
unique diagonal representation ρ such that x is an eigenvalue of ρ(µ) and y is an eigenvalue of ρ(λ).
One can check that t is 2 : 1 away from the points (1, 1), (1, −1), (−1, 1), (−1, 1).
To deﬁne the A-polynomial, consider the aﬃne variety t−1(r(X(EK))) ⊂C∗× C∗⊂C2. It is
a fact of algebraic geometry that any codimension 1 subvariety in Cn is the vanishing locus of a
principal ideal. It therefore makes sense to consider the following deﬁnition.
Deﬁnition 5.15. ([CCG+94]) Let A(K) = A(m, l) ∈C[m, l] be the generator of the vanishing
ideal of the 1-dimensional components of t−1(r(X(EK))) ⊂C2. We call A(m, l) the A-polynomial
of K ⊂Y . This polynomial is well-deﬁned up to multiplication by nonzero scalars.
To deﬁne the bA-polynomial, let {Xj} be an enumeration of the one-dimensional components of
X(EK) which contain an irreducible character and have the property that the Zariski closure r(Xj)
is 1-dimensional. Let αj be the degree of r : Xj →r(Xj) ⊂X(∂M). Finally, let bAj(m, l) be the
deﬁning polynomial (of smallest degree) of t−1(r(Xj)) ⊂C∗× C∗⊂C2.
Deﬁnition 5.16. ([BZ01]) Let bA(K) := Q
j bAj(m, l)αj. We say that bA(K) is the bA-polynomial of
K ⊂Y . This polynomial is well-deﬁned up to multiplication by nonzero scalars.
The relation between the bA-polynomial and our knot invariant is expressed in the following
statement.
Theorem 5.17. Let Y be an integral homology sphere. Suppose that K ⊂Y satisﬁes A.1–A.2
and that τ ∈(−2, 2) satisﬁes B.1–B.4.
It then follows that HP∗
τ(K) = Zd in degree 0, where
d = degl bA(m, l).


## Page 26


26
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
Before proving Theorem 5.17, we need the following technical lemma.
Lemma 5.18. Assume that K ⊂Y satisﬁes A.1–A.2. Then for all but ﬁnitely many choices of
τ ∈C, the scheme theoretic intersection Hτ ∩X0(Γ) ⊂Cn is reduced and is topologically a ﬁnite
set of points.
Proof. As in Corollary 5.13, let U14 ⊂C be the coﬁnite set on which B.1 and B.4 are satisﬁed. We
saw there that Hτ ∩X0(Γ) has degree d for all τ ∈U14. It follows as in the proof of Lemma 5.11 that
there is a map U14 →Hilbd(Cn) sending τ ∈U14 to Hτ ∩X0(Γ). Non-reducedness of the scheme-
theoretic intersection Hτ ∩X0(Γ) is equivalent to two points colliding in the Hilbert scheme. This
is a Zariski closed condition. Hence, if we can show that this condition is not always satisﬁed, it
will follow that it is satisﬁed for at most ﬁnitely many points.
To this end, referring to the group presentation (5.1), observe that the {Hτ}τ∈C are set theo-
retically just aﬃne coordinate hyperplanes in Cn, i.e. Hτ = {(x1, . . . , xn) ∈Cn | x1 = τ}. Let us
now consider the map π : X0(Γ) →C given by projecting onto the ﬁrst coordinate. If Hτ ∩X0(Γ)
has a non-reduced point, then τ is a critical value of π. Hence it is enough to show that the set of
critical values of π is not all of C. But since X0(Γ) is a smooth manifold away from a ﬁnite set of
singularities, this is a direct corollary of Sard’s theorem.
□
We can now give the proof of Theorem 5.17.
Proof of Theorem 5.17. Let C = S
j Xj ⊂Cn be the union of the 1-dimensional components of
X(Γ) ⊂Cn which contain an irreducible representation. Note that C is precisely the closure of
X0(Γ) in Cn. It follows from Corollary 5.8 and Lemma 5.18 that there is a coﬁnite set V ⊂(−2, 2)
such that P
j #{Hσ ∩Xj} = d for σ ∈V , where HP∗
σ(K) = Zd in degree 0. By Corollary 5.14, we
also have HP∗
τ(K) = Zd in degree 0 for the given value of τ.
In the notation of Deﬁnition 5.16, the restriction of r to Xj is a degree αj map. This means
that there is a Zariski open subset of r(Xj) in which every point has αj preimages. Since r(Xj)
has dimension 1, this open subset has ﬁnite complement. Hence there is a coﬁnite subset ˜V ⊂V ⊂
(−2, 2) such that every point in r(Hσ ∩Xj) has precisely αj preimages for σ ∈˜V . It follows that
r(Hσ ∩Xj) has cardinality #{Hσ ∩Xj}/αj for σ ∈˜V .
We now consider the preimage of r(Hσ∩Xj) under t for σ ∈˜V . Since σ ̸= ±2, this has cardinality
2(#{Hσ ∩Xj}/αj). Fixing m0 so that 2 cos(m0) = τ ′, we observe that half of the points in the set
t−1(r(Hσ ∩Cj)) are solutions to bAj(K)(m0, l) = 0 and the other half to bAj(K)(1/m0, l) = 0. In
other words, the hyperplane {m0 = 0} intersects the zero set of bA in #{Hσ ∩Xj}/αj points.
Since this holds for all σ ∈˜V , we conclude that degl bAj(K) = #{Hσ ∩Xj}/αj. But bA(K) =
Q
j bAj(K)αj so degl bA(K) = P
j αj(#{Hσ ∩Xj}/αj) = P
j #{Hσ ∩Xj} = d.
□
Proof of Theorem 1.3. This is an immediate consequence of Proposition 5.1 and Theorem 5.17.
□
6. Some computations
In the previous section, we studied P •
τ (K) for knots satisfying A.1 and A.2. We showed that
HP∗
τ(K) is generically independent of τ and expressible in terms of the bA-polynomial of K; cf.
Proposition 5.1 and Theorem 5.17. In this section, we will consider examples of knots which satisfy
A.1–A.2. We will use the results of the previous section to compute HP∗
τ(K) for some of these
knots.
6.1. Some knots satisfying A.1 and A.2. The ﬁrst class of knots which we consider is the
following.
Deﬁnition 6.1. A knot K ⊂S3 is said to be small if its complement does not contain a closed,
orientable, essential surface. Otherwise, K is said to be large.


## Page 27


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
27
The class of small knots is known to contain all 2-bridge knots [HT85] and all torus knots [Tsa94].
A well-known result of Culler and Shalen [CCG+94, Sec. 2.4] implies that the character variety of
a small knot is at most 1-dimensional. It follows that small knots satisfy A.1. More information
on the properties of small knots can be found in the survey of Ozawa [Oza17, Sec. 5].
We also wish to consider a distinguished class of hyperbolic knots. Recall that a hyperbolic knot
can be characterized by the property that its complement admits a discrete, faithful representation
to PSL(2, C). It is a general fact that this distinguished representation can always be lifted to
SL(2, C); see [CS83, Prop. 3.1.1]. Note however that the SL(2, C)-character variety of a hyperbolic
knot may in general contain many components, and one does not expect all of them to contain a
discrete, faithful representation.
Deﬁnition 6.2. We say that a knot K ⊂S3 is slim if it is hyperbolic and if every component of
X(Γ) which contains an irreducible representation also contains a discrete, faithful representation.
Given an orientable hyperbolic 3-manifold of ﬁnite volume with n cusps, a well-known result
of 3-manifold topology which is usually attributed to Thurston (see [Sha02, Sec. 4.5]) states that
any component of its SL(2, C)-character variety which contains a discrete, faithful representation
is n-dimensional. In particular, any component of the character variety of a hyperbolic knot which
contains a discrete, faithful representation is 1-dimensional. It follows that all components of the
character variety of a slim knot which contain an irreducible representation are 1-dimensional. The
remaining component of the character variety consists of abelian representations and is always
1-dimensional. It follows that slim knots satisfy A.1.
It can be shown using [Bur90] that hyperbolic twist knots are slim, because their character
variety has only one component containing an irreducible representation. It has also been shown
in [Mat00] that the (−2, 3, n) pretzel knot is slim provided that it is hyperbolic and that n is not
divisible by 3. In fact, (−2, 3, n) is hyperbolic precisely when n /∈{1, 3, 5}; see [MM08, p. 1834].
We refer the reader to [BLZ02, p. 2] for a discussion of these facts.
The classes of small knots and slim knots overlap, but neither one is contained in the other.
For example, it is a fact that all twist-knots are two-bridge knots, which implies that hyperbolic
twist-knots are both small and slim. However, any two-bridge knot which is not hyperbolic (e.g.
the trefoil) is automatically small but not slim.
An example of a slim knot which is not small is the (−2, 3, 7) pretzel knot, which is also known
as the Fintushel-Stern knot. It is easy to see that this knot admits multiple Conway spheres, i.e.
2-spheres which intersect the knot transversally in 4 points. It can be shown that any knot which
admits a Conway sphere automatically admits a genus 2 incompressible surface in its complement,
and therefore fails to be small. We refer to [Bud] for an illuminating exposition of these facts.
We now discuss to what extent the classes of small knots and slim knots satisfy A.2. As we
noted in Section 5.1, A.2 has been conjectured to hold for all knots in S3. This has been veriﬁed
for many examples, including all two-bridge knots and torus knots; see [BC16, Sec. 2]. It has also
been veriﬁed by Le and Tran [LT15] for the (−2, 3, 2n + 1) pretzel knot for all n ∈Z. We can
therefore state the following result, which can be viewed as a corollary of Theorem 5.17 and the
preceding discussion. The ﬁrst part of this corollary is exactly Theorem 1.4 from the Introduction.
Corollary 6.3. Suppose that K ⊂S3 is a two-bridge knot, a torus knot, or a (−2, 3, 2n+1) pretzel
knot where n ̸= 0, 1, 2 and 2n + 1 is not divisible by 3. Then, for all but ﬁnitely many τ ∈(−2, 2),
HP∗
τ(K) = Zd in degree 0 where d = degl bA(K). More generally, this holds for all small and slim
knots which satisfy A.2.
From a practical standpoint, Corollary 6.3 does not help with computing HP∗
τ(K) unless one is
able to get a handle on the bA-polynomial of K. Unfortunately, there appears to be little in the way
of general computations of the bA-polynomial in the literature (but see [BC16] for the bA-polynomial
of certain Whitehead doubles). In contrast, the ordinary A-polynomial is known to be eﬀectively


## Page 28


28
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
computable, and has been computed for wide classes of examples. One can take advantage of these
computations in cases where the A- and bA-polynomial coincide. The class of slim knots turns out
to have this property, and provides a source of examples which will be discussed in Section 6.3.
6.2. The trefoil and ﬁgure-eight. For the trefoil and ﬁgure-eight knots, the SL(2, C)-character
variety is well-understood. We can therefore compute P •
τ (K) explicitly. The arguments of this
section are elementary and could potentially be pushed to other two-bridge knots, but they quickly
become tedious.
Let K = 31 ⊂S3 be a right-handed or left-handed trefoil. It follows from the above discussion
that K ⊂S3 satisﬁes A.1–A.2, for example because it is a two-bridge knot. According to [Por], the
character variety of K is given by the equations
(6.1)
X(Γ) = {(x, y) | (y −2)(x2 −y −1) = 0},
where {(y −2) = 0} is the component of reducible representations, and x is the trace of a meridian.
One can check by hand that B.1 and B.4 are always satisﬁed, and that B.2 is satisﬁed away from
the points (±
√
3, 2) which correspond to the intersection of the component of reducible represen-
tations {(y −2) = 0} with the component of irreducibles {x2 −y −1 = 0}. Using the fact that the
Alexander polynomial of the trefoil is ∆(t) = t2 −t + 1, one can check that these are precisely the
points ruled out by B.3.
In summary, the trefoil K ⊂S3 satisﬁes A.1–A.2 and τ ∈(−2, 2) satisﬁes B.1–B.4 provided that
τ ̸= ±
√
3. It follows from Theorem 5.17 that, for τ ∈(−2, 2) \ {−
√
3,
√
3}, we have HP∗
τ(K) = Zd
in degree 0, where d = degl bA(m, l).
To compute d, let χl : X(Γ) →C be the trace of the longitude of K. Observe that (x, y) 7→(x, χl)
restricts on X(Γ) ⊂C2 to an injective map which thus has degree 1. It follows that A(K) = bA(K).
Now A(K) is computed for instance in [CL96] and equals 1 + m6l or l + m6, depending on the
orientation. The l-degree is independent of the orientation, and we ﬁnd degl A(K) = 1. It follows
from Theorem 5.17 that HP∗
τ(K) = Z in degree zero, for τ ∈(−2, 2) \ {−
√
3,
√
3}.
Let us also consider what happens when τ = ±
√
3. We will show that X
√
3
irr (Γ) and X−
√
3
irr (Γ) are
empty. This implies that HP∗√
3(K) = HP∗
−
√
3(K) = 0 in all degrees.
To this end, note that Xτ
irr(Γ) is an open subvariety of the aﬃne variety Xτ(Γ), for any τ ∈C.
It is then a fact that Xτ
irr(Γ) must have a closed point if it is non-empty; see [Vak, 3.6.J.(a)]. It is
therefore enough to show that X
√
3
irr (Γ) and X−
√
3
irr (Γ) have no closed points.
Recall ﬁrst from Proposition 2.2 that closed points on Xτ
irr(Γ) for τ ∈C correspond to irre-
ducible representations with trace τ along the meridian. Recall also that the closed points of X(Γ)
correspond to completely reducible representations Γ →SL(2, C). Referring to (6.1), we see that
the lines {x =
√
3} and {x = −
√
3} intersect the character variety of the trefoil in a single point.
This means that the trefoil admits unique completely reducible representations having trace
√
3
and −
√
3 respectively along the meridian.
It’s easy to construct abelian representations having this property: just send a generator of
Z = Ab(Γ) to diag(eπi/6, e−πi/6) and diag(e5πi/6, e−5πi/6) respectively. Since abelian representations
are in particular completely reducible, it follows that there are no irreducible representations with
trace
√
3 and −
√
3 respectively along the meridian. Hence X
√
3
irr (Γ) and X−
√
3
irr (Γ) have no closed
points.
We conclude that, as advertised in the Introduction,
HP∗
τ(31) =
(
Z(0)
if τ ∈(−2, 2) \ {
√
3, −
√
3},
0
if τ ∈{
√
3, −
√
3}.
.
The ﬁgure-eight knot can be handled similarly. According to [Por], its character variety is
(6.2)
X(Γ) = {(x, y) | (y −2)(y2 −(x2 −1)y + x2 −1) = 0},


## Page 29


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
29
where {(y −2) = 0} is the component of reducible representations, and x is the trace of a meridian.
The ﬁgure-eight K = 41 satisﬁes A.1–A.2 for the same reasons as the trefoil. One can again
check by hand that B.1–B.4 are satisﬁed for all τ ∈(−2, 2) ( B.3 turns out to be vacuous for
the ﬁgure-eight knot). We again have A(K) = bA(K), and it is shown in [CL96] that A(K) =
l2m4 + l(−m8 + m6 + 2m4 + m2 −1) + m4. We conclude from Theorem 5.17 that
HP∗
τ(41) = Z2
(0),
for any τ ∈(−2, 2).
6.3. Computations for slim knots. Let K ⊂S3 be a slim knot. Thanks to a theorem of Dunﬁeld
[Dun99, Cor. 3.2], we know that the restriction map r : X(EK) →X(∂EK) which appears in the
deﬁnition of bA(K) has degree 1. This implies that A(K) = bA(K). As was noted previously, the
A-polynomial of a knot in S3 is eﬀectively computable. It follows that the bA-polynomial of a slim
knot is also eﬀectively computable.
In order to relate P •
τ (K) to bA(K), we need the character scheme of K to be reduced, i.e. K must
satisfy A.2. As we discussed in the paragraph preceding Corollary 6.3, this is not known in general
for slim knots. However, A.2 is known for all twist knots (since they are two-bridge knots) and for
all (−2, 3, 2n + 1) pretzel knots where n ∈Z [LT15]. This provides a reasonably large source of
examples for which we can compute HP∗
τ(K) for generic values of τ.
Example 6.4. Consider the twist knots Km with m ̸= 0 full twists and one clasp, as in [Mat14]. In
the Rolfsen knot table, the ﬁrst twist knots are K1 = 31 (trefoil), K−1 = 41 (ﬁgure-eight), K2 = 52,
K−2 = 61 (stevedore), K3 = 72, K−3 = 81. Except for the trefoil, they are all hyperbolic and
hence slim. Their A-polynomials can all be found in the appendix of [CCG+94]. One ﬁnds that,
for generic τ,
HP∗
τ(52) = Z3
(0), HP∗
τ(61) = Z4
(0), HP∗
τ(72) = Z5
(0), HP∗
τ(81) = Z6
(0).
(We warn the reader that the deﬁnition of the A-polynomial in [CCG+94] includes a factor of (l−2)
corresponding to the component of irreducibles, which shifts the degree by 1).
In fact, the A-polynomial of all twists knots has been computed explicitly, and is presented in
a closed form in [Mat14]. One can verify using [Mat14] that the l-degree of the A-polynomial is
always 2 less than the crossing number, which explains the pattern in the above examples. (We
will see in Example 6.5 that this pattern is special to twist knots.) Thus, for general twist knots
and generic τ, we have
HP∗
τ(Kn) =
(
Z2n−1
(0)
if n > 0,
Z−2n
(0)
if n < 0.
A diﬀerent class of examples for which we can explicitly determine HP∗
τ(K) are certain hyperbolic
pretzel knots. As was mentioned previously, Mattman [Mat00] showed that the (−2, 3, m) pretzel
knots is slim provided that it is hyperbolic (which happens if and only if m /∈{1, 3, 5}) and that
m is not divisible by 3. Moreover, Le and Tran showed that the character variety is reduced for
all (−2, 3, 2n + 1) pretzel knots where n ∈Z [LT15]. Finally, in [GM11] the authors identify a
recursion relation which allows one to compute A(−2, 3, 2n + 1) for n ∈Z.
Putting these results together, it follows that one can in principle compute HP∗
τ(P(−2, 3, 2n+1))
provided that n /∈{0, 1, 2} and that 2n + 1 is not divisible by 3. We refer the reader to [GM11] for
the precise recursion relation, and limit ourselves to the following example.
Example 6.5. The pretzel knot (−2, 3, 7), also known as the Fintushel-Stern knot, has crossing
number 12. As we remarked in Section 6.1, (−2, 3, 7) is not a small knot, since its complement


## Page 30


30
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
contains an incompressible genus 2 surface. It is shown in [GM11] that A(−2, 3, 7) = −1 + lm8 −
2lm10 + 2lm20 + l2m22 −l4m4 −2l4m42 −l5m50 + 2l5m52 −l5m54 + l6m62. It follows that
HP∗
τ(P(−2, 3, 7)) = Z6
(0),
for all but ﬁnitely many values of τ ∈(−2, 2).
7. Connected sums of knots
In this section, we consider a class of knots whose SL(2, C)-character variety has 2-dimensional
components. A knot K in this class can be constructed as the connected sum of two knots satisfying
A.1 and A.2 in Section 5.2. Under certain assumptions on τ ∈(−2, 2) which are satisﬁed generically,
we will show that HP∗
τ(K) is supported in degrees −1 and 0 and compute it explicitly for some
examples.
7.1. Topological preliminaries. For the purpose of ﬁxing some notation, we begin by brieﬂy
reviewing how to form the connected sum of two knots.
Let K1 ⊂Y1 and K2 ⊂Y2 be oriented knots, where Y1, Y2 are homology 3-spheres. Choose em-
bedded closed balls B1 ⊂Y1, B2 ⊂Y2 such that Bi −Ki is diﬀeomorphic to {(x, y, z) | ∥(x, y, z)∥≤
1, (x, y, z) ̸= (x, 0, 0)}. Let Bi ⊂Bi be the (open) interior. Let Ci := ∂(Yi −Bi) and observe that
Ci ∩Ki is a disjoint union of two points, which are canonically ordered by the orientation on Ki.
Let φ : C1 →C2 be a diﬀeomorphism which maps C1 ∩K1 to C2 ∩K2 and preserves the ordering.
Deﬁnition 7.1. We say that K1#K2 := (K1 −B1) ∪φ (K2 −B2) is the connected sum of K1 and
K2. Note that K1#K2 is a knot in Y1#Y2 := (Y1 −B1) ∪φ (Y2 −B2). It can be shown that the
connected sum is well-deﬁned up to equivalence of knots, even though the construction depends a
priori on many choices.
A knot in S3 which is the connected sum of two nontrivial knots is often said to be a composite
knot. Two well-known examples of composite knots are the granny knot and the square knot, which
are respectively the connected sum of two trefoils with the same and opposite orientations.
The fundamental group of K1#K2 can be easily computed using van Kampen’s theorem. Writing
K := K1#K2 and Y = Y1#Y2, we have
π1(Y −K) = π1(Y1 −K1 −B1) ∗π1(S2−p1−p2) π1(Y2 −K2 −B2)
(7.1)
= π1(Y1 −K1) ∗π1(S2−p1−p2) π1(Y2 −K2).
Here {p1, p2} = C1 ∩K1 ≡φ C2 ∩K2, where the ordering is inherited from the orientation of
K1, K2. The fundamental groups considered in (7.1) are assumed to be deﬁned with respect to
some ﬁxed basepoint x0 ∈S2 −p1 −p2. We do not keep track of this choice in our notation since
it plays no role in this section.
For future reference, we let ιi : π1(Yi −Ki) →π1(Y −K) be the natural maps associated to the
amalgamated product. Note that the fundamental group of K = K1#K2 is independent of the
choice of orientations of K1 and K2.
We will rely throughout this section on deﬁnitions and notation introduced in Section 2.1. How-
ever, we deviate from the notation of the previous sections in one important way: namely, given
a knot K ⊂Y , we will let R(Y −K) and X (Y −K) denote the representation and character
schemes of π1(Y −K) with respect to an unspeciﬁed basepoint x0. We follow the analogous nota-
tional convention for the representation and character varieties, and for their relative counterparts.
There is an inconsistency in the fact that we are now considering representation and character
varieties of knot complements: in Sections 5 and Section 6, we always considered representation
and character varieties associated to the blowup EK of a doubly-pointed pointed knot (Y, K, p, q).
The reason for this change is that it allows us to avoid considering blowups of connected sums. Of
course, the fundamental group of a blowup is isomorphic to that of the knot complement, so one
can always pass between these choices (in a non-canonical way).


## Page 31


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
31
7.2. Some assumptions. We will now restrict our attention to knots in integral homology spheres
satisfying some additional assumptions.
As in Section 5.2, it will be convenient to label these
assumptions separately.
Let Y be an integral homology sphere and let K ⊂Y be a knot. Let τ ∈(−2, 2) be a real
parameter. We consider the following assumptions on this data.
Assumption C.1. The irreducible locus of the relative character scheme X τ
irr(Y −K) is smooth.
Assumption C.2. The irreducible locus of the relative character scheme X τ
irr(Y −K) is zero-
dimensional.
Assumption C.3. If x ∈[0, 1] has the property that e4πix is a root of the Alexander polynomial
of K ⊂Y , then τ ̸= 2 cos(2πx).
Note that C.1–C.3 depend both on the topological data K ⊂Y and on τ ∈(−2, 2). Moreover
C.1–C.3 are closely related to the assumptions introduced in Section 5.2. In fact, C.3 is essentially
identical to B.3, while we will show in Section 7.6 that the knot K ⊂Y satisﬁes C.1–C.3 for all but
ﬁnitely many τ ∈(−2, 2) provided that it satisﬁes A.1 and A.2.
It will be useful to introduce the following deﬁnition.
Deﬁnition 7.2. Given a ﬁnitely-presented group Γ, a representation Γ →SL(2, C) is said to be
diagonal if it can be conjugated to have image consisting only of diagonal matrices.
Diagonal
representations are in particular reducible.
Let us now state an important proposition which will be used throughout this section.
Proposition 7.3. For i = 1, 2 let Ki ⊂Yi be a knot in an integral homology sphere. Let K =
K1#K2 ⊂Y = Y1#Y2 and suppose that τ ∈(−2, 2) satisﬁes C.3 with respect to K1 ⊂Y1 and
K2 ⊂Y2. Then any irreducible representation of π1(Y −K) into SL(2, C) must pull back to an
irreducible representation along ι1 or ι2 (or both).
This proposition justiﬁes the following deﬁnition.
Deﬁnition 7.4. For i = 1, 2, let Ki ⊂Yi be as in Deﬁnition 7.4. The representations π1(Y −K) →
SL(2, C) which pull back to an irreducible representation along ιi and to a reducible representation
along ιj for i ̸= j with i, j ∈{1, 2} are said to be of Type I. The representations which pull back to
an irreducible representation along both factors are said to be of Type II.
Proof of Proposition 7.3. We need to check that ρ is reducible if ρ ◦ιi is reducible for i = 1, 2. To
this end, it is useful to note that if ρ ◦ιi is reducible, then it is abelian. This is a consequence of
[CCG+94, Prop. 6.1] and the fact that τ ∈(−2, 2) satisﬁes C.3 for Ki ⊂Yi. It then follows from
the classiﬁcation of SL(2, C) representations in [AM, Sec. 2.1] that ρ ◦ιi is in fact diagonal since
τ ̸= ±2. It is therefore enough to check that the fact that ρ ◦ιi are diagonal for i = 1, 2 implies
that ρ is diagonal.
Let us then suppose that x ∈π1(S2 −p1 −p2) is a generator. Viewing x as an element of both
π1(Y1 −K1) and π1(Y2 −K2), note that ρ ◦ι1(x) = ρ ◦ι2(x). If we assume that ρ ◦ι1 is diagonal,
then there is an element g ∈SL(2, C) such that gρι1(x)g−1 = diag(l, l−1) for some l ∈C∗, where
l ̸= ±1. It now follows from Lemma 7.5 below that in fact ρ◦ι1 and ρ◦ι2 are in fact simultaneously
diagonalized by g. Since the image of the ιi generates π1(Y −K), we conclude that g diagonalizes
ρ.
□
Lemma 7.5. Let Γ be a ﬁnitely-generated group and let σ : Γ →SL(2, C) be a diagonal repre-
sentation. Suppose that there exists an element h ∈Γ with σ(h) = diag(l, l−1) for l ̸= ±1. Then
Im σ ⊂{diag(z, z−1) | z ∈C∗}, i.e. σ is diagonal.


## Page 32


32
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
Proof. By hypothesis, there exists M ∈SL(2, C) such that MσM−1 is diagonal. In particular, this
means that Mσ(h)M−1 = M diag(l, l−1)M−1 is diagonal. One can check that this implies that
either M = D for D ∈{diag(l, l−1) | l ∈C∗} or M = JD for J =

0
−1
1
0

and D ∈{diag(l, l−1) |
l ∈C∗}.
The conclusion now follows from the fact – which is also straightforward to verify – that conju-
gation by D or JD cannot send a non-diagonal matrix to a diagonal matrix.
□
7.3. Analysis of the character variety. According to Lemma 2.5, the isomorphism (7.1) gives
rise to a ﬁber product of relative representation schemes
(7.2)
Rτ(Y −K) = Rτ(Y1 −K1) ×Rτ (S2−p1−p2) Rτ(Y2 −K2).
Let πi : Rτ(Yi −Ki) →Rτ(S2 −p1 −p2) be the maps associated to the ﬁber product. Observe
that the πi are compatible with the usual conjugation action of the algebraic group SL2.
By a slight abuse of notation, we also let πi : Rτ(Yi−Ki) →Rτ(S2−p1−p2) be the corresponding
maps on character varieties. Observe that πi maps a representation ρ to its restriction to π1(S2 −
p1 −p2). The conjugation action of SL(2, C) is compatible with πi. Since {± Id} acts trivially, it
descends to an action of PSL(2, C).
Given ρ : π1(Yi −Ki) →SL(2, C) for some i = 1, 2, let Rτ(Yi −Ki)ρ be the connected component
of ρ in Rτ(Yi −Ki) and let πi|ρ be the restriction of πi to Rτ(Yi −Ki)ρ.
The next two propositions give a more precise description of πi|ρ in the case where ρ is reducible
and irreducible respectively. Eventually, we wish to consider a certain ﬁber product over Rτ(S2 −
p1 −p2) and to show that it forms a smooth scheme; see Proposition 7.8. In ordinary diﬀerential
topology, one often veriﬁes that a ﬁber product is smooth by showing that the maps from each
factor onto the base are submersions. The scheme theoretic analog of a submersion is a smooth
morphism.
We will need to make use of this notion which unfortunately requires a signiﬁcant
amount of scheme theory to deﬁne; see [Har77, III. Chap. 10]. However, we will mostly use it as
a black box by appealing to general results which allow one to promote ordinary submersions on
closed points to smooth morphisms of schemes.
Proposition 7.6. For i = 1, 2, suppose that Ki ⊂Yi and τ ∈(−2, 2) satisfy C.3. If ρ ∈Rτ(Yi−Ki)
is a reducible representation, then πi|ρ : Rτ(Yi−Ki)ρ →Rτ(S2−p1−p2) is an isomorphism. More-
over, Rτ(Yi −Ki)ρ is the unique component of Rτ(Yi −Ki) containing a reducible representation.
Proof. We saw in the proof of Proposition 7.3 that all reducible SL(2, C) representations of π1(Yi −
Ki) are in fact abelian. Since any abelian representation factors through H1(Yi −K1) = Z, this
implies that all such representations are conjugate. Hence they belong to the same component of
Rτ(Yi −Ki).
One can check by hand that
Rτ(S2 −p1 −p2) = Rτ(Z) ≃PSL(2, C)/C∗≃TS2
is smooth as a scheme provided that τ ̸= ±2.
Since Rτ(Yi −Ki)ρ is a component of abelian
representations, one can show that Rτ(Yi −Ki) = Rτ(Z) which implies that Rτ(Yi −Ki) is also
smooth.
We previously observed that the map of representation varieties πi|ρ : Rτ(Yi −Ki)ρ →Rτ(S2 −
p1 −p2) is compatible with the conjugation action of PSL(2, C). This action is evidently transitive
on Rτ(S2 −p1 −p2), from which it follows that πj|ρ is surjective at the level of closed points and
of tangent spaces. This can be shown to imply (see [Har77, III, Prop. 10.4]) that πi is a smooth
morphism of schemes.
□
Proposition 7.7. For i = 1, 2, suppose that Ki ⊂Yi and τ ∈(−2, 2) satisfy C.1 and C.3. If
ρ ∈Rτ(Yi −Ki) is irreducible, then πi|ρ : Rτ(Yi −Ki)ρ →Rτ(S2 −p1 −p2) is a smooth morphism
of schemes.


## Page 33


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
33
Proof. It follows by combining C.1 with Proposition 2.13 that Rτ(Yi −Ki)ρ is a smooth scheme.
We saw in the proof of the previous proposition that Rτ(S2−p1−p2) is a smooth scheme. We again
observe that the map πi|ρ : Rτ(Yi −Ki)ρ →Rτ(S2 −p1 −p2) is compatible with the conjugation
action of PSL(2, C), and that πj|ρ is surjective at the level of closed points and of tangent spaces.
Using again [Har77, III, Prop. 10.4], this implies that πi|ρ is a smooth morphism of schemes.
□
Proposition 7.8. For i = 1, 2, suppose that Ki ⊂Yi and τ ∈(−2, 2) satisfy C.1 and C.3. Then
X τ
irr(K1#K2) is smooth as a scheme. Moreover, each connected component consists exclusively or
Type I or Type II representations.
Proof. It follows by combining Proposition 7.3 and Equation (7.2) that each connected component
of Rτ
irr(K1#K2) consists exclusively of Type I or Type II representations. It follows that the same
is true for the connected components of Xτ
irr(K1#K2), which is the quotient of Rτ
irr(K1#K2) by a
free PSL(2, C) action.
We saw in Propositions 7.6 and 7.7 that πi restricts to a smooth morphism of schemes on
Rτ(Yi −Ki). It is a general fact that the property of being a smooth morphism is closed under
ﬁber products and composition; see [Har77, III, Prop. 10.1]. Appealing again to (7.2), this implies
in particular that the composition Rτ
irr(Y −K) →Rτ(S2−p1−p2) →Spec C is a smooth morphism
of schemes, which means that Rτ
irr(Y −K) is a smooth scheme. Appealing to Proposition 2.13,
this implies that X τ
irr(Y −K) is also a smooth scheme.
□
We record the following lemma, which follows immediately from (7.2).
Lemma 7.9. Assuming that Ki ⊂Yi and τ ∈(−2, 2) satisfy C.1 and C.3 for i = 1, 2, the locus of
Type I components of Xτ
irr(K1#K2) is topologically the disjoint union of Xτ
irr(K1) and Xτ
irr(K2).
We obtain the following corollary by combining Proposition 7.8 with Proposition 4.3.
Corollary 7.10. Under the hypotheses of Proposition 7.8, the perverse sheaf P •
τ (K) is a local
system. Its stalks over every k-dimensional component are isomorphic to Z, supported in degree
−k.
We now specialize to knots which satisfy C.2 in addition to C.1 and C.3. Given τ ∈(−2, 2), if
Ki ⊂Yi is a knot in an integral homology sphere which satisﬁes C.2, it makes sense to let mi ∈N
be the number of components of Xτ
irr(Yi −Ki). We now have the useful following proposition.
Proposition 7.11. For i = 1, 2, suppose that Ki ⊂Yi and τ ∈(−2, 2) satisfy C.1–C.3. If ρ ∈
Rτ(Yi −Ki) is irreducible, then Rτ(Yi −Ki)ρ is a C∗-bundle over Rτ(S2 −p1 −p2) ≃PSL(2, C)/C∗.
Proof. We showed in Proposition 7.8 that πi|ρ : Rτ(Yi −Ki)ρ →Rτ(S2 −p1 −p2) is a smooth
morphism of schemes if ρ ∈Rτ(Yi −Ki) is irreducible.
The discussion preceding the proof of
Proposition 2.10 (2) also implies that Rτ(Yi −Ki)ρ is a PSL(2, C)-bundle over the point [ρ] ∈
Xτ
irr(Yi −Ki).
Let us now show that πi|ρ : Rτ(Yi −Ki)ρ →Rτ(S2 −p1 −p2) is a C∗-bundle.
Given any
σ ∈Rτ(Yi −Ki)ρ, we will show that the ﬁber over πi|ρ(σ) is a copy of C∗. Let µ ∈π1(S2 −p1 −p2)
be a generator.
After possibly conjugating by an element of SL(2, C), we may as well assume
that σ(µ) is diagonal.
Since SL(2, C) acts transitively on Rτ(Yi −Ki)ρ, the ﬁber over πi|ρ(σ)
can be identiﬁed with the orbit of σ under the action of Stab(σ(µ)). But since σ(µ) is diagonal
and Tr σ(µ) ̸= ±2, one can check that Stab(σ(µ)) = {diag(l, l−1) | l ∈C∗}. Finally, since the
kernel of the SL(2, C)-action is precisely {± Id}, it follows that the orbit of σ under Stab(σ(µ)) is
C∗/{± Id} = C∗.
□
If we continue to assume that Ki ⊂Yi and τ ∈(−2, 2) satisfy C.1–C.3, we can precisely describe
Xτ
irr(Y −K) ⊂Xτ(Y −K).
Indeed, (7.2) implies that we can think of a representation ρ :
π1(Y −K) →SL(2, C) as a pair (ρ1, ρ2) where ρi : π1(Yi −Ki) →SL(2, C) and where the ρi restrict


## Page 34


34
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
to the same representation on π1(S2 −p1 −p2). One then counts that there are precisely m1 Type
I components of Rτ(Y −K) which restrict to an abelian representation on the ﬁrst factor, and m2
Type I components which restrict to an abelian representation on the second factor. Observe that
each such component is topologically a copy of PSL(2, C). Recalling that PSL(2, C) acts transitively
on Rτ
irr(Y −K) by conjugation, we ﬁnd that the locus of Type I components of Xτ
irr(Y −K) is a
disjoint union of m1 + m2 isolated points.
Similarly, one counts m1m2 Type II components of Rτ
irr(Y −K). These form C∗× C∗bundles
over Rτ(S2 −p1 −p2) ≃PSL(2, C)/C∗. The PSL(2, C) conjugation action is free and transitive
and one ﬁnds that the image of each component in the character variety is a copy of C∗. We
summarize the previous discussion with the following corollary, which also relies on Proposition 7.8
and Corollary 7.10.
Corollary 7.12. Suppose that Ki ⊂Yi and τ ∈(−2, 2) satisfy C.1–C.3 for i = 1, 2, and let mi ∈N
be deﬁned as above. Then the irreducible locus X τ
irr(Y −K) is a smooth scheme. Topologically, it
is a disjoint union of m1 + m2 points corresponding to Type I representations, and m1m2 copies
of C∗corresponding to Type II representations. The restriction of the perverse sheaf P •
τ (K) to any
k-dimensional component is a local system whose stalks are isomorphic to Z, in degree −k.
7.4. Local systems. We now wish to strengthen Corollary 7.12 by showing that the local system
P •
τ (K) is in fact trivial. It is evidently enough to consider the Type II components of Xτ
irr(Y −K)
which are diﬀeomorphic to C∗. Let C be such a component.
Recall from Section 3.1 that a Heegaard splitting H = (Σ, U0, U1) induces inclusions Xτ
irr(Ui) →
Xτ
irr(Σ). These inclusions are Lagrangian with respect to the natural symplectic form on Xτ
irr(Σ)
and we therefore write Xτ
irr(Ui) := Li. We showed in Section 3.6 that the Li carry unique spin
structures provided that the genus of Σ is at least 6, which we can always assume. We can then
identify C with a component of L0 ∩L1.
In order to show that P •
τ (K) is a trivial local system on C, we will appeal to Lemma 6.3 of [AM]
and to the discussion preceding this lemma. The main objects under consideration are a certain
local system |W +| on C and a map
(7.3)
TL0|C →TL1|C.
Here (7.3) corresponds to (29) in [AM], which is described in the paragraphs preceding the statement
of Lemma 6.3 in [AM].
In our particular setting, Lemma 6.3 of [AM] says that
P •
τ (K)|C ≃|W +|[1],
provided that the map (7.3) preserves spin structures.
Our ﬁrst task in the remainder of this
section is to show that (7.3) does indeed preserve spin structures. Then, we will describe |W +|
more carefully and argue that it is a trivial local system.
We begin by introducing a Heegaard splitting which is well adapted to our setting. Unlike in
Section 3, we will consider Heegaard splittings for knot complements rather than knot exteriors.
Since these have isomorphic homotopy groups, the distinction is immaterial for our present purposes
– indeed, we only needed to emphasize this distinction in Section 3 for the purpose of proving the
naturality of our invariant.
Let (Σ, p, q, U0, U1) be a Heegaard splitting of genus at least 3 for Y1 −K1 where p, q ∈K are
marked points on Σ. Similarly, let (Σ′, p′, q′, U ′
0, U ′
1) be a Heegaard splitting for Y2 −K2 of genus
at least 3.
We get a Heegaard splitting (of genus at least 6) for (Y1#Y2)−(K#K′) = Y −K = by identifying
disks around q and p′:
(Σ#Σ′, p, q′, U0#bU ′
0, U1#bU ′
1),
where #b denotes the boundary connected sum.


## Page 35


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
35
Let G = SL(2, C) and let Cτ ⊂G be the conjugacy class of elements of trace τ. The relative
character variety of the Heegaard surface used for K1 can be described as
Xτ(Σ) = {(A1, . . . , Ag, B1, . . . , Bg, C1, C2) ∈G2g+2 | C1, C2 ∈Cτ,
Y
[Ai, Bi]C1C2 = 1}/G
= {(A1, . . . , Ag, B1, . . . , Bg, C1) ∈G2g+1 | C1 ∈Cτ,
Y
[Ai, Bi]C1 = diag(t, t−1)}/C∗,
where t + t−1 = τ. We have a similar description for K2:
Xτ(Σ′) = {(A′
1, . . . , A′
h, B′
1, . . . , B′
h, C′
2) ∈G2h+1, | C′
2 ∈Cτ,
Y
[A′
i, B′
i]C′
2 = diag(t, t−1)}/C∗.
For the connected sum, we have
Xτ(Σ#Σ′) = {(A1, . . . , Ag, B1, . . . , Bg, C1, A′
1, . . . , A′
h, B′
1, . . . , B′
h, C′
2) ∈G2g+2h+2 | C1, C′
2 ∈Cτ,
Y
[Ai, Bi]C1 =
Y
[A′
i, B′
i]C′
2}/G
Note that Xτ(Σ) × Xτ(Σ′) lives inside Xτ(Σ#Σ′) as a complex codimension one subset, given
by asking that the holonomy around the curve where we do the connect sum, Q[Ai, Bi]C1 =
Q[A′
i, B′
i]C′
2, has trace τ.
Consider a neighborhood V of this subset where the same holonomy has trace contained in the
interval (τ −ǫ, τ + ǫ) ⊂(−2, 2), for some ǫ > 0 suitably small. There, we can assume
(7.4)
Y
[Ai, Bi]C1 =
Y
[A′
i, B′
i]C′
2 = diag(u, u−1),
and divide by the residual action of C∗instead of G. Note that (7.4) involves making a choice,
since we could also have conjugated the above expression to diag(u−1, u). The C∗action depends
on this choice. However, if ǫ is small enough, then this choice can be made consistently and one
can then verify that the resulting C∗action is holomorphic; cf. [Gol04].
Furthermore, there is a C∗action on V given by simultaneous conjugation on A1, . . . , Ag,
B1, . . . , Bg, C1, and leaving A′
1, . . . , A′
h, B′
1, . . . , B′
h, C′
2 unchanged. Let us call this action ϕ. Note
that ϕ preserves the Lagrangians L0, L1, but the action ϕ on the Li is not free. However, we will
exhibit open subsets L0
i ⊂Li on which the action is free, and such that L0
0 ∩L0
1 is precisely the
sub-locus of L0 ∩L1 consisting of Type II representations.
Without loss of generality, by a suitable choice of the generators for π1 of the surfaces under
consideration, we can assume that L0 is given by the equations
B1 = · · · = Bg = B′
1 = · · · = B′
h = I.
Then, the closure of L0 inside Xτ(Σ) is the set
L0 = {(A1, . . . , Ag, A′
1, . . . , A′
h, C1, C′
2) ∈G2g+2 | C1 = C′
2 ∈Cτ}/G
= {(A1, . . . , Ag, A′
1, . . . , A′
h, C) ∈G2g+1 | C = diag(u, u−1)}/C∗
=
 {(A1, . . . , Ag, A′
1, . . . , A′
h) ∈G2g}/C∗
× diag(u, u−1),
where u + u−1 = τ and the C∗action is by conjugation of the {Ai, A′
i}i.
Consider now the restriction of ϕ to L0, which conjugates the Ai while keeping the A′
i ﬁxed.
Since both C∗actions commute, we have
L0/C∗=
 ({(A1, . . . , Ag, A′
1, . . . , A′
g) ∈G2g}/C∗) × diag(u, u−1)}

/C∗
=

(A1, . . . , Ag) ∈Gg	
/C∗×

(A′
1, . . . , A′
g) ∈Gg	
/C∗× diag(u, u−1)
=

(A1, . . . , Ag) ∈Gg	
/C∗×

(A′
1, . . . , A′
g) ∈Gg	
/C∗.
Let X1
irr ⊂{(A1, . . . , Ag) ∈Gg}/C∗be the open locus of representations such that (A1, . . . , Ag,
diag(u, u−1)) is irreducible and let X2
irr ⊂{(A′
1, . . . , A′
g) ∈Gg}/C∗be deﬁned analogously. Let L0
0
be the preimage of X1
irr × X2
irr under the quotient map L0 →L0/C∗.


## Page 36


36
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
Lemma 7.13. The inclusion L0
0 ⊂L0 has codimension at least 4.
Proof. Let R1 ⊂L0 be the set of representations such that (A1, . . . , Ag, diag(u, u−1)) is reducible
and such that (A′
1, . . . , A′
g, diag(u, u−1)) is irreducible. Let R2 ⊂L be deﬁned analogously. Finally,
let R12 be the set of representations such that (A1, . . . , Ag, diag(u, u−1)) and (A′
1, . . . , A′
g, diag(u, u−1))
are both reducible.
By an argument as in [AM, Lem. 2.6], we see that R1 has dimension at most (2g+1)+3g = 5g+1.
Similarly, R2 has dimension at most 5g + 1, while R12 has dimension at most (2g + 1) + (2g + 1) =
4g + 2. Since L0 has dimension 6g −1, we conclude that the codimension is at least g −2. Since
we are working with a Heegaard splitting of genus at least 6, the lemma follows.
□
Lemma 7.14. The manifold X1
irr × X2
irr ≃L0
0/C∗admits a unique spin structure.
Proof. Observe that the Xi
irr coincide with the varieties Xτ
irr(Ui) considered in Section 3.6 (note
that the Ui occurring in Section 3.6 are diﬀerent from the Ui considered in this section). Having
made this observation, the existence of spin structure follows from Proposition 3.14. The uniqueness
follows from the proof of Proposition 3.14, which shows that the Xi
irr are simply-connected.
□
The above discussion goes through for L1 in place of L0. Note that, if we assume that L0 is given
by setting Bi and B′
i to the identity, we do not have a simple expression for L1 in terms of the
chosen matrices. However, by choosing diﬀerent sets of generators for fundamental groups, we can
put L1 in the same form as we did for L0 (at the expense of putting L0 in a complicated form). The
actions of C∗are independent of these choices of generators, so we can construct a subset L0
1 ⊂L1
by the same procedure as above.
Examining the deﬁnition of L0
i ⊂Li, we see that L0
0 ∩L0
1 ⊂L0 ∩L1 is precisely the sub-locus of
Type II representations. Hence C is a connected component of L0
0 ∩L0
1 and the action preserves C
since it is continuous.
Remark 7.15. Although we have been assuming throughout Section 7.4 that τ ∈(−2, 2) and Ki ⊂Yi
satisfy C.1–C.3, we did not use C.2 in constructing the C∗action ϕ.
The next proposition relies crucially on the fact that the knots Ki ⊂Yi satisfy C.2.
Proposition 7.16. The action of ϕ on C is transitive.
Proof. It will be helpful to consider an alternative description of ϕ in the spirit of Corollary 7.12.
Recall that C is the quotient of a Type II component ˜C ⊂Rτ
irr(K −Y ) by a transitive SL(2, C)-
action. Now ˜C is a C∗× C∗bundle over Rτ(S2 −q −p′) ≃SL(2, C)/C∗. Let m ∈π1(S2 −q −p′)
be a generator and let σ ∈Rτ(S2 −q −p′) be the unique representation with the property that
σ(µ) = diag(u, u−1).
The elements of ˜C are pairs (ρ1, ρ2) of irreducible representations of π1(Y1 −K1) and π2(Y2 −K2)
respectively, which agree on the generator µ ∈π1(S2 −q −p′). By conjugating, we can ensure that
ρ(µ) = ρ′(µ) = σ(µ) = diag(u, u−1). This has the eﬀect of identifying all of the ﬁbers with the ﬁber
Fσ over σ ∈Rτ(S2 −q −p′). This is precisely what we did in (7.4).
The stabilizer of diag(u, u−1) is isomorphic to C∗, and the quotient of Fσ by the residual C∗
action is then precisely C ⊂Xτ(Y −K).
However, we can also acts by conjugation on either
factor of Fσ = C∗× C∗while leaving the other factor ﬁxed. One of these actions is ϕ, while the
other corresponds to acting by simultaneous conjugation on A′
1, . . . , A′
h, B1, . . . , B′
h, C′
2 while leaving
A1, . . . , Ag, B1, . . . , Bg, C1 unchanged. It follows from this description that ϕ acts transitively on
C = Fσ/C∗.
□
Putting together the previous results, we arrive at the following corollary.
Corollary 7.17. The map (7.3) preserves spin structures.


## Page 37


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
37
Proof. Consider the projections πi : L0
i →L0
i /C∗. We note that TL0
i = π∗
i (L0
i /C∗) ⊕R2, where
R2 is viewed as the Lie algebra of C∗. According to Lemma 7.14 applied to both L0
0 and L0
1, the
quotients L0
i /C∗admit a unique spin structure which we call si for concreteness. We can then
endow TL0
i with a spin structure Si, which is the direct sum of π∗
i (si) and the trivial spin structure
on the trivial R2-bundle.
According to Lemma 7.13 applied to L0 and L1, the inclusion L0
i ⊂Li has complex codimension
g −2. Since Σ has genus at least 6, the inclusion induces an isomorphism on fundamental groups.
It follows that the L0
i are simply-connected since the Li are simply-connected. Hence the spin
structure Si coincides with the restriction of the spin structure coming from Li. In particular, it is
enough to prove that (7.3) takes S0|C to S1|C.
According to Proposition 7.16, the C∗action is transitive on C ⊂L0
0 ∪L0
1. This means that (7.3)
is the pullback of a map
(7.5)
(TL0
0)[ρ] →(TL0
1)[ρ],
where [ρ] ∈L0
0/C∗∩L0
1/C∗. But (7.5) necessarily maps s0[ρ] →s1[ρ] since spin structures are unique
over a point. By deﬁnition of the Si, it follows that (7.3) sends S0|C to S1|C since both (7.3) and
the Si are obtained from a pullback.
□
Having shown that (7.3) preserves spin structures, it remains to argue that |W +| is a trivial local
system. To prove this, we will appeal to similar considerations as in the proof of Corollary 7.17
and that of Lemma 8.3 in [AM].
For i = 1, 2, let NiC ⊂TL0
i |C be the normal bundle associated to the inclusion C ⊂L0
i . Let TC⊥
be the symplectic orthogonal complement to TC ⊂TXτ
irr(Σ)|C. As argued in [AM, Sec. 6], there is
a natural isomorphism from the direct sum N0C ⊕N1C to the symplectic normal bundle TC⊥/TC.
In particular, N0C ⊕N1C is a symplectic vector bundle and the NiC are transverse Lagrangian
sub-bundles.
A polarization of N0C ⊕N1C can be thought of as a Lagrangian sub-bundle which is ﬁberwise
transverse to both summands. As explained in [AM, Sec. 6], a choice of such a polarization allows
one to view N1C as a sub-bundle of N0C ⊕N ∗
0 C, which can be described by the graph of a quadratic
form q on N0C. The bundle |W +| ⊂N0Q is a maximal sub-bundle on which the real part of q is
positive, which depends only on q up to isomorphism; see [AM, Sec. 6].
As in the proof of Corollary 7.17, one notes that the NiC are equivariant under the C∗action
ϕ, in the sense that they are isomorphic to pullbacks of vector bundles over a point [ρ] ∈L0
0/C∗∩
L0
1/C∗. As argued in the proof of Lemma 8.3 in [AM], we can therefore construct a C∗-equivariant
polarization of N0C ⊕N1C, simply by pulling back a polarization over ρ. We then ﬁnd that q has
constant coeﬃcients with respect to a C∗-equivariant trivialization of N0C, which implies that |W +|
is trivial.
We conclude that P •
τ (K) is a trivial local system. Along with Corollary 7.10, this implies the
following result.
Theorem 7.18. Suppose that C.1–C.3 are satisﬁed. Then P •
τ (K) is a trivial local system supported
on m1 +m2 isolated points and m1m2 copies of C∗. It follows that HP−1
τ (K) = Zm1m2, HP0
τ(K) =
Zm1+m2+m1m2 and HPk
τ(K) = 0 for all k /∈{−1, 0}.
7.5. Euler characteristics. We now discuss the behavior of the Euler characteristic of HP∗
τ(K),
the SL(2, C) Casson-Lin invariant χτ(K) deﬁned in the Introduction. In this section we assume
that the knots Ki satisfy C.1 and C.3, but they do not have to satisfy C.2. The following theorem
asserts that the SL(2, C) Casson-Lin invariant is additive for such knots.
Theorem 7.19. For i = 1, 2, suppose that Ki ⊂Yi and τ ∈(−2, 2) satisfy C.1 and C.3. Then
χτ(K1#K2) = χτ(K1) + χτ(K2).


## Page 38


38
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
Proof. According to Proposition 7.8, X τ
irr(K1#K2) is smooth as a scheme. By Proposition 4.3, it
follows that our perverse sheaf is a rank one local system on Xτ
irr(K1#K2). On each component C
of Xτ
irr(K1#K2) of complex dimension k, this local system is supported in degree −k. Note that the
Euler characteristic of a cochain complex with twisted coeﬃcients in a local system depends only
on the rank, and not on the twisting. Thus, the contribution to χτ(K1#K2) from the component
C equals (−1)k times the topological Euler characteristic of C.
Since the Ki satisfy C.1, the
same argument shows that χτ(Ki) is a signed count of the topological Euler characteristics of the
components of Xτ
irr(Ki).
Proposition 7.8 shows that Xτ
irr(K1#K2) consists exclusively of Type I and Type II components.
According to Lemma 7.9, the locus of Type I components is topologically the disjoint union of
Xτ
irr(K1) and Xτ
irr(K2).
The theorem now follows from the fact that the Type II components of Xτ
irr(K1#K2) have
vanishing topological Euler characteristic.
This is a consequence of the fact that the Type II
components admit a free C∗action, and are therefore C∗-bundles which always have trivial Euler
characteristic; cf. Section 7.4 and Remark 7.15.
□
By repeatedly applying Theorem 7.19, we can in fact compute the Euler characteristic of arbitrary
connected sums of knots.
Corollary 7.20. For j ∈{1, 2, . . . , n}, let Kj ⊂Yj be a knot in an integral homology sphere.
Suppose that Kj ⊂Yj and τ ∈(−2, 2) satisfy C.1 and C.3. Then χτ(#n
j=1Kj) = Pn
j=1 χτ(Kj).
Proof. Using Proposition 7.8, one sees that the connected sum of two knots satisfying C.1 also
satisﬁes C.1. Similarly, the connected sum of two knots satisfying C.3 also satisﬁes C.3, since the
Alexander polynomial is multiplicative under connected sums. The corollary follows.
□
7.6. Some computations. The character varieties of the trefoil and ﬁgure-eight were described
in Theorem 7.18. For a trefoil K′ = 31 ⊂S3, one computes that
(7.6)
Xτ(S3 −K′) = {(x, y) | (y −2)(τ 2 −y −1) = 0}.
Away from the point τ = ±
√
3, this is a smooth, zero-dimensional scheme which thus satisﬁes C.1.
Using the fact that the Alexander polynomial of the trefoil is ∆(t) = t2 −t + 1, one can check that
these are precisely the points ruled out by C.3.
Let us write K = 31#31 for a connected sum of two trefoils. It follows from Corollary 7.12
that Xτ
irr(31#31) is a disjoint union of one copy of C∗and two isolated points.
According to
Theorem 7.18, we have for τ ∈(−2, 2) \ {±
√
3} that HP∗
τ(31#31) is supported in degrees −1, 0
with
HP−1
τ (31#31) = Z,
HP0
τ(31#31) = Z3, .
For the ﬁgure-eight K′′ = 41 ⊂S3, we compute similarly that
(7.7)
Xτ(S3 −K′′) = {(x, y) | (y −2)(y2 −(τ 2 −1)y + τ 2 −1) = 0},
which is smooth and zero-dimensional for all τ ∈(−2, 2). Writing K = 41#41 for a connected sum
of two ﬁgure-eight knots, it again follows from Corollary 7.12 that Xτ
irr(41#41) is a disjoint union
of four copies of C∗and four isolated points. We ﬁnd for τ ∈(−2, 2) that HP∗
τ(41#41) is supported
in degrees −1, 0, with
HP−1
τ (41#41) = Z4,
HP0
τ(41#41) = Z8.
We can similarly compute for τ ∈(−2, 2) \ {±
√
3} that HP∗
τ(31#41) is supported in degrees
−1, 0, with HP−1
τ (31#41) = Z2 and HP0
τ(41#41) = Z5.
Using Corollary 7.20, we can compute the Euler characteristic of our invariant for arbitrary
connected sums of trefoils and ﬁgure-eights. Letting K = (#n31)#(#m41) denote a connected sum
of n trefoils and m ﬁgure-eights, we ﬁnd that
χτ(K) = n + 2m,


## Page 39


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
39
provided that τ ∈(−2, 2) \ {±
√
3}.
We would like to extend the above computations to connected sums of the small knots and slim
knots which were considered in Section 6. Thanks to the following lemma, we can show that these
knots satisfy C.1–C.3 for all but ﬁnitely many τ ∈(−2, 2).
Lemma 7.21. Suppose that K ⊂Y satisﬁes A.1–A.2 in Section 5.2. Then X τ
irr(Y −K) is smooth
and zero-dimensional for all but ﬁnitely many τ ∈(−2, 2).
Proof. Let us ﬁrst note that B.1–B.4 hold for all values of τ contained in some coﬁnite subset V ⊂
(−2, 2) according to Proposition 5.1. It then follows by Proposition 5.5 that X τ
irr(Γ) = Hτ ∩X0(Γ),
where Γ = π1(K, x0). But by Proposition 5.6 and Lemma 5.7, we know that Hτ ∩X0(Γ) = Spec Rτ
where
(7.8)
Rτ = C[ǫ1]
ǫn1
1
× . . . × C[ǫk]
ǫnk
k
.
Finally, it follows from Lemma 5.18 that, after restricting to a possibly smaller coﬁnite subset
V ′ ⊂V ⊂(−2, 2), we have that ni = 1 for i = 1, . . . , k. This proves the claim.
□
We saw in Section 6.1 that A.1–A.2 hold for generic τ for a wide class of small knots and slim
knots, including all two-bridge knots, torus knots, and (−2, 3, 2n+1) pretzel knots where n ̸= 0, 1, 2
and 2n+1 is not divisible by 3. The above lemma now implies that these knots also satisfy C.1–C.3
for all but ﬁnitely many τ ∈(−2, 2). By combining Lemma 7.21 with Theorem 5.17, Corollary 6.3
and Theorem 7.18, we obtain Theorem 1.5, which we restate here for convenience.
Corollary 7.22 (Theorem 1.5). For i = 1, 2, suppose that Ki ⊂S3 is a two-bridge knot, a torus
knot, or a (−2, 3, 2n + 1) pretzel knot where n ̸= 0, 1, 2 and 2n + 1 is not divisible by 3.
Let
K = K1#K2. Then, for all but ﬁnitely many τ ∈(−2, 2), we have that HP∗
τ(K) is supported in
degrees −1, 0 with
HP−1
τ (K) = Z(degl b
A(K1))·(degl b
A(K2))
and
HP0
τ(K) = Z(degl b
A(K1))+(degl b
A(K2))+(degl b
A(K1))·(degl b
A(K2)).
We can compute P •
τ (K) explicitly when K is a connected sum of the slim knots considered in
Section 6.3 whose bA-polynomial can be determined exactly. We limit ourselves to the following
example.
Example 7.23. We saw in Example 6.4 that degl bA(81) = Z6. It follows from Corollary 7.22 that,
for all but ﬁnitely many τ ∈(−2, 2), we have that HP∗
τ(81#81) is supported in degrees −1, 0 with
HP−1
τ (81#81) = Z36 and HP0
τ(81#81) = Z48.
Finally, Corollary 7.20 allows us to compute the Euler characteristic of our invariant for arbitrary
connected sums of the knots considered in Corollary 7.22. More precisely, if we let Kj ⊂Yj be one
of the knots considered in Corollary 7.22 for j = 1, 2, . . . , n, we ﬁnd that
χτ(#n
j=1Kj) =
n
X
j=1
degl bA(Kj),
for all but ﬁnitely many τ ∈(−2, 2).
8. Appendix I: Parabolic Higgs bundles
The purpose of this appendix is to prove that the character variety Xτ
irr(Σ) considered in Propo-
sition 3.9 is connected and simply-connected. We do this by exploiting a version of the non-abelian
Hodge theory correspondence due to Simpson, which establishes an isomorphism between Xτ
irr(Σ)
and a certain moduli space of parabolic Higgs bundles; see Theorem 8.4.


## Page 40


40
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
The topology of parabolic Higgs bundles can be probed using Morse theory.
In particular,
Boden and Yokagawa showed in [BY96] that the relevant moduli spaces are connected and simply-
connected, under a technical hypothesis involving “genericity of weights”.
Unfortunately, this
hypothesis is violated in the case of interest to us. Our analysis, which draws signiﬁcantly from
the paper of Thaddeus [Tha02], will show that the desired conclusion is nonetheless true, provided
that Σ has genus at least 2.
We begin with a brief introduction to the theory of parabolic Higgs bundles. More details can
be found in [BY96], [Tha02] and [Mon16]. We particularly recommend the last reference to readers
with no prior exposure to this theory. This appendix is self-contained and completely independent
from the rest of the paper.
8.1. General deﬁnitions. This section collects some important deﬁnitions from the theory of
parabolic Higgs bundles. We warn the reader that there are many variants of these deﬁnitions in
the literature.
Let S be a Riemann surface of genus g. Fix a set of distinct points p1, . . . , pn ∈S and deﬁne the
eﬀective divisor D = p1 + · · · + pn.
Deﬁnition 8.1. A parabolic vector bundle E∗of rank r on (S, D) consists of the following data:
(i) a holomorphic vector bundle E of rank r,
(ii) for each point pi, a complete ﬂag Epi = E1(pi) ⊃E2(pi) ⊃· · · ⊃Er(pi) ⊃0,
(iii) for each point pi, a choice of weights 0 ≤α1(pi) < α2(pi) < · · · < αr(pi) < 1.
There are many conventions in the literature regarding the indexing of the ﬂags and weights.
Deﬁnition 8.1 is identical to [BY96, Deﬁnition 2.1], except that we require the ﬂags to be complete
for notational simplicity since this is the only case relevant to us.
Let E∗and F∗be parabolic vector bundles on (S, D) with weights α1
j(pi) and α2
j(pi) respectively.
A morphism φ : E →F of vector bundles is said to be a parabolic morphism if φ(Ej(pi)) ⊂Fk+1(pi)
whenever α1
j(pi) > α2
k(pi). It is said to be strongly parabolic if this holds whenever α1
j(pi) ≥α2
k(pi).
Deﬁnition 8.2. A parabolic Higgs bundle consists in the data of a parabolic vector bundle E∗and
a strongly parabolic morphism Φ : E →E ⊗K(D). This morphism is usually called the Higgs ﬁeld.
We will usually use boldface letters E = (E∗, Φ) to denote parabolic Higgs bundles.
There are natural notions of sub-bundle and quotient bundle in the categories of parabolic vector
bundles and parabolic Higgs bundles; see [Tha02, p. 3]. Given a parabolic vector bundle E∗on
(S, D), we say that F∗⊂E∗is a parabolic sub-bundle if F∗is a vector sub-bundle of E∗where the
weights and ﬁltration of F∗are induced from the corresponding data for E∗. More precisely, given
a point pi ∈D, we consider the sequence of vector spaces
(8.1)
Epi ∩Fpi ⊇E2(pi) ∩Fpi ⊇· · · ⊇Er(pi) ∩Fpi.
We obtain the ﬂag of F∗at pi by discarding any repetitions in (8.1). The weights of F∗at pi are
obtained from those of E∗by discarding αj(pi) if Ej−1(pi) ∩Fi = Ej(pi) ∩Fi. The ﬁltration and
weights of the quotient E∗/F∗are obtained similarly by considering the sequence
Epi/Fpi ⊇E2(pi) ∩(Fpi ∩E2(pi)) ⊇· · · ⊇Er(pi)/(Fpi ∩Er(pi)).
A Higgs sub-bundle F ⊂E is an ordinary parabolic sub-bundle F∗⊂E∗which is Φ-invariant,
where E = (E∗, Φ).
In this case, Φ passes to the quotient E∗/F∗, which thus also carries the
structure of a Higgs bundle.
The parabolic degree of a parabolic vector bundle E∗is deﬁned as follows
pdeg(E∗) := deg(E) +
X
p∈D
r
X
i=1
αi.


## Page 41


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
41
The slope is then
µ(E∗) = pdeg(E∗)
rank(E) .
We say that a parabolic vector bundle E∗is stable (resp. semistable) if there does not exist a
proper sub-bundle E′
∗⊂E∗such that µ(E′
∗) > µ(E) (resp. ≥). We say that a parabolic Higgs
bundle is stable (resp. semistable) if there does not exist a proper Φ-invariant sub-bundle E′
∗⊂E∗
(i.e. a proper Higgs sub-bundle) such that µ(E′
∗) > µ(E) (resp. ≥).
Given a line bundle L and real numbers 0 ≤α(pi) for i = 1, . . . , n, we deﬁne the parabolic bundle
L(α(p1)p1 + · · · + α(pn)pn) to be the underlying line bundle L([α(p1)]p1 + · · · + [α(pn)]pn) endowed
with the weight α(pi) −[α(pi)] at the point pi and the obvious ﬂag structure. Here [−] denotes the
integer part of a non-negative real number.
The determinant of a parabolic vector bundle E∗is deﬁned as
det(E∗) = det(E) ⊗


n
O
1
OX(
X
p∈D
(
r
X
i=1
αj(p))p)

.
Observe that we have det(E∗) = E∗if E∗is a parabolic line bundle, because in that case all
αj(p) are zero.
All of the above notions have sheaf-theoretic analogs. We refer the reader to [BY96, Sec. 2.2] for
the relevant deﬁnitions.
8.2. The main equivalence. We now specialize to the case of a Riemann surface S of genus g
with two distinguished points p, q ∈S. We set D = p + q as above. Let w denote the data of
weights 0 < α1(p) < α2(p) < 1 and 0 < α1(q) < α2(q) < 1.
We introduce the set Higgss(S, w, 2, OS) whose elements are isomorphism classes of parabolic
Higgs bundles (E∗, Φ) on (S, D) satisfying the following conditions:
• (E∗, Φ) is stable,
• rank E = 2,
• E∗has weights w,
• there is an isomorphism det(E∗) →OS,
• Tr Φ = 0.
We deﬁne Higgsss(S, w, 2, OS) in the analogous way, where we now only require (E∗, Φ) to be
semistable.
We also record the following important fact.
Proposition 8.3 (see Thm. 1.6 of [Kon93]). The set Higgss(S, w, 2, OS) has the structure of a
smooth (in general non-compact) complex manifold.
Let Σ be a Riemann surface with two boundary components which arises from a Heegaard
splitting (Σ, U0, U1) as in Section 3.2. Let c1 = Conj([cp]) and c2 = Conj([cq]) be deﬁned as in 3.1.
Then (Γ; c1, c2) is an object of Gp+. Given τ ∈(−2, 2), let Xτ
irr(Σ) = Xτ
irr(Γ) be the associated
character variety, deﬁned as in Section 2.
Let S be a closed Riemann surface obtained from Σ by gluing disks to its two boundary compo-
nents. Let p and q be distinguished points in the interior of these disks.
Theorem 8.4 (Simpson [Sim90]; see also Theorem 4.12 in [Mon16]). Fix α ∈(0, 1/2) and let
τ = 2 cos(2πα). Let the weights w be deﬁned by letting α1(p) = α1(q) = α and α2(p) = α2(q) = 1−α.
Then there is a diﬀeomorphism
(8.2)
Xτ
irr(Σ) ≃Higgss(S, w, 2, OS).
Remark 8.5. The left-hand side of Simpson’s original correspondence involves the character variety
of the punctured Riemann surface S −p −q, as opposed to the Riemann surface with boundary Σ.


## Page 42


42
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
Since the character variety only depends on the underlying fundamental group, this distinction is
immaterial.
8.3. Variations of the weights. It will be convenient for our purposes to consider the set P =
(0, 1/2) × (0, 1/2) with coordinates (α, β), which we will think of as a parameter space. We will
refer to the subset {α = β} ⊂P as the wall and to the subsets ∆+ = {α > β} and ∆−= {β > α}
as the chambers.
A point (α, β) ∈P determines a choice of weights w(α, β) on (S, D) by setting α1(p) = α,
α2(p) = 1−α, and α1(q) = β, α2(q) = 1−β. We would like to study how Higgsss(S, w(α, β), 2, OS)
changes as we vary (α, β) ∈P.
To this end, it will be necessary to adopt a slight change of perspective. According to Deﬁni-
tion 8.1 and Deﬁnition 8.2, we are viewing the weights of a parabolic Higgs bundle E = (E∗, Φ)
as being part of the data of the underlying parabolic vector bundle E∗. Instead, let us now view
the choice of weights as an independent piece of data, i.e. a parabolic Higgs bundle should now be
viewed as a triple (E∗, Φ, w).
Observe that as we vary (α, β) ∈P, a parabolic Higgs bundle (E∗, Φ, w(α, β)) remains of constant
rank and parabolic degree. The determinant det(E∗) and the trace Tr Φ are also constant. However,
the parabolic degree and slope of sub-bundles E′
∗⊂E∗can change.
Lemma 8.6. Suppose that α ̸= β and let w = w(α, β). Then
Higgsss(S, w, 2, OS) = Higgss(S, w, 2, OS).
Proof. If E∗∈Higgsss(S, w, 2, OS) is semistable but not stable, then there exists a Φ-invariant
sub-bundle E′
∗⊂E such that µ(E′
∗) = µ(E) = 0. Hence pdeg(E′
∗) = 0. But this means that either
α1(p) + α2(q) ∈Z or α2(p) + α1(q) ∈Z. This is possible only if α1(p) = α2(q), i.e. α = β.
□
By combining Proposition 8.3 and Lemma 8.6, it follows that Higgsss(S, w, 2, OS) has the struc-
ture of a smooth complex manifold if we let w = w(α, β) for (α, β) ∈∆+ ∪∆−. The following
important result describes the topology of this manifold.
Theorem 8.7 (Boden and Yokagawa, see p. 2 and Thm. 4.2 in [BY96]). Suppose that (α, β) ∈
∆+ ∪∆−and let w = w(α, β). Then Higgsss(S, w, 2, OS) has the structure of a smooth complex
manifold of complex dimension 6g −2. If g ≥1, it is connected and simply-connected.
Fix α ∈(0, 1/2). For 0 < ǫ < α, deﬁne γ : (0, ǫ) →(0, 1/2)2 by setting γ(t) = (α, α + t). Let
w(t) := w(γ(t)). Observe that w(t) ∈∆+ ∪∆−when t > 0, and so it follows by Lemma 8.6 that
Higgsss(S, w, 2, OS) = Higgss(S, w, 2, OS). Let us analyze what happens as t →0.
Lemma 8.8. Suppose that (E∗, Φ, w(t)) is stable for t > 0 and unstable for t = 0. Then there
exists a unique destabilizing Φ-invariant sub-bundle E+
∗⊂E∗. Thus, E∗can be uniquely presented
as a non-split extension of parabolic Higgs bundles 0 →E+ →E →E−→0.
Proof. Since E∗is unstable, there exists a Φ-invariant sub-bundle E+
∗⊂E such that µ(E+
∗) =
µ(E∗) = 0. To verify uniqueness, suppose for contradiction that ˜E+
∗⊂E is also destabilizing. Then
there is a morphism ˜E+
∗→E →E−
∗:= E/E+
∗of Φ-invariant bundles. But since ˜E+
∗and E−
∗are
both tautologically stable (since they are of rank 1) and of equal slope, this morphism is either zero
or an isomorphism; see (3.3) in [Tha02]. It cannot be the zero map since ˜E+
∗̸= E+
∗by assumption.
It cannot be an isomorphism since ˜E+
∗and E−
∗have diﬀerent parabolic structures. This gives the
desired contradiction.
To see that the extension is non-split, suppose for contradiction that E = E+ ⊕E−.
Then
0 = µ(E∗) = µ(E+
∗) + µ(E−
∗) for all 0 ≤t < ǫ.
In particular, for 0 < t < ǫ, we ﬁnd that
µ(E−
∗) = −µ(E+
∗) > 0 = µ(E∗), which contradicts the stability of E.
□


## Page 43


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
43
8.4. Dimension count. Throughout this section, α ∈(0, 1/2) is an arbitrary ﬁxed parameter.
We will be considering parabolic Higgs bundles of rank 1 on (S, D). A choice of weights therefore
consists in a choice of two real numbers 0 < α1(p) < 1 and 0 < α1(q) < 1. Let w1,t be weights
obtained by setting α1(p) = α and α1(q) = 1−α−t and let w2,t be obtained by setting α2(p) = 1−α
and α2(q) = α + t.
For t > 0, let E be the set of non-split extensions 0 →E+ →E →E−→0 of parabolic Higgs
bundles such that E = (E∗, Φ, w(t)) ∈Higgsss(S, w(t), 2, OS) and such that E+ = (E+
∗, Φ+) has
rank 1. Observe that E+ and E−are related by the following conditions:
(i) (E+
∗, Φ+) and (E−
∗, Φ−) have rank 1,
(ii) E+
∗≃(E−
∗)−1 and Tr Φ+ = −Tr Φ−.
We let X be the set of pairs ((E+
∗, Φ+, w1,t), (E−
∗, Φ−, w2,t)) satisfying the conditions (i) and (ii)
above. There is a natural surjection
(8.3)
E →X,
whose ﬁber Ep over a point p = ((E+
∗, Φ+, w1,t), (E−
∗, Φ−, w2,t)) is simply the set of non-split
extensions of (E−
∗, Φ−, w2,t) by (E+
∗, Φ+, w1,t).
Similarly, let ˜E be the set of non-split extensions 0 →E−→E →E+ →0.
The goal of this section is to prove the following claim.
Theorem 8.9. The complex dimension of E and ˜E is at most 4g −1.
Corollary 8.10. For g ≥2, the moduli space Higgss(S, w(α, α), 2, OS) is connected and simply-
connected for any α ∈(0, 1/2).
Proof of Corollary 8.10. Recall from the previous section that w(t) = w(α, α+t). By Theorem 8.7,
we know that Higgss(S, w(t), 2, OS) is connected and simply-connected and of complex dimension
6g −2 when t > 0 and g ≥1.
Given 0 < t0 < ǫ, there is a natural map Higgss(S, w(t0), 2, OS) →Higgsss(S, w(0), 2, OS)
obtained by sending (E∗, Φ, w(t0)) 7→(E∗, Φ, w(0)).
Since stability is an open condition under varying the weights, this image of this map con-
tains Higgss(S, w(0), 2, OS).
According to Lemma 8.8, if one restricts the map to the com-
plement of the locus E ∪˜E consisting of non-split extensions, then it is an isomorphism onto
Higgss(S, w(0), 2, OS) = Higgss(S, w(α, α), 2, OS). But it follows by the theorem that the comple-
ment of E ∪˜E has complex codimension 2g −1. If g ≥2, then 2g −1 ≥3 so the complement remains
connected and simply-connected, which gives the desired result.
□
It remains to prove Theorem 8.9. For simplicity, we will only consider the case of E. It will be
apparent that the argument works equally well for ˜E.
Lemma 8.11. The dimension of X is exactly 2g.
Proof. Let Higgs(S, w1,t) be the space of parabolic Higgs bundles of rank 1 and weights w1,t.
According to [BY96, p. 2], this space has complex dimension 2(g −1) + 2 = 2g. However, it
follows by condition (ii) in the deﬁnition of X that the projection X →Higgs(S, w1,t) taking a pair
((E+, Φ+, w1,t), (E−, Φ−, w2,t)) to the ﬁrst factor is an isomorphism. The claim follows.
□
Let E = (E∗, Φ) and F = (F∗, Ψ) be parabolic Higgs bundles on (S, D). Following [GPGM07, p.
7], we deﬁne a complex of sheaves
C•(E, F) : ParHom(E, F) →SParHom(E, F) ⊗K(D)
f 7→(f ⊗1)Φ −Ψf,
where ParHom(E, F) and SParHom(E, F) denote the spaces of parabolic, resp. strictly parabolic,
morphisms between E and F.
We write C•(E) = C•(E, E). We will need the following proposition.


## Page 44


44
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
Proposition 8.12 (Prop. 2.2 in [GPGM07]). The space of isomorphism classes of non-split exten-
sions 0 →E′ →E →E′′ →0 is parametrized by P(H1(C•(E′, E′′))).
We also record the following useful facts as a lemma.
Lemma 8.13. Let E′ and E′′ be non-isomorphic, stable parabolic Higgs bundles of rank 1. Then
we have:
(1) H0(C•(E′, E′′)) = 0.
(2) H2(C•(E′, E′′)) ≃H0(C•(E′′, E′)).
(3) Hi(C•(E′, E′′)) = 0 for all i < 0 and i > 2.
Proof. By [GPGM07, Prop. 2.2(ii)], the set H0(C•(E′, E′′)) parametrizes morphisms of parabolic
Higgs bundles from E′ to E′′. But since E′ and E′′ are non-isomorphic and have equal rank, it
follows from [Tha02, (3.3)] that the zero map is the only such morphism. This proves (1). Next, (2)
is a direct corollary of [GPGM07, 2.3(ii)]. Finally, (3) follows from [GPGM07, 2.3(ii)] and the fact
that C•(E′, E′′) is concentrated in non-negative degrees, and therefore has no hypercohomology in
negative degrees.
□
It follows from (1) and (2) that H2(C•(E′, E′′)) = 0, which implies that dim H1(C•(E′, E′′)) =
−χ(C•(E′, E′′)).
Lemma 8.14. Let E′ and E′′ be non-isomorphic, stable parabolic Higgs bundles on (S, D) of rank
1. Assume moreover that E′ and E′′ have distinct weights. Then χ(C•(E′, E′′)) = −2g.
Proof. By Riemann-Roch, we have
χ(SParHom(E′, E′′) ⊗K(D)) = deg(SParHom(E′, E′′) ⊗K(D)) + r(1 −g)
= deg(SParHom(E′, E′′)) + deg(K(D)) + r(1 −g)
= deg(SParHom(E′, E′′)) + (2g −2) + deg(D) + 1(1 −g).
Again applying Riemann-Roch, we have
χ(SParHom(E′, E′′)) = deg(SParHom(E′, E′′)) + r(1 −g)
= deg(SParHom(E′, E′′)) + (1 −g).
Putting together the above two equations, it follows that
χ(SParHom(E′, E′′) ⊗K(D)) = χ(SParHom(E′, E′′)) + (2g −2) + deg(D)
= χ(SParHom(E′, E′′)) + 2g,
where we have used the fact that deg(D) = 2.
Now, by deﬁnition we have χ(C•(E′, E′′)) = χ(ParHom(E′, E′′))−χ(SParHom(E′, E′′)⊗K(D)).
This is equivalent to χ(C•(E′, E′′)) = χ(ParHom(E′, E′′)) −χ(SParHom(E′, E′′) −2g by the above
equality.
Since E′ and E′′ have distinct weights, there is no diﬀerence between parabolic and strictly
parabolic morphisms, and it follows that ParHom(E′, E′′) = SParHom(E′, E′′). Therefore we have
χ(ParHom(E′, E′′)) −χ(SParHom(E′, E′′)) = 0 and the lemma follows.
□
Lemma 8.14, along with the observation that dim H1(C•(E′, E′′)) = −χ(C•(E′, E′′)) which was
stated after the proof of Lemma 8.13, implies that dim H1(C•(E′, E′′)) = 2g. This leads to the
following corollary of Proposition 8.12.
Corollary 8.15. The dimension of Ep is at most 2g −1.
It is now straightforward to prove Theorem 8.9.


## Page 45


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
45
Proof of Theorem 8.9. There exists a natural surjection E →X, whose ﬁber over a point p =
((E+
∗, Φ+, w1), (E−
∗, Φ−, w2)) is simply the set of extensions of (E−
∗, Φ−, w2) by (E+
∗, Φ+, w1). The
dimension of E is bounded above by the sum of the dimensions of X and Ep. The theorem thus
follows by putting together Lemma 8.11 and Corollary 8.15. As noted previously, this argument
works just as well for ˜E in place of E.
□
References
[AM] Mohammed Abouzaid and Ciprian Manolescu, A sheaf-theoretic model for SL(2, C) Floer homology, avail-
able at arXiv:1708.00289[math.GT].
[AK10] Gregory Arone and Marja Kankaanrinta, On the functoriality of the blow-up construction, Bull. Belg.
Math. Soc. Simon Stevin 17 (2010), no. 5, 821–832.
[BG93] I. Biswas and K. Guruprasad, Principal bundles on open surfaces and invariant functions on Lie groups,
International J. of Math. 4 (1993), no. 4, 535-544.
[BC16] Hans U. Boden and Cynthia L. Curtis, The SL(2, C) Casson invariant for knots and the ˆA-polynomial,
Canad. J. Math. 68 (2016), no. 1, 3–23.
[BY96] Hans U. Boden and Kˆoji Yokogawa, Moduli spaces of parabolic Higgs bundles and parabolic K(D) pairs
over smooth curves. I, Internat. J. Math. 7 (1996), no. 5, 573–598.
[BLZ02] S. Boyer, E. Luft, and X. Zhang, On the algebraic components of the SL(2, C) character varieties of knot
exteriors, Topology 41 (2002), no. 4, 667–694.
[BZ01] Steven Boyer and Xingru Zhang, A proof of the ﬁnite ﬁlling conjecture, J. Diﬀerential Geom. 59 (2001),
no. 1, 87–176.
[Bro94] Kenneth S. Brown, Cohomology of groups, Graduate Texts in Mathematics, vol. 87, Springer-Verlag, New
York, 1994. Corrected reprint of the 1982 original.
[Bud] Ryan Budney, Looking for large knot examples, MathOverﬂow. URL: https://mathoverﬂow.net/q/141251
(version: 2013-09-04).
[Bur90] Gerhard Burde, SU(2)-representation spaces for two-bridge knot groups, Math. Ann. 288 (1990), no. 1,
103–119.
[Bus] Vittoria Bussi, Categoriﬁcation of Lagrangian intersections on complex symplectic manifolds using per-
verse sheaves of vanishing cycles, available at arXiv:1404.1329[math.AG].
[Coh] Ralph
Cohen,
The
Topology
of
Fiber
Bundles,
Lecture
Notes,
available
at
http://math.stanford.edu/~ralph/fiber.pdf.
[CCG+94] D. Cooper, M. Culler, H. Gillet, D. D. Long, and P. B. Shalen, Plane curves associated to character
varieties of 3-manifolds, Invent. Math. 118 (1994), no. 1, 47–84.
[CS83] Marc Culler and Peter B. Shalen, Varieties of group representations and splittings of 3-manifolds, Ann.
of Math. (2) 117 (1983), no. 1, 109–146.
[CL96] D. Cooper and D. D. Long, Remarks on the A-polynomial of a knot, J. Knot Theory Ramiﬁcations 5
(1996), no. 5, 609–628.
[Don02] S. K. Donaldson, Floer homology groups in Yang-Mills theory, Cambridge Tracts in Mathematics, vol. 147,
Cambridge University Press, Cambridge, 2002. With the assistance of M. Furuta and D. Kotschick.
[Dr´e04] Jean-Marc Dr´ezet, Luna’s slice theorem and applications, Algebraic group actions and quotients, Hindawi
Publ. Corp., Cairo, 2004, pp. 39–89.
[Dun99] Nathan M. Dunﬁeld, Cyclic surgery, degrees of maps of character curves, and volume rigidity for hyperbolic
manifolds, Invent. Math. 136 (1999), no. 3, 623–657.
[Flo88] Andreas Floer, An instanton-invariant for 3-manifolds, Comm. Math. Phys. 118 (1988), no. 2, 215–240.
[Flo90]
, Instanton homology, surgery, and knots, Geometry of low-dimensional manifolds, 1 (Durham,
1989), 1990, pp. 97–114.
[GPGM07] O. Garc´ıa-Prada, P.B. Gothen, and V. Mu˜noz, Betti numbers of the moduli space of rank 3 parabolic
Higgs bundles, Memoirs of the American Mathematical Society, vol. 187, 2007.
[GM11] Stavros Garoufalidis and Thomas W. Mattman, The A-polynomial of the (−2, 3, 3 + 2n) pretzel knots,
New York J. Math. 17 (2011), 269–279.
[Gol04] William M. Goldman, The complex-symplectic geometry of SL(2, C)-characters over surfaces, Algebraic
groups and arithmetic, Tata Inst. Fund. Res., Mumbai, 2004.
[Gul] Martin
Gulbrandsen,
Local
aspects
of
geometric
invariant
theory,
available
at
https://people.kth.se/~gulbr/local-git.pdf.
[Har77] Robin Hartshorne, Algebraic geometry, Springer-Verlag, New York-Heidelberg, 1977. Graduate Texts in
Mathematics, No. 52.


## Page 46


46
LAURENT C ˆOT´E AND CIPRIAN MANOLESCU
[HT85] A. Hatcher and W. Thurston, Incompressible surfaces in 2-bridge knot complements, Invent. Math. 79
(1985), no. 2, 225–246.
[Her97] Christopher M. Herald, Flat connections, the Alexander invariant, and Casson’s invariant, Comm. Anal.
Geom. 5 (1997), no. 1, 93–120.
[Hid93] Haruzo Hida, Elementary theory of L-functions and Eisenstein series, London Mathematical Society
Student Texts, vol. 26, Cambridge University Press, Cambridge, 1993.
[Joy15] Dominic Joyce, A classical model for derived critical loci, J. Diﬀerential Geom. 101 (2015), no. 2, 289–367.
[Juh06] Andr´as Juh´asz, Holomorphic discs and sutured manifolds, Algebr. Geom. Topol. 6 (2006), 1429–1457.
[JTZ18] Andr´as Juh´asz, Dylan Thurston, and Ian Zemke, Naturality and mapping class groups in Heegaard Floer
homology (2018), available at arXiv:1210.4996v4. (preprint).
[Kap15] Misha
Kapovich,
On
character
varieties
of
3-manifold
groups
(2015),
available
at
http://sgt.imj-prg.fr/curve2015/Slides/Kapovich.pdf. (Talk slides).
[Kon93] Hiroshi Konno, Construction of the moduli space of stable parabolic Higgs bundles on a Riemann surface,
J. Math. Soc. Japan 45 (1993), no. 2, 253–276.
[KM11a] Peter B. Kronheimer and Tomasz S. Mrowka, Khovanov homology is an unknot-detector, Publ. Math.
Inst. Hautes ´Etudes Sci. 113 (2011), 97–208.
[KM11b]
, Knot homology groups from instantons, J. Topol. 4 (2011), no. 4, 835–918.
[KM13]
, Gauge theory and Rasmussen’s invariant, J. Topol. 6 (2013), no. 3, 659–674.
[Lau14] Fran¸cois Laudenbach, A proof of Reidemeister-Singer’s theorem by Cerf’s methods, Ann. Fac. Sci.
Toulouse Math. (6) 23 (2014), no. 1, 197–221 (English, with English and French summaries).
[LT15] Thang T. Q. Le and Anh T. Tran, On the AJ conjecture for knots, Indiana Univ. Math. J. 64 (2015),
no. 4, 1103–1151. With an appendix written jointly with Vu Q. Huynh.
[Lee13] John M. Lee, Introduction to smooth manifolds, 2nd ed., Graduate Texts in Mathematics, vol. 218,
Springer, New York, 2013.
[Lin92] Xiao-Song Lin, A knot invariant via representation spaces, J. Diﬀerential Geom. 35 (1992), no. 2, 337–357.
[LM85] Alexander Lubotzky and Andy R. Magid, Varieties of representations of ﬁnitely generated groups, Mem-
oirs of the American Math Society, vol. 58, American Mathematical Society, 1985.
[MM08] Melissa L. Macasieb and Thomas W. Mattman, Commensurability classes of (−2, 3, n) pretzel knot com-
plements, Algebr. Geom. Topol. 8 (2008), no. 3, 1833–1853.
[Mar15] Julien
March´e,
Character
varieties
in
SL2
and
Kauﬀman
skein
algebras
(2015),
available
at
https://arxiv.org/pdf/1510.09107.pdf[math.GT].
[Man75] Yuri Manin, Introduction to the Theory of Schemes, Moscow Lectures, Springer, 1975.
[Mat14] Daniel V. Mathews, An explicit formula for the A-polynomial of twist knots, J. Knot Theory Ramiﬁcations
23 (2014), no. 9.
[Mat00] Thomas Mattman, The Culler-Shalen seminorms of Pretzel knots, Ph.D. thesis, McGill University (2000).
[MS74] John W. Milnor and James D. Stasheﬀ, Characteristic classes, Princeton University Press, Princeton, N.
J.; University of Tokyo Press, Tokyo, 1974. Annals of Mathematics Studies, No. 76.
[Mon16] Gabriele Mondello, Topology of representation spaces of surface groups in PSL2(R) with assigned boundary
monodromy and nonzero Euler number, Pure Appl. Math. Q. 12 (2016), no. 3, 399–462.
[Muk03] Shigeru Mukai, An introduction to invariants and moduli, Cambridge Studies in Advanced Mathematics,
vol. 81, Cambridge University Press, Cambridge, 2003. Translated from the 1998 and 2000 Japanese
editions by W. M. Oxbury.
[Oza17] Makoto Ozawa, Knots and surfaces (2017), available at https://arxiv.org/pdf/1603.09039.pdf.
[Por] Joan
Porti,
Varieties
of
characters
and
knot
symmetries
(I),
available
at
http://mat.uab.es/%7Eporti/Cortona.pdf. (Talk slides).
[Sch08] Alexander H. W. Schmitt, Geometric invariant theory and decorated principal bundles, Zurich Lectures
in Advanced Mathematics, European Mathematical Society (EMS), Z¨urich, 2008.
[Sha02] Peter B. Shalen, Representations of 3-manifold groups, Handbook of geometric topology, North-Holland,
Amsterdam, 2002, pp. 955–1044.
[Sik12] Adam S. Sikora, Character Varieties, Trans. Am. Math. Soc. 364 (2012), 5173–5208.
[Sim90] Carlos Simpson, Harmonic bundles on noncompact curves, J. Amer. Math. Soc. 3 (1990), 713-770.
[Tha02] Michael Thaddeus, Variation of moduli of parabolic Higgs bundles, J. Reine Angew. Math. 547 (2002),
1-14.
[Tsa94] Chichen M. Tsau, Incompressible surfaces in the knot manifolds of torus knots, Topology 33 (1994), no. 1,
197–201.
[Vak] Ravi Vakil, The Rising Sea: Foundations Of Algebraic Geometry Notes, September 2015 version, available
at http://math.stanford.edu/~vakil/216blog/index.html.
[War83] F.W. Warner, Foundations of Diﬀerentiable Manifolds and Lie Groups, Graduate Texts in Mathematics,
Springer, 1983.


## Page 47


A SHEAF-THEORETIC SL(2, C) FLOER HOMOLOGY FOR KNOTS
47
[Wei64] Andr´e Weil, Remarks on the Cohomology of Groups, Ann. of Math. 80 (1964), no. 1, 149-158.
[Wit12] Edward Witten, Fivebranes and knots, Quantum Topol. 3 (2012), no. 1, 1–137.
Department of Mathematics, Stanford University, 450 Serra Mall, Stanford, CA 94305
E-mail address: lcote@stanford.edu
Department of Mathematics, UCLA, 520 Portola Plaza, Los Angeles, CA 90095
E-mail address: cm@math.ucla.edu

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 1811_07000v2_a_sheaf_theoretic_sl_2_c_floer_homology_for_knots
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1811_07000V2_A_SHEAF_THEORETIC_SL_2_C_FLOER_HOMOLOGY_FOR_KNOTS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

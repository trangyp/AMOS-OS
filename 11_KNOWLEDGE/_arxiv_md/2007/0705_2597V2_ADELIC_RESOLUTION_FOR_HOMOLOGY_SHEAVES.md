---
canon-group: reference
rscf-state: source-claim
arxiv_id: 0705.2597v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0705.2597v2_Adelic_resolution_for_homology_sheaves

> Source: 0705.2597v2_Adelic_resolution_for_homology_sheaves.pdf

> Pages: 64

---


## Page 1


arXiv:0705.2597v2  [math.AG]  11 Feb 2008
Adelic resolution for homology sheaves
Sergey Gorchinskiy∗
Steklov Mathematical Institute
e-mail: gorchins@mi.ras.ru
Abstract
A generalization of the usual ideles group is proposed, namely, we construct
certain adelic complexes for sheaves of K-groups on schemes. More generally, such
complexes are deﬁned for any abelian sheaf on a scheme. We focus on the case
when the sheaf is associated to the presheaf of a homology theory with certain
natural axioms, satisﬁed by K-theory. In this case it is proven that the adelic
complex provides a ﬂasque resolution for the above sheaf and that the natural
morphism to the Gersten complex is a quasiisomorphism. The main advantage of
the new adelic resolution is that it is contravariant and multiplicative in contrast
to the Gersten resolution. In particular, this allows to reprove that the intersection
in Chow groups coincides up to sign with the natural product in the corresponding
K-cohomology groups. Also, we show that the Weil pairing can be expressed as a
Massey triple product in K-cohomology groups with certain indices.
Contents
1
Introduction
2
2
Generalities on adeles
6
2.1
Deﬁnition and ﬁrst properties . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2
Relation with the Cousin complex . . . . . . . . . . . . . . . . . . . . . .
12
2.3
Projection formula
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
2.4
Sheaves with controllable support . . . . . . . . . . . . . . . . . . . . . .
16
2.5
1-pure sheaves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
2.6
A′-adelic groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
3
Adeles for homology sheaves
24
3.1
Homology theories
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
3.2
Strongly locally eﬀaceable pairs . . . . . . . . . . . . . . . . . . . . . . .
29
3.3
Existence and addition of strongly locally eﬀaceable pairs . . . . . . . . .
30
∗The author was partially supported by the grants RFBR 04-01-00613, 05-01-00455, and INTAS
05-1000008-8118.
1


## Page 2


3.4
Patching systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
3.5
Main theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
38
3.6
Explicit cocycles
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
4
Applications to K-cohomology
47
4.1
Generalities on K-cohomology and K-adeles . . . . . . . . . . . . . . . .
47
4.2
Euler characteristic with support for K-groups . . . . . . . . . . . . . . .
51
4.3
Formula for product in K-cohomology
. . . . . . . . . . . . . . . . . . .
58
4.4
Massey triple product and the Weil pairing . . . . . . . . . . . . . . . . .
60
1
Introduction
Classical adeles have been deﬁned by A. Weil and C. Chevalley for a global ﬁeld K in
the following way: adeles are elements of the set AK =
Y
v
Kv, where v runs over all
valuations of the ﬁeld K, Kv is the completion of K at the point v, and the restricted
product
Q means that we consider only collections {fv} ∈
Y
v
Kv such that fv ∈ˆOv
for almost all v, where ˆOv ⊂Kv is the complete local ring corresponding to v. The set
of adeles has a natural structure of a topological ring. Its group of units is called the
group of ideles and is equal to A∗
K =
Y
v
K∗
v, where the restricted product is taken in
the same sense as above with Kv replaced by K∗
v and ˆOv replaced by ˆO∗
v (we omit the
details about a topological structure of the ideles). The group of ideles plays a central
role in the classical one-dimensional global class ﬁeld theory. One of its main properties
is the relation with the class group Cl(K) of K. Actually there is a natural surjective
homomorphism A∗
K →Cl(K) deﬁned by the formula {fv} 7→P
v
νv(f) · [v], where the
sum is taken over all non-archemedian valuations v and νv denotes a discrete valuation
corresponding to v.
Further, J.-P. Serre used in [24] non-complete adeles on a curve X over a ﬁeld k
to prove the Riemann–Roch theorem for X. Namely he considered collections {fx} ∈
Y
x∈X
k(X) such that fx ∈OX,x for almost all closed points x ∈X, where OX,x is the local
ring of X at x. Similarly, one may construct a non-complete version of ideles. Moreover,
Serre was using a certain complex of adeles though he did not mention this explicitly.
A. N. Parshin introduced in [19] non-complete (also called rational) adeles on a sur-
face, and has constructed a certain adelic complex. In [20] there is also a multiplicative
version of complete adeles on a surface, related to the K2-functor, and have been pro-
posed a natural two-dimensional generalization of the classical class ﬁeld theory. Later,
A. A. Beilinson deﬁned in [1] a complex of adeles A(X, OX)• for any Noetherian scheme
X using simplicial language (in fact, the adelic complex is deﬁned for any quasicoherent
sheaf F on X instead of OX). Let us describe explicitly the complexes of rational adeles
2


## Page 3


in low dimensions. For a curve X over a ﬁeld k, it looks like
0 →k(X) ⊕
Y
x∈X
OX,x →
Y
x∈X
k(X) →0,
where the restricted product is taken in the above sense and the diﬀerential is deﬁned
using the natural inclusions by the formula (fX, {fx}) 7→{fx −fX}. For a surface X,
the rational adelic complex has the following form:
0 →k(X)⊕
Y
x∈X
OX,x⊕
Y
C⊂X
OX,C →
Y
C⊂X
k(X)⊕
Y
x∈X
k(X)⊕
Y
x∈C
OX,C →
Y
x∈C⊂X
k(X) →0,
where the restricted products can be deﬁned explicitly in terms of the poles of functions,
and the diﬀerentials are deﬁned using the natural inclusion by the formulas
(fX, {fx}, {fC}) 7→({fC −fX}, {fx −fX}, {fx −fC})
and
({fXC}, {fXx}, {fCx}) 7→{fCx −fXx + fXC}.
The Beilinson–Huber theorem tells that for any Noetherian scheme, the cohomology
groups of the adelic complex A(X, OX)• are canonically isomorphic to the cohomology
groups Hi(X, OX), see [1], [14] (the analogous result holds true for any quasicoherent
sheaf F on X).
The aim of this paper is to give a version of these constructions for a class of sheaves
of abelian groups on schemes diﬀerent from quasicoherent sheaves, in particular, for
sheaves of K-groups. Recall that a sheaf of K-groups KX
n = Kn(OX) is associated with
the presheaf given by U 7→Kn(k[U]), n ≥0, where U ⊂X is an open subset in the
scheme X and Kn(−) denotes the Quillen K-group. Recall that for a regular Noetherian
separable scheme X of ﬁnite type over a ﬁeld, there are Gersten (or Cousin) complexes
Gers(X, n)• whose cohomology groups are equal to Hi(X, KX
n ). On the other hand, for
the case of a regular curve X, there is a natural quasiisomorphism of complexes
0
→
Kn(k(X)) ⊕
Y
x∈C
Kn(OX,x)
→
Y
x∈X
Kn(k(X))
→
0
↓
↓
0
→
Kn(k(X))
→
L
x∈X
Kn−1(k(x))
→
0
where the restricted product is taken in the same way as before for rational adeles with
k(X) replaced by Kn(k(X)) and OX,x replaced by Kn(OX,x), k(x) stands for the residue
ﬁeld at x, the complex on the bottom is the Gersten complex for the curve X, the ﬁrst
vertical morphism is the projection on the ﬁrst summand, and the second one is given
by residue maps. We give a higher-dimensional generalization of this. Recall that in
general the Cousin complex of an abelian sheaf consists of direct sums over schematic
points of ﬁxed codimension. Following the general deﬁnition of adeles, we replace these
direct sums by adelic groups, which are certain restricted products over ﬂags of ﬁxed
3


## Page 4


length, i.e., sequences of schematic points η0 . . . ηp on a scheme X such that ηi ∈ηi−1
for all 1 ≤i ≤p. For the explicit construction of these groups in the simplest cases see
Examples 2.32. Next, we construct an adelic complex A(X, F)•, which consists of adelic
groups. Under certain natural conditions, there is a canonical morphism of complexes
νX : A(X, F)• →Cous(X, F)•, where Cous(X, F)• is the Cousin complex of F on X.
We restrict our attention to a special type of abelian sheaves, namely, sheaves associated
with the presheaves of a homology theory that satisﬁes certain axioms (see Section 3.1).
Our main result is that for such sheaves, the morphism νX is a quasiisomorphism on
smooth varieties over an inﬁnite perfect ﬁeld. In particular, we get the following result.
Theorem 1.1. There is a canonical morphism of complexes νX
: A(X, KX
n )• →
Gers(X, n)•. This morphism is a quasiisomorphism if X is a smooth variety over an
inﬁnite perfect ﬁeld.
Recall that one of the main advantages of the Gersten complex is that it allows to
relate explicitly cohomology of the sheaves of K-groups, called K-cohomology, with the
(algebraic) geometry of X. In particular, the famous Bloch–Quillen formula says that
Hn(X, Kn(OX)) = CHn(X), see [22]. At the same time there is a canonical product
between the sheaves of K-groups, induced by the product in K-groups themselves. This
product structure cannot be prolonged to the Gersten complex: otherwise there would
exist an intersection theory for algebraic cycles without taking them modulo rational
equivalence.
The main advantage of the adelic construction is that the ﬂag simplicial structure,
involved in the deﬁnition of the adelic complexes, allows to deﬁne a product on them,
i.e., the complex L
n≥0
A(X, KX
n )• is a DG-ring. Note that the general theory of sheaves
provides many multiplicative simplicial resolutions of sheaves, i.e., resolutions carrying
the product structure, for example, Chech or Godement resolutions. Nevertheless these
resolutions seem to be too general to reﬂect the algebro-geometric structure of a scheme,
for instance, relations of K-cohomology to algebraic cycles or direct images for proper
morphisms.
Though the adelic complex as presented here also does not have direct
images, the covariant Gersten complex turns out to be a right DG-module over the DG-
ring of adeles. Roughly speaking, the diﬀerence between the adelic complex A(X, KX
n )•
and the Gersten complex Gers(X, n)• consists of all possible systems of local K-group
equations along ﬂags for each irreducible subvariety on X. The main idea is that in
order to get an intersection-product on the groups of algebraic cycles we enlarge them
by systems of equations instead of taking them modulo rational equivalence.
Analysis of the adelic complex provides certain explicit formulas for products and
also Massey higher products in K-cohomology. In particular, we obtain a new direct
proof of the coincidence up to sign of the intersection product in Chow groups and the
natural product in K-cohomology. Another example is the triple product m3(α, l, β),
where α ∈CHd(X)l, β ∈Pic0(X)l. It occurs that this triple is equal to the Weil pairing
of α and β. In the case of a curve the equality of the corresponding explicit adelic formula
with the Weil pairing was proved by diﬀerent methods in [13], [17], and [10].
The paper is organized as follows. First in Section 2.1 we deﬁne adelic groups for
abelian sheaves on arbitrary schemes and study their basic properties, such as multi-
4


## Page 5


plicativity and contravariancy. Section 2.2 shows an important relation of the adelic
complex with the Cousin complex. In Sections 2.4 and 2.5 we establish more properties
of adelic groups imposing rather mild conditions on sheaves. In Section 2.6 we deﬁne a
new type of adelic groups, called A′-adeles, which do not have a multiplicative structure
but provide a ﬂasque resolution for any Cohen–Macaulay sheaf.
In Section 3.1 we introduce the notion of a homology theory locally acyclic in ﬁbra-
tions (l.a.f. homology theory). We discuss the basic properties of an l.a.f. homology
theory and deﬁne the associated homology sheaves.
Then, in Section 3.2 we deﬁne
strongly locally eﬀaceable pairs of closed subvarieties on a smooth variety with respect
to an l.a.f. homology theory. This is a globalization of the method from Quillen’s proof
of the Gersten conjecture in the geometric case. Section 3.3 contains the existence and
the addition results for strongly locally eﬀaceable pairs. In particular, we get some uni-
form version of the local exactness of a Gersten resolution, which might have interest in
its own right (see Corollary 3.20). In Section 3.4 we introduce the notion of patching
systems of closed subvarieties on a smooth variety. This is our key tool for studying the
relation between the adelic and the Gersten complexes. Section 3.5 contains the main
result (Theorem 3.34): for any l.a.f. homology theory the adelic complex of the homology
sheaves is quasiisomorphic to the Gersten complex on any smooth variety over an inﬁnite
perfect ﬁeld. After several easy reductions the proof of the main theorem is reduced to a
certain approximation result, namely Lemma 3.37, whose proof uses the developed tech-
nique of patching systems. Section 3.6 is devoted to the explicit construction of cocycles
in the adelic complex representing cocycles in the Gersten complex.
Then we consider our main example of an l.a.f.
homology theory, namely the
K′-theory of schemes. We recall some general facts on K-sheaves and K-cohomology
in Section 4.1. We also give some examples of the explicit K-adelic cocycles for algebraic
cycles and we study the link between the K-adeles and the coherent diﬀerential adeles
of Parshin and Beilinson. Section 4.2 provides an explicit construction of an Euler char-
acteristic map from the K-groups of the exact category of complexes of coherent sheaves
on a scheme T that are exact outside of a closed subscheme S ⊂T to the K′-groups of S.
This map can be also constructed using R-spaces introduced in [3] or general preperties
of Waldhausen K-theory of perfect complexes given in [26]. Next, explicit formulas for
products in K-cohomology in terms of Gersten cocycles are obtain in Section 4.3 as a
consequence of the product structure on the adelic complex (Theorem 4.22). The case
of certain Massey triple products is treated in Section 4.4. We also show the coincidence
of the considered Massey triple product with the Weil pairing between zero-cycles and
divisors (Proposition 4.27).
It is a pleasure for the author to thank A. N. Parshin for his constant attention to this
work and many helpful suggestions, C. Soul´e for many useful discussions and remarks,
D. Grayson, and D. Kaledin for important comments, which appeared after they read the
manuscript of this text. The author is very grateful for the hospitality during his visits
to Institut de Math´ematiques de Jussieu, where many parts of the text had been written
down.
5


## Page 6


2
Generalities on adeles
2.1
Deﬁnition and ﬁrst properties
We use Beilinson’s simplicial approach to higher-dimensional adeles, ﬁrst deﬁned by
Parshin in the two-dimensional case (see [1], [19]). Besides, we follow most notations
from [14]. For a cosimplicial group A∗, let A• be the associated cochain complex. We
deﬁne the diﬀerential in the tensor product A• ⊗B• of two complexes A• and B• by the
formula d(a ⊗b) = da ⊗b + (−1)deg aa ⊗db. For a scheme X, by X(p) denote the set of
all schematic points of codimension p on X.
Let X be a scheme and let P(X) be the set of all its schematic points. By η denote
the closure of a point η ∈P(X). By deﬁnition, put
S(X)p = {(η0, η1 . . . , ηp) : ηi ∈P(X), ηi ∈ηi−1 for all 1 ≤i ≤p}.
An element F = (ηp . . . ηp) ∈S(X)p is called a ﬂag of length p. The assignment X 7→
S(X)∗is a covariant functor from the category of schemes to the category of simplicial
sets. Let δp
i : S(X)p →S(X)p−1, 0 ≤i ≤p and σp
i : S(X)p →S(X)p+1, 0 ≤i ≤p be
the natural boundary and degeneracy maps, respectively.
There is an exact additive functor F 7→S(X, F) from the category of abelian sheaves
on X to the category of cohomological abelian systems of coeﬃcients on S(X)∗, given
by S(X, F)(η0 . . . ηp) = Fη0 for any ﬂag (η0 . . . ηp) ∈S(X)p. By C(X, F)∗denote the
cosimplicial group associated to the system of coeﬃcients S(X, F) on S(X)∗. We have
C(X, F)p =
Q
η0...ηp
Fη0. Explicitly, the diﬀerential in the complex C(X, F)• is given by
the formula (df)η0...ηp+1 =
pP
i=0
(−1)ifη0...ˆηi...ηp+1 ∈Fη0 for any element f ∈C(X, F)p, where
the hat means that we omit the corresponding element in the ﬂag. By deﬁnition, put
C(M, F) =
Q
(η0...ηp)∈M
Fη0 for a subset M ⊂S(X)p. In particular, we have C(X, F)p =
C(S(X)p, F).
Evidently, S(X, F ⊗G) = S(X, F) ⊗S(X, G) for any two sheaves F and G on X
(we consider a point wise multiplication for systems of coeﬃcients). Consequently there
is a canonical morphism of complexes C(X, F)• ⊗C(X, G)• →C(X, F ⊗G)• given by
(f · g)η0...ηp+q = fη0...ηp ⊗gηp...ηp+q for any elements f ∈C(X, F)p, g ∈C(X, G)q.
If f : X →Y is a morphism of schemes, then there is a natural morphism
of systems of coeﬃcients S(Y, f∗F) →f∗S(X, F) on S(Y )∗, where f∗S(X, F)(G) =
Q
F :f(F )=G
S(X, F)(F) for any ﬂag G ∈S(Y )∗.
Consequently there is a morphism of
cosimplicial groups C(Y, f∗F)∗→C(X, F)∗.
Let F be a sheaf of abelian groups on a scheme X. We put FU = (iU)∗i∗
UF for any
open embedding iU : U ֒→X. Note that (FU)V = FU∩V for two open subsets U and V
in X. For a point η ∈X, we put [F]η = j∗j∗(F), where j : SpecOX,η →X is the natural
morphism. We have [F]η = lim
−→FU, where the limit is taken over all open subsets U ⊂X
containing the point η.
6


## Page 7


For M ⊂S(X)p, η ∈P(X), by ηM denote the following set:
ηM = {(η1, . . . , ηp) ∈S(X)p−1 : (η, η1, . . . , ηp) ∈M}.
We deﬁne inductively the adelic groups A(M, F), M ⊂S(X)p of F on X in the following
way.
Deﬁnition 2.1. For a subset M ⊂P(X) = S(X)0, we put
A(M, F) = C(M, F) =
Y
η∈M
Fη.
For a subset M ⊂S(X)p, p > 0, we put
A(M, F) =
Y
η∈P (X)
eA(ηM, [F]η),
and
eA(M, [F]η) = lim
−→
U
A(M, FU),
where the limit is taken over all open subsets U ⊂X containing the point η. Also, we
put A(∅, F) = 0. Elements of the adelic groups A(M, F) are called adeles.
Remark 2.2. The deﬁnition of adelic groups does not use the ring structure of the sheaf
OX. In fact, all generalities about adeles that are discussed below make sense for abelian
sheaves on any topological space such that every closed subset has a unique generic point.
Remark 2.3. This deﬁnition is analogous to the deﬁnition of adeles from [1]. The main
diﬀerences with [1] are as follows: we replace coherent sheaves by sheaves of type FV
and we use no completion in the construction. Consequently our adelic condition is more
rough: if F is a coherent sheaf on a Noetherian scheme X, then the deﬁned above group
A(M, F) contains the corresponding group of rational adeles (see [19] and [14]). However
there is a comparison in the backward direction, see Proposition 4.7.
Remark 2.4. The scheme X is not included in our notation for adelic groups A(M, F).
Nevertheless in what follows X could be always reconstructed from the notation for a
sheaf F.
Remark 2.5. It follows from the deﬁnition that for any subset M ⊂S(X)p, p > 0 and
for any open subset V ⊂X, we have
A(M, FV ) =
Y
η∈P (X)
lim
−→
Uη
A(ηM, FV ∩Uη) = lim
−→
{Uη}
Y
η∈P (X)
A(ηM, FV ∩Uη),
where the second limit is taken over the set of systems {Uη} of open subsets in X
parameterized by schematic points η such that η ∈Uη for any η ∈P(X), and {Uη} ≤
{U′
η} if and only if Uη ⊇U′
η for all η ∈P(X).
7


## Page 8


Evidently, F 7→A(M, F) is a covariant functor from the category of abelian sheaves
on X to the category of abelian groups for any subset M ⊂S(X)p. It is easily shown that
A((η0 . . . ηp), F) = Fη0 for any element (η0 . . . ηp) ∈S(X)p. For any subset M ⊂S(X)p,
there is a natural morphism θ : A(M, F) →C(M, F) =
Q
(η0...ηp)∈M
Fη0.
Proposition 2.6.
(i) For any subsets M, N ⊂S(X)p, p ≥0 such that M ∩N = ∅, there is a decompo-
sition A(M ∪N, F) = A(M, F) ⊕A(N, F);
(ii) for any subset M ⊂S(X)p, p > 0, there are boundary maps dp
i : A(δp+1
i
(M), F) →
A(M, F), 0 ≤i ≤p;
(iii) for any subset M ⊂S(X)p, there are isomorphisms sp
i : A(σp
i (M), F) →A(M, F),
0 ≤i ≤p;
(iv) for any subset M ⊂S(X)p and for any sheaves F, G on X, there is a morphism
A(M, F) ⊗A(M, G) →A(M, F ⊗G);
(v) for any subset M ⊂S(Y )p and for any morphism of schemes f : X →Y , there is
a natural morphism f ∗: A(M, f∗F) →A(f −1(M), F);
(vi) all the morphisms constructed in (i)−(v) commute via the map θ with their natural
counterparts for the corresponding direct product groups.
Proof. The proof of (i) and the constructions in (ii), (iii) are the same as the proof of
Propositions 2.1.5, Deﬁnition 2.2.2, and the proof of Proposition 2.3.1, respectively, from
[14]. The only diﬀerence is that we use sheaves of type FU in place of coherent sheaves.
The proof of (iv) is by induction on p and uses that there is a natural morphism of
sheaves FU ⊗GV →(F ⊗G)U∩V for any open subsets U, V ⊂X. Besides, for p = 0, the
morphisms in question equals the point wise multiplication in stalks of sheaves.
The proof of (v) is also by induction on p and uses that there is a natural morphism
of sheaves (f∗F)U →f∗(Ff−1(U)) for any open subset U ⊂Y . Besides, for p = 0, the
morphism in question equals the point wise map on stalks of sheaves.
The proof of (vi) is straightforward.
For a closed or an open subscheme Y ⊂X, let iY be the corresponding embedding.
For any subset M ⊂S(X)p, let M(Y ) be the set of ﬂags on Y that are in M. The
following consequences of Proposition 2.6 are needed for the sequel.
Corollary 2.7.
(i) For any open subset U ⊂X and any subset M ⊂S(X)p, we have
A(M(U), F) = A(M(U), i∗
UF),
where the right hand side is the adelic group on U. In particular, A(M, F) =
A(M(U), i∗
UF) ⊕A for some subgroup A ⊂A(M, F);
8


## Page 9


(ii) for any schematic point η ∈X and any subset M ⊂S(X)p, we have
A(M(η), F) = A(M(η), j∗
ηF),
where jη : Xη = Spec(OX,η) →X is the natural morphism of schemes, M(η)
is the set of ﬂags on Xη that are from M, and the right hand side is the adelic
group on Xη. In particular, A(M, F) = A(M(η), j∗
ηF) ⊕B for some subgroup
B ⊂A(M, F);
(iii) for any closed subset Z ⊂X and any subset M ⊂S(X)p, we have
A(M(Z), F) = A(M(Z), i∗
ZF),
where the right hand side is the adelic group on Z. In particular, for any sheaf G
on Z we have A(M(Z), (iZ)∗G) = A(M(Z), G);
(iv) suppose that Y, Z are closed subschemes in X such that X = Y ∪Z; then for any
sheaf F on X and for any subset M ⊂S(X)p we have
A(M, F) = [A(M(Y ), i∗
Y F) ⊕A(M(Z), i∗
ZF)]/A(M(Y ∩Z), i∗
Y ∩ZF);
(v) consider a point η ∈X and a subset M ⊂S(X)p such that any ﬂag in M starts
with η; then for any sheaf F on X and for any open subset U ⊂X containing η
we have
A(M, F) = A(M, FU).
We put As(X, F)p = A(S(X)p, F).
Using Proposition 2.6, we get the following
statement.
Corollary 2.8.
(i) There is a natural structure of a cosimplicial group on As(X, F)∗such that the
natural morphism θ : As(X, F)∗→C(X, F)∗is a morphism of cosimplicial groups;
(ii) for any two sheaves F and G on X there is a morphism of complexes As(X, F)• ⊗
As(X, G)• →As(X, F⊗G)•, which commutes via θ with the morphism of complexes
C(X, F)• ⊗C(X, G)• →C(X, F ⊗G)•;
(iii) for any morphism of schemes f : X →Y and for any sheaf F on X there is a
morphism of cosimplicial groups As(Y, f∗F)∗→As(X, F)∗, which commutes via θ
with the morphism of cosimplicial groups C(Y, f∗F)∗→C(X, F)∗.
For a cosimplicial group A∗, we put Ap
deg =
pP
i=0
Im(sp
i ), where sp
i : Ap+1 →Ap are
the degeneracy maps; then A•
deg is a subcomplex in the complex A• (however there is
no analogous inclusion of cosimplicial groups). It is well known that the quotient map
A• →A•/A•
deg is a quasiisomorphism.
We put A•
red = A•/A•
deg.
Any morphism of
simplicial groups f : A∗→B∗induces a morphism of complexes f : A•
red →B•
red.
9


## Page 10


Deﬁnition 2.9. For a scheme X and an abelian sheaf F on X, let the adelic complex
A(X, F)• be As(X, F)•
red.
It follows from Corollary 2.8 that for any sheaves F and G on X there is a morphism of
complexes A(X, F)• ⊗A(X, G)• →A(X, F ⊗G)• and that for any morphism of schemes
f : X →Y there is a morphism of complexes f ∗: A(Y, f∗F) →A(X, F). In particular,
if A is a sheaf of associative rings on X, then A(X, A)• is a DG-ring. Given a morphism
of schemes f : X →Y , we get a homomorphism of DG-rings A(Y, f∗A)• →A(X, A)•.
In addition, for any sheaf F, there is a natural inclusion Γ(X, F) ֒→H0(A(X, F)•).
Suppose that the scheme X is Noetherian of ﬁnite dimension d. Then it is easily
shown that
As(X, F)p =
Y
0≤i0≤...≤ip≤d
A((i0 . . . ip), F),
A(X, F)p =
Y
0≤i0<...<ip≤d
A((i0 . . . ip), F),
where the expression (i0 . . . ip) stands for the set of all ﬂags η0 . . . ηp on X such that for
any j, 0 ≤j ≤p, we have codim(ηj) = ij. We say that such ﬂags are of type (i0 . . . ip).
For example, A(X, F)0 =
Q
0≤p≤d
A((p), F) and A((p), F) = C((p), F) =
Q
η∈X(p) Fη. Thus
the adelic complex is bounded and has length d. In fact, the adelic complex is bounded
for any Noetherian scheme X of ﬁnite Krull dimension by the maximal dimension of the
irreducible components of X.
We may sheaﬁfy the above construction. Namely for any scheme X, an abelian sheaf
F on X, and a subset M ⊂S(X)p there is an abelian presheaf A(M, F)∗deﬁned by the
formula U 7→As(M(U), i∗
UF) (see Corollary 2.7(i)).
Proposition 2.10. If the scheme X is Noetherian, then the presheaf As(X, F) is actu-
ally a ﬂasque sheaf.
Proof. The ﬂasqueness of this presheaf follows from Corollary 2.7(i). Clearly, it is enough
to prove the sheaf property for the case of a ﬁnite open covering ∪αVα of X. In this case
we proceed by induction on p, using that for any collection of open subsets Uα ⊂Vα
containing a ﬁxed point η ∈X, the open subset ∩αUα ⊂X also contains η.
Thus if X is Noetherian, then we get the ﬂasque cosimplicial abelian sheaf As(X, F)∗
and the complexes of ﬂasque sheaves As(X, F)•, As(X, F)•
deg, and A(X, F)•. Moreover,
there is a morphism of complexes F →A(X, F)•, where F is considered as a complex
concentrated in the zero term.
Question 2.11. Under which conditions on F the complex of sheaves A(X, F)• is a
ﬂasque resolution of F?
Remark 2.12.
(i) Let F, G be two sheaves on a Noetherian scheme X; then the composition of the
morphisms of complexes F ⊗G →A(X, F)• ⊗A(X, G)• →A(X, F ⊗G)• is the
natural map described above.
10


## Page 11


(ii) Let f : X →Y be a morphism of Noetherian schemes, F be a sheaf on X; then
the composition of the morphisms of complexes f∗F →A(Y, f∗F)• →f∗A(X, F)•
coincides with the value of the functor f∗at the natural morphism F →A(X, F)•
described above.
In particular, if A is a sheaf of associative rings, then the map L
i≥0
Hi(X, A) →
L
i≥0
Hi(A(X, F)•) is a homomorphism of rings.
We will use the following explicit description of adelic groups on Noetherian schemes.
Let us introduce the following notation.
Deﬁnition 2.13. Let Z be a closed subscheme in a Noetherian scheme X and η be a
schematic point in X; then by Z(η) ⊂X(1) denote the set of irreducible reduced divisors
on X that are contained in Z and pass through η. Analogously, for a closed subset
W ⊂X, by Z(W) ⊂X(1) denote the set of irreducible reduced divisors on X that are
contained in Z and contain W.
Proposition 2.14. For any subset M ⊂S(X)p, we have
A(M, F) =
lim
−→
{Dη0...ηk }
Y
(η0...ηp)∈M
(FX\Dη0...ηp−1)ηp,
where the limit is taken over the set of systems {Dη0...ηk}, 0 ≤k < p of eﬀective, reduced,
possibly reducible divisors on X parameterized by ﬂags η0 . . . ηk that can be extended to
the right to a ﬂag from M with the following property. For any k, 0 < k < p and for any
“left part” (η0 . . . ηk) of a ﬂag from M, we have
Dη0...ηk−1(ηk) ⊇Dη0...ηk−1ηk(ηk)
(∗)
and Dη0(η0) = ∅. The partial order on the systems {Dη0...ηk}, 0 ≤k < p is given by the
ﬂag wise embedding of divisors in X.
Proof. Using Remark 2.5, one proves by induction on p that
A(M, F) =
lim
−→
{Uη0...ηk }
Y
(η0...ηp)∈M
(FUη0∩...∩Uη0...ηp−1)ηp,
where the limit is taken over the set of systems {Uη0...ηk}, 0 ≤k < p of open subsets in X
parameterized by “left parts” of ﬂags from M such that for any “left part” (η0 . . . ηk) of a
ﬂag from M, we have ηk ∈Uη0...ηk. The partial order on the systems {Uη0...ηk}, 0 ≤k < p
is given as the inverse to the ﬂag wise embedding of open subsets in X.
Since the scheme X is Noetherian, enlarging the complement X\Uη0...ηk, we may
assume that this complement is reduced, has pure codimension one, and does not contain
ηk. Finally, we put Dη0 = X\Uη0 and Dη0...ηk = Dη0...ηk−1 ∪X\Uη0...ηk for 1 ≤k < p.
Claim 2.15. Condition (∗) implies that
Dη0...ηk(ηj) ⊇Dη0...ηk...ηk+l(ηj)
for any 0 ≤j ≤k + 1, 0 ≤l ≤p −k −1.
11


## Page 12


Proof. It is enough to show this for l = 1. Each irreducible divisor D ∈Dη0...ηk,ηk+1(ηj)
contains ηk+1 and thus belongs to Dη0...ηk(ηk+1). Moreover, since D contains ηj, we see
that D also belongs to Dη0...ηk(ηj).
2.2
Relation with the Cousin complex
Let X be a Noetherian catenary scheme such that all irreducible components of X have
the same ﬁnite dimension d. For a closed subset Z ⊂X and a sheaf F on X, denote
by γZF the sheaf on Z such that if U ⊂X is an open subset, then (γZF)(U ∩Z)
consists of all sections in F(U) with support on U ∩Z. Thus, RγZ = i!
Z. One can
also apply functors RpγZ to complexes of sheaves on X. Following the notations from
[12], for any sheaf F on X and any point η ∈X(p), we put Hp
η(X, F) = (RpγηF)η. Let
νηξ : Hp
η(X, F) →Hp+1
ξ
(X, F) be the natural map deﬁned for any two points η, ξ ∈X
such that ξ ∈η and ξ has codimension one in η (see [12]). Let Cous(X, F)• be the
Cousin complex of F on X, i.e.,
Cous(X, F)p =
L
η∈X(p) Hp
η(X, F),
where the diﬀerential is the sum of the maps νηξ.
Let us sheaﬁfy the Cousin com-
plex, namely, consider the complex of sheaves Cous(X, F)• given by Cous(X, F)p =
L
η∈X(p)(iη)∗Hp
η(X, F), where for each point η ∈X(p) we consider Hp
η(X, F) as a constant
sheaf on η. There is a natural map of complexes F →Cous(X, F)•, where we consider
F as a complex concentrated in the zero term.
Let 0 ≤i0 < . . . < ip be a strictly increasing sequence of natural numbers; then the
depth of (i0 . . . ip) is the maximal natural number l ≥0 such that (i0 . . . il) = (0 . . . l) if
i0 = 0. Otherwise, the depth of (i0 . . . ip) equals −1.
Proposition 2.16. Let (i0 . . . ip) be a strictly increasing sequence of natural numbers
such that ip ≤d. Suppose that the depth of (i0 . . . ip) is l ≥0; then there exists a natural
map
ν0...l : A((01 . . . lil+1 . . . ip), F) →
L
η∈X(l) A((0(il+1 −l) . . . (ip −l)), RlγηCous(X, F)•),
where the right hand side is the direct sum of adelic groups on η ∈X(l). Moreover, for
any adele f ∈A((01 . . . lil+1 . . . ip), F) and any ﬂag ηlηil+1 . . . ηip of type (lil+1 . . . ip) on
X, we have
θ(ν0...l(f))ηlηil+1...ηip =
X
η0...ηl
(νηl−1ηl ◦. . . ◦νη0η1)(θ(f)η0...ηlηil+1...ηip),
where the sum in the left hand side is actually ﬁnite.
Proof. The proof is by induction on l. For l = 0, by Proposition 2.7(iii), (iv), (v), we
have the natural map
A((0i1 . . . ip), F) =
L
η∈X(0) A((0i1 . . . ip)(η), i∗
ηF) =
L
η∈X(0) A((0i1 . . . ip), γηF) →
12


## Page 13


→
L
η∈X(0) A((0i1 . . . ip), γηCous(X, F)•).
Further, note that for the composition of closed embeddings Z′ ⊂Z ⊂X, where
Z has pure codimension l in X and Z′ has pure codimension one in Z, the natural
morphism of complexes
RlγZCous(X, F)• →γZCous(X, F)•[l]
induces the morphism of sheaves
R1γZ′Z(RlγZCous(X, F)•) →R1γZ′Z(γZCous(X, F)•[l]) = Rl+1γZ′Cous(X, F)•.
Therefore, to prove the proposition by induction on l, it is enough to consider the case
l = 1 and X is irreducible. Recall that for any closed subscheme D ⊂X, there is a
morphism of sheaves FU →(iD)∗R1γDF, where U = X\D. Hence, using the same
argument as for the case l = 0, we get the map
A((01i2 . . . ip), F) = lim
−→
U
A((1i2 . . . ip), FU) →
lim
−→
D=X\U
A((1i2 . . . ip), (iD)∗R1γDF) =
= lim
−→
D
A(0(i2 −1) . . . (ip −1)), R1γDF) =
L
η∈X(1) A((0(i2 −1) . . . (ip −1)), R1γηF) →
→
L
η∈X(1) A((0(i2 −1) . . . (ip −1)), R1γηCous(X, F)•),
where the second limit is taken over all closed subschemes D ⊂X of pure codimension
one.
Remark 2.17. It seems that it is impossible to replace in the formulation of Proposi-
tion 2.16 the sheaf RlγZCous(X, F)• by a more natural sheaf RlγZF.
At least the
induction step in the above proof will not be valid, because in general there is no map
R1γZ′Z(RlγF) →Rl+1γZ′F in notations from the proof of Proposition 2.16.
Example 2.18. Suppose that l = p; then we get the map νp = ν0...p: A((0 . . . p), F) →
L
η∈X(p) Hp
η(X, F).
There is a morphism of complexes
νX : A(X, F)• →Cous(X, F)•
that is equal to the map (−1)
p(p+1)
2
νp on the (0 . . . p)-type components of the adelic
complex and equals zero on all the other components of the adelic complex.
Also, for any two sheaves F and G on X and a point η ∈X(p), we have the natural
morphism
Hp
η(X, F) ⊗A(X, G)q = A((p), (iη)∗RpγηF) ⊗A(X, G)q →A(η, Rpγη(F ⊗G))q
νη
−→
νη
−→L
ξ∈η(q) Hq
ξ(η, Rpγη(F ⊗G)) ⊂
L
ξ∈X(p+q) Hp+q
ξ
(X, F ⊗G).
13


## Page 14


It is easily checked that this deﬁnes a morphism of complexes
µ : Cous(X, F)• ⊗A(X, G)• →Cous(X, F ⊗G)•
given by the formula
µ(f ⊗g)η = (−1)ǫ(p,q)
X
η0...ηq−1
(νηq−1η ◦. . . ◦νη0η1)(fη0 · θ(g)η0...ηq−1η)
for any f ∈Cous(X, F)p, g ∈A(X, G)q, and η ∈X(p+q), where the sum is taken over all
ﬂags η0 . . . ηq−1 of type (p, p + 1 . . . , p + q −1) such that η ∈ηq−1 and fη0 · θ(g)η0...ηq−1η ∈
Hp
η(X, F ⊗G), and ǫ(p, q) = pq + q(q+1)
2
.
Remark 2.19. The analogous product is well deﬁned of one replaces F by a complex of
abelian sheaves F •.
Remark 2.20. A coherent version of the product between the Cousin and the adelic
complex was considered in [27].
Example 2.21. Multiplication of the adelic complex on the right by 1 ∈Z = Z(X)
coincides with the morphism νX.
In particular, if A is a sheaf of associative rings on X, then Cous(X, A)• is a right
DG-module over the DG-ring A(X, A)•.
Remark 2.22. Evidently, we also have the morphism of complexes of sheaves νX :
A(X, F)• →Cous(X, F)•. Suppose that the sheaf F on X is Cohen–Macaulay in the
sense of [12], i.e., that the composition F →A(X, F)• →Cous(X, F)• is a quasiisomor-
phism; then for any i ≥0, the cohomology group Hi(X, F) is a direct summand in the
group Hi(A(X, F)•). One may expect that the map F →A(X, F)• is a quasiisomor-
phism for any Cohen–Macaulay sheaf F. For the particular case of this statement see
Theorem 3.34. In particular, if A is a Cohen–Macaulay sheaf of associative rings, then the
ring L
i≥0
Hi(X, A) is a direct summand as a ring in the associative ring L
i≥0
Hi(A(X, A)•).
The next statement is needed for the sequel.
Lemma 2.23. Suppose that X is a Noetherian catenary scheme such that all irreducible
components of X have the same ﬁnite dimension d. Let F be a Cohen–Macaulay sheaf
on X (see [12]); then for any p, 0 ≤p ≤d, the map νp : L
η0...ηp
Fη0 →
L
η∈X(p) Hp
η(X, F) is
surjective, where the ﬁrst direct sum is taken over all ﬂags of type (0 . . . p) on X.
Proof. The proof is by induction on p. For p = 0, there is nothing to prove. Suppose
that p > 0.
Consider a collection {fη} ∈
L
η∈X(p) Hp
η(X, F).
Note that for any point
η ∈X(p), the sheaf j∗
ηF is Cohen–Macaulay on Xη, where jη : Xη = Spec(OX,η) →X is
the natural morphism. Hence for each point η ∈X(p), there exists a collection {gξ}(η) ∈
L
η∈X(p−1)
η
Hp−1
ξ
(Xη, j∗
ηF) such that dη{gξ}(η) = fη, where dη denotes the diﬀerential in the
14


## Page 15


Cousin complex on Xη. We may suppose that {gξ}(η) = 0 for almost all η ∈X(p). By
the induction hypothesis, for each point η ∈X(p), there exists a collection {gξ0...ξp−1}(η) ∈
L
ξ0...ξp−1
Fξ0 such that νp−1{gξ0...ξp−1}(η) = {gξ}(η), where the direct sum is taken over all
ﬂags of type (0 . . . p−1) on Xη. Again, we may suppose that {gξ0...ξp−1}(η) = 0 for almost
all η ∈X(p). Finally, we put {fη0...ηp} = {gη0...ηp−1}(ηp).
2.3
Projection formula
Let X, Y
be Noetherian catenary irreducible schemes, f
: X
→Y
be a mor-
phism such that for any point η ∈X, we have dim(η) ≥dim(f(η)).
Under the
above hypothesis, for any sheaf F on X, there is a canonical morphism of complexes
Cous(X, F)• →Cous(Y, Rf∗F[d])•, where d = dim(f) = dim(X) −dim(Y ). The deﬁni-
tion of this morphism uses inclusions of complexes ΓZ(X, C(F)•) ֒→Γf(Z)(Y, f∗C(F)•)
for any closed subset Z ⊂X, where C(F)• is a ﬂasque resolution of F on X.
The morphism Cous(X, F)• →Cous(Y, Rf∗F[d])• consists of homomorphisms of type
f∗: Hp
η(X, F) →Hp−d
f(η)(X, Rf∗F[d]), where dim(η) = dim(f(η)).
The following adelic projection formula holds true.
Proposition 2.24. Let f : X →Y be as above and let F, G be two sheaves on X;
then the following natural diagram commutes up to the sign (−1)d·degA, where degA is
the degree of the components in the adelic complex:
Cous(X, F)• ⊗A(Y, f∗G)•
=
Cous(X, F)• ⊗A(Y, f∗G)•
↓
↓
Cous(X, F)• ⊗A(X, G)•
Cous(Y, Rf∗F[d])• ⊗A(Y, G)•
↓
↓
Cous(X, F ⊗G)•
−→
Cous(Y, Rf∗(F ⊗G)[d])•.
Proof. For any point η ∈X(p) such that dim(η) = dim(f(η)), the following diagram
commutes
Hp
η(X, F) ⊗(f∗G)f(η)
=
Hp
η(X, F) ⊗(f∗G)f(η)
↓
↓
Hp
η(X, F) ⊗Gη
Hp−d
f(η)(Y, Rf∗F[d]) ⊗(f∗G)f(η)
↓
↓
Hp
η(X, F ⊗G)
−→
Hp−d
f(η)(Y, Rf∗(F ⊗G)[d]),
where f(η) ∈Y (q). Hence the proposition follows from Lemma 2.25 and the explicit
formula for the product between the Cousin and the adelic complexes.
Lemma 2.25. Let f : X →Y be as above with dim(X) = dim(Y ), H be a sheaf on X,
and (ξ0 . . . ξr) be a ﬂag on Y such that ξl ∈Y (l) for all l, 0 ≤l ≤r; then for any element
h ∈HX, we have
f∗
 X
η0...ηr
νη0...ηr(h)
!
= νξ0...ξr(f∗(h)),
15


## Page 16


where f∗: H∗
η(X, H) →H∗−d
f(η)(Y, Rf∗H[d]) are the natural homomorphisms and the sum
is taken over all ﬂags η0 . . . ηr on X such that f(η0 . . . ηr) = (ξ0 . . . ξr) and ηl ∈X(l) for
all l, 0 ≤l ≤r.
Proof. The proof is by induction on r. Note that there are only ﬁnitely many schematic
points η1 ∈X(1) such that f(η1) = ξ1. Hence, if we replace X and Y by η1 and ξ1,
respectively, we see that the induction step is equivalent to the case r = 1. On the other
hand, when r = 1 the residue maps νη0η1 and νξ0ξ1 correspond to the diﬀerentials in
the Cousin complexes Cous(X, H)• and Cous(Y, Rf∗H[d])∗. Therefore Lemma 2.25 is
equivalent to the fact that the homomorphisms f∗deﬁne a morphism of the corresponding
Cousin complexes.
2.4
Sheaves with controllable support
Deﬁnition 2.26. We say that a sheaf F on a scheme X has controllable support if
for any point η ∈X, there exists a closed subset Zη ⊂X such that η /∈Zη and
lim
−→(iZ)∗γZF = (iZη)∗γZηF, where the limit is taken over all closed subsets Z ⊂X such
that η /∈Z.
Remark 2.27.
(i) If F has controllable support, then for any open subset U ⊂X the sheaf FU has also
controllable support (indeed, for any closed subset Z ⊂X we have (iZ)∗γZ(FU) =
((iZ)∗γZF)U;
(ii) any subsheaf in a sheaf with controllable support has also controllable support.
Examples 2.28.
1) If X has ﬁnitely many irreducible components, then a constant sheaf on X has
controllable support.
2) If F is a coherent sheaf on a Noetherian scheme X, then F has controllable support.
Indeed, all sheaves (iZ)∗γZF in the deﬁnition are coherent subsheaves in the sheaf F.
3) Any Cohen–Macaulay sheaf on a Noetherian scheme has controllable support.
4) Let X be an irreducible one-dimensional scheme with inﬁnitely many closed
points. Consider the sheaf L
x∈X
(ix)∗Z, where x ranges over all closed points in X and
ix : Speck(x) ֒→X is the closed embedding of a point. Then the sheaf L
x∈X
(ix)∗Z does
not have controllable support.
Claim 2.29. If a sheaf F on a scheme X has controllable support, then for any point
η ∈X there exists an open subset Uη ⊂X containing η such that for any open subsets
V ⊂U ⊂Uη containing η the natural morphism of sheaves FU →FV is injective.
Proof. We have Ker{FU →FV } = ((iZ)∗γZF)U, where Z = X\V . We put Uη = X\Zη;
since Zη ⊂Z and U ⊂X\Zη, we get ((iZ)∗γZF)U = ((iZη)∗γZηF)U = 0.
16


## Page 17


Proposition 2.30. Suppose that the sheaf F on a scheme X has controllable support;
then the map θ is injective for any subset M ⊂S(X)p:
θ : A(M, F) ֒→C(M, F) =
Y
(η0...ηp)∈M
Fη0.
Proof. The proof is by induction on p. For p = 0, there is nothing to prove. Suppose
that p > 0; then, by the induction hypothesis, we have
A(M, F) =
Y
η∈P (X)
lim
−→
Uη
A(ηM, FUη) ֒→
Y
η∈P (X)
lim
−→
Uη
Y
(η1...ηp)∈ηM
(FUη)η1 ֒→
֒→
Y
η∈P (X)
Y
(η1...ηp)∈ηM
lim
−→
Uη
(FUη)η1 =
Y
(η0...ηp)∈M
Fη,
where the injectivity of the second map follows from Claim 2.29.
Thus when F has controllable support, each adele f ∈A(M, F) is uniquely deter-
mined by its components fη0...ηp ∈Fη0, where (η0 . . . ηp) runs over ﬂags in M.
Remark 2.31. Let F be a sheaf with controllable support on a scheme X; then for any
subset M ⊂S(X)p, there is a natural inclusion
L
(η0...ηp)∈M
Fη0 ⊂A(M, F).
Examples 2.32. Let F be a sheaf with controllable support on X. For an irreducible
closed subscheme Z ⊂X, by FZ denote the stalk of F at the generic point of Z.
1) Suppose that dimX = 1; then the adelic group A((01), F) ⊂Q
x∈X
FX consists of
all collections {fXx} ∈Q
x∈X
FX such that fXx ∈Im(Fx →FX) for almost all x ∈X. In
particular, we get rational adeles on a curve if F = OX (see [24], where rational adeles
are called repartitions).
2) Suppose that dimX = 2.
Let us describe explicitly the arising adelic groups.
The adelic group A((01), F) ⊂Q
C⊂X
FX consists of all collection {fXC} such that fXC ∈
Im(FC →FX) for almost all irreducible curves C ∈X. The adelic group A((12), F) ⊂
Q
x∈C
FC consists of all collections {fCx} such that fCx ∈Im(Fx →FC) for almost all points
x ∈C for a ﬁxed C. The adelic group A((02), F) ⊂Q
x⊂X
FX consists of all collections
{fXx} such that there exists a divisor D ⊂X such that fXx ∈Im((FX\D)x →FX)
for any closed point x ∈X. The adelic group A((012), F) ⊂
Q
x∈C⊂X
FX consists of all
collections {fXCx} satisfying the following condition. There exists a divisor D ⊂X and
for each irreducible curve C ⊂X, there is a divisor DC such that DC(C) = D(C) (see
Deﬁnition 2.13), and fXCx ∈Im((FX\DC)x →FX) for all ﬂags x ∈C ⊂X. This is
analogous to the construction given in [19], p. 751.
17


## Page 18


2.5
1-pure sheaves
Deﬁnition 2.33. We say that a sheaf F on a Noetherian scheme X is 1-pure if for any
point η ∈X(i), we have H0
η(X, F) = 0 if i ≥1 and also H1
η(X, F) = 0 if i ≥2.
Equivalently, a sheaf F is 1-pure if the following complex of sheaves is exact:
0 →F →Cous(X, F)0 →Cous(X, F)1.
Remark 2.34. For any open subset U ⊂X, any point ξ ∈P(X), and a 1-pure sheaf F
on X, there are exact sequences of sheaves
0 →FU →
L
η∈X(0)(iη)∗Fη →
L
η∈D(X\U)
(iη)∗H1
η(X, F),
0 →[F]ξ →
L
η∈X(0)(iη)∗Fη →
L
η∈D(ξ)
(iη)∗H1
η(X, F),
where D(X\U) is the set of codimension one points in X that belong to the complement
X\U and D(ξ) is the set of codimension one points η in X such that ξ ∈η. In particular,
the sheaves FU and [F]ξ are 1-pure for any 1-pure sheaf F.
Remark 2.35. It is easily shown that for a sheaf F on a Noetherian scheme X, the sheaf
L
η∈X(0)(iη)∗Fη has controllable support. Hence any 1-pure sheaf on a Noetherian scheme
has controllable support.
For any ﬂag F
=
(η0 . . . ηi) and a subset M
⊂
S(X)p, we put
FM
=
ηi(ηi−1(. . .η0 (M))).
Proposition 2.36. Let F be a 1-pure sheaf on a Noetherian irreducible scheme X.
Suppose that the subset M ⊂S(X)p and a natural number l, 0 ≤l ≤p satisfy the
following condition: either p ≤l + 1, or for any ﬂag F = (η0 . . . ηl+1) ∈S(X)p+1, we
have FM = ηl+1(δp−l
0
. . . δp
l (M)) or FM = ∅. Then the boundary maps C(δp
l (M), F) →
C(M, F) and A(δp
l (M), F) →A(M, F), 0 ≤l ≤p (see Proposition 2.6(ii)) are injective
and we have
A(δp
l (M), F) = A(M, F) ∩C(δp
l (M), F),
where the intersection is taken inside the group C(M, F).
Proof. Since X is irreducible, the sheaf F is a subsheaf in a constant sheaf and for any
points η, ξ ∈X and any open subset U such that ξ ∈η, η ∈U, and U is connected, the
natural morphisms Fξ →Fη and F(U) →Fη are injective. Thus we get the injectivity
of the boundary maps for the direct product groups and hence, by Proposition 2.30, we
get the injectivity of the boundary maps for the adelic groups. In particular, the left
hand side of the equality is contained in the right hand side.
To prove the backward inclusion we use induction on p and l. For p = 1 and l = 0, 1,
we have A(δ1
l (M), F) = C(δ1
l (M), F) and the assertion is clear.
Suppose that p > 1, l = 0. Denote by A the right hand side of the needed equality.
For each η ∈P(X), consider the image Aη of A under the natural map C(δp
0(M), F) →
18


## Page 19


C(ηM, F), see Proposition 2.6(i).
The group Aη coincides with the projection of A
on the η-part in the direct product C(M, F) =
Q
η∈P (X)
C(ηM, [F]η) and hence Aη =
lim
−→
Uη
A(ηM, FUη) ∩C(ηM, F), where the intersection is taken in the group C(ηM, [F]η).
Therefore, by Lemma 2.40, Aη = A(ηM, F). Further, note that δ0
p(M) =
S
η∈P (X)
ηM and
for any point ξ ∈P(X) there exists η ∈P(X) such that ξ(ηM) =ξ (δp
0(M)). Therefore,
by Lemma 2.41, A = A(δp
0(M), F).
Suppose that p > 1, l > 0; then, by deﬁnition, the right hand side is equal to
Y
η∈P (X)
lim
−→
Uη
A(ηM, FUη) ∩C(δp
l (M), F) =
Y
η∈P (X)
 
lim
−→
Uη
A(ηM, FUη) ∩C(ηδp
l (M), [F]η)
!
.
Since l > 0, for each point η ∈P(X), we have ηδp
l (M) = δp
l−1(ηM). On the other hand, by
Proposition 2.30, A(ηM, FUη) ⊂C(ηM, FUη) and the intersection corresponding to the
point η is actually contained in the subgroup lim
−→
Uη
C(δp
l−1(ηM), FUη) ⊂C(δp
l−1(ηM), [F]η).
Hence, by the inductive assumption for FUη, ηM, p −1, and l −1, the intersection
considered above is equal to
Y
η∈P (X)
lim
−→
Uη
 A(ηM, FUη) ∩C(δp
l−1(ηM), FUη)

=
Y
η∈P (X)
lim
−→
Uη
A(δp
l−1(ηM), FUη) = A(δp
l (M), F).
Remark 2.37. It follows from the proof of Proposition 2.36 that for any subsheaf F
of a constant sheaf on a scheme X with ﬁnitely many irreducible components, for any
M ⊂S(X)p, and for any l, 0 ≤l ≤p, there is the inclusion
A(δp
l (M), F) ⊂A(M, F) ∩C(δp
l (M), F).
Remark 2.38. The condition that F is 1-pure in Proposition 2.36 might be replaced by
a weaker condition but actually we do not need such improvement: all sheaves that we
consider further are 1-pure. The same is true about the condition on the set M.
Example 2.39. Suppose that X is irreducible and dim(X) = 2. Let D ⊂X be a closed
irreducible codimension one subset with inﬁnitely many closed points. We put G = L
y∈D
Z,
where the sum is taken over all closed points y on D.
Let F be the kernel of the
natural map G →L
y∈D
(iy)∗Z of sheaves on X.
Then F is a subsheaf in a constant
sheaf but is not 1-pure on X. Further, consider the adele f ∈C((12), F) deﬁned by
fCx = {1x} ∈G if C = D and fCx = 0 otherwise. For C = D, we have fCx ∈(FX\{x})x
and there are two inclusions (FX\{x})x ⊂(FX\C)x and (FX\{x})x ⊂FC.
Therefore,
f ∈A((012), F) ∩C((12), F) but f /∈A((12), F).
19


## Page 20


Lemma 2.40. Let F be 1-pure sheaf on a Noetherian scheme X. Consider the sheaf
G = FV for some open subset V ⊂X. Then for any subset M ⊂S(X)p, we have
A(M, G) ∩C(M, F) = A(M, F),
where the intersection is taken in the group C(M, G).
Proof. The proof is by induction on p.
For p
=
0,
there is nothing to
prove.
Suppose that p > 0; then, by deﬁnition, the left hand side is equal to
Q
η∈P (X)
 
lim
−→
Uη
A(ηM, GUη) ∩C(ηM, [F]η)
!
.
Consider a point η ∈P(X) and an open subset U ⊂X containing η. Suppose that
U is small enough so that all irreducible components of U\V contain η and the natural
morphisms FU →[F]η, GU →[G]η are injective. It follows from the explicit description
given in Remark 2.34 that GU ∩[F]η = FU, where the intersection is taken inside the
sheaf [G]η. Therefore C(N, GU) ∩C(N, [F]η) = C(N, FU) for any subset N ⊂S(X)q.
Consequently the intersection lim
−→
Uη
A(ηM, GUη) ∩C(ηM, [F]η) is actually contained in
the subgroup lim
−→
Uη
C(ηM, FUη) ⊂C(ηM, [F]η) and, by the inductive hypothesis, we get
the needed statement.
Lemma 2.41. Let F be a sheaf with controllable support on a scheme X and let N be
a subset in S(X)p such that N = S
α
Nα, where Nα ⊂S(X)p for each α. Suppose that
for any point η ∈P(X) there exists α such that η(Nα) = ηN. Let A be a subgroup in
C(N, F) such that for any α, the image of A under the natural map C(N, F) →C(Nα, F)
is contained inside A(Nα, F). Then A ⊂A(N, F).
Proof. For a point η ∈P(X) let α be such that η(Nα) = ηN. Then the projection
of A to the group C(ηN, [F]η) = C(η(Nα), [F]η) from the direct product C(N, F) =
Q
η∈P (X)
C(ηN, [F]η) is contained in the group lim
−→
Uη
A(η(Nα), FUη) = lim
−→
Uη
A(ηN, FUη). Thus
we get that A ⊂A(N, F).
Let X be a Noetherian scheme. Consider an increasing sequence of natural numbers
i0 ≤. . . ≤ip. Recall that (i0 . . . ip) denotes the set of all ﬂags from S(X)p of type
(i0 . . . ip). For any l, 0 ≤l ≤p, we have δp
l (i0 . . . ip) = (i0 . . .ˆıl . . . ip). From this one de-
duces that the subset (i0 . . . ip) ⊂S(X)p satisﬁes the condition from Proposition 2.36 for
any l, 0 ≤l ≤p. Let (j0 . . . jq) be a subsequence in (i0 . . . ip), q ≤p. There are canonical
maps α : C((j0 . . . jq), F) →C((i0 . . . ip), F) and β : A((j0 . . . jq), F) →A((i0 . . . ip), F)
that are compositions of the corresponding boundary maps. By Proposition 2.36, we get
the following.
Corollary 2.42. Let F be a 1-pure sheaf on a Noetherian irreducible scheme X. Then
for any sequences (i0 . . . ip) and (j0 . . . jq) as above, the maps α and β are injective and
we have
A((j0 . . . jq), F) = A((i0 . . . ip), F) ∩C((j0 . . . jq), F),
where the intersection is taken inside the group C((i0 . . . ip), F).
20


## Page 21


In what follows we will always imply the inclusion β when comparing adelic groups
with diﬀerent indices given by type.
2.6
A′-adelic groups
We introduce a new type of adelic groups. Let X be a Noetherian catenary scheme such
that all irreducible components of X have the same ﬁnite dimension d and let F be an
abelian sheaf on X.
Consider a strictly increasing sequence of natural numbers (i0, . . . , ip) such that ip ≤
d. Recall that C((i0 . . . ip), F) =
Y
η0...ηp
Fη0, where the product is taken over all ﬂags of
type (i0 . . . ip) on X. We put l to be the depth of (i0 . . . ip) (see Proposition 2.16).
Deﬁnition 2.43. Let the subgroup A′((i0 . . . ip), F) ⊆C((i0 . . . ip), F) consist of all ele-
ments f ∈C((i0 . . . ip), F) such that for any number m, 0 ≤m ≤l and a ﬂag ηm+1 . . . ηp
of type (im+1 . . . ip) on X, there are only ﬁnitely many ﬂags η0 . . . ηm of type (0 . . . m) on
X such that the composition of the residue maps (νηm−1ηm ◦. . . ◦νη0η1)(fη0...ηmηm+1...ηp) ∈
Hm
ηm(X, F) is not zero. These new adelic groups are called A′-adelic groups, while the
old adelic groups will be called A-adelic groups.
When l = −1, we have A′((i0 . . . ip), F) = C((i0 . . . ip), F). When l ≥0, for any
number m, 0 ≤m ≤l, there is a map
ν′
0...m : A′((i0 . . . ip), F) →
Y
ηm+1...ηp
 
L
η∈X(m)Hm
η (X, F)
!
,
where for each ﬂag ηm+1 . . . ηp of type (im+1 . . . ip) on X, the direct sum is taken over all
points η ∈X(m) such that ηm+1 ∈η (compare with Proposition 2.16).
Remark 2.44.
(i) By Proposition 2.16, the image θ(A((i0 . . . ip), F)) ⊂C((i0 . . . ip), F) is contained
in A′(i0 . . . ip), F).
(ii) It is readily seen that the analogue of Corollary 2.7(i), (ii) with M = (i0 . . . ip)
holds for the A′-adelic groups.
(iii) By reciprocity law, for any j, 0 ≤j ≤p, the boundary map
dp
j : C((i0 . . .ˆıj . . . ip), F) →C((i0 . . . ip), F)
induces the map of the corresponding A′-groups; deﬁne the A′-adelic complex
A′(X, F)• by formula
A′(X, F)p =
Y
0≤i0<...<ip≤d
A((i0 . . . ip), F)
21


## Page 22


and with the diﬀerential induced from the complex C(X, F)•
red; we have the mor-
phism of complexes A′(X, F)•
ν′
X
−→Cous(X, F)• deﬁned in the same way as for
the A-adelic complex; the composition A(X, F)• →A′(X, F)• →Cous(X, F)• is
equal to νX.
(iv) Given two sheaves F, G on X, the morphism of complexes C(X, F)•
red ⊗
C(X, G)•
red →C(X, F⊗G)•
red does not induce a morphism of complexes A′(X, F)•⊗
A′(X, G)• →A′(X, F ⊗G)•; also, the analogue of Corollary 2.42 is not true for the
A′-adelic groups.
(v) We may consider the sheaﬁﬁed version A′(X, F)• of the A′-adelic complex; there
is a natural morphism of complexes F →A′(X, F)•.
Lemma 2.45. For any natural numbers i0, . . . , il, p such that 0 ≤i0 < . . . < il < p ≤d
and (i0 . . . il) ̸= (0 . . . (p −1)), we have
A′((i0 . . . ilp), F) =
Y
η∈X(p)
A′((i0 . . . ilη), F),
where the index (i0 . . . ilη) stands for the set of all ﬂags η0 . . . ηlηp on X of type (i0 . . . ilp)
such that ηp = η. Also, we have
A′((0 . . . (p −1)p), F) =
Y
η∈X(p)
A′((0 . . . (p −1)η), F),
where the restricted product means that we consider the set of all collections {fη} ∈
Q
η∈X(p) A′((0 . . . (p −1)η), F) such that for almost all points η ∈X(p), the A′-adele fη ∈
A′((0 . . . (p −1)η), F) ⊂A′((0 . . . (p −1)p), F) belongs to Ker(ν0...p).
Proof. This follows immediately from the deﬁnition of A′-adelic groups combined with
the A′-analogue of Corollary 2.7(ii) (see Remark 2.44(ii)).
The lack of the multiplicative structure is the main disadvantage of the A′-adelic com-
plex (see Remark 2.44(iv)). Nevertheless, the main advantage of the A′-adelic complex
is the following statement.
Theorem 2.46. Suppose that X is a Noetherian catenary scheme such that all irreducible
components of X have the same ﬁnite dimension d and the sheaf F on X is Cohen–
Macaulay in the sense of [12]. Then the morphism ν′
X : A′(X, F)• →Cous(X, F)• is a
quasiisomorphism.
Corollary 2.47. Under the assumptions from Theorem 2.46, the natural morphism F →
A′(X, F)• is a quasiisomorphism.
22


## Page 23


Proof of Theorem 2.46. It is enough to prove that the morphism ν′
U : A′(U, F|U)• →
Cous(U, F|U)• is a quasiisomorphism for any open subset U ⊂X. The sheaf F|U is
Cohen–Macaulay on U, hence we may suppose that U = X.
Using several intermediate complexes, we transform the A′-adelic complex into the
Cousin complex. For each number p, 0 ≤p ≤d, consider the following complex:
C•
p : 0 →
Y
0≤i≤p
A′((i), F) →. . . →
Y
0≤i0<...il≤p
A′((i0 . . . il), F) →. . . →A′((0 . . . p), F) →
→
L
η∈X(p+1) Hp+1
η
(X, F) →. . . →
L
η∈X(d) Hd
η(X, F).
The diﬀerential in the ﬁrst part of this complex coincides with that in the A′-adelic
complex, the diﬀerential in the second part coincides with that in the Cousin complex,
and the diﬀerential in the middle A′((0 . . . p), F) →
L
η∈X(p+1) Hp+1
η
(X, F) is equal to the
composition of the boundary map A′((0 . . . p), F) →A′((0 . . . p, (p + 1)), F) with the
map ν′
0...(p+1). Thus C•
0 = Cous(X, F)• and C•
d = A′(X, F)•.
For each p, 1 ≤p ≤d, there is a natural morphism of complexes ϕp : C•
p →C•
p−1 that
is equal to the natural projection for the ﬁrst part of the complex C•
p, is equal to ν′
0...p
for the p-th terms of C•
p, and is equal to the identity maps for the second part of the
complex C•
p. We have ϕ1 ◦. . .◦ϕd = ν′
X. We prove by induction on p that the morphism
ϕp is actually a quasiisomorphism for all X and F as above.
For p = 0, there is nothing to prove. Suppose that 1 ≤p ≤d = dim(X). By Lemma
2.23, the morphism ϕp is surjective. So we need to show that the kernel of ϕp is an exact
complex. By construction, Ker(ϕp)• is equal to the complex
0 →A′((p), F) →
Y
0≤i<p
A′((ip), F) →. . . →
Y
0≤i0<...<il<p
A′((i0 . . . ilp), F) →. . .
. . . →
Y
0≤i<p
A′((0 . . .ˆı . . . p), F) →Ker(ν′
0...p) →0.
For each schematic point η ∈X(p), consider the natural morphism jη
: Xη
=
Spec(OX,η) →X. Note that j∗
ηF is Cohen–Macaulay on Xη. Hence, by the induction
hypothesis, the following complex is exact:
0 →Fη →
Y
0≤i<p
A′((i), j∗
ηF) →. . . →
Y
0≤i0<...<il<p
A′((i0 . . . il), j∗
ηF) →. . .
. . . →A′((0 . . . (p −1)), j∗
ηF) →Hp
η(X, F) →0.
Now we take the product of these complexes over all points η ∈X(k). We get the
exact complex
B•
p : 0 →
Y
η∈X(p)
Fη →. . . →
Y
η∈X(p)
 
Y
0≤i0<...<il<p
A′((i0 . . . ilη), j∗
ηF)
!
→. . .
23


## Page 24


. . . →
Y
η∈X(p)
A′((0 . . . (p −1)η), j∗
ηF)
ν′
0...p
−→
L
η∈X(p) Hp
η(X, F) →0,
where the restricted product is taken in the same sense as in Lemma 2.45 and, as above,
the index (i0 . . . ilηp) means that we consider the set of all ﬂags η0 . . . ηlηp on X of type
(i0 . . . ilp) with ﬁxed ηp. Finally, by Lemma 2.45, we see that Ker(ϕp)• = τ≤p(B•
p), where
τ≤p is the canonical truncation of a complex, and thus the complex Ker(ϕp)• is exact.
The following technical result is needed for the sequel.
For any adele h and an
increasing sequence of natural numbers (j0 . . . jq), by hj0...jq denote the component of h
that has type (j0 . . . jq).
Lemma 2.48. Under the assumptions from Theorem 2.46, consider an increasing se-
quence (0 . . . lil+1 . . . ip) of depth l and an adele g ∈A′((0 . . . lil+1 . . . ip), F) such that
ν′
0...(l+1)(g) = 0. Then there exists an adele h ∈
Q
0≤i≤l
A′((0 . . .ˆı . . . lil+1 . . . ip), F) such
that (dh)0...lil+1...ip = g, where d is the diﬀerential in the A′-adelic complex.
Proof. We use notations from the proof of Theorem 2.46.
Fix a ﬂag ηl+1 . . . ηp of
type (il+1 . . . ip). We have g0...lηl+1...ηp ∈A′((0 . . . l), j∗
ηl+1F). By the condition of the
lemma, g0...lηl+1...ηp is a degree l cocycle in the complex C•
l constructed for the lo-
cal scheme Xηl+1 and the sheaf j∗
ηl+1F.
It follows from the proof of Theorem 3.34
that the complex C•
l is exact for Xηl+1 and j∗
ηl+1F.
Therefore there exists an adele
hηl+1...ηp ∈
Q
0≤i≤l
A′((0 . . .ˆı . . . l), j∗
ηl+1F) such that dηl+1(hηl+1...ηp)0...l = f0...lηl+1...ηp, where
dηl+1 is the diﬀerential in the A′-adelic complex on Xηl+1. By Lemma 2.45, the collection
h = {hηl+1...ηp} ∈
Y
ηl+1...ηp
Y
0≤i≤l
A′((0 . . .ˆı . . . l), j∗
ηl+1F)
belongs to the A′-adelic group
Q
0≤i≤l
A′((0 . . .ˆı . . . lil+1 . . . ip), F) and h satisﬁed the
needed condition.
3
Adeles for homology sheaves
We give some particular example of a class of sheaves on a smooth variety X over a ﬁeld
such that for any sheaf F from this class the morphism of complexes of sheaves F →
A(X, F)• is a quasiisomorphism, i.e., the adelic complex is in fact a ﬂasque resolution for
the sheaf F. This class of sheaves naturally arises from homology theories. In addition,
these sheaves are Cohen–Macaulay in the sense of [12] (see Corollary 3.9(i)).
3.1
Homology theories
Let k be a ﬁeld and Vk be the category of varieties over k.
24


## Page 25


Deﬁnition 3.1. A weak homology theory over k is a presheaf on Vk in the Zariski
topology with value in the category of graded abelian groups
X 7→L
n∈Z
Fn(X),
(j : U ֒→X) 7→(j∗: Fn(X) →Fn(U))
such that for any closed embedding f : X′ ֒→X, there is a functorial homomorphism of
graded abelian groups f∗: Fn(X′) →Fn(X) satisfying the following axioms:
(WH1): for any open embedding j : U ֒→X and a closed embedding f : X′ ֒→X, the
following diagram commutes:
Fn(U′)
(j′)∗
←−
Fn(X′)
↓f∗
↓f∗
Fn(U)
j∗
←−
Fn(X),
where j′ : U′ = f −1(U) ֒→X′ is an open embedding;
(WH2): for any closed embedding i : Z ֒→X there exists a long exact localization sequence
. . . →Fn(Z)
i∗
−→Fn(X)
j∗
−→Fn(X\Z)
∂XZ
−→Fn−1(Z) →. . . ,
where j : X\Z ֒→X is an open embedding; in addition, for any for any closed
embedding f : X′ ֒→X and any pair of closed subsets i : Z ֒→X, i′ : Z′ ֒→X′
such that f(Z′) ⊆Z, the following diagram commutes:
. . . →
Fn(Z′)
i′
∗
−→
Fn(X′)
(j′)∗
−→
Fn(X′\Z′)
∂X′Z′
−→
Fn−1(Z′)
→. . .
↓f∗
↓f∗
↓f∗α∗
↓f∗
. . . →
Fn(Z)
i∗
−→
Fn(X)
j∗
−→
Fn(X\Z)
∂XZ
−→
Fn−1(Z)
→. . . ,
where α : f −1(X\Z) ֒→X\Z is an open embedding.
Note that this is a modiﬁed version of the notion of a twisted homology theory
from [5].
Let F∗be a weak homology theory over a ﬁeld k. For an irreducible variety X over
k and n ∈Z, we put Fn(k(X)) = lim
−→
U
Fn(U), where the limit is taken over all open
non-empty subsets U ⊂X. Evidently, this deﬁnition is correct, i.e., Fn(k(X)) depends
only on the birational class of X.
The same reasoning as in [5], Proposition 3.7 shows that for any variety X over k,
there is a homological type spectral sequence E1
p,q(X, F∗) =
L
η∈X(p)
Fp+q(k(η)) ⇒Fp+q(X),
where X(p) is the set of all points η on X such that dim(η) = p. The corresponding
ascending ﬁltration on Fn(X) is deﬁned by Im( lim
−→
Z∈X≤p
Fn(Z) →Fn(X)) ⊆Fn(X), where
X≤p is the set of all closed subsets Z in X of dimension at most p. For p, q ∈Z, we put
Gers(X, F∗, q)p = E1
p,q(X, F∗). Thus Gers(X, F∗, q)• is a homological type complex.
25


## Page 26


Let us say that a variety X is equidimensional if all irreducible components of X
have the same dimension. For an equidimensional variety X of dimension d, we put
Gers(X, F∗, n)p = E1
d−p,n−d(X, F∗) =
L
η∈X(p) Fn−p(k(η)). The cohomological type complex
Gers(X, F∗, n)• is called the Gersten complex associated to the weak homology theory
F∗. Given a collection {fη} ∈
L
η∈X(p) Fn−p(k(η)), the set of all schematic points η ∈X(p)
such that fη ̸= 0 is called the support of the collection {fη}.
It is readily seen that for any q ∈Z the functors F(q)n(X) = Hn(Gers(X, F∗, q)•),
n ∈Z, n ≥0 also form a weak homology theory.
For an irreducible variety X of
dimension d, we have F(q)d(k(X)) = Fd+q(k(X)) and F(q)n(k(X)) = 0 for n ̸= d.
Therefore, Gers(X, F(q)∗, 0)• = Gers(X, F∗, q)• and Gers(X, F(q)∗, m)• = 0 if m ̸= 0.
Deﬁnition 3.2. For a weak homology theory F∗, the homology sheaves Fn, n ∈Z are
the sheaves on Vk in the Zariski topology associated to the presheaves Fn, n ∈Z.
We put F X
n to be the restriction of the sheaf Fn to the variety X if we need to
distinguish sheaves on diﬀerent spaces.
Thus for an irreducible variety X, we have
(F X
n )X = Fn(k(X)). Note that for an open subset iU : U ֒→X, we have (iU)∗F X
n = F U
n .
We also denote by F U
n the sheaf (F X
n )U = (iU)∗F U
n on X.
It is readily seen that for any irreducible variety X of dimension d and any q ∈Z,
the sheaf F(q)X
d is 1-pure (see Section 2.5).
Remark 3.3. Suppose that X is an equidimensional variety of dimension d over k, η is
a schematic point on X, and D ⊂X is a divisor; then any element f ∈(F(n)X\D
d
)η,
n ∈Z, is equal to the restriction of an element from Fn+d(Xη\(D ∪R)), where R is a
closed subset in X such that all irreducible components of R have codimension at least
two in X. This follows directly from deﬁnitions and the localization sequence.
For an equidimensional variety X, we may also consider the sheaﬁﬁed Gersten com-
plex Gers(X, F∗, n)•, namely Gers(X, F∗, n)p =
L
η∈X(p)(iη)∗Fn−p(k(η)), where for each
point η ∈X(p), we consider Fn−p(k(η)) as a constant sheaf on η. There is a morphism
of complexes of sheaves F X
n →Cous(X, F X
n )• →Gers(X, F∗, n)•, where F X
n is consid-
ered as a complex concentrated in the zero term. Also, we have Hq(Gers(X, F∗, n)•) =
F(n −d)X
d−q and there is a natural morphism of sheaves F X
n
→F(n −d)X
d , where
d = dim(X).
For any equidimensional closed subset Z ⊂X of codimension p in X, we have
γZGers(X, F∗, n)• = Gers(Z, F∗, n −p)•[−p].
In particular, RqγZGers(X, F∗, n) =
F(n −d)Z
d−q, where d = dim(X).
Also, there are natural morphisms of sheaves
F Z
n−p →RpγZGers(X, F∗, n) = F(n −d)Z
d−p and RpγZF X
n →RpγZGers(X, F∗, n). How-
ever, in general there is no natural morphism between the sheaves F Z
n−p and RpγZF X
n .
Deﬁnition 3.4. We say that a weak homology theory F∗over a ﬁeld k is a homology
theory locally acyclic in ﬁbrations (l.a.f. homology theory) if the following two conditions
are satisﬁed:
26


## Page 27


(H): for any ﬁnite morphism f : X′ →X, there is a functorial homomorphism of graded
abelian groups f∗: Fn(X′) →Fn(X) extending the one for closed embeddings
and such that the axioms (WH1) and (WH2) are satisﬁed with f being a ﬁnite
morphism;
(LAF): if for a closed embedding i : Z ֒→X and a point η ∈Z there exists a morphism
π : X →Z such that π ◦i = idZ and π smooth at η, then there exists an open
subset U ⊂X containing η such that the composition Fn(Z) →Fn(X) →Fn(U)
is zero for any n ∈Z.
We say that a scheme Y is of geometric type over k if Y = ∩αUα, where {Uα} is a
collection of open subsets in a variety X over k. For such Y , we put Fn(Y ) = lim
−→
U
Fn(U),
where the limit is taken over all open subsets U ⊂X containing Y . It follows easily that
Fn(Y ) is independent in X. If Y is an equidimensional scheme of geometric type over
k, then we put Fn(Y ≥p) = lim
−→
Z
Fn(Z), where the limit is taken over all closed subsets
Z ⊂Y such that all irreducible components of Z have codimension at least p in Y .
The proof of the next statement is the same as the proof of Theorem 5.11 in [22] or
Theorem 4.2 in [5].
Proposition 3.5. Let F∗be an l.a.f. homology theory over a ﬁeld k; then for any regular
irreducible local scheme Y of geometric type over k and any n ∈Z, there is a natural
short exact sequence
0 →Fn(Y ≥p) →
L
η∈Y (p) Fn(k(η)) →Fn−1(Y ≥(p+1)) →0,
where the ﬁrst map takes each element α ∈Fn(Z) to the restrictions of α to the generic
points of all components in Z that have codimension p in Y .
Remark 3.6. The diﬀerential in the Gersten complex for Y equals to the composition of
two corresponding maps in the exact triples from Proposition 3.5 for n and for n + 1.
Corollary
3.7. Under the notations from Proposition 3.5, any cocycle {fη}
∈
L
η∈Y (p) Fn(k(η)) in the Gersten complex on Y is equal to the restriction of an element
α ∈Fn(Z) such that the set of all codimension p components of Z is equal to the support
of {fη}.
Proof. By Proposition 3.5, any cocycle {fη} ∈
L
η∈Y (p) Fn(k(η)) is deﬁned by an element
α ∈Fn(Z) for a certain closed subset Z ⊂Y of codimension at least p. Let Z0 ⊂Z be
a codimension p irreducible component in Y that is not from the support of {fη}. Note
that Fn(k(Z0)) = lim
−→Fn(U), where the limit is taken over all open subsets U ⊂Z0 that
are also open in Z. From the localization sequence it follows that, in fact, α belongs
to Fn(Z′), where the closed subset Z′ ⊂Z has the same irreducible components as Z
except for Z0 and Z0 is replaced by a proper closed subset. This concludes the proof.
27


## Page 28


Proposition 3.5 also implies the following important statement.
Proposition 3.8. Let F∗be an l.a.f.
homology theory over a ﬁeld k; then for any
equidimensional regular variety X over k and for any n ∈Z, the morphism of complexes
of sheaves F X
n →Gers(X, F∗, n)• is a quasiisomorphism.
Corollary 3.9. Let F∗be an l.a.f. homology theory over a ﬁeld k, X be an equidimen-
sional regular variety X over k, and n ∈Z; then we have:
(i) the sheaf F X
n on X is Cohen–Macaulay in the sense of [12] and the natural mor-
phism of complexes of sheaves Cous(X, F X
n )• →Gers(X, F∗, n)• is an isomor-
phism; in particular, the sheaves F X
n are 1-pure on X.
(ii) for any equidimensional closed subset Z ⊂X of codimension p, the natural mor-
phism of sheaves RpγZF X
n →RpγZGers(X, F∗, n)• = F(n −d)Z
d−p is an isomor-
phism; in particular, there is a natural morphism F Z
n−p →RpγZF X
n , which is an
isomorphism at the generic points of Z;
(iii) for any q ∈Z, we have F(q)X
d = F X
d+q and F(q)X
m = 0 if m ̸= 0.
Corollary 3.10. Let F∗be an l.a.f. homology theory. Suppose X is an equidimensional
variety that is regular outside of a codimension two closed subset; then for any point
η ∈X and any n ∈Z, we have
(F(n)X
d )η = T
D
Fn+d(OX,D) ⊂Fn+d(k(X)),
where d = dim(X) and D runs over all irreducible divisors in X containing η.
Proof. This follows from the regularity of the discrete valuation ring OX,D for any D and
the exactness of the Gersten complex for XD = Spec(OX,D).
Examples 3.11.
The following examples are homology theories locally acyclic in ﬁbrations:
1) Fn(X) = K′
n(X) = πn+1(BQM(X)) for n ≥0 and Fn(X) = 0 for n < 0, where
M(X) is the exact category of coherent sheaves on X (see [22], proof of Theorem 5.11).
2) Fn(X) = Hn(X, i) for some i ∈Z, where (H∗, H∗) is a Poincar´e duality theory
with supports in the sense of Bloch–Ogus (see [5], Proposition 4.5).
3) Fn(X) = An(X; M), where M is a cycle module over k in the sense of Rost (see
[23], proof of Proposition 6.4). In this case we have Gers(X, F∗, 0)• = C•(X; M) in
notations from [23] and Gers(X, F∗, m)• = 0 if m ̸= 0.
Remark 3.12. The sheaf Kn(OX) on a smooth variety X over k from both Examples
3.11, 1) and Examples 3.11, 3) for M = L
n≥0
Kn (compare with Corollary 3.9,(iii)).
In the next three sections we develop some technique necessary for the proof of
Lemma 3.37.
28


## Page 29


3.2
Strongly locally eﬀaceable pairs
Let F∗be a homology theory locally acyclic in ﬁbrations over a ﬁeld k and X be an
equidimensional variety. Consider equidimensional subvarieties Z ⊂X and eZ ⊂X of
codimensions p and p −1 in X, respectively, such that Z ⊂eZ.
Deﬁnition 3.13. Suppose that for each (not necessary closed) point x ∈Z and for any
open subset V ⊂X containing x, there exists a smaller open subset W ⊂X containing
x such that the natural map
Fn(V ∩Z) →Fn(W ∩eZ)
is zero for all n ∈Z. In addition, suppose that for any q ≥0, there exists an assignment
R 7→Λ(R), where R is an equidimensional subvariety of codimension q in Z, Λ(R) is an
equidimensional subvariety of codimension q in eZ such that R ⊂Λ(R) and for any (not
necessary closed) point x ∈Z, for any open subset V ⊂X containing x, there exists a
smaller open subset W ⊂X containing x such that the composition
Fn(V ∩(Z\R)) →Fn(V ∩(Z\Λ(R))) →Fn(W ∩( eZ\Λ(R)))
is zero for all n ∈Z (in fact, this condition makes sense whenever x ∈R). Then we say
that the pair of subvarieties (Z, eZ) is a strongly locally eﬀaceable pair, or an s.l.e. pair
(developing the terminology from [5]).
The assignment Λ in the deﬁnition of s.l.e. pairs is needed to establish a relation
with the Gersten complex, as is stated in the next proposition.
Proposition 3.14. Suppose that the ﬁeld k is inﬁnite and perfect. Let (Z, eZ) be an s.l.e.
pair of subvarieties on a smooth variety X over the ﬁeld k such that Z has codimension p
in X. Choose an arbitrary (not necessary closed) point x ∈Z. Suppose that the collection
{fz} ∈
L
z∈Z(0)
x
Fn(k(z)) is a cocycle in the Gersten complex on Xx = Spec(OX,x), i.e.,
suppose that dx({fz}) = 0, where dx is the diﬀerential in the complex Gers(Xx, F∗, n+p)•.
Then there exists a collection {gez} ∈
L
ez∈eZ(0)
x
Fn+1(k(ez)) such that dx({gez}) = {fx}.
Proof. It follows from Corollary 3.7 that the collection {fz} is deﬁned by an element
α ∈Fn((Z ∪S)x) for a certain closed subset S ⊂X such that each irreducible component
of S has codimension at least p+1 in X and is not contained in Z. We may assume that
S is equidimensional of codimension p+1 in X. Hence the intersection Z ∩S is contained
in some equidimensional subvariety R ⊂Z of codimension p + 2 in X. Furthermore,
α ∈Fn(V ∩(Z ∪S)) for some open subset V ⊂X containing x.
By Corollary 3.18, there is an equidimensional subvariety eS of codimension p in X
such that the pair (Λ(R) ∪S, eS) is strongly locally eﬀaceable. Consider the following
29


## Page 30


commutative diagram, whose middle column is exact in the middle term:
Fn(Λ(R) ∪S)
−→
Fn(eS)
↓
↓
Fn(Z ∪S)
−→
Fn( eZ ∪S)
−→
Fn( eZ ∪eS)
↓
↓
Fn(Z\R)
−→
Fn( eZ\(Λ(R) ∪S))
The map in the bottom raw is the composition
Fn(Z\R) →Fn( eZ\Λ(R)) →Fn( eZ\(Λ(R) ∪S)).
Since the pairs (Z, eZ) and (Λ(R) ∪S, eS) are s.l.e., for the point x ∈Z and the open
subset V ⊂X considered above, there exists a smaller open subset W ⊂X containing
x such that the map
Fn(V ∩(Z ∪S)) →Fn(W ∩( eZ ∪eS))
is zero. Therefore α is a coboundary of an element β ∈Fn+1(W ∩(( eZ∪eS)\(Z∪S))) in the
localization exact sequence associated to the closed embedding W∩(Z∪S) ֒→W∩( eZ∪eS).
In particular, β deﬁnes a collection {gez} ∈
L
ez∈eZ(0)
x
Fn+1(k(ez)). Note that all codimension
p −1 irreducible components of eZ ∪eS are contained in eZ, while all codimension p
irreducible components of Z ∪S are in Z (as before, codimensions are taken with respect
to X). Therefore dx({gez}) = {fz} and the proposition is proved.
3.3
Existence and addition of strongly locally eﬀaceable pairs
Let F∗be an l.a.f. homology theory over a ﬁeld k and X be a variety over k.
Deﬁnition 3.15. Let f ≥0 be a natural number and (Z, eZ) be an s.l.e. pair on X.
Suppose that for each irreducible subvariety C ⊂X and an equidimensional subvariety
R ⊂Z of codimension q in Z with C ⊈R, we can choose an equidimensional subva-
riety ΛC(R) ⊂eZ of codimension q in eZ such that C ⊈ΛC(R), R ⊂ΛC(R), and the
following property holds true. For any f irreducible subvarieties C1, . . . , Cf ⊂eZ, for any
f equidimensional subvarieties R1, . . . , Rf ⊂Z (maybe of diﬀerent codimensions in Z)
with Ci ⊈Ri for all i, 1 ≤i ≤f, for any schematic point x ∈Z, and an open subset
V ⊂X containing x, there exists a smaller open subset W ⊂X containing x such that
the natural map
Fn(V ∩(Z\(R1 ∪. . . ∪Rf))) →Fn(W ∩( eZ\(ΛC1(R1) ∪. . . ∪ΛCf(Rf))))
is zero for all n ∈Z. Then we say that the pair of subvarieties (Z, eZ) is strongly locally
eﬀaceable with the freedom degree at least f or is an f-s.l.e. pair. In particular, a strongly
locally eﬀaceable pair with the freedom degree at least zero is the same as a strongly locally
eﬀaceable pair.
30


## Page 31


Remark 3.16. If the pair (Z, eZ) is f-s.l.e. and Z′ ⊂Z is any closed equidimensional
subset of the same dimension as Z, then the pair (Z′, eZ) is also f-s.l.e.
Here is the existence theorem for strongly locally eﬀaceable pairs with a given freedom
degree.
Theorem 3.17. Suppose that the ﬁeld k is inﬁnite and perfect. Let X be an aﬃne smooth
variety over the ﬁeld k. Consider an equidimensional subvariety Z of codimension p ≥2
in X and a ﬁnite subset of closed points T ⊂X\Z. Then for any natural number f ≥0,
there exists a subvariety eZ ⊃Z that does not contain any point from T and such that
the pair (Z, eZ) is strongly locally eﬀaceable with the freedom degree at least f.
Corollary 3.18. Suppose that the ﬁeld k is inﬁnite and perfect. Let X be a smooth
variety over the ﬁeld k. Consider an equidimensional subvariety Z of codimension p ≥2
in X and a closed subset T ⊂X such that no irreducible component of T is contained in
Z and T has codimension at most p−1 in X. Then there exists a subvariety eZ ⊃Z that
does not contain any irreducible component of T and such that the pair (Z, eZ) is s.l.e.
Proof. Consider a ﬁnite open aﬃne covering X = ∪αUα.
For each α and for each
irreducible component of T ∩Uα, choose a closed point on it outside of Z and thus get
a ﬁnite subset T ′
α ⊂Uα\Z. The application of Theorem 3.17 for the intersection of all
data with Uα yields the existence of a closed subset eZα ⊂Uα such that eZα does not
contain any point from T ′
α and the pair (Z ∩Uα, eZα) is s.l.e. We put eZ = ∪α eZα, where
the bar denotes the closure in X. By the codimension assumption, eZ does not contain
any irreducible component of T. Also, the pair (Z, eZ) is s.l.e., where Λ(R) can be taken
as the union over α of the closures of Λα(R ∩Uα) for an equidimensional subvariety
R ⊂Z.
Corollary 3.19. Suppose that the ﬁeld k is inﬁnite and perfect. Let X be a smooth
quasiprojective variety over the ﬁeld k. Consider an equidimensional subvariety Z of
codimension p ≥2 in X and a closed subset T ⊂X such that no irreducible component
of T is contained in Z. Then there exists a subvariety eZ ⊃Z that does not contain any
irreducible component of T and such that the pair (Z, eZ) is s.l.e.
Proof. For each irreducible component of T we choose a closed point on it outside of Z.
Thus we get a ﬁnite set of closed points T ′ ⊂X\Z. Since X is quasiprojective, there
exists a ﬁnite open aﬃne covering X = ∪αUα such that for each α we have T ′ ⊂Uα. To
conclude the proof, we repeat the same argument as in the proof of Corollary 3.18.
Combining Proposition 3.14 and Corollary 3.18, we get the following statement, which
could be considered as a uniform version of Gersten conjecture for smooth varieties and
has interest in its own right.
Corollary 3.20. Suppose that the ﬁeld k is inﬁnite and perfect. Let X be a smooth
variety over the ﬁeld k. Then for any equidimensional subvariety Z ⊂X of codimension
p in X there exists an equidimensional subvariety eZ ⊃Z of codimension p −1 in X
with the following property. Suppose we are given an arbitrary (not necessary closed)
31


## Page 32


point x ∈Z and a collection {fz} ∈
L
z∈Z(0)
x
Fn(k(z)) such that {fz} is a cocycle in the
local Gersten resolution at x, i.e., that dx({fz}) = 0. Then there exists a collection
{gez} ∈
L
ez∈eZ(0)
x
Fn+1(k(ez)) such that dx({gez}) = {fz}.
Remark 3.21. Corollary 3.20 is stronger than Theorem 4.2 in [5] or Theorem 5.11 in
[22]. Namely in [5] the analogous result was shown for a ﬁxed subvariety Z, a ﬁxed
point x ∈Z, and a ﬁxed collection {fz} on Zx. The proof in [5] does not seem to imply
directly Corollary 3.20 and that is why we use some diﬀerent geometrical method during
the proof of Theorem 3.17.
Proof of Theorem 3.17. The proof is in two steps.
Step 1.
During this step “a point” always means “a closed point”.
Recall that
d = dimX. We say that a morphism π : X →Ad−1 resolves a point x ∈Z if π is smooth
of relative dimension one at x, the restriction ϕ = π|Z is ﬁnite, ϕ−1(ϕ(x)) = {x},
and π(T) ∩π(Z) = ∅. The following geometric result is a globalization of Quillen’s
construction used in his proof of Gersten conjecture, see [22], Lemma 5.12 and [5], Claim
on p.191.
Proposition 3.22. Under the above assumptions, there exists a ﬁnite set Σ of morphisms
π : X →Ad−1 such that for any f points y1, . . . , yf ∈X and any point x ∈Z, there
exists π ∈Σ such that π resolves x and π(yi) /∈π(Z\{yi}) for all i, 1 ≤i ≤f.
Proof. Using Claim 3.23, we prove by decreasing induction on e, −1 ≤e ≤f that
for any e + 1 irreducible subsets Z0 . . . , Ze in Z there exist non-empty open subsets
U0 ⊂Z0, . . . , Ue ⊂Ze and a ﬁnite set of morphisms Σ such that the statement of
Proposition 3.22 is true for all collections of points (x, y1, . . . , yf, y′
1, . . . , y′
f) satisfying
x ∈U0, yi ∈Ui for all i, 1 ≤i ≤e, yi ∈Z for all i, e + 1 ≤i ≤f, and y′
i ∈X\Z for
all i, 0 ≤i ≤f. Note that for e = −1 this immediately implies the needed statement of
Proposition 3.22.
Suppose that e = f and y′
1, . . . , y′
f are f arbitrary points in X\Z. The application
of Claim 3.23 for the points y′
1, . . . , y′
f and the closed subsets Z0, . . . , Zf in Z yields the
existence of non-empty open subsets U0 ⊂Z0, . . . , Uf ⊂Zf and a morphism π satisfying
the conditions from Claim 3.23. Since the conditions y′
i /∈π−1(π(Z)), 1 ≤i ≤f are
open, there is a ﬁnite open covering ∪αVα of the direct product (X\Z)×f such that for
all α, any collection (y′
1, . . . , y′
f) from the open subset Vα satisﬁes the conditions from
Claim 3.23 with respect to some non-empty open subsets Uα
0 ⊂Z0, . . . , Uα
f ⊂Zf and a
morphism πα. Taking the ﬁnite intersections Ui = ∩αUα
i for each i, 0 ≤i ≤f, we get
the needed open subsets in Zi, 0 ≤i ≤f, while the needed ﬁnite set of morphisms is
Σ = {πα}.
Now let us do the induction step from e to e −1.
Choose any irreducible com-
ponent C1 of Z.
By the inductive hypothesis, there exist non-empty open subsets
U1
0 ⊂Z0, . . . , U1
e−1 ⊂Ze−1, U1
e ⊂C1 and a ﬁnite set of morphisms Σ1 such that they
satisfy the conditions stated above. We may assume that the subset U1
e ⊂C1 is also
32


## Page 33


open in Z. Let C2 be one of the irreducible components of Z\U1
e . Again, by the induc-
tive hypothesis, there exist other open subsets U2
0 ⊂Z0, . . . , U2
e−1 ⊂Ze−1, U2
e ⊂C2 and a
ﬁnite set of morphisms Σ2 such that they satisfy the conditions stated above. We repeat
the same step until we come to the end of the obtained ﬁnite stratiﬁcation of Z by open
subsets Uj
e in Cj. Taking the ﬁnite intersections Ui = ∩jUj
i for each i, 0 ≤i ≤e −1, we
get the needed open subsets in Zi, 0 ≤i ≤e, while the needed ﬁnite set of morphisms is
equal to the ﬁnite union Σ = ∪jΣj.
Claim 3.23. For any f points y′
1 . . . , y′
f ∈X\Z and f +1 closed subsets Z0, . . . , Zf ⊂Z
there exist non-empty open subsets Ui ⊂Zi, 0 ≤i ≤f and a morphism π : X →Ad−1
such that π resolves all point x from U0 (with respect to Z), π(yi) /∈π(Z\{yi}) for any
point yi ∈Ui, 1 ≤i ≤f, and π(y′
i) /∈π(Z) for all i, 1 ≤i ≤f.
Proof. Let X ⊂PN be a projective variety such that X = X\H, where H ⊂PN is a
hyperplane. In what follows the bar denotes the projective closure in PN and the star
denotes a join of two projective subvarieties in PN.
Without loss of generality we may assume that T contains the points y′
1 . . . , y′
f and
that Zi are irreducible for all i, 0 ≤i ≤f. Let x′
i be an arbitrary smooth point on
Zi for each i, 0 ≤i ≤f (such x′
i exist because the ﬁeld is perfect).
We have the
following dimension conditions: dim(H ∩Z) ≤d −3, dim(H ∩(T ∗Z)) ≤d −2,
dim(H ∩Tx′
0X) = d −1, and dim(H ∩Tx′
iZi) ≤d −3 for all i, 0 ≤i ≤f. Since the
ground ﬁeld is inﬁnite, there exists a projective subspace L′ ⊂H of codimension d −2
in H such that L′ does not intersect with Z, intersects T ∗Z in a ﬁnite set of points,
intersects Tx′
0X in a line, and does not intersect with any Tx′
iZi for 0 ≤i ≤f. Note
that the projection πL′ with the center at L′ deﬁnes on Z a ﬁnite morphism ϕL′. Put
Z′
i = ϕ−1
L′ (ϕL′(Zi)) ⊂Z for 0 ≤i ≤f. For each i, 0 ≤i ≤f, let xi be an arbitrary point
on Zi ⊂Z′
i such that xi is smooth on Z′
i, TxiZi does not intersect with L′, and Tx0X
intersects L′ in a line.
We claim that the intersection L′ ∩(xi ∗Z′
i) is a ﬁnite set of points for all i, 0 ≤i ≤f.
Indeed, each join xi ∗Z′
i is the union two subsets. The ﬁrst one is the tangent space to Z′
i
at xi and does not intersect with L′. The second one is the union of lines passing through
xi and other points from Z′
i. The intersection of this union of lines with L′ corresponds
to the ﬁber of xi under the ﬁnite morphism ϕL′ and therefore is ﬁnite. Hence there exists
a hyperplane L ⊂L′ that does not intersect with the joins T ∗Z and xi ∗Z′
i for any
i, 0 ≤i ≤f and that intersects the tangent spaces Tx0X in one point. Since the variety
X is smooth, the projection πL with the center at L is smooth at x0. Besides, the map
πL can not glue points from Z′
i with points from Z\Z′
i for any i, 0 ≤i ≤f. Therefore the
application of Lemma 3.24 with Y = Z′
i yields that there exist non-empty open subsets
Ui ⊂Zi containing xi such that πL resolves all points x from U0 and ϕ−1
L (ϕL(yi)) = {yi}
for all points yi from Ui, 1 ≤i ≤f, where ϕL = πL|Z. In addition, π(T) does not
intersect with π(Z), and, in particular, π(y′
i) /∈π(Z) for all i, 1 ≤i ≤f.
We have used the following fact from projective geometry.
Lemma 3.24. Let Y ⊂PN be a projective variety, x ∈Y be a smooth point on Y .
Suppose that a projective subspace M ⊂PN does not intersect with the join x ∗Y . Then
33


## Page 34


there exists an open subset W ⊂Y containing x such that ϕ−1(ϕ(y)) = {y} for all
y ∈W, where ϕ is the restriction to Y of the projection πM with the center at M.
Step 2. In notations from Proposition 3.22, consider the ﬁnite set Σ of morphisms
π : X →Ad−1. Put eZ = ∪π−1(π(Z)), where the union is taken over all π ∈Σ. By
construction, eZ does not contain any irreducible component of T.
Proposition 3.25. The pair (Z, eZ) is f-s.l.e.
Proof. Essentially, we repeat the proof of Theorem 5.11 in [22] with some modiﬁcations.
First we note that after we choose a suitable closed point x′ on x ⊂Z we may suppose
that the given open subset V ∋x actually contains x′. Thus we may suppose x to be
closed.
Choose π ∈Σ that resolves x and, as before, put ϕ = π|Z. Following the construction
of Quillen, consider the Cartesian square:
Y
ϕ′
−→
X
↓π′
↓π
Z
ϕ
−→
Ad−1.
Note that ϕ′ is ﬁnite onto its image, ϕ′(Y ) = π−1(π(Z)) is a closed subset in eZ, and
(ϕ′)−1(x) consists of one point, which we denote by z. Besides, the morphism π′ is smooth
at z and admits a canonical section σ : Z →Y (with σ(x) = z). Since the homology
theory F∗is locally acyclic in ﬁbrations, the composition Fn(Z)
σ∗
−→Fn(Y ) →Fn(Y ′) is
zero for all n ∈Z and for some suitable open subset Y ′ ⊂Y containing z. Hence the
map Fn(Z) →Fn( eZ ∩U) is also zero for all n ∈Z and for some suitable open subset
U ⊂X containing x such that (ϕ′)−1(U) ⊂Y ′ (such U exists, since ϕ′ is ﬁnite and
(ϕ′)−1(x) = {z}).
Take an arbitrary open subset V ⊂X containing x. Since ϕ−1(ϕ(x)) = {x} and ϕ is
ﬁnite, there exists an open subset D ⊂Ad−1 such that x ∈ϕ−1(D) ⊂V . Restricting the
Cartesian diagram from Ad−1 to D, we get that the natural map Fn(V ∩Z) →Fn(W ∩eZ)
is zero for all n ∈Z and for some suitable open subset W ⊂V containing x.
Further, consider an irreducible subvariety C ⊂X and an equidimensional subvariety
R ⊂Z of codimension q in Z such that C ⊈R. We put
ΛC(R) =
[
y∈C\R

[
π∈Σy
π−1(π(R))

,
where Σy is the set of all π ∈Σ such that π(y) /∈π(Z\{y}). For instance, if C is not
contained in eZ, then ΛC(R) = ∪π−1(π(R)) where the union is taken over all π ∈Σ.
For irreducible subvarieties C1, . . . , Cf in X and subvarieties R1, . . . , Rf in Z satisfying
the needed conditions, we choose closed points yi ∈Ci\Ri. By construction, for any
closed point x ∈Z, there is a morphism π ∈Σ such that it resolves x and belongs to
Σy1 ∩. . . ∩Σyf. The same argument with the analogous Cartesian diagram as before
leads to the needed result.
34


## Page 35


This completes the proof of Theorem 3.17.
Remark 3.26. In Theorem 3.17 one may also require that each irreducible component
in eZ contains some irreducible component in Z. This follows from the fact that for
each irreducible component Z0 in Z, the variety π−1(π(Z0)) is irreducible in an open
neighborhood of a given point x, where π : X →Ad−1 is a morphism that resolves the
point x and, in particular, is smooth at x.
The following proposition allows to add strongly locally eﬀaceable pairs.
Proposition 3.27. Suppose that the ﬁeld k is inﬁnite and perfect. Let X be an aﬃne
smooth variety over the ﬁeld k. Consider two equidimensional subvarieties Z1 and Z2
of the same codimension p ≥2 in X. Suppose that we are given a subvariety eZ1 ⊃Z1
such that the pair (Z1, eZ1) is strongly locally eﬀaceable with the freedom degree at least
f ≥2. Consider a closed subset T ⊂X such that all irreducible components of T have
codimension at most p−1 in X, and an irreducible subvariety K ⊂X such that K is not
contained in Z2. Then there exists a subvariety eZ2 such that no irreducible component of
T and K is contained in eZ2 and the pair (Z1 ∪Z2, eZ1 ∪eZ2) is strongly locally eﬀaceable
with the freedom degree at least f −1.
Proof. If K is not contained in Z1, then the statement of the proposition follows directly
from Theorem 3.17 after we choose a closed point on each irreducible component of T
and K outside of Z1 ∪Z2 (in this case the freedom degree does not decrease). Otherwise
we use the same construction as in the proof of Proposition 3.14.
Suppose that K ⊂Z1. Then there is a codimension one subvariety Z′
2 in Z1 such that
Z′
2 does not contain K and contains the intersection of Z1 with each irreducible compo-
nent of Z2 that is not contained in Z1. Put Z3 = ΛK(Z′
2) ⊂eZ1. By the codimension
assumption, Z2 ∪Z3 does not contain any irreducible component of T. Choosing closed
points on each irreducible component of T and on K outside of Z2 ∪Z3, we see that,
by Theorem 3.17, there exists a subvariety eZ2 ⊂X such that the pair (Z2 ∪Z3, eZ2) is
(f −1)-s.l.e. and eZ2 does not contain any irreducible component of T and K.
We claim that the pair (Z1 ∪Z2, eZ1 ∪eZ2) is s.l.e. This is implied by the following
commutative diagram, whose middle column is exact in the middle term:
Fn(Z2 ∪Z3)
−→
Fn( eZ2)
↓
↓
Fn(Z1 ∪Z2)
−→
Fn( eZ1 ∪Z2)
−→
Fn( eZ1 ∪eZ2)
↓
↓
Fn(Z1\Z′
2)
−→
Fn( eZ1\(Z2 ∪Z3))
The map in the bottom raw is the composition
Fn(Z1\Z′
2) →Fn( eZ1\Z3) →Fn( eZ1\(Z2 ∪Z3)).
Since the pairs (Z1, eZ1) and (Z2 ∪Z3, eZ2) are s.l.e., for any point x ∈Z1 ∪Z2 and any
open subset V ⊂X containing x, there exists a smaller open subset x ∈W ⊂X such
that the map
Fn(V ∩(Z1 ∪Z2)) →Fn(W ∩( eZ1 ∪eZ2))
35


## Page 36


is zero for all n ∈Z.
Now consider an irreducible subvariety C ⊂X and an equidimensional subvariety
R ⊂Z1 ∪Z2 of codimension q in Z1 ∪Z2 such that C ⊈R. Let R′ be the union of all
irreducible components in R that are not contained in Z′
2 ∪Z2. Let Λ′
C(R′) be the union
of all irreducible components in ΛC(R′) ⊂eZ1 that are not contained in Z2 ∪Z3. Then
there exists an equidimensional subvariety R′′ ⊂Z2 ∪Z3 of codimension q in Z2 ∪Z3
such that R′′ contains the intersection (Λ′
C(R′) ∪R) ∩(Z2 ∪Z3) and does not contain
C. Consider ΛC(R′′) ⊂eZ2, where now ΛC is taken with respect to the (f −1)-s.l.e. pair
(Z2 ∪Z3, eZ2).
We claim that (Z1∪Z2, eZ1∪eZ2) is an (f −1)-s.l.e. pair with respect to the assignment
(R, C) 7→ΛC(R) = Λ′
C(R′)∪ΛC(R′′). This is implied by the commutative diagram, which
analogous to the previous one. This new diagram is the combination of two following
diagrams:
Fn((Z1 ∪Z2)\{Ri})
−→
Fn(( eZ1 ∪Z2)\{Λ′
Ci(R′
i) ∪Ri})
↓
↓
Fn(Z1\(Z′
2 ∪{Ri}))
−→
Fn( eZ1\(Z2 ∪Z3 ∪{Λ′
Ci(R′
i)})),
Fn((Z2 ∪Z3)\{Λ′
Ci(R′
i) ∪Ri})
−→
Fn( eZ2\{ΛCi(Ri)})
↓
↓
Fn(( eZ1 ∪Z2)\{Λ′
Ci(R′
i) ∪Ri})
−→
Fn(( eZ1 ∪eZ2)\{ΛCi(Ri)}).
We glue these diagrams together using the following sequence, which is exact in the
middle term:
Fn((Z2 ∪Z3)\{Λ′
Ci(R′
i) ∪Ri}) →Fn(( eZ1 ∪Z2)\{Λ′
Ci(R′
i) ∪Ri}) →
→Fn( eZ1\(Z2 ∪Z3 ∪{Λ′
Ci(R′
i)})).
Here {Oi} means the union of objects Oi over all i, 1 ≤i ≤f −1 and the horizontal
maps in the diagrams are the compositions of direct images under closed embedding
and restrictions to open subsets. The new diagram is analyzed in the same way as the
previous one.
Remark 3.28. For p = 1 by Quillen’s result the only possible pair (Z, X) is s.l.e. However
there is no analogue of Theorem 3.17 and Proposition 3.27 in this case with non-empty
T and K.
3.4
Patching systems
Let k be a ﬁeld and X be an equidimensional variety over k. Consider an equidimensional
subvariety Z ⊂X of codimension p in X.
Deﬁnition 3.29. Suppose that the system of equidimensional subvarieties {Z1,2
r }, 1 ≤
r ≤p −1 of codimension r in X, respectively, satisﬁes the following conditions:
36


## Page 37


(i) the variety Z is contained in both varieties Z1
p−1 and Z2
p−1, and the variety Z1
r ∪Z2
r
is contained in both varieties Z1
r−1 and Z2
r−1 for all r, 2 ≤r ≤p −1;
(ii) the pairs (Z, Z1
p−1), (Z, Z2
p−1), (Z1
r ∪Z2
r, Z1
r−1), and (Z1
r ∪Z2
r, Z2
r−1) are strongly
locally eﬀaceable with the freedom degree at least f for all r, 2 ≤r ≤p −1;
(iii) the varieties Z1
r and Z2
r have no common irreducible components for all r, 1 ≤r ≤
p −1.
Then we say that the system of subvarieties {Z1,2
r }, 1 ≤r ≤p −1 is a patching system
for the subvariety Z with the freedom degree at least f.
Proposition 3.30. Suppose that the ﬁeld k is inﬁnite and perfect; then for any integer
f ≥0 and any equidimensional subvariety Z of codimension p in the aﬃne smooth
variety X over the ﬁeld k, there exists a patching system {Z1,2
r }, 1 ≤r ≤p −1 on X for
the subvariety Z with the freedom degree at least f.
Proof. We construct the needed system of subvarieties {Z1,2
r } by decreasing induction
on r, 1 ≤r ≤p −1.
Suppose that r = p −1.
The application of Theorem 3.17 with empty T yields
the existence of an equidimensional subvariety Z1
p−1 = eZ ⊂X of codimension p −1 in
X such that (Z, Z1
p−1) is an f-s.l.e pair. Choosing a closed point on each irreducible
component of Z1
p−1, we see that the application of Theorem 3.17 yields the existence of
an equidimensional subvariety Z2
p−1 = eZ of codimension p −1 in X such that Z2
p−1 has
no common irreducible components with Z1
p−1 and (Z, Z2
p−1) is an f-s.l.e. pair.
The induction step from r + 1 to r, 1 ≤r < p −1 is analogous to the case r = p −1
with Z replaced by Z1
r+1 ∪Z2
r+1.
Remark 3.31. Using Corollary 3.18 instead of Theorem 3.17 in the proof of Proposition
3.30, it is possible to show that for any equidimensional subvariety Z on a (not necessary
aﬃne) smooth variety X over an inﬁnite perfect ﬁeld there exists a patching system with
the freedom degree at least zero.
Remark 3.32.
(i) By Remark 3.26, in Proposition 3.30 one may also require that each irreducible
component in Z1
p−1 and Z2
p−1 contains some irreducible component in Z and that
for all r, 1 ≤r ≤p −2, each irreducible component in Z1
r and Z2
r contains some
irreducible component in Z1
r+1 ∪Z2
r+1.
(ii) Let W ⊂X be an equidimensional subvariety such that W meets Z properly; if the
patching system {Z1,2
r } satisﬁes the condition from (i), then W meets Zi
r properly
for all r, 1 ≤r ≤p−1 and i = 1, 2. Combining this fact with Corollary 3.19, we get
that under conditions of Proposition 3.30 one may also require that no irreducible
component in W ∩Z1
r is contained in Z2
r for all r, 1 ≤r ≤p −1.
37


## Page 38


Let us introduce the following notation.
Suppose that Zi ⊂X, p ≤i ≤q are
equidimensional subvarieties of codimension i in an equidimensional variety X over k
such that Zq ⊂. . . ⊂Zp.
Consider a collection f = {fη} ∈
L
η∈X(p) Fn(k(η)).
We
put νZp...Zq(f) =
X
zp...zq
(νk(zq−1)k(zq) ◦. . . ◦νk(zp)k(zp−1))(fzp), where zp, . . . , zq range over
all collections of generic points in Zp, . . . , Zq such that for any i, p < i ≤q, we have
zi ∈zi−1. For f ∈Fn(k(X)), let sing(f) be the set of irreducible divisors D on X such
that νXD(f) ̸= 0.
Here is the main property of patching systems.
Proposition 3.33. Let {Z1,2
r }, 1 ≤r ≤p −1 be a patching system on X for the
equidimensional subvariety Z ⊂X of codimension p in X with the freedom degree at
least zero. Given a (not necessary closed) point x ∈Z, suppose that a collection g ∈
L
η∈X(p) Fn−p(k(η)) is a cocycle in the local Gersten resolution Gers(Y, F∗, n)• at x, where
Y = Xx, and that the support of the collection g is contained in Z. Then there exists
a collection f ∈
L
η∈X(0) Fn(k(η)) such that the subvariety sing(νXZ1
1...Z1
r−1(f)) ⊂Z1
r−1 is
contained in Z1
r ∪Z2
r for all r, 1 ≤r ≤p −1, and dxνXZ1
1...Z1
p−1(f) = g, where dx is the
diﬀerential in the local Gersten complex Gers(Y, F∗, n)•.
Proof. The proof is by induction on p ≥1. For p = 1, by Remark 3.28, there is nothing
to prove.
Suppose that p > 1. Then, by Proposition 3.14, there exist two collections g1, g2 ∈
L
η∈X(p−1) Fn−p+1(k(η)) with the support on Z1
p−1 and Z2
p−1, respectively, such that dx(gi) =
g for i = 1, 2.
Therefore, dx(g1 −g2) = 0 and, by the inductive assumption, there
exists a collection f ∈Gers(X, F∗, n)0 such that sing(νXZ1
1...Z1
r−1(f)) ⊂Z1
r ∪Z2
r for all
r, 1 ≤r ≤p −2 and dxνXZ1
1...Z1
p−2(f) = g1 −g2, where Zp−1 = Z1
p−1 ∪Z2
p−1. Such f
satisﬁes the needed conditions with respect to the initial collection g.
3.5
Main theorem
Let F∗be a homology theory locally acyclic in ﬁbrations over a ﬁeld k.
Theorem 3.34. Suppose that k is an inﬁnite perfect ﬁeld and that X is an irre-
ducible smooth variety over k; then for any n ∈Z, the morphism νX : A(X, F X
n )• →
Cous(X, F X
n )• = Gers(X, F∗, n)• is a quasiisomorphism.
Corollary 3.35. Under the assumptions from Theorem 3.34, the natural morphism
F X
n
→
A(X, F X
n )• is a quasiisomorphism; in particular, the cohomology groups
Hi(A(X, F X
n )•) are canonically isomorphic to the cohomology groups Hi(X, F X
n ).
Remark 3.36. In Theorem 3.34 we make a strong restriction on the ground ﬁeld to be
inﬁnite and perfect. In fact, the only one place where we use this is the geometric proof
of Claim 3.23. It seems possible to prove the same result for smooth varieties over a
38


## Page 39


ﬁnite ﬁeld, and, then, to reduce the case of regular varieties over an arbitrary ﬁeld to
that case by a standard argument of choosing a model. On the other hand, the author
can prove Theorem 3.34 for dimX ≤3 over an arbitrary ﬁeld, avoiding Claim 3.23.
Proof of Theorem 3.34. In is enough to prove that the morphism νU : A(U, F U
n ) →
Cous(U, F X
n ) is a quasiisomorphism for any aﬃne open subset U ⊂X. We may put
X = U. Since F X
n is a subsheaf in a constant sheaf, by Proposition 2.30, the complex
A(X, F X
n )• is a subcomplex in the complex A′(X, F X
n )•. By Remark 2.22 and Theorem
2.46, it is enough to show that for any p, 0 ≤p ≤d, the natural homomorphism
Hp(A(X, F X
n )•) →Hp(A′(X, F X
n )•) is injective.
For p = 0, there is nothing to prove. Suppose that 1 ≤p ≤d and consider an element
f ∈A(X, F X
n )p. Suppose that f = d(g′), where g′ ∈A′(X, F X
n )p−1. We want to show
that there exists g ∈A(X, F X
n )p−1 such that d(g) = f. We prove this by induction on
the maximal depth l, −1 ≤l ≤p −1, of types for non-zero components of g′. Recall
that for any adele h and an increasing sequence of natural numbers (j0 . . . jq), by hj0...jq
we denote the component of h that has type (j0 . . . jq).
Suppose that l = −1. Let (i0 . . . ip−1) be a sequence such that g′
i0...ip−1 ̸= 0; then
i0 > 0 and we have g′
i0...ip−1 = f0i0...ip−1 ∈A((0i0 . . . ip−1), F X
n ).
By Corollary 2.42,
g′
i0...ip−1 ∈A((i0 . . . ip−1), F X
n ) and thus g′ ∈A(X, F X
n )p−1.
Now suppose that l
≥
0.
Let (0 . . . lil+1 . . . ip−1) be a sequence such that
g′
0...lil+1...ip−1 ̸= 0. Suppose that l < p −1. Combining Proposition 2.16 and Corollary
3.9(ii), we get that the element ν0...l+1(f0...l+1il+1...ip−1) belong to the group
L
ηl+1∈X(l+1) A((0(il+1 −l −1) . . . (ip−1 −l −1)), F(n −d)
ηl+1
d−l−1) ⊂
⊂
Y
ηil+1...ηip
 
L
ηl+1∈X(l+1)Fn−l−1(k(ηl+1))
!
,
where d = dim(X) and the product is taken over all ﬂags ηil+1 . . . ηip of type (il+1 . . . ip)
and ηil+1 ∈ηl+1. On the other hand, the reciprocity law implies that
ν0...l+1(f0...l+1il+1...ip−1) = ν′
0...l+1(−1)l+1g′
0...lil+1...ip−1.
By Lemma 3.37, there exists an element g0 ∈A((0 . . . lil+1 . . . ip−1), F X
n ) such that
ν′
0...l+1(g′
0...lil+1...ip−1 −g0) = 0.
By Lemma 2.48, there exists an element h′ ∈
Q
0≤i≤l
A′((0 . . .ˆı . . . lil+1 . . . ip−1), F X
n ) such
that d(h′)0...lil+1...ip−1 = g′
0...lil+1...ip−1 −g0. Note that d(g′ −g0 −d(h′)) ∈A(X, F X
n )p and
the adele g′ −g0 −d(h′) has a strictly less nonzero depth l components than the adele
g′. Therefore, by the inductive assumption, there exists an element g1 ∈A(X, F X
n )p−1
such that d(g1) = d(g′ −g0 −d(h′)) and we put g = g0 + g1.
Now suppose that l = p −1; then, by Lemma 2.23, there exists an element g0 ∈
A((0 . . . p−1), F X
n ) such that ν′
0...p−1(g′−g0) = 0. By Lemma 2.48, there exists an element
39


## Page 40


h′ ∈
Q
0≤i<p−1
A′((0 . . .ˆı . . . p −1), F X
n ) such that d(h′)0...p−1 = (g′ −g0)0...p−1. Note that
d(g′ −g0 −d(h′)) ∈A(X, F X
n )p and the adele g′ −g0 −d(h′) has no components of depth
p−1. Therefore, by the inductive assumption, there exists an element g1 ∈A(X, F X
n )p−1
such that d(g1) = d(g′ −g0 −d(h′)) and we put g = g0 + g1.
The essential part in the proof of Theorem 3.34 is the following approximation type
lemma.
Lemma
3.37. Under the assumptions from Theorem 3.34,
consider an adele
f ∈A′((i0 . . . ip), F X
n ) such that the depth of the sequence (i0 . . . ip) is l < p and
ν′
0...(l+1)(f) ∈
L
ηl+1∈X(l+1) A((0(il+1 −l −1) . . . (ip −l −1)), F(n −d)
ηl+1
d−l−1) ⊂
⊂
Y
ηil+1...ηip
 
L
ηl+1∈X(l+1)Fn−l−1(k(ηl+1))
!
,
where d = dim(X) and the product is taken over all ﬂags ηil+1 . . . ηip of type (il+1 . . . ip)
and with ηil+1 ∈ηl+1. Then there exists an adele g ∈A((i0 . . . ip), F X
n ) of the same type
as f such that ν0...(l+1)(g) = ν′
0...(l+1)(f).
Proof. During the proof ηs denotes a schematic point on X of codimension s in X (though
sometimes points are considered on proper closed subvarieties in X). Further, dηs is the
diﬀerential in the local Gersten resolution at ηs, i.e., in the complex Gers(Xηs, F∗, n)•.
For any two subvarieties C1, C2 in X, denote by C1 −C2 the union of all irreducible
components of C1 that are not contained in C2. Notice that for any two subvarieties C1,
C2 in X, we have (C1 −C2) ∪C2 = C1 ∪C2.
The proof is in two steps.
Step 1. Consider the collection of A-adeles
{hηl+1(il+1−l−1)...(ip−l−1)} = ν′
0...(l+1)(f) ∈
L
ηl+1∈X(l+1) A((0(il+1 −l −1) . . . (ip −l −1)), F
ηl+1
n−l−1).
Let Zl+1 = ∪ηl+1 be the union of the closures over the ﬁnite set of schematic points
ηl+1 ∈X(l+1) such that hηl+1(il+1−l−1)...(ip−l−1) is a non-zero adele on ηl+1.
For each
schematic point ηl+1 ∈Z(0)
l+1 let {Dηl+1, Dηl+1ηil+1...ηik}, l + 1 ≤k < p be the system of
divisors on ηl+1 arising from the adelic condition for the A-adele hηl+1(il+1−l−1)...(ip−l−1)
on ηl+1 (see Proposition 2.14).
Proposition 3.38. For any ﬂag ηil+1 . . . ηik, l+1 ≤k < p on Zl+1, there exists an equidi-
mensional subvariety Zl+1;ηil+1...ηik ⊂X of codimension l + 1 in X such that the system
of subvarieties {Zl+1;ηil+1...ηik}, l + 1 ≤k < p on X satisﬁes the following conditions:
(i) for any point ηil+1 on Zl+1, we have Zl+1;ηil+1(ηil+1) ⊆Zl+1(ηil+1) and for any ﬂag
ηil+1 . . . ηik, l + 1 < k < p on Zl+1 we have Zl+1;ηil+1...ηik(ηik) ⊆Zl+1;ηil+1...ηik−1(ηik);
40


## Page 41


(ii) for any ﬂag ηil+1 . . . ηik, l + 1 ≤k < p on Zl+1, the subvariety Zl+1;ηil+1...ηik −Zl+1
contains the equidimensional subvariety
Eηil+1...ηik =
[
ηl+1∈Z(0)
l+1
(Dηl+1ηil+1...ηik −Dηl+1)
of codimension l + 2 in X and the pair (Eηil+1...ηik, Zl+1;ηil+1...ηik −Zl+1) is strongly
locally eﬀaceable with the freedom degree at least p −k.
Proof. We construct the needed system of subvarieties {Zl+1;ηil+1...ηik} by induction on
k, l + 1 ≤k < p.
Suppose that k = l + 1. Since for each point ηl+1 ∈Z(0)
l+1 the system of divisors
{Dηl+1, Dηl+1ηil+1...ηik}, l + 1 ≤k < p on ηl+1 satisﬁes condition (∗) from Proposition
2.14, we get that for any point ηil+1 on X, the deﬁned above subvariety Eηil+1 does not
contain ηil+1. For each point ηil+1 on Zl+1, we choose closed points on each irreducible
component of Zl+1 and on ηil+1 outside of Eηil+1 and thus get a ﬁnite set of closed points
Tηil+1 ⊂X\Eηil+1. The application of Theorem 3.17 with f = p −l −1, Z = Eηil+1, and
T = Tηil+1 yields the existence of an equidimensional subvariety zηil+1 = eZ of codimension
l +1 in X such that zηil+1 does not contain ηil+1, has no common irreducible components
with Zl+1, and (Eηil+1, zηil+1) is an (p−l −1)-s.l.e. pair. We put Zl+1;ηil+1 = Zl+1 ∪zηil+1.
Now we do the induction step from k −1 to k, l + 1 < k < p. As before, by condition
(∗) from Proposition 2.14, for any ﬂag ηil+1 . . . ηik on Zl+1, the subvariety
Eηil+1...ηik −Eηil+1...ηik−1 =
[
ηl+1∈Z(0)
l+1
(Dηl+1ηil+1...ηik −(Dηl+1ηil+1...ηik−1 ∪Dηl+1))
does not contain ηik. For each ﬂag ηil+1 . . . ηik, the application of Proposition 3.27 with
Z1 = Eηil+1...ηik−1, Z2 = Eηil+1...ηik −Eηil+1...ηik−1, eZ1 = Zl+1;ηil+1...ηik−1 −Zl+1, T = Zl+1,
and C = ηik yields the existence of an equidimensional subvariety zl+1;ηil+1...ηik = eZ2
of codimension l + 1 in X such that zl+1;ηil+1...ηik does not contain ηik, has no common
irreducible components with Zl+1, and
(Eηil+1...ηik−1 ∪Eηil+1...ηik, (Zl+1;ηil+1...ηik−1 −Zl+1) ∪zl+1;ηil+1...ηik)
is a (p −k)-s.l.e. pair. We put Zl+1;ηil+1...ηik = Zl+1;ηil+1...ηik−1 ∪zl+1;ηil+1...ηik. By Remark
3.16,
(Eηil+1...ηik, Zl+1;ηil+1...ηik −Zl+1)
is a (p −k)-s.l.e. pair and Zl+1;ηil+1...ηik(ηik) ⊆Zl+1;ηil+1...ηik−1(ηk).
Corollary 3.39. For any ﬂag ηil+1 . . . ηip on Zl+1, there exists a collection
{gηl+1;ηil+1...ηip} ∈
L
ηl+1∈X(l+1)
ηip
Fn−l−1(k(ηl+1)),
satisfying the following conditions (note that the closure of the point ηl+1 from the index
of g may not contain ηil+1):
41


## Page 42


(i) dηip({gηl+1;ηil+1...ηip}) = 0;
(ii) if ηl+1 contains ηil+1, then gηl+1;ηil+1...ηip = hηl+1ηil+1...ηip;
(iii) the support of the collection {gηl+1;ηil+1...ηip} is contained in the subvariety
Zl+1;ηil+1...ηip−1.
Proof. We use the notations from Proposition 3.38.
Since the A′-adele f has type
(0 . . . lil+1 . . . ip), il+1 > l + 1, by reciprocity law, we have dηil+1({hηl+1ηil+1...ηip}) =
0
for
any
ﬂag
ηil+1 . . . ηip
on
Zl+1,
where
{hηl+1ηil+1...ηip}
is
considered
as
a
collection from Gers(Xηil+1, F∗, n)l+1.
Therefore the support of the collection
{gηl+2;ηil+1...ηip} = dηip({hηl+1ηil+1...ηip}) ∈Gers(Xηip, F∗, n)l+2 is contained in the sub-
variety Eηil+1...ηip−1.
Hence, by Propositions 3.14 and 3.38, there exists a collection
{g′
ηl+1;ηil+1...ηip} ∈Gers(Xηp, F∗, n)l+1 with the support on Zl+1;ηil+1...ηip−1 −Zl+1 such that
dηip({g′
ηl+1;ηil+1...ηip}) = gηl+2;ηil+1...ηip. Finally, we put gηl+1;ηil+1...ηip = {hηl+1ηil+1...ηip} −
{g′
ηl+1;ηil+1...ηip}.
Step 2. By Proposition 3.30, there exists a patching system {Z1,2
r }, 1 ≤r ≤l on X
for the subvariety Zl+1 with the freedom degree at least p −l. We extend this patching
system to patching systems for all subvarieties Zl+1;ηil+1...ηik, l + 1 ≤k < p.
Proposition 3.40. For each k, l+1 ≤k < p, and for each ﬂag ηil+1 . . . ηik on Zl+1, there
exists a patching system Z1,2
r;ηil+1...ηik, 1 ≤r ≤l on X for the subvariety Zl+1;ηil+1...ηik with
the freedom degree at least p−k, satisfying the following condition. Put D = Z1
1 ∪Z2
1 and
Dηil+1...ηik = Z1
1;ηil+1...ηik ∪Z2
1;ηil+1...ηik for any ﬂag ηil+1 . . . ηik, l+1 ≤k < p on Zl+1. Then
for any point ηil+1 on Zl+1, we have Dηil+1(ηil+1) ⊆D(ηil+1) and for any ﬂag ηil+1 . . . ηik,
l + 1 < k < p on Zl+1, we have Dηil+1...ηik(ηik) ⊆Dηil+1...ηik−1(ηik).
Proof. We use the notations from the proof of Proposition 3.38. The proof is by double
induction on k and r, l + 1 ≤k < p, 1 ≤r ≤l (the induction on r is decreasing, as in
the proof of Proposition 3.30).
Suppose that k = l + 1, r = l.
For each point ηil+1 on Zl+1, the application of
Proposition 3.27 with Z1 = Zl+1, Z2 = zl+1;ηil+1, eZ1 = Z1
l , T = Z2
l , and C = ηil+1 yields
the existence of an equidimensional subvariety z1
l;ηil+1 = eZ2 ⊂X of codimension l in X
such that z1
l;ηil+1 does not contain ηil+1, has no common irreducible components with Z2
l ,
and (Zl+1;ηil+1, Z1
l ∪z1
l;ηil+1) is a (p−l−1)-s.l.e. pair. We put Z1
l;ηil+1 = Z1
l ∪z1
l;ηil+1. Using
Proposition 3.27 with Z1 = Zl+1, Z2 = zl+1;ηil+1, eZ1 = Z2
l , T = Z1
l+1;ηil+1, and C = ηil+1,
we get an equidimensional subvariety z2
l;ηil+1 = eZ2 ⊂X of codimension l in X such that
z2
l;ηil+1 does not contain ηil+1, has no common irreducible components with Z1
l+1;ηil+1, and
(Zl+1;ηil+1, Z2
l ∪z2
l;ηil+1) is a (p −l −1)-s.l.e. pair. We put Z2
l;ηil+1 = Z2
l ∪z2
l;ηil+1.
42


## Page 43


The induction step from r + 1 to r for k = l + 1, 1 ≤r < l is analogous with Zl+1
replaced by Z1
r+1 ∪Z2
r+1, zl+1;ηil+1 replaced by z1
r+1;ηil+1 ∪z2
r+1;ηil+1, and Zj
l replaced by
Zj
r, j = 1, 2.
The reasoning for arbitrary k, l + 1 < k < p is the same as for k = l + 1 with
the subvarieties ηil+1, Zl+1;ηil+1, zl+1;ηil+1 replaced by the subvarieties ηik, Zl+1;ηil+1...ηik,
zl+1;ηil+1...ηik, respectively, for each ﬂag ηil+1 . . . ηik on Zl+1 and with the patching system
{Z1,2
r }, 1 ≤r ≤l replaced by the inductively deﬁned patching system {Z1,2
r;ηil+1...ηik−1}.
By construction, the system of divisors {D, Dηil+1,...,ηik }, l + 1 ≤k < p on X satisﬁes
the needed condition.
Corollary 3.41. For any ﬂag (ηil+1 . . . ηip) on Zl+1, there exists a collection
{gη0;ηil+1...ηip} ∈
L
η0∈X(0) Fn(k(η0)),
such that gη0;ηil+1...ηip ∈(F
X\Dηil+1 ...ηip−1
n
)ηip and
dηil+1νXZ1
1;F ...Z1
l;F ({gη0;ηil+1...ηip}) = {hηl+1ηil+1...ηip}.
Proof. The corollary follows from the direct application of Proposition 3.33 for the
collection {gηl+1;ηil+1...ηik} from Corollary 3.39 and the patching system {Z1,2
r;ηil+1...ηip−1},
1 ≤r ≤l from Proposition 3.40.
Now we are ready to deﬁne the needed adele g
∈
A((i0 . . . ip), F X
n ).
Let
η0 . . . ηlηil+1 . . . ηip be a ﬂag of type (i0 . . . ip) on X.
Then we put gη0...ηlηil+1...ηip =
gη0;(ηil+1...ηip) if ηil+1 . . . ηip is a ﬂag on Zl+1 and ηr ∈(Z1
r;F)(0) for all 1 ≤r ≤l. Otherwise
we put gη0...ηlηil+1...ηp = 0.
For any ﬂag η0 . . . ηk of type (i0 . . . ik), 0 ≤k ≤l on X, we put Dη0...ηk = D. For any
ﬂag η0 . . . ηlηil+1 . . . ηik of type (i0 . . . ik) on X, l + 1 ≤k < p, we put Dη0...ηlηil+1...ηk =
Dηil+1...ηik if ηil+1 . . . ηik is a ﬂag on Zl+1. Otherwise we put Dη0...ηlηil+1...ηk = ∅.
By Proposition 3.40, the system of divisors Dη0...ηk, 0 ≤k < p on X satisﬁes condition
(∗) from Proposition 2.14.
By Corollary 3.41, the distribution g satisﬁes the adelic
condition with respect to the system of divisors Dη0...ηk, 0 ≤k < p on X and we have
ν0...(l+1)(g) = ν′
0...(l+1)(f).
This concludes the proof of Lemma 3.37.
3.6
Explicit cocycles
In this section we construct explicitly certain cocycles in the adelic complex correspond-
ing to the given cocycles in the Gersten complex. Suppose k is an inﬁnite perfect ﬁeld,
F∗is an l.a.f.
homology theory over k, X is an irreducible smooth variety over the
ﬁeld k, and Y ⊂X is an equidimensional subvariety of codimension p in X. Consider
a collection {fy} ∈
L
y∈Y (0) Fm(k(y)) such that {fη} is a cocycle in the Gersten complex
Gers(X, F∗, p + m)• on X. By Remark 3.31, there exists a patching system {Y 1,2
r
},
43


## Page 44


1 ≤r ≤p −1 on X for the subvariety Y with the freedom degree at least zero. We put
Y 1
p = Y .
Proposition 3.42. There exists an adele f = [{fy}] ∈A(X, F X
p+m)p such that f is a co-
cycle in the adelic complex A(X, F X
p+m)• with νX(f) = {fy}, where νX : A(X, F X
p+m)• →
Gers(X, F∗, p + m)• is the morphism from Theorem 3.34, and f satisﬁes the following
conditions for any ﬂag ηi0 . . . ηip on X:
(i) fηi0...ηip = 0 unless ηir ∈Y 1
r for all r, 1 ≤r ≤p;
(ii) suppose that ηi0 /∈Y 1
1 , ηir ∈Y 1
r , ηir /∈Y 2
r for all r, 1 ≤r ≤p −1 and ηip ∈Y ;
then fηi0...ηip = efηip ∈Fp+m(k(X)), where efηip depends only on ηip and satisﬁes the
condition dηipνXY 1
1 ...Y 1
p−1( efηip) = {fy}ηip. Here dηip is the diﬀerential in the Gersten
resolution on Xηip = Spec(OX,ηip), the notation νXY 1
1 ...Y 1
p−1 was introduced in Sec-
tion 3.4, and the index ηip by a collection means that we consider the restriction of
the collection to Xηip;
(iii) we have sing(νXY 1
1 ...Y 1
r−1(fηi0...ηip)) ⊂Y 1
r ∪Y 2
r for all r, 1 ≤r ≤l, where l is the
depth of the type (i0 . . . ip).
Remark 3.43. Since d(f) = 0, we have ν0...(l+1)(d(f)) = 0 for any integer l, 0 ≤l ≤p −1.
Explicitly, for any ﬂag ηi1 . . . ηip−l+1 of type (i1 . . . ip−l+1) on X with i1 > l, we have
0 = dηi1ν0...l(
p−l+1
X
j=1
(−1)j+1f01...lηi1...ˆηij ...ηip−l+1) ∈
L
η∈X(l+1)
ηi1
Fp+m−l−1(k(η)),
(∗∗)
where for any ﬂag Φ of type T on X, the index (0 . . . lΦ) means that we consider the set
of all ﬂags η0 . . . ηlΦ of type (0 . . . lT) on X with the ﬁxed T-part Φ.
Proof of Proposition 3.42. We deﬁne the components of the adele f by decreasing in-
duction on the depth l, −1 ≤l ≤p of the type of a component. Moreover, we enlarge
the induction hypothesis by condition (∗∗).
Let η0 . . . ηp−1ηi be a ﬂag on X with the type depth l ≥p −1, i.e., i ≥p. If ηi /∈Y ,
then we put fη0...ηp−1ηi = 0. Suppose that ηi ∈Y . Then, by Proposition 3.33, there
exists an element efηi ∈Fp+m(k(X)) such that sing(νXY 1
1 ...Y 1
r−1( efηi)) ⊂Y 1
r ∪Y 2
r for all
r, 1 ≤r ≤p −1 and
dηiνXY 1
1 ...Y 1
p−1( efηi) = {fy}ηi ∈
L
η∈X(p)
ηi
Fm(k(η)).
We put fη0...ηp−1ηi = (−1)
p(p+1)
2
efηi if ηr is a generic point of some irreducible component
of Y 1
r for all r, 1 ≤r ≤p −1. Otherwise, we put fη0...ηp−1ηi = 0. It is readily seen that
conditions (i), (ii) are satisﬁed for the deﬁned above (0 . . . p −1, i)-type component of f,
and also condition (∗∗) holds for l = p −1 and any ﬂag ηi1ηi2 of type (i1i2) on X such
that i1 > p −1.
44


## Page 45


Now we do the induction step from l + 1 to l, 0 ≤l ≤p −2. Let η0 . . . ηlηi1 . . . ηip−l
be a ﬂag of type (0 . . . li1 . . . ip−l) on X, i1 > l + 1.
If ηi1
/∈Y 1
l+1, then we put
fη0...ηlηi1...ηip−l = 0. Suppose that ηi1 ∈Y 1
l+1. Then, by the inductive assumption and
by Proposition 3.33 applied to the patching system {Y 1,2
r
}, 1 ≤r ≤l on X for the
subvariety Y 1
l+1 and the point ηi1, there exists an element efηi1...ηip−l ∈Fp+m(k(X)) such
that sing(νXY 1
1 ...Y 1
r−1( efηi1...ηip−l)) ⊂Y 1
r ∪Y 2
r for all r, 1 ≤r ≤l and we have
dηi1νXY 1
1 ...Y 1
l ( efηi1...ηip−l) = νl+1(
p−l
X
j=1
(−1)j+1f01...l+1ηi1...ˆηij ...ηip−l)ηi1 ∈
L
η∈X(l+1)
ηi1
Fp+m−l−1(k(η)).
We put fη0...ηlηi1...ηip−l = efηi1...ηip−l if ηr is a generic point of some irreducible component
of Y 1
r for all r, 1 ≤r ≤l. Otherwise, we put fη0...ηlηi1...ηip−l = 0.
In the above notation suppose that ηir /∈Y 1
l+r for some r, 1 < r ≤p −l. Since for
any j, 1 ≤j < r, we have ηir /∈Y 1
l+r and for any j, r ≤j ≤p −l, we have ηir−1 /∈Y 1
l+r,
by the induction hypothesis, we get that f0...l+1ηi1...ˆηij ...ηip−l = 0 for any j, 1 ≤j ≤p −l.
Therefore we may put efηi1...ηip−l = 0 and hence the (0 . . . li1 . . . ip−l)-type component of
f satisﬁes condition (i).
Further, suppose that ηir ∈Y 1
l+r, ηir /∈Y 2
l+r for all r, 1 ≤r ≤p −1 and ηip ∈Y ; then
ηi1 /∈Y 1
l+2 and, by the inductive hypothesis, f0...l+1ηi1...ˆηij ...ηip−l = 0 for all j, 1 < j ≤p −l
and ef0...l+1ηi2...ηip−l = efηip−l, where efηip−l ∈Fp+m(k(X)) satisﬁes condition (ii). Therefore
we have the condition
dηi1νXY 1
1 ...Y 1
l ( efηi1...ηip−l) = νXY 1
1 ...Y 1
l+1( efηip−l).
By the inductive hypothesis, we have sing(νXY 1
1 ...Y 1
l ( efηip−l)) ⊂Y 1
l+1 ∪Y 2
l+1. Therefore we
may put efηi1...ηip−l = efηip−l and hence the (0 . . . li1 . . . ip−l)-type component of f satisﬁes
condition (ii).
As above, it is a trivial check that condition (∗∗) holds for l −1 and any ﬂag
ηi1 . . . ηip−l−1 of type (i1 . . . ip−l−1) on X such that i1 > l −1.
Finally, we put fηi0...ηip =
p
X
j=0
(−1)jf0ηi0...ˆηij ...ηip for any ﬂag ηi0 . . . ηip of type (i0 . . . ip)
on X with i0 > 0. By the induction hypothesis, we have fηi0...ηip ∈(F X
p+m)ηi0. The
same reasoning as above shows that conditions (i) and (ii) hold for the (i0 . . . ip)-type
component of f.
Since sing(fηi0...ηip) ⊂Y 1
1 ∪Y 2
1 for any ﬂag ηi0 . . . ηip on X, we see that the distribution
f satisﬁes the adelic condition with respect to the constant system of divisors Y 1
1 ∪Y 2
1 .
Thus we have deﬁned the needed cocycle f ∈A(X, F X
p+m)p.
The following claim is necessary for the proof of Theorem 4.22.
Claim 3.44. Under the above assumptions, consider a schematic point η ∈Y and sup-
pose that the cocycle {fy}η ∈Gers(Xη, F∗, p + m)p in the local Gersten resolution on Xη
45


## Page 46


is the restriction of an element α ∈Fm(Yη). Then the element efη ∈Fp+m(k(X)) in con-
dition (ii) from Proposition 3.42 may be chosen such that the collection dηνXY 1
1 ...Y 1
r−1( efη)
is the restriction of an element αr ∈Fp+m−r((Y 1
r ∪Y 2
r )η) for all r, 1 ≤r ≤p −1. More-
over, for all r, 1 ≤r < p −1, the restriction of αr to Fp+m−r((Y 1
r )η\Y 2
r ) is equal to the
restriction of an element from Fp+m−r((Y 1
r )η\(Y 1
r+1 ∪Y 2
r+1)) and the restriction of αp−1
to Fp+1((Y 1
p−1)η\Y 2
p−1) is equal to the restriction of an element from Fp+1((Y 1
p−1)η\Y ).
Finally, efη is the restriction of an element α0 ∈Fp+m(Xη\(Y 1
1 ∪Y 2
1 )).
Proof. The proof is by decreasing induction on r, 1 ≤r ≤p −1.
Suppose that r = p −1. Since {Y 1,2
r
} is a patching system with the freedom degree
at least zero, we see that the natural maps Fm(Yη) →Fm((Y 1
p−1)η) and Fm(Yη) →
Fm((Y 2
p−1)η) are equal to zero. Hence there are elements αi
p−1 ∈Fm+1((Y i
p−1)η\Y ), i = 1, 2
such that their coboundary is equal to α ∈Fm(Yη). The localization sequence associated
to the closed embedding (Y 1
p−1 ∩Y 2
p−1 ֒→Y 1
p−1 ∪Y 2
p−1) implies that both elements α1
p−1
and α2
p−1 are restrictions of an element αp−1 ∈Fm+1((Y 1
p−1 ∪Y 2
p−1)η).
The induction step from r + 1 to r, 1 ≤r < p −1 is analogous to the case r = p −1
with the subvarieties Y and Y 1,2
p−1 replaced by the subvarieties Y 1
r+1 ∪Y 2
r+1 and Y 1,2
r
,
respectively. At the end, for r = 0, we repeat the same with Y and Y 1,2
p−1 replaced by
Y 1
1 ∪Y 2
1 and X, respectively.
Remark 3.45. The condition from Claim 3.44 is satisﬁed for all η ∈X(p). Indeed, in this
case one puts α = fη ∈Fm(k(η)) = Fm(Yη).
Deﬁnition 3.46. Let {fy} ∈Gers(X, F∗, p + m)p be a cocycle in the Gersten complex,
and {Y 1,2
r
}, 1 ≤r ≤p −1 be a patching system on X for the support Y of {fy} with the
freedom degree ar least zero; then a cocycle [{fy}] ∈A(X, F X
p+m)p is called a good cocycle
for {fy} ∈Gers(X, F∗, p+m)p with respect to the patching system {Y 1,2
r
}, 1 ≤r ≤p−1,
if it satisﬁes all conditions from Proposition 3.42 and Claim 3.44 (for each point η ∈Y ).
It follows from Proposition 3.42 and Claim 3.44 that good cocycles always exist.
Claim 3.47. Let X be a smooth variety over an inﬁnite perfect ﬁeld; then for any cocycle
{fy} ∈Gers(X, F∗, m)p in the Gersten complex and a patching system {Y 1,2
r
}, 1 ≤r ≤
p −1 on X for the support Y of {fy}, there exists a good cocycle [{fy}] ∈A(X, F X
m)p for
{fy} with respect to the patching system {Y 1,2
r
}.
The next technical lemma illustrates the freedom of choice in calculations with adeles.
Lemma 3.48. Let X be a smooth variety over an inﬁnite perfect ﬁeld and let the collec-
tion {fy} ∈Gers(X, F∗, m)p be supported on an equidimensional subvariety Y ⊂X. Sup-
pose that d{ efey} = {fy}, where { efey} ∈Gers(X, F∗, m)p−1. Suppose that f ∈A(X, F X
m)p
is such that νX(f) = {fy} and fU = 0, where fU ∈A(U, F U
m)p is the restriction of f
to U = X\Y . Let {Y 1,2
r
} be a patching system on X for Y ; then there exists an adele
ef ∈A(X, F X
m)p−1 such that d ef = f, νX( ef) = { efey} and efU is a good cocycle on U for
{ efey}U ∈Gers(U, F∗, m)p−1 with respect to the restriction of the patching system {Y 1,2
r
}
to U.
46


## Page 47


Proof. We put B• = Ker(νX : A(X, F X
m)• →Gers(X, F∗, m)•). Since by Lemma 2.23,
νX is surjective, we see that the complex B• is exact by Theorem 3.34.
Let ef1 ∈
A(X, F X
m)p−1 be such that νX( ef1) = { efex}. We have d(d( ef1)−f) = 0 and νX(d( ef1)−f) =
0, hence there exists h ∈Bp−1 such that dh = d( ef1) −f. The adele ef2 = ef1 −h satisﬁes
d ef2 = f, νX( ef2) = { efey}.
If p = 1, then the adele ( ef2)U is a good cocycle for { efey}U ∈Gers(U, m)p−1 on
U.
Suppose that p ≥2.
Let ef3 ∈A(U, F U
m)p−1 be a good cocycle for { efey}U ∈
Gers(U, F∗, m)p−1 with respect to the restriction of the patching system {Y 1,2
r
} to U.
We have dU( ef3 −( ef2)U) = −fU = 0, νU( ef3 −( ef2)U) = 0. Therefore there exists h ∈Bp−2
U
such that dU(h) = ef3 −( ef2)U. Here we put B•
U = ker(νU) and dU denotes the diﬀerential
in the adelic complex on U. Let h′ ∈A(X, F X
m)p−2 be the extension by zero of h from U
to X, i.e., we put h′
η0...ηp−2 = hη0...ηp−2 if η0 . . . ηp−2 is a ﬂag on U and, otherwise, we put
h′
η0...ηp−2 = 0 (see Corollary 2.7(i)). It follows easily that h′ ∈Bp−2 and the restriction
of h′ from X to U is equal to h. Thus the adele ef = ef2 + dh′ ∈A(X, F X
m)p−1 satisﬁes all
needed conditions.
4
Applications to K-cohomology
4.1
Generalities on K-cohomology and K-adeles
Recall several standard facts on sheaves of K-groups and K-cohomology.
Consider a weak homology theory for Noetherian schemes given by F∗= K′
∗. The
corresponding Zariski homology sheaves will be denoted by K′
n, n ∈Z.
We put
Gers(X, n)• = Gers(X, K′
∗, n)•, i.e., Gers(X, n)p =
L
η∈X(p) Kn−p(k(η)). For a scheme
X and an integer n ≥0, let KX
n be the sheaf associated to the presheaf given by the
formula U 7→Kn(U) for any open subset U ⊂X, where Kn(U) = πn+1(BQP(U)) and
P(U) is the exact category of coherent locally free sheaves on U. The Zariski cohomology
groups H•(X, KX
n ) are called the K-cohomology of X. Evidently, there is a morphism
of sheaves KX
n →(K′
n)X for any n ≥0, which is an isomorphism if X is regular and
separated. The sheaf KX = L
n≥0
KX
n is the sheaf of supercommutative associative rings.
Any morphism of schemes f : X →Y deﬁnes a homomorphism of sheaves of algebras
f ∗: KY →f∗KX.
For any integers m, n ≥0, there is a morphism of complexes of sheaves Gers(X, m)•⊗
KX
n →Gers(X, m+n)• given by the formula {fη}⊗g 7→{fη·i∗
ηg}, where i∗
η is the natural
morphism of sheaves i∗
η : KX
n →(iη)∗Kn(k(η)), iη : η ֒→X. Thus the complex of sheaves
Gers(X)• = L
m≥0
Gers(X, m)• is a right module over the sheaf of associative rings KX and
the natural morphism L
m≥0
(K′
m)X →Gers(X)• is a homomorphism of KX-modules. For
any proper morphism f : X →Y of irreducible schemes, there is a canonical morphism
of complexes of sheaves Rf∗Gers(X)•[d] = f∗Gers(X)•[d]
f∗
−→Gers(Y )•, where d =
dim(f) = dim(X) −dim(Y ).
The projection formula tells that this morphism is a
47


## Page 48


homomorphism of KY -modules via the homomorphism KY →f∗KX. Therefore general
properties of resolutions of sheaves imply the following fact.
Lemma 4.1. Let f
: X
→Y
be a proper morphism of schemes.
Let a1
∈
Hp1(X, Gers(X)•) = Hp1(Y, Rf∗Gers(X)•), bi ∈Hpi(Y, KY ), 2 ≤i ≤k be classes
in K-cohomology groups such that their k-th higher product mk(a1, b2, . . . , bk) is well de-
ﬁned, where we consider Rf∗Gers(X)• as a module over KY via the homomorphism
KY
→f∗KX →Rf∗KX.
Then the higher products mk(a1, f ∗(b2), . . . , f ∗(bk)) and
mk(f∗(a1), b2, . . . , bk) are also well deﬁned and there is an equality
f∗(mk(a1, f ∗(b2), . . . , f ∗(bk))) = (−1)d(p2+...+pk)mk(f∗(a1), b2, . . . , bk).
Remark 4.2. An alternative, more direct, way to show Lemma 4.1 for smooth varieties
over an inﬁnite perfect ﬁeld is to use Theorem 3.34 and the adelic projection formula
from Proposition 2.24.
Remark 4.3. Let us recall that Massey higher products for a right DG-module M• over
a DG-ring A• are deﬁned via the higher diﬀerentials in the spectral sequence associ-
ated with the Hochschild bicomplex (M• ⊗(A•)⊗(p−1))q. More precisely, Massey higher
products have the form
mk : (Hi1(M•) ⊗Hi2(A•) ⊗. . . ⊗Hik(A•))◦→◦(Hi1+...+ik−k(M•)),
where for a group G, the notation (G)◦means that we take a certain subgroup in G and
◦(G) means that we take a certain quotient of G. In particular, for a sheaf of associative
algebras A on a topological space X and a sheaf M of right modules over A, there are
Massey higher products in cohomology groups H•(X, A) and H•(X, M); to deﬁne them
one should take multiplicative resolutions for sheaves A and M on X (e.g., Godement
resolutions), see more details in [6].
If X is a regular scheme of ﬁnite type over a ﬁeld, then KX
n = (K′
n)X, the complex
of sheaves Gers(X, n)• is quasiisomorphic to KX
n , and Hn(X, KX
n ) = CHn(X) for any
n ≥0 (see [22] and also Proposition 3.8).
By Section 2.1, the complex A(X, KX)• is a DG-ring, any morphism of schemes
f : X →Y deﬁnes a DG-homomorphism A(Y, KY )• →A(X, KX)•, and the com-
plex Gers(X)• is a right DG-module over the DG-ring A(X, KX)•.
By Proposition
2.24, for any proper morphism f : X →Y of irreducible schemes, the morphism
Gers(X)•[d] →Gers(Y )• is a homomorphism of right DG-modules over A(Y, KY )• via
the homomorphism A(Y, KY )• →A(X, KX)•, where d = dim(f).
Remark 4.4. It seems that there is no way to deﬁne a direct image map on the adelic
complexes A(X, KX)• for proper morphisms of smooth varieties. This fact can be already
seen in the simplest cases of ﬁnite morphisms or a closed embeddings. Nevertheless it is
expected that there exists a complete version of K-adeles such that the complete adelic
complex would have a (non-canonical) direct image map.
Also, completed K-adeles
should correspond to the global class ﬁeld theory of arithmetical schemes, see [20]. Some
particular cases were treated in [18]. However the “complete” theory is still to be built.
48


## Page 49


Remark 4.5. It follows from what is said above that for each p ≥0, there is a canonical
map αp from Hp(A(X, KX
p )•) to the bivariant Chow group Ap(X
id
−→X) (see [8]). In
addition, the natural map βp : Hp(X, Kp) →Ap(X
id
−→X) factors through αp.
Question 4.6. Does there exist a singular variety X such that the image Im(αp :
Hp(A(X, KX
p )•) →Ap(X
id
−→X)) is strictly bigger than the image Im(βp : Hp(X, Kp) →
Ap(X
id
−→X)), i.e., such that adelic cocycles deﬁne new elements in the bivariant Chow
groups?
Now let us ﬁx an inﬁnite perfect ﬁeld k and consider K′
∗as an l.a.f. homology theory
over k, see Example 3.11, 1). Let X be an irreducible smooth variety over k; then by
Proposition 3.42 and Claim 3.44, for any algebraic cycle Y = P niYi of codimension p on
X, there is a good cocycle [Y ] = [{1Y }] ∈A(X, KX
p )p, where {1Y } denotes a collection
from
L
η∈X(p) Z that equals ni ∈Z at the generic point ηi of Yi for each i and equals 0 ∈Z
at all other schematic points η ∈X(p). Let us give two examples for adelic classes of
subvarieties.
Let D be a (not necessary reduced or eﬀective) divisor on X, d = dim(X). For each
schematic point η ∈X, consider a local equation sη ∈k(X)∗of D in Xη = Spec(OX,η).
Evidently, sξ/sη ∈O∗
X,η whenever ξ ∈η. Thus we get a 1-cocycle [D] ∈A(X, KX
1 )1 such
that the (Xη)-component of [D] is s−1
η
for η ̸= X and the (ηξ)-component of [D] is sη/sξ
for η ̸= X, ξ ∈η, ξ ̸= η. By construction, the class of [D] in H1(A(X, KX
1 )•) = CH1(X)
coincides with the class of D in the ﬁrst Chow group under the map νX. In [9], [11], and
Corollary 4.23 it is proved that the intersection product in Chow groups coincides up to
sign with the natural product in the corresponding K-cohomology groups. Thus we get
the following adelic formula for the intersection index of divisors D1, . . . , Dd when X is
proper:
(D1, . . . , Dd) = −
X
η0...ηd
[k(ηd) : k]νη0...ηd{s−1
1,η1, s2,η1/s2,η2, . . . , sd,ηd−1/sd,ηd} =
= −
X
η0...ηd
[k(ηd) : k]νη0...ηd{s−1
1,η1, s−1
2,η2, . . . , s−1
d,ηd},
where the last identity follows from reciprocity law. This formula was proved by diﬀerent
methods ﬁrst for d = 2 in [21] and for arbitrary d in [16]. We generalize the explicit
computations from [21] and [16] in the proof of Theorem 4.22.
The next example is the intersection of a 1-cycle C and a divisor D in the three-
dimensional irreducible smooth variety X over k. We describe explicitly a 2-cocycle [C]
in the adelic complex A(X, KX
2 )• that represents C. Let us choose an eﬀective reduced
divisor E with the following properties: for each schematic point η ∈X of codimension
at least two in X, there exists an element tη ∈K2(k(X)) and a subdivisor Eη ⊂E such
that sing(tη) ⊂E and dη(νXEη(tη)) = Cη. Recall that νXEη denotes the residue map
from K2(k(X)) to the direct sum of multiplicative groups of ﬁelds of rational functions
on all irreducible components of Eη (see Section 3.4), Cη is the restriction of C to Xη,
49


## Page 50


and dη is the diﬀerential in the local Gersten resolution on Xη. The existence of such
divisor E follows from Proposition 3.14 and Remark 3.31. Further, we deﬁne the adeles
f012 and f013 such that fXEηη = t−1
η
∈K2(k(X)), where tη is as above. We put all the
other components of f012 and f013 to be any elements from (KX
2 )η = K2(OX,η). For each
ﬂag ηξ of type (23), we have
dη(νXEη(tη)/νXEξ(tξ)) = 0,
hence there exists an element tηξ ∈K2(k(X)) such that
dη(tηξ) = νXEη(tη)/νXEξ(tξ).
This deﬁnes the adele f023. Finally, we see that for each ﬂag µηξ of type (123), the
product fµηξ = fXηξf −1
XµξfXµη belongs to (KX
2 )µ and is also an adele.
Thus we have
deﬁned the cocycle [C] = f ∈A(X, KX
2 )2 such that [C] represents the class of C in
H2(A(X, KX
2 )•) = CH2(X) with respect to the map νX. From this we get the following
intersection formula when X is proper:
(D, C) =
X
µηξ
[k(ξ) : k]νXµηξ{s−1
µ , fµηξ} =
X
µηξ
[k(ξ) : k]νXµηξ{s−1
µ , tηξ},
where, as above, sµ is the local equation of the divisor D at the point µ and µηξ ranges
over all ﬂags of type (123) on X. As in the previous case, the last equality follows from
reciprocity law.
Further, let us indicate a link between the adelic complex A(X, KX
n )• and coherent
adeles.
Proposition 4.7. Let X be a smooth variety over a ﬁeld k; then for any n ≥0, there
is a natural morphism of complexes
dlog : A(X, KX
n )• →a(X, Ωn
X)•,
where a(X, Ωn
X)• is the complex of rational coherent adeles (see [19] and [14], Proposition
5.2.1) and the local component of this morphism for a ﬂag η0 . . . ηp is equal to the natural
map Kn(Oη0) →Ωn
Oη0/k (see [2]).
Proof. Let us prove by induction on p that for any natural number p ≥0, any subset
M ⊂S(X)p, and any open subset U ⊂X, the map dlog : A(M, KU
n ) →a(M, Ωn
U) is
well deﬁned. Since the sheaf Ωn
X is locally free, it is 1-pure and we may suppose that
X\U = D is a divisor.
Suppose that p
=
0.
We have A(M, KU
n )
=
Q
η∈M
(KU
n )η and A(M, Ωn
U)
=
lim
−→
l≥0
Q
η∈M
(Ωn
X(lD))η and, by Lemma 4.8, we get the needed result. For p > 0, we have
a(M, Ωn
U) =
Y
η∈P (X)
a(ηM, (Ωn
U)η) =
Y
η∈P (X)
lim
−→
V
a(ηM, Ωn
U∩V ),
50


## Page 51


where for each schematic point η ∈P(X) the limit is taken over all open subsets V ⊂X
containing η (for the second equality we use that the adelic functor commutes with direct
limits of quasicoherent sheaves). Since the same equality holds for the adelic groups for
the sheaf KX
n , the induction step is proved.
The author is grateful to C. Soul´e for explaining the proof of the following lemma.
Lemma 4.8. Rational diﬀerential forms from the image of the map Kn(k(X)) →Ωn
k(X)/k
have pole of order at most one along each irreducible divisor D ⊂X.
Proof. Let us recall the construction of the map Kn(R) →Ωn
R/Z and its properties. There
are universal classes cn ∈lim
←−Hn(GLm(R), Ωn
R/Z), where the limit is taken over m ≥0;
they deﬁne the canonical maps Kn(R) →Hn(GL(R), Z)
cn
−→Ωn
R/Z. The map cn is trivial
on Hn(GLn−1(R), Z). Moreover, the composition R∗×. . .×R∗→H1(GL1(R), Z)×. . .×
H1(GL1(R), Z) →Hn(GLn(R), Z) →Hn(GL(R), Z)
cn
−→Ωn
R/Z is given by the formula
(r1, . . . , rn) 7→dr1
r1 ∧. . .∧drn
rn . Since one may suppose that dimX > 0, the ﬁeld F = k(X)
is inﬁnite. By the results of Suslin, see [25], there is an isomorphism Hn(GLn(F), Z) ∼=
Hn(GL(F), Z) and the natural map constructed above F ∗× . . . × F ∗→Hn(GLn(F), Z)
induces an isomorphism KM
n (F) ∼= Hn(GLn(F), Z)/Hn(GLn−1(F), Z).
Since for any
non-zero rational functions f1, . . . , fn ∈k(X)∗, the diﬀerential form df1
f1 ∧. . . ∧dfn
fn has
pole of order at most one along each irreducible divisor D ⊂X, the lemma is proved.
Remark 4.9. It follows from [25] that for any ﬁeld F the natural composition KM
n (F) →
Kn(F) →Ωn
F/Z is given by the formula {f1, . . . , fn} 7→(−1)n(n −1)! df1
f1 ∧. . . ∧dfn
fn .
Remark 4.10. There is an equality dlog(f · g) = −
(m+n−1)!
(m−1)!(n−1)!dlog(f) · dlog(g), where
f ∈A(X, KX
m)•, g ∈A(X, KX
n )•, and in the right hand side we consider the product in
the DG-ring L
n≥0
a(X, Ωn
X).
Remark 4.11. Let Y be an algebraic cycle of codimension p on a smooth variety X over
an inﬁnite perfect ﬁeld k. Then there is an explicit construction for the class of Y in the
rational adelic group a(X, Ωp
X)p. Indeed, one should take the image under the map dlog
of the explicit (good) class [Y ] of Y in A(X, KX
p )p constructed in Proposition 3.42.
4.2
Euler characteristic with support for K-groups
The construction and the results of this section are needed for the proof of Theorem
4.22 given in the next section. These results are not new; for example, they follow from
Waldhausen K-theory of perfect complexes, developed in [26] or they may be obtained
by using R-spaces constructed in [3]. However the author did not ﬁnd a reference for an
explicit construction, that is why this section is written.
By ΩS denote the loop space of a pointed space (S, s0). Let f : (X, x0) →(Y, y0) be
a continuous map of pointed topological spaces. Consider the mapping path ﬁbration
M(f) = {(x, ϕ)|x ∈X, ϕ : I →Y, ϕ(0) = f(x)},
51


## Page 52


where I is the interval [0, 1]. Recall that the homotopy ﬁber F(f) is the ﬁber over y0
of the natural map M(f) →Y , (x, ϕ) 7→ϕ(1). Notice that F(f) and M(f) are pointed
spaces with the point (x0, ϕ0), where ϕ0 is the constant map to y0. There is a natural map
ΩY →F(f), deﬁned by γ 7→(x0, γ). Moreover, the composition ΩX →ΩY →F(f) is
canonically homotopic to the constant map to (x0, ϕ0) ∈F(f). Indeed, the homotopy
G : ΩX × I →F(f)
is given by
(γ, t) 7→(γ(t), ϕt),
where ϕt(s) = (f ◦γ)(t + s(1 −t)).
Let M be an exact category, E3 be the exact category of exact triples of objects in
M. The exact functors
{0 →M′ →M →M′′ →0} 7→(M′, M′′)
and
(M′, M′′) 7→{0 →M′ →M′ ⊕M′′ →M′′ →0}
induce the maps BQE3 →BQM × BQM and BQM × BQM →BQE3, respectively.
The well-known result of Quillen says that these two maps of pointed spaces are homotopy
inverse (see [22], Theorem 2). Furthermore, let M′ and M′′ be two exact subcategories in
M and let E′
3 be the category of exact triples in M such that in the above notations the
object M′ is in M′ and the object M′′ is in M′′. Then, analogously, BQE′
3 is homotopy
equivalent to BQM′ × BQM′′.
In what follows we suppose for simplicity that M is an abelian category (which is
enough for further applications).
Lemma 4.12. Let Cn be the exact category of length n complexes of objects in M
and let En be the full subcategory in Cn consisting of all exact complexes.
We put
Bi = Im(Mi−1 →Mi) for a complex M•. Then the natural maps BQCn →BQMn+1,
BQEn →BQMn induced by the exact functors
{0 →M0 →. . . →Mn →0} 7→(M0, . . . , Mn),
{0 →M0 →. . . →Mn →0} 7→(B1, . . . , Bn),
respectively, are homotopy equivalences.
Moreover, the following diagram of pointed
spaces is commutative up to homotopy:
BQEn
−→
BQMn
↓
↓i
BQCn
−→
BQMn+1,
where the horizontal maps are as deﬁned above, the left vertical arrow is the natural
inclusion, and i is induced by the exact functor
(B1, . . . , Bn) 7→(B1, B1 ⊕B2, . . . , Bn−1 ⊕Bn, Bn).
52


## Page 53


Proof. We follow the proof of Theorem 1.11.7 from [26]. Nevertheless we do not use the
language of K-theory spectra of Waldhausen categories.
The proof is by induction on n ≥3. The case n = 3 is the result of Quillen mentioned
above. For arbitrary n ≥4, consider the natural inclusions of categories En−1 ֒→En and
M ֒→En given by the functors
{0 →M0 →. . . Mn−1 →0} 7→{0 →M0 →. . . →Mn−1 →0 →0}
and
M 7→{0 →0 . . . →0 →M →M →0},
respectively. The category En is equivalent to the category of exact triples in En that
start with an object from En−1 ֒→En and end with an object in E2 = M ֒→En. Indeed,
the explicit equivalence is given by the functor
M• 7→{0 →τ≤(n−1)(M•) →M• →{0 →Bn →Bn →0}},
where τ≤i is the usual truncation functor associated to the canonical ﬁltration on com-
plexes. Thus, applying the result of Quillen modiﬁed above, we get that BQEn is homo-
topy equivalent to BQEn−1 × BQE. Combining the explicit view of this homotopy and
the inductive hypothesis, we get the desired result for En.
The analogous reasoning leads to the needed result for Cn. In this case we should
replace the canonical ﬁltration on complexes by the “bˆete” ﬁltration and consider the
inclusion of categories M ֒→Cn given by the functor
M 7→{0 →. . . →0 →M →0}.
Finally, for any exact complex M• from En, we have the exact sequences
0 →Bi →Mi →Bi+1 →0
for all 0 < i < n. It follows from the proof of Corollary 1, §3, [22] that this leads to the
needed homotopy equivalence in the diagram from the lemma.
Let F be the homotopy ﬁber of the natural map BQEn →BQCn and put KN =
ΩBQN for any exact category N .
Corollary 4.13. The inclusion of the categories M ֒→Cn given by the functor M 7→
{0 →M →0 →. . . →0} induces the map KM →KCn →F such that the composition
is a homotopy equivalence.
Proof. Let us compute the induced map on homotopy groups. By Lemma 4.12, for each
i ≥0, there is a commutative diagram
πi(KEn)
−→
πi+1(BQM)n
↓
↓i∗
πi(KCn)
−→
πi+1(BQM)n+1,
53


## Page 54


where the horizontal arrows are the isomorphisms induced by the maps described in
Lemma 4.12. Thus there is a canonical isomorphism πi(F) ∼= πi+1(BQM) given by the
alternated sum of projections πi+1(BQM)n+1 →πi+1(BQM). Moreover, the composi-
tion πi+1(BQM) ∼= πi(KM) →πi(KCn) →πi(F) ∼= πi+1(BQM) is the identity map.
Since by Milnor’s result, KM has the homotopy type of a CW-complex, we conclude by
the well known theorem of Whitehead.
By M(S) denote the abelian category of coherent sheaves on a scheme S. We put
En(S) = En, Cn(S) = Cn, F(S) = F, and K(S) = KM for M = M(S).
Proposition 4.14. Let S be a closed subscheme in the scheme T and let Cn(T, S) be a
full subcategory in Cn(T) consisting of complexes whose cohomology sheaves have support
on S, i.e., complexes whose restriction to T\S is in En(T\S). Then there exists a well
deﬁned up to homotopy the “Euler characteristic with support” map χ : KCn(T, S) →
K(S) with the following properties:
(i) the induced homomorphism χ∗: K0(Cn(T, S)) →K′
0(S) is equal to
[F •] 7→
n
X
i=0
(−1)i[Hi(F •)],
where F • is in Cn(T, S) (here we imply the canonical isomorphism K′
0(S) ∼= K′
0(eS),
induced by the closed embeddings Sred ֒→S and eSred ֒→eS, where eS is any closed
subscheme in T such that Sred = eSred);
(ii) χ commutes with the direct image under closed embeddings; namely consider a
closed subscheme i : T ′ ֒→T and put S′ = S ×T T ′. Then the following diagram of
pointed spaces is commutative up to homotopy:
KCn(T, S)
χ
−→
K(S)
↑i∗
↑i∗
KCn(T ′, S′)
χ
−→
K(S′);
(iii) χ commutes with the restriction to open subsets; namely consider an open subset
j : U ֒→T and put V = S ×T U. Then the following diagram of pointed spaces is
commutative up to homotopy:
KCn(T, S)
χ
−→
K(S)
↓j∗
↓j∗
KCn(U, V )
χ
−→
K(V ).
Proof. The natural map KCn(T, S) →F(T\S), deﬁned by the diagram
KCn(T, S)
−→
KEn(T\S)
↓
↓
KCn(T)
−→
KCn(T\S)
↓
↓
F(T)
−→
F(T\S),
54


## Page 55


is canonically homotopy trivial. Hence there is a well deﬁned map
KCn(T, S) →F {F(T) →F(T\S)} .
On the other hand, by Corollary 4.13 and by Quillen’s localization lemma (see [22]), the
diagram
K(T)
−→
K(T\S)
↓
↓
F(T)
−→
F(T\S)
induces a homotopy equivalence K(S) →F {F(T) →F(T\S)}. This deﬁnes the map
χ : KCn(T, S) →K(S) uniquely up to homotopy.
Now we prove (i), i.e., we compute explicitly χ∗on π0-groups.
Consider a point
[F •] in KCn(T, S) corresponding to a loop in BQCn(T, S) deﬁned by a complex F • from
Cn(T, S) in the standard way. There exists a homotopy inside BQCn(T, S) between the
loop [F •] and the sum of loops
[τ≤(n−1)F •] + [{0 →. . . →Bn →Bn →0}] + [Hn(F •)[−n]].
In addition, [Hn(F •)[−n]] is homotopic inside BQCn(T, S) to the sum
(−1)n[Hn(F •)] +
n−1
X
j=0
(−1)j[{0 →Hn(F •) →Hn(F •) →0}[−j]],
where the short complexes have support in degrees 0 and 1. Continuing, we show by
induction that the initial loop may be homotoped inside BQCn(T, S) to the sum of
P(−1)i[Hi(F •)] and some loops in BQEn(T). The classes of points in KCn(T, S), cor-
responding to loops in BQEn(T), evidently have zero image under χ∗on π0-groups, and
we are done.
For the proof of (ii) and (iii) one uses that the natural maps
T ′\S′ = (T\S) ×T T ′ ֒→T\S
and
U\V = (T\S) ×T U ֒→T\S
are closed embedding and open embedding, respectively. Also, one uses the fact that if
in the commutative diagram of pointed spaces
X
−→
Y
↓
↓
Z
−→
W
the vertical arrows are homotopy equivalences, then the diagram remains commutative up
to homotopy after we take the homotopy inverse to the vertical homotopy equivalences.
55


## Page 56


Remark 4.15. A similar way to deﬁne the Euler characteristic with support on K-groups
K∗(Cn(T, S)) →K∗(S) is to use the R-space construction from [3], Section 1. Recall that
for any exact category M, the space RM has the same homotopy type as BQM and
the H-space RM has a canonical inverse map, not just an inverse up to homotopy. Thus
there is the Euler characteristic map RCn(T, S) →RM(T) such that its composition
with the natural map RM(T) →RM(T\S) is canonically homotopy trivial. This gives
a well deﬁned map RCn(T, S) →RM(S) up to homotopy.
Now consider a complex P• from Cn(T, S) such that P• consists of ﬂat sheaves on
T. Let the map ∗· P• : K(T) →K(S) be the composition of the map induced by
the exact functor ∗⊗OT P• : M(T) →Cn(T, S), F 7→F ⊗OT P• and the map χ :
KCn(T, S) →K(S) from Proposition 4.14. The map ∗·P• is well deﬁned up to homotopy.
A standard argument shows that the maps ∗· P• and ∗· (P′)• are homotopy equivalent
for quasiisomorphic complexes P• and (P′)•. By Proposition 4.14(i), for any class [F]
from K′
0(T) we have [F] · P• = P(−1)iHi(F ⊗OT P•) ∈K′
0(S).
Proposition 4.16. Let P• be a ﬁnite ﬂat resolution of OS on T (here the complex P•
has support in non-positive terms) and suppose that T admits an ample line bundle (for
example, T is quasi-projective). Then the map ∗· P• is homotopic to the map f ∗, where
f : S ֒→T is the closed embedding (see [22], §7, 2.5).
Proof. By Quillen resolution theorem (see [22], §4, Corollary 1), the space BQM(T)
is homotopy equivalent to its subspace BQF(T), where F(T) is the exact category of
coherent sheaves on T that are Tor-independent with OS. For BQF(T) we have the
exact sequence of functors from F(T) to Cn(T, S)
0 →τ ′
≤0(∗⊗OT P•) →∗⊗OT P• →∗⊗OT OS →0
where we put
τ ′
≤0(A•) = {. . . →Ai →. . . →A−1 →B0 →0},
for any complex A•. It follows from the proof of Corollary 1, §3, [22] that the map
K(∗⊗OT P•) is homotopic to the map K(τ ′
≤0(∗⊗OT P•)) + K(∗⊗OT OS), where the sum
is taken with respect to the natural H-structures on K-spaces of exact categories. More-
over, the image of the map K(τ ′
≤0(∗⊗OT P•)) is in the space K(En(T)) ⊂K(Cn(T, S))
and the map K(∗⊗OT OS) equals f ∗on K(F(T)). This concludes the proof.
Remark 4.17. For the elements from K∗(T), the map ∗· P• is equal to the composition
of the usual restriction to S with multiplication by χ∗([P•]) ∈K′
0(S).
Proposition 4.18. Let i : T ′ ֒→T be a closed embedding and put S′ = S ×T T ′,
j : U = T\T ′ ֒→T, V = S ×T U. Consider arbitrary elements x ∈Km(S), y ∈K′
n(U),
where m, n ≥0, m + n ≥1. Then we have
ν(x · (y · P•)) = (−1)mx · (ν(y) · i∗P•) ∈K′
m+n−1(S′),
where ν : K′
∗(U) →K′
∗−1(T ′) denotes the usual boundary map (the same for V and S′).
56


## Page 57


Proof. By Proposition 4.14(ii),(iii), both squares in the following diagram of spaces are
commutative up to homotopy:
K(P(S)) ∧K(T ′)
∗·P•⊗∗
−→
K(S′)
↓i∗× id
↓i∗
K(P(S)) ∧K(T)
∗·P•⊗∗
−→
K(S)
↓j∗× id
↓j∗
K(P(S)) ∧K(U)
∗·P•⊗∗
−→
K(V ),
where P(S) denotes the exact category of locally free coherent sheaves on S and “∧”
denotes the wedge product of pointed topological spaces. Thus rest is a direct application
of Theorem 2.5 from [11].
Let us mention the following simple fact.
Lemma 4.19. Let S ֒→T be a closed embedding, Sred be the reduced scheme, j :
Sred →S be a natural embedding. Then j∗◦νred = ν, where ν : K′
∗(T\S) →K′
∗−1(S),
νred : K′
∗(T\S) →K′
∗−1(Sred) are the boundary maps.
Proof. This follows immediately from the commutativity of the diagram of CW-spaces
BQM(Sred)
j∗
−→
BQM(S)
↓
↓
BQM(T)
=
−→
BQM(T)
↓
↓
BQM(T\Sred)
=
−→
BQM(T\S)
after we pass to the long homotopy sequences, associated to the vertical sequences, which
are ﬁbrations up to homotopy.
Lemma 4.19 implies the following statement.
Corollary 4.20. Proposition 4.18 remains true after we change the schematic intersec-
tion S′ = S ×T T ′ by its reduced part S′
red.
Example 4.21. Let k be a ﬁeld, T be the local scheme (A2
k)(0,0) with coordinates (x, y),
T ′ = {xy = 0}, S = {x + y = 0}, P• = {OT
x+y
−→OT}. Let f(x), g(y) be rational
functions on the corresponding irreducible components of T ′ such that f(x) and g(y)
have the opposite valuations at the origin. These functions naturally deﬁne an element
α ∈K′
1(T ′). We have α · i∗P• = a/b ∈K1(k), where a and b are the main parts of f(x)
and g(y) in x and y, respectively.
57


## Page 58


4.3
Formula for product in K-cohomology
Let X be an irreducible smooth quasiprojective variety over an inﬁnite perfect ﬁeld,
Y , Z be two equidimensional subvarieties in X of codimensions p and q, respectively.
Consider two cocycles {fy} ∈
L
y∈Y (0) Km(k(y)) and {gz} ∈
L
z∈Z(0) Kn(k(z)) in the Gersten
complexes Gers(X, p + m)p and Gers(X, q + n)q, respectively.
Suppose that the subvarieties Y and Z intersect properly. In addition, suppose that
for any irreducible component w of the intersection W = Y ∩Z, the collections {fy}w
and {gz}w are represented by some elements αw and βw from the groups Km(Yw) and
K′
n(Zw), respectively (recall that the index w means the restriction of a collection to
Xw = Spec(OX,w)).
By Remark 3.31 and Remark 3.32, there are patching systems {Y 1,2
r
}, 1 ≤r ≤p −1
and {Z1,2
s }, 1 ≤s ≤q −1 on X for subvarieties Y and Z, respectively, with the freedom
degree at least zero such that the following conditions are satisﬁed:
(i) for any s, 1 ≤s ≤q −1, no irreducible component in Y ∩Z1
s is contained in Z2
s;
(ii) each irreducible component in Y 1,2
p−1 contains some irreducible component in Y , each
irreducible component in Y 1,2
r
, 2 ≤r ≤p−2, contains some irreducible component
in Y 1
r+1∪Y 2
r+1, and the analogous is true for the patching system Z1,2
s , 1 ≤s ≤q−1;
in particular, the subvarieties Y 1,2
r
and Y meet the subvarieties Z1,2
s
and Z properly.
Let f ∈A(X, KX
p+m)p and g ∈A(X, KX
q+n)q be good cocycles for the collections
{fy} and {gz} with respect to the patching systems {Y 1,2
r
}, 1 ≤r ≤p −1 and {Z1,2
s },
1 ≤s ≤q −1, respectively, such that {Y 1,2
r
} and {Z1,2
s } satisfy two conditions from
above (see Section 3.6).
Theorem 4.22. Let P• →OY be a ﬁnite ﬂat resolution of OY on X. Under the above
assumptions we have:
νX(f · g) = (−1)(p+m)q{αw · (βw · i∗
ZP•)} ∈
L
w∈W (0) Km+n(k(w)),
where iZ : Z ֒→X is the closed embedding (considered locally around w for each
summand) and the bar over αw denotes the image under the natural homomorphisms
Km(Yw) →Km(k(w)) for each point w.
Proof. Let η0 . . . ηp+q be a ﬂag of type (0 . . . p + q) on X. By condition (i) from Propo-
sition 3.42, we have fη0...ηp · gηp...ηp+q = 0 unless ηr is the generic point of an irreducible
component of Y 1
r for all r, 1 ≤r ≤p −1, ηp is the generic point of an irreducible com-
ponent of Y , ηp+s is the generic point of an irreducible component of the intersection
Y ∩Z1
s for all s, 1 ≤s ≤q −1, and ηp+q is the generic point of an irreducible component
of the intersection Y ∩Z.
Suppose that the ﬂag η0 . . . ηp+q enjoys this property. Combining the assumption on
the patching systems {Y 1,2
r
}, 1 ≤r ≤p −1 and {Z1,2
s }, 1 ≤s ≤q −1, condition (ii)
from Proposition 3.42, and Claim 3.44, we see that
fη0...ηp = efηp ∈Kp+m(Xηp\(Y 1
1 ∪Y 2
1 )), gηp...ηp+q = egηp+q ∈Kq+n(Xηp+q\(Z1
1 ∪Z2
1)),
58


## Page 59


where
dηpνXY 1
1 ...Y 1
p−1( efηp) = (−1)
p(p+1)
2
fηp = {fy}ηp,
dηp+qνXZ1
1...Z1
q−1(egηp+q) = (−1)
q(q+1)
2
{gz}ηp+q.
Henceforth, ν0...p(f · g)ηp...ηp+q = νXY 1
1 ...Y 1
p−1ηp( efηp · egηp+q).
We claim that the residue νXY 1
1 ...Y 1
p−1ηp( efηp · egηp+q) is equal to the product
(−1)
p(p+1)
2
fηp · i∗
ηpegηp+q ∈Km+q+n(k(ηp)), where iηp : Spec(k(ηp)) →X is the natural
morphism (notice that ηp does not belong to Z1
1 ∪Z2
1). This can be shown using Proposi-
tion 4.18 ﬁrst with S = T = Xηp, P• = OS, T ′ = (Y 1
1 ∪Y 2
1 )ηp and then, inductively, with
S = T = (Y 1
s )ηp, P• = OS, T ′ = (Y 1
s+1 ∪Y 2
s+1)ηp for 1 ≤s ≤p−1 (more precisely, for the
induction step we use that the cocycles f and g satisfy the conditions from Claim 3.44).
In addition, the product fηp · i∗
ηpegηp+q ∈Km+q+n(k(ηp)) equals the restriction to
Spec(k(ηp)) of the product
αηp+q · i∗
Y egηp+q ∈Km+q+n(Yηp+q\(Z1
1 ∪Z2
1)),
where iY : Y ֒→X is the closed embedding. Consequently, we have νp+q(f · g)w =
(−1)
p(p+1)
2
νY,Y ∩Z1
1,...,Y ∩Z1
q−1,w(αw · i∗
Y egw) if w is the generic point of an irreducible compo-
nent of the intersection W = Y ∩Z. Otherwise, νp+q(f · g)w = 0.
Let w be the generic point of an irreducible component of W. In what follows we
consider all schemes on X locally around the schematic point w, i.e., we consider their
restrictions to Xw = Spec(OX,w), though we denote them by the same letter.
Put
Z1
0 = X, Z1
q = Z and by is : Z1
s ֒→X denote the natural closed embedding for each
s, 0 ≤s ≤q. By Proposition 4.14 and Corollary 4.20, the following diagram commutes
up to sign (−1)m for all s, 0 ≤s ≤q −1:
K′
∗+m(Y ∩(Z1
s\(Z1
s+1 ∪Z2
s+1)))
←−
K′
∗(Z1
s\(Z1
s+1 ∪Z2
s+1))
↓
↓
K′
∗+m−1(Y ∩(Z1
s+1\Z2
s+1))
←−
K′
∗−1(Z1
s+1\Z2
s+1)),
where the vertical arrows are the compositions of the boundary maps with the restrictions
to open subsets and the horizontal arrows are the compositions of the map ∗· i∗
sP•
(respectively, ∗·i∗
s+1P•) with the multiplication on the right by the restriction of αηp+q ∈
Km(Y ) to the corresponding closed subsets in Y . Therefore, by Claim 3.44 and Remark
4.17, we get
νY,Y ∩Z1
1,...,Y ∩Z1
q−1,w(αw · i∗
Y egw) = νY,Y ∩Z1
1,...,Y ∩Z1
q−1,w(αw · (egw · P•)) =
= αw · ((−1)mqνXZ1
1...Z1
q−1w(egw) · i∗
ZP•) = (−1)mq+ q(q+1)
2
αw · (βw · i∗
ZP•).
Combining this with the equality νX = (−1)
(p+q)(p+q+1)
2
νp+q, we conclude the proof of the
theorem.
59


## Page 60


Let {fy} ∈Gers(X, p + m)p and {gz} ∈Gers(X, q + n)q be two Gersten cocycles as
above with one additional property: for any irreducible component w of the intersection
W = Y ∩Z, the collection {gz}w is represented by an element βw from the group Kn(Zw).
Corollary 4.23. Under the above assumptions, the product of the classes of {gy} and
{hz} in K-cohomology groups is represented by the Gersten cocycle
(−1)(p+m)q{(Y, Z; w)αw · βw} ∈
L
w∈W (0) Km+n(k(w)),
where (Y, Z; w) is the local intersection index of Y and Z at the component w.
In
particular, the intersection product in Chow groups coincides up to sign with the natural
product in the corresponding K-cohomology groups (the last assertion had been proved by
diﬀerent methods in [9] and [11]).
Proof. The composition of the morphisms of complexes Kn(OX) →A(X, Kn)•
νX
−→
Gers(X, n)• is identity on the (hyper)cohomology groups.
Therefore the product of
the classes of Gersten cocycles in K-cohomology groups is represented by the image
under the map νX of the adelic product of the corresponding adelic cocycles.
On the other hand, we have (Y, Z; w) =
X
i≥0
(−1)il(Tor
OX,w
i
(OY,w, OZ,w)), where l(·)
is the length of an OX,w-module, i.e., the length of a ﬁltration whose adjoint quotients
are one-dimensional vector spaces over the ﬁeld k(w). Thus the lemma follows directly
from Theorem 4.22 and Remark 4.17.
Remark 4.24. If each generic point w of an irreducible component of the intersection
W = Y ∩Z is regular on Y and Z, then the conditions of Corollary 4.23 are satisﬁed.
4.4
Massey triple product and the Weil pairing
In this section we apply the adelic resolution to computation of some Massey triple
product.
Let X be a smooth variety of dimension d over an inﬁnite perfect ﬁeld k.
Consider elements α ∈CHp(X)l = Hp(X, KX
p )l, β ∈CHq(X)l = Hq(X, KX
q )l, and
l ∈H0(X, KX
0 ) = Z such that p + q = d + 1. The triple (α, l, β) satisﬁes α · l = l · β = 0
in K-cohomology groups, hence there is a triple product
m3(α, l, β) ∈Hd(X, Kd+1)/(α · Hq−1(X, KX
q ) + Hp−1(X, KX
p ) · β).
We compute this product explicitly.
Let us represent the classes α ∈CHp(X)l and
β ∈CHq(X)l by cycles Y = P
i mi ·Yi and Z = P
j nj ·Zj, respectively, where Yi and Zj
are irreducible subvarieties in X of codimensions p and q, respectively, and mi, nj ∈Z.
Since p + q = d + 1, it can be assumed that the supports |Y | = ∪iYi and |Z| = ∪jZj
do not intersect. Let {fey} ∈Gers(X, p)p−1 and {gez} ∈Gers(X, q)q−1 be two collections
such that d{fey} = lY , d{gez} = lZ and let eY ⊂X and eZ ⊂X be the supports of {fey}
and {gez}, respectively. It follows the moving lemma for higher Chow groups (see [4] and
also [15]) that for X either aﬃne or projective, one can choose {fey} and {gez} such that
60


## Page 61


the intersections eY ∩|Z| and |Y | ∩eZ are proper and the rational functions fey and gez are
regular at all points from the intersections eY ∩|Z| and |Y | ∩eZ, respectively. For each
point x ∈eY ∩|Z|, we put f(x) = Q
ey f (ey,Z;x)
ey
(x). Similarly, we deﬁne g(x) for each point
x ∈|Y | ∩eZ.
Proposition 4.25. Under the above assumptions, the triple product m3(α, l, β) is rep-
resented by the Gersten cocycle
(−1)pq(
X
x∈eY ∩|Z|
f(x) · x +
X
x∈|Y |∩eZ
g−1(x) · x) ∈Gers(X, d + 1)d.
Proof. By Remark 3.31 and Remark 3.32, there are patching systems {Y 1,2
r
}, {eY 1,2
r
},
{Z1,2
s }, and { eZ1,2
s } on X for subvarieties |Y |, eY , |Z|, and eZ, respectively, such that
the pairs of patching systems ({Y 1,2
r
}, { eZ1,2
s }) and ({eY 1,2
r
}, {Z1,2
s }) satisfy conditions
of Theorem 4.22.
Let [Y ] ∈A(X, Kp)p and [Z] ∈A(X, q)q be good cocycles for Y
and Z with respect to the patching systems {Y 1,2
r
} and {Z1,2
s } on X, respectively. By
Lemma 3.48, there are adeles f ∈A(X, KX
p )p−1 and g ∈A(X, KX
q )q−1 such that df =
l[Y ], dg = l[Z], and the restrictions fU and gV are good cocycles for {fey}U and {gez}V
with respect to the patching systems {eY 1,2
r
}U and { eZ1,2
s }V respectively, where U =
X\|Y | and V = X\|Z|. By deﬁnition, m3(α, l, β) is represented by the Gersten cocycle
νX(f ·[Z]−(−1)p[Y ]·g). Since νX(f ·[Z]) = νU((f ·[Z])U) and νX([Y ]·g) = νV (([Y ]·g)V ),
we conclude by Theorem 4.22 and Corollary 4.23.
Let X be a smooth projective variety of dimension d over a ﬁeld k. Evidently, for
any degree zero element α ∈CHd(X), we have π∗(α · H0(X, KX
1 )) = π∗(α · O∗(X)) = 1,
where π∗: Hd(X, KX
d+1) →k∗is the direct image map associated with the structure
morphism π : X →Spec(k).
Proposition 4.26. The subgroup Hd−1(X, KX
d )·Pic0(X) ⊂Hd(X, KX
d+1) is in the kernel
of the direct image map π∗: Hd(X, KX
d+1) →k∗.
Proof. After the base change, one may assume that the ground ﬁeld k is algebraically
closed. Consider a K1-chain {fj} ∈Gers(X, d)d−1 with P
j div(fj) = 0 and a group
homomorphism Pic0(X)(k) →k∗given by β 7→π∗({fj} · β). We claim that this ho-
momorphism is induced by a regular morphism from the Picard variety Pic0(X) to the
algebraic group Gm and therefore is identically equal to 1 ∈k∗.
For each j, by C′
j denote the complement to the divisor of the function fj on Cj.
For any closed point γ ∈Pic0(X), there exists a rational section s of the Poincar´e line
bundle on the product X ×Pic0(X) such that the restriction Dγ to X ×{γ} of the divisor
D = P miDi of the section s meets the curve C × {γ} properly and this intersection
is contained in C′
j × {γ}. Clearly, this condition holds for all closed points β from a
suﬃciently small open neighborhood U of the point γ in Pic0(X). Let aij be the degree
of the natural ﬁnite map Di ∩(Cj × U) →U. We get a regular morphism
ef : U →
Y
i
Symaij(C′
j)
f
−→Gm,
61


## Page 62


where f = Q
i(Symaij(fj))mi.
Moreover, for any point β ∈U, there is an equality
ef(β) = Q
i,j
Q
x∈(Di)β∩Cj
f
miaij(x)
j
(x), where aij(x) is the intersection index of the divisor
(Di)β with Cj at a point x. Therefore by Corollary 4.23, π∗({fj} · β) = ef(β)(−1)d. This
proves the needed statement.
By Proposition 4.26, for any elements α ∈CHd(X)l, β ∈Pic0(X)l, the direct image
of the Massey triple product m3(α, l, β) = π∗(m3(α, l, β)) is well deﬁned.
Proposition 4.27. Suppose that l is prime to char(k); then for any elements α ∈
CHd(X)l, β ∈Pic0(X)l, there is an equality
m3(α, l, β) = ψl(α, β)(−1)d,
where ψl is the Weil pairing between the l-torsion of Albanese and Picard varieties of X.
Proof. Since both sides of the equality evidently do not change under extensions of the
ground ﬁeld, we can assume that the ﬁeld k is algebraically closed. First, suppose that
dim(X) = 1 and consider elements L, M ∈Pic0(X)l. Choose two adeles (in fact, ideles)
f, g ∈A(X, KX
1 )1 that correspond to L and M, respectively.
There are two adeles
ef, eg ∈A(X, KX
1 )0 such that d ef = f l, deg = gl (we write the group law for K1-groups in
the multiplicative way). By deﬁnition, we have
m3(L, l, M) =
Y
x∈X
( efX, gXx)x(fXx, egx)x,
where (·, ·)x is the tame symbol in the discrete valuation ring OX,x. We may assume that
the supports of the divisors D = −div(f) and E = −div(g) do not intersect. In this case
we get φl(L, M) = fX(E) · gX(−D). This formula for the Weil pairing ψl(L, M) of L
and M is well known. The proof can be found in [13], [17], and [10] (these three proofs
use diﬀerent methods).
Now suppose that X is not a curve. Let i : C ֒→X be a general (d−1)-th hyperplane
section of X. Consider two elements M ∈Pic0(C)l, L ∈Pic0(X)l. The projection
formula for Weil pairing (following, for example, from that for ´etale cohomology) implies
that ψl(i∗(M), L) = ψl(M, i∗(L)). The projection formula for Massey higher products,
stated in Lemma 4.1, implies that φl(i∗(M), L) = φl(M, i∗(L))(−1)d−1. On the other
hand, it is well known that the map i∗: Pic0(C)l →Alb(X)l is surjective. Thus, by the
previous step, we get the needed result.
Propositions 4.25 and 4.27 imply the following formula.
Corollary 4.28. Let the class α ∈CHd(X)l be represented by a zero-cycle z = P
i mi·zi
and let the class β ∈Pic0(X)l be represented by a divisor D such that z does not intersect
with D. Suppose that div(g) = lD with g ∈k(X)∗and d({fm}) = lz, where d is the
diﬀerential in the Gersten complex on X, fm ∈k(Cm)∗, and Cm are irreducible curves
on X. Assume that for any m the rational function fm is regular at all points from the
62


## Page 63


intersection of D with Cm. Then in the notations from Proposition 4.25 we have the
following formula for the Weil pairing of α and L:
ψl(α, L) = (
Y
x∈C∩D
f(x) ·
Y
i
g−mi(zi))(−1)d.
References
[1] A. A. Beilinson, “Residues and adeles”, Funct. Anal. And Appl., 14 (1980), 34–35.
[2] S. Bloch,
“Algebraic
K-theory
and
crystalline
cohomology”,
Publications
Math´ematiques de l’I.H.´E.S., 46 (1977), 187–268.
[3] S. Bloch, “Height pairing for algebraic cycles”, Journal of Pure and Applied Algebra,
34 (1984), 119–145.
[4] S. Bloch, “Alegraic cycles and higher K-theory”, Advances in Mathematics, 61
(1986), 267–304.
[5] S. Bloch, A. Ogus, “Gersten’s conjecture and homology of schemes”, Ann. Scient.
Ec. Norm. Sup., 7 (1974), 181–202.
[6] C. Deninger, “Higher order operations in Deligne cohomology”, Schriftenreihe Math.
Inst. Univ. M¨unster 3, 3 (1991).
[7] T. Fimmel, A. N. Parshin, “An introduction to the higher adelic theory”, preprint
(1999).
[8] W. Fulton, “Intersection Theory”, Ergebnisse der Mathematik und ihrer Grenzgebi-
ete. 3. Folge. A Series of Modern Surveys in Mathematics, Springer Verlag (1984).
[9] H. Gillet, “Comparison of K-theory spectral sequences, with applications”, Springer
Lecture Notes, 854 (1981), 141–167.
[10] S. Gorchinskiy, “Poincare biextensions and ideles on the algebraic curve”, Sbornik
Mathematics, 197:1 (2006), 25–38.
[11] D. Grayson, “Products in K-theory and intersecting algebraic cycles”, Inventiones
Mathematicae, 47 (1978), 71–83.
[12] R. Hartshorne, “Resudues and duality”, Lecture Note in Mathematics, 20 (1966).
[13] E. W. Howe, “The Weil pairing and the Hilbert symbol”, Math. Ann., 305:2 (1996),
387–392.
[14] A. Huber, “On the Parshin–Beilinson adeles for schemes”, Abh. Math. Sem. Univ.
Hamburg, 61 (1991), 249–273.
[15] M. Levine, “Mixed motives”, Math. Surveys and Monographs, 57 (1998).
63


## Page 64


[16] V. G. Lomadze, “On the intersection index of divisors”, Izv. Akadem. Nauk. SSSR,
44 (1980), 1120–1130.
[17] M. Mazo, “Weil pairing and tame symbols”, Math. Notes, 77:5 (2005), 797–800.
[18] D. Osipov, “Adelic constructions of direct images of diﬀerentials and symbols”,
Sbornik Mathematics, 188:5 (1997), 59–84.
[19] A. N. Parshin, “On the arithmetic of two-dimensional schemes I. Repartitions and
residues”, Izv. Akad. Nauk SSSR, 40:4 (1976), 736–773.
[20] A. N. Parshin, “Abelian coverings of arithmetic schemes”, Dokl. Akad. Nauk SSSR,
243:4 (1978), 855–858.
[21] A. N. Parshin, “Chern classes, adeles and L-functions”, J. Reine Angew. Math., 341
(1983), 174–192.
[22] D. Quillen, “Higher Algebraic K-theory”, Lecture Notes in Mathematics, 341
(1973), 85–147.
[23] M. Rost, “Chow groups with coeﬃcients”, Documenta Mathematica, 1:16 (1996),
319–393.
[24] J.-P. Serre, “Groupes alg´ebriques et corps de classes”, Hermann, Paris (1959).
[25] A. Suslin, “Homology of GLn, characteristic classes and Milnor K-theory”, Lecture
Notes in Mathematics, 1046 (1984), 357–375.
[26] R. W. Thomason, T. Trobaugh, “Higher Algebraic K-theory of Schemes and of De-
rived Categories”, Progress in Mathematics, 88 (1990), 247–435.
[27] A. Yekutieli, “The action of adeles on the residue complex”, Comm Algebra, 31:8
(2003), 4131–4151.
64

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 0705_2597v2_adelic_resolution_for_homology_sheaves
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2007/0705_2597V2_ADELIC_RESOLUTION_FOR_HOMOLOGY_SHEAVES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

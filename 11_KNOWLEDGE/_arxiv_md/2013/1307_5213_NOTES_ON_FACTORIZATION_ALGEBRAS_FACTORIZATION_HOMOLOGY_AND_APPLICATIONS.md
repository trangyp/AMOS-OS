---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1307.5213
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1307.5213_Notes_on_factorization_algebras__factorization_homology_and_applications

> Source: 1307.5213_Notes_on_factorization_algebras__factorization_homology_and_applications.pdf

> Pages: 122

---


## Page 1


Notes on factorization algebras, factorization
homology and applications
Gr´egory Ginot
Institut Math´ematiques de Jussieu Paris Rive Gauche,
Universit´e Pierre et Marie Curie - Sorbonne Universit´es
April 22, 2014
Abstract
These notes are an expanded version of two series of lectures given at the
winter school in mathematical physics at les Houches and at the Vietnamese
Institute for Mathematical Sciences. They are an introduction to factorization
algebras, factorization homology and some of their applications, notably for
studying En-algebras. We give an account of homology theory for mani-
folds (and spaces), which give invariant of manifolds but also invariant of
En-algebras. We particularly emphasize the point of view of factorization al-
gebras (a structure originating from quantum ﬁeld theory) which plays, with
respect to homology theory for manifolds, the role of sheaves with respect to
singular cohomology. We mention some applications to the study of mapping
spaces, in particular in string topology and for (iterated) Bar constructions
and study several examples, including some over stratiﬁed spaces.
Contents
1
Introduction and motivations
3
1.1
Eilenberg-Steenrod axioms for homology theory of spaces
. . . .
4
1.2
Notation and conventions . . . . . . . . . . . . . . . . . . . . . .
7
2
Factorization homology for commutative algebras and spaces and de-
rived higher Hochschild homology
10
2.1
Homology theory for spaces and derived Hochschild homology . .
10
2.2
Pointed spaces and higher Hochschild cohomology . . . . . . . .
14
2.3
Explicit model for derived Hochschild chains . . . . . . . . . . .
16
2.4
Relationship with mapping spaces . . . . . . . . . . . . . . . . .
20
2.5
The wedge product of higher Hochschild cohomology . . . . . . .
23
1
arXiv:1307.5213v2  [math.AT]  20 Apr 2014


## Page 2


3
Homology Theory for manifolds
24
3.1
Categories of structured manifolds and variations on En-algebras .
24
3.2
Factorization homology of manifolds . . . . . . . . . . . . . . . .
28
4
Factorizations algebras
33
4.1
The category of factorization algebras . . . . . . . . . . . . . . .
33
4.2
Factorization homology and locally constant factorization algebras
38
5
Operations for factorization algebras
44
5.1
Pushforward . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
5.2
Extension from a basis
. . . . . . . . . . . . . . . . . . . . . . .
46
5.3
Exponential law: factorization algebras on a product
. . . . . . .
47
5.4
Pullback along open immersions and equivariant factorization al-
gebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
5.5
Example: locally constant factorization algebras over the circle . .
51
5.6
Descent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
6
Locally constant factorization algebras on stratiﬁed spaces and cate-
gories of modules
53
6.1
Stratiﬁed locally constant factorization algebras . . . . . . . . . .
54
6.2
Factorization algebras on the interval and (bi)modules . . . . . . .
56
6.3
Factorization algebras on pointed disk and En-modules . . . . . .
58
6.4
More examples . . . . . . . . . . . . . . . . . . . . . . . . . . .
61
7
Applications of factorization algebras and homology
69
7.1
Enveloping algebras of En-algebras and Hochschild cohomology
of En-algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . .
69
7.2
Centralizers and (higher) Deligne conjectures . . . . . . . . . . .
72
7.3
Higher string topology
. . . . . . . . . . . . . . . . . . . . . . .
77
7.4
Iterated loop spaces and Bar constructions . . . . . . . . . . . . .
79
7.5
En-Koszul duality and Lie algebras homology . . . . . . . . . . .
84
7.6
Extended topological quantum ﬁeld theories . . . . . . . . . . . .
85
8
Commutative factorization algebras
87
8.1
Classical homology as factorization homology . . . . . . . . . . .
87
8.2
Cosheaves as factorization algebras
. . . . . . . . . . . . . . . .
90
9
Complements on factorization algebras
93
9.1
Some proofs related to the locally constant condition and the push-
forward . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
93
9.2
Complements on § 6.2
. . . . . . . . . . . . . . . . . . . . . . .
96
9.3
Complements on § 6.3
. . . . . . . . . . . . . . . . . . . . . . .
98
2


## Page 3


10 Appendix
105
10.1 ∞-category overview . . . . . . . . . . . . . . . . . . . . . . . .
105
10.2 En-algebras and En-modules
. . . . . . . . . . . . . . . . . . . .
110
1
Introduction and motivations
These notes are an introduction to factorization algebras and factorization homol-
ogy in the context of topological spaces and manifolds. The origin of factoriza-
tion algebras and factorization homology, as deﬁned by Lurie [L3] and Costello-
Gwilliam [CG], are to be found in topological quantum ﬁeld theories and con-
formal ﬁeld theories. Indeed, they were largely motivated and inﬂuenced by the
pioneering work of Beilinson-Drinfeld [BD] and also of Segal [S2, S3]. Factor-
ization homology is a catchword to describe homology theories speciﬁc to say ori-
ented manifolds of a ﬁxed dimension n. There are also variant speciﬁc to many
other classes of structured manifold of ﬁxed dimension. Typically the structure in
question would be a framing1 or a spin structure or simply no structure at all.
Factorization algebras are algebraic structures which shed many similarities
with (co)sheaves and were introduced to describe Quantum Field Theories much
in the same way as the structure of a manifold or scheme is described by its sheaf
of functions [BD, CG]. They are related to factorization homology in the same
way as singular cohomology is related to sheaf cohomology.
Unlike classical singular homology for which any abelian group can be used
as coefﬁcient of the theory, in order to deﬁne factorization homology, one needs a
more complicated piece of algebraic data: that of an En-algebra2. These algebras
have been heavily studied in algebraic topology ever since the seventies where
they were introduced to study iterated loop spaces and conﬁguration spaces [BV,
Ma, S1]. They have been proved to also have deep signiﬁcance in mathemati-
cal physics [Ko, CG], string topology [CS, CV] and (derived) algebraic geome-
try [BD, FG, PTTV, L4]. E1-algebras are essentially the same thing as A∞-algebras,
that is homotopy associative algebras. On the other hand, E∞-algebras are homo-
topy commutative algebras. In general the En- structures form a hierarchy of more
and more homotopy commutative algebra structures. In fact, an En-algebra is an
homotopy associative algebra whose multiplication µ0 is commutative up to an
homotopy operator µ1. This operator is itself commutative up to an homotopy
operator µ2 and so on up to µn−1 which is no longer required to be homotopy
commutative.
Since factorization homology depends on (some class of) both manifold and
En-algebra, they also give rise to invariant of En-algebras. These invariants have
proven useful as we illustrate in § 7. For instance, in dimension n = 1, factoriza-
1that is a trivialization of the tangent bundle
2More accurately, En-algebras are the piece of data needed in the case of framed manifolds. For
other structured manifolds, one needs En-algebras equipped with additional structure; for instance
an invariance under their natural SO(n)-action in the oriented manifold case
3


## Page 4


tion homology evaluated on a circle is the usual Hochschild homology of algebras
(together with its circle action inducing cyclic homology as well). For n = ∞, fac-
torization homology gives rise to an invariant of topological spaces3 (sometimes
called higher Hochschild homology [P]) which we recall in § 2. It is easier to study
and interesting in its own since it is closely related to mapping spaces, their derived
analogues and observables of classical topological ﬁeld theories.
We give the precise axioms of homology theory of manifolds in § 3. Factoriza-
tion homology can be computed using ˇCech complexes of factorization algebras,
which, as previously alluded to, are a kind of “multiplicative, non-commutative”
analogue of cosheaves. Deﬁnitions, properties and many examples of factorization
algebras are discussed in § 4. Factorization algebras were introduced to describe
observables of Quantum Field Theories [CG, BD] but they also are a very conve-
nient way to encode and study many algebraic structures which arose in algebraic
topology and mathematical physics as we illustrate in § 4. In particular, in § 6 we
study in depth locally constant factorization algebras on stratiﬁed spaces and their
link with various categories of modules over En-algebras, giving many examples.
We also give a detail account of various operations and properties of factorization
algebras in § 5. We then (§ 7) review several applications of the formalism of fac-
torization algebras and homology. Notably to cohomology and deformations of
En-algebras, (higher) Deligne conjecture and also in (higher) string topology and
for Bar constructions of iterated loop spaces (and more generally to obtain models
for iterated Bar constructions with their algebraic structure). In § 8 , we consider
the case of commutative factorization algebras and prove their theory reduces to
the one of cosheaves. In particular, we cover the pedagogical example of classical
homology (with twisted coefﬁcient) viewed as factorization homology.
1.1
Eilenberg-Steenrod axioms for homology theory of spaces
Factorization homology and factorization algebras generalize ideas from the ax-
iomatic approach to classical homology of spaces (and (co)sheaf theory) which we
now recall. We then explain how they can be generalized. The usual (co)homology
groups of topological spaces are uniquely determined by a set of axioms. These
are the Eilenberg-Steenrod axioms which were formulated in the 40s [ES].
Classically they express that an homology theory for spaces is uniquely deter-
mined by (ordinary) functors from the category of pairs (X,A) (A ⊂X) of spaces to
the category of (N)-graded abelian groups satisfying some axioms. Such a functor
splits as the direct sum H∗(X,A) = L
i≥0 Hi(X,A) where Hi(X,A) is the degree i
homology groups of the pair. This homology group can in fact be deﬁned as the
homology of the mapping cone cone(A ,→X) of the inclusion of the pair. Fur-
ther, the long exact sequence in homology relating the homology of the pair to the
homology of A and X is induced by a short exact sequence of chain complexes
C∗(A) ,→C∗(X) ↠C∗(X,A) (where C∗is the singular chain complex). Similarly,
3and not just manifolds of a ﬁx dimension
4


## Page 5


the Mayer-Vietoris exact sequence is induced by a short exact sequence of chain
complexes.
This suggests that the classical Eilenberg-Steenrod axioms can be lifted at the
chain complex level. That is, we can characterize classical homology as a functor
from the category of spaces (up to homotopy) to the category of chain complexes
(up to quasi-isomorphism).
Let us formalize a bit this idea. A homology theory H for spaces is a functor
H : Top →Chain(Z) from the category Top of topological spaces4 to the category
Chain(Z) of chain complexes over Z (in other words differential graded abelian
groups). This functor has to satisfy the following three axioms.
1. (homotopy invariance) The functor H shall send homotopies between maps
of topological spaces to homotopies between maps of chain complexes.
2. (monoidal) The functor H shall be deﬁned by its value on the connected
components of a space. Hence we require it sends disjoint unions of topolog-
ical spaces to direct sum, that is the canonical map ⊕α∈IF(Xα) →H (`
α∈I Xα)
is an homotopy equivalence5 (here I is any set).
3. (excision) There is another additional property encoding (given the other
ones) the classical excision property as well as the Mayer-Vietoris principle.
The additional property essentially stipulates the effect of gluing together
two CW-complexes along a sub-complex. Let us formulate it this way: as-
sume i : Z ,→X and j : Z ,→Y are inclusions of closed sub CW-complex
of X and Y. Let X ∪Z Y ∼= X `Y/(i(z) = j(z), z ∈Z) be the pushout of
X, Y along Z. The functoriality of H gives maps H (Z)
i∗→H (X) and
H (Z)
j∗→H (Y); hence a chain complex morphism H (Z)
i∗−j∗
→H (X) ⊕
H (Y) . Functoriality also yields a natural map H (X)⊕H (Y) →H (X ∪Z
Y) whose composition with i∗−j∗is null.
The excision axioms requires that the canonical map
cone

H (Z)
i∗−j∗
→H (X)⊕H (Y)

−→H (X ∪Z Y)
is an homotopy equivalence. Here cone(f) is the mapping cone6 (inChain(Z))
of the map f of chain complexes.
We can state the following theorem (which follows from Corollary 20 and is the
(pre-)dual of a result of Mandell [M1] for cochains).
Theorem 1 (Eilenberg-Steenrod). Let G be an abelian group. Up to natural ho-
motopy equivalence, there is a unique homology theory for spaces, that is functor
4for simplicity we assume that we consider only spaces homotopy equivalent to CW-complexes
5sometimes this map is required to be an actual isomorphism but this is not needed
6if we know that f :C∗→D∗is injective, then cone(f) is quasi-isomorphic to the quotient chain
complex D∗/C∗. See for instance [W] for mapping cones of general chain maps.
5


## Page 6


H : Top →Chain(Z) satisfying axioms 1, 2 and 3 and further the dimension ax-
iom:
H (pt) ≃→G.
The functor in Theorem 1 is of course given by the usual singular chain com-
plex with value in G. We can even assume in the theorem that G is any chain
complex, in which case we recover extraordinary homology theories7.
Theorem 1 implies that the category of functors satisfying axioms 1, 2, 3 is
(homotopy) equivalent to the category of chain complexes; the equivalence being
given by the evaluation of a functor at the point. To assign to a chain complex V∗
an homology theory, one consider the functor X 7→C∗(X,Z)⊗V∗.
For a CW-complex X, the singular cohomology H∗(X,G) can be computed
as sheaf cohomology of X with value in the constant sheaf GX of locallly con-
stant functions on X with values in G. In particular, the singular cochain complex
is naturally quasi-isomorphic to the derived functor RΓ(GX) of sections of GX.
Replacing GX by a locally constant sheaf (with germs G) yields cohomology with
local coefﬁcient in G8. This point of view realizes singular cohomology (with local
coefﬁcient) as a special case of the theory of sheaf/ ˇCech cohomology which also
has other signiﬁcance and applications in geometry when allowing more general
sheaves.
Note that the homotopy invariance axiom can be reinterpreted as saying that
the functor H is continuous. Indeed, there are natural topologies on the mor-
phism sets of both categories. For instance, one can consider the compact-open
topology on the set of maps HomTop(X,Y) (see Example 61 for Chain(Z)). Any
continuous functor, that is a functor H such that the maps HomTop(X,Y) →
HomChain(Z)(H (X),H (Y)) are continuous, sends homotopies to homotopies (and
homotopies between homotopies to homotopies between homotopies and so on).
Note also that excision axiom really identiﬁes H (X ∪Z Y) with a homotopy
colimit.
It is precisely the homotopy coequalizer hocoeq

H (Z)
i∗⇒
j∗
H (X) ⊕
H (Y)

which is computed by the mapping cone cone(i∗−j∗). Further, in this
axiom, we do not need H to be precisely the cone but any natural chain complex
quasi-isomorphic to it will do the job. This suggests to actually use a more ﬂex-
ible model than topological categories. A convenient way to deal simultaneously
with topological categories, homotopy colimits (in particular homotopy quotients)
and identiﬁcation of chain complexes up to quasi-isomorphism is to consider the
∞-categories associated to topological spaces and chain complexes and ∞-functors
between them (see Appendix 10.1, Examples 60 and 61). The passage from topo-
logical categories to ∞-categories essentially allows to work in categories in which
7in this case, the uniqueness is not necessarily true if one works at the homology level instead of
chain complexes.
8if G is a linear representation of a group H and X is the classifying space of H, then one recovers
this way the group (co)homology of H with value in G
6


## Page 7


(weak) homotopy equivalences have been somehow “inverted” but which still re-
tain enough information of the topology of the initial categories.
Furthermore, in the monoidal axiom, we can replace the direct sum of chain
complexes by any symmetric monoidal structure, for instance by the tensor prod-
uct ⊗of chain complexes. This yields the notion of homology theory for spaces
with values in (Chain(Z),⊗) see § 2.1.1. The latter are not determined by a mere
chain complex but by a (homotopy) commutative algebra A. This theory is called
factorization homology for spaces and commutative algebras and its main proper-
ties are detailled in § 2. In fact, already at this level, we see that one needs to replace
the cone construction in the excision axiom by an appropriate derived functor.
To produce invariant of manifolds which are not invariant of spaces, one needs
to replace Top by another topological category of manifolds. For instance, ﬁxing
n ∈N, one can consider the category Mﬂdfr
n whose objects are framed manifolds
of dimension n and whose morphisms are framed embeddings. In that case, an ho-
mology theory is completely determined by an En-algebra. The precise deﬁnitions
and variants of homology theories for various classes of structured manifolds (in-
cluding the local coefﬁcient ones) and the appropriate notion of coefﬁcient is the
content of § 3.
The (variants of) En-algebras which arise as coefﬁcient of homology theory
for manifolds can be seen as a special case of factorization algebras, and more
precisely as locally constant factorization algebras, which are to factorization al-
gebras what (acyclic resolutions of) locally constant sheaves are to sheaves. This
point of view is detailed in § 4.2 and extended to stratiﬁed spaces in § 6. The latter
case gives simple9 description of several categories of modules over En-algebras as
well as categories of En-algebras acting on Em-algebras, which is used in the many
applications of § 7.
1.2
Notation and conventions
1. Let k be a commutative unital ring. The ∞-category of differential graded
k-modules (i.e. chain complexes) will be denoted Chain(k). The (derived)
tensor product over k will be denoted ⊗. The k-linear dual of M ∈Chain(k)
will be denoted M∨.
2. All manifolds are assumed to be Hausdorff, second countable, paracompact
and thus metrizable.
3. We write Top for the ∞-category of topological spaces (up to homotopy) and
Topf for its sub ∞-category spanned by the (spaces with the homotopy type
of) ﬁnite CW-complexes. We also denote Top∗, resp. sSet∗, the ∞-categories
of pointed topological spaces and simplicial sets. We write C∗(X) and C∗(X)
for the singular chain and cochain complex of a space X. We write sSet for
9in the sense that the cosheaf condition satisﬁed by factorization algebras encodes some topology
which, from the classical En-operad point of view necessitates an heavier homotopical machinery.
7


## Page 8


the ∞-category of simplicial sets (up to homotopy) which is equivalent to
Top.
4. The ∞-categories of unital commutative differential graded algebras (up tho
homotopy) will be denoted byCDGA. We simply refer to unital commutative
differential graded algebras as CDGAs.
5. Let n ∈N∪{∞}. By an En-algebra we mean an algebra over an En-operad.
We write En-Alg for the ∞-category of (unital) En-algebras (in Chain(k)).
See Appendix: § 10.2. We also write En-ModA, resp. E1-LModA, resp.
E1-RModA the ∞-categories of En-A-modules, resp. left A-modules, resp.
right A-modules.
6. The ∞-category of (small) ∞-categories will be denoted ∞-Cat.
7. We work with a cohomological grading (unless otherwise stated) for all our
(co)homology groups and graded spaces, even when we use subscripts to
denote the grading (so that our chain complexes have a funny grading). In
particular, all differentials are of degree +1, of the form d : Ai →Ai+1 and
the homology groups Hi(X) of a space X are concentrated in non-positive
degree. If (C∗,dC) ∈Chain(k), we denote C∗[n] the chain complex given by
(C∗[n])i := Ci+n with differential (−1)ndC.
8. We will denote PFacX, resp. FacX, resp. Faclc
X the ∞-categories of pref-
actorization algebras, resp. factorization algebras, resp. locally constant
factorization algebras over X. See Deﬁnition 15.
9. Usually, if C a (topological or simplicial or model) category, we will use the
boldface letter C to denote the ∞-category associated toC (see Appendix 10).
This is for instance the case for the categories of topological spaces or chain
complexes or CDGAs mentionned above.
10. Despite their names, the values of Hochschild or factorization (co)homology
will be (co)chain complexes (up to equivalences), i.e. objects of Chain(k),
or objects of another ∞-category such as E∞-Alg.
These notes deal mainly with applications of factorization algebras in algebraic
topology and homotopical algebra. However, there are very interesting applications
to mathematical physics as described in the work of Costello et al [CG, C2, C3],
[GrGw, Gw] and also beautiful applications in algebraic geometry and geometric
representation theory, for instance see [BD, FG, Ga1, Ga2].
We almost always refer to the existing literature for proofs; though there are
some exceptions to this rule, mainly in sections § 5, § 6 and § 8, where we treat
several new (or not detailed in the literature) examples and results related to fac-
torization algebras. To help the reader browsing through the examples in § 5 and
§ 6, the longer proofs are postponed to a dedicated appendix, namely § 9. Some
8


## Page 9


other references concerning factorization algebras and factorization homology in-
clude [L3, L2] and [An, AFT, Ca2, F1, F2, GTZ2, GTZ3, Ta].
About ∞-categories:
We use ∞-categories as a convenient framework for homo-
topical algebra and in particular as higher categorical derived categories. In our
context, they will typically arise when one consider a topological category or a
category M with a notion of (weak homotopy) equivalence. The ∞-category asso-
ciated to that case will be a lifting of the homotopy category Ho(M ) (the category
obtained by formally inverting the equivalences). It has spaces of morphisms and
composition and associativity laws are deﬁned up to coherent homotopies. We
recall some basic examples and deﬁnitions in the Appendix: § 10.1.
Topological categories and continuous functors between them are actually a
model for ∞-categories and (∞-)functors between them. By a topological cate-
gory we mean a category C endowed with a space of morphisms MapC (x,y) be-
tween objects such that the composition MapC (x,y) × MapC (y,z) →MapC (x,z)
is continuous. A continuous functor F : C →D between topological categories
is a functor (of the underlying categories) such that for all objects x, y, the map
MapC (x,y) F→MapD(F(x),F(y)) is continuous. In fact, every ∞-category admits
a strict model, in other word is equivalent to a topological category (though ﬁnd-
ing a strict model can be hard in practice). One can also replace, in the previous
paragraph, topological categories by simplicially enriched categories, which are
the same thing as topological categories where spaces are replaced by simplicial
sets (and continuous maps by maps of simplicial sets). In practice many topo-
logical categories we consider are geometric realization of simplicially enriched
categories.
The reader can thus substitute topological category to ∞-category in every
statement of these notes (or also simplicially enriched or even differential graded10
), but modulo the fact that one may have to replace the topological or ∞-category
in question by another equivalent topological one. The same remark applies to
functors between ∞-categories. Furthermore, many constructions involving factor-
ization algebras are actually carried out in (topological) categories (which provide
concrete models to homotopy equivalent (derived) ∞-category of some algebraic
structures).
If C is an ∞-category, we will denote MapC (x,y) its space of morphisms from
x to y while we will simply write HomD(x,y) for the morphism set of an ordinary
category D (that is a topological category whose space of morphisms are discrete).
Many derived functors of homological algebra have natural extensions to the
setting of ∞-categories. In that case we will use the usual derived functor notation
to denote their canonical lifting to ∞-category and to emphasize that they can be
computed using the usual resolutions of homological algebra. For instance, we will
denote (M,N) 7→M ⊗L
A N for the functor E1-RModA × E1-LModA →Chain(k)
lifting the usual tensor product of left and right modules to their ∞-categories.
10in this case, we refer to [To] for the needed homotopy categorical framework on dg-categories
9


## Page 10


There is a slight exception to this notational rule. We denote M ⊗N the derived
tensor products of complexes in Chain(k). We do not use a derived tensor product
notation since it will be too cumbersome and since in practice it will often be
applied in the case where k is a ﬁeld or M, N are projective over k.
Acknowledgments. The author thanks the Newton Institute for Mathematical Sci-
ences for its stimulating environment and hospitality during the time when most of
these notes were written. The author was partially supported by ANR grant HOGT.
The author deeply thanks Damien Calaque for all the numerous conversations
we had about factorization stuff and also wish to thank Kevin Costello, John Fran-
cis, Owen Gwilliam, Geoffroy Horel, Fr´ed´eric Paugam, Hiro-Lee Tanaka, Thomas
Tradler and Mahmoud Zeinalian for several enlightening discussions related to the
topic of theses notes.
2
Factorization homology for commutative algebras and
spaces and derived higher Hochschild homology
Factorization homology restricted to commutative algebras is also known as higher
Hochschild homology and has been studied (in various guise) since at least the
end of the 90s (see the approach of [EKMM, MCSV] to topological Hochschild
homology, or, the work of Pirashvili [P] which is closely related to Γ-homology).
Though its axiomatic description is an easy corollary of the description of Top
as a symmetric monoidal category with pushouts, it has a lot of nice properties
and appealing combinatorial description in characteristic zero (related to rational
homotopy theory `a la Sullivan). We review some of its main properties in this
Section.
2.1
Homology theory for spaces and derived Hochschild homology
2.1.1
Axiomatic presentation
Let us ﬁrst start by deﬁning the axioms of an homology theory for spaces with val-
ues in the symmetric monoidal ∞-category (Chain(k),⊗) (instead of (Chain(Z),⊕)).
The (homotopy) commutative monoids in (Chain(k),⊗) are the E∞-algebras (Def-
inition 34). In characteristic zero, one can restrict to differential graded commuta-
tive algebras since the natural functor CDGA →E∞-Alg is an (homotopy) equiva-
lence.
The ∞-category Top has a symmetric monoidal structure given by disjoint
union of spaces X `Y, which is also the coproduct of X and Y in Top. The identity
map idX : X →X yields a canonical map X `X
`idX
−→X which is associative and
commutative in the ordinary category of topological spaces. Hence X is canoni-
cally a commutative algebra object in (Top,`). And so is its image by a symmetric
monoidal functor. We thus have:
10


## Page 11


Lemma 1. Let (C ,⊗) be a symmetric monoidal ∞-category. Any symmetric monoidal
functor F : Top →C has a canonical lift ˜F : Top →E∞-Alg(C ).
In particular, any homology theory Top →Chain(k) shall have a canonical
factorization Top →E∞-Alg. This motivates the following deﬁnition.
Deﬁnition 1. An homology theory for spaces with values in the symmetric monoidal
∞-category (Chain(k),⊗) is an ∞-functor C H : Top × E∞-Alg →E∞-Alg (de-
noted (X,A) 7→CHX(A) on the objects), satisfying the following axioms:
i) (value on a point) there is a natural equivalence CH pt(A) ≃→A in E∞-Alg;
ii) (monoidal) the canonical maps (induced by universal property of coprod-
ucts)
O
i∈I
CHXi(A)
≃
−→CH`
i∈I Xi(A)
are equivalences (for any set I);
iii) (excision) The functor C H commutes with homotopy pushout of spaces,
i.e., the canonical maps (induced by the universal property of derived tensor
product)
CHX(A)
L⊗
CHZ(A)CHY(A)
≃
−→CHX∪h
ZY(A)
are natural equivalences.
Remark 1. If one replace Top by Topf then axiom ii) is equivalent to saying that,
the functors X 7→CHX(A) are symmetric monoidal.
Remark 2 (Homology theory for spaces in an arbitrary symmetric monoidal
∞-category). If (C ,⊗) is a symmetric monoidal ∞-category, we deﬁne an homol-
ogy theory with values in (C ,⊗) in the same way, simply replacing Chain(k) by
C (and thus E∞-Alg by E∞-Alg(C )).
All results (in particular the existence and uniqueness Theorem 2) in Sec-
tion 2.1, Section 2.2 and Section 2.3 still hold by just replacing the monoidal
structure of Chain(k) by the one of C , provided that C has colimits and that its
monoidal structure commutes with geometric realization.
Theorem 2.
1. There is an unique11 homology theory for spaces (in the sense
of Deﬁnition 1).
2. This homology theory is given by derived Hochschild chains, i.e., there are
natural equivalences
A⊠X ∼= CHX(A)
where A ⊠X is the tensor of the E∞-algebra A with the space X (see Re-
mark 37). In particular,
MapTop
 X,MapE∞-Alg(A,B)
 ∼= MapE∞-Alg(CHX(A),B).
(1)
11up to contractible choices
11


## Page 12


3. (generalized uniqueness) Let F : E∞-Alg →E∞-Alg be a functor. There is
an unique functor Top×E∞-Alg →E∞-Alg satisfying axioms ii), iii) in Def-
inition 1 and whose value on a point is F(A). This functor is (X,A) 7→
CHX(F(A)).
Remark 3. Theorem 2 still holds with Topf instead of Top (and where in axiom
ii) one restricts to ﬁnite sets I). In that case, it can be rephrased as follows:
Proposition 1. The functor F 7→F(pt) from the category of symmetric monoidal
functors Top f →Chain(k) satisfying excision12 to the category of E∞-algebras is
a natural equivalence.
Similarly, Theorem 2 can be rephrased in the following way:
“The functor F 7→F(pt) from the category of functors Top →Chain(k)
preserving arbitrary coproducts and satisfying excision to the category
of E∞-algebras is an natural equivalence.”
An immediate consequence of A ⊠X ∼= CHX(A) and the identity (1) is the
following natural equivalence
CHX×Y(A) ∼= CHX
 CHY(A)

(2)
in E∞-Alg. This is the “exponential law” for derived Hochschild homology.
Another interesting consequence of (1) is that, for any spaces K and X and E∞-
algebra A, the identity map in MapE∞-Alg(CHX×K(A),CHX×K(A)) yields a canoni-
cal element in MapTop
 K,MapE∞-Alg(CHX(A),CHX×K(A))

hence a canonical map
of chain complexes
tens : C∗
 K

⊗CHX(A) −→CHK×X(A).
(3)
Similarly, let f : K ×X →Y be a map of topological spaces, then we get a canonical
continuous map K −→MapE∞-Alg(CHX(A),CHY(A)) or equivalently a chain map
f∗: C∗(K)⊗CHX(A) −→CHY(A) in Chain(k) which is just the composition
C∗(K)⊗CHX(A) tens
−→CHK×X(A)
f∗
−→CHY(A)
where the last map is by functoriality of C H with respect to maps of topological
spaces.
Remark 4 (Group actions on derived Hochschild homology). Since C H is a
functor of both variables, CHX(A) has a natural action of the topological monoid
MapTop(X,X) (and thus of the group Homeo(X)), i.e., there is a monoid13 map
MapTop(X,X) →MapE∞-Alg(CHX(A),CHX(A)). By adjunction, we get a chain
map14 C∗
 MapTop(X,X)

⊗CHX(A) →CHX(A) which exhibits CHX(A) as a mod-
ule over MapTop(X,X) in E∞-Alg .
12by Lemma 1, the excision axiom makes sense for any such functor
13here, monoid means an homotopy monoid, that is an E1-algebra in the symmetric monoidal
category (Top,×)
14and higher homotopy coherences
12


## Page 13


2.1.2
Derived functor interpretation
We now explain a derived functor interpretation of derived Hochschild homology.
Recall (Example 65) that the singular chain functor of a space X has a natural struc-
ture of E∞-coalgebras. In other words, it is an object (abusively denoted C∗(X)) of
Fun⊗(Finop,Chain(k)) the category of contravariant symmetric monoidal functor
from ﬁnite sets to chain complexes.
We can identify an E∞-coalgebra C, resp. an E∞-algebra A, respectively, with a
right module, resp. left module over the (∞-)operad E∞; or equivalently with con-
travariant, resp. covariant, symmetric monoidal functors from Fin to Chain(k)).
We can thus form their (derived) tensor products C
L⊗
E∞
A ∈Chain(k) which is com-
puted as a (homotopy) coequalizer:
C
L⊗
E⊗∞
A ∼= hocoeq

a
f:{1,...,q}→{1,...,p}
C⊗p ⊗E∞(q, p)⊗A⊗q ⇒
a
n
C⊗n ⊗A⊗n
where the maps f : {1,...,q} →{1,..., p} are maps of sets. The upper map in the
coequalizer is induced by the maps f ∗: C⊗p ⊗E∞(q, p) ⊗A⊗q →C⊗q ⊗A⊗q ob-
tained from the coalgebra structure of C and the lower map is induced by the maps
f∗: C⊗p ⊗E⊗
∞(q, p)⊗A⊗q →C⊗p ⊗A⊗p induced by the algebra structure. One can
deﬁne similarly C
L⊗
FinA the derived tensor product of a covariant and contravariant
Fin-modules.
Proposition 2. Let X be a space and A be an E∞-algebra. There is a natural
equivalence (in Chain(k))
CHX(A) ∼= C∗(X)
L⊗
E∞
A.
If A has a structure of CDGA, then we further have CHX(A) ∼= C∗(X)
L⊗
FinA
Proof. Note that the E∞-coalgebra structure on C∗(X•) is given by the functor
Finop →Chain(k) deﬁned by I 7→k

HomFin(I,X•)

. The rest of the proof is the
same as in [GTZ2, Proposition 4].
Remark 5 (Factorization homology of commutative algebras as derived mapping
stacks). There is another nice interpretation of derived Hochschild homology in
terms of derived (or homotopical) algebraic geometry. Let dStk be the ∞-category
of derived stacks over the ground ring k described in details in [TV2, Section
2.2]. This category admits internal Hom’s that we denote by RMap(F,G) fol-
lowing [TV2, TV3] and further is also an enrichment of the homotopy category
of spaces.
Indeed, any simplicial set X• yields a constant simplicial presheaf
E∞-Alg →sSet deﬁned by R 7→X• which, in turn, can be stackiﬁed. We denote
X the associated stack, i.e. the stackiﬁcation of R 7→X•, which depends only on
13


## Page 14


the (weak) homotopy type of X•. For a (derived) stack Y ∈dStk, we denote OY
its functions, i.e., OY := RHom(Y,A1), (see [TV2]). A direct application of The-
orem 2 is:
Corollary 1 ([GTZ2]). Let R = RSpec(R) be an afﬁne derived stack (for in-
stance an afﬁne stack) [TV2] and X be the stack associated to a space X. Then
the Hochschild chains over X with coefﬁcients in R represent the mapping stack
RMap(X,R). That is, there are canonical equivalences
ORMap(X,R) ∼= CHX(R),
RMap(X,R) ∼= RSpec
 CHX(R)

If a group G acts on X, the natural action of G on CHX(A) (Remark 4) identiﬁes
with the natural one on RMap(X,R) under the equivalence given by Corollary 1.
2.2
Pointed spaces and higher Hochschild cohomology
In order to have a dual and relative versions of the construction of § 2.1, we consider
the (∞-)category Top∗of pointed spaces. Let τ : pt →X be a base point of X ∈
Top∗. The map τ yields a map of E∞-algebras A ∼= CHpt(A)
τ∗
−→CHX(A) and thus
makes CHX(A) an A-module. Let M be an E∞-module over A; for instance, take M
to be a module over a CDGA A. Note that M has induced left and right modules
structures15 over A.
Deﬁnition 2. Let A be an E∞-algebra and M be an E∞-module over A.
• The (derived) Hochschild cochains of A with values in M over (a pointed
topological space) X is given by
CHX(A,M) := RHomle ft
A
(CHX(A),M),
the (derived) chain complex of homomorphisms of underlying left E1-modules
over A (Deﬁnition 36).
• The (derived) Hochschild homology of A with values in M over (a pointed
space) X is deﬁned as
CHX(A,M) := M
L⊗
A CHX•(A)
the relative tensor product of (a left and a right) E1-modules over A.
The two deﬁnitions above depend on the choice of the base point even though
we do not write it explicitly in the deﬁnition.
Remark 6. One can also use the relative tensor products of E∞-modules over A
(as deﬁned, for instance, in [L3, KM]) for deﬁning the Hochschild homology
CHX(A,M). This does not change the computation (and makes Lemma 2 below
trivial) according to Proposition 40 (or [L3, KM]). The same remark applies to the
deﬁnition of derived Hochschild cohomology.
15Note also that there is an equivalence of ∞-categories E1-LModA ∼= E1-RModA if A ∈E∞-Alg
14


## Page 15


Since the based point map τ∗: A →CHX(A) is a map of E∞-algebras, the canon-
ical module structure of CHX(A) over itself induces a CHX(A)-module structure on
CHX(A,M) after tensoring by A (see [KM, Part V], [L3]):
Lemma 2. Let M be in E∞-ModA, that is, M is an E∞-A-module. Then CHX(A,M)
is canonically a E∞-module over CHX(A).
The Lemma is obvious when A is a CDGA.
We have the ∞-category E∞-Mod of pairs (A,M) with A an E∞-algebra and
M an A-module (Deﬁnition 35). Let πE∞: E∞-Mod →E∞-Alg be the canonical
functor.
Proposition 3 ([GTZ2, GTZ3]).
• The derived Hochschild chains (Deﬁnition 2)
induces a functor of ∞-categories CH : (X,M) 7→CHX(πE∞(M),M) from
Top∗×E∞-Mod to E∞-Mod which ﬁts into a commutative diagram
Top∗×E∞-Mod
for×πE∞

CH
/ E∞-Mod
πE∞

Top×E∞-Alg C H
/ E∞-Alg.
Here for : Top∗→Top forget the base point.
• The derived Hochschild cochains (Deﬁnition 2) induces a functor of ∞-
categories (X,M) 7→CHX•(A,M) from (Top∗)op × E∞-ModA to E∞-ModA,
which is further contravariant with respect to A.
In particular, if M = A, then we have an natural equivalence CHX(A,A) ∼=
CHX(A) in E∞-Mod16.
Remark 7 (Functor homology point of view). There is also a derived functor
interpretation of the above functors as in § 2.1.2. Let Fin∗be the ∞-category as-
sociated to the category of pointed ﬁnite sets (Example 57). If X is pointed, then
we have a functor ˜C∗(X) : Fin∗op →Chain(k) which sends a ﬁnite pointed set I to
C∗(Mappointed(I,X)) the singular chain on the space of pointed maps from I to X.
Further, let M be an E∞-module. Similarly to § 2.1.2 we ﬁnd a symmetric monoidal
functor ˜M : Fin∗→Chain(k). When M is a module over a CDGA A, denoting ∗
the base point, this is simply the functor ˜M({∗}`J) = M ⊗A⊗J, see [Gi]. This
functor actually factors through E1-LModA.
We have a dual version of ˜M, that we denote H (A,M) : Fin∗op →Chain(k),
deﬁned as H (A,M)(J) := HomA( ˜A(J),M) (where J 7→˜A(J) is the functor Fin∗→
E1-LModA deﬁned by the canonical E∞-module structure of A). See [Gi] for an
explicit construction when A is a CDGA and M a module.
A proof similar to the one of Proposition 2 yields:
16here we implicitly use the canonical functor E∞-Alg →E∞-Mod which sees an A-lagebra as a
module over itself
15


## Page 16


Proposition 4. There are natural equivalences
CHX(A,M) ∼= ˜C∗(X)
L⊗
Fin∗
˜M,
CHX(A,M) ∼= RHomFin∗( ˜C∗(X),H (A,M)).
2.3
Explicit model for derived Hochschild chains
Following Pirashvili [P], one can construct rather simple explicit chain complexes
computing derived Hochschild chains when the input is a CDGA. We mainly deal
with the unpointed case, the pointed one being similar and left to the reader.
In this section, we consider only CDGAs. Note that, if we assume k is of
characteristic zero, E∞-algebras are always homotopy equivalent to a CDGA so
that we do not loose much generality. This construction, using simplicial sets as
models for topological spaces, provides explicit semi-free resolutions for CHX(A)
which makes them combinatorially appealing.
Let (A = L
i∈Z Ai,d,µ) be a differential graded, associative, commutative al-
gebra and let n+ be the set n+ := {0,...,n}. We deﬁne CHn+(A) := A⊗n+1 ∼= A⊗n+.
Let f : k+ →ℓ+ be any set map, we denote by f∗: A⊗k+ →A⊗ℓ+, the linear map
given by
f∗(a0 ⊗a1 ⊗···⊗ak) = (−1)ε ·b0 ⊗b1 ⊗···⊗bℓ,
(4)
where bj = ∏i∈f −1(j) ai (or bj = 1 if f −1(j) = /0) for j = 0,...,ℓ. The sign ε in
equation (4) is determined by the usual Koszul sign rule of (−1)|x|·|y| whenever x
moves across y. In particular, n+ 7→CHn+(A) is functorial. Extending the con-
struction by colimit we obtain a well-deﬁned functor
Y 7→CHY(A) :=
lim
−→
Fin∋K→Y
CHK(A)
(5)
from sets to differential graded commutative algebras (since the tensor products
of CDGAs is a CDGA). Now, if Y• is a simplicial set, we get a simplicial CDGA
CHY•(A) and by the Dold-Kan construction a CDGA whose product is induced by
the shufﬂe product which is deﬁned (in simplicial degree p, q) as the composition
sh : CHYp(A)⊗CHYq(A) sh×
−→CHYp+q(A)⊗CHYp+q(A) ∼= CHYp+q(A⊗A)
µ∗
−→CHYp+q(A).
(6)
Here µ : A ⊗A →A denotes the multiplication in A (which is a map of algebras)
and, denoting si the degeneracies of the simplicial structure in CHY•(A),
sh×(v⊗w) = ∑
(µ,ν)
sgn(µ,ν)(sνq ...sν1(v)⊗sµp ...sµ1(w)),
where (µ,ν) denotes a (p,q)-shufﬂe, i.e. a permutation of {0,..., p+q−1} map-
ping 0 ≤j ≤p−1 to µj+1 and p ≤j ≤p+q−1 to νj−p+1, such that µ1 < ··· < µp
and ν1 < ··· < νq. The differential D : CHY•(A) →CHY•(A)[1] is given as follows.
16


## Page 17


The tensor products of chain complexes A⊗Yi have an internal differential which
we abusively denote as d since it is induced by the differential d : A →A[1]. Then,
the differential on CHY•(A) is given by the formula:
D
 O
i∈Yi
ai

:=
(−1)id
 O
i∈Yi
ai

+
i
∑
r=0
(−1)r(dr)∗
 O
i∈Yi
ai

,
where the (dr)∗: CHYi(A) →CHYi−1(A) are induced by the corresponding faces
dr : Yi →Yi−1 of the simplicial set Y•.
Deﬁnition 3. Let Y• be a simplicial set. The Hochschild chains over Y• of A is the
commutative differential graded algebra (CHY•(A),D,sh).
The rule (Y•,A) 7→(CHY•(A),D,sh) is a bifunctor from the ordinary discrete
categories of simplicial sets and CDGA to the ordinary discrete category of CDGA.
IfY• is a pointed simplicial set, we have a canonical CDGA map A ∼→CHpt•(A) →
CHY•(A). This allows to mimick Deﬁnition 2:
Deﬁnition 4. Let Y• be a simplicial set, A a CDGA and M an A-module (viewed as
a symmetric bimodule).
• The Hochschild chains of A with values in M over Y• are:
CHX•(A,M) := M ⊗
A CHX•(A).
• The Hochschild cochains of A with values in M over Y• are:
CHX•(A,M) = HomA(CHX•(A),M).
The above deﬁnition computes the derived Hochschild homology of Theo-
rem 2. Indeed, we have the adjunction |−| : sSet
∼
⇄
∼Top : ∆•(−) given by the geo-
metric realization |Y•| of a simplicial set and the singular set functor: n 7→∆n(X) :=
HomTop(∆n,X) (where ∆n ∈Top is the standard n-simplex). This adjunction is a
Quillen adjunction hence induces an equivalence of ∞-categories. Further (by unic-
ity Theorem 2) we have a commutative diagram (in Fun(sSet ×CDGA,E∞-Alg))
sSet ×CDGA
(Y•,A)7→CHY•(A)
/
|−| ≃

CDGA

Top×CDGA
/ Top×E∞-Alg
C H
/ E∞-Alg,
(7)
see [GTZ2, GTZ3] for more details. From there, we get
Proposition 5. One has natural equivalencesCHX•(A) ∼=CH|X•|(A) of E∞-algebras
as well as equivalences
CHX•(A,M) ∼= CH|X•|(A,M),
CHX•(A,M) ∼= CH|X•|(A,M)
of CH|X•|(A)-modules.
17


## Page 18


We now demonstrate the above combinatorial deﬁnitions in a few examples (in
which we assume, for simplicity, that A has a trivial differential).
Example 1 (The point and the interval). The point has a trivial simplicial model
given by the constant simplicial set ptn = {pt}. Hence
(CHpt•(A),D) := A 0←A id←A 0←A id←A···
which is a deformation retract of A (as a CDGA). A (pointed) simplicial model for
the interval I = [0,1] is given by In = {0,1··· ,n + 1}, hence in simplicial degree
n, CHIn(A,M) = M ⊗A⊗n+1 and the simplicial face maps are
di(a0 ⊗···an+1) = a0 ⊗···⊗(aiai+1)⊗···⊗an+1.
An easy computation shows that CHI•(A,M) = Bar(M,A,A) is the standard Bar
construction17 which is quasi-isomorphic to M.
Example 2 (The circle). The circle S1 ∼= I/(0 ∼1) has (by Example 1) a simplicial
model S1
• which is the quotient S1
n = In/(0 ∼n + 1) ∼= {0,...,n}. One computes
that the face maps di : S1
n →S1
n−1, for 0 ≤i ≤n −1 are given by di(j) is equal to
j or j −1 depending on j = 0,...,i or j = i+1,...,n and dn(j) is equal to j or 0
depending on j = 0,...,n −1 or j = n. For i = 0,...,n, the degeneracies si(j) is
equal to j or j+1 depending on j = 0,...,i or j = i+1,...,n. This is the standard
simplicial model of S1 cf. [L, 6.4.2]. Thus, CHS1•(A) = L
n≥0 A ⊗A⊗n and the
differential agrees with the usual one on the Hochschild chain complex C•(A) of A
(see [L]).
It can be proved that the S1 action on CHS1(A) given by Remark 4 agrees with
the canonical mixed complex structure of CHS1•(A) (see [TV4]).
Example 3 (The torus). The torus T is the product S1 ×S1. Thus, by Example 2, it
has a simplicial model given by (S1 ×S1)• the diagonal simplicial set associated to
the bisimplicial set S1
• ×S1
•, i.e. (S1 ×S1)k = S1
k ×S1
k = {0,...,k}2. We may write
(S1 ×S1)k = {(p,q)| p,q = 0,...,k} which we equipped with the lexicographical
ordering. The face maps di : (S1 ×S1)k →(S1 ×S1)k−1 and degeneracies si : (S1 ×
S1)k →(S1 ×S1)k+1, for i = 0,...,k, are given as the products of the differentials
and degeneracies of S1
•, i.e. di(p,q) = (di(p),di(q)) and si(p,q) = (si(p),si(q)).
We obtain CH(S1×S1)•(A,A) = L
k≥0 A ⊗A⊗(k2+2k). The face maps di can be
described more explicitly, when placing the tensor a(0,0) ⊗···⊗a(k,k) in a (k+1)×
(k+1) matrix. For i = 0,...,k−1, we obtain di(a(0,0) ⊗···⊗a(k,k)) by multiplying
the ith and (i + 1)th rows and the ith and (i + 1)th columns simultaneously, i.e.,
17the two-sided one, with values in the two A-modules A and M
18


## Page 19


di(a(0,0) ⊗···⊗a(k,k)) is equal to:
a(0,0)
...
(a(0,i)a(0,i+1))
...
a(0,k)
...
...
...
a(i−1,0)
...
(a(i−1,i)a(i−1,i+1))
...
⊗a(i−1,k)
(a(i,0)a(i+1,0))
...
(a(i,i)a(i,i+1)a(i+1,i)a(i+1,i+1))
...
(a(i,k)a(i+1,k))
a(i+2,0)
...
(a(i+2,i)a(i+2,i+1))
...
a(i+2,k)
...
...
...
a(k,0)
...
(a(k,i)a(k,i+1))
...
a(k,k)
The differential dk is obtained by multiplying the kth and 0th rows and the kth
and 0th columns simultaneously, i.e., dk(a(0,0) ⊗···⊗a(k,k)) equals
(a(0,0)a(0,k)a(k,0)a(k,k))
(a(0,1)a(k,1))
...
(a(0,k−1)a(k,k−1))
(a(1,0)a(1,k))
a(1,1)
...
a(1,k−1)
...
...
...
(a(k−1,0)a(k−1,k))
a(k−1,1)
...
a(k−1,k−1)
Example 4 (The Riemann sphere S2). The sphere S2 has a simplicial model S2
• =
I2
•/∂I2
• i.e. S2
n = {(0,0)}`{1···n}2. Thus CHS2•(A) = L
n≥0 A⊗A⊗n2.
Here the face and degeneracies maps are the diagonal ones as for (S1 × S1)•
in Example 3. In particular, the ith differential is also obtained from the previous
examples by setting dS2
•
i (p,q) = (0,0) in the case that di(p) = 0 or di(q) = 0 (where
di is the ith-face map of S1
•), or setting otherwise di(p,q) = (di(p),di(q)). For
i ≤n−1, we obtain di(a(0,0) ⊗···⊗a(k,k)) is equal to:
a(0,0)
(a(i−1,i)a(i−1,i+1))
...
a(i−1,n)
(a(i,i)a(i,i+1)a(i+1,i)a(i+1,i+1))
...
(a(i,n)a(i+1,n))
(a(i+2,i)a(i+2,i+1))
...
a(i+2,n)
...
...
(a(n,i)a(n,i+1))
...
a(n,n)
which is similar to the one of Example 3 without the “boldface” tensors.
Example 5 (higher spheres). Similarly to S2, we have the standard model Sd
• :=
(I•)d/∂(I•)d ∼= S1
•∧···∧S1
• (d-factors) for the sphere Sd. Hence Sd
n ∼= {0}`{1···n}d
and CHSd•(A) = L
n≥0 A ⊗A⊗nd. The face operators are similar to those of Ex-
ample 4 (except that, instead of a matrix, we have a dimension d-lattice) and
face maps are obtained by simultaneously multiplying each ith-hyperplane with
(i+1)th-hyperplane in each dimension. The last face dn is obtained by multiplying
all tensors of all nth-hyperplanes with a0.
We also have the small model Sd
sm• which is the simplicial set with exactly
two non-degenerate simplices, one in degree 0 and one in degree d. Then Sd
smn ∼=
19


## Page 20


{1,...,
 n
d

}. Using this model, it is straightforward to check the following compu-
tation of the ﬁrst homology groups of CHSd(A):
Hn(CHSd(A)) ∼= Hn(CHSdsm•(A)) =



= A
if n = 0
= 0
if 0 < n < d
= Ω1
A
if n = d
where Ω1
A is the A-module of K¨ahler differentials (see [L, W]).
Example 6 (Hochschild-Kostant-Rosenberg). Let A be a smooth commutative al-
gebra. The classical Hochschild-Kostant-Rosenberg Theorem states that its (stan-
dard) Hochschild homology is given by the algebra of K¨ahler forms ∧•
A(Ω1
A) ∼=
S•
A(Ω1
A[1]), where Ω1
A is the A-module of K¨ahler differentials; here a i-form is
viewed as having cohomological degree −i and S•
A is the free graded commuta-
tive algebra functor (in the category of graded A-modules). This theorem extends
to Hochschild homology over all spheres:
Theorem 3 (Generalized HKR). Let A be a smooth algebra and X be an afﬁne
smooth scheme or a smooth manifold. Let n ≥1 and Σg be a genus g surface.
1. (Pirashvili [P]) There is a quasi-isomorphism of CDGAs: CHSn(A) ∼= S•
A
 Ω1
A[n]

.
2. ([GTZ]) There is an equivalenceCHΣg(A) ∼= S•
A
 Ω1
A[2]⊕(Ω1
A[1])⊕2g
of CDGAs.
3. There are equivalences CHSn(OX) ∼= S•
OX
 Ω1
X[n]

and
CHΣg(OX) ∼= S•
OX
 Ω1
X[2]⊕(Ω1
X[1])⊕2g
of sheaves of CDGAs18.
The third assertion in Theorem 3 follows from 1 and 2 after sheaﬁfying in an
appropriate way the derived Hochschild chains.
2.4
Relationship with mapping spaces
We have seen the relationship between derived Hochschild chains and derived map-
ping spaces (Remark 5). It is also classical that the usual Hochschild homology of
de Rham forms of a simply connected manifold M is a model for the de Rham
forms on the free loop space LM := Map(S1,M) of M (see [Ch]). There is a gen-
eralization of this result for spaces where the forms are replaced by the singular
cochains with their E∞-algebra structure ([Jo]). These two results extend to de-
rived Hochschild chains in general to provide algebraic models of mapping spaces.
First, we sketch a generalization of Chen iterated integrals (studied in [GTZ]).
Let M be a compact, oriented manifold, denote by Ω•
dR(M) the differential graded
algebra of differential forms on M, and let Y• be a simplicial set with geometric
realization Y := |Y•|. Denote MY := Mapsm(Y,M) the space of continuous maps
18here the differentials on the right hand sides are zero; they are not the de Rham differential
20


## Page 21


from Y to M, which are smooth on the interior of each simplex in Y. Recall from
Chen [Ch, Deﬁnition 1.2.1], that a differentiable structure on MY is speciﬁed by the
set of plots φ : U →MY, where U ⊂Rn for some n, which are those maps whose
adjoint φ♯: U ×Y →M is continuous on U ×Y, and smooth on the restriction to
the interior of each simplex of Y, i.e. φ♯|U×(simplex of Y)◦is smooth. Following [Ch,
Deﬁnition 1.2.2], a p-form ω ∈Ωp
dR(MY) on MY is given by a p-form ωφ ∈Ωp
dR(U)
for each plot φ :U →MY, which is invariant with respect to smooth transformations
of the domain.
We now deﬁne the space of Chen (generalized) iterated integrals C hen(MY)
of the mapping space MY. Let η : Y• →∆•|Y•| be the canonical simplicial map
(induced by adjunction) which is given for i ∈Yk by maps η(i) : ∆k →Y in the
following way,
η(i)(t1 ≤··· ≤tk) := [(t1 ≤··· ≤tk)×{i}] ∈
a
∆• ×Y•/ ∼

= Y.
(8)
The map η allows to deﬁne, for any plot φ : U →MY, a map ρφ := ev◦(φ ×id),
ρφ : U ×∆k φ×id
−→MY ×∆k
ev
−→MYk,
(9)
where ev is deﬁned as the evaluation map,
ev(γ : Y →M,t)(i) = γ
 η(i)(t)

.
(10)
Now, if we are given a form N
y∈Yk
ay ∈
 ΩdR(M)
⊗Yk (with only ﬁnitely many ai ̸= 1),
the pullback (ρφ)∗  N
y∈Yk
ay

∈Ω•(U ×∆k), may be integrated along the ﬁber ∆k, and
is denoted by
 Z
C
O
y∈Yk
ay
!
φ
:=
Z
∆k(ρφ)∗ ⊗
y∈Yk
ay

∈Ω•
dR(U).
The resulting p = (∑i deg(ai)−k)-form
R
C

⊗
y∈Yk
ay

∈Ωp
dR(MY is called the (gen-
eralized) iterated integral of a0,...,ayk. The subspace of the space of De Rham
forms Ω•(MY) generated by all iterated integrals is denoted by C hen(MY). In
short, we may picture an iterated integral as the pullback composed with the inte-
gration along the ﬁber ∆k of a form in MYk,
MY
MY ×∆k
ev
/
R
∆k
o
MYk
Deﬁnition 5. We deﬁne I tY• : CHY•(Ω•
dR(M)) ∼= (Ω•
dR(M))⊗Y• →C hen(MY) by
I tY•
 
O
y∈Yk
ay
!
:=
Z
C

⊗
y∈Yk
ay

.
(11)
21


## Page 22


Interesting applications of iterated integrals to study gerbes and higher holon-
omy are given in [AbWa, TWZ].
Theorem 4 ([GTZ]). The iterated integral map I tY• :CHY•(Ω•
dR(M)) →Ω•
dR(MY)
is a (natural) map of CDGAs.
Further, assume that Y = |Y•| is n-dimensional, i.e. the highest degree of any
non-degenerate simplex is n, and assume that M is n-connected. Then, I tY• is a
quasi-isomorphism.
There is also a purely topological and characteristic free analogue of this result
using singular cochains instead of forms.
Theorem 5 ([F2, GTZ3]). Let X,Y be topological spaces. There is a natural map
of E∞-algebras
CHY(C∗(X)) −→C∗(Map(Y,X))
which is an equivalence when Y = |Y•| is n-dimensional and X is connected, nilpo-
tent with ﬁnite homotopy groups in degree less or equal to n (for instance when X
is n-connected).
Example 7. We compute the iterated integral map (11) in the case of S1
• (Example 2)
and T (Example 3). Since S1 is the interval I = [0,1] where the endpoints 0 and
1 are identiﬁed, the map η(i) : S1
k = {0,1...,k} →∆k(S1) = Map(∆k,S1) deﬁned
via (8) is given by η(i)(0 ≤t1 ≤··· ≤tk ≤1) = ti, where we have set t0 = 0. Thus,
the evaluation map (10) becomes
ev(γ : S1 →M,t1 ≤··· ≤tk) = (γ(0),γ(t1),...,γ(tk)) ∈Mk+1.
Furthermore, this recovers the classical Chen iterated integrals ItS1
• : CH•(A,A) →
Ω•(MS1) as follows. For a plot φ : U →MS1 we have,
ItS1
•(a0 ⊗···⊗ak)φ =
Z
C a0 ...ak

φ
=
Z
∆k(ρφ)∗(a0 ⊗···⊗ak)
= (π0)∗(a0)∧
Z
∆k(f
ρφ)∗(a1 ⊗···⊗ak) = (π0)∗(a0)∧
Z
a1 ...ak,
where f
ρφ :U ×∆k φ×id
−→MS1 ×∆k eev
→Mk is the classical Chen integral
R a1 ...ak from
[Ch] and π0 : MS1 →M is the evaluation at the base point π0 : γ 7→γ(0).
In the case of the torus T = S1×S1, the map η(p,q) : (S1×S1)k →Map(∆k,S1×
S1) is given by η(p,q)(0 ≤t1 ≤··· ≤tk ≤1) = (tp,tq) ∈S1 ×S1, for p,q = 0,...,k
and t0 = 0. Thus, the evaluation map (10) becomes
ev(γ : T →M,t1 ≤··· ≤tk) =




γ(0,0), γ(0,t1), ··· , γ(0,tk),
γ(t1,0),γ(t1,t1),··· ,γ(t1,tk),
...
γ(tk,0),γ(tk,t1),··· ,γ(tk,tk)



∈M(k+1)2
According to deﬁnition 5, the iterated integral ItS1×S1(a(0,0) ⊗···⊗a(k,k)) is given
by a pullback under the above map MS1×S1 ×∆k
ev
−→M(k+1)2, and integration along
the ﬁber ∆k.
22


## Page 23


2.5
The wedge product of higher Hochschild cohomology
Let A
f→B be a map of CDGAs. Note that it makes B into an A-algebra as well
as an A⊗A-algebra (since the multiplication A⊗A →A is an algebra morphism).
The excision axiom (Theorem 2) implies
Lemma 3. Let M be an A-module and X,Y be pointed topological spaces. There
is a natural equivalence
µ : HomA⊗A (CHX(A)⊗CHY(A),M)
≃
−→CHX∨Y(A,M)
We use Lemma 3 to obtain
Deﬁnition 6 ([Gi]). The wedge product of (derived) Hochschild cochains is the
linear map
µ∨: CHX(A,B)⊗CHY(A,B) −→HomA⊗A

CHX(A)⊗CHY(A),B⊗B

(mB)∗
−→HomA⊗A

CHX(A)⊗CHY(A),B

∼= CHX∨Y(A,B)
(12)
where the ﬁrst map is the obvious one: f ⊗g 7→
 x⊗y 7→f(x)⊗g(y)

.
Example 8. If X•,Y• are ﬁnite simplicial sets models of X,Y, the map µ∨can be
combinatorially described as the composition of the linear map ˜µ given, for any
f ∈CHXn(A,B) ∼= HomA(A⊗#Xn,B), g ∈CHXn(A,B) ∼= HomA(A⊗#Yn,B)) by
˜µ(f,g)(a0,a2,...a#Xn,b2,...,b#Yn) = a0.f(1,a2,...a#Xn).g(1,b2,...,b#Yn)
(where a0 corresponds to the element indexed by the base point of Xn ∨Yn) with the
Eilenberg-Zilber quasi-isomorphism from CHX•(A,B) ⊗CHY•(A,B) to the chain
complex associated to the diagonal cosimplicial space
 CHXn(A,B)⊗CHYn(A,B)

n∈N.
Proposition 6. The wedge product (of Deﬁnition 6) is associative19. In particular,
if there is a diagonal X
δ→X ∨X making X an E1-coalgebra (in (Top∗,∨)), then
(CHX(A,B),δ ∗◦µ∨) is an E1-algebra.
Example 9. A standard example of space with a diagonal is a sphere Sd. For d = 1,
we obtain a cup product on the usual Hochschild cochain complex which is (homo-
topy) equivalent to the standard cup-product for Hochschild cochains from [Ge].
The little d-dimensional little cubes operad Cubed acts continuously on Sd by
the pinching map
pinch : Cubed(r)×Sd −→
_
i=1...r
Sd.
(13)
19precisely, it means that µ∨makes X 7→CHX(A,B) into a lax monoidal functor ((Top∗)op,∨) →
(Chain(k),⊗)
23


## Page 24


given, for any c ∈Cubed(r), by the map pinchc : Sd →WSd collapsing the com-
plement of the interiors of the r rectangles to the base point. We thus get a map
˜
pinch : Cubed(r) −→MapCDGA(CHSd(A,B),CHWSd(A,B))
(14)
Applying the contravariance of Hochschild cochains and the wedge product
(Deﬁnition 6), we get, for all d ≥1, a morphism
pinch∗
Sd,r : C∗
 Cubed(r)

⊗

CHSd(A,B)
⊗r
(µ∨)(d−1)
−→
C∗
 Cubed(r)

⊗CH
Wr
i=1 Sd A,B

˜
pinch∗
−→CHSd(A,B).
(15)
The map (15) has a canonical extension to the case of E∞-algebras. We ﬁnd
Proposition 7 ([Gi, GTZ3]). Let A
f→B be a CDGA (or E∞-algebra) map. The
collection of maps (pinchSd,k)k≥1 makes CHSd(A,B) an Ed-algebra.
The algebra structure is natural with respect to CDGA maps, meaning that
given a commutative diagram
A
f
/ B
ϕ

A′
ψ
O
f ′
/ B′
, the canonical map h′ 7→ϕ ◦h′ ◦ψ is
an Ed-algebras morphism CHSd(A′,B′) →CHSd(A,B).
Remark 8. If f : A →B is a CDGA map, it is possible to describe this Ed-algebra
structure by giving an explicit action of the ﬁltration FdBE of the Barrat-Eccles
operad on CHSd
•(A,B) using the standard simplicial model of Sd (Example 5).
Example 10. If A = k, CHSn(k,B) ∼= B (viewed as En-algebras). If B = k, then the
En-algebra structure of CHSn(A,k) is the dual of the En-coalgebra structure given
by the n-times iterated Bar construction Bar(n)(A), see § 7.4.
3
Homology Theory for manifolds
3.1
Categories of structured manifolds and variations on En-algebras
In order to specify what is a homology theory for manifolds, we need to specify an
interesting category of manifolds.
Deﬁnition 7. Let Mﬂdn be the ∞-category associated20 to the topological category
with objects topological manifolds of dimension n and with morphism space
MapMﬂdn(M,N) := Emb(M,N)
the space of all embeddings of M into N (viewed as a subspace of the space
Map(M,N) of all continuous maps from M to N endowed with the compact-open
topology).
20by Example 58
24


## Page 25


In the above deﬁnition, the manifolds can be closed or open, but have no bound-
ary21.
Remark 9. It is important to consider embeddings instead of smooth maps. Indeed,
the category of all manifolds and all (smooth) maps is weakly homotopy equivalent
to Top so that, in that case, one would obtain a homology theory which extends to
spaces.
Remark 10 (smooth manifolds). One can also restrict to smooth manifolds in which
case it makes sense to equip Emb(M,N) with the weak Whitney C∞-topology;
this gives us the ∞-category Mﬂdun
n of smooth manifolds of dimension n. This
latter category embeds in Mﬂdn and this embedding is an equivalence onto the full
subcategory of Mﬂdn spanned by the smooth manifolds.
One can also consider categories of more structured manifolds, such as ori-
ented, spin or framed manifolds, as follows.
Let E →X be a topological n-
dimensional vector bundle, which is the same as a space X together with a (ho-
motopy class of) map e : X →BHomeo(Rn) from X to the classifying space of the
group of homeomorphisms of Rn. An (X,e)-structure on a manifold M ∈Mﬂdn
is a map f : M →X such that TM is the pullback f ∗(E) which is the same as a
factorization M
f→X
e→BHomeo(Rn) of the map M
eM
−→BHomeo(Rn) classifying
the tangent (micro-)bundle of M.
Deﬁnition 8. Let Mﬂd(X,e)
n
be the (homotopy) pullback (in ∞-Cat)
Mﬂd(X,e)
n
:= Mﬂdn ×h
Top/BHomeo(Rn) Top/X.
In other words Mﬂd(X,e)
n
is the ∞-category with objects n-dimensional topologi-
cal manifolds with an (X,e)-structure and with morphism the embeddings preserv-
ing the (X,e)-structure. The latter morphisms are made into a topological space by
identifying them with the homotopy pullback space
MapMﬂd(X,e)
n
(M,N) := Emb(X,e)(M,N)
∼= Emb(M,N)×h
Map/BHomeo(Rn)(M,N) Map/X(M,N).
Example 11. We list our main examples of study.
• Let X = pt, then E is trivial (here e is induced by the canonical base point of
BHomeo(Rn)) and an (X,e)-structure on M is a framing, that is, a trivializa-
tion of the tangent (micro-)bundle of M. In that case, we denote Mﬂdfr
n :=
Mﬂd(pt,e)
n
the ∞-category of framed manifolds. Note that this ∞-category is
equivalent to the one associated to the topological category with objects the
framed manifolds of dimension n and morphism spaces from M to N the
framed embeddings, that is the pairs (f,h) where f ∈Emb(M,N) and h is
an homotopy between the two trivialisation of TM induced by the framing
of M and the framing of N pulled-back along f.
21though homology theory for manifolds can be extended to stratiﬁed manifolds, see [AFT]
25


## Page 26


• Let X = BO(n) and BO(n)
e→BHomeo(Rn) be the canonical map. Then
Mﬂd(BO(n),e)
n
is (equivalent to) the ∞-category of smooth n-manifolds of Re-
mark 10. This essentially follows because the map O(n) →Diffeo(Rn) is a
deformation retract and the characterization of smooth manifolds in terms of
their micro-bundle structure [KiSi].
• Let X = BSO(n) and BSO(n) e→BHomeo(Rn) be the canonical map induced
by the inclusion of SO(n) ,→Homeo(Rn). Then a (BSO(n),e)-structure
on M is an orientation of M. We denote Mﬂdor
n := Mﬂd(BSO(n),e)
n
the ∞-
category of oriented smooth n-manifolds. Similarly to the framed case, it
has a straightforward description as the ∞-category associated a topological
category with morphisms the space of oriented embeddings.
• If X is a n-dimensional manifold, we can take eX : X →BHomeo(Rn) to be
the map corresponding to the tangent bundle TX →X of X. We simply de-
note Mﬂd(X,TX)
n
the associated ∞-category of manifolds. Every open subset
of X is canonically an object of Mﬂd(X,TX)
n
.
The (topological) coproduct M `N (that is disjoint union) of two (X,e)-manifolds
M,N has a canonical structure of (X,e)-manifold (given by M `N
f `g
→X where
M
f→X and N
g→X deﬁne the (X,e)-structures). Note that in general there are no
embeddings M `M →M so that the disjoint union of manifolds is not a coproduct
(in the sense of category theory) in Mﬂd(X,e)
n
. Nevertheless
Lemma 4. (Mﬂd(X,e)
n
,`) is a symmetric monoidal ∞-category.
There is a canonical choice of framing of Rn which induces a canonical (X,e)-
structure on Rn for any pointed space X. Unlike other manifolds, there are interest-
ing framed embeddings `Ri →Ri for any integer i. Indeed, in view of Example 11
and Deﬁnition 51, the space of embeddings Emb fr(`
{1,...,r} Rn,Rn) = Diskfr
n (r,1)
is homotopy equivalent to Cuben(r) the arity r space of the little cube operad and
thus is homotopy equivalent to the conﬁguration space of r unordered points in Rn.
This motivates the following (X,e)-structured version of En-algebras.
Deﬁnition 9. Let Disk(X,e)
n
be the full subcategory of Mﬂd(X,e)
n
spanned by disjoints
union of standard euclidean disks Rn. The ∞-category of Disk(X,e)
n
-algebras22 is the
category
Fun⊗(Disk(X,e)
n
,Chain(k))
of symmetric monoidal (∞-)functors from (Disk(X,e)
n
,`) to (Chain(k),⊗).
The underlying object of a Disk(X,e)
n
-algebra A is its value A(Rn) on a single
disk Rn. We will often abusively denote in the same way the Disk(X,e)
n
-algebra and
its underlying object.
22which we also referred to as the category of (X,e)-structured En-algebras
26


## Page 27


We denote Disk(X,e)-Alg the ∞-category of Disk(X,e)
n
-algebras and Disk(X,e)-Alg(C )
the one of Disk(X,e)
n
-algebras with values in a symmetric monoidal category C
(whose deﬁnition are the same as Deﬁnition 9 with (Chain(k),⊗) replaced by
(C ,⊗)). The underlying object induces a functor
Disk(X,e)-Alg(C ) −→C
(16)
Example 12.
• For X = pt, the category of Disk(X,e)
n
-algebras will be denoted
Diskfr
n -Alg. It is equivalent to the usual category of En-algebras and corre-
sponds to the case of framed manifolds.
• The category of Disk(BSO(n),e)
n
-algebras is equivalent to the category of alge-
bras over the operad
 Cuben(r)⋉SO(n)r
r≥1 introduced in [SW] (and called
the framed little disk operad). Since these algebras corresponds to the case of
oriented manifolds, we call them oriented En-algebras and we simply write
Diskor
n for Disk(BSO(n),e)
n
. It can be shown that Diskor
n -algebras are homotopy
ﬁxed points of the En-algebras with respect to the action of SO(n) on the
operad Diskfr
n .
• Similarly, the category of Disk(BO(n),e)
n
-algebras is equivalent to the category
of algebras over the operad
 Cuben(r) ⋉O(n)r
r≥1. We also call them un-
oriented En-algebras and simply write Diskun
n for Disk(BO(n),e)
n
.
• Let U ∼= Rn be a disk in X. By restriction to sub-disks of U, we have a
canonical functor Disk(X,TX)
n
-Alg →Disk(Rn,TRn)
n
-Alg ∼= En-Alg (see Theo-
rem 9 below). It follows that a Disk(X,TX)
n
-algebra is simply a family of
En-algebras over X.
Example 13 (Commutative algebras as Disk(X,e)
n
-algebras). The canonical func-
tor Disk(X,e)
n
→Fin (where Fin is the ∞-category associated to the category of
ﬁnite sets) shows that any E∞-algebra (Deﬁnition 34) has a canonical structure of
Disk(X,e)
n
-algebras. Thus we have canonical functors
CDGA −→E∞-Alg −→Disk(X,e)
n
-Alg.
For A a differential graded commutative algebra, this structure is the symmet-
ric monoidal functor deﬁned by A(`
i∈I Rn) := A⊗I and, for an (X,e)-preserving
embedding `
I Rn ,→Rn, by the (iterated) multiplication A⊗I →A.
Example 14 (Opposite of an En-algebra). There is a canonical Z/2Z-action on
En-Alg induced by the antipodal map τ : Rn →Rn, x 7→−x acting on the source
of Fun⊗(Disk fr
n , Chain(k)). If A is an En-algebra, then the result of this action
Aop := τ∗(A) is its opposite algebra. If n = ∞, the antipodal map is homotopical to
the identity so that Aop is equivalent to A as an E∞-algebra.
27


## Page 28


3.2
Factorization homology of manifolds
We now explain what is a Homology Theory for Manifolds (Deﬁnition 10) in a
way parallel to the presentation of the Eilenberg-Steenrod axioms. We ﬁrst need
an analogue of Lemma 1 for monoidal functors out of manifolds (instead of spaces)
in order to formulate the correct excision axiom.
Observe that Rn is canonically an En-algebra object in Mﬂdn. Let N be an (n−
s)-dimensional manifold such that N ×Rs has an (X,e)-structure. Then, similarly,
N ×Rs is also an Es-algebra object in Mﬂd(X,e)
n
. Let us describe more precisily this
structure: for ﬁnite sets I,J, we have continuous maps
γN
I,J : Emb fra
I
Rs,
a
J
Rs
→Emb(X,e)a
I
(N ×Rs),
a
J
(N ×Rs)

induced by the composition
a
I
(N ×Rs) ∼= N ×
a
I
Rs idN×f
→N ×
a
J
Rs
∼=
a
J
(N ×Rs)
for any f ∈Emb fr `
I Rs,`
J Rs
. In particular, taking s = n, N = pt, the above
maps induce a canonical map of operads
γ : Disk fr
n →Disk(X,e)
n
and thus we have an underlying functor γ∗: Disk(X,e)
n
-Alg −→En-Alg. And more
generally we obtain functors: (γN)∗: Disk(N×Rs,T(N×Rs))
n
-Alg −→Es-Alg.
The main consequence is that any symmetric monoidal functor (from Mﬂd(X,e)
n
)
maps N ×Rs to an Es-algebra object of the target category. More precisely:
Lemma 5. Let
 Mﬂd(X,e)
n
,`
F
−→(Chain(k),⊗) be a symmetric monoidal func-
tor.
1. For any manifold N ×Rs with an (X,e)-structure, F(N ×Rs) has a canoni-
cal Es-algebra structure.
2. Let M be an (X,e)-structured manifold with an end23 trivialized as N × R
(where N is of codimension 1 and the open part of M lies in the neighborhood
of N × {−∞}, see Figure 1). Then F(M) has a canonical left24 module
structure over the E1-algebra F(N ×R).
3. F(Rn) has a natural structure of Disk(X,e)
n
-algebra.
23i.e. open boundary component
24If N × R is trivialized so that the open part of M is in the neighborhood of N × {+∞}, then
F(M) has a canonical right module structure.
28


## Page 29


Proof. Endow Rn with its canonical framing. It automatically inherits an (X,e)-
structure for every connected component25 of X (since every vector bundle is lo-
cally trivial). Now, since F is symmetric monoidal, then F(Rn) also has an in-
duced structure of Disk(X,e)
n
-algebra. Let us describe the structure mentioned in 1.
and 2.
1. For any manifold N × Rs with an (X,e)-structure, the Es-algebra structure
on F(N ×Ri) is given by the structure maps
Embfra
I
Rs,Rs
×
 F(N ×Rs)
I
γN
I,pt
−→Emb(X,e)a
I
(N ×Ri),N ×Rs
×
 F(N ×Rs)
I
−→Emb(X,e)a
I
(N×Rs),N×Rs
×F
a
I
(N×Rs)
 F(Emb(X,e)(−,−))
−→
F(N×Rs).
The fact that F is monoidal ensures it deﬁnes an Es-algebra structure.
From the deﬁnition, it is clear that γ∗(F(Rn)) ∼= F(Rn) as an En-algebra
(where the two structures are given by 1. and 3.).
2. Now, let M be an (X,e)-structured manifold with an end trivialized as N ×R;
F(N ×R) is an E1-algebra by 1. The left module structure of F(M) is given
by the maps
Embfr
(
a
I
R)
a
(0,1],(0,1]

×

F(N ×R)
I
×F(M)
γN
I `{∗},pt
−→Emb(X,e) a
I
N ×R
a
M,M

×
 F(N ×Ri)
I ×F(M)
−→Emb(X,e)a
I
(N ×R)
a
M,M

×F
 a
I
(N ×R)
a
M

F(Emb(X,e)(−,−))
−→
F(N ×Ri).
N × R
M
−∞
Figure 1: A manifold M with a trivialization N ×R of its open boundary.
25In practice, X will almost always be connex so that the structure will be canonical
29


## Page 30


The above lemma is crucial in order to formulate the excision property.
Deﬁnition 10. An homology theory for (X,e)-manifolds (with values in the sym-
metric monoidal ∞-category (Chain(k),⊗)) is a functor
F : Mﬂd(X,e)
n
×Disk(X,e)
n
-Alg →Chain(k)
(denoted (M,A) 7→FM(A)) satisfying the following axioms:
i) (dimension) there is a natural equivalence FRn(A) ∼= A in Chain(k);
ii) (monoidal) the functor M 7→FM(A) is symmetric lax-monoidal and, for any
set I, the following induced maps are equivalences (naturally in A)
O
i∈I
FMi(A)
≃
−→F`
i∈I Mi(A).
(17)
iii) (excision) Let M be an (X,e)-manifold. Assume there is a codimension 1
submanifold N of M with a trivialization N × R of its neighborhood such
that M is decomposable as M = R∪N×R L where R,L are submanifolds of M
glued along N × R. By Lemma 5, FN×R(A) is an E1-algebra and FR(A),
FL(A) are respectively right and left modules. The excision axiom26 is that
the canonical map
FL(A)
L⊗
FN×R(A)FR(A)
≃
−→FM(A)
(induced by the universal property of the right hand side) is an equivalence.
Remark 11. The symmetric lax-monoidal condition in axiom ii) means that there
are natural (in A, M) transformations like (17) compatible with composition for any
ﬁnite I and invariant under the action of permutations. The axiom ii) thus implies
that M 7→FM(A) is symmetric monoidal. When I is not ﬁnite, the right hand side
in (17) is the colimit lim
−→
F→I
N
j∈F FMj(A) over all ﬁnite sets F and the map is induced
by the universal property of the colimit and the lax monoidal property.
Theorem 6 (Francis [F2]). There is an unique27 homology theory for (X,e)-manifolds
(in the sense of Deﬁnition 10), which is called factorization homology28.
Factorization homology is deﬁned in [L3] and its value on a (X,e)-manifold M
and Disk(X,e)
n
-algebra A is denoted
R
M A.
26or Mayer-Vietoris principle
27up to contractible choices
28the name comes from the fact that it satisﬁes the factorization property (Remark 20). Another
name is topological chiral homology.
30


## Page 31


Remark 12 (other coefﬁcients). In Deﬁnition 10 and Theorem 6, one can replace
the symmetric monoidal category (Chain(k),⊗) by any symmetric monoidal ∞-
category (C ,⊗) which has all colimits and whose monoidal structure commutes
with geometric realization and ﬁltered colimits, see [F1, F2, AFT].
Remark 13 (ﬁnite variant). If one restricts to the full subcategory of Mﬂd(X,e)
n
spanned by the manifolds which have ﬁnitely many connected components which
are the interior of closed manifolds, then axiom ii) becomes equivalent to asking
F to be naturally symmetric monoidal and Theorem 6 stills holds in this context.
Note that factorization homology depends on the (X,e)-structure not the un-
derlying topological manifold structure of M in general. For instance, if M = R is
equipped with its standard framing and A is an associative algebra (hence E1), then
R
R A ∼= A as an E1-algebra. However, if N = R is equipped with the opposite fram-
ing (pointing toward −∞), then
R
N A ∼= Aop (where Aop is the algebra with opposite
multiplication) as an E1-algebra (see [F1, L3] for more general statements).
Remark 14. In particular, Theorem 6 implies that the functor F 7→FRn from,
the category of symmetric monoidal functors Mﬂd(X,e)
n
→Chain(k) satisfying ex-
cision29, to the category of Disk(X,e)
n
-algebras (which is a well deﬁned functor by
Lemma 5) is a natural equivalence.
Deﬁnition 11. Let A ∈Disk(X,e)
n
-Alg. The homology theory for (X,e)-manifolds
deﬁned30 by A will be called factorization homology (or homology theory) with
coefﬁcient in A.
Example 15 (Hochschild homology). Let A be a differential graded associative
algebra (or even an A∞-algebra) and choose a framing of S1 = SO(2) induced by
its Lie group structure. We can use excision to evaluate the factorization homology
with value in A on the framed manifold S1. Here, we see the circle as being obtained
by gluing two intervals: S1 = R∪{1,−1}×R R, see Figure 2 .
Note that the induced framing on {1,−1}×R correspond to the standard fram-
ing of R on the component {1} × R and the opposite framing on the component
R
L
1
−1
Figure 2: The decomposition of the cir-
cle S1 into 2 intervals (pictured in blue
just across the circle) L ∼= R and R ∼= R
along a trivialization {1,−1} × R (pic-
tured in red). The arrows are indicat-
ing the orientations/framing of the cir-
cle and other various pieces of the de-
composition.
29i.e. axiom iii) in Deﬁnition 10
30in the sense of Remark 14
31


## Page 32


{−1} × R so that
R
{−1}×R A = Aop (see Example 27). Thus, by excision we ﬁnd
that
Z
S1 A ∼=
Z
R A
L⊗
R
{1,−1}×R A
Z
R A ∼= A
L⊗
A⊗Aop A ∼= HH(A)
(18)
where HH(A) is the usual Hochschild homology31 of A with value in itself.
Example 16. Let Freen be the free En-algebra on k, which is naturally a Diskun
n -
algebra (Example 12). It can thus be evaluated on any manifold.
Proposition 8 ([AFT]). Let M be a manifold. Then
R
M Freen ∼= C∗
 `
n∈N Confn(M)

where Confn(M) is the space of conﬁgurations of n -unordered points in M.
In particular, factorization homology is not an homotopy invariant of manifolds
(since conﬁgurations spaces of unordered points are not, see [LS]). By considering
conﬁguration spaces of points with labels, one has a similar result for the free En-
algebra Freen(V) associated to V ∈Chain(k), see [AFT].
Example 17 (Non-abelian Poincar´e duality). Let us now mention another impor-
tant example of computation of factorization homology. Let (Y,y0) be a pointed
space and Ωn(Y) := { f : [0,1]n →Y, f(∂[0,1]n) = y0} be its n-fold based loop
space. Then the singular chains C∗(Ωn(Y)) has a natural structure of unoriented
En-algebra.
Theorem 7 (non-abelian Poincar´e duality, Lurie [L3]). If M is a manifold of dimen-
sion n and Y an n−1-connective pointed space, then
Z
MC∗(Ωn(Y)) ∼= C∗(Mapc(M,Y))
where Mapc(M,Y) is the space of compactly supported maps from M to Y.
If n = 1 andY is connected, Theorem 7 reduces to Goodwillie’s quasi-isomorphism [G]
HH(C∗(Ω(Y))) ∼= C∗(LY) where LY = Map(S1,Y) is the free loop space of Y.
Remark 15 (Derived functor deﬁnition). One possible way for deﬁning factor-
ization homology is similar to the one of § 2.1.2. Indeed, let A be a Disk(X,e)
n
-
algebra. Then A deﬁnes a covariant functor Disk(X,e)
n
→Chain(k). Similarly, if M
is in Mﬂd(X,e)
n
, then it deﬁnes a contravariant functor E(X,e)
M
:
 Disk(X,e)
n
op →Top,
given by the formula
E(X,e)
M
a
i∈I
Rn
:= Emb(X,e)a
i∈I
Rn,M

.
The data of A and M thus gave a functor
E(X,e)
M
⊗A :
 Disk(X,e)
n
op ×Disk(X,e)
n
E(X,e)
M
×A
−→Top×Chain(k)
⊗
−→Chain(k).
31at least if A is projective over k; if A is not projective over k, there are several variants of
Hochschild homology, the one we are considering is the derived version and correspond to what is
sometimes called shukla homology [Sh, Q]
32


## Page 33


Here Top×Chain(k) ⊗→Chain(k) means the tensor of a space with a chain complex
which is equivalent to (X,D∗) 7→C∗(X) ⊗D∗where C∗(X) is the singular chain
functor of X (with value in k).
Proposition 9 ([F2]). The factorization homology
R
M A is the (homotopy) coend of
E(X,e)
M
⊗A. In other words:
Z
M A ∼= E(X,e)
M
L⊗
Disk(X,e)
n
A
∼= hocolim


a
f:{1,...,q}→{1,...,p}
C∗
 E(X,e)
M
(Rn)
⊗p ⊗Disk(X,e)
n
(q, p)⊗A⊗q
⇒
a
m
C∗
 E(X,e)
M
(Rn)
⊗m ⊗A⊗m
!
The Proposition remains true with (Chain(k),⊗) replaced by any symmetric
monoidal ∞-category satisfying the assumptions of Remark 12.
4
Factorizations algebras
In this section we will give a ˇCech type construction of Factorization homology
which plays for Factorization homology the same role as sheaf cohomology plays
for singular cohomology32. This analogue of cosheaf theory is given by factoriza-
tion algebras which we describe in length here.
4.1
The category of factorization algebras
We start by describing various categories of (pre)factorization algebras (including
the locally constant ones).
Following Costello Gwilliam [CG], given a topological space X, a prefactor-
ization algebra over X is an algebra over the colored operad whose objects are
open subsets of X and whose morphisms from {U1,··· ,Un} to V are empty unless
when Ui’s are mutually disjoint subsets of U, in which case they are singletons.
Unfolding the deﬁnition, we ﬁnd
Deﬁnition 12. A prefactorization algebra on X (with value in chain complexes)
is a rule that assigns to any open set U a chain complex F(U) and, to any ﬁnite
family of pairwise disjoint open sets U1,...,Un ⊂V included in an open V, a chain
map
ρU1,...,Un,V : F(U1)⊗···⊗F(Un) −→F(V).
32singular cohomology of a paracompact space X can be computed as the cohomology of the
constant sheaf ZX on X while singular cohomology with twisted coefﬁcient is computed by sheaf
cohomology with value in a locally constant sheaf
33


## Page 34


These structure maps are required to satisfy obvious associativity and symmetry
conditions (see [CG]): the map ρU1,...,Un,V is invariant with respect to the action
of the symmetric group Sn by permutations of the factors on its domain (in other
words, the map ρU1,...,Un,V depends only of the collection U1,...,Un,V not on the
particular choice of ordering of the open sets) and ρU,U is the identity33 of F(U).
Further, the associativity condition is that: for any ﬁnite collection of pairwise
disjoint open subsets (Vj)j∈J lying in an open subsetW together with, for all j ∈J, a
ﬁnite collections (Ui,j)i∈Ij of pairwise disjoint open subset lying inVj, the following
diagram
N
(i,j)∈`
r Ir
F (Ui j)
N
j
ρ(Uij)i∈Ij ,Vj
&
ρ(Uij),W
/ F (W)
N
j∈J
F (Vj)
ρ(Vj)j∈J,W
;
(19)
is commutative.
If U is an open cover of X, we deﬁne a prefactorization algebra on U , also
denoted a U -prefactorization algebra, to be the same thing as a prefactorization
algebra except that F(U) is deﬁned only for U ∈U .
Remark 16. One can deﬁne a prefactorization algebra with value in any symmetric
monoidal category (C ,⊗) by replacing chain complexes by objects of C .
Remark 17. Prefactorization algebras are pointed since the inclusion /0 ,→U of
the empty set in any open induces a canonical map F(/0) →F(U). Further, the
structure maps of a prefactorization algebra exhibit F(/0) as a commutative algebra
in (C ,⊗) (non necessarily unital) and F(U) as a F(/0)-module.
There is a ˇCech-complex associated to a cover U of an open set U. Denoting
PU the set of ﬁnite pairwise disjoint open subsets {U1,...,Un |Ui ∈U } (n is not
ﬁxed), it is, by deﬁnition the realization of the simplicial chain complex
ˇC•(U ,F) =
M
α∈PU
 
O
U∈α
F(U)
!
⇔
M
(α,β)∈PU ×PU


O
(U,V)∈α×β
F(U ∩V)

←
←
←···
where the horizontal arrows are induced by the natural inclusions as for the usual
ˇCech complex of a cosheaf (see [CG]).
Let us describe the simplicial structure more precisely. In simplicial degree i,
we get the chain complex ˇCi(U ,F) :=
L
α∈PU i+1 F(α) where, for α = (α0,...,αi) ∈
33we could weaken this condition to be only a weak-equivalence or actually just a chain map.
In the latter case, we will obtain a (homotopy) strictly weaker notion of prefactorization algebras;
however, this will not change the notion of factorization algebras since the condition of being a fac-
torization algebra (Deﬁnition 13) will imply that ρU,U is an equivalence as U is always a factorizing
cover of itself; since it is idempotent by associativity, we will get that it is homotopy equivalent to
the identity
34


## Page 35


PU i,we denote F(α) the tensor product of chain complexes (with its natural dif-
ferential) :
F(α) =
O
Uj∈αj
F

i\
j=0
Uj

.
We write din : L
α∈PU i+1 F(α) →L
α∈PU i+1 F(α) the induced differential. The
face maps ∂s :
L
α∈PU n+1 F(α) −→
L
β∈PU n F(β) (s = 0...n) are the direct sum of
maps bρs
α : F(α) →F(bαs) where bαs = (α0,...,αs−1,αs+1,...,αn) is obtained by
discarding the sth-collection of opens in PU n+1. Precisely bρs
α is the tensor product
O
Uj∈α j
F
 n\
j=0
Uj

−→
O
Uk ∈αk,
k ̸= s
F

n\
k = 0
k ̸= s
Uk

of the structure maps associated to the inclusion of opens
T
j=0...n
Uj into T
j̸=s
Uj. The
degeneracies are similarly given by operations (α0,...,αn) 7→(α0,...,αj,αj,...,αn)
doubling a set α j.
The simplicial chain-complex ˇC•(U ,F) can be made into a chain complex
(which is the total complex of a bicomplex):
ˇC(U ,F) =
M
α∈PU
F(α) ←
M
β∈PU ×PU
F(β)[1] ←···
where the horizontal arrows are induced by the alternating sum of the faces ∂j in the
standard way. In other words, ˇC(U ,F) = L
i≥0

L
α∈PU i+1 F(α)[i]

with differential
the sum of F(α)[i]
(−1)idin
−→F(α)[i] and
n
∑
j=0
(−1)j∂j :
M
α∈PU n+1
F(α)[n] →
M
β∈PU n
F(β)[n−1].
Remark 18. If a cover U is stable under ﬁnite intersections, we only need F to be
a prefactorization algebra on U , to deﬁne the ˇCech-complex ˇC(U ,F).
If U is a cover of an open set U, then the structure maps of F yield canonical
maps F(α) →F(U) which commute with the simplicial maps. Thus, we get a
natural map of simplicial chain complexes
  ˇCi(U ,F) →F(U)

i≥0 to the constant
simplicial chain complex
 F(U)

i≥0. Passing to geometric realization, we obtain
a canonical chain complex homomorphism:
ˇC(U ,F) −→F(U).
(20)
Remark 19 ( ˇCech complexes in (C ,⊗)). If (C ,⊗) is a symmetric monoidal cat-
egory with coproducts, we deﬁne the ˇCech complex of a prefactorization algebra
35


## Page 36


with values in C in the same way, replacing the direct sum by the coproduct in
order to get a simplicial object ˇC•(U ,F) in C . If further, C has a geometric
realization, then we obtain the ˇCech complex ˇC(U ,F) ∈C exactly as for chain
complexes above and the canonical map (20) is also well deﬁned.
Deﬁnition 13. An open cover of U is factorizing if, for all ﬁnite collections
x1,...,xn of distinct points in U, there are pairwise disjoint open subsets U1,...,Uk
in U such that {x1,...,xn} ⊂Sk
i=1Ui.
A prefactorization algebra F on X is said to be a homotopy34 factorization
algebra if, for all open subsets U ∈Op(X) and for every factorizing cover U of
U, the canonical map ˇC(U ,F) →F(U) is a quasi-isomorphism (see [C2, CG]).
Note that we do not consider the lax version of homotopy factorization algebra
deﬁned in [CG].
Remark 20 (Factorization property). If F is a factorization algebra andU1,...,Ui
are disjoint open subsets of X, the factorization condition implies that the structure
map
F(U1)⊗···⊗F(Ui) −→F(U1 ∪···∪Ui)
(21)
is a quasi-isomorphism. In particular, this implies that our deﬁnition of factoriza-
tion algebra agrees with the one of [CG].
Another consequence is that F(/0) ∼= k (or, more generally, is the unit of the
symmetric monoidal category C if F has values in C ).
The fact that the map (21) is an equivalence is called the factorization property
in the terminology of Beilinson-Drinfeld [BD], in the sense that the value of F on
disjoint opens factors through its value on each connected component.
Example 18 (the trivial factorization algebra). The trivial prefactorization algebra
k is the constant prefactorization algebra given by the rule U 7→k(U) := k, with
structure maps given by multiplication. It is a (homotopy) factorization algebra. It
is in particular locally constant over any stratiﬁed space X (Deﬁnitions 14 and 21).
One deﬁnes similarly the trivial factorization algebra over X with values in a
symmetric monoidal ∞-category (C ,⊗) by the rule U 7→1C where 1C is the unit
of the monoidal structure.
Remark 21 (genuine factorization algebras). The notion of homotopy (or derived)
factorization algebra in Deﬁnition 13 is a homotopy version of a more naive, un-
derived, version of factorization algebra. This version is a prefactorization algebra
such that the following sequence
 M
α∈PU 2
F(α)
 ∂0⇒
∂1
 M
β∈PU
F(β)

→F(U)
is (right) exact for any factorizing cover U ofU. In other words we ask for a similar
condition as in Deﬁnition 13 but with the truncated ˇCech complex. We refer to
34we can also say derived factorization algebra. Unless otherwise speciﬁed, the word factoriza-
tion algebra will always mean a homotopy factorization algebra in these notes
36


## Page 37


prefactorization algebras satisfying this condition as genuine factorization algebras
(they are also called strict in [CG]). Note that a genuine factorization algebra is not
a (homotopy) factorization algebra in general. Homotopy factorization algebras are
to genuine factorization algebras what homotopy cosheaves are to cosheaves; that
is they are obtained by replacing the naive version by an acyclic resolution.
When X is a manifold we have the notion of locally constant factorization
algebra which roughly means that the structure maps do not depend on the size of
the open subsets but only their relative shapes:
Deﬁnition 14. Let X be a topological manifold of dimension n. We say that an
open subset U of X is a disk if U is homeomorphic to a standard euclidean disk Rn.
A (pre-)factorization algebra over X is locally constant if for any inclusion of open
disks U ,→V in X, the structure map F(U) →F(V) is a quasi-isomorphism.
Let us mention that a locally constant prefactorization algebra is automatically
a (homotopy) factorization algebra, see Remark 24.
Deﬁnition 15. A morphism F →G of (pre)factorization algebras over X is the
data of chain complexes morphisms φU : F(U) →G (U) for every open set U ⊂X
which commute with the structures maps; that is the following diagram
F(U1)⊗···⊗F(Ui)
⊗φj(Uj)

ρU1,...,Ui,V
/ F(V)
φV

G (U1)⊗···⊗G (Ui)
ρU1,...,Ui,V
/ G (V)
is commutative for any pairwise disjoint ﬁnite family U1,...,Ui of open subsets
of an open set V. Morphisms of (pre)factorization algebras are naturally enriched
over topological space. Indeed, we have mapping spaces Map(F,G ) deﬁned as
the geometric realization of the simplicial set
n 7→Map(F,G )n := {prefactorization algebras morphisms from F to C∗(∆n)⊗G }
where C∗(∆n)⊗G is the prefactorization algebra whose value on an open set U is
C∗(∆n)⊗G (U). We obtain in this way ∞-categories of (pre)factorization algebras
(as in § 10.1, Example 58).
The ∞-category of prefactorization algebras over X is denoted PFacX and sim-
ilarly we write FacX for the ∞-categories of factorization algebras over X and Faclc
X
for the locally constant ones (which is a full subcategory). Also if (C ,⊗) is a sym-
metric monoidal (∞-)category (with coproducts and geometric realization), we will
denote FacX(C ), Faclc
X (C ) the ∞-categories of factorization algebras in C .
Note that the embedding FacX →PFacX is a fully faithful embedding.
The underlying tensor product35 of chain complexes induces a tensor product
of factorization algebras which is computed pointwise: for F,G ∈PFacX and an
35recall our convention that if k is not a ﬁeld, the tensor product really means derived tensor
product
37


## Page 38


open set U, we have
 F ⊗G

(U) := F(U)⊗G (U)
(22)
and the structure maps are just the tensor product of the structure maps. If (C ,⊗) is
symmetric monoidal, the same construction yields a monoidal structure on PFacX(C ).
Its unit is the trivial factorization algebra with values in C (Example 18).
Proposition 10 (Costello-Gwilliam [CG]). The (∞-)categories PFacX(C ), FacX(C ),
Faclc
X (C )36 are symmetric monoidal with tensor product given by (22).
Remark 22 (Restrictions). If Y ⊂X is an open subspace, then we have natural
restriction functors PFacX(C ) →PFacY(C ), FacX(C ) →FacY(C ). When X is a
manifold, the same holds for locally constant factorization algebras.
Deﬁnition 16. If U is an open subset of X and A ∈PFac(X), we write A|U ∈
PFacU for the restriction of A to U and similarly for (possibly locally constant)
factorization algebras.
A homeomorphism f : X
≃→Y induces isomorphisms PFacX ∼= PFacY and
FacX ∼= FacY (or Faclc
X ∼= Faclc
Y when X is a manifold) realized by the functor
f∗see § 5.1.
4.2
Factorization homology and locally constant factorization alge-
bras
We now explain the relationship between the ˇCech complex of a factorization al-
gebras and factorization homology. We ﬁrst start to express Disk(X,TX)
n
-algebras in
terms of factorization algebras. For simplicity, we assume in § 4.2 that manifolds
are smooth. For topological manifolds one obtains the same result as below by re-
placing geodesic convex neighborhoods by families of embeddings Rn →M wich
preserves the (M,TM)-structure and whose images form a basis of open of M.
Let M be a manifold with an (X,e)-structure. Every open subset U of M
inherits a canonical (X,e)-structure given by the factorization U ,→M
f→X
e→
BHomeo(Rn) of the map eU : U →BHomeo(Rn) classifying the tangent bundle of
U. This construction extends canonically into a functor
f∗: Disk(M,TM)
n
−→Disk(X,e)
n
and (by Deﬁnition 9) we have
Lemma 6. An (X,e)-structure M
f→X
e→BHomeo(Rn) on a manifold M induces
a functor f ∗: Disk(X,e)
n
-Alg →Disk(M,TM)
n
-Alg.
36the latter is deﬁned when X is a manifold
38


## Page 39


Now let A be a Disk(X,e)
n
-algebra and choose a metric on M. A family of pair-
wise disjoint open convex geodesic neighborhoods U1,...,Ui which lies in a con-
vex geodesic neighborhood37 V, deﬁnes an (X,e)-structure preserving embedding
iU1,...,Ui,V ∈Emb(X,e) `
{1,...,i} Rn,Rn
so that the Disk(X,e)
n
-algebra structure of A
yields a structure map
µU1,...,Ui,V : A⊗i iU1,...,Ui,V
−→Emb(X,e) a
{1,...,i}
Rn,Rn
⊗A⊗i →A.
This allows us to deﬁne a prefactorization algebra FA on open convex geodesic
subsets by the formula FA(V) := A. Since, the convex geodesic neighborhoods
form a basis of open which is stable by intersection, for any open set U ⊂M, we
have the ˇCech complex38
ˇC(C V (U),FA)
where C V (U) is the factorizing cover of U given by the geodesic convex open
subsets of U. The following result shows that FA is actually (the restriction of) a
factorization algebra and computes factorization homology.
Theorem 8 ([GTZ2]). Let A be a Disk(X,e)
n
-algebra.
• The rule M 7→ˇC(C V (M),FA) is a homology theory for (X,e)-manifolds. In
particular the ˇCech complex is independent of the choice of the metric and
computes factorization homology of M:
ˇC(C V (M),FA) ≃
Z
M A.
• The functor (U,A) 7→ˇC(C V (U),FA) induces an equivalence of ∞-categories
Disk(M,TM)
n
-Alg
≃
−→Faclc
M.
Since we have a preferred choice of framing for Rn, the projection map Rn →
pt induces an equivalence of ∞-categories Disk(Rn,TRn)
n
≃→Disk(pt,e)
n
and thus equiv-
alences Disk(X,TX)
n
-Alg ∼= Disk fr
n -Alg ∼= En-Alg (see Example 12). Hence Theo-
rem 8 is a slight generalization of the following beautiful result.
Theorem 9 (Lurie [L3]). There is a natural equivalence of ∞-categories
En-Alg ∼= Faclc
Rn.
The functor Faclc
Rn →En-Alg is given by the global section (i.e. the pushforward
p∗where p : Rn →pt, see § 5.1) and the inverse functor is precisely given by
factorization homology.
37which is thus canonically homeomorphic to an euclidean disk
38the construction is actually the extension of a factorization algebra on C V (U) as in Section 5
39


## Page 40


Locally constant factorization algebras on Rn are thus a model for En-algebras.
More generally, locally constant factorization algebras are a model for Disk(X,TX)
n
-
algebras in which the cosheaf property replaces39 some of the higher homotopy
machinery needed for studying these algebras (at the price of working with “lax”
algebras).
Remark 23. Theorem 9 is the key example of the relationship between factor-
ization algebras and factorization homology so we now explain the equivalence
in more depth. Recall that En-Alg is the ∞-category of algebras over the operad
Cuben of little cubes. It is equivalent to the ∞-category Disk fr
n -Alg since we have
an equivalence of operads Cuben
≃
−→Diskfr
n induced by a choice of diffeomor-
phism θ : (0,1)n ∼= Rn. Consider the open cover D of Rn consisting of all open
disks and denote PFaclc
D
40 the category of D-prefactorization algebras which sat-
isfy the locally constant condition (Deﬁnition 14 and Deﬁnition 12). Evaluation of
a Diskfr
n -algebra on an open disk yields a functor Disk fr
n -Alg →PFaclc
D which is
an equivalence by [L3, §5.2.4].
Similarly, let R be the cover of (0,1)n by open rectangles and PFaclc
R be the
category of locally constant R-prefactorization algebras. Evaluation of a Cuben-
algebra on rectangles yields a functor En-Alg = Cuben-Alg →PFaclc
R. Denote
Faclc
D, Faclc
R the category of locally constant factorization algebras over the covers
D, R respectively (see § 5.2). We have two commutative diagram and an equiva-
lence between them induced by the diffeomorphism θ:
Diskfr
n -Alg
≃
/
(
PFaclc
D
Faclc
Rn
o
≃
w
Faclc
D
?
O
(23)
En-Alg
'
≃
/ PFaclc
R
Faclc
(0,1)n
≃
w
o
Faclc
R
?
O
(24)
where the dotted arrows exists by Theorem 8 and the diagonal right equivalences
are given by Proposition 17. Since the embedding of factorization algebras in pref-
actorization algebras (over any cover or space) is fully faithful, we obtain that all
maps in Diagrams (23) and (24) are equivalences so that we recover the equiva-
lence En-Alg ∼= Faclc
Rn ∼= Faclc
(0,1)n of Theorem 9, also see [Ca2].
Example 19 (Constant factorization algebra on framed manifolds). Let M be a
framed manifold of dimension n. By Theorem 8 or [L3, GTZ2], any En-algebra A
39note that factorization algebras are described by operads in discrete space together with the
ˇCech condition, see Remark 24
40Note that the category of D-prefactorization algebras is the category of algebras over the col-
ored operad N(Disk(Rn)), see Remark 24.
40


## Page 41


yields a locally constant factorization algebra A on M which is deﬁned by assign-
ing to any geodesic disk D the chain complex A (D) ∼= A. We call such a factoriza-
tion algebra the constant factorization algebra on M associated to A since it satis-
ﬁes the property that there is a (globally deﬁned) En-algebra A together with natural
(with respect to the structure map of the factorization algebra) quasi-isomorphism
A (D) ≃→A for every disk D.
In particular, for n = 0,1,3,7, there is a faithful embedding of En-algebras into
constant factorization algebras over the n-sphere Sn.
If a manifold X is not framable, we can obtain constant factorization algebras
on X by using (un)oriented En-algebras instead of plain En-algebras:
Example 20 (Constant factorization algebra on (oriented) smooth manifolds). Let
A be an unoriented En-algebra (i.e. a Diskun
n -algebra, Example 12). Then A yields a
(locally) constant factorization A algebra on any smooth manifold of dimension n
which is deﬁned by assigning to any geodesic disk D the chain complex A (D) ∼= A.
Similarly, an oriented En-algebra (i.e. a Diskor
n -algebra) yields a (locally) con-
stant factorization algebra on any oriented dimension n manifold.
Example 21 (Commutative factorization algebras). The canonical functor E∞-Alg →
Disk(X,e)
n
-Alg (see Example 13) shows that any E∞-algebras induces a canonical
structure of (locally) constant factorization algebra on any (topological) manifold
M. In that case, the factorization homology reduces to the derived Hochschild
chains according to Theorem 8 and Theorem 10 below. See § 8.2 for more details.
Theorem 10. If A is an E∞-algebra41, then, for every topological manifold M, there
is an natural equivalence CHM(A) ∼=
R
M A. In particular, factorization homology of
E∞-algebras extends uniquely as an homology theory for spaces (see Deﬁnition 1).
Proof. This is proved in [GTZ2], also see [F1]. The result essentially follows by
uniqueness of the homology theories (Theorem 6). Namely, if HA is an homology
theory for spaces whose value on a point is A, then HA(Rn) = A (Rn is contractible)
and further HA satisﬁes the monoidal and excision axioms of a homology theory
for manifolds.
Example 22 (pre-cosheaves). Let P be a pre-cosheaf on X (with values in vector
spaces or chain complexes). For any open U ⊂X, set F(U) := S•(P(U)) =
L
n≥0(P(U)⊗n)Sn where S• is the free (differential graded) commutative algebra
functor. Then F is a prefactorization algebra with structure maps given by the
algebra structure of S•(P(V)):
F(U1)⊗···⊗F(Ui) ∼= S•(P(U1))⊗···⊗S•(P(Ui))
⊗S•(P(Ui→V))
−→
S•(P(V))⊗···⊗S•(P(V)) −→S•(P(V)) = F(V).
41for instance a (differential graded) commutative algebra
41


## Page 42


Proposition 11 (cf. [CG]). If F is a homotopy cosheaf, then F is a factorization
algebra (not necessarily locally constant).
In characteristic zero, if P is a homotopy cosheaf, then F is a factorization
algebra.
Example 23 (Observables). Several examples of (pre-)factorization algebras aris-
ing from theoretical physics (more precisely from perturbative quantum ﬁeld theo-
ries) are described in the beautiful work [CG, C2]. They arose as deformations of
those obtained as in the previous Example 22. For instance, let E →X be a (possi-
bly graded) vector bundle over a smooth manifold X. Let E be the sheaf of smooth
sections of E (which may be endowed with a differential which is a differential
operator) and E
′ be its associated distributions. The above construction yields a
(homotopy) factorization algebra U 7→S(E
′(U)) = L
n≥0 HomOX(U)(E (U)⊗n,R).
In [CG], Costello-Gwilliam have been reﬁning this example to equip the classical
observables of a classical ﬁeld theory with the structure of a factorization algebra
(with values in P0-algebras, Example 64). Their construction is a variant of the
classical AKSZ formalism [AKSZ]. Related constructions are studied in [Pa].
Further, the quantum observables of a quantization of the classical ﬁeld theory,
when they exist, also form a factorization algebra (not necessarily locally constant).
A very nice example of this procedure arises when X is an elliptic curve, see [C2].
These factorization algebras (with values in lax P0-algebras) encode the alge-
braic structure governing observables of the ﬁeld theories (in the same way as the
observables of classical mechanics are described by the algebra of smooth func-
tions on a manifold together with its Poisson bracket). Very roughly speaking, the
locally constant factorization algebras correspond to observables of topological
ﬁeld theories.
Example 24 (Enveloping factorization algebra of a dg-Lie algebra). Let L be a ho-
motopy cosheaf of differential graded Lie algebras on a Hausdorff space X, over a
characteristic zero ring. For instance, L can be the cosheaf of compactly supported
forms Ω•,c
dR,M ⊗g with value in g where g is a differential graded Lie algebra and
Ω•
dR,M is the (complex of) sheaf on a manifold M given by the de Rham complex.
If M is a complex manifold, another interesting example is obtained by substituting
the Dolbeaut complex to the de Rham complex.
For any open U ⊂X, we can form the Chevalley-Eilenberg chain complex
CCE
•
 L (U)

of the (dg-)Lie algebra L (U). Its underlying k-module (see [W]) is
given by
CCE
•
 L (U)

:= S• L (U)[1]

and its differential is induced by the Lie bracket and inner differential of L . The
structure maps of Example 22 (applied to F = L [1]) are maps of chain complexes
(since L is a precosheaf of dg-Lie algebras), hence make CCE
•
 L (−)

a prefactor-
ization algebra over X, which we denote CCE(L ) (note that this construction only
requires L to be a precoheaf of dg-Lie algebras). As a corollary of Proposition 11,
one obtains
42


## Page 43


Corollary 2 (Theorem 4.5.3, [Gw]). If L is a homotopy cosheaf of dg-Lie alge-
bras, the prefactorization algebra CCE(L ) is a (homotopy) factorization algebra.
The above corollary extends to homotopy cohseaves of L∞-algebras as well.
This construction actually generalizes the construction of the universal en-
veloping algebra of a Lie algebra which corresponds to the case L = Ω•,c
dR,R ⊗g
([Gw]).
More generally the observables of Free Field Theories can be obtained this
way, see [Gw] for many examples.
Remark 24 (Algebras over disks in X). Assume X has a cover by euclidean neigh-
borhoods. One can deﬁne a colored operad whose objects are open subsets of
X that are homeomorphic to Rn and whose morphisms from {U1,··· ,Un} to V
are empty except when the Ui’s are mutually disjoint subsets of V, in which case
they are singletons. We can take the monoidal envelope of this operad (as in Ap-
pendix 10.2 or [L3, §2.4]) to get a symmetric monoidal ∞-category Disk(X) (also
see [L3], Remark 5.2.4.7). For any symmetric monoidal ∞-category C , we thus get
the ∞-category Disk(X)-Alg := Fun⊗(Disk(X),C ) of Disk(X)-algebras. Unfold-
ing the deﬁnition we ﬁnd that a Disk(X)-algebra is precisely a Disk-prefactorization
algebra over X where Disk is the set of all open disks in X.
A Disk(X)-algebra is locally constant if for any inclusion of open disks U ,→V
in X, the structure map F(U) →F(V) is a quasi-isomorphism (see [L3]). By
Theorem 8 and [L3, §5.2.4], locally constant N(Disk(M))-algebras are the same as
locally constant factorization algebras. Hence we have
Proposition 12. A locally constant Disk-prefactorization algebra has an unique
extension as a locally constant homotopy factorization algebra. In fact, the functor
Faclc
X →PFaclc
Disk ∼= Disk(X)-Alglc is an equivalence.
In particular, a locally constant prefactorization algebra F has an unique ex-
tension as a locally constant factorization algebra F ◦taking the same values as
F on any disk.
Example 25. The unique extension F ◦of F as a factorization algebra can have
different values than F and two different prefactorization algebras on X can have
the same values on the open cover Disk. As a trivial example, let X = {x,y} be
a two points discrete set. Then a Disk-prefactorization algebra is given by two
pointed chain complexes F({x}) = Vx, F({y}) = Vy. It is locally constant and
the associated factorization algebra is given by F ◦({x,y}) ∼= Vx ⊗Vy. However,
if W is any chain complex with pointed maps Vx →W, Vy →W then we have a
prefactorization algebras G deﬁned by G (X) = W and is otherwise the same as
F ◦. In particular, G is a prefactorization algebra on X with the same values as F ◦
on the disks of X but is different from F ◦.
The notion of being locally constant for a factorization algebra is indeed a
local property (though its deﬁnition is about all disks) as proved by the following
result.
43


## Page 44


Proposition 13. Let M be a topological manifold and F be a factorization algebra
on M. Assume that there is an open cover U of M such that for any U ∈U the
restriction F|U is locally constant. Then F is locally constant on M.
See § 9.1 for a proof.
Remark 25 (Ran space). Factorization algebras on X can be seen as a certain kind
of cosheaf on the Ran space of X. This deﬁnition is actually the correct one to deal
with factorization algebras in the algebraic geometry context (see [BD, FG]). The
Ran space Ran(X) of a manifold X is the space of ﬁnite non-empty subsets of X.
Its topology42 is the coarsest topology on Ran(X) for which the sets Ran({Ui}i∈I)
are open for every non-empty ﬁnite collection of pairwise disjoint opens subsets
Ui (i ∈I) of X. Here, the set Ran({Ui}i∈I) is the collection of all ﬁnite subsets
{xj}j∈J ⊂X such that {xj}j∈J ∩Ui is non empty for every i ∈I.
Two subsets U, V of Ran(X) are said to be independent if the two subsets
 S
S∈U S

⊂X and
 S
T∈V T

⊂X are disjoint (as subsets of X). If U, V are subsets
of Ran(X), one denotes U ⋆V the subset {S∪T, S ∈U, T ∈V} of Ran(X).
It is proved in [L3] that a factorization algebra on X is the same thing as a
constructible cosheaf F on Ran(X) which satisﬁes in addition the factorizing con-
dition, that is, that satisﬁes that, for every family of pairwise independent open
subsets, the canonical map
F(U1)⊗···⊗F(Un) −→F(U1 ⋆···⋆Un)
is an equivalence (the condition is similar to Remark 20).
This characterization explain why there is a similarity between cosheaves and
factorization algebras. However, the factorization condition is not a purely cosheaf
condition and is not compatible with every operations on cosheaves.
5
Operations for factorization algebras
In this section we review many properties and operations available for factorization
algebras.
5.1
Pushforward
If F is a prefactorization algebra on X, and f : X →Y is a continuous map, one
can deﬁne the pushforward f∗(F) by the formula f∗(F)(V) = F(f −1(V)). If F
is an (homotopy) factorization algebra then so is f∗(F), see [CG].
Proposition 14. The pushforward is a symmetric monoidal functor f∗: FacX →
FacY and further (f ◦g)∗= f∗◦g∗.
42this topology is closely related (but different) to the ﬁnal topology on Ran(X) making the
canonical applications Xn →Ran(X) (n > 0) continuous
44


## Page 45


Let us abusively denote G for the global section G (pt) of a factorization alge-
bra over the point pt. Let p : X →pt be the canonical map. By Theorem 8, when
X is a manifold and FA is a locally constant factorization algebra associated to a
Disk(X,TX)
n
-algebra, then the factorization homology of M is
Z
X A ∼= FA(A) ∼= p∗(FA).
(25)
This analogy legitimates to call p∗(F), that is the (derived) global sections of F,
its factorization homology:
Deﬁnition 17. The factorization homology43 of a factorization algebra F ∈FacX
is p∗(F) and is also denoted
R
X F.
Proposition 15. Let f : X →Y be a locally trivial ﬁbration between smooth mani-
folds. If F ∈FacX is locally constant, then f∗(F) ∈FacY is locally constant.
Proof. Let U ,→V be an inclusion of an open sub-disk U inside an open disk V ⊂
Y. Since V is contractible, it can be trivialized so we can assume f −1(V) = V ×F
with F a smooth manifold. Taking a stable by ﬁnite intersection and factorizing
cover V of F by open disks, we have a factorizing cover {V} × V of f −1(V)
consisting of open disks in X. Similarly {U}×V is a factorizing cover of f −1(U)
consisting of open disks. In particular for any D ∈V , the structure map F(U ×
D) →F(V × D) is a quasi-isomorphism since F is locally constant. Thus the
induced map ˇC({U} × V ,F) →ˇC({V} × V ,F) is a quasi-isomorphism as well
which implies that f∗(F)(U) →f∗(F)(V) is a quasi-isomorphism.
Example 26. Locally constant factorization algebras induced on a submanifold Let
i : X ,→Rn be an embedding of a manifold X into Rn and NX be an open tubular
neighborhood of X in Rn. We write q : NX →X for the bundle map. If A is an
En-algebra, then it deﬁnes a factorisation algebra FA on Rn. Then the pushforward
q∗(FA |NX) is a locally constant (by Proposition 15) factorization algebra on X,
which is not constant in general if the normal bundle NX is not trivialized.
Since a continuous map f : X →Y yields a factorization X
f→Y →pt of
X →pt, Proposition 14 and the equivalence (25) imply the following pushforward
formula of factorization homology.
Proposition 16 (pushforward formula). Let X
f→Y be continuous and F be in
FacX. The factorization homology of F over X is the same as the factorization
homology of f∗(F) over Y:
Z
X F ∼= p∗(F) ∼= p∗
 f∗(F)
 ∼=
Z
Y f∗(F).
(26)
43recall that we are considering homotopy factorization algebras, which are already derived ob-
jects. If G is a genuine factorization algebra (Remark 21), then its factorization homology would be
Lp∗(G ) := p∗( ˜G) where ˜G is an acyclic resolution of G (as genuine factorization algebra)
45


## Page 46


5.2
Extension from a basis
Let U be a basis stable by ﬁnite intersections for the topology of a space X and
which is also a factorizing cover. Let F be a (homotopy) U -factorization alge-
bra, that is a U -prefactorization algebra (Deﬁnition 12) such that, for any U ∈U
and factorizing cover V of U consisting of open sets in U , the canonical map
ˇC(V ,F) →F(U) is a quasi-isomorphism.
Proposition 17 (Costello-Gwilliam [CG]). There is an unique44 (homotopy) fac-
torization algebra iU
∗(F) on X extending F (that is equipped with a quasi-isomorphism
of U -factorization algebras iU
∗(F) →F).
Precisely, for any open set V ⊂X, one has
iU
∗(F)(V) := ˇC(UV,F)
where UV is the open cover of V consisting of all open subsets of V which are in
U .
Note that the uniqueness is immediate since, if G is a factorization algebra on
X, then for any openV the canonical map ˇC(UV,G ) →G (V) is a quasi-isomorphism
and, further, the ˇCech complex ˇC(UV,G ) is computed using only open subset in
U .
Proposition 17 gives a way to construct (locally constant) factorization algebras
as we now demonstrate.
Example 27. By Example 19, we know that an associative unital algebra (possibly
differential graded) gives a locally constant factorization algebra on the interval
R. It can be explicitly given by using extension along a basis. Indeed, the collec-
tion I of intervals (a,b) (a < b) is a factorizing basis of opens, which is stable
by ﬁnite intersections. Then one can set a I -prefactorization algebra FA by set-
ting FA((a,b)) := A. For pairwise disjoints open interval I1,...,In ⊂I, where the
indices are chosen so that sup(Ii) ≤inf(Ii+1), the structure maps are given by
A⊗n = FA(I1)⊗···⊗FA(In)
−→
FA(I) = A
(27)
a1 ⊗···⊗an
7−→
a1 ···an .
(28)
To extend this construction to a full homotopy factorization algebra on R, one
needs to check that FA is a I -factorization algebra which is the content of Propo-
sition 27 below.
In the construction, we have chosen an implicit orientation of R; namely, in the
structure map (27), we have decided to multiply the elements (ai) by choosing to
order the intervals in increasing order from left to right.
Let τ : R →R be the antipodal map x 7→−x reversing the orientation. One
can check that τ∗(FA) = FAop where Aop is the algebra A with opposite multipli-
cation (a,b) 7→b·a. In other words, choosing the opposite orientation (that is the
decreasing one) of R amounts to replacing the algebra by its opposite algebra.
44up to contractoble choices
46


## Page 47


Example 28 (back to the circle). The circle S1 also has a (factorizing) basis given
by the open (embedded) intervals (of length less than half of the perimeter of the
circle in order to be stable by intersection). Choosing an orientation on the circle,
one can deﬁne a (homotopy) factorization algebra SA on the circle using again
the structure maps (27). This gives an explicit construction of the factorization
algebra associated to a framing of S1 from Example 19 (since they agree on a
stable by ﬁnite intersection basis of open sets). The global section of SA are thus
the Hochschild chains of A by the computation (18).
Similarly to Example 27, choosing the opposite framing on the circle amounts
to considering the factorization algebra SAop. However, unlike on R, there is an
equivalence SA ∼= SAop induced by the fact that there is an orientation preserving
diffeomorphism between the to possible orientations of the circle and that further,
the value of SA on any interval is constant.
5.3
Exponential law: factorization algebras on a product
Let π1 : X ×Y →X be the canonical projection. By Proposition 15, we have the
pushforward functor π1∗: Faclc
X×Y →Faclc
X . This functor has an natural lift into
Faclc(Y). Indeed, if U is open in X and V is open in Y, we have a chain complex:
π1∗(F)(U,V) := F(π1−1
|X×V(U)) = F(U ×V).
Let V1,...,Vi be pairwise disjoint open subsets in an open set W ⊂Y and consider
π1∗(F)(U,V1)⊗···⊗π1∗(F)(U,Vi) ∼= F(U ×V1)⊗···⊗F(U ×Vi)
ρU×V1,...,U×Vi,U×W
−→
F(U ×W) = π1∗(F)(U,W).
(29)
The map (29) makes π1∗(F)(U) a prefactorization algebra on Y. If U1,...,Uj are
pairwise disjoint open inside an open O ⊂X, the collection of structure maps
π1∗(F)(U1,V)⊗···⊗π1∗(F)(Uj,V) ∼= F(U1 ×V)⊗···⊗F(Uj ×V)
ρU1×V,...,Uj×V,O×V
−→
F(O×V) = π1∗(F)(O,V)
(30)
indexed by opens V ⊂Y is a map π1∗(F)(U1)⊗···⊗π1∗(F)(Uj) −→π1∗(F)(O)
of prefactorization algebras over Y.
Combining the two constructions, we ﬁnd that the structure maps (29) and (30)
make π1∗(F) a prefactorization algebra over X with values in the category of pref-
actorization algebras over Y. In other words we have just deﬁned a functor:
π1∗: PFacX×Y −→PFacX(PFacY)
(31)
ﬁtting into a commutative diagram
PFacX×Y
π1∗/
(π1)∗
'
PFacX(PFacY)
PFacX(p∗)

PFacX
47


## Page 48


where p∗is given by Deﬁnition 17.
Proposition 18. Let π1 : X ×Y →X be the canonical projection. The pushfor-
ward (31) by π1 induces a functor
π1∗: FacX×Y −→FacX(FacY)
and, if X, Y are smooth manifolds, an equivalence π1∗: Faclc
X×Y
≃
−→Faclc
X (Faclc
Y )
of ∞-categories .
See § 9.1 for a proof.
The above Proposition is a slight generalization of (and relies on) the follow-
ing ∞-category version of the beautiful Dunn’s Theorem [Du] proved under the
following form by Lurie [L3] (see [GTZ2] for the pushforward interpretation):
Theorem 11 (Dunn’s Theorem). There is an equivalence of ∞-categories
Em+n-Alg
≃
−→Em-Alg(En-Alg).
Under the equivalence En-Alg ∼= Faclc
Rn (Theorem 9), the above equivalence is real-
ized by the pushforward π∗: Faclc
Rm×Rn →Faclc
Rm(Faclc
Rn) associated to the canon-
ical projection π : Rm ×Rn →Rm.
Example 29 (PTVV construction). There is a derived geometry variant of the
AKSZ formalism introduced recently in [PTTV] which leads to factorization al-
gebras similarly to Example 23. We brieﬂy sketch it. The main input is a (de-
rived Artin) stack X (over a characteristic zero ﬁeld) which is assumed to be com-
pact and equipped with an orientation (write dX for the dimension of X) and a
stack Y with an n-shifted symplectic structure ω (for instance take Y to be the
shifted cotangent complex Y = T ∗[n]Z of a scheme Z). The natural evaluation
map ev : X ×RMap(X,Y) allows to pullback the symplectic structure on the space
of ﬁelds RMap(X,Y). Precisely, RMap(X,Y) carries an natural (n−dX)-shifted
symplectic structure roughly given by the integration
R
[X] ev∗(ω) of the pullback of
ω on the fundamental class of X. It is expected that the observables ORMap(X,Y)
carries a structure of P1+n−dX-algebra. Assume further that X is a Betti stack, that
is in the essential image of Top →dStk. It will then follow from Corollary 1
and Example 21 that ORMap(X,Y) belongs to Faclc
X (P1+n−dX-Alg). Using the for-
mality of the little disks operads in dimension ≥2, Proposition 18 then will give
ORMap(X,Y) the structure of a locally constant factorization algebra on X ×R1+n−dX
when n > dX. It is also expected that the quantization of such shifted symplectic
stacks shall carries canonical locally constant factorization algebras structures.
Note that the Pantev-To¨en-Vaqui´e-Vezzosi construction was recently extended
by Calaque [Ca] to add boundary conditions. The global observables of such rel-
ative mapping stacks shall be naturally endowed with the structure of locally con-
stant factorization algebra on stratiﬁed spaces (as deﬁned in § 6).
Proposition 18 and Theorem 8 have the following consequence
48


## Page 49


Corollary 3 (Fubini formula [GTZ2]). Let M, N be manifolds of respective dimen-
sion m, n and let A be a Disk(M×N,T(M×N))
n+m
-algebra. Then,
R
N A has a canonical
structure of Disk(M,TM)
m
-algebra and further,
Z
M×N A ∼=
Z
M
Z
N A

.
Example 30. Let A be a smooth commutative algebra. By Hochschild-Kostant-
Rosenberg theorem (see Example 6), CHS1(A) ≃→S•
A(Ω1(A)[1]); this algebra is
also smooth. Since A is commutative it deﬁnes a factorization algebra on the torus
S1 ×S1. By Corollary 3, we ﬁnd that
Z
S1×S1 A ∼=
Z
S1
 S•
A(Ω1(A)[1])
 ∼= S•
A

Ω1(A)[1]⊕Ω1(A)[1]⊕Ω1(A)[2]

.
5.4
Pullback along open immersions and equivariant factorization al-
gebras
Let f : X →Y be an open immersion and let G be a factorization algebra on Y.
Since f : X →Y is an open immersion, the set
Uf := {U open in X such that f|U : U →Y is an homeomorphism}
is an open cover of X as well as a factorizing basis.
For U ∈Uf , we deﬁne
f ∗(G )(U) := G (f(U)). The structure maps of G make f ∗(G ) a Uf -factorization
algebra in a canonical way. Thus by Proposition 17, iUf
∗(f ∗(G )) is the factorization
algebra on X extending f ∗(G ) . We (abusively) denote f ∗(G ) := iUf
∗(f ∗(G )) and
call it the pullback along f of the factorization algebra G .
Proposition 19 ([CG]). The pullback along open immersion is a functor f ∗: FacY →
FacX. If f : X →Y and g : Y →Z are open immersions, then (g◦f)∗= f ∗◦g∗.
If U ∈Uf , then U is an open subset of the open set f −1(f(U)). Thus if F is a
factorization algebra on X, we have the natural map
F(U)
ρU,f−1(f(U))
−→
F(f −1(f(U))) ∼= f ∗(f∗(F))(U)
(32)
which is a map of Uf -factorization algebras. Since F and f ∗(f∗(F)) are factor-
ization algebras on X, the above map extends uniquely into a map of factorization
algebras on X. We have proved:
Proposition 20. Let f : X →Y be an open immersion. There is an natural trans-
formation IdFacX →f ∗f∗induced by the maps (32).
Example 31. Let X = {c,d} be a discrete space with two elements and consider
the projection f : X →pt. A factorization algebra G on pt is just the data of a
chain complex G with a distinguished cycle g0 while a factorization algebra F
49


## Page 50


on X is given by two chain complexes C, D (with distinguished cycles c0, d0)
and the rule F({c}) = C, F({d}) = D, F({c}) = C
id⊗{d0}
−→C ⊗D = F(X) and
F({d}) = C
{c0}⊗id
−→C ⊗D = F(X). In that case we have that
f ∗(f∗(F)({x}) = C ⊗D = f ∗(f∗(F)({y}) = f ∗(f∗(F)(X)
while f∗(f ∗(G ))(pt) = F ⊗F. Note that there are no natural transformation of
chain complexes F ⊗F →F in general; in particular f ∗and f∗are not adjoint.
In fact f∗does not have any adjoint in general; indeed as the above example of
F : {c,d} →pt demonstrates, f∗does not commute with coproducts nor products.
We now turn on to a descent property of factorization algebras. Let G be a
discrete group acting on a space X. For g ∈G, we write g : X →X the homeomor-
phism x 7→g·x induced by the action.
Deﬁnition 18. A G-equivariant factorization algebra on X is a factorization alge-
bra G ∈FacX together with, for all g ∈G, (quasi-)isomorphisms of factorization
algebras
θg : g∗(G ) ≃→G
such that θ1 = id and
θgh = θh ◦h∗(θg) : h∗(g∗(G )) →G .
We write FacG
X for the category of G-equivariant factorization algebras over X.
Assume G acts properly discontinuously and X is Hausdorff so that the quotient
map q : X →X/G is an open immersion. If F is a factorization algebra over
X/G, then q∗(F) is G-equivariant (since q(g·x) = q(x)). We thus have a functor
q∗: FacX/G −→FacG
X.
Proposition 21 (Costello-Gwilliam [CG]). If the discrete group G acts properly
discontinuously on X, then the functor q∗: FacX/G −→FacG
X is an equivalence of
categories.
The proof essentially relies on considering the factorization basis given by triv-
ialization of the principal G-bundle X →X/G to deﬁne an inverse to q∗.
Proposition 22. If the discrete group G acts properly discontinuously on a smooth
manifold X, then the equivalence q∗: FacX/G −→FacG
X factors as an equivalence
q∗: Faclc
X/G −→(Faclc
X )G between the subcategories of locally constant factoriza-
tion algebras.
Proof. Let U be an open set such that q|U : U →X/G is an homeomorphism onto
its image. Then, for every open subset V of U, q∗(F)(V) = F(q(V)). Thus, if
F satisﬁes the condition of being locally constant for disks included in U, then
so does q∗(F) for disks included in q(U). Hence, by Proposition 13, q∗(F) is
locally constant if F is locally constant.
50


## Page 51


Now, assume G ∈FacG
X is locally constant. Then (q∗)−1(G ) is the factorization
algebra deﬁned on every section X/G ⊃U →σ(U) ⊂X of q (with U open) by
(q∗)−1(G )(U) = G (σ(U)). Since every disk D is contractible, we always have a
section D →X of q|D. Thus, if G is locally constant, then so is (q∗)−1(G ).
Remark 26 (General deﬁnition of equivariant factorization algebras). Deﬁnition 18
can be easily generalized to topological groups as follows. Indeed, if G acts contin-
uously on X, then the rule (g,F) 7→g∗(F) induces a right action of G on FacX 45.
The ∞-category of G-equivariant factorization algebras is the ∞-category of
homotopy G-ﬁxed points of FacX:
FacG
X := (FacX)hG.
This ∞-category is equivalent to the one of Deﬁnition 18 for discrete groups. It is
the ∞-category consisting of a factorization algebra G on X together with quasi-
isomorphisms of factorization algebras θg : g∗(G ) →G (inducing a ∞-functor
BG →FacX, where BG is the ∞-category associated to the topological category
with a single object and mapping space of morphisms given by G) and equiva-
lences θgh ∼θh ◦h∗(θg) satisfying some higher coherences.
5.5
Example: locally constant factorization algebras over the circle
Let q : R →S1 = R/Z be the universal cover of S1 and let F be a locally constant
factorization algebra on S1. By Proposition 22, F is equivalent to the data of
a Z-equivariant locally constant factorization algebra on R which is the same as
a locally constant factorization algebra over R together with an equivalence of
factorization algebras, the equivalence being given by θ1 : 1∗(q∗(F)) ≃→q∗(F).
By Theorem 9, the category of locally constant factorization algebras on R is the
same as the category of E1-algebras, and thus is equivalent to its full subcategory
of constant factorization algebras. It follows that we have a canonical equivalence
1∗(G ) ∼= G for G ∈Faclc
R (in particular, for any open interval I, the structure map
1∗(G (I)) = G (1+I) →G (R) is a quasi-isomorphism).
Deﬁnition 19. We denote mon : q∗(F) ∼= 1∗(q∗(F))
θ1
→q∗(F) the self-equivalence
of q∗(F) induced by θ1 and call it the monodromy of F.
We thus get the following result
Corollary 4. The category Faclc
S1 of locally constant factorization algebra on the
circle is equivalent to the ∞-category Aut(E1-Alg) of E1-algebras equipped with a
self-equivalence.
Remark 27. Using Proposition 18, it is easy to prove similarly that Faclc
S1×S1 is
equivalent to the category of E2-algebras equipped with two commuting mon-
odromies (i.e. self-equivalences).
45that is a map of E1-algebras (in Top) from Gop to Fun(FacX,FacX)
51


## Page 52


It seems harder to describe the categories of locally constant factorization alge-
bras over the spheres S3, S7 in terms of E3 and E7-algebras (due to the complicated
homotopy groups of the spheres). However, for n = 3,7, there shall be an embed-
ding of the categories of En-algebras equipped with an n-gerbe46 into Faclc
Sn.
Let F be a locally constant factorization algebra on S1 (identiﬁed with the
unit sphere in C). We wish to compute the global section of F (i.e. its factoriza-
tion homology
R
S1 F). Let B ∼= F(S1 \ {1}) be its underlying E1-algebra (with
monodromy mon : B ≃→B). We use the orthogonal projection π : S1 →[−1,1]
from S1 to the real axis. The equivalence (26) yields F(S1) ∼= π∗(F)([−1,1])
and by Proposition 15 and Proposition 27, we are left to compute the E1-algebra
π∗(F)
 (−1,1)

and left and right modules π∗(F
 (−1,1]

, π∗(F)
 [−1,1)

. From
Example 27, we get π∗(F)
 (−1,1)
 ∼= B ⊗Bop. Further,
π∗(F)
 [−1,1)
 ∼= F(S1 \{1}) = B
(as a B ⊗Bop-module).
Similarly π∗(F)
 (−1,1]
 ∼= Bmon, that is B viewed as a B⊗Bop-module through
the monodromy. When B is actually a differential graded algebra, then the bi-
module stucture of Bmon boils down to a · x · b = mon(b) · m · a. This proves the
following which is also asserted in [L3, §5.3.3].
Corollary 5. Let B be a locally constant factorization algebra on S1. Let B be a
differential graded algebra and mon : B ≃→B be a quasi-isomorphism of algebras
so that (B,mon) is a model for the underlying E1-algebra of B and its monodromy.
Then the factorization homology
Z
S1 B ∼= B
L⊗
B⊗Bop Bmon ∼= HH(B,Bmon)
is computed by the (standard) Hochschild homology47 HH(B) of B with value in B
twisted by the monodromy.
Example 32 (the circle again). Let p : R →S1 be the universal cover of S1. By
Example 27, an unital associative algebra A deﬁnes a locally constant factorization
algebra, denoted A , on R. By Proposition 15, the pushforward p∗(A ) is a locally
constant factorization algebra on S1, which, on any interval I ⊂S1 is given by
p∗(A )(I) = A (I × Z) = A⊗Z. It is however not a constant factorization algebra
since the global section of p∗(A ) is different from the Hochschild homology of A:
p∗(A )(S1) = A (R) ∼= A ̸≃HH(A⊗Z)
(for instance if A is commutative the Hochschild homology of A⊗Z is A⊗Z in degree
0.) Indeed, the monodromy of A is given by the automorphism σ of A which sends
the element ai in the tensor index by an integer i into the tensor factor indexed by
i+1, that is σ
 N
i∈Z ai

= N
i∈Z ai−1.
However, by Corollary 5, we have that, for any E1-algebra A,
HH
 A⊗Z,
 A⊗Zmon ∼= A.
46by an n-gerbe over A ∈En-Alg, we mean a monoid map Z →Ωn−1MapEn-Alg(A,A).
47in particular by the standard Hochschild complex (see [L]) C∗(B,Bmon) when B is ﬂat over k
52


## Page 53


5.6
Descent
There is a way to glue together factorization algebras provided they satisfy some
descent conditions which we now explain.
Let U be an open cover of a space X (which we assume to be equipped with
a factorizing basis). We also assume that all intersections of inﬁnitely many dif-
ferent opens in U are empty. For every ﬁnite subset {Ui}i∈I of U , let FI be a
factorization algebra on T
i∈IUi. For any i ∈I, we have an inclusion si : T
i∈IUi ,→
T
j∈I\{i}Uj.
Deﬁnition 20. A gluing data is a collection, for all ﬁnite subset {Ui}i∈I ⊂U and
i ∈I, of quasi-isomorphisms rI,i : FI −→
 FI\{i}

|UI such that, for all I, i, j ∈I,
the following diagram commutes:
FI
rI,i

rI,j
/  FI\{ j}

|UI
rI\{j},i

 FI\{i}

|UI
rI\{i},j
/  FI\{i,j}

|UI.
Given a gluing data, one can deﬁne a factorizing basis VU given by the family
of all opens which lies in some U ∈U . For any V ∈VU , set F(V) = FIV (V)
where IV is the largest subset of I such that V ∈T
j∈IV Uj. The maps RI,i induce a
structure of VU -prefactorization algebra.
Proposition 23 ([CG]). Given a gluing data, the VU -prefactorization F extends
uniquely into a factorization algebra F on X whose restriction F|UI on each UI
is canonically equivalent to FI.
Note that if the FI are the restrictions to UI of a factorization algebra F, then
the collection of the FI satisfy the condition of a gluing data.
6
Locally constant factorization algebras on stratiﬁed spaces
and categories of modules
There is an interesting variant of locally constant factorization algebras over (topo-
logically) stratiﬁed spaces which can be used to encode categories of En-algebras
and their modules for instance. Note that by Remark 20, all our categories of
modules will be pointed, that is coming with a preferred element. We gave the
deﬁnition and several examples in this Section. An analogue of Theorem 8 for
stratiﬁed spaces shall provide the link between the result in this section and results
of [AFT].
53


## Page 54


6.1
Stratiﬁed locally constant factorization algebras
In this paper, by a stratiﬁed space of dimension n, we mean a Hausdorff paracom-
pact topological space X, which is ﬁltered as the union of a sequence of closed
subspaces /0 = X−1 ⊂X0 ⊂X1 ⊂··· ⊂Xn = X such that any point x ∈Xi \Xi−1 has
a neighborhood Ux
φ≃Ri ×C(L) in X where C(L) is the (open) cone on a stratiﬁed
space of dimension n −i −1 and the homeomorphism preserves the ﬁltration48.
We further require that X \ Xn−1 is dense in X. In particular, a stratiﬁed space of
dimension 0 is simply a topological manifold of dimension 0 and Xi \ Xi−1 is a
topological manifold of dimension i (possibly empty or non-connected).
The connected components of Xi \ Xi−1 are called the dimension i-strata of X.
We always assume that X has at most countable strata.
Deﬁnition 21. An open subset D of X is called a (stratiﬁed) disk if it is homeo-
morphic to Ri ×C(L) with L stratiﬁed of dimension n−i−1, the homeomorphism
preserves the ﬁltration and further D∩Xi ̸= /0 and D ⊂X \Xi−1. We call i the index
of the (stratiﬁed disk) D. It is the smallest integer j such that D∩Xj ̸= /0
We say that a (stratiﬁed) disk D is a good neighborhood at Xi if i is the index
of D and D intersects only one connected component of Xi \Xi−1.
A factorization algebra F over a stratiﬁed space X is called locally constant
if for any inclusion of (stratiﬁed) disks U ,→V such that both U and V are good
neighborhoods at Xi (for the same i ∈{0,...,n})49, the structure map F(U) →
F(V) is a quasi-isomorphism.
The underlying space of almost all examples of stratiﬁed spaces X arising in
these notes will be a manifold (with boundary or corners). In that cases, all (strati-
ﬁed) disk are homeomorphic to to a standard euclidean (half-)disk Rn−j ×[0,+∞)j.
Let X be a manifold (without boundary) and let Xstr be the same manifold
endowed with some stratiﬁcation. A locally constant factorization algebra on X is
also locally constant with respect to the stratiﬁcation. Thus, we have a fully faithful
embedding
Faclc
X −→Faclc
Xstr.
(33)
Several general results on locally constant factorization algebras from § 4 have
analogues in the stratiﬁed case. We now list three useful ones.
Proposition 24. Let X be a stratiﬁed manifold and F be a factorization algebra on
X such that there is an open cover U of X such that for any U ∈U the restriction
F|U is locally constant. Then F is locally constant on X.
The functor (33) generalizes to inclusion of any stratiﬁed subspace.
48that is φ(Ux ∩Xi+j+1) = Ri ×C(Lj) for 0 ≤j ≤n−i−1
49in other words are good neighborhoods of same index
54


## Page 55


Proposition 25. Let i : X ,→Y be a stratiﬁed (that is ﬁltration preserving) embed-
ding of stratiﬁed spaces in such a way that i(X) is a reunion of strata of Y. Then
the pushforward along i preserves locally constantness, that is lift as a functor
Faclc
X →Faclc
Y .
Proof. Let F be in Faclc
X and U ⊂D be good disks of index j at a neigborhood
of a strata in i(X). The preimage i−1(U) ∼= i(X) ∩U is a good disk of index j
in X and so is i−1(D). Hence i∗(F(U)) →i∗(F(D)) is a quasi-isomorphism.
On the other hand, if V ⊂Y \ i(X) is a good disk, then i∗(F(V)) ∼= k. Since the
constant factorization algebra with values k (example 18) is locally constant on
every stratiﬁed space, the result follows.
Let f : X →Y be a locally trivial ﬁbration between stratiﬁed spaces. We say
that f is adequatly stratiﬁed if Y has an open cover by trivializing (stratiﬁed) disks
V which are good neighborhoods satisfying that:
• f −1(V)
ψ≃V × F has a cover by (stratiﬁed) disks of the form ψ−1(V × D)
which are good neighborhoods in X;
• for sub-disks T ⊂U which are good neighborhoods (in V) with the same
index, then ψ−1(T × D) is a good neighborhood of X of same index as
ψ−1(U ×D).
Obvious examples of adequatly stratiﬁed maps are given by locally trivial stratiﬁed
ﬁbrations; in particular by proper stratiﬁed submersions according to Thom ﬁrst
isotopy lemma [Th, GMcP].
Proposition 26. Let f : X →Y be adequatly stratiﬁed. If F ∈FacX is locally
constant, then f∗(F) ∈FacY is locally constant.
Proof. Let U ,→V be an inclusion of open disks which are both good neighbor-
hoods at Yi; by proposition 24, we may assume V lies in one of the good trivializ-
ing disk in the deﬁnition of an adequatly stratiﬁed map so that we have a cover by
opens homeomorphic to (ψ−1(V ×Dj))j∈J which are good neigborhood such that
(ψ−1(U × D j))j∈J is also a good neighborhood of same index. This reduces the
proof to the same argument as the one of Proposition 15.
If X, Y are stratiﬁed spaces with ﬁnitely many strata, there is a natural strati-
ﬁcation on the product X ×Y, given by (X ×Y)k := S
i+j=k Xi ×Yj ⊂X ×Y. The
natural projections on X and Y are adequatly stratiﬁed.
Corollary 6. Let X, Y be stratiﬁed spaces with ﬁnitely many strata. The push-
forward π1∗: FacX×Y −→FacX(FacY) (see Proposition 18) induces a functor
π1∗: Faclc
X×Y −→Faclc
X (Faclc
Y ).
We conjecture that π1∗is an equivalence under rather weak conditions on X
and Y. We will give a couple of examples.
55


## Page 56


Proof. Since the projections are adequatly stratiﬁed, the result follows from Propo-
sition 18 together with Proposition 26 applied to both projections (on X andY).
Remark 28. Let F be a stratiﬁed locally constant factorization algebra on X.
Let U ⊂V be stratiﬁed disks of same index i, but not necessarily good neigh-
borhoods at Xi. Assume all connected component of V ∩Xi contains exactly one
connected component of U ∩Xi. Then the structure maps F(U) →F(V) is a
quasi-isomorphism. Indeed, we can take a factorizing cover V of V by good neigh-
borhoods D such that D ∩U are good neigborhoods. Then, F(D ∩U) →F(D)
is a quasi-isomorphism and thus we get a quasi-isomorphism ˇC(F,V ∩U) ≃→
ˇC(F,V ).
6.2
Factorization algebras on the interval and (bi)modules
Let us consider an important example: the closed interval I = [0,1] viewed as a
stratiﬁed space50 with two dimension 0-strata given by I0 = {0,1}.
The disks at I0 are the half-closed intervals [0,s) (s < 1) and (t,1] (0 <t) and the
disks at I1 are the open intervals (t,u) (0 < t < u < 1). The disks of (the stratiﬁed
space) I form a (stable by ﬁnite intersection) factorizing basis denoted I .
An example of stratiﬁed locally constant factorization algebra on I is obtained
as follows. Let A be a differential graded associative unital algebra, Mr a pointed
differential graded right A-module (with distinguished element denoted mr ∈Mr)
and Mℓa pointed differential graded left A-module (with distinguished element
mℓ∈Mℓ). We deﬁne a I -prefactorization algebra by setting, for any interval
J ∈I
F(J) :=





Mr if 0 ∈J
Mℓif 1 ∈J
A else.
We deﬁne its structure maps to be given by the following51:
• F(/0) →F([0,s)) is given by k ∋1 7→mr, F(/0) →F((t,s)) is given by
1 7→1A and F(/0) →F((t,1])) is given by k ∋1 7→mℓ;
• For 0 < s < t1 < u1 < ··· < ti < ui < v < 1 one sets
Mr ⊗A⊗i = F([0,s))⊗F((t1,u1))⊗···⊗F((ti,ui))
−→
F([0,v)) = Mr
m⊗a1 ⊗···⊗ai
7−→
m·a1 ···ai ;
A⊗i ⊗Mℓ= F((t1,u1))⊗···⊗F((ti,ui))⊗F((v,1])
−→
F((s,1]) = Mℓ
a1 ⊗···⊗ai ⊗n
7−→
a1 ···ai ·n;
50note that this stratiﬁcation is just given by looking at [0,1] as a manifold with boundary
51as in Example 27, we use the implicit orientation of I given by increasing numbers
56


## Page 57


and also
A⊗i = F((t1,u1))⊗···⊗F((ti,ui))
−→
F((s,v)) = A
a1 ⊗···⊗ai
7−→
a1 ···ai .
It is straightforward to check that F is a I -prefactorization algebra and, by deﬁ-
nition, it satisﬁes the locally constant condition.
Proposition 27 shows that F is indeed a locally constant factorization algebra
on the closed interval I. Further, any locally constant factorization algebra on I is
(homotopy) equivalent to such a factorization algebra.
Also note that the I -prefactorization algebra induced by F on the open in-
terval (0,1) is precisely the I -prefactorization algebra constructed in Example 27
(up to an identiﬁcation of (0,1) with R). We denote it FA.
Proposition 27. Let F, FA be deﬁned as above.
1. The I - prefactorization algebra F is an I -factorization algebra hence ex-
tends uniquely into a factorization algebra (still denoted) F on the stratiﬁed
closed interval I = [0,1];
2. in particular, FA also extends uniquely into a factorization algebra (still
denoted) FA on (0,1).
3. There is an equivalence
R
[0,1] F = F([0,1]) ∼= Mr L⊗
A Mℓin Chain(k).
4. Moreover, any locally constant factorization algebra G on I = [0,1] is equiv-
alent52 to F for some A,Mℓ,Mr, that is, it is uniquely determined by an
E1-algebra A and pointed left module M ℓand pointed right module M r
satisfying
G ([0,1)) ∼= M r,
G ((0,1]) ∼= M ℓ,
G ((0,1)) ∼= A
with structure maps given by the E1-structure similarly to those of F.
For a proof, see § 9.2. The last statement restricted to the open interval (0,1) is
just Theorem 9 (in the case n = 1).
Example 33. We consider the closed half-line [0,+∞) as a stratiﬁed manifold, with
strata {0} ⊂[0,+∞) given by its boundary. Namely, it has a 0-dimensional strata
given by {0} and thus one dimension 1 strata (0,+∞). Similarly, there is a stratiﬁed
closed half-line (−∞,0]. From Proposition 27 (and its proof) we also deduce
52more precisely, taking A, Mℓ, Mr be strictiﬁcation of A , M ℓand M r, there is a quasi-
isomorphism of factorization algebras from F (associated to A,Mℓ,Mr) to G .
57


## Page 58


Proposition 28. There is an equivalence of ∞-categories between locally constant
factorization algebra on the closed half-line [0,+∞) and the category E1-RMod of
(pointed) right modules over E1-algebras53. This equivalence sits in a commutative
diagram
Faclc
[0,+∞)
∼=
/

E1-RMod

Faclc
(0,+∞)
∼=
/ E1-Alg
where the left vertical functor is given by restriction to the open line and the lower
horizontal functor is given by Theorem 9.
There is a similar equivalence (and diagram) of ∞-categories between locally
constant factorization algebra on the closed half-line (−∞,0] and the category
E1-LMod of (pointed) left modules over E1-algebras.
Let X be a manifold and consider the stratiﬁed manifold X × [0,+∞), with a
dim(X) open strata X ×{0}. Using Corollary 6 and Proposition 28 one can get
Corollary 7. The pushforward along the projection X ×[0,+∞) →[0,+∞) induces
an equivalence
Faclc
X×[0,+∞)
≃
−→E1-RMod(Faclc
X ).
6.3
Factorization algebras on pointed disk and En-modules
In this section we relate En-modules54 and factorization algebras over the pointed
disk.
Let Rn
∗denote the pointed disk which we see as a stratiﬁed manifold with one
0-dimensional strata given by the point 0 ∈Rn and n-dimensional strata given by
the complement Rn \{0}.
Deﬁnition 22. We denote Faclc
Rn∗the ∞-category of locally constant factorization
algebras on the pointed disk Rn
∗(in the sense of Deﬁnition 21).
Recall the functor (33) giving the obvious embedding Faclc
Rn −→Faclc
Rn∗.
Locally constant factorization algebras on Rn
∗are related to those on the closed
half-line (§ 6.2) as follows: let N : Rn →[0,+∞) be the euclidean norm map x 7→
∥x∥. We have the pushforwards N∗: FacRn∗→Fac[0,+∞) and (−N)∗: FacRn∗→
Fac(−∞,0].
Lemma 7. If F ∈Faclc
Rn∗, then N∗(F) ∈Faclc
[0,+∞) and (−N)∗(F) ∈Faclc
(−∞,0].
53which, informally, is the category of pairs (A,Mr) where A is an E1-algebra and Mr a (pointed)
right A-module
54according to our convention in Appendix 10.2, all En-modules are pointed by deﬁnition
58


## Page 59


Proof. For 0 < ε < η, the structure map N∗(F)
 [0,ε)
 ∼= F
 N−1([0,ε))

→
F
 N−1([0,η))
 ∼= N∗(F)
 [0,η)

is an equivalence since F is locally constant
and N−1([0,α) is a euclidean disk centered at 0.
Further, by Proposition 15,
N∗(F|Rn\{0}) is locally constant from which we deduce that N∗(F) is locally con-
stant on the stratiﬁed half-line [0,+∞). The case of (−N)∗is the same.
Our next task is to deﬁne a functor En-Mod →Faclc
Rn∗from (pointed) En-
modules (see § 10.2) to (locally constant) factorization algebras on the pointed
disk. It is enough to associate (functorially), to any M ∈En-Mod, a C V (Rn)-
factorization algebra FM where C V (Rn) is the (stable by ﬁnite intersection) fac-
torizing basis of Rn of convex open subsets. It turns out to be easy: since any con-
vex subset C is canonically an embedded framed disk, we can set FM(C) := M(C).
In other words, we assign the module to a convex neighborhood of 0 and the alge-
bra to a convex neigborhood which does not contain the origin.
Then set the structure maps FM(C1) ⊗··· ⊗FM(Ci) →FM(D), for any pair-
wise disjoint convex subsetsCk of D, to be given by the map M(C1)⊗···⊗M(Ci) →
M(D) associated to the framed embedding `
k=1...i Rn ∼=
S
k=1...iCk ,→D ,→Rn.
Theorem 12. The rule M 7→FM induces a fully faithful functor ψ : En-Mod →
Faclc
Rn∗which ﬁts in a commutative diagram
En-Alg
≃
/
can

Faclc
Rn

En-Mod
ψ
/ Faclc
Rn∗.
Here can : En-Alg →En-Mod is given by the canonical module structure of an
algebra over itself.
We will now identify En-modules in terms of factorization algebras on Rn
∗;
that is the essential image of the functor ψ : En-Mod →Faclc
Rn∗given by Theo-
rem 12. Recall the functor πEn : En-Mod →En-Alg ∼= Faclc
Rn which, to a module
M ∈En-ModA, associates πEn(M) = A.
By restriction to the open set Rn \ {0} we get that the two compositions of
functors
En-Mod
ψ
−→Faclc
Rn∗→Faclc
Rn\{0} and En-Mod
πEn
−→En-Alg ∼= Faclc
Rn →Faclc
Rn\{0}
are equivalent. Hence, we get a factorization of (ψ,πEn) to the pullback
(ψ,πEn) : En-Mod −→Faclc
Rn∗×h
Faclc
Rn\{0} Faclc
Rn.
Informally, Faclc
Rn∗×h
Faclc
Rn\{0} Faclc
Rn is simply the (∞-)category of pairs (A ,M ) ∈
Faclc
Rn ×Faclc
Rn∗together with a quasi-isomorphism f : A|Rn\{0} →M|Rn\{0} of fac-
torization algebras.
59


## Page 60


Corollary 8. The functor En-Mod
(ψ,πEn)
−→Faclc
Rn∗×h
Faclc
Rn\{0} Faclc
Rn is an equivalence.
Now, if A is an En-algebra, we can see it as a factorization algebra on Rn
(Theorem 9) and taking the (homotopy) ﬁber at {A} of the right hand side of the
equivalence in Corollary 8, we get
Corollary 9. The functor En-ModA
ψ
−→Faclc
Rn∗×h
Faclc
Rn\{0} {A} is an equivalence.
Example 34 (Locally constant factorization algebra on the pointed line R∗). The
case of the pointed line R∗is slightly special since it has two (and not one) strata of
maximal dimension. The two embeddings j+ : (0,+∞) ,→R and j−: (−∞,0) ,→R
yields two restrictions functors: j∗
± : Faclc
R∗→Faclc
R. Hence F ∈Faclc
R∗determines
two E1-algebras R ∼= F
 (0,+∞)

and L ∼= F
 (−∞,0)

.
By Lemma 7, the pushforward (−N)∗: Faclc
R∗→Faclc
(−∞,0] along −N : x 7→−|x|
is well deﬁned. Then Proposition 28 implies that (−N)∗(F) is determined by a
left module M over the E1-algebra A ∼= (−N)∗(F)
 (0,+∞)
 ∼= L ⊗Rop, i.e. by a
(L,R)-bimodule.
We thus have a functor (j∗
±,(−N)∗) : Faclc
R∗→BiMod where BiMod is the
∞-category of bimodules (in Chain(k)) deﬁned in [L3, §4.3] (i.e. the ∞-category
of triples (L,R,M) where L, R are E1-algebras and M is a (L,R)-bimodule).
Proposition 29. The functor (j∗
±,(−N)∗) : Faclc
R∗∼= BiMod is an equivalence.
Example 35 (From pointed disk to the n-dimensional annulus: Sn−1 ×R). Let M
be a locally constant factorization algebra on the pointed disk Rn
∗. By the previous
results in this Section (speciﬁcally Lemma 7 and Proposition 28), for any A ∈
Faclc
Sn−1×R, the pushforward along the euclidean norm N : Rn →[0,+∞) factors as
a functor
N∗: Faclc
Rn∗×Faclc
Rn\{0} {A } −→E1-RModA (Sn−1×R)
from the category of locally constant factorization algebras on the pointed disk
whose restriction to Rn \ {0} is (quasi-isomorphic to) A to the category of right
modules over the E1-algebra55 A (Sn−1 ×R) ∼=
R
Sn−1×R A . Similarly, we have the
functor (−N)∗: Faclc
Rn∗×Faclc
Rn\{0} {A } −→E1-LModA (Sn−1×R).
Proposition 30. Let A be in Faclc
Sn−1×R.
• The functor N∗: Faclc
Rn∗×Faclc
Rn\{0} {A } −→E1-RModA (Sn−1×R) is an equiva-
lence of ∞-categories.
• (−N)∗: Faclc
Rn∗×Faclc
Rn\{0} {A } −→E1-LModA (Sn−1×R) is an equivalence.
55the E1-structure is given by Lemma 5
60


## Page 61


See § 9.3 for a Proof.
The Proposition allows to reduce a category of“modules” over A to a category
of modules over an (homotopy) dg-associative algebra.
We will see in section 7.1 that it essentially gives a concrete description of the
enveloping algebra of an En-algebra.
6.4
More examples
We now give, without going into any details, a few more examples of locally con-
stant factorization algebras on stratiﬁed spaces which can be studied along the same
way as we did previously.
Example 36 (towards quantum mechanics). One can make the following variant of
the interval example of Proposition 27 (see [CG] for details). Fix a one parameter
group (αt)t∈[0,1] of invertible elements in an associative (topological) algebra A.
Now, we deﬁne a factorization algebra on the basis I of open disks of [0,1] in the
same way as in Proposition 27 except that we add the element αd to any hole of
length d between two intervals (corresponding to the inclusion of the empty set:
F(/0) →F(I) into any open interval). Precisely, we set:
• the structure map k = F(/0) →F
 s,t)

= A is given by the element αt−s,
the structure map k = F(/0) →F

0,t)

= Mr mr ·αt and the structure map
k = F(/0) →F
 u,1]

= Mℓα1−u ·mℓ.
• For 0 < s < t1 < u1 < ··· < ti < ui < v < 1 one sets the map
Mr ⊗A⊗i = F([0,s))⊗F((t1,u1))⊗···F((ti,ui)) −→F([0,v)) = Mr
to be given by
m⊗a1 ⊗···⊗ai 7−→m·αt1−sa1αt2−u1a2 ···αti−ui−1aiαv−ui,
the map
A⊗i ⊗Mℓ= F((t1,u1))⊗···F((ti,ui))⊗F((v,1]) −→F((s,1]) = Mℓ
to be given by a1 ⊗···⊗ai ⊗n 7−→αt1−sa1αt2−u1a2 ···αti−ui−1aiαv−uin, and
also the map A⊗i = F((t1,u1)) ⊗··· ⊗F((ti,ui)) −→F((s,v)) = A to be
given by
a1 ⊗···⊗ai 7−→αt1−sa1αt2−u1a2 ···αti−ui−1aiαv−ui.
One can check that these structure maps deﬁne a I -factorization algebra and thus
a factorization algebra on I.
One can replace chain complexes with topological C-vector spaces (with monoidal
structure the completed tensor product) and take V to be an Hilbert space. Then
one can choose A = (Endcont(V))op and Mr = V = Mℓwhere the left A-module
61


## Page 62


structure on Mℓis given by the action of adjoint operators. Let αt := eitϕ where
ϕ ∈Endcont(V). One has F([0,1]) = C. One can think of A as the algebra of
observables where V is the space of states and eitϕ is the time evolution operator.
Now, given two consecutives measures O1,O2 made during the time intervals ]s,t[
and ]u,v[ (0 < s < t < u < v < 1), the probability amplitude that the system goes
from an initial state vr to a ﬁnal state vℓis the image of O1 ⊗O2 under the structure
map
A⊗A = F(]s,t[)⊗F(]u,v[) −→F([0,1]) = C,
and is usually denoted ⟨vℓ|ei(1−v)ϕO2ei(u−t)ϕO1eisϕ|vr⟩.
Example 37 (the upper half-plane). Let H = {z = x+iy ∈C,y ≥0} be the closed
upper half-plane, viewed as a stratiﬁed space with H0 = /0, H1 = R the real line
as dimension 1 strata and H2 = H. The orthogonal projection π : H →R onto the
imaginary axis Ri ⊂C induces, by Proposition 6 (and Proposition 28), an equiva-
lence
Faclc
H
≃
−→Faclc
[0,+∞)(Faclc
R) ∼= E1-RMod(E1-Alg).
Using Dunn Theorem 11, we have (sketched a proof of the fact) that
Proposition 31. The ∞-category of stratiﬁed locally constant factorization algebra
on H is equivalent to the ∞-category of algebras over the swiss cheese operad, that
is the ∞-category consisting of triples (A,B,ρ) where A is an E2-algebra, B an
E1-algebra and ρ : A →RHomE1
B (B,B) is an action of A on B compatible with all
the multiplications56.
One can also consider another stratiﬁcation ˜H on R×[0,+∞) given by adding
a 0-dimensional strata to H, given by the point 0 ∈C. There is now 4 kinds of
(stratiﬁed) disks in ˜H: the half-disk containing 0, the half disk with a connected
boundary component lying on (−∞,0), the half-disk containing 0, the half disk
with a connected boundary component lying on (0,+∞) and the open disks in the
interior {x+iy, y > 0} of H.
One proves similarly
Proposition 32. Locally constant factorization algebras on the stratiﬁed space ˜H
are the same as the category given by quadruples (M,A,B,ρA,ρB,E) where E is
an E2-algebra, (A,ρA), (B,ρB) are E1-algebras together with a compatible action
of E and (M,ρM) is a (A,B)-bimodule together with a compatible action57 of E.
Examples of such factorization algebras occur in deformation quantization in
the presence of two branes, see [CFFR].
Note that the norm is again adequatly stratiﬁed so that, if F ∈Faclc
˜H, then
(−N)∗(F) ∈Faclc (−∞,0]
 ∼= E1-LMod. Using the argument of Proposition 30
56that is the map ρ is a map of E2-algebras where RHomE1
B (B,B) is the E2-algebra given by the
(derived) center of B. In particular, ρ induces a map ρ(1B) : A →B
57precisely, this means the choice of a factorization A ⊗Bop −→A
L⊗
E Bop ρM
−→RHom(M,M) (in
E1-Alg) of the (A,B)-bimodule structure of M
62


## Page 63


and Proposition 27, we see that if F is given by a tuple (M,A,B,ρA,ρB,E), then the
underlying E1-algebra of (−N)∗(F) is (the two-sided Bar construction) A
L⊗
E Bop.
Example 38 (the unit disk in C). Let D = {z ∈C, |z| ≤1} be the closed unit disk
(with dimension 1 strata given by its boundary). By Lemma 7, the norm gives us a
pushforward functor N∗: Faclc
D →Faclc
[0,1]. A proof similar to the one of Corollary 7
and Theorem 12 shows that the two restrictions of N∗to D\∂D and D\{0} induces
an equivalence
Faclc
D
≃
−→Faclc
D\∂D ×h
Faclc
(0,1) E1-RMod
 Faclc
S1

.
By Corollary 4 and Theorem 9, one obtains:
Proposition 33. The ∞-category of locally constant factorization algebra on the
(stratiﬁed) closed unit disk D is equivalent to the ∞-category consisting of quadru-
ples (A,B,ρ, f) where A is an E2-algebra, B an E1-algebra, ρ : A : RHomE1-Alg(B,B)
is an action of A on B compatible with all the multiplications and f : B →B is a
monodromy compatible with ρ.
One can also consider a variant of this construction with dimension 0 strata
given by the center of the disk. In that case, one has to add a E2-A-module to the
data in Proposition 33.
Example 39 (the closed unit disk in Rn). Let Dn be the closed unit disk of Rn which
is stratiﬁed with a single strata of dimension n −1 given by its boundary ∂Dn =
Sn−1. We have restriction functors Faclc
Dn −→Faclc
Dn\∂Dn ∼= En-Alg (Theorem 9),
En-Alg ∼= Faclc
Dn\∂Dn →Faclc
Sn−1×(0,1) ∼= E1-Alg(Faclc
Sn−1)
(by Proposition 18)
and Faclc
Dn −→Faclc
Dn\{0}. From Corollary 7, we deduce
Proposition 34. The above restriction functors induce an equivalence
Faclc
Dn
≃
−→En-Alg×E1-Alg
 Faclc
Sn−1
 E1-LMod
 Faclc
Sn−1

.
Let f : A →B be an En-algebra map. Since Sn−1 ×R has a canonical framing,
both A and B carries a structure of locally constant factorization algebra on Sn−1,
which is induced by pushforward along the projection q : Sn−1×R →Sn−1 (see Ex-
ample 26). Further, B inherits an En-module structure over A induced by f and, by
restriction, q∗(B|Sn−1×R) is an E1-module over q∗(A|Sn−1×R). Thus, Proposition 34
yields a factorization algebra ωDn(A
f→B) ∈Faclc
Dn.
Proposition 35. The map ωDn induces a faithful functor ωDn : HomEn-Alg −→Faclc
Dn
where HomEn-Alg is the ∞-groupoid of En-algebras maps.
63


## Page 64


By the relative higher Deligne conjecture (Theorem 16), we also have the En-
algebra HHEn(A,B f ) and an En-algebra map HHEn(A,B f ) →B given as the com-
position
HHEn(A,B f ) ∼= z(f)
id⊗1A
−→z(f)⊗z(k
1A
→A) −→z(k
1B
→B) ∼= B.
Thus by Proposition 35, the pair (HHEn(A,B f ),B) also deﬁnes a factorization al-
gebra on Dn.
Let τ : Dn →Rn ∪{∞} be the map collapsing ∂Dn to the point ∞. It is an
adequatly stratiﬁed map if we see Rn ∪{∞} as being stratiﬁed with one dimension
0 strata given by ∞. Denote c
Rn this stratiﬁed manifold. The composition of τ∗with
ωDn gives us:
Corollary 10. There is a faithful functor bω : HomEn-Alg −→Faclc
c
Rn.
Example 40 (The Square). Consider the square I2 := [0,1]2, the product of the
interval (with its natural stratiﬁcation of § 6.2) with itself. This stratiﬁcation agrees
with the one given by seeing I2 as a manifold with corners. Thus, there are four 0-
dimensional strata corresponding to the vertices of I2 and four 1-dimensional strata
corresponding to the edges. Let us denote {1,2,3,4} the set of vertices and [i,i+1]
the corresponding edge linking the vertices i and i + 1 (ordered cyclically58). See
Figure 3.
We can construct a factorization algebra on I2 as follows. For every edge [i, j]
of I2, let A[i,j] be an E1-algebra; also let A be an E2-algebra. For every vertex i, let
Mi be a (A[i−1,i],A[i,i+1])-bimodule. Finally, assume that A acts on each A[i,j] and
Mk in a compatible way with algebras and module structures. Compatible, here,
means that for every vertex i, the data (Mi,A[i−1,i],A[i,i+1],A) (together with the
various module structures) deﬁne a locally constant stratiﬁed factorization algebra
on a neighborhood59 of the vertex i as given by Proposition 32.
Using Propositions 27 and 29 (and their proofs) and Remark 23, we see that
we obtain a locally constant factorization algebra I on I2 whose value on an open
rectangle R ⊂I2 is given by
I (R) :=



Mi
if R is a good neighborhood at the vertex i;
A[i,i+1]
if R is a good neighborhood at the edge [i,i+1];
A
if R lies in I2 \∂I2.
(34)
The structure maps being given by the various module and algebras structure60.
By Corollary 6, we get the functor π1∗: Faclc
[0,1]2 →Faclc
[0,1](Faclc
[0,1]). Com-
bining the proof of Proposition 18 and Proposition 27 (similarly to the proof of
Corollary 7), we get:
58in other words we have the 4 edges [1,2], [2,3], [3,4] and [4,1]
59for instance, take the complement of the closed sub-triangle of I2 given by the three other
vertices, which is isomorphic as a stratiﬁed space to the pointed half plane ˜H of Example 37
60note that we orient the edges accordingly to the ordering of the edges
64


## Page 65


Proposition 36. The functor π1∗: Faclc
[0,1]2 →Faclc
[0,1](Faclc
[0,1]) is an equivalence of
∞-categories.
Moreover, any stratiﬁed locally constant factorization algebra on I2 is quasi-
isomorphic to a factorization algebra associated to a tuple (A,A[i,i+1],Mi,i = 1...4)
as in the rule (34) above.
Let us give some examples of computations of the global sections of I on
various opens.
• The band I2 \ ([4,1] ∪[2,3]) is isomorphic (as a stratiﬁed space) to (0,1) ×
[0,1].
Then from the deﬁnition of factorization homology and Proposi-
tion 27.3, we get
I
 I2 \([4,1]∪[2,3])

∼=
p∗
 I|I2\([4,1]∪[2,3])
 ∼= p∗(π1∗(I|I2\([4,1]∪[2,3]))
=
Z
[0,1] π1∗(I|I2\([4,1]∪[2,3]) ∼= A[1,2]
L⊗
A (A[3,4])op.
In view of Corollary 7 in the case X = R (and Theorem 9); this is an equiva-
lence of E1-algebras.
• Consider a tubular neighborhood of the boundary, namely the complement61
T := I2 \ [1/4,3/4]2 (see Figure 3). The argument of Proposition 27 and
Example 15 shows (by projecting the square on [0,1]×{1/2}) that
I
 T
 ∼=

M4
L⊗
A[4,1]
M1

L
O
A[1,2]⊗(A[3,4])op

M2
L⊗
A[2,3]
M3

.
• Now, consider a diagonal band, say a tubular neigborhood D13 of the diago-
nal linking the vertex 1 to the vertex 3 (see Figure 3). Then projecting onto
the diagonal [1,3] and using again Proposition 27, we ﬁnd,
I
 D13) ∼= M1
L⊗
A M3.
M1
M2
M3
M4
A[4,1]
A[1,2]
A[2,3]
A[3,4]
A
Figure 3:
The stratiﬁcation of the
square. The (oriented) edges and ver-
tices are decorated with their associated
algebras and modules. Also 4 rectan-
gles which are good neighborhoods at
respectively 1, [4,1], [1,2] and the di-
mension 2-strata are depicted in blue.
The band D13 is delimited by the dotted
lines while the annulus T is the comple-
ment of the interior blue square.
61note that the obvious radial projection T →∂I2 is not adequatly stratiﬁed
65


## Page 66


Iterating the above constructions to higher dimensional cubes, one ﬁnds
Proposition 37. Let [0,1]n be the stratiﬁed cube. The pushforward along the canon-
ical projections is an equivalence Faclc
[0,1]n
≃→Faclc
[0,1]
 ···(Faclc
[0,1])···

.
In other words, Faclc
[0,1]n is a tractable model for an ∞-category consisting of
the data of an En-algebra An together with En−1-algebras An−1,in−1 (in−1 = 1...2n)
equipped with an action of An, En−2-algebras An2,in−2 (in−2 = 1...2n(n −1)) each
equipped with a structure of bimodule over 2 of the An−1,j compatible with the A
actions, . . . , Ek-algebras Ak,ik (ik = 1...2n−k n
k

) equipped with structure of n−k-
fold modules over (n−k many of) the Ak+1,j algebras, compatible with the previous
actions, and so on . . . .
Similarly to the previous example 39, we also have a faithful functor
En-Alg ∼= Faclc
Rn −→Faclc
[0,1]n.
Example 41 (Iterated categories of (bi)modules). We consider the n-fold product
(R∗)n of the pointed line (see Example 34) with its induced stratiﬁcation. It has
one 0-dimensional strata given by the origins, 2n many 1-dimensional strata given
by half of the coordinate axis, . .., and 2n open strata.
Locally constant (stratiﬁed) factorization algebras on (R∗)n are a model for iter-
ated categories of bimodules objects. Indeed, by Corollary 6, the iterated ﬁrst pro-
jections on R∗yields a functor π∗: Faclc
(R∗)n −→Faclc
R∗

Faclc
R∗
 ...(Faclc
R∗)...

.
From Proposition 29 (and its proof) combined with the arguments of the proofs of
Corollary 7 and Proposition 30, we get
Corollary 11. The functor
π∗: Faclc
(R∗)n −→Faclc
R∗

Faclc
R∗
 ...(Faclc
R∗)...

∼= BiMod

BiMod
 ...(BiMod)...

is an equivalence.
An interesting consequence arise if we assume that the restriction to Rn \ {0}
of F ∈Faclc
(R∗)n is constant, that is in the essential image of the functor Faclc
Rn →
Faclc
(R∗)n. In that case, F belongs to the essential image of Faclc
Rn∗→Faclc
(R∗)n. Thus
Corollary 9 and Corollary 11 imply
Corollary 12. There is a natural equivalence
En-Mod ∼= E1-Mod

E1-Mod
 ...(E1-Mod)...

inducing an equivalence
En-ModA ∼= E1-ModA

E1-ModA
 ...(E1-ModA)...

66


## Page 67


between the relevant ∞-subcategories62.
Let us describe now informally Faclc
(R∗)2. A basis of (stratiﬁed) disks is given
by the convex open subsets. Such a subset is a good disk of index 0 if it is a neig-
borhood of the origin, of index 1 if it is in R2 \{0} and intersects one and only one
half open coordinate axis. It is a good disk of index 2 if it lies in the complement of
the coordinate axis. We can construct a factorization algebra on (R∗)2 as follows.
Let Ei, i = 1...4 be four E2-algebras (labelled by the cyclically ordered four quad-
rants of R2). Let A1,2, A2,3, A3,4 and A4,1 be four E1-algebras endowed, for each
i ∈Z/4Z, with a compatible (Ei,Ei+1)-bimodule structure63 on Ai,i+1. Also let M
be a E2-module over each Ei in a compatible way. Precisely, this means that M is
endowed with a right action64 of the E1-algebra
 A4,1
L⊗
E1
A1,2

L
N
E2⊗(E4)op
 A2,3
L⊗
E3
A3,4

.
Similarly to previous examples (in particular example 40), we see that we ob-
tain a locally constant factorization algebra M on (R∗)2 whose value on an open
rectangle is given by
M (R) :=







M
if R is a good neighborhood of the origin;
Ai,i+1
if R is a good neighborhood of index 1
intersecting the quadrant labelled i and i+1;
Ei
if R lies in the interior of the ith-quadrant.
(35)
The structure maps are given by the various module and algebras structures. As in
example 40, we get
Proposition 38. Any stratiﬁed locally constant factorization algebra on (R∗)2 is
quasi-isomorphic to a factorization algebra associated to a tuple (M,Ai,i+1,Ei,i =
1...4) as in the rule (35) above.
Example 42 (Butterﬂy). Let us give one of the most simple singular stratiﬁed ex-
ample. Consider the “(semi-open) butterﬂy” that is the subspace B := {(x,y) ∈
R2||y| < |x|}∪{(0,0)} of R2 . B has a dimension 0 strata given by the origin and
two open strata B+, B−of dimension 2 given respectively by restricting to those
points (x,y) ∈B such that x > 0, resp. x < 0.
The restriction to B+ of a stratiﬁed locally constant factorization algebra on
B is locally constant factorization over B+ ∼= R2 (hence is determined by an E2-
algebra). This way, we get the restriction functor res∗: Faclc
B →Faclc
R2 ×Faclc
R2.
Let π : R2 →R be the projection (x,y) 7→x on the ﬁrst coordinate. Then, by
Corollary 6, we get a functor π∗: Faclc
B →Faclc
R∗where R∗is the pointed line
(example 34). The restriction of π∗to B+ ∪B−thus yields a the functor Faclc
R2 ×
Faclc
R2 →Faclc
R\{0}.
62the A-E1-module structure on the right hand side are taken along the various underlying E1-
structures of A obtained by projecting on the various component R of Rn
63that is a map of E2-algebras Ei ⊗(Ei+1)op →RHomE1
Ai,i+1(Ai,i+1,Ai,i+1)
64In particular, it implies that the tuple (M,Ai−1,i,Ai,i+1,Ei) deﬁnes a stratiﬁed locally constant
factorization algebra on ˜H by Proposition 32
67


## Page 68


A proof similar (and slightly easier) to the one of Proposition 45 shows that the
induced functor
(π∗,res∗) : Faclc
B −→Faclc
R∗×h
Faclc
R\{0} (Faclc
R2 ×Faclc
R2)
is an equivalence. From Proposition 29, we then deduce
Proposition 39. There is an equivalence
Faclc
B ∼= BiMod×h
(E1-Alg×E1-Alg)
 E2-Alg×E2-Alg

.
In other words, locally constant factorization algebras on the (semi-open) butterﬂy
are equivalent to the ∞-category of triples (A,B,M) where A, B are E2-algebras
and M is a left A⊗Bop-module (for the underlying E1-algebras structures of A and
B).
Let B = {(x,y) ∈R2||y| ≤|x|} be the closure of the butterﬂy. It has four addi-
tional dimension 1 strata, given by the boundary of B+ and B−. The above argu-
ment yields an equivalence
Faclc
B
≃
−→Faclc
R∗×h
Faclc
R\{0}
 Faclc
˜H ×Faclc
˜H

where ˜H is the pointed half-plane, see example 37. From Propositions 32, 27
and 29 we see that a locally constant factorization algebra on the closed butterﬂy B
is equivalent to the data of two E2-algebras E+, E−, four E1-algebras A+, B+, A−,
B−, equipped respectively with left or right modules structures over E+ or E−, and
a left
 A+ ⊗L
E+ B+

⊗
 A−⊗L
E−B−
op-module M.
Example 43 (Homotopy calculus). The canonical action of S1 = SO(2) on R2 has
the origin for ﬁxed point. It follows that S1 acts canonically on FacR2∗, the cate-
gory of factorization algebras over the pointed disk. If F ∈Faclc
R2∗, its restriction
to R2 \{0} determines an E2-algebra A with monodromy by Corollary 4, Proposi-
tion 18 and Theorem 11. If F is S1-equivariant, then its monodromy is trivial and
it follows that the global section F(R2) is an E2-module over A. The S1-action
yields an S1-action on F(R2) which, algebraically, boils down to an additional
differential of homological degree 1 on F(R2). We believe that the techniques in
this section suitably extended to the case of compact group actions on factorization
algebras allow to prove
Claim.
The category
 Faclc
R2∗
S1
of S1-equivariant locally constant factorization
algebras on the pointed disk R2
∗is equivalent to the category of homotopy calculus
of Tamarkin-Tsygan [TT] describing homotopy Gerstenhaber algebras acting on a
BV-module.
There are nice examples of homotopy calculus arising in algebraic geome-
try [BF].
68


## Page 69


Example 44. Let K : S1 →R3 be a knot, that is a smooth embedding of S1 inside
R3. Then we can consider the stratiﬁed manifold R3
K with a 1 dimensional open
strata given by the image of K, and another 3-dimensional open strata given by the
knot complement R3 \ K(S1). Then the category of locally constant factorization
algebra on R3
K is equivalent to the category of quadruples (A,B, f,ρ) where A is an
E3-algebras, B is an E1-algebra, f : B →B is a monodromy and ρ : A⊗B →B is an
action of A onto B (compatible with all the structures (that is making B an object of
E2-ModA(E1-Alg). We refer to [AFT] and [Ta] for details on the invariant of knots
produced this way.
7
Applications of factorization algebras and homology
7.1
Enveloping algebras of En-algebras and Hochschild cohomology
of En-algebras
In this section we describe the universal enveloping algebra of an En-algebra in
terms of factorization algebras, and apply it to describe En-Hochschild cohomol-
ogy.
Given an En-algebra A, we get a factorization algebra on Rn and thus on its
submanifold Sn−1 ×R (equipped with the induced framing); see Example 19. We
can use the results of § 6 to study the category of En-modules over A.
In particular, from Corollary 8, and Proposition 30, we obtain the following
corollary which was ﬁrst proved by J. Francis [F1].
Corollary 13. Let A be an En-algebra. The functor N∗: En-ModA →E1-RModR
Sn−1×R A
is an equivalence.
Similarly, the functor (−N)∗: En-ModA →E1-LModR
Sn−1×R A is an equivalence.
We call
R
Sn−1×R A the universal (E1-)enveloping algebra of the En-algebra A.
A virtue of Corollary 13 is that it reduces the homological algebra aspects in
the category of En-modules to standard homological algebra in the category of
modules over a differential graded algebra (given by any strict model of
R
Sn−1×R A).
Remark 29. Corollary 8 remains true for n = ∞(and follows from the above study,
see [GTZ3]), in which case, since S∞is contractible, it boils down to the following
result:
Proposition 40 ([L3], [KM]). Let A be an E∞-algebra. There is an natural equiv-
alence of ∞-categories E∞-ModA ∼= E1-RModA (where in the right hand side, A is
identiﬁed with its underlying E1-algebra).
Example 45. Let A be a smooth commutative algebra (or the sheaf of functions of
a smooth scheme or manifold) viewed as an En-algebra. Then, by Theorem 3 and
Theorem 10, we have
69


## Page 70


Proposition 41. For n ≥2, there is an equivalence
En-ModA ∼= E1-RModS•
A(Ω1
A[n−1]).
The right hand side is just a category of modules over a graded commutative
algebra. If A = OX, then one thus has an equivalence between En-ModOX and right
graded modules over OTX[1−n], the functions on the graded tangent space of X.
Example 46. Let A be an En-algebra. It is canonically a En-module over itself; thus
by Corollary 13 it has a structure of right module over
R
Sn−1×R A. The later has
an easy geometrict description. Indeed, by the dimension axiom, A ∼=
R
Rn A. The
euclidean norm gives the trivialization Sn−1 ×(0,+∞) of the end(s) of Rn so that,
by Lemma 5,
R
Rn A has a canonical structure of right module over
R
Sn−1×(0,+∞) A.
Let us consider the example of an n-fold loop space. Let Y be an n-connective
pointed space (n ≥0) and let A = C∗(Ωn(Y)) be the associated En-algebra. By
non-abelian Poincar´e duality (Theorem 7) we have an equivalence
Z
Sn−1×R A ∼= C∗
 Mapc(Sn−1 ×R,Y)
 ∼= C∗

Ω

Y Sn−1
.
By Corollary 13 we get
Corollary 14. The category of En-modules over C∗(Ωn(Y)) is equivalent to the
category of right modules over C∗

Ω

Y Sn−1
.
The algebra C∗

Ω

Y Sn−1
in Corollary 14 is computed by the cobar construc-
tion of the differential graded coalgebra C∗
 Map(Sn−1,Y)

. If Y is of ﬁnite type,
n −1-connected and the ground ring k is a ﬁeld of characteristic zero, the latter
is the linear dual of the commutative differential graded algebra CHSn−1(Ω∗
dR(Y))
where Ω∗
dR(Y) is (by Theorem 5) the differential graded algebra of Sullivan poly-
nomial forms on Y. In that case, the structure can be computed using rational
homotopy techniques.
Example 47. Assume Y = S2m+1, with 2m ≥n. Then, Y has a Sullivan model
given by the CDGA S(y), with |y| = 2m + 1. By Theorem 3 and Theorem 5,
C∗(Map(Sn−1,S2m+1)) is equivalent to the cofree cocommutative coalgebra S(u,v)
with |u| = −1−2m and |v| = n−2m−2. By Corollary 14 and Corollary 19 we ﬁnd
that the category of En-modules over C∗(Ωn(S2m+1) is equivalent to the category of
right modules over the graded commutative algebra S(a,b) where |u| = −2m −2
and |v| = n−2m−3.
There is an natural notion of cohomology for En-algebras which generalizes
Hochschild cohomology of associative algebras. It plays the same role with respect
to deformations of En-algebras as Hochschild cohomology plays with respect to
deformations of associatives algebras.
70


## Page 71


Deﬁnition 23. Let M be an En-module over an En-algebra A. The En-Hochschild
cohomology65 of A with values in M, denoted by HHEn(A,M), is by deﬁnition
(see [F1]) RHomEn
A (A,M) (Deﬁnition 35).
Corollary 15. Let A be an En-algebra, and M, N be En-modules over A.
1. There is a canonical equivalence
RHomEn
A (M,N) ∼= RHomleft
R
Sn−1×R A(M,N)
where the right hand side are homomorphisms of left modules (Deﬁnition 36).
2. In particular HHEn(A,M) ∼= RHomleft
R
Sn−1×R A(A,M).
3. If A is a CDGA (or E∞-algebra) and M is a left module over A, then
HHEn(A,M) ∼= RHomEn
A (A,M) ∼= CHSn(A,M).
Proof. The ﬁrst two points follows from from Corollary 13. The last one follows
from Theorem 10 which yields equivalences
RHomleft
R
Sn−1×R A(A,M) ∼= RHomle ft
CHSn−1(A) (CHRn(A),M)
∼= RHomle ft
A

CHRn(A)⊗L
CHSn−1(A) A,M

∼= RHomle ft
A
(CHSn(A),M) ∼= CHSn(A,M)
(36)
when A is an E∞-algebra.
Example 48. Let A be a smooth commutative algebra and M a symmetric A-
bimodule. By the HKR Theorem (see Theorem 3), one has CHSd(A) ∼= S•
A(Ω1
A[d])
which is a projective A-module since A is smooth. Thus, Corollary 15 implies
HHEd(A,M) ∼= S•
A(Der(A,M)[−d]).
We now explain the relationship in between En-Hochschild cohomology and
deformation of En-algebras. Denote En-Alg|A the ∞-category of En-algebras over
A. The bifunctor of En-derivations Der : (En-Alg|A)op × En-ModA →Chain(k) is
deﬁned as
Der(R,N) := MapEn-Alg|A(R,A⊕N).
The (absolute) cotangent complex of A (as an En-algebra) is the value on A of the
left adjoint of the split square zero extension functor En-ModA ∋M 7→A ⊕M ∈
En-Alg|A. In other words, there is an natural equivalence
MapEn-ModA(LA,−)
≃
−→Der(A,−)
65which is an object of Chain(k)
71


## Page 72


of functors. The (absolute) tangent complex of A (as an En-algebra) is the dual of
LA (as an En-module):
TA := RHomEn
A (LA,A) ∼= RHomleft
R
Sn−1×R A(LA,A).
The tangent complex has a structure of an (homotopy) Lie algebra which controls
the deformation of A as an En-algebra (that is, its deformations are precisely given
by the solutions of Maurer-Cartan equations in TA). Indeed, Francis [F1] has proved
the following beautiful result which solve (and generalize) a conjecture of Kontse-
vich [Ko]. His proof relies heavily on factorization homology and in particular on
the excision property to identify En-ModA with the En−1-Hochschild homology of
E1-LModA which is a En−1-monoidal category.
Theorem 13 ([F1]). Let A be an En-algebra and TA be its tangent complex. There
is a ﬁber sequence of non-unital En+1-algebras
A[−1] −→TA[−n] −→HHEn(A)
inducing a ﬁber sequence of (homotopy) Lie algebras
A[n−1] −→TA −→HHEn(A)[n]
after suspension.
7.2
Centralizers and (higher) Deligne conjectures
We will here sketch applications of factorization algebras to study centralizers and
solve the (relative and higher) Deligne conjecture.
The following deﬁnition is due to Lurie [L3] (and generalize the notion of
center of a category due to Drinfeld).
Deﬁnition 24. The (derived) centralizer of an En-algebra map f : A →B is the
universal En-algebra zn(f) equipped with a map of En-algebras ezn(f) : A⊗zn(f) →
B making the following diagram
A⊗zn(f)
ezn(f)
#
A
id⊗1zn(f)
;
f
/ B
(37)
commutative in En-Alg. The (derived) center of an En-algebra A is the centralizer
zn(A) := zn(A id→A) of the identity map.
The existence of the derived centralizer zn(f) of an En-algebra map f : A →B
is a non-trivial result of Lurie [L3]. The universal property means that if C
ϕ→B is
an En-algebra map ﬁtting inside a commutative diagram
A⊗C
ϕ
"
A
id⊗1C
<
f
/ B
(38)
72


## Page 73


then there is a unique66 factorization ϕ : A ⊗C
id⊗κ
99K A ⊗zn(f)
ezn(f)
−→B of ϕ by an
En-algebra map κ : C →zn(f). In particular, the commutative diagram
A⊗zn(f)⊗zn(g)
ezn(f)⊗id
(
A⊗zn(f)
id⊗1zn(g)
6
ezn(f)
(
B⊗zn(g)
ezn(g)
#
A
id⊗1zn(f)
;
f
/ B
id⊗1zn(g)
6
g
/ C
induces natural maps of En-algebras
zn(◦) : zn(f)⊗zn(g) −→zn(g◦f).
(39)
Example 49. Let M be a monoid (for instance a group). That is an E1-algebra
in the (discrete) category of sets with cartesian product for monoidal structure.
Then z1(M) = Z(M) is the usual center {m ∈M,∀n ∈M,n · m = m · n} of M. Let
f : H ,→G be the inclusion of a subgroup in a group G. Then z1(f) is the usual
centralizer of the subgroup H in G. This examples explain the name centralizer.
Similarly, let k-Mod be the (discrete) category of k-vector spaces over a ﬁeld k.
Then an E1-algebra in k-Mod is an associative algebra and z1(A) = Z(A) is its usual
(non-derived) center. However, if one sees A as an E1-algebra in the ∞-category
Chain(k) of chain complexes, then z1(A) ∼= RHomA⊗Aop(A,A) is (computed by)
the usual Hochschild cochain complex ([L]) in which the usual center embeds nat-
urally, but is different from it even when A is commutative.
Let A
f→B be an En-algebra map. Then B inherits a canonical structure of
En-A-module, denoted B f , which is the pullback along f of the tautological En-B-
module structure on B.
The relative Deligne conjecture claims that the centralizer is computed by En-
Hochschild cohomology.
Theorem 14 (Relative Deligne conjecture). Let A
f→B and B
g→C be maps of
En-algebras.
1. There is an En-algebra structure on HHEn(A,B f ) ∼= RHomEn
A (A,B f ) which
makes HHEn(A,B f ) the centralizer zn(f) of f (in particular, z(f) exists);
2. the diagram
zn(f)⊗zn(g)
zn(◦)
/ zn(g◦f)
RHomEn
A (A,B f )⊗RHomEn
B (B,Cg)
∼=
O
◦
/ RHomEn
A (A,Cg◦f )
∼=
O
66up to a contractible space of choices
73


## Page 74


is commutative in En-Alg (where the lower arrow is induced by composition
of maps in En-Mod).
3. If A
f→B is a map of E∞-algebras, then there is an equivalence of En-algebras
zn ∼= CHSn(A,B f ) where CHSn(A,B) is endowed with the structure given by
Proposition 7.
SKETCH OF PROOF. This result is proved in [GTZ3] (the techniques of [F1] shall
also give an independent proof) and we only brieﬂy sketch the main point of the
argument. We ﬁrst deﬁne an En-algebra structure on RHomEn
A (A,B f ). By Corol-
lary 8 and Theorem 9, we can assume that A, B are factorization algebras on Rn
and that a morphism of modules is a map of the underlying (stratiﬁed) factorization
algebras. We are left to prove that there is a locally constant factorization algebra
structure on Rn whose global sections are HHEn(A,B f ) ∼= RHomEn
A (A,B f ). It is
enough to deﬁne it on the basis of convex open subsets C V of Rn (by Proposi-
tion 17). To any convex open set U (with central point xU), we associate the chain
complex RHomFacU
A|U (A|U,B f |U) of factorization algebras morphisms from the re-
strictions A|U to B|U which, on the restriction to U \{xU} are given by f. Note that
since U is convex, there is a quasi-isomorphism
RHomFacU
A|U (A|U,B f |U) ∼= RHomEn
A (A,B f ) = RHomFacRn
A|Rn (A|Rn,Bf |Rn).
(40)
Now, given convex sets U1,...,Ur which are pairwise disjoint inside a bigger con-
vex V, we deﬁne a map
ρU1,...,Ur,V :
O
i=1...r
RHom
FacUi
A|Ui (A|Ui,B f |Ui) −→RHomFacV
A|V (A|V,B f |V)
as follows. To deﬁne ρU1,...,Ur,V(g1,...,gr), we need to deﬁne a factorization alge-
bra map on V and for this, it is enough to do it on the open set consisting of convex
subsets of V which either are included in one of the Ui and contains xUi or else does
not contains any xUi. To each open set xUi ∈Di ⊂Ui of the ﬁrst kind, we deﬁne
ρU1,...,Ur,V(g1,...,gr)(Di) : A(Di)
gi
−→B f (Di)
to be given by gi, while for any open set D ⊂V \{xU1,...,x|Ur}, we deﬁne
ρU1,...,Ur,V(g1,...,gr)(D) : A(D)
f
−→B f (D)
to be given by f. The conditions that g1,...,gr are maps of En-modules over A(Ui)
ensures that ρU1,...,Ur,V deﬁne the structure maps of a factorization algebra which is
further locally constant since ρU,Rn is the equivalence (40).
The construction is roughly described in Figure 4. One can check that the
natural evaluation map eval : A⊗RHomEn
A (A,B f ) →B is a map of En-algebras.
Now let C be an En-algebra ﬁtting in the commutative diagram (38), which
we again identify with a factorization algebra map (over Rn). By adjunction (in
74


## Page 75


Chain(k)), the map ϕ : A ⊗C →B has a (derived) adjoint θϕ : C →RHom(A,B).
Since ϕ is a map of factorization algebras and diagram (37) is commutative, one
check that θϕ factors through a map
˜θϕ : C −→RHomEn
A (A,B) ∼= CHSn(A,B).
(41)
which can be proved to be a map of factorization algebras. Further, by deﬁnition
of θϕ, the identity
eval ◦
 idA ⊗θϕ

= ϕ
holds. The uniqueness of the map ˜θϕ follows from the fact that the composition
RHomEn
A (A,B)
1RHomEn
A (A,A)⊗id
−→
RHomEn
A

A,A⊗RHomEn
A (A,B)
 ev∗
−→RHomEn
A (A,B)
is the identity map.
Finally the equivalence between zn(f) and CHSn(A,B f ) in the commutative
case follows from the string of equivalences (36) which can be checked to be an
equivalence of En-algebras using diagram (24) connecting algebras over the oper-
ads of little rectangles of dimension n and factorization algebras.
2
Example 50. Let A
f→B be a map of CDGAs. then by Proposition 15 we have an
equivalence HHEn(A,B) ∼= RHomle ft
CH∂In(A)(CHIn(A),CHIn(B)) where I = [0,1] and
∂In ∼= Sn−1 is the boundary of the unit cube In. We have a simplicial model In
• of
In where I• is the standard model of Example 1; its boundary ∂In
• is a simplicial
model for Sn−1. Then Theorem 14 identiﬁes the derived composition (39) as the
usual composition (of left dg-modules)
Homleft
CH∂In• (A)
 CHIn•(A),CHIn•(B)

⊗Homle ft
CH∂In• (B)
 CHIn•(B),CHIn•(C)

◦
−→Homle ft
CH∂In• (A)
 CHIn•(A),CHIn•(C)

.
f
g2
g3
V
U2
U3
U1
g1
Figure 4: The factorization al-
gebra map A|V →B|V obtained
by applying the relevant maps
of modules g1,g2,g3 (viewed
as maps of factorizations alge-
bras) and the En-algebra map
f : A →B on the respective re-
gions
75


## Page 76


The relative Deligne conjecture implies easily the standard one and also the
Swiss cheese conjecture. Indeed, Theorem 14 implies that the multiplication zn(A)⊗
zn(A)
zn(◦)
−→zn(A) makes zn(A) into an E1-algebra in the ∞-category En-Alg. The ∞-
category version of Dunn Theorem (Theorem 11) gives an equivalence E1-Alg
 En-Alg
 ∼=
En+1-Alg. This yields the following solution to the higher Deligne conjecture,
see [GTZ3, L3].
Corollary 16 (Higher Deligne Conjecture). Let A be an En-algebra.
The En-
Hochschild cohomology HHEn(A,A) has an En+1-algebra structure lifting the Yoneda
product which further lifts the En-algebra structure of the centralizer z(A id→A).
In particular, if A is commutative, there is a natural En+1-algebra structure on
CHSn(A,A) ∼= HHEn(A,A) whose underlying En-algebra structure is the one given
by Theorem 7. Hence the underlying E1-algebra structure is given by the cup-
product (Example 9).
Example 51. Let C be a monoidal (ordinary) category. Then the center z1(C ) is
in E2-Alg(Cat), that is a braided monoidal category. One can prove that z1(C ) is
actually the Drinfeld center of C , see [L3].
Remark 30. Presumably, the En+1-structure on HHEn(A) given by Corollary 16
shall be closely related to the one given by Theorem 13.
Example 52. Let 1A : k →A be the unit of an En-algebra A. Then zn(1A) ∼= A as an
En-algebra. The derived composition (39) yields canonical map67 of En-algebras
zn(A) ⊗zn(1A) −→zn(1A) which exhibits A ∼= zn(1A) as a right E1-module over
zn(A) ∼= HHEn(A,A) in the category of En-algebras (by Theorem 16). Hence, in
view of Example 37, we obtain, as an immediate corollary (see [Ca2]), a proof of
the Swiss-Cheese version of Deligne conjecture68:
Corollary 17 (Deligne conjecture with action). Let A be an En-algebra. Then the
pair (HHEn(A,A),A) is canonically an object of E1-RMod(En-Alg), that is A has
an natural action of the En+1-algebra HHEn(A,A).
Example 53 ((Higher homotopy) calculus again [Ca2]). Let A be an En-algebra.
Assume n = 0,1,3,7, so that A deﬁnes canonically a (locally constant) factoriza-
tion algebra ASn on the framed manifold Sn (see Example 19). Similarly the En+1-
algebra given by the higher Hochschild cohomology HHEn(A,A) deﬁnes canoni-
cally a (locally constant) factorization algebra on the manifold Sn×(0,∞) endowed
with the product framing.
The Deligne conjecture with action (Corollary 17) shows that A is also a left
module over HHEn(A,A). Thus, according to Proposition 30, the pair (HHEn(A,A),A)
yields a stratiﬁed locally constant factorization algebra H on Dn+1 \ {0}, the
closed disk in which we have removed the origin.
67which is equivalent to ez(1A)
68originally proved, for a slightly different variant of the swiss cheese operad, in [DTT, V]
76


## Page 77


By Theorem 8, we have that (ASn)(∂Dn+1) ∼=
R
Sn A. Collapsing the bound-
ary ∂Dn+1 to a point yields an adequatly stratiﬁed map τ : Dn+1 \ {0} →Rn+1
∗
so
that A := τ∗(H ) is stratiﬁed locally constant on Rn+1
∗
. It is further SO(n + 1)-
equivariant. Together with example 43, the above paragraph thus sketches a proof
of the following fact:
Corollary 18. Let A be an En-algebra and n = 0,1,3,7. Then A gives rise to an
SO(n + 1)-equivariant stratiﬁed locally constant factorization algebra A on the
pointed disk Rn+1
∗
such that A (Rn+1) ∼=
R
Sn A and for any sub-disk D ⊂Rn+1\{0},
there is an natural (with respect to disk inclusions) equivalence of En+1-algebras
A (D) ≃→HHEn(A,A).
In particular, for n = 1, we recover that the pair (HHE1(A,A),CHS1(A)), given
by Hochschild cohomology and Hochschild homology of an associative or A∞-
algebra A, deﬁnes an homotopy calculus (see [KS, TT] or Example 43).
This corollary is proved in details (using indeed factorization homology tech-
niques) in the interesting paper [Ho] along with many other examples in which Dn
is replaced by other framed manifold.
7.3
Higher string topology
The formalism of factorization homology for CDGAs and higher Deligne conjec-
ture was applied in [Gi, GTZ3] to higher string topology which we now explain
brieﬂy. We also refer to the work [Hu, HKV] for a related approach.
Let M be a closed oriented manifold, equipped with a Riemannian metric.
String topology is about the algebraic structure of the chains and homology of
the free loop space LM := Map(S1,M) and its higher free sphere spaces MSn :=
Map(Sn,M). These spaces have Fr´echet manifold structures and there is a submer-
sion ev : MSn →M given by evaluating at a chosen base point in Sn. The canon-
ical embedding Map(Sn ∨Sn,M)
ρin
−→Map(Sn,M) × Map(Sn,M) has an oriented
normal bundle69. It follows that there is a Gysin map (ρin)! : H∗

MSn `Sn
−→
H∗−dim(M)

MSn∨Sn
. The pinching map δSn : Sn →Sn ∨Sn (obtained by collapsing
the equator to a point) yields the map δ ∗
Sn : Map(Sn ∨Sn,M) −→MSn. The sphere
product is the composition
⋆Sn : H∗+dim(M)

MSn⊗2
→H∗+2dim(M)

MSn `Sn
(ρin)!
−→H∗+dim(M)

MSn∨Sn (δ ∗
Sn)∗
−→H∗+dim(M)

MSn
.
(42)
The circle action on itself induces an action γ : LM ×S1 →LM.
69which can be obtained as a pullback along ev of the normal bundle of the diagonal M →M ×M
77


## Page 78


Theorem 15.
1. (Chas-Sullivan [CS]) Let ∆: H∗(LM)
×[S1]
−→H∗+1(LM×S1)
γ∗
−→
H∗+1(LM) be induced by the S1-action. Then (H∗+dim(M)(LM),⋆S1,∆) is a
Batalin Vilkoviski-algebra and in particular a P2-algebra.
2. (Sullivan-Voronov [CV]) (H∗+dim(M)(LM),⋆Sn) is a graded commutative al-
gebra.
3. (Costello [C1], Lurie [L2]) If M is simply connected, the chainsC∗(LM)[dim(M)]
have a structure of E2-algebra (and actually of Diskor
2 -algebra) which, in
characteristic 0, induces Chas-Sullivan P2-structure in homology (by [FT]).
In [CV], Sullivan-Voronov also sketched a proof of the fact that H•+dim(M)(MSn)
is an algebra over the homology H∗(Diskor
n+1) of the operad Diskor
n+1 and in partic-
ular has a Pn+1-algebra structure (see Example 64). Their work and the aforemen-
tioned work for n = 1 (Theorem 15.3) rise the following
Question 1. Is there a natural En+1-algebra (or even Diskor
n+1-algebra) on the chains
C∗

MSn
[dim(M)] which induces Sullivan-Voronov product in homology ?
Using the solution to the higher Deligne conjecture and the relationship be-
tween factorization homology and mapping spaces, one obtains a positive solution
to the above question for sufﬁciently connected manifolds.
Theorem 16 ([GTZ3]). Let M be an n-connected70 Poincar´e duality space. The
shifted chain complexC•+dim(X)(XSn) has a natural71 En+1-algebra structure which
induces the sphere product ⋆Sn (given by the map (42)) of Sullivan-Voronov [CV]
Hp
 XSn
⊗Hq
 XSn
→Hp+q−dim(X)
 XSn
in homology when X is an oriented closed manifold.
SKETCH OF PROOF. We only gives the key steps of the proof following [GTZ3,
Gi].
• Let [M] be the fundamental class of M. The Poincar´e duality map χM : x 7→
x ∩[M] is a map of left modules and thus, by Proposition 40 (and since,
by assumption, the biduality homomorphism C∗(X) →(C∗(X))∨is a quasi-
isomorphism),
χM : C∗(X) →C∗(X)[dim(X)] ∼=
 C∗(X)
∨[dim(X)]
has an natural lift as an E∞-module. And thus as an En-module as well.
70it is actually sufﬁcient to assume that M is nilpotent, connected and has ﬁnite homotopy groups
πi(M,m0) for 1 ≤i ≤n
71with respect to maps of Poincar´e duality spaces
78


## Page 79


• From the previous point we deduce that there is an equivalence
HHEn(C∗(X),C∗(X)) ∼= RHomEn
C∗(X)
 C∗(X),C∗(X)

(χM)∗
−→RHomEn
C∗(X)
 C∗(X),
 C∗(X)
∨
[dim(M)]
∼= RHomleft
R
Sn−1×RC∗(X)
 C∗(X),
 C∗(X)
∨
[dim(M)]
∼= RHomleft
C∗(X)
 C∗(X)⊗LR
Sn−1×RC∗(X)C∗(X),k

[dim(M)]
∼= RHomle ft
C∗(X)
 CHSn(C∗(X)),k

[dim(M)].
(43)
where the last equivalence follows from Theorem 10.
• By Theorem 5 relating Factorization homology of singular cochains with
mapping spaces, the above equivalence (43) induces an equivalence
C∗

MSn
[dim(M)]
≃
−→HHEn(C∗(X),C∗(X)).
(44)
• Now, one uses the higher Deligne conjecture (Corollary 16) and the lat-
ter equivalence (44) to get an En+1-algebra structure on C∗

MSn
[dim(M)].
The explicit deﬁnition of the cup-product given by Proposition 7 (and Theo-
rem 14) allows to describe explicitly the E1-algebra structure at the level of
the cochains C∗
MSn
through the equivalence (44), which, in turn allows
to check it induces the product ⋆Sn.
2
Example 54. Let M = G be a Lie group and A = S(V) ≃→ΩdR(G) be its minimal
model. The graded space V is concentrated in positive odd degrees. If G is n-
connected, by the generalized HKR Theorem 3, there is an equivalence
S(V ⊕V ∗[−n]) ∼= CHSn(A,A) ∼= C∗

GSn
[dim(G)]
(45)
in Chain(k). The higher formality conjecture shows that the equivalence (45) is
an equivalence of En+1-algebras. Here the left hand side is viewed as an En+1-
algebra obtained by the formality of the En+1-operad from the Pn+1-structure on
S(V ⊕V ∗[−n]) whose multiplicative structure is the one given by the symmetric
algebra and the bracket is given by the pairing between V and V ∗.
7.4
Iterated loop spaces and Bar constructions
In this section we apply the formalism of factorization homology to describe it-
erated Bar constructions equipped with their algebraic structure and relate them
to the En-algebra structure of nth-iterated loop spaces. We follow the approach
of [F1, AF, GTZ3].
79


## Page 80


Bar constructions have been introduced in topology as a model for the coal-
gebra structure of the cochains on Ω(X), the based loop space of a pointed space
X. Similarly the cobar construction of coaugmented coalgebra has been studied
originally as a model for the (E1-)algebra structure of the chains on Ω(X). The Bar
and coBar constructions also induce equivalences between algebras and coalgebras
under sufﬁcient nilpotence and degree assumptions [HMS, FHT, FG].
Let (A,d) be a differential graded unital associative algebra which is aug-
mented, that is equipped with an algebra homomorphism ε : A →k.
Deﬁnition 25. The standard Bar functor of the augmented algebra (A,d,ε) is
Bar(A) := k
L⊗
A k.
If A is ﬂat over k, it is computed by the standard chain complex Barstd(A) =
L
n≥0 A
⊗n (where A = ker(A ε→k) is the augmentation ideal of A) endowed with
the differential
b(a1 ⊗···an)
=
n
∑
i=1
±a1 ⊗···⊗d(ai)⊗···⊗an
+
n−1
∑
i=1
±a1 ⊗···⊗(ai ·ai+1)⊗···⊗an
see [FHT, Fr2] for details (and signs).
The Bar construction has a standard coalgebra structure. It is well-known that
if A is a commutative differential graded algebra, then the shufﬂe product makes
the Bar construction Barstd(A) a CDGA and a bialgebra as well. It was proved
by Fresse [Fr2] that Bar constructions of E∞-algebras have an (augmented) E∞-
structure, allowing to consider iterated Bar constructions and further that there
is a canonical nth-iterated Bar construction functor for augmented En-algebras as
well [Fr3].
Let us now describe the factorization homology/algebra point of view on Bar
constructions.
An augmented En-algebra is an En-algebra A equipped with an En-algebra map
ε : A →k, called the augmentation. We denote En-Algaug the ∞-category of aug-
mented En-algebras (see Deﬁnition 31). The augmentation makes k an En-module
over A.
By Proposition 35, an augmented En-algebra deﬁnes naturally a locally con-
stant factorization algebra on the closed unit disk (with its stratiﬁcation given by
its boundary) of dimension less than n. Indeed, we obtain functors
ωDi : En-Algaug −→Ei-Algaug(En−i-Algaug) −→Faclc
Di(En−i-Algaug).
(46)
80


## Page 81


Deﬁnition 26. Let A be an augmented En-algebra. Its Bar construction is
Bar(A) :=
Z
I×Rn−1 A
L⊗
R
S0×Rn−1 Ak.
This deﬁnition agrees with Deﬁnition 25 for differential graded associative al-
gebras and further we have equivalences
Bar(A) :=
Z
I×Rn−1 A
L⊗
R
S0×Rn−1 Ak ∼= k
L⊗
A k ∼= p∗(ωD1(A))
(47)
where I is the closed interval [0,1] and p : I →pt is the unique map; in particular
the right hand side of (47) is just the factorization homology of the associated
factorization algebra on D1.
The functor (46) shows that Bar(A) ∼= p∗(ωD1(A)) has an natural structure of
augmented En−1-algebra (which can also be deduced from Lemma 5.2).
We can thus iterate (up to n-times) the Bar constructions of an augmented En-
algebra.
Deﬁnition 27. Let 0 ≤i ≤n. The ith-iterated Bar construction of an augmented
En-algebra A is the augmented En−i-algebra
Bar(i)(A) := Bar(···(Bar(A))···).
Using the excision axiom of factorization homology, one ﬁnds
Lemma 8 (Francis [F1], [GTZ3]). Let A be an En-algebra and 0 ≤i ≤n. There is
a natural equivalence of En−i-algebras
Bar(i)(A) ∼=
Z
Di×Rn−i A
L⊗
R
Si−1×Rn−i+1 Ak ∼= p∗(ωDi(A))
In particular, taking n = ∞, we recover an E∞-structure on the iterated Bar
construction Bar(i)(A) of an augmented E∞-algebra.
We now describes the expected coalgebras structures. We start with the E∞-
case, for which we can use the derived Hochschild chains from § 2. Then, Lemma 8,
Theorem 10 and the excision axiom give natural equivalences of E∞-algebras ([GTZ3]):
CHSi(A,k) ∼= Bar(i)(A).
(48)
Recall the continuous map (13) pinch : Cubed(r)×Sd −→W
i=1...r Sd. Similarly
to the deﬁnition of the map (15), applying the singular set functor to the map (13)
we get a morphism
pinchSn,r
∗
: C∗
 Cubed(r)

⊗CHSd(A)
L⊗
A k
pinch∗⊗L
Aid
−→
CHWr
i=1 Sd(A)
L⊗
A k ∼=

CH`r
i=1 Sd(A)
L⊗
A⊗r A
 L⊗
A k
∼=

CH`r
i=1 Sd(A)
 L⊗
A⊗r k ∼=

CHSd(A,k)
⊗r
(49)
81


## Page 82


Proposition 42 ([GTZ3]). Let A be an augmented E∞-algebra. The maps (49)
pinchSd,r
∗
makes the iterated Bar construction Bar(d)(A) ∼= CHSd(A,k) a natural
En-coalgebra in the ∞-category of E∞-algebras.
If Y is a pointed space, its E∞-algebra of cochains C∗(Y) has a canonical aug-
mentation C∗(Y) →C∗(pt) ∼= k induced by the base point pt →Y. By Theorem 4,
we have an E∞-algebra morphism
I tΩn : Bar(n)(C∗(Y)) ∼= CHSn(C∗(Y),k)
I t⊗L
C∗(Y)k
−→
C∗ Y Sn
⊗L
C∗(Y) k −→C∗ Ωn(Y)

.
(50)
We now have a nice application of factorization homology in algebraic topol-
ogy.
Corollary 19.
1. The map (50) I tΩn : Bar(n)(C∗(Y)) →C∗ Ωn(Y)

is an En-
coalgebra morphism in the category of E∞-algebras. It is further an equiv-
alence if Y is connected, nilpotent and has ﬁnite homotopy groups πi(Y) in
degree i ≤n.
2. The dual of (50) C∗
 Ωn(Y)

−→
 C∗
 Ωn(Y)
∨∨I tΩn
−→

Bar(n)(C∗(Y))
∨
is
a morphism in En-Alg. If Y is n-connected, it is an equivalence.
We now sketch the construction of the Ei-coalgebra structure of the ith-iterated
Bar construction of an En-algebra. To do so, we only need to deﬁne a locally
constant cofactorization algebra structure72 whose global section is Bar(i)(A). By
(the dual of) Proposition 17, it is enough to deﬁne such a structure on the basis of
convex open disks of Ri. Let A ∈Faclc
Ri(En−i-Algaug) be the factorization algebra
associated to A (by Theorem 9 and Theorem 11).
Let V be a convex open subset. By Corollary 10 (and Theorem 9), the aug-
mentation gives us a stratiﬁed locally constant factorization algebra bω(A|V) on
bV = V ∪{∞} (with values in En−i-Algaug).
If U ⊂V is a convex open subset, we have a continuous map πU : bV →bU
which maps the complement of U to a single point. Further, the augmentation
deﬁnes maps of factorization algebras (on bU)
εU : πU ∗( bω(A|V)) −→bω(A|U)
which, on every open convex subset of U is the identity, and, on every open convex
neighborhood of ∞is given by the augmentation.
Deﬁne
Bar(i)(A)(U) :=
Z
V
bω(A|V) ∼=
Z
U πU ∗( bω(A|V))
72that is a locally constant coalgebra over the ∞-operad Disk(Ri) see remark 24
82


## Page 83


to be the factorization homology of bω(A|V). We ﬁnally get, for U1,...,Us pairwise
disjoint convex subsets of a convex open subset V, a structure map
∇U1,...,Us,V : Bar(i)(A)(V) =
Z
V( bω(A|V)
NR
Ui εUi
−→
O
i=1...s
Z
Ui
bω(A|Ui)
≃
−→Bar(i)(A)(U1)⊗···⊗Bar(i)(A)(Us).
(51)
The maps ∇U1,...,Us,V are the structure maps of a locally constant factorization
coalgebras (see [GTZ3]) hence they make Bar(i)(A) into an Ei-coalgebra (with
values in the category of En−i-algebras), naturally in A:
Theorem 17 ([F1, GTZ3, AF]). The iterated Bar construction lifts into an ∞-
functor
Bar(i) : En-Algaug −→Ei-coAlg

En−i-Algaug
.
One has an natural equivalence73 Bar(i)(A) ∼= k
L⊗
A k in En−i-Alg.
Further this functor is equivalent to the one given by Proposition 42 when
restricted to augmented E∞-algebras.
Example 55. Let Freen be the free En-algebra on k as in Example 16. By Deﬁni-
tion 26, we have equivalences of En−1-algebras.
Bar(Freen)
=
Z
D1×Rn−1 Freen
L⊗
R
S0×Rn−1 Freen
k
∼=
Z
S1×Rn−1 Freen
L⊗
R
Rn−1 Freen
k
∼=

Freen ⊗Freen−1(k[1])

L⊗
R
Rn−1 Freen
k
(by Proposition 8)
∼=
Freen−1(k[1]).
The result also holds for Freen(V) instead of Freen, see [F2]. Iterating, one ﬁnds
Proposition 43 ([F2]). There is a natural equivalence of En−i-algebras
Bar(i)(Freen(V)) ∼= Freen−i(V[i]).
If one works in Top∗instead of Chain(k), then Freen(X) = ΩnΣnX and the
above proposition boils down to Bar(i)(ΩnΣnX) ∼= BiΩi(Ωn−iΣnX) ≃←Ωn−iΣn−i(ΣiX).
73the relative tensor product being the tensor product of Ei-modules over A
83


## Page 84


7.5
En-Koszul duality and Lie algebras homology
Let A ε→k be an augmented En-algebra. The linear dual RHom(Bar(n)(A),k) of the
nth-iterated Bar construction inherits an En-algebra structure (Theorem 17).
Deﬁnition 28 ([L3, F1]). The En-algebra A(n)! := RHom(Bar(n)(A),k) dual to the
iterated Bar construction is called the (derived) En-Koszul dual of A.
The terminology is chosen because it agrees with the usual notion of Koszul
duality for quadratic associative algebras but it is really more like a En-Bar-duality.
Direct inspection of the En-algebra structures show that the dual of the iterated
Bar construction is equivalent to the centralizer of the augmentation. (see § 7.2):
Lemma 9 ([L3, GTZ3]). Let A
ε→k be an augmented En-algebra. There is an
natural equivalence of En-algebras A(n)! ∼= zn(A ε→k).
Let M be a dimension m manifold endowed with a framing of M × Rn. By
Proposition 35, Theorem 11 and Proposition 18, we have the functor
ωM×Dn : En+m-Algaug →En-Algaug(Em-Alg)
ωDn
−→Faclc
Dn(Em-Alg) ∼= Faclc
Rm×Dn −→Faclc
M×Dn
where the last map is induced by the framing of M×Rn as in Example 19. Let p be
the map p : M ×Dn →pt. We can compute the factorization homology p∗(ωM×Dn)
by ﬁrst pushing forward along the projection on Dn and then applying p∗or ﬁrst
pushing forward on M and then pushing forward to the point. By Theorem 17, we
thus obtain an equivalence
p∗(ωM×Dn) ∼= Bar(n)Z
M×Rn A

∼=
Z
M
 Bar(n)(A)

(52)
where the right equivalence is an equivalence of En-coalgebras. When M is further
closed, this result can be extended to obtain :
Proposition 44 (Francis [F2, AF]). Let A be an augmented En+m-algebra, M ×Rn
be a framed closed manifold. There is an natural equivalence of En-algebras
Z
M×Rn A(n+m)! ∼=
Z
M×Rn A
(n)!
if Bar(n)R
M×Rn A

has projective ﬁnite type homology groups in each degree. In
particular,
R
M A(m)! ∼=
 R
M A
∨when M is framed (and the above condition is sat-
isﬁed).
In plain english, we can say that the factorization homology over a closed
framed manifold of an algebra and its En-Koszul dual are the same (up to ﬁniteness
issues).
84


## Page 85


Example 56 (Lie algebras and their En-enveloping algebras). Let Lie-Alg be the
∞-category of Lie algebras74. The forgetful functor En-Alg →Lie-Alg, induced
by A 7→A[n −1], has a left adjoint U(n) : Lie-Alg →En-Alg, the En-enveloping
algebra functor (see [Fr4, FG] for a construction). For n = 1, this functor agrees
with the standard universal enveloping algebra.
Proposition 45 (Francis [F2]). Let g be a (differential graded) Lie algebra. There
is an natural equivalence of En-coalgebras
(U(n)(g))(n)! ∼= C•
Lie(g)
where C•
Lie(g) is the usual Chevalley-Eilenberg cochain complex (endowed with its
differential graded commutative algebra structure).
Then using Proposition 44 and Proposition 45, we obtain for n = 1,3,7 that
Z
Sn U(n)(g) ∼=
Z
Sn C•
Lie(g)
∨
which for n = 1 gives the following standard result computing the Hochschild ho-
mology groups of an universal enveloping algebra: HH∗(U(g)) ∼= HH∗(C•
Lie(g))∨.
Applying the Fubini formula, we also ﬁnd
Z
S1×S1 U(2)(g) ∼= CH∗
 CH∗(C•
Lie(g))(1)!
.
7.6
Extended topological quantum ﬁeld theories
In [L2], Lurie introduced factorization homology as a (generalization of) an in-
variant of an extended topological ﬁeld theory and offshoot of the cobordism hy-
pothesis. We wish now to reverse this construction and explain very roughly how
factorization homology can be used to produce an extended topological ﬁeld the-
ory.
Following [L2], there is an ∞-category75 of extended topological ﬁeld theo-
ries with values in a symmetric monoidal (∞,n)-category with duals (C ,⊗). It is
the category of symmetric monoidal functors Fun⊗ (Bordfr
n ,`),(C ,⊗)

where
Bord fr
n
is the (∞,n)-category of bordisms of framed manifolds with monoidal
structure given by disjoint union. In [L2], Bord fr
n is deﬁned as an n-fold Segal space
which precisely models the following intuitive notion of an (∞,n)-category whose
objects are framed compact 0-dimensional manifolds. The morphisms between
objects are framed 1-bordism, that is HomBord fr
n (X,Y) consists of 1-dimensional
framed manifolds T with boundary ∂T = Y `Xop (where Xop has the opposite
framing to the one of the object X). The 2-morphisms in Bord fr
n are framed 2-
bordisms between 1-dimensional framed manifolds (with corners) and so on. The
74which is equivalent to the category of L∞-algebras
75the cobordism hypothesis actually ensures that it is an ∞-groupoid
85


## Page 86


n-morphisms are n-framed bordisms between n−1-dimensional framed manifolds
with corners, its n+1-morphisms diffeomorphisms and the higher morphisms are
isotopies.
Note that in the precise model of Bordfr
n , the boundary component
N1,...,Nr of a manifold M are represented by an open manifold with boundary
components N1 ×R,...,Nr ×R (in other words are replaced by open collars).
There is an (∞,n + 1)-category E≤n-Alg whose construction is only sketched
in [L2] and detailled in [Sc] using a model based on factorization algebras. The
category E≤n-Alg can be described informally as the ∞-category with objects the
En-algebras, 1-morphisms HomE≤n-Alg(A,B) is the space of all (A,B)-bimodules
in En−1-Alg and so on. The (∞-)category n-HomE≤n-Alg(P,Q)) of n-morphisms
is the ∞-category of (P,Q)-bimodules where P,Q are E1-algebras (with additional
structure). In other words we have
n-HomE≤n-Alg(P,Q))
∼=
{P}
×
Faclc
(−∞,0)
Faclc
R∗
×
Faclc
(0,+∞)
{R}
∼=
{P} ×
E1-AlgBiMod ×
E1-Alg{R}
see Example 34. The composition
n-HomE≤n-Alg(P,Q))×n-HomE≤n-Alg(Q,R)) −→n-HomE≤n-Alg(P,R))
is given by tensor products of bimodules: PMQ ⊗L
Q QNR which in terms of factor-
ization algebras is induced by the pushforward along the map q : R∗×R R∗→R∗
where R∗×R R∗is identiﬁed with R stratiﬁed in two points −1 and 1 and q is the
quotient map identifying the interval [−1,1] with the stratiﬁed point 0 ∈R∗.
Let E≤n-Alg(0) be the (∞,n)-category obtained from E≤n-Alg by discarding
non-invertible n+1-morphisms, that is E≤n-Alg(0) = Gr(n)(E≤n-Alg) where Gr(n)
is the right adjoint of the forgetful functor (∞,n+1)-Cat →(∞,n)-Cat.
The (∞,n)-category E≤n-Alg(0) is fully dualizable (the dual of an algebra is its
opposite algebra) hence every En-algebra determines in an unique way an extended
topological ﬁeld theory by the cobordism hypothesis.
In fact, this extended ﬁeld theory can be constructed by factorization homology.
Let M be a m-dimensional manifold. We say that M is stably n-framed if M×Rn−m
is framed. Assume that M has two ends which are trivialized as L×Rop ⊂M and
R×R ⊂M, where L,R are stably framed codimension 1 closed sub-manifolds; here
Rop means R endowed with the opposite framing to the standard one. For instance,
M can be the interior of compact manifold M with two boundary component L, R
and trivializations L × [0,∞) ,→M and R × (−∞,0] ,→M where the trivialization
on L×[0,∞) has the opposite orientation as the one induced by M.
In that case, Lemma 5 (and Proposition 29) imply that the factorization homol-
ogy
R
M A is an En−m-algebra which is also a bimodule over the En−m+1-algebras
 R
L×Rn−m+1 A,
R
R×Rn−m+1 A

:
Z
M×Rn−m A ∈
nZ
L×Rn−m+1 A
o
×
E1−-AlgBiMod
 En−m-Alg

×
E1−-Alg
nZ
R×Rn−m+1 A
o
.
86


## Page 87


Thus
R
M A is a m-morphism in E≤n-Alg(0) from R to L. In fact, one can prove
Theorem 18 ([Sc]). Let A be an En-algebra. The rule which, to a stably n-framed
manifold M of dimension m, associates
ZA(M) :=
Z
M×Rn−m A
extends as an extended ﬁeld theory ZA ∈Fun⊗ Bordfr
n ,E≤n-Alg(0)

.
8
Commutative factorization algebras
In this Section, we explain in details the relationship in between classical homology
theory `a la Eilenberg-Steenrod with factorization homology and more generally
between (co)sheaves and factorization algebras. The main point is that when C is
endowed with the monoidal structure given by the coproduct, then Factorization
algebras boils down to the usual theory of cosheaves. This is in particular the
case of factorization algebras with values in a category of commutative algebras
E∞-Alg(C ,⊗) in (C ,⊗).
8.1
Classical homology as factorization homology
In this section we explain the relationship between factorization homology and
singular homology (as well as generalized (co)homology theories for spaces).
Let Chain(Z) be the (∞-)category of differential graded abelian groups (i.e.
chain complexes of Z-modules). It has a symmetric monoidal structure given by
the direct sum of chain complexes, which is the coproduct in Chain(Z). We can
thus deﬁne homology theory for manifolds with values in (Chain(Z),⊕). These
are precisely (restrictions of) the (generalized) cohomology theories for spaces and
nothing more. Recall that Mﬂdor
n is the (∞-)category of oriented manifolds, Exam-
ple 11.
Corollary 20. Let G be an abelian group76. There is an unique homology theory
for oriented manifolds with coefﬁcient in G (Deﬁnition 11), that is (continuous)
functor HG : Mﬂdor
n →Chain(Z) satisfying the axioms
• (dimension) HG(Rn) ∼= G ;
• (monoidal) the canonical map L
i∈I
HG(Mi)
≃
−→HG(`
i∈I
Mi) is a quasi-isomorphism;
• (excision) If M is an oriented manifold obtained as the gluing M = R∪N×R L
of two submanifolds along a a codimension 1 submanifold N of M with a
76or even a graded abelian group or chain complex of abelian groups
87


## Page 88


trivialization N × R of its tubular neighborhood in M, there is an natural
equivalence
HG(M)
≃
←−cone

HG(N ×R)
iL−iN
−→HG(L)⊕HG(R)

.
Here HG(N ×R)
iL
−→HG(L) and HG(N ×R)
iR
−→HG(R) are the maps
induced by functoriality by the inclusions of N ×R in L and R.
Then, this homology theory is singular homology77 with coefﬁcient in G. In partic-
ular, it extends as an homology theory for spaces.
The uniqueness means of course up to a contractible choice, meaning that any
two homology theory with coefﬁcient in G will be naturally equivalent and any two
choices of equivalences will also be naturally equivalent and so on.
Proof. This is a consequence of Proposition 46 below applied to C = Chain(Z)
and the fact that the homotopy colimit
hocolim

HG(R)
HG(N ×R)
iR
o
iL
/ HG(L)

is precisely computed by the cone78 of the map iL −iR.
Remark 31. Let H be a topological group, f : H →Homeo(Rn) a map of topo-
logical groups and B f : BH →BHomeo(Rn) the induced map, so that we have the
category Mﬂd(BH,Bf)
n
of manifolds with H-structure, see Example 11. As shown
by its proof, Corollary 20 also holds with oriented manifolds replaced by mani-
fold with a H-structure; in particular for all manifolds or a contrario for framed
manifolds.
Remark 32. Corollary 20 and Theorem 10 implies that HG(M) is computed by
(derived) Hochschild homology CHM(G) (in (Chain(Z),⊕)). If M• is a simplicial
set model of M, then HG(M) ∼= CHM•(G) which is exactly (by § 2.3) the chain
complex of the simplicial abelian group G[M•]. In particular, for M• = ∆•(M) =
Hom(∆•,M), one recovers exactly the singular chain complex C∗(M) of M.
Corollary 20 is a particular case of a more general result which we now de-
scribe. Let C be a category with coproducts. Then (C ,`) is symmetric monoidal,
with unit given by its initial object /0. As we have seen in § 2.1, any object X of C
carries a canonical (thus natural in X) structure of commutative algebra in (C ,`)
which is given by the “multiplication” X `X
`idX
−→X induced by the identity map
idX : X →X on each component. This algebra structure is further unital, with unit
given by the unique map /0 →X. This deﬁnes a functor triv : C →E∞-Alg(C )
77or generalized exceptional homology when G is graded or a chain complex
78note that in this case, we know a posteriori that we can choose HG to be singular chains, so
that HG(iL)⊕HG(iR) is injective and the cone is equivalent to a quotient of chain complexes
88


## Page 89


which to an object associates its trivial commutative algebra structure. In fact, the
latter algebras are the only only possible commutative and even associative ones in
(C ,`).
Lemma 10 (Eckman-Hilton principle). Let C be a category with coproducts and
(C ,`) the associated symmetric monoidal category. Let H
f→Homeo(Rn) be
a topological group morphism and ι : Disk(BH,B f)
n
-Alg(C ) →C be the underlying
object functor (16) (Deﬁnition 9). We have a commutative diagram of equivalences
E∞-Alg(C )
≃
/ Disk(BH,B f)
n
-Alg(C )
≃
ι
w
C
≃
triv
d
where the horizontal arrow is the canonical functor of Example 13.
In particular, any En-algebra (n ≥1) in (C ,`) is a (trivial) commutative al-
gebra.
Proof. Let I = {1,...,n} be a ﬁnite set and mI : `
i∈IC →C be any map. The
universal property of the coproduct yields a commutative diagram
 `
i∈IC
` `
i∈IC

mI
`mI
/
 `
i∈I(`idC)

◦σI

C`C
`idC

`
i∈IC
mI
/ C
where σI is the permutation induced by the bijection (1,n+1)(2,n+2)···(n,2n)
of I `I = {1,...,2n} on itself. Hence, if C is an En-algebra, it is naturally an ob-
ject of En-Alg(E∞-Alg) where the commutative algebra structure is the trivial one
C`C
`idC
→C. By Dunn Theorem 11 (or Eckman-Hilton principle), the forgetful
map (induced by the pushforward of factorization algebras) En-Alg((E∞-Alg)) −→
E0-Alg(E∞-Alg) is an equivalence. It follows that the En-algebra C is an E∞-
algebra whose structure is equivalent to triv(C).
The group map {1} →H induces a canonical functor Disk(BH,B f)
n
-Alg →En-Alg
so that the above result implies that such a Disk(BH,B f)-algebra with underlying ob-
ject C is necessarily of the form triv(C).
Proposition 46. Let (C ,`) be a ∞-category whose monoidal structure is given by
the coproduct and f : H →Homeo(Rn) be a topological group morphism .
• Any homology theory for (BH,Bf)-structured manifolds (Deﬁnition 10) ex-
tends uniquely into an homology theory for spaces (Deﬁnition 1).
• Any objectC ∈C determines a unique homology theory for (BH,Bf)-manifolds
with values in C (Deﬁnition 11); further the evaluation map H 7→H (Rn)
is an equivalence between the category of homology theories for (BH,Bf)-
manifolds in (C ,`) and C .
89


## Page 90


Proof. By Theorem 6, homology theories for (BH,Bf)-structured manifolds are
equivalent to Disk(BH,Bf)
n
-algebras which, by Lemma 10, are equivalent to C . In
particular, any Disk(BH,Bf)
n
-algebra is given by the commutative algebra associated
to an object of C so that by Theorem 10, it extends to an homology theory for
spaces.
8.2
Cosheaves as factorization algebras
In this Section we identify (pre-)cosheaves and (pre-)factorization algebras when
the monoidal structure is given by the coproduct.
Let (C ,⊗) be symmetric monoidal and let F be in PFacX(C ). Then the struc-
ture maps F(U) →F(V) for any open U inside an open V induces a functor
γC : PFacX(C ) −→PcoShvX(C ) where PcoShvX(C ) := Fun(Open(X),C ) is the
∞-category of precosheaves on X with values in C .
Lemma 11. Let (C ,`) be an ∞-category with coproducts whose monoidal struc-
ture is given by the coproduct and X be a topological space.
1. The functor γC : PFacX(C ) −→PcoShvX(C ) is an equivalence.
2. If X has a factorizing basis of opens79, then the functor γC : PFacX(C ) −→
PcoShvX(C ) restricts to an equivalence
FacX(C )
≃
−→coShvX(C )
between factorization algebras on X and the ∞-category coShvX(C ) of (ho-
motopy) cosheaves on X with values in C .
3. If X is a manifold, then the above equivalence also induces an equivalence
Faclc
X (C )
≃
−→coShvlc
X (C ) between locally constant factorization algebras
and locally constant cosheaves.
Proof. Let F be in PFacX and U1,...,Ur be open subsets of V ∈Open(X), which
are pairwise disjoint. Let ρU1,...,Ui,V : F(U1)`...`F(Ui) →F(V) be the struc-
ture map of F. The associativity of the structure maps (diagram (19)) shows that
the structure map ρUj,V : F(Uj) →F(V) factors as
F(Uj)
ρUj,V
/
∼=

F(V)
/0`... /0`F(Uj)` /0...` /0
  j−1
`
k=1
ρ/0,Uk
`id ` i`
k=j+1
ρ/0,Uk

/ F(U1)`...`F(Ui).
ρU1,...,Ui,V
O
79for instance when X is Hausdorff
90


## Page 91


The universal property of the coproduct implies that the following diagram
F(U1)`...`F(Ui)
ρU1,...,Ui,V
/
ρU1,V
`...`ρUi,V

F(V)
F(V)`...`F(V)
`idF(V)
3
(53)
is commutative. It follows that the structure maps are completely determined by
the precosheaf structure. Conversely, any precosheaf on C gives rise functorially
to a prefactorization algebra with structure maps given by the composition
F(U1)
a
...
a
F(Ui) −→F(V)
a
...
a
F(V)
`idF(V)
−→
F(V)
yielding a functor θC : PcoShvX(C ) →PFacX(C ). The commutativity of dia-
gram (53) implies that this functor θC is inverse to γC : PFacX(C ) →PcoShvX(C ).
Note that both the cosheaf condition and the factorization algebra conditions
implies that the canonical map F(U1)`...`F(Ui) →F(U1
`...`Ui) is an
equivalence (of constant simplicial objects). Now, we can identify the two gluing
conditions. Since U is a (factorizing) cover of V, then
P(U) := {{U1,...,Uk}, which are pairwise disjoint}
is a cover of V. Further, if F ∈FacX, the ˇCech complex ˇC(U ,F) is precisely the
(standard) ˇCech complex ˇCcosheaf(PU ,γC (F)) of the cosheaf γC (F) computed
on the cover PU so that the map ˇC(U ,F) →F(V) is an equivalence if and only
if ˇCcosheaf(PU ,γC (F)) →F(V) is an equivalence.
Assume X has a factorizing basis of opens. Both factorization algebras and
cosheaf are determined by their restriction on a basis of opens. It follows that γC
sends factorization algebras to cosheaves and θC sends cosheaves to factorization
algebras.
It remains to consider the locally constant condition when X is a manifold,
thus has a basis of euclidean neighborhood. On each euclidean neighborhood D,
by Theorem 9, the restriction of F ∈Faclc
X to D is the factorization algebra given
by an En-algebra A ∈En-Alg((C ,`)) in C . Lemma 10 implies that A is given
by the trivial commutative algebra triv(C) associated to an object C ∈C . It fol-
lows from the identiﬁcation of ˇCech complexes above, that F|D is thus equivalent
to the constant cosheaf on D associated to the object C. The converse follows
from the fact if G ∈coShvlc
X (C ), then for any point x ∈X, there is an euclidean
neighborhood Dx ∼= Rn on which G|Dx is constant. The identiﬁcation of the ˇCech
complexes above implies that θC (G|Dx) is locally constant on Dx. Proposition 13
implies that the factorization algebra θC (G ) is locally constant on X, hence ﬁnishes
the proof.
From the identiﬁcation between cosheaves and factorization algebras, we de-
duce that factorization homology in (C ,`) agrees with homology with local co-
efﬁcient:
91


## Page 92


Proposition 47. Let (C ,`) be a ∞-category whose monoidal structure is given by
the coproduct and X a manifold.
• There is an equivalence between homology theories for (X,TX)-structured
manifolds (Deﬁnition 10) and coShvlc
X (C ), the (∞-)category of locally con-
stant cosheaves on X with values in C .
• The above equivalence is given, for any (X,TX)-structured manifold M and
(homotopy) cosheaf G ∈coShvlc
X (C ), by
Z
M G := RΓ(M,G )
the cosheaf homology of M with values in the cosheaf p∗(G ) where p : M →
X is the map deﬁning the (X,TX)-structure.
Proof. The ﬁrst claim is an immediate application of Lemma 11.3 and Theorem 8.
The latter result implies that factorization homology is computed by the ˇCech com-
plex of the locally constant factorization algebra associated to a Disk(M,TM)
n
-algebra
given by the pullback along p : M →X of some A ∈Disk(X,TX)
n
-Alg. Now the sec-
ond claims follows from Lemma 11.2.
Remark 33. Factorization homology on a (X,e)-structured manifold M depends
only on its value on open sub sets of M. Thus Proposition 47 implies that, for any
manifold M and A ∈Disk(X,e)
n
-Alg(C ), factorization homology
R
M A is given by
cosheaf homology of the locally constant cosheaf G given by the image of A under
the functor Disk(X,e)
n
-Alg →Disk(M,TM)
n
-Alg (of Example 12) and the equivalence
Faclc
X (C )
≃
−→coShvlc
X (C ) of Lemma 11.
Let (C ,⊗) be a symmetric monoidal (∞-)category. We say that a factoriza-
tion algebra F on X is commutative if each F(U) is given a structure of differ-
ential graded commutative (or E∞-) algebra and the structure maps are maps of
algebras. In other words, the category of commutative factorization algebras is
FacX(E∞-Alg).
A peculiar property of (differential graded) commutative algebras is that their
coproduct is given by their tensor product (that is the underlying tensor product in
C endowed with its canonical algebra structure). From Lemma 11, we obtain the
following:
Proposition 48. Let (C ,⊗) be a symmetric monoidal (∞-)category. The functor
γE∞-Alg(C ) : FacX(E∞-Alg(C )) −→coShvX(E∞-Alg(C ))
is an equivalence.
In other words, commutative factorization algebras are cosheaves (in E∞-Alg).
Remark 34. In view of Proposition 48, one can think general factorization algebras
as non-commutative cosheaves.
92


## Page 93


Combining Proposition 48, Proposition 47 and Theorem 10, we obtain:
Corollary 21. Let F ∈Faclc
X (E∞-Alg) be a locally constant commutative factor-
ization algebra on X. Then
Z
X A ∼= C H X(F)
where C H X(F) is the (derived) global section of the cosheaf which to any open
U included in an euclidean Disk D associates the derived Hochschild homology
CHU(F(D)).
9
Complements on factorization algebras
In this Section, we give several proofs of results, some of them probably known by
the experts, about factorization algebras that we have postponed and for which we
do not know any reference in the literature.
9.1
Some proofs related to the locally constant condition and the push-
forward
Proof of Propositions 13 and 24.
Let U ⊂D ⊂M be an inclusion of open disks;
we need to prove that F(U) →F(D) is a quasi-isomorphism. We can assume
D = Rn (by composing with a homeomorphism); the proof in the stratiﬁed case
is similar to the non-stratiﬁed one by replacing Rn with Ri × [0,+∞)n−i. We ﬁrst
consider the case where F|U is locally constant and further, that U is an euclidean
disk (with center x and radius r0). Denote D(y,r) an euclidean open disk of center
y and radius r > 0 and let
T+ := sup(t ∈R, such that ∀r0
2 ≤s < t, F(D(x, r0
2 ) →F(D(x,s)) is an equivalence).
By assumption T+ ≥r0. We claim that T = +∞. Indeed, let T be ﬁnite and such
that , F(D(x, r0
2 ) →F(D(x,s)) is an equivalence for all s < T. We will prove that
T can not be equal to T+. Every point y on the sphere of center x and radius T has
a neighborhood in which F is locally constant. In particular, there is a number
εy > 0, an open angular sector S[0,T+εy) of length T +εy and angle θy containing y
such that F|S(T−εy,T+εy) is locally constant. Here, S(τ,γ) denotes the restriction of the
angular sector to the band containing numbers of radius lying in (τ,γ).
We ﬁrst note that S[0,T+εy) has a factorizing cover Ay consisting of open angular
sectors of the form S(T−τ,T+εy) (0 < τ ≤εy) and S[0,κ) (0 < κ < T); there is an
induced similar cover Ay ∩U of S[0,T) given by the angular sectors of the form
S(T−τ,T) (0 < τ ≤εy) and S[0,κ) (0 < κ < T). The structure maps F(S(T−τ,T)) →
F(S(T−τ,T+εy)) induce a map of ˇCech complex ψy : ˇC(Ay ∩U,F) →ˇC(Ay,F) so
93


## Page 94


that the following diagram is commutative:
ˇC(Ay ∩U,F)
ψy
/
≃

ˇC(Ay,F)
≃

F(S[0,T))
/ F(S[0,T+εy))
.
(54)
Since the map S(T−τ,T+εy) →S(T−τ,T+εy) is the inclusion of a sub-disk inside a
disk in S(T−εy,T+εy), it is a quasi-isomorphism and, thus, so is the map ψy : ˇC(Ay ∩
U,F) →ˇC(Ay,F). It follows from diagram (54) that the structure map F(S[0,T)) →
F(S[0,T+εy)) is a quasi-isomorphism. In the above proof, we could also have taken
any angle θ ≤θy or replaced εy by any ε ≤εy without changing the result.
By compactness of the sphere of radius T, we can thus ﬁnd an ε > 0 and a
θ > 0 such that the structure map F(S ∩U) →F(S) is a quasi-isomorphism for
any angular sector S around x of radius r = T +ε′ < T +ε and arc length φS < θ.
The collection of such angular sectors S is a (stable by intersection) factorizing
basis of the disk D(x,T + ε′) while the collection of sectors S ∩U is a (stable by
intersection) factorizing basis of the disk D(x,T). Further, we have proved that
the structure maps F(S ∩U) →F(S) is a quasi-isomorphism for any such S. It
follows that the map F(D(x,T)) →F(D(x,T +ε′) is a quasi-isomorphism (since
again the induced map in between the ˇCech complexes associated to this two covers
is a quasi-isomorphism). It follows that T+ > T for any ﬁnite T hence is inﬁnite as
claimed above. In particular, the canonical map F(D(x,T)) →F(D(x,T +r)) is
a quasi-isomorphism for any r ≥0.
Now, since the collection of disks of radius T > 0 centered at x is a factoriz-
ing cover of Rn, we deduce that F(D(x,T)) →F(Rn) is a quasi-isomorphism.
Indeed, ﬁx some R > 0 and let jR : x + y 7→x + R/(R −|y|)y be the homothety
centered at x mapping D(x,R) homeomorphically onto Rn. The map jR is a bi-
jection between the set DR of (euclidean) sub-disks of D(x,R) centered at x and
the set D of all (euclidean) disks of Rn centered at x. For any disk centered at x,
the inclusion D(x,T) ,→D(x, jR(T)) yields a quasi-isomorphism F(D(x,T)) →
F(D(x, jR(T)). If α = {D(x,r0),...,D(x,ri)} ∈(PDR)i+1, we thus get a quasi-
isomorphism
F(α) ∼= F

D
 x,min(rj, j = 0...i)

≃
−→F

D
 x,min(jR(rj), j = 0...i)

∼= F(jR(α)).
Assembling those for all α’s yields a quasi-isomorphism ˇC(DR,F)
≃
−→ˇC(D,F)
which ﬁt into a commutative diagram
ˇC(DR,F)
≃

≃
/ ˇC(D,F)
≃

F(D(x,R))
/ F(Rn)
94


## Page 95


whose vertical arrows are quasi-isomorphisms since F is a factorization algebra.
It follows that the lower horizontal arrow is a quasi-isomorphism as claimed.
We are left to prove the result for U ,→D = Rn when U is not necessarily an
euclidean disk. Choose an euclidean open disk ˜D inside U small enough so that
F| ˜D is locally constant. Let h : ˜D ∼= Rn be an homothety (with the same center as
˜D) identifying ˜D and Rn. Then ˜U := h−1(U) ⊂D ⊂U is an open disk homothetic
to U. So that by the above reasoning (after using an homeomorphism between
U and an euclidean disk Rn) we have that the structure map F( ˜U) →F(U) is
a quasi-isomorphism as well. Since F| ˜D is locally constant, the structure map
F( ˜U) →F( ˜D) is a quasi-isomorphism. Now, Proposition 13 follows from the
commutative diagram
F( ˜U)
≃
/
≃

F(U)
#
F( ˜D)
≃
/
;
F(D)
which implies that the structure map F(U) →F(D) is a quasi-isomorphism.
Proof of Proposition 18.
First we check that if F is a factorization algebra on
X ×Y and U ⊂X is open, then π1∗(F(U)) is a factorization algebra over Y. If V
is a factorizing cover of an open set V ⊂Y, then {U}×V is a factorizing cover of
U ×V and the ˇCech complex ˇC
 V ,π1∗F(U)

is equal to ˇC({U}×V ,F). Hence
the natural map ˇC
 V ,π1∗F(U)

→π1∗(F)(U,V) factors as
ˇC
 V ,π1∗F(U)

= ˇC({U}×V ,F) →F(U ×V) = π1∗(F)(U,V).
It is a quasi-isomorphism since F is a factorization algebra. We have proved that
π1∗(F) ∈PFacX(FacY). To show that π1∗(F) ∈FacX(FacY), we only need to
check that for every open V ⊂Y, and any factorizing cover U of U, the natural map
ˇC
 U ,π1∗(F)(−,V)

→π1∗(F)(U,V) is a quasi-isomorphism, which follows by
the same argument. Hence π1∗factors as a functor π1∗: FacX×Y −→FacX(FacY).
When F is locally constant, Proposition 15 applied to the ﬁrst and second
projection implies that π1∗(F) ∈Faclc
X (Faclc
Y ).
Now we build an inverse of π1∗in the locally constant case. Let B be in
FacX(FacY). A (stable by ﬁnite intersection) basis of neighborhood of X ×Y is
given by the products U ×V, with (U,V) ∈C V (X) × C V (Y) where C V (X),
C V (Y) are bounded geodesically convex neighborhoods (for some choice of Rie-
mannian metric on X and Y). Thus by § 5.2, in order to extend B to a factoriza-
tion algebra on X ×Y, it is enough to prove that the rule (U ×V) 7→B(U)(V)
(where U ⊂X, V ⊂Y) deﬁnes an C V (X) × C V (Y)-factorization algebra.
If
U ×V ∈C V (X) × C V (Y), then U and V are canonically homeomorphic to Rn
and Rm respectively. Now, the construction of the structure maps for opens in
95


## Page 96


C V (U) × C V (V) restricts to proving the result for B|U×V ∈Faclc
Rn(Faclc
Rm). By
Theorem 9, FacRd ∼= Ed-Alg, hence by Dunn Theorem 11 below, we have that
Faclc
Rn+m
π1∗
−→Faclc
Rn(Faclc
Rm) is an equivalence which allows to deﬁne a C V (X) ×
C V (Y)-factorization algebra structure associated to B. We denote j(B) ∈FacX×Y
the induced factorization algebra on X ×Y. Note that j(B) is locally constant,
since, again, the question reduces to Dunn Theorem.
It remains to prove that j : Faclc
X (Faclc
Y ) →FacX×Y is a natural inverse to π1∗.
This follows by uniqueness of the factorization algebra extending a factorization
algebra on a factorizing basis, that is, Proposition 17.
9.2
Complements on § 6.2
Here we collect the proofs of statements relating factorization algebras and inter-
vals.
Proof of Proposition 27.
The (sketch of) proof is extracted from the excision
property for factorization algebras in [GTZ2]. By deﬁnition of a Diskfr
1 -algebra,
a factorization algebra G on R carries a structure of Disk fr
1 -algebra (by simply
restricting the value of G to open sub-intervals, just as in Remark 23).
Similarly, if G is a factorization algebra on [0,+∞), it carries a structure of a
Disk fr
1 -algebra and a (pointed) right module over it, while a factorization algebra
on (−∞,0] carries the structure of a left (pointed) module over a Diskfr
1 -algebra
(see Deﬁnition 36). It follows that a factorization algebra over the closed interval
[0,1] determines an E1-algebra A and pointed left module M ℓand pointed right
module M r over A .
By strictiﬁcation we can replace the E1-algebra and modules by differential
graded associative ones so that we are left to the case of a factorization algebra
F on [−1,1] which, on the factorizing basis I of [0,1], is precisely the I -
prefactorization algebra F deﬁned before the Proposition 27.
Now, we are left to prove that, for any A,Mℓ,Mr,mr,mℓ, F is a I -factorization
algebra, and then to compute its global section F([0,1]). Theorem 9 implies that
the restriction FA of F to (0,1) is a factorization algebra. In order to conclude we
only need to prove that the canonical maps
ˇC
 U[0,1),F)

−→F([0,1)) = Mr,
ˇC
 U(0,1],F)

−→F((0,1]) = Mℓ
and
ˇC
 U[0,1],F)

−→F([0,1]) ∼= Mr L⊗
A Mℓ
are quasi-isomorphisms. Here, U[0,1] is the factorizing covers given by all opens
Ut := [0,1]\{t} where t ∈[0,1] (in other words by the complement of a singleton).
Similarly, U[0,1), U(0,1] are respectively covers given by all opens Uℓ
t := ([0,1)\{t}
where t ∈[0,1) and all opens Ur
t := (0,1]\{t} where t ∈(0,1].
96


## Page 97


The proof in the 3 cases are essentially the same so we only consider the case
of the opens Ut. Since Mr L⊗
A Mℓ∼= Mr ⊗
A B(A,A,A)⊗A Mℓwhere B(A,A,A) is the
two-sided Bar construction of A, it is enough to prove the result for Mr = Mℓ= A
in which case we are left to prove that the canonical map
ˇC
 U[0,1],F)

−→A
L⊗
A A ∼= B(A,A,A)
≃
−→A
is an equivalence.
Any two open sets in U[0,1] intersect non-trivially so that the set PU are sin-
gletons. We have F(Ut) ∼= F([−1,t))⊗F((t,1]) which is A⊗A if t ̸= ±1 and is
A⊗k or k ⊗A if t = 1 or t = −1. More generally,
F(Ut0,...,Utn,U±1) ∼= F(Ut0,...,Utn)⊗k.
Further, if 0 < t0 < ··· < tn < 1, then F(Ut0,...,Utn) ∼= A⊗A⊗n ⊗A and the struc-
ture map F(Ut0,...,Utn) →F(Ut0,...,c
Uti,...,Utn) is given by the multiplication
a0 ⊗···⊗an+1 7→a0 ⊗···(aiai+1)⊗···⊗an+1.
This identiﬁes the ˇCech complex ˇC
 U ,F

with a kind of parametrized analogue
of the standard two sided Bar construction with coefﬁcients in A. We have canoni-
cal maps
φt : F(Ut) ∼= F([−1,t))⊗F((t,1]) →F([−1,1))⊗F((−1,1]) ∼= A⊗A →A
induced by the multiplication in A.
The composition
L
Ur,Us∈PU
F(Ur,Us)[1] →
L
Ut∈PU
F(Ut)[0] →A is the zero map so that we have a map of (total) chain com-
plexes: η : ˇC
 U ,F

→A. In order to prove that η is an equivalence, we consider
the retract κ : A ∼= F(U1) ,→
L
Ut∈PU
F(Ut)[0] ,→ˇC
 U ,F

which satisﬁes η ◦κ =
idA. Let h be the homotopy operator on ˇC
 U ,F

deﬁned, on F(Ut0,...,Utn)[n],
by
n
∑
i=0
(−1)ist0,...,tn
i
: F(Ut0,...,Utn)[n] −→
M
Ur0,...Urn+1∈PU
F(Ur0,...,Urn+1)[n+1]
where, for 0 ≤i ≤n−1, st0,...,tn
i
is deﬁned as the suspension of the identity map
F(Ut0,...,Utn)[n] →F(Ut0,...,Utn)[n+1] ∼= F(Ut0,...,Uti,Uti,...,Utn)[n+1]
followed by the inclusion in the ˇCech complex.
Similarly, the map st0,...,tn
n
is deﬁned as the suspension of the identity map
F(Ut0,...,Utn)[n] →F(Ut0,...,Utn)[n+1] ∼= F(Ut0,...,Utn,U1)[n+1] (followed
by the inclusion in the ˇCech complex). Note that dh+hd = id −κ ◦η where d is
the total differential on ˇC
 U ,F

. It follows that η : ˇC
 U ,F

→A is an equiva-
lence.
97


## Page 98


Proof of Corollary 7.
The functor π1∗: Faclc
X×[0,+∞) →E1-RMod(Faclc
X ) is well-
deﬁned by Corollary 6 and Proposition 28. In order to check it is an equivalence, as
in the proof of Proposition 18, we only need to prove it when X = Rn, that is that,
if F ∈Faclc
[0,+∞)(Faclc
X ), then it is in the essential image of π1∗. By Proposition 18,
we can also assume that the restriction F|(0,+∞) is in π1∗(Faclc
Rn×(0,+∞)).
Let Iε be the factorizing cover of [0,+∞) consisting of all intervals with the
restriction that intervals containing 0 are included in [0,ε) note that Iτ ⊂Iε if ε > τ.
We can replace F by its ˇCech complex on Iε (for any ε) and thus by its limit over
all ε > 0, which we still denote F. As in the proof of Proposition 18, we only
need to prove that (U,V) 7→
 F(V)

(U) extends as a factorization algebra relative
to the factorizing basis of Rn × [0,+∞) consisting of cubes (with sides parallel to
the axes). The only difﬁculty is to deﬁne the prefactorization algebra structure on
this basis (since we already know it is locally constant, and thus will extend into a
factorization algebra). As noticed above, we already have such structure when no
cubes intersect Rn ×{0}. Given a ﬁnite family of pairwise disjoint cubes lying in
a bigger cube K ×[0,R) intersecting {0}, we can ﬁnd ε > 0 such that no cubes of
the family lying in Rn × (0,+∞) lies in the band Rn × [0,ε). The value of F on
each square containing Rn × {0} can be computed using the ˇCech complex asso-
ciated to Iε. This left us, in every such cube, with one term containing a summand
[0,τ) (τ ≤ε) and cubes in the complement. Now choosing the maximum of the
possible τ allows to ﬁrst maps (F(c))(d) to
 F(τ,R)

(K) for every cube c × d
in Rn × (τ,R) (since we already have a factorization algebra on Rn × (0,+∞)).
Then to maps all other summands to terms of the form F([0,τ))(d), then all of
them in F([0,τ))(K) and ﬁnally to evaluate the last two remaining summand in
F([0,R))(K) using the prefactorization algebra structure of F with respect to in-
tervals in [0,∞). This is essentially the same argument as in the proof of Corol-
lary 8.
9.3
Complements on § 6.3
Here we collect proofs of statements relating factorization algebras and En-modules.
Proof of Theorem 12
The functoriality is immediate from the construction. Let
Fin∗be the ∞-category associated to the category Fin∗of pointed ﬁnite sets. If O
is an operad, the ∞-category O-ModA of O-modules80 over an O-algebra A is the
category of O-linear functors O-ModA := MapO(O∗,Chain(k)). Here, following
the notations of § 10.2, O is the ∞-categorical enveloppe of O as in [L3] and O∗:=
O ×Fin Fin∗. There is an natural ﬁbration πO : O-Mod −→O-Alg whose ﬁber at
A ∈O-Alg is O-ModA.
Let Disk be the set of all open disks in Rn. Recall from Remark 24 that Disk-
prefactorization algebras are exactly algebras over the operad Disk(Rn) and that
80in Chain(k)
98


## Page 99


locally constant Disk-prefactorization algebras are the same as locally constant fac-
torization algebras on Rn (Proposition 12). The map of operad Disk(Rn) →ERn
of [L3, §5.2.4] induces a fully faithful functor En-Alg →Disk(Rn)-Alg and thus a
functor
˜ψ : En-Mod −→Disk(Rn)-Mod −→Disk(Rn)-Alg.
The map ˜ψ satisﬁes that, for every convex subset C ⊂Rn, one has
˜ψ(M)(C) = M(C) = FM(C).
By deﬁnition, ˜ψ ◦can : En-Alg →Disk(Rn)-Alg is the composition
En-Alg −→Faclc
Rn −→Disk(Rn)-Alg.
Hence, the commutativity of the diagram in the Theorem will follow automatically
once we have proved that ˜ψ factors as a composition of functors
˜ψ : En-Mod
ψ
−→Faclc
Rn∗−→Disk(Rn)-Alg.
(55)
Assuming for the moment that we have proved that ˜ψ factors through Faclc
Rn∗, let
us show that ψ is fully faithful. By deﬁnition of categories of modules, we have a
commutative diagram
En-Mod
πEn

/ Disk(Rn)-Mod
πDisk(Rn)

En-Alg
/ Disk(Rn)-Alg
whose bottom arrow is a fully faithful embedding by [L3, §5.2.4]. Since the map-
ping spaces of F ∈Faclc
X are the mapping spaces of the underlying prefactorization
algebra, the map Faclc
Rn∗→Disk(Rn)-Alg is fully faithful, and we are left to prove
that
˜ψ : MapEn-Mod(M,N) →MapDisk(Rn)-Alg( ˜ψ(M), ˜ψ(N))
is an equivalence for all M ∈En-ModA and N ∈En-ModB. The ﬁber at (the image
of) an En-algebra A of Disk(Rn)-Mod →Disk(Rn)-Alg is the (homotopy) pullback
Disk(Rn)-ModA := Disk(Rn)-Alg/A ×h
Disk(Rn\{0})-Alg/A IsoDisk(Rn\{0})-Alg(A).
Here we write Disk(Rn)-Alg/A for the ∞-category of Disk(Rn)-algebras under A
and IsoDisk(Rn)-Alg(A) its subcategory of objects A
f→B such that f is an equiva-
lence. In plain english, Disk(Rn)-ModA is the ∞-category of maps A
f→B (where
B runs through Disk(Rn)-Alg) whose restriction to Rn \{0} is an equivalence.
It is now sufﬁcient to prove, given En-algebras A and B (identiﬁed with ob-
jects of Faclc
Rn) and two locally constant factorization algebras ˜ψ(M), ˜ψ(N) on Rn
∗
99


## Page 100


together with two maps of factorizations algebras f : A →˜ψ(M), g : B →˜ψ(N)
whose restrictions to Rn \{0} are quasi-isomorphisms, that the canonical map
MapDisk(Rn)-Alg(A,B)×h
MapDisk(Rn)-Alg(A, ˜ψ(N))MapDisk(Rn)-Alg( ˜ψ(M), ˜ψ(N))
−→MapDisk(Rn)-Alg( ˜ψ(M), ˜ψ(N))
(56)
is an equivalence. This pullback is the mapping space MapDisk(Rn)-Mod( ˜ψ(M), ˜ψ(N))
and the maps to MapDisk(Rn)-Alg(A, ˜ψ(N)) are induced by post-composition by g
and precomposition by f.
The ﬁber of the map (56) at Θ : ˜ψ(M) →˜ψ(N)) is the mapping space of
Disk(Rn)-algebras A τ→B such that, for any disk U ⊂Rn \ {0}, which is a sub-
disk of a disk D containing 0, the following diagram is commutative:
A(D)
τ(D)

A(U)
ρA
U,D
o
≃
f
/
τ(U)

˜ψ(M)(U)
Θ(U)

B(D)
B(U)
ρB
U,D
o
≃
g
/ ˜ψ(N)(U).
(57)
Here ρA
U,D and ρB
U,D are the structure maps of the factorization algebras associ-
ated to A and B. The right hand square of Diagram (57) shows that τ is uniquely
determined by Θ on every open disk in Rn \{0}.
Since A and B are locally constant factorization algebras on Rn, the maps ρA
U,D
and ρB
U,D are natural quasi-isomorphisms. It follows from the left hand square in
Diagram (57) that the restriction of τ to Rn \{0} also determines the map τ on Rn.
Hence the map (56) is an equivalence which concludes the proof that ψ is fully
faithful.
It remains to prove that ˜ψ factors through a functor ψ, that is that we have a
composition as written in (55). This amounts to prove that for any M ∈En-ModA
(that is M is an En-module over A), ˜ψ(M) is a locally constant factorization algebra
on the stratiﬁed manifold given by the pointed disk Rn
∗. Since the convex subsets
are a factorizing basis stable by ﬁnite intersection, we only have to prove this result
on the cover C V (Rn) (by Proposition 17 and Proposition 13).
Note that if V ∈C V (Rn) is a subset of Rn \ {0}, then ψ(M)|V lies in the
essential image of ψ ◦can(M)|V where ψ ◦can(M) is the functor inducing the
equivalence between En-algebras and locally constant factorization algebras on Rn
(Theorem 9). We denote FA := ψ ◦can(A) the locally constant factorization alge-
bra on Rn induced by A. In particular, the canonical map
ˇC(C V (V),FM) = ˇC(C V (V),FA) →FA(V) ∼= FM(V)
is a quasi-isomorphism and further, if U ⊂V is a sub disk, then FM(U) →FM(V)
is a quasi-isomorphism.
We are left to consider the case where V is a convex set containing 0. Let UV
be the cover of V consisting of all open sets which contains 0 and are a ﬁnite union
100


## Page 101


of disjoint convex subsets of V. It is a factorizing cover, and, by construction,
two open sets in UV intersects non-trivially since they contain 0. Hence PUV =
UV. Since UV ⊂PC V (V), we have a diagram of short exact sequences of chain
complexes
0
/ ˇC(UV,FM)
iM
/ ˇC(C V (V),FM)
/ ˇC(C V (V),FM)/ ˇC(UV,FM)
/
≃

0
0
/ ˇC(UV,FA)
iA
/ ˇC(C V (V),FA)
/ ˇC(C V (V),FA)/ ˇC(UV,FA)
/ 0
where the vertical equivalence follows from the fact that FM(U) ∼= FA(U) ifU is a
convex set not containing 0. Moreover, since UV is a factorizing cover of V and FA
a factorization algebra, iA is a quasi-isomorphism, hence ˇC(C V (V),FA)/ ˇC(UV,FA)
is acyclic. It follows that iM : ˇC(UV,FM) →ˇC(C V (V),FM) is a quasi-isomorphism
as well.
We are left to prove that the canonical map ˇC(UV,FM) →F(M) ∼= M is a
quasi-isomorphism. Note that for any U ∈UV, we have FM(U) ∼= M ⊗L
A FA(U).
We deduce that ˇC(UV,FM) ∼= M ⊗L
A ˇC(UV,FA) as well. The chain map
M ⊗L
A ˇC(UV,FA) ∼= ˇC(UV,FM) −→F(M) ∼= M ⊗L
A A
is an equivalence since it is obtained by tensoring (by M over A) the quasi-isomorphism
ˇC(UV,FA) →FA(V) ∼= A (which follows from the fact that FA is a factorization
algebra).
It remains to prove that FM(U) →FM(V) is a quasi-isomorphism if both U,
V are convex subsets containing 0. This is immediate since M(U) →M(V) is an
equivalence by deﬁnition of an En-module over A.
Proof of Corollary 8.
By Theorem 12, we have a commutative diagram
En-Mod
πEn

/ Faclc
Rn∗×h
Faclc
Rn\{0} Faclc
Rn

En-Alg
/ Faclc
Rn
with fully faithful horizontal arrows. Since En-Alg →Faclc
Rn is an equivalence, we
only need to prove that, for any En-algebra A, the induced fully faithful functor
En-ModA −→Faclc
Rn∗×Faclc
Rn\{0} {A} between the ﬁbers is essentially surjective81.
Let M be a locally constant factorization algebra on Rn
∗such that M|R\{0} is
equal to A|Rn\{0} where A is the factorization algebra associated to A (by Theo-
rem 9). Recall that N : Rn →[0,+∞) is the euclidean norm map. Lemma 7 implies
that N∗(M ) is is locally constant on the stratiﬁed half-line [0,+∞) and thus equiv-
alent to a right module over the E1-algebra N∗(M )(Rn \ {0}) ∼= A (Rn \ {0}) ∼=
R
Sn−1×R A.
81that is we are left to prove Corollary 9
101


## Page 102


By homeomorphism invariance of (locally constant) factorization algebras, we
can replace Rn by the unit open disk Dn of Rn in the above analysis. We also
denote Dn
∗the disk Dn viewed as a pointed space with base point 0. We now use
this observation to deﬁne a structure of En-module over A on M := M (Dn) =
N∗(M )
 [0,1)

. It amount to deﬁne, for any ﬁnite set I, continuous maps (compat-
ible with the structure of the operad of little disks of dimension n)
Rect∗

Dn
∗
aa
i∈I
Dn
,Dn
∗

−→MapChain(k)
 M ⊗A⊗I,M

≃
−→MapChain(k)

M ⊗
Z
Dn A
⊗I
,M

where Rect∗is the space of rectilinear embeddings which maps the center of the
ﬁrst copy Dn
∗to the center of Dn
∗(i.e. preserves the base point of Dn). Let IN be the
map that sends an element f ∈Rect∗
 Dn ` `
i∈I Dn
,Dn
to the smallest open
sub-interval IN(f) ⊂(0,1) which contains N
 f
 `
i∈I Dn
, that is the smallest
interval that contains the image of the non-pointed disks. By deﬁnition IN is con-
tinuous (meaning the lower and the upper bound of IN(f) depends continuously
of f) and its image is disjoint from the image N(Dn
∗) of the pointed copy of Dn.
Similarly we deﬁne r(f) to be the radius of f(Dn
∗). We have a continuous map
˜N : Rect∗

Dn
∗
a a
i∈I
Dn
,Dn
∗

−→Rect

[0,1)
a
(0,1),[0,1)

given by ˜N(f)
 (0,1)

= IN(f) and ˜N(f)
 [0,1)

= [0,r(f)). Since f(`
i∈I Dn) ⊂
Sn−1 ×(0,1) , we have the composition
ϒ : Rect∗

Dn
∗
a a
i∈I
Dn
,Dn
∗

−→Rect
a
i∈I
Dn,Sn−1 ×(0,1)

−→MapChain(k)
Z
Dn A
⊗I
,
Z
Sn−1×(0,1) A

where the ﬁrst map is induced by the restriction to `
i∈I Dn and the last one by
functoriality of factorization homology with respect to embeddings. We ﬁnally
deﬁne
µ : Rect∗

Dn
∗
a a
i∈I
Dn
,Dn
∗
 ˜N×ϒ
−→
Rect

[0,1)
a
(0,1),[0,1)

×MapChain(k)
Z
DnA
⊗I
,
Z
Sn−1×(0,1)A

−→
MapChain(k)

M ⊗
Z
Sn−1×(0,1)A, M

×MapChain(k)
Z
DnA
⊗I
,
Z
Sn−1×(0,1)A

idM⊗◦
−→MapChain(k)

M ⊗
Z
Dn A
⊗I
, M

102


## Page 103


where the second map is induced by the E1-module structure of M = N∗(M )([0,1))
over
R
Sn−1×(0,1) A and the last one by composition. That µ is compatible with the
action of the little disks operad follows from the fact that ϒ is induced by the En-
algebra structure of A and M is an E1-module over
R
Sn−1×(0,1) A. Hence, M is in
En-ModA.
We now prove that the factorization algebra ψ(M) is M . For all euclidean
disks D centered at 0, one has ψ(M)(D) = µ({D ,→Dn})(M) = M (D) and further
ψ(M)(U) = A (U) if U is a disk that does not contain 0. The D-prefactorization
algebra structure of ψ(M) (where D is the basis of opens consisting of all euclidean
disks centered at 0 and all those who do not contain 0) is precisely given by µ
according to the construction of ψ (see Theorem 12). Hence, by Proposition 17,
ψ(M) ∼= M and the essential surjectivity follows.
Proof of Proposition 29.
By [L3, §4.3], we have two functors i± : BiMod →
E1-Alg and the (homotopy) ﬁber of BiMod
(i−,i+)
−→E1-Alg×E1-Alg at a point (L,R)
is the category of (L,R)-bimodules which is equivalent to the category E1-LModL⊗Rop.
We have a factorization
Faclc
R∗
(j∗
−,j∗
+)
,
(j∗
±,(−N)∗)
/ BiMod
(i−,i+)/ E1-Alg×E1-Alg
Faclc
(−∞,0) ×Faclc
(0,+∞).
≃
O
(58)
We can assume that L,R are strict and consider the ﬁber
 Faclc
R∗

L,R := {FL,FR}×Faclc
(−∞,0)×Faclc
(0,+∞) Faclc
R∗
of (j∗
−, j∗
+) at the pair of factorization algebras (FL,FR) on (−∞,0), (0,+∞) cor-
responding to L, R respectively (using Proposition 27). The pushforward along
the opposite of the euclidean norm map gives the functor (−N)∗:
 Faclc
R∗

L,R →
E1-LModL⊗Rop.
We further have a locally constant factorization algebra G L,R
M
on R∗which is
deﬁned on the basis of disks by the same rule as for the open interval (for disks
included in a component R \ {0}) together with G L,R
M (α,β) = M for α < 0 < β.
For r < t1 < u1 ··· < tn < un < α < 0 < β < x1 < y1 < ··· < xm < ym < s, the
structure maps
 O
i=1...n
G L,R
M
 (ui,ti)

⊗G L,R
M
 (α,β)

⊗
 O
i=1...n
G L,R
M
 (ui,ti)

∼= L⊗n ⊗M ⊗R⊗m −→M ∼= G L,R
M
 (r,s)

are given by ℓ1 ⊗···⊗ℓn ⊗a⊗r1 ⊗···⊗rn 7→(ℓ1 ···ℓn)·a·(r1 ···rn).
One checks as in Proposition 27 that G L,R
M
is a locally constant factorization al-
gebra on R∗. The induced functor E1-LModL⊗Rop →Faclc
R∗is an inverse of (−N)∗.
103


## Page 104


Thus the ﬁber
 Faclc
R∗

L,R of (j∗
−, j∗
+) is equivalent to E1-LModL⊗Rop. It now fol-
lows from diagram (58) that the functor (j∗
±,(−N)∗) : Faclc
R∗∼= BiMod is an equiv-
alence.
Proof of Proposition 30.
We deﬁne a functor G : E1-RModA (Sn−1×R) →Faclc
Rn∗×Faclc
Rn\{0}
{A } (which will be an inverse of N∗) as follows. By Proposition 28 we have an
equivalence
E1-RModA (Sn−1×R) ∼= Faclc
[0,+∞) ×Faclc
(0,+∞) {N∗(A )}.
It is enough to deﬁne G as a functor from Faclc
[0,+∞) ×Faclc
(0,+∞) {N∗(A )} to locally
constant U -factorization algebras, where U is a (stable by ﬁnite intersections)
factorizing basis of Rn (by Proposition 17). We choose U to be the basis consisting
of all euclidean disks centered at 0 and all convex open subsets not containing 0.
Let R ∈Faclc
[0,+∞) ×Faclc
(0,+∞) {N∗(A )}. If U ∈U does not contains 0, then we set
G(R)(U) = A (U) and structure maps on open sets in U not containing 0 to be
the one of A ; this deﬁnes a locally constant factorization algebra on Rn \{0} since
A does.
We denote D(0,r) the euclidean disk of radius r > 0 and set G(R)(D(0,r)) =
R([0,ε)). Let D(0,r),U1,...,Ui be pairwise subsets of U which are sub-sets of an
euclidean disk D(0,s). Then, U1,...,Ui lies in Sn−1 ×(r,s). Denoting respectively
ρA , ρR the structure maps of the factorization algebras A ∈Faclc
Sn−1×(0,+∞) and
R ∈Faclc
[0,+∞), we have the following composition
G(R)
 D(0,r)

⊗G(R)(U1)⊗···⊗G(R)(Ui) ∼= R
 [0,r)

⊗A (U1)⊗···⊗A (Ui)
id⊗ρA
U1,...,Ui,Sn−1×(r,s)
−→
R
 [0,r)

⊗A
 Sn−1 ×(r,s)
 ∼= R
 [0,r)

⊗N∗(A )
 (r,s)

ρR
[0,r),(r,s),[0,s)
−→
R
 [0,s)

= G(R)
 D(0,s)

.
(59)
The maps (59) together with the structure maps of A|Rn\{0} ∼= R|Rn\{0} deﬁne the
structure of a U -factorization algebra since R and A are factorization algebras.
The maps G(R)
 D(0,r)

→G(R)
 D(0,s)

are quasi-isomorphisms since R
is locally constant. Since the maps (59) only depend on the structure maps of R
and A , the rule R 7→G(R) extends into a functor
G : E1-RModA (Sn−1×R) ∼= Faclc
[0,+∞) ×Faclc
(0,+∞) {N∗(A )} →Faclc
Rn∗×Faclc
Rn\{0} {A }.
In order to check that N∗◦G is equivalent to the identity functor of E1-RModA (Sn−1×R)
it is sufﬁcient to check it on the basis of opens of [0,+∞) given by the open intervals
and the half-closed intervals [0,s) for which the result follows from the deﬁnition
of the maps (59). Similarly, one can check that G◦N∗is equivalent to the identity
of Faclc
Rn∗×Faclc
Rn\{0} {A } by checking it on the open cover U .
104


## Page 105


10
Appendix
In this appendix, we brieﬂy collect several notions and results about ∞-categories
and (∞-)operads and in particular the En-operad and its algebras and their modules.
10.1
∞-category overview
There are several equivalent (see [Be1]) notions of (symmetric monoidal) ∞-categories
and the reader shall feel free to use its favorite ones in these notes though we choose
Deﬁnition 29. In this paper, an ∞-category means a complete Segal spaces [R, L2].
Other appropriate models82 are given by Segal category [HS, TV1] or Joyal
quasi-categories [L1]. Almost all ∞-categories in these notes arise as some (de-
rived) topological (or simplicial or dg) categories or localization of a category with
weak equivalences. They carry along derived functors (such as derived homomor-
phisms) lifting the usual derived functors of usual derived categories. We recall
below (examples 59 and 58) how to go from a model or topological category to an
∞-category.
Following [R, L2], a Segal space is a functor X• : ∆op →Top, that is a sim-
plicial space83, which is Reedy ﬁbrant (see [H]) and satisﬁes the the condition that
for every integers n ≥0, the natural map (induced by the face maps)
Xn −→X1 ×X0 ×X1 ×X0 ···×X0 X1
(60)
(where there is n copies of X1) is a weak homotopy equivalence. 84
Associated to a Segal space X• is a (discrete) category ho(X•) with objects
the points of X0 and morphisms ho(X•)(a,b) = π0
 {a} ×X0 X1 ×X0 {b}

. We call
ho(X•) the homotopy category of X•.
A Segal space X• is complete if the canonical map X0 →Iso(X1) is a weak
equivalence, where Iso(X1) is the subspace of X1 consisting of maps f whose class
[f] ∈ho(X•) is invertible.
There is a simplicial closed model category structure, denoted S eS p on the
category of simplicial spaces such that a ﬁbrant object in S eS p is precisely a
Segal space. The category of simplicial spaces has another simplicial closed model
structure, denoted C S eS p, whose ﬁbrant objects are precisely complete Segal
spaces [R, Theorem 7.2]. Let R : S eS p →S eS p be a ﬁbrant replacement
82Depending on the context some models are more natural to use than others
83here a space can also mean a simplicial set and it is often technically easier to work in this
setting
84Alternatively, one can work out an equivalent notion fo Segal spaces which forget about the
Reedy ﬁbrancy condition and replace condition (60) by the condition that the following natural map
is is a weak homotopy equivalence:
Xn −→holim
 X1
d0
−→X0
d1
←−X1
d0
−→···
d1
←−X1
d0
−→X0
d1
←−X1

.
105


## Page 106


functor andb· : SeSp →C S eS p be the completion functor that assigns to a Segal
space X• an equivalent complete Segal space bX•. The composition X• 7→\
R(X•)
gives a ﬁbrant replacement functor LC S eS p from simplicial spaces to complete
Segal spaces.
Example 57 (Discrete categories). Let C be an ordinary category (which we also
referred to as a discrete category since its Hom-spaces are discrete). Its nerve is a
Segal space which is not complete in general. However, one can form its classifying
diagram, abusively denoted N(C ) which is a complete Segal space [R]. This is the
∞-category associated to C .
By deﬁnition, the classifying diagram is the simplicial space n 7→
 N(C )

n :=
N•(Iso(C [n])) given by the ordinary nerves (or classifying spaces) of Iso(C [n]) the
subcategories of isomorphisms of the categories of n-composables arrows in C .
Example 58 (Topological category). Let T be a topological (or simplicial) cate-
gory. Its nerve N•(T) is a simplicial space. Applying the complete Segal Space
replacement functor we get the ∞-category T∞:= LC S eS p(N•(T)) associated to
T.
Note that there is a model category structure on topological category which
is Quillen equivalent85 to C S eS p, ([Be1]). The functor T 7→T∞realizes this
equivalence. If T is a discrete topological category (in other words an usual cat-
egory viewed as a topological category), then T∞is equivalent to the ∞-category
N(T) associated to T in Example 57 ([Be2]). It is worth mentioning that the func-
tor T 7→T∞is the analogue for complete Segal spaces of the homotopy coherent
nerve ([L1]) for quasi-categories, see [Be3] for a comparison.
Example 59 (The ∞-category of a model category). Let M be a model category
and W be its subcategory of weak-equivalences. We denote LH(M ,W ) its ham-
mock localization, see [DK]. One of the main property of LH(M ,W ) is that it
is a simplicial category and that the (usual) category π0(LH(M ,W )) is the ho-
motopy category of M . Further, every weak equivalence has a (weak) inverse
in LH(M ,W ). If M is a simplicial model category, then for every pair (x,y) of
objects the simplicial set of morphisms HomLH(M ,W )(x,y) is naturally homotopy
equivalent to the function complex MapM (x,y).
By construction, the nerve N•(LH(M ,W )) is a simplicial space. Applying the
complete Segal Space replacement functor we get
Proposition 49. [Be1]The simplicial space L∞(M ) := LC S eS p(N•(LH(M ,W )))
is a complete Segal space, which is the ∞-category associated to M .
Note that the above construction extends to any category with weak equiva-
lences.
Also, the limit and colimit in the ∞-category L∞(M ) associated to a closed
model category M can be computed by the homotopy limit and homotopy colimit
85more precisely there is a zigzag of Quillen equivalences in between them; zigzag which goes
through the model category structure of Segal categories.
106


## Page 107


in M , that is by using ﬁbrant and coﬁbrant resolutions. The same is true for derived
functors. For instance a right Quillen functor f : M →N has a lift Lf : L∞(M ) →
L∞(N ).
Remark 35. There are other functors that yields a complete Segal space out of a
model category. For instance, one can generalize the construction of Example 57.
For M a model category and any integer n, let M [n] be the (model) category of n-
composables morphisms, that is the category of functors from the poset [n] to M .
The classiﬁcation diagram of M is the simplicial space n 7→N•(W e(M [n])) where
W e(M [n]) is the subcategory of weak equivalences of M [n]. Then taking a Reedy
ﬁbrant replacement yields another complete Segal space N•(W e(M [n]))f ([Be2,
Theorem 6.2], [R, Theorem 8.3]). It is known that the Segal space N•(W e(M [n]))f
is equivalent to L∞(M ) = LC S eS p(N•(LH(M ,W ))) ([Be2]).
Deﬁnition 30. The objects of an ∞-category C are the points of C0. By deﬁnition,
an ∞-category has a space (and not just a set) of morphisms
MapC(x,y) := {x}×h
C0 C1 ×h
C0 {y}
between two objects x and y. A morphism f ∈MapC(x,y) is called an equivalence
if its image [f] ∈Mapho(C)(x,y) is an isomorphism.
From Example 59, we get an ∞-category of ∞-categories, denoted ∞-Cat,
whose morphisms are called ∞-functors (or just functors for short). An equiva-
lence of ∞-categories is an equivalence in ∞-Cat in the sense of Deﬁnition 30.
The model category of complete Segal spaces is cartesian closed [R] hence
so is the ∞-category ∞-Cat. In particular, given two ∞-categories C , D we have
an ∞-category Fun(C ,D) of functors86 from C to D. There is an natural weak
equivalence of spaces:
Map∞-Cat
 B,Fun(C ,D
 ≃→Map∞-Cat
 B ×C ,D

.
(61)
Remark 36 (the case of simplicial model categories). When M is a simplicial
closed model category, there are natural equivalences ([R]) of spaces
MapL∞(M )(x,y) ∼= Map LH(M ,W )

∞
(x,y) ∼= MapLH(M ,W )(x,y) ∼= MapM (x,y)
where the right hand side is the function complex of M and x,y two objects. The
ﬁrst two equivalences also hold for general model categories ([Be1]). In particular,
the two constructions of an ∞-category associated to a simplicial model category,
either viewed as topological category as in Example 58, or as a model category as
in Example 59, are equivalent:
Proposition 50. Let M be a simplicial model category. Then M∞∼= L∞(M ).
86computed from the Hom-space in the category of simplicial spaces using the ﬁbrant replace-
ment functor LC S eS p
107


## Page 108


Let I be the ∞-category associated to the trivial category ∆1 = {0} →{1}
which has two objects and only one non-trivial morphism. We have two maps
i0,i1 : {pt} →I from the trivial category to I which respectively maps the object
pt to 0 and 1.
Deﬁnition 31. Let A be an object of an ∞-category C . The ∞-category CA of
objects over A is the pullback
CA
/

Fun(I,C )
i∗
1

{A}
/ C .
The ∞-category AC of objects under A is the pullback
CA
/

Fun(I,C )
i∗
0

{A}
/ C .
Informally, the ∞-category CA is just the category of objects B ∈C equipped
with a map f : B →A in C .
There is a notion of symmetric monoidal ∞-category generalizing the classical
notion for discrete categories. There are several equivalent way to deﬁne this no-
tion, see [L3, L1, TV3] for details. Let Γ be the skeleton of the category Fin∗of
ﬁnite pointed sets, that is the subcategory spanned by the objects n+ := {0,...,n},
n ∈N. For i = 1...n, let si : n+ →1+ be the map sending i to 1 and everything else
to 0.
Deﬁnition 32. A symmetric monoidal ∞-category is a functor T ∈Fun(Γ,∞-Cat)
such that the canonical map T(n+)
∏n
i=0 si
−→
 T(1+)
n is an equivalence. The full
sub-category of Fun(Γ,∞-Cat) spanned by the symmetric monoidal categories is
denoted ∞-Cat⊗. Its morphisms are called symmetric monoidal functors. Further
∞-Cat⊗is enriched over ∞-Cat.
A symmetric monoidal category T : Γ →∞-Cat will usually be denoted as
(T ,⊗) where T := T(1). If C : Γ →∞-Cat and D : Γ →∞-Cat are symmetric
monoidal categories, we will denote Fun⊗(C ,D) the ∞-categories of symmetric
monoidal functors.
Equivalently, a symmetric monoidal category is an E∞-algebra object in the ∞-
category ∞-Cat. An (∞-)category with ﬁnite coproducts has a canonical structure
of symmetric monoidal ∞-category and so does a category with ﬁnite products.
Example 60 (The ∞-category Top). Applying the above procedure(Example 59)
to the model category of simplicial sets, we obtain the ∞-category sSet. Similarly,
the model category of topological spaces yields the ∞-category Top of topological
108


## Page 109


spaces. By Remark 36, we can also apply Example 58 to the standard enrichment of
these categories into topological (or simplicial) categories to construct (equivalent)
models of sSet and Top.
Since the model categories sSet and Top are Quillen equivalent [GJ, H], their
associated ∞-categories are equivalent. The left and right equivalences |−| : sSet
∼
⇄
∼
Top : ∆•(−) are respectively induced by the singular set and geometric realization
functors. The disjoint union of simplicial sets and topological spaces make sSet
and Top into symmetric monoidal ∞-categories.
The above analysis also holds for the pointed versions sSet∗and Top∗of the
above ∞-categories (using the model categories of these pointed versions [H]).
Example 61 (Chain complexes). The model category of (unbounded) chain com-
plexes over k (say with the projective model structure) [H] yields the ∞-category
of chain complexes Chain(k)(Example 59).
The mapping space between two
chain complex P∗,Q∗is equivalent to the geometric realization of the simplicial
set n 7→HomChain(k)(P∗⊗C∗(∆n),Q∗) where HomChain(k) stands for morphisms of
chain complexes. It follows from Proposition 50, that one can also use Example 58
applied to the category of chain complexes endowed with the above topological
space of morphisms to deﬁne Chain(k). In particular a chain homotopy between
two chain maps f,g ∈MapChain(k)(P∗,Q∗) is a path in MapChain(k)(P∗,Q∗).
In fact, ho(Chain(k)) ∼= D(k) is the usual derived category of k-modules. The
(derived) tensor product over k yields a symmetric monoidal structure to Chain(k)
which will usually simply denote by ⊗. Note that Chain(k) is enriched over itself,
that is, for any P∗,Q∗∈Chain(k), there is an object RHomk(P∗,Q∗) ∈Chain(k)
together with an adjunction
MapChain(k)
 P∗⊗Q∗,R∗
 ∼= MapChain(k)
 P∗,RHomk(Q∗,R∗)

.
The interested reader can refer to [GH, L3] for details of ∞-categories enriched
over ∞-categories and to [GM, DS] for model categories enriched over symmet-
ric monoidal closed model categories (which is the case of the category of chain
complexes).
Example 62. In characteristic zero, there is a standard closed model category
structure on the category of commutative differential graded algebras (CDGA for
short), see [Hi, Theorem 4.1.1]. Its ﬁbrations are epimorphisms and (weak) equiva-
lences are quasi-isomorphisms (of CDGAs). We thus get the ∞-category CDGA of
CDGAs. The category CDGA also has a monoidal structure given by the (derived)
tensor product (over k) of differential graded commutative algebras, which makes
CDGA a symmetric monoidal model category. Given A,B ∈CDGA, the mapping
space MapCDGA(A,B) is the (geometric realization of the) simplicial set of maps
[n] 7→Homdg-Algebras(A,B⊗Ω∗(∆n)) (where Ω∗(∆n) is the CDGA of forms on the
n-dimensional standard simplex and Homdg-Algebras is the module of differential
graded algebras maps). It has thus a canonical enrichment over chain complexes.
The model categories of left modules and commutative algebras over a CDGA
A yield the ∞-categories E1-LModA and CDGAA . The base change functor lifts
109


## Page 110


to a functor of ∞-categories. Further, if f : A →B is a weak equivalence, the nat-
ural functor f∗: E1-LModB →: E1-LModA induces an equivalence E1-LModB
∼→
E1-LModA of ∞-categories since it is induced by a Quillen equivalence.
Moreover, if f : A →B is a morphism of CDGAs, we get a natural func-
tor f ∗: E1-LModA →E1-LModB, M 7→M ⊗L
A B, which is an equivalence of ∞-
categories when f is a quasi-isomorphism, and is a (weak) inverse of f∗(see [TV2]
or [KM]). The same results applies to monoids in E1-LModA that is to the cate-
gories of commutative differential graded A-algebras.
10.2
En-algebras and En-modules
The classical deﬁnition of an En-algebra (in chain complexes) is an algebra over
any En-operad in chain complexes, that is an operad weakly homotopy equivalent
to the chains on the little (n-dimensional) cubes operad (Cuben(r))r≥0 ([Ma]). Here
Cuben(r) := Rect

ra
i=1
(0,1)n,(0,1)n
is the space of rectilinear embeddings of r-many disjoint copies of the unit open
cube in itself. It is topologized as the subspace of the space of all continuous
maps. By a rectilinear embedding, we mean a composition of a translation and
dilatations in the direction given by a vector of the canonical basis of Rn. In other
words, Cuben(r) is the conﬁguration space of r-many disjoint open rectangles87
parallel to the axes lying in the unit open cube. The operad structure Cuben(r) ×
Cuben(k1)×···×Cuben(kr) →Cuben(k1+···+kr) is simply given by composition
of embeddings.
An En-algebra in chain complexes is thus a chain complex A together with
chain maps γr : C∗(Cuben(r)) ⊗A⊗r −→A compatible with the composition of
operads [BV, Ma, Fr5]. By deﬁnition of the operad Cuben, we are only considering
(weakly) unital versions of En-algebras.
The model category of En-algebras gives rises to the ∞-category En-Alg of En-
algebras in the symmetric monoidal ∞-category of differential graded k-modules.
The symmetric structure of Chain(k) lifts to a a symmetric monoidal structure on
(En-Alg,⊗) given by the tensor product of the underlying chain complexes88.
One can extend the above notion to deﬁne En-algebras with coefﬁcient in any
symmetric monoidal ∞-category following [L3]. One way is to rewrite it in terms
of symmetric monoidal functor as follows. Any topological (resp. simplicial) op-
erad O deﬁnes a symmetric monoidal category, denoted O, ﬁbered over the cate-
gory of pointed ﬁnite sets Fin∗. This category O has the ﬁnite sets for objects. For
any sets n+ := {0,...n}, m+ := {0,...,m} (with base point 0), its morphism space
O(n+,m+) (from n+ to m+) is the disjoint union `
f:n+→m+ ∏i∈m+ O((f −1(i))+)
87more precisely rectangular parallelepiped in dimension bigger than 2
88other possible models for the symmetric monoidal ∞-category (En-Alg,⊗) are given by alge-
braic Hopf operads such as those arising from the ﬁltration of the Barratt-Eccles operad in [BF]
110


## Page 111


and the composition is induced by the operadic structure. The rule n+ ⊗m+ =
(n+m)+ makes canonically O into a symmetric monoidal topological (resp. sim-
plicial) category. We abusively denote O its associated ∞-category. Note that this
construction extends to colored operad and is a special case of an ∞-operad 89.
Then, if (C ,⊗) is a symmetric monoidal ∞-category, a O-algebra in C is
a symmetric monoidal functor A ∈Fun⊗(O,C ). We call A(1+) the underlying
algebra object of A and we usually denote it simply by A.
Deﬁnition 33. [L3, F1] Let (C ,⊗) be symmetric monoidal (∞-)category. The ∞-
category of En-algebras with values in C is
En-Alg(C ) := Fun⊗(Cuben,C ).
Similarly En-coAlg(C ) := Fun⊗(Cuben,C op) is the category of En-coalgebras in
C . We denote MapEn-Alg(A,B) the mapping space of En-algebras maps from A to
B.
Note that Deﬁnition 33 is a deﬁnition of categories of (weakly) (co)unital En-
coalgebra objects.
One has an equivalence En-Alg ∼= En-Alg(Chain(k)) of symmetric monoidal
∞-categories (see [L3, F2]) where En-Alg is the ∞-category associated to algebras
over the operad Cuben considered above. It is clear from the above deﬁnition that
any (∞-)operad En weakly homotopy equivalent (as an operad) to Cuben gives rise
to an equivalent ∞-category of algebra. In particular, the inclusion of rectilinear
embeddings into all framed embeddings gives us an alternative deﬁnition for En-
algebras:
Proposition 51 ([L3]). Let Disk fr
n be the category with objects the integers and
morphism the spaces Diskfr
n (k,ℓ) := Emb fr(`
k Rn,`
ℓRn) of framed embeddings
of k disjoint copies of a disk Rn into ℓsuch copies (see Example 12). The natural
map Fun⊗(Disk fr
n , Chain(k))
≃
−→En-Alg is an equivalence.
Example 63. (Iterated loop spaces) The standard examples90 of En-algebras are
given by iterated loop spaces. If X is a pointed space, we denote Ωn(X) := Map∗(Sn,X)
the set of all pointed maps from Sn ∼= In/∂In to X, equipped with the compact-open
topology. The pinching map (13) pinch : Cuben(r)×Sn −→W
i=1...r Sn induces an
En-algebra structure (in (Top,×)) given by
Cuben(r)×
 Ωn(X))
r ∼= Cuben(r)×Map∗(
_
i=1...r
Sn,X)
pinch∗
−→Ωn(X).
Since the construction is functorial in X, the singular chain complex C∗(Ωn(X))
is also an En-algebra in chain complexes, and further this structure is compatible
89An ∞-operad O⊗is a ∞-category together with a functor O⊗→N(Fin∗) satisfying a list of
axioms, see [L3]. It is to colored topological operads what ∞-categories are to topological categories.
90May’s recognition principle [Ma] actually asserts that any En-algebra in (Top,×) which is
group-like is homotopy equivalent to such an iterated loop space
111


## Page 112


with the E∞-coalgebra structure of C∗(Ωn(X)) (from Example 65). Similarly, the
singular cochain complex C∗(Ωn(X)) is an En-coalgebra in a way compatible with
its E∞-algebra structure; that is an object of En-coAlg(E∞-Alg).
Example 64 (Pn-algebras). A standard result of Cohen [Co] shows that, for n ≥2,
the homology of an En-algebra is a Pn-algebra (also see [Si, Fr5]). A Pn-algebra is
a graded vector space A endowed with a degree 0 multiplication with unit which
makes A a graded commutative algebra, and a (cohomological) degree 1-n opera-
tion [−,−] which makes A[1 −n] a graded Lie algebra. These operations are also
required to satisfy the Leibniz rule [a·b,c] = a[b,c]+(−1)|b|(|c|+1−n)[a,c]·b.
For n = 1, Pn-algebras are just usual Poisson algebras while for n = 2, they are
Gerstenhaber algebras.
In characteristic 0, the operad Cuben is formal, thus equivalent as an operad to
the operad governing Pn-algebras (for n ≥2). It follows that Pn-algebras gives rise
to En-algebras in that case, that is there is a functor91 Pn-Alg →En-Alg.
There are natural maps (sometimes called the stabilization functors)
Cube0 −→Cube1 −→Cube2 −→···
(62)
(induced by taking products of cubes with the interval (0,1)). It is a fact ([Ma, L3])
that the colimit of this diagram, denoted by E∞is equivalent to the commutative
operad Com (whose associated symmetric monoidal ∞-category is Fin∗).
Deﬁnition 34. The(∞-) category of E∞-algebras with value in C is E∞-Alg(C ) :=
Fun⊗(Cube∞,C ). It is simply denoted E∞-Alg if (C ,⊗) = (Chain(k),⊗). Simi-
larly, the category of E∞-coalgebras. is E∞-coAlg := Fun⊗(Cube∞,C op).
Note that Deﬁnition 34 is a deﬁnition of (weakly) unital E∞-algebras.
The category E∞-Alg is (equivalent to) the ∞-category associated to the model
category of E∞-algebras for any E∞-operad E∞.
The natural map Fun⊗(Fin∗,C ) −→Fun⊗(Cube∞,C ) = E∞-Alg is also an
equivalence.
For any n ∈N −{0} ∪{+∞}, the map Cube1 →Cuben (from the nested se-
quence (62)) induces a functor En-Alg −→E1-Alg which associates to an En-
algebra its underlying E1-algebra structure.
Example 65 (Singular (co)chains). Let X be a topological space.
Its singular
cochain complex C∗(X) has a natural structure of E∞-algebra, whose underlying
E1-structure is given by the usual (strictly associative) cup-product (for instance
see [M2]). The singular chains C∗(X) have a natural structure of E∞-coalgebra
which is the predual of (C∗(X),∪). There are similar constructions for simplicial
sets X• instead of spaces, see [BF]. We recall that C∗(X) is the linear dual of the
singular chain complex C∗(X) with coefﬁcient in k which is the geometric real-
ization (in the ordinary category of chain complexes) of the simplicial k-module
91which is not canonical, see [T]
112


## Page 113


k[∆•(X)] spanned by the singular set ∆•(X) := {∆•
f→X, f continuous}. Here ∆n
is the standard n-dimensional simplex.
Remark 37. The mapping space MapE∞-Alg(A,B) of two E∞-algebras A, B (in the
model category of E∞-algebras) is the (geometric realization of the) simplicial set
[n] 7→HomE∞-Alg
 A,B⊗C∗(∆n)

.
The ∞-category E∞-Alg is enriched over sSet (hence Top as well by Exam-
ple 60) and has all (∞-)colimits. In particular, it is tensored over sSet, see [L1, L3]
for details on tensored ∞-categories or [EKMM, MCSV] in the context of topo-
logically enriched model categories. We recall that it means that there is a functor
E∞-Alg×sSet →E∞-Alg, denoted (A,X•) 7→A⊠X•, together with natural equiva-
lences
MapE∞-Alg
 A⊠X•,B
 ∼= MapsSet
 X•,MapE∞-Alg
 A,B

.
To compute explicitly this tensor, it is useful to know the following proposition.
Proposition 52. Let (C ,⊗) be a symmetric monoidal ∞-category. In the symmetric
monoidal ∞-category E∞-Alg(C ), the tensor product is a coproduct.
For a proof see Proposition 3.2.4.7 of [L3] (or [KM, Corollary 3.4]); for C =
Chain(k), this essentially follows from the observation that an E∞-algebra is a com-
mutative monoid in (Chain(k),⊗), see [L3] or [KM, Section 5.3]. In particular,
Proposition 52 implies that, for any ﬁnite set I, A⊗I has a natural structure of E∞-
algebra.
Modules over En-algebras.
In this paragraph, we give a brief account of vari-
ous categories of modules over En-algebras. Note that by deﬁnition (see below),
the categories we considered are categories of pointed modules. Roughly, an A-
modules M being pointed means it is equipped with a map A →M.
Let Fin, (resp. Fin∗) be the category of (resp. pointed) ﬁnite sets. There is a
forgetful functor Fin∗→Fin forgetting which point is the base point. There is also
a functor Fin →Fin∗which adds an extra point called the base point. We write
Fin, Fin∗for the associated ∞-categories (see Example 57). Following [L3, F1],
if O is a (coherent) operad, the ∞-category O-ModA of O-modules92 over an O-
algebra A is the category of O-linear functors O-ModA := MapO(O∗,Chain(k))
where O is the (∞-)category associated93 to the operad O and O∗:= O ×Fin Fin∗
(also see [Fr1] for similar constructions in the model category setting of topological
operads).
The categories O-ModA for A ∈O-Alg assemble to form an ∞-category O-Mod
describing pairs consisting of an O-algebra and a module over it. More precisely,
there is an natural ﬁbration πO : O-Mod −→O-Alg whose ﬁber at A ∈O-Alg is
O-ModA. When O is an En-operad (that is an operad equivalent to Cuben), we
simply write En instead of O:
92in Chain(k). Of course, similar construction hold with Chain(k) replaced by a symmetric
monoidal ∞-category
93in the paragraph above Deﬁnition 33
113


## Page 114


Deﬁnition 35. Let A be an En-algebra (in Chain(k)). We denote En-ModA the
∞-category of (pointed) En-modules over A. Since Chain(k) is bicomplete and
enriched over itself, En-ModA is naturally enriched over Chain(k) as well.
We denote94 RHomEn
A (M,N) ∈Chain(k) the enriched mapping space of mor-
phisms of En-modules over A. Note that if En is a coﬁbrant En-operad and further
M, N are modules over an En-algebra A, then RHomEn
A (M,N) is computed by
HomModEn
A (Q(M),R(N)). Here Q(M) is a coﬁbrant replacement of M and R(N)
a ﬁbrant replacement of N in the model category ModEn
A of modules over the En-
algebra A. In particular, RHomEn
A (M,N) ∼= HomEn-ModA(M,N). This follows from
the fact that En-ModA is equivalent to the ∞-category associated to the model cat-
egory ModEn
A .
If (C ,⊗) is a symmetric monoidal (∞-)category and A ∈En-Alg, then we de-
note En-ModA(C ) the ∞-category of En-modules over A (in C ).
We denote respectively En-Mod the ∞-category of all En-modules in Chain(k)
and En-Mod(C ) the ∞-category of all En-modules in (C ,⊗).
By deﬁnition, the canonical functor95 πEn : En-Mod(C ) →En-Alg(C ) gives
rise, for any En-algebra A, to a (homotopy) pullback square:
En-ModA(C )
/

En-Mod(C )
πEn

{A}
/ En-Alg(C )
(63)
Note that the functor πEn is monoidal.
We also have a canonical functor can : En-Alg →En-Mod induced by the tau-
tological module structure that any algebra has over itself.
Example 66. If A is a differential graded algebra, E1-ModA is equivalent to the
∞-category of (pointed) A-bimodules. If A is a CDGA, E∞-ModA is equivalent to
the ∞-category of (pointed) left A-modules.
Example 67 (left and right modules). If n = 1, we also have naturally deﬁned ∞-
categories of left and right modules over an E1-algebra A (as well as ∞-categories
of all right modules and left modules). They are the immediate generalization
of the (∞-categories associated to the model) categories of pointed left and right
differential graded modules over a differential graded associative unital algebra.
We refer to [L3] for details.
Deﬁnition 36. We write respectively E1-LModA(C ), E1-RModA(C ), E1-LMod(C )
and E1-RMod(C ) for the ∞-categories of left modules over a ﬁxed A, right mod-
ules over A, and all left modules and all right modules (with values in (C ,⊗)).
94The R in the notation is here to recall that this corresponds to a functor that can be computed
as a derived functor associated to ordinary model categories using standard techniques of homologi-
cal/homotopical algebras
95which essentially forget the module in the pair (A,M)
114


## Page 115


If C = Chain(k), we simply write E1-LModA, E1-RModA, E1-LMod, E1-RMod.
Further, we will denote RHomle ft
A
(M,N) ∈Chain(k) the enriched mapping space
of morphisms of left modules over A (induced by the enrichment of Chain(k)). In
particular RHomleft
A
(M,N) ∼= HomE1-LModA(M,N).
There are standard models for these categories. For instance, the category of
right modules over an E1-algebra can be obtained by considering a colored operad
Cuberight
1
obtained from the little interval operad Cube1 as follows. Denote c, i the
two colors. We deﬁne Cuberight
1
({Xj}r
j=1,i) := Cube1(r) if all Xj = i. If X1 = c and
all others Xj = i, we set Cuberight
1
({Xj}r
j=1,c) := Rect
 [0,1)` `r
i=1(0,1)

,[0,1)

where Rect is the space of rectilinear embeddings (mapping 0 to itself). All other
spaces of maps are empty. Then the ∞-category associated to the category of
Cuberight
1
-algebras is equivalent to E1-RMod.
Let A be an E1-algebra, then the usual tensor product of right and left A-
modules has a canonical lift
−
L⊗
A −: E1-RModA ×E1-LModA −→Chain(k)
which, for a differential graded associative algebra over a ﬁeld k is computed by the
two-sided Bar construction. There is a similar derived functor E1-RModA(C ) ×
E1-LModA(C ) −→C , still denoted (R,L) 7→R ⊗L
A L, whenever (C ,⊗) is a sym-
metric monoidal ∞-category with geometric realization and such that ⊗preserves
geometric realization in both variables, see [L3]. There are (derived) adjunction
MapE1-LModA
 P∗⊗L,N
 ∼= MapChain(k)
 P∗,RHomle ft
A
(L,N)

,
MapChain(k)
 R
L⊗
A L,N
 ∼= MapE1-LModA
 L,RHomk(R,N)

which relates the tensor product with the enriched mapping spaces of modules.
References
[AbWa] H. Abbaspour, F. Wagemann, On 2-holonomy, preprint, arXiv:1202.2292.
[AKSZ] M. Alexandrov, A. Schwarz, O. Zaboronsky, M. Kontsevich, The geom-
etry of the master equation and topological quantum ﬁeld theory, Internat. J.
Modern Phys. A 12 (1997), no. 7, 1405–1429.
[An] R. Andrade, From manifolds to invariants of En-algebras, MIT Thesis,
arXiv:1210.7909.
[AF] D. Ayala, J. Francis, Poincar´e duality from Koszul duality, in preparation.
[AFT] D. Ayala, J. Francis, H.-L. Tanaka, Structured singular manifolds and fac-
torization homology, preprint arXiv:1206.5164.
115


## Page 116


[BF] K. Behrend and B. Fantechi, Gerstenhaber and Batalin-Vilkovisky structures
on Lagrangian intersections, in Algebra, arithmetic, and geometry: in honor
of Yu. I. Manin. Vol. I, 1–47, Progr. Math., 269 Birkh¨auser Boston, Boston
[BD] A. Beilinson, V. Drinfeld, Chiral algebras, American Mathematical Society
Colloquium Publications, 51. American Mathematical Society, Providence,
RI, 2004
[BF] C. Berger, B. Fresse, Combinatorial operad actions on cochains, Math. Proc.
Cambridge Philos. Soc. 137 (2004), 135-174.
[Be1] J. E. Bergner, Three models for the homotopy theory of homotopy theories,
Topology 46 (2007), 397–436.
[Be2] J. E. Bergner, Complete Segal Spaces arising from simplicial categories,
Trans. Amer. Math. Soc. 361 (2009), no. 1, 525–546.
[Be3] J. E. Bergner, A survey of (∞,1)-categories, in Towards higher categories,
69–83, IMA Vol. Math. Appl., 152 Springer, New York.
[BV] J. M. Boardman and R. M. Vogt, Homotopy-everything H-spaces, Bull.
Amer. Math. Soc. 74 (1968), 1117–1122.
[Ca] D. Calaque, Lagrangian structures on mapping stacks and semi-classical
TFTs, preprint arXiv:1306.3235.
[Ca2] D. Calaque, Around Hochschild (co)homology, Habilitation thesis.
[CFFR] D. Calaque, G. Felder, A. Ferrario, C. Rossi, Bimodules and branes in
deformation quantization, Compos. Math. 147 (2011), no. 1, 105–160.
[CS] M. Chas, D. Sullivan, String Topology, arXiv:math/9911159
[Ch] K.-T. Chen, Iterated integrals of differential forms and loop space homology,
Ann. of Math. (2) 97 (1973), 217–246.
[Co] F. R. Cohen, T. J. Lada and J. P. May, The homology of iterated loop spaces,
Lecture Notes in Mathematics, Vol. 533, Springer, Berlin, 1976.
[CV] R. Cohen, A. Voronov, Notes on String topology, String topology and cyclic
homology, 1–95, Adv. Courses Math. CRM Barcelona, Birkhauser, Basel,
2006.
[C1] K. Costello, Topological conformal ﬁeld theories and Calabi-Yau categories,
Adv. Math. 210 (2007), no. 1, 165–214.
[C2] K. Costello, A geometric construction of Witten Genus, I, preprint,
arXiv:1006.5422v2.
116


## Page 117


[C3] K. Costello, Mathematical aspects of (twisted) supersymmetric gauge theo-
ries, note taken by C. Scheimbauer. To appear in “Mathematical Aspects of
Field Theories”, Mathematical Physics Studies, Springer.
[CG] K. Costello, O. Gwilliam, Factorization algebras in perturbative quantum
ﬁeld theory,
Online wiki available at http://math.northwestern.edu/∼costello/factorization public.html.
To appear, Cambridge University Press.
[DTT] V. Dolgushev, D. Tamarkin, B. Tsygan, Proof of Swiss Cheese Version of
Deligne’s Conjecture,
[DS] D. Dugger, B. Shipley, Enriched model categories and an application to
additive endomorphism spectra, Theory Appl. Categ. 18 (2007), No. 15, 400–
439.
[Du] G. Dunn, Tensor product of operads and iterated loop spaces, Int. Math. Res.
Not. IMRN 2011, no. 20, 4666–4746. J. Pure Appl. Algebra 50 (1988), no. 3,
237–258.
[DK] W.G. Dwyer, D.M. Kan, Calculating simplicial localizations, J. Pure Appl.
Alg. 18 (1980), 17–35.
[ES] S. Eilenberg and N. E. Steenrod, Axiomatic approach to homology theory,
Proc. Nat. Acad. Sci. U. S. A. 31 (1945), 117–120.
[EKMM] A. D. Elmendorf, M. Mandell, I. Kriz, J. P. May, Rings, modules, and
algebras in stable homotopy theory, Mathematical Surveys and Monographs,
47, Amer. Math. Soc., Providence, RI, 1997.
[FHT] Y. F´elix, S. Halperin, J.-C. Thomas, Rational homotopy theory, Graduate
Texts in Mathematics, 205. Springer-Verlag. MR2415345 (2009c:55015)
[FT] Y. F´elix, J.-C. Thomas, Rational BV-algebra in string topology, Bull. Soc.
Math. France 136 (2008), no. 2, 311–327
[FG] J. Francis and D. Gaitsgory, Chiral Koszul duality, Selecta Math. (N.S.) 18
(2012), no. 1, 27–87.
[F1] J. Francis. The tangent complex and Hochschild cohomology of En-rings, to
appear, Compositio Mathematica.
[F2] J. Francis, Factorization homology of topological manifolds, preprint
arXiv:1206.5522.
[Fr1] B. Fresse, Modules over Operads and Functors, Lect. Notes in Maths. vol.
1967, Springer verlag (2009).
117


## Page 118


[Fr2] B. Fresse, The bar complex of an E∞-algebra, Adv. Math. 223 (2010), pp.
2049–2096.
[Fr3] B. Fresse, Iterated bar complexes of E-inﬁnity algebras and homology theo-
ries, Alg. Geom. Topol. 11 (2011), pp. 747–838.
[Fr4] B. Fresse, Koszul duality of En-operads, Selecta Math. (N.S.) 17 (2011),
no. 2, 363–434.
[Fr5] B. Fresse, Operads and Grothendieck-Teichm¨uller groups, Part I, book avail-
able at http://math.univ-lille1.fr/∼fresse/Recherches.html
[Ga1] D. Gaitsgory, Contractibility of the space of rational maps, Preprint
arXiv:1108.1741.
[Ga2] D. Gaitsgory, Outline of the proof of the geometric Langlands conjecture
for GL(2), Preprint arXiv:1302.2506.
[GH] D. Gepner, R. Haugseng, Enriched inﬁnity categories, preprint.
[Ge] M. Gerstenhaber, The Cohomology Structure Of An Associative ring Ann.
Maths. 78(2) (1963).
[Gi] G. Ginot, Higher order Hochschild Cohomology, C. R. Math. Acad. Sci. Paris
346 (2008), no. 1-2, 5–10.
[GTZ] G. Ginot, T. Tradler, M. Zeinalian, A Chen model for mapping spaces and
the surface product, Ann. Sc. de l’´Ec. Norm. Sup., 4e s´erie, t. 43 (2010), p.
811-881.
[GTZ2] G. Ginot, T. Tradler, M. Zeinalian, Derived Higher Hochschild Ho-
mology, Topological Chiral Homology and Factorization algebras, preprint
arXiv:1011.6483. To appear Commun. Math. Phys.
[GTZ3] G. Ginot, T. Tradler, M. Zeinalian, Higher Hochschild cohomology, Brane
topology and centralizers of En-algebra maps, preprint arXiv:1205.7056.
[GJ] P. Goerss, J. Jardine, Simplicial Homotopy Theory, Modern Birkh¨auser Clas-
sics, ﬁrst ed. (2009), Birkh¨auser Basel.
[G] T. Goodwillie, Cyclic homology, derivations, and the free loop space Topol.
24 (1985), no. 2, 187–215.
[GMcP] M. Goresky, R. MacPherson, Stratiﬁed Morse theory, Ergebnisse der
Mathematik und ihrer Grenzgebiete (3), 14, Springer, Berlin, 1988.
[GrGw] R. Grady, O. Gwilliam, One-dimensional Chern-Simons Theory and the
A-hat genus, preprint arXiv:1110.3533.
118


## Page 119


[GM] B. Guillou, J.-P. May, Enriched Model Categories and Presheaf Categories,
preprint arXiv:1110.3567.
[Gw] O.
Gwilliam,
Factorization
algebras
and
free
ﬁeld
theo-
ries,
PH-D
Thesis,
Northwestern
University,
available
oline
at:
http://math.berkeley.edu/ gwilliam/
[Hi] V. Hinich, Homological Algebra of Homotopy Algebras, Comm. Algebra 25
(1997), no. 10, 3291–3323.
[HS] A Hirschowitz,
C. Simpson,
Descente pour les n-champs,
preprint
math.AG/987049,
[Hu] P. Hu, Higher string topology on general spaces, Proc. London Math. Soc.
93 (2006), 515–544.
[HKV] P. Hu, I. Kriz, A. Voronov, On Kontsevich’s Hochschild cohomology con-
jecture, Compos. Math. 142 (2006), no. 1, 143–168.
[Ho] G. Horel, Factorization Homology and Calculus `a la Kontsevich-Soibelman,
Preprint arXiv:1307.0322.
[H] M. Hovey, Model Categories, Mathematical Surveys and Monographs, 63.
American Mathematical Society, Providence, RI, 1999. xii+209 pp.
[HMS] D. Husemoller, J. C. Moore and J. Stasheff, Differential homological al-
gebra and homogeneous spaces, J. Pure Appl. Algebra 5 (1974), 113–185.
[Jo] J.D.S. Jones Cyclic homology and equivariant homology, Inv. Math. 87, no.2
(1987), 403–423
[KiSi] R. C. Kirby, L. C. Siebenmann, Foundational essays on topological man-
ifolds, smoothings, and triangulations, Princeton Univ. Press, Princeton, NJ,
1977.
[Ko] M. Kontsevich, Operads and motives in deformation quantization, Lett.
Math. Phys. 48 (1999), no. 1, 35–72.
[KS] M. Kontsevich and Y. Soibelman, Notes on A∞-algebras, A∞-categories and
non-commutative geometry, in Homological mirror symmetry, 153–219, Lec-
ture Notes in Phys., 757 Springer, Berlin.
[KM] I. Kriz, J. P. May, Operads, algebras, modules and motives, Ast´erisque No.
233 (1995), iv+145pp.
[L]
J.-L. Loday, Cyclic Homology, Grundlehren der mathematischen Wis-
senschaften 301 (1992), Springer Verlag.
[LS] R. Longoni, P. Salvatore, Conﬁguration spaces are not homotopy invariant,
Topology 44 (2005), no. 2, 375–380.
119


## Page 120


[L1] J. Lurie, Higher Topos Theory, Annals of Mathematics Studies, 170. Prince-
ton University Press, Princeton, NJ, 2009. xviii+925 pp.
[L2] J. Lurie, On the Classiﬁcation of Topological Field Theories, preprint,
arXiv:0905.0465v1.
[L3] J.
Lurie,
Higher
Algebra,
preprint,
available
at
http://www.math.harvard.edu/∼lurie/
[L4] J. Lurie, Derived Algebraic Geometry X: Formal Moduli Problems, preprint,
available at http://www.math.harvard.edu/∼lurie/
[MCSV] J. McClure, R. Schw¨anzl and R. Vogt, THH(R) ∼= R ⊗S1 for E∞ring
spectra, J. Pure Appl. Algebra 121 (1997), no. 2, 137–159.
[M1] M. A. Mandell, Cochain multiplications, Amer. J. Math. 124 (2002), no. 3,
547–566.
[M2] M. Mandell, Cochains and homotopy type, Publ. Math. Inst. Hautes ´Etudes
Sci. No. 103 (2006), 213–246.
[Ma] J. P. May, The geometry of iterated loop spaces, Springer, Berlin, 1972.
[PTTV] T. Pantev, B. To¨en, M. Vaqui´e, G. Vezzosi, Shifted Symplectic Structures,
to appear in ubl. Math. Inst. Hautes ´Etudes Sci., arXiv:1111.3209.
[Pa] F. Paugam, Towards the mathematics of Quantum Field Theory, book avail-
able at http://people.math.jussieu.fr/∼fpaugam/parts-fr/publications.html , to
appear, Springer.
[P]
T. Pirashvili, Hodge Decomposition for higher order Hochschild Homology,
Ann. Sci. ´Ecole Norm. Sup. (4) 33 (2000), no. 2, 151–179.
[Q] D. Quillen, On the (co-)homology of commutative rings, in Applications of
Categorical Algebra (Proc. Sympos. Pure Math., Vol. XVII, New York, 1968),
65–87, Amer. Math. Soc., Providence, RI.
[R]
C. Rezk, A model for the homotopy theory of homotopy theory, Trans. Amer.
Math. Soc. 353 (3) (2001), 937–1007.
[SW] P. Salvatore, N. Wahl, Framed discs operads and Batalin Vilkovisky alge-
bras, Q. J. Math. 54 (2003), no. 2, 213–231.
[Sa] E. Satger, Paris 6, PH-D thesis, in preparation.
[Sc] C. Scheimbauer, in preparation.
[S1] G. Segal Conﬁguration-spaces and iterated loop-spaces, Invent. Math. 21
(1973), 213–221.
120


## Page 121


[S2] G. Segal, The deﬁnition of conformal ﬁeld theory in Topology, geometry
and quantum ﬁeld theory, London Mathematical Society Lecture Note Se-
ries, 308, Cambridge Univ. Press, Cambridge, 2004.
[S3] G. Segal, Locality of holomorphic bundles, and locality in quantum ﬁeld the-
ory, in The many facets of geometry, 164–176, Oxford Univ. Press, Oxford.
[Sh] U. Shukla, Cohomologie des alg`ebres associatives, Ann. Sci. ´Ecole Norm.
Sup. (3) 78 (1961), 163–209.
[Si] D. Sinha, The (non)-equivariant homology of the little disk operad, in Oper-
ads 2009, S´eminaires et Congr`es 26 (2012), 255-281.
[T]
D. Tamarkin, Quantization of Lie bialgebras via the formality of the operad
of little disks, Geom. Funct. Anal. 17 (2007), no. 2, 537–604.
[TT] D. Tamarkin and B. Tsygan, Noncommutative differential calculus, homo-
topy BV algebras and formality conjectures, Methods Funct. Anal. Topology
6 (2000), no. 2, 85–100.
[Ta] H.-L. Tanaka, Factorization homology and link invariant. To appear in
“Mathematical Aspects of Field Theories”, Mathematical Physics Studies,
Springer.
[Th] R. Thom, Ensembles et morphismes stratiﬁ´es, Bull. Amer. Math. Soc. 75
(1969), 240–284.
[To] B. To¨en, The homotopy theory of dg-categories and derived Morita theory,
Invent. Math. 167 (2007), no. 3, 615–667.
[TV1] B. To¨en, G. Vezzosi, Segal topoi and stacks over Segal categories, preprint
math.AG/0212330
[TV2] B. To¨en, G. Vezzosi, Homotopical Algebraic Geometry II: geometric stacks
and applications, Mem. Amer. Math. Soc. 193 (2008), no. 902.
[TV3] B. To¨en, G. Vezzosi, A note on Chern character, loop spaces and derived
algebraic geometry, Abel Symposium, Oslo (2007), Volume 4, 331-354.
[TV4] B. To¨en, G. Vezzosi, Alg`ebres simpliciales S1-´equivariantes et th´eorie de
de Rham. Compos. Math. 147 (2011), no. 6, 1979–2000.
[TV3] B. To¨en, G. Vezzosi, Caract`eres de Chern, traces ´equivariantes et
g´eom´etrie alg´ebrique d´eriv´ee, Preprint, arXiv:0903.3292.
[TWZ] T. Tradler, S. O. Wilson, M. Zeinalian Equivariant holonomy for bundles
and abelian gerbes, Commun. Math. Phys. 315 (2012), 39–108.
121


## Page 122


[V] A. Voronov, The Swiss-cheese operad, in Homotopy invariant algebraic
structures (Baltimore, MD, 1998), 365–373, Contemp. Math., 239 Amer.
Math. Soc., Providence, RI.
[W] C. A. Weibel, An introduction to homological algebra, Cambridge Studies in
Advanced Mathematics, 38, Cambridge Univ. Press, Cambridge, 1994.
122

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1307_5213_notes_on_factorization_algebras_factorization_homology_and_applications
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2013/1307_5213_NOTES_ON_FACTORIZATION_ALGEBRAS_FACTORIZATION_HOMOLOGY_AND_APPLICATIONS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

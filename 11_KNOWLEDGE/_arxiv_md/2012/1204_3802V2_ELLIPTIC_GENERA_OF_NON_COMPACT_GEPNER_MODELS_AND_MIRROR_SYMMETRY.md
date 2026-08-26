---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1204.3802v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1204.3802v2_Elliptic_Genera_of_Non-compact_Gepner_Models_and_Mirror_Symmetry

> Source: 1204.3802v2_Elliptic_Genera_of_Non-compact_Gepner_Models_and_Mirror_Symmetry.pdf

> Pages: 30

---


## Page 1


arXiv:1204.3802v2  [hep-th]  27 Jun 2012
Elliptic Genera of Non-compact Gepner Models
and Mirror Symmetry
Sujay K. Ashoka and Jan Troostb
aInstitute of Mathematical Sciences
C.I.T Campus, Taramani
Chennai, India 600113
b Laboratoire de Physique Th´eorique1
Ecole Normale Sup´erieure
24 rue Lhomond
F–75231 Paris Cedex 05, France
Abstract
We consider tensor products of N = 2 minimal models and non-compact conformal
ﬁeld theories with N = 2 superconformal symmetry, and their orbifolds. The elliptic
genera of these models give rise to a large and interesting class of real Jacobi forms.
The tensor product of conformal ﬁeld theories leads to a natural product on the space
of completed mock modular forms. We exhibit families of non-compact mirror pairs of
orbifold models with c = 9 and show explicitly the equality of elliptic genera, including
contributions from the long multiplet sector. The Liouville and cigar deformed elliptic
genera transform into each other under the mirror transformation.
1Unit´e Mixte du CNRS et de l’Ecole Normale Sup´erieure associ´ee `a l’universit´e Pierre et Marie Curie 6,
UMR 8549.


## Page 2


Contents
1
Introduction
2
2
Elliptic genera
3
2.1
Deﬁnition and Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
2.2
The building blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
2.2.1
The N = 2 minimal models
. . . . . . . . . . . . . . . . . . . . . . .
4
2.2.2
The N = 2 Liouville model . . . . . . . . . . . . . . . . . . . . . . . .
4
2.2.3
The coset conformal ﬁeld theory . . . . . . . . . . . . . . . . . . . . .
5
2.3
Tensor product theories
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.4
Twisted blocks
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
3
Mirror symmetry for Gepner models
7
3.1
Non-compact Gepner models . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3.2
Mirror symmetry through orbifolds . . . . . . . . . . . . . . . . . . . . . . .
8
3.3
Models with central charge c = 6
. . . . . . . . . . . . . . . . . . . . . . . .
8
3.3.1
The ground states . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
3.3.2
Mirror symmetry . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
4
Models with central charge c = 9
11
4.1
The (2k, 2k; k) model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
4.1.1
An inﬁnite family of mirror pairs
. . . . . . . . . . . . . . . . . . . .
12
4.1.2
The long multiplet sector . . . . . . . . . . . . . . . . . . . . . . . . .
14
4.2
The (k; 2k, 2k) model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.2.1
The short multiplet bound states . . . . . . . . . . . . . . . . . . . .
17
4.2.2
The long multiplet scattering states . . . . . . . . . . . . . . . . . . .
17
5
Notes on mock modular forms
19
5.1
The shadow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
5.2
The product of mock modular forms
. . . . . . . . . . . . . . . . . . . . . .
20
5.3
The orbifolds of completions of mock modular forms . . . . . . . . . . . . . .
21
5.4
Uniqueness
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
A Characters
22
A.1 Minimal model characters
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
A.2 Minimal model twisted blocks . . . . . . . . . . . . . . . . . . . . . . . . . .
23
A.3 The Zk orbifold and mirror symmetry . . . . . . . . . . . . . . . . . . . . . .
24
A.4 Characters at c > 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
A.5 Twisted building blocks at c > 3 . . . . . . . . . . . . . . . . . . . . . . . . .
26
A.5.1
Character formulae . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
A.5.2
Twisted blocks for the non-holomorphic sector . . . . . . . . . . . . .
26
A.5.3
Exact expressions for twisted blocks . . . . . . . . . . . . . . . . . . .
27
1


## Page 3


1
Introduction
The study of two-dimensional conformal ﬁeld theories in terms of their minimal model de-
scription, their Landau-Ginzburg phase or as gauged linear sigma-models has proven to be
very useful [1,2]. It has taught us about the space of two-dimensional conformal ﬁeld theories,
and its geometrical structure. The study has had a profound impact on our understanding of
compact Calabi-Yau manifolds and mirror symmetry, and it has had interesting applications
in the ﬁeld of singular manifolds and toric varieties (see [3] for a review).
The extension of this study to include theories with non-compact targets, and in par-
ticular non-compact Calabi-Yau manifolds is very interesting. It is a natural generalization
from the perspective of studying Calabi-Yau manifolds locally, or from the viewpoint of
understanding holography in curved non-compact spaces that asymptotically have a linear
dilaton proﬁle [4, 5]. This ﬁeld has already given rise to many results including a study of
the map between deformations of the geometry and the spectrum of non-compact confor-
mal ﬁeld theories [6–10], mirror symmetry for non-compact Gepner models, as well as an
intriguing relation between orbifolds in asymptotically linear dilaton spaces and ﬂat space
toric orbifolds [10]. However many of the results have been based on studying the chiral
(anti-chiral) rings of the theory.
Recently, there has been a lot of progress in our understanding of the elliptic genus
of non-compact N = 2 superconformal ﬁeld theories with central charge larger than three
[11–13]. In particular, it was understood that the elliptic genus is modular covariant and real.
Non-holomorphic contributions arise from the continuous part of the spectrum of the two-
dimensional conformal ﬁeld theory. This has led to a physical understanding of the modular
completion of mock modular forms in terms of both a modular Lagrangian path integral
description [11], and a Hamiltonian viewpoint in terms of an integral over a diﬀerence of
spectral densities for right-moving primary bosons and fermions [13].
In this paper we apply these new insights to the study of conformal ﬁeld theories which
are tensor products of N = 2 minimal models and N = 2 Liouville theories (or N = 2
cigar coset models), and their orbifolds. The elliptic genus of tensor product theories is the
product of the individual elliptic genera. For orbifold theories, we can often identify the
elliptic genus via standard twisting procedures.
For orbifolds of products of compact Gepner models, there have been many interesting
results [14–18], especially in the context of mirror symmetry.
Given a Landau-Ginzburg
formulation of a compact Calabi-Yau, there is an algorithmic way to construct the mirror.
Most of the results on elliptic genera rely on the fact that, given the Poincar´e polynomial of
the theory, there is a unique extension to the elliptic genus and the identiﬁcation of mirror
pairs thus becomes simpler.
For non-compact conformal ﬁeld theories, our generic construction will give rise to a large
new class of real Jacobi forms. In particular, when more than one non-compact model is
involved, the product of elliptic genera gives rise to a modular completion of the product of
mock modular forms. Conformal ﬁeld theory elliptic genera thus provide a natural way to
complete the product of two mock modular forms.
2


## Page 4


We apply this general reasoning to non-compact Gepner models and their orbifolds in
type II string theory. The knowledge we gained about non-compact elliptic genera allows us
to check mirror symmetry explicitly in these models in a way coherent with modularity and
ellipticity. The check includes some long multiplet contributions. Our analysis is constructive
in the sense that, starting from the elliptic genus of a given orbifold theory we rewrite it
such that the ﬁnal expression has a natural interpretation as the elliptic genus of the mirror
model. Under the mirror transform, the Liouville factors naturally go over into their cigar
counterparts.
The paper has the following organization. In section 2 we discuss the elliptic genera
of the basic models, which are the minimal models with c < 3 and the two types of non-
compact models with c > 3, the Liouville and cigar theories. We also describe how to put
these together and construct the elliptic genera of tensor product and orbifold models. In
section 3 we restrict to orbifold models which are non-compact generalizations of Gepner
models in type II string theory. Examples with central charge c = 6 are provided in section
3.3 and those with central charge c = 9 are discussed in section 4. The technical ingredients
necessary for the calculations in these sections are provided in appendix A. We end in section
5 with a number of proposals for how to extend our class of examples to a broader domain.
2
Elliptic genera
In this section, we review the elliptic genera of N = 2 minimal models and N = 2 super-
conformal ﬁeld theories with central charge greater than three, since these conformal ﬁeld
theories form the building blocks of the models we study in sections 3 and 4. We also pause
to make a point about an embryonic example of mirror symmetry.
2.1
Deﬁnition and Properties
We study N = 2 superconformal ﬁeld theories with a left U(1)R charge J0 and a right charge
¯J0, as well as scaling dimension operators L0 and ¯L0. The elliptic genus χ [19,20] is deﬁned
as a twisted partition sum with periodic boundary conditions for the fermions:
χ(q, z)
=
Tr (−1)FqL0−c
24 ¯q
˜L0−c
24zJ0.
(2.1)
We will also use the notation χ(q, z) ≡χ(τ, α) for the elliptic genus, where the arguments
are related through the equations q = e2πiτ and z = e2πiα. The elliptic genus has elliptic and
modular covariance properties which make it a Jacobi form.
2.2
The building blocks
In this subsection, we list the elliptic genera of the elementary building blocks that we will
use to construct our models.
3


## Page 5


2.2.1
The N = 2 minimal models
The elliptic genus of an N = 2 minimal model with central charge c = 3−6
k and k a positive
integer is given by [1]:
χ(k; −)(q, z)
=
θ11(q, z
k−1
k )
θ11(q, z
1
k )
.
(2.2)
This is also the elliptic genus of the compact Landau-Ginzburg model with superpotential
W = Xk . It can, moreover, be derived from the gauged Wess-Zumino-Witten description of
the model. We denote the level of the minimal model as an extra argument for the elliptic
genus, followed by a semicolon. The elliptic genus of the minimal model has an expansion
in terms of twisted Ramond sector characters [1,21]:
χ(k; −)(q, z) =
k−2
2
X
j=0, 1
2,...
Cj
2j+1(q, z) .
(2.3)
The basic deﬁnitions and the modular and elliptic properties of these characters are reviewed
in appendix A.
2.2.2
The N = 2 Liouville model
Next, we consider models with central charge c = 3 + 6
l with the level l equal to a positive
integer. The Zl ⊂U(1)R orbifold of the SL(2, R)l/U(1) coset theory with central charge
c = 3 + 6
l has elliptic genus [11]:
χ(−; l)(q, z) = iθ11(q, z)
η3
ˆA2l(z
1
l , z2; q).
(2.4)
The level l of the non-compact model follows the semicolon. This elliptic genus is also the
genus of a generalized non-compact Landau-Ginzburg model with superpotential W = e−lY ,
coinciding with N = 2 Liouville theory at radius R =
√
lα′.
Let us discuss these points in some detail, since it provides an important embryonic
example of mirror symmetry that pervades the rest of our paper.
Note that there are
two known ways to obtain the expression (2.4) for the elliptic genus.
The ﬁrst way is
through the non-compact Landau-Ginzburg model, where one identiﬁes the R-charges of
the ﬁelds, and their proper conﬁguration space, then to do a free ﬁeld calculation to obtain
the holomorphic part of the elliptic genus [11]. A scattering calculation using the Landau-
Ginzburg potential will then further provide the remainder term in the elliptic genus [13],
thus proving that expression (2.4) is the elliptic genus of N = 2 Liouville theory at radius
R =
√
lα′. Alternatively, a path integral calculation shows that this is also the elliptic genus
of the Zl orbifold of the cigar coset conformal ﬁeld theory [11, 13]. This provides further
evidence for the equivalence of these models [22, 23] in terms of the match of a modular
covariant partition sum.
4


## Page 6


The mock modular form, of which the elliptic genus is the completion, is a holomorphic
Appell-Lerch sum which has an expansion in terms of twisted Ramond N = 2 superconformal
characters Ch extended by spectral ﬂow (see [23,24] for our conventions for the arguments):
χhol(−; l)(q, z) =
l−1
X
2j−1=0
Ch(j; −1
2; q, z).
(2.5)
2.2.3
The coset conformal ﬁeld theory
The SL(2, R)l/U(1) supersymmetric coset theory, which we refer to as the cigar theory, has
an elliptic genus obtained by taking the Zl orbifold of the elliptic genus quoted above. It is
given by
χ(−; l)Zl(q, z) = 1
l
iθ11(q, z)
η3
X
ma,mb∈Zl
e−2πimamb
l
q−m2a
l ˆA2l(z
1
l q
mb
l e
2πimb
l
, z2; q).
(2.6)
We have denoted the orbifold group as a superscript to the elliptic genus. It is also the
elliptic genus of N = 2 Liouville theory at radius R =
p
α′/l. The holomorphic part of the
elliptic genus can again be expanded in terms of the extended characters:
χhol(−; l)Zl(q, z) =
l−1
X
2j−1=0
Ch(j; −1
2 −(2j −1); q, z) .
(2.7)
2.3
Tensor product theories
An elementary but important point is that the elliptic genus of a tensor product conformal
ﬁeld theory is the product of the individual elliptic genera:
χ(⊗iCFTi)
=
Y
i
χ(CFTi).
(2.8)
For example, for the tensor product of compact and non-compact Landau-Ginzburg models
with central charges associated to the positive and integer levels (k1, k2, . . . , kp; l1, l2, . . . , lq),
the elliptic genus reads:
χ(k1, k2, . . . , kp; l1, l2, . . . , lq)(q, z)
=
p
Y
i=1
θ11(q, z1−1
ki )
θ11(q, z
1
ki )
qY
j=1
iθ11(q, z)
η3
ˆA2lj(z
1
lj , z2; q).(2.9)
One can generalize this elliptic genus to one which keeps track of the R-charges of the
individual factor theories. We ﬁnd a generalized elliptic genus:
χ(k1, k2, . . . , kp; l1, l2, . . . , lq)(q, zi, zj) =
p
Y
i=1
θ11(q, z
1−1
ki
i
)
θ11(q, z
1
ki
i )
qY
j=1
iθ11(q, zj)
η3
ˆA2lj(z
1
lj
j , z2
j ; q) .
(2.10)
This is one of many generalizations of the twisted index. One can write down similar ex-
pressions where we replace some of the Liouville factors with cigar coset theories.
5


## Page 7


2.4
Twisted blocks
In the following, we consider orbifolds of tensor products of the above models. For simplicity,
we restrict our orbifold groups to be discrete subgroups of the product of the U(1) R-
symmetry groups of the factor models.
In these circumstances, it is straightforward to
generalize the techniques of [14] to describe the twisted partition sums from which we build
the elliptic genus of the orbifold. In each factor theory, we have partition sums in the sectors
twisted by the generator of an orbifold group Zn to the power ma ∈Zn and we can insert
an operator corresponding to a generator of the orbifold group to the power mb ∈Zn. We
then obtain the twisted partition functions:
χma,mb(q, z)
=
e2πi c
6mambe2πi c
6(m2
aτ+2maα)χ(τ, α + maτ + mb).
(2.11)
The transformation properties of these twisted elliptic genera are (with λ, µ ∈Z):
χma,mb(−1
τ , α
τ )
=
e2πi c
6
α2
τ χmb,−ma(τ, α)
χma,mb(τ + 1, α)
=
χma+mb,mb(τ, α)
χma,mb(τ, α + λτ + µ)
=
e2πi c
6(maµ−mbλ−λµ)e−2πi c
6(λ2τ+2λα)χma+λ,mb+µ(τ, z).
(2.12)
We assign a canonical phase factor to each factor model:
ǫ(ma, mb)
=
(−1)ma+mb+mamb,
(2.13)
which will ensure that the total orbifolded model is free of discrete torsion. For the partition
sum including the phase, we use the notation:
˜χma,mb = ǫ(ma, mb)χma,mb.
(2.14)
The twisted building blocks for the R-symmetry orbifolds can be simpliﬁed using the ellip-
ticity and modular properties of theta functions and completed Appell-Lerch sums ˆA (see
appendix A for details). It will be convenient to express the twisted building blocks ˜χma,mb
of the minimal models and the non-compact conformal ﬁeld theories in terms of the twisted
Ramond sector characters of the conformal ﬁeld theory. This renders the transformation
properties of each term under the insertion of a generator in the trace manifest. We ﬁnd the
twisted blocks:
• for the minimal models
˜χma,mb(k; −) = e−2πimamb
k
k−2
2
X
j=0, 1
2 ,...
e
2πimb
k
(2j+1)Cj
2j+1−2ma(q, z) .
(2.15)
• for the anti-diagonal (or Zk orbifolded) minimal models
˜χma,mb(k; −)Zk = e−2πimamb
k
k−2
2
X
j=0, 1
2,...
e−2πimb
k
(2j+1)Cj
−2j−1−2ma(q, z) .
(2.16)
6


## Page 8


• for the holomorphic part of a Liouville factor:
˜χhol;ma,mb(−; l) = e
2πimamb
l
l−1
X
2j−1=0
e
2πimb
l
(2j−1)Ch(j; −1
2 + ma; q, z).
(2.17)
• for the holomorphic part of a cigar factor:
˜χhol;ma.mb(−; l)Zl = e
2πimamb
l
l−1
X
2j−1=0
e−2πimb
l
(2j−1)Ch(j; −1
2 −(2j −1) + ma; q, z).
(2.18)
The completed twisted blocks for non-compact factors are recorded in appendix A.
3
Mirror symmetry for Gepner models
In this section we recapitulate the construction of mirror Gepner models [26], generalized to
include non-compact conformal ﬁeld theories.
3.1
Non-compact Gepner models
Gepner’s construction of string compactiﬁcations in terms of exactly solvable N = 2 super-
conformal ﬁeld theories [25] can be suitably extended to include factor models with central
charge larger than 3 (see e.g. [10]). We study non-compact Gepner models consisting of
p minimal models at levels ki and q non-compact models at levels lj tensored with Rd−1,1.
They can be characterized in the light-cone as having a
U(1)
d−2
2
2
× U(1)p+q
2
×
p
Y
i=1
U(1)ki ×
qY
j=1
U(1)lj
(3.1)
worldsheet current algebra. The level 2 factors refer to worldsheet fermion numbers, and
the U(1) current algebras at level ki and lj are the R-currents of compact and non-compact
N = 2 superconformal ﬁeld theories. We have the corresponding charge vectors r:
r = (s−d−4
2 , . . . , s0, s1, . . . , sp+q; n1, . . . , np; −2m1, . . . , −2mq),
(3.2)
with inner product:
r(1) · r(2) = −
s(1)
−d−4
2 s(2)
−d−4
2
4
· · · + n(1)
1 n(2)
2
2k1
· · · −2m(1)
1 2m(2)
2
2l1
. . .
(3.3)
7


## Page 9


We introduce a vector β0 such that twice its inner product with the left-moving charge vector
is proportional to the left-moving R-charge. It satisﬁes β0 · β0 = −1. We ﬁx conventions
such that β0 is equal to:
β0 = (1, . . . , 1, 1, . . . , 1; 1, . . . , 1; 1, . . . , 1).
(3.4)
If we start from a model diagonal in the charge lattice quantum numbers, then we must
perform an orbifold to render the model local on the worldsheet, in the sense of containing
only purely NS or purely Ramond states. The necessary Zp+q+(d−4)/2
2
orbifold involves discrete
torsion [26]. To obtain the type II Gepner model, one further performs an integer R-charge
orbifold, and a Z2 GSO projection.
3.2
Mirror symmetry through orbifolds
Mirror symmetry is implemented in Gepner models through orbifolding by a subgroup of
the discrete group Gphase = Qp
i=1 Zki × Qq
j=1 Zlj of the U(1)R symmetries of the factor
theories [26]. The integer R-charge orbifold Zn is already such a subgroup2. The maximal
subgroup H of the group Gphase which preserves space-time supersymmetry gives rise to
the mirror theory. Thus, the group H will be the maximal subgroup of Gphase/Zn which
preserves the condition that the left and right R-charge remain integer. Let us denote the
original Gepner model by M1, and the mirror model by M2 = M1/H. Then if we consider
orbifolds of theory M1 by the subgroup H1 ⊂H, we will ﬁnd that the theory M1/H1 is
mirror to the theory M2/(H/H1).
We further note that the maximal allowed orbifold will give rise to (the GSO projection
of) the T-dual of the original model (before GSO). In the T-dual, all left-moving angular
momenta will have an opposite sign. These statements are true for the compact theory be-
cause a Zk orbifold of the minimal model gives rise to its T-dual. For a singular non-compact
theory (described by a purely linear dilaton background), the statement also holds. For the
deformed or resolved non-compact theories, we need a mild modiﬁcation. For instance, the
Zl orbifold of Liouville theory at radius R =
√
lα′ is Liouville theory at radius R =
p
α′/l.
That is T-dual to the cigar theory at radius R =
√
lα′. Thus orbifolding is equivalent to
T-duality only for the compact factors. For the non-compact factors, we must combine orb-
ifolding with an exchange of deformation and resolution in order to obtain the T-dual model.
We conﬁrm this picture by the direct evaluation of elliptic genera for the mirror pair.
3.3
Models with central charge c = 6
In this subsection, we get our feet wet with simple examples of non-compact Gepner models
with central charge c = 6, and make some preliminary observations. We concentrate on
models involving one compact and one non-compact model at equal levels. As a starting
2Here we ignore the fermionic entries in the charge vectors, which we can do if we allow for ﬂat space
charge conjugation.
8


## Page 10


point, we take a product of a minimal model with central charge c = 3 −6/k and an N = 2
Liouville theory at radius R =
√
kα′ with central charge c = 3 + 6/k.
The integer R-
charge orbifold is an orbifold by the group Zk. The conformal ﬁeld theory describes strings
propagating on a space which is asymptotically locally ﬂat, with a linear dilaton slope. It has
a deformed C2/Zk singularity at the center. See [10,27] for detailed discussions. The elliptic
genus of this theory is given by the orbifold formula applied to the two factor theories:
χ(k; k)Zk = 1
k
k−1
X
ma,mb=0
˜χma,mb(k; −)˜χma,mb(−; k)
= 1
k
iθ11(q, z)
η(q)3
k−1
X
ma,mb=0
k−2
2
X
j=0, 1
2,...
e
2πimb(2j+1)
k
q
m2a
k z
2ma
k
Cj
2j+1−2ma(q, z) ˆA2k(z
1
k q
ma
k e
2πimb
k
, z2q2ma; q) .
(3.5)
3.3.1
The ground states
To link our results to known results on massless states, we observe that we can recuperate
the Poincar´e polynomial of these models from these expressions, by taking the limit that
projects onto left-moving (R-charged weighted) Ramond ground states. One thus recovers
the results described for instance in [10].
3.3.2
Mirror symmetry
To advance our analysis of mirror symmetry we ﬁrst observe that, for this c = 6 model, the
maximal group H of phase symmetries that we can mod out by while preserving supersym-
metry is trivial. Thus, the model must be self-mirror. This can also be seen as a consequence
of the (generalized) hyperk¨ahler structure of the target space. We conclude that the elliptic
genus of the model has to be equal to the elliptic genus of a diagonal minimal model times
the cigar model at radius
√
kα′ modded out by the integer R-charge and GSO projection.
The latter elliptic genus is given by:
χ′(k; k)Zk = 1
k
k−1
X
ma,mb=0
˜χma,mb(k; −)˜χma,mb(−; k)Zk
= 1
k2
iθ11(τ, α)
η3
k−1
X
ma,mb=0
k−1
2
X
j=0, 1
2 ,...
e
2πimb(2j+1)
k
q
m2a
k z
2ma
k
Cj
2j+1−2ma(q, z)
×
X
m′a,m′
b∈Zk
q−m
′2
a
k e−2πim′an′a
k
ˆA2l(z
1
k q
ma+m′a
k
e
2πi(mb+m′
b)
k
, z2q2ma; q) .
(3.6)
The equality of the elliptic genera in equations (3.5) and (3.6) is non-trivial. To prove the
equality, it is useful to render the N = 2 superconformal representation content of the com-
9


## Page 11


pact and non-compact elliptic genera manifest. In particular, let us write the holomorphic
part of the elliptic genus (3.5) in terms of the characters of the minimal model and the
analogous extended characters (2.15) and (2.17):
χhol(k; k)Zk =
X
j1,j2
X
ma,mb∈Zk
e
2πimb
k
[(2j1+1)+(2j2−1)]Cj1
2j1+1−2ma(q, z)Ch(j2; −1
2 + ma; q, z) . (3.7)
The sum over mb imposes the GSO constraint and relates the spin of the two individual
factors. In order to render the mirror interpretation manifest, we shift the twisted sector label
ma by −(2j2 −1) . We then use the integer R-charge constraint in the angular momentum
quantum number of the minimal model character, to end up with the ﬁnal expression:
χhol(k; k)Zk =
X
j1,j2
X
ma,mb∈Zk
e
2πimb
k
[(2j1+1)+(2j2−1)]
Cj1
−2j1−1−2ma(q, z)Ch(j2; −1
2 + ma −(2j2 −1); q, z) .
(3.8)
Repackaging this in terms of the twisted blocks, we ﬁnd
χ(k; k)Zk = 1
k
k−1
X
ma,mb=0
˜χma,mb(k; −)Zk ˜χhol;ma,mb(−; k)Zk
(3.9)
We recognize this to be the elliptic genus of an anti-diagonal minimal model times the cigar
theory at R =
√
kα′, the whole orbifolded by Zk. Performing a similar calculation for the
non-holomorphic long multiplet contributions gives rise to the modular completion of the
above formula.
In order to fully appreciate the relation between expressions (3.5) and (3.6), we have to
go a bit further. We will give more details in the intricate c = 9 examples, but we already
outline the idea here. We wish to re-interpret the mirror model as an orbifold of a diagonal
model. For this purpose, we note that the elliptic genus of the anti-diagonal minimal model
is related to the diagonal minimal model elliptic genus through a sign ﬂip in the second
argument α, and the addition of an overall sign (see equation (A.6)). Analogously the non-
compact elliptic genus is invariant under such a sign ﬂip (see equation (A.21)). Rewriting in
terms of the twisted blocks we ﬁnd
χ(k; k)Zk(τ, α) = −1
k
k−1
X
ma,mb=0
˜χma,mb(k; −)(τ, −α)˜χma,mb(−; k)Zk(τ, α)
= −χ′(k; k)Zk(τ, −α) .
(3.10)
Therefore the elliptic genus of the original model is self-mirror and furthermore equal to the
elliptic genus (3.6), up to an overall sign and a sign ﬂip in the second argument α. The
calculation provides a proof of a non-trivial relation between products and sums of theta-
functions and completed Appell-Lerch sums. In the following sections, we will consider more
involved examples of mirror symmetry, including inﬁnite families of mirror pairs, and many
more details on the long multiplet contributions, in the context of non-compact Gepner
models with central charge c = 9.
10


## Page 12


4
Models with central charge c = 9
In this section we will study two types of models with central charge c = 9. The ﬁrst type has
tensor products of two minimal models and a Liouville/cigar model. The second type has a
single minimal model tensored with two non-compact factors. We consider supersymmetric
orbifolds of these models and exhibit families of mirror pairs. The ﬁrst set serves to generate
an inﬁnite set of mirror pairs (see also [10]), and illustrates in a fairly simple setting how
mirror symmetry acts on elliptic genera in the non-compact case. The second set analyzes
more deeply how mirror symmetry operates in the long multiplet sector.
4.1
The (2k, 2k; k) model
From the general discussion on mirror symmetry via orbifolds, it is clear that we must identify
the largest subgroup H of the phase symmetries with which one can orbifold and still preserve
supersymmetry. Let us perform this calculation for the (2k, 2k; k) model corresponding to
two diagonal minimal models and one N = 2 Liouville theory at radius R =
√
kα′. There
exists a Landau-Ginzburg (LG) model which ﬂows to this conformal ﬁeld theory in the
infrared and it is sometimes convenient to think in terms of such a description. The LG
model contains three chiral superﬁelds X1, X2 and Y3 with superpotential:
W = X2k
1 + X2k
2 + e−kY3 .
(4.1)
The phase symmetries of the model are given by Gphase = Z2k×Z2k×Zk. We can identify the
elements of the group Gphase with charge vectors in the following manner. A group element
corresponds to a charge vector γ if it multiplies a state with diagonal charge vector r by the
phase e2πiγ·r. We can choose generators γi in each factor of the group Gphase such that γi
is the charge vector with entry 2 in the spot corresponding to the relevant U(1) charge (see
deﬁnition (3.3)).
We identify the group G = (Z2k ×Z2k ×Zk)/Z2k as the subgroup by which we can divide
after taking into account the integer R-charge orbifold Zn = Z2k. The maximal subgroup
H of G that preserves supersymmetry corresponds to charge vectors βm which are integer
linear combinations of the charge vectors γi. The generators βm need to satisfy:
βm =
X
i
ci
mγi
and
βm · β0 ∈Z.
(4.2)
Using our conventions for β0, this is equivalent to
p
X
i=1
ci
m
ki
−
q
X
j=1
cj
m
lj
∈Z ,
(4.3)
where the ki are the levels of the minimal models while the li refer to the levels of the non-
compact models. The ci
m are integers. In our speciﬁc example, we have three coeﬃcients
11


## Page 13


ci=1,2,3
m
for each generator βm, which have to satisfy:
+ c1
m
2k + c2
m
2k −c3
m
k
∈
Z.
(4.4)
The integers ci
m are deﬁned modulo (2k, 2k, k). The integer R-charge orbifold corresponds
to ci
m = (1, 1, 1). Thus, we can use the gauging of the integer R-charge orbifold to put the
last entry to zero. Note also that if we consider the element of the R-charge orbifold group
that squares to one we ﬁnd that it corresponds to the vector ci
m = (+k, −k, 0). Thus, we
conclude that the elements of the group H have representatives where the ﬁrst two entries
are opposite and that these entries are only non-trivial modulo k. We therefore ﬁnd that
the group H is the Zk group generated by multiplication of the phases of X1 and X2 by e
2πi
2k
and e−2πi
2k respectively.
4.1.1
An inﬁnite family of mirror pairs
To generate an inﬁnite family of mirror pairs, we can consider subgroups of the group H.
We suppose that the level k of our initial models is equal to the product of two positive
integers k = k1k2. We can then consider orbifolds of our diagonal model with the subgroup
Z2k × Zk1 (or strictly speaking, their semi-direct product) where the ﬁrst factor corresponds
to the integer R-charge orbifold and the second factor to the subgroup Zk1 of the group H
generated by the phase multiplication e±2πi k2
2k acting on the ﬁelds X1,2. Each group element
of the orbifold group is labeled by a pair of integers (m, n), taking values in Zk and Zk1
respectively.
Details of the calculation
In what follows, we begin with the elliptic genus of this doubly orbifolded model and show,
analogous to what was done for the c = 6 case, that we are able to rewrite it as the elliptic
genus of the mirror model. In this case, the mirror is a Z2k × Zk2 orbifold of a product
conformal ﬁeld theory with two minimal model factors and the cigar conformal ﬁeld theory.
We start out with the holomorphic part of the orbifolded elliptic genus written in terms
of the twisted blocks. It depends only on the charges of the ﬁelds under the orbifold group:
χhol(2k, 2k; k)Z2k,Zk1 =
1
2kk1
X
ma,mb∈Z2k
X
na,nb∈Zk1
˜χma+k2na,mb+k2nb(2k; −)
˜χma−k2na,mb−k2nb(2k; −)˜χhol;ma,mb(−; k).
(4.5)
The ﬁrst minimal model factor contributes
˜χma+k2na,mb+k2nb(2k; −) = e−2πi(ma+k2na)(mb+k2nb)
2k
2k−2
2
X
j1=0, 1
2,...
e
2πi(mb+k2nb)(2j1+1)
2k
Cj1
2j1+1−2(ma+k2na)(q, z) ,
(4.6)
12


## Page 14


and similarly for the second minimal model factor with a sign ﬂip for the na, nb quantum
numbers. For the Liouville sector, we have
˜χhol;ma,mb(−; k)(τ, α) = e
2πimamb
k
k−1
X
2j3−1=0
e
(2j3−1)
k
2πimbCh(j3; −1
2 + ma; q, z) .
(4.7)
Putting all the factors together we obtain:
χhol(2k, 2k; k)Z2k,Zk1 =
1
2kk1
X
j1,j2,j3
X
ma,mb∈Z2k
X
na,nb∈Zk1
e
2πimb
2k
((2j1+1)+(2j2+1)+2(2j3−1)) e
2πinb
2k1 ((2j1+1)−(2j2+1)−2k2na)
Cj1
2j1+1−2(ma+k2na)(q, z)Cj2
2j2+1−2(ma−k2na)(q, z)Ch(j3; −1
2 + ma; q, z) .
(4.8)
The sum over the twist insertion mb then imposes the desired integer R-charge constraint:
j1 + j2 + 2j3
k
∈Z.
(4.9)
A second constraint arises from the sum over the values of nb:
j1 −j2 −k2na
k1
∈Z .
(4.10)
Indeed, for any projection beyond the initial integer R-charge projection, we will ﬁnd a
constraint between spins and a new quantum number. In order to rewrite this as the mirror
elliptic genus we ﬁnd it useful to eliminate the twisted quantum numbers na in terms of
the spin quantum numbers.
In order to solve for the second constraint, recall that the
angular momentum quantum number in the minimal model factor is deﬁned modulo twice
the level. Using this we ﬁnd that there are precisely k2 solutions to the second equation
(where k = k1 · k2). Solving for na, we substitute:
k2na = j1 −j2 + n′
ak1
with
n′
a ∈Zk2 .
(4.11)
This leads to
χhol(2k, 2k; k)Z2k,Zk1 =
1
2kk2
X
j1,j2,j3
X
ma,mb∈Z2k
X
n′a,n′
b∈Zk2
e
2πimb
2k
((2j1+1)+(2j2+1)+2(2j3−1))e
2πin′
b
2k2 ((2j1+1)−(2j2+1)+2k1n′
a)
X
n′a∈Zk2
Cj1
2j2+1−2(ma+k1n′a)(q, z)Cj2
2j1+1−2(ma−k1n′a)(q, z)Ch(j3; −1
2 + ma; q, z) .
(4.12)
13


## Page 15


The sum over the integer n′
b ∈Zk2 ensures that the numbers n′
a, j1 and j2 satisfy the
constraint (4.11). We now use the integer R-charge constraint to eliminate the spin j2 in the
ﬁrst minimal model and the spin j1 in the second minimal model character. After a shift in
the ma variable by −(2j3 −1), we obtain our ﬁnal expression:
χhol(2k, 2k; k)Z2k,Zk1 =
1
2kk2
X
j1,j2,j3
X
ma,mb∈Z2k
e−2πimb
2k
[(2j1+1)+(2j2+1)+2(2j3−1)]
X
n′a,n′
b∈Zk2
e
2πin′
b
2k2 ((2j1+1)−(2j2+1)+2k1n′
a)Cj1
−2j1−1−2(ma+k1n′a)(q, z)
Cj2
−2j2−1−2(ma−k1n′a)(q, z) Ch(j3; −1
2 + ma −2j3 −1; q, z) . (4.13)
Rewriting this back in terms of the twisted blocks, we ﬁnd that the ﬁnal expression is equal
to:
χhol(2k, 2k; k)Z2k,Zk1 =
1
2kk2
X
ma,mb∈Z2k
X
n′a,n′
b∈Zk2
˜χma+k1n′a,mb+k1n′
b(2k; −)Z2k
˜χma−k1n′a,mb−k1n′
b(2k; −)Z2k ˜χhol;ma,mb(−; k)Zk.(4.14)
To infer the mirror we have more work to do.
Firstly we have to ensure that the non-
holomorphic part of the orbifold elliptic genus can also be written such that it is the appro-
priate modular completion of the above mock modular form. Secondly we need to have the
orbifold of a diagonal model in order to read of the mirror.
4.1.2
The long multiplet sector
In order to complete our matching of elliptic genera of the mirror pairs, we also need to
check the equality for the states in the long multiplet sector. For simplicity, we restrict to
the case in which the levels satisfy k1 = k and k2 = 1. The generalization to the other cases
is straightforward. The remainder term of the orbifold elliptic genus takes the form
χrem(2k, 2k; k)Z2k,Zk =
1
2k2
X
ma,mb∈Z2k
X
na,nb∈Zk
χma+na,mb+nb(2k−; )
χma−na,mb−nb(2k−; )χrem;ma,mb(−; k) .
(4.15)
In order to proceed we require the twisted blocks that correspond to the non-holomorphic
piece of the elliptic genus. These are given in appendix A. Using these blocks along with the
14


## Page 16


expressions for the minimal model elliptic genera, we obtain
χrem(2k, 2k; k)Z2k,Zk =
1
2k2
X
j1,j2
X
ma,mb∈Z2k
e
2πimb
2k
((2j1+1)+(2j2+1))
X
na,nb∈Zk
e
2πinb
2k
((2j1+1)−(2j2+1)−2na)
X
w,n∈Z
e2πi nmb
k z
n−kw+2ma
k
Cj1
2j1+1−2(ma+na)(q, z)Cj2
2j2+1−2(ma−na)(q, z)
(−1) 1
πiθ11(τ, α)
η3
Z +∞−iǫ
−∞−iǫ
ds
2is + n + kwq
s2
k + (n−kw+2ma)2
4k
¯q
s2
k + (n+kw)2
4k
.
(4.16)
The calculation follows the same scheme as the previous one. The sum over the integers mb
and nb again imposes the desired constraints:
2j1 + 1
2k
+ 2j2 + 1
2k
+ n
k ∈Z ,
j1
k −j2
k −na
k ∈Z .
(4.17)
We eliminate the twisted quantum numbers na in terms of the spins and obtain:
χrem(2k, 2k; k)Z2k,Zk = 1
2k
X
j1,j2
X
ma,mb∈Z2k
e
2πimb
2k
((2j1+1)+(2j2+1))
X
w,n∈Z
e2πi nmb
k z
n−kw+2ma
k
Cj1
2j2+1−2ma(q, z) Cj2
2j1+1−2ma(q, z)
(−1) 1
πiθ11(τ, α)
η3
Z +∞−iǫ
−∞−iǫ
ds
2is + n + kwq
s2
k + (n−kw+2ma)2
4k
¯q
s2
k + (n+kw)2
4k
.
We substitute the integer R-charge constraint in the angular momentum variable of the two
minimal models and shift the variable ma to ma −n + kw and ﬁnd:
χrem(2k, 2k; k)Z2k,Zk = 1
2k
X
j1,j2
X
ma,mb∈Z2k
e
2πimb
2k
((2j1+1)+(2j2+1))
X
w,n∈Z
e2πi nmb
k z
−n+kw+2ma
k
Cj1
−2j1−1−2ma(q, z) Cj2
−2j2−1−2ma(q, z)
(−1) 1
πiθ11(τ, α)
η3
Z +∞−iǫ
−∞−iǫ
ds
2is + n + kwq
s2
k + (−n+kw+2ma)2
4k
¯q
s2
k + (n+kw)2
4k
.
(4.18)
We then ﬂip the sign of the variable mb, and ﬁnd that all individual factors combined indeed
agree with the twisted blocks of the mirror model:
χrem(2k, 2k; k)Z2k,Zk = 1
2k
X
ma,mb∈Z2k
˜χma,mb(2k; −)Z2k ˜χma,mb(2k; −)Z2k ˜χrem;ma,mb(−; k)Zk.
(4.19)
15


## Page 17


This is the modular completion of the mock modular form deﬁned in equation (4.14) for
k1 = k and k2 = 1. We thus extended the proof of the equality of elliptic genera of mirror
symmetric models to the long multiplet sector.
Finally, we can rewrite the formula for the mirror elliptic genus in terms of characters
which are more easily read as being associated to a diagonal spectrum. We ﬁnd that the
mirror can be written as:
χ(2k, 2k; k)Z2k,Zk(τ, α) = 1
2k
X
ma,mb∈Z2k
˜χma,mb(2k; −)(τ, −α)
˜χma,mb(2k; −)(τ, −α)˜χma,mb(−; k)Zk(τ, −α), (4.20)
where we have ﬂipped the sign of the summation variables. We have used two facts which
we already encountered while discussing the self-mirror c = 6 example. Firstly, that the
anti-diagonal minimal model elliptic genera are equal to their diagonal model counterpart,
up to an overall sign change and a change in the sign of the second argument (see equation
(A.6)). Secondly, that the elliptic genus of a non-compact model is equal to itself under
the sign ﬂip of the second argument (see equation (A.21)).
Note how a sign ﬂip in the
left-moving angular momentum comes down to T-duality for the compact factor, which is
self-dual under T-duality. For the non-compact factor, the sign ﬂip changes its nature from
Liouville theory to cigar model.
Our ﬁnal expression is consistent with our expectations about the mirror model. The
original model M1 was a (2k, 2k; k) model with Liouville deformation at radius
√
kα′. The
Z2k ×Zk1 orbifold of the model gives rise to the mirror M2 of this model which is a (2k, 2k; k)
model at radius R =
√
kα′ modded out by Z2k × Zk2. If the original model M1 is (Liouville)
deformed, then the mirror M2 is expected to be (cigar) resolved, which is indeed the case.
We have thus exhibited an inﬁnite family of models, parameterized by a pair of integers
(k1, k2) that are mirror to one another and for which the elliptic genera match.
4.2
The (k; 2k, 2k) model
We next consider the model with two non-compact factors and one minimal model. The
non-holomorphic sector of this model has qualitatively diﬀerent features from the models of
subsection 4.1 since it involves the modular completion of a product of two mock modular
forms. The Landau-Ginzburg description of the model is given by the superpotential
W = Xk
1 + e−2kY2 + e−2kY3 .
(4.21)
We consider the orbifold by the group Z2k × Zk generated by:
(X1, e−Y2, e−Y3) −→

e
2πi
k X1, e
2πi
2k e−Y2, e
2πi
2k e−Y3
(X1, e−Y2, e−Y3) −→

X1, e
2πi
2k e−Y2, e−2πi
2k e−Y3
.
(4.22)
For simplicity we only focus on the orbifold by the full group H = Zk.
16


## Page 18


4.2.1
The short multiplet bound states
Using the twisted blocks in equations (2.15) and (2.17), the holomorphic part of the elliptic
genus of the double orbifold takes the form:
χhol(k; 2k, 2k)Z2k,Zk =
1
2k2
X
j1,j2,j3
X
ma,mb∈Z2k
X
na,nb∈Zk
e
2πimb
2k
(2(2j1+1)+(2j2−1)+(2j3−1))e
2πinb
2k
((2j2−1)−(2j3−1)+2na)
Cj1
2j1+1−2ma Ch(j2; −1
2 + (ma + na); q, z)Ch(j3; −1
2 + (ma −na); q, z) .
(4.23)
We ﬁnd the constraints:
2j1 + j2 + j3
k
∈Z
and
j2
k −j3
k + na
k ∈Z .
(4.24)
As before we will ﬁnd it useful to eliminate the twisted quantum numbers na in terms of
the spins, while retaining the integer R-charge constraint as it is. We then substitute the R-
charge constraint in the angular momentum variable of the two Liouville factors. Redeﬁning
the variable ma variable to m′
a = ma −(2j1 −1), we ﬁnally obtain the expression:
χhol(k; 2k, 2k)Z2k,Zk = 1
2k
X
ma,mb∈Z2k
X
j1,j2,j3
e−2πimb
2j1+j2+j3
k
Cj1
−2j1−1−2ma(q, z)
Ch(j2; −1
2 + ma −2j2 −1; q, z) Ch(j3; −1
2 + ma −2j3 −1; q, z) .
(4.25)
Repackaging this in terms of the twisted blocks, we ﬁnd:
χ(k; 2k, 2k)Z2k,Zk = 1
2k
X
ma,mb∈Z2k
˜χma,mb(k−; )Zk ˜χhol;ma,mb(−; 2k)Z2k ˜χhol;ma,mb(−; 2k)Z2k .
(4.26)
As was done in the earlier examples we turn now to a calculation of the non-holomorphic
completion of the elliptic genus in order to read oﬀthe mirror model. The non-holomorphic
contribution for this model is qualitatively diﬀerent in nature and throws up new and inter-
esting points.
4.2.2
The long multiplet scattering states
Schematically, the fully modular elliptic genus of this orbifold model can be decomposed into
a holomorphic and non-holomorphic piece as follows3:
χ = χ1 χ2 χ3 = χ1
hol
 χ2
holχ3
hol +

χ2
holχ3
rem + χ2
remχ3
hol + χ2
remχ3
rem

,
(4.27)
3We elaborate on this point in section 5.
17


## Page 19


where we have suppressed the summation indices over the twisted blocks of the orbifold. The
terms in the square parenthesis are the non-holomorphic completion for the product of two
mock modular forms. The mirror analysis of the ﬁrst two terms in this completion parallel
the discussion in the previous subsections and we do not show the details of the calculation
since we obtain the expected result parallel to the one obtained in equation (4.26). The last
term is of a new type, and we consider it in detail below. Denoting it by T3, and reinstating
the missing summation indices, let us use the twisted blocks for the non-holomorphic sector
and write it out in full glory:
T3 =
1
2k2
2k−1
X
ma,mb=0
k−1
X
na,nb=0
˜χma,mb(k; −)˜χrem;ma+na,mb+nb(−; 2k)˜χrem;ma−na,mb−nb(−; 2k)
=
1
2k2
 i
π
θ11
η3
2 X
j1
X
w1,n1
X
w2,n2
X
ma,mb
X
na,nb
e
2πimb((2j1+1)−ma)
k
Cj1
2j1+1−2ma
× e
2πi
2k ((mb+nb)(n1+(ma+na))+(mb−nb)(n2+(ma−na))) × z
n1−2kw1+2(ma+na)
2k
+ n2−2kw2+2(ma−na)
2k
×
Z
ds1
2is1 + n1 + 2kw1
q
s2
1
2k + (n1−2kw1+2(ma+na))2
8k
¯q
s2
1
2k + (n1+2kw1)2
8k
×
Z
ds2
2is2 + n2 + 2kw2
q
s2
2
2k + (n2−2kw2+2(ma−na))2
8k
¯q
s2
2
2k + (n2+2kw2)2
8k
.
(4.28)
The phase factors give rise to the two constraints:
n1 −2kw1
2k
+ n2 −2kw2
2k
+ 2j1 + 1
k
∈Z ,
n1 −2kw1
2k
−n2 −2kw2
2k
+ 2na
2k ∈Z .
(4.29)
We have used the fact that na is deﬁned modulo k. As before we can solve for the variable
na using the second constraint:
2na = (n2 −2kw1) −(n1 −2kw1) .
(4.30)
The variable na appears in two diﬀerent combinations with the other variables in both of
the non-compact factors. Let us label those combinations e1 and e2, where
e1 = (n1 −2kw1) + 2(ma + na)
and
e2 = (n2 −2kw2) + 2(ma −na) .
(4.31)
Substituting for na, we see that the combinations e1 and e2 become
e1 = n2 −2kw2 + 2ma
and
e2 = n1 −2kw1 + 2ma .
(4.32)
We use the integer R-charge constraint in equation (4.29) to obtain:
e1 = −(n1−2kw1)+2ma−2(2j1+1)
and
e2 = −(n2−2kw2)+2ma−2(2j1+1) . (4.33)
18


## Page 20


Shifting the variable ma by (−2j1 −1) and substituting for the combinations ei in the
expression for T3, we ﬁnd the ﬁnal form:
T3 = 1
2k
 i
π
θ11
η3
2 X
j1
X
w1,n1
X
w2,n2
X
ma,mb
e
2πimb(2(2j1+1)+n1+n2)
2k
z
(−n1+2kw1+2ma)
2k
+ (−n2+2kw2+2ma)
2k
×
Z
ds1
2is1 + n1 + 2kw1
q
s2
1
2k + (−n1+2kw1+2ma)2
8k
¯q
s2
1
2k + (n1+2kw1)2
8k
×
Z
ds2
2is2 + n2 + 2kw2
q
s2
2
2k + (−n2+2kw2+2ma))2
8k
¯q
s2
2
2k + (n2+2kw2)2
8k
Cj1
−2j1−1−2ma
= 1
2k
X
ma,mb
˜χhol;ma,mb(k; −)Zk ˜χrem;ma,mb(−; 2k)Z2k ˜χrem;ma,mb(−; 2k)Z2k .
(4.34)
The factors agree with the twisted blocks of the mirror model. Indeed, one can now combine
all terms in equation (4.27) and rewrite the full elliptic genus as the integer R-charge orbifold
of an anti-diagonal minimal model at level k, tensored with the two cigar theories at level 2k.
Thus, all terms in the elliptic genera conﬁrm the mirror symmetry of the models, including
the long multiplet contributions. We can also rewrite this as the elliptic genus of a diagonal
minimal model combined with two cigars (up to an overall minus sign, and a minus sign
in the second argument of the elliptic genus). Note how our calculation again gives rise to
non-trivial identities between the orbifolded product of two modular completed Appell-Lerch
sums ˆA.
Finally, let us stress that our method, ultimately based on T-duality, will work for any
number of products of minimal models and Liouville/cigar theories and their orbifolds.
5
Notes on mock modular forms
In this section, we make various remarks on mock modular forms, a ﬁeld which is in full
development in both mathematics (see e.g. [29,30]) and physics (see e.g. [31–35]). We propose
that the embedding of the mathematics of mock modular forms in our present conformal
ﬁeld theory perspective provides a fruitful point of view.
5.1
The shadow
As a prelude to our discussion, it will be useful to introduce the concept of a shadow. It
is sometimes convenient to make explicit the dependence of the twisted partition function
(which is a real Jacobi form) on the anti-holomorphic parameter ¯τ.
Once the partition
function is known, this dependence can be read oﬀfrom its anti-holomorphic derivative which
we refer to as the shadow [29,30]. For starters, let us explicitly compute the shadow [29] of
the elliptic genus of N = 2 Liouville theory at radius R =
√
lα′ directly from the partition
19


## Page 21


function [11]4. The shadow is deﬁned (up to normalization and conjugation) as the anti-
holomorphic derivative of the real Jacobi form χ(−; l):
χshad(−; l)
=
∂¯τχ(−; l)
=
−
1
4√lτ2
θ11(τ, α)
η3
X
w,n∈Z
z
n−lw
l
(n + lw)q
(n−lw)2
4l
¯q
(n+lw)2
4l
=
−1
2
r
l
τ2
θ11(τ, α)
η3
X
m∈Z2l
Θm,l(q, z
2
l )Θ
3
2
m,l(¯q),
(5.1)
where we used the deﬁnitions of the theta-functions of weight 1/2 and 3/2 at level l:
Θm,l(q, z)
=
X
p∈Z
ql(p+ m
2l )2zl(p+ m
2l )
Θ
3
2
m,l(q)
=
X
p∈Z
(p + m
2l)ql(p+ m
2l )2.
(5.2)
The shadow is a sum of terms which are the product of a holomorphic theta-function of
weight 1/2, and an anti-holomorphic theta-function of weight 3/2.
5.2
The product of mock modular forms
Modular forms exhibit a ring structure. In particular, the product of modular forms gives
rise to another modular form. For mock modular forms, the corresponding ring structure is
not yet fully understood. We therefore believe that it is interesting to observe that if mock
modular forms can be interpreted as the holomorphic parts of the elliptic genera of conformal
ﬁeld theories, then their product can be interpreted as the holomorphic part of the elliptic
genus of the tensor product conformal ﬁeld theory (as in equation (2.8)). Thus, the tensor
product operation on conformal ﬁeld theories can give rise to a natural product of mock
modular forms, or to a suggestion of how to extend the deﬁnition of mock modular forms
to include these products.
Clearly, the completions of these products of mock modular
forms will include products of mock modular forms and remainder functions, as well as
the product of remainder functions. Indeed, imagine we have two real Jacobi forms χ1,2,
which are modular completions of mock modular forms χ1,2
hol, then their product will have a
remainder term of a new type:
χ1χ2
=
χ1
holχ2
hol + (χ1
holχ2
rem + χ1
remχ2
hol + χ1
remχ2
rem).
(5.3)
These sums of products of holomorphic and non-holomorphic pieces give rise to generalized
shadows including the product of remainder terms (consisting of properly weighted modular
integrals of theta-functions) and the shadows of individual non-compact elliptic genera (for
example as in equation (5.1)).
4The shadow was also obtained in this fashion by Sameer Murthy.
20


## Page 22


5.3
The orbifolds of completions of mock modular forms
We gave an explicit example of an orbifold of such a product of completed mock modular
forms in subsection 4.2. It is clear that our construction gives rise to a large class of real Ja-
cobi forms that is non-trivial. The corresponding mock modular forms may contain multiple
poles5. Beyond the orbifolds discussed in this paper, we can imagine many diﬀerent types
of mock modular forms and their completions that can arise in physical contexts. Instead of
performing R-charge orbifolds as we have done up to now, we can extend the orbifold group
much further.
For instance, we can consider symmetric product orbifold groups. It is straightforward to
write down the elliptic genus of a symmetric product orbifold, using its Lagrangian descrip-
tion in terms of a sum over coverings of the torus by the torus. The result is a new Jacobi
form obtained from the seed through Hecke operators. The Hamiltonian interpretation of
the resulting formula could prove interesting. Moreover, we can introduce discrete torsion
in more general abelian or non-abelian orbifolds, further enlarging the class of expressions
that one can obtain on the physics side, providing more examples of what could be called
(generalized) mock modular forms.
Yet another class of theories that can be examined, are Landau-Ginzburg theories with
mixes of polynomial potentials, and exponentials.
One can compute their elliptic genus
using free ﬁeld techniques. For the polynomials, one uses the techniques of [1] while for the
exponentials, one uses the approach of [11]. This could potentially open up a whole new
realm of mock modular forms, corresponding to elliptic genera of conformal ﬁeld theories that
may not be exactly solvable but that can be described as infrared limits of supersymmetric
ﬁeld theories.
5.4
Uniqueness
Since the mathematics of mock modular forms is not yet set in stone, it is harder at the
moment to prove the uniqueness of modular completions of the largest class of mock mod-
ular forms (see however [28–30] for interesting results in this direction). In particular, the
approach (used for compact models) of identifying polar parts and using ellipticity and mod-
ularity to prove equality of elliptic genera is not yet available for generic completed mock
modular forms (though it may apply to the case of a single non-compact factor examined in
subsection 4.1.2). Such a general mathematical theory could give rise to the physical state-
ment that the long multiplet sector matching is guaranteed by ellipticity and modularity.
That would provide interesting information on the asymptotics of these non-compact Gepner
models from their bound state spectrum, and vice versa.
5The typical shadow however will be diﬀerent from the shadow for the double pole case discussed in [28],
where it is the sum of a product of holomorphic and anti-holomorphic modular forms. We thank Sameer
Murthy for a discussion on this point.
21


## Page 23


Acknowledgements
We would like to thank Atish Dabholkar, JeﬀHarvey, Amir Kashani-Poor, Albrecht Klemm,
Sameer Murthy and Thomas Wotschke for interesting discussions and useful correspondence.
We thank the authors of [28] for making a preliminary version of their work available to
us. S.A would like to thank the Chennai Mathematical Institute for hospitality during the
completion of this work. Our research is partly funded by the grant ANR-09-BLAN-0157-02.
A
Characters
A.1
Minimal model characters
One way to deﬁne N = 2 minimal model characters is implicitly:
X
n∈Z2k
Cj(s)
n
(τ, α)Θn,k(τ, −2α
k ) = χj(τ, 0)Θs,2(τ, −α).
(A.1)
We used the theta-functions deﬁned by the formula:
Θn,k(τ, α)
=
X
m∈Z
e2πiτk(m+ n
2k )2e2πiαk(m+ n
2k ).
(A.2)
The Ramond sector ground states correspond to states with R-charges ±((2j + 1)/k −1/2).
The characters for representations built on ground states are Cj(+1)
2j+1 and Cj(−1)
−2j−1. We note
that these two lists are in fact identical when we use the equivalence relation (j, n, s) ≡
(k/2−j −1, n+k, s+2). From their implicit deﬁnition, we ﬁnd the character transformation
rule:
Cj(s)
n
(τ, α + maτ + mb) = q−c
6m2
az−c
3 mae2πi( n
k −s
2)mbCj(s−2ma)
n−2ma
(τ, α).
(A.3)
We also need the twisted Ramond sector characters Cj
n which we deﬁne as:
Cj
n
=
Cj(1)
n
−Cj(−1)
n
.
(A.4)
They satisfy the transformation rule:
Cj
n(τ, α + maτ + mb)
=
(−1)ma+mbq−c
6m2
az−c
3 mae2πi n
k mbCj
n−2ma(τ, α),
(A.5)
as well as the equality:
Cj
−n(τ, α)
=
−Cj
n(τ, −α).
(A.6)
22


## Page 24


A.2
Minimal model twisted blocks
In computing the minimal model twisted blocks, we assume that for an individual model
we have a partition function in which we sum over left and right spins which satisfy s = ¯s
modulo 2. This is a diagonal sum in terms of NS and R sectors. We then ﬁnd for the elliptic
genus:
χ(k; −) = θ11(q, z
k−1
k )
θ11(q, z
1
k )
=
k−2
2
X
j=0, 1
2,...
Cj
2j+1(q, z) .
(A.7)
The twisted blocks are:
χma,mb(k; −) = e2πi c
6mambe2πi c
6(m2
aτ+2maα)
k−2
2
X
j=0, 1
2,...
Cj
2j+1(τ, α + maτ + mb)
= e2πi c
6mamb(−1)ma+mb
k−2
2
X
j=0, 1
2,...
e2πimb
2j+1
k Cj
2j+1−2ma(τ, α).
(A.8)
Inserting the standard phase ǫ, we obtain
˜χma,mb(k; −) = e−2πimamb
k
k−2
2
X
j=0, 1
2,...
e2πimb
2j+1
k Cj
2j+1−2ma(τ, α).
(A.9)
We have used the known elliptic properties of the Ramond sector characters in order to
derive the twisted blocks. Equivalently, we can perform the calculation using the ellipticity
properties of the theta-function. We obtain
˜χma,mb(k; −) = z−ma
k θ11(z(1−1
k )q−ma
k e−2πimb
k
)
θ11(z
1
k q
ma
k e
2πimb
k
)
.
(A.10)
We note in passing that with this choice of phase ǫ, the twisted blocks of [14] and [16] agree.
It remains to compare this to the sum of the Ramond sector characters. We rewrite:
˜χma,mb(k; −) = z−ma
k θ11(z′(1−1
k ) q−ma; q)
θ11(z′ 1
k ; q)
,
(A.11)
with
z′ = zqma e2πimb .
(A.12)
Using the elliptic property of the theta-function, we can write this as
˜χma,mb(k; −) = (−1)maq
m2a
2 (1−2
k )zma(1−2
k )e−2πimamb
k
θ11(z′(1−1
k ); q)
θ11(z′ 1
k ; q)
.
(A.13)
The ratio of theta functions can be expanded in terms of the Ramond-sector characters as
in equation (A.7). We then again use the elliptic properties of the minimal model characters
(A.5) to ﬁnd that the result agrees with equation (A.9). We have come full circle.
23


## Page 25


A.3
The Zk orbifold and mirror symmetry
Consider the Zk orbifold the N = 2 minimal model (with s = ¯s mod 2) of central charge
c = 3 −6/k. Let us calculate the elliptic genus of the orbifold:
χ(k; −)Zk = 1
k
X
ma,mb∈Zk
˜χma,mb(k; −)
= 1
k
X
m,n∈Zk
e−2πi mamb
k
k−2
2
X
j=0, 1
2,...
e2πimb
2j+1
k Cj
2j+1−2ma(τ, α).
(A.14)
The sum over the variable mb puts ma = 2j + 1 (mod k) and adds a factor of k. We can
most easily eliminate ma from the sum and ﬁnd:
χ(k; −)Zk =
k−2
2
X
j=0, 1
2,...
Cj
−2j−1(τ, α)
= −
k−2
2
X
j=0, 1
2,...
Cj
2j+1(τ, −α).
(A.15)
This is one of the simplest examples of mirror symmetry in conformal ﬁeld theory.
We
recognize the previous to last line as the elliptic genus of the anti-diagonal minimal model.
Note that for these compact models, the Zk orbifold is equivalent to performing T-duality.
A.4
Characters at c > 3
The elliptic genus of N = 2 Liouville theory at radius R =
√
lα′ contains a holomorphic part
and a remainder term, namely it is a completed Appell-Lerch sum ˆA2l:
χ(; l)
=
χhol + χrem
=
iθ11(τ, α)
η3
ˆA2l(z
1
l , z2; q)
χhol(; l)
=
iθ11(τ, α)
η3
X
m∈Z
qlm2z2m
1 −z
1
l qm
χrem(; l)
=
−1
πiθ11(τ, α)
η3
X
w,n∈Z
z
n−lw
l
Z +∞−iǫ
−∞−iǫ
ds
2is + n + lwq
s2
l + (n−lw)2
4l
¯q
s2
l + (n+lw)2
4l (A.16)
24


## Page 26


The holomorphic part of the Liouville elliptic genus can be expanded in terms of the twisted
Ramond sector characters. We have the equation:
χhol(−; l) = iθ11(q, z)
η3
X
m∈Z
qlm2z2m
1 −zqlm
l−1
X
2j−1=0
z
2j−1
l qm(2j−1)
=
l−1
X
2j−1=0
Ch(j; −1
2; q, z) .
(A.17)
We notice that the elliptic genus is expressed as a sum over extended characters. These
correspond to ordinary characters summed over spectral ﬂow orbits that shift the angular
momentum quantum number by multiples of the level l.
The holomorphic part of the cigar elliptic genus can also be written in terms of these
extended characters:
χhol(−; l)Zk(q, z) =
X
m=0,1,...l−1
X
w
iθ11(q, z)
η3
qlw2−mwz2w−m
l
1 −zqlw−m
.
=
k−1
X
2j−1=0
Ch(j; −1
2 −(2j −1); q, z).
(A.18)
The modular and ellipticity properties of the extended characters are (for ma, mb ∈Z):
Ch(j; r′; q, zqmae2πimb) = (−1)ma+mbq−c
6 m2
az−c
3 mae
2πimb(2j+2r′)
l
Ch(j; r′ + ma; q, z).
(A.19)
The angular momentum of the representations corresponding to these characters is 2j + 2r′.
We also have the following transformation rules for the holomorphic and remainder term of
the elliptic genus:
χhol(−; l)(τ, −α)
=
χhol(−; l)(τ, α) −iθ11
η3
X
m∈Z
qkm2z2m
χrem(−; l)(τ, −α)
=
χrem(−; l)(τ, α) + iθ11
η3
X
m∈Z
qkm2z2m.
(A.20)
The extra term is a reminder of the ambiguity of the holomorphic part of the elliptic genus,
due to the bound state spectrum touching the delta-function normalizable continuum. To-
gether, these equations give rise to the equality:
χ(; l)(τ, −α)
=
χ(; l)(τ, α),
(A.21)
which can also be derived directly from the integral representation of the non-compact elliptic
genus.
25


## Page 27


A.5
Twisted building blocks at c > 3
A.5.1
Character formulae
Using these properties, we can calculate the holomorphic part of the twisted blocks for the
Liouville and cigar elliptic genera:
χma,mb(−; l)(τ, α) = e2πi c
6mambe2πi c
6(m2
aτ+2maα)
l−1
X
2j−1=0
Ch(j; −1
2; τ, α + maτ + mb)
= (−1)ma+mbe2πi c
6mamb
l−1
X
2j−1=0
e2πimb
2j−1
l Ch(j; −1
2 + ma; τ, α).
(A.22)
We use the value of the central charge c = 3+6/l, multiply by the phase factor ǫ and obtain:
˜χhol;ma,mb(−; l) = e
2πimamb
l
l−1
X
2j−1=0
e
(2j−1)
k
2πimbCh(j; −1
2 + ma; q, z).
(A.23)
For the cigar, we ﬁnd:
˜χhol;ma.mb(−; l)Zl = e
2πimamb
l
l−1
X
2j−1=0
e
−(2j−1)
l
2πimbCh(j; −1
2 −(2j −1) + ma; q, z).
(A.24)
A.5.2
Twisted blocks for the non-holomorphic sector
For the continuous character part of the elliptic genus we ﬁnd, for the Liouville theory twisted
block:
˜χrem;ma,mb(−; l) = (−1) 1
πiθ11(τ, α)
η3
X
w,n∈Z
e2πi (n+ma)mb
l
z
n−lw+2ma
l
Z +∞−iǫ
−∞−iǫ
ds
2is + n + lwq
s2
l + (n−lw+2ma)2
4l
¯q
s2
l + (n+lw)2
4l
.
(A.25)
For the cigar theory, we end up with:
˜χrem;ma,mb(−; l)Zl = e2πi mamb
l
(−1) 1
πiθ11(τ, α)
η3
X
w,n∈Z
e−2πimb n
l z−n−lw
l
+ 2ma
l
Z +∞−iǫ
−∞−iǫ
ds
2is + n + lwq
s2
l + (n−lw−2ma)2
4l
¯q
s2
l + (n+lw)2
4l
. (A.26)
26


## Page 28


A.5.3
Exact expressions for twisted blocks
Finally, we give the expressions for the complete twisted building blocks, for the Liouville
theory:
˜χma,mb(−; l) = e
2πimamb
l
q
m2a
l z
2ma
l
iθ11(τ, α)
η3
ˆA2l(z
1
l q
ma
l e
2πimb
l
, z2q2ma; q),
(A.27)
and for the cigar theory at radius R =
√
lα′:
˜χma,mb(−; l)Zl = e
2πimamb
l
q
m2a
l z
2ma
l
iθ11(τ, α)
η3
× 1
l
X
m′a,m′
b∈Zl
q−m
′2
a
l e−2πim′an′a
l
ˆA2l(z
1
l q
ma+m′a
l
e
2πi(mb+m′
b)
l
, z2q2ma; q).
(A.28)
References
[1] E. Witten, “On the Landau-Ginzburg description of N=2 minimal models,” Int. J. Mod.
Phys. A 9, 4783 (1994) [arXiv:hep-th/9304026].
[2] E. Witten, “Phases of N=2 theories in two-dimensions,” Nucl. Phys. B 403, 159 (1993)
[hep-th/9301042].
[3] K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil and
E. Zaslow, “Mirror symmetry,” (Clay mathematics monographs. 1)
[4] O. Aharony, M. Berkooz, D. Kutasov and N. Seiberg, “Linear dilatons, NS ﬁve-branes
and holography,” JHEP 9810 (1998) 004 [hep-th/9808149].
[5] A. Giveon, D. Kutasov and O. Pelc, “Holography for noncritical superstrings,” JHEP
9910, 035 (1999) [hep-th/9907178].
[6] T. Eguchi and Y. Sugawara, “Modular invariance in superstring on Calabi-Yau n fold
with ADE singularity,” Nucl. Phys. B 577, 3 (2000) [hep-th/0002100].
[7] T. Eguchi and Y. Sugawara, “D-branes in singular Calabi-Yau n fold and N=2 Liouville
theory,” Nucl. Phys. B 598, 467 (2001) [hep-th/0011148].
[8] T. Eguchi and Y. Sugawara, “SL(2,R) / U(1) supercoset and elliptic genera of noncom-
pact Calabi-Yau manifolds,” JHEP 0405, 014 (2004) [hep-th/0403193].
[9] T. Eguchi and Y. Sugawara,
“Conifold type singularities,
N=2 Liouville and
SL(2:R)/U(1) theories,” JHEP 0501, 027 (2005) [hep-th/0411041].
27


## Page 29


[10] S. K. Ashok, R. Benichou and J. Troost, “Non-compact Gepner Models, Landau-
Ginzburg Orbifolds and Mirror Symmetry,” JHEP 0801, 050 (2008) [arXiv:0710.1990
[hep-th]].
[11] J. Troost, “The non-compact elliptic genus: mock or modular,” JHEP 1006, 104 (2010)
[arXiv:1004.3649 [hep-th]].
[12] T. Eguchi, Y. Sugawara, “Non-holomorphic Modular Forms and SL(2,R)/U(1) Super-
conformal Field Theory,” JHEP 1103 (2011) 107. [arXiv:1012.5721 [hep-th]].
[13] S. K. Ashok, J. Troost, “A Twisted Non-compact Elliptic Genus,” JHEP 1103 (2011)
067. [arXiv:1101.1059 [hep-th]].
[14] T. Kawai, Y. Yamada, S. -K. Yang, “Elliptic genera and N=2 superconformal ﬁeld
theory,” Nucl. Phys. B414 (1994) 191-212. [hep-th/9306096].
[15] P. Di Francesco, O. Aharony, S. Yankielowicz, “Elliptic genera and the Landau-Ginzburg
approach to N=2 orbifolds,” Nucl. Phys. B411 (1994) 584-608. [hep-th/9306157].
[16] P. Berglund, M. Henningson, “Landau-Ginzburg orbifolds, mirror symmetry and the
elliptic genus,” Nucl. Phys. B433 (1995) 311-332. [hep-th/9401029].
[17] P. Berglund, S. H. Katz, “Mirror symmetry constructions: A review,” In *Greene, B.
(ed.), Yau, S.T. (ed.): Mirror symmetry II* 87-113. [hep-th/9406008].
[18] T. Kawai, S. -K. Yang, “Duality of orbifoldized elliptic genera,” Prog. Theor. Phys.
Suppl. 118 (1995) 277-298. [hep-th/9408121].
[19] A. N. Schellekens and N. P. Warner, “Anomalies and Modular Invariance in String
Theory,” Phys. Lett. B 177 (1986) 317.
[20] E. Witten, “Elliptic Genera and Quantum Field Theory,” Commun. Math. Phys. 109
(1987) 525.
[21] P. Di Francesco and S. Yankielowicz, “Ramond sector characters and N=2 Landau-
Ginzburg models,” Nucl. Phys. B 409, 186 (1993) [hep-th/9305037].
[22] K. Hori and A. Kapustin, “Duality of the fermionic 2d black hole and N = 2 Liouville
theory as mirror symmetry,” JHEP 0108, 045 (2001) [arXiv:hep-th/0104202].
[23] D. Israel, A. Pakman and J. Troost, “D-branes in N = 2 Liouville theory and its mirror,”
Nucl. Phys. B 710, 529 (2005) [arXiv:hep-th/0405259].
[24] S. K. Ashok, S. Murthy and J. Troost, “D-branes in non-critical superstrings and
minimal super Yang-Mills in various dimensions,” Nucl. Phys. B 749 (2006) 172
[hep-th/0504079].
28


## Page 30


[25] D. Gepner, “Space-Time Supersymmetry in Compactiﬁed String Theory and Supercon-
formal Models,” Nucl. Phys. B 296 (1988) 757.
[26] B. R. Greene and M. R. Plesser, “Duality In Calabi-yau Moduli Space,” Nucl. Phys. B
338 (1990) 15.
[27] D. Israel, C. Kounnas, A. Pakman and J. Troost, “The Partition function of the super-
symmetric two-dimensional black hole and little string theory,” JHEP 0406 (2004) 033
[hep-th/0403237].
[28] A. Dabholkar, S. Murthy and D. Zagier, unpublished.
[29] S. Zwegers, PhD thesis, “Mock Theta functions”, Utrecht University, 2002.
[30] D. Zagier, “Ramanujan’s mock theta functions and their applications d’apr`es Zwegers
and Bringmann-Ono”, S´eminaire Bourbaki, 986 (2007).
[31] A. M. Semikhatov, A. Taormina and I. Y. .Tipunin, “Higher level Appell functions,
modular transformations, and characters,” math/0311314 [math-qa].
[32] D. Gaiotto, G. W. Moore and A. Neitzke, “Four-dimensional wall-crossing via three-
dimensional ﬁeld theory,” Commun. Math. Phys. 299 (2010) 163 [arXiv:0807.4723 [hep-
th]].
[33] J. Manschot, “BPS invariants of N=4 gauge theory on a surface,” arXiv:1103.0012
[math-ph].
[34] M. Alim,
B. Haghighat,
M. Hecht,
A. Klemm,
M. Rauch and T. Wotschke,
“Wall-crossing holomorphic anomaly and mock modularity of multiple M5-branes,”
arXiv:1012.1608 [hep-th].
[35] M. -x. Huang, A. -K. Kashani-Poor and A. Klemm, “The Omega deformed B-model for
rigid N=2 theories,” arXiv:1109.5728 [hep-th].
29

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1204_3802v2_elliptic_genera_of_non_compact_gepner_models_and_mirror_symmetry
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2012/1204_3802V2_ELLIPTIC_GENERA_OF_NON_COMPACT_GEPNER_MODELS_AND_MIRROR_SYMMETRY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

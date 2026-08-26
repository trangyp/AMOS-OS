---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1107.2713
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1107.2713_On_toric_schemes

> Source: 1107.2713_On_toric_schemes.pdf

> Pages: 7

---


## Page 1


arXiv:1107.2713v2  [math.AG]  26 Jul 2014
ON TORIC SCHEMES
FRED ROHRER
Abstract. Studying toric varieties from a scheme-theoretical point of view
leads to toric schemes, i.e. “toric varieties over arbitrary base rings”.
It is
shown how the base ring aﬀects the geometry of a toric scheme. Moreover,
generalisations of results by Cox and Mustaţˇa allow to describe quasicoherent
sheaves on toric schemes in terms of graded modules. Finally, a toric version
of the Serre-Grothendieck correspondence relates cohomology of quasicoherent
sheaves on toric schemes to local cohomology of graded modules.
0. From toric varieties to toric schemes
During the last forty years a huge amount of work on toric varieties was and still
is published. Their theory was generalised in several directions, and this often lead
to a better understanding of classical toric varieties. However, the generalisation
that seems to be the most natural and the most important – the study of toric
varieties from a scheme-theoretical point of view – was never actually carried out.
It is clear that to do this one has to be able to make arbitrary base changes. Hence,
instead of considering toric varieties over an algebraically closed ﬁeld (or, as often
done, over the ﬁeld of complex numbers), one needs to study toric schemes, that is
“toric varieties over arbitrary base rings”. Special cases of this generalisation were
mentioned brieﬂy in [3, §4] (for regular fans and mainly over the ring of integers)
and [9, IV.3] (over discrete valuation rings). But unfortunately later authors seemed
to ignore this, and hence the knowledge of toric schemes is very small compared to
the one of toric varieties.
Besides yielding a better understanding of the geometry of toric varieties, there
are concrete applications of the above generalisation, as the following remark shows.
(0) Let X be the toric variety over an algebraically closed ﬁeld K associated
with a fan Σ. A fundamental question in algebraic geometry is then if the Hilbert
functor HilbX/K of X over K is representable, i.e.
if the Hilbert scheme of X
exists (cf. [7]). If X is projective, then this is indeed the case and follows from
Grothendieck’s more general result [7, Théorème 3.1]. However, toric varieties are
not necessarily projective, and in general it is not known whether their Hilbert
schemes exist. Studying HilbX/K amounts to studying quasicoherent sheaves on
the base change X ⊗K R for every K-algebra R, and it turns out that X ⊗K R is
the same as the toric scheme over R associated with Σ. Hence, in order to study
2010 Mathematics Subject Classiﬁcation. Primary 14M25; Secondary 13A02, 13D45.
Key words and phrases. Toric scheme, toric variety, graded module, sheaf cohomology, local
cohomology.
This
is
a
slightly
updated
and
corrected
version
of
the
author’s
contribution
to
the Proceedings of the 32nd Symposium and the 6th Japan-Vietnam Joint Seminar on
Commutative
Algebra,
held
in
December
2010
in
Hayama,
Japan.
The
author
was
supported by the Swiss National Science Foundation.
1


## Page 2


2
FRED ROHRER
Hilbert functors of toric varieties it is necessary to study toric schemes over more
general bases than just over algebraically closed ﬁelds.
The development of a theory of toric schemes was begun in the PhD Thesis [11],
and its contents were reﬁned and extended in [12], [13] and [14]. Here we give an
overview of the most important results and refer the reader to the aforementioned
sources for a more extensive treatment including proofs.
1. The geometry of toric schemes
We start by brieﬂy describing the construction of toric schemes from fans. In
[13], toric schemes are obtained as a special case of the more general construction
of schemes from so-called openly immersive projective systems of monoids (also
yielding the Cox schemes introduced below).
•
From now on let V be an
R-vector space of ﬁnite dimension n, let N be a
Z-
structure on V (i.e. a subgroup of rank n of the additive group underlying V with
⟨N⟩
R = V ), and let M := N ∗denote the dual of N which is a
Z-structure on the
dual V ∗of V .
An N-polycone (in V ) is the set of
R-linear combinations with coeﬃcients in
R≥0
of a ﬁnite subset of N, and an N-polycone is called sharp if it does not contain a
line. If σ is an N-polycone then a face of σ is a set of the form σ ∩Ker(u) for some
u ∈σ∨∩M (where E∨:= {v ∈V ∗| v(E) ⊆
R≥0} for a subset E ⊆V ). The set
of faces of a (sharp) N-polycone is a ﬁnite set of (sharp) N-polycones. An N-fan
(in V ) is a ﬁnite set Σ of sharp N-polycones that is closed under taking faces and
such that the intersection of two cones in Σ is a common face of both of them. By
means of the relation “τ is a face of σ”, denoted by τ ≼σ, we consider an N-fan as
an ordered set.
•
From now on let Σ be an N-fan in V and let R be a ring1.
If σ ∈Σ then σ∨∩M is a torsionfree, cancellable, ﬁnitely generated submonoid
of M, and if moreover τ ≼σ then σ∨∩M is a submonoid of τ ∨∩M. Taking
spectra of algebras of monoids over R and setting Xσ(R) := Spec(R[σ∨∩M]) for
σ ∈Σ we get an inductive system (Xσ(R))σ∈Σ of R-schemes over Σ. Its inductive
limit exists and is an R-scheme denoted by XΣ(R) →Spec(R) and called the toric
scheme over R associated with Σ (and N). It can be understood as obtained by
glueing (Xσ(R))σ∈Σ along (Xσ∩τ(R))(σ,τ)∈Σ2.
The above construction of toric schemes gives rise to a contravariant functor XΣ
from the category of rings to the category of schemes together with a morphism
XΣ →Spec.
Moreover, the functor XΣ is compatible with base change in the
following sense.
(1) Proposition
([13, 1.6]) There is a canonical isomorphism
XΣ(•) ∼= XΣ(R) ⊗R •
of contravariant functors from the category of R-algebras to the category of R-
schemes.
1By a ring, group or monoid we always mean a commutative ring, group or monoid, respectively,
and by an algebra we always mean a commutative, unital and associative algebra.


## Page 3


ON TORIC SCHEMES
3
In particular, if a ⊆R is an ideal then XΣ(R/a) is canonically identiﬁed with a
closed subscheme of XΣ(R).
The ﬁrst important question is now of course how the base ring aﬀects the
geometry of a toric scheme. It turns out that some basic properties hold for all
toric schemes, making them a class of “nice schemes”. More precisely, on use of the
above base change property we get the following result.
(2) Proposition
([13, 3.4]) The R-scheme XΣ(R) →Spec(R) is separated, qua-
sicompact, ﬂat, and of ﬁnite presentation; it is faithfully ﬂat if and only if Σ ̸= ∅
or R = 0.
In contrast, a lot of other basic properties are respected and reﬂected by XΣ.
The following statements are proved by reducing to the aﬃne case, i.e. Xσ, and
then applying corresponding results about algebras of monoids (see e.g. [6]).
(3) Proposition
([13, 3.4]) a) The scheme XΣ(R) is reduced, connected, or nor-
mal if and only if R is so or Σ = ∅; it is irreducible, or integral if and only if R is
so and Σ ̸= ∅.
b) If Σ ̸= ∅then there is a bijection p 7→XΣ(R/p) from the set of minimal
prime ideals of R to the set of irreducible components of XΣ(R).
c) The scheme XΣ(R) is Noetherian if and only if R is so or Σ = ∅; it is Artinian
if and only if R is so and n = 0, or R = 0, or Σ = ∅.
d) If Σ ̸= ∅then
dim(R) + n ≤dim(XΣ(R)) ≤(n + 1) dim(R) + n;
if R is moreover Noetherian then dim(R) + n = dim(XΣ(R)).
e) If R is Noetherian, then XΣ(R) is equidimensional if and only if R is so or
Σ = ∅.
The above shows in particular that on general toric schemes no satisfying theory
of Weil divisors is available. Since a lot of results about toric varieties were proved
by heavy use of Weil divisor techniques (see e.g. [2], [5]), one has to come up with
new proofs in order to generalise these results to toric schemes.
Finally, as an example of a property depending on the fan but not on the base ring
we consider properness. Its characterisation needs the notion of a complete N-fan
Σ, i.e. an N-fan Σ with S Σ = V . This result is well-known for toric varieties (see
e.g. [5, 2.4]), and proved on use of torus operations for toric schemes associated with
regular fans in [3, §4 Proposition 4]. Our proof for arbitrary fans avoids speaking
of torus operations and relies only on the valuative criterion for properness and on
properties of projections of fans proved in [12].
(4) Proposition
The R-scheme XΣ(R) →Spec(R) is proper if and only if Σ is
complete, or Σ = ∅, or R = 0.
2. Sheaves on toric schemes
Generalising work by Cox [2] and Mustaţˇa [10] we introduce a notion of Cox
ring (not to be confused with the one introduced in [8]) and describe quasicoherent
modules on toric schemes in terms of graded modules over these rings. In order to
do so we need to deﬁne some objects encoding the combinatorics of the fan Σ.


## Page 4


4
FRED ROHRER
Let Σ1 denote the set of 1-dimensional cones in Σ. Every ρ ∈Σ1 has a unique
minimal N-generator (i.e. an x ∈N with ρ =
R≥0x such that rx /∈N for every
r ∈]0, 1[), denoted by ρN. There is an exact sequence of groups
M
c
−→
ZΣ1
a
−→A −→0,
where c(u) := (u(ρN))ρ∈Σ1 for u ∈M and where a is deﬁned as the cokernel of c.
Note that c is a monomorphism if and only if Σ if full, i.e. ⟨S Σ⟩
R = V . We denote
by (δρ)ρ∈Σ1 the canonical basis of
ZΣ1 and we set αρ := a(δρ) for ρ ∈Σ1.
Now, we denote by S the polynomial algebra R[(Zρ)ρ∈Σ1] in indeterminates
(Zρ)ρ∈Σ1 over R, furnished with the A-graduation induced by a, i.e. such that
deg(Zρ) = αρ for ρ ∈Σ1.
For σ ∈Σ we set bZσ := Q
ρ∈Σ1\σ1 Zρ ∈S (where
σ1 denotes the set of 1-dimensional faces of σ). Finally we deﬁne a graded ideal
I := ⟨bZσ | σ ∈Σ⟩S.
•
From now on let B ⊆A be a subgroup.
The B-graded R-algebra SB := L
α∈B Sα obtained from S by degree restriction
to B is called the B-restricted Cox ring over R associated with Σ1 (and N), and its
graded ideal IB := I∩SB is called the B-restricted irrelevant ideal over R associated
with Σ (and N). One can show that IB is generated by ﬁnitely many monomials.
To proceed we need to “invert the monomials bZσ in the Cox ring”, and hence we
have to assure that some power of these monomials lies in SB. This amounts to
supposing that B is big, i.e. it has ﬁnite index in A.
•
From now on suppose that B is big, so that there exists m ∈
N0 with bZm
σ ∈SB
for every σ ∈Σ.
For σ ∈Σ the B-graded ring of fractions (SB) b
Zm
σ is independent of the choice of
m. Its component of degree 0 is independent of the choice of B and is denoted by
S(σ). Moreover, for τ ≼σ there is a canonical morphism of rings S(σ) →S(τ) which
is independent of m and B. Taking spectra and setting Y(σ)(R) := Spec(S(σ)) for
σ ∈Σ we obtain an inductive system (Yσ(R))σ∈Σ of R-schemes over Σ. Its inductive
limit exists and is an R-scheme denoted by YΣ(R) →Spec(R) and called the Cox
scheme over R associated with Σ (and N). It can be understood as obtained by
glueing (Yσ(R))σ∈Σ along (Yσ∩τ(R))(σ,τ)∈Σ2.
The above construction of Cox schemes gives rise to a contravariant functor YΣ
from the category of rings to the category of schemes together with a morphism
YΣ →Spec, and YΣ is compatible with base change in the sense of (1).
Cox schemes are closely related to toric schemes as follows. The morphism of
groups c: M →
ZΣ1 induces morphisms of rings R[σ∨∩M] →S(σ) for σ ∈Σ, and
these induce a canonical morphism of contravariant functors γ : YΣ →XΣ. Then,
we have the following result.
(5) Proposition
([14, 3.3.3]) The canonical morphism of contravariant functors
γ : YΣ →XΣ is an isomorphism if and only if Σ is full.
Using the (non-canonical) procedure to consider a toric scheme associated with
a non-full fan as a toric scheme associated with a full fan ([13, 3.3]) it is suﬃcient to
study from now on Cox schemes instead of toric schemes. (Note that this reduction
demands a base change and is in general not available for toric varieties.)
Now we are ready to explain how B-graded SB-modules give rise to quasicoherent
sheaves on YΣ(R). We denote by GrModB(SB) and QCMod(OYΣ(R)) the categories


## Page 5


ON TORIC SCHEMES
5
of B-graded SB-modules and of quasicoherent OYΣ(R)-modules. Moreover, for a B-
graded SB-module F we denote by F(σ) the component of degree 0 of the B-graded
module of fractions F b
Zm
σ = F ⊗SB (SB) b
Zm
σ , and for an S(σ)-module G we denote by
eG the OYσ(R)-module associated with G.
(6) Proposition
([14, 4.1.1]) There exists a unique functor
SB : GrModB(SB) →QCMod(OYΣ(R))
with SB(F)↾Yσ(R)= g
F(σ) for every σ ∈Σ and every B-graded SB-module F.
Since SB coincides locally with the canonical equivalence between modules and
quasicoherent sheaves on aﬃne schemes it is exact and commutes with inductive
limits. Furthermore, denoting by •(α) the functor of shifting degrees by α, we can
construct a right quasiinverse
ΓB
∗(•) :=
M
α∈B
Γ
 YΣ(R),
 • ⊗OYΣ(R) SB(SB(α))

for SB, called the ﬁrst total functor of sections associated with Σ and B over R.
Thus, we get the following generalisation of [10, Theorem 1.1], itself a generalisation
of [2, Theorem 3.2].
(7) Theorem
([14, 4.4.3]) The functor SB : GrModB(SB) →QCMod(OYΣ(R)) is
essentially surjective.
Next, we restrict our attention to ideals. A graded ideal a ⊆SB is called IB-
saturated if a = S
k∈N0(a :SB Ik
B). Let
Jsat
B
and e
J denote the sets of IB-saturated
graded ideals of SB and of quasicoherent ideals of OYΣ(R), respectively. Then, SB
induces by exactness a map ΞB :
Jsat
B
→e
J. The next result treats the question
whether this map is surjective or injective. To get injectivity, besides being big the
subgroup B must not be “too big”. More precisely, B is called small (with respect
to Σ) if it is contained in T
σ∈Σ⟨{αρ | ρ ∈Σ1 \ σ1}⟩
Z.
(8) Theorem
([14, 4.4.9]) The map ΞB :
Jsat
B →e
J is surjective, and if B is small
then it is bijective.
An example of a subgroup that is big and small (and moreover well understood)
is given in the following remark (cf. [4, V.5]).
Consider a family (Uσ)σ∈Σ of subsets of V ∗such that for every σ ∈Σ there exists
a (not necessarily unique) mσ ∈M with Uσ = mσ + σ∨. Such a family is called a
virtual polytope over Σ if τ ⊆Ker(mσ −mτ) for all σ, τ ∈Σ with τ ≼σ, and this
condition is independent of the choice of the family (mσ)σ∈Σ. There is a canonical
structure of group on the set of virtual polytopes over Σ, and the set of virtual
polytopes of the form (m + σ∨)σ∈Σ is a subgroup. The corresponding quotient
group is denoted by Pic(Σ) and called the Picard group of Σ. It can be considered
as the group of virtual polytopes over Σ modulo M-rational translations.
The map
(mσ + σ∨)σ∈Σ 7→(mρ(ρN))ρ∈Σ1
yields a monomorphism from the group of virtual polytopes over Σ to
ZΣ1, and
this induces a monomorphism Pic(Σ) ֌ A by means of which we consider Pic(Σ)
as a subgroup of A. Then, Pic(Σ) is small, and if Σ is simplicial then Pic(Σ) is big.
Hence, it provides an example of a subgroup of A to which (8) can be applied.


## Page 6


6
FRED ROHRER
Finally, since Pic(Σ) ∼= Pic(XΣ(C)) by [4, Theorem VII.2.15] we get back [2,
Corollary 3.9] as a special case.
3. Cohomology on toric schemes
Our results about quasicoherent sheaves in the last section reveals that toric
schemes (or more precisely, Cox schemes) are very similar to projective schemes.
Hence, we ask if there is a toric version of the Serre-Grothendieck correspondence
(cf. [1, 20.4.4]), relating cohomology of quasicoherent sheaves on a Cox scheme to
graded local cohomology of B-graded SB-modules with respect to the irrelevant
ideal IB. This is indeed the case.
First, we have to explain what we mean by graded local cohomology. We denote
by
BΓIB : GrModB(SB) →GrModB(SB)
the B-graded IB-torsion functor. Its right derived cohomological functor is denoted
by (BHi
IB)i∈Z and called B-graded local cohomology with respect to IB. The reason
for this clumsy notation is that the ungraded module underlying a graded local
cohomology module of a graded module F might not be the same as the local
cohomology module of the ungraded module underlying F. (A suﬃcient condition
for this to hold is coherence of the graded ring SB.)
Next, we introduce a variant of sheaf cohomology that is useful for our purpose.
We deﬁne a functor
ΓB
∗∗(•): GrModB(SB) →GrModB(SB),
called the second total functor of sections associated with Σ and B over R, by
setting
ΓB
∗∗(•) :=
M
α∈B
Γ(YΣ(R), SB(•(α))).
Note that despite its name it is deﬁned on the category GrModB(SB). However, by
(7) this is merely a technical point. The reason for two (in general diﬀerent) total
functors of sections is that the canonical morphism
SB(•) ⊗OYΣ(R) SB(SB(α)) →SB(•(α))
is not necessarily an isomorphism.
The right derived cohomological functor of
ΓB
∗∗(•) is denoted by (Hi
∗∗,B)i∈Z and contains the usual sheaf cohomology as a
direct summand.
To go on we need a certain behaviour of injectives in the category GrModB(SB).
Namely, the B-graded ring SB is said to have the ITR-property with respect to IB
if every B-graded IB-torsion SB-module has an injective resolution whose compo-
nents are B-graded IB-torsion SB-modules. This is fulﬁlled for example if SB is
Noetherian (as a graded ring), and in particular if R is Noetherian. Using this
notion and imitating the corresponding proof in the projective case we arrive at the
Toric Serre-Grothendieck Correspondence.
(9) Theorem
([14, 4.5.4]) If SB has the ITR-property with respect to IB, then
there exist an exact sequence of functors
0 −→BΓIB −→IdGrModB(SB) −→ΓB
∗∗
ζB
−→BH1
IB −→0


## Page 7


ON TORIC SCHEMES
7
and a unique morphism of δ-functors
(ζi
B)i∈Z :
 Hi
∗∗,B

i∈Z −→
 BHi+1
IB

i∈Z
with ζ0
B = ζB, and ζi
B is an isomorphism for every i ∈
N.
As an application we can prove a toric version of Serre’s Finiteness Theorem.
(10) Proposition
([14, 4.5.5]) Let F be a ﬁnitely generated B-graded SB-module,
and suppose that Σ is complete and that R is Noetherian. Then, the R-modules
Hi
∗∗,B(F)α and BHi
IB(F)α are ﬁnitely generated for every i ∈
Z and every α ∈B.
Considering the ﬁbres of a toric scheme, this allows us to deﬁne and investigate
Hilbert functions of toric schemes, a task we would like to address in future re-
search. Note that the above hypothesis of a complete fan Σ can be achieved by the
Completion Theorem ([12]).
References
[1]
M. P. BRODMANN, R. Y. SHARP, Local cohomology: an algebraic introduction with geo-
metric appplications. Cambridge Stud. Adv. Math. 60, Cambridge Univ. Press, Cambridge,
1998.
[2]
D. A. COX, The homogeneous coordinate ring of a toric variety. J. Algebraic Geom. 4 (1995)
17–50.
[3]
M. DEMAZURE, Sous-groupes algébriques de rang maximum du groupe de Cremona. Ann.
Sci. École Norm. Sup. (4) 3 (1970), 507–588.
[4]
G. EWALD, Combinatorial convexity and algebraic geometry. Grad. Texts in Math. 168,
Springer-Verlag, New York, 1996.
[5]
W. FULTON, Introduction to toric varieties. Ann. of Math. Stud. 131, Princeton University
Press, Princeton, 1993.
[6]
R. GILMER, Commutative semigroup rings. Chicago Lectures in Math., University of
Chicago Press, Chicago, 1984.
[7]
A. GROTHENDIECK, Techniques de construction et théorèmes d’existence en géométrie
algébrique. IV: Les schémas de Hilbert. Séminaire Bourbaki 6, Exp. 221 (249–276), Soc.
Math. France, Paris, 1995.
[8]
Y. HU, S. KEEL, Mori dream spaces and GIT. Michigan Math. J. 48 (2000), 331–348.
[9]
G. KEMPF, F. F. KNUDSEN, D. MUMFORD, B. SAINT-DONAT, Toroidal embeddings I.
Lecture Notes in Math. 339, Springer-Verlag, Berlin, 1973.
[10] M. MUSTAŢˇA, Vanishing theorems on toric varieties. Tohoku Math. J. (2) 54 (2002), 451–
470.
[11] F.
ROHRER,
Toric
schemes.
Dissertation,
Universität
Zürich,
2010
(available
at
www.dissertationen.uzh.ch).
[12] F. ROHRER, Completions of fans. J. Geom. 100 (2011), 147–169.
[13] F. ROHRER, The geometry of toric schemes. J. Pure Appl. Algebra 217 (2013), 700–708.
[14] F. ROHRER, Quasicoherent sheaves on toric schemes. Expo. Math. 32 (2014), 33–78.
Institute of Mathematics, Vietnam Academy of Science and Technology, 18 Hoàng
Quốc Việt, 10307 Hà Nội, Việt Nam
E-mail address: fredrohrer0@gmail.com

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1107_2713_on_toric_schemes
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2011/1107_2713_ON_TORIC_SCHEMES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

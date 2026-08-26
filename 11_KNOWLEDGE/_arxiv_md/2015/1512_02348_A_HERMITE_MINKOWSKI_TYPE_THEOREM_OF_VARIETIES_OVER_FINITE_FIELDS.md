---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1512.02348
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1512.02348_A_Hermite-Minkowski_type_theorem_of_varieties_over_finite_fields

> Source: 1512.02348_A_Hermite-Minkowski_type_theorem_of_varieties_over_finite_fields.pdf

> Pages: 26

---


## Page 1


arXiv:1512.02348v3  [math.NT]  9 Dec 2016
A Hermite-Minkowski type theorem of
varieties over ﬁnite ﬁelds
Toshiro Hiranouchi
June 28, 2018
We show the ﬁniteness of ´etale coverings of a variety over a ﬁnite ﬁeld
with given degree whose ramiﬁcation bounded along an eﬀective Cartier di-
visor. The proof is an application of P. Delgine’s theorem [4] (H. Esnault and
M. Kerz in Acta Math. Vietnam. 37:531–562, 2012) on a ﬁniteness of l-adic
sheaves with restricted ramiﬁcation.
By applying our result to a smooth
curve over a ﬁnite ﬁeld, we obtain a function ﬁeld analogue of the classical
Hermite-Minkowski theorem.
1 Introduction
For a number ﬁeld F, that is, a ﬁnite extension of Q, the Hermite-Minkowski theorem
asserts that there exist only ﬁnitely many extensions of the number ﬁeld F with given
degree unramiﬁed outside a ﬁnite set of primes of F (e.g., [15], Chap. III, Thm. 2.13;
[5], Chap. V, Thm. 2.6). In [5], G. Faltings gave a higher dimensional generalization of
this theorem stated as follows:
Theorem 1.1 ([5], Chap. VI, Sect. 2.4; [9], Thm. 2.9). Let X be a connected scheme
of ﬁnite type and dominant (e.g., ﬂat) over SpecpZq. Then there exist only ﬁnitely
many ´etale coverings of X with given degree.
Here, an ´etale covering of X means a ﬁnite ´etale morphism X1 Ñ X. The aim of this
note is to give a “function ﬁeld” analogue of this theorem. We begin simple observations:
˝ For a function ﬁeld F of one variable over a ﬁnite ﬁeld with characteristic p, the
Artin-Schreier equations produce inﬁnitely many extensions of F of degree p which
ramify only in a ﬁnite set of places (see e.g., [7], Sect. 8.23).
˝ For a number ﬁeld F, (the exponents of) the discriminant of an extension of F
has an upper bound depending on the extension degree and the primes at which it
ramiﬁes ([16], Chap. III, Sect. 6, Prop. 13, see also remarks after the proposition).
Under the conditions in the Hermite-Minkowski theorem, namely, the extension
1


## Page 2


degree and a ﬁnite set of primes are given, the discriminants of extensions of F are
automatically bounded.
Considering these facts together, to obtain a ﬁniteness as above in the case of function
ﬁelds we have to restrict ramiﬁcation.
Now, we present the results in this note more precisely. Let X be a connected and
separated scheme of ﬁnite type over a ﬁnite ﬁeld (we call such schemes just varieties in
the following cf. Notation), and X a compactiﬁcation of X (cf. Sect. 2). For an eﬀective
Cartier divisor D with support |D| Ă Z “ X ∖X, we will introduce the notion of
bounded ramiﬁcation along D for ´etale coverings of X (whose ramiﬁcation locus is in the
boundary Z) in the next section (Def. 2.2). Adopting this notion, we show the following
theorem.
Theorem 1.2 (Thm. 3.4). Let X Ă X be as above. There exist only ﬁnitely many
´etale coverings of X with bounded degree and ramiﬁcation bounded by a given eﬀective
Cartier divisor D with support in Z “ X ∖X.
A key ingredient for the proof is (a weak form of) Deligne’s ﬁniteness theorem on smooth
Weil sheaves with bounded ramiﬁcation [4] (Thm. 3.3).
For an ´etale covering X1 Ñ X of smooth curves over a ﬁnite ﬁeld, if its degree and the
discriminant are bounded, then the ramiﬁcation of the covering X1 Ñ X in our sense is
also bounded (Prop. 2.9):
bounded degree & discriminant ñ bounded ramiﬁcation.
From this, we obtain an alternative proof of the following well-known theorem:
Corollary 1.3 ([7], Thm. 8.23.5). Let F be a function ﬁeld of one variable over a
ﬁnite ﬁeld. Then there exist only ﬁnitely many separable extensions of F with bounded
degree and discriminant.
On the other hand, we have another implication
bounded degree & ramiﬁcation ñ bounded discriminant
(see Rem. 2.12). As a result, Thm. 1.3 is equivalent to the main theorem (Thm. 1.2) for
the case where X is a smooth curve over a ﬁnite ﬁeld.
Contents
The contents of this note is the following:
• Sect. 2 :
2


## Page 3


– We deﬁne the notion of bounded ramiﬁcation along an eﬀective Cartier divisor
D for ´etale coverings of a variety X over a ﬁnite ﬁeld (Def. 2.1).
We also
introduce the fundamental group π1pX, Dq which classiﬁes such ´etale coverings
of X with bounded ramiﬁcation along D (Def. 2.2).
– We deﬁne the Swan conductor of smooth Ql-sheaves as in [4] (Def. 2.14). In
Lem. 2.17, we give a relation between the Swan conductor of smooth Ql-sheaf
and our notion of the bounded ramiﬁcation.
• Sect. 3 :
– We interpret the Hermite-Minkowski type ﬁniteness as above into a property
of proﬁnite groups called smallness which is studied in [9] (Def. 3.1).
– The proof of the main theorem (Thm. 3.4) is given by showing the smallness
of the fundamental group π1pX, Dq.
– We also provide some applications of our main theorem to a ﬁniteness of repre-
sentations (with ﬁnite images) of the fundamental group π1pX, Dq (Cor. 3.6).
Notation
In this note, a local ﬁeld is a complete discrete valuation ﬁeld with perfect residue ﬁeld.
For such a local ﬁeld K, we denote by
• OK : the valuation ring of K, and
• vK : the valuation of K normalized as vKpKˆq “ Z.
For a ﬁeld F, we denote by
• F : a separable closure of F, and
• GF :“ GalpF{Fq : the Galois group of F over F.
We also use the following notation:
• p : a ﬁxed prime number,
• l : a prime number ‰ p, and
• k : a ﬁnite ﬁeld of characteristic p.
Throughout this note, we assume that l is invertible in all schemes we consider. For
a scheme X, an ´etale covering of X we mean a ﬁnite ´etale morphism X1 Ñ X. A
variety over k means a separated and connected scheme of ﬁnite type over Specpkq. A
curve over k is a variety over k with dimension 1. For an integral variety X over k, we
denote by
• kpXq : the function ﬁeld of X.
Following [6], Sect. 3.2, we call a pair pX, xq of a scheme and a geometric point x of X
a pointed scheme. A morphism f : pX1, x1q Ñ pX, xq of pointed schemes means a
morphism f : X1 Ñ X of schemes with fpx1q “ x.
3


## Page 4


Acknowledgments
The author would like to thank Professor Yuichiro Taguchi for helpful advice and com-
ments on Lem. 2.17, and the proof of Thm. 3.4. Thanks also are due to Shinya Harada,
and Takahiro Tsushima for fruitful discussions and valuable suggestions on this note.
This work was supported by JSPS KAKENHI Grant Number 25800019.
2 Ramiﬁcation
Adding to Notation, throughout this note, we use the following notation: For a variety
X over a ﬁnite ﬁeld k (cf. Notation),
• X : a compactiﬁcation of X (over Specpkq) by Nagata’s theorem (cf. [14]), that is,
a proper scheme over Specpkq which contains X as a dense open subscheme,
• Z :“ X ∖X : the boundary of X,
• CupXq : the set of the normalizations of closed integral subschemes of X of dimen-
sion 1, and
• Div`
ZpXq : the monoid of eﬀective Cartier divisors D on X whose support |D| is in
Z.
For each φ : C Ñ X P CupXq, we denote by
• C : the smooth compactiﬁcation of C (which exists uniquely by a resolution of
singularities),
• φ : C Ñ X : the canonical extension of φ (by the valuative criterion of properness),
and
• kpCqx : the completion of the function ﬁeld kpCq at x P C which is a local ﬁeld in
our sense.
For a ﬁnite Galois extension L{K of local ﬁelds, we use the following ramiﬁcation ﬁltra-
tions (cf. [16], Chap. IV, Sect. 3):
• pGalpL{KqµqµPRě´1 : the ramiﬁcation ﬁltration of GalpL{Kq in the lower numbering
which is given by
GalpL{Kqµ “ t σ P GalpL{Kq | vLpσpθq ´ θq ě µ ` 1 u ,
(1)
where θ P L is a generator of the valuation ring OL as an OK-algebra: OL “ OKrθs
([16], Chap. III, Sect. 6, Prop. 12). For each µ P Rě´1, GalpL{Kqµ is a normal
subgroup of GalpL{Kq. In particular, it is known that GalpL{Kq1 is the p-Sylow
subgroup of the inertia subgroup GalpL{Kq0, where p is the characteristic of the
residue ﬁeld of K.
• pGalpL{KqλqλPRě´1 : the ramiﬁcation ﬁltration of GalpL{Kq in the upper numbering
which is deﬁned by the relation
GalpL{KqϕL{Kpµq “ GalpL{Kqµ,
(2)
4


## Page 5


where ϕL{K : Rě´1 Ñ Rě´1 is the Herbrand function
ϕL{Kpµq “
ż µ
0
dx
pGalpL{Kq0 : GalpL{Kqxq
(3)
and its inverse function is denoted by ψL{K.
We note here, these ramiﬁcation ﬁltrations satisfy the following compatibility properties:
Lemma 2.1 ([16], Chap. IV, Sect. 1, Prop. 2, and Sect. 3, Prop. 14). Let L{K be a
ﬁnite Galois extension of local ﬁelds.
piq For a sub extension K1{K of L, we have
GalpL{K1qµ “ GalpL{Kqµ X GalpL{K1q,
for any µ P Rě´1.
piiq For a sub Galois extension K1{K of L, we have
GalpK1{Kqλ “ GalpL{Kqλ GalpL{K1q{ GalpL{K1q,
for any λ P Rě´1.
For a local ﬁeld K, from Lem. 2.1 (ii) one can introduce
• pGλ
KqλPRě´1 : the ramiﬁcation ﬁltration of GK “ GalpK{Kq (in the upper number-
ing) which is given by
Gλ
K “
lim
ÐÝ
L{K: ﬁnite Galois Ă K
GalpL{Kqλ,
(4)
and
• Gλ`
K :“ the topological closure of Ť
λ1ąλ Gλ1
K in GK for λ P Rě0.
´Etale coverings
Deﬁnition 2.2 (cf. [9], Def. 3.2).
piq Let K be a local ﬁeld. For a separable ﬁeld
extension L{K (contained in K) and λ P Rě0, we say that the ramiﬁcation of
L{K is bounded by λ if we have Gλ`
K Ă GL “ GalpK{Lq.
piiq Let X be a smooth curve over k, and X the smooth compactiﬁcation of X. Let
D “ ř
zPZ mzrzs P Div`
ZpXq (mz P Zě0). An ´etale covering X1 Ñ X is said
to be of ramiﬁcation bounded by D if the extension kpX1qz1{kpXqz of local
ﬁelds is of ramiﬁcation bounded by mz for all z P Z (putting mz “ 0 if z R |D|)
and for all z1 P X1 above z.
5


## Page 6


piiiq Let X be a variety over k. For D P Div`
ZpXq, an ´etale covering X1 Ñ X is said
to be of ramiﬁcation bounded by D if for every φ : C Ñ X P CupXq and
for each irreducible component C1 of C ˆX X1, the ramiﬁcation of the induced
morphism C1 Ñ C is bounded by φ
˚D, where φ
˚D is the inverse image of D by
φ : C Ñ X (for the existence of φ ˚D, see Lem. 2.7 below).
Lemma 2.3. Let L{K be a ﬁnite separable extension of local ﬁelds.
piq The extension L{K is tamely ramiﬁed if and only if it is of ramiﬁcation bounded
by 0.
piiq We denote by rL the Galois closure of L{K. For any λ P Rě0, the extension L{K
is of ramiﬁcation bounded by λ if and only if rL{K is of ramiﬁcation bounded by
λ.
piiiq Assume that the extension L{K is Galois. For any λ P Rě0, the ramiﬁcation of
L{K is bounded by λ if and only if GalpL{Kqλ1 “ t 1 u for any λ1 ą λ.
Proof. (ii) The “if” part follows immediately from the deﬁnition. We show the “only if”
part. Assume that L{K is of ramiﬁcation bounded by λ for some λ P Rě0. Namely, we
have Gλ`
K Ă GL. Since GrL “ GalpK{rLq is the maximal normal subgroup of GK which
is contained in GL, we have Gλ`
K Ă GrL.
(iii) The restriction GK ։ GalpL{Kq; σ ÞÑ σ|L induces Gλ
K ։ GalpL{Kqλ from the
very deﬁnition of Gλ
K in (4) for any λ.
For any λ1 ą λ, Gλ1
K Ă GL if and only if
GalpL{Kqλ1 “ t 1 u, and the assertion follows from it.
(i) By taking the Galois closure of the extension L{K and using (ii), we may assume
that L{K is a Galois extension. Let p be the characteristic of the residue ﬁeld of K.
As Ş
λą0 GalpL{Kqλ “ GalpL{Kq1 is the p-Sylow subgroup of the inertia subgroup
GalpL{Kq0, the extension L{K is tamely ramiﬁed if and only if GalpL{Kqλ “ t 1 u for
any λ ą 0. The assertion (i) follows from (iii).
□
For a pointed connected Noetherian scheme pX, xq (cf. Notation), we deﬁne
• CovpXq : the Galois category of ´etale coverings of X,
• π1pX, xq : the fundamental group of pX, xq associated to CovpXq, which is deﬁned
by
π1pX, xq “
lim
ÐÝ
pX1,x1qPCovpXq
AutXpX1qop,
where the projective limit is taken over a projective system of pointed Galois cov-
erings pX1, x1q Ñ pX, xq in CovpXq ([8], Exp. V, Sect. 7), and
• pπ1pX, xq-setsq : the category of ﬁnite sets on which π1pX, xq acts continuously on
the left.
6


## Page 7


The ﬁber functor Y ÞÑ HomXpx, Y q gives an equivalence of categories
CovpXq
» / pπ1pX, xq-setsq
(5)
([8], Exp. V, Prop. 5.8; [6], Thm. 3.2.12).
Now, we assume that X is a variety over k (cf. Notation). For D P Div`
ZpXq, the
full subcategory CovpX Ă X, Dq Ă CovpXq of ´etale coverings of X with ramiﬁcation
bounded by D also forms a Galois category (see [9], Lem. 3.3).
Deﬁnition 2.4. Associated to the Galois category CovpX Ă X, Dq, we deﬁne the
fundamental group by
π1pX Ă X, D, xq “
lim
ÐÝ
pX1,x1qPCovpXĂX,Dq
AutXpX1qop,
where the projective limit is taken over a projective system of pointed Galois coverings
pX1, x1q Ñ pX, xq in CovpX Ă X, Dq.
In the following, we write π1pX, D, xq and CovpX, Dq when we need not specify the
ﬁxed compactiﬁcation X of X.
For the geometric point x : SpecpΩq Ñ X with a
separably closed ﬁeld Ω, we denote also by x the geometric point SpecpΩq xÑ X ãÑ X of
X. The functors CovpXq Ñ CovpX, Dq; Y ÞÑ Y ˆX X, and CovpX, Dq Ñ CovpXq; Y ÞÑ
Y induce homomorphisms
π1pX, xq
/ / π1pX, D, xq
/ / π1pX, xq
(6)
which are surjective ([8], Exp. V, Prop. 6.9).
Lemma 2.5. Let f : pX1, x1q Ñ pX, xq be a morphism of pointed varieties over k,
and D P Div`
ZpXq. Assume the conditions paq and pbq below.
paq There exists a commutative diagram:
X1
f
/ X
X1
?
O
f
/ X
?
O
with a morphism f : X1 Ñ X from a compactiﬁcation X1 of X1 to X, where the
vertical morphisms are the inclusions.
pbq The inverse image f
˚D P Div`
Z1pX1q of D exists, where Z1 “ X1 ∖X1.
Then we have a canonical homomorphism
π1pX1 Ă X1, f ˚D, x1q
/ π1pX Ă X, D, xq.
7


## Page 8


Proof. We prove that the functor CovpXq Ñ CovpX1q; Y ÞÑ Y ˆX X1 induces a functor
CovpX Ă X, Dq Ñ CovpX1 Ă X1, f
˚Dq. The latter functor gives the required homo-
morphism on the fundamental groups ([8], Exp. V, Sect. 6). For h : Y Ñ X P CovpX Ă
X, Dq, it is enough to show that Y 1 :“ Y ˆX X1 Ñ X1 is of ramiﬁcation bounded by
f
˚D. Take any φ1 : C1 Ñ X1 P CupX1q, and we have to show that h1 : Y 1 ˆX1 C1 Ñ C1
gives ´etale coverings of ramiﬁcation bounded by φ1 ˚pf ˚Dq. Here, we divide the proof
into the two cases according to the image f ˝ φ1pC1q in X.
(The case where f ˝ φ1pC1q is a point) If the image of the composite f ˝ φ1 is a closed
point of X, then h1 : Y 1ˆX1 C1 Ñ C1 induces separable constant ﬁeld extensions of kpC1q,
and thus unramiﬁed on the boundary of C1. In particular, h1 is of ramiﬁcation bounded
by φ1 ˚pf
˚Dq.
(The case where f ˝ φ1pC1q is a curve) If f ˝ φ1 factors through φ : C Ñ X P CupXq
as in
C1
φ1
/
g

X1
f

C
φ
/ X,
then the extension g : C1 Ñ C of g ﬁts into the following commutative diagram:
C1
g 
φ1
/ X1
f
C
φ
/ X.
Since h : Y Ñ X is of ramiﬁcation bounded by D, the base change Y ˆXC Ñ C produces
´etale coverings of C which are of ramiﬁcation bounded by φ
˚D. It is left to show that
h1 : Y 1 ˆX1 C1 “ Y ˆX C1 Ñ C1 is of ramiﬁcation bounded by φ1 ˚pf
˚Dq “ g ˚pφ
˚Dq.
As a result, we may assume that f : X1 Ñ X is a dominant morphism of smooth curves
over k.
Let D “ ř
z mzrzs P Div`
ZpXq, and Y P CovpX Ă X, Dq. Take an irreducible com-
ponent Y 1 of Y ˆX X1. We prove that the induced covering Y 1 Ñ X1 is of ramiﬁcation
bounded by f ˚D. At z1 P Z1 “ X1 ∖X1 with fpz1q “ z, the multiplicity of f ˚D is ezmz,
where ez is the ramiﬁcation index of the extension kpX1qz1{kpXqz. The assertion carries
over to the local situation as in the following lemma.
□
Lemma 2.6. Let K be a local ﬁeld, and K1{K a ﬁnite extension with ramiﬁcation
index e. If a ﬁnite separable extension L{K is of ramiﬁcation bounded by λ for some
λ P Rě0, then LK1{K1 is of ramiﬁcation bounded by eλ.
Proof. (Reduction to L{K is Galois) We denote by rL the Galois closure of L{K.
From Lem. 2.3 (ii), rL{K is of ramiﬁcation bounded by λ. On the other hand, if rLK1{K1
8


## Page 9


is of ramiﬁcation bounded by eλ, so is LK1{K1 by Lem. 2.3 (ii) again. We may assume
that L{K is a Galois extension.
(Proof of the lemma) We put L1 “ LK1 and consider the two cases below:
Case 1 (K1{K is purely inseparable): Assume that K1{K is purely inseparable. In
this case, we show that L1{K1 is of ramiﬁcation bounded by λ. Since we have K1XL “ K,
the restriction gives an isomorphism GalpL1{K1q »
Ñ GalpL{Kq and hence rK1 : Ks “ rL1 :
Ls “ e. As the local ﬁeld K is of characteristic p ą 0 with perfect residue ﬁeld, we have
pK1qe “ K and pL1qe “ L. Take θ P OL1 such that OL1 “ OK1rθs ([16], Chap. III, Sect. 6,
Prop. 12) and this gives OL “ OKrθes. For any σ P GalpL1{K1q, we have
e ¨ vL1pσpθq ´ θq “ vL1pσpθeq ´ θeq
psince e is a power of pq
“ e ¨ vLpσpθeq ´ θeq.
Thus, the restriction GalpL1{Kq »
Ñ GalpL{Kq induces an isomorphism GalpL1{K1qµ »
GalpL{Kqµ for any µ P Rě´1 and thus ψL1{K1 “ ψL{K by (3). From the assumption, for
any λ1 ą λ,
GalpL1{K1qλ1 “ GalpL1{K1qψL1{K1pλ1q » GalpL{KqψL{Kpλ1q “ GalpL{Kqλ1 “ t 1 u .
This implies that the extension L1{K1 is of ramiﬁcation bounded by λ (Lem. 2.3 (iii)).
Case 2 (K1{K is separable): Assume that K1{K is a separable extension. We show
that L1{K1 is of ramiﬁcation bounded by eλ. Take a ﬁnite Galois extension M{K with
L1 Ă M. The Herbrand function ψK1{K of the separable extension K1{K is deﬁned to be
ψK1{K “ ϕM{K1 ˝ψM{K ([16], Chap. IV, Sect. 3, Rem. 2) and it satisﬁes ψK1{Kpµ{eq ď µ
for any µ P Rě´1. In fact,
ϕK1{Kpµq “ ϕM{K ˝ ψM{K1pµq
p:q
ě 1
eϕM{K1 ˝ ψM{K1pµq “ µ
e ,
where the inequality (:) follows from # GalpM{Kq0 “ e# GalpM{K1q0 and Lem. 2.1 (i).
For any λ1 ą eλ, we have
GalpM{K1qλ1 Ă GalpM{K1qψK1{Kpλ1{eq
pby ψK1{Kpλ1{eq ď λ1q
“ GalpM{K1qψM{Kpλ1{eq
pby Lem. 2.1 (ii)q
“ GalpM{KqψM{Kpλ1{eq X GalpM{K1q
pby Lem. 2.1 (i)q
Ă GalpM{Kqλ1{e
pby Lem. 2.1 (ii)q
Ă GalpM{Lq
pby λ1{e ą λ and L{K is of ramiﬁcation bounded by λq.
As a result, we have GalpM{K1qλ1 Ă GalpM{Lq X GalpM{K1q “ GalpM{L1q and hence
GalpL1{K1qλ1 “ GalpM{K1qλ1 GalpM{L1q{ GalpM{L1q “ t 1 u
by Lem. 2.1 (ii). This implies the assertion by Lem. 2.3 (iii).
(Proof of the lemma – continued) We take the separable closure Ks of K within K1.
From Case 2 above, the extension LKs{Ks is of ramiﬁcation bounded by eλ. Applying
Case 1 to the purely inseparable extension K1{Ks, the extension L1 “ LK1{K1 is of
ramiﬁcation bounded by eλ as required.
□
9


## Page 10


Concerning the condition (b) in Lem. 2.5, the lemma below assures the existence of
the inverse image of an eﬀective Cartier divisor in some situations.
Lemma 2.7 (cf. [3], Chap. IV, Sect. 21.4). Let f : X1 Ñ X be a morphism of
varieties over k, and D an eﬀective Cartier divisor on X. Then the inverse image
f ˚D is deﬁned in each of the following conditions:
paq f is ﬂat,
pbq X1, X are integral, and f is a dominant morphism,
pcq X1 is reduced, and for the generic point ξ1 P X1 of any irreducible component of
X1, we have fpξ1q R |D|, and
pdq f is a blowing up of X along a closed subscheme of X.
For a normal variety X over k, take a separably closed ﬁeld Ωas kpXq Ă Ω. We denote
by ξ both the geometric point SpecpΩq Ñ SpecpkpXqq which is given by kpXq Ă Ω, and
the geometric point SpecpΩq Ñ SpecpkpXqq Ñ X. The map SpecpkpXqq Ñ X induces a
canonical and surjective homomorphism
GkpXq “ GalpkpXq{kpXqq » π1pSpecpkpXqq, ξq
/ / π1pX, ξq,
(7)
where kpXq is the separable closure of kpXq in Ω([8] Exp. V, Prop. 8.2; [6], Prop. 3.3.6).
Its kernel is the subgroup GalpkpXq{kpXqZq, where kpXqZ is the maximal extension of
kpXq unramiﬁed outside Z, that is, the subﬁeld of kpXq generated by all ﬁnite separable
extensions E of kpXq contained in kpXq satisfying that the normalization XE Ñ X of
X in E is unramiﬁed. In particular, the surjective map (7) induces an isomorphism
GalpkpXqZ{kpXqq » π1pX, ξq.
In the same way, the fundamental group π1pX, D, ξq also has a description
GalpkpXqD{kpXqq » π1pX, D, ξq.
Here, kpXqD is the subﬁeld of kpXqZ generated by all ﬁnite separable extensions E of
kpXq contained in kpXqZ satisfying that the normalization XE Ñ X is of ramiﬁcation
bounded by D. When X is a smooth curve, it is easy to describe the kernel of the map
π1pX, ξq ։ π1pX, D, ξq given in (6) explicitly as follows:
Lemma 2.8. Let X be a smooth curve over k, and X the smooth compactiﬁcation of
X. We take a geometric point ξ of X and a separable closure kpXq as above. For D “
ř mzrzs P Div`
ZpXq, we denote by N the normal closed subgroup of π1pX, ξq generated
by the image of the ramiﬁcation subgroup Gmz`
z
of Gz :“ GalpkpXqz{kpXqzq by the
homomorphism Gz Ñ π1pX, ξq which is given by choosing an embedding kpXq ãÑ
kpXqz over kpXq and their conjugates in π1pX, ξq, for all z P Z. Then we have
π1pX, ξq{N
» / π1pX, D, ξq.
10


## Page 11


For each ﬁnite ´etale morphism f : X1 Ñ X of smooth curves over k, let f : X1 Ñ X
be the canonical extension of f to the smooth compactiﬁcations. We denote by DX1{X
the discriminant for the extension of the function ﬁelds kpX1q{kpXq ([16], Chap. III,
Sect. 3). In the following, we write the discriminant additively as a divisor
DX1{X “
ÿ
xPX
vxpDX1{Xqrxs
with the multiplicity vxpDX1{Xq P Zě0 at x. The ramiﬁcation locus of f coincides with
the support |DX1{X| “ t x P X | vxpDX1{Xq ą 0 u ([16], Chap. III, Sect. 5, Cor. 1) so that
one can consider the discriminant DX1{X as a Cartier divisor with support in Z “ X ∖X.
Proposition 2.9. Let f : X1 Ñ X be a ﬁnite ´etale morphism of smooth curves over
k, and X the smooth compactiﬁcation. If we have DX1{X ď D for some D P Div`
ZpXq,
then there exists D1 P Div`
ZpXq which depends only on D and the degree of f such
that the ramiﬁcation of f : X1 Ñ X is bounded by D1.
To show this proposition, we prepare the following notation and a lemma: For a ﬁnite
separable extension K1{K of local ﬁelds, we denote by
• DK1{K Ă OK : the discriminant of K1{K, and
• DK1{K Ă OK1 : the diﬀerent of K1{K (written multiplicatively as usual)
(cf. [16], Chap. III, Sect. 3).
Lemma 2.10. Let K be a local ﬁeld. Let K1 and K2 be two ﬁnite separable extensions
of K, and L “ K1K2 the compositum. As ideals in the valuation ring OL, we have
DL{K Ą DK1{KDK2{K.
Proof. Take θ P OK1 such that OK1 “ OKrθs ([16], Chap. III, Sect. 6, Prop. 12). Let
f P OKrTs be the minimal polynomial for θ over K. From the equality K1 “ Kpθq, we
have L “ K1K2 “ K2pθq. If we denote by g P OK2rTs the minimal polynomial for θ over
K2, one can write f “ gh in OK2rTs for some h P OK2rTs. Hence,
DK1{KOL “ f 1pθqOL
pby [16], Chap. III, Sect. 6, Cor. 2q
“ g1pθqhpθqOL
pby f “ ghq
Ă g1pθqOL
Ă DL{K2
pby [16], Chap. III, Sect. 6, Cor. 2 againq.
From the transitivity of the diﬀerents ([16], Chap. III, Sect. 4, Prop. 8), we obtain
DL{K “ DL{K2DK2{K Ą DK1{KDK2{K as ideals in OL.
□
11


## Page 12


Proof of Prop. 2.9. Let f : X1 Ñ X be the canonical extension of f to the smooth
compactiﬁcations. The multiplicity of DX1{X at z P Z is written as the sum
vzpDX1{Xq “
ÿ
z1PX1, fpz1q“z
vzpDkpX1qz1{kpXqzq,
where vzpDkpX1qz1{kpXqzq is the valuation of the discriminant DkpX1qz1{kpXqz at z ([15],
Chap. III, Sect. 2, Cor. 2.11). It is enough to show the following lemma.
□
Lemma 2.11. Let K1{K be a separable extension of local ﬁelds with rK1 : Ks “ n.
We denote by vKpDK1{Kq the valuation of the discriminant DK1{K. If vKpDK1{Kq ď m
for some m P Zě0, then there exists m1 P Zě0 which depends only on m and n such
that the extension K1{K is of ramiﬁcation bounded by m1.
Proof. (Reduction to Galois) Let K1, . . . , Kn be the conjugate ﬁelds of K1 “ K1. We
denote by L “ K1 ¨ ¨ ¨ Kn the Galois closure of K1{K. By using Lem. 2.10 repeatedly, we
have DL{K Ą DK1{K ¨ ¨ ¨ DKn{K as ideals in OL. From the equality DL{K “ NL{KpDL{Kq
([16], Chap. III, Prop. 6), we obtain
vKpDL{Kq ď nn!vKpDK1{Kq ď nn!m.
On the other hand, for any λ P Rě0, the ramiﬁcation of K1{K is bounded by λ if and
only if L{K is of ramiﬁcation bounded by λ (Lem. 2.3 (ii)). We may assume that K1{K
is a Galois extension.
(Proof of the lemma) It is enough to show GalpK1{Kqλ “ t 1 u for any λ ą m (Lem.
2.3 (iii)). Take θ P OK1 such that OK1 “ OKrθs ([16], Chap. III, Sect. 6, Prop. 12). The
Hilbert formula ([16], Chap. IV, Sect. 2, Prop. 4) gives
vK1pDK1{Kq “
ÿ
σPGalpK1{Kq∖t 1 u
vK1pσpθq ´ θq.
(8)
For any σ ‰ 1 in GalpK1{Kq, we have the following inequalities
m ě vKpDK1{Kq
pfrom the assumptionq
ě vK1pDK1{Kq
pby DK1{K “ NK1{KpDK1{Kqq
ě vK1pσpθq ´ θq
pby (8)q.
Hence, GalpK1{Kqλ “ GalpK1{KqψK1{Kpλq Ă GalpK1{Kqλ “ t 1 u for any λ ą m.
□
Remark 2.12. For a ﬁnite ´etale morphism f : X1 Ñ X of smooth curves over
k, by using the Hilbert’s formula (8) locally as in Prop. 2.9, we have the following
proposition: If the ramiﬁcation of f : X1 Ñ X is bounded by D for some D P
Div`
ZpXq, then there exists D1 P Div`
ZpXq which depends only on D and the degree
of f such that DX1{X ď D1.
12


## Page 13


l-adic sheaves
For a pointed connected Noetherian scheme pX, xq (in which the ﬁxed prime l is invertible
cf. Notation), we have an equivalence of categories ([6], Cor. 10.1.24):
(smooth Ql-sheaves on X)
» / (Ql-representations π1pX, xq Ñ AutpV q).
(9)
Here, a Ql-representation we mean a continuous homomorphism ρ : π1pX, xq Ñ AutpV q
with a ﬁnite dimensional Ql-vector space V (for the precise deﬁnition, see [2], 1.1.6, or
[6], Sect. 10.1). The equivalence above is given by F ÞÑ Fx “ V , where Fx is the stalk
of F at x.
Lemma 2.13. Let f : pX1, x1q Ñ pX, xq be a morphism of pointed connected
Noetherian schemes, and F a smooth Ql-sheaf on X. Identifying the isomorphism
Fx » pf ˚Fqx1 on stalks, the Ql-representation ρ1 : π1pX1, x1q Ñ Autppf ˚Fqx1q corre-
sponding to f ˚F makes the following diagram commutative:
π1pX, xq
ρ
/ AutpFxq
π1pX1, x1q
ρ1
/
ϕ
O
Autppf ˚Fqx1q,
where ϕ is the induced homomorphism of fundamental groups from f, and ρ is the
representation corresponding to F.
Proof. For some ﬁnite extension E of Ql in Ql with valuation ring R “ OE, the Ql-sheaf
F is represented by an E-sheaf. So we may assume that F “ pFnqně0 is an λ-adic
sheaf, where λ is a uniformizer of R. Recall that the representation corresponding to F
is given by taking the inverse limit of the representation π1pX, xq Ñ AutR{pλn`1qppFnqxq
(cf. [6], proof of Prop. 10.1.23), and f ˚F “ pf ˚Fnqně0 by the very deﬁnition. Without
loss of generality, we may assume that F is a locally constant sheaf on X with ﬁnite
stalks and ρ : π1pX, xq Ñ AutpFxq is given by the action of π1pX, xq on Fx. There exists
an ´etale covering Y Ñ X such that Y » F, where Y :“ HomXp´, Y q ([6], Prop. 5.8.1
(i)). On the other hand, we have f ˚F » Y ˆX X1 ([6], Prop. 5.2.7). The ﬁber functors
at x and x1 (5) make the following diagram commutative:
CovpXq
»
/
´ˆXX1

pπ1pX, xq-setsq
ϕ˚

CovpX1q
»
/ pπ1pX1, x1q-setsq,
where ϕ˚ is the functor induced by the homomorphism ϕ ([6], Prop. 3.3.1). As a result,
the action of π1pX1, x1q on pf ˚Fqx1 comes from that of π1pX, xq on Fx.
□
13


## Page 14


Deﬁnition 2.14 ([4], Sect. 3, see also [12], Sect. 10.1).
piq Let K be a local ﬁeld
with residue ﬁeld of characteristic p. For a Ql-representation ρ : GK Ñ AutpV q,
the Swan conductor of V is deﬁned by
SwpV q “
ÿ
λą0
λ dimpV Gλ`
K {V Gλ
Kq,
where V Gλ`
K
and V Gλ
K are the ﬁxed subspace of V by ρpGλ`
K q and ρpGλ
Kq re-
spectively.
piiq Let X be a smooth curve over k, and X the smooth compactiﬁcation of X. For
a smooth Ql-sheaf F on X, the Swan conductor of F is deﬁned to be the
eﬀective Cartier divisor
SwpFq “
ÿ
zPZ
SwzpFqrzs P Div`
ZpXq.
Here, for each z P Z, SwzpFq :“ SwpF|SpecpkpXqzqq P Zě0 (Lem. 2.15 (i) below)
is the Swan conductor of (the Ql-representation corresponding to) the restriction
F|SpecpkpXqzq.
piiiq Let X be a variety over k. For D P Div`
ZpXq and for a smooth Ql-sheaf F
on X, we say that the ramiﬁcation of F is bounded by D (and write as
SwpFq ď D formally) if, for every φ : C Ñ X P CupXq, we have Swpφ˚Fq ď
φ ˚D, where φ˚F is the pullback of F by φ.
Lemma 2.15 ([12], Thm. 4.85, [4], Sect. 3.1, (3.1)). Let K be a local ﬁeld with residue
ﬁeld of characteristic p.
piq For a Ql-representation V of GK, the Swan conductor SwpV q takes a value in
Zě0.
piiq For two Ql-representations V and V 1 of GK, we have SwpV ‘ V 1q “ SwpV q `
SwpV 1q.
Remark 2.16. For use later (in Lem. 3.7), we refer to the Artin conductor (cf. [16],
Chap. IV and [19], Sect. 4).
piq Let K be a local ﬁeld with residue ﬁeld of characteristic p, and ρ : GK Ñ AutpV q
a Ql-representation of GK. We assume that the restriction ρ|G0
K of ρ to G0
K has
ﬁnite image. The Artin conductor of V is deﬁned by
ArpV q “
ż 8
´1
dimpV {V Gx
Kqdx.
14


## Page 15


Putting
ǫpV q “
ż 0
´1
dimpV {V Gx
Kqdx “ dimpV {V G0
Kq,
we have
ArpV q “ ǫpV q `
ż 8
0
dimpV {V Gx
Kqdx
“ ǫpV q ` SwpV q.
piiq Let F be a smooth Ql-sheaf on a smooth curve X over k. We assume that
the corresponding Ql-representation ρ : π1pX, xq Ñ AutpFxq by (9) has ﬁnite
image, for simplicity. The global conductors of F are deﬁned by
ArpFq “
ÿ
zPZ
ArzpFqrzs
and
ǫpFq “
ÿ
zPZ
ǫzpFqrzs P Div`
ZpXq,
by using the local conductors ArzpFq :“ ArpF|SpecpkpXqzqq and ǫzpFq :“
ǫpF|SpecpkpXqzqq respectively.
From the relation of the local Artin and Swan
conductors noted above, we have
ArpFq “ ǫpFq ` SwpFq.
(10)
Lemma 2.17. Let pX, xq be a pointed variety over k, and F a smooth Ql-sheaf on
X of rank r. If the corresponding Ql-representation ρ : π1pX, xq Ñ AutpFxq factors
through π1pX, D, xq for some D P Div`
ZpXq, then we have SwpFq ď rD.
Proof. For each φ : C Ñ X P CupXq, we show Swpφ˚Fq ď φ ˚prDq “ rpφ ˚Dq (the last
equality follows from the additivity property of φ ˚: φ ˚pD ` D1q “ φ ˚D ` φ ˚D1, cf. [3],
Sect. 21.4.2). The assumption on ρ does not depend on the choice of the geometric point x
of X. By replacing the geometric point x if necessary, the morphism φ : C Ñ X P CupXq
induces a commutative diagram
π1pC, aq
ϕ
/

π1pX, xq

π1pC, φ
˚D, aq
/ π1pX, D, xq
(11)
by Lem. 2.5, where ϕ is the induced homomorphism of fundamental groups from φ,
and a a geometric point of C. By Lem. 2.13, the pullback φ˚F corresponds to the
representation given by the composition π1pC, aq
ϕÑ π1pX, xq
ρÑ AutpFxq. From the
assumption and the diagram (11), this representation factors through π1pC, φ ˚D, aq.
From this, we may assume that X is a smooth curve over k.
15


## Page 16


Since the Swan conductor is deﬁned to be SwpFq “ ř
zPZ SwzpFqrzs, if we write
D “ ř
zPZ mzrzs, it is enough to show SwzpFq ď rmz for each z P Z. By replacing
the geometric point and using Lem. 2.13 again, the multiplicity SwzpFq at z P Z is
given by the Swan conductor of the representation Gz Ñ π1pX, xq ρÑ AutpFxq of Gz :“
GalpkpXqz{kpXqzq, where the ﬁrst homomorphism is given by choosing an embedding
kpXq ãÑ kpXqz over kpXq as in Lem. 2.8. The assumption and Lem. 2.8 imply that
this representation factors through Gz{Gmz`
z
. The assertion is reduced to showing the
lemma below.
□
Lemma 2.18. Let K be a local ﬁeld with residue ﬁeld of characteristic p. If a Ql-
representation ρ : GK Ñ AutpV q annihilates Gλ`
K
for some λ P Rě0, then we have
SwpV q ď dimpV qλ.
Proof. Let L “ KKerpρq be the extension of K corresponding to Kerpρq.
From the
assumption, we have Gλ`
K
Ă Kerpρq “ GL. The ramiﬁcation of L{K is bounded by λ.
In particular, we have V Gλ1
K “ V for any λ1 ą λ. We obtain
SwpV q “
ÿ
0ăλ1ďλ
λ1 dimpV Gλ1`
K {V Gλ1
K q ď λ dimpV q.
□
3 Finiteness
Smallness
We recall a property of proﬁnite groups called smallness. This notion is also refereed as
“type (F)” in [17], Chap. III, Sect. 4.1.
Deﬁnition 3.1 ([9], Def. 2.1). A proﬁnite group G is said to be small if there exist
only ﬁnitely many open subgroups H with pG : Hq ď n for any n P Zě1.
For example, a topologically ﬁnitely generated proﬁnite group is small ([9], Prop. 2.4).
Using this notion, one can interpret the Hermite-Minkowski theorem as follows: For a
number ﬁeld F and a ﬁnite set S of primes of F, the Galois group GS of the maximal
Galois extension of F unramiﬁed outside S is small.
Proposition 3.2 ([9], Sect. 2). Let G and G1 be proﬁnite groups.
piq G is small if and only if there exist only ﬁnitely many open normal subgroups
N with pG : Nq ď n for any n P Zě1.
piiq If G is small and N is a closed normal subgroup of G, then the quotient group
G{N is small.
16


## Page 17


piiiq If G and G1 are small, then their free product G ˚ G1 is also small.
Main theorem
Recall that a smooth Weil sheaf F on a variety X over k consists of a smooth Ql-sheaf
F on X bk k :“ X ˆSpecpkq Specpkq and an action of the Weil group Wk “ Wpk{kq Ă Gk
on F ([2], Def. 1.1.10 (i)). For a smooth Ql-sheaf F on X, the pullback of F on X bk k
by the projection X bk k Ñ X and the action of Wk which is given by the restriction of
that of Gk produce a smooth Weil sheaf on X. This construction gives a fully faithful
functor
(smooth Ql-sheaves on X)  
/ (smooth Weil sheaves on X).
(12)
The Weil sheaves in the essential image of the above functor are said to be ´etale ([2],
1.3.2).
In fact, for a general Weil sheaf F on X and D P Div`
ZpXq the condition
“SwpFq ď D” is deﬁned in the same manner as Def. 2.14 using the Weil group WpX, xq Ă
π1pX, xq ([4], Sect. 3). For a smooth Ql-sheaf F, we have
SwpFq ď D in the sense of Def. 2.14 ks
+3 SwpF as an ´etale Weil sheaf q ď D.
(13)
From this, we often identify smooth Ql-sheaves with the corresponding ´etale Weil sheaves.
Adding to [2], for more details on Weil sheaves, see also [11], Chap. I, and [12], Sect. 10.
Following [4], for r P Zě1, we denote by
• RrpXq : the set of smooth Weil sheaves on X of rank r up to isomorphism and up
to semi-simpliﬁcation.
Theorem 3.3 ([4], Thm. 2.1). Let X be a smooth variety over k, and X a normal
compactiﬁcation of X such that Z “ X ∖X is the support of an eﬀective Cartier
divisor on X. Then for any r, n P Zě1 and D P Div`
ZpXq, the set of irreducible
sheaves F P RrpXq with
• SwpFq ď D, and
• detpFqbn “ 1
is ﬁnite, where detpFq :“ Źr F is the determinant of F.
From the Galois correspondence within the Galois category CovpX, Dq for a variety
X over k, Thm. 1.2 is equivalent to the smallness of the fundamental group π1pX, D, xq
which is stated in Thm. 3.4 below. For another geometric point x1 of X, we have an
isomorphism π1pX, D, x1q »
Ñ π1pX, D, xq and two such isomorphisms diﬀer by an inner
automorphism of π1pX, D, xq ([6], Prop. 3.2.13). Since we are interested in the smallness,
we omit the base point x of X from the fundamental groups and write π1pX, Dq as well
as π1pXq. Under this convention, it must be noted that a canonical homomorphism or a
commutative diagram concerning these groups makes sense viewing it up to conjugates.
17


## Page 18


Theorem 3.4. Let X be a variety over a ﬁnite ﬁeld k of characteristic p, X a
compactiﬁcation of X, and Z “ X∖X. Then π1pX, Dq is small for any D P Div`
ZpXq.
Proof. First, we reduce the assertion to the situation in which Thm. 3.3 holds, that
is, X is smooth over Specpkq and the compactiﬁcation X is normal with the boundary
Z “ X ∖X which is the support of an eﬀective Cartier divisor on X.
(Reduction to reduced) Let Xred and Xred be the reduced closed subschemes associ-
ated to X and X respectively. The natural morphisms f : Xred ãÑ X and f : Xred ãÑ X
which are closed immersions give the following commutative diagram
Xred  
f
/ X
Xred
?
jred
O
 
f
/ X,
?
j
O
where jred is the morphism associated to the inclusion map j ([3], Chap. I, 5.1.5). Since
we have |Xred| “ |X| and |Xred| “ |X| as the underlying topological spaces, the induced
morphism jred is a dominant open immersion ([3], Chap. I, Prop. 5.1.6). Here, Xred is
reduced, and for the generic point ξ of an irreducible component of Xred, we have fpξq R
Z “ X ∖X. In particular, fpξq R |D|. The inverse image f
˚D P Div`
Xred∖XredpXredq is
deﬁned (the case (c) in Lem. 2.7). By Lem. 2.5, there is a commutative diagram
π1pXredq

/ π1pXq

π1pXred, f
˚Dq
/ π1pX, Dq,
(14)
where the vertical homomorphisms are surjective as we noted in (6).
Since the top
horizontal homomorphism in (14) is known to be bijective ([8], Exp. IX, Prop. 1.7), the
bottom is surjective. If we assume that π1pXred, f
˚Dq is small, then so is π1pX, Dq by
Prop. 3.2 (ii). Therefore, we may assume that X and X are reduced.
(Reduction to integral) Since X is Noetherian, it has only a ﬁnite number of ir-
reducible components X1, . . . , Xn.
The irreducible components of X are given by
Xi :“ Xi X X for i “ 1, . . . , n ([13], Prop. 2.4.5(b)).
We endow these components
with the reduced closed subscheme structure. For each i, we obtain the following com-
mutative diagram
Xi  
fi
/ X
Xi
?
O
 
fi
/ X,
?
O
18


## Page 19


where fi is the natural morphism and fi is induced by fi. The inverse image Di :“
fi ˚D P Div`
Xi∖XipXiq exists. In fact, for the generic point ξi P Xi, we have fipξiq R |D|
(the case (c) in Lem. 2.7). The canonical homomorphism π1pXi, Diq Ñ π1pX, Dq exists
for each i by Lem. 2.5. The collection of morphisms t fi u1ďiďn induces Ůn
i“1 Xi Ñ X
which is an eﬀective descent morphism ([8], Exp. IX, see also [18], Thm. 5.2).
The
descent theory ([8], Exp. IX, Thm. 5.1, see also [18], Cor. 5.3) says that there exist
ﬁnitely many generators γ1, . . . , γm such that we have a surjective homomorphism
n˚
i“1
π1pXiq ˚ xγ1, . . . , γmy
/ / π1pXq,
where xγ1, . . . , γmy is the proﬁnite completion of the free group on the set t γ1, . . . , γm u.
The fundamental groups π1pXi, Diq and π1pX, Dq are quotients of π1pXiq and π1pXq
respectively as in (6). The canonical homomorphisms π1pXi, Diq Ñ π1pX, Dq and the
composition xγ1, . . . , γmy Ñ π1pXq ։ π1pX, Dq give a commutative diagram
n˚
i“1
π1pXiq ˚ xγ1, . . . , γmy

/ / π1pXq

n˚
i“1
π1pXi, Diq ˚ xγ1, . . . , γmy
/ π1pX, Dq.
(15)
From the diagram (15), the bottom horizontal map is surjective. As the free proﬁnite
group xγ1, . . . , γmy is topologically ﬁnitely generated, it is small ([9], Prop. 2.4). If we
assume π1pXi, Diq is small for all i, the free product ˚n
i“1 π1pXi, Diq ˚ xγ1, . . . , γmy is
small by Prop. 3.2 (iii) and the same holds for π1pX, Dq by Prop. 3.2 (ii). Thus, we may
assume that X and X are integral.
(Reduction to normal) Let f : X1 Ñ X be the normalization of X. The morphism f
is ﬁnite ([13], Cor. 4.1.30) and hence proper. The restriction f : X1 :“ f ´1pXq Ñ X of
f gives
X1
f
/ X
X1
?
O
f
/ X
?
O
which is commutative. The morphism f is also the normalization of X (from the very
deﬁnition of the normalization, [13], Cor. 4.1.19).
By the descent theory again ([8],
Exp. IX, Thm. 5.1, see also [18], Cor. 5.3), π1pXq is a quotient of the free product of
π1pX1q and a free proﬁnite group xγ1, . . . , γmy as
π1pX1q ˚ xγ1, . . . , γmy
/ / π1pXq.
19


## Page 20


The inverse image D1 :“ f
˚pDq on X1 exists by Lem. 2.7 (the case (b)). From Lem. 2.5
we have the following commutative diagram:
π1pX1q ˚ xγ1, . . . , γmy

/ / π1pXq

π1pX1, D1q ˚ xγ1, . . . , γmy
/ π1pX, Dq.
(16)
The bottom homomorphism in the diagram (16) becomes surjective. By Prop. 3.2 (ii)
and (iii) as above (the reduction to integral), the assertion is reduced to the situation
where X and X are normal.
(Reduction to smooth) Take the smooth locus U of X.
This U forms an open
subscheme of X ([13], Prop. 8.2.40).
Since X and hence U are normal, π1pXq and
π1pUq are quotient of the absolute Galois group GkpXq and GkpUq respectively (7). As
these quotient maps are canonical (up to inner automorphisms), we have the following
commutative diagram:
GkpUq

GkpXq

π1pUq
/ π1pXq.
By the commutativity, the bottom horizontal map is surjective. From Lem. 2.5, there is
a commutative diagram
π1pUq
/ /

π1pXq

π1pU Ă X, Dq
/ π1pX Ă X, Dq.
Since the top horizontal homomorphism π1pUq Ñ π1pXq in the diagram above is sur-
jective, so is the bottom. From Lem. 3.2 (ii), we may assume that X is smooth over
k.
(Reduction to Z “ |E| for some E P Div`
ZpXq) Let p : X1 Ñ X be the blowing up of
X along the reduced closed subscheme Z “ X ∖X ãÑ X. Note that X1 is integral ([3],
Chap. II, Prop. 8.1.4) (but may not be normal), p is proper and induces an isomorphism
X1 :“ p´1pXq »
Ñ X ([13], Prop. 8.1.12 (b) and (d)) which makes the following diagram
commutative:
X1
p
/ X
X1
?
O
»
/ X.
?
O
Hence, we have a dominant open immersion X1 ãÑ X1 whose complement X1 ∖X1 is the
support of an eﬀective Cartier divisor on X1 ([13], Prop. 8.1.12 (e)). The inverse image
20


## Page 21


D1 :“ p˚D exists (the case (d) in Lem. 2.7). Lem. 2.5 gives a commutative diagram
π1pX1q

»
/ π1pXq

π1pX1 Ă X1, D1q
/ π1pX Ă X, Dq.
(17)
From this diagram, the bottom horizontal map π1pX1 Ă X1, D1q ։ π1pX Ă X, Dq is
surjective. Using Prop. 3.2 (ii), we may assume that Z “ X ∖X is the support of an
eﬀective Cartier divisor E on X.
(Reduction to a normal compactiﬁcation) Let f : X1 Ñ X be the normalization.
This morphism f is ﬁnite and induces an isomorphism X1 :“ f
´1pXq
»
Ñ X as X is
normal. From Lem. 2.5, the diagram
X1
f
/ X
X1
?
O
»
/ X
?
O
induces a commutative diagram
π1pX1q

»
/ π1pXq

π1pX1 Ă X1, D1q
/ π1pX Ă X, Dq,
(18)
where D1 “ f˚pDq.
In particular, we obtain a surjective homomorphism π1pX1 Ă
X1, D1q ։ π1pX Ă X, Dq. Accordingly, there exists an open immersion X1 ãÑ X1 with
|X1 ∖X1| “ |f ˚E|. Therefore, without loss of generality, we may assume that X is
smooth and X is a normal compactiﬁcation of X whose boundary Z “ X ∖X is the
support of an eﬀective Cartier divisor on X.
Next, we show the smallness of the fundamental group π1pX, Dq under these assump-
tions.
(Proof of the smallness) For r P Zě1, we denote by Sr the set of open normal
subgroups N of π1pX, Dq with pπ1pX, Dq : Nq “ r. By Prop. 3.2 (i), it is enough to
show #Sr ă 8. For each N P Sr, consider the regular (and semi-simple) representation
ρN : π1pX, Dq{N ãÑ GLrpQlq of the ﬁnite group π1pX, Dq{N (with l ‰ p). By composing
the natural homomorphisms (cf. (6)), ρN induces
ρN : π1pXq
/ / π1pX, Dq
/ / π1pX, Dq{N   ρN / GLrpQlq.
21


## Page 22


We denote by FN P RrpXq the ´etale Weil sheaf on X associated with ρN (cf. (9)
and (12)).
By considering the irreducible decomposition, FN consists of irreducible
components F of rank ď r satisfying
• SwpFq ď SwpFNq ď rD
(by Lem. 2.15 (ii), Lem. 2.17 and (13)), and
• detpFqbr “ detpFNqbr “ 1
(for pπ1pX, Dq : Nq “ r, and hence detpρNqbr “ 1).
Thm. 3.3 implies that there exist only ﬁnitely many such irreducible sheaves. For we
have #Sr “ # t FN uNPSr, the assertion #Sr ă 8 follows.
□
Applications
Let F be an algebraically closed ﬁeld, X a variety over k, and D P Div`
ZpXq.
As
in Sect. 4 of [9], in the following, we derive some ﬁniteness results of representations
π1pX, Dq Ñ GLrpFq from our main theorem (Thm. 3.4) (so that we still omit the base
point). Here, we endow GLrpFq with the discrete topology. We deﬁne
π1pX, Dq0 :“ Kerpϕ : π1pX, Dq
/ π1pSpecpkqq “ Gkq,
(19)
where the homomorphism ϕ is induced from the structure morphism X Ñ Specpkq.
Since Gkp» pZq is abelian, π1pX, Dq0 does not depend on the choice of the (omitted)
geometric point.
Deﬁnition 3.5. A representation ρ : π1pX, Dq Ñ GLrpFq is said to be geometric if
it satisﬁes ρpπ1pX, Dqq “ ρpπ1pX, Dq0q.
When X is normal, this is equivalent to that the corresponding extension of the
function ﬁeld kpXq contains no constant ﬁeld extension.
Corollary 3.6. Let X be a normal variety over k, X a compactiﬁcation of X, and
Z “ X ∖X. For r P Zě1 and D P Div`
ZpXq, we have the following:
piq There exist only ﬁnitely many isomorphism classes of semi-simple geometric
representations π1pX, Dq Ñ GLrpFq with solvable image.
piiq If the characteristic of F is 0, then there exist only ﬁnitely many isomorphism
classes of semi-simple geometric representations π1pX, Dq Ñ GLrpFq.
To show this corollary, we prepare some notation and a lemma on a ﬁniteness of the
abelian fundamental group. For a topological group G, we denote by
• G_ “ t χ P HompG, Q{Zq | continuous u : the Pontrjagin dual group of G, and
• Gab “ G{rG, Gs : the abelianization of G, where rG, Gs is the topological closure of
the commutator subgroup of G.
22


## Page 23


The structure map X Ñ Specpkq as in (19) induces
π1pX, Dqab,0 :“ Kerpϕab : π1pX, Dqab
/ π1pSpecpkqqab “ Gkq.
Lemma 3.7. Let X be a normal variety over k, and X a compactiﬁcation of X. For
any D P Div`
ZpXq, we have #π1pX, Dqab,0 ă 8.
Proof. As in the proof of the main theorem (Thm. 3.4), we reduce the lemma to the case
where X is normal and the boundary Z “ X ∖X is the support of an eﬀective Cartier
divisor on X.
(Reduction to Z “ |E| for some E P Div`
ZpXq) Let p : X1 Ñ X be the blowing up
along the reduced closed subscheme Z “ X ∖X. As in (17), there exists a commutative
diagram
π1pX1qab

»
/ π1pXqab

π1pX1 Ă X1, p˚Dqab
/ π1pX Ă X, Dqab
with X1 “ ppq´1pXq, and the bottom horizontal map becomes surjective.
We may
assume that Z “ X ∖X is the support of an eﬀective Cartier divisor on X.
(Reduction to a normal compactiﬁcation) Let f : X1 Ñ X be the normalization.
As in (18), the isomorphism X1 :“ f´1pXq »
Ñ X induces a commutative diagram
π1pX1qab

»
/ π1pXqab

π1pX1 Ă X1, f
˚Dqab
/ π1pX Ă X, Dqab.
The bottom map is surjective so that we may assume that X is normal and there exists
E P Div`
ZpXq such that Z “ |E|.
(Proof of the lemma) Recall that there exists a canonical isomorphism pπ1pXqabq_ »
H1pX, Q{Zq, where H1pX, Q{Zq denotes the ´etale cohomology group ([1] Exp. 1, Sect. 2.2.1).
By composing this with the dual of π1pXqab ։ π1pX, Dqab induced from (6), we have
an injective homomorphism
ψ : pπ1pX, Dqabq_  
/ H1pX, Q{Zq.
(20)
Following [10], Def. 2.4, we deﬁne
ﬁlD H1pX, Q{Zq :“
␣
χ P H1pX, Q{Zq
ˇˇ Arpχq ď D
(
.
23


## Page 24


Here, the condition “Arpχq ď D” is deﬁned by Arpφ˚χq ď φ
˚D for every φ : C Ñ X P
CupXq using the Artin conductor Arpφ˚χq of the character φ˚χ : π1pCqab Ñ Q{Z (which
is corresponding to φ˚χ P H1pC, Q{Zq) ([16], Chap. IV, Sect. 3). We ﬁx Cˆ » pQlqˆ.
One can consider χ P pπ1pX, Dqabq_ as a Ql-representation (with ﬁnite image)
π1pXq
/ / π1pX, Dq
/ / π1pX, Dqab
χ / Q{Z  
/ GL1pQlq
of π1pXq, where π1pX, Dq ։ π1pX, Dqab is the quotient map. We denote by Fχ the
corresponding Ql-sheaf on X (by (9)). It satisﬁes SwpFχq ď D by Lem. 2.17. For every
φ : C Ñ X P CupXq, we have
Arpφ˚χq “ Arpφ˚Fχq deﬁned in Rem. 2.16.
(21)
Take E P Div`
ZpXq such that Z “ |E| and we denote by Ered the reduced divisor
associated to E. Putting D1 “ Ered ` D, we obtain
Arpφ˚χq “ Arpφ˚Fχq
pfrom (21)q
“ ǫpφ˚Fχq ` Swpφ˚Fχq
pfrom (10)q
ď φ
˚pEredq ` φ
˚pDq
“ φ ˚pD1q.
This implies that the image of ψ deﬁned in (20) is contained in ﬁlD1 H1pX, Q{Zq. By
taking the dual of ψ : pπ1pX, Dqabq_ ãÑ ﬁlD1 H1pX, Q{Zq, we have a surjective homomor-
phism ψ_ : pﬁlD1 H1pX, Q{Zqq_ ։ π1pX, Dqab using the Pontryagin duality theorem.
(In fact, the group pﬁlD1 H1pX, Q{Zqq_ is denoted by πab
1 pX, D1q in [10].) The structure
map X Ñ Specpkq induces a commutative diagram
pﬁlD1 H1pX, Q{Zqq_
ψ_
/ /

π1pX, Dqab
ϕab

H1pSpecpkq, Q{Zq_
»
/ π1pSpecpkqqab.
Here, the left vertical map is given by H1pSpecpkq, Q{Zq Ñ H1pX, Q{Zq.
As X is
normal, the kernel of the left vertical map (which is πab
1 pX, D1q0 in the sense of [10])
is ﬁnite by Cor. 1.2 in [10]. Our claim #π1pX, Dqab,0 ă 8 follows from this and the
commutative diagram above.
□
Proof of Cor. 3.6. As in the proof of Lem. 4.4 in [9], by induction on n, we also ob-
tain the ﬁniteness of the quotient π1pX, Dq0{pπ1pX, Dq0qpnq for any n P Zě1, where
pπ1pX, Dq0qpnq is the n-th commutator subgroup ([9], Def. 4.2). Starting from this, the
same proofs of Thm. 4.5 (ii) and Thm. 4.6 (ii) in [9] work and the assertions follow.
□
24


## Page 25


References
[1] P. Deligne, Cohomologie ´etale, Lecture Notes in Mathematics, Vol. 569, Springer-
Verlag, Berlin-New York, 1977, S´eminaire de G´eom´etrie Alg´ebrique du Bois-Marie
SGA 41
2, Avec la collaboration de J. F. Boutot, A. Grothendieck, L. Illusie et J. L.
Verdier. 23
[2]
, La conjecture de Weil. II, Inst. Hautes ´Etudes Sci. Publ. Math. (1980),
no. 52, 137–252. 13, 17
[3] J. Dieudonn´e and A. Grothendieck, ´El´ements de g´eom´etrie alg´ebrique, Inst. Hautes
´Etudes Sci. Publ. Math. 4, 8, 11, 17, 20, 24, 28, 32 (1961–1967). 10, 15, 18, 20
[4] H. Esnault and M. Kerz, A ﬁniteness theorem for Galois representations of function
ﬁelds over ﬁnite ﬁelds (after Deligne), Acta Math. Vietnam. 37 (2012), no. 4, 531–
562. 1, 2, 3, 14, 17
[5] G. Faltings, G. W¨ustholz, F. Grunewald, N. Schappacher, and U. Stuhler, Rational
points, third ed., Aspects of Mathematics, E6, Friedr. Vieweg & Sohn, Braun-
schweig, 1992, Papers from the seminar held at the Max-Planck-Institut f¨ur Math-
ematik, Bonn/Wuppertal, 1983/1984, With an appendix by W¨ustholz. 1
[6] L. Fu, Etale cohomology theory, Nankai Tracts in Mathematics, vol. 13, World
Scientiﬁc Publishing Co. Pte. Ltd., Hackensack, NJ, 2011. 3, 7, 10, 13, 17
[7] D. Goss, Basic structures of function ﬁeld arithmetic, Ergebnisse der Mathematik
und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)], vol. 35,
Springer-Verlag, Berlin, 1996. 1, 2
[8] A. Grothendieck, Revˆetements ´etales et groupe fondamental, Springer-Verlag,
Berlin, 1971, S´eminaire de G´eom´etrie Alg´ebrique du Bois Marie 1960–1961 (SGA
1), Dirig´e par Alexandre Grothendieck. Augment´e de deux expos´es de M. Raynaud,
Lecture Notes in Mathematics, Vol. 224. 6, 7, 8, 10, 18, 19
[9] S. Harada and T. Hiranouchi, Smallness of fundamental groups for arithmetic
schemes, J. Number Theory 129 (2009), no. 11, 2702–2712.
1, 3, 5, 7, 16, 19,
22, 24
[10] M. Kerz and S. Saito, Lefschetz theorem for abelian fundamental group with modulus,
Algebra Number Theory 8 (2014), no. 3, 689–701. 23, 24
[11] R. Kiehl and R. Weissauer, Weil conjectures, perverse sheaves and l’adic Fourier
transform, Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series
of Modern Surveys in Mathematics [Results in Mathematics and Related Areas.
3rd Series. A Series of Modern Surveys in Mathematics], vol. 42, Springer-Verlag,
Berlin, 2001. 17
25


## Page 26


[12] L. Kindler and K. R¨ulling, Introductory course on ℓ-adic sheaves and their ramiﬁ-
cation theory on curves, arXiv:1409.6899 [math.AG]. 14, 17
[13] Q. Liu, Algebraic geometry and arithmetic curves, Oxford Graduate Texts in Math-
ematics, vol. 6, Oxford University Press, Oxford, 2002, Translated from the French
by Reinie Ern´e, Oxford Science Publications. 18, 19, 20
[14] W. L¨utkebohmert, On compactiﬁcation of schemes, Manuscripta Math. 80 (1993),
no. 1, 95–111. 4
[15] J. Neukirch, Algebraic number theory, Grundlehren der Mathematischen Wis-
senschaften [Fundamental Principles of Mathematical Sciences], vol. 322, Springer-
Verlag, Berlin, 1999, Translated from the 1992 German original and with a note by
Norbert Schappacher, With a foreword by G. Harder. 1, 12
[16] J.-P. Serre, Corps locaux, Hermann, Paris, 1968, Deuxi`eme ´edition, Publications de
l’Universit´e de Nancago, No. VIII. 1, 4, 5, 9, 11, 12, 14, 24
[17]
, Cohomologie galoisienne, ﬁfth ed., Lecture Notes in Mathematics, vol. 5,
Springer-Verlag, Berlin, 1994. 16
[18] J. Stix, A general Seifert-Van Kampen theorem for algebraic fundamental groups,
Publ. Res. Inst. Math. Sci. 42 (2006), no. 3, 763–786. 19
[19] D. Ulmer, Conductors of ℓ-adic representations, Proc. Amer. Math. Soc. 144 (2016),
no. 6, 2291–2299. 14
Toshiro Hiranouchi
Department of Mathematics, Graduate School of Science, Hiroshima University 1-3-1
Kagamiyama, Higashi-Hiroshima, 739-8526 JAPAN
Email address: hira@hiroshima-u.ac.jp
26

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
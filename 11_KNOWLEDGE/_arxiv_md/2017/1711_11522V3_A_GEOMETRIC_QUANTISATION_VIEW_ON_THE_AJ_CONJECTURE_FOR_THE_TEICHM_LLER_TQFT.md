---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1711.11522v3
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1711.11522v3_A_Geometric_Quantisation_view_on_the_AJ-conjecture_for_the_Teichmüller_TQFT

> Source: 1711.11522v3_A_Geometric_Quantisation_view_on_the_AJ-conjecture_for_the_Teichmüller_TQFT.pdf

> Pages: 32

---


## Page 1


arXiv:1711.11522v3  [math.DG]  30 Apr 2024
A Geometric Quantisation view on
the AJ-conjecture for the Teichmüller TQFT
Jørgen Ellegaard Andersen and Alessandro Malusà
Abstract
We provide a Geometric Quantisation formulation of the AJ-conjecture
for the Teichmüller TQFT, and we prove it in detail in the case of the
knot complements of 41 and 52. The conjecture states that the level-N
Andersen-Kashaev invariant is annihilated by the non-homogeneous ˆA-
polynomial, evaluated at appropriate q-commutative operators. We ob-
tained the latter via Geometric Quantisation on the moduli space of ﬂat
SL(2, C)-connections on a genus-1 surface, by considering the holonomy
functions associated to a meridian and longitude. The construction de-
pends on a parameter σ in the Teichmüller space in a way measured by
the Hitchin-Witten connection, but we show that the resulting quantum
operators are covariantly constant. Their action on the Andersen-Kashaev
invariant is then deﬁned via a trivialisation of the Hitchin-Witten connec-
tion and the Weil-Gel’Fand-Zak transform.
Contents
1
Introduction
2
1.1
Geometric Quantisation
. . . . . . . . . . . . . . . . . . . . . . .
3
1.2
AJ-conjecture and partition functions
. . . . . . . . . . . . . . .
4
2
General background
8
2.1
AN and the level-N quantum dilogarithm
. . . . . . . . . . . .
8
2.2
Algebraic setting and A-polynomials
. . . . . . . . . . . . . . .
10
2.3
The Andersen-Kashaev theory
. . . . . . . . . . . . . . . . . . .
11
3
Setup for geometric quantisation
12
4
Operators from geometric quantisation on T2
C
15
4.1
The quantum operators on H(t)
σ
. . . . . . . . . . . . . . . . . .
15
4.2
Trivialisation of the Hitchin-Witten connection . . . . . . . . . .
17
4.3
The Weil-Gel’fand-Zak transform . . . . . . . . . . . . . . . . . .
19
5
The annihilator of J(b,N)
M,K
21
5.1
The ﬁgure-eight knot 41
. . . . . . . . . . . . . . . . . . . . . . .
22
5.2
The knot 52 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
References
28
1


## Page 2


1
Introduction
In this paper we consider the SL(2, C)–Chern-Simons theory and the interplay
between its formulations via geometric quantisation [Hit90, ADPW91, Wit89]
and the Teichmüller TQFT [AK14b].
Our starting point is the problem of
quantising functions on the moduli space of ﬂat connections on a closed ori-
ented surface of genus one, particularly the A-polynomial of a knot K em-
bedded in a 3-dimensional manifold M. Direct geometric quantisation, how-
ever, immediately gives rise to the usual issues. First, the pre-quantisation
of these functions is in most cases incompatible with the polarisations in
use.
Nonetheless, we ﬁnd that the holonomy functions associated with a
longitude and meridian behave nicely enough to give rise to a pair of q-
commuting quantum operators bℓand bm. Attempting to combine these into
a quantisation of polynomial functions would of course cause the usual or-
dering issues, so we turn to a more indirect approach. Namely, we use the
so-called Weil-Gel’fand-Zak transform to turn bℓand bm into operators acting
on J(b,N)
M,K , a minor transform of the Andersen-Kashaev partition function on
the knot complement M \ K. We are then in the perfect setting to consider the
AJ-conjecture [BDP14, Dim13, Dim15, FGL02, Gar04, Guk05] and give a ge-
ometric quantisation formulation of it, speciﬁcally for the Teichmüller TQFT.
Previously proposed for various other versions of the Chern-Simons partition
function, the conjecture predicts that the latter is annihilated by an operator
which, in the appropriate limit, reproduces the A-polynomial. This suggests
that the desired quantisation should then be obtained as a preferred generator
of the annihilator of J(b,N)
M,K in the algebra of (q-commutative) polynomials in
bℓand bm. We give a precise algebraic deﬁnition of such a generator and spec-
ulate, following the existing versions of the AJ-conjecture, that the resulting
expressions agree with those already found in the literature. We carry out
the full construction and computation for the ﬁrst two hyperbolic knots, 41
and 52, using reduction to ﬁnd the polynomials. We additionally include a
detailed account of the convergence of the relevant integrals and a proof that
the operators thus constructed annihilate J(b,N)
M,K as expected.
This work contributes in several ways to the mathematical discussion of
quantum SL(2, C)–Chern-Simons theory. It brings forth evidence of the little
understood relation between two different formulations, extending them both
by complementing each other. On the one hand, we obtain a precise algebraic
statement for the AJ-conjecture within the purely mathematical framework of
the Teichmüller TQFT. To this, the geometric quantisation side contributes a
new interpretation of the q-commuting pair, deriving it rigorously and di-
rectly from the holonomy functions they are associated with. On the other
hand, this approach offers candidates for the quantisation of A-polynomials as
functions on the moduli space of ﬂat connection on a torus, something which
geometric quantisation alone does not seem to be able to produce. What is
more, it strengthens the role of the Weil-Gel’fand-Zak transform, formerly in-
troduced as a bridge between these two approaches. While much remains to
be understood in those regards, the results of our work show further evidence
that this transform will likely play a central role in proving their equivalence.
Let us now provide further background for the sake of context, without
2


## Page 3


attempting to give a detailed historical account.
1.1
Geometric Quantisation
The geometric quantisation approach to Chern-Simons theory was proposed
by Hitchin [Hit90] and Axelord-Della Pietra-Witten [ADPW91] for SU(2) and
by Witten [Wit91] for SL(2, C). Given a smooth oriented 3-manifold X, possi-
bly with boundary, the classical solutions (i.e. ﬂat connections) form a moduli
space which, however, lacks the necessary structure to carry out geometric
quantisation. For a closed oriented smooth surface, on the other hand, the
resulting moduli space has a natural symplectic form and pre-quantum line
bundle, both tightly related to Chern-Simons theory [Fre95]. This space also
comes with a family of polarisations parametrised by the Teichmüller space T,
but there is no preferred way to choose one in particular. Therefore, the quan-
tisation procedures result in vector bundles over T, whose ﬁbres are identiﬁed
(up to rescaling) by the holonomies of appropriate projectively ﬂat connec-
tions.
The latter carry the name of Hitchin and Hitchin-Witten in the re-
spective cases of SU(2) and SL(2, C); both have been studied extensively, and
they play a pivotal role in Chern-Simons theory, geometric quantisation, and
related quantisation schemes [And05, And06, And10, And12, AG11, AG14,
AGL12, AM19, AMR24, AM16, AM23, AN16, Lau10, Mal18, Mar16, Woo92].
Returning to the geometry of the moduli spaces, the pull-back mapping
induced by restricting a connection on X to Σ := ∂X turns out to be La-
grangian [Fre95]. Said slightly differently, the locus of ﬂat connections on Σ
which extend to the bulk of X deﬁnes a Lagrangian subvariety. One may then
attempt to quantise this object in place of ﬂat connections on X themselves.
In the setting above, if X is the exterior of an embedded knot K in a
closed oriented 3-manifold M, then Σ is a connected surface of genus one—the
boundary of a tubular neighbourhood of K. The holonomy functions ℓand m
associated to a longitude and meridian deﬁne global coordinates on the mod-
uli space for SL(2, C), and (the Zariski closure of) the Lagrangian of interest is
cut by a single function A ∈Z[ℓ, m]—the A-polynomial of K [CC+94].
The goal is then to quantise this function A in the case of SL(2, C). As
previously mentioned, we do not do this directly, but we start by considering
the operators associated to the logarithmic holonomy functions U and V.
Theorem 1 (See Theorems 9, 11, 13). Let T denote the Teichmüller space of a closed
oriented surface of genus 1, and U, V the logarithmic holonomies along a meridian
and longitude, viewed as functions on the moduli space of ﬂat SL(2, C)-connections.
For every σ ∈T, the pre-quantum operators deﬁned by U and V preserve the real
polarisation Pσ associated to σ as deﬁned by Witten [Wit91]. The resulting quantum
operators bUσ and bVσ have central commutator, and moreover they are normal and
covariantly constant with respect to the Hitchin-Witten connection.
This allows us to deﬁne operators bmσ and bℓσ as the exponentials of bUσ and
bVσ. These form a covariantly constant T-family of q-commutative pairs, each
compatible with the respective polarisation. We proceed by using a trivialisa-
tion of the Hitchin-Witten connection, whose existence and explicit expression
was suggested by Witten [Wit91] and discussed in [Mal18] (see Section 4.2)—it
3


## Page 4


was also used in [AM23] to understand the SL(2, C) quantum representations
of the mapping class groups.
Theorem 2 (See Theorem 13). The operators bm and bℓ, deﬁned by conjugating
exp(bUσ) and exp(bVσ) by the trivialisation of the Hitchin-Witten connection, are
independent of σ and form a q-commutative pair for some appropriate q.
1.2
AJ-conjecture and partition functions
The AJ-conjecture, in its version for SU(2), brings together two knot invariants
of rather different origin—the A-polynomial discussed above and the coloured
Jones polynomial. Roughly speaking, the conjecture states that the latter is an-
nihilated by an operator bAq,K, expressed a q-commutative polynomial, which
in an appropriate sense is minimal and reproduces the A-polynomial when
q = 1. Early works on this include, in no particular order, those of Frohman-
Gelca-Lofaro [FGL02], Garoufalidis [Gar04], and [Guk05]. In [FGL02], the au-
thors construct a non-commutative analogue of the A-polynomial by replacing
the coordinate rings of character varieties with Kauffman bracket skein mod-
ules. They show their invariant is orthogonal to the coloured Jones polyno-
mial under the natural pairing, and speculate whether its containment in the
annihilator is proper. In [Gar04], Garoufalidis studies the coloured Jones poly-
nomial in terms of recursive relations, and formulates his version of the con-
jecture in terms of a preferred generator of the ideal of such relations, a view-
point further developed in [GL05, GL16, GLL18, Lê06]. The approach pro-
posed by Gukov [Guk05] and later expanded e.g. in [BDP14, DGG14, Dim13,
Dim15, DGLZ09], on the other hand, is in terms of the partition function of
(analytically continued) Chern-Simons theory. In that context, the equation
A(ℓ, m) = 0 represents the classical conﬁgurations (i.e. ﬂat connections) on
a knot complement M as sitting inside those on the boundary torus. Anal-
ogously, Gukov views the partition function Z of M as the wave function of
a state on the boundary, which one should expect to satisfy a relation of the
form bAZ = 0 quantising the classical equation A(ℓ, m) = 0. The relation with
the coloured Jones naturally follows from Witten’s interpretation of it as the
partition function for the SU(2)-theory [Wit89].
Although Witten’s work on the coloured Jones polynomial was originally
based on path-integral methods, his results were later made mathematically
rigorous by Reshetikhin-Turaev [RT90, RT91] in terms of category theory and
TQFT’s.
The equivalence of this partition-function approach to geometric
quantisation was later established by a chain of isomorphisms due to Andersen-
Ueno [AU07a, AU07b, AU12, AU15] and Laszlo [Las98].
For non-compact groups, such as SL(2, C) and SL(2, R), the situation is
more involved. Numerous constructions of partition functions have been pro-
posed with varying degrees of generality, using both path-integral techniques
and more mathematically rigorous methods. Without discussing speciﬁc de-
tails, some examples in no particular order include [AK14a, AK14b, AK14c,
BB04, BB07, BDP14, DFM11, Dim13, Dim15, DGLZ09, Guk05, Hik01, Hik07].
Most of these approaches are based on Faddeev’s quantum dilogarithm (§ 2.1)
and some version of gluing formula, and in the examples that have been ex-
plicitly carried out they seem to essentially agree. Despite the similarities,
however, the exact relation between all these different approaches, as well as
4


## Page 5


with geometric quantisation, is not yet fully understood, to the best of these
authors’ knowledge. Nonetheless, Gukov’s argument for the AJ-conjecture is
general enough that it should apply to any partition-function model of Chern-
Simons theory, regardless of the speciﬁcs of its construction.
Of particular inspiration for our work are the methods of Dimofte [Dim13]
and Beem-Dimofte-Pasquetti [BDP14], based on ideal triangulations of knot
complements. Besides producing their own version of the partition function,
they also propose a plan for quantising the A-polynomial directly from gluing
data. On the classical side, to the gluing of ideal tetrahedra corresponds sym-
plectic reduction on the space of ﬂat connections on the boundary, and the
equation of the Lagrangian associated to the bordism can be obtained from
those of the individual tetrahedra by an elimination and evaluation process.
On the other hand, recognising the Faddeev difference operator (2) as a quan-
tisation of the Lagrangian of a single tetrahedron, Dimofte proposes using
q-commutative elimination theory to mimic the same process as a quantisa-
tion of the A-polynomial.
The construction is carried out explicitly in the
cited works for some of the ﬁrst few knots, and the appropriate conjectures
are veriﬁed there for those cases.
Our next goal is then to use similar elimination techniques and the oper-
ators discussed above to ﬁnd relations on the partition function of the Teich-
müller TQFT. For context, the latter is expressed as a functor between suit-
ably deﬁned categoroids of decorated (2 + 1)-cobordisms and inﬁnite-rank
topological vector spaces. After its ﬁrst formulation in [AK14a], dependent
of a single quantum parameter b, it was further extended in [AK14b] to in-
clude a second parameter N, called its level—see [AM16] for more details.
What is most important to know for this work is that the theory assigns a
complex number, dependent of the pair (b, N) of quantum parameters, to ev-
ery hyperbolic knot K embedded in a closed oriented 3-manifold M. This
object—the partition function of the theory—is conjecturally equivalent to the
aforementioned J(b,N)
M,K , which is a complex-valued entire function on the space
AN := R × Z/NZ. Importantly, J(b,N)
M,K is expected to share several fundamen-
tal properties with the coloured Jones polynomial, further strengthening its
role as an SL(2, C) analogue of it. The precise statements are discussed in
detail in op. cit.; the relevant conjectures are veriﬁed therein for the knot com-
plements of 41 and 52, for 61 (with N = 1) by Andersen-Nissen [AN16]. Later
works of Ben Aribi-Piquet-Nakazawa [BP19] and Ben Aribi-Guéritaud-Piguet-
Nakazawa [BGP23] extended their results to all twist knots.
The key ingredient in reconnecting this viewpoint to that of geometric
quantisation is the so-called Weil-Gel’fand-Zak transform [AK14b]. This map
identiﬁes Schwartz-class functions on AN with smooth sections of the level-
N Chern-Simons line bundle for a genus-one closed oriented surface. As it
happens, the transform is also compatible with the natural L2 norms on the
two spaces, and therefore extends to a unitary isomorphism between their clo-
sures. In particular, we can use this to translate our bm and bℓfrom Theorem 2
into operators acting on functions on AN.
Theorem 3 (See Lemma 15, Theorem 16). Under conjugation by the Weil-Gel’fand-
5


## Page 6


Zak transform, bm and bℓcorrespond to the operators bmx and bℓx deﬁned by
  bmxf

(x, n) := e−2π bx
√
N e2πi n
N f(x, n) ,
 bℓxf

(x, n) := f

x −ib
√
N
, n + 1

.
Crucially, bmx and bℓx are the fundamental constituents of the Faddeev dif-
ference operator (2). They are also the same operators used by Dimofte [Dim13,
Dim15] as the building blocks for the construction of his version of the quan-
tum bA-polynomial.
In order to formulate our conjecture precisely, we shall take an algebraic
approach similar to that of [Gar04]. Namely, we consider the algebra A for-
mally generated over Z[q± 1
2 ] by two q-commuting elements E and Q. The
operators bℓx and bmx then deﬁne a representation of A, and we may consider
the annihilator of J(b,N)
M,K . If this left ideal is non-trivial it contains a preferred
generator (in a sense discussed below), which we shall call the bAC-polynomial.
Conjecture 1. Let K ⊆M be a hyperbolic knot inside a closed oriented 3-manifold.
Then the ideal annihilating J(b,N)
M,K is non-trivial. The resulting bAC-polynomial agrees
with the non-homogeneous bA-polynomial from the coloured Jones theory (see § 2.2) up
to a right factor in Q, and it reproduces the classical A-polynomial in the evaluation
at q = 1, E = ℓ, and Q = m2, again up to a factor in m.
As highlighted above, our statement is very close in spirit to the works of
Gukov [Guk05] and Dimofte [Dim13, Dim15]. In fact, in the ﬁnal part of this
article we will use the same q-commutative elimination process as Dimofte to
produce a guess for the bAC-polynomial. In contrast to his a priori approach,
however, we will work indirectly from the explicit expression of J(b,N)
M,K . Since
we are using the same operators and the partition functions match, the al-
gebraic manipulations will result in the same non-commutative polynomials,
which do agree with the non-homogeneous bA from the coloured Jones theory.
In order to conclude that the polynomials thus obtained annihilate J(b,N)
M,K as
expected, we will need to carefully carry out some further analytic checks.
After doing so, we can conclude the following.
Theorem 4. Conjecture 1 holds for the ﬁgure-eight knot 41, and 52.
To give a sense of the procedure, for the two knots in question and x ∈AN
the function J(b,N)
M,K takes the form
J(b,N)
M,K (x) =
Z
AN
Φ(x, y) dy
for some meromorphic function Φ deﬁned on AC
N × AC
N, AC
N := C ⊕Z/NZ.
To this corresponds an annihilator in the obvious representation of A⊗2
loc, and
its structure makes it straightforward to ﬁnd generators of this ideal. It is
intuitively clear here that the action of bmx and bℓx should commute with inte-
gration, while bℓy essentially amounts to a change of variable. It should then
follow that any element in A⊗2
loc which annihilates Φ and does not contain
6


## Page 7


bmy will also annihilate J(b,N)
M,K after evaluation at bℓy = 1. Once again, this is
consistent with the elimination/evaluation procedure of Dimofte, although
differently motivated.
Upon closer inspection on Φ and its integral, however, one sees that its
convergence may not hold when x or the integration contour are shifted in the
imaginary direction. To wok around this, we will introduce new integration
contours γh,a, labelled by appropriate parameters and stable under shifts. We
will establish convergence of the new integral whenever x lies in appropriate
regions Rh,a, and that the sum is holomorphic and agrees with J(b,N)
M,K for real x.
This gives a full characterisation of the holomorphic extension of J(b,N)
M,K to the
whole AC
N. Choosing the parameters h and a appropriately, the region Rh,a
will then be large enough to be stable under any set number of shifts in both
variables. Given a polynomial in bℓx, bmx, and bℓy annihilating the integrand,
this will allow us to take each individual monomial out of the integral (after
replacing bℓy with 1), thus obtain an operator which kills the partition function.
Structure of the paper
In section 2 we give an overview of the background material we refer to
throughout the the rest of the work. This includes generalities on geometric
quantisation and the Hitchin-Witten connection, the level-N quantum diloga-
rithm and the Weil-Gel’fand-Zak transform, the Teichmüller TQFT, and some
algebraic setup. In section 3 we deﬁne the precise structure to which we are
going to apply geometric quantisation, and argue that it provides a model for
(a double cover of) the moduli space relevant for genus one Chern-Simons
theory. In section 4 we actually run the geometric quantisation machinery
to obtain the desired operators. First, we use the standard deﬁnition of the
pre-quantum operators to quantise the logarithmic holonomy functions cor-
responding to the meridian and longitude on the torus. Next, we check that
the operators are compatible with the chosen polarisation, thus descending
to quantum operators. We then show that these are normal, thus admitting
well-deﬁned exponentials.
Finally, we use the explicit trivialisation of the
Hitchin-Witten connection to remove the dependence of the operators on the
Teichmüller parameter. After that, we determine the action of the operators
on functions on AN via the Weil-Gel’fand-Zak transform. In section 5, we
explicitly carry out the procedure described above to ﬁnd the bAC-polynomial
for the ﬁrst two hyperbolic knots.
Acknowledgements
We wish to thank Tudor Dimofte for proﬁtable insight on the techniques used
for computing the polynomial annihilating J(b,N)
M,K , and Simone Marzioni for
frequent discussion on aspects of his work on the Teichmüller TQFT. We also
owe an acknowledgement to the developers of Singular [DGPS16], which we
have used along the process of computing the polynomials.
Both authors were supported in part by the Danish National Science Foun-
dation Center of Excellence grant, Centre for Quantum Geometry of Moduli
spaces, DNRF95.
7


## Page 8


The ﬁrst-named author is supported by the grant from the Simons founda-
tion, Simons Collaboration on New Structures in Low-Dimensional Topology
grant no. 994320, the ERC-SyG project, Recursive and Exact New Quantum
Theory (ReNewQuantum) with funding from the European Research Coun-
cil (ERC) under the European Union‘s Horizon 2020 research and innovation
programme, grant agreement no. 810573.
The second-named author, in addition, thanks for their support the Uni-
versity of Toronto and the University of Saskatchewan, as well as the Paciﬁc
Institute for the Mathematical Sciences (PIMS) and the Centre for Quantum
Topology and its Applications (quanTA).
2
General background
2.1
AN and the level-N quantum dilogarithm
Deﬁnition 1. For every positive integer N, let AN be the locally compact Abelian
group R ⊕Z/NZ endowed with the nomalised Haar measure d(x, n) deﬁned by
Z
AN
f(x, n) d(x, n) :=
1
√
N
N
X
n=1
Z
R
f(x, n) dx .
We denote by S(AN, C) the space of Schwartz class functions on AN, i.e. functions
f(x, n) on AN which restrict to Schwartz class functions on R for every n. We shall
denote C ⊕Z/NZ by AC
N.
Of course S(AN, C) sits inside the space L2(AN, C) of square-summable
functions, as a dense subspace. We will often use the notation x = (x, n);
moreover, if λ ∈C we write x + λ as a short-hand for (x + λ, n).
As in [AK14b], we use the following notations for Fourier Kernels and
Gaussians on AN:

(x, n), (y, m)

= e2πixye−2πinm/N ,

(x, n)

= eπix2e−πin(n+N)/N .
(1)
Fix now b, a complex unitary parameter with Re(b) > 0 and Im(b) ⩾0,
and introduce constants
cb := i(b + b−1)
2
= i Re(b) ,
q
1
2 := −eπi b2+1
N
=
D ib
√
N
, −1
E−1
.
We summarise here the fundamental properties of the level N quantum
dilogarithm which are relevant for this work. For the precise deﬁnition and
further details see e.g. [AK14b, AM16]. For N a positive odd integer, the quan-
tum dilogarithm Db at level N and quantum parameter b is a meromorphic
function on AC
N which satisﬁes the Faddeev difference equations
Db

x ± ib
√
N
, n ± 1

=

1 −e± b2+1
N e2π
b
√
N xe2πi n
N
∓1
Db(x, n) ,
Db

x ± ib
√
N
, n ∓1

=

1 −e± b2+1
N e2π
b
√
N xe−2πi n
N
∓1
Db(x, n)
(2)
8


## Page 9


and the the inversion relation
Db(x)Db(−x) = ζ−1
N,inv ⟨x⟩,
ζN,inv = eπi(N+2c2
bN−1)/6 .
Lemma 5. For n ∈Z/NZ ﬁxed, the quantum dilogarithm has the following asymp-
totic behaviour for x →∞:
Db(x, n) ≈



1
on
arg(x)
 > π
2 + arg(b),
ζ−1
N,inv ⟨x⟩
on
arg(x)
 < π
2 −arg(b).
Furthermore, the dilogarithm satisﬁes the unitarity relation
Db(x, n)Db(x, n) = 1 .
It is convenient to change the notation according to [AM16], calling
ϕb(x, n) := Db(x, −n) .
The zeroes and poles of ϕb occur at the points pα,β and −pα,β respectively,
for α, β ∈Z⩾0, where
pα,β :=

−cb + iαb + iβb
√
N
, α −β

.
We shall often call
T :=








x ∈C: Re

b

x +
cb
√
N

⩽0 and Re

b

x +
cb
√
N

⩾0

if b ̸= 1,

x ∈C: Im(x) ⩽1 and
Re(x)
 ⩽1

if b = 1.
(3)
In particular, the zeroes and poles of ϕb(x, n) for n ﬁxed occur only for x ∈T
and x ∈−T respectively. Lemma 5 holds unchanged for ϕb in place of Db.
Deﬁnition 2. If k ∈Z>0 and µ : (AC
N)k →AC
N is a Z-linear function, denote by
bmµ the operator acting on complex-valued functions on (AC
N)k as
bmµf :=
D
µ,
 ib
√
N
, −1
E
f .
Moreover, call bℓx the operator acting on complex-valued functions on AC
N as
 bℓxf

(x, n) := f

x −ib
√
N
, n + 1

.
Remark 6. The action of bmx and bℓx is clearly well deﬁned on meromorphic func-
tions, and in fact on (dense subspaces of) L2(AN, C), with the caveat that ib/
√
N
cannot be real, owing to the condition that Re(b) > 0. On the one hand, this implies
that the factor ⟨x, (ib/
√
N, −1)⟩is unbounded on AN as it grows exponentially for
x →−∞. Nonetheless, the domain of bmx as an operator on L2(AN, C) contains all
compactly supported functions, and is therefore dense. On the other hand, the shift
along (−ib/
√
N, 1) does not preserve AN ⊆AC
N, so that, strictly speaking, bℓx is
9


## Page 10


not well deﬁned on L2(AN, C). However, if f ∈L2(AN, C) is entire, i.e. analytic
with inﬁnite radius of convergence, then it has a unique holomorphic extension, and
there is a natural way to make sense of bℓxf. This occurs, for instance, whenever f
is the Fourier transform of a compactly supported function, in which case bℓxf is also
square-integrable, showing that bℓx is also a densely deﬁned operator on L2(AN, C).
In fact, a little Fourier analysis also shows that, for any λ ∈C, (the closure of) the
shift operator along (λ, 0) is the exponential of λ d
dx, a fact we shall use later.
The following lemma is an immediate consequence of the deﬁnitions and
Faddeev’s difference equation.
Lemma 7. The operator bℓx acts on the Gaussian and the quantum dilogarithm as
bℓx ⟨x⟩= q−1
2 bm−1
x
⟨x⟩,
bℓxϕb(x) =

1 + q−1
2 bm−1
x

ϕb(x) ,
bℓ−1
x ϕb(x) =

1 + q
1
2 bm−1
x
−1
ϕb(x) .
Moreover, bℓx and bmx undergo the commutation relation
bℓx bmx = q bmxbℓx .
2.2
Algebraic setting and A-polynomials
For the algebraic setup of our conjecture, we shall borrow notations from
Garoufalidis [Gar04] as follows.
First, we consider the q-commutative algebra
A := Z[q± 1
2 ]⟨E, Q⟩
. EQ −qQE

.
One can also make sense of inverting polynomials in Q and obtain
Aloc :=



l
X
k=0
ak(q, Q)Ek : l ∈Z⩾0, ak ∈Q(q, Q)



(4)
with the product determined by
 a(q, Q)Ek
·
 b(q, Q)Eh
:= a(q, Q)b(q, qkQ)Ek+h .
Given a representation of Aloc and a vector e in it, one may deﬁne the sets
Iloc(e) :=

p(Q, E) ∈Aloc : p(Q, E)e = 0
	
and
I(e) := Iloc(e) ∩A
of elements annihilating e, each of which is a left ideal in its respective algebra.
Since every ideal in Aloc is principal, there exists a unique generator of Iloc(e)
of minimal degree in E and co-prime coefﬁcients in Z[q, Q]. As such, this
element actually lies in A, thus giving a preferred “generator” of I(e).
One way to phrase the AJ-conjecture for the coloured Jones polynomial is
to study recursive relations on it in terms of representations of A and Aloc.
10


## Page 11


This leads to a deﬁnition of the bA-polynomial as the preferred generator of
I(K) := I(JK) as discussed above. One version of this construction leads to the
so-called non-homogeneous polynomial bAq,K(Q, E). We shall later refer to the
formulæ found in [GS10] for 41 and 52, which read
bAnh
q,41 = q2 q2Q −1
 qQ2 −1

Q2E2
−
 qQ −1
 qQ + 1

q4Q4 −q3Q3 −q(q2 + 1)Q2 −qQ + 1

E
+ q2 Q −1
 q3Q2 −1)Q2 ,
(5)
bAnh
q,52 =
 q3Q −1
 qQ2 −1
 q2Q2 −1

E3
+ q
 q2Q −1
 qQ2 −1
 q4Q2 −1

·

q9Q5 −q7Q4 −q4(q3 −q2 −q + 1)Q3 + q2(q3 + 1)Q2 + 2q2Q −1

E2
−q5Q2 qQ −1
 q2Q2 −1
 q5Q2 −1

·

q6Q5 −2q5Q4 −q2(q3 + 1)Q3 + q(q3 −q2 −q + 1)Q2 + qQ −1

E
+ q9Q7 Q −1
 q4Q2 −1
 q5Q2 −1

.
The A-polynomials of these knots, known to be irreducible [HS04], read
A41(m, ℓ) = m4ℓ2 −

m8 −m6 −2m4 −m2 + 1

ℓ+ m4 ,
(6)
A52(m, ℓ) = ℓ3 +

m10 −m8 + 2m4 + 2m2 −1

ℓ2
−m4
m10 −2m8 −2m6 + m2 −1

ℓ+ m14 .
2.3
The Andersen-Kashaev theory
The Andersen-Kashaev theory deﬁnes an inﬁnite-rank TQFT Z from quan-
tum Teichmüller theory.
In particular, it deﬁnes an invariant Z(X) for ev-
ery object X consisting of a closed oriented 3-manifold M, a hyperbolic knot
K, and a suitably decorated triangulation of its complement. However, it is
conjectured [AK14a, AM16] that a two-parameter family of smooth functions
J(b,N)
M,K (x) on AN exists such that
Z(N)
b
(X) = eic2
bφ
Z
AN
J(b,N)
M,K (x)eiλcbx dx ,
where λ and φ carry the information relative to the decorated triangulation,
while J(b,N)
M,K (x) depends on the pair (M, K) alone. In addition, this function
is also conjectured to enjoy certain asymptotic conditions analogous to those
expected from the coloured Jones polynomial, something that has been estab-
lished in several particular cases [AN16, BP19, BGP23]. For the knots 41 and
11


## Page 12


52 in S3, the expression for J(b,N)
M,K is found to be
J(b,N)
S3, 41 (x) = e4πi
cbx
√
N χ41(x) ,
χ41(x) =
Z
AN
ϕb(x −y)

y
2
ϕb(y)

x −y
2 dy ,
J(b,N)
S3, 52 (x) = e2πi
cbx
√
N χ52(x) ,
χ52(x) =
Z
AN

y

⟨x⟩−1
ϕb(y + x)ϕb(y)ϕb(y −x) dy .
3
Setup for geometric quantisation
In this section we shall introduce the space on which we will run geometric
quantisation, as well as all the relevant notations and conventions. A more
general version of this discussion may be found in [AMR22].
Throughout this paper, we will write T2 to denote the real torus S1 × S1,
and T2
C for the 2-dimensional complex torus C∗× C∗containing it. We shall
use coordinates u, v ∈R on T2 and U, V ∈C on T2
C, with
(u, v) 7→
 e2πiu, e2πiv
∈T2 ,
(U, V) 7→
 e2πiU, e2πiV
∈T2
C .
We refer to these as the logarithmic coordinates, as opposed to the exponential
coordinates
m = e2πiU ,
ℓ= e2πiV
on T2
C. Using u = Re(U), v = Re(V), Im(U), and Im(V) as real coordinates, it
makes sense to regard
∂
∂u and
∂
∂v as vector ﬁeld on T2
C as well as on T2.
On these spaces we consider symplectic 2-forms
ω = −2π du ∧dv ;
ωC = −2π dU ∧dV .
We now ﬁx a positive integer N and a real number S (without further restric-
tions), calling t = N + iS the level of the theory, and deﬁne the level-t real
symplectic structure on T2
C as
ωt := 1
2 Re
 tωC

,
which restricts to the form Nω on T2. A pre-quantum line bundle L (t) on
(T2
C, ωt) is deﬁned by the quasi-periodicity conditions
ψ(U + 1, V) = e−πi Re(tV)ψ(U, V) ,
and
ψ(U, V + 1) = eπi Re(tU)ψ(U, V) ,
and connection ∇(t) = d−iθ(t) with
θ(t)
(U,V) = π Re

t
 V dU −U dV

.
This bundle restricts to one on (T2, Nω), which we call L N. Explicitly, the
quasi-periodicity conditions and the connection form for this bundle are
ψ(u + 1, v) = e−Nπivψ(u, v)
and
ψ(u, v + 1) = eNπiuψ(u, v) ,
θN
(u,v) = Nπ
 v du −u dv

.
We refer to these as the Chern-Simons line bundles over T2
C and T2 at the level
t and N respectively, and we shall often omit the superscript in the connection.
12


## Page 13


The family of complex structures on T2.
Denote by T the upper half-plane
T =

σ ∈C : Im(σ) > 0
	
.
To every point of T one can associate an almost complex structure on T2
represented in the logarithmic coordinates by the constant matrix
J :=
i
σ −σ
 
−(σ + σ)
2σσ
−2
σ + σ
!
.
(7)
It is easily checked that this deﬁnes a complex structure on T2, with holomor-
phic and anti-holomorphic vector ﬁelds given by
∂
∂w := 1 + iJ
2
∂
∂u =
1
σ −σ

σ ∂
∂u + ∂
∂v

,
∂
∂w := 1 −iJ
2
∂
∂u = −
1
σ −σ

σ ∂
∂u + ∂
∂v

,
(8)
to which correspond complex coordinates
w = u −σv ,
w = u −σv .
For later convenience, note that ω is determined in these coordinates by
ω
 ∂
∂w, ∂
∂w

= 1
4ω
 ∂
∂u −iJ ∂
∂u, ∂
∂u + iJ ∂
∂u

= −2π
σ −σ ,
which implies

∇w, ∇w

= 2Nπi
σ −σ .
Together with ω, J deﬁnes a Kähler structure on T2 with metric
g =
2πi
σ −σ
 
2
−(σ + σ)
−(σ + σ)
2σσ
!
,
whose inverse is
˜g =
i
2π(σ −σ)
 
2σσ
σ + σ
σ + σ
2
!
.
The Laplace operator ∆, which acts on sections of L N by differentiating twice
and then contracting both indices with ˜g, can be written as
∆= −iσ −σ
2π

∇w∇w + ∇w∇w

= −iσ −σ
π
∇w∇w −N ,
(9)
by noticing that the metric is determined by
g
 ∂
∂w, ∂
∂w

= −iω
 ∂
∂w, ∂
∂w

=
2πi
σ −σ .
13


## Page 14


Since the coefﬁcients of g are constant functions on T2, its Levi-Civita connec-
tion is trivial for all values of σ, and therefore independent of it. Consequently,
the variation of ∆with respect to σ is determined by that of ˜g, which is
∂˜g
∂σ =
i
π(σ −σ)2
 
σ2
σ
σ
1
!
,
∂˜g
∂σ = −
i
π(σ −σ)2
 
σ2
σ
σ
1
!
.
These two tensors are also parallel, and up to constant coefﬁcients one can
recognise them as
∂
∂w ⊗
∂
∂w and
∂
∂w ⊗
∂
∂w. In particular, this makes J holo-
morphic and rigid in the sense of [AG14]. The variation of ∆is then
∂
∂σ∆= −i
π∇w∇w ,
∂
∂σ∆= i
π∇w∇w .
Polarisations on T2
C and geometric quantisation.
Using the natural complex
structure I on T2
C, the right-most expressions in (8) may also be read as real
vector ﬁelds on the complex torus. To avoid confusion, we shall denote these
as X and X, respectively, although both objects are real and not the conjugate of
one another. They span integrable distributions in T T2
C which are Lagrangian
for ωC, thus for ωt for every t, i.e. polarisations. We set
P = Pσ := Span

X, IX

.
Because each leaf of P intersects T2 ⊆T2
C at exactly one point, and trans-
versely, this subspace may be identiﬁed with the reduction T2
C/P. One can
identify the space of smooth polarised sections of L (t) over T2
C with that of
all smooth sections of L N over T2, the latter supporting an L2-product via
the volume form ω. In other words, one can deﬁne the level-t Hilbert space
H(t)
σ
arising from geometric quantisation on (T2
C, ωt) with pre-quantum line
bundle L (t) and polarisation Pσ as L2(T2, L N). Although σ does not mani-
festly enter the deﬁnition of this last space, the dependence on this parameter
should be measured via the Hitchin-Witten connection [Wit91, AG14] on the
trivial bundle
Ht := T × L2(T2, L N) →T .
Due to the ﬂatness of g, the deﬁnition of the connection simpliﬁes to
˜∇σ = ∂
∂σ + i
π∇w∇w ,
˜∇σ = ∂
∂σ −i
π∇w∇w .
Although the arguments of [AG14] do not apply, T2 having non-trivial holo-
morphic vector ﬁelds and ﬁst cohomology, it is not difﬁcult to show that ˜∇is
ﬂat in this case. In fact, Witten proposes the following statement.
Proposition 8. The Hitchin-Witten connection ˜∇for T2
C has a trivialisation
˜∇= exp(−r∆)∇Tr exp(r∆)
for r a complex parameter such that
e4Nr = −t
t .
The result can be proven via a straightforward adaptation of the argument
presented in [AM19].
14


## Page 15


Motivation: the moduli spaces of ﬂat connections on a genus-one surface.
The deﬁnitions introduced in this section are motivated by the SL(2, C)–Chern-
Simons theory on a smooth oriented surface Σ of genus one. If G denotes
either SU(2) or SL(2, C), the moduli space of ﬂat G-connections on Σ can be
realised as a product of two copies of a maximal torus in G, modulo the action
of the Weyl group W ≃Z/2Z. The moduli spaces, which we denote as M and
MC, can then be described as T2/W and T2
C/W respectively, where W acts on
each space by simultaneously inverting both entries. One can use the coordi-
nates above on the moduli spaces, on which are deﬁned the respective Atiyah-
Bott forms ωAB and ωAB
C , which pull back to 2ω and 2ωC. For every positive
integer k and real number s, Chern-Simons theory deﬁnes pre-quantum line
bundles L k and L (k+is) for kωAB and ωAB
k+is = Re((k + is)ωAB
C ). It follows
from the deﬁnitions that these lift to L 2k and L (2k+2is) on T2 and T2
C.
If (x, y) are 1-periodic coordinates on the surface, every σ ∈T deﬁnes a
Riemann surface structure on Σ with holomorphic coordinate z = x + σ−1y
(for the reversed orientation). This correspondence gives a biholomorphism
between T and the Teichmüller space of Σ.
The Hodge ∗-operator, which
deﬁnes the Kähler structure on M for the given Riemann surface structure, is
represented in these coordinates by the matrix J of (7). Vectors on the moduli
spaces are identiﬁed with Lie-algebra valued forms on Σ: if T is a generator
of a Cartan sub-algebra of su(2), to
∂
∂u and
∂
∂v correspond T dx and T dy.
In order to run geometric quantisation, Witten deﬁnes a polarisation on
MC spanned by the forms of type (1, 0); since T dz represents
∂
∂w up to rescal-
ing, this lifts to P on T2
C. Therefore, the quantum Hilbert space thus obtained
for the SL(2, C)–Chern-Simons theory at the level k + is is contained in H(t)
σ
for t = 2(k + is), as the sub-space of W-invariant sections. As σ varies, these
spaces form a sub-bundle of H(t), identiﬁed with T × L2(M, L k), which is pre-
served by ˜∇. The restriction is the connection introduced by Witten in [Wit89].
4
Operators from geometric quantisation on T2
C
4.1
The quantum operators on H(t)
σ
We now ﬁx t = N + iS and study the level-t pre-quantum operators associ-
ated to the logarithmic coordinates U and V on T2
C. Strictly speaking, these
functions are only well deﬁned up to picking a branch, so we should start by
specifying one. For instance, we may choose the coordinates on T2 so that
0 ⩽u, v < 1 and impose that U and V extend them continuously away from
the Pσ-leaves through { u = 0 } and { v = 0 }, respectively. It will be clear later
that the resulting operators are essentially independent of the choice of a spe-
ciﬁc branch (see Remark 12). We shall also talk freely of the differentials and
Hamiltonian vector ﬁelds of U and V regardless of their discontinuity, since
these objects extend unambiguously to their singular locus.
Theorem 9. For every σ ∈T, the pre-quantum operators of U and V are compatible
with the polarisation Pσ and therefore descend to the quantum Hilbert space. Their
action on smooth sections of L N over T2 is given by
bUσ := u −iσ
πt∇w ,
bVσ := v −i
πt∇w .
15


## Page 16


Proof. Recall that the pre-quantum operator of a function f on T2
C is deﬁned
on sections of L (t) as
bf := f −i∇Hf ,
where Hf, the Hamiltonian vector ﬁeld of f relative to ωt, is determined by
Y[f] = ωt(Y, Hf)
for every Y ∈T T2
C.
(10)
It is well known that bf preserves the space of polarised sections if and only if
the Lie derivative by Hf preserves the space of vector ﬁelds tangent to P. This
is clearly the case for U and V, given that both the symplectic form and the
generators of P have constant coefﬁcients.
For the last part of our assertion it is enough to show that
σ
πt
∂
∂w and
1
πt
∂
∂w
differ from HU and HV by elements of P. By direct calculation we see
ωt

X, ∂
∂w

=
πt
σ −σ = πt
σ X[U] = πtX[V] ,
ωt

IX, ∂
∂w

=
iπt
σ −σ = πt
σ (IX)[U] = πt(IX)[V] .
Since X and IX span P, it follows from (10) that HU −σ
πt
∂
∂w and HV −
1
πt
∂
∂w
are ωt-orthogonal to P, and our conclusion follows.
We now wish to deﬁne quantum operators for the exponential coordinates
m and ℓ, to which end we rely on the spectral theorem for normal operators,
see e.g. [Con94]. In summary, a densely deﬁned operator E on a separable
Hilbert space is called normal if it is closed, shares the same domain as its
adjoint E†, and the two commute. The spectral theorem states that any such
operator is unitarily equivalent to the multiplication by a function φ on the L2
space of some measure space. The exponential exp(E) is then deﬁned as the
operator corresponding to eφ, also closed and densely deﬁned.
Remark 10. In the following we shall use two consequences of the spectral theorem
for a normal operator E on a separable Hilbert space. First, if ψ is a vector on which
the exponential series of E converges, then the sum equals exp(E)ψ. Second, there
exists a nested family of subspaces HC, C ∈R>0 whose union is dense and such
that, for each C, both E and E† preserve HC and are bounded by C on that subspace.
In particular the exponential series of E is strongly convergent on every HC, and
therefore exp(E) may be expressed as a series on a dense subspace.
Theorem 11. The quantum operators bUσ and bVσ, acting on H(t)
σ , are normal.
Proof. On the one hand, u and v are bounded and self-adjoint, so the condi-
tions on the domains of bUσ and bVσ break down to ∇w. The latter operator
is well deﬁned on the subspace W1,2(T2, L N) ⊆L2(T2, L N) consisting of
all sections whose (distributional) covariant derivatives along
∂
∂u and
∂
∂v are
themselves L2-sections. A standard exercise shows that, with this domain, ∇w
is a closed operator with adjoint −∇w deﬁned on the same domain.
We check the commutation relations by direct computation, namely
h
bUσ, bU†
σ
i
=
h
u −iσ
πt∇w, u −iσ
πt∇w
i
=
= iσ
πt ·
σ
σ −σ + iσ
πt ·
σ
σ −σ −σσ
π2tt · 2Nπi
σ −σ = 0
16


## Page 17


and
h
bVσ, bV†
σ
i
=
h
v −i
πt∇w, v −i
πt∇w
i
=
= i
πt ·
σ
σ −σ + i
πt ·
σ
σ −σ −
1
π2tt · 2Nπi
σ −σ = 0 .
Since for every λ ∈C and every normal operator N on a Hilbert space λN
is also normal, the lemma ensures then that the following is well posed.
Deﬁnition 3. We deﬁne quantum operators associated to m and ℓon H(t)
σ
as
bmσ = exp

2πibUσ

,
bℓσ = exp

2πibVσ

.
Remark 12. A different branch of U, say continuous on an open dense, would differ
from the ﬁrst by a function c valued in Z, and thus locally constant. This change is of
no consequence on HU, and therefore the only effect on bUσ is to add c. However, the
multiplication by a locally constant function commutes with all differential operators,
and therefore by Baker-Campbell-Hausdorff we have
exp

2πi
 bUσ + c

= e2πic exp

2πibUσ

= exp

2πibUσ

.
In other words, bmσ is unaffected by choosing a different branch, and the situation is
analogous for V and bℓσ.
4.2
Trivialisation of the Hitchin-Witten connection and σ-independent
operators
Our next goal is to show that, after trivialising ˜∇using Proposition 8, the
operators from the previous section become σ-independent.
Deﬁnition 4. We deﬁne the σ-independent quantum operators of U, V, m, and ℓas
bU := exp
 r∆
bUσ exp
 −r∆

,
bV := exp
 r∆
bVσ exp
 −r∆

,
bm := exp
 r∆
 bmσ exp
 −r∆

,
bℓ:= exp
 r∆
bℓσ exp
 −r∆

.
The phrasing of the deﬁnition above is justiﬁed by the following result.
Theorem 13. The σ-independent operators are
bU = u −ie2rN −1
2Nπ
∇v
bV = v + ie2rN −1
2Nπ
∇u ,
bm = exp
 2πibU

= e2πiu exp
e2rN −1
N
∇v

,
bℓ= exp
 2πibV

= e2πiv exp

−e2rN −1
N
∇u

,
and therefore are indeed independent of σ.
17


## Page 18


Proof. We proceed to study bU and bV by expanding exp(±r∆) as power series.
Throughout the proof we will use that
[∆, u] = −i
π
 σ∇w −σ∇w

,
[∆, v] = −i
π
 ∇w −∇w

,
[∆, ∇w] = −2N∇w ,
[∆, ∇w] = 2N∇w ,
(11)
from which it follows by induction that
∆n bUσ = bUσ∆n −i
πt
n
X
k=1
n
k

(2N)k−1
(−1)kσt∇w −σt∇w

∆n−k ,
∆n bVσ = bVσ∆n −i
πt
n
X
k=1
n
k

(2N)k−1
(−1)kt∇w −t∇w

∆n−k .
To prove the theorem, suppose that subspaces HC ⊆L2(T2, L N), C ∈R>0
are given as in Remark 10, for E = ∆. We will show below that the series
Sψ :=
X
n,m∈Z⩾0
(−1)mrn+m
n!m!
∆n bUσ∆mψ .
(12)
is totally convergent whenever ψ lies in HC. Assuming this as a given for now,
we see on the one hand, summing over n ﬁrst and then over m, that
Sψ =
∞
X
m=0
(−r)m
m!
exp(r∆)bUσ∆mψ = exp(r∆)bUσ
 ∞
X
m=0
(−r)m
m!
∆mψ

= bUψ
where we used that exp(r∆) is continuous and bUσ closed. On the other hand,
a different arrangement of the terms yields
Sψ =
∞
X
n=0
n
X
k=0
(−1)n−krn
k!(n −k)! ∆k bUσ∆n−kψ =
∞
X
n=0
rn
n! adn
∆(bUσ)ψ ,
which using (11) evaluates to
Sψ =

u −iσ
πt∇w

ψ −
i
2Ntπ
∞
X
n=1
(2Nr)n
n!
 (−1)nσt∇w −σt∇w

ψ =
= uψ + i
π

−t
t
e−2Nr −1
2N
−1
t

σ∇w + e2Nr −1
2N
σ∇w

ψ =
= uψ + i(e2Nr −1)
2Nπ
 σ∇w + σ∇w

ψ =

u −i(e2Nr −1)
2Nπ
∇v

ψ .
This establishes the desired equality for bU on HC for every C, and thus on a
dense subspace. Since the operators are closed, the equality then extends to
the respective domains.
What remains to be seen is the total convergence of (12). It is well known
that ∆is a self-adjoint operator with essential domain consisting of all L2 sec-
tions whose weak Laplacian is itself an L2-section. Therefore, if ψ ∈dom(∆)
18


## Page 19


is approximated by a sequence of smooth sections ψn, then ∆ψn converges in
L2 (to ∆ψ). Given any ε > 0, using (9) we ﬁnd


∇w(ψn −ψm)


2 =
⟨∇w∇w(ψn −ψm), ψn −ψm⟩

⩽
π
|σ −σ|


(∆+ N)(ψn −ψm)


∥ψn −ψm∥< ε
for n and m sufﬁciently large. Therefore, ∇wψn is a Cauchy sequence in L2
and therefore ψ ∈dom(∇w) = dom(∇w). If, in particular, ψ ∈HC, then a
similar manipulation yields
∥∇wψ∥2 ⩽C + N
|σ −σ| ∥ψ∥2 =: R2∥ψ∥2 ,
and similarly for ∇wψ. Since ∆preserves HC, the same will hold with ∆nψ
in place of ψ for any n. Moreover, using the expressions for bUσ and bVσ in
Theorem 9 similar inequalities will hold for these operators as well.
For every n, m ∈Z⩾0 we then have that



∆n bUσ∆mψ



 ⩽
 1 +|σ| R

Cn+m∥ψ∥+
n
X
k=1
n
k

(2N)k−1|σ| RCn−k+m∥ψ∥
⩽Cm

Cn +|σ| R
n
X
k=0
n
k

(2N)kCn−k

∥ψ∥
= Cm

Cn +|σ| R(C + 2N)n

∥ψ∥.
This is enough to show total convergence of (12) as claimed, and ﬁnally estab-
lish our claim on bU.
The process for bV is completely analogous.
The relations for bm and bℓ
follow since exponentiation is stable under conjugation by unitary maps, the
splitting following by Baker-Campbell-Hausdorff.
4.3
The Weil-Gel’fand-Zak transform
Lemma 14 ([AK14b],[AM16]). The map W(N): S(AN, C) →C∞(T2, LN) deﬁned
by
f(x, n) 7→s(u, v) = eiπNuv X
m∈Z
f
√
Nu + m
√
N
, −m

e2πimv
is an isomorphism. Moreover, it intertwines the L2-pairings on the two spaces and
thus extends to an isometry of their completions.
The above map is called the Weil-Gel’fand-Zak transform, and it trans-
forms the quantum operators on H(t) according to the following statement.
19


## Page 20


Lemma 15. For every f ∈S(AN, C), one has
∇uW(N) f(x)

= W(N) √
Nf′(x)

,
∇vW(N) f(x)

= W(N)
2πi
√
Nxf(x)

,
e2πiuW(N) f(x)

= W(N)
e2πi
x
√
N e2πi n
N f(x)

,
e2πivW(N) f(x)

= W(N)
f

x −
1
√
N
, n + 1

.
Proof. We proceed by direct computation. Fast decay of Schwartz-class func-
tions and their derivatives justiﬁes term-by-term differentiation, which yields
∇uW(N) f(x)

= ∂
∂uW(N) f(x)

−iπNvW(N) f(x)

=
= eiπNuv X
m∈Z
∂
∂uf
√
Nu + m
√
N
, −m

e2πimv+
+ iπNvW(N) f

−iπNvW(N) f

=
= eiπNuv X
m∈Z
√
Nf′√
Nu + m
√
N
, −m

e2πimv .
Similarly, differentiation in v yields
∇vW(N) f(x)

= ∂
∂vW(N) f(x)

+ NπiuW(N) f(x)

=
= NπiueNπiuv X
m∈Z
f
√
Nu + m
√
N
, −m

e2πimv+
2πieNπiuv X
m∈Z
mf
√
Nu + m
√
N
, −m

e2πimv+
+ NπiuW(N) f(x, n)

=
= 2πi
√
NeNπiuv X
m∈Z
√
Nu + m
√
N

f
√
Nu + m
√
N
, −m

e2πimv .
By a simple manipulation we see that
e2πiuW(N) f(x)

= eiπNuv X
m∈Z
e2πiuf
√
Nu + m
√
N
, −m

e2πimv =
= eiπNuv X
m∈Z
e2πi(u+ m
N )e−2πi m
N f
√
Nu + m
√
N
, −m

e2πimv .
Finally, changing variable from m to m −1 we ﬁnd
e2πivW(N) f(x)

= eiπNuv X
m∈Z
f
√
Nu + m
√
N
, −m

e2πi(m+1)v =
= eNπiuv X
m∈Z
f
√
Nu + m −1
√
N
, −m + 1

e−2πimv .
20


## Page 21


Theorem 16. Let t = N + iS be ﬁxed, r as in Proposition 8, b := −ie2rN. Then the
Weil-Gel’fand-Zak transform intertwines the operators bm and bℓon L2(T2, L N) with
bmx and bℓx (cf. Deﬁnition 2) on L2(AN, C), respectively.
Proof. The identities of Lemma 15, being established on a dense subspace,
extend to the respective essential domains in L2.
Since W(N) is a unitary
isomorphism, the identities also carry over to the exponentials. Given that
e2πiu and ∇v correspond to multiplication operators, checking the relation
between bm and bmx reduces to
bmW(N) f(x)

= W(N)
e2πi
x
√
N e2πi n
N e2πi ib−1
√
N xf(x)

= W(N)  bmxf(x)

.
On the other hand, we have that
exp

−ib −1
N
∇u

W(N) = W(N) exp

−ib −1
√
N
d
dx

.
Following Remark 6 the exponential on the right-hand side acts, in the appro-
priate sense, as the shift by −ib−1
√
N in x. We may then conclude that
bℓW(N) f(x)

= W(N)

f

x −ib −1
√
N
−
1
√
N
, n + 1

= W(N) bℓxf(x)

,
which was our claim.
5
The annihilator of J(b,N)
M,K
Throughout this section we will always assume that N is an odd positive inte-
ger. For a ﬁxed S ∈R, let t = N + iS and
b = −ie2rN ,
cb = i(b + b−1)
2
,
q−1
2 = −eiπ qb2+1
N
as before. We then have an action of the algebra Aloc from (4) on the space of
meromorphic functions on AC
N by
E 7→bℓx ,
Q 7→bmx .
As before, if f is a meromorphic function it makes sense to consider its anni-
hilating left ideals I(f) and Iloc(f) in Aloc and A, respectively:
Iloc(f) =

p ∈Aloc : p( bmx,bℓx)f = 0

,
I(f) = Iloc(f) ∩A .
Deﬁnition 5. Let K be an embedded knot in a closed oriented 3-manifold M, J(b,N)
M,K as
in [AK14a, AM16]. We call bAC
q,(M,K), or the bAC-polynomial of (M, K), the unique
element of I(J(b,N)
M,K ) which, as a polynomial in E, has lowest degree and co-prime
coefﬁcients in Z[q± 1
2 , Q].
We shall often drop one or more of the subscripts in bAC
q,(M,K) where no
risk of ambiguity is present. Recalling from Section 2.2 the notations for the
A- and bA-polynomial of a knot, we are now ready to rephrase Theorem 4
more precisely.
21


## Page 22


Theorem 17. For K ⊆S3 the ﬁgure-eight knot 41 or 52, we have
bAC
q,K(Q, E) ·
 Q −1

= bAnh
q,K(Q, E) .
In the evaluation at q = 1 (corresponding to the limit t →∞), we have that
 m4 −1
bAC
1,K(m2, ℓ) = AK(m, ℓ) .
We shall dedicate the rest of the paper to the proof of this statement.
5.1
The ﬁgure-eight knot 41
The formula for J41(x) = J(b,N)
S3,41 (x) for x ∈AN ⊆AC
N may be found e.g.
in [AM16], and it reads
J41(x) = e4πi
cbx
√
N
Z
AN
ϕb(x −y)

y
2
ϕb(y)

x −y
2 dy .
We look for operators annihilating J41 by working on the integrand, which
we shall call Φ = Φ(x, y). The action of bmx and bℓx is well deﬁned on mero-
morphic functions of (x, y), and so is that of bmy and bℓy acting analogously
through the variable y. This action may be expressed as a representation of
the commutative tensor product A⊗2, whose formal generators we shall de-
note E1, Q1, E2, Q2. It is then immediate to check that
bℓxΦ = q bm2
x bm−2
y
 1 + q−1
2 bm−1
x
bmy

Φ ,
bℓyΦ = bm−2
x
 1 + q
1
2 bm−1
x
bmy
−1 1 + q−1
2 bm−1
y
−1Φ .
By a simple manipulation, this shows that the annihilator of Φ in A⊗2
loc contains
g1 := E1Q2
2 −q
1
2 Q1Q2 −qQ2
1 ,
g2 := E2Q1Q2
2 + q
1
2  E2Q2
1 + E2Q1 −q

Q2 + qE2Q2
1 .
With the aid of appropriate software (we used Singular [DGPS16]), one may
then run elimination to ﬁnd an element in this ideal that does not contain the
variable Q2, namely
P = Pq(E1, Q1, E2) =
= q3E2
2
 qE2Q2
1 −1)Q2
1E2
1
−
 q2E2Q2
1 −1

q4E2
2Q4
1 −q3E2
2Q3
1 −q(q2 + 1)E2Q2
1 −qE2Q1 + 1

E1
+ qE2
 q3E2Q2
1 −1

Q2
1 .
(13)
We shall not report here the full elimination process, which is rather long,
tedious, and computationally heavy, but the reader may verify that
q
9
2 Q2
1P = qa1g1 −a2g2 ,
22


## Page 23


where
a1 = E2Q1
 qE2Q2
1 −1
 q3E2Q2
1 + qE2Q1 −1

E1 + q2E2
 q3E2Q2
1 −1

Q2
1

Q2
+q
1
2  qE2Q2
1 −1

q5E2
2Q4
1 + q3E2
2Q3
1 + qE2
2Q2
1 −q2(q + 1)E2Q2
1 −(q + 1)E2Q1 + 1

E1
+q
5
2 E2
 E2Q1 −q
 q3E2Q2
1 −1

Q2
1
and
a2 =
 qE2Q2
1 −1

q3E2Q2
1 + qE2Q1 −1

E2
1 + q3E2

q3E2Q2
1 −1

Q2
1E1

Q2
−q
5
2 E2
 qE2Q2
1 −1

Q2
1E2
1
−q
3
2

q4(q + 1)E2
2Q4
1 + q2E2
2Q3
1 −q(q2 + q + 1)E2Q2
1 −qE2Q1 + 1

Q1E1
−q
7
2 E2
 q3E2Q2
1 −1

Q3
1 .
In order to obtain from P ∈A⊗2 an element of I(J41), we need to show that,
in an appropriate sense, all monomials in bmx, bℓx, and bℓy can be taken out of
the integral. While this is clearly the case for bmx, convergence of the integral
does depend on the value of x and on the speciﬁc contour, and some care is
needed when shifting either variable. With that in mind, for ﬁxed h < 0 and
a ∈−T −
cb
√
N we deﬁne (cf. Figure 1) a region
Rh,a :=

ξ + λ ib
√
N
∈T + a: ξ ∈R and h
2 < λ < −h

⊆C
and a contour
γh,a := ∂
 
y ∈C: Im

y −h ib
√
N

⩾0

\

T + cb
√
N
+a
!
× Z/NZ ⊆AC
N ,
(14)
where we recall that T is as in (3).
Proposition 18. Suppose h < 0 and a ∈−T −
cb
√
N are ﬁxed. For every x ∈AC
N
with x ∈Rh,a, the integral
χh,a(x) :=
Z
γh,a
Φ(x, y) dy
is absolutely convergent. The function χh,a is holomorphic, and if x ∈Rh,a ∩R then
e4πi
cbx
√
N χh,a(x) = J41(x) .
Proof. For ﬁxed x, the singularities of Φ(x, y) lie at the zeroes of ϕb(y) and
poles of ϕb(x −y). These occur for y in T and T + x, respectively, both of
which are contained in T + a if a ∈−T −
cb
√
N and x ∈T + a. Therefore, under
these conditions, the contour γh,a avoids all the singularities of the integrand.
23


## Page 24


R
iR
b
−cb
x
x + T
T
(a)
For ﬁxed x, the poles of the inte-
grand occur inside the inﬁnite triangles
with tips at x and −cb.
The shifted
triangle with tip at a contains all these
points if it contains both x and −cb.
R
iR
b
−cb
a
γε,a
γρ,a
Rh,a
(b) The contour follows R+ihb (h < 0)
and deviates along the triangle with tip
at a.
The integrand decays quickly in
y if x lies in the strip, and the poles lie
below γh,a if −cb and x do.
Figure 1: The distribution of the poles of the integrand and the contour are
illustrated for N = 1. The situation is analogous for higher N, up to rescaling
cb by
√
N and replicating the picture N times.
In order to study the behaviour of Φ at inﬁnity, express x and y as ξ + λ ib
√
N
and η + ρ ib
√
N, respectively—such expressions exist uniquely since Re(b) > 0.
Using Lemma 5 and expanding the deﬁnition of ⟨y⟩and ⟨x −y⟩(1) we see that
Φ(x, y)
 ≈














⟨y⟩2
⟨x −y⟩
 = C−(x, ρ)e−2πη(ρ+λ) Re(b)
√
N
for η →−∞

⟨y⟩
⟨x −y⟩2
 = C+(x, ρ)e2πη(ρ−2λ) Re(b)
√
N
for η →+∞
(15)
for some continuous functions C± of x and ρ alone. We then see that, for
ρ = h, the integrand decays exponentially near −∞if λ < −ρ and near +∞
if λ > ρ
2 . When that is the case, the integral is absolutely convergent, which
proves the ﬁrst part of our statement.
For the second part, suppose that x0 = (x0, n0) is ﬁxed with x0 ∈Rh,a,
and that B ⊆Rh,a is a compact neighbourhood of x0. By (15) it is then easy
to bound
Φ(x, y)
 by an absolutely integrable function of y alone, uniformly
for all x ∈B, whence the continuity of χh,a on that region by dominated
convergence. Furthermore, for any closed contour α inside B, the same bound
justiﬁes the use of Fubini-Tonelli in
Z
α
χh,a(x) dx =
Z
γh,a
Z
α
Φ(x, y) dx dy .
The holomorphicity of χh,a follows then from Morera’s theorem.
For the ﬁnal part, suppose that x is ﬁxed, with x ∈Rh,a ∩R, which is to
say that λ = 0. For a positive real number M consider, for each component
in AC
N, the compact region D enclosed by AN, γh,a, and the lines ibR ± M.
Since Φ(x, y) is holomorphic in y on D, the integral of Φ(x, y) dy around ∂D
vanishes.
Using (15) again, the integrand is bounded by 2C±(x, ρ) on the
components of ∂D along ibR ± M, uniformly in M. It is then easy to see that
24


## Page 25


the corresponding contributions vanish in the limit for M →∞, showing that
Z
AN
Φ(x, y) dy =
Z
γh,a
Φ(x, y) dy ,
which concludes our proof.
The proposition vindicates the claim that J41 extends holomorphically to
AC
N. It is now also clear that, for h and a as usual, h′ = h −1, a′ = a −
ib
√
N,
and x ∈Rh′,a′, we have
e4πi
cbx
√
N
Z
γh,a
bℓyΦ(x, y) dy = e4πi
cbx
√
N
Z
γh′,a′
Φ(x, y) dy = J41(x) ,
and that if both x, x −
ib
√
N ∈Rh,a then
e4πi
cbx
√
N
Z
γh,a
bℓxΦ(x, y) dy = q−1bℓxJ41(x) .
Up to choosing h and a sufﬁciently large, we see then that
0 = e4πi
cbx
√
N
Z
γh,a
Pq
 bℓx, bmx,bℓy

Φ(x, y) dy = Pq
 q−1bℓx, bmx, 1

J41(x)
on some open subset of AC
N, and therefore Pq(q−1bℓx, bmx, 1) annihilates J41.
We are now ready to prove Conjecture 1 for 41.
Theorem 19. Conjecture 1 holds for the ﬁgure-eight knot.
Proof. Call P ′ = P ′
q(E, Q) := Pq(q−1E, Q, 1), so that P ′
q(bℓx, bmx)J41 = 0. We can
see by direct comparison of (13) with (5) and (6) that
qP ′
q(E, Q)(Q −1) = bAnh
q,41(E, Q)
and
P ′
1(ℓ, m2) =
 m4 −1

A41(ℓ, m) .
By deﬁnition, bAC
q,41 is the preferred generator of Iloc(41), and therefore
P ′ = pbAC
q,41
for some p ∈Aloc. In the evaluation at q = 1, the above gives a factorisation of
(m4 −1)A41, and since A41 is known to be irreducible it follows that only one
between p and bAC
q,41 can contain the variable E. On the other hand, if bAC
q,41
were a polynomial of Q alone it would follow that J41 = 0, a contradiction.
Therefore, p is a non-zero polynomial in Q, so we can write bAC
q,41 = p−1P ′ in
Aloc. Since qP ′ has integer and co-prime coefﬁcients, it follows that p = q−1
and bAC
q,41 = qP ′, which as we have seen satisﬁes all the claimed properties.
5.2
The knot 52
The discussion for 52 is similar. From [AM16] we have
J52(x) = e2πi
cbx
√
N
Z
AN

y
 ⟨x⟩−1
ϕb(y + x)ϕb(y)ϕb(y −x) dy .
25


## Page 26


We will again call Φ = Φ(x, y) the integrand and see that
bℓxΦ = q
1
2 bmx
 1 + q−1
2 bm−1
x
bm−1
y
−1 1 + q
1
2 bmx bm−1
y

Φ ,
bℓyΦ = q−1
2 bm−1
y
 1 + q−1
2 bm−1
x
bm−1
y
−1 1 + q−1
2 bm−1
y
−1 1 + q−1
2 bm−1
y
bmx
−1Φ .
Therefore, the annihilator of Φ in A⊗2
loc contains
g1 := q
1
2  Q1E1 −q
1
2 Q2
1

Q2 + E1 −q
3
2 Q3
1 ,
g2 := E2Q1Q3
2 + q
1
2

E2Q2
1 + E2Q1 −q2Q1 + E2

Q2
2 + qE2

Q2
1 + Q1 + 1

Q2 + q
3
2 E2Q1 .
By eliminating E2 we ﬁnd that the element
P = Pq(E1, Q1, E2)
:= −q
1
2  qQ2
1 −1
 q2Q2
1 −1

E3
1
+ q
 qQ2
1 −1
 q4Q2
1 −1

q9E2Q5
1 −q7E2Q4
1 −q4(q3 + 1)E2Q3
1
+ q5(q + 1)Q3
1 + q2(q3 + 1)E2Q2
1 + q2(E2 + 1)Q1 −E2

E2
1
+ q
9
2 Q2
1
 q2Q2
1 −1
 q5Q2
1 −1

q6E2Q5
1 −q5(E2 + 1)Q4
1
−q2(q3 + 1)E2Q3
1 + q(q3E2 −q2 −q + E2)E2Q2
1 + qE2Q1 −E2

E1
+ q8Q7
1
 q4Q2
1 −1
 q5Q2
1 −1

may be expressed as
P = a1g1 + Q1g2
with
a1 =

−q
1
2 E2Q1
 qQ2
1 −1
 q2Q2
1 −1

E2
1 + q2(q + 1)E2Q2
1
 qQ2
1 −1
 q5Q2
1 −1

E1
−q
7
2 E2Q3
1
 q4Q2
1 −1
 q5Q2
1 −1

Q2
2
+

−qQ1
 qQ2
1 −1
 q2Q1 −1
 q3E2Q1 + E2 −q2
E2
1
+ q
5
2 Q1
 qQ2
1 −1
 q5Q2
1 −1

q3E2Q2
1 + (q + 1)E2Q1 −q2(q + 1)Q1 + E2

E1
−q8Q2
1
 q4Q2
1 −1
 q5Q2
1 −1
 E2Q1 −q2Q1 + E2

Q2
−q
1
2  qQ2
1 −1
 q2Q2
1 −1
 q4E2Q2
1 + 1

E2
1 −q
 qQ2
1 −1
 q5Q2
1 −1

·

q6E2Q4
1 −q5E2Q3
1 −q5Q3
1 −q2(q2 + 1)E2Q2
1 −q2E2Q1 −q2Q1 + E2

E1
−q
9
2 Q2
1
 q2Q2
1 + E2
 q4Q2
1 −1
 q5Q2
1 −1

and
a2 =
 qQ2
1 −1
 q2Q2
1 −1

E3
1 −q
3
2 Q1
 q2 + q + 1
 qQ2
1 −1
 q4Q2
1 −1

E2
1
+ q3Q2
1
 q2 + q + 1
 q2Q2
1 −1
 q5Q2
1 −1

E1
−q
9
2 Q3
1
 q4Q2
1 −1
 q5Q2
1 −1

.
26


## Page 27


Proposition 20. Let h < 0 and a ∈−T −
cb
√
N be ﬁxed, γh,a as in (14), and
Ra :=

(x, n) ∈AC
N : x ∈

T + cb
√
N
+ a

∩

−T −cb
√
N
−a
 
.
For every x ∈Ra, the integral
χh,a(x) :=
Z
γh,a
Φ(x, y) dy
is absolutely convergent. The function χh,a is holomorphic, and if x ∈Ra ∩AN then
e2πi
cbx
√
N χh,a(x) = J52(x) .
Proof. For ﬁxed x, every pole of Φ(x, y) has y ∈(T −x) ∪T ∪(T + x). A simple
check shows that
x ∈±

T + cb
√
N
+ a

=⇒T ± x ⊆T + cb
√
N
+ a ,
respectively. Therefore, if x ∈Ra and a ∈−T −
cb
√
N, then all the poles of
Φ(x, y) lie inside T +
cb
√
N + a, and in particular strictly below γh,a.
Writing x = ξ + λ ib
√
N and y = η + ρ ib
√
N, and using Lemma 5, we see that
Φ(x, y)
 ≈











⟨y⟩⟨x⟩−1 = C−(x, ρ)e−2πηρ Re(b)
√
N
for η →−∞

⟨x⟩−1
⟨y + x⟩⟨y −x⟩
 =

1
⟨y⟩2 ⟨x⟩3
 = C+(x, ρ)e4πηρ Re(b)
√
N
for η →+∞
for appropriate continuous functions C±. Therefore, Φ decays exponentially
at inﬁnity along γh,a as long as h < 0, regardless of the value of x, establishing
absolute convergence of the integral.
The rest of the proof is essentially identical to that of Proposition 18.
As in the case of 41, we may conclude that each χh,a is the holomorphic
extension of J52 on Ra, and that
e2πi
cbx
√
N
Z
γh,a
bℓd
y Φ(x, y) dy = J52(x)
for every d ∈Z⩾0 provided that h < −d and x ∈Ra, and that
e2πi
cbx
√
N
Z
γh,a
bℓxΦ(x, y) dy = e2πi
cbx
√
Nbℓxχh,a = −q−1
2bℓxJ52(x)
if x and x +
ib
√
N lie in Ra. Choosing h and a appropriately, we conclude that
0 =
Z
γa,h
Pq
 bℓx, bmx,bℓy

Φ(x, y) dy = Pq
 −q−1
2bℓx, bmx, 1

J52(x)
on some open subset, so Pq
 −q−1
2 E, Q, 1

∈I(J52).
Theorem 21. Conjecture 1 holds for the knot 52.
Proof. Calling P ′
q(E, Q) := Pq
 −q−1
2 E, Q, 1

, we see that P ′
q
 bℓx, bmx

J52 and
qP ′
q(E, Q)(Q −1) = bAnh
q,52(E, Q)
and
P ′
1(ℓ, m2) = (m4 −1)2A52(ℓ, m) .
The conclusion that bAC
q,52 = qP ′ follows by the same argument as for 41.
27


## Page 28


References
[And05]
J. E. Andersen. Deformation Quantization and Geometric Quan-
tization of Abelian Moduli Spaces.
Commun. Math. Phys.,
255(3):727–745 (Feb. 2005). doi:10.1007/s00220-004-1244-y.
[And06]
J. E. Andersen. Asymptotic faithfulness of the quantum SU(n) rep-
resentations of the mapping class groups. Annals of Mathematics,
163(1):347–368 (2006). doi:10.4007/annals.2006.163.347.
[And10]
J. E. Andersen.
Asymptotics of the Hilbert–Schmidt Norm of
Curve Operators in TQFT.
Lett Math Phys, 91(3):205–214 (Jan.
2010). doi:10.1007/s11005-009-0368-6.
[And12]
J. E. Andersen.
Hitchin’s connection, Toeplitz operators and
symmetry invariant deformation quantization. Quantum topology,
3:293–325 (2012). doi:10.4171/QT/30.
[AG11]
J. E. Andersen and N. L. Gammelgaard. Hitchin’s projectively ﬂat
connection, Toeplitz operators and the asymptotic expansion of
TQFT curve operators. In Grassmannians, Moduli Spaces and Vector
Bundles, vol. 14 of Clay Math. Proc., pages 1–24. Amer. Math. Soc.,
Providence, RI (2011).
[AG14]
J.
E.
Andersen
and
N.
L.
Gammelgaard.
The
Hitchin-
Witten Connection and Complex Quantum Chern-Simons Theory.
arXiv:1409.1035 (Sep. 2014).
[AGL12]
J. E. Andersen, N. L. Gammelgaard, and M. R. Lauridsen.
Hitchin’s connection in metaplectic quantization. Quantum topol-
ogy, 3:327–357 (2012). doi:10.4171/QT/31.
[AK14a]
J. E. Andersen and R. Kashaev. A TQFT from Quantum Teich-
müller Theory. Commun. Math. Phys., 330(3):887–934 (Jun. 2014).
doi:10.1007/s00220-014-2073-2.
[AK14b]
J. E. Andersen and R. Kashaev. Complex Quantum Chern-Simons.
arXiv:1409.1208 [math] (Sep. 2014).
[AK14c]
J. E. Andersen and R. Kashaev. Quantum Teichmüller theory and
TQFT.
In XVIIth International Congress on Mathematical Physics,
pages 684–692. World Sci. Publ., Hackensack, NJ (2014).
[AM19]
J. E. Andersen and A. Malusà.
Asymptotic properties of the
Hitchin-Witten connection.
In Lett Math Phys, 109: 1747–1775
(2019). doi:10.1007/s11005-019-01157-z
[AMR22]
J. E. Andersen, A. Malusà, and G. Rembado.
Genus-one com-
plex quantum Chern–Simons theory.
In J. Symplectic Geometry,
20(6):1215–1253 (2022). doi:10.4310/JSG.2022.v20.n6.a1
[AMR24]
J. E. Andersen, A. Malusà, and G. Rembado.
Sp(1)-symmetric
hyper-Kähler quantisation. Accepted by Paciﬁc Journal of Mathe-
matics (Mar. 2024). arXiv:2111.03584 [math].
28


## Page 29


[AM16]
J. E. Andersen and S. Marzioni. Level N Teichmüller TQFT and
Complex Chern-Simons Theory. Travaux mathématiques, 25:97–146
(Dec. 2016).
[AM23]
J. E. Andersen and S. Marzioni. The genus one Complex Quantum
Chern-Simons representation of the Mapping Class Group. In J.
Knot Theory Ramiﬁcations (2023).
[AN16]
J. E. Andersen and J.-J. K. Nissen. Asymptotic aspects of the Te-
ichmüller TQFT. Travaux mathématiques, 25:41–95 (Mar. 2017).
[AU07a]
J. E. Andersen and K. Ueno. Geometric construction of modular
functors from conformal ﬁeld theory. J. Knot Theory Ramiﬁcations,
16(02):127–202 (Feb. 2007). doi:10.1142/S0218216507005233.
[AU07b]
J. E. Andersen and K. Ueno. Abelian conformal ﬁeld theory and
determinant bundles. Int. J. Math., 18(08):919–993 (9 2007). doi:
10.1142/S0129167X07004369.
[AU12]
J. E. Andersen and K. Ueno. Modular functors are determined by
their genus zero data. Quantum Topol., 3(3):255–291 (2012). doi:
10.4171/QT/29.
[AU15]
J. E. Andersen and K. Ueno.
Construction
of the Wit-
ten–Reshetikhin–Turaev
TQFT
from
conformal
ﬁeld
theory.
Invent.
math.,
201(2):519–559
(Aug.
2015).
doi:10.1007/
s00222-014-0555-7.
[ADPW91] S. Axelrod, S. Della Pietra, and E. Witten. Geometric quantization
of Chern-Simons gauge theory. J. Differential Geometry, 33(3):787–
902 (1991).
[BB04]
S. Baseilhac and R. Benedetti. Quantum hyperbolic invariants of
3-manifolds with PSL(2,C)-characters. Topology, 43(6):1373–1423
(Nov. 2004). doi:10.1016/j.top.2004.02.001.
[BB07]
S. Baseilhac and R. Benedetti.
Quantum hyperbolic geometry.
Algebraic & Geometric Topology, 7(2):845–917 (Jun. 2007).
doi:
10.2140/agt.2007.7.845.
[BDP14]
C. Beem, T. Dimofte, and S. Pasquetti.
Holomorphic blocks in
three dimensions. J. High Energy Phys. 2014, 177 (Dec. 2014). doi:
10.1007/JHEP12(2014)177
[BGP23]
F. Ben Aribi, F. Guéritaud, E. Piguet-Nakazawa. Geometric trian-
gulations and the Teichmüller TQFT volume conjecture for twist
knots.
Quantum Topol. 14 (2023) 2, 285-406 (Sep. 2023).
doi:
10.4171/QT/178
[BP19]
F. Ben Aribi, E. Piguet-Nakazawa. The Teichmüller TQFT volume
conjecture for twist knots. Comptes Rendus Mathematique 357(3),
299-305 (March 2019). doi:10.1016/j.crma.2019.02.004
[CS74]
S.-S. Chern and J. Simons. Characteristic Forms and Geometric
Invariants. Annals of Mathematics, 99(1):48–69 (Jan. 1974).
29


## Page 30


[Con94]
J. B. Conway. A Course in Functional Analysis. Springer Science &
Business Media (Jan. 1994). ISBN 978-0-387-97245-9.
[CC+94]
D. Cooper, M. Culler, H. Gillet, D. Long, P. Shalen. Plane curves
associated to character varieties of 3-manifolds. In Invent. Math.
118(1), 47–84 (1994). doi:10.1007/BF01231526
[dW99]
A. C. da Silva and A. Weinstein. Geometric Models for Noncommuta-
tive Algebras, vol. 10 of Berkley Mathematics Lecture Notes. American
Mathematical Society (1999). ISBN 978-0-8218-0952-5.
[DGPS16]
W. Decker, G. M. Greuel, G. Pﬁster, and H. Schönemann. Singu-
lar 4-1-0 — A computer algebra system for polynomial compu-
tations. http://www.singular.uni-kl.de (2016).
[DFM11]
R. Dijkgraaf, H. Fuji, and M. Manabe. The volume conjecture,
perturbative knot invariants, and recursion relations for topolog-
ical strings. Nuclear Physics B, 849(1):166–211 (Aug. 2011). doi:
10.1016/j.nuclphysb.2011.03.014.
[Dim13]
T. Dimofte. Quantum Riemann surfaces in Chern-Simons theory.
Adv. Theor. Math. Phys., 17(3):479–599 (2013).
[Dim15]
T. Dimofte. Complex Chern-Simons theory at level k via the 3d-3d
correspondence. Comm. Math. Phys., 339 (2):619–662 (2015).
[DGG14]
T. Dimofte, D. Gaiotto, S. Gukov. Gauge theories labelled by three-
manifolds. In Commun. Math. Phys. 325, 367–419 (2014). doi:10.
1007/s00220-013-1863-2
[DGLZ09]
T. Dimofte, S. Gukov, J. Lenells, and D. Zagier. Exact results for
perturbative Chern–Simons theory with complex gauge group.
Commun. Number Theory Phys., 3(2):363–443 (Jun. 2009).
doi:
10.4310/CNTP.2009.v3.n2.a4.
[Fre95]
D. S. Freed.
Classical Chern-Simons theory. I.
Adv. Math.,
113(2):237–303 (1995). doi:10.1006/aima.1995.1039.
[FGL02]
C. Frohman, R. Gelca, and W. Lofaro. The A-polynomial from
the noncommutative viewpoint
Trans. Amer. Math. Soc. 354 (2):
735–747 (2002).
[Gar04]
S. Garoufalidis. On the characteristic and deformation varieties of
a knot. Proceedings of the Casson Fest, vol. 7 of Geom. Topol. Monogr.,
pages 291–309 (electronic). Geom. Topol. Publ., Coventry (2004).
doi:10.2140/gtm.2004.7.291.
[GLL18]
S. Garoufalidis, A. D. Lauda, and T. T. Q. Lê. The colored HOM-
FLYPT function is q-holonomic. In Duke Math J. 3: 397–447.
[GL05]
S. Garoufalidis and T. T. Q. Lê. The colored Jones function is q-
holonomic. In Geom. Topol. 9: 1253–1293 (2005).
[GL16]
S. Garoufalidis and T. T. Q. Lê. A survey of q-holonomic functions.
Enseign. Math. 62, no. 3/4, pp. 501–525 (2016).
30


## Page 31


[GS10]
S. Garoufalidis and X. Sun. The non-commutative A-polynomial
of twist knots. J. Knot Theory Ramiﬁcations, 19(12):1571–1595 (2010).
[Guk05]
S. Gukov. Three-Dimensional Quantum Gravity, Chern-Simons
Theory, and the A-Polynomial. Commun. Math. Phys., 255(3):577–
627 (Apr. 2005). doi:10.1007/s00220-005-1312-y.
[Hik01]
K. Hikami.
Hyperbolicity of partition function and quantum
gravity.
Nuclear Physics B, 616(3):537–548 (Nov. 2001).
doi:
10.1016/S0550-3213(01)00464-3.
[Hik04]
K. Hikami. Difference equation of the colored Jones polynomial
for the torus knot. In Int. J. Math. 15:959–965 (2004). doi:10.1142/
S0129167X04002582
[Hik07]
K.
Hikami.
Generalized
volume
conjecture
and
the
A-
polynomials: The Neumann–Zagier potential function as a classi-
cal limit of the partition function. Journal of Geometry and Physics,
57(9):1895–1940 (Aug. 2007). doi:10.1016/j.geomphys.2007.03.008.
[Hit90]
N. J. Hitchin. Flat connections and geometric quantization. Com-
munications in Mathematical Physics, 131(2):347–380 (1990).
doi:
10.1007/BF02161419.
[HS04]
J. Hoste and P. D. Shanahan.
A formula for the A-polynomial
of twist knots. J. Knot Theory Ramiﬁcations, 13(02):193–209 (Mar.
2004). doi:10.1142/S0218216504003081.
[KN63]
S. Kobayashi and K. Nomizu. Foundations of Differential Geometry,
vol. 1. Interscience Publishers (1963).
[Las98]
Y. Laszlo. Hitchin’s and WZW connections are the same. J. Differ-
ential Geom., 49(3):547–576 (1998). doi:10.4310/jdg/1214461110.
[Lau10]
M. R. Lauridsen. Aspects of Quantum Mechanics: Hitchin Connec-
tions and AJ Conjectures. Ph.D. thesis, Aarhus University (Jul. 2010).
[Lê06]
T. T. Q. Lê. The Colored Jones Polynomial and the A-Polynomial
of Knots. Adv. Math. 207:782–804 (2006). doi:10.1016/j.aim.2006.
01.006
[LT15]
T. T. Q. Lê and A. T. Tran. On the AJ conjecture for knots. Indiana
Univ. Math. J., 64(4):1103–1151 (2015).
[Mal18]
A. Malusà. Geometric Quantisation, the Hitchin-Witten Connection,
and Quantum Operators in Complex Chern-Simons Theory. PhD the-
sis, Aarhus University - QGM (2018).
[Mar16]
S. Marzioni.
Complex Chern–Simons Theory: Knot Invariants and
Mapping Class Group Representations. Ph.D. thesis, Aarhus Univer-
sity - QGM (Oct. 2016).
[RT91]
N. Y. Reshetikhin and V. G. Turaev. Invariants of 3-manifolds via
link polynomials and quantum groups. Inventiones mathematicae,
103(3):547–598 (1991).
31


## Page 32


[RT90]
N. Y. Reshetikhin and V. G. Turaev.
Ribbon graphs and their
invariants derived from quantum groups.
Comm. Math. Phys.,
127(1):1–26 (1990).
[Rol03]
D. Rolfsen. Knots and Links. AMS Chelsea Press (2003).
[Tur10]
V. G. Turaev. Quantum Invariants of Knots and 3-Manifolds. No. 18
in de Gruyter Studies in Mathematics. De Gruyter, 2nd edition
(2010). ISBN 978-3-11-022183-1.
[Wit89]
E. Witten. Quantum ﬁeld theory and the Jones polynomial. Com-
munications in Mathematical Physics, 121(3):351–399 (1989).
doi:
10.1007/BF01217730.
[Wit91]
E. Witten.
Quantization of Chern Simons Gauge Theory with
Complex Gauge Group. Communications in Mathematical Physics,
66:29–66 (1991).
[Woo92]
N. M. J. Woodhouse. Geometric Quantization. Oxford Mathematical
Monographs. The Clarendon Press, Oxford University Press, New
York, second edn. (1992).
ISBN 0-19-853673-9. Oxford Science
Publications.
32

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1711_11522v3_a_geometric_quantisation_view_on_the_aj_conjecture_for_the_teichm_ller_tqft
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1711_11522V3_A_GEOMETRIC_QUANTISATION_VIEW_ON_THE_AJ_CONJECTURE_FOR_THE_TEICHM_LLER_TQFT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

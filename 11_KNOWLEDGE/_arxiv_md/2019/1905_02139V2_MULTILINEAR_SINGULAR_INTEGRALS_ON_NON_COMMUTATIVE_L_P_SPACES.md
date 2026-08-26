---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.02139v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1905.02139v2_Multilinear_singular_integrals_on_non-commutative__L_p__spaces

> Source: 1905.02139v2_Multilinear_singular_integrals_on_non-commutative__L_p__spaces.pdf

> Pages: 37

---


## Page 1


arXiv:1905.02139v2  [math.CA]  14 Aug 2020
MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
Abstract. We prove Lp bounds for the extensions of standard multilinear Calderón-
Zygmund operators to tuples of UMD spaces tied by a natural product structure. The
product can, for instance, mean the pointwise product in UMD function lattices, or the
composition of operators in the Schatten-von Neumann subclass of the algebra of bounded
operators on a Hilbert space. We do not require additional assumptions beyond UMD on
each space – in contrast to previous results, we e.g. show that the Rademacher maximal
function property is not necessary. The obtained generality allows for novel applications.
For instance, we prove new versions of fractional Leibniz rules via our results concerning
the boundedness of multilinear singular integrals in non-commutative Lp spaces. Our
proof techniques combine a novel scheme of induction on the multilinearity index with
dyadic-probabilistic techniques in the UMD space setting.
1. Introduction
A Banach space X has the UMD property if any X-valued martingale diﬀerence se-
quence converges unconditionally in Lp for some (equivalently, all) p ∈(1, ∞). Standard
examples of UMD spaces are provided by the reﬂexive Lp function spaces, as well as the
reﬂexive Schatten-von Neumann subclasses Sp of the algebra of bounded operators on a
Hilbert space. The works by Burkholder [2] and Bourgain [1] yield an alternative char-
acterization: X is a UMD space if and only if singular integrals, in particular the Hilbert
transform, admit an Lp(X)-bounded extension. Such equivalence, albeit striking, is not so
surprising when viewed from the modern dyadic-probabilistic perspective on singular
integral operators. Indeed, Petermichl [43, 44] realized that the Hilbert transform lies in
the convex hull of certain dyadic operators akin to martingale transforms (the so-called
dyadic shifts), while Hytönen [28] extended this representation to general singular inte-
gral operators of Calderón-Zygmund type, relying on a probabilistic construction. These
2010 Mathematics Subject Classiﬁcation. 42B20 (primary), 46E40, 46L52 (secondary).
Key words and phrases. Calderón–Zygmund operators, singular integrals, multilinear analysis, non-
commutative spaces, representation theorems, UMD spaces.
F. Di Plinio has been partially supported by the National Science Foundation under the grants NSF-DMS-
1650810, NSF-DMS-1800628 and NSF-DMS-2000510.
K. Li was supported by Juan de la Cierva - Formación 2015 FJCI-2015-24547, by the Basque Government
through the BERC 2018-2021 program and by Spanish Ministry of Economy and Competitiveness MINECO
through BCAM Severo Ochoa excellence accreditation SEV-2017-0718 and through project MTM2017-82160-
C2-1-P funded by (AEI/FEDER, UE) and acronym “HAQMEC”.
H. Martikainen was supported by the Academy of Finland through the grants 294840 and 306901, and by
the three-year research grant 75160010 of the University of Helsinki. He is a member of the Finnish Centre
of Excellence in Analysis and Dynamics Research.
E. Vuorinen was supported by the Academy of Finland through the grant 306901, by the Finnish Centre of
Excellence in Analysis and Dynamics Research, and by Jenny and Antti Wihuri Foundation.
1


## Page 2


2
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
results have roots in the pioneering work of Figiel [13] and on the probabilistic approach
of Nazarov–Treil–Volberg to non-homogeneous Tb theorems [41].
The theory of linearsingular integrals on Banach spaces,beyond its intrinsic interest,has
historically been motivated by its interplay with several related areas, such as geometry
of Banach spaces [31, 32], elliptic and parabolic regularity theory [3, 47], the theory of
quasiconformal mappings [15]. Furthermore, vector-valued bounds may often be used
in the pursuit of their multi-parameter analogs [22, 27].
In this article, we are concerned with Banach-valued extensions of multilinear singular
integral operators. A linear singular integral takes the general form
T f(x) =
ˆ
Rd K(x, y) f(y) dy,
where diﬀerent assumptions on the kernel K lead to important classes of linear transfor-
mations arising across pure and applied analysis. The term singular integral refers just to
the underlying kernel structure – a Calderón-Zygmund operator is a bounded singular
integral operator. A heuristic model of an n-linear singular integral operator T in Rd is
then obtained by setting
T( f1, . . . , fn)(x) = U( f1 ⊗· · · ⊗fn)(x, . . . , x),
x ∈Rd, fi : Rd →C,
where U is a linear singular integral operator in Rnd.
For the basic theory see e.g.
Grafakos–Torres [18].
Multilinear singular integrals arise naturally from applications to partial diﬀerential
equations, complex function theory and ergodic theory, among others. Focusing on the
results of greater signiﬁcance for the present work, we mention that Lp estimates for the
fractional derivative of a product, often referred to as fractional Leibniz rules, are widely
employed in the study of dispersive equations starting from the work of Kato and Ponce
[33], descend from the multilinear Hörmander-Mihlin multiplier theorem of Coifman-
Meyer [4]. The bilinear Hilbert transform is a prime example of a modulation invariant
bilinear Calderón-Zygmund operator. It rose to prominence with Calderón’s ﬁrst com-
mutator program, and has been featured as a model operator in the study of bilinear
ergodic averages; the latter connection is expounded in e.g. [11]. Proving Lp estimates for
the bilinear Hilbert transform in the Lacey-Thiele framework [34, 35] involves a decom-
position into single trees, which are essentially modulated bilinear Calderón-Zygmund
operators.
Vector-valued extensions of multilinear Calderón-Zygmund operators have mostly
been studied within the more restrictive framework of ℓp spaces and function lattices.
Boundedness of these extensions is classically obtained through weighted norm inequal-
ities, more recently in connection with localized techniques such as sparse domination:
see [16] and the more recent [6, 37, 42] for a non-exhaustive overview of their interplay.
The paper [10], by Y. Ou and one of us, contains a bilinear multiplier theorem which
applies to certain non-lattice UMD spaces. The approach of [10] is based on a localization
of the UMD-valued tent space norms, see for instance [23], within the Carleson embed-
ding framework of Do and Thiele [12]. The tent space techniques lead to the additional
assumption of Lp estimates for a certain analogue of the Hardy-Littlewood maximal op-
erator obtained by replacing uniform bounds with randomized, or R-bounds, see e.g.
[47] for a deﬁnition. This assumption, usually referred to as the RMF property of X, dates


## Page 3


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
3
back to the work of Hytönen, McIntosh and Portal on the vector-valued Kato square root
problem [21], and is in fact necessary for the X-valued Carleson embedding theorem to
hold [20].
In this article, we obtain vector-valued extensions of multilinear singular integrals
to tuples of UMD spaces tied by a natural product structure, such as that of pointwise
product in UMD function lattices or, more generally in fact, that of composition within the
Schatten-von Neumann classes. We do not require additional conditions on the spaces
involved – in particular, we do not require the RMF property. Thus, we are able to
extend multilinear Calrerón–Zygmund operators to natural tuples of non-commutative
Lp spaces – a result which does not seem attainable via abstract theorems involving
multilinear RMF type assumptions. A motivating corollary is a version of the fractional
Leibniz rule for products of Schatten-von Neumann class-valued functions.
In contrast to [10, 21, 23], our techniques are dyadic-probabilistic: a multilinear version
of the representation theorem of Hytönen [28], which appeared in the bilinear case in
[39] by Y. Ou and three of us, reduces the problem to the boundedness of the extensions
of a class of multilinear dyadic model operators, namely paraproducts and multilinear
dyadic shifts of arbitrary complexity. The novelty lies in how we treat these operators –
multilinearity poses signiﬁcant problems in the vector-valued setup.
We note that UMD-valued extensions of bilinear, complexity zero dyadic shifts have
implicitly been treated in the work by Hytönen, Lacey and Parissis on the UMD dyadic
model of the bilinear Hilbert transform [30, Section 6]. The simple approach of [30] does
not extend to either the higher complexity or the multilinear cases. We tackle the n-linear
case by inducting suitably on the linearity, which is made possible by associating to our n-
tuples of UMD spaces a collection of related m-tuples, m < n. The framework is carefully
designed to allow us to treat non-commutative theory. Moreover, bilinear theory would
not reveal all the diﬃculties and is, in fact, strictly easier – a feature that is also present in
our followup paper [9] involving operator-valued multilinear analysis. Before providing
further insights on the novelty of our proof techniques, and comparisons to previous
approaches, we give the statements of our main results.
1.1. Main results. We start by discussing a simpler question, where the current literature
already has some restrictions that we can lift. If X is a Banach space and T is an n-linear
integral operator on Rd acting on n-tuples of functions in L∞
c (Rd), we may let T act on
(L∞
c (Rd) ⊗X) × L∞
c (Rd) × · · · × L∞
c (Rd) by
T  f1, f2, . . . , fn
 (x) =
X
e1,jT( f1,j, f2, . . . , fn)(x),
x ∈Rd,
f1 =
X
e1,j f1,j,
f1,j ∈L∞
c (Rd), e1,j ∈X.
A basic thing implied by our methods is that n-linear Calderón-Zygmund operators
extend boundedly when applied to one UMD-valued function and n −1 scalar func-
tions, without any additional assumption on the UMD space. We send to Subsection 2.4
for the precise deﬁnition of an n-linear Calderón-Zygmund operator. This is the sim-
plest complete multilinear analogue of Bourgain’s UMD Hörmander-Mihlin multiplier
theorem from [1]; see also Weis [47] and Hytönen-Weis [26] for the operator-valued,
non-translation invariant case.
In the bilinear, translation invariant, operator-valued setting, a related result appeared
in [10, Corollary 1.2] under the assumption,known to be rather restrictive,that X is a UMD


## Page 4


4
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
space with the non-tangential Rademacher maximal function property [21]. Theorem 1.1
shows, in particular, that the latter assumption is unnecessary. However, we formulate the
following more general version to facilitate the discussion below regarding the somewhat
special nature of bilinear theory.
1.1. Theorem. Let X1, X2, Y3 be UMD spaces with an associated product (a bounded bilinear
operator)
X1 × X2 →Y3 : (x1, x2) 7→x1x2,
|x1x2|Y3 ≤|x1|X1|x2|X2.
Let n ≥2 and T be an n-linear Calderón-Zygmund operator on Rd. The n-linear operator
T  f1, f2, . . . , fn
 (x) =
X
j1,j2
e1,j1e2,j2T( f1,j1, f2,j2, f3, . . . , fn)(x),
x ∈Rd,
f1 =
X
j1
e1,j1 f1,j1, f2 =
X
j2
e2,j2 f2,j2
f1,j, f2,j ∈L∞
c (Rd), e1,j1 ∈X1, e2,j2 ∈X2,
extends to a bounded operator
T: Lp1(Rd; X1)×Lp2(Rd; X2) ×
n
Y
k=3
Lpj(Rd) →Lqn+1(Rd; Y3),
1 < pk ≤∞, 1
n < qn+1 < ∞,
1
qn+1 =
n
X
k=1
1
pk .
The proof of this model case is an adaptation of the proof of Theorem 3.31 with some
additional observations regarding the bilinear case – see Remark 4.13. This simpler result
also showcases why the genuine n-linear theory that we formulate next is harder than
bilinear theory: the n-linear theory requires us to exploit a more careful product setting
so that we can run our inductive proof.
We also note that at least in the basic case
X1 = Y3 = X and X2 = C, Theorem 1.1 can also be seen as a corollary of Theorem 3.31
using Example 3.17. It is simpler to just look at the proof, however.
Our main theorem concerns extensions of n-linear CZO operators T to an n-tuple
X1, . . . , Xn of UMD Banach spaces lying in an enveloping algebra A, allowing for a
standard deﬁnition of (associative, not necessarily abelian) product A × A →A. We
refer to these conﬁgurations as UMD Hölder tuples if certain conditions are in place,
in particular, if the n-tuples are associated with suitable collections of related m-tuples,
m < n. If each Xj is a subspace of A, and fk ∈L∞
c (Rd) ⊗Xk for 1 ≤k ≤n, we may deﬁne
the extension of a scalar integral operator by
T   f1, . . . , fn
 (x) =
X
j1,...,jn
T( f1,j1, . . . , fn,jn)(x)
n
Y
k=1
ek,jk,
x ∈Rd,
fk =
X
jk
ek,jk fk,jk,
fk,jk ∈L∞
c (Rd), ek,jk ∈Xk.
(1.2)
The abstract setup is developed in Section 3. For expository purposes, herein we provide
a statement in a rather general concrete case of a UMD Hölder tuple. In the statement, we
denote by Lp(M) the non-commutative Lp spaces associated to a von Neumann algebra
M endowed with a normal, semiﬁnite, faithful trace τ.


## Page 5


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
5
1.3. Theorem. Let M be a von Neumann algebra endowed with a normal, semiﬁnite, faithful
trace. For s = 1, . . . , S, let (Ms, µs) be measure spaces and for s = 0, . . . , S let
1 < ps
1, . . . ps
n, qs
n+1 < ∞,
1
qs
n+1
=
n
X
k=1
1
ps
k
be Banach Hölder tuples. Let
Xk = LpS
k (MS, µs; LpS−1
k (MS−1, µS−1; · · · Lp1
k(M1, µ1; Lp0
k(M)) · · · ),
k = 1, . . . , n,
Yn+1 = LqS
n+1(MS, µS; LqS−1
n+1(MS−1, µS−1; · · · Lq1
n+1(M1, µ1; Lq0
n+1(M)) · · · ).
(1.4)
The n-linear operator (1.2) extends to a bounded operator
T :
n
Y
k=1
Lpk(Rd; Xk) →Lqn+1(Rd; Yn+1),
1 < pk ≤∞, 1
n < qn+1 < ∞,
1
qn+1 =
n
X
k=1
1
pk ,
T :
n
Y
k=1
L1(Rd; Xk) →L
1
n ,∞(Rd; Yn+1).
In fact, we have the stronger estimate
|⟨T( f1, . . . , fn), fn+1⟩| ≲




M

| f1|X1, . . . , | fn|Xn, | fn+1|Y∗
n+1




1 ,
M(g1, . . . , gn+1)(x) ≔sup
x∈Q
n+1
Y
j=1
⟨|gj|⟩Q,
⟨g⟩Q≔1
|Q|
ˆ
Q
g.
(1.5)
The estimate (1.5) is equivalent to a certain sparse bound, see Remark 3.29.
We send to Subsection 3.3 and to the references [7, 8] for more details on sparse
bounds and to [37, 38] for a survey of the weighted inequalities that may be derived as a
consequence.
Theorem 1.3 is obtained as a corollary of Theorem 3.31 using Example 3.21. However,
we remark that, at least to the best of the authors’ knowledge, the spaces (1.4) encompass
all known examples of UMD Banach spaces. We further remark that the mixed norm
structure of the spaces (1.4) prevents from using purely non-commutative tools, as (1.4)
may be interpreted as semi-commutative spaces only if ps
k does not vary with s for all
1 ≤k ≤n; on the other hand, (1.4) are not UMD lattices, so that Theorem 1.3 is out of
reach of purely lattice-type techniques.
Theorems 1.1 and 1.3 can be used to deduce certain weighted multilinear Leibniz
rules in the UMD-valued and non-commutative setting.
For simplicity of notation,
we particularize the statements to the bilinear, unweighted, non-endpoint case for the
homogeneous fractional derivative Ds f = F −1(|ξ|s bf(ξ)), in the setting of Theorem 1.1. A
variety of formulations may be found e.g. in the article by Grafakos and Oh [17].
1.6. Corollary (Fractional Leibniz rules in UMD spaces). Let X1, X2, Y3 be UMD spaces as
in the statement of Theorem 1.1. For all suﬃciently smooth f1 : Rd →X1, f2 : Rd →X2 there
holds 


Ds( f1 f2)



Lq3(Rd;Y3) ≲



Ds f1



Lp1(Rd;X1)



 f2



Lp2(Rd;X2) +



 f1



Lr1(Rd;X1)



Ds f2



Lr2(Rd;X2)


## Page 6


6
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
whenever s > d and
1 < p1, p2, r1, r2 ≤∞, 1
2 < q3 < ∞,
1
q3 = 1
p1 + 1
p2 = 1
r1 + 1
r2 .
Corollary 1.6 appears to be the ﬁrst instance of a Leibniz type rule in the full vector-
valued setting, with no additional assumptions on the UMD spaces involved. We have
not strived for optimality of the range for the fractional exponent s. While the range
obtained in Corollary 1.6 is wider than what would follow from results of Coifman-
Meyer type, see [17, Remark 1], the extension to the sharp range s > max
n
0, d
 1
q3 −1
 o
requires bilinear estimates for kernels which fail to be of the standard CZ type considered
herein. Such estimates are carried out e.g. in [17]: their extension to the full vector-valued
setting is left for future work.
Proof of Corollary 1.6. We follow the beginning of the proof of [17, Theorem 1]. The es-
timate we seek is reduced to a bound for the UMD-valued extension of three diﬀerent
bilinear paraproducts (meaning suitable parts of a Littlewood–Paley decomposition of
a product of functions – not in the exact sense as we use the word in connection with
dyadic model operators). We note that the symbol of the high-low paraproducts Π1 and
Π2 is of Coifman-Meyer type; therefore Π1, Π2 are bilinear CZO operators as deﬁned
in Subsection 2.4 and Theorem 1.3 applies directly. The high-high term Π3 is a bilinear
integral operator with kernel
K(x, y1, y2) =
X
m∈Z
ˆ
Rd 23mdφs(2m(u −x))ψ(2m(u −y1))ψ(2m(u −y2)) du
where ψ is a Schwartz function whose Fourier transform Ψ is supported in an annular
region around the origin and φs = Dsφ for some Schwartz function φ such that its Fourier
transform has compact support containing 0, so that
|φs(x)| ≲(1 + |x|)−(d+s),
x ∈Rd.
As s > d for us, this implies that Π3 is a bilinear CZO operator with a kernel K satisfying
∥Π3∥
L3×L3→L
3
2 + ∥K∥CZ(s−d)/2 ≲1,
where ∥K∥CZα is the kernel constant deﬁned in the beginning of Section 2.4. The required
bounds for Π3 follow from an application of Theorem 1.1.
□
1.2. Proof techniques and novelties. A basic example of an n-linear dyadic shift operator
of complexity zero on R, in adjoint form, is
( f1, . . . , fn+1) 7→
X
m∈Z
εm
ˆ  Y
k∈C
∆m fk(x)
 Y
k∈N
Em fk(x)

dx
where εm are bounded coeﬃcients, and Em and ∆m respectively indicate the conditional
expectation on the m-th dyadic ﬁltration and the corresponding martingale diﬀerence,
C ∩N = ∅and C ∪N = {1, . . . , n + 1}, with the key feature that the cardinality of the
cancellative indices C is always at least 2. We approach UMD-valued extensions of the
above forms to (n + 1)-tuples of UMD spaces via a novel induction argument, aimed at
reducing the cardinality of the set of non-cancellative indices N and the linearity of the shift
n at the same time. The induction relies upon a certain structure of the tuples involved,


## Page 7


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
7
which is most easily described in the bilinear, n = 2, case. Loosely speaking, we consider
UMD spaces X1, X2, X3 endowed with a linear functional τ deﬁned on all products e1e2e3,
ej ∈Xj, with the property that
∥e1∥X1 ∼
sup
|e2|X2=|e3|X3=1
|τ(e1e2e3)|
and the same holds for all permutations of X1, X2, X3. In combination with the martingale
decoupling inequality of McConnell [40] and Hytönen [29], and Stein’s inequality in UMD
spaces, this structure allows to reduce a trilinear shift form on X1, X2, X3 where, say, 1 ∈C
and 2 ∈N, to a bilinear shift form on X1, X∗
1, where both indices are cancellative, and
whose boundedness is known from the UMD character of X1. The induction is crucial in
the n-linear case to allow a repeated use of Stein’s inequality.
We remark here that the martingale decoupling has been previously used by Hänninen
and Hytönen [19] in the proof of a T1 theorem for linear singular integrals on UMD spaces
with operator-valued kernels, providing among other results a non-translation invariant
analogue of Weis’s theorem [47]. The multilinear operator-valued theory, together with
a related representation theorem, is the object of forthcoming work by the authors [9].
Acknowledgments. The authors would like to warmly thank Yumeng Ou for fruitful
discussions on the subject of multilinear UMD-valued singular integrals. F. Di Plinio is
grateful to Ben Hayes and Vittorino Pata for enlightening exchanges on factorization in
noncommutative Lp spaces.
2. Definitions and preliminaries
2.1. Vinogradov notation. We write A ≲B if A ≤CB for some absolute constant C. The
constant C can at least depend on the dimensions of the appearing Euclidean spaces,
on integration exponents, on the degree of linearity of the multilinear operators, and on
various Banach space constants. We use the notation A ∼B if B ≲A ≲B.
2.2. Dyadic notation. Let D0 be the dyadic lattice in Rd, deﬁned by
D0 = {2−k([0, 1)d + m): k ∈Z, m ∈Zd}.
We recall the random dyadic grids of Nazarov–Treil–Volberg, see for example [41]. The
version we use here is from [29]. Let Ω= ({0, 1}d)Z and let P be the natural probability
measure on Ωsuch that the coordinates are independent and uniformly distributed on
{0, 1}d. If Q ∈D0 and ω = (ωk)k∈Z ∈Ω, we set
Q + ω≔Q +
X
k: 2−k<ℓ(Q)
ωk2−k.
The random dyadic lattice Dω on Rd is deﬁned by Dω = {Q + ω: Q ∈D0}. By a dyadic
lattice D we mean that D = Dω for some ω.
Let X be a Banach space. If p ∈(0, ∞] we denote by Lp(X) = Lp(Rd; X) the usual Bochner
space of X-valued functions f : Rd →X. Let D be a dyadic lattice. Suppose Q ∈D and
f ∈L1
loc(X) (the set of locally integrable functions). We use the following notation:
• The side length of Q is denoted by ℓ(Q);
• ch(Q) consists of those Q′ ∈D such that Q′ ⊂Q and ℓ(Q′) = ℓ(Q)/2;
• If k ∈Z, k ≥0, then Q(k) denotes the cube R ∈D such that Q ⊂R and 2kℓ(Q) = ℓ(R);


## Page 8


8
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
• The average of f over Q is ⟨f⟩Q =
1
|Q|
´
Q f dx, and we also write EQ f = ⟨f⟩Q1Q;
• The martingale diﬀerence ∆Q f is ∆Q f = P
Q′∈ch(Q) EQ′ f −EQ f;
• For k ∈Z, k ≥0, deﬁne
∆k
Q f =
X
R∈D
R(k)=Q
∆R f
and
Ek
Q f =
X
R∈D
R(k)=Q
ER f.
Haar functions. When Q ∈D we denote by hQ a cancellative L2 normalized Haar function.
This means the following. Writing Q = I1 × · · · × Id we can deﬁne the Haar function hη
Q,
η = (η1, . . . , ηd) ∈{0, 1}d, by setting
hη
Q = hη1
I1 ⊗· · · ⊗hηd
Id ,
where h0
Ii = |Ii|−1/21Ii and h1
Ii = |Ii|−1/2(1Ii,l −1Ii,r) for every i = 1, . . . , d. Here Ii,l and Ii,r
are the left and right halves of the interval Ii respectively. If η , 0 the Haar function is
cancellative:
´
hη
Q = 0. We usually exploit notation by suppressing the presence of η, and
simply write hQ for some hη
Q, η , 0.
Notice that if f ∈L1
loc(X), then ∆Q f = P
η,0⟨f, hη
Q⟩hη
Q, or suppressing the η summation,
∆Q f = ⟨f, hQ⟩hQ. Here ⟨f, hQ⟩=
´
fhQ.
2.3. Deﬁnitions and properties related to Banach spaces. An extensive treatment of
Banach space theory is given in the books [24, 25] by Hytönen, van Neerven, Veraar and
Weis.
We say that {εk}k is a collection of independent random signs, where k runs over some index
set, if there exists a probability space (M, µ) so that ε: M →{−1, 1}, {εk}k is independent
and µ({εk = 1}) = µ({εk = −1}) = 1/2. Below, {εk}k will always denote a collection of
independent random signs.
Suppose X is a Banach space. We denote the underlying norm by | · |X. The Kahane-
Khintchine inequality says that for all x1, . . . , xM ∈X and p, q ∈(0, ∞) there holds that

E

M
X
m=1
εmxm

p
X
1/p
∼

E

M
X
m=1
εmxm

q
X
1/q
.
We also denote
∥(xm)∥Rad(X)≔

E

X
εmxm

2
X
1/2
.
The Kahane contraction principle says that if (am)M
m=1 is a sequence of scalars and p ∈(0, ∞],
then
(2.1)

E

M
X
m=1
εmamxm

p
X
1/p
≲max |am|

E

M
X
m=1
εmxm

p
X
1/p
.
Actually, if p ∈[1, ∞] and am ∈R, then (2.1) holds with “≤” in place of “≲”, see [24] for
more details.


## Page 9


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
9
A Banach space X is said to be a UMD space if for all p ∈(1, ∞), all X-valued Lp-
martingale diﬀerence sequences (dj)k
j=1 and signs ǫj ∈{−1, 1} there holds that
(2.2)




k
X
j=1
ǫjdj




Lp(X) ≲




k
X
j=1
dj




Lp(X).
Here the Lp(X)-norm is with respect to the measure space where the martingale diﬀerences
are deﬁned. If the estimate (2.2) holds for one p0 ∈(1, ∞), then it holds for all p ∈(1, ∞).
A version for UMD-valued functions of Stein’s inequality concerning conditional ex-
pectations is due to Bourgain. For a proof, see for example [24, Theorem 4.2.23]. For our
purposes we formulate the estimate in the following way. Suppose X is a UMD space
and let D ⊂Rd be a dyadic lattice. Suppose that for each Q ∈D we have a function
fQ ∈L1
loc(X) supported in Q (such that only ﬁnitely many of them are non-zero). Then for
all p ∈(1, ∞) there holds that
(2.3)
E




X
Q∈D
εQ⟨fQ⟩Q1Q




Lp(X) ≲E




X
Q∈D
εQ fQ




Lp(X).
The decoupling inequality. We record a special case of the decoupling estimate [19, Theorem
6] by Hänninen–Hytönen. These decoupling estimates originate from McConnell [40],
but see also Hytönen [29].
Let D be a dyadic lattice in Rd and Q ∈D. Let VQ be the probability measure space
VQ = (Q, Leb(Q), |Q|−1 dx⌊Q), where Leb(Q) is the set of Lebesgue measurable subsets of
Q and |Q|−1 dx⌊Q is the normalized Lebesgue measure restricted to Q. Deﬁne the product
probability space V = Q
Q∈D VQ, and let ν be the related measure. If y ∈V, we denote
the coordinate related to Q ∈D by yQ.
Suppose X is a UMD space, p ∈(1, ∞) and f ∈Lp(X). Let k ∈{0, 1, 2, . . . } and j ∈
{0, . . . , k}. Deﬁne Dj,k ⊂D by
(2.4)
Dj,k = {Q ∈D: ℓ(Q) = 2m(k+1)+j for some m ∈Z}.
[19, Theorem 6] implies that
(2.5)
ˆ
Rd

X
Q∈Dj,k
∆l
Q f(x)

p
X dx ∼E
ˆ
Rd
ˆ
V

X
Q∈Dj,k
εQ1Q(x)∆l
Q f(yQ)

p
X dν(y) dx
for any l ∈{0, 1, . . . , k}. The point of dividing to the subcollections Dj,k is that now ∆l
Q f
is constant on every Q′ ∈Dj,k such that Q′ ⊊Q, which is required by the decoupling
theorem (together with the fact that
´
∆l
Q f = 0 and spt ∆l
Q f ⊂Q).
2.4. Multilinear singular integrals and model operators. A function
K: Rd(n+1) \ ∆→C,
∆= {x = (x1, . . . , xn+1) ∈Rd(n+1) : x1 = · · · = xn+1},
is called an n-linear basic kernel if for some α ∈(0, 1] and CK < ∞it holds that
|K(x)| ≤
CK
 Pn+1
m=2 |x1 −xm|
dn ,


## Page 10


10
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
and for all j ∈{1, . . . , n + 1} it holds that
|K(x) −K(x′)| ≤CK
|xj −x′
j|α
 Pn+1
m=2 |x1 −xm|
dn+α
whenever x = (x1, . . . , xn+1) ∈Rd(n+1) \ ∆and x′ = (x1, . . . , xj−1, x′
j, xj+1, . . . xn+1) ∈Rd(n+1)
satisfy
|xj −x′
j| ≤2−1
max
2≤m≤n+1 |x1 −xm|.
The best constant CK is called ∥K∥CZα.
An n-linear operator T deﬁned on a suitable class of functions (e.g. on the linear
combinations of cubes) is an n-linear singular integral operator (SIO) with an associated
kernel K, if we have
⟨T( f1, . . . , fn), fn+1⟩=
ˆ
Rd(n+1) K(xn+1, x1, . . . , xn)
n+1
Y
j=1
fj(xj) dx
whenever spt fi ∩spt fj = ∅for some i , j.
We say that T is an n-linear Calderón–Zygmundoperator (CZO) if the following conditions
hold:
• T is an n-linear SIO.
• We have that for all m ∈{0, . . . , n} there holds that
∥Tm∗(1, . . . , 1)∥BMO≔sup
D
sup
K0∈D
 1
|K0|
X
K∈D
K⊂K0
|⟨Tm∗(1, . . . , 1), hK⟩|21/2
< ∞,
where the ﬁrst supremum is taken over all dyadic lattices D. Here T0∗≔T, Tm∗
denotes the mth adjoint of T for m ∈{1, . . . , n}, and the pairings ⟨Tm∗(1, . . . , 1), hK⟩
have a standard T1 type deﬁnition with the aid of the kernel K.
• We have that
∥T∥WBP≔sup
D
sup
Q∈D
|Q|−1|⟨T(1Q, . . . , 1Q), 1Q⟩| < ∞.
An SIO T is a CZO if and only if
(2.6)
∥T( f1, . . . , fn)∥Lqn+1(Rd) ≲
n
Y
m=1
∥fm∥Lpm(Rd)
for some (equivalently for all) exponents p1, . . . , pn ∈(1, ∞), qn+1 ∈(1/n, ∞) satisfying
Pn
m=1 1/pm = 1/qn+1. While such a T1 theorem is well-known (see e.g. [9, 18, 39]), we will
need a very precise version of this called a dyadic representation theorem. To this end,
we need some deﬁnitions.
Let k = (k1, . . . , kn+1), 0 ≤ki ∈Z, and let D be a dyadic lattice in Rd. An operator S = Sk
D
is called an n-linear dyadic shift if it has the form
(2.7)
S( f1, . . . , fn) =
X
K∈D
AK( f1, . . . , fn),


## Page 11


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
11
where
AK( f1, . . . , fn) =
X
Q1,...,Qn+1∈D
Q
(kj)
j
=K
aK,(Qj)
n
Y
j=1
⟨fj,ehQj⟩ehQn+1.
Here aK,(Qj) = aK,Q1,...,Qn+1 is a scalar satisfying the normalization
|aK,(Qj)| ≤
Qn+1
j=1 |Qj|1/2
|K|n
,
and there exist two indices j0, j1 ∈{1, . . . , n + 1}, j0 , j1, so thatehQj0 = hQj0,ehQj1 = hQj1 and
ehQj = h0
Qj if j < {j0, j1}.
An n-linear dyadic paraproduct π = πD also has n + 1 possible forms, but there is no
complexity (the k = (k1, . . . , kn+1)) associated to them. One of the forms is
π( f1, . . . , fn) =
X
K∈D
aK
n
Y
j=1
⟨fj⟩KhK,
where the coeﬃcients satisfy the BMO condition
(2.8)
sup
K0∈D
 1
|K0|
X
K∈D
K⊂K0
|aK|21/2
≤1.
This is the paraproduct associated with the tuple (1K/|K|, . . . , 1K/|K|, hK), and in the re-
maining n alternative forms the hK is in a diﬀerent position.
We call shifts and paraproducts dyadic model operators (DMOs). Suppose T is an n-linear
Calderón-Zygmund operator in Rd related to a kernel K. If f1, . . . , fn+1 are, say, Ln+1(Rd)
functions, then the representation theorem states that
(2.9)
⟨T( f1, . . . , fn), fn+1⟩= CTEω
∞
X
k1,...,kn+1=0
X
u
2−max kiα/2⟨Uk
Dω,u( f1, . . . , fn), fn+1⟩.
Here
|CT| ≲
n
X
m=0
∥Tm∗(1, . . . , 1)∥BMO + ∥T∥WBP + ∥K∥CZα
≲∥T∥Ln+1×···×Ln+1→L(n+1)/n + ∥K∥CZα,
α is the parameter in the Hölder continuity assumptions of the kernel of T, and the sum
over u is ﬁnite, say, over u = 1, 2, . . . , C(n, d). If max ki > 0, then Uk
Dω,u is some dyadic
shift Sk
Dω of complexity k with respect to the lattice Dω. If max ki = 0, then Uk
Dω,u is a shift
of complexity zero or a paraproduct. In this sense, a CZO T can be represented using
DMOs. For n = 2, a proof of this result is given by three of us and Y. Ou in [39]. The
n-linear case for general n, which requires certain modiﬁcations, is [9, Theorem 6.3]. The
reference [9, Theorem 6.3] is a more general theorem involving operator-valued CZOs.
We note that the additional assumptions related to the operator-valued setup, such as
the RMF assumption, concern only the estimation of the model operators. They are not


## Page 12


12
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
needed for the above stated structural theorem, which has essentially the same proof in
the scalar-valued and operator-valued settings.
As DMOs satisfy Lp estimates in the full expected range of exponents, the T1 theorem
follows from the representation theorem. Our main task in this paper will be to prove
Lp-bounds for the extensions of n-linear DMOs to suitably deﬁned tuples of UMD spaces,
which we term UMD Hölder tuples and deﬁne in the subsequent section.
3. UMD H¨older tuples and the boundedness of multilinear SIOs
Throughout this section, and the remainder of the article, we make use of the follow-
ing notational conventions. For m ∈N we write Jm≔{1, . . . , m} and denote the set of
permutations of J ⊂Jm by Σ(J). We simply write Σ(m) in place of Σ(Jm). We say that
p1, . . . , pm is a Hölder tuple of exponents if
(3.1)
1 < p1, . . . , pm < ∞,
m
X
j=1
1
pj = 1.
3.1. UMD Hölder tuples. The notion of UMD Hölder tuple involves ﬁxing an associative
algebra A over C. We denote the associative operation A × A →A by the product
notation, that is, we write (e, f) 7→e f. In the abstract deﬁnition, we do not ﬁnd useful
for A itself to be endowed with a topology; on the other hand, we will work with linear
subspaces of A endowed with a Banach norm.
We assume that there exists a subspace L1 of A and a linear functional τ : L1 →C,
which we refer to as trace.
Given an m-tuple (X1, . . . , Xm) of Banach subspaces of A, we construct the seminorm
(3.2)
|e|Y(X1,...,Xm) = sup


τ

e
m
Y
ℓ=1
eσ(ℓ)



: σ ∈Σ(m), |ej|Xj = 1, j = 1, . . . , m

on the subspace
(3.3)
Y(X1, . . . , Xm) =
e ∈A : e
m
Y
ℓ=1
eσ(ℓ) ∈L1 ∀σ ∈Σ(m), ej ∈Xj, j = 1, . . . , m

of A. The next lemma clariﬁes the intent of deﬁnition (3.2): if | · |Z is a seminorm such
that all (m + 1)-linear forms on X1 × · · · × Xm × Z in (3.5) below are bounded, then the
Z-seminorm dominates the seminorm Y(X1, . . . , Xm).
3.4. Lemma. Let (X1, . . . , Xm) be a m-tuple of Banach subspaces of A. Suppose that e ∈A
belongs to the subspace (3.3). Then
(3.5)

τ

e
m
Y
ℓ=1
eσ(ℓ)



≤|e|Z
m
Y
j=1
|ej|Xj,
∀σ ∈Σ(m), ej ∈Xj, j = 1, . . . , m,
holds for |e|Z = |e|Y(X1,...,Xm). In addition, if | · |Z is a seminorm on A such that (3.5) holds,
|e|Y(X1,...,Xm) ≲|e|Z.
Proof. Immediate from the deﬁnitions.
□


## Page 13


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
13
3.6. Deﬁnition (Admissible spaces). We say that a Banach subspace X of A is admissible
if Y(X) from (3.3) is a Banach space with respect to | · |Y(X) of (3.2)1, the map
(3.7)
y ∈Y(X) 7→x∗[y] ∈X∗,
x∗[y](x) = τ(yx),
x ∈X,
is onto, and furthermore, for each x ∈X, y ∈Y(X), xy ∈L1 and
(3.8)
τ(xy) = τ(yx).
3.9. Remark. If X is admissible, then the map (3.7) is an isometric bijection from Y(X) onto
X∗. We are thus allowed to identify Y(X) with X∗via (3.7) and we do so without explicit
mention from now on. Notice that if X is admissible, then X is a UMD space if and only
if Y(X) is.
For our purposes, it is convenient to state the next observation in the form of a lemma.
3.10. Lemma. Let X be admissible and reﬂexive. If Y(X) is also admissible, then Y(Y(X)) = X as
sets and |x|Y(Y(X)) = |x|X for all x ∈X.
Proof. The reﬂexivity of X and Remark 3.9 imply that Y(Y(X)) is isometrically isomorphic
with X. Here we want to show that they are actually equal as sets with equal norms.
Denote Y≔Y(X) and Z≔Y(Y). It follows quite directly from the deﬁnitions that X is a
subset of Z.
Let ϕ: X∗→Y be the isometric isomorphism from the deﬁnition of the admissibility
of X. This induces the isometric isomorphism φ: X∗∗→Y∗deﬁned by
φ(x∗∗)(y)≔x∗∗(ϕ−1(y)),
where x∗∗∈X∗∗and y ∈Y. Since X is reﬂexive and Y is admissible, we have the canonical
isometric isomorphism ρ: X →X∗∗and the isometric isomorphism η: Y∗→Z. Now, the
composition η ◦φ ◦ρ: X →Z is an isometric isomorphism.
Suppose x ∈X and denote z≔η ◦φ ◦ρ(x). Let y ∈Y. Then we have that
τ(zy) = η−1(z)(y) = φ−1 ◦η−1(z)(ϕ−1(y)) = ϕ−1(y)(ρ−1 ◦φ−1 ◦η−1(z)) = τ(xy).
Since x and z are both elements of Z, the fact that τ(zy) = τ(xy) for all y ∈Y implies that
x = z. Thus, the isometric isomorphism η ◦φ ◦ρ: X →Z is actually the identity map.
□
If X, X1, . . . , Xm are Banach spaces we write X = Y(X1, . . . , Xm) to mean that X and
Y(X1, . . . , Xm) coincide as sets, Y(X1, . . . , Xm) is a Banach space with the norm | · |Y(X1,...,Xm),
and that the norms are equivalent, that is, |x|X ∼|x|Y(X1,...,Xm) for all x ∈X.
We turn to deﬁning UMD Hölder m-tuples relatively to A, τ. We ﬁrst do so for m = 2.
3.11. Deﬁnition (UMD Hölder pair). Let X1, X2 be admissible spaces. We say that {X1, X2}
is a UMD Hölder pair if X1 is a UMD space and X2 = Y(X1). In view of Remark 3.9 and
Lemma 3.10 one can equivalently say that {X1, X2} is a UMD Hölder pair if X2 is a UMD
space and X1 = Y(X2).
For m ≥3 the deﬁnition of a UMD Hölder m-tuple is given inductively on m as follows.
3.12. Deﬁnition (UMD Hölder m-tuple, m ≥3). Let X1, . . . , Xm be admissible spaces. We
say that {X1, . . . , Xm} is a UMD Hölder m-tuple if the following properties hold.
1This includes that if y ∈Y(X) then |y|Y(X) < ∞.


## Page 14


14
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
P1. For all j0 ∈Jm there holds
Xj0 = Y
n
Xj : j ∈Jm \ {j0}
o
.
P2. If 1 ≤k ≤m−2 and J = {j1 < j2 < · · · < jk} ⊂Jm, then Y(Xj1, . . . , Xjk) is an admissible
Banach space with the norm (3.2) and
(3.13)
{Xj1, . . . , Xjk, Y(Xj1, . . . , Xjk)}
is a UMD Hölder (k + 1)-tuple.
The following remark is an important consequence of the deﬁnition.
3.14. Remark. Let m ≥3 and {X1, . . . , Xm} be a UMD Hölder m-tuple. Then according to
P2 the pair {Xj0, Y(Xj0)} is a UMD Hölder pair, which by Deﬁnition 3.11 implies that Xj0
and Y(Xj0) are UMD spaces. The inductive nature of the deﬁnition then ensures that each
Y(Xj1, . . . , Xjk) appearing in (3.13) is a UMD space.
3.15. Remark. Let m ≥2 and {X1, . . . , Xm} be a UMD m-Hölder tuple. Let ej ∈Xj for j ∈Jm.
For each σ ∈Σ(m), as Xσ(1) = Y(Xσ(2), . . . , Xσ(m)), we necessarily have Qm
j=1 eσ(j) ∈L1 and
|τ(eσ(1) · · · eσ(m))| ≤|eσ(1)|Y(Xσ(2),··· ,Xσ(m))
m
Y
j=2
|eσ(j)|Xσ(j) =
m
Y
j=1
|ej|Xj.
We clarify the extent of our deﬁnition with some examples of UMD Hölder tuples.
3.16. Example. It is immediate to verify that the m-tuple Xj = C, j = 1, . . . , m, is a UMD
Hölder m-tuple with respect to the usual product.
The next example is of relevance if one wants to deduce Theorem 1.1 in the basic case
X1 = Y3 = X and X2 = C from Theorem 3.31. However, otherwise we do not need it, and
Theorem 1.1 is best seen mimicking our main proofs.
3.17. Example. Let X = X1 be a complex UMD space and denote X2 = X∗. The goal of
this example is to show that for each m ≥2 the tuple {X1, X2, . . . , Xm} with Xj = C for
2 < j ≤m is a UMD Hölder tuple. This is conceptually simple but requires some work in
order to deﬁne a suitable enveloping algebra A. We let V = X ⊕X∗, and deﬁne A to be
the tensor algebra over V, namely
A =
∞
M
k=0
V⊗k.
We let
L1 = span{e ⊗e∗+ f ∗⊗f, e, f ∈X, e∗, f ∗∈X∗};
notice that this is a linear subspace of V⊗2. We then deﬁne the functional τ by
τ

e ⊗e∗+ f ∗⊗f

= ⟨f ∗, e⟩+ ⟨e∗, f⟩
for e, f ∈X, e∗, f ∗∈X∗and extend it to all of L1 by linearity. We notice that the deﬁnition
(3.3) yields that
Y(Xj1, . . . , Xjk) =

X
1 < {j1 . . . , jk}, 2 ∈{j1 . . . , jk},
X∗
1 ∈{j1 . . . , jk}, 2 < {j1 . . . , jk},
C
{1, 2} ⊂{j1 . . . , jk} or {1, 2} ∩{j1 . . . , jk} = ∅.


## Page 15


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
15
With this information in hand, we learn that X, X∗, C are admissible spaces. Proceeding
by induction on m, we then easily verify that {X1, X2, . . . , Xm} is a UMD Hölder tuple.
We now start explaining how non-commutative Lp spaces ﬁt our abstract framework.
3.18. Example. Consider a von Neumann algebra M ⊂B(H), namely a self-adjoint unital
subalgebra of the algebra of bounded linear operators on a complex Hilbert space Hwhich
is closed in the weak operator topology [45, 46]. Let M+ = {A ∈M : ⟨Ah, h⟩≥0 ∀h ∈H}
denote the positive part of M. A trace τ is a functional M+ →[0, ∞] satisfying
τ(A + λB) = τ(A) + λτ(B),
∀A, B ∈M+, λ > 0
as well as the tracial property
τ(AA∗) = τ(A∗A)
for all A ∈M. Following [46], we assume τ is normal, semiﬁnite, faithful (n.s.f.) and deﬁne
the corresponding space of measurable operators A = L0(M) equipped with convergence
in measure: a detailed deﬁnition is in [46]. Then A is a (metrizable) topological ∗-algebra
and M is dense in A. We will also recall the notion of S+, S as introduced in [46, p.1463]:
S+ is the cone of those A ∈M+ such that τ(supp A) < ∞, where supp A is the least
projection P ∈M+ with PA = A, and S ⊂M is the linear span of S+. We note [48,
Proposition 1.15(ii)] that τ may be extended to a unique linear functional on S, satisfying
(3.19)
τ(A∗) = τ(A),
τ(AB) = τ(BA),
∀A, B ∈S.
For 1 ≤p < ∞, we call noncommutative Lp space the Banach subspace of A obtained by
completion of S with respect to the norm
∥A∥Lp(M) =
"
τ
 
A⋆A
 p
2
!# 1
p
,
1 ≤p < ∞.
In fact, we record the characterization
Lp(M) =
n
A ∈A : τ

(A⋆A))
p
2

< ∞
o
;
in the above equality, τ denotes the extension of the trace to the positive part of A deﬁned
via generalized singular numbers [46]. We also point out the Hölder inequality
∥ξ1ξ2∥Lp(M) ≤∥ξ1∥Lp1(M)∥ξ2∥Lp2(M),
1
p = 1
p1 + 1
p2
valid whenever 1 ≤p1, p2, p < ∞. A suitable substitute holds for p = ∞if the Lp(M)-norm
is replaced by the B(H)-norm. Furthermore, notice that τ may be extended from S to a
unique linear bounded functional on L1(M) satisfying
|τ(A)| ≤∥A∥L1(M).
The tracial property (3.19) extends to the following: if A, B ∈A are such that A ∈Lp(M)
and B ∈Lp′(M), then
(3.20)
τ(AB) = τ(BA).
This is the concrete equivalent of property (3.8) we assumed in the abstract setup. We
refer to [48, Rem. 1.2.11] for the details of (3.20).


## Page 16


16
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
For 1 < p < ∞, we then have Lp(M)∗= Lp′(M) with isometric isomorphism given by
the Riesz representation map
λ ∈Lp(M)∗7→Bλ ∈Lp′(M),
λ(A) = τ(BλA)
∀A ∈Lp(M).
A fortiori, Lp(M) is reﬂexive for 1 < p < ∞. For our purposes, it is also important to
observe that Lp(M) is a UMD space in the same range [46, Corollary 7.7]. We detail below
two concrete examples of von Neumann algebras equipped with a n.s.f. trace.
If M is an abelian von Neumann algebra, then M = L∞(M, µ) for some measure
space (M, µ), a n.s.f. trace is obtained by integration with respect to the measure µ, and
A = L0(M, µ), the topological ∗-algebra of measurable functions on M with respect to
convergence in measure. Then Lp(M) = Lp(M, µ) for 1 ≤p < ∞.
If M = B(H), the bounded linear operators over a separable Hilbert space H and
τ(A) =
∞
X
j=1
⟨Aei, ei⟩
where ei is any orthonormal basis of H [46, Example (ii), p. 1465], then the spaces Lp(M)
are referred to as Schatten-von Neumann classes and denoted by Sp.
Let now pj, j = 1, . . . , m be a Hölder tuple as in (3.1). We claim that Xj = Lpj(M) is a
UMD Hölder tuple relative to the algebra A = L0(M), with trace τ. This can be proved
by induction on m, relying on the equality
Lp(J)(M) = Y({Lpj(M) : j ∈J}),
1
p(J) = 1 −
X
j∈J
1
pj
valid for each ∅⊊J ⊊Jm, whose veriﬁcation is immediate and left to the reader.
3.21. Example. In Appendix A, we prove that if {ps
j : 1 ≤j ≤m} are Hölder tuples of
exponents as in (3.1) for s = 0, . . . , S, M is a von Neumann algebra with n.s.f. trace τ as in
Example 3.18, and (Ms, µs) are σ-ﬁnite Borel measure spaces for s = 1, . . . , S, the tuple of
spaces
Xj = LpS
j (MS, µS; LpS−1
j
(MS−1, µS−1; · · · Lp1
j (M1, µ1; Lp0
j (M)) · · · )
is a UMD Hölder m-tuple relative to the trace
f 7→
ˆ
M1×···×MS
τ( f(t1, . . . , tS)) dµ1 × · · · × µS(t1, . . . , tS).
A precise statement is provided in Proposition A.1.
3.2. Extensions of CZOs. If X is a Banach space we will use the notation L∞
c ⊗X for
functions of the type PN
i=1 fiei, where N ∈N, fi ∈L∞
c (Rd) =: L∞
c and ei ∈X.
Let {X1, . . . , Xn+1} be a UMD Hölder tuple where n ≥1. Suppose T0 is an n-linear
CZO with a kernel K0 as deﬁned in Section 2.4. Since we know that T0 is a bounded
operator, see (2.6), we know that ⟨T0( f1, . . . , fn), fn+1⟩makes sense for fj ∈L∞
c . We deﬁne


## Page 17


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
17
the corresponding (n + 1)-linear form
ΛT0 : L∞
c ⊗X1 × · · · × L∞
c ⊗Xn+1 →C,
ΛT0( f1, . . . , fn+1) =
X
a1,...,an+1
⟨T0( f1,a1, . . . , fn,an), fn+1,an+1⟩τ
 n+1
Y
j=1
ej,aj

,
(3.22)
where fj = PNj
a=1 fj,aej,a. If U is a dyadic model operator as in Section 2.4 we deﬁne the
form ΛU in the corresponding way. We can also make sense of ΛU more directly. For
example, if U is a dyadic shift as in (2.7), then
(3.23)
ΛU( f1, . . . , fn+1) =
X
K∈D
X
Q1,...,Qn+1∈D
Q
(kj)
j
=K
aK,(Qj)τ
 n+1
Y
j=1
⟨fj,ehQj⟩

.
3.24. Remark. We chose to utilize the identity permutation in Σ(n + 1) for the product
appearing in (3.22). However, the notion of being a UMD Hölder tuple is clearly invariant
under reordering of {X1, . . . , Xn+1} .
Let pj ∈(1, ∞) for j ∈Jn+1 be such that Pn+1
j=1 1/pj = 1. From Theorem 3.31 it will follow
among other things that
(3.25)
|ΛT0( f1, . . . , fn+1)| ≲
n+1
Y
j=1
∥fj∥Lpj(Xj).
Based on this boundedness one can deﬁne as usual n+1 adjoint operators. Let us describe
how the adjoints look like in our Hölder tuple set up.
Fix j0 ∈Jn+1 and fj ∈Lpj(Xj) for j ∈Jn+1 \ {j0}. Consider the linear functional
(3.26)
fj0 ∈Lpj0(Xj0) 7→ΛT0( f1, . . . , fn+1),
which is bounded because of (3.25). Recall that Lpj0(Xj0)∗is identiﬁed with L(pj0)′(Y(Xj0))
with duality pairing
⟨g, fj0⟩=
ˆ
Rd τ(g(x) fj0(x)) dx.
Therefore, there exists a function
T∗j0( fj : j ∈Jn+1 \ {j0})≔Tj0∗( f1, . . . , fj0−1, fj0+1, . . . , fn+1) ∈L(pj0)′(Y(Xj0))
so that
ΛT0( f1, . . . , fn+1) =
ˆ
Rd τ(T∗j0( fj : j ∈Jn+1 \ {j0})(x) fj0(x)) dx.
The n-linear bounded operator
Tj0∗: Lp1(X1) × · · · × Lpj0−1(Xj0−1) × Lpj0+1(Xj0+1) × · · · × Lpn+1(Xn+1) →L(pj0)′(Y(Xj0))
is one of the adjoint operators. In the same way one can deﬁne the adjoint Tj∗
0 of T0 so
that
⟨Tj0∗
0 (g1, . . . , gj0−1, gj0+1, . . . , gn+1), gj0⟩= ⟨T0(g1, . . . , gn), gn+1⟩,
where gj ∈Lpj.


## Page 18


18
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
Suppose fj = PNj
a=1 fj,aej,a ∈L∞
c ⊗Xj for j ∈Jn+1 \ {j0}. A calculation involving the
invariance of τ under cyclic permutations yields that
T∗j0( fj : j ∈Jn+1 \ {j0})
=
X
Tj0∗
0 ( fj,aj : j ∈Jn+1 \ {j0})ej0+1,aj0+1 · · · en+1,an+1 · · · ej0−1,aj0−1.
3.3. Sparse domination of dyadic operators. The following basic sparse domination
result, Lemma 3.27, was ﬁrst proved by Culiuc, Ou and one of us in the linear scalar-
valued setting in [6, 7] and recast by Y. Ou and three of us in the multilinear scalar-valued
case [39]. The proof in our current Banach-valued setting is completely analogous.
Let η ∈(0, 1). We say that a collection S of cubes in Rd (not necessarily dyadic) is
η-sparse (or just sparse) if for every Q ∈S there exists a set EQ ⊂Q with |EQ| > η|Q| so
that the sets EQ, Q ∈S, are pairwise disjoint.
3.27. Lemma. Let n ≥1, {X1, . . . , Xn+1} be a UMD Hölder tuple, D be a dyadic grid, k =
(k1, . . . , kn+1), 0 ≤ki ∈Z. Suppose that the scalars aK,(Qj) satisfy the normalization
|aK,(Qj)| ≤A1
n+1
Y
j=1
|Qj|1/2|K|−n
and we are given scalar functions uj,Q = P
Q′∈ch(Q) cj,Q′1Q′ satisfying |uj,Q| ≤|Q|−1/2.
If there exists a Hölder tuple p1, . . . , pn+1 as in (3.1) such that the forms
UD′(g1, . . . , gn+1)≔
X
K∈D′
X
Q1,...,Qn+1∈D
Q
(ki)
i
=K
aK,(Qi)τ
 n+1
Y
j=1
⟨gj, uj,Qj⟩

,
D′ ⊂D,
satisfy
sup
D′⊂D
|UD′(g1, . . . , gn+1)| ≤A2
n+1
Y
j=1
∥gj∥Lpj(Rd;Xj),
gj ∈L∞
c (Rd; Xj), j = 1, . . . , n + 1,
then for each tuple fj ∈L∞
c (Xj), j = 1, . . . , n + 1, and η > 0 there exists an η-sparse collection
S = S(( fj), η) ⊂D such that
|⟨UD( f1, . . . , fn), fn+1⟩| ≲η (A1 + A1κ + A2)
X
Q∈S
|Q|
n+1
Y
j=1
⟨| fj|Xj⟩Q,
where κ = max km.
In the previous lemma the sparse collection is in the same grid where the dyadic
operator is deﬁned. The result can be updated to involve a universal sparse set, which
is explained in Remark 3.28. This is important when we move the sparse estimate from
DMOs to CZOs via the representation theorem, which involves a family of dyadic grids.
3.28. Remark. There exist dyadic grids Di, i = 1, . . . , 3d, with the following property, see
Lacey–Mena [36], [39], or [8] for a simple proof. Let gm ∈L1
loc, m = 1, . . . , n + 1, be


## Page 19


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
19
scalar-valued and let η1, η2 ∈(0, 1). Then for some i there exists an η2-sparse collection
U = U((gm), η2) ⊂Di, so that for all η1-sparse collections of cubes S we have
X
Q∈S
|Q|
n+1
Y
m=1
⟨|gm|⟩Q ≲η1,η2
X
Q∈U
|Q|
n+1
Y
m=1
⟨|gm|⟩Q.
3.29. Remark. In [8], it is noted that the sparse domination estimate for an n + 1-linear
form Λ on Rd, acting on scalar functions
|Λ( f1, . . . , fn+1)| ≲
X
Q∈S
|Q|
n+1
Y
j=1
⟨| fj|⟩Q,
is equivalent to the estimate in terms of the multilinear maximal operator M
|Λ( f1, . . . , fn+1)| ≲∥M( f1, . . . , fn+1)∥1,
M( f1, . . . , fn+1)(x) = sup
x∈Q
n+1
Y
j=1
⟨| fj|⟩Q.
Vector-valued versions of this principle may be formulated in a totally analogous way.
We have used this equivalence to state the sparse bounds in our main results; this is
particularly convenient as the formulation in terms of the multilinear maximal function
may be given without deﬁning what a sparse collection is.
Next, we discuss the well known fact that the sparse domination of an operator implies
boundedness in the full range: for more details and weighted corollaries see [8, 39] and
references therein.
Let X1, . . . , Xn+1 be Banach spaces, n ≥1. Assume that Λ is an (n + 1)-linear form
initially deﬁned on L∞
c (Rd) ⊗X1 × · · · × L∞
c (Rd) ⊗Xn+1 such that if fj ∈L∞
c (Rd) ⊗Xj, then
there exists a dyadic lattice D and a sparse collection S ⊂D so that
(3.30)
|Λ( f1, . . . , fn+1)| ≲
X
Q∈S
|Q|
n+1
Y
j=1
⟨| fj|Xj⟩Q.
This easily implies that if pj ∈(1, ∞) for j ∈Jn+1 are such that Pn+1
j=1 1/pj = 1 then Λ can be
extended to a bounded form Λ: Lp1(X1) × · · · × Lpn+1(Xn+1) →C. Indeed, just use Hölder’s
inequality and then Carleson embedding theorem in the right hand side of (3.30).
We estimate the adjoints Tj∗of Λ, which are deﬁned in the usual way based on the
functional as in (3.26). By symmetry it will suﬃce to tackle the case j = n + 1 and simply
write T in place of T(n+1)∗.
We use the so-called A∞extrapolation from Cruz-Uribe–Martell–Pérez [5]. Let A∞(Rd)
be the class of A∞weights in Rd, see [5] for a deﬁnition.
Suppose v ∈A∞(Rd) and
fj ∈L∞
c (Xj) for j ∈Jn. Taking fn+1(x) = ξ(x)v(x) for a suitably chosen ξ ∈L∞
c (Xn+1) there


## Page 20


20
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
holds that
ˆ
Rd |T( f1, . . . , fn)|X∗
n+1v ∼Λ( f1, . . . , fn+1) ≲
X
Q∈S
n
Y
j=1
⟨| fj|Xj⟩Qv(Q)
≤
X
Q∈S
D
Mn
D(| f1|X1, . . . , | fn|Xn)1/2Ev
Q
2
v(Q)
≲
ˆ
Rd Mn
D(| f1|X1, . . . , | fn|Xn)v,
where ⟨h⟩v
Q = v(Q)−1 ´
Q hv and Mn
D(g1, . . . , gn)≔supQ∈D
Qn
m=1⟨|gm|⟩Q1Q is the dyadic max-
imal function and in the last step we used the Carleson embedding theorem. Now, the
A∞extrapolation result, Theorem 2.1 in [5], gives that
ˆ
Rd |T( f1, . . . , fn)|p
X∗
n+1v ≲
ˆ
Rd Mn
D(| f1|X1, . . . , | fn|Xn)pv
for all p ∈(0, ∞) and v ∈A∞(Rd). Using this with v = 1 the boundedness of the maximal
function gives that
∥T( f1, . . . , fn)∥Lqn+1(X∗
n+1) ≲
n
Y
j=1
∥fj∥Lpj(Xj),
where pj ∈(1, ∞] are such that 1/qn+1≔Pn
j=1 1/pj > 0. Notice that the boundedness of
Mn
D follows from Hölder’s inequality and the boundedness of M1
D, since there holds that
Mn
D(g1, . . . , gn) ≤Qn
m=1 M1
D(gm). As is clear, multilinear weighted bounds also follow
from this argument and the corresponding results of Mn
D.
3.4. Proof of the main theorem. In this section we state and prove our main theorem
assuming the estimates for model operators from Section 4 and Section 5.
3.31. Theorem. Let n ≥1, T0 be an n-linear CZO with kernel K0 and {X1, . . . , Xn+1} be a UMD
Hölder tuple. The (n + 1)-linear form ΛT0 deﬁned in (3.22) can be extended to act on functions
fj ∈L∞
c (Xj), and given η ∈(0, 1) there exists an η-sparse collection of cubes S = S(( fm), η) so
that
|ΛT0( f1, . . . , fn+1)| ≲η
h
∥K0∥CZα + ∥T0∥WBP +
n+1
X
j=1
∥(T0)j∗(1, . . . , 1)∥BMO
i
×
X
Q∈S
|Q|
n+1
Y
j=1
⟨| fj|Xj⟩Q.
Consequently, we for instance have
∥T0( f1, . . . , fn)∥Lqn+1(X∗
n+1) ≲
n
Y
j=1
∥fj∥Lpj(Xj)
whenever pj ∈(1, ∞] are such that 1/qn+1≔Pn
j=1 1/pj > 0. See Section 3.3 for a full discussion
of the corollaries of the sparse estimate.


## Page 21


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
21
Proof. Let fj ∈L∞
c ⊗Xj for j ∈Jn+1 be of the form fj = PNj
a=1 fj,aej,a. Then, we have by the
dyadic representation (2.9) that
ΛT0( f1, . . . , fn+1)
= CT
X
a1,...,an+1
Eω
∞
X
k1,...,kn+1=0
X
u
2−
α max ki
2
⟨Uk
Dω,u( f1,a1, . . . , fn,an), fn+1,an+1⟩τ
 n+1
Y
j=1
ej,aj

= CTEω
∞
X
k1,...,kn+1=0
X
u
2−
α max ki
2
ΛUk
Dω,u( f1, . . . , fn+1).
(3.32)
In Section 4 and Section 5 it is shown that if U is a dyadic model operator then
(3.33)
|ΛU(g1, . . . , gn+1)| ≲
n+1
Y
j=1
∥gj∥Lpj(Xj)
holds for any pj ∈(1, ∞) and gj ∈L∞
c (Xj), j ∈Jn+1, such that Pn+1
j=1 1/pj = 1; if U is a shift,
then the estimate depends polynomially on the complexity. This implies that ΛT0 can be
extended to act on functions fj ∈L∞
c (Xj) and that (3.32) holds for such functions.
The estimate (3.33) implies via Lemma 3.27 and Remark 3.28 that if fj ∈L∞
c (Xj) for
j ∈Jn+1 then there exist a dyadic grid and an η-sparse collection S = S(( fj)) ⊂D so that
all the model operators appearing in (3.32) satisfy
|ΛUk
Dω,u( f1, . . . , fn+1)| ≲
X
Q∈S
|Q|
n+1
Y
j=1
⟨| fj|Xj⟩Q,
where the estimate depends polynomially on the complexity. This combined with (3.32)
ﬁnishes the proof.
□
In Section 6, we show that the UMD Hölder tuples enjoy a suitable maximal property
among tuples of spaces admitting Lp-bounded extensions of n-linear CZO operators and
dyadic shifts.
4. Boundedness of multilinear shifts in UMD H¨older tuples
This section is dedicated to the proof of the boundedness of multilinear shifts. Before
starting the main argument, we record a randomized bound for UMD Hölder tuples in
the following lemma.
4.1. Lemma. Let {X1, . . . , Xn+1} be a UMD Hölder tuple, n ≥2, and let K ∈Z+. For each
k = 1, . . . , K let ak be a scalar such that |ak| ≤1 and for each j ∈Jn assume that we are given
ej,k ∈Xj. Then we have

K
X
k=1
ak
n
Y
j=1
ej,k
Y(Xn+1) ≤
n
Y
j=1
∥(ej,k)K
k=1∥Rad(Xj).
Proof. Fix K, |ak| ≤1 and ej,k ∈Xj as in the assumptions. Let {εi
k}K
k=1, i ∈Jn−1, be collections
of independent random signs. We denote the expectation with respect to the random


## Page 22


22
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
variables {εi
k}K
k=1 by Ei, and write E = E1 · · · En−1. We have the identity
K
X
k=1
ak
n
Y
j=1
ej,k = E
K
X
k1,...,kn=1
ε1
k1ε1
k2ε2
k2ε2
k3 · · · εn−1
kn−1εn−1
kn ak1
n
Y
j=1
ej,kj
= E

K
X
k1=1
ε1
k1ak1e1,k1

K
X
k2=1
ε1
k2ε2
k2e2,k2

· · ·

K
X
kn=1
εn−1
kn en,kn

.
We can dominate this with
E




K
X
k1=1
ε1
k1ak1e1,k1




X1
 n−1
Y
i=2




K
X
ki=1
εi−1
ki εi
kiei,ki




Xi




K
X
kn=1
εn−1
kn en,kn




Xn,
which is further controlled by

E




K
X
k1=1
ε1
k1ak1e1,k1




2
X1
1/2
×
h
E
 n−1
Y
i=2




K
X
ki=1
εi−1
ki εi
kiei,ki




2
Xi




K
X
kn=1
εn−1
kn en,kn




2
Xn
i1/2
.
(4.2)
The ﬁrst factor is less than ∥(e1,k)K
k=1∥Rad(X1) by Kahane’s contraction principle. We now
consider the second factor. We see that the variables ε1
k appear only inside the norm X2,
and moreover there holds that
E1



K
X
k2=1
ε1
k2ε2
k2e2,k2




2
X2 = ∥(e2,k)K
k=1∥2
Rad(X2).
After using this identity, the variables ε1
k do not appear anymore, and the variables ε2
k
appear only inside the norm X3. Repeating the same reasoning, we deduce that the
second factor in (4.2) is equal to the product Qn
j=2 ∥(ej,k)K
k=1∥Rad(Xj).
□
Now, we turn to the actual proof of boundedness of shifts. We assume that n ≥1
and that {X1, . . . , Xn+1} is a UMD Hölder tuple. Let k = (k1, . . . , kn+1), 0 ≤ki ∈Z, and
let D be a dyadic lattice in Rd. Suppose Sk≔Sk
D is an n-linear dyadic shift as described
in Equation (2.7). We consider its related (n + 1)-linear form ΛSk which acts on locally
integrable functions fj: Rd →Xj by
(4.3)
ΛSk( f1, . . . , fn+1) =
X
K∈D
ΛK( f1, . . . , fn+1),
where
ΛK( f1, . . . , fn+1) =
X
Q1,...,Qn+1∈D
Q
(kj)
j
=K
aK,(Qj)j∈Jn+1τ
 n+1
Y
j=1
⟨fj,ehQj⟩

.
Here aK,(Qj)j∈Jn+1 is a scalar satisfying |aK,(Qj)j∈Jn+1| ≤Qn+1
j=1 |Qj|1/2|K|−n, and there exist two
indices j0, j1 ∈Jn+1, j0 , j1, so thatehQj0 = hQj0,ehQj1 = hQj1 andehQj = h0
Qj if j ∈Jn+1\{j0, j1}.


## Page 23


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
23
The sparse domination lemma 3.27 reduces the problem to the following theorem.
4.4. Theorem. Suppose pj ∈(1, ∞) for j ∈Jn+1 are such that Pn+1
j=1 1/pj = 1. The dyadic shift
form from (4.3) satisﬁes the estimate
|ΛSk( f1, . . . , fn+1)| ≲
n+1
Y
j=1
∥fj∥Lpj(Xj)
for fj ∈L∞
c (Xj), where the estimate depends polynomially on κ≔maxj kj.
Proof. Let fj ∈L∞
c (Xj) for j ∈Jn and consider (4.3). Recall the lattices Di,κ from (2.4),
where κ≔maxj kj. We ﬁrst divide the sum over the cubes K ∈D as Pκ
i=0
P
K∈Di,κ. We ﬁx
one i and consider the corresponding term.
Let e
J be the set of those indices such that the corresponding Haar functions are non-
cancellative, that is, ehQj = h0
Qj. Suppose j ∈e
J is such that kj > 0. We use that fact that
⟨fj,ehQj⟩= ⟨E
kj
K fj, h0
Qj⟩and split
(4.5)
E
kj
K fj =
kj−1
X
lj=0
∆
lj
K fj + EK fj.
There holds that
(4.6)
⟨EK fj, h0
Qj⟩= ⟨fj, h0
K⟩⟨h0
K, h0
Qj⟩
and
(4.7)
⟨∆
lj
K fj, h0
Qj⟩= ⟨fj, h
Q
(kj−lj)
j
⟩⟨h
Q
(kj−lj)
j
, h0
Qj⟩,
where as usual we suppressed the summation over the diﬀerent Haar functions.
We use (4.5) to split P
K∈Di,κ ΛK( f1, . . . , fn+1) into at most (1 + κ)n−1 terms of the form
(4.8)
X
K∈Di,κ
X
Q1,...,Qn+1∈D
Q
(kj)
j
=K
aK,(Qj)j∈Jn+1τ
 n+1
Y
j=1
⟨P
lj
K,j fj,ehQj⟩

,
where lj ∈Z, 0 ≤lj ≤kj. For j ∈Jn+1 \ e
J we have that P
lj
K,j is the identity operator, and
below we write lj = kj. If j ∈e
J and lj > 0 then P
lj
K,j = ∆
lj
K, and if j ∈e
J and lj = 0 then P0
K,j
is either EK or ∆K (but does not change with K). We write
X
K∈Di,κ
X
Q1,...,Qn+1∈D
Q
(kj)
j
=K
=
X
K∈Di,κ
X
L1,...,Ln+1∈D
L
(lj)
j
=K
X
Q1,...,Qn+1∈D
Q
(kj−lj)
j
=Lj
and notice that by (4.6) and (4.7) we always have that
⟨P
lj
K,j fj,ehQj⟩= ⟨fj, h′
Lj⟩γ(Qj, Lj),


## Page 24


24
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
where h′
Lj ∈{h0
Lj, hLj} and
|γ(Qj, Lj)| =
|Qj|1/2
|Lj|1/2 .
We can now write (4.8) further as
(4.9)
X
K∈Di,κ
X
L1,...,Ln+1∈D
L
(lj)
j
=K
bK,(Lj)j∈Jn+1τ
 n+1
Y
j=1
⟨fj, h′
Lj⟩

,
where
bK,(Lj)j∈Jn+1 =
X
Q1,...,Qn+1∈D
Q
(kj−lj)
j
=Lj
aK,(Qj)j∈Jn+1
n+1
Y
j=1
γ(Qj, Lj).
There exists J ⊂Jn+1 with #J ≥2 so that h′
Lj = hLj for j ∈J and if j ∈Jn+1 \ J then
h′
Lj = h0
Lj and lj = 0. Also, we have the normalization |bK,(Lj)j∈Jn+1| ≤Qn+1
j=1 |Lj|1/2|K|−n.
We have reduced to considering the new shift type operator (4.9). The coeﬃcients
satisfy the usual normalization of shifts, but the number #J of indices with cancellative
Haar functions may be bigger than 2. What is essential is that the complexity related
to the non-cancellative indices is zero – that is, if j ∈Jn+1 \ J then lj = 0. We now
start estimating (4.9). Also, the separation of scales, K ∈Di,κ, will allow us to use the
decoupling estimate (2.5).
Case 1. Assume that J = Jn+1. Let qn+1 ∈(1, ∞) be the exponent determined by
1/qn+1 = Pn
j=1 1/pj. We need to estimate




X
K∈Di,κ
X
L1,...,Ln+1∈D
L
(lj)
j
=K
bK,(Lj)j∈Jn+1
n
Y
j=1
⟨fj, hLj⟩hLn+1




Lqn+1(Y(Xn+1))
∼

E
ˆ
Rd
ˆ
V

X
K∈Di,κ
εK1K(x)
X
L1,...,Ln+1∈D
L
(lj)
j
=K
bK,(Lj)j∈Jn+1
×
n
Y
j=1
⟨fj, hLj⟩hLn+1(yK)

qn+1
Y(Xn+1) dν(y) dx
1/qn+1,
where we used the decoupling estimate.
Notice that since by assumption Xn+1 =
Y(X1, . . . , Xn), there holds also that Y(Xn+1) = Y(Y(X1, . . . , Xn)), so we could also use


## Page 25


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
25
the norm | · |Y(Y(X1,...,Xn)) instead. Write
X
L1,...,Ln+1∈D
L
(lj)
j
=K
bK,(Lj)j∈Jn+1
n
Y
j=1
⟨fj, hLj⟩hLn+1(yK)
=
1
|K|n
ˆ
Kn bK(yK, z)
n
Y
j=1
∆
lj
K fj(zj) dz =
ˆ
Vn bK(yK, zK)
n
Y
j=1
∆
lj
K fj(zj,K) dνn(z),
where νn is the product measure ν × · · · × ν on the product space Vn and
bK(yK, zK) = |K|n
X
L1,...,Ln+1∈D
L
(lj)
j
=K
bK,(Lj)j∈Jn+1
n
Y
j=1
hLj(zj,K)hLn+1(yK).
We can now continue the estimate by using Hölder’s inequality related to the integral
´
Vn. We end up with
(4.10)

E
ˆ
Rd
ˆ
V
ˆ
Vn

X
K∈Di,κ
εK1K(x)bK(yK, zK)
n
Y
j=1
∆
lj
K fj(zj,K)

qn+1
Y(Xn+1) dνn(z) dν(y) dx
1/qn+1.
Suppose n ≥2. Notice that |bK(yK, zK)| ≤1 and use Lemma 4.1 to get that

X
K∈Di,κ
εK1K(x)bK(yK, zK)
n
Y
j=1
∆
lj
K fj(zj,K)
Y(Xn+1)
≤
n
Y
j=1
∥(1K(x)∆
lj
K fj(zj,K))K∈Di,κ∥Rad(Xj).
Using ﬁrst Hölder’s inequality, then Kahane-Khintchine inequality and ﬁnally the de-
coupling estimate, we conclude that
(4.10) ≲
n
Y
j=1
 ˆ
Rd
ˆ
V
∥(1K(x)∆
lj
K fj(zK))K∈Di,κ∥
pj
Rad(Xj) dν(z) dx
1/pj
∼
n
Y
j=1

E
ˆ
Rd
ˆ
V

X
K∈Di,κ
εK1K(x)∆
lj
K fj(zK)

pj
Xj dν(z) dx
1/pj
≲
n
Y
j=1
∥fj∥Lpj(Xj).
Suppose then n = 1. In this case we have that q2 = p1 and Y(X2) = X1. We use Kahane-
Khintchine inequality to move the expectation inside of the exponent p1. Then, we use
Kahane’s contraction principle and move the expectation out again. This gives that
(4.10) ≲

E
ˆ
Rd
ˆ
V

X
K∈Di,κ
εK1K(x)∆l1
K f1(zK)

p1
X1 dν(z) dx
1/p1 ≲∥f1∥Lp1(X1),


## Page 26


26
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
where the last step used the decoupling estimate. Linear estimates for shifts have ap-
peared e.g. in [19, 29].
Case 2. Assume now that J ⊊Jn+1. Since #J ≥2, this implies that n ≥2. Let
j0 ∈Jn+1 \ J be an index such that j0 + 1 ∈J; by (n + 1) + 1 we mean 1. Let σ ∈Σ(n + 1)
be the cyclic permutation such that σ(n) = j0. Then σ(n + 1) ∈J. If ej ∈Xj for j ∈Jn+1
then from Remark 3.15 one sees that Qn
j=1 ej ∈Y(Xn+1) and therefore the cyclic invariance
of the trace (3.8) gives that τ(e1 · · · en+1) = τ(en+1e1 · · · en). Repeating this we have that (4.9)
is equal to
X
K∈Di,κ
X
L1,...,Ln+1∈D
L
(lj)
j
=K
bK,(Lj)j∈Jn+1τ
 n+1
Y
j=1
⟨fσ(j), h′
Lσ(j)⟩

.
Having made this important observation, we may now assume, for small notational
convenience, that j0 = n and σ = id. Under this assumption n ∈Jn+1 \ J, which implies
that ln = 0. Thus, the coeﬃcient bK,(Lj)j∈Jn+1 depends only on the cubes L1, . . . , Ln−1, Ln+1
and K. Below we will write the coeﬃcient as bK,(Lj).
We need to estimate




X
K∈Di,κ
X
L1,...,Ln−1,Ln+1∈D
L
(lj)
j
=K
bK,(Lj)
n−1
Y
j=1
⟨fj, h′
Lj⟩⟨fn⟩K|K|1/2hLn+1




Lqn+1(Y(Xn+1))
∼

E
ˆ
Rd
ˆ
V

X
K∈Di,κ
εK1K(x)⟨ϕK,y⟩K

qn+1
Y(Xn+1) dν(y) dx
1/qn+1,
where we used the decoupling estimate, and for K ∈Di,κ and y ∈V we deﬁned the
function ϕK,y : Rd →Y(Xn+1) by setting ϕK,y(x) to equal
|K|1/2
X
L1,...,Ln−1,Ln+1∈D
L
(lj)
j
=K
bK,(Lj)
n−1
Y
j=1
⟨fj, h′
Lj⟩fn(x)hLn+1(yK).
After using Stein’s inequality (2.3) with respect to x ∈Rd with ﬁxed y ∈V we are left
with
(4.11)

E
ˆ
Rd
ˆ
V

X
K∈Di,κ
εK1K(x)ϕK,y(x)

qn+1
Y(Xn+1) dν(y) dx
1/qn+1.
Recall that n ≥2 in Case 2. From Remark 3.15 we can deduce that if en ∈Xn and
en+1 ∈Xn+1, then enen+1 ∈Y(X1, . . . , Xn−1) and |enen+1|Y(X1,...,Xn−1) ≤|en|Xn|en+1|Xn+1. Also,
since {X1, . . . , Xn−1, Y(X1, . . . , Xn−1)} is a UMD Hölder tuple, we see from Remark 3.15
again that if ej ∈Xj for j ∈Jn−1, then Qn−1
j=1 ej ∈Y(Y(X1, . . . , Xn−1)). Suppose now that
ej,k ∈Xj for j ∈Jn−1, k = 1, . . . , K, and en ∈Xn. Then the above consideration implies that
the key inequality
(4.12)

K
X
k=1
n−1
Y
j=1
ej,ken
Y(Xn+1) ≤

K
X
k=1
n−1
Y
j=1
ej,k
Y(Y(X1,...,Xn−1))|en|Xn


## Page 27


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
27
holds. Write Z≔Y(Y(X1, . . . , Xn−1)) for the moment. Using this in (4.11) and then Hölder’s
inequality we have that (4.11) is dominated by ∥fn∥Lpn(Xn) multiplied by

E
ˆ
Rd
ˆ
V

X
K∈Di,κ
εK1K(x)
X
L1,...,Ln−1,Ln+1∈D
L
(lj)
j
=K
ebK,(Lj)
n−1
Y
j=1
⟨fj, h′
Lj⟩hLn+1(yK)

p(Jn−1)
Z
dν(y) dx

1
p(Jn−1)
∼




X
K∈Di,κ
X
L1,...,Ln−1,Ln+1∈D
L
(lj)
j
=K
ebK,(Lj)
n−1
Y
j=1
⟨fj, h′
Lj⟩hLn+1




Lp(Jn−1)(Z),
where we deﬁned 1/p(Jn−1)≔Pn−1
j=1 1/pj, ebK,(Lj)≔|K|1/2bK,(Lj) and used the decoupling in-
equality. Notice that
|ebK,(Lj)| ≤
Qn−1
j=1 |Lj|1/2|Ln+1|1/2
|K|n−1
.
We see that we have reduced the estimate to the boundedness of an (n −1)-linear shift
type operator as in (4.9). Now, we have two possibilities. If all the Haar functions h′
Lj
for j ∈Jn−1 are cancellative then we are in a position to apply Case 1 from above to
ﬁnish the estimate. If some of them is non-cancellative, then we dualize with a function
g ∈Lp(Jn−1)′(Y(X1, . . . , Xn−1)). This leads us to a corresponding situation as the beginning
of Case 2 above but now the form is n-linear and the underlying UMD Hölder n-tuple is
{X1, . . . , Xn−1, Y(X1, . . . , Xn−1)}. We see that we can repeat the argument in Case 2 until we
can apply Case 1. This ﬁnishes the proof.
□
4.13. Remark. We discuss why Theorem 1.1 works without any UMD Hölder tuple as-
sumptions on the spaces X1, X2 and Y3, and why we can’t allow more UMD spaces in
Theorem 1.1. The key point is that for e1,k ∈X1 and e2 ∈X2 the estimate
(4.14)

K
X
k=1
e1,ke2
Y3 ≤

K
X
k=1
e1,k
X1|e2|X2,
which corresponds to (4.12), holds without any further assumptions on the spaces. Using
this kind of estimates one can prove Theorem 1.1 with similar techniques as in the proof
of Theorem 4.4.
Suppose then we have UMD spaces X1, . . . , Xn and Yn+1, where n ≥3, and we have
a product X1 × · · · × Xn →Yn+1 – a bounded n-linear operator. Of course, an estimate
corresponding to (4.14) holds, namely

K
X
k=1
e1,k
n
Y
j=2
ej
Yn+1 ≤

K
X
k=1
e1,k
X1
n
Y
j=2
|ej|Xj.
However, in the above proof for shifts, when we use Stein’s inequality, we need to reduce
the linearity before we can use it again. That is why we need the product structure of
UMD Hölder tuples rather than just a product X1 × · · · × Xn →Yn+1 on the top level.


## Page 28


28
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
5. Boundedness of multilinear paraproducts in UMD H¨older tuples
In this section we prove the boundedness of multilinear paraproducts. Let us ﬁrst
recall a result for paraproducts acting on UMD-valued functions. If X is a UMD space,
D is a dyadic lattice and {aQ}Q∈D is a collection of scalars satisfying the BMO condition
(2.8), then
(5.1)




X
Q∈D
aQ⟨f⟩QhQ




Lp(X) ≲∥f∥Lp(X),
where p ∈(1, ∞). This result goes back to Bourgain, see Figiel–Wojtaszczyk [14]. Another
nice proof is obtained by adapting the argument of Hänninen–Hytönen [19], who consider
paraproducts with operator coeﬃcients.
Let n ≥1 and let {X1, . . . , Xn+1} be a UMD Hölder tuple. Suppose that D is a dyadic
lattice and that π≔πD is a paraproduct as described in Section 2.4. Let j0 ∈Jn+1 be the
index related to the cancellative Haar functions of π and let σ ∈Σ(n + 1) be the cyclic
permutation such that σ(n + 1) = j0. We consider the (n + 1)-linear form Λπ acting on
functions fj ∈L∞
c (Xj) by
(5.2)
Λπ( f1, . . . , fn+1) =
X
Q∈D
aQτ


h
n
Y
j=1
⟨fσ(j)⟩Q
i
⟨fσ(n+1), hQ⟩

,
where the scalars {aQ}Q∈D satisfy the BMO condition (2.8). The following theorem com-
bined with Lemma 3.27 proves the desired estimate.
5.3. Theorem. Suppose that pj ∈(1, ∞) for j ∈Jn+1 are such that Pn+1
j=1 1/pj = 1. If fj ∈L∞
c (Xj)
for j ∈Jn+1 then the form Λπ from (5.2) satisﬁes the estimate
|Λπ( f1, . . . , fn+1)| ≲
n+1
Y
j=1
∥fj∥Lpj(Xj).
Proof. For m ∈Jn we let p(Jm) be the exponent deﬁned by 1/p(Jm) = Pm
j=1 1/pj. For
convenience of notation we may assume that j0 = n + 1, so that σ = id. In this case we
need to estimate the term




X
Q∈D
aQ
n
Y
j=1
⟨fj⟩QhQ




Lp(Jn)(Y(Xn+1)).
The case n = 1 is the known estimate (5.1). Therefore, we assume that n ≥2.
Applying the UMD property of Y(Xn+1) we are led to
(5.4)

E
ˆ
Rd

X
Q∈D
εQaQ
n
Y
j=1
⟨fj⟩Q|hQ(x)|

p(Jn)
Y(Xn+1) dx
1/p(Jn)
,
where to pass from hQ to |hQ| we used that for ﬁxed x ∈Rd the families {εQhQ(x)} and
{εQ|hQ(x)|} are identically distributed. Since |hQ| = 1Q/|Q|1/2, we can use Stein’s inequality
to have that
(5.4) ≲

E
ˆ
Rd

X
Q∈D
εQaQ
n−1
Y
j=1
⟨fj⟩Q fn(x)|hQ(x)|

p(Jn)
Y(Xn+1) dx
1/p(Jn)
.


## Page 29


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
29
Now, we use the same inequality we used in the shift proof, Equation (4.12), and
Hölder’s inequality to have that the last term is less than ∥fn∥Lpn(Xn) multiplied by

E
ˆ
Rd

X
Q∈D
εQaQ
n−1
Y
j=1
⟨fj⟩Q|hQ(x)|

p(Jn−1)
Y(Y(X1,...,Xn−1)) dx
1/p(Jn−1)
.
Since {X1, . . . , Xn−1, Y(X1, . . . , Xn−1} is a UMD Hölder n- tuple, we see that we have reduced
to a situation as in (5.4) but now the degree of linearity is n−1. We can repeat the argument
until we end up with a linear operator, and then we apply (5.1).
□
6. Maximality of UMD H¨older tuples
In this brief section, we show that UMD Hölder tuples are in a suitable sense maximal
for Lp-boundedness of extensions of n-linear CZO operators and dyadic shifts via an
associative product as in Section 3. The precise statement is in Proposition 6.3 below.
Therefore, we ﬁx an associative algebra A and a functional τ as in Section 3. We begin
with a lemma.
6.1. Lemma. Let (X1, . . . , Xn) be a n-tuple of admissible spaces. If Xn+1 is an admissible space
such that for all (n + 1)-linear shift forms (3.23) and functions fj ∈C1(Rd) ⊗Xj, j = 1, . . . , n + 1
(6.2)
ΛUk
Dω,u( f1, . . . , fn, fn+1)
 ≲


n+1
Y
ℓ=1
∥fj∥Ln+1(Rd;Xj)


with implicit constant depending possibly on the complexity k, then (3.5) holds for m = n, and in
particular Xn+1 ֒→Y(X1, . . . , Xn).
Proof. Test (6.2) on a suitable trivial shift and appeal to Lemma 3.4.
□
To make our maximality claim precise, we need an additional deﬁnition. We say that
the tuple {X1, . . . , Xn+1} of admissible spaces is an n-linear shift extension if (6.2) holds for all
(n+1)-linear shift forms (3.23). If in addition, whenever Z is an admissible space such that
for some j0 ∈Jn+1 the tuple {X1, . . . Xj0−1, Z, Xj0+1, . . . Xn+1} is an n-linear shift extension,
it must be Z ֒→Xj0, we say that {X1, . . . , Xn+1} is a maximal n-linear shift extension.
6.3. Proposition. Let {X1, . . . , Xn+1} be a UMD Hölder tuple. Then
• {X1, . . . , Xn+1} is a maximal n-linear shift extension;
• whenever 1 ≤k ≤n −1 and #J = k, {Xj : j ∈J} ∪{Y({Xj : j ∈J})} is a maximal
k-linear shift extension.
Proof. Theorem 4.4 shows that if {X1, . . . , Xn+1} is a UMD Hölder tuple, then it is an n-
linear shift extension. As Xj0 = Y({Xj : j ∈J0}) by deﬁnition of UMD Hölder tuple, we
learn from Lemma 6.1 that {X1, . . . , Xn+1} is in fact a maximal n-linear shift extension. This
proves the ﬁrst point.
By the inductive deﬁnition of UMD Hölder tuple, for each 1 ≤k ≤n −1 and #J = k,
{Xj : j ∈J} ∪{Y({Xj : j ∈J})} is a UMD Hölder tuple. Then this tuple must be a maximal
k-linear shift extension because of the ﬁrst point. The second point is also proved.
□


## Page 30


30
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
Appendix A. Iterated mixed-norm non-commutative Lp spaces
Let M be a von Neumann algebra equipped with a n.s.f. trace as described in Example
3.18. Recall in particular that A = L0(M) is an associative ∗-algebra endowed with a
compatible complete metrizable topology, induced by the metric dA of convergence in
measure. For an integer S ≥1, let (Ms, µs), s = 1, . . . , S, be σ-ﬁnite measure spaces and
(ΩS, ωS) the product measure space
ΩS =
S
Y
s=1
Ms,
ωS =
S
Y
s=1
µs.
Let A0,S be the vector space of simple functions f : ΩS →A, namely
f(t) =
J
X
j=1
Aj1Ej(t),
t = (t1, . . . , ts) ∈ΩS,
with Aj ∈A, Ej ⊂ΩS with ωS(Ej) < ∞. Then A0,S is an associative algebra with respect to
the pointwise product: for f, g ∈A0,S, the function f g deﬁned by ( f g)(t) = f(t)g(t), where
the latter is the strong product in A, belongs to A0,S. We denote by
AS≔closure of A0 w.r.t. sequential dA-pointwise convergence
namely, f ∈AS if there exists a sequence fn ∈A0,S such that
lim
n dA( f(t), fn(t)) = 0
a.e. t ∈ΩS.
Then AS, the class of strongly measurable A-valued functions on ΩS, is an associative
algebra with respect to the same product. Furthermore, AS is complete with respect to
the topology of convergence in measure, namely fn →f if for all ε > 0
lim
n µ  t ∈ΩS : dA( f(t), fn(t)) > ε	 = 0,
and the product operation is continuous. Note that the latter topology is also metrizable,
proceeding in an analogous way to [24, Proposition A.2.4].
Recall that M is equipped with the n.s.f. trace τ, which is a linear bounded functional
on L1(M). Then the functional
τS( f) ≔
ˆ
ΩS
τ( f(t)) dωS(t)
is linear and bounded on the Bochner space L1(ΩS, ωS; L1(M)), which is a subspace of AS.
With this deﬁnition, AS is endowed with the trace τS. Under these assumptions, we have
the following proposition.
A.1. Proposition. For a Hölder tuple {p0
j : 1 ≤j ≤m} as in (3.1), let
X0
j = Lp0
j (M).
Let {ps
j : 1 ≤j ≤m} be further Hölder tuples of exponents, for 1 ≤s ≤S. Then the Banach
subspaces of As
(A.2)
Xs
j = Lps
j(Ms, µs; Xs−1
j
),
s = 1, . . . , S,


## Page 31


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
31
are a UMD Hölder m-tuple.
Before the proof proper, we need to set some notation, and develop suitable auxiliary
lemmata. For 1 ≤k ≤m −1, J = {j1 < j2 < · · · < jk} ⊂Jm, and 0 ≤s ≤S we write
1
qs
J
=
k
X
u=1
1
ps
ju
,
1
ps
J
= 1 −1
qs
J
.
It will be convenient to introduce the auxiliary mixed norm spaces
E1
j = Lp1
j (M1, µ1),
Es
j = Lps
j(Ms, µs; Es−1
j
),
s = 2, . . . , S,
for j = 1, . . . , m and similarly
E0
J = C,
Es
J = Lqs
J(Ms, µs; Es−1
J ),
s = 1, . . . , S.
In general we write S(X) for the unit sphere in the Banach space X.
A.3. Lemma. Let J = {ju : 1 ≤u ≤k}. There exists maps Bs
u : S(Es
J) →S(Es
ju) such that
f =
k
Y
u=1
Bs
u( f)
∀f ∈S(Es
J)
and
∥fn −f∥Es
J →0, ∥fn(ts) −f(ts)∥Es−1
J →0 a.e. ts ∈Ms =⇒
∥Bs
u( f) −Bs
u( fn)∥Es
ju →0, ∥Bs
u( fn)(ts) −Bs
u( fn)(ts)∥Es−1
ju →0 a.e. ts ∈Ms,
1 ≤u ≤k.
(A.4)
Proof. We deal with the case ju = u, u = 1, . . . , k which is generic. We prove the statement
by induction on s. If s ≥2, assume inductively that maps Bs−1
u
as in the statement have
been constructed; for the base case s = 1, we run the argument below with B0
u the identity
map. In both cases, we need to deﬁne Bs
u : S(Es
J) →S(Es
u). We use that each f ∈S(Es
J) is
Es−1
J -valued. So for each ts ∈Ms, write
f(ts) = | f(ts)|Es−1
J g(ts) =
k
Y
u=1

| f(ts)|
qs
J
psu
Es−1
J
gu(ts)

≕
k
Y
u=1
Bs
u( f)(ts)
where g is S(Es−1
J )-valued, so that each gu = Bs−1
u (g) is S(Es−1
u )-valued. Notice that each
fu = Bs
u( f) is (strongly) µs-measurable with values in Es−1
u : in fact | f(·)|Es−1
J is µs-measurable
and each gu is µs-measurable, as Bs−1
u
is (norm) continuous from Es−1
J
→Es−1
u
and g is
µs-measurable with values in Es−1
J
. A direct calculation reveals that
∥fu∥Es
u = 1,
1 ≤u ≤k.
It remains to show that the thus deﬁned maps Bs
u are continuous in the sense of (A.4)
by assuming the same properties hold for the maps Bs−1
u . Let fn, f be as in the ﬁrst line


## Page 32


32
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
of (A.4) and write fn(ts) = | fn(ts)|Es−1
J gn(ts). We ﬁrst show the pointwise convergence: for
each we have
∥Bs
u( f)(ts) −Bs
u( fn)(ts)∥Es−1
u
≤∥f(ts)∥Es−1
J ∥Bs−1
u (g(ts)) −Bs−1
u (gn(ts))∥Es−1
u
+
∥Bs−1
u (gn(ts))∥Es−1
u
∥f(ts)∥
qs
J
psu
Es−1
J
−∥fn(ts)∥
qs
J
psu
Es−1
J

Relying on the norm continuity of Bs−1
u
we obtain that both summands in the previous
display converge to zero for each ts such that ∥fn(ts)∥Es−1
J →∥f(ts)∥Es−1
J , ∥gn(ts)−g(ts)∥Es−1
J →
0; this is a set of full µs measure, so that this part of the proof is complete. We come to the
norm continuity in (A.4). We have
∥Bs
u( f) −Bs
u( fn)∥ps
u
Es
u ≲
ˆ
Ms
| f(ts)|
qs
J
Es−1
J
|Bs−1
u (g(ts)) −Bs−1
u (gn(ts))|ps
u
Es−1
u
dµs(ts)
+
ˆ
Ms

| f(ts)|
qs
J
psu
Es−1
J
−| fn(ts)|
qs
J
psu
Es−1
J

ps
u
|Bs−1
u (gn(ts))|ps
u
Es−1
u
dµs(ts)
The ﬁrst integrand converges to zero pointwise a.e. and is dominated by | f(ts)|
qs
J
Es−1
J
, so the
integral converges to zero by dominated convergence. The second integral is equal to
∥F −Fn∥ps
u
Lpsu(Ms,µs),
F(ts) = | f(ts)|
qs
J
psu
Es−1
J
,
Fn(ts) = | fn(ts)|
qs
J
psu
Es−1
J
.
Notice that ∥F∥ps
u = ∥f∥
qs
J/ps
u
Es
J
, ∥Fn∥pu = ∥fn∥
qs
J/ps
u
Es
J
.
As Fn →F pointwise, Fn, F ∈Lps
u(Ms, µs)
and ∥Fn∥ps
u →∥F∥ps
u, then ∥F −Fn∥ps
u converges to zero by a well-known variation of the
proof of the Lp dominated convergence theorem.
□
A.5. Lemma. Let 2
X0
J = Lq0
J(M),
X0
J,+ = Lq0
J(M)+,
Xs
J = Lqs
J(Ms, µs; Xs−1
J ),
Xs
J,+ = Lqs
J(Ms, µs; Xs−1
J,+),
s = 1, . . . , S.
Let f ∈Xs
J,+ be a simple function with ∥f∥Xs
J = 1. Then there exist fu ∈Xs
ju,+, u = 1, . . . , k with
f =
k
Y
u=1
fu,
∥fu∥XS
ju = 1.
Proof. Again we deal with the generic case ju = u, u = 1, . . . , k. First of all, we make a
remark about the case s = 0. Fix A ∈X0
J,+ with ∥A∥X0
J = 1. Using the Borel functional
calculus for positive closed densely deﬁned operators to deﬁne Aθ for θ > 0
(A.6)
A =
k
Y
u=1
Bu(A),
Bu(A) = A
q0
J
p0u ,
u = 1, . . . , k.
2Recall that Lq0
J(M)+ denotes the positive cone of Lq0
J (M), namely the positive operators in Lq0
J(M).


## Page 33


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
33
Trivially
∥Bu(A)∥X0
u = ∥A∥
q0
J
p0u
X0
J
= 1,
u = 1, . . . , k.
We now prove the main statement. Let f ∈Xs
J,+ be a simple function with ∥f∥Xs
J = 1. We
factor
f(t) = F(t)A(t),
F(t) = | f(t)|X0
J ,
t ∈Ωs.
Notice that F ∈Es
J of unit norm, so that using Lemma A.3
F =
k
Y
u=1
Bs
u(F),
∥Bs
u(F)∥Es
u = 1,
and we may write, also using (A.6)
f =
k
Y
u=1
fu,
fu(t) = Bs
u(F)(t)Bu(A(t)),
Notice that each fu is strongly measurable as Bu(A(·)) is a simple X0
u,+-valued function
and Bs
u(F) is a measurable function in Es
u. Also as |Bu(A(t))|X0
u = 1 for all t ∈Ωs
∥fu∥Xs
u = ∥Bs
u(F)∥Es
u = 1,
which completes the proof of the claim.
□
We turn to the proof of the proposition. Namely we need to show that the tuple Xs
j
from (A.2) is a UMD Hölder tuple for each s = 1, . . . , S. In proving this, by virtue of
the case s = 0 being already established in Example 3.18 we may argue inductively and
assume the claim has been proved in the cases of 0, . . . , s −1.
Clearly each Xs
j is a subspace of As. Denoting by qs
j, s = 0, . . . , S the conjugate exponent
of ps
j, it is convenient to deﬁne the spaces
Y0
j = Lq0
j (M),
Ys
j = Lqs
j(Ms, µs; Ys−1
j
),
s = 1, . . . , S.
which are Banach subspaces of As. Further, as each Xs
j is a reﬂexive Banach space and
enjoys the Radon-Nikodým property [24, Theorem 1.3.21], an inductive argument yields
the Riesz representation theorem (cf. [24, Theorem 1.3.10]) then yields that

Xs
j
∗= Ys
j,
1 ≤j ≤m
through the identiﬁcation
λ ∈(Xs
j)∗7→gλ ∈Ys
j
λ( f) = τs(gλ f),
f ∈Xs
j.
We have in particular shown that each Xs
j is an admissible space for the algebra As with
trace τs and Y(Xs
j) = Ys
j .
We verify that {Xs
j : j ∈Jm} is a UMD Hölder tuple by induction on m. The case m = 2
is actually immediate by virtue of the observation and the well known fact that each
Xs
j, Ys
j is a UMD space.


## Page 34


34
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
To obtain the inductive step, we ﬁx m ≥3 and verify the following equality. For each
1 ≤k ≤m −1, J = {j1 < j2 < · · · < jk} ⊂Jm, there holds
(A.7)
Y({Xs
j : j ∈J}) is isometrically isomorphic to

Xs
J
∗,
where we refer to the spaces deﬁned in Lemma A.5. More explicitly, denoting
Y0
J = Lp0
J(M),
Ys
J = Lps
J(Ms, µs; Ys−1
J ),
s = 1, . . . , S,
we have Y({Xs
j : j ∈J}) = Ys
J =

Xs
J
∗.
Property P1 then corresponds to this equality in the cases k = m−1. Verifying property
P2 amounts to checking that when k < m−1, the tuple {Xs
j : j ∈J}∪{Ys
J} is a UMD Hölder
(k + 1)-tuple. As k < m −1, {Xs
j : j ∈J} ∪{Ys
J} is a UMD Hölder (k + 1)-tuple and the
exponents {ps
j : j ∈J, ps(J)} are a Hölder tuple, this check is made by a straightforward
appeal to the induction assumption.
We are left with proving (A.7). To do this we will deﬁne a linear surjective isometry
Φ : Y({Xs
j : j ∈J}) →Ys
J. First of all note that
(A.8)
∥g∥Y({Xs
j:j∈J}) ≤∥g∥
L
ps
J (Ms,µs;Ys−1
J ) = ∥g∥Ys
J
descends immediately from Hölder’s inequality in Lp(Ms, µs)-spaces and Lemma 3.4
applied to the UMD Hölder tuple Xs−1
j1 , Xs−1
j2 , . . . , Xs−1
jk . We will use this below.
Fix then g ∈Y({Xs
j : j ∈J}). We claim that if f is a simple X0
J,+-valued function on Ωs
with ∥f∥Xs
J = 1, then
(A.9)
|τs(gf)| ≤∥g∥Y({Xs
j:j∈J}).
Indeed, applying Lemma 3.4 we obtain
τs(gf)
 =

τs

g
k
Y
u=1
fu



≤∥g∥Y({Xs
j:j∈J})
k
Y
u=1
∥fu∥Xs
ju,
∥fu∥Xs
ju = 1,
u = 1, . . . , k,
which is (A.9). As Xs
J is the Xs
J-norm closure of the linear span of simple X0
J,+-valued
function on Ωs, the linear bounded functional f 7→τs(gf) extends uniquely to an element
Φ(g) of (Xs
J)∗≡Ys
J with
∥Φ(g)∥Ys
J ≤∥g∥Y({Xs
j:j∈J}).
It is easy to see that the map Φ : Y({Xs
j : j ∈J}) →Ys
J is linear. From (A.8) we gather
that if g ∈Ys
J then Φ(g) is well-deﬁned. In this case the linear bounded functionals
g 7→τs(gf) and Φ(g) coincide on a dense set, it must be Φ(g) = g. So Φ is obviously
surjective. Furthermore using (A.8) again we obtain
∥Φ(g)∥Ys
J ≥∥Φ(g)∥Y({Xs
j:j∈J}) = ∥g∥Y({Xs
j:j∈J}) ≥∥Φ(g)∥Ys
J
whence equality must hold throughout. So Φ is a linear isometric isomorphism and the
proof of (A.7) is complete.


## Page 35


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
35
References
[1] Jean Bourgain, Some remarks on Banach spaces in which martingale diﬀerence sequences are unconditional,
Ark. Mat. 21 (1983), no. 2, 163–168. MR 727340 1, 3
[2] Donald L. Burkholder, A geometric condition that implies the existence of certain singular integrals of Banach-
space-valued functions, Conference on harmonic analysis in honor of Antoni Zygmund, Vol. I, II (Chicago,
Ill., 1981), Wadsworth Math. Ser., Wadsworth, Belmont, CA, 1983, pp. 270–286. MR 730072 1
[3] Alejandro J. Castro and Tuomas P. Hytönen, Bounds for partial derivatives: necessity of UMD and sharp
constants, Math. Z. 282 (2016), no. 3-4, 635–650. MR 3473635 2
[4] Ronald R. Coifman and Yves Meyer, Nonlinear harmonic analysis, operator theory and P.D.E, Beijing lectures
in harmonic analysis (Beijing, 1984), Ann. of Math. Stud., vol. 112, Princeton Univ. Press, Princeton, NJ,
1986, pp. 3–45. MR 864370 2
[5] David Cruz-Uribe, José María Martell, and Carlos Pérez, Extrapolation from A∞weights and applications,
J. Funct. Anal. 213 (2004), no. 2, 412–439. MR 2078632 19, 20
[6] Amalia Culiuc, Francesco Di Plinio, and Yumeng Ou, Domination of multilinear singular integrals by
positive sparse forms, J. Lond. Math. Soc. (2) 98 (2018), no. 2, 369–392. MR 3873113 2, 18
[7]
, Uniform sparse domination of singular integrals via dyadic shifts, Math. Res. Lett. 25 (2018), no. 1,
21–42. MR 3818613 5, 18
[8] Amalia Culiuc, Francesco Di Plinio, and Yumeng Ou, A sparse estimate for multisublinear forms involving
vector-valued maximal functions, Bruno Pini Mathematical Analysis Seminar 8 (2018), no. 1, 168–184. 5,
18, 19
[9] Francesco Di Plinio, Kangwei Li, Henri Martikainen, and Emil Vuorinen, Multilinear operator-valued
Calderón-Zygmund theory, J. Funct. Anal. 279 (2020), no. 8, 108666, 62. MR 4109091 3, 7, 10, 11
[10] Francesco Di Plinio and Yumeng Ou, Banach-valued multilinear singular integrals, Indiana Univ. Math. J.
67 (2018), no. 5, 1711–1763. MR 3875242 2, 3
[11] Yen Do, Richard Oberlin, and Eyvindur A. Palsson, Variation-norm and ﬂuctuation estimates for ergodic
bilinear averages, Indiana Univ. Math. J. 66 (2017), no. 1, 55–99. MR 3623404 2
[12] Yen Do and Christoph Thiele, Lp theory for outer measures and two themes of Lennart Carleson united, Bull.
Amer. Math. Soc. (N.S.) 52 (2015), no. 2, 249–296. MR 3312633 2
[13] Tadeusz Figiel, Singular integral operators: a martingale approach, Geometry of Banach spaces (Strobl,
1989), London Math. Soc. Lecture Note Ser., vol. 158, Cambridge Univ. Press, Cambridge, 1990, pp. 95–
110. MR 1110189 2
[14] Tadeusz Figiel and Przemysław Wojtaszczyk, Special bases in function spaces, Handbook of the geometry
of Banach spaces, Vol. I, North-Holland, Amsterdam, 2001, pp. 561–597. MR 1863702 28
[15] Stefan Geiss, Stephen Montgomery-Smith, and Eero Saksman, On singular integral and martingale trans-
forms, Trans. Amer. Math. Soc. 362 (2010), no. 2, 553–575. MR 2551497 2
[16] Loukas Grafakos and José María Martell, Extrapolation of weighted norm inequalities for multivariable
operators and applications, J. Geom. Anal. 14 (2004), no. 1, 19–46. MR 2030573 2
[17] Loukas Grafakos and Seungly Oh, The Kato-Ponce inequality, Comm. Partial Diﬀerential Equations 39
(2014), no. 6, 1128–1157. MR 3200091 5, 6
[18] Loukas Grafakos and Rodolfo H. Torres, Multilinear Calderón-Zygmund theory, Adv. Math. 165 (2002),
no. 1, 124–164. MR 1880324 2, 10
[19] Timo S. Hänninen and Tuomas P. Hytönen, Operator-valued dyadic shifts and the T(1) theorem, Monatsh.
Math. 180 (2016), no. 2, 213–253. MR 3502626 7, 9, 26, 28
[20] Tuomas Hytönen and Mikko Kemppainen, On the relation of Carleson’s embedding and the maximal theorem
in the context of Banach space geometry, Math. Scand. 109 (2011), no. 2, 269–284. MR 2854692 3
[21] Tuomas Hytönen, Alan McIntosh, and Pierre Portal, Kato’s square root problem in Banach spaces, J. Funct.
Anal. 254 (2008), no. 3, 675–726. MR 2381159 3, 4
[22] Tuomas Hytönen and Pierre Portal, Vector-valued multiparameter singular integrals and pseudodiﬀerential
operators, Adv. Math. 217 (2008), no. 2, 519–536. MR 2370274 (2009e:42027) 2
[23] Tuomas Hytönen, Jan van Neerven, and Pierre Portal, Conical square function estimates in UMD Banach
spaces and applications to H∞-functional calculi, J. Anal. Math. 106 (2008), 317–351. MR 2448989 2, 3
[24] Tuomas Hytönen, Jan van Neerven, Mark Veraar, and Lutz Weis, Analysis in Banach spaces. Vol. I.
Martingales and Littlewood-Paley theory, Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A


## Page 36


36
FRANCESCO DI PLINIO, KANGWEI LI, HENRI MARTIKAINEN, AND EMIL VUORINEN
Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A
Series of Modern Surveys in Mathematics], vol. 63, Springer, Cham, 2016. MR 3617205 8, 9, 30, 33
[25]
, Analysis in Banach spaces. Vol. II, Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge.
A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A
Series of Modern Surveys in Mathematics], vol. 67, Springer, Cham, 2017, Probabilistic methods and
operator theory. MR 3752640 8
[26] Tuomas Hytönen and Lutz Weis, A T1 theorem for integral transformations with operator-valued kernel, J.
Reine Angew. Math. 599 (2006), 155–200. MR 2279101 3
[27] Tuomas P. Hytönen, On operator-multipliers for mixed-norm Lp spaces, Arch. Math. (Basel) 85 (2005), no. 2,
151–155. MR 2161804 (2006c:42011) 2
[28] Tuomas P. Hytönen, The sharp weighted bound for general Calderón-Zygmund operators, Ann. of Math. (2)
175 (2012), no. 3, 1473–1506. MR 2912709 1, 3
[29]
, The vector-valued nonhomogeneous Tb theorem, Int. Math. Res. Not. IMRN (2014), no. 2, 451–511.
MR 3159078 7, 9, 26
[30] Tuomas P. Hytönen, Michael T. Lacey, and Ioannis Parissis, The vector valued quartile operator, Collect.
Math. 64 (2013), no. 3, 427–454. MR 3084406 3
[31] Marius Junge and Quanhua Xu, Representation of certain homogeneous Hilbertian operator spaces and appli-
cations, Invent. Math. 179 (2010), no. 1, 75–118. MR 2563760 2
[32] Nigel Kalton and Lutz Weis, The H∞-calculus and sums of closed operators, Math. Ann. 321 (2001), no. 2,
319–345. MR 1866491 2
[33] Tosio Kato and Gustavo Ponce, Commutator estimates and the Euler and Navier-Stokes equations, Comm.
Pure Appl. Math. 41 (1988), no. 7, 891–907. MR 951744 2
[34] Michael Lacey and Christoph Thiele, Lp estimates on the bilinear Hilbert transform for 2 < p < ∞, Ann. of
Math. (2) 146 (1997), no. 3, 693–724. MR 1491450 2
[35]
, On Calderón’s conjecture, Ann. of Math. (2) 149 (1999), no. 2, 475–496. MR 1689336 2
[36] Michael T. Lacey and Darío Mena Arias, The sparse T1 theorem, Houston J. Math. 43 (2017), no. 1, 111–127.
MR 3647935 18
[37] Kangwei Li, José María Martell, Henri Martikainen, Sheldy Ombrosi, and Emil Vuorinen, End-point
estimates, extrapolation for multilinear Muckenhoupt classes, and applications, Trans. Amer. Math. Soc., to
appear. 2, 5
[38] Kangwei Li, José María Martell, and Sheldy Ombrosi, Extrapolation for multilinear muckenhoupt classes
and applications, Adv. Math., to appear. 5
[39] Kangwei Li, Henri Martikainen, Yumeng Ou, and Emil Vuorinen, Bilinear representation theorem, Trans.
Amer. Math. Soc. 371 (2019), no. 6, 4193–4214. MR 3917220 3, 10, 11, 18, 19
[40] Terry R. McConnell, Decoupling and stochastic integration in UMD Banach spaces, Probab. Math. Statist. 10
(1989), no. 2, 283–295. MR 1057936 7, 9
[41] Fedor Nazarov, Sergei Treil, and Alexander Volberg, The Tb-theorem on non-homogeneous spaces, Acta
Math. 190 (2003), no. 2, 151–239. MR 1998349 2, 7
[42] Bas Nieraeth, Quantitative estimates and extrapolation for multilinear weight classes, Math. Ann. 375 (2019),
no. 1-2, 453–507. MR 4000248 2
[43] Stefanie Petermichl, Dyadic shifts and a logarithmic estimate for Hankel operators with matrix symbol, C. R.
Acad. Sci. Paris Sér. I Math. 330 (2000), no. 6, 455–460. MR 1756958 1
[44]
, The sharp bound for the Hilbert transform on weighted Lebesgue spaces in terms of the classical Ap
characteristic, Amer. J. Math. 129 (2007), no. 5, 1355–1375. MR 2354322 1
[45] Gilles Pisier, Martingales in Banach spaces, Cambridge Studies in Advanced Mathematics, vol. 155,
Cambridge University Press, Cambridge, 2016. MR 3617459 15
[46] Gilles Pisier and Quanhua Xu, Non-commutative Lp-spaces, Handbook of the geometry of Banach spaces,
Vol. 2, North-Holland, Amsterdam, 2003, pp. 1459–1517. MR 1999201 15, 16
[47] Lutz Weis, Operator-valued Fourier multiplier theorems and maximal Lp-regularity, Math. Ann. 319 (2001),
no. 4, 735–758. MR 1825406 2, 3, 7
[48] Quanhua Xu, Noncommutative Lp-spaces and martingale inequalities, 2007, Book manuscript. 15


## Page 37


MULTILINEAR SINGULAR INTEGRALS ON NON-COMMUTATIVE Lp SPACES
37
(F.D.P.) Department of Mathematics, Washington University in St. Louis, One Brookings Drive,
St. Louis, MO 63130-4899, USA
E-mail address: francesco.diplinio@wustl.edu
(Kangwei Li) Center for Applied Mathematics, Tianjin University, Weijin Road 92, 300072 Tianjin,
China
and
BCAM, Basque Center for Applied Mathematics, Mazarredo 14, 48009 Bilbao, Basque Country,
Spain
E-mail address: kli@tju.edu.cn
(H.M.) Department of Mathematics and Statistics, University of Helsinki, P.O.B. 68,
FI-00014 University of Helsinki, Finland
E-mail address: henri.martikainen@helsinki.fi
(E.V.) Centre for Mathematical Sciences, University of Lund, P.O.B. 118, 22100 Lund, Sweden
E-mail address: j.e.vuorin@gmail.com

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
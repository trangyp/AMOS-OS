---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1512.08753
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1512.08753_On_the_continuity_of_the_geometric_side_of_the_trace_formula

> Source: 1512.08753_On_the_continuity_of_the_geometric_side_of_the_trace_formula.pdf

> Pages: 33

---


## Page 1


arXiv:1512.08753v3  [math.NT]  8 May 2016
ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE
FORMULA
TOBIAS FINIS AND EREZ LAPID
Abstract. We extend the geometric side of Arthur’s non-invariant trace formula for
a reductive group G deﬁned over Q continuously to a natural space C(G(A)1) of test
functions which are not necessarily compactly supported. The analogous result for the
spectral side was obtained in [FLM11]. The geometric side is decomposed according to the
following equivalence relation on G(Q): γ1 ∼γ2 if γ1 and γ2 are conjugate in G(Q) and
their semisimple parts are conjugate in G(Q). All terms in the resulting decomposition are
continuous linear forms on the space C(G(A)1), and can be approximated (with continuous
error terms) by naively truncated integrals.
Contents
1.
Introduction
1
2.
Notation and preliminaries
4
3.
An estimate for truncated integrals
7
4.
Alternating sum-integrals over unipotent radicals
12
5.
Continuity of the coarse geometric expansion
19
6.
Modiﬁcations for the ﬁner classes
22
7.
The main result
30
References
32
1. Introduction
Let G be a reductive group deﬁned over Q and let A = R × Af be the ring of adeles.
As usual, we write G(A)1 = ∩Ker |χ|A×, where χ ranges over the rational characters of
G. The original (non-invariant) form of Arthur’s trace formula is an identity between two
distributions f 7→J(f) on G(A)1, a geometric one and a spectral one. The geometric side
can be split according to the following equivalence relation on G(Q): γ1 ∼γ2 if γ1 and γ2
are conjugate in G(Q) and their semisimple parts are conjugate in G(Q). In other words,
if O is the set of pertinent equivalence classes, then there is a decomposition
(1)
J(f) =
X
o∈O
Jo(f),
f ∈C∞
c (G(A)1).
Date: November 8, 2018.
Second named author partially supported by grant #711733 from the Minerva Stiftung.
1


## Page 2


2
TOBIAS FINIS AND EREZ LAPID
(See [Art86]. Actually, in [ibid.] a ﬁner equivalence relation is considered, but for our
purposes the relation ∼is more suitable.1) The distributions Jo(f) are well understood
(as weighted orbital integrals) in the case where o is a semisimple conjugacy class of
G(Q). However, they are more mysterious for other classes, most notably for the unipotent
geometric orbits. See [Cha, HW13, Hof14] for some recent progress on this problem.
For any compact open subgroup K of G(Af) the space G(A)1/K is a diﬀerentiable
manifold (namely a countable disjoint union of copies of G(R)1 = G(R) ∩G(A)1). Any
element X ∈U(g1
∞) of the universal enveloping algebra of the Lie algebra g1
∞of G(R)1
deﬁnes a left invariant diﬀerential operator f 7→f ∗X on G(A)1/K. Let C(G(A)1; K) be
the space of smooth right K-invariant functions on G(A)1 which belong, together with all
their derivatives, to L1(G(A)1). The space C(G(A)1; K) becomes a Fr´echet space under
the seminorms
∥f ∗X∥L1(G(A)1),
X ∈U(g1
∞).
We denote by C(G(A)1) the union of C(G(A)1; K) as K varies over the compact open
subgroups of G(Af) and endow C(G(A)1) with the inductive limit topology.
The purpose of this paper is to show that the geometric side of Arthur’s trace formula
(1) extends continuously to the class C(G(A)1). More precisely, we show that
X
o∈O
|Jo(f)|
extends to a continuous seminorm on C(G(A)1) (see Corollary 7.2 below). The analogous
result for the spectral side was obtained in [FLM11], so that the present paper establishes
a trace formula for functions in the class C(G(A)1).
Moreover, we show that the distributions Jo can be computed using naive truncation.
Namely, using the notation of §2.1 below, there exist distributions f 7→JT
o (f), o ∈O,
on C(G(A)1), which are polynomial functions of the parameter T ∈a0, and satisfy the
following approximation property: for any K there exists a continuous seminorm µ on
C(G(A)1; K) (depending polynomially on the level of K) such that
X
o∈O

Z
G(Q)\G(A)1
≤T
X
γ∈o
f(x−1γx) dx −JT
o (f)
 ≤µ(f)(1 + ∥T∥)re−d(T)
for all f ∈C(G(A)1; K) and T ∈a0 with d(T) := minα∈∆0 ⟨α, T⟩> d0, where the constants
d0 and r are independent of f and K. The distribution Jo(f) is obtained by evaluating
JT
o (f) at a certain distinguished point T = T0 (see [Art81, §1]).
In a previous paper [FL11] we proved similar results for the contribution of the semisim-
ple conjugacy classes of G(Q). In fact, if we coarsen the relation ∼by only requiring
that the semisimple parts are conjugate in G(Q) (obtaining the so-called coarse classes of
Arthur), then the methods of [ibid.], combined with Arthur’s basic procedure in [Art78],
yield the desired result for the coarse geometric expansion, as will be explained in §3–5
below. The main result of this part of the paper is Theorem 5.1. To go further, we use
1In Remark 7.3 below we will consider a slight reﬁnement of the equivalence relation ∼in the case
where the derived group of G is not simply connected.


## Page 3


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
3
recent work of Chaudouard–Laumon [CL16], which provides a suitable deﬁnition for the
modiﬁed kernel pertaining to a class of ∼. This deﬁnition, which has also been suggested
by Hoﬀmann [Hof14], turns out to be very useful for our purpose. The continuity of the
ﬁner decomposition with respect to ∼is dealt with in §6–7, the main results being Theorem
7.1 and Corollary 7.2. We remark that our results extend earlier results by Hoﬀmann in
this direction [Hof08]. In the Lie algebra case, Chaudouard proved very recently similar
results for the space of Schwartz-Bruhat functions [Cha15].
One of the main reasons to consider the trace formula on the space C(G(A)1) is the
connection to automorphic L-functions (in a suitable right half-plane). Namely, ﬁxing a
model of G over Z, there exists a ﬁnite set S0 ⊃{∞} of places of Q with the following
property. Let ρ be a representation of the L-group LG of G. Then for all p /∈S0 there
exists a unique bi-G(Zp)-invariant function φρ,p,s on G(Qp) with tr πp(φρ,p,s) = Lp(πp, ρ, s)
for all unramiﬁed representations πp of G(Qp), where both sides are either considered as
formal power series in p−s or Re s has to be suitably large.
Let now S ⊃S0 be ﬁnite set of places of Q, φp ∈L1(G(Qp)) for all p ∈S \ {∞} and φ∞
be a C∞-function on G(R) with ∥f ∗X∥L1(G(R)) < ∞for all X ∈U(g∞). Set
φρ,s(g) =
Y
v∈S
φv(gv)
Y
p/∈S
φρ,p,s(gp),
g = (gv) ∈G(A).
Then for Re s large enough (depending on G and ρ) the function
fρ,s(g) =
Z
SZ(R)◦φρ,s(ag) da,
where SZ is the maximal split torus contained in the center of G, is an element of C(G(A)1).
The contribution of a discrete automorphic representation π of G(A) to the spectral side
of the trace formula for fρ,s will be non-zero only if π is unramiﬁed outside of S, and in
this case it will be equal to
m(π)
Y
v∈S
tr πv(φv) LS(π, ρ, s),
where m(π) is the multiplicity of π in the discrete spectrum and LS(π, ρ, s) = Q
p/∈S Lp(πp, ρ, s)
is the (incomplete) automorphic L-function of π associated to ρ.
A prototype case is G = GL(n) and ρ the standard representation. In this case one
might more concretely take φ to be the product of the restriction to G(A) of a Schwartz-
Bruhat function Φ on the adelic Lie algebra g(A) of G and of the function |det|s+(n−1)/2
A×
.
The resulting function fρ,s will be an element of C(G(A)1) for Re s > (n + 1)/2. The
contribution of a discrete automorphic representation π can be expressed in terms of the
zeta integrals of Godement-Jacquet [GJ72], and it is therefore the product of a locally
deﬁned entire function of s (which depends on Φ and π) and of the completed standard
L-function of π at the point s. This case and its connection to the trace formula for the
Lie algebra have been studied by Jasmin Matz (see [Mat13] and work in preparation).
Although this is very far-fetched at this stage, the hope is that using the trace formula for
generating functions of the above type will ultimately provide means to attack Langlands


## Page 4


4
TOBIAS FINIS AND EREZ LAPID
functoriality conjectures beyond the very limited scope (however important) of the current
methods. This general idea, and its variations were suggested by Langlands in [Lan04,
Lan07] with some subsequent analysis in [FLN10, Lan13] – see also [Ngˆo14] and [BCS14]
for closely related themes. The humble purpose of the current paper is to provide one of
the very ﬁrst technical steps in this direction.
We are very grateful to Werner Hoﬀmann for spotting a mistake as well as a number
of inaccuracies in an earlier version of this paper and for his suggestion to explicate the
dependence of our estimates on the level of K. We also thank Laurent Clozel and Bao
Chˆau Ngˆo for useful discussions.
2. Notation and preliminaries
2.1.
For the rest of the paper let G be a reductive group deﬁned over Q. Let Gder be its
derived group and ZG be the center of G. We ﬁx a minimal parabolic subgroup P0 deﬁned
over Q and a Levi decomposition P0 = M0 ⋉N0 of P0. Let S0 be the split part of the
center of M0 ∩Gder and X∗(S0) the lattice of co-characters of S0. Let A0 be the identity
component of the topological group S0(R) and a0 = X∗(S0) ⊗R. We can identify the dual
space a∗
0 with X∗(M0/ZG) ⊗R, where X∗(M0/ZG) is the lattice of rational characters of
M0 (or P0) which are trivial on ZG. We denote the set of simple roots of S0 acting on N0
by ∆0. Let ρ0 ∈a∗
0 be the element corresponding to δ1/2
0 , where δ0 is the modulus function
of P0. We deﬁne the homomorphism
H0 : M0(A) →a0
by ⟨χ, H0(m)⟩= log |χ(m)|A∗for any m ∈M0(A) and χ ∈X∗(M0/ZG), where |·|A∗is the
standard absolute value on A∗.
Except otherwise mentioned, all parabolic subgroups considered are implicitly assumed
to be deﬁned over Q. If P is a standard parabolic subgroup, then we write P = MP ⋉NP
(or simply P = M ⋉N, if P is clear from the context) for its standard Levi decomposition.
The set of simple roots of S0 in N0 ∩MP is denoted by ∆P
0 . It is a subset of ∆0. We write
aP = X∗(SM) ⊗R, where SM is the split part of the center of M ∩Gder, and view aP as
a subspace of a0 whose complement is aP
0 = X∗(S0 ∩Mder). Thus, we may view the dual
space a∗
P as a subspace of a∗
0. We also write AM for the identity component of SM(R). We
write ∆P for the image of ∆0 \ ∆P
0 under the projection a∗
0 →a∗
P. More generally, if Q is
a parabolic subgroup containing P, then we write ∆Q
P for the projection of ∆Q
0 \ ∆P
0 under
a∗
0 →a∗
P. Similarly, we have the set of coroots ∆∨
0 and, more generally, for Q ⊃P the
set (∆Q
P )∨which forms a basis of aQ
P := aP ∩aQ
0 . We denote the basis of (aQ
P )∗(resp., aQ
P)
dual to (∆Q
P)∨(resp., ∆Q
P ) by ˆ∆Q
P (resp., ( ˆ∆Q
P )∨). As usual, we suppress the superscript if
Q = G. We write τ Q
P and ˆτ Q
P for the characteristic functions of the sets
{X ∈a0 : ⟨α, X⟩> 0 for all α ∈∆Q
P }
and
{X ∈a0 : ⟨̟, X⟩> 0 for all ̟ ∈ˆ∆Q
P },
respectively.


## Page 5


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
5
We ﬁx a “good” maximal compact subgroup K = K∞Kﬁn of G(A) (i.e., we require K
to be admissible relative to M0 in the sense of [Art81, §1]). We extend the left M0(A)1-
invariant map H0 : M0(A) →a0 to a left P0(A)1- and right K-invariant function
H0 : G(A) →a0.
For T1 ∈a0 let
ST1 = {x ∈G(A) : τ0(H0(x) −T1) = 1}
and more generally
SP
T1 = {x ∈G(A) : τ P
0 (H0(x) −T1) = 1}
for any P ⊃P0. These sets are then evidently left P0(A)1-invariant. By reduction theory,
there exists T1 ∈a0 such that
P(Q)SP
T1 = G(A)
for all P ⊃P0, and in particular for P = G. Thus,
(2)
Z
P (Q)\G(A)1 |f(x)| dx ≤
Z
K
Z
N0(Q)\N0(A)
Z
A0
Z
M0(Q)\M0(A)1 |f(uamk)| τ P
0 (H0(a) −T1)δ0(a)−1 dm da du dk
for any left P(Q)-invariant measurable function f on G(A)1. We ﬁx T1 as above once and
for all.
Let
G(A)1
≤T = {g ∈G(A)1 : ˆτ0(T −H0(γg)) = 1 for all γ ∈G(Q)}.
There exists d0 > 0 (which depends only on G, P0 and K, and which we may therefore ﬁx
once and for all) such that
G(A)1
≤T ∩ST1 = {g ∈G(A)1 : τ0(H0(g) −T1)ˆτ0(T −H0(g)) = 1}
provided that d(T) := minα∈∆0 ⟨α, T⟩> d0. More generally, for any P ⊃P0 let F P(x, T)
be the characteristic function of the set
{g ∈G(A) : ˆτ P
0 (T −H0(γg)) = 1 for all γ ∈P(Q)}.
By Arthur’s partition lemma [Art78, Lemma 6.4], we have
(3)
X
P ⊃P0
X
γ∈P (Q)\G(Q)
F P(γx, T)τP(HP(γx) −T) = 1,
x ∈G(A),
provided that d(T) > d0.
Let W = NG(Q)(M0)/M0 be the Weyl group of G. For any w ∈W we ﬁx a representative
nw ∈G(Q) (it is determined up to multiplication by an element of M0(Q)) and set
(4)
Q(w) = the smallest standard parabolic subgroup of G containing nw.


## Page 6


6
TOBIAS FINIS AND EREZ LAPID
2.2.
Let H be an algebraic subgroup of G deﬁned over Q. We denote by δH the modulus
function of the group H(A). We will write h for the Lie algebra of H(R). (We will retain
this typographic convention for other groups.) We recall the norms
∥f∥H,k =
X
i
∥f ∗Xi∥L1(H(A)),
k ≥0,
where Xi ranges over a ﬁxed basis of U(h)≤k with respect to the standard ﬁltration. We
write µH
0 (f) = ∥f∥H,dim H.
For any compact open subgroup K of H(Af) we consider
the Fr´echet space C(H(A); K) of right K-invariant smooth functions f on H(A) such
that ∥f∥H,k < ∞for all k, and deﬁne C(H(A)1; K) and µH,1
0
(f) = ∥f∥H(A)1, dim H−rk X∗(H)
analogously.
We recall a few useful facts about these norms. (See [FL11, §3]. Note that the depen-
dence on K is not explicated in [ibid.], but it is easy to extract it from the argument. Also
note that a factor δH(h)−1 is missing on the right-hand side of the second inequality of
[FL11, Lemma 3.3].)
Henceforth, for non-negative quantities A and B we use the notation A ≪B to mean
that there exists some constant c > 0 such that A ≤cB. If c depends on some additional
parameters (such as X) we will write A ≪X B.
Lemma 2.1.
(1) For any f ∈C(H(A)1; K) we have
X
γ∈H(Q)
|f(γ)| ≪H vol(K)−1µH,1
0
(f).
(2) Let C ⊂H(A)1 be a compact set and µ a continuous seminorm on C(H(A)1; K).
Then supx∈C µ(f(·x)) and supx∈C µ(f(x−1 · x)) are continuous seminorms on the
space C(H(A)1; ∩x∈Cx−1Kx) and ∥f(x−1·x)∥H(A)1,k = ∥f(·x)∥H(A)1,k ≪C,k ∥f∥H(A)1,k
for all f ∈C(H(A)1), k ≥0, x ∈C.
(3) For any f ∈C(G(A)1; K) there exists ˜f ∈C(G(A)1; Kﬁn) such that ˜f(x) ≥|f(x)|
for all x ∈G(A)1, ˜f is right K-invariant, and ∥˜f ∗X∥L1(G(A)1) ≪X vol(K)−1µG,1
0 (f)
for any X ∈U(g1).
(4) Let P be a standard parabolic subgroup of G. For any f ∈C(G(A)1; K) deﬁne
(5)
fP(m) =
Z
K
Z
N(A)
f(k−1mnk) dn dk,
m ∈M(A)1.
Then f 7→fP is a continuous map from the space C(G(A)1; K) to the space
C(M(A)1; ∩k∈KkKk−1 ∩M(A)).
2.3.
We ﬁx a faithful Q-rational representation r0 : G →GL(N0) such that Kﬁn = {g ∈
G(Af) : r0(g) ∈GL(N0, ˆZ)}. For any positive integer N let
K(N) = {g ∈G(Af) : r0(g) ≡1
(mod N)}
be the principal congruence subgroup of level N, a factorizable normal open subgroup of
Kﬁn. The groups K(N) form a neighborhood base of the identity element in G(Af).


## Page 7


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
7
Throughout the paper K denotes a compact open subgroup of G(Af). The level of K is
deﬁned as the smallest positive integer N with K(N) ⊂K. We denote it by level(K).
3. An estimate for truncated integrals
3.1.
In this section, we prove a slight variant of the main result of [FL11], which is basic
for all following estimates. For any parabolic subgroup P of G (deﬁned over Q) we deﬁne
G(Q)◦
P = G(Q) \ ∪P ⊂P ′⊊GP ′(Q).
The set G(Q)◦
P is bi-P(Q)-invariant and G(Q)◦
G = G(Q). For standard parabolic subgroups
P ⊂Q we set
(6)
ξQ
P =
X
α∈∆Q
0 \∆P
0
α ∈a∗
0.
Theorem 3.1. There exist an integer r ≥0, depending only on G, and a continuous
seminorm µ on C(G(A)1; K), such that for any standard parabolic subgroup P of G and
any l ≥0 we have
(7)
Z
P (Q)\G(A)1 F P(g, T)τP(HP(g) −T)∥HP(g) −TP∥l
X
γ∈G(Q)◦
P
f(g−1γg)
 dg
≪l (1 + ∥T∥)re−⟨ξP ,T⟩µ(f)
for any f ∈C(G(A)1; K) and any T ∈a0 such that ⟨α, T −T1⟩≥0 for all α ∈∆0.
Moreover, we can take µ = c vol(K)−1µG,1
0
with a constant c that does not depend on K.
For P = P0, T = T1 and l = 0 this specializes to one of the main intermediate results
of [FL11] (which implies immediately the continuity of the regular elliptic contribution to
the trace formula). For P = G we obtain that
(8)
f 7→
sup
T:d(T)>d0
(1 + ∥T∥)−r
Z
G(Q)\G(A)1
≤T
X
γ∈G(Q)
f(g−1γg)
 dg
is a continuous seminorm on C(G(A)1).
(A more careful analysis shows that we can in fact take r = dim a0.)
In the remainder of this section we will prove Theorem 3.1.
The proof follows the
argument of [FL11] closely, but on the one hand it is possible to simplify the argument
(cf. [ibid., Remark 3]), and on the other hand we need to keep track of the dependence on
T.
As in [ibid.], the main intermediate step is an estimate for truncated integrals over the
Bruhat cells of Weyl group elements w ∈W with Q(w)P = G. We state the necessary
generalization of [ibid., Proposition 5.1] now, and postpone the proof to §3.2 below.


## Page 8


8
TOBIAS FINIS AND EREZ LAPID
Proposition 3.2. Let P be a standard parabolic subgroup of G and w ∈W with Q(w)P =
G. There exist an integer r ≥0 and a continuous seminorm µ on C(G(A)1; K) such that
for any l ≥0 we have
Z
N0(A)/Nw(A)
Z
N0(A)
Z
A0
Z
M0(A)1
f(a−1u2nwau1m)
 χT,P,l(a) dm da du1 du2
≪K,l µ(f)(1 + ∥T∥)re−⟨ξP ,T⟩,
where Nw = N0 ∩nwN0n−1
w and
χT,P,l(a) = τP(HP(a) −T)τ P
0 (H0(a) −T1)ˆτ P
0 (T −H0(a))
X
α∈∆P
⟨α, HP(a) −T⟩l .
As usual, we also need to estimate sums over the unipotent radicals of standard parabolic
subgroups by integrals.
Lemma 3.3. Let P = M ⋉N be a standard parabolic subgroup of G. Then there exist
X1, . . . , Xm ∈U(n) such that for any compact open subgroup K′ of N(Af) we have
X
n∈N(Q)
f(a−1nua)
 ≤vol(K′)−1 X
i
Z
N(A)
(f ∗Xi)(a−1na)
 dn
for any f ∈C(N(A); K′), u ∈N(A) and a ∈A0 such that τ0(H0(a) −T1) = 1.
Proof. The special case a = 1 follows immediately from Lemma 2.1, parts 1 and 2, since u
can be taken in a compact set.
Moreover, we can take the diﬀerential operators Xi to be a basis for U(n)≤dim n with
Ad(a)Xi = χi(a)Xi for a ∈A0, where each χi is a character of A0 which is a sum of
positive roots.
We therefore have |χi(a)|−1 ≪1 for τ0(H0(a) −T1) = 1.
The lemma
follows, since the function fa = f(a−1 · a) on N(A) satisﬁes
fa ∗Xi(n) = [f ∗Ad(a−1)Xi](a−1na) = χi(a)−1(f ∗Xi)(a−1na),
n ∈N(A).
□
Proof of Theorem 3.1. Using (2), we ﬁrst estimate the left-hand side of (7) by a constant
multiple (which depends only on l) of
Z
K
Z
N0(Q)\N0(A)
Z
A0
Z
M0(Q)\M0(A)1
X
γ∈G(Q)◦
P
f((uamk)−1γuamk)
 χ(a)δ0(a)−1 dm da du dk,
where for convenience we write χ(a) = χT,P,l(a). Note that χ(a) is non-negative, and that
under our assumption on T the argument of [Art78, pp. 943–944] shows that
(9)
χ(a) > 0 implies τ0(H0(a) −T1) = 1.
Since m and k are integrated over compact sets, we can use Lemma 2.1, part 2, to reduce
to bounding
Z
N0(Q)\N0(A)
Z
A0
X
γ∈G(Q)◦
P
f(a−1u−1γua)
 χ(a)δ0(a)−1 da du.


## Page 9


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
9
Recall that G(Q)◦
P is bi-P(Q)-invariant and therefore a union of Bruhat cells. In fact,
G(Q)◦
P =
[
w∈W : Q(w)P =G
N0(Q)nwP0(Q).
Thus, we need to consider
Z
N0(Q)\N0(A)
Z
A0
X
γ∈N0(Q)nwP0(Q)
f(a−1u−1γua)
 χ(a)δ0(a)−1 da du
for any w ∈W with Q(w)P = G. We write this as
Z
N0(Q)\N0(A)
Z
A0
X
u2∈Nw(Q)\N0(Q)
X
m∈M0(Q)
X
u1∈N0(Q)
f(a−1u−1u−1
2 mnwu1ua)
 χ(a)δ0(a)−1 da du.
Using (9), we can apply Lemma 3.3 and estimate the sum over u1 by the integrals of the
functions f ∗X, X ranging over a ﬁxed ﬁnite set of diﬀerential operators. Replacing f by
one of these derivatives, we can reduce to
Z
N0(Q)\N0(A)
Z
A0
Z
N0(A)
X
u2∈Nw(Q)\N0(Q)
X
m∈M0(Q)
f(a−1u−1u−1
2 mnwau1)
 χ(a) du1 da du,
i.e., to
Z
Nw(Q)\N0(A)
Z
A0
Z
N0(A)
X
m∈M0(Q)
f(a−1u−1mnwau1)
 χ(a) du1 da du.
Note that as a function of u, the inner integral is left Nw(A)-invariant, and hence we get
Z
Nw(A)\N0(A)
Z
A0
Z
N0(A)
X
m∈M0(Q)
f(a−1u−1mnwau1)
 χ(a) du1 da du,
which is also
Z
Nw(A)\N0(A)
Z
A0
Z
N0(A)
X
m∈M0(Q)
f(a−1u−1nwau1m)
 χ(a) du1 da du.
Finally, using Lemma 2.1, part 1, we reduce to
Z
Nw(A)\N0(A)
Z
A0
Z
N0(A)
Z
M0(A)1
f(a−1u−1nwau1m)
 χ(a) dm du1 da du,
which is continuous by Proposition 3.2. The assertion about µ follows directly from Lemma
2.1, part 3.
□


## Page 10


10
TOBIAS FINIS AND EREZ LAPID
3.2.
It remains to prove Proposition 3.2. Since the argument is very similar to the proof
of [FL11, Proposition 5.1], we refer the reader to the earlier paper and only give the parts
of the argument of [ibid.] that need to be modiﬁed. We remark that the case P = P0,
l = 0 and T = T1 is already contained in [ibid., Proposition 5.1]. The main diﬀerence is
that we now have to keep track of the dependence of T.
To that end, we ﬁrst recall [FL11, Proposition 3.1]. Let V be a ﬁnite-dimensional real
vector space and let D(V ) be the space of invariant diﬀerential operators on V with the
standard ﬁltration. Let C(V ) be the Fr´echet space of smooth functions f on V such that
∥f ∗D∥L1(V ) < ∞for any D ∈D(V ). For any f ∈C∞
c (V ) let ˆf be its Fourier-Laplace
transform given by
ˆf(λ) =
Z
V
e−⟨λ,v⟩f(v) dv,
λ ∈V ∗
C,
where V ∗
C the complexiﬁed dual space of V . Then ˆf is an entire function which is rapidly
decreasing for Re λ in a compact set.
Fix a linearly independent set S in V and µ0 ∈V ∗. Let h be a holomorphic function
on the set of λ ∈V ∗
C with Re λ ∈R, where R is a bounded connected open subset of V ∗
containing µ0. Assume that h is majorized by a polynomial function and let λ0 ∈R be
with ⟨λ0 −µ0, u⟩> 0 for all u ∈S. Then
f ∈C∞
c (V ) 7→
Z
Re λ=λ0
ˆf(λ −µ0)h(λ)
Q
u∈S ⟨λ −µ0, u⟩dλ
extends to a continuous functional on C(V ). We now make this statement eﬀective as
follows.
Proposition 3.4. Let S, µ0, λ0, and h be as above. For any n ≥0 there exists a continuous
seminorm µ on C(V ) such that

Z
Re λ=λ0
ˆf(λ −µ0)h(λ)
Q
u∈S ⟨λ −µ0, u⟩dλ
 ≪n,S µ(f)
X
i
sup
Re λ=µ0
(1 + ∥λ∥)−n |(h ∗Xi)(λ)| ,
where (Xi)i is a basis of D(V ∗)≤|S|.
Proof. We may assume without loss of generality that µ0 = 0. Following the proof of
[FL11, Proposition 3.1], let ̟u ∈V ∗, u ∈S, be elements with ⟨̟u, u′⟩= δu,u′ and deﬁne
for any I ⊂S the holomorphic function hS,I by
hS,I(λ) =
P
I⊂J⊂S(−1)|J|−|I|h(λ −P
u∈J ⟨λ, u⟩̟u)
Q
u∈S\I ⟨λ, u⟩
.
We then need to estimate (1 + ∥λ∥)−n |hS,I(λ)| for λ ∈iI⊥.
Let f be a smooth function on R and g(x) = (f(x) −f(0))/x. Then we have
|g(x)| =

Z 1
0
f ′(tx) dt
 ≤sup
|t|≤|x|
|f ′(t)|


## Page 11


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
11
for all x ∈R. Applying this to the independent variables ⟨λ, u⟩, u ∈S \ I, we obtain the
estimate
|hS,I(λ)| ≪
X
i
sup
µ∈iV ∗:∥µ∥≤∥λ∥
|(h ∗Xi)(µ)| ,
Re λ = 0,
which ﬁnishes the proof.
□
Lemma 3.5. Let P be a standard parabolic subgroup of G and w ∈W with Q(w)P = G.
Then the integral
φT,P,l(λ) =
Z
A0
aw−1λ−λχT,P,l(a) da
converges absolutely and uniformly for Re λ in any compact subset of the positive Weyl
chamber. Moreover, for Re λ = ρ0 we have
|(φT,P,l ∗D)(λ)| ≪D,l (1 + ∥T∥)d+dim aP
0 e−⟨ξP ,T⟩
for any diﬀerential operator D ∈D(a∗
0) of degree d.
Proof. Using the direct sum decomposition a0 = aP ⊕aP
0 , we ﬁrst apply Fubini’s theorem
formally to obtain φT,P,l(λ) = ψT,P,l(λ)ψP
T (λ) with
ψT,P,l(λ) =
Z
aP
e⟨w−1λ−λ,X⟩τP(X −T)
X
α∈∆P
⟨α, X −T⟩l dX
and
ψP
T (λ) =
Z
aP
0
e⟨w−1λ−λ,Y ⟩τ P
0 (Y −T1)ˆτ P
0 (T −Y ) dY.
The integrand in the deﬁnition of ψP
T (λ) is compactly supported, and the integral therefore
converges absolutely for any value of λ. For λ = λ0 ∈a∗
0, the integrands above are all non-
negative real, and it remains to check the convergence of the integral deﬁning ψT,P,l(λ0)
for λ0 in the positive Weyl chamber. By [FL11, Lemma 2.2], for such values of λ0 we
have λ0 −w−1λ0 = P
α∈∆Q(w)
0
cαα with cα > 0 for all α ∈∆Q(w)
0
. Since ∆Q(w)
0
∪∆P
0 = ∆0
by our assumptions on P and w, we have ⟨λ0 −w−1λ0, ̟∨⟩> 0 for all ̟∨∈ˆ∆∨
P. The
convergence assertion follows.
Furthermore, in the range of absolute convergence for ψT,P,l(λ) we can express X in the
basis ˆ∆∨
P and compute
ψT,P,l(λ) = vol(aP/Z ˆ∆∨
P )e⟨w−1λ−λ,TP⟩
Y
̟∨∈ˆ∆∨
P
1
⟨w−1λ −λ, ̟∨⟩
X
̟∨∈ˆ∆∨
P
l!
⟨w−1λ −λ, ̟∨⟩l .
To estimate the derivatives of φT,P,l(λ) for Re λ = ρ0, we may without loss of generality
assume that D = DPDP with DP ∈D(a∗
P) and DP ∈D((aP
0 )∗) of degree dP and dP,
respectively. It is then clear from the expression above that
|(ψT,P,l ∗DP)(λ)| ≪DP ,l (1 + ∥T∥)dP e⟨w−1ρ0−ρ0,TP⟩.


## Page 12


12
TOBIAS FINIS AND EREZ LAPID
On the other hand, the function τ P
0 (Y −T1)ˆτ P
0 (T −Y ) is the characteristic function of the
convex hull of the points {T P
Q + T Q
1
: P0 ⊂Q ⊂P}. Therefore,
(ψP
T ∗DP)(λ)
 ≪DP (1 + ∥T∥)dP +dim aP
0
X
P0⊂Q⊂P
e⟨w−1ρ0−ρ0,T P
Q⟩.
Since for any P0 ⊂Q ⊂P we have ⟨w−1ρ0 −ρ0, TQ⟩≤−⟨ξP, T⟩, the required estimate
follows.
□
It is of course possible to evaluate the integral φT,P,l(λ) explicitly, since the factor ψP
T (λ)
can be computed by applying [Art81, Lemma 2.2].
Proof of Proposition 3.2. Following [FL11, §5], we may assume f ∈C(G(A)1) to be com-
pactly supported, non-negative and right K-invariant, and write the integral as
Z
Re λ=λ0
φT,P,l(λ)m(w−1, λ)ϕ(λ) dλ
for λ0 ∈a∗
0 such that λ0 −ρ0 lies in the positive Weyl chamber. Here, the scalar m(w−1, λ)
is the spherical intertwining operator (cf. [ibid., §3.3]) and
ϕ(λ) =
Z
A0
Z
P0(A)1 f(pa)a−(λ+ρ0) dp da.
It remains to apply Proposition 3.4 with V = a0, µ0 = ρ0 and S = {α∨∈∆∨
0 : w−1(α) <
0}, and to invoke the estimate of Lemma 3.5.
□
4. Alternating sum-integrals over unipotent radicals
4.1.
Let I be a ﬁnite set and L ≥1 an integer parameter (which will eventually be taken
to be essentially the level of K). For any I′ ⊂I let [0, L]I;I′ be the face of the cube [0, L]I
consisting of the vectors whose coordinates in I′ vanish, endowed with the normalized
Lebesgue measure. Using integration by parts it is easy to see that
Z
[0,L]I
∂|I′|f
Q
i∈I′ ∂xi
(x)
Y
i∈I′
(xi −L) dx =
X
I′′⊂I′
(−1)|I′\I′′|
Z
[0,L]I;I′′ f(x) dx,
or equivalently,
Z
[0,L]I;I′ f(x) dx =
X
I′′⊂I′
Z
[0,L]I
∂|I′′|f
Q
i∈I′′ ∂xi
(x)
Y
i∈I′′
(xi −L) dx
for any f ∈C|I|([0, L]I) and I′ ⊂I. Thus, given any numbers cI′ ∈C indexed by the
subsets I′ of I, we have
(10)
X
I′⊂I
cI′
Z
[0,L]I;I′ f(x) dx =
X
I′⊂I
dI′
Z
[0,L]I
∂|I′|f
Q
i∈I′ ∂xi
(x)
Y
i∈I′
(xi −L) dx,
where dI′ = P
I′′⊃I′ cI′′. We single out a special case.


## Page 13


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
13
Lemma 4.1. Let Ij, j ∈J, be a family of (not necessarily disjoint) non-empty subsets of
I. For any J′ ⊂J let [0, L]I
J′ be the face of [0, L]I consisting of the vectors whose support
is contained in the index set ∪j /∈J′Ij ⊂I, endowed with the normalized Lebesgue measure.
Then for any f ∈C|I|([0, L]I) we have
X
J′⊂J
(−1)|J\J′|
Z
[0,L]I
J′
f(x) dx =
X′
I′
Z
[0,L]I
∂|I′|f
Q
i∈I′ ∂xi
(x)
Y
i∈I′
(xi −L) dx,
and in particular
(11)

X
J′⊂J
(−1)|J′|
Z
[0,L]I
J′
f(x) dx
 ≤L|I| X′
I′
Z
[0,L]I

∂|I′|f
Q
i∈I′ ∂xi
(x)
 dx,
where the sums on the right-hand sides range over the subsets I′ ⊂I such that I′ ∩Ij ̸= ∅
for all j ∈J.
Proof. Indeed, we take
cI′ =
X
J′⊂J:∪j /∈J′Ij=I\I′
(−1)|J\J′|,
and note that
dI′ =
X
I′′⊃I′
cI′′ =
X
J′⊂J:∪j /∈J′Ij⊂I\I′
(−1)|J\J′| =
X
{j∈J:Ij∩I′̸=∅}⊂J′⊂J
(−1)|J\J′|,
which is 1 if Ij ∩I′ ̸= ∅for all j ∈J, and 0 otherwise.
□
As an immediate consequence we derive an adelic version as follows. Let Bﬁn(L) be the
compact open subgroup
Bﬁn(L) =
Y
p<∞
pvp(L)Zp
of Af and let B(L) be the set
B(L) = [0, L) × Bﬁn(L),
endowed with the product of the Lebesgue measure and the Haar measure, normalized
such that vol(B(L)) = 1. The set B(L) is a fundamental domain for Q\A.
Lemma 4.2. Let Ij, j ∈J, be as in Lemma 4.1. Then for any f ∈C|I|(AI; Bﬁn(L)I) we
have

X
J′⊂J
(−1)|J′|
Z
BI
J′(L)
f(x) dx
 ≤L|I| X′
I′
Z
B(L)I

∂|I′|f
Q
i∈I′ ∂xi
(x)
 dx,
where B(L)I
J′ is the subset of B(L)I consisting of the vectors whose coordinates outside
∪j /∈J′Ij vanish (with the natural measure normalized by vol = 1).


## Page 14


14
TOBIAS FINIS AND EREZ LAPID
4.2.
We ﬁx once and for all a basis (eα)α∈Σ0 of n0, indexed by a set Σ0, such that Ad(a),
a ∈A0, acts on each basis vector eα by multiplication with a character. We simply write
Ad(a)eα = α(a)eα for all a ∈A0, α ∈Σ0, i.e., we consider the index set Σ0 as the set of roots
of A0 on N0, counting multiplicities. For α, β ∈Σ0 we write α ≺β if β −α = P
γ∈∆0 xγγ
where xγ ≥0 for all γ. For any standard parabolic subgroup P ⊂G we view the set ΣP
of roots of A0 on n as a subset of Σ0. The vectors (eα)α∈ΣP form then a basis of n. Let
cP : AΣP →n(A) be the isomorphism given by cP((xα)α∈ΣP ) = P xαeα. We deﬁne
BP(L) = exp(cP(B(L)ΣP )),
BP,ﬁn(L) = exp(cP(Bﬁn(L)ΣP )).
Note that there exists an integer L0 ≥1, depending only on G, such that BP,ﬁn(L) is a
compact open subgroup of N(Af) whenever L is divisible by L0. Also, BP (L) = B0(L) ∩
N(A), and more generally BQ(L) = BP(L) ∩NQ(A) for any P ⊂Q.
Lemma 4.3. The set BP(L) is a fundamental domain for N(Q)\N(A).
Proof. Fix a linear order ≤on ΣP which extends ≺. Let N≥α (resp., N>α) be the image
under exp of the linear span of eβ, β ≥α (resp., β > α). Then N≥α and N>α are normal
subgroups of N deﬁned over Q, and for all α ∈ΣP , N≥α/N>α is one-dimensional and
central in N/N>α. Moreover, exp(x + y) ∈exp(x) exp(y)N>α for any x ∈n and y in the
linear span of eβ, β ≥α. We show by induction on α that
(12)
N(Q)N≥α(A) exp({
X
β<α
xβeβ : xβ ∈B(L)}) = N(A).
The case where α is the minimal element of ΣP is trivial. Assume that (12) holds for some
α ∈ΣP . Then
N(A)
=
N(Q)N≥α(A) exp({
X
β<α
xβeβ : xβ ∈B(L)})
=
N(Q)N>α(A)N≥α(Q) exp({xeα : x ∈B(L)}) exp({
X
β<α
xβeβ : xβ ∈B(L)})
=
N(Q)N>α(A) exp({xeα : x ∈B(L)}) exp({
X
β<α
xβeβ : xβ ∈B(L)})
=
N(Q)N>α(A) exp({
X
β≤α
xβeβ : xβ ∈B(L)}).
This yields the induction step. Also, for the maximal α ∈ΣP we infer that N(Q)BP (L) =
N(A).
Suppose that e ̸= γ ∈N(Q) and write γ = exp(c((λα)α∈ΣP )) with λα ∈Q. Let α be the
smallest element of ΣP such that λα ̸= 0. Then γ ∈N≥α and we have
N>α(A)γBP(L) = N>α(A) exp({λα +
X
β≤α
xβeβ : xβ ∈B(L)}).
Thus, N>α(A)γBP(L) ∩N>α(A)BP(L) = ∅and in particular, γBP(L) ∩BP(L) = ∅.
□


## Page 15


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
15
In order to apply Lemma 4.2 to the alternating sum of constant terms, we will need to
pass between partial derivatives of f ◦exp and derivatives of f for any f ∈C∞(N(A)).
This is quite standard. For any x ∈n consider the map φx : n →n given by φx(y) =
log(exp(−x) exp(x + y)). For any y ∈n we have
∂
∂y(f ◦exp)(x) = (f ∗Dφx(y))(exp x),
where Dφx is the diﬀerential of φx at 0, considered as a linear transformation from n to
itself. By the well-known formula for the diﬀerential of the exponential function we have
Dφx =
X
k≥0
(−adx)k
(k + 1)! ,
where the sum is of course ﬁnite. In other words, if for any β ∈ΣP we write pβ(y) for the
β-coordinate of y with respect to the basis (eα)α∈ΣP , and for any y ∈n we denote by ϕβ
y
the smooth function ϕβ
y(x) = pβ(Dφx(y)) on n (which is in fact a polynomial function of
the archimedean component), then
(13)
∂
∂y(f ◦exp) =
X
β∈ΣP
ϕβ
y · (f ∗eβ) ◦exp .
Note that for any α ∈ΣP and x ∈n, Dφx(eα) is contained in the span of eβ, α ≺β. Thus,
(14)
ϕβ
eα ≡0 if α ̸≺β.
Moreover,
∂ϕβ
y
∂eα
(x) =
X
k≥0
(−1)k
(k + 1)!
X
0≤j<k
(pβ ◦(adx)k−j−1 ◦adeα ◦(adx)j)(y),
and hence
(15)
∂ϕβ
y
∂eα
≡0 if α ̸≺β.
For any sequence J = (β1, . . . , βm), βi ∈ΣP , we write eJ = eβ1 · · ·eβm ∈U(n).
Lemma 4.4. For any sequence I = (α1, . . . , αl), αi ∈ΣP , we can write
(16)
∂l(f ◦exp)
Q
i ∂eαi
=
X
J
ψJ
I · (f ∗eJ) ◦exp
for any f ∈C∞(N(A)), where J ranges over the sequences (β1, . . . , βm), βi ∈ΣP, m ≤l,
such that for every 1 ≤i ≤l there exists 1 ≤j ≤m such that αi ≺βj, and the ψJ
I
are certain smooth functions on n, polynomial in the archimedean component, which are
independent of f.
Remark 4.5. The left-hand side of (16) is unchanged if we permute the αi’s. However, the
individual functions ψJ
I may depend on the order of the sequence I.


## Page 16


16
TOBIAS FINIS AND EREZ LAPID
Proof. Using induction on m and the identity (13) we have the relation (16), where
ψ∅
∅≡1, ψ∅
I ≡0 for I ̸= ∅, ψJ
∅≡0 for J ̸= ∅,
and for I = (α1, . . . , αl) and J = (β1, . . . , βm), l, m > 0, ψJ
I satisfy the recursion relations
ψJ
I =
∂ψJ
(α1,...,αl−1)
∂eαl
+ ϕβm
eαl · ψ(β1,...,βm−1)
(α1,...,αl−1) .
We ﬁrst note that using induction on the length of I and property (15) we have
∂ψJ
I
∂eα
≡0 if α ̸≺βj for all 1 ≤j ≤m.
Using this, we can now show by induction on |I| that ψJ
I ≡0 unless for every 1 ≤i ≤l
there exists 1 ≤j ≤m such that αi ≺βj. Indeed, for i < l this follows from the induction
hypothesis and for i = l this follows from (14) and the claim above.
□
Let now P1 ⊂P2 be standard parabolic subgroups. For brevity we write ξ2
1 = ξP2
P1, where
ξP2
P1 has been introduced in (6).
Proposition 4.6. There exist X1, . . . , Xm ∈U(n2
1) such that for any compact open sub-
group K1 of N1(Af) and any a ∈A0 satisfying τ 2
0 (H0(a) −T1) = 1 we have

X
P :P1⊂P ⊂P2
(−1)dim aP
X
ν∈NP
1 (Q)
Z
NP (A)
f(a−1νna) dn

≪K1
e−⟨ξ2
1,H0(a)⟩
m
X
i=1
Z
N1(A)
(f ∗Xi)(a−1na)
 dn
for any f ∈C(N1(A); K1). Moreover, if K1 contains BP1,ﬁn(L), then we may take the
implied constant to be Ls, where s is a positive integer depending only on G.
Proof. Upon replacing f by
R
N2(A) f(n·) dn and G by M2, we may assume without loss
of generality that P2 = G. We apply Lemma 4.2, taking the coordinates eα, α ∈ΣP1.
More precisely, let I = ΣP1, J = ∆0 \ ∆1
0, and for any α ∈J set Iα = ΣPα, where Pα is
the maximal parabolic subgroup of G corresponding to α. Thus, ∪α/∈∆P
0 Iα = ΣP for any
P ⊃P1. Take L to be a multiple of L0 so that K1 contains BP1,ﬁn(L). By Lemma 4.2 we
have

X
P :P1⊂P
(−1)dim aP
Z
BP (L)
f(x) dx
 =

X
P :P1⊂P
(−1)dim aP
Z
B(L)ΣP
f(exp(cP(x))) dx
 ≤
L|I| X′
I′
Z
B(L)ΣP1

∂|I′|(f ◦exp ◦cP1)
Q
α∈I′ ∂xα
(x)
 dx = L|I| X′
I′
Z
log(BP1(L))

∂|I′|(f ◦exp)
Q
α∈I′ ∂eα
(x)
 dx,


## Page 17


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
17
where the sum is over all I′ ⊂I such that for any α ∈∆0 \ ∆1
0 there exists β ∈I′ with
α ≺β. It follows from Lemma 4.4 that

X
P :P1⊂P
(−1)dim aP
Z
BP (L)
f(x) dx
 ≪Ls X′′
J
Z
BP1(L)
|(f ∗eJ)(x)| dx,
for a suitable integer s (depending only on G), where J ranges over all sequences (β1, . . . , βm),
m ≤|Σ1|, such that for any α ∈∆0 \ ∆1
0 there exists 1 ≤j ≤m with α ≺βj. Summing
over all left translates of f by ν ∈N1(Q) and using Lemma 4.3 we obtain

X
P :P1⊂P
(−1)dim aP
X
ν∈NP
1 (Q)
Z
NP (A)
f(νn) dn

≪Ls X′′
J
Z
N1(A)
|(f ∗eJ)(x)| dx.
Applying this to fa = f(a−1 · a) we obtain the required bound. Note that
fa ∗eJ(x) = (f ∗Ad(a−1)eJ)(a−1xa) =
Y
j
βj(a−1)(f ∗eJ)(a−1xa),
and that |β(a−1)| ≪1 for all β ∈ΣP by the condition on a.
□
Corollary 4.7. Let P1 ⊂P3 ⊂P2 be standard parabolic subgroups. Then there exist an
integer s and X1, . . . , Xm ∈U(g1) such that
(17)

X
P :P3⊂P ⊂P2
(−1)dim aP
X
ν∈NP
3 (Q)
Z
NP (A)
f(g−1νng) dn

≤
level(K)se−⟨ξ2
3,T⟩e−⟨(ξ2
3)P1,H0(g)−T⟩
m
X
i=1
Z
N3(A)
(f ∗Xi)(g−1ng)
 dn
for any f ∈C(G(A)1; K) and g ∈G(A)1 such that F 1(g, T)τ 2
1(HP1(g) −T) = 1.
Proof. We follow the argument of [Art78] and [Art85, §3]. As a function of g, both sides of
(17) are left P1(Q)N2(A)-invariant. Hence, we may assume that g is of the form g = namk,
where k ∈K, and a ∈A0 satisﬁes
(18)
τ 1
0 (H0(a) −T1) = 1,
n is in a ﬁxed compact subset of N2
0(A) and m is in a ﬁxed compact subset of M0(A)1. As
explained in [Art78, pp. 943–944], the condition F 1(g, T)τ 2
1(HP1(g) −T) = 1 implies that
(19)
⟨α, H0(a) −T⟩= ⟨αP1, H0(a) −T⟩+ ⟨α −αP1, H0(a) −T⟩≥⟨αP1, H0(a) −T⟩> 0
for all α ∈∆2
0 \ ∆1
0. Hence, by (18), τ 2
0 (H0(a) −T1) = 1 and a−1na lies in a ﬁxed compact
subset of N2
0(A) that is independent of T (and K). Therefore, by Lemma 2.1, part 2, we
may assume that g = a. This case follows from Proposition 4.6 (with P1 = P3) since by
(19) we have

ξ2
3, T

+

(ξ2
3)P1, H0(a) −T

≤

ξ2
3, H0(a)

.


## Page 18


18
TOBIAS FINIS AND EREZ LAPID
The corollary follows. Note that K ∩N3(Af) contains BP3,ﬁn(L) for L = L1 level(K), where
L1 is a positive integer depending only on G and the representation r0 ﬁxed in §2.3.
□
4.3.
For the application in the next section, we need another auxiliary result.
As in
[Art78, §6] let σ2
1 be the function
σ2
1 =
X
P1⊂P3⊂P2
(−1)dim a2
3τ 3
1 ˆτ3
on a0. This function is described in [ibid., Lemma 6.1 and Corollary 6.2]. In particular, σ2
1
is the characteristic function of a certain subset of a0, and if σ2
1(H) = 1 then τ 2
1 (H) = 1
and ∥H∥≤c(1 + ∥H2
1∥), where H2
1 denotes the projection of H to a2
1 and the constant c
depends only on G.
Lemma 4.8. Let P1 ⊂P3 ⊂P2 be standard parabolic subgroups. Then for any X ∈a3
1 we
have
(20)
Z
a3
σ2
1(X + X1 −T)e−⟨(ξ2
3)P1,X+X1−T⟩dX1 ≪(1 + ∥X −T P3
P1 ∥)dim a2τ 3
1 (X −T).
Proof. We write the left-hand side as
Z
a2
3
e−⟨(ξ2
3)P1,X+X1−T⟩
Z
a2
σ2
1(X + X1 + X2 −T) dX2

dX1.
By the above-mentioned property of σ2
1, the inner integral is bounded by a constant multiple
of
τ 2
1 (X + X1 −T)(1 + ∥X + X1 −T P2
P1 ∥)dim a2.
Let tβ = ⟨β, X + X1 −T⟩, β ∈∆2
1. In particular, tβ = ⟨β, X −T⟩for β ∈∆3
1. The
condition τ 2
1 (X + X1 −T) = 1 means that tβ > 0 for all β ∈∆2
1, and in particular implies
τ 3
1 (X −T) = 1. For convenience let ∆′ = ∆2
1 \ ∆3
1. Thus, the left-hand side of (20) is
≪τ 3
1 (X −T)
Z
a2
3
Y
β∈∆′
1>0(tβ)e−P
β∈∆′ tβ(1 +
X
β∈∆2
1
|tβ|)dim a2 dX1 ≤
(1 +
X
β∈∆3
1
|tβ|)dim a2τ 3
1 (X −T)
Z
a2
3
Y
β∈∆′
1>0(tβ)e−P
β∈∆′ tβ(1 +
X
β∈∆′
tβ)dim a2 dX1,
where 1>0 is the characteristic function of the positive reals. The last integral converges
since we can replace the integration variable X1 by tβ, β ∈∆′. The lemma follows.
□
Remark 4.9. We may obviously replace (ξ2
3)P1 here by any positive multiple and obtain the
same estimate (changing only the implicit constant).


## Page 19


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
19
5. Continuity of the coarse geometric expansion
We now prove the continuity of the coarse geometric expansion of Arthur’s trace formula
[Art78].
We ﬁrst recall Arthur’s derivation of this expansion.
Let for the time being
f ∈C∞
c (G(A)1). For any T ∈a0 with d(T) > d0 let kT(·, f) be Arthur’s modiﬁed kernel
(21)
kT(x, f) =
X
P ⊃P0
(−1)dim aP
X
δ∈P (Q)\G(Q)
kP(δx)ˆτP(HP(δx) −T)
with
kP(x) =
X
γ∈MP (Q)
Z
NP (A)
f(x−1γnx) dn.
The inner sum in (21) has only ﬁnitely many non-zero terms (and the possible values for
δ depend only on x, not on f). Let
JT(f) =
Z
G(Q)\G(A)1 kT(x) dx.
Arthur shows that this integral is absolutely convergent for all T with d(T) large enough,
the bound depending on the support of f.
Following [Art78, §7], we can invoke Arthur’s partition lemma (3) to rewrite (21) as
kT(x) =
X
P1⊂P2
X
δ∈P1(Q)\G(Q)
F 1(δx, T)σ2
1(HP1(δx) −T)k1,2(δx),
where
k1,2(x) =
X
P :P1⊂P ⊂P2
(−1)dim aP kP(x).
For γ1, γ2 ∈G(Q) we write γ1 ∼w γ2 if the semisimple parts of γ1 and γ2 are conjugate
in G(Q). The equivalence classes of ∼w are called coarse classes. Let ˜O be the set of all
coarse classes. Each ˜o ∈˜O contains a unique semisimple conjugacy class of G(Q). For any
˜o ∈˜O Arthur sets
k˜o(x) =
X
γ∈˜o
f(x−1γx)
and
kT
˜o (x) =
X
P ⊃P0
(−1)dim aP
X
δ∈P (Q)\G(Q)
k˜o,P(δx)ˆτP(HP(δx) −T)
with
k˜o,P(x) =
X
γ∈MP (Q)∩˜o
Z
NP (A)
f(x−1γnx) dn.
A basic fact [Art78, p. 923] is that
(22)
˜o ∩P(Q) = (˜o ∩M(Q))N(Q).


## Page 20


20
TOBIAS FINIS AND EREZ LAPID
Clearly, we have
kT(x) =
X
˜o∈˜O
kT
˜o (x).
The integrals
JT
˜o (f) =
Z
G(Q)\G(A)1 kT
˜o (x) dx
are again absolutely convergent for d(T) large enough (depending on the support of f) and
we have the decomposition JT(f) = P
˜o∈˜O JT
˜o (f) for all such T.
Exactly as before, we can write
(23)
kT
˜o (x) =
X
P1⊂P2
X
δ∈P1(Q)\G(Q)
F 1(δx, T)σ2
1(HP1(δx) −T)k˜o,1,2(δx),
where
k˜o,1,2(x) =
X
P :P1⊂P ⊂P2
(−1)dim aP k˜o,P(x).
We now extend Arthur’s convergence results as follows.
Theorem 5.1.
(1) For any f ∈C(G(A)1; K), ˜o ∈˜O and T ∈a0 such that d(T) > d0,
the integrals deﬁning JT (f) and JT
˜o (f) are absolutely convergent.
(2) JT(f) and JT
˜o (f) are polynomials in T of degree ≤dim a0 whose coeﬃcients are
continuous linear forms in f.
(3) There exist r ≥0 and a continuous seminorm µ on C(G(A)1; K) such that
X
˜o∈˜O

Z
G(Q)\G(A)1
≤T
k˜o(x) dx −JT
˜o (f)
 ≤
X
˜o∈˜O
Z
G(Q)\G(A)1
F(x, T)k˜o(x) −kT
˜o (x)
 dx
≤µ(f)(1 + ∥T∥)re−d(T)
for any f ∈C(G(A)1; K) and T such that d(T) > d0.
(4) JT(f) = P
˜o∈˜O JT
˜o (f).
In addition, the absolute values of the coeﬃcients in part 2 and the seminorm µ of part
3 can be bounded by c level(K)s∥·∥G(A)1, t for a constant c and positive integers s, t that do
not depend on K.
Proof. First note that each kP(x), and hence the modiﬁed kernel kT(f), is well-deﬁned for
any f ∈C(G(A)1; K) by Lemma 2.1. Also, by (8) there exist r ≥0 and a continuous
seminorm µ on C(G(A)1; K) such that
X
˜o∈˜O
Z
G(Q)\G(A)1
≤T
|k˜o(x)| dx ≤µ(f)(1 + ∥T∥)r
for any f ∈C(G(A)1; K) and T such that d(T) > d0. It follows that part 3 implies the
convergence of JT (f) and JT
˜o (f), as well as the relation JT(f) = P
˜o∈˜O JT
˜o (f). Moreover,
Arthur’s argument in [Art81, §2] shows that part 2 is valid for any f for which JT(f) (or
JT
˜o (f)) is absolutely convergent.


## Page 21


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
21
Thus, it remains to prove part 3. Following [Art78, §7] (and recalling (22)) we can write
k˜o,1,2(x) =
X
P1⊂P3⊂P2
k˜o,1,2;3(x),
where
k˜o,1,2;3(x) =
X
η∈M3(Q)◦
1∩˜o
X
P :P3⊂P ⊂P2
(−1)dim aP
X
ν∈NP
3 (Q)
Z
NP (A)
f(x−1ηνnx) dn
with the deﬁnition
M3(Q)◦
1 = M3(Q) \ ∪P :P1⊂P ⊊P3P(Q).
As a side remark, we note that Arthur shows in [ibid., pp. 943–944], that for compactly
supported f only the terms with P3 = P1 contribute, provided that T is large with respect
to the support of f.
The function k˜o,1,2;3 is left P1(Q)N2(A)-invariant, since the set M3(Q)◦
1 is invariant un-
der conjugation by P1(Q). Recall the decomposition (23) of kT
˜o (x), and observe that σP
P
vanishes identically unless P = G and that the contribution from P1 = P2 = G to (23) is
simply F(x, T)k˜o(x). In order to prove part 3, it therefore suﬃces to show that there exist
r ≥0 and a continuous seminorm µ on C(G(A)1; K) such that for any triplet P1 ⊂P3 ⊂P2
with P1 ̸= P2 we have
X
˜o
Z
P1(Q)\G(A)1 F 1(x, T)σ2
1(HP1(x) −T) |k˜o,1,2;3(x)| dx ≤µ(f)(1 + ∥T∥)re−⟨ξ2
1,T⟩.
By Corollary 4.7 (applied to suitable left translates of f), we have
|k˜o,1,2;3(x)| ≤e−⟨ξ2
3,T⟩e−⟨(ξ2
3)P1,H0(x)−T⟩X
i
X
η∈M3(Q)◦
1∩˜o
Z
N3(A)
(f ∗Xi)(x−1ηnx)
 dn,
provided that F 1(x, T)σ2
1(HP1(x) −T) = 1. Since ξ2
1 = ξ3
1 + ξ2
3, it remains to show that
Z
P1(Q)\G(A)1 F 1(x, T)σ2
1(HP1(x) −T)e−⟨(ξ2
3)P1,H0(x)−T⟩
X
η∈M3(Q)◦
1
Z
N3(A)
f(x−1ηnx)
 dn dx
≤µ(f)(1 + ∥T∥)re−⟨ξ3
1,T⟩
with a suitable continuous seminorm µ. At this point we note that using Lemma 2.1, part
3, we may assume without loss of generality that f ≥0 and K = Kﬁn. Using the Iwasawa
decomposition with respect to P3, we need to estimate
Z
P 3
1 (Q)\M3(A)∩G(A)1 e−⟨(ξ2
3)P1,H0(x)−T⟩F 1(x, T)σ2
1(HP1(x) −T)
X
η∈M3(Q)◦
1
fP3(x−1ηx) dx,
where P 3
1 = P1 ∩M3, and fP3 is as in (5). Splitting M3(A) ∩G(A)1 as the direct product
of AM3 and M3(A)1, we may estimate the integral over AM3 using Lemma 4.8. The above


## Page 22


22
TOBIAS FINIS AND EREZ LAPID
integral is then majorized by a constant multiple of
Z
P 3
1 (Q)\M3(A)1 F 1(x, T)(1 + ∥HP1(x) −T P3
P1 ∥)dim a2τ 3
1 (HP1(x) −T)
X
η∈M3(Q)◦
1
fP3(x−1ηx) dx.
We can now appeal to Theorem 3.1 (with G = M3 and P = P 3
1 ) and Lemma 2.1, part 4,
to ﬁnish the proof.
□
6. Modifications for the finer classes
In this section we will ﬁne-tune the results of §4 to adapt the continuity argument to
the decomposition of the trace formula with respect to the equivalence relation ∼of the
introduction instead of ∼w. The goal is to prove Corollary 6.11 below, which is the main
technical prerequisite for the continuity argument in §7.
6.1.
We ﬁrst go back to the situation of Lemmas 4.1 and 4.2. Namely, I is a ﬁnite set and
Ij, j ∈J, is a family of (not necessarily disjoint) non-empty subsets of I. We also have
an integer parameter L ≥1. Recall that for any J′ ⊂J we denote by [0, L]I
J′ the face of
[0, L]I consisting of the vectors whose support is contained in ∪j /∈J′Ij.
We say that a family F of subsets of J is monotone if whenever J′ ∈F and J′ ⊂J′′ ⊂J,
we also have J′′ ∈F.
Lemma 6.1. Let F be a monotone family of subsets of J and let Fmin be the set of minimal
elements of F with respect to inclusion. Then there exist coeﬃcients dI′ ∈Z, depending
only on F, such that for any f ∈C|I|([0, L]I) we have
(24)
X
J′∈F
(−1)|J\J′|
Z
[0,L]I
J′
f(x) dx =
X′′
I′
dI′
Z
[0,L]I
∂|I′|f
Q
i∈I′ ∂xi
(x)
Y
i∈I′
(xi −L) dx,
where the sum is over all I′ ⊂I such that I′ ∩Ij ̸= ∅for every j ∈J \ ∪Fmin.
Proof. This is a special case of (10) with
cI′ =
X
J′∈F:∪j /∈J′Ij=I\I′
(−1)|J0\J′|.
Note that
dI′ =
X
I′′⊃I′
cI′′ =
X
J′∈F:∪j /∈J′Ij⊂I\I′
(−1)|J0\J′| =
X
{j∈J:Ij∩I′̸=∅}⊂J′∈F
(−1)|J0\J′|.
Observe that if j0 ∈J \ ∪Fmin then for any J′ ⊂J, J′ ∈F if and only if J′ ∪{j0} ∈F.
Similarly, if I′ ∩Ij0 = ∅then for any J′ ⊂J, {j ∈J : Ij ∩I′ ̸= ∅} ⊂J′ if and only if
{j ∈J : Ij ∩I′ ̸= ∅} ⊂J′ ∪{j0}. Thus, dI′ = 0 if there exists j0 ∈J \ ∪Fmin such that
I′ ∩Ij0 = ∅, as required.
□
Once again, an adelic version follows immediately.


## Page 23


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
23
Corollary 6.2. Let I, Ij, j ∈J, and F be as in Lemma 6.1 above. Then we have (using
the notation of Lemma 4.2)

X
J′∈F
(−1)|J′|
Z
B(L)I
J′
f(x) dx
 ≪F L|I| X′′
I′
Z
B(L)I

∂|I′|f
Q
i∈I′ ∂xi
(x)
 dx
for any f ∈C|I|(AI; Bﬁn(L)I).
We say that a non-empty family P of parabolic subgroups of G is monotone if whenever
Q ∈P and Q′ ⊃Q, we also have Q′ ∈P. For a monotone family P let Pmin be the set of
minimal elements of P (with respect to inclusion) and let Q(P) be the parabolic subgroup
generated by the elements of Pmin.
Corollary 6.3. Let P be a standard parabolic subgroup. Let P be a monotone family of par-
abolic subgroups of G which all contain P. Then there exist an integer s and X1, . . . , Xm ∈
U(n) such that for any L divisible by L0 and a ∈A0 satisfying τ0(H0(a) −T1) = 1 we have
X
ν∈N(Q)

X
Q∈P
(−1)dim aQ
Z
BQ(L)
f(a−1νna) dn

≤Lse−⟨ξQ(P),H0(a)⟩
m
X
i=1
Z
N(A)
(f ∗Xi)(a−1na)
 dn
for every f ∈C(N(A); BP,ﬁn(L)).
Proof. This follows from Corollary 6.2 exactly as in the proof of Proposition 4.6. Recall
that I = ΣP , J = ∆0\∆P
0 and that Iα = ΣPα for α ∈J, where Pα is the maximal parabolic
subgroup of G corresponding to α. In the case at hand we have F = {∆Q
0 \ ∆P
0 : Q ∈P}
and Fmin = {∆Q
0 \ ∆P
0 : Q ∈Pmin}, and therefore ∆Q(P)
0
\ ∆P
0 = ∪Fmin.
□
6.2.
The following is a version of [CL16, Proposition 5.3.1].
Lemma 6.4. Let a1, . . . , an ∈R∗and let α : An →An be the A-linear transformation
given by α(x1, . . . , xn) = (a1x1, . . . , anxn). Fix a constant c > 0 and assume that |aj| ≤c
for all j. Then for a non-zero polynomial φ ∈Q[x1, . . . , xn] we have
(25)
X
v∈Qn:φ(v)=0
|f(α(v))| ≪c,n Ln deg φ max |aj|
X
I⊂{1,...,n}
Z
An

∂|I|f
Q
i∈I ∂xi
(α(v))
 dv
for any f ∈C(An; Bﬁn(L)n).
Proof. Note ﬁrst that the bound
(26)
X
v∈Qn
|f(α(v))| ≪c,n Ln
X
I⊂{1,...,n}
Z
An

∂|I|f
Q
i∈I ∂xi
(α(v))
 dv
follows already from Lemma 2.1, part 1.


## Page 24


24
TOBIAS FINIS AND EREZ LAPID
Let d = deg φ. We prove the lemma by induction on n. In the case n = 1, (25) follows
from the inequality
sup |f| ≤L(∥f∥L1(A) + ∥f ′∥L1(A)),
and the fact that the number of roots of φ is at most d.
For the induction step, we write
φ(x1, . . . , xn) =
d
X
i=0
φi(x1, . . . , xn−1)xi
n,
where at least one of the polynomials φi, say φi0, is non-zero. Let p : Qn →Qn−1 be the
projection to the ﬁrst n −1 coordinates. We split the sum on the left-hand side of (25)
into two according to whether or not φi0(p(v)) = 0. The ﬁrst sum is bounded by
X
v′∈Qn−1:φi0(v′)=0
X
xn∈Q
|f(α(v′, xn))|
which is majorized by
L
X
v′∈Qn−1:φi0(v′)=0
Z
A
 |f(α(v′, xn))| +

∂f
∂xn
(α(v′, xn))


dxn,
to which we can apply the induction hypothesis. The second sum is
X
v′∈Qn−1:φi0(v′)̸=0
X
xn∈Q:φ(v′,xn)=0
|f(α(v′, xn))| .
By the case n = 1, the inner sum is bounded by
≪c Ld |an|
Z
A
 |f(α(v′, xn))| +

∂f
∂xn
(α(v′, xn))


dxn,
since φ(v′, xn) is a non-zero polynomial in xn of degree ≤d if φi0(v′) ̸= 0. We can now use
(26) for the ﬁrst n −1 variables to bound the sum over v′, no longer using the condition
φi0(v′) ̸= 0.
□
Corollary 6.5. Let P be a maximal parabolic subgroup of G with ∆0 \ ∆P
0 = {α}. Then
there exist X1, . . . , Xm ∈U(n) such that for any non-zero polynomial φ on n of degree ≤d
and any compact open subgroup K′ of N(Af) we have
X
n∈N(Q):φ(log n)=0
f(a−1na)
 ≪K′ d e−⟨α,H0(a)⟩
m
X
i=1
Z
N(A)
(f ∗Xi)(a−1na)
 dn
for any f ∈C(N(A); K′) and a ∈A0 such that τ0(H0(a) −T1) = 1. Moreover, if K′
contains BP,ﬁn(L), then we may take the implied constant to be Ls, where s is a positive
integer depending only on G.
Proof. This immediately follows from Lemma 6.4 and Lemma 4.4.
Note that for any
β ∈ΣP we have ⟨β, H0(a)⟩≥⟨α, H0(a)⟩−C for some constant C (depending on T1).
□


## Page 25


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
25
6.3.
We recollect some known facts about the “parabolic induction” of conjugacy classes `a
la Lusztig-Spaltenstein [LS79]. In the current setup this notion was considered by Hoﬀmann
[Hof12].
Let P = M ⋉N be a parabolic subgroup of G (deﬁned over Q) and let γ ∈M. As
explained in [Hof12], there exists a unique conjugacy class IP(γ) = IG
P(γ) of G which
intersects γN in a Zariski open dense set. This follows from the fact that there are only
ﬁnitely many conjugacy classes of G intersecting γN and that each conjugacy class is a
locally closed subvariety. If γ ∈M(Q) then IP(γ) is deﬁned over Q and we let IP(γ) =
IP(γ) ∩˜oγ where ˜oγ is the coarse class of γ in G(Q). Note that IP(γ) is non-empty (and
consists of a union of conjugacy classes of G(Q)) since it contains the rational points of a
dense Zariski open subset of γN. (We recall that γN(Q) ⊂˜oγ.) More generally, if Q ⊃P
we will write IQ
P (γ) = I
MQ
P ∩MQ(γ) and similarly for IQ
P (γ) (if γ ∈MP(Q)). It will also be
convenient to set IQ
P(γ) = IQ
P (γM) for any γ ∈P, where γM is the projection of γ to M,
and to deﬁne IQ
P (γ) similarly if γ ∈P(Q).
Let γ ∈P and suppose that Q is a parabolic subgroup of G containing P. Induction is
transitive in the sense that if Q ⊃P and η ∈IQ
P(γ) then IQ(η) = IP(γ) (see [LS79]). Thus,
(27)
if γ ∈P(Q) and η ∈IQ
P (γ) then IQ(η) = IP(γ).
Another simple property is that if δ ∈[γ]M, where [γ]M is the conjugacy class of γ in M,
then
(28)
IP(δ) ⊂IP(γ).
Indeed, IP(γ) ⊃[γ]MN ⊃[γ]MN ⊃δN and IP(δ) ∩δN ̸= ∅. It follows from the two
properties above that
(29)
IQ(γ) ⊂IP(γ) for Q ⊃P,
since γ ∈IQ
P(γ).
We will need an additional qualitative property pertaining to induced classes. By the
deﬁnition of IP(γ), for each γ ∈M there exists a non-zero regular function Fγ on N which
vanishes on the complement of γ−1IP(γ) in N.
Lemma 6.6. We may choose Fγ so that the degree of the polynomial function Fγ ◦exp on
n is bounded in terms of G only.
Let γs (resp., γu) be the semisimple (resp., unipotent) part of γ in the Jordan–Chevalley
decomposition. Denote by Nγs the centralizer of γs in N. In order to prove Lemma 6.6, we
use the following result of Arthur on algebraic groups. (We have already used it implicitly
when quoting relation (22).)
Lemma 6.7. ([Art78, Lemma 2.1]) For any n ∈N there exists u ∈N, unique up to
left translation by Nγs, such that uγnu−1 ∈γNγs. The map n 7→u deﬁnes a morphism
qγ : N →Nγs\N of aﬃne varieties. Moreover, if γ ∈M(Q) then qγ is deﬁned over Q.


## Page 26


26
TOBIAS FINIS AND EREZ LAPID
We will need to know that in a suitable sense qγ is algebraic in γ. Before making this more
precise we prove another lemma. Let Gγs (resp., Pγs, Mγs) be the connected component
of the identity of the centralizer of γs in G (resp., P, M). It is well known that Pγs is a
parabolic subgroup of Gγs with Levi decomposition Pγs = Mγs ⋉Nγs.
Lemma 6.8. Let n ∈N and suppose that there exists u ∈N such that γ−1uγnu−1 ∈
Nγs ∩γ−1
u IGγs
Pγs (γu). Then n ∈γ−1IP(γ).
Proof. The set Xγ := γ−1IP(γ) ∩Nγs is non-empty and Zariski open in Nγs, since if
γn ∈IP(γ) then by Lemma 6.7 there exists u ∈N such that u−1γnu ∈γNγs. Therefore
Xγ intersects non-trivially the Zariski open and dense set Yγ := γ−1
u IGγs
Pγs (γu) ∩Nγs of Nγs.
Let z ∈Xγ ∩Yγ. Then for any y ∈Yγ there exists g ∈Gγs such that γuy = g−1γuxg. Thus
γy = g−1γzg and hence y ∈Xγ. It follows that Yγ ⊂Xγ, hence the lemma.
□
Proof of Lemma 6.6. Fix a Borel subgroup B ⊂P of G (so that its unipotent radical U
contains N) and a maximal torus S of G contained in B ∩M. (Of course S, B and U
are not necessarily deﬁned over Q.) Let R(S, N) be the set of roots of S in N. For any
subset I of R(S, N) let XI be the aﬃne subvariety of B ∩M consisting of the elements
γ such that γs ∈S and I = {α ∈R(S, N) : α(γs) = 1}. Also, let NI be the subgroup
of N generated by the root subgroups corresponding to the roots in I. Then Nγs = NI if
γ ∈XI. The proof of [Art78, Lemma 2.1] shows that (γ, n) 7→qγ(n) deﬁnes a regular map
qI : XI × N →NI\N.
For completeness we provide the details, since the setup of [Art78, Lemma 2.1] is slightly
diﬀerent. Let N = U0 ⊃· · · ⊃Ur = 0 be a sequence of subgroups of N normalized by
B, such that for all i = 0, . . . , r −1, Ui/Ui+1 ≃Ga and [Ui, U] ⊂Ui+1. We claim that for
every i there exists a morphism qi : XI × N →UiNI\N of aﬃne varieties characterized by
the property that
γ−1qi(γ, n)γnqi(γ, n)−1 ∈UiNI for any γ ∈XI, n ∈N.
The case i = r is then the sought-after result. We argue by induction on i. The assertion
is trivial for i = 0. For the induction step, assume that qi is deﬁned for some i < r.
Let αi be the root corresponding to Ui/Ui+1.
If αi ∈I then UiNI = Ui+1NI and we
simply take qi+1 = qi.
Otherwise, ﬁxing u ∈N such that x := γ−1uγnu−1 ∈UiNI
we need to show that there exists v ∈Ui, uniquely determined modulo Ui+1, such that
yv := γ−1vuγnu−1v−1 ∈Ui+1NI. Note that
yv = γ−1vγxv−1 = γ−1vγv−1x[x−1, v] = γ−1
s vγs · γ−1
s [v−1, γ−1
u ]γs · v−1x[x−1, v]
so that
yv ∈[γ−1
s , v]xUi+1.
The map v 7→[γ−1
s , v] induces an isomorphism of Ui/Ui+1 which under the identiﬁcation
with Ga is given by multiplication by αi(γs) −1. Thus qi+1 is deﬁned and it is clearly a
morphism (by choosing an algebraic section UiNI\N →N for the quotient map). This
ﬁnishes the construction of qI.


## Page 27


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
27
Fix an algebraic section sI : NI\N →N for the canonical projection N →NI\N such
that sI(NI) = e. Let
κI : XI × N →NI
be the regular map given by
κI(γ, n) = γ−1sI(qI(γ, n))γnsI(qI(γ, n))−1.
For any γ ∈XI, the map κI(γ, ·) : N →NI is surjective, since its restriction to NI is the
identity map.
We can now conclude Lemma 6.6. For any subset J of R(S, U) let YJ be the subvariety
of B ∩M consisting of elements γ such that γs ∈S and J = {α ∈R(S, U) : α(γs) = 1}.
Thus, YJ ⊂XI for I = J ∩R(S, N). Upon conjugating γ by an element of M we may
assume without loss of generality that γ ∈YJ for some J. Let GJ (resp., PJ; MJ) be the
subgroup of G (resp., P; M) generated by S and the root subgroups corresponding to J
and −J (resp., J and −(J ∩R(S, U ∩M)); ±(J ∩R(S, U ∩M))). Thus, GJ = Gγs, PJ = Pγs,
MJ = Mγs and PJ is a parabolic subgroup of GJ with Levi decomposition PJ = MJ ⋉NI.
(Recall that NI = Nγs.) Since there are only ﬁnitely many unipotent conjugacy classes in
MI, we may regard γu (as well as J) as ﬁxed. By Lemma 6.8, γn ∈IP(γ) if for some u ∈N
we have γ−1uγnu−1 ∈NI ∩γ−1
u IGJ
PJ (γu). Thus, n ∈γ−1IP(γ) if κI(γ, n) ∈(γu)−1IGJ
PJ (γu).
Hence, if we choose a non-zero regular function f on NI which vanishes on the complement
of (γu)−1IGJ
PJ (γu) in NI then we can take Fγ = f ◦κI(γ, ·). Lemma 6.6 follows.
□
6.4.
The following result is modeled after [CL16, §6]. For standard parabolic subgroups
P1 ⊂P2 of G deﬁne
˜ξ2
1 =
(
ξ2
1
dim a2
1,
P1 ⊊P2,
0,
otherwise.
Proposition 6.9. Let P1 ⊂P2 be standard parabolic subgroups of G. There exist X1, . . . , Xm ∈
U(n2
1), such that for a closed subvariety V of G, a compact open subgroup K1 of N1(Af)
and an element η ∈M1(Q) we have
(30)

X
P :P1⊂P ⊂P2
(−1)dim aP
X
ν∈NP
1 (Q):IP (ην)⊂V
Z
NP (A)
f(a−1νna) dn

≪K1
e−⟨˜ξ2
1,H0(a)⟩
m
X
i=1
Z
N1(A)
(f ∗Xi)(a−1na)
 dn
for any f ∈C(N1(A); K1) and a ∈A0 such that τ 2
0 (H0(a) −T1) = 1. Moreover, if K1
contains BP1,ﬁn(L), then we may take the implied constant to be Ls, where s is a positive
integer depending only on G.
Proof. We ﬁrst remark that the condition IP(ην) ⊂V is equivalent to IP(ην) ⊂V , since
for any γ ∈G(Q) the conjugacy class of γ in G(Q) is Zariski dense in the conjugacy class
of γ in G. Also, the condition IP(ην) ⊂V is equivalent to IP2
P (ην) ⊂V ′, where
V ′ = {δ ∈M2 : IP2(δ) ⊂V },


## Page 28


28
TOBIAS FINIS AND EREZ LAPID
which is a closed subvariety of M2 by (28).
We may therefore, after replacing f by
R
N2(A) f(n·) dn, assume without loss of generality that P2 = G.
For any ν ∈N1(Q) let
P(ν) = {P ⊃P1 : IP(ην) ⊂V } = {P ⊃P1 : IP(ην) ⊂V }.
Note that by (29), P(ν) is monotone. Recall that in Lemma 4.3 we have constructed
for any standard parabolic subgroup P of G a family of fundamental domains BP(L) for
NP(Q)\NP(A). Let L be a positive integer such that BP1,ﬁn(L) is a subgroup of K1. Let
P be a monotone family of parabolic subgroups of G which contain P1 and consider
A(P) =
X
ν∈N1(Q):P(ν)=P
X
P ∈P
(−1)dim aP
Z
BP (L)
f(a−1νna) dn.
Then the left-hand side of (30) is equal to |P A(P)|, where P ranges over all monotone
families. Thus, in order to prove the proposition it suﬃces to show that there exist suitable
Xi and s such that
(31)
|A(P)| ≤Lse−⟨α,H0(a)⟩
m
X
i=1
Z
N1(A)
(f ∗Xi)(a−1na)
 dn
for any α ∈∆2
0 \ ∆1
0. Recall the notation Q(P) for the parabolic subgroup generated by
the inclusion-minimal elements of P. To show (31), we distinguish two cases for α. If
α /∈∆Q(P)
0
then (31) follows from Corollary 6.3. For α ∈∆Q(P)
0
, we will show in fact that
(32)

X
ν∈N1(Q):P(ν)=P
f(a−1νa)

≤Ls′e−⟨α,H0(a)⟩
m
X
i=1
Z
N1(A)
(f ∗Xi)(a−1na)
 dn
for all P ⊃P1. From this we obtain (with possibly diﬀerent diﬀerential operators Xi) the
estimate
(33)

X
ν∈N1(Q):P(ν)=P
Z
BP (L)
f(a−1νna) dn

≤Lse−⟨α,H0(a)⟩
m
X
i=1
Z
N1(A)
(f ∗Xi)(a−1na)
 dn,
which in turn implies (31) for such α. To derive (33) from (32), we apply the latter for each
n ∈BP(L) to the right translate ˜f of f by a−1na. The sets a−1BP (L)a for all possible a are
contained in a compact subset of NP(A) of the form Ω∞BP,ﬁn(L), where the coordinates
of the elements of log(Ω∞) are bounded linearly in L. Therefore ˜f ∈C(N1(A); BP1,ﬁn(L)),
and the coordinates of Ad(a−1na)Xi with respect to a ﬁxed basis of U(n) are bounded
polynomially in L. Thus, (33) follows from (32).
To show (32), let R ∈Pmin be such that α ∈∆R
0 and let S be the standard parabolic
subgroup of G such that ∆S
0 = ∆R
0 \ {α}. Thus, P1 ⊂S ⊊R. We claim that the left-hand
side of (32) is majorized by
(34)
X
ν1∈NS
1 (Q)
X
ν2∈NR
S (Q):ην1ν2 /∈IR
S (ην1)
X
ν3∈NR(Q)
f(a−1ν1ν2ν3a)
 .


## Page 29


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
29
Indeed, if P(ν1ν2ν3) = P then ην1ν2 /∈IR
S(ην1), for otherwise, by (27) we would have
IS(ην1ν2ν3) = IS(ην1) = IR(ην1ν2) = IR(ην1ν2ν3),
in contradiction to the minimality of R (cf. [CL16, Lemme 6.7.5]).
Using Lemma 3.3, we bound the inner sum in (34) by
Ls1 X
i
Z
NR(A)
(f ∗X′
i)(a−1ν1ν2n3a)
 dn3
for suitable X′
1, . . . , X′
m′ ∈U(nR). By Corollary 6.5 and Lemma 6.6 we can now bound the
sum over ν2 in (34) by
Ls2e−⟨α,H0(a)⟩X
i
Z
NS(A)
(f ∗X′′
i )(a−1ν1n2a)
 dn2
for suitable X′′
1 , . . . , X′′
m′′ ∈U(nS). Using Lemma 3.3 once again, we bound (34) by the
right-hand side of (32), as required.
□
The following corollary follows from this proposition exactly like Corollary 4.7 follows
from Proposition 4.6.
Corollary 6.10. Let P1 ⊂P3 ⊂P2 be standard parabolic subgroups of G. There exist
an integer s and X1, . . . , Xm ∈U(g1) such that for any closed subvariety V of G and
η ∈M3(Q) we have
(35)

X
P :P3⊂P ⊂P2
(−1)dim aP
X
ν∈NP
3 (Q):IP (ην)⊂V
Z
NP (A)
f(g−1νng) dn

≤
level(K)se−⟨˜ξ2
3,T⟩e−⟨(˜ξ2
3)P1,H0(g)−T⟩
m
X
i=1
Z
N3(A)
(f ∗Xi)(g−1ng)
 dn
for any f ∈C(G(A)1; K) and g ∈G(A)1 such that F 1(g, T)τ 2
1(HP1(g) −T) = 1.
Recall the equivalence relation ∼on G(Q) introduced in the introduction: for γ, δ ∈
G(Q) we write γ ∼δ if γ ∼w δ and γ and δ are conjugate in G(Q). Let O be the set of
equivalence classes of ∼.
Let o = ˜o∩C be an equivalence class of ∼, where ˜o is a coarse class and C is a geometric
conjugacy class of G, and let C be the Zariski closure of C. Applying Corollary 6.10 to
the closed varieties V = C and V = C \ C and subtracting, we obtain:


## Page 30


30
TOBIAS FINIS AND EREZ LAPID
Corollary 6.11. Let P1 ⊂P3 ⊂P2 be standard parabolic subgroups of G. There exist an
integer s and X1, . . . , Xm ∈U(g1) such that for any η ∈M3(Q) and o ∈O we have
(36)

X
P :P3⊂P ⊂P2
(−1)dim aP
X
ν∈NP
3 (Q):IP (ην)=o
Z
NP (A)
f(g−1νng) dn

≤
level(K)se−⟨˜ξ2
3,T⟩e−⟨(˜ξ2
3)P1,H0(g)−T⟩
m
X
i=1
Z
N3(A)
(f ∗Xi)(g−1ng)
 dn
for any f ∈C(G(A)1; K) and g ∈G(A)1 such that F 1(g, T)τ 2
1(HP1(g) −T) = 1.
7. The main result
We are now ready to prove the continuity of the decomposition of the geometric side with
respect to the equivalence relation ∼. Observe that if σ ∈G(Q) is semisimple then the
equivalence classes with respect to ∼in the coarse class of σ are indexed by the geometric
unipotent conjugacy classes of the centralizer of σ containing a rational point. In particular,
(37)
the number of equivalence classes of ∼in a coarse class is bounded in terms of G only.
Following [CL16, Hof14], we deﬁne for any o ∈O
ko(x) =
X
γ∈o
f(x−1γx)
and
kT
o (x) =
X
P ⊃P0
(−1)dim aP
X
δ∈P (Q)\G(Q)
ko,P(δx)ˆτP(HP(δx) −T),
where
ko,P(x) =
X
γ∈MP (Q):IP (γ)=o
Z
NP (A)
f(x−1γnx) dn.
Let
JT
o (f) =
Z
G(Q)\G(A)1 kT
o (x) dx.
Exactly as before, we can write
kT
o (x) =
X
P1⊂P2
X
δ∈P1(Q)\G(Q)
F P1(δx, T)σ2
1(HP1(δx) −T)ko,1,2(δx),
where
ko,1,2(x) =
X
P :P1⊂P ⊂P2
(−1)dim aP ko,P(x).
Clearly,
kT(x) =
X
o∈O
kT
o (x).


## Page 31


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
31
Theorem 7.1. The analogue of Theorem 5.1 holds for the integrals JT
o (f), o ∈O, instead
of JT
˜o (f), ˜o ∈˜O.
Proof. The proof is very similar to that of Theorem 5.1. The main task is to prove the
analogue of part 3 for the integrals JT
o (f). We write as before
ko,1,2(x) =
X
P1⊂P3⊂P2
ko,1,2;3(x),
where ko,1,2;3 is the left P1(Q)N2(A)-invariant function given by
ko,1,2;3(x) =
X
η∈M3(Q)◦
1
X
P :P3⊂P ⊂P2
(−1)dim aP
X
ν∈NP
3 (Q):IP (ην)=o
Z
NP (A)
f(x−1ηνnx) dn.
We show that there exist r ≥0 and a continuous seminorm µ on C(G(A)1; K), such that
for any triplet P1 ⊂P3 ⊂P2 with P1 ̸= P2 we have
X
o
Z
P1(Q)\G(A)1 F 1(x, T)σ2
1(HP1(x) −T) |ko,1,2;3(x)| dx ≤µ(f)(1 + ∥T∥)re−d(T).
For that we use Corollary 6.11 (applied to suitable left translates of f) to obtain
|ko,1,2;3(x)| ≤e−⟨˜ξ2
3,T⟩e−⟨(˜ξ2
3)P1,H0(x)−T⟩X
i
X
η∈M3(Q)◦
1∩˜o
Z
N3(A)
(f ∗Xi)(x−1ηnx)
 dn,
provided that F 1(x, T)σ2
1(HP1(x)−T) = 1, where ˜o is the coarse class containing o. Taking
into account Remark 4.9 and (37), the rest of the argument proceeds as in the proof of
Theorem 5.1.
□
We continue to write JT
o (f) for the value at T of the polynomial JT
o (f), even if d(T) ≤d0.
Corollary 7.2. For any T ∈a0,
f 7→
X
o∈O
JT
o (f)

is a continuous seminorm on C(G(A)1). On C(G(A)1; K) this seminorm is bounded by
c(T) level(K)s∥·∥G(A)1, t for a constant c(T) and positive integers s, t that do not depend on
K.
Proof. By extrapolation, it is enough to prove this for d(T) > d0.
The claim follows
immediately from Theorem 7.1 and the fact (see (8)) that
X
˜o∈˜O
Z
G(Q)\G(A)1
≤T
|k˜o(x)| dx
is a continuous seminorm on C(G(A)1; K).
□


## Page 32


32
TOBIAS FINIS AND EREZ LAPID
Remark 7.3. Motivated by [Art86, §8], we may consider instead of the equivalence relation
∼on G(Q), the slightly ﬁner relation γ ∼′ δ if δ = gγg−1 for some g ∈G(Q)Gγs(Q). Thus,
the ∼′-classes in the coarse class of a semisimple element σ ∈G(Q) are indexed by the
geometric unipotent classes of Gσ containing a rational point. In particular, in the case
where Gder is simply connected, ∼′ coincides with ∼, since the centralizers of semisimple
elements are then connected (cf. [Kot82, pp. 788–789]). In general, Theorem 7.1 continues
to hold for the classes of ∼′. The proof is identical except that in the case at hand IG
P (γ)
will be deﬁned to be the ∼′-class of an element of γsIGγs
Pγs (γu). In practice, this reﬁnement
is not very essential, since in most applications of the trace formula we can reduce to the
case where Gder is simply connected by considering a z-extension of G.
References
[Art78]
James G. Arthur, A trace formula for reductive groups. I. Terms associated to classes in G(Q),
Duke Math. J. 45 (1978), no. 4, 911–952. MR 518111 (80d:10043)
[Art81]
James Arthur, The trace formula in invariant form, Ann. of Math. (2) 114 (1981), no. 1, 1–74.
MR 625344 (84a:10031)
[Art85]
, A measure on the unipotent variety, Canad. J. Math. 37 (1985), no. 6, 1237–1274.
MR 828844 (87m:22049)
[Art86]
, On a family of distributions obtained from orbits, Canad. J. Math. 38 (1986), no. 1,
179–214. MR 835041 (87k:11058)
[BCS14] Alexis Bouthier, Ngo Bao Chau, and Yiannis Sakellaridis, On the formal arc space of a reductive
monoid, 2014, arXiv:1412.6174.
[Cha]
Pierre-Henri Chaudouard, Sur la contribution unipotente dans la formule des traces d’Arthur
pour les groupes g´en´eraux lin´eaires, Israel J. Math. to appear, arXiv:1411.3005.
[Cha15]
, Sur certaines contributions unipotentes dans la formule des traces d’Arthur, 2015,
arXiv:1510.02783.
[CL16]
Pierre-Henri Chaudouard and G´erard Laumon, Sur le comptage des ﬁbr´es de Hitchin nilpotents,
J. Inst. Math. Jussieu 15 (2016), no. 1, 91–164. MR 3427596
[FL11]
Tobias Finis and Erez Lapid, On the continuity of Arthur’s trace formula: the semisimple terms,
Compos. Math. 147 (2011), no. 3, 784–802. MR 2801400 (2012d:11120)
[FLM11] Tobias Finis, Erez Lapid, and Werner M¨uller, On the spectral side of Arthur’s trace formula—
absolute convergence, Ann. of Math. (2) 174 (2011), no. 1, 173–195. MR 2811597
[FLN10] Edward Frenkel, Robert Langlands, and B´ao Chˆau Ngˆo, Formule des traces et fonctorialit´e:
le d´ebut d’un programme, Ann. Sci. Math. Qu´ebec 34 (2010), no. 2, 199–243. MR 2779866
(2012c:11240)
[GJ72]
Roger Godement and Herv´e Jacquet, Zeta functions of simple algebras, Springer-Verlag, Berlin,
1972, Lecture Notes in Mathematics, Vol. 260. MR MR0342495 (49 #7241)
[Hof08]
Werner Hoﬀmann, Geometric estimates for the trace formula, Ann. Global Anal. Geom. 34
(2008), no. 3, 233–261. MR 2434856 (2009e:11100)
[Hof12]
, Induced conjugacy classes, prehomogeneous varieties, and canonical parabolic subgroups,
2012, arXiv:1206.3068.
[Hof14]
, The trace formula and prehomogeneous vector spaces, 2014, arXiv:1412.8673.
[HW13]
Werner Hoﬀmann and Satoshi Wakatsuki, On the geometric side of the Arthur trace formula for
the symplectic group of rank 2, 2013, arXiv:1310.0541.
[Kot82]
Robert E. Kottwitz, Rational conjugacy classes in reductive groups, Duke Math. J. 49 (1982),
no. 4, 785–806. MR 683003 (84k:20020)


## Page 33


ON THE CONTINUITY OF THE GEOMETRIC SIDE OF THE TRACE FORMULA
33
[Lan04]
Robert P. Langlands, Beyond endoscopy, Contributions to automorphic forms, geometry, and
number theory, Johns Hopkins Univ. Press, Baltimore, MD, 2004, pp. 611–697. MR 2058622
(2005f:11102)
[Lan07]
, Un nouveau point de rep`ere dans la th´eorie des formes automorphes, Canad. Math. Bull.
50 (2007), no. 2, 243–267. MR 2317447 (2008m:11095)
[Lan13]
, Singularit´es et transfert, Ann. Math. Qu´e. 37 (2013), no. 2, 173–253. MR 3117742
[LS79]
G. Lusztig and N. Spaltenstein, Induced unipotent classes, J. London Math. Soc. (2) 19 (1979),
no. 1, 41–52. MR MR527733 (82g:20070)
[Mat13]
Jasmin Matz, Zeta functions for the adjoint action of GL(n) and density of residues of Dedekind
zeta functions, 2013, arXiv:1308.5394.
[Ngˆo14]
Bao Chˆau Ngˆo, On a certain sum of automorphic L-functions, Automorphic forms and related
geometry: assessing the legacy of I. I. Piatetski-Shapiro, Contemp. Math., vol. 614, Amer. Math.
Soc., Providence, RI, 2014, pp. 337–343. MR 3220933
Universit¨at Leipzig, Mathematisches Institut, Postfach 100920, D-04009 Leipzig, Ger-
many
E-mail address: finis@math.uni-leipzig.de
Department of Mathematics, Weizmann Institute of Science, Rehovot 7610001, Israel
E-mail address: erez.m.lapid@gmail.com

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1512_08753_on_the_continuity_of_the_geometric_side_of_the_trace_formula
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2015/1512_08753_ON_THE_CONTINUITY_OF_THE_GEOMETRIC_SIDE_OF_THE_TRACE_FORMULA.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

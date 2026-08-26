---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1707.03005v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1707.03005v3_Trace-free____rm_SL__2__mathbb_C___-representations_of_arborescent_links

> Source: 1707.03005v3_Trace-free____rm_SL__2__mathbb_C___-representations_of_arborescent_links.pdf

> Pages: 19

---


## Page 1


Trace-free SL(2, C)-representations of
arborescent links
Haimiao Chen ∗
Beijing Technology and Business University, Beijing, China
Abstract
Given a link L ⊂S3, a representation π1(S3 −L) →SL(2, C)
is trace-free if it sends each meridian to an element with trace zero.
We present a method for completely determining trace-free SL(2, C)-
representations for arborescent links. Concrete computations are done
for a class of 3-bridge arborescent links.
Keywords: trace-free representation, arborescent link, arborescent
tangle, 3-bridge
MSC2010: 57M25, 57M27
1
Introduction
Let G be a linear group. Given a link L ⊂S3, a trace-free G-representation
is a homomorphism ρ : π1(S3 −L) →G which sends each meridian to an
element with trace zero.
Researchers have paid attention to such representations for long. For a
knot K, Lin [6] deﬁned an invariant h(K) roughly by counting (with signs)
conjugacy classes of trace-free SU(2)-representations of K, and showed that
h(K) equals half of the signature of K. Interestingly, it was shown in [5]
that if L is an alternating link or a 2-component link, then its Khovanov
homology is isomorphic to the singular homology of the space of binary
dihedral representations (a special kind of trace-free SU(2)-representations)
of L, as graded abelian groups. Also interesting is that, by the result of [7],
each trace-free SL(2, C)-representation of L gives rise to a representation
π1(M2(L)) →SL(2, C), where M2(L) is the double covering of S3 branched
along L.
∗Email: chenhm@math.pku.edu.cn
1
arXiv:1707.03005v3  [math.GT]  20 Oct 2018


## Page 2


As is well-known, linear representations of links are useful, but there is
no general method to systematically ﬁnd nontrivial ones. We may ﬁrst fo-
cus on trace-free representations, which turn out to be easier to manipulate.
This makes up another motivation. In this paper we aim to determine all
trace-free SL(2, C)-representations for each arboresent link, which is a con-
tinuation of the previous work [1]. From now on, we abbreviate “trace-free
SL(2, C)-representation” to “representation”. The main results are Theorem
4.2 and Theorem 4.3. Based on them, we are able to explicitly determine
all representations for any given arborescent link.
We introduce some basic notions in Section 2, and deﬁne representation
of a tangle in Section 3. In the main body, Section 4, we clarify properties
of representations of arborescent tangles, uncovering an exquisite structure
in the representation space, and then explain how to determine all repre-
sentations for arborescent tangles. These lead to a practical method to ﬁnd
all representations for arborescent links, as presented in Section 5. As an
illustration, explicit formulas are given for a class of 3-bridge arborescent
links.
It should be pointed out that most of the results in this paper will remain
valid when C is replaced by a general ﬁeld, or even a ring.
2
Preliminary
2.1
Tangles and tangle diagrams
Adopt the notions in [3]. A 2-tangle T is an embedding of [0, 1]⊔[0, 1]⊔mS1
(where mS1 denotes the disjoint union of m copies of S1 and m ≥0) into a
3-dimensional ball B3, such that ∂T ∩B3 is a speciﬁc set of four points on
∂B3 = S2. Two 2-tangles T, T ′ are isotopic if there exists a homeomorphism
h : B3 →B3 such that h|S2 = id and h(T) = T ′.
Each tangle can be represented by a diagram by a usual manner, as done
throughout the paper. Abusing the notation, by “tangle” we also mean a
diagram, whenever there is no ambiguity.
Let T2 denote the set of 2-tangles. The simplest four ones are given in
Figure 1. In T2 there are two binary operations: horizontal composition +
and vertical composition ∗, as illustrated in Figure 2. Let Tar denote the
subset of T2 containing [±1] and closed under + and ∗. An element of Tar
is called an arborescent tangle. Each arborescent tangle other than [0], [∞]
can be obtained from copies of [±1] via iterated horizontal and vertical
compositions.
2


## Page 3


Figure 1: The simplest four tangles: (a) [0], (b) [∞], (c) [1], (d) [−1]
Figure 2: (a) T1 + T2; (b) T1 ∗T2
Lemma 2.1. There is a unique function f : T2 →Q ∪{∞} such that f(T)
depends only on the isotopy class of T, and characterized by
f([±1]) = ±1,
(1)
f(T1 + T2) = f(T1) + f(T2),
(2)
f(T1 ∗T2) =
1
1/f(T1) + 1/f(T2).
(3)
As a convention, 1/0 = ∞, 1/∞= 0, a + b = ∞if a = ∞or b = ∞.
This was established in [3]. Call f(T) the fraction of T.
For k ̸= 0, the horizontal composite of |k| copies of [1] (resp. [−1]) is
denoted by [k] if k > 0 (resp. k < 0), and the vertical composite of |k| copies
of [1] (resp. [−1]) is denoted by [1/k] if k > 0 (resp. k < 0). Obviously,
f([k]) = k and f([1/k]) = 1/k. Given integers k1, . . . , km, the rational tangle
[[k1], . . . , [km]] is deﬁned as
(
[k1] ∗[1/k2] + · · · ∗[1/km],
if 2 | m,
[k1] ∗[1/k2] + · · · + [km],
if 2 ∤m.
(4)
It is easy to see that
f([[k1], . . . , [km]]) = [[k1, . . . , km]](−1)m−1,
(5)
3


## Page 4


where the continued fraction [[k1, . . . , km]] ∈Q is deﬁned inductively as
[[k1]] = k1,
[[k1, . . . , km]] = km + 1/[[k1, . . . , km−1]].
(6)
By Theorem 3 of [4], two rational tangles are isotopic if and only if their
fractions coincide. Denote [[k1], . . . , [km]] as [p/q] if its fraction equals p/q.
A Montesinos tangle is a tangle of the form [p1/q1] ∗· · · ∗[pn/qn].
Figure 3: (a) the numerator of T; (b) a tangle T; (c) the denominator of T
Each tangle T ∈T2 leads to two links: the numerator N(T) and the
denominator D(T); see Figure 3. An arborescent link is a link of the form
N(T) or D(T), with T ∈Tar. In particular, a Montesinos link is a link of
the form D([p1/q1] ∗· · · ∗[pn/qn]), denoted as M(p1/q1, . . . , pn/qn).
2.2
Some linear algebra
Let SL0(2, C) denote the subset of SL(2, C) consisting of matrices with trace
zero. For any X, Y ∈SL0(2, C), we have
X−1 = −X,
XY X−1 = −tr(XY ) · X −Y.
(7)
For X, Z ∈SL(2, C), denote ZXZ−1 by Z.X. For X, Y, X′, Y ′ ∈SL0(2, C),
denote (X, Y ) ∼(X′, Y ′) if there exists Z ∈SL(2, C) such that Z.X = X′
and Z.Y = Y ′. This deﬁnes an equivalence relation on SL0(2, C)×SL0(2, C).
For a, b, c ∈C with a, b ̸= 0, let
t(a) = a + a−1,
s(a) = a −a−1,
(8)
Ab(a) = 1
2

t(a)i
s(a)b
s(a)b−1
−t(a)i

,
(9)
B1(c) =
 i
c
0
−i

,
B2(c) =
 i
0
c
−i

.
(10)
4


## Page 5


Let A = A1(1) and Bℓ= Bℓ(1) for ℓ= 1, 2, i.e.,
A =
 i
0
0
−i

,
B1 =
 i
1
0
−i

,
B2 =
 i
0
1
−i

.
(11)
As can be veriﬁed,
tr(A1(a1)Ac(a2)) = 1
4s(a1)s(a2)t(c) −1
2t(a1)t(a2) =: γa1,a2(c),
(12)
tr(Ac(a)Bℓ) = 1
2s(a)c(−1)ℓ−t(a) =: δa,ℓ(c).
(13)
These two formulas will be useful in Example 4.6 and the last section.
Remark 2.2. As a special case of (12), tr(AA1(a)) = −t(a). Observe that
if a /∈{±1} and tr(AX) = −t(a), then X = Ab(a) for some b.
For any a, b ∈C, we have
Bℓ(a).Bℓ(b) = Bℓ(2a −b);
(14)
in particular, Bℓ(a).A = Bℓ(2a).
For X, Y ∈SL0(2, C) with tr(XY ) = t(a), call the pair (X, Y ) regular
(R for short) if (X, Y ) ∼(A, −A1(a)), and call it non-regular (NR for short)
otherwise.
It is a simple exercise in linear algebra that (X, Y ) is NR if
and only if a ∈{±1} and X ̸= −aY , in which case (X, Y ) ∼(A, −aB1)
or (X, Y ) ∼(A, −aB2); it is clear that (A, −aB1) ̸∼(A, −aB2).
When
(X, Y ) ∼(A, −aBℓ), say (X, Y ) is NR of type ℓ(NRℓfor short).
For (a, b) ∈C× × C× with a /∈{±1}, put
S(a,b) =
1
s(a)
 s(ab−1)
s(b)
−s(b)
s(ab)

.
(15)
Observe that
S(a,b) = ±I ⇔b = ±1,
(16)
S(a,b) = S(a′,b′) ⇔(a, b) ∼(a′, b′),
(17)
S(a,b)S(a,b′) = S(a,bb′).
(18)
Let
U = C× × C×/(a, b) ∼(a−1, b−1).
(19)
5


## Page 6


Denote the equivalence class of (a, b) by [a, b]. From (17) we see that S[a,b]
can be deﬁned without ambiguity. Also well-deﬁned is the map
t : U →C2,
[a, b] 7→(t(a), t(b)).
(20)
For c ∈{±1} and u ∈C, put
Cc(u) =
 1 + u
−cu
cu
1 −u

.
(21)
It is easy to see that for any u1, u2,
Cc(u1)Cc(u2) = Cc(u1 + u2),
(22)
and for any a, b, u ∈C,
(Bℓ(a), −cBℓ(b))Cc(u) = (Bℓ(a + ua −ub), −cBℓ(b + ua −ub)).
(23)
3
Representations of tangles
In a tangle T, each arc together with a choice of direction is called a directed
arc; let D(T) denote the set of directed arcs of T. For x ∈D(T), let x−1
denote the same underlying arc of x with direction reversed.
Given a 2-tangle T.
A (trace-free SL(2, C)-)representation of T is a
homomorphism π1(B3−T) →SL(2, C) sending each meridian to an element
of SL0(2, C). In virtue of Wirtinger presentation, it is the same as a map
ρ : D(T) →SL0(2, C) such that ρ(x−1) = ρ(x)−1 = −ρ(x) for each x and
ρ(z) = ρ(x)ρ(y)ρ(x)−1 = −tr(ρ(x)ρ(y)) · ρ(x) −ρ(y)
(24)
for all x, y, z that are placed as in Figure 4 (a) or (b). To denote such a map,
Figure 4: Three arcs forming a crossing
we choose for each arc a direction and label it with an element of SL0(2, C).
Let R(T) denote the set of representations of a tangle T.
6


## Page 7


Remark 3.1. Observe that, for each ρ ∈R(T), the function
D(T) →SL0(2, C),
x 7→ρ(x)t
(25)
(Xt denotes the transpose of X) is also a representation. This deﬁnes an
involution on R(T).
Let T nw, T ne, T sw, T se denote the directed arcs shown in Figure 5. Given
ρ ∈R(T), let
ρnw = ρ(T nw),
ρsw = ρ(T sw),
ρne = ρ(T ne),
ρse = ρ(T se),
(26)
ρw = (ρnw, ρsw),
ρe = (ρne, ρse),
ρn = (ρnw, ρne),
ρs = (ρsw, ρse), (27)
trv(ρ) = tr(ρnwρsw) = tr(ρneρse),
(28)
trh(ρ) = tr(ρnwρne) = tr(ρswρse).
(29)
Say that ρn is R (resp. NRℓ) if (ρnw, ρne) is R (resp. NRℓ), and so on.
Figure 5: A tangle diagram with the ends directed outwards
Let ρ be a representation of T. Call ρ reducible if all of the elements in
its image Im(ρ) share an eigenvector, or equivalently, ρ is conjugate to an
upper-triangular representation, which by deﬁnition sends each x ∈D(T)
to an upper-triangular matrix; it follows that tr(ρ(x)ρ(y)) ∈{±2} for any
x, y ∈D(T). In particular, call ρ abelian if Im(ρ) is abelian. Call ρ irreducible
if it is not reducible.
If T ′ is a sub-tangle of T, then the map
ρ|T ′ : D(T ′) ,→D(T)
ρ
−→SL0(2, C)
(30)
is a representation, called the restriction of ρ on T ′.
Given ρj ∈R(Tj), j = 1, 2. If ρw
2 = −ρe
1, meaning ρnw
2
= −ρne
1 , ρsw
2
=
−ρse
1 , then we can “glue” ρ1 and ρ2 to obtain a representation of T1 + T2,
denoted by ρ1 + ρ2. Similarly, if ρn
2 = −ρs
1, then we can deﬁne ρ1 ∗ρ2 ∈
R(T1 ∗T2). Thus there are partial compositions
+ : R(T1) ×h R(T2) →R(T1 + T2),
(ρ1, ρ2) 7→ρ1 + ρ2,
(31)
∗: R(T1) ×v R(T2) →R(T1 ∗T2),
(ρ1, ρ2) 7→ρ1 ∗ρ2,
(32)
7


## Page 8


where
R(T1) ×h R(T2) = {(ρ1, ρ2) ∈R(T1) × R(T1): ρw
2 = −ρe
1},
(33)
R(T1) ×v R(T2) = {(ρ1, ρ2) ∈R(T1) × R(T1): ρn
2 = −ρs
1}.
(34)
Example 3.2. Representations of [±1] are easy to describe. If ρ is a rep-
resentation of [1] (resp. [−1]), with ρw = (X, Y ) and tr(XY ) = t(a), then
ρe = (−t(a)X −Y, X) (resp. ρe = (Y, −t(a)Y −X)). Note that
(a) ρ is irreducible if and only if a /∈{±1};
(b) when a ∈{±1},
ρw is NR ⇔ρe is NR ⇔Y ̸= −aX ⇔ρn is NR ⇔ρs is NR.
Figure 6: (a) a representation of [1]; (b) a representation of [−1]
4
Representation spaces of arborescent tangles
We separately investigate reducible representations.
Proposition 4.1. Suppose T ∈Tar, with f(T) = f; suppose ρ ∈R(T) is
reducible, so that trv(ρ) = 2a, trh(ρ) = 2b for some a, b ∈{±1}. Then
(i) ρe = −bρwCa(f) if f ̸= ∞,
(ii) ρs = −aρnCb(f−1) if f ̸= 0.
Proof. Referring to (b) in Example 3.2, it is easy to check (i), (ii) for [±1].
Suppose the conclusion is true for T1, T2, we shall prove it for T = T1 + T2;
the proof for T = T1 ∗T2 is similar. Let fj = f(Tj), then f = f1 + f2 by (2).
Let ρj = ρ|Tj, then ρ1, ρ2 are both reducible. Clearly, trv(ρ1) = trv(ρ2) = 2a;
suppose trh(ρj) = 2bj with bj ∈{±1}.
8


## Page 9


If f ̸= ∞, then f1, f2 ̸= ∞, so ρe
j = −bjρw
j Ca(fj), j = 1, 2. Hence
ρe = ρe
2 = −b2ρw
2 Ca(f2) = b2ρe
1Ca(f2) = −b1b2ρw
1 Ca(f1)Ca(f2)
= −b1b2ρwCa(f1 + f2) = −b′ρwCa(f),
with
b′ = b1b2,
where (22) is used. Computing directly, we obtain
tr(ρneρnw) = tr(−b′((1 + f)ρnw + afρsw)ρnw) = b′(2(1 + f) −2a2f) = 2b′,
(35)
which shows that actually b = b′. Hence (i) is true.
If f ̸= 0, ∞, then writing ρsw = −aρnw + X, so that
ρe = −bρwCa(f) = −b(ρnw + afX, −aρnw + (1 −f)X),
we obtain ρs = −aρnCb(f−1), i.e., (ii) is true in the case f ̸= ∞.
If f = ∞, then f1 = ∞or f2 = ∞.
• If f1 = f2 = ∞, then ρs
j = −aρn
j Cbj(0), so that ρsw
1
= −aρnw
1
and
ρse
2 = −aρne
2 , i.e., ρs = −aρnCa(0);
• if f1 = ∞and f2 ̸= ∞, then ρs
1 = −aρn
1 and ρe
2 = −b2ρw
2 Ca(f2), which
implies ρse
2 = −aρne
2 , hence also ρs = −aρnCa(0);
• if f1 ̸= ∞and f2 = ∞, the proof is similar.
Thus (ii) is true in the case f = ∞.
Now state and prove our ﬁrst main result.
Theorem 4.2. Let T ∈Tar, with f(T) = f, and let ρ ∈R(T).
(i) Let {α, β} = {e, w}. If ρα is NRℓ, then trv(ρ) = 2a, trh(ρ) = 2b with
a, b ∈{±1}, ρβ = −bραCa(u) for some u ∈Q, and ρβ is also NRℓ;
moreover, u ̸= 0 if and only if ρn, ρs are NRℓ.
(ii) Let {α, β} = {n, s}. If ρα is NRℓ, then trv(ρ) = 2a, trh(ρ) = 2b with
a, b ∈{±1}, ρβ = −aραCb(v) for some v ∈Q, and ρβ is also NRℓ;
moreover, v ̸= 0 if and only if ρw, ρe are NRℓ.
(iii) If tv /∈{±2}, then ρn, ρw, ρs, ρe are all R, and there exists a unique
[a, b] ∈U with t([a, b]) = (trv(ρ), trh(ρ)) and ρe = −ρwS[a,b].
(iv) If th /∈{±2}, then ρn, ρw, ρs, ρe are all R, and there exists a unique
[a, b] ∈U with t([a, b]) = (trv(ρ), trh(ρ)) and ρs = −ρnS[b,a].
9


## Page 10


In any case, denote [a, b] ∈U by χ(ρ).
Proof. For T ∈Tar, let Hk(T) denote the statement (k) for T. It is easy to
verify Hk([±1]), k ∈{i, . . . , iv}. Suppose Hk(Tj), k ∈{i, . . . , iv}, j ∈{1, 2}
have been established. We shall prove Hk(T), k ∈{i, . . . , iv} for T = T1+T2;
the proof for T1 ∗T2 is similar. Let ρj = ρ|Tj.
(i) Assume α = w, β = e; the proof for the other case is similar.
For j = 1, 2, by Hi(Tj), trv(ρj) = 2a, trh(ρj) = 2bj with a, bj ∈{±1},
and there exists uj ∈Q, such that ρe
j = −bjρw
j Ca(uj). Then due to ρw
2 = −ρe
1
and (22), we have
ρe = −(b1b2)ρw
1 Ca(u1)Ca(u2) = −b′ρwCa(u),
with u = u1 + u2, b′ = b1b2. Computing similarly as in (35),
tr(ρneρnw) = tr(−b((1 + u)ρnw + auρsw)ρnw) = b′(2(1 + u) −2a2u) = 2b′.
Hence b = b′, and ρe = −b′ρwCa(u).
Up to conjugacy we may assume ρw = (A, −aBℓ), then
ρe = −b(A, −aBℓ)Ca(u) = −b(Bℓ(−u), −aBℓ(1 −u)).
Since by (14), Bℓ(−u) = Bℓ(−u/2).A and Bℓ(1 −u) = Bℓ(−u/2).Bℓ(−1),
we see that ρe is NRℓ. Obviously, u ̸= 0 if and only if ρn, ρs are NRℓ.
(iii) If trv(ρ) /∈{±2}, then ρw, ρe are R; by Hiii(Tj), there exists a unique
[aj, bj] ∈U such that t([aj, bj]) = (trv(ρj), trh(ρj)) and ρe
j = −ρw
j S[aj,bj].
Replacing a2 by its inverse if necessary, we may assume a2 = a1 =: a. Then
ρe = −ρw
2 S[a,b2] = ρe
1S[a,b2] = −ρw
1 S[a,b1]S[a,b2] = −ρwS[a,b],
(36)
with b = b1b2. By computation, tr(ρnwρne) = t(b). If b ∈{±1}, then by
(16), ρe = −bρw. Thus ρn, ρs are R.
(iv) Suppose trh(ρ) /∈{±2}. Then ρn, ρs are R, and by (i), ρw, ρe are
R. If trv(ρ) = 2a with a ∈{±1}, then ρs = −aρn = −aρnS[b,a], where b
is any of the two roots of b + b−1 = trh(ρ), (note that [a, b] = [a, b−1]).
If trv(ρ) /∈{±2}, then by (iii) there exists a unique [a, b] ∈U such that
t([a, b]) = (trv(ρ), trh(ρ)) and ρe = −ρwS[a,b]; writing ρsw = −aρnw + s(a)X,
we have
ρe = (−b−1ρnw −s(b)X, ab−1ρnw + s(ba−1)X),
implying ρs = −aρnS[b,a] straightforward.
(ii) Assume ρn is NRℓ; the proof for the other case is similar. By (iii),
trv(ρ) = 2a with a ∈{±2}.
10


## Page 11


If ρw
1 , ρe
1, ρe
2 are all R, then ρs = −aρn = −aρnCb(0), and ρs is NRℓ.
If at least one of ρw
1 , ρe
1, ρe
2 is NRℓ′, then by Hi(T1), Hi(T2), all of them
are NRℓ′. By (i), trh(ρ) = 2b with b ∈{±1} and ρe = −bρwCa(u) for some
u ∈Q. Since Ca(0) = I but ρn is NR, we have u ̸= 0; by (i) again, ℓ′ = ℓand
ρs is also NRℓ. Similarly as in the proof of Proposition 4.1, we can deduce
ρs = −aρnCb(u−1) from ρe = −bρwCa(u).
For T ∈Tar and a, b ∈C×, let
Ra,b(T) = {ρ ∈R(T): (trv(ρ), trh(ρ)) = (t(a), t(b))}.
(37)
For ρ ∈Ra,b(T),
• say ρ is (of type) VR0 if a ∈{±1} and ρw is R, and write ρ ∈VR0;
• say ρ is (of type) VR1 if a /∈{±1}, and write ρ ∈VR1;
• say ρ is (of type) VNRℓif ρw is NRℓ, and write ρ ∈VNRℓ.
The three types are called V-types. Similarly, we have notions of H-types.
For a, b ∈{±1}, ℓ∈{1, 2} and u, v ∈Q, let
Ra,b
vn(ℓ,u)(T) = {ρ ∈Ra,b(T): ρ ∈VNRℓ, ρe = −bρwCa(u)};
(38)
Ra,b
hn(ℓ,v)(T) = {ρ ∈Ra,b(T): ρ ∈HNRℓ, ρs = −aρnCb(v)}.
(39)
The proof of Theorem 4.2 clariﬁes that, if u ̸= 0, then
Ra,b
vn(ℓ,u)(T) = Ra,b
hn(ℓ,u−1)(T).
Note that the involution deﬁned in Remark 3.1 interchanges Ra,b
vn(ℓ,u)(T) with
Ra,b
vn(ℓ′,u)(T) for {ℓ, ℓ′} = {1, 2}.
For a, b ∈{±1} and U, V ∈SL0(2, C), set
RU,V
vr(a)(T) = {ρ ∈R(T): ρ ∈VR0, ρn = (U, V )},
(40)
RU,V
hr(b)(T) = {ρ ∈R(T): ρ ∈HR0, ρw = (U, V )}.
(41)
From the proof of Theorem we see that the partial operation + (deﬁned
in Section 3) restricts to
Ra,b1(T1) ×h Ra,b2(T2) →Ra,b1b2(T1 + T2),
a /∈{±1},
RU,W
vr(a)(T1) × R−W,V
vr(a) (T2) →RU,V
vr(a)(T1 + T2),
a ∈{±1},
Ra,b1
vn(ℓ,u1)(T1) ×h Ra,b2
vn(ℓ,u2)(T2) →Ra,b1b2
vn(ℓ,u1+u2)(T1 + T2),
a, b1, b2 ∈{±1}.
The situation for ∗is similar.
Here is our second main result.
11


## Page 12


Theorem 4.3. One may inductively determine representations of an ar-
borescent tangle by the following rules:
(a) When a /∈{±1},
Ra,b(T1 + T2) =
G
b1b2=b
Ra,b1(T1) + Ra,b2(T2);
(42)
when a ∈{±1},
RU,V
vr(a)(T1 + T2) =
G
W
RU,W
vr(a)(T1) + R−W,V
vr(a) (T2),
(43)
Ra,b
vn(ℓ,u)(T1 + T2) =
G
u1+u2=u
b1b2=b
Ra,b1
vn(ℓ,u1)(T1) + Ra,b2
vn(ℓ,u2)(T2).
(44)
For ρ ∈RU,V
vr(a)(T1 + T2), denoting ρj = ρ|Tj, there are three cases:
(i) if ρ ∈HR0, then b2 ∈{bb±1
1 } and ρ1, ρ2 are of the same H-type;
(ii) if ρ ∈HR1, then either ρ1 ∈HR1, or ρ2 ∈HR1, or ρj ∈HNRℓj,
j = 1, 2, with ℓ1 ̸= ℓ2;
(iii) if ρ ∈HNRℓ, then either ρj ∈HR1, ρj′ /∈HR0 for j′ ̸= j, or ρj ∈
HNRℓ, ρj′ /∈HNRℓ′ for j′ ̸= j, with ℓ′ ̸= ℓ.
(b) When b /∈{±1},
Ra,b(T1 ∗T2) =
G
a1a2=a
Ra1,b(T1) ∗Ra2,b(T2);
(45)
when b ∈{±1},
RU,V
hr(b)(T1 ∗T2) =
G
W
RU,W
hr(b)(T1) ∗R−W,V
hr(b) (T2),
(46)
Ra,b
hn(ℓ,v)(T1 ∗T2) =
G
v1+v2=v
a1a2=a
Ra1,b
hn(ℓ,v1)(T1) ∗Ra2,b
hn(ℓ,v2)(T2).
(47)
For ρ ∈RU,V
hr(b)(T1 ∗T2), denoting ρj = ρ|Tj, there are three cases:
(i) if ρ ∈VR0, then a2 ∈{aa±1
1 } and ρ1, ρ2 are of the same V-type;
(ii) if ρ ∈VR1, then either ρ1 ∈VR1, or ρ2 ∈VR1, or ρj ∈VNRℓj,
j = 1, 2, with ℓ1 ̸= ℓ2;
12


## Page 13


(iii) if ρ ∈VNRℓ, then either ρj ∈VR1, ρj′ /∈VR0 for j′ ̸= j, or ρj ∈
VNRℓ, ρj′ /∈VNRℓ′ for j′ ̸= j, with ℓ′ ̸= ℓ.
Proof. We only prove (a); the proof for (b) is similar.
The equations (42) and (43) are obvious.
In the three cases for ρ ∈
RU,V
vr(a)(T1+T2), (i) is obvious, (ii) and (iii) are consequences of the following:
• If ρj ∈HR0 then ρ1 + ρ2 has the same H-type as ρj′, j′ ̸= j. This is
obvious.
• If ρ1, ρ2 ∈HNRℓj, then
ρ1 + ρ2 ∈
(
HR0 ⊔HNRℓ,
ℓ1 = ℓ2 = ℓ,
HR1,
ℓ1 ̸= ℓ2.
.
To see this, just assume ρne
1
= A, then ρnw
1
= −b1Bℓ1(c1) for some
c1 ̸= 0, and ρnw
2
= b2Bℓ2(c2) for some c2 ̸= 0, so that tr(ρnw
1 ρne
2 ) ∈{±2}
if ℓ1 = ℓ2 and tr(ρnw
1 ρne
2 ) /∈{±2} if ℓ1 ̸= ℓ2.
Figure 7: A representation of a rational tangle
Example 4.4. Let T = [p/q] = [[k1], . . . , [km]] ̸= [0].
As illustrated by
Figure 7, a representation ρ is determined by (X, Y ) (called the generating
pair).
More precisely, Xj, Yj, j = 1, . . . , m are all linear combinations of
X, Y , the coeﬃcients being polynomials in tr(XY ) that are independent of
the type (i.e., H-type and V-type) of ρ. Suppose tr(XY ) = t(c). Up to
conjugacy, ρ is determined by its type and t(c).
13


## Page 14


If c /∈{±1}, then by induction on m, we can show
χ(ρ) = [(−1)˜q−1cq, (−1)˜p−1cp],
(48)
where ˜p/˜q = [[k2, . . . , km]](−1)m−1 so that p˜p−q˜q = 1; see Section 2 of [1] for
more details. Let a = (−1)˜q−1cq, b = (−1)˜p−1cp, so that [a, b] = χ(ρ), and
(−a)p + (−b)q = 0.
(49)
Note that c = b˜pa−˜q, so a /∈{±1} or b /∈{±1}, and ρn, ρw, ρs, ρe are all R.
If c ∈{±1} and Y = −cX, then ρ is abelian, so ρn, ρw, ρs, ρe are all R.
If c ∈{±1} and Y ̸= −cX, then (X, Y ) ∼(A, −cBℓ) with ℓ∈{±1},
and ρ is reducible. Applying Proposition 4.1, we can successively show that
(X, Yj) is NRℓfor j = 1, 2, . . . , m. Consequently, ρn, ρw, ρs, ρe are all NRℓ.
Remark 4.5. It is worth emphasizing three features of representations ρ of
a rational tangle diﬀerent from [0]:
(i) ρn, ρw, ρs, ρe are simultaneously R or NR, in which case we simply say
that ρ is R or NR, respectively;
(ii) the condition (49) is also true when ρ is NR, since the expressions of
Xj, Yj in terms of X, Y and t(c) do not depend on the type of ρ;
(iii) ρ is determined by ρnw, ρne, ρsw, ρse.
Example 4.6. Let T = [p1/q1] + [p2/q2] and ρ ∈R(T). Up to conjugacy
we may assume ρnw = A. Let ρj = ρ|[pj/qj]. Suppose χ(ρ) = [a, b], and
χ(ρj) = [a, bj], j = 1, 2. Then by (49),
(−a)pj + (−bj)qj = 0,
j = 1, 2.
If ρ ∈VR1, then b1b2 = b; up to conjugacy, ρsw = −A1(α), and ρ is
determined by
ρe
1 = −(A, −aBℓ)S(a,b1),
ρe
2 = −(A, −aBℓ)S(a,b).
If ρ ∈VNRℓ, then b1b2 = b; up to conjugacy, ρsw = −aBℓ, and ρ is
determined by
ρe
1 = −b1(A, −aBℓ)Ca(p1/q1),
ρe
2 = −b(A, −aBℓ)Ca(p1/q1 + p2/q2).
If ρ ∈VR0, then ρsw = −aA, and ρse
j = −aρne
j , j = 1, 2, so ρ is deter-
mined by ρne
1 and ρne
2 . There are three possibilities:
14


## Page 15


(i) If ρ ∈HR0, then b2 ∈{bb±1
1 }, ρne
2 = −bA, and ρ1, ρ2 are both R, hence
up to conjugacy, ρne
1 = −A1(b1).
(ii) If ρ ∈HR1, then up to conjugacy, ρne
2
= −A1(b), and one of the
following occurs:
• ρ1 ∈HR1, ρ2 ∈HR0, b2 ∈{±1}, b = b1b2, and ρne
1 = −A1(b1);
• ρ1 ∈HR0, ρ2 ∈HR1, b1 ∈{±1}, b = b1b2, and ρne
1 = −b1A;
• ρ1 ∈HR1, ρ2 ∈HR1, b1, b2 /∈{±1}; up to conjugacy, ρne
1
=
−Ac(b1), with γb,b1(c) = −t(b2).
(iii) If ρ ∈HNRℓ, then ρ1, ρ2 ∈HR1, so that bj /∈{±1}; up to conjugacy,
ρne
2 = −bBℓand ρne
1 = −Ac(b1), with δb1,ℓ(c) = −t(b2)b.
5
Finding all representations of an arborescent link
The method is straightforward. For T ∈Tar, a representation of N(T) is
the same as ρ ∈R(T) with ρe = −ρw, which is equivalent to







b = 1,
if ρ ∈Ra,b(T) with a /∈{±1},
b = 1, U = −V,
if ρ ∈RU,V
vr(a)(T) with a ∈{±1},
b = 1, u = 0,
if ρ ∈Ra,b
vn(ℓ,u)(T);
(50)
a representation of D(T) is the same as ρ ∈R(T) with ρs = −ρn, which is
equivalent to







a = 1,
if ρ ∈Ra,b(T) with b /∈{±1},
a = 1, U = −V,
if ρ ∈RU,V
hr(b)(T) with b ∈{±1},
a = 1, v = 0,
if ρ ∈Ra,b
hn(ℓ,v)(T).
(51)
Thus the problem is reduced to ﬁnding all representations of T with
some speciﬁed conditions.
5.1
A class of 3-bridge arborescent links
3-bridge arborescent links were completely classiﬁed by Jang [2]. Accord-
ing to [2] Theorem 1, there are three families of non-Montesinos 3-bridge
arborescent links, one of which consists of links of the form L = N(T) with
T = ([p1/q1] ∗[p′
1/q′
1]) + [1/k0] + ([p2/q2] ∗[p′
2/q′
2]).
15


## Page 16


Figure 8 illustrates L together with some directed arcs x0, . . . , x9.
Given a representation ˜ρ of L, let Xj = ˜ρ(xj), j = 0, . . . , 9, and let ρ
denote the corresponding representation of T. Then ρe = −ρw. By (iii) in
Remark 4.5, to describe ρ (and ˜ρ), it suﬃces to write down the Xj’s. Up to
conjugacy, we may assume X0 = A.
Let ρ0 = ρ|[1/k0], and ρj = ρ|[pj/qj]∗[p′
j/q′
j], j = 1, 2. Suppose
χ(ρ) = [a, b],
χ(ρ0) = [a, b0],
(52)
χ(ρ|[pj/qj]) = [aj, bj],
χ(ρ|[p′
j/q′
j]) = [a′
j, bj],
j = 1, 2.
(53)
Then
a = (−b0)k0;
(−aj)pj + (−bj)qj = (−a′
j)p′
j + (−bj)q′
j = 0,
j = 1, 2.
(54)
Figure 8: L = N(T) with T = ([p1/q1] ∗[p′
1/q′
1]) + [1/k0] + ([p2/q2] ∗[p′
2/q′
2])
To simplify the writing, let
hj = qj
pj
+
q′
j
p′
j
,
j = 1, 2.
(55)
16


## Page 17


5.1.1
ρ is VR1
In this case, a /∈{±1}, b0b1b2 = 1, and aja′
j = a if bj /∈{±1}.
Up to
conjugacy we may assume X7 = −A1(a), then
(X1, X8) = −(X0, X7)S(a,b1),
(X2, X9) = (X1, X8)S(a,b0),
(X3, X4) = −(X0, X1)S(b1,a1)
when
b1 /∈{±1},
(X5, X6) = (X2, X0)S(b2,a2)
when
b2 /∈{±1};
when b1 ∈{±1}, X3 = −Ac1(a1), with γa,a1(c1) = t(a′
1), and X4 = −b1X3;
when b2 ∈{±1}, X6 = −Ac2(a2), with γa,a2(c2) = −t(a′
2), and X5 = −b2X6.
5.1.2
ρ is VR0
In this case, a ∈{±1}, ρ0 is R, and Xj = −aXj−7 for j = 7, 8, 9.
For j = 1, 2,
• if ρj ∈HR0, then a′
j ∈{aa±1
j }, X3j = (−1)jAcj(aj), and X3j−(−1)j =
−bjX3j;
• if ρj ∈HR1, then aja′
j = a, and
(
(X3, X4) = −(X0, X1)S(b1,a1),
j = 1,
(X5, X6) = (X2, X0)S(b2,a2),
j = 2;
• if ρj ∈HNRℓj, then aja′
j = a, hj = 0, and
(
(X3, X4) = −a1(X0, X1)Cb1(q1/p1),
j = 1,
(X5, X6) = a2(X2, X0)Cb2(q2/p2),
j = 2.
To determine ρ, it remains to work out X1, X2. There are 7 cases, as
listed below. In each case, (up to conjugacy) the value of (X1, X2) is given
in the upper cell, and an extra constraint is given in the lower cell.
HHHHHH
ρ1
ρ2
HR0
HR1
HNRℓ2
HR0
(−b1A, −b2A)
(−b1A, −A1(b2))
b1b2 = b0
t(b2)b1 = t(b0)
HR1
(−A1(b1), −b2A)
(−A1(b1), −Ac(b2))
(−Ac(b1), −b2Bℓ2)
t(b1)b2 = t(b0)
γb1,b2(c) = −t(b0)
δb1,ℓ2(c)b2 = −t(b0)
HNRℓ1
(−b1Bℓ1, −Ac(b2))
(−b1Bℓ1, −b2Bℓ2(d))
δb2,ℓ1(c)b1 = −t(b0)
⋆
17


## Page 18


The ⋆stands for the condition
t(b0) =
(
(2 −d)b1b2,
ℓ1 ̸= ℓ2,
2b1b2,
ℓ1 = ℓ2.
5.1.3
ρ is VNRℓ
In this case, b0, b1, b2 ∈{±1}, and b0b1b2 = 1. Up to conjugacy we may
assume X7 = −aBℓ.
For j = 1, 2, ρj is either HR0 or HNRℓ. If ρ1 and ρ2 are both HR, then
X1 = −b1A, X2 = −b2A so that ρ0 is abelian, which is impossible. Thus
there are three possibilities:
• If ρ1 is HR0 and ρ2 is HNRℓ, then h2 = −k0, a1, a′
1 /∈{±1}, and
Xj = −b1Xj−1 for j = 1, 4, 8. Up to conjugacy, X3 = −Ac1(a1), with
δa1,ℓ(c1) = −t(a′
1)a; The remaining Xj’s are determined by
(X2, X9) = b0(X1, X8)Ca(1/k0),
(X5, X6) = a2(X2, X0)Cb2(q2/p2).
• If ρ1 is HNRℓand ρ2 is HR0, then h1 = −k0, a2, a′
2 /∈{±1}, and X2 =
−b2X0, X5 = −b2X6, X9 = −b2X7. Up to conjugacy, X6 = Ac2(a2),
with δa2,ℓ(c2) = −t(a′
2)a. The remaining Xj’s are determined by
(X1, X8) = b0(X2, X9)Ca(−1/k0),
(X3, X4) = −a1(X0, X1)Cb1(q1/p1).
• If ρ1 and ρ2 are both HNRℓ, then
1
k0
+ 1
h1
+ 1
h2
= 0,
and the Xj’s are determined as follow:
(X1, X8) = −b1(X0, X7)Ca(1/h1),
(X2, X9) = −b2(X0, X7)Ca(−1/h2),
(X3, X4) = −a1(X0, X1)Cb1(q1/p1),
(X5, X6) = a2(X2, X0)Cb2(q2/p2).
Acknowledgement
This work is supported by NSFC-11401014 and NSFC-11501014.
18


## Page 19


References
[1] H.-M. Chen, Trace-free representations of Montesinos links.
J. Knot Theor. Ramif. 27 (2018), no. 8, 1850050 (10 pages).
[2] Y. Jang, Classiﬁcation of 3-bridge arborescent links. Hiroshima Math. J.
41 (2011), 89–136.
[3] L.H. Kauﬀman, S. Lambropoulou, From Tangle Fractions to DNA. In:
Topology in Molecular Biology, pp. 69–110, Springer Berlin Heidelberg,
2003.
[4] L.H. Kauﬀman, S. Lambropoulou, On the classiﬁcation of rational tan-
gles. Adv. Appl. Math. 33 (2004), no. 2, 199–237.
[5] S. Lewallen, Khovanov homology of alternating links and SU(2) repre-
sentations of the link group. arXiv:0910.5047.
[6] X.-S. Lin, A knot invariant via representation spaces. J. Diﬀ. Geom. 35
(1992), 337–357.
[7] F. Nagasato, Y. Yamaguchi, On the geometry of the slice of trace-free
SL2(C)-characters of a knot group. Math. Ann. 354 (2012), 967–1002.
19

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

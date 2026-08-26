---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1708.09008
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1708.09008_Assassins_and_torsion_functors

> Source: 1708.09008_Assassins_and_torsion_functors.pdf

> Pages: 14

---


## Page 1


arXiv:1708.09008v2  [math.AC]  29 Nov 2017
ASSASSINS AND TORSION FUNCTORS
FRED ROHRER
Abstract. Let R be a ring, let a ⊆R be an ideal, and let M be an R-
module.
Let Γa denote the a-torsion functor.
Conditions are given for the
(weakly) associated primes of Γa(M) to be the (weakly) associated primes of
M containing a, and for the (weakly) associated primes of M/Γa(M) to be the
(weakly) associated primes of M not containing a.
1. Introduction
Let R be a ring1, let a ⊆R be an ideal, and let M be an R-module. We denote by
Γa(M) = S
n∈N(0 :M an) the a-torsion submodule of M. The a-torsion functor Γa,
and especially its right derived cohomological functor, i.e., local cohomology with
respect to a, are important tools in commutative algebra and algebraic geometry.
They are mostly studied in case the ring R is noetherian. If R is not noetherian,
then these functors may behave diﬀerently to what is known from the noetherian
case. For example, the functors Γa and Γ√a need not be equal ([9]), and Γa(I)
need not be injective for an injective R-module I ([8]). So, when trying to extend
the theory of local cohomology to not necessarily noetherian rings, one has to be
careful, and some basic results on local cohomology need additional hypotheses in
order to still hold. Another approach, for supporting ideals of ﬁnite type, is via
the notion of weak proregularity as explained in [1] (cf. 2.5).
In this article, we study the interplay between torsion functors and assassins.
Let AssR(M) denote the assassin of M, i.e., the set of prime ideals of R of the
form (0 :R x) for some x ∈M. It is well-known that noetherianness of R implies
the following nice relations between the assassins of Γa(M), M and M/Γa(M):
(A) AssR(Γa(M)) = AssR(M) ∩Var(a);
(B) AssR(M/Γa(M)) = AssR(M) \ Var(a).
2010 Mathematics Subject Classiﬁcation. Primary 13C12; Secondary 13D30, 13D45.
Key words and phrases. Torsion functor, assassin, weak assassin, non-noetherian ring, well-
centered torsion theory, weakly proregular ideal.
1Throughout what follows, rings are understood to be commutative. In general, notation and
terminology follow Bourbaki’s ´El´ements de math´ematique.
1


## Page 2


Assassins and torsion functors
Our ﬁrst goal is to investigate these relations in case R is non-noetherian. Our
main results are as follows.
Statement (A) and the inclusion “⊇” in (B) hold
without any hypothesis (3.1). Statement (B) need not hold in general (3.8, 3.9),
but it does so in the following cases: i) M is noetherian (3.6); ii) a is principal and
idempotent, and M = R (5.1); iii) a and all associated primes of M/Γa(M) are of
ﬁnite type (5.10).
In non-noetherian situations, assassins are often not so well-behaved, in contrast
to weak assassins. The weak assassin of M, denoted by Assf
R(M), is the set of
prime ideals of R that are minimal primes of ideals of the form (0 :R x) for some
x ∈M. Our second goal is to investigate the analogues to (A) and (B) for weak
assassins:
(A′) Assf
R(Γa(M)) = Assf
R(M) ∩Var(a);
(B′) Assf
R(M/Γa(M)) = Assf
R(M) \ Var(a).
Here, our main results are as follows. The inclusion “⊆” in (A′) and the inclusion
“⊇” in (B′) hold without any hypothesis (3.1), and (B′) implies (A′) (3.3). Neither
(A′) nor (B′) holds in general (3.8, 3.9). Statement (A′) holds if a is of ﬁnite type
(5.4). Statement (B′) holds if a is principal (5.5), and if a has a ﬁnite generating
family (ai)n
i=1 such that (ai)m
i=1 is weakly proregular for every m ∈[1, n −1] and
that ai is weakly proregular for every i ∈[2, n] (5.9).
If Γa is a radical (e.g., if a is of ﬁnite type), then it deﬁnes a torsion theory. This
torsion theory is well-centered in the sense of Cahen ([5]) if and only if (A′) holds
for any R-module M (4.4).
Finally, let us note that there is another way to sweeten a non-noetherian situ-
ation. Namely, instead of Γa we can consider the left exact radical Γa deﬁned by
Γa(M) = {x ∈M | SuppR(⟨x⟩R) ⊆Var(a)}. It coincides with Γa if a is of ﬁnite
type, but not in general. We will pursue the study of assassins and weak assassins
of Γa(M) and M/Γa(M) in a subsequent work.
2. Preliminaries
Throughout this section, let R be a ring, let a ⊆R be an ideal, and let M be an
R-module.
(2.1) We denote by Nil(R) the nilradical of R, by Var(a) the set of prime ideals of
R containing a, by min(a) the set of ⊆-minimal elements of Var(a), by NZDR(M)
and ZDR(M) the sets of non-zerodivisors and zerodivisors on M, resp., and by
SuppR(M) the support of M.
2


## Page 3


Assassins and torsion functors
(2.2) A prime ideal p ⊆R is said to be associated to M if there exists x ∈M
with p = (0 :R x); it is said to be weakly associated to M if there exists x ∈M
with p ∈min(0 :R x). The sets AssR(M) and Assf
R(M) of associated and weakly
associated primes of M are called the assassin of M and the weak assassin of M,
resp.
If not indicated otherwise, the following facts about assassins and weak assassins
are proven in [2, IV.1.1; IV.1 Exercise 17] and [11, 00L9; 0546].
(2.3) A) We have {p ∈Assf
R(M) | p is of ﬁnite type} ⊆AssR(M) ⊆Assf
R(M); if
R or M is noetherian, then AssR(M) = Assf
R(M).
B) If p ∈Spec(R), then AssR(R/p) = Assf
R(R/p) = {p}.
C) We have M = 0 if and only if Assf
R(M) = ∅.
D) If 0 →L →M →N →0 is a short exact sequence of R-modules, then
AssR(L) ⊆AssR(M) ⊆AssR(L) ∪AssR(N)
and
Assf
R(L) ⊆Assf
R(M) ⊆Assf
R(L) ∪Assf
R(N).
E) If (Mi)i∈I is a ﬁltering inductive system of R-modules, then
{p ∈AssR(lim
−→
i∈I
Mi) | p is of ﬁnite type} ⊆
[
i∈I
AssR(Mi),
as follows from the proof of [6, 2.10].
F) Let S ⊆R be a subset, and let η: M →S−1M denote the canonical morph-
ism. Then, Assf
R(Ker(η)) = {p ∈Assf
R(M) | p ∩S = ∅}, and there is a bijection
{p ∈Assf
R(M) | p ∩S = ∅}
∼
=
−→Assf
S−1R(S−1M), p 7→S−1p.
G) We have SuppR(M) = {p ∈Spec(R) | ∃q ∈Assf
R(M) : q ⊆p}. If N ⊆M is a
sub-R-module, then SuppR(M) = SuppR(N)∪SuppR(M/N) ([2, II.4.4 Proposition
16]).
H) Suppose M is of ﬁnite type, and let N be a further R-module. In [2, IV.1.4
Proposition 10], it is shown that if R is noetherian, then
AssR(HomR(M, N)) = AssR(N) ∩SuppR(M).
A careful analysis of the proof reveals that the noetherian hypothesis is superﬂu-
ous, and moreover that Assf
R(HomR(M, N)) ⊆Assf
R(N) ∩SuppR(M). This last
inclusion need not be an equality, as can be seen from [12, Example 4].
3


## Page 4


Assassins and torsion functors
If not indicated otherwise, the following facts about torsion functors are proven
in [4, Chapters 1–2] (where one has to check that the hypothesis of a noetherian
ring is not used) and [3, Chapter 1].
(2.4) A) The a-torsion functor, denoted by Γa, is the subfunctor of IdMod(R) with
Γa(M) = S
n∈N(0 :M an) for every R-module M. It is left exact.
B) A subfunctor F of IdMod(R) is called a radical if F(M/F(M)) = 0 for every
R-module M. The functor Γa need not be a radical, but it is so if a is of ﬁnite
type. Moreover, if M is noetherian, then Γa(M/Γa(M)) = 0.
C) Suppose that M is noetherian. Then, there exists n ∈
N with anΓa(M) = 0.
If moreover Γa(M) = 0, then NZDR(M) ∩a ̸= ∅.
D) Let S ⊆R be a subset. The canonical monomorphism of S−1R-modules
S−1Γa(M) ֌ ΓS−1a(S−1M) need not be an isomorphism, but it is so if a is of
ﬁnite type.
E) If Γa is a radical and HomR(M, N) = 0 for every a-torsionfree R-module N,
then Γa(M) = M. (Indeed, we consider the short exact sequence
0 −→Γa(M)
h
−→M
l
−→M/Γa(M) −→0.
Then, Γa(M/Γa(M)) = 0, hence l = 0, thus h is an isomorphism, and therefore
Γa(M) = M.)
F) There is a canonical monomorphism of R-modules
M/Γa(M) ֌ lim
−→
n∈N
HomR(an, M).
We recall the notion of weak proregularity of an ideal and refer the reader to
[1], [7] and [10] for details.
(2.5) A) Suppose a is of ﬁnite type.
Let a = (ai)n
i=1 be a ﬁnite generating
family of a. The right derived cohomological functor of Γa is denoted by (Hi
a)i∈Z
and called local cohomology with respect to a. ˇCech cohomology with respect to
a yields a further cohomological functor, denoted by ( ˇHi(a, •))i∈Z.
There is a
canonical isomorphism Γa(•) ∼= ˇH0(a, •) that can be canonically extended to a
morphism of δ-functors γa: (Hi
a(•))i∈Z →( ˇHi(a, •))i∈Z. The sequence a is called
weakly proregular if γa is an isomorphism. The ideal a is called weakly proregular
if it has a weakly proregular ﬁnite generating family, and this holds if and only if
every ﬁnite generating family of a is weakly proregular.
B) If a is weakly proregular and i ∈
N∗, then Hi
a◦Γa = 0, as follows immediately
from the deﬁnitions of weak proregularity and ˇCech cohomology.
4


## Page 5


Assassins and torsion functors
3. Basic relations, first examples, and counterexamples
Throughout this section, let R be a ring, let a ⊆R be an ideal, and let M be an
R-module.
(3.1) Proposition
a) AssR(Γa(M)) = AssR(M) ∩Var(a).
b) Assf
R(Γa(M)) ⊆Assf
R(M) ∩Var(a).
c) AssR(M/Γa(M)) ⊇AssR(M) \ Var(a).
d) Assf
R(M/Γa(M)) ⊇Assf
R(M) \ Var(a).
Proof. We have AssR(Γa(M)) ⊆AssR(M) and Assf
R(Γa(M)) ⊆Assf
R(M) by 2.3
D). For p ∈Assf
R(Γa(M)) there exists x ∈Γa(M) with (0 :R x) ⊆p, hence there
exists n ∈
N with anx = 0, and it follows that an ⊆(0 :R x) ⊆p, thus a ⊆p. By
2.3 A) this shows
AssR(Γa(M)) ⊆Assf
R(Γa(M)) ⊆Var(a).
So, we have proven b) and the inclusion “⊆” in a).
For p ∈AssR(M) ∩Var(a) there exists x ∈M with a ⊆p = (0 :R x), implying
ax = 0, hence x ∈Γa(M), and thus p ∈AssR(Γa(M)). This proves the inclusion
“⊇” in a).
By 2.3 D) we have
AssR(M) ⊆AssR(Γa(M)) ∪AssR(M/Γa(M))
and
Assf
R(M) ⊆Assf
R(Γa(M)) ∪Assf
R(M/Γa(M)).
Thus, c) and d) follow immediately from a) and b).
□
(3.2) The R-module M is called a-fair if
AssR(M/Γa(M)) = AssR(M) \ Var(a);
it is called weakly a-quasifair if
Assf
R(Γa(M)) = Assf
R(M) ∩Var(a),
and weakly a-fair if
Assf
R(M/Γa(M)) = Assf
R(M) \ Var(a).
(3.3) Proposition
If M is weakly a-fair, then it is weakly a-quasifair.
Proof. By 2.3 D) we have
Assf
R(M) ∩Var(a) ⊆Assf
R(Γa(M)) ∪(Assf
R(M/Γa(M)) ∩Var(a)) =
Assf
R(Γa(M)) ∪((Assf
R(M) \ Var(a)) ∩Var(a)) = Assf
R(Γa(M)).
5


## Page 6


Assassins and torsion functors
So, the claim follows from 3.1 b).
□
(3.4) Examples A) Every R-module is R-fair and weakly R-fair.
B) If a is nilpotent, then every R-module is a-fair and weakly a-fair.
C) Every a-torsion R-module is a-fair and weakly a-fair.
D) If p ∈Spec(R), then the R-module R/p is a-fair and weakly a-fair, as follows
on use of 2.3 B). In particular, if R is integral, then the R-module R is a-fair and
weakly a-fair.
E) Suppose a ⊆Nil(R). Then, M is a-fair if and only if AssR(M/Γa(M)) = ∅,
and this is fulﬁlled if Γa is a radical. Furthermore, M is weakly a-fair if and only
if Assf
R(M/Γa(M)) = ∅, and, by 2.3 C), this holds if and only if M is an a-torsion
R-module.
(3.5) Proposition
If every monogeneous R-module is weakly a-quasifair, a-fair,
or weakly a-fair, resp., then so is every R-module.
Proof. Let M be an R-module. Suppose that every monogeneous R-module is a-
fair or weakly a-fair, resp. Let p ∈AssR(M/Γa(M)) or p ∈Assf
R(M/Γa(M)), resp.
There exists x ∈M with p = (0 :R x) or p ∈min(0 :R x), resp., where x denotes
the canonical image of x in M/Γa(M). Then, ⟨x⟩R/Γa(⟨x⟩R) ∼= ⟨x⟩R ⊆M/Γa(M),
and thus
p ∈AssR(⟨x⟩R) = AssR(⟨x⟩) \ Var(a) ⊆AssR(M) \ Var(a)
or
p ∈Assf
R(⟨x⟩R) = Assf
R(⟨x⟩) \ Var(a) ⊆Assf
R(M) \ Var(a),
resp. by 2.3 D). Now, 3.1 c), d) implies that M is a-fair or weakly a-fair, resp.
Suppose that every monogeneous R-module is weakly a-quasifair.
Let p ∈
Assf
R(M) ∩Var(a). There exists x ∈M with p ∈min(0 :R x). It follows that
p ∈Assf
R(⟨x⟩R) ∩Var(a) = Assf
R(Γa(⟨x⟩R)) ⊆Assf
R(Γa(M))
by 2.4 A) and 2.3 D), and so 3.1 b) implies that M is weakly a-quasifair.
□
(3.6) Proposition
If R or M is noetherian, then M is a-fair and weakly a-fair.
Proof. By 2.3 A) it suﬃces to show that M is a-fair, and by 3.5 it suﬃces to
consider the case that M is noetherian. Let p ∈AssR(M/Γa(M)). Since M is
noetherian, we have Γa(M/Γa(M)) = 0 by 2.4 B), so since M/Γa(M) is noetherian,
too, there exists x ∈NZDR(M/Γa(M))∩a by 2.4 C). As p ⊆S AssR(M/Γa(M)) ⊆
ZDR(M/Γa(M)), it follows that x ∈a \ p, and therefore p /∈Var(a). Furthermore,
there exists v ∈M such that, setting v = v + Γa(M) ∈M/Γa(M), we have
6


## Page 7


Assassins and torsion functors
p = (0 :R v), hence pv = 0, and thus pv ⊆Γa(M). Since M is noetherian, there
exists n ∈
N with anΓa(M) = 0 by 2.4 C), implying pxnv = xnpv ⊆xnΓa(M) = 0,
and thus p ⊆(0 :R xnv). If a ∈(0 :R xnv), then (axn)v = a(xnv) = 0 ∈Γa(M),
hence axnv = 0, thus axn ∈(0 :R v) = p, and as x /∈p it follows that a ∈p.
Therefore, (0 :R xnv) ⊆p, hence p = (0 :R xnv), and thus p ∈AssR(M). The
claim follows now from 3.1 c).
□
(3.7) Proposition
Let R be 0-dimensional and local with maximal ideal m.
a) The R-module R is weakly m-quasifair if and only if Γm(R) ̸= 0.
b) The R-module R is weakly m-fair if and only if m is nilpotent.
c) If Γm(R) = m, then the R-module R is weakly m-quasifair, but neither m-fair
nor weakly m-fair.
d) If Γm(R) = 0, then the R-module R is m-fair, but not weakly m-quasifair.
Proof. a) The R-module R is weakly m-quasifair if and only if Assf
R(Γm(R)) = {m},
hence if and only if Assf
R(Γm(R)) ̸= ∅, and thus, by 2.3 C), if and only if Γm(R) ̸= 0.
b) The R-module R is weakly m-fair if and only if Assf
R(R/Γm(R)) = ∅, thus,
by 2.3 C), if and only R/Γm(R) = 0, and hence if and only if m is nilpotent.
c) The R-module R is weakly m-quasifair by a).
As AssR(R) \ Var(m) =
Assf
R(R) \ Var(m) = ∅, we get, on use of 2.3 A),
{m} ⊆AssR(R/m) = AssR(R/Γm(R)) ⊆Assf
R(R/Γm(R)) ⊆{m},
and therefore the remaining claims.
d) As Γm(R) = 0, we have m /∈AssR(R) ⊆Var(m). On use of 3.1 a) we thus get
AssR(R) \ Var(m) = ∅= AssR(Γm(R)) =
AssR(R) ∩Var(m) = AssR(R) = AssR(R/Γm(R)).
Hence, the R-module R is m-fair. By a), it is not weakly a-quasifair.
□
(3.8) Proposition
There exist a ring R, an ideal a ⊆R, and an R-module M
such that M is weakly a-quasifair, but neither a-fair nor weakly a-fair.2
Proof. Let K be a ﬁeld and let
R = K[(Xi)i∈N]/⟨{XiXj | i, j ∈
N, i ̸= j} ∪{Xi+1
i
| i ∈
N}⟩K[(Xi)i∈N].
For i ∈
N we denote by Yi the image of Xi in R.
Let m = ⟨Yi | i ∈
N⟩R.
Then, R is a 0-dimensional local ring with maximal ideal m.
If n ∈
N, then
mn = ⟨Y n
i
| i ≥n⟩R, hence (0 :R mn) = ⟨Y max{1,i−n+1}
i
| i ∈
N⟩R, and thus
Γm(R) = m. Now, setting a = m and M = R, the claim follows from 3.7.
□
2This shows that the converse of 3.3 need not hold.
7


## Page 8


Assassins and torsion functors
(3.9) Proposition
There exist a ring R, an ideal a ⊆R, and an R-module M
such that M is a-fair, but not weakly a-quasifair.
Proof. Let K be a ﬁeld, let Q denote the additive monoid of positive rational
numbers, let R = K[Q] denote the algebra of Q over K, and let {eα | α ∈Q}
denote its canonical basis. Then, m = ⟨eα | α > 0⟩R is a maximal ideal. We
consider S = Rm and n = mm. Then, S is a 1-dimensional local valuation ring
with idempotent maximal ideal n ([8, 2.2]). Let a = ⟨e1
1 ⟩S, let T = S/a, and let
p = n/a. Then, T is a 0-dimensional local ring with idempotent maximal ideal p.
We will show now that Γp(T) = 0, and then 3.7 d) will yield the claim. Since
p is idempotent, we have to show that if f ∈T with pf = 0, then f = 0. By
construction of T and S we have to show that if f ∈R with nf
1 ⊆a, then f
1 ∈a.
So, let f ∈R with nf
1 ⊆a. We assume that f
1 /∈a and will derive a contradiction.
There exist l ∈
N, a family (fi)l
i=0 in K \ 0, and a strictly increasing family (βi)l
i=0
in Q with f = Pl
i=0 fieβi. If β0 ≥1, then we get the contradiction f
1 ∈a. So,
β0 < 1, and hence there exists α ∈Q with α > 0 and β0 + α < 1. As nf
1 ⊆a
it follows that
eα
1
f
1 ∈a, and thus there exist g ∈R \ 0 and t ∈R \ m with
feα
1 = ge1
t ∈S. As R is integral this implies
(∗)
tfeα = ge1.
There exist k ∈
N, a family (ti)k
i=0 in K \0, and a strictly increasing family (αi)k
i=1
in Q \ 0 with t = t0 + Pk
i=1 tieαi. Furthermore, there exist m ∈
N, a family (gi)m
i=0
in K \ 0, and a strictly increasing family (γi)m
i=0 in Q with g = Pm
i=0 gieγi. Thus,
(∗) takes the form
(∗∗)
l
X
j=0
t0fjeα+βj +
k
X
i=1
l
X
j=0
tifjeα+αi+βj =
m
X
i=0
gieγi+1.
Both sides of (∗∗) being nonzero, there exists the smallest δ ∈Q such that eδ occurs
on both sides. As αi > 0 for every i ∈[1, k], the left side yields δ = α+β0, while the
right side yields δ = γ0 + 1. So, we get the contradiction 1 > α + β0 = γ0 + 1 ≥1,
and thus Γp(T) = 0 as claimed.
□
(3.10) Questions We saw in 3.3 that a weakly a-fair R-module is weakly a-
quasifair.
On the other hand, 3.8 and 3.9 show that a weakly a-quasifair R-
module need not be a-fair or weakly a-fair, and that an a-fair R-module need not
be weakly a-quasifair or weakly a-fair. Thus, in this general setting we are left
with the following questions:
(∗) Is a weakly a-fair R-module necessarily a-fair?
(∗∗) Is a weakly a-quasifair and a-fair R-module necessarily weakly a-fair?
8


## Page 9


Assassins and torsion functors
By combinatorial observations one can show that if R is a 0-dimensional local ring
or a 1-dimensional local ring with a single minimal prime ideal that is of ﬁnite
type, then every weakly a-fair R-module is a-fair. But we were not able to answer
the above questions in general.
4. Results in the radical case
Throughout this section, let R be a ring, and let a ⊆R be an ideal.
(4.1) Proposition
If Γa is a radical and M is an R-module, then
AssR(M/Γa(M)) ∩Var(a) = ∅.
Proof. Applying 3.1 a) to the R-module M/Γa(M) yields
∅= AssR(0) = AssR(Γa(M/Γa(M))) = AssR(M/Γa(M)) ∩Var(a),
and thus our claim.
□
(4.2) Proposition
Let M be an R-module. Then:
a) Assf
R(M) ∩Var(a) = ∅⇒Γa(M) = 0 ⇒AssR(M) ∩Var(a) = ∅.
b) Γa(M) = M ⇒Assf
R(M) ⊆Var(a) ⇒AssR(M) ⊆Var(a).
Proof. a) Suppose Assf
R(M) ∩Var(a) = ∅, and assume there exists x ∈Γa(M) \ 0.
Then, there exists p ∈min(0 :R x), and so we have p ∈Assf
R(M). Moreover, we
have the situation
Γa(M) ⊇⟨x⟩R
∼
=
←−R/(0 :R x) ։ R/p,
implying Γa(R/p) = R/p, and therefore the contradiction a ⊆p. This proves the
ﬁrst implication. The second one follows from 3.1 a).
b) (cf. [8, 1.14]) If Γa(M) = M and p ∈Assf
R(M), then there exists x ∈M
such that p ∈min(0 :R x), and there exists n ∈
N with anx = 0. It follows that
an ⊆(0 :R x) ⊆p, hence a ⊆p. This proves the ﬁrst implication. The second one
holds by 2.3 A).
□
(4.3) A) The ideal a is called centered if the ﬁrst implication in 4.2 a) is an
equivalence for every R-module M, i.e., if
Γa(M) = 0 ⇔Assf
R(M) ∩Var(a) = ∅
for every R-module M; it is called half-centered if the ﬁrst implication in 4.2 b) is
an equivalence for every R-module M, i.e., if
Γa(M) = M ⇔Assf
R(M) ⊆Var(a)
9


## Page 10


Assassins and torsion functors
for every R-module M.
Finally, a is called well-centered if it is centered and
half-centered.
B) Suppose Γa is a radical (2.4 B)). Denoting by Ta and Fa the classes of a-
torsion and a-torsionfree R-modules, resp., we get a torsion theory (Ta, Fa). It is
readily checked now that (Ta, Fa) is half-centered or well-centered, resp., in the
sense of [5] if and only if the ideal a is so.
C) (cf. [8, 1.14; 1.21 B)]) An arbitrary ideal need not be half-centered, but ideals
of ﬁnite type are so. Indeed, if R is a 0-dimensional local ring whose maximal ideal
m is not nilpotent (e.g., the ring in 3.8), then R is not an m-torsion module, but
Assf
R(R) ⊆Spec(R) = Var(m), and therefore m is not half-centered.
On the
other hand, if a is of ﬁnite type and Assf
R(M) ⊆Var(a), then for x ∈M we
have a ⊆
p
(0 :R x), hence there exists n ∈
N with anx = 0, and therefore a is
half-centered.
(4.4) Proposition
If Γa is a radical, then the following statements are equi-
valent: (i) a is centered; (ii) a is well-centered; (iii) Every R-module is weakly
a-quasifair.
Proof. “(i)⇒(ii)”: Suppose a is centered. Let M be an R-module with Assf
R(M) ⊆
Var(a). Let P be an a-torsionfree R-module, and let f ∈HomR(M, P). Then,
Assf
R(M/ Ker(f)) ⊆SuppR(M/ Ker(f)) ⊆SuppR(M) ⊆Var(a)
by 2.3 G). Moreover, f induces a monomorphism of R-modules M/ Ker(f) ֌ P.
So, M/ Ker(f) is a-torsionfree, and thus
Assf
R(M/ Ker(f)) = Assf
R(M/ Ker(f)) ∩Var(a) = ∅
by our hypothesis. It follows that M/ Ker(f) = 0 by 2.3 C), and therefore f = 0.
This shows that whenever P is an a-torsionfree R-module, then HomR(M, P) = 0.
Since Γa is a radical, this implies M = Γa(M) by 2.4 E). So, a is half-centered and
therefore well-centered.
“(ii)⇒(iii)”: Suppose a is well-centered. By 2.3 D) we have
Assf
R(M) ∩Var(a) ⊆Assf
R(Γa(M)) ∪(Assf
R(M/Γa(M)) ∩Var(a)).
Our hypotheses imply Assf
R(M/Γa(M)) ∩Var(a) = ∅, hence Assf
R(M) ∩Var(a) ⊆
Assf
R(Γa(M)), and then 3.1 b) yields the claim.
“(iii)⇒(i)”: Suppose every R-module is weakly a-quasifair. Let M be an a-
torsionfree R-module. Then, Assf
R(M) ∩Var(a) = Assf
R(Γa(M)) = Assf
R(0) = ∅,
and thus a is centered.
□
10


## Page 11


Assassins and torsion functors
(4.5) Suppose that AssR(M) = Assf
R(M) for every R-module M. Then, a is
centered. If in addition Γa is a radical, and in particular if a is of ﬁnite type, then
a is well-centered by 4.4. It follows thus from 2.3 A) that ideals in noetherian rings
are well-centered.
5. Results for ideals of finite type
Throughout this section, let R be a ring, and let a ⊆R be an ideal.
(5.1) Proposition
If a is principal and idempotent, then the R-module R is
a-fair.
Proof. There exists x ∈R with a = ⟨x⟩R, and Γa(R) = (0 :R x). We get
R/Γa(R) = R/(0 :R x) ∼= ⟨x⟩R = a ⊆R,
hence AssR(R/Γa(R)) ⊆AssR(R) by 2.3 D), and so the claim follows from 3.1 c),
2.4 B) and 4.1.
□
(5.2) Corollary
If R is absolutely ﬂat and a is of ﬁnite type, then the R-module
R is a-fair.
Proof. Immediately from 5.1, since ideals of ﬁnite type in absolutely ﬂat rings are
principal and idempotent.
□
(5.3) Proposition
If a is of ﬁnite type and M is an R-module, then
Assf
R(M/Γa(M)) ∩Var(a) = ∅.
Proof. We assume there exists p ∈Assf
R(M/Γa(M)) ∩Var(a).
By exactness
of localisation we have a canonical isomorphism of Rp-modules (M/Γa(M))p ∼=
Mp/Γa(M)p. Since a is of ﬁnite type, we have a canonical isomorphism of Rp-
modules Mp/Γa(M)p ∼= Mp/Γap(Mp) by 2.4 D), hence pp ∈Assf
Rp((M/Γa(M))p) =
Assf
Rp(Mp/Γap(Mp)) by 2.3 F). So, there exists x ∈(Mp/Γap(Mp)) \ 0 with pp ∈
min(0 :Rp x). Since pp is the unique maximal ideal of Rp it follows that pp =
p
(0 :Rp x). Since p ∈Var(a) we have ap ⊆pp =
p
(0 :Rp x). So, as a is of ﬁnite
type, the same holds for ap, and thus there exists n ∈
N with (ap)n ⊆(0 :Rp x).
This implies x ∈Γap(Mp/Γap(Mp)). But as ap is of ﬁnite type we know that Γap is
a radical (2.4 B)), and thus we get the contradiction x = 0. Herewith the claim is
proven.
□
(5.4) Proposition
If a is of ﬁnite type, then every R-module is weakly a-quasi-
fair.
11


## Page 12


Assassins and torsion functors
Proof. Let M be an R-module with Γa(M) = 0. Since a is of ﬁnite type, 5.3
implies
Assf
R(M/Γa(M)) ∩Var(a) = ∅,
and thus, by 2.3 D), it follows that
Assf
R(M) ∩Var(a) ⊆Assf
R(Γa(M)) ∪(Assf
R(M/Γa(M)) ∩Var(a)) = Assf
R(Γa(M)).
Therefore, a is centered, and so 2.4 B) and 4.4 yield the claim.
□
(5.5) Proposition
If a is principal, then every R-module is weakly a-fair.
Proof. Let a = ⟨a⟩R with a ∈R, and let M be an R-module. As Γ⟨a⟩R(M) is the
kernel of the canonical morphism of R-modules ηa: M →Ma, we have
Assf
R(M/Γ⟨a⟩R(M)) = {p ∈Assf
R(M) | a /∈p} ⊆Assf
R(M)
by 2.3 F), and thus 5.3 implies the claim.
□
(5.6) Corollary
If R is a Bezout ring and a ⊆R is an ideal of ﬁnite type, then
every R-module is weakly a-fair.
Proof. Immediately from 5.5, since ideals of ﬁnite type of Bezout rings are prin-
cipal.
□
(5.7) Lemma
Let b ⊆R be a weakly proregular ideal with Γb ◦Γa = Γa, and let
M be an R-module. Then, there is an isomorphism of R-modules
(M/Γa(M))/Γb(M/Γa(M)) ∼= M/Γb(M).
Proof. Applying the functor Γb to the short exact sequence
0 −→Γa(M) −→M −→M/Γa(M) −→0
and keeping in mind that Γb ◦Γa = Γa we get an exact sequence
0 −→Γa(M) −→Γb(M) −→Γb(M/Γa(M)) −→H1
b(Γa(M)).
By 2.5 B) we have H1
b ◦Γb = 0, hence by our hypothesis H1
b(Γa(M)) = 0. The
claim follows from this.3
□
(5.8) Proposition
Let b, c ⊆R be weakly proregular ideals such that a = b + c,
and let M be an R-module. If M is weakly b-fair and weakly c-fair, then it is
weakly a-fair.
3It is seen from the proof that in fact we do not need b to be weakly proregular, but rather to have
a ﬁnite generating family b such that the canonical morphism γ1
b : H1
b →ˇH1
b is an isomorphism.
12


## Page 13


Assassins and torsion functors
Proof. Let p ∈Assf
R(M/Γa(M)). Since a is of ﬁnite type this implies p /∈Var(a)
by 5.3, and so we may without loss of generality suppose that p /∈Var(b). Now,
we have
Assf
R(M/Γa(M)) ⊆Assf
R(Γb(M/Γa(M))) ∪Assf
R((M/Γa(M))/Γb(M/Γa(M)))
and Assf
R(Γb(M/Γa(M))) ⊆Var(b) by 2.3 D) and 3.1 b). On use of 5.7 and our
hypothesis it follows that
p ∈Assf
R((M/Γa(M))/Γb(M/Γa(M))) = Assf
R(M/Γb(M)) ⊆Assf
R(M).
Thus, 3.1 d) yields the claim.
□
(5.9) Proposition
If there exists a generating family (ai)n
i=1 of a such that (ai)m
i=1
is weakly proregular for every m ∈[1, n −1] and that ai is weakly proregular for
every i ∈[2, n], then every R-module is weakly a-fair.
Proof. We show the claim by induction on n. If n ≤1 then we are done by 3.4 B)
and 5.5. Let n > 1, and suppose the claim to hold for strictly smaller values of n.
Let b = ⟨a1, . . . , an−1⟩R and c = ⟨an⟩R. Then, b and c are weakly proregular, and
every R-module is weakly b-fair and weakly c-fair by our hypothesis. Therefore,
5.8 implies that every R-module is weakly a-fair, and thus the claim is proven.
□
(5.10) Proposition
Let a be of ﬁnite type, and let M be an R-module such that
every (weakly) associated prime of M/Γa(M) is of ﬁnite type. Then, M is (weakly)
a-fair.
Proof. By 2.3 A) it suﬃces to show the claim about assassins. By 2.4 F) we have
a monomorphism M/Γa(M) ֌ lim
−→n∈N HomR(an, M), and so 2.3 D), E) and H)
imply
AssR(M/Γa(M)) ⊆{p ∈AssR(lim
−→
n∈N
HomR(an, M)) | p is of ﬁnite type} ⊆
[
n∈N
AssR(HomR(an, M)) ⊆AssR(M).
The claim follows now from 5.3.
□
(5.11) Questions We are left with the following questions, on whose answers
we dare not speculate.
(∗) Suppose Γa is a radical. Is then every R-module weakly a-quasifair, a-fair or
weakly a-fair?
(∗∗) Suppose a is of ﬁnite type. Is then every R-module a-fair or weakly a-fair?
13


## Page 14


Assassins and torsion functors
Acknowledgements. I thank the referee for his careful reading and his sug-
gestions, and – as so often – Pham Hung Quy for suggesting nice counterexamples.
References
[1] L. Alonso Tarr´ıo, A. Jerem´ıas L´opez, J. Lipman, Local homology and cohomology on
schemes. Ann. Sci. ´Ec. Norm. Sup´er. (4) 30 (1997), 1–39. Corrections available at
http://www.math.purdue.edu/~lipman/papers/homologyfix.pdf
[2] N. Bourbaki, ´El´ements de math´ematique. Alg`ebre commutative. Chapitres 1 `a 4. Masson,
1985.
[3] M. Brodmann, S. Fumasoli, F. Rohrer, First lectures on local cohomology. (In preparation)
[4] M. P. Brodmann, R. Y. Sharp, Local cohomology. Second edition. Cambridge Stud. Adv.
Math. 136. Cambridge Univ. Press, 2013.
[5] P.-J. Cahen, Torsion theory and associated primes. Proc. Amer. Math. Soc. 38 (1973),
471–476.
[6] P. ˇCoupek, Tilting theory for quasicoherent sheaves. Diploma thesis. Charles University
Prague, 2016.
[7] M. Porta, L. Shaul, A. Yekutieli, On the homology of completion and torsion. Algebr.
Represent. Theory 17 (2014), 31–67.
[8] P. H. Quy, F. Rohrer, Injective modules and torsion functors. Comm. Algebra 45 (2017),
285–298.
[9] F. Rohrer, Torsion functors with monomial support. Acta Math. Vietnam. 38 (2013),
293–301.
[10] P. Schenzel, Proregular sequences, local cohomology, and completion. Math. Scand. 92
(2003), 161–180.
[11] The Stacks Project Authors, Stacks project. http://stacks.math.columbia.edu
[12] S. Yassemi, A survey of associated and coassociated primes. Vietnam J. Math. 28 (2000),
195–208.
Grosse Grof 9, 9470 Buchs, Switzerland
E-mail address: fredrohrer@math.ch
14

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
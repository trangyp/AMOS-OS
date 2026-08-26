---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1812.02644
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1812.02644_Addendum__A_separation_in_modulus_property_of_the_zeros_of_a_partial_theta_funct

> Source: 1812.02644_Addendum__A_separation_in_modulus_property_of_the_zeros_of_a_partial_theta_funct.pdf

> Pages: 9

---


## Page 1


arXiv:1812.02644v1  [math.CA]  6 Dec 2018
Addendum: A separation in modulus property of the zeros of a
partial theta function
Vladimir Petrov Kostov
Universit´e Cˆote d’Azur, CNRS, LJAD, France,
e-mail: kostov@math.unice.fr
Abstract
We consider the partial theta function θ(q, z) := P∞
j=0 qj(j+1)/2zj, where z ∈C is a
variable and q ∈C, 0 < |q| < 1, is a parameter.
Set D(a) := {q ∈C, 0 < |q| ≤a,
arg(q) ∈[π/2, 3π/2]}. We show that for k ∈N and q ∈D(0.55), there exists exactly one zero
of θ(q, .) (which is a simple one) in the open annulus |q|−k+1/2 < z < |q|−k−1/2 (if k ≥2) or
in the punctured disk 0 < z < |q|−3/2 (if k = 1). For k = 1, 4, 5, 6, . . ., this holds true for
q ∈D(0.6) as well.
Keywords: partial theta function; separation in modulus
AMS classiﬁcation: 26A06
1
The new results
In this addendum to [3] we consider the partial theta function θ(q, z) := P∞
j=0 qj(j+1)/2zj. The
series converges for q ∈D1, z ∈C, where Da denotes the open disk centered at 0 and of radius
a. We regard q as a parameter and z as a variable.
Deﬁnition 1. For 0 < a < b and for q ∈D1 \ 0 ﬁxed, denote by Ua,b ⊂C the open annulus
{|q|−a < |z| < |q|−b}. For q ﬁxed, we say that strong separation (in modulus) of the zeros of θ
takes place for k ≥k0, if for any k ≥k0, there exists a unique zero ξk of θ(q, .) which is a simple
one and
|ξk| ∈Uk−1/2,k+1/2
,
if
k ≥2
,
and
ξk ∈(D|q|−3/2 \ 0)
,
if
k = 1 ,
(1)
while the remaining k0 −1 zeros (counted with multiplicity) are in D|q|−k0+1/2 \ 0. If k0 = 1,
then we say that the zeros of θ are strongly separated. (One can notice that the cases k0 = 1
and k0 = 2 are identical.)
It is shown in [3] that the zeros of θ are strongly separated for 0 < |q| ≤c0 := 0.2078750206 . . .,
see Lemma 1 and its proof therein. Set D(a) := {q ∈C, 0 < |q| ≤a, arg(q) ∈[π/2, 3π/2]}.
Theorem 2. (1) For q ∈D(0.55), the zeros of θ are strongly separated.
(2) For q ∈D(0.6), conditions (1) hold true for k = 1, 4, 5, 6, . . ., and there are exactly two
zeros of θ (counted with multiplicity) in U3/2,7/2.
Remarks 3. (1) The domain D(0.55)∪(Dc0 \0) is much larger than the domain Dc0 \0 in which
strong separation of the zeros of θ is guaranteed by Lemma 1 in [3]. It is impossible to extend
1


## Page 2


Theorem 2 to the whole of D0.55 \ 0, because for certain values of q in the right half of D0.55 \ 0,
the function θ(q, .) has double zeros, see [4] and [3].
(2) Numerical computations suggest that in part (1) of Theorem 2 the number 0.55 can be
replaced by 0.6, see Remark 14.
2
Comments
Theorem 2 can be compared with the results of [3]. Set α0 :=
√
3/2π = 0.2756644477 . . .. Parts
(1) and (4) of Theorem 5 in [3] read:
Theorem 4. (1) For n ≥5 and for |q| ≤1 −1/(α0n), strong separation of the zeros ξk of θ
occurs for k ≥n.
(2) For 0 < |q| ≤1/2, strong separation of the zeros of θ occurs for k ≥4.
Part (1) of the theorem implies that for k ≥n ≥5, one has
(1 −1/(α0k))−k+1/2 =: mk ≤|ξk| ≤Mk := (1 −1/(α0k))−k−1/2 .
The following table gives an idea how the numbers mn and Mn decrease as n increases (both
of them tend to e1/α0 = 37.62236657 . . . as n →∞). We list the truncations up to the second
decimal for the numbers τn := 1 −1/(α0n) and up to the ﬁrst decimal for mn and Mn. The
numbers mn and Mn are the internal and external radius of the open annulus to which the zero
ξn belongs for |q| = τn.
n
5
6
7
8
9
10
15
20
25
30
τn
0.27
0.39
0.48
0.54
0.59
0.63
0.75
0.81
0.85
0.87
mn
336.2
164.5
115.2
92.8
80.2
72.2
55.3
49.5
46.5
44.7
Mn
1225.1
416.1
239.1
169.8
134.4
113.4
73.0
60.5
54.4
50.9
3
Proof of Theorem 2
We use the same method of proof as the one of the proof of Theorem 5 in [3], but with more
accurate estimations. We remind that (see [3]) θ = Θ∗−G, where Θ∗(q, z) := P∞
j=−∞qj(j+1)/2zj
and G(q, z) := P−1
−∞qj(j+1)/2zj = P∞
j=1 qj(j−1)/2z−j. Set
Q :=
∞
Y
j=1
(1 −qj)
,
U :=
∞
Y
j=1
(1 + zqj)
and
R :=
∞
Y
j=1
(1 + qj−1/z) .
We recall that by formula (4) in [3] (resulting from the Jacobi triple product), one has Θ∗=
QUR.
Lemma 5. For q ∈D(0.6), one has |Q| ≥1.2.
Proof. We set Q := Q0Q1, where Q0 := Q11
j=1(1−qj) and Q1 := Q∞
j=12(1−qj). For the quantity
|Q1| one obtains the minoration
2


## Page 3


|Q1| ≥
∞
Y
j=12
(1 −|q|j) ≥
∞
Y
j=12
(1 −0.6j) = γ := 0.9945691384 . . . .
Hence to prove the lemma it suﬃces to show that for q ∈D(0.6), the inequality
|Q0| ≥1.2/γ = 1.206552620 . . .
holds true. This can be proved using the maximum principle. The polynomial Q0 has no zeros
in D(0.6) hence minD(0.6) |Q0| = 1/ maxD(0.6) |1/Q0| is attained on the border ∂D(0.6) of the
domain D(0.6).
The restrictions of |Q0|2 to the segment (resp.
to the arc) of ∂D(0.6) are
a polynomial and a trigonometric polynomial respectively and the latter displayed inequality
is readily checked numerically. The check can be limited to the upper half-plane, because all
coeﬃcients of Q are real hence Q(¯q) = Q(q).
Lemma 6. For q ∈D(0.6), k ∈N, k ≥5 and |z| = |q|−k+1/2, one has θ(q, z) ̸= 0.
Proof. One can minorize |U| and |R| as follows:
|U|
≥
Q∞
j=1 ||zqj| −1|
=
Q∞
j=1 ||q|−k+j+1/2 −1|
≥
Q∞
j=1 |0.6−k+j+1/2 −1|
≥
Q∞
j=1 |0.6−9/2+j −1|
=
η
:=
0.2411047426 . . .
and
|R|
≥
Q∞
j=0 |1 −|qj/z||
=
Q∞
j=0 |1 −|q|k+j−1/2|
≥
Q∞
j=0 |1 −|q|9/2+j|
≥
Q∞
j=0 |1 −0.69/2+j|
=
ξ
:=
0.7715882456 . . . .
Thus using Lemma 5 one obtains the inequality
|QRU| ≥1.2 · η · ξ = 0.2232403024 . . . .
(2)
On the other hand the quantity |G| can be majorized as follows:
|G|
≤
P∞
j=1 |q|j(j−1)/2/|z|j
=
P∞
j=1 |q|j(j−1)/2+(k−1/2)j
≤
P∞
j=1 |q|j(j−1)/2+9j/2
≤
P∞
j=1 0.6j(j−1)/2+9j/2
=
0.1066576686 . . . .
(3)
The lemma follows from inequalities (2) and (3) – for |z| = |q|−k+1/2, one has at the same time
θ = Θ∗−G, |Θ∗| > 0.22 and |G| < 0.11, so θ = 0 is impossible.
Lemma 7. For q ∈D(0.6) and |z| = |q|−7/2, one has θ(q, z) ̸= 0.
Lemma 8. For q ∈D(0.6) and |z| = |q|−3/2, one has θ(q, z) ̸= 0.
Lemma 9. For q ∈D(0.55) and |z| = |q|−5/2, one has θ(q, z) ̸= 0.
3


## Page 4


The last three lemmas are proved in Sections 4, 5 and 6 respectively.
We explain how
Theorem 2 results from them and from Lemma 6. We recall that for |q| ≤0.108, all zeros of
θ(q, .) are simple (see [2]). For any k ∈N ﬁxed and for |q| suﬃciently small, there exists a single
zero of θ(q, .) which is ∼−q−k as q →0, see Proposition 10 in [1]. Hence for |q| suﬃciently small,
this zero satisﬁes the conditions (1). These conditions hold true as q varies along any segment
S belonging to a half-line passing through the origin and such that S ⊂(D(0.55) ∪Dc0). Hence
these conditions hold true for q ∈D(0.55). In the same way one sees that, with the possible
exception of ξ2 and ξ3, the zeros of θ satisfy conditions (1) for q ∈D(0.6).
4
Proof of Lemma 7
For |G| we obtain the majoration
|G| ≤
∞
X
j=1
|q|j(j−1)/2+7j/2 ≤
∞
X
j=1
0.6j(j−1)/2+7j/2 = 0.1851580824 . . . .
We minorize the quantity |Q| using Lemma 5. There remains to minorize |U| and |R|.
We observe that θ(¯q, ¯z) = θ(q, z), therefore when |θ| is majorized, we can assume that
arg(q) ∈[0, π]. Suppose that q ∈D(0.6), arg(q) ∈[3π/4, π]. We deﬁne the sectors Sj in C by
the fomula
Sj := {arg(z) ∈[(j −1)π/4, jπ/4)} ,
j = 1 ,
2 ,
3
,
S4 := {arg(z) ∈[3π/4, π]} ,
and S−j as the symmetric of Sj w.r.t. the real axis. Suppose that ζ ∈S±j. Set ψ := arg(ζ). By
the cosine theorem
|1 −ζ|2 = 1 + |ζ|2 −2|ζ| cos(ψ) .
The function cos(t) being even and decreasing on [0, π] one obtains the minoration
|1 −ζ| ≥µj(|ζ|) := (1 + |ζ|2 −2|ζ| cos((j −1)π/4))1/2 .
(4)
Remarks 10. (1) For ζ ̸= 0, one has µ4(|ζ|) > µ3(|ζ|) > µ2(|ζ|) > µ1(|ζ|).
(2) For j ﬁxed and for |ζ| ≥1, the right-hand side of (4) is an increasing function in |ζ|.
(3) One can prove by straightforward computation that for 1 ≥|ζ1| > |ζ2| and for 3 ≥ℓ>
m ≥1, one has µℓ(|ζ1|) · µm(|ζ2|) > µℓ(|ζ2|) · µm(|ζ1|).
Consider for |z| = |q|−7/2 (i.e. for z = |q|−7/2ω, |ω| = 1), the moduli of three consecutive
factors uk := 1 + zqk of U, for k = k∗, k∗+ 1 and k∗+ 2. (The role of ζ will be played by the
numbers −zqk.) Notice that the numbers uk are of the form
1 + |q|−7/2+kωk
,
|ωk| = 1 .
(5)
Remarks 11. (1) At least one of the three numbers −zqk belongs to the left half-plane, because
arg(q) ∈[π/2, π]. Hence to the corresponding modulus |uk| minoration µ3 is applicable. If at
most one of the other two numbers −zqk belongs to S1∪S−1, then to the corresponding modulus
|uk| minoration µ1, and to the third modulus minoration µ2 are applicable respectively.
(2) Suppose that at least two of the three numbers −zqk belong to S1 ∪S−1. Then these
correspond to k = k∗and k = k∗+ 2, because arg(q) ∈[π/2, π]. Moreover, −zqk∗+1 ∈S4 ∪S−4,
so minoration µ4 is applicable to |uk∗+1| and minoration µ1 to |uk∗| and |uk∗+2|.
4


## Page 5


Consider the three numbers u1, u2, u3. When represented in the form (5), their exponents
−7/2+k are negative, so |−zqk| > 1. For ﬁxed ωk, the modulus |−zqk| decreases as |q| increases.
Hence one can apply part (2) of Remarks 10 and minorize |uk| by its value for |q| = 0.6. Making
use of Remarks 11 one ﬁnds that the product |u1| · |u2| · |u3| is minorized by the least of the 7
numbers µ1(0.6−5/2)·µ4(0.6−3/2)·µ1(0.6−1/2) and µi1(0.6−5/2)·µi2(0.6−3/2)·µi3(0.6−1/2), where
(i1, i2, i3) is a permutation of (1, 2, 3). This is the number
µ3(0.6−5/2) · µ2(0.6−3/2) · µ1(0.6−1/2) = 1.742379963 . . . =: χ0 .
Now consider for j = 1, 2, . . ., a triple |u3j+1|, |u3j+2|, |u3j+3|, j ∈N. Hence | −zqk| < 1 and
by Remarks 10 one has
˜uj := |u3j+1| · |u3j+2| · |u3j+3| ≥min(Aj, Bj)
,
where
Aj := µ3(|q|−5/2+3j) · µ2(|q|−3/2+3j) · µ1(|q|−1/2+3j)
and
Bj := µ1(|q|−5/2+3j) · µ4(|q|−3/2+3j) · µ1(|q|−1/2+3j)
.
Set ρ := |q|. We prove Lemma 7 with the help of the following result (the proof is given at the
end of this section):
Lemma 12. The quantities Aj(ρ) and Bj(ρ) are decreasing in ρ for ρ ∈(0, 0.6].
This means that one can minorize the product ˜uj by χj := min(Aj(0.6), Bj(0.6)). For j = 1,
2, 3 and 4, the values of χj are respectively
0.1749135662 . . . , 0.7772399345 . . . , 0.9492771959 . . . , 0.9889171980 . . .
(in all cases they equal Aj(0.6)). For k ≥16, the factors |uk| can be minorized by |1−|q|−7/2+k|,
and then by |1 −0.6−7/2+k|. We set χ5 := Q∞
k=16 |1 −0.6−7/2+k| = 0.9957913379 . . .. Thus we
minorize |U| by χ0 · χ1 · χ2 · χ3 · χ4 · χ5.
To minorize the product R one can observe that for |z| = |q|−7/2, each number 1 + qj−1/z is
of the form (5) with k ≥7. Therefore when minorizing |R| one can use the same reasoning as
for |U| and obtain a minoration by χ2 · χ3 · χ4 · χ5 (the ﬁrst value of the index k being 7, not 1,
one has to skip the analogs of the minorations of |uk| for k = 1, . . ., 6, i.e. to skip χ0 and χ1).
Set χ∗:= χ2 · χ3 · χ4 · χ5. Thus one can minorize the product |Q| · |U| · |R| by
1.2 · χ0 · χ1 · χ2
∗= 0.1930636291 . . . > 0.1851580824 . . . ≥|G|
from which the lemma follows.
Proof of Lemma 12: One has A2
j = CEF, where
C := 1 + ρ6j+6
,
E := 1 + ρ6j+4 −
√
2ρ3j+2
,
F := 1 + ρ6j+2 −2ρ3j+1 .
For ρ ∈(0, 0.6], each factor C, E and F is positive-valued. Clearly E′ = (3j + 2)ρ3j+1(2ρ3j+2 −
√
2) < 0, because 2ρ ≤1.2 <
√
2. We show that (CF)′ < 0 from which and from Aj > 0 follows
that A′
j < 0. A direct computation shows that
(CF)′
=
ρ3j((6j + 6)ρ3j+5 + (6j + 2)ρ3j+1 + (12j + 8)ρ9j+7
−(6j + 2) −(18j + 14)ρ6j+6) .
5


## Page 6


For j ≥1 and ρ ∈(0, 0.6], the ﬁrst three summands inside the brackets are majorized respectively
by (6j + 6) · 0.68, (6j + 2) · 0.64 and (12j + 8) · 0.616. Their sum is less than 6j + 2, so (CF)′ < 0.
We set B2
j = MNW, where
M := (1 −ρ3j+1)2
,
N := 1 + ρ6j+4 +
√
2ρ3j+2
,
W := (1 −ρ3j+3)2 .
Obviously W ′ < 0. We show that (MN)′ < 0 which together with M > 0, N > 0, W > 0 and
Bj > 0 proves that B′
j < 0. One has (MN)′ = (K1 + K2 −L1) + (K3 + K4 −L2) + (K5 −L3),
where
K1 := (6j + 2)ρ6j+1
,
K2 :=
√
2(3j + 2)ρ3j+1
,
L1 := (6j + 2)ρ3j
,
K3 := (6j + 4)ρ6j+3
,
K4 :=
√
2(9j + 4)ρ9j+3
,
L2 := 2
√
2(6j + 3)ρ6j+2
,
K5 := (12j + 6)ρ12j+5
and
L3 := (18j + 10)ρ9j+4
.
The inequality K5 < L3 is evident. One has K4/L2 ≤(3/4)ρ3j+1 ≤(3/4) · 0.64 = 0.0972 and
K3/L2 ≤(10/9) · (0.6/2
√
2) = 0.2357022603 . . ., so K3 + K4 < L2. Finally, K1/L1 ≤0.63j+1 ≤
0.64 = 0.1296 and K2/L1 ≤
√
2·0.6 = 0.8485281372 . . . hence K1+K2 < L1 and (MN)′ < 0.
5
Proof of Lemma 8
We set θ†(q, z) := θ(q, z/q) = P∞
j=0 qj(j−1)/2zj = 1 + z + qz2 + q3z3 + · · ·.
We show that
θ†(q, z) ̸= 0 for |z| = |q|−1/2 from which the lemma follows. As θ†(¯q, ¯z) = θ†(q, z), we consider
only the case arg(q) ∈[π/2, π]. We assume that |q| ∈[c0, 0.6], because for |q| ≤c0, the zeros of
θ are strongly separated in modulus, see [3]. Set
b0 := 1
,
b1 := z
,
b2 := qz2
and
rk :=
∞
X
j=k
qj(j−1)/2zj .
To show that θ† ̸= 0 we prove that the modulus of the sum of some or all of the terms b0, b1 and
b2 (we denote the set of the chosen terms by S) is larger than the modulus of the sum of the
remaining terms of the series of θ†. We distinguish the following cases according to the intervals
to which arg(z) and arg(q) belong:
Case 1) Re z ≥0, i.e. arg(z) ∈[−π/2, π/2], and arg(q) ∈[π/2, π]. We set S := {b0, b1}.
One has
|r2| ≤
∞
X
j=2
|q|j(j−1)/2−j/2 =: Φ♭(|q|)
,
|r3| ≤
∞
X
j=3
|q|j(j−1)/2−j/2 = Φ♭(|q|) −1
(6)
and
|1 + z| ≥(1 + |z|2)1/2 = (1 + |q|−1)1/2 =: Φ∗(|q|) > Φ♭(|q|) .
The last inequality follows from Φ∗(|q|) and Φ♭(|q|) being respectively decreasing and increasing
on [c0, 0.6] and
Φ∗(0.6) = 1.632993162 . . . > 1.618354488 . . . = Φ♭(0.6) .
6


## Page 7


Case 2) arg(z) ∈[π, 3π/2] and arg(q) ∈[π/2, π]. Then arg(qz) ∈[3π/2, 5π/2], i.e. Re (qz) ≥
0. We set S := {b1, b2}. Hence
|z + qz2| = |z| · |1 + qz| ≥|q|−1/2 · (1 + |q|)1/2 = Φ∗(|q|) .
The other terms of θ† are 1, q3z3, q6z4, . . .. For |z| = |q|−1/2, their moduli equal respectively
1, |q|3/2, |q|4, . . ., which are precisely the terms of the series Φ♭, so as in Case 1) one concludes
that |z + qz2| ≥Φ∗(|q|) > Φ♭(|q|) ≥1 + |r3|.
Case 3) arg(z) ∈[π/2, 3π/4] and arg(q) ∈[π/2, π]. The case is subdivided into ﬁve subcases
in all of which we set S := {b0, b1, b2}.
Case 3A) arg(z) ∈[π/2, 3π/4] and arg(q) ∈[3π/4, π]. Then arg(qz2) ∈[7π/4, 5π/2]. If
arg(qz2) ∈[2π, 5π/2], then
|1 + z + qz2|
≥
Im (1 + z + qz2)
≥
Im (z)
≥
sin(3π/4) · |q|−1/2
≥
(2 · 0.6)−1/2
=
0.9128709292 . . .
>
0.618354488 . . .
=
Φ♭(0.6) −1
≥
|r3| ,
see (6). Set τ(|q|) := (2·|q|)−1/2 −2−1/2 = sin(3π/4)·|q|−1/2 +sin(7π/4) = −cos(3π/4)·|q|−1/2 −
cos(7π/4). If arg(qz2) ∈[7π/4, 2π], then
Im (1 + z + qz2) ≥τ(|q|)
and
Re (1 + z + qz2) ≥1 −τ(|q|)
(one can observe that 1 −τ(|q|) > 0 for q ≥c0). Thus
|1 + z + qz2| ≥(τ 2 + (1 −τ)2)1/2 = ((1 −2τ)2/2 + 1/2)1/2 .
The latter quantity is minimal for τ = 1/2, i.e.
for |q| = 0.3431457506 . . ., when it equals
1/
√
2 = 0.7071067814 . . . > Φ♭(0.6) −1 ≥|r3|.
Case 3B) arg(z) ∈[5π/8, 3π/4] ⊂[π/2, 3π/4] and arg(q) ∈[π/2, 3π/4]. Then arg(qz2) ∈
[7π/4, 9π/4] ⊂[7π/4, 5π/2] and one proves as in Case 3A) that |1 + z + qz2| > |r3|.
Case 3C) arg(z) ∈[π/2, 5π/8] and arg(q) ∈[5π/8, 3π/4]. Then arg(qz2) ∈[13π/8, 2π]. If
|q| ∈[0.3, 0.6], then
|1 + z + qz2|
≥
Re (1 + z + qz2)
≥
1 + |q|−1/2 · cos(5π/8) + cos(13π/8)
≥
1 + 0.3−1/2 · cos(5π/8) + cos(13π/8)
>
0.68 > Φ♭(0.6) −1 ≥|r3| .
If |q| ∈[c0, 0.3], then
1 + |q|−1/2 · cos(5π/8) + cos(13π/8)
≥
1 + c−1/2
0
· cos(5π/8) + cos(13π/8)
≥
0.5433422972 . . .
>
Φ♭(0.3) −1 = 0.1725370862 . . .
≥|r3| .
Case 3D) arg(z) ∈[9π/16, 5π/8] and arg(q) ∈[π/2, 5π/8]. Then arg(qz2) ∈[13π/8, 15π/8].
Just as in Case 3C) one obtains |1 + z + qz2| > |r3|.
Case 3E) arg(z) ∈[π/2, 9π/16] and arg(q) ∈[π/2, 5π/8]. Then arg(qz2) ∈[3π/2, 7π/4] and
7


## Page 8


Re (1 + z + qz2)
≥
1 + |q|−1/2 · cos(9π/16)
≥
1 + c−1/2
0
· cos(9π/16)
>
0.5712
,
Im (1 + z + qz2)
≥
|q|−1/2 · sin(9π/16) −1
≥
0.6−1/2 · sin(9π/16) −1
>
0.2661
,
so |1 + z + qz2| > (0.57122 + 0.26612)1/2 > 0.63 > Φ♭(0.6) −1 ≥|r3|.
Case 4) arg(z) ∈[3π/4, π] and arg(q) ∈[π/2, π]. Then arg(qz2) ∈[2π, 3π], i.e. Im (qz2) ≥0.
We consider four subcases in all of which we set S := {b0, b1, b2}:
Case 4A) arg(z) ∈[3π/4, 5π/6] and arg(q) ∈[π/2, π].
In this case Im (z) ≥0.6−1/2 ·
sin(5π/6) and
|1 + z + qz2| ≥Im (1 + z + qz2) ≥0.6−1/2 · sin(5π/6) = 0.64 . . . > Φ♭(0.6) −1 ≥|r3| .
Case 4B) arg(z) ∈[5π/6, 11π/12] and arg(q) ∈[π/2, π]. Hence arg(qz2) ∈[13π/6, 17π/6]
(with sin(13π/6) = sin(17π/6) = 1/2) and
|1+z+qz2| ≥Im (1+z+qz2) ≥0.6−1/2·sin(11π/12)+sin(13π/6) = 0.83 . . . > Φ♭(0.6)−1 ≥|r3| .
Case 4C) arg(z) ∈[11π/12, π] and arg(q) ∈[π/2, 5π/6] hence arg(qz2) ∈[7π/3, 17π/6]. If
arg(qz2) ∈[7π/3, 5π/2], then
|1 + z + qz2| ≥Im (1 + z + qz2) ≥Im (qz2) ≥sin(7π/3) =
√
3/2 = 0.86 . . . > Φ♭(0.6) −1 ≥|r3| .
If φ := arg(qz2) ∈[5π/2, 17π/6], then
Im (1 + z + qz2)
≥
Im (qz2)
=
sin(φ)
,
|Re (1 + z + qz2)|
≥
|0.6−1/2 · cos(11π/12) + 1 + cos(φ)|
and
|1 + z + qz2|
≥
T(φ)
:=
(sin2(φ) + (0.6−1/2 · cos(11π/12) + 1 + cos(φ))2)1/2
.
The function T(φ) takes only values larger than 1 (hence larger than |r3|) for φ ∈[5π/2, 17π/6].
Case 4D) arg(z) ∈[11π/12, π] and arg(q) ∈[5π/6, π], so arg(qz2) ∈[8π/3, 3π] and
Re (1 + z + qz2) ≤0.6−1/2 · cos(11π/12) + 1 + cos(8π/3) = −0.7470048804 . . . .
Hence |1 + z + qz2| ≥|Re (1 + z + qz2)| > Φ♭(0.6) −1 ≥|r3|.
6
Proof of Lemma 9
We set z := qξ hence |ξ| = |q|−3/2.
Thus θ = P∞
j=0 qj(j−1)/2ξj.
Next we set A := 1 +
P∞
j=4 qj(j−1)/2ξj and B := 1+qξ+q3ξ2, so θ = A+ξB. Finally we set ξ := qζ, thus B = 1+ζ+qζ2
and |ζ| = |q|−1/2.
8


## Page 9


Lemma 13. (1) For |q| ≤0.6 and |ξ| ≤|q|−3/2, one has |A| ≤a0 := 1+P∞
j=4 0.6j(j−1)/2−3j/2 =
2.330487021 . . ..
(2) For |q| ≤0.6, arg(q) ∈[2π/3, π] and |ξ| ≤|q|−3/2, one has |ξB| > a0 ≥|A| hence θ ̸= 0.
(3) For |q| ≤0.55 and |ξ| ≤|q|−3/2, one has |ξB| > a0 ≥|A| hence θ ̸= 0.
Remark 14. For arg(q) ∈[π/2, 2π/3], it is possible to show numerically that |ξB| > a0 ≥|A|
also for |q| ∈[0.55, 0.6]. To this end one can compute the quantities |ξB| and |A| with suﬃciently
small steps in arg(q) and |q|. To obtain a majoration of |A| one can set A := A∗+ A∗∗with
A∗:= 1 + P7
j=4 qj(j−1)/2ξj and A∗∗:= P∞
j=8 qj(j−1)/2ξj. For |ξ| = |q|−3/2 and |q| ≤0.6, one has
|A∗∗| ≤P∞
j=8 0.6j(j−1)/2−3j/2 = 0.0002925303367 . . .. Thus there remains to estimate |ξB| and
|A∗| which contain ﬁnitely-many terms.
Proof of Lemma 13. Part (1) follows from |A| ≤1 + P∞
j=4 |q|j(j−1)/2−3j/2 ≤a0. To prove parts
(2) and (3) we set q := ρeiω, ρ ≥0, ω ∈[π/2, π], and ζ := ρ−1/2eiψ, ψ ∈[0, 2π]. Observe that
|qζ2| = 1. Thus
B
=
1 + ρ−1/2eiψ + ei(2ψ+ω)
and
|B|2
=
(1 + cos(2ψ + ω) + ρ−1/2 cos ψ)2 + (sin(2ψ + ω) + ρ−1/2 sin ψ)2
=
2 + ρ−1 + 2ρ−1/2 cos(ψ + ω) + 2 cos(2ψ + ω) + 2ρ−1/2 cos ψ
=
2 + ρ−1 + 4ρ−1/2 cos(ψ + ω/2) cos(ω/2) + 2 cos(2ψ + ω)
=
ρ−1 + 4ρ−1/2 cos(ψ + ω/2) cos(ω/2) + 4 cos2(ψ + ω/2) .
Set a := cos(ψ + ω/2) ∈[−1, 1] and b := cos(ω/2) ∈[0,
√
2/2] (because ω/2 ∈[π/4, π/2]). The
polynomial 4a2 + 4ρ−1/2ab + ρ−1 (considered as a polynomial in a with b as a parameter) takes
its minimal value for a = −ρ−1/2b/2. This value is (1 −b2)ρ−1. Therefore for b ≤1/2 (hence for
ω ∈[2π/3, π]), one has |B|2 ≥3 · ρ−1/4 ≥3 · 0.6−1/4. So for |ξ| = |q|−3/2 ≥0.6−3/2, one has
|ξB| = |q|−3/2 · |B| ≥0.6−3/2 · (3 · 0.6−1/4)1/2 = 2.405626123 . . . > a0 ≥|A| .
For ρ = |q| ≤0.55, one has |B|2 ≥ρ−1/2 and |ξB| ≥0.55−2/
√
2 = 2.337543079 . . . > a0 ≥
|A|.
References
[1] V.P. Kostov, On the zeros of a partial theta function, Bull. Sci. Math. 137:8 (2013), 1018-
1030.
[2] V.P. Kostov, On the spectrum of a partial theta function, Proc. Royal Soc. Edinb. A 144:5
(2014), 925-933.
[3] V.P. Kostov, A separation in modulus property of the zeros of a partial theta function,
Analysis Mathematica 44 (2018), no. 4, 501-519. arXiv:1704.01901.
[4] V.P. Kostov, B. Shapiro, Hardy-Petrovitch-Hutchinson’s problem and partial theta func-
tion, Duke Math. J. 162:5 (2013), 825-861. arXiv:1106.6262v1[math.CA].
9

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
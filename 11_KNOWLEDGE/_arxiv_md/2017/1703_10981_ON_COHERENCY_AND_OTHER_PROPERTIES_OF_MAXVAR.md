---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1703.10981
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1703.10981_On_coherency_and_other_properties_of_MAXVAR

> Source: 1703.10981_On_coherency_and_other_properties_of_MAXVAR.pdf

> Pages: 10

---


## Page 1


arXiv:1703.10981v2  [q-fin.MF]  6 Sep 2017
On coherency and other properties of
MAXVAR ∗
Jie Sun† and Qiang Yao‡
August 27, 2018
Abstract
This paper is concerned with the MAXVAR risk measure on L 2 space. We present
an elementary and direct proof of its coherency and averseness. Based on the obser-
vation that the MAXVAR measure is a continuous convex combination of the CVaR
measure, we provide an explicit formula for the risk envelope of MAXVAR.
2010 MR subject classiﬁcation: 49N15, 91G40
Key words: coherent risk measure, risk averse, risk envelope.
1
Introduction
In Cherny and Madan [2] and Cherny and Orlov [3], a new kind of risk measure –“MAXVAR”
– is proposed, which is useful in the analysis of large portfolios. Given a probability space
(Ω, Σ, P0) and a random variable X ∈L 2(Ω, Σ, P0), where L 2(Ω, Σ, P0) is the square inte-
grable Lebesgue space (L 2 for short), the MAXVAR is deﬁned as
MAXVARn(X) := E(max{X1, · · · , Xn}),
where X1, · · · , Xn are i.i.d. copies of X. We call MAXVARn(·) the “MAXVAR risk mea-
sure”.
∗This paper is dedicated to Michel Th´era in celebration of his 70th birthday.
†School of Mathematical Sciences, Chongqing Normal University, PRC and School of Science and CIC,
Curtin University, Australia. Email: jie.sun@curtin.edu.au.
‡School of Statistics, East China Normal University, PRC and NYU—ECNU Institute of Mathematical
Sciences at NYU Shanghai, China. E-mail: qyao@sfs.ecnu.edu.cn.
1


## Page 2


Note that MAXVARn(·) is always ﬁnite on L 2 since |MAXVARn(X)| ≤nE(|X|) < +∞
for any X ∈L 2.
In [2, 3], the name of “MINVAR risk measure” was used. Since we treat risk measures
as a nondecreasing function, we use “MAXVAR risk measure” instead. Obviously, we have
MAXVARn(X) = −MINVARn(−X).
Diﬀerent from papers [2, 3], which considered co-
herency of MINVAR in L ∞space, this paper deals with the L 2 space. Our proof of the
coherency of MAXVAR risk measure is direct and independent of [2, 3]. Moreover, we show
risk averseness of MAXVAR and give an explicit formula for its risk envelope.
In Section 2, we present a simple proof for the coherency of MAXVAR. We show its
aversity in Section 3. Section 4 is devoted to the discussion of a continuous representation
of MAXVAR and Section 5 provides an explicit formula for its risk envelope.
2
Coherency of MAXVAR
In this section, we show that MAXVAR is a coherent risk measure in basic sense of Rock-
afellar.
Deﬁnition 1 (Rockafellar [5]) A functional R : L 2 →(−∞, +∞] is a coherent risk mea-
sure in basic sense if it satisﬁes
(A1) R(C) = C for all constant C;
(A2) (“convexity”) R(λX + (1 −λ)Y ) ≤λ · R(X) + (1 −λ) · R(Y ) for any X, Y ∈L 2 and
any ﬁxed 0 ≤λ ≤1;
(A3) (“monotonicity”) R(X) ≤R(Y ) for any X, Y ∈L 2 satisfying X ≤Y ;
(A4) (“closedness”) If ∥Xk −X∥2 →0 and R(Xk) ≤0 for all k ∈N, then R(X) ≤0;
(A5) (“positive homogeneity”) R(λX) = λR(X) for any λ > 0 and X ∈L 2.
Theorem 1 MAXVARn(·) is a coherent risk measure in basic sense.
Proof. (A1) is obvious by deﬁnition. (A5) is also easy to check since if X1, · · · , Xn are
i.i.d. copies of X and λ > 0, then λX1, · · · , λXn are i.i.d. copies of λX.
2


## Page 3


Proof of (A2). We only need to show the following subadditive property of MAXVAR
MAXVARn(X + Y ) ≤MAXVARn(X) + MAXVARn(Y )
∀X, Y.
(1)
Then (1) and (A5) imply (A2).
For any X, Y
∈L 2, take (X1, Y1), · · · , (Xn, Yn) as
i.i.d. copies of the two dimensional random vector (X, Y ). That is, the random vectors
(X1, Y1), · · · , (Xn, Yn) are independent and have the same joint distribution as the random
vector (X, Y ). Then X1, · · · , Xn are i.i.d. copies of X and Y1, · · · , Yn are i.i.d. copies of Y .
We next show that X1 + Y1, · · · , Xn + Yn are i.i.d. copies of X + Y .
Since (Xi, Yi) has the same joint distribution as (X, Y ), i = 1, ..., n, it follows that
Xi + Yi has the same distribution as X + Y . In order to prove that X1 + Y1, · · · , Xn + Yn
are independent, we only need to prove that for any t1, · · · , tn ∈R,
P0 (X1 + Y1 ≤t1, · · · , Xn + Yn ≤tn)
=P0 (X1 + Y1 ≤t1) · · · · · P0 (Xn + Yn ≤tn) .
(2)
In fact, since the random vectors (X1, Y1), · · · , (Xn, Yn) are independent, we have
P0((X1, Y1) ∈B1, · · · , (Xn, Yn) ∈Bn)
=P0((X1, Y1) ∈B1) · · · · · P0((Xn, Yn) ∈Bn)
(3)
for any Borel sets B1, · · · , Bn ⊆R2. In particular, if we take
Bi =

(x, y) ∈R2 : x + y ≤ti
	
for any 1 ≤i ≤n in (3), we can get (2). Therefore, X1 + Y1, · · · , Xn + Yn are independent.
Moreover, they are i.i.d. copies of X + Y .
Since the deﬁnition of MAXVAR does not depend on the choice of the i.i.d. copies, we
have
MAXVARn(X) = E(max{X1, · · · , Xn}),
MAXVARn(Y ) = E(max{Y1, · · · , Yn}),
MAXVARn(X + Y ) = E(max{X1 + Y1, · · · , Xn + Yn}).
Furthermore, since
max{X1 + Y1, · · · , Xn + Yn} ≤max{X1, · · · , Xn} + max{Y1, · · · , Yn},
we get
MAXVARn(X + Y ) = E(max{X1 + Y1, · · · , Xn + Yn})
3


## Page 4


≤E(max{X1, · · · , Xn}) + E(max{Y1, · · · , Yn})
= MAXVARn(X) + MAXVARn(Y ).
Proof of (A3). For any X, Y ∈L 2 satisfying X ≤Y , suppose X1, · · · , Xn are i.i.d. copies
of X and Y1, · · · , Yn are i.i.d. copies of Y . We can see that P0(X ≤t) ≥P0(Y ≤t) for any
t ∈R since X ≤Y . Then we have
MAXVARn(X)
=
Z 0
−∞
[P0(max{X1, · · · , Xn} > t) −1] dt +
Z +∞
0
P0(max{X1, · · · , Xn} > t)dt
= −
Z 0
−∞
(P0(X ≤t))ndt +
Z +∞
0
[1 −(P0(X ≤t))n] dt
≤−
Z 0
−∞
(P0(Y ≤t))ndt +
Z +∞
0
[1 −(P0(Y ≤t))n] dt
=
Z 0
−∞
[P0(max{Y1, · · · , Yn} > t) −1] dt +
Z +∞
0
P0(max{Y1, · · · , Yn} > t)dt
= MAXVARn(Y ).
The detail of the ﬁrst equality is as follows. Denote by
F(t) = P0(max{X1, · · · , Xn} ≤t)
the cumulative distribution function of max{X1, · · · , Xn}. Then
E(max{X1, · · · , Xn})
=
Z +∞
−∞
xdF(x)
=
−
Z 0
−∞
Z 0
x
dt

dF(x) +
Z +∞
0
Z x
0
dt

dF(x)
(by Fubini’s Theorem)
=
−
Z 0
−∞
Z t
−∞
dF(x)

dt +
Z +∞
0
Z +∞
t
dF(x)

dt
=
−
Z 0
−∞
F(t)dt +
Z +∞
0
[1 −F(t)]dt.
(4)
And the second equality comes from the fact that F(t) = (P0(X ≤t))n.
Proof of (A4).
Suppose Xk (k = 1, 2, · · ·), X ∈L 2 and ∥Xk −X∥2 →0 as k tends
to inﬁnity. Then Xk →X in distribution. Denote by Fk(t) the distribution function of
Xk (k = 1, 2, · · ·) and by F(t) the distribution of X.
Then lim
k→∞Fk(t) = F(t) for all
continuous points of F(·). It implies that lim
k→∞[Fk(t)]n = [F(t)]n for all continuous points of
[F(·)]n. Note that [Fk(t)]n is the distribution function of max{Xk
1, · · · , Xk
n} and [F(t)]n is
4


## Page 5


the distribution function of max{X1, · · · , Xn}, where Xk
1 , · · · , Xk
n are i.i.d. copies of Xk (k =
1, 2, · · ·) and X1, · · · , Xn are i.i.d. copies of X. Therefore, we have max{Xk
1, · · · , Xk
n} →
max{X1, · · · , Xn} in distribution, and
MAXVARn(Xk)
=
E(max{Xk
1, · · · , Xk
n})
→
E(max{X1, · · · , Xn}) = MAXVARn(X)
as k tends to inﬁnity. Thus, if MAXVARn(Xk) ≤0 for all k = 1, 2, · · · then MAXVARn(X) ≤
0. The proof of the theorem is completed.
✷
3
Risk-averseness of MAXVAR
Suppose R is a functional from L 2 to (−∞, +∞]. Recall that an averse risk measure is
deﬁned by axioms (A1), (A2), (A4), (A5) and
(A6) R(X) > E(X) for all non-constant X.
We then have the next theorem.
Theorem 2 If n ≥2, then MAXVARn(·) is averse.
F¨ollmer and Schied [4] proved that if R is a coherent, law-invariant risk measure in
L ∞(not L 2) other than E(·), then R is averse, where “law-invariant” stands for that
R(X) = R(Y ) whenever X and Y have the same distribution under P0. Since we are now
considering the L 2 case, we cannot use the result in F¨ollmer and Schied [4] directly. We
next give a separate proof.
Proof of Theorem 2 On one hand, for any X ∈L 2, let X1, · · · , Xn be i.i.d. copies of X.
Then we have
MAXVARn(X) = E(max{X1, · · · , Xn}) ≥E(X1) = E(X).
On the other hand, if MAXVARn(X) = E(X) = E(X1) (n ≥2), then
max{X1, · · · , Xn} = X1 almost surely. Similarly, max{X1, · · · , Xn} = X2 almost surely.
Therefore, X1 = X2 almost surely. Since X1 and X2 are independent, we must have X1
equals to a constant almost surely, which is equivalent to say X equals to a constant al-
most surely.
Therefore, MAXVARn(X) > E(X) for nonconstant X, which implies that
5


## Page 6


MAXVARn(·) is averse when n ≥2.
Remark. In fact, Theorems 1 and 2 can be obtained as corollaries of Theorem 3 in the next
section. See the remark after the proof of Theorem 3 for details. However, we think it is of
interest to provide an elementary proof only based on deﬁnition of MAXVAR.
4
MAXVAR as a continuous convex combination of
CVaR
An important coherent risk measure in basic sense is the conditional value at risk (CVaR)
popularized by Rockafellar and Uryasev [6]. Among several equivalent deﬁnitions of CVaR,
the most familiar one is probably the following.
CVaRα(X) = min
β∈R

β +
1
1 −αE(X −β)+

,
(5)
where (t)+ = max(t, 0) and α ∈[0, 1). The minimum is attained at β∗= VaRα(X), and the
VaR ( “Value-at-Risk”) is deﬁned as
VaRα(X) := inf {ν ∈R : P0(X > ν) < 1 −α} .
(6)
In this section, we show that MAXVARn(·) is certain “continuous convex combination”
of the CVaR measure in the sense that
MAXVARn(·) =
Z 1
0
CVaRα(·)wn(α)dα,
where wn(α) (α ∈[0, 1]) is the “weight function” which satisﬁes wn(α) ≥0 on [0, 1] and
R 1
0 wn(α)dα = 1. Speciﬁcally, we have the next theorem.
Theorem 3 For any X ∈L 2, we have
MAXVARn(X) =
Z 1
0
CVaRα(X)wn(α)dα,
where
wn(α) := n(n −1)(1 −α)αn−2,
α ∈[0, 1]
is the weight function.
Remark. It can be easily checked that wn(α) ≥0 on [0, 1], and
Z 1
0
wn(α)dα = n(n −1)
Z 1
0
(αn−2 −αn−1)dα = n(n −1)

1
n −1 −1
n

= 1.
6


## Page 7


Therefore, wn(α) is indeed a weight function.
Theorem 3 was mentioned in Cherny and Orlov [3] without details.
We now give a
detailed proof by using the so called “Choquet integral”. First, we need a lemma. For any
α ∈[0, 1), deﬁne fα(·) : Σ →[0, 1] in the following way,
fα(A) : =



1
1−αP0(A)
if P0(A) ≤1 −α,
1
otherwise.
= gα[P0(A)],
where
gα(x) :=



1
1−αx
if x ∈[0, 1 −α),
1
if x ∈[1 −α, 1].
(7)
We then have the following lemma, which implies that the CVaR measure can be written
as the “Choquet integral” with respect to fα(·).
Lemma 1 For any X ∈L 2 and α ∈[0, 1), we have
CVaRα(X) =
Z 0
−∞
[fα(X > t) −1]dt +
Z +∞
0
fα(X > t)dt.
Proof. If VaRα(X) ≤0, then
Z 0
−∞
[fα(X > t) −1]dt +
Z +∞
0
fα(X > t)dt
=
Z 0
VaRα(X)

1
1 −αP0(X > t) −1

dt +
Z +∞
0
1
1 −αP0(X > t)dt
=VaRα(X) +
1
1 −α ·
Z +∞
VaRα(X)
P0(X > t)dt
=VaRα(X) +
1
1 −α · E[(X −VaRα(X))+] = CVaRα(X).
The last step above is due to (5) and (6).
If VaRα(X) > 0, then
Z 0
−∞
[fα(X > t) −1]dt +
Z +∞
0
fα(X > t)dt
=
Z VaRα(X)
0
dt +
Z +∞
VaRα(X)
1
1 −αP0(X > t)dt
=VaRα(X) +
1
1 −α ·
Z +∞
VaRα(X)
P0(X > t)dt
7


## Page 8


=VaRα(X) +
1
1 −α · E[(X −VaRα(X))+] = CVaRα(X),
which completes the proof.
✷
Proof of Theorem 3
Deﬁne
h(x) := 1 −(1 −x)n,
x ∈[0, 1].
It is not diﬃcult to check that
h(x) =
Z 1
0
gα(x)wn(α)dα,
x ∈[0, 1],
(8)
where gα(x) is as deﬁned in (7). By (4), for any X ∈L 2 we have
MAXVARn(X) =
Z 0
−∞
[h(P0(X > t)) −1]dt +
Z +∞
0
h(P0(X > t))dt.
(9)
So by (8), (9) and Lemma 1, together with Fubini’s theorem and the fact that
R 1
0 wn(α)dα =
1, we get
MAXVARn(X) =
Z 0
−∞
Z 1
0
[fα(X > t) −1]wn(α)dαdt +
Z +∞
0
Z 1
0
fα(X > t)wn(α)dαdt
=
Z 1
0
Z 0
−∞
[fα(X > t) −1]dt +
Z +∞
0
fα(X > t)dt

wn(α)dα
=
Z 1
0
CVaRα(X)wn(α)dα
for any X ∈L 2, as desired.
Remark. Theorem 3 says that MAXVARn(·) is a continuous convex combination of the
CVaR measure, its coherency in basic sense follows from Proposition 2.1 of Ang et al [1],
and its averseness follows from the averseness of the CVaR (Proposition 4.4 of Ang et al [1])
together with the basic property of integral. Therefore, Theorem 3 can actually provide an
alternative proof of the coherency and averseness of MAXVARn(·).
5
The risk envelope of MAXVAR
Since
MAXVARn(·) =
Z 1
0
CVaRα(·)wn(α)dα
8


## Page 9


is a coherent risk measure on L 2, by the dual representation theorem (Rockafellar [5]),
there exists a unique, nonempty, convex and closed set Qn ⊆L 2, called “the risk envelope
of MAXVARn(·)” such that
MAXVARn(X) = sup
Q∈Qn
E(XQ)
for any X ∈L 2.
In this section we aim at characterizing the risk envelope of MAXVARn(·)”. First recall
the following well-known result for the discrete convex combination of the CVaR measure,
which can be found in Rockafellar [5] and whose proof can be found in Ang et al [1].
Proposition 1 Let R(·) =
nP
i=1
λiCVaRαi(·) with positive weights λi adding up to 1. Then
R is a coherent risk measure in the basic sense and its risk envelope is
( n
X
i=1
λiQi : 0 ≤Qi ≤
1
1 −αi
, E(Qi) = 1, ∀i = 1, 2, · · · , n
)
.
A continuous version of Proposition 1 gives the risk envelope of MAXVAR as follows.
Theorem 4 The risk envelope of MAXVAR is
Qn := cl
Z 1
0
Qαwn(α)dα, 0 ≤Qα ≤
1
1 −α, E(Qα) = 1, ∀α ∈[0, 1)

,
(10)
where
wn(α) := n(n −1)(1 −α)αn−2
α ∈[0, 1]
is the weight function (00 is deﬁned to be 1), and “cl” stands for the closure in L 2.
Proof. Note that the integration “
R 1
0 Qαwn(α)dα” in (10) is deﬁned pointwise. That is,
Y =
R 1
0 Qαwn(α)dα means Y (ω) =
R 1
0 Qα(ω)wn(α)dα for any ω ∈Ω. Since 0 ≤Qα ≤
1
1 −α
for any α ∈[0, 1), we have
0 ≤
Z 1
0
Qα(ω)wn(α)dα ≤
Z 1
0
n(n −1)αn−2dα = n
for any ω ∈Ω. Therefore, Qn ⊆L ∞⊆L 2. In addition, we can check that
MAXVARn(X) =
Z 1
0
CVaRα(X)wn(α)dα
= sup

E

X
Z 1
0
Qαwn(α)dα

:
Z 1
0
Qαwn(α)dα ∈Qn

(11)
9


## Page 10


for any X ∈L 2. Furthermore, it is easy to check the convexity of Qn. Since Qn is closed in
L 2, it follows from the dual representation theorem that Formula (11) implies that (10) is
the risk envelope of MAXVARn(·).
✷
Acknowledgment. We would like to thank the anonymous referees for their useful sug-
gestions, which are of great help for improving the manuscript. The research of Jie Sun
is partially supported by Australian Research Council under Grant DP160102819. The re-
search of Qiang Yao is partially supported by grants from National Science Foundation of
China (No.11201150 and No.11126236) and the 111 Project (No.B14019).
References
[1] M. Ang, J. Sun and Q. Yao (2017) On the dual representation of coherent risk measures,
Ann. Oper. Res. to appear. DOI: 10.1007/s10479-017-2441-3.
[2] A. Cherny and D. Madan (2009) New measures for performance evaluation, Rev. Finan.
Stud. 22, 2571-2606.
[3] A. Cherny and D. Orlov (2011) On two approaches to coherent risk contribution, Math.
Finance 23, 557-571.
[4] H. F¨ollmer and A. Schied (2004).Stochastic Finance (2nd Edition). Walter de Gruyter,
Berlin, Germany.
[5] R. T. Rockafellar (2007) Coherent approaches to risk in optimization under uncertainty,
Tutorials in Operations Research, INFORMS, 38-61.
[6] R.T. Rockafellar and S. Uryasev (2000). Optimization of conditional value-at-risk. Jour-
nal of Risk, 2(3), 21-42.
10

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
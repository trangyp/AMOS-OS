---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.09306v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1905.09306v1_Absolutely_continuous_copulas_with_prescribed_support_constructed_by_differentia

> Source: 1905.09306v1_Absolutely_continuous_copulas_with_prescribed_support_constructed_by_differentia.pdf

> Pages: 27

---


## Page 1


Absolutely continuous copulas with prescribed
support constructed by diﬀerential equations,
with an application in toxicology
Oscar Bj¨ornham
FOI CBRN Defence and Security
oscar.bjornham@foi.se
Niklas Br¨annstr¨om
FOI CBRN Defence and Security
niklas.brannstrom@foi.se
Leif Persson
Mathematics Department, Ume˚a University
leif.persson@umu.se
May 24, 2019
Abstract
A new method for constructing absolutely continuous two–dimensional
copulas by diﬀerential equations is presented. The copulas are symmet-
ric with respect to reﬂection in the opposite diagonal. The support of
the copula density may be prescribed to arbitrary opposite symmetric hy-
pographs of invertible functions, containing the diagonal. The method is
applied to toxicological probit modeling, where new compatibility condi-
tions for the probit parameters are derived.
1
Introduction and main results
This paper is motivated by the following result, which is probably well known,
although we have not been able to ﬁnd any explicit statement or proof:
Proposition 1.1. Suppose that a, ∆∈R, a > 0. Then there exists random
variables X, Y satisfying
Y ≤aX + ∆and X, Y standard normal
(1)
if and only if a = 1 and ∆≥0, and then if ∆> 0, there exists X, Y with
absolutely continuous joint distribution satisfying (1).
1
arXiv:1905.09306v1  [math.PR]  22 May 2019


## Page 2


A proof is given at the end of this section. Our interests in this result comes
from applications in toxicological probit modeling, accounted for in Section 7
where we prove new compatibility conditions for toxicological probit models. For
simulation purposes, we are also interested in constructing absolute continuous
distributions of Proposition 1.1:
Problem 1.2. Given a number ∆> 0, construct a pair of standard normal
random variables X, Y with absolutely continuous joint distribution supported
on y ≤x + ∆.
This seems to be a very simple and basic problem in probability theory,
but to our surprise we could not ﬁnd any simple constructions in the literature.
Independent standard normal X, Y have absolutely continuous joint distribution
but do not fullﬁll the support condition, and truncating to y ≤x+∆yields non–
normal marginals. It is easy to construct singular solutions to the problem, the
simplest being X = Y . The diﬃculty lies in imposing the absolute continuity.
We reduce Problem 1.2 to a problem of the dependence structure, or copula of
(X, Y ). Before we state our main result, let us brieﬂy review the main facts
about copulas.
A function C : [0, 1]2 →[0, 1] is said to be a copula if C(u, 0) = C(0, v) = 0,
C(u, 1) = u, C(1, v) = v and C(u2, v2) −C(u2, v1) −C(u1, v2) + C(u1, v1) ≥0
for all u, v, u1, v1, u1, v2 ∈[0, 1] such that u1 ≤u2, v1 ≤v2, cf. [18, Deﬁnition
2.2.2]. By Sklar’s theorem ([18, Theorem 2.3.3]), the cumulative distribution
function (CDF) FX,Y of any bivariate random variable (X, Y ) is representable
by the marginal CDF’s FX, FY and a copula C as
FX,Y (x, y) = C(FX(x), FY (y)).
(2)
This may be regarded as a change of variables X = F −1
X (U), Y = F −1
Y (V )
such that (U, V ) has uniform marginals.
The copula C is uniquely deﬁned
on Range(FX)×Range(FY ) for all bivariate random variables (X, Y ), and if
FX, FY are continuous, C is uniquely deﬁned on [0, 1]2. Morover, the partial
derivatives C′
u, C′
v, C′′
uv of a copula C(u, v) are deﬁned almost everywhere on
[0, 1]2 ([18, Theorem 2.2.7]) and C′′
uv ≥0. If
RR
C′′
uvdudv = 1, C is said to be
absolutely continuous. Copulas are common in statistical modeling, in particular
mathematical ﬁnance. The main beneﬁt of copulas is that by Sklar’s theorem,
the marginal statistics and dependence structure can be modeled separately.
For an introduction to copulas we refer to [18], for a recent review see [9].
Returning to Problem 1.2, the half–plane {(x, y) : y ≤x + ∆} is symmetric
with respect to reﬂection (x, y) 7→(−y, −x) through the line x + y = 0. There-
fore, we assume that (X, Y ) and (−Y, −X) are equal in distribution. Moreover,
X, −X, Y, −Y are all identically distributed so it follows (from Theorem 2.4 be-
low) that the copula C(u, v) of (X, Y ) is opposite symmetric, according to the
following deﬁnition.
Deﬁnition 1.3. A copula C is said to be opposite symmetric if
C(u, v) = C(1 −v, 1 −u) + u + v −1
(3)
2


## Page 3


for all (u, v) ∈[0, 1]2.
Opposite symmetry means symmetry with respect to reﬂection (u, v) 7→
(1 −v, 1 −u) in the opposite diagonal u + v = 1, and was introduced in [5].
Applying the copula transformation, using the standard normal CDF Φ:
u = Φ(x), v = Φ(y), FX,Y (x, y) = C(u, v),
(4)
Problem 1.2 reduces to ﬁnding an absolutely continuous opposite symmetric
copula C(u, v) with density supported on {(u, v) ∈[0, 1]2 : v ≤H(u)} where
H(u) = Φ(Φ−1(u) + ∆).
(5)
Our main result is the construction of C(u, v) in the following Theorem 1.4. We
want to emphasize its simplicity, involving H and its inverse explicitly. The cru-
cial part is the evaluation of the integral in (10), which is suitable for numerical
integration if not analytically integrable.
Theorem 1.4. Assume that H : [0, 1] →[0, 1] is a bijective function such that
H(u) + H−1(1 −u) = 1 and H(u) ≥u,
u ∈[0, 1],
(6)
u0 ∈(0, 1/2) and H(u0) = 1 −u0,
(7)
Z u
u0
dz
H(z) −z < ∞,
u ∈[u0, 1)
(8)
and
lim
u↗1
Z u
u0
dz
H(z) −z = ∞.
(9)
Let
G(v) = exp

−
Z 1−v
u0
dz
H(z) −z

,
v ∈[0, 1 −u0],
(10)
K(u) = H(u) −u
G(1 −u) −1 + 2u0,
u ∈[u0, 1]
(11)
and
F(u) = (1 −2u0)(1 −G(1 −u)),
u ∈[u0, 1].
(12)
Deﬁne C(u, v) by
1. If 0 < u ≤u0 and 0 ≤v ≤H(u), then
C(u, v) = H−1(v) + (K(1 −v) −K(1 −H(u)))G(v).
(13)
2. If 0 < u ≤u0 and H(u) < v ≤1 −u then
C(u, v) = u
(14)
3


## Page 4


3. If u0 < u < 1 and 0 ≤v ≤1 −u then
C(u, v) = H−1(v) + (K(1 −v) + F(u))G(v).
(15)
4. If 0 < u < 1 and u + v > 1 then C(u, v) is deﬁned by (3).
Then C(u, v) is an absolutely continuous opposite symmetric copula with prob-
ability density supported on v ≤H(u).
Note that the hypograph v ≤H(u) is opposite symmetric if and only if
(6) holds true. The copula is piecewisely deﬁned, on parts of the unit square
depicted in Figure 1.
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
Figure 1: Parts of the unit square for piecewise deﬁnition of the copula in
Theorem 1.4.
Theorem 1.4 is proved at then end of Section 5. Before that, we develop a
theory for construction of opposite symmetric copulas by diﬀerential equations
in Section 3 and Section 5, which we believe is of interest in its own right,
and gives in fact a much larger class of copulas than Theorem 1.4. In section
4 we compare our method to two other methods in the literature, Durantes
and Jaworskis construction of absolutely continuous copulas with given diagonal
section [6], and Jaworskis characterization of copulas using diﬀerential equations
[14]. In Section 6 we adapt our diﬀerential equation method to sampling from
the copula. We conclude the paper with section 7, an application in toxicological
probit modeling, where new compatibility conditions for the probit coeﬃcients
are derived.
4


## Page 5


Example 1.5. In this example we construct a solution to Problem 1.2 using
Theorem 1.4. Let Φ be the standard normal CDF, φ(x) = Φ′(x) the standard
normal probability density function (PDF), ∆> 0 and H given by (5). Then
H−1(v) = Φ(Φ−1(v) −∆) and because of the symmetries Φ(x) + Φ(−x) = 1,
Φ−1(u) + Φ−1(1 −u) = 0, condition (6) is satisﬁed, and
u0 = Φ(−∆/2).
(16)
Moreover, with the change of variables z = Φ(w) and the mean value theorem
we obtain
Z u
u0
dz
H(z) −z =
Z Φ−1(u)
−∆/2
φ(w)dw
Φ(w + ∆) −Φ(w)
=
Z Φ−1(u)
−∆/2
φ(w)dw
φ(w + θ(w)∆) =
1
√
2π
Z Φ−1(u)
−∆/2
exp

w∆θ(w) −∆2θ(w)2
2

dw
(17)
for some function θ(w) with 0 ≤θ(w) ≤1, so
1
√
2π∆

e∆Φ−1(u) −e∆2/2
≥
Z u
u0
dz
H(z) −z ≥e−∆2/2
√
2π

Φ−1(u) + ∆
2

(18)
which proves that conditions (8) and (9) are satisﬁed. The function G deﬁned
by equation (10) can not be expressed in terms of special functions (to our
knowledge), but can be determined by numerical integration, and C(u, v) is
then determined by equations (3) and (13)-(15). The density of C is illustrated
in ﬁgure 1.5. The joint PDF of (X, Y ) is given by
p(x, y) = C′′
uv(Φ(x), Φ(y))φ(x)φ(y)
(19)
and is illustrated in ﬁgure 1.5. Here, G(v) is computed with the MATLAB R
⃝
function integral
at 400 uniformly distributed grid points on [ϵ, 1 −u0], and
computed at intermediate points on [ϵ, 1 −u0] by spline interpolation, where
ϵ = 10−11. Consequently, the copula and its density is computed on [ϵ, 1 −ϵ]2.
5


## Page 6


0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
0
0.5
1
1.5
2
Figure 2: Copula density C′′
uv(u, v) for Example 1.5, ∆= 1. The density is
discontinuous on the curve v = H(u) and tends to inﬁnity when approaching
(0, 0) or (1, 1).
-2
0
2
-3
-2
-1
0
1
2
0
0.05
0.1
0.15
0.2
Figure 3: Probability density function p(x, y) for Example 1.5, ∆= 1. The
wiggles in the level curves at the upper right and lower left corners of right plot
are numerical artifacts.
Proof of Proposition 1.1. If (1) is satisﬁed then Φ((y −∆)/a) = P{aX + ∆≤
y} ≤P{Y ≤y} = Φ(y) for all y ∈R, which is possible only if a = 1 and ∆≥0.
For ∆≥0 we can take X = Y , which gives a singular distribution supported
on x = y. If ∆> 0, Example 1.5 shows that X, Y with absolutely continuous
joint distribution exists.
2
Symmetries and copulas
Several notions of bivariate symmetries are considered in [17]. A pair of random
variables(X, Y ) are said to be exchangeable if (X, Y ) and (Y, X) are equal in
distribution, and (X, Y ) is exchangeable if and only if its copula C(u, v) is a
symmetric function, i.e., C(u, v) = C(v, u).
Moreover, (X, Y ) is said to be
6


## Page 7


radially symmetric about (a, b) ∈R2 if (X −a, Y −b) and (a −X, b −Y ) are
equal in distribution, or equivalently,
FX,Y (a + x, b + y) = 1 −FX(a −x) −FY (b −y) + FX,Y (a −x, b −y)
(20)
Also, (X, Y ) is said to be marginally symmetric about (a, b) ∈R2 if
FX(a + x) = 1 −FX(a −x) and FY (b + y) = 1 −FY (b −y).
(21)
The following theorem is proved in [17, Theorem 3.2]:
Theorem 2.1. Suppose (X, Y ) is marginally symmetric about (a, b) with copula
C. Then (X, Y ) is radially symmetric about (a, b) if and only if C satisﬁes the
functional equation
C(u, v) = C(1 −u, 1 −v) + u + v −1
(22)
There is a corresponding class of bivariate random variables associated to
opposite symmetric copulas, which we propose to call opposite radially symmet-
ric variables, in accordance with the terminology in [5], and analogous to the
radially symmetric variables of [17].
Deﬁnition 2.2. The bivariate random variable (X, Y ) is said to be opposite
radially symmetric about (a, b) ∈R2 if (a + X, b + Y ) and (b −Y, a −X) are
equal in distribution, or, equivalently,
FX,Y (a + x, b + y) = 1 −FX(a −y) −FY (b −x) + FX,Y (a −y, b −x).
(23)
We need to replace marginal symmetry with the following analog of (20):
Deﬁnition 2.3. The bivariate random variable (X, Y ) is said to be opposite
marginally symmetric about (a, b) ∈R2 if FX, FY satisfy
FX(a + x) = 1 −FY (b −x) and FY (b + y) = 1 −FX(a −y)
(24)
for all x, y.
Remark. If X, Y are identically distributed and marginally symmetric about
(a, a) ∈R2, then (X, Y ) is opposite marginally symmetric about (a, a). There
are no identically distributed opposite marginally symmetric (X, Y ) about (a, b)
if b ̸= a, since then the common CDF FX = FY = F would satisfy F(x) =
F(x + b −a) for all x.
We have the following analog of Theorem 2.1:
Theorem 2.4. Suppose that (X, Y ) is opposite marginally symmetric about
(a, b) ∈R2 with copula C, and suppose that FX, FY are continuous.
Then
(X, Y ) is opposite radially symmetric about (a, b) if and only if C is opposite
symmetric.
7


## Page 8


Proof. It follows from equations (23) and (24) that (X, Y ) is opposite radially
symmetric if and only if
C(1 −FY (b −x), 1 −FX(a −y)) = C(FX(a + x), FY (b + y))
= 1 −FX(a −y) −FY (b −x) + C(FX(a −y), FY (b −x)).
(25)
Since the range of FX and FY is [0, 1] this proves the theorem.
Remark. There is an erroneous statement in [5, Remark 1] that if C is opposite
symmetric, then (X, Y ) and (1 −Y, 1 −X) are equal in distribution, i.e., (X, Y )
is opposite radially symmetric about (1/2, 1/2), but additional assumptions like
opposite marginal symmetry in Theorem 2.4 is needed to draw that conclusion.
3
Diﬀerential equations for copulas with oppo-
site symmetry
The following theorem provides a characterization of absolutely continuous cop-
ulas with opposite symmetry, and constitutes the basis for deriving the diﬀer-
ential equations. We also obtain a simple formula for Kendall’s τ rank cor-
relation coeﬃcient for opposite symmetric copulas. Kendall’s τ is deﬁned as
τC = −1 + 4
R 1
0
R 1
0 C(u, v)dC(u, v), cf [18, chapter 5].
Theorem 3.1. Assume that p is an integrable function on [0, 1]2satisfying
p(u, v) = p(1 −v, 1 −u)
(26)
and let
C(u, v) =
Z u
0
Z v
0
p(w, z)dwdz.
(27)
Then
C(u, v) = C(1 −v, 1 −u) + C(u, 1) + C(1, v) −C(1, 1)
(28)
and the following two conditions are equivalent:
1. C′
u(u, 1) = 1 for all u ∈[0, 1].
2. C′
v(1, v) = 1 for all v ∈[0, 1].
Furthermore, if p ≥0 these conditions are equivalent to
3. C is an absolutely continuous opposite symmetric copula.
and then if also
Z 1
0
Z 1
0
C′
uC′
vdudv < ∞,
(29)
Kendall’s τ is given by
τC = −1 + 8
Z 1
0
C(u, 1 −u)du
(30)
8


## Page 9


Proof of Theorem 3.1. By the inclusion-exclusion principle for integrals we have
Z 1
u
Z 1
v
p(w, z)dzdw = C(u, v) + C(1, 1) −C(u, 1) −C(1, v).
(31)
By change of variables and symmetry (26) we also have
Z 1
u
Z 1
v
p(w, z)dzdw =
Z 1−v
0
Z 1−u
0
p(1 −z, 1 −w)dzdw
=
Z 1−v
0
Z 1−u
0
p(w, z)dzdw = C(1 −v, 1 −u).
(32)
which proves (28).
Assume that C′
u(u, 1) = 1 for u ∈[0, 1], it follows that
C(u, 1) = u for u ∈[0, 1]. Then (28) with u = 0 simpliﬁes to 0 = C(1, v) −v,
so C′
v(1, v) = 1. Similarly, C′
v(1, v) ≡1 =⇒C′
u(u, 1) ≡1. If these conditions
hold, C(u, 1) ≡u and C(1, v) ≡v, which shows that C is a copula, which is
absolutely continuous by equation (27), and equation (28) implies equation (3),
i.e., opposite symmetry. Conversely, assuming C an absolute continuous copula
satisfying (3), diﬀerentiation yields C′
u(u, 1) ≡1 and C′
v(1, v) ≡1. Suppose in
addition that (29) holds true. Diﬀerentiation of (3) yields
C′
u(1 −v, 1 −u) = 1 −C′
v(u, v),
C′
v(1 −v, 1 −u) = 1 −C′
u(u, v)
(33)
which gives
Z 1
0
Z 1
0
C′
uC′
vdvdu =
Z 1
0
Z 1−u
0
C′
uC′
vdvdu +
Z 1
0
Z 1
1−u
C′
uC′
vdvdu
=
Z 1
0
Z 1−u
0
C′
uC′
v + (1 −C′
v)(1 −C′
u)dvdu
=
Z 1
0
Z 1−u
0
1 −C′
u −C′
vdvdu = 1
2 −2
Z 1
0
C(u, 1 −u)du
(34)
According to [18, equation (5.1.10)], equation (29) implies that τC = 1 −
4
R 1
0
R 1
0 C′
uC′
vdudv, which proves (30).
We will now show that copulas satisfying the assumptions in Theorem 2.4,
with the additional assumption of being conditionally independent on u + v ≤1
can be characterized by diﬀerential equations. This method is reminiscent of
the well known method of separation of variables for construction of solutions
to partial diﬀerential equations. This will also give a construction method for
absolutely continuous copulas with given opposite diagonal section, a problem
considered in [5], cf. Theorem 3.7 below. Later, we will modify the construction,
restricting the copula density support to v ≤H(u), which is required to solve
Problem 1.2.
9


## Page 10


Theorem 3.2. Assume that
p(u, v) =

F ′(u)G′(v)
if
u + v ≤1
F ′(1 −v)G′(1 −u)
if
u + v > 1
(35)
where F(0) = G(0) = 0, G′ ≥0 and C is given by (27). Then
C′
u(u, v) =

F ′(u)G(v)
if
u + v ≤1
G(1 −u)F ′(u) + G′(1 −u)(F(u) −F(1 −v))
if
u + v > 1
(36)
and the following are equivalent:
1. F ′ ≥0 and
G(1 −u)F ′(u) + G′(1 −u)F(u) = 1, u ∈[0, 1]
(37)
2. C(u, v) is an absolutely continuous copula,
and then
C(u, v) =

F(u)G(v)
if
u + v ≤1
F(1 −v)G(1 −u) + u + v −1
if
u + v > 1
(38)
Proof. Integration C′
u(u, v) =
R v
0 C′′
uv(u, z)dz of the piecewise deﬁned function
p = C′′
uv yields C′
u(u, v) = F ′(u)G(v) for u + v ≤1 and C′
u(u, v) = G(1 −
u)F ′(u) + G′(1 −u)(F(u) −F(1 −v)) for u + v > 1, so C′
u(u, 1) = G(1 −
u)F ′(u) + G′(1 −u)F(u).
Suppose that F ′ ≥0 and (37) holds true.
Then
p ≥0 and C′
u(u, 1) ≡1 so C is an absolutely continuous copula by Theorem
3.1.
Conversely, suppose that C is an absolutely continuous copula.
Then
C′′
uv = p ≥0 so F ′ ≥0 by (35), and (37) holds since C′
u(u, 1) ≡1. Moreover,
integration C(u, v) =
R u
0 C′
u(z, v)dz yields (38) for u + v ≤1, and (38) for
u + v > 1 follows from Theorem 3.1.
The diﬀerential equation (37) can be solved with the integrating factor
method. Moreover, a condition for F ′(u) ≥0 can be derived.
Theorem 3.3. Assume that G satisﬁes the assumptions of Theorem 3.2. Then
F(u) satisfy (37) and F(0) = 0 if and only if
F(u) = G(1 −u)
Z u
0
dz
G(1 −z)2
(39)
Moreover, if F(u) is given by (39), then
F ′(u) = G′(1 −u)
 L(0)
G(1)2 +
Z u
0
1 + L′(z)
G(1 −z)2 dz

(40)
where
L(u) = G(1 −u)
G′(1 −u).
(41)
10


## Page 11


Finally, if u∗∈[0, 1], L′(u) ≥−1 for u ∈(u∗, 1) and if
−
Z u∗
0
1 + L′(z)
G(1 −z)2 dz ≤L(0)
G(1)2
(42)
then F ′(u) ≥0 for u ∈(0, 1).
Proof. Equation (39) is obtained by multiplying (37) with the integrating factor
1/G(1 −u)2. Equation (37) yields
F ′(u) =
1
G(1 −u) −
1
L(u)F(u)
(43)
and substituting (39) in (43) using (41) yields
F ′(u) = G′(1 −u)

L(u)
G(1 −u)2 −
Z u
0
dz
G(1 −z)2

(44)
and the identity
d
du

L(u)
G(1 −u)2

= 2 + L′(u)
G(1 −u)2
(45)
yields
L(u)
G(1 −u)2 = L(0)
G(1)2 +
Z u
0
2 + L′(z)
G(1 −z)2 dz
(46)
which proves (40). Moreover, by the assumptions, u 7→−
R u
0 (1 + L′(z))/G(1 −
z)2dz has its maximum for u = u∗, so it follows from (42) that F ′(u) ≥F ′(u∗) ≥
0 for u ∈[0, 1].
Example 3.4. G(v) = v, L(u) = 1 −u, 1 + L′(u) = 0, F ′(u) = G′(1 −u)/G(1),
yields the independence copula C(u, v) = uv.
Example 3.5. If k ≥1 and G(v) = vk, then (37) has solution
F(u) = (1 −u)1−k −(1 −u)k
2k −1
(47)
and F ′(u) ≥0 for u ∈[0, 1], so
C(u, v) =

((1 −u)1−k −(1 −u)k)vk/(2k −1)
if
u + v ≤1
(1 −u)k(v1−k −vk)/(2k −1) + u + v −1
if
u + v > 1
(48)
is a one–parameter family of absolutely continuous copulas. In particular, for
k = 1 we obtain the independence copula uv. For k > 1, limu↗1 F(u) = ∞.
Example 3.6. If G(v) = sin(πv/2), then (37) has solution
F(u) = 2 sin(πu/2)/π
(49)
and F ′(u) ≥0 for u ∈[0, 1], so
C(u, v) =

2 sin(πu/2) sin(πv/2)/π
if
u + v ≤1
2 cos(πu/2) cos(πv/2)/π + u + v −1
if
u + v > 1
(50)
is an absolutely continuous copula.
11


## Page 12


Since the positivity conditions in Theorem 3.3 is formulated in terms of the
function L, it is natural to start by specifying L satisfying (42). This is also
related to the problem of constructing copulas with prescribed opposite diagonal
section ω(u) = C(u, 1 −u) considered in [5]. In fact, given ω, the function L is
given by the explicit formula (55) below. This is formulated in Theorem 3.7.
Theorem 3.7. Suppose that L is a positive real–valued function deﬁned on [0, 1]
such that
Z u
0
dz
L(z) < ∞
(51)
for u ∈[0, 1) and
lim
u→1−
Z u
0
dz
L(z) = ∞.
(52)
Let
G(v) = exp

−
Z 1−v
0
dz
L(z)

(53)
and suppose that (42) holds true. Moreover, let F(u) be given by (39). Then
C given by (38) is an absolutely continuous copula.
Moreover, the opposite
diagonal section
ω(u) ≡C(u, 1 −u)
(54)
satisﬁes
L(u) =
2ω(u)
1 −ω′(u).
(55)
Proof. Clearly, because L is positive and satisﬁes (51) and (52), G deﬁned by
(53) is positive, G is increasing (in fact strictly increasing) and G(0) = 0. More-
over, it follows from (53) that (41) holds true. By Theorem 3.3, F ′(u) ≥0
and by Theorem 3.2, C is an absolutely continuous copula. Diﬀerentiation of
F(u)G(1 −u) = ω(u) yields F ′(u)G(1 −u) −F(u)G′(1 −u) = ω′(u), so in view
of (37) we get
F ′(u)G(1 −u) = 1 + ω′(u)
2
(56)
and
F(u)G′(1 −u) = 1 −ω′(u)
2
(57)
Solving for F(u) in (57), diﬀerentiating and substituting F ′(u) in the left hand
side of (56) yields
(1 −ω′(u))G′′(1 −u)G(1 −u)
G′(1 −u)2
−ω′′(u) G(1 −u)
G′(1 −u) = 1 + ω′(u).
(58)
Using (41) and the identity
G′′(1 −u)G(1 −u)
G′(1 −u)2
= 1 + L′(u)
(59)
12


## Page 13


we get
(1 −ω′(u))L′(u) −ω′′(u)L(u) = 2ω′(u)
(60)
which is integrated to (1−ω′(u))L(u) = 2ω(u)+constant. Since ω(1) = C(1, 0) =
0 and L(1) = 0 in view of (52), the integration constant is zero, which proves
(55).
Example 3.8. Assume that k ≥1 and let L(u) = (1 −u)/k. Then we get
G(1 −u) = (1 −u)k so we recover Example 3.5. Also, L′(u) = −1/k ≥−1
so u∗= 0 and and since 0 ≤L(0) = 1/k we infer from Theorem 3.3 that an
absolutely continuous copula is obtained.
Example 3.9. Assume that a ∈[0, 1) and let L(u) = (1 −u)(1 −au). Then
G(1 −u) =
 1 −u
1 −au
1/(1−a)
and u∗= 1/2: L′(u) = −1+a(−1+2u) ≤−1 if u ≤1/2, L′(u) ≥−1 if u ≥1/2.
We obtain
Z u∗
0
1 + L′(z)
G(1 −z)2 dz =
Z 1/2
0
1 −au
1 −u
2/(1−a)
a(1 −2u)du
= 1
2F1

1,
2
1 −a, −
2
1 −a; 3; 1
2, a
2

Here F1 is the Appell series (see [10, p. 1027] for a deﬁnition), which may be
represented by Picard’s integral formula, cf. [4]:
F1(a, b, b′; c; x, y)
=
Γ(c)
Γ(a)Γ(c −a)
Z 1
0
ta−1(1 −t)c−a−1(1 −tx)−b(1 −ty)−b′dt
Here, Γ denotes Euler’s gamma function ([10, p.
901]).
The function F1 is
available in computer algebra systems like Maple R
⃝and Mathematica R
⃝, and
numerical investigation reveals that the right hand side is an increasing function
of a and approaches the value 0.861485 as a →1−. Therefore condition (42) is
satisﬁed, so Theorem 3.3 yields an absolutely continuous copula, and (39) can
be evaluated to
F(u) = uG(1 −u)F1

1,
2
1 −a, −
2
1 −a; 2; au, u

.
When 2/(1 −a) is integer, this expression can be simpliﬁed to a ﬁnite sum of
powers and logarithms, cf. [4].
13


## Page 14


4
Comparison with other methods
A method by Durante and Jaworski is found in [6], where absolutely continuous
copulas C(u, v) with given diagonal section C(t, t) are constructed, in terms of
convex combinations of singular diagonal copulas
Cδ(u, v) = min

u, v, δ(u) + δ(v)
2

(61)
(satisfying Cδ(t, t) = δ(t)). The problem with this approach for our purposes is
that the constraint v ≤H(u) imposes functional inequalities δ(H(u)) + δ(u) ≤
2u that must be fullﬁlled for the δ’s used in the construction. In comparison,
the advantage of our diﬀerential equation method is that H is used explicitly,
using only elementary calculus.
Regarding copulas and diﬀerential equations, there is a characterization of all
copulas by Jaworski, in terms of a certain type of weak solutions to diﬀerential
equations in [14]. For comparison we give here a simpliﬁed account of his method
in the special case of absolutely continuous copulas with diﬀerentiable density
and sectional inverse. For ﬁxed u ∈[0, 1] let C(u, ·)−1(z) denote the assumed
unique solution v to the equation C(u, v) = z, i.e., C(u, C(u, ·)−1(z)) = z for
all z ∈[0, 1], and deﬁne
C[u](t, z) = u−1C(ut, C(u, ·)−1(uz))
(62)
Moreover, deﬁne
FC(u, z) = ∂
∂tC[u](t, z)

t=1
−z = C′
u(u, C(u, ·)−1(uz)) −z
(63)
Now suppose that for each v ∈[0, 1], gv(u) is solution to the terminal value
problem
ug′
v(u)
=
FC(u, gv(u)), u ∈(0, 1)
(64)
gv(1)
=
v
(65)
Then C can be characterized in terms of gv(u) as
C(u, v) = ugu(v)
(66)
To see this, note that by the deﬁnition of FC and the product rule of diﬀeren-
tiation, (64) is equivalent to
d
du(ugv(u)) = C′
u(u, C(u, ·)−1(ugv(u)))
(67)
and this ODE for gv(u) is satisﬁed for gv(u) = C(u, v)/u, so by uniqueness of
solution to (64)-(65), (66) must hold. The general result (valid for all copulas)
can be found in [14, Theorems 3.1 and 3.2]. Now, applying Jaworski’s character-
ization theorem to a copula of the form (38), we need to compute C(u, ·)−1(z)
14


## Page 15


to obtain FC. For z ≤1 −u we get F(u)G(v) = z, which can be solved ex-
plicitly, yielding v = C(u, ·)−1(z) = G−1(z/F(u)). However, for z > 1 −u,
v = C(u, ·)−1(z) is implicitly deﬁned by F(1−v)G(1−u)+u+v −1 = z, which
can not be solved for v in terms of F, G and their inverses. Therefore, we have
not been able to use Jaworski’s method to obtain equations for F, G for copulas
of the type (38).
5
Absolutely continuous copulas with prescribed
support
Here we construct absolutely continuous opposite symmetric copulas with the
support of the probability measure prescribed by a constraint v ≤H(v). The
construction is simple, using elementary calculus and a piecewise deﬁnition of
the copula density, similar to Theorem 3.2
Theorem 5.1. Suppose that 0 < u0 < 1/2 and that H is a strictly increas-
ing function deﬁned on [0, 1], continuously diﬀerentiable on (0, u0), satisfying
H(u0) = 1 −u0 and satisfying the symmetry condition
H(u) + H−1(1 −u) = 1.
(68)
Furthermore, suppose that F is a diﬀerentiable function deﬁned on [u0, 1) such
that F(u0) = 0, G is a diﬀerentiable function deﬁned on [0, 1 −u0] such that
G(0) = 0, G′ ≥0 and C(u, v) given by (27), where
p(u, v) =







G′(v)/G(H(u))
if
0 < u ≤u0,
0 < v ≤H(u)
0
if
0 < u ≤u0,
H(u) < v ≤1 −u
F ′(u)G′(v)
if
u0 < u < 1,
0 < v ≤1 −u
p(1 −v, 1 −u)
if
0 < u < 1,
1 −u < v < 1
(69)
Furthermore, let
K(u) =
Z u
u0
H′(z)dz
G(1 −z)
(70)
for u0 ≤u ≤1. Then the following are equivalent:
1. F ′ ≥0 and
F ′(u)G(1 −u) + G′(1 −u)(F(u) + K(u)) = 1
(71)
for u ∈[u0, 1).
2. C(u, v) is an absolutely continuous copula, and then
(a) If 0 ≤u ≤u0 and 0 ≤v ≤H(u), then
C(u, v) = H−1(v) + (K(1 −v) −K(H−1(1 −u)))G(v)
(72)
15


## Page 16


(b) If 0 ≤u ≤u0 and H(u) ≤v ≤1 −u then
C(u, v) = u
(73)
(c) If u0 ≤u ≤1 and 0 ≤v ≤1 −u then
C(u, v) = H−1(v) + (K(1 −v) + F(u))G(v)
(74)
(d) If 0 ≤u ≤1 and u + v > 1 then C(u, v) is given by (3).
Proof. The basic idea of the proof is similar to Theorem 3.2: integrate the given
piecewise deﬁned ansatz for the copula density C′′
uv to derive C′
u and use Theo-
rem 3.1. By deﬁnition p(u, v) = C′′
uv(u, v) and piecewisely deﬁned on the regions
1-7 depicted in Figure 5 as follows; region 1: C′′
uv = G′(v)/G(H(u)), region
2,3,7: C′′
uv = 0, region 4: C′′
uv = F ′(u)G′(v), region 5: C′′
uv = F ′(1−v)G′(1−u),
and region 6: C′′
uv = G′(1 −u)/G(H(1 −v)). Integration yields C′
u(u, v) =
R v
0 C′′
uv(u, z)dz, piecewisely deﬁned as follows; region 1: C′
u = G(v)/G(H(u)),
region 2,3: C′
u = 1, region 4: C′
u = F ′(u)G(v), region 5: C′
u = F ′(u)G(1 −
u) + (F(u) −F(1 −v))G′(1 −u), region 6: C′
u = F ′(u)G(1 −u) + (F(u) +
K(H−1(v)))G′(1−u), and region 7: C′
u = F ′(u)G(1−u)+(F(u)+K(u))G′(1−
u). To derive the expression in region 6, write K on the alternate form
K(u) =
Z u0
H−1(1−u)
dw
G(H(w))
(75)
(derived by the change of variables z = 1 −H(w) = H−1(1 −w)) and note that
Z v
1−u0
dz
G(H(1 −z)) =
Z u0
1−v
dw
G(H(w))
=
Z u0
H−1(1−H−1(v))
dw
G(H(w)) = K(H−1(v))
in view of (68). If F ′ ≥0 and (71) holds true, then p ≥0 by (69) and C′
u(u, 1) ≡
1 by (71) since the left hand side of (71) is the expression for C′
u in region 7.
Thus, by theorem 3.1, C is an absolutely continous copula. Conversely, if C is
an absolutely continuous copula, then p = C′′
uv ≥0 so F ′ ≥0 and by (69), and
C′
u(u, 1) = 1 which proves (71). The conditions C′
u(u, 1) ≡1 and C′
v(1, v) ≡1
are equivalent by Theorem 3.1. Assume now that C is an absolutely continuous
copula, then C′
u = 1 in region 7 by (71). Integration C(u, v) =
R u
0 C′
u(z, v)dz
yields the following piecewise deﬁned function C(u, v); region 2,3,7: C = u
which proves (73), region 1: C = H−1(v) + (K(1 −v) −K(H−1(1 −u)))G(v)
which proves (72), and region 4: C = H−1(v) + (K(1 −v) + F(u))G(v) which
proves (74). The ﬁnal statement for u + v > 1 follows from Theorem 3.1.
16


## Page 17


0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
Figure 4: Subdivision of the unit square for piecewise deﬁnition of p = C′′
uv in
Theorem 5.1.
Equation (71) can be solved with the integrating factor method, and a pos-
itivity condition can be derived, analogous to Theorem 3.3:
Theorem 5.2. Assume that K(u) is given by (70), and G satisﬁes the assump-
tions of Theorem 5.1. Then F(u) satisﬁes (71) if and only if
F(u) = −K(u) + G(1 −u)
Z u
u0
1 + H′(z)
G(1 −z)2 dz.
(76)
Moreover, if F(u) is given by (76), then
F ′(u) = G′(1 −u)

L(u0)
G(1 −u0)2 +
Z u
u0
1 + L′(z) −H′(z)
G(1 −z)2
dz

(77)
where L is given by (41).
Finally, if u∗∈[u0, 1], L′(u) −H′(u) ≤−1 for
u ∈(u0, u∗), L′(u) −H′(u) ≥−1 for u ∈(u∗, 1) and
−
Z u∗
u0
1 + L′(z) −H′(z)
G(1 −z)2
dz ≤
L(u0)
G(1 −u0)2
(78)
then F ′(u) ≥0 for u ∈(u0, 1).
Proof. Multiplying (71) with the integrating factor 1/G(1−u)2 and integrating
by parts (using K(u0) = 0) yields
F(u) = G(1 −u)
Z u
u0
1 −G′(1 −z)K(z)
G(1 −z)2
= G(1 −u)
Z u
u0
dz
G(1 −z)2 −
K(u)
G(1 −u) +
Z u
u0
K′(z)
G(1 −z)

17


## Page 18


so substituting
K′(z) =
H′(z)
G(1 −z)
(79)
according to (70) yields (76). Solving for F ′ in (71):
F ′(u) =
1
G(1 −u) −
1
L(u)(K(u) + F(u))
(80)
and substituting
K(u) + F(u) =
Z u
u0
1 + H′(z)
G(1 −z)2
(81)
according to (76) yields
F ′(u) = G′(1 −u)

L(u)
G(1 −u)2 −
Z u
u0
1 + H′(z)
G(1 −z)2 dz

(82)
The identity (45) yields
L(u)
G(1 −u)2 =
L(u0)
G(1 −u0)2 +
Z u
u0
2 + L′(z)
G(1 −z)2 dz
(83)
which proves (77). Finally, by the assumptions, u 7→−
R u
u0(1+L′(z)−H′(z))/G(1−
z)2dz has its maximum for u = u∗, so it follows from (78) that F ′(u) ≥F ′(u∗) ≥
0 for u ∈[u0, 1].
Example 5.3. If
H(u) =

(1 −u0)u/u0
if
u ≤u0
1 −u0(1 −u)/(1 −u0)
if
u > u0 ,
(84)
G(v) = vk and k ≥(1 −u0)/(1 −2u0), then (70) yields
K(u) = ((1 −u)1−k −(1 −u0)1−k)u0
(1 −u0)(k −1)
,
(85)
(76) evaluates to
F(u) =
(1 −2u0)k −(1 −u0)
(2k −1)(k −1)(1 −u0)(1 −u)1−k
−
(1 −u0)1−2k
(2k −1)(1 −u0)(1 −u)k + (1 −u0)1−ku0
(k −1)(1 −u0).
(86)
Moreover, L(u) = (1 −u)/k, so L′(u) −H′(u) = −1/k −u0/(1 −u0) ≥−1
if and only if k ≥(1 −u0)/(1 −2u0), in which case F ′(u) is positive.
By
theorem 5.1 we obtain a two-parameter family of absolutely continuous copulas
(with parameters 0 < u0 < 1/2 and k ≥(1 −u0)/(1 −2u0)), with probability
18


## Page 19


density supported on v ≤H(u). Indeed, in this example F ′(u) can be computed
explicitly:
F ′(u) = ((1 −2u0)k −(1 −u0))(1 −u)−k + k(1 −u0)1−2k(1 −u)k−1
(2k −1)(1 −u0)
(87)
and is strictly positive on [u0, 1) if and only if the coeﬃcient for (1 −u)−k is
positive, which is equivalent to k ≥(1 −u0)/(1 −2u0).
Example 5.4. In this example we construct more solutions to Problem 1.2,
using Theorem 5.2. Let k ∈R, k > 1 and L(u) = (1 −u)/k. Then we obtain
G(v) = vk/(1 −u0)k and
K(u) = (1 −u0)k
Z u
u0
H′(z)
(1 −z)k dz
(88)
and
F(u) = −K(u) + (1 −u0)k(1 −u)k
Z u
u0
1 + H′(z)
(1 −z)2k dz
(89)
where H is given by (5) and
H′(z) =
1
√
2π exp

−∆

Φ−1(u) + ∆
2

.
(90)
Since L′(u) = −1/k and H′ decreasing we have u∗satisfying the assumptions in
Theorem 5.2 and determined by H′(u∗) = 1 −1/k. Solving this equation yields
u∗= Φ
 
−
√
2π
∆

1 −1
k

−∆
2
!
.
(91)
Thus, 1 −u∗= Φ(
√
2π(1 −1/k)/∆+ ∆/2), and also 1 −u0 = Φ(∆/2), and one
can show that condition (78) is equivalent to
Z u∗
u0
H′(z)
(1 −z)2k dz ≤(1 −u0)1−2k
2k −1
+

1 −1
k

(1 −u∗)1−2k
(92)
so if k satisﬁes this condition, an absolutely continuous copula is obtained.
19


## Page 20


0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
0
0.5
1
1.5
2
2.5
Figure 5: Copula density C′′
uv(u, v) for Example 5.4, ∆= 1, k = 2. The density
is discontinuous on the curve v = H(u) and tends to inﬁnity when approaching
(0, 0), (1, 1) or (1, 0).
-3
-2
-1
0
1
2
3
-3
-2
-1
0
1
2
3
0
0.05
0.1
0.15
0.2
0.25
Figure 6: Probability density function p(x, y) for Example 5.4, ∆= 1, k = 2.
The wiggles in the level curves at the upper right and lower left corners of right
plot are numerical artifacts.
We have the following analogue of Theorem 3.7. Here, given the opposite
diagonal section ω, the function L is given by an integral equation (96), (97)
below.
Theorem 5.5. Suppose that H, u0 satisﬁes (6) and (7). Suppose also that L is
a positive real–valued function deﬁned on [u0, 1] such that
Z u
u0
dz
L(z) < ∞
(93)
for u ∈[u0, 1) and
lim
u→1−
Z u
u0
dz
L(z) = ∞.
(94)
20


## Page 21


Let
G(v) = exp

−
Z 1−v
u0
dz
L(z)

(95)
Moreover, let K(u) and F(u) be given by (70) and (76) and suppose that (78)
holds true.
Then C given by (72)-(74) and (3) is an absolutely continuous
copula.
Moreover, the opposite diagonal section (54) satisﬁes ω(u) = u for
u ∈[0, u0] and
L(u) = 2ω(u) + G(1 −u)K(u)
1 −ω′(u)
(96)
for u ∈[u0, 1], where
G(1 −u)K(u) =
Z u
u0
exp

−
Z u
z
dw
L(w)

H′(z)dz
(97)
Proof. The proof is similar to the proof of Theorem 3.7, with some additional
terms involving K. More precisely, (56) and (57) are replaced by
G(1 −u)F ′(u) = 1 + ω′(u) −G′(1 −u)K(u)
2
(98)
and
G′(1 −u)F(u) = 1 −ω′(u) −G′(1 −u)K(u)
2
.
(99)
Solving for F in (99), diﬀerentiating and substituting for F ′ in the left hand
side of (98) yields
(1 −ω′(u))(1 + L′(u)) −ω′′(u)L(u)
= 1 + ω′(u) + K′(u)G(1 −u) −K(u)G′(1 −u)
(100)
which is integrated to (1 −ω′(u))L(u) = 2ω(u) + G(1 −u)K(u)+constant.
The equation (97) follows from (70) and (95). For each ﬁxed z, the integrand
in (97) is decreasing towards 0 as u →1−in view of (93) and (94), so by
the mononotone convergence theorem, limu→1−G(1 −u)K(u) = 0. Hence the
constant of integration is zero, which proves (96).
Proof of Theorem 1.4. Since 1+L′(z)−H′(z) ≡0, L(u0) = H(u0)−u0 = 1−2u0
and G(1 −u0) = 1 we have by (77)
F ′(u) = (1 −2u0)G′(1 −u)
(101)
so F(u) satisﬁes (12). Solving for K in (71) yields
K(u) =
1
G′(1 −u) −G(1 −u)
G′(1 −u)F ′(u) −F(u)
(102)
and substituting (12) and (101) in (102) implies that K(u) satisﬁes (11).
21


## Page 22


6
Sampling
To sample from a two–dimensional copula C(u, v) we use the conditional density
C′
u of Corollary 6.1 in the following way (cf. [18, Chap. 2.9]): First sample U, T,
independently from U(0, 1). Then for each Ti, Ti let Vi satisfy Ti = C′
u(Ui, Vi).
Then (Ui, Vi) is distributed according to C(u, v). For sampling from the copula,
the following corollary is useful:
Corollary 6.1. Suppose that C(u, v) is an absolutely continuous copula given
by Theorem 5.1 and F, G, K deﬁned accordingly. Then C′
u(u, v) is given by the
following formulas:
1. If 0 ≤u ≤u0 and 0 < v < H(u) then
C′
u(u, v) = G(v)/G(H(u))
(103)
2. If 0 ≤u ≤1 and H(u) ≤v ≤1 then
C′
u(u, v) = 1
(104)
3. If u0 < u < 1 and 0 < v ≤1 −u then
C′
u(u, v) = (1 −G′(1 −u)(K(u) + F(u)))G(v)/G(1 −u)
(105)
4. If u0 < u < 1 and 1 −u < v ≤1 −u0 then
C′
u(u, v) = 1 −G′(1 −u)(K(u) + F(1 −v))
(106)
5. If u0 < u < 1 and 1 −u0 < v ≤H(u) then
C′
u(u, v) = 1 −G′(1 −u)(K(u) −F(1 −H(1 −v)))
(107)
6. If u0 < u < 1 and H(u) < v < 1 then C′
u(u, v) = 1.
Proof. Follows from the equations for C′
u in the proof of Theorem 5.1, and
equations (68), (71).
Figure 6 illustrates sampling in Example 1.5.
Figure 7: Samples from distributions in Example 1.5, sample size 105.
22


## Page 23


7
Application to toxicological probit models
The probit model is the standard statistical method for estimating the injury
outcome of a population exposed to a toxic substance. It originates from an
analysis on the eﬀect of pesticides conducted by Bliss in 1934 [2]. The method-
ology was later cast in a more rigid mathematic formulation by Finney [8, 7].
It has since then been used frequently in toxicological assessments of the in-
jury outcome when a population has been exposed to dangerous chemicals
[16, 1, 3, 13, 15, 19, 11]. In short, the probit model operates as follows. The
exposure concentration c(t) is integrated over time to yield probit values
Γi(t) = αi + βi log
Z t
0
c(t)nidt

.
(108)
The fraction of the population that has attainted the injury at time t is then
estimated by
Φ(Γi(t))
(109)
where αi, βi, ni are model parameters associated with the substance, and Φ
is the CDF for a standard normal variable. There are often several levels of
injury outcome used in toxicology, e.g., light injury, severe injury and death.
These diﬀerent injury levels are indexed by i = 1, 2, ... in equations (108)-(109).
The fraction of the population that obtains an injury increases continuously
with growing exposure due to the individual variation of the toxic susceptiblity
within the population. It is believed that modeling this variation improves the
quantitative toxicological risk assessment, cf. [12].
A population that is not resolved on an individual level is referred to as a
macroscopic population and can be described as a density ﬁeld. In contrast, a
population can be described as a set of discrete individuals, referred to as agents.
A model that uses this type of population representation is called a microscale
model or an agent–based model. In an agent–based toxicological model, see for
example [15], the overall population statistics is obtained from the set of agents
that are exposed to the toxic substance. In such a setting, individual probit
values Γi(t), acquired by exposure to individual model concentrations c(t), are
computed for each agent. In the transition from a macroscopic population to
an agent–based population, it is convenient to distribute individual threshold
values, γi, for the probit values to all agents representing their susceptibilities.
Thus, when an agent has been exposed to a concentration yielding a probit
value exceeding the corresponding threshold value, the agent has acquired that
injury. Every agent is attributed one threshold value for each injury level. These
threshold values are drawn from a standard normal distribution to maintain the
overall probability distribution for the entire population. This method implies
that the injury outcome of the agent–based population approaches asymptot-
ically that of the macrosopic population (with static populations) when the
number of agents increases. An advantage with an agent–based population is
that the agents may have individual properties including their movement pat-
terns.
In a dynamic simulation, each agent follows its individual spacetime
23


## Page 24


path, passing through concentration ﬁelds, and thereby proceeds through some
or all of the injury stages, transiting successive injury stages when the agent’s
increasing probit functions Γi(t) pass their threshold values γi. As mentioned,
the individual toxic susceptibility thresholds γi are random variables and must
obey the requirement
P(γi ≤Γ) = Φ(Γ)
(110)
We propose that the γ1, γ2, ... are modeled as a discrete time Markov process
with absolutely continuous transition densities pi+1|i, so by the Markov property,
the joint density p is
p(γ1, ..., γn) = p1(γ1)p2|1(γ2 | γ1)p3|2(γ3 | γ2)...pn|n−1(γn | γn−1).
(111)
However, there is a potential pitfall: the injury stages must be passed in the
correct order. Therefore, it must be true with probability one that if an injury
level is acquired, then also the previous injury level is acquired, i.e.
γi+1 ≤Γi+1(t) =⇒γi ≤Γi(t).
(112)
Therefore, the transition densities pi+1|i must satisfy
pi+1|i(γi+1 | γi) = 0 if γi+1 ≤Γi+1(t) and γi > Γi(t).
(113)
This imposes a restriction on the support of the joint probability density of
(γi, γi+1), which we need to investigate in order to ensure that the model is
consistent. To this end, we need to relate possible values of Γi(t), Γi+1(t) for all
possible exposures c(t), t ≥0. This can be done in terms of
Γi(t) −αi
βi
= log
Z t
0
cnidt

(114)
according to the following lemma:
Lemma 7.1. Assume that n ≥m > 0 and c ≥0, t > 0. Then
log
Z t
0
cmdt

≤m
n log
Z t
0
cndt

+

1 −m
n

log(t)
(115)
and
log
Z t
0
cndt

≤log
Z t
0
cmdt

+ (n −m) log

max
[0,t] c

(116)
Moreover, the inequalities are sharp: if c(t) =constant, then equalities holds in
the inequalities above.
Proof. Apply H¨older’s inequality
R
fgdt ≤(f pdt)1/p (gqdt)1/q and the elemen-
tary estimate
R
f pdt ≤(max f)p−1 R
fdt with f = cm, g = 1 and p = n/m.
The following theorems provide suﬃcient conditions for (112), and necessary
compatibility conditions for the probit parameters α, β, n.
24


## Page 25


Theorem 7.2. Assume that Γi(t), Γi+1(t) are probit functions deﬁned by (108),
and ni+1 ≤ni. Also assume that (γi, γi+1) is a bivariate random variable such
that
γi+1 −αi+1
βi+1
≥ni+1
ni
γi −αi
βi
+

1 −ni+1
ni

log(t)
(117)
almost surely. Then γi+1 ≤Γi+1(t) =⇒γi ≤Γi(t) almost surely. Moreover,
there exists standard normal γi, γi+1 satisfying (117) if and only if
ni+1βi+1 = niβi
(118)
and
∆i ≡αi −αi+1 −βi+1

1 −ni+1
ni

log t ≥0,
(119)
and then if ∆i > 0 there exists (γi, γi+1) with absolutely continuous joint density.
Proof. Assume that γi+1 ≤Γi+1(t). Then we get by (114), (115) with m = ni+1,
n = ni, and (117) that
ni+1
ni
Γi(t) −αi
βi
+

1 −ni+1
ni

log(t)
≥Γi+1(t) −αi+1
βi+1
≥γi+1 −αi+1
βi+1
≥ni+1
ni
γi −αi
βi
+

1 −ni+1
ni

log(t)
(120)
i.e., Γi(t) ≥γi, which proves the ﬁrst part.
The second part follows from
Proposition 1.1, since equation (117) is equivalent to equation (1) with X = −γi,
Y = −γi+1, a = (βi+1ni+1)/(βini) and
∆= βi+1ni+1
βini
αi −αi+1 −βi+1

1 −ni+1
ni

log(t),
and a = 1, ∆≥0 is equivalent to equations (118), (119).
Theorem 7.3. Assume that Γi(t), Γi+1(t) are probit functions deﬁned by (108),
and ni+1 ≥ni. Also assume that (γi, γi+1) is a bivariate random variable such
that
γi+1 −αi+1
βi+1
≥γi −αi
βi
+ (ni+1 −ni) log

max
[0,t] c

(121)
almost surely. Then γi+1 ≤Γi+1(t) =⇒γi ≤Γi(t) almost surely. Moreover,
there exist standard normal γi, γi+1 satisfying (121) if and only if
βi+1 = βi
(122)
and
∆i ≡αi −αi+1 −βi(ni+1 −ni) log

max
[0,t] c

≥0,
(123)
and then if ∆i > 0 there exists (γi, γi+1) with absolutely continuous joint density.
25


## Page 26


Proof of Theorem 7.3. Assume that γi+1 ≤Γi+1(t).
Then we get by (114),
(116) with m = ni, n = ni+1 and (121) that
Γi(t) −αi
βi
+ (ni+1 −ni) log

max
[0,t] c

≥Γi+1(t) −αi+1
βi+1
≥γi+1 −αi+1
βi+1
≥γi −αi
βi
+ (ni+1 −ni) log

max
[0,t] c

(124)
i.e., Γi(t) ≥γi, which proves the ﬁrst part.
The second part follows from
Proposition 1.1, since equation (121) is equivalent to equation (1) with X = −γi,
Y = −γi+1, a = βi+1/βi and
∆= βi+1
βi
αi −αi+1 −βi+1 (ni+1 −ni) log

max
[0,t] c(t)

,
and a = 1, ∆≥0 is equivalent to equations (122), (123).
Remark. Note that if ni+1 = ni, then the compatibility conditions (118), (119)
and (122), (123) in the preceding theorems involve only the probit coeﬃcients
α, β, n, not t or max c.
References
[1] O. Bj¨ornham, H. Grahn, P. von Schoenberg, B. Liljedahl, A. Waleij, and
N. Niklas Br¨annstr¨om. The 2016 Al-Mishraq sulphur plant ﬁre: Source
and health risk area estimation. Atmospheric Environment, 169:287 – 296,
2017.
[2] C. I. Bliss. The method of probits. Science, 79(2037):38–39, 1934.
[3] J. Burman and L. Jonsson. Issues when linking computational ﬂuid dynam-
ics for urban modeling to toxic load models: The need for further research.
Atmospheric Environment, 104:112 – 124, 2015.
[4] A. Cuyt, K. Driver, J. Tan, and B. Verdonk. A ﬁnite sum representation of
the Appell series F1(a, b, b′; c; x, y). Journal of Computational and Applied
Mathematics, 105(1):213 – 219, 1999.
[5] B. De Baets, H. De Meyer, and M. Ubeda-Flores. Opposite diagonal sec-
tions of quasi–copulas and copulas. International Journal of Uncertainty,
Fuzziness and Knowledge-Based Systems, 17(04):481–490, 2009.
[6] F. Durante and P. Jaworski. Absolutely Continuous Copulas with Given
Diagonal Sections. Communications in Statistics - Theory and Methods,
37(18):2924–2942, 2008.
26


## Page 27


[7] D. J. Finney. Probit analysis. Cambridge University Press, 1977.
[8] D. J. Finney and F. Tattersﬁeld. Probit analysis. Cambridge University
Press, 1952.
[9] M. U. Flores, E. de Amo, A. F. Durante, and J. F. Sanchez. Copulas and
Dependence Models with Applications. Springer, 2017.
[10] I. S. Gradshteyn and I. M. Ryzhik. Table of integrals, series, and products.
Elsevier/Academic Press, Amsterdam, eighth edition, 2014.
Translated
from the Russian, Translation edited and with a preface by Alan Jeﬀrey and
Daniel Zwillinger, With one CD-ROM (Windows, Macintosh and UNIX).
[11] H. Haghnazarloo, M. Parvini, and M. N. Lotfollahi. Consequence modeling
of a real rupture of toluene storage tank. Journal of Loss Prevention in the
Process Industries, 37:11 – 18, 2015.
[12] D. Hattis, P. Banati, and R. Goble. Distributions of Individual Suscepti-
bility among Humans for Toxic Eﬀects: How Much Protection Does the
Traditional Tenfold Factor Provide for What Fraction of Which Kinds of
Chemicals and Eﬀects?
Annals of the New York Academy of Sciences,
895(1):286–316, 1999.
[13] U. Hauptmanns. A risk-based approach to land-use planning. Journal of
Hazardous Materials, 125(1):1 – 9, 2005.
[14] P. Jaworski.
On the Characterization of Copulas by Diﬀerential Equa-
tions. Communications in Statistics - Theory and Methods, 43(16):3402–
3428, 2014.
[15] R. Lovreglio, E. Ronchi, G. Maragkos, T. Beji, and B. Merci. A dynamic
approach for the impact of a toxic gas dispersion hazard considering hu-
man behaviour and dispersion modelling. Journal of Hazardous Materials,
318:758 – 771, 2016.
[16] M. A. Mcbride, A. B. Reeves, M. D. Vanderheyden, C. J. Lea, and X. X.
Zhou. Use of advanced techniques to model the dispersion of chlorine in
complex terrain. Process Safety and Environmental Protection, 79(2):89 –
102, 2001.
[17] R. B. Nelsen. Some concepts of bivariate symmetry. Journal of Nonpara-
metric Statistics, 3(1):95–101, 1993.
[18] R. B. Nelsen. An Introduction to Copulas. Springer, 1999.
[19] S. A. Stage. Determination of Acute Exposure Guideline Levels in a Dis-
persion Model.
Journal of the Air & Waste Management Association,
54(1):49–59, 2004.
27

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1905_09306v1_absolutely_continuous_copulas_with_prescribed_support_constructed_by_differentia
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1905_09306V1_ABSOLUTELY_CONTINUOUS_COPULAS_WITH_PRESCRIBED_SUPPORT_CONSTRUCTED_BY_DIFFERENTIA.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

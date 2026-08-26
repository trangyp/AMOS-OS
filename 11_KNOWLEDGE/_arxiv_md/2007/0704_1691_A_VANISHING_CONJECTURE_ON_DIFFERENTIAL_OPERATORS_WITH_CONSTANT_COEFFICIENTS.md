---
canon-group: reference
rscf-state: source-claim
arxiv_id: 704.1691
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0704.1691_A_Vanishing_Conjecture_on_Differential_Operators_with_Constant_Coefficients

> Source: 0704.1691_A_Vanishing_Conjecture_on_Differential_Operators_with_Constant_Coefficients.pdf

> Pages: 32

---


## Page 1


arXiv:0704.1691v2  [math.CV]  28 Oct 2007
A VANISHING CONJECTURE ON DIFFERENTIAL
OPERATORS WITH CONSTANT COEFFICIENTS
WENHUA ZHAO
Abstract. In the recent progress [BE1], [Me] and [Z2], the well-
known JC (Jacobian conjecture) ([BCW], [E]) has been reduced
to a VC (vanishing conjecture) on the Laplace operators and HN
(Hessian nilpotent) polynomials (the polynomials whose Hessian
matrix are nilpotent). In this paper, we ﬁrst show that the vanish-
ing conjecture above, hence also the JC, is equivalent to a vanishing
conjecture for all 2nd order homogeneous diﬀerential operators Λ
and Λ-nilpotent polynomials P (the polynomials P(z) satisfying
ΛmP m = 0 for all m ≥1). We then transform some results in the
literature on the JC, HN polynomials and the VC of the Laplace
operators to certain results on Λ-nilpotent polynomials and the
associated VC for 2nd order homogeneous diﬀerential operators
Λ.
This part of the paper can also be read as a short survey
on HN polynomials and the associated VC in the more general
setting. Finally, we discuss a still-to-be-understood connection of
Λ-nilpotent polynomials in general with the classical orthogonal
polynomials in one or more variables. This connection provides
a conceptual understanding for the isotropic properties of homo-
geneous Λ-nilpotent polynomials for 2nd order homogeneous full
rank diﬀerential operators Λ with constant coeﬃcients.
1. Introduction
Let z = (z1, z2, . . . , zn, . . . ) be a sequence of free commutative vari-
ables and D = (D1, D2, . . . , Dn, . . . ) with Di :=
∂
∂zi (i ≥1). For any
n ≥1, denote by An (resp. ¯An) the algebra of polynomials (resp. formal
power series) in zi (1 ≤i ≤n). Furthermore, we denote by D[An] or
D[n] (resp. D[An] or D[n]) the algebra of diﬀerential operators of the
polynomial algebra An (resp. with constant coeﬃcients). Note that, for
any k ≥n, elements of D[n] are also diﬀerential operators of Ak and
Date: November 7, 2018.
2000 Mathematics Subject Classiﬁcation. 14R15, 33C45, 32W99.
Key words and phrases. Diﬀerential operators with constant coeﬃcients, Λ-
nilpotent polynomials, Hessian nilpotent polynomials, classical orthogonal poly-
nomials, the Jacobian conjecture.
1


## Page 2


2
WENHUA ZHAO
¯Ak. For any d ≥0, denote by Dd[n] the set of homogeneous diﬀeren-
tial operators of order d with constants coeﬃcients. We let A (resp. ¯A)
be the union of An (resp. ¯An) (n ≥1), D (resp. D) the union of D[n]
(resp. D[n]) (n ≥1), and, for any d ≥1, Dd the union of Dd[n] (n ≥1).
Recall that JC (the Jacobian conjecture) which was ﬁrst proposed
by Keller [Ke] in 1939, claims that, for any polynomial map F of Cn
with Jacobian j(F) = 1, its formal inverse map G must also be a
polynomial map. Despite intense study from mathematicians in more
than sixty years, the conjecture is still open even for the case n = 2.
For more history and known results before 2000 on JC, see [BCW], [E]
and references there.
Based on the remarkable symmetric reduction achieved in [BE1],
[Me] and the classical celebrated homogeneous reduction [BCW] and
[Y] on JC, the author in [Z2] reduced JC further to the following
vanishing conjecture on the Laplace operators ∆n := Pn
i=1 D2
i of the
polynomial algebra An and HN (Hessian nilpotent) polynomials P(z) ∈
An, where we say a polynomial or formal power series P(z) ∈¯An is
HN if its Hessian matrix Hes (P):= ( ∂2P
∂zi∂zj )n×n is nilpotent.
Conjecture 1.1. For any HN (homogeneous) polynomial P(z) ∈An
(of degree d = 4), we have ∆m
n P m+1(z) = 0 when m >> 0.
Note that, the following criteria of Hessian nilpotency were also
proved in Theorem 4.3, [Z2].
Theorem 1.2. For any P(z) ∈¯An with o(P(z)) ≥2, the following
statements are equivalent.
(1) P(z) is HN.
(2) ∆mP m = 0 for any m ≥1.
(3) ∆mP m = 0 for any 1 ≤m ≤n.
Through the criteria in the proposition above, Conjecture 1.1 can
be generalized to other diﬀerential operators as follows (see Conjecture
1.4 below).
First let us ﬁx the following notion that will be used throughout the
paper.
Deﬁnition 1.3. Let Λ ∈D[An] and P(z) ∈¯An.
We say P(z) is
Λ-nilpotent if ΛmP m = 0 for any m ≥1.
Note that, when Λ is the Laplace operator ∆n, by Theorem 1.2, a
polynomial or formal power series P(z) ∈An is Λ-nilpotent iﬀit is HN.
With the notion above, Conjecture 1.1 has the following natural
generalization to diﬀerential operators with constant coeﬃcients.


## Page 3


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
3
Conjecture 1.4. For any n ≥1 and Λ ∈D[n], if P(z) ∈An is Λ-
nilpotent, then ΛmP m+1 = 0 when m >> 0.
We call the conjecture above the vanishing conjecture for diﬀerential
operators with constant coeﬃcients and denote it by VC. The special
case of VC with P(z) homogeneous is called the homogeneous vanish-
ing conjecture and denoted by HVC. When the number n of variables
is ﬁxed, VC (resp. HVC) is called (resp. homogeneous) vanishing con-
jecture in n variables and denoted by VC[n] (resp. HVC[n]).
Two remarks on VC are as follows. First, due to a counter-example
given by M. de Bondt (see example 2.4), VC does not hold in general
for diﬀerential operators with non-constant coeﬃcients. Secondly, one
may also allow P(z) in VC to be any Λ-nilpotent formal power series.
No counter-example to this more general VC is known yet.
In this paper, we ﬁrst apply certain linear automorphisms and Lef-
schetz’s principle to show Conjecture 1.1, hence also JC, is equivalent
to VC or HVC for all 2nd order homogeneous diﬀerential operators
Λ ∈D2 (see Theorem 2.9). We then in Section 3 transform some results
on JC, HN polynomials and Conjecture 1.1 obtained in [Wa], [BE2],
[BE3], [Z2], [Z3] and [EZ] to certain results on Λ-nilpotent (Λ ∈D2)
polynomials and VC for Λ. Another purpose of this section is to give
a survey on recent study on Conjecture 1.1 and HN polynomials in the
more general setting of Λ ∈D2 and Λ-nilpotent polynomials. This is
also why some results in the general setting, even though their proofs
are straightforward, are also included here.
Even though, due to M. de Bondt’s counter-example (see Example
2.4), VC does not hold for all diﬀerential operators with non-constant
coeﬃcients, it is still interesting to consider whether or not VC holds
for higher order diﬀerential operators with constant coeﬃcients; and
if it also holds even for certain families of diﬀerential operators with
non-constant coeﬃcients. For example, when Λ = Da with a ∈Nn and
|a| ≥2, VC[n] for Λ is equivalent to a conjecture on Laurent polynomi-
als (see Conjecture 3.21). This conjecture is very similar to a non-trivial
theorem (see Theorem 3.20) on Laurent polynomials, which was ﬁrst
conjectured by O. Mathieu [Ma] and later proved by J. Duistermaat
and W. van der Kallen [DK].
In general, to consider the questions above, one certainly needs to get
better understandings on the Λ-nilpotency condition, i.e. ΛmP m = 0
for any m ≥1. One natural way to look at this condition is to consider
the sequences of the form {ΛmP m | m ≥1} for general diﬀerential op-
erators Λ and polynomials P(z) ∈A. What special properties do these


## Page 4


4
WENHUA ZHAO
sequences have so that VC wants them all vanish? Do they play any
important roles in other areas of mathematics?
The answer to the ﬁrst question above is still not clear. The answer
to the later seems to be ”No”. It seems that the sequences of the form
{ΛmP m | m ≥1} do not appear very often in mathematics. But the
answer turns out to be “Yes” if one considers the question in the setting
of some localizations B of An. Actually, as we will discuss in some detail
in subsection 4.1, all classical orthogonal polynomials in one variable
have the form {ΛmP m | m ≥1} except there one often chooses P(z)
from some localizations B of An and Λ a diﬀerential operators of B.
Some classical polynomials in several variables can also be obtained
from sequences of the form {ΛmP m | m ≥1} by a slightly modiﬁed
procedure.
Note that, due to their applications in many diﬀerent areas of math-
ematics, especially in ODE, PDE, the eigenfunction problems and rep-
resentation theory, orthogonal polynomials have been under intense
study by mathematicians in the last two centuries. For example, in
[SHW] published in 1940, about 2000 published articles mostly on one-
variable orthogonal polynomials have been included. The classical ref-
erence for one-variable orthogonal polynomials is [Sz] (see also [AS],
[C], [Si]). For multi-variable orthogonal polynomials, see [DX], [Ko]
and references there.
It is hard to believe that the connection discussed above between
Λ-nilpotent polynomials or formal power series and classical orthog-
onal polynomials is just a coincidence. But a precise understanding
of this connection still remains mysterious. What is clear is that, Λ-
nilpotent polynomials or formal power series and the polynomials or
formal power series P(z) ∈¯An such that the sequence {ΛmP m | m ≥1}
for some diﬀerential operator Λ provides a sequence of orthogonal poly-
nomials lie in two opposite extreme sides, since, from the same sequence
{ΛmP m | m ≥1}, the former provides nothing but zero; while the later
provides an orthogonal basis for An.
Therefore, one naturally expects that Λ-nilpotent polynomials P(z)∈
An should be isotropic with respect to a certain C-bilinear form of An.
It turns out that, as we will show in Theorem 4.10 and Corollary 4.11,
it is indeed the case when P(z) is homogeneous and Λ ∈D2[n] is of
full rank. Actually, in this case ΛmP m+1 (m ≥0) are all isotropic with
respect to same properly deﬁned C-bilinear form. Note that, Theorem
4.10 and Corollary 4.11 are just transformations of the isotropic prop-
erties of HN nilpotent polynomials, which were ﬁrst proved in [Z2].
But the proof in [Z2] is very technical and lacks any convincing inter-
pretations. From the “formal” connection of Λ-nilpotent polynomials


## Page 5


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
5
and orthogonal polynomials discussed above, the isotropic properties
of homogeneous Λ-nilpotent polynomials with Λ ∈D2[n] of full rank
become much more natural.
The arrangement of the paper is as follows. In Section 2, we mainly
show that Conjecture 1.1, hence also JC, is equivalent to VC or HVC
for all Λ ∈D2 (see Theorem 2.9). One consequence of this equivalence
is that, to prove or disprove VC or JC, the Laplace operators are not
the only choices, even though they are the best in many situations.
Instead, one can choose any sequence Λnk ∈D2 with strictly increasing
ranks (see Proposition 2.10). For example, one can choose the “Laplace
operators” with respect to the Minkowski metric or symplectic metric,
or simply choose Λ to be the complex ¯∂-Laplace operator ∆¯∂,k (k ≥1)
in Eq. (2.11).
In Section 3, we transform some results on JC, HN polynomials
and Conjecture 1.1 in the literature to certain results on Λ-nilpotent
(Λ ∈D2) polynomials P(z) and VC for Λ.
In subsection 3.1, we
discuss some results on the polynomial maps and PDEs associated
with Λ-nilpotent polynomials for Λ ∈D2[n] of full rank (see Theorems
3.1–3.3). The results in this subsection are transformations of those
in [Z1] and [Z2] on HN polynomials and their associated symmetric
polynomial maps.
In subsection 3.2, we give four criteria of Λ-nilpotency (Λ ∈D2) (see
Propositions 3.4, 3.6, 3.7 and 3.10). The criteria in this subsection
are transformations of the criteria of Hessian nilpotency derived in
[Z2] and [Z3]. In subsection 3.3, we transform some results in [BCW],
[Wa] and [Y] on JC; [BE2] and [BE3] on symmetric polynomial maps;
[Z2], [Z3] and [EZ] on HN polynomials to certain results on VC for
Λ ∈D2. Finally, we recall a result in [Z3] which says, VC over ﬁelds
k of characteristic p > 0, even under some conditions weaker than Λ-
nilpotency, actually holds for any diﬀerential operators Λ of k[z] (see
Proposition 3.22 and Corollary 3.23).
In subsection 3.4, we consider VC for high order diﬀerential opera-
tors with constant coeﬃcients. In particular, we show in Proposition
3.18 VC holds for Λ = δk (k ≥1), where δ is a derivation of A. In
particular, VC holds for any Λ ∈D1 (see Corollary 3.19). We also
show that, when Λ = Da with a ∈Nn and |a| ≥2, VC is equivalent
to a conjecture, Conjecture 3.21, on Laurent polynomials. This con-
jecture is very similar to a non-trivial theorem (see Theorem 3.20) ﬁrst
conjectured by O. Mathieu [Ma] and later proved by J. Duistermaat
and W. van der Kallen [DK].


## Page 6


6
WENHUA ZHAO
In subsection 4.1, by using Rodrigues’ formulas Eq. (4.1), we show
that all classical orthogonal polynomials in one variable have the form
{ΛmP m | m ≥1} for some P(z) in certain localizations B of An and Λ a
diﬀerential operators of B. We also show that some classical polynomi-
als in several variables can also be obtained from sequences of the form
{ΛmP m | m ≥1} with a slight modiﬁcation. Some of the most classical
orthogonal polynomials in one or more variables are brieﬂy discussed
in Examples 4.2–4.5, 4.8 and 4.9. In subsection 4.2, we transform the
isotropic properties of homogeneous HN homogeneous polynomials de-
rived in [Z2] to homogeneous Λ-nilpotent polynomials for Λ ∈D2[n] of
full rank (see Theorem 4.10 and Corollary 4.11).
Acknowledgment: The author is very grateful to Michiel de Bondt
for sharing his counterexample (see Example 2.4) with the author, and
to Arno van den Essen for inspiring personal communications. The
author would also like to thank the referee very much for many valuable
suggestions to improve the ﬁrst version of the paper.
2. The Vanishing Conjecture for the 2nd Order
Homogeneous Diﬀerential Operators with Constant
Coeﬃcients
In this section, we apply certain linear automorphisms and Lef-
schetz’s principle to show Conjecture 1.1, hence also JC, is equivalent
to VC or HVC for all Λ ∈D2 (see Theorem 2.9). In subsection 2.1, we
ﬁx some notation and recall some lemmas that will be needed through-
out this paper. In subsection 2.2, we prove the main results of this
section, Theorem 2.9 and Proposition 2.10.
2.1. Notation and Preliminaries. Throughout this paper, unless
stated otherwise, we will keep using the notations and terminology in-
troduced in the previous section and also the ones ﬁxed as below.
(1) For any P(z) ∈An, we denote by ∇P the gradient of P(z), i.e.
we set
∇P(z):= (D1P, D2P, . . . , DnP).
(2.1)
(2) For any n ≥1, we let SM(n, C) (resp. SGL(n, C)) denote the
symmetric complex n × n (resp. invertible) matrices.
(3) For any A = (aij) ∈SM(n, C), we set
∆A :=
n
X
i,j=1
aijDiDj ∈D2[n].
(2.2)


## Page 7


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
7
Note that, for any Λ ∈D2[n], there exists a unique A ∈
SM(n, C) such that Λ = ∆A. We deﬁne the rank of Λ = ∆A
simply to be the rank of the matrix A.
(4) For any n ≥1, Λ ∈D2[n] is said to be full rank if Λ has rank n.
The set of full rank elements of D2[n] will be denoted by D◦
2[n].
(5) For any r ≥1, we set
∆r :=
r
X
i=1
D2
i .
(2.3)
Note that ∆r is a full rank element in D2[r] but not in D2[n] for
any n > r.
For U ∈GL(n, C), we deﬁne
ΦU : ¯
An →
¯
An
(2.4)
P(z) →P(U−1z)
and
ΨU : D[n]
→
D[n]
(2.5)
Λ
→ΦU ◦Λ ◦Φ−1
U
It is easy to see that, ΦU (resp. ΨU) is an algebra automorphism of
An (resp. D[n]). Moreover, the following standard facts are also easy
to check directly.
Lemma 2.1. (a) For any U = (uij) ∈GL(n, C), P(z) ∈¯An and
Λ ∈D[n], we have
ΦU(ΛP) = ΨU(Λ)ΦU(P).
(2.6)
(b) For any 1 ≤i ≤n and f(z) ∈An we have
ΨU(Di) =
n
X
j=1
ujiDj,
ΨU(f(D)) = f(UτD).
In particular, for any A ∈SM(n, C), we have
ΨU(∆A) = ∆UAUτ.
(2.7)
The following lemma will play a crucial role in our later arguments.
Actually the lemma can be stated in a stronger form (see [Hu], for
example) which we do not need here.


## Page 8


8
WENHUA ZHAO
Lemma 2.2. For any A ∈SM(n, C) of rank r > 0, there exists U ∈
GL(n, C) such that
A = U

Ir×r
0
0
0

Uτ
(2.8)
Combining Lemmas 2.1 and 2.2, it is easy to see we have the following
corollary.
Corollary 2.3. For any n ≥1 and Λ, Ξ ∈D2[n] of same rank, there
exists U ∈GL(n, C) such that ΨU(Λ) = Ξ.
2.2. The Vanishing Conjecture for the 2nd Order Homoge-
neous Diﬀerential Operators with Constant Coeﬃcients. In
this subsection, we show that Conjecture 1.1, hence also JC, is actu-
ally equivalent to VC or HVC for all 2nd order homogeneous diﬀer-
ential operators Λ ∈D2 (see Theorem 2.9). We also show that the
Laplace operators are not the only choices in the study of VC or JC
(see Proposition 2.10 and Example 2.11).
First, let us point out that VC fails badly for diﬀerential opera-
tors with non-constant coeﬃcients. The following counter-example was
given by M. de Bondt [B].
Example 2.4. Let x be a free variable and Λ = x d2
dx2. Let P(x) = x.
Then one can check inductively that P(x) is Λ-nilpotent, but ΛmP m+1 ̸=
0 for any m ≥1.
Lemma 2.5. For any Λ ∈D[n], U ∈GL(n, C), A ∈SM(n, C) and
P(z) ∈¯An, we have
(a) P(z) is Λ-nilpotent iﬀΦU(P) is ΨU(Λ)-nilpotent. In particular,
P(z) is ∆A-nilpotent iﬀΦU(P) = P(U−1z) is ∆UAUτ-nilpotent.
(b) VC[n] (resp. HVC[n]) holds for Λ iﬀit holds for ΨU(Λ). In
particular, VC[n] (resp. HVC[n]) holds for ∆A iﬀit holds for
∆UAUτ.
Proof:
Note ﬁrst that, for any m, k ≥1, we have
ΦU
 ΛmP k
= (ΦUΛmΦ−1
U ) ΦUP k
= (ΦUΛΦ−1
U )m(ΦUP)k
= [ΨU(Λ)]m(ΦUP)k.
When Λ = ∆A, by Eq. (2.7), we further have
ΦU
 ∆m
AP k
= Λm
UAUτ(ΦUP)k.


## Page 9


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
9
Since ΦU (resp. ΨU) is an automorphism of ¯An (resp. D[n]), it is easy
to check directly that both (a) and (b) follow from the equations above.
✷
Combining the lemma above with Corollary 2.3, we immediately
have the following corollary.
Corollary 2.6. Suppose HVC[n] (resp. VC[n]) holds for a diﬀerential
operator Λ ∈D2[n] of rank r ≥1. Then HVC[n] (resp. VC[n]) holds
for all diﬀerential operators Ξ ∈D2[n] of rank r.
Actually we can derive much more (as follows) from the conditions
in the corollary above.
Proposition 2.7. (a) Suppose HVC[n] holds for a full rank Λ ∈D◦
2[n].
Then, for any k ≤n, HVC[k] holds for all full rank Ξ ∈D◦
2[k].
(b) Suppose VC[n] holds for a full rank Λ ∈D◦
2[n]. Then, for any
m ≥n, VC[m] holds for all Ξ ∈D2[m] of rank n.
Proof:
Note ﬁrst that, the cases k = n in (a) and m = n in (b)
follow directly from Corollary 2.6. So we may assume k < n in (a) and
m > n in (b). Secondly, by Corollary 2.6, it will be enough to show
HVC[k] (k < n) holds for ∆k for (a) and VC[m] (m > n) holds for
∆n for (b).
(a) Let P ∈Ak a homogeneous ∆k-nilpotent polynomial. We view
∆k and P as elements of D2[n] and An, respectively. Since P does not
depend on zi (k + 1 ≤i ≤n), for any m, ℓ≥0, we have
∆m
k P ℓ= ∆m
n P ℓ.
Hence, P is also ∆n-nilpotent. Since HVC[n] holds for ∆n (as pointed
out at the beginning of the proof), we have ∆m
k P m+1 = ∆m
n P m+1 = 0
when m >> 0. Therefore, HVC[k] holds for ∆k.
(b) Let K be the rational function ﬁeld C(zn+1, . . . , zm). We view Am
as a subalgebra of the polynomial algebra K[z1, . . . , zn] in the standard
way. Note that the diﬀerential operator ∆n = Pn
i=1 D2
i of Am extends
canonically to a diﬀerential operator of K[z1, . . . , zn] with constant co-
eﬃcients.
Since VC[n] holds for ∆n over the complex ﬁeld (as pointed out
at the beginning of the proof), by Lefschetz’s principle, we know that
VC[n] also holds for ∆n over the ﬁeld K.
Therefore, for any ∆n-
nilpotent P(z) ∈Am, by viewing ∆n as an element of D2(K[z1, . . . , zn])
and P(z) an element of K[z1, . . . , zn] (which is still ∆n-nilpotent in the
new setting), we have ∆k
nP k+1 = 0 when k >> 0. Hence VC[m] holds
for P(z) ∈Am and ∆n ∈D2[m].
✷


## Page 10


10
WENHUA ZHAO
Proposition 2.8. Suppose HVC[n] holds for a diﬀerential operator
Λ ∈D2[n] with rank r < n. Then, for any k ≥r, VC[k] holds for all
Ξ ∈D2[k] of rank r.
Proof:
First, by Corollary 2.6, we know HVC[n] holds for ∆r. To
show Proposition 2.8, by Proposition 2.7, (b), it will be enough to show
that VC[r] holds for ∆r.
Let P ∈Ar ⊂An be a ∆r-nilpotent polynomial. If P is homoge-
neous, there is nothing to prove since, as pointed out above, HVC[n]
holds for ∆r. Otherwise, we homogenize P(z) to eP ∈Ar+1 ⊆An.
Since ∆r is a homogeneous diﬀerential operator, it is easy to see that,
for any m, k ≥1, ∆m
r P k = 0 iﬀ∆m
r eP k = 0. Therefore, eP ∈An is
also ∆r-nilpotent when we view ∆r as a diﬀerential operator of An.
Since HVC[n] holds for ∆r, we have that ∆m
r eP m+1 = 0 when m >> 0.
Then, by the observation above again, we also have ∆m
r P m+1 = 0 when
m >> 0. Therefore, VC[r] holds for ∆r.
✷
Now we are ready to prove our main result of this section.
Theorem 2.9. The following statements are equivalent to each other.
(1) JC holds.
(2) HVC[n] (n ≥1) hold for the Laplace operator ∆n.
(3) VC[n] (n ≥1) hold for the Laplace operator ∆n.
(4) HVC[n] (n ≥1) hold for all Λ ∈D2[n].
(5) VC[n] (n ≥1) hold for all Λ ∈D2[n].
Proof:
First, the equivalences of (1), (2) and (3) have been estab-
lished in Theorem 7.2 in [Z2]. While (4) ⇒(2), (5) ⇒(3) and (5) ⇒(4)
are trivial. Therefore, it will be enough to show (3) ⇒(5).
To show (3) ⇒(5), we ﬁx any n ≥1. By Corollary 2.6, it will
be enough to show VC[n] holds for ∆r (1 ≤r ≤n). But under the
assumption of (3) (with n = r), we know that VC[r] holds for ∆r.
Then, by Proposition 2.7, (b), we know VC[n] also holds for ∆r.
✷
Next, we show that, to study HVC, equivalently VC or JC, the
Laplace operators are not the only choices, even though they are the
best in many situations.
Proposition 2.10. Let {nk | k ≥1} be a strictly increasing sequence of
positive integers and {Λnk | k ≥1} a sequence of diﬀerential operators
in D2 with rank (Λnk) = nk (k ≥1). Suppose that, for any k ≥1,
HVC[Nk] holds for Λnk for some Nk ≥nk. Then, the equivalent state-
ments in Theorem 2.9 hold.


## Page 11


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
11
Proof:
We show, under the assumption in the proposition, the state-
ment (2) in Theorem 2.9 holds, i.e. for any n ≥1, HVC[n] (n ≥1)
holds for the Laplace operator ∆n ∈D2[n].
For any ﬁxed n ≥1, let k ≥1 such that nk ≥n.
If Nk = nk,
then, by Proposition 2.7, (a), we have HVC[n] (n ≥1) holds for the
Laplace operator ∆n ∈D2[n]. If Nk > nk, then, by Proposition 2.8, we
know VC[nk] (hence also HVC[nk]) holds for ∆nk. Since nk ≥n, by
Proposition 2.7, (a) again, we know HVC[n] does hold for the Laplace
operator ∆n.
✷
Example 2.11. Besides the Laplace operators, by Proposition 2.10, the
following sequences of diﬀerential operators are also among the most
natural choices.
(1) Let nk = k (k ≥2) (or any other strictly increasing sequence of
positive integers). Let Λnk be the “Laplace operator” with respect
to the standard Minkowski metric of Rnk. Namely, choose
Λk = D2
1 −
k
X
i=2
D2
i .
(2.9)
(2) Choose nk = 2k (k ≥1) (or any other strictly increasing se-
quence of positive even numbers). Let Λ2k be the “Laplace op-
erator” with respect to the standard symplectic metric on R2k,
i.e. choose
Λ2k =
k
X
i=1
DiDi+k.
(2.10)
(3) We may also choose the complex Laplace operators ∆¯∂instead of
the real Laplace operator ∆. More precisely, we choose nk = 2k
for any k ≥1 and view the polynomial algebra of wi (1 ≤i ≤
2k) over C as the polynomial algebra C[zi, ¯zi | 1 ≤i ≤k] by
setting zi = wi + √−1 wi+k for any 1 ≤i ≤k. Then, for any
k ≥1, we set
Λk = ∆¯∂,k :=
k
X
i=1
∂2
∂zi∂¯zi
.
(2.11)
(4) More generally, we may also choose Λk = ∆Ank, where nk ∈N
and Ank ∈SM(nk, C) (not necessarily invertible) (k ≥1) with
strictly increasing ranks.


## Page 12


12
WENHUA ZHAO
3. Some Properties of ∆A-Nilpotent Polynomials
As pointed earlier in Section 1 (see page 2), for the Laplace operators
∆n (n ≥1), the notion ∆n-nilpotency coincides with the notion of Hes-
sian nilpotency. HN (Hessian nilpotent) polynomials or formal power
series, their associated symmetric polynomial maps and Conjecture 1.1
have been studied in [BE2], [BE3], [Z1]–[Z3] and [EZ]. In this section,
we apply Corollary 2.3, Lemma 2.5 and also Lefschetz’s principle to
transform some results obtained in the references above to certain re-
sults on Λ-nilpotent (Λ ∈D2) polynomials or formal power series, VC
for Λ and also associated polynomial maps. Another purpose of this
section is to give a short survey on some results on HN polynomials and
Conjecture 1.1 in the more general setting of Λ-nilpotent polynomials
and VC for diﬀerential operators Λ ∈D2.
In subsection 3.1, we transform some results in [Z1] and [Z2] to the
setting of Λ-nilpotent polynomials for Λ ∈D2[n] of full rank (see Theo-
rems 3.1–3.3). In subsection 3.2, we derive four criteria for Λ-nilpotency
(Λ ∈D2) (see Propositions 3.4, 3.6, 3.7 and 3.10). The criteria in this
subsection are transformations of the criteria of Hessian nilpotency de-
rived in [Z2] and [Z3].
In subsection 3.3, we transform some results in [BCW], [Wa] and
[Y] on JC; [BE2] and [BE3] on symmetric polynomial maps; [Z2], [Z3]
and [EZ] on HN polynomials to certain results on VC for Λ ∈D2.
In subsection 3.4, we consider VC for high order diﬀerential operators
with constant coeﬃcients. We mainly focus on the diﬀerential operators
Λ = Da (a ∈Nn). Surprisingly, VC for these operators is equivalent
to a conjecture (see Conjecture 3.21) on Laurent polynomials, which
is similar to a non-trivial theorem (see Theorem 3.20) ﬁrst conjectured
by O. Mathieu [Ma] and later proved by J. Duistermaat and W. van
der Kallen [DK].
3.1. Associated Polynomial Maps and PDEs. Once and for all in
this section, we ﬁx any n ≥1 and A ∈SM(n, C) of rank 1 ≤r ≤n. We
use z and D, unlike we did before, to denote the n-tuples (z1, z2, . . . , zn)
and (D1, D2, . . . , Dn), respectively. We deﬁne a C-bilinear form ⟨·, ·⟩A
by setting ⟨u, v⟩A := uτAv for any u, v ∈Cn. Note that, when A =
In×n, the bilinear form deﬁned above is just the standard C-bilinear
form of Cn, which we also denote by ⟨·, ·⟩.
By Lemma 2.2, we may write A as in Eq. (2.8). For any P(z) ∈¯
An,
we set
eP(z) = Φ−1
U P(z) = P(Uz).
(3.1)


## Page 13


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
13
Note that, by Lemma 2.1, (b), we have Ψ−1
U (∆A) = ∆r. By Lemma
2.5, (a), P(z) is ∆A-nilpotent iﬀeP(z) is ∆r-nilpotent.
Theorem 3.1. Let t be a central parameter. For any P(z) ∈An with
o(P(z)) ≥2 and A ∈SGL(n, C), set FA,t(z):= z −tA∇P(z). Then
(a) there exists a unique QA,t(z) ∈C[t][[z]] such that the formal
inverse map GA,t(z) of FA,t(z) is given by
GA,t(z) = z + tA∇QA,t(z).
(3.2)
(b) The QA,t(z) ∈C[t][[z]] in (a) is the unique formal power series
solution of the following Cauchy problem:
(∂QA,t
∂t (z) = 1
2 ⟨∇QA,t, ∇QA,t⟩A,
QA,t=0(z) = P(z).
(3.3)
Proof:
Let eP as given in Eq. (3.1) and set
eFA,t(z) = z −t∇eP(z).
(3.4)
By Theorem 3.6 in [Z1], we know the formal inverse map eGA,t(z) of
eFA,t(z) is given by
eGA,t(z) = z + t∇eQA,t(z),
(3.5)
where eQA,t(z) ∈C[t][[z]] is the unique formal power series solution of
the following Cauchy problem:
(
∂e
QA,t
∂t (z) = 1
2 ⟨∇eQA,t, ∇eQA,t⟩,
eQA,t=0(z) = eP(z).
(3.6)
From the fact that ∇eP(z) = (Uτ∇P)(Uz), it is easy to check that
(ΦU ◦eFA,t ◦Φ−1
U )(z) = z −tA∇P(z) = FA,t(z),
(3.7)
which is the formal inverse map of
(ΦU ◦eGA,t ◦Φ−1
U )(z) = z + t(U∇eQA,t)(U−1z).
(3.8)
Set
QA,t(z):= eQA,t(U−1z).
(3.9)
Then we have
∇QA,t(z) = (Uτ)−1(∇eQA,t)(U−1z),
Uτ∇QA,t(z) = (∇eQA,t)(U−1z),
(3.10)


## Page 14


14
WENHUA ZHAO
Multiplying U to the both sides of the equation above and noticing
that A = UUτ by Eq. (2.8) since A is of full rank, we get
A∇QA,t(z) = (U∇eQA,t)(U−1z).
(3.11)
Then, combining Eq. (3.8) and the equation above, we see the formal
inverse GA,t(z) of FA,t(z) is given by
GA,t(z) = (ΦU ◦eGA,t ◦Φ−1
U )(z) = z + tA∇QA,t(z).
(3.12)
Applying ΦU to Eq. (3.6) and by Eqs. (3.9), (3.10), we see that QA,t(z) is
the unique formal power series solution of the Cauchy problem Eq. (3.3).
✷
By applying the linear automorphism ΦU of C[[z]] and employing a
similar argument as in the proof of Theorem 3.1 above, we can gen-
eralize Theorems 3.1 and 3.4 in [Z2] to the following theorem on ∆A-
nilpotent (A ∈SGL(n, C)) formal power series.
Theorem 3.2. Let A, P(z) and QA,t(z) as in Theorem 3.1. We further
assume P(z) is ∆A-nilpotent. Then,
(a) QA,t(z) is the unique formal power series solution of the follow-
ing Cauchy problem:
(∂QA,t
∂t (z) = 1
4 ∆AQ2
A,t,
QA,t=0(z) = P(z).
(3.13)
(b) For any k ≥1, we have
Qk
A,t(z) =
X
m≥1
tm−1
2mm!(m + k)! ∆m
AP m+1(z).
(3.14)
Applying the same strategy to Theorem 3.2 in [Z2], we get the fol-
lowing theorem.
Theorem 3.3. Let A, P(z) and QA,t(z) as in Theorem 3.2. For any
non-zero s ∈C, set
Vt,s(z):= exp(sQt(z)) =
∞
X
k=0
skQk
t (z)
k!
.
Then, Vt,s(z) is the unique formal power series solution of the following
Cauchy problem of the heat-like equation:
(
∂Vt,s
∂t (z) =
1
2s ∆AVt,s(z),
Ut=0,s(z) = exp(sP(z)).
(3.15)


## Page 15


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
15
3.2. Some Criteria of ∆A-Nilpotency. In this subsection, with the
notation and remarks ﬁxed in the previous subsection in mind, we
apply the linear automorphism ΦU to transform some criteria of Hessian
nilpotency derived in [Z2] and [Z3] to criteria of ∆A-nilpotency (A ∈
SM(n, C)) (see Proposition 3.4, 3.6, 3.7 and 3.10 below).
Proposition 3.4. Let A be given as in Eq. (2.8). Then, for any P(z) ∈
An, it is ∆A-nilpotent iﬀthe submatrix of Uτ(Hes P) U consisting of
the ﬁrst r rows and r columns is nilpotent.
In particular, when r = n, i.e. ∆A is full rank, any P(z) ∈D2[n] is
∆A-nilpotent iﬀUτ(Hes P) U is nilpotent.
Proof:
Let eP(z) be as in Eq. (3.1). Then, as pointed earlier, P(z)
is ∆A-nilpotent iﬀeP(z) is ∆r-nilpotent.
If r = n, then by Theorem 1.2 , eP(z) is ∆r-nilpotent iﬀHes eP(z) is
nilpotent. But note that in general we have
Hes eP(z) = Hes P(Uz) = Uτ[(Hes P)(Uz)] U.
(3.16)
Therefore, Hes eP(z) is nilpotent iﬀUτ[(Hes P)(Uz)] U is nilpotent iﬀ,
with z replaced by U−1z, Uτ[(Hes P)(z)] U is nilpotent.
Hence the
proposition follows in this case.
Assume r < n.
We view Ar as a subalgebra of the polynomial
algebra K[z1, . . . , zr], where K is the rational ﬁeld C(zr+1, . . . , zn). By
Theorem 1.2 and Lefschetz’s principle, we know that eP is ∆r-nilpotent
iﬀthe matrix

∂2 eP
∂zi∂zj

1≤i,j≤r is nilpotent.
Note that the matrix

∂2 e
P
∂zi∂zj

1≤i,j≤r is the submatrix of Hes eP(z) con-
sisting of the ﬁrst r rows and r columns. By Eq. (3.16), it is also the sub-
matrix of Uτ[Hes P(Uz)] U consisting of the ﬁrst r rows and r columns.
Replacing z by U−1z in the submatrix above, we see

∂2 eP
∂zi∂zj

1≤i,j≤r is
nilpotent iﬀthe submatrix of Uτ[Hes P(z)] U consisting of the ﬁrst r
rows and r columns is nilpotent. Hence the proposition follows.
✷
Note that, for any homogeneous quadratic polynomial P(z) = zτBz
with B ∈SM(n, C), we have Hes P(z) = 2B. Then, by Proposition
3.4, we immediately have the following corollary.
Corollary 3.5. For any homogeneous quadratic polynomial P(z) =
zτBz with B ∈SM(n, C), it is ∆A-nilpotent iﬀthe submatrix of
UτB U consisting of the ﬁrst r rows and r columns is nilpotent.


## Page 16


16
WENHUA ZHAO
Proposition 3.6. Let A be given as in Eq. (2.8). Then, for any P(z) ∈
¯An with o(P(z)) ≥2, P(z) is ∆A-nilpotent iﬀ∆m
AP m = 0 for any
1 ≤m ≤r.
Proof:
Again, we let eP(z) be as in Eq. (3.1) and note that P(z) is
∆A-nilpotent iﬀeP(z) is ∆r-nilpotent.
Since r ≤n. We view Ar as a subalgebra of the polynomial algebra
K[z1, . . . , zr], where K is the rational ﬁeld C(zr+1, . . . , zn). By Theorem
1.2 and Lefschetz’s principle (if r < n), we have eP(z) is ∆r-nilpotent
iﬀ∆m
r eP m = 0 for any 1 ≤m ≤r. On the other hand, by Eqs. (2.6)
and (2.7), we have ΦU

∆m
r eP m
= ∆m
AP m for any m ≥1. Since ΦU is
an automorphism of An, we have that, ∆m
r eP m = 0 for any 1 ≤m ≤r
iﬀ∆m
AP m = 0 for any 1 ≤m ≤r. Therefore, eP(z) is ∆A-nilpotent iﬀ
∆m
AP m = 0 for any 1 ≤m ≤r. Hence the proposition follows.
✷
Proposition 3.7. For any A ∈SGL(n, C) and any homogeneous
P(z) ∈An of degree d ≥2, we have, P(z) is ∆A-nilpotent iﬀ, for
any β ∈C, (βD)d−2P(z) is Λ-nilpotent, where βD := ⟨β, D⟩.
Proof:
Let A be given as in Eq. (2.8) and eP(z) as in Eq. (3.1). Note
that, Ψ−1
U (∆A) = ∆n (for ∆A is of full rank), and P(z) is ∆A-nilpotent
iﬀeP(z) is ∆n-nilpotent.
Since eP is also homogeneous of degree d ≥2, by Theorem 1.2 in
[Z3], we know that, eP(z) is ∆n-nilpotent iﬀ, for any β ∈Cn, βd−2
D
eP is
∆n-nilpotent. Note that, from Lemma 2.1, (b), we have
ΨU(βD) = ⟨β, UτD⟩
= ⟨Uβ, D⟩
= (Uβ)D,
and
ΦU(βd−2
D
eP) = ΨU(βD)d−2ΦU( eP) = (Uβ)d−2
D P.
(3.17)
Therefore, by Lemma 2.5, (a), βd−2
D
eP is ∆n-nilpotent iﬀ(Uβ)d−2
D P is
∆A-nilpotent since ΨU(∆n) = ∆A. Combining all equivalences above,
we have P(z) is ∆n-nilpotent iﬀ, for any β ∈Cn, (Uβ)d−2
D P is ∆A-
nilpotent.
Since U is invertible, when β runs over Cn so does Uβ.
Therefore the proposition follows.
✷
Let {ei | 1 ≤i ≤n} be the standard basis of Cn. Applying the propo-
sition above to β = ei (1 ≤i ≤n), we have the following corollary.


## Page 17


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
17
Corollary 3.8. For any homogeneous ∆A-nilpotent polynomial P(z) ∈
An of degree d ≥2, Dd−2
i
P(z) (1 ≤i ≤n) are also ∆A-nilpotent.
We think that Proposition 3.7 and Corollary 3.8 are interesting be-
cause, due to Corollary 3.5, it is much easier to decide whether a qua-
dratic form is ∆A-nilpotent or not.
To state the next criterion, we need ﬁx the following notation.
For any A ∈SGL(n, C), we let XA(Cn) be the set of isotropic vectors
u ∈Cn with respect to the C-bilinear form ⟨·, ·⟩A. When A = In×n, we
also denote XA(Cn) simply by of X(Cn).
For any β ∈Cn, we set hα(z) := ⟨α, z⟩. Then, by applying ΦU to
a well-known theorem on classical harmonic polynomials, which is the
following theorem for A = In×n (see, for example, [He] and [T]), we
have the following result on homogeneous ∆A-nilpotent polynomials.
Theorem 3.9. Let P be any homogeneous polynomial of degree d ≥2
such that ∆AP = 0. We have
P(z) =
k
X
i=1
hd
αi(z)
(3.18)
for some k ≥1 and αi ∈XA(Cn) (1 ≤i ≤k).
Next, for any homogeneous polynomial P(z) of degree d ≥2, we
introduce the following matrices:
ΞP := (⟨αi, αj⟩A)k×k ,
(3.19)
ΩP :=

⟨αi, αj⟩A hd−2
αj (z)

k×k .
(3.20)
Then, by applying ΦU to Proposition 5.3 in [Z2] (the details will
be omitted here), we have the following criterion of ∆A-nilpotency for
homogeneous polynomials.
Proposition 3.10. Let P(z) be as given in Eq. (3.18). Then P(z) is
∆A-nilpotent iﬀthe matrix ΩP is nilpotent.
One simple remark on the criterion above is as follows.
Let B be the k × k diagonal matrix with hαi(z) (1 ≤i ≤k) as the
ith diagonal entry. For any 1 ≤j ≤k, set
ΩP ;j := BjΞPBd−2−j = (hj
αi⟨αi, αj⟩hd−2−j
αj
).
(3.21)
Then, by repeatedly applying the fact that, for any C, D ∈M(k, C),
CD is nilpotent iﬀso is DC, it is easy to see that Proposition 3.10 can
also be re-stated as follows.


## Page 18


18
WENHUA ZHAO
Corollary 3.11. Let P(z) be given by Eq. (3.18) with d ≥2. Then,
for any 1 ≤j ≤d −2 and m ≥1, P(z) is ∆A-nilpotent iﬀthe matrix
ΩP ;j is nilpotent.
Note that, when d is even, we may choose j = (d −2)/2. So P is
∆A-nilpotent iﬀthe symmetric matrix
ΩP ;(d−2)/2 = (h(d−2)/2
αi
⟨αi, αj⟩Ah(d−2)/2
αj
)
(3.22)
is nilpotent.
3.3. Some Results on the Vanishing Conjecture of the 2nd
Order Homogeneous Diﬀerential Operators with Constants
Coeﬃcients. In this subsection, we transform some known results of
VC for the Laplace operators ∆n (n ≥1) to certain results on VC for
∆A (A ∈SGL(n, C)).
First, by Wang’s theorem [Wa], we know that JC holds for any
polynomial maps F(z) with deg F ≤2.
Hence, JC also holds for
symmetric polynomials F(z) = z −∇P(z) with P(z) ∈C[z] of degree
d ≤3. By the equivalence of JC and VC for the Laplace operators
established in [Z2], we know VC holds if Λ = ∆n and P(z) is a HN
polynomials of degree d ≤3. Then, applying the linear automorphism
ΦU, we have the following proposition.
Theorem 3.12. For any A ∈SGL(n, C) and ∆A-nilpotent P(z) ∈An
(not necessarily homogeneous) of degree d ≤3, we have ΛmP m+1 = 0
when m >> 0, i.e. VC[n] holds for Λ and P(z).
Applying the classical homogeneous reduction on JC (see [BCW],
[Y]) to associated symmetric maps, we know that, to show VC for ∆n
(n ≥1), it will be enough to consider only homogeneous HN polyno-
mials of degree 4. Therefore, by applying the linear automorphism ΦU
of An, we have the same reduction for HVC too.
Theorem 3.13. To study HVC in general, it will be enough to con-
sider only homogeneous P(z) ∈A of degree 4.
In [BE2] and [BE3] it has been shown that JC holds for symmetric
maps F(z) = z−∇P(z) (P(z) ∈An) if the number of variables n is less
or equal to 4, or n = 5 and P(z) is homogeneous. By the equivalence of
JC for symmetric polynomial maps and VC for the Laplace operators
established in [Z2], and Proposition 2.8 and Corollary 2.6, we have the
following results on VC and HVC.
Theorem 3.14. (a) For any n ≥1, VC[n] holds for any Λ ∈D2 of
rank 1 ≤r ≤4.
(b) HVC[5] holds for any Λ ∈D2[5].


## Page 19


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
19
Note that the following vanishing properties of HN formal power
series have been proved in Theorem 6.2 in [Z2] for the Laplace operators
∆n (n ≥1). By applying the linear automorphism ΦU, one can show
it also holds for any Λ-nilpotent (Λ ∈D2) formal power series.
Theorem 3.15. Let Λ ∈D2[n] and P(z) ∈¯An be Λ-nilpotent with
o(P) ≥2. The following statements are equivalent.
(1) ΛmP m+1 = 0 when m >> 0.
(2) There exists k0 ≥1 such that ΛmP m+k0 = 0 when m >> 0.
(3) For any ﬁxed k ≥1, ΛmP m+k = 0 when m >> 0.
By applying the linear automorphism ΦU, one can transform Theo-
rem 1.5 in [EZ] on VC of the Laplace operators to the following result
on VC of Λ ∈D2.
Theorem 3.16. Let Λ ∈D2[n] and P(z) ∈¯An any Λ-nilpotent poly-
nomial with o(P) ≥2. Then VC holds for Λ and P(z) iﬀ, for any
g(z) ∈An, we have Λm(g(z)P m) = 0 when m >> 0.
In [EZ], the following theorem has also been proved for Λ = ∆n.
Next we show it is also true in general.
Theorem 3.17. Let A ∈SGL(n, C) and P(z) ∈An a homogeneous
∆A-nilpotent polynomial with deg P ≥2.
Assume that σA−1(z) :=
zτA−1z and the partial derivatives ∂P
∂zi (1 ≤i ≤n) have no non-zero
common zeros. Then HVC[n] holds for ∆A and P(z).
In particular, if the projective subvariety determined by the ideal
⟨P(z)⟩of An is regular, HVC[n] holds for ∆A and P(z).
Proof:
Let eP as given in Eq. (3.1). By Theorem 1.2 in [EZ], we know
that, when σ2(z):= Pn
i=1 z2
i and the partial derivatives ∂eP
∂zi (1 ≤i ≤n)
have no non-zero common zeros, HVC[n] holds for ∆n and eP. Then,
by Lemma 2.5, (b), HVC[n] also holds for ∆A and P.
But, on the other hand, since U is invertible and, for any 1 ≤i ≤n,
∂eP
∂zi
=
n
X
j=1
uji
∂P
∂zj
(Uz),
σ2(z) and ∂eP
∂zi (1 ≤i ≤n) have no non-zero common zeros iﬀσ2(z) and
∂P
∂zi(Uz) (1 ≤i ≤n) have no non-zero common zeros, and iﬀ, with z
replaced by U−1z, σ2(U−1z) = σA−1(z) and ∂P
∂zi(z) (1 ≤i ≤n) have no
non-zero common zeros. Therefore, the theorem holds.
✷


## Page 20


20
WENHUA ZHAO
3.4. The Vanishing Conjecture for Higher Order Diﬀerential
Operators with Constant Coeﬃcients. Even though the most in-
teresting case of VC is for Λ ∈D2, at least when JC is concerned,
the case of VC for higher order diﬀerential operators with constant
coeﬃcients is also interesting and non-trivial. In this subsection, we
mainly discuss VC for the diﬀerential operators Da (a ∈Nn). At the
end of this subsection, we also recall a result proved in [Z3] which says
that, when the base ﬁeld has characteristic p > 0, VC, even under a
weaker condition, actually holds for any diﬀerential operator Λ (not
necessarily with constant coeﬃcients).
Let βj ∈Cn (1 ≤j ≤ℓ) be linearly independent and set δj := ⟨βj, D⟩.
Let Λ = Qℓ
j=1 δai
j with aj ≥1 (1 ≤j ≤ℓ).
When ℓ= 1, VC for Λ can be proved easily as follows.
Proposition 3.18. Let δ ∈D1[z] and Λ = δk for some k ≥1. Then
(a) A polynomial P(z) is Λ-nilpotent if (and only if) ΛP = 0.
(b) VC holds for Λ.
Proof:
Applying a change of variables, if necessary, we may assume
δ = D1 and Λ = Dk
1.
Let P(z) ∈C[z] such that ΛP(z) = Dk
1P(z) = 0. Let d be the degree
of P(z) in z1. From the equation above, we have k > d. Therefore, for
any m ≥1, we have km > dm which implies ΛmP(z)m = Dkm
1 P m(z) =
0. Hence, we have (a).
To show (b), let P(z) be a Λ-nilpotent polynomial. By the same
notation and argument above, we have k > d. Choose a positive integer
N >
d
k−d. Then, for any m ≥N, we have m >
d
k−d, which is equivalent
to (m + 1)d < km. Hence we have ΛmP(z)m+1 = Dkm
1 P m+1(z) = 0.
✷
In particular, when k = 1 in the proposition above, we have the
following corollary.
Corollary 3.19. VC holds for any diﬀerential operator Λ ∈D1.
Next we consider the case ℓ≥2. Note that, when ℓ= 2 and a1 =
a2 = 1. Λ ∈D2 and has rank 2. Then, by Theorem 3.14, we know VC
holds for Λ.
Besides the case above, VC for Λ = Qℓ
j=1 δai
j
with ℓ≥2 seems to
be non-trivial at all. Actually, we will show below, it is equivalent to a
conjecture (see Conjecture 3.21) on Laurent polynomials.
First, by applying a change of variables, if necessary, we may (and
will) assume Λ = Da with a ∈(N+)ℓ. Secondly, note that, for any


## Page 21


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
21
b ∈Nn and h(z) ∈C[z], Dbh(z) = 0 iﬀthe holomorphic part of the
Laurent polynomial z−bh(z) is zero.
Now we ﬁx a P(z) ∈C[z] and set f(z):= z−aP(z). With the obser-
vation above, it is easy to see that, P(z) is Da-nilpotent iﬀthe holo-
morphic parts of the Laurent polynomials f m(z) (m ≥1) are all zero;
and VC holds for Λ and P(z) iﬀthe holomorphic part of P(z)f m(z)
is zero when m >> 0. Therefore, VC for Da can be restated as follows:
Re-Stated VC for Λ = Da: Let P(z) ∈An and f(z) as above.
Suppose that, for any m ≥1, the holomorphic part of the Laurent poly-
nomial f m(z) is zero, then the holomorphic part of P(z)f m(z) equals
to zero when m >> 0.
Note that the re-stated VC above is very similar to the following
non-trivial theorem which was ﬁrst conjectured by O. Mathieu [Ma]
and later proved by J. Duistermaat and W. van der Kallen [DK].
Theorem 3.20. Let f and g be Laurent polynomials in z. Assume that,
for any m ≥1, the constant term of f m is zero. Then the constant term
gf m equals to zero when m >> 0.
Note that, Mathieu’s conjecture [Ma] is a conjecture on all real com-
pact Lie groups G, which is also mainly motivated by JC. The the-
orem above is the special case of Mathieu’s conjecture when G the
n-dimensional real torus. For other compact real Lie groups, Math-
ieu’s conjecture seems to be still wide open.
Motivated by Theorem 3.20, the above re-stated VC for Λ = Da
and also the result on VC in Theorem 3.16, we would like to propose
the following conjecture on Laurent polynomials.
Conjecture 3.21. Let f and g be Laurent polynomials in z. Assume
that, for any m ≥1, the holomorphic part of f m is zero. Then the
holomorphic part gf m equals to zero when m >> 0.
Note that, a positive answer to the conjecture above will imply VC
for Λ = Da (a ∈Nn) by simply choosing g(z) to be P(z).
Finally let us to point out that, it is well-known that JC does not
hold over ﬁelds of ﬁnite characteristic (see [BCW], for example), but,
by Proposition 5.3 in [Z3], the situation for VC over ﬁelds of ﬁnite
characteristic is dramatically diﬀerent even though it is equivalent to
JC over the complex ﬁeld C.
Proposition 3.22. Let k be a ﬁeld of char. p > 0 and Λ any diﬀerential
operator of k[z]. Let f ∈k[[z]]. Assume that, for any 1 ≤m ≤p −1,


## Page 22


22
WENHUA ZHAO
there exists Nm > 0 such that ΛNmf m = 0. Then, Λmf m+1 = 0 when
m >> 0.
From the proposition above, we immediately have the following corol-
lary.
Corollary 3.23. Let k be a ﬁeld of char. p > 0. Then
(a) VC holds for any diﬀerential operator Λ of k[z].
(b) If Λ strictly decreases the degree of polynomials. Then, for any
polynomial f ∈k[z] (not necessarily Λ-nilpotent), we have Λmf m+1 = 0
when m >> 0.
4. A Remark on Λ-Nilpotent Polynomials and Classical
Orthogonal Polynomials
In this section, we ﬁrst in subsection 4.1 consider the “formal” con-
nection between Λ-nilpotent polynomials or formal power series and
classical orthogonal polynomials, which has been discussed in Section
1 (see page 4). We then in subsection 4.2 transform the isotropic prop-
erties of homogeneous HN polynomials proved in [Z2] to isotropic prop-
erties of homogeneous ∆A-nilpotent (A ∈SGL(n, C)) polynomials (see
Theorem 4.10 and Corollary 4.11). Note that, as pointed in Section
1, the isotropic results in subsection 4.2 can be understood as some
natural consequences of the connection of Λ-nilpotent polynomials and
classical orthogonal polynomials discussed in subsection 4.1.
4.1. Some Classical Orthogonal Polynomials. First, let us recall
the deﬁnition of classical orthogonal polynomials.
Note that, to be
consistent with the tradition for orthogonal polynomials, we will in
this subsection use x = (x1, x2, . . . , xn) instead of z = (z1, z2, . . . , zn)
to denote free commutative variables.
Deﬁnition 4.1. Let B be an open set of Rn and w(x) a real valued
function deﬁned over B such that w(x) ≥0 for any x ∈B and 0 <
R
B w(x)dx < ∞. A sequence of polynomials {fm(x) | m ∈Nn} is said
to be orthogonal over B if
(1) deg fm = |m| for any m ∈Nn.
(2)
R
B fm(x)fk(x)w(x) dx = 0 for any m ̸= k ∈Nn.
The function w(x) is called the weight function.
When the open
set B ⊂Rn and w(x) are clear in the context, we simply call the
polynomials fm(x) (m ∈Nn) in the deﬁnition above orthogonal poly-
nomials. If the orthogonal polynomials fm(x) (m ∈Nn) also satisfy
R
B f 2
m(x)w(x)dx = 1 for any m ∈Nn, we call fm(x) (m ∈Nn) or-
thonormal polynomials. Note that, in the one dimensional case w(x)


## Page 23


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
23
determines orthogonal polynomials over B up to multiplicative con-
stants, i.e. if fm(x) (m ≥0) are orthogonal polynomials as in Deﬁ-
nition 4.1, then, for any am ∈R× (m ≥0), amfm (m ≥0) are also
orthogonal over B with respect to the weight function w(x).
The most natural way to construct orthogonal or orthonormal se-
quences is: ﬁrst to list all monomials in an order such that the degrees
of monomials are non-decreasing; and then to apply Gram-Schmidt
procedure to orthogonalize or orthonormalize the sequence of mono-
mials. But, surprisingly, most of classical orthogonal polynomials can
also be obtained by the so-called Rodrigues’ formulas.
We ﬁrst consider orthogonal polynomials in one variable.
Rodrigues’ formula: Let fm(x) (m ≥0) be the orthogonal polyno-
mials as in Deﬁnition 4.1. Then, there exist a function g(x) deﬁned
over B and non-zero constants cm ∈R (m ≥0) such that
fm(x) = cmw(x)−1 dm
dxm(w(x)gm(x)).
(4.1)
Let P(x):= g(x) and Λ:= w(x)−1   d
dx

w(x), where, throughout this
paper any polynomial or function appearing in a (diﬀerential) operator
always means the multiplication operator by the polynomial or function
itself. Then, by Rodrigues’ formula above, we see that the orthogonal
polynomials {fm(x) | m ≥0} have the form
fm(x) = cmΛmP m(x),
(4.2)
for any m ≥0.
In other words, all orthogonal polynomials in one variable, up to
multiplicative constants, has the form {ΛmP m | m ≥0} for a single
diﬀerential operator Λ and a single function P(x).
Next we consider some of the most well-known classical orthonor-
mal polynomials in one variable. For more details on these orthogonal
polynomials, see [Sz], [AS], [DX].
Example 4.2. (Hermite Polynomials)
(a) B = R and the weight function w(x) = e−x2.
(b) Rodrigues’ formula:
Hm(x) = (−1)mex2( d
dx)me−x2.


## Page 24


24
WENHUA ZHAO
(c) Diﬀerential operator Λ and polynomial P(x):
(
Λ = ex2( d
dx)e−x2 =
d
dx −2x,
P(x) = 1,
(d) Hermite polynomials in terms of Λ and P(x):
Hm(x) = (−1)m ΛmP m(x).
Example 4.3. (Laguerre Polynomials)
(a) B = R+ and w(x) = xαe−x (α > −1).
(b) Rodrigues’ formula:
Lα
m(x) = 1
m!x−αex( d
dx)m(xm+αe−x).
(c) Diﬀerential operator Λ and polynomial P(x):
(
Λα = x−αex( d
dx)(e−xxα) =
d
dx + (αx−1 −1),
P(x) = x,
(d) Laguerre polynomials in terms of Λ and P(x):
Lm(x) = 1
m! ΛmP m(x).
Example 4.4. (Jacobi Polynomials)
(a) B = (−1, 1) and w(x) = (1 −x)α(1 + x)β, where α, β > −1.
(b) Rodrigues’ formula:
P α,β
m (x) = (−1)m
2mm! (1 −x)−α(1 + x)−β( d
dx)m(1 −x)α+m(1 + x)β+m.
(c) Diﬀerential operator Λ and polynomial P(x):
Λ = (1 −x)−α(1 + x)−β( d
dx)(1 −x)α(1 + x)β
= d
dx −α(1 −x)−1 + β(1 + x)−1,
and
P(x) = 1 −x2.
(d) Laguerre polynomials in terms of Λ and P(x):
P α,β
m (x) = (−1)m
2mm! ΛmP m(x).
A very important special family of Jacobi polynomials are the Gegen-
bauer polynomials which are obtained by setting α = β = λ −1/2 for
some λ > −1/2. Gegenbauer polynomials are also called ultraspherical
polynomials in the literature.


## Page 25


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
25
Example 4.5. (Gegenbauer Polynomials)
(a) B = (−1, 1) and w(x) = (1 −x2)λ−1/2, where λ > −1/2.
(b) Rodrigues’ formula:
P λ
m(x) =
(−1)m
2m(λ + 1/2)m
(1 −x2)1/2−λ( d
dx)m(1 −x2)m+λ−1/2.
where, for any c ∈R and k ∈N, (c)k = c(c + 1) · · · (c + k −1).
(c) Diﬀerential operator Λ and polynomial P(x):
Λ = (1 −x2)1/2−λ( d
dx)(1 −x2)λ−1/2
(4.3)
= d
dx −(2λ −1) x
(1 −x2) ,
and
P(x) = 1 −x2.
(d) Laguerre polynomials in terms of Λ and P(x):
P λ
m(x) =
(−1)m
2m(λ + 1/2)m
ΛmP m(x).
Note that, for the special cases with λ = 0, 1, 1/2, the Gegenbauer
Polynomials P λ
m(x) are called the Chebyshev polynomial of the ﬁrst
kind, the second kind and Legendre polynomials, respectively. Hence
all these classical orthogonal polynomials also have the form of ΛmP m
(m ≥0) up to some scalar multiple constants cm with P(x) = 1 −x2
and the corresponding special forms of the diﬀerential operator Λ in
Eq. (4.3).
Remark 4.6. Actually, the Gegenbauer polynomials are more closely
and directly related with VC in some diﬀerent ways. See [Z4] for more
discussions on connections of the Gegenbauer polynomials with VC.
Next, we consider some classical orthogonal polynomials in several
variables.
We will see that they can also be obtained from certain
sequences of the form {ΛmP m | m ≥0} in a slightly modiﬁed way. One
remark is that, unlike the one-variable case, orthogonal polynomials
in several variables up to multiplicative constants are not uniquely
determined by weight functions.
The ﬁrst family of classical orthogonal polynomials in several vari-
ables can be constructed by taking Cartesian products of orthogonal
polynomials in one variable as follows.


## Page 26


26
WENHUA ZHAO
Suppose {fm | m ≥0} is a sequence of orthogonal polynomials in one
variable, say as given in Deﬁnition 4.1. We ﬁx any n ≥2 and set
W(x):=
n
Y
i=1
w(xi),
(4.4)
fm(x):=
n
Y
i=1
fmi(xi),
(4.5)
for any x ∈B×n and m ∈Nn.
Then it is easy to see that the sequence {fm(x) | m ∈Nn} are orthog-
onal polynomials over B×n with respect to the weight function W(x)
deﬁned above.
Note that, by applying the construction above to the classical one-
variable orthogonal polynomials discussed in the previous examples,
one gets the classical multiple Hermite Polynomials, multiple Laguerre
polynomials, multiple Jacobi polynomials and multiple Gegenbauer poly-
nomials, respectively.
To see that the multi-variable orthogonal polynomials constructed
above can be obtained from a sequence of the form {ΛmP m(x) | m ≥
0}, we suppose fm (m ≥0) have Rodrigues’ formula Eq. (4.1). Let
s = (s1, . . . , sn) be n central formal parameters and set
Λs:=W(x)−1
 n
X
i=1
si
∂
∂xi
!
W(x),
(4.6)
P(x):=
n
Y
i=1
g(xi).
(4.7)
Let Vm(x) (m ∈Nn) be the coeﬃcient of sm in Λ|m|
s P |m|(x). Then,
from Eqs. (4.1), (4.4)–(4.7), it is easy to check that, for any m ∈Nn,
we have
fm(x) = cm
m!
|m|! Vm(x),
(4.8)
where cm = Qn
i=1 cmi.
Therefore, we see that any multi-variable orthogonal polynomials
constructed as above from Cartesian products of one-variable orthogo-
nal polynomials can also be obtained from a single diﬀerential operator
Λs and a single function P(x) via the sequence {Λm
s P m | m ≥0}.
Remark 4.7. Note that, one can also take Cartesian products of dif-
ferent kinds of one-variable orthogonal polynomials to create more or-
thogonal polynomials in several variables. By a similar argument as


## Page 27


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
27
above, we see that all these multi-variable orthogonal polynomials can
also be obtained similarly from a single sequence {Λm
s P m | m ≥0}.
Next, we consider the following two examples of classical multi-
variable orthogonal polynomials which are not Cartesian products of
one-variable orthogonal polynomials.
Example 4.8. (Classical Orthogonal Polynomials over Unit
Balls)
(a) Choose B to be the open unit ball Bn of Rn and the weight func-
tion
Wµ(x) = (1 −||x||2)µ−1/2,
where ||x|| = Pn
i=1 x2
i and µ > 1/2.
(b) Rodrigues’ formula: For any m ∈Nn, set
Um(x):=
(−1)m(2µ)|m|
2|m|m!(µ + 1/2)|m|
∂|m|
∂xm1
1
· · · ∂xmn
n
(1 −||x||2)|m|+µ−1/2.
Then, by Proposition 2.2.5 in [DX], {Um(x) | m ∈Nn} are orthonormal
over Bn with respect to the weight function Wµ(x).
(c) Diﬀerential operator Λs and polynomial P(x): Let s = (s1, . . . , sn)
be n central formal parameters and set
Λs:=Wµ(x)−1
 n
X
i=1
si
∂
∂xi
!
Wµ(x),
P(x):=1 −||x||2.
Let Vm(x) (m ∈Nn) be the coeﬃcient of sm in Λ|m|
s P |m|(x). Then
from the Rodrigues type formula above, we have, for any m ∈Nn,
Um(x) =
(−1)|m|(2µ)|m|
2|m||m|!(µ + 1/2)|m|
Vm(x).
Therefore, the classical orthonormal polynomials {Um(x) | m ∈Nn}
over Bn can be obtained from a single diﬀerential operator Λs and P(x)
via the sequence {Λm
s P m | m ≥0}.
Example 4.9. (Classical Orthogonal Polynomials over Sim-
plices)
(a) Choose B to be the simplex
T n = {x ∈Rn |
n
X
i=1
xi < 1; x1, ..., xn > 0}


## Page 28


28
WENHUA ZHAO
in Rn and the weight function
Wκ(x) = xκ1
1 · · · xκn
n (1 −|x|1)κn+1−1/2,
(4.9)
where κi > −1/2 (1 ≤i ≤n + 1) and |x|1 = Pn
i=1 xi.
(b) Rodrigues’ formula: For any m ∈Nn, set
Um(x):= Wκ(x)−1
∂|m|
∂xm1
1
· · · ∂xmn
n
 Wκ(x)(1 −|x|1)|m|
.
Then, {Um(x) | m ∈Nn} are orthonormal over T n with respect to the
weight function Wκ(x). See Section 2.3.3 of [DX] for a proof of this
claim.
(c) Diﬀerential operator Λ and polynomial P(x): Let s = (s1, . . . , sn)
be n central formal parameters and set
Λs :=Wκ(x)−1
 n
X
i=1
si
∂
∂xi
!
Wκ(x),
P(x):=1 −|x|1.
Let Vm(x) (m ∈Nn) be the coeﬃcient of sm in Λ|m|
s P |m|(x). Then
from the Rodrigues type formula in (b), we have, for any m ∈Nn,
Um(x) = m!
|m|! Vm(x).
Therefore, the classical orthonormal polynomials {Um(x) | m ∈Nn}
over T n can be obtained from a single diﬀerential operator Λs and a
function P(x) via the sequence {Λm
s P m | m ≥0}.
4.2. The Isotropic Property of ∆A-Nilpotent Polynomials. As
discussed in Section 1, the “formal” connection of Λ-nilpotent polyno-
mials with classical orthogonal polynomials predicts that Λ-nilpotent
polynomials should be isotropic with respect to a certain C-bilinear
form of An. In this subsection, we show that, for diﬀerential operators
Λ = ∆A (A ∈SGL(n, C)), this is indeed the case for any homogeneous
Λ-nilpotent polynomials (see Theorem 4.10 and Corollaries 4.11, 4.12).
We ﬁx any n ≥1 and let z and D denote the n-tuples (z1, . . . , zn)
and (D1, D2, . . . , Dn), respectively. Let A ∈SGL(n, C) and deﬁne the
C-bilinear map
{·, ·}A : An × An →
An
(4.10)
(f, g)
→f(AD)g(z),
Furthermore, we also deﬁne a C-bilinear form
(·, ·)A : An × An →
C
(4.11)


## Page 29


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
29
(f, g)
→{f, g}A|z=0,
It is straightforward to check that the C-bilinear form deﬁned above
is symmetric and its restriction on the subspace of homogeneous poly-
nomials of any ﬁxed degree is non-singular. Note also that, for any
homogeneous polynomials f, g ∈An of the same degree, we have
{f, g}A = (f, g)A.
The main result of this subsection is the following theorem.
Theorem 4.10. Let A ∈SGL(n, C) and P(z) ∈An a homogeneous
∆A-nilpotent polynomial of degree d ≥3. Let I(P) be the ideal of An
generated by σA−1(z) := zτA−1z and ∂P
∂zi (1 ≤i ≤n). Then, for any
f(z) ∈I(P) and m ≥0, we have
{f, ∆m
AP m+1}A = f(AD) ∆m
AP m+1 = 0.
(4.12)
Note that, by Theorem 6.3 in [Z2], we know that the theorem does
hold when A = In and ∆A = ∆n.
Proof:
Note ﬁrst that, elements of An satisfying Eq. (4.12) do form
an ideal. Therefore, it will be enough to show σA−1(z) and ∂P
∂zi (1 ≤
i ≤n) satisfy Eq. (4.12). But Eq. (4.12) for σA−1(z) simply follows the
facts that σA−1(Az) = zτAz and σA−1(AD) = ∆A.
Secondly, by Lemma 2.2, we can write A = UUτ for some U = (uij) ∈
GL(n, C). Then, by Eq. (2.7), we have ΨU(∆n) = ∆A or Ψ−1
U (∆A) =
∆n. Let eP(z) := Φ−1
U (P) = P(Uz). Then by Lemma 2.5, (a), eP is a
homogeneous ∆n-nilpotent polynomial, and by Eq. (2.6), we also have
Φ−1
U (∆m
AP m+1) = ∆m
n eP m+1.
(4.13)
By Theorem 6.3 in [Z2], for any 1 ≤i ≤n and m ≥0, we have,
∂eP
∂zi
(D)

∆m
n eP m+1
= 0
Since
∂eP
∂zi
(z) =
n
X
k=1
uki
∂P
∂zk
(Uz),
we further have,
n
X
k=1
uki
∂P
∂zk
(UD)

∆m
n eP m+1
= 0.
Since U is invertible, for any 1 ≤i ≤n, we have
∂P
∂zi
(UD)

∆m
n eP m+1
= 0.
(4.14)


## Page 30


30
WENHUA ZHAO
Combining the equation above with Eq. (4.13), we get
∂P
∂zi
(UD)Φ−1
U
 ∆m
AP m+1
= 0.
Φ−1
U (ΦU
∂P
∂zi
(UD)Φ−1
U )
 ∆m
AP m+1
= 0.
(ΦU
∂P
∂zi
(UD)Φ−1
U )
 ∆m
AP m+1
= 0.
(4.15)
By Lemma 2.1, (b), Eq. (4.15) and the fact that A = UUτ, we get
∂P
∂zi
(UUτD)
 ∆m
AP m+1
= ∂P
∂zi
(AD)
 ∆m
AP m+1
= 0,
which is Eq. (4.12) for ∂P
∂zi (1 ≤i ≤n).
✷
Corollary 4.11. Let A be as in Theorem 4.10 and P(z) be a homoge-
neous ∆A-nilpotent polynomial of degree d ≥3. Then, for any m ≥1,
∆m
AP m+1 is isotropic with respect to the C-bilinear form (·, ·)A, i.e.
(∆m
AP m+1, ∆m
AP m+1)A = 0.
(4.16)
In particular, we have (P, P)A = 0.
Proof:
By the deﬁnition Eq. (4.11) of the C-bilinear form (·, ·)A and
Theorem 4.10, it will be enough to show that P and ∆m
AP m+1 (m ≥1)
belong to the ideal generated by the polynomials ∂P
∂zi (1 ≤i ≤n) (here
we do not need to consider the polynomial σA−1(z)). But this statement
has been proved in the proof of Corollary 6.7 in [Z2]. So we refer the
reader to [Z2] for a proof of the statement above.
✷
Theorem 4.10 and Corollary 4.11 do not hold for homogeneous HN
polynomials P(z) of degree d = 2. But, by applying similar arguments
as in the proof of Theorem 4.10 above to Proposition 6.8 in [Z2], one
can show that the following proposition holds.
Proposition 4.12. Let A be as in Theorem 4.10 and P(z) a homoge-
neous ∆A-nilpotent polynomial of degree d = 2. Let J(P) the ideal of
C[z] generated by P(z) and σA−1(z). Then, for any f(z) ∈J(P) and
m ≥0, we have
{f, ∆m
AP m+1}A = f(AD) ∆m
AP m+1 = 0.
(4.17)
In particular, we still have (P, P)A = 0.


## Page 31


A VANISHING CONJECTURE ON DIFFERENTIAL OPERATORS
31
References
[AS]
Handbook of mathematical functions with formulas, graphs, and mathemat-
ical tables. Edited by Milton Abramowitz and Irene A. Stegun. Reprint of
the 1972 edition. Dover Publications, Inc., New York, 1992. [MR0757537].
[BCW] H. Bass, E. Connell, D. Wright, The Jacobian conjecture, reduction of
degree and formal expansion of the inverse. Bull. Amer. Math. Soc. 7,
(1982), 287–330. [MR 83k:14028]. Zbl.539.13012.
[B]
M. de Bondt, Personal Communications.
[BE1]
M. de Bondt and A. van den Essen, A Reduction of the Jacobian Conjecture
to the Symmetric Case, Proc. Amer. Math. Soc. 133 (2005), no. 8, 2201–
2205 (electronic). [MR2138860].
[BE2]
M. de Bondt and A. van den Essen, Nilpotent Symmetric Jacobian Matrices
and the Jacobian Conjecture, J. Pure Appl. Algebra 193 (2004), no. 1-3,
61–70. [MR2076378].
[BE3]
M. de Bondt and A. van den Essen, Nilpotent Symmetric Jacobian Matrices
and the Jacobian Conjecture II, J. Pure Appl. Algebra 196 (2005), no. 2-3,
135–148. [MR2110519].
[C]
T. S. Chihara, An introduction to orthogonal polynomials. Mathematics
and its Applications, Vol. 13. Gordon and Breach Science Publishers, New
York-London-Paris, 1978. [MR0481884].
[DK]
J. J. Duistermaat and W. van der Kallen, Constant terms in powers
of a Laurent polynomial. Indag. Math. (N.S.) 9 (1998), no. 2, 221–231.
[MR1691479].
[DX]
C. Dunkl and Y. Xu, Orthogonal polynomials of several variables. Ency-
clopedia of Mathematics and its Applications, 81. Cambridge University
Press, Cambridge, 2001. [MR1827871].
[E]
A. van den Essen, Polynomial automorphisms and the Jacobian con-
jecture. Progress in Mathematics, 190. Birkh¨auser Verlag, Basel, 2000.
[MR1790619].
[EZ]
A. van den Essen and W. Zhao, Two results on Hessian nilpotent polyno-
mials. Preprint, arXiv:0704.1690v1 [math.AG].
[He]
H. Henryk, Topics in classical automorphic forms, Graduate Studies in
Mathematics, 17. American Mathematical Society, Providence, RI, 1997.
[MR1474964]
[Hu]
L. K. Hua, On the theory of automorphic functions of a matrix level. I.
Geometrical basis. Amer. J. Math. 66, (1944). 470–488. [MR0011133].
[Ke]
O. H. Keller, Ganze Gremona-Transformation, Monats. Math. Physik 47
(1939), no. 1, 299-306. [MR1550818].
[Ko]
T. H. Koornwinder, Two-variable analogues of the classical orthogonal
polynomials. Theory and application of special functions (Proc. Advanced
Sem., Math. Res. Center, Univ. Wisconsin, Madison, Wis., 1975), pp. 435–
495. Math. Res. Center, Univ. Wisconsin, Publ. No. 35, Academic Press,
New York, 1975. [MR0402146].
[Ma]
O. Mathieu, Some conjectures about invariant theory and their applica-
tions. Alg`ebre non commutative, groupes quantiques et invariants (Reims,
1995), 263–279, S´emin. Congr., 2, Soc. Math. France, Paris, 1997.
[MR1601155].


## Page 32


32
WENHUA ZHAO
[Me]
G. Meng, Legendre transform, Hessian conjecture and tree formula.
Appl. Math. Lett. 19 (2006), no. 6, 503–510, [MR2221506]. See also
math-ph/0308035.
[SHW]
J. A. Shohat; E. Hille and J. L. Walsh, A Bibliography on Orthogonal
Polynomials. Bull. Nat. Research Council, no. 103. National Research
Council of the National Academy of Sciences, Washington, D. C., 1940.
[MR0003302].
[Si]
B. Simon, Orthogonal polynomials on the unit circle. Part 1. Classical
theory. American Mathematical Society Colloquium Publications, 54, Part
1. American Mathematical Society, Providence, RI, 2005. [MR2105088].
[Sz]
G. Szeg¨o, Orthogonal Polynomials. 4th edition. American Mathematical
Society, Colloquium Publications, Vol. XXIII. American Mathematical So-
ciety, Providence, R.I., 1975. [MR0372517].
[T]
M. Takeuchi, Modern spherical functions, Translations of Mathematical
Monographs, 135. American Mathematical Society, Providence, RI, 1994.
[MR 1280269].
[Wa]
S. Wang, A Jacobian Criterion for Separability, J. Algebra 65 (1980), 453-
494. [MR 83e:14010].
[Y]
A. V. Jagˇzev, On a problem of O.-H. Keller. (Russian) Sibirsk. Mat. Zh.
21 (1980), no. 5, 141–150, 191. [MR0592226].
[Z1]
W. Zhao, Inversion Problem, Legendre Transform and Inviscid Burg-
ers’ Equation, J. Pure Appl. Algebra, 199 (2005), no. 1-3, 299–317.
[MR2134306]. See also math. CV/0403020.
[Z2]
W. Zhao,
Hessian Nilpotent Polynomials and the Jacobian Conjec-
ture, Trans. Amer. Math. Soc. 359 (2007), no. 1, 249–274 (electronic).
[MR2247890]. See also math.CV/0409534.
[Z3]
W. Zhao, Some Properties and Open Problems of Hessian Nilpotent Poly-
nomials. Preprint, arXiv:0704.1689v1 [math.CV].
[Z4]
W. Zhao, A Conjecture on the Laplace-Beltrami Eigenfunctions. In prepa-
ration.
Department of Mathematics, Illinois State University, Nor-
mal, IL 61790-4520.
E-mail: wzhao@ilstu.edu.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]

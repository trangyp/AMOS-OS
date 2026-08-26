# 0309265v2_Injectivity_of_the_symmetric_map_for_line_bundles

> Source: 0309265v2_Injectivity_of_the_symmetric_map_for_line_bundles.pdf

> Pages: 7

---


## Page 1


arXiv:math/0309265v2  [math.AG]  17 Sep 2003
INJECTIVITY OF THE SYMMETRIC MAP FOR LINE
BUNDLES
MONTSERRAT TEIXIDOR I BIGAS
Abstract. Let C be a generic non-singular curve of genus g de-
ﬁned over a ﬁeld of characteristic diﬀerent from two. We show
that for every line bundle on C of degree at most g +1, the natural
product map
S2(H0(C, L)) →H0(C, L2)
is injective. We also show that the bound on the degree of L is
sharp
1. Introduction
Linear series have played a key role in the study of curves (and higher
dimensional varieties). It is usually important to know how the spaces
of sections of line bundles relate to each other.
For example for a
generic curve of genus g, the Petri map
H0(C, L) ⊗H0(C, K ⊗L−1) →H0(C, K)
is injective. This property gives a lot of information on the structure
of the set of linear series of a given dimension. On the other hand, the
surjectivity of the maps
Sn(H0(C, L)) →H0(C, Ln)
ensure the projective normality of a curve.
Despite its usefulness, there are few criteria that help in computing
the rank of maps among various spaces of sections of vector bundles
(see [B], [T2]). The purpose of the following note is to help ﬁll in this
gap. We want to show that for a generic curve and any line bundle
of degree at most g +1 with a given number of sections, the symmetric
product map
S2(H0(C, L)) →H0(C, L2)
is injective. The result is obviously false for line bundles of high degree,
as even the dimension of the left hand side space becomes bigger than
the dimension of the right hand side. We prove in fact that our bound
is sharp: we construct an example of a line bundle of degree g + 2 on a
1


## Page 2


2
MONTSERRAT TEIXIDOR I BIGAS
generic curve of genus g (for every even g ≥4) for which the symmetric
product map is not injective (see 3.1).
Note that the natural product map
m : H0(C, L) ⊗H0(C, L) →H0(C, L2)
is never injective for k ≥2. Its kernel contains the subspace ∧2(H0(C, L)).
Therefore, proving the injectivity of the map with domain in the sym-
metric power is equivalent to showing that the kernel of m is precisely
the wedge power. This kernel has proved to have important deforma-
tion theoretical meaning in particular cases (see for instance [T1]).
The main result of this paper is the following:
1.1. Theorem Let C be a generic curve deﬁned over an algebraically
closed ﬁeld of characteristic diﬀerent from two. Let L be a line bundle
on C such that deg(L) = d ≤g + 1. Then the map
S2(H0(C, L)) →H0(C, L2)
is injective.
The proof of this result is inspired in the proof of the injectivity of
the Petri map given by Eisenbud and Harris in [E,H2] (see also [W]).
2. The case of degree at most g −1
We shall ﬁx a genus g and the degree d for line bundles L on C. We
shall denote by k (rather than the classical r + 1) the dimension of the
space of sections of these line bundles. We shall assume that k, g, d
have been ﬁxed so that the generic curve of genus g has line bundles
of degree d with k sections (equivalently, the Brill- Noether number
g −k(g −1 −d + k) is non-negative).
In order to prove 1.1 for a generic curve, it suﬃces to prove it for a
special curve. Consider a family of curves π : C →T. Let T be the
spectrum of a discrete valuation ring O with maximal ideal generated
by t. Assume that the generic ﬁber of π is a non-singular curve and
the special ﬁber C looks as follows:
Take g elliptic curves Ei and let P i, Qi be generic points on Ei. Take
any number of rational curves C0
1, ..C0
k0, ...Cg
0...Cg
kg again with points
P i
j, Qi
j on them. Glue Ci
j to Ci
j+1 by identifying Qi
j to P i
j+1. Glue Ci−1
ki−1
to Ei by identifying Qi−1
ki−1 to P i. Glue Ei to Ci
1 by identifying Qi to
P i
1.
For convenience of notation, we shall denote by
Y1, ...YM, M = k0 + ... + kg + g


## Page 3


INJECTIVITY OF THE SYMMETRIC MAP FOR LINE BUNDLES
3
the components of C starting with C0
1 and ending with Cg
kg. We shall
denote by Pi, Qi the two points in Yi that get identiﬁed to Qi−1 ∈Yi−1
and Pi+1 ∈Yi+1 respectively. We warn the reader that we shall keep
the superindices i when we need to refer to the ith elliptic curve. We
hope this will not produce too much confusion.
Note that the form of the central ﬁber does not change if we make
base changes and normalisations.
Consider now the set up of limit of a linear series in the sense of
Eisenbud and Harris ([E,H2] p.273 or [E,H1], section 2).
Let L be
a line bundle on C. One can modify L by tensoring with divisor with
support on the central ﬁber. This leaves invariant the line bundle on the
generic ﬁber but modiﬁes it in the central ﬁber. For every component
Yi of C, there is a line bundle Li on C such that it has degree zero on
every component of the central ﬁber except for the component Yi. As
Li = Li+1(−d
P
j≤i Yj), one can identify Li with a subsheaf of Li+1.
Consider π∗(Li) This is a free O module of rank k. Moreover, Li ⊂
Li+1 is a lattice. Denote by Vi the image of the restriction map
π∗Li →π∗Li|Yi = H0(Yi, Li|Yi)
As degLi|Yj = 0, j ̸= i, this map is injective and we shall sometimes
identify π∗(Li) with Vi.
From [E,H2] Lemma 1.2, one can ﬁnd a basis of sections σi
m, m =
1..k of the free module π∗(Li) such that the orders of vanishing of the
sections σi
m at Pi are the diﬀerent orders of vanishing of the sections of
Vi and tαi
mσi
m, m = 1...k form a basis for π∗Li+1.
We shall now relate the vanishing of sections of line bundles at the
various nodes.
2.1. Lemma 1) Let Y be any irreducible non-singular curve L a line
bundle of degree d on Y and P, Q two points on Y . The sum of the
orders of vanishing at P and Q of any section of L is at most d.
2) Let Y be an elliptic curve and P, Q generic points of Y . Let L
be a line bundle of degree d on Y .The sum of the orders of vanishing
at P and Q of any section of L is at most d −1 except in the case
where L = O(aP + (d −a)Q) for some a. In this case, there is only
one section of L vanishing with multiplicities adding up to d at the two
points.
Proof. If a section of a line bundle L vanishes with order a at P and
b at Q, then O(aP + bQ) is a subsheaf of L. Hence, d ≥a + b. This
proves the ﬁrst statement.
If a + b = d, then L = O(aP + bQ). If there is another section
vanishing to orders a′, b′ at P, Q with a′ + b′ = d and say a′ > a then


## Page 4


4
MONTSERRAT TEIXIDOR I BIGAS
aP +bQ ≡a′P +b′Q. Hence, cP ≡cQ with c = a′−a. This contradicts
the genericity of the pair P, Q if Y is not rational.
□
Remark The genericity of P, Q is essential here. If cP is linearly
equivalent to cQ for some c ≤d, then the line bundle O(aP + (d −
a)Q), a ≥c has (at least) two sections with orders of vanishing adding
up to d at P, Q namely aP + (d −a)Q and (a −c)P + (d −a + c)Q.
The following result of Eisenbud and Harris (cf. Prop 1.1 in [E,H]),
will be used in the sequel.
2.2. Lemma Let σ be a section in π∗Li. Let α be the unique integer
such that tασ ∈π∗(Li+1) −tπ∗(Li+1), then
ordPi(σ|Yi) ≤d −ordQi(σ|Yi) ≤α ≤ordPi+1(tασ|Yi+1)
As in [E,H], p.277, one can deﬁne the order of a section ρ ∈S2(π∗LY )
at a point P in a component Y as follows:
2.3. Deﬁnition We say ordP(ρ|Y ) ≥l if and only if ρ is in the linear
span of t(S2(π∗(LY ))) and elements of the form σm ⊗σn + σn ⊗σm
where ordP(σn) + ordP(σm) ≥l, σn, σm ∈π∗(LY ).
One then has the following result (cf. [E,H2], Lemma 3.2)
2.4. Lemma Let σm be a basis of the free O module π∗(Li) such that the
orders of vanishing of the σm at Pi are the distinct orders of vanishing
of the linear series at this point and tαmσm is a basis of π∗(Li+1). If
ρ =
X
fn,m(σn ⊗σm + σm ⊗σn) ∈S2(π∗Li)
where the fn,m are functions on the discrete valuation ring O and the
associated discrete valuation is ν, then
ordPi(ρ|Yi) = min{ν(fn,m)=0}(ordPi(σn) + ordPi(σm))
If β is the unique integer such that
tβρ ∈S2π∗Li+1 −t(S2π∗Li+1)
then
β = max{αn + αm −ν(fnm)}
Let us assume now that the kernel of the symmetric product map
is non-zero on the generic curve. We can then ﬁnd an element ρ such
that say ρ ∈S2(π∗L1) −tS2(π∗L1) and integers βi, i = 2...M such that
tβiρ ∈S2(π∗Li) −tS2(π∗Li) and tβiρ ∈Ker(S2(π∗Li) →π∗(Li)2).
As a section of a line bundle cannot vanish to order higher than the
degree, the following claim will conclude the proof in the case d ≤g−1.


## Page 5


INJECTIVITY OF THE SYMMETRIC MAP FOR LINE BUNDLES
5
2.5. Claim If l > k0 + ... + km−1 + m, then ordPl(tβlρ) ≥2m. In
particular, for l ≥k0 + ... + kg−1 + g, ordPl(tβlρ) ≥2g.
Proof. We prove the following two statements:
1) If Ci is a rational curve,
ordPi+1(tβi+1ρ|Yi+1) ≥ordPi(tβiρ|Yi)
.
2) If Ci is an elliptic component,
ordPi+1(tβi+1ρ|Yi+1) ≥ordPi(tβiρ|Yi) + 2
In other words, the order of vanishing of a section tβi+1ρ at Pi+1 is
at least as large as that of tβiρ at Pi if Yi is rational and at least two
units larger if it is elliptic. As the order of vanishing tβ0ρ at P0 is non-
negative, this shows that the order of vanishing of tβiρ at Pi is at least
2m if m elliptic curves precede Yi. This is the ﬁrst part of the claim.
The second part follows from the ﬁrst when m = g.
We now turn to the proof of 1) and 2). Choose a basis σm, m =
1...k of π∗(Li) such that tαmσm is a basis of π∗Li+1. For simplicity of
notation, we shall assume that βi = 0 Write
ρ =
X
n≤m
fnm(σn ⊗σm + σm ⊗σn) ∈S2(π∗Li)
Then, from 2.4,
ordPi(ρ|Yi) = min{ν(fnm)=0}(ordPi(σn) + ordPi(σm))
Assume that this minimum is attained by a pair corresponding to the
indices n0, m0 with ν(fn0,m0) = 0. Then from 2.2,
(ordPi(σn0) + ordPi(σm0)) ≤2d −ordQi(σn0) −ordQi(σm0) ≤αn0 + αm0
From 2.4 and the fact that ν(fn0,m0) = 0, the latter is at most βi+1.
Write
tβi+1ρ =
X
n≤m
(tβi+1−αn−αmfnm)(tαnσn ⊗tαmσm + tαmσm ⊗tαnσn)
Hence, from 2.4
ordPi+1(tβi+1ρ|Yi+1) = min{βi+1−αn−αm+ν(fnm)=0}(ordPi+1(tαnσn)+ordPi+1(tαmσm))
Assume that this minimum is attained at a pair n1, m1 with
βi+1 −αn1 −αm1 + ν(fn1,m1) = 0
Then,
βi+1 ≤βi+1+ν(fn1,m1) = αn1+αm1 ≤ordPi+1(tαn1σn1)+ordPi+1(tαm1σm1))
where the last inequality comes from 2.2


## Page 6


6
MONTSERRAT TEIXIDOR I BIGAS
Stringing together the above inequalities, we obtain ordPi(ρ|Yi) ≤
ordPi+1(ρ|Yi+1). Hence part 1) is proved.
Assume now that there is equality in the inequality above. Then all
the previous inequalities must be equalities. In particular, the terms
σn0 ⊗σm0 + σm0 ⊗σn0 that give the vanishing of ρ at Pi satisfy
ordPi(σk) + ordQi(σk) = d, k = n0, m0
.
If we have ordPi+1(ρ|Yi+1) = ordPi(ρ|Yi) + 1, then in each pair, one of
σk, k = n0, m0 would vanish to order d between the two nodes. From
2.1, there is at most one such section σi0 on our elliptic curves.
Hence, if ordPi+1(ρ|Yi+1) ≤ordPi(ρ|Yi) + 1, the terms in ρ giving the
vanishing at Pi could be written as
σi0 ⊗σ + σ ⊗σi0
for some section σ. As a section like this cannot be in the kernel of the
symmetric product map, this concludes the proof of the claim.
□
3. The cases of degree g, g + 1 and counterexamples in
degree g + 2
Assume now d = g. Consider the last elliptic component Eg with
nodes P g, Qg. Write the restriction to the central ﬁber of an element
in the kernel of the symmetric evaluation map as
ρ =
X
fnm(σn ⊗σm + σm ⊗σn), σn, σm ∈π∗(LEg)
.
Consider a pair σn, σm that gives the vanishing of ρ at P g. From 2.5,
ordP g(σn) + ordP g(σm) ≥2(g −1). As deg(LEg|Eg) = g, ordP g(σk) ≤
g, k = n, m. It follows that the possible orders of such sections are
g, g −1, g −2. If there is a section vanishing to order g at P g, then
LEg|Eg = O(gP g) and this line bundle does not have any section van-
ishing to order g −1 at P g. Hence there are at most two independent
sections among the σk and for every pair that appears, the sum of the
orders of vanishing at P g is the same. But then ρ cannot be in the
kernel of the symmetric product map. This concludes the proof for
d = g
Assume now that d = g + 1. If ordP 1(ρ) = 0, 1, then the pairs of
sections giving the vanishing at P 1 will vanish to orders 0, 1. From
our choice of basis, there are at most two sections satisfying these
conditions. Hence, again ρ could not be in the kernel of the symmetric
product map. Therefore the vanishing of ρ at P 1 is at least two. From


## Page 7


INJECTIVITY OF THE SYMMETRIC MAP FOR LINE BUNDLES
7
statements 1) and 2) in 2.5, the vanishing at P g is at least 2g. Now,
we conclude as in the case d = g.
3.1. Example If g is even, g ≥4 a generic curve of genus g has a line
bundle of degree g + 2 such that the kernel of the symmetric product
map is not injective.
Proof. A generic curve of even genus g has line bundles of degree g/2+1
with two sections (because the corresponding Brill-Noether number is
zero). Take two diﬀerent ones L1, L2 and choose independent sections
s1, t1 and s2, t2 of them. Take L = L1 ⊗L2. This is a line bundle of
degree g + 2 that contains the sections s1s2, s1t2, t1s2, t1t2. These are
four independent sections, as can be checked using the base point free
pencil trick.
Consider now the following section
(s1s2 ⊗t1t2 + t1t2 ⊗s1s2) −(s1t2 ⊗s2t1 + s2t1 ⊗s1t2)
This section is non-zero and in the kernel of the symmetric product
map.
□
References
[B]
D.Butler normal generation of vector bundles over a curve J.Diﬀ.Geom 39
(1994), 1-34.
[E,H1] D.Eisenbud, J.Harris Limit linear series, basic theory, Invent.Math. 85
(1986), 337-371.
[E,H2] D.Eisenbud, J.Harris A simpler proof of the Gieseker-Petri Theorem for
special divisors, Invent.Math. 74 (1983), 269-280.
[T1] M.Teixidor Half-canonical series on algebraic curves Trans.AMS 302 (1987),
99-115.
[T2] M.Teixidor Curves in Grassmannians Proc.AMS 126 (1998), 1597-1603.
[W]
G.Welters A Theorem of Gieseker-Petri type for Prym varieties Ann.Sci. Ec.
Norm. 4s., t 18, 1985, 671-683
Mathematics Department, Tufts University, Medford, MA02155
E-mail address: montserrat.teixidoribigas@tufts.edu

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1710.07895
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1710.07895_On_the_determination_of_the_Singer_transfer

> Source: 1710.07895_On_the_determination_of_the_Singer_transfer.pdf

> Pages: 19

---


## Page 1


ON THE DETERMINATION OF THE SINGER TRANSFER
NGUYỄN SUM
Abstract. Let Pk be the graded polynomial algebra F2[x1, x2, . . . , xk] with
the degree of each generator xi being 1, where F2 denote the prime field of two
elements, and let GLk be the general linear group over F2 which acts regularly
on Pk.
We study the algebraic transfer constructed by Singer [18] using the tech-
nique of the Peterson hit problem. This transfer is a homomorphism from the
homology of the mod-2 Steenrod algebra A, TorA
k,k+d(F2, F2), to the subspace
of F2⊗APk consisting of all the GLk-invariant classes of degree d.
In this paper, by using the results on the Peterson hit problem we present
the proof of the fact that the Singer algebraic transfer is an isomorphism for
k ⩽3. This result has been proved by Singer in [18] for k ⩽2 and by Boardman
in [3] for k = 3. We show that the fourth Singer transfer is also an isomorphism
in certain internal degrees. This result is new and it is different from the ones
of Bruner, Hà and Hưng [5], Chơn and Hà [8], Hà [9], Hưng and Quỳnh [12],
Nam [16].
1. Introduction
Denote by Pk := F2[x1, x2, . . . , xk] the polynomial algebra over the field of two
elements, F2, in k generators x1, x2, . . . , xk, each of degree 1. This algebra arises
as the cohomology with coefficients in F2 of an elementary abelian 2-group of rank
k. Therefore, Pk is a module over the mod-2 Steenrod algebra, A. The action of A
on Pn is determined by the elementary properties of the Steenrod squares Sqi and
subject to the Cartan formula Sqk(fg) = Pk
i=0 Sqi(f)Sqk−i(g), for f, g ∈Pk (see
Steenrod and Epstein [19]).
The Peterson hit problem is to find a minimal generating set for Pk regarded as
a module over the mod-2 Steenrod algebra. Equivalently, this problem is to find
a vector space basis for QPk := F2 ⊗A Pk in each degree d. Such a basis may be
represented by a list of monomials of degree d. It is completely determined for
k ⩽4, unknown in general.
Let GLk be the general linear group over the field F2. This group acts naturally
on Pk by matrix substitution. Since the two actions of A and GLk upon Pk commute
with each other, there is an inherited action of GLk on QPk.
Denote by (Pk)d the subspace of Pk consisting of all the homogeneous polyno-
mials of degree d in Pk and by (QPk)d the subspace of QPk consisting of all the
classes represented by the elements in (Pk)d. In [18], Singer defined the algebraic
2010 Mathematics Subject Classification. Primary 55T15; Secondary 55S10, 55S05.
Key words and phrases. Steenrod algebra, algebraic transfer, polynomial algebra.
This research is funded by Vietnam National Foundation for Science and Technology Develop-
ment (NAFOSTED) under grant number 101.04-2017.05.
1
arXiv:1710.07895v4  [math.AT]  7 Aug 2025


## Page 2


2
NGUYỄN SUM
transfer, which is a homomorphism
φk : TorA
k,k+d(F2, F2) −→(QPk)GLk
d
from the homology of the Steenrod algebra to the subspace of (QPk)d consisting of
all the GLk-invariant classes. It is a useful tool in describing the homology groups of
the Steenrod algebra, TorA
k,k+d(F2, F2). This transfer was studied by Boardman [3],
Bruner, Hà and Hưng [5], Hà [9], Hưng [11], Chơn and Hà [6, 7, 8], Minami [15],
Nam [16], Hưng and Quỳnh [12], the present author [22] and others.
Singer showed in [18] that φk is an isomorphism for k = 1, 2. Boardman showed
in [3] that φ3 is also an isomorphism. However, for any k ⩾4, φk is not a monomor-
phism in infinitely many degrees (see Singer [18], Bruner, Hà and Hưng [5], Hưng
[11].) Singer made a conjecture in [18] that the algebraic transfer φk is an epimor-
phism for any k ⩾0. This conjecture is true for k ⩽3. It can be verified for k = 4
by using the results in [21, 28]. The conjecture for k ⩾5 is an open problem.
In this paper, by using the results on the Peterson hit problem we present the
proof of the fact that the Singer algebraic transfer is an isomorphism for k ⩽3.
Recall that this result has been proved by Singer in [18] for k ⩽2 and by Boardman
in [3] for k = 3. To prove this result, Boardman [3] computed the space QP GL3
3
by
using a basis consisting of the all the classes represented by certain polynomials in
P3. We also compute this space, however we use the admissible monomial basis for
QP3 that is different from the one of Boardman in [3]. By applying this technique
for k = 4, we show that the fourth Singer transfer is also an isomorphism in certain
internal degrees. This result is new and it is different from the ones of Bruner, Hà
and Hưng [5], Chơn and Hà [8], Hà [9], Hưng and Quỳnh [12], Nam [16]. In those
works it is shown only that the fourth Singer transfer detects certain families of
elements in Ext4,∗
A (F2, F2), and fails to detect others.
This paper is organized as follows. In Section 2, we recall some needed infor-
mation on the lambda algebra and the Singer algebraic transfer. In Sections 3, we
present the determination of the algebraic transfer for k ⩽3. Finally, in Section
4, we show that the fourth Singer transfer is an isomorphism in certain internal
degrees.
2. The Singer algebraic transfer and the lambda algebra
First of all, we briefly recall the definition of the Singer transfer. Let bP1 be the
submodule of F2[x1, x−1
1 ] spanned by all powers xi
1 with i ⩾−1. The usual A-action
on P1 = F2[x1] is canonically extended to an A-action on F2[x1, x−1
1 ] (see Singer
[18]). bP1 is an A-submodule of F2[x1, x−1
1 ]. The inclusion P1 ⊂bP1 gives rise to a
short exact sequence of A-modules:
0 −→P1 −→bP1 −→Σ−1F2 −→0.
Let e1 be the corresponding element in Ext1
A(Σ−1F2, P1). By using the cross and
Yoneda products, Singer set
ek = (e1 × Pk−1) ◦(e1 × Pk−2) ◦. . . (e1 × P1) ◦e1 ∈Extk
A(Σ−kF2, Pk).
Then, he defined ˆ
φk : TorA
k (F2, Σ−kF2) −→TorA
0 (F2, Pk) = QPk by ˆφk(z) = ek ∩z.
Its image is a submodule of (QPk)GLk. So, ˆφk induces the homomorphism
φk : TorA
k (F2, Σ−kF2) −→QP GLk
k
.


## Page 3


ON THE DETERMINATION OF THE SINGER TRANSFER
3
Denote by (Pk)∗the dual of Pk and by P((Pk)∗) the primitive subspace consisting
of all elements in (Pk)∗that are annihilated by every positive degree operations in
the mod-2 Steenrod algebra. The dual of φk:
Trk := (φk)∗: F2 ⊗GLk P((Pk)∗
d) −→Extk,k+d
A
(F2, F2)
is also called the k-th Singer transfer.
The algebra Ext∗,∗
A (F2, F2) is described in terms of the mod-2 lambda algebra
Λ (see [4]). Recall that Λ is a bigraded differential algebra over F2 generated by
λj ∈Λ1,j, j ⩾0, with the relations
λjλ2j+1+m =
X
ν⩾0
m −ν −1
ν

λj+m−νλ2j+1+ν,
(2.1)
for m ⩾0 and the differential
δ(λi) =
X
ν⩾0
i −ν −1
ν + 1

λk−ν−1λν,
(2.2)
for i > 0, δ(λ0) = 0 and that Hk,d(Λ, δ) = Extk,k+d
A
(F2, F2).
For example, the elements λ2i−1 ∈Λ1,2i−1, i ⩾0, and ¯d0 = λ6λ2λ2
3 + λ2
4λ2
3 +
λ2λ4λ5λ3 + λ1λ5λ1λ7 ∈Λ4,14 are the cycles in the lambda algebra Λ. So, hi =
[λ2i−1] and d0 = [ ¯d0] are the elements in Ext∗,∗
A (F2, F2). Note that hi is the Adams
element in Ext1,2i
A (F2, F2).
There is a homomorphism f
Sq
0 : Λ →Λ determined by
f
Sq
0(λj1λj2 . . . λjk) = λ2j1+1λ2j2+1 . . . λ2jk+1, k ⩾0.
This homomorphism respects the relations in (2.1) and commutes the differential
in (2.2). Therefore, it induces a homomorphism
Sq0 : Extk,k+d
A
(F2, F2) = Hk,d(Λ) −→Hk,k+2d(Λ) = Extk,2k+2d
A
(F2, F2).
A family {ai : i ⩾0} of elements in Extk,k+∗
A
(F2, F2) is called a Sq0-family if ai =
(Sq0)i(a0) for every i ⩾0. It is well known that Ext3,3+∗
A
(F2, F2) contains the Sq0-
family of indecomposable elements {ci} and Ext4,4+∗
A
(F2, F2) contains seven Sq0-
families of indecomposable elements, namely {di}, {ei}, {fi}, {gi+1}, {pi}, {D3(i)},
and {p′
i}. Note that {hi} is also a Sq0-family in Ext1,1+∗
A
(F2, F2).
The algebra {Extk,k+∗
A
(F2, F2)|k ⩾0} has been explicitly computed by Adem [2]
for k = 1, by Adams [1] and Wall [24] for k = 2, by Adams [1] and Wang [25] for
k = 3 and by Lin [14] for k = 4.
Theorem 2.1 (See [1, 2, 14, 24, 25]).
i) The algebra {Extk,k+∗
A
(F2, F2)|k ⩾0} for k ⩽3 is generated by hi and ci
for i ⩾0 and subject only to the relations hihi+1 = 0, hih2
i+2 = 0 and h3
i =
h2
i−1hi+1. In particular, {ci : i ⩾0} is an F2-basis for the indecomposable elements
in Ext3,3+∗
A
(F2, F2).
ii) The algebra {Extk,k+∗
A
(F2, F2)|k ⩾0} for k ⩽4 is generated by hi, ci, di, ei,
fi, gi+1, pi, D3(i) and p′
i for i ⩾0 and subject to the relations in i) together with
the relations h2
i h2
i+3 = 0, hjci = 0 for j = i −1, i, i + 2 and i + 3. Furthermore, the
set of the elements di, ei, fi, gi+1, pi, D3(i) and p′
i, for i ⩾0, is an F2-basis for the
indecomposable elements in Ext4,4+∗
A
(F2, F2).


## Page 4


4
NGUYỄN SUM
It is well known that the dual of Pk is the divided power algebra generated by
a1, a2, . . . , ak:
(Pk)∗= Γ(a1, a2, . . . , ak)
where a(i)
j
is dual to xi
j ∈Pk with respect to the basis of Pk consisting of all
monomials in x1, x2, . . . , xk and aj = a(1)
j . The graded vector space {(Pk)∗|k ⩾0}
is an algebra with a multiplication defined by
(a(i1)
1
. . . a(ik)
k
)(a(ik+1)
1
. . . a(ik+m)
m
) = a(i1)
1
. . . a(ik)
k
a(ik+1)
k+1
. . . a(ik+m)
k+m
∈(Pk+m)∗,
for any a(i1)
1
. . . a(ik)
k
∈(Pk)∗and a(ik+1)
1
. . . a(ik+m)
m
∈(Pm)∗. In [6], Chơn and Hà
defined a homomorphism of algebras
ϕ = {ϕk|k ⩾0} : {(Pk)∗|k ⩾0} −→{Λk,∗|k ⩾0} = Λ,
which induces the Singer transfer. Here, the homomorphism ϕk : (Pk)∗→Λk,∗is
defined by the following inductive formula:
ϕk(a(I,t)) =
(
λt,
if k −1 = ℓ(I) = 0,
P
i⩾t ϕk−1(Sqi−taI)λi,
if k −1 = ℓ(I) > 0,
for any a(I,t) = a(i1)
1
a(i2)
2
. . . a(ik−1)
k−1
a(t)
k
∈(Pk)∗and I = (i1, i2, . . . , ik−1).
Theorem 2.2 (See Chơn and Hà [6]). If b ∈P((Pk)∗), then ϕk(b) is a cycle in the
lambda algebra Λ and Trk([b]) = [ϕk(b)].
Note that this theorem is a dual version of the one in Hưng [10].
We end this section by recalling some results on Kameko’s homomorphism and
the generators of the general linear group GLk.
One of the main tools in the study of the hit problem is Kameko’s homomorphism
f
Sq
0
∗: QPk →QPk. This homomorphism is induced by the F2-linear map ψ : Pk →
Pk, given by
ψ(x) =
(
y,
if x = x1x2 . . . xky2,
0,
otherwise,
for any monomial x ∈Pk. Note that ψ is not an A-homomorphism. However,
ψSq2t = Sqtψ, and ψSq2t+1 = 0 for any non-negative integer t.
For a positive integer n, by µ(n) one means the smallest number r for which it
is possible to write n = P
1⩽i⩽r(2ui −1), where ui > 0.
Theorem 2.3 (Kameko [13]). Let m be a positive integer. If µ(2m + k) = k, then
(f
Sq
0
∗)m : (QPk)2m+k →(QPk)m is an isomorphism of the GLk-modules.
Definition 2.4. Let f, g be two polynomials of the same degree in Pk. Then, f ≡g
if and only if f −g ∈A+Pk. If f ≡0, then f is called hit.
For 1 ⩽i ⩽k, define the A-homomorphism ρi : Pk →Pk, which is determined
by ρi(xi) = xi+1, ρi(xi+1) = xi, ρi(xj) = xj for j ̸= i, i + 1, 1 ⩽i < k, and
ρk(x1) = x1 + x2, ρk(xj) = xj for j > 1.
It is easy to see that the general linear group GLk is generated by the matrices
associated with ρi, 1 ⩽i ⩽k, and the symmetric group Σk is generated by the
ones associated with ρi, 1 ⩽i < k. So, a class [f] represented by a homogeneous
polynomial f ∈Pk is an GLk-invariant if and only if ρi(f) ≡f for 1 ⩽i ⩽k. It is
an Σk-invariant if and only if ρi(f) ≡f for 1 ⩽i < k.


## Page 5


ON THE DETERMINATION OF THE SINGER TRANSFER
5
3. Determination of Trk for k ⩽3
3.1. Determination of Trk for k ⩽2.
In this subsection, we present the proof of the following.
Theorem 3.1.1 (Singer [18]). The algebraic transfer Trk is an isomorphism for
k ⩽2.
It is well-known that
(QP1)GL1
n
= (QP1)n =
(
⟨[x2u−1]⟩,
if n = 2u −1, u ⩾0,
0,
otherwise.
According to Theorem 2.1, we have
Ext1,t+1
A
(F2, F2) =
(
⟨hu⟩,
if t = 2u −1, u ⩾0,
0,
otherwise.
Since (P1)∗= Γ(a) and a(2u−1) ∈P((P1)∗), ϕ1(a(2u−1)) = λ2u−1 is a cycle in Λ1,∗.
Using Theorem 2.2, we get
Tr1([a(2u−1)]) = [ϕ1(a(2u−1))] = [λ2u−1] = hu, ∀u ⩾0.
So, Tr1 is a isomorphism.
Now, we present the proof of this theorem for k = 2 by computing the space
(QP2)GL2. From a result of Wood [26], we need only to compute this space in the
degree n = 2s+t + 2s −2 with s, t non-negative integers.
First, we consider the degree n = 2s+1−2 with s ⩾0. Since the iterated Kameko
homomorphism (f
Sq
0
∗)s : (QP2)n →(QP2)0 is a isomorphism of GL2-modules and
(QP2)GL2
0
= ⟨1⟩, hence (QP2)GL2
n
= ⟨[p2,s]⟩with p2,s := (x1x2)2s−1.
Next, we compute (QP2)GL2
n
with n = 2s+1 + 2s −2, s ⩾0. Since the iterated
Kameko homomorphism (f
Sq
0
∗)s : (QP2)n →(QP2)1 is a isomorphism of GL2-
modules, we need only to compute (QP2)GL2
1
.
According to Peterson [17], (QP2)n is the vector space of dimension 2 with a
basis consisting of 2 classes represented by the following monomials:
vs,1 = x2s−1
1
x2s+1−1
2
, vs,2 = x2s+1−1
1
x2s−1
2
.
In particular, v0,1 = x2. v0,2 = x1. Suppose θ = a1v1 + a2v2 = a1x2 + a2x1 ∈
(QP2)GL2
1
with a1, a2 ∈F2. Then ρ1(θ) = a1v2 + a2v1 ≡θ. So, we get a1 = a2.
Since ρ2(θ) ≡a1v1 + a2(v1 + v2) ≡θ, we obtain a1 = a2 = 0. Hence, (QP2)GL2
1
= 0
and (QP2)GL2
n
= 0.
Now, we consider the degree n = 2s+t + 2s −2 with s, t non-negative integers,
t ⩾2. Since (f
Sq
0
∗)s : (QP2)n →(QP2)2t−1 is a isomorphism of GL2-modules, we
need only to compute (QP2)GL2
2t−1.
According to Peterson [17], (QP2)2t−1 is the
vector space of dimension 3 with a basis consisting of 3 classes represented by the
following monomials:
ut,1 = x2t−1
1
, ut,2 = x2t−1
2
, ut,3 = x1x2t−2
2
.
Suppose θt = a1ut,1 + a2ut,2 + a3ut,3 with a1, a2, a3 ∈F2 and [θt] ∈(QP2)GL2
2t−1.
By a simple computation, we have ρ1(θt) = a1ut,2 + a2ut,1 + a3ut,3 ≡θt, hence


## Page 6


6
NGUYỄN SUM
a1 = a2 = a. Then, ρ2(θt) ≡a(ut,1 + ut,2) + aut,2 + a3(ut,2 + ut,3) ≡θt. So, we get
a3 = a. Hence, θt = ap2,0,t with p2,0,t = ut,1 + ut,2 + ut,3 and
(QP2)GL2
n
= ⟨[ψs(p2,0,t)]⟩.
Combining the above results, we obtain
Proposition 3.1.2. Let n be a non-negative integer. We have
(QP2)GL2
n
=





⟨[p2,s]⟩,
if n = 2s+1 −2, s ⩾0
⟨[p2,s,t]⟩,
if n = 2s+t + 2s −2, s ⩾0, t ⩾2,
0,
otherwise,
where p2,s,t = ψs(p2,0,t).
Recall that (P2)∗= Γ(a1, a2). For any s, t ⩾0, we set
q2,s,t := a(2s−1)
1
a(2s+t−1)
2
∈P((P2)∗
2s+t+2s−2).
Since ⟨q2,s,0, p2,s⟩= 1 and ⟨q2,s,t, p2,s,t⟩= 1 for every s ⩾0, t ⩾2, from Proposition
3.1.2, we get the following.
Proposition 3.1.3. For n a non-negative integer, we obtain
F2⊗GL2P((P2)∗
n) =





⟨[q2,s,0]⟩,
if n = 2s+1 −2, s ⩾0
⟨[q2,s,t]⟩,
if n = 2s+t + 2s −2, s ⩾0, t ⩾2,
0,
otherwise.
It is easy to see that ϕ2(q2,s,t) = λ2s−1λ2s+t−1 is a cycle in Λ2,∗.
Applying
Theorem 2.2, we get
Tr2([q2,s,t]) = [ϕ2(q2,s,t)] = [λ2s−1λs+t] = hshs+t.
Since hshs+1 = 0, applying Theorem 2.1, we have
Ext2,m
A (F2, F2) =





⟨h2
s⟩,
if m = 2s+1, with s ⩾0,
⟨hshs+t⟩,
if m = 2s+t + 2s, with s ⩾0, t ⩾2,
0,
otherwise.
Theorem 3.1.1 is completely proved.
3.2. Determination of Tr3.
In this subsection, we present the proof of the following.
Theorem 3.2.1 (Boardman [3]). The third Singer algebraic transfer
Tr3 : F2⊗GL3P((P3)∗) −→Ext3,∗+3
A
(F2, F2)
is an isomorphism.
To prove this theorem, Boardman [3] computed the space QP GL3
3
by using a
basis consisting of the all the classes represented by certain polynomials in P3. It
is difficult to use his method for k = 4, where there are 315 polynomials instead of
21. We also compute this space, however we use the admissible monomial basis for
QP3 that is different from the one of Boardman in [3]. Our approach can be apply
for k = 4 by using the admissible monomial basis for QP4 which is given in [21, 28].
From a result of Wood [26], we need only to compute QP GL3
3
in the degree n
with µ(n) ⩽3.


## Page 7


ON THE DETERMINATION OF THE SINGER TRANSFER
7
3.2.1. The case n = 2t+1 −2.
According to Kameko [13], (QP3)n is a vector space with a basis consisting of
all the classes represented by the following monomials:
vt,1 = x2t−1
2
x2t−1
3
, vt,2 = x2t−1
1
x2t−1
3
, vt,3 = x2t−1
1
x2t−1
2
,
for t ⩾1,
vt,4 = x1x2t−2
2
x2t−1
3
, vt,5 = x1x2t−1
2
x2t−2
3
, vt,6 = x2t−1
1
x2x2t−2
3
,
for t ⩾2,
vt,7 = x3
1x2t−3
2
x2t−2
3
,
for t ⩾3
Set p3,t = P7
i=1 vt,i, with t ⩾3. By a direct computation, we have
Proposition 3.2.2. For any non-negative integer t, we have
(QP3)GL3
2t+1−2 =





⟨1⟩,
if t = 0,
0,
if t = 1, 2,
⟨[p3,t]⟩,
if t ⩾3.
Recall that (P3)∗= Γ(a1, a2, a3). We set
q3,t = a(0)
1 a(2t−1)
2
a(2t−1)
3
∈P((P3)∗
2t+1−2).
Since ⟨p3,t, q3,t⟩= 1, we get
F2⊗GL3P((P3)∗
2t+1−2) =





⟨[1]⟩,
if t = 0
0,
if t = 1, 2,
⟨[q3,t]⟩,
if t ⩾3.
It is easy to see that ϕ3(q3,t) = λ0λ2
2t−1 is a cycle in Λ3,∗. By Theorem 2.2, we
have
Tr3([q3,t]) = [ϕ3(q3,t)] = [λ0λ2
2t−1] = h0h2
t.
According to Theorem 2.1, we have
Ext3,2t+1+1
A
(F2, F2) = ⟨h0h2
t⟩.
Since h0h1 = 0 and h0h2
2 = 0, from the above equalities we see that Theorem 3.2.1
is true in this case.
3.2.2. The case n = 2t+u + 2u −3.
If u > 1 then µ(n) = 3, hence the iterated Kameko homomorphism
(f
Sq
0
∗)u−1 : (QP3)2t+u+2u−3 →(QP3)2t+1−1
is also an isomorphism GL3-modules. Hence, we need only to compute (QP3)GL3
2t+1−1.
According to Kameko [13], (QP3)n is a vector space with a basis consisting of all


## Page 8


8
NGUYỄN SUM
the classes represented by the following monomials:
ut,1 = x2t+1−1
3
, ut,2 = x2t+1−1
2
, ut,3 = x2t+1−1
1
,
for t ⩾0,
ut,4 = x2x2t+1−2
3
, ut,5 = x1x2t+1−2
3
, ut,6 = x1x2t+1−2
2
,
for t ⩾1,
u1,7 = x1x2x3, for t = 1,
ut,7 = x1x2
2x2t+1−4
3
, ut,8 = x1x2t−1
2
x2t−1
3
,
ut,9 = x2t−1
1
x2x2t−1
3
, ut,10 = x2t−1
1
x2t−1
2
x3,
for t ⩾2,
ut,11 = x3
1x2t−3
2
x2t−1
3
, ut,12 = x3
1x2t−1
2
x2t−3
3
, ut,13 = x2t−1
1
x3
2x2t−3
3
,
for t ⩾3,
ut,14 = x7
1x2t−5
2
x2t−3
3
,
for t ⩾4.
Set p3,t,1 = P7
i=1 ut,i for t ⩾1 and ¯p3,t,1 = P14
j=7 ut,j for t ⩾4. By a direct
computation we have
Proposition 3.2.3. For any integers t ⩾0, u > 0, we have
(QP3)GL3
2t+u+2u−3 =





0,
if t = 0,
⟨[p3,t,u]⟩,
if 1 ⩽t ⩽3,
⟨[p3,t,u], [¯p3,t,u]⟩,
if t ⩾4,
where p3,t,u = ψu−1(p3,t,1), ¯p3,t,u = ψu−1(¯p3,t,1).
We set
q3,t,u = a(2u−1−1)
1
a(2u−1−1)
2
a(2t+u−1)
3
,
¯q3,t,u = a(2u−1)
1
a(2t+u−1−1)
2
a(2t+u−1−1)
3
.
It is easy to see that q3,t,u, ¯q3,t,u ∈P((P3)∗
2t+1−2) and
⟨p3,t,u, q3,t,u⟩= 1, ⟨p3,t,u, ¯q3,t,u⟩= 0,
⟨¯p3,t,u, q3,t,u⟩= 0, ⟨¯p3,t,u, ¯q3,t,u⟩= 1.
So, we get
F2⊗GL3P((P3)∗
2t+u+2u−3) =





0,
if t = 0,
⟨[q3,t,u]⟩,
if 1 ⩽t ⩽3,
⟨[q3,t,u], [¯q3,t,u]⟩,
if t ⩾4.
By applying Theorem 2.2, we have
ϕ3(q3,t,u) = λ2
2u−1−1λ2t+u−1,
ϕ3(¯q3,t,u) = λ2u−1λ2
2t+u−1−1
are the cycles in Λ3,∗. So, we obtain
Tr3([q3,t,u]) = [ϕ3(q3,t,u)] = [λ2
2u−1−1λ2t+u−1] = h2
u−1ht+u,
Tr3([¯q3,t,u]) = [ϕ3(¯q3,t,u)] = [λ2
2u−1λ2
2t+u−1−1] = huh2
t+u−1.
According to Theorem 2.1, we have
Ext3,2t+u+2u
A
(F2, F2) = ⟨huh2
t+u−1, h2
u−1ht+u⟩.
If t = 0 then huh2
u−1 = h2
uhu−1 = 0. If t = 1 then huh2
t+u−1 = h3
u = h2
u−1hu+1 =
h2
u−1ht+u. If t = 2 then huh2
t+u−1 = huh2
u+1 = 0. If t = 3 then huh2
t+u−1 =
huh2
u+2 = 0. Hence, from the above equalities we can easily see that Theorem 3.2.1
is true in this case.


## Page 9


ON THE DETERMINATION OF THE SINGER TRANSFER
9
3.2.3. The case n = 2s+u+1 + 2u+1 + 2u −3.
If u > 0 then µ(n) = 3, hence the iterated Kameko homomorphism
(f
Sq
0
∗)u : (QP3)2s+u+2u−3 →(QP3)2s+1
is also an isomorphism of GL3-modules. Hence, we need only to compute (QP3)GL3
2s+1.
According to Kameko [13], (QP3)2s+1 is a vector space with a basis consisting of
all the classes represented by the following monomials:
vs,1 = x2x2s+1−1
3
, vs,2 = x2s+1−1
2
x3, vs,3 = x1x2s+1−1
3
,
vs,4 = x1x2s+1−1
2
, vs,5 = x2s+1−1
1
x3, vs,6 = x2s+1−1
1
x2, for s ⩾1,
v1,7 = x1x2x2
3, v1,8 = x1x2
2x3, for s = 1,
vs,7 = x3
2x2s+1−3
3
, vs,8 = x3
1x2s+1−3
3
, vs,9 = x3
1x2s+1−3
2
,
vs,10 = x1x2x2s+1−2
2
, vs,11 = x1x2s+1−2
2
x3, vs,12 = x1x2
2x2s+1−3
3
,
vs,13 = x1x3
2x2s+1−4
3
, vs,14 = x3
1x2x2s+1−4
3
for s ⩾2
v15 = x3
1x4
2x3, for s = 2.
Set ¯p0 = v2,10 + v2,11 + v2,14 + v2,15. By a direct computation, we have
Proposition 3.2.4. For any integers s > 0, u ⩾0 and n = 2s+u+1 +2u+1 +2u −3,
we have
(QP3)GL3
n
=
(
⟨[ψu(¯p0)]⟩,
if s = 2,
0,
if s ̸= 2.
We set
¯cu = a(3.2u−1)
1
a(4.2u−1)
2
a(4.2u−1)
3
+ a(2.2u−1)
1
a(5.2u−1)
2
a(4.2u−1)
3
+ a(2.2u−1)
1
a(3.2u−1)
2
a(6.2u−1)
3
+ a(2.2u−1)
1
a(2.2u−1)
2
a(7.2u−1)
3
is an element in (P3)∗= Γ(a1, a2, a3). By a direct computation, we can see that
¯cu ∈P((P3)∗
2t+u+2u−3) and ⟨ψu(¯p0), ¯cu⟩= 1. So, we get
F2⊗GL3P((P3)∗
n) =
(
⟨[¯cu]⟩,
if s = 2,
0,
if s ̸= 2.
For u = 0, we have ¯c0 = a(2)
1 a(3)
2 a(3)
3
+ a(1)
1 a(4)
2 a(3)
3
+ a(1)
1 a(2)
2 a(5)
3
+ a(1)
1 a(1)
2 a(6)
3 .
A direct computation shows
ϕ3(a(2)
1 a(3)
2 a(3)
3 ) = λ2λ2
3 + λ1λ4λ3 + λ1λ3λ4,
ϕ3(a(1)
1 a(4)
2 a(3)
3 ) = λ1λ4λ3 + λ1λ3λ4 + λ1λ2λ5,
ϕ3(a(1)
1 a(2)
2 a(5)
3 ) = λ1λ2λ5 + λ2
1λ6,
ϕ3(a(1)
1 a(1)
2 a(6)
3 ) = λ2
1λ6.
Hence, we obtain ϕ3(¯c0) = λ2λ2
3. By Theorem 2.2, we have Tr3([¯c0]) = [λ2λ2
3] = c0.
Since [¯cu] = (f
Sq
0
∗)u([¯c0]), we get
Tr3([¯cu]) = Tr3((f
Sq
0)u([¯c0])) = (Sq0)uTr3([¯c0]) = (Sq0)u(c0) = cu.


## Page 10


10
NGUYỄN SUM
By Theorem 2.1, we have huhu+1 = 0. Hence,
Ext3,2s+u+1+2u+1+2u
A
(F2, F2) =
(
⟨huhu+1hu+3, cu⟩= ⟨cu⟩,
if s = 2,
⟨huhu+1hs+u+1⟩= 0,
if s ̸= 2.
Theorem 3.2.1 in this case follows from the above equalities.
3.2.4. The case of the generic degree.
In this subsection, we consider the degree
n = 2s+t+u + 2t+u + 2u −3,
with s, t, u non-negative integers.
The subcases either s = 0 or t = 0 have been determined in Subsections 3.2.1
and 3.2.2. The case s > 0 and t = 1 has been determined in Subsection 3.2.3. So,
we assume that s > 0 and t > 1.
The iterated homomorphism
(f
Sq
0
∗)u : (QP3)2s+t+u+2t+u+2u−3 →(QP3)2s+t+2t−2
is an isomorphism of GL3-modules. So, we need only to compute (QP3)GL3
2s+t+2t−2.
The subcase s = 1. Then n = 2t+1 + 2t −2. According to Kameko [13], (QP3)n
is the vector space with a basis consisting of all the classes represented by the
following monomials:
vt,1 = x2t−1
2
x2t+1−1
3
vt,2 = x2t+1−1
2
x2t−1
3
vt,3 = x2t−1
1
x2t+1−1
3
vt,4 = x2t−1
1
x2t+1−1
2
vt,5 = x2t+1−1
1
x2t−1
3
vt,6 = x2t+1−1
1
x2t−1
2
.
vt,7 = x1x2t−2
2
x2t+1−1
3
vt,8 = x1x2t+1−1
2
x2t−2
3
vt,9 = x2t+1−1
1
x2x2t−2
3
vt,10 = x1x2t−1
2
x2t+1−2
3
vt,11 = x1x2t+1−2
2
x2t−1
3
vt,12 = x2t−1
1
x2x2t+1−2
3
vt,13 = x3
1x2t+1−3
2
x2t−2
3
,
v2,14 = x3
1x3
2x4
3 for t = 2, and vt,14 = x3
1x2t−3
2
x2t+1−2
3
for t > 2.
By a direct computation using the above basis, we obtain
Proposition 3.2.5. For any integers t > 1, u ⩾0 and n = 2t+u+1 + 2t+u + 2u −3,
we have (QP3)GL3
n
= 0.
By Theorem 2.1 ht+uht+u+1 = 0, so we have
Ext3,2t+u+1+2t+u+2u
A
(F2, F2) = ⟨huht+uht+u+1⟩= 0.
Hence, from the above equalities, we can see that
Tr3 : F2⊗GL3P((P3)∗
2t+u+1+2t+u+2u−3) −→Ext3,2t+u+1+2t+u+2u
A
(F2, F2)
is a trivial isomorphism.
Now, suppose that s, t > 1 and n = 2s+t + 2t −2. From the results of Kameko
[13], we see that (QP3)n is the vector space of dimension 21 with a basis consisting
of all the classes represented by the following monomials:


## Page 11


ON THE DETERMINATION OF THE SINGER TRANSFER
11
vs,t,1 = x2t−1
2
x2s+t−1
3
vs,t,2 = x2s+t−1
2
x2t−1
3
vs,t,3 = x2t−1
1
x2s+t−1
3
vs,t,4 = x2t−1
1
x2s+t−1
2
vs,t,5 = x2s+t−1
1
x2t−1
3
vs,t,6 = x2s+t−1
1
x2t−1
2
vs,t,7 = x2t+1−1
2
x2s+t−2t−1
3
vs,t,8 = x2t+1−1
1
x2s+t−2t−1
3
vs,t,9 = x2t+1−1
1
x2s+t−2t−1
2
vs,t,10 = x1x2t−2
2
x2s+t−1
3
vs,t,11 = x1x2s+t−1
2
x2t−2
3
vs,t,12 = x2s+t−1
1
x2x2t−2
3
vs,t,13 = x1x2t−1
2
x2s+t−2
3
vs,t,14 = x1x2s+t−2
2
x2t−1
3
vs,t,15 = x2t−1
1
x2x2s+t−2
3
vs,t,16 = x1x2t+1−2
2
x2s+t−2t−1
3
vs,t,17 = x1x2t+1−1
2
x2s+t−2t−2
3
vs,t,18 = x2t+1−1
1
x2x2s+t−2t−2
3
vs,t,19 = x3
1x2s+t−3
2
x2t−2
3
vs,t,20 = x3
1x2t+1−3
2
x2s+t−2t−2
3
,
vs,2,21 = x3
1x3
2x2s+2−4
3
, for t = 2 and vs,t,21 = x3
1x2t−3
2
x2s+t−2
3
for t > 2.
We set
p3,s,t,u =
(P
1⩽j⩽21,j̸=13,15 ψu(vs,2,j),
if t = 2,
P
1⩽j⩽21 ψu(vs,t,j),
if t > 2.
By a direct computation using this basis, we get
Proposition 3.2.6. For any integers s, t > 1, u ⩾0 and n = 2s+t+u+2t+u+2u−3,
we have (QP3)GL3
n
= ⟨[p3,s,t,u]⟩.
By Theorem 2.1, we have
Ext3,2s+t+u+2t+u+2u
A
(F2, F2) = ⟨huht+uhs+t+u⟩.
Note that ψu(vs,t,1) = x2u−1
1
x2t+u−1
2
x2s+t+u−1
3
. Consider the element
q3,s,t,u = a(2u−1)
1
a(2t+u−1)
2
a(2s+t+u−1)
3
∈F2⊗GL3P((P3)∗
n).
Since ⟨p3,s,t,u, q3,s,t,u⟩= 1, from Proposition 3.2.6, we obtain
F2⊗GL3P((P3)∗
n) = ⟨[q3,s,t,u]⟩.
It is easy to see that ϕ3(q3,s,t,u) = λuλt+uλs+t+u, hence using Theorem 2.2 we
get
Tr3([q3,s,t,u]) = [λuλt+uλs+t+u] = huht+uhs+t+u.
Theorem 3.2.1 is completely proved.
4. Determination of Tr4 in some internal degrees
In this section, we explicitly determined Tr4 in some internal degrees. Our main
result is the following.
Theorem 4.1. Let s be a positive integer and let n be one of the degrees 2s+1 −1,
2s+1 −2, 2s+1 −3. If n ̸= 61 and n ̸= 126, then the homomorphism
Tr4 : F2⊗GL4P((P4)∗
n) −→Ext4,n+4
A
(F2, F2)
is an isomorphism. If either n = 61 or n = 126, then Tr4 is a monomorphism but
it is not an epimorphism.
We prove the theorem by computing the space (QP4)GL4
n
.


## Page 12


12
NGUYỄN SUM
4.1. The case n = 2s+1 −3.
Proposition 4.1.1 (see [20, 28]). Let n = 2s+1 −3 with s a positive integer. Then,
the dimension of the F2-vector space (QP4)n is determined by the following table:
n = 2s+1 −3
s = 1
s = 2
s = 3
s ⩾4
dim(QP4)n
4
15
35
45
A basis for (QP4)n is the set consisting of all the classes represented monomials
aj = as,j which are determined as follows:
For s = 1, a1,1 = x4, a1,2 = x3, a1,3 = x2, a1,4 = x1.
For s ⩾2,
as,1 = x2s−1−1
2
x2s−1−1
3
x2s−1
4
as,2 = x2s−1−1
2
x2s−1
3
x2s−1−1
4
as,3 = x2s−1
2
x2s−1−1
3
x2s−1−1
4
as,4 = x2s−1−1
1
x2s−1−1
3
x2s−1
4
as,5 = x2s−1−1
1
x2s−1
3
x2s−1−1
4
as,6 = x2s−1−1
1
x2s−1−1
2
x2s−1
4
as,7 = x2s−1−1
1
x2s−1−1
2
x2s−1
3
as,8 = x2s−1−1
1
x2s−1
2
x2s−1−1
4
as,9 = x2s−1−1
1
x2s−1
2
x2s−1−1
3
as,10 = x2s−1
1
x2s−1−1
3
x2s−1−1
4
as,11 = x2s−1
1
x2s−1−1
2
x2s−1−1
4
as,12 = x2s−1
1
x2s−1−1
2
x2s−1−1
3
For s = 2, a2,13 = x1x2x3x2
4, a2,14 = x1x2x2
3x4, a2,15 = x1x2
2x3x4.
For s ⩾3,
as,13 = x1x2s−1−2
2
x2s−1−1
3
x2s−1
4
as,14 = x1x2s−1−2
2
x2s−1
3
x2s−1−1
4
as,15 = x1x2s−1−1
2
x2s−1−2
3
x2s−1
4
as,16 = x1x2s−1−1
2
x2s−1
3
x2s−1−2
4
as,17 = x1x2s−1
2
x2s−1−2
3
x2s−1−1
4
as,18 = x1x2s−1
2
x2s−1−1
3
x2s−1−2
4
as,19 = x2s−1−1
1
x2x2s−1−2
3
x2s−1
4
as,20 = x2s−1−1
1
x2x2s−1
3
x2s−1−2
4
as,21 = x2s−1−1
1
x2s−1
2
x3x2s−1−2
4
as,22 = x2s−1
1
x2x2s−1−2
3
x2s−1−1
4
as,23 = x2s−1
1
x2x2s−1−1
3
x2s−1−2
4
as,24 = x2s−1
1
x2s−1−1
2
x3x2s−1−2
4
as,25 = x1x2s−1−1
2
x2s−1−1
3
x2s−2
4
as,26 = x1x2s−1−1
2
x2s−2
3
x2s−1−1
4
as,27 = x1x2s−2
2
x2s−1−1
3
x2s−1−1
4
as,28 = x2s−1−1
1
x2x2s−1−1
3
x2s−2
4
as,29 = x2s−1−1
1
x2x2s−2
3
x2s−1−1
4
as,30 = x2s−1−1
1
x2s−1−1
2
x3x2s−2
4
For s = 3,
a3,31 = x3
1x3
2x5
3x2
4
a3,32 = x3
1x5
2x2
3x3
4
a3,33 = x3
1x5
2x3
3x2
4
a3,34 = x3
1x3
2x3
3x4
4
a3,35 = x3
1x3
2x4
3x3
4
For s ⩾4,
as,31 = x3
1x2s−1−3
2
x2s−1−2
3
x2s−1
4
as,32 = x3
1x2s−1−3
2
x2s−1
3
x2s−1−2
4
as,33 = x3
1x2s−1
2
x2s−1−3
3
x2s−1−2
4
as,34 = x2s−1
1
x3
2x2s−1−3
3
x2s−1−2
4
as,35 = x3
1x2s−1−3
2
x2s−1−1
3
x2s−2
4
as,36 = x3
1x2s−1−3
2
x2s−2
3
x2s−1−1
4
as,37 = x3
1x2s−1−1
2
x2s−1−3
3
x2s−2
4
as,38 = x2s−1−1
1
x3
2x2s−1−3
3
x2s−2
4
as,39 = x3
1x2s−1−1
2
x2s−3
3
x2s−1−2
4
as,40 = x3
1x2s−3
2
x2s−1−2
3
x2s−1−1
4
as,41 = x3
1x2s−3
2
x2s−1−1
3
x2s−1−2
4
as,42 = x2s−1−1
1
x3
2x2s−3
3
x2s−1−2
4
as,43 = x7
1x2s−5
2
x2s−1−3
3
x2s−1−2
4
For s = 4, a4,44 = x7
1x7
2x9
3x6
4, a4,45 = x7
1x7
2x7
3x8
4.
For s ⩾5, as,44 = x7
1x2s−1−5
2
x2s−3
3
x2s−1−2
4
, as,45 = x7
1x2s−1−5
2
x2s−1−3
3
x2s−2
4
.


## Page 13


ON THE DETERMINATION OF THE SINGER TRANSFER
13
Proposition 4.1.2. Let s be a positive integer. Then, (QP4)GL4
2s+1−3 = 0.
For simplicity, we prove the proposition in detail for s ⩾5. The other cases can
be proved by the similar computations.
For any monomials z1, z2, . . . , zm in Pk and for a subgroup G ⊂GLk, we denote
G(z1, z2, . . . , zm) the G-submodule of QPk generated by the set {[zi] : 1 ⩽i ⩽m}.
We have the following.
Lemma 4.1.3. i) For any s ⩾5, there is a direct summand decomposition of the
Σ4-modules:
(QP4)2s+1−3 = Σ4(as,1) ⊕Σ4(as,13) ⊕Σ4(as,31) ⊕Σ4(as,25, as,35, as,43).
ii) Σ4(as,1)Σ4 = ⟨[p4,s,1]⟩, with p4,s,1 = P12
j=1 as,j.
iii) Σ4(as,13)Σ4 = ⟨[p4,s,2]⟩, with p4,s,2 = P24
j=13 as,j.
iv) Σ4(as,31)Σ4 = ⟨[p4,s,3]⟩, with p4,s,3 = P34
j=31 as,j.
v) Σ4(as,25, as,35, as,43)Σ4 = ⟨[p4,s,4]⟩, with
p4,s,4 =
30
X
j=25
as,j +
43
X
j=39
as,j + as,45.
Proof. We obtain Part i) by a simple computation using Proposition 4.1.1. We
prove Part v) in detail. The others can be proved by the similar computations. By
a simple computation we see that the set {[as,j] : j = 25, . . . , 30, 35 . . . , 45} is a
basis for Σ4(as,25, as,35, as,43). Suppose [f] ∈Σ4(as,25, as,35, as,43)Σ4, then
f ≡
30
X
j=25
γjas,j +
45
X
j=35
γjas,j
with γj ∈F2. By a direct computation, we get
ρ1(f) + f ≡(γ25 + γ28)(as,25 + as,28) + (γ26 + γ29)(as,26 + as,29)
+ (γ27 + γ41)as,35 + (γ27 + γ40)as,36 + (γ37 + γ38)(as,37 + as,38)
+ (γ39 + γ42)(as,39 + as,42) + (γ41 + γ43)as,44 + (γ40 + γ43)as,45 ≡0,
ρ2(f) + f ≡(γ26 + γ27)(as,26 + as,27) + (γ28 + γ30)(as,28 + as,30)
+ (γ35 + γ37)(as,35 + as,37) + (γ29 + γ36 + γ40)(as,36 + as,40)
+ (γ39 + γ41)(as,39 + as,41) + (γ42 + γ43 + γ44)(as,43 + as,44)
+ (γ29 + γ42)(as,38 + as,45) ≡0,
ρ3(f) + f ≡(γ25 + γ26)(as,25 + as,26) + (γ28 + γ29)(as,28 + as,29)
+ (γ35 + γ36)(as,35 + as,36) + (γ30 + γ37 + γ39)(as,37 + as,39)
+ (γ30 + γ38 + γ42)(as,38 + as,42) + (γ40 + γ41)(as,40 + as,41)
+ (γ30 + γ44 + γ45)(as,44 + as,45) ≡0.
The above equalities imply γj = 0 for j = 35, 36, 37, 38, 44 and γj = γ25 for j ̸=
35, 36, 37, 38, 44. The lemma is proved.
□
Proof of Proposition 4.1.2. Let f ∈P4 such that [f] ∈(QP4)GL4
2s+1−3. Since Σ4 ⊂
GL4, we have [f] ∈(QP4)Σ4
2s+1−3. Then, f ≡P4
j=1 γjp4,s,j with γj ∈F2. By a


## Page 14


14
NGUYỄN SUM
direct computation, we get
ρ4(f) + f ≡(γ1 + γ4)as,3 + γ1as,9 + (γ2 + γ3)as,15
+ γ2as,21 + other terms ≡0.
The last equality implies γj = 0 for j = 1, 2, 3, 4. The proposition follows.
□
From Theorem 2.1, we see that Ext4,2s+1+1
A
(F2, F2) = 0 for any s ̸= 5 and
Ext4,65
A
(F2, F2) = ⟨D3(0)⟩. Hence, Theorem 4.1 holds for n = 2s+1 −3.
4.2. The case n = 2s+1 −2.
Since Kameko’s homomorphism in the degree 2s+1 −2,
(f
Sq
0
∗)2s+1−2 : (QP4)2s+1−2 →(QP4)2s−3
is an epimorphism of GL4-modules, using Proposition 4.1.2, we have
(QP4)GL4
2s+1−2 ⊂
 Ker(f
Sq
0
∗)2s+1−2
GL4.
From [20, 28], we have the following.
Proposition 4.2.1 (see [20, 28]). Let s be a positive integer. Then,
dim
 Ker(f
Sq
0
∗)2s+1−2

=





6,
if s = 1,
20,
if s = 2,
35
if s ⩾3.
A basis for
 Ker(f
Sq
0
∗)2s+1−2

is the set consisting of all the classes represented
monomials bj = bs,j which are determined as follows:
For s ⩾1,
bs,1 = x2s−1
3
x2s−1
4
bs,2 = x2s−1
2
x2s−1
4
bs,3 = x2s−1
2
x2s−1
3
bs,4 = x2s−1
1
x2s−1
4
bs,5 = x2s−1
1
x2s−1
3
bs,6 = x2s−1
1
x2s−1
2
For s ⩾2,
bs,7 = x2x2s−2
3
x2s−1
4
bs,8 = x2x2s−1
3
x2s−2
4
bs,9 = x2s−1
2
x3x2s−2
4
bs,10 = x1x2s−2
3
x2s−1
4
bs,11 = x1x2s−1
3
x2s−2
4
bs,12 = x1x2s−2
2
x2s−1
4
bs,13 = x1x2s−2
2
x2s−1
3
bs,14 = x1x2s−1
2
x2s−2
4
bs,15 = x1x2s−1
2
x2s−2
3
bs,16 = x2s−1
1
x3x2s−2
4
bs,17 = x2s−1
1
x2x2s−2
4
bs,18 = x2s−1
1
x2x2s−2
3
For s = 2, b2,19 = x1x2x2
3x2
4, b2,20 = x1x2
2x3x2
4.
For s ⩾3,
bs,19 = x3
2x2s−3
3
x2s−2
4
bs,20 = x3
1x2s−3
3
x2s−2
4
bs,21 = x3
1x2s−3
2
x2s−2
4
bs,22 = x3
1x2s−3
2
x2s−2
3
bs,23 = x1x2
2x2s−4
3
x2s−1
4
bs,24 = x1x2
2x2s−1
3
x2s−4
4
bs,25 = x1x2s−1
2
x2
3x2s−4
4
bs,26 = x2s−1
1
x2x2
3x2s−4
4
bs,27 = x1x2x2s−2
3
x2s−2
4
bs,28 = x1x2s−2
2
x3x2s−2
4
bs,29 = x3
1x5
2x2s−6
3
x2s−4
4
bs,30 = x1x2
2x2s−3
3
x2s−2
4
bs,31 = x1x3
2x2s−4
3
x2s−2
4
bs,32 = x1x3
2x2s−2
3
x2s−4
4
bs,33 = x3
1x2x2s−4
3
x2s−2
4
bs,34 = x3
1x2x2s−2
3
x2s−4
4
For s = 3, b3,35 = x3
1x3
2x4
3x4
4, and for s ⩾4, bs,35 = x3
1x2s−3
2
x2
3x2s−4
4
.


## Page 15


ON THE DETERMINATION OF THE SINGER TRANSFER
15
We set
p4,s =
(
x1x2x6
3x6
4 + x3
1x3
2x4
3x4
4,
if s = 3,
P35
j=1 bs,j
if s ⩾4.
By a direct computation using Proposition 4.2.1, one gets the following.
Proposition 4.2.2. Let s be a positive integer. Then,
 Ker(f
Sq
0
∗)2s+1−2
GL4 =
(
0,
if s ⩽2,
⟨[p4,s]⟩
if s ⩾3.
For simplicity, we will prove this proposition in detail for s ⩾4. The others can
be proved by the similar computations. We have the following.
Lemma 4.2.3. i) For any s ⩾4, there is a direct summand decomposition of the
Σ4-modules:
 Ker(f
Sq
0
∗)2s+1−2 = Σ4(bs,1) ⊕Σ4(bs,7) ⊕Σ4(bs,19) ⊕Σ4(bs,23) ⊕Σ4(bs,29, bs,30).
ii) Σ4(bs,1)Σ4 = ⟨[¯p4,s,1]⟩, with ¯p4,s,1 = P6
j=1 bs,j.
iii) Σ4(bs,7)Σ4 = ⟨[¯p4,s,2]⟩, with ¯p4,s,2 = P18
j=7 bs,j.
iv) Σ4(bs,19)Σ4 = ⟨[¯p4,s,3]⟩, with ¯p4,s,3 = P22
j=19 bs,j.
v) Σ4(bs,23)Σ4 = ⟨[¯p4,s,4]⟩, with ¯p4,s,4 = P26
j=23 bs,j.
vi) Σ4(bs,29, as,30)Σ4 = ⟨[¯p4,s,5], [¯p4,s,6]⟩, where
¯p4,s,5 =
29
X
j=27
bs,j, ¯p4,s,6 =
35
X
j=30
bs,j.
Proof. From Proposition 4.2.1 we easily obtain Part i). Now, we prove Part vi) in
detail. The others can be proved by the similar computations. By a direct compu-
tation we see that the set {[bs,j] : j = 27 ⩽j ⩽35} is a basis for Σ4(bs,29, bs,30).
Suppose [f] ∈Σ4(bs,29, bs,30)Σ4, then f ≡P35
j=27 γjbs,j with γj ∈F2. By a direct
computation, we obtain
ρ1(f) + f ≡(γ28 + γ29 + γ30 + γ35)bs,27 + (γ31 + γ33)(bs,31 + bs,33)
+ (γ32 + γ34)(bs,32 + bs,34) ≡0,
ρ2(f) + f ≡(γ27 + γ28 + γ32 + γ33)(bs,27 + bs,28)
+ (γ30 + γ31)(bs,30 + bs,31) + (γ34 + γ35)(bs,34 + bs,35) ≡0,
ρ3(f) + f ≡(γ28 + γ29 + γ30 + γ35)bs,27 + (γ31 + γ32)(bs,31 + bs,32)
+ (γ33 + γ34)(bs,33 + bs,34) ≡0.
The above equalities imply γj = γ27 for j = 27, 28, 29 and γj = γ30 for 30 ⩽j ⩽35.
The lemma is proved.
□
Remark 4.2.4. For s = 3, Parts i) to v) of Lemma 4.2.3 hold. We replace Part
vi) with Σ4(b3,29, a3,30)Σ4 = ⟨[p4,3]⟩.
Proof of Proposition 4.2.2. Let f ∈P4 such that [f] ∈Ker(f
Sq
0
∗)GL4
2s+1−2. Then, [f] ∈
Ker(f
Sq
0
∗)Σ4
2s+1−2. Hence, f ≡P6
j=1 γj ¯p4,s,j with γj ∈F2. By a direct computation,


## Page 16


16
NGUYỄN SUM
we have
ρ4(f) + f ≡(γ1 + γ2)(bs,2 + bs,3) + (γ2 + γ4)(bs,7 + bs,8) + (γ2 + γ5)bs,9
+ (γ2 + γ3)(bs,14 + bs,15) + (γ3 + γ6)bs,19 + (γ4 + γ6)bs,25
+ (γ2 + γ3 + γ4 + γ5)bs,27 + (γ5 + γ6)(bs,31 + bs,32) ≡0.
The last equality implies γj = γ1 for 1 ⩽j ⩽6. The proposition follows.
□
From Theorem 2.1, we have
Ext4,2s+1+2
A
(F2, F2) =









0,
if s ⩽2,
⟨d0⟩
if s = 3,
⟨h2
0h2
6, D3(1)⟩
if s = 6,
⟨h2
0h2
s⟩
if s ⩾4, s ̸= 6.
Denote by q4,s ∈P((P ∗
4 )2s+1−2) the dual of p4,s ∈
 Ker(f
Sq
0
∗)2s+1−2
GL4. Then, we
have
F2⊗GL4P((P4)∗
2s+1−2) =
(
0,
if s ⩽2,
⟨[q4,s]⟩,
if s ⩾3.
From Hà [9] and Singer [18], we see that d0, h2
0h2
s ∈Im(Tr4), hence we get
Tr4([q4,s]) = [ϕ4(q4,s)] =
(
d0,
if s = 3,
h2
0h2
s,
if s > 3.
Theorem 4.1 holds for n = 2s+1 −2.
Remark 4.2.5. a) It is well-known that the space Im(Tr4) had been explicitly
determined from the works Bruner, Hà and Hưng [5], Chơn and Hà [8], Hà [9], Hưng
and Quỳnh [12], Nam [16] and Singer [18]. Hence, the proof that a certain element
is in Im(Tr4) is unnecessary (see [28]). To illustrate the fact that d0 ∈Im(Tr4), we
present the computations of Hà [9] for this result.
In [9, Page 102], Hà showed that the element q4,3 ∈P((P ∗
4 )14) can be determined
by
q4,3 = a(1)
1 a(1)
2 a(6)
3 a(6)
4
+ a(1)
1 a(2)
2 a(5)
3 a(6)
4
+ a(1)
1 a(3)
2 a(4)
3 a(6)
4
+ a(1)
1 a(4)
2 a(3)
3 a(6)
4
+ a(1)
1 a(5)
2 a(2)
3 a(6)
4
+ a(1)
1 a(6)
2 a(1)
3 a(6)
4
+ a(2)
1 a(1)
2 a(6)
3 a(5)
4
+ a(2)
1 a(2)
2 a(5)
3 a(5)
4
+ a(2)
1 a(3)
2 a(4)
3 a(5)
4
+ a(2)
1 a(4)
2 a(3)
3 a(5)
4
+ a(2)
1 a(5)
2 a(2)
3 a(5)
4
+ a(2)
1 a(6)
2 a(1)
3 a(5)
4
+ a(3)
1 a(1)
2 a(5)
3 a(5)
4
+ a(3)
1 a(2)
2 a(6)
3 a(3)
4
+ a(3)
1 a(3)
2 a(2)
3 a(6)
4
+ a(3)
1 a(4)
2 a(1)
3 a(6)
4
+ a(3)
1 a(4)
2 a(2)
3 a(5)
4
+ a(3)
1 a(4)
2 a(4)
3 a(3)
4
+ a(3)
1 a(6)
2 a(2)
3 a(3)
4
+ a(4)
1 a(1)
2 a(6)
3 a(3)
4
+ a(4)
1 a(2)
2 a(5)
3 a(3)
4
+ a(4)
1 a(3)
2 a(4)
3 a(3)
4
+ a(4)
1 a(4)
2 a(3)
3 a(3)
4
+ a(4)
1 a(5)
2 a(2)
3 a(3)
4
+ a(4)
1 a(6)
2 a(1)
3 a(3)
4
+ a(5)
1 a(1)
2 a(3)
3 a(5)
4
+ a(5)
1 a(2)
2 a(1)
3 a(6)
4
+ a(5)
1 a(2)
2 a(2)
3 a(5)
4
+ a(5)
1 a(2)
2 a(4)
3 a(3)
4
+ a(5)
1 a(3)
2 a(1)
3 a(5)
4
+ a(5)
1 a(3)
2 a(3)
3 a(3)
4
+ a(5)
1 a(5)
2 a(1)
3 a(3)
4
+ a(6)
1 a(1)
2 a(1)
3 a(6)
4
+ a(6)
1 a(1)
2 a(2)
3 a(5)
4
+ a(6)
1 a(1)
2 a(4)
3 a(3)
4
+ a(6)
1 a(2)
2 a(3)
3 a(3)
4 ,
By a direct computation we can easily verify that Sq1(q4,3) = 0, Sq2(q4,3) = 0,
Sq4(q4,3) = 0. Hence, q4,3 ∈P((P ∗
4 )14).


## Page 17


ON THE DETERMINATION OF THE SINGER TRANSFER
17
Chơn showed in his PhD thesis that ϕ4(q4,3) = ¯d0 + δ(λ2
3λ9 + λ3λ9λ3). Hence,
one gets Tr4([q4,3]) = [ϕ4(q4,3)] = [ ¯d0] = d0.
So, it is possible the algorithm in [29] is flawed.
b) In [12], Hưng and Quỳnh stated that p0 ∈Im(Tr4) but did not provide the
detailed proof. However, this result is explicitly proved in Chơn and Hà [8]. Hence,
the computations in [29] for p0 may be new but they are unnecessary for studying
Singer’s conjecture.
c) In [27], we have given a negative answer for Singer’s conjecture for the alge-
braic transfer. Hence, Singer’s algebraic transfer cannot be a tool for studying the
cohomology of Steenrod algebra. Therefore, the study of Singer’s algebraic transfer
is no longer necessary.
4.3. The case n = 2s+1 −1.
First, we recall the following.
Proposition 4.3.1 (see [20, 28]). Let n = 2s+1 −1 with s a positive integer. Then,
the dimension of the F2-vector space (QP4)n is determined by the following table:
n = 2s −1
s = 1
s = 2
s = 3
s = 4
s ⩾5
dim(QP4)n
14
35
75
89
85
A basis of (QP4)n has been given in [28]. For s ⩾k −2, we set
ηk,s =
k−1
X
m=1
X
1⩽i1<...<im⩽k
xi1x2
i2 . . . x2m−2
im−1 x2s+1−2m−1
im
∈(Pk)2s+1−1.
For k = 4, we denote
¯p4,s =
(
η4,s + x1x2
2x2
3x2
4,
if s = 2,
η4,s + x1x2
2x4
3x2s+1−8
4
,
if s ⩾3.
By a computation similar to the one in Proposition 4.2.1, one gets the following.
Proposition 4.3.2. Let s be a positive integer. Then,
(QP4)GL4
2s+1−1 =
(
0,
if s = 1,
⟨[¯p4,s]⟩,
if s ⩾2.
From Theorem 2.1, we have
Ext4,2s+1+3
A
(F2, F2) =
(
0,
if s = 1,
⟨h3
0hs+1⟩
if s ⩾2.
Denote ¯q4,s = a(0)
1 a(0)
2 a(0)
2 a(2s+1−1)
4
∈P((P ∗
4 )2s+1−1), for s ⩾2. It is easy to see
that ⟨[¯p4,s], [¯q4,s]⟩= 1 Hence, we obtain
F2⊗GL4P((P4)∗
2s+1−1) =
(
0,
if s = 1,
⟨[¯q4,s]⟩,
if s ⩾2.
By a simple computation, we have ϕ4(¯q4,s) = λ3
0λ2s+1−1. Hence, using Theorem
2.2, one gets
Tr4([¯q4,s]) = [ϕ4(¯q4,s)] = [λ3
0λ2s+1−1] = h3
0hs+1.
Theorem 4.1 is completely proved.


## Page 18


18
NGUYỄN SUM
Acknowledgment
This article was written when the author was visiting the Vietnam Institute
for Advanced Study in Mathematics (VIASM) from August to November 2017.
He would like to thank the VIASM for supporting the visit, convenient working
condition and for kind hospitality.
The author would like to express his warmest thanks to the referee for carefully
reading the manuscript and giving many criticisms and suggestions, which have led
to an improvement of the article’s exposition.
References
1. J.F. Adams, On the non-existence of elements of Hopf invariant one, Ann. of Math. 72 (1960),
20-104, MR0141119.
2. J. Adem, The iteration of the Steenrod squares in algebraic topology, Proc. Nat. Acad. Sci.
U.S.A. 38 (1952), 720-726, MR0050278.
3. J.M. Boardman, Modular representations on the homology of power of real projective space,
in: M. C. Tangora (Ed.), Algebraic Topology, Oaxtepec, 1991, in: Contemp. Math., vol. 146,
1993, pp. 49-70, MR1224907.
4. A.K. Bousfield, E.B. Curtis, D.M. Kan, D.G. Quillen, D.L. Rector and J.W. Schlesinger, The
mod p lower central series and the Adams spectral sequence, Topology 5 (1966), 331-342,
MR0199862 .
5. R.R. Bruner, L.M. Hà and N.H.V. Hưng, On behavior of the algebraic transfer, Trans. Amer.
Math. Soc. 357 (2005), 473-487, MR2095619.
6. P.H. Chơn and L.M. Hà, Lambda algebra and the Singer transfer, C. R. Math. Acad. Sci.
Paris 349 (2011) 21-23, MR2755689.
7. P.H. Chơn and L.M. Hà, On May spectral sequence and the algebraic transfer, Manuscripta
Math. 138 (2012) 141-160, MR2898751.
8. P. H. Chơn and L. M. Hà, On the May spectral sequence and the algebraic transfer II, Topology
Appl. 178 (2014) 372-383, MR3276753.
9. L.M. Hà, Sub-Hopf algebras of the Steenrod algebra and the Singer transfer, “Proceedings of
the International School and Conference in Algebraic Topology, Hà Nội 2004”, Geom. Topol.
Monogr., Geom. Topol. Publ., Coventry, vol. 11 (2007), 81-105, MR2402802.
10. N.H.V. Hưng, The weak conjecture on spherical classes, Math. Zeit. 231 (1999) 727-743,
MR1709493
11. N.H.V. Hưng, The cohomology of the Steenrod algebra and representations of the general
linear groups, Trans. Amer. Math. Soc. 357 (2005), 4065-4089, MR2159700.
12. N.H.V. Hưng and V. T. N. Quỳnh, The image of Singer’s fourth transfer, C. R. Math. Acad.
Sci. Paris 347 (2009) 1415-1418, MR2588792.
13. M.Kameko, Products of projective spaces as Steenrod modules, PhD. Thesis, The Johns Hop-
kins University, ProQuest LLC, Ann Arbor, MI, 1990. 29 pp. MR2638633.
14. W.H. Lin, Ext4,∗
A (Z/2, Z/2) and Ext5,∗
A (Z/2, Z/2), Topology Appl., 155 (2008) 459-496,
MR2380930.
15. N. Minami, The iterated transfer analogue of the new doomsday conjecture, Trans. Amer.
Math. Soc. 351 (1999) 2325-2351, MR1443884.
16. T.N. Nam, Transfert algébrique et action du groupe linéaire sur les puissances divisées modulo
2, Ann. Inst. Fourier (Grenoble) 58 (2008) 1785-1837, MR2445834.
17. F.P. Peterson, Generators of H∗(RP ∞× RP ∞) as a module over the Steenrod algebra, Ab-
stracts Amer. Math. Soc. No. 833 (1987) 55-89.
18. W.M. Singer,
The transfer in homological algebra,
Math. Zeit. 202 (1989) 493-523,
MR1022818.
19. N. E. Steenrod and D.B.A. Epstein, Cohomology operations, Annals of Mathematics Studies
50, Princeton University Press, Princeton N.J (1962), MR0145525.
20. N. Sum, The hit problem for the polynomial algebra of four variables, Quy Nhơn University,
Việt Nam, Preprint 2007, 240 pp., available online at: http://arxiv.org/abs/1412.1709.
21. N. Sum, The negative answer to Kameko’s conjecture on the hit problem, Adv. Math. 225
(2010), 2365-2390, MR2680169.


## Page 19


ON THE DETERMINATION OF THE SINGER TRANSFER
19
22. N. Sum, On the Peterson hit problem of five variables and its applications to the fifth Singer
transfer, East-West J. of Mathematics, 16 (2014) 47-62, MR3409252.
23. N. Sum, On the Peterson hit problem, Adv. Math. 274 (2015) 432-489, MR3318156.
24. C.T.C. Wall, Generators and relations for the Steenrod algebra, Annals of Math. 72 (1960),
429-444, MR0116326.
25. J.S.P. Wang On the cohomology of the mod-2 Steenrod algebra and the non-existence of
mappings of Hopf invariant one, Illinois Jour. Math. 11 (1967), 480-490, MR0214065.
26. R.M.W. Wood, Steenrod squares of polynomials and the Peterson conjecture, Math. Proc.
Cambriges Phil. Soc. 105 (1989), 307-309, MR0974986.
27. N. Sum, A counter-example to Singer’s conjecture for the algebraic transfer. Preprint 2024,
available online at: http://arxiv.org/abs/2408.06669.
28. N. Sum, An application of the hit problem to the algebraic transfer, Preprint 2025, 83 pp.,
available online at http://arxiv.org/abs/2505.23218.
29. Đ.
V.
Phúc,
Computational
Approaches
to
the
Singer
Transfer:
Preimages
in
the
Lambda
Algebra
and
Gk-Invariant
Theory,
Preprint
2025,
available
online
at:
https://arxiv.org/abs/2507.10108.
Department of Mathematics, Quy Nhơn University, 170 An Dương Vương, Quy Nhơn,
Bình Định, Viet Nam
Email address: nguyensum@qnu.edu.vn

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1710_07895_on_the_determination_of_the_singer_transfer
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1710_07895_ON_THE_DETERMINATION_OF_THE_SINGER_TRANSFER.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

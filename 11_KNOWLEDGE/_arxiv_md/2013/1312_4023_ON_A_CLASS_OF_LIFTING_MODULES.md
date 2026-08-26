---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1312.4023
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1312.4023_On_A_Class_of_Lifting_Modules

> Source: 1312.4023_On_A_Class_of_Lifting_Modules.pdf

> Pages: 13

---


## Page 1


arXiv:1312.4023v1  [math.RA]  14 Dec 2013
ON A CLASS OF LIFTING MODULES
HATICE INANKIL, SAIT HALICIO ˘GLU, AND ABDULLAH HARMANCI
Abstract. In this paper, we introduce principally δ-lifting modules which
are analogous to δ-lifting modules and principally δ-semiperfect modules as a
generalization of δ-semiperfect modules and investigate their properties.
1. Introduction
Throughout this paper all rings have an identity, all modules considered are
unital right modules. Let M be a module and N, P be submodules of M. We call
P a supplement of N in M if M = P + N and P ∩N is small in P. A module M
is called supplemented if every submodule of M has a supplement in M. A module
M is called lifting if, for all N ≤M, there exists a decomposition M = A ⊕B such
that A ≤N and N ∩B is small in M. Supplemented and lifting modules have
been discussed by several authors (see [2, 4, 6]) and these modules are useful in
characterizing semiperfect and right perfect rings (see [4, 7]).
In this note, we study and investigate principally δ-lifting modules and princi-
pally δ-semiperfect modules. A module M is called principally δ-lifting if for each
cyclic submodule has the δ-lifting property, i.e., for each m ∈M, M has a decom-
position M = A ⊕B with A ≤mR and mR ∩B is δ-small in B, where B is called
a δ-supplement of mR. A module M is called principally δ-semiperfect if, for each
m ∈M, M/mR has a projective δ-cover. We prove that if M1 is semisimple, M2
is principally δ-lifting, M1 and M2 are relatively projective, then M = M1 ⊕M2 is
a principally δ-lifting module. Among others we also prove that for a principally
δ-semiperfect module M, M is principally δ-supplemented, each factor module of
M is principally δ-semiperfect, hence any homomorphic image and any direct sum-
mand of M is principally δ-semiperfect. As an application, for a projective module
M, it is shown that M is principally δ-semiperfect if and only if it is principally
δ-lifting, and therefore a ring R is principally δ-semiperfect if and only if it is
principally δ-lifting.
In section 2, we give some properties of δ-small submodules that we use in the
paper, and in section 3, principally δ-lifting modules are introduced and various
properties of principally δ-lifting and δ-supplemented modules are obtained.
In
section 4, principally δ-semiperfect modules are deﬁned and characterized in terms
of principally δ-lifting modules.
In what follows, by Z, Q, Zn and Z/Zn we denote, respectively, integers, ra-
tional numbers, the ring of integers and the Z-module of integers modulo n. For
unexplained concepts and notations, we refer the reader to [1, 4].
2000 Mathematics Subject Classiﬁcation. 16U80.
Key words and phrases. lifting modules, δ-lifting modules, semiperfect modules, δ-semiperfect
modules.
1


## Page 2


2
HATICE INANKIL, SAIT HALICIO ˘GLU, AND ABDULLAH HARMANCI
2. δ-Small Submodules
Following Zhou [9], a submodule N of a module M is called a δ-small submodule
if, whenever M = N + X with M/X singular, we have M = X. We begin by
stating the next lemma which is contained in [9, Lemma 1.2 and 1.3].
Lemma 2.1. Let M be a module. Then we have the following.
(1) If N is δ-small in M and M = X + N, then M = X ⊕Y for a projective
semisimple submodule Y with Y ⊆N.
(2) If K is δ-small in M and f : M →N is a homomorphism, then f(K) is
δ-small in N. In particular, if K is δ-small in M ⊆N, then K is δ-small
in N.
(3) Let K1 ⊆M1 ⊆M, K2 ⊆M2 ⊆M and M = M1 ⊕M2. Then K1 ⊕K2 is
δ-small in M1 ⊕M2 if and only if K1 is δ-small in M1 and K2is δ-small
in M2.
(4) Let N, K be submodules of M with K is δ-small in M and N ≤K. Then
N is also δ-small in M.
Lemma 2.2. Let M be a module and m ∈M. Then the following are equivalent.
(1) mR is not δ-small in M.
(2) There is a maximal submodule N of M such that m ̸∈N and M/N singular.
Proof. (1) ⇒(2) Let Γ := {B ≤M | B ̸= M, mR + B = M, M/B singular}.
Since mR is not δ-small in M, there exists a proper submodule B of M such that
mR + B = M and M/B singular. So Γ is non empty. Let Λ be a nonempty totally
ordered subset of Γ and B0 := ∪B∈ΛB. If m is in B0 then there is a B ∈Λ with
m ∈B. Then B = mR + B = M which is a contraction. So we have m /∈B0 and
B0 ̸= M. Since mR + B0 = M and M/B0 singular, B0 is upper bound in Γ. By
Zorn’s Lemma, Γ has a maximal element, say N. If N is a maximal submodule of
M there is nothing to do. Assume that there exists a submodule K containing N
properly. Since N is maximal in Γ, K is not in Γ. Since M = mR+N and N ≤K,
so M = mR + K. M/K is singular as a homomorphic image of singular module
M/N. Hence K must belong to the Γ. This is the required contradiction.
(2) ⇒(1) Let N be a maximal submodule with m ∈M \ N and M/N singular.
We have M = mR + N. Then mR is not δ-small in M.
□
Let A and B be submodules of M with A ≤B. A is called a δ-cosmall submodule
of B in M if B/A is δ-small in M/A. Let A be a submodule of M. A is called
a δ-coclosed submodule in M if A has no proper δ-cosmall submodules in M. A
submodule A is called δ-coclosure of B in M if A is δ-coclosed submodule of M and
it is δ-cosmall submodule of B. Equivalently, for any submodule C ≤A with A/C
is δ-small in M/C implies C = A and B/A is δ-small in M/A. Note that δ-coclosed
submodules need not always exist.


## Page 3


ON A CLASS OF LIFTING MODULES
3
Lemma 2.3. Let A and B be submodules of M with A ≤B. Then we have:
(1) A is δ-cosmall submodule of B in M if and only if M = A + L for any
submodule L of M with M = B + L and M/L singular.
(2) If A is δ-small and B is δ-coclosed in M, then A is δ-small in B.
Proof. (1) Necessity: Let M = B + L and M/L be singular. We have M/A =
B/A + (L + A)/A and M/(L + A) is singular as homomorphic image of singular
module M/L. Since B/A is δ-small, M/A = (L + A)/A or M = L + A.
Suﬃciency: Let M/A = B/A + K/A and M/K singular. Then M = B + K. By
hypothesis, M = A + K and so M = K. Hence A is δ-cosmall submodule of B in
M.
(2) Assume that A is δ-small submodule of M and B is δ-coclosed in M.
Let
B = A + K with B/K singular.
Since B is δ-coclosed in M, to complete the
proof, by part (1) it suﬃces to show that K is δ-small submodule of B in M. Let
M = B + L with M/L singular. By assumption, M = A + K + L = K + L since
M/(K + L) is singular. By (1), K is δ-small submodule of B in M.
□
Lemma 2.4. Let A, B and C be submodules of M with M = A + C and A ⊆B.
If B ∩C is a δ-small submodule of M, then A is a δ-cosmall submodule of B in M.
Proof. Let M/A = B/A + L/A with M/L singular. We have M = B + L and
B = A + (B ∩C). Then M = A + (B ∩C) + L = (B ∩C) + L. Hence M = L since
B ∩K is δ-small in M and M/L is singular. Hence B/A is δ-small in M/A. Thus
A is δ-cosmall submodule of B in M.
□
3. Principally δ-Lifting Modules
In this section, we study and investigate some properties of principally δ-lifting
modules. The following deﬁnition is motivated by [9, Lemma 3.4] and Lemma 3.4.
Deﬁnition 3.1. A module M is called ﬁnitely δ-lifting if for any ﬁnitely generated
submodule A of M has the δ-lifting property, that is, there is a decomposition
M = N ⊕S with N ≤A and A∩S is δ-small in S. In this case A∩S is δ-small in S
if and only if A∩S is δ-small in M. A module M is called principally δ-lifting if for
each cyclic submodule has the principally δ-lifting property, i.e., for each m ∈M,
M has a decomposition M = A ⊕B with A ≤mR and mR ∩B is δ-small in B.
Example 3.2. Every submodule of any semisimple module satisﬁes principally
δ-lifting property.
Example 3.3. Let p be a prime integer and n any positive integer. Then the
Z-module M = Z/Zpn is a principally δ-lifting module.


## Page 4


4
HATICE INANKIL, SAIT HALICIO ˘GLU, AND ABDULLAH HARMANCI
Lemma 3.4 is proved in [7] and [9].
Lemma 3.4. The following are equivalent for a module M.
(1) M is ﬁnitely δ-lifting.
(2) M is principally δ-lifting.
Let M be a module and N a submodule of M.
A submodule L is called a
δ-supplement of N in M if M = N + L and N ∩L is δ-small in L(therefore in M).
Proposition 3.5. Let M be a principally δ-lifting module. The we have:
(1) Every direct summand of M is a principally δ-lifting module.
(2) Every cyclic submodule C of M has a δ-supplement S which is a direct
summand, and C contains a complementary summand of S in M.
Proof. (1) Let K be a direct summand of M and k ∈K. Then M has a decom-
position M = N ⊕S with N ≤kR and kR ∩S is δ-small in M. It follows that
K = N ⊕(K ∩S), and kR ∩(K ∩S) ≤kR ∩S is δ-small in M and so kR ∩(K ∩S)
is δ-small in K. Therefore K is a principally δ-lifting module.
(2) Assume that M is a principally δ-lifting module and C is a cyclic submodule
of M. Then we have M = N ⊕S, where N ≤C and C ∩S is δ-small in M. Hence
M = N + S ≤C + S ≤M, we have M = C + S. Since S is direct summand and
C ∩S is δ-small in M, C ∩S is δ-small in S. Therefore S is a δ-supplement of C
in M.
□
Theorem 3.6. The following are equivalent for a module M.
(1) M is a principally δ-lifting module.
(2) Every cyclic submodule C of M can be written as C = N ⊕S, where N is
direct summand and S is δ-small in M.
(3) For every cyclic submodule C of M, there is a direct summand A of M with
A ≤C and C/A is δ-small in M/A.
(4) Every cyclic submodule C of M has a δ-supplement K in M such that C∩K
is a direct summand in C.
(5) For every cyclic submodule C of M, there is an idempotent e ∈End(M)
with eM ≤C and (1 −e)C is δ-small in (1 −e)M.
(6) For each m ∈M, there exist ideals I and J of R such that mR = mI ⊕mJ,
where mI is direct summand of M and mJ is δ-small in M.
Proof. (1)⇒(2) Let C be a cyclic submodule of M. By hypothesis there exist N
and S submodules of M such that N ≤C, C ∩S is δ-small in M and M = N ⊕S.
Then we have C = N ⊕(C ∩S).


## Page 5


ON A CLASS OF LIFTING MODULES
5
(2) ⇒(3) Let C be a cyclic submodule of M . By hypothesis, C = N ⊕S, where
N is direct summand and S is δ-small in M. Let π : M →M/N be the natural
projection.
Since S is δ-small in M, we have π(S) is δ-small in M/N.
Since
π(S) ∼= S ∼= C/N, C/N is δ-small in M/N.
(3) ⇒(4) Let C be a cyclic submodule of M. By hypothesis, there is a direct
summand A ≤M with A ≤C and C/A is δ-small in M/A. Let M = A ⊕A′ .
Hence C = A ⊕(A′ ∩C). Let σ : M/A →A′ denote the obvious isomorphism.
Then σ(C/A) = A′ ∩C is δ-small in A′.
(4) ⇒(5) Let C be any cyclic submodule of M and K ≤M such that C∩K is direct
summand of C, M = C + K and C ∩K is δ-small in K . So C = (C ∩K) ⊕X for
some X ≤C . Then M = X+(C∩K)+K = X⊕K . Let e : M →X ; e(x+k) = x
and (1 −e) : M →K ; e(x + k) = k are projection maps. e(M) ≤X ≤C and
(1 −e)C = C ∩(1 −e)M = C ∩K is δ-small in (1 −e)M.
(5) ⇒(6) Let mR be any cyclic submodule of M . By hypothesis, there exists an
idempotent e ∈End(M) such that eM ≤mR, M = eM ⊕(1−e)M and (1−e)mR is
δ-small in (1−e)M. Note that (mR)∩((1−e)M) = (1−e)mR ( for if m = em1+y,
where em1 ∈eM, y ∈(mR) ∩((1 −e)M). Then (1 −e)m = em1 + (1 −e)y = y
and so (1 −e)mR ≤(mR) ∩((1 −e)M). Let mr = (1 −e)m′ ∈(mR) ∩((1 −e)M).
Then mr = (1 −e)mr ∈(1 −e)mR. So (mR) ∩((1 −e)M) ≤(1 −e)mR. Thus
(mR) ∩((1 −e)M) = (1 −e)mR ). So mR = eM ⊕(1 −e)mR. Let I = {r ∈R :
mr ∈eM} and J = {t ∈R : mt ∈(1 −e)mR}. Then mR = mI ⊕mJ , mI = eM
and mJ = (1 −e)mR is δ-small in (1 −e)M.
(6) ⇒(1) Let m ∈M. By hypothesis, there exist ideals I and J of R such that
mR = mI ⊕mJ, where mI is direct summand and mJ is δ-small in M.
Let
M = mI ⊕K for some submodule K. Since K ∩mR ∼= mJ and mJ is δ-small in
M , M is principally δ-lifting.
□
Note that every lifting module is principally δ-lifting.
There are principally
δ-lifting modules but not lifting.
Example 3.7. Let M be the Z-module Q and m ∈M. It is well known that
every cyclic submodule mR of M is small, therefore δ-small in M. Hence M is a
principally δ-lifting Z-module. If N is a nonsmall proper submodule of M, then N
is neither direct summand nor contains a direct summand of M. It follows that M
is not a lifting Z-module.
It is clear that every δ-lifting module is principally δ-lifting. However the converse
is not true.
Example 3.8. Let R and T denote the rings in [9, Example 4.1], where


## Page 6


6
HATICE INANKIL, SAIT HALICIO ˘GLU, AND ABDULLAH HARMANCI
R =
∞
P
i=1
L Z2 + Z2.1 = {(f1, f2, . . . , fn, f, f, . . . ) ∈
∞
Q
i=1
Z2}
and T =
("
x
y
o
x
#
: x ∈R, y ∈Soc(R)
)
. Then Radδ(T ) =
"
0
Soc(R)
0
0
#
and T/Radδ(T ) is not semisimple as isomorphic to R. So T is not δ-semiperfect
by [9, Theorem 3.6]. Hence T is not a δ-lifting module over T . It is easy to show
that T/Radδ(T ) lift to idempotents of T , so T is a semiregular ring. Since T is
a δ-semiregular ring, every ﬁnitely generated right ideal H of T can be written as
H = aT ⊕S, where a2 = a ∈T and S ≤Radδ(T ) by [9, Theorem 3.5]. Hence T is
a principally δ-lifting module.
Proposition 3.9. Let M be a principally δ-lifting module. If M = M1 + M2 such
that M1 ∩M2 is cyclic, then M2 contains a δ-supplement of M1 in M.
Proof. Assume that M = M1+M2 and M1∩M2 is cyclic. Then we have M1∩M2 =
N ⊕S, where N is direct summand of M and S is δ-small in M. Let M = N ⊕N ′
and M2 = N ⊕(M2 ∩N ′). It follows that M1 ∩M2 = N ⊕(M1 ∩M2 ∩N ′) = N ⊕S.
Let π : M2 = N ⊕(M2 ∩N ′) →N ′ be the natural projection. It follows that
π(M1 ∩M2 ∩N ′) = M1 ∩M2 ∩N ′ = π(S). Since S is δ-small in M, it is δ-small in
N ′ by Lemma 2.1. Hence M = M1 +(M2 ∩N ′), M2 ∩N ′ ≤M2 and M1 ∩(M2 ∩N ′)
is δ-small in M2 ∩N ′. M2 ∩N ′ is contained in M2 and a δ-supplement of M1 in
M2. This completes the proof.
□
Let M be a module. A submodule N is called fully invariant if for each endo-
morphism f of M, f(N) ≤N. Let S = End(MR), the ring of R-endomorphisms of
M. Then M is a left S-, right R-bimodule and a principal submodule N of the right
R-module M is fully invariant if and only if N is a sub-bimodule of M. Clearly
0 and M are fully invariant submodules of M. The right R-module M is called
a duo module provided every submodule of M is fully invariant. For the readers’
convenience we state and prove Lemma 3.10 which is proved in [5].
Lemma 3.10. Let a module M = L
i∈I
Mi be a direct sum of submodules Mi (i ∈I)
and let N be a fully invariant submodule of M. Then N = L
i∈I
(N ∩Mi).
Proof. For each j ∈I, let pj : M →Mj denote the canonical projection and let
ij : Mj →M denote inclusion. Then ijpj is an endomorphism of M and hence
ijpj(N) ⊆N for each j ∈I. It follows that N ⊆L
j∈I
ijpj(N) ⊆L
j∈I
(N ∩Mj) ⊆N,
so that N = L
j∈I
(N ∩Mj).
□
One may suspect that if M1 and M2 are principally δ-lifting modules, then
M1 ⊕M2 is also principally δ-lifting. But this is not the case.


## Page 7


ON A CLASS OF LIFTING MODULES
7
Example 3.11. Consider the Z-modules M1 = Z/Z2 and M2 = Z/Z8.
It is
clear that M1 and M2 are principally δ-lifting. Let M = M1 ⊕M2. Then M is
not a principally δ-lifting Z-module. Let N1 = (1, 2)Z and N2 = (1, 1)Z. Then
M = N1 + N2, N1 is not a direct summand of M and does not contain any nonzero
direct summand of M.
For any proper submodule N of M, M/N is singular
Z-module. Hence the principal submodule does not satisfy δ-lifting property. It
follows that M is not principally δ-lifting Z-module. By the same reasoning, for any
prime integer p, the Z-module M = (Z/Zp) ⊕(Z/Zp3) is not principally δ-lifting.
We have already observed by the preceding example that the direct sum of
principally δ-lifting modules need not be principally δ-lifting. Note the following
fact.
Proposition 3.12. Let M = M1 ⊕M2 be a decomposition of M with M1 and M2
principally δ-lifting modules. If M is a duo module, then M is principally δ-lifting.
Proof. Let M = M1 ⊕M2 be a duo module and mR be a submodule of M. By
Lemma 3.10, mR = ((mR)∩M1)⊕((mR)∩M2). Since (mR)∩M1 and (mR)∩M2
are principal submodules of M1 and M2 respectively, there exist A1, B1 ≤M1 such
that A1 ≤(mR) ∩M1 ≤M1 = A1 ⊕B1, B1 ∩((mR) ∩M1) = B1 ∩(mR) is
δ-small in B1, and A2, B2 ≤M2 such that A2 ≤(mR) ∩M2 ≤M2 = A2 ⊕B2,
B2 ∩((mR) ∩M2) = B2 ∩(mR) is δ-small in B2. Then M = A1 ⊕A2 ⊕B1 ⊕B2,
A1 ⊕A2 ≤N and (mR) ∩(B1 ⊕B2) = ((mR) ∩B1) ⊕((mR) ∩B2) is δ-small in
M1 ⊕M2.
□
Lemma 3.13. The following are equivalent for a module M = M ′ ⊕M ′′.
(1) M ′ is M ′′-projective.
(2) For each submodule N of M with M = N + M ′′, there exists a submodule
N ′ ≤N such that M = N ′ ⊕M ′′.
Proof. See [7, 41.14]
□
Theorem 3.14. Let M1 be a semisimple module and M2 a principally δ-lifting
module. Assume that M1 and M2 are relatively projective. Then M = M1 ⊕M2 is
principally δ-lifting.
Proof. Let 0 ̸= m ∈M and let K = M1 ∩((mR) + M2). We divide the proof into
two cases:
Case (i): K ̸= 0. Then M1 = K ⊕K1 for some submodule K1 of M1 and so
M = K ⊕K1 ⊕M2 = (mR) + (M2 ⊕K1).
Hence K is M2 ⊕K1-projective.
By Lemma 3.13, there exists a submodule N of mR such that M = N ⊕(M2 ⊕


## Page 8


8
HATICE INANKIL, SAIT HALICIO ˘GLU, AND ABDULLAH HARMANCI
K1).
We may assume (mR) ∩(M2 ⊕K1) ̸= 0.
Note that for any submod-
ule L of M2, we have (mR) ∩(L + K1) = L ∩((mR) + K1).
In particular
(mR) ∩(M2 + K1) = M2 ∩(mR + K1). Then mR = N ⊕(mR) ∩(K1 ⊕M2). There
exist n ∈N and m′ ∈(mR) ∩(K1 ⊕M2) such that m = n + m′. Then nR = N
and m′R = (mR) ∩(K1 ⊕M2). Since (mR) ∩(M2 + K1) = M2 ∩((mR) + K1),
M2 ∩((mR) + K1) is a principal submodule of M2 and M2 is principally δ-lifting,
there exists a submodule X of M2 ∩((mR) + K1) = (mR) ∩(M2 ⊕K1) such
that M2 = X ⊕Y and Y ∩M2 ∩((mR) + K1) = Y ∩((mR) + K1) is δ-small in
M2∩((mR)+K1) and in M2. Hence M = (N ⊕X)⊕(Y ⊕K1). Since N ⊕X ≤mR
and (mR) ∩(Y ⊕K1) = Y ∩((mR) + K1), (mR) ∩(Y ⊕K1) = Y ∩((mR) + K1)
is δ-small in Y ⊕K1. So M is δ-lifting.
Case (ii):
K = 0. Then mR ≤M2. Since M2 is δ-lifting, there exists a submodule
X of mR such that M2 = X ⊕Y and (mR)∩Y is δ-small in Y for some submodule
Y of M2. Hence M = X ⊕(M1 ⊕Y ). Since (mR) ∩(M1 ⊕Y ) = (mR) ∩Y and
(mR)∩(M1 ⊕Y ) = (mR)∩Y is δ-small in Y . By Lemma 2.1 (3), (mR)∩(M1 ⊕Y )
is δ-small in M1 ⊕Y . It follows that M is δ-lifting.
□
A module M is said to be a principally semisimple if every cyclic submodule is
a direct summand of M. Tuganbayev calls a principally semisimple module as a
regular module in [3]. Every semisimple module is principally semisimple. Every
principally semisimple module is principally δ-lifting. For a module M, we write
Radδ(M) = P{L | L is a δ-small submodule of M}.
Lemma 3.15. Let M be a principally δ-lifting module. Then M/Radδ(M) is a
principally semisimple module.
Proof. Let m ∈M. There exists M1 ≤mR such that M = M1⊕M2 and (mR)∩M2
is δ-small in M2. So(mR) ∩M2 is δ-small in M. Then
M/Radδ(M) = [(mR + Radδ(M))/Radδ(M)] ⊕[(M2 + Radδ(M))/Radδ(M)]
because (mR+ Radδ(M)) ∩(M2+Radδ(M)) =Radδ(M).
Hence every principal
submodule of M/Radδ(M) is a direct summand.
□
Proposition 3.16. Let M be a principally δ-lifting module. Then M = M1 ⊕M2,
where M1 is a principally semisimple module and M2 is a module with Radδ(M)
essential in M2.
Proof. Let M1 be a submodule of M such that Radδ(M)⊕M1 is essential in M and
m ∈M1. Since M is principally δ-lifting, there exists a direct summand M2 of M
such that M2 ≤mR, M = M2 ⊕M ′
2 and mR∩M ′
2 is δ-small in M. Hence mR∩M ′
2
is a submodule of Radδ(M) and so mR ∩M ′
2 = 0. Then m ∈M2 and mR = M2.
Since M2∩Radδ(M) = 0, M2 is isomorphic to a submodule of M/Radδ(M). By


## Page 9


ON A CLASS OF LIFTING MODULES
9
Lemma 3.15, M/Radδ(M) is principally semisimple, M2 is principally semisimple.
On the other hand, Radδ(M) =Radδ(M ′
2) is essential in M2 that it is clear from
the construction of M ′
2.
□
A nonzero module M is called δ-hollow if every proper submodule is δ-small in
M, and M is principally δ-hollow if every proper cyclic submodule is δ-small in M,
and M is ﬁnitely δ-hollow if every proper ﬁnitely generated submodule is δ-small
in M. Since ﬁnite direct sum of δ-small submodules is δ-small, M is principally
δ-hollow if and only if it is ﬁnitely δ-hollow.
Lemma 3.17. The following are equivalent for an indecomposable module M.
(1) M is a principally δ-lifting module.
(2) M is a principally δ-hollow module.
Proof. (1)⇒(2) Let m ∈M. Since M is a principally δ-lifting module, there exist
N and S submodules of M such that N ≤mR, mR ∩S is δ-small in M and
M = N ⊕S. By hypothesis, N = 0 and S = M. So that mR ∩S = mR is δ-small
in M.
(2)⇒(1) Let m ∈M. Then mR = (mR) ⊕(0). By (2) mR is δ-small and (0) is
direct summand in M. Hence M is a principally δ-lifting module.
□
Lemma 3.18. Let M be a module, then we have
(1) If M is principally δ-hollow, then every factor module is principally δ-
hollow.
(2) If K is δ-small submodule of M and M/K is principally δ-hollow, then M
is principally δ-hollow.
(3) M is principally δ-hollow if and only if M is local or Radδ(M) = M.
Proof. (1) Assume that M is principally δ-hollow and N a submodule of M. Let
m + N ∈M/N and (mR + N)/N + K/N = M/N. Suppose that M/K is singular.
We have mR + K = M. Since M/K is singular and M is principally δ-hollow,
M = K.
(2) Let m ∈M. Assume that mR + N = M for some submodule N with M/N
singular. Then (m + K)R = (mR + K)/K is a cyclic submodule of M/K and
(mR+K)/K +(N +K)/K = M/K and M/(N +K) is singular as an homomorphic
image of M/N. Hence (N +K)/K = M/K or N +K = M. By hypothesis N = M.
(3) Suppose that M is principally δ-hollow and it is not local. Let N and K be
two distinct maximal submodules of M and k ∈K \ N. Then M = kR + N and
M/N is a simple module, and so M/N is a singular or projective module. If M/N
is singular, then M = N since kR is δ-small. But this is not possible since N is
maximal. So M/N is projective. Hence N is direct summand. So M = N ⊕N ′


## Page 10


10
HATICE INANKIL, SAIT HALICIO ˘GLU, AND ABDULLAH HARMANCI
for some nonzero submodule N ′ of M, that is, N and kR are proper submodules of
M. Since every proper submodule of M is contained in Radδ(M), M = Radδ(M).
The converse is clear.
□
Proposition 3.19. Let M be a module. Then the following are equivalent.
(1) M is principally δ-hollow.
(2) If N is submodule with M/N cyclic, then N is a δ-small submodule of M.
Proof. (1) ⇒(2) Assume that N is a submodule with M/N cyclic. Lemma 2.1
implies that M/N is principally δ-hollow since being δ-small is preserved under
homomorphisms. Since M/N has maximal submodules, and by Lemma 3.18, M/N
is local. There exists a unique maximal submodule N1 containing N. Hence N is
small, therefore it is δ-small.
(2) ⇒(1) We prove that every cyclic submodule is δ-small in M. So let m ∈M
and M = mR + N with M/N singular. Then M/N is cyclic. By hypothesis, N
is δ-small submodule of M. By Lemma 2.1, there exists a projective semisimple
submodule Y of N such that M = (mR) ⊕Y . Let Y = L
i∈I
Ni where each Ni is
simple. Now we write M = ((mR) L
i̸=j
Nj) ⊕Ni. Then M/((mR) L
i̸=j
Nj) is cyclic
module as it is isomorphic to simple module Ni. By hypothesis, ((mR) L
i̸=j
Nj) is δ-
small in M. Again by Lemma 2.1, there exists a projective semisimple submodule
Z of ((mR) L
i̸=j
Nj) such that M = Z ⊕Ni. Hence M is projective semisimple
module. So M = N ⊕N ′ for some submodule N ′. Then N ′ is projective. M/N
is projective as it is isomorphic to N ′. Hence M/N is both singular and projective
module. Thus M = N.
□
4. Applications
In this section, we introduce and study some properties of principally δ-semiperfect
modules. By [9], a projective module P is called a projective δ-cover of a module M
if there exists an epimorphism f : P −→M with Kerf is δ-small in P, and a ring
is called δ-perfect (or δ-semiperfect) if every R-module (or every simple R-module)
has a projective δ-cover. For more detailed discussion on δ-small submodules, δ-
perfect and δ-semiperfect rings, we refer to [9]. A module M is called principally
δ-semiperfect if every factor module of M by a cyclic submodule has a projective
δ-cover. A ring R is called principally δ-semiperfect in case the right R-module R is
principally δ-semiperfect. Every δ-semiperfect module is principally δ-semiperfect.
In [9], a ring R is called δ-semiregular if every cyclically presented R-module has a
projective δ-cover.
Theorem 4.1. Let M be a projective module. Then the following are equivalent.
(1) M is principally δ-semiperfect.


## Page 11


ON A CLASS OF LIFTING MODULES
11
(2) M is principally δ-lifting.
Proof. (1)⇒(2) Let m ∈M and P
f→M/mR be a projective δ-cover and
M
π→M/mR the natural epimorphism.
M
P
M/mR
0
♣♣♣♣♣♣♣♣♣♣♣✠
g
❄
π
✲
f
✲
Then there exists a map M
g→P such that fg = π. Then P = g(M)+Ker(f). Since
Ker(f) is δ-small, by Lemma 2.1, there exists a projective semisimple submodule Y
of Ker(f) such that P = g(M)⊕Y . So g(M) is projective. Hence M = K ⊕Ker(g)
for some submodule K of M. It is easy to see that g(K ∩mR) = g(K)∩Ker(f)
and Ker(g) ≤mR. Hence M = K + mR. Next we prove K ∩(mR) is δ-small in
K. Since Ker(f) is δ-small in P, g(K)∩Ker(f) = g(K ∩mR) is δ-small in P by
Lemma 2.1 (4). Hence K ∩(mR) is δ-small in K since g−1 is an isomorphism from
g(M) onto K.
(2)⇒(1) Assume that M is a principally δ-lifting module. Let m ∈M. There
exist direct summands N and K of M such that M = N ⊕K, N ≤mR and
mR ∩K is δ-small in K. Let K
π→M/mR denote the natural epimorphism de-
ﬁned by π(k) = k + mR where k ∈K, k + mR ∈M/mR. It is obvious that
Ker(π) = mR ∩K. It follows that K is projective δ-cover of M/mR. So M is
principally δ-semiperfect.
□
Corollary 4.2. Let R be a ring. Then the following are equivalent.
(1) R is principally δ-semiperfect.
(2) R is principally δ-lifting.
(3) R is δ-semiregular.
Proof. (1) ⇔(2) Clear by Theorem 4.1.
(2) ⇔(3) By Theorem 3.6 (2), R is principally δ-lifting if and only if for every
principal right ideal I of R can be written as I = N ⊕S, where N is direct
summand and S is δ-small in R. This is equivalent to being R δ-semiregular since
for any ring R, Radδ(R) is δ-small in R and each submodule of a δ-small submodule
is δ-small.
□
The module M is called principally δ-supplemented if every cyclic submodule of
M has a δ-supplement in M. Clearly, every δ-supplemented module is principally
δ-supplemented. Every principally δ-lifting module is principally δ-supplemented.


## Page 12


12
HATICE INANKIL, SAIT HALICIO ˘GLU, AND ABDULLAH HARMANCI
In a subsequent paper we investigate principally δ-supplemented modules in detail.
Now we prove:
Theorem 4.3. Let M be a principally δ-semiperfect module. Then
(1) M is principally δ-supplemented.
(2) Each factor module of M is principally δ-semiperfect, hence any homomor-
phic image and any direct summand of M is principally δ-semiperfect.
Proof. (1) Let m ∈M.
Then M/mR has a projective δ-cover P
β→M/mR.
There exists P
α→M such that the following diagram is commutative, β = πα,
where M
π→M/mR is the natural epimorphism.
P
M
M/mR
0
♣♣♣♣♣♣♣♣♣♣♣✠
α
❄
β
✲
π
✲
Then M = α(P) + mR, and α(P) ∩mR is δ-small in α(P), by Lemma 2.1 (1).
Hence M is principally δ-supplemented.
(2) Let M
f→N be an epimorphism and nR a cyclic submodule of N.
Let
m ∈f −1(nR) and P
g→M/(mR) be a projective δ-cover. Deﬁne M/(mR)
h→N/nR
by h(m′ + mR) = f(m′) + nR, where m′ + mR ∈M/(mR). Then Ker(g) is con-
tained in Ker(hg). By projectivity of P, there is a map α from P to N such that
hg = πα.
P
M/mR
N
N/nR
0
✲
g
♣♣♣♣♣♣♣♣♣♣♣❄
α
❄
h
✲
π
✲
It is routine to check that (nR)∩α(P) = α(Ker(g)). By Lemma 2.1 (2), α(Ker(g))
is δ-small in N since Ker(g) is δ-small. Let x ∈Ker(πα). Then hg(x) = (πα)(x) = 0
or α(x) ∈(nR) ∩α(P). So Ker(πα) is δ-small. Hence P is a projective δ-cover for
N/(nR).
□
Theorem 4.4. Let P be a projective module with Radδ(P) is δ-small in P. Then
the following are equivalent.
(1) P is principally δ-lifting.
(2) P/Radδ(P) is principally semisimple and, for any cyclic submodule xR of
P/Radδ(P) that is a direct summand of P/Radδ(P), there exists a cyclic
direct summand A of P such that xR = A.


## Page 13


ON A CLASS OF LIFTING MODULES
13
Proof. (1)⇒(2) Since P is a principally δ-lifting module, P/Radδ(P) is principally
semisimple by Lemma 3.15. Let xR be any cyclic submodule of P/ Radδ(P). By
Theorem 3.6, there exists a direct summand A of P and a δ-small submodule B
such that xR = A ⊕B. Since B is contained in Radδ(R), xR+ Radδ(R) = A+
Radδ(R). Hence xR = A.
(2)⇒(1) Let xR be any cyclic submodule of P. Then we have P/ Radδ(P) =
[(xR+Radδ(P))/Radδ(P)] ⊕[U/ Radδ(P)] for some U ≤P. By (2), there exists
a direct summand A of P such that P = A ⊕B and U = B+ Radδ(P). Then
P = A ⊕B = A + U+ Radδ(P). Since Radδ(P) is δ-small in P, there exists a
projective and semisimple submodule Y of P such that P = A ⊕B = (A + U) ⊕Y .
Since P is projective, A + B is also projective and so by Lemma 3.13, we have
A + B = V ⊕B for some V ≤A. Hence P = V ⊕B ⊕Y . On the other hand
(xR) ∩(B ⊕Y ) = (xR) ∩B ≤(xR) ∩U ≤Radδ(R). Since Radδ(R) is δ-small in
P, it is δ-small in B ⊕Y by Lemma 2.1 (3). Thus P is principally δ-lifting.
□
References
[1] F.W. Anderson and K.R. Fuller, Rings and Categories of Modules, Springer-Verlag, New
York, 1974.
[2] J. Clark, C. Lomp, N. Vanaja and R. Wisbauer, Lifting modules, Brikhauser-Basel, 2006.
[3] C. Lomp, Regular and Biregular Module Algebras, Arab. J. Sci. and Eng., 33(2008), 351-363.
[4] S. Mohamed and B. J. M¨uller, Continuous and discrete modules, Cambridge University Press,
1990.
[5] A. C. Ozcan , A. Harmanci and P. F. Smith, Duo Modules, Glasgow Math. J., 48(3)(2006),
533-545.
[6] K. Oshiro, Semiperfect modules and quasi-semiperfect modules, Osaka J. Math., 20(1983),
337-372.
[7] R. Wisbauer, Foundations of module and ring theory, Gordon and Breach , Reading, 1991.
[8] M.F. Yousif and Y. Zhou, Semiregular, Semiperfect and Perfect Rings Relative To An Ideal,
Rocky Mountain J. Math., 32(4)(2002), 1651-1671.
[9] Y. Zhou, Generalizations of Perfect, Semiperfect and Semiregular Rings, Algebra Colloq.,
7(3)(2000), 305-318.
Department of Mathematics, Ankara University, 06100 Ankara, Turkey
E-mail address: hatinankil@gmail.com
Department of Mathematics, Ankara University, 06100 Ankara, Turkey
E-mail address: halici@science.ankara.edu.tr
Department of Mathematics, Hacettepe University, 06550 Ankara, Turkey
E-mail address: harmanci@hacettepe.edu.tr

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
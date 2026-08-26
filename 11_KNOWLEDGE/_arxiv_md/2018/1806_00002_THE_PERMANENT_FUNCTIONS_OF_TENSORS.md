---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1806.00002
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1806.00002_The_permanent_functions_of_tensors

> Source: 1806.00002_The_permanent_functions_of_tensors.pdf

> Pages: 15

---


## Page 1


The permanent functions of tensors
Qing-wen Wang a, Fuzhen Zhang b
a Shanghai University, Shanghai, P.R. China; wqw@t.shu.edu.cn
b Nova Southeastern University, Fort Lauderdale, USA; zhang@nova.edu
Abstract By a tensor we mean a multidimensional array (matrix) or hyperma-
trix over a number ﬁeld. This article aims to set an account of the studies on the
permanent functions of tensors. We formulate the deﬁnitions of 1-permanent,
2-permanent, and k-permanent of a tensor in terms of hyperplanes, planes and
k-planes of the tensor; we discuss the polytopes of stochastic tensors; at end we
present an extension of the generalized matrix function for tensors.
AMS Classiﬁcation: 15A15, 15A02, 52B12
Keywords: Birkhoﬀ-von Neumann Theorem, doubly stochastic matrix, hypermatrix, matrix
of higher order, multidimensional array, permanent, polytope, stochastic tensor, tensor
1
Introduction
The study on multidimensional arrays (or matrices) may date back as early as
the nineteenth century by Cayley [7, 8]. Jurkat and Ryser revived the topic
in their seminal paper [21] in 1968 in which they investigated conﬁgurations
and decompositions for multidimensional arrays. Jurkat and Ryser’s work was
followed by a great deal of research on the topic, mainly on the combinatorial
aspects of certain types (such as stochasticity) of multidimensional arrays; see,
e.g., Brualdi and Csima [3, 5].
In recent years, multidimensional arrays are
found applications in practical ﬁelds such as image processing (see, e.g., Qi
and Luo [32]), theory of computing (see, e.g., Cifuentes and Parrilo [12]), and
physics (see, e.g., Tichy [36]). We are concerned with the permanent functions of
multidimensional arrays. Our purpose is to set an account on the speciﬁc topic
based on publications, including, in particular, the ones by Dow and Gibson [16]
and Taranenko [35]. The results are expositorily presented with explanations
other than in the format of theorem-proofs. Some results are easy observations;
they are not necessarily new. For the determinants of multidimensional arrays,
hyperdeterminants, and related topics, see, e.g., [19, 20, 26, 34].
Let n1, n2, . . . , nd be positive integers.
We write A = (ai1i2...id), ik =
1, 2, . . . , nk, k = 1, 2, . . . , d, for an n1 × n2 × · · · × nd multidimensional array
or hypermatrix of order d (the number of indices). Multidimensional arrays, or
1
arXiv:1806.00002v1  [math.CO]  30 May 2018


## Page 2


hypermatrices, or matrices of higher orders, are referred to as tensors; see, e.g.,
[15, 24, 32]. So, by a tensor we mean a multidimensional array. The tensors
of order 1 (i.e., d = 1) are vectors in Rn1, while the 2nd order tensors are just
regular n1 × n2 matrices. A 3rd order tensor, i.e., an n1 × n2 × n3 tensor, may
be viewed as a book of n3 pages (slices), each page is an n1 × n2 matrix.
If n1 = n2 = · · · = nd = n, we say that A is of order d and dimension n or we
say that A is an
d
z
}|
{
n × · · · × n tensor. We also call an n×n×n tensor (i.e., of order
3 and dimension n) a tensor cube or a 3D matrix. We refer to the permanents
of multidimensional arrays as the permanents of tensors, or hyperpermanents.
Following the line of Dow and Gibson [16], we will begin with the deﬁnitions
of 1-permanent, 2-permanent, and k-permanent of tensors. 1-permanents, the
most modest ones, are useful in studying hypergraphs (see, e.g., [16, 35]), the
2-permanents with d = 3 or of special relation of d and n are found applications
in projective planes (see, e.g., [16]) and polytope theory (see, e.g., [9, 14, 25]),
while k-permanents are certainly an object in combinatorics themselves.
Remark 1 We adopt Lim’s terminology in [26] (see also [24, 32]), calling an
d
z
}|
{
n × · · · × n tensor a tensor of order d and dimension n. Such a tensor is also
said to be of order n and dimension d in the literature; see, e.g., [5, 35].
2
The deﬁnitions of permanents of tensors
2.1
1-permanent and 2-permanent
Let A = (ai1...id) be an n1 × · · · × nd tensor of order d with real entries. Dow
and Gibson [16] deﬁned (over a commutative ring) the permanent of A as
per (A) =
X n1
Y
i=1
aiσ2(i)...σd(i),
(1)
where the summation runs over all one-to-one functions σk from {1, 2, . . . , n1}
to {1, 2, . . . , nk}, k = 2, 3, . . . , d, with per (A) = 0 if n1 > nk for some k.
Note: under the deﬁnition (1), if A is an n1 × n2 matrix and n1 > n2, then
per (A) = 0, but per (At) need not be 0, where At is the transpose of A. This
is not in agreement with the fact that a matrix (i.e., order 2 tensor) and its
transpose have the same permanent. We may slightly modify and extend the
deﬁnition (1) as follows. Let n = min{n1, n2, . . . , nd} = nj for some j. Then
per (A) =
X
n
Y
i=1
aσ1(i)···σj(i)...σd(i),
(2)
where the summation runs over all one-to-one functions σk from {1, 2, . . . , n} to
{1, 2, . . . , nk}, k ̸= j, and σj is the identity map. (2) reduces to (1) if n = n1. It
is immediate by deﬁnition (2) that per (A) = per (At) for rectangular matrices.
2


## Page 3


When n1 = n2 = · · · = nd = n, (1) can be written in a symmetric form
per (A) = 1
n!
X
π1,...,πd∈Sn
n
Y
i=1
aπ1(i)···πd(i),
(3)
where Sn is the symmetric group of degree n.
If d = 2, (3) reduces to the usual permanent for square matrices.
The deﬁnition (1) of permanent is in fact the so-called 1-permanent (or 1-per
for short) of the tensor A. 1-per (v.s. k-per; see the deﬁnition below or see [16,
Sec. 4]) of A is the sum of all products of n1 entries of A no two of which are
taken from the same hyperplane (of order d −1; see Sec. 2.2). In the case of 3D
matrices, the planes of A are the submatrices obtained by ﬁxing one of i, j, k,
and the lines of A are the submatrices obtained by ﬁxing two of i, j, k.
Figure 1: 2 × 2 × 2 tensors and their ﬂattened frontal slices
A =

a111
a121
...
a112
a122
a211
a221
...
a212
a222

,
B =

1
0
...
0
1
0
1
...
1
0

.
For example, take A = (aijk), i, j, k = 1, 2. Then
1-per (A)
=
a111a222 + a211a122 + a121a212 + a221a112,
2-per (A)
=
a111a221a122a212 + a211a121a112a222.
Note that we use the same symbol for the tensor and its frontal slice ﬂat-
tening as there is no confusion will be caused in this paper.
By a (0,1)-tensor, we mean a tensor in which every entry is either 0 or 1.
For the 2 × 2 × 2 (0,1)-tensor B in Fig. 1 on the right hand side, 1-per (B) = 0,
2-per (B) = 1.
If I3 is the 3 × 3 × 3 identity tensor, i.e., the entry in the
(i, i, i) position is 1 for every i and everywhere else is 0, then 1-per (I3) = 1 and
2-per (I3) = 0. Let J3 be the 3 × 3 × 3 tensor of 1s (i.e., all entries are 1). Then
1-per (J3) = 9 · 4 = (3!)2 = 36 and 2-per (J3) = 6 · 2 = 12.
1-permanent and 2-permanent are the most important permanent functions
of tensors. We write per (·) for 1-per (·) and Per (·) for 2-per (·). We simply call
1-permanent permanent in the sense of (1) unless otherwise stated.
3


## Page 4


The following observations are immediate for permanents (i.e., 1-permanents):
(i) the permanent function of tensors is linear with respect to each hyperplane;
(ii) interchange of two hyperplanes does not change the permanent; (iii) if
A = (ai1i2...id) is a tensor of order d and dimension n and Aσ = (aiσ(1)iσ(2)...iσ(d))
is the σ-transpose of A, where σ ∈Sd, then A and Aσ have the same permanent;
(iv) if A = (ai1i2...id) and B = (bi1i2...id) are nonnegative tensors of the same
size and A ≤B entrywise, then the permanent of A is less than or equal to the
permanent of B; and (v) the Laplace expansion theorem holds.
The classic Frobenius-K¨onig theorem (see, e.g., [38, p. 158]) states that for
an n × n nonnegative matrix A, the permanent of A vanishes if and only if A
contains an r × s zero submatrix such that r + s = n + 1. The following result
is an analog for tensors.
Proposition 2 (Dow and Gibson [16]) Let A be an n1×n2×· · ·×nd tensor.
If A contains an m1 × m2 × · · · × md zero sub-tensor such that Pd
k=1 mk =
1 + Pd
k=2 nk, then per (A) = 0; but not conversely.
Consequently, for a nonnegative tensor of order d and dimension n, if 1-
permanent is positive, then Pd
k=1 mk ≤(d −1)n. The positivity of the per-
manent of a nonnegative tensor of order d and dimension n is characterized in
terms of term rank in [6]: it is positive if and only if the term rank is n .
Lower and upper bounds for the permanents of (0,1)-tensors (or matrices,
or Latin squares, etc) are always interesting and challenging. Shown below is a
lower bound of the permanent, given the number of zero entries.
Proposition 3 (Dow and Gibson [16]) Let A be an n × n × · · · × n (0,1)-
tensor of order d with exactly t 0s. Then per (A) ≥(nd−1 −t) ((n −1)!)d−1 .
The well-known Minc-Bregman theorem on a (0,1)-matrix gives an upper
bound for the permanent of the (0,1)-matrix in terms of the numbers of 1s on
each row (or column). For tensors, we have the following.
Proposition 4 (Dow and Gibson [17]) Let A = (aijk) be an n×n×n (0,1)-
tensor. Let ri = P
j,k aijk for i = 1, 2, . . . , n. Then the Minc-Bregman type
inequality for 1-permanent holds:
per (A) ≤
n
Y
i=1
(ri!)1/ri.
Proposition 5 (Dow and Gibson [17]) Let A = (aijk) be an n×n×n (0,1)-
tensor. Let rij = P
k aijk for i, j = 1, 2, . . . , n. Then the Minc-Bregman type
inequality for 2-permanent holds:
Per (A) ≤
n
Y
i=1
(rij!)1/rij.
4


## Page 5


A permutation tensor is a (0,1)-tensor in which every hyperplane contains
one and only one 1. In particular, the usual permutation matrices are permuta-
tion tensors of order 2; the identity tensor In (all entries on the main diagonal
(i, i, i), i = 1, 2, . . . , n, are 1) is a permutation tensor of order 3. (Note: permu-
tation tensors are deﬁned diﬀerently in the literature; see, e.g., [27].) Let Ωd
n
be the convex hull of the permutation tensors of order d and dimension n. An
analog of the Van der Waerden conjecture (see, e.g., [30]) for tensors is surely
appealing. Dow and Gibson [16] conjectured that if A = (ai1i2···id) ∈Ωd
n, then
per (A) ≥(n!/nn)d−1
with equality if and only if A = (1/nd−1)Jn, where Jn is the tensor of all 1s.
This is disproved by Taranenko [35, Proposition 4, p. 590]. Taranenko pre-
sented as many as 13 conjectures concerning permanents and stochastic poly-
topes in [35]. We single out a couple that are easily stated and understood.
Conjecture 6 (Taranenko [35]) Let A be an
d
z
}|
{
n × · · · × n line-stochastic ten-
sor. If d is even, then per (A) > 0.
Conjecture 7 (Taranenko [35]) Let A be an
d
z
}|
{
n × · · · × n line-stochastic ten-
sor. If n is odd, then per (A) > 0.
For more discussions on this, see Theorems 19 and 22 of [35].
2.2
k-permanent and the Hadamard product
Let A = (ai1i2...id) be a tensor of order d.
For 1 ≤k ≤d, let f = d −k.
If we ﬁx f of the indices i1, i2, . . . , id and let the rest k indices vary, then we
obtain a sub-tensor of A. We call such a sub-tensor a k-plane of A (see [16, 35]).
1-plane (1 free index) is referred to as a line (or ﬁber or tube); 2-plane (2 free
indices) is simply a plane; a (d −1)-plane of an order d tenor is usually called
a hyperplane.
Dow and Gibson [16] deﬁned the k-permanent of A, denoted by k-per (A),
to be the sum of all possible products of nk entries of A so that no two entries
are taken from the same (d −k)-plane [16, p. 142]. If such a selection of entries
of A does not exist, then we write k-per (A) = 0.
Remark 8 The existence of such selections of the entries of A is extensively
studied (see, e.g., [5, 11, 21, 28, 33]) and it is in the area of conﬁgurations and
block designs in combinatorics (see, e.g., [13]).
For 2×2×2 tensors, we have demonstrated 1-per and 2-per in the previous
examples. Permanents deﬁned by (1) always exist. Let A = (aijst) be a 2 × 2 ×
2 × 2 tensor. The 2-per(A) is the sum of products of nk = 22 = 4 entries of A
that are not in the same d −k = 4 −2 = 2-plane. Such a selection of entries is
5


## Page 6


impossible for four sequences i, j, s, t of length 4 whose components are 1 or 2:
ai1i2i3i4aj1j2j3j4as1s2s3s4at1t2t3t4. Thus,
2-per (A) =
X
aiajasat = 0.
Let A = (ai1i2...id) be an
d
z
}|
{
n × · · · × n tensor and let 1 ≤k < d. A k-per
diagonal of A consists of nk entries of A; each entry is from a (d −k)-plane and
no two entries are from the same (d−k)-plane. A 1-per diagonal is simply called
a diagonal; that is, a diagonal of a tensor of dimension n consists of n entries,
no two are from the same hyperplane. For d = 2, k = 1, a 1-per diagonal of
A consists of n entries of A from diﬀerent lines (i.e., rows and columns). For
d = 3, k = 1, a 1-per diagonal of A consists of n entries of A, each of which is
from 1-plane, no two fall on the same plane. For d = 3, k = 2, a 2-per diagonal
of A consists of n2 entries of A each plane contains exactly n entries of A.
We say that A is k-per feasible if it is possible to choose nk entries of A,
no two in the same (d −k)-plane. Such a selection of the nk entries comprises
of a
k-per diagonal of A. The k-per diagonal of A can be extracted by the
Hadamard (Schur or entrywise) product of A with a (0,1)-tensor D of the same
size (order and dimension) as A in which the k-per diagonal entries of D in the
same positions as the k-per diagonal of A are 1s and 0s elsewhere. We call such
a (0,1)-tensor D a k-per index tensor (or a k-per cell). That is, a k-per index
tensor is a (0,1)-tensor of order d and dimension n which contains nk 1s so that
no two 1s are located in the same (d −k)-plane. Let Q(A ◦D) be the product
of the k-per diagonal entries of A indexed by D. Denote by Pd,n,k, or simply
Pk, the set of k-per index tensors. (Note: again, the existence of a k-per index
tensor for a given k is a problem of conﬁguration which is not a concern of this
paper. For the study of the existence of (0,1)-tensors with a ﬁxed number of 1s
on a k-plane, see, e.g., [11, 13, 33].)
We formulate the k-permanent of tensor A [16] as follows.
Proposition 9 Let A = (ai1i2...id) be an
d
z
}|
{
n × · · · × n tensor, 1 ≤k < d. Then
k-per (A) =
X
D∈Pk
Y
(A ◦D).
Proposition 10 Let A = (ai1i2...id) be an
d
z
}|
{
n × · · · × n tensor, 1 ≤k < d. Then
k-per (cA) = cnk (k-per (A)) , where c is a constant.
The following result states that every k-per can be converted to a 1-per.
Proposition 11 (Dow and Gibson [16]) Let A be a tensor of order d and
dimension n, 1 ≤k < d. Then there exists an nk × nk × · · · × nk tensor B of
order
 d
k

whose nonzero entries are equal to the nonzero entries of A such that
k-per (A) = 1-per (B).
6


## Page 7


Remark 12 Diﬀerent generalizations of the permanents from matrices to ten-
sors exist. Taranenko [35] deﬁned r-permanents, perr, of multidimensional ma-
trices by the Maximum Distance Separable (MDS) codes with distance r. In
[35], the permanent is in fact the d-permanent, that is, per (A) = perd(A),
which is the same as the 1-permanent in [16], namely our (1). More generally,
if r + s = d + 1, then the r-permanent in [35] is just the s-permanent in [16].
For n × n × n tensors, the 2-permanents deﬁned in [16] and in [35] turn out to
be the same, namely, 2-per (A)= per2(A). However, for 2 × 2 × 2 × 2 tensors,
2-per (A) ̸= per2(A).
2.3
Permanent and the Hamming distance
Let x = (x1, x2, . . . , xn), y = (y1, y2, . . . , yn) ∈Rn. The Hamming distance,
denoted by ρ(x, y), of x and y is the number of nonzero components of x −y.
Take x = (1, 2, 3), y = (1, 3, 2). Then x −y = (0, −1, 1). Thus, ρ(x, y) = 2.
Denote Id
n = {(i1, i2, . . . , id)}, where 1 ≤ik ≤n for k = 1, 2, . . . , d. Let
A = (ai1i2...id). We write A = (ai), where ai = ai1i2···id, i = (i1, . . . , id) ∈Id
n.
For i = (i1, . . . , id) and j = (j1, . . . , jd), ρ(i, j) = d implies that the correspond-
ing components of i and j are pairwise distinct. Taranenko [35] deﬁned the
permanent of a tensor using Hamming distance, which is essentially the same
as (1), i.e., the 1-permanent of [16], namely the d-permanent of [35].
Proposition 13 Let A = (ai1i2...id) be an
d
z
}|
{
n × · · · × n tensor. Then
per (A) =
X
α1, α2,...,αd∈Id
n
ρ(αi, αj)=d, i̸=j
aα1aα2 · · · aαn.
(4)
Let A = (aijst) be a 2 × 2 × 2 × 2 tensor. Then per (A) is the sum of all
products of nk = 21 = 2 entries of A that are not in the same d−k = 4−1 = 3-
plane. It follows from (4) that
per (A)
=
X
ρ(α,β)=4
aαaβ
=
a1111a2222 + a1112a2221 + a1121a2212 + a1211a2122
+a2111a1222 + a1122a2211 + a1212a2121 + a1221a2112.
Note that the 2-per (A) is the sum of all products of nk = 22 = 4 entries of
A that are not in the same d −k = 4 −2 = 2-plane. It is impossible for four
sequences α, β, γ, δ of length 4 whose components are 1 or 2 to have ρ(p, q) ≥3
for all pairs p and q from {α, β, γ, δ}. Thus, Per (A) = 0.
2.4
The permanents of 3D matrices (i.e., n×n×n tensors)
For α, β ∈Sn, we may regard α and β as sequences in Rn: α = (α(1), . . . , α(n))
and β = (β(1), . . . , β(n)). If ρ(α, β) = n, then α(i) ̸= β(i) for all i.
7


## Page 8


Let A = (aijk) be a 3D matrix (i.e., a tensor of order 3 and dimension n),
namely, A is an n × n × n tensor. A diagonal of A consists of n entries, each
of which is taken from a plane and no two entries are from the same plane (as
d −k = 3 −1 = 2); A triagonal ([18, p. 181]) of A consists of n2 entries, each
of which is taken from a line and no two are from the same line. Then 1-per (A)
is the sum of products of diagonal entries. Thus [17],
1-per (A) =
X
α, β∈Sn
n
Y
i=1
aiα(i)β(i),
(5)
while 2-per (A) is the sum of products of triagonal entries. So,
2-per (A) =
X Y
(n2 entries of A; no two are colinear).
For 3×3×3 tensors, 1-permanent is the sum of all products of 3 elements, no
two are on the same plane (frontal, lateral or horizontal [24]), i.e., one element
from each plane, while 2-permanent is the sum of all products of 9 entries any
two of which are non-collinear (in any direction), i.e., one entry from each line.
Let A = (aijk) be an n × n × n tensor. If we denote (or label) the kth frontal
page of A by πk ∈Sn, we can write a triagonal aπ of A as
aπ = (aπ1, aπ2, . . . , aπn)
where ρ(πi, πj) = n whenever i ̸= j. Let D(aπ) = Qn
i=1 D(aπi) for the product
of the triagonal entries. Then (see, e.g., [9, 14]), we have
Proposition 14 Let A = (aijk) be an n × n × n tensor. Then
Per (A) = 2-per (A) =
X
π
Y
D(aπ) =
X
π1,π2,...,πd∈Sn
ρ(πi,πj)=n, i̸=j
n
Y
i=1
D(aπi).
It is easy to see that there are n2 · (n −1)2 · · · 22 · 12 = (n!)2 permutation
tensors of order 3 and dimension n. Let Ln be the number of Latin squares of
order n and let J3
n denote the n × n × n tensor of all 1s. Then Per (J3
n) is equal
to the number of triagonals of A = (aijk). Observe that every triagonal of J3
n
corresponds solely to a Latin square of order n (see, e.g., [21]).
Proposition 15 A 3D matrix of dimension n has Ln triagonals.
3
Stochastic tensors
3.1
Line, plane, k-stochastic, and permutation tensors
Recall the celebrated Birkhoﬀ-von Neumann theorem on the polytope of doubly
stochastic matrices (see, e.g., [38, p.159]). It states that an n×n matrix is doubly
8


## Page 9


stochastic if and only if it is a convex combination of some n × n permutation
matrices. This result is about the matrices that are 2-way stochastic. What
would be the mathematical objects that are 3-way stochastic?
Let A = (aijk) be an n × n × n tensor. A is said to be triply line stochastic
[14] (or stochastic semi-magic cube [1]) if all aijk ≥0 and
n
X
i=1
aijk = 1,
n
X
j=1
aijk = 1,
n
X
k=1
aijk = 1.
That is, each of horizontal, lateral and frontal slices (see [24]) is a doubly stochas-
tic matrix. For a nonnegative tensor A = (ai1i2...id) of order d and dimension
n, we say A is line-stochastic [18] if the sum of the entries on each line is 1:
n
X
i=1
a···i··· = 1.
Equivalently, every plane (i.e., 2-plane) of A is doubly stochastic, namely, for
e = (1, 1, . . . , 1)t ∈Rn, every n × n matrix with (i, j) entry a···i···j··· satisﬁes
(a···i···j···)e = e,
et(a···i···j···) = et.
We say that A is plane-stochastic [4] if the sum of all elements on every plane
is equal to 1, that is,
n
X
i,j=1
a···i···j··· = 1.
More generally, let A be a nonnegative tensor of order d and dimension n
and let 1 ≤k ≤d. If the sum of the entries of A on every k-plane is 1, then A is
said to be k-stochastic (see, e.g., [5, 33]). A k-stochastic (0,1)-tensor is called
a k-permutation tensor (or a permutation tensor of degree k; for its existence,
see Remark 8). Being line stochastic is 1-stochastic; being 2-stochastic is plane-
stochastic; and a 1-permutation tensor is nothing but a line-permutation
tensor, while a 2-permutation tensor is a plane-permutation tensor. In case
of n × n × n, 1-permutation tensor has 1s on its diagonal and 2-permutation
tensor has 1s on its triagonal. The (d −1)-permutation tensors (of order d and
dimension n) are simply called permutation tensors [16].
Let P and Q be n × n permutation matrices. We say that P and Q are
diagonally disjoint (or Hadamard orthogonal) if no 1 appears in the same (over-
lapping) position of P and Q, that is, the Hadamard product P ◦Q = 0.
Proposition 16 Let P1, P2, . . . , Pn be n × n permutation matrices and π1, π2,
. . . , πn be the corresponding elements (via group isomorphism) in the symmetric
group Sn. The following statements are equivalent:
1. The tensor with frontal slice ﬂattening [P1|P2| · · · |Pn] is an n × n × n
line-permutation tensor.
9


## Page 10


2. P1, P2, . . . , Pn are mutually diagonally disjoint.
3. ρ(πi, πj) = n for all i ̸= j.
4. P1 + P2 + · · · + Pn = J (where J is the matrix of 1s).
For an analog for n × n × n plane-permutation tensors, let Q1, Q2, . . . , Qn
be n × n permutation matrices. Then the n × n × n (0,1)-tensor R with frontal
slice ﬂattening [Q1|Q2| · · · |Qn] is a plane-permutation tensor if and only if each
of the plus-projections (by adding the elements) fi(R), fj(R), and fk(R) of R
along i, j, and k-axes is an n × n permutation matrix.
3.2
Polytopes of stochastic tensors
The Birkhoﬀ-von Neumann Theorem asserts that the set of the doubly stochas-
tic matrices and the convex hull of the permutation matrices coincide. In other
words, the permutation matrices are precisely the vertices (extreme points)
of the polytope of doubly stochastic matrices. This is usually proven by the
Frobenius-K¨onig theorem (see, e.g., [38, p.158]).
The Birkhoﬀ-von Neumann Theorem does not generalize to tensors of higher
dimensions. The 3×3×3 line-stochastic tensor D in Fig. 2 is not a combination
of line-permutation tensors; in fact, it is an extreme point of the polytope of
3 × 3 × 3 line-stochastic tensors. Moreover, Per (D) = 0. Let
• ∆ℓ
n be the convex hull of n × n × n line-permutation tensors.
• ∆℘
n be the convex hull of n × n × n plane-permutation tensors.
• Ωℓ
n be the set of all n × n × n line-stochastic tensors.
• Ω℘
n be the set of all n × n × n plane-stochastic tensors.
The ∆s and Ωs are polytopes in Rn3. It is tempting to know the structures
and the numbers of the extreme points of the polytopes ∆s. Obviously,
∆ı
n ⊆Ωı
n,
where ı = ℓor ℘.
The following facts are known or easy to obtain:
1. For n = 2, ∆ℓ
2 = Ωℓ
2. That is to say, every 2 × 2 × 2 line-stochastic tensor
is a convex combination of the two (0,1) line-stochastic tensors.
2. For n = 2, ∆℘
2 is a proper subset of Ω℘
2 . Take C = (cijk) with c211 = c121 =
c112 = c222 = 1
2, and 0 everywhere else. C is not a convex combination
of the plane-permutation tensors. Ω℘
2 has 6 extreme points, 4 of which
are (0,1)-tensors and 2 are non-(0,1) (with entries 1/2); see [4, 10, 23, 33].
The cube on the left in Fig. 2 represents the tensor C, while shown below
is its frontal slice ﬂattening. (Likewise, the other cube is for tensor D.)
C = 1
2

0
1
...
1
0
1
0
...
0
1

.
10


## Page 11


Figure 2: C ∈Ω℘
2 \ ∆℘
2 and D ∈Ωℓ
3 \ ∆ℓ
3
3. For n = 3, the polytope Ωℓ
3 has 66 vertices, of which 12 are line-permutation
tensors (due to the fact that there are 12 Latin squares of order 3), 54 are
non-(0,1) (with entries 1/2). ∆ℓ
3 is a proper subset of Ωℓ
3 because tensor
D is not a convex combination of line-permutation tensors (see, e.g., [9]).
Moreover, for the line-stochastic tensor D, we have Per (D) = 0. This says,
unlike the permanent of a doubly stochastic matrix, that the 2-permanent
(i.e., Per ) of a triply line-stochastic tensor may vanish.
D = 1
2





0
1
1
...
1
1
0
...
1
0
1
1
1
0
...
0
1
1
...
1
0
1
1
0
1
...
1
0
1
...
0
2
0




.
4. For n = 3, ∆℘
3 is a proper subset of Ω℘
3 . A complete list of the extreme
points of Ω℘
3 , up to equivalence, is available in [4].
Question 17 What would be the minimums of the permanents on the sets ∆s?
Proposition 18 Let A = (aijk) be an n × n × n nonnegative tensor. If a plus-
projection (by adding the elements) fi(A), fj(A), or fk(A) of A along i, j, or
k-axis contains a 0, then Per (A) = 0. (The converse is not true.)
If R is a nonnegative tensor such that (k-per or) Per (R) > 0, then for any
nonnegative tensor S of the same size, (k-per, resp.) Per (R+S) ≥Per (R) > 0.
Proposition 19 Let P0 = {A ∈Ωℓ
n | Per (A) = 0} and let P and Q be in
P0. Then either everything between P and Q is contained in P0 (i.e., tP +
(1 −t)Q ∈P0 for all 0 < t < 1), or nothing between P and Q lies in P0 (i.e.,
tP + (1 −t)Q ̸∈P0 for all 0 < t < 1).
4
Generalized tensor functions
Let A = (aij) be an n × n matrix. Let G be a subgroup of Sn and χ be a
character on G. The classic determinant, permanent, and generalized matrix
11


## Page 12


function of A are respectively deﬁned by
det A =
X
β∈Sn
(−1)sgn(β)
n
Y
i=1
aiβ(i) = 1
n!
X
α,β∈Sn
(−1)sgn(α)sgn(β)
n
Y
i=1
aα(i)β(i),
per A =
X
β∈Sn
n
Y
i=1
aiβ(i) = 1
n!
X
α,β∈Sn
n
Y
i=1
aα(i)β(i),
dχ
GA =
X
β∈G
χ(β)
n
Y
i=1
aiβ(i) =
1
|G|
X
α,β∈G
χ(α)χ(β)
n
Y
i=1
aα(i)β(i).
For a tensor A = (ai1i2···id) of order d and dimension n. Cayley’s combina-
torial (v.s. geometric) hyperdeterminant of A is deﬁned to be
det A = 1
n!
X
π1,...,πd∈Sn
sgn(π1) . . . sgn(πd)
n
Y
i=1
aπ1(i)···πd(i).
(6)
The reader is referred to [19, 26, 34, 20] for hyperdeterminants or the deter-
minants of multidimensional matrices (tensors).
For a tensor A = (ai1i2···id) of order d and dimension n, the permanent (1-
permanent) of A is deﬁned analogously as in (1) and (3). We now give a try to
extend the notation to generalized tensor functions.
Let A = (ai1i2···id) be a tensor of order d and dimension n.
Let G =
(G1, G2, . . . , Gd) and χ = (χ1, χ2, . . . , χd), where Gi is a subgroup of Sn and χi
is a character on Gi, i = 1, 2, . . . , d. We deﬁne
dχ
G(A) =
1
|G1|
X
π1∈G1,...,πd∈Gd
χ1(π1) · · · χd(πd)
n
Y
i=1
aπ1(i)···πd(i).
(7)
Apparently, the determinant (6) and permanent (3) are special cases of (7).
Like 2-permanent for n × n × n tensors, we may deﬁne 2-dχ
G as follows:
2-dχ
G(A) =
X
ρ(πi,πj)=n, i̸=j
n
Y
i=1
χi(πi)aπi.
(8)
Additionally, in regard to the k-permanent, we may deﬁne the k-generalized
tensor functions (k-gtf). Let fk be a scalar-valued function deﬁned on a domain
that contains all k-per diagonals A ◦D of A, where D ∈Pk (see Sec. 2.2). Then
k-gtf(A) =
X
D∈Pk
fk(A ◦D)
Y
(A ◦D).
(9)
The work of Merris [29] may be a hint for the study in this direction.
Acknowledgement. The work was done while the second author was vis-
iting Shanghai University during his sabbatical leave from Nova Southeastern
12


## Page 13


University. The work of Wang was partially supported by the Natural Science
Foundation of China (11571220); the work of Zhang was partially supported by
an NSU PFRDG Research Scholar grant. This expository article was written
based on the second author’s presentation at ICMAA in Da Nang, Vietnam,
June 14-18, 2017. The authors appreciate the communications with C. Bu, L.
Cui, S. Hu, L. Qi, A. Taranenko, Y. Wei, and G. Yu during the preparation of
the manuscript.
References
[1] M. Ahmed, Algebraic Combinatorics of Magic Squares, University of Califorina -
Davis, Ph.D. Thesis, 2004.
[2] A. Barvinok, Computing the Permanent of (Some) Complex Matrices, Found.
Comput. Math. 16 (2016) 329–342.
[3] R.A. Brualdi and J. Csima, Stochastic patterns, J. Combin. Theory Ser. A 19
(1975) 1–12.
[4] R.A. Brualdi and J. Csima, Extremal plane stochastic matrices of dimension
three, Linear Algebra Appl. 11 (1975) 105–133.
[5] R.A. Brualdi and J. Csima, Small matrices of large dimension. Proceedings of the
First Conference of the International Linear Algebra Society (Provo, UT, 1989),
Linear Algebra Appl. 150 (1991) 227–241.
[6] C. Bu, W. Wang, L. Sun, and J. Zhou, Minimum (maximum) rank of sign pattern
tensors and sign nonsingular tensors, Linear Algebra Appl. 483 (2015) 101–114.
[7] A. Cayley, On the Theory of Linear Transformations, Cambridge Math. J. 4
(1845) 193–209.
[8] A. Cayley, Sur les determinants gauches (Suite du Memoire T. XXXII. p. 119),
(French) J. Reine Angew. Math. 38 (1849) 93–96.
[9] H. Chang, V.E. Paksoy, F. Zhang, Polytopes of Stochastic Tensors, Ann. Funct.
Anal. 7 (2016) 386–393.
[10] M. Che, C. Bu, L. Qi, and Y. Wei, Nonnegative tensors revisited: plane stochastic
tensors, manuscript, 2017.
[11] J.P.R. Christensen and P. Fischer, Multidimensional stochastic matrices and
error-correcting codes, Linear Algebra Appl. 183 (1993) 255-276.
[12] D. Cifuentes, P.A. Parrilo, An eﬃcient tree decomposition method for permanents
and mixed discriminants, Linear Algebra Appl. 493 (2016) 45–81.
[13] C.J. Colbourn and J. Dinitz (eds.), Handbook of Combinatorial Designs, Second
Edition, 2006, Chapman and Hall/CRC Press.
[14] L.-B. Cui, W. Li, and M. K. Ng, Birkhoﬀ–von Neumann Theorem for Multi-
stochastic Tensors, SIAM. J. Matrix Anal. Appl. 35–3 (2014) 956–973.
[15] W. Ding and Y. Wei, Theory and computation of tensors, Elsevier/Academic
Press, London, 2016.
[16] S.J. Dow and P.M. Gibson, Permanents of d-dimensional matrices, Linear Algebra
Appl. 90 (1987) 133–145.
13


## Page 14


[17] S.J. Dow and P.M. Gibson, An upper bound for the permanent of a 3-dimensional
(0,1)-matrix, Proc. Amer. Math. Soc. 99 (1987), no. 1, 29–34.
[18] P. Fischer and E.R. Swart, Three dimensional line stochastic matrices and ex-
treme points, Linear Algebra Appl. 69 (1985) 179–203.
[19] I.M. Gelfand, M.M. Kapranov, and A.V. Zelevinsky, Discriminants, Resul-
tants and Multidimensional Determinants, Reprint of the 1994 Edition (Modern
Birkhuser Classics), Boston.
[20] S. Hu, Z.-H. Huang, C. Ling, and L. Qi, On determinants and eigenvalue theory
of tensors, J. Symbolic Comput. 50 (2013) 508–531.
[21] W.B. Jurkat and H.J. Ryser, Extremal Conﬁgurations and Decomposition Theo-
rems, J. Algebra 8 (1968) 194–222.
[22] R. Ke, W. Li and M. Xiao, Characterization of Extreme Points of Multi-Stochastic
Tensors, Comput. Methods Appl. Math. 16 (2016) 459–274.
[23] Y. Liang, R. Ke, W. Li, and L. Cui, On the extreme point of m-stochastic tensors,
manuscript, 2017.
[24] T.G. Kolda and B.W. Bader, Tensor Decompositions and Applications, SIAM
Review, 51(3) (2009) 455–500.
[25] Z. Li, F. Zhang and X.-D. Zhang, On the number of vertices of the stochastic
tensor polytope, Linear Multilinear Algebra 65 (2017) 2064–2075.
[26] L.-H. Lim, Tensors and Hypermatrices, Chapter 15 in Handbook of Linear Alge-
bra, Second Edition, edited by Leslie Hogben, Chapman and Hall/CRC 2013.
[27] N. Linial and Z. Luria, An upper bound on the number of high-dimensional
permutations, Combinatorica 34 (2014), no. 4, 471–486.
[28] E. Marchi and P. Tarazaga, About (k, n) stochastic matrices, Linear Algebra Appl
26 (1979) 1530.
[29] R. Merris, Trace functions I, Duke Math. J. 38 (1971) 527–530.
[30] H.
Minc,
Theory
of
permanents
1978-1981,
Linear
Multilinear
Algebra
12(1983)227–263.
[31] R. Oldenburger, Higher dimensional determinants, Amer. Math. Monthly Vol. 47,
No. 1 (Jan., 1940) 25–33
[32] L. Qi and Z. Luo, Tensor analysis. Spectral theory and special tensors, Society
for Industrial and Applied Mathematics, Philadelphia, PA, 2017.
[33] G. Schrage, Some inequalities for multidimensional (0, 1)-matrices, Discrete
Math. 23 (1978) 169–175.
[34] J. Shao, H. Shan and L. Zhang, On some properties of the determinants of tensors.
Linear Algebra Appl. 439 (2013), no. 10, 3057–3069.
[35] A.A. Taranenko, Permanents of multidimensional matrices: properties and appli-
cations. (Russian) Diskretn. Anal. Issled. Oper. 23 (2016), no. 4, 35–101; trans-
lation in J. Appl. Ind. Math. 10 (2016), no. 4, 567–604.
[36] M.C. Tichy, Sampling of partially distinguishable bosons and the relation to the
multidimensional permanent, Phys. Rev. A 91, 022316 (2015).
[37] F. Zhang, Matrix Theory: Basic Results and Techniques, Springer, New York,
2nd edition, 2011.
14


## Page 15


[38] F. Zhang, Matrix Theory: Basic Results and Techniques, Springer, New York,
2nd edition, 2011.
[39] F. Zhang, An update on a few permanent conjectures, Special Matrices 4 (2016)
305–316.
15

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1806_00002_the_permanent_functions_of_tensors
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1806_00002_THE_PERMANENT_FUNCTIONS_OF_TENSORS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 910.0919
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 0910.0919_On_local_cohomology_of_a_tetrahedral_curve

> Source: 0910.0919_On_local_cohomology_of_a_tetrahedral_curve.pdf

> Pages: 16

---


## Page 1


arXiv:0910.0919v1  [math.AC]  6 Oct 2009
On local cohomology of a tetrahedral curve
Dˆo Ho`ang Giang and Lˆe Tuˆan Hoa
Institute of Mathematics Hanoi, 18 Hoang Quoc Viet Road, 10307 Hanoi,
Vietnam
Abstract
It is shown that the diameter diam(H1
m(R/I)) of the ﬁrst local cohomology module
of a tetrahedral curve C = C(a1, ..., a6) can be explicitly expressed in terms of the ai
and is the smallest non-negative integer k such that mkH1
m(R/I) = 0. From that one
can describe all arithmetically Cohen-Macaulay or Buchsbaum tetrahedral curves.
Key words: Local cohomology, Cohen-Macaulay, Buchsbaum, tetrahedral curve,
Fourier-Motzkin.
2000 Mathematics Subject Classiﬁcation: Primary 13D45, 14M25
Introduction
A tetrahedral curve C = C(a1, ..., a6) is a curve in P3 deﬁned by the ideal
I = (x1, x2)a1 ∩(x1, x3)a2 ∩(x1, x4)a3 ∩(x2, x3)a4 ∩(x2, x4)a5 ∩(x3, x4)a6
of the polynomial ring R = K[x1, x2, x3, x4] over a ﬁeld K, where a1, ..., a6
are non-negative integers and not all of them are zero. The case a2 = a5 =
0 was ﬁrst considered by Schwartau [7]. He gave a characterization of the
Cohen-Macaulay property of C in terms of a1, a3, a4, a6. The general case of
tetrahedral curves, when a2 and a5 are not necessarily zero, was introduced
in [6]. Using basic double linkage, Migliore and Nagel gave there an eﬃcient
numerical algorithm for determining when a particular tetrahedral curve is
arithmetically Cohen-Macaulay and asked for an explicit characterization in
terms of a1, ..., a6. This problem was solved later by Francisco in [3]. Moreover,
it was shown in the papers [6,4] that these curves have many nice properties.
⋆Both authors were supported by NAFOSTED (Vietnam)
Email addresses: dhgiang@math.ac.vn (Dˆo Ho`ang Giang), lthoa@math.ac.vn
(Lˆe Tuˆan Hoa).
Preprint submitted to Elsevier
30 October 2018


## Page 2


In this paper we study the structure of the ﬁrst local cohomology module
H1
m(R/I) with the support in the maximal homogeneous ideal m = (x1, x2, x3, x4).
This study is important because we can characterize many properties, such as
the Cohen-Macaulayness or the Buchsbaumness, of C in terms of H1
m(R/I).
Recall that the diameter of a Z-graded module M of ﬁnite length is the in-
teger diam(M) = max{n| Mn ̸= 0} −min{n| Mn ̸= 0} + 1 (diam(M) := 0 if
M = 0). Let J be the deﬁning ideal of an arbitrary projective curve X in P3.
Then the module H1
m(R/J) is of ﬁnite length and let k(R/J) be the smallest
non-negative integer k such that mkH1
m(R/J) = 0 (see [5,1]). It is obvious
that k(R/J) ≤diam(H1
m(R/J)). The main result of this paper states that
k(R/I) = diam(H1
m(R/I)) for an arbitrary tetrahedral curve (see Theorem
3.4). Thus our result implies that for all tetrahedral curves, diam(H1
m(R/I))
has no gap and k(R/I) is, in this sense, as large as possible. (Note that mono-
mial curves in P3 also have this property, see [1].) Moreover, we can explicitly
compute diam(H1
m(R/I)) in terms of a1, ..., a6 (see Theorem 3.2 and Theo-
rem 3.4). Since C is an arithmetically Cohen-Macaulay curve if and only if
diam(H1
m(R/I)) = 0, this result is much more general than the Francisco’s
one in [3]. In particular, it also enables us to determine all arithmetically
Buchsbaum tetrahedral curves (Theorem 3.7), thus extending Corollary 5.4 in
[6].
Our approach is to reduce the above question to a problem in integer program-
ming. First, based on a description of local cohomology modules of monomial
ideals given recently in [9], we reduce the problem to describing the set of
integer solutions of a certain linear constraints. Then using the well-known
Fourier-Motzkin elimination we can determine when the set of solutions is
empty (Theorem 3.2). This is corresponding the case of arithmetically Cohen-
Macaulay curves. If this set is not empty, we can still use it to determine
the module structure of the ﬁrst local cohomology (Proposition 3.3). Thus
our result is not only an interesting application of integer programming to
Commutative Algebra, but it also shows the usefulness of Takayama’s for-
mula in [9]. We believe that Takayama’s formula, which is a generalization of
Hochster’s formula, can be applied in many other situations.
The paper has four sections with the current one being an introduction. In
Section 1 we recall the main result of Takayama in [9] and relate the problem
of describing H1
m(R/I) to a problem in integer programming (Lemma 1.4).
In Section 2 we apply the Fourier-Motzkin elimination to solve that integer
programming problem. The structure of the ﬁrst local cohomology module is
given in the last Section 3, where the main Theorem 3.4 is proved and some
of its consequences are derived.
2


## Page 3


1
Preliminaries
Let I ⊂R = K[x1, ..., xn] be a monomial ideal. Denote by G(I) the minimal
set of monomial generators of I. Let ∆be the simplicial complex corresponding
to the radical ideal
√
I, i.e.
∆= {{i1, ..., ik} ⊆{1, ..., n}| xi1 · · ·xik ̸∈
√
I}.
A simplicial complex is uniquely deﬁned by the set Max(∆) of its facets.
Following [9], for α = (α1, ..., αn) ∈Zn, we set
Gα = {i| αi < 0},
and
∆α = {F ⊂{1, ..., n} \ Gα|
for all xβ = xβ1
1 · · · xβn
n ∈G(I) there exists
i ̸∈F ∪Gα such that βi > αi ≥0}.
Lemma 1.1 Denote by I(xi1...xik) the monomial ideal generated by I in the lo-
calization K[x](xi1...xik) w.r.t. the set of all monomials in the variables xi1, ..., xik.
Then
∆α = {F ⊂{1, ..., n} \ Gα|
Y
i̸∈F ∪Gα
xαi
i
̸∈I(Q
j∈F ∪Gα xj)}.
PROOF. For simplicity we may assume that F ∪Gα = {1, ..., r}. For a
monomial m ∈K[x1, ..., xn] let m′ ∈K[xr+1, ..., xn] be the monomial obtained
from m by deleting all powers of xi, i ≤r. Let G′ = {m′| m ∈G(I)}. Then
G′ is a generating set of I′ := I(x1...xr). Note that the monomial
Q
i>r xαi
i
∈I′
if and only if there exists m′ = Q
i>r xβi
i ∈G′ such that βi ≤αi for all i > r, or
equivalently, there exists m =
Qn
i=1 xβi
i ∈G(I) such that βi ≤αi for all i > r.
From that we immediately get the claim.
□.
Note that all local cohomology modules Hi
m(R/I), i ≥0, inherit a natural
Zn-grading. Theorem 1 in [9] can be reformulated as follows.
Lemma 1.2 Let ρi = max{βi| xβ ∈G(I)}. For all i ≥0 and α ∈Zn we have
dim Hi
m(R/I)α =



dim ˜Hi−|Gα|−1(∆α, K)
if Gα ∈∆and αj ≤ρj −1, j ≤n,
0
otherwise.
From now on we consider ideals of tetrahedral curves
I = (x1, x2)a1 ∩(x1, x3)a2 ∩(x1, x4)a3 ∩(x2, x3)a4 ∩(x2, x4)a5 ∩(x3, x4)a6
3


## Page 4


of the polynomial ring R = K[x1, x2, x3, x4].
Lemma 1.3 If H1
m(R/I)α ̸= 0, then αi ≥0 for all i ≥1 and
Max(∆α) = {{1, i}, {j, k}| {i, j, k} = {2, 3, 4}}.
PROOF. Assume H1
m(R/I)α ̸= 0. By Lemma 1.2, either Gα = ∅and ∆α is
disconnected, or |Gα| = 1 and ∆α = {∅}.
If |Gα| = 1, w.l.o.g. we may assume that Gα = {1}, i. e. α1 < 0 and α2, α3, α4 ≥
0. By Lemma 1.1, ∆α = {∅} is equivalent to the following two conditions
(i) xα2
2 xα3
3 xα4
4 ̸∈I(x1) = (x2, x3)a4 ∩(x2, x4)a5 ∩(x3, x4)a6, and
(ii) xαi
i x
αj
j
∈I(x1,xk) for all {i, j, k} = {2, 3, 4}.
This is impossible, because
(i) ⇔


α2 + α3 ≤a4 −1, or
α2 + α4 ≤a5 −1, or
α3 + α4 ≤a6 −1,
and (ii) ⇔













α2 + α3 ≥a4, and
α2 + α4 ≥a5, and
α3 + α4 ≥a6.
Hence we must have Gα = ∅and ∆α is disconnected. The ﬁrst condition
implies that αi ≥0 for all i ≥1. Since ∆α is a disconnected simplicial complex
on a subset of {1, 2, 3, 4}, in order to show the second statement of the lemma
it suﬃces to show that ∆α does not contain a facet consisting of a single point.
Assume, by contrary, that {1} is a facet of ∆α. Then we again get (i) and (ii)
(the only diﬀerence now is that all αi ≥0 which, however, have no eﬀect on
(i) and (ii)). This is a contradiction.
□
As an example let us consider the well-known Buchsbaum curve deﬁned by
I = (x1, x2)∩(x3, x4). In this case H1
m(R/I)α ̸= 0 if and only if α = (0, 0, 0, 0).
We have Max(∆(0,0,0,0)) = {{1, 2}, {3, 4}}.
Lemma 1.4 Fix an integer d. Assume that deg(α) := α1+· · ·+α4 = d. Then
Max(∆α) = {{1, 2}, {3, 4}} if and only if α satisﬁes the following system of
inequalities
(1)
α1 + α3 ≥a2
α1 + α4 ≥a3
α2 + α3 ≥a4
α2 + α4 ≥a5
4


## Page 5


α1 + α2 ≤a1 −1
α3 + α4 ≤a6 −1
α1 + α2 + α3 + α4 = d
α1, α2, α3, α4 ≥0.
In this case dim H1
m(R/I)α = 1.
PROOF. The condition Max(∆α) = {{1, 2}, {3, 4}} implies Gα = ∅, i.e.
α1, α2, α3, α4 ≥0. By Lemma 1.1, {1, 2} ∈∆α if and only if xα3
3 xα4
4
̸∈
(x3, x4)a6, or equivalently, α3 + α4 ≤a6 −1. Similarly, {3, 4} ∈∆α if and
only if α1 + α2 ≤a1 −1. On the other hand, {1, 3}, {1, 4}, {2, 3}, {2, 4} ̸∈∆α
are equivalent to the ﬁrst four inequalities given above. Thus, Max(∆α) =
{{1, 2}, {3, 4}} implies (1). The converse is also clear from these arguments.
When Max(∆α) = {{1, 2}, {3, 4}} we have ˜H0(∆α, K) ∼= K and |Gα| = 0.
Hence, by Lemma 1.2, dim H1
m(R/I)α = 1, as required.
□
2
Fourier-Motzkin elimination
By Lemma 1.4 we are interested in ﬁnding an integer solution of the following
system of inequalities
(2)
y1 + y3 ≥a2
y1 + y4 ≥a3
y2 + y3 ≥a4
y2 + y4 ≥a5
y1 + y2 ≤a1 −1
y3 + y4 ≤a6 −1
y1 + y2 + y3 + y4 = d
y1, y2, y3, y4 ≥0.
For this purpose we apply the Fourier-Motzkin elimination which at ﬁrst en-
ables to ﬁnd a real solution of a system of linear equalities and inequalities, see,
e.g. [2], Section 2.3. We sketch here the algorithm by considering a concrete
example.
5


## Page 6


Example. Consider the system
(3)
y1 + 2y2 −y3 + 4 ≥0
−2y1 + y2 + 3y3 −2 ≥0
2y2 −y3 ≥0
y1 = y2 + y3.
First, replace the equality y1 = y2 + y3 by two inequalities y1 ≥y2 + y3 and
y1 ≤y2 +y3. The obtained system is not reduced w.r.t. y1, i.e. y1 appears with
a non-zero coeﬃcient in at least one inequality. After dividing by the absolute
value of the coeﬃcient of y1 when nonzero and rearranging the terms and the
order of the constraints, we can then partition them in 3 groups, depending
on whether in a particular constraint y1 is on the right or the left hand, or its
y1-coeﬃcient is zero.
1
2y2 + 3
2y3 −1 ≥y1
(E1)
y2 + y3 ≥y1
(E2)
y1 ≥−2y2 + y3 −4
(E3)
y1 ≥y2 + y3
(E4)
2y2 −y3 ≥0.
(E5)
Combining each inequality in the ﬁrst group {(E1), (E2)} with another one
in the second group {(E3), (E4)} and keep all inequalities in the third group
({(E5)} in this example), we obtain a new system of inequalities
1
2y2 + 3
2y3 −1 ≥−2y2 + y3 −4
(E1, E3)
1
2y2 + 3
2y3 −1 ≥y2 + y3
(E1, E4)
y2 + y3 ≥−2y2 + y3 −4
(E2, E3)
y2 + y3 ≥y2 + y3
(E2, E4)
2y2 −y3 ≥0.
(E5)
The temporary label (E1, E3) means that this inequality appears by com-
bining (E1) and (E3). Note that in the last system, (E1, E3) follows from
(E1, E4) and (E2, E3). For short, we will write this reduction as (E1, E4) +
(E2, E3) ⇒(E1, E3). The constraint (E2, E4) trivially holds. We say that
(E1, E3) and (E2, E4) are redundant. Deleting the redundant inequalities, we
6


## Page 7


ﬁnally get the system
(4)
1
2y2 + 3
2y3 −1 ≥y2 + y3
y2 + y3 ≥−2y2 + y3 −4
2y2 −y3 ≥0.
Thus (3) implies (4), where y1 appears with zero coeﬃcient in all inequalities.
We say that y1 has been ”eliminated”. The process is repeated with the new
system except now y2 is eliminated.
We now apply the Fourier-Motzkin elimination to our system (2). First rewrite
it in the form
(5)
a6 −1 −y3 ≥y4
y4 = d −y1 −y2 −y3
y4 ≥a3 −y1
y4 ≥a5 −y2
y4 ≥0
y1 + y3 ≥a2
y1 + y2 ≤a1 −1
y2 + y3 ≥a4
y1, y2, y3 ≥0.
Eliminating y4 we then get
(6)
d −a3 −y2 ≥y3
d −a5 −y1 ≥y3
d −y1 −y2 ≥y3
y3 ≥0
y3 ≥a2 −y1
y3 ≥a4 −y2
y1 + y2 + a6 −d −1 ≥0
y1 + y2 ≤a1 −1
y1, y2 ≥0.
Eliminating y3 we now obtain
7


## Page 8


(7)
d −a3 ≥y2
(7.1)
d −a2 −a3 + y1 ≥y2
(7.2)
d −y1 ≥y2
(7.3)
d −a2 ≥y2
(7.4)
a1 −1 −y1 ≥y2
(7.5)
y2 ≥0
(7.6)
y2 ≥a4 + a5 −d + y1
(7.7)
y2 ≥d + 1 −a6 −y1
(7.8)
d −a5 ≥y1
(7.9)
d −a4 ≥y1
(7.10)
y1 ≥0
(7.11)
d ≥a3 + a4
(7.12)
d ≥a2 + a5.
(7.13)
By eliminating y2 we get a system of 20 constraints. However 7 of them are
redundant: (7.12) ⇒(7.1, 7.6); (7.9) + (7.12) ⇒(7.1, 7.7); (7.12) + (7.13) ⇒
(7.2, 7.7); (7.9)+(7.10) ⇒(7.3, 7.6), (7.3, 7.7), (7.4, 7.7) and (7.13) ⇒(7.4, 7.6).
Deleting these redundant constraints we get
(8)
d −a4 ≥y1
(8.1)
d −a5 ≥y1
(8.2)
a1 −1 ≥y1
(8.3)
⌊1
2(d + a1 −a4 −a5 −1)⌋≥y1
(8.4)
y1 ≥0
(8.5)
y1 ≥⌈1
2(a2 + a3 −a6 + 1)⌉
(8.6)
y1 ≥a2 + a3 −d
(8.7)
y1 ≥a3 −a6 + 1
(8.8)
y1 ≥a2 −a6 + 1
(8.9)
a1 + a6 −2 ≥d
(8.10)
d ≥a2 + a5
(8.11)
8


## Page 9


d ≥a3 + a4
(8.12)
a6 ≥1.
(8.13)
Here, for a real number a, we set
⌈a⌉= min{n ∈Z| n ≥a} and ⌊a⌋= max{n ∈Z| n ≤a}.
Eliminating y1 we get a system of 24 constraints. Among them 14 are redun-
dant: (8.12) ⇒(8.1, 8.5); (8.1, 8.9) + (8.12) ⇒(8.1, 8.6); (8.11) + (8.12) ⇒
(8.1, 8.7); (8.12)+8.13) ⇒(8.1, 8.8); (8.11) ⇒(8.2, 8.5); (8.2, 8.8)+(8.11) ⇒
(8.2, 8.6); (8.11)+(8.12) ⇒(8.2, 8.7); (8.11)+(8.13) ⇒(8.2, 8.9); (8.3, 8.7)+
(8.10) ⇒(8.3, 8.6); (8.10)+(8.12) ⇒(8.3, 8.8); (8.10)+(8.11) ⇒(8.3, 8.9); (8.11)+
(8.12) + (8.3, 8.7) ⇒(8.4, 8.7); (8.10) + (8.12) + (8.2, 8.8) ⇒(8.4, 8.8) and
(8.10) + (8.11) + (8.1, 8.9) ⇒(8.4, 8.9). Deleting these redundant constraints,
we ﬁnally get the system
(9)
a1 + a6 −2 ≥d
d ≥a2 + a5
d ≥a3 + a4
d ≥a2 + a4 −a6 + 1
d ≥a3 + a5 −a6 + 1
d ≥a2 + a3 −a1 + 1
d ≥a4 + a5 −a1 + 1
⌊1
2(d + a1 −a4 −a5 −1)⌋≥⌈1
2(a2 + a3 −a6 + 1)⌉
a1, a6 ≥1.
Lemma 2.1 Assume that a1 + a6 −2 ≥d ≥max{a2 + a5, a3 + a4}. Then
⌊1
2(d + a1 −a4 −a5 −1)⌋< ⌈1
2(a2 + a3 −a6 + 1)⌉if and only if a2 + a3 −a6 is
even and a1 + a6 −2 = a2 + a5 = a3 + a4.
PROOF. If a2 + a3 −a6 is odd, then
⌈1
2(a2 + a3 −a6 + 1)⌉= 1
2(a2 + a3 −a6 + 1).
Since a2+a5+a3+a4 ≤d+a1+a6−2, we get d+a1−a4−a5−1 ≥a2+a3−a6+1,
which yields
1
2(d + a1 −a4 −a5 −1) ≥1
2(a2 + a3 −a6 + 1).
9


## Page 10


Hence
⌊1
2(d + a1 −a4 −a5 −1)⌋≥1
2(a2 + a3 −a6 + 1) = ⌈1
2(a2 + a3 −a6 + 1)⌉.
If a2 + a3 −a6 is even, then
⌈1
2(a2 + a3 −a6 + 1)⌉= 1
2(a2 + a3 −a6) + 1.
In the case a1 + a6 −2 > min{a2 + a5, a3 + a4}, we have a2 + a5 + a3 + a4 ≤
d + a1 + a6 −3. Hence d + a1 −a4 −a5 −1 ≥a2 + a3 −a6 + 2, which implies
⌊1
2(d + a1 −a4 −a5 −1)⌋≥1
2(a2 + a3 −a6) + 1 = ⌈1
2(a2 + a3 −a6 + 1)⌉.
The left case is a1 + a6 −2 = min{a2 + a5, a3 + a4}. Since a1 + a6 −2 ≥d ≥
max{a2 +a5, a3 +a4}, we must have d = a2 +a5 = a3 +a4 = a1 +a6 −2. Then
d + a1 −a4 −a5 −1 = a2 + a3 −a6 + 1 is an odd number. Therefore
⌊1
2(d + a1 −a4 −a5 −1)⌋< ⌈1
2(a2 + a3 −a6 + 1)⌉.
This completes the proof of the lemma.
□
Going back from (9) to (5), the Fourier-Motzkin algorithm gives us in general
only a rational solution of (2) if (9) holds. However, in our concrete situation
we can already ﬁnd an integer solution.
Lemma 2.2 Let
A = max{ a2 + a5, a3 + a4, a2 + a4 −a6 + 1, a3 + a5 −a6 + 1,
a2 + a3 −a1 + 1, a4 + a5 −a1 + 1}.
The system (2) has an integer solution if and only if a1, a6 ≥1 and one of the
following conditions holds:
(i) a1 + a6 −2 > A and a1 + a6 −2 ≥d ≥A.
(ii) a1 + a6 −2 = A = d and a1 + a6 −2 > min{a2 + a5, a3 + a4}.
(iii) a1 + a6 −2 = a2 + a5 = a3 + a4 = A = d and a2 + a3 −a6 is odd.
PROOF. If (2) has an integer solution, then by Fourier-Motzkin algorithm,
(9) holds. Using Lemma 2.1 we get the necessity.
Assume that a1, a6 ≥1 and one of the above conditions (i)-(iii) holds. Then
for any d such that A ≤d ≤a1 + a6 −2, the system (9) holds by Lemma
2.1. Fix such an integer d. Denote by L8 the minimum of integers in the left
10


## Page 11


sides of (8.1) −(8.4) and R8 the maximum of integers in the right sides of
(8.5) −(8.9). Then from (9) it follows that L8 ≥R8. Hence y1 = R8 is
an integer solution of (8). Putting y1 = R8 into (7)-(5) and repeating this
process, we can similarly deﬁne L7 ≥R7, L6 ≥R6, L5 ≥R5 such that
y1 = R8, y2 = R7, y3 = R6, y4 = R5 is an integer solution of (5), which is
equivalent to (2) .
□
3
Structure of the ﬁrst local cohomology module
In this section we describe the ﬁrst local cohomology module of R/I. From
now on, w.l.o.g., we always assume that a1 + a6 is the maximum among the
sums a1+a6, a2+a5, a3+a4. In other words we may assume that the following
holds:
(∗)
a1 + a6 ≥max{a2 + a5, a3 + a4}.
Lemma 3.1 Under the assumption (*) there exists no α ∈Z4 such that
Max(∆α) = {{1, 3}, {2, 4}} or Max(∆α) = {{1, 4}, {2, 3}}.
PROOF. Assume, w.l.o.g., the existence of α ∈Zn such that Max(∆α) =
{{1, 3}, {2, 4}}. Then applying Lemma 1.4 and Lemma 2.2 to this situation
we would get a2 + a5 −2 ≥a1 + a6, a contradiction to (*).
□
We can now explicitly determine all arithmetically Cohen-Macaulay tetrahe-
dral curves in terms of ai. This result recovers the main theorem in [3].
Theorem 3.2 Let
A = max{ a2 + a5, a3 + a4, a2 + a4 −a6 + 1, a3 + a5 −a6 + 1,
a2 + a3 −a1 + 1, a4 + a5 −a1 + 1}.
Under the assumption (*), a tetrahedral curve C(a1, ..., a6) is arithmetically
Cohen-Macaulay if and only if one of the following conditions holds:
(i) a1 = 0 or a6 = 0;
(ii) a1 + a6 −2 < A;
(iii) a1 + a6 −2 = a2 + a5 = a3 + a4 = A and a2 + a3 −a6 is even.
PROOF. By Lemma 3.1, C = C(a1, ..., a6) is arithmetically Cohen-Macaulay
if and only if there is no d such that the system (2) has an integer solution.
Hence the statement follows from Lemma 2.2.
□
11


## Page 12


Remark. In [6], Question 7.4(5), Migliore and Nagel asked whether an arith-
metically Cohen-Macaulay tetrahedral curve C = C(a1, ..., a6) can be explic-
itly identiﬁed by the 6-tuples a1, ..., a6. This question was solved by Francisco
in [3]. His main result says that under the assumption (*), C(a1, ..., a6) is
arithmetically Cohen-Macaulay if and only if one of the following conditions
holds:
(a) a1 = 0 or a6 = 0;
(b) a1 + a6 = ǫ + max{a2 + a5, a3 + a4}, where ǫ ∈{0, 1}.
(c) 2a1 < a2 + a3 −a6 + 3 or 2a1 < a4 + a5 −a6 + 3 or 2a6 < a2 + a4 −a1 + 3
or 2a6 < a3 + a5 −a1 + 3;
(d) All inequalities of (c) fail, a1 +a6 = a2 +a5 +2 = a3 +a4 +2 and a1 +a3 +a5
is even.
One can easily check that this statement is equivalent to that of Theorem 3.2.
Assume now that C is not arithmetically Cohen-Macaulay. Then a1, a6 ≥1
and one of three conditions in Lemma 2.2 is satisﬁed. In particular A ≤
a1 + a6 −2. Let
T1 = {y ∈N4| y1 + y3 ≥a2, y1 + y4 ≥a3, y2 + y3 ≥a4, y2 + y4 ≥a5},
T2 = {y ∈T1| y1 + y2 ≥a1},
and
T3 = {y ∈T1| y3 + y4 ≥a6}.
Let S = T1 \ (T2 ∪T3). Then the set Sd of all elements of degree d of S is
the set of all solutions of the system (2). As usual we identify K[Ti], i ≤3,
and K[S] with subsets of R = K[x1, ..., x4]. Note that K[Ti], i ≤3, are ideals
of R. Hence we may consider K[S] as a factor module K[T1]/K[T2] + K[T3].
Thus, the module structure on K[S] over R is deﬁned as follows: for α ∈S
and β ∈N4,
xβ · xα =



xβ+α
if β + α ∈S,
0
otherwise.
The following result describes the module structure of H1
m(R/I).
Proposition 3.3 Under the assumption (*),
H1
m(R/I) ∼= K[S]
as graded modules over R.
PROOF. Let
C• : 0 →R/I →⊕4
i=1(R/I)xi →· · · →(R/I)x1x2x3x4 →0,
12


## Page 13


be the ˇCech complex of R/I. Then H1
m(R/I) ∼= H1(C•). By [9], Lemma 2, for
all α ∈Z4 there is an isomorphism of complexes
(C•
α) ∼= HomZ(C(∆α)[−j −1], K),
where j = |Gα| and C(∆α)[−j −1] means the shifting of the augmented
oriented chain complex C(∆α) by −j −1. Denote by π the simplicial complex
on {1, 2, 3, 4} with Max(π) = {{1, 2}, {3, 4}}. By Lemmas 1.3, 1.4 and 3.1 it
follows that H1(C•
α) ̸= 0 if and only if ∆α = π, Gα = ∅and α ∈S. Moreover,
in this case H1(C•
α) ∼= Kxα. From this we get H1
m(R/I) ∼= K[S], as required.
□
The above description of S allows us to describe the module structure of K[S]
in an obvious way. Of course, S can be written as:
S = {y ∈N4| y1 + y3 ≥a2, y1 + y4 ≥a3, y2 + y3 ≥a4, y2 + y4 ≥a5,
y1 + y2 < a1, y3 + y4 < a6}.
It is easy to write a program to compute this set S. Hence the module structure
of H1
m(R/I) is known once a1, ..., a6 are given.
We say that a non-zero Z-graded module M has no gap if Mi ̸= 0 and Mj ̸= 0
for some i ≤j, then Mk ̸= 0 for all i ≤k ≤j. Recall that the diameter of a
module M of ﬁnite length is deﬁned as
diam(M) = end(M) −beg(M) + 1,
where beg(M) = min{i| Mi ̸= 0} and end(M) = max{i| Mi ̸= 0} (if M = 0
we set diam(M) = 0).
Theorem 3.4 Let
A = max{ a2 + a5, a3 + a4, a2 + a4 −a6 + 1, a3 + a5 −a6 + 1,
a2 + a3 −a1 + 1, a4 + a5 −a1 + 1}.
Assume that (*) holds and the tetrahedral curve C is not arithmetically Cohen-
Macaulay. Then a1 + a6 −2 ≥A and
k(R/I) = diam(H1
m(R/I)) = a1 + a6 −A −1.
In particular, H1
m(R/I) has no gap.
PROOF. Since R/I is not a Cohen-Macaulay ring, by Theorem 3.2, a1 +
a6 −2 ≥A and a1, a6 ≥1. By Lemma 2.2, for each d such that A ≤d ≤
13


## Page 14


a1 + a6 −2 we have Sd ̸= ∅. Hence, by Proposition 3.3, H1
m(R/I) has no
gap, beg(H1
m(R/I)) = A and end(H1
m(R/I)) = a1 + a6 −2, which implies
diam(H1
m(R/I)) = a1 + a6 −A −1.
Further, let α = (α1, α2, α3, α4) ∈SA be a ﬁxed element. Then α1 + α2 ≤
a1 −1 and α3 + α4 ≤a6 −1. Let α∗= (α1, a1 −1 −α1, α3, a6 −1 −α3).
Since a1 −1 −α1 ≥α2 and a6 −1 −α3 ≥α4, the condition α ∈T1 implies
α∗∈T1 too. On the other hand α∗̸∈T1 ∪T2. Hence α∗∈Sa1+a6−2. Note that
α∗= α + β, where β = (0, a1 −1 −α1 −α2, 0, a6 −1 −α3 −α4) ∈N4 and
deg(β) = a1 + a6 −A −2. Therefore, by Proposition 3.3,
xβH1
m(R/I)α ∼= H1
m(R/I)α+β = H1
m(R/I)α∗̸= 0,
which yields
k(R/I) ≥a1 + a6 −A −1 = diam(H1
m(R/I)).
Since diam(H1
m(R/I)) ≥k(R/I), we ﬁnally get k(R/I) = diam(H1
m(R/I)), as
required.
□
In the above proof we already showed:
Corollary 3.5 Assume that (*) holds and the tetrahedral curve C is not
arithmetically Cohen-Macaulay. Then a1 + a6 −2 ≥A and end(H1
m(R/I)) =
a1 + a6 −2.
Recall that C is arithmetically Buchsbaum if and only if k(R/I) ≤1. As an
immediate consequence of Theorem 3.4 we recover Corollary 4 in [6].
Corollary 3.6 A tetrahedral curve C is arithmetically Buchsbaum if and only
if
H1
m(R/I) ∼= Km(t),
for some non-negative integers m, t.
Migliore and Nagel found all arithmetically Buchsbaum tetrahedral curves
which are so-called minimal (see Corollary 3.8 below). Using Theorem 3.4 and
3.2 we are able to determine all arithmetically Buchsbaum tetrahedral curves
which are not necessarily minimal.
Theorem 3.7 Under the assumption (*), a tetrahedral curve C is arithmeti-
cally Buchsbaum if and only if one of the following conditions is satisﬁed:
(i) a1 = 0 or a2 = 0;
(ii) a1 + a6 −2 ≤A.
14


## Page 15


PROOF. If C is arithmetically Cohen-Macaulay, by Theorem 3.2, one of the
above condition holds. Assume that C is not arithmetically Cohen-Macaulay
and arithmetically Buchsbaum. Then k(R/I) = 1. By Theorem 3.4, a1, a6 ≥1
and a1 + a6 −2 = A. Conversely, by Theorem 3.2 we may assume from the
beginning that a1, a6 ≥1. Under these conditions, again by Theorem 3.4,we
immediately have k(R/I) ≤1, i.e. C is arithmetically Buchsbaum.
□
Migliore and Nagel introduced the following notion: Assume that
a6 = max{a1, ..., a6}. A tetrahedral curve C is said to be minimal if a1 >
max{a2 + a4, a3 + a5} and a6 > max{a2 + a3, a4 + a5} (see [6], Deﬁnition
3.4 and Corollary 3.5). Note that in this case we already have a1, a6 ≥1 and
a1 + a6 −2 ≥A.
Corollary 3.8 ([6], Corollary 4.3 and Corollary 5.4). Assume that
a6 = max{a1, ..., a6} and C is a minimal tetrahedral curve. Then
(i) C is not arithmetically Cohen-Macaulay.
(ii) C is arithmetically Buchsbaum if and only if either a2 = a5 = 0 and a1 =
a6 = a3 + 1 = a4 + 1 or a3 = a4 = 0 and a1 = a6 = a2 + 1 = a5 + 1.
PROOF. Since a1 > max{a2 + a4, a3 + a5} and a6 > max{a2 + a3, a4 + a5},
we have
(10)
a1 + a6 −2 ≥max{ a2 + a5 + 2a4, a2 + a5 + 2a3,
a3 + a4 + 2a2, a3 + a4 + 2a5} ≥A.
If C is arithmetically Buchsbaum, then since a1, a6 ≥1, by Theorem 3.2 and
Theorem 3.7, we must have a1 + a6 −2 = A. Combining with (10) it implies
that either a2 = a5 = 0 or a3 = a4 = 0. W.l.o.g. assume that a2 = a5 = 0.
Then A = a3 + a4 and a1 + a6 −2 = a3 + a4. Since a1, a6 > max{a3, a4}, the
later equality gives a1 = a6 = a3 +1 = a4 +1. In this case a2 +a3 −a6 = −1 is
odd, so C is not arithmetically Cohen-Macaulay. Thus we have proved (i) and
the necessity of (ii). The suﬃciency of (ii) immediately follows from Theorem
3.7.
□
Similarly, using Theorem 3.4, we can quickly get
Corollary 3.9 ([6], Lemma 6.2). Assume that a6 = max{a1, ..., a6} and C is
a minimal tetrahedral curve. Then diam(H1
m(R/I)) = 2 if and only if after a
suitable permutation of variables we have (a1, ..., a6) = (k, k −1, 0, 0, k −1, k +
1), k ≥1 or (a1, ..., a6) = (k, k −2, 0, 0, k −1, k), k ≥2.
15


## Page 16


References
[1]
H. Bresinsky, F. Curtis, M. Fiorentini and L. T. Hoa, On the structure of local
cohomology modules for monomial curves in P3
k, Nagoya Math. J. 136(1994),
81–114; MR1309382 (96b:14040).
[2]
G. B. Dantzig and M. N. Thapa, Linear Programming 1: Introduction,
Springer Verlag 1997; MR1485773 (98m:90081).
[3]
C. A. Francisco, Tetrahedral curves via graphs and Alexander duality, J. Pure
Appl. Algebra 212 (2008), no. 2, 364–375; MR2357338.
[4]
C. A. Francisco, J. C. Migliore and U. Nagel, On the componentwise linearity
and the minimal free resolution of a tetrahedral curve, J. Algebra 299(2006),
535–569; MR2228326 (2007f:13021).
[5]
J. C. Migliore and R. M. Mir´o-Roig, On k-Buchsbaum curves in P3, Comm.
in Algebra 18(1990), 2403–2422; MR1074235 (91i:14025).
[6]
J. C. Migliore and U. Nagel, Tetrahedral curves, Int. Math. Res. Not. No.
15(2005), 899–939; MR2147092 (2005m:14087).
[7]
P. Schwartau, Liaison addition and monomial ideals, PhD thesis, Brandeis
University, 1982.
[8]
J. St¨uckrad and W. Vogel, Buchsbaum rings and applications. An interaction
between algebra, geometry and topology. Springer-Verlag, Berlin, 1986;
MR0881220 (88h:13011a).
[9]
Y.
Takayama,
Combinatorial
characterizations
of
generalized
Cohen-
Macaulay monomial ideals, Bull. Math. Soc. Sci. Math. Roumanie (N. S.)
48 (96)(2005), 327–344; MR2165349 (2006e:13017) .
16

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]

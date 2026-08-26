---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1808.01975
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1808.01975_A_Survey_on_Surrogate_Approaches_to_Non-negative_Matrix_Factorization

> Source: 1808.01975_A_Survey_on_Surrogate_Approaches_to_Non-negative_Matrix_Factorization.pdf

> Pages: 37

---


## Page 1


Vietnam Journal of Mathematics manuscript No.
(will be inserted by the editor)
A Survey on Surrogate Approaches to Non-negative
Matrix Factorization
Pascal Fernsel · Peter Maass
Abstract Motivated by applications in hyperspectral imaging we investigate meth-
ods for approximating a high-dimensional non-negative matrix Y by a product
of two lower-dimensional, non-negative matrices K and X . This so-called non-
negative matrix factorization is based on deﬁning suitable Tikhonov functionals,
which combine a discrepancy measure for Y ≈KX with penalty terms for en-
forcing additional properties of K and X .
The minimization is based on alternating minimization with respect to K or X ,
where in each iteration step one replaces the original Tikhonov functional by a
locally deﬁned surrogate functional. The choice of surrogate functionals is crucial:
It should allow a comparatively simple minimization and simultaneously its ﬁrst
order optimality condition should lead to multiplicative update rules, which auto-
matically preserve non-negativity of the iterates.
We review the most standard construction principles for surrogate functionals for
Frobenius-norm and Kullback-Leibler discrepancy measures. We extend the known
surrogate constructions by a general framework, which allows to add a large vari-
ety of penalty terms.
The paper ﬁnishes by deriving the corresponding alternating minimization schemes
explicitely and by applying these methods to MALDI imaging data.
Keywords Non-negative matrix factorization · Multi-parameter regularization ·
Surrogate approaches · MM algorithms · Orthogonal NMF · Supervised NMF ·
MALDI mass spectrometry
P. Fernsel
Center for Industrial Mathematics, University of Bremen, D-28334 Bremen, Germany
Tel.: +49-421-218-63814
E-mail: pfernsel@math.uni-bremen.de
P. Maass
Center for Industrial Mathematics, University of Bremen, D-28334 Bremen, Germany
Tel.: +49-421-218-63 801
Fax.: 49-421-218-98 63 801
E-mail: pmaass@math.uni-bremen.de
arXiv:1808.01975v2  [cs.LG]  9 Aug 2018


## Page 2


2
Pascal Fernsel, Peter Maass
1 Introduction
Matrix factorization methods for large scale data sets have seen increasing scientiﬁc
interest recently due to their central role for a large variety of machine learning
tasks. The main aim of such approaches is to obtain a low-rank approximation
of a typically large data matrix by factorizing it into two smaller matrices. One
of the most widely used matrix factorization method is the principal component
analysis (PCA), which uses the singular value decomposition (SVD) of the given
data matrix.
In this work, we review the particular case of non-negative matrix factorization
(NMF), which is favorable for a range of applications where the data under inves-
tigation naturally satisﬁes a non-negativity constraint. These include dimension
reduction, data compression, basis learning, feature extraction as well as higher
level tasks such as classiﬁcation or clustering [11,26,27,30]. PCA based approaches
without any non-negativity constraints would not lead to satisfactory results in
this case since possible negative entries of the computed matrices cannot be easily
interpreted for naturally non-negative datasets.
Typically, the NMF problem is formulated as a minimization problem. The corre-
sponding cost function includes a suitable discrepancy term, which measures the
diﬀerence between the data matrix and the calculated factorization, as well as
penalty terms to tackle the non-uniqueness of the NMF, to deal with numerical
instabilities but also to provide the matrices with desirable properties depending
on the application task. The NMF cost functions are commonly non-convex and
require tailored minimization techniques to ensure the minimization but also the
non-negativity of the matrix iterates. This leads us to the so called surrogate min-
imization approaches, which are also known as majorize-minimization algorithms
[18,23,36]. Such surrogate methods have been investigated intensively for some of
the most interesting discrepancy measures and penalty terms [11,13,16,23,25,33,
36]. The idea is to replace the original cost function by a so called surrogate func-
tional, such that its minimization induces a monotonic decrease of the objective
function. It should be constructed in such a way that it is easier to minimize and
that the deduced update rules should preserve the non-negativity of the iterates,
which typically leads to alternating, multiplicative update rules.
It appears, that these constructions are obtained case-by-case employing diﬀerent
analytical approaches and diﬀerent motivations for their derivation. The purpose
of this paper, ﬁrst of all, is to give a uniﬁed approach to surrogate constructions for
NMF discrepancy functionals. This general construction principle is then applied
to a wide class of functionals obtained by diﬀerent combinations of divergence
measures and penalty terms, thus extending the present state of the art for surro-
gate based NMF-constructions.
Secondly, one needs to develop minimization schemes for these functionals. Here
we develop concepts for obtaining multiplicative minimization schemes, which au-
tomatically preserve non-negativity without the need for further projections.
Finally, we exemplify some characteristic properties of the diﬀerent functionals
with MALDI imaging data, which are particularly high-dimensional and challeng-
ing hyperspectral data sets.
The paper is organized as follows. Section 2 introduces the basic deﬁnition of the
considered NMF problems. Section 3 gives an overview about the theory of surro-
gate functionals as well as the construction principles. This is then exempliﬁed in


## Page 3


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
3
Section 4 for the most important cases of discrepancy terms, namely the Frobe-
nius norm and the Kullback-Leibler divergence as well as for a variety of penalty
terms. Section 5 discusses alternating minimization schemes for these general func-
tionals with the aim to obatin non-negativity-preserving, multiplicative iterations.
Finally, Section 6 contains numerical results for MALDI imaging data.
1.1 Notation
Throughout this work, we will denote matrices in bold capital Latin or Greek
letters (e.g. Y , K, Ψ, Λ) while vectors will be written in small bold Latin or
Greek letters (e.g. c, d, β, ζ). The entries of matrices and vectors will be indicated
in a non-bold format to distinguish between the i-th entry xi of a vector x and n
diﬀerent vectors x j for j = 1, . . . , n. In doing so, we write for the entry of a matrix
M in the i-th row and the j-th column Mij and the i-th entry of a vector x the
symbol xi. The same holds for an entry of a matrix product: the ij-th entry of the
matrix product MN will be indicated as (MN)ij.
Furthermore, we will use a dot notation to indicate rows and columns of matrices.
For a matrix M we will write M •,j for the j-th column and M i,• for the i-th row
of the matrix.
What is more, we will use ∥· ∥for the usual Euclidean norm, ∥M ∥1 := P
ij |Mij|
for the 1-norm and ∥M ∥F for the Frobenius norm of a matrix M .
Besides that, we will use equivalently the terms function and functional for a
mapping into the real numbers.
Finally, the dimensions of the matrices in the considered NMF problem are reused
in this work and will be introduced in the following section.
2 Non-negative Matrix Factorization
Before we introduce the basic NMF problem, we give the following deﬁnition to
clarify the meaning of a non-negative matrix.
Deﬁnition 1 A matrix M ∈Rm×n is called non-negative if M ∈Rm×n
≥0
, where
R≥0 := {x ∈R : x ≥0}.
The non-negativity of an arbitrary matrix M will be abbreviated for simplicity as
M ≥0 in the later sections of this work.
The basic NMF problem requires to approximately decompose a given non-negative
matrix Y ∈Rn×m
≥0
into two smaller non-negative matrix factors K ∈Rn×p
≥0
and
X ∈Rp×m
≥0
, such that p ≪min(n, m) and
Y ≈KX .
For an interpretation let us assume, that we are given m data vectors Y •,j ∈Rn
for j = 1, . . . , m, which are stored column-wise in the matrix Y . Similarly for
k = 1, . . . , p we denote by K •,k, respectively X k,•, the column vectors of K,
respectively the row vectors of X . We then obtain the following approximation for


## Page 4


4
Pascal Fernsel, Peter Maass
the column vectors Y •,j as well as the row vectors Y i,• :
Y •,j ≈
p
X
k=1
K •,kXkj,
Y i,• ≈
p
X
k=1
KikX k,•,
Y ≈KX =
p
X
k=1
K •,kX k,•.
Note that the product K •,kX k,• on the right hand side of the third equation
yields rank-one matrices for every k.
By these representations, we can regard the rows X k,• as a low-dimensional set
of basis vectors, which are tailored for approximating the high-dimensional data
vectors, i.e. NMF solves the task of basis learning with non-negativity constraints.
Following the interpretation given above, we can also regard NMF as a basis for
compression. K and X are determined by storing (n+m)·p coeﬃcients, as opposed
to n · m coeﬃcients for Y . The columns of K can be regarded as characteristic
components of the given data set {Y •,j}j. If these data vectors are input for a
classiﬁcation task, one can use the p correlation values with the column vectors of
K as features for constructing the classiﬁcation scheme, which yields eﬃcient and
qualitatively excellent classiﬁcations, see [26,30,34].
The standard variational approach for constructing an NMF is to deﬁne a suitable
discrepancy measure D(·, ·) between Y and KX and to minimize the resulting
functional. Despite their seemingly simple structure NMF problems are ill-posed,
non-linear and non-convex, i.e. they require stabilization techniques as well as tai-
lored approaches for minimization. In this paper, we consider discrepancy measures
based on divergences [17].
Deﬁnition 2 (Divergence) Let Ωbe an arbitrary set. A divergence D is a
map D : Ω× Ω→R, which fulﬁlls the following properties:
(i) D(x, y) ≥0
∀(x, y) ∈Ω× Ω
(ii) D(x, y) = 0 ⇔x = y
Deﬁnition 3 (β-divergence) The β-divergence dβ : R>0 × R>0 →R≥0 for
β ∈R is deﬁned as
dβ(x, y) :=


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


xβ
β(β −1) + yβ
β −xyβ−1
β −1
for β ∈R \ {0, 1},
x log
x
y

−x + y
for β = 1,
x
y −log
x
y

−1
for β = 0.
(1)
Furthermore, we deﬁne accordingly Dβ : Rn×m
>0
× Rn×m
>0
→R for arbitrary m, n ∈
N as
Dβ(M , N ) =
n
X
i=1
m
X
j=1
dβ(Mij, Nij).
(2)


## Page 5


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
5
The corresponding matrix divergences are deﬁned componentwise, i.e. β = 2 yields
the Frobenius norm and β = 1 the Kullback-Leibler divergence.
These discrepancy measures are typically amended by so called penalty terms for
stabilization and for enforcing additional properties such as sparsity or orthogo-
nality. This yields the following general minimization task.
Deﬁnition 4 (NMF Minimization Problem) For a data matrix Y ∈Rn×m
≥0
,
we consider the following generalized NMF minimization task
min
K≥0,X ≥0 Dβ(Y , KX ) +
L
X
ℓ=1
αℓϕℓ(K, X ).
(3)
The functional
F(K, X ) := Dβ(Y , KX ) +
L
X
ℓ=1
αℓϕℓ(K, X )
(4)
is called the cost functional. Furthermore, we call
(i) Dβ(Y , KX ) the discrepancy term,
(ii) αℓthe regularization parameters or weights
(iii) and ϕℓ(K, X ) the penalty terms.
The functional in (4) is typically non-convex in (K, X ). Hence, algortihms based
on alternating minimization with respect to K or X are favourable, i.e.
K [d+1] = arg min
K≥0 F(K, X [d]),
(5)
X [d+1] = arg min
X ≥0 F(K [d+1], X ),
(6)
where the index d denotes the iteration index of the corresponding matrices.
This yields simpler, often convex restricted problems with respect to either K or
X . Considering for example the minimization of the NMF functional with Frobe-
nius norm and without any penalty term, yields a high dimensional linear system
K ⊺Y = K ⊺KX , which, however, would need to be solved iteratively.
Instead, so called surrogate methods for computing NMF decompositions have
been proposed recently and are introduced in the next section. They also con-
sider alternating minimization steps for K and X , but they replace the restricted
minimization problems in (5) and (6) by simpler minimization tasks, which are
obtained by locally replacing F by surrogate functionals for K and X separately.
3 Surrogate Functionals
In this section, we discuss general surrogate approaches for minimizing general
non-convex functionals, which are then exempliﬁed for speciﬁc NMF functionals
in later sections.
Let us consider a general functional F : Ω→R where Ω⊂RN and the minimiza-
tion problem
min
x∈ΩF(x).


## Page 6


6
Pascal Fernsel, Peter Maass
We will later add suitable conditions guaranteeing the existence of minimizers or
at least the existence of stationary points. Surrogate concepts replace this task
by solving a sequence of comparatively simpler and convex surrogate functionals,
which can be minimized eﬃciently. These methods are also commonly referred
to as surrogate minimization (or maximization) algorithms (SM) or also as MM
algorithms, where the ﬁrst M stands for majorize and the second M for minimize
(see also [18,23,36]). Such approaches have been demonstrated to be very useful
in many ﬁelds of inverse problems, in particular for hyperspectral imaging [11],
medical imaging applications such as transmisson tomography [13,14] as well as
MALDI imaging and tumor typing applications [26].
Replacing a non-convex functional by a series of convex problems is the main moti-
vation for such surrogate approaches. However, if constructed appropriately, they
can also be used to replace non-diﬀerentiable functionals by a series of diﬀeren-
tiable problems and they can be tailored such that gradient-descent methods for
minimization yield multiplicative update rules which automatically incorporate
non-negativity constraints without further projections.
From this point on it is important to note that possible zero denominators during
the derivation of the NMF algorithms as well as in the multiplicative update rules
themselves will not be discussed explicitly throughout this work. Usually, this is-
sue is handled in practice by adding a small positive constant in the denominator
during the iteration scheme. In fact, the instability of NMF algorithms due to the
convergence of some entries in the matrices to zero is not suﬃciently discussed
in the literature and still needs proper solution techniques. We will not focus on
this problem and turn now to the basic deﬁnition and properties of surrogate
functionals.
3.1 Deﬁnitions and Basic Properties
As in [25], we use the following deﬁnition of a surrogate functional.
Deﬁnition 5 (Surrogate Functional) Let Ω⊆RN denote an open set and
F : Ω→R a functional deﬁned on Ω. Then QF : Ω×Ω→R is called a surrogate
functional or a surrogate for F, if it satisﬁes the following conditions:
(i) QF (x, a) ≥F(x) for all x, a ∈Ω
(ii) QF (x, x) = F(x) for all x ∈Ω
This is the most basic deﬁnition, which does not require any convexity or diﬀer-
entiability of the functional. However, it already allows to prove that the iteration
x [d+1] := arg min
x∈ΩQF (x, x [d])
(7)
yields a sequence which monotonically decreases F.
Lemma 1 (Monotonic Decrease by Surrogate Functionals) Let Ω⊆RN
denote an open set, F : Ω→R a given function and QF a surrogate functional
for F. Assume that arg minx∈ΩQF (x, a) is well deﬁned for all a ∈Ω. Deﬁne the
iterated updates by
x [d+1] := arg min
x∈ΩQF (x, x [d])
(8)


## Page 7


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
7
Fig. 1: Visualization of the surrogate principle for non-convex F with convex
surrogate functional QF according to Lemma 1
with x [0] = arg minx∈ΩQF (x, a) for an arbitrary a ∈Ω. Then, F(x [d]) is a
monotonoically decreasing sequence, i.e.
F(x [d+1]) ≤F(x [d]).
(9)
Proof The monotone decrease (9) follows directly from the deﬁning properties of
surrogate functionals, see Deﬁnition 5: We obtain
F(x [d+1]) ≤QF (x [d+1], x [d])
(⋆)
≤QF (x [d], x [d]) = F(x [d]),
where (⋆) follows from the deﬁnition of x [d+1] in (8).
⊓⊔
Remark 1 (Addition of Surrogate Functionals) Let Ω⊆Rn be an open set, F, G :
Ω→R pointwise deﬁned functionals and QF , QG corresponding surrogates. Then
QF + QG is a surrogate functional for F + G.
For each functional F there typically exist a large variety of surrogate functionals
and we can aim at optimizing the structure of surrogate functionals. The following
additional property is the key to simple and eﬃcient minimization schemes for
surrogate functionals.
Deﬁnition 6 (Separability of a Surrogate Functional) Let Ω⊆RN denote
an open set, F : Ω→R a functional and QF a surrogate for F. The surrogate QF
is called separable, if there exist functions gi : R × Ω→R, such that
QF (x, a) =
N
X
i=1
gi(xi, a)
∀x, a ∈Ω.
(10)


## Page 8


8
Pascal Fernsel, Peter Maass
Lemma 1 above only ensures the monotonic decrease of the cost functional, which
is not suﬃcient to guarantee convergence of the sequence {x [d]} to a minimizer
of F or at least to a stationary point of F. The convergence theory for surrogate
functionals is far from being complete (see also the works [23] and [36]).
Despite this lack of theoretical foundation, surrogate based minimization yields
strictly decreasing sequences for a large variety of applications. In particular, sur-
rogate based methods can be constructed such that ﬁrst order optimality condi-
tions lead to multiplicative update rules, which - in view of applications to NMF
constructions - is a very desirable property.
We now turn to discussing three diﬀerent construction principles for surrogate
functionals.
3.2 Jensen’s Inequality
The starting point is the well known Jensen’s inequality for convex functions, see
[10].
Lemma 2 (Jensen’s Inequality) Let Ω⊆RN denote a convex set, F : Ω→R
a convex function and λi ∈[0, 1] non-negative numbers for i ∈{1, . . . , k} with
Pk
i=1 λi = 1. Then for all x i ∈Ω, it holds that
F
 k
X
i=1
λix i
!
≤
k
X
i=1
λiF(x i).
(11)
In this subsection we consider functionals F which are derived from continuously
diﬀerentiable and convex functions f : R>0 →R via
F : Ω→R
v 7→f(c⊺v) .
(12)
for Ω⊆RN
≥0 and some auxiliary variable c ∈Ω. This also implies, that F is
convex, since
F(v) ≥F(˜v) + ∇F(˜v)⊺(v −˜v)
⇔f(c⊺v) ≥f(c⊺˜v) + f ′(c⊺˜v)(c⊺v −c⊺˜v).
We now choose λi ∈[0, 1] with PN
i=1 λi = 1 and α ∈RN and deﬁne
λi := cibi
c⊺b
(13)
αi := civi
λi

= vic⊺b
bi

(14)
for some b ∈Ω. This implies
F(v) = f(c⊺v) = f
 N
X
i=1
λiαi
!
≤
N
X
i=1
cibi
c⊺b f
c⊺b
bi vi

=: QF (v, b).
(15)


## Page 9


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
9
The functional QF : Ω× Ω→R deﬁnes a surrogate for F, which can be seen by
the inequality above and by observing
QF (v, v) =
N
X
i=1
civi
c⊺v f(c⊺v) = f(c⊺v) = F(v).
3.3 Low Quadratic Bound Principle
This concept is based on a Taylor expansion of F in combination with a majoriza-
tion of the quadratic term. This so called low quadratic bound principle (LQBP)
has been introduced in [5] and was used in particularly for the computation of
maximum-likelihood estimators. These methods do not require that F itself is
convex and its construction is based on the following lemma.
Lemma 3 (Low Quadratic Bound Principle) Let Ω⊆RN denote an open
and convex set and f : Ω→R a twice diﬀerentiable functional. Assume that a
matrix Λ(x) ∈RN×N exists, such that Λ(x) −∇2f(x) is positive semi-deﬁnite
for all x ∈Ω. We then obtain a quadratic majorization
f(x) ≤f(a) + ∇f(a)⊺(x −a) + 1
2(x −a)⊺Λ(a)(x −a)
∀x, a ∈Ω
(16)
=: Qf(x, a),
and Qf is a surrogate functional for f.
Proof The proof of this classical result is based on the second-order Taylor poly-
nomial of f and shall be left to the reader.
⊓⊔
The related update rule for surrogate minimization can be stated explicitly under
natural assumptions on the matrix Λ.
Corollary 1 Assume that the assumptions of Lemma 3 hold. In addition, assume
that Λ is a positive deﬁnite and symmetric matrix. Then, the corresponding sur-
rogate Qf is strictly convex in its ﬁrst variable and we have from (8)
x [d+1] = arg min
x∈ΩQf(x, x [d])
= x [d] −Λ−1(x [d])∇f(x [d]).
(17)
Proof For an arbitrary α ∈{1, . . . , N}, we have that
∂Qf
∂xα (x, a) =
∂
∂xα


N
X
i=1
∂f
∂xi (a)(xi −ai) + 1
2
N
X
i=1
N
X
j=1
Λ(a)ij · (xi −ai)(xj −aj)


= ∂f
xα (a) + 1
2
N
X
i=1
i̸=α
Λ(a)αi(xi −ai) + 1
2
N
X
i=1
i̸=α
Λ(a)iα(xi −ai) + Λ(a)αα(xα −aα)
(⋆)
= ∂f
xα (a) + Λ(a)α,•(x −a),


## Page 10


10
Pascal Fernsel, Peter Maass
where (⋆) utilizes the symmetry of Λ. Hence, it holds that ∇xQf(x, a) = ∇f(a)+
Λ(a)(x −a). The Hessian matrix of Qf then satisﬁes
∇2
xQf(x, a) = Λ(a).
This implies the positive deﬁniteness of the functional, hence, it has a uniqie
minimizer, which is given by
∇xQf(x ∗
a, a) = 0 = ∇f(a) + Λ(a)(x ∗
a −a)
⇔x ∗
a = a −Λ−1(a)∇f(a).
This is the update rule above.
⊓⊔
The computation of the inverse of Λ is particularly simple if Λ is a diagonal ma-
trix. Furthermore, the diagonal structure ensures the separability of the surrogate
functional mentioned in Deﬁnition 6. Therefore, we consider matrices of the form
Λ(a)ii := (∇2f(a) a)i + κi
ai
,
(18)
where κi ≥0 has to be chosen individually depending on the considered cost
function. We will see that an appropriate choice of κi will lead ﬁnally to the
desired multiplicative update rules of the NMF algorithm.
The matrix Λ(a) in (18) fulﬁlls the conditions in Corollary 1 as it can be seen by
the following lemma. Therefore, if Λ is constructed as in (18), the update rule in
(17) can be applied immediately.
Lemma 4 Let M ∈RN×N
≥0
denote a symmetric matrix. With a ∈RN
>0 and κi ≥
0, we deﬁne the diagonal matrix Λ, such that
Λii := (Ma)i + κi
ai
(19)
for i = 1, . . . , N. Then Λ and Λ −M are positive semi-deﬁnite.
Proof Let ζ ∈RN denote an arbitrary vector and let δ denote the Kronecker
symbol. Then
ζ⊺(Λ −M )ζ =
N
X
i,j=1
ζiδij (Ma)i + κi
ai
ζj −
N
X
i,j=1
ζiMijζj
=
N
X
i=1
ζ2
i
(Ma)i
ai
+ ζ2
i
κi
ai −
N
X
i,j=1
ζiMijζj
≥
N
X
i,j=1
ζ2
i
aj
ai Mij −
N
X
i,j=1
ζiMijζj
=
N
X
i=1
ζ2
i Mij +
N
X
i,j=1
i<j

ζ2
i
aj
ai + ζ2
j
ai
aj

Mij −
N
X
i,j=1
ζiMijζj


## Page 11


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
11
=
N
X
i,j=1
1
2ζ2
i
aj
ai Mij + 1
2ζ2
j
ai
aj Mij −ζiMijζj

= 1
2
N
X
i,j=1
ζ2
i
aj
ai Mij + ζ2
j
ai
aj Mij −2
raj
ai
r ai
aj ζiMijζj
= 1
2
N
X
i,j=1
raj
ai ζi −
r ai
aj ζj
2
Mij ≥0.
The positive semi-deﬁniteness of Λ follows from its diagonal structure.
⊓⊔
3.4 Further Construction Principles
So far we have discussed two major construction principles based on either Jensen’s
inequality or on upper bounds for the quadratic term in Taylor expansions. [23]
lists further construction principles, which however will not be used for NMF
constructions in the subsequent sections of this paper. For completeness we shortly
list their main properties.
A relaxation of the approach based on Jensen’s inequality is achieved by choosing
αi ≥0, i ∈{1, . . . , N} such that PN
i=1 αi = 1 and αi > 0 if ci ̸= 0, which yields
F(v) = f(c⊺v) ≤
N
X
i=1
αif
 ci
αi (vi −bi) + c⊺b

=: QF (v, b).
A typical choice is
αi :=
|ci|p
Pn
j=1 |cj|p
which leads to surrogate functionals for p ≥0. This type of surrogate was origi-
nally introduced in the context of medical imaging, see [12], for positron emission
tomography.
Another approach is based on combining arithmetic with geometic means and can
be used for constructing surrogates for posynomial functions. For α, v, a ∈RN
>0,
we obtain
F(v) =
N
Y
i=1
vαi
i
≤
 N
Y
i=1
aαi
i
! N
X
i=1
αi
PN
k=1 αi
vi
ai
PN
k=1 αi
=: QF (v, a)
4 Surrogates for NMF Functionals
In this section we apply the general construction principles of Section 3 to the
NMF problem as stated in (3). The resulting functional F(K, X ) depends on
both factors of the matrix decomposition and minimization is attempted by alter-
nating minimization with respect to K and X as described in (5) and (6).
However, we replace the functional F in each iteration by suitable surrogate func-
tionals, which allow an explicit minimization. Hence, we avoid the minimization of
F itself, which even for the most simple quadaratic formulation requires to solve


## Page 12


12
Pascal Fernsel, Peter Maass
a high dimensional linear system.
We start by considering the discrepancy terms for β = 2 (Frobenius norm) and
β = 1 (Kullback-Leibler divergence) and determine surrogate functionals with re-
spect to X and K. We then add several penalty terms and develop surrogate
functionals accordingly. With regard to the construction of surrogates for the case
of β = 0, which leads to the so-called Itakura-Saito divergence, we refer to the
works [15,16,32].
4.1 Frobenius Discrepancy and Low Quadratic Bound Principle
We start by constructing a surrogate for the minimization with respect to X for
the Frobenius discrepancy
F(X ) := 1
2∥Y −KX ∥2
F .
(20)
Let Y •,j, resp. X •,j, denote the column vectors of Y , resp. X . The separability
of F yields
F(X ) = 1
2
m
X
j=1
∥Y •,j −KX •,j∥2 =:
m
X
j=1
fY •,j(X •,j),
(21)
Hence, the minimization separates for the diﬀerent fY•,j terms. The Hessian of
these terms is given by
∇2fY•,j (a) = K ⊺K
and the LQBP construction principle of the previous section with κk = 0 yields
ΛfY•,j (a)kk = (K⊺Ka)k
ak
,
leading to the surrogate functionals
QfY•,j (x, a) = fY•,j (a) + ∇fY•,j (a)⊺(x −a) + 1
2(x −a)⊺ΛfY•,j (a)(x −a). (22)
An appropriate choice of κk ensures the multiplicativity of the ﬁnal NMF algo-
rithm. In the case of the Frobenius discrepancy term, we will see that suitable κk
can be chosen dependent on ℓ1 regularization terms in the cost function, which
are not included up to now (see Subsection 4.4 and Appendix A.1 for more details
on this issue). Due to the absent ℓ1 terms, we set κk = 0 to get the desired multi-
plicative update rules. Summing up the contributions of the columns of X yields
the ﬁnal surrogate
QF : Rp×m × Rp×m →R,
(X , A) 7→
m
X
j=1
QfY•,j (X •,j, A•,j)
The equivalent construction for K can be obtained by regarding the rows of K
separately, which for
gy : Rp
≥0 →R,
k 7→1
2∥y −kX ∥2


## Page 13


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
13
yields ∇2gy(a) = XX ⊺. Putting
Λgy (a)kk = (aXX⊺)k
ak
leads to the surrogate
Qgy (k, a) = gy(a) + (k −a)∇gy(a) + 1
2(k −a)Λgy (a)(k −a)⊺.
We summarize this surrogate construction in the following theorem.
Theorem 1 (Surrogate Functional for the Frobenius Norm with LQBP)
We consider the cost functionals F(X ) := 1/2∥Y −KX ∥2
F and G(K) := 1/2∥Y −
KX ∥2
F . Then
QF,1(X , A) =
m
X
j=1
QfY •,j (X •,j, A•,j),
(23)
QG,1(K, A) =
n
X
i=1
QgY i,• (K i,•, Ai,•)
(24)
deﬁne separable and convex surrogate functionals.
4.2 Frobenius Discrepancy and Jensen’s Inequality
Again we focus on deriving a surrogate functional for X , the construction for K
will be very similar. Expanding the Frobenius discrepancy yields
F(X ) := 1
2∥Y −KX ∥2
F = 1
2
n
X
i=1
m
X
j=1
(Yij −(KX)ij)2.
Putting v := X •,j ∈Rp
≥0 and c := K i,•⊺∈Rp
≥0 allows us to deﬁne
f : R≥0 →R
with
f(t) := (Yij −t)2,
(25)
such that
f(c⊺v) = (Yij −(KX)ij)2.
(26)
Hence we have separated the Forbenius discrepancy suitably for applying Jensen’s
inequality. Following the construction principle in Subsection 3.2, we deﬁne
λk = KikAkj
(KA)ij ,
(27)
αk = KikXkj
λk
.
(28)
with the auxiliary variable A ∈Rp×m
≥0
and b := A•,j ∈Rp
≥0, which yields the
inequality
(Yij −(KX)ij)2 ≤
p
X
k=1
KikAkj
(KA)ij

Yij −Xkj
Akj
(KA)ij
2
.


## Page 14


14
Pascal Fernsel, Peter Maass
Inserting this into the decomposition of the Frobenius discrepancy yields the sur-
rogate QF,2(X , A) by
F(X ) ≤1
2
n
X
i=1
m
X
j=1
1
(KA)ij
p
X
k=1
KikAkj

Yij −Xkj
Akj
(KA)ij
2
=: QF,2(X , A),
The construction of a surrogate for K proceeds in the same way. We summarize
the results in the following theorem.
Theorem 2 (Surrogate Functional for the Frobenius Norm with Jensen’s
Inequality) We consider the cost functionals F(X ) :=
1/2∥Y −KX ∥2
F and
G(K) := 1/2∥Y −KX ∥2
F . Then
QF,2(X , A) := 1
2
n
X
i=1
m
X
j=1
1
(KA)ij
p
X
k=1
KikAkj

Yij −Xkj
Akj
(KA)ij
2
(29)
QG,2(K, A) := 1
2
n
X
i=1
m
X
j=1
1
(AX)ij
p
X
k=1
AikXkj

Yij −Kik
Aik
(AX)ij
2
(30)
deﬁne separable and convex surrogate functionals.
These surrogates are equal to the ones proposed in [11]. We will later use ﬁrst
order necessary conditions of the surrogate functionals for obtaining algorithms
for minimization. We already note
∂QF,1
∂Xαβ
= ∂QF,2
∂Xαβ
and
∂QG,1
∂Kαβ
= ∂QG,2
∂Kαβ
,
i.e. despite the rather diﬀerent derivations, the update rules for the surrogates
obtained by LQBP and Jensen’s inequality will be identical.
4.3 Surrogates for Kullback-Leibler Divergence
The case β = 1 in Deﬁnition 3 yields the so-called Kullback-Leibler divergence
(KLD). For matrices M , N ∈Rn×m
>0
, it is deﬁned as
KL(M , N ) := D1(M , N ) =
n
X
i=1
m
X
j=1
Mij log
Mij
Nij

−Mij + Nij
(31)
and has been investigated intensively in connection with non-negative matrix fac-
torization methods [11,16,24,25]. In our context, we deﬁne the cost functional for
the NMF construction by
F(X , K) := KL(Y , KX ).
We will focus in this subsection on Jensen’s inequality for constructing surrogates
for the KLD since they will lead to the known classical NMF algorithms (see also
[11,24,25]). However, it is also possible to use the LQBP principle to construct a
suitable surrogate functional for the KLD which leads to diﬀerent, multiplicative
update rules (see Appendix B).


## Page 15


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
15
We start by deriving a surrogate for the minimization with respect to X , i.e. we
consider
F(X ) := KL(Y , KX ) =
n
X
i=1
m
X
j=1
Yij log(Yij) −Yij log((KX)ij) −Yij + (KX)ij.
Using the same λk and αk as in the section above and applying it to the convex
function f(t) := −ln(t), we obtain
−ln((KX)ij) ≤−
p
X
k=1
KikAkj
(KA)ij ln
Xkj
Akj
(KA)ij

.
Multiplication with Yij ≥0 and the addition of appropriate terms yields
F(X ) ≤
n
X
i=1
m
X
j=1
Yij ln(Yij) −Yij + (KX)ij −
Yij
(KA)ij
p
X
k=1
KikAkj ln
 Xkj
Akj
(KA)ij

=: QF,1(X , A).
The condition QF,1(X , X ) = F(X ) follows by simple algebraic manipulations,
such that QF,1 is a valid surrogate functional for F.
The approach by Jensen’s inequality is very ﬂexible and we obtain diﬀerent sur-
rogate functionals QF,2 and QF,3 by using i.e. f1(t) = Yij ln(Yij/t) −Yij + t or
f2(t) = −Yij ln(t) + t instead of f. Inserting the same λk and αk as before in
Equation (15), we obtain immediately the surrogates
QF,2(X , A) =
n
X
i=1
m
X
j=1
1
(KA)ij
p
X
k=1
KikAkj



Yij ln




Yij
Xkj
Akj
(KA)ij



−Yij + Xkj
Akj
(KA)ij



,
QF,3(X , A) =
n
X
i=1
m
X
j=1
"
Yij ln(Yij) −Yij
+
1
(KA)ij
p
X
k=1
KikAkj

−Yij ln
 Xkj
Akj
(KA)ij

+ Xkj
Akj
(KA)ij
#
.
It easy to check, that the partial derivatives for all three variants are the same,
hence, the update rules obtained in the next section based on ﬁrst order optimality
conditions will be identical. Applying the same approach for obtaining a surrogate
for K yields the following theorem.
Theorem 3 (Surrogate Functional for the Kullback-Leibler Divergence
with Jensens Inequality) We consider the cost functionals F(X ) := KL(Y , KX )
and G(K) := KL(Y , KX ). Then
QF (X , A) :=
n
X
i=1
m
X
j=1
Yij ln(Yij) −Yij + (KX)ij −
Yij
(KA)ij
p
X
k=1
KikAkj ln
 Xkj
Akj
(KA)ij

QG(K, A) :=
n
X
i=1
m
X
j=1
Yij ln(Yij) −Yij + (KX)ij −
Yij
(AX)ij
p
X
k=1
AikXkj ln
 Kik
Aik
(AX)ij

deﬁne separable and convex surrogate functionals.


## Page 16


16
Pascal Fernsel, Peter Maass
4.4 Surrogates for ℓ1- and ℓ2-Norm Penalties
Computing an NMF is an ill-posed problem, see [11], hence one needs to add
stabilizing penalty terms for obtaining reliable matrix decompositions. The most
standard penalties are ℓ1- and ℓ2-terms for the matrix factors leading to
min
K,X ≥0 Dβ(Y , KX ) + λ∥X ∥1 + µ
2 ∥K∥2
F + ν
2 ∥X ∥2
F + ω∥K∥1
(32)
for β ∈{1, 2}.
The ℓ2-penalty prohibits exploding norms for each matrix factor and the ℓ1-term
promotes sparsity in the minimizing factors, see [21,28] for a general exposition.
Combinations of ℓ1- and ℓ2-norms are sometimes called elastic net regularization,
[20], due to there importance in medical imaging.
These penalty terms are convex and they separate, hence, they can be used as
surrogates themselves. For the case of Kullback-Leibler divergences this leads to
the following surrogate for minimization with respect to X :
QF (X , A) := QKL(X , A) + λ∥X ∥1 + ν
2 ∥X ∥2
F ,
where QKL is the surrogate for the Kullback-Leibler divergence of Theorem 3 for
X .
The Frobenius case cannot be treated in the same way. If we use the penalty terms
as surrogates themselves and obtain the standard minimization algorithm by ﬁrst
order optimality conditions, then this does not lead to a multiplicative algorithm,
which preserves the non-negativity of the iterates. It can be easily seen that the
ℓ1-penalty term causes this diﬃculty. For a more extended discussion on this, see
Appendix A.1.
Hence, we have to construct a diﬀerent surrogate. Similar to the discussion in
Subsection 4.1, we consider here fy : Rp
≥0 →R with
fy(x) := 1
2∥y −Kx∥2 + λ∥x∥1 + ν
2 ∥x∥2,
which yields the Hessian ∇2fy(a) = K ⊺K + νI . The choice of κk is done depen-
dent on the ℓ1 regularization term of the cost function fy as already described
in Subsection 4.1. It can be shown in the derivation of the NMF algorithm that
κk = λ for all k leads to multiplicative update rules. A more general cost function
is considered in Appendix A.1, where the concrete eﬀect of κk is described in more
detail.
This yields the following diagonal matrix Λfy (a):
Λfy (a)kk = ((K⊺K + νIp×p)a)k + λ
ak
.
The surrogate for minimization with respect to X is then
Qfy (x, a) = fy(a) + ∇fy(a)⊺(x −a) + 1
2(x −a)⊺Λfy (a)(x −a).
Similar, for minimization with respect to K we obtain the surrogate by using the
diagonal matrix
Λgy (a)kk := (a(XX⊺+ µIp×p))k + ω
ak
.


## Page 17


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
17
4.5 Surrogates for Orthogonality Constraints
The observation that a non-negative matrix with pairwise orthogonal rows has at
most one non-zero entry per column is the motivation for introducing orthogonal-
ity constraints for K or X . This will lead to strictly uncorrelated feature vectors,
which is desirable in several applications e.g. for obtaining discriminating biomark-
ers from mass spectra, see Section 6 on MALDI Imaging.
We could add the orthogonality constraint K ⊺K = I as an additional penalty
term σK ∥K ⊺K −I ∥2. However, this would introduce fourth order terms. Hence
we introduce additional variables V and W and split the orthogonality condition
into two second order terms leading to
min
K,X ,V ,W ≥0
n
Dβ(Y , KX ) + σK,1
2
∥I −V ⊺K∥2
F + σK,2
2
∥V −K∥2
F
+ σX ,1
2
∥I −X W ⊺∥2
F + σX ,2
2
∥W −X ∥2
F
o
.
(33)
Surrogates for the terms ∥I −V ⊺K∥2
F and ∥I −X W ⊺∥2
F can be calculated via
Jensen’s inequality (see Subsection 4.2). The other penalties can be used as sur-
rogates themselves and therefore, we obtain
Theorem 4 (Surrogate Functionals for Orthogonality Constraints) We
consider the cost functionals
F(X ) := σX ,1
2
∥I −X W ⊺∥2
F + σX ,2
2
∥W −X ∥2
F =: G(W ),
H(K) := σK,1
2
∥I −V ⊺K∥2
F + σK,2
2
∥V −K∥2
F =: J(V )
with σX ,1, σX ,2, σK,1, σK,2 ≥0. Then
QF (X , A) := σX ,1
2
p
X
k=1
p
X
ℓ=1
1
(AW ⊺)kℓ
m
X
j=1
AkjWℓj

δkℓ−Xkj
Akj
(AW ⊺)kℓ
2
+ σX ,2
2
∥W −X ∥2
F
QG(W , A) := σX ,1
2
p
X
k=1
p
X
ℓ=1
1
(XA⊺)kℓ
m
X
j=1
XkjAℓj

δkℓ−Wℓj
Aℓj
(XA⊺)kℓ
2
+ σX ,2
2
∥W −X ∥2
F
QH(K, A) := σK,1
2
p
X
k=1
p
X
ℓ=1
1
(V ⊺A)kℓ
n
X
i=1
VikAiℓ

δkℓ−Kiℓ
Aiℓ
(V ⊺A)kℓ
2
+ σK,2
2
∥V −K∥2
F
QJ(V , A) := σK,1
2
p
X
k=1
p
X
ℓ=1
1
(A⊺K)kℓ
n
X
i=1
AikKiℓ

δkℓ−Vik
Aik
(A⊺K)kℓ
2
+ σK,2
2
∥V −K∥2
F
deﬁne separable and convex surrogate functionals.
4.6 Surrogates for Total Variation Penalties
Total variation (TV) penalty terms are the second important class of regularization
terms besides ℓp-penalty terms. TV-penalties aim at smooth or even piecewise
constant minimizers, hence they are deﬁned in terms of ﬁrst order or higher order
derivatives [7].
Originally, they were introduced for denoising applications in image processing


## Page 18


18
Pascal Fernsel, Peter Maass
[31] but have since been applied to inpainting, deconvolution and other inverse
problems, see e.g. [8]. The precise mathematical formulation of the total variation
in the continuous case is described in the following deﬁnition.
Deﬁnition 7 (Total Variation (Continuous)) Let Ω⊂RN be open and
bounded. The total variation of a function u ∈L1
loc(Ω) is deﬁned as
TV(u) := sup

−
Z
Ω
u div φ dx : φ ∈C∞
c (Ω, RN) mit ∥φ(x)∥≤1 ∀x ∈Ω

.
There exist several analytic relaxations of TV based on ℓ1-norms of the gradient,
which are more tractable for analytical investigations. For numerical implementa-
tions one rather uses the L1-norm of the gradient ∥∇f∥L1 as a more computation-
ally tractable substitute. For discretization the gradient is typically replaced by a
ﬁnite diﬀerence approximation [9].
For applying TV-norms to data, we assume that the row index in the data ma-
trix Y refers to spatial locations and the column index to so-called channels. In
this case, we consider the most frequently used isotropic TV for applying it to
measured, discretized hyperspectral data.
Deﬁnition 8 (Total Variation (Discrete)) For ﬁxed εTV > 0, the total vari-
ation of a matrix K ∈Rn×p
≥0
is deﬁned as
TV(K) :=
p
X
k=1
ψk
n
X
i=1
s
ε2
TV +
X
ℓ∈Ni
(Kik −Kℓk)2,
(34)
where ψk ∈R≥0 is a weighting of the k-th data channel and Ni ⊆{1, . . . , n} \ {i}
denotes the index set referring to spatially neighboring pixels.
We will use the following short hand notation
|∇ikK| :=
s
ε2
TV +
X
ℓ∈Ni
(Kik −Kℓk)2,
(35)
which can be seen as a ﬁnite diﬀerence approximation of the gradient magnitude
of the image K •,k at pixel Kik for some neighbourhood pixels deﬁned by Ni. A
typical choice for neighbourhood pixels in two dimensions for the pixel (0, 0) is
N(0,0) := {(1, 0), (0, 1)} to get an estimate of the gradient components along both
axes. Finally, by introducing the positive constant εTV > 0, we get a diﬀerentiable
approximation of the total variation penalty.
In Section 6, we will discuss the application of NMF methods to hyperspectral
MALDI imaging datasets, which has a natural ’spatial structure’ in its columns.
In this section we stay with a generic choice of Ni as well as of the ψk and we
construct a surrogate following the approach of the groundbreaking works of [13]
and [29].
For t ≥0 and s > 0 we use the inequality (linear majorization)
√
t ≤√s + t −s
2√s
(36)
and apply it in order to compare ∇ikK with values obtained by an arbitrary
non-negative matrix A:


## Page 19


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
19
|∇ikK| ≤|∇ikA| + |∇ikK|2 −|∇ikA|2
2|∇ikA|
≤|∇ikK|2 + |∇ikA|2
2|∇ikA|
=
2ε2
TV + P
ℓ∈Ni

(Kik −Kℓk)2 + (Aik −Aℓk)2
2|∇ikA|
.
Summation with respect to i, multiplication with ψk and summation with respect
to k leads to
TV(K) ≤
p
X
k=1
ψk
n
X
i=1
2ε2
TV + P
ℓ∈Ni

(Kik −Kℓk)2 + (Aik −Aℓk)2
2|∇ikA|
=: QOli
TV(K, A).
This yields a candidate for a surrogate QOli
TV for the TV-penalty term, which is
the same as the one used in [29]. However, it is not separable, hence we aim at a
second, separable approximation. For arbitrary a, b, c, d ∈R we have
1
2

(a −b)2 + (c −d)2
≤(a −b)(c −d) + (b −d)2 + (a −c)2.
(37)
This leads to
QOli
TV(K, A) =
p
X
k=1
ψk
n
X
i=1
ε2
TV + P
ℓ∈Ni
1/2

(Kik −Kℓk)2 + (Aik −Aℓk)2
|∇ikA|
≤
p
X
k=1
ψk
n
X
i=1
ε2
TV+P
ℓ∈Ni

(Kik−Kℓk)(Aik−Aℓk)+(Kℓk−Aℓk)2+(Kik−Aik)2
|∇ikA|
=: QTV(K, A).
Therefore, we have the following
Theorem 5 (Surrogate Functional for TV Penalty Term) We consider the
cost functional F(K) := TV(K) with the total variation deﬁned in (34). Then
QTV(K,A):=
p
X
k=1
ψk
n
X
i=1
ε2
TV+P
ℓ∈Ni

(Kik−Kℓk)(Aik−Aℓk)+(Kℓk−Aℓk)2+(Kik−Aik)2
|∇ikA|
deﬁnes a separable and convex surrogate functional.
The separability of the surrogate is not obvious. The proof (see Appendix C) deliv-
ers the following notation, which we also need for an description of the algorithms
in the next section. First of all we need the deﬁnition of the so-called adjoint
neighborhood pixels ¯
Ni given by
ℓ∈¯
Ni ⇔i ∈Nℓ.
(38)
One then introduces matrices P(A) ∈Rn×p
≥0
and Z(A) ∈Rn×p
≥0
via
P(A)ik :=
1
|∇ikA|
X
ℓ∈Ni
1 +
X
ℓ∈¯
Ni
1
|∇ℓkA|,
(39)


## Page 20


20
Pascal Fernsel, Peter Maass
Z(A)ik :=
1
P(A)ik


1
|∇ikA|
X
ℓ∈Ni
Aik + Aℓk
2
+
X
ℓ∈¯
Ni
Aik + Aℓk
2|∇ℓkA|

.
(40)
Using these notations, it can be shown that the surrogate can be written as
QTV(K, A) =
p
X
k=1
ψk
n
X
i=1
h
P(A)ik(Kik −Z(A)ik)2i
+ C(A),
(41)
such that we obtain the desired separability. Here, C(A) denotes some function
depending on A. The description of QTV with the help of P(A)ik and Z(A)ik will
also allow us to compute the partial derivatives in a way more comfortable way
(see also Appendix A.2).
4.7 Surrogates for Supervised NMF
As a motivation for this section, we consider classiﬁcation tasks. We view the data
matrix Y as a collection of n data vectors, which are stored in the rows of Y .
Moreover, we do have an expert annotation ui for i = 1, . . . , n, which assigns a
label to each data vector. For a classiﬁcation problem with two classes we have
ui ∈{0, 1}.
As already stated, the rows of the matrix X of an NMF decomposition can be
regarded as a basis for approximating the rows of Y . Hence, one assumes that the
correlations between a row Y i,• of Y and all row vectors of X , i.e. computing
Y i,•X ⊺, contains the relevant information of Y i,•. The vector of correlations
yields a so-called feature vector of length p. A classical linear regression model,
which uses these feature vectors, then asks to compute weights βk for k = 1, . . . , p,
such that Y i,•X ⊺β ≈ui (for more details on linear discriminant analysis methods,
we refer to Chapter 4 in [4]).
In matrix notation and using least squares, this is equivalent to computing β as a
minimizer of
∥u −Y X ⊺β∥2.
We now use X and β to deﬁne
x ∗:= X ⊺β.
In tumor typing classiﬁcations, where the data matrix Y is obtained by MALDI
measurements, the vector x ∗can be interpreted as a characteristic mass spectrum
of some speciﬁc tumor type and can be directly used for classiﬁcation tasks in the
arising ﬁeld of digital pathology (see also Section 6 and [26]).
The classiﬁcation of a new data vector y is then simply obtained by computing the
scalar product w = x ∗⊺y and assigning either the class label 0 or 1 by comparing
w with a pre-assigned threshold s. This threshold is typically obtained in the
training phase of the classiﬁcation procedure by computing YX ⊺β for some given
training data Y and choosing s, such that a performance measure of the classiﬁer
is optimized.
The approach we have described is based on ﬁrst computing an NMF, i.e. K and


## Page 21


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
21
X , and then computing the weights β of the classiﬁer. Hence, the computation of
the NMF is done independently of the class labels u, which is also referred to as
an unsupervised NMF approach. We might expect, that computing the NMF by
minimizing a functional which includes the class labels, i.e.
F(K, X , β) := Dβ(Y , KX ) + ρ
2∥u −Y X ⊺β∥2,
will lead to an improved classiﬁer. In the application ﬁeld of MALDI imaging, this
supervised approach yields an extraction of features from the given training data,
which allow a better distinction between spectra obtained from diﬀerent tissue
types such as tumorous and non-tumorous regions (see also [26]).
Surrogates for the ﬁrst term have been determined in the previous section for the
case of the Frobenius norm and the Kullback-Leibler divergence. Hence, we need
to determine surrogates of the new penalty term for minimization with respect to
X and β:
F(X ) := 1
2∥u −YX ⊺β∥2,
(42)
G(β) := 1
2∥u −YX ⊺β∥2.
(43)
Surrogates can be obtained by extending the Jensen principle to the matrix valued
case. Here, we consider a convex subset Ω⊂RN×M
>0
and deﬁne
˜F : Ω→R
V 7→f(c⊺V d)
(44)
with a convex and continuously diﬀerentiable function f and auxiliary variables
c ∈RN
>0 and d ∈RM
>0. We now use the following generalized Jensen’s inequality
f


N
X
j=1
M
X
k=1
λjkαjk

≤
N
X
j=1
M
X
k=1
λjkf(αjk).
(45)
Setting
λjk = YijAkjβk
Y i,•A⊺β
(46)
αjk = YijXkjβk
λjk
.
(47)
for some i ∈{1, . . . , n} yields by inserting λjk and αjk into (45)
F(X ) ≤1
2
n
X
i=1
1
(Y A⊺β)i
m
X
j=1
p
X
k=1
YijAkjβk

ui −Xkj
Akj
(Y A⊺β)i
2
:= QF (X , A).
The computation of a surrogate for minimization with respect to β proceeds anal-
ogously. We summarize the results in the following theorem.


## Page 22


22
Pascal Fernsel, Peter Maass
Theorem 6 (Surrogate Functionals for Linear Regression) Let F(X ) :=
1/2∥u −YX ⊺β∥2 und G(β) := 1/2∥u −YX ⊺β∥2 denote a cost functional with
repect to X and β. Then
QF (X , A) := 1
2
n
X
i=1
1
(Y A⊺β)i
m
X
j=1
p
X
k=1
YijAkjβk

ui −Xkj
Akj
(Y A⊺β)i
2
(48)
QG(β, a) := 1
2
n
X
i=1
1
(Y X⊺a)i
p
X
k=1
(Y X⊺)ikak

ui −βk
ak
(Y X⊺a)i
2
(49)
deﬁne separable and convex surrogate functionals.
A big advantage of linear regression models are their simplicity and manageability.
However, they are by far not the optimal approach to approximate the binary
output data u with a continuous input. Logistic regression models oﬀer a way
more natural method for binary classiﬁcation tasks. Together with the supervised
NMF as a feature extraction method, this overall workﬂow leads in [26] to excellent
classiﬁcation results and outperformed classical approaches.
However, the proposed model is based on a gradient descent approach, such that
the non-negativity of the iterates can only be guaranteed by a projection step.
Appropriate surrogate functionals for this workﬂow are still ongoing research and
could lead to even better outcomes (see also [35,36]).
5 Surrogate Based NMF Algorithms
In the previous section we have deﬁned surrogate functionals for various NMF cost
functions. Besides the necessary surrogate properties we also expect that the min-
imization of these surrogates is straightforward and can be computed eﬃciently.
In our case we demand additionally, that the minimization schemes based on
solving the ﬁrst order optimality conditions leads to a separable algorithm and
that it only requires multiplicative updates, which automatically preserve the non-
negativity of its iterates. Let us start with denoting the most general functional
with Kullback-Leibler divergence, the Frobenius case follows similarly.
For constructing non-negative matrix factorizations, we incorporate ℓ2-, sparsity-,
orthogonality-, TV-constraints and also the penalty terms coming from the super-
vised NMF. Of course, in most applications one only uses a subset of these con-
straints for stabilization and for enhancing certain properties. These algorithms
can readily be obtained from the general case by putting the respective regulariza-
tion parameters to zero. The corresponding update rules are classical results and
can be found in numerous works [11,24,25].
Deﬁnition 9 (NMF Problem) For Y ∈Rn×m
≥0
, K, V ∈Rn×p
≥0 , X , W ∈
Rp×m
≥0
, β ∈Rp
≥0 and a set of regularization parameters λ, µ, ν, ω, τ, σK,1, σK,2, σX ,1,
σX ,2, ρ ≥0, we deﬁne the NMF minimization problem by
min
K,X ,V ,W ,β≥0

KL(Y , KX ) + λ∥X ∥1 + µ
2 ∥K∥2
F + ν
2 ∥X ∥2
F + ω∥K∥1 + τ
2 TV(K)
+ σK,1
2
∥I −V ⊺K∥2
F + σK,2
2
∥V −K∥2
F + σX ,1
2
∥I −X W ⊺∥2
F
+ σX ,2
2
∥W −X ∥2
F + ρ
2∥u −YX ⊺β∥2

.


## Page 23


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
23
The choice of the various regularization parameters occuring in Deﬁnition 9 is often
based on heuristic approaches. We will not focus on that issue in this work and
refer instead to [19] and the references therein, where two methods are investigated
for the general case of multi-parameter Tikhonov regularization.
The algorithms studied in this section will start with positive initializations for
K, X , V , W and β. These matrices are updated alternatingly, i.e. all matrices
except one matrix are kept ﬁxed and only the selected matrix is updated by solving
the respective ﬁrst order optimality condition.
We will focus in this section on the derivation of the update rules of K (see also
Appendix A.2). The iteration schemes for the other matrices follow analogously.
For that, we only have to consider those terms in the general functional which
depend on K, i.e. we aim at determining a minimizer for
F(K) := KL(Y , KX ) + µ
2 ∥K∥2
F + ω∥K∥1 + τ
2 TV(K) + σK,1
2
∥I −V ⊺K∥2
F + σK,2
2
∥V −K∥2
F .
Instead of minimizing this functional we exchange it with the previously con-
structed surrogate functionals, which leads to
QF (K, A) := QKL(K, A) + µ
2 ∥K∥2
F + ω∥K∥1 + τ
2 QTV(K, A) + QOrth(K, A)
with the surrogates QKL for the Kullback-Leibler divergence in Theorem 3, QTV
for the TV penalty term in Theorem 5 and QOrth for the orthogonality penalty
terms in Theorem 4.
The computation of the partial derivatives leads to a system of equations
∂QF
∂Kξζ
(K, A) = 0
(50)
for ξ ∈{1, . . . , n} and ζ ∈{1, . . . , p}. This leads to a system of quadratic equations
K2
ξζ

µ + τψζPξζ(A) + σK,1
Aξζ
(V V ⊺A)ξζ + σK,2

+Kξζ


m
X
j=1
Xζj + ω −τψζP(A)ξζZ(A)ξζ −(σK,1 + σK,1)Vξζ


=Aξζ
m
X
j=1
Yξj
(AX)ξj
Xζj.
Solving for Kξζ and denoting the Hadamard product by ◦as well as the matrix
division for each entry separately by a fraction line, yields the following update
rule for K. (Note that the notation for P(A) and Z(A) was introduced in the


## Page 24


24
Pascal Fernsel, Peter Maass
section on TV-regularization above.)
K [d+1] =






K [d]
µ1 n×p + τΨ ◦P(K [d]) + σK,1
VV ⊺K [d]
K [d]
+ σK,21 n×p



◦

Y
K [d]X
X ⊺

|
{z
}
=:Θ[d]
+ 1
4




1 n×mX ⊺+ ω1 n×p −τΨ ◦P(K [d]) ◦Z(K [d]) −(σK,1 + σK,2)V
µ1 n×p + τΨ ◦P(K [d]) + σK,1
VV ⊺K [d]
K [d]
+ σK,21 n×p




2 

1/2
−1
2




1 n×mX ⊺+ ω1 n×p −τΨ ◦P(K [d]) ◦Z(K [d]) −(σK,1 + σK,2)V
µ1 n×p + τΨ ◦P(K [d]) + σK,1
VV ⊺K [d]
K [d]
+ σK,21 n×p




|
{z
}
=:Φ[d]
In the above update rule, 1 n×p denotes an n × p matrix with ones in every entry
and Ψ ∈Rn×p
≥0
is deﬁned as
Ψ :=





ψ1 ψ2 · · · ψp
ψ1 ψ2 · · · ψp
...
...
...
ψ1 ψ2 · · · ψp




.
Details on the derivation can be found in Appendix A.2.
The partial derivatives with repect to X are computed similarly. Deﬁning
Λ[d] :=




X [d]
ν1 p×m + σX ,1
X [d]W ⊺W
X [d]
+ σX ,21 p×m + ρ ββ⊺X [d]Y ⊺Y
X [d]



◦

K ⊺
Y
KX [d]

Γ [d] :=
K ⊺1 n×m + λ1 p×m −(σX ,1 + σX ,2)W −ρβu⊺Y
ν1 p×m + σX ,1 X [d]W ⊺W
X [d]
+ σX ,21 p×m + ρββ⊺X [d]Y ⊺Y
X [d]
leads to the update
X [d+1] =
r
Λ[d] + 1
4Γ [d] ◦Γ [d] −1
2Γ [d].
The updates for V , W are straight forward and we obtain the following theorem.
Theorem 7 (Alternating Algorithm for NMF Problem in Deﬁnition 9)
The initializations K [0], V [0] ∈Rn×p
>0 , X [0], W [0] ∈Rp×m
>0
, β[0] ∈Rp
>0 and the
iterative updates
V [d+1] =
(σK,1 + σK,2)K [d]
σK,1 K [d]K [d]⊺V [d]
V [d]
+ σK,21 n×p
(51)


## Page 25


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
25
K [d+1] =
r
Θ[d] + 1
4Φ[d] ◦Φ[d] −1
2Φ[d]
(52)
W [d+1] =
(σX ,1 + σX ,2)X [d]
σX ,1 W [d]X [d]⊺X [d]
W [d]
+ σX ,21 p×m
(53)
X [d+1] =
r
Λ[d] + 1
4Γ [d] ◦Γ [d] −1
2Γ [d]
(54)
β[d+1] =
X [d+1]Y ⊺u
X [d+1]Y ⊺Y X [d+1]⊺β[d] ◦β[d]
(55)
lead to a monotonically decrease of the cost functional
F(K, X , V , W , β) := KL(Y , KX ) + λ∥X ∥1 + µ
2 ∥K∥2
F + ν
2 ∥X ∥2
F + ω∥K∥1
+ τ
2 TV(K) + σK,1
2
∥I −V ⊺K∥2
F + σK,2
2
∥V −K∥2
F
+ σX,1
2
∥I −X W ⊺∥2
F + σX,2
2
∥W −X ∥2
F + ρ
2∥u −YX ⊺β∥2.
It is easy to see that the classical, regularized NMF algorithms described in [11,
24,25] can be regained by putting the corresponding regularization parameters to
zero. In the case of ℓ1- and ℓ2-regularized NMF, this leads to the cost function
F(K, X ) = KL(Y , KX ) + λ∥X ∥1 + µ
2 ∥K∥2
F + ν
2 ∥X ∥2
F + ω∥K∥1.
The classical update rule for X is obtained by setting
˜Λ
[d] := X [d] ◦

K [d+1]⊺
Y
K [d+1]X [d]

,
˜Γ
[d] := K [d+1]⊺1 n×m + λ1 p×m,
which - in connection with the update rule for X of the previous theorem - leads
to
X [d+1] =
r
1
ν
˜Λ
[d] +
1
4ν2 ˜Γ
[d] ◦˜Γ
[d] −1
2ν
˜Γ
[d]
=
2˜Λ
[d]
˜Γ
[d] +
q
4ν ˜Λ
[d] + ˜Γ
[d] ◦˜Γ
[d] ,
(56)
which is the update rule described in [11].
By the same approach and with the surrogate functionals derived in Section 4, we
obtain the update rules for the Frobenius discrepancy term, i.e. we consider the
functional
F(K, X , V , W , β) := 1
2∥Y −KX ∥2
F + λ∥X ∥1 + µ
2 ∥K∥2
F + ν
2 ∥X ∥2
F + ω∥K∥1
+ τ
2 TV(K) + σK,1
2
∥I −V ⊺K∥2
F + σK,2
2
∥V −K∥2
F
+ σX,1
2
∥I −X W ⊺∥2
F + σX,2
2
∥W −X ∥2
F + ρ
2∥u −YX ⊺β∥2


## Page 26


26
Pascal Fernsel, Peter Maass
A monotone decrease of this functional is obtained by the following iteration in
combination with the update rules for V , W , β as in Theorem 7 (see also Appendix
A.1 for more details on the derivation of these algorithms.)
K [d+1] =
YX [d]⊺+ τΨ ◦P (K [d]) ◦Z(K [d]) + (σK,1 + σK,2)V [d+1]
τΨ ◦P (K [d]) + σK,21 n×p + K [d]X [d]X [d]⊺+µK [d] + ω1 n×p + σK,1V [d+1]V [d+1]⊺K [d]
K [d]
X [d+1] =
K [d+1]⊺Y + (σX ,1 + σX ,2)W [d+1] + ρβ[d]u⊺Y
σX ,21 p×m+ K [d+1]⊺K [d+1]X [d]+νX [d]+λ1 p×m+ρβ[d]β[d]⊺X [d]Y ⊺Y +σX ,1X [d]W [d+1]⊺W [d+1]
X [d]
.
6 MALDI Imaging
As a test case we analyse MALDI imaging data (matrix assisted laser desorp-
tion/ionization) of a rat brain. MALDI imaging is a comparatively novel modality,
which unravels the molecular landscape of tissue slices and allows a subsequent
proteomic or metabolic analysis [1,6,22]. Clustering this data reveals for example
diﬀerent metabolic regions of the tissue, which can be used for supporting patho-
logical diagnosis of tumors.
The data used in this paper was obtained by a MALDI imaging experiment, see
Figure 2 for a schematic experimental setup.
In our numerical experiments, we used a classical rat brain dataset which has been
used in several data processing papers before [2,3,22]. It constitutes a standard
test set for hyperspectral data analysis.
The tissue slice was scanned at 20185 positions. At each position a full mass spec-
trum with 2974 m/z (mass over charge) values was collected. I.e. instead of three
color channels, as it is usual in image processing, this data has 2974 channels,
each channel containing the spatial distribution of molecules having the same m/z
value.
The following numerical examples were obtained with the multiplicative algorithms
described in the previous section. We just illustrate the eﬀect of the diﬀerent
penalty terms for some selected functionals. One can either display the columns of
K as the pseudo channels of the NMF decomposition or the rows of X as pseudo
spectra characterizing the diﬀerent metabolic processes present in the tissue slice,
see the Figures 3-6.
Both ways of visualization do have their respective value. Looking at the pseudo
spectra in connection with orthogonality constraints leads to a clustering of the
spectra and to a subdivision of the tissue slice in regions with potentially diﬀer-
ent metabolic activities, see [22]. Considering instead the diﬀerent pseudo spectra,
which were constructed in order to have a bases which allows a low dimensional
approximaton of the data set, is the basis for subsequent proteomic analysis. E.g.
one may target pseudospectra where the related pseudo channels are concentrated
in regions, which were annotated by pathological experts. Mass values which are
dominant in those spectra may stem from proteins/peptides relating to biomark-
ers as indicators for certain diseases. Hence, classiﬁcation schemes based on NMF
decompositions have been widely investigated [26,30,34].


## Page 27


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
27
Laser
Intensity
m/z
Fig. 2: Structure of MALDI imaging data: A mass spectrum is obtained at dif-
ferent positions of a tissue slice. The full data set is a data cube, which can be
visualized with diﬀerent perspectives. Fixing a position of the tissue slice gives the
mass spectrum at this position. Fixing a particular molecular weight reveals the
distribution of molecules across the tissue slice with this weight.
0
0.005
0.01
3000
4000
5000
6000
7000
8000
9000
0
2
4
0
0.01
0.02
3000
4000
5000
6000
7000
8000
9000
0
0.2
0.4
0.6
0
0.005
0.01
0.015
0.02
3000
4000
5000
6000
7000
8000
9000
0
0.2
0.4
0
0.005
0.01
0.015
3000
4000
5000
6000
7000
8000
9000
0
0.2
0.4
0
0.005
0.01
0.015
0.02
3000
4000
5000
6000
7000
8000
9000
0
0.2
0.4
0
0.01
0.02
0.03
3000
4000
5000
6000
7000
8000
9000
0
0.05
0.1
Fig. 3: NMF of the rat brain dataset for p = 6. Orthogonality constraints on the
channels with σK,1 = 1 and σK,2 = 1.


## Page 28


28
Pascal Fernsel, Peter Maass
0
0.005
0.01
0.015
3000
4000
5000
6000
7000
8000
9000
0
1
2
3
0
0.01
0.02
0.03
3000
4000
5000
6000
7000
8000
9000
0
0.2
0.4
0.6
0
0.01
0.02
3000
4000
5000
6000
7000
8000
9000
0
0.2
0.4
0.6
0.8
0
0.005
0.01
0.015
3000
4000
5000
6000
7000
8000
9000
0
0.2
0.4
0
0.01
0.02
0.03
3000
4000
5000
6000
7000
8000
9000
0
0.2
0.4
0.6
0.8
0
0.01
0.02
0.03
3000
4000
5000
6000
7000
8000
9000
0
0.05
0.1
0.15
0.2
Fig. 4: NMF of the rat brain dataset for p = 6. Orthogonality constraints on the
channels with σK,1 = 200 and σK,2 = 200.
7 Conclusion
In this paper, we investigated methods based on surrogate minimization approaches
for the solution of NMF problems. The interest in NMF methods is related to its
importance for several machine learning tasks. Application for large data sets re-
quire that the resulting algorithms are very eﬃcient and that iteration schemes
only need simple matrix-vector multiplications.
The state of the art for constructing appropriate surrogates are based on case-by-
case studies for the diﬀerent, considered NMF models. In this paper, we embedded
the diﬀerent approaches in a general framework, which allowed us to analyze sev-
eral extensions to the NMF cost functional, including ℓ1- and ℓ2-regularization,
orthogonality constraints, total variation penalties as well as extensions, which
leaded to supervised NMF concepts.
Secondly, we analyzed surrogates in the context of the related iteration schemes,
which are based on ﬁrst order optimality conditions. The requirement of separa-
bility as well as the need of having multiplicative updates, which preserve non-
negativity without additional projections, were analyzed. This resulted in a gen-
eral description of algorithms for alternating minimization of constrained NMF
functionals. The potential of these methods is conﬁrmed by numerical tests using
hyperspectral data from a MALDI imaging experiment.
Several further directions of research would be of interest. First of all, besides the
most widely used penalty terms discussed in this paper further penalty terms, e.g.
higher order TV-terms, could be considered. Secondly, construction principles for


## Page 29


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
29
0
0.01
0.02
0.03
3000
4000
5000
6000
7000
8000
9000
0
0.5
1
0
0.005
0.01
0.015
0.02
3000
4000
5000
6000
7000
8000
9000
0
0.2
0.4
0.6
0
0.005
0.01
0.015
3000
4000
5000
6000
7000
8000
9000
0
0.1
0.2
0.3
0.4
0
0.005
0.01
0.015
0.02
3000
4000
5000
6000
7000
8000
9000
0
0.1
0.2
0.3
0
0.005
0.01
3000
4000
5000
6000
7000
8000
9000
0
0.1
0.2
0.3
0.4
0
0.005
0.01
0.015
3000
4000
5000
6000
7000
8000
9000
0
0.05
0.1
0.15
Fig. 5: NMF of the rat brain dataset for p = 6. Orthogonality constraints on the
channels with σK,1 = 1 and σK,2 = 1 and TV-penalty term with τ = 0.4 and
εTV = 10−7.
more general discrepancy terms could be analyzed (see also [16]).
Potentially more importantly, this paper contains only very ﬁrst results for combin-
ing NMF constructions directly with subsequent classiﬁcation tasks. The question
of an appropriate surrogate functional for the supervised NMF model with lo-
gistic regression used in [26] remains unanswered and also the comparison with
algorithmic alternatives such as ADMM methods needs to be explored.
Acknowledgements The authors want to thank Christine DeMol: her excellent presentations
at several conferences and our joint discussions were the starting point for this paper.
The authors would also like to thank the German Science Foundation. The work on this paper
was funded by project no. GRK 2224/1 (Reasearch traning group π3 parameter identiﬁcation:
analysis, algorithms, applications).
The results in this paper are based on the Master thesis of the ﬁrst author.
References
1. Aebersold, R., Goodlett, D.: Mass spectrometry in proteomics. Chem. Rev. 101(2), 269–
295 (2001)
2. Alexandrov, T., Bartels, A.: Testing for presence of known and unknown molecules in
imaging mass spectrometry. Bioinformatics 29(18), 2335–2342 (2013)
3. Alexandrov, T., Becker, M., Deininger, S., Ernst, G., Wehder, L., Grasmair, M., von
Eggeling, F., Thiele, H., Maass, P.: Spatial segmentation of imaging mass spectrometry
data with edge-preserving image denoising and clustering. Journal of Proteome Research
9(12), 6535–6546 (2010)


## Page 30


30
Pascal Fernsel, Peter Maass
0
0.005
0.01
0.015
3000
4000
5000
6000
7000
8000
9000
0
1
2
3
0
0.01
0.02
0.03
3000
4000
5000
6000
7000
8000
9000
0
0.2
0.4
0
0.01
0.02
0.03
3000
4000
5000
6000
7000
8000
9000
0
0.05
0.1
0.15
0
0.005
0.01
0.015
3000
4000
5000
6000
7000
8000
9000
0
0.1
0.2
0.3
0.4
# 10-6
0
2
4
6
8
3000
4000
5000
6000
7000
8000
9000
0
0.02
0.04
0.06
0
0.01
0.02
0.03
3000
4000
5000
6000
7000
8000
9000
0
0.01
0.02
0.03
0.04
Fig. 6: NMF of the rat brain dataset for p = 6. Orthogonality constraints on the
channels with σK,1 = 10 and σK,2 = 10 and sparsity penalty term on X with λ =
0.06. The sparsity penalty term has in connection with the orthogonality constraint
a comparatively strong inﬂuence on the NMF computation: The sparsity in the
spectra increases signiﬁcantly and thus their biological interpretability, whereas
the anatomic structure in the pseudo channels diminishes.
4. Bishop, C.: Pattern Recognition and Machine Learning. Springer-Verlag New York (2006)
5. B¨ohning, D., Lindsay, B.G.: Monotonicity of quadratic approximation algorithms. Annals
of the Institute of Statistical Mathematics 40(4), 641–663 (1988)
6. Caprioli, R., Terry, B., Gile, J.: Molecular imaging of biological samples: localization of
peptides and proteins using maldi-tof ms. Anal. Chem. 69(23), 4751–4760 (1997)
7. Chambolle, A., Caselles, V., Novaga, M., Cremers, D., Pock, T.: An introduction to total
variation for image analysis. Theoretical Foundations and Numerical Methods for Sparse
Recovery 9, 263–340 (2010)
8. Chan, T., Esedoglu, S., Park, F., Yip, A.: Recent developments in total variation image
restoration. In: In Mathematical Models of Computer Vision. Springer Verlag (2005)
9. Condat, L.: Discrete total variation: New deﬁnition and minimization. Research report,
GIPSA-lab (2016)
10. Cvetkovski, Z.: Inequalities - Theorems, Techniques and Selected Problems.
Springer-
Verlag Berlin Heidelberg (2012)
11. De Mol, C.: Regularized multiplicative algorithms for nonnegative matrix factorization.
Methodological Aspects of Hyperspectral Imaging Workshop (2013)
12. De Pierro, A.R.: On the relation between the isra and the em algorithm for positron
emission tomography. IEEE Transactions on Medical Imaging 12(2), 328–333 (1993)
13. Defrise, M., Vanhove, C., Liu, X.: An algorithm for total variation regularization in high-
dimensional linear problems. Inverse Problems 27(6) (2011)
14. Fessler, J.A.: Statistical image reconstruction methods for transmission tomography. In:
M. Sonka, J. Fitzpatrick (eds.) Handbook of Medical Imaging, Volume 2. Medical Image
Processing and Analysis, pp. 1–70. SPIE (2000)


## Page 31


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
31
15. F´evotte, C., Bertin, N., Durrieu, J.L.: Nonnegative matrix factorization with the itakura-
saito-divergence: With application to music analysis. Neural Computation 21(3), 793–830
(2009)
16. F´evotte, C., Idier, J.: Algorithms for nonnegative matrix factorization with the beta-
divergence. Neural Computation 23(9), 2421–2456 (2011)
17. Hennequin, R., David, B., Badeau, R.: beta-divergence as a subclass of bregman diver-
gence. IEEE Signal Processing Letters 18(2), 83–86 (2011)
18. Hunter, D.R., Lange, K.: A tutorial on mm algorithms. The American Statistician 58(1),
30–37 (2004)
19. Ito, K., Jin, B., Takeuchi, T.: Multi-parameter tikhonov regularization – an augmented
approach. Chinese Annals of Mathematics, Series B 35(3), 383–398 (2014)
20. Jin, B., Lorenz, D.A., Schiﬄer, S.: Elastic-net regularization: error estimates and active
set methods. Inverse Problems 25(11) (2009)
21. Jin, B., Maass, P.: Sparsity regularization for parameter identiﬁcation problems. Inverse
Problems 28(12) (2012)
22. Kobarg, J.H., Maass, P., Oetjen, J., Hirsch, E., Sagiv, C., Golbabaee, M., Vandergheynst,
P.: Numerical experiments with maldi imaging data. Advances in Computational Mathe-
matics 40(3), 667–682 (2014)
23. Lange, K.: Optimization, Springer Texts in Statistics, vol. 95, 2 edn. Springer-Verlag New
York (2013)
24. Lecharlier, L., Mol, C.D.: Regularized blind deconvolution with poisson data. Journal of
Physics: Conference Series 464(1) (2013)
25. Lee, D.D., Seung, H.S.: Learning the parts of objects by non-negative matrix factorization.
Nature 401, 788–791 (1999)
26. Leuschner, J., Fernsel, P., Schmidt, M., Lachmund, D., Boskamp, T., Maass, P.: Supervised
non-negative matrix factorization methods with maldi-imaging applications. Bioinformat-
ics (in review) (2018)
27. Li, T., Ding, C.: Non-negative matrix factorization for clustering: A survey.
In: Data
Clustering: Algorithms and Applications, pp. 149–176 (2013)
28. Louis, A.K.: Inverse und schlecht gestellte Probleme. Vieweg+Teubner Verlag (1989)
29. Oliveira, J.P., Bioucas-Dias, J.M., Figueiredo, M.A.T.: Review: Adaptive total variation
image deblurring: A majorization-minimization approach. Signal Process. 89(9), 1683–
1693 (2009)
30. Phon-Amnuaisuk, S.: Applying non-negative matrix factorization to classify superimposed
handwritten digits. Procedia Computer Science 24, 261–267 (2013)
31. Rudin, L.I., Osher, S., Fatemi, E.: Nonlinear total variation based noise removal algo-
rithms. Physica D 60(1-4), 259–268 (1992)
32. Sun, D.L., F´evotte, C.: Alternating direction method of multipliers for non-negative ma-
trix factorization with the beta-divergence. In: 2014 IEEE International Conference on
Acoustics, Speech and Signal Processing (ICASSP), pp. 6201–6205 (2014)
33. Tan, V.Y.F., F´evotte, C.: Automatic relevance determination in nonnegative matrix fac-
torization with the beta-divergence. arXiv preprint arXiv: 1111.6085v3 (2012)
34. Tang, J., Ceng, X., Peng, B.: New methods of data clustering and classiﬁcation based on
nmf. In: 2011 International Conference on Business Computing and Global Informatiza-
tion, pp. 432–435 (2011)
35. Zhang, Z., Kwok, J.T., Yeung, D.Y.: Surrogate maximization/minimization algorithms for
adaboost and the logistic regression model. In: Proceedings of the Twenty-ﬁrst Interna-
tional Conference on Machine Learning, ICML ’04 (2004)
36. Zhang, Z., Kwok, J.T., Yeung, D.Y.: Surrogate maximization/minimization algorithms
and extensions. Machine Learning 69(1), 1–33 (2007)


## Page 32


32
Pascal Fernsel, Peter Maass
Appendix A
Details on the Derivation of the Algorithms in Section 5
In this section, we give a more detailed derivation of the algorithms presented in
Section 5. We start with the less complex case of the Frobenius norm as discrepancy
term and then turn to the Kullback-Leibler divergence. To cover both aspects, we
derive the update rules of X for the Frobenius discrepancy term and of K in the
case of the KLD. We will also take a closer look at the eﬀect of κ in equation (18)
with respect to the LQBP construction principle.
A.1
Frobenius Norm
We consider the general cost function described in Section 5 for the case of the
Frobenius norm. To compute the update rules for X , it is enough to examine the
function
F(X ) := 1
2∥Y −KX ∥2
F + λ∥X ∥1
|
{z
}
=:F1(X )
+ν
2 ∥X ∥2
F
+ σX ,1
2
∥I −X W ⊺∥2
F + σX ,2
2
∥W −X ∥2
F + ρ
2∥u −YX ⊺β∥2,
where all terms independent from X are omitted. Based on Remark 1 and following
the discussion of Section 4.4, the construction of a surrogate for F can be done
separately for F1 and the remaining penalty terms.
The construction of a surrogate for F1 with the LQBP principle as it has been
done similarly in Subsection 4.4 is essential. If we would use instead a surrogate
for the discrepancy term 1/2∥Y −KX ∥2
F from Subsection 4.1 or 4.2 and take
the ℓ1-penalty term λ∥X ∥1 as surrogate itself, it is easy to see that this would
not lead to multiplicative update rules. It is the ℓ1-penalty term which causes the
diﬃculty. Computing the ﬁrst order optimality condition for the corresponding
surrogate ˜QF (X , A) =: λ∥X ∥1 + ˆQF (X , A) with respect to X would lead to
0 = ∂˜QF
∂Xξζ
(X , A) = λ + ∂ˆQF
∂Xξζ
(X , A),
where the second term on the right hand side does not depend on λ. Hence, we
get a sign in front of λ by solving the equation for Xξζ and we will not obtain
multiplicative updates for X .
A correct surrogate is obtained by using the LQBP principle to F1 and leads to
QF (X , A) := QF1(X , A) + ν
2 ∥X ∥2
F + QOrth(X , A) + QLR(X , A)
with
QF1(X , A) =
m
X
j=1
fY •,j(A•,j) + ∇fY •,j(A•,j)⊺(X •,j −A•,j)
+ 1
2(X •,j −A•,j)⊺ΛfY •,j (A•,j)(X •,j −A•,j),


## Page 33


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
33
where fY •,j : Rp
≥0 →R is deﬁned as
fY •,j(x) := 1
2∥Y •,j −Kx∥2 + λ∥x∥1
and with the diagonal matrix
ΛfY •,j (A•,j)kk = (∇2fY •,j(A•,j) A•,j)k + κk
Akj
= (K⊺KA•,j)k + κk
Akj
.
The functionals QOrth resp. QLR are the surrogates obtained from Theorem 4
resp. Theorem 6. It will turn out that an appropriate choice of κk will ensure a
multiplicative NMF algorithm.
The computation of the ﬁrst order optimality condition for QF leads to
0 = ∂QF
∂Xξζ
(X , A) = (K⊺KA)ξζ −(K⊺Y )ξζ + λ + (K⊺KA)ξζ + κξ
Aξ,ζ
(Xξζ −Aξζ)
+ σX ,1
p
X
k=1
Wkζ
Xξζ
Aξζ
(AW ⊺)ξk −δξk

+ σX ,2(Xξζ −Wξζ)
+ ρβξ
n
X
i=1
Yiζ
Xξζ
Aξζ
(Y A⊺β)i −ui

+ νXξζ.
One can see immediately, that the choice of κξ := λ for all ξ ∈{1, . . . , p} is
appropriate to get rid of the problematic term λ. Hence, we obtain
0 = −(K⊺Y )ξζ + Xξζ
Aξζ
((K⊺KA)ξζ + λ)
+ σX ,1
p
X
k=1
Wkζ
Xξζ
Aξζ
(AW ⊺)ξk −δξk

+ σX ,2(Xξζ −Wξζ)
+ ρβξ
n
X
i=1
Yiζ
Xξζ
Aξζ
(Y A⊺β)i −ui

+ νXξζ.
Reordering the terms leads to
(K⊺Y )ξζ + (σX ,1 + σX ,2)Wξζ + ρβξ(Y ⊺u)ζ
= Xξζ
Aξζ
 (K⊺KA)ξζ + νAξζ + λ + ρβξ(Y ⊺Y A⊺β)ζ + σX ,1(AW ⊺W)ξζ + σX ,2Aξζ

.
Solving for Xξζ and extending the equation to the whole matrix X yields ﬁnally
X = A ◦
K ⊺Y + (σX ,1 + σX ,2)W + ρβu⊺Y
K ⊺KA + (σX ,2 + ν)A + λ1 p×m + ρββ⊺AY ⊺Y + σX ,1AW ⊺W .
By exploiting the surrogate minimization principle as described in Lemma 1, we
get ﬁnally the update rule for X presented in Section 5.


## Page 34


34
Pascal Fernsel, Peter Maass
A.2
Kullback-Leibler Divergence
We take Equation (50) as our starting point. The computation of the ﬁrst order
optimality condition gives
∂QF
∂Kξζ
(K, A) =
m
X
j=1

Xζj −
Yξj
(AX)ξj
AξζXζj
1
Kξζ

+ µKξζ + ω + σK,2(Kξζ −Vξζ)
+ τψζP(A)ξζ(Kξζ −Z(A)ξζ) + σK,1
p
X
k=1
Vξk
Kξζ
Aξζ
(V ⊺A)kζ −δkζ

= 0.
Multiplying on both sides with Kξζ and sorting the terms already gives the system
of quadratic equations mentioned in Section 5, namely
K2
ξζ

µ + τψζP(A)ξζ + σK,1
Aξζ
(V V ⊺A)ξζ + σK,2

+Kξζ


m
X
j=1
Xζj + ω −τψζP(A)ξζZ(A)ξζ −(σK,1 + σK,1)Vξζ


=Aξζ
m
X
j=1
Yξj
(AX)ξj
Xζj.
Taking into account that
m
X
j=1
Yξj
(AX)ξj
Xζj =
 Y
AX X⊺

ξζ
and
m
X
j=1
Xζj = (1n×mX⊺)ξζ,
we obtain the explicit solution of Kξζ by completing the square and get
Kξζ =


Aξζ
µ + τψζP(A)ξζ + σK,1
Aξζ
(V V ⊺A)ξζ + σK,2
 Y
AX X⊺

ξζ
+1
4


(1n×mX⊺)ξζ + ω −τψζP(A)ξζZ(A)ξζ −Vξζ(σK,1 + σK,1)
µ + τψζP(A)ξζ + σK,1
Aξζ
(V V ⊺A)ξζ + σK,2



2 

1/2
−1
2


(1n×mX⊺)ξζ + ω −τψζP(A)ξζZ(A)ξζ −Vξζ(σK,1 + σK,1)
µ + τψζP(A)ξζ + σK,1
Aξζ
(V V ⊺A)ξζ + σK,2


.


## Page 35


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
35
This equation holds for arbitrary ξ ∈{1, . . . , n} and ζ ∈{1, . . . , k}. We therefore
can extend this relation to the whole matrix K and obtain
K
=





A
µ1 n×p + τΨ ◦P(A) + σK,1 VV ⊺A
A
+ σK,21 n×p


◦
 Y
AX X ⊺

+1
4


1 n×mX ⊺+ ω1 n×p −τΨ ◦P(A) ◦Z(A) −(σK,1 + σK,2)V
µ1 n×p + τΨ ◦P(A) + σK,1 VV ⊺A
A
+ σK,21 n×p



2 

1/2
−1
2


1 n×mX ⊺+ ω1 n×p −τΨ ◦P(A) ◦Z(A) −(σK,1 + σK,2)V
µ1 n×p + τΨ ◦P(A) + σK,1 VV ⊺A
A
+ σK,21 n×p


,
which is exactly the described update rule in Section 5.
Appendix B
Kullback-Leibler Divergence Discrepancy and LQBP
In this Section, we will use the LQBP construction principle to derive a multi-
plicative algorithm for the cost function
F(X ) := KL(Y , KX ) =
m
X
j=1
KL(Y •,j, KX •,j) =:
m
X
j=1
fY •,j(X •,j)
Similar to the approach in Appendix A.2, we deﬁne according to the LQBP prin-
ciple the surrogate
QF (X , A) =
m
X
j=1
fY •,j(A•,j) + ∇fY •,j(A•,j)⊺(X •,j −A•,j)
+ 1
2(X •,j −A•,j)⊺ΛfY •,j (A•,j)(X •,j −A•,j)
with the diagonal matrix
ΛfY •,j (A•,j)kk = (∇2fY •,j(A•,j) A•,j)k + κk
Akj
.
It follows for the partial derivatives of f
∂fY •,ζ
∂Xβζ
(X •,ζ) = −
n
X
i=1
YiζKiβ
(KX)iζ
+ Kiβ,
∂2fY •,ζ
∂Xαζ∂Xβζ
(X •,ζ) =
n
X
i=1
YiζKiαKiβ
(KX)2
iζ
.


## Page 36


36
Pascal Fernsel, Peter Maass
The ﬁrst order optimality condition of the surrogate functional leads then to
0 = ∂QF
∂Xξζ
(X , A) = −
n
X
i=1
YiζKiξ
(KA)iζ
+
n
X
i=1
Kiξ
+
Pn
i=1
YiζKiξ
(KA)iζ
+ κξ
Aξζ
(Xξζ −Aξζ).
Setting κξ := Pn
i=1 Kiξ and solving for Xξζ leads ﬁnally to the multiplicative
update rule
X [d+1] =
2X [d]
K [d+1]⊺
Y
K [d+1]X [d] + K [d+1]⊺1 n×m
◦K [d+1]⊺
Y
K [d+1]X [d] ,
which diﬀers from the classical update rule for the KLD described in [11,24,25].
Appendix C
Surrogate of the TV Penalty - Separability
In this section, we will prove the separability of the surrogate functional
QTV(K, A) =
p
X
k=1
ψk
n
X
i=1
1
|∇ikA|

ε2
TV +
X
ℓ∈Ni
K2
ik + K2
ℓk −Kik(Aik + Aℓk)
−Kℓk(Aik + Aℓk) + A2
ik + A2
ℓk

.
(57)
described in Theorem 5. Furthermore, we choose an arbitrary s ∈{1, . . . , n} and
t ∈{1, . . . , p}. The aim is now to ﬁnd all terms in (57) with K2
st and Kst.
To ﬁnd all quadratic terms K2
st in (57), we see that we have to ﬁx the index k,
such that k = t. The remaining indices in (57), which have to be analyzed, are i
and ℓ.
For the case i = s, we ﬁnd that the preceding coeﬃcient is
ψt
|∇stA|
X
r∈Ns
1.
The case ℓ= s can only occur for those indices i, which satisfy s ∈Ni. The
deﬁnition of the adjoint neighbourhood pixels gives
∀i : s ∈Ni
⇔
∀i : i ∈¯
Ns.
Therefore, the corresponding preceding coeﬃcient is here
ψt
X
r∈¯
Ns
1
|∇rtA|.
Altogether, we obtain for the quadratic terms K2
st the coeﬃcient
˜Pst(A) := ψt


1
|∇stA|
X
r∈Ns
1 +
X
r∈¯
Ns
1
|∇rtA|

,


## Page 37


A Survey on Surrogate Approaches to Non-negative Matrix Factorization
37
such that ˜Pst(A) · K2
st takes all quadratic terms of the matrix entries of K in the
surrogate functional into account.
The same can be done with the linear terms Kst, which leads to the coeﬃcient
˜Zst(A) := −ψt


1
|∇stA|
X
r∈Ns
[Ast + Art] +
X
r∈¯
Ns
Ast + Art
|∇rtA|

.
Therefore, the surrogate QTV can be written as
QTV(K, A) =
p
X
t=1
n
X
s=1
h
˜Pst(A) · K2
st + ˜Zst(A) · Kst
i
+ ˜C(A)
for some function ˜C, which only depends on A. This shows the separability of the
surrogate.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
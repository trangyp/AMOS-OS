---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1903.09546v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1903.09546v2_An_asymptotically_superlinearly_convergent_semismooth_Newton_augmented_Lagrangia

> Source: 1903.09546v2_An_asymptotically_superlinearly_convergent_semismooth_Newton_augmented_Lagrangia.pdf

> Pages: 32

---


## Page 1


arXiv:1903.09546v2  [math.OC]  19 Mar 2020
An asymptotically superlinearly convergent semismooth Newton
augmented Lagrangian method for Linear Programming
Xudong Li∗
Defeng Sun†
Kim-Chuan Toh‡
March 19, 2020
Abstract
Powerful interior-point methods (IPM) based commercial solvers, such as Gurobi and Mosek,
have been hugely successful in solving large-scale linear programming (LP) problems. The high
eﬃciency of these solvers depends critically on the sparsity of the problem data and advanced
matrix factorization techniques. For a large scale LP problem with data matrix A that is dense
(possibly structured) or whose corresponding normal matrix AAT has a dense Cholesky factor
(even with re-ordering), these solvers may require excessive computational cost and/or extremely
heavy memory usage in each interior-point iteration. Unfortunately, the natural remedy, i.e.,
the use of iterative methods based IPM solvers, although can avoid the explicit computation
of the coeﬃcient matrix and its factorization, is not practically viable due to the inherent ex-
treme ill-conditioning of the large scale normal equation arising in each interior-point iteration.
To provide a better alternative choice for solving large scale LPs with dense data or requiring
expensive factorization of its normal equation, we propose a semismooth Newton based inex-
act proximal augmented Lagrangian (Snipal) method. Diﬀerent from classical IPMs, in each
iteration of Snipal, iterative methods can eﬃciently be used to solve simpler yet better condi-
tioned semismooth Newton linear systems. Moreover, Snipal not only enjoys a fast asymptotic
superlinear convergence but is also proven to enjoy a ﬁnite termination property. Numerical
comparisons with Gurobi have demonstrated encouraging potential of Snipal for handling large-
scale LP problems where the constraint matrix A has a dense representation or AAT has a dense
factorization even with an appropriate re-ordering. For a few large LP instances arising from
correlation clustering, our algorithm can be up to 20 −100 times faster than the barrier method
implemented in Gurobi for solving the problems to the accuracy of 10−8 in the relative KKT
residual. However, when tested on some large sparse LP problems available in the public do-
main, our algorithm is not yet practically competitive against the barrier method in Gurobi,
especially when the latter can compute the Schur complement matrix and its sparse Cholesky
factorization in each iteration cheaply.
Keywords: Linear programming, semismooth Newton method, augmented Lagrangian method
AMS subject classiﬁcations: 90C05, 90C06, 90C25, 65F10
∗School of Data Science, Fudan University, Shanghai, China (lixudong@fudan.edu.cn); Shanghai Center for
Mathematical Sciences, Fudan University, Shanghai, China.
†Department of Applied Mathematics, The Hong Kong Polytechnic University, Hung Hom, Hong Kong
(defeng.sun@polyu.edu.hk).
‡Department of Mathematics, and Institute of Operations Research and Analytics, National University of Singa-
pore, Singapore (mattohkc@nus.edu.sg). This author’s research is partially supported by the Academic Research
Fund of the Ministry of Singapore under Grant R146-000-257-112.
1


## Page 2


1
Introduction
It is well known that primal-dual interior-point methods (IPMs) as implemented in highly opti-
mized commercial solvers, such as Gurobi and Mosek, are powerful methods for solving large scale
linear programming (LP) problems with conducive sparsity. However, the large scale normal (also
called Schur complement) equation arising in each interior-point iteration is generally highly ill-
conditioned when the barrier parameter is small, and typically it is necessary to employ a direct
method, such as the sparse Cholesky factorization, to solve the equation stably and accurately.
Various attempts, for example in [3, 8, 13, 21, 32], have been made in using an iterative solver,
such as the preconditioned conjugate-gradient (PCG) method, to solve the normal equation when
it is too expensive to compute the coeﬃcient matrix or the sparse Cholesky factorization because
of excessive computing time or memory usage due to ﬁll-ins. For more details on the numerical
performance of iterative methods based IPMs for solving large scale LP, we refer the readers to [13]
and the references therein. However, the extreme ill-conditioning of the normal equation (and also
of the augmented equation) makes it extremely costly for an iterative method to solve the equation
either because it takes excessive number of steps to converge or because constructing an eﬀective
preconditioner is prohibitively expensive. For a long time since their inceptions, iterative methods
based IPMs have not been proven convincingly to be more eﬃcient in general than the highly
powerful solvers, such as Gurobi and Mosek, on various large scale LP test instances. Fortunately,
recent promising progress has been made in the work of Schork and Gondzio [43] where the authors
proposed eﬀective basis matrix preconditioners for iterative methods based IPMs. However, we
should note that as the construction of the basis matrix preconditioners in [43] requires the explicit
storage of the constraint matrix A, the approach may not be applicable to the case when A is not
explicitly given but deﬁned via a linear map. In contrast, the algorithm designed in this paper is
still applicable under the latter scenario. For later discussion, here we give an example where A is
deﬁned by a linear map: A ∈Rn2 →Rp2 such that Ax = vec(B mat(x) DT ), where B, D ∈Rp×n are
given matrices, mat(x) denotes the operation of converting a vector x ∈Rn2 into an n × n matrix
and vec(X) denotes the operation of converting a matrix X ∈Rp×p into a p2-dimensional vector.
It is easy to see that the matrix representation of A is the kronecker product D ⊗B, and it could
be extremely costly to store D ⊗B explicitly when B, D are large dimensional dense matrices.
The goal of this paper is to design a semismooth Newton inexact proximal augmented La-
grangian (Snipal) method for solving large scale LP problems, which has the following key proper-
ties: (a) The Snipal method can achieve fast local linear convergence; (b) The semismooth Newton
equation arising in each iteration can fully exploit the solution sparsity in addition to data sparsity;
(c) The semismooth Newton equation is typically much better conditioned than its counterparts
in IPMs, even when the iterates approach optimality. The latter two properties thus make it cost
eﬀective for one to use an iterative method, such as the PCG method, to solve the aforementioned
linear system when it is large. It is these three key properties that give the competitive advantage
of our Snipal method over the highly developed IPMs for solving certain classes of large scale LP
problems which we will describe shortly.
Consider the following primal and dual LP problems:
(P)
min
n
cT x + δK(x) | Ax = b, x ∈Rno
(D)
max
n
−δ∗
K(A∗y −c) + bT y | y ∈Rmo
where A ∈Rm×n, b ∈Rm, c ∈Rn are given data. The set K = {x ∈Rn | l ≤x ≤u} is a simple
polyhedral set, where l, u are given vectors. We allow the components of l and u to be −∞and ∞,
2


## Page 3


respectively. In particular, K can model the nonnegative orthant Rn
+. In the above, δK(·) denotes
the indicator function over the set K such that δK(x) = 0 if x ∈K and δK(x) = ∞otherwise.
The Fenchel conjugate of δK is denoted by δ∗
K.
We note that while we focus on the indicator
function δK(·) in (P), the algorithm and theoretical results we have developed in this paper are
also applicable when δK is replaced by a closed convex polyhedral function p : Rn →(−∞, ∞]. We
make the following assumption on the problems (P) and (D).
Assumption 1. The solution set of (P) and (D) is nonempty and A has full row rank (hence
m ≤n).
Our Snipal method is designed for the dual LP but the primal variable is also generated in
each iteration. In order for the fast local convergence property to kick-in early, we warm-start the
Snipal method by an alternating direction method of multipliers (ADMM), which is also applied
to the dual LP. We should mention that our goal is not to use Snipal as a general purpose solver
for LP but to complement the excellent general solvers (Gurobi and Mosek) when the latter are
too expensive or have diﬃculties in solving very large scale problems due to memory limitation.
In particular, we are interested in solving large scale LP problems having one of the following
characteristics.
1. The number of variables n in (P) is signiﬁcantly larger than the number of linear constraints
m. We note that such a property is not restrictive since for a primal problem with a huge
number of inequality constraints Ax ≤b and m ≫n, we can treat the dual problem (D) as
the primal LP, and the required property is satisﬁed.
2. The constraint matrix A is large and dense but it has an economical representation such as
being the Kronecker product of two matrices, or A is sparse but AAT has a dense factorization
even with an appropriate re-ordering. For such an LP problem, it may not be possible to
solve it by using the standard interior-point methods implemented in Gurobi or Mosek since
A cannot be stored explicitly. Instead, one would need to use a Krylov subspace iterative
method to solve the underlying large and dense linear system of equations arising in each
iteration of an IPM or Snipal.
In [46], Wright proposed an algorithm for solving the primal problem (P) for the special case
where K = Rn
+. The proposed method is in fact the proximal method of multipliers applied to (P)
while keeping the nonnegative constraint in the quadratic programming (QP) subproblem. More
speciﬁcally, suppose that the iterate at the kth iteration is (xk, yk) and the penalty parameter is
γk = σ−1
k . Then the QP subproblem is given by min{1
2⟨(σkA∗A + σ−1
k In)x, x⟩+ ⟨x, c −A∗yk −
σ−1
k xk −σkA∗b⟩| x ≥0}. In [46], an SOR (successive over-relaxation) method is used to solve
the QP subproblem.
But it is unclear how this subproblem can be solved eﬃciently when n
is large.
In contrast, in this paper, we propose a semismooth Newton based inexact proximal
augmented Lagrangian (Snipal) method that is applied to the dual problem (D) and the associated
subproblems are solved eﬃciently by a semismooth Newton method having at least local superlinear
convegence or even quadratic convergence.
In the pioneering work of De Leone and Mangasarian [28], an augmented Lagrangian method
is applied to an equivalent reformulation of (D), and the QP subproblem of the form min{−bT y +
σ
2 ∥A∗y + z −c + σ−1xk∥2 | y ∈Rm, z ≥0} in each iteration is solved by a projected SOR method.
Interestingly, in a later paper [30], based on the results obtained in [29], Mangasarian designed a
generalized Newton method to ﬁrst solve a penalty problem of the form min{−ǫbT y+ 1
2∥ΠRn
+(A∗y−
c)∥2} and then use its solution to indirectly solve (P) for K = Rn
+, under the condition that the
3


## Page 4


positive parameter ǫ must be below a certain unknown threshold and a strong uniqueness condition
holds. Soon after, [17] observed that the restriction on the parameter in [30] can be avoided by
modifying the procedure in [30] via the augmented Lagrangian method but the corresponding
subproblem in each iteration must be solved exactly. As the generalized Newton system is likely
to be singular, in both [30] and [17], the system is modiﬁed by adding a scalar multiple of the
identity matrix to the generalized Hessian. Such a perturbation, however, would destroy the fast
local convergence property of the generalized Newton method. We also note that to obtain the
minimum norm solution of the primal problem (P), [23] proposed a generalized Newton method
for solving min{1
2∥ΠRn
+(A∗y −rc)∥2 −⟨b, y⟩} with the positive parameter r being suﬃciently large.
Although [23] contains no computational results, the authors obtained the global convergence and
ﬁnite termination properties of the proposed method under the assumption that the Newton linear
systems involved are solved exactly and a certain regularity condition on the nonsingularity of
generalized Jacobians holds. More recently, [48] designed an ALM for the primal problem (P) for
which a bound-constrained convex QP subproblem must be solved in each iteration. In the paper,
this subproblem is solved by a randomized coordinate descent (RCD) method with an active set
implementation. There are several drawbacks to this approach. First, solving the QP subproblem
can be time consuming. Second, the RCD approach can hardly exploit any speciﬁc structure of
the matrix A (for example, when A is deﬁned by the Kronecker product of two given matrices)
to speed up the computation of the QP subproblem. Finally, it also does not exploit the sparsity
structure present in the Hessian of the underlying QP subproblem to speed up the computation.
Here, we employ the an inexact proximal augmented Lagrangian (PAL) method to (D) to simul-
taneously solve (P) and (D). Our entire algorithmic design is dictated by the focus on computational
eﬃciency and generality. From this perspective, now we elaborate on the key diﬀerences between
our paper and [17]. First, without any reformulation, our algorithm is directly applicable to prob-
lems with a more general set K instead of just Rn
+ as in [30] and [17]. Second, we use the inexact
PAL framework which ensures that in each iteration, an unconstrained minimization subproblem
involving the variable y is strongly convex and hence the semismooth Newton method we employ to
solve this subproblem can attain local quadratic convergence. Third, the ﬂexibility of allowing the
PAL subproblems to be solved inexactly can lead to substantial computational savings, especially
during the initial phase of the algorithm. Fourth, for computational eﬃciency, we warm-start our
inexact PAL method by using a ﬁrst-order method. Finally, as solving the semismooth Newton
linear systems is the most critical component of the entire algorithm, we have devoted a substantial
part of the paper on proposing novel numerical strategies to solve the linear systems eﬃciently.
Numerical comparisons of our semismooth Newton proximal augmented Lagrangian method
(Snipal) with the barrier method in Gurobi have demonstrated encouraging potential of our method
for handling large-scale LP problems where the constraint matrix A has a dense representation or
AAT has a dense factorization even with an appropriate re-ordering. For a few large LP instances
arising from correlation clustering, our algorithm can be up to 20−100 times faster than the barrier
method implemented in Gurobi for solving the problems to the accuracy of 10−8 in the relative KKT
residual. However, when tested on some large sparse LP problems available in the MIPLIB2010 [31],
our algorithm is not yet practically competitive against the barrier method in Gurobi, especially
when the latter can compute the Schur complement matrix and its sparse Cholesky factorization
in each iteration cheaply.
The remaining part of the paper is organized as follows.
In the next section, we introduce
a preconditioned proximal point algorithm (PPA) and establish its global and local (asymptotic)
superlinear convergence.
In section 3, we develop a semismooth Newton proximal augmented
Lagrangian method for solving the dual LP (D), and derive its connection to the preconditioned
4


## Page 5


PPA. Section 4 is devoted to developing numerical techniques for solving the linear system of
equations in the semismooth Newton method employed to solve the subproblem in each proximal
augmented Lagrangian iteration. We describe how to employ an ADMM to warm-start the proximal
augmented Lagrangian method in section 5. In section 6, we evaluate the numerical performance
of our algorithm (called Snipal) against the barrier method in Gurobi on various classes of large
scale LPs, including some large sparse LPs available in the public domain. We conclude the paper
in the ﬁnal section.
Notation. We use X and Y to denote ﬁnite dimensional real Euclidean spaces each endowed with
an inner product ⟨·, ·⟩and its induced norm ∥· ∥. For any self-adjoint positive semideﬁnite linear
operator M : X →X, we deﬁne ⟨x, x′⟩M := ⟨x, Mx′⟩and ∥x∥M :=
p
⟨x, Mx⟩for all x, x′ ∈X.
The largest eigenvalue of M is denoted by λmax(M). A similar notation is used when M is replaced
by a matrix M. Let D be a given subset of X. We write the weighted distance of x ∈X to D by
distM(x, D) := infx′∈D ∥x −x′∥M. If M is the identity operator, we just omit it from the notation
so that dist(·, D) is the Euclidean distance function. If D is closed, the Euclidean projector over
D is deﬁned by ΠD(x) := argmin{∥x −d∥| d ∈D}. Let F : X ⇒Y be a multivalued mapping.
We deﬁne the graph of F to be the set gphF := {(x, y) ∈X × Y | y ∈F(x)}. The range of a
multifunction is deﬁned by Range(F) := {y | ∃x with y ∈F(x)}.
2
A preconditioned proximal point algorithm
In this section, we present a preconditioned proximal point algorithm (PPA) and study its conver-
gence properties. In particular, following the classical framework developed in [39, 40], we prove
the global convergence of the preconditioned PPA. Under a mild error bound condition, global
linear rate convergence is also derived. In fact, by choosing the parameter ck in the algorithm to
be suﬃciently large, the linear rate can be as fast as we please. We further show in Section 3.1
that our main Algorithm Snipal is in fact an application of the preconditioned proximal point
algorithm. Hence, Snipal’s convergence properties can be obtained as a direct application of the
general theory developed here.
Let X and Y be ﬁnite dimensional Hilbert spaces and T : X →X be a maximal monotone
operator. Throughout this section, we assume that Ω:= T −1(0) is nonempty. We further note from
[41, Excerise 12.8] that Ωis a closed set. The preconditioned proximal point algorithm generates
for any start point z0 ∈X a sequence {zk} ⊆X by the following approximate rule:
zk+1 ≈Pk(zk),
where
Pk = (Mk + ckT )−1Mk.
(1)
Here {ck} and {Mk} are some sequences of positive real numbers and self-adjoint positive deﬁnite
linear operators over X. If Mk ≡I for all k ≥0, the updating scheme (1) recovers the classical
proximal point algorithm considered in [39]. Since Mk + ckT is a strongly monotone operator,
we know from [41, Proposition 12.54] that Pk is single-valued and is globally Lipschitz continuous.
Here, we further assume that {ck} bounded away from zero, and
(1 + νk)Mk ⪰Mk+1,
Mk ⪰λminI
∀k ≥0
and lim sup
k→∞
λmax(Mk) = λ∞
(2)
with some nonnegative summarable sequence {νk} and constants +∞> λ∞≥λmin > 0. The same
condition on Mk is also used in [34] and can be easily satisﬁed. For example, it holds obviously if
we set λ∞I ⪰Mk ⪰λminI and Mk ⪰Mk+1 for all k ≥0. Note that if T is a linear operator, one
may rewrite Pk as Pk = (I + ckM−1
k T )−1. We show in the next lemma that this expression in fact
5


## Page 6


holds even for a general maximal monotone operator T . Therefore, we can regard the self-adjoint
positive deﬁnite linear operator Mk as a preconditioner for the maximal monotone operator T .
Based on this observation, we name the algorithm described in (1) as the preconditioned proximal
point algorithm.
Lemma 1. Given a constant α > 0, a self-adjoint positive deﬁnite linear operator M and a
maximal monotone operator T on X, it holds that Range(I + αM−1T ) = X and (I + αM−1T )−1
is a single-valued mapping. In addition,
(M + αT )−1M = (I + αM−1T )−1.
Proof. By [2, Proposition 20.24], we know that M−1T is maximally monotone. Hence, Range(I +
αM−1T ) = X and (I + αM−1T )−1 is a single-valued mapping from X to itself.
Now, for any given z ∈X, suppose that z1 = (I + αM−1T )−1(z). Then, it holds that
Mz ∈(M + αT )z1.
Since (M + αT )−1 is a single-valued operator [41, Proposition 12.54], we know that
z1 = (M + αT )−1Mz,
i.e., (I + αM−1T )−1z = (M + αT )−1Mz for all z ∈X.
Thus we have proved the desired
equation.
In the literature, the updating scheme (1) is closely related to the so-called “variable metric
proximal point algorithms”; see for examples [4, 6, 5, 7, 11, 34, 35]. Among these papers, [4, 11, 35]
focus only on the case of optimization, i.e., the maximal monotone operator T is the subdiﬀerential
mapping of a convex function. In addition, they emphasize more on the combination of the proximal
point algorithm with quasi Newton method. In [6] and the subsequent papers [5, 7], the authors
deal with a general maximal monotone operator T and study the following scheme in the exact
setting:
zk+1 = zk + Mk
 (I + ckT )−1 −I

zk.
(3)
The global convergence of the scheme (3) requires a rather restrictive assumption on Mk [6, Hy-
pothesis (H2)], although Mk is not required to be self-adjoint.
In fact, the authors essentially
assumed that the deviation of Mk from the identity operator should be small, and the veriﬁcation
of the assumption can be quite diﬃcult. As far as we aware of, [34] may be the most related work
to ours. In [34], the authors consider a variable metric hybrid inexact proximal point method whose
updating rule consists of an inexact proximal step and a projection step. Moreover, some specially
designed stopping criteria for the inexact solution of the proximal subproblem are also used. How-
ever, due to the extra projection step, the connection between their algorithm and the proximal
method of multipliers [40] is no longer available. Therefore, the results derived in [34] cannot be
directly used to analyze the convergence properties of Snipal proposed in this paper, which is a
variant of the proximal method of multipliers. We should also mention that in [15], Eckstein dis-
cussed nonlinear proximal point algorithms using Bregman functions and the preconditioned PPA
(1) may be viewed as a special instance if Mk is ﬁxed for all k. However, the algorithms and con-
vergence results in [15] are not applicable to our setting where the linear operator Mk can change
across iterations. Since the scheme (1) under the classical setting of [39, 40] ﬁts our context best,
we conduct a comprehensive analysis of its convergence properties which, to our best knowledge,
are currently not available in the literature.
6


## Page 7


For all k ≥0, deﬁne the mapping Qk := I −Pk. Clearly, if 0 ∈T (z), we have that Pk(z) = z
and Qk(z) = 0 for all k ≥0. Similar to [39, Proposition 1], we summarize the properties of Pk and
Qk in the following proposition:
Proposition 1. It holds for all k ≥0 that:
(a) z = Pk(z) + Qk(z) and c−1
k MkQk(z) ∈T (Pk(z)) for all z ∈X;
(b) ⟨Pk(z) −Pk(z′), Qk(z) −Qk(z′)⟩Mk ≥0 for all z, z′ ∈X;
(c) ∥Pk(z) −Pk(z′)∥2
Mk + ∥Qk(z) −Qk(z′)∥2
Mk ≤∥z −z′∥2
Mk for all z, z′ ∈X.
Proof. The proof can be obtained via simple calculations and is similar to the proof of [39, Propo-
sition 1]. We omit the details here.
We list the following two general criteria for the approximate calculation of Pk(zk) which are
analogous to those proposed in [39]:
(A)
∥zk+1 −Pk(zk)∥Mk ≤ǫk,
0 ≤ǫk,
P∞
k=0ǫk < ∞,
(B)
∥zk+1 −Pk(zk)∥Mk ≤δk∥zk+1 −zk∥Mk,
0 ≤δk < 1,
P∞
k=0δk < ∞.
Theorem 1. Suppose that Ω= T −1(0) ̸= ∅. Let {zk} be any sequence generated by the mPPA (1)
under criterion (A). Then {zk} is bounded and
distMk+1(zk+1, Ω) ≤(1 + νk)distMk(zk, Ω) + (1 + νk)ǫk
∀k ≥0.
(4)
In addition, {zk} converges to a point z∞such that 0 ∈T (z∞).
Proof. Let ¯z ∈X be a point satisfying 0 ∈T (¯z). It is readily shown that ¯z = Pk(¯z). We have
∥zk+1 −¯z∥Mk −ǫk ≤∥Pk(zk) −¯z∥Mk = ∥Pk(zk) −Pk(¯z)∥Mk ≤∥zk −¯z∥Mk.
(5)
Since (1 + νk)Mk ⪰Mk+1, we know that
∥zk+1 −¯z∥Mk+1 ≤(1 + νk)∥zk+1 −¯z∥Mk ≤(1 + νk)∥zk −¯z∥Mk + (1 + νk)ǫk.
(6)
Let ΠΩ(z) denotes the projection of z onto Ω. By noting that 0 ∈T (ΠΩ(zk)), we get from the
above inequality (by setting ¯z = ΠΩ(zk)) that
distMk+1(zk+1, Ω) ≤∥zk+1 −ΠΩ(zk)∥Mk+1
≤(1 + νk)∥zk −ΠΩ(zk)∥Mk + (1 + νk)ǫk
= (1 + νk)distMk(zk, Ω) + (1 + νk)ǫk.
Since
∞
X
k=0
(1 + νk)ǫk ≤
∞
X
k=0
ǫk + (max
k≥0 ǫk)
∞
X
k=0
νk < +∞,
we know from [33, Lemma 2.2.2], (5) and (6) that
lim
k→∞∥zk −¯z∥Mk = lim
k→∞∥zk+1 −¯z∥Mk = µ < ∞
and
lim
k→∞∥Pk(zk) −¯z∥Mk = µ.
(7)
7


## Page 8


The boundedness of {zk} thus follows directly from the fact that Mk ⪰λminI for all k ≥0.
Therefore, {zk} has at least one cluster point z∞.
From Proposition 1, we know that for all k ≥0
0 ≤∥Qk(zk)∥2
Mk ≤∥zk −¯z∥2
Mk −∥Pk(zk) −¯z∥2
Mk.
(8)
Therefore, limk→∞∥Qk(zk)∥2
Mk = 0. It follows that
lim
k→∞c−1
k MkQk(zk) = lim
k→∞Qk(zk) = 0,
(9)
because the number ck is bounded away from zero and Mk ⪰λminI for all k ≥0. Since
∥Qk(zk)∥Mk = ∥(zk −zk+1) + (zk+1 −Pk(zk))∥Mk ≥∥zk −zk+1∥Mk −ǫk,
we further have limk→∞∥zk −zk+1∥= 0.
Since z∞is a cluster point of zk and
lim
k→∞∥Pk(zk) −zk+1∥= lim
k→∞∥zk+1 −zk∥= 0,
z∞is also a cluster point of Pk(zk). From Proposition 1 (a), we have that for any w ∈T (z)
0 ≤⟨z −Pk(zk), w −c−1
k MkQk(zk)⟩
∀k ≥0,
which, together with (9), implies
0 ≤⟨z −z∞, w⟩
∀z, w satisfying w ∈T (z).
From the maximality of T , we know that 0 ∈T (z∞).
Hence, we can replace ¯z in (7) by z∞.
Therefore,
lim
k→∞∥zk −z∞∥Mk = 0.
That is limk→∞zk = z∞.
Next, we study the convergence rate of the preconditioned proximal point algorithm.
The
following error bound assumption associated with T is critical to the study of the convergence rate
of the preconditioned PPA.
Assumption 2. For any r > 0, there exists κ > 0 such that
dist(x, T −1(0)) ≤κ dist(0, T (x))
∀x ∈X satisfying dist(x, T −1(0)) ≤r.
(10)
In Rockafellar’s classic work [39], the asymptotic Q-superlinear convergence of PPA is estab-
lished under the assumption that T −1 is Lipschitz continuous at zero. Note that the Lipschitz
continuity assumption on T −1 is rather restrictive, since it implicitly implies that T −1(0) is a sin-
gleton. In [27], Luque extended Rockafellar’s work by considering the following relaxed condition
over T : there exist γ > 0 and ǫ > 0 such that
dist(x, T −1(0)) ≤γdist(0, T (x))
∀x ∈{x ∈X | dist(0, T (x)) < ǫ}.
(11)
We show in the following lemma that this condition in fact implies Assumption 2.
Thus, our
Assumption 2 is quite mild and weaker than condition (11).
8


## Page 9


Lemma 2. Let F be a multifunction from X to Y with F −1(0) ̸= ∅. If F satisﬁes condition (11),
then Assumption 2 holds for F, i.e., for any r > 0, there exists κ > 0 such that
dist(x, F −1(0)) ≤κ dist(0, F(x))
∀x ∈X satisfying dist(x, F −1(0)) ≤r.
Proof. Since F satisﬁes condition (11), there exist ε > 0 and κ0 ≥0 such that if x ∈X satisﬁes
dist(0, F(x)) < ε, then
dist(x, F −1(0)) ≤κ0dist(0, F(x)).
For any r > 0 and x satisfying dist(x, F −1(0)) ≤r, if dist(0, F(x)) < ǫ, then dist(x, F −1(0)) ≤
κ0dist(0, F(x)); otherwise if dist(0, F(x)) ≥ǫ, then
dist(0, F(x)) ≥ǫ ≥ǫ
rdist(x, F −1(0)),
i.e., dist(x, F −1(0)) ≤r
ǫdist(0, F(x)). Therefore, the desired inequality holds for κ = max{κ0, r
ǫ}.
Remark 1. In fact, condition (11) is exactly the local upper Lipschitz continuity of T −1 at the
origin which was introduced by Robinson in [36]. Later, Robinson established in [37] the celebrated
result that every polyhedral multifunction is locally upper Lipschitz continuous, i.e., satisﬁes con-
dition (11). Thus from Lemma 2, we know that any polyhedral multifunction F with F −1(0) ̸= ∅
satisﬁes Assumption 2.
Since the nonnegative sequences {νk} and {ǫk} in condition (2) and the stopping criterion (A),
respectively, are summable, we know that 0 < Π∞
k=0(1 + νk) < +∞and we can choose r to be
a positive number satisfying r > P∞
k=0 ǫk(1 + νk). Assume that T satisﬁes Assumption 2, then
associated with r, there exists a positive constant κ such that (10) holds. With these preparations,
we prove in the following theorem the asymptotic Q-superlinear (R-superlinear) convergence of the
weighted (unweighted) distance between the sequence generated by the preconditioned PPA and
Ω.
Theorem 2. Suppose that Ω̸= ∅and the initial point z0 satisﬁes
distM0(z0, Ω) ≤r −P∞
k=0 ǫk(1 + νk)
Π∞
k=0(1 + νk)
.
Let {zk} be the inﬁnite sequence generated by the preconditioned PPA under criteria (A) and (B)
with {ck} nondecreasing (ck ↑c∞≤∞). Then for all k ≥0, it holds that
distMk+1(zk+1, Ω) ≤µkdistMk(zk, Ω),
(12)
where µk = (1 + νk)(1 −δk)−1 δk + (1 + δk)κλmax(Mk)/
q
c2
k + κ2λ2max(Mk)

and
lim sup
k→∞
µk = µ∞=
κλ∞
p
c2∞+ κ2λ2∞
< 1
(µ∞= 0 if c∞= ∞),
(13)
with λ∞given in (2). In addition, one has that for all k ≥0,
dist(zk+1, Ω) ≤
µk
p
λmin(Mk+1)
distMk(zk, Ω).
(14)
9


## Page 10


Proof. From (4) in Theorem 1, we know that for all k ≥0, distMk(zk, Ω) ≤Π∞
k=0(1+νk)distM0(z0, Ω)+
P∞
k=0 ǫk(1 + νk) ≤r, and consequently,
distMk(Pk(zk), Ω) ≤∥Pk(zk)−ΠΩ(zk)∥Mk= ∥Pk(zk) −Pk(ΠΩ(zk))∥Mk ≤distMk(zk, Ω) ≤r
∀k ≥0.
From Proposition 1 (a), we have
c−1
k MkQk(zk) ∈T (Pk(zk)),
which, together with Assumption 2, implies that for all k ≥0
dist(Pk(zk), Ω) ≤κc−1
k ∥MkQk(zk)∥.
It further implies that for all k ≥0,
1
p
λmax(Mk)
distMk(Pk(zk), Ω) ≤dist(Pk(zk), Ω) ≤
p
λmax(Mk)κc−1
k ∥Qk(zk)∥Mk.
Now taking ¯z = ΠΩ(zk), we deduce from (8) that for all k ≥0,
∥Qk(zk)∥2
Mk ≤∥zk −ΠΩ(zk)∥2
Mk −∥Pk(zk) −ΠΩ(zk)∥2
Mk
≤dist2
Mk(zk, Ω) −dist2
Mk(Pk(zk), Ω).
(15)
Therefore, it holds that
distMk(Pk(zk), Ω) ≤
κλmax(Mk)
q
c2
k + κ2λ2max(Mk)
distMk(zk, Ω)
∀k ≥0.
(16)
Under stopping criterion (B), we further have for all k ≥0,
∥zk+1 −ΠΩ(Pk(zk))∥Mk ≤∥zk+1 −Pk(zk)∥Mk + ∥Pk(zk) −ΠΩ(Pk(zk))∥Mk
≤
δk∥zk+1 −zk∥Mk + ∥Pk(zk) −ΠΩ(Pk(zk))∥Mk
≤
δk
 ∥zk+1 −ΠΩ(Pk(zk))∥Mk + ∥zk −ΠΩ(Pk(zk)∥Mk

+ ∥Pk(zk) −ΠΩ(Pk(zk))∥Mk.
Thus,
(1 −δk)∥zk+1 −ΠΩ(Pk(zk))∥Mk ≤δk∥zk −ΠΩ(Pk(zk)∥Mk + ∥Pk(zk) −ΠΩ(Pk(zk))∥Mk.
Now
δk∥zk −ΠΩ(Pk(zk)∥Mk ≤δk∥Pk(zk) −ΠΩ(Pk(zk)∥Mk + δk∥Qk(zk)∥Mk
≤
δk∥Pk(zk) −ΠΩ(Pk(zk)∥Mk + δkdistMk(zk, Ω),
where the last inequality follows from (15). By using the above inequality in the previous one, we
get
(1 −δk)∥zk+1 −ΠΩ(Pk(zk))∥Mk ≤δkdistMk(zk, Ω) + (1 + δk)distMk(Pk(zk), Ω).
10


## Page 11


Therefore, from the last inequality and (16), it holds that for all k ≥0,
distMk+1(zk+1, Ω) ≤(1 + νk)distMk(zk+1, Ω)
≤(1 + νk)∥zk+1 −ΠΩ(Pk(zk))∥Mk ≤µkdistMk(zk, Ω),
where µk = (1 + νk)(1 −δk)−1
δk + (1 + δk)κλmax(Mk)/
q
c2
k + κ2λ2max(Mk)

. That is, (12) holds
for all k ≥0. Since for all k ≥0, Mk ⪰λminI, (13) and (14) can be obtained through simple
calculations.
Remark 2. Suppose that {δk} in criterion (B) is nonincreasing and νk ≡0 for all k ≥0. Since {ck}
is nondecreasing and λmax(Mk) is nonincreasing, we know that {µk} is nonincrasing. Therefore,
if one chooses c0 large enough such that µ0 < 1, then we have µk ≤µ0 < 1 for all k ≥0. The
inequality (12) thus implies the global Q-linear convergence of {distMk(zk, Ω)}. In addition, (14)
implies that for all k ≥0,
dist(zk+1, Ω) ≤
 distM0(z0, Ω)/
p
λmin

Πk
i=0µi ≤(µ0)k+1 distM0(z0, Ω)/
p
λmin

,
i.e., {dist(zk, Ω)} converges globally R-linearly.
3
A semismooth Newton proximal augmented Lagragian method
Note that we can equivalently rewrite problem (D) in the following minimization form:
(D)
−min
n
g(y) := δ∗
K(A∗y −c) −bT y
o
.
Associated with this unconstrained formulation, we write the augmented Lagrangian function fol-
lowing the framework developed in [41, Examples 11.46 and 11.57]. To do so, we ﬁrst identify (D)
with the problem of minimizing g(y) = eg(y, 0) over Rm for
eg(y, ξ) = −bT y + δ∗
K(A∗y −c + ξ)
∀(y, ξ) ∈Rm × Rn.
Obviously, eg is jointly convex in (y, ξ). Now, we are able to write down the Lagrangian function
l : Rm × Rn through partial dualization as follows:
l(y; x) := inf
ξ {eg(y, ξ) −⟨x, ξ⟩} = −bTy −⟨x, c −A∗y⟩−δK(x).
Thus, the KKT conditions associated with (P) and (D) are given by
−b + Ax = 0,
A∗y −c ∈∂δK(x),
(x, y) ∈Rn × Rm.
(17)
Given σ > 0, the augmented Lagrangian function corresponding to (D) can be obtained by
Lσ(y; x) := sup
s∈Rn
n
l(y; s) −1
2σ ∥s −x∥2o
= −bT y −inf
s∈Rn
n
δK(s) + ⟨s, c −A∗y⟩+ 1
2σ∥s −x∥2o
= −bT y −⟨ΠK(x −σ(c −A∗y)), c −A∗y⟩−1
2σ ∥ΠK(x −σ(c −A∗y)) −x∥2.
11


## Page 12


We propose to solve (D) via an inexact proximal augmented Lagrangian method. Our algorithm is
named as the semi-smooth Newton inexact proximal augmented Lagrangian (Snipal) method be-
cause we will design a semi-smooth Newton method to solve the underlying augmented Lagrangian
subproblems. Its template is given as follows.
Algorithm 1 Snipal: Semi-smooth Newton inexact proximal augmented Lagrangian
Let σ0, σ∞> 0 be given parameters, {τk}∞
k=0 be a given nonincreasing sequence such that τk > 0
for all k ≥0. Choose (x0, y0) ∈Rn × Rm. For k = 1, . . ., perform the following steps in each
iteration.
Step 1. Compute
yk+1 ≈argminy∈Rm
n
Lσk(y; xk) + τk
2σk
∥y −yk∥2o
(18)
via the semismooth Newton method.
Step 2. Compute xk+1 = ΠK
 xk −σk(c −A∗yk+1)

.
Step 3. Update σk+1 ↑σ∞≤∞.
Note that diﬀerent from the classic proximal method of multipliers in [40] with τk ≡1 for all
k, we allow an adaptive choice of the parameter τk in the proximal term
τk
2σk ∥y −yk∥2 in the inner
subproblem (18) of Algorithm Snipal. Here, the proximal term is added to guarantee the existence
of the optimal solution to the inner subproblem (18), and to ensure the positive deﬁniteness of the
coeﬃcient matrix of the underlying semi-smooth Newton linear system. Moreover, our numerical
experience with Snipal indicates that having the additional ﬂexibility of choosing the parameter τk
can help to improve the practical performance of the algorithm. We emphasize here that comparing
with [40], our modiﬁcations focus more on the computational and implementational aspects.
While the introduction of the parameters {τk} brings us more ﬂexibility and some promising
numerical advantages, it also makes the convergence analysis of the algorithm more challenging.
Fortunately, we are able to rigorously characterize the connection between our Algorithm Snipal
and the preconditioned PPA studied in Section 2. As one will see in the subsequent text, this
connection allows us to conduct a comprehensive convergence analysis for Algorithm Snipal. From
the convergence analysis, we also note that
τk
2σk ∥y−yk∥2 can be replaced by a more general proximal
term, i.e.,
1
2σk ∥y −yk∥2
Tk with a symmetric positive deﬁnite matrix Tk.
3.1
Global convergence properties of Snipal
In this section, we present a comprehensive analysis for the convergence properties of Snipal. The
global convergence and global linear-rate convergence of Snipal are presented as an application of
the theory of the preconditioned PPA.
To establish the connection between Snipal and the preconditioned PPA, we ﬁrst introduce
some notation. To this end, for k = 0, 1, . . . , and any given (¯y, ¯x) ∈Rm × Rn, deﬁne the function
Pk(¯y, ¯x) := arg minimax
y,x
n
l(y, x) + τk
2σk
∥y −¯y∥2 −
1
2σk
∥x −¯x∥2o
.
(19)
Corresponding to the closed proper convex-concave function l, we can deﬁne the maximal monotone
12


## Page 13


operator Tl [38, Corollary 37.5.2], by
Tl(y, x) := {(y′, x′) | (y′, −x′) ∈∂l(y, x)}
= {(y′, x′) | y′ = −b + Ax, x′ ∈c −A∗y + ∂δK(x)},
whose corresponding inverse operator is given by
T −1
l
(y′, x′) := arg minimax
y,x
{l(y, x) −⟨y′, y⟩+ ⟨x′, x⟩}.
(20)
Since K is a polyhedral set, ∂δK is known to be a polyhedral multifunction (see, e.g., [24, p. 108]).
As the sum of two polyhedral multifunctions is also polyhedral, Tl is also polyhedral. Deﬁne, for
k = 0, 1, . . . ,
Λk = Diag (τkIm, In) ≻0.
(21)
The optimal solution of problem (19), i.e., Pk(¯y, ¯x), can be obtained via the following lemma.
Lemma 3. For all k ≥0, it holds that
Pk(¯y, ¯x) = (Λk + σkTl)−1Λk(¯y, ¯x)
∀(¯y, ¯x) ∈Rm × Rn.
(22)
If (y∗, x∗) ∈T −1
l
(0), then Pk(y∗, x∗) = (y∗, x∗).
In Snipal, at k-th iteration, denote
ψk(y) := Lσk(y; xk) + τk
2σk
∥y −yk∥2.
(23)
From the property of the proximal mapping, we know that ψk is continuously diﬀerentiable and
∇ψk(y) = −b + A ΠK
 xk + σk(A∗y −c)

+ τkσ−1
k (y −yk).
As a generalization of Proposition 8 in [40], the following proposition about the weighted distance
between (yk+1, xk+1) generated by Snipal and Pk(yk, xk) is important for designing the stopping
criteria for the subproblem (18) and establishing the connection between Snipal and the precondi-
tioned PPA.
Proposition 2. Let Pk, Λk and ψk be deﬁned in (19), (21) and (23), respectively. Let (yk+1, xk+1)
be generated by Algorithm Snipal at iteration k + 1. It holds that
∥(yk+1, xk+1) −Pk(yk, xk)∥Λk ≤
σk
min(√τk, 1) ∥∇ψk(yk+1)∥.
(24)
Proof. Since ∇ψk(yk+1) = ∇yLσk(yk+1, xk) + τkσ−1
k (yk+1 −yk), we have
∇ψk(yk+1) + σ−1
k τk(yk −yk+1) = ∇yLσk(yk+1, xk),
which, by [40, Proposition 7], implies (∇ψk(yk+1)+σ−1
k τk(yk−yk+1), σ−1
k (xk−xk+1)) ∈Tl(yk+1, xk+1).
Thus,
σk(∇ψk(yk+1), 0) + Λk
 (yk, xk) −(yk+1, xk+1)

∈σkTl(yk+1, xk+1)
and σk(∇ψk(yk+1), 0) + Λk(yk, xk) ∈(Λk + σkTl)(yk+1, xk+1), or equivalently,
(yk+1, xk+1) = (Λk + σkTl)−1Λk
 Λ−1
k (σk∇ψk(yk+1), 0) + (yk, xk)

.
13


## Page 14


Then, by Lemma 3 and Proposition 1, we know that
∥(yk+1, xk+1) −Pk(yk, xk)∥Λk
= ∥(Λk + σkTl)−1Λk
 Λ−1
k (σk∇ψk(yk+1), 0) + (yk, xk)

−(Λk + σkTl)−1Λk
 (yk, xk)

∥Λk
≤∥Λ−1
k
 σk∇ψk(yk+1), 0

∥Λk ≤
σk
min (√τk, 1)∥∇ψk(yk+1)∥.
This completes the proof for the proposition.
Based on Proposition 2, we propose the following stopping criteria for the approximate compu-
tation of yk+1 in Step 1 of Snipal:
(A’)
∥∇ψk(yk+1)∥≤min(√τk, 1)
σk
ǫk,
0 ≤ǫk,
P∞
k=0ǫk < ∞,
(B’)
∥∇ψk(yk+1)∥≤δk min(√τk, 1)
σk
∥(yk+1, xk+1) −(yk, xk)∥Λk, 0 ≤δk < 1, P∞
k=0δk < ∞.
For the convergence of Snipal, we also need the following assumption on τk:
Assumption 3. The positive sequence {τk} is non-increasing and bounded away from zero, i.e.,
τk ↓τ∞> 0 for some positive constant τ∞.
Under Assumption 3, we have that for all k ≥0,
Λk ⪰Λk+1 and Λk ⪰min(1, τ∞)Im+n.
We now present the global convergence result for Snipal in the following Theorem. Similar to the
case in [40], it is in fact a direct application of Theorem 1.
Theorem 3 (Global convergence of Snipal). Suppose that Assumptions 1 and 3 hold. Let {(yk, xk)}
be the sequence generated by Algorithm Snipal with the stopping criterion (A’). Then {(yk, xk)}
is bounded. In addition, {xk} converges to an optimal solution of (P) and {yk} converges to an
optimal solution of (D), respectively.
Since Tl is a polyhedral multifunction, we know from Lemma 2 and Remark 1 that Tl satisﬁes
Assumption 2. Let r be a positive number satisfying r > P∞
i=0 ǫk with ǫk being the summable
sequence in (A’). Then, there exists κ > 0 associated with r such that for any (y, x) ∈Rm × Rn
satisfying dist((y, x), T −1
l
(0)) ≤r,
dist((y, x), T −1
l
(0)) ≤κ dist(0, Tl(y, x)).
(25)
As an application of Theorem 2, we are now ready to show the asymptotic superlinear convergence
of Snipal in the following theorem.
Theorem 4 (Asymptotic superlinear convergence of Snipal). Suppose that Assumptions 1 and 3
hold and the initial z0 := (y0, x0) satisﬁes distΛ0(z0, T −1
l
(0)) ≤r −P∞
i=0 ǫk. Let κ be the modulus
given in (25) and {zk := (yk, xk)} be the inﬁnite sequence generated by the preconditioned PPA
under criteria (A’) and (B’). Then, for all k ≥0, it holds that
distΛk+1(zk+1, T −1
l
(0)) ≤µkdistΛk(zk, T −1
l
(0)),
dist(zk+1, T −1
l
(0)) ≤
µk
p
min(1, τk+1)
distΛk(zk, T −1
l
(0)),
(26)
14


## Page 15


where µk = (1 −δk)−1
δk + (1 + δk)κγk/
q
σ2
k + κ2γ2
k

with γk := max(τk, 1) and
lim
k→∞µk = µ∞=
κγ∞
p
σ2∞+ κ2γ2∞
< 1
(µ∞= 0 if σ∞= ∞),
with γ∞= max(τ∞, 1).
Remark 3. Suppose that {δk} in criterion (B’) is nonincreasing. We know from Remark 2 that if
one chooses σ0 large enough such that µ0 < 1, then µk ≤µ0 < 1 for all k ≥0. Thus, from (26),
we have the global linear convergence of {distΛk(zk, T −1
l
(0))} and {dist(zk, T −1
l
(0))}.
3.2
Semismooth Newton method for subproblems (18)
In this subsection, we discuss how the subproblem (18) in Snipal can be solved eﬃciently. As is
mentioned in the name of Snipal, we propose to solve (18) via an inexact semismooth Newton
method which converges at least locally superlinearly. In fact, the local convergence rate can even
be quadratic.
For given (˜x, ˜y) ∈Rn × Rm and τ, σ > 0, deﬁne the function ψ : Rm →R as
ψ(y) := Lσ(y; ˜x) + τ
2σ ∥y −˜y∥2
∀y ∈Rm,
and we aim to solve
min
y∈Rm ψ(y).
(27)
Note that ψ is strongly convex and continuously diﬀerentiable over Rm with
∇ψ(y) = −b + A ΠK
 ˜x + σ(A∗y −c)

+ τσ−1(y −˜y).
Hence, we know that for any given α ≥infy ψ(y), the level set Lα := {y ∈Rm | ψ(y) ≤α} is a
nonempty closed and bounded convex set. In addition, problem (27) has a unique optimal solution
which we denote as ¯y.
As an unconstrained optimization problem, the optimality condition for (27) is given by
∇ψ(y) = 0,
y ∈Rm,
(28)
and ¯y is the unique solution to this nonsmooth equation. Since ΠK is a Lipschitz continuous piece-
wise aﬃne function, we have that ∇ψ is strongly semismooth. Hence, we can solve the nonsmooth
equation (28) via a semismooth Newton method. For this purpose, we deﬁne the following operator:
ˆ∂2ψ(y) := τσ−1Im + σA∂ΠK(˜x + σ(A∗y −c))A∗
∀y ∈Rm,
where ∂ΠK(˜x + σ(A∗y −c)) is the Clarke subdiﬀerential [12] of the Lipschitz continuous mapping
ΠK(·) at ˜x + σ(A∗y −c). Note that from [22, Example 2.5], we have that
ˆ∂2ψ(y)d = ∂2ψ(y)d
∀d ∈Rm,
where ∂2ψ(y) denotes the generalized Hessian of ψ at y. However, we caution the reader that it is
unclear whether ˆ∂2ψ(y) = ∂2ψ(y). Given any y ∈Rm, deﬁne
H := τσ−1Im + σAUA∗
(29)
15


## Page 16


with U ∈∂ΠK(˜x + σ(A∗y −c)). Then, we know that H ∈ˆ∂2ψ(y) and H is symmetric positive
deﬁnite.
After these preparations, we are ready to present the following semismooth Newton method for
solving the nonsmooth equation (28) and we can expect a fast local superlinear convergence.
Algorithm 2 Ssn: A Semi-smooth Newton method for solving (28) (Ssn(˜x, ˜y, σ, τ))
Given τ > 0, σ > 0, choose parameters ¯η ∈(0, 1), γ ∈(0, 1] and µ ∈(0, 1/2), δ ∈(0, 1) and set
y0 = ˜y. Iterate the following steps for j = 0, 1, . . ..
Step 1. Choose Uj ∈∂ΠK(˜x+σ(A∗yj −c)). Set Hj := τσ−1Im+σAUjA∗. Solve the linear system
Hjd = −∇ψ(yj)
(30)
exactly or by a Krylov iterative method to ﬁnd dj such that ∥Hjdj + ∇ψ(yj)∥
≤
min(¯η, ∥∇ψ(yj)∥1+γ).
Step 2. (Line search) Set αj = δmj, where mj is the ﬁrst nonnegative integer m for which
ψ(yj + δmdj) ≤ψ(yj) + µδm⟨∇ψ(yj), dj⟩.
Step 3. Set yj+1 = yj + αjdj.
The convergence results of Algorithm Ssn are stated in the following theorem.
Theorem 5. Let {yj} be the inﬁnite sequence generated by Algorithm Ssn. It holds that {yj}
converges to the unique optimal solution ¯y of (27) and ∥yj+1 −¯y∥= O(∥yj −¯y∥1+γ).
Proof. We know from [49, Proposition 3.3] that dj is always a descent direction. Then, the strong
convexity of ψ and [49, Theorem 3.4] imply that {yj} converges to the unique optimal solution ¯y
of (27). By (29), we have that the symmetric positive deﬁnite matrix Hj ∈ˆ∂2ψ(yj) satisﬁes the
property that Hj ⪰τσ−1Im for all j. The desired results thus can be obtained by following the
proof of [49, Theorem 3.5]. We omit the details here.
3.3
Finite termination property of Snipal
In our numerical experience with Snipal, we observe that it nearly possesses a certain ﬁnite con-
vergence property for solving (P) and (D) when σk and 1/τk are suﬃciently large. We note that
most available theoretical results corresponding to the ﬁnite termination property of proximal point
algorithms require each subproblem involved to be solved exactly, e.g., see [39], [40] and [27]. Hence,
all these results cannot be directly adopted to support our numerical ﬁndings. In this section, we
aim to investigate the ﬁnite termination property of Snipal by showing that it is possible to obtain
a solution pair of (P) and (D) without requiring the exact solutions of each and every subproblem
involved in the algorithm.
Our analysis is based on an interesting property called “staircase property” associated with
subdiﬀerential mappings of convex closed polyhedral functions. Let
f(x) := cT x + δK(x) + δ{x|Ax=b}(x).
16


## Page 17


Clearly, f is a convex closed polyhedral function. From [16, Sec. 6] and earlier work in [14, 27],
we know that its subdiﬀerential mapping enjoys the following staircase property, i.e., there exists
δ > 0 such that
w ∈∂f(x), ∥w∥≤δ ⇒0 ∈∂f(x).
(31)
Based on the staircase property of ∂f, we present the ﬁnite convergence property of Snipal in the
following theorem.
Theorem 6. Suppose that Assumptions 1 and 3 hold and let {(yl, xl)} be the inﬁnite sequence
generated by Snipal with the stopping criterion (A′). For any given k ≥0, suppose that ¯yk+1 is an
exact solution to the following optimization problem:
¯yk+1 = argmin
y∈Rm Lσk(y; xk).
(32)
Then, the following results hold.
(a) The point ¯xk+1 := ΠK
 xk −σk(c −A∗¯yk+1)

is the unique solution to the following proximal
problem:
min
n
cT x +
1
2σk
∥x −xk∥2 | Ax = b, x ∈K
o
.
(33)
(b) There exists a positive scalar ¯σ independent of k such that for all σk ≥¯σ, ¯xk+1 also solves the
problem (P).
(c) If xk is a solution of (P), then ¯yk+1 also solves (D).
Proof. (a) Observe that the dual of (32) is exactly (33), and the KKT conditions associated with
(32) and (33) are given as follows:
x = ΠK
 xk −σk(c −A∗y)

,
Ax −b = 0.
(34)
Since ¯yk+1 is a solution of the problem (32), it holds from the optimality condition associated with
(32) that AΠK(xk −σk(c −A∗¯yk+1)) = b. Thus, (¯xk+1, ¯yk+1) satisfy (34). Therefore, ¯xk+1 solves
(33). The uniqueness of ¯xk+1 follows directly from the strong convexity of (33).
(b) By Theorem 3, we know that xl →x∗as l →∞for some x∗∈∂f −1(0). Therefore, there
exists a constant M > 0 (independent of k) such that
∥xl −x∗∥≤M
∀l ≥0.
(35)
From the optimality of ¯xk+1 and the deﬁnition of f, we have that
1
σk
(xk −¯xk+1) ∈∂f(¯xk+1).
It also holds from the nonexpansive property of the proximal mapping that ∥¯xk+1−x∗∥≤∥xk−x∗∥,
which, together with (35), further implies that
∥¯xk+1 −xk∥≤2∥xk −x∗∥≤2M.
Therefore, there exists ¯σ > 0 (independent of k) such that for all σk ≥¯σ and k ≥0,
1
σk
∥¯xk+1 −xk∥≤2M
¯σ
≤δ,
17


## Page 18


where δ > 0 is the constant given in (31). Thus, by using the “staircase” property (31), we know
that
0 ∈∂f(¯xk+1).
That is, ¯xk+1 solves the problem (P).
(c) Next, consider the case when xk is a solution of (P). From the minimization property of xk,
it is clear that the unique solution of (33) must be ¯xk+1 = xk. Thus, xk = ΠK
 xk −σk(c−A∗¯yk+1)

and Axk = b. Note that it can be equivalently rewritten as:
A∗¯yk+1 −c ∈∂δK(xk),
Axk = b,
i.e., (xk, ¯yk+1) satisfy the KKT conditions for (P) and (D) in (17). Thus, ¯yk+1 solves (D).
Remark 4. We now remark on the signiﬁcance of the above theorem. Essentially, it says that when
σk is suﬃciently large with σk ≥¯σ, then ¯xk+1 solves (P), and it holds that ¯yk+2 = argmin Lσk+1(y; ¯xk+1)
solves (D).
From the fact that the Ssn method used to solve (28) has the ﬁnite termination property [19, 44],
we know that yk+1 computed in Step 1 of Snipal is in fact the exact solution of the subproblem
min ψk(y) when the corresponding linear system is solved exactly. In addition, when σk is suﬃciently
large and τk is small enough, we have that
0 = ∇Lσk(yk+1; xk) + τkσ−1
k (yk+1 −yk) ≈∇Lσk(yk+1; xk),
and consequently, yk+1 can be regarded as a highly accurate solution to the problem min Lσk(y; xk).
In this sense, Theorem 6 explains the ﬁnite termination phenomenon in the practical performance
of Snipal.
4
Solving the linear systems arising from the semismooth Newton
method
Note that the most expensive operation in Algorithm Ssn is the computation of the search direction
d ∈Rm through solving the linear system (30). To ensure the eﬃciency of Ssn and consequently
that of Snipal, in this section, we shall discuss eﬃcient approaches for solving (30) in Algorithm
Ssn. Given c, ˜x ∈Rn, ˜y ∈Rm, the parameters τ, σ > 0 and the current iterate of Ssn ˆy ∈Rm, let
g := −∇ψ(ˆy) = Rp −τσ−1(ˆy −˜y),
where Rp = b −AΠK(w(ˆy)) with w(ˆy) := ˜x + σ(A∗ˆy −c). At each Ssn iteration, we need to solve
a linear system of the form:
H∆y = g,
(36)
where H = τσ−1Im + σAUA∗with U ∈∂ΠK(w(ˆy)). Deﬁne the index set J = {i | li < [w(ˆy)]i <
ui, i = 1, . . . , n} and p = |J |, i.e., the cardinality of J . In the implementation, we always construct
the generalized Jacobian matrix U ∈∂ΠK(w(ˆy)) as a diagonal matrix in the following manner:
U = Diag(u) with ui =
(
1
if
i ∈J ,
0
otherwise,
i = 1, . . . , n.
18


## Page 19


Without the loss of generality, we can partition A ≡[AJ , AN ] with AJ ∈Rm×p, AN ∈Rm×(n−p),
and hence
H = σAJ A∗
J + τσ−1Im = σ(AJ A∗
J + ρIm)
(37)
where ρ := τσ−2. To solve the linear system (36) eﬃciently, we need to consider various scenarios.
In the discussion below, we use nnzden(M) to denote the density of the nonzero elements of a given
matrix M.
(a) First, we consider the case where p ≥m and the sparse Cholesky factorization of AJ A∗
J
can be computed at a moderate cost. In this case, the main cost of solving the linear system is in
forming the matrix AJ A∗
J at the cost of O(m2p nnzden(AJ )) and computing the sparse Cholesky
factorization of AJ A∗
J + ρIm.
Observe that the index set J generally changes from one SSN iteration to the next. However,
when the SSN method is converging, the index set J may only change slightly from the current
iteration to the next. In this case, one can update the inverse of H via a low-rank update by using
the Sherman-Morrison-Woodbury formula.
When it is expensive to compute and factorize H, one would naturally use a preconditioned
conjugate gradient (PCG) method or the MINRES (minimim residual) method to solve (36). Ob-
serve that the condition number of H is given by κ(H) = (ω2
max + ρ)/(ω2
min + ρ) if p ≥m, where
ωmax, ωmin are the largest and smallest singular value of AJ , respectively.
Note that when A
is not explicitly given as a matrix, one can compute the matrix-vector product Hv as follows:
Hv = σρv + σA(eJ ◦(A∗v)) where eJ ∈Rn is a 0-1 vector whose non-zero entries are located at
the index set J , and “◦” denotes the elementwise product.
(b) Next we consider the case where p < m. In this case, it is more economical to solve (36) by
using the Sherman-Morrison-Woodbury formula to get
∆y = H−1g = τ −1σ
 Im −PJ

g,
(38)
where PJ = AJ G−1A∗
J , G = ρIp + A∗
J AJ ∈Rp×p. Thus to compute ∆y, one needs only to solve a
smaller p×p linear system of equations Gv = A∗
J g. Observe that when ρ ≪1, ∆y is approximately
the orthogonal projection of τ −1σg onto the null space of A∗
J .
To solve (38), one can compute the sparse Cholesky factorization of the symmetric positive
deﬁnite matrix G ∈Rp×p if the task can be done at a reasonable cost. In this case, the main
cost involved in (38) is in computing A∗
J AJ at the cost of O(p2m nnzden(AJ )) operations and the
sparse Cholesky factorization of G = ρIp + A∗
J AJ .
When it is too expensive to compute and factorize G, one can use a Krylov iterative method to
solve the p × p linear system of equations:
Gv = (ρIp + A∗
J AJ )v = A∗
J g.
(39)
To estimate the convergence rate of the Krylov iterative method, it is important for us to analyse
the conditioning of the above linear system, as is done in the next theorem.
Theorem 7. Let B ∈Rm×p with p < m. Consider linear system Gv = B∗g, where G = B∗B +ρIp
and g ∈Rm. Then the eﬀective condition number for solving the system by the MINRES (minimum
residual) method with zero initial point is given by
κ = ω2
max + ρ
ω2
min + ρ
where ωmax is the largest singular value and ωmin > 0 is the smallest positive singular value of B,
respectively.
19


## Page 20


Proof. Consider the following full SVD of B:
B = UΣV T = [U1, U2]
 ˆΣ
0
0
0
  V T
1
V T
2

,
where ˆΣ is the diagonal matrix consisting of the positive singular values of B. Let P0
k be the set of
polynomials pk with degree at most k and pk(0) = 1. Then for pk ∈P0
k, we have that
pk(G)B∗g
=
V pk(ΣT Σ + ρI)ΣT U T g = [V1, V2]

pk(ˆΣ2 + ρI)ˆΣ
0
0
0
  U T
1 g
U T
2 g

=
V1pk(ˆΣ2 + ρI)ˆΣU T
1 g.
Since the k-th iteration of the MINRES method computes an approximate solution xk such that
its residual ξ = ¯pk(G)B∗g satisﬁes the condition that
∥ξ∥= ∥¯pk(G)B∗g∥=
min
pk∈P0
k
∥pk(G)B∗g∥≤∥ˆΣU T
1 g∥min
pk∈P0
k
∥pk(z)∥[ω2
min+ρ, ω2max+ρ],
thus we see that the convergence rate of the MINRES method is determined by the best approxi-
mation of the zero function by the polynomials in P 0
k over the interval [ω2
min + ρ, ω2
max + ρ]. More
speciﬁcally, by [42, Theorem 6.4], we have that minpk∈P0
k ∥pk(z)∥[ω2
min+ρ, ω2max+ρ] ≤2κ−k. Hence the
convergence rate of the MINRES method is determined by κ.
After (39) is solved via the MINRES method, one can compute the residual vector associated
with system (38) without much diﬃculty. Indeed, let the computed solution of (38) be given as
follows:
c
∆y = τ −1σ(g −AJ v)
where Gv = A∗
J g −ξ with ξ being the residual vector obtained from the MINRES iteration. Now
the residual vector associated with (38) is given by
η
:=
g −H c
∆y = g −τ −1σHg + τ −1σHAJ G−1(A∗
J g −ξ)
=
g −τ −1σH(g −PJ g) −τ −1σHAJ G−1ξ
=
−τ −1σHAJ G−1ξ = −ρ−1AJ ξ,
where the last equation follows directly from the fact that HAJ = σAJ G. Based on the computed
η, one can check the termination condition for solving the linear system in (30).
Now, we are ready to bound the condition numbers of the Newton linear systems involved in
Snipal. As can be observed from the above discussions, for both cases (a) and (b), the eﬀective
condition number of the linear system involved is upper bounded by
κ ≤1 + ω2
max
ρ
,
where ωmax is the largest singular value of AJ and ρ = τσ−2. Since AJ is a sub-matrix of A, it
holds that ωmax ≤∥A∥2. Hence, for any linear system involved in the k-th iteration of Snipal, we
can provide an upper bound for the condition number as follows:
κ ≤1 + ∥A∥2
2σ2
k
τk
.
(40)
20


## Page 21


From our assumptions on Snipal, we note that σk ≤σ∞and τk ≥τ∞> 0 for all k ≥0. Hence, for
all the linear systems involved in Snipal, there exists an uniform upper bound for the corresponding
condition number:
κ ≤1 + ∥A∥2
2σ2
∞
τ∞
.
As long as σ∞< +∞, we have shown that all these linear systems have bounded condition numbers.
This diﬀers signiﬁcantly from the setting in interior-point based algorithms where the condition
numbers of the corresponding normal equations are asymptotically unbounded. The competitive
advantage of Snipal can be partially explained from the above observation. Meanwhile, in the
k-th iteration of Sinpal, to maintain a small condition number based on (40), one should choose
small σk but large τk. However, the convergence rate of Snipal developed in Theorem 2 requires
the opposite choice, i.e., large σk and τk should be moderate. The preceding discussion thus reveals
the trade-oﬀbetween the convergence rate of the ALM and the condition numbers of the Newton
linear systems. Clearly, in the implementation of Snipal, the parameters {σk} and {τk} should be
chosen to balance the progress of the outer and inner algorithms, i.e., the ALM and the semismooth
Newton method.
5
Warm-start algorithm for Snipal
As is mentioned in the introduction, to achieve high performance, it is desirable to use a simple
ﬁrst-order algorithm to warm start Snipal so that its local linear convergence behavior can be
observed earlier. For this purpose, we present an ADMM algorithm for solving (D). We note that
a similar strategy has also been employed for solving large scale semideﬁnite programming and
quadratic semideﬁnite programming problems [47, 25].
We begin by rewriting (D) into the following equivalent form:
min

δ∗
K(−z) −bT y | z + A∗y = c
	
.
(41)
Given σ > 0, the augmented Lagrangian function associated with (41) can be written as
Lσ(z, y; x) = δ∗
K(−z) −bT y + ⟨x, z + A∗y −c⟩+ σ
2 ∥z + A∗y −c∥2
for all (x, y, z) ∈Rn × Rm × Rn. The template of the classical ADMM for solving (41) is given as
follows.
Algorithm 3 ADMM: An ADMM method for solving (41)
Given (x0, y0) ∈Rn × Rm and γ > 0, perform the following steps for k = 1, . . .,
Step 1. Compute
zk+1 = argmin Lσ(z, yk; xk) = 1
σ

ΠK(xk + σ(A∗yk −c)) −(xk + σ(A∗yk −c))

.
(42)
Step 2. Compute
yk+1 = argmin Lσ(zk+1, y; xk) = (AA∗)−1
b/σ −A(xk/σ + zk+1 −c)

.
(43)
Step 3. Compute xk+1 = xk + γσ(zk+1 + A∗yk+1 −c).
21


## Page 22


The convergence of the above classical ADMM for solving the two-block optimization problem
(41) with the steplength γ ∈(0, (1 +
√
5)/2) can be readily obtained from the vast literature on
ADMM. Here, we adopt a newly developed result from [10] stating that the above ADMM is in
fact an inexact proximal ALM. This new interpretation allows us to choose the steplength γ in the
larger interval (0, 2) which usually leads a better numerical performance when γ is chosen to be
1.9 instead of 1.618. We summarize the convergence results in the following theorem. The detailed
proof can be found in [10].
Theorem 8. Suppose that Assumption 1 holds and γ ∈(0, 2). Let {(xk, yk, zk)} be the sequence
generated by Algorithm ADMM. Then, {xk} converges to an optimal solution of (P) and {(yk, zk)}
converges to an optimal solution of (41), respectively.
Remark 5. In the above algorithm, one can also handle (43) by adding an appropriate proximal
term or by using an iterative method to solve the corresponding linear system. The convergence of
the resulting proximal or inexact ADMM with steplength γ ∈(0, 2) has also been discussed in [10].
For simplicity, we only discussed the exact version here.
6
Numerical experiments
In this section, we evaluate the performance of Snipal against the powerful commercial solver
Gurobi (version 8.0.1) on various LP data sets. Our goal is to compare the performance of our
algorithm against the barrier method implemented in Gurobi in terms of its speed and ability to
solve the tested instances to the relatively high accuracy of 10−6 or 10−8 in the relative KKT
residual. That is, for a given computed solution (x, y, z), we stop the algorithm when
η = max
n∥b −Ax∥
1 + ∥b∥, ∥AT y + z −c∥
1 + ∥c∥
, ∥x −ΠK(x −z)∥
1 + ∥x∥+ ∥z∥
o
≤Tol
(44)
where Tol is a given accuracy tolerance. We should note that it is possible to solve an LP by
using the primal or dual simplex methods in Gurobi, and those methods could sometimes be more
eﬃcient than the barrier method in solving large scale LPs. However, as our Snipal algorithm is
akin to a barrier method, in that each of its semismooth Newton iteration also requires the solution
of a linear system having the form of a normal equation just as in the case of the barrier method,
we thus restrict the comparison of our algorithm only to the barrier method in Gurobi. To purely
use the barrier method in Gurobi, we also turn oﬀits crossover capability from the barrier method
to simplex methods. We should note that sometimes the presolve phrase in Gurobi is too time
consuming and does not lead to any reduction in the problem size. In that case, we turn oﬀthe
presolve phase in Gurobi to get the actual performance of its barrier method.
All the numerical experiments in this paper are run in Matlab on a Dell Laptop with Intel(R)
Core i7-6820HQ CPU @2.70GHz and 16GB of RAM. As Gurobi is extremely powerful in exploiting
multi-thread computing, we set the number of threads allowed for Gurobi to be two so that its
overall CPU utilization rate is roughly the same as that observed for running Snipal in Matlab
when setting the maximum number of computational threads to be two.
6.1
Randomly generated sparse LP in [30]
Here we test large synthetic LP problems generated as in [30].
In particular, the matrix A is
generated as follows:
22


## Page 23


rng(‘default’);
A = sprand(m,n,d);
A = 100*(A-0.5*spones(A));
In this case, we turn oﬀthe presolve phase in Gurobi as this phase is too time consuming for these
randomly generated problems and it also does not lead to any reduction in the problem sizes. As
we can observe from Table 1, Snipal is able to outperform Gurobi by a factor of about 1.5 −2.3
times in computational time in most cases.
Note that for the column “iter (itssn)” in Table 1, we report the number of Snipal iterations
and the total number of semismooth Newton linear systems solved in Algorithm 2. For the columns
“time (RAM)” and “Gurobi time (RAM)”, we report the wall-clock time and the memory consumed
by Snipal and Gurobi, respectively.
Table 1: Numerical results for random sparse LPs with Tol = 10−8.
m
n
d
Snipal
iter (itssn)
Snipal
time (s) (RAM)
Gurobi
barrier iter
Gurobi
time (s) (RAM)
2e3
1e5
0.025
4 (18)
3.5 (0.8GB)
7
5.2 (1.0GB)
0.050
4 (18)
6.8 (0.8GB)
7
10.5 (1.3GB)
5e3
1e5
0.025
4 (15)
15.0 (1.5GB)
7
22.4 (1.7GB)
0.050
4 (15)
31.1 (1.8GB)
7
46.1 (2.6GB)
10e3
1e5
0.025
5 (24)
50.6 (3.2GB)
8
96.6 (3.2GB)
0.050
5 (24)
101.5 (5.3GB)
8
181.6 (6.0GB)
1e3
1e6
0.025
5 (30)
10.3 (2.0GB)
7
22.2 (4.1GB)
0.050
5 (29)
18.9 (3.2GB)
7
40.0 (6.0GB)
2e3
1e6
0.025
6 (32)
27.2 (3.2GB)
7
52.2 (6.1GB)
0.050
5 (28)
53.1 (5.2GB)
6
92.7 (9.6GB)
5e3
1e6
0.025
5 (26)
91.8 (4.5GB)
7
184.1 (10.0GB)
10e3
1e6
0.010
7 (40)
84.6 (4.3GB)
7
194.4 (8.5GB)
6.2
Transportation problem
In this problem, s suppliers of a1, . . . , as units of a certain goods must be transported to meet the
demands b1, . . . , bt of t customers. Let the cost of transporting one unit of goods from supplier i to
customer j be cij. Then, the objective is to ﬁnd a transportation plan denoted by xij to solve the
following LP:
min
Ps
i=1
Pt
j=1 cijxij
s.t.
Pt
j=1 xij = ai,
i ∈[s]
Ps
i=1 xij = bj,
j ∈[t]
xij ≥0, ∀i ∈[s], j ∈[t].
In the above problem, we assume that Ps
i=1 ai = Pt
j=1 bj. Note that this assumption is needed for
the LP to be feasible. We can write the transportation LP compactly as follows:
min
n
⟨C, X⟩| A(X) = [a; b], X ≥0
o
,
(45)
where
A(X) =
"
ˆeT ⊗Is
It ⊗eT
#
vec(X),
23


## Page 24


e ∈Rs and ˆe ∈Rt are vector of all ones, and vec(X) is the st-dimensional column vector obtained
from X by concatenating its columns sequentially.
In Table 2, we report the results for some randomly generated transportation instances. For
each pair of given s, t, we generate a random transportation instance as follows:
rng(‘default’); M=abs(rand(s,t)); a=sum(M,2); b=sum(M,1)’; C=ceil(100*rand(s,t));
Note that
we turn oﬀthe presolve phase in Gurobi as this phase is too time consuming (about
20–30% of the total time) and there is no beneﬁt in cutting down the computation time per iteration.
We can observe that for this class of problems, Snipal is able to outperform the highly powerful
barrier method in Gurobi by a factor of about 1–3 times in terms of computation times. Moreover,
our solver Snipal consumed less peak memory than Gurobi. For the largest instance where the
primal LP has 12,000 linear constraints and 27 millions variables, our solver is at least ﬁve times
faster than the barrier method in Guorbi, and it only needs 5.4GB of RAM whereas Gurobi required
12.8GB.
Table 2: Numerical results for transportation LPs with Tol = 10−8.
s
t
Snipal
iter (itssn)
Snipal
time (s) (RAM)
Gurobi
barrier iter
Gurobi
time (s) (RAM)
2000
3000
5 (17)
18.3 (1.8GB)
8
20.7 (4.8GB)
2000
4000
5 (18)
22.0 (2.1GB)
8
32.6 (6.5GB)
2000
6000
5 (18)
34.2 (3.4GB)
8
59.5 (8.9GB)
3000
4500
5 (17)
40.4 (3.5GB)
8
61.6 (9.2GB)
3000
6000
5 (18)
53.4 (4.0GB)
8
93.9 (10.3GB)
3000
9000
5 (20)
65.1 (5.4GB)
7
191.1 (12.8GB)
6.3
Generalized transportation problem
The Generalized Transportation Problem (GTP) was introduced by Fergusan and Dantzig [18] in
their study of an aircraft routing problem. Eisemann and Lourie [20] applied it to the machine
loading problem. In that problem, there are m types of machines which can produce n types of
products such that machine i would take hij hours at the cost of cij to produce one unit of product
j. It is assumed that machine i is available for at most ai hours, and the demand for product j is
bj. The problem is to determine xij, the amount of product j to be produced on machine i during
the planning period so that the total cost is minimized, namely,
min
Ps
i=1
Pt
j=1 cijxij
s.t.
Pt
j=1 hijxij = ai,
i ∈[s]
Ps
i=1 xij = bj,
j ∈[t]
xij ≥0, ∀i ∈[s], j ∈[t].
In addition to assuming, similar to the transportation problem in the previous subsection, that
Ps
i=1 ai = Pt
j=1 bj, we also apply the normalization Ps
i=1
Pt
j=1 hij = st.
Table 3 presents the results for randomly generated generalized transportation LPs where a, b, c
are generated as in the last subsection. The weight matrix H = (hij) is generated by setting H =
rand(s,t); H = (s*t/sum(sum(H)))*H. We can observe that Snipal can be up to 3 times faster
than the barrier method in Gurobi when the problems are large.
24


## Page 25


Table 3: Numerical results for generalized transportation LPs with Tol = 10−8.
s
t
Snipal
iter (itssn)
Snipal
time (s) (RAM)
Gurobi
barrier iter
Gurobi
time (s) (RAM)
2000
3000
5 (19)
22.4 (1.6GB)
7
19.4 (2.9GB)
2000
4000
5 (18)
27.1 (2.5GB)
8
32.7 (5.5GB)
2000
6000
5 (18)
40.6 (3.6GB)
8
61.0 (8.0GB)
3000
4500
5 (18)
48.4 (3.4GB)
8
59.7 (6.0GB)
3000
6000
5 (18)
63.5 (4.0GB)
8
90.0 (12.9GB)
3000
9000
5 (19)
85.3 (5.8GB)
7
258.0 (13.1GB)
6.4
Covering and packing LPs
Given a nonnegative matrix A ∈Rm×n and cost vector c ∈Rn
+, the covering and packing LPs are
deﬁned by
(Covering)
min
n
⟨c, x⟩| Ax ≥e, x ≥0
o
(Packing)
min
n
⟨−c, x⟩| Ax ≤e, x ≥0
o
.
It is easy to see that by adding a slack variable, the above problems can be converted into the
standard form expressed in (P).
In our numerical experiments in Table 4, we generate A and c randomly as follows:
rng(‘default’); c = rand(n,1); A = sprand(m,n,den); A = round(A);
Table 4 presents the numerical performance of Snipal versus Gurobi on some randomly generated
large scale covering and packing LPs. As we can observe, Snipal is competitive against the barrier
method in Gurobi for solving these large scale LPs, and the former can be up to 2.9 times faster
than the barrier method in Gurobi.
Table 4: Numerical results for covering and packing LPs with Tol = 10−8.
Type
m
n
den
Snipal
iter (itssn)
Snipal
time (s)
Gurobi
barrier iter
Gurobi
time (s)
C
1e3
5e5
0.2
22 (148)
49.8
14
62.1
C
2e3
5e5
0.1
25 (151)
103.3
16
90.6
C
2e3
1e6
0.05
24 (160)
90.4
17
102.0
C
3e3
5e6
0.02
24 (148)
190.5
22
560.5
P
1e3
5e5
0.2
28 (160)
49.3
12
53.3
P
2e3
5e5
0.1
29 (160)
97.0
12
68.2
P
2e3
1e6
0.05
30 (173)
75.1
15
91.4
P
3e3
5e6
0.02
26 (228)
259.8
20
500.2
6.5
LPs arising from correlation clustering
A correlation clustering problem [1] is deﬁned over an undirected graph G = (V, E) with p nodes
and edge weights ce ∈R (for each e ∈E) that is interpreted as a conﬁdence measure of the similarity
or dissimilarity of the edge’s end nodes. In general, for e = (u, v) ∈E, ce is given a negative value
if u, v are dissimilar, and a positive value if u, v are similar. For the goal of ﬁnding a clustering that
25


## Page 26


minimizes the disagreements, the problem can be formulated as an integer programming problem as
follows. Suppose that we are given a clustering S = {S1, . . . , SN} where each St ⊂V , t = 1, . . . , N,
denotes a cluster. For each edge e = (u, v) ∈E, set ye = 0 if u, v ∈St for some t, and set ye = 1
otherwise. Observe that 1 −ye is 1 if u, v are in the same cluster, and 0 if u, v are in diﬀerent
clusters. Now deﬁne the constants
me = | min{0, ce}|,
pe = max{0, ce}.
Then the cost of disagreements for the clustering S is given by P
e∈E me(1 −ye) + P
e∈E peye.
A version of the correlation clustering problem is to ﬁnd a valid assignment (i.e., it satisﬁes
the triangle inequalities) of ye for all e ∈E to minimize the disagreements’ cost. We consider the
relaxation of this integer program to get the following LP:
min
P
(i,j)∈E mij(1 −yij) + P
(i,j)∈E pijyij
s.t.
−yij ≤0, yij ≤1
∀(i, j) ∈E
−yij −yjk + yik ≤0
∀1 ≤i < j < k ≤n, such that (i, j), (j, k), (i, k) ∈E.
In the above formulation, we assumed that the edge set E is a subset of {(i, j) | 1 ≤i < j ≤p}.
Let M be the number of all possible triangles in E. Deﬁne T : R|E| →RM to be the linear map
that maps y to all the M terms −yij −yjk + yik in the triangle inequalities. We can express the
above LP in the dual form as follows:
⟨m, 1⟩−max
n
⟨m −p, y⟩|


−I
I
T

y ≤


0
1
0


o
,
and the corresponding primal LP is given by
⟨m, 1⟩−min
n
⟨[0; 1; 0], x⟩| [−I, I, T ∗]x = m −p, x ∈R2|E|+M
+
o
.
(46)
Observe that the primal LP has |E| equality constraints and a large number of 2|E| + M variables.
In Table 5, we evaluate the performance of our algorithm on correlation clustering LPs on data
that were used in [45]. One can observe that for the LP problem (46), our solver Snipal is much
more eﬃcient than the barrier method in Gurobi, and the former can be up to 117 times faster for the
largest problem. The main reason why Snipal is able to outperform the barrier method in Gurobi
lies in the fact that the former is able to make use of an iterative solver to solve the moderately well
conditioned linear system in (37) rather eﬃciently in each semismooth Newton iteration, whereas
for the latter, it has to rely on sparse Cholesky factorization to solve the associated normal equation
and for this class of problems, computing the sparse Cholesky factorization is expensive. Under the
column “itminres” in Table 5, we report the average number of MINRES iterations needed to solve
a single linear system of the form in (37). As one can observe, the average number of MINRES
iterations is small compared to the dimension of the linear system for all the tested instances.
6.6
LPs from MIPLIB2010
In this subsection, we evaluate the potential of Snipal as a tool for solving general LPs with
the characteristic that the number of linear constraints are much smaller than the dimension of
the variables. For this purpose, we consider the root-node LP relaxations of some mixed-integer
programming problems in the library MIPLIB2010 [31].
26


## Page 27


Table 5: Numerical results for correlation clustering LPs with Tol = 10−8.
Data
p
|E|
2|E| + M
Snipal
iter (itssn | itminres)
Snipal
time (s)
Gurobi
barrier iter
Gurobi
time (s)
planted(5)
200
19900
1353200
5 (70 | 110.0)
38.1
37
690.9
planted(10)
200
19900
1353200
6 (91 | 146.5)
36.8
49
1146.6
planted(5)
300
44850
4544800
5 (86 | 109.2)
170.2
37
8350.7
planted(10)
300
44850
4544800
7 (127 | 186.3)
158.0
82
18615.8
stocks
200
19900
1353200
5 (57 | 147.7)
57.8
53
1009.2
stocks
300
44850
4544800
5 (75 | 191.1)
276.9
60
13797.0
Table 6 reports the performance of Snipal against the barrier method in Gurobi for solving the
LPs from the two sources mentioned in the last paragraph to the accuracy level to 10−6. Note that
we ﬁrst use Gurobi’s presolve function to pre-processed the LPs. Then the pre-processed instances
are used for comparison with Gurobi’s presolve capability turned oﬀ.
As one can observe, the
barrier method in Gurobi performed much better than Snipal, with the former typically requiring
less than 50 iterations to solve the LPs while the latter typically needs hundreds of semismooth
Newton iterations except for a few problems such as datt256, neos-xxxx, etc. Overall, the barrier
method in Gurobi can be 10-50 times faster than Snipal on many of the tested instances, with the
exception of ns2137859.
The large number of semismooth Newton iterations needed by Snipal to solve the LPs can be
attributed to the fact that for most of the LP instances tested here, the local superlinear convergent
property of the semismooth Newton method in solving the subproblems of the SPALM generally
does not kick-in before a large number of initial iterations has been taken. From this limited set of
tested LPs, we may conclude that substantial numerical work must be done to improve the practical
performance of Snipal before it is competitive enough to solve general large scale sparse LPs.
Table 6: Numerical results for some LPs from MIPLIB2010 with Tol =
10−6.
problem
m
n
it (itssn)
time
Gurobi
barrier iter
Gurobi
time
app1-2
26850
107132
33 (878)
54.33
16
0.73
bab3
22449
411334
40 (789)
139.43
37
6.41
bley-xl1
746
7361
7 (114)
1.06
21
0.21
circ10-3
2700
46130
7 (17)
4.98
10
0.80
co-100
1293
22823
39 (634)
4.09
23
0.64
core2536-691
1895
12991
11 (325)
15.35
25
0.83
core4872-1529
3982
18965
16 (285)
34.37
22
1.52
datt256
9809
193639
3 (37)
31.24
5
1.69
dc1l
1071
34931
16 (209)
8.86
39
1.06
ds-big
1039
173026
27 (623)
74.91
25
5.37
eilA101.2
100
65832
14 (88)
7.71
21
0.96
ivu06-big
1177
2197774
19 (236)
87.28
27
34.97
ivu52
2116
135634
31 (559)
47.19
23
3.22
lectsched-1-obj
9246
34592
28 (331)
2.46
12
0.32
lectsched-1
6731
27042
7 (15)
0.26
5
0.15
lectsched-4-obj
2592
9716
22 (94)
0.76
7
0.06
leo2
539
11456
24 (106)
0.68
22
0.16
27


## Page 28


problem
m
n
it (itssn)
time
Gurobi
barrier iter
Gurobi
time
mspp16
4065
532749
26 (54)
68.67
14
59.88
n3div36
4450
25052
20 (75)
0.72
27
0.25
n3seq24
5950
125746
14 (71)
20.25
15
6.42
n15-3
29234
153400
22 (475)
63.86
30
4.30
neos13
1826
22930
30 (154)
9.83
22
0.23
neos-476283
9227
20643
22 (495)
174.60
14
10.58
neos-506428
40806
200653
4 (8)
7.86
16
0.96
neos-631710
3072
169825
4 (9)
13.90
5
0.54
neos-885524
60
21317
4 (8)
0.84
12
0.11
neos-932816
2568
8932
7 (17)
2.88
10
0.14
neos-941313
12919
129180
6 (17)
5.71
10
0.42
neos-1429212
8773
42620
37 (541)
118.34
28
6.91
netdiversion
99482
208447
33 (324)
173.07
15
5.38
ns1111636
12992
85327
4 (38)
7.85
16
0.79
ns1116954
11928
141529
2 (6)
125.54
11
23.86
ns1688926
16489
41170
26 (160)
150.80
88
12.68
ns1904248
38184
222489
3 (6)
6.00
6
0.96
ns2118727
7017
15853
30 (1079)
20.63
24
0.41
ns2124243
19663
53716
22 (122)
13.08
14
0.36
ns2137859
16357
49795
11 (22)
6.20
50
61.53
opm2-z12-s7
10328
145436
13 (43)
19.13
17
16.19
opm2-z12-s14
10323
145261
12 (36)
19.46
16
15.39
pb-simp-nonunif
11706
146052
2 (4)
2.08
10
0.68
rail507
449
23161
14 (240)
1.95
23
0.25
rocII-7-11
5534
25590
20 (73)
2.26
17
0.35
rocII-9-11
8176
37159
22 (106)
3.85
17
0.51
rvb-sub
217
33200
24 (157)
1.67
11
0.56
shipsched
5165
22806
16 (35)
0.73
10
0.24
sp97ar
1627
15686
26 (264)
2.63
26
0.33
sp98ic
806
11697
27 (155)
1.63
25
0.25
stp3d
95279
205516
71 (2892)
228.56
22
11.75
sts729
729
89910
2 (4)
0.72
3
0.26
t1717
551
16428
22 (141)
1.59
13
0.22
tanglegram1
32705
130562
2 (4)
0.90
5
0.30
van
7360
36736
4 (8)
7.39
15
3.63
vpphard
9621
22841
3 (6)
2.90
9
0.90
vpphard2
13085
28311
4 (6)
2.77
7
0.64
wnq-n100-mw99-14
594
10594
24 (119)
0.73
15
0.22
7
Conclusion
In this paper, we proposed a method called Snipal targeted at solving large scale LP problems
where the dimension n of the decision variables is much larger than the number m of equality con-
straints. Snipal is an inexact proximal augmented Lagrangian method where the inner subproblems
are solved via an eﬃcient semismooth Newton method. By connecting the inexact proximal aug-
mented Lagrangian method with the preconditioned proximal point algorithm, we are able to show
28


## Page 29


the global and local asymptotic superlinear convergence of Snipal. Our analysis also reveals that
Snipal can enjoy a certain ﬁnite termination property. To achieve high performance, we further
study various eﬃcient approaches for solving the large linear systems in the semismooth Newton
method. Our ﬁndings indicate that the linear systems involved in Snipal have uniformly bounded
condition numbers, in contrast to those involved in an interior point algorithm which has unbounded
condition numbers. Building upon all the aforementioned desirable properties, our algorithm Sni-
pal has demonstrated a clear computational advantage in solving some classes of large-scale LP
problems in the numerical experiments when tested against the barrier method in the powerful
commercial LP solver Gurobi. However, when tested on some large sparse LPs available in the
public domain, our Snipal is not yet competitive against the barrier method in Gurobi on most
of the test instances. Thus much work remains to be done to improve the practical eﬃciency of
Snipal and we leave it as a future research project.
Appendix
Here we show that the dual of (18) with τ = 0 is given by (33). Consider the augmented Lagrangian
function
inf
y Lσk(y; xk)
=
inf
y max
x

l(y; x) −1
2σ ∥x −xk∥2

= max
x

−1
2σ ∥x −xk∥2 + inf
y l(y; x)

=
max
x
n
−δK(x) −⟨c, x⟩−1
2σ ∥x −xk∥2 | Ax = b
o
,
where l(y; x) = −bT y −⟨x, c −A∗y⟩−δK(x) for any (y, x) ∈Rm × Rn. The interchange of infy and
maxx follows from the growth properties in x of the “minimaximand” in question [38, Theorem
37.3]. See also the proof of [40, Proposition 6].
References
[1] N. Bansal, A. Blum, and S. Chawla, Correlation clustering, IEEE Symposium on
Foundations of Computer Science, 2002.
[2] H. H. Bauschke and P. L. Combettes, Convex Analysis and Monotone Operator
Theory in Hilbert Spaces, Springer, 2011.
[3] L. Bergamaschi, J. Gondzio, and G. Zilli, Preconditioning indeﬁnite systems in
interior point methods for optimization, Computational Optimization and Applications,
28 (2004), pp. 149–171.
[4] J. F. Bonnans, J. Ch. Gilbert, C. Lemar´echal, and C. A. Sagastiz´abal, A family
of variable metric proximal methods, Mathematical Programming, 68 (1995), pp. 15–47.
[5] J. V. Burke and M. Qian, A variable metric proximal point algorithm for monotone
operators, SIAM Journal on Control and Optimization, 37 (1999), pp. 353–375.
[6] J. V. Burke and M. Qian, On the local super-linear convergence of a matrix secant
implementation of the variable metric proximal point algorithm for monotone operators, in
Reformulation - Nonsmooth, Piecewise Smooth, Semismooth and Smoothing Methods, M.
Fukushima and L. Qi, eds., Kluwer Academic Publishers, Norwell, MA, 1999, pp. 317–334.
29


## Page 30


[7] J. V. Burke and M. Qian, On the superlinear convergence of the variable metric proxi-
mal point algorithm using Broyden and BFGS matrix secant updating, Mathematical Pro-
gramming, 88 (2000), pp. 157–181.
[8] J. S. Chai and K.-C. Toh, Preconditioning and iterative solution of symmetric indeﬁnite
linear systems arising from interior point methods for linear programming, Computational
Optimization and Applications, 36 (2007), pp. 221–247.
[9] J. Chen and S. Burer, A ﬁrst-order smoothing technique for a class of large-scale linear
programs, SIAM Journal on Optimization, 24 (2014), pp. 598–620.
[10] L. Chen, X. D. Li, D. F. Sun and K.-C. Toh, On the equivalence of inexact proximal
ALM and ADMM for a class of convex composite programming, Mathematical Program-
ming, (2020), DOI:10.1007/s10107-019-01423-x.
[11] X. Chen and M. Fukushima, Proximal quasi-Newton methods for nondiﬀerentiable con-
vex optimization, Mathematical Programming, 85 (1999), pp. 313–334.
[12] F. Clarke, Optimization and Nonsmooth Analysis, John Wiley and Sons, New York,
1983.
[13] Y. Cui, K. Morikuni, T. Tsuchiya, and K. Hayami, Implementation of interior-point
methods for LP based on Krylov subspace iterative solvers with inner-iteration precondi-
tioning, Computational Optimization and Applications, 74 (2019), pp. 143–176.
[14] R. Durier, On locally polyhedral convex functions, in Trends in Mathematical Optimiza-
tion (Irsee, 1986), Internat. Schriftenreihe Numer. Math., 84, Birkh¨auser, Basel, 1988, pp.
55–66.
[15] J. Eckstein, Nonlinear proximal point algorithms using Bregman functions, with applica-
tions to convex programming, Mathematics of Operations Research, 18 (1993), pp. 202–226.
[16] J. Eckstein and D. P. Bertsekas, On the Douglas-Rachford splitting method and the
proximal point algorithm for maximal monotone operators, Mathematical Programming,
55 (1992), pp. 293–318.
[17] Yu. G. Evtushenko, A. I. Golikov, and N. Mollaverdy, Augmented Lagrangian
method for large-scale linear programming problems, Optimization Methods and Software,
20 (2005), pp. 515–524.
[18] A. R. Fergusan and G. B. Dantzig, The allocation of aircrafts to routes - an example
of linear programming under uncertain demand, Management Science, 3 (1956).
[19] A. Fischer and C. Kanzow, On ﬁnite termination of an iterative method for linear
complementarity problems, Mathematical Programming, 74 (1996), pp. 279–292.
[20] K. Eisemann and J.R. Lourie, The machine loading problem, IBM 704 Program, BML-
1, IBM Application Library, New York, 1959.
[21] G. Al-Jeiroudi, J. Gondzio and J.A.J. Hall, Preconditioning indeﬁnite systems in
interior point methods for large scale linear optimization, Optimization Methods and Soft-
ware, 23 (2008), pp. 345–363.
30


## Page 31


[22] J.-B. Hiriart-Urruty, J.-J. Strodiot, and V. H. Nguyen, Generalized Hessian
matrix and second-order optimality conditions for problems with C1,1 data, Applied Math-
ematics and Optimization, 11 (1984), pp. 43–56.
[23] C. Kanzow, H. Qi, and L. Qi, On the minimum norm solution of linear programs,
Journal of Optimization Theory and Applications, 116 (2003), pp. 333–345.
[24] D. Klatte and B. Kummer, Nonsmooth Equations in Optimization, Regularity, Calcu-
lus, Methods and Applications, Kluwer Academic Publishers, Dordrecht, the Netherlands,
2002.
[25] X. D. Li, D. F. Sun, and K.-C. Toh, QSDPNAL: A two-phase augmented Lagrangian
method for convex quadratic semideﬁnite programming, Mathematical Programming Com-
putation, 10 (2018), pp. 703–743.
[26] X. D. Li, D. F. Sun, and K.-C. Toh, On the eﬃcient computation of a generalized Ja-
cobian of the projector over the Birkhoﬀpolytope, Mathematical Programming, 179 (2020),
pp. 419–446.
[27] F. J. Luque, Asymptotic convergence analysis of the proximal point algorithm, SIAM
Journal on Control and Optimization, 22 (1984), pp. 277–293.
[28] R. De Leone and O. L. Mangasarian, Serial and parallel solution of large scale linear
programs by augmented Lagrangian successive overrelaxation, in A. Kurzhanski, K. Neu-
mann, and D. Pallaschke, editors, Optimization, Parallel Processing and Applications, pp.
103–124, Berlin, 1988. Springer-Verlag.
[29] O. L. Mangasarian and R. R. Meyer, Nonlinear perturbation of linear programs,
SIAM J. Control and Optimization, 17 (1979), pp. 745–752.
[30] O. L. Mangasarian, A Newton method for linear programming, Journal of Optimization
Theory and Applications, 121 (2004), pp. 1–18.
[31] MIPLIB
–
C
the
Mixed
Integer
Programming
LIBrary,
available
at
http://miplib2010.zib.de/.
[32] A. R. L. Oliveira and D. C. Sorensen, A new class of preconditioners for large-scale
linear systems from interior point methods for linear programming, Linear Algebra and its
Applications, 394, 1-24, 2005.
[33] B. T. Polyak, Introduction to Optimization, Optimization Software Inc., New York, 1987.
[34] L. A. Parente, P. A. Lotito, and M. V. Solodov, A class of inexact variable metric
proximal point algorithms, SIAM Journal on Optimization, 19 (2008), pp. 240–260.
[35] L. Qi and X. Chen, A preconditioning proximal Newton’s method for nondiﬀerentiable
convex optimization, Mathematical Programming, 76 (1995), pp. 411–430.
[36] S. M. Robinson, An implicit-function theorem for generalized variational inequali-
ties, Technical summary report no. 1672, Mathematics Research Center, University of
Wisconsin-Madison, (1976); available from National Technical Information Service under
Accession No. ADA031952.
31


## Page 32


[37] S. M. Robinson, Some continuity properties of polyhedral multifunctions, in Mathematical
Programming at Oberwolfach, Math. Program. Stud., Springer, Berlin, Heidelberg, 1981,
pp. 206–214.
[38] R. T. Rockafellar, Convex Analysis, Princeton University Press, Princeton, N.J., 1970.
[39] R. T. Rockafellar, Monotone operators and the proximal point algorithm, SIAM Jour-
nal on Control and Optimization, 14 (1976), pp. 877–898.
[40] R. T. Rockafellar, Augmented Lagrangians and applications of the proximal point
algorithm in convex programming, Mathematics of operations research, 1 (1976), pp. 97–
116.
[41] R. T. Rockafellar and R. J.-B. Wets, Variational Analysis, Springer, New York,
2009.
[42] Y. Saad, Iterative Methods, PWS Publishing Company, Boston, 1996.
[43] L. Schork and J. Gondzio, Implementation of an Interior Point Method with Basis
Preconditioning, Mathematical Programming Computation, (2020), DOI:10.1007/s12532-
020-00181-8.
[44] D. F. Sun, J. Y. Han, and Y. Zhao, On the ﬁnite termination of the damped-newton
algorithm for the linear complementarity problem, Acta Mathematica Applicatae Sinica, 21
(1998), pp. 148–154.
[45] N. Veldt, A. Wirth, and D. Gleich, Correlation clustering with low-rank matrices,
Proceedings of the 26th International Conference on World Wide Web, 2017, pp. 1025–
1034.
[46] S. J. Wirght, Implementing proximal point methods for linear programming, Journal of
Optimization Theory and Applications, 65 (1990), pp. 531–554.
[47] L. Q. Yang, D. F. Sun, and K.-C. Toh, SDPNAL+: a majorized semismooth Newton-
CG augmented Lagrangian method for semideﬁnite programming with nonnegative con-
straints, Mathematical Programming Computation, 7 (2015), pp. 331–366.
[48] E.-H. Yen, K. Zhong, C.-J. Hsieh, P. K. Ravikumar, and I. S. Dhillon, Sparse linear
programming via primal and dual augmented coordinate descent, Advances in Neural Infor-
mation Processing Systems, 2015, pp. 2368–2376.
[49] X.-Y. Zhao, D. F. Sun, and K.-C. Toh, A Newton-CG augmented Lagrangian method
for semideﬁnite programming, SIAM Journal on Optimization, 20 (2010), pp. 1737–1765.
32

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1903_09546v2_an_asymptotically_superlinearly_convergent_semismooth_newton_augmented_lagrangia
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1903_09546V2_AN_ASYMPTOTICALLY_SUPERLINEARLY_CONVERGENT_SEMISMOOTH_NEWTON_AUGMENTED_LAGRANGIA.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

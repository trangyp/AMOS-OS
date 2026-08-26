---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1603.01786
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1603.01786_Complex-demand_Scheduling_Problem_with_Application_in_Smart_Grid

> Source: 1603.01786_Complex-demand_Scheduling_Problem_with_Application_in_Smart_Grid.pdf

> Pages: 26

---


## Page 1


Complex-demand Scheduling Problem with Application
in Smart Grid1
Majid Khonji, Areg Karapetyan, Khaled Elbassioni
Masdar Institute, Khalifa University of Science and Technology, Abu Dhabi, UAE
Sid Chi-Kin Chau
Research School of Computer Science, Australian National University, Canberra, Australia
Abstract
We consider the problem of scheduling complex-valued demands over a dis-
cretized time horizon. Given a set of users, each user is associated with a set
of demands representing diﬀerent power consumption preferences. A demand is
represented by a complex number, a time interval, and a utility value obtained
if it is satisﬁed. At each time slot, the magnitude of the total selected demands
should not exceed a given generation capacity. This naturally captures the sup-
ply constraints in alternating current (AC) electric systems. In this paper, we
consider maximizing the aggregate user utility subject to power supply limits
over a time horizon. We present approximation algorithms characterized by the
maximum angle φ between any two complex-valued demands. More precisely, a
PTAS is presented for the case φ ∈[0, π
2 ], a bi-criteria FPTAS for φ ∈[0, π-ε] for
any polynomially small ε, assuming the number of time slots in the discretized
time horizon is a constant. Furthermore, if the number of time slots is part of
the input, we present a reduction to the real-valued unsplittable ﬂow problem
on a path with only a constant approximation ratio. Finally, we present a prac-
tical greedy algorithm for the single time slot case with an approximation ratio
of 1
2 cos φ
2 and a running time complexity of only O(N log N), N standing for
the aggregate number of user demands, which can be implemented eﬃciently in
practice.
Keywords:
Algorithms, Scheduling, Smart Grid, Unsplittable Flow, Knapsack
1This paper appears in Theoretical Computer Science (DOI: 10.1016/j.tcs.2018.08.023).
A preliminary version appeared in the 22nd International Conference on Computing and
Combinatorics, COCOON 2016, Ho Chi Minh City, Vietnam, August 2-4, 2016.
Email addresses: majid.khonji@ku.ac.ae (Majid Khonji), areg.karapetyan@ku.ac.ae
(Areg Karapetyan), khaled.elbassioni@ku.ac.ae (Khaled Elbassioni),
sid.chau@anu.edu.au (Sid Chi-Kin Chau)
To appear in Theoretical Computer Science
October 11, 2018
arXiv:1603.01786v3  [cs.DS]  10 Oct 2018


## Page 2


1. Introduction
A key aspect of the emerging smart grid is to modulate users’ electricity
consumption around the available power supply. A microgrid could run short of
power due to emergency conditions, high electricity purchase price in the bulk
market, or volatility of renewable sources. In such cases, consumers’ deferrable
loads, such as dish washers and electric vehicles, can be scheduled according to
the grid’s operational or economic conditions. This, in fact, models the day-
ahead electric market at the distribution network whereby customers provide
their deferrable demand preferences along with the amount they are welling to
pay, and the grid operator decides the best allocation.
Although resource allocation and scheduling mechanisms have been well-
studied in various systems from transportation to communication networks, the
rise of the smart grid presents a new range of algorithmic problems, which are
a departure from these systems. One focal diﬀerence is the presence of periodic
time-varying entities (e.g., current, power, voltage) in AC electric systems, which
are often expressed in terms of non-positive real, or even complex numbers. In
power terminology [1], the real component of the complex number is called the
active power, the imaginary is known as reactive power, and the magnitude as
apparent power. For example, purely resistive appliances have positive active
power and zero reactive power. Appliances and instruments with capacitive or
inductive components have non-zero reactive power, depending on the phase lag
with the input power. Machinery, such as in factories, has large inductors, and
hence has positive power demand. On the contrary, shunt-capacitor equipped
electric vehicle charging stations can generate reactive power.
We consider a variable power generation capacity over a discrete time hori-
zon. Every user of the smart grid is associated with a set of demand preferences,
wherein a demand is represented by a complex-valued number, a time interval at
which it should be supplied, and a utility value obtained if it is satisﬁed. Some
demands are inelastic (i.e., indivisible) in a sense that are either fully satisﬁed,
or completely dropped. At each time slot, the magnitude of the total satisﬁed
demands among all diﬀerent preferences should not exceed the current net gen-
eration capacity of the grid. This captures the variation in supply constraints
over time in alternating current (AC) electric systems, and allows to model the
demand response management in power systems[2].
Conventionally, demands in AC systems are represented by complex numbers
in the ﬁrst and fourth quadrants of the complex plane. We note that our problem
is invariant, when the arguments of all demands are shifted by the same angle.
For convenience, we assume the demands are rotated such that one of them is
aligned along the positive real axis. In realistic setting of power systems, the
active power demand is positive, but the power factor (i.e., the cosine of the
demand’s argument) is bounded from below by a certain threshold, which is
equivalent to restricting the argument of complex-valued demands.
We present approximation algorithms characterized by the maximum angle
φ between any two complex-valued demands. More precisely, we present a PTAS
for the case φ ∈[0, π
2 ], a bi-criteria FPTAS for φ ∈[0, π-ε] for any polynomially
2


## Page 3


small ε, assuming the number of time slots in the discretized time horizon is
constant. Furthermore, if the number of time slots is polynomial (in the input
size), we present a reduction to the unsplittable ﬂow problem on a path that
adds only a constant factor to the approximation ratio. We remark that the
unsplittable ﬂow problem considers only real-valued demands which is indeed
simpler than our setting. Finally, we present a practical greedy algorithm for the
single time slot case with an approximation ratio of 1
2 cos φ
2 and a running time
of O(N log N), where N is the total number of complex-valued user demands,
which can be implemented in real world power systems.
The paper is structured as follows. In Sec. 2, we brieﬂy present the related
works.
In Sec. 3, we provide the problem deﬁnitions and notations needed.
Then we present algorithms for the case of a constant number of time slots
in Sec. 4, namely, a PTAS for φ ∈[0, π
2 ] and an FPTAS for φ ∈[0, π-ε]. In
Sec. 5 we present the reduction to the unsplittable ﬂow problem for the case of
a polynomial number of time slots. The proposed greedy algorithm is provided
in Sec. 6. In Sec. 7, we show how to include elastic demands, i.e., demands
that can be partially satisﬁed, along with the inelastic ones in the problem
formulation. Lastly, Sec. 8 concludes this article.
2. Related work
Several recent studies consider resource allocation with inelastic demands
(that is, when the decision variables are all binary).
For a single time slot
case, the problem studied here resembles the complex-demand knapsack problem
(CKP) [3]. Let φ be the maximum angle between any pair of complex-valued
demands and N be the total number of these demands. A 1
2-approximation was
obtained [3] for the case where 0 ≤φ ≤π
2 . On the other hand, it was shown
in [4] (also [3]) that no fully polynomial-time approximation scheme (FPTAS)
exists. Recently, a polynomial-time approximation scheme (PTAS), and a bi-
criteria FPTAS (allowing constraint violation) for π
2 < φ < π −ε were obtained
in [5, 6]. This essentially closes the approximation gap as it is shown in [7]
that when φ ∈( π
2 , π], there is no α-approximation to CKP for any α with
polynomial number of bits, unless P=NP. Additionally, when ε is arbitrarily
close to zero (i.e., φ →π) there is no (α, β)-approximation in general for any
α, β with polynomial number of bits, unless P=NP. Therefore, the PTAS and
the bi-criteria FPTAS [5] are the best approximation possible for CKP. In [8],
an extension of CKP was provided to handle a constant number of quadratic
(and linear) constraints. A fast greedy algorithm was given in [9] for solving
CKP with a constant approximation ratio that runs in O(N log N) time. A
recent work [10] extends the greedy algorithm to solve the optimal power ﬂow
problem (OPF) with inelastic demands, a generalization of CKP to a networked
setting including voltage constraints.
When the demands are real-valued, the problem under study (considering
multiple time slots) is related to the unsplittable ﬂow problem on a path (UFP).
In UFP, each demand is associated with a unique path from a source to a
sink. UFP is strongly NP-hard [11]. A Quasi-PTAS was obtained by Bansal
3


## Page 4


et al. [12].
Anagnostopoulos et al. [13] obtained a 1/(2 + ϵ)-approximation
(where ϵ > 0 is a constant). This matched the previously known approximation
under the no bottleneck assumption (NBA) [14], which is the case when the
largest demand is at most the smallest capacity. The UFP with bag constraints
(bag-UFP) is the generalization of UFP where each user has a set of demands
among which at most one is selected [15]. This problem is APX-hard even in
the case of unit demands and capacities [16]. Under the NBA assumption, a
1
65-approximation was obtained in
[17], which was later improved by [15] to
1
17. More recently, an O(log N/ log log N)−1-approximation without NBA was
obtained in [18].
A constant factor approximation to bag-UFP remains an
interesting open question.
In this paper, we extend the complex-demand knapsack problem over a dis-
cretized time horizon, where each time slot is associated with a ﬁxed supply
limit. A user provides multiple demand preferences with their respective time
window from which at most one is selected. When the number of time slots is
constant, the problem generalizes CKP (see, [5]) to multiple time slots, and also
extends that of [8] by considering multiple demands per user, thereby adding
n extra constraints, where n is the number of users. Furthermore, for the case
of a polynomial number of time slots, our problem is a generalization of the
unsplittable ﬂow problem on paths to accommodate complex-valued demands.
Finally, we extend the greedy algorithm in [9] (for the single time slot case) to
handle multiple demands per user keeping the same approximation ratio and
running time.
3. Problem Deﬁnitions and Notations
In this section we formally deﬁne the complex-demand scheduling problem.
Throughout this paper, we sometimes denote νR ≜Re(ν) as the real part and
νI ≜Im(ν) as the imaginary part of a given complex number ν ∈C. We use
|ν| to denote the magnitude of ν and arg(ν) to denote the angle ν makes with
the positive real axis. Unless stated otherwise, we denote µt (and sometimes
µ(t) whenever we use subscripts for other purposes) as the t-th component of
the vector µ.
3.1. Complex-demand Scheduling Problem
Consider a discrete time horizon denoted by T ≜{1, ..., m}. At each time
slot t ∈T , the generation capacity of the power grid is denoted by Ct ∈R+.
Denote by N ≜{1, ..., n} the set of all users with cardinality n ≜|N|. Each user
k ∈N declares a set of demand preferences indexed by the set Dk. Each demand
j ∈Dk is deﬁned over a time interval Tj ⊆T , that is, Tj = {t1, t1 + 1, ..., t2}
where t1, t2 ∈T and t1 ≤t2. Demand j is also associated with a set of complex
numbers {sk,j(t)}t∈Tj where sk,j(t) ≜sR
k,j(t) + isI
k,j(t) ∈C is a complex power
demand at time t. A positive utility uk,j is associated with each user demand
(k, j) if satisﬁed.
4


## Page 5


The goal is to ﬁnd a solution of control variables (xk,j)k∈N,j∈Dk ∈{0, 1}
P
i∈N |Di|
that maximizes the total utility of satisﬁed users subject to the generation ca-
pacity over time.
More formally, we deﬁne the complex-demand scheduling
problem over m discrete time slots (m-CSP) by the following integer program-
ming problem.
(m-CSP)
max
X
k∈N
X
j∈Dk
uk,jxk,j
(1)
subject to

X
k∈N
X
j∈Dk:Tj∋t
sk,j(t) · xk,j
 ≤Ct,
for all t ∈T
(2)
X
j∈Dk
xk,j ≤1,
for all k ∈N
(3)
xk,j ∈{0, 1},
for all (k, j) ∈I,
(4)
where I = {(k, j) :
k ∈N
and j ∈Dk}. Cons. (2) captures the capacity
limit, and Cons. (3) forces at most one demand for every user to be selected.
Note that (2) is equivalent to a quadratic constraint

X
k∈N
X
j∈Dk:Tj∋t
Re(sk,j(t)) · xk,j


2
+

X
k∈N
X
j∈Dk:Tj∋t
Im(sk,j(t)) · xk,j


2
≤C2
t , ∀t ∈T .
We consider the following assumption that are mainly needed in Sec. 4.2: for
any user k,
• all demands sk,j(t), for j ∈Dk and t ∈Tj, reside in the same quadrant of
the complex plane.
We also assume without loss of generality that uk,j > 0 and |sk,j(t)| ≤Ct for
all (k, j) ∈I and t ∈T . Problem 1-CSP (i.e., |T | = 1) is called the complex-
demand knapsack, denoted by CKP. Evidently, m-CSP is NP-complete, since
the knapsack problem is its special case when we set all sI
k,j(1) = 0, T = {1}, and
|Dk| = 1. We will write m-CSP[φ1, φ2] for the restriction of problem m-CSP
subject to φ1 ≤maxk∈N arg(sk,j(t)) ≤φ2, where we assume arg(sk,j(t)) ≥0
for all (k, j) ∈I, t ∈Tj.
3.2. Approximation Algorithms
Given a solution x ≜(xk,j)k∈N,j∈Dk, denote the total utility by u(x) ≜
P
k∈N
P
j∈Dk uk,jxk,j. We denote an optimal solution to m-CSP by x∗and
Opt ≜u(x∗). With a slight abuse of notation, for a given subset S ⊆N, we
write u(S) ≜P
k∈S
P
j∈Dk uk,j.
Deﬁnition 1. For α ∈(0, 1] and β ≥1, we deﬁne a bi-criteria (α, β)-approximation
to m-CSP as a solution ˆx = (ˆxk,j)(k,j)∈I ∈{0, 1}|I| satisfying Cons. (3)- (4),
and

X
k∈N
X
j∈Dk:Tj∋t
sk,j(t)ˆxk,j
 ≤β · Ct
for all t ∈T
(5)
such that u(ˆx) ≥αOpt.
5


## Page 6


In the above deﬁnition, α characterizes the approximation ratio between an
approximate solution and the optimal solution, whereas β characterizes the
violation bound of constraints. In particular, polynomial-time approximation
scheme (PTAS) is a (1 −ϵ, 1)- approximation algorithm for any ϵ > 0. The
running time of a PTAS is polynomial in the input size for every ﬁxed ϵ, but
the exponent of the polynomial might depend on 1/ϵ. An even stronger notion
is a fully polynomial-time approximation scheme (FPTAS), which requires the
running time to be polynomial both in input size and 1/ϵ. In this paper, we are
interested in bi-criteria FPTAS, which is a (1, 1 + ϵ)-approximation algorithm
for any ϵ > 0, with the running time to be polynomial in the input size and 1/ϵ.
When β = 1, we sometimes call an (α, β)-approximation an α-approximation.
4. m-CSP with a Constant Number of Time Slots
In this section we assume the number of time slots |T | is a constant. This
assumption is practical in the realistic setting, where users declare their demands
on hourly basis one day ahead in the electricity market. We remark that the
results in this and the next section do not require Tj to be a continuous interval
in T .
4.1. PTAS for m-CSP[0, π
2 ]
Deﬁne a convex relaxation of m-CSP (denoted by rlxCSP), such that
Cons. (4) are replaced by xk,j ∈[0, 1] for all (k, j) ∈I. We deﬁne another con-
vex relaxation that will be used in the PTAS denoted by rlxCSP[S1, S0] which
is equivalent to rlxCSP, subject to partial substitution such that xk,j = 1, for
all (k, j) ∈S1 and xk,j = 0, for all (k, j) ∈S0, where S1, S0 ⊆I such that
S1 ∩S0 = ∅:
(rlxCSP[S1, S0])
max
xk,j∈[0,1]
X
k∈N
X
j∈Dk
uk,jxk,j,
s.t.
(6)
 X
k∈N
X
j∈Dk:t∈Tj
sR
k,j(t) · xk,j
2
+
 X
k∈N
X
j∈Dk:t∈Tj
sI
k,j(t) · xk,j
2
≤C2
t , ∀t ∈T
(7)
X
j∈Dk
xk,j ≤1,
for all k ∈N
(8)
xk,j = 1,
for all (k, j) ∈S1
(9)
xk,j = 0
for all (k, j) ∈S0.
(10)
The above relaxation can be solved approximately in polynomial time us-
ing standard convex programming algorithms (see, e.g., [19]).
In fact, such
algorithms can ﬁnd a feasible solution xcx to the convex relaxation such that
u(xcx) ≥Opt∗−δ, in time polynomial in the input size (including the bit com-
plexity) and log 1
δ , where Opt∗is the optimal objective value of rlxCSP[S1, S0].
Notice that the value of an optimal solution to rlxCSP[S1, S0] problem is no
6


## Page 7


worse than that of m-CSP since the feasibility region of the latter is a subset of
that of the former. This, in turn, implies that Opt∗≥Opt ≥¯u ≜maxk,j uk,j,
and hence setting δ to ϵ
2 · ¯u assures that u(xcx) ≥(1 −ϵ
2) · Opt∗.
We provide a (1 −ϵ, 1)-approximation for m-CSP[0, π
2 ] in Algorithm 1, de-
noted by m-CSP-PTAS. The idea of m-CSP-PTAS is based on that proposed
in [8, 20] with two extensions. First, we consider multiple demands per user.
This in fact adds n extra constraints to that in [8, 20], and thus the round-
ing procedure requires further analysis. The second extension is the addition of
elastic demands F. We remark that [5] considers multiple inelastic demands per
user for the single time slot case (denoted by CKP); however, their algorithm
is based on a completely diﬀerent geometric approach that is more complicated
than that in [8].
Given a feasible solution x∗to rlxCSP[S1, S0], a restricted set of demands
S ⊆I ∪F, and vectors c1, c2 ∈Rm
+, we deﬁne the following relaxation, denoted
by LP[c1, c2, x∗, S]:
(LP[c1, c2, x∗, S])
max
xk,j∈[0,1]
X
k∈N
X
j∈Dk
uk,jxk,j
(11)
s.t
X
k∈N
X
j∈Dk:t∈Tj
sR
k,j(t) · xk,j ≤c1
t,
for all t ∈T
(12)
X
k∈N
X
j∈Dk:t∈Tj
sI
k,j(t) · xk,j ≤c2
t,
for all t ∈T
(13)
X
j∈Dk
xk,j ≤1,
for all k ∈N
(14)
xk,j = x∗
k,j
for all (k, j) ∈S.
(15)
The Algorithm 1 proceeds as follows. We guess S1 ⊆I to be the set of
largest-utility 8m
ϵ
inelastic demands in the optimal solution; this deﬁnes an ex-
cluded set of demands S0 ⊆I \S1 whose utilities exceed one of the utilities in S1
(Step 4). For each such S1 and S0, we solve the convex program rlxCSP[S1, S0]
and obtain a (1 −ϵ
2)-approximation xcx (note that the feasibility of the convex
program is guaranteed by the conditions in Step 3). The real and imaginary
projections over all time slots of solution xcx, denoted by LR ∈Rm
+ and LI ∈Rm
+,
are used to deﬁne the linear program LP[LR, LI, xcx, S1 ∪S0] over the restricted
set of demands S1 ∪S0. We solve the linear program in Step 9, and then round
down the solution corresponding to demands (k, j) ∈I in Step 10. Finally, we
return a solution ˆx that attains maximum utility among all obtained solutions.
Theorem 1. For any ﬁxed ϵ, Algorithm 1 obtains a (1−ϵ, 1)-approximation in
polynomial time.
We remark that a PTAS is the best approximation one can hope for, since
it is shown in [3, 4] that it is NP-Hard to obtain an FPTAS for the single time
slot version (1-CSP[0, π
2 ]).
7


## Page 8


Algorithm 1 m-CSP-PTAS[{uk,j, {sk,j(t)}t∈Tj}k∈N,j∈Dk, (Ct)t∈T , ϵ]
Require: Users’ utilities and demands {uk,j, {sk,j(t)}t∈Tj}k∈N,j∈Dk; capacity
over time Ct; accuracy parameter ϵ
Ensure: (1 −ϵ, 1)-solution ˆx to m-CSP[0, π
2 ]
1: ˆx ←0
2: for each set S1 ⊆I such that |S1| ≤8m
ϵ
do
3:
if

X
(k,j)∈S1:t∈Tj
sk,j(t)
 ≤Ct for all t ∈T and |{j : (k, j) ∈S1}| ≤
1, for all k ∈N then
4:
S0 ←{(k, j) ∈I \ S1 | uk,j > min(k′,j′)∈S1 uk′,j′}
5:
xcx ←Solution of rlxCSP[S1, S0] ▷Obtain a (1 −ϵ
2)-approximation
6:
for all t ∈T
do
7:
LR
t ←
X
k∈N
X
j∈Dk:t∈Tj
sR
k,j(t) · x
cx
k,j; LI
t ←
X
k∈N
X
j∈Dk:t∈Tj
sI
k,j(t) · x
cx
k,j
8:
end for
9:
xlp ←Solution of LP[LR, LI, xcx, S1 ∪S0]
▷Round the LP solution
10:
¯x ←{(¯xk,j)k∈N,j∈Dk | ¯xk,j = ⌊x
lp
k,j⌋for (k, j) ∈I}
11:
if u(¯x) > u(ˆx) then
12:
ˆx ←¯x
13:
end if
14:
end if
15: end for
16: return ˆx
Proof.
One can easily see that the running time of Algorithm 1 is polynomial
in size of the input, for any given ϵ. We now argue that the solution ˆx is (1−ϵ)-
approximation for m-CSP[0, π
2 ]. Let x∗be the optimal solution for m-CSP[0, π
2 ]
of utility Opt ≜u(x∗). Deﬁne S∗≜{(k, j) ∈I | x∗
k,j = 1}. By the feasibility
of x∗, in Step 5 the algorithm obtains
u(x
cx) ≥(1 −ϵ
2) · Opt∗≥(1 −ϵ
2) · Opt,
(16)
where Opt∗is the optimal value of rlxCSP[S1, S0] for some S1 equal to the
highest 8m
ϵ utility demands in S∗, and S0∩S∗= ∅. If |S∗| ≤8m
ϵ , then obviously
ˆx = xlp = xcx and u(xcx) ≥(1 −ϵ
2)Opt.
Now suppose |S∗| > 8m
ϵ . Observe that xcx is feasible for LP[LR, LI, xcx, S1 ∪
S0] (Cons. (12)-(15) are tight when xcx is substituted). Therefore, the optimal
solution xlp of LP[LR, LI, xcx, S1 ∪S0] satisﬁes
u(x
lp) ≥u(x
cx).
(17)
By Lemma 1 below, LP[LR, LI, xcx, S1 ∪S0] has a basic feasible solution
(BFS) with at most 4m fractional components, and for any fractional component
(k, j) ∈I \ (S1 ∪S0), uk,j < min(k′,j′)∈S1 uk′,j′ ≤
P
(k′,j′)∈S1 uk′,j′
|S1|
. Therefore,
8


## Page 9


rounding down xlp in Step 10 gives,
u(ˆx) ≥u(x
lp) −4m
P
(k,j)∈S1 uk,j
|S1|
≥(1 −ϵ
2)u(x
lp)
≥(1 −ϵ
2)2 · Opt ≥(1 −ϵ) · Opt,
where the second to last inequalities follow by Eqns. (16)-(17).
It remains
to show that ˆx is feasible. Since ˆx is obtained by rounding down (some) xlp
(Step. 10),
 X
k∈N
X
j∈Dk:t∈Tj
sR
k,j(t) · ˆxk,j
2
+
 X
k∈N
X
j∈Dk:t∈Tj
sI
k,j(t) · ˆxk,j
2
(18)
≤
 X
k∈N
X
j∈Dk:t∈Tj
sR
k,j(t) · x
lp
k,j
2
+
 X
k∈N
X
j∈Dk:t∈Tj
sI
k,j(t) · x
lp
k,j
2
≤(LR
t )2 + (LI
t)2 =
 X
k∈N
X
j∈Dk:t∈Tj
sR
k,j(t)x
cx
k,j
2
+
 X
k∈N
X
j∈Dk:t∈Tj
sI
k,j(t)x
cx
k,j
2
≤C2
t ,
(19)
where Eqn. (19) follows by the feasibility of xlp and xcx respectively. Hence,
Cons. (2) are satisﬁed. Finally, since some components of xlp in Step 10 are
only rounded down, Cons. (3)-(4) are also satisﬁed.
Lemma 1 ([21]). Let x be a basic feasible solution (BFS) for LP[c1, c2, x∗, S].
Then x has at most 4m non-integral components.
Remark 1. The above proof shows that we do not need actually to solve LP[LR,
LI, xcx, S1 ∪S0]; starting from xcx, we only need to get a BFS with the same
(or better) objective value, which can be reduced to solving systems of linear
equations.
Proof.
Let h be the number of users k such that P
j∈Dk xk,j = 1.
By
the properties of a BFS (see, e.g., [22, 23]), the number of strictly positive
components in x is at most 2m + h. Furthermore, constraints (14) impose that
for each k ∈N among those h users, there is a j ∈Dk such that xk,j > 0. The
remaining 2m positive variables can belong to at most 2m of the constraints
(14), implying that at least max{h −2m, 0} variables are set to 1. It follows
that the total number variables taking non-integral values is at most 2m + h −
max{h −2m, 0} ≤4m.
4.2. Bi-criteria FPTAS for m-CSP[0, π-ε]
In the previous section, we have restricted our attention to the setting where
all demands lie in the positive quadrant of the complex plane (i.e., m-CSP[0, π
2 ]).
In this section, we extend this setting to the second quadrant (m-CSP[0, π-ε])
for any arbitrary small constant ε > 0, that is, we assume arg(sk,j(t)) ≤π −ε
for all k ∈N, j ∈Dk, t ∈Tj.
It is shown in [7] that for 1-CSP[0, π] (the
case |T | = 1) there is no (α, 1)-approximation for 1-CSP[0, π-ε] unless P=NP.
9


## Page 10


Therefore, a bi-criteria (1, 1 + ϵ) is the best approximation one can hope for.
Additionally, it is shown that if ε is arbitrarily close to zero, then there is no
(α, β)-approximation in general for any α, β with polynomial number of bits,
unless P=NP. Thus, one should expect the running time of (1, 1 + ϵ) to depend
on the maximum angle φ ≜maxk∈N,j∈Dk,t∈Tj arg(sk,j(t)). We present below
such an algorithm, which is an extension of that presented by [5] for multiple
time slots.
For convenience, we let θ = max{φ−π
2 , 0} (see Fig. 1 for an illustration). We
present a (1, 1 + ϵ)-approximation for m-CSP[0, π-ε] in Algorithm 2, denoted
by m-CSP-biFPTAS, with running time polynomial in both
1
ϵ and n (i.e.,
FPTAS). We assume that tan θ is bounded by a polynomial in n; as mentioned
above, without this assumption, a bi-criteria FPTAS is unlikely to exist (see
[7]).
Figure 1:
We measure θ = φ −π
2 from the imaginary axis.
Let N+ ≜{k ∈N | sR
k,j(t) ≥0, ∀j ∈Dk, t ∈Tj} and N−≜{k ∈N |
sR
k,j(t) < 0, ∀j ∈Dk, t ∈Tj} be the subsets of users with demands in the ﬁrst
and second quadrants, respectively. Note that N+ and N−partition the set
of users N by the assumption stated in Sec. 3. Consider any solution bx to m-
CSP[0, π-ε]. The basic idea of Algorithm m-CSP-biFPTAS is to enumerate
the guessed total projections on real and imaginary axes of all time slots for
P
k∈N+
P
j∈Dk:t∈Tj bxk,jsk,j(t) and P
k∈N−
P
j∈Dk:t∈Tj bxk,jsk,j(t), respectively.
We can use tan θ to upper bound the total projections for any feasible solution
bx (see Fig. 1 for a pictorial illustration) as follows, for all t:
X
k∈N
X
j∈Dk:t∈Tj
sI
k,j(t) · bxk,j ≤Ct,
X
k∈N−
X
j∈Dk:t∈Tj
−sR
k,j(t) · bxk,j ≤Ct tan θ,
X
k∈N+
X
j∈Dk:t∈Tj
sR
k,j(t) · bxk,j ≤Ct(1 + tan θ).
(20)
We then solve two separate multi-dimensional knapsack problems of dimen-
sion 2m (denoted by 2mDKP), to ﬁnd subsets of demands that satisfy the
individual guessed total projections. But since 2mDKP is generally NP-hard,
we need to round-up the demands to get a problem that can be solved eﬃciently
by dynamic programming. We show that the violation of the optimal solution
to the rounded problem w.r.t. to the original problem is small in ϵ.
10


## Page 11


Next, we describe the rounding in detail. First, deﬁne Lt ≜
ϵCt
n(tan θ+1), for all
t ∈T such that the new rounded demands bsk,j(t) are deﬁned by:
bsk,j(t) = bsR
k,j(t) + ibsI
k,j(t) ≜





l sR
k,j(t)
Lt
m
· Lt + i
l sI
k,j(t)
Lt
m
· Lt,
if sR
k,j(t) ≥0,
j sR
k,j(t)
Lt
k
· Lt + i
l sI
k,j(t)
Lt
m
· Lt,
otherwise.
(21)
For convenience, we assume that sk,j(t) = 0 if t ∈T \ Tj. Let ξ+ ∈Rm
+
(and ξ−∈Rm
+), ζ+ ∈Rm
+ (and ζ−∈Rm
+) be respectively the guessed real
and imaginary absolute total rounded projections of an optimal solution. Then,
the possible values of ξ+, ξ−, ζ+ and ζ−in each component t ∈T are integer
mutiples of Lt:
ξ+(t) ∈A+(t) ≜

0, Lt, 2Lt, . . . ,
Ct(1 + tan θ)
Lt

· Lt

,
ξ−(t) ∈A−(t) ≜

0, Lt, 2Lt, . . . ,
Ct · tan θ
Lt

· Lt

,
ζ+(t), ζ−(t) ∈B(t) ≜

0, Lt, 2Lt, . . . ,
Ct
Lt

· Lt

.
(22)
The next step is to solve the rounded instance exactly. Assume an arbitrary
order on N = {1, ..., n}. We use recursion to deﬁne a table, with each entry
U(k, c1, c2), c1, c2 ∈Rm
+, as the maximum utility obtained from a subset of
users {1, 2, . . . , K} ⊆N with demands {bsk,j(t)}k∈{1,...,K},j∈Dk,t∈Tj that can ﬁt
exactly (i.e., satisfy the capacity constraints with equality) within capacities
{c1
t}t=1,...,m on the real axis and {c2
t}t=1,...,m on the imaginary axis. We denote
by 2mDKP-Exact[·] the algorithm for solving exactly the rounded 2mDKP
by dynamic programming.
We provide the detailed description of 2mDKP-
Exact[·] in Algorithm 3.
Theorem 2. Algorithm m-CSP-biFPTAS is a (1, 1 + 4ϵ)-approximation for
m-CSP[0, π-ε] and its running time is polynomial in both n,
 S
k Dk
, and 1
ϵ .
Proof.
First, the running time is proportional to the number of guesses, upper
bounded by ( 1
ϵ n(tan θ + 1))O(m). For each guess, 2mDKP-Exact constructs a
table of size at most ( 1
ϵ n(tan θ + 1))O(m). Since we assumed tan θ is polynomial
in n, the total running time is polynomial in n and 1
ϵ , if m = O(1).
To show the approximation ratio of 1, we note that m-CSP-biFPTAS enu-
merates over all possible rounded projections subject to the capacity constraints
in m-CSP and that 2mDKP-Exact returns the exact optimal solution for each
rounded problem. In particular, by Lemma 2 below one of the choices would be
the rounded projection for the optimum solution x∗. It remains to show that
the violation of the returned solution is small in ϵ. This is given in Lemma 3
below, which shows that the solution bx to the rounded problem violates the
capacity constraint by only a factor of at most (1 + 4ϵ). Both lemmas can be
proved in the same way as in [6]; we include the proof below for completeness.
11


## Page 12


Algorithm 2 m-CSP-biFPTAS[{uk,j, {sk,j(t)}t∈Tj}k∈N,j∈Dk, (Ct)t∈T , ϵ]
Require: Users’ utilities and demands {uk,j, {sk,j(t)}t∈Tj}k∈N,j∈Dk; capacity
over time Ct; accuracy parameter ϵ
Ensure: (1, 1 + 4ϵ)-solution bx to m-CSP[0, π-ε]
1: bx ←0
2: for all sk,j(t), k ∈N, j ∈Dk, and t ∈Tj do
3:
Set bsk,j(t) ←bsR
k,j(t) + ibsI
k,j(t) as deﬁned by (21)
4: end for
5: for all ξ+ ∈Q
t∈T A+(t), ξ−∈Q
t∈T A−(t), ζ+, ζ−∈Q
t∈T B(t) do
6:
if
 ξ+(t) −ξ−(t)
2 +
 ζ+(t) + ζ−(t)
2 ≤(1 + 2ϵ)2C2
t for all t ∈T then
7:
y+ ←2mDKP-Exact

{uk,j, (bsk,j(t)/Lt)t}k∈N+,j∈Dk,
 ξ+(t)/Lt

t,
 ζ+(t)/Lt

t

8:
y−←2mDKP-Exact

{uk,j, (−bsk,j(t)/Lt)t}k∈N−,j∈Dk,
 ξ−(t)/Lt

t,
 ζ−(t)/Lt

t

9:
if u(y+ + y−) > u(bx) then
10:
bx ←y+ + y−
11:
end if
12:
end if
13: end for
14: return bx
Algorithm 3 2mDKP-Exact[{uk,j, {bsk,j(t)}t∈Tj}k∈W,j∈Dk, (c1
t)t∈T , (c2
t)t∈T ]
Require: Utilities, and rounded demands of a restricted set of users W ⊆N,
{uk,j, {sk,j(t)}t∈Tj}k∈N,j∈Dk; integer capacity vectors (c1
t)t∈T , (c2
t)t∈T
Ensure: A utility-maximizing optimal binary vector y subject to the capacity
constraints deﬁned by c1
t, c2
t
1: Create a table of size |W| · Q
t(c1
t + 1) · (c2
t + 1), with each entry U(k, c1, c2)
according to:
U(1, c1, c2) ≜max
j∈D1{u1,j | bsR
1,j(t) = c1
t,
bsI
1,j(t) = c2
t, ∀t}
U(k, c1, c2) ≜max

max
j∈Dk
n
uk,j + U
 k −1, (c1
t −bsk,j(t))t, (c2
t −bsk,j(t))t
o
, U(k −1, c1, c2)

U(k, c1, c2) ≜−∞for all c1, c2 ̸∈Rm
+
2: Compute the corresponding binary vector y(k, c1, c2) according to the com-
putations in step 1
3: return y(|W|, c1, c2).
For any binary vector x feasible for (m-CSP), let us write for brevity
P+,t(x) ≜
X
k∈N+
X
j∈Dk:t∈Tj
xk,jsR
k,j(t),
P−,t(x) ≜
X
k∈N−
X
j∈Dk:t∈Tj
−xk,jsR
k,j(t),
and PI,t(x) ≜
X
k∈N
X
j∈Dk:t∈Tj
xk,jsI
k,j(t).
12


## Page 13


Also, write
bP+,t(x) ≜
X
k∈N+
X
j∈Dk:t∈Tj
xk,jbsR
k,j(t),
bP−,t(x) ≜
X
k∈N−
X
j∈Dk:t∈Tj
−xk,jbsR
k,j(t), and
bPI,t(x) ≜
X
k∈N
X
j∈Dk:t∈Tj
xk,jbsI
k,j(t).
Using the fact that ℓ≤τ⌈ℓ
τ ⌉≤ℓ+ τ for any ℓ, τ such that τ > 0, and that
P
j∈Dk xk,j ≤1 by (3), we have
bP+,t(x) =
X
k∈N+
X
j∈Dk:t∈Tj
xk,jbsR
k,j(t)
≤
X
k∈N+
X
j∈Dk:t∈Tj
xk,j(sR
k,j(t) + Lt) = P+,t(x) + nLt.
The same bound holds for bP−,t and bPI,t:
max{ bP+,t(bx) −nLt, 0} ≤P+,t(x) ≤bP+,t(bx), max{ bP−,t(bx) −nLt, 0} ≤P−,t(x) ≤bP−,t(bx),
max{ bPI,t(bx) −nLt, 0} ≤PI,t(x) ≤bPI,t(bx).
(23)
Lemma 2. For any feasible solution x to m-CSP [0, π-ε], we have

X
k∈N
X
j∈Dk:t∈Tj
xk,jbsk,j(t)
 ≤(1 + 2ϵ)Ct
for all t ∈T .
Proof.
Using (20) and (23), for all t ∈T ,
 X
k∈N
X
j∈Dk:t∈Tj
xk,jbsR
k,j(t)
2
+
 X
k∈N
X
j∈Dk:t∈Tj
xk,jbsI
k,j(t)
2
=

bP+,t(x) −bP−,t(x)
2
+ bP 2
I,t(x)
= bP 2
+,t(x) + bP 2
−,t(x) −2 bP+,t(x) bP−,t(x) + bP 2
I,t(x)
≤(P+,t(x) + nLt)2 + (P−,t(x) + nLt)2 −2P+,t(x)P−,t(x) + (PI,t(x) + nLt)2
= (P+,t(x) −P−,t(x))2 + P 2
I,t(x) + 2nLt(P+,t(x) + P−,t(x) + PI,t(x)) + 3n2L2
t
=
 X
k∈N
X
j∈Dk:t∈Tj
xk,jsR
k,j(t)
2
+
 X
k∈N
X
j∈Dk:t∈Tj
xk,jsI
k,j(t)
2
+ 2nLt
 X
k∈N
X
j∈Dk:t∈Tj
xk,j|sR
k,j(t)| +
X
k∈N
X
j∈Dk:t∈Tj
xk,jsI
k,j(t)

+ 3n2L2
t
≤C2
t + 4nLt(tan θ + 1)Ct + 3n2L2
t = C2
t + 4ϵC2
t + 3ϵ2C2
t /(1 + tan θ)2
≤C2
t (1 + 4ϵ + 3ϵ2) ≤C2
t (1 + 2ϵ)2.
13


## Page 14


Lemma 3. Let bx be the solution returned by m-CSP-FPTAS. Then,

X
k∈N
X
j∈Dk:t∈Tj
bxk,jsk,j(t)
 ≤(1 + 4ϵ)Ct
for all t ∈T .
Proof.
As in the proof of Lemma 2, for all t ∈T ,
 X
k∈N
X
j∈Dk:t∈Tj
bxk,jsR
k,j(t)
2
+
 X
k∈N
X
j∈Dk:t∈Tj
bxk,jsI
k,j(t)
2
= (P+,t(bx) −P−,t(bx))2 + P 2
I,t(bx)
= P 2
+,t(bx) + P 2
−,t(bx) −2P+,t(bx)P−,t(bx) + P 2
I,t(bx).
(24)
If both bP+,t(bx) and bP−,t(bx) are less than nLt, then the R.H.S. of (24) can be bounded
by
bP 2
+,t(bx) + bP 2
−,t(bx) + bP 2
I,t(bx)
≤
bP 2
+,t(bx) + bP 2
−,t(bx) −2 bP+,t(bx) bP−,t(bx) + 2n2L2
t + bP 2
I,t(bx)
=
( bP+,t(bx) −bP−,t(bx))2 + bP 2
I,t(bx) + 2n2L2
t.
(25)
Otherwise, we bound the R.H.S. of Eqn. (24) by
bP 2
+,t(bx) + bP 2
−,t(bx) −2( bP+,t(bx) −nLt)( bP−,t(bx) −nLt) + bP 2
I,t(bx)
= ( bP+,t(bx) −bP−,t(bx))2 + bP 2
I,t(bx) + 2nLt( bP+,t(bx) + bP−,t(bx)) −2n2L2
t.
(26)
Since bx = y+ + y−is obtained from feasible solutions y+ and y−to
2mDKP-Exact

{uk,j, (bsk,j(t)/Lt)t}k∈N+,j∈Dk,
 ξ+(t)/Lt

t,
 ζ+(t)/Lt

t

and
2mDKP-Exact

{uk,j, (−bsk,j(t)/Lt)t}k∈N−,j∈Dk,
 ξ−(t)/Lt

t,
 ζ−(t)/Lt

t

, respectively,
and ξ+, ξ−, ζ+, ζ−satisfy the condition in Step 6 of Algorithm 2, it follows from (24)-
(26) that
 X
k∈N
X
j∈Dk:t∈Tj
bxk,jsR
k,j(t)
2
+
 X
k∈N
X
j∈Dk:t∈Tj
bxk,jsI
k,j(t)
2
≤
 X
k∈N
X
j∈Dk:t∈Tj
bxk,jbsR
k,j(t)
2
+
 X
k∈N
X
j∈Dk:t∈Tj
bxk,jbsI
k,j(t)
2
+ 2nLt
X
k∈N
X
j∈Dk:t∈Tj
bxk,j|bsR
k,j(t)| + 2n2L2
t
= (ξ+(t) −ξ−(t))2 + (ζ+(t) + ζ−(t))2 + 2nLt(ξ+(t) + ξ−(t)) + 2n2L2
t
≤

(1 + 2ϵ)2C2
t + 4n
ϵCt
n(tan θ + 1)(1 + tan θ)Ct + 2n2
ϵ2C2
t
n2(tan θ + 1)2

≤

(1 + 2ϵ)2 + 4ϵ + 2ϵ2
C2
t ≤(1 + 4ϵ)2C2
t .
5. m-CSP[0, π
2 ] with Polynomial number of Time Slots
In this section, we extend our results to polynomial number of time slots |T |. We
assume herein that all demands lie in the ﬁrst quadrant of the complex plane (i.e.,
φ ≜maxk arg(sk,j(t)) ≤π
2 for ∀t ∈T ). We provide a reduction to the unsplittable ﬂow
14


## Page 15


problem on a path with bag constraints (bag-UFP) for which recent approximation
algorithms are developed in the literature (see, e.g., [18, 24, 17]). We remark that bag-
UFP considers only real-valued demands, whereas in m-CSP demands are complex-
valued. We will show that such reduction will increase the approximation ratio of
bag-UFP by a constant factor of cos φ
2 , where φ ≤
π
2 is the maximum argument
of any demand. We will need the following further assumption to accommodate the
setting of bag-UFP:
• all demands are constant over time: sk,j(t) = sk,j(t′) for any t, t′ ∈Tj. To
simplify notation, let sk,j denote the unique demand over all time steps Tj.
For convenience, we shall refer to the problem as m-CSP′ when restricted with the
above assumption. When all demands in m-CSP′ are real-valued, the problem is called
bag-UFP. We can approximate an instance of m-CSP′ by an instance of (bag-UFP)
deﬁned as follows:
(bag-UFP)
max
xk,j∈{0,1}
X
k∈N
X
j∈Dk
uk,jxk,j
s.t.
X
k∈N
X
j∈Dk:t∈Tj
|sk,j|xk,j ≤Ct,
for all t ∈T
(27)
X
j∈Dk
xk,j ≤1
for all k ∈N.
(28)
Note that the absolute of the sum in Cons. (2) is replaced in bag-UFP by the sum
of the absolutes in Cons. (27). Thus all demands in bag-UFP are real-valued.
We denote by m-CSP∗(resp., bag-UFP∗) the linear relaxation of m-CSP′ (resp.,
bag-UFP), that is, when xk,j ∈[0, 1] for all k ∈N, j ∈Dk. Let Opt and Opt be the
optimal objective values of m-CSP′ and bag-UFP respectively. Also denote by Opt∗
and Opt
∗the optimal objective value of m-CSP∗and bag-UFP∗, respectively.
We will show in Lemma 4 and Theorem 3 below that one can use the algorithms
developed for bag-UFP with bounded integrality gap to obtain approximate solutions
to m-CSP′[0, π
2 ].
Lemma 4. Given a solution ¯x ∈{0, 1}|I| to bag-UFP such that u(¯x) ≥ψ · Opt
∗,
ψ ∈[0, 1], then ¯x is feasible for m-CSP′[0, π
2 ] and u(¯x) ≥ψ cos φ
2 · Opt.
Proof.
Let (x∗
k,j)k∈N ,j∈Dk be an optimal solution for m-CSP∗. Lemma 5 below
implies that
cos φ
2 ·
X
k∈N
X
j∈Dk:t∈Tj
|sk,j|x∗
k,j ≤

X
k∈N
X
j∈Dk:t∈Tj
sk,jx∗
k,j
 ≤Ct
∀t ∈T .
According to the above inequality, we can construct a feasible solution (˜xk,j)k∈N ,j∈Dk
to bag-UFP∗deﬁned by ˜xk,j ≜cos φ
2 · x∗
k,j. By the feasibility of (˜xk,j)k∈N ,j∈Dk,
Opt
∗≥
X
k∈N
X
j∈Dk
uk,j ˜xk,j = cos φ
2 ·
X
k∈N
X
j∈Dk
uk,jx∗
k,j = cos φ
2 · Opt∗.
Therefore, u(¯x) ≥ψ · Opt
∗≥ψ · cos φ
2 · Opt∗≥ψ cos φ
2 · Opt.
It remains to show that ¯x is feasible for m-CSP′, which follows readily from the
triangular inequality:

X
k∈N
X
j∈Dk:t∈Tj
sk,j ¯xk,j
 ≤
X
k∈Dk
X
j∈Dk:t∈Tj
|sk,j|¯xk,j ≤Ct
∀t ∈T .
15


## Page 16


Lemma 5 ([9]). Given a set of vectors {di ∈R2}n
i=1, then
Pn
i=1 |di|
 Pn
i=1 di
 ≤sec θ
2, where
θ is the maximum angle between any pair of vectors {di ∈R2}n
i=1 and 0 ≤θ ≤π
2 .
For completeness, we provide the proof in the appendix.
We can apply Lemma 4 using the recent LP-based algorithm by Grandoni et al. [18]
to obtain the following result.
Theorem 3. There exists an (Ω(log log n/ log n), 1)-approximation for m-CSP′[0, π
2 ].
Additionally, if all demands have the same utility, we obtain (Ω(1), 1)-approximation.
Prior work has addressed an important restriction of UFP (also bag-UFP) called
the no bottleneck assumption (NBA), namely, maxk∈N , j∈Dk |sk,j| ≤Cmin ≜mint∈T Ct,
that is, the largest demand is at most the smallest capacity over all time slots. De-
ﬁne the bottleneck time of demand (k, j) by bk,j ≜arg mint∈Tj Ct. Given a constant
δ ∈[0, 1], we call a demand (k, j) δ-small if |sk,j| ≤δCbk,j, otherwise we call it δ-large.
We remark that the NBA assumption naturally holds in smart grids since individ-
ual demands are typically much smaller than the generation capacity over all time
slots. In the following, we show that there exists an (Ω(1), 1)-approximation for m-
CSP′[0, π
2 ], under NBA. This is achieved by splitting demands to δ-small and δ-large
and solving each instance separately then taking the maximum utility solution. The
next lemma is an extension to an earlier work by Chakrabarti et al. [25] (to accommo-
date complex-valued demands) used to derive a dynamic program that approximates
δ-large demands.
Lemma 6. The number of δ-large demands that cross any time slot in any feasible
solution is at most 2⌊1
δ2 · sec φ
2 ⌋.
Proof.
Given a feasible solution ˆx, let S ≜{(k, j) ∈I | ˆxk,j = 1, sk,j > δbk,j} be the
set of indices of δ-large demands. Consider any time slot t, let St ≜{(k, j) ∈S | t ∈Tj}
be the set of demands that cross time t. Then we partition St to the sets SL
t and SR
t ,
such that SL
t (resp., SR
t ) contains demands with bottleneck time slot on the left (resp.,
right) of t. We show that |SL
t | ≤⌊1
δ2 · sec φ
2 ⌋, and a similar argument shows the same
bound for |SR
t |.
Let B be the set of bottleneck time slots for demands in SL
t . Now let t′ ∈B be
the rightmost bottleneck time slot in B. Since t′ is the bottleneck of some δ-large
demand (k, j), i.e., δCt′ < |sk,j|, and by the NBA assumption, |sk,j| ≤Cmin; it follows
that Ct′ < Cmin
δ
. Because t′ is the rightmost time slot in B, all demands in SL
t pass
through t′, therefore | P
(k,j)∈SL
t sk,j| ≤Ct′. Since all demands (k, j) ∈SL
t are δ-large,
|sk,j| > δCbk,j ≥δCmin. Therefore, using Lemma 5
δCmin|SL
t | <
X
(k,j)∈SL
t
|sk,j| ≤sec φ
2

X
(k,j)∈SL
t
sk,j
 ≤sec φ
2 · Ct′ < sec φ
2 · 1
δ Cmin.
This gives |SL
t | ≤⌊1
δ2 · sec φ
2 ⌋.
Theorem 4. Under the NBA assumption, there exists an (Ω(1), 1)-approximation for
m-CSP′[0, π
2 ]. The running time is O(n2).
Proof.
We set δ = 1
2. For small demands, Chakaravarthy et al. [24] present a primal-
dual 1
9-approximation algorithm for bag-UFP that runs in O(n2). By Lemma 4, this
algorithm is also ( 1
9 cos φ
2 )-approximation to m-CSP′ with small demands.
Large
16


## Page 17


demands can be handled via a simple reduction to the weighted job interval selection
problem proposed in [17] (i.e., restrict selected demands to be disjoint). By Lemma 6
we loose a factor of 8 sec φ
2 , then we apply the 2-approximation by Bar-Noy et al. [26]
which runs in O(n log n). Hence we obtain a ( 1
25 cos φ
2 , 1)-approximation that runs in
O(n2).
6. Practical Greedy Approximation for 1-CSP[0, π
2 ]
In this section we give a practical greedy constant-factor approximation algorithm,
presented in Algorithm 4, and denoted by 1-CSP-Greedy, for the single time slot case
(1-CSP[0, π
2 ]) where |T | = 1. Despite the theoretical value of the PTAS and FPTAS
presented in [5] (that are generalized in Sec. 4), the running time is quite large and
hence impractical for real world applications. Algorithm 1-CSP-Greedy, on the other
hand, achieves
  1
2 cos φ
2 , 1

-approximation in O(N log N) time, where N ≜P
k∈N |Dk|.
This result can be derived directly by combining Lemma 4 (restricted to the case
|T | = 1) with the known analysis of the greedy algorithm for the multiple-choice
Knapsack problem [27] and its connection to the LP relaxation. However, we include
the proof here for completeness. Note that such a simple greedy algorithm can be
used to provide a fast heuristic for practical settings when considering multiple time
slots. For instance, in the setting where users arrive online, 1-CSP-Greedy could be
applied to each time slot, after reducing the capacity by the magnitude of demands
consumed in previous time slots.
Consider the simpliﬁed version of m-CSP denoted by 1-CSP where |T | = 1:
(1-CSP)
max
X
k∈N
X
j∈Dk
uk,jxk,j
(29)
subject to

X
k∈N
X
j∈Dk
sk,j · xk,j
 ≤C
(30)
X
j∈Dk
xk,j ≤1,
for all k ∈N
(31)
xk,j ∈{0, 1} for all (k, j) ∈I.
(32)
For convenience, we add a dummy demand to each set Dk, for each user k ∈N
with utility of 0 and demand of sk,0 = 0. This is to guarantee that a solution to
1-CSP problem contains exactly one demand from each set Dk for every user k ∈N.
Note that this change does not aﬀect the 1-CSP problem.
If a user’s complex-valued power demand is substituted in (1-CSP) by its real-
valued magnitude, the inequality constraint (31) is transformed into an equality con-
straint and the binary decision variables xk,j are relaxed such that they take non-
negative real values (i.e., (xk,j)k∈N ,j∈Dk ∈[0, 1]|I|), the following linear programming
(LP) problem is obtained.
17


## Page 18


(Rx1-CSP)
max
X
k∈N
X
j∈Dk
uk,jxk,j
(33)
subject to
X
k∈N
X
j∈Dk
sk,j
 · xk,j ≤C
(34)
X
j∈Dk
xk,j = 1,
for all k ∈N
(35)
xk,j ∈[0, 1] for all (k, j) ∈I .
(36)
We make use of the following statement.
Proposition 1 ([28, 27, 29]).
(i) If two demands j, h ∈Dk belonging to the same
set Dk, for k ∈N, with |sk,j| ≤|sk,h| satisfy
uk,j ≥uk,h ,
then an optimal solution to (1-CSP) with xk,h = 0 exists.
(ii) If two demands j, h ∈Dk belonging to the same set Dk, for k ∈N, with |sk,j| ≤
|sk,h| satisfy
uk,j
|sk,j| ≤uk,h
|sk,h| ,
then an optimal solution to Rx1-CSP with xk,j = 0 exists.
(iii) If some demands j, h, l ∈Dk, k ∈N with |sk,j| < |sk,h| < |sk,l|, uk,j < uk,h <
uk,l, and
uk,j
|sk,j| ≥
uk,h
|sk,h| ≥
uk,l
|sk,l| satisfy
uk,h −uk,j
|sk,h| −|sk,j| ≤
uk,l −uk,h
|sk,l| −|sk,h| ,
then an optimal solution to Rx1-CSP with xk,h = 0 exists.
The above proposition implies that, without losing all optimal solutions to Rx1-
CSP, we can preprocess the demands of each set Dk, k ∈N, to obtain a corresponding
new set Rk ⊆Dk that satisﬁes:
|sk,1| ≤|sk,2| ≤... ≤|sk,rk|,
(37)
|uk,1| ≤|uk,2| ≤... ≤|uk,rk|,
(38)
uk,1
|sk,1| > uk,2
|sk,2| > ... > uk,rk
|sk,rk|,
(39)
uk,2 −uk,1
|sk,2| −|sk,1| >
uk,3 −uk,2
|sk,3| −|sk,2| > ... >
uk,rk −uk,rk−1
|sk,rk| −|sk,rk−1|.
(40)
Observe that this reduction requires only O(P
k∈N |Dk| log |Dk|) time, as it can be
done by sorting each Dk followed by a linear scan to remove the demands that do not
appear in the optimal solution.
In [27] (see also [29, Chapter 11]), it was also proved that the LP optimal solution to
Rx1-CSP problem may be found by a greedy algorithm which starts by ﬁnding the sets
Rk above. Assume the ordering |sk,1| ≤|sk,2| ≤... ≤|sk,rk| in Rk, where rk = |Rk|.
Initially, the algorithm selects the dummy demand sk,0 for each customer and sets
the corresponding decision variables to 1. Next, the greedy algorithm constructs a
18


## Page 19


new set E by combining all the sets Rk, k ∈N and setting ˜uk,j = uk,j −uk,j−1 and
|˜sk,j| = |sk,j| −|sk,j−1| for j = 1, ..., rk. After sorting entries in E by their eﬃciency,
deﬁned as
˜uk,j
|˜sk,j| in non-increasing order, the greedy execution continues by selecting
demands in the aforementioned sorted considering the capacity C. Each time an item
(k, j) is selected from set E, we assign ˜xk,j ←1, ˜xk,j−1 ←0 and τ = τ + |˜sk,j|, where
the initial value of τ is 0. Assume at some iteration adding the next item (k′, j′) to
the current solution vector ˜x causes capacity violation, that is
τ ≤C and τ + |˜sk′,j′| > C .
(41)
The greedy execution is stopped at this point and the remaining capacity C −τ is
occupied by the corresponding fractional part of the (k′, j′) item’s power demand and
the item’s (k′, j′ −1) decision variable is set as follows:
˜xk′,j′ = C −τ
|˜sk′,j′| and ˜xk′,j′−1 = 1 −˜xk′,j′ where k′ ∈N, j′ ∈Rk′.
In [28, 27], it was shown that this greedy strategy indeed produces an optimal
solution to Rx1-CSP problem containing at most two fractional variables that belong
to adjacent users in the sorted set Rk′ as given above. Note that algorithm 1-CSP-
Greedy is almost the same as this greedy algorithm algorithm described above, except
that we drop the fractional values.
Theorem 5. Algorithm 1-CSP-Greedy is
  1
2 cos φ
2 , 1

-approximation for 1-CSP[0, π
2 ].
The running time is O(N log N).
Proof.
Let S∗⊆I be an optimal solution of (1-CSP), and denote by Opt and Opt∗
the optimal objective values of (1-CSP) and (Rx1-CSP), respectively.
Denote by
Es ≜E \ {(k′, j′), (k′, j′ −1)}, and let
bp ≜
X
(k,j)∈Es
uk,j ˜xk,j and umax ≜
max
j∈Rk,k∈N{uk,j} ,
(42)
where ˜x is as deﬁned in the algorithm. For the optimal solution to Rx1-CSP problem
we get
Opt∗= ˆp + ˜xk′,j′uk′,j′ + ˜xk′,j′−1uk′,j′−1 ≤ˆp + uk′,j′ .
(43)
On the other hand, by Lemma 5 it follows that
cos φ
2 ·
X
(k,j)∈S∗
|sk,j| ≤

X
(k,j)∈S∗
sk,j
 ≤C .
(44)
Note that the subset S∗, which is an optimal solution to (1-CSP), becomes a
feasible solution to Rx1-CSP if the relaxed decision variables are set xk,j = cos φ
2 for
all (k, j) ∈S∗, xk,0 = 1 −P
(k,j)∈S∗xk,j and xk,j = 0 otherwise. This implies that
Opt∗≥cos φ
2 ·
X
(k,j)∈S∗
uk,j = cos φ
2 · Opt .
(45)
Denote by ZAlg the utility of the output solution of 1-CSP-Greedy when applied
to 1-CSP problem.
To investigate the worst case approximation ratio of 1-CSP-
Greedy for 1-CSP problem, consider Eqn. (43) and observe that
Opt∗≤ˆp + umax .
(46)
19


## Page 20


Algorithm 4 1-CSP-Greedy[{uk,j, sk,j}k∈N,j∈Dk, C]
Require: Users’ utilities and demands {uk,j, sk,j}k∈N,j∈Dk; capacity C
Ensure: ( 1
2 cos φ
2 , 1)-solution ¯x to 1-CSP
Initialization:
• Add a dummy demand with zero utility and zero demand to each set Dk,
k ∈N
• Sort users in each set Dk, k ∈N by the magnitude of their demands in
increasing order such that if j ≤j′, then |sk,j| ≤|sk′,j′| for all j′, j ∈Dk
• For each k ∈N deﬁne a new set Rk ⊆Dk by successively testing the
demands in Dk according to Eqns. (37)-(40). Assume the ordering |sk,1| ≤
|sk,2| ≤... ≤|sk,rk| in Rk, where rk = |Rk|
• E ←∅, ˜x ←0, ˜xk,0 ←1 for all k ∈N, τ ←0, bx ←˜x
1: for k ∈N, j = 1, ..., rk do
2:
˜uk,j ←uk,j −uk,j−1, ˜sk,j ←sk,j −sk,j−1
3:
E ←E ∪{(k, j)}
4: end for
5: Sort items in E by their eﬃciency ( ˜uk,j
|˜sk,j|) in a non-increasing order
6: for (k, j) ∈E (in the sorted order) do
7:
if τ +
˜sk,j
 ≤C then
8:
˜xk,j ←1, ˜xk,j−1 ←0, τ ←τ +
˜sk,j

9:
break
10:
end if
11: end for
12: Set bxk′,j′ ←1 for (k′, j′) ≜arg maxj∈Rk,k∈N {uk,j}, bxk′,0 ←0
13: Set ¯x ←arg maxx∈{bx,˜x} u(x)
14: return ¯x
Evidently, ZAlg ≥ˆp. This gives
Opt∗≤ZAlg + umax .
(47)
From the formulation of algorithm 1-CSP-Greedy, ZAlg ≥umax, and hence by
Eqns. (47) and (45) it follows that
ZAlg ≥1
2 cos φ
2 · Opt .
(48)
Finally, note that the solution ¯x is feasible for (1-CSP) by the triangular inequal-
ity.
7. Extension to the Mixed Case
In practical applications of the complex-demand scheduling problem, we may have
the situation when some of the users’ demands are elastic in the sense that they can
be partially satisﬁed. An example is an appliance that should be either supplied with
a ﬁxed amount of power, or switched oﬀ. Formally, we may assume that each user’s
demand is composed of two sets Dk = DI
k ∪DF
k , where each is a set of demands of the
20


## Page 21


form {sk,j(t)}t∈Tj, as before. A feasible solution now would select, for each user k,
one of the demands in j ∈Dk and assign either xk,j ∈{0, 1} if j ∈DI
k or xk,j ∈[0, 1]
if j ∈DF
k .
We show in this section that we can reduce this mixed case to the fully inelastic
case. First, we note that
Opt ≥LB ≜max
(
max
k∈N , j∈DI
k
uk,j,
max
k∈N , j∈DF
k
min

min
t∈Tj
uk,jCt
|sk,j(t)|, uk,j
)
.
(49)
Let O = {uk,j, {sk,j(t)}t∈Tj}k∈N ,j∈Dk=DI
k ∪DF
k , we construct a fully inelastic in-
stance O′ = {u′
k,j, {s′
k,j(t)}t∈Tj}k∈N ,j∈D′
k as follows. Let ϵ ∈(0, 1) be an arbitrary
constant. For each k ∈N, we deﬁne the set D′
k = DI
k ∪D′′
k, where D′′
k is deﬁned as
follows. For each k ∈N, j ∈DF
k , we introduce a number of nk,j =

log1+ϵ
nuk,j
ϵ·LB

new
demands, given by si
k,j(t) =
ϵ·LB(1+ϵ)isk,j(t)
nuk,j
for t ∈Tj, with utility ui
k,j = ϵ·LB(1+ϵ)i
n
.
Then we set D′′
k = {(j, i) : i = 1, . . . , nk,j }, where (j, i) ∈D′′
k indices the demand
{si
k,j(t)}t∈Tj; we denote the corresponding variable in the formulation (m-CSP) of
the new instance by xi
k,j.
Given a solution x for O′, we construct a solution bx for O in the obvious way: if
j ∈DI
k , then we set bxk,j = xk,j; otherwise, if xi
k,j = 1, we set bxk,j = ϵ·LB(1+ϵ)i
nuk,j
.
Lemma 7. Let x be an (α, β)-approximate solution for O′. Then bx is a ((1 −ϵ)α, β)-
approximate solution for O.
Proof.
Let x∗be an optimal solution for O. We round x∗to a (1−ϵ, 1)-approximate
solution ex for O′ as follows. If j ∈DI
k , we keep exk,j = x∗
k,j ∈{0, 1}. Otherwise,
x∗
k,j ∈[0, 1] is positive only for at most one index j ∈DF
k . In this case, we set exk,j = 0
if x∗
k,j <
ϵ·LB
nuk,j , and otherwise set exk,j = ϵ·LB(1+ϵ)i
nuk,j
, where i is the largest integer i′
such that ϵ·LB(1+ϵ)i′
nuk,j
≤x∗
k,j. Note that ex is feasible for O′ since ex ≤x∗. Furthermore,
u(ex) ≥(1 −ϵ)u(x∗), since the total utility corresponding to all the variables that are
dropped to 0 is at most
X
k∈N , j∈DF
k
uk,j · ϵ · LB
nuk,j ≤ϵ · Opt = ϵ · u(x∗),
while for all other variables we have exk,j ≥(1 −ϵ)x∗
k,j. Moreover,
X
k∈N
X
j∈Dk:Tj∋t
sk,j(t) · bxk,j =
X
k∈N
X
j∈DI
k :Tj∋t, xk,j=1
sk,j(t)
+
X
k∈N
X
j∈DF
k :Tj∋t, xi
k,j=1
sk,j(t)ϵ · LB(1 + ϵ)i
nuk,j
=
X
k∈N
X
j∈DI
k :Tj∋t
sk,j(t)xk,j +
X
k∈N
X
(j,i)∈D′′
k :Tj∋t
si
k,j(t)xi
k,j
≤β · Ct,
by the β-feasibility of x for O′. The lemma follows.
21


## Page 22


8. Conclusion
This paper extends the previous results known for the single time slot case (CKP)
to a more general scheduling setting. When the number of time slots m is constant,
both the previously known PTAS and FPTAS are extended to handle multiple-time
slots, multiple user preferences, and handle mixed elastic and inelastic demands. For
polynomial m, a reduction is presented from CSP[0, π
2 ] to the real-valued bag-UFP,
which can be used to obtain algorithms for CSP[0, π
2 ] based on bag-UFP algorithms
that have bounded integrability gap for their LP-relaxation. We further presented a
practical greedy algorithm that can be implemented eﬃciently in real systems. As a
future work, it would be interesting to improve the second case (polynomial m) to
a constant-factor approximation, following the recent results in [30]. Additionally, it
might be of interest to consider diﬀerent objective functions such as minimizing the
maximum peak consumption at any time slot. Complementing this paper, extended
algorithms have been developed for more sophisticated settings, such as online algo-
rithm for CSP [31] and scheduling in electrical power networks [32, 33, 34, 35]
Acknowledgments
We thank the anonymous reviewers for careful reading and helpful comments.
References
References
[1] J. Grainger, W. Stevenson, Power System Analysis, McGraw-Hill, 1994.
[2] C.-L. Su, D. Kirschen, Quantifying the eﬀect of demand response on electricity
markets, Power Systems, IEEE Transactions on 24 (3) (2009) 1199–1207. doi:
10.1109/TPWRS.2009.2023259.
[3] L. Yu, C.-K. Chau, Complex-demand Knapsack Problems and Incentives in AC
Power Systems, in: Proceedings of the 2013 International Conference on Au-
tonomous Agents and Multi-agent Systems, AAMAS ’13, Richland, SC, 2013,
pp. 973–980.
[4] G. J. Woeginger, When does a dynamic programming formulation guarantee the
existence of a fully polynomial time approximation scheme (FPTAS)?, INFORMS
Journal on Computing 12 (1) (2000) 57–74.
[5] C.-K. Chau, K. Elbassioni, M. Khonji, Truthful mechanisms for combinatorial ac
electric power allocation, in: Proceedings of the 2014 International Conference on
Autonomous Agents and Multi-agent Systems, AAMAS ’14, Richland, SC, 2014,
pp. 1005–1012, http://arxiv.org/abs/1403.3907.
[6] C.-K. Chau, K. Elbassioni, M. Khonji, Truthful mechanisms for combinatorial
allocation of electric power in alternating current electric systems for smart
grid, ACM Transactions on Economics and Computation 5 (2016) 7:1–7:29,
http://arxiv.org/abs/1507.01762.
22


## Page 23


[7] M. Khonji, C. K. Chau, K. Elbassioni, Inapproximability of power allocation with
inelastic demands in ac electric systems and networks, in: 2014 23rd International
Conference on Computer Communication and Networks (ICCCN), 2014, pp. 1–6.
[8] K. Elbassioni, T. T. Nguyen, Approximation schemes for multi-objective opti-
mization with quadratic constraints of ﬁxed cp-rank, in: Proceedings of the 4th
International Conference on Algorithmic Decision Theory - Volume 9346, ADT
2015, Springer-Verlag, Berlin, Heidelberg, 2015, pp. 273–287.
[9] A. Karapetyan, M. Khonji, C. K. Chau, K. Elbassioni, H. H. Zeineldin, Eﬃcient
algorithm for scalable event-based demand response management in microgrids,
IEEE Transactions on Smart Grid 9 (4) (2018) 2714–2725. doi:10.1109/TSG.
2016.2616945.
[10] M. Khonji, C. K. Chau, K. Elbassioni, Optimal power ﬂow with inelastic demands
for demand response in radial distribution networks, IEEE Transactions on Con-
trol of Network Systems 5 (1) (2018) 513–524. doi:10.1109/TCNS.2016.2622362.
[11] A. Darmann, U. Pferschy, J. Schauer, Resource allocation with time intervals,
Theoretical Computer Science 411 (49) (2010) 4217–4234.
[12] N. Bansal, A. Chakrabarti, A. Epstein, B. Schieber, A quasi-ptas for unsplittable
ﬂow on line graphs, in: STOC, ACM, 2006, pp. 721–729. doi:10.1145/1132516.
1132617.
[13] A. Anagnostopoulos, F. Grandoni, S. Leonardi, A. Wiese, A mazing 2+ ε approx-
imation for unsplittable ﬂow on a path, in: SODA, SIAM, 2014, pp. 26–41.
[14] C. Chekuri, M. Mydlarz, F. B. Shepherd, Multicommodity demand ﬂow in a tree
and packing integer programs, ACM Transactions on Algorithms (TALG) 3 (3).
doi:10.1145/1273340.1273343.
[15] V. T. Chakaravarthy, V. Pandit, Y. Sabharwal, D. P. Seetharam, Varying band-
width resource allocation problem with bag constraints, in: IEEE International
Symposium on Parallel & Distributed Processing (IPDPS), 2010, pp. 1–10.
[16] F. C. Spieksma, On the approximability of an interval scheduling problem, Jour-
nal of Scheduling 2 (5) (1999) 215–227.
[17] K. Elbassioni, N. Garg, D. Gupta, A. Kumar, V. Narula, A. Pal, Approximation
Algorithms for the Unsplittable Flow Problem on Paths and Trees, in: IARCS
Annual Conference on Foundations of Software Technology and Theoretical Com-
puter Science (FSTTCS 2012), Vol. 18 of Leibniz International Proceedings in
Informatics (LIPIcs), Dagstuhl, Germany, 2012, pp. 267–275.
[18] F. Grandoni, S. Ingala, S. Uniyal, Improved Approximation Algorithms for Un-
splittable Flow on a Path with Time Windows, Springer International Publishing,
2015, pp. 13–24.
[19] A. S. Nemirovski, M. J. Todd, Interior-point methods for optimization, Acta
Numerica 17 (1) (2008) 191–234.
23


## Page 24


[20] K. Elbassioni, T. T. Nguyen, Approximation algorithms for binary packing prob-
lems with quadratic constraints of low cp-rank decompositions, Discrete Applied
Mathematics 230 (2017) 56–70.
[21] B. Patt-Shamir, D. Rawitz, Vector bin packing with multiple-choice, in: Al-
gorithm Theory - SWAT 2010, Springer Berlin Heidelberg, 2010, pp. 248–259.
doi:10.1007/978-3-642-13731-0_24.
[22] M. Gr¨otschel, L. Lov´asz, A. Schrijver, Geometric Algorithms and Combinatorial
Optimization, Springer, New York, 1988.
[23] A. Schrijver, Theory of Linear and Integer Programming, Wiley, New York, 1986.
[24] V. T. Chakaravarthy, A. R. Choudhury, S. Gupta, S. Roy, Y. Sabharwal, Improved
algorithms for resource allocation under varying capacity, in: Algorithms-ESA
2014, Springer Berlin Heidelberg, Berlin, Heidelberg, 2014, pp. 222–234.
[25] A. Chakrabarti, C. Chekuri, A. Gupta, A. Kumar, Approximation algorithms for
the unsplittable ﬂow problem, Algorithmica 47 (1) (2007) 53–78.
[26] A. Bar-Noy, R. Bar-Yehuda, A. Freund, J. (Seﬃ) Naor, B. Schieber, A uniﬁed
approach to approximating resource allocation and scheduling, J. ACM 48 (5)
(2001) 1069–1090. doi:10.1145/502102.502107.
[27] T. Ibaraki, T. Hasegawa, The Multiple-Choice Knapsack Problem, Journal of the
Operations Research Society of Japan 21 (1) (1978) 59–93.
[28] A. Chandra, D. Hirschberg, C. Wong, Approximate algorithms for the knapsack
problem and its generalizations, IBM Research Report RC56l6, IBM T. J. Watson
Research Center.
[29] H. Kellerer, U. Pferschy, D. Pisinger, Knapsack Problems, Springer, 2010.
[30] A. Anagnostopoulos, F. Grandoni, S. Leonardi, A. Wiese, Constant integrality
gap LP formulations of unsplittable ﬂow on a path, in: International Conference
Integer Programming and Combinatorial Optimization (IPCO), 2013, pp. 25–36.
[31] A. Karapetyan, M. Khonji, C.-K. Chau, K. Elbassioni, Online algorithm for de-
mand response with inelastic demands and apparent power constraint, Tech. rep.,
Masdar Institute, https://arxiv.org/abs/1611.00559 (2016).
[32] M. Khonji, S. C.-K. Chau, K. Elbassion, Combinatorial optimization of ac optimal
power ﬂow in radial distribution networks, arXiv preprint arXiv:1709.08431.
[33] M. Khonji, S. C.-K. Chau, K. Elbassioni, Challenges in scheduling electric vehicle
charging with discrete charging rates in ac power networks, in: Proceedings of the
Ninth International Conference on Future Energy Systems, e-Energy ’18, 2018,
pp. 183–186. doi:10.1145/3208903.3208934.
URL http://doi.acm.org/10.1145/3208903.3208934
[34] M. Khonji, S. C.-K. Chau, K. Elbassioni, Approximation scheduling algorithms
for electric vehicle charging with discrete charging options, in: Proceedings of the
Ninth International Conference on Future Energy Systems, e-Energy ’18, 2018,
pp. 579–585. doi:10.1145/3208903.3213895.
URL http://doi.acm.org/10.1145/3208903.3213895
24


## Page 25


[35] M. Khonji, S. C.-K. Chau, K. Elbassioni, Combinatorial optimization of elec-
tric vehicle charging in ac power distribution networks, in: IEEE International
Conference on Communications, Control, and Computing Technologies for Smart
Grids, SmartGridComm ’18, 2018.
Appendix
Proof of Lemma 5
Lemma 5 ([9]). Given a set of 2D vectors {di ∈R2}n
i=1
Pn
i=1 |di|

Pn
i=1 di

≤sec θ
2,
where θ is the maximum angle between any pair of vectors and 0 ≤θ ≤π
2 .
Proof.
If θ = 0 then the statement is trivial, therefore we assume otherwise. We
prove
(Pn
i=1 |di|)2
| Pn
i=1 di|2
≤
2
cos θ+1 by induction (notice that sec θ
2 =
q
2
cos θ+1). First, we
expand the left-hand side by
Pn
i=1 |di|2 + 2 P
1≤i<j≤n |di| · |dj|
Pn
i=1 |di|2 + 2 P
1≤i<j≤n |di| · |dj|(sin θi sin θj + cos θi cos θj)
=
Pn
i=1 |di|2 + 2 P
1≤i<j≤n |di| · |dj|
Pn
i=1 |di|2 + 2 P
1≤i<j≤n |di| · |dj| cos(θi −θj),
(50)
where θi is the angle that di makes with the x axis.
Consider the base case: n = 2. Eqn. (50) becomes
|d1|2 + |d2|2 + 2|d1| · |d2|
|d1|2 + |d2|2 + 2|d1| · |d2| cos(θ) = f
|d2|
|d1|

,
(51)
where f(x) ≜
1+x2+2x
1+x2+2x cos θ . The ﬁrst derivative is given by
f ′(x) = (1 + x2 + 2x cos θ)(2x + 2) −1 + x2 + 2x)(2x + 2 cos θ)
(1 + x2 + 2x cos θ)2
f ′(x) is zero only when x = 1. Hence, f(1) is an extreminum point. We compare f(1)
with f(x) at the boundaries x ∈{0, ∞}:
f(1) =
2
cos θ + 1 ≥f(0) = lim
x→∞f(x) = 1
Therefore, f(x) has a global maximum of
2
cos θ+1.
Next, we proceed to the inductive step. We assume
Pr−1
i=1 |di|
 Pr−1
i=1 di
 ≤
q
2
cos θ+1 where
r ∈{1, . . . , n}. W.l.o.g., assume θ2 ≥θ3 ≥· · · ≥θn ≥θ1. Rewrite Eqn. (50) as
(Pr
i=1 |di|)2
r
X
i=1
|di|2 + 2
X
1≤i<j<r
|di||dj| cos(θi −θj) + 2|dr|
X
1≤i<r
|di| cos(θi −θr)
(52)
25


## Page 26


Let g(θr) be the denominator of Eqn. (52). We take the second derivative of g(θr):
g′′(θr) = −2|dr|
X
1≤i<r
|di| cos(θi −θr)
Notice that cos(θi −θr) ≥0, therefore the second derivative is always negative. This
indicates that all local exterma in [0, θr−1] of g(θn) are local maxima.
Hence, the
minimum occurs at the boundaries:
min
θr∈[0,θr−1] g(θr) ∈{g(0), g(θr−1)}
If θr ∈{0, θr} , then there must exist at least a pair of vectors in {di}r
i=1 with the same
angle. Combining these two vectors into one, we can obtain an instance with r −1
vectors. Hence, by the inductive hypothesis, the same bound holds up to r vectors.
26

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
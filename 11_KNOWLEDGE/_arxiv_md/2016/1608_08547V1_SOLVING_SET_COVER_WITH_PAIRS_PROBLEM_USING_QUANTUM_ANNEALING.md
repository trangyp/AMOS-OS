---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1608.08547v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1608.08547v1_Solving_Set_Cover_with_Pairs_Problem_Using_Quantum_Annealing

> Source: 1608.08547v1_Solving_Set_Cover_with_Pairs_Problem_Using_Quantum_Annealing.pdf

> Pages: 19

---


## Page 1


Solving Set Cover with Pairs Problem Using
Quantum Annealing
Yudong Cao1,*, Shuxian Jiang1,†, Debbie Perouli2, and Sabre Kais3,4
1Department of Computer Science, Purdue University, West Lafayette, IN 47906, USA
2Department of Mathematics, Statistics and Computer Science, Marquette University, Milwaukee, WI 53233, USA
3Department of Chemistry, Physics and Birck Nanotechnology Center, Purdue University, West Lafayette, IN 47906,
USA
4Qatar Energy and Environment Research Institute (QEERI), HBKU, Doha, Qatar
*cao23@purdue.edu, † jiang97@purdue.edu
ABSTRACT
Here we consider using quantum annealing to solve Set Cover with Pairs (SCP), an NP-hard combinatorial optimization
problem that play an important role in networking, computational biology, and biochemistry. We show an explicit construction of
Ising Hamiltonians whose ground states encode the solution of SCP instances. We numerically simulate the time-dependent
Schr¨odinger equation in order to test the performance of quantum annealing for random instances and compare with that of
simulated annealing. We also discuss explicit embedding strategies for realizing our Hamiltonian construction on the D-wave
type restricted Ising Hamiltonian based on Chimera graphs. Our embedding on the Chimera graph preserves the structure of
the original SCP instance and in particular, the embedding for general complete bipartite graphs and logical disjunctions may
be of broader use than that the speciﬁc problem we deal with.
1 Introduction
Quantum annealing (QA) uses the principles of quantum mechanics for solving unconstrained optimization problems1–4. Since
the initial proposal of QA, there has been much interest in the search for practical problems where it can be advantageous with
respect to classical algorithms4–33, particularly simulated annealing (SA)34–36. Extensive theoretical, numerical and expeirmental
efforts have been dedicated to studying the performance of quantum annealing on problems such as satisﬁability37–39, exact
cover3,39, max independent set39, max clique40, integer factorization41, graph isomorphism42,43, ramsey number44, binary
classiﬁcation45,46, unstructured search47 and search engine ranking48. Many of these approaches3,37,38,40–46 recast the
computational problem at hand into a problem of ﬁnding the ground state of a quantum Ising spin glass model, which is
NP-complete to solve in the worst case49,50.
The computational difﬁculty of Ising spin glass has not only given the quantum Ising Hamiltonians the versatility for
efﬁciently encoding many problems in NP50, but also motivated physical realization of QA using systems described by the
quantum Ising model6,7,9. The notion of adiabatic quantum computing (AQC)3,37,51, which can be regarded as a particular
class of QA, has further established QA in the context of quantum computation (In this work we will use the terms quantum
annealing and adiabatic quantum computing synonymously). Although it is believed that even universal quantum computers
cannot solve NP-complete problems efﬁciently in general52, there has been evidence in experimental quantum Ising systems
that suggests quantum speedup over classical computation due to quantum tunneling53,54. It is then of great interest to explore
more regimes where quantum annealing could offer a speedup compared with simulated annealing.
Here we consider a variant of Set Cover (SC) called Set Cover with Pairs (SCP). SC is one of Karp’s 21 NP-complete
problems55 and SCP was ﬁrst introduced56 as a generalization of SC. Instead of requiring each element to be covered by a
single object as in SC, the SCP problem is to ﬁnd a minimum subset of objects so that each element is covered by at least
one pair of objects. We will present its formal deﬁnition in Section 2. SCP and its variants arise in a wide variety of contexts
including Internet trafﬁc monitoring and content distribution57, computational biology58,59, and biochemistry60. On classical
computers, the SCP problem is at least as hard to approximate as SC. Speciﬁcally, its difﬁculty on classical computers can
be manifested in the results by Breslau et al57, which showed that no polynomial time algorithm can approximately solve
Disjoint-Path Facility Location, a special case of SCP, on n objects to within a factor that is 2log1−ε n for any ε > 0. Due to its
complexity, various heuristics56 and local search algorithms60 have been proposed.
In this paper we explore using quantum annealing based on Ising spin glass to solve SCP. We start by reducing SCP to
ﬁnding the ground state of Ising spin glass, via integer linear programming (Theorem 1). We then simulate the adiabatic
arXiv:1608.08547v1  [quant-ph]  30 Aug 2016


## Page 2


evolution of the time dependent transverse Ising Hamiltonian H(s) = (1−s)H0 +sH1 which interpolates linearly between an
initial Hamiltonian H0 of independent spins in uniform transverse ﬁeld and a ﬁnal Hamiltonian H1 that encodes an SCP instance.
For randomly generated SCP instances that lead to Ising Hamiltonian constructions of up to 19 spins, we explicitly simulate the
time dependent Schr¨odinger equation. We compute the minimum evolution time that each instance needed to accomplish 25%
success probability. For benchmark purpose we also use simulate annealing to solve the instances and compare its performance
with that of adiabatic evolution. Results show that the median time for yielding 25% success probablity scales as O(20.33M) for
quantum annealing and O(20.21M) for simulated annealing, observing no general quantum speedup. However, the performance
of quantum annealing appears to have wider range of variance from instance to instance than simulated annealing, casting hope
that perhaps certain subsets of the instance could yield a quantum advantage over the classical algorithms.
Aside from the theoretical and numerical studies, we also consider the potential implementation our Hamiltonian con-
struction on the large-scale Ising spin systems manufactured by D-Wave Systems6,7,9,14. Benchmarking the efﬁciency of
QA is currently of signiﬁcant interest. An important issue that needs to be addressed in such benchmarks is that the physical
implementation of the algorithm could be affected by instance-speciﬁc features. This is manifested in the embedding61,62 of
the Ising Hamiltonian construction onto the speciﬁc topology of the hardware (the Chimera graph21,61,63). Here we present a
general embedding of SCP instances onto a Chimera graph that preserves the original structure of the instances and requires
less qubits than the usual approach by complete graph embedding. This allows for efﬁcient physical implementations that are
untainted by ad hoc constructions that are speciﬁc to individual instances.
2 Preliminaries
2.1 Set Cover with Pairs
Given a ground set U and a collection S of subsets of U, which we call the cover set. Each element in S has a non-negative
weight, the Set Cover (SC) problem asks to ﬁnd a minimum weight subset of S that covers all elements in U. Deﬁne cover
function as Q : S 7→2U where ∀s ∈S, Q(s) is the set of all elements in U covered by s. Then SC can be formulated as ﬁnding a
minimum weight S′ ⊆S such that Q(S′) = ∪s′∈S′Q(s′) = U. Set Cover with Pairs (SCP) can be considered as a generalization
of SC in the sense that if we deﬁne the cover function such that ∀i, j ∈S, i ̸= j, Q(i, j) is the set of elements in U covered by
the pair {i, j}, then SCP asks to ﬁnd a minimum subset A ⊆S such that Q(A) = ∪{i,j}∈SQ(i, j) = U. Here we restrict to cases
where each element of S has unit weight.
A graph G(V,E) is a set of vertices V connected by a set of edges E. A bipartite graph is deﬁned as a graph whose set of
vertices V can be partitioned into two disjoint sets V1 and V2 such that no two vertices within the same set are adjacent. We
formally deﬁne SCP as the following.
Deﬁnition 1. (Set Cover with Pairs) Let U and S be disjoint sets of elements and V = U ∪S. Given a bipartite graph G(V,E)
between U and S with E being the set of all edges, ﬁnd a subset A ⊆S such that:
1. ∀ci ∈U, ∃a(i)
1 ,a(i)
2 ∈A such that (a(i)
1 ,ci) ∈E and (a(i)
2 ,ci) ∈E. In other words, ci is covered by the pair {a(i)
1 ,a(i)
2 }.
2. The size of the set, |A|, is minimized.
We use the notation SCP(G,U,S) to refer to a problem instance with |U| = n, |S| = m and the connectivity between U and S
determined by G.
2.2 Quantum annealing, adiabatic quantum computing
In this paper we use QA as a heuristic method to solve the SCP problem. QA was proposed2 for solving optimization problems
using quantum ﬂuctuations, known as quantum tunneling, to escape local minima and discover the lowest energy state. Farhi et
al.3 provide the framework for using Adiabatic Quantum Computation (AQC), which is closely related to QA, as a quantum
paradigm to solve NP-hard optimization problems. The ﬁrst step of the framework is to deﬁne a Hamiltonian HP whose ground
state corresponds to the solution of the combinatorial optimization problem. Then, we initialize a system in the ground state
of some beginning Hamiltonian HB that is easy to solve, and perform the adiabatic evolution H(s) = (1−s)HB +sHP. Here
s ∈[0,1] is a time parameter. In this paper we only consider time-dependent function s(t) = t/T for total evolution time T,
but in general it could be any general functions that satisfy s(0) = 0 and s(T) = 1. The adiabatic evolution is governed by the
Schr¨odinger equation
i d
dt |ψ(t)⟩= H(s(t))|ψ(t)⟩
(1)
where |ψ(t)⟩is the state of the system at any time t ∈[0,T]. Let πi(s) be the i-th instantaneous eigenstate of H(s). In other
words, let H(s)|πi(s)⟩= Ei(s)|πi(s)⟩for any s. In particular, let |π0(s)⟩be the instantaneous ground state of H(s).
According to the adiabatic theorem64, for s varying sufﬁciently slow from 0 to 1, the state of the system |ψ(t)⟩will remain
close to the true ground state |π0(s(t))⟩. At the end of the evolution the system is roughly in the ground state of HP, which
2/19


## Page 3


encodes the optimal solution to the problem. If the ground state of HP is NP-complete to ﬁnd (for instance consider the case for
Ising spin glass49), then the adiabatic evolution H(s) could be used as a heuristic for solving the problem.
An important issue associated with AQC is that the adiabatic evolution needs to be slow enough to avoid exciting the
system out of its ground state at any point. In order to estimate the scaling of the minimum runtime T needed for the adiabatic
computation, criteria based on the minimum gap between the ground state and the ﬁrst excited state of H(s) is often used.
However, here we do not use the minimum gap as an intermediate for estimating the runtime scaling, but instead numerically
integrate the time dependent Schr¨odinger equation (1).
2.3 Quantum Ising model with transverse ﬁeld
The Hamiltonian for an Ising spin glass on N spins can be written as
H =
N
∑
i=1
hiσz
i +
N
∑
i<j
Ji jσz
i σz
j
(2)
where σz
i = I⊗(i−1) ⊗
  1 0
0 −1

⊗I⊗(n−i) acts on the i-th spin with I being a 2×2 identity matrix. hi, Jij are coefﬁcients. The
Hamiltonian is diagonal in the basis {|s⟩∈C2N|s ∈{0,1}N} in the Hilbert space H . In particular σz|0⟩= |0⟩and σz|1⟩= −|1⟩.
We formally deﬁne the problem of ﬁnding the ground state of an N-qubit Ising Hamiltonian in the following.
Deﬁnition 2. (Ising Hamiltonian) Given the Hamiltonian H in equation (2), ﬁnd a quantum state |s⟩∈H , where H is
2N-dimensional, such that the energy E(s) = ⟨s|H|s⟩is minimized. We use the notation ISING(h,J) to refer to the problem
instance where h = (h1,h2,··· ,hN)T and J ∈RN×N is a matrix such that the ij-th and the ji-th elements are equal to Jij/2.
The diagonal elements of J are 0. Hence E(s) = hTp(s)+p(s)TJp(s) where p(s) = 1−2s ∈{−1,1}N.
In this paper, we construct Ising Hamiltonians whose ground state encodes the solution to an arbitrary instance of the SCP
problem. The physical system used for quantum annealing that we assume is identical to that of D-Wave6,7,9,14, namely Ising
spin glass with transverse ﬁeld
H =
N
∑
i=1
∆iσx
i +
N
∑
i=1
hiσz
i +
N
∑
i<j
Ji jσz
i σz
j
(3)
where σx
i = I⊗(i−1) ⊗
  0 1
1 0

⊗I⊗(n−i) acts on the i-th spin. The beginning Hamiltonian HB has its hi,Jij = 0 for all i, j and
the ﬁnal Hamiltonian HP has ∆i = 0 for all i while hi and Jij depend on the problem instance at hand. We will elaborate on
assigning hi and Ji j coefﬁcients in HP in Theorem 1.
2.4 Graph minor embedding
The interactions described by the transverse Ising Hamiltonian in equation (3) are not restricted by any constrains. However, in
practice the topology of interactions is always constrained to the connectivity that the hardware permits. Therefore in order to
physically implement an arbitrary transverse Ising Hamiltonian, one must address the problem of embedding the Hamiltonian
into the logical fabric of the hardware61,62. For convenience we deﬁne the interaction graph of an Ising Hamiltonian H of the
form in equation (2) as a graph GH(VH,EH) such that each spin i maps to a distinctive element vi in VH and there is an edge
between vi and vj iff Ji j ̸= 0. This deﬁnition also applies to the transverse Ising system described in equation (3). We use the
term hardware graph to refer to a graph whose vertices represent the qubits in the hardware and the edges describe the allowed
set of couplings in the hardware.
In Section 2.1 we deﬁned bipartite graphs. Here we deﬁne a complete bipartite graph Km,n as a bipartite graph where
|V1| = m, |V2| = n and each vertex in V1 is connected with each vertex in V2. A graph H(W,F) is a subgraph of G(V,E) if
W ⊆V and F ⊆E. It is possible that the interaction graph of the desired Ising Hamiltonian is a subgraph of the hardware
connectivity graph. In this case the embedding problem can be solved by subgraph embedding, which we deﬁne as the
following.
Deﬁnition 3. A subgraph embedding of G(V,E) into G′(V ′,E′) is a mapping f : V 7→V ′ such that each vertex in V is mapped
to a unique vertex in V ′ and if (u,v) ∈E then (f(u), f(v)) ∈E′.
In more general cases, for an arbitrary Ising Hamiltonian, a subgraph embedding may not be obtainable and we will need to
embed the interaction graph into the hardware as a graph minor. Before we deﬁne minor embedding rigorously, recall that a
graph is connected if for any pair of vertices u and v there is a path from u to v. A tree is a connected graph which does not
contain any simple cycles as subgraphs. T is a subtree of G if T is a subgraph of G and T is a tree. We then deﬁne minor
embedding as the following.
3/19


## Page 4


Figure 1. The Chimera graph that represents the qubit connectivity of D-Wave hardware. (a) Example of a 3×3 grid of K4,4
cells, denoted as F(3,3,4). (b) Labelling of nodes within a particular cell on the a-th row and b-th column. Here we use the
cell on the 2nd row and 3rd column as an example.
Deﬁnition 4. A minor embedding of G(V,E) in G′(V ′,E′) is deﬁned by a mapping φ : V 7→V ′ such that each vertex v ∈V is
mapped to a connected subtree Tv of G′ and if (u,v) ∈E then there exist iu,iv ∈V ′ such that iu ∈Tu, iv ∈Tv and (iu,iv) ∈E′.
If such a mapping φ exists between G and G′, we say G is a minor of G′ and we use G ≤m G′ to denote such relationship.
Our goal is to take the interaction graph GH of our Ising Hamiltonian construction and construct the mapping φ that embeds
GH into the hardware graph as a minor.
2.5 Chimera graphs
Here we speciﬁcally consider the embedding our construction into a particular type of hardware graphs used by D-Wave
devices44,65 called the Chimera graphs. The basic components of this graph are 8-spin unit cells6 whose interactions form a
K4,4. The K4,4 unit cells are tiled together and the 4 nodes on the left half of K4,4 are connected to their counterparts in the
cells above and below. The 4 nodes on the right half of K4,4 are connected to their counterparts in the cells left and right.
Furthermore, we deﬁne F(p,q,c) as a Chimera graph formed by an p ×q grid of Kc,c cells. Figure 1a shows F(3,4) as an
example. Note that any Km,n with m,n ≤c can be trivially embedded in F(p,q,c) with any p,q ≥1 via subgraph embedding.
However, it is not clear a priori how to embed Km,n with m > c or n > c onto a Chimera graph, other than using the general
embedding of an (m+n)-node complete graph and consider Km,n as a subgraph. This costs O((m+n)2) qubits in general and
one may lose the intuitive structure of a bipartite graph in the embedding. One of the building blocks of our embedding for our
Ising Hamiltonian construction (Section 4) is an alternative embedding strategy for mapping any Km,n onto F(⌈n/c⌉,⌈m/c⌉,c)
as a graph minor. Our embedding costs O(mn) qubits and preserves the structure of the bipartite graph.
3 Quantum annealing for solving SCP
3.1 From an arbitrary SCP instance to an Ising Hamiltonian construction
SCP is NP-complete most simply because Set Cover (SC) is a special case of SCP56 and a solution to SCP is clearly efﬁciently
veriﬁable. Since SC is NP-complete itself, any SCP instance can be rewritten as an instance of SC with polynomial overhead.
The Ising Hamiltonian construction for Set Cover is explicitly known39,50. Hence it is natural to consider using the chain of
reductions from SCP to SC and then from SC to ISING (Deﬁnition 2). If we recast each SCP(G,U,S) with |S| = m into an SC
4/19


## Page 5


instance with a cover set of size O(m2). Using the construction by Lucas50 we have an Ising Hamiltonian
H = HA +HB = A
n
∑
α=1
(1−∑
i:α∈Vi
xi)2 +B
N
∑
i=1
xi
(4)
where Vi is the i-th cover set in the SC instance. Since the cover set {Vi} is possibly of size up to O(m2), this leads to the Ising
Hamiltonian in equation (4) costing O(nm2) qubits.
Here we present an alternative Ising Hamiltonian construction for encoding the solution to any SCP instance. We state the
result precisely as Theorem 1 below. The qubit cost of our construction is comparable to that of Lucas. However, in Section 4
we argue that our construction affords more advantages in terms of embedding.
Theorem 1. Given an instance of the Set Cover with Pairs Problem SCP(G,U,S) as in Deﬁnition 1, there exists an efﬁcient
(classical) algorithm that computes an instance of the Ising Hamiltonian ground state problem ISING(h,J) with h ∈RM and
J ∈RM×M where the number of qubits involved in the Hamiltonian is M = O(nm2) with n = |U| and m = |S|.
Proof. First, we recast an SCP instance to an instance of integer programming, which is NP-hard in the worst case. Then,
we convert the integer programming problem to an instance of the ISING problem. Recall Deﬁnition 1 of an SCP(G,U,S)
instance, where G(V,E) is a graph on the vertices V = U ∪S. For each pair fi, f j ∈S deﬁne a set Qij = {ck ∈U|(fi,ck) ∈E
and (f j,ck) ∈E}. The problem can be recast as an integer program by
min
∑
fi∈S
si
(LP)
s.t.
∑
ck∈Qij
ti j ≥1
∀ck ∈U
(LP.1)
tij ≤si and ti j ≤s j
∀fi ̸= f j,where fi, f j ∈S and i < j
(LP.2)
si,tij ∈{0,1}
∀fi ̸= f j,where fi, f j ∈S
(LP.3)
We have introduced the variable si to indicate whether fi is chosen for the cover A ⊆S (si = 1 means that fi is chosen,
otherwise si = 0). We have also introduced the auxiliary variable tij to indicate whether fi and f j are both chosen. Hence,
constraint LP.1 ensures that each element ck ∈U is covered by at least one pair in S. LP.2 ensures that a pair of elements in S
cannot cover any ck ∈U unless both elements are chosen.
To convert the integer program to an ISING instance, we ﬁrst convert the constraints into expressions of logical operations.
LP.1 can be rewritten as
_
ck∈Qij
t(k)
ij = 1,
∀ck ∈U
(5)
LP.2 can be translated to a truth table for the binary operation involving tij and si(s j) where only the entry {si = 0,tij =
1}(sj = 0,tij = 1) evaluates to 0 and the other three entries evaluate to 1. Using the following Hamiltonians we could translate
the logic operations ∨, ∧and ≤into the ground states of Ising model, see66 for more details.
H∨(s1,s2,s∗)
=
1
4(3I−σz
1 −σz
2 +2σz
∗+σz
1σz
2 −2σz
1σz
∗−2σz
2σz
∗)
H∧(s1,s2,s∗)
=
1
4(4I+σz
1 +σz
2 −2σz
∗+2σz
1σz
2 −3σz
1σz
∗−3σz
2σz
∗)
H≤(s1,s2)
=
1
4(I−σz
1 +σz
2 −σz
1σz
2).
(6)
Note that H≤(s1,s2) is essentially |10⟩⟨10|s1s2. In other words we are penalizing the only 2-bit string s1s2 that violates the
constraint s1 ≤s2. The ground state subspace of H∨is spanned by {|s1s2s∗⟩|s1 ∨s2 = s∗,s1,s2,s∗∈{0,1}}. Similarly, the
ground state subspace of H∧is spanned by {|s1s2s∗⟩|s1 ∧s2 = s∗} and that of H≤spanned by {|s1s2⟩|s1 ≤s2}.
By linearly combining the above constraint Hamiltonians, we can enforce multiple constraints to hold at the same time.
For example, the statement s1 ∨s2 ∧s3 = 1 can be decomposed as simultaneously ensuring s1 ∨s2 = y, y ∧s3 = z, and
z = 1. In other words we have used auxiliary variables y and z to transform the constraint s1 ∨s2 ∧s3 = 1, which involves
a clause s1 ∨s2 ∧s3 of three variables, to a set of constraints involving only clauses of two variables. Then, the Ising
Hamiltonian H = H∨(s1,s2,y) + H∧(y,s3,z) + |0⟩⟨0|z has its ground state spanned by states |s1s2s3yz⟩with s1, s2, and s3
satisfying s1 ∨s2 ∧s3 = 1. The third term in H ensures that z = 1 by penalizing states with |z⟩= |1⟩.
5/19


## Page 6


Figure 2. Example of converting an SCP instance to Ising Hamiltonian. (a) The SCP instance. Here S = { f1, f2, f3, f4} and
U = {c1,c2}. The solution is the set A = {f1, f4}. The circles represent the covering set elements S and the squares are the
ground elements U. (b) The interaction of Ising instance HSCP converted from the SCP instance in (a). Every node corresponds
to a qubit. The si’s are the output bits that correspond to the covering set elements S. The others are auxiliary variables. Every
edge represents an interaction term between the corresponding spins. Here we do not show the 1-local terms in our construction
of HSCP (for example the terms in Htarg for enforcing the minimization of the target function). The bold dashed black line
exempliﬁes the edges between the t(k)
i j nodes and the si nodes, which come from the constraints t(k)
ij ≤si and t(k)
ij ≤sj for each
pair { fi, f j} that covers ck. Each of the inequality constraints is enforced by a H≤term in (6). The bold triangle exempliﬁes the
H∨constraints in (6) that are used to enforce the logical relationship between the t(k)
ij variables and the auxiliary variables as
shown in (7). The areas marked by G(1)
1 , G(2)
1
etc outline the structure of the Ising Hamiltonian that is relevant in the discussion
of hardware embedding.
6/19


## Page 7


Therefore, we can translate (5) to an Ising Hamiltonian. For a ﬁxed k, the constraint (5) takes the form of t(k)
1
∨t(k)
2
∨···∨
t(k)
Nk = 1 where each t(k)
j
∈{0,1} and Nk ≤1
2m(m−1) = O(m2). Similarly to the example above, we introduce Nk −1 auxiliary
variables x(k)
1 , x(k)
2 , ···, x(k)
Nk−1 such that
x(k)
j
=



t(k)
1
∨t(k)
2
j = 1
x(k)
j−1 ∨t(k)
j+1
j = 2,··· ,Nk −1
(7)
Thus, x(k)
Nk−1 = t(k)
1
∨t(k)
2
∨···∨t(k)
Nk . In order to ensure the ﬁrst constrain holds, it is needed to ensure that x(k)
Nk−1 = 1. Then we
could write down the corresponding Ising Hamiltonian for the constraint as
Hk = H∨(t(k)
1 ,t(k)
2 ,x(k)
1 )+
Nk−1
∑
j=2
H∨(x(k)
j−1,t(k)
j+1,x(k)
j )+|0⟩⟨0|x(k)
Nk−1.
(8)
The last term is meant to make sure that x(k)
Nk−1 = 1 in the ground state of Hk. Therefore the Hamiltonian whose ground state
subspace is spanned by all states that obey both of the constraints in the integer program (5) can be written as
Hcons
=
∑
ck∈U
Hk +H≤
H≤
=
∑
i,j:fi,f j∈S
(H≤(ti j,si)+H≤(ti j,sj)).
(9)
The target function ∑fi∈S si which we seek to minimize can be directly mapped to an Ising Hamiltonian Htarg = ∑fi∈S |1⟩⟨1|si =
∑fi∈S
1
2(1−σsi). This is because we would like to essentially minimize the number of 1’s in the set of si values and penalize
choices with more 1’s. Therefore the ﬁnal Hamiltonian whose ground state contains the solution to the original SCP instance
becomes
HSCP = αHtarg +Hcons
(10)
for some weight factor α.
We now estimate the overhead for the mapping. Htarg acts on |S| = m qubits. In Hcons, H≤acts on O(m2) qubits, since there
are O(m2) variables ti j. Each Hk in Hcons requires Nk = O(m2) qubits. There are in total |U| = n of the Hk terms, which gives
O(nm2) qubits in total.
□
Example
Consider the SCP instance shown in Figure 2a. With the mapping presented in Theorem 1, we arrive at an Ising in-
stance ISING(h,J) where α = 1/4 in (10) and h, J are presented in Supplementary Material.
The ground state sub-
space of the Hamiltonian in (2) with hi and Ji j coefﬁcients deﬁned above, restricted to the si elements is spanned by
{|ψ⟩= |s1s2 ···x(2)
2 ⟩such that |s1s2s3s4⟩= |1001⟩}. This corresponds to A = { f1, f4}, the solution to the SCP instance.
Figure 2b illustrates the interaction graph of the spins in the Ising Hamiltonian that corresponds to the SCP instance.
3.2 Numerical simulation of quantum annealing
In order to test the time complexity of using quantum annealing to solve SCP instances via the construction in Theorem 1,
we generate random instances of SCP that lead to Ising Hamiltonian HSCP of M = 3,4,··· ,19 spins. In Deﬁnition 1 we use
a bipartite graph between the ground state U of size n and the cover set S of size m to describe an SCP instance. For ﬁxed
n and m, there are in total 2mn such possible bipartite graphs (if we consider each bipartite graph as a subgraph of Km,n and
count the cardinality of the power set of the edges of Km,n). Therefore to generate random bipartite graphs we only need to ﬂip
mn fair coins to uniformly choose from all possibile bipartite graphs between U and S. However, we would like to exclude
the bipartite graphs where some element of S is not connected to any element in U. These “dummy nodes” are not pertinent
to the computational problem at hand and should be removed from consideration before converting the SCP instance to an
Ising Hamiltonian HSCP. We thus use a scheme for generating random instances of SCP without dummy nodes as described in
Algorithm 1. Under the constraint that no dummy element in S is allowed, there are in total (2n −1)m possible bipartite graphs.
In Supplementary Material we rigorously show that Algorithm 1 indeed samples uniformly among the (2n −1)m possible
“dummy-free” bipartite graphs.
For each randomly generated instance from Algorithm 1 we construct an Ising Hamiltonian HSCP according to Theorem 1.
We then perform a numerical simulation of the time dependent Schr¨odinger equation (1) from time t = 0 to t = T with time
7/19


## Page 8


Algorithm 1 Algorithm for generating a random SCP(G,U,S) without dummy elements in the cover set
Input: The ground set U and the cover set S
Procedure:
1: Initialize the output graph G ←/0;
2: for all s ∈S do
3:
for all u ∈U do
4:
With probability 1/2, add edge (s,u) to G;
5:
end for
6:
if s is still unattached to any element in U then
7:
Repeat steps 3 through 5 until s is attached to some element in U.
8:
end if
9: end for
10: return G.
step ∆t = 1 and the time dependent Hamiltonian deﬁned as
H(s(t))
=

1−t
T

HB + t
T HSCP
HB
=
M
∑
i=1
σx
i
(11)
where HSCP is deﬁned in equation (10). Here because of the construction of HSCP, our total Hamiltonian H(s(t)) acts not only
on the spins s ∈{0,1}m indicating our choice of elements in the cover set S, but also auxiliary variables t(k)
ij and x(k)
i , for which
we use t and x to denote their respective collections. Our initial state is the ground state of HB, namely
|ψ(0)⟩=
1
√
2M
∑
s,t,x∈{0,1}M
|s,t,x⟩.
(12)
To obtain the ﬁnal state |ψ(T)⟩where T is some positive integer, we use the ode45 subroutine of MATLAB under default
settings to numerically integrate Schr¨odinger equation to obtain |ψ(1)⟩from |ψ(0)⟩, and then use |ψ(1)⟩as an initial state to
obtain |ψ(2)⟩in the same fashion, and so on. We deﬁne the success probability p as a function of the total annealing time T as
p(T) = ∥Π|ψ(T)⟩∥2 where Π is a projector onto the subspace spanned by states with s being a solution of the original SCP
instance. Using binary search we determine the minimum time T ∗to achieve p(T ∗) ≥0.25 for each instance of SCP. Figure
3 shows the distribution of T ∗for SCP instances that lead to Ising Hamiltonians HSCP of the same sizes, as well as how the
median annealing time scales as a function of number of spins M. Results show that for instances with M up to 19, the median
annealing time scales roughly as O(20.31M).
3.3 Numerical experiment with Simulated Annealing
Simulated annealing, ﬁrst introduced three decades ago67, has been widely used as a heuristic for handling hard combinatorial
optimization problems. It is especially of interest as a benchmark for quantum annealing34–36 because of similarities between
the two algorithms. While quantum annealing employs quantum tunneling to escape from local minima, simulated annealing
relies on thermal excitation to avoid being trapped in local minima. The general procedure we adopt for simulated annealing to
approach the ground state of an Ising spin glass can be summarized as the following68:
1. Repeat R times the following:
(a) Initialize s ←s0 randomly;
(b) Perform S times the following: (let i = 0,1,··· ,S−1 index the steps)
i. Set the temperature Ti ←τ(i);
ii. Perform a sweep on si to obtain s′; (a sweep is a sequence of steps each of which randomly selects a spin and
ﬂips its state, so that on average each spin is ﬂipped once during a sweep)
iii. With probability exp( E(s′)−E(s)
Ti
), let si+1 = s′. Otherwise let si+1 ←si.
8/19


## Page 9


Figure 3. Plot of the optimal quantum annealing time T ∗versus the number of spins involved in the construction of HSCP.
Here we ﬁt the logarithm of median T ∗with a straight line. The size M of our Ising systems ranges from 3 to 19. From the
ﬁtting function we observe that the annealing time scales as roughly O(20.31M). We also provide on the bottom plot the number
of instances for each M.
9/19


## Page 10


2. Return sS as the answer.
For the purpose of comparison we also used simulated annealing to solve the same set of instances generated by Algorithm
1 for testing quantum annealing. The program implementation that we use is built by Isakov et al68, which is a highly optimized
implementation of simulated annealing with care taken to exploit the structures of the interaction graph, such as being bipartite
and of bounded degree. Here we use the program’s most basic realization of single-spin code for general interactions with
magnetic ﬁeld on an interaction graph of any degree.
As mentioned by Isakov et al., to improve the solution returned by simulated annealing, one could increase either the
number of sweeps S or number of repetitions R in the implementation, or both of them. However, note that the total annealing
time is proportional to the product S·R and there is a trade-off between S and R. For a ﬁxed number of sweeps S let the success
probability (i.e. the fraction of si that is satisfactory) be w(S). In order to achieve a constant success probability p (say 25%,
which is what we use here), we need at least R = ⌈log(1−p)/log(1−w(S))⌉repetitions. Hence the total time of simulated
annealing can be written as
T(S) =

log(1−p)
log(1−w(S))

·S.
(13)
In general w(S) increases as S increases, leading to a decrease in R. We numerically investigate this with an Ising system of
N = 17 spins generated from an SCP instance via the construction in Theorem 1. We plot the annealing time T versus S in
Figure 4a. For each SCP instance with the number of spin M we compute the optimal S∗such that T ∗= T(S∗) is the optimized
runtime (Figure 4a). We further explore how the optimal runtime T ∗scales as a function of the number of spins M. As shown
in Figure 4b, a linear ﬁt on a semilog plot shows that roughly T ∗= O(20.21M).
The units of time used for both Figure 4a and Figure 4b are arbitrary and thus do not support a point-to-point comparison.
But the scaling difference seems apparent. For quantum annealing we restrict to systems of at most 19 spins due to computational
limitations faced in representing the full Ising Hamiltonian when numerically integrating the time-dependent Schr¨odinger
equation (1).
Although there is no quantum speedup observed in terms of median runtime over all randomly generated instances of the
same size, we notice that for a ﬁxed number of spins M the performances of both quantum annealing and simulated annealing
are sensitive to the speciﬁc instance of Ising Hamiltonian HSCP than simulated annealing. This can be seen by considering at
the same time the quantum annealing results in Figure 3 and the test results for simulated annealing shown in Figure 4b. One
could then speculate that perhaps by focusing on a speciﬁc subset of SCP instances could yield a quantum advantage.
4 Embedding on quantum hardware
In this section we deal with the physical realization of quantum annealing for solving SCP instances using D-Wave type
hardwares. There are mainly two aspects62,69 of this effort: 1) The embedding problem62, namely embedding the interaction
graph of the Ising Hamiltonian construction HSCP as a graph minor of a Chimera graph (refer to Section 2.4 for deﬁnitions
of the graph terminologies). 2) The parameter setting problem69, namely assigning the strengths of the couplings and local
magnetic ﬁelds for embedded graph on the hardware, in a way that minimizes the energy scaling (or control precision) required
for implementing the embedding. Here we focus on the former issue.
We start with an observation on the structures of HSCP. For any instance SCP(G,U,S) according to Deﬁnition 1, the
interaction graph ISCP(G,U,S) of the corresponding Ising Hamiltonian HSCP can be regarded as a union of n subgraphs, namely
ISCP(G,U,S) = G(1) ∪G(2) ∪···∪G(n). Each subgraph G(i) is associated with an element of the ground set ci ∈U as in Figure
2a. Each G(i) could be further partitioned into two parts, G(i)
1 and G(i)
2 . For any k, G(k)
1
is a bipartite graph between {si}m
i=1
and {t(k)
ij |fi, f j ∈S cover ck ∈U}. G(k)
2
essentially describes the interaction between the auxiliary variables t(k)
ij
and x(k)
i
as
described in equation (7). In Figure 2b we illustrate such partition using the example from Figure 2b. Our goal is then to show
constructively that ISCP(G,U,S) ≤m F(f1, f2,c) for some f1, f2 that depend on m, n and c = 4, which describes the Chimera
graph realized by D-Wave hardware (Figure 1a).
It is known61 that one could embed a complete graph on cm+1 nodes onto Chimera graph F(m,m,c). Since any n-node
graph is a subgraph of the n-node complete graph, in principle any n-node graph can be embedded onto Chimera graphs of size
O(n2) using the complete graph embedding. A downside of this approach is that it may fail to embed many graphs that are in
fact embeddable61. Also, using embeddings based on complete graph embeddings will likely lose the intuition on the structure
of the original graph. For graphs with speciﬁc structures, such as bipartite graphs one may be able to ﬁnd an embedding that is
also in some sense structured. We show in the following Lemma an embedding for any complete bipartite graph Kp,q onto a
Chimera graph. The ability to do so enables us to embed any bipartite graph onto a Chimera graph.
Lemma 1. For any positive integers p, q and c, Kp,q ≤m F(⌈q/c⌉,⌈p/c⌉,c).
10/19


## Page 11


Figure 4. (a) Plot of annealing time T versus number of sweeps S using the simulated annealing implementation68 on an Ising
Hamiltonians of 17 spins constructed from an SCP instance. We use the default settings for all parameters other than S and R.
Also we mark the optimal runtime T∗. (b) Plot of optimized annealing time T ∗versus the number of spins involved in the Ising
Hamiltonian HSCP corresponding to randomly generated SCP instances according to Algorithm 1. We also provide on the
bottom plot the number of instances for each M.
Proof. By the deﬁnition of graph minor embedding in Section 2.4, it sufﬁces to construct a mapping φp,q : Kp,q 7→F(⌈q/c⌉,⌈p/c⌉,c)
where each v in Fp,q is mapped to a tree Tv in F(⌈q/c⌉,⌈p/c⌉,c) and each edge e = (u,v) in Kp,q is mapped to an edge (iu,iv)
with iu ∈Tu and iv ∈Tv.
Let i = 1,2,··· , p label the nodes on one side of Kp,q and j′ = 1,2,··· ,q label the nodes in the other. Using the labelling
scheme on the nodes of Chimera graphs introduced in Section 2.5 and Figure 1b, we deﬁne our mapping φp,q as
φp,q(i)
=
{v(t,⌈i/c⌉)
i mod c |t = 1,··· ,⌈q/c⌉}
φp,q(j′)
=
{v(⌈j′/c⌉,t)
c+(j′ mod c)|t = 1,··· ,⌈p/c⌉}.
φp,q(i, j′)
=

v(⌈i/c⌉,⌈j′/c⌉)
i mod c
,v(⌈i/c⌉,⌈j′/c⌉)
c+(j′ mod c)

(14)
where φp,q(u,v) maps an edge (u,v) in Kp,q to the Chimera graph. If we choose the edges in the Chimera graph properly, it
could be checked that φp,q(Kp,q) is a subgraph of F(⌈q/c⌉,⌈p/c⌉,c).
In Figure 5 we show an example of embedding K7,10 into F(3,2,4). A natural corollary of Lemma 1 is that any bipartite
graph between p and q nodes can be minor embedded in F(⌈q/c⌉,⌈p/c⌉,c). We are then prepared to handle embedding the
G(i)
1 parts of the interaction graphs of HSCP, which are but bipartite graphs (see Figure 2b for example).
We then proceed to treat the G(i)
2 parts of the interaction graph. The connectivity of G(k)
2
is completely speciﬁed by
(7). To describe such connectivity we deﬁne a family of graph Ln(Vn,En) as Vn = Tn ∪Xn−1 where Tn = {t1,t2,··· ,tn} and
Xn−1 = {x1,x2,··· ,xn−1} are two disjoint sets of nodes, the former representing the intermediate variables t(k)
ij and the latter
11/19


## Page 12


Figure 5. An example showing the embedding scheme outlined in Lemma 1. The nodes and the trees mapped from the nodes
are marked with the same colors.
representing the xk variables in equation (7). The set of edges takes the form
En = {(t1,t2),(t1,x1),(t2,x1)}∪
 n−1
[
i=2
{(xi−1,xi),(xi−1,ti+1),(xi,ti+1)}
!
.
(15)
In Figure 6 we show an example of L10. For any k = 1,2,··· ,|U|, let rk be the number of pairs fi, f j ∈S that cover k. Then
G(k)
2
= Lrk. Hence in order to show that we could embed any G(i)
2 onto a Chimera graph, it sufﬁces to show that we can embed
any Ln onto a Chimera graph. We show this in the following Lemma for c = 4.
Lemma 2. For any positive integer n, Ln ≤m F(⌈2n/c⌉,2,c) where we restrict to c = 4.
Proof. Similar to Lemma 1, we construct a mapping µn : Ln 7→F(⌈2n/c⌉,2,c) where we ﬁx c = 4. Following the notation for
nodes in Ln in Figure 6 and the notation for nodes in F(p,q,c) in Figure 1b, we construct µ as
µn(ti)
=
{v
(⌈2i−1
c
⌉,1)
(2i−1) mod c,v
(⌈2i−1
c
⌉,1)
c+[(2i−1) mod c]}∪ξt(ti)
µn(xi)
=
{v
(⌈2i
c ⌉,1)
(2i) mod c,v
(⌈2i
c ⌉,1)
c+[(2i) mod c],v
(⌈2i
c ⌉,2)
c+[(2i) mod c]}∪ξx(xi)
(16)
where ξt and ξx are deﬁned as
ξt(ti) =



/0
if i = 1,2
{v
(⌈2i−1
c
⌉,2)
c+[(2i−1) mod c]}
otherwise.
(17)
ξx(xi) =











{v
(⌈2i
c ⌉,2)
(2i) mod c,v
(⌈2i
c ⌉+1,2)
(2i) mod c }
if ⌈i/2⌉mod 2 = 1 and 2i+4 < 2n−1
{v
(⌈2i
c ⌉,2)
[(2i) mod c]−1,v
(⌈2i
c ⌉+1,2)
[(2i) mod c]−1}
if ⌈i/2⌉mod 2 = 0 and 2i+4 < 2n−1
/0
otherwise.
(18)
With the vertex mapping µn, a mapping of edges in Ln onto the Chimera graph F(⌈2n/c⌉,2,c) is easy to ﬁnd.
12/19


## Page 13


Figure 6. An example of embedding L10 onto F(5,2,4). Each color in the left diagram represents a node u in L10 and the
nodes of the same color in the right diagram shows µ10(u).
13/19


## Page 14


In Figure 6 we show an example of embedding L10 onto F(5,2,4). We could then proceed to embed the interaction graph
ISCP(G,U,S), such as the one shown in Figure 2b, in a Chimera graph. Speciﬁcally, we state the following theorem.
Theorem 2. For any instance SCP(G,U,S) with |U| = n and |S| = m, ISCP(G,U,S) ≤m F(f1, f2,c) where f1 = O(nm2), f2 =
O(m) and c = 4 is a constant.
Proof. Our embedding combines ideas from Lemma 1 and 2. We modify the mapping φp,q constructed in Lemma 1 to produce
a new mapping θp,q that produces more spacing between the embedded nodes (see for example G(1)
1
and G(2)
1
in Figure 7):
θp,q(i)
=
{v(t,⌈(2i−1)/c⌉)
(2i−1) mod c |t = 1,··· ,⌈q/c⌉}
θp,q(j′)
=
{v(⌈(2 j′−1)/c⌉,t)
c+(2j′−1 mod c)|t = 1,··· ,⌈p/c⌉}
(19)
Let µ(r,s)
n
denote a mapping µ described in Lemma 2 that maps the upper left node (Figure 6) t1 to v(r,s)
1
instead of v(1,1)
1
. The
rest of the mapping then proceeds from v(r,s)
1
. In other words, µ(r,s)
n
is the mapping µ that is shifted by p−1 cells to the right and
q−1 cells below. Trivially µ(1,1)
n
= µ. Similarly we deﬁne θ (r,s)
p,q as the shifted embedding under θp,q where θ (r,s)
p,q (1) = v(r,s)
1
.
Recall that for any ground set element ck ∈U, rk is the number of pairs in S that covers ck. We could then specify the embedding
from ISCP(G,U,S) onto F(f1, f2,c) as
Φ(si)
=
n[
j=1
θ
(1+dj,1)
m,ri
(i), where i = 1,··· ,m
Φ(t(j)
i
)
=
θ
(1+dj,1)
m,ri
(ti)∪µ
(1+dj,1+⌈2m/c⌉)
rj
(ti), where i = 1,··· ,rj and j = 1,··· ,n
Φ(x(j)
i )
=
µ
(1+d j,1+⌈2m/c⌉)
r j
(ti), where i = 1,··· ,rj −1 and j = 1,··· ,n
(20)
where dj = ∑j−1
k=1⌈2rk/c⌉is the total number of rows of cells occupied by the embedded graphs for handling the ground elements
c1 through cj−1. In total Φ(ISCP(G,U,S)) will occupy f1 = ∑n
k=1⌈2rk/c⌉≤n(m
2 )·2/c = O(nm2) rows and f2 = ⌈2m/c⌉+2 =
O(m) columns.
In Figure 7 we show an embedding ISCP(G,U,S) of the example instance in Figure 2 onto F(4,4,4). Note that our embedding
preserves the original structure of the interaction graph as shown in Figure 2b. Furthermore, note that the interaction graph
ISCP(G,U,S) has M = O(nm2) nodes. Using the complete graph embedding requires O(M2) = O(n2m4) qubits. For the same
reason, the construction of Ising Hamiltonian described in equation (4) is likely going to cost O(nm4) in the worst case of
embeding in a Chimera graph since the interaction graph of the Hamiltonian could involve complete graphs of size O(m2)
due to the square term HA. By comparison our embedding costs f1 f2 ·2c = O(nm3) qubits and preserves the structure of the
original instance, which affords slightly more advantage for scalable physical implementations.
5 Discussion
Our interest in SCP is largely motivated by its important applications in various areas57–60. We have shown a complete pipeline
of reductions that converts an arbitrary SCP instance to an interaction graph on a D-Wave type hardware based on Chimera
graphs, in a way that preserves the structure of the instance throughout (Figure 2b and 7) and is more qubit efﬁcient than the
usual approach by complete graph embedding. Although no quantum speedup is observed at this stage based on comparison
of median annealing times, the large variance of runtimes observed in Figure 3a from instance to instance might suggest that
speciﬁc subsets of instances could provide quantum speedup. Of course, a clearer understanding of the performance of quantum
annealing on solving SCP could only be brought forth by both scaling up the numerical simulation of the quantum annealing
process to include instances with larger number of spins and actual experimental implementation of the quantum annealing
process. Both of them are of interest to us in our future work.
References
1. Finnila, A. B., Gomez, M. A., Sebenik, C., Stenson, C. & Doll, J. D. Quantum annealing: A new method for minimizing
multidimensional functions. Chemical Physics Letter 219, 343–348 (1994).
2. Kadowaki, T. & Nishimori, H. Quantum annealing in the transverse ising model. Physical Review E 58, 5355 (1998).
3. Farhi, E. et al. A quantum adiabatic evolution algorithm applied to random instances of an NP-complete problem. Science
292, 472–475 (2001).
14/19


## Page 15


Figure 7. Embedding the interaction graph of the example physical system in Figure 2b onto F(4,4,4). Note that the
structure of Figure 2 is preserved on the Chimera graph.
15/19


## Page 16


4. Das, A. & Chakrabarti, B. K. Quantum annealing and related optimization methods, vol. 679 (Springer Science & Business
Media, 2005).
5. Das, A. & Chakrabarti, B. K. Quantum annealing and analog quantum computation. Review of Modern Physics 80, 1061
(2008).
6. Harris, R. et al. Experimental investigation of an eight-qubit unit cell in a superconducting optimization processor. Physical
Review B 82, 024511 (2010).
7. Johnson, M. W. et al. Quantum annealing with manufactured spins. Nature 473, 194–198 (2011).
8. Bapst, V., Foini, L., Krzakala, F., Somerjian, G. & Zamponi, F. The quantum adiabatic algorithm applied to random
optimization problems: The quantum spin glass perspective. Physics Reports 523, 127–205 (2013).
9. Dickson, N. G. et al. Thermally assisted quantum annealing of a 16-qubit problem. Nature Communications 4, 1903
(2013).
10. Boixo, S. et al. Evidence for quantum annealing with more than one hundred qubits. Nature Physics 10, 218–224 (2014).
11. McGeoch, C. C. & Wang, C. Experimental evaluation of an adiabiatic quantum system for combinatorial optimization. In
Proceedings of the ACM International Conference on Computing Frontiers (New York, USA, 2013).
12. Dash, S. A note on QUBO instances deﬁned on Chimera graphs (2013). ArXiv:1306.1202 [math.OC].
13. Boixo, S., Albash, T., Spedalieri, F. M., Chancellor, N. & Lidar, D. A. Experimental signature of programmable quantum
annealing. Nature Communications 4, 3067 (2013).
14. Lanting, T. et al. Entanglement in a quantum annealing processor. Physical Review X 4, 021041 (2014).
15. Santra, S., Quiroz, G., Steeg, G. V. & Lidar, D. MAX 2-SAT with up to 108 qubits. New Journal of Physics 16, 045006
(2014).
16. Rønnow, T. F. et al. Deﬁning and detecting quantum speedup. Science 345, 420 (2014).
17. Vinci, W. et al. Hearing the shape of the ising model with a programmable superconducting-ﬂux annealer. Scientiﬁc Report
4, 5703 (2014).
18. Shin, S. W., Smith, G., Smolin, J. A. & Vazirani, U. How “quantum” is the D-Wave machine? (2014). ArXiv:1401.7087
[quant-ph].
19. Albash, T., Vinci, W., Mishra, A., Warburton, P. A. & Lidar, D. A. Consistency tests of classical and quantum models for a
quantum annealer. Physical Review A 91, 042314 (2015).
20. McGeoch, C. In Adiabatic Quantum Computation and Quantum Annealing: Theory and Practice (Morgan & Claypool).
21. Venturelli, D. et al. Quantum optimization of fully-connected spin glasses. Physical Review X 5, 031040 (2015).
22. Vinci, W., Albash, T., Paz-Silva, G., Hen, I. & Lidar, D. A. Quantum annealing correction with minor embedding. Physical
Review A 92, 042310 (2015).
23. Albash, T., Rønnow, T. F., Troyer, M. & Lidar, D. A. Reexamining classical and quantum models for the D-Wave One
processor. The European Physical Journal Special Topics 224, 111 (2015).
24. King, A. D. & McGeoch, C. C. Algorithm engineering for a quantum annealing platform (2014). ArXiv:1410.2628
[cs.DS].
25. Crowley, P. J. D., Duric, T., Vinci, W., Warburton, P. A. & Green, A. G. Quantum and classical in adiabatic computation.
Physical Review A 90, 042317 (2014).
26. Hen, I. et al. Probing for quantum speedup in spin glass problems with planted solutions. Physical Review A 92, 042325
(2015).
27. Steiger, D. S., Rønnow, T. F. & Troyer, M. Heavy tails in the distribution of time-to-solution for classical and quantum
annealing. Physical Review Letters 115, 230501 (2015).
28. Bauer, B., Wang, L., Piˇzorn, I. & Troyer, M. Entanglement as a resource in adiabatic quantum optimization (2015).
29. Albash, T., Hen, I., Spedalieri, F. M. & Lidar, D. A. Reexamination of the evidence for entanglement in the d-wave
processor. Physical Review A 92, 062328 (2015).
30. Katzgraber, H. G., Hamze, F., Zhu, Z., Ochoa, A. J. & Munoz-Bauza, H. Seeking quantum speedup through spin glasses:
The good, the bad, and the ugly. Physical Review X 5, 031026 (2015).
31. Chancellor, N., Szoke, S., Vinci, W., Aeppli, G. & Warburton, P. A. Maximum-entropy inference with a programmable
annealer. Scientiﬁc Report 22318 (2016).
16/19


## Page 17


32. Perdomo-Ortiz, A., O’Gorman, B., Fluegemann, J., Biswas, R. & Smelyanskiy, V. N. Determination and correction of
persistent biases in quantum annealers arXiv:1503.05679 [quant–ph] (2015).
33. Vinci, W., Albash, T. & Lidar, D. A. Nested quantum annealing correction arXiv:1511.07084 [quant–ph] (2015).
34. Farhi, E., Goldstone, J. & Gutmann, S. Quantum adiabatic evolution algorithms versus simulated annealing. MIT-CTP-3228
(2002).
35. Santoro, G. E., Martoˇn´ak, R., Tosatti, E. & Car, R. Theory of quantum annealing of an Ising spin glass. Science 295,
2427–2430 (2002).
36. Heim, B., Rønnow, T. F., Isakov, S. V. & Troyer, M. Quantum versus classical annealing of ising spin glasses. Science 348,
215–217 (2014).
37. Farhi, E., Goldstone, J., Gutmann, S. & Sipser, M. Quantum computation by adiabatic evolution. MIT-CTP-2936 (2000).
38. Farhi, E., Goldstone, J. & Gutmann, S. A numerical study of the performance of a quantum adiabatic evolution algorithm
for satisﬁability. MIT-CTP-3006 (2000).
39. Choi, V. Adiabatic quantum algorithms for the NP-complete Maximum-Weight Independent set, Exact Cover and 3SAT
problems (2010). ArXiv:1004.2226.
40. Childs, A. M., Farhi, E., Goldstone, J. & Gutmann, S. Finding cliques by quantum adiabatic evolution. Quantum
Information and Computation 2 (2002). MIT-CTP #3067.
41. Peng, X. et al. Quantum adiabatic algorithm for factorization and its experimental implementation. Physical Review
Letters 101, 220405 (2008).
42. Hen, I. & Young, A. P. Solving the graph-isomorphism problem with a quantum annealer. Physical Review A 86, 042310
(2012).
43. Gaitan, F. & Clark, L. Graph isomorphism and adiabatic quantum computing. Physical Review A 89, 022342 (2014).
44. Bian, Z., Chudak, F., Macready, W. G., Clark, L. & Gaitan, F. Experimental determination of ramsey numbers. Physical
Review Letters 111, 130505 (2013).
45. Neven, H., Denchev, V. S., Rose, G. & Macready, W. G. Training a binary classiﬁer with the quantum adiabatic algorithm
(2008). ArXiv:0811.0416.
46. Denchev, V. S., Ding, N., Vishwanathan, S. & Neven, H. Robust classiﬁcation with adiabatic quantum optimization (2012).
ArXiv:1205.1148.
47. Roland, J. & Cerf, N. J. Quantum search by local adiabatic evolution. Physical Review A 65, 042308 (2002).
48. Garnerone, S., Zanardi, P. & Lidar, D. A. Adiabatic quantum algorithm for search engine ranking. Physical Review Letters
108, 230506 (2012).
49. Barahona, F. On the computational complexity of ising spin glass models. Journal of Physics A: Mathematical and
General 15, 3241 (1982). URL http://stacks.iop.org/0305-4470/15/i=10/a=028.
50. Lucas, A. Ising formulations of many NP problems (2013). ArXiv:1302.5843.
51. Crosson, E., Farhi, E., Lin, C. Y.-Y., Lin, H.-H. & Shor, P. Different strategies for optimization using the quantum adiabatic
algorithm (2014). ArXiv:1401.7320.
52. Aaronson, S. BQP and the polynomial hierarchy. Proceedings of the forty-second ACM Symposium on Theory of Computing
(STOC) 141–150 (2010).
53. Nagaj, D., Somma, R. D. & Kieferova, M. Quantum Speedup by Quantun Annealing. Phys. Rev. Lett. 109, 050501 (2012).
54. Denchev, V. S. et al. What is the computational value of ﬁnite range tunneling? (2015). ArXiv:1512.02206.
55. Karp, R. M. Reducibility among Combinatorial Problems: Proceedings of a symposium on the Complexity of Computer
Computations 85–103 (1972).
56. Hassin, R. & Segev, D. The Set Cover with Pairs Problem. Lecture Notes in Computer Science 3821, 164–176 (2005).
57. Breslau, L. et al. Disjoint-path Facility Location: Theory and Practice. Proceedings of the Thirteenth Workshop on
Algorithm Engineering and Experiments (ALENEX) 60–74 (2011).
58. Lancia, G., Pinotti, C. M. & Rizzi, R. Haplotyping populations by pure parsimony: Complexity, exact and approximation
algorithms. INFORMS Journal on Computing 16, 348–359 (2004).
59. Wang, I.-L. & Yang, H.-E. Haplotyping populations by pure parsimony based on compatible genotypes and greedy
heuristics. Applied Mathematics and computation 217, 9798–9809 (2011).
17/19


## Page 18


60. Gonc¸alves, L. B., de Lima Martins, S., Ochi, L. S. & Subramanian, A. Exact and heuristic approaches for the set cover
with pairs problem. Optimization Letters 6, 641–653 (2012).
61. Klymko, C., Sullivan, B. D. & Humble, T. S. Adiabatic quantum programming: Minor embedding with hard faults (2012).
ArXiv:1210.8395 [quant-ph].
62. Choi, V. Minor-embedding in adiabatic quantum computation: II. Minor-universal graph design. Quantum Information
Processing 10, 343–353 (2011).
63. Bian, Z. et al. Discrete optimization using quantum annealing on sparse ising models. Frontiers in Physics 2 (2014).
64. Messiah, A. Quantum Mechanics:Volume 2 (North-Holland Publishing Company, 1962).
65. Perdomo-Ortiz, A., Dickson, N., Drew-Brook, M., Rose, G. & Aspuru-Guzik, A. Finding low-energy conformations of
lattice protein models by quantum annealing. Scientiﬁc Reports 2 (2012).
66. Biamonte, J. D. Nonperturbative k-body to two-body commuting conversion hamiltonians and embedding problem
instances into ising spins. Physical Review A 77, 052331 (2008).
67. Kirkpatrick, S., Gelatt, C. D. & Vecchi, M. P. Optimization by simulated annealing. Science 220, 671–680 (1983).
68. Isakov, S. V., Zintchenko, I. N., Ronnow, T. F. & Troyer, M. Optimised simulated annealing for ising spin glasses. Computer
Physics Communications, 192 265–271 (2015).
69. Choi, V. Minor-embedding in adiabatic quantum computation: I. The Parameter setting problem. Quantum Information
Processing 7, 193–209 (2008).
Acknowledgements
The authors thank Sergei Isakov for helpful discussions on the simulated annealing code, and Howard J. Karloff for the original
discussion on the disjoint path facility location problem.
6 Appendix
6.1 Details of the example SCP instance
In the paper we consider an example SCP instance for illustrating our mappings from SCP to Ising and eventually to a Chimera
graph. Speciﬁcally, the ISING(h,J) described in Figure 2b has
hT = 1
8 ·
 s1
s2
s3
s4
t(1)
12
t(1)
14
t(1)
24
t(2)
13
t(2)
14
t(2)
34
x(1)
1
x(1)
2
x(2)
1
x(2)
2
7
3
3
7
−6
−6
−6
−6
−6
−6
2
4
2
4

.
Here the labels above each element of h indicates which spin the coefﬁcient is associated to. The matrix of interaction
coefﬁcients J is shown in Figure 8.
6.2 Proof of correctness for Algorithm 1
Here we show that Algorithm 1 indeed samples uniformly from all (2n −1)m possible “dummy-free” bipartite graphs for a ﬁxed
setting of the ground set U of size n and cover set S of size m. Formally we say a bipartite graph G(U ∪S,E) between two sets
U and S is dummy-free if for any s ∈S there exists at least one u ∈U such that (s,u) ∈E. Then we state the following claim.
Claim 1. Given any set U of n elements and S of m elements, for any dummy-free bipartite graph G(V,E) between U and S,
Algorithm 1 generates G with probability (2n −1)−m.
Proof. Let Pr(G) be the probability that Algorithm 1 generates G. Recall that if at a particular s ∈S during the looping on line
2, when Algorithm 1 scanned through all u ∈U but did not end up selecting any element in U, the algorithm enters line 7 to
repeat the process from scratch for s. Then depending on how many times the algorithm entered line 7 during the process of
generating G, we could express Pr(G) as
Pr(G) =
∞
∑
k=0
Pr(G|Algorithm 1 entered line 7 in total k times)
(22)
If the algorithm never entered line 7 and generated G, then the probability of generating G is essentially the probability of mn
coin ﬂips, namely 2−mn. If the algorithm entered line 7 once, then the probability Pr(G) = 2−mn ·m2−n, where the extra factor
m2−n is essentially the probability of one hit and m−1 misses during m independent Bernoulli trial with the hit probability 2−n
18/19


## Page 19


J
=
1
8 ·


































s1
s2
s3
s4
t(1)
12
t(1)
14
t(1)
24
t(2)
13
t(2)
14
t(2)
34
x(1)
1
x(1)
2
x(2)
1
x(2)
2
s1
−1
−1
−1
−1
s2
−1
−1
s3
−1
−1
s4
−1
−1
−1
−1
t(1)
12
−1
−1
1
−2
t(1)
14
−1
−1
1
−2
t(1)
24
−1
−1
1
−2
t(2)
13
−1
−1
1
−2
t(2)
14
−1
−1
1
−2
t(2)
34
−1
−1
1
−2
x(1)
1
−2
−2
1
−2
x(1)
2
−2
−2
x(2)
1
−2
−2
1
−2
x(2)
2
−2
−2


































(21)
Figure 8. The matrix of coupling coefﬁcients in the Ising Hamiltonian instance constructed for the example SCP instance
shown in Figure 2. The interpretation of the matrix elements of J follows Deﬁnition 2.
(if we regard the event of entering line 7 as a hit). Carrying this argument to the general case if the algorithm enters line 7 k
times, then we need to consider all possible ways of distributing the k hits onto the m iterations on line 2. This gives
Pr(G|Algorithm 1 entered line 7 in total k times) =
∑
(k1,···,km)
2−mn ·

k
k1,k2,··· ,km

·(2−n)k1+k2+···+km
(23)
where the summation is over the set of non-negative integers k1 through km that sums up to k. Then Equation 22 leads to
Pr(G)
=
2−mn ·
∞
∑
k=0
∑
(k1,···,km)
2−kn

k
k1,··· ,km

=
2−mn(1+2−n +2−2n +···)m
=
2−mn

1
1−2−n
m
=
(2n −1)−m.
(24)
19/19

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1608_08547v1_solving_set_cover_with_pairs_problem_using_quantum_annealing
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1608_08547V1_SOLVING_SET_COVER_WITH_PAIRS_PROBLEM_USING_QUANTUM_ANNEALING.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

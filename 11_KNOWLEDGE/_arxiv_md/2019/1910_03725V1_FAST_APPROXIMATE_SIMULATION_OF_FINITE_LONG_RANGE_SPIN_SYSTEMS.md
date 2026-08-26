---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1910.03725v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1910.03725v1_Fast_approximate_simulation_of_finite_long-range_spin_systems

> Source: 1910.03725v1_Fast_approximate_simulation_of_finite_long-range_spin_systems.pdf

> Pages: 38

---


## Page 1


Fast approximate simulation of ﬁnite
long-range spin systems
Ross McVinish† and Liam Hodgkinson∗†
School of Mathematics and Physics
University of Queensland
St. Lucia, Brisbane
Queensland, 4072
Australia
e-mail: r.mcvinish@uq.edu.au
liam.hodgkinson@uqconnect.edu.au
Abstract: Tau leaping is a popular method for performing fast approxi-
mate simulation of certain continuous time Markov chain models typically
found in chemistry and biochemistry. This method is known to perform
well when the transition rates satisfy some form of scaling behaviour. In
a similar spirit to tau leaping, we propose a new method for approximate
simulation of spin systems which approximates the evolution of spin at each
site between sampling epochs as an independent two-state Markov chain.
When combined with fast summation methods, our method oﬀers consid-
erable improvement in speed over the standard Doob-Gillespie algorithm.
We provide a detailed analysis of the error incurred for both the number
of sites incorrectly labelled and for linear functions of the state.
MSC 2010 subject classiﬁcations: Primary 60H35; secondary 60K35,
65C99.
Keywords and phrases: Tau-leaping, simulation, spin system, error anal-
ysis, rate of convergence, mean-ﬁeld models.
1. Introduction
Finite spin systems are continuous-time Markov chains on {0, 1}S, where S is a
ﬁnite collection of sites, and the value at only one site changes in each transition.
Special cases include the contact process, voter model and Ising model. While
great advances have been made in the analysis of these systems in relation to
qualitative issues such as phase transitions, rates of convergence, and central
limit theorems [26, 27, 28], to address more quantitative questions it is often
necessary to employ simulation. As a ﬁnite-state continuous-time Markov chain,
sample paths can be constructed from the jump chain and holding time distri-
bution based on the work of Doob [10, 11]. In the chemistry and biochemistry
literature this algorithm is often referred to as the Gillespie algorithm following
[15, 16]; in the sequel, shall be referred to as the Doob–Gillespie algorithm.
∗Supported by an Australian Postgraduate Award.
†All authors are supported in part by the Australian Research Council (Discovery Grant
DP150101459 and the ARC Centre of Excellence for Mathematical and Statistical Frontiers,
CE140100049).
1
arXiv:1910.03725v1  [math.PR]  9 Oct 2019


## Page 2


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
2
When the number of sites is large, exact simulation over a desired time in-
terval can be infeasible due to prohibitively small expected times between tran-
sitions. This issue is not particular to spin systems and arises more generally in
the simulation of continuous time Markov chains modelling large populations.
Gillespie [17] proposed the tau-leaping method as a means of generating an ap-
proximate sample path that avoids this problem. Tau-leaping essentially treats
the transition rates as constant over small time intervals. Anderson et al. [2]
provide a detailed analysis of resulting error in the sample paths. In princi-
ple, tau-leaping could be applied to spin systems, however they lack the scaling
required for tau-leaping to provide a reasonable speed-accuracy trade oﬀ.
In this paper we propose a new algorithm for the approximate simulation of
long-range ﬁnite spin systems. The basic idea here is to brieﬂy decouple sites
over small time intervals so that the spin system is treated as a collection of
independent two-state Markov chains. We provide a detailed analysis of the
error in terms of the number of sites incorrectly labelled and accuracy of certain
linear functionals of the state. Our analysis is inspired by [2], though we keep
our analysis entirely non-asymptotic.
1.1. The basic model
We formulate the class of ﬁnite spin systems as continuous-time Markov pro-
cesses on the state space {0, 1}n for some positive integer n representing the total
number of sites, where simultaneous transitions at multiple distinct sites occurs
with zero probability. Any ﬁnite spin system (η(t), t ≥0) can be represented as
a Markov jump process in the usual transition notation:
ηi :
0 →1
at rate q+
i (η)
1 →0
at rate q−
i (η)
for i = 1, . . . , n.
Here, the functions q+
i , q−
i : {0, 1}n →[0, ∞) represent the rate at which sites
ﬂip to the positive state (1), and the zero state (0), respectively. The function
q(η, i) = ηiq−
i (η) + (1 −ηi)q+
i (η) is often called the rate function of the process
[27]. Let N +
i
and N −
i
for each i = 1, . . . , n be independent unit-rate Poisson
processes. Representing the ﬁnite spin system η as a random time change of
Poisson processes [13, §6], we ﬁnd that for any t ≥0,
ηi(t) = ηi(0) + N +
i
Z t
0
(1 −ηi(s))q+
i (η(s))ds

−N −
i
Z t
0
ηi(s)q−
i (η(s))ds

,
i = 1, . . . , n.
(1)
The focus in this paper is on a predominant subclass of practical spin systems
whose q+
i and q−
i functions are of the general form
fi(vi),
where
vi =
n
X
j=1
sijxj,
(2)


## Page 3


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
3
for some functions fi : R →R+ and constants sij ∈R such that the sums
Pn
j=1 sij are uniformly bounded independently of n. As a model of mean-ﬁeld
type, {vi}n
i=1 are commonly referred to as potentials. Transition rate functions
of this form are common in applications such as Hanski’s metapopulation model
[22, 1], spatial SIS epidemic model [7, 21], the voter model [27, §5] and the Ising
model with Kac potentials [8]. They are often considered for their capacity to
interact with a very large number of other sites (indeed, the entire system!).
The form of (2) suggests that it will be important to understand the evolution
of linear functionals of the state. Under certain conditions, the spin system is
well approximated by a deterministic system ρ(t) = (ρi(t))n
i=1 in the sense that
supφ∈Φ |Pn
i=1 φi(ηi(t) −ρi(t))| is small for suﬃciently regular Φ ⊂Rn [4]. In
particular, this deterministic system is given by the solution to
ρi(t) = ρi(0) +
Z t
0
(1 −ρi(s))q+
i (ρ(s)) −ρi(s)q−
i (ρ(s))ds,
for all t ≥0,
(3)
assuming that q+
i
and q−
i
can be smoothly extended to [0, 1]n (see Appendix
A).
1.2. Approximate simulation
As noted earlier, ﬁnite spin systems can in principle be simulated exactly using
the Doob-Gillespie algorithm, though this may be computationally infeasible.
Assuming that for each η ∈{0, 1}n, Pn
i=1 q(η, i) = O(n), the expected number
of transitions in a sample path on [0, T] is then O(nT). If each of the transition
rates can be updated after a transition in constant time, as is the case for
transition rate functions above by storing and updating the potentials, then
the computational cost of simulating this sample path using the Doob-Gillespie
algorithm is O(n2T).
Basic tau leaping is ill-suited to simulating spin systems. Fixing some step
size δ > 0, let tk := kδ denote the lattice of points over which the simulation is
carried out. For notational convenience, we deﬁne χ as the simple function
χ(s) :=
∞
X
k=0
tk1s∈[tk,tk+1).
that maps each time point t to the last point on the lattice. The process of
Euler tau-leaping translates to holding the transition rates constant over each
interval [tk, tk+1). With this in mind, the Euler tau-leaping approximation ˆηδ
to (1) satisﬁes
ˆηδ
i (t) = ηi(0) + N +
i
Z t
0
(1 −ˆηδ
i ◦χ(s)) q+
i (ˆηδ ◦χ(s))ds

−N −
i
Z t
0
ˆηδ
i ◦χ(s) q−
i (ˆηδ ◦χ(s))ds

,
i = 1, . . . , n.
(4)


## Page 4


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
4
At the lattice points, ˆηδ can be evaluated recursively via
ˆηδ
i (tk+1) = ˆηδ
i (tk) + Λ+
i,k −Λ−
i,k,
where Λ+
i,k and Λ−
i,k are independent Poisson random variables with means
δˆηδ
i q+
i (ˆηδ(tk)) and δ(1−ˆηδ
i )q−
i (ˆηδ(tk)), respectively. For the path of ˆηδ to remain
in {0, 1}n it is necessary that the Poisson random variables Λ+
i,k and Λ−
i,k are
either 0 or 1 for all i and k. For this to occur with high probability it is necessary
that the step size is O(n−1). The need to take such a small step size removes
any beneﬁt to performing tau-leaping.
Motivated by the propagation of chaos results that often hold for this type
of system [25, 32, 3], our strategy is to decouple the sites over each time inter-
val [tk, tk+1) so that the process becomes a system of n independent two-state
Markov chains whose transition probabilities are known explicitly. This process
never leaves the set {0, 1}n so avoids the issue described above. However, the
quality of the approximation will depend on how well q+
i (η(t)) and q−
i (η(t)) can
be approximated over [tk, tk+1] by suitably chosen constants. The simplest way
of incorporating this idea is via a forward Euler scheme, approximating q+
i (η(t))
and q−
i (η(t)) by their value at the most recent point on the lattice. With this
in mind, the Euler approximation ηδ to (1) satisﬁes
ηδ
i (t) = ηi(0) + N +
i
Z t
0
(1 −ηδ
i (s))q+
i (ηδ
i ◦χ(s))ds

−N −
i
Z t
0
ηδ
i (s)q−
i (ηδ
i ◦χ(s))ds

,
i = 1, . . . , n,
(5)
The resulting two-state Markov chains on [tk, tk+1] can be simulated using the
Doob-Gillespie algorithm . Even more convenient is the fact that the transition
probabilities of two-state Markov jump processes are known explicitly, and so
it is possible to simulate the process at each time point tk as a discrete-time
Markov chain. Indeed, by letting Qi(x) = q+
i (x) + q−
i (x) for each i = 1, . . . , n,
assuming Qi(x) ̸= 0, P(ηδ
i (tk+1) = 1|ηδ(tk)) = P δ
i (ηδ(tk)), where
P δ
i (ηδ(tk)) :=



q+
i (ηδ(tk))
Qi(ηδ(tk))(1 −e−δQi(ηδ(tk)))
if ηδ
i (tk) = 0
1 −q−
i (ηδ(tk))
Qi(ηδ(tk))(1 −e−δQi(ηδ(tk)))
if ηδ
i (tk) = 1.
(6)
Pseudocode for simulating the Euler approximation on the lattice {kδ}N
k=0 is
provided in Algorithm 1.
To improve upon the Euler method, a midpoint approximation to q+
i (η(s))
and q−
i (η(s)) will also be considered. Analogous to the deterministic approxi-
mation (3), this requires extending q+
i and q−
i smoothly to [0, 1]n. This can be
done in an arbitrary manner, but the choice of extension will play a role in the
quality of the approximation, and consequently, in the error analysis to follow.
Letting pδ
i (z) := zi + 1
2δqi(z) for z ∈[0, 1]n and each i = 1, . . . , n, and assum-
ing that δ is suﬃciently small so that pδ
i maps [0, 1]n into itself, the midpoint


## Page 5


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
5
Algorithm 1: Simulating the Euler approximation (5) for spin systems
Input
: Number of sites n, transition rates q+
i , q−
i
for i = 1, . . . , n, initial value
ηδ(0) ∈{0, 1}n, time step δ > 0, and number of time steps N
Output: System state at each time point {ηδ(δ), ηδ(2δ), . . . , ηδ(Nδ)}
for k = 0, . . . , N −1 do
for i = 1, . . . , n do
Sample ηδ
i ((k + 1)δ) as a Bernoulli random variable with success probability
P δ
i (ηδ(kδ)).
end
end
approximation ˚ηδ satisﬁes
˚ηδ
i (t) = ηi(0) + N +
i
Z t
0
(1 −˚ηδ
i (s))q+
i (pδ ◦˚ηδ ◦χ(s))ds

−N −
i
Z t
0
˚ηδ
i (s)q−
i (pδ ◦˚ηδ ◦χ(s))ds

,
i = 1, . . . , n.
(7)
This time, the transition probabilities are given by
P(˚ηδ
i (tk+1) = 1|˚ηδ
i (tk)) = P δ
i (pδ ◦˚ηδ(tk)).
(8)
Pseudocode for simulating the midpoint approximation on the lattice {kδ}N
k=0
is provided in Algorithm 2.
Algorithm 2: Simulating the midpoint approximation (7) for spin systems
Input
: Number of sites n, transition rates q+
i , q−
i
for i = 1, . . . , n, initial value
˚ηδ(0) ∈{0, 1}n, time step δ > 0, and number of time steps N
Output: System state at each time point {˚ηδ(δ),˚ηδ(2δ), . . . ,˚ηδ(Nδ)}
for k = 0, . . . , N −1 do
for i = 1, . . . , n do
Compute ˜ηδ
i (kδ) = pδ
i (˚ηδ(kδ)).
end
for i = 1, . . . , n do
Sample ˚ηδ((k + 1)δ) as a Bernoulli random variable with success probability
P δ
i (˜ηδ(kδ)).
end
end
Practically speaking, a single step of Algorithm 2 is not much more chal-
lenging to execute than Algorithm 1, only doubling the computation involved.
However, as we shall see, the midpoint approximation can be substantially more
accurate than the Euler approximation allowing a much larger step size to be
taken.


## Page 6


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
6
1.3. Fast summation methods
Algorithms 1 and 2 will only be useful if they can be implemented with signiﬁ-
cantly less computational cost than the Doob-Gillepie algorithm applied to the
original process (1). When the functions q+
i
and q−
i
have the form (2), naive
evaluation of the 2n transition rates requires O(n2) operations. In Algorithms
1 and 2 they must be recomputed at every time-step, implying an O(n2T/δ)
computational burden. On the other hand the computation burden of the Doob-
Gillespie algorithm is O(n2T). Therefore, naively implemented, these algorithms
are more costly to implement than the Doob-Gillespie algorithm. For Algorithms
1 and 2 to oﬀer computational savings we need methods which can evaluate n
sums of the form (2) in sub-quadratic time.
In the special case where the sites are indexed on a d-dimensional regular
lattice and sij = k(i −j) for some kernel function k, the sums in (2) become
convolutions which may be rapidly computed exactly in O(n log n) time using
the fast Fourier transform. This approach is simple and well-known, yet remains
eﬀective and highly recommended whenever applicable, thanks to the accessibil-
ity of highly eﬃcient implementations of the fast Fourier transform [14]. In fact,
our numerical experiments will focus predominantly on this particular method.
The state-of-the-art methods in this arena are the class of tree methods and
their siblings. When the number of spatial dimensions d is not too large, these
comprise perhaps the fastest summation methods to date [18]. The simpler,
single-tree case involves the construction of a tree which groups the n sites
together in O(log n) levels, in O(n log n) time. Usually this is performed spatially
with respect to some metric (usually Euclidean). By utilising some form of
approximation (either spatial averages or multipole expansions), information
necessary to estimate potentials can be contained in each group at each level of
the tree. For each source site zi, the corresponding potential vi can be obtained
by passing through each level of the tree. The number of steps required to
estimate the potential of a single node becomes O(log n), for a total O(n log n)
computation time. Algorithms of this form include the celebrated Barnes-Hut
algorithm [5] commonly used for simulations of the n-body problem.
A more sophisticated, and often much more eﬃcient, approach, is to group
source sites according to a tree as well. Such methods are referred to as dualtree
methods, and have linear total computation complexity, for a ﬁxed tolerance
ϵ [18]. The most noteworthy dualtree method is the fast multipole method of
Greengard and Rokhlin [19] (including its application to the Gaussian kernel,
called the fast Gauss transform [20, 34]). Provided the bandwidth of the kernel
is not too small, computation of the potentials can be achieved in O(n) time.
On the other hand, if the bandwidth is too small, the fast multipole method
can prove even less eﬃcient than the naive approach.
1.4. Paper outline
The remainder of the paper is organised as follows: ﬁrst, in §2, we develop strong
error bounds for the approximations (5) and (7), controlling the expected num-


## Page 7


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
7
ber of sites with incorrect spin in terms of the step size and norms on the
derivatives of q. In §3, we study the renormalised diﬀerences of linear combi-
nations of the state vectors for the Euler method. Unlike the approach seen in
[2], ours will be purely non-asymptotic, deriving an explicit error bound on the
rate of convergence as well. Together with the strong error bounds, this analysis
shows that the mid-point method is substantially more accurate than the Euler
method when the system is not in equilibrium. Finally, in §4, we empirically
demonstrate the accuracy of the approximation and the reduced computational
cost of the proposed simulation method. All proofs have been relegated to Ap-
pendix B.
2. Strong error analysis
Our analysis begins with the development of strong error bounds for the Euler
and midpoint methods. These arguments adhere fairly closely to those of [2], but
must take greater care to keep track of terms depending on n, especially those
involving derivatives of q+ and q−. For this purpose, it is necessary to introduce
some notation. For a function f : [0, 1]n →Rm, let ∥f∥∞= maxi supx |fi(x)|.
Deﬁne
∥Df∥1 := max
j
X
i
∥∂jfi∥∞,
∥D∗f∥1 := max
j
X
i̸=j
∥∂jfi∥∞,
∥Df∥∞:= max
i
X
j
∥∂jfi∥∞,
∥D∗f∥∞:= max
i
X
j̸=i
∥∂jfi∥∞.
Since qi(x) = q+
i (x) if xi = 0 and qi(x) = q−
i (x) if xi = 1, it follows that
∥q+∥∞≤∥q∥∞and ∥q−∥∞≤∥q∥∞. Furthermore, by construction, ∂iq+
i (x) =
∂iq−
i (x) = 0 and, for j ̸= i, ∂jqi(x) = (1 −xi)∂jq+
i (x) −xi∂jq−
i (x), Therefore,
if p = 1 or p = ∞, ∥Dq+∥p ≤∥D∗q∥p and ∥Dq−∥p ≤∥D∗q∥p.
With this in tow, the strong error analysis for the Euler method is stated
in Theorem 2.1. Note that the only assumption required here is that q ∈
C1([0, 1]n, Rn
+).
Theorem 2.1. For some step-size δ > 0, let η(t) and ηδ(t) satisfy (1) and the
Euler approximation (5) respectively. Then for any time T > 0,
sup
t∈[0,T ]
n
X
i=1
E|ηi(t) −ηδ
i (t)| ≤4nδT∥q∥∞∥D∗q∥1e2T (∥q∥∞+∥D∗q∥1).
To elucidate the order of approximation of the strong error bound in Theorem
2.1, we return to the aforementioned ‘mean-ﬁeld’ case. Here, both ∥q∥∞and
∥D∗q∥1 are O(1), and so the expected number of discrepancies between η(t)
and the Euler approximation ηδ(t) is O(nδ). Recalling that the corresponding
error for the deterministic approximation is O(n1/2), the Euler approximation
can be guaranteed to be competitive only if δ = O(n−1/2).
We now proceed on to obtain a strong error bound for the midpoint method.
The situation here is more complex, now involving second-order derivatives of q,


## Page 8


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
8
so requiring q ∈C2([0, 1]n, Rn
+). Once again, we deﬁne two variables that control
this higher-order regularity:
γn =
n
X
i,j=1
i̸=j
∥∂2
j qi∥∞,
and
Γn =
max
i=1,...,n
n
X
j,k=1
j,k̸=i
∥∂j∂kqi∥∞.
For a function f : [0, 1]n →Rm, we will also require
∥Df∥2,1 =
n
X
i=1


n
X
j=1
∥∂jfi∥2
∞


1/2
, ∥D∗f∥2,1 =
m
X
i=1


n
X
j=1,j̸=i
∥∂jfi∥2
∞


1/2
.
The strong error bound for the midpoint method is presented in Theorem 2.2.
Theorem 2.2. Let η(t) and ˚ηδ(t) satisfy (1) and the midpoint approximation
(7) respectively. Then for any step-size δ > 0 and any time T > 0,
sup
t∈[0,T ]
n
X
i=1
E|ηi(t) −˚ηδ
i (t)| ≤10α(n, δ)(T + 1)e2T (∥q∥∞+∥D∗q∥1).
where
α(n, δ) = nδ2∥q∥∞(1 + ∥q∥∞)(1 + ∥D∗q∥1) (Γn + ∥D∗q∥1)
+ δ∥q∥∞γn + δ1/2∥q∥1/2
∞∥D∗q∥2,1.
Returning to the mean-ﬁeld case, both γn and Γn are O(1), while ∥D∗q∥2,1 is
O(n1/2), implying the error bound in Theorem 2.2 is of order O(nδ2 + (nδ)1/2).
If δ ≥n−1/3, the O(nδ2) term dominates as n →∞, implying that the midpoint
method is competitive with the deterministic approximation if δ = O(n−1/4).
Ignoring constants, for large n, this suggests that the midpoint method has
smaller error than the Euler method for the viable case δ ≥n−1.
3. Exact error asymptotics
Having now established strong error bounds for the two approximation methods,
we shall formally demonstrate that the midpoint method should outperform the
Euler method in the n →∞regime for viable step sizes. To accomplish this,
we will prove that the O(nδ) error complexity is exact by characterising the
limiting behaviour of weighted errors
(nδ)−1
n
X
i=1
φi(ηi(t) −ηδ
i (t)),
φi ∈R,
between the ﬁnite spin system η(t) and the Euler approximation ηδ(t), as nδ →
∞. More speciﬁcally, these errors will be shown in Theorem 3.1 to be well-
approximated by n−1 Pn
i=1 φiEi(t), where E(t) is the solution to the system of


## Page 9


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
9
ordinary diﬀerential equations:
d
dtEi(t) = Dq(ρ(t))⊤E(t) + 1
2D∗q(ρ(t))⊤q(ρ(t))
(9a)
Ei(0) = 0.
(9b)
Using Gronwall’s inequality, the growth of E(t) can be readily controlled. Since
for each i = 1, . . . , n and any t ≥0,
Ei(t) ≤
Z t
0
∥Dq∥1∥E(s)∥∞ds + 1
2∥D∗q∥1∥q∥∞t,
for any T > 0,
sup
t∈[0,T ]
∥E(t)∥∞≤1
2∥q∥∞∥D∗q∥1TeT ∥Dq∥1,
(10)
which grows comparably to the error bound in Theorem 2.1.
3.1. Assumptions
Although the strong error bounds have been obtained in virtually complete
generality, unfortunately, the same could not be achieved for the exact error
asymptotics. Indeed, some regularity between the functions qi, i = 1, . . . , n,
needs to be enforced. This can be accomplished by parameterisation, assum-
ing that qi(x) = q(x; zi) for each i = 1, . . . , n. Now, one need only impose
appropriate assumptions on q and zi.
The idea here will be to take advantage of the small metric entropy and
closure under pointwise multiplication of the following set of analytic func-
tions. Let Ω⊂Cd be a compact parameter space and let Φ denote the set
of functions φ : Ω→R analytic on Ω, each with an analytic continuation
to a function φ∗: Ω′ →C where Ω⊂Ω′ ⊂Cd satisfying |φ∗(z)| ≤1 for
z ∈Ω′. For each ϵ > 0, we assign an ϵ-internal covering Φϵ ⊂Φ of minimal
cardinality under the uniform metric. From [33, Theorem 9.2], there exists a
constant CΩ,Ω′,d depending only on Ω, Ω′ and their dimension d such that for
any 0 < ϵ < 1, log |Φϵ| ≤CΩ,Ω′,d| log ϵ|d+1. Also note that, for any chosen pa-
rameters z1, . . . , zn ∈Ω, we can bound the Rademacher complexity of the set
of vectors Φ(z) = {(φ(zi))n
i=1 : φ ∈Φ}. Indeed, letting σ1, . . . , σn denote inde-
pendent Rademacher random variables, using similar arguments to [9, Theorem
3.2],
Rad(Φ(z)) := E sup
φ∈Φ(z)
1
n
n
X
i=1
φiσi ≤
C1/2
Ω,Ω′,dΓ
  d+3
2

√n
.
(11)
Deﬁne a norm on the space of analytic functions φ : Ω→R by ∥φ∥Φ :=
supz∈Ω′ |φ∗(z)|. By construction, if φ ∈Φ, then ∥φ∥Φ ≤1, and if ∥φ∥Φ < ∞,
then φ/∥φ∥Φ ∈Φ. With this notation, our primary assumption is as follows.


## Page 10


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
10
Assumption 1. There exist points z1, . . . , zn ∈Ωand a function q such that
qi(x) = q(x; zi) for each i = 1, . . . , n, and there exists Ω′ with Ω⊊Ω′ ⊂Cd
for which
• ∥q∥Φ := supx∈[0,1]n ∥q(x; ·)∥Φ < +∞;
• ∥Dq∥Φ := Pn
i=1 supx∈[0,1]n ∥∂xiq(x; ·)∥Φ < +∞.
While we expect Assumption 1 to hold for many practical ﬁnite spin systems
(as most of them are constructed to occupy some region of space), it is not
altogether trivial to verify. An obvious suﬃcient condition to guarantee that
∥φ∥Φ < ∞is to impose that φ has an analytic continuation that is entire on
Cd. For example, if z1, . . . , zn ∈[−1, 1]d and
q+
i (x) = λ
n
n
X
j=1
κ(zi −zj)xj,
q−
i (x) = µ,
i = 1, . . . , n,
where λ, µ > 0, and κ(x) = e−a∥x∥2 is a Gaussian kernel with bandwidth 1/a,
then Assumption 1 is satisﬁed for any choice of Ω′. Taking Ω′ = {z ∈C : |z| ≤
R}d for R > 1, then
∥q∥Φ ≤λe4adR2 + µ,
∥Dq∥Φ ≤λe4adR2.
This form arises in connection with the Hanski incidence function model [29].
On the other hand, consider the Ising model with Gaussian Kac potentials [30],
given by
q±
i (x) = 1
2

1 ± tanh

β
n
n
X
j=1
e−a∥zi−zj∥2(2xj −1)



,
(12)
where each z1, . . . , zn ∈[−1, 1]d. Since tanh(x) is not entire, we must take care
to choose Ω′, a and β appropriately to avoid its poles. Fortunately, choosing Ω
to be a suﬃciently thin open set on Cd encompassing [−1, 1]d, there will always
exist an Ω′ for which Assumption 1 holds.
3.2. Main result
Now that appropriate assumptions on the rate functions qi have been estab-
lished, we can proceed with our main result on the exact error asymptotics
of the Euler method. Of course, quantifying a rate of convergence requires an
appropriate metric — a natural choice, like the strong error bounds in the previ-
ous section, would be the L1 norm. Unfortunately, we have found this to require
extraordinary control over the quadratic variation of the errors ηi(t)−ηδ
i (t). In-
stead, we shall do so under the classic metrisation of convergence in probability.
For any random variable X, we let ¯EX := E[X ∧1], recalling that for random


## Page 11


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
11
variables X, X1, X2, . . . , ¯E|Xn −X| →0 if and only if Xn
P→X. We shall make
use of the fact that the truncated L1 norm satisﬁes
¯E|X| ≤2 inf{ϵ > 0 : P(|X| > ϵ) < ϵ}.
(13)
Also, to facilitate the proof, it will be necessary to deﬁne the following:
˜Γn =
n
X
i=1
max
j,k=1,...,n ∥∂j∂kqi∥∞,
θn =
n
X
i,k=1
i̸=k
max
j=1,...,n ∥∂j∂2
kqi∥∞.
With this in tow, we present our main result in Theorem 3.1.
Theorem 3.1. Suppose that Assumption 1 holds and nδ ≥1. There exists a
polynomial P in
T, ∥q∥Φ, ∥Dq∥Φ, ∥D∗q∥F , n˜Γn, n1/2θn,
such that
¯E sup
φ∈Φ
sup
t∈[0,T ]

1
nδ
n
X
i=1
φi(ηi(t) −ηδ
i (t) −δEi(t))

≤Pe6T (∥q∥Φ+∥Dq∥Φ)
log(1 + nδ)
(nδ)1/3
+ δ

.
The proof of Theorem 3.1 is quite long, comprising Appendix B.2. For mean-
ﬁeld-type models satisfying Assumption 1, we can see that P is necessarily
bounded independently of n and δ. However, we suspect that the order of ap-
proximation in nδ of this bound can be improved with better control over the
quadratic variation of the errors ηi(t) −ηδ
i (t). Consider, for instance, that if
ρ(t) has a stable equilibrium ρ∞= limt→∞ρ(t), then n−1 Pn
i=1 φiEi(t) →0 as
t →∞. Furthermore, if η(t) starts near its (quasi-)stationary regime with each
ηi(0) taken to be independent with P(ηi(0) = ρ∞,i) for each i = 1, . . . , n, then
E(t) = 0 and so Theorem 3.1 suggests that
¯E sup
φ∈Φ
sup
t∈[0,T ]

n
X
i=1
φi(ηi(t) −ηδ
i (t))
 = O((nδ)2/3 + nδ2),
excluding logarithmic terms. On the other hand, assuming that the error terms
Ei comprise all ﬁrst-order errors in the Euler approximation, we expect the
Euler and midpoint approximations to perform comparably in this scenario.
In the next section, we shall conduct numerical experiments to support this
hypothesis. Based on this, we should expect the optimal rate of convergence to
be at most O((nδ)−1/2 + δ), excluding logarithmic terms.


## Page 12


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
12
4. Numerical experiments
To complement the results obtained thus far and assess their relevance in prac-
tice, we conduct numerical experiments comparing the performance of the Doob-
Gillespie algorithm to the Euler and midpoint approximations. We shall begin by
assessing accuracy of the approximations by simulating the coupled processes
(1), (5) and (7) with respect to the same Poisson processes. Of course, this
negates the computational advantages of the Euler and midpoint approxima-
tions, so we shall forego comparisons of computation time between the methods
for now.
For the sake of illustration, we restrict ourselves to the one–dimensional case
(with site space {1, . . . , n}), considering a transition rate function constructed
according to an Gaussian convolutional kernel:
q+
i (x) =
2σ
n√π
n
X
j=1
exp
"
−
σ(i −j)
n
2#
xj,
(14)
for some scale parameter σ > 0. The extinction rates are chosen uniformly
q−
i (x) ≡1. The corresponding spin system is of mean-ﬁeld-type, and satisﬁes
Assumption 1. As n →∞, the solution ρ∞to qi(ρ∞) = 0 for i = 1, . . . , n
becomes increasingly uniform ρ∞≡ρ. The quasi-stationary distribution of η is
approximately a product of n Bernoulli random variables with probability 1/2;
in fact, for each i = 1, . . . , n,
q+
i (ρ1) = 2ρ + O(e−σ2) + O(n−1),
as σ, n →∞,
Since (14) is of convolutional form, the corresponding potentials can be com-
puted eﬃciently using the univariate fast Fourier transform.
Figure 1 presents a realisation of the Euler and midpoint approximations and
their evolution in time for the same spin system, coupled together with the same
Poisson processes. Locations of errors from an exact Doob-Gillespie simulation
for the same process are also shown. Here, the process does not start near quasi-
stationarity, and the midpoint approximation displays signiﬁcantly fewer errors
than the Euler approximation throughout the duration of the simulation.
To more precisely compare the accuracy of the two methods, we can measure
the largest proportion of errors encountered up to that point in time. For the
Euler and midpoint approximations, this is given by
sup
s∈[0,t]
1
n
n
X
i=1
|ηi(s) −ηδ
i (s)|,
sup
s∈[0,t]
1
n
n
X
i=1
|ηi(s) −˚ηδ
i (s)|.
(15)
These quantities are plotted in Figure 2, whose left-hand side once again illus-
trates the improved accuracy for the midpoint approximation when initialised
away from quasi-stationarity. In fact, we see improved accuracy for the mid-
point approximation, even for a much larger step size (ten times larger, in this
case). On the other hand, as the process tends towards quasi-stationarity in


## Page 13


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
13
Euler Approximation
8.0
6.0
4.0
2.0
Errors (Euler)
Midpoint Approximation
sites
8.0
6.0
4.0
2.0
Errors (Midpoint)
sites
Fig 1. Simulation of the Euler (top) and midpoint (bottom) approximations for a ﬁnite spin
system with n = 2000 sites, q+
i
given by (14) with σ = 20, and q−
i
≡1 for i = 1, . . . , n,
coupled together with the same Poisson processes, and with step size δ = n−1/3. For each
process, the realisation is presented on left with presence (ηi(t) = 1) denoted by a black site
and absence (ηi(t) = 0) a white site. Locations of errors compared with the coupled Doob-
Gillespie simulation are presented on right in black.


## Page 14


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
14
0
1
2
3
4
5
6
7
8
9
10
0
0.005
0.01
0.015
0.02
0.025
0.03
0.035
0.04
0.045
0
1
2
3
4
5
6
7
8
9
10
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
10-3
Fig 2.
Plots of the largest proportion of errors encountered (15) up to time t for the Euler
approximation with step size δ = n−1/2 (blue) and midpoint approximation with step sizes
δ = n−1/2 (red) and δ = n−1/4 (yellow) for a spin system with n = 104 sites, q+
i
given
by (14) with σ = 20, and q−
i
≡1 for i = 1, . . . , n, coupled together with the same Poisson
processes. The process is started with 10% of its sites initially occupied (left) and near the
quasi-stationary distribution with P(ηi(0) = 1) = 1/2 for all i = 1, . . . , n (right).
time, supi=1,...,n Ei(t) →0. As discussed earlier, in this regime, Theorem 3.1
would still imply increased accuracy for the midpoint approximation. However,
this does not appear to be the case — as seen in the right-hand plot of Figure
2, when the process is started near quasi-stationarity, the accuracy of the Euler
and midpoint approximations appear comparable. This supports the hypothesis
that the rate of convergence in Theorem 3.1 may be further improved. Finally,
to illustrate the precision of the exact asymptotics in Theorem 3.1, Figure 3 dis-
plays the average normalised errors (nδ)−1 Pn
i=1(ηi(t)−ηδ
i (t)) with the average
predicted errors n−1 Pn
i=1 Ei(t) for the Euler approximation.
Turning now to computation time, in Figure 4, average speedup factors
over the time interval [0, T] for the Euler and midpoint approximations (Al-
gorithms 1 and 2, respectively) over the Doob–Gillespie algorithm are pre-
sented. Here, we consider the Ising–Kac model over a two-dimensional site
space S = {1, . . . , n} × {1, . . . , n} with q+
i
and q−
i
given by (12) with β = 1
and a = 40n−1, which we have shown to satisfy Assumption 1. In all cases, the
process is initialised with an initial distribution of P(ηi(0) = 1) = 1/2. The step
sizes for the Euler and midpoint approximations are chosen to be of the order of
the maximal competitive step size; that is, δ = n−1/2 for the Euler approxima-
tion, and δ = n−1/4 for the midpoint approximation. As was shown in Figure
2, the accuracy of the midpoint approximation is competitive to that of the
Euler approximation for these choices of step size. Despite the roughly-doubled
computation time for the midpoint approximation over the Euler approximation
for the same step size, for large site spaces, the signiﬁcantly smaller step size
for the midpoint approximation sees greatly improved performance over both
the Euler and Doob-Gillespie algorithms. Altogether, Figures 2 and 4 suggest
that, among the three methods discussed, the midpoint approximation is the
better choice for ﬁnite spin systems not near (quasi-)stationarity. On the other
hand, since the Euler approximation is universally faster to compute than the


## Page 15


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
15
0
1
2
3
4
5
6
7
8
9
10
-0.1
0
0.1
0.2
0.3
0.4
0.5
0.6
0
1
2
3
4
5
6
7
8
9
10
-0.1
0
0.1
0.2
0.3
0.4
0.5
0.6
Fig 3.
Comparison of normalised errors (nδ)−1 Pn
i=1(ηi(t) −ηδ
i (t)) for the Euler approx-
imation (blue) to average predicted ﬁrst-order error n−1 Pn
i=1 Ei(t) (red) for a ﬁnite spin
system with q+
i
given by (14) with σ = 20, and q−
i ≡1 for i = 1, . . . , n, with 10% of its sites
initially occupied. The number of sites n and the step size δ are taken to be n = 104 and
δ = n−1/2 (left); and n = 105 and δ = n−1/4 (right).
32x32
64x64
128x128
256x256
512x512
site space
1
101/2
101
103/2
102
Speedup Factor
Euler approximation
midpoint approximation
Fig 4. Average speedup factors for Algorithms 1 (blue) and 2 (red) over the Doob–Gillespie
algorithm for the Ising–Kac model over two-dimensional site spaces of size 2m × 2m for
m ∈{5, . . . , 9}, with initial states ηi(0) generated independently with P(ηi(0) = 1) = 1/2.


## Page 16


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
16
midpoint approximation for the same step size, Figure 2 suggests that the Euler
approximation may be preferred for ﬁnite spin systems near (quasi-)stationarity.
Appendix A: Independent site approximation
To enable the application of standard techniques, as in [4, 23], we compare η(t)
with an independent site approximation ω(t) with transition rates
ωi(t) →ωi(t) + 1
at rate q+
i (ρ(t))(1 −ωi(t))
ωi(t) →ωi(t) −1
at rate q−
i (ρ(t))ωi(t),
for each i = 1, . . . , n, and where ρ(t) is deﬁned in (3). Because each element of
ω(t) is independent for all time, for 1 ≤r ≤2, using the method of bounded
diﬀerences [6, Corollary 3.2] and the Lindeburg argument [23, eq. (2.5)], we can
estimate for any smooth function f,
∥f(ω(t)) −f(ρ(t))∥r ≤1
2


n
X
j=1
∥∂jf∥2
∞


1/2
+ 1
2
n
X
j=1


∂2
j f


∞.
(16)
To compare η(t) and ω(t), we couple them together using the basic coupling for
spin systems (see [27, Section III.1]). Let Ji(T) := supt∈[0,T ] 1{ηi(t) ̸= ωi(t)} and
deﬁne ¯J(T) := n−1 Pn
i=1 Ji(T). Now, since X = (η, ω, J, ρ) is a Feller process,
denoting by LX the inﬁnitesimal generator of X, we may deﬁne the process J (t)
by
J (t) := LX ¯J(η(t), ω(t), J(t), ρ(t))
= 1
n
n
X
i=1
LX Ji(η(t), ω(t), J(t), ρ(t))
= 1
n
n
X
i=1
(1 −Ji(t)){(1 −ωi(t))|q+
i (η(t)) −q+
i (ρ(t))|
(17)
+ ωi(t)|q−
i (η(t)) −q−
i (ρ(t))|},
and by Dynkin’s formula, since ¯J(0) = 0, there exists a martingale M such that
¯J(t) = M(t) +
Z t
0
J (s)ds,
t ≥0.
(18)
Lemma A.1. For any T ≥0,
E ¯J(T) ≤n−1(∥D∗q∥2,1 + γn)Te2T ∥D∗q∥1
(19)
∥¯J(T)∥2 ≤2n−1(1 + (∥D∗q∥2,1 + γn)T)e3T ∥D∗q∥1.
(20)
Proof. Combining (17) and (18),
d
dtE ¯J(t) = EJ (t) ≤1
n
n
X
i=1
E|q+
i (η(t)) −q+
i (ρ(t))| + E|q−
i (η(t)) −q−
i (ρ(t))|,


## Page 17


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
17
and so applying (16) with the Mean Value Theorem gives
EJ (t) ≤2∥D∗q∥1E ¯J(t) + n−1(∥D∗q∥2,1 + γn)
(21)
and so
E ¯J(t) ≤2∥D∗q∥1
Z t
0
E ¯J(s)ds + tn−1(∥D∗q∥2,1 + γn).
Equation (19) now follows from Gronwall’s inequality. To show (20), once again
from (18),
∥¯J(t)∥2 ≤∥M(t)∥2 +
Z t
0
∥J (s)∥2ds,
t ≥0,
(22)
and from (17),
∥J (t)∥2 ≤





1
n
n
X
i=1
q+
i (η(t)) −q+
i (ρ(t))





2
+





1
n
n
X
i=1
q−
i (η(t)) −q−
i (ρ(t))





2
,
whereby (16) with the Mean Value Theorem once again implies
∥J (t)∥2 ≤2∥D∗q∥1∥¯J(t)∥2 + n−1(∥D∗q∥2,1 + γn),
t ≥0.
(23)
It only remains to bound ∥M(t)∥2. However, since M(0) = 0, EM(t)2 = E[M]t,
where [M]t is the quadratic variation of M. As ¯J moves only by jumps of size
n−1, it follows [M]t = n−1 ¯J(t). Therefore, by (19),
∥M(T)∥2 ≤n−1(∥D∗q∥2,1 + γn)1/2T 1/2eT ∥D∗q∥1
(24)
≤n−1(1 + (∥D∗q∥2,1 + γn)T)eT ∥D∗q∥1.
(25)
Combining (22), (23), and (25) yields
∥¯J(t)∥2 ≤2∥D∗q∥1
Z t
0
∥¯J(s)∥2ds + 2n−1(1 + (∥D∗q∥2,1 + γn)t)et∥D∗q∥1,
from whence (20) follows by Gronwall’s inequality.
Similarly, for the Euler tau-leaping process, we compare ηδ(t) with its inde-
pendent site approximation ωδ(t) with transition rates
ωδ
i (t) →ωδ
i (t) + 1
at rate q+
i (ρδ ◦χ(t))(1 −ωδ
i (t))
ωδ
i (t) →ωδ
i (t) −1
at rate q−
i (ρδ ◦χ(t))ωδ
i (t),
for each i = 1, . . . , n, where
d
dtρδ
i (t) = (1 −ρδ
i (t))q+
i (ρδ ◦χ(t)) −ρδ
i (t)q−
i (ρδ ◦χ(t))


## Page 18


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
18
As before, each element of ωδ(t) is independent for all time, Eωδ(t) = ρδ(t), and
∥f(ωδ(t)) −f(ρδ(t))∥r ≤1
2


n
X
j=1
∥∂jf∥2
∞


1/2
+ 1
2
n
X
j=1
∥∂2
j f∥∞.
(26)
Deﬁne Jδ
i (T) := supt∈[0,T ] 1{ηδ
i (t) ̸= ωδ
i (t)} and ¯Jδ(T) := n−1 Pn
i=1 Jδ
i (T). Nei-
ther ηδ nor ωδ are Markov processes, however, they are Markov over each time
interval [kδ, (k+1)δ) for k ≥0. Therefore, for any k ≥0, we can couple ηδ and ωδ
together using the basic coupling, and form a Feller process Zk = (ηδ, ωδ, Jδ)
over [kδ, (k + 1)δ), conditioned on ηδ(kδ), ωδ(kδ), and Jδ(kδ). Proceeding as
before, by Dynkin’s formula, there is a martingale Mk such that
¯Jδ(kδ + t) = ¯Jδ(kδ) + M δ
k(t) +
Z kδ+t
kδ
J δ(s)ds,
0 ≤t < δ,
(27)
where
J δ(t) = 1
n
n
X
i=1
(1 −Jδ
i (t))(1 −ωδ
i (t))|q+
i (ηδ ◦χ(t)) −q+
i (ρδ ◦χ(t))|+
1
n
n
X
i=1
(1 −Jδ
i (t))ωδ
i (t)|q−
i (η ◦χ(t)) −q−
i (ρδ ◦χ(t))|.
Lemma A.2. For any T ≥0,
E ¯Jδ(T) ≤n−1(∥D∗q∥2,1 + γn)Te2T ∥D∗q∥1
(28)
∥¯Jδ(T)∥2 ≤2n−1(1 + (∥D∗q∥2,1 + γn)T)e3T ∥D∗q∥1.
(29)
Proof. As in the proof of Lemma A.1, by the Mean Value Theorem and (26),
EJ δ(t) ≤2∥D∗q∥1E ¯Jδ(χ(t)) + n−1(∥D∗q∥2,1 + ∥D2q∥1,1),
t ≥0,
(30)
and so by direct integration, (27) implies that for 0 ≤t < δ,
E ¯Jδ(kδ + t) ≤(1 + 2t∥D∗q∥1)E ¯Jδ(kδ) + tn−1(∥D∗q∥2,1 + γn).
(31)
Since E ¯Jδ(t) is continuous in t, taking t →δ−, this implies
E ¯Jδ((k + 1)δ) ≤(1 + 2δ∥D∗q∥1)E ¯Jδ(kδ) + δn−1(∥D∗q∥2,1 + γn).
Performing induction over k, with ¯Jδ(0) = 0 gives
E ¯Jδ(kδ) = n−1(∥D∗q∥2,1 + γn)kδe2kδ∥D∗q∥1.
Together with (31), this implies (28). We shall now prove (29). By iterating
equation (27), for any k ≥0 and 0 ≤t < δ,
¯Jδ(kδ + t) =
Z kδ+t
0
J δ(s)ds + M δ
k(t) +
k−1
X
l=0
M δ
l (δ).


## Page 19


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
19
It can be seen that {M δ
1(δ), . . . , M δ
k−1(δ), M δ
k(t)} forms a martingale diﬀerence
sequence relative to the increasing sequence of σ-algebras Fk = σ(ηδ(t), ωδ(t), Jδ(t), 0 ≤
t ≤kδ). Therefore,





M δ
k(t) +
k−1
X
l=0
M δ
l (δ)





2
2
= EM δ
k(t)2 +
k−1
X
l=0
EM δ
l (δ)2.
(32)
Since EM δ
k(t)2 = [M δ
k]t = n−1  E ¯Jδ(kδ + t) −E ¯Jδ(kδ)

for each k and 0 ≤t ≤
δ, (28) implies





M δ
k(t) +
k−1
X
l=0
M δ
l (δ)





2
≤n−1(∥D∗q∥2,1 + γn)1/2(kδ + t)1/2e(kδ+t)∥D∗q∥1
≤n−1(1 + (∥D∗q∥2,1 + γn)(kδ + t))e(kδ+t)∥D∗q∥1.
On the other hand, equation (26) implies that
∥J δ(t)∥2 ≤2∥D∗q∥1∥¯Jδ(χ(t))∥2 + n−1(∥D∗q∥2,1 + γn),
t ≥0.
which altogether implies that for any k ≥0 and 0 ≤t < δ,
∥¯Jδ(kδ + t)∥2 ≤2δ∥D∗q∥1
k−1
X
l=0
∥¯Jδ(lδ)∥2 + 2t∥D∗q∥1∥¯JV (kδ)∥2
+ 2n−1(1 + (∥D∗q∥2,1 + γn)(kδ + t))e(kδ+t)∥D∗q∥1.
By induction, we ﬁnd that
∥¯Jδ(kδ)∥2 ≤2n−1(1 + (∥D∗q∥2,1 + γn)kδ)e3kδ∥D∗q∥1
which ﬁnally implies (29).
As usual, the primary application of the independent site approximation is
for obtaining a bound on the ﬁrst- and second-order weak error between η(t)
and the deterministic approximation ρ(t). A bound on the ﬁrst-order weak error
for vector-valued functions, which follows from (16), (26), and Lemmas A.1 and
A.2, is presented in Lemma A.3.
Lemma A.3. For any f = (f1, . . . , fm) ∈C2([0, 1]n, Rm) and any t > 0,
m
X
i=1
[E |fi(η(t)) −fi(ρ(t))| + E|fi(ηδ(t)) −fi(ρδ(t))|]
≤2∥Df∥1(∥D∗q∥2,1 + γn)te2t∥D∗q∥1 + ∥Df∥2,1 +
n
X
i,j=1
∥∂2
j fi∥∞.


## Page 20


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
20
Following the same arguments as [23, Proposition 9], using Lemmas A.1 and
A.2 in place of [23, Lemma 7], we arrive at a bound on the second-order weak
error, presented in Lemma A.4. For brevity, we introduce the notation
Tn(f) =
p
n(1 + log n)
"
√n
max
j,k=1,...,n ∥∂j∂kf∥∞+
max
j=1,...,n
n
X
k=1
∥∂j∂2
kf∥∞
#
.
Lemma A.4. There is a universal constant C > 0 such that, for any f ∈
C([0, 1]n, R) and t > 0,
E

f(η(t)) −f(ρ(t)) −
n
X
j=1
∂jf(ρ(t))(ηj(t) −ρj(t))

≤C(1 + n∥¯J∥2
2)Tn(f)
E

f(ηδ(t)) −f(ρδ(t)) −
n
X
j=1
∂jf(ρδ(t))(ηδ
j(t) −ρδ(t))

≤C(1 + n∥¯Jδ∥2
2)Tn(f).
Appendix B: Proofs
B.1. Strong error analysis
We begin by providing proofs of the strong error bounds presented in Theorems
2.1 and 2.2.
Proof of Theorem 2.1. As will be a recurring theme for all of the main results to
be presented, the method of proof is centered about an application of Gronwall’s
inequality. In this case, the application is fairly standard; ﬁrst, by decomposing
n
X
i=1
E|ηi(t) −ηδ
i (t)| ≤E(T (1)
+
+ T (2)
+
+ T (1)
−
+ T (2)
−),
where each of the terms are given by
T (1)
+
:=
n
X
i=1
Z t
0
(1 −ηi(s))q+
i (η(s)) −(1 −ηδ
i (s))q+
i (ηδ(s))
 ds
T (2)
+
:=
n
X
i=1
Z t
0
(1 −ηδ
i (s))(q+
i (ηδ(s)) −q+
i (ηδ ◦χ(s)))
 ds
T (1)
−
:=
n
X
i=1
Z t
0
ηi(s)q−
i (η(s)) −ηδ
i (s)q−
i (ηδ(s))
 ds
T (2)
−
:=
n
X
i=1
Z t
0
ηδ
i (s)(q−
i (ηδ(s)) −q−
i (ηδ ◦χ(s)))
 ds.


## Page 21


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
21
Treating T (1)
+
and T (2)
+
(the arguments for T (1)
−
and T (2)
−
are similar), the Mean
Value Theorem implies
T (1)
+
≤(∥q+∥∞+ ∥Dq+∥1)
Z t
0
n
X
i=1
|ηi(s) −ηδ
i (s)|ds,
T (2)
+
≤∥Dq+∥1
Z t
0
n
X
i=1
|ηδ
i (s) −ηδ
i ◦χ(s)|ds.
Since |s −χ(s)| ≤δ for any s ≥0, E|ηδ
i (s) −ηδ
i ◦χ(s)| is bounded above by
2∥q∥∞δ. Altogether, this implies
n
X
i=1
E|ηi(t) −ηδ
i (t)| ≤2(∥q∥∞+ ∥D∗q∥1)
Z t
0
n
X
i=1
E|ηi(s) −ηδ
i (s)|ds
+ 4∥q∥∞∥D∗q∥1nδt,
and applying Gronwall’s inequality completes the proof.
Proof of Theorem 2.2. We proceed as in the proof of Theorem 2.1, but now
T (2)
+
:=
n
X
i=1

Z t
0
(1 −˚ηδ
i (s))(q+
i (˚ηδ(s)) −q+
i (pδ ◦˚ηδ ◦χ(s)))ds

T (2)
−
:=
n
X
i=1

Z t
0
˚ηδ
i (s)(q−
i (˚ηδ(s)) −q−
i (pδ ◦˚ηδ ◦χ(s)))ds
 .
To apply Gronwall’s inequality as before, it is necessary to bound the expecta-
tion of these terms. In fact, it will suﬃce to consider T (2)
+
alone, as the procedure
for T (2)
−
is virtually identical. Let
Ui(s) := q+
i (˚ηδ(s)) −q+
i (pδ ◦˚ηδ ◦χ(s)).
Applying a ﬁrst order Taylor expansion to q+
i about ˚ηδ ◦χ(s),
Ui(s) =
n
X
j=1
∂jq+
i (˚ηδ ◦χ(s))

˚ηδ
j(s) −˚ηδ
j ◦χ(s) −δ
2Qj(˚ηδ ◦χ(s))

+ Ri,1 + Ri,2,
where Ri,1 and Ri,2 are the remainders from the expansion of q+
i (pδ ◦˚ηδ ◦χ(s))
and q+
i (˚ηδ(s)), respectively. Note that |Ri,1| ≤δ2∥q∥2
∞
Pn
j,k=1 ∥∂j∂kq+
i ∥∞. For
Ri,2,
E |Ri,2| ≤
n
X
j,k=1
∥∂j∂kq+
i ∥∞E
(˚ηδ
j(s) −˚ηδ
j ◦χ(s))(˚ηδ
k(s) −˚ηδ
k ◦χ(s))
 .


## Page 22


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
22
From (7), the number of jumps in ˚ηδ
i on [a, b] is stochastically dominated by a
Poisson random variable with mean 2∥q∥∞(b −a) so for each j = 1, . . . , n,
E

|˚ηδ
j(s) −˚ηδ
j ◦χ(s)|
 ˚ηδ ◦χ(s)

≤1 −e−2δ∥q∥∞≤2δ∥q∥∞.
Since the ˚ηδ
j(s) are independent conditioned on ˚ηδ ◦χ(s), it follows
E |Ri,2| ≤4δ2∥q∥2
∞
n
X
j,k=1
j̸=k
∥∂j∂kq+
i ∥∞+ 2δ∥q∥∞
n
X
j=1
∥∂2
j q+
i ∥∞.
For each i = 1, . . . , n, deﬁne
˜Ui(s) :=

s −χ(s) −δ
2

n
X
j=1
∂jq+
i (˚ηδ ◦χ(s))qj(˚ηδ ◦χ(s)).
Since
R χ(t)+δ
χ(t)
|s −χ(s) −δ/2|ds = δ2/4 and
R χ(t)+δ
χ(t)
(s −χ(s) −δ/2)ds = 0 for
any bounded function g and any t > 0,

Z t
0
(1 −˚ηδ
i (s))

s −χ(s) −δ
2

g(χ(s))ds
 ≤δ2∥g∥∞

1 +
X
s∈[0,t]
∆˚ηδ
i (s)

.
Again using the fact that the expected number of jumps in ˚ηδ
i on [a, b] is bounded
by 2∥q∥∞(b −a),
E

Z t
0
(1 −˚ηδ
i (s)) ˜Ui(s)ds
 ≤2(t + 1)δ2∥q∥∞(1 + ∥q∥∞)
n
X
j=1
∥∂jq+
i ∥∞.
(33)
Therefore, to control T (2)
+ , it now suﬃces to consider the remaining error term
E

Z t
0
(1 −˚ηδ
i (s))(Ui(s) −˜Ui(s))ds
 ≤t sup
s∈[0,t]
E|Ui(s) −˜Ui(s)|.
To do so, let M(t) denote the martingale
Mi(t) = ˚ηδ
i (t) −
Z t
0
((1 −˚ηδ
i (s))q+
i (pδ ◦˚ηδ ◦χ(s))
−˚ηδ
i (s)q−
i (pδ ◦˚ηδ ◦χ(s)))ds.
In terms of M(t), the diﬀerence Ui(s)−˜Ui(s) = Ti,1+Ti,2−Ti,3−Ti,4+Ri,1+Ri,2,


## Page 23


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
23
where
Ti,1 =
n
X
j=1
∂jq+
i (˚ηδ ◦χ(s))(Mj(s) −Mj ◦χ(s))
Ti,2 =
n
X
j=1
∂jq+
i (˚ηδ ◦χ(s))
Z s
χ(s)
(1 −˚ηδ
j (u))
h
q+
j (pδ ◦˚ηδ ◦χ(u)) −q+
j (˚ηδ ◦χ(u))
i
du
Ti,3 =
n
X
j=1
∂jq+
i (˚ηδ ◦χ(s))
Z s
χ(s)
˚ηδ
j (u)
h
q−
j (pδ ◦˚ηδ ◦χ(u)) −q−
j (˚ηδ ◦χ(u))
i
du
Ti,4 =
n
X
j=1
∂jq+
i (˚ηδ ◦χ(s))[q+
j (˚ηδ ◦χ(s)) + q−
j (˚ηδ ◦χ(s))]
Z s
χ(s)
[˚ηδ
j (u) −˚ηδ
j ◦χ(u)]du.
First, to bound Ti,1, let M +
i (s) := Pn
j=1 ∂jq+
i (˚ηδ ◦χ(s))Mj(s), so that
ET 2
i,1 = E[M +
i (s) −M +
i ◦χ(s)]2 = E[M +
i ]s −E[M +
i ]χ(s).
Note that the quadratic variation of Mj, (resp. M +
i ), is just the number of
jumps in Mj (resp. M +
i ) and that, recalling the deﬁning property of a spin
system, with probability one, no two sites experience simultaneous jumps in ˚ηδ.
Therefore, E[M +
i ]s −E[M +
i ]χ(s) ≤2δ∥q∥∞
Pn
j=1 ∥∂jq+
i ∥2
∞, and so
(E|Ti,1|)2 ≤2δ∥q∥∞
n
X
j=1
∥∂jq+
i ∥2
∞.
(34)
The terms Ti,2 and Ti,3 are controlled together: by the Mean Value Theorem,
|q+
j (pδ ◦˚ηδ ◦χ(s)) −q+
j (˚ηδ ◦χ(s))| ≤1
2δ∥q∥∞
n
X
k=1
∥∂kq+
j ∥∞,
and similarly for q−
j , which implies
E|Ti,2| + E|Ti,3| ≤1
2δ2∥q∥∞
n
X
j,k=1
∥∂jq+
i ∥∞
 ∥∂kq+
j ∥∞+ ∥∂kq−
j ∥∞

.
(35)
Finally, to bound Ti,4,
E|Ti,4| ≤2∥q∥∞
n
X
j=1
∥∂jq+
i ∥∞
Z s
χ(s)
E|˚ηδ
j(u) −˚ηδ
j ◦χ(u)|du
≤2δ∥q∥∞
n
X
j=1
∥∂jq+
i ∥∞E
X
u∈[χ(s),s]
∆˚ηδ
j(u) ≤4δ2∥q∥2
∞
n
X
j=1
∥∂jq+
i ∥∞.
(36)
Combining (33)-(36) with the bounds on Ri,1 and Ri,2 gives
E|T (2)
+ | ≤5(t + 1)nδ2∥q∥∞(1 + ∥q∥∞)[∥D∗q∥1 + Γn + ∥D∗q∥2
1]
+ 2δt∥q∥∞γn +
√
2δ1/2∥q∥1/2
∞t∥D∗q∥2,1


## Page 24


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
24
and so E|T (2)
+ | ≤5α(n, δ)(1 + t). Applying the same arguments to T (2)
−
yields
n
X
i=1
E|ηi(t) −˚ηδ
i (t)| ≤2(∥q∥∞+ ∥D∗q∥1)
Z t
0
n
X
i=1
E|ηi(s) −˚ηδ
i (s)|ds
+ 10α(n, δ)(1 + t).
The proof is completed by applying Gronwall’s inequality as in the proof of
Theorem 2.1.
B.2. Proof of Theorem 3.1
Throughout this proof, for the sake of brevity, the notation x ≲y will be used
to imply there exists some universal constant c > 0 such that x ≤cy. Naturally,
we assume throughout that the hypotheses of Theorem 3.1 hold. We begin by
coupling η(t) and ηδ(t) using the basic coupling, that is, for independent unit-
rate Poisson processes N +
i,k, N −
i,k with i = 1, . . . , n; k = 1, 2, 3:
ηi(t) = ηi(0) + N +
i,1
Z t
0
[(1 −ηi(s))q+
i (η(s)) ∧(1 −ηδ
i (s)q+
i (ηδ ◦χ(s))]ds

+ N +
i,2
Z t
0
[(1 −ηi(s))q+
i (η(s)) −(1 −ηδ
i (s))q+
i (ηδ ◦χ(s))]+ds

−N −
i,1
Z t
0
[ηi(s)q−
i (η(s)) ∧ηδ
i (s)q−
i (ηδ ◦χ(s))]ds

−N −
i,2
Z t
0
[ηi(s)q−
i (η(s)) −ηδ
i (s)q−
i (ηδ ◦χ(s))]+ds

and
ηδ
i (t) = ηi(0) + N +
i,1
Z t
0

(1 −ηi(s))q+
i (η(s)) ∧(1 −ηδ
i (s)q+
i (ηδ ◦χ(s))

ds

+ N +
i,3
Z t
0
[(1 −ηδ
i (s))q+
i (ηδ ◦χ(s)) −(1 −ηi(s))q+
i (η(s))]+ds

−N −
i,1
Z t
0
[ηi(s)q−
i (η(s)) ∧ηδ
i (s)q−
i (ηδ ◦χ(s))]ds

−N −
i,3
Z t
0
[ηδ
i (s)q−
i (ηδ ◦χ(s)) −ηi(s)q−
i (η(s))]+ds

.
Centering the Poisson processes, there is
ηi(t) −ηδ
i (t) = Mi(t) +
Z t
0
[(1 −ηi(s))q+
i (η(s)) −(1 −ηδ
i (s))q+
i (ηδ ◦χ(s))]ds
−
Z t
0
[ηi(s)q−
i (η(s)) −ηδ
i (s)q−
i (ηδ ◦χ(s))]ds.
(37)


## Page 25


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
25
where the remainder Mi(t) is a martingale. For φ ∈Φ, let φi = φ(zi) for each
i = 1, . . . , n. For the sake of brevity, let M φ
δ (t) := (nδ)−1 Pn
i=1 φiMi(t). Then
from (37) and (9a),
(nδ)−1
n
X
i=1
φi(ηi(t) −ηδ
i (t) −δEi(t)) = M φ
δ (t)
−
Z t
0
n−1
n
X
i=1
φi[δ−1(ηi(s) −ηδ
i (s)) −Ei(s)][q+
i (ηδ(s)) + q−
i (ηδ(s))]ds
+ S+(φ, t) −S−(φ, t) +
3
X
k=1
R(k)
+ (φ, t) +
3
X
k=1
R(k)
−(φ, t) + D+(φ, t) + D−(φ, t),
(38)
where S+ and S−denote the second-order weak error terms
S+(φ, t) =
Z t
0
n−1
n
X
i=1
φi(1 −ηi(s))
"
q+
i (η(s)) −q+
i (ηδ(s))
δ
−
n
X
j=1
∂jq+
i (ρ(s))Ej(s)
#
ds
S−(φ, t) =
Z t
0
n−1
n
X
i=1
φiηi(s)
"
q−
i (η(s)) −q−
i (ηδ(s))
δ
−
n
X
j=1
∂jq−
i (ρ(s))Ej(s)
#
ds,
D± denote the discretisation error terms
D+(φ, t) =
Z t
0
n−1
n
X
i=1
φi(1 −ηδ
i (s))q+
i (η(s)) −q+
i (ηδ ◦χ(s))
δ
ds
−1
2
Z t
0
n−1
n
X
i=1
φi(1 −ρi(s))
n
X
j=1
∂jq+
i (ρ(s))qj(ρ(s))ds
D−(φ, t) =
Z t
0
n−1
n
X
i=1
φiηδ
i (s)q−
i (ηδ(s)) −q−
i (ηδ ◦χ(s))
δ
ds
−1
2
Z t
0
n−1
n
X
i=1
φiρi(s)
n
X
j=1
∂jq−
i (ρ(s))qj(ρ(s))ds,
and R(k)
±
denote the remainder terms:
R(1)
± (φ, t) =
Z t
0
n−1
n
X
i=1
φi(ρi(s) −ηi(s))
n
X
j=1
∂jq±
i (ρ(s))Ej(s)ds
R(2)
± (φ, t) =
Z t
0
n−1
n
X
i=1
φiEi(s)[q±
i (ρ(s)) −q±
i (η(s))]ds
R(3)
± (φ, t) =
Z t
0
n−1
n
X
i=1
φiEi(s)[q±
i (η(s)) −q±
i (ηδ(s))]ds.


## Page 26


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
26
Observe that, under Assumption 1, the second term on the right-hand side of
(38) can be bounded in magnitude by
2∥q∥Φ
Z T
0
sup
s∈[0,t]
sup
φ∈Φ
(nδ)−1
n
X
i=1
φi[ηi(s) −ηδ
i (s) −δEi(s)]
 dt,
suggesting that we may use Gronwall’s inequality on (38) to obtain the desired
bound. The remainder of the proof comprises controlling the other terms, in
order of their appearance.
B.2.1. Controlling the martingale term
Fixing T > 0, let Mδ(φ) = supt∈[0,T ] |M φ
δ (t)|. Due to (37),
Mδ(φ) ≤(nδ)−1 sup
t∈[0,T ]
n
X
i=1
φi|Mi(t)| ≤δ−1∥φ∥∞(1 + 2T∥q∥∞).
(39)
Central to our strategy of controlling the martingale M φ
δ is the Fuk-Nagaev
inequality of [12]. First observe that the predictable quadratic variation of M φ
δ
is
⟨M φ
δ ⟩t =
Z t
0
n
X
i=1
(nδ)−2φ2
i
(1 −ηi(s))q+
i (η(s)) −(1 −ηδ
i (s))q+
i (ηδ ◦χ(s))
 ds
+
Z t
0
n
X
i=1
(nδ)−2φ2
i
ηi(s)q−
i (η(s)) −ηδ
i (s)q−
i (ηδ ◦χ(s))
 ds.
Adopting the notation from the proof of Theorem 2.1, for any Φ′ ⊂Φ,
sup
φ∈Φ′⟨M φ
δ ⟩t ≤
∥Φ′∥∞
nδ
2
[T (1)
+
+ T (1)
−
+ T (2)
+
+ T (2)
−],
and so by following the same arguments,
E sup
φ∈Φ′ sup
t∈[0,T ]
⟨M φ
δ ⟩t ≤4T∥Φ′∥2
∞
nδ
∥q∥∞∥D∗q∥1e2T (∥q∥∞+∥D∗q∥1) =: CT ∥Φ′∥2
∞
nδ
.
Lemma B.1. Assuming that δ ≥n−1, there exists a constant C > 0 depending
only on Ω, Ω′, d such that for any T > 0,
¯E sup
φ∈Φ
sup
t∈[0,T ]
M φ
δ (t) ≲1 + log(nδ)
(nδ)1/3
h
1 + 2T∥q∥∞∥D∗q∥1e2T (∥q∥∞+∥D∗q∥1)i
.
Proof. For any Φ′ ⊂Φ, let Mδ(Φ′) := supφ∈Φ′ Mδ(φ). Assuming for now that
Φ′ is a ﬁnite subset of Φ, by the Fuk-Nageav inequality [12, Corollary 3.4], for
any x, L > 0,
P

Mδ(Φ′) ≥
√
2Lx + 2∥Φ′∥∞
3nδ
x

≤2|Φ′|e−x + CT ∥Φ′∥2
∞
nδL
.
(40)


## Page 27


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
27
To apply the inequality in (13), it suﬃces to choose x and L such that
√
2Lx =
(nδL)−1CT ∥Φ′∥2
∞and (3nδ)−1∥Φ′∥∞x = |Φ′|e−x. The only real solution to
these relations is given by
x = W0
3|Φ′|nδ
∥Φ′∥∞

,
L =
CT ∥Φ′∥2
∞
nδ
2/3
·
1
(2x)1/3 ,
(41)
where W0 is the principal branch cut of the Lambert W-function. Now, since
W0(x) ≤log(1 + x) for all x > 0, (13), (40), and (41) imply that
¯EMδ(Φ′) ≤4∥Φ′∥∞
3nδ
· log

1 + 3|Φ′|nδ
∥Φ′∥∞

+ 2
2CT
nδ
1/3
∥Φ′∥2/3
∞· log

1 + 3|Φ′|nδ
∥Φ′∥∞
1/3
.
Assuming nδ ≥1, log(1 + 3|Φ′|nδ
∥Φ′∥∞) ≤2[1 + log(nδ) + log(
|Φ′|
∥Φ′∥∞)], so
¯EMδ(Φ′) ≤6(nδ)−1/3[∥Φ′∥∞+ (1 + CT )∥Φ′∥2/3
∞]

1 + log(nδ) + log
 |Φ′|
∥Φ′∥∞

.
(42)
The extension of the estimate (42) to Φ′ = Φ relies on the chaining argument of
Dudley. Let {φ(k)}∞
k=1 be a sequence of random elements in Φ adapted to the
same probability space as M(t), for which Mδ(φ(k)) →Mδ(Φ) in the topology
of pointwise convergence, and ∥φ(k)−φ(l)∥∞≤2−m for k, l ≥m. Such a sequence
is guaranteed to exist since Φ is relatively compact in the space of continuous
functions on Ω. From this, construct a new sequence {¯φ(k)}∞
k=1 such that ¯φ(k)
occupies the 2−k-internal covering of Φ, Φ2−k, and ∥¯φ(k) −φ(k)∥∞≤2−k for
each k = 1, 2, . . . . Applying dominated convergence under the estimate (39),
¯EMδ(Φ) ≤
∞
X
k=1
¯EMδ(¯φ(k) −¯φ(k−1)).
Observe that for k = 1, 2, . . . , ∥¯φ(k) −¯φ(k−1)∥∞≤5 · 2−k. Now, letting
Φ(k) = {z = x −y : x ∈Φ2−k, y ∈Φ2−(k−1), ∥z∥∞≤5 · 2−k},
evidently, ∥Φ(k)∥∞≤5 · 2−k and |Φ(k)| ≤|Φ2−k| · |Φ2−(k−1)| and so by [33,
Theorem 9.2], there is a constant C > 0 depending only on Ω, Ω′, d such that
log |Φ(k)| ≤Ckd+1. Since ¯φ(k) −¯φ(k−1) ∈Φ(k) by construction, ¯EMδ(Φ) ≤
P∞
k=1 ¯EMδ(Φ(k)) and so (42) implies
¯EMδ(Φ) ≲1 + CT
(nδ)1/3
∞
X
k=1
1 + log(nδ) + kd+1
4k/3
,
where C > 0 depends only on Ω, Ω′, d. The series is absolutely convergent,
implying the result.


## Page 28


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
28
B.2.2. The second-order error terms
Moving on to the second-order error terms S+ and S−, observe that
sup
t∈[0,T ]
sup
φ∈Φ
|S+(φ, t)|
≤∥Dq∥Φ
Z T
0
sup
s∈[0,t]
sup
φ∈Φ

n−1
n
X
j=1
φj[δ−1(ηj(s) −ηδ
j(s)) −Ej(s)]

dt
+
Z T
0
(nδ)−1
n
X
i=1

q+
i (η(s)) −q+
i (ηδ(s)) −
n
X
j=1
∂jq+
i (ρ(s))(ηj(s) −ηδ
j(s))

ds,
(43)
and similarly for S−. The ﬁrst term on the right-hand side of (43) will contribute
to our use of Gronwall’s inequality on (38), so we need only consider the second
term. This is treated for S+ in Lemma B.2; the procedure for S−is identical. For
brevity, we leave the inequality (44) in terms of the L1 and L2 norms of ¯J(T)
and ¯Jδ(T), recalling that these quantities are bounded according to Lemmas
A.1 and A.2.
Lemma B.2. For any T > 0, there is
E
Z T
0
(nδ)−1
n
X
i=1

q+
i (η(s)) −q+
i (ηδ(s)) −
n
X
j=1
∂jq+
i (ρ(s))(ηj(s) −ηδ
j(s))

ds
≲n˜ΓnT 2∥q∥∞∥D∗q∥1e4T (∥q∥∞+∥D∗q∥1)(E ¯J(T) + n−1/2 + δT∥q∥∞∥D∗q∥1)
+ T√1 + log n
nδ
(n˜Γn + n1/2θn)(1 + n(∥¯J(T)∥2
2 + ∥¯Jδ(T)∥2
2)).
(44)
Proof. The proof proceeds in a similar fashion to [23, Proposition 9], comparing
η(t) to ρ(t), ρ(t) to ρδ(t), and ﬁnally ρδ(t) to ηδ(t). First, from Lemma A.4,
n
X
i=1
E

q+
i (η(s)) −q+
i (ρ(s)) −
n
X
j=1
∂jq+
i (ρ(s))(ηj(s) −ρj(s))

+
n
X
i=1
E

q+
i (ηδ(s)) −q+
i (ρδ(s)) −
n
X
j=1
∂jq+
i (ρδ(s))(ηδ
j(s) −ρδ(s))

≲
p
1 + log n(n˜Γn + n1/2θn)(1 + n∥¯J(s)∥2
2 + n∥¯Jδ(s)∥2
2).
(45)
Following the arguments of the proof of Theorem 2.1,
n
X
j=1
|ρj(t) −ρδ
j(t)| ≤4nδt∥q∥∞∥D∗q∥1e2t(∥q∥∞+∥D∗q∥1),
(46)


## Page 29


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
29
and so a second order Taylor expansion for q+
i implies
n
X
i=1

q+
i (ρδ(s)) −q+
i (ρ(s)) −
n
X
j=1
∂jq+
i (ρ(s))(ρδ
j(s) −ρj(s))

≲Γn

nδs∥q∥∞∥D∗q∥1e2s(∥q∥∞+∥D∗q∥1)2
.
(47)
For the remaining cross terms, once again due to (46),
n
X
i=1
E

n
X
j=1
(ηδ
j(s) −ωδ
j(s))[∂jq+
i (ρδ(s)) −∂jq+
i (ρ(s))]

≤4nδs∥q∥∞∥D∗q∥1e2s(∥q∥∞+∥D∗q∥1)˜Γn∥¯Jδ(s)∥1,
(48)
and since the ωδ
j(t) are independent with P(ωδ
j(t) = 1) = ρδ
j(t),
n
X
i=1
E

n
X
j=1
[ωδ
j(s) −ρδ
j(s)][∂jq+
i (ρδ(s)) −∂jq+
i (ρ(s))]

≤


n
X
j=1
ρδ
j(s)(1 −ρδ
j(s))

∂jq+
i (ρδ(s)) −∂jq+
i (ρ(s))
2


1/2
≤2n1/2δs∥q∥∞∥D∗q∥1e2s(∥q∥∞+∥D∗q∥1)˜Γn.
(49)
Combining (45), (47), (48), and (49) implies (44).
B.2.3. The remainder terms R(k)
±
Next, we turn our attention to the remainder terms R(k)
±
for k = 1, 2, 3. The
ﬁrst of these terms, R(1)
± , is controlled in Lemma B.3.
Lemma B.3. For any T > 0,
E sup
t∈[0,T ]
sup
φ∈Φ
(|R(1)
+ (φ, t)| + |R(1)
−(φ, t)|)
≲∥D∗q∥∞
 Z T
0
∥E(s)∥∞ds
!
(E ¯J(T) + n−1/2)
Proof. It will suﬃce to consider R(1)
+ , as the process for R(1)
−is identical. Using


## Page 30


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
30
the independent site approximation W(t),
sup
t∈[0,T ]
sup
φ∈Φ
|R(1)
+ (φ, t)|
≤
Z T
0
sup
φ∈Φ

n−1
n
X
i=1
φi


n
X
j=1
∂jq+
i (ρ(s))Ej(s)

(ρi(s) −ωi(s))

ds
+
Z T
0
sup
φ∈Φ

n−1
n
X
i=1
φi


n
X
j=1
∂jq+
i (ρ(s))Ej(s)

(ωi(s) −ηi(s))

ds
(50)
The second term on the right-hand side of (50) is bounded by ∥Dq+∥∞¯J(T)
R T
0 ∥E(s)∥∞ds.
Turning our attention now to the ﬁrst term, let ˜ω(s) be an independent copy of
ω(s). Using the symmetrisation method (see [9, §3]),
E sup
φ∈Φ

n−1
n
X
i=1
φi


n
X
j=1
∂jq+
i (ρ(s))Ej(s)

(ρi(s) −ωi(s))

≤E sup
φ∈Φ

n−1
n
X
i=1
φi


n
X
j=1
∂jq+
i (ρ(s))Ej(s)

(˜ωi(s) −ωi(s))

≤Rad(Ψ(s; z)),
where Ψ(s; z) = {ψ : ψi = φi
hPn
j=1 ∂jq+
i (ρ(s))Ej(s)
i
, φ ∈Φ}. Finally, apply-
ing [31, Lemma 26.9] with (11) gives
Rad(Ψ(s; z)) ≤∥Dq+∥∞∥E(s)∥∞Rad(Φ(z)) ≲n−1/2∥Dq+∥∞∥E(s)∥∞,
which proves the lemma.
The second terms, R(2)
± , can be bounded almost directly using Lemma A.3.
Indeed, for any T > 0,
E sup
t∈[0,T ]
sup
φ∈Φ
|R(2)
+ (φ, t)| ≤
Z T
0
n−1
n
X
i=1
|Ei(s)|E|q+
i (ρ(s)) −q+
i (η(s))|ds
≤n−1
 Z T
0
∥E(s)∥∞ds
!
[∥Dq+∥1(∥D∗q∥2,1 + γn)Te2T ∥D∗q∥1+
1
2∥Dq+∥2,1 + 1
2γn].
(51)
A similar result also holds for R(2)
−(φ, t). Therefore, it only remains to bound
R(3)
± , which is accomplished in Lemma B.4.
Lemma B.4. For any T > 0,
E sup
t∈[0,T ]
sup
φ∈Φ
(|R(3)
+ (φ, t)| + |R(3)
−(φ, t)|)
≤8δT∥q∥∞∥D∗q∥2
1e2T (∥q∥∞+∥D∗q∥1)
Z T
0
∥E(s)∥∞ds.


## Page 31


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
31
Proof. The result follows by an application of Theorem 2.1, upon observing that
sup
t∈[0,T ]
sup
φ∈Φ
|R(3)
+ (φ, t)| ≤
Z T
0
∥E(s)∥∞n−1
n
X
i=1
|q+
i (η(s)) −q+
i (ηδ(s))|ds
≤∥Dq+∥1
Z T
0
∥E(s)∥∞n−1
n
X
j=1
|ηj(s) −ηδ
j(s)|ds.
Repeating this process for R(3)
−completes the proof.
B.2.4. The discretisation terms D+ and D−
Easily the most involved portion of our proof of Theorem 3.1 involves bounding
the discretisation terms D+ and D−. We demonstrate the process for D+ only,
as it is virtually identical for D−. The ﬁrst step is to compare q+
i (ηδ(s))−q+
i (ηδ◦
χ(s)) to Pn
j=1 ∂jq+
i (ηδ◦χ(s))(ηδ
j(s)−ηδ
j◦χ(s)) by ¯E supt∈[0,T ] supφ∈Φ |D+(φ, t)| ≤
D(1)
+ + D(2)
+ , where
D(1)
+ = E
Z T
0
(nδ)−1
n
X
i=1
q+
i (ηδ(s)) −q+
i (ηδ ◦χ(s))−
n
X
j=1
∂jq+
i (ηδ ◦χ(s))(ηδ
j(s) −ηδ
j ◦χ(s))

ds,
D(2)
+ = sup
t∈[0,T ]
sup
φ∈Φ
E

1
2
Z t
0
n−1
n
X
i,j=1
φi(1 −ρi(s))∂jq+
i (ρ(s))qj(ρ(s))ds
−
Z t
0
(nδ)−1
n
X
i,j=1
φi(1 −ηδ
i (s))∂jq+
i (ηδ ◦χ(s))(ηδ
j(s) −ηδ
j ◦χ(s))ds

.
The error in D(1)
+
is bounded in the following Lemma B.5.
Lemma B.5. For any T > 0, D(1)
+ ≲T(n−1∥q∥∞+ 2δ∥q∥2
∞)n˜Γn.
Proof. A second-order Taylor expansion yields
n
X
i=1
E

q+
i (ηδ(s)) −q+
i (ηδ ◦χ(s)) −
n
X
j=1
∂jq+
i (ηδ ◦χ(s))(ηδ
j(s) −ηδ
j ◦χ(s))

≤1
2
n
X
i,j,k=1
∥∂j∂kq+
i ∥∞E
(ηδ
j(s) −ηδ
j ◦χ(s))(ηδ
k(s) −ηδ
k ◦χ(s))

≤1
2
˜ΓnE


n
X
j=1
|ηδ
j(s) −ηδ
j ◦χ(s)|


2
.


## Page 32


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
32
Given ηδ ◦χ(s), the variables |ηδ
i (s)−ηδ
i ◦χ(s)| for i = 1, . . . , n are conditionally
independent Bernoulli random variables with E|ηδ
i (s) −ηδ
i ◦χ(s)| ≤2δ∥q∥∞.
Therefore,
E


n
X
j=1
|ηδ
j(s) −ηδ
j ◦χ(s)|


2
≤2nδ∥q∥∞+ 4(nδ)2∥q∥2
∞,
from which the result follows directly.
For D(2)
+ , we let ˜ηδ denote the martingale part of ηδ(t):
˜ηδ
i (t) = ηδ
i (t) −
Z t
0
(1 −ηδ
i (s))q+
i (ηδ ◦χ(s)) −ηδ
i (s)q−
i (ηδ ◦χ(s))ds.
Now, D(2)
+ ≤D1 + D+
2 + D−
2 + D3, where
D1 = 1
nE
Z T
0
n
X
i=1

n
X
j=1
∂jq+
i (ηδ ◦χ(s)) ˜ηδ
j(s) −˜ηδ
j ◦χ(s)
δ

ds
D±
2 = 1
nE
Z T
0
n
X
i,j=1

∂jq+
i (ηδ ◦χ(s))
δ
Z s
χ(s)
(ηδ
j ◦χ(u) −ηδ
j(u))q±
j (ηδ ◦χ(u))du
 ds
D3 = E sup
t∈[0,T ]
sup
φ∈Φ

1
2
Z t
0
1
n
n
X
i,j=1
φi(1 −ρi(s))∂jq+
i (ρ(s))qj(ρ(s))ds
−
Z t
0
1
n
n
X
i,j=1
φi(1 −ηδ
i (s))∂jq+
i (ηδ ◦χ(s))qj(ηδ ◦χ(s))s −χ(s)
δ
ds

.
are each to be bounded in turn, beginning with D1 in Lemma B.6.
Lemma B.6. For any T > 0, there is D1 ≤
2T
√
nδ∥q∥1/2
∞( 1
√n∥Dq+∥2,1).
Proof. Letting tr = (rδ) ∧T, ﬁrst observe that
D1 ≤(nδ)−1
⌊T/h⌋
X
r=0
(tr+1 −tr)
n
X
i=1
E
sup
s∈[tr,tr+1]

n
X
j=1
∂jq+
i (ηδ(tr))(˜ηδ
j(s) −˜ηδ
j(tr))

.
This quantity can be controlled in a similar way to Ti,1 of the proof of Theorem
2.2. For each r = 0, . . . , ⌊T/h⌋, denote the martingale
M (r)
i
(t) =
n
X
j=1
∂jq+
i (ηδ(tr))(˜ηδ
j(t) −˜ηδ
j(tr)),
for t ≥tr.
Using Doob’s inequality for martingales [24, eq. (7.38)],
E
sup
s∈[tr,tr+1]
M (r)
i
(t)2 ≤4[E⟨M (r)
i
⟩tr+1 −E⟨M (r)
i
⟩tr],


## Page 33


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
33
where ⟨M (r)
i
⟩is the predictable quadratic variation of M (r)
i
, given by
⟨M (r)
i
⟩t =
Z t
0
n
X
j=1
|∂jq+
i (ηδ(tr))|2((1 −ηδ
j(s))q+
j (ηδ ◦χ(s))
+ ηδ
j(s)q−
j (ηδ ◦χ(s)))ds.
Therefore, E sups∈[tr,tr+1] M (r)
i
(t)2 ≤4δ∥q∥∞
Pn
j=1 ∥∂jq+
i ∥2
∞, which implies the
lemma.
Lemma B.7. For any T > 0, D+
2 + D−
2 ≤4δT∥q∥2
∞∥Dq+∥1.
Proof. In terms of the number of jumps in ηδ
i in the interval [a, b],

Z s
χ(s)
(ηδ
j ◦χ(u) −ηδ
j(u))q+
j (ηδ ◦χ(u))du

≤∥q+
j ∥∞
Z s
χ(s)
|ηδ
j ◦χ(u) −ηδ
j(u)|du ≤δ∥q+
j ∥∞I


X
u∈[χ(s),s]
ηδ
j(u) ≥1

.
Therefore,
D+
2 ≤E
Z T
0
n−1
n
X
i,j=1
∥q+
j ∥∞∥∂jq+
i ∥∞I


X
u∈[χ(s),s]
ηδ
j(u) ≥1

ds
≤δ∥q∥∞∥Dq+∥1n−1
n
X
j=1
E
X
s∈[0,T ]
∆ηδ
j(s).
(52)
It is clear from (5) that E P
s∈[0,T ] ∆ηδ
i (s) ≤2T∥q∥∞, which may be substituted
into (52). Applying the same arguments to D−
2 completes the proof.
It now only remains to control D3. To do so, in Lemma B.8, we ﬁrst bound the
error incurred by estimating ∂jq+
i (ηδ ◦ξ(s))qj(ηδ ◦χ(s)) by ∂jq+
i (ρ ◦χ(s))qj(ρ ◦
χ(s)).
Lemma B.8. For any T > 0,
E
Z T
0
1
n
n
X
i=1

n
X
j=1
∂jq+
i (ηδ ◦χ(s))qj(ηδ ◦χ(s)) −∂jq+
i (ρ ◦χ(s))qj(ρ ◦χ(s))

ds
≲T 2
n e2T (∥q∥∞+∥D∗q∥1)(n∥q∥∞˜Γn + ∥D∗q∥2
1)(nδ∥q∥∞∥D∗q∥1 + ∥D∗q∥2,1 + γn)
+ n−1/2T∥q∥∞(n˜Γn + n1/2θn) + n−1/2T∥D∗q∥F .


## Page 34


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
34
Proof. For the sake of brevity, let dij(x) = ∂jq+
i (x)qj(x). It is a matter of direct
computation to show that
max
k=1,...,n
n
X
i,j=1
∥∂kdij∥∞≤n∥q∥∞˜Γn + ∥Dq+∥1∥D∗q∥1
(53)
and
n
X
i=1



n
X
k=1


n
X
j=1
∥∂kdij∥∞


2


1/2
≲n3/2∥q∥∞˜Γn + ∥(Dq+)(D∗q)∥2,1
≲n3/2∥q∥∞˜Γn + n1/2∥D∗q∥2
F ,
(54)
where we once again make use of the fact that ∥A∥2,1 ≤n1/2∥A∥F for any n×n
matrix A. For the second derivatives, there is
n
X
i,j,k=1
∥∂2
kdij∥∞≲n∥q∥∞θn + n˜Γn∥D∗q∥1 + ∥Dq+∥1γn.
(55)
Applying the Mean Value Theorem for dij together with Theorem 2.1 and (53)
gives,
E
Z T
0
n−1
n
X
i=1

n
X
j=1
dij(ηδ ◦χ(s)) −dij(η ◦χ(s))

ds
≤
Z T
0
n−1
n
X
i,j,k=1
∥∂kdij∥∞E|ηδ
k ◦χ(s) −ηk ◦χ(s)|ds
≲δT 2(n∥q∥∞˜Γn + ∥Dq+∥1∥D∗q∥1)∥q∥∞∥D∗q∥1e2T (∥q∥∞+∥D∗q∥1).
(56)
Finally, by applying Lemma A.3 with fi(x) = Pn
j=1 dij(x) together with (53),
(54), and (55) implies
E
Z T
0
n−1
n
X
i=1

n
X
j=1
dij(η ◦χ(s)) −dij(ρ ◦χ(s))

ds
≲n−1T 2(n∥q∥∞˜Γn + ∥Dq+∥1∥D∗q∥1)(∥D∗q∥2,1 + γn)e2T ∥D∗q∥1
+ n−1/2T∥q∥∞(n˜Γn + n1/2θn) + n−1/2T∥D∗q∥F ,
which, together with (56), implies the lemma.
Next, in Lemma B.9, we bound the error incurred by replacing the remaining
occurrence of ηδ
i by ρi. For brevity, we let
Qρ,δ
i
(s) =
n
X
j=1
∂jq+
i (ρ ◦χ(s))qj(ρ ◦χ(s))s −χ(s)
δ
,
s ≥0,
for each i = 1, . . . , n.


## Page 35


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
35
Lemma B.9. For any T > 0,
E sup
t∈[0,T ]
sup
φ∈Φ

Z t
0
n−1
n
X
i=1
φi(ρi(s) −ηδ
i (s))Qρ,δ
i
(s)

≲T∥Dq+∥∞∥q∥∞(n−1/2 + T(∥D∗q∥2,1 + γn)
+ δT∥q∥∞∥D∗q∥1)e2T (∥q∥∞+∥D∗q∥1).
Proof. First, since t −χ(t) ≤δ for any t > 0, Theorem 2.1 implies
E sup
t∈[0,T ]
sup
φ∈Φ

Z t
0
n−1
n
X
i=1
φi(ηi(s) −ηδ
i (s))Qρ,δ
i
(s)ds

≤4δT 2∥q∥2
∞∥Dq+∥∞∥D∗q∥1e2T (∥q∥∞+∥D∗q∥1).
(57)
Now, we let Ψ(s; z) denote the set of vectors
Ψ(s; z) = {ψ : ψi = φiQρ,δ
i
(s), φ ∈Φ}.
Once again, using [31, Lemma 26.9] and (11), the Rademacher complexity of
this set can be bounded by
Rad(Ψ(s; z)) ≤max
i
|Qρ,δ
i
(s)|Rad(Φ(z)) ≲n−1/2∥q∥∞∥Dq+∥∞.
(58)
Now, by using the symmetrisation method, comparing ηi to ωi and then ωi to
ρi, we ﬁnd
E sup
t∈[0,T ]
sup
φ∈Φ

Z t
0
n−1
n
X
i=1
φi(ηi(s) −ρi(s))Qρ,δ
i
(s)ds

≤T∥Dq+∥∞∥q∥∞E ¯J(T) +
Z T
0
Rad(Ψ(s; z))ds.
(59)
The lemma follows by combining (57), (58), and (59).
Finally, in Lemma B.10, we bound the remaining component of D3.
Lemma B.10. For any T > 0,
sup
t∈[0,T ]
sup
φ∈Φ

1
2
Z t
0
n−1
n
X
i=1
φi(1 −ρi(s))
n
X
j=1
∂jq+
i (ρ(s))qj(ρ(s))ds
−
Z t
0
n−1
n
X
i=1
φi(1 −ρi(s))Qρ,δ
i
(s)ds

≲δ∥q∥∞(1 + T)[n˜Γn∥q∥∞+ ∥Dq+∥1(1 + ∥Dq∥1 + ∥q∥∞)].


## Page 36


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
36
Proof. One can show that for any real valued diﬀerentiable functions f and g,

Z T
0
g(s)

(s −χ(s))δ−1f ◦χ(s) −1
2f(s)

ds

≤2δT (∥f∥∞∥g′∥∞+ ∥g∥∞∥f ′∥∞) + δ∥g∥∞∥f∥∞.
(60)
The result follows from applying (60) with g(s) = φi(1 −ρi(s)) and f(s) =
∂jq+
i (ρ(s))qj(ρ(s)) for each i, j = 1, . . . , n.
Theorem 3.1 now follows from Gronwall’s inequality with respect to (38) and
(43), with the additional terms bounded according to Lemmas B.1–B.10 and
equation (51).
References
[1] Alonso, D. and McKane, A. (2002). Extinction dynamics in mainland-
island metapopulations: a n patch stochastic model. Bulletin of Mathematical
Biology 64, 913–958.
[2] Anderson, D., Ganguly, A., and Kurtz, T. (2011). Error analysis of
tau-leap simulation methods. The Annals of Applied Probability 21, 6, 2226–
2262. MR2895415
[3] Barbour, A. D. and Luczak, M. (2015). Individual and patch behaviour
in structured metapopulation models. Journal of Mathematical Biology 71,
713–733. MR3382730
[4] Barbour, A. D., McVinish, R., and Pollett, P. K. (2015). Connecting
deterministic and stochastic metapopulation models. Journal of Mathematical
Biology 71, 6-7, 1481–1504. MR3419897
[5] Barnes, J. and Hut, P. (1986).
A hierarchical O(N log N) force-
calculation algorithm. Nature 324, 6096, 446.
[6] Boucheron, S., Lugosi, G., and Massart, P. (2013). Concentration in-
equalities: A nonasymptotic theory of independence. Oxford University Press.
[7] Brand, S., Tidesley, M. J., and Keeling, M. J. (2015). Rapid simu-
lation of spatial epidemics: A spectral method. Journal of Theoretical Biol-
ogy 370, 121–134. MR3319448
[8] De Masi, A. (2003). Spin systems with long range interactions. In From
Classical to Modern Probability, P. Picco and J. San Martin, Eds. Springer
Basel AG, 25–81.
[9] Devroye, L. and Lugosi, G. (2001). Combinatorial Methods in Density
Estimation. Springer Series in Statistics. Springer-Verlag New York.
[10] Doob, J. L. (1942). Topics in the theory of Markoﬀchains. Transactions
of the American Mathematical Society 52, 37–64. MR0006633
[11] Doob, J. L. (1945). Markoﬀchains – Denumerable case. Transactions of
the American Mathematical Society 58, 3, 455–473. MR0013857
[12] Dzhaparidze, K. and Van Zanten, J. H. (2001). On Bernstein-type
inequalities for martingales. Stochastic Processes and their Applications 93, 1,
109–117. MR1819486


## Page 37


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
37
[13] Ethier, S. and Kurtz, T. (2005). Markov Processes Characterization
and Convergence. John Wiley & Sons.
[14] Frigo, M. and Johnson, S. G. (1998). FFTW: An adaptive software
architecture for the FFT.
In Proceedings of the 1998 IEEE International
Conference on Acoustics, Speech and Signal Processing, ICASSP’98 (Cat.
No. 98CH36181). Vol. 3. IEEE, 1381–1384.
[15] Gillespie, D. (1976). A general method for numerically simulating the
stochastic time evolution of coupled chemical reactions. Journal of Compu-
tational Physics 22, 4, 404–434. MR0503370
[16] Gillespie, D. (1977).
Exact stochastic simulation of coupled chemical
reactions. Journal of Physical Chemistry 81, 25, 2340–2361.
[17] Gillespie, D. (2001). Approximate accelerated stochastic simulation of
chemically reacting systems. Journal of Chemical Physics 115, 4, 1716–1733.
[18] Gray, A. G. and Moore, A. W. (2001). ‘N-body’ problems in statistical
learning. In Advances in Neural Information Processing Systems 13, T. K.
Leen, T. G. Dietterich, and V. Tresp, Eds. MIT Press, 521–527.
[19] Greengard, L. and Rokhlin, V. (1987). A fast algorithm for particle
simulations. Journal of Computational Physics 73, 2, 325–348. MR0918448
[20] Greengard, L. and Strain, J. (1991). The fast Gauss transform. SIAM
Journal on Scientiﬁc and Statistical Computing 12, 1, 79–94. MR1078797
[21] Hamada, M. and Takasu, F. (2019). Equilibrium properties of the spa-
tial SIS model as a point pattern dynamics – How is infection distributed over
space? Journal of Theoretical Biology 468, 12–26. MR3914494
[22] Hanski, I. (1994). A practical model of metapopulation dynamics. Journal
of Animal Ecology 63, 1, 151–162.
[23] Hodgkinson, L., McVinish, R., and Pollett, P. K. (2018).
Nor-
mal approximations for discrete-time occupancy processes.
arXiv preprint
arXiv:1801.00542.
[24] Klebaner, F. (2012). Introduction to stochastic calculus with applications.
World Scientiﬁc Publishing Company.
[25] L´eonard, C. (1990). Some epidemic systems are long range interacting
particle systems. In Stochastic processes in epidemic theory, C. Picard, Ed.
Springer, New York, 170–183.
[26] Liggett, T. (1999).
Stochastic interacting systems: contact, voter and
exclusion processes. Grundlehren der mathematischen Wissenschaften, Vol.
324. Springer-Verlag.
[27] Liggett, T. (2005). Interacting particle systems. Vol. 276. Springer Sci-
ence & Business Media.
[28] Liggett, T. (2010). Stochastic models for large interacting systems and
related correlation inequalities. Proceedings of the National Academy of Sci-
ences 107, 38, 16413–16419. MR2726545
[29] McVinish, R. and Pollett, P. K. (2014). The limiting behaviour of
Hanski’s incidence function metapopulation model. Journal of Applied Prob-
ability 51, 2, 297–316. MR3217768
[30] Mourrat, J.-C. and Weber, H. (2017).
Convergence of the two-
dimensional dynamic Ising-Kac model to φ4
2. Communications on Pure and


## Page 38


R. McVinish, L. Hodgkinson/Fast simulation of spin systems
38
Applied Mathematics 70, 4, 717–812. MR3628883
[31] Shalev-Shwartz, S. and Ben-David, S. (2014). Understanding machine
learning: from theory to algorithms. Cambridge University Press.
[32] Sznitman, A.-S. (1991). Topics in propagation of chaos. In Ecole d’Et´e
de Probabilit´es de Saint-Flour XIX – 1989, P.-L. Hennequin, Ed. Springer,
Berlin Heidelberg, 165–251. MR1108185
[33] Vitushkin, A. G. (1961). Theory of the Transmission and Processing of
Information. Pergamon Press.
[34] Yang, C., Duraiswami, R., Gumerov, N., and Davis, L. (2003). Im-
proved fast Gauss transform and eﬃcient kernel density estimation. In Pro-
ceedings Ninth IEEE International Conference on Computer Vision. IEEE,
464–471.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
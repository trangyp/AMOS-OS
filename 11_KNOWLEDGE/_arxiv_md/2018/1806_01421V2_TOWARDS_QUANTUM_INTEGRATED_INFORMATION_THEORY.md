---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1806.01421v2
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1806.01421v2_Towards_Quantum_Integrated_Information_Theory

> Source: 1806.01421v2_Towards_Quantum_Integrated_Information_Theory.pdf

> Pages: 15

---


## Page 1


Towards Quantum Integrated Information Theory
Paolo Zanardi1,2, Michael Tomka1,2, Lorenzo Campos Venuti1,2
1 Department of Physics and Astronomy, University of Southern California, Los Angeles, CA 90089-0484, USA
2 Center for Quantum Information Science & Technology,
University of Southern California, Los Angeles, California 90089, USA
Integrated Information Theory (IIT) has emerged as one of the leading research lines in compu-
tational neuroscience to provide a mechanistic and mathematically well-deﬁned description of the
neural correlates of consciousness. Integrated Information (Φ) quantiﬁes how much the integrated
cause/eﬀect structure of the global neural network fails to be accounted for by any partitioned
version of it.
The holistic IIT approach is in principle applicable to any information-processing
dynamical network regardless of its interpretation in the context of consciousness. In this paper we
take the ﬁrst steps towards a formulation of a general and consistent version of IIT for interacting
networks of quantum systems. A variety of diﬀerent phases, from the dis-integrated (Φ = 0) to the
holistic one (extensive log Φ), can be identiﬁed and their cross-overs studied.
arXiv:1806.01421v2  [quant-ph]  9 Dec 2018


## Page 2


2
I.
INTRODUCTION
Over the last decade Integrated Information Theory (IIT), developed by G. Tononi and collaborators, has emerged
as one of the leading research lines in computational neuroscience. IIT aims at providing a mechanistic and mathe-
matically well-deﬁned description of the neural correlates of consciousness [1–4].
The idea is to quantify the amount of cause/eﬀect power in the neural network that is holistic in the sense that
goes beyond and above the sum of its parts. This is done in a bottom-up approach by quantifying how arbitrary parts
of the network (“mechanisms”), in a given state, inﬂuence the future and constrain the past of other arbitrary parts
(“purviews”), in a way that is irreducible to the separate (and independent) actions of parts of the mechanism over
parts of the purview. Iterated at the global network level this process gives rise to a so-called “conceptual structure”,
comprising a family of mechanisms and purviews, where the latter represent the integrated core causes/eﬀects of
the former [2]. A measure of the distance between this conceptual structure with the closest one obtainable from
a suitably partitioned network quantiﬁes how much of the cause/eﬀect structure of dynamical newtwork fails to be
reducible to the sum of its parts. This minimal distance is, by deﬁnition, the Integrated Information (denoted by Φ)
of the network.
In IIT it is then boldly postulated that the larger Φ, the higher is the degree of consciousness of the network
in the given state.
The irreducibility of the causal information-processing structure of the network measured by
Φ is independent of the speciﬁc “wetware” implementing the brain circuitry. It follows that the IIT approach to
consciousness seems to lead to a, rather controversial [5], panpsychist view of the world [4].
Besides, and irrespective of, the applications to consciousness, the IIT approach is in principle applicable to any
information-processing network. For example, applications of IIT to Elementary Cellular Automata and Adapting
Animats have been discussed [6]. Moreover, potential extensions of IIT to more general systems, including quantum
ones, have been proposed in [7, 8] by M. Tegmark (see also [9]).
In this paper we shall make an attempt to formulate a general and consistent version of IIT for interacting networks of
ﬁnite-dimensional and non-relativistic quantum systems. Our approach is going to be a quantum information-theoretic
one: neural networks are being replaced by networks of qudits, probability distributions by non-commutative density
matrices, and markov processes by trace preserving completely positive maps. The irreducible cause/eﬀect structure
of the global network is encoded by a so-called conceptual structure operator. The minimal distance of the latter
from those obtained by factorized versions of the network, deﬁnes the quantum Integrated Information Φ. We would
like to strongly emphasize from the very beginning that:
i) Our goal is not to account for potential quantum features of consciousness. We aim at understanding the role
that, a suitably designed notion of, information integration may play in a) quantum information processing in sensu
lato, and b) in a novel categorization of the diﬀerent phases of quantum matter.
ii) The quantum extension of IIT (QIIT) that we are going to discuss is not unique. In fact, exploring new avenues
toward QIIT is one of the main goals for further investigations.
Here we deem necessary a word of warning: in the following we will often borrow jargon from classical IIT e.g.,
mechanism, repertories, purviews, concepts, conceptual structures,..., these are technical terms (precisely deﬁned in
the paper) which may not be necessarily familiar to quantum information experts and should not be confused with
the ordinary language usage of the same terms.
II.
SETTING THE STAGE
Let Λ be a set of cardinality |Λ| < ∞. For each j ∈Λ there is an associated d−dimensional quantum system
with Hilbert space hj ∼= Cd. Adopting the IIT jargon we will refer to subsets M of Λ as to mechanisms. Usually
Λ will be equipped by a distance function d; in this case we deﬁne the distance between mechanisms M and P
by: dist(M, P) := minx∈M, y∈P d(x, y). Given any Ω⊂Λ we deﬁne HΩ= ⊗j∈Ωhj, with dimension d|Ω|. We will
denote by L(HΛ) (S(HΛ)) the associated operator-algebra (state-space). One has that HΛ ∼= HΩ⊗HΩ′, where Ω′
denotes the complement of Ω(in Λ). The network dynamics will be described by a trace preserving unital CP-map
U : L(HΛ) →L(HΛ) with U(1) = 1. This map has to be thought of as the one-step evolution of a discrete time
process. If U is a CP-map its dual U∗is deﬁned by: ⟨X, U(Y )⟩= ⟨U∗(X), (Y )⟩, ∀X, Y ∈L(HΛ). Given Ω⊂Λ we
deﬁne the noising CP-map NΩby NΩ: L(HΛ) →L(HΛ): X 7→(TrΩX) ⊗1Ω
d|Ω| .
The ﬁrst step in classical IIT is to is to consider pairs M, P ⊂Λ (where the mechanism P is referred to as the purview
of M) and to quantify how the state i.e., a probability distribution, of M (with M ′ being in a maximally random
state) at time t conditions (constraints) the state of P (at time t −1). The quantiﬁcation is obtained measuring the
distance between the conditioned states (referred to as the eﬀect and cause repertoires of P) and the un-conditioned
one. It follows that the ﬁrst step toward a QIIT of is to deﬁne a quantum version of the cause/eﬀect repertoires of
classical IIT [3, 4]. Let us now motivate our choice for the quantum counterparts.


## Page 3


3
 
 
FIG. 1.
The mechanism M in state ΨM conditions (constrains) the future (past) of the purview P by means of the action of
U (U∗). The complement M ′ of M is “noised” and set into the maximally mixed state
1M′
d|M′| .
Eﬀects.– We will denote by p (p′) the degrees of freedom (DOFs) associated with the purview P at time t + 1 (its
complement P ′) and by m (m′) the DOFs associated to the mechanism M at time t (its complement M ′). On purely
classical probabilistic grounds one can write
Pr(p|m) = Pr(q, m)
Pr(m)
=
X
p′,m′
Pr(q, q′, m, m′)
Pr(m)
=
X
p′,m′
Pr(q, q′, m, m′)
Pr(m)Pr(m′) Pr(m′) =
X
p′,m′
Pr(q, q′|m, m′)Pr(m′).
(1)
Here we have assumed that the prior of m and m′ factorizes, i.e., Pr(m, m′) = Pr(m)Pr(m′). Now quantum mechanics
enters in deﬁning the transition probability Pr(q, q′|m, m′) = ⟨p, p′|U(|m, m′⟩⟨m, m′|)|p, p′⟩, where U is the unital CP-
map describing the (one-step) dynamics of the network. Inserting this in the equation above one gets
Pr(p|m) =
X
p′
⟨p|⟨p′|U(|m⟩⟨m| ⊗
X
m′
Pr(m′)|m′⟩⟨m′|)|p′⟩|p⟩
= ⟨p|TrP ′U(|m⟩⟨m| ⊗1M ′
d|M ′| )|p⟩.
(2)
Here we have assumed that the prior for m′ is the uniform unconstrained one, i.e., Pr(m) = d−|M ′|. The last equation
shows that the probability for the purview being in the state p at time t + 1 (conditioned on the mechanism being in
the state m at time t) is the diagonal element |p⟩of the reduced density matrix ρU(P|M) := TrP ′U(|m⟩⟨m| ⊗1M′
d|M′| ).
Causes.– We now consider cause repertoires and denote by p (p′) the degrees of freedom (DOFs) associated with
the purview P at time t −1 (its complement P ′) and by m (m′) the DOFs associated to the mechanism M at time t
(its complement M ′). Using Bayes rule and Eq. (2) (with p and m interchanged) one can write
Pr(p|m) = Pr(m|p)Pr(p)
Pr(m)
= ⟨m|TrM ′U(|p⟩⟨p| ⊗1P ′
d|P ′| )|m⟩Pr(p)
Pr(m)
= Tr

(|m⟩⟨m| ⊗1M ′
d|M ′| ) U(|p⟩⟨p| ⊗1P ′)

.
(3)
Here we used
Pr(p)
d|P ′|Pr(m) = d|M|−|P |−|P ′| = d−(|Λ|−|M|) = d−|M ′|. Using the Hilbert-Schmidt dualand the properties of
reduced density matrices, the equation above becomes
Pr(p|m) = Tr

U∗(|m⟩⟨m| ⊗1M ′
d|M ′| ) (|p⟩⟨p| ⊗1P ′)

= ⟨p|TrP ′U∗(|m⟩⟨m| ⊗1M ′
d|M ′| )|p⟩.
(4)
Again, the last equation shows that the probability for the purview being in the state p at time t −1 (conditioned on
the mechanism being in the state m at time t) is the diagonal element |p⟩of ρU∗(P|M).


## Page 4


4
III.
QIIT
The considerations above naturally lead to a deﬁnition for cause/eﬀect repertoires where we consider the full
quantum density matrix as opposed to just its diagonal entries. We would like to stress that, given the essential role
of entanglement in quantum theory, in our approach we drop out the assumption of conditional independence of the
repertoires and the associated need of virtualization [3]. Also, notice that in this paper we restrict ourselves to the
unital case, in order to have the unconditioned repertoires equal to the maximally mixed state (see below). This is a
simplifying technical assumption, not a key requirement.
Deﬁnition 1a: cause/eﬀect Repertoires: Given the unital U, the state ΨΛ ∈S(HΛ),and M, P ⊂Λ, we deﬁne
the eﬀect (e) and cause (c) repertoire of M over the purview P, by
ρ(x)(P|M) := TrP ′ U(x) ◦NM ′(ΨΛ) = ρ(x)(P|M) := TrP ′ U(x)

ΨM ⊗⊗1M ′
d|M ′|

,
(x = e, c)
(5)
where, ΨN = TrM ′ΨΛ, U(e) = U and U(c) = U∗(Hilbert-Schmidt dual of U).
The set of density matrices ρ(e)(P|M) (ρ(c)(P|M)) encode how the dynamics constrains the future (past) of P,
given that the system is initialized in ΨM and noised over M ′ (see Fig. (1)). From a qualitative physical point of
view one might think in the following way: Λ supports an extended quantum medium that is everywhere at inﬁnite
temperature but over the region M where it has been locally “cooled oﬀ” to some (possibly pure) quantum state
ΨM. The system is then evolved forward (backward) in time by the map U (U∗). The quantities (6) quantiﬁes the
distinguishability of the states obtained in this way from the inﬁnite temperature one if only measurements local to
the region P are allowed.
The next step is to deﬁne the cause/eﬀect information by the information-theoretic distance between the conditioned
and the un-conditioned repertoire ρ(x)(P|∅) = U(x)( 1Λ
d|Λ| ) =
1P
d|P | , (x = e, c). In classical IIT the distance between
repertoires is usually taken to be the Wasserstein distance [3]. In this paper, in view of its salient quantum-information
theoretic properties and simplicity, we will adopt the trace distance between density matrices ρ and σ as a measure
of statistical distinguishability, i.e., D(ρ, σ) := 1
2∥ρ −σ∥1 ∈[0, 1].
Deﬁnition 1b: cause/eﬀect Information: The cause/eﬀect information of M over P is given by
xi(P|M) := D(ρ(x)(P|M), 1P
d|P | ),
(x = e, c).
(6)
A: Repertories for the Swap operation For the sake of illustration we will us the case d = 2 = |Λ| with
U(X) = SXS where S : C2 ⊗C2 →C2 ⊗C2/φ ⊗ψ 7→ψ ⊗φ, is a swap operation. The initial state is taken in
the factorized form ΨΛ = Ψ ⊗Ψ where Ψ is a pure density matrix over C2. One can easily check that the non-
trivial repertoires (notice that U = U∗) are given by ρ(1|1) = 1
2, ρ(2|1) = Ψ, ρ(Λ|1) = 1
2 ⊗Ψ, ρ(2|2) = 1
2, ρ(1|2) =
Ψ, ρ(Λ|2) = Ψ ⊗1
2, ρ(1|Λ) = Ψ, ρ(2|Λ) = Ψ, and ρ(Λ|Λ) = Ψ⊗2. From this it follows xi(1|1) = xi(2|2) = 0, xi(2|1) =
xi(1|2) = xi(1|Λ) = xi(2|Λ) = 1
2, xi(Λ|Λ) = 3
4.
At the technical level the following remarks are now useful:
1) Since pure states have the maximum distance from the maximally mixed state and by distance monotonicity
under partial traces xi(P|M) ≤min{1 −d−|P |, 1 −d−|M|}.
2) For unitary U’s generated by a local Hamiltonian HΛ = P
X⊂Λ, |X|=O(1) HX, the functions xi(P|M), (x = e, c)
fulﬁll a Lieb-Robinson type inequality [11]
xi(P|M) ≤c exp (−a(dist(P, M) −v|t|)) , (x = c, e).
Here a, c > 0 are constants depending on dM, |M|, |P|, and ∥OP ∥. Moreover, v > 0 is the Lieb-Robinson velocity
which depends on HΛ (see Appendix for a proof).
3) The average cause/eﬀect information of a map U is deﬁned by the uniform average of xi(P|M) over all mecha-
nisms/purviews XI(U) :=
1
22|Λ|
P
P,M⊂Λ xi(P|M) =: ⟨xi(P|M)⟩P,M, (x, X = c, e)
4) Using the inequality ∥ρ −σ∥2
1 ≤2S(ρ||σ) one ﬁnds xi(P|M) ≤
1
√
2
p
Smax
P
−S(ρ(x)(P|M)), (x = e, c)
where Smax
P
:= log d|P |, here S denotes the von-Neumann entropy. Introducing the 2-Renyi entropy i.e., S2(ρ) =
−log Tr(ρ2) ≤S(ρ) one gets
xi(P|M) ≤
r
1
2 log
 d|P | ∥ρ(x)(P|M)∥2
2

,
(x = c, e).
(7)


## Page 5


5
This inequality is useful as the purity ∥ρ(x)(P|M)∥2
2 is technically easier to handle than the trace-distance.
Let us illustrate this fact in two ways: the ﬁrst shows that the conditional repertoires purities have a simple
expression in terms of standard multi-point spin correlators; the second shows how, using Eq. (7), one can gain an
insight on the behavior of cause-eﬀect power for typical (Haar) random unitaries.
5) We focus on eﬀect repertoires as everything in the following holds for cause ones by replacing U with U∗. Using
the notation {σ(j)
α }3
α=0 = {1, σ(j)
x , σ(j)
y , σ(j)
z } for the j- th spin (tensorized with the identity over Λ −{j}) one ﬁnds
[10] ΨM = ⊗j∈M|ψj⟩⟨ψj| = Q
j∈M
1
2(1 + λ(j) · σ(j)) = 2−|M| P
β∈Z|M|
4
Q
j∈M λ(j)
βj σ(j)
βj and
∥ρ(e)(P|M)∥2
2 =
1
2|P |
X
α∈Z|P |
4
|
X
β∈Z|M|
4
G(P|M)α,βλβ|2,
(8)
where λα = Q
j∈M λ(j)
αj (similarly for λγ) and
G(P|M)α,β :=
1
2|Λ| Tr

Y
j∈P
σ(j)
αj U

Y
j∈M
σ(j)
βj



, (α ∈Z|P |
4 , β ∈Z|M|
4
)
is a (|P| + |M|)-point (inﬁnite temperature) spin-spin correlator for the CP-map U. Similiar expressions hold for the
cause repertoires.
In the special case |M| = |P| = 1 (i.e., both mechanism and its purview consist of single qubit, say the i-th and
the j-th respectively) ) one has a further simpliﬁcation. Indeed in this case G(j|i)0,0 = 1 and G(j|i)0,β = G(j|i)β,0 =
0, (β = 1, 2, 3) from which it follows ∥ρ(e)(j|i)∥2
2 = 1
2(1+∥G(j|i)λ(i)∥2) where G(j|i)α,β = 2−|Λ| Tr(σ(j)
α U(σ(i)
α )) is 3×3
two-point spin correlator, λ(i) is the Bloch vector of the mechanism state and ∥• ∥denotes the standard euclidean
norm. Moreover the Bloch vector of ρ(e)(j|i) is nothing but G(j|i)λ(i) i.e., ρ(e)(j|i) = 1
2[1 + (G(j|i)λ(i) · σ(j)].
6) For unitary evolutions U and pure and factorized ΨΛ, one can explicitly (Haar) average over U’s [10]
EU
h
∥ρ(x)
U (P|M)∥2
2
i
= 1
2
X
α=±1
d|Λ| + αd|M|
d|Λ| + α
  1
d|P | + α
1
d|P ′|

,
(x = e, c)
(9)
This result is the same for cause and eﬀects repertoires (invariance of the Haar measure under U 7→U †) and its
state independent. If |P| = O(1) and (i.e., the purview not a ﬁnite fraction of |Λ|) then from (9) it follows that
EU
h
d|P |∥ρ(x)
U (P|M)∥2
2
i
= 1 + O(e−|Λ|) which in turn, using (7) and concavity, implies EU [xiU(P|M)] = O(e−|Λ|/2).
This bound holds true for any mechanism M. For |M| = O(Λ) the physical interpretation is that a typical (Haar)
random U will map the initial network state onto a nearly maximally entangled one which locally, for |P| = O(1), will
look almost indistinguishable from the maximally mixed state i.e., the unconditional one. This remark may seem to
suggest that quantum entanglement plays a sort of “negative” role in the type of QIIT we are here trying to develop
(see more about this issue later on).
Examples. The following examples show that the type of causal power deﬁned by Eq. (6) has counter-intuitive
aspects and should, therefore, handled with care. When U = U∗= 1 one has that ρ(x)(P|M) = ΨP ∩M ⊗1P ∩M′
d|P ∩M′| ; now
if ΨΛ = ⊗i∈Λ|ψi⟩⟨ψi| one ﬁnds xi(P|M) = 1 −d−|P ∩M|, (x = c, e). Moreover the XI can be computed using the fact
that |P ∩M| = P
i∈Λ xM(i)xP (i)
XI(1) =
1
22|Λ|
X
xP ,xM∈{0,1}|Λ|
(1 −d−⟨xM,xP ⟩) =
1 −
1
22|Λ|
X
xP ,xM∈{0,1}|Λ|
Y
i∈Λ
d−xM(i)xP (i) = 1 −
3d + 1
4d
|Λ|
.
(10)
Here xM,P ∈{0, 1}|Λ| are bit-strings of length |Λ| which parametrize the sets M and P. Notice that the same result
holds for any totally factorized unitary U = ⊗i∈ΛUi. For one qubit one has XI(1)d=2,|Λ|=1 = 1 −7/8 = 1/8; whereas
for two qubits XI(1)d=2,|Λ|=2 = 1 −49/64 = 15/64. The latter result is identical to the one for U being the swap
between the two qubits (direct computation) showing that the XI of identity can be equal to the one of non trivial
(and integrated) transformation. Moreover, for two qubits, and U = cNOT with Ψ = |1⟩⟨1|⊗2 one ﬁnds (direct


## Page 6


6
computation) XI(cNOT) = 11/64 showing that a non-trivial interaction can have less total cause-eﬀect power that
identity (i.e., doing nothing).
The next deﬁnition captures quantitatively the notion of irreducibility of c/e repertories, namely how far the
conditional repertoires are from those obtainable from disjoint parts of M independently conditioning disjoint parts
of P. The idea of IIT is that only irreducible actions are “real” and exists per se [2].
Deﬁnition 2: Integrated information for mechanisms- Given the mechanism M and the purview P we
consider all possible bi-partitions of them {M1, M2} and {P1, P2}, where X1 ∩X2 = ∅, X1 ∪X2 = X (X = M, P).
We deﬁne the (cause/eﬀect) integrated information (ii) of M over P by
ϕ(x)(P|M) =
min
(Pi,Mi) D[ρ(x)(P|M), ρ(x)(P1|M1) ⊗ρ(x)(P2|M2)] ∈[0, 1], (x = e, c)
(11)
In this deﬁnition the minimum is taken over all the 2|P |+|M|−1 −1 possible pairings (Pi, Mi) (i = 1, 2) diﬀerent
from the trivial one (∅, ∅), (P, M), which would make any repertoire factorizable. Notice that, since the ρ(x)(Pi|Mi)’s
(i = 1, 2) are not the reduced density matrices of ρ(x)(P|M), the factorizability of the latter is a necessary, but not
suﬃcient condition for the vanishing of ϕ(x)(P|M). If (P1, P2) is the partition of P, which achieves the minimum,
then quantum entanglement of ρ(x)(P|M), measured by its distance from the set of separable states over HP1 ⊗HP2,
provides a lower-bound to ϕ(x)(P|M). Moreover, cause/eﬀect information gives an upper bound to the integrated
information (note that ρ(x)(∅|M) = 1, ∀M by normalization)
ϕx(P|M) ≤D(ρ(x)(P|M), ρ(x)(∅|M) ⊗ρ(x)(P|∅)) = xi(P|M),
(x = e, c).
(12)
The bound is saturated in |M| = |P| = 1. In particular, Eq. (12) and remark 2) above imply that integrated
information obeys a Lieb-Robinson type of bound for U’s generated by local-Hamiltonians. This shows that ϕ obeys
locality in the usual sense allowed in non-relativistic quantum theory [11]. Furthermore, Eq. (12) along with the
bounds for cause/eﬀect information in 4) above show that for ﬁnite purviews and typical (Haar) random unitaries
integrated information is exponentially small in the network size.
B: ϕ for the Swap From Eq. (12) one sees that ϕ(1|1) = ϕ(2|2) = 0. Moreover from: ρ(1|Λ) = ρ(1|2) ⊗
ρ(∅|1), ρ(2|Λ) = ρ(2|1) ⊗ρ(∅|2), ρ(Λ|1) = ρ(1|∅) ⊗ρ(2|1), ρ(Λ|2) = ρ(1|2) ⊗ρ(2|∅) and ρ(Λ|Λ) = ρ(1|2) ⊗ρ(2|1), ⇒
ϕ(Λ|1) = ϕ(Λ|2) = ϕ(1|Λ) = ϕ(2|Λ) = ϕ(Λ|Λ) = 0. Finally, ϕ(2|1) = ϕ(1|2) = 1
2∥Ψ −1
2∥1 = 1
2.
Using Eq. (11) one can now, for each mechanism M ⊂Λ, identify two purviews over which M has maximal
irreducible causal power.
Deﬁnition 3: Core causes, eﬀects.– The purview P (e/c)
∗
is a core eﬀect/cause of M, if P (e/c)
∗
= arg maxP ϕ(e/c)(P|M).
The corresponding value of ϕ will be denoted by ϕ(x)(M) := maxP ϕ(x)(P|M) = ϕ(P (x)
∗
|M), (x = e, c). The associ-
ated (global) repertoires are given by ρ(x)(M) := ρ(x)(P (x)
∗
|M) ⊗
1Q(x)
d|Q(x)| , where Q(x) := (P (x)
∗
)′ is the complement of
the core eﬀect/cause of M. The integrated cause/eﬀect information of M is given by ϕ(M) = min{ϕe(M), ϕc(M)}.
If ϕ(M) = 0, then either ϕ(e)(P|M) = 0, ∀P or ϕ(c)(P|M) = 0, ∀P. In the ﬁrst (second) case, the mechanism M
fails to constrain the future (past) on any purview P in an integrated fashion. Either way, such a mechanism is not
regarded as an integrated part of the network and it is dropped out of the picture.
The irreducible causal structure of the network has been so far described at the level of mechanisms. The next
deﬁnition is instrumental in uplifting the construction to the global network level.
Deﬁnition 4: Conceptual Structure operators.– For any mechanism M ⊂Λ the triple (ρc(M), ρe(M), ϕ(M))
with ϕ(M) > 0 is called a concept. The totality of concepts forms a conceptual structure (CS) [3]. Formally one can
encode a CS on a positive semi-deﬁnite operator over (C2)⊗|Λ| ⊗C2 ⊗HΛ, given by
C(U) := 1
2
X
M,α
ϕU(M) |Mα⟩⟨αM| ⊗ρα
U(M),
(13)
where M ⊂Λ, α = e, c, and we have made explicit the U-dependence (but kept implicit the ΨΛ one).
A CS can be also be seen a “constellation” of triples {(ρc(M), ρe(M), ϕ(M)) / M ⊂Λ, ϕ(M) > 0} ⊂S(HΛ) ×
S(HΛ) × [0, 1]. The latter compact set may be referred to as the quantum “Qualia Space” [3].
Given two CS’s, C1 and C2 associated to U1 and U2, respectively, we deﬁne the distance between them as the
(trace-norm) distance bewteen the associated CS operators D(C1, C2) = 1
2∥C1 −C2∥1. More explicitly,
D(C1, C2) = 1
4
X
M,α
∥ϕ1(M)ρ(α)
1 (M) −ϕ2(M)ρ(α)
2 (M)∥1.
(14)


## Page 7


7
In particular, D(C(U1), C(U2)) = 0 iﬀ∀M ⊂Λ one has either ϕU1(M) = ϕU2(M) ̸= 0 and ρα
U1(M) = ρα
U2(M), (α =
c, e), or ϕU1(M) = ϕU2(M) = 0. In words: two conceptual structures are the same iﬀall the core eﬀects/causes
repertoires and the associated integrated-information coincide for all concepts.
It is important to notice that if the repertoires depend continuously on some parameter, e.g., through the map U,
then ϕ(M) will be a continuous function as well. However, core eﬀects/causes may change dis-continuously and this
will be reﬂected by CS operators (13) and functions thereof, e.g., Eq. (14).
C: The CS of the Swap The network supports just two concepts. The conceptual structure operator is given
bu: C(S) = 1
2
P
α=e,c
  1
2|1α⟩⟨1α| ⊗( 1
2 ⊗Ψ) + 1
2|2α⟩⟨2α| ⊗(Ψ ⊗1
2)

. The core eﬀect/cause of M = {1} (M = {2}) is
P = {2} ( P = {1}).
The key idea in IIT is to compare the global cause/eﬀect structure (encoded in our quantum version in (13)) with
those of factorized maps associated to bi-partitioned and decoupled networks. In this way one wants to assess how
the “whole goes beyond and above the sum of its parts” i.e., it exists intrinsically The standard way in classical IIT to
produce factorized maps is by bi-partitioning the total set Λ and by “cutting the connections between the two halves
by injecting them with noise” [3]. We adopt here a natural quantum version of this procedure. Given the (non-trivial)
partition P = {Λ1, Λ2 = Λ′
1}, one can deﬁne
UP = U1 ⊗U2,
Ui : L(HΛi) →L(HΛi): X 7→Ui(X) := TrΛ′
iU(X ⊗1Λ′
i
d|Λ′
i| ),
(i = 1, 2)
(15)
Notice that the Ui’s, while unital, are not in general unitary even if the unpartitioned map U is. We are now ﬁnally
ready to deﬁne the fundamental global quantity of the paper: the Integrated Information, denoted by Φ, of the whole
network. Qualitatively, Φ measures how the integrated cause/eﬀect structure of the quantum network fails to be
described by any partitioned and decoupled version of it.
Deﬁnition 5: Integrated Information.– We deﬁne Quantum Integrated Information (II) by
Φ(U) := min
P D(C(U), C(UP)).
(16)
The minimum here is taken over the set of 2|Λ|−1−1 bi-partitions of Λ. If Φ(U) = 0, we say that the network (Λ, U, ΨΛ)
is dis-integrated. The bi-partition PMIP , for which the minimum in Eq. (16) occurs, is referred to as the Maximally
Irreducible Partition (MIP) in classical IIT, i.e., Φ(U) = D(C(U), C(UPMIP )).
If the network is dis-integrated C(U) = C(UPMIP ), namely there exists a “cut and noising” of the network in two
halves that does not aﬀect its global (integrated) cause/eﬀect structure. The system does not exist as a whole per
se; in a network-intrinsic information-theoretic sense there is no “added value” in combining the two halves. For a
completely factorized ΨΛ and U = 1 one has UP = U, ∀P ⇒Φ(1) = 0.
D: Φ of the Swap We have of course just one partition which dis-integrates both concepts in C(S). Therefore,
using (14) and (16) one has
Φ(S) = 2 × 1
4

∥1
2(1
2 ⊗Ψ) −0∥1 + ∥1
2(Ψ ⊗1
2 ) −0∥1

= 1
2(1
2 + 1
2) = 1
2.
Several remarks are now in order to shed some light on the nature of the quantum II deﬁned by Eq. (16).
7) Φ obeys “time-reversal symmetry” Φ(U∗) = Φ(U) [13] and, for unitary Ui’s, Φ((⊗i∈ΛUi)U) = Φ(U) [14].
8) In spite of the simpliﬁed notation, one should not forget that the conceptual structure operator and, therefore Φ
depends on ΨΛ as well. In this paper we will focus at ﬁrst on completely factorized pure states ΨΛ = ⊗i∈Λ|ψi⟩⟨ψi|. In
this case factorizability of U is a suﬃcient condition for vanishing Φ. In fact, for a given ΨΛ, vanishing Φ is a weaker
property than factorizability of the dynamical map. Take, e.g., any non-factorizable unitary U that is diagonal in a
tensor product basis and ΨΛ to be any basis element. One has that U(ΨM ⊗
1M′
d|M′| ) = ΨM ⊗
1M′
d|M′| , (∀M ⊂Λ). The
action of U, for this ΨΛ, is the same of the identity map and therefore Φ(U) = 0.
9) It is essential to stress that diﬀerent state choices for ΨΛ, e.g., entangled, may result in dramatically diﬀerent
result. For example, even factorized maps may have non-vanishing Φ. To illustrate this intriguing fact let us consider
e.g., d = 2, |Λ| = 2, U = 1, |ΨΛ⟩=
1
√
2(|00⟩+ |11⟩). One can easily see that there is just one concept (supported
by the full Λ) and one partition P = {Λ1 = {1}, Λ2 = {2}}, from which it follows that Φ(1) = 3
4 > 0 [10]. This is
an example of what might be dubbed entanglement activated integration, and it shows a sense in which genuinely
quantum eﬀects may play a “positive” role in our version of IIT.
10) At the quantum level one might deﬁne the minimization (16) over all possible virtual bi-partitions of HΛ [15, 16].
This would provide a lower bound to Φ and a much more stringent, and uniquely quantum, deﬁnition of integration.
Of course at the computational level this would be a tremendous challenge.


## Page 8


8
11) If Ω⊂Λ one can consider the reduced network (HΩ, UΩ, ΨΩ) where: if X ∈L(HΩ) then UΩ(X) := TrΩ′U(X ⊗
1Ω′
d|Ω′| ), and ΨΩ= TrΩ′ΨΛ. If ˜Ω∩Ω̸= ∅⇒Φ(UΩ) ≥Φ(U˜Ω) the reduced network is referred to as a complex [1, 2]. A
network may have many complexes which represent, in a sense, “local maxima” of Φ.
We are now ready to illustrate the rather complex mathematical framework developed so far by means of physically
motivated examples. Let us start with a very simple one.
A.
Partial Swap
Let us consider a basic network with |Λ| = 2, d = 2, ΨΛ = Ψ⊗2 (Ψ pure state paperion), equipped with a “partial
swap” map Ut(X) := eitSXe−itS, (t ∈[0, π
2 ]). One has three mechanisms/purviews M, P = {1}, {2}, Λ = {1, 2}.
Direct computation shows [10]:
ρ(e/c)(1|1) = c2
tΨ + s2
t1,
ρ(e/c)(2|1) = s2
tΨ + c2
t1,
ρ(e/c)(Λ|1) = c2
tΨ ⊗1
2 + s2
t
1
2 ⊗Ψ ± ictst[S, Ψ ⊗1
2 ].
(17)
Identical expressions hold for the repertoires ρ(x)(P|2), (ct = cos t, st = sin t).
Finally, ρ(1|Λ) = ρ(2|Λ) = Ψ
and ρ(x)(Λ|Λ) = Ψ⊗2. One can obtain ϕ for each mechanism (i = 1, 2) ϕe/c
t
(i) =
1
2 max

c2
t, s2
t, min{ s2
t
2 +
q
( s2
t
2 )2 + c2
ts2
t, c2
t
2 +
q
( c2
t
2 )2 + c2
ts2
t}
	
, and ϕe/c
t
(Λ) = 1
2 min{s2
t(2 −s2
t
2 ), c2
t(2 −c2
t
2 )}. It follows that for small (near to
π
2 ) t’s the core eﬀect/cause of {1} is itself ({2}) (analogously for {2}), whereas the core eﬀect/cause of Λ is itself ∀t.
Moreover, there is a window around t = π
4 in which the core eﬀect/cause of {1} and {2} delocalize and comprise the
full Λ. The corresponding jumps of Φ(t) are shown in Fig. 2. The intermediate, high Φ, delocalized phase originates
from the commutator term in (17). It can be regarded as a genuine quantum feature, i.e., it would disappear if Ut
were just a probabilistic mixture of identity and swap.
0.0
0.5
1.0
1.5
0.0
0.1
0.2
0.3
0.4
0.5
0.6
FIG. 2.
Two qubit network.
Solid blue curve: U = exp(i t S).
For small t (near
π
2 ) the network is in the “identity”
(“swap”) phase. The discontinuities at t = cos−1(
p
2/3) and t = cos−1(1/
√
3) are due to a jump and delocalization of the core
cause/eﬀect repertoires. The dashed red curve shows the average of Φ where U = exp(i t HGUE) and HGUE is sampled from
the Gaussian unitary ensemble (GUE) with unit variance.
B.
Permutational networks
Let us now discuss the case of Permutational networks which is another obvious generalization of the Swap case.
Here ΨΛ = ⊗i∈Λ|ψi⟩⟨ψi| and U(X) = UσXU †
σ, where Uσ acts as the permutation σ ∈S|Λ| over HΛ ∼= (Cd)⊗|Λ| i.e.,
Uσ ⊗i∈Λ |ψi⟩= ⊗i∈Λ|ψσ(i)⟩. One can see that [10]
ρ(e)(P|M) = Ψσ−1(P ∩σ(M)) ⊗1P ∩σ(M)′
d|P ∩σ(M)′| = ρ(e)(σ(M) ∩P|M) ⊗ρ(e)(σ(M)′ ∩P|∅)
ρ(e)(σ(M) ∩P|M) = ⊗j∈σ−1(P )∩Mρ(e)(σ(j)|j) ⊗ρ(e)(∅|σ−1(P ′) ∩M).
(18)


## Page 9


9
 
 
FIG. 3.
Permutational networks
(See Fig. (3)). The same equations hold, with σ−1 replacing σ, for the cause repertoires. From this totally factorized
form one sees that the only irreducible (M, P) pairs are given by (i, σ±1(i)) [and that the core eﬀect (cause) of i ∈Λ
is σ(i) (σ−1(i))] with ϕ(i) = 1 −d−1 =: cd. From these results and (13) one has
C(σ) = cd
2
X
i∈Λ,x=±1
|ix⟩⟨ix| ⊗ρ(x)(i),
ρ(x)(i) := |ψσx(i)⟩⟨ψσx(i)| ⊗1{σx(i)}′
d|Λ|−1 .
(19)
Now given the partition P = (Ω, Ω′), (Ω̸= ∅), from the Dis-integration Lemma in the Appendix it follows that the
concepts which are dis-integrated are those whose core eﬀects or/and causes lie on the complementary set. Any
permutation can be factorized in disjoint cycles, if the number of cycles is larger than one, one can choose a partition
the of Λ that gives rise to the same CS and, therefore Φ(σ) = 0. Each of the cycles will give rise to a complex with
locally maximum Φ. If there is just one cycle (and |Λ| > 2) the MIP is anyone of the form P = {{i}, {i}′} in which the
three concepts associated with i, σ(i), σ−1(i) are dis-integrated and all the others left intact (see Fig. (4)). It follows
from (16) that Φ(σ) = 3
2cd = O(1). For |Λ| = 2, just two concepts are dis-integrated by the only possible partition
and Φ(σ) = cd.
 
 
FIG. 4.
On the left: a permutation in S4 which factorizes in two disjoint (order two) cycles. The MIP does not dis-integrate
any concept and this results in Φ = 0. On the right: an order four cycle. Here the MIP dis-integrate three concepts: the core
eﬀect (cause) of site 4 (2) is on the other side of the cut, while both core cause and eﬀect of site 3 are on the other side. This
results (see text) in Φ = 3
2cd.
IV.
HOLISTIC AND LOW-INTEGRATION PHASES
As customary in statistical mechanics one can consider families of increasingly large networks (Λ, UΛ, ΨΛ) and
study how Φ behaves in the “thermodynamical limit” (TDL) |Λ| →∞. If the maps UΛ are associated with unitaries
UΛ = e−itΛHΛ one has to choose how to scale with |Λ| both the times tΛ as well as the Hamiltonians HΛ. For the
former three natural options are: a) t = O(1); b) “constant action” tΛ∥HΛ∥= O(1); c) tΛ := argmaxtΦΛ(t), where
the maximum over t is taken at ﬁxed |Λ|


## Page 10


10
Deﬁnition 6: Holistic Phases When
O(U) :=
lim
|Λ|→∞
log2 Φ(UΛ)
|Λ|
> 0,
(20)
we say that the network (Λ, U, ΨΛ) is the holistic phase in the TDL.
In the holistic phase the system shows the maximal level of integration as an irreducible causal whole. The quantity
O(U) can be referred to as the holistic parameter and it is at most one [17]
To study the diﬀerent integration phases it is useful to consider the following upper bound to Φ [18]
Φ(U) ≤Tr C(U) =
X
M⊂Λ
ϕU(M) ≤Nc(U),
(21)
If Nc(U) = O(|Λ|κ) with κ > 0 then, from (21), it follows that the holistic parameter is vanishing: O(U) =
lim|Λ|→∞|Λ|−1 log2 Φ(U) ≤lim|Λ|→∞|Λ|−1 log2 |Λ|κ = 0. On the other hand, in order to be in the holistic phase, the
network needs to have a number of concepts asymptotically lower bounded by 2a|Λ| (1 ≥a > 0). Whence, if the
concepts are supported only on mechanisms M, such that |M| = κ = O(1), then the network is necessarily in the
non-holistic phase. The permutational case discussed in the former section, where concepts are supported by sites of
Λ only, provides an example of these low Φ networks.
A.
Holistic Phase
In this section we discuss a suﬃcient condition for a network to be in the holistic phase and provide a physical
example. Before doing so we need to deﬁne the “boundary of the partition” Given a (non-trivial) bi-partition P :=
{Λ1, Λ2 = Λ′
1} we deﬁne ∂P := {S ⊂Λ / S ∩Λ1 ̸= ∅∧S ∩Λ2 ̸= ∅}. This set contains |∂P| = 2|Λ| −2|Λ1| −2|Λ2| + 1
elements. Now, one can prove that [19]
Φ(U) ≥1
2
X
M∈∂PMIP
ϕU(M) ≥|∂PMIP |ϕ0
2 ,
(22)
where ϕ0 := minM∈∂PMIP ϕU(M). Notice that |∂PMIP | ≥2|Λ|−1 −1, therefore, in view of the lower bound above,
one is guaranteed to be in the holistic phase if ϕ0 is lower-bounded by a non-zero constant.
●●●●●●●●●●●●●●●●●●●●
●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
●●●●●●●●●●●●●●●●●●●●
■■■■■■■■■■■■■■■■■■■■
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
■■■■■■■■■■■■■■■■■■■■
◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
◆◆◆◆◆◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
●
■
◆
0.0
0.5
1.0
1.5
0
2
4
6
8
(a)
●
●
●
●
●
■
■
■
■
■
◆
◆
◆
◆
◆
●
■
◆
3
4
5
6
7
0
1
2
3
4
5
(b)
FIG. 5.
(a) Φ as a function of the parameter t, for diﬀerent system sizes |Λ| = 3, 4, 5, with ΨΛ = ⊗i∈Λ|+⟩⟨+|i. The red
dashed line shows 2s2
tc2
t. (b) Scaling of Φ with the system size |Λ|, for the three options to ﬁx the time scale a) t = 0.5 (solid
blue line) log2 Φ = 1.04|Λ|−2.60, b) t∥Z∥∞= 2.5 (dashed orange line) log2 Φ = 1.04|Λ|−2.35 and c) t = argmaxtΦΛ(t) (dotted
green line) log2 Φ = 1.04|Λ| −2.29.
Example: |Λ|-local interaction:
Let us consider a qubit network of size |Λ| with
U(X) = eitZXe−itZ, Z := ⊗i∈Λσz
i ,
ΨΛ = ⊗i∈Λ|+⟩⟨+|i =: Π+
Λ.
(23)
In the Appendix is shown that, for M ̸= Λ, one has ϕ(M|M) = 2s2
tc2
t. Whereas, for the case M = Λ one ﬁnds
ϕ(Λ|Λ) = |stct|(1 + |stct|) ≥2s2
tc2
t. Since, by deﬁnition, ϕUt(M) ≥ϕUt(M|M) by setting, e.g., t = π
4 , one ﬁnds


## Page 11


11
ϕ0 ≥1
2. This also shows that the holistic parameter O(Ut) is one for all t ̸= 0, π/2, where it is ill-deﬁned as Φ = 0.
Turning on the global interaction Z (or mixing it with the 1) results in a direct transition from the dis-integrated
phase to the holistic one.
In Fig. 5 (a) we plot Φ(t), for diﬀerent system sizes |Λ| = 3, 4, 5, given the initial state ΨΛ = ⊗i∈Λ|+⟩⟨+|i. As
predicted by the above analytical calculations, we ﬁnd Φ > 2s2
tc2
t, (the dashed red line represents 2s2
tc2
t), and for t = 0
and t = π/2 we obtain Φ = 0. Fig. 5 (b) shows the holistic behaviour of the network, i.e., the exponential scaling of Φ
with the system size |Λ|. In particular, we observe an exponential scaling of Φ for all the three natural prescriptions
for ﬁxing the timescale: a) for t = 0.5 (solid blue line) we get log2 Φ = 1.05|Λ| −2.64, b) for t∥Z∥∞= 2.5 (dashed
orange line), log2 Φ = 1.04|Λ| −2.35 and c) for t = argmaxtΦΛ(t) (dotted green line), log2 Φ = 1.04|Λ| −2.29. The
ﬁts obtained using all the three diﬀerent prescriptions are consistent with a scaling of the form Φ ∼2|Λ|.
B.
Low-integration: O(1)-local interactions
In general, using Lieb-Robinson type arguments, one might be tempted to speculate that k-local (k = O(1))
interactions will give rise to low-integration networks with sub-extensive log2 Φ [10]. Preliminary numerical results
are shown in Fig. 6 in which U(X) = e−itΛHXeitΛH, but now the dynamics is generated by a two-body Hamiltonian
H. Namely, the dynamics are governed by i) the XX Hamiltonian on a ring
HXX =
|Λ|
X
i=1
(σx
i σx
i+1 + σy
i σy
i+1),
ii) by the XX Hamiltonian on a fully connected graph
HXXfc =
|Λ|
X
i<j
(σx
i σx
j + σy
i σy
j ),
iii) by the XXX Hamiltonian on a ring
HXXX =
|Λ|
X
i=1
(σx
i σx
i+1 + σy
i σy
i+1 + σz
i σz
i+1),
and iv) by the XXX Hamiltonian on a fully connected graph
HXXXfc =
|Λ|
X
i<j
(σx
i σx
j + σy
i σy
j + σz
i σz
j ).
The initial state was chosen to be ΨΛ = N
i∈Λ |0⟩⟨0|i, whereas for the holistic example with Z = ⊗i∈Λσz
i , we used the
state ΨΛ = N
i∈Λ |+⟩⟨+|i, where |+⟩=
1
√
2(|0⟩+ |1⟩.
V.
CONCLUSIONS
The main goal of classical Integrated Information Theory (IIT) [1–4] is to provide a mathematical and conceptual
framework to study the neural correlates of consciousness. In this paper we took the ﬁrst steps towards a possible
quantum version of IIT irrespective of its applications to consciousness.
Our approach is a quantum information-theoretic one, in which neural networks are being replaced by networks of
qudits, probability distributions by non-commutative density matrices, and markov processes by completely positive
maps. The irreducible cause/eﬀect structure of the global network is encoded by a so-called conceptual structure
operator. The minimal distance of the latter from those obtained by factorized versions of the network, deﬁnes the
quantum Integrated Information Φ.
We have studied quantum eﬀects in small qubit networks and provided examples, analytical and numerical, of
families of low integration networks. Also, we have demonstrated suﬃcient conditions for the existence of highly
integrated ones and given illustrations.
The scaling of Φ with the network size deﬁnes diﬀerent phases distinguished by a diﬀerent level of integration of their
global cause/eﬀect structure. The study of those phases and cross-overs, their relation to locality and entanglement,


## Page 12


12
●
●
●
●
●
■
■
■
■
■
●HXX
■HXXfc
◆Z
1.6
1.8
2.0
2.2
2.4
2.6
2.8
0
1
2
3
4
◆
◆
◆
◆
◆
3
4
5
6
7
0
1
2
3
4
5
FIG. 6.
Low-integrated and holistic networks: Numerical simulations of Φ, for the two-body Hamiltonian on a ring
HXX = P|Λ|
i=1(σx
i σx
i+1+σy
i σy
i+1), and on a fully connected graph HXXfc = P|Λ|
i<j(σx
i σx
j +σy
i σy
j ), as well as for a |Λ|-local interaction
Z = N|Λ|
i=1 σz
i , are depicted. For HXX (HXXfc) the ﬁt gives log2(Φ) = 2.38 log2 |Λ| −3.15 (log2(Φ) = 2.03 log2 |Λ| −2.58),
illustrating a polynomial growth of the integrated information Φ with the system size |Λ| (low-integration). The same behavior
is also observed for the Heisenberg XXX model. Inset: holistic phase for the |Λ|-local interaction Z. The ﬁt shows log2(Φ) =
1.04|Λ| −2.35, consistent with an exponential scaling Φ ∼2|Λ|. The time-step t for the diﬀerent system sizes |Λ| is ﬁxed by the
“constant action” prescription t∥H∥∞= 2.5.
and in general the question whether the quantum IIT discussed in this paper has any direct bearing on standard
quantum information processing, are challenging tasks for future investigations.
acknowledgements P.Z. thanks the “Waking up Podcast” of Sam Harris for the inception, Giulio Tononi for useful
input and G. Styliaris for help with some of the pictures. Partial support from the NSF award PHY-1819189 is
acknowledged.
[1] G. Tononi, An information integration theory of consciousness. BMC Neurosci 5: 42 (2004).
[2] M. Oizumi, L. Albantakis, and G. Tononi, From the Phenomenology to the Mechanisms of Consciousness: Integrated
Information Theory 3.0, PLoS Comput Biol 10(5): e1003588. doi:10.1371/journal.pcbi.1003588 (2014)
[3] G. Tononi, Integrated Information Theory, Scholarpedia, (2015), URL: www.scholarpedia.org/article/Integrated information theory.
[4] G. Tononi and C. Koch ,Consciousness: here, there and everywhere?, Phil. Trans. R. Soc. B 370, 20140167 (2015).
[5] S. Aaronson, Why I Am Not An Integrated Information Theorist (or, The Unconscious Expander), (2014), URL:
www.scottaaronson.com/blog/?p=1799.
[6] L. Albantakis and G. Tononi, The Intrinsic Cause-Eﬀect Power of Discrete Dynamical SystemsFrom Elementary Cellular
Automata to Adapting Animats, Entropy 17, 5472 (2015).
[7] M. Tegmark, Consciousness as a state of matter, Chaos, Solitons & Fractals 76 (2015) 238270
[8] M.
Tegmark,
Improved
Measures
of
Integrated
Information.
PLoS
Comput
Biol
12(11):
e1005123.
doi:10.1371/journal.pcbi.1005123 (2016)
[9] K. Kremnizer and A. Ranchin, Integrated Information-Induced Quantum Collapse, Found. Phys. 45, 889 (2015).
[10] P. Zanardi et al, unpublished
[11] E. Lieb, D. Robinson, The ﬁnite group velocity of quantum spin systems, Commun. Math. Phys. 28, 251 (1972)
[12] E. Chitambar, and G. Gour, Quantum Resource Theories, arXiv: 1806.06107;
[13] In Fact, from Eq. (5) one sees that causes and eﬀects are exchanged by replacing U with its dual U∗, moreover ϕ(M) is
symmetric under this exchange (∀M). Therefore, C(U∗) = XC(U∗)X†, where X := 1 ⊗σx ⊗1. Since the distance D in
Eq. (16) is unitarily-invariant one gets Φ(U∗) = Φ(U).
[14] Since ρ(x)
(⊗iUi)U(P|M) = (⊗iUi)(ρ(x)
U (P|M)), (∀P, M) ⇒ϕ(⊗iUi)U(M) = ϕU(M) (∥• ∥1-invariance under unitaries) one has
that C((⊗iUi)U) = (1 ⊗(⊗iUi))C(U), ∀U i.e., conceptual structure operators transform covariantly, from Eq. (14), (16),
and using again ∥• ∥1-invariance one obtains Φ((⊗iUi)U) = Φ(U).
[15] P. Zanardi, Virtual quantum systems, Phys. Rev. Lett. 87, 077901 (2001)
[16] P. Zanardi, D. A. Lidar, and S. Lloyd, Quantum Tensor Product Structures are Observable Induced, Phys. Rev. Lett. 92,
060402 (2004).
[17] From Def. 3, Eq. (12) and xi(P|M)
≤
min{1 −d−|P |, 1 −d−|M|}
⇒
ϕ(M)
≤
1 −d|M|. Now D(C1, C2)
≤
1
2
P
M⊂Λ(ϕ1(M) + ϕ2(M)) ≤P|Λ|
|M|=0
  |Λ|
|M|

(1 −d−|M|). From (16) one has Φ(U) ≤

2|Λ| −(1 + d−1)|Λ|
⇒O(U) ≤
1
|Λ| lim|Λ|→∞log2
h
2|Λ|(1 −( 1−d−1
2
)|Λ|i
= 1.


## Page 13


13
[18] By deﬁnition Φ(U) ≤D[C(U), C(UP)], for all partitions P. From Eq. (14) one has D[C(U), C(UP)] = 1
2∥C(U)−C(UP)∥1 ≤
1
2(∥C(U)∥1 + ∥C(UP)∥1 ≤1
2
P
M⊂Λ(ϕU(M) + ϕUP (M)) ≤1
2(Nc(U) + Nc(UP)) ≤Nc(U). Here we have used the fact that
the number of concepts Nc(UP) of the partitioned network is always not larger than the one Nc(U) of the un-partitioned
one ∀P. In the same way one proves Φ(U) ≤P
M⊂Λ ϕU(M).
[19] From the Deﬁnitions(14), (16) and the dis-integration Lemma in the Appendix one has Φ = D(C(U), C(UMIP )) =
1
4
P′
M, α=e,c ∥ϕU(M)ρ(α)
U (M)−ϕUMIP (M)ρ(α)
UMIP (M)∥1, where the sum is over those M ⊂Λ such that either M or its core
cause/eﬀect are in PMIP (as all the other M’s give contribution which are the same for U and UMIP and therefore cancel
out.) In particular the sum is lower bounded by restricting to the subset of M ∈∂PMIP . Since for these dis-integrated
mechanisms ϕUMIP (M) = 0 and ∥ρ(α)
U (M)∥1 = 1 one arrives at the ﬁrst inequality Eq. (22). The second inequality is
obvious.
Appendix A: Lieb-Robinson Bounds for Cause/Eﬀect Information
We now assume that the CP map U is a unitary generated by a local Hamiltonian HΛ, i.e., U(X) = eitHΛXe−itHΛ.
In this case one can show that a Lieb-Robinson type bound holds for the cei (6). Indeed,
2 ei(P|M) = ∥ρ(e)(P|M) −1P
d|P | ∥1 = TrP

OP (ρ(x)(P|M) −1P
d|P | )

= Tr

(OP ⊗1P ′)U(ΨM ⊗1M ′
d|M ′| −1Λ
d|Λ| )

= Tr

˜OP (ΨM ⊗1M ′
d|M ′| −1Λ
d|Λ| )

,
(A1)
where ˜OP := U∗(OP ⊗1P ′). Now one can write ΨM ⊗1M′
d|M′| = TM( 1Λ
d|Λ| ), where TM is a “preparation” CP Map, local
to the M mechanism whose Kraus operators can be given by Ak = |Ψ⟩⟨k| ⊗
1M′
d|M′| ({|k⟩}dM
k=1 is a basis for HM and
∥Ak∥= 1). Therefore,
2 ei(P|M) = Tr

(T ∗
M −1)( ˜OP ) 1Λ
d|Λ|

≤∥(T ∗
M −1)( ˜OP )∥
= ∥T ∗
M( ˜OP ) −˜OP ∥= ∥
X
k
(A†
k ˜OP Ak −A†
kAk ˜OP ∥
≤
X
k
∥A†
k∥∥[ ˜OP , Ak]∥≤dM max
k
∥[ ˜OP , Ak]∥.
(A2)
Now, since ˜OP is the evolution of an operator local at P and the Ak’s are local to M, the Lieb-Robinson holds in the
form
ei(P|M) ≤c exp (−a(dist(P, M) −v|t|)) =: ϵ.
(A3)
Here a, c > 0 are constants depending on dM, |M|, |P|, and ∥OP ∥. Moreover, v > 0 is the Lieb-Robinson velocity,
which depends on HΛ. Since U∗is also generated by a local Hamiltonian (−HΛ), an identical proof holds for ci(P|M).
Finally, in the light of Eqs. (12) and (A3) one has that integrated-information fulﬁlls a Lieb-Robinson bound as well,
i.e., ϕ(e)(P|M) ≤c exp (−a(dist(P, M) −v|t|)) (and a similar one for ϕ(c)).
From the Lieb-Robinson bound, by a standard argument, it also follows that ∥ρ(x)(Λ|M)−ρ(x)( ˜
M ′|∅)⊗ρ(x)( ˜
M|M)∥≤
ϵ, where ˜
M ⊃M is a suitable Lieb-Robinson “fattening” of M. From this inequality by taking traces with respect P ′,
it follows (again) that the repertoires ρ(x)(P|M) with purviews P ⊂˜
M, are exponentially close to the unconditioned
one
1
d|P | .
Appendix B: Holistic phase example
Let us consider a qubit network of size |Λ| with
U(X) = eitZXe−itZ,
Z := ⊗i∈Λσz
i ,
ΨΛ = ⊗i∈Λ|+⟩⟨+|i =: Π+
Λ.
(B1)
For M ̸= Λ, one directly ﬁnds ρ(e/c)(P|M) = (c2
tΠ+
M∩P + s2
tΠ−
M∩P ) ⊗
1P ∩M′
2|P ∩M′| , where Π±
X := ⊗i∈X|±⟩⟨±|i and
ct := cos t, st := sin t. We now focus on the P = M case with |M| > 1 and look for factorizations of the form


## Page 14


14
ρ(e/c)( ˜
M1|M1) ⊗ρ(e/c)( ˜
M2|M2), where (M1, M2) and ( ˜
M1, ˜
M2) are (non-trivial) pairings of M.
Using the above
expression for the repertoires, one has that ρ(e/c)(M|M) −ρ(e/c)( ˜
M1|M1) ⊗ρ(e/c)( ˜
M2|M2) is equal to
Π+
A ⊗(c2
tΠ+
BC −c4
t
1BC
dBC
) ⊗Π+
D + Π−
A ⊗(s2
tΠ−
BC −s4
t
1BC
dBC
) ⊗Π−
D
−s2
tc2
t(Π+
A ⊗1BC
dBC
⊗Π−
D + Π−
A ⊗1BC
dBC
⊗Π+
D),
where A := M1 ∩˜
M1, B = ˜
M1 ∩M2, C := ˜
M2 ∩M1, D := M2 ∩˜
M2, and dBC := 2|B|+|C|. The operator above can be
easily diagonalized giving
σ(X) = {0, c2
t −
c4
t
dBC
, s2
t −s4
t
dBC
, −c2
ts2
t
dBC
, −c4
t
dBC
, −s4
t
dBC
},
with degeneracies {d|M| −4dBC, 1, 1, 2dBC, dBC −1, dBC −1}. From this it follows ∥X∥1 = 2(1 −
c4
t
dBC −
s4
t
dBC ) ≥
2(1 −c4
t −s4
t) = 4s2
tc2
t. The lower bound is achieved when dBC = 1, i.e., M1 = ˜
M1 and M2 = ˜
M2. Finally,
ϕ(M|M) =
min
(Mi, ˜
Mi)
1
2∥ρ(e/c)(P|M) −ρ(e/c)( ˜
M1|M1) ⊗ρ(e/c)( ˜
M2|M2)∥1 = 2s2
tc2
t.
The case M = Λ gives, with a similar calculation, ϕ(Λ|Λ) = |stct|(1 + |stct|) ≥2s2
tc2
t.
Appendix C: Computing Φ
Evaluating quantum II, Eq. (16), involves several combinatorial layers and constitues (as in the classical case [1])
a formidable computational challenge. This implies that this paper entails a non-negligible algorithmic component.
We summarize here below our strategy to compute Φ :
i) Compute ρ(e/c)(P|M) for all non empty M, P ⊂Λ (# of repertoires: 2 (22|Λ| −2|Λ|+1 + 1))
ii) For each non-trivial ρ(e/c)(P|M) compute ϕ (# of pairings of (P, M): (2|M|+|P |−1 −1))
iii) For each M ̸= ∅ﬁnd its core eﬀect/cause P (x)
∗
and associated integrated-information ϕ(x)(M) = maxP ϕ(x)(P|M) =
ϕ(x)(P (x)
∗
|M), (x = e, c). Now the CS (13) is deﬁned for the given U.
iv) Iterate i)–iii) for each partition P of Λ (# partitions of Λ: (2|Λ|−1 −1) to compute C(UP)
v) Compute Φ (Eq. (16) by ﬁnding the partition (MIP) which minimizes D(C(U), C(UP) (Eq. 14).
The total number of steps (for a ﬁxed partition) is P
M,P ⊂Λ(2|M|+|P |−1−1) = 1
2
P|Λ|
|M|,|P |=0
  |Λ|
|M|
 |Λ|
|P |

(2|M|2|P |−2) =
O(32|Λ|/2). As in the classical IIT case, the actual computation of Φ is exponentially costly (in |Λ|) and therefore
provides a challenging task even for networks of moderate size.
Here below state an important technical lemma (proven in the Appendix), which shows how the CS is aﬀected by
partitioning the system (with P = {Λ1, Λ2 = Λ′
1}) and simpliﬁes the algorithms for computing Φ.
 
 
FIG. 7.
Illustration of the dis-integration lemma. The mechanism (purview) M (P) is split in two sub-mechanism M1
and M2 ( P1 and P2) by the partition P. Since the UΛi’s (i = 1, 2)) connects only mechanisms on the “same side” of P the
conditional repertoires factorizes (see Eq. (C1)).
Dis-integration Lemma The cause/eﬀect repertoires of the partitioned map UP are factorized:
ρ(e/c)
UP
(P|M) = ρ(e/c)
U
(P1|M1) ⊗ρ(e/c)
U
(P2|M2),
(C1)


## Page 15


15
where Pi := P ∩Λi, Mi := M ∩Λi, (i = 1, 2) (see Fig. (7).
From the factorized (C1) form it follows that : a)
if both M and P are on the same side of the partition
the ρ(x)(P|M) is unaﬀected b) If they are on opposite sides there is zero cause/eﬀect information (ρ(x)(P|M) =
ρ(x)(P|∅) ⊗ρ(x)(∅|M) =
1P
d|P | ) c) if either one the two is straddling between the partition there is zero ϕ(P|M).
From a)–c) above one sees that all the concepts such that M ∪P (x)
∗
∈∂P are dis-integrated whereas all those that
M ∪P (x)
∗
/∈∂P are left invariant. From Eqs. (14) and (16) we see that, for a given P just the former contributes
to Φ (as the latter cancel being identical for U and UP). The MIP is then the partition that dis-integrates the least
number of concepts in the CS of the undivided system.
Proof.– We deﬁne ΨΩ= ⊗i∈ΩΨi, (∀Ω⊂Λ). From Eqs (5) and the deﬁnition of the factorized map one ﬁnds
ρ(e/c)
P
(P|M) = TrP ′ UP ◦NM ′(ΨΛ), where
UP ◦NM ′(ΨΛ) = ⊗2
i=1Ui

ΨMi ⊗1M ′∩Λi
d|M ′∩Λi|

= ⊗2
i=1TrΛ′
i U

ΨMi ⊗1M ′∩Λi
d|M ′∩Λi| ⊗1Λi′
d|Λ′
i|

.
First notice that
1M′∩Λi
d|M′∩Λi| ⊗
1Λi′
d|Λ′
i| =
1Mi′
d|M′
i| The result follows now from TrP ′ = TrP ′∩Λ1 ⊗TrP ′∩Λ2 and TrP ′∩Λi ◦TrΛ′
i =
Tr(P ′∩Λi)∪Λ′
i = Tr(P ∩Λi)′. Where we used (P ′ ∩Λi) ∪Λ′
i = (P ′ ∪Λ′
i) ∩(Λi ∪Λ′
i) = P ′ ∪Λ′
i = (P ∩Λi)′ = P ′
i.
If in Eq. (16) one considers just a subset of partitions of Λ one ﬁnds an upper-bound of Φ. One can deﬁne a monotonic
family {Φ(k)}|Λ|
k=1 of II measures by deﬁning Φ(k) as in Eq. (16) where the minimization is performed over partitions
(Λ1, Λ′
1) in which |Λ1| ≤k. Notice that i ∈Λ) and that i ≥j ⇒Φ(j)(U) ≥Φ(i)(U) ≥Φ(|Λ|) = Φ, (i, j = 1, . . . , |Λ|, ∀U).
In our numerical experiments we found that often Φ(1) = Φ. When this is the case the minimization in Eq. (16) requires
to consider O(|Λ|) partitions only.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
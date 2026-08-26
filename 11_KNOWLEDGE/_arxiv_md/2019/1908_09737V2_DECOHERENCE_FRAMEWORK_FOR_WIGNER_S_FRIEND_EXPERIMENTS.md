---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.09737v2
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1908.09737v2_Decoherence_framework_for_Wigner_s_friend_experiments

> Source: 1908.09737v2_Decoherence_framework_for_Wigner_s_friend_experiments.pdf

> Pages: 29

---


## Page 1


Decoherence framework for Wigner’s friend experiments
Armando Rela˜no1
1Departamento de Estructura de la Materia, F´ısica T´ermica y Electr´onica, and GISC,
Universidad Complutense de Madrid, Av. Complutense s/n, 28040 Madrid, Spain∗
The decoherence interpretation of quantum measurements is applied to Wigner’s friend experi-
ments. A framework in which all the experimental outcomes arise from unitary evolutions is pro-
posed. Within it, a measurement is not completed until an uncontrolled environment monitorizes
the state composed by the system, the apparatus and the observer. The (apparent) wave-function
collapse and the corresponding randomness result from tracing out this environment; it is thus the
ultimate responsible for the emergence of deﬁnite outcomes. Two main eﬀects arise from this fact.
First, external interference measurements, trademark of Wigner’s friend experiments, modify the
memory records of the internal observers; this framework provides a univocal protocol to calculate
all these changes. Second, it can be used to build a consistent scenario for the recenly proposed
extended versions of the Wigner’s friend experiment.
Regarding [D. Frauchiger and R. Renner,
Quantum theory cannot consistently describe the use of itself, Nat. Comm. 9, 3711 (2018)], this
framework shows that the agents’ claims become consistent if the changes in their memories are
properly taken into account. Furthermore, the particular setup discussed in [C. Brukner, A no-
go theorem for observer-indepdendent facts, Entropy 20, 350 (2018)] cannot be tested against the
decoherence framework, because it does not give rise to well-deﬁned outcomes according to this
formalism. A variation of this setup, devised to ﬁll this gap, makes it possible to assign joint truth
values to the observations made by all the agents. This framework also narrows down the requi-
sites for such experiments, making them virtually impossible to apply to conscious (human) beings.
Notwithstanding, it also opens the door to future relizations on quantum machines.
I.
INTRODUCTION
In 1961, Eugene Wigner proposed a thought experiment to show that a conscious being must have a diﬀerent
role in quantum mechanics than that of an inanimate device [1]. This experiment consists of two observers playing
diﬀerent roles. The ﬁrst one, Wigner’s friend, performs a measurement on a particular quantum system in a closed
laboratory; as a consequence of it, she observes one of the possible outcomes of her experiment. The second one,
Wigner himself, measures the whole laboratory from outside. If quantum theory properly accounts for what happens
inside the laboratory, Wigner observes that both his friend and the measured system are in an entangled superposition
state. Hence, the conclusions of both observers are incompatible. For Wigner’s friend, the reality consists in a deﬁnite
state equal to one of the possible outcomes of her experiment; for Wigner, it consists in a superposition of all these
possible outcomes.
Since then, a large number of discussions, interpretations and extensions have been done. Among them, this work
focus on a recent extended version of this experiment, from which two diﬀerent no-go theorems have been formulated.
The ﬁrst one shows that diﬀerent agents, measuring on and reasoning over the same quantum system, are bound
to get contradictory conclusions [2]. The second one establishes that it is impossible to assign join truth values to
the observations made by all the agents [3]. This extended version of the Wigner’s friend experiment consists of two
closed laboratories, each one with an observer inside, and two outside observers dealing with a diﬀerent laboratory.
All the measurements are performed on a pair of entangled quantum systems, each one being measured in a diﬀerent
laboratory. An experiment to prove the second no-go theorem has been recently done [4].
The key point of the original and the extended versions of the Wigner’s friend experiment is the quantum treatment
of the measurements performed inside the closed laboratories. It is assumed that Wigner’s friend observes a deﬁnite
outcome from her experiment, but the wavefunction of the whole laboratory in which she lives remains in an entangled
superposition state. This is somehow in contradiction with the spirit of the Copenhaguen interpretation, since the
measurement does not entail a non-unitary collapse. Its main shortcoming is not providing a speciﬁc procedure to
determine whether a proper measurement has been performed. It is not clear at all whether an agent has observed
a deﬁnite outcome, or just a simple quantum correlation, implying no deﬁnite outcomes, has been crafted. But, at
the same time, it can be useful in the era of quatum technologies, because it can describe the evolution of a quantum
machine able to perform experiments, infer conclusions from the outcomes, and act as a consequence of them.
∗armando.relano@ﬁs.ucm.es
arXiv:1908.09737v2  [quant-ph]  18 Mar 2020


## Page 2


2
The aim of this work is to provide a framework which keeps the quantum character of all the measurements, while
supplying a mechanism for the (apparent) wavefunction collapse that the agents perceive. This is done by means of
the decoherence interpretation of quantum measurements [5], whose origin comes back to almost forty years ago [6].
The key element of this interpretation is that a third party, besides the measured system and the measuring apparatus,
is required to complete a quantum measurement. It consists in an uncontrolled environment, which cannot be the
object of present or future experiments, and which is the ultimate responsible of the emergence of deﬁnite outcomes,
and the (apparent) wavefunction collapse. Hence, the laboratory in which Wigner’s friend lives must include three
diﬀerent objects: the measured system, the measuring apparatus, and the uncontrolled environment —a quantum
machine performing such an experiment must contain a set of qbits making up the measuring apparatus and the
computer memory, and a second set of qbits forming the environment; the Hamiltonian of the complete machine,
including all these qbits, is supossed to be known. The decoherence formalism establishes that this environment, not
present in standard Wigner’s friend setups [1–4], determines to which states the memory of Wigner’s friend collapses,
and therefore which outcomes are recorded by her. And, at the same time, it guarantees the unitary evolution of the
whole laboratory, making it possible for Wigner to observe the system as an entangled superposition of his friend,
the measuring apparatus, and the environment. Notwithstanding, our aim is not to support this framework against
other possibilities, like wave-function collapse theories, for which the collapse is real and due to slight modiﬁcations
in the quantum theory that only become important for large systems [7]; or recently proposed modiﬁcations of the
Born rule [8]. We just intend to show that: (i) this framework provides a univocal protocol to calculate the state of
the memories of all the agents involved in the experiment, at any time; (ii) it rules out all the inconsistencies arising
from the standard interpretations of Wigner’s friend experiments, and (iii) it narrows down the circumstances under
which such experiments can be properly performed. We can trust in future experiments involving quantum intelligent
machines to determine which is the correct alternative —if any of these.
Our ﬁrst step is to build a simple model for the interaction between the measuring apparatus and the environment.
This model allows us to determine the properties of the interaction and the size of the environment required to give
rise to a proper measurement, as discussed in [5]. Therefore, it can be used to build a quantum machine to perform
Wigner’s friend experiments. Then, we proﬁt from it to discuss the original Wigner’s friend experiment [1], and the
no-go theorems devised in [2, 3]. We obtain the following conclusions. First, the external interference measurement
that Wigner performs on his friend changes her memory record. This change can be calculated, and its consequences
on further measurements can be exactly predicted. Second, the decoherence framework rules out all the inconsistencies
arising from the usual interpretations of these experiments. Finally, it also establishes restrictive requirements for
such experiments.
To avoid all the diﬃculties that conscious (human) beings entail, all the observers are considered quantum machines,
that is, devices operating in the quantum domain, and programmed with algorithms allowing them to reach conclusions
from their own observations. This choice facilitates the challenge of the experimental veriﬁcation (or refutation) of the
results that the decoherence framework provides, against, for example, predictions of wave-function collapse models
[7], or modiﬁcations of the Born rule [8]. Within this spirit, all the Hamiltonians discussed throughout this paper must
be understood as fundamental parts of quantum machines dealing with Wigner’s friend experiments; the Hamiltonians
modelling the algorithms used by any particular setup are far beyond the scope of this paper.
The paper is organised as follows. Sec. II is devoted to the decoherence interpretation of quantum measurements.
A simple numerical model is proposed to guide all the discussions. In Sec. III, the original Wigner’s friend experiment
is studied in terms of the decoherence framework. A numerical simulation is used to illustrate its most signiﬁcative
consequences. In Sec. IV the consistency of the quantum theory is discussed, following the argument devised in [2].
Sec. V refers to the possibility of assigning joint truth values to all the measurements in an extended Wigner’s friend
experiments, following the point of view publised in [3]. Finally, conclusions are gathered in Sec. VI.
II.
DECOHERENCE FRAMEWORK
The ﬁrst aim of this section is to review the decoherence formalism. We have chosen the examples and adapted
the notation to facilitate its application to Wigner’s friend experiments. After this part is completed, we propose a
Hamiltonian model giving rise to the deﬁnite outcomes observed by any agents involved in any quantum experiment,
and we explore its consequences by means of numerical simulations.
A.
Decoherence interpretation of quantum measurements
In all the versions of Wigner’s friend experiments, the protocol starts with a measurement performed by a certain
agent, I. Let us consider that a single photon is the object of such measurement, and let us suposse that the experiment


## Page 3


3
starts from the following initial state,
|Ψ⟩=
r
1
2 (|h⟩+ |v⟩) ,
(1)
where |h⟩denotes that it is horizontally polarised, and |v⟩, vertically polarised.
The usual way to model a quantum measurement consists in a unitary evolution, given by the Hamiltonian that
encodes the dynamics of the system and the measuring apparatus. It transforms the initial state, in which system
and apparatus are uncorrelated, onto a ﬁnal state in which the system and the apparatus are perfectly correlated
1
√
2 (|h⟩+ |v⟩) ⊗|A0⟩−→
1
√
2 (|h⟩⊗|Ah⟩+ |v⟩⊗|Av⟩) ,
(2)
where |A0⟩represents the state of the apparatus before the measurement, ⟨Ah|Av⟩= 0, and ⟨Ah|Ah⟩= ⟨Av|Av⟩= 1.
In [4], an ancillary photon plays the role of the apparatus. In general, such a measurement can be performed by means
of a C-NOT gate. As the choice of |A0⟩is arbitrary, we can consider that |A0⟩≡|Ah⟩, and thus the corresponding
Hamiltonian is given by
H = g
2 |v⟩⟨v| ⊗
[|Ah⟩⟨Ah| + |Av⟩⟨Av| −|Av⟩⟨Ah| −|Ah⟩⟨Av|] ,
(3)
where g is a coupling constant. This Hamiltonian performs Eq. (2), if it is applied during an interaction time given
by gτ = π/2 [5]. The resulting state, which we denote
|Ψ⟩=
r
1
2 (|h⟩|Ah⟩+ |v⟩|Av⟩)
(4)
for simplicity, entails that if the photon has horizontal polarisation, then the apparatus is in state |Ah⟩, and if the
photon has vertical polarisation, then the apparatus is in state |Av⟩. That is, it is enough to observe the apparatus
to know the state of the photon.
As we have just pointed out, this is the usual description of a quantum measurement. Once the state (4) is ﬁxed,
the measurement is completed, and the only remaining task is to interpret the results. This is precisely what is
done in the experimental facility discussed in [4]. In both the original and the extended versions of Wigner’s friend
experiments, the interpretation is the following. The observer inside the laboratory, I, sees that the outcome of the
experiment is either h or v, with probability 1/2, following the standard Born rule; it sees the reality as consisting
in a deﬁnite state corresponding either to |h⟩or |v⟩, according to the information it has gathered. Even more, it can
write that its observation has been completed, making possible for an external obsever, E, to know that I is seeing a
deﬁnite outcome,
|Ψ′
1⟩=
 1
√
2 (|h⟩|Ah⟩+ |v⟩|Av⟩)

⊗|Observation⟩.
(5)
This implies that I has observed a deﬁnite outcome, whereas the whole laboratory in which it lives remains in a
superposition state that can be observed by E, despite knowing that I sees the photon either in horizontal or vertical
polarisation, and not in such a superposition state.
This conclusion is the basis of all the versions of the Wigner’s friend experiment. Notwithstanding, it suﬀers from
two important shortcomings. The ﬁrst one is that the complete laboratory consists just in the measured system
and the measuring apparatus. Hence, there is no place for a quantum device able to act as a consequence of its
measurement —the reasonings to infer contradictory conclusions, as discussed in [2], require a complex machine, not
just a qbit signaling whether the measured photon is vertically or horizontally polarised. Therefore, as is pointed
out in [4], the consideration of Eq. (4) as a proper measurement is questionable. However, this shortcomming is
solvable —at least from a theoretical point of view— just by considering that the apparatus represents, not only the
measuring machine, but also the memory of the observer. We will rely on this interpretation throughout the rest
of the paper; technical considerations are far beyond its scope. Therefore, from now on, the state of any measuring
apparatus will represent the memory record of any quantum machine playing the observer role. After the complete
protocol is ﬁnished, all these records are supposed to be available as the outputs of the quantum computation.
The second one is the basis ambiguity problem [5]. The very same state in Eq. (4), |Ψ1⟩, can be written in diﬀerent
basis,
|Ψ1⟩=
1
√
2 (|α⟩|Aα⟩+ |β⟩|Aβ⟩) ,
(6)


## Page 4


4
where
|α⟩= sin θ |h⟩+ cos θ |v⟩,
(7a)
|β⟩= −cos θ |h⟩+ sin θ |v⟩,
(7b)
|Aα⟩= sin θ |Ah⟩+ cos θ |Av⟩,
(7c)
|Aβ⟩= −cos θ |Ah⟩+ sin θ |Av⟩.
(7d)
That is, the ﬁnal state of the very same measuring protocol, starting from the very same initial condition, can also
be written as the superposition given in Eq. (6) for arbitrary values of θ. This problem blurs the usual interpretation
of all the versions of the Wigner’s friend experiment. As Eq. (6) is a correct representation of agent’s I memory,
we have no grounds to conclude that outcome of its measurement is either h or v, instead of α or β. The unitary
evolution giving rise to the measurement, Eq. (2), does not determine a preferred basis for the corresponding deﬁnite
outcome. Hence, a physical mechanism for the emergence of such an outcome must be provided, in order to not
get stuck on a fuzzy interpretation issue. The main trademark of the decoherence formalism is providing a plausible
mechanism.
There are several ways to solve this problem. One of them consists in modifying the Schr¨odinger equation to model
the wavefunction collapse and to choose the corresponding preferred basis. These theories are based on the fact that
superpositions have been experimentally observed in systems up to 10−21 g, whereas the lower bound for a classical
apparatus is around 10−6 g [7]. This means that the Schr¨odinger equation is just an approximation, which works
pretty well for small systems, but fails for systems as large as measurement devices. Such a real collapse would change
all the dynamics of Wigner’s friend experiments, presumably ruling out all their inconsistencies.
Another possibility, the one which is the object of this work, is that Eq.
(2) is not a complete measurement,
but just a pre-measurement —a previous step required for any observation [5, 9]. Following this interpretation, the
observation is not completed until a third party, an environment which is not the object of the measurement, becomes
correlated with the measured system and the measuring apparatus. This correlation is given again by a Hamiltonian,
and therefore consists in a unitary evolution. If such an environment is continously monitorizing the system [10], the
state of the whole system becomes
|Ψ2⟩=
1
√
2 (|h⟩|Ah⟩|ε1(t)⟩+ |v⟩|Av⟩|ε2(t)⟩) ,
(8)
where the states of the environment |ε1(t)⟩and |ε2(t)⟩change over time, because the apparatus is continuously
interacting with it, and ⟨ε1(t)|ε1(t)⟩= ⟨ε2(t)|ε2(t)⟩= 1. Note that Eq. (8) entails that the correlations betweem the
system and the apparatus remain untouched despite the continuous monitorization by the environment. Hence, the
states |Ah⟩and |Av⟩are called pointer states, because they represent the stable states of the apparatus [5, 6] and the
stable records in the memory of the observers. Furthermore, if such an apparatus-environment interaction implies
⟨ε1(t)|ε2(t)⟩= 0, ∀t > τ, where τ can be understood as the time required to complete the measurement, the following
aﬃrmations hold:
(i) There is no other triorthogonal basis to write the state given by Eq. (8) [11]. That is, the basis ambiguity
problem is ﬁxed by the action of the uncontrolled environment.
(ii) As the observer I cannot measure the environment, its memory record and all the further experiments it can
perform on the system and the apparatus are compatible with the following mixed state
ρ = 1
2 (|h⟩|Ah⟩⟨h| ⟨Ah| + |v⟩|Av⟩⟨v| ⟨Av|) ,
(9)
independently of the particular shapes of both |ε1(t)⟩and |ε2(t)⟩. That is, the observer I sees the system as if it were
randomly collapsed either to |h⟩|Ah⟩or to |v⟩|Av⟩, even though the real evolution of the complete system, including
itself!, is deterministic and given by Eq. (8). Relying on the decoherence framework, such an observer can only
deduce that the real state of the system, the apparatus and itself must be something like Eq. (8) [12]. Randomness
arises through this lack of knowledge.
At this point, it is worth remarking that the decoherent environment must be understood as a fundamental part of
the measuring device, not a practical diﬃculty under realistic condictions —the diﬃculty of keeping the system aside
from external perturbations. If the decoherence framework is applied, any quantum machine must include such an
environment as an inseparable part of it. The trademark of this framework is postulating that deﬁnite —classical—
outcomes arise as a consequence of the continuous environmental monitorization; if such an environment does not
exist, no deﬁnite outcomes are observed. In other words, the observation is completed when the state given by Eq.
(8) is reached: if the observer sees a collapsed state is because an uncontrolled environment is monitorizing the system
(including itself!), and thus the complete wavefunction is given by Eq. (8). The decoherence interpretation of quantum


## Page 5


5
measurements also provides a framework to derive the Born rule from fundamental postulates [9]. Notwidthstanding,
all this work is based just on the previous facts (i) and (ii), and therefore the possible issues in this derivation of the
Born rule are not relevant.
Before ending this section, it is interesting to delve into the diﬀerences between the standard interpretation of
quantum measurements and the one supplied by the decoherence formalism.
Under normal circumstances, both
interpretations provide indistinguishable results. For example, the standard interpretation establises that, once an
agent has observed a deﬁnite outcome in a polarisation experiment, say h, then any further measurements performed
in the same basis are bounded to give the same outcome, h.
This important fact is exactly reproduced by the
decoherence framework. A second measurement with an identical apparatus, denoted A′, performed on Eq. (8) will
give
|Ψ3⟩=
r
1
2 (|h⟩|Ah⟩|A′
h⟩|ϵ1(t)⟩+ |v⟩|Av⟩|A′
v⟩|ϵ2(t)⟩) ,
(10)
if we logically assume that the Hamiltonian modelling the interaction between the apparatus and the environment is
identical for two identical apparati. Therefore, the perception of the observer is given by
ρ = 1
2 (|h⟩|Ah⟩|A′
h⟩⟨h| ⟨Ah| ⟨A′
h| + |v⟩|Av⟩|A′
v⟩⟨v| ⟨Av| ⟨A′
v|) .
(11)
That is, its internal memory says that if it has observed h in the ﬁrst measurement, then it has also observed h in the
second.
In the next sections we will show that the standard interpretation and the decoherence formalism do show important
diﬀerences when the observers are the object of external interference experiments. The key point lies, again, in the role
played by the environment. To perform a proper interference experiment, the external observer must act coherently
on the system, the apparatus (that is, the memory of the internal agent), and the environment. As a consequence
of this action, the state of the environment will eventually change in a perfectly predictable way. And, as it is the
ultimate responsible of the deﬁnite outcome observed by the internal agent, its internal memory will also change
accordingly. We will discuss below how these changes release quantum theory from inconsistencies.
B.
A simple model for the laboratories
The laboratories in which agents I perform their measurements are quantum machines evolving unitarily. Their
Hamiltonians must consist of: (i) a system-apparatus interaction, performing the pre-measurements; and (ii) an
apparatus-environment interaction, following the decoherence formalism. For (i) we consider the logical C-NOT gate
given in Eq. (3). Following [5], for (ii) we propose a model
H = |Ah⟩⟨Ah|
X
n,m
V h
nm |εn⟩⟨εm| +
+ |Av⟩⟨Av|
X
n,m
V v
nm |εn⟩⟨εm| ,
(12)
where V h and V v are the coupling matrices giving rise to the interaction. The only condition for them is to be
hermitian matrices; independently of their particular shapes, the Hamiltonian given by Eq. (12) guarantees that the
correlations |h⟩|Ah⟩and |v⟩|Av⟩remain unperturbed, that is, |Ah⟩and |Av⟩are the pointer states resulting from this
interaction, and the state given by Eq. (8) holds for any time.
To build a simple model, we consider that both V h and V v are real symmetric random matrices of the Gaussian
Orthogonal Ensemble (GOE), which is the paradigmatic model for quantum chaos [13]. They are symmetric square
matrices of size N, with independent Gaussian random elements with mean µ(Vnm) = 0, ∀n, m = 1, . . . , N, and
standard deviation σ(Vnn) = 1, ∀n = 1, . . . , N (diagonal elements); and σ(Vnm) = 1/
√
2, ∀n ̸= m = 1, . . . , N
(non-diagonal elements).
In panel (a) of Fig. 1 we show how the overlap between the two states of the environment, |ε1(t)⟩and |ε2(t)⟩, evolves
with time; in panel (b) how it evolves with the environment size. To perform the calculations, we have considered
that the environment consists in N qbits, and hence the dimension of its Hilbert space is d = 2N. In all the cases,
the initial state is a tensor product
|Ψ(0)⟩=
1
√
2 [|h⟩|Ah⟩+ |v⟩|Av⟩] ⊗|ϵ0⟩,
(13)


## Page 6


6
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 2
 4
 6
 8
 10
|<ε1 | ε2>|2
t
(a)
 0.001
 0.01
 0.1
 1
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
|<ε1 | ε2>|2
N
(b)
FIG. 1. Panel (a), value of |⟨ε1(t)|ε2(t)⟩|2 as a function of time, for environments composed by diﬀerent number of qbits. The
solid curves show, from the upper one to the lower one, N = 1, N = 3, N = 5, N = 7 and N = 9. Panel (b), ﬁnite-size scaling
for the long-time average of |⟨ε1(t)|ε2(t)⟩|2, as a function of the number of qbits composing the environment, N.
L1 The measured system.
L2 The measuring apparatus.
L3 An internal environment, with a chaotic interaction
like the one given by Eq. (12), and large enough to
guarantee |⟨ε1(t)|ε2(t)⟩|2 ∼0.
TABLE I. Parts of laboratories in which the agents I perform their measurements in a Wigner’s friend experiment, following
the decoherence framework.
where |ϵ0⟩is the ﬁrst element of the environmental basis (as the interaction is a GOE random matrix, the particular
shape of the basis is irrelevant [13]). All the results are averaged over 50 diﬀerent realizations. We have considered
ℏ= 1.
Panel (a) of Fig. 1 shows the results of |⟨ε1(t)|ε2(t)⟩|2 for N = 1 (d = 2), N = 3 (d = 8), N = 5 (d = 32),
N = 7 (d = 128), and N = 9 (d = 512). We clearly see that, the larger the number of environmental qbits, the
smaller the value of |⟨ε1(t)|ε2(t)⟩|2 at large times, and the smaller the characteristic time τ required to complete the
measurement process. Therefore, the condition |⟨ε1(t)|ε2(t)⟩|2 ∼0 is fast reached if the number of the environmental
qbits is N ∼10. The results plotted in panel (b) of the same ﬁgure conﬁrm this conclusion. We show there the
long-time average of |⟨ε1(t)|ε2(t)⟩|2, calculated for 2 ≤t ≤10, as a function of the number of environmental qbits. It
is clearly seen that the overlap between these states decreases fast with this number. As a consequence, we can safely
conclude that an agent I operating within a laboratory described by Eq. (12) will observe a state given by Eq. (9).
These results imply that the laboratories in which all the agents perform their measurements must have the structure
summarized in Tab. I. It is worth to note that this structure is independent from any further evolution of the measured
system, after the pre-measurement is completed. For example, let us imagine that the measured system has its own


## Page 7


7
Hamiltonian, and therfore the time evolution for the whole system is governed by
H = HS ⊗IAε + IS ⊗HAε,
(14)
where HS is the Hamiltonian for the measured system, HAε represents the environment-apparatus interaction, given
by Eq. (12), and IS (IAε) is the identity operator for the system (environment-apparatus). As the two terms in this
Hamiltonian commute pairwise, the time evolution of the whole system is
|Ψ(t)⟩=
r
1
2 |η(t)⟩|Ah⟩|ε1(t)⟩+
r
1
2 |υ(t)⟩|Av⟩|ε2(t)⟩,
(15)
where the notation η(t) and υ(t) has been chosen to denote that η(t) is the state which evolves from an initial
condition consisting in an horizontally polarised photon, |η(t)⟩= exp (−iHSt) |h⟩, and υ(t) the state which evolves
from a vertically polarised photon, |υ(t)⟩= exp (−iHSt) |v⟩. Therefore all further measurements of the same agents
are well described by
ρ(t) = 1
2 |η(t)⟩|Ah⟩⟨η(t)| ⟨Ah| + |υ(t)⟩|Av⟩⟨υ(t)| ⟨Av| .
(16)
That is, all the possible experiments that agent I can perform in the future are compatible with the system collapsing
onto either |h⟩or |v⟩after the measurement, and unitarily evolving from the corresponding initial condition. In other
words, and as we have already pointed out, this framework is fully compatible with the Copenhaguen interpretation. . .
but the wave-function collapse being just a consequence of ignoring the environmental degrees of freedom. It is worth
to remark that this is not a subjective interpretation, but the result of a unitary time evolution including a number
of degrees of freedom that cannot be measured by the same observer. Eq. (16) establishes that a further reading of
the agent memory record would reveal that the photon has collapsed either to h or v, and then it has evolved from
the corresponding initial condition.
As the key point in Wigner’s friend experiments consists in further interference measurements on the whole labo-
ratory, a study of the complexity of the state resulting from the time evolution summarized in Fig. 1 is necessary.
Such a study can be made by means of a correlation function C(τ) = |⟨ε1(t)|ε1(t + τ)⟩|2. If C(τ) ∼1, then the time
evolution of the environmental state |ε1(t)⟩is quite simple; its only possible change is an irrelevant global phase. Such
a simple evolution would facilitate further interference experiments. On the contrary, if C(τ) quickly decays to zero,
the same evolution is highly involved, implying that the state of the whole laboratory is complex enough to hinder
further interference experiments.
Results are summarized in Fig. 2. Panel (a) shows C(τ) for the same environments displayed in the same panel
of Fig. 1. It has been obtained after a double average: over 50 diﬀerent realizations, and over 104 diﬀerent values
of the time t. Panel (b) of Fig. 2 displays a ﬁnite size scaling of C(τ) for large values of time versus the number
of environmental qbits, calculated averaging over τ ≥10. It is clearly seen that the results shown in this Figure are
correlated with the ones displayed in Fig. 1. That is, if the environment is large enough to give rise to |⟨ε1(t)|ε2(t)⟩|2 ∼
0, then the environmental states fulﬁll C(τ) ∼0; the smaller the overlap between |ε1(t)⟩and |ε2(t)⟩, the smaller the
value of the correlation function C(τ). It is also worth noting that C(τ) decays very fast to zero; for N = 9, C(τ) ∼0
for τ ≃10−1. This means that the state of the environment is changing fast, and therefore the state of the whole
laboratory, including the measured system, the measuring apparatus and the environment, is very complex.
As we have pointed out above, the key point of all the versions of Wigner’s friend experiments consist in further
interference measurements performed by an external agent, for which the whole laboratory evolves unitarily following
Eq. (8). Both in its original [1] and its extended versions, discussed in [2–4], the external agents perform interference
experiments involving only two states, |Ah⟩|h⟩and |Av⟩|v⟩. The Hilbert spaces of the simpliﬁed versions of the
laboratories discussed in these papers are spanned by {|Ah⟩|h⟩, |Av⟩|v⟩, |Ah⟩|v⟩, |Av⟩|h⟩}. Notwithstanding, the
last two states are never occupied, and hence such two-state interference experiments are feasible [4]. The situation
arising from the decoherence framework is far more complex. The dimension of the whole laboratory, composed by
the measured system, the measuring apparatus, and an environment with N qbits, is d = 2N+2. From the results
summarized in Fig. 2, we conjecture that all the 2N states of the environment are populated, and therefore 2N+1
states of the whole laboratory become relevant for further interference experiments. Hence, the ﬁrst consequence of
the results discussed in this section is that experiments like the ones in [1–4] become extremely diﬃcult. However, as
|⟨ε1(t)|ε2(t)⟩|2 ∼0, it is true that only two states, |h⟩|Ah⟩|ε1(t)⟩and |v⟩|Av⟩|ε2(t)⟩, are populated at each time t; the
rest of the Hilbert space is irrelevant at that particular value of the time t. Unfortunately, these states change very fast
with time, and in a very complex way. Therefore, an interference experiment involving only two states, |h⟩|Ah⟩|ε1(t)⟩
and |v⟩|Av⟩|ε2(t)⟩, would require a very restrictive protocol, whose main requisites are summarized in Tab. II. Only if
such requisites are fulﬁlled, the external agent E can rely on a simpliﬁed basis, composed by |h(τ)⟩≡|h⟩|Ah⟩|ε1(τ)⟩
and |v(τ)⟩≡|v⟩|Av⟩|ε2(τ)⟩, where τ = tE −tI, tI the time at which agent I performs its measurement, and tE


## Page 8


8
 0
 0.2
 0.4
 0.6
 0.8
 1
10-510-410-310-210-1 100 101 102 103 105
C(τ)
τ
(a)
 0.001
 0.01
 0.1
 1
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
C(τ)
N
(b)
FIG. 2. Panel (a), value of C(τ) as a function of τ, for environments composed by diﬀerent number of qbits. The solid curves
show, from the upper one to the lower one, N = 1, N = 3, N = 5, N = 7 and N = 9. Panel (b), ﬁnite-size scaling for the
long-time average of C(τ), as a function of the number of qbits composing the environment, N.
R1 A perfect knowlede of the interaction between the sys-
tem and the apparatus, H, given by Eq. (12).
R2 A perfect knowledge of the environmental initial
state, |ε0⟩.
R3 A perfect knowledge of the time at which agent I
performs its measurement, tI.
R4 A perfect choice of the time at which agent E per-
forms its interference experiment, tE.
TABLE II. Requisites for an extended Wigner’s friend experiment in which the external agent, E, performs an interference
experiment involving only two states.
the same for agent E.
A small error in points R1-R4 would imply that the real state of the laboratory, |Ψ(t)⟩,
had negligible overlaps with both |h(τ)⟩and |v(τ)⟩, and therefore any interference experiments involving just these
two states would give no signiﬁcative outcomes. Notwithstanding, given the promising state-of-the-art in quantum
computing [14], we can trust in future quantum machines able to work with enough precission.
Before applying these conclusions to the original and the extended versions of the Wigner’s friend experiments, it
makes sense to test if these conclusions depend on the particular model we have chosen for the apparatus-environment
interaction.
To tackle this task, we consider more general random matrices V h and V v in Eq.
(12), in which
µ(Vnm) = 0, ∀n, m = 1, . . . , N, σ(Vnn) = 1, ∀n = 1, . . . , N (diagonal elements); and σ(Vnm) = 1/
 √
2 |n −m|α
∀n ̸= m = 1, . . . N (non-diagonal elements). If the parameter α is large, then only very few non-diagonal elements
are relevant, and hence the interaction becomes approximately integrable. On the contrary, if α = 0, GOE (chaotic)
results are recovered.


## Page 9


9
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 0.5
 1
 1.5
 2
 2.5
 3
 3.5
 4
P(r)
r
(a)
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 0.5
 1
 1.5
 2
 2.5
 3
 3.5
 4
P(r)
r
(b)
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 0.5
 1
 1.5
 2
 2.5
 3
 3.5
 4
P(r)
r
(c)
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 0.5
 1
 1.5
 2
 2.5
 3
 3.5
 4
P(r)
r
(d)
FIG. 3. Ratio of consecutive level spacings distribution, P(r), for α = 0.5 [panel (a)], α = 1 [panel (b)], α = 2 [panel (c)],
and α = 4 [panel (d)]. Solid histograms show the numerical results for 2000 matrices with dimension d = 512; green dashed
line, the result for a GOE system, P(r) = 27(r + r2)/

8(1 + r + r2)5/2
, and the blue dashed line, the result for an integrable
system, P(r) = 1/(1 + r)2.
We ﬁx our attention in the degree of chaos of the resulting Hamiltonian. To do so, we study the ratio of consecutive
level spacings distribution, P(r), where rn = sn+1/sn and sn = En+1 −En, {En} being the energy spectrum of the
system. It has been shown [15] that the distribution for standard integrable systems is P(r) = 1/(1 + r)2, whereas
it is P(r) = 27(r + r2)/
 8(1 + r + r2)5/2
for GOE systems; a generic interpolating distribution has been recently
proposed [16].
In Fig. 3 we show the results for four diﬀerent values of α, α = 0.5, α = 1, α = 2, α = 4. They consist in the
average over 2000 realizations of matrices of dimension d = 512. The case with α = 0 (not shown) exactly recovers
the GOE result, as expected. The case with α = 0.5 [panel (a)] is also fully chaotic; its ratio of consecutive level
spacings distribution, P(r), is identical to the GOE result. Things become diﬀerent for larger values of α. The case
α = 1 [panel (b)] is yet diﬀerent from the GOE result, althought its behavior is still highly chaotic. The cases α = 2
[panel (c)] and α = 4 [panel (d)] are very close to the integrable result.
In Fig. 4 we show how the long-time average of |⟨ε1(t)|ε2(t)⟩|2, calculated for 2 ≤t ≤50, scales with the number of
environmental qbits, N, for ﬁve diﬀerent values of α = 0, 0.5, 1, 2, and 4. The results are averaged over 50 diﬀerent
realizations. It is clearly seen that the two fully chaotic cases, α = 0 (circles) and α = 0.5 (sqares), behave in the
same way; the overlap |⟨ε1(t)|ε2(t)⟩|2 decreases with the number of environmental qbits, and therefore we can expect
|ε1(t)⟩and |ε2(t)⟩to become ortogonal if the environment is large enough. The behavior of the case with α = 1 (upper
triangles) is diﬀerent. First, the overlap |⟨ε1(t)|ε2(t)⟩|2 decreases with N, but it seems to reach an asymptotic value for
N ≳7. This fact suggests that a fully chaotic apparatus-environment interaction is required for the scenario described
by the decoherence framework. This conclusion is reinforced with the results for α = 2 (lower triangles) and α = 4
(diamonds). These two cases correspond with (almost) integrable Hamiltonians, and their overlaps |⟨ε1(t)|ε2(t)⟩|2
remain large independently of the number of environmental qbits.


## Page 10


10
 0.001
 0.01
 0.1
 1
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
|<ε1 | ε2>|2
N
FIG. 4. Finite-size scaling for the long-time average of |⟨ε1(t)|ε2(t)⟩|2, as a function of the number of qbits composing the
environment, N.
Solid circles represent the case α = 0; solid squares, α = 0.5; solid upper triangles, α = 1; solid lower
triangles, α = 2, and solid diamons, α = 4.
F1 After the measurement performed by agent I is com-
pleted, the real state of the measured system, the
measuring apparatus and the surrounding environ-
ment (which includes the agent itself) is given by Eq.
(8), with |⟨ε1(t)|ε2(t)⟩|2 ∼0.
F2 All the results obtained by the agent I are compatible
with the mixed state given by Eq. (9). That is, it
sees the system as if it were collapsed onto one of the
possible outcomes of its experiment, despite fact F1.
TABLE III. Summary of the facts consequence of the decoherence interpretation of quantum measurements, for Wigner’s friend
experiments.
C.
Summary of results
The results discussed in the previous section narrow down the circumstances under which Wigner’s friend experi-
ments are feasible, if we take into account the decoherence interpretation of quantum measurements. First, laboratories
in which all the agents work must have the structure given in Tab. I. Second, if external agents want to perform
interference experiments relying on just two basis states, requirements listed in Tab. II are mandatory. And third, if
such circumstances hold, then the facts F1 and F2 listed in Tab. III characterize such experiments. Fact F1 establishes
that an observer cannot get a conclusion about the exact state of the whole system (including itself!) just from the
outcome of as many experiments as it can perform. On the contrary, the very fact of observing a deﬁnite outcome
entails that the observer is a part of a larger, entangled superposition state, including an environment from which the
observer cannot get information. (Note that the decoherence framework establishes that this happens in any quantum
measurement, independently of the existence of an external observer). Fact F2 refers to the practical consequences
of F1. It entails that all the agents involved in an experiment are limited to discuss about the outcomes they obtain,
outcomes that depend both on their measuring apparatus and the environmental degrees of freedom which have been
traced out. If either the apparatus or the environmental degrees of freedom are diﬀerent, then the whole experiment
is also diﬀerent, and thus diﬀerent outcomes can be expected.
III.
STANDARD WIGNER’S FRIEND EXPERIMENTS AND THE DECOHERENCE FRAMEWORK
In this section we discuss the consequences of the decoherence framework in the standard Wigner’s friend experiment
[1]. This discussion sets the grounds to analyze the extended versions of the experiments [2–4].
Let us consider that an internal agent I has performed a measurement on an initial state given by Eq. (1). As we
have explained above, independently of the outcome it observes, the resulting state is given by Eq. (8), which is the


## Page 11


11
result of the unitary evolution due to Hamiltonians (3) and (12). To simplify the notation, we consider the whole
state of the laboratory as follows,
|h(t)⟩= |h⟩|Ah⟩|ε1(t)⟩,
(17a)
|v(t)⟩= |v⟩|Av⟩|ε2(t)⟩,
(17b)
where both |h(t)⟩and |v(t)⟩may in general change with time. Thus, the state after the measurement by agent I is
|Ψ1(t)⟩=
r
1
2 (|h(t)⟩+ |v(t)⟩) .
(18)
Following the protocol proposed by Wigner [1], an external agent, E, performs a measurement on |Ψ1(τ)⟩, at a
particular instant of time τ. Let us consider that the four requisites, R1-R4, of Tab. II are fulﬁlled, and therefore an
interference experiment can be performed with a two-state basis, {|α(τ)⟩, |β(τ)⟩}, given by
|α(τ)⟩= sin θ |h(τ)⟩+ cos θ |v(τ)⟩,
(19a)
|β(τ)⟩= −cos θ |h(τ)⟩+ sin θ |v(τ)⟩,
(19b)
for an arbitrary value of the angle θ. In this basis, the state |Ψ1(τ)⟩reads,
|Ψ1(τ)⟩=
r
1
2 (sin θ + cos θ) |α(τ)⟩+
+
r
1
2 (sin θ −cos θ) |β(τ)⟩.
(20)
Therefore, following the decoherence formalism, and as a consequence of the same kind of unitary evolution than
before, the state resulting from agent E measurement is
|Ψ2(τ)⟩=
r
1
2 (sin θ + cos θ) |α(τ)⟩|A′
α⟩|ε′
1(τ)⟩+
+
r
1
2 (sin θ −cos θ) |β(τ)⟩
A′
β

|ε′
2(τ)⟩,
(21)
where A′ represents its apparatus, and ε′ the environment required by the decoherence framework.
Up to now, we have considered that both the measurement and the correlation between the apparatus A′ and the
environment ε′ happen at time τ. But this consideration is not relevant. Taking into account that both the internal,
A, and the external, A′, apparati are continuously monitorized by their respective environments, the former state
unitarily evolves with a Hamiltonian H = HI ⊗IE + II ⊗HE, where II (IE) represents the identity operator for the
internal (external) laboratory. Therefore, in any moment after the measurement the resulting state is
|Ψ2(t)⟩=
r
1
2 (sin θ + cos θ) |α(t)⟩|A′
α⟩|ε′
1(t)⟩+
+
r
1
2 (sin θ −cos θ) |β(t)⟩
A′
β

|ε′
2(t)⟩,
(22)
with |⟨ε′
1(t)|ε′
2(t)⟩|2 ∼0. And hence, any further experiment performed by agent E, in which the external environment
is not measured, is compatible with the state:
ρE = 1
2 (sin θ + cos θ)2 |α(t)⟩|A′
α⟩⟨A′
α| ⟨α(t)| +
+ 1
2 (sin θ −cos θ)2 |β(t)⟩
A′
β
 
A′
β
 ⟨β(t)| .
(23)
Two remarks are useful at this point. First, as we have pointed out above, the real state of the system is given
by Eq. (22); the mixed state given by Eq. (23) is only a description of what agent E sees, that is, of what agent
E can infer from any further measurements performed by itself, and what it is recorded in its memory. Second, the
interpretation of Eq. (23) is independent of the precise forms of |α(t)⟩and |β(t)⟩. The fact that the internal laboratory
changes with time, as a consequence of the monitorization by its environment, due to the Hamiltonian (12), has no
inﬂuence on agent E conclusions because its apparatus remains pointing at either α or β.


## Page 12


12
As we have explained in the previous section, the main diﬀerence between the decoherence framework and the
standard interpretation of quantum measurements, consisting just in a correlation between the system and the appa-
ratus, is that deﬁnite outcomes arise as a consequence of the environmental monitorization, given by the Hamiltonian
(12), and therefore can be exactly tracked at any instant of time. This fact releases us from the need of choosing a
particular perspective to intepret the results without inconsistencies, as it is proposed in [17]; within the decoherence
framework, we just need to calculate the state of the agents’ memories. So, as the action of an external observer
includes an interaction with the internal environment, one may wonder the consequences of such an action. The
measurement performed by agent E has changed the state of the system from
|Ψ1(t)⟩=
r
1
2 (|h(t)⟩+ |v(t)⟩) ⊗|A′
0⟩|ε′
0⟩,
(24)
where |A′
0⟩and |ε′
0⟩are the (irrelevant) initial states of agent E apparatus and the external environment, to Eq. (22).
The decoherence framework establishes that agent I sees the system as if it were collapsed either onto |h⟩or |v⟩(both
with probability ph = pv = 1/2) as a consequence of tracing out the degrees of freedom of ε, A′ and ε′ from Eq. (24).
But, as the global state has changed onto Eq. (22) as a consequence of agent E measurement, a change of how agent
I perceives the reality is possible. To answer this question, we can rewrite Eq. (22) using the basis {|h⟩, |v⟩}. The
resulting state is
|Ψ2(t)⟩= sin θ
√
2 (sin θ + cos θ) |h⟩|Ah⟩|ε1(t)⟩|A′
α⟩|ε′
1(t)⟩+
+ cos θ
√
2 (sin θ + cos θ) |v⟩|Av⟩|ε2(t)⟩|A′
α⟩|ε′
1(t)⟩+
+ cos θ
√
2 (cos θ −sin θ) |h⟩|Ah⟩|ε1(t)⟩
A′
β

|ε′
2(t)⟩+
+ sin θ
√
2 (sin θ −cos θ) |v⟩|Av⟩|ε2(t)⟩
A′
β

|ε′
2(t)⟩.
(25)
As any further measurements performed by agent I will involve neither its environment, ε, nor agent E apparatus, A′,
nor agent E environment, ε′, the resulting outcomes can be calculated tracing out all these three degrees of freedom.
The result is
ρI = 1
4 (2 −sin 4θ) |h⟩|Ah⟩⟨h| ⟨Ah| +
+ 1
4 (2 + sin 4θ) |v⟩|Av⟩⟨v| ⟨Av| .
(26)
This is the ﬁrst remarkable consequence of the decoherence framework, and shows that one has to be very cautious
when testing claims made at diﬀerent stages of an external interference experiment. Let us imagine that the protocol
discussed in this section, with θ = π/8, has been performed a large number, N, of times. Then, let us suposse that
we acceed to the memory record of agent I —encoded in the pointer states of the apparatus, |Ah⟩and |Av⟩— before
the external interference measurement takes place, in every realization of the experiment. This reading would reveal
us that agent I has observed h roughly N/2 times, and v roughly the same amount of times. Now, let us imagine
that an identical protocol is being performed by a colleague, but with a slight diﬀerence: in every realization, she
reads the internal memory of agent I after the external interference measurement has been completed. Astonishingly,
our colleague’s reading would reveal that agent I has observed h roughly N/4 times, and v roughly 3N/4 times. At
a ﬁrst sight, this conclusion seems preposterous. Our colleague and we are reading an identical internal memory of
an identical quantum machine performing an identical ensemble of experiments, modelled by identical Hamiltonians,
Eqs. (3) and (12); but we claim that the machine has observed h N/2 times, and our colleague claims that this
outcome has occured only N/4 times. This absurd contradiction is easily ruled out if we take into account that the
external measurement modiﬁes the state of the internal environment, which is the ultimate responsible of the deﬁnite
outcomes recorded on the memory of the internal agent, and therefore it also modiﬁes these records. Furthermore,
the decoherence framework provides an exact procedure to calculate these changes, as we have pointed out above.
This signiﬁcative result can be summarized by means of the following statement: if the internal agent I observes a
deﬁnite outcome, then the exernal interference measurement performed by agent E changes its memory record; if this
change does not occur is because agent I has not observed a deﬁnite outcome.
The main conclusion we can gather from this analysis is that a contradiction between two claims, one made before an
external interference measurement, and the other made afterwards, can be the logical consequence of this interference
measurement. Hence, the arguments given in [2], which are based on the same kind of contradictions, must be studied


## Page 13


13
with care, taking into account all the changes due to all the measurements performed throughout all the protocol.
This is the aim of the next section.
To illustrate this analysis, we perform now a numerical simulation covering all the protocol. We study the case
with θ = π/8, and we consider that both environments are composed by 6 qbits —the total size of the Hilbert space
is 215 = 32768. We start from the state resulting from agent I pre-measurement
|Ψ0⟩=
r
1
2 (|h⟩|Ah⟩+ |v⟩|Av⟩) |ε1⟩|A′
α⟩|ε′
1⟩,
(27)
where ε1 and ε′
1 represent the ﬁrst states of the basis used to model the internal and the external environments,
respectively. Note that we have considered the state |A′
α⟩as the zero state of the apparatus, but the results do not
depend on this particular choice. From this state, the system passes through three stages:
Stage 1.- From t = 0 to t = τ1, the internal environment interacts with apparatus A to complete the measurement.
Even though the external agent E has not performed any measurement yet, we also consider a similar interaction for
the external environment —in such a case, the external agent E would see a deﬁnite outcome pointing to zero, that
in this case corresponds to the outcome α. The corresponding Hamiltonian is
H1 =
 
|Ah⟩⟨Ah|
X
n,m
V h
nm |εn⟩⟨εm| + |Av⟩⟨Av|
X
n,m
V v
nm |εn⟩⟨εm|
!
⊗IE+
+
 
|A′
α⟩⟨A′
α|
X
n,m
V α
nm |ε′
n⟩⟨ε′
m| +
A′
β
 
A′
β
 X
n,m
V β
nm |ε′
n⟩⟨ε′
m|
!
⊗II,
(28)
where II represents the identity operator over the laboratory in which agent I lives, and IE the identity operator over
the degrees of freedom corresponding to A′ and ε′.
Stage 2.- From t = τ1 to t = τ2, agent E performs its pre-measurement. We consider that the interaction with the
external environment is switched oﬀ, to model that this part of the measurement is purely quantum [18]. However,
the interaction between the internal apparatus and the internal environment still exists, because the monitorization
is always present after a measurement is completed. The corresponding Hamiltonian is
H2 =
 
|Ah⟩⟨Ah|
X
n,m
V h
nm |εn⟩⟨εm| + |Av⟩⟨Av|
X
n,m
V v
nm |εn⟩⟨εm|
!
⊗IE+
+ g |β(τ1)⟩⟨β(τ1)|

|A′
α⟩⟨A′
α| +
A′
β
 
A′
β
 −|A′
α⟩

A′
β
 −
A′
β

⟨A′
α|

⊗II.
(29)
It is worth remarking that the requirements R1-R4 of Tab. II have been explicitely taken into account. The interaction
leading to agent E pre-measurement is based on |β(τ1)⟩, which is the exact state of the internal laboratory at time
t = τ1. The duration of this stage is exactly τ2 −τ1 = π/(2g).
Stage 3.- From t = τ2 on, the external environment gets correlated with apparatus A′, to complete the measurement
performed by agent E. Hence, the Hamiltonian is again given by Eq. (28).
In summary, the system evolves from the initial state given by Eq. (27), |Ψ0⟩, by means of H1, given by Eq. (28),
from t = 0 to t = τ1; by means of H2, given by Eq. (29), from t = τ1 to t = τ2; and by means of H1 again, from
t = τ2 on. Agent’s I point of view is directly obtained from the real state of the whole system, |Ψ(t)⟩, by tracing out
the degrees of freedom corresponding to ε, A′ and ε′. The resulting state can be written
ρI(t) = Chh(t) |h⟩|Ah⟩⟨h| ⟨Ah| +
+ Chv(t) |h⟩|Ah⟩⟨v| ⟨Av| +
+ Cvh(t) |v⟩|Av⟩⟨h| ⟨Ah| +
+ Cvv(t) |v⟩|Av⟩⟨v| ⟨Av| .
(30)
If Chv ∼0 and Cvh ∼0, agent I sees the system as if it were collapsed onto either |h⟩|Ah⟩, with probability Chh, or
|v⟩|Av⟩, with probability Cvv [19].
Following the same line of reasoning, agent E point of view is obtained from |Ψ(t)⟩by tracing out the external
environment, ε′. The resulting state can be written
ρE(t) = Cαα(t) |α(t)⟩|Aα⟩⟨α(t)| ⟨Aα| +
+ Cαβ(t) |α(t)⟩|Aα⟩⟨β(t)| ⟨Aβ| +
+ Cβα(t) |β(t)⟩|Aβ⟩⟨α(t)| ⟨Aα| +
+ Cββ(t) |β(t)⟩|Aβ⟩⟨β(t)| ⟨Aβ| .
(31)


## Page 14


14
FIG. 5. Panel (a), matrix elements Chh (solid, violet line), Cvv (solid green line), and Cnd =
q
|Chv|2 + |Cvh|2 (dashed blue
line), from Eq. (30). Dotted-dashed lines show the expected values at stage 3. The inset show Chh and Cvv around stage 2.
Panel (b), matrix elements Cαα (solid, violet line), Cββ (solid green line), and Cnd =
q
|Cαβ|2 + |Cβα|2 (dashed blue line),
from Eq. (31). Dotted-dashed lines show the expected values at stage 3. The inset show Cαα and Cββ around stage 2. The
number of qbits of both environment is N = 6, g = 102, τ1 = 10, and τ2 −τ1 = π/200.
The interpretation is the same as before. If Cαβ ∼0 and Cβα ∼0, agent E sees the reality as it if were collapsed
onto either |α(t)⟩|Aα⟩, with probability Cαα, or |β(t)⟩|Aβ⟩, with probability Cββ. It is worth to note that the states
of the internal laboratory |α(t)⟩and |β(t)⟩, change with time, but this is not relevant for agent E point of view.
In panel (a) of Fig. 5 we show the results from agent’s I point of view. The coupling constant is set g = 100;
τ1 = 10, and τ2 −τ1 = π/200. The non-diagonal element, Cnd =
q
|Chv|2 + |Cvh|2 (dotted blue line), is signiﬁcatively
large only at the beginning of the simulation; from results in Fig. 1, we expect that larger environments give rise
to smaller values for Cnd (see Fig. 6 for a deeper discussion). Hence, our ﬁrst conclusion is that agent’s I point
of view is compatible with the photon collapsing either to horizontal or to vertical polarizations. The measurement
performed by agent E, that starts at τ1 = 10, does not alter this fact. However, as we clearly see in the inset of the
same panel, this measurement does change elements Chh (violet line) and Cvv (green line). In the main part of the
panel, we display the expected values, given in Eq. (26), Chh = 1/4, Cvv = 3/4, as black dashed-dotted lines; we can
see that these values are fast reached. Furthermore, we can also see in the inset that this is a smooth change, due to
the physical interaction between the laboratory and the apparatus A′. Therefore, agent’s I point of view continuously
changes during this small period of time. As we have already pointed out, the dependence of the Hamiltonian (29)
on the internal environmental states alter the deﬁnite outcomes observed by agent I, and therefore the records of its
internal memory. Thus, this simulation illustrates how the apparent contradiction discussed above is solved.
Panel (b) of Fig. 5 represents agent’s E point of view. Before performing the measurement, its apparatus points α


## Page 15


15
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0
 20
 40
 60
 80
 100
Cnd
t
 0.05
 0.1
 0.15
 3
 4
 5
 6
<Cnd>
N
FIG. 6.
Cnd =
q
|Chv|2 + |Cvh|2, from Eq. (30), for an environment with N = 3 qbits (light green line) (dashed blue line),
and for an environment with N = 6 qbits (dark red line). In the inset, scaling analysis for the time average of Cnd obtained
from t = 3 to t = 100.
 0.2
 0.25
 0.3
 0.35
 0.4
 0.45
 0.5
 0.55
 0.6
 0
 5
 10
 15
 20
Chh
t
FIG. 7. Chh from Eq. (30) for diﬀerent coupling constants g in Eq. (29): g = 1 (blue line), g = 10 (green line), g = 100 (violet
line). Dotted-dashed line shows the expected value for stage 3.
because this is chosen as zero. Then, at t = τ1 this point of view starts to change. Cαα (solid violet line) changes to
Cαα = 0.854, the expected value from Eq. (23), and equally Cββ (solid green line) changes to Cββ = 0.146. During
the ﬁrst instants of time after the pre-measurement, the non-diagonal element Cnd =
q
|Cαβ|2 + |Cβα|2 (blue dotted
line) is signiﬁcatively diﬀerent from zero; but, after the external environment has played its role, agent E point of view
becomes compatible with the laboratory collapsed either to α (with probability p = 0.854) or to β (with probability
p = 0.146) as expected.
A ﬁnite-size scaling analysis of the non-diagonal element of ρI is given in Fig. 6. Due to the huge size of the whole
Hilbert space, it is not possible to reach large environmental sizes. However, we clearly see in the inset how the size
of this non-diagonal element, Cnd, averaged from t = 3 to t = 100, decays with the number of environmental qbits.
Furthermore, a visual comparison between the cases with N = 3 (green line) and N = 6 (red line), given in the main
panel of the same ﬁgure, corroborates this impression. Therefore, we can conjecture that both agents I and E see
their measured systems as if they were collapsed, provided that their corresponding environments are large enough.
Finally, we study how the results depend on the coupling constant between the external apparatus, A′, and the
laboratory whose state is measured by agent E. In Fig. 7 we show Chh for N = 6 and g = 1 (blue line), g = 10
(green line), and g = 100 (violet line), together with the expected value, Chh = 1/4 (dotted-dashed black line).
We conclude that this expected value is reached only if g is large enough. The explanation is quite simple. If g


## Page 16


16
is small, the time required for the external apparatus A′ to complete the pre-measurement is large compared with
the characteristic correlation time of the laboratory, given in Fig. 2. Therefore, the state β(τ1), used in Eq. (29),
ceases to be the real state of the laboratory while the external apparatus, A′, is still performing the pre-measurement.
As a consequence, the resulting measurement is not correct, and neither agent E nor agent I reach the expected
results. This is an important fact that diﬃcults a bit more the external interference measurements trademark of
Wigner’s friend experiments. Besides the requirements R1-R4 of Tab. II, it is also mandatory that the external
pre-measurement is shorter than the characteristic time of the internal dynamics of the measured laboratory. As it is
shown in Fig. 2, the larger the internal environment, the shorter this time. Hence, if agent I is a conscious (human)
being, composed by a huge number of molecules, the external interference pre-measurement must be completed in a
tiny amount of time.
The ﬁrst conclusion we can gather from all these results is that, according to the decoherence framework, the
memory records of all the agents involved in a Wigner’s friend experiment will generically change after the actions of
any other agents, and therefore we must take these changes into account when comparing claims made at diﬀerent
stages of the experiment. As we will see in next sections, this is the clue to interpret the extended versions of the
experiment.
Notwithstanding, agent I still sees the reality as if the measured photon were either horizontally or vertically
polarised —not in a superposition of both states. Even more, states ρE, given by Eq. (23), and ρI, given by Eq.
(26), seem incompatible at a ﬁrst sight. But this is just a consequence of the diﬀerences between the experiments
performed by these two agents. Agent I sees the universe as if it were in state ρI, because it ignores ε, A′ and ε′.
On the other hand, agent E sees the universe as if it were in state ρE, because it just ignores ε′, and therefore has
relevant information about A′ and ε. And, even more important, both agents agree that their perceptions about the
reality are linked to the limitations of their experiments, and that the real state of the universe is a complex, entangled
and superposition state involving the measured photon, both their apparatus, both the environments that surround
them, and themselves —neither ρI, nor ρE. Nevertheless, one of the most remarkable consequences of the decoherence
framework is that this fact does not prevent any of the agents from making right claims about the outcomes observed
by the others. We will see in next sections that the four agents involved in the extended version of the Wigner’s friend
experiment discussed in Refs. [2–4] can make right —not contradictory— claims about the other agents outcomes just
considering: (i) the results of their own experiments, that is, the records of their own memories, and (ii) how external
interference measurements change these records. No other ingredients, like the point of view change proposed in [17]
are required.
IV.
CONSISTENCY OF THE QUANTUM THEORY
The aim of this section is to discuss the thought experiment proposed in [2] within the framework presented above.
A number of comments and criticisms have been already published, including [3] itself, and some others [20–23]. This
work deals with the original proposal in [2].
A.
No-go theorem and original interpretation
Both no-go theorems discussed in [2, 3] share a similar scheme:
(a) A pair of entangled quantum systems is generated. In [2] it consists in a quantum coin, with an orthogonal
basis given by {|head⟩R, |tail⟩R}, and a 1/2-spin, spanned by {|↓⟩S, |↑⟩S}. The initial entangled state is
|Ψ⟩=
r
1
3 |head⟩R |↓⟩S +
r
2
3 |tail⟩R |→⟩S ,
(32)
where |→⟩S =
q
1
2 (|↓⟩S + |↑⟩S).
To simplify the notation and make it compatible with [3, 4], the following changes are made: (i) instead of the
quantum coin and the spin in Eq. (32), two polarised photons are used; (ii) the ﬁrst photon is denoted by the subindex
a, and the second one, by the subindex b; (iii) the superpositions of vertical and horizontal polarisation are denoted
|+⟩=
q
1
2 (|h⟩+ |v⟩) and |−⟩=
q
1
2 (|h⟩−|v⟩), respectively. With this notation, the initial state in [2] reads
|Ψ⟩=
r
1
3 |h⟩a |v⟩b +
r
2
3 |v⟩a |+⟩b .
(33)
(b) Photon a is sent to a closed laboratory A, and photon b, to a closed laboratory B.


## Page 17


17
(c) An observer IA, inside laboratory A, measures the state of photon a; and an observer IB, inside laboratory B,
measures the state of photon b.
(d) An external observer EA measures the state of the whole laboratory A, and an external observer EB measures
the state of the whole laboratory B.
Both no-go theorems [2, 3] deal with the observations made by IA, IB, EA, and EB. The one formulated in [2] is
based upon the following assumptions:
Assumption Q.- Let us consider that a quantum system is in the state |Ψ⟩. Then, let us suppose that an experiment
has been performed on a complete basis {|x1⟩, . . . , |xn⟩}, giving an unknown outcome x. Then, if ⟨Ψ| πm |Ψ⟩= 1,
where πm = |xm⟩⟨xm|, for a particular state of the former basis, |xm⟩, then I am certain that the outcome is x = xm.
Assumption C.- If I am certain that some agent, upon reasoning within the same theory I am using, knows that a
particular outcome x is x = xm, then I am also certain that x = xm.
Assumption S.- If I am certain that a particular outcome is x = xm, I can safely reject that x ̸= xm.
The theorem says that there exist circumstances under which any quantum theory satisfying these three assumptions
is bound to yield constradictory conclusions. The extended version of the Wigner’s friend experiment discussed in [2]
constitutes one paradigmatic example of such circumstances.
Before continuing with the analysis, it is worth to remark that the theorem focuses on particular outcomes that
happen for certain —with probability p = 1. It refers neither to the real state of the corresponding system, nor to a
subjective interpretation made by any of the agents. Hence, its most remarkable feature is that contradictions arise
as consequences of simple observations.
Let us review now all the steps of the experiment from the four agents’ points of view. As it is explained in [2],
to infer their conclusions they need: (i) the knowledge of the initial state of the whole system; (ii) their outcomes;
(iii) the details of the experimental protocol, in order to predict future outcomes, or track back past ones, relying
on the unitary evolutions of the corresponding (pre)measurements. We do not go into details about the assumptions
required to reach each conclusion; we refer the reader to the original paper [2] for that purpose. Moreover, we do not
consider now the decoherence framework; all the measurements are understood as correlations between the measured
(part of the) system and the measuring apparatus.
Step 1.- Agent IA measures the initial state, given by Eq. (33), in the basis {|h⟩a , |v⟩a}.
Fact 1: Given the shape of the initial state, agent IA concludes that, if it obtains that photon a is vertically polarised
(outcome va), then, a further measurement of the laboratory B in the basis {|+⟩B , |−⟩B} will lead to the outcome
+B.
The resulting state of agent’s IA measurement is
|Ψ⟩1 =
r
1
3 |h⟩a |v⟩b |Ah⟩a +
r
2
3 |v⟩a |+⟩b |Av⟩a .
(34)
This expression can be simpliﬁed considering the whole state of the laboratory A which consists in the photon a
and the measuring apparatus Aa. Hence, let us denote
|h⟩A ≡|h⟩a |Ah⟩a ,
(35a)
|v⟩A ≡|v⟩a |Av⟩a .
(35b)
And, therefore, the state after this measurement is
|Ψ1⟩=
r
1
3 |h⟩A |v⟩b +
r
2
3 |v⟩A |+⟩b .
(36)
Fact 1 seems compatible with this state. There is a perfect correlation between state |v⟩A, which represents the
case in which agent IA has observed that the photon a is vertically polarised, and state |+⟩b. Thus, agent IA can
deduce that the laboratory B will evolve from |+⟩b to |+⟩B, as a consequence of agent’s IB measurement. And
hence, considering irrelevant the further action of agent EA, because it does not deal with laboratory B [2], a further
measurement on laboratory B will yield +B, subjected to the outcome va. We will see in Sec. IV C that considering
irrelevant the action of agent EA is not important if the decoherence framework is not taken into account —if the
measurements consist just on correlations between the systems and the apparati. In Sec. IV B we will discuss how
the decoherence framework alter this fact.
Step 2.- Agent IB measures photon b in the basis {|h⟩b , |v⟩b}.
Fact 2: If agent IB observes that the photon is horizontally polarised, then the outcome of agent IA cannot
correspond to a horizontally polarised photon.
Using the same notation as before (applied to laboratory B), the state after agent IB completes its measurement is
|Ψ2⟩=
r
1
3 |v⟩A |h⟩B +
r
1
3 |v⟩A |v⟩B +
r
1
3 |h⟩A |v⟩B .
(37)


## Page 18


18
Therefore, there is a perfect correlation between |h⟩B and |v⟩A; the probability of observing hb and ha in the same
realization of the experiment is zero. Hence, all the previous conclusions are well supported.
Step 3.- Agent EA measures laboratory A in the basis {|+⟩A , |−⟩A}, where
|+⟩A =
r
1
2 (|h⟩A + |v⟩A) ,
(38a)
|−⟩A =
r
1
2 (|h⟩A −|v⟩A) .
(38b)
Then, the state after this measurement is
|Ψ3⟩=
r
2
3 |+⟩A
A′
+

A |v⟩B +
r
1
6 |+⟩A
A′
+

A |h⟩B −
r
1
6 |−⟩A
A′
−

A |h⟩B ,
(39)
where A′ is the measuring apparatus used by agent EA. From this state, we obtain:
Fact 3a: If the outcome obtained by agent EA is −A, then agent IB has obtained an horizontally polarised photon,
hb, in its measurement.
Fact 3b: Given facts 3a and 2, the outcome −A, obtained by agent EA determines that agent IA could not obtain
an horizontally polarised photon.
Fact 3c: Given the facts 3b and 1, the outcome −A determines that a further measurement on laboratory B, in the
basis {|+⟩B , |−⟩B} will necessary yield +B.
The main conclusion we can infer from these sequential reasonings is that, if agent EA observes −A, then EB is
bounded to observe +B. Therefore, it is not possible that outcomes −A and −B occur in the same realization of the
experiment. Furthermore, as it is discussed in detail in [2], relying on assumptions Q, S, and C, it is straightforward
to show that the four agents agree with that.
The contradiction that (presumably) establishes that quantum theory cannot consistently describe the use of itself
consists in that the probability of obtaining −A and −B in the same realization of the experiments is 1/12, even though
all the agents, relying on assumptions Q, C and S, agree that such probability must be zero. This can be easily inferred
from the ﬁnal state of the system after measurements performed by all the agents (including EB) are completed,
|Ψ⟩=
r
3
4 |+⟩A
A′
+

A |+⟩B
A′
+

B −
r
1
12 |+⟩A
A′
+

A |−⟩B
A′
−

B −
−
r
1
12 |−⟩A
A′
−

A |+⟩B
A′
+

B −
r
1
12 |−⟩A
A′
−

A |−⟩B
A′
−

B .
(40)
B.
The role of the decoherence framework
The ﬁrst element that the decoherence framework introduces is that every pre-measurement has to be ﬁxed by the
action of the corresponding environment. Notwithstanding, this fact does not change too much the equations discussed
in the previous section. The states of all the laboratories change with time, due to the continuous monitorization by
their environments, and all the measurements must be completed at their exact times, following the results in Tab.
II, but the structure of all the resulting equations is pretty much the same. For example, the state of laboratory A
must be written
|h(t)⟩A ≡|h⟩a |Ah⟩a |ε1(t)⟩a ,
(41a)
|v(t)⟩A ≡|v⟩a |Av⟩a |ε2(t)⟩a ,
(41b)
including the time-dependent environment, the ﬁnal state of the whole setup becomes
|Ψ⟩=
r
3
4 |+(τ)⟩A
A′
+(τ)

A |ε′
1(τ)⟩A |+(τ)⟩B
A′
+(τ)

B |ε′
1(τ)⟩B −
−
r
1
12 |+(τ)⟩A
A′
+(τ)

A |ε′
1(τ)⟩A |−(τ)⟩B
A′
−(τ)

B |ε′
2(τ)⟩B −
−
r
1
12 |−(τ)⟩A
A′
−(τ)

A |ε′
2(τ)⟩A |+(τ)⟩B
A′
+(τ)

B |ε′
1(τ)⟩B −
−
r
1
12 |−(τ)⟩A
A′
−(τ)

A |ε′
2(τ)⟩A |−(τ)⟩B
A′
−(τ)

B |ε′
2(τ)⟩B ,
(42)


## Page 19


19
instead of much simpler Eq. (40).
Another important point is that requisites R1-R4 from Tab. II, together with the fast-enough realization of the
external interference experiments, are mandatory to reach the previous conclusion. Hence, assumptions Q, S and C
might only lead to contradictory conclusions if the experiment is performed under very speciﬁc circumstances. Results
in Fig. 2 suggest that, the larger the laboratories A and B are, the more speciﬁc the circumstances of the experiment
must be. Thus, if agents are not small quantum machines, composed by just a few qbits, but human beings, composed
by a huge number of particles, the probability that such a contradiction might arise is virtually zero. Notwithstanding,
this conclusion only aﬀects human beings acting as agents. Quantum machines acting coherently, like the 53 qbit
quantum computer recently developed [14], are free from this limitation. Therefore, and despite the huge complexity
of such experiments, we can trust that they will be feasible in the future.
Now, let us imagine that quantum technologies are suﬃcently developed, and let us go ahead with the experiment.
That is, let us wonder if quantum theory can consistently describe the use of itself, relying on the decoherence
formalism. For this purpose, we follow the same guidelines of the setup in [2]: we assume that all agents are aware
of the whole experimental procedure, and use the decoherence framework to determine the outcomes that the other
agents have obtained or will obtain, conditioned to their own outcomes.
We start our analysis with fact 1. Considering the environmental monitorization, the state after IA has performed
its measurement is
|Ψ1⟩=
r
1
3 |h(t)⟩A |v⟩b +
r
2
3 |v(t)⟩A |+⟩b ,
(43)
with |h(t)⟩A and |v(t)⟩A given by Eqs. (41a) and (41b). Let us study the conclusions that agent IA can reach from
this state, relying on assumptions Q, C, and S, and the decoherence framework. After tracing out the environental
degrees of freedom, Eq. (43) gives rise to
ρ1 = 1
3 |h⟩a |Ah⟩a |v⟩b ⟨h|a ⟨Ah|a ⟨v|b + 2
3 |v⟩a |Av⟩a |+⟩b ⟨v|a ⟨Av|a ⟨+|b ,
(44)
that is, it establishes a correlation between the outcome va, obtained by agent IA, and the state |+⟩b. Hence, the ﬁrst
conclusion that agent IA can reach is:
(i) If agent IB measures photon b in the basis {|+⟩b , |−⟩b}, it will obtain the outcome +b, if I have obtained va.
However, as this measurement is not actually performed, this statement is useless; agent IA needs further resonings
and calculations to reach a valid conclusion. Thus, it jumps to the next step in the experimental protocol and takes
into account the consequences of agent’s IB measurement. Relying on the decoherence framework and considering
the action of the corresponding unitary operators, agent IA can calculate that the resulting state is
|Ψ2⟩=
r
1
3 |v⟩a |Av⟩a |ε2(t)⟩a |h⟩b |Ah⟩b |ε1(t)⟩b +
+
r
1
3 |v⟩a |Av⟩a |ε2(t)⟩a |v⟩b |Av⟩b |ε2(t)⟩b +
+
r
1
3 |h⟩a |Ah⟩a |ε1(t)⟩a |v⟩b |Av⟩b |ε2(t)⟩b ,
(45)
which can be written
|Ψ2⟩=
r
2
3 |v⟩a |Av⟩a |ε2(t)⟩a |+(t)⟩B +
r
1
6 |h⟩a |Ah⟩a |ε1(t)⟩a |+(t)⟩B −
r
1
6 |h⟩a |Ah⟩a |ε1(t)⟩a |−(t)⟩B .
(46)
And, after tracing out the corresponding environmental degrees of freedom, agent’s IA perception can be written as
ρ2 = 2
3 |v⟩a |Av⟩a |+(t)⟩B ⟨v|a ⟨Av|a ⟨+(t)|B +
+ 1
6 |h⟩a |Ah⟩a |+(t)⟩B ⟨h|a ⟨Ah|a ⟨+(t)|B + 1
6 |h⟩a |Ah⟩a |−(t)⟩B ⟨h|a ⟨Ah|a ⟨−(t)|B −
−1
6 |h⟩a |Ah⟩a |+(t)⟩B ⟨h|a ⟨Ah|a ⟨−(t)|B −1
6 |h⟩a |Ah⟩a |−(t)⟩B ⟨h|a ⟨Ah|a ⟨+(t)|B .
(47)
Therefore, agent IA can make the following statement, which seems similar to fact 1:
(ii) If agent IB measures photon b in the basis {|h⟩b , |v⟩b}, and subsequently, without any other measurement in
between, agent EB measures laboratory B in the basis {|+(τ)⟩B , |−(τ)B⟩}, the last one will obtain |+⟩B, if I have
obtained |v⟩a.


## Page 20


20
However, this statement does not represent the thought experiment discussed in [2]. The experimental protocol
establishes that agent IB measures photon b in the basis {|h⟩b , |v⟩b}, then agent EA measures the whole laboratory
A in the basis {|+(τ)⟩A , |−(τ)B⟩}, and ﬁnally agent EB measures laboratory B in the basis {|+(τ)⟩B , |−(τ)B⟩}.
This is the point at which the diﬀerences between the decoherence framework and the standard interpretations —
measurements as correlations between systems and apparati— emerge. As we have discussed in Sec. III, an external
interference measurement, like the one performed by agent EA, generally implies changes in the memory record of
the measured agent. Notwithstanding, as these changes can be exactly calculated, agent IA can still rely on the
decoherence framework to predict the correlations between its outcome, va, and the one that agent EB will obtain
when measuring laboratory B in the basis {|+(τ)⟩B , |−(τ)⟩B}. Just before the ﬁnal measurement by agent EB, the
state of the whole system can be written
|Ψ3(τ)⟩=
r
3
8 |h⟩a |Ah⟩a |ε1(τ)⟩a
A′
+

A |ε′
1(τ)⟩A |+⟩B +
r
3
8 |v⟩a |Av⟩a |ε2(τ)⟩a
A′
+

A |ε′
1(τ)⟩A |+⟩B −
−
r
1
24 |h⟩a |Ah⟩a |ε1(τ)⟩a
A′
+

A |ε′
1(τ)⟩A |−⟩B −
r
1
24 |v⟩a |Av⟩a |ε2(τ)⟩a
A′
+

A |ε′
1(τ)⟩A |−⟩B −
−
r
1
24 |h⟩a |Ah⟩a |ε1(τ)⟩a
A′
−

A |ε′
2(τ)⟩A |+⟩B +
r
1
24 |v⟩a |Av⟩a |ε2(τ)⟩a
A′
−

A |ε′
2(τ)⟩A |+⟩B −
−
r
1
24 |h⟩a |Ah⟩a |ε1(τ)⟩a
A′
−

A |ε′
2(τ)⟩A |−⟩B +
r
1
24 |v⟩a |Av⟩a |ε2(τ)⟩a
A′
−

A |ε′
2(τ)⟩A |−⟩B .
(48)
Hence, tracing out agent’s IA environment, and both agent’s EA apparatus and environment, since agent’s EA outcome
is irrelevant, the state of agent’s IA memory reads
ρ3 = 5
12 |h⟩a |Ah⟩a |+⟩B ⟨h|a ⟨Ah|a ⟨+|B + 5
12 |v⟩a |Av⟩a |+⟩B ⟨v|a ⟨Av|a ⟨+|B +
+ 1
12 |h⟩a |Ah⟩a |−⟩B ⟨h|a ⟨Ah|a ⟨−|B + 1
12 |v⟩a |Av⟩a |−⟩B ⟨v|a ⟨Av|a ⟨−|B .
(49)
And therefore, relying on assumption Q, agent IA can make the following claims: (i) the system is in state given by
Eq. (48) just before agent’s EB measurement; (ii) a certain outcome in the basis {|+(τ)⟩B , |(−)⟩B} is going to be
obtained; (iii) neither ⟨Ψ3(τ)| π+,B |Ψ3(τ)⟩= 1, nor ⟨Ψ3(τ)| π−,B |Ψ3(τ)⟩= 1, conditioned to my memory record is
va. Hence, the decoherence framework modiﬁes fact 1, giving rise to
New fact 1: If agent IA obtains that the photon is vertically polarised (outcome va), then, a further measurement
of the laboratory B in the basis {|+(τ)⟩B , |−(τ)⟩B} will lead to either +B (with p = 5/6) or −B (with p = 1/6).
It is worth noting that this prediction can be experimentally conﬁrmed by simultaneously reading the memory
records of agents IA and EB, as soon as the last outcome is ﬁxed by the corresponding environmental monitorization.
Even though it is reasonable to wonder if this inconclusive statement is a consequence of the changes induced in agent’s
IA memory by the external interference measurement performed by agent EA, the key point is that no correlations
between IA and EB perceptions exist before the action of agent EA, so there is no other way to determine whether
agent’s EB outcome is bounded by agent’s IA or not. In Sec. IV C we will see that the results are diﬀerent is the
decoherence framework is not taken into account.
As the inconsistency discussed in [2] is based on fact 1, the result we have obtained is enough to show that the
decoherence framework is free from it. Notwithstanding, to delve in the interpretation of this remarkable thought
experiment, follows a discussion about facts 2 and 3.
Again, we focus on the predictions that the involved agents can make by means of the decoherence framework, and
their experimental veriﬁcation by reading their corresponding memory records. Fact 2 is made from agent’s IB point
of view, so we focus on the state of the system after both agents IA and IB have completed their measurements, which
reads
|Ψ2⟩=
r
1
3 |v⟩a |Av⟩a |ε2(t)⟩a |h⟩b |Ah⟩b |ε1(t)⟩b +
+
r
1
3 |v⟩a |Av⟩a |ε2(t)⟩a |v⟩b |Av⟩b |ε2(t)⟩b +
+
r
1
3 |h⟩a |Ah⟩a |ε1(t)⟩a |v⟩b |Av⟩b |ε2(t)⟩b .
(50)
To obtain their common view of the system, both their environment must be traced out. Hence, the memory records


## Page 21


21
of both agents are compatible with the mixed state given by [24]
ρ2 = 1
3 |v⟩a |Av⟩a |h⟩b |Ah⟩b ⟨v|a ⟨Av|a ⟨h|b ⟨Ah|b +
+ 1
3 |v⟩a |Av⟩a |v⟩b |Av⟩b ⟨v|a ⟨Av|a ⟨v|b ⟨Av|b +
+ 1
3 |h⟩a |Ah⟩a |v⟩b |Av⟩b ⟨h|a ⟨Ah|a ⟨v|b ⟨Av|b .
(51)
That is, if agent IB relies on the decoherence framework to calculate agent’s IA outputs conditioned to the one it has
obtained, it can safely conclude fact 2 at this stage of the experiment.
Let us now proceed with fact 3. As it is formulated from agent’s EA point of view, we start from the state of the
system after agent’s EA measurement, which reads
|Ψ3(τ)⟩=
r
2
3 |+(τ)⟩A
A′
+

A |ε′
1(τ)⟩A |v⟩b |Av⟩b |ε2(τ)⟩b +
+
r
1
6 |+(τ)⟩A
A′
+

A |ε′
1(τ)⟩A |h⟩b |Ah⟩b |ε1(τ)⟩b −
−
r
1
6 |−(τ)⟩A
A′
−

A |ε′
2(τ)⟩A |h⟩b |Ah⟩b |ε1(τ)⟩b .
(52)
Eq. (52) represents the state of the whole system after the measurements performed by agents IA, IB and EA are
completed. The way that these agents perceive this state depends again on the action of their respective environments,
and therefore can be described by tracing out the corresponding degrees of freedom. A joint vision of agents IB and
EA is obtained tracing out the environments εb and ε′
A, leading to
ρ3(τ) = 2
3 |+(τ)⟩A
A′
+

A |v⟩b |Av⟩b ⟨+(τ)|A

A′
+

A ⟨v|b ⟨Av|b +
+ 1
6 |+(τ)⟩A
A′
+

A |h⟩b |Ah⟩b ⟨+(τ)|A

A′
+

A ⟨h|b ⟨Ah|b +
+ 1
6 |−(τ)⟩A
A′
−

A |h⟩b |Ah⟩b ⟨−(τ)|A

A′
−

A ⟨h|b ⟨Ah|b .
(53)
This state is fully compatible with fact 3a. At this stage of the experiment, the correlation between the memory records
of IB and EA is incompatible with the outcomes −A and vb being obtained at the same run of the experiment. This
means that agent EA can use assumption Q to conclude: (i) system is in state given by Eq. (52) after my measurement;
(ii) a certain outcome was obtained by agent IB in the basis {|h⟩b , |v⟩b}; (iii) as ⟨Ψ3(τ)| πh,b |Ψ3(τ)⟩= 1, conditioned
I have obtained −A, then fact 3a is correct. Furthermore, agent IB, relying only on its outcome, the details of the
whole protocol and the decoherence framework, can also predict fact 3a.
To follow with the argument, agent EA performs a nested reasoning to determine the outcome obtained by agent
IA. A very relevant point is the time at which agent’s IA memory record is evaluated. If we re-write the current state
of the system, Eq. (52), in a basis including {|h⟩a |h⟩b , |h⟩a |v⟩b , |v⟩a |h⟩b , |v⟩a |v⟩b}, we obtain
|Ψ3(τ)⟩=
r
1
3 |h⟩a |Ah⟩a |ε1(τ)⟩a
A′
+

A |ε′
1(τ)⟩A |v⟩b |Av⟩b |ε2(τ)⟩b +
+
r
1
3 |v⟩a |Av⟩a |ε2(τ)⟩a
A′
+

A |ε′
1(τ)⟩A |v⟩b |Av⟩b |ε2(τ)⟩b +
+
r
1
12 |h⟩a |Ah⟩a |ε1(τ)⟩a
A′
+

A |ε′
1(τ)⟩A |h⟩b |Ah⟩b |ε1(τ)⟩b +
+
r
1
12 |v⟩a |Av⟩a |ε2(τ)⟩a
A′
+

A |ε′
1(τ)⟩A |h⟩b |Ah⟩b |ε1(τ)⟩b −
−
r
1
12 |h⟩a |Ah⟩a |ε1(τ)⟩a
A′
−

A |ε′
2(τ)⟩A |h⟩b |Ah⟩b |ε1(τ)⟩b +
+
r
1
12 |v⟩a |Av⟩a |ε2(τ)⟩a
A′
−

A |ε′
2(τ)⟩A |h⟩b |Ah⟩b |ε1(τ)⟩b .
(54)


## Page 22


22
Thus, to determine the joint vision of agents IA and IB at this stage of the experiment we have just to trace out εa,
εb, A′
A and ε′
A from the density matrix arising from this wavefunction. This leads to
ρ3 = 1
3 |h⟩b |Ah⟩b |v⟩a |Av⟩a ⟨h|b ⟨Ah|b ⟨v|a ⟨Av|a +
+ 1
3 |v⟩b |Av⟩b |v⟩a |Av⟩a ⟨v|b ⟨Av|b ⟨v|a ⟨Av|a +
+ 1
6 |h⟩b |Ah⟩b |h⟩a |Ah⟩a ⟨h|b ⟨Ah|b ⟨h|a ⟨Ah|a +
+ 1
6 |v⟩b |Av⟩b |h⟩a |Ah⟩a ⟨v|b ⟨Av|b ⟨h|a ⟨Ah|a .
(55)
This is one the most remarkable consequences of the decoherence framework. In Sec. III we have shown that
external interference measurements generally change the memory records of measured agents. Eq. (55) shows that
such interference measurements also change the correlations between the memories of two distant agents.
If the
correlations between agents’s IA and IB outcomes are evaluated before the interference experiment performed by
agent EA, fact 2 is correct; if they are evaluated afterwards, it changes to: if agent IB has observed hb, then agent’s
IA memory record is compatible with both ha and va. It is worth noting that the decoherence framework can be used
by all the agents to calculate both situations.
The agents involved in the thought experiment devised in [2] use the time evolution corresponding to each measure-
ment to track the system back, that is, in the language of the decoherence framework, to calculate what agents IB and
IA thought in the past. Hence, agent EA can rely on the decoherence framework to conclude: (i) given Eq. (52), agent
IB obtained the outcome hb before my own measurement, since no changes in laboratory B have ocurred in between;
(ii) hence, independently of what agent IA thinks now, it obtained the outcome va before my own measurement and
conditioned to agent’s IB outcome hb; (iii) therefore, agent’s IA memory record was va in the past, if I have obtained
−A, even though it can be either va and ha now.
The previous paragraph illustrates one of the most signiﬁcatives features of the decoherence framework: it can
be used to calculate both the past and the current state of all agents’s memory records; no ambiguities arise as a
consequence of external interference experiments.
Regarding the thought experiment devised in [2], a proper use of the decoherence framework, taking into account
the exact times at which the agents make their claims, shows that both facts 3a and 3b are correct. But this framework
also shows that fact 3c is not correct, beacuse it relies on fact 1, which is incompatible with it. Hence, the reasonings
discussed in this section invalidate the proof of the no-go theorem presented in [2]. If assumptions Q, S and C are
used within the decoherence framework, agents IA, IB, EA and EB do not reach the contradictory conclusion that
−A implies +B. The key point in this argument is that one agent must predict a correlation which is only ﬁxed after
an external interference experiment on itself, if it wants to make a claim about the ﬁnal outcome of the protocol. The
standard interpretation of quantum measurements is ambiguous about this point. One can suspect that something
weird might happen, but a calculation to conﬁrm or to refute this thought cannot be done. On the contrary, the
decoherence framework provides exact results that can be tested by means of a proper experiment
Finally, it is worth to remark that we have not proved that the decoherence framework is free from inconsistencies.
We have just shown that the proof of the theorem proposed in [2] is not valid if the decoherence framework is taken
into account. But the main statement of the theorem can be still considered as a conjecture.
C.
Discussion
The conclusions of the previous section are enterely based on the decoherence framework. Resuls of [2] are well
substantiated if this framework is not taken into account, that is, if a correlation between a system and a measuring
apparatus is considered enough to complete a measurement. In such a case, the ﬁnal state of the protocol can be


## Page 23


23
written in four diﬀerent shapes
|Ψα⟩=
r
1
3 |v⟩A |h⟩B +
r
1
3 |h⟩A |v⟩B +
r
1
3 |v⟩A |v⟩B ,
(56a)
|Ψβ⟩=
r
2
3 |+⟩A |h⟩B −
r
1
6 |−⟩A |h⟩B +
r
1
6 |+⟩A |h⟩B ,
(56b)
|Ψγ⟩=
r
2
3 |v⟩A |+⟩B −
r
1
6 |h⟩A |−⟩B +
r
1
6 |h⟩A |−⟩B ,
(56c)
|Ψδ⟩=
r
3
4 |+⟩A |+⟩B −
r
1
12 |+⟩A |−⟩B +
r
1
12 |−⟩A |−⟩B −
r
1
12 |−⟩A |+⟩B ,
(56d)
relying on four diﬀerent basis. If the preferred basis for each measurement is not ﬁxed by a unique mechanism, like
the one coming from the decoherence framework, the conclusions of the involved agents become ambiguous. The
following reasoning can be understood as a consequence of the basis ambiguity problem [5]:
Eq. (56c) can be used to establish a perfect correlation between the outcomes va and +B: if laboratory A is in state
|v⟩A, which can be understood as the state resulting from the outcome va obtained by agent IA, then the outcome
+B is guaranteed. Hence, fact 1 is well supported —the ﬁnal state of the whole experiment can be written in a way
compatible with it. In a similar way. Eq. (56b) establishes a perfect correlation between |−⟩A and |h⟩B, which can
be interpreted as follows: if agent EA as obtained −A, then agent EB has obtained hB. Again, the ﬁnal state of the
whole protocol is compatible with this fact. Finally. Eq. (56a) establishes a perfect correlation between |hB⟩and
|vA⟩, meaning that if agent IB has obtained hB, then agent IA has obtained vA. And this is again compatible with
the ﬁnal state of the experiment.
Hence, as a consequence of the basis ambiguity problem, agents IA, IB, EA and EB can rely on Eqs. (56a), (56b)
and (56c) to infer a conclusion incompatible with Eq. (56d). As we have discussed in Sec. IV B, the decoherence
framework ﬁxes this bug by ruling out the basis ambiguity, and by providing just one preferred basis for each outcome.
V.
OBSERVER-INDEPENDENT FACTS
This section deals with the no-go theorem discussed in [3]. This theorem has been experimentally conﬁrmed in [4].
A criticism is published in [22].
A.
Original version of the experiment and no-go theorem
The structure of this experiment has been already discussed in Sec. IV A. The only diﬀerence is the initial state,
which consists in a pair of polarised photons, spanned by {|h⟩, |v⟩}, and reads
|Ψ⟩β =
r
1
2 cos π
8 (|h⟩a |v⟩b + |v⟩a |h⟩b) +
+
r
1
2 sin π
8 (|h⟩a |h⟩b −|v⟩a |v⟩b) .
(57)
This state is used to illustrate a no-go theorem that establishes that the following four statements are incompatible,
that is, are bounded to yield a contradiction:
Statement 1.- Quantum theory is valid at any scale.
Statement 2.- The choice of the measurement settings of one observer has no inﬂuence on the outcomes of other
distant observer(s).
Statement 3.- The choice of measurement settings is statistically independent from the rest of the experiment.
Statement 4.- One can jointly assign truth values to the propositions about outcomes of diﬀerent observers.
In [3, 4], the thought experiment used to proof this theorem consists of the following steps:
(i) The internal agents, IA and IB, perform their (pre)measurements, that is, establish a correlation between the
measured photons and their apparati given by Eq. (4).
(ii) The external agents, EA and EB, choose between performing interference experiments, or measuring the
polarisation of the internal photons.
(iii) A Bell-like test is performed on the four diﬀerent combinations resulting from point (ii), to conclude that it is
not possible to jointly assign truth values to the outcomes obtained by the internal and the external agents.


## Page 24


24
This protocol was experimentally performed in [4], validating the violation of the Bell-like test prediction in [3].
The state resulting from step (i) is
|Ψ0⟩=
r
1
2 cos π
8 (|h⟩a |Ah⟩a |v⟩b |Av⟩b + |v⟩a |Av⟩a |h⟩b |Ah⟩b) +
+
r
1
2 sin π
8 (|h⟩a |Ah⟩a |h⟩b |Ah⟩b −|v⟩a |Av⟩a |v⟩b |Av⟩b) .
(58)
To proceed with step (ii), agent EA chooses between observables A0 and B0,
A0 = |h⟩a |Ah⟩a ⟨h|a ⟨Ah|a −|v⟩a |Av⟩a ⟨v|a ⟨Av|a ,
(59)
B0 = |+⟩A |+⟩A −|−⟩A ⟨−|A ,
(60)
where |±⟩A = (|h⟩a |Ah⟩a ± |v⟩a |Av⟩a) /
√
2. The ﬁrst one, A0, can be interpreted as a simple reading of agent’s IA
memory, whereas the second one, B0, performs an external interference experiment, and therefore can be linked to
agent’s EA memory. Following the same spirit, agent EB chooses between A1 and B1,
A1 = |h⟩b |Ah⟩b ⟨h|b ⟨Ah|b −|v⟩b |Av⟩b ⟨v|b ⟨Av|b ,
(61)
B1 = |+⟩B |+⟩B −|−⟩B ⟨−|B ,
(62)
where |±⟩B = (|h⟩b |Ah⟩b ± |v⟩b |Av⟩b) /
√
2.
Finally, the third step is performed taking into account that statements 1−4 imply the existence of a joint probability
distribution p(A0, B0, A1, B1) whose marginals satisfy the Claude-Horne-Shimony-Holt (CHSH) inequality [25, 26]
S = ⟨A1B1⟩+ ⟨A1B0⟩+ ⟨A0B1⟩−⟨A0B0⟩≤2.
(63)
In [3] is theoretically shown that the initial state given by Eq. (57) leads to S = 2
√
2; in [4] this result is conﬁrmed
by an experiment. The conclusion is that these resuls are incompatible with statements 1−4, and therefore, assuming
that statements 2 (non-locality) and 3 (freedom of choice) are compatible with quantum mechanics [3, 4, 26], quantum
theory is incompatible with the existence of observer-independent well established facts.
B.
The role of the decoherence framework
Unfortunately, this simple protocol is not consistent with the decoherence framework. The previous analysis ac-
counts neither for the structure of laboratories summarized in Tab. I, nor for the measuring protocol given in Tab.
II. The decoherence framework postulates that a deﬁnite outcome does not emerge until an external environment
monitorizes the state composed by the system, the apparatus and the observer. Therefore, Eq. (58) does not repre-
sent the outcomes obtained by agents IA and IB, but just an entangled system composed by two photons and two
aparati. And consequently, the fact that it violates a CHSH inequality does not entail the refutation of the fourth
statement of the theorem, since deﬁnite outcomes have not still appeared —it just shows that the state (58) includes
quantum correlations that cannot be described by means of a joint probability distribution, but such correlations
involve neither deﬁnite outcomes, nor observers’ memory records.
As a ﬁrst conclusion, the previous paragraph is enough to show that the thought experiment devised in [3] cannot
refute the possibility of jointly assigning truth values to the propositions about the outcomes of diﬀerent observers,
if the decoherence framework is considered. Following the same line of reasoning that in Sec. IV C we can also state
that the conclusion in [3] is well supported if a measurement is understood as a correlation between a system and
its measuring apparatus. In such a case, the correlations between A and B observables represent the correlations
between the outcomes obtained by the internal and the external observables, and therefore the CHSH proves that
they are incompatible with a deﬁnite joint probability distribution.
The rest of the section is devoted to a variation of the setup devised in [3]. The idea is to follow the same spirit, but
making it suitable to challenge the decoherence framework. This modiﬁed experimental setup consists of two main
steps:
(i) The internal agents measure their systems in the basis {|h⟩, |v⟩}, and the external ones perform interference
experiment in the basis {|+⟩, |−⟩}.
(ii) Two super-external agents choose between the operators A and B, given by Eqs. (65a)-(65d), to establish
complementary facts about the outcomes obtained in step (i).
This variation allows to apply a CHSH inequality to the outcomes obtained by the internal and the external agents,
and therefore to test if we can jointly assing truth values to them. To properly apply the decoherence framework to


## Page 25


25
this experiment, it is mandatory to include in the protocol all the environments which determine the emergence of
deﬁnite outcomes. This can be done in three diﬀerent stages:
Stage 1.- Agent IA measures the state of photon a in a basis given by {|h⟩a , |v⟩a}, and IB measures the state of pho-
ton b in a basis given by {|h⟩b , |v⟩b}. Without explicitly taking into account the external apparati and environments,
which are not entangled with laboratories A and B at this stage, the resulting state is
|Ψ1⟩=
r
1
2 cos π
8 |h⟩a |Ah⟩a |ε1(t)⟩a |v⟩b |Av⟩b |ε2(t)⟩b +
+
r
1
2 cos π
8 |v⟩a |Av⟩a |ε2(t)⟩a |h⟩b |Ah⟩b |ε1(t)⟩b +
+
r
1
2 sin π
8 |h⟩a |Ah⟩a |ε1(t)⟩a |h⟩b |Ah⟩b |ε1(t)⟩b −
−
r
1
2 sin π
8 |v⟩a |Av⟩a |ε2(t)⟩a |v⟩b |Av⟩b |ε2(t)⟩b .
(64)
The decoherence framework establishes that agents IA and IB do not observe deﬁnite outcomes until this stage is
reached. It is worth remembering that each of its environment is continuously monitorizing each of its apparati, by
means of Hamiltonians like (12).
At this stage, an experiment equivalent to the one discussed in [3, 4] could be done, by means of the following A0,
A1, B0, and B1 observables
A0 = |h⟩a |Ah⟩a ⟨h|a ⟨Ah|a −|v⟩a |Av⟩a ⟨v|a ⟨Av|a ,
(65a)
B0 = |h⟩b |Ah⟩b ⟨h|b ⟨Ah|b −|v⟩b |Av⟩b ⟨v|b ⟨Av|b ,
(65b)
A1(τ) = |+(τ)⟩A ⟨+(τ)|A −|−(τ)⟩A ⟨−(τ)|A ,
(65c)
B1(τ) = |+(τ)⟩B ⟨+(τ)|B −|−(τ)⟩B ⟨−(τ)|B ,
(65d)
where |+(τ)⟩A is given by Eq. (38a); |−(τ)⟩A is given by Eq. (38b), and equivalent relations determine |+(τ)⟩B and
|−(τ)⟩B. Again, τ is the time at which the interference measurements are performed, according to points R1-R4 of
Tab. II. In such a case, A0 and B0 can be properly interpreted as agents’ IA and IB points of view, but A1 and B1
are still not linked to agents’ EA and EB perceptions —their environments must act to determine the corresponding
deﬁnite outcomes. Hence, the CHSH inequality applied to this state would allow us to get a conclusion about the
compatibility of the internal agents’ memories and the states of the laboratories in which they live, but they would
tell us nothing about the outcomes obtained by the external agents.
Stage 2a.- From Eq. (64), agent EA measures the state of laboratory A in the basis {|+(τ)⟩A , |−(τ)A⟩}, considering
requisites R1-R4 of Tab. II. The resulting state is
|Ψ2⟩= 1
2

cos π
8 −sin π
8

|+(τ)⟩A
A′
+

A |ε′
1(τ)⟩A |v⟩b |Av⟩b |ε2(τ)⟩b +
+ 1
2

cos π
8 + sin π
8

|−(τ)⟩A
A′
−

A |ε′
2(τ)⟩A |v⟩b |Av⟩b |ε2(τ)⟩b +
+ 1
2

cos π
8 + sin π
8

|+(τ)⟩A
A′
+

A |ε′
1(τ)⟩A |h⟩b |Ah⟩b |ε1(τ)⟩b +
+ 1
2

sin π
8 −cos π
8

|−(τ)⟩A
A′
−

A |ε′
2(τ)⟩A |h⟩b |Ah⟩b |εh(τ)⟩b .
(66)
At this stage, observable A1 represents agent’s EA point of view, but B1 is still not linked to agent’s EB memory.
Stage 2b.- From Eq. (64) again, agent EB measures the state of laboratory B in the basis {|+(τ)⟩B , |−(τ)B⟩},
considering requisites R1-R4 of Tab. II. The resulting state is
|Ψ3⟩= 1
2

cos π
8 −sin π
8

|v⟩a |Av⟩a |ε2(τ)⟩a |+(τ)⟩B
A′
+

B |ε′
1(τ)⟩B +
+ 1
2

cos π
8 + sin π
8

|v⟩a |Av⟩a |ε2(τ)⟩a |−(τ)⟩B
A′
−

B |ε′
2(τ)⟩B +
+ 1
2

cos π
8 + sin π
8

|h⟩a |Ah⟩a |ε1(τ)⟩a |+(τ)⟩B
A′
+

B |ε′
1(τ)⟩B +
+ 1
2

sin π
8 −cos π
8

|h⟩a |Ah⟩a |ε1(τ)⟩a |−(τ)⟩B
A′
−

B |ε′
2(τ)⟩B .
(67)


## Page 26


26
As this stage has been obtained from Eq. (64), it is not subsequent to Eq. (66). Therefore, observable B1 represents
agent’s EB point of view, but A1 is still not linked to agent’s EA memory.
Stage 3.- Agent EA measures the state of laboratory A in the basis {|+(τ)⟩A , |−(τ)A⟩}, considering requisites
R1-R4 of Tab. II, and agent EB measures the state of laboratory B in the basis {|+(τ)⟩B , |−(τ)B⟩}, following the
same procedure. This case is subsequent to either stage 2a or stage 2b. The resulting state is
|Ψ4⟩=
r
1
2 cos π
8 |+(τ)⟩A
A′
+

A |ε′
1(τ)⟩A |+(τ)⟩B
A′
+

B |ε′
1(τ)⟩B −
−
r
1
2 cos π
8 |−(τ)⟩A
A′
−

A |ε′
2(τ)⟩A |−(τ)⟩B
A′
−

B |ε′
2(τ)⟩B +
+
r
1
2 sin π
8 |+(τ)⟩A
A′
+

A |ε′
1(τ)⟩A |−(τ)⟩B
A′
−

B |ε′
2(τ)⟩B +
+
r
1
2 sin π
8 |−(τ)⟩A
A′
−

A |ε′
2(τ)⟩A |+(τ)⟩B
A′
+

B |ε′
1(τ)⟩B .
(68)
At this stage, the four agents have observed deﬁnite outcomes, and therefore their four memories can be read to
interpret these outcomes. Hence, if one wants to test statements 1-4 of the theorem formulated in [3], one must
start from this state. So, let us image that we are running a quantum algorithm performing this experiment and we
want to test if we can jointly assign truth values to the outcomes obtained by the four agents. One of us can choose
between A0 and B0, deﬁned in Eqs. (65a) and (65b), to decide between reading agent’s IA or agent’s EA memories,
and another one can choose between A1 and B1, deﬁned in Eqs. (65c) and (65d), to decide between reading agent’s
IB or agent EB memories. Then, we can run a large number of realizations of the same experiment to test if the
CHSH inequality given in Eq. (63) holds. If it gives rise to S > 2 we can conclude that statement (4) of the theorem
is violated; if not, we can conclude that it is possible to jointly assign truth values to the observations done by the
four agents.
A straightforward calculations provides the following result,
⟨Ψ4| A0B0 |Ψ4⟩
= 0,
(69)
⟨Ψ4| A1B0 |Ψ4⟩
= 0,
(70)
⟨Ψ4| A0B1 |Ψ4⟩
= 0,
(71)
⟨Ψ4| A1B1 |Ψ4⟩= 1/
√
2.
(72)
Therefore, the CHSH inequality, Eq. (63), applied to |Ψ4⟩leads to S = 1/
√
2 < 2.
Two main conclusions can be gathered from this section. First, the experiment devised in [3], and its experimental
realization [4], are incompatible with the decoherence framework, because, according to it, they do not deal with
proper outcomes; thus, they cannot be used to refute the possibility of jointly assigning truth values to the outcomes
obtained by diﬀerent observers. Second, a variation to the experiment in [3] designed to challenge the decoherence
framework following the same spirit is compatible with the four statements discussed above —quantum theory is
valid at any scale; the choice of the measurement settings of one observer has no inﬂuence on the outcomes of other
distant observers; the choice of the measurement settings is independent form the rest of the experiment, and one
can jointly assign truth values to the propositions about the outcomes of diﬀerent observers. In other words, these
statements do not imply a contradiction in this experiment, if the role of all the parts of each laboratory, given in
Tab. I, and the physical mechanisms giving rise to each outcome, are considered. This conclusion is fully compatible
with the main idea behind the decoherence framework. As it is clearly stated in the title of Ref. [5], the main aim of
this formalism is to explain how classical results, like deﬁnite outcomes, can be obtained from quantum mechanics,
without relying on a non-unitary wave-function collapse. This section shows that the memory records of all the agents
are indeed classical as a consequence of the continuous monitorization by their environments, and therefore satisfy
the corresponding CHSH inequality. Notwithstanding, the state after all these deﬁnite outcomes have emerged, Eq.
(68), is quantum and has true quantum correlations. If one applies the CHSH inequality to the states of the two
internal and the two external laboratories, the resulting equations are formally the same that those in [3] —conﬁrming
that the thought experiment discussed in this section follows the same spirit that the one in [3]—, and therefore one
recovers the original result, S = 2
√
2. This means that we cannot assign joint truth values to the state of these
laboratories, but we can make this assignement to the state of the agents memories. In [3, 4] there is no distinction
between the state of the laboratory in which an agent lives, and the state of its memory; the decoherence framework
is based precisely on this distinction.
Before ending this section, it is worth remarking that our result does not prove that the use of statements 1 −4
is free from contradictions in any circumstances. We have just shown that the particular setup used to prove the


## Page 27


27
no-go theorem in [3] does not lead to contradictions if the decoherence framework is properly taken into account. But,
again, the main statement of the theorem can be still considered as a conjecture.
VI.
CONCLUSIONS
The main conclusion of this work is that neither the original Wigner’s friend experiment, nor the extended version
proposed in [2], nor the one in [3] (and its corresponding experimental realization, [4]) entail contradictions if the
decoherence framework is properly taken into account.
This framework consists in considering that a quantum measurement and the corresponding (apparent) wave-
function collapse are the consequence of the interaction between the measuring apparatus and an uncontrolled envi-
ronment, which must be considered as an inseparable part of the measuring device. In this work, we have relied on
a simple model to show that a chaotic interaction is necessary to induce such an apparent collapse, but, at the same
time, a quite small number of environmental qbits suﬃces for that purpose. This implies that any experiment on
any quantum system can be modeled by means of a unitary evolution, and therefore all the time evolution, including
the outcomes obtained by any observers, is univocally determined by the initial state, the interaction between the
system and the measuring apparati, and the interaction between such apparati and the corresponding environments.
Seeing the reality as if a random wave-function collapse had happend is due to the lack of information suﬀered by the
observers —only the system as a whole evolves unitarilly, not a part of it. This is a somehow paradoxical solution to
the quantum measurement problem: ignoring an important piece of information about the state in which the observer
lives is mandatory to observe a deﬁnite outcome; taking it into account would lead to no observations at all. But,
besides the ontological problems arising for such an explanation, the resulting framework is enough for the purpose
of this work.
The ﬁrst consequence of this framework is that the memory records of Wigner’s friends —the internal agents
in a Wigner’s friend experiment— change as a consequence of the external interference experiment performed by
Wigner, these changes are univocally determined by the Hamiltonian encoding all the time evolution, and therefore
can be exactly predicted. Hence, if an agent has observed a deﬁnite outcome, then external interference experiments
performed on the laboratory in which it lives change its memory records; if such changes do not occur is because the
agent has not observed a deﬁnite outcome.
The second consequence of the decoherence framework is that the contradictions discussed in [2] and [3] are ruled
out. If the agents involved in the thought experiment devised in [2] use the decoherence framework as the common
theory to predict the other agents’ outcomes, their conclusions are not contradictory at all.
The analysis of the
experiment proposed in [3] is a bit more complicated. Its original design is not compatible with the decoherence
framework. Hence, it cannot be used to refute the possibility to jointly assigning truth values to the agents’ outcomes,
that is, it cannot be used to prove the no-go theorem formulated in [3]. Therefore, a variation of that experiment,
following the same spirit, is proposed to show that, if the CHSH inequality is applied to the state at which the whole
system is at the end of the protocol, that is, when the records in the memories of the four agents are ﬁxed, the
resulting value is compatible with the existence of observer-independent facts.
However, this is not enough to dismiss the main statements of the no-go theorems formulated in such references.
The conclusion of this work is that the examples used to prove these theorems are not valid within the decoherence
framework, but we have not proved that this framework is totally free from similar inconsistencies. Hence, these
statements can be still considered as conjectures. Further work is required to go beyond this point.
It is also worth to remark that the decoherence formalism also narrows down the conditions under which the external
interference measurements, trademark of Wigner’s friend experiments, are expected to work. This means that, if the
decoherence framework results to be true, human beings acting as observers are almost free from suﬀering the strange
eﬀects of such experiments. Notwithstanding, the promising state-of-the-art in quantum technologies may provide us,
in the future, quantum machines able to perform these experiments.
Finally, the conclusion of this work must not be understood as a strong support of the decoherence framework.
It just establishes that such a framework does not suﬀer from the inconsistencies typically ensuing Wigner’s friend
experiments. However, there is plenty of space for theories in which the wavefunction collapse is real [7]. These
theories predict a totally diﬀerent scenario, since after each measurement the wave function of the whole system
collapses, and therefore becomes diﬀerent from the predictions of the decoherence framework. Hence, experiments
like the ones discussed in this work might be a way to test which of this proposals is correct —if any.


## Page 28


28
ACKNOWLEDGMENTS
This work has been supported by the Spanish Grants Nos. FIS2015-63770-P (MINECO/ FEDER) and PGC2018-
094180-B-I00 (MCIU/AEI/FEDER, EU). The author acknowledges A. L. Corps for his critical reading of the
manuscript.
[1] E. P. Wigner, Remarks on the mind-body question. In The Scientiest Speculates, Ed. I. J. Good; Heinemann: London, UK
(1961).
[2] D. Frauchiger and R. Renner, Quantum theory cannot consistently describe the use of itself, Nat. Comm. 9, 3711 (2018).
[3] C. Brukner, A No-Go Theorem for Observer-Independent Facts, Entropy 20, 350 (2018).
[4] M. Proietti, A. Pickston, F. Graﬃtti, P. Barrow, D. Kundys, C. Branciard, M. Ringbauer, and A. Ferizzi, Experimental
rejection of observer-independence in the quantum world, arXiv:1902.05080 (2019).
[5] W. H. Zurek, Decoherence, einselection, and the quantum origins of the classical, Rev. Mod. Phys. 75, 715 (2003).
[6] W. H. Zurek, Pointer basis of quantum apparatus: Into what mixture does the wave packet collapse?, Phys. Rev. D 24,
1516 (1981).
[7] A. Bassi, K. Lochan, S. Satin, T. P. Singh, and H. Ulbricht, Models of wave-function collapse, underlying theories, and
experimental tests, Rev. Mod. Phys. 85, 471 (2013).
[8] V. Baumann and S. Wolf, On formalisms and interpretations, Quantum 2, 99 (2018).
[9] W. H. Zurek, Relative states and the environment: einselection, envariance, quantum darwinism, and the existential
interpretation, arXiv:0707.2832 (2007).
[10] One of the trademarks of the decoherence interpretation of quantum mechanics is that the pointer states of any apparati,
that is, the states which appear as objective outcomes, are those which survive to the continuous monitorization by a
complex environment. In other words, the environment, and its interaction with the measuring apparatus, is the origin of
the classical perception of the reality. For a more detailed discussion, we refer the reader to [5, 9].
[11] A. Elby and J. Bub, Triorthogonal uniqueness theorem and its relevance to the interpretation of quantum mechanics, Phys.
Rev. A 49, 4213 (1994).
[12] Of course, the agent cannot restore the complete state from a single measurement. If its outcome is, say, h, it can just
conclude that the global state must be |Ψ2⟩= α |h⟩|Ah⟩|ϵ1(t)⟩+ β |v⟩|Av⟩|ϵ2(t)⟩, with unknown coeﬃcents α and β such
that |α|2 + |β|2 = 1, and |α| > 0. It is very important to note that this conclusion, which is one of the trademarks of the
decoherence formalism, is totally diﬀerent from the standard interpretation of quantum measurements, following which
the observer concludes that the state of the system is |Ψ2⟩= |h⟩|Ah⟩as the aftermath of observing the outcome h.
[13] J. M. G. G´omez, K. Kar, V. K. B. Kota, R. A. Molina, A. Rela˜no, and J. Retamosa, Many-body quantum chaos: Recent
developments and applications to nuclei, Phys. Rep. 499, 103 (2011).
[14] F. Arute et al., Quantum supremacy using a programmable superconducting processor, Nature 574, 505 (2019).
[15] Y. Y. Atas, E. Bogomolny, O. Giraud, and G. Roux, Distribution of the Ratio of Consecutive Level Spacings in Random
Matrix Ensembles, Phys. Rev. Lett. 110, 084101 (2013).
[16] A. L. Corps and A. Rela˜no, Distribution of the Ratio of Consecutive Level Spacings for Any Symmetry and Arbitrary
Degree of Chaos, arXiv:1910-01434 (2019).
[17] V. Baumann and C. Brukner, Wigner’s friend as a rational agent, arXiv:1901.11274 (2019).
[18] From this point of view, we can consider that the measurement is done by a small quantum machine, and that an
ampliﬁcation process is done by the environment afterwards. In this way, the pre-measurement can be considered purely
quantum, whereas the ampliﬁcation, required for a large agent to see the outcome, is the responsible for the transition to
a classical outcome. Nevertheless, the result is the same if the external environment-apparatus interaction is still present,
provided that its characteristic time is larger than the time required to complete the pre-measurement.
[19] An interesting question is what happens if the non-diagonal elements, Chv and Cvh, are clearly diﬀerent from zero. In such
a case, the interaction between the apparatus and the environment does not determine the pointer states of the apparatus,
and therefore the agent cannot see a deﬁnite outcome. On the contrary, the instantaneous eigenbasis of the reduced density
matrix resulting from tracing out the environmental degrees of freedom is continuously changing in time, and therefore the
agent memory does not record a deﬁnite result for the measurement. As the ﬂuctuations of these diagonal elements are
expected to be tiny if the environment is large enough, the outcomes can be considered stable. A more detailed discussion
can be found in [5].
[20] M. F. Pusey, An inconsistent friend, Nat. Phys. 14, 973 (2018).
[21] I. Salom, To the rescue of Copenhaguen interpretation, arXiv:1809.01746 (2018).
[22] R. Haley, Quantum theory and the limits of objetivity, Found. Phys. 48, 1568 (2018).
[23] D. Lazarovici and M. Hubert, How quantum mechanics can consistently describe the use of itself, Sci. Rep. 9, 470 (2019).
[24] As a marginal note, it is revealing to notice that the perfect correlation between outcomes hb and va, or, equivalently,
between ha and vb, occur without any kind of non-local collapse. The measurement performed on stage 1 does not aﬀect
photon b, and hence the fact that agent IA observes the deﬁnite outcome ha does not imply that the other photon, which
can be far away, instantaneoulsy collapses onto vb. The result of such a measurement is Eq. (34). Eq. (51) is just a practical
representation of what both agents see as a consequence of ignoring both environments, but not the result of a physical


## Page 29


29
process involving a non-local collapse.
[25] J. Clauser, M. Horne, A. Shimony, and R. Holt, Proposed Experiment to Test Local Hidden-Variable Theories, Phys. Rev.
Lett. 23, 880 (1969).
[26] M. Zukowksi and C. Brukner, Quantum non-locality —it ain’t necessarily so. . ., J. Phys. A 47, 424009 (2014).

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1908_09737v2_decoherence_framework_for_wigner_s_friend_experiments
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1908_09737V2_DECOHERENCE_FRAMEWORK_FOR_WIGNER_S_FRIEND_EXPERIMENTS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

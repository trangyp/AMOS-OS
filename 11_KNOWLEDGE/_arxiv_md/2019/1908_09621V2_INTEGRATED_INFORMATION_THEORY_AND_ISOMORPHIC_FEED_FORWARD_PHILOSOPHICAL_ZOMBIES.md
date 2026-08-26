---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.09621v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1908.09621v2_Integrated_Information_Theory_and_Isomorphic_Feed-Forward_Philosophical_Zombies

> Source: 1908.09621v2_Integrated_Information_Theory_and_Isomorphic_Feed-Forward_Philosophical_Zombies.pdf

> Pages: 13

---


## Page 1


Article
Integrated Information Theory and Isomorphic
Feed-Forward Philosophical Zombies
Jake R. Hanson 1,2 and Sara I. Walker 1,2,3,∗
1
School of Earth and Space Exploration, Arizona State University, Tempe, AZ, USA
2
Beyond Center for Fundamental Concepts in Science, Arizona State University, Tempe, AZ, USA
3
ASU–SFI Center for Biosocial Complex Systems, Arizona State University, Tempe, AZ, USA
*
Correspondence: jake.hanson@asu.edu
Received: date; Accepted: date; Published: date
Abstract: Any theory amenable to scientiﬁc inquiry must have testable consequences. This minimal
criterion is uniquely challenging for the study of consciousness, as we do not know if it is possible to
conﬁrm via observation from the outside whether or not a physical system knows what it feels like to
have an inside - a challenge referred to as the "hard problem” of consciousness. To arrive at a theory
of consciousness, the hard problem has motivated development of phenomenological approaches
that adopt assumptions of what properties consciousness has based on ﬁrst-hand experience and,
from these, derive the physical processes that give rise to these properties. A leading theory adopting
this approach is Integrated Information Theory (IIT), which assumes our subjective experience
is a “uniﬁed whole”, subsequently yielding a requirement for physical feedback as a necessary
condition for consciousness. Here, we develop a mathematical framework to assess the validity of
this assumption by testing it in the context of isomorphic physical systems with and without feedback.
The isomorphism allows us to isolate changes in Φ without affecting the size or functionality of the
original system. Indeed, we show that the only mathematical difference between a "conscious" system
with Φ > 0 and an isomorphic "philosophical zombie" with Φ = 0 is a permutation of the binary labels
used to internally represent functional states. This implies Φ is sensitive to functionally arbitrary
aspects of a particular labeling scheme, with no clear justiﬁcation in terms of phenomenological
differences. In light of this, we argue any quantitative theory of consciousness, including IIT, should
be invariant under isomorphisms if it is to avoid the existence of isomorphic philosophical zombies
and the epistemological problems they pose.
Keywords: Consciousness; Integrated Information Theory; Krohn-Rhodes Decomposition
1. Introduction
The scientiﬁc study of consciousness walks a ﬁne line between physics and metaphysics. On the
one hand, there are observable consequences to what we intuitively describe as consciousness. Sleep,
for example, is an outward behavior that is uncontroversially associated with a lower overall level
of consciousness. Similarly, scientists can decipher what is intrinsically experienced when humans
are conscious via verbal reports or other outward signs of awareness. By studying the physiology of
the brain during these speciﬁc behaviors, scientists can build "neuronal correlates of consciousness"
(NCCs), which specify where in the brain conscious experience is generated and what physiological
processes correlate with it [1]. On the other hand, NCCs cannot be used to explain why we are conscious
or to predict whether or not another system demonstrating similar properties to NCCs is conscious.
Indeed, NCCs can only tell us the physiological processes that correlate with what are assumed to
be the functional consequences of consciousness and, in principle, may not actually correspond to a
measurement of what it is like to have subjective experience [2]. In other words, we can objectively
measure behaviors we assume accurately reﬂect consciousness but, currently, there exist no scientiﬁc
tools permitting testing our assumptions. As a result, we struggle to differentiate whether a system is
arXiv:1908.09621v2  [cs.IT]  1 Oct 2019


## Page 2


2 of 13
truly conscious or is instead simply going through the motions and giving outward signs of, or even
actively reporting, an internal experience that does not exist (e.g. [3]).
This is the "hard problem" of consciousness [2] and it is what differentiates the study of
consciousness from all other scientiﬁc endeavors. Since consciousness is subjective (by deﬁnition), there
is no objective way to prove whether or not a system experiences it. Addressing the hard problem,
therefore, necessitates an inversion of the approach underlying NCCs: rather than starting with
observables and deducing consciousness, one must start with consciousness and deduce observables.
This has motivated theorists to develop phenomenological approaches that adopt rigorous assumptions
of what properties consciousness must include based on human experience, and, from these, "derive"
the physical processes that give rise to these properties. The beneﬁt to this approach is not that the
hard-problem is avoided, but rather, that the solution appears self-evident given the phenomenological
axioms of the theory. In practice, translating from phenomenology to physics is rarely obvious, but the
approach remains promising.
The phenomenological approach to addressing the hard problem of consciousness is exempliﬁed
in Integrated Information Theory (IIT) [4,5], a leading theory of consciousness. Indeed, IIT is a leading
contender in modern neuroscience precisely because it takes a phenomenological approach and offers
a well-motivated solution to the hard problem of consciousness [6]. Three phenomenological axioms
form the backbone of IIT: information, integration, and exclusion. The ﬁrst, information, states that
by taking on only one of the many possibilities a conscious experience generates information (in the
Shannon sense, e.g. via a reduction in uncertainty [7]). The second, integration, states each conscious
experience is a single "uniﬁed whole". And the third, exclusion, states conscious experience is exclusive
in that each component in a system can take part in at most one conscious experience at a time
(simultaneous overlapping experiences are forbidden). Given these three phenomenological axioms,
IIT derives a mathematical measure of integrated information - Φ - that is designed to quantify the
extent to which a system is conscious based on the logical architecture (i.e. the "wiring") underlying its
internal dynamics.
In constructing Φ as a phenomenologically-derived measure of consciousness, IIT must assume
a connection between its phenomenological axioms and the physical processes that embody these
axioms. It is important to emphasize that this assumption is nothing less than a proposed solution to
the hard problem of consciousness, as it connects subjective experience (axiomatized as integration,
information, and exclusion) and objective (measurable) properties of a physical system. As such, it
is possible for one to accept the phenomenological axioms of the theory without accepting Φ as the
correct quantiﬁcation of these axioms and, indeed IIT has undergone several revisions in an attempt
to better reﬂect the phenomenological axioms in the proposed construction of Φ [5,8,9]. If, on the
other hand, one accepts Φ as the correct mathematical translation of the theory’s phenomenological
axioms, no experimental result can disprove the theory because the theory automatically dictates the
interpretation of experimental results if the axioms hold.
The possibility of multiple mathematical interpretations of the same phenomenological axioms
implies that, in principle, two competing theories of consciousness can disagree on the results of an
experiment even if they accept the same phenomenological axioms - a situation that arises precisely
because of the hard problem. Justiﬁcation for a given phenomenological theory, therefore, must
ultimately come from how well the deductions of the theory match our intuitive understanding of what
consciousness is, as well as the logical consistency and believability of the underlying assumptions. In
this regard, it is important to thoroughly understand any unique or counterintuitive predictions that
are deduced, because accepting or rejecting these conclusions is the only way to even approach testing
the validity of the theory [10].
In the context of IIT, the implied existence of philosophical zombies is a particularly controversial
claim. Philosophical zombies are deﬁned as physical systems that are capable of perfectly emulating
the outward behavior of conscious systems but which nonetheless, lack subjective experience.
Epistemologically, the existence of philosophical zombies is problematic, as many have argued that


## Page 3


3 of 13
it is logically impossible for a scientiﬁc theory to justify their existence [11–13]. The fact that IIT
admits such systems, therefore, poses a serious threat to the validity of the assumptions that form the
foundations of the theory and, in particular, IIT’s mathematical translation of the integration axiom.
This is because, according to IIT, the phenomenological experience of an "irreducible whole" must be
mirrored by physical irreducibility in the substrate that gives rise to consciousness. Because of this,
physical feedback is assumed to be a necessary (but not sufﬁcient) condition for conscious experience,
such that any system that lacks feedback has Φ = 0 by deﬁnition [5]. Yet, results in automata theory
suggest a different interpretation. In what follows, we point to the Krohn-Rhodes [14,15] theorem
and other feed-forward decomposition techniques [13], which prove that there is nothing inherently
special about feedback from a functional perspective, aside from the fact that it often allows for a more
efﬁcient representation. This leads to the controversial conclusion that the behavior of any system with
feedback and Φ > 0 can be perfectly emulated by a feed-forward philosophical zombie with Φ = 0.
In response, IIT claims such systems lack consciousness because they are incapable of generating an
integrated experience, but this claim rests solely on the assumption that physical feedback is the correct
interpretation of what it means to have an integrated subjective experience.
To test this assumption, we demonstrate the existence of a fundamentally new type of
feed-forward philosophical zombie, namely, one that is isomorphic to its conscious counterpart in
its state-transitions. The isomorphism guarantees that the feed-forward system with Φ = 0 not only
emulates the input-output behavior of its conscious counterpart but does so without increasing the size of
the system. Thus, the internal states of the two systems are in one-to-one correspondence, which allows
us to isolate mathematical changes in Φ without introducing a qualitative difference in efﬁciency,
autonomy, or behavior across systems. Indeed, we show the only mathematical difference between the
"conscious" system with Φ > 0 and "unconscious" system with Φ = 0 is a permutation of the binary
labels used to instantiate internal states. This implies Φ depends on the speciﬁc internal representation
of a computation rather than the computation itself. Our formalism translates into a proposed
mathematical criterion that any measure of consciousness must be invariant under isomorphisms in
the state transition diagram. Enforcement of this criterion serves as a necessary, but not sufﬁcient,
formal condition for any theory of consciousness to be free from philosophical zombies and the
epistemological problems they pose.
2. Methods
2.1. Finite-State Automata
Finite-state automata are abstract computing devices, or "machines", designed to model a discrete
system as it transitions between states. Automata theory was invented to address biological and
psychological problems [16,17] and it remains an extremely intuitive choice for modeling neuronal
systems. This is because one can deﬁne an automaton in terms of how speciﬁc abstract inputs lead to
changes within a system. Namely, if we have a set of potential inputs Σ and a set of internal states Q,
we deﬁne an automaton A in terms of the tuple A = (Σ, Q, δ, q0) where δ : Σ × Q →Q is a map from
the current state and input symbol to the next state, and q0 ∈Q is the starting state of the system. To
simplify notation, we write δ(s, q) = q′ to denote the transition from q to q′ upon receiving the input
symbol s ∈Σ.
For example, consider the "right-shift automaton" A shown in Figure 1. This automaton is
designed to model a system with a two bit internal register that processes new elements from the input
alphabet Σ = {0, 1} by shifting the bits in the register to the right and appending the new element
on the left [18]. The global state of the machine is the combined state of the left and right register, so
Q = {00, 01, 10, 11} and the transition function δ speciﬁes how this global state changes in response to
each input, as shown in Figure 1b.
In addition to the global state transitions, each individual bit in the register of the right-shift
automaton is itself an automaton. In other words, the global functionality of the system is nothing


## Page 4


4 of 13
more than the combined output from a system of interconnected automata, each specifying the state of
a single component or "coordinate" of the system. Speciﬁcally, the right-shift automaton is comprised
of an automaton AQ1 responsible for the left bit of register and an automaton AQ2 responsible for the
right bit of the register. By deﬁnition, AQ1 copies the input from the environment and AQ2 copies
the state of AQ1. Thus, ΣQ1 = {0, 1} and ΣQ2 = Q1 = {0, 1} and the transition functions for the
coordinates are δQ1 = δQ2 = {δ(0, 0) = 0; δ(0, 1) = 0; δ(1, 0) = 1; δ(1, 1) = 1}. This ﬁne-grained view
of the right-shift automaton speciﬁes its logical architecture and is shown in Figure 1c. The logical
architecture of the system is the "circuitry" that underlies its behavior and, as such, is often speciﬁed
explicitly in terms of logic gates, with the implicit understanding that each logic gate is a component
automaton.
(a)
(b)
(c)
Figure 1. The "right-shift automaton" A in terms of its state-transition diagram (1a), transition function
δ (1b), and logical architecture (1c).
It is important to note that not all automata require multiple input symbols and it is common to
ﬁnd examples of automata with a single-letter input alphabet. In fact, any deterministic state-transition
diagram can be represented in this way, with a single input letter signaling the passage of time. In
this case, the states of the automaton are the states of the system, the input alphabet is the passage of
time, and the transition function δ is given by the transition probability matrix (TPM) for the system.
Because Φ is a mathematical measure that takes a TPM as input, this specialized case provides a
concrete link between IIT and automata theory. Non-deterministic TPMs can also be described in
terms of ﬁnite-state automata [18,19] but, for our purposes, this generalization is not necessary.
2.2. Cascade Decomposition
The idea of decomposability is central to both IIT and automata theory. As Tegmark [20] points out,
mathematical measures of integrated information, including Φ, quantify the inability to decompose
a transition probability matrix M into two independent processes MA and MB. Given a distribution
over initial states p, if we approximate M by the tensor factorization ˆM ≈MA ⊗MB, then Φ, in
general, quantiﬁes an information theoretic distance D between the regular dynamics Mp and the
dynamics under the partitioned approximation ˆMp (i.e. Φ = D(Mp|| ˆMp)). In the latest version of IIT
[5], only unidirectional partitions are implemented (information can ﬂow in one direction across the
partition) which mathematically enforces the assumption that feedback is a necessary condition for
consciousness.
Decomposition in automata theory, on the other hand, has historically been an engineering
problem. The goal is to decompose an automaton A into an automaton A′ which is made of simpler
physical components than A and maps homomorphically onto A. Here, we deﬁne a homomorphism h


## Page 5


5 of 13
as a map from the states, stimuli, and transitions of A′ onto the states, stimuli, and transitions of A
such that for every state and stimulus in A′ the results obtained by the following two methods are
equivalent [16]:
1. Use the stimulus of A′ to update the state of A′ then map the resulting state onto A.
2. Map the stimulus of A′and the state of A′ to the corresponding stimulus/state in A then update
the state of A using the stimulus of A.
In other words, the map h is a homomorphism if it commutes with the dynamics of the system.
The two operations (listed above) that must commute are shown schematically in Figure 2. If the
homomorphism h is bijective then it is also an isomorphism and the two automata necessarily have the
the same number of states.
From an engineering perspective, homomorphic/isomorphic logical architectures are useful
because they allow ﬂexibility when choosing a logical architecture to implement a given computation.
Mathematically, the difference between homomorphic automata is the internal labeling scheme used to
encode the states/stimuli of the global ﬁnite-state machine, which speciﬁes the behavior of the system.
Thus, the homomorphism h is a dictionary that translates between different representations of the same
computation. Just as the same sentence can be spoken in different languages, the same computation can
be instantiated using different encodings. Under this view, what gives a computational state meaning
is not its binary representation (label) but rather its causal relationship with other states/stimuli, which
is what the homomorphism preserves.
Figure 2. For the map h to be a homomorphism from A′ onto A, updating the dynamics then applying
h (top) must yield the same state of A as applying h then updating the dynamics (bottom).
Because we are interested in isolating the role of feedback, the speciﬁc type of decomposition we
seek is a feed-forward or cascade decomposition of the logical architecture of a given system. Cascade
decomposition takes the automaton A and decomposes it into a homomorphic automaton A′ comprised
of several elementary automata "cascaded together". By this, what is meant is that the output from one
component serves as the input to another such that the ﬂow of information in the system is strictly
unidirectional (Figure 3). The resulting logical architecture is said to be in "cascade" or "hierarchical"
form and is functionally identical to the original system (i.e. it realizes the same global ﬁnite-state
machine).
At this point, the connection between IIT and cascade decomposition is readily apparent: if an
automaton with feedback allows a homomorphic cascade decomposition, then the behavior of the
resulting system is indistinguishable from the original but utilizes only feed-forward connections.
Therefore, there exists a unidirectional partition of the system that leaves the dynamics of the new
system (i.e. the transition probability matrix) unchanged such that Φ = 0 for all states.
In the language of Oizumi et al. [5], we can prove this by letting C→be the constellation that is
generated as a result of any unidirectional partition and C be the original constellation. Because C→
has no effect on the TPM, we are guaranteed that C→= C and ΦMIP = D(C|C→) = 0. We can repeat
this process for every possible subsystem within a given system and, since the ﬂow of information is
always unidirectional, ΦMIP = 0 for all subsets so ΦMax = 0. Thus, Φ = 0 for all states and subsystems
of a cascade automaton.


## Page 6


6 of 13
Figure 3. An example of a fully connected three component system in cascade form. Any subset of the
connections drawn above meets the criteria for cascade form because information ﬂows unidirectionally.
Pertinently, the Krohn-Rhodes theorem proves that every automaton can be decomposed into
cascade form [14,15], which implies every system for which we can measure non-zero Φ allows a feed-forward
decomposition with Φ = 0. These feed-forward systems are "philosophical zombies" in the sense that
they lack subjective experience according to IIT (e.g. Φ = 0), but they nonetheless perfectly emulate the
behavior of conscious systems. Yet, the Krohn-Rhodes theorem does not tell us how to construct such
systems. Furthermore, the map between systems is only guaranteed to be homomorphic (many-to-one)
which allows for the possibility that Φ is picking up on other properties (e.g. such as the efﬁciency
and/or autonomy of the computation) in addition to the presence or absence of feedback [5].
To isolate what Φ is measuring, we must go one step further and insist that the decomposition is
isomorphic (one-to-one) such that the original and zombie systems can be considered to perform the
same computation (same global state-transition topology) under the same resource constraints. In
this case, the feed-forward system has the exact same number of states as its counterpart with feedback.
Provided the latter has Φ > 0, this implies Φ is not a measure of the efﬁciency of a given computation,
as both systems require the same amount of memory. This is not to say that feedback and Φ do not
correlate with efﬁciency because, in general, they do [21]. For certain computations, however, the
presence of feedback is not associated with increased efﬁciency but only increased interdependence
among elements.
It is these speciﬁc corner cases that are most beneﬁcial if one wants to assess the validity of
the theory, as they allow one to understand whether or not feedback is important in absence of the
beneﬁts typically associated with its presence. In other words, IIT’s translation of the integration
axiom is that feedback is a minimal criterion for the subjective experience of a uniﬁed whole; yet, Φ is
described as quantifying "the amount of information generated by a complex of elements, above and
beyond the information generated by its parts" [4], which seems to imply feedback enables something
"extra" feed-forward systems cannot reproduce. An isomorphic feed-forward decomposition allows
us to carefully track the mathematical changes that destroy this additional information, in a way that
lets us preserve the efﬁciency and functionality of the original system. This, in turn, provides the
clearest possible case to test whether or not this additional information is likely to correspond to a
phenomenological difference between systems.
2.3. Feed-forward Isomorphisms via Preserved Partitions
The special type of computation that allows an isomorphic feed-forward decomposition is one
in which the global state-transition diagram is amenable to decomposition via a nested sequence of
preserved partitions. A preserved partition is a way of partitioning the state space of a system into
blocks of states (macrostates) that transition together. Namely, a partition P is preserved if it breaks the
state space S into a set of blocks {B1, B2, ..., BN} such that every state within each block transitions to a


## Page 7


7 of 13
state within the same block [16,22]. If we denote the state-transition function f : S →S, then a block Bi
is preserved when:
∃j ∈{1, 2, ..., N} such that f (x) ∈Bj∀x ∈Bi
In other words, for Bi to be preserved, ∀x in Bi x must transition to some state in a single block Bj
(i = j is allowed). Conversely, Bi is not preserved if there exist two or more states in Bi that transition
to different blocks (i.e. ∃x1, x2 ∈Bi such that f (x1) = Bj and f (x2) = Bk with j ̸= k ). In order for the
entire partition Pi to be preserved, each block within the partition must be preserved.
For an isomorphic cascade decomposition to exist, we must be able to iteratively construct a
hierarchy or "nested sequence" of preserved partitions such that each partition Pi evenly splits the
partition Pi−1 above it in half, leading to a more and more reﬁned description of the system. For a
system with 2n states where n is the number of binary components in the original system, this implies
that we need to ﬁnd exactly n nested preserved partitions, each of which then maps onto a unique
component of the cascade automaton, as demonstrated in Section 2.3.1.
If one cannot ﬁnd a preserved partition made of disjoint blocks or the blocks of a given partition
do not evenly split the blocks of the partition above it in half, then the system in question does not allow
an isomorphic feed-forward decomposition. It will, however, still allow a homomorphic feed-forward
decomposition based on a nested sequence of preserved covers, which forms the basis of standard
Krohn-Rhodes decomposition techniques [16,23,24]. Unfortunately, we do not know of a way to
tell a priori whether or not a given computation will ultimately allow an isomorphic feed-forward
decomposition, although a high degree of symmetry in the global state-transition diagram is certainly
a requirement.
2.3.1. Example: AND/OR ∼= COPY/OR
As an example, we will isomorphically decompose the feedback system X, comprised of an AND
gate and an OR gate, shown in Figure 4a. As it stands, X is not in cascade form because information
ﬂows bidirectionally between the components Q1 and Q2. While this feedback alone is insufﬁcient to
guarantee Φ > 0, one can readily check that X does indeed have Φ > 0 for all possible states (e.g. [25]).
The global state-transition diagram for the system X is shown in Figure 4c. Note, we have purposefully
left off the binary labels that X uses to instantiate these computational states, as the goal is to relabel
them in a way that results in a different (feed-forward) instantiation. In general, one typically starts
from the computation and derives a single logical architecture but, here, we must start and end with
ﬁxed (isomorphic) logical architectures - passing through the underlying computation in between. The
general form of the feed-forward logical architecture X′ that we seek is shown in Figure 4b.
Given the global state-transition diagram shown in Figure 4c, we let our ﬁrst preserved partition
be P1 = {B0, B1} with B0 = {A, D} and B1 = {B, C}. It is easy to check that this partition is preserved,
as one can verify that every element in B0 transitions to an element in B0 and every element in B1
transitions to an element in B1 (shown topologically in Figure 5a). We then assign all the states in B0 a
ﬁrst coordinate value of 0 and all the states in B1 a ﬁrst coordinate value of 1, which guarantees the
state of the ﬁrst coordinate is independent of later coordinates. If the value of the ﬁrst coordinate is 0
it will remain 0 and if the value of the ﬁrst coordinate is 1 it will remain one, because states within
a given block transition together. Because 0 goes to 0 and 1 goes to 1, the logic element (component
automaton) representing the ﬁrst coordinate Q′
1 is a COPY gate receiving its previous state as input.
The second preserved partition P2 must evenly split each block within P1 in half. Letting P2 =
{{B00, B01}, {B10, B11}} we have B00 = {A}, B01 = {B}, B10 = {C}, and B11 = {D}. At this stage, it is
trivial to verify that the partition is preserved because each block is comprised of only one state which
is guaranteed to transition to a single block. As with Q′
1, the logic gate for the second coordinate (Q′
2)
is speciﬁed by the way the labeled blocks of P2 transition. Namely, we have B00 →B00, B01 →B01,
B10 →B01, and B11 →B11. Note, the transition function δQ2 is completely deterministic given input
from the ﬁrst two coordinates (as required) and is given by δQ2 = {00 →0; 01 →1; 10 →1; 11 →1}.
This implies Q′
2 is an OR gate receiving input from both Q′
1 and Q′
2.


## Page 8


8 of 13
(a)
(b)
(c)
Figure 4. The goal of an isomorphic cascade decomposition is to decompose the integrated logical
architecture of the system X (4a) so that it is in cascade form X′ (4b) without affecting the state-transition
topology of the original system (4c).
(a)
(b)
(c)
Figure 5. The nested sequence of preserved partitions in 5a yields the isomorphism 5b between X and
X′ which can be translated into the strictly feed-forward logical architecture with Φ = 0 shown in 5c.
At this point, the isomorphic cascade decomposition is complete. We have constructed an
automaton for Q′
1 that takes input from only itself and an automaton for Q′
2 that takes input only from
itself and earlier coordinates (i.e. Q′
1 and Q′
2). The mapping between the states of X and the states of
X′, shown in Figure 5b, is speciﬁed by identifying the binary labels (internal representations) each
system uses to instantiate the abstract computational states A, B, C, D of the global state-transition
diagram. Because X and X′ operate on the same support (the same four binary states) the fact that they
are isomorphic implies the difference between representations is nothing more than a permutation
of the labels used to instantiate the computation. By choosing a speciﬁc labelling scheme based on
isomorphic cascade decomposition, we can induce a logical architecture that is guaranteed to be
feedback free and has Φ = 0. In this way we have "unfolded" the feedback present in X without
affecting the size/efﬁciency of the system.
3. Results/Discussion
We are now prepared to demonstrate the existence of isomorphic feed-forward philosophical
zombies in systems similar to those found in Oizumi et al. [5]. To do so, we will decompose the
integrated system Y shown in Figure 6 into an isomorphic feed-forward philosophical zombie Y′ of the
form shown in Figure 3. The system Y, comprised of two XNOR gates and one XOR gate, clearly contains
feedback between components and has Φ > 0 for all states for which Φ can be calculated (Figure 8c).
As in Section 2.3, the goal of the decomposition is an isomorphic relabeling of the ﬁnite-state machine
representing the global behavior of the system, such that the induced logical architecture is strictly
feed-forward.


## Page 9


9 of 13
(a)
(b)
(c)
Figure 6. The transition probability matrix (6a), logical architecture (6b), and all available Φ values (6c)
for the example system Y (n/a implies Φ is not deﬁned for a given state because it is unreachable).
We ﬁrst evenly partition the state space of Y into two blocks B0 = {A, C, G, H} and B1 =
{B, D, E, F}. Under this partition, B0 transitions to B1 and B1 transitions to B0, which implies the
automaton representing the ﬁrst coordinate in the new labeling scheme is a NOT gate. Note, this
choice is not unique, as we could just as easily have chosen a different preserved partition such as
B0 = {A, D, E, H} and B1 = {B, C, F, G}, in which case the ﬁrst coordinate would be a COPY gate; as
long as the partition is preserved, the choice here is arbitrary and amounts to selecting one of several
different feed-forward logical architectures - all in cascade form. For the second preserved partition, we
let P2 = {{B00, B01}, {B10, B11}} with B00 = {C, G}, B01 = {A, H}, B10 = {B, F}. and B11 = {D, E}.
The transition function for the automaton representing the second coordinate, given by the movement
of these blocks, is: δQ2′ = {00 →0; 01 →1; 10 →0; 11 →1}, which is again a COPY gate receiving
input from itself. The third and ﬁnal partition P3 assigns each state to its own unique block. As is
always the case, this last partition is trivially preserved because individual states are guaranteed to
transition to a single block. The transition function for this coordinate, read off the bottom row of
Figure 7, is given by:
δQ3′ = {000 →0; 001 →0; 010 →1; 011 →1; 100 →0; 101 →0; 110 →1; 111 →1}
Using Karnuagh maps [26], one can identify δQ3 as a COPY gate receiving input from Q′
2. With the
speciﬁcation of the logic for the third coordinate, the cascade decomposition is complete and the new
labeling scheme is shown in Figure 7. A side-by-side comparison of the original system Y and the
feed-forward system Y′ is shown in Figure 8. As required, the feed-forward system has Φ = 0 but
executes the same sequence of state transitions as the original system, modulo a permutation of the
labels used to instantiate the states of the global state-transition diagram. If the system with Φ > 0 is
experiencing something more, it is something beyond the ﬁnite-state description of the system (the
state-transition diagram) and, therefore, its presence or absence has no causal consequences to the
structure of its internal state-transition map (the computation it performs).
3.1. Discussion
Behavior is most frequently described in terms of abstract states/stimuli, which are not tied
to a speciﬁc representation (binary or otherwise). Examples include descriptors of mental states,
such as being asleep or awake, etc., these are representations of system states that must be deﬁned
either by an external observer or internally in the system performing the computation by its own
logical implementation, but are not necessarily an intrinsic attribute of the computational states
themselves (e.g. these states could be labeled with any binary assignment consistent with the state
transition diagram of the computation). The analysis presented here is based on this premise, such
that behavior is deﬁned by the topology of the state-transition diagram, independent of a particular


## Page 10


10 of 13
Figure 7. Nested sequence of preserved partitions used to decompose Y into cascade form.
(a)
(b)
(c)
(d)
Figure 8. Side-by-side comparison of the feedback system Y with Φ > 0 (8a) and its isomorphic
feed-forward counterpart Y′ with Φ = 0 (8c). The global state-transition diagrams (8b and 8d,
respectively) differ only by a permutation of labels.
labeling scheme. And, indeed, it is this premise that enables Krohn-Rhodes decomposition to be useful
from an engineering perspective, as one can swap between logical architectures without affecting the
operation of a system in any way.
Phenomenologically, consciousness is often associated with the concept of “top-down causation”,
where ‘higher level’ mental states exert causal control over lower level implementation [27]. The
"additional information" provided by consciousness above and beyond non-conscious systems is
considered to be functionally relevant by affecting how states transition to other states. It is in this
sense behavior associated with consciousness in our formalism is most appropriately thought of as a
computation having to do with the topology (causal architecture) of state-transitions, rather than the
labels of the states or the speciﬁc logical architecture. We note this kind of top-down causation can occur
without the need to appeal to supervenience because in our framework the computation/function
describes a functional equivalence class [28] of logical architectures that all implement the same causal


## Page 11


11 of 13
relations among states, i.e. it is an abstraction implemented in a particular logic. There is no additional
“room at the bottom” for a particular logical architecture to exert more causal inﬂuence than another if
they perform the same function. Any measure of consciousness that changes under the isomorphism
we introduce here, such as Φ, cannot therefore account for “additional information” in this sense,
because of the existence of zombie systems with an identical structure to their state transitions.
It is important to recognize there exists an alternative interpretation of behavior associated to
consciousness, where one deﬁnes behavior not in terms of abstract computation, but in terms of the
speciﬁc logical implementation, for example as IIT adopts. A clear example is the right-shift automaton,
which is deﬁned in terms of the relationship between components, resulting in a state-transition
diagram with speciﬁc labels, because their exists strict constraints on the logical implementation of
the behavior. However, this does not address, in our view, whether isomorphic systems ultimately
experience a phenomenological difference as there is no way to test that assumption other than
accepting it axiomatically. In particular, for the examples we consider here, there is only one input
signal, meaning there are not multiple ways to encode input from the environment. Therefore there
is no physical mechanism by which the environment can dictate a privileged internal representation.
Instead the choice of internal representation is arbitrary with respect to the environment and depends
only on the physical constraints of the architecture of the system performing the computation. For
a system as complex as the human brain, there are presumably many possible logical architectures
(network topologies) that can perform the same computation given the same input, differing only in
how the states are internally represented (e.g. by how neurons are wired together). Why the ones
that have evolved were selected in the ﬁrst place is important for understanding why consciousness
emerged in the universe. The foregoing suggests Φ is independent of functionality (computation),
which implies there are no inherent evolutionary beneﬁts to the presence or absence of Φ because it is
not selectable as being distinctive to a particular computation an organism must perform for survival,
only to how that computation is internally represented. Integration as a criterion separated from
computation, is also itself problematic as it must be experienced by every component individually, yet,
a single bit can make only one measurement (yes/no) and therefore components cannot sense where
their information came from or where it is going.
This leads us to the central question of this manuscript, which is what is experienced as the
isomorphic system with Φ > 0 cycles through its internal states that is not experienced by the
isomorphic system with Φ = 0?
Since in our examples the environment is not dictating the
representation of the input, and all state transitions are isomorphic, the representation and therefore
the logic is arbitrary so long as a logical architecture is selected with the proper input-output map
under all circumstances. In light of this, our formalism suggests any mathematical measure of
consciousness, phenomenologically motivated or otherwise, must be invariant under isomorphisms in
the computation. This minimal criterion implies measurable differences in consciousness are always
associated with measurable differences in the computational function (though the inverse need not
be true), which is nothing more than a precise mathematical enforcement of the precedent set by
Turing [11]. From this perspective, measures of consciousness should operate on the topology of the
state-transition diagram, rather than the topology or logic of a particular physical implementation. That
is, they should probe the computational capacity of the system without being biased by implementation
- allowing identifying equivalence classes of physical systems that could have the same or similar
conscious experience.
Our motivation in this work is to provide new roads to address the hard problem of consciousness
by raising new questions. Our framework focuses attention on the fact that we currently lack
a sufﬁciently formal understanding of the relationship between physical implementation and
computation to truly address the hard problem. The logical architectures in Figures 8a and 8c are
radically different, and yet, they perform the same computation. The fact that this computation allows
a feed-forward decomposition is a consequence of redundancies that allow a compressed description
in terms of a feed-forward logical architecture. There are symmetries present in the computation that


## Page 12


12 of 13
allow one to take advantage of shortcuts and reduce the computational load. This, in turn, shows
up as a ﬂexibility in the logical architecture that can generate the computation. In other words, the
computation in question does not appear to require the maximum computational power of a three-bit
logical architecture. For sufﬁciently complex eight-state computations, however, the full capacity of
a three-bit architecture is required, as there is no redundancy to compress. Such systems cannot be
generated without feedback, as the presence of feedback is accompanied by indispensable functional
consequences. Thus, the computation is special because it cannot be efﬁciently represented without
feedback - a relationship that can, in principle, be understood, but is only tangentially accounted for
in current formalisms. It is up to the community to decide if the functionalist or phenomenological
perspective will ultimately hold up, our goal in this work is simply to point out where the distinction
between the two sets of ideas is very apparent and clear-cut mathematically, so that additional progress
can be made.
Author Contributions: Conceptualization, J.H. and S.W.; formal analysis, J.H.; funding acquisition, S.W.;
investigation, J.H.; methodology, J.H.; project administration, S.W.; resources, S.W.; supervision, S.W.; visualization,
J.H.; writing-original draft preparation, J.H. and S.W.; writing-review and editing, J.H. and S.W.
Acknowledgments: The authors would like to thank Doug Moore for his assistance with the Krohn-Rhodes
theorem and semigroup theory, as well as Dylan Gagler and the rest of the emergence@asu lab for thoughtful
feed-back and discussions. SIW also acknowledges funding support from the Foundational Questions in Science
Institute.
Conﬂicts of Interest: The authors declare no conﬂict of interest. The funders had no role in the design of the
study; in the collection, analyses, or interpretation of data; in the writing of the manuscript, or in the decision to
publish the results.
References
1.
Rees, G.; Kreiman, G.; Koch, C. Neural correlates of consciousness in humans. Nature Reviews Neuroscience
2002, 3, 261.
2.
Chalmers, D.J. Facing Up to the Problem of Consciousness. Journal of Consciousness Studies 1995, 2, 200–19.
3.
Searle, J.R. Minds, brains, and programs. Behavioral and brain sciences 1980, 3, 417–424.
4.
Tononi, G. Consciousness as integrated information: a provisional manifesto. The Biological Bulletin 2008,
215, 216–242.
5.
Oizumi, M.; Albantakis, L.; Tononi, G. From the phenomenology to the mechanisms of consciousness:
integrated information theory 3.0. PLoS computational biology 2014, 10, e1003588.
6.
Tononi, G.; Boly, M.; Massimini, M.; Koch, C. Integrated information theory: from consciousness to its
physical substrate. Nature Reviews Neuroscience 2016, 17, 450.
7.
Shannon, C.E. A mathematical theory of communication. Bell system technical journal 1948, 27, 379–423.
8.
Tononi, G. An information integration theory of consciousness. BMC neuroscience 2004, 5, 42.
9.
Balduzzi, D.; Tononi, G. Integrated information in discrete dynamical systems: motivation and theoretical
framework. PLoS computational biology 2008, 4, e1000091.
10.
Godfrey-Smith, P. Theory and reality: An introduction to the philosophy of science; University of Chicago Press,
2009.
11.
Turing, A. Computing Machinery and Intelligence. Mind 1950, 59, 433–433.
12.
Harnad, S. Why and how we are not zombies. Journal of Consciousness Studies 1995, 1, 164–167.
13.
Doerig, A.; Schurger, A.; Hess, K.; Herzog, M.H.
The unfolding argument: Why IIT and other
causal structure theories cannot explain consciousness.
Consciousness and Cognition 2019, 72, 49 – 59.
doi:https://doi.org/10.1016/j.concog.2019.04.002.
14.
Krohn, K.; Rhodes, J. Algebraic theory of machines. I. Prime decomposition theorem for ﬁnite semigroups
and machines. Transactions of the American Mathematical Society 1965, 116, 450–464.
15.
Zeiger, H.P. Cascade synthesis of ﬁnite-state machines. Information and Control 1967, 10, 419–433.
16.
Arbib, M.; Krohn, K.; Rhodes, J. Algebraic theory of machines, languages, and semi-groups; Academic Press,
1968.
17.
Shannon, C.E.; McCarthy, J. Automata Studies.(AM-34); Vol. 34, Princeton University Press, 2016.


## Page 13


13 of 13
18.
DeDeo, S.
Effective Theories for Circuits and Automata.
Chaos (Woodbury, N.Y.) 2011, 21, 037106.
doi:10.1063/1.3640747.
19.
Maler, O. A decomposition theorem for probabilistic transition systems. Theoretical Computer Science 1995,
145, 391–396.
20.
Tegmark, M. Improved measures of integrated information. PLoS computational biology 2016, 12, e1005123.
21.
Albantakis, L.; Hintze, A.; Koch, C.; Adami, C.; Tononi, G. Evolution of Integrated Causal Structures in
Animats Exposed to Environments of Increasing Complexity. PLOS Computational Biology 2014, 10, 1–19.
doi:10.1371/journal.pcbi.1003966.
22.
Hartmanis, J. Algebraic structure theory of sequential machines (prentice-hall international series in applied
mathematics); Prentice-Hall, Inc., 1966.
23.
Egri-Nagy, A.; Nehaniv, C.L. Hierarchical coordinate systems for understanding complexity and its
evolution, with applications to genetic regulatory networks. Artiﬁcial Life 2008, 14, 299–312.
24.
Egri-Nagy, A.; Nehaniv, C.L. Computational Holonomy Decomposition of Transformation Semigroups.
arXiv preprint arXiv:1508.06345 2015.
25.
Mayner, W.G.; Marshall, W.; Albantakis, L.; Findlay, G.; Marchman, R.; Tononi, G. PyPhi: A toolbox for
integrated information theory. PLoS computational biology 2018, 14, e1006343.
26.
Karnaugh, M. The map method for synthesis of combinational logic circuits. Transactions of the American
Institute of Electrical Engineers, Part I: Communication and Electronics 1953, 72, 593–599.
27.
Ellis, G. How can Physics Underlie the Mind. Springer2016 2016.
28.
Auletta, G.; Ellis, G.F.; Jaeger, L. Top-down causation by information control: from a philosophical problem
to a scientiﬁc research programme. Journal of the Royal Society Interface 2008, 5, 1159–1172.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
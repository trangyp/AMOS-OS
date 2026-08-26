---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1712.09644v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1712.09644v3_PyPhi__A_toolbox_for_integrated_information_theory

> Source: 1712.09644v3_PyPhi__A_toolbox_for_integrated_information_theory.pdf

> Pages: 29

---


## Page 1


PyPhi: A toolbox for integrated information theory
William G. P. Mayner1,2,*, William Marshall2, Larissa Albantakis2, Graham Findlay1,2,
Robert Marchman2, Giulio Tononi2,*
1 Neuroscience Training Program, University of Wisconsin–Madison, Madison, WI, USA
2 Department of Psychiatry, Wisconsin Institute for Sleep and Consciousness, University of Wisconsin–Madison,
Madison, WI, USA
*mayner@wisc.edu, *gtononi@wisc.edu
Abstract
Integrated information theory provides a mathematical framework to fully characterize
the cause-effect structure of a physical system. Here, we introduce PyPhi, a Python
software package that implements this framework for causal analysis and unfolds the
full cause-effect structure of discrete dynamical systems of binary elements. The
software allows users to easily study these structures, serves as an up-to-date reference
implementation of the formalisms of integrated information theory, and has been
applied in research on complexity, emergence, and certain biological questions. We first
provide an overview of the main algorithm and demonstrate PyPhi’s functionality in the
course of analyzing an example system, and then describe details of the algorithm’s
design and implementation.
PyPhi can be installed with Python’s package manager via the command
‘pip install pyphi’ on Linux and macOS systems equipped with Python 3.4 or higher.
PyPhi is open-source and licensed under the GPLv3; the source code is hosted on GitHub
at https://github.com/wmayner/pyphi. Comprehensive and continually-updated
documentation is available at https://pyphi.readthedocs.io. The pyphi-users mailing
list can be joined at https://groups.google.com/forum/#!forum/pyphi-users. A web-based
graphical interface to the software is available at
http://integratedinformationtheory.org/calculate.html.
1
Introduction
Integrated information theory (IIT) has been proposed as a theory of consciousness. The
central hypothesis is that a physical system has to meet five requirements (‘postulates’)
in order to be a physical substrate of subjective experience: (1) intrinsic existence (the
system must be able to make a difference to itself); (2) composition (it must be
composed of parts that have causal power within the whole); (3) information (its causal
power must be specific); (4) integration (its causal power must not be reducible to that
of its parts); and (5) exclusion (it must be maximally irreducible) [1–5].
From these postulates, IIT develops a mathematical framework to assess the
cause-effect structure (CES) of a physical system that is applicable to discrete dynamical
systems. This framework has proven useful not only for the study of consciousness but
has also been applied in research on complexity [6–9], emergence [10–12], and certain
biological questions [13].
The main measure of cause-effect power, integrated information (denoted Φ),
quantifies how irreducible a system’s CES is to those of its parts. Φ also serves as a
general measure of complexity that captures to what extent a system is both
integrated [6] and differentiated (informative) [14].
Here we describe PyPhi, a Python software package that implements IIT’s framework
for causal analysis and unfolds the full CES of discrete dynamical systems of binary
1/23
arXiv:1712.09644v3  [q-bio.NC]  27 Jun 2018


## Page 2


elements. The software allows users to easily study these CESs and serves as an
up-to-date reference implementation of the formalisms of IIT.
Details of the mathematical framework are published elsewhere [1,3]; in § Results
we describe the output and input of the software and give an overview of the main
algorithm in the course of reproducing results obtained from an example system studied
in [3]. In § Design and implementation we discuss specific issues concerning the
algorithm’s implementation. Finally in § Availability and future directions we describe
how the software can be obtained and discuss new functionality planned for future
versions.
2
Results
2.1
Output
The software has two primary functions: (1) to unfold the full CES of a discrete
dynamical system of interacting elements and compute its Φ value, and (2) to compute
the maximally-irreducible cause-effect repertoires of a particular set of elements within
the system. The first is function is implemented by pyphi.compute.major_complex(),
which returns a SystemIrreducibilityAnalysis object (Fig. 1A). The system’s CES is
contained in the ‘ces’ attribute and its Φ value is contained in ‘phi’. Other attributes are
detailed in the online documentation.
The CES is composed of Concept objects, which are the output of the second main
function: Subsystem.concept() (Fig. 1B). Each Concept is specified by a set of elements
within the system (contained in its ‘mechanism’ attribute). A Concept contains a
maximally-irreducible cause and effect repertoire (‘cause_repertoire’ and
‘effect_repertoire’), which are probability distributions that capture how the
mechanism elements in their current state constrain the previous and next state of the
system, respectively; a ϕ value (‘phi’), which measures the irreducibility of the
repertoires; and several other attributes discussed below and detailed in the online
documentation.
2.2
Input
The starting point for the IIT analysis is a discrete dynamical system S composed of n
interacting elements. Such a system can be represented by a directed graph of
interconnected nodes, each equipped with a Markovian function that outputs the node’s
state at the next timestep t + 1 given the state of its parents at the previous timestep t
(Fig. 2). At present, PyPhi can analyze both deterministic and stochastic systems
consisting of elements with two states.
Such a discrete dynamical system is completely specified by its transition probability
matrix (TPM), which contains the probabilities of all state transitions from t to t + 1. It
can be obtained from the graphical representation of the system by perturbing the
system into each of its possible states and observing the following state at the next
timestep (for stochastic systems, repeated trials of perturbation/observation will yield
the probabilities of each state transition). In PyPhi, the TPM is the fundamental
representation of the system.
Formally, if we let St be the random variable of the system state at t, the TPM
specifies the conditional probability distribution over the next state St+1 given each
current state st:
Pr(St+1 | St = st),
∀st ∈ΩS,
where ΩS denotes the set of possible states. Furthermore, given a marginal distribution
over the previous states of the system, the TPM fully specifies the joint distribution over
2/23


## Page 3


.phi
A
BC
.cut
A
C
B
.effect
.effect.repertoire
0
0.5
1
0
1
Pr(state)
.effect.purview
B
.effect.phi
.effect.mip
.effect.partitioned_repertoire
0
0.5
1
0
1
Pr(state)
.cause.partitioned_repertoire
0
0.5
1
00
10
01
11
Pr(state)
.cause.repertoire
0
0.5
1
00
10
01
11
Pr(state)
.cause.purview
B
C
.cause.phi
.cause.mip
.cause
.mechanism
A
.phi
Concept
SystemIrreducibilityAnalysis
.ces
Concept
Concept
Concept
.partitioned_ces
Concept
Concept
Concept
B
A
Fig 1. Output. (A) The SystemIrreducibilityAnalysis object is the main output of
the software. It represents the results of the analysis of the system in question. It has
several attributes (grey boxes): ‘ces’ is a CauseEffectStructure object containing all of
the system’s Concepts; ‘cut’ is a Cut object that represents the minimum-information
partition (MIP) of the system (the partition of the system that makes the least difference
to its CES); ‘partitioned_ces’ is the CauseEffectStructure of Concepts specified by
the system after applying the MIP; and ‘phi’ is the Φ value, which measures the
difference between the unpartitioned and partitioned CES. (B) A Concept represents the
maximally-irreducible cause (MIC) and maximally-irreducible effect (MIE) of a
mechanism in a state. The ‘mechanism’ attribute contains the indices of the mechanism
elements. The ‘cause’ and ‘effect’ attributes contain MaximallyIrreducibleCause and
MaximallyIrreducibleEffect objects that describe the mechanism’s MIC and MIE,
respectively; each of these contains a purview, repertoire, MIP, partitioned repertoire,
and ϕ value. The ‘phi’ attribute contains the concept’s ϕ value, which is the minimum of
the ϕ values of the MIC and MIE.
state transitions. Here IIT imposes uniformity on the marginal distribution of the
previous states because the aim of the analysis is to capture direct causal relationships
across a single timestep without confounding factors, such as influences from system
3/23


## Page 4


A
B
Network state at t
Pr(N = ON) at t + 1
A
B
C
A
B
C
0.0
0.0
0.0
0.0
0.0
1.0
1.0
0.0
1.0
1.0
0.0
0.0
1.0
0.0
0.0
1.0
1.0
1.0
1.0
0.0
1.0
1.0
1.0
0.0
OR
Input state
at t
Pr(ON)
at t + 1
B
C
A
0.0
1.0
1.0
1.0
XOR
Input state
at t
Pr(ON)
at t + 1
A
B
C
0.0
1.0
1.0
0.0
AND
Input state
at t
Pr(ON)
at t + 1
A
C
B
0.0
0.0
0.0
1.0
C
ON
OFF
Node TPMs
Network TPM
Fig 2. A network of nodes and its TPM. Each node has its own TPM—in this case, the
truth-table of a deterministic logic gate. Yellow signifies the “ON” state; white signifies
“OFF”. The system’s TPM (right) is composed of the TPMs of its nodes (left), here shown
in state-by-node form (see § Representation of the TPM and probability distributions).
Note that in PyPhi’s TPM representation, the first node’s state varies the fastest,
according to the little-endian convention (see § 2-dimensional state-by-node form).
states before t −1 [3,4,11,15,16]. The marginal distribution thus corresponds to an
interventional (causal), not observed, state distribution.
Moreover, IIT assumes that there is no instantaneous causation; that is, it is assumed
that the elements of the dynamical system influence one another only from one timestep
to the next. Therefore we require that the system satisfies the following Markov
condition, called the conditional independence property: each element’s state at t + 1
must be independent of the state of the others, given the state of the system at t [17],
Pr(St+1 | St = st) =
Y
N ∈S
Pr(Nt+1 | St = st) ,
∀st ∈S.
(1)
For systems of binary elements, a TPM that satisfies Eq. (1) can be represented in
state-by-node form (Fig. 2, right), since we need only store each element’s marginal
distribution rather than the full joint distribution.
In PyPhi, the system under analysis is represented by a Network object. A Network is
created by passing its TPM as the first argument: network = pyphi.Network(tpm) (see
4/23


## Page 5


§ Setup). Optionally, a connectivity matrix (CM) can also be provided, where
[CM]i,j =
(
1
if there is an edge from element i to element j
0
otherwise,
via the cm keyword argument: network = pyphi.Network(tpm, cm=cm). Because the
TPM completely specifies the system, providing a CM is not necessary; however, explicit
connectivity information can be used to make computations more efficient, especially for
sparse networks, because PyPhi can rule out certain causal influences a priori if there are
missing connections (see § Connectivity optimizations). Note that this means providing
an incorrect CM can result in inaccurate output. If no CM is given, PyPhi assumes full
connectivity; i.e., it assumes each element may have an effect on any other, which
guarantees correct results.
Once the Network is created, a subset of elements within the system (called a
candidate system), together with a particular system state, can be selected for analysis by
creating a Subsystem object. Hereafter we refer to a candidate system as a subsystem.
2.3
Demonstration
The mathematical framework of IIT is typically formulated using graphical causal
models as representations of physical systems of elements. The framework builds on the
causal calculus of the do( · ) operator introduced by Pearl [17]. In order to assess causal
relationships among the elements, interventions (manipulations, perturbations) are used
to actively set elements into a specific state, after which the resulting state transition is
observed.
For reference, we define a set of graphical operations that are used during the IIT
analysis. To fix an element is to use system interventions to keep it in the same state for
every observation. To noise an element is to use system interventions to set it into a state
chosen uniformly at random. Finally, to cut a connection from a source element to a
target element is to make the source appear noised to the target, while the remaining,
uncut connections from the source still correctly transmit its state.
In this section we demonstrate some of the capabilities of the software by unfolding
the CES of a small deterministic system of logic gates as described in [3] while
describing how the algorithm is implemented in terms of TPM manipulations, which we
link to the graphical operations defined above. A schematic of the algorithm is shown in
Fig. 3 and Fig. 4, and a more detailed illustration is given in S1 Calculating Φ.
2.3.1
Setup
The first step is to create the Network object. Here we choose to provide the TPM in
2-dimensional state-by-node form (see § 2-dimensional state-by-node form). The TPM is
the only required argument, but we provide the CM as well, since we know that there
are no self-loops in the system and PyPhi will use this information to speed up the
5/23


## Page 6


EXCLUSION
INTEGRATION
INFORMATION
mic(mechanism)
arg max φcause
cause_mip(mechanism, purview)
arg min repertoire_distance
effect_repertoire(
mechanism_part, purview_part)
effect_repertoire(
mechanism, purview)
mie(mechanism)
arg max φeffect
effect_mip(mechanism, purview)
arg min repertoire_distance
φ = min(φcause, φeffect)
concept(mechanism)
CAUSE
EFFECT
⊗
cause_repertoire(
mechanism_part, purview_part)
cause_repertoire(
mechanism, purview)
⊗
Iterate over all 
partitions of the 
(mechanism, purview)
pair
Iterate over all 
partitions of the 
(mechanism, purview)
pair
Iterate over all purviews, 
i.e., all subsets of the 
subsystem, P ∈𝒫(S ),
for a specific mechanism
Iterate over all purviews, 
i.e., all subsets of the 
subsystem, P ∈𝒫(S ),
for a specific mechanism
All parts (Mi, Pi) 
in the partition
All parts (Mi, Pi) 
in the partition
Fig 3. Algorithm schematic at the mechanism level. PyPhi functions are named in
boxes, with arguments in grey. Arrows point from callee to caller. Functions are
organized by the postulate they correspond to (left). ⊗denotes the tensor product; P
denotes the power set.
computation. We also label the nodes A, B, and C to make the output easier to read.
>>> import pyphi
>>> import numpy as np
>>> tpm = np.array([
...
[0.0, 0.0, 0.0],
...
[0.0, 0.0, 1.0],
...
[1.0, 0.0, 1.0],
...
[1.0, 0.0, 0.0],
...
[1.0, 0.0, 0.0],
...
[1.0, 1.0, 1.0],
...
[1.0, 0.0, 1.0],
...
[1.0, 1.0, 0.0]
... ])
>>> cm = np.array([
...
[0, 1, 1],
...
[1, 0, 1],
...
[1, 1, 0],
... ])
>>> network = pyphi.Network(tpm, cm=cm, node_labels=['A', 'B', 'C'])
We select a subsystem and a system state for analysis by creating a Subsystem object.
System states are represented by tuples of 1s and 0s, with 1 meaning “ON” and 0
meaning “OFF.” In this case we will analyze the entire system, so the subsystem will
contain all three nodes. The nodes to include can be specified with either their labels or
their indices (note that in other PyPhi functions, nodes must be specified with their
6/23


## Page 7


EXCLUSION
ces(cut_subsystem)
major_complex(network, state)
INTEGRATION
INFORMATION
ces(subsystem)
sia(subsystem)
Iterate over 
all subsets of the 
network, S ∈𝒫(N )
arg min ces_distance
arg max Φ(S )
concept(mechanism)
Iterate over 
all system cuts 
of the subsystem
concept(mechanism)
Iterate over 
all subsets of the 
subsystem, M ∈𝒫(S )
Iterate over 
all subsets of the 
cut_subsystem,
M ∈𝒫(Scut )
Fig 4. Algorithm schematic at the system level. PyPhi functions are named in boxes,
with arguments in grey. Arrows point from callee to caller. Functions are organized by
the postulate they correspond to (left). P denotes the power set.
indices).
>>> state = (1, 0, 0)
>>> nodes = ('A', 'B', 'C')
>>> subsystem = pyphi.Subsystem(network, state, nodes)
If there are nodes outside the subsystem, they are considered as background
conditions for the causal analysis [3]. In the graphical representation of the system, the
background conditions are fixed in their current state while the subsystem is perturbed
and observed in order to derive its TPM. In the TPM representation, the equivalent
operation is performed by conditioning the system TPM on the state at t of the nodes
outside the subsystem and then marginalizing out those nodes at t + 1 (illustrated in
S1 Calculating Φ). In PyPhi, this is done when the subsystem is created; the subsystem
TPM can be accessed with the tpm attribute, e.g. subsystem.tpm.
2.3.2
Cause/effect repertoires (mechanism-level information)
The lowest-level objects in the CES of a system are the cause repertoire and effect
repertoire of a set of nodes within the subsystem, called a mechanism, over another set of
nodes within the subsystem, called a purview of the mechanism. The cause (effect)
7/23


## Page 8


repertoire is a probability distribution that captures the information specified by the
mechanism about the purview by describing how the previous (next) state of the
purview is constrained by the current state of the mechanism.
In terms of graphical operations, the effect repertoire is obtained by (1) fixing the
mechanism nodes in their state at t; (2) noising the non-mechanism nodes at time t, so
as to remove their causal influence on the purview; and (3) observing the resulting state
transition from t to t + 1 while ignoring the state at t + 1 of non-purview nodes, in order
to derive a distribution over purview states at t + 1.
The cause repertoire is obtained similarly, but in that case, the purview nodes at time
t −1 are noised, and the resulting state transition from t −1 to t is observed while
ignoring the state of non-mechanism nodes. Bayes’ rule is then applied, resulting in a
distribution over purview states at t −1. The corresponding operations on the TPM are
detailed in § Calculation of cause/effect repertoires from the TPM and illustrated in
S1 Calculating Φ.
Note that, operationally, we enforce that each input from a noised node conveys
independent noise during the perturbation/observation step. In this way, we avoid
counting correlations from outside the mechanism-purview pair as constraints due to the
current state of the mechanism. Graphically, this process would correspond to replacing
each noised node that is a parent of multiple purview nodes (for the effect repertoire) or
mechanism nodes (for the cause repertoire) with multiple, independent “virtual nodes”
(as in [3, Supplementary Methods]). However, the equivalent definition of repertoires in
Eqs. (3) and (5) obviates the need to actually implement virtual nodes in PyPhi.
With the cause_repertoire() method of the Subsystem, we can obtain the cause
repertoire of, for example, mechanism A over the purview ABC depicted in Fig. 4
of [3]:
>>> A, B, C = subsystem.node_indices
>>> print(subsystem.state)
(1, 0, 0)
>>> mechanism = (A,)
>>> purview = (A, B, C)
>>> cr = subsystem.cause_repertoire(mechanism, purview)
>>> print(cr)
[[[ 0.
0.16666667]
[ 0.16666667
0.16666667]]
[[ 0.
0.16666667]
[ 0.16666667
0.16666667]]]
We see that mechanism A in its current state, ON (1), specifies information by ruling
out the previous states in which B and C are OFF (0). That is, the probability that either
(0, 0, 0) or (1, 0, 0) was the previous state, given that A is currently ON, is zero:
>>> print(cr[(0, 0, 0)])
0.0
>>> print(cr[(1, 0, 0)])
0.0
Note that repertoires are returned in multidimensional form, so they can be indexed
with state tuples as above. Repertoires can be reshaped to be 1-dimensional if needed,
e.g. for plotting, but care must be taken that NumPy’s FORTRAN (column-major)
ordering is used so that PyPhi’s little-endian convention for indexing states is respected
(see § 2-dimensional state-by-node form). PyPhi provides the
8/23


## Page 9


pyphi.distribution.flatten() function for this:
>>> flat_cr = pyphi.distribution.flatten(cr)
>>> print(flat_cr)
[ 0.
0.
0.16666667
0.16666667
0.16666667
0.16666667
0.16666667
0.16666667]
2.3.3
Minimum-information partitions (mechanism-level integration)
Having assessed the information of a mechanism over a purview, the next step is to
assess its integrated information (denoted ϕ) by quantifying the extent to which the
cause and effect repertoires of the mechanism-purview pair can be reduced to the
repertoires of its parts.
In terms of graphical operations, the irreducibility of a mechanism-purview pair is
tested by partitioning it into parts and cutting the connections between them. By
applying the perturbation/observation procedure after cutting the connections we
obtain a partitioned repertoire. Since the partition renders the parts independent, in
terms of TPM manipulations, the partitioned repertoire can be calculated as the product
of the individual repertoires for each of the parts. If the partitioned repertoire is no
different than the original unpartitioned repertoire, then the mechanism as a whole did
not specify integrated information about the purview. By contrast, if a repertoire cannot
be factored in this way, then some of its selectivity is due to the causal influence of the
mechanism as an integrated whole on the purview, and the repertoire is said to be
irreducible.
The amount of irreducibility of a mechanism over a purview with respect to a
partition is quantified as the distance between the unpartitioned repertoire and the
partitioned repertoire (calculated with pyphi.distance.repertoire_distance()).
There are many ways to divide the mechanism and purview into parts, so the
irreducibility is measured for every partition and the partition that yields the minimum
irreducibility is called the minimum-information partition (MIP). The integrated
information (ϕ) of a mechanism-purview pair is the distance between the unpartitioned
repertoire and the partitioned repertoire associated with the MIP. PyPhi supports several
distance measures and partitioning schemes (see § Configuration).
The MIP search procedure is implemented by the Subsystem.cause_mip() and
Subsystem.effect_mip() methods. Each returns a
RepertoireIrreducibilityAnalysis object that contains the MIP, as well as the ϕ
value, mechanism, purview, temporal direction (cause or effect), unpartitioned
repertoire, and partitioned repertoire. For example, we compute the effect MIP of
9/23


## Page 10


mechanism ABC over purview ABC from Fig. 6 of [3] as follows:
>>> mechanism = (A, B, C)
>>> purview = (A, B, C)
>>> mip = subsystem.effect_mip(mechanism, purview)
>>> print(mip)
Repertoire irreducibility analysis
ϕ = 1/4
Mechanism: [A, B, C]
Purview = [A, B, C]
Direction: EFFECT
Partition:
∅
A,B,C
--- × -----
B
A,C
Repertoire:
+--------------+
|
S
P(S)
|
| ------------ |
| 000
0
|
| 100
0
|
| 010
0
|
| 110
0
|
| 001
1
|
| 101
0
|
| 011
0
|
| 111
0
|
+--------------+
Partitioned repertoire:
+--------------+
|
S
P(S)
|
| ------------ |
| 000
0
|
| 100
0
|
| 010
0
|
| 110
0
|
| 001
3/4
|
| 101
0
|
| 011
1/4
|
| 111
0
|
+--------------+
Here we can see that the MIP attempts to factor the repertoire of ABC over ABC
into the product of the repertoire of ABC over AC and the repertoire of the empty
mechanism ∅over B. However, the repertoire cannot be factored in this way without
information loss; the distance between the unpartitioned and partitioned repertoire is
nonzero (ϕ = 1
4). Thus mechanism ABC over the purview ABC is irreducible.
2.3.4
Maximally-irreducible cause-effect repertoires (mechanism-level
exclusion)
Next, we apply IIT’s postulate of exclusion at the mechanism level by finding the
maximally-irreducible cause (MIC) and maximally irreducible effect (MIE) specified by a
mechanism. This is done by searching over all possible purviews for the
RepertoireIrreducibilityAnalysis object with the maximal ϕ value. The
Subsystem.mic() and Subsystem.mie() methods implement this search procedure; they
10/23


## Page 11


return a MaximallyIrreducibleCause and a MaximallyIrreducibleEffect object,
respectively. The MIC of mechanism BC, for example, is the purview AB (Fig. 8 of [3]).
This is computed like so:
>>> mechanism = (B, C)
>>> mic = subsystem.mic(mechanism)
>>> print(mic)
Maximally-irreducible cause
ϕ = 1/3
Mechanism: [B, C]
Purview = [A, B]
Direction: CAUSE
MIP:
B
C
--- × ---
∅
A,B
Repertoire:
+-------------+
| S
P(S)
|
| ----------- |
| 00
2/3
|
| 10
0
|
| 01
0
|
| 11
1/3
|
+-------------+
Partitioned repertoire:
+-------------+
| S
P(S)
|
| ----------- |
| 00
1/2
|
| 10
0
|
| 01
0
|
| 11
1/2
|
+-------------+
2.3.5
Concepts
If the mechanism’s MIC has ϕcause > 0 and its MIE has ϕeffect > 0, then the mechanism
is said to specify a concept. The ϕ value of the concept as a whole is the minimum of
ϕcause and ϕeffect.
We can compute the concept depicted in Fig. 9 of [3] using the Subsystem.concept()
method, which takes a mechanism and returns a Concept object containing the ϕ value,
11/23


## Page 12


the MIC (in the ‘cause’ attribute), and the MIE (in the ‘effect’ attribute):
>>> mechanism = (A,)
>>> concept = subsystem.concept(mechanism)
>>> print(concept)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Concept: Mechanism = [A], ϕ = 1/6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MIC
MIE
+--------------------------++--------------------------+
|
ϕ = 1/6
||
ϕ = 1/4
|
|
Purview = [B, C]
||
Purview = [B]
|
|
MIP:
||
MIP:
|
|
∅
A
||
∅
A
|
|
--- × ---
||
--- × ---
|
|
B
C
||
B
∅
|
|
Repertoire:
||
Repertoire:
|
|
+-------------+
||
+------------+
|
|
| S
P(S)
|
||
| S
P(S)
|
|
|
| ----------- |
||
| ---------- |
|
|
| 00
0
|
||
| 0
1/2
|
|
|
| 10
1/3
|
||
| 1
1/2
|
|
|
| 01
1/3
|
||
+------------+
|
|
| 11
1/3
|
||
Partitioned repertoire: |
|
+-------------+
||
+------------+
|
|
Partitioned repertoire: ||
| S
P(S)
|
|
|
+-------------+
||
| ---------- |
|
|
| S
P(S)
|
||
| 0
3/4
|
|
|
| ----------- |
||
| 1
1/4
|
|
|
| 00
1/6
|
||
+------------+
|
|
| 10
1/6
|
|+--------------------------+
|
| 01
1/3
|
|
|
| 11
1/3
|
|
|
+-------------+
|
+--------------------------+
Note that in PyPhi, the repertoires are distributions over purview states, rather than
system states. Occasionally it is more convenient to represent repertoires as distributions
over the entire system. This can be done with the expand_cause_repertoire() and
expand_effect_repertoire() methods of the Concept object, which assume the
unconstrained (maximum-entropy) distribution over the states of non-purview nodes:
>>> full_cr = concept.expand_cause_repertoire()
>>> print(pyphi.distribution.flatten(full_cr))
[ 0.
0.
0.16666667
0.16666667
0.16666667
0.16666667
0.16666667
0.16666667]
>>> full_er = concept.expand_effect_repertoire()
>>> print(pyphi.distribution.flatten(full_er))
[ 0.0625
0.1875
0.0625
0.1875
0.0625
0.1875
0.0625
0.1875]
Also note that Subsystem.concept() will return a Concept object when ϕ = 0 even
though these are not concepts, strictly speaking. For convenience, bool(concept)
evaluates to True if ϕ > 0 and False otherwise.
2.3.6
Cause-effect structures (system-level information)
The next step is to compute the CES, the set of all concepts specified by the subsystem.
The CES characterizes all of the causal constraints that are intrinsic to a physical system.
12/23


## Page 13


This is implemented by the pyphi.compute.ces() function, which simply calls
Subsystem.concept() for every mechanism M ∈P(S), where P(S) is the power set of
subsystem nodes. It returns a CauseEffectStructure object containing those Concepts
for which ϕ > 0.
We see that every mechanism in P(S) except for AC specifies a concept, as described
in Fig. 10 of [3]:
>>> ces = pyphi.compute.ces(subsystem)
>>> print(ces.labeled_mechanisms)
(['A'], ['B'], ['C'], ['A', 'B'], ['B', 'C'], ['A', 'B', 'C'])
2.3.7
Irreducible cause-effect structures (system-level integration)
At this point, the irreducibility of the subsystem’s CES is evaluated by applying the
integration postulate at the system level. As with integration at the mechanism level, the
idea is to measure the difference made by each partition and then take the minimal
value as the irreducibility of the subsystem.
We begin by performing a system cut. Graphically, the subsystem is partitioned into
two parts and the edges going from one part to the other are cut, rendering them
causally ineffective. This is implemented as an operation on the TPM as follows: Let
Ecut denote the set of directed edges in the subsystem that are to be cut, where each
edge e ∈Ecut has a source node a and a target node b. For each edge, we modify the
individual TPM of node b (Fig. 2) by marginalizing over the states of a at t. The
resulting TPM specifies the function implemented by b with the causal influence of a
removed. We then combine the modified node TPMs to recover the full TPM of the
partitioned subsystem. Finally, we recalculate the CES of the subsystem with this
modified TPM (the partitioned CES).
The irreducibility of a CES with respect to a partition is the distance between the
unpartitioned and partitioned CESs (calculated with pyphi.compute.ces_distance();
several distances are supported; see § Configuration). This distance is evaluated for
every partition, and the minimum value across all partitions is the subsystem’s
integrated information Φ, which measures the extent to which the CES specified by the
subsystem is irreducible to the CES under the minimal partition.
This procedure is implemented by the pyphi.compute.sia() function, which returns
a SystemIrreducibilityAnalysis object (Fig. 1). We can verify that the Φ value of the
example system in [3] is 1.92 and the minimal partition is that which removes the causal
connections from AB to C:
>>> sia = pyphi.compute.sia(subsystem)
>>> print(sia.phi)
1.916665
>>> print(sia.cut)
Cut [0, 1] --/ /--> [2]
2.3.8
Complexes (system-level exclusion)
The final step in unfolding the CES of the system is to apply the postulate of exclusion at
the system level. We compute the CES of each subset of the network, considered as a
subsystem (that is, fixing the external nodes as background conditions), and find the
CES with maximal Φ, called the maximally-irreducible cause-effect structure (MICS) of
the system. The subsystem giving rise to it is called the major complex; any overlapping
subsets with lower Φ are excluded. Non-overlapping subsets may be further analyzed to
find additional complexes within the system.
13/23


## Page 14


In this example, we find that the whole system ABC is the system’s major complex,
and all proper subsets are excluded:
>>> state = (1, 0, 0)
>>> major_complex = pyphi.compute.major_complex(network, state)
>>> print(major_complex.subsystem)
Subsystem(A, B, C)
Note that since pyphi.compute.major_complex() is a function of the Network, rather
than a particular Subsystem, it is necessary to specify the state in which the system
should be analyzed.
3
Design and implementation
PyPhi was designed to be easy to use in interactive, exploratory research settings while
nonetheless remaining suitable for use in large-scale simulations or as a component in
larger applications. It was also designed to be efficient, given the high computational
complexity of the algorithms in IIT. Here we describe some implementation details and
optimizations used in the software.
3.1
Representation of the TPM and probability distributions
PyPhi supports three different TPM representations: 2-dimensional state-by-node,
multidimensional state-by-node, and state-by-state. The state-by-node form is the
canonical representation in PyPhi, with the 2-dimensional form used for input and
visualization and the multidimensional form used for internal computation. The
state-by-state representation is given as an input option for those accustomed to this
more general form. If the TPM is given in state-by-state form, PyPhi will raise an error if
it does not satisfy Eq. (1) (conditional independence).
3.1.1
2-dimensional state-by-node form
A TPM in state-by-node form is a matrix where the entry (i, j) gives the probability that
the jth node will be ON at t + 1 if the system is in the ith state at t. This representation
has the advantage of being more compact than the state-by-state form, with 2n×n
entries instead of 2n×2n, where n is the number of nodes. Note that the TPM admits
this representation because in PyPhi the nodes are binary; both Pr(Nt+1 = ON) and
Pr(Nt+1 = OFF) can be specified by a single entry, in our case Pr(Nt+1 = ON), since
the two probabilities must sum to 1.
Because the possible system states at t are represented implicitly as row indices in
2-dimensional TPMs, there must be an implicit mapping from states to indices. In PyPhi
this mapping is achieved by listing the state tuples in lexicographical order and then
interpreting them as binary numbers where the state of the first node corresponds to the
least-significant bit, so that e.g. the state (0, 0, 0, 1) is mapped to the row with index
8 (the ninth row, since Python uses zero-based indexing [18]). Designating the first
node’s state as the least-significant bit is analogous to choosing the little-endian
convention in organizing computer memory. This convention is preferable because the
mapping is stable under the inclusion of new nodes: including another node in a
subsystem only requires concatenating new rows and a new column to its TPM rather
than interleaving them. Note that this is opposite convention to that used in writing
numbers in positional notation; care must be taken when converting between states and
indices and between different TPM representations (the pyphi.convert module
provides convenience functions for these purposes).
14/23


## Page 15


3.1.2
Multidimensional state-by-node form
When a state-by-state TPM is provided to PyPhi by the user, it is converted to
state-by-node form and the conditional independence property (Eq. (1)) is checked.
Note that any TPM in state-by-node form necessarily satisfies Eq. (1). For internal
computations, the TPM is then reshaped so that it has n + 1 dimensions rather than two:
the first n dimensions correspond to the states of each of the n nodes at t, while the last
dimension corresponds to the probabilities of each node being ON at t + 1. In other
words, the indices of the rows (current states) in the 2-dimensional TPM are “unraveled”
into n dimensions, with the ith dimension indexed by the ith bit of the 2-dimensional
row index according to the little-endian convention. Because the TPM is stored in a
NumPy array, this multidimensional form allows us to take advantage of NumPy
indexing [19] and use a state tuple as an index directly, without converting it to an
integer index:
>>> state = (0, 1, 1)
>>> print(tpm[state])
[ 1.
0.25
0.75]
The first entry of this array signifies that if the state of the system is (0, 1, 1) at t,
then the probability of the first node N0 being ON at t + 1 is Pr(N0, t+1 = ON) = 1.
Similarly, the second entry means Pr(N1, t+1 = ON) = 0.25 and the third entry means
Pr(N2, t+1 = ON) = 0.75.
Most importantly, the multidimensional representation simplifies the calculation of
marginal and conditional distributions and cause/effect repertoires, because it allows
efficient “broadcasting” [19] of probabilities when multiplying distributions. Specifically,
the Python multiplication operator ‘*’ acts as the tensor product when the operands are
NumPy arrays A and B of equal dimensionality such that for each dimension d, either
A.shape[d] == 1 or B.shape[d] == 1.
3.2
Calculation of cause/effect repertoires from the TPM
The cause and effect repertoires of a mechanism over a purview describe how the
mechanism nodes in a particular state at t constrain the possible states of the purview
nodes at t −1 and t + 1, respectively. Here we describe how they are derived from the
TPM in PyPhi.
3.2.1
The effect repertoire
We begin with the simplest case: calculating the effect repertoire of a mechanism M ⊆S
over a purview consisting of a single element Pi ∈S. This is defined as a conditional
probability distribution over states of the purview element at t + 1 given the current
state of the mechanism,
effect_repertoire(M, Pi) := Pr(Pi,t+1 | Mt = mt).
(2)
It is derived from the TPM by conditioning on the state of the mechanism elements,
marginalizing over the states of non-purview elements P ′ = S \ Pi (these states
correspond to columns in the state-by-state TPM), and marginalizing over the states of
non-mechanism elements M ′ = S \ M (these correspond to rows):
Pr(Pi,t+1 | Mt = mt) =
1
|ΩM ′|
X
m′
t ∈ΩM′
1
|ΩP ′|
X
p′
t+1 ∈ΩP ′
Pr(Pi,t+1, p′
t+1 | M = mt, M ′ = m′
t).
15/23


## Page 16


This operation is implemented in PyPhi by several subroutines. First, in a
pre-processing step performed when the Subsystem object is created, a Node object is
created for each element in the subsystem. Each Node contains its own individual TPM,
extracted from the subsystem’s TPM; this is a 2s×2 matrix where s is the number of the
node’s parents and the entry (i, j) gives the probability that the node is in state j (0 or 1)
at t + 1 given that its parents are in state i at t. This node TPM is represented internally
in multidimensional state-by-node form as usual, with singleton dimensions for those
subsystem elements that are not parents of the node. The effect repertoire is then
calculated by conditioning the purview node’s TPM on the state of the mechanism nodes
that are also parents of the purview node, via the pyphi.tpm.condition_tpm() function,
and marginalizing out non-mechanism nodes, with pyphi.tpm.marginalize_out().
In cases where there are mechanism nodes that are not parents of the purview node,
the resulting array is multiplied by an array of ones that has the desired shape
(dimensions of size two for each mechanism node, and singleton dimensions for each
non-mechanism node). Because of NumPy’s broadcasting feature, this step is equivalent
to taking the tensor product of the array with the maximum-entropy distribution over
mechanism nodes that are not parents, so that the final result is a distribution over all
mechanism nodes, as desired.
The effect repertoire over a purview of more than one element is given by the tensor
product of the effect repertories over each individual purview element,
effect_repertoire(M, P) :=
O
Pi ∈P
effect_repertoire(M, Pi).
(3)
Again, because PyPhi TPMs and repertoires are represented as tensors
(multidimensional arrays), with each dimension corresponding to a node, the NumPy
multiplication operator between distributions over different nodes is equivalent to the
tensor product. Thus the effect repertoire over an arbitrary purview is trivially
implemented by taking the product of the effect repertoires over each purview node
with numpy.multiply().
3.2.2
The cause repertoire
The cause repertoire of a single-element mechanism Mi ∈S over a purview P ⊆S is
defined as a conditional probability distribution over the states of the purview at t −1
given the current state of the mechanism,
cause_repertoire(Mi, P) := Pr(Pt−1 | Mi,t = mi,t).
(4)
As with the effect repertoire, it is obtained by conditioning and marginalizing the TPM.
However, because the TPM gives conditional probabilities of states at t + 1 given the
state at t, Bayes’ rule is first applied to express the cause repertoire in terms of a
conditional distribution over states at t −1 given the state at t,
Pr(Pt−1 | Mi,t = mi,t) = Pr(mi,t | Pt−1) Pr(Pt−1)
Pr(mi,t)
.
where the marginal distribution Pr(Pt−1) over previous states is the uniform
distribution. In this way, the analysis captures how a mechanism in a state constrains a
purview without being biased by whether certain states arise more frequently than
others in the dynamical evolution of the system [3,4,11,16]. Then the cause repertoire
can be calculated by marginalizing over the states of non-mechanism elements
M ′ = S \ Mi (now corresponding to columns in the state-by-state TPM) and
16/23


## Page 17


non-purview elements P ′ = S \ P (now corresponding to rows),
Pr(mi,t | Pt−1) Pr(Pt−1)
Pr(mi,t)
=


1
|ΩP ′|
X
p′
t−1 ∈ΩP ′
1
|ΩM ′|
X
m′
t ∈ΩM′
Pr(mi,t, m′
t | Pt−1, P ′
t−1 = p′
t−1)

Pr(Pt−1)
1
|ΩM ′|
X
m′
t ∈ΩM′
Pr(mi,t, m′
t)
=


1
|ΩP ′|
X
p′
t−1 ∈ΩP ′
X
m′
t ∈ΩM′
Pr(mt, m′
t | Pt−1, P ′
t−1 = p′
t−1)

Pr(Pt−1)
X
m′
t ∈ΩM′
Pr(mi,t, m′
t)
.
In PyPhi, the “backward” conditional probabilities Pr(mi,t | Pt−1) for a single
mechanism node are obtained by indexing into the last dimension of the node’s TPM
with the state mi,t and then marginalizing out non-purview nodes via
pyphi.tpm.marginalize_out(). As with the effect repertoire, the resulting array is then
multiplied by an array of ones with the desired shape in order to obtain a distribution
over the entire purview. Finally, because in this case the probabilities were obtained
from columns of the TPM, which do not necessarily sum to 1, the distribution is
normalized with pyphi.distribution.normalize().
The cause repertoire of a mechanism with multiple elements is the normalized tensor
product of the cause repertoires of each individual mechanism element,
cause_repertoire(M, P) =
1
K
O
Mi ∈M
cause_repertoire(Mi, P),
(5)
where
K =
X
pt−1 ∈ΩP
Y
mi,t ∈ΩM
Pr(Pt−1 = pt−1 | Mi,t = mi,t)
is a normalization factor that ensures that the distribution sums to 1. This is
implemented in PyPhi via numpy.multiply() and pyphi.distribution.normalize().
For a more complete illustration of these procedures, see S1 Calculating Φ.
3.3
Code organization and interface design
The postulates of IIT induce a natural hierarchy of computations [1, Supplementary
Information S2], and PyPhi’s implementation mirrors this hierarchy by using
object-oriented programming (Table 1) and factoring the computations into
compositions of separate functions where possible. One advantage of this approach is
that each level of the computation can be performed independently of the higher levels;
for example, if one were interested only in the MIE of certain mechanisms rather than
the full MICS, then one could simply call Subsystem.effect_mip() on those
mechanisms instead of calling pyphi.compute.sia() and extracting them from the
resulting SystemIrreducibilityAnalysis object (this is especially important in the case
of large systems where the full calculation is infeasible). Separating the calculation into
many subroutines and exposing them to the user also has the advantage that they can be
easily composed to implement functionality that is not already built-in.
17/23


## Page 18


Table 1. Correspondence between theoretical objects and PyPhi objects.
Theoretical object
PyPhi object
Discrete dynamical system
Network
Candidate system
Subsystem
System element
Node in Subsystem.nodes
System state
Python tuple containing a 0 or 1 for each node
Mechanism
Python tuple of node indices
Purview
Python tuple of node indices
Repertoire over a purview P
NumPy array with |P| dimensions, each of size 2
MIP
The partition attribute of the
RepertoireIrreducibilityAnalysis returned by
Subsystem.cause_mip() or
Subsystem.effect_mip()
MIC and MIE
MaximallyIrreducibleCause and
MaximallyIrreducibleEffect
Concept
Concept
ϕ
The phi attribute of a Concept
CES
CauseEffectStructure
Φ
The phi attribute of a CauseEffectStructure
MICS
The ces attribute of the
SystemIrreducibilityAnalysis returned by
pyphi.compute.major_complex()
Complex
The subsystem attribute of the
SystemIrreducibilityAnalysis returned by
pyphi.compute.major_complex()
3.4
Configuration
Many aspects of PyPhi’s behavior may be configured via the pyphi.config object. The
configuration can be specified in a YAML file [20]; an example is available in the GitHub
repository. When PyPhi is imported, it checks the current directory for a file named
pyphi_config.yml and automatically loads it if it exists. Configuration settings can also
be loaded on the fly from an arbitrary file with the pyphi.config.load_config_file()
function.
Alternatively, pyphi.config.load_config_dict() can load configuration settings
from a Python dictionary. Many settings can also be changed by directly assigning them
a new value.
Default settings are used if no configuration is provided. A full description of the
available settings and their default values is available in the “Configuration” section of
the online documentation.
18/23


## Page 19


3.5
Optimizations and approximations
Here we describe various optimizations and approximations used by the software to
reduce the complexity of the calculations (see § Limitations). Memoization and caching
optimizations are described in S2 Appendix.
3.5.1
Connectivity optimizations
As mentioned in § Input, providing connectivity information explicitly with a CM can
greatly reduce the time complexity of the computations, because in certain cases missing
connections imply reducibility a priori.
For example, at the system level, if the subsystem is not strongly connected then Φ is
necessarily zero. This is because a unidirectional cut between one system part and the
rest can always be found that will not actually remove any edges, so the CESs with and
without the cut will be identical (see S3 Appendix for proof). Accordingly, PyPhi
immediately excludes these subsystems when finding the major complex of a system.
Similarly, at the mechanism level, PyPhi uses the CM to exclude certain purviews
from consideration when computing a MIC or MIE by efficiently determining that
repertoires over those purviews are reducible without needing to explicitly compute
them. Suppose there are two sets of nodes X and Y for which there exist partitions
X = (X1, X2) and Y = (Y1, Y2) such that there are no edges from X1 to Y2 and no
edges from X2 to Y1. Then the effect repertoire of mechanism X over purview Y can be
factored as
effect_repertoire(X, Y ) =
effect_repertoire(X1, Y1) ⊗effect_repertoire(X2, Y2),
and the cause repertoire of mechanism Y over purview X can be factored as
cause_repertoire(Y, X) =
cause_repertoire(Y1, X1) ⊗cause_repertoire(Y2, X2).
Thus in these cases the mechanism is reducible for that purview and ϕ = 0 (see
S4 Appendix for proof).
3.5.2
Analytical solution to the earth mover’s distance
One of the repertoire distances available in PyPhi is the earth mover’s distance (EMD),
with the Hamming distance as the ground metric. Computing the EMD between
repertoires is a costly operation, with time complexity O(n23n) where n is the number of
nodes in the purview [21]. However, when comparing effect repertoires, PyPhi exploits
a theorem that states that the EMD between two distributions p and q over multiple
nodes is the sum of the EMDs between the marginal distributions over each individual
node, if p and q are independent. This analytical solution has time complexity O(n), a
significant improvement over the general EMD algorithm (note that this estimate does
not include the cost of computing the marginals, which already have been computed to
obtain the repertoires). By the conditional independence property (Eq. 1), the
conditions of the theorem hold for EMD calculations between effect repertoires, and
thus the analytical solution can be used for half of all repertoire calculations performed
in the analysis. The theorem is formally stated and proved in S5 Appendix.
3.5.3
Approximations
Currently, two approximate methods of computing Φ are available. These can be used
via settings in the PyPhi configuration file (they are disabled by default):
19/23


## Page 20


1. pyphi.config.CUT_ONE_APPROXIMATION (the “cut one” approximation), and
2. pyphi.config.ASSUME_CUTS_CANNOT_CREATE_NEW_CONCEPTS (the “no new
concepts” approximation).
In both cases, the complexity of the calculation is greatly reduced by replacing the
optimal partitioned CES by an approximate solution. The system’s Φ value is then
computed as usual as the difference between the unpartitioned CES and the
approximate partitioned CES.
Cut one.
The “cut one” approximation reduces the scope of the search for the MIP
over possible system cuts. Instead of evaluating the partitioned CES for each of the 2n
unidirectional bipartitions of the system, only those 2n bipartitions are evaluated that
sever the edges from a single node to the rest of the network or vice versa. Since the
goal is to find the minimal Φ value across all possible partitions, the “cut one”
approximation provides an upper bound on the exact Φ value of the system.
No new concepts.
For most choices of mechanism partitioning schemes and distance
measures, it is possible that the CES of the partitioned system contains concepts that are
reducible in the unpartitioned system and thus not part of the unpartitioned CES. For
this reason, PyPhi by default computes the partitioned CES from scratch from the
partitioned TPM. Under the “no new concepts” approximation, such new concepts are
ignored. Instead of repeating the entire CES computation for each system partition,
which requires reevaluating all possible candidate mechanisms for irreducibility, only
those mechanisms are taken into account that already specify concepts in the
unpartitioned CES. In many types of systems, new concepts due to the partition are rare.
Approximations using the “no new concepts” option are thus often accurate. Note,
however, that this approximation provides neither a theoretical upper nor lower bound
on the exact Φ value of the system.
Limitations
PyPhi’s main limitation is that the algorithm is exponential time in the number of nodes,
O(n53n). This is because the number of states, subsystems, mechanisms, purviews, and
partitions that must be considered each grows exponentially in the size of the system.
This limits the size of systems that can be practically analyzed to ~10–12 nodes. For
example, calculating the major complex of systems of three, five, and seven stochastic
majority gates, connected in a circular chain of bidirectional edges, takes ~1 s, ~16 s,
and ~2.75 h respectively (parallel evaluation of system cuts, 32 × 3.1GHz CPU cores).
Using the “cut one” approximation, these calculations take ~1 s, ~12 s, and ~0.63 h. In
practice, actual execution times are substantially variable and depend on the specific
network under analysis, because network structure determines the effectiveness of the
optimizations discussed above.
Another limitation is that the analysis can only be meaningfully applied to a system
that is Markovian and satisfies the conditional independence property. These are
reasonable assumptions for the intended use case of the software: analyzing a causal
TPM derived using the calculus of perturbations [17]. However, there is no guarantee
that these assumptions will be valid in other circumstances, such as TPMs derived from
observed time series (e.g., EEG recordings). Whether a system has the Markov property
and conditional independence property should be carefully checked before applying the
software in novel contexts.
20/23


## Page 21


4
Availability and future directions
PyPhi can be installed with Python’s package manager via the command
‘pip install pyphi’ on Linux and macOS systems equipped with Python 3.4 or higher.
It is open-source and licensed under the GNU General Public License v3.0. The source
code is version-controlled with git and hosted in a public repository on GitHub at
https://github.com/wmayner/pyphi. Comprehensive and continually-updated
documentation is available online at https://pyphi.readthedocs.io. The pyphi-users
mailing list can be joined at https://groups.google.com/forum/#!forum/pyphi-users. A
web-based graphical interface to the software is available at
http://integratedinformationtheory.org/calculate.html.
Several additional features are in development and will be released in future
versions. These include a module for calculating Φ over multiple spatial and temporal
scales, as theoretically required by the exclusion postulate (in the current version, the
Network is assumed to represent the system at the spatiotemporal timescale at which Φ
is maximized [10,12]), and a module implementing a calculus for “actual causation” as
formulated in [15] (preliminary versions of these modules are available in the current
release). The software will also be updated to reflect developments in IIT and further
optimizations in the algorithm.
5
Acknowledgments
We thank Andrew Haun, Leonardo Barbosa, Sabrina Streipert, and Erik Hoel for their
valuable feedback as early users of the software.
WGPM, WM, LA, RM and GT received funding from the Templeton World Charities
Foundbtion (Grant #TWCF 0067/AB41). WGPM and GF were also supported by
National Research Service Award (NRSA) T32 GM007507.
6
References
1. Tononi G, Boly M, Massimini M, Koch C. Integrated information theory: from
consciousness to its physical substrate. Nature Reviews Neuroscience.
2016;17(7):450–461. doi:10.1038/nrn.2016.44.
2. Tononi G. Integrated information theory. Scholarpedia. 2015;10(1):4164.
doi:10.4249/scholarpedia.4164.
3. Oizumi M, Albantakis L, Tononi G. From the Phenomenology to the Mechanisms
of Consciousness: Integrated Information Theory 3.0. PLoS computational
biology. 2014;10(5):e1003588. doi:10.1371/journal.pcbi.1003588.
4. Balduzzi D, Tononi G. Integrated information in discrete dynamical systems:
motivation and theoretical framework. PLoS computational biology.
2008;4(6):e1000091. doi:10.1371/journal.pcbi.1000091.
5. Tononi G. An information integration theory of consciousness. BMC neuroscience.
2004;5(1):42. doi:10.1186/1471-2202-5-42.
6. Albantakis L, Tononi G. The Intrinsic Cause-Effect Power of Discrete Dynamical
Systems—From Elementary Cellular Automata to Adapting Animats. Entropy.
2015;17(8):5472. doi:10.3390/e17085472.
21/23


## Page 22


7. Albantakis L, Hintze A, Koch C, Adami C, Tononi G. Evolution of Integrated
Causal Structures in Animats Exposed to Environments of Increasing Complexity.
PLoS computational biology. 2014;10(12):e1003966.
doi:10.1371/journal.pcbi.1003966.
8. Oizumi M, Tsuchiya N, Amari S. Unified framework for information integration
based on information geometry. Proceedings of the National Academy of Sciences.
2016;113(51):14817–14822. doi:10.1073/pnas.1603583113.
9. Albantakis L, Tononi G. Chapter 14: Automata and Animats. From Matter to Life:
Information and Causality. 2017; p. 334. doi:10.1017/9781316584200.014.
10. Hoel EP, Albantakis L, Marshall W, Tononi G. Can the macro beat the micro?
Integrated information across spatiotemporal scales. Neuroscience of
Consciousness. 2016;2016(1):niw012. doi:10.1093/nc/niw012.
11. Hoel EP, Albantakis L, Tononi G. Quantifying causal emergence shows that macro
can beat micro. Proceedings of the National Academy of Sciences.
2013;110(49):19790–19795. doi:10.1073/pnas.1314922110.
12. Marshall W, Albantakis L, Tononi G. Black-boxing and cause-effect power. PLoS
computational biology. 2018;14(4):e1006114.
doi:10.1371/journal.pcbi.1006114.
13. Marshall W, Kim H, Walker SI, Tononi G, Albantakis L. How causal analysis can
reveal autonomy in models of biological systems. Philosophical Transactions of
the Royal Society of London A: Mathematical, Physical and Engineering Sciences.
2017;375(2109). doi:10.1098/rsta.2016.0358.
14. Marshall W, Gomez-Ramirez J, Tononi G. Integrated Information and State
Differentiation. Frontiers in Psychology. 2016;7:926.
doi:10.3389/fpsyg.2016.00926.
15. Albantakis L, Marshall W, Tononi G. What caused what? An irreducible account
of actual causation. arXiv:1708.06716 [cs.AI]. 2017.
16. Ay N, Polani D. Information flows in causal networks. Advances in complex
systems. 2008;11(01):17–41. doi:10.1142/S0219525908001465.
17. Pearl J. Causality. Cambridge university press; 2009.
18. Dijkstra EW. Why numbering should start at zero (EWD 831); 1982. Available
from: https:
//www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html.
19. Walt Svd, Colbert SC, Varoquaux G. The NumPy array: a structure for efficient
numerical computation. Computing in Science & Engineering. 2011;13(2):22–30.
doi:10.1109/MCSE.2011.37.
20. Ben-Kiki O, Evans C, Net Id. YAML specification; 2009. Available from:
http://yaml.org/spec/.
21. Pele O, Werman M. Fast and robust earth mover’s distances. In: 2009 IEEE 12th
International Conference on Computer Vision. IEEE; 2009. p. 460–467.
doi:10.1109/ICCV.2009.5459199.
22/23


## Page 23


7
Supporting information
S1 Calculating Φ.
Illustration of the algorithm.
S2 Appendix.
Memoization and caching optimizations.
S3 Appendix.
Proof of the strong connectivity optimization.
S4 Appendix.
Proof of the block-factorable optimization.
S5 Appendix.
Proof of an analytical solution to the EMD between effect
repertoires.
23/23


## Page 24


S2 Appendix
Memoization and caching optimizations.
During the course of computing a SystemIrreducibilityAnalysis, several functions in
PyPhi are called multiple times with the same input. For example, calculating
cause_repertoire((A,B), (A,B,C) and cause_repertoire((A,C), (A,B,C)) both
require calculating cause_repertoire((A,), (A,B,C)). Similarly,
cause_repertoire((A,), (B,C)) is both the unpartitioned repertoire of the candidate
MIP of mechanism A over purview BC and the first term in the expression for the
partitioned repertoire of the candidate MIP of mechanism AB over purview ABC under
the partition
A
BC × B
A.
In such situations, a natural optimization technique to reduce expensive re-computation
of these functions is memoization: when a function is computed for a given input, the
input-output pair is stored in a lookup table; if the function is called again with that
input, the output is simply looked up in the table and returned, without computing the
function again.
In PyPhi, memoization is applied to various functions at different levels of the
algorithm, listed here:
• Subsystem._single_node_cause_repertoire() and
Subsystem._single_node_effect_repertoire(), the un-normalized cause
repertoire of a single-node mechanism and the effect repertoire over a single-node
purview, respectively (note that these functions are meant to be called internally by
other PyPhi functions and not by the user, as indicated by the leading underscore);
• Subsystem.cause_repertoire() and Subsystem.effect_repertoire(), the cause
and effect repertoires of arbitrary mechanism-purview pairs;
• Subsystem.mic() and Subsystem.mie(), the MIC and MIE of a mechanism;
• Network.potential_purviews(), the purviews which are not necessarily reducible
based on the CM;
• Various utility functions such as
pyphi.distribution.max_entropy_distribution(); and
• pyphi.compute.sia(), the full IIT analysis of a Subsystem.
At the highest level, pyphi.compute.sia() is memoized such that the
SystemIrreducibilityAnalysis object is stored persistently on the filesystem, rather
than in memory, in a directory named __pyphi_cache__ (which is automatically created
in the directory where the Python session was started). This means that the
SystemIrreducibilityAnalysis objects are automatically saved across Python sessions
and can be quickly retrieved simply by running the same code, which is useful for
interactive, exploratory work. This behavior can be controlled with the
pyphi.config.CACHE_SIAS configuration setting. Note, however, that this feature is
primarily for convenience and is not intended to replace explicit data management.
Additionally, care must be taken to erase or disable the cache when upgrading to new
versions of PyPhi, as changes to the algorithm may invalidate previously computed
output. A final caveat: because the results are stored on the filesystem, they can
accumulate and occupy a large amount of disk space if the __pyphi_cache__ directory is
not periodically removed.
1/1


## Page 25


S3 Appendix
Proof of the strong connectivity optimization.
Theorem (strong connectivity). If G = (V, E) is a directed graph that is not strongly
connected, then Φ(G) = 0.
Proof. Since G is not strongly connected, G contains n ≥2 strongly connected
components, which we arbitrarily label
G1, G2, . . . , Gn = (V1, E1), (V2, E2), . . . , (Vn, En).
Let Ej,k denote the set of directed edges from nodes in component Gj to those in
component Gk, {(a, b) ∈E | a ∈Vj and b ∈Vk}.
Consider the first component G1. For every other component Gi, i ̸= 1, either
E1,i = ∅or Ei,1 = ∅, because otherwise G1 and Gi would not be distinct connected
components. Now let G1 be the indices of components that receive no edges from G1,
{i ∈1, . . . , n | E1,i = ∅}. Then let Y be the union of the nodes in these components,
Y =
[
i ∈G1
Vi ,
and let X = V \ Y . Then X and Y form a partition of V such that there are no edges
from any nodes in X to any nodes in Y .
Now consider the system cut c(X, Y ) that cuts edges from nodes in X to nodes in Y .
Because there are no such edges, none of the node TPMs are changed after applying the
cut, and thus the subsystem TPM is unchanged because it is the product of the node
TPMs. Since the cause-effect structure of a system is a function of the subsystem’s TPM,
the cause-effect structure Cc(X,Y ) of the partitioned subsystem and the cause-effect
structure C of the unpartitioned subsystem are identical.
Let Φc(X,Y )(G) be the Φ value of G with respect to c(X, Y ). By definition, this is the
ces_distance between C and Cc(X,Y ). The ces_distance function is a metric, so since
Cc(X,Y ) = C we have that
ces_distance(C, Cc(X,Y )) = 0
by non-negativity of metrics, and thus Φc(X,Y )(G) = 0. Now, by definition,
Φ(G) = min
c ∈C Φc(G)
where C is the set of all system cuts. Since Φc(X,Y )(G) = 0, by non-negativity we have
Φ(G) = 0.
■
1/1


## Page 26


S4 Appendix
Proof of the block-factorable optimization.
Definition (block diagonal). An n×m matrix An,m is said to be block diagonal if it can
be written as
An,m =
Bs,t
0s,m−t
0n−s,t
Cn−s,m−t

,
where 1 ≤s < n and 1 ≤t < m.
We consider sub-matrices of the connectivity matrix CM of the form CM(πrow, πcol),
where
[CM(πrow, πcol)]i,j = [CM]πrow(i),πcol(j).
Definition (block factorable). A mechanism-purview pair (M, P) is said to be block
factorable if there exists a permutation πM of the mechanism indices and a permutation πP
of the purview indices such that CM(πM, πP ) is block diagonal (for effect purviews) or
CM(πP , πM) is block diagonal (for cause purviews).
Theorem (block reducibility). If a mechanism-purview pair is block factorable, then it is
reducible (ϕ = 0).
Proof. Consider a mechanism M constituted of n elements and a purview P constituted
of m elements. Assume without loss of generality that P is an effect purview. Since
(M, P) is block factorable, there exist permutations πM and πP such that CM(πM, πP ) is
block diagonal, i.e.,
CM(πM, πP ) =
Bs,t
0s,m−t
0n−s,t
Cn−s,m−t

,
where 1 ≤s < n and 1 ≤t < m.
We define a mechanism-purview partition
c := M1
P1
× M2
P2
that cuts edges from M1 to P2 and from M2 to P1, where
M1 = { πM(i) |
1 ≤i < s + 1 }
M2 = { πM(i) | s + 1 ≤i < n + 1 }
P1 = { πP (i) |
1 ≤i < t + 1 }
P2 = { πP (i) | t + 1 ≤i < m + 1 }
Note that [CM(πM, πP )]i,j = 0 if either i ∈M1 and j ∈P2 or i ∈M2 and j ∈P1. Thus
there are no edges cut by c, and it leaves the subsystem’s TPM unchanged. Since the
effect repertoire of a mechanism-purview combination is a function of the subsystem’s
TPM, the unpartitioned effect repertoire, ER(M, P) and the partitioned repertoire
ERc(M, P) are identical.
By definition, ϕc(M, P) is the distance between ER(M, P) and ERc(M, P), so
ϕc(M, P) = 0. Now, by definition,
ϕ(M, P) = min
p ∈P ϕp(M, P),
where P is the set of all partitions of (M, P). Since ϕc(M, P) = 0, by the non-negativity
of metrics we have ϕ(M, P) = 0.
■
1/1


## Page 27


S5 Appendix
Proof of an analytical solution to the EMD between effect repertoires.
Theorem (analytical EMD). Consider two random variables X1, X2 with corresponding
state spaces Ω1, Ω2 and an ‘additive’ metric D,
D((i1, i2), (j1, j2)) = D(i1, j1) + D(i2, j2)
∀(i1, i2) and (j1, j2) ∈Ω1 × Ω2.
Let p1 and q1 be two probability distributions on X1, and let p2 and q2 be probability
distributions on X2. If X1 and X2 are independent, then the EMD between the joint
distributions p = p1p2 and q = q1q2, with D as the ground metric, is equal to the sum of
the EMDs between the marginal distributions:
EMD(p, q) = EMD(p1, q1) + EMD(p2, q2).
Proof. First, we demonstrate that
EMD(p, q) ≤EMD(p1, q1) + EMD(p2, q2).
To do this, we define a third probability distribution as an intermediate point,
r := q1p2.
We define the following flow from p to r,
fp,r(i1, i2, j1, j2) :=
(
p2(i2)f ∗
p1,q1(i1, j1)
if i2 = j2
0
otherwise,
where f ∗
p1,q1 is the optimal flow for the EMD between p1 and q1. With this flow, we have
EMD(p, r) ≤
X
i1,i2,j1,j2
fp,r(i1, i2, j1, j2)D((i1, i2), (j1, j2))
=
X
i1,i2,j1
p2(i2)f ∗
p1,q1(i1, j1)D(i1, j1)
=
X
i2
p2(i2)
X
i1,j1
f ∗
p1,q1(i1, j1)D(i1, j1)
= EMD(p1, q1)
We next define a flow from r to q,
fr,q(i1, i2, j1, j2) :=
(
q1(i1)f ∗
p2,q2(i2, j2)
if i1 = j1
0
otherwise,
where f ∗
p2,q2 is the optimal flow for the EMD between p2 and q2. With this flow, we have
EMD(r, q) ≤
X
i1,i2,j1,j2
fr,q(i1, i2, j1, j2)D((i1, i2), (j1, j2))
=
X
i1,i2,j2
q1(i1)f ∗
p2,q2(i2, j2)D(i2, j2)
=
X
i1
q1(i1)
X
i2,j2
f ∗
p2,q2(i2, j2)D(i2, j2)
= EMD(p2, q2)
1/3


## Page 28


Then using the triangle inequality (the EMD is a metric), we have
EMD(p, q) ≤EMD(p, r) + EMD(r, q) ≤EMD(p1, q1) + EMD(p2, q2).
To complete the proof, we next demonstrate that
EMD(p, q) ≥EMD(p1, q1) + EMD(p2, q2).
If f ∗
p,q is the optimal flow for EMD(p, q), then define a flow between p1 and q1,
f1(i1, j1) :=
X
i2,j2
f ∗
p,q(i1, i2, j1, j2),
and a flow between p2 and q2
f2(i2, j2) :=
X
i1,j1
f ∗
p,q(i1, i2, j1, j2).
Then using the additive property of the ground metric D,
EMD(p, q) =
X
i1,i2,j1,j2
f ∗
p,q(i1, i2, j1, j2)D((i1, i2), (j1, j2))
=
X
i1,i2,j1,j2
f ∗
p,q(i1, i2, j1, j2)D(i1, j1) +
X
i1,i2,j1,j2
f ∗
p,q(i1, i2, j1, j2)D(i2, j2)
=
X
i1,j1

X
i2,j2
f ∗
p,q(i1, i2, j1, j2)

D(i1, j1)
+
X
i2,j2

X
i1,j1
f ∗
p,q(i1, i2, j1, j2)

D(i2, j2)
=
X
i1,j1
f1(i1, j1)D(i1, j1) +
X
i2,j2
f2(i2, j2)D(i2, j2)
≥EMD(p1, q1) + EMD(p2, q2).
Therefore EMD(p, q) = EMD(p1, q1) + EMD(p2, q2).
■
Perhaps it is worth demonstrating that the flows f1, f2, fp,r and fr,q satisfy the EMD
requirements. Consider fp,r,
fp,r(i1, i2, j1, j2) =
(
p2(i2)f ∗
p1,q1(i1, j1)
if i2 = j2
0
otherwise,
where f ∗
p1,q1 is the optimal flow for the EMD between p1 and q1.
Since p2(i2) ≥0 (probability) and f ∗
p1,q1(i1, j1) ≥0 (definition of optimal flow),
fp,r(i1, i2, j1, j2) ≥0.
Next,
X
j1,j2
fp,r(i1, i2, j1, j2) =
X
j1
p2(i2)f ∗
p1,q1(i1, j1)
= q1(i1)p2(i2)
= r(i1, i2),
2/3


## Page 29


and
X
i1,i2
fp,r(i1, i2, j1, j2) =
X
i1
p2(j2)f ∗
p1,q1(i1, j1)
= q1(j1)p2(i2)
= r(j1, j2).
Finally,
X
i1,i2,j1,j2
fp,r(i1, i2, j1, j2) =
X
i2
p2(i2)
X
i1,j1
f ∗
p1,q1(i1, j1)
=
X
i1,j1
f ∗
p1,q1(i1, j1)
= 1
Thus fp,r satisfies the criteria for a potential flow. The others follow similarly.
3/3

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
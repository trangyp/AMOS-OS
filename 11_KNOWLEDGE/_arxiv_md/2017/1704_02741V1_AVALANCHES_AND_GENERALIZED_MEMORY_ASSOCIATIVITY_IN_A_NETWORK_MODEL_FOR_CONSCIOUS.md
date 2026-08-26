---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1704.02741v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1704.02741v1_Avalanches_and_Generalized_Memory_Associativity_in_a_Network_Model_for_Conscious

> Source: 1704.02741v1_Avalanches_and_Generalized_Memory_Associativity_in_a_Network_Model_for_Conscious.pdf

> Pages: 24

---


## Page 1


arXiv:1704.02741v1  [q-bio.NC]  10 Apr 2017
Avalanches and Generalized Memory Associativity in a Network
Model for Conscious and Unconscious Mental Functioning
Maheen Siddiqui∗
Centre for Brain and Cognitive Development,
Birkbeck College, University of London,
London WC1E 7HX, United Kingdom.
Roseli S. Wedemann, Corresponding Author†
Instituto de Matem´atica e Estat´ıstica,
Universidade do Estado do Rio de Janeiro,
Rua S˜ao Francisco Xavier 524, 20550-013, Rio de Janeiro, Brazil.
Henrik Jensen‡
Centre for Complexity Science and Department of Mathematics,
Imperial College London,
London SW7 2AZ, United Kingdom,
and
Institute of Innovative Research,
Tokyo Institute of Technology,
4259, Nagatsuta-cho,
Yokohama 226-8502, Japan.
(Dated: July 25, 2018)
1


## Page 2


Abstract
We explore statistical characteristics of avalanches associated with the dynamics of a complex-
network model, where two modules corresponding to sensorial and symbolic memories interact,
representing unconscious and conscious mental processes.
The model illustrates Freud’s ideas
regarding the neuroses and that consciousness is related with symbolic and linguistic memory
activity in the brain. It incorporates the Stariolo-Tsallis generalization of the Boltzmann Machine
in order to model memory retrieval and associativity. In the present work, we deﬁne and measure
avalanche size distributions during memory retrieval, in order to gain insight regarding basic aspects
of the functioning of these complex networks. The avalanche sizes deﬁned for our model should be
related to the time consumed and also to the size of the neuronal region which is activated, during
memory retrieval.
This allows the qualitative comparison of the behaviour of the distribution
of cluster sizes, obtained during fMRI measurements of the propagation of signals in the brain,
with the distribution of avalanche sizes obtained in our simulation experiments. This comparison
corroborates the indication that the Nonextensive Statistical Mechanics formalism may indeed be
more well suited to model the complex networks which constitute brain and mental structure.
PACS numbers:
Keywords: Consciousness-Unconsciousness, Neuroses, Self-organized Neural Networks, Boltzmann Machine,
Generalized Simulated Annealing, Avalanches
∗Electronic address: Maheen.faisal.14@ucl.ac.uk
†Electronic address: roseli@ime.uerj.br
‡Electronic address: h.jensen@imperial.ac.uk
2


## Page 3


I.
INTRODUCTION
The purpose of the present work is to deﬁne, measure and study statistical properties
of avalanches which occur during memory retrieval in an artiﬁcial neural network, devel-
oped to model neurotic phenomena and the associated conscious/unconscious interactions
in mental life [1].
It was famously reported by Freud [2, 3] that patients with neurotic
symptoms systematically repeated these symptoms in the guise of ideas and impulses. This
tendency was referred to as the compulsion to repeat. The patients’ repetitive behaviour
suggested to Freud that they had “. . . the intention of correcting a distressing portion of the
past. . . ” [4]. Although the patient is aware of the obsessional ideas and impulses, and of
the performance of the neurotic actions, the concomitant psychical predeterminants remain
unconscious. In order to infer these predeterminants, and to bring them under the light
of consciousness, Freud developed the analytical treatment called working-through. This
treatment provides, through the interpretation of the predeterminants by freely talking in
psychoanalytical sessions, the connections into which they are inserted.
One of the early seminal ﬁndings of psychoanalytic research is that neurotic symptoms
arise from traumatic and repressed memories. In fact, the repressed material can be con-
strued as knowledge that, in spite of being present in the subject, is inaccessible to him
through symbolical representation. In other words, this knowledge is momentarily or per-
manently inaccessible to the patient’s conscience, and is therefore regarded as unconscious
knowledge [4, 5]. In these considerations, by symbolic representation we mean the association
of symbols to meaning, as occurs in language, as well as in other ways of expressing thoughts
and emotions, such as artistic representations (e.g., a painting or musical composition), and
the recollection of dreams.
Consequently, an important part of the analytical treatment proposed by Freud consists
of a procedure for “bringing what is unconscious into consciousness”. This is tantamount
to a basic technique aiming at “ﬁlling up the gaps in the patient’s memories, to remove
his amnesias” [4]. Indeed, these amnesias are closely related to the origin of the neurotic
symptoms, that is, to the compulsion to repeat. An important purpose of the therapeu-
tic method called working-through, whereby neurotic analysands obtain relief and cure of
painful symptoms, is to develop knowledge regarding the causes of those symptoms. This is
achieved by accessing unconscious memories through free associative talking, which yields
3


## Page 4


understanding and a change in the analysand’s compulsion to repeat [2, 3, 5]. The method is
mainly based on the analysis of free associative talking, symptoms, parapraxes (slips of the
tongue and pen, misreading, forgetting, etc.), dreams, and also on analyzing what is acted
out in transference. This procedure allows the patient to slowly symbolize his repressed
memories and to create new representations of his past experiences.
An illustrative, schematic model of this neurotic mechanism and the working-through
therapeutic method, was advanced in [1, 6]. It was there proposed that the neuroses can be
understood in terms of an associative memory process in neural networks, where the network,
when presented with an input pattern, retrieves a stored pattern which is most similar to the
one currently shown. In order to model the compulsion to repeat a neurotic symptom, it was
assumed that such a symptom is produced when the subject receives a stimulus resembling a
repressed or traumatic memory trace. The stimulus then contributes to stabilize the neural
net in a minimal energy state, corresponding to the trace that synthesizes the original
repressed experience, which in turn produces a neurotic response (an act). The neurotic
act does not result from the stimulus as a new situation, but as a response to the repressed
memory.
The model is based on the conception that the linguistic, symbolic, and associative pro-
cess associated with psychoanalytic working-through therapy is mapped onto a correspond-
ing scheme of reinforcing synapses among memory traces in the brain. These connections
should involve declarative memory, implying that repressed memories are, at least par-
tially, transformed into conscious ones. This takes into account the paramount importance
that language has in psychoanalytic sessions, and the idea that unconscious memories are
precisely those that cannot be expressed symbolically. It was thus proposed that, as the
analysand symbolically elaborates manifestations of unconscious material through transfer-
ence in psychoanalytic sessions, he creates new neural connections, and reinforces or inhibits
older ones, reconﬁguring the topology of his neural net. The network topology arising from
this reconﬁguration process stabilizes onto new energy minima, associated with new acts.
Following the memory organization advanced in [7] (see also [1]), it is assumed that neu-
rons belong to two hierarchically structured modules, respectively corresponding to sensorial
and symbolic memories. Mental images of stimuli received by sensory receptors, either from
the environment or from the body itself, are represented by memory traces stored in the sen-
sorial memory module. On the other hand, higher level representations of traces in sensorial
4


## Page 5


memory, i.e. symbols, are stored in the symbolic memory module. This module represents
brain structures corresponding to symbolic processing, language, and consciousness. Sen-
sorial and symbolic memories are not isolated from each other and indeed, they interact,
generating unconscious and conscious mental activity.
In the model, the unconscious compulsion to repeat in neuroses [2–4] is interpreted as a
bodily response (an act) to an input stimulus (of any kind) that resonates with a pattern
in sensorial memory, without activating symbolic memory. In this sense, the compulsion to
repeat is akin to a reﬂexive act. This accounts for neurotic patients’ claim that they cannot
explain their neurotic acts. A sensorial memory trace becomes conscious when its retrieval
also activates the retrieval of patterns in symbolic memory. If this happens, the resulting
output does not resemble reﬂexive behaviour, and another level of processing becomes rele-
vant. One may also have symbolic representations of emotions, as when someone says “I felt
a warm happiness when I embraced my young nephew”. Sensorial information that is not
(or cannot be) associated to a symbol stays unconscious. The neurotic mechanism described
here is in line with the hypothesis that the emergence of conscious experience requires the
existence of a physical (neural) layer that is able to support metarepresentations [8].
A detailed description of the neural network model for these neurotic features can be found
in [1], which includes a full description of the relevant algorithms. Memory functioning was
ﬁrst modelled by recourse to a Boltzmann Machine (BM), which is a stochastic extension of
the Hopﬁeld model. However, it was later found that the node-degree distributions of the
hierarchically clustered network topologies generated by the model’s clustering algorithm
(see section II), with long and short-range synapses, are well represented by the asymp-
totic power-law, q-exponential distributions. This behaviour indicates that the statistical
features of our model may not be well described by Boltzmann-Gibbs statistical mechan-
ics, but rather by Nonextensive Statistical Mechanics (NSM) [9–11]. The NSM theoretical
framework, and its variegated applications to physics, biology, economics, and other areas,
have been the focus of an intense research activity in recent years [10]. The concomitant
formalism has been applied to the study of diverse types of complex systems, including sys-
tems with long-range interactions [12], systems exhibiting weak chaos [13], complex networks
[14], processes involving nonlinear diﬀusion [15], and many others. In recent work [16, 17]
(see also references therein), the authors have also used Hopﬁeld neural networks to model
attachment in developmental psychology, as well as behavioural patterns in psychology and
5


## Page 6


psychotherapy. In the present work, we thus use the model described in [1], where memory
is simulated by a generalization of the BM inspired on NSM, called Generalized Simulated
Annealing (GSA) [1, 9], and this aﬀects the sequence of associations of thoughts in the
mental processes we are illustrating.
The model is in good qualitative agreement with the main facts provided by psycho-
analytic experience. In particular, it is consistent with the (sometimes exasperating) slow
nature of the working-through process. The model’s dynamics reproduces in a plausible
way the re-association of unconscious sensorial memory traces, and of new experiences, to
symbolic processing areas, mimicking the repetitive, adaptive, reinforcement learning in-
volved in the simulation of working-through. As a result of this self-reconﬁguration process,
represented in the model by a change in network connectivity, the analysand is partially
freed from his/her original neurotic states and concomitant acts. The new network topology
evolves to, and stabilizes itself onto, new energy minima. These resulting network states
are associated with new conscious or unconscious acts. Evidently, the ultimate aim of both
the analysand and the analyst is to reach new states, and generate new acts, that are more
pleasant and comfortable to the analysand and his relations. As the therapy progresses, the
analysand rewrites his/her life history, through a process of new signiﬁcations. Furthermore,
and perhaps more importantly, both the present and the future of the analysand are also
being rewritten, by creating new possibilities, and by opening new windows of opportunity
for the pursuit of happiness. Our central tenet is that this story is embedded, i.e. written,
in the individual’s biological neural network.
It is clear that psychoanalytic theory is still far from having the rigorous quantitative
support required by modern science. However, we agree with some contemporary scien-
tists [18, 19], as well as early psychoanalysts [4, 20, 21] that, although this state of aﬀairs
poses serious limitations and diﬃculties, it also constitutes a challenge and a stimulus for
further scientiﬁc research. These venues of enquiry are worth pursuing, since many ﬁnd-
ings of psychodynamic theories have already contributed both to our understanding and
characterization of mental phenomena, as well as to the development of successful clinical
treatments for many mental disorders [18, 19].
In the present work, we study some additional properties of the aforementioned model,
which give us further knowledge on how basic microscopic and macroscopic features and
mechanisms inﬂuence emergent behaviour of the complex network structures proposed by
6


## Page 7


the model. In Section II, we give a brief overview of the basic algorithms that characterize
the model and which we use in our simulation experiments.
We present a deﬁnition of
avalanche sizes during the memory retrieval mechanism and results of their measurements, in
simulation experiments in Section III. These avalanche sizes can be qualitatively compared
to brain imaging experiments [22], showing that the NSM memory retrieval mechanism
produces power-law behaviour, which does not emerge from BM functioning, i.e.
from
Boltzmann-Gibbs statistical mechanics.
II.
NETWORK TOPOLOGY AND MEMORY ACCESS MECHANISMS
The topological structure of each of the two memory modules was generated by a clus-
tering algorithm proposed in [7] (see also [1]), which models the self-organizing process that
controls synaptic plasticity, resulting in a hierarchically structured neural network topol-
ogy. The algorithm is inspired on microscopic biological mechanisms, found in typical brain,
cellular processes of many animals [23, 24].
As an example we can mention the on-center/oﬀ-surround structure, characterized by
neurons that are in cooperation, through excitatory synapses, with other neurons in their
immediate neighbourhood, while they are in competition with neurons that lie outside these
surroundings. Competition and cooperation occur both in statically hardwired structures,
and as part of a variety of neuronal dynamical processes, where neurons compete for certain
chemicals [23, 24]. In synaptogenesis, for instance, stimulated neurons release neural growth
factors that spread through diﬀusion, reaching neighbouring cells and promoting synaptic
growth. The cells receiving neural growth factors make synapses and live, while those hav-
ing no contact with these substances die [23, 25]. A neuron releasing neural growth factors
ushers the process of synaptic formation in its tridimensional neighbourhood, and becomes
a center of synaptic convergence. Neighbouring neurons releasing diﬀerent neural growth
factors at diﬀerent rates give rise to several synaptic convergence centers. These centers
then compete through the new synapses being created in their surroundings. Through these
processes, a signaling network is established, that controls the development and plasticity
of the brain’s neuronal circuits. This neural competition is started and controlled by envi-
ronmental stimulation and, consequently, it constitutes an important mechanism through
which features of the environment can be mapped onto brain structures.
7


## Page 8


A.
Clustering Algorithm
We reproduce the algorithm proposed in [1, 7] here, to aid understanding of the mea-
surements and analysis which we introduce in this paper. This clustering algorithm models
the self-organizing process which controls synaptic plasticity, and results in a structured
hierarchical topology of each of the two memory modules. It consists of the following steps.
Step 1 The initial bidimensional positions of the neurons are randomly generated according
to a uniform probability density on a square sheet.
Step 2 To simulate synaptic growth, we assume a Gaussian solution of the equation gov-
erning the diﬀusion of the neural growth factors, thus avoiding the time-consuming
numerical treatment of this equation. Consequently, a synapse with strength wij (the
synaptic weight) is allocated to transmit the output signal from neuron nj to a neuron
ni, according to the Gaussian probability density
Pij = exp(−(rj −ri)2/(2σ2))/
√
2πσ2 ,
(1)
where rj and ri are the respective positions of nj and ni in the bidimensional sheet,
and σ is the standard deviation of the Gaussian distribution, which is here a model
parameter. If a synapse connecting nj to ni is generated, its strength wij is proportional
to Pij.
Step 3 It was veriﬁed in [26] that cortical maps representing diﬀerent stimuli are formed,
such that each stimulus activates a group of neurons spatially close to each other, and
that these groups are uniformly distributed along the sheet of neurons representing
memory. So one now randomly selects m neurons which will each be a center of the
representation of a stimulus. To choose the value of m, one should take into account
the storage capacity of the BM [27].
Step 4 Reinforce synapses adjacent to each of the m centers chosen in Step 3, according
to the following criteria.
If ni is a center, deﬁne sumni = P
j |wij|.
For each nj
adjacent to ni, increase |wij| by ∆wij, with probability Probnj = |wij|/sumni, where
∆wij = ηProbnj and η ∈ℜis a model parameter chosen in [0, 1]. After incrementing
|wij|, decrement ∆wij from the weights of all the other neighbours of ni, according to:
∀k ̸= j, |wik| = |wik| −∆wik, where ∆wik = (1 −|wik|/ P
k̸=j |wik|)∆wij.
8


## Page 9


Step 5 Repeat step 4 until a clustering criterion is met.
In the above clustering algorithm, Step 4 regulates the strength of synaptic connections,
i.e., plasticity, by intensifying synapses within a cluster and reducing synaptic strength
between clusters (disconnecting clusters). A cluster is therefore formed by a group of neu-
rons that are close to each other, with higher probability of being connected by stronger
synapses. This mechanism is akin to a preferential attachment criterion, constrained by an
energy conservation (neurosubstances) prescription, controlling synaptic plasticity. Neurons
that have been sensorially more stimulated and are therefore more strongly connected will
stimulate other neurons in their neighbourhoods and promote still stronger connections.
This is compatible with the biological mechanisms mentioned earlier.
The growth of long-range synapses in the brain occurs less frequently than the growth
of short-range ones. The reason for this is that the former are energetically more costly
than the latter. In order to allocate long-range synapses connecting clusters, one should
regard the basic learning scheme proposed by Hebb [27–29], which is based on the idea that
synaptic growth among two neurons is promoted by their concomitant stimulation. Since
we are still not aware of the synaptic distributions that result in topologies which represent
the structure of associations of symbols in language and thought, as a ﬁrst approximation,
we have allocated long-range synapses randomly among clusters of neurons (for a more
detailed discussion see [1, 7]).
Within a randomly chosen cluster C, deﬁned by one of
the m neurons which is the center of representation of a stimulus (step 3 of the clustering
algorithm), a neuron ni is chosen to receive a long-range connection with probability Pi =
P
j |wij|/ P
nj∈C
P
k |wjk|. If the long-range synapse connects clusters in diﬀerent memory
sheets (sensorial and symbolic memories), its randomly chosen weight is multiplied by a
real number ζ in the interval (0, 1], reﬂecting the fact that, in neurotic patterns, sensorial
information is weakly accessible to consciousness, i.e., repressed.
B.
Memory Retrieval
The topologies generated with the clustering algorithm have a hierarchical structure
and the average node-degree distributions present an asymptotic power-law behaviour [1].
The functioning of memory retrieval was originally modelled by a Boltzmann Machine
(BM) [27, 30]. There is no theoretical indication of the exact relation between network
9


## Page 10


topology and memory access dynamics. There have been indications that complex physical
systems characterized by spatial disorder and/or long-range interactions, often presenting
power-law behaviour (are asymptotically scale invariant) may be described by the Nonex-
tensive Statistical Mechanics (NSM) formalism [9–15]. The power-law and generalized q-
exponential behaviour for the node-degree distributions of the network topologies generated
be the clustering algorithm [1] indicate that they may not be well described by Boltzmann-
Gibbs (BG) statistical mechanics, but rather by NSM [9]. Memory access was thus modelled
by a generalization of the BM called Generalized Simulated Annealing (GSA) [1, 9], and
this changes the chain of associations generated by the model.
In the BM [27, 30], the N nodes in the neural network are connected symmetrically
by weights wij = wji. The state Si of each unit ni takes output values in {0, 1}. As a
consequence of the symmetry of the connections, one can associate an energy functional
H({Si}) = −1
2
X
ij
wijSiSj ,
(2)
to network state S = {Si} and, according to the BG distribution, the transition probability
(acceptance probability) from state S to S′, if H(S′) ≥H(S), is given by
PBG(S →S′) = exp
H(S) −H(S′)
T

,
(3)
where T is the network “temperature” parameter. Pattern retrieval on the net is achieved
by a standard simulated annealing process, in which T is gradually lowered by a factor
α, according to the BG distribution [27]. In the NSM formalism, one uses a generalized
acceptance probability [9] for a transition from S to S′, if H(S′) ≥H(S), given by
PGSA(S →S′) =





1
[1+(qA−1)(H(S′)−H(S))/T]1/(qA−1) ,
if ϕ > 0 ,
0 ,
if ϕ ≤0 ,
(4)
where qA is a parameter called q-acceptance and ϕ = 1 + (qA −1)(H(S′) −H(S))/T. In
the limit qA →1, (4) reduces to the Boltzmann-Gibbs transition probability (3). If one
uses transition probability (4) in place of transition probability (3), in the standard BM
simulated annealing algorithm, the resulting procedure is called GSA (see [9] for a more
detailed discussion).
It is convenient that we deﬁne, for each transition from state S to S′ during annealing,
the quantity
∆E = H(S′) −H(S) .
(5)
10


## Page 11


Both the BM and GSA diﬀer from a gradient descent minimization scheme since, besides
allowing state transitions that lower the total energy of the network (2), they also allow the
system to transition into a state with an increase in energy, depending on the values of T
and qA, according to (3) and (4). The BG transition probability (3) predominantly allows
changes of states with small increases in energy, and state transitions with higher energy
increases occur with almost negligible probabilities. The BM will thus strongly prefer visiting
state space within a nearby energy neighbourhood from the starting point (initial state of
the annealing process). The GSA transition probability (4) allows state transitions with
higher energy increases than the BM and, although the probabilities for these transitions
are very low, they are still considerable when compared to the BM. This allows the system to
transition into attractor states that are farther in state space from the initial network state
and also into basins of attraction corresponding to higher energy values [1, 31] (see Figure 2
in [31]). This implies that the hierarchically structured memory modules having both long
and short-range connections, with memory access modelled by GSA achieves associations
among memory traces that are not achieved by the BM [31]. This increase in associativity
observed in the GSA memory retrieval mechanism, when compared to the BM, suggests
that if memory functions according to the NSM theoretical framework, one will have a more
creative mode of memory and mental functioning.
In traditional neural network modelling, the temperature parameter is inspired by the fact
that biological neurons ﬁre with variable strength, and that there are delays in synapses,
random ﬂuctuations from the release of neurotransmitters, and so on. These eﬀects can
be considered as noise in synaptic functioning [23, 27], and we may thus consider that
temperature in the BM and GSA and the qA parameter in GSA control noise. In the model
we are considering [1], non-zero temperature and qA ̸= 1 values regulate associations among
memory traces, in an analogy with the concept that freely talking in analytic sessions and
stimulation from the psychoanalyst lower resistances and allow greater associativity and
creativity.
Once the network topology is generated by the clustering algorithm, one can ﬁnd the
stored patterns by presenting many random patterns to both the BM and the GSA mech-
anism, with an annealing schedule α that allows stabilizing onto the many local minimum
values of the network energy function. Each of the minimum energy values corresponds to
a stable state of the network and is associated with a stored memory trace. These initially
11


## Page 12


stored patterns represent the neurotic memory attractors (as in the compulsion to repeat),
since they are associated with the two weakly linked sensorial and symbolic subnetworks.
In [26], Carvalho et al. proposed a neurocomputational model to describe how the original
memory traces are formed in cortical maps. It is important to note that in our experiments,
we are not aiming at ﬁnding a global minimum energy state, but at visiting the many local
minima of the energy landscape, which represent stored information in a cognitive network.
III.
AVALANCHES IN MEMORY ACCESS
In the present work, we have deﬁned and measured avalanche sizes during the memory
retrieval process. The size of an avalanche during the simulated annealing procedure, both in
the BM and in GSA, is deﬁned to be the number of state changes that occur during annealing,
from the initial to the ﬁnal network state, which corresponds to one of the minima in the
energy landscape of the network. This is equivalent to saying that the size of an avalanche
corresponds to the number of hops (steps) that the access mechanism performs on the
network energy landscape, from an initial state until it reaches one of the local minima.
The avalanche size should thus be proportional to the time for the propagation of a signal
(stimulus), during access of information in memory.
In other words, the avalanche size
should be related to the time associated with memory retrieval and also to the size of the
neuronal region activated during memory access.
In each of the simulation experiments we present here, we performed 2,048,000 minimiza-
tion (annealing) procedures, starting each one from a diﬀerent random network conﬁgura-
tion. Since the simulations require much computational time (many days and even a few
weeks), we have analysed smaller networks with total number of neurons N = 32, such that
Nsens = Nsymb = 16 neurons belong to the sensorial and symbolic modules, respectively.
This is a small network size when one considers the brain, as there are billions of neurons
in the human brain. However, the brain is considered to be scale invariant [22] and because
the short-range mechanisms in the algorithms we use to create network topology are scal-
able, we expect that our experiments should, to some extent, qualitatively be comparable
to biological processes [1].
The annealing schedule was controlled so that the network stabilizes on the many local
minima of the energy landscape, and was the same for both machines in all experiments. We
12


## Page 13


conducted experiments with diﬀerent values of the temperature T and qA parameters. Both
of these parameters model stochastic ﬂuctuations in network functioning and we studied
how the change in T and qA values caused a change in the behaviour of the two machines,
thus aﬀecting the distribution of avalanche sizes, the network energy loss and measurements
of correlations among energy increments along the path followed during annealing.
In Figure 1, we show the avalanche size distributions obtained with the two machines,
for T = 0.05 and qA = 1.3. In this experiment, when executing step 2 of the clustering
algorithm, 50% of the synapses of the network are excitatory (positive synaptic weights)
and 50% are inhibitory (negative synaptic weights). On the left, we see the avalanche size
distributions for the BM and on the right, for GSA. From the distribution in Figure 1-a, it
is clear that the BM has a preferred avalanche size of 125 with an associated probability of
occurrence of 0.96. This distribution also has a smaller peak at avalanche size 1325, which
occurs with probability 0.0022. The smaller peak has a slower decay before a sharp drop.
The distribution for GSA in Figure 1-b, on the other hand, behaves quite diﬀerently.
For the range of avalanche sizes we measured, we observe a monotonic drop in the fre-
quency for GSA. The points measured in this simulation can be approximately ﬁtted by a
q-exponential [10]
expq(x) =





[1 + (1 −q)x]
1
1−q ,
if 1 + (1 −q)x > 0 ,
0 ,
if 1 + (1 −q)x ≤0 .
(6)
This function is at the core of nonextensive thermostatistics, being the result of the con-
strained optimization of the power-law, nonadditive entropic functional
Sq =
1
q −1[1 −
X
i
pq
i] ,
(7)
where pi is a normalized probability distribution and q is a real parameter. The q-exponential
asymptotically behaves as a power-law and, in Figure 1-b, the curve which ﬁts the points
within the observed values of avalanche sizes, corresponding to q = qf = 1.19, does show an
asymptotic behaviour akin to a power-law.
The imaging technique in neuroscience referred to as functional magnetic resonance imag-
ing (fMRI) uses a method known as blood-oxygen-level dependent (BOLD) contrast imag-
ing [32].
Most cells in the body possess their own reservoirs of sugar which undergoes
respiration to produce energy, when the cells need it.
It is known that neurons do not
13


## Page 14


10-7
10-6
10-5
10-4
10-3
10-2
10-1
100
101
 10
 100
 1000
 10000
Frequency
Avalanche Size
BM, T = 0.05
10-8
10-7
10-6
10-5
10-4
10-3
10-2
10-1
100
101
102
 100
 1000
 10000
Frequency
Avalanche Size
GSA, T = 0.05, qA = 1.3
0.09*(( 1-(1-1.19)*( (x - 360) /112.0 ) )**(1/(1-1.19)))
(a)
(b)
FIG. 1:
(a) Frequency of occurrence of avalanche sizes for the BM. (b) Frequency of avalanche
sizes with GSA. For both machines, T = 0.05 and for GSA, qA = 1.3. In both cases, 50% of the
synapses are inhibitive. All depicted quantities are dimensionless.
possess internal stores of energy and, when a neuron is in a ﬁring state it requires energy
in the form of sugar and oxygen, which it obtains by means of a haemodynamic response,
whereby blood releases oxygen to the ﬁring neurons at a greater rate in comparison to those
in resting state. This causes a diﬀerence in magnetic susceptibility between oxygenated and
deoxygenated blood, which results in a magnetic signal variation that may be detected on
an MRI scanner [32]. Studying changes in the brain BOLD signal allows observation of
diﬀerent active areas of the brain to further understand certain aspects of brain functioning.
In 2003, the work of Beggs and Plenz [33] with cortical slices revealed the phenomena
which they called neuronal avalanches in the brain. In those observations, avalanches were
deﬁned as short bursts of activity that last a few milliseconds, followed by several seconds
of inactivity. These phenomena can be observed in cortical slices of the neocortex, although
their relation to physiological processes in the brain is still unknown [33]. The avalanche
sizes detected by Beggs and Plenz follow a power-law-like distribution, with an exponent
of -3/2. In their observations, they recorded spontaneous local ﬁeld potentials continuously
using a 60 channel multielectrode array, and avalanches are a measure of time duration and
spatial reach of the propagation of signals in the brain.
Tagliazucchi et al. [22] extended the work done by Beggs and Plenz [33], “by inspecting
only the relatively large amplitude BOLD signal peaks, suggesting that relevant information
14


## Page 15


can be condensed in discrete events”. The authors present a spatiotemporal point process,
where the timing and location of these discrete events is obtained to study and capture the
dynamics of the brain in a resting state. When regions of the brain show activity above a
certain threshold level, the detected BOLD signal determines the location of the activity as
well as the duration. Figure 3-A in [22] shows examples of co-activated clusters, deﬁned as
“... groups of contiguous voxels with signal above the threshold at a given time” (clusters
are measured in units of voxels).
In [22], Figure 3-D shows the distribution of average measured cluster sizes in fMRI im-
ages for ten individuals, which has a power-law (scale-free) behaviour spanning four orders
of magnitude, also with an exponent of approximately -3/2. The size of a cluster is propor-
tional to the duration of brain activity. The longer the duration for which an avalanche is
seen in the brain, the larger are the observed cluster sizes. This happens because when the
duration of activity is longer, clusters (voxels) cause the activation of neighbouring clusters,
before reducing activity and fading away. This behaviour is comparable to the avalanche size
distributions produced by our computational model, as in Figure 1-b, because an avalanche
size, in our simulation experiments, was deﬁned in a way so that it should be proportional
to the time for propagation of a signal during the access of information in memory. This is
a reasonable assumption, since transition probabilities (3) and (4) which regulate network
functioning should mimic the way the memory network occupies phase-space, during the re-
trieval of a mnemenic trace. So the larger avalanche sizes observed in our simulations should
be associated with larger cluster sizes, as a larger avalanche size is associated with a longer
time for propagation of a signal, with access to a larger number of neighbouring neurons. We
therefore qualitatively compared the behaviour of the distribution of cluster sizes obtained
in [22] with the distribution of avalanche sizes obtained in our simulation experiments, for
some values of the T and qA parameters, and we found q-exponentials with a similar asymp-
totic power-law like behaviour, spanning similar orders of magnitude of avalanche sizes and
frequencies, only for the GSA machine, however with larger absolute values of the exponent
(exponent close to -5 in Figure 1-b and approximately -10 in Figure 4-b). The Boltzmann
machine did not present power-laws in our experiments. This qualitatively corroborates our
initial indication, that the power-law and generalized q-exponential behaviour of quantities
which describe the structure of the complex networks generated by the clustering algorithm
of our model suggest that they may not be well described by Boltzmann-Gibbs (BG) statis-
15


## Page 16


tical mechanics, but rather by NSM [1, 9].
For a sequence of values of energy increments ∆E given by (5) during an avalanche, we
also measured if the value ∆E(τ0) at step τ0 inﬂuences (is correlated to) the value at a later
step ∆E(τ0 + τ). The temporal correlation function G(τ) among elements in a sequence
separated by an interval τ is deﬁned as [34]
G(τ) =
m−τ
X
τ0=1
∆E(τ0)∆E(τ0 + τ)
m −τ
−
 m
X
τ0=1
∆E(τ0)
m
!2
,
(8)
where m is the size of the sequence which is being considered, and should be much larger
than the largest value of τ in the domain of (8).
In Figure 2, we show correlations for one avalanche of the BM in Figure 2-a and for
another avalanche generated by GSA in Figure 2-b. Since avalanches in the BM and GSA
typically have diﬀerent sizes, Figures 2-a and b correspond to diﬀerent values of m. For
both machines we notice an approximate exponential fall of G(τ) for smaller values of τ,
with larger ﬂuctuations around an average decay for GSA. These larger ﬂuctuations for GSA
occur because GSA generates higher probabilities of making state transitions with positive
values of ∆E than the BM. After a rapid decrease, both ﬁgures converge to a situation
where they ﬂuctuate around zero correlation values. A similar behaviour occurs for the
other avalanches which we measured. For larger values of T and qA, the ﬂuctuations around
average correlation values are much larger, since the machines then have higher probabilities
of making state transitions with positive values of ∆E, and the ﬁrst term in (8) is negative
more often than for lower values of T and qA.
We show avalanche size distributions obtained with the two machines, for T = 0.2 and
qA = 1.6, in Figure 3. As a consequence of the increase of the values of the two parameters
that control associativity and noise in the network, both machines have a higher probability
of increasing energy during the annealing process, and therefore achieve higher values of
avalanche sizes more frequently. The BM now has a preferred avalanche size of 1025, with
a corresponding probability of 0.31, as seen from Figure 3-a. The distribution of avalanche
sizes for GSA now loses the general q-exponential behaviour and has two preferred values
(the ﬁrst is 4775 with 0.035 probability and the second is 6375 with probability 0.056), with a
very short power-law like behaviour after the second peak, before a sharp drop. The increase
in frequency of larger avalanche sizes for both machines is consistent with the increase in
associativity for larger values of T and qA found in [31], with GSA still producing more
16


## Page 17


-0.005
 0
 0.005
 0.01
 0.015
 0.02
 0.025
 0.03
 0.035
 0
 5
 10
 15
 20
 25
Correlation G(τ)
τ
BM, Avalanche Size = 1593
-0.01
 0
 0.01
 0.02
 0.03
 0.04
 0.05
 0.06
 0.07
 0
 5
 10
 15
 20
 25
 30
 35
 40
Correlation G(τ)
τ
GSA, Avalanche Size = 2873
(a)
(b)
FIG. 2:
(a) Correlations among the sequence of ∆E values during an avalanche of the BM. The
avalanche size for this experiment is m = 1593 and the maximum value of τ is 25. (b) Correlations
among the ∆E for an avalanche generated by GSA. The avalanche size for this experiment is
m = 2873 and the maximum value of τ is 40. For both machines, T = 0.05 and for GSA, qA = 1.3.
50% of the synapses are inhibitive. All depicted quantities are dimensionless.
associativity than the BM.
There has been recent work regarding the study of the proportion of inhibitory synapses in
the brain (see [35] and references therein). In mammals, this proportion has been measured
to have values between 20 and 30%. We have thus conducted avalanche measurements in our
model so that, when executing step 2 of the clustering algorithm, 70% of randomly chosen
synapses of the network are excitatory (positive synaptic weights) and 30% are inhibitory
(negative synaptic weights). A distribution of avalanche sizes for this proportion of inhibitory
synapses, for both the BM and GSA with T = 0.2, and qA = 0.7 in GSA is shown in Figure 4.
Again we see a preferred avalanche size for the BM, in this case at 1025 with probability
0.32. We also observe once more for GSA in Figure 4-b, for the range of avalanche sizes
which we measured, a monotonic decrease in the distribution of avalanche sizes, so that
the experimental points resulting from this simulation can be approximately ﬁtted by a
q-exponential, with q = qf = 1.098. This is also asymptotically in accordance with the
scale-free, power-law behaviour observed experimentally in [22].
Besides the avalanche size distributions and temporal correlations, we also measured the
17


## Page 18


10-7
10-6
10-5
10-4
10-3
10-2
10-1
100
 10
 100
 1000
 10000
Frequency
Avalanche Size
BM, T = 0.2
10-7
10-6
10-5
10-4
10-3
10-2
10-1
 3000
 4000
 5000
 6000
 7000
 8000
 9000  10000
Frequency
Avalanche Size
GSA, T = 0.2, qA = 1.6
(a)
(b)
FIG. 3:
(a) Frequency of occurrence of avalanche sizes for the BM. (b) Frequency of avalanche
sizes with GSA. For both machines, T = 0.2 and for GSA, qA = 1.6. In both cases, 50% of the
synapses are inhibitive. All depicted quantities are dimensionless.
10-7
10-6
10-5
10-4
10-3
10-2
10-1
100
101
 100
 1000
Frequency
Avalanche Size
BM, T = 0.2
10-6
10-5
10-4
10-3
10-2
10-1
100
101
 100
 1000
Frequency
Avalanche Size
GSA, T = 0.2, qA = 0.7
0.35*(1-(1-1.098)*((x - 160)/161.0))**(1/(1-1.098))
(a)
(b)
FIG. 4:
(a) Frequency of occurrence of avalanche sizes for the BM. (b) Frequency of avalanche
sizes with GSA. For both machines, T = 0.2 and for GSA, qA = 0.7. In both cases, 30% of the
synapses are inhibitive. All depicted quantities are dimensionless.
distributions of the total energy lost by the network, during the annealing processes of each
set of simulation experiments, for both machines, i.e. H(SF inal) −H(SInit) , where SF inal
and SInit are respectively the ﬁnal and initial states of the network, during one memory
retrieval procedure. These distributions are basically the same for both machines during the
18


## Page 19


same experiment, with just a very slight and negligible diﬀerence close to the tales of the
distributions, due to limited size statistics.
IV.
CONCLUSIONS
We have further studied the memory mechanism in a schematic neural network model,
which illustrates conscious and unconscious mental processes in neurotic mental function-
ing [1–5]. The model illustrates aspects of mental functioning related to memory associa-
tivity, creativity, consciousness and unconsciousness, which are present both in pathological
and normal mental processing. The model is based on a self-organizing, clustering algorithm
which generates a hierarchically structured bimodular neural network, based on basic biolog-
ical cellular mechanisms, which have aspects akin to a preferential attachment mechanism,
constrained by an energy conservation (conservation of neurosubstances) prescription, con-
trolling synaptic plasticity. The networks generated by the algorithm have a small-world-like
topology, with clusters of neurons strongly coupled by short-range connections (synapses)
and also less frequent long-range connections. The node-degree distributions of these net-
work topologies present a generalized q-exponential and asymptotic power-law behaviour.
This structure suggests that memory access may best be modelled by a generalization of the
Boltzmann Machine called Generalized Simulated Annealing, and this determines the chain
of associations generated by the model.
In the present work, we have introduced a deﬁnition of avalanche sizes during the simu-
lated annealing procedure of the BM and GSA machine, which model memory access. Both
the BM and GSA are regulated by parameters (temperature T and qA for the NSM formal-
ism) which control stochastic ﬂuctuations in network functioning and model noisy behaviour
present in biological synaptic mechanisms. We conducted simulation experiments with dif-
ferent values of T and qA, and studied how this causes a change in the behaviour of the
two machines, thus aﬀecting the distribution of avalanche sizes, the network energy loss and
measurements of correlations among energy increments along the path followed during an-
nealing. In these experiments, we found that for some values of T and qA, the avalanche size
distributions of the GSA machine may be approximately ﬁtted by a q-exponential, with the
corresponding asymptotic power-law behaviour. The BM does not generate this behaviour
and produces smaller avalanche sizes, related to less associative memory functioning, when
19


## Page 20


compared to GSA.
We conjecture that avalanche sizes deﬁned for our model should be related to the time
consumed and also to the size of the neuronal region which is activated, during access of
information in memory. This assumption is reasonable, since the transition probabilities (3)
and (4) which regulate the BM and GSA network functioning should mimic the way the
memory apparatus occupies phase-space, during the retrieval of a mnemenic trace. We may
therefore qualitatively compare the behaviour of the distribution of cluster sizes, obtained
during fMRI measurements of the propagation of signals in the brain reported in [22], with
the distribution of avalanche sizes obtained in our simulation experiments. For some values of
the T and qA parameters, we ﬁnd a similar power-law like behaviour, spanning similar orders
of magnitude of avalanche sizes and frequencies, only when using the GSA machine, which
is based on the NSM formalism. The BM did not produce this pattern in our simulation
experiments. This result experimentally corroborates our original indication, that the q-
exponential and asymptotic power-law (scale-free) behaviour of macroscopic quantities which
describe the structure of the complex networks generated by the algorithm of our model
suggest that they may indeed be better described by the NSM [9] formalism, rather than by
Boltzmann-Gibbs (BG) statistical mechanics.
We have also considered recent indications that the brains of mammals are composed
of a proportion of inhibitive synapses, which has been measured to have values between
20 and 30% [35]. We therefore measured avalanche size distributions during memory ac-
cess, in networks generated by the clustering algorithm of our model with a proportion of
30% of inhibitive synapses. In this case, we also found that, for some T and qA values,
the avalanche size distributions may be ﬁtted by a q-exponential (with the corresponding
asymptotic power-law behaviour), only for the GSA machine. Indeed, the q-exponential ﬁt
for the case we analysed seems even better with this proportion of inhibitive synapses than
with 50% of inhibitive synapses.
Although the fMRI measurements presented in [22], capture the dynamics of the brain
in a resting state, the authors argue that “... despite the fact that in resting data there are
not explicit inputs, the average BOLD signal around the extracted points ... still resembles
the hemodynamic response function (HRF) evoked by a stimulus”. This further supports
the qualitative comparison of the results of our simulation experiments with their fMRI
measurements.
20


## Page 21


We may thus conclude that the computational model studied in this work is viable as an
illustrative schematic model of some basic mental mechanisms and in fact is qualitatively
comparable to fMRI data obtained from patients, demonstrating actual brain activity. This
comparison also reinforces the idea that complex systems such as the brain may well be
better described by Nonextensive Statistical Mechanics, which produces the asymptotic
power-law behaviour, for various temperatures and qA values, while Boltzmann-Gibbs sta-
tistical mechanic does not show such behaviour. In [33], the authors argue that in the critical
states characterized by power-laws, “the network may satisfy the competing demands of in-
formation transmission and network stability”. As demonstrated in earlier work regarding
this model [1, 31], as well as in our simulations, memory retrieval governed by Nonex-
tensive Statistical Mechanics allows much more associativity in memory functioning than
Boltzmann-Gibbs statistical mechanics, while still achieving the stability necessary for infor-
mation storage (see also [36]). This results in a potentially more creative mental structure
with more capacity for the establishment of metaphors. From the perspective of psychother-
apy, patients with more creativity have a larger possibility of reassociating traumatic and
repressed experiences, and to construct new historical perspectives for their present and fu-
ture, during therapy. Further investigations along this line of research are important, since
they may reveal more basic structural features of brain and mental functioning.
Acknowledgments
We are grateful to Constantino Tsallis, Evaldo Curado, Angel R. Plastino and Abbas
Edalat for fruitful conversations. This research was developed with grants from the Brazil-
ian National Research Council (CNPq), the Rio de Janeiro State Research Foundation
(FAPERJ) and the Brazilian agency which funds graduate studies (CAPES).
[1] R.S. Wedemann, R. Donangelo, L.A.V. de Carvalho, Generalized Memory Associativity in a
Network Model for the Neuroses, Chaos 19 (2009) 015116-(1–11).
[2] S. Freud, Beyond the Pleasure Principle, Standard Edition of The Complete Psychological
Works of Sigmund Freud, Vol. XI, First German edition in 1920, The Hogarth Press, London,
1974.
21


## Page 22


[3] S. Freud, Remembering, Repeating and Working-Through, Standard Edition of The Complete
Psychological Works of Sigmund Freud, Vol. XII, First German edition in 1914, The Hogarth
Press, London, 1953.
[4] S. Freud, Introductory Lectures on Psycho-Analysis, Standard Edition, First German edition
in 1917, W. W. Norton and Company, New York - London, 1966.
[5] S. Freud, The Unconscious, Standard Edition of The Complete Psychological Works of Sig-
mund Freud, First German edition in 1915, Vol. XIV, The Hogarth Press, London, 1957.
[6] R.S. Wedemann, R. Donangelo, L.A.V. de Carvalho, I.H. Martins, Memory Functioning in
Psychopathology, Lecture Notes in Computer Science 2329 (2002) 236–245.
[7] R.S. Wedemann, L.A.V. de Carvalho, R. Donangelo, A Complex Neural Network Model for
Memory Functioning in Psychopathology, Lecture Notes in Computer Science 4131 (2006)
543–552.
[8] A. Cleeremans, B. Timmermans, A. Pasquali, Consciousness and metarepresentation: A com-
putational sketch, Neural Networks 20 (2007) 1032–1039.
[9] C. Tsallis, D.A. Stariolo, Generalized simulated annealing, Physica A 233 (1996) 395–406.
[10] C. Tsallis, Introduction to Nonextensive Statistical Mechanics, Approaching a Complex World,
Springer, New York, 2009.
[11] C. Beck, Generalised information and entropy measures in physics, Contemporary Physics
50(4) (2009) 495–510.
[12] C. Vignat, A. Plastino, A.R. Plastino, Entropic upper bound on gravitational binding energy,
Physica A 390 (2011) 2491–2496.
[13] U. Tirnakli, E.P. Borges, The standard map: From Boltzmann-Gibbs statistics to Tsallis
statistics. Nature Sci. Rep. 6 (2016) 23644.1–8.
[14] S. Brito, L.R. da Silva, C. Tsallis, Role of dimensionality in complex networks. Nature Sci.
Rep. 6 (2016) 27992.1–8.
[15] M.S. Ribeiro, F.D. Nobre, E.M.F. Curado, Classes of N-Dimensional Nonlinear Fokker-Planck
Equations Associated to Tsallis Entropy, Entropy 13(11), (2011) 1928–1944.
[16] A. Edalat, F. Mancinelli, Strong Attractors of Hopﬁeld Neural Networks to Model Attachment
Types and Behavioural Patterns, in: P. Angelov, D. Levine (Eds.), Proceedings of The 2013
International Joint Conference on Neural Networks (IJCNN), IEEE - Curran Associates, Inc.,
New York, 2013, pp. 1-10.
22


## Page 23


[17] A. Edalat, F. Mancinelli, Introduction to self-attachment and its neural basis, in: D.S. Huang,
Y. Choe (Eds.), Proceedings of The 2015 International Joint Conference on Neural Networks
(IJCNN), IEEE - Curran Associates, Inc., New York, 2015, pp. 1-8.
[18] E. Kandel, Psychiatry, Psychoanalysis, and the New Biology of Mind, American Psychiatric
Publishing, Inc., Washington D.C., London, 2005.
[19] Shedler, J., The Eﬃcacy of Psychodynamic Psychotherapy, American Psychologist 65(2)
(2010) 98–109.
[20] Lacan, J.: On a Discourse that Might not be a Semblance. The Seminar of Jacques La-
can, Book XVIII. Translated by Cormac Gallagher from unedited French manuscripts,
http://www.lacaninireland.com, (accessed 07.04.17) Seminar in France (1971), French edi-
tion, Editions du Seuil, 2007.
[21] J. Lacan, O Semin´ario, Livro 8: A Transferˆencia, Jorge Zahar, Rio de Janeiro, 1992, First
French edition in 1991.
[22] E. Tagliazucchi, P. Balenzuela, D. Fraiman, D. R. Chialvo, Criticality in large-scale brain
fMRI dynamics unveiled by a novel point process analysis, Frontiers in Physiology — Fractal
Physiology 3, (2012) Article 15.
[23] E.R. Kandel, J.H. Schwartz, T.M. Jessel (Eds.), Principles of Neural Science, MacGraw Hill,
New York, 2000.
[24] H. Hartline, F. Ratcliﬀ, Inhibitory Interactions of Receptor Units in the Eye of Limulus,
Journal of General Physiology 40 (1957) 357–376.
[25] W.F. Ganong, Review of Medical Physiology, MacGraw Hill, USA, 2003.
[26] L.A.V. de Carvalho, D.Q. Mendes, R.S. Wedemann, Creativity and Delusions: The Dopamin-
ergic Modulation of Cortical Maps, Lecture Notes in Computer Science 2657 (2003) 511–520.
[27] J.A. Hertz, A. Krogh, R.G. Palmer, Introduction to the Theory of Neural Computation,
Perseus Books, Cambridge, Massachusetts, USA, 1991.
[28] G.M. Edelman, Wider than the Sky, a Revolutionary View of Consciousness, Penguin Books,
London, 2005.
[29] E.R. Kandel, I. Kupfermann, S. Iversen, Learning and Memory, in:
E.R. Kandel, J.H.
Schwartz, T.M. Jessel (Eds.), Principles of Neural Science, fourth ed., MacGraw Hill, New
York, 2000, pp. 1227-1246.
[30] W.C. Barbosa, Massively Parallel Models of Computation, Ellis Horwood Limited, England,
23


## Page 24


1993.
[31] R.S. Wedemann, L.A.V. de Carvalho, R. Donangelo, Access to Symbolization and Associativ-
ity Mechanisms in a Model of Conscious and Unconscious Processes, in: A. V. Samsonovich
and K. R. J´ohannsd´ottir (Eds.), Biologically Inspired Cognitive Architectures, Frontiers in
Artiﬁcial Intelligence and Applications, IOS Press, USA, 2011, pp. 444–449.
[32] S.A. Huettel, A.W. Song, G. McCarthy, Functional Magnetic Resonance Imaging, second ed.,
Sinauer, Massachusetts, USA (2009).
[33] J.M. Beggs, D. Plenz, Neuronal avalanches in neocortical circuits, Journal of Neuroscience 23
(2003) 11167–11177.
[34] H.J. Jensen, Self-Organized Criticality, Emergent Complex Behavior in Physical and Biological
Systems, Cambridge University Press, Cambridge, UK, 1998.
[35] V. Capano, H.J. Herrmann, L. de Arcangelis, Optimal percentage of inhibitory synapses in
multi-task learning, Nature Sci. Reps. 5 (2015) Article 9895.
[36] R.S. Wedemann, A.R. Plastino, Asymmetries in Synaptic Connections and the Nonlinear
Fokker-Planck Formalism. Lecture Notes in Computer Science 9886 (2016) 19–27.
24

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
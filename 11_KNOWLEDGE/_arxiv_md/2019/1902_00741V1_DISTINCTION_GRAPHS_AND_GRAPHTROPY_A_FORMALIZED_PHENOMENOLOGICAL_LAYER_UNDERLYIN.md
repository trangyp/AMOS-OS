---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1902.00741v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1902.00741v1_Distinction_Graphs_and_Graphtropy__A_Formalized_Phenomenological_Layer_Underlyin

> Source: 1902.00741v1_Distinction_Graphs_and_Graphtropy__A_Formalized_Phenomenological_Layer_Underlyin.pdf

> Pages: 28

---


## Page 1


arXiv:1902.00741v1  [cs.AI]  2 Feb 2019
Distinction Graphs and Graphtropy:
A Formalized Phenomenological Layer
Underlying Classical and Quantum Entropy,
Observational Semantics
and Cognitive Computation
Ben Goertzel
February 5, 2019
Abstract
A new conceptual foundation for the notion of “information” is pro-
posed, based on the concept of a distinction graph: a graph in which
two nodes are connected iﬀthey cannot be distinguished by a particu-
lar observer. The “graphtropy” of a distinction graph is deﬁned as the
average connection probability of two nodes; in the case where the distinc-
tion graph is a composed of disconnected components that are fully con-
nected subgraphs, this is equivalent to Ellerman’s logical entropy, which
has straightforward relationships to Shannon entropy. Probabilistic dis-
tinction graphs and probabilistic graphtropy are also considered, as well
as connections between graphtropy and thermodynamic and quantum en-
tropy.
The semantics of the Second Law of Thermodynamics and the Max-
imum Entropy Production Principle are unfolded in a novel way, via
analysis of the cognitive processes underlying the making of distinction
graphs. The Second Law is re-cast in the form: “The graphtropy of an
observer’s memory graph will never decrease,” which is argued to hold
true under speciﬁc assumptions regarding the observer’s cognitive struc-
ture.
This evokes a connection between graphtropy and consciousness
theory, in which complex intelligence is seen to correspond to states of
consciousness with intermediate graphtropy, which are associated with
memory imperfections that violate the assumptions leading to derivation
of the Second Law.
A connection with algorithmic information theory is made: In the case
where nodes of a distinction graph are labeled by computable entities,
graphtropy is shown to be monotonically related to the average algorith-
mic information of the nodes (relative to to the algorithmic information
of the observer).
A quantum-mechanical version of distinction graphs is considered, in
which distinctions can exist in a superposed state; this yields to graph-
1


## Page 2


tropy as a measure of the impurity of a mixed state, and to a concept of
“quangraphtropy” that connects Feynman-type sums with graphtropy of
distinction graphs.
A novel computational model called Dynamic Distinction Graphs (DDGs)
is formulated, via enhancing distinction graphs with additional links ex-
pressing causal implications. DDGs enable a detailed model of the “ob-
servers” that play a central role in distinction graph theory and graph-
tropy.
Via these diverse considerations, the position is advanced that found-
ing information in the graph of distinctions perceivable by a particular
observer (who is himself a set of distinctions and causal relations there-
between), yields insight into many of the multiple aspects of physical and
mental reality in which the “information” concept plays a role.
Contents
1
Introduction
3
2
Logical Entropy
6
2.1
Quantum Logical Entropy . . . . . . . . . . . . . . . . . . . . . .
6
3
Graphtropy
6
3.0.1
Graphtropy of Combinations
. . . . . . . . . . . . . . . .
7
3.0.2
Graphtropy of Distributions . . . . . . . . . . . . . . . . .
7
3.1
Semantic Interpretation of Graph Logical Entropy in Terms of
Distinction Graphs . . . . . . . . . . . . . . . . . . . . . . . . . .
8
3.1.1
Combinatory Operations on Distinction Subgraphs . . . .
9
3.2
Key Properties of Graphtropy . . . . . . . . . . . . . . . . . . . .
9
4
Probabilistic Graphtropy
10
5
Graphtropic Thermodynamics
10
5.1
The Analogue of Thermodynamic Entropy on Distinction Graphs
11
5.2
The Analogue of the Maximum-Entropy Distribution on Distinc-
tion Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
6
Connecting Graphtropy with Algorithmic Information
13
6.1
Graphtropic Energy
. . . . . . . . . . . . . . . . . . . . . . . . .
14
6.2
Graphtropic Temperature . . . . . . . . . . . . . . . . . . . . . .
14
7
Dynamic Distinction Graphs: a Phenomenology-Based Com-
putational Model
15
7.1
Modeling Observers as Dynamic Distinction Graphs
. . . . . . .
17
8
The Second Law of Thermodynamics on Distinction Graphs
18
8.1
Object Persistence and the Second Law
. . . . . . . . . . . . . .
19
8.2
Graphtropy, States of Consciousness and Intelligence . . . . . . .
21
2


## Page 3


8.3
Maximum Entropy Production
. . . . . . . . . . . . . . . . . . .
22
9
Quantum Graphtropy
24
9.1
Quantum Distinction Graphs as a Representation of Mixed States 24
9.2
Quangraphtropy
. . . . . . . . . . . . . . . . . . . . . . . . . . .
25
9.3
Quantum Dynamic Distinction Graphs . . . . . . . . . . . . . . .
25
10 Conclusion
26
1
Introduction
“Information” is increasingly accepted as a fundamental concept; it is now some-
what commonly posited that the physical world [Llo06] and the thinking mind
[Bat79] are both composed of information.
The basic nature of information, however, is not made especially clear in
traditional mathematical, physical or engineering presentations of information
theory and related ideas.
Often “information” is grounded in terms of “entropy”. Entropy has a clear
meaning in thermodynamics, and is a fundamental concept in numerous other
areas of science including quantum mechanics, communication theory, statistics,
computational linguistics, AI and others. Related concepts such as the Maxi-
mum Entropy Principle have a very broad applicability as well. However, the
foundations of the entropy concept are not as plain as one might think. For
instance the thermodynamic and communication-theoretic notions of entropy
are often discussed as if they were interchangeable, but on the mathematical
level are interrelated only by an approximation. The role of the observer in
entropy-related phenomena such as the Second Law of Thermodynamics is also
less clear than is generally suggested, and is rarely grounded in a serious model
of the “observer” as a particular system in the world.
Here we seek to establish a new foundation for the information concept, via
taking a slightly diﬀerent approach both mathematically and conceptually.
Mathematically, we begin with Ellerman’s notion of “logical entropy” [Ell13]
and extend it to a new concept of “graph entropy” or graphtropy. Graphtropy
is an extremely simple quantity – merely the “mean connection weight” in a
graph. However, this simple measure turns out to have an intriguing semantic
interpretation, if one focuses on “distinction graphs,” in which the existence or
weight of a link between two nodes a and b denotes the propensity of a certain
observing system to confuse a with b.
Conceptually, our key innovation is to take the observer seriously. To under-
stand information, we suggest, one should begin with a speciﬁc observer, and
ask what distinctions this observer is capable of making. This leads to a distinc-
tion graph and to graphtropy as one among a number of interesting quantities
to compute.
The answer to the question “What is information?”, is then posited to be:
3


## Page 4


• a body of information is a set of distinctions, drawn by some particular
observer
• There are various ways of quantifying the amount of information in a
certain body of information (i.e.
in a certain set of distinctions).
The
graphtropy (the mean amount of distinctiveness between entities) is one
key measure of this sort.
Logical entropy, with clear relationships to traditional Shannon entropy, emerges
as the formula for the graphtropy of a body of information if one makes certain
special assumptions about the structure of this body. These assumptions are
not accurate for real observers, but are often good enough approximations for
practical purposes.
On a philosophical level, the perspective given here is inspired somewhat
by the thinking of G. Spencer-Brown [Bro69] and Lou Kauﬀman [Kau87], who
have emphasized the foundational role of the concept of distinction in explaining
how an observer creates a world, and how a world creates an observer. However,
the types of mathematical analysis pursued here are quite diﬀerent from (and
complementary to) what these two authors have done. There is also a very
close connection between the ideas given here and Isaacson and Kauﬀman’s
notion of “recursive distinctioning” (RD) [IK16]. RD is concerned with con-
structing graphs whose edges represent distinctions, and then studying these
graphs. However, the speciﬁc work presented so far under the RD umbrella
involves distinction graphs with rigid geometric structure (e.g. square lattices),
and the algebras implicit in what happens when one labels these graphs in cer-
tain ways; interesting considerations, but quite diﬀerent than the directions we
pursue here (though probably there are relationships to be unfolded).
Graphtropy can be applied, as a mathematical measure, independently of
the interpretation of graphs as distinction graphs. However, it is the use of
graphtropy in the context of distinction graphs that will preoccupy us here the
most. From this perspective, graphtropy allows the exploration of entropy and
related concepts at a level more primitive and foundational than the analyses
associated with the standard entropy formulae. One begins with the “observer”
as a system that has a certain capability to distinguish pairs of entities from each
other, and builds a distinction graph based on a speciﬁc observer’s capability of
distinction, and then studies quantities associated with this distinction graph
– thus obtaining a new view of traditional information-theoretic formulae, and
also some additional distinctive quantities of interest.
Graphtropy can be deﬁned and calculated in a quantum-mechanical context.
If one has distinctions that are “superposed between being drawn and not being
drawn,” in the way that quantum logic allows, then one can calculate graphtropy
in a way that takes this into account, still getting a meaningful quantitative
measure of the amount of information in a certain body of information. The
study of graphtropy on complexly structured distinction graphs may potentially
shed light on the nature of weak quantum coherence.
Graphtropy connects with thermodynamics, in diﬀerent (though related)
4


## Page 5


ways to the links between these areas and traditional entropy. Both the maxi-
mum entropy principle and the maximum entropy production principle appear
meaningful in a graphtropic context, though with considerable mathematical
complexities that are mostly indicated rather than resolved here. The Second
Law of Thermodynamics can be studied in a novel way using distinction graphs,
and in this context takes the form of a statement about the subjective perspec-
tives of certain classes of observers. If one assumes an observer’s memory retains
data about distinctions observed between states of a system, then one arrives
at the conclusion that the graphtropy of the observer’s memory graph will never
decrease, which is a well-founded cognitive version of the Second Law.
Of course, a real-world system’s memory is going to be strictly bounded
relative to the totality of its historical perceptions, and so the assumptions
underlying the graphtropic Second Law will not hold. This ties in with the
observation that real-world intelligent systems tend to occupy conditions of in-
termediate graphtropy, corresponding to states of consciousness inbetween the
purely “oceanic” state of minimum graphtropy and the ultimately “individuat-
ing” state of maximal graphtropy.
Graphtropy also connects with algorithmic information theory. If the nodes
in a distinction graph are associated with entities possessing various degrees
of complexity (in the sense of algorithmic information), then the graphtropy
emerges as a nonlinear, monotonic transform of the mean degree of complexity
of these entities, as compared to the complexity of the observer. Graphtropy is
thus, in a sense, a monotonic transform of the algorithmic information of the
observed relative to the observer. This connects computing theory with more
philosophically basic considerations related to bodies of perceived distinctions.
Finally we articulate a simple, novel computing model based on distinction
graphs, obtained via augmenting the basic distinction graph model with causal
implication links to yield what are called Dynamic Distinction Graphs (DDGs).
In this model the complexity of a node has to do with the set of computational
operations that are embodied by the graph links connecting that node. The
goal here is to show how computing can emerge from very simple phenomeno-
logical entities. Such a model may be useful for understanding computing at
the border between classical and quantum, and at the border between physical
and cognitive. It also gives an in-depth formal model for the “observers” that
play such a critical role in distinction graph theory. A distinction graph exists
relative to an observer, so it’s elegant that an observer can in turn be modeled
as a dynamic distinction graph; and a time-series of distinction graphs can be
data-mined to form a DDG which can in turn be considered as an observer.
This paper is an initial foray into a new area, and much remains to be
done. However, I believe enough is presented here to make the key point. If
one begins by taking the observer seriously, and constructing a graph represent-
ing the distinctions this observer is capable of making, then one can calculate
simple quantities associated with this graph and arrive at a more foundational
understanding of “what is information, relative to an observer.” Traditional no-
tions of entropy then emerge from these same graphs under special structural
assumptions. Traditional notions of entropy are extremely useful in various ap-
5


## Page 6


plications, but we believe that the study of distinction graphs provides a deeper
view of the concept of “information” and thus of the foundations of information
theory, and a pointer into a rich domain of associated, important and minimally
explored ideas.
2
Logical Entropy
In this section we brieﬂy summarize some mathematical and conceptual pre-
liminaries: Ellerman’s notion of logical entropy, which connects elegantly to
traditional Shannon entropy, and which also turns out to be a special case of
our concept of graphtropy.
Given a partition π = {B1, . . . , Bn} of a set U, David Ellerman [Ell13]
deﬁnes a dit or distinction of the partition as an ordered pair (u, u′) ∈u × U so
that u and u′ are in diﬀerent elements of the partition. The set of distinctions
of the partition π is the dit set dit(π). The logical entropy of the partition is
then deﬁned as
h(π) = |dit(π)|
|u × u|
If one sets pi = Bi
B , then it follows that
h(π) = 1 −
n
X
i=1
p2
i
2.1
Quantum Logical Entropy
The quantum variant of these ideas follows similarly [Ell16]. Let V be an n-
dimensional Hilbert space Cn. Let |Φi⟩, i = 1 . . . m be a set of orthornormal
vectors in V , and let p = (p1, . . . , pm) be a probability distribution; then
ρ(Φ) =
m
X
i=1
pi |Phii⟩⟨Phii|
is a density matrix, and any positive operator on V of trace 1 can be represented
this way. The quantum logical entropy is then deﬁned as
h(ρ) = 1 −tr[ρ2]
– a formula often referred to as the ”purity” of the density matrix.
3
Graphtropy
Ellerman’s logical entropy may be viewed as a special case of a more general
concept of graph logical entropy, or more concisely “graphtropy.” Given N el-
ements viewed as nodes of a graph, a partition of the elements corresponds
6


## Page 7


to a “partition graph” that consists of a set of disjoint completely-connected
subgraphs spanning the N elements. We will describe here a way of calculat-
ing a “logical entropy” for a general graph, which reduces to Ellerman’s logical
entropy for the special case of a partition graph. After presenting the formal
notion of graphtropy we will outline a natural semantic interpretation in terms
of the distinctions made by an observer.
Given an undirected graph G = (UG, EG) = (U, E), we may deﬁne a “dit”
as a pair (u, u′) of nodes that don’t have an edge between them in the edge-set
E. In the case that G is a partition graph, the dit set git(G) of G is the dit set
of the corresponding partition.
We then deﬁne the graphtropy of G as
h(G) = |git(G)|
|UG|2
As Ellerman does with his logical entropy, one can deﬁne a conditional ver-
sion of graphtropy. If one has two graphs G and H over the same node-set U,
one can deﬁne conditional graphtropy as
h(G|H) = |git(G ∩H)|
git(H)
– i.e.
the odds, when choosing an edge (a distinction) in H, that one gets
an edge that is also a distinction in G. Similarly one can deﬁne (symmetric)
graphtropic mutual information via
m(G, H) = |git(G ∩H)|
|UG|2
3.0.1
Graphtropy of Combinations
Next, and dropping the assumption that G and H have the same node-set, we
can look at the categorical product G N H, observing that
h(G
O
H) = |git(G)git(H)|
|UGUH|2
= h(G)h(H)
The categorial product forms a lattice if paired with the disjoint union
G L H; and we may calculate
h(G
M
H) = h(G)|UG| + h(H)|UH|
|UG| + |UH|
3.0.2
Graphtropy of Distributions
Next, suppose that instead of two concrete graphs G and H, we have a joint
weight function w(x, y) over the space of graphs x N y with some ﬁxed node-sets
Ux and Uy. Here w(x, y) indicates the probability that a random graph drawn
from the speciﬁed distribution is of the form x N y for the x and y given.
7


## Page 8


(Also, let us assume that the graphs G and H involved all have speciﬁc
orderings to their node-lists. This assumption will play a meaningful role in some
counting arguments below, when we get to “graphtropic thermodynamics.”)
Note that w(x, y) is not a probability density function because the same
graph z may be represented as the categorial product of multiple diﬀerent pairs
(x, y). We can deﬁne a corresponding density p(x, y) = w(x, y)/n(x, y) where
n(x, y) indicates the number of other pairs (x′, y′) with (x′, y′) ̸= (x, y) and
x Ny= x′ N y′.
We can then deﬁne the graphtropic mutual information of the distribution
p as:
m(x, y) = h(x) + h(y) −h(x, y)
Here h(x) represents the odds that (a, a1) is not in the speciﬁed graph x, and
h(y) represents the odds that (b, b1) is not in the speciﬁed graph y.
h(x, y)
represents the odds that we have both (a, a1) ̸∈Ex and (b, b1) ̸∈Ey. If the
weight w is set up so that x and y are drawn independently, then h(x, y) =
h(x)h(y).
In a similar way we can deﬁne graphtropic conditional information, KL diver-
gence, and Fisher metric. The latter enables us to deﬁne a natural information
geometry on the space of distributions over graphs, which is interesting in the
context of the semantic interpretations to be discussed below.
3.1
Semantic Interpretation of Graph Logical Entropy in
Terms of Distinction Graphs
The above mathematics is subject to many possible semantic interpretations;
however, it was developed with a particular interpretation in mind, involving
graphs representing relationships between observations by cognitive systems.
(For now, we leave the innards of these “cognitive systems” out of consideration,
but later on we will introduce the option of modeling these cognitive systems
as Dynamic Distinction Graphs, bringing the observer underlying the posited
observations more fully into the fold of the theory.)
In this interpretation, we consider nodes in a graph as possible observed
entities, observed by some system. We can model a system as receiving a set
of percepts, each one arriving during a certain interval of time, an “entity”
then corresponds to a set of percept-sets (each percept-set in the set, being an
“instance” of the entity). Then, a link between two nodes indicates that the two
entities are perceived as identical – i.e., non-distinguishable –by the given
observer.
In the case that distinction (or equivalently non-distinction, i.e.“perception
as identical”) is transitive, the graph consists of a set of disconnected compo-
nents, each of which is a fully connected graph – i.e. a partition. But in the
case of a real-world perceiving agent, non-distinction is generally not transitive;
because, after all, perceived entities can continuously morph into quite diﬀerent
perceived entities.
8


## Page 9


Table 1: Key features of graphtropy algebra
Elements
dits (u, u′) of G
Order
Reﬁnement, dit(G) < dit(H)
Top of Order
graph with no edges
Bottom of Order
completely connected graph
Variables in Formulas
graphs on vertex set V
Operations
graph operations (e.g. categorial product, disjoint union)
Formula Φ(x, y, . . .) holds
(u, u′) a dit of Φ(G, H, . . .)
Valid formula
Φ(G, H, ..) = 1 for all G, H, . . .
A subgraph of linked entities may also be considered a higher-level entity
(formed of lower-level entities with distinguishability relations between them).
The reader may see where we’re going with this. In the case of transitive
non-distinction, we are dealing with partitions and hence the concept of logical
entropy applies. In the case where non-distinction is intransitive, we are dealing
with graphs that do not represent partitions, and graphtropy is the relevant
concept for measuring information.
3.1.1
Combinatory Operations on Distinction Subgraphs
To combine entities A and B semantically, we can use the Boolean or categorial
operator-sets.
For instance, suppose A refers to blue chickens, and B refers to red dogs.
Then,
• The categorial product a N B is the set of pairings of a blue chicken and
a red dog.
• The categorial sum A L B is the set of entities to be used in building
pairings of a blue chicken and a red dog (where if there is some individual
that is both a blue chicken and a red dog, it gets double-counted).
• The Boolean product A∩B is the set of entities that are both blue chickens
and red dogs.
• The Boolean sum A ∪B is the set of entities that are either blue chickens
or red dogs.
3.2
Key Properties of Graphtropy
In [Ell13], Ellerman compares Shannon entropy and logical entropy on various
points. Similarly we may compare graphtropy on these points; the results are
shown in Tables 1 and 2.
9


## Page 10


Table 2: Probabilistic interpretation of graphtropy algebra
Outcomes
edges in graph
Events
graphs with vertex set v
Event occurs
u, u′ are not linked (are distinguished)
Quantitative measure
p(G) = |git(G)|/|V xV |
Random drawing
Prob. that graph G does not have the link randomly selected
4
Probabilistic Graphtropy
Extending the above ideas, we can also look at graphs with weighted links. Here
the semantic interpretation is a “weighted distinction graph”: the link between
the node representing entity a and the node representing entity B, represents
the probability that the cognitive agent in question can distinguish an instance
of a and an instance of B.
Many types of weights can be considered, e.g. individual probabilities or
probability intervals. To make the math comes out simpler, we will focus here
on the case where the weights are interval probabilities, e.g. [.6, .8]. These may
be interpreted as imprecise probabilities a la Walley [Wal00]. The case where
weights are indeﬁnite probabilities (a la [GIGH08]) is an immediate extension.
In this case, instead of the probability of there being a link between A and
B, we can look at the distribution of link weights between A and B (given that
A and B are randomly drawn from B), and at parameters of this distribution,
such as the mean. For a non-weighted graph, this distribution is bimodal, and
its mean is the percentage of pairs of nodes that are interlinked.
We may deﬁne “weighted graphtropy” as graphtropy in the context of weighted
graphs. Key features of the weighted graphtropy are shown in Tables 3 and 4.
Here we deﬁne an order between two edges in a weighted graph via (u, u′, w) <
(u, u′, w1) iﬀw < w1, i.e. wL > w1L, wU < w1U; i.e. if the interval probability
w is more speciﬁc than the interval probability w1, and the former is contained
within the latter.
An “event” in the context of a weighted distinction graph corresponds to a
second-order probability distribution, i.e. a statement regarding the probability
values on the edges of the graph (which is also a statement regarding the links
existing in the graph, implicitly).
The value |E|, where E is a set of weighted edges, in general could be given
by some probability density p over graph space.
It would then denote the
percentage of graphs G, according to p, so that: For each edge e ∈E, there is
some edge e′ ∈G so that e′ < e.
5
Graphtropic Thermodynamics
One of the most interesting aspects of Shannon entropy is the bridge that it
forms between thermodynamics and information theory. Graphtropy turns out
to form a diﬀerent, related sort of bridge between these disciplines.
10


## Page 11


Table 3: Key features of weighted graphtropy algebra
Elements
dits (u, u′, w) of G , where w is an imprecise probability
Order
Reﬁnement, dit(G) < dit(H)
Top of Order
graph with no edges
Bottom of Order
completely connected graph, all edges with weight 1
Variables in Formulas
weighted graphs on vertex set V
Operations
graph operations (e.g. categorial product, disjoint union)
Formula Φ(x, y, . . .) holds
(u, u′, w) is less than some dit of Φ(G, H, . . .)
Valid formula
Φ(G, H, ..) = 1 for all G, H, . . .
Table 4: Probabilistic interpretation of weighted graphtropy algebra
Outcomes
edges in graph
Events
graphs with vertex set v
Event occurs
u, u′ has weight within interval w
Quantitative measure
p(G) = |git(G)|/|V xV |
Random drawing
Prob. that graph G does not have the link randomly selected,
with a weight inside the interval w randomly selected
5.1
The Analogue of Thermodynamic Entropy on Distinc-
tion Graphs
The thermodynamic entropy of a macrostate consists of the log of the number
of microstates consistent with that macrostate. The Shannon entropy approxi-
mates (but does not equal exactly) the number of micro states consistent with
the observed macro state (the observed probability distribution over partition
cells).
What are the micro and macro states in the above interpretation of graph-
tropy. Consider ﬁrst the case of partition graphs. Here a graph node consists
of a microstate; and a “macrostate” consists of a set of statistical observations
of the graph, where what is observed is the percentage of the observations that
lie in each partition cell.
For a distinction graph, then, the number of “microstates” consistent with
the graph is the number of automorphisms of the graph.
If the graph is a
partition graph, then this yields the entropy according to standard calculations.
For a weighted distinction graph G, we want to average, over all automor-
phisms s, the distance between s(G) and G. Here distance may be measured
e.g. by the average over all edges of the KL divergence between the distribution
given to E by G and the distribution given E to by s(G).
5.2
The Analogue of the Maximum-Entropy Distribution
on Distinction Graphs
Suppose we have a “node-weighted graph” – i.e., each node has an integer
weight on it, drawn from some ﬁxed ﬁnite set of integers. Suppose the sum
11


## Page 12


(or, equivalently, average) of the weights is supposed to be kept equal to some
constant K.
Suppose we also have some constraints on the graph structure – e.g.
• that the graph has to be a set of disconnected completely-connected graphs;
or
• that the graph has to have maximum degree less than m; or
• that the graphtropy must be equal to, or closely approximated by, some
ﬁxed value (we will return to this case below)
Then, what is the most likely way for the weights to be distributed among the
nodes?
Suppose we adopt the principle that, given lack of any other information, we
should assume the various microstates compatible with an observed macrostate
to have equal probability. In this case, the most likely way for the weights to
be distributed, is the one that can occur in the most ways.
For each node-weighted graph G, we can calculate the number of automor-
phisms of the graph that preserve the weights on the nodes, as well as the
connection structure. Speciﬁcally, each automorphism has got to map a node
with weight m into another node with weight m.
The most likely weighted graph is then going to be the one that has the
greatest number of node-weight-preserving automorphisms.
This is the “maximum likelihood distribution” on G.
For a partition graph in which all nodes in the same partition cell i have
the same weight ni , this yields the ordinary maximum entropy distribution
associated with the probabilities pi deﬁned by the sizes of the partition, subject
to the constraint P
i nipi = K.
If G has probabilistic weights on its links, we can make a similar deﬁnition,
by restricting attention to automorphisms that map each link with weight w
into another link with weight w′ < w. Or more adventurously, we can look at
“ǫ-automorphisms” Φ for which: where w(a) is the weight on node a and µab is
the mean of the imprecise probability weight on the link between a and b, and
some speciﬁc assumed small numbers ǫi,
|wa −wΦ(a)| < ǫ1
1 −ǫ2 <
µab
µΦ(a)Φ(ab)
1 + ǫ2
µabµΦ(a)Φ(ab)(|wa −wΦ(a)| + |wb −wΦ(b)|) < ǫ3
for all nodes a, b. This is a sort of “fuzzy automorphism” – the weight on the
image Φ(a) is allowed to diﬀer a bit from that of a, and the weight on the link
(Φ(a), Φ(b)) is allowed to diﬀer a bit from that of (a, b). But the diﬀerences
can’t get too big, and speciﬁcally, it matters more if strongly connected nodes
12


## Page 13


are mapped into strongly connected nodes, than if weakly connected nodes are
mapped into weakly connected nodes.
For partition graphs and linear constraints on the node weights, we know the
maximum likelihood distribution is given by the Gibbs distribution. Whether
there is an equally elegant formula for more general distinction graphs is not
clear. There is some combinatorial work to be done here. Given a certain ﬁxed
graphtropy g, and m integer labels (say, 1 . . . m) constrained to have a ﬁxed
average, is there a closed-form formula for he most likely distribution of labels
(given constraint that two linked nodes must have the same label)? A closed-
form formula for the ǫ-automorphism case is less likely, but this case is perhaps
more often directly relevant in practice.
6
Connecting Graphtropy with Algorithmic In-
formation
There are well known and interesting connections between the Shannon informa-
tion and the algorithmic information (the Kolmogorov complexity) [TSMA10]
[Zur89]. There turn out to be diﬀerent, also interesting connections between the
graphtropy and the algorithmic information.
Suppose the states represented by the nodes in the distinction graph G
are programs running on some universal computer U (such programs may be
represented, for example, as bit strings; though we will explore a little later the
possibility of expressing such programs natively within distinction graphs by
adding extra link types) Suppose the observer, who is making the distinctions
represented in the graph, has a ﬁxed algorithmic information content K. Then,
consider two nodes N1 and N2 with algorithmic information content M >> K.
The odds that the observer can distinguish N1 and N2 based on their contents
decrease as M increases. There are roughly 2M possibilities with algorithmic
information content = M, but the observer can only distinguish 2K at most;
so the odds that observer can distinguish two random nodes with algorithmic
information M is around 2K−M−1 (the odds that N1 and N2 lie in the same
one of the 2K−M partition cells).
Thus the probability of a link between N1 and N2 is 1 −2K−M−1 – a direct
relation between algorithmic information and graphtropy.
To sum up our conclusion: If the nodes in a graph represent randomly
chosen states with algorithmic information M, and the observer’s algorithmic
information is K, then the graphtropy is 1 −2K−M−1.
The graphtropy of a distinction graph, constructed relative to an observer,
is therefore considerable as a measure of how much excessive algorithmic infor-
mation exists in the system of observations modeled by the distinction graph,
relative to the observer. Or to put it more simply, the graphtropy measures
how much more complexity there is in the environment relative to
the observer.
If the nodes represent randomly chosen states with algorithmic info < M,
13


## Page 14


then a similar formula can be derived, and the same conceptual conclusion holds.
6.1
Graphtropic Energy
There is also a connection between these ideas and Tadaki’s [Tad08] 1 formu-
lation of the connection between algorithmic information theory and statistical
mechanics.
Recall that in our discussion of maximum entropy distributions
above, we assumed each node in our distinction graph was weighted with a
non-negative integer. If these integers vi are taken to represent the algorithmic
information content of a bit string or other state resident at each node i, then
we can interpret the sum
PN
i=1 vi
N
as a kind of “graph energy,” where the possible values taken by the algorithmic
information play the role of energy eigenstates in statistical mechanics. If the
possible values for the vi are Ej, then the graph energy may be rewritten
X
j
Ejp(Ej)
where p(Ej) denotes the percentage of nodes in the graph with vi = Ej.
Given a graph of this nature, in which each node holds a state possessing a
certain amount of algorithmic information, the graph energy corresponds
to the average algorithmic information across the nodes of the graph.
It may be interesting to explore the maximum entropy distribution according
to a constraint of ﬁxed average algorithmic information, and under various as-
sumptions regarding the distribution from which the distinction graph is drawn.
If the graph is a partition graph, then the maximum entropy distribution
takes the form of the standard Gibbs distribution, and the energy takes the
form of the “algorithmic energy” presented in [Tad08].
6.2
Graphtropic Temperature
An interesting feature of the analysis in [Tad08] is that the compression ratio
(the maximum compression ratio achievable by any computable program) is
shown to be a formal analogue of the temperature in thermodynamics: the
more compressible, the lower the temperature. For the Gibbs distribution in
thermodynamics, the temperature plays a role as a parameter determining the
variance of the distribution: higher temperature means less concentration of
the distribution in the most probable states. It is natural to ask whether the
role of the algorithmic temperature is similar in the case of distinction graphs.
This seems likely, although validating this rigorously would require some graph
combinatorics that we will not unfold here.
1see also [BS12] for related considerations
14


## Page 15


If we view nodes of the distinction graph as labeled with programs of ﬁxed
length S, then the compression ratio determines the connection probability. The
more compressible the program strings are, the greater the connection probabil-
ity; where, according to the logic sketched above, connection probability would
depend exponentially on compression ratio.
According to the logic outlined
above, if the nodes in a graph represent randomly chosen states with size S and
compressibility D, and the observer’s algorithmic information is K, then the
graphtropy is 1 −2K−S
D −1 = 1 −2K−12
S
D . Temperature guiding the concentra-
tion of the maximum likelihood distribution in its most probable states, then
means the same thing as graphtropy guiding the concentration in this way.
Speciﬁcally, suppose we have m (e.g. m = S
T diﬀerent values for the integer
weights on the N nodes (which may represent e.g. algorithmic informations of
the states at the nodes); and suppose we have a much large number of nodes
than values (N >> m). Then it seems intuitive that the maximum-likelihood
distribution is going to be at its ﬂattest when the connection probability is such
that each node connects to around m
N other nodes. If so, this would mean that,
roughly speaking, the maximum-likelihood distribution will tend to get ﬂatter
as the temperature descends toward m
N (which we have assumed is quite small).
As the connection probability goes below m
N , strange things may happen; but at
this point we are verging away from the statistical foundation of the concept of
temperature, because the temperature is getting around the granularity of the
weight values. In any case, these issues seem somewhat subtle and will beneﬁt
from detailed calculations.
7
Dynamic Distinction Graphs: a Phenomenology-
Based Computational Model
We now show how to extend the basic construct of a distinction graph to that
of a dynamic distinction graph (DDG), which incorporates a small number
of additional features suﬃcient to implement an elemental model of computing.
Unlike most computing models out there, the DDG model is fundamentally in-
spired by phenomenology rather than physical computing machinery or abstract
mathematics. Philosophically, we can think of DDG as a model of “cognitive
computation” – i.e. it is a computational model whose primitives are natural
mental operations. We believe it may be found natural for modeling dynamical
and computational phenomena at the border between classical and quantum
physics, and phenomena at the border between physical and cognitive opera-
tions (e.g. measurement and consciousness).
As in the above, we start with a ?distinction graph? in which node x is
linked to node y if the given observer can?t distinguish x from y. Here x and y
here are categories of observations, made by some observer.
An asymmetric link from x to y indicates that if an observer is observing
x, they can’t notice x changing into y. A symmetric link from x to y indicates
that both asymmetric links from x to y exist.
15


## Page 16


Then introduce degrees of distinction, where x is linked asymmetrically to y
with weight p if the given observer can distinguish x changing into y (1 −p)%
of the time.
Note that one can consider there to be an implicit time-scale here: some-
times an observer may notice x changing into y only if the change is suﬃciently
rapid, but not if the change occurs slowly. So in calculating the probability p,
some average over diﬀerent ways of changing is implicitly assumed, including
an average over rates of change. The basic model of the DDG, however, does
not depend on any speciﬁc assumptions made in this regard.
Next, introduce weights or counts for nodes, indicating how often observa-
tions classiﬁable as node x are encountered in the observer?s experience. These
weights may obviously be combined with the weights on distinction-graph links,
in standard probabilistic formulas such as Bayes’ rule.
So far we have something very similar to the underlying semantic model
of OpenCog’s Probabilistic Logic Networks framework [GIGH08].
If all the
speciﬁcs are deﬁned consistently, then the degree of distinction between x and
y will be a monotone (nonlinear) transformation of the strength of the PLN
Inheritance link between x and y. Because the Inheritance link measures what
percentage of x’s properties are shared by y, and clearly the larger this number
is, the smaller the chance that an observer can distinguish x changing into y.
To make the model dynamic, we next introduce the notion of increasing or
decreasing degrees of distinction – x or y may be “”getting more distinct” or
“getting less distinct.”
This enables us to introduce the notion of causal implication between links,
e.g. links embodying relationships such as
• If x and y get more distinct, then w and z get more distinct
• If x and y get more distinct, then w and z get less distinct
These implication links may have weights as well (and these weights will also
embody some assumptions about distribution over time-lags).
In the PLN framework, temporal and causal implication links may be tagged
with speciﬁc distributions over lengths of time, so that diﬀerent such links in
the same graph may pertain to diﬀerent time-distributions. This can also be
done within the DDG model as needed.
To get a general, abstract computation model out of this, we then let causal
implication links point to other causal implication links, so e.g. we have things
like
• If x and y get more distinct, then it becomes more strongly true that: If
w and z get more distinct, u and v get less distinct?
Note that grouping is basically there already as part of this framework.
If one has a set of nodes that are completely interconnected, then this set of
nodes can be treated as a whole within implications (because the nodes are
indistinguishable).
16


## Page 17


The operation of replacing a node with a completely connected subgraph
should also be considered a primitive (and it?s important because doing this
substitution sets the stage for the nodes in the subgraph to become less com-
pletely connected).
This is a simple computational model founded on a handful of basic phe-
nomenological primitives:
• distinct
• indistinct
• increasing
• decreasing
• cause = temporally-imply
• always / often / sometimes / rarely / never
The logic corresponding to this computational model via a Curry-Howard
style correspondence has not been worked out in detail, but would seem at ﬁrst
blush to be a simple ﬂavor of higher-order predicate logic.
Given an observed time-series of distinction graphs, rules such as the above
can be data-mined using probabilistic causal inference methods, and a DDG
model of the time-series can be reconstructed. This DDG can then be operated
going forward, as a simulation model corresponding to the observed time-series.
A node x in a DDG, plus the causal implication links associated with the
node, may be considered as a computational element; and its complexity may
be assessed simply by counting the number of causal implication links involved
(including links pointed to by higher-order links involving x, and so forth re-
cursively). The algorithmic information of a node in a distinction graph G then
consists of the minimal number of causal implication links needed to give the
node x the dynamics that it has in the graph G. The correspondences between
algorithmic information and graphtropy touched earlier can then be explored,
with all the computation-theoretic and information-theoretic action occurring
within the same distinction graphs enhanced with causal implication links.
7.1
Modeling Observers as Dynamic Distinction Graphs
DDGs allow us to bring the graphtropy model full circle, via dynamically mod-
eling an observer as a DDG, aka an enhanced distinction graph. An observer
A’s action of observation may be modeled by considering certain of A’s DDG’s
nodes as “sensors”, or by considering each of its DDG nodes as “sensory” to
a certain degree, some more than others. From the perspective of a second
observer B, which divides possible objects of sensation into categories, one can
then calculate whether A reacts the same way (in terms of the dynamics within
A’s DDG on exposure to sensations) to sensations in category x and category
y, and create the link between x and y in A’s distinction graph.
17


## Page 18


Similarly, B’s division of objects of sensation into categories may be under-
stood from the view of a third observer, C, who looks at the state of B’s DDG
upon exposure to these sensations, and notes if there are diﬀerences between
sensations in category x and category y, etc. One does not escape the ultimate
observer-dependence of all distinctions. But one can push it higher and higher
up the hierarchy, modeling observers, observers of observers, etc. using a simple
model of weighted distinctions associated with causal implications.
8
The Second Law of Thermodynamics on Dis-
tinction Graphs
The distinction-graph approach provides a new view of the law of entropy non-
decrease, making clearer the assumptions on which it rests as regards the ob-
server’s cognitive structure and relationship to the world.
Let us begin with the Second Law as formulated in terms of partitions. We
will move to more general distinction graphs a little later.
As Baranger [Bar00] and others have argued, the standard Second Law of
Thermodynamics is rooted in the simple fact that, in a complex dynamical
system, it will often happen that two states in the same partition cell at time
t end up in diﬀerent partition cells at time t + 1. Each such event increases
the entropy of the overall partition; in terms of logical entropy it increases the
number of dits.
On the other hand, one may also ask: If two states in diﬀerent partition cells
at time t end up in the same partition cell at time t + 1, does this not decrease
the number of dits, the amount of entropy?
The key is to introduce the notion of an observer with a memory. Suppose we
assume our observer has a long-term memory comprising a series of partitions,
one at each point in time; and that the observer cross-indexes these partitions,
so that it considers the same nodes to exist in the partitions associated with
diﬀerent times. In general one can consider observers for whom the partitions
at diﬀerent times may involve overlapping but not identical node-sets; but for
simplicity, let us now restrict attention to the case where the partitions at
diﬀerent times involve the same node-set.
Let us associate a “memory meta-partition” with the observer: in the meta-
partition, two nodes go in diﬀerent partition cells if they have ever (in the
observer’s memory) gone in diﬀerent partition cells. That is to say, the observer’s
memory meta-partition is the lattice join of the time-speciﬁc partitions in the
observer’s memory.
In this case:
• When two nodes in the same cell at time t end up in diﬀerent cells at time
t+ 1, they are then in diﬀerent cells in the memory meta-partition forever
after, so the number of dits in the memory meta-partition has increased
• When two nodes in diﬀerent cells at time t end up in the same cells at
18


## Page 19


time t + 1, they remain in diﬀerent cells in the memory meta-partition; so
the number of dits in the memory meta-partition has not decreased
Clearly, we then have a “Second Law of Thermodynamics” for the meta-partition:
the entropy will never decrease and will often increase.
A similar argument holds if we forget about partitions and just look at
distinction graphs. If we introduce a memory graph that consists of the join of
a series of historical distinction graphs, we will ﬁnd that this join loses but does
not accumulate links. So the graphtropy of the observer’s memory graph
will never decrease, and based on the observer’s experience will generally
eventually increase. This is a graphtropic version of the Second Law.
Of course, this conclusion will not hold exactly for a real observer, because
a real observer will forget things, and this forgetting will cause previously noted
distinctions to disappear in its memory graph. Also a real observer can develop
and get modiﬁed in profound ways which result in introducing new nodes into
its memory graph. But the conclusion is nevertheless interesting.
This perspective on the Second Law makes clear that it relies on an assump-
tion about the operation of memory. Suppose our observer had precognition
and thus, in its memory meta-partition, marked two nodes as distinguishable
if they ever, in past or future, were distinguishable. In this case, the memory
meta-partition would not change over time and there would be no Second Law.
However, if its precognition were weaker or more erroneous than its ordinary
memory, then one would still have a probabilistic Second Law.
8.1
Object Persistence and the Second Law
It is interesting to dig a little deeper here. a ﬁrst step is to look at what happens
if we have probabilistic distinctions and weighted distinction graphs; and thus
a probabilistically weighted memory graph.
In this case, to get the Second
Law according to the above argument, what we need is some sort of auxiliary
assumption such as
• Each time two nodes are viewed as distinct, this decreases the weight on
their link in the weighted memory distinction graph.
• But when two nodes are viewed as the same, this does not increase the
weight on their link as much; because it is assumed that their existing
diﬀerences are simply not being observed at that time.
But this starts to seem a little suspicious.
Why is it, actually that we as-
sume previously observed distinctions are permanent, but previous observed
non-distinctions are temporary?
To understand this better we need to ask: What does it mean to identify
“nodes” observed at diﬀerent points in time, in one’s memory graph?
To say that a node at observed during interval t and a node bs observed
during interval s represent the same entity, is presumably to say that there are
observed patterns of interrelationship (with other nodes) that are common to
19


## Page 20


at and bs. We could represent these interrelationships in a graph framework,
e.g. by introducing hyperlinks between nodes to represent relationships of the
form e ∗f = h where ∗is a combinatory operator.
For instance, if we are modeling nodes as harboring bit-strings encoding
programs, e ∗f might be interpreted as the output resultant from running the
program at e with the program at f as input; saying e ∗f = h then means that
running e’s program with f’s program as input results in h’s program. The
identiﬁcation of at with bs is then a statement that the two nodes are involved
in similar sets of ternary links; where, two ternary links are judged as similar
if they point between similar nodes (where nodes harboring the same program
count as similar, providing a base case for the recursive deﬁnition).
In the Dynamic Distinction Graph framework introduced above, the “ternary
links” here are simply causal implication links. So one can consider two nodes
in a DDG as similar if they are involved in similar causal implication links.
Similarity of two causal implication links may then be gauged partly in terms
of similarity of the nodes they point to, which is a recursion, but not a vicious
one; it’s the kind of recursion that PLN deals with routinely.
In this framework, the (graphtropic) Second Law then (speaking just a bit
loosely) appears to ensue from the assumption that
• observing a ternary link e ∗f = h at a certain time , increases the odds
that another similar ternary link will be observed in future
• the fact of not observing a ternary link e∗f = h at a certain time, increases
the odds that no link similar to this one will be observed in future – but
by a smaller amount
This assumption appears to follow if one assumes that
• The observer’s window into the world during any interval of time is quite
incomplete (so that not seeing something at some moment, is not a good
indicate that said thing does not exist)
• The world is not utterly random but has some continuity over time – so
that the relationships existing at one point in time have a better odds of
existing in the future, as compared to comparable randomly selected sets
of relationships
These both seem quite reasonable assumptions in a commonsensical context.
The second assumption is related to what Peirce called the “tendency to take
habits” [Pei91] and Lee Smolin called the “precedence principle” [Smo12]. In a
basic physics context it seems to ensue from such things as special relativity and
the conservation of momentum and energy, which tend to keep many systems
stable over time and prevent the world from looking like a random succession
of utterly disconnected situations.
What one gets from boiling down the Second Law to a very basic level
of observations and distinctions, is a clearer understanding of the cognitive
assumptions on which it rests.
20


## Page 21


8.2
Graphtropy, States of Consciousness and Intelligence
These reﬂections on the Second Law evoke a connection between graphtropy
and consciousness theory, which is in turn somewhat revelatory regarding the
nature of intelligence, admittedly in on a speculative level.
From the perspective of consciousness theory, it seems that graphtropy is a
measure of the “individuation” associated with a state of consciousness. Mini-
mum graphtropy occurs when everything is perceived as identical to everything
else (an “oceanic state” of total “oneness” [Wer86]); and maximum graphtropy
occurs when everything is viewed as distinct from everything else.
Real-world intelligent systems are necessarily somewhere between these ex-
tremes. Seeing everything as identical will not lead to interesting complex adap-
tive behaviors with high probability. On the other hand, real environments have
too much complexity for any realistic bounded-resources intelligence to make all
possible distinctions. So real-world-intelligent systems will display intermediate
graphtropy, in their internal cognitive distinction graphs. This corresponds to
our ordinary states of consciousness in which each experienced entity is merged
into other highly (subjectively) similar entities, but not directly into all other
entities.
The heuristic derivation of the graphtropic Second Law given above, de-
pended on the assumption that the observer’s memory graph was the join of
his past memory graphs. But of course, this is not realistic in practice, since
any real-world observer is going to have a memory that is very limited in size
compared to the total sum of its historical perceptions. In practice some past
distinctions are going to be forgotten. This suggests that the Second Law need
not hold for real-world cognitive systems – i.e. the graphtropy of a real-world
intelligent system’s distinction graph need not steadily increase ... it may go up
and down as the system learns and forgets.
Forgetting gives rise to the need for complex reasoning. The practical in-
ability to store and recall all of one’s past particular distinctions, leads a system
to generate abstractions, which can then be used to imperfectly and probabilis-
tically reconstitute past distinctions and to imperfectly and probabilistically
apply the lessons of the totality of past distinctions to the future. Intelligence is
a way of coping with the same memory imperfections that violate the assump-
tions leading to derivation of the Second Law. Intelligence has to do with the
regulation of the ongoing gain and loss of distinctions that keeps the graphtropy
of a complex adaptive system, most of the time, within reasonable homeostatic
bounds, and in states of consciousness that are neither purely individuated nor
fully oceanic.
These observations are not in themselves especially informative about the
detailed aspects of real-world intelligent systems. From the high-level perspec-
tive given here, about all we can say in this regard is that speciﬁc environments
will tend to lead to the survival of systems with speciﬁc patterns of remember-
ing and abstracting – which is rather obvious and uninteresting. The concepts
given here do connect naturally with the train of thought presented in [Goe09],
in which the structure and dynamics of human-like minds is viewed as emerging
21


## Page 22


from the need to achieve complex goals involving embodied communication, in
environments heavily populated by other embodied communicating agents. But
for the purposes of the present paper, it is suﬃcient to observe that our treat-
ment of graphtropy and its relation to observation in a physics context, does
ﬁt naturally and sensibly with models of cognition as a complex adaptive self-
organizing process, and with models of the states of consciousness associated
with cognitive systems.
8.3
Maximum Entropy Production
Another intriguing “thermodynamic law” related to entropy is the “maximum
entropy production principle,” which states that, in many cases, a complex
system will maximize the rate of entropy production. The precise conditions
under which this principle holds appear complex and are still under investigation
from a variety of perspectives [MS06]. The graphtropy perspective provides a
diﬀerent, in some ways simpler and more revealing view.
“Graphtropy production” may be deﬁned as the rate of increase of graph-
tropy. Consider a time series of distinction graphs, with the same nodes but
possibly diﬀerent links at diﬀerent times. In a non-weighted distinction graph,
then, the graphtropy production is simply the number of links removed per unit
time. In a weighted distinction graph, it is the average decrease of link weight
per unit time.
Going back to the simple model introduced above in the analysis of the
Second Law, we see that what determines the rate of graphtropy production,
is the rate of identiﬁcation of new ternary relationships that diﬀerentiate nodes
a and b – i.e. so that a and b would have appeared less diﬀerentiated if not
for the new ternary relationships. The more diﬀerentiations that are discovered
and recorded in the memory graph, the more graphtropy.
To see why, under reasonable assumptions, the rate of graphtropy production
might be maximized, let us return to the logic of partitions. A property of nodes,
such as for example
P 2
a (c) = ∃a ∈NG : a ∗x = c
can be viewed as a partition of the set of nodes into two categories: those nodes
for which the property holds, and those for which it doesn’t. a fuzzy property
can be viewed as a fuzzy partition also; but let’s stick with strict properties for
right now.
So, suppose a system experiences a number of events over a certain interval
of time, and that each of these events can be represented as a ternary link in
the manner described above. Each ternary link a ∗b = c deﬁnes six properties
in a natural way: the property Pa described above has a reverse
P 2∗
c (a) = ∃a ∈NG : a ∗x = c
and then there are the two properties
22


## Page 23


P 3
a (b) = ∃a ∈NG : a ∗b = x
P 1
b (c) = ∃a ∈NG : x ∗b = c
and their reverses P 3∗
b (a), P 1∗
c (b).
So, each event that occurs creates 6 binary divisions of the nodes, according
to each of these 6 properties. If there are M events altogether, then we have at
maximum 6M binary divisions of the nodes, which in general divides the set of
nodes into 26M partition cells, based on combinations of the properties implied
by the events.
Now suppose we consider a 26M dimensional probability vector, with a prob-
ability pi for each cell. If the number of nodes in the graph satisﬁes N >> 26M,
then we have a statistical-thermodynamics type situation. Lacking additional
constraints, the probability vector corresponding to the greatest number of mi-
crostates is going to be the one that makes each of these partition cells roughly
equally numerous.
If N is not quite big enough for this, we can look at binary or ternary
combinations of properties only; for instance, looking at binary combinations
only gives us a (6M)2 dimensional probability vector instead, which is much
more reasonable; N > (6M)2 looks more like an assumption that can commonly
be fulﬁlled in practice.
In short, then: If we assume a system is having a bunch of random inter-
actions during an interval of time, the most likely case is the one in which the
Shannon entropy of the set of distinctions created by the interactions (from the
perspective of an observer who sees all the interactions) is maximal. This is also
of course the set of distinctions for which the logical entropy is maximal.
Next, if we have an observer watching all these interactions over time, and
remembering them, we will have a situation in which the entropy of the sys-
tem from the perspective of the observer is increasing very rapidly, because
new distinctions keep getting added. In other words, we see maximum entropy
production.
The modeling of events in terms of ternary interactions on a graph is not
natural for all real-world situations (though it is adequate to model all com-
putable dynamical systems and, under some interpretations, others as well).
However, we have introduced this speciﬁc model here mostly as a simple way
to make a conceptual point. The key concept here is that: From the point
of view of an observer watching a complex system change, the ob-
served system will often demonstrate maximum entropy production
because: The most likely scenario is for the events the system experi-
ences to implicitly keep giving rise to system properties that overlap
in a maximally entropic way.
The argument becomes more tedious to state, but the same conclusion ap-
pears to hold for the case of graphtropy production on intransitive distinction
graphs.
23


## Page 24


Of course, if we take the ternary-interaction model of events, we conclude
that eventually all possible properties of the 6 types described above (deﬁned
relative to nodes in the graph) will have occurred, so that the entropy will stop
increasing. But this takes us out of the “statistical” scenario where a rule like
maximum entropy production makes sense. In the ternary-interaction model,
one must consider the “environment” of a system as part of a larger system; so
that what is thought of as a “large heat bath” in classical thermodynamics in
this perspective just takes the form of more and more nodes in the distinction
graph.
9
Quantum Graphtropy
Ellerman has extended the logical entropy to the quantum case, deﬁning the
“quantum logical entropy” of a mixed state essentially as the degree of impurity
of the corresponding density matrix [Ell16].
One can extend graphtropy to
the quantum case in a somewhat similar way, learning something about the
semantics of quantum measurement in the process.
9.1
Quantum Distinction Graphs as a Representation of
Mixed States
Quantum logic, it is often said [SKZ13], should be used by an observer to rea-
son about things that this observer cannot in principle observe. It follows from
this that: Quantum logic is how an observer should reason about potential dis-
tinctions between things that it cannot distinguish from each other. However,
non-distinguishability by an observer is not necessarily a transitive property of
potential distinctions. Speculatively, we suggest that perhaps weak quantum
coherence may be eﬀectively modeled in terms of distinction graphs where dis-
tinction is nontransitive in regard to the relevant observers. [Rie11] [LLC+12].
If N1 and N2 are linked in a distinction graph deﬁned relative to a certain
observer, then this observer should reason about their relationship using quan-
tum logic. What if N1 and N2 are linked, and N2 and N3 are non-linked, but
N1 and N3 are not? Then the quantum conclusion about N1 and N3 obtained
from reasoning about their relation with N2, has got to be consistent with the
non-quantum conclusion obtained from reasoning about N1 and N3 based on
direct observation.
If the nodes in the graph represent quantum histories, so that the graph rep-
resents a “mixed quantum history”, then the graphtropy represents the prob-
ability of getting diﬀerent results in two independent measurements with the
same observable and the same pure state. That is, graphtropy is a measure of
impurity in a set of complexly related observables.
The full apparatus of graphtropy outlined above then applies to the case of
a graph whose nodes represent quantum histories; one “merely” has a diﬀerent
interpretation.
24


## Page 25


9.2
Quangraphtropy
John Baez and Blake Pollard have introduced the notion of quantropy [BP15],
a complex-variable version of the entropy, and have shown that the quantropy
connects to basic quantum mechanics in a similar way to how Shannon en-
tropy connects to classical thermodynamics. Using overlapping mathematics, a
complex-variable graphtropy (“quangraphtropy”) can be connected to quantum
mechanics in a conceptually suggestive way.
Suppose we have a complex number (the action) associated with each node
on the graph G. Suppose these are normalized so that their sum across the
graph is 1; and suppose we have a constraint on the expected action,
X
x∈NG
A(x)a(x) = ⟨a⟩
What we can then ask is: given the distinguishability relationships between
the states in the graph, what is the most likely graph consistent with the con-
straints? This will be the graph that, consistent with the constraints, has the
greatest number of automorphisms (where we are concerned only with automor-
phisms that map a node x with action a(x) into another node with a(x) = a(y)).
In a simple situation (a large partition graph), this will come out the same
as in quantropy formulation of quantum theory.
But what if the graph is not a partition graph? Then the most likely graph
will be more complex, representing a set of non-transitive ”distinguishability”
relationships between observable entities. Since in the quantum context, non-
distinguishability implies entanglement, the most likely situation will then be
a complex web in which various entities are non-transitively entangled with
each other; i.e. with respect to a particular observer, A may be signiﬁcantly
entangled with B, and y signiﬁcantly entangled with C, but a not signiﬁcantly
entangled with C.
This sort of intransitivity is not that odd of a phenomenon; entanglement is
a type of correlation, and correlations are not generally transitive. For instance,
it can happen that several particles are entangled, yet if you ignore some of the
particles, the remaining pair is not entangled. But these quantum distinction
graphs constitute a particularly simple way to model webs of intransitive entan-
glement. It seems this may perhaps be an interesting way of modeling systems
at the boundary between quantum and classical, i.e. systems displaying “weak
quantum coherence.”
9.3
Quantum Dynamic Distinction Graphs
One can also articulate a quantum-computational version of a DDG, whose
causal implication links involve; complex-number directional values, such as
• If x and y get more distinct in direction a, then w and z get more distinct
in direction b (by multiplier α)
25


## Page 26


• If x and y get more distinct in direction a, then w and z get less distinct
in direction b (by multiplier α)
It is not hard to see that enaction of such causal implication links is equivalent
to multiplication of a complex number matrix by the complex number values
associated with the nodes in the network. If the nodes represent quantum histo-
ries, evolving according to a unitary matrix as happens in quantum mechanics,
then the entries in the unitary matrix will imply the multipliers. Conversely, a
suﬃciently complete set of such causal implication links will allow one to derive
the unitary matrix driving the quantum system’s evolution; or a less complete
set of such causal implication links will imply a probability distribution over
unitary quantum evolution matrices.
10
Conclusion
Beginning from a very simple foundation (connection probability as a kind of
entropy) we have explored a great variety of diﬀerent concepts; some fairly
straightforward and clearly-demonstrated, others more digressive and specula-
tive. For certain, more questions have been raised than answers provided. Our
hope is that graphtropy, as outlined here, will prove a promising direction for
diverse investigations.
While the math of graphtropy and distinction graphs is fascinating in itself,
our primary motivation for exploring in this direction has been more philosoph-
ical and conceptual. Given the intuition that “information” is a foundational
concept, both in physics and in psychology, one is drawn to try to understand,
at bottom, what information is. Communication theory, thermodynamics and
quantum mechanics provide intriguing clues but appear not to get at the crux
of the issue.
The crux of the matter of information, we suggest, is the body of distinc-
tions made by a particular observer. This body of distinctions may be modeled
as a graph, and may be quantiﬁed in various ways.
The graphtropy is one
particularly interesting quantiﬁcation, which reduces to more standard entropy
notions (Ellerman’s logical entropy, which relates with Shannon entropy in clear
ways) under special assumptions. Graphtropy relates naturally to phenomeno-
logical aspects of states of consciousness (e.g. degree of “oceanic”-ness). The
graphtropy perspective also clariﬁes the semantics of quantum distinctions, via
constructions like the “quangraphtropy” and quantum DDGs. Exploring con-
cepts like maximum entropy and maximum entropy production in the context
of distinction graphs leads to some complex mathematics and unresolved par-
ticulars, but appears a promising direction.
Overall, we believe these preliminary investigations lend weight to the idea
that, in order to understand the fundamental meaning of information and to
better comprehend the application of information in various disciplines, one
should carefully ground one’s informational calculations and constructions in
distinction graphs formed to represent the perspectives of particular observers.
26


## Page 27


Observers may also be modeled in terms of the distinctions they embody, and
the causal relations between their embodied distinctions at various points in
time, pointing toward a perspective in which a small number of primitive con-
cepts (distinction, probability, time, causation) suﬃce to model the complex
informational structures and dynamics of the physical and cognitive world.
References
[Bar00]
Michel Baranger. Chaos, complexity, and entropy. New England
Complex Systems Institute, Cambridge, 2000.
[Bat79]
Gregory Bateson. Mind and nature: A necessary unity. Dutton New
York, 1979.
[BP15]
John C Baez and Blake S Pollard. Quantropy. Entropy, 17(2):772–
789, 2015.
[Bro69]
George Spencer Brown. Laws of form. Allen & Unwin London, 1969.
[BS12]
John Baez and Mike Stay. Algorithmic thermodynamics. Mathe-
matical Structures in Computer Science, 22(5):771–787, 2012.
[Ell13]
David Ellerman. An introduction to logical entropy and its relation
to shannon entropy, 2013.
[Ell16]
David Ellerman. On classical and quantum logical entropy. 2016.
[GIGH08] B. Goertzel, M. Ikle, I. Goertzel, and A. Heljakka. Probabilistic Logic
Networks. Springer, 2008.
[Goe09]
Ben Goertzel. The embodied communication prior: A characteriza-
tion of general intelligence in the context of embodied social inter-
action. In Cognitive Informatics, 2009. ICCI’09. 8th IEEE Interna-
tional Conference on, pages 38–43. IEEE, 2009.
[IK16]
Joel Isaacson and Louis H Kauﬀman. Recursive distinctioning. arXiv
preprint arXiv:1606.06965, 2016.
[Kau87]
Louis H Kauﬀman. Self-reference and recursive forms. Journal of
Social and Biological Structures, 10(1):53–72, 1987.
[LLC+12] Che-Ming Li, Neill Lambert, Yueh-Nan Chen, Guang-Yin Chen, and
Franco Nori. Witnessing quantum coherence: from solid-state to
biological systems. Scientiﬁc reports, 2:885, 2012.
[Llo06]
Seth Lloyd. Programming the universe: a quantum computer scien-
tist takes on the cosmos. Vintage Books, 2006.
27


## Page 28


[MS06]
LM Martyushev and VD Seleznev.
Maximum entropy produc-
tion principle in physics, chemistry and biology.
Physics reports,
426(1):1–45, 2006.
[Pei91]
Charles S Peirce. The architecture of theories. The Monist, pages
161–176, 1891.
[Rie11]
Elisabeth Rieper. Quantum Coherence in Biological Systems. PhD
thesis, 2011.
[SKZ13]
Maximilian Schlosshauer, Johannes Koﬂer, and Anton Zeilinger.
A snapshot of foundational attitudes toward quantum mechanics.
Studies in History and Philosophy of Science Part B: Studies in
History and Philosophy of Modern Physics, 44(3):222–230, 2013.
[Smo12]
Lee Smolin. Precedence and freedom in quantum physics. arXiv
preprint arXiv:1205.3707, 2012.
[Tad08]
Kohtaro Tadaki. A statistical mechanical interpretation of algorith-
mic information theory. arXiv preprint arXiv:0801.4194, 2008.
[TSMA10] Andreia Teixeira, Andre Souto, Armando Matos, and Luis Antunes.
Entropy measures vs. algorithmic information. In Information The-
ory Proceedings (ISIT), 2010 IEEE International Symposium on,
pages 1413–1417. IEEE, 2010.
[Wal00]
Peter Walley.
Towards a uniﬁed theory of imprecise probability.
International Journal of Approximate Reasoning, 24(2-3):125–148,
2000.
[Wer86]
David S Werman. On the nature of the oceanic experience. Journal
of the American Psychoanalytic Association, 34(1):123–139, 1986.
[Zur89]
Wojciech H Zurek. Algorithmic randomness and physical entropy.
Physical Review A, 40(8):4731, 1989.
28

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1902_00741v1_distinction_graphs_and_graphtropy_a_formalized_phenomenological_layer_underlyin
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1902_00741V1_DISTINCTION_GRAPHS_AND_GRAPHTROPY_A_FORMALIZED_PHENOMENOLOGICAL_LAYER_UNDERLYIN.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

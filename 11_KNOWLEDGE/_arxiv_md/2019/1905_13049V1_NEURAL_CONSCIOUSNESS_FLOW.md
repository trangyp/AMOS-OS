---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.13049v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1905.13049v1_Neural_Consciousness_Flow

> Source: 1905.13049v1_Neural_Consciousness_Flow.pdf

> Pages: 30

---


## Page 1


Neural Consciousness Flow
Xiaoran Xu1, Wei Feng1, Zhiqing Sun2, Zhi-Hong Deng2
1Hulu LLC, Beijing, China
{xiaoran.xu, wei.feng}@hulu.com
2Peking University, Beijing, China
{1500012783, zhdeng}@pku.edu.cn
Abstract
The ability of reasoning beyond data ﬁtting is substantial to deep learning systems
in order to make a leap forward towards artiﬁcial general intelligence. A lot of
efforts have been made to model neural-based reasoning as an iterative decision-
making process based on recurrent networks and reinforcement learning. Instead,
inspired by the consciousness prior proposed by Yoshua Bengio [1], we explore
reasoning with the notion of attentive awareness from a cognitive perspective, and
formulate it in the form of attentive message passing on graphs, called neural
consciousness ﬂow (NeuCFlow). Aiming to bridge the gap between deep learning
systems and reasoning, we propose an attentive computation framework with
a three-layer architecture, which consists of an unconsciousness ﬂow layer, a
consciousness ﬂow layer, and an attention ﬂow layer. We implement the NeuCFlow
model with graph neural networks (GNNs) and conditional transition matrices.
Our attentive computation greatly reduces the complexity of vanilla GNN-based
methods, capable of running on large-scale graphs. We validate our model for
knowledge graph reasoning by solving a series of knowledge base completion
(KBC) tasks. The experimental results show NeuCFlow signiﬁcantly outperforms
previous state-of-the-art KBC methods, including the embedding-based and the
path-based. The reproducible code can be found by the link1 below.
1
Introduction
To discover the mystery of consciousness, several competing theories [2, 3, 4, 5] have been proposed
by neuroscientists. Despite their contradictory claims, they share a common notion that consciousness
is a cognitive state of experiencing one’s own existence, i.e. the state of awareness. Here, we do not
refer to those elusive and mysterious meanings attributed to the word "consciousness". Instead, we
focus on the basic idea, awareness or attentive awareness, to derive a neural network-based attentive
computation framework on graphs, attempting to mimic the phenomenon of consciousness to some
extent.
The ﬁrst work to bring the idea of attentive awareness into deep learning models, as far as we know,
is Yoshua Bengio’s consciousness prior [1]. He points out the process of disentangling higher-level
abstract factors from full underlying representation and forming a low-dimensional combination
of a few selected factors or concepts to constitute a conscious thought. Bengio emphasizes the
role of attention mechanism in expressing awareness, which helps focus on a few elements of state
representation at a given moment and combining them to make a statement, an action or policy. Two
recurrent neural networks (RNNs), the representation RNN and the consciousness RNN, are used to
summarize the current and recent past information and encode two types of state, the unconscious
state denoted by a full high-dimensional vector before applying attention, and the conscious state by
a derived low-dimensional vector after applying attention.
1https://github.com/netpaladinx/NeuCFlow
Preprint. Under review.
arXiv:1905.13049v1  [cs.AI]  30 May 2019


## Page 2


Inspired by the consciousness prior, we develop an attentive message passing mechanism. We model
query-dependent states as motivation to drive iterative sparse access to an underlying large graph and
navigate information ﬂow via a few nodes to reach a target. Instead of using RNNs, we use two GNNs
[6, 7] with node state representations. Nodes sense nearby topological structures by exchanging
messages with neighbors, and then use aggregated information to update their states. However, the
standard message passing runs globally and uniformly. Messages gathered by a node can come from
possibly everywhere and get further entangled by aggregation operations. Therefore, we need to draw
a query-dependent or context-aware local subgraph to guide message passing. Nodes within such a
subgraph are densely connected, forming a community to further exchange and share information,
reaching some resonance, and making subsequent decisions collectively to expand the subgraph
and navigate information ﬂow. To support such attentive information ﬂow, we design an attention
ﬂow layer above two GNNs. One GNN uses the standard message passing over a full graph, called
unconsciousness ﬂow layer, while the other GNN runs on a subgraph built by attention ﬂow, called
consciousness ﬂow layer. These three ﬂow layers constitute our attentive computation framework.
We realize the connection between attentive awareness and reasoning. A reasoning process is
understood as a sequence of obvious or interpretable steps, either deductive, inductive, or abductive,
to derive a less obvious conclusion. From the aspect of awareness, reasoning requires computation
to be self-attentive or self-aware during processing in a way different from ﬁtting by a black box.
Therefore, interpretability must be one of the properties of reasoning. Taking KBC tasks as an
example, many embedding-based models [8, 9, 10, 11, 12, 13] can do a really good job in link
prediction, but lacking interpretation makes it hard to argue for their reasoning ability. People who
aim at knowledge graph reasoning mainly focus on the path-based models using RL [14, 15, 16, 17]
or logic-like methods [18, 19] to explicitly model a reasoning process to provide interpretations
beyond predictions. Here, instead, we apply a ﬂow-based attention mechanism, proposed in [20],
as an alternative to RL for learning composition structure. In a manner of ﬂowing, attention can
propagate to cover a broader scope and increase the chance to hit a target. It maintains an end-to-end
differentiable style, contrary to the way RL agents learn to choose a discrete action.
Other crucial properties of reasoning include relational inductive biases and iterative processing.
Therefore, GNNs [6, 7] are a better choice compared to RNNs for encoding structured knowledge
explicitly. Compared with the majority of previous GNN literature, focusing on the computation side,
making neural-based architectures more composable and complex, we put a cognitive insight into
it under the notion of attentive awareness. Speciﬁcally, we design an attention ﬂow layer to chain
attention operations directly with transition matrices, parallel to the message-passing pipeline to get
less entangled with representation computation. This gives our model the ability to select edges step
by step during computation and attend to a query-dependent subgraph, making a sharper prediction
due to the disentanglement. These extracted subgraphs can reduce the computation cost greatly. In
practice, we ﬁnd our model can be applied to very large graphs with millions of nodes, such as the
YAGO3-10 dataset, even running on a single laptop.
Our contributions are three-fold: (1) We propose an attentive computation framework on graphs,
combining GNNs’ representation power with explicit reasoning pattern, motivated by the cognitive
notion of attentive awareness. (2) We exploit query-dependent subgraph structure, extracted by
an attention ﬂow mechanism, to address two shortcomings of most GNN implementations: the
complexity and the non-context-aware aggregation schema. (3) We design a speciﬁc architecture for
KBC tasks and demonstrate our model’s strong reasoning capability compared to the state of the art,
showing that a compact query-dependent subgraph is better than a path as a reasoning pattern.
2
Related Work
KBC and knowledge graph reasoning. Early work for KBC, including TransE [8] and its analogues
[21, 22, 23], DistMult [9], ConvE [10] and ComplEx [11], focuses on learning embeddings of entities
and relations. Some recent work of this line [12, 13] achieves high accuracy, yet unable to explicitly
deal with compositional relationships that is crucial for reasoning. Another line aims to learn inference
paths [14, 24, 25, 26, 27, 28] for knowledge graph reasoning, such as DeepPath [15], MINERVA
[16], and M-Walk [17], using RL to learn multi-hop relational paths over a graph towards a target
given a query. However, these approaches, based on policy gradients or Monte Carlo tree search,
often suffer from low sample efﬁciency and sparse rewards, requiring a large number of rollouts or
2


## Page 3


Figure 1: Illustration for the three-layer attentive computation framework. The bottom is a uniﬁed
unconsciousness ﬂow layer, the middle contains small disentangled subgraphs to run attentive message
passing separately, constituting a consciousness ﬂow layer, and the top is an attention ﬂow layer for
extracting local subgraph structures.
running many simulations, and also the sophisticated reward function design. Other efforts include
learning soft logical rules [18, 19] or compostional programs [29] to reason over knowledge graphs.
Relational reasoning by GNNs and attention mechanisms. Relational reasoning is regarded
as the key component of humans’ capacity for combinatorial generalization, taking the form of
entity- and relation-centric organization to reason about the composition structure of the world
[30, 31, 32, 33, 34]. A multitude of recent implementations [7] encode relational inductive biases
into neural networks to exploit graph-structured representation, including graph convolution networks
(GCNs) [35, 36, 37, 38, 39, 40, 41, 42] and graph neural networks [6, 43, 44, 45, 46], and overcome
the difﬁculty to achieve relational reasoning for traditional deep learning models. These approaches
have been widely applied to accomplishing real-world reasoning tasks (such as physical reasoning
[45, 47, 48, 49, 50, 51], visual reasoning [44, 51, 52, 53, 54], textual reasoning [44, 55, 56], knowledge
graph reasoning [41, 57, 58], multiagent relationship reasoning [59, 60], and chemical reasoning [46]),
solving algorithmic problems (such as program veriﬁcation [43, 61], combinatorial optimization
[62, 63, 64], state transitions [65], and bollean satisﬁability [66]), or facilitating reinforcement
learning with the structured reasoning or planning ability [67, 68, 49, 50, 69, 70, 71]. Variants of
GNN architectures have been developed with different focuses. Relation networks [44] use a simple
but effective neural module to equip deep learning models with the relational reasoning ability, and its
recurrent versions [55, 56] do multi-step relational inference for long periods; Interaction networks
[45] provide a general-purpose learnable physics engine, and two of its variants are visual interaction
networks [51] learning directly from raw visual data, and vertex attention interaction networks [60]
with an attention mechanism; Message passing neural networks [46] unify various GCNs and GCNs
into a general message passing formalism by analogy to the one in graphical models.
Despite the strong representation power of GNNs, recent work points out its drawbacks that limit its
capability. The vanilla message passing or neighborhood aggregation schema cannot adapt to strongly
diverse local subgraph structure, causing performance degeneration when applying a deeper version
or running more iterations [72], since a walk of more steps might drift away from local neighborhood
with information washed out via averaging. It is suggested that covariance rather than invariance
to permutations of nodes and edges is preferable [73], since being fully invariant by summing or
averaging messages may worsen the representation power, lacking steerability. In this context, our
model expresses permutation invariance under a constrained compositional transformation according
to the group of possible permutations within each extracted query-dependent subgraph rather than the
underlying full graph. Another drawback is the heavy computation complexity. GNNs are notorious
for its poor scalability due to its quadratic complexity in the number of nodes when graphs are fully
connected. Even scaling linearly with the number of edges by exploiting structure sparsity can still
cause trouble on very large graphs, making selective or attentive computation on graphs so desirable.
Neighborhood attention operation can alleviate some limitation on GNNs’ representation power by
specifying different weights to different nodes or nodes’ features [74, 60, 53, 75]. These approaches
often use multi-head self-attention to focus on speciﬁc interactions with neighbors when aggregating
messages, inspired by [76, 77, 78] originally for capturing long range dependencies. We notice that
most graph-based attention mechanisms attend over neighborhood in a single-hop fashion, and [60]
claims that the multi-hop architecture does not help in experiments, though they expect multiple hops
to offer the potential to model high-order interaction. However, a ﬂow-based design of attention in
[20] shows a promising way to characterize long distance dependencies over graphs, breaking the
isolation of attention operations and stringing them in chronological order by transition matrices, like
the spread of a random walk, parallel to the message-passing pipeline.
3


## Page 4


Query:
(head, rel, ?)
Aggr
Op
...  
Pooling or returning the last
...  
Aggr
Op
...  
Attd
Op
...
Unconsciousness Flow
Consciousness Flow
Sparse 
Transition
One
Batch
Attention Flow
...  
Figure 2: The neural consciousness ﬂow architecture.
It is natural to extend relational reasoning to graph structure inference or graph generation, such as
reasoning about a latent interaction graph explicitly to acquire knowledge of observed dynamics [48],
or learning generative models of graphs [79, 80, 81, 82]. Soft plus hard attention mechanisms may be
a better alternative to probabilistic models that is hard to train with latent discrete variables or might
degenerate multi-step predictions due to the inaccuracy (biased gradients) of back-propagation.
3
NeuCFlow Model
3.1
Attentive computation framework
We extend Bengio’s consciousness prior to graph-structured representation. Conscious thoughts
are modeled by a few selected nodes and their edges, forming a context-aware subgraph, cohesive
with sharper semantics, disentangled from the full graph. The underlying full graph forms the initial
representation, entangled but rich, to help shape potential high-level subgraphs. We use attention ﬂow
to navigate conscious thoughts, capturing a step-by-step reasoning pattern. The attentive computation
framework, as illustrated in Figure 1, consists of: (1) an unconsciousness ﬂow (U-Flow) layer, (2) a
consciousness ﬂow (C-Flow) layer, and (3) an attention ﬂow (A-Flow) layer, with four guidelines to
design a speciﬁc implementation as follows:
• U-Flow corresponds to a low-level computation graph for full state representation learning.
• C-Flow contains high-level disentangled subgraphs for context-aware representation learning.
• A-Flow is conditioned by both U-Flow and C-Flow, and also motivate C-Flow but not U-Flow.
• Information can be accessed by C-Flow from U-Flow with the help of A-Flow.
3.2
Model architecture design for knowledge graph reasoning
We choose KBC tasks to do KG reasoning. We let ⟨V, E⟩denote a KG where V is a set of nodes (or
entities) and E is a set of edges (or relations). A KG is viewed as a directed graph with each edge
represented by a triple ⟨head, rel, tail⟩, where head is the head entity, tail is the tail entity, and rel
is their relation type. The aim of a KBC task is to predict potential unknown links, i.e., which entity
is likely to be the tail given a query ⟨head, rel, ?⟩with the head and the relation type speciﬁed.
The model architecture has three core components as shown in Figure 2. We here use the term
"component" instead of "layer" to differentiate our ﬂow layers from the referring normally used in
neural networks, as each ﬂow layer is more like a block containing many neural network layers.
U-Flow component. We implement this component over the full graph using the standard message
passing mechanism [46]. If the graph has an extremely large number of edges, we sample a subset
4


## Page 5


of edges, Eτ
smpl ⊂E, randomly each step when running message passing. For each batch of input
queries, we let the representation computed by the U-Flow component be shared across these different
queries, which means U-Flow is query-independent, with its state representation tensors containing no
batch dimension, so that its complexity does not scale with the batch size and the saved computation
resources can be allocated to sampling more edges. In U-Flow, each node v has a learnable embedding
ev and a dynamical state ˜hτ
v for step τ, called unconscious node states, where the initial ˜h0
v := ev
for all v ∈V. Each edge type r also has a learnable embedding er, and edge ⟨v′, r, v⟩can produce a
message, denoted by ˜mτ
⟨v′,r,v⟩, at step τ. The U-Flow component includes:
• Message function: ˜mτ
⟨v′,r,v⟩= ψunc(˜hτ
v′, er, ˜hτ
v), where ⟨v′, r, v⟩∈Eτ
smpl.
• Message aggregation: ˜µτ
v =
1
√˜
N τ
v
P
v′,r ˜mτ
⟨v′,r,v⟩, where ⟨v′, r, v⟩∈Eτ
smpl.
• Node state update function: ˜hτ+1
v
= ˜hτ
v + δunc(˜µτ
v, ˜hτ
v, ev), where v ∈V.
We compute messages only for the sampled edges, ⟨v′, r, v⟩∈Eτ
smpl, each step. Functions ψunc and
δunc are implemented by a two-layer MLP (using leakyReLu for the ﬁrst layer and tanh for the
second layer) with input arguments concatenated respectively. Messages are aggregated by dividing
the sum by the square root of the number of sampled neighbors that send messages, preserving the
scale of variance. We use a residual adding to update each node state instead of a GRU or a LSTM.
After running U-Flow for T steps, we return a pooling result or simply the last, ˜hv := ˜hT
v , to feed
into downstream components.
C-Flow component. C-Flow is query-dependent, which means that conscious node states, denoted
by ht
v, have a batch dimension representing different input queries, making the complexity scale
with the batch size. However, as C-Flow uses attentive message passing, running on small local
subgraphs each conditioned by a query, we leverage the sparsity to record ht
v only for the visited
nodes v ∈Vt
visit. For example, when t = 0, for query ⟨head, rel, ?⟩, we start from node head, with
V0
visit = {vhead} being a singleton, and thus record h0
vhead only. When computing messages, denoted
by mt
⟨v′,r,v⟩, in C-Flow, we use a sampling-attending procedure, explained in Section 3.3, to further
control the number of computed edges. The C-Flow component has:
• Message function: mt
⟨v′,r,v⟩= ψcon(ht
v′, cr, ht
v), where ⟨v′, r, v⟩∈Et
topks(at+1) | topka(at), and
cr = [er, qhead, qrel].
• Message aggregation: µt
v =
1
√
Ntv
P
v′,r mt
⟨v′,r,v⟩, where ⟨v′, r, v⟩∈Et
topks(at+1) | topka(at).
• Node state attending function: ˜ηt+1
v
= at+1
v
A · ˜hv, where at+1
v
= at+1[v] and v ∈Vt+1
visit.
• Node state update function: ht+1
v
= ht
v + δcon(µt
v, ht
v, ct+1
v
), where ct+1
v
= [˜ηt+1
v
, qhead, qrel].
C-Flow and U-Flow share the embeddings er. A query is represented by its head and relation
embeddings, qhead := ehead and qrel := erel, participating in computing messages and updating
node states. We here select a subset of edges, Et
topks(at+1) | topka(at), rather than sampling, according
to edges between the attended nodes at step t and the seen nodes at step t + 1, deﬁned in Section 3.3,
as shown in Figure 3. We introduce the node state attending function to pass an unconscious state ˜hv
to C-Flow adjusted by a scalar attention at+1
v
and a learnable matrix A. We initialize h0
v := ˜hv for
v ∈V0
visit, treating the rest as zero states.
A-Flow component. Attention ﬂow is represented by a series of probability distributions changing
across steps, denoted as at, t = 1, 2 . . . , T. The initial distribution a0 is a one-hot vector with
a0[vhead] = 1. To spread attention, we need to compute transition matrices Tt each step. Given that
A-Flow is conditioned by both U-Flow and C-Flow, we model the transition from v′ to v by two
types of interaction: conscious-to-conscious, ht
v′ ∼ht
v, and conscious-to-unconscious, ht
v′ ∼˜hv.
The former favors previously visited nodes, while the latter is useful to attend to unseen nodes.
Tt[:, v′] = softmaxv∈N t
v′
  X
r αcc(ht
v′, cr, ht
v) +
X
r αcu(ht
v′, cr, ˜hv)

where αcc = MLP(ht
v′, cr)TΘccMLP(ht
v, cr) and αcu = MLP(ht
v′, cr)TΘcuMLP(˜hv, cr), and
Θcc and Θcu are two learnable matrices. Each MLP uses one single layer with the leakyReLu
5


## Page 6


All Candidate Nodes
Sampled Nodes
Seen Nodes
Attended 
Nodes
All Candidate Nodes
Sampled Nodes
Step t
Step t+1
Visited Nodes
Visited Nodes
Seen Nodes
Attended 
Nodes
Figure 3: The iterative sampling-attending procedure for attentive complexity reduction, balancing
the coverage as well as the complexity.
activation. To reduce the complexity for computing Tt, we select attended nodes, v′ ∈topka(at),
which is the set of nodes with the k-largest attention, and then sample v from v′ neighbors as next
nodes. Then, we compute a sparse Tt according to edges ⟨v′, r, v⟩∈Esmpl | topka(at). Due to the
fact that the attended nodes may not carry all attention, a small amount of attention can be lost
during transition, causing the total amount to decrease. Therefore, we use a renormalized version,
at+1 = Ttat/∥Ttat∥. We use the ﬁnal attention on the tail as the probability for prediction to
compute the training objective, as shown in Figure 2.
3.3
Complexity reduction by iterative sampling and attending
Previously, we use edge sampling, in a globally and uniformly random manner, to address the
complexity issue in U-Flow, where we are not concerned about the batch size. Here, we need to
confront the complexity that scales with the batch size in C-Flow. Suppose that we run a normal
message passing for T steps on a KG with |V| nodes and |E| edges for a batch of N queries. Then,
the complexity is O(NTD(|V| + |E|)) where D represents the number of representation dimensions.
The complexity can be reduced to O(NTD(|V| + |Esmpl|)) by using edges sampling. T is a small
positive integer, often less than 10. D is normally between 50 and 200, and being too small for
D would lead to underﬁtting. In U-Flow, we have N = 1, while in C-Flow, let us say N = 100.
Then, to maintain the same complexity as U-Flow, we have to reduce the sampling rate by a factor
of 100 on each query. However, the U-Flow’s edge sampling procedure is for the full graph, and it
is inappropriate to apply to C-Flow on each query due to the reduced sample rate. Also, when |V|
becomes as large as |Esmpl|, we also need to consider decreasing |V|.
Good news is that C-Flow deals with a local subgraph for each query so that we only record a few
selected nodes, called visited nodes, denoted by Vt
visit. We can see that |Vt
visit| is much less than
|V|. The initial V0
visit, when t = 0, contains only one node vhead, and then Vt
visit is enlarged each
step by adding new nodes during spreading. When propagating messages, we only care about the
one-step neighborhood each step. However, the spreading goes so rapidly that after only a few steps it
covers almost all nodes, causing the number of computed edges to increase dramatically. The key to
address the problem is that we need to constrain the scope of nodes we jump from each step, i.e., the
core nodes that determine where we can go based on where we depart from. We call them attended
nodes, which are in charge of the attending-from horizon, selected by topka(at) based on the current
attention at. Given the set of attended nodes, we still need edge sampling over their neighborhoods
in case of a hub node of extremely high degree. Here, we face a tricky problem that is to make a
trade-off between the coverage and the complexity when sampling over the neighborhoods. Also, we
need to well maintain these coherent context-aware node states and avoid possible noises or drifting
away caused by sampling neighbors randomly. Therefore, we introduce an attending-to horizon inside
the sampling horizon. We compute A-Flow over the sampling horizon with a smaller dimension
to compute the attention, exchanged for sampling more neighbors to increase the coverage. Based
6


## Page 7


Table 1: Statistics of the six KG datasets. A KG is built on all training triples including their inverse
triples. Note that we do not count the inverse triples in FB15K, FB15K-237, WN18, WN18RR, and
YAGO3-10 as shown below to be consistent with the statistics reported in other papers, though we
include them in the training, validation and test set. PME (tr) means the proportion of multi-edge
triples in train; PME (te) means the proportion of multi-edge triples in test; AvgD (te) means the
average length of shortest paths connecting each head-tail pair in test.
Dataset
#Entities #Rels
#Train
#Valid
#Test
PME (tr)
PME (te)
AvgD (te)
FB15K
14,951
1,345
483,142
50,000
59,071
81.2%
80.9%
1.22
FB15K-237
14,541
237
272,115
17,535
20,466
38.0%
0%
2.25
WN18
40,943
18
141,442
5,000
5,000
93.1%
94.0%
1.18
WN18RR
40,943
11
86,835
3,034
3,134
34.5%
35.0%
2.87
NELL995
74,536
200
149,678
543
2,818
100%
41.0%
2.06
YAGO3-10
123,188
37
1,079,040
5,000
5,000
56.4%
56.0%
1.75
Table 2: Comparison results on the FB15K-237 and WN18RR datasets. Results of [♠] are taken
from [83], results of [♣] from [10], results of [♥] from [17], results of [♦] from [12], and results of
[△] from [16]. Some collected results only have a metric score while some including ours take the
form of "mean (standard deviation)".
FB15K-237
WN18RR
Metric (%)
H@1
H@3
H@10
MRR
H@1
H@3
H@10
MRR
TransE [♠]
-
-
46.5
29.4
-
-
50.1
22.6
DistMult [♣]
15.5
26.3
41.9
24.1
39
44
49
43
DistMult [♥]
20.6 (.4) 31.8 (.2)
-
29.0 (.2) 38.4 (.4) 42.4 (.3)
-
41.3 (.3)
ComplEx [♣]
15.8
27.5
42.8
24.7
41
46
51
44
ComplEx [♥]
20.8 (.2) 32.6 (.5)
-
29.6 (.2) 38.5 (.3) 43.9 (.3)
-
42.2 (.2)
ConvE [♣]
23.7
35.6
50.1
32.5
40
44
52
43
ConvE [♥]
23.3 (.4) 33.8 (.3)
-
30.8 (.2) 39.6 (.3) 44.7 (.2)
-
43.3 (.2)
RotatE [♦]
24.1
37.5
53.3
33.8
42.8
49.2
57.1
47.6
NeuralLP [♥]
18.2 (.6) 27.2 (.3)
-
24.9 (.2) 37.2 (.1) 43.4 (.1)
-
43.5 (.1)
MINERVA [♥]
14.1 (.2) 23.2 (.4)
-
20.5 (.3) 35.1 (.1) 44.5 (.4)
-
40.9 (.1)
MINERVA [△]
-
-
45.6
-
41.3
45.6
51.3
-
M-Walk [♥]
16.5 (.3) 24.3 (.2)
-
23.2 (.2) 41.4 (.1) 44.5 (.2)
-
43.7 (.1)
NeuCFlow
28.6 (.1) 40.3 (.1) 53.0 (.3) 36.9 (.1) 44.4 (.4) 49.7 (.8) 55.8 (.5) 48.2 (.5)
on the newly computed attention at+1, we select a smaller subset of nodes, topks(at+1), to receive
messages in C-Flow, called seen nodes, in charge of the attending-to horizon. The next attending-
from horizon is chosen by topka(at+1) ⊂topks(at+1), a sub-horizon of the current attending-to
horizon. All seen and attended nodes are stored as visited nodes along steps. We illustrate this
sampling-attending procedure in Figure 3.
To compute our reduced complexity, we let Ne be the maximum number of sampled edges per
attended node per step, Ns the maximum number of seen nodes per step, and Na the maximum
number of attended nodes per step. We also denote the dimension number used in A-Flow as Da.
For one batch, the complexity of C-Flow is O(NTD(Na + Ns + NaNs)) for the worst case, where
attended and seen nodes are fully connected, and O(NTD · c(Na + Ns)) in most cases, where c is a
small constant. The complexity of A-Flow is O(NTDaNaNe) where Da is much smaller than D.
4
Experiments
4.1
Datasets and experimental settings
Datasets. We evaluate our model using six large KG datasets2: FB15K, FB15K-237, WN18,
WN18RR, NELL995, and YAGO3-10. FB15K-237 [84] is sampled from FB15K [8] with redundant
relations removed, and WN18RR [10] is a subset of WN18 [8] removing triples that cause test
leakage. Thus, they are both considered more challenging. NELL995 [15] has separate datasets
2https://github.com/netpaladinx/NeuCFlow/tree/master/data
7


## Page 8


Table 3: Comparison results on the FB15K and WN18 datasets. Results of [♠] are taken from [86],
results of [♣] are from [10], results of [♦] are from [12], and results of [♥] are from [19]. Our results
take the form of "mean (standard deviation)".
FB15K
WN18
Metric (%)
H@1
H@3
H@10
MRR
H@1
H@3
H@10
MRR
TransE [♠]
29.7
57.8
74.9
46.3
11.3
88.8
94.3
49.5
HolE [♠]
40.2
61.3
73.9
52.4
93.0
94.5
94.9
93.8
DistMult [♣]
54.6
73.3
82.4
65.4
72.8
91.4
93.6
82.2
ComplEx [♣]
59.9
75.9
84.0
69.2
93.6
93.6
94.7
94.1
ConvE [♣]
55.8
72.3
83.1
65.7
93.5
94.6
95.6
94.3
RotatE [♦]
74.6
83.0
88.4
79.7
94.4
95.2
95.9
94.9
NeuralLP [♥]
-
-
83.7
76
-
-
94.5
94
NeuCFlow
72.6 (.4) 78.4 (.4) 83.4 (.5)
76.4 (.4)
91.6 (.8)
93.6 (.4)
94.9 (.4)
92.8 (.6)
Table 4: Comparison results on the YAGO3-10 dataset. Results of [♠] are taken from [10], and
results of [♣] are from [13].
YAGO3-10
Metric (%)
H@1
H@3
H@10
MRR
DistMult [♠]
24
38
54
34
ComplEx [♠]
26
40
55
36
ConvE [♠]
35
49
62
44
ComplEx-N3 [♣]
-
-
71
58
NeuCFlow
48.4
59.5
67.9
55.3
for 12 query relations each corresponding to a single-query-relation KBC task. YAGO3-10 [85]
contains the largest KG with millions of edges. Their statistics are shown in Table 1. We ﬁnd some
statistical differences between train and test. In a KG with all training triples as its edges, a triple
(head, rel, tail) is considered as a multi-edge triple if the KG contains other triples that also connect
head and tail ignoring the direction. We notice that FB15K-237 is a special case compared with the
others, as there are no edges in its KG directly linking any pair of head and tail in test. Therefore,
when using training triples as queries to train our model, given a batch, for FB15K-237, we cut off
from the KG all triples connecting the head-tail pairs in the given batch, ignoring relation types and
edge directions, forcing the model to learn a composite reasoning pattern rather than a single-hop
pattern, and for the rest datasets, we only remove the triples of this batch and their inverse from the
KG before training on this batch.
Experimental settings. We use the same data split protocol as in many papers [10, 15, 16]. We
create a KG, a directed graph, consisting of all train triples and their inverse added for each dataset
except NELL995, since it already includes reciprocal relations. Besides, every node in KGs has a
self-loop edge to itself. We also add inverse relations into the validation and test set to evaluate the
two directions. For evaluation metrics, we use HITS@1,3,10 and the mean reciprocal rank (MRR) in
the ﬁltered setting for FB15K-237, WN18RR, FB15K, WN18, and YAGO3-10, and use the mean
average precision (MAP) for NELL995’s single-query-relation KBC tasks. For NELL995, we follow
the same evaluation procedure as in [15, 16, 17], ranking the answer entities against the negative
examples given in their experiments. We run our experiments using a 12G-memory GPU, TITAN X
(Pascal), with Intel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz. Our code is written in Python based
on TensorFlow 2.0 and NumPy 1.16.
4.2
Baselines and comparison results
Baselines. We compare our model against embedding-based approaches, including TransE [8],
TransR [22], DistMult [9], ConvE [10], ComplE [11], HolE [86], RotatE [12], and ComplEx-N3
[13], and path-based approaches that use RL methods, including DeepPath [15], MINERVA [16],
and M-Walk [17], and also that uses learned neural logic, NeuralLP [19]. For all the baselines, we
quote the results from the corresponding papers instead of rerunning them. For our method, we run
8


## Page 9


Table 5: Comparison results of MAP scores (%) on NELL995’s single-query-relation KBC tasks. We
take our baselines’ results from [17]. All results take the form of "mean (standard deviation)" except
for TransE and TransR.
Tasks
NeuCFlow
M-Walk
MINERVA
DeepPath
TransE
TransR
AthletePlaysForTeam
83.9 (0.5)
84.7 (1.3)
82.7 (0.8)
72.1 (1.2)
62.7
67.3
AthletePlaysInLeague
97.5 (0.1)
97.8 (0.2)
95.2 (0.8)
92.7 (5.3)
77.3
91.2
AthleteHomeStadium
93.6 (0.1)
91.9 (0.1)
92.8 (0.1)
84.6 (0.8)
71.8
72.2
AthletePlaysSport
98.6 (0.0)
98.3 (0.1)
98.6 (0.1)
91.7 (4.1)
87.6
96.3
TeamPlayssport
90.4 (0.4)
88.4 (1.8)
87.5 (0.5)
69.6 (6.7)
76.1
81.4
OrgHeadQuarteredInCity
94.7 (0.3)
95.0 (0.7)
94.5 (0.3)
79.0 (0.0)
62.0
65.7
WorksFor
86.8 (0.0)
84.2 (0.6)
82.7 (0.5)
69.9 (0.3)
67.7
69.2
PersonBornInLocation
84.1 (0.5)
81.2 (0.0)
78.2 (0.0)
75.5 (0.5)
71.2
81.2
PersonLeadsOrg
88.4 (0.1)
88.8 (0.5)
83.0 (2.6)
79.0 (1.0)
75.1
77.2
OrgHiredPerson
84.7 (0.8)
88.8 (0.6)
87.0 (0.3)
73.8 (1.9)
71.9
73.7
AgentBelongsToOrg
89.3 (1.2)
-
-
-
-
-
TeamPlaysInLeague
97.2 (0.3)
-
-
-
-
-
the experiments three times in each hyperparameter setting on each dataset to report the means and
standard deviations of the results. We put the details of our hyperparameter settings in the appendix.
Comparison results and analysis. We ﬁrst report the comparison on FB15K-23 and WN18RR in
Table 2. NeuCFlow has a surprisingly good result, signiﬁcantly outperforming all the compared
methods in HITS@1,3 and MRR on both the two datasets. Compared to the best baseline, RotatE,
published very recently, we only lose a few points in HITS@10 but gain a lot in HITS@1,3 and MRR.
Based on the observation that NeuCFlow gains a larger amount of advantage when k in HITS@k gets
smaller, we speculate that the reasoning ability acquired by NeuCFlow is to make a sharper prediction
by exploiting graph-structured composition locally and conditionally, in contrast to embedding-based
methods, which totally rely on vectorized representation. When a target becomes too vague to
predict, reasoning may lose its great advantage, though still very competitive. However, path-based
baselines, with a certain ability to do KG reasoning, perform worse than we expect. We argue that it
is inappropriate to think of reasoning, a sequential decision process, as a sequence of nodes, i.e. a
path, in KGs. The average length of the shortest paths between heads and tails in the test set in a KG,
as shown in Table 1, suggests an extremely short path, making the motivation for using a path pattern
almost pointless. The iterative reasoning pattern should be characterized in the form of dynamically
varying local graph-structured patterns, holding a bunch of nodes resonating with each other to
produce a decision collectively. Then, we run our model on larger KGs, including FB15K, WN18,
and YAGO3-10, and summarize the comparison in Table 3,4, where NeuCFlow beats most well-
known baselines and achieves a very competitive position against the best state-of-the-art methods.
Moreover, we summarize the comparison on NELL995’s tasks in Table 5. NeuCFlow performs the
best on ﬁve tasks, also being very competitive against M-Walk, the best path-based method as far as
we know, on the rest. We ﬁnd no reporting on the last two tasks from the corresponding papers.
4.3
Experimental analysis
Convergence analysis. During training we ﬁnd that NeuCFlow converges surprisingly fast. We may
use half of training examples to get the model well trained and generalize it to the test, sometimes
producing an even better metric score than trained for a full epoch, as shown in Figure 4(A). Compared
with the less expensive computation using embedding-based models, although our model takes a
large number of edges to compute for each input query, consuming more time on one batch, it does
not need a second epoch or even taking all training triples as queries in one epoch, thus saving a lot
of training time. The reason may be that all queries are directly from the KG’s edge set and some
of them have probably been exploited to construct subgraphs for many times during the training of
other queries, so that we might not have to train the model on each query explicitly as long as we
have other ways to exploit them.
Component analysis. If we do not run U-Flow, then the unconscious state ˜hv is just the initial
embedding of node v, and we can still run C-Flow as usual. We want to know whether the U-Flow
component is actually useful. Considering that long-distance message passing might bring in less
9


## Page 10


0.5
1.0
1.5
2.0
2.5
3.0
Epoch
40.0
42.5
45.0
47.5
50.0
52.5
55.0
57.5
60.0
Metric Score (%)
(A) Convergence Analysis (by evaluation on test during training)
H@1
H@3
H@10
MMR
H@1
H@3
H@10
MMR
40.0
42.5
45.0
47.5
50.0
52.5
55.0
57.5
60.0
Metric Score (%)
(B) U-Flow Component Analysis
W/o U-Flow
With U-Flow
H@1
MMR
40
42
44
46
48
50
52
54
Metric Score (%)
(C) Sampling Horizon Analysis
Max-sampled-edges-per-node = 20
Max-sampled-edges-per-node = 50
Max-sampled-edges-per-node = 100
Max-sampled-edges-per-node = 200
Max-sampled-edges-per-node = 400
H@1
MMR
40
42
44
46
48
50
52
54
Metric Score (%)
(D) Attending-to Horizon Analysis
Max-seen-nodes-per-step = 20
Max-seen-nodes-per-step = 50
Max-seen-nodes-per-step = 100
Max-seen-nodes-per-step = 200
Max-seen-nodes-per-step = 400
H@1
MMR
40
42
44
46
48
50
52
54
Metric Score (%)
(E) Attending-from Horizon Analysis
Max-attended-nodes-per-step = 5
Max-attended-nodes-per-step = 10
Max-attended-nodes-per-step = 20
Max-attended-nodes-per-step = 40
H@1
MMR
35.0
37.5
40.0
42.5
45.0
47.5
50.0
52.5
55.0
Metric Score (%)
(F) Searching Horizon Analysis
#Steps-of-C-Flow = 2
#Steps-of-C-Flow = 4
#Steps-of-C-Flow = 6
#Steps-of-C-Flow = 8
Figure 4: Experimental analysis on WN18RR: (A) During training we pick six model snapshots
at time points of 0.3, 0.5, 0.7, 1, 2, and 3 epochs and evaluate them on test; (B) The w/o U-Flow
uses zero step to run U-Flow, while the with U-Flow uses two steps; (C)-(F) are for the sampling,
attending and searching horizon analysis based on the standard hyperparameter settings listed in the
appendix. The experimental analysis charts on FB15K-237 can be found in the appendix.
informative features, we compare running U-Flow for two steps against totally shutting it down. The
result in Figure 4(B) shows that U-Flow brings a small gain in each metric on WN18RR.
Horizon analysis. The sampling, attending and searching horizons determine how large area the
ﬂow can spread over. They impact the computation complexity as well as the performance of the
model with different degrees depending on the properties of a dataset. Intuitively, enlarging the
probe scope by sampling more, attending more, or searching longer, may increase the chance to hit
a target. However, the experimental results in Figure 4(C)(D) show that it is not always the case.
In Figure 4(E), we can see that increasing the maximum number of the attending-from nodes, i.e.
attended nodes, per step is more important, but our GPU does not allow for a larger number to
accommodate more intermediate data produced during computation, otherwise causing the error of
ResourceExhaustedError. Figure 4(F) shows the step number of C-Flow cannot get too small as two.
Attention ﬂow analysis. If attention ﬂow can really capture the way we reason about the world, its
process should be conducted in a diverging-converging thinking pattern. Intuitively, ﬁrst, for the
diverging thinking, we search and collect ideas as much as we can; then, for the converging thinking,
we try to concentrate our thoughts on one point. To check whether the attention ﬂow has such a
pattern, we measure the average entropy of attention distributions varying along steps and also the
proportion of attention concentrated at the top-1,3,5 attended nodes. As we expect, attention indeed
is more focused at the ﬁnal step as well as at the beginning.
Time cost analysis. The time cost is affected not only by the scale of a dataset but also by the
horizon setting. For each dataset, we list the training time for one epoch corresponding to the
standard hyperparameter settings in the appendix. Note that there is always a trade-off between the
complexity and the performance. We thus study whether we can reduce the time cost a lot at the price
of sacriﬁcing a little performance. We plot the one-epoch training time in Figure 6(A)-(D), using
the same settings as we do in the horizon analysis. We can see that Max-attended-nodes-per-step
and #Steps-of-C-Flow affect the training time signiﬁcantly while Max-sampled-edges-per-node and
Max-seen-nodes-per-step affect very slightly. Therefore, we can use smaller Max-sampled-edges-per-
node and Max-seen-nodes-per-step in order to gain a larger batch size, making the computation more
efﬁciency as shown in Figure 6(E).
10


## Page 11


0
1
2
3
4
Step
0
2
4
6
8
10
Entropy of Attention Distribution
(A) Attention Flow Analysis (on entroy)
AthletePlaysForTeam
AthletePlaysInLeague
AthleteHomeStadium
AthletePlaysSport
TeamPlaysSport
OrgHeadQuarteredInCity
WorksFor
PersonBornInLocation
PersonLeadsOrg
OrgHiredPerson
AgentBelongsToOrg
TeamPlaysInLeague
0
1
2
3
4
Step
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Proportion-of-Top1
(B) Attention Flow Analysis (on top1's proportion)
AthletePlaysForTeam
AthletePlaysInLeague
AthleteHomeStadium
AthletePlaysSport
TeamPlaysSport
OrgHeadQuarteredInCity
WorksFor
PersonBornInLocation
PersonLeadsOrg
OrgHiredPerson
AgentBelongsToOrg
TeamPlaysInLeague
0
1
2
3
4
Step
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Proportion-of-Top3
(C) Attention Flow Analysis (on top3's proportion)
AthletePlaysForTeam
AthletePlaysInLeague
AthleteHomeStadium
AthletePlaysSport
TeamPlaysSport
OrgHeadQuarteredInCity
WorksFor
PersonBornInLocation
PersonLeadsOrg
OrgHiredPerson
AgentBelongsToOrg
TeamPlaysInLeague
0
1
2
3
4
Step
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Proportion-of-Top5
(D) Attention Flow Analysis (on top5's proportion)
AthletePlaysForTeam
AthletePlaysInLeague
AthleteHomeStadium
AthletePlaysSport
TeamPlaysSport
OrgHeadQuarteredInCity
WorksFor
PersonBornInLocation
PersonLeadsOrg
OrgHiredPerson
AgentBelongsToOrg
TeamPlaysInLeague
Figure 5: Analysis of attention ﬂow on NELL995 tasks: (A) records how the average entropy of
attention distributions varies along steps for each single-query-relation KBC task. (B)(C)(D) measure
the changing of the proportion of attention concentrated at the top-1,3,5 attended nodes per step for
each task.
0
2
4
6
8
10
Training Time for One Epoch (h)
(A) Time Cost for Different Sampling Horizons
Max-sampled-edges-per-node = 20
Max-sampled-edges-per-node = 50
Max-sampled-edges-per-node = 100
Max-sampled-edges-per-node = 200
Max-sampled-edges-per-node = 400
0
2
4
6
8
10
Training Time for One Epoch (h)
(B) Time Cost for Different Attending-to Horizons
Max-seen-nodes-per-step = 20
Max-seen-nodes-per-step = 50
Max-seen-nodes-per-step = 100
Max-seen-nodes-per-step = 200
Max-seen-nodes-per-step = 400
0
2
4
6
8
10
Training Time for One Epoch (h)
(C) Time Cost for Different Attending-from Horizons
Max-attended-nodes-per-step = 5
Max-attended-nodes-per-step = 10
Max-attended-nodes-per-step = 20
Max-attended-nodes-per-step = 40
0
2
4
6
8
10
Training Time for One Epoch (h)
(D) Time Cost for Different Searching Horizons
#Steps-of-C-Flow = 2
#Steps-of-C-Flow = 4
#Steps-of-C-Flow = 6
#Steps-of-C-Flow = 8
0
2
4
6
8
10
Training Time for One Epoch (h)
(E) Time Cost for Different Batch Sizes
Batch-size = 50
Batch-size = 100
Batch-size = 200
Batch-size = 300
Figure 6: Analysis of time cost on WN18RR: (A)-(D) measure the training time for one epoch on
different horizon settings corresponding to Figure 4(C)-(F); (E) measures the training time for one
epoch for different batch sizes using the same horizon setting, which is Max-sampled-edges-per-
node=20, Max-seen-nodes-per-step=20, Max-attended-nodes-per-step=20, and #Steps-of-C-Flow=8.
The time cost analysis charts on FB15K-237 can be found in the appendix.
4.4
Visualization
To further demonstrate the reasoning ability acquired by our model, we show some visualization
results of the extracted subgraphs on NELL995’s test data for 12 separate tasks. We avoid using
the training data in order to show the generalization of our model’s learned reasoning ability on
knowledge graphs. Here, we show the visualization result for the AthletePlaysForTeam task. The rest
can be found in the appendix.
For the AthletePlaysForTeam task
Query :
( concept_personnorthamerica_michael_turner ,
concept : athleteplaysforteam ,
concept_sportsteam_falcons )
Selected key edges :
concept_personnorthamerica_michael_turner ,
concept : agentbelongstoorganization ,
concept_sportsleague_nfl
concept_personnorthamerica_michael_turner ,
concept : athletehomestadium ,
concept_stadiumoreventvenue_georgia_dome
concept_sportsleague_nfl ,
concept : agentcompeteswithagent ,
concept_sportsleague_nfl
concept_sportsleague_nfl ,
concept : agentcompeteswithagent_inv ,
concept_sportsleague_nfl
concept_sportsleague_nfl ,
concept : teamplaysinleague_inv ,
concept_sportsteam_sd_chargers
concept_sportsleague_nfl ,
concept : leaguestadiums ,
concept_stadiumoreventvenue_georgia_dome
concept_sportsleague_nfl ,
concept : teamplaysinleague_inv ,
concept_sportsteam_falcons
concept_sportsleague_nfl ,
concept : agentbelongstoorganization_inv ,
concept_personnorthamerica_michael_turner
concept_stadiumoreventvenue_georgia_dome ,
concept : leaguestadiums_inv ,
concept_sportsleague_nfl
concept_stadiumoreventvenue_georgia_dome ,
concept : teamhomestadium_inv ,
concept_sportsteam_falcons
concept_stadiumoreventvenue_georgia_dome ,
concept : athletehomestadium_inv ,
concept_athlete_joey_harrington
concept_stadiumoreventvenue_georgia_dome ,
concept : athletehomestadium_inv ,
concept_athlete_roddy_white
concept_stadiumoreventvenue_georgia_dome ,
concept : athletehomestadium_inv ,
concept_coach_deangelo_hall
concept_stadiumoreventvenue_georgia_dome ,
concept : athletehomestadium_inv ,
concept_personnorthamerica_michael_turner
concept_sportsleague_nfl ,
concept : subpartoforganization_inv ,
concept_sportsteam_oakland_raiders
concept_sportsteam_sd_chargers ,
concept : teamplaysinleague ,
concept_sportsleague_nfl
concept_sportsteam_sd_chargers ,
concept : teamplaysagainstteam ,
concept_sportsteam_falcons
concept_sportsteam_sd_chargers ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_falcons
concept_sportsteam_sd_chargers ,
concept : teamplaysagainstteam ,
concept_sportsteam_oakland_raiders
concept_sportsteam_sd_chargers ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_oakland_raiders
concept_sportsteam_falcons ,
concept : teamplaysinleague ,
concept_sportsleague_nfl
concept_sportsteam_falcons ,
concept : teamplaysagainstteam ,
concept_sportsteam_sd_chargers
concept_sportsteam_falcons ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_sd_chargers
concept_sportsteam_falcons ,
concept : teamhomestadium ,
concept_stadiumoreventvenue_georgia_dome
11


## Page 12


nnorthamerica_michael_turner
concept_stadiumoreventvenue_georgia_dome
concept_sportsleague_nfl
concept_coach_deangelo_hall
concept_athlete_roddy_
concept_athlete_joey_harrington
concept_athlete_quarterback_matt_ryan
concept_coach_jerious_norwood
concept_athlete_chris_redman
concept_city_atlanta
concept_sportsteam_falcons
concept_sportsteam_dallas_cowboys
concept_sportsteam_seahawks
concept_sportsteam_sd_chargers
concept_sportsteam_minnesota_vikingsconcept_sportsteam_broncos
concept_sportsteam_cleveland_browns
concept_sportsteam_titans
_sportsteam_buffalo_bills
concept_sportsteam_kansas_city_chiefs
concept_sportsteam_oakland_raiders
concept_sport_football
concept_awardtrophytournament_division
concept_sportsteam_packers
concept_sportsteam_colts
concept_sportsteam_eagles
concept_sportsteam_new_york_giants
concept_sportsteam_bears_29_17
concept_sportsteam_bills
concept_sportsteam_steelers
concept_sportsteam_buccaneers
concept_sportsteam_rams
concept_sportsteam_saints
concept_sportsteam_bucs
concept_sportsteam_tampa
concept_sportsteam_texans
concept_sportsteam_new_york_jets
concept_sportsteam_r
orthamerica_michael_turner
concept_stadiumoreventvenue_georgia_dome
concept_sportsleague_nfl
concept_coach_deangelo_hall
concept_athlete_roddy_white
oncept_athlete_joey_harrington
ncept_athlete_quarterback_matt_ryan
_coach_jerious_norwood
concept_sportsteam_falcons
concept_sportsteam_oakland_raiders
concept_sport_fo
concept_sportsteam_sd_chargers
concept_sportsteam_minnesota_vikings
concept_sportsteam_dallas_cowboys
concept_sportsteam_new_york_giants
concept_sportsteam_kansas_city_chie
concept_sportsteam_tampa
Figure 7: AthletePlaysForTeam. The head is concept_personnorthamerica_michael_turner, the
query relation is concept:athleteplaysforteam, and the desired tail is concept_sportsteam_falcons.
The left is a full subgraph derived with max_attended_nodes_per_step = 20, and the right is a
further extracted subgraph from the left based on attention. The big yellow node represents the head,
and the big red node represents the tail. Colors indicate how important a node is attended to in a local
subgraph. Grey means less important, yellow means it is more attended during the early steps, and
red means it is more attended when getting close to the ﬁnal step.
concept_sportsteam_falcons ,
concept : teamplaysagainstteam ,
concept_sportsteam_oakland_raiders
concept_sportsteam_falcons ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_oakland_raiders
concept_sportsteam_falcons ,
concept : athleteledsportsteam_inv ,
concept_athlete_joey_harrington
concept_athlete_joey_harrington ,
concept : athletehomestadium ,
concept_stadiumoreventvenue_georgia_dome
concept_athlete_joey_harrington ,
concept : athleteledsportsteam ,
concept_sportsteam_falcons
concept_athlete_joey_harrington ,
concept : athleteplaysforteam ,
concept_sportsteam_falcons
concept_athlete_roddy_white ,
concept : athletehomestadium ,
concept_stadiumoreventvenue_georgia_dome
concept_athlete_roddy_white ,
concept : athleteplaysforteam ,
concept_sportsteam_falcons
concept_coach_deangelo_hall ,
concept : athletehomestadium ,
concept_stadiumoreventvenue_georgia_dome
concept_coach_deangelo_hall ,
concept : athleteplaysforteam ,
concept_sportsteam_oakland_raiders
concept_sportsleague_nfl ,
concept : teamplaysinleague_inv ,
concept_sportsteam_new_york_giants
concept_sportsteam_sd_chargers ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_new_york_giants
concept_sportsteam_falcons ,
concept : teamplaysagainstteam ,
concept_sportsteam_new_york_giants
concept_sportsteam_falcons ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_new_york_giants
concept_sportsteam_oakland_raiders ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_new_york_giants
concept_sportsteam_oakland_raiders ,
concept : teamplaysagainstteam ,
concept_sportsteam_sd_chargers
concept_sportsteam_oakland_raiders ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_sd_chargers
concept_sportsteam_oakland_raiders ,
concept : teamplaysagainstteam ,
concept_sportsteam_falcons
concept_sportsteam_oakland_raiders ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_falcons
concept_sportsteam_oakland_raiders ,
concept : agentcompeteswithagent ,
concept_sportsteam_oakland_raiders
concept_sportsteam_oakland_raiders ,
concept : agentcompeteswithagent_inv ,
concept_sportsteam_oakland_raiders
concept_sportsteam_new_york_giants ,
concept : teamplaysagainstteam ,
concept_sportsteam_sd_chargers
concept_sportsteam_new_york_giants ,
concept : teamplaysagainstteam ,
concept_sportsteam_falcons
concept_sportsteam_new_york_giants ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_falcons
concept_sportsteam_new_york_giants ,
concept : teamplaysagainstteam ,
concept_sportsteam_oakland_raiders
In the above case, the query is (concept_personnorthamerica_michael_turner, concept:athleteplays-
forteam, ?) and the desired answer is concept_sportsteam_falcons. From Figure 7, we can see our
model learns that (concept_personnorthamerica_michael_turner, concept:athletehomestadium, con-
cept_stadiumoreventvenue_georgia_dome) and (concept_stadiumoreventvenue_georgia_dome, con-
cept:teamhomestadium_inv, concept_sportsteam_falcons) are two important facts to support the an-
swer of concept_sportsteam_falcons. Besides, other facts, such as (concept_athlete_joey_harrington,
concept:athletehomestadium, concept_stadiumoreventvenue_georgia_dome) and (concept_athlete-
_joey_harrington, concept:athleteplaysforteam, concept_sportsteam_falcons), provide a vivid exam-
ple that a person or an athlete with concept_stadiumoreventvenue_georgia_dome as his or her home
stadium might play for the team concept_sportsteam_falcons. We have such examples more than
one, like concept_athlete_roddy_white’s and concept_athlete_quarterback_matt_ryan’s. The entity
12


## Page 13


concept_sportsleague_nﬂcannot help us differentiate the true answer from other NFL teams, but it
can at least exclude those non-NFL teams. In a word, our subgraph-structured representation can
well capture the relational and compositional reasoning pattern.
5
Conclusion
We introduce an attentive message passing mechanism on graphs under the notion of attentive aware-
ness, inspired by the phenomenon of consciousness, to model the iterative compositional reasoning
pattern by forming a compact query-dependent subgraph. We propose an attentive computation
framework with three ﬂow-based layer to combine GNNs’ representation power with explicit rea-
soning process, and further reduce the complexity when applying GNNs to large-scale graphs. It is
worth mentioning that our framework is not limited to knowledge graph reasoning, but has a wider
applicability to large-scale graph-based computation with a few input-dependent nodes and edges
involved each time.
References
[1] Yoshua Bengio. The consciousness prior. CoRR, abs/1709.08568, 2017.
[2] Stanislas Dehaene, Michel Kerszberg, and Jean Pierre Changeux. A neuronal model of a global
workspace in effortful cognitive tasks. Proceedings of the National Academy of Sciences of the
United States of America, 95 24:14529–34, 1998.
[3] Giulio Tononi, Mélanie Boly, Marcello Massimini, and Christof Koch. Integrated information
theory: from consciousness to its physical substrate. Nature Reviews Neuroscience, 17:450–461,
2016.
[4] David Rosenthal and Josh Weisberg. Higher-order theories of consciousness. Scholarpedia,
3:4407, 2008.
[5] Robert Van Gulick. Higher-order global states (hogs): an alternative higher-order model.
Higher-order theories of consciousness, pages 67–93, 2004.
[6] Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbuchner, and Gabriele Monfardini.
The graph neural network model. IEEE Transactions on Neural Networks, 20:61–80, 2009.
[7] Peter W. Battaglia, Jessica B. Hamrick, Victor Bapst, Alvaro Sanchez-Gonzalez, Vinícius Flo-
res Zambaldi, Mateusz Malinowski, Andrea Tacchetti, David Raposo, Adam Santoro, Ryan
Faulkner, Çaglar Gülçehre, Francis Song, Andrew J. Ballard, Justin Gilmer, George E. Dahl,
Ashish Vaswani, Kelsey R. Allen, Charles Nash, Victoria Langston, Chris Dyer, Nicolas Heess,
Daan Wierstra, Pushmeet Kohli, Matthew Botvinick, Oriol Vinyals, Yujia Li, and Razvan Pas-
canu. Relational inductive biases, deep learning, and graph networks. CoRR, abs/1806.01261,
2018.
[8] Antoine Bordes, Nicolas Usunier, Alberto García-Durán, Jason Weston, and Oksana Yakhnenko.
Translating embeddings for modeling multi-relational data. In NIPS, 2013.
[9] Bishan Yang, Wen tau Yih, Xiaodong He, Jianfeng Gao, and Li Deng. Embedding entities and
relations for learning and inference in knowledge bases. CoRR, abs/1412.6575, 2015.
[10] Tim Dettmers, Pasquale Minervini, Pontus Stenetorp, and Sebastian Riedel. Convolutional 2d
knowledge graph embeddings. In AAAI, 2018.
[11] Théo Trouillon, Johannes Welbl, Sebastian Riedel, Éric Gaussier, and Guillaume Bouchard.
Complex embeddings for simple link prediction. In ICML, 2016.
[12] Zhiqing Sun, Zhi-Hong Deng, Jian-Yun Nie, and Jian Tang. Rotate: Knowledge graph embed-
ding by relational rotation in complex space. CoRR, abs/1902.10197, 2018.
[13] Timothée Lacroix, Nicolas Usunier, and Guillaume Obozinski. Canonical tensor decomposition
for knowledge base completion. In ICML, 2018.
13


## Page 14


[14] Ni Lao, Tom Michael Mitchell, and William W. Cohen. Random walk inference and learning in
a large scale knowledge base. In EMNLP, 2011.
[15] Wenhan Xiong, Thien Hoang, and William Yang Wang. Deeppath: A reinforcement learning
method for knowledge graph reasoning. In EMNLP, 2017.
[16] Rajarshi Das, Shehzaad Dhuliawala, Manzil Zaheer, Luke Vilnis, Ishan Durugkar, Akshay
Krishnamurthy, Alexander J. Smola, and Andrew McCallum. Go for a walk and arrive at
the answer: Reasoning over paths in knowledge bases using reinforcement learning. CoRR,
abs/1711.05851, 2018.
[17] Yelong Shen, Jianshu Chen, Pu Huang, Yuqing Guo, and Jianfeng Gao. M-walk: Learning to
walk over graphs using monte carlo tree search. In NeurIPS, 2018.
[18] William W. Cohen. Tensorlog: A differentiable deductive database. CoRR, abs/1605.06523,
2016.
[19] Fan Yang, Zhilin Yang, and William W. Cohen. Differentiable learning of logical rules for
knowledge base reasoning. In NIPS, 2017.
[20] Xiaoran Xu, Songpeng Zu, Chengliang Gao, Yuan Zhang, and Wei Feng. Modeling attention
ﬂow on graphs. CoRR, abs/1811.00497, 2018.
[21] Zhen Wang, Jianwen Zhang, Jianlin Feng, and Zheng Chen. Knowledge graph embedding by
translating on hyperplanes. In AAAI, 2014.
[22] Yankai Lin, Zhiyuan Liu, Maosong Sun, Yang Liu, and Xuan Zhu. Learning entity and relation
embeddings for knowledge graph completion. In AAAI, 2015.
[23] Guoliang Ji, Shizhu He, Liheng Xu, Kang Liu, and Jian Zhao. Knowledge graph embedding
via dynamic mapping matrix. In ACL, 2015.
[24] Matt Gardner, Partha Pratim Talukdar, Jayant Krishnamurthy, and Tom Michael Mitchell.
Incorporating vector space similarity in random walk inference over knowledge bases. In
EMNLP, 2014.
[25] Kelvin Guu, John Miller, and Percy S. Liang. Traversing knowledge graphs in vector space. In
EMNLP, 2015.
[26] Yankai Lin, Zhiyuan Liu, and Maosong Sun. Modeling relation paths for representation learning
of knowledge bases. In EMNLP, 2015.
[27] Kristina Toutanova, Victoria Lin, Wen tau Yih, Hoifung Poon, and Chris Quirk. Compositional
learning of embeddings for relation paths in knowledge base and text. In ACL, 2016.
[28] Rajarshi Das, Arvind Neelakantan, David Belanger, and Andrew McCallum. Chains of reasoning
over entities, relations, and text using recurrent neural networks. In EACL, 2017.
[29] Chen Liang, Jonathan Berant, Quoc V. Le, Kenneth D. Forbus, and Ni Lao. Neural symbolic
machines: Learning semantic parsers on freebase with weak supervision. In ACL, 2016.
[30] Kenneth H. Craik. The nature of explanation. 1952.
[31] John R. Anderson. Acquisition of cognitive skill. 1982.
[32] Dedre Gentner and Arthur B. Markman. Structure mapping in analogy and similarity. 1997.
[33] John E. Hummel and Keith J. Holyoak. A symbolic-connectionist theory of relational inference
and generalization. Psychological review, 110 2:220–64, 2003.
[34] Brenden M. Lake, Tomer D. Ullman, Joshua B. Tenenbaum, and Samuel J Gershman. Building
machines that learn and think like people. The Behavioral and brain sciences, 40:e253, 2017.
[35] Joan Bruna, Wojciech Zaremba, Arthur Szlam, and Yann LeCun. Spectral networks and locally
connected networks on graphs. CoRR, abs/1312.6203, 2014.
14


## Page 15


[36] Mikael Henaff, Joan Bruna, and Yann LeCun. Deep convolutional networks on graph-structured
data. CoRR, abs/1506.05163, 2015.
[37] David K. Duvenaud, Dougal Maclaurin, Jorge Aguilera-Iparraguirre, Rafael Gómez-Bombarelli,
Timothy Hirzel, Alán Aspuru-Guzik, and Ryan P. Adams. Convolutional networks on graphs
for learning molecular ﬁngerprints. In NIPS, 2015.
[38] Steven M. Kearnes, Kevin McCloskey, Marc Berndl, Vijay S. Pande, and Patrick Riley. Molec-
ular graph convolutions: moving beyond ﬁngerprints. Journal of computer-aided molecular
design, 30 8:595–608, 2016.
[39] Michaël Defferrard, Xavier Bresson, and Pierre Vandergheynst. Convolutional neural networks
on graphs with fast localized spectral ﬁltering. In NIPS, 2016.
[40] Mathias Niepert, Mohammed Hassan Ahmed, and Konstantin Kutzkov. Learning convolutional
neural networks for graphs. In ICML, 2016.
[41] Thomas N. Kipf and Max Welling. Semi-supervised classiﬁcation with graph convolutional
networks. CoRR, abs/1609.02907, 2017.
[42] Michael M. Bronstein, Joan Bruna, Yann LeCun, Arthur Szlam, and Pierre Vandergheynst.
Geometric deep learning: Going beyond euclidean data. IEEE Signal Processing Magazine,
34:18–42, 2017.
[43] Yujia Li, Daniel Tarlow, Marc Brockschmidt, and Richard S. Zemel. Gated graph sequence
neural networks. CoRR, abs/1511.05493, 2016.
[44] Adam Santoro, David Raposo, David G. T. Barrett, Mateusz Malinowski, Razvan Pascanu,
Peter W. Battaglia, and Timothy P. Lillicrap. A simple neural network module for relational
reasoning. In NIPS, 2017.
[45] Peter W. Battaglia, Razvan Pascanu, Matthew Lai, Danilo Jimenez Rezende, and Koray
Kavukcuoglu. Interaction networks for learning about objects, relations and physics. In
NIPS, 2016.
[46] Justin Gilmer, Samuel S. Schoenholz, Patrick F. Riley, Oriol Vinyals, and George E. Dahl.
Neural message passing for quantum chemistry. In ICML, 2017.
[47] Michael Chang, Tomer Ullman, Antonio Torralba, and Joshua B. Tenenbaum. A compositional
object-based approach to learning physical dynamics. CoRR, abs/1612.00341, 2017.
[48] Thomas N. Kipf, Ethan Fetaya, Kuan-Chieh Wang, Max Welling, and Richard S. Zemel. Neural
relational inference for interacting systems. In ICML, 2018.
[49] Alvaro Sanchez-Gonzalez, Nicolas Heess, Jost Tobias Springenberg, Josh Merel, Martin A.
Riedmiller, Raia Hadsell, and Peter W. Battaglia. Graph networks as learnable physics engines
for inference and control. In ICML, 2018.
[50] Jessica B. Hamrick, Kelsey R. Allen, Victor Bapst, Tina Zhu, Kevin R. McKee, Joshua B.
Tenenbaum, and Peter W. Battaglia. Relational inductive bias for physical construction in
humans and machines. CoRR, abs/1806.01203, 2018.
[51] Nicholas Watters, Daniel Zoran, Théophane Weber, Peter W. Battaglia, Razvan Pascanu, and
Andrea Tacchetti. Visual interaction networks: Learning a physics simulator from video. In
NIPS, 2017.
[52] David Raposo, Adam Santoro, David G. T. Barrett, Razvan Pascanu, Timothy P. Lillicrap, and
Peter W. Battaglia. Discovering objects and their relations from entangled scene representations.
CoRR, abs/1702.05068, 2017.
[53] Xiaolong Wang, Ross B. Girshick, Abhinav Gupta, and Kaiming He. Non-local neural networks.
2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 7794–7803,
2018.
15


## Page 16


[54] Xinlei Chen, Li-Jia Li, Li Fei-Fei, and Abhinav Gupta. Iterative visual reasoning beyond
convolutions. 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
7239–7248, 2018.
[55] Adam Santoro, Ryan Faulkner, David Raposo, Jack W. Rae, Mike Chrzanowski, Théophane
Weber, Daan Wierstra, Oriol Vinyals, Razvan Pascanu, and Timothy P. Lillicrap. Relational
recurrent neural networks. In NeurIPS, 2018.
[56] Rasmus Berg Palm, Ulrich Paquet, and Ole Winther. Recurrent relational networks. In NeurIPS,
2018.
[57] Daniel Oñoro-Rubio, Mathias Niepert, Alberto García-Durán, Roberto Gonzalez, and
Roberto Javier López-Sastre. Representation learning for visual-relational knowledge graphs.
CoRR, abs/1709.02314, 2017.
[58] Takuo Hamaguchi, Hidekazu Oiwa, Masashi Shimbo, and Yuji Matsumoto. Knowledge transfer
for out-of-knowledge-base entities: A graph neural network approach. 2017.
[59] Sainbayar Sukhbaatar, Arthur Szlam, and Rob Fergus. Learning multiagent communication
with backpropagation. In NIPS, 2016.
[60] Yedid Hoshen. Vain: Attentional multi-agent predictive modeling. In NIPS, 2017.
[61] Miltiadis Allamanis, Marc Brockschmidt, and Mahmoud Khademi. Learning to represent
programs with graphs. CoRR, abs/1711.00740, 2018.
[62] Irwan Bello, Hieu Quang Pham, Quoc V. Le, Mohammad Norouzi, and Samy Bengio. Neural
combinatorial optimization with reinforcement learning. CoRR, abs/1611.09940, 2017.
[63] Alex Nowak, Soledad Villar, Afonso S. Bandeira, and Joan Bruna. A note on learning algorithms
for quadratic assignment with graph neural networks. CoRR, abs/1706.07450, 2017.
[64] Elias Boutros Khalil, Hanjun Dai, Yuyu Zhang, Bistra N. Dilkina, and Le Song. Learning
combinatorial optimization algorithms over graphs. In NIPS, 2017.
[65] Daniel D. Johnson. Learning graphical state transitions. In ICLR, 2017.
[66] Daniel Selsam, Matthew Lamm, Benedikt Bünz, Percy S. Liang, Leonardo de Moura, and
David L. Dill. Learning a sat solver from single-bit supervision. CoRR, abs/1802.03685, 2018.
[67] Jessica B. Hamrick, Andrew J. Ballard, Razvan Pascanu, Oriol Vinyals, Nicolas Heess,
and Peter W. Battaglia. Metacontrol for adaptive imagination-based optimization. CoRR,
abs/1705.02670, 2017.
[68] Razvan Pascanu, Yujia Li, Oriol Vinyals, Nicolas Heess, Lars Buesing, Sébastien Racanière,
David P. Reichert, Théophane Weber, Daan Wierstra, and Peter W. Battaglia. Learning model-
based planning from scratch. CoRR, abs/1707.06170, 2017.
[69] Tingwu Wang, Renjie Liao, Jimmy Ba, and Sanja Fidler. Nervenet: Learning structured policy
with graph neural networks. In ICLR, 2018.
[70] Vinícius Flores Zambaldi, David Raposo, Adam Santoro, Victor Bapst, Yujia Li, Igor
Babuschkin, Karl Tuyls, David P. Reichert, Timothy P. Lillicrap, Edward Lockhart, Mur-
ray Shanahan, Victoria Langston, Razvan Pascanu, Matthew Botvinick, Oriol Vinyals, and
Peter W. Battaglia. Relational deep reinforcement learning. CoRR, abs/1806.01830, 2018.
[71] Sam Toyer, Felipe W. Trevizan, Sylvie Thiébaux, and Lexing Xie. Action schema networks:
Generalised policies with deep learning. In AAAI, 2018.
[72] Keyulu Xu, Chengtao Li, Yonglong Tian, Tomohiro Sonobe, Ken ichi Kawarabayashi, and
Stefanie Jegelka. Representation learning on graphs with jumping knowledge networks. In
ICML, 2018.
[73] Risi Kondor, Hy Truong Son, Horace Pan, Brandon M. Anderson, and Shubhendu Trivedi.
Covariant compositional networks for learning graphs. CoRR, abs/1801.02144, 2018.
16


## Page 17


[74] Petar Velickovic, Guillem Cucurull, Arantxa Casanova, Alejandro Romero, Pietro Lió, and
Yoshua Bengio. Graph attention networks. CoRR, abs/1710.10903, 2018.
[75] Wouter Kool. Attention solves your tsp , approximately. 2018.
[76] Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly
learning to align and translate. CoRR, abs/1409.0473, 2015.
[77] Zhouhan Lin, Minwei Feng, Cícero Nogueira dos Santos, Mo Yu, Bing Xiang, Bowen Zhou,
and Yoshua Bengio. A structured self-attentive sentence embedding. CoRR, abs/1703.03130,
2017.
[78] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez,
Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In NIPS, 2017.
[79] Yujia Li, Oriol Vinyals, Chris Dyer, Razvan Pascanu, and Peter W. Battaglia. Learning deep
generative models of graphs. CoRR, abs/1803.03324, 2018.
[80] Nicola De Cao and Thomas Kipf. Molgan: An implicit generative model for small molecular
graphs. CoRR, abs/1805.11973, 2018.
[81] Jiaxuan You, Zhitao Ying, Xiang Ren, William L. Hamilton, and Jure Leskovec. Graphrnn:
Generating realistic graphs with deep auto-regressive models. In ICML, 2018.
[82] Aleksandar Bojchevski, Oleksandr Shchur, Daniel Zügner, and Stephan Günnemann. Netgan:
Generating graphs via random walks. In ICML, 2018.
[83] Dai Quoc Nguyen, Tu Dinh Nguyen, Dat Quoc Nguyen, and Dinh Q. Phung. A novel embedding
model for knowledge base completion based on convolutional neural network. In NAACL-HLT,
2018.
[84] Kristina Toutanova and Danqi Chen. Observed versus latent features for knowledge base and
text inference. 2015.
[85] Farzaneh Mahdisoltani, Joanna Asia Biega, and Fabian M. Suchanek. Yago3: A knowledge
base from multilingual wikipedias. In CIDR, 2014.
[86] Maximilian Nickel, Lorenzo Rosasco, and Tomaso A. Poggio. Holographic embeddings of
knowledge graphs. In AAAI, 2016.
17


## Page 18


6
Appendix
6.1
Hyperparameter settings
Table 6: The standard hyperparameter settings we use for each dataset plus their training time for one
epoch. For the experimental analysis, we only adjust one hyperparameter and keep the remaining
ﬁxed at the standard setting. For NELL995, the training time per epoch means the average time cost
of the 12 single-query-relation tasks.
Hyperparameter
FB15K-237 FB15K WN18RR WN18 YAGO3-10 NELL995
batch_size
80
80
100
100
100
10
n_dims_att
50
50
50
50
50
200
n_dims
100
100
100
100
100
200
max_sampled_edges_per_step
10000
10000
10000
10000
10000
10000
max_attended_nodes_per_step
20
20
20
20
20
100
max_sampled_edges_per_node
200
200
200
200
200
1000
max_seen_nodes_per_step
200
200
200
200
200
1000
n_steps_of_u_ﬂow
2
1
2
1
1
1
n_steps_of_c_ﬂow
6
6
8
8
6
5
learning_rate
0.001
0.001
0.001
0.001
0.0001
0.001
optimizer
Adam
Adam
Adam
Adam
Adam
Adam
grad_clipnorm
1
1
1
1
1
1
n_epochs
1
1
1
1
1
3
Training time per epoch (h)
25.7
63.7
4.3
8.5
185.0
0.12
Our hyperparameters can be categorized into three groups:
• The normal hyperparameters, including batch_size, n_dims_att, n_dims, learning_rate,
grad_clipnorm, and n_epochs. Here, we set a smaller dimension, n_dims_att, for the
attention ﬂow computation, as it uses more edges for computation than the message passing
uses in the consciousness ﬂow layer, and also intuitively, it does not need to propagate high-
dimensional messages but only compute a scalar score for each of the sampled neighbor
nodes, in concert with the idea in the key-value mechanism [1]. We set n_epochs = 1 in
most cases, indicating that our model needs to be trained only for one epoch due to its fast
convergence.
• The hyperparameters that are in charge of controlling the sampling-attending hori-
zon, including max_sampled_edges_per_step that controls the maximum number to
sample edges per step per query for the message passing in the unconsciousness
ﬂow layer, and max_sampled_edges_per_node, max_attended_nodes_per_step and
max_seen_nodes_per_step that control the maximum number to sample edges connected to
each current node per step per query, the maximum number of current nodes to attend from
per step per query, and the maximum number of neighbor nodes to attend to per step per
query in the consciousness ﬂow layer.
• The hyperparameters that are in charge of controlling the searching horizon, including
n_steps_of_u_ﬂow representing the number of steps to run the unconcsiousness ﬂow, and
n_steps_of_c_ﬂow representing the number of steps to run the consciousness ﬂow.
Note that we choose these hyperparameters not only by their performances but also the computation
resources available to us. In some cases, to deal with a very large knowledge graph with limited
resources, we need to make a trade-off between the efﬁciency and the effectiveness. For example, each
of NELL995’s single-query-relation tasks has a small training set, though still with a large graph, so
we can reduce the batch size in favor of affording larger dimensions and a larger sampling-attending
horizon without any concern for waiting too long to ﬁnish one epoch.
6.2
Other experimental analysis
See Figure 8,9.
18


## Page 19


0.5
1.0
1.5
2.0
2.5
3.0
Epoch
20
25
30
35
40
45
50
55
60
65
Metric Score (%)
(A) Convergence Analysis (by evaluation on test during training)
H@1
H@3
H@10
MMR
H@1
H@3
H@10
MMR
25
30
35
40
45
50
55
Metric Score (%)
(B) U-Flow Component Analysis
W/o U-Flow
With U-Flow
H@1
MMR
25.0
27.5
30.0
32.5
35.0
37.5
40.0
42.5
45.0
Metric Score (%)
(C) Sampling Horizon Analysis
Max-sampled-edges-per-node = 20
Max-sampled-edges-per-node = 50
Max-sampled-edges-per-node = 100
Max-sampled-edges-per-node = 200
H@1
MMR
25.0
27.5
30.0
32.5
35.0
37.5
40.0
42.5
45.0
Metric Score (%)
(D) Attending-to Horizon Analysis
Max-seen-nodes-per-step = 20
Max-seen-nodes-per-step = 50
Max-seen-nodes-per-step = 100
Max-seen-nodes-per-step = 200
H@1
MMR
25.0
27.5
30.0
32.5
35.0
37.5
40.0
42.5
45.0
Metric Score (%)
(E) Attending-from Horizon Analysis
Max-attended-nodes-per-step = 5
Max-attended-nodes-per-step = 10
Max-attended-nodes-per-step = 20
H@1
MMR
15
20
25
30
35
40
45
Metric Score (%)
(F) Searching Horizon Analysis
#Steps-of-C-Flow = 2
#Steps-of-C-Flow = 4
#Steps-of-C-Flow = 6
Figure 8: Experimental analysis on FB15K-237: (A) During training we pick six model snapshots
at time points of 0.3, 0.5, 0.7, 1, 2, and 3 epochs and evaluate them on test; (B) The w/o U-Flow
uses zero step to run U-Flow, while the with U-Flow uses two steps; (C)-(F) are for the sampling,
attending and searching horizon analysis based on the standard hyperparameter settings listed in the
appendix.
0
5
10
15
20
25
30
35
Training Time for One Epoch (h)
(A) Time Cost for Different Sampling Horizons
Max-sampled-edges-per-node = 20
Max-sampled-edges-per-node = 50
Max-sampled-edges-per-node = 100
Max-sampled-edges-per-node = 200
0
5
10
15
20
25
30
35
Training Time for One Epoch (h)
(B) Time Cost for Different Attending-to Horizons
Max-seen-nodes-per-step = 20
Max-seen-nodes-per-step = 50
Max-seen-nodes-per-step = 100
Max-seen-nodes-per-step = 200
0
5
10
15
20
25
30
35
Training Time for One Epoch (h)
(C) Time Cost for Different Attending-from Horizons
Max-attended-nodes-per-step = 5
Max-attended-nodes-per-step = 10
Max-attended-nodes-per-step = 20
0
5
10
15
20
25
30
35
Training Time for One Epoch (h)
(D) Time Cost for Different Searching Horizons
#Steps-of-C-Flow = 2
#Steps-of-C-Flow = 4
#Steps-of-C-Flow = 6
0
5
10
15
20
25
30
35
Training Time for One Epoch (h)
(E) Time Cost for Different Batch Sizes
Batch-size = 50
Batch-size = 100
Batch-size = 200
Batch-size = 300
Figure 9: Analysis of time cost on FB15K-237: (A)-(D) measure the training time for one epoch
on different horizon settings corresponding to Figure 8(C)-(F); (E) measures the training time for
one epoch for different batch sizes using the same horizon setting, which is Max-sampled-edges-per-
node=20, Max-seen-nodes-per-step=20, Max-attended-nodes-per-step=20, and #Steps-of-C-Flow=6.
6.3
Other visualization
For the AthletePlaysInLeague task
Query :
( concept_personnorthamerica_matt_treanor ,
concept : athleteplaysinleague ,
concept_sportsleague_mlb )
Selected key edges :
concept_personnorthamerica_matt_treanor ,
concept : athleteflyouttosportsteamposition ,
concept_sportsteamposition_center
concept_personnorthamerica_matt_treanor ,
concept : athleteplayssport ,
concept_sport_baseball
concept_sportsteamposition_center ,
concept : athleteflyouttosportsteamposition_inv ,
concept_personus_orlando_hudson
concept_sportsteamposition_center ,
concept : athleteflyouttosportsteamposition_inv ,
concept_athlete_ben_hendrickson
concept_sportsteamposition_center ,
concept : athleteflyouttosportsteamposition_inv ,
concept_coach_j_j__hardy
concept_sportsteamposition_center ,
concept : athleteflyouttosportsteamposition_inv ,
concept_athlete_hunter_pence
concept_sport_baseball ,
concept : athleteplayssport_inv ,
concept_personus_orlando_hudson
concept_sport_baseball ,
concept : athleteplayssport_inv ,
concept_athlete_ben_hendrickson
concept_sport_baseball ,
concept : athleteplayssport_inv ,
concept_coach_j_j__hardy
concept_sport_baseball ,
concept : athleteplayssport_inv ,
concept_athlete_hunter_pence
concept_personus_orlando_hudson ,
concept : athleteplaysinleague ,
concept_sportsleague_mlb
concept_personus_orlando_hudson ,
concept : athleteplayssport ,
concept_sport_baseball
concept_athlete_ben_hendrickson ,
concept : coachesinleague ,
concept_sportsleague_mlb
concept_athlete_ben_hendrickson ,
concept : athleteplayssport ,
concept_sport_baseball
19


## Page 20


onnorthamerica_matt_treanor
concept_sportsteamposition_center
concept_sport_baseball
concept_personus_orlando_hudson
concept_athlete_ben_hendrickson
concept_athlete_hunter_pence
concept_athlete_gary_carter
concept_athlete_kevin_cash
concept_athlete_scott_linebrink
concept_athlete_jeff_kent
concept_athlete_freddy_sanchez
ncept_athlete_mike_mussina
concept_athlete_matt_clement
concept_coach_ian_snell
concept_athlete_shin_soo_choo
concept_athlete_justin_verlander
concept_athlete_aaron_hill
concept_coach_alex_gordon
concept_athlete_pelfrey
concept_athlete_rajai_davis
concept_athlete_justin_morneau
concept_coach_j_j__hardy
concept_athlete_steve_carlton
concept_sportsleague_mlb
concept_sportsteam_twins
concept_athlete_kei_igawa
concept_coach_adam_laroche
concept_male_mike_sta
concept_athlete_jake_peavy
concept_coach_seth_mcclung
concept_athlete_mark_he
concept_personmexico_jason_giambi
concept_athlete_russell_branyan
northamerica_matt_treanor
concept_sportsteamposition_center
concept_sport_baseball
concept_personus_orlando_hudson
concept_athlete_ben_
concept_athlete_hunter_pence
concept_athlete_gary_carter
concept_athlete_kevin_c
concept_sportsleague_mlb
concept_coach_j_j__hardy
Figure 10: AthletePlaysInLeague. The head is , the query relation is concept:athleteplaysinleague,
and the desired tail is . The left is a full subgraph derived with max_attended_nodes_per_step =
20, and the right is a further extracted subgraph from the left based on attention. The big yellow node
represents the head, and the big red node represents the tail. Colors indicate how important a node is
attended to in a local subgraph. Grey means less important, yellow means it is more attended during
the early steps, and red means it is more attended when getting close to the ﬁnal step.
concept_coach_j_j__hardy ,
concept : coachesinleague ,
concept_sportsleague_mlb
concept_coach_j_j__hardy ,
concept : athleteplaysinleague ,
concept_sportsleague_mlb
concept_coach_j_j__hardy ,
concept : athleteplayssport ,
concept_sport_baseball
concept_athlete_hunter_pence ,
concept : athleteplaysinleague ,
concept_sportsleague_mlb
concept_athlete_hunter_pence ,
concept : athleteplayssport ,
concept_sport_baseball
concept_sportsleague_mlb ,
concept : coachesinleague_inv ,
concept_athlete_ben_hendrickson
concept_sportsleague_mlb ,
concept : coachesinleague_inv ,
concept_coach_j_j__hardy
For the AthleteHomeStadium task
Query :
( concept_athlete_eli_manning ,
concept : athletehomestadium ,
concept_stadiumoreventvenue_giants_stadium )
Selected key edges :
concept_athlete_eli_manning ,
concept : personbelongstoorganization ,
concept_sportsteam_new_york_giants
concept_athlete_eli_manning ,
concept : athleteplaysforteam ,
concept_sportsteam_new_york_giants
concept_athlete_eli_manning ,
concept : athleteledsportsteam ,
concept_sportsteam_new_york_giants
concept_athlete_eli_manning ,
concept : athleteplaysinleague ,
concept_sportsleague_nfl
concept_athlete_eli_manning ,
concept : fatherofperson_inv ,
concept_male_archie_manning
concept_sportsteam_new_york_giants ,
concept : teamplaysinleague ,
concept_sportsleague_nfl
concept_sportsteam_new_york_giants ,
concept : teamhomestadium ,
concept_stadiumoreventvenue_giants_stadium
concept_sportsteam_new_york_giants ,
concept : personbelongstoorganization_inv ,
concept_athlete_eli_manning
concept_sportsteam_new_york_giants ,
concept : athleteplaysforteam_inv ,
concept_athlete_eli_manning
concept_sportsteam_new_york_giants ,
concept : athleteledsportsteam_inv ,
concept_athlete_eli_manning
concept_sportsleague_nfl ,
concept : teamplaysinleague_inv ,
concept_sportsteam_new_york_giants
concept_sportsleague_nfl ,
concept : agentcompeteswithagent ,
concept_sportsleague_nfl
concept_sportsleague_nfl ,
concept : agentcompeteswithagent_inv ,
concept_sportsleague_nfl
concept_sportsleague_nfl ,
concept : leaguestadiums ,
concept_stadiumoreventvenue_giants_stadium
concept_sportsleague_nfl ,
concept : athleteplaysinleague_inv ,
concept_athlete_eli_manning
concept_male_archie_manning ,
concept : fatherofperson ,
concept_athlete_eli_manning
concept_sportsleague_nfl ,
concept : leaguestadiums ,
concept_stadiumoreventvenue_paul_brown_stadium
concept_stadiumoreventvenue_giants_stadium ,
concept : teamhomestadium_inv ,
concept_sportsteam_new_york_giants
concept_stadiumoreventvenue_giants_stadium ,
concept : leaguestadiums_inv ,
concept_sportsleague_nfl
concept_stadiumoreventvenue_giants_stadium ,
concept : proxyfor_inv ,
concept_city_east_rutherford
concept_city_east_rutherford ,
concept : proxyfor ,
concept_stadiumoreventvenue_giants_stadium
concept_stadiumoreventvenue_paul_brown_stadium ,
concept : leaguestadiums_inv ,
concept_sportsleague_nfl
For the AthletePlaysSport task
Query :
( concept_athlete_vernon_wells ,
concept : athleteplayssport ,
concept_sport_baseball )
20


## Page 21


concept_athlete_eli_manning
concept_sportsteam_new_york_giants
concept_sportsleague_nfl
concept_male_archie_manning
concept_athlete_joe_bradley
concept_sport_football
concept_awardtrophytournament_super_bowl
concept_stadiumoreventvenue_giants_stadium
concept_sportsteam_pats
concept_city_philadelphia
concept_athlete_barry_bonds
concept_sportsteamposition_center
concept_bone_knee
concept_athlete_blair_betts
concept_personus_jeremy_shockey
concept_athlete_phil_simms
concept_sport_basketball
concept_athlete_rich_aurilia
concept_athlete_justin_tuck
concept_coach_john_mcgraw
concept_athlete_lawrence_taylor
concept_athlete_steve_smith
concept_lake_new
concept_city_east_rutherford
concept_sportsleague_nhl
concept_sportsteam_new_york_jets
concept_city_new_york
concept_person_belichick
concept_athlete_john_cassell
concept_stadiumoreventvenue_paul_brown_stadium
concept_sportsteam_colts
concept_stadiumoreventvenue_mcafee_coliseum
concept_awardtrophytournament_super_bowl_xlii
concept_stadiumoreventvenue_lucas_oil_stadium
concept_stadiumoreventvenue_meadowlands_stadium
concept_stadiumoreventvenue_gillette_stadium
concept_stadiumoreventvenue_izod_center
concept_stadiumoreventvenue_metrodome
concept_geopoliticalorganizatio
concept_geopoliticallocation_national
concept_athlete_ensberg
concept_stateorprovince_states
ncept_sport_hockey
concept_stadiumoreventvenue_united_center
concept_athlete_eli_manning
concept_sportsteam_new_york_giants
concept_sportsleague_nfl
concept_male_archie_manning
concept_athlete_joe_bradley
concept_sport_football
concept_stadiumoreventvenue_giants_stadium
concept_lake_new
city_east_rutherford
concept_sportsleague_nhl
concept_stadiumoreventvenue_
concept_stadiumoreventvenue_mcafee_coliseum
concept_stadiumoreventvenue_lu
Figure 11: AthleteHomeStadium. The head is concept_athlete_eli_manning, the query relation is
concept:athletehomestadium, and the desired tail is concept_stadiumoreventvenue_giants_stadium.
The left is a full subgraph derived with max_attended_nodes_per_step = 20, and the right is a
further extracted subgraph from the left based on attention. The big yellow node represents the head,
and the big red node represents the tail. Colors indicate how important a node is attended to in a local
subgraph. Grey means less important, yellow means it is more attended during the early steps, and
red means it is more attended when getting close to the ﬁnal step.
Selected key edges :
concept_athlete_vernon_wells ,
concept : athleteplaysinleague ,
concept_sportsleague_mlb
concept_athlete_vernon_wells ,
concept : coachwontrophy ,
concept_awardtrophytournament_world_series
concept_athlete_vernon_wells ,
concept : agentcollaborateswithagent_inv ,
concept_sportsteam_blue_jays
concept_athlete_vernon_wells ,
concept : personbelongstoorganization ,
concept_sportsteam_blue_jays
concept_athlete_vernon_wells ,
concept : athleteplaysforteam ,
concept_sportsteam_blue_jays
concept_athlete_vernon_wells ,
concept : athleteledsportsteam ,
concept_sportsteam_blue_jays
concept_sportsleague_mlb ,
concept : teamplaysinleague_inv ,
concept_sportsteam_dodgers
concept_sportsleague_mlb ,
concept : teamplaysinleague_inv ,
concept_sportsteam_yankees
concept_sportsleague_mlb ,
concept : teamplaysinleague_inv ,
concept_sportsteam_pittsburgh_pirates
concept_awardtrophytournament_world_series ,
concept : teamwontrophy_inv ,
concept_sportsteam_dodgers
concept_awardtrophytournament_world_series ,
concept : teamwontrophy_inv ,
concept_sportsteam_yankees
concept_awardtrophytournament_world_series ,
concept : awardtrophytournamentisthechampionshipgameofthenationalsport ,
concept_sport_baseball
concept_awardtrophytournament_world_series ,
concept : teamwontrophy_inv ,
concept_sportsteam_pittsburgh_pirates
concept_sportsteam_blue_jays ,
concept : teamplaysinleague ,
concept_sportsleague_mlb
concept_sportsteam_blue_jays ,
concept : teamplaysagainstteam ,
concept_sportsteam_yankees
concept_sportsteam_blue_jays ,
concept : teamplayssport ,
concept_sport_baseball
concept_sportsteam_dodgers ,
concept : teamplaysagainstteam ,
concept_sportsteam_yankees
concept_sportsteam_dodgers ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_yankees
concept_sportsteam_dodgers ,
concept : teamwontrophy ,
concept_awardtrophytournament_world_series
concept_sportsteam_dodgers ,
concept : teamplayssport ,
concept_sport_baseball
concept_sportsteam_yankees ,
concept : teamplaysagainstteam ,
concept_sportsteam_dodgers
concept_sportsteam_yankees ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_dodgers
concept_sportsteam_yankees ,
concept : teamwontrophy ,
concept_awardtrophytournament_world_series
concept_sportsteam_yankees ,
concept : teamplayssport ,
concept_sport_baseball
concept_sportsteam_yankees ,
concept : teamplaysagainstteam ,
concept_sportsteam_pittsburgh_pirates
concept_sportsteam_yankees ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_pittsburgh_pirates
concept_sport_baseball ,
concept : teamplayssport_inv ,
concept_sportsteam_dodgers
concept_sport_baseball ,
concept : teamplayssport_inv ,
concept_sportsteam_yankees
concept_sport_baseball ,
concept : awardtrophytournamentisthechampionshipgameofthenationalsport_inv ,
concept_awardtrophytournament_world_series
concept_sport_baseball ,
concept : teamplayssport_inv ,
concept_sportsteam_pittsburgh_pirates
concept_sportsteam_pittsburgh_pirates ,
concept : teamplaysagainstteam ,
concept_sportsteam_yankees
concept_sportsteam_pittsburgh_pirates ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_yankees
concept_sportsteam_pittsburgh_pirates ,
concept : teamwontrophy ,
concept_awardtrophytournament_world_series
concept_sportsteam_pittsburgh_pirates ,
concept : teamplayssport ,
concept_sport_baseball
21


## Page 22


concept_athlete_vernon_wells
concept_sportsleague_mlb
concept_sportsteam_blue_jays
concept_awardtrophytournament_world_series
concept_sportsteamposition_center
concept_sportsteam_yankees
concept_sportsteam_pittsburgh_pirates
concept_sportsteam_dodgers
concept_sportsteam_twins
concept_sport_baseball
concept_sportsteam_white_sox
concept_sportsteam_new_york_mets
concept_sportsteam_red_sox
concept_sportsteam_phillies
concept_sportsteam_cleveland_indians_organization
concept_sportsteam_los_angeles_dodgers
concept_sportsteam_red_sox_this_season
concept_sportsteam_orioles
concept_sportsteam_detroit_tigers
concept_sportsteam_philadelphia_athletics
concept_sportsteam_washington_nationals
concept_sportsteam_mariners
concept_sportsteam_louisville_cardinals
concept_sportsteam_st___louis_cardinals
concept_country_netherlands
concept_country_china
concept_country___america
concept_sportsgame_n1951_world_series
concept_sportsgame_alds
concept_stadiumoreventvenue_us_cellular_field
concept_sportsteam_eagles
concept_country_canada_canada
concept_awardtrophytournament_championships
concept_sport_hockey
concept_sport_golf
concept_sport_football
concept_sport_ski
concept_sport_basketball
concept_geopoliticallocation_national
concept_sport_skiing
concept_country_countries
concept_publication_people_
concept_beverage_tea
concept_sport_cricket
concept_beverage_beer
concept_person_willia
concept_sport_soccer
concept_bank_national
concept_bank_china_construction_bank
concept_stateorprovince_states
concept_country_new_zealand
concept_country_u_s_
concept_hobby_hobbies
concept_country_the_united_kingdom
concept_country_thailand
concept_country_france_france
concept_country_switzerland
ardtrophytournament_prizes
concept_country_spain
concept_country_britain
concept_country_wales
concept_country_portugal
concept_country_malaysia
concept_country_bulgaria
concept_athlete_vernon_wells
concept_sportsleague_mlb
concept_sportsteam_blue_jays
concept_awardtrophytournament_world_series
rtsteamposition_center
concept_sportsteam_yankees
sportsteam_pittsburgh_pirates
concept_sportsteam_dodgers
concept_sportsteam_twins
concept_sport_baseball
concept_sport_hockey
concept_sport_golf
concept_sport_fo
concept_sport_ski
concept_country_new_zealand
Figure 12: AthletePlaysSport. The head is concept_athlete_vernon_wells, the query relation is
concept:athleteplayssport, and the desired tail is concept_sport_baseball. The left is a full subgraph
derived with max_attended_nodes_per_step = 20, and the right is a further extracted subgraph
from the left based on attention. The big yellow node represents the head, and the big red node
represents the tail. Colors indicate how important a node is attended to in a local subgraph. Grey
means less important, yellow means it is more attended during the early steps, and red means it is
more attended when getting close to the ﬁnal step.
For the TeamPlaysSport task
Query :
( concept_sportsteam_red_wings ,
concept : teamplayssport ,
concept_sport_hockey )
Selected key edges :
concept_sportsteam_red_wings ,
concept : teamplaysagainstteam ,
concept_sportsteam_montreal_canadiens
concept_sportsteam_red_wings ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_montreal_canadiens
concept_sportsteam_red_wings ,
concept : teamplaysagainstteam ,
concept_sportsteam_blue_jackets
concept_sportsteam_red_wings ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_blue_jackets
concept_sportsteam_red_wings ,
concept : worksfor_inv ,
concept_athlete_lidstrom
concept_sportsteam_red_wings ,
concept : organizationhiredperson ,
concept_athlete_lidstrom
concept_sportsteam_red_wings ,
concept : athleteplaysforteam_inv ,
concept_athlete_lidstrom
concept_sportsteam_red_wings ,
concept : athleteledsportsteam_inv ,
concept_athlete_lidstrom
concept_sportsteam_montreal_canadiens ,
concept : teamplaysagainstteam ,
concept_sportsteam_red_wings
concept_sportsteam_montreal_canadiens ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_red_wings
concept_sportsteam_montreal_canadiens ,
concept : teamplaysinleague ,
concept_sportsleague_nhl
concept_sportsteam_montreal_canadiens ,
concept : teamplaysagainstteam ,
concept_sportsteam_leafs
concept_sportsteam_montreal_canadiens ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_leafs
concept_sportsteam_blue_jackets ,
concept : teamplaysagainstteam ,
concept_sportsteam_red_wings
concept_sportsteam_blue_jackets ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_red_wings
concept_sportsteam_blue_jackets ,
concept : teamplaysinleague ,
concept_sportsleague_nhl
concept_athlete_lidstrom ,
concept : worksfor ,
concept_sportsteam_red_wings
concept_athlete_lidstrom ,
concept : organizationhiredperson_inv ,
concept_sportsteam_red_wings
concept_athlete_lidstrom ,
concept : athleteplaysforteam ,
concept_sportsteam_red_wings
concept_athlete_lidstrom ,
concept : athleteledsportsteam ,
concept_sportsteam_red_wings
concept_sportsteam_red_wings ,
concept : teamplaysinleague ,
concept_sportsleague_nhl
concept_sportsteam_red_wings ,
concept : teamplaysagainstteam ,
concept_sportsteam_leafs
concept_sportsteam_red_wings ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_leafs
concept_sportsleague_nhl ,
concept : agentcompeteswithagent ,
concept_sportsleague_nhl
concept_sportsleague_nhl ,
concept : agentcompeteswithagent_inv ,
concept_sportsleague_nhl
concept_sportsleague_nhl ,
concept : teamplaysinleague_inv ,
concept_sportsteam_leafs
concept_sportsteam_leafs ,
concept : teamplaysinleague ,
concept_sportsleague_nhl
concept_sportsteam_leafs ,
concept : teamplayssport ,
concept_sport_hockey
For the OrganizationHeadQuarteredInCity task
Query :
( concept_company_disney ,
concept : organizationheadquarteredincity ,
concept_city_burbank )
22


## Page 23


concept_sportsteam_red_wings
concept_athlete_lidstrom
concept_sportsteam_blue_jackets
concept_sportsteam_montreal_canadiens
concept_sportsteam_anaheim_ducks
concept_sportsteam_columbus_blue_jackets
concept_athlete_chelios
concept_sportsteam_hawks
concept_sportsteam_edmonton_oilers
concept_sportsteam_chicago_blackhawks
concept_sportsteam_flyers_playoff_tickets
concept_sportsteam_pittsburgh_penguins
concept_sportsteam_l_a__kings
concept_sportsteam_colorado_avalanche
concept_sportsteam_dallas_stars
concept_stateorprovince_new_york
concept_sportsteam_devils
concept_sportsteam_buffalo_sabres
cept_sportsgame_series
concept_sportsteam_bruins
concept_sportsteam_kings_college
concept_sport_hockey
concept_sportsleague_nhl
concept_sport_basketball
concept_sportsteam_leafs
concept_stadiumoreventvenue_joe_louis_arena
concept_sportsteam_blackhawks
concept_sportsteam_rangers
concept_sportsteam_capitals
concept_sportsteam_new_york_islanders
concept_sportsteam_oilers
concept_sportsteam_ottawa_senators
ept_sportsteam_spurs
concept_sportsteam_tampa_bay_lightning
concept_country___america
concept_country_republic_of_india
concept_country_canada_canada
concept_sportsequipment_ball
concept_awardtrophytournament_championships
concept_sportsequipment_clubs
ncept_sportsequipment_hockey_sticks
concept_stadiumoreventvenue_td_banknorth_garden
concept_tool_accessories
concept_stadiumoreventvenue_pete_times_forum
concept_stadiumoreventvenue_staples_center
concept_sportsteamposition_forward
concept_hobby_hobbies
concept_sport_football
concept_sport_baseball
concept_sport_golf
concept_company_national
concept_sport_soccer
concept_country_usa
concept_sport_wrestling
concept_sport_team
concept_sport_fitness
concept_sportsteam_packers
concept_hobby_hiking
concept_sport_sports
concept_hobby_fishing
concept_country_england
concept_country_ir
concept_country_russia
concept_coach_billy_butler
concept_sportsteamposition_quarterback
concept_sportsteam_red_wings
concept_athlete_lidstrom
ortsteam_blue_jackets
concept_sportsteam_montreal_canadiens
rtsteam_anaheim_ducks
concept_sportsteam_columbus_blue_jackets
concept_sport_hockey
concept_sportsleague_nhl
concept_sport_basketball
concept_sportsteam_leafs
concept_country___america
concept_sport_football
concept_sport_base
concept_sport_
Figure 13: TeamPlaysSport. The head is concept_sportsteam_red_wings, the query relation is
concept:teamplayssport, and the desired tail is concept_sport_hockey. The left is a full subgraph
derived with max_attended_nodes_per_step = 20, and the right is a further extracted subgraph
from the left based on attention. The big yellow node represents the head, and the big red node
represents the tail. Colors indicate how important a node is attended to in a local subgraph. Grey
means less important, yellow means it is more attended during the early steps, and red means it is
more attended when getting close to the ﬁnal step.
Selected key edges :
concept_company_disney ,
concept : headquarteredin ,
concept_city_burbank
concept_company_disney ,
concept : subpartoforganization_inv ,
concept_website_network
concept_company_disney ,
concept : worksfor_inv ,
concept_ceo_robert_iger
concept_company_disney ,
concept : proxyfor_inv ,
concept_ceo_robert_iger
concept_company_disney ,
concept : personleadsorganization_inv ,
concept_ceo_robert_iger
concept_company_disney ,
concept : ceoof_inv ,
concept_ceo_robert_iger
concept_company_disney ,
concept : personleadsorganization_inv ,
concept_ceo_jeffrey_katzenberg
concept_company_disney ,
concept : organizationhiredperson ,
concept_ceo_jeffrey_katzenberg
concept_company_disney ,
concept : organizationterminatedperson ,
concept_ceo_jeffrey_katzenberg
concept_city_burbank ,
concept : headquarteredin_inv ,
concept_company_disney
concept_city_burbank ,
concept : headquarteredin_inv ,
concept_biotechcompany_the_walt_disney_co_
concept_website_network ,
concept : subpartoforganization ,
concept_company_disney
concept_ceo_robert_iger ,
concept : worksfor ,
concept_company_disney
concept_ceo_robert_iger ,
concept : proxyfor ,
concept_company_disney
concept_ceo_robert_iger ,
concept : personleadsorganization ,
concept_company_disney
concept_ceo_robert_iger ,
concept : ceoof ,
concept_company_disney
concept_ceo_robert_iger ,
concept : topmemberoforganization ,
concept_biotechcompany_the_walt_disney_co_
concept_ceo_robert_iger ,
concept : organizationterminatedperson_inv ,
concept_biotechcompany_the_walt_disney_co_
concept_ceo_jeffrey_katzenberg ,
concept : personleadsorganization ,
concept_company_disney
concept_ceo_jeffrey_katzenberg ,
concept : organizationhiredperson_inv ,
concept_company_disney
concept_ceo_jeffrey_katzenberg ,
concept : organizationterminatedperson_inv ,
concept_company_disney
concept_ceo_jeffrey_katzenberg ,
concept : worksfor ,
concept_recordlabel_dreamworks_skg
concept_ceo_jeffrey_katzenberg ,
concept : topmemberoforganization ,
concept_recordlabel_dreamworks_skg
concept_ceo_jeffrey_katzenberg ,
concept : organizationterminatedperson_inv ,
concept_recordlabel_dreamworks_skg
concept_ceo_jeffrey_katzenberg ,
concept : ceoof ,
concept_recordlabel_dreamworks_skg
concept_biotechcompany_the_walt_disney_co_ ,
concept : headquarteredin ,
concept_city_burbank
concept_biotechcompany_the_walt_disney_co_ ,
concept : organizationheadquarteredincity ,
concept_city_burbank
concept_recordlabel_dreamworks_skg ,
concept : worksfor_inv ,
concept_ceo_jeffrey_katzenberg
concept_recordlabel_dreamworks_skg ,
concept : topmemberoforganization_inv ,
concept_ceo_jeffrey_katzenberg
concept_recordlabel_dreamworks_skg ,
concept : organizationterminatedperson ,
concept_ceo_jeffrey_katzenberg
concept_recordlabel_dreamworks_skg ,
concept : ceoof_inv ,
concept_ceo_jeffrey_katzenberg
concept_city_burbank ,
concept : a i r p o r t i n c i t y _ i n v ,
concept_transportation_burbank_glendale_pasadena
concept_transportation_burbank_glendale_pasadena ,
concept : a i r p o r t i n c i t y ,
concept_city_burbank
For the WorksFor task
Query :
( concept_scientist_balmer ,
concept : worksfor ,
concept_university_microsoft )
23


## Page 24


concept_company_disney
concept_city_burbank
concept_ceo_robert_iger
concept_ceo_jeffrey_katzenberg
concept_city_abc
concept_ceo_michael_eisner
concept_politicsblog_rights
concept_blog_espn_the_magazine
concept_website_network
concept_academicfield_media
concept_politicsissue_entertainment
concept_publication_espn
concept_company_abc_television_network
concept_personaustralia_jobs
concept_company_club_penguin
concept_televisionnetwork_abc
concept_website_infoseek
concept_company_pixar
concept_person_disney
concept_biotechcompany_the_walt_disney_co_
concept_city_new_york
concept_recordlabel_dreamworks_skg
concept_company_disney_feature_animation
concept_ceo_george_bodenheimer
concept_company_walt_disney
concept_city_emeryville
concept_personeurope_disney
concept_university_search
concept_personus_david_geffen
concept_sportsleague_espn
concept_personus_steven_spielberg
concept_musicartist_toy
concept_person_steven_spielberg
concept_city_lego
concept_personaustralia_david_geffen
concept_transportation_burbank_g
concept_company_asylum
politicianus_rudy_giuliani
concept_company_walt_disney
concept_stateorprovince_illinois
concept_company_walt_disney_w
concept_company_disney
concept_city_burbank
concept_ceo_robert_iger
concept_ceo_jeffrey_katzenberg
concept_city_abc
concept_ceo_michael_eisner
concept_biotechcompany_the_walt_disney_co_
concept_city_new
concept_recordlabel_dreamworks_skg
concept_website_network
concept_ceo_george_bodenheimer
on_burbank_glendale_pasadena
Figure 14: OrganizationHeadQuarteredInCity. The head is concept_company_disney, the query
relation is concept:organizationheadquarteredincity, and the desired tail is concept_city_burbank.
The left is a full subgraph derived with max_attended_nodes_per_step = 20, and the right is a
further extracted subgraph from the left based on attention. The big yellow node represents the head,
and the big red node represents the tail. Colors indicate how important a node is attended to in a local
subgraph. Grey means less important, yellow means it is more attended during the early steps, and
red means it is more attended when getting close to the ﬁnal step.
Selected key edges :
concept_scientist_balmer ,
concept : topmemberoforganization ,
concept_company_microsoft
concept_scientist_balmer ,
concept : organizationterminatedperson_inv ,
concept_university_microsoft
concept_company_microsoft ,
concept : topmemberoforganization_inv ,
concept_personus_steve_ballmer
concept_company_microsoft ,
concept : topmemberoforganization_inv ,
concept_scientist_balmer
concept_university_microsoft ,
concept : agentcollaborateswithagent ,
concept_personus_steve_ballmer
concept_university_microsoft ,
concept : personleadsorganization_inv ,
concept_personus_steve_ballmer
concept_university_microsoft ,
concept : personleadsorganization_inv ,
concept_person_bill
concept_university_microsoft ,
concept : organizationterminatedperson ,
concept_scientist_balmer
concept_university_microsoft ,
concept : personleadsorganization_inv ,
concept_person_robbie_bach
concept_personus_steve_ballmer ,
concept : topmemberoforganization ,
concept_company_microsoft
concept_personus_steve_ballmer ,
concept : agentcollaborateswithagent_inv ,
concept_university_microsoft
concept_personus_steve_ballmer ,
concept : personleadsorganization ,
concept_university_microsoft
concept_personus_steve_ballmer ,
concept : worksfor ,
concept_university_microsoft
concept_personus_steve_ballmer ,
concept : proxyfor ,
concept_retailstore_microsoft
concept_personus_steve_ballmer ,
concept : subpartof ,
concept_retailstore_microsoft
concept_personus_steve_ballmer ,
concept : agentcontrols ,
concept_retailstore_microsoft
concept_person_bill ,
concept : personleadsorganization ,
concept_university_microsoft
concept_person_bill ,
concept : worksfor ,
concept_university_microsoft
concept_person_robbie_bach ,
concept : personleadsorganization ,
concept_university_microsoft
concept_person_robbie_bach ,
concept : worksfor ,
concept_university_microsoft
concept_retailstore_microsoft ,
concept : proxyfor_inv ,
concept_personus_steve_ballmer
concept_retailstore_microsoft ,
concept : subpartof_inv ,
concept_personus_steve_ballmer
concept_retailstore_microsoft ,
concept : agentcontrols_inv ,
concept_personus_steve_ballmer
For the PersonBornInLocation task
Query :
( concept_person_mark001 ,
concept : personborninlocation ,
concept_county_york_city )
Selected key edges :
concept_person_mark001 ,
concept : persongraduatedfromuniversity ,
concept_university_college
concept_person_mark001 ,
concept : persongraduatedschool ,
concept_university_college
concept_person_mark001 ,
concept : persongraduatedfromuniversity ,
concept_university_state_university
concept_person_mark001 ,
concept : persongraduatedschool ,
concept_university_state_university
concept_person_mark001 ,
concept : personbornincity ,
concept_city_hampshire
concept_person_mark001 ,
concept : hasspouse ,
concept_person_diane001
concept_person_mark001 ,
concept : hasspouse_inv ,
concept_person_diane001
24


## Page 25


concept_scientist_balmer
concept_university_microsoft
concept_company_microsoft
concept_personus_steve_ballmer
concept_person_robbie_bach
concept_politician_jobs
concept_person_bill
concept_personaustralia_paul_allen
concept_ceo_steve_ballmer
concept_company_gates
concept_buildingfeature_windows
concept_date_bill
concept_website_download
concept_product_powerpoint
concept_charactertrait_vista
concept_product_word_documents
concept_mlalgorithm_microsoft_word
concept_museum_steve
concept_city_outlook
concept_emotion_word
concept_consumerelectronicitem_ms_word
concept_hallwayitem_access
concept_personmexico_ryan_whitney
concept_retailstore_microsoft
concept_company_adobe
concept_beverage_n
concept_sportsteam_harvard_divinity_school
concept_coach_vulcan_inc
concept_sportsteam_state_university
concept_biotechcompany_microsoft_corp
concept_person_edwards
concept_company_clinton
concept_politicianus_rodham_clinton
concept_geopoliticallocation_kerry
concept_person_mccain
concept_governmentorganization_representatives
concept_politicalparty_senate
concept_politicalparty_college
concept_governmentorganization_house
concept_personus_paul_allen
concept_coach_tim_murphy
concept_software_microsoft_excel
concept_ceo_paul_allen
concept_sportsteam_new_york_jets
concept_company_sun
concept_software_office_2003
concept_company_yahoo001
concept_female_hillary
concept_personafrica_george_bush
concept_stateorprovince_last_year
concept_university_yahoo
concept_geopoliticallocation_world
concept_university_google
mpany_microsoft_corporation
concept_automobilemaker_jeff_bezos
t_scientist_balmer
concept_university_microsoft
ncept_company_microsoft
concept_personus_steve_ballmer
concept_person_robbie_bach
concept_politician_jobs
concept_person_bill
concept_personmexico_
concept_retailstore_microsoft
concept_company_adobe
concept_personaustralia_paul_allen
concept_sportsteam_harvard_divinity_scho
concept_sportsteam_state_university
Figure 15: WorksFor. The head is concept_scientist_balmer, the query relation is concept:worksfor,
and the desired tail is concept_university_microsoft. The left is a full subgraph derived with
max_attended_nodes_per_step = 20, and the right is a further extracted subgraph from the
left based on attention. The big yellow node represents the head, and the big red node represents
the tail. Colors indicate how important a node is attended to in a local subgraph. Grey means less
important, yellow means it is more attended during the early steps, and red means it is more attended
when getting close to the ﬁnal step.
concept_university_college ,
concept : persongraduatedfromuniversity_inv ,
concept_person_mark001
concept_university_college ,
concept : persongraduatedschool_inv ,
concept_person_mark001
concept_university_college ,
concept : persongraduatedfromuniversity_inv ,
concept_person_bill
concept_university_college ,
concept : persongraduatedschool_inv ,
concept_person_bill
concept_university_state_university ,
concept : persongraduatedfromuniversity_inv ,
concept_person_mark001
concept_university_state_university ,
concept : persongraduatedschool_inv ,
concept_person_mark001
concept_university_state_university ,
concept : persongraduatedfromuniversity_inv ,
concept_person_bill
concept_university_state_university ,
concept : persongraduatedschool_inv ,
concept_person_bill
concept_city_hampshire ,
concept : personbornincity_inv ,
concept_person_mark001
concept_person_diane001 ,
concept : persongraduatedfromuniversity ,
concept_university_state_university
concept_person_diane001 ,
concept : persongraduatedschool ,
concept_university_state_university
concept_person_diane001 ,
concept : hasspouse ,
concept_person_mark001
concept_person_diane001 ,
concept : hasspouse_inv ,
concept_person_mark001
concept_person_diane001 ,
concept : personborninlocation ,
concept_county_york_city
concept_university_state_university ,
concept : persongraduatedfromuniversity_inv ,
concept_person_diane001
concept_university_state_university ,
concept : persongraduatedschool_inv ,
concept_person_diane001
concept_person_bill ,
concept : personbornincity ,
concept_city_york
concept_person_bill ,
concept : personborninlocation ,
concept_city_york
concept_person_bill ,
concept : persongraduatedfromuniversity ,
concept_university_college
concept_person_bill ,
concept : persongraduatedschool ,
concept_university_college
concept_person_bill ,
concept : persongraduatedfromuniversity ,
concept_university_state_university
concept_person_bill ,
concept : persongraduatedschool ,
concept_university_state_university
concept_city_york ,
concept : personbornincity_inv ,
concept_person_bill
concept_city_york ,
concept : personbornincity_inv ,
concept_person_diane001
concept_university_college ,
concept : persongraduatedfromuniversity_inv ,
concept_person_diane001
concept_person_diane001 ,
concept : personbornincity ,
concept_city_york
For the PersonLeadsOrganization task
Query :
( c o n c e p t _ j o u r n a l i s t _ b i l l _ p l a n t e ,
concept : personleadsorganization ,
concept_company_cnn__pbs )
Selected key edges :
c o n c e p t _ j o u r n a l i s t _ b i l l _ p l a n t e ,
concept : worksfor ,
concept_televisionnetwork_cbs
c o n c e p t _ j o u r n a l i s t _ b i l l _ p l a n t e ,
concept : agentcollaborateswithagent_inv ,
concept_televisionnetwork_cbs
concept_televisionnetwork_cbs ,
concept : worksfor_inv ,
concept_journalist_walter_cronkite
concept_televisionnetwork_cbs ,
concept : agentcollaborateswithagent ,
concept_journalist_walter_cronkite
concept_televisionnetwork_cbs ,
concept : worksfor_inv ,
concept_personus_scott_pelley
concept_televisionnetwork_cbs ,
concept : worksfor_inv ,
concept_actor_daniel_schorr
25


## Page 26


concept_person_mark001
concept_university_college
concept_university_state_university
concept_person_diane001
concept_male_world
concept_sportsteam_state_university
concept_politicalparty_college
10
concept_university_syracuse_university
concept_stateorprovince_california
concept_university_high_school
concept_sportsgame_series
concept_city_hampshire
concept_stateorprovince_georgia
concept_geopoliticallocation_world
concept_stateorprovince_massachusetts
concept_stateorprovince_maine
concept_stateorprovince_illinois
concept_jobposition_king
concept_charactertrait_world
concept_county_york_city
concept_person_bill
concept_person_david
concept_person_greg001
concept_person_james001
concept_politician_jobs
concept_language_english
concept_person_michael002
concept_person_joe002
concept_person_aaron_brooks
concept_journalist_dan
concept_person_john003
concept_person_andrew001
concept_person_kevin
concept_person_jim
concept_person_adam001
concept_academicfield_science
concept_city_york
concept_lake_new
concept_buildingfeature_american
concept_city_new_y
concept_building_the_metropolitan
concept_stateorprovince_new_york
concept_building_metropolitan
concept_room_contemporary
concept_river_arts
concept_country_orleans
concept_governmentorganization_federal
concept_geopoliticallocation_state
concept_personeurope_whitney
concept_person_sean002
concept_person_charles001
concept_person_princess
concept_river_state
concept_person_robert003
concept_female_mary
concept_person_prince
concept_sportsleague_new
concept_book_new
concept_country_monaco
concept_country_luxembourg
concept_writer_new
concept_musicinstrument_guitar
concept_country_brazil
concept_country_sweden
concept_geopoliticalorganization_wurttemberg
t_country_mecklenburg
concept_country_romania
concept_person_mark001
concept_university_college
concept_university_state_university
concept_person_diane001
concept_male_world
concept_sportsteam_state_university
concept_county_york_city
concept_person_bill
rsity_syracuse_university
concept_person_david
concept_city_york
concept_lake_new
concept_city_hampshire
concept_person_adam001
concept_country_
Figure 16: PersonBornInLocation. The head is concept_person_mark001, the query relation is
concept:personborninlocation, and the desired tail is concept_county_york_city. The left is a full
subgraph derived with max_attended_nodes_per_step = 20, and the right is a further extracted
subgraph from the left based on attention. The big yellow node represents the head, and the big red
node represents the tail. Colors indicate how important a node is attended to in a local subgraph.
Grey means less important, yellow means it is more attended during the early steps, and red means it
is more attended when getting close to the ﬁnal step.
concept_televisionnetwork_cbs ,
concept : worksfor_inv ,
concept_person_edward_r__murrow
concept_televisionnetwork_cbs ,
concept : agentcollaborateswithagent ,
concept_person_edward_r__murrow
concept_televisionnetwork_cbs ,
concept : worksfor_inv ,
c o n c e p t _ j o u r n a l i s t _ b i l l _ p l a n t e
concept_televisionnetwork_cbs ,
concept : agentcollaborateswithagent ,
c o n c e p t _ j o u r n a l i s t _ b i l l _ p l a n t e
concept_journalist_walter_cronkite ,
concept : worksfor ,
concept_televisionnetwork_cbs
concept_journalist_walter_cronkite ,
concept : agentcollaborateswithagent_inv ,
concept_televisionnetwork_cbs
concept_journalist_walter_cronkite ,
concept : worksfor ,
concept_nonprofitorganization_cbs_evening
concept_personus_scott_pelley ,
concept : worksfor ,
concept_televisionnetwork_cbs
concept_personus_scott_pelley ,
concept : personleadsorganization ,
concept_televisionnetwork_cbs
concept_personus_scott_pelley ,
concept : personleadsorganization ,
concept_company_cnn__pbs
concept_actor_daniel_schorr ,
concept : worksfor ,
concept_televisionnetwork_cbs
concept_actor_daniel_schorr ,
concept : personleadsorganization ,
concept_televisionnetwork_cbs
concept_actor_daniel_schorr ,
concept : personleadsorganization ,
concept_company_cnn__pbs
concept_person_edward_r__murrow ,
concept : worksfor ,
concept_televisionnetwork_cbs
concept_person_edward_r__murrow ,
concept : agentcollaborateswithagent_inv ,
concept_televisionnetwork_cbs
concept_person_edward_r__murrow ,
concept : personleadsorganization ,
concept_televisionnetwork_cbs
concept_person_edward_r__murrow ,
concept : personleadsorganization ,
concept_company_cnn__pbs
concept_televisionnetwork_cbs ,
concept : organizationheadquarteredincity ,
concept_city_new_york
concept_televisionnetwork_cbs ,
concept : headquarteredin ,
concept_city_new_york
concept_televisionnetwork_cbs ,
concept : agentcollaborateswithagent ,
concept_personeurope_william_paley
concept_televisionnetwork_cbs ,
concept : topmemberoforganization_inv ,
concept_personeurope_william_paley
concept_company_cnn__pbs ,
concept : headquarteredin ,
concept_city_new_york
concept_company_cnn__pbs ,
concept : personbelongstoorganization_inv ,
concept_personeurope_william_paley
concept_nonprofitorganization_cbs_evening ,
concept : worksfor_inv ,
concept_journalist_walter_cronkite
concept_city_new_york ,
concept : organizationheadquarteredincity_inv ,
concept_televisionnetwork_cbs
concept_city_new_york ,
concept : headquarteredin_inv ,
concept_televisionnetwork_cbs
concept_city_new_york ,
concept : headquarteredin_inv ,
concept_company_cnn__pbs
concept_personeurope_william_paley ,
concept : agentcollaborateswithagent_inv ,
concept_televisionnetwork_cbs
concept_personeurope_william_paley ,
concept : topmemberoforganization ,
concept_televisionnetwork_cbs
concept_personeurope_william_paley ,
concept : personbelongstoorganization ,
concept_company_cnn__pbs
concept_personeurope_william_paley ,
concept : personleadsorganization ,
concept_company_cnn__pbs
For the OrganizationHiredPerson task
Query :
( concept_stateorprovince_afternoon ,
concept : organizationhiredperson ,
concept_personmexico_ryan_whitney )
Selected key edges :
concept_stateorprovince_afternoon ,
concept : atdate ,
concept_dateliteral_n2007
26


## Page 27


concept_journalist_bill_plante
concept_televisionnetwork_cbs
concept_person_edward_r__murrow
concept_personus_scott_pelley
concept_actor_daniel_schorr
concept_journalist_wyatt_andrews
concept_athlete_anthony_mason
concept_journalist_connie_chung
concept_journalist_andy_rooney
concept_journalist_ed_bradley
concept_writer_bill_geist
pt_person_byron_pitts
concept_personaustralia_harry_smith
concept_journalist_morley_safer
concept_journalist_gloria_borger
concept_writer_bernard_goldberg
concept_person_eric_sevareid
concept_journalist_lesley_stahl
cept_personmexico_david_martin
concept_journalist_walter_cronkite
concept_personaustralia_phil_jones
concept_company_cnn__pbs
concept_nonprofitorganization_cbs_evening
ept_musicartist_television
concept_crustacean_tv
concept_website_cbs_evening_news
concept_city_new_york
concept_personeurope_william_paley
concept_coach_douglas_edwards
concept_academicfield_media
concept_person_sean_mcmanus
concept_televisionstation_wcsc
concept_comedian_leslie_moonves
concept_person_nina_tassler
concept_televisionstation_kion_tv
concept_televisionstation_wowk_tv
concept_televisionstation_kbci_tv
concept_televisionstation_wjtv
concept_politicsissue_entertainment
concept_person_les_moonves
concept_televisionstation_kfda
concept_televisionstation_wdtv
concept_televisionstation_khqa_tv
pt_televisionstation_wrbl
cept_televisionstation_wltx_tv
concept_website_cbs
concept_company_cbs_corp_
concept_recordlabel_un
concept_blog_mtv
cept_journalist_bill_plante
concept_televisionnetwork_cbs
concept_person_edward_r__murrow
concept_personus_scott_pelley
concept_actor_daniel_schorr
urnalist_wyatt_andrews
concept_athlete_anthony_mason
concept_company_cnn__pbs
concept_nonprofitorganization
concept_musicartist_television
concept_crustacean_tv
concept_journalist_walter_cronkite
concept_city_new_york
concept_personeurope_william_paley
concept_coach_douglas_edwards
cademicfield_media
concept_websit
concept_televisionstation_wcsc
Figure 17: PersonLeadsOrganization. The head is concept_journalist_bill_plante, the query rela-
tion is concept:organizationheadquarteredincity, and the desired tail is concept_company_cnn__pbs.
The left is a full subgraph derived with max_attended_nodes_per_step = 20, and the right is a
further extracted subgraph from the left based on attention. The big yellow node represents the head,
and the big red node represents the tail. Colors indicate how important a node is attended to in a local
subgraph. Grey means less important, yellow means it is more attended during the early steps, and
red means it is more attended when getting close to the ﬁnal step.
concept_stateorprovince_afternoon ,
concept : atdate ,
concept_date_n2003
concept_stateorprovince_afternoon ,
concept : atdate ,
concept_dateliteral_n2006
concept_dateliteral_n2007 ,
concept : atdate_inv ,
concept_country_united_states
concept_dateliteral_n2007 ,
concept : atdate_inv ,
concept_city_home
concept_dateliteral_n2007 ,
concept : atdate_inv ,
concept_city_service
concept_dateliteral_n2007 ,
concept : atdate_inv ,
concept_country_left_parties
concept_date_n2003 ,
concept : atdate_inv ,
concept_country_united_states
concept_date_n2003 ,
concept : atdate_inv ,
concept_city_home
concept_date_n2003 ,
concept : atdate_inv ,
concept_city_service
concept_date_n2003 ,
concept : atdate_inv ,
concept_country_left_parties
concept_dateliteral_n2006 ,
concept : atdate_inv ,
concept_country_united_states
concept_dateliteral_n2006 ,
concept : atdate_inv ,
concept_city_home
concept_dateliteral_n2006 ,
concept : atdate_inv ,
concept_city_service
concept_dateliteral_n2006 ,
concept : atdate_inv ,
concept_country_left_parties
concept_country_united_states ,
concept : atdate ,
concept_year_n1992
concept_country_united_states ,
concept : atdate ,
concept_year_n1997
concept_country_united_states ,
concept : organizationhiredperson ,
concept_personmexico_ryan_whitney
concept_city_home ,
concept : atdate ,
concept_year_n1992
concept_city_home ,
concept : atdate ,
concept_year_n1997
concept_city_home ,
concept : organizationhiredperson ,
concept_personmexico_ryan_whitney
concept_city_service ,
concept : atdate ,
concept_year_n1992
concept_city_service ,
concept : atdate ,
concept_year_n1997
concept_city_service ,
concept : organizationhiredperson ,
concept_personmexico_ryan_whitney
concept_country_left_parties ,
concept : worksfor_inv ,
concept_personmexico_ryan_whitney
concept_country_left_parties ,
concept : organizationhiredperson ,
concept_personmexico_ryan_whitney
concept_year_n1992 ,
concept : atdate_inv ,
concept_governmentorganization_house
concept_year_n1992 ,
concept : atdate_inv ,
concept_country_united_states
concept_year_n1992 ,
concept : atdate_inv ,
concept_city_home
concept_year_n1992 ,
concept : atdate_inv ,
concept_tradeunion_congress
concept_year_n1997 ,
concept : atdate_inv ,
concept_governmentorganization_house
concept_year_n1997 ,
concept : atdate_inv ,
concept_country_united_states
concept_year_n1997 ,
concept : atdate_inv ,
concept_city_home
concept_personmexico_ryan_whitney ,
concept : worksfor ,
concept_governmentorganization_house
concept_personmexico_ryan_whitney ,
concept : worksfor ,
concept_tradeunion_congress
concept_personmexico_ryan_whitney ,
concept : worksfor ,
concept_country_left_parties
concept_governmentorganization_house ,
concept : personbelongstoorganization_inv ,
concept_personus_party
concept_governmentorganization_house ,
concept : worksfor_inv ,
concept_personmexico_ryan_whitney
concept_governmentorganization_house ,
concept : organizationhiredperson ,
concept_personmexico_ryan_whitney
27


## Page 28


concept_stateorprovince_afternoon
concept_dateliteral_n2007
concept_dateliteral_n2006
concept_date_n2003
concept_dateliteral_n2002
concept_dateliteral_n2008
concept_dateliteral_n2005
concept_date_n2004
concept_date_n2001
concept_date_n1996
concept_date_n1999
concept_year_n1991
concept_year_n1998
concept_date_n2000
concept_book_new
concept_lake_new
concept_university_na
concept_city_home
concept_country_united_states
concept_city_service
concept_governmentorganization_law
concept_governmentorganization_program
concept_book_morning
concept_programminglanguage_project
concept_academicfield_directors
concept_musicsong_night
concept_website_tour
concept_country_israel
concept_musicsong_end
concept_book_years
concept_country_left_parties
concept_website_visit
concept_governmentorganization_fire
concept_academicfield_trial
concept_website_trip
concept_governmentorganization_launch
concept_company_case
concept_personmexico_ryan_whitney
concept_year_n1997
concept_year_n1992
concept_year_n1994
concept_year_n1995
concept_date_n1993
concept_date_n2009
concept_year_n1986
concept_date_n1968
concept_year_n1989
concept_year_n1975
concept_year_n1982
concept_director_committee
concept_dayofweek_wednesday
concept_date_n1944
concept_dateliteral_n1990
concept_year_n1978
concept_year_n1967
concept_dateliteral_n1987
concept_tradeunion_congress
concept_governmentorganization_house
concept_governmentorganization_epa
ncept_governmentorganization_commission
concept_nongovorganization_council
concept_politicsblog_white_house
concept_country_party
concept_geopoliticallocation_iraq
concept_county_records
oncept_city_capital
concept_city_team
concept_visualizablething_use
concept_biotechcompany_china
concept_governmentorganization_action
rnmentorganization_representatives
concept_city_members
concept_personus_party
concept_person_state
concept_buildingfeature_window
concept_politicianus_president_george_w__bush
concept_person_president
concept_person_mugabe
concept_personasia_number
concept_buildingfeature_windows
concept_astronaut_herbert_hoover
ept_stateorprovince_afternoon
concept_dateliteral_n2007
concept_dateliteral_n2006
concept_date_n2003
concept_dateliteral_n2002
concept_dateliteral_n2008
concept_city_home
concept_country_united_states
concept_city_service
concept_governmentorganization_law
concept_governmentorganization_program
concept_personmexico_ryan_whitney
concept_year_n1997
concept_year_n1992
concept_year_n1994
concept_tradeunion_congress
concept_governmentorganization_house
concept_governmentorganization_epa
concept_governmentorganiz
concept_personus_party
concept_country_left_parties
pt_person_state
Figure 18:
OrganizationHiredPerson.
The head is concept_stateorprovince_afternoon,
the
query
relation
is
concept:organizationhiredperson,
and
the
desired
tail
is
concept_personmexico_ryan_whitney.
The
left
is
a
full
subgraph
derived
with
max_attended_nodes_per_step = 20, and the right is a further extracted subgraph from
the left based on attention. The big yellow node represents the head, and the big red node represents
the tail. Colors indicate how important a node is attended to in a local subgraph. Grey means less
important, yellow means it is more attended during the early steps, and red means it is more attended
when getting close to the ﬁnal step.
concept_tradeunion_congress ,
concept : organizationhiredperson ,
concept_personus_party
concept_tradeunion_congress ,
concept : worksfor_inv ,
concept_personmexico_ryan_whitney
concept_tradeunion_congress ,
concept : organizationhiredperson ,
concept_personmexico_ryan_whitney
concept_country_left_parties ,
concept : organizationhiredperson ,
concept_personus_party
For the AgentBelongsToOrganization task
Query :
( concept_person_mark001 ,
concept : agentbelongstoorganization ,
concept_geopoliticallocation_world )
Selected key edges :
concept_person_mark001 ,
concept : personbelongstoorganization ,
concept_sportsteam_state_university
concept_person_mark001 ,
concept : agentcollaborateswithagent ,
concept_male_world
concept_person_mark001 ,
concept : agentcollaborateswithagent_inv ,
concept_male_world
concept_person_mark001 ,
concept : personbelongstoorganization ,
c o n c e p t _ p o l i t i c a l p a r t y _ c o l l e g e
concept_sportsteam_state_university ,
concept : personbelongstoorganization_inv ,
concept_politician_jobs
concept_sportsteam_state_university ,
concept : personbelongstoorganization_inv ,
concept_person_mark001
concept_sportsteam_state_university ,
concept : personbelongstoorganization_inv ,
concept_person_greg001
concept_sportsteam_state_university ,
concept : personbelongstoorganization_inv ,
concept_person_michael002
concept_male_world ,
concept : agentcollaborateswithagent ,
concept_politician_jobs
concept_male_world ,
concept : agentcollaborateswithagent_inv ,
concept_politician_jobs
concept_male_world ,
concept : agentcollaborateswithagent ,
concept_person_mark001
concept_male_world ,
concept : agentcollaborateswithagent_inv ,
concept_person_mark001
concept_male_world ,
concept : agentcollaborateswithagent ,
concept_person_greg001
concept_male_world ,
concept : agentcollaborateswithagent_inv ,
concept_person_greg001
concept_male_world ,
concept : agentcontrols ,
concept_person_greg001
concept_male_world ,
concept : agentcollaborateswithagent ,
concept_person_michael002
concept_male_world ,
concept : agentcollaborateswithagent_inv ,
concept_person_michael002
concept_politicalparty_college ,
concept : personbelongstoorganization_inv ,
concept_person_mark001
concept_politicalparty_college ,
concept : personbelongstoorganization_inv ,
concept_person_greg001
concept_politicalparty_college ,
concept : personbelongstoorganization_inv ,
concept_person_michael002
concept_politician_jobs ,
concept : personbelongstoorganization ,
concept_sportsteam_state_university
concept_politician_jobs ,
concept : agentcollaborateswithagent ,
concept_male_world
concept_politician_jobs ,
concept : agentcollaborateswithagent_inv ,
concept_male_world
concept_politician_jobs ,
concept : worksfor ,
concept_geopoliticallocation_world
concept_person_greg001 ,
concept : personbelongstoorganization ,
concept_sportsteam_state_university
concept_person_greg001 ,
concept : agentcollaborateswithagent ,
concept_male_world
28


## Page 29


concept_person_mark001
concept_sportsteam_state_university
concept_male_world
concept_politicalparty_college
concept_sportsgame_series
concept_university_state_university
concept_charactertrait_world
concept_university_college
concept_person_diane001
concept_university_high_school
concept_televisionshow_passion
concept_musicsong_gospel
10
concept_university_syracuse_university
concept_city_hampshire
concept_person_louise
concept_jobposition_king
concept_county_york_city
concept_stateorprovince_california
concept_stateorprovince_maine
concept_stateorprovince_georgia
concept_person_greg001
concept_person_michael002
concept_stateorprovince_author
concept_person_bill
concept_person_kevin
concept_person_john003
concept_politician_jobs
concept_person_mike
concept_person_stephen
concept_person_fred
concept_person_karen
concept_person_william001
concept_person_tom001
concept_journalist_dan
concept_person_joe002
concept_person_adam001
concept_politician_james
concept_eventoutcome_result
concept_geopoliticallocation_world
concept_recordlabel_friends
concept_politicalparty_house
concept_company_apple001
concept_televisionnetwo
concept_company_apple
3
concept_automobilemaker_announcement
concept_personmexico_ryan_whitney
concept_museum_steve
concept_city_downtown_manhattan
concept_attraction_nyc
concept_city_nyc_
concept_personasia_number
concept_scientist_no_
concept_country_united_states
ept_geopoliticallocation_agencies
ncept_company_nbc
concept_city_team
concept_terroristorganization_state
concept_automobilemaker_jeff_bezos
concept_ceo_richard
concept_lake_new
concept_city_service
concept_governmentorganization_u_s__department
concept_person_mark001
concept_sportsteam_state_university
concept_male_world
concept_politicalparty_college
sportsgame_series
concept_university_state_university
concept_person_greg001
concept_person_michael002
concept_stateorprovince_author
concept_geopoliticallocation_w
concept_recordlabel_friends
concept_personmexico_
concept_politician_jobs
concept_eventoutcome_result
concept_museum_steve
Figure 19: AgentBelongsToOrganization. The head is concept_person_mark001, the query relation
is concept:agentbelongstoorganization, and the desired tail is concept_geopoliticallocation_world.
The left is a full subgraph derived with max_attended_nodes_per_step = 20, and the right is a
further extracted subgraph from the left based on attention. The big yellow node represents the head,
and the big red node represents the tail. Colors indicate how important a node is attended to in a local
subgraph. Grey means less important, yellow means it is more attended during the early steps, and
red means it is more attended when getting close to the ﬁnal step.
concept_person_greg001 ,
concept : agentcollaborateswithagent_inv ,
concept_male_world
concept_person_greg001 ,
concept : agentcontrols_inv ,
concept_male_world
concept_person_greg001 ,
concept : agentbelongstoorganization ,
concept_geopoliticallocation_world
concept_person_greg001 ,
concept : personbelongstoorganization ,
c o n c e p t _ p o l i t i c a l p a r t y _ c o l l e g e
concept_person_greg001 ,
concept : agentbelongstoorganization ,
concept_recordlabel_friends
concept_person_michael002 ,
concept : personbelongstoorganization ,
concept_sportsteam_state_university
concept_person_michael002 ,
concept : agentcollaborateswithagent ,
concept_male_world
concept_person_michael002 ,
concept : agentcollaborateswithagent_inv ,
concept_male_world
concept_person_michael002 ,
concept : agentbelongstoorganization ,
concept_geopoliticallocation_world
concept_person_michael002 ,
concept : personbelongstoorganization ,
c o n c e p t _ p o l i t i c a l p a r t y _ c o l l e g e
concept_geopoliticallocation_world ,
concept : worksfor_inv ,
concept_personmexico_ryan_whitney
concept_geopoliticallocation_world ,
concept : organizationhiredperson ,
concept_personmexico_ryan_whitney
concept_geopoliticallocation_world ,
concept : worksfor_inv ,
concept_politician_jobs
concept_recordlabel_friends ,
concept : organizationhiredperson ,
concept_personmexico_ryan_whitney
concept_personmexico_ryan_whitney ,
concept : worksfor ,
concept_geopoliticallocation_world
concept_personmexico_ryan_whitney ,
concept : organizationhiredperson_inv ,
concept_geopoliticallocation_world
concept_personmexico_ryan_whitney ,
concept : organizationhiredperson_inv ,
concept_recordlabel_friends
For the TeamPlaysInLeague task
Query :
( concept_sportsteam_mavericks ,
concept : teamplaysinleague ,
concept_sportsleague_nba )
Selected key edges :
concept_sportsteam_mavericks ,
concept : teamplayssport ,
concept_sport_basketball
concept_sportsteam_mavericks ,
concept : teamplaysagainstteam ,
concept_sportsteam_boston_celtics
concept_sportsteam_mavericks ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_boston_celtics
concept_sportsteam_mavericks ,
concept : teamplaysagainstteam ,
concept_sportsteam_spurs
concept_sportsteam_mavericks ,
concept : teamplaysagainstteam_inv ,
concept_sportsteam_spurs
concept_sport_basketball ,
concept : teamplayssport_inv ,
concept_sportsteam_college
concept_sport_basketball ,
concept : teamplayssport_inv ,
concept_sportsteam_marshall_university
concept_sportsteam_boston_celtics ,
concept : teamplaysinleague ,
concept_sportsleague_nba
concept_sportsteam_spurs ,
concept : teamplaysinleague ,
concept_sportsleague_nba
concept_sportsleague_nba ,
concept : agentcompeteswithagent ,
concept_sportsleague_nba
concept_sportsleague_nba ,
concept : agentcompeteswithagent_inv ,
concept_sportsleague_nba
concept_sportsteam_college ,
concept : teamplaysinleague ,
concept_sportsleague_international
29


## Page 30


concept_sportsteam_mavericks
concept_sport_basketball
concept_sportsteam_boston_celtics
concept_sportsteam_spurs
concept_sportsteam_suns
concept_sportsteam_esu_hornets
concept_sportsteam_rockets
concept_sportsteam_knicks
concept_sportsteam_memphis_grizzlies
concept_sportsteam_kings_college
concept_sportsteam_san_antonio
concept_sportsgame_series
concept_sportsteam_chicago_bulls
concept_sportsteam_golden_state_warriors
concept_sportsteam_utah_jazz
concept_sportsgame_championship
concept_sportsteam_la_clippers
concept_convention_games
concept_athlete_josh_howard
concept_awardtrophytournament_nba_finals
concept_sportsteam_marshall_university
concept_sportsleague_nba
concept_sportsteam_college
concept_sportsteam_pacers
concept_athlete_o__j__simpson
concept_sportsteam_devils
concept_athlete_dikembe_mutombo
concept_sportsleague_nascar
concept_sportsteam_pistons
concept_sportsteam_los_angeles_lakers
t_athlete_shane_battier
concept_sportsteam_hawks
concept_sportsteam_washington_wizards
concept_sportsteam_michigan_state_university
concept_sportsteam_new_jersey_nets
concept_sportsteam_astros
concept_sportsteam_trail_blazers
concept_athlete_cuttino_mobley
concept_sportsteam_george_mason_university
concept_athlete_colin_long
concept_sportsleague_international
concept_city_huntington
concept_sportsleague
concept_sportsleague_mlb
concept_stadiumoreventvenue_toyota_center
concept_sportsteam_mavericks
concept_sport_basketball
concept_sportsteam_boston_celtics
concept_sportsteam_spurs
concept_sportsteam_suns
concept_sportsteam_esu_hornets
concept_sportsteam_marshall_university
concept_sportsleague_nba
concept_sportsteam_college
concept_sportsteam_pacers
thlete_o__j__simpson
concept_sportsleague_
concept_city_huntington
concept_sportsleague_nhl
concept_sportsleague_nascar
Figure 20: TeamPlaysInLeague. The head is concept_sportsteam_mavericks, the query relation
is concept:teamplaysinleague, and the desired tail is concept_sportsleague_nba. The left is a full
subgraph derived with max_attended_nodes_per_step = 20, and the right is a further extracted
subgraph from the left based on attention. The big yellow node represents the head, and the big red
node represents the tail. Colors indicate how important a node is attended to in a local subgraph.
Grey means less important, yellow means it is more attended during the early steps, and red means it
is more attended when getting close to the ﬁnal step.
30

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1905_13049v1_neural_consciousness_flow
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1905_13049V1_NEURAL_CONSCIOUSNESS_FLOW.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

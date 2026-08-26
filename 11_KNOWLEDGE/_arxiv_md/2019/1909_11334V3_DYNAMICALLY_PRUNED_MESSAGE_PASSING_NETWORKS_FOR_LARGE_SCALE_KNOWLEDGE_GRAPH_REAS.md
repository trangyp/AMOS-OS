---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1909.11334v3
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1909.11334v3_Dynamically_Pruned_Message_Passing_Networks_for_Large-Scale_Knowledge_Graph_Reas

> Source: 1909.11334v3_Dynamically_Pruned_Message_Passing_Networks_for_Large-Scale_Knowledge_Graph_Reas.pdf

> Pages: 30

---


## Page 1


Published as a conference paper at ICLR 2020
DYNAMICALLY PRUNED MESSAGE PASSING NET-
WORKS
FOR
LARGE-SCALE
KNOWLEDGE
GRAPH
REASONING
Xiaoran Xu1, Wei Feng1, Yunsheng Jiang1, Xiaohui Xie1, Zhiqing Sun2, Zhi-Hong Deng3
1Hulu, {xiaoran.xu, wei.feng, yunsheng.jiang, xiaohui.xie}@hulu.com
2Carnegie Mellon University, zhiqings@andrew.cmu.edu
3Peking University, zhdeng@pku.edu.cn
ABSTRACT
We propose Dynamically Pruned Message Passing Networks (DPMPN) for large-
scale knowledge graph reasoning. In contrast to existing models, embedding-
based or path-based, we learn an input-dependent subgraph to explicitly model
reasoning process. Subgraphs are dynamically constructed and expanded by ap-
plying graphical attention mechanism conditioned on input queries. In this way,
we not only construct graph-structured explanations but also enable message pass-
ing designed in Graph Neural Networks (GNNs) to scale with graph sizes. We take
the inspiration from the consciousness prior proposed by Bengio (2017) and de-
velop a two-GNN framework to simultaneously encode input-agnostic full graph
representation and learn input-dependent local one coordinated by an attention
module. Experiments demonstrate the reasoning capability of our model that is to
provide clear graphical explanations as well as deliver accurate predictions, out-
performing most state-of-the-art methods in knowledge base completion tasks.
1
INTRODUCTION
Modern deep learning systems should bring in explicit reasoning modeling to complement their
black-box models, where reasoning takes a step-by-step form about organizing facts to yield new
knowledge and ﬁnally draw a conclusion. Particularly, we rely on graph-structured representation
to model reasoning by manipulating nodes and edges where semantic entities or relations can be
explicitly represented (Battaglia et al., 2018). Here, we choose knowledge graph scenarios to study
reasoning where semantics have been deﬁned on nodes and edges. For example, in knowledge base
completion tasks, each edge is represented by a triple ⟨head, rel, tail⟩that contains two entities and
their relation. The goal is to predict which entity might be a tail given query ⟨head, rel, ?⟩.
Existing models can be categorized into embedding-based and path-based model families. The
embedding-based (Bordes et al., 2013; Sun et al., 2018; Lacroix et al., 2018) often achieves a high
score by ﬁtting data using various neural network techniques but lacks interpretability. The path-
based (Xiong et al., 2017; Das et al., 2018; Shen et al., 2018; Wang, 2018) attempts to construct an
explanatory path to model an iterative decision-making process using reinforcement learning and
recurrent networks. A question is: can we construct structured explanations other than a path to
better explain reasoning in graph context. To this end, we propose to learn a dynamically induced
subgraph which starts with a head node and ends with a predicted tail node as shown in Figure 1.
Graph reasoning can be powered by Graph Neural Networks. Graph reasoning needs to learn
about entities, relations, and their composing rules to manipulate structured knowledge and produce
structured explanations. Graph Neural Networks (GNNs) provide such structured computation and
also inherit powerful data-ﬁtting capacity from deep neural networks (Scarselli et al., 2009; Battaglia
et al., 2018). Speciﬁcally, GNNs follow a neighborhood aggregation scheme to recursively aggregate
information from neighbors to update node states. After T iterations, each node can carry structure
information from its T-hop neighborhood (Gilmer et al., 2017; Xu et al., 2018a).
GNNs need graphical attention expression to interpret. Neighborhood attention operation is a
popular way to implement attention mechanism on graphs (Velickovic et al., 2018; Hoshen, 2017)
1
arXiv:1909.11334v3  [cs.AI]  7 Apr 2020


## Page 2


Published as a conference paper at ICLR 2020
(a) The AthletePlaysForTeam task.
(b) The OrganizationHiredPerson task.
Figure 1: Subgraph visualization on two examples from NELL995’s test data. Each task has ten
thousands of nodes and edges. The big yellow represents a given head and the big red represents a
predicted tail. Color indicates attention gained along T-step reasoning. Yellow means more attention
during early steps while red means more attention at the end. Grey means less attention.
by focusing on speciﬁc interactions with neighbors. Here, we propose a new graphical attention
mechanism not only for computation but also for interpretation. We present three considerations
when constructing attention-induced subgraphs: (1) given a subgraph, we ﬁrst attend within it to
select a few nodes and then attend over those nodes’ neighborhood for next expansion; (2) we prop-
agate attention across steps to capture long-term dependency; (3) our attention mechanism models
reasoning process explicitly through cascading computing pipeline that is disentangled from and
runs above underlying representation computation.
GNNs need input-dependent pruning to scale. GNNs are notorious for their poor scalability.
Consider one message passing iteration on a graph with |V | nodes and |E| edges. Even if the graph
is sparse, the complexity of O(|E|) is still problematic on large graphs with millions of nodes and
edges. Besides, mini-batch based training with batch size B and high dimensions D would lead to
O(BD|E|) making things worse. However, we can avoid this situation by learning input-dependent
pruning to run computation on dynamical subgraphs, as an input query often triggers a small fraction
of the entire graph so that it is wasteful to perform computation over the full graph for each input.
Cognitive intuition of the consciousness prior. Bengio (2017) brought the notion of attentive
awareness from cognitive science into deep learning in his consciousness prior proposal. He pointed
out a process of disentangling high-level factors from full underlying representation to form a low-
dimensional combination through attention mechanism. He proposed to use two recurrent neural
networks (RNNs) to encode two types of state: unconscious state represented by a high-dimensional
vector before attention and conscious state by a derived low-dimensional vector after attention.
We use two GNNs instead to encode such states on nodes. We construct input-dependent subgraphs
to run message passing efﬁciently, and also run full message passing over the entire graph to acquire
features beyond a local view constrained by subgraphs. We apply attention mechanism between
the two GNNs, where the bottom runs before attention, called Inattentive GNN (IGNN), and the
above runs on each attention-induced subgraph, called Attentive GNN (AGNN). IGNN provides
representation computed on the full graph for AGNN. AGNN further processes representation within
a group of relevant nodes to produce sharp semantics. Experimental results show that our model
attains very competitive scores on HITS@1,3 and the mean reciprocal rank (MRR) compared to the
best existing methods so far. More importantly, we provide explanations while they do not.
2
ADDRESSING THE SCALE-UP PROBLEM
Notation.
We denote training data by {(xi, yi)}N
i=1.
We denote a full graph by G = ⟨V, E⟩
with relations R and an input-dependent subgraph by G(x) = ⟨VG(x), EG(x)⟩which is an in-
duced subgraph of G. We denote boundary of a graph by ∂G where V∂G = N(VG) −VG and
N(VG) means neighbors of nodes in VG. We also denote high-order boundaries such as ∂2G where
2


## Page 3


Published as a conference paper at ICLR 2020
V∂2G = N(N(VG)) ∪N(VG) −VG. Trainable parameters include node embeddings {ev}v∈V,
relation embeddings {er}r∈R, and weights used in two GNNs and an attention module. When per-
forming full or pruned message passing, node and relation embeddings will be indexed according to
the operated graph, denoted by θG or θG(x). For IGNN, we use Ht of size |V| × D to denote node
hidden states at step t; for AGNN, we use Ht(x) of size |VG(x)| × D to denote. The objective is
written as PN
i=1 l(xi, yi; θG(xi), θG), where G(xi) is dynamically constructed.
The scale-up problem in GNNs. First, we write the full message passing in IGNN as
Ht = fIGNN(Ht−1; θG),
(1)
where fIGNN represents all involved operations in one message passing iteration over G, including:
(1) computing messages along each edge with the complexity1 of O(BD|E|), (2) aggregating mes-
sages received at each node with O(BD|E|), and (3) updating node states with O(BD|V|). For
T-step propagation, the per-batch complexity is O(BDT(|E| + |V|)). Considering that backpropa-
gation requires intermediate computation results to be saved during one pass, this complexity counts
for both time and space. However, since IGNN is input-agnostic, node representations can be shared
across inputs in one batch so that we can remove B to get O(DT(|E| + |V|)). If we use a sampled
edge set ˆE from E such that | ˆE| ≈k|V|, the complexity can be further reduced to O(DT|V|).
The pruned message passing in AGNN can be written as
Ht(x) = fAGNN(Ht−1(x), Ht; θG(x)).
(2)
Its complexity can be computed similarly as above. However, we cannot remove B. Fortunately,
subgraph G(x) is not G. If we let x be a node v, G(x) grows from a single node, i.e., G0(x) = {v},
and expands itself each step, leading to a sequence of (G0(x), G1(x), . . . , GT (x)). Here, we de-
scribe the expansion behavior as consecutive expansion, which means no jumping across neighbor-
hood allowed, so that we can ensure that
Gt(x) ⊆Gt−1(x) ∪∂Gt−1(x) ⊆Gt−2(x) ∪∂2Gt−2(x).
(3)
Many real-world graphs follow the small-world pattern, and the six degrees of separation implies
G0(x) ∪∂6G0(x) ≈G. The upper bound of Gt(x) can grow exponentially in t, and there is no
guarantee that Gt(x) will not explode.
Proposition. Given a graph G (undirected or directed in both directions), we assume the probability
of the degree of an arbitrary node being less than or equal to d is larger than p, i.e., P(deg(v) ≤
d) > p, ∀v ∈V . Considering a sequence of consecutively expanding subgraphs (G0, G1, . . . , GT ),
starting with G0 = {v}, for all t ≥1, we can ensure
P
 |VGt| ≤d(d −1)t −2
d −2

> p
d(d−1)t−1−2
d−2
.
(4)
The proposition implies the guarantee of upper-bounding |VGt(x)| becomes exponentially looser and
weaker as t gets larger even if the given assumption has a small d and a large p (close to 1). We
deﬁne graph increment at step t as ∆Gt(x) such that Gt(x) = Gt−1(x) ∪∆Gt(x). To prevent
Gt(x) from explosion, we need to constrain ∆Gt(x).
Sampling strategies. A simple but effective way to handle the large scale is to do sampling.
1. ∆Gt(x) = ˆ∂Gt−1(x), where we sample nodes from the boundary of Gt−1(x).
2. ∆Gt(x) = ∂\
Gt−1(x), where we take the boundary of sampled nodes from Gt−1(x).
3. ∆Gt(x) = ˆ∂\
Gt−1(x), where we sample nodes twice from Gt−1(x) and from ∂\
Gt−1(x).
4. ∆Gt(x) = ˆ∂\
Gt−1(x)
b, where we sample nodes three times with the last from ˆ∂\
Gt−1(x).
Obviously, we have ˆ∂\
Gt−1(x)
b ⊆ˆ∂\
Gt−1(x) ⊆∂\
Gt−1(x) and Gt−1(x) ∪∂\
Gt−1(x) ⊆Gt−1(x) ∪
∂Gt−1(x). Further, we let N1 and N3 be the maximum number of sampled nodes in ∂\
Gt−1(x) and
the last sampling of ˆ∂\
Gt−1(x)
b respectively and let N2 be per-node maximum sampled neighbors in
ˆ∂Gt−1(x), and then we can obtain much tighter guarantee as follow:
1We assume per-example per-edge per-dimension time cost as a unit time.
3


## Page 4


Published as a conference paper at ICLR 2020
Aggr
Op
...  
...
...  
Aggr
Op
...  
Attd
Op
...
Inattentive GNN
Attentive GNN
One
Batch
Attention Module
...  
Pooling or returning the last
Figure 2: Model architecture used in knowledge graph reasoning.
1. P(|V∆Gt(x)| ≤N1(d −1)) > pN1 for ∂\
Gt−1(x).
2. P(|V∆Gt(x)| ≤N1N2) = 1 and P(|V∆Gt(x)| ≤N1·min(d−1, N2)) > pN1 for ˆ∂\
Gt−1(x).
3. P(|V∆Gt(x)| ≤min(N1N2, N3)) = 1 for ˆ∂\
Gt−1(x)
b.
Attention strategies. Although we guarantee |VGT (x)| ≤1 + T min(N1N2, N3) by ˆ∂\
Gt−1(x)
b and
constrain the growth of Gt−1(x) by decreasing either N1N2 or N3, smaller sampling size means
less area explored and less chance to hit target nodes. To make efﬁcient selection rather than ran-
dom sampling, we apply attention mechanism to do the top-K selection where K can be small. We
change ˆ∂\
Gt−1(x)
b to ˆ∂Gt−1(x)
e
e where ∼represents the operation of attending over nodes and pick-
ing the top-K. There are two types of attention operations, one applied to Gt−1(x) and the other
applied to ˆ∂Gt−1(x)
e. Note that the size of ˆ∂Gt−1(x)
e might be much larger if we intend to sample
more nodes with larger N2 to sufﬁciently explore the boundary. Nevertheless, we can address this
problem by using smaller dimensions to compute attention, since attention on each node is a scalar
requiring a smaller capacity compared to node representation vectors computed in message passing.
3
DPMPN MODEL
3.1
ARCHITECTURE DESIGN FOR KNOWLEDGE GRAPH REASONING
Our model architecture as shown in Figure 2 consists of:
• IGNN module: performs full message passing to compute full-graph node representations.
• AGNN module: performs a batch of pruned message passing to compute input-dependent node
representations which also make use of underlying representations from IGNN.
• Attention Module: performs a ﬂow-style attention transition process, conditioned on node repre-
sentations from both IGNN and AGNN but only affecting AGNN.
IGNN module. We implement it using standard message passing mechanism (Gilmer et al., 2017).
If the full graph has an extremely large number of edges, we sample a subset of edges, ˆEτ ⊂E,
randomly each step. For a batch of input queries, we let node representations from IGNN be shared
across queries, containing no batch dimension. Thus, its complexity does not scale with batch size
and the saved resources can be allocated to sampling more edges. Each node v has a state Hτ
v,: at
step τ, where the initial H0
v,: = ev. Each edge ⟨v′, r, v⟩produces a message, denoted by Mτ
⟨v′,r,v⟩,:
at step τ. The computation components include:
4


## Page 5


Published as a conference paper at ICLR 2020
• Message function: Mτ
⟨v′,r,v⟩,: = ψIGNN(Hτ
v′,:, er, Hτ
v,:), where ⟨v′, r, v⟩∈ˆEτ.
• Message aggregation: M
τ
v,: =
1
√
N τ (v)
P
v′,r Mτ
⟨v′,r,v⟩,:, where ⟨v′, r, v⟩∈ˆEτ.
• Node state update function: Hτ+1
v,:
= Hτ
v,: + δIGNN(Hτ
v,:, M
τ
v,:, ev), where v ∈V.
We compute messages only for sampled edges, ⟨v′, r, v⟩∈ˆEτ, each step. Functions ψIGNN and
δIGNN are implemented by a two-layer MLP (using leakyReLu for the ﬁrst layer and tanh for the
second) with input arguments concatenated respectively. Messages are aggregated by dividing the
sum by the square root of N τ(v), the number of neighbors that send messages to v, preserving the
scale of variance. We use a residual adding to update each node state instead of a GRU or a LSTM.
After running for T steps, we output a pooling result or simply the last, denoted by H = HT , to
feed into downstream modules.
AGNN module.
AGNN is input-dependent, which means node states depend on input query
x = ⟨head, rel, ?⟩, denoted by Ht
v,:(x). We implement pruned message passing, running on small
subgraphs each conditioned on an input query. We leverage the sparsity and only save Ht
v,:(x) for
visited nodes v ∈VGt(x). When t = 0, we start from node head with VG0(x) = {vhead}. When
computing messages, denoted by M t
⟨v′,r,v⟩,:(x), we use an attending-sampling-attending procedure,
explained in Section 3.2, to constrain the number of computed edges. The computation components
include:
• Message function: M t
⟨v′,r,v⟩,:(x) = ψAGNN(Ht
v′,:(x), cr(x), Ht
v,:(x)), where ⟨v′, r, v⟩∈
EGt(x)2, and cr(x) = [er, qhead, qrel] represents a context vector.
• Message aggregation: M
t
v,:(x) =
1
√
Nt(v)
P
v′,r M t
⟨v′,r,v⟩,:(x), where ⟨v′, r, v⟩∈EGt(x).
• Node state attending function: f
Ht+1
v,: (x) = at+1
v
W Hv,:, where at+1
v
is an attention score.
• Node state update function: Ht+1
v,: (x) = Ht
v,:(x) + δAGNN(Ht
v,:(x), M
t
v,:(x), ct+1
v
(x)), where
ct+1
v
(x) = [f
Ht+1
v,: (x), qhead, qrel] also represents a context vector.
Query context is deﬁned by its head and relation embeddings, i.e., qhead = ehead and qrel = erel.
We introduce a node state attending function to pass node representation information from IGNN
to AGNN weighted by a scalar attention score at+1
v
and projected by a learnable matrix W . We
initialize H0
v,:(x) = Hv,: for node v ∈VG0(x), letting unseen nodes hold zero states.
Attention module. Attention over T steps is represented by a sequence of node probability dis-
tributions, denoted by at (t = 1, 2 . . . , T). The initial distribution a0 is a one-hot vector with
a0[vhead] = 1. To spread attention, we need to compute transition matrices T t each step. Since
it is conditioned on both IGNN and AGNN, we capture two types of interaction between v′ and v:
Ht
v′,:(x) ∼Ht
v,:(x), and Ht
v′,:(x) ∼Hv,:. The former favors visited nodes, while the latter is used
to attend to unseen neighboring nodes.
T t
:,v′ = softmaxv∈Nt(v′)
  X
r α1(Ht
v′,:(x), cr(x), Ht
v,:(x)) + α2(Ht
v′,:(x), cr(x), Hv,:)

α1(·) = MLP(Ht
v′,:(x), cr(x))TW1MLP(Ht
v,:(x), cr(x))
α2(·) = MLP(Ht
v′,:(x), cr(x))TW2MLP(Hv,:, cr(x))
(5)
where W1 and W2 are two learnable matrices. Each MLP uses one single layer with the leakyReLu
activation. To reduce the complexity for computing T t, we use nodes v′ ∈V
Gt(x)
e
, which contains
nodes with the k-largest attention scores at step t, and use nodes v sampled from v′’s neighbors
to compute attention transition for the next step. Due to the fact that nodes v′ result from the
top-k pruning, the loss of attention may occur to diminish the total amount. Therefore, we use a
renormalized version, at+1 = T tat/∥T tat∥, to compute new attention scores. We use attention
scores at the ﬁnal step as the probability to predict the tail node.
2In practice, we can use a smaller set of edges than EGt(x) to pass messages as discussed in Section 3.2
5


## Page 6


Published as a conference paper at ICLR 2020
Sampling Horizon
Attending-to Horizon
Attending-from Horizon
Visited Nodes
Visited Nodes
Full Neighborhood
Sampling Horizon
Attending-to Horizon
Attending-from Horizon
Full Neighborhood
Figure 3: Iterative attending-sampling-attending procedure balancing coverage and complexity.
3.2
COMPLEXITY REDUCTION BY ITERATIVE ATTENDING, SAMPLING AND ATTENDING
AGNN deals with each subgraph relying on input x and keeps a few selected nodes in VGt(x), called
visited nodes. Initially, VG0(x) contains only one node vhead, and then VGt(x) is enlarged by adding
new nodes each step. When propagating messages, we can just consider the one-hop neighborhood
each step. However, the expansion goes so rapidly that it covers almost all nodes after a few steps.
The key to address the problem is to constrain the scope of nodes we can expand the boundary from,
i.e., the core nodes which determine where we can go next. We call it the attending-from horizon,
Gt(x)
e, selected according to attention scores at. Given this horizon, we may still need node sam-
pling over the neighborhood N(Gt(x)
e) in some cases where a hub node of extremely high degree
exists to cause an extremely large neighborhood. We introduce an attending-to horizon, denoted by
b
N(Gt(x)
e)
e, inside the sampling horizon, denoted by b
N(Gt(x)
e). The attention module runs within
the sampling horizon with smaller dimensions exchanged for sampling more neighbors for a larger
coverage. In one word, we face a trade-off between coverage and complexity, and our strategy is
to sample more but attend less plus using small dimensions to compute attention. We obtain the
attending-to horizon according to newly computed attention scores at+1. Then, message passing
iteration at step t in AGNN can be further constrained on edges between Gt(x)
e and b
N(Gt(x)
e)
e, a
smaller set than EGt(x). We illustrate this procedure in Figure 3.
4
EXPERIMENTS
Datasets. We use six large KG datasets: FB15K, FB15K-237, WN18, WN18RR, NELL995, and
YAGO3-10. FB15K-237 (Toutanova & Chen, 2015) is sampled from FB15K (Bordes et al., 2013)
with redundant relations removed, and WN18RR (Dettmers et al., 2018) is a subset of WN18 (Bor-
des et al., 2013) removing triples that cause test leakage. Thus, they are both considered more
challenging. NELL995 (Xiong et al., 2017) has separate datasets for 12 query relations each corre-
sponding to a single-query-relation KBC task. YAGO3-10 (Mahdisoltani et al., 2014) contains the
largest KG with millions of edges. Their statistics are shown in Table 1. We ﬁnd some statistical
differences between train and validation (or test). In a KG with all training triples as its edges, a
triple (head, rel, tail) is considered as a multi-edge triple if the KG contains other triples that also
connect head and tail ignoring the direction. We notice that FB15K-237 is a special case compared
to the others, as there are no edges in its KG directly linking any pair of head and tail in valida-
tion (or test). Therefore, when using training triples as queries to train our model, given a batch,
for FB15K-237, we cut off from the KG all triples connecting the head-tail pairs in the given batch,
ignoring relation types and edge directions, forcing the model to learn a composite reasoning pattern
rather than a single-hop pattern, and for the rest datasets, we only remove the triples of this batch
and their inverse from the KG to avoid information leakage before training on this batch. This can
be regarded as a hyperparameter tuning whether to force a multi-hop reasoning or not, leading to a
performance boost of about 2% in HITS@1 on FB15-237.
Experimental settings. We use the same data split protocol as in many papers (Dettmers et al.,
2018; Xiong et al., 2017; Das et al., 2018). We create a KG, a directed graph, consisting of all
train triples and their inverse added for each dataset except NELL995, since it already includes
reciprocal relations. Besides, every node in KGs has a self-loop edge to itself. We also add inverse
relations into the validation and test set to evaluate the two directions. For evaluation metrics, we use
HITS@1,3,10 and the mean reciprocal rank (MRR) in the ﬁltered setting for FB15K-237, WN18RR,
6


## Page 7


Published as a conference paper at ICLR 2020
Table 1: Statistics of the six KG datasets. PME (tr) means the proportion of multi-edge triples in
train; PME (va) means the proportion of multi-edge triples in validation; AL (va) means the average
length of shortest paths connecting each head-tail pair in validation.
Dataset
#Entities
#Rels
#Train
#Valid
#Test
PME (tr)
PME (va)
AL (va)
FB15K
14,951
1,345
483,142
50,000
59,071
81.2%
80.6%
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
35.5%
2.84
NELL995
74,536
200
149,678
543
2,818
100%
31.1%
2.00
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
from (Nguyen et al., 2018), [♣] from (Dettmers et al., 2018), [♥] from (Shen et al., 2018), [♦] from
(Sun et al., 2018), [△] from (Das et al., 2018), and [✠] from (Lacroix et al., 2018). Some collected
results only have a metric score while some including ours take the form of “mean (std)”.
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
20.6 (.4)
31.8 (.2)
-
29.0 (.2)
38.4 (.4)
42.4 (.3)
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
20.8 (.2)
32.6 (.5)
-
29.6 (.2)
38.5 (.3)
43.9 (.3)
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
23.3 (.4)
33.8 (.3)
-
30.8 (.2)
39.6 (.3)
44.7 (.2)
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
ComplEx-N3[✠]
-
-
56
37
-
-
57
48
NeuralLP [♥]
18.2 (.6)
27.2 (.3)
-
24.9 (.2)
37.2 (.1)
43.4 (.1)
-
43.5 (.1)
MINERVA [♥]
14.1 (.2)
23.2 (.4)
-
20.5 (.3)
35.1 (.1)
44.5 (.4)
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
16.5 (.3)
24.3 (.2)
-
23.2 (.2)
41.4 (.1)
44.5 (.2)
-
43.7 (.1)
DPMPN
28.6 (.1)
40.3 (.1)
53.0 (.3)
36.9 (.1)
44.4 (.4)
49.7 (.8)
55.8 (.5)
48.2 (.5)
FB15K, WN18, and YAGO3-10, and use the mean average precision (MAP) for NELL995’s single-
query-relation KBC tasks. For NELL995, we follow the same evaluation procedure as in (Xiong
et al., 2017; Das et al., 2018; Shen et al., 2018), ranking the answer entities against the negative
examples given in their experiments. We run our experiments using a 12G-memory GPU, TITAN
X (Pascal), with Intel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz. Our code is written in Python
based on TensorFlow 2.0 and NumPy 1.16 and can be found by the link3 below. We run three
times for each hyperparameter setting per dataset to report the means and standard deviations. See
hyperparameter details in the appendix.
Baselines. We compare our model against embedding-based approaches, including TransE (Bordes
et al., 2013), TransR (Lin et al., 2015b), DistMult (Yang et al., 2015), ConvE (Dettmers et al.,
2018), ComplE (Trouillon et al., 2016), HolE (Nickel et al., 2016), RotatE (Sun et al., 2018), and
ComplEx-N3 (Lacroix et al., 2018), and path-based approaches that use RL methods, including
DeepPath (Xiong et al., 2017), MINERVA (Das et al., 2018), and M-Walk (Shen et al., 2018), and
also that uses learned neural logic, NeuralLP (Yang et al., 2017).
Comparison results and analysis. We report comparison on FB15K-23 and WN18RR in Table 2.
Our model DPMPN signiﬁcantly outperforms all the baselines in HITS@1,3 and MRR. Compared
to the best baseline, we only lose a few points in HITS@10 but gain a lot in HITS@1,3. We
speculate that it is the reasoning capability that helps DPMPN make a sharp prediction by exploiting
graph-structured composition locally and conditionally. When a target becomes too vague to predict,
reasoning may lose its advantage against embedding-based models. However, path-based baselines,
with a certain ability to do reasoning, perform worse than we expect. We argue that it might be
inappropriate to think of reasoning, a sequential decision process, equivalent to a sequence of nodes.
The average lengths of the shortest paths between heads and tails as shown in Table 1 suggests a very
short path, which makes the motivation of using a path almost useless. The reasoning pattern should
be modeled in the form of dynamical local graph-structured pattern with nodes densely connected
3https://github.com/anonymousauthor123/DPMPN
7


## Page 8


Published as a conference paper at ICLR 2020
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
(A) Convergence Analysis (eval on test)
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
(B) IGNN Component Analysis
W/o IGNN
With IGNN
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
Max-sampling-per-node = 20
Max-sampling-per-node = 50
Max-sampling-per-node = 100
Max-sampling-per-node = 200
Max-sampling-per-node = 400
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
Max-atteding-to-per-step = 20
Max-atteding-to-per-step = 50
Max-atteding-to-per-step = 100
Max-atteding-to-per-step = 200
Max-atteding-to-per-step = 400
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
Max-atteding-from-per-step = 5
Max-atteding-from-per-step = 10
Max-atteding-from-per-step = 20
Max-atteding-from-per-step = 40
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
#Steps-in-AGNN = 2
#Steps-in-AGNN = 4
#Steps-in-AGNN = 6
#Steps-in-AGNN = 8
Figure 4: Experimental analysis on WN18RR. (A) Convergence analysis: we pick six model snap-
shots during training and evaluate them on test. (B) IGNN component analysis: w/o IGNN uses zero
step to run message passing, while with IGNN uses two; (C)-(F) Sampling, attending-to, attending-
from and searching horizon analysis. The charts on FB15K-237 can be found in the appendix.
with each other to produce a decision collectively. We also run our model on FB15K, WN18,
and YAGO3-10, and the comparison results in the appendix show that DPMPN achieves a very
competitive position against the best state of the art. We summarize the comparison on NELL995’s
tasks in the appendix. DPMPN performs the best on ﬁve tasks, also being competitive on the rest.
Convergence analysis. Our model converges very fast during training. We may use half of train-
ing queries to train model to generalize as shown in Figure 4(A). Compared to less expensive
embedding-based models, our model need to traverse a number of edges when training on one
input, consuming much time per batch, but it does not need to pass a second epoch, thus saving a lot
of training time. The reason may be that training queries also belong to the KG’s edges and some
might be exploited to construct subgraphs during training on other queries.
Component analysis. Given the stacked GNN architecture, we want to examine how much each
GNN component contributes to the performance. Since IGNN is input-agnostic, we cannot rely
on its node representations only to predict a tail given an input query. However, AGNN is input-
dependent, which means it can be carried out to complete the task without taking underlying node
representations from IGNN. Therefore, we can arrange two sets of experiments: (1) AGNN + IGNN,
and (2) AGNN-only. In AGNN-only, we do not run message passing in IGNN to compute Hv,:
but instead use node embeddings as Hv,:, and then we run pruned message passing in AGNN as
usual. We want to be sure whether IGNN is actually useful. In this setting, we compare the ﬁrst
set which runs IGNN for two steps against the second one which totally shuts IGNN down. The
results in Figure 4(B) (and Figure 7(B) in Appendix) show that IGNN brings an amount of gains in
each metric on WN18RR (and FB15K-23), indicating that representations computed by full-graph
message passing indeed help subgraph-based message passing.
Horizon analysis. The sampling, attending-to, attending-from and searching (i.e., propagation
steps) horizons determine how large area a subgraph can expand over. These factors affect com-
putation complexity as well as prediction performance. Intuitively, enlarging the exploring area by
sampling more, attending more, and searching longer, may increase the chance of hitting a target
to gain some performance. However, the experimental results in Figure 4(C)(D) show that it is not
always the case. In Figure 4(E), we can see that increasing the maximum number of attending-
8


## Page 9


Published as a conference paper at ICLR 2020
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
(B) Attention Flow Analysis (top1's proportion)
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
(C) Attention Flow Analysis (top3's proportion)
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
(D) Attention Flow Analysis (top5's proportion)
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
Figure 5: Analysis of attention ﬂow on NELL995 tasks. (A) The average entropy of attention
distributions changing along steps for each single-query-relation KBC task. (B)(C)(D) The changing
of the proportion of attention concentrated at the top-1,3,5 nodes per step for each task.
0
2
4
6
8
10
Training Time for One Epoch (h)
(A) Time Cost on Sampling Horizons
Max-sampling-per-node = 20
Max-sampling-per-node = 50
Max-sampling-per-node = 100
Max-sampling-per-node = 200
Max-sampling-per-node = 400
0
2
4
6
8
10
Training Time for One Epoch (h)
(B) Time Cost on Attending-to Horizons
Max-atteding-to-per-step = 20
Max-atteding-to-per-step = 50
Max-atteding-to-per-step = 100
Max-atteding-to-per-step = 200
Max-atteding-to-per-step = 400
0
2
4
6
8
10
Training Time for One Epoch (h)
(C) Time Cost on Attending-from Horizons
Max-atteding-from-per-step = 5
Max-atteding-from-per-step = 10
Max-atteding-from-per-step = 20
Max-atteding-from-per-step = 40
0
2
4
6
8
10
Training Time for One Epoch (h)
(D) Time Cost on Searching Horizons
#Steps-in-AGNN = 2
#Steps-in-AGNN = 4
#Steps-in-AGNN = 6
#Steps-in-AGNN = 8
0
2
4
6
8
10
Training Time for One Epoch (h)
(E) Time Cost on Batch Sizes
Batch-size = 50
Batch-size = 100
Batch-size = 200
Batch-size = 300
Figure 6: Analysis of time cost on WN18RR: (A)-(D) measure the one-epoch training time on dif-
ferent horizon settings corresponding to Figure 4(C)-(F); (E) measures on different batch sizes us-
ing horizon setting Max-sampling-per-node=20, Max-attending-to-per-step=20, Max-attending-from-per-
step=20, and #Steps-in-AGNN=8. The charts on FB15K-237 can be found in the appendix.
from nodes per step is useful. That also explains why we call nodes in the attending-from horizon
the core nodes, as they determine where subgraphs can be expanded and how attention will be
propagated to affect the ﬁnal probability distribution on the tail prediction. However, GPUs with
a limited memory do not allow for a too large number of sampled or attended nodes especially for
Max-attending-from-per-step. The detailed explanations can be found in attention strategies in Section
2 where the upper bound is controlled by N1N2 and N3 (Max-attending-from-per-step corresponding
to N1, Max-sampling-per-node to N2, and Max-attending-to-per-step to N3). In N1N2, Section 3.2 sug-
gests that we should sample more by a large N2 but attend less by a small N1. Figure 4(F) suggests
that the propagation steps of AGNN should not go below four.
Attention ﬂow analysis. If the ﬂow-style attention really captures the way we reason about the
world, its process should be conducted in a diverging-converging thinking pattern. Intuitively, ﬁrst,
for the diverging thinking phase, we search and collect ideas as much as we can; then, for the
converging thinking phase, we try to concentrate our thoughts on one point. To check whether the
attention ﬂow has such a pattern, we measure the average entropy of attention distributions changing
along steps and also the proportion of attention concentrated at the top-1,3,5 nodes. As we expect,
attention is more focused at the ﬁnal step and the beginning.
Time cost analysis. The time cost is affected not only by the scale of a dataset but also by the horizon
setting. For each dataset, we list the training time for one epoch corresponding to our standard
hyperparameter settings in the appendix. Note that there is always a trade-off between complexity
and performance. We thus study whether we can reduce time cost a lot at the price of sacriﬁcing a
little performance. We plot the one-epoch training time in Figure 6(A)-(D), using the same settings
as we do in the horizon analysis. We can see that Max-attending-from-per-step and #Steps-in-AGNN
affect the training time signiﬁcantly while Max-sampling-per-node and Max-attending-to-per-step affect
very slightly. Therefore, we can use smaller Max-sampling-per-node and Max-attending-to-per-step in
order to gain a larger batch size, making the computation more efﬁciency as shown in Figure 6(E).
Visualization. To further demonstrate the reasoning capability, we show visualization results of
some pruned subgraphs on NELL995’s test data for 12 separate tasks. We avoid using the training
data in order to show generalization of the learned reasoning capability. We show the visualization
results in Figure 1. See the appendix for detailed analysis and more visualization results.
9


## Page 10


Published as a conference paper at ICLR 2020
Discussion of the limitation. Although DPMPN shows a promising way to harness the scalability
on large-scale graph data, current GPU-based machine learning platforms, such as TensorFlow and
PyTorch, seem not ready to fully leverage sparse tensor computation which acts as building blocks
to support dynamical computation graphs which varies from one input to another. Extra overhead
caused by extensive sparse operations will neutralize the beneﬁts of exploiting sparsity.
5
RELATED WORK
Knowledge graph reasoning. Early work, including TransE (Bordes et al., 2013) and its analogues
(Wang et al., 2014; Lin et al., 2015b; Ji et al., 2015), DistMult (Yang et al., 2015), ConvE (Dettmers
et al., 2018) and ComplEx (Trouillon et al., 2016), focuses on learning embeddings of entities and
relations. Some recent works of this line (Sun et al., 2018; Lacroix et al., 2018) achieve high accu-
racy. Another line aims to learn inference paths (Lao et al., 2011; Guu et al., 2015; Lin et al., 2015a;
Toutanova et al., 2016; Chen et al., 2018; Lin et al., 2018) for knowledge graph reasoning, especially
DeepPath (Xiong et al., 2017), MINERVA (Das et al., 2018), and M-Walk (Shen et al., 2018), which
use RL to learn multi-hop relational paths. However, these approaches, based on policy gradients
or Monte Carlo tree search, often suffer from low sample efﬁciency and sparse rewards, requiring
a large number of rollouts and sophisticated reward function design. Other efforts include learning
soft logical rules (Cohen, 2016; Yang et al., 2017) or compostional programs (Liang et al., 2016).
Relational reasoning in Graph Neural Networks. Relational reasoning is regarded as the key for
combinatorial generalization, taking the form of entity- and relation-centric organization to reason
about the composition structure of the world (Craik, 1952; Lake et al., 2017). A multitude of recent
implementations (Battaglia et al., 2018) encode relational inductive biases into neural networks to
exploit graph-structured representation, including graph convolution networks (GCNs) (Bruna et al.,
2014; Henaff et al., 2015; Duvenaud et al., 2015; Kearnes et al., 2016; Defferrard et al., 2016; Niepert
et al., 2016; Kipf & Welling, 2017; Bronstein et al., 2017) and graph neural networks (Scarselli et al.,
2009; Li et al., 2016; Santoro et al., 2017; Battaglia et al., 2016; Gilmer et al., 2017). Variants of
GNN architectures have been developed. Relation networks (Santoro et al., 2017) use a simple
but effective neural module to model relational reasoning, and its recurrent versions (Santoro et al.,
2018; Palm et al., 2018) do multi-step relational inference for long periods; Interaction networks
(Battaglia et al., 2016) provide a general-purpose learnable physics engine, and two of its variants are
visual interaction networks (Watters et al., 2017) and vertex attention interaction networks (Hoshen,
2017); Message passing neural networks (Gilmer et al., 2017) unify various GCNs and GNNs into
a general message passing formalism by analogy to the one in graphical models.
Attention mechanism on graphs. Neighborhood attention operation can enhance GNNs’ repre-
sentation power (Velickovic et al., 2018; Hoshen, 2017; Wang et al., 2018; Kool, 2018). These
approaches often use multi-head self-attention to focus on speciﬁc interactions with neighbors when
aggregating messages, inspired by (Bahdanau et al., 2015; Lin et al., 2017; Vaswani et al., 2017).
Most graph-based attention mechanisms attend over neighborhood in a single-hop fashion, and
(Hoshen, 2017) claims that the multi-hop architecture does not help to model high-order interac-
tion in experiments. However, a ﬂow-style design of attention in (Xu et al., 2018b) shows a way to
model long-range attention, stringing isolated attention operations by transition matrices.
6
CONCLUSION
We introduce Dynamically Pruned Message Passing Networks (DPMPN) and apply it to large-scale
knowledge graph reasoning tasks. We propose to learn an input-dependent local subgraph which
is progressively and selectively constructed to model a sequential reasoning process in knowledge
graphs. We use graphical attention expression, a ﬂow-style attention mechanism, to guide and prune
the underlying message passing, making it scalable for large-scale graphs and also providing clear
graphical interpretations. We also take the inspiration from the consciousness prior to develop a
two-GNN framework to boost experimental performances.
10


## Page 11


Published as a conference paper at ICLR 2020
REFERENCES
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly
learning to align and translate. CoRR, abs/1409.0473, 2015.
Peter W. Battaglia, Razvan Pascanu, Matthew Lai, Danilo Jimenez Rezende, and Koray
Kavukcuoglu. Interaction networks for learning about objects, relations and physics. In NIPS,
2016.
Peter W. Battaglia, Jessica B. Hamrick, Victor Bapst, Alvaro Sanchez-Gonzalez, Vin´ıcius Flores
Zambaldi, Mateusz Malinowski, Andrea Tacchetti, David Raposo, Adam Santoro, Ryan Faulkner,
aglar G¨ulehre, Francis Song, Andrew J. Ballard, Justin Gilmer, George E. Dahl, Ashish Vaswani,
Kelsey R. Allen, Charles Nash, Victoria Langston, Chris Dyer, Nicolas Heess, Daan Wierstra,
Pushmeet Kohli, Matthew Botvinick, Oriol Vinyals, Yujia Li, and Razvan Pascanu. Relational
inductive biases, deep learning, and graph networks. CoRR, abs/1806.01261, 2018.
Yoshua Bengio. The consciousness prior. CoRR, abs/1709.08568, 2017.
Antoine Bordes, Nicolas Usunier, Alberto Garc´ıa-Dur´an, Jason Weston, and Oksana Yakhnenko.
Translating embeddings for modeling multi-relational data. In NIPS, 2013.
Michael M. Bronstein, Joan Bruna, Yann LeCun, Arthur Szlam, and Pierre Vandergheynst. Geomet-
ric deep learning: Going beyond euclidean data. IEEE Signal Processing Magazine, 34:18–42,
2017.
Joan Bruna, Wojciech Zaremba, Arthur Szlam, and Yann LeCun. Spectral networks and locally
connected networks on graphs. CoRR, abs/1312.6203, 2014.
Wenhu Chen, Wenhan Xiong, Xifeng Yan, and William Yang Wang. Variational knowledge graph
reasoning. In NAACL-HLT, 2018.
William W. Cohen. Tensorlog: A differentiable deductive database. CoRR, abs/1605.06523, 2016.
Kenneth H. Craik. The nature of explanation. 1952.
Rajarshi Das, Shehzaad Dhuliawala, Manzil Zaheer, Luke Vilnis, Ishan Durugkar, Akshay Krish-
namurthy, Alexander J. Smola, and Andrew McCallum. Go for a walk and arrive at the answer:
Reasoning over paths in knowledge bases using reinforcement learning. CoRR, abs/1711.05851,
2018.
Micha¨el Defferrard, Xavier Bresson, and Pierre Vandergheynst. Convolutional neural networks on
graphs with fast localized spectral ﬁltering. In NIPS, 2016.
Tim Dettmers, Pasquale Minervini, Pontus Stenetorp, and Sebastian Riedel.
Convolutional 2d
knowledge graph embeddings. In AAAI, 2018.
David K. Duvenaud, Dougal Maclaurin, Jorge Aguilera-Iparraguirre, Rafael G´omez-Bombarelli,
Timothy Hirzel, Al´an Aspuru-Guzik, and Ryan P. Adams. Convolutional networks on graphs for
learning molecular ﬁngerprints. In NIPS, 2015.
Justin Gilmer, Samuel S. Schoenholz, Patrick F. Riley, Oriol Vinyals, and George E. Dahl. Neural
message passing for quantum chemistry. In ICML, 2017.
Kelvin Guu, John Miller, and Percy S. Liang. Traversing knowledge graphs in vector space. In
EMNLP, 2015.
Mikael Henaff, Joan Bruna, and Yann LeCun. Deep convolutional networks on graph-structured
data. CoRR, abs/1506.05163, 2015.
Yedid Hoshen. Vain: Attentional multi-agent predictive modeling. In NIPS, 2017.
Guoliang Ji, Shizhu He, Liheng Xu, Kang Liu, and Jian Zhao. Knowledge graph embedding via
dynamic mapping matrix. In ACL, 2015.
11


## Page 12


Published as a conference paper at ICLR 2020
Steven M. Kearnes, Kevin McCloskey, Marc Berndl, Vijay S. Pande, and Patrick Riley. Molecular
graph convolutions: moving beyond ﬁngerprints. Journal of computer-aided molecular design,
30 8:595–608, 2016.
Thomas N. Kipf and Max Welling. Semi-supervised classiﬁcation with graph convolutional net-
works. CoRR, abs/1609.02907, 2017.
Wouter Kool. Attention solves your tsp , approximately. 2018.
Timoth´ee Lacroix, Nicolas Usunier, and Guillaume Obozinski. Canonical tensor decomposition for
knowledge base completion. In ICML, 2018.
Brenden M. Lake, Tomer D. Ullman, Joshua B. Tenenbaum, and Samuel J Gershman. Building
machines that learn and think like people. The Behavioral and brain sciences, 40:e253, 2017.
Ni Lao, Tom Michael Mitchell, and William W. Cohen. Random walk inference and learning in a
large scale knowledge base. In EMNLP, 2011.
Yujia Li, Daniel Tarlow, Marc Brockschmidt, and Richard S. Zemel. Gated graph sequence neural
networks. CoRR, abs/1511.05493, 2016.
Chen Liang, Jonathan Berant, Quoc V. Le, Kenneth D. Forbus, and Ni Lao. Neural symbolic ma-
chines: Learning semantic parsers on freebase with weak supervision. In ACL, 2016.
Xi Victoria Lin, Richard Socher, and Caiming Xiong. Multi-hop knowledge graph reasoning with
reward shaping. In EMNLP, 2018.
Yankai Lin, Zhiyuan Liu, and Maosong Sun. Modeling relation paths for representation learning of
knowledge bases. In EMNLP, 2015a.
Yankai Lin, Zhiyuan Liu, Maosong Sun, Yang Liu, and Xuan Zhu. Learning entity and relation
embeddings for knowledge graph completion. In AAAI, 2015b.
Zhouhan Lin, Minwei Feng, C´ıcero Nogueira dos Santos, Mo Yu, Bing Xiang, Bowen Zhou, and
Yoshua Bengio. A structured self-attentive sentence embedding. CoRR, abs/1703.03130, 2017.
Farzaneh Mahdisoltani, Joanna Asia Biega, and Fabian M. Suchanek. Yago3: A knowledge base
from multilingual wikipedias. In CIDR, 2014.
Dai Quoc Nguyen, Tu Dinh Nguyen, Dat Quoc Nguyen, and Dinh Q. Phung. A novel embedding
model for knowledge base completion based on convolutional neural network. In NAACL-HLT,
2018.
Maximilian Nickel, Lorenzo Rosasco, and Tomaso A. Poggio. Holographic embeddings of knowl-
edge graphs. In AAAI, 2016.
Mathias Niepert, Mohammed Hassan Ahmed, and Konstantin Kutzkov. Learning convolutional
neural networks for graphs. In ICML, 2016.
Rasmus Berg Palm, Ulrich Paquet, and Ole Winther. Recurrent relational networks. In NeurIPS,
2018.
Adam Santoro, David Raposo, David G. T. Barrett, Mateusz Malinowski, Razvan Pascanu, Peter W.
Battaglia, and Timothy P. Lillicrap. A simple neural network module for relational reasoning. In
NIPS, 2017.
Adam Santoro, Ryan Faulkner, David Raposo, Jack W. Rae, Mike Chrzanowski, Th´eophane Weber,
Daan Wierstra, Oriol Vinyals, Razvan Pascanu, and Timothy P. Lillicrap. Relational recurrent
neural networks. In NeurIPS, 2018.
Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbuchner, and Gabriele Monfardini.
The graph neural network model. IEEE Transactions on Neural Networks, 20:61–80, 2009.
Yelong Shen, Jianshu Chen, Pu Huang, Yuqing Guo, and Jianfeng Gao. M-walk: Learning to walk
over graphs using monte carlo tree search. In NeurIPS, 2018.
12


## Page 13


Published as a conference paper at ICLR 2020
Zhiqing Sun, Zhi-Hong Deng, Jian-Yun Nie, and Jian Tang. Rotate: Knowledge graph embedding
by relational rotation in complex space. CoRR, abs/1902.10197, 2018.
Kristina Toutanova and Danqi Chen. Observed versus latent features for knowledge base and text
inference. In Proceedings of the 3rd Workshop on Continuous Vector Space Models and their
Compositionality, 2015.
Kristina Toutanova, Victoria Lin, Wen tau Yih, Hoifung Poon, and Chris Quirk. Compositional
learning of embeddings for relation paths in knowledge base and text. In ACL, 2016.
Th´eo Trouillon, Johannes Welbl, Sebastian Riedel, ´Eric Gaussier, and Guillaume Bouchard. Com-
plex embeddings for simple link prediction. In ICML, 2016.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez,
Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In NIPS, 2017.
Petar Velickovic, Guillem Cucurull, Arantxa Casanova, Alejandro Romero, Pietro Li´o, and Yoshua
Bengio. Graph attention networks. CoRR, abs/1710.10903, 2018.
William Wang. Knowledge graph reasoning: Recent advances, 2018.
Xiaolong Wang, Ross B. Girshick, Abhinav Gupta, and Kaiming He. Non-local neural networks.
2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 7794–7803, 2018.
Zhen Wang, Jianwen Zhang, Jianlin Feng, and Zheng Chen. Knowledge graph embedding by trans-
lating on hyperplanes. In AAAI, 2014.
Nicholas Watters, Daniel Zoran, Th´eophane Weber, Peter W. Battaglia, Razvan Pascanu, and Andrea
Tacchetti. Visual interaction networks: Learning a physics simulator from video. In NIPS, 2017.
Wenhan Xiong, Thien Hoang, and William Yang Wang. Deeppath: A reinforcement learning method
for knowledge graph reasoning. In EMNLP, 2017.
Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka.
How powerful are graph neural
networks? ArXiv, abs/1810.00826, 2018a.
Xiaoran Xu, Songpeng Zu, Chengliang Gao, Yuan Zhang, and Wei Feng. Modeling attention ﬂow
on graphs. CoRR, abs/1811.00497, 2018b.
Bishan Yang, Wen tau Yih, Xiaodong He, Jianfeng Gao, and Li Deng. Embedding entities and
relations for learning and inference in knowledge bases. CoRR, abs/1412.6575, 2015.
Fan Yang, Zhilin Yang, and William W. Cohen. Differentiable learning of logical rules for knowl-
edge base reasoning. In NIPS, 2017.
13


## Page 14


Published as a conference paper at ICLR 2020
Appendix
7
PROOF
Proposition. Given a graph G (undirected or directed in both directions), we assume the probability
of the degree of an arbitrary node being less than or equal to d is larger than p, i.e., P(deg(v) ≤
d) > p, ∀v ∈V . Considering a sequence of consecutively expanding subgraphs (G0, G1, . . . , GT ),
starting with G0 = {v}, for all t ≥1, we can ensure
P
 |VGt| ≤d(d −1)t −2
d −2

> p
d(d−1)t−1−2
d−2
.
(6)
Proof. We consider the extreme case of greedy consecutive expansion, where Gt = Gt−1 ∪∆Gt =
Gt−1 ∪∂Gt−1, since if this case satisﬁes the inequality, any case of consecutive expansion can also
satisfy it. By deﬁnition, all the subgraphs Gt are a connected graph. Here, we use ∆V t to denote
V∆Gt for short. In the extreme case, we can ensure that the newly added nodes ∆V t at step t only
belong to the neighborhood of the last added nodes ∆V t−1. Since for t ≥2 each node in ∆V t−1
already has at least one edge within Gt−1 due to the deﬁnition of connected graphs, we can have
P
 |∆V t| ≤|∆V t−1|(d −1)

> p|∆V t−1|.
(7)
For t = 1, we have P(|∆V 1| ≤d) > p and thus
P
 |VG1| ≤1 + d

> p.
(8)
For t ≥2, based on |VGt| = 1 + |∆V 1| + . . . + |∆V t|, we obtain
P
 |VGt| ≤1 + d + d(d −1) + . . . + d(d −1)t−1
> p1+d+d(d−1)+...+d(d−1)t−2,
(9)
which is
P
 |VGt| ≤d(d −1)t −2
d −2

> p
d(d−1)t−1−2
d−2
.
(10)
We can ﬁnd that t = 1 also satisﬁes this inequality.
14


## Page 15


Published as a conference paper at ICLR 2020
8
HYPERPARAMETER SETTINGS
Table 3: Our standard hyperparameter settings we use for each dataset plus their one-epoch training
time. For experimental analysis, we only adjust one hyperparameter and keep the remaining ﬁxed
as the standard setting. For NELL995, the one-epoch training time means the average time cost of
the 12 single-query-relation tasks.
Hyperparameter
FB15K-237
FB15K
WN18RR
WN18
YAGO3-10
NELL995
batch size
80
80
100
100
100
10
n dims att
50
50
50
50
50
200
n dims
100
100
100
100
100
200
max sampling per step (in IGNN)
10000
10000
10000
10000
10000
10000
max attending from per step
20
20
20
20
20
100
max sampling per node (in AGNN)
200
200
200
200
200
1000
max attending to per step
200
200
200
200
200
1000
n steps in IGNN
2
1
2
1
1
1
n steps in AGNN
6
6
8
8
6
5
learning rate
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
grad clipnorm
1
1
1
1
1
1
n epochs
1
1
1
1
1
3
One-epoch training time (h)
25.7
63.7
4.3
8.5
185.0
0.12
The hyperparameters can be categorized into three groups:
• Normal hyperparameters, including batch size, n dims att, n dims, learning rate, grad clipnorm, and
n epochs. We set smaller dimensions, n dims att, for computation in the attention module, as it
uses more edges than the message passing uses in AGNN, and also intuitively, it does not need to
propagate high-dimensional messages but only compute scalar scores over a sampled neighbor-
hood, in concert with the idea in the key-value mechanism (Bengio, 2017). We set n epochs = 1
in most cases, indicating that our model can be trained well by one epoch only due to its fast
convergence.
• The
hyperparameters
in
charge
of
the
sampling-attending
horizon,
including
max sampling per step that controls the maximum number to sample edges per step in IGNN, and
max sampling per node, max attending from per step and max attending to per step that control the
maximum number to sample neighbors of each selected node per step per input, the maximum
number of selected nodes for attending-from per step per input, and the maximum number of
selected nodes in a sampled neighborhood for attending-to per step per input in AGNN.
• The hyperparameters in charge of the searching horizon, including n steps in IGNN representing
the number of propagation steps to run standard message passing in IGNN, and n steps in AGNN
representing the number of propagation steps to run pruned message passing in AGNN.
Note that we tune these hyperparameters according to not only their performances but also the
computation resources available to us. In some cases, to deal with a very large knowledge graph with
limited resources, we need to make a trade-off between efﬁciency and effectiveness. For example,
each of NELL995’s single-query-relation tasks has a small training set, though still with a large
graph, so we can reduce the batch size in favor of affording larger dimensions and a larger sampling-
attending horizon without any concern for waiting too long to ﬁnish one epoch.
15


## Page 16


Published as a conference paper at ICLR 2020
9
MORE EXPERIMENTAL RESULTS
Table 4: Comparison results on the FB15K and WN18 datasets. Results of [♠] are taken from
(Nickel et al., 2016), [♣] from (Dettmers et al., 2018), [♦] from (Sun et al., 2018), [♥] from (Yang
et al., 2017), and [✠] from (Lacroix et al., 2018). Our results take the form of ”mean (std)”.
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
ComplEx-N3 [✠]
-
-
91
86
-
-
96
95
NeuralLP [♥]
-
-
83.7
76
-
-
94.5
94
DPMPN
72.6 (.4)
78.4 (.4)
83.4 (.5)
76.4 (.4)
91.6 (.8)
93.6 (.4)
94.9 (.4)
92.8 (.6)
Table 5: Comparison results on the YAGO3-10 dataset. Results of [♠] are taken from (Dettmers
et al., 2018), [♣] from (Lacroix et al., 2018), and [✠] from (Lacroix et al., 2018).
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
ComplEx-N3 [✠]
-
-
71
58
DPMPN
48.4
59.5
67.9
55.3
Table 6: Comparison results of MAP scores (%) on NELL995’s single-query-relation KBC tasks.
We take our baselines’ results from (Shen et al., 2018). No reports found on the last two in the paper.
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
16


## Page 17


Published as a conference paper at ICLR 2020
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
(A) Convergence Analysis (eval on test)
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
(B) IGNN Component Analysis
W/o IGNN
With IGNN
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
Max-sampling-per-node = 20
Max-sampling-per-node = 50
Max-sampling-per-node = 100
Max-sampling-per-node = 200
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
Max-atteding-to-per-step = 20
Max-atteding-to-per-step = 50
Max-atteding-to-per-step = 100
Max-atteding-to-per-step = 200
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
Max-atteding-from-per-step = 5
Max-atteding-from-per-step = 10
Max-atteding-from-per-step = 20
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
#Steps-in-AGNN = 2
#Steps-in-AGNN = 4
#Steps-in-AGNN = 6
Figure 7: Experimental analysis on FB15K-237. (A) Convergence analysis: we pick six model
snapshots at time points of 0.3, 0.5, 0.7, 1, 2, and 3 epochs during training and evaluate them on test;
(B) IGNN component analysis: w/o IGNN uses zero step to run message passing, while with IGNN
uses two steps; (C)-(F) Sampling, attending-to, attending-from and searching horizon analysis.
0
5
10
15
20
25
30
35
Training Time for One Epoch (h)
(A) Time Cost on Sampling Horizons
Max-sampling-per-node = 20
Max-sampling-per-node = 50
Max-sampling-per-node = 100
Max-sampling-per-node = 200
0
5
10
15
20
25
30
35
Training Time for One Epoch (h)
(B) Time Cost on Attending-to Horizons
Max-atteding-to-per-step = 20
Max-atteding-to-per-step = 50
Max-atteding-to-per-step = 100
Max-atteding-to-per-step = 200
0
5
10
15
20
25
30
35
Training Time for One Epoch (h)
(C) Time Cost on Attending-from Horizons
Max-atteding-from-per-step = 5
Max-atteding-from-per-step = 10
Max-atteding-from-per-step = 20
0
5
10
15
20
25
30
35
Training Time for One Epoch (h)
(D) Time Cost on Searching Horizons
#Steps-in-AGNN = 2
#Steps-in-AGNN = 4
#Steps-in-AGNN = 6
0
5
10
15
20
25
30
35
Training Time for One Epoch (h)
(E) Time Cost on Batch Sizes
Batch-size = 50
Batch-size = 100
Batch-size = 200
Batch-size = 300
Figure 8: Analysis of time cost on FB15K-237: (A)-(D) measure the one-epoch training time on dif-
ferent horizon settings corresponding to Figure 7(C)-(F); (E) measures on different batch sizes using
horizon setting Max-sampled-edges-per-node=20, Max-seen-nodes-per-step=20, Max-attended-nodes-per-
step=20, and #Steps-of-AGNN=6.
10
MORE VISUALIZATION RESUTLS
10.1
CASE STUDY ON THE ATHLETEPLAYSFORTEAM TASK
In
the
case
shown
in
Figure
9,
the
query
is
(concept personnorthamerica michael turner,
concept:athleteplays-forteam, ?) and a true answer is concept sportsteam falcons. From Figure 9, we
can see our model learns that (concept personnorthamerica michael turner, concept:athletehomestadium,
concept stadiumoreventvenue georgia dome)
and
(concept stadiumoreventvenue georgia dome,
con-
cept:teamhomestadium inv, concept sportsteam falcons) are two important facts to support the an-
swer of concept sportsteam falcons.
Besides, other facts, such as (concept athlete joey harrington,
concept:athletehomestadium,
concept stadiumoreventvenue georgia dome)
and
(concept athlete-
joey harrington, concept:athleteplaysforteam, concept sportsteam falcons), provide a vivid example
that a person or an athlete with concept stadiumoreventvenue georgia dome as his or her home
stadium might play for the team concept sportsteam falcons.
We have such examples more than
one, like concept athlete roddy white’s and concept athlete quarterback matt ryan’s.
The entity con-
17


## Page 18


Published as a conference paper at ICLR 2020
cept sportsleague nﬂcannot help us differentiate the true answer from other NFL teams, but it can
at least exclude those non-NFL teams. In a word, our subgraph-structured representation can well
capture the relational and compositional reasoning pattern.
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
Figure 9: AthletePlaysForTeam. The head is concept personnorthamerica michael turner, the query
relation is concept:athleteplaysforteam, and the tail is concept sportsteam falcons. The left is a full sub-
graph derived with max attending from per step=20, and the right is a further pruned subgraph from
the left based on attention. The big yellow node represents the head, and the big red node represents
the tail. Color on the rest indicates attention scores over a T-step reasoning process, where grey
means less attention, yellow means more attention gained during early steps, and red means gaining
more attention when getting closer to the ﬁnal step.
For the AthletePlaysForTeam task
Query :
( concept personnorthamerica michael turner ,
concept : athleteplaysforteam ,
concept sportsteam falcons )
Selected key edges :
concept personnorthamerica michael turner ,
concept : agentbelongstoorganization ,
concept sportsleague nfl
concept personnorthamerica michael turner ,
concept : athletehomestadium ,
concept stadiumoreventvenue georgia dome
concept sportsleague nfl ,
concept : agentcompeteswithagent ,
concept sportsleague nfl
concept sportsleague nfl ,
concept : agentcompeteswithagent inv ,
concept sportsleague nfl
concept sportsleague nfl ,
concept : teamplaysinleague inv ,
concept sportsteam sd chargers
concept sportsleague nfl ,
concept : leaguestadiums ,
concept stadiumoreventvenue georgia dome
concept sportsleague nfl ,
concept : teamplaysinleague inv ,
concept sportsteam falcons
concept sportsleague nfl ,
concept : agentbelongstoorganization inv ,
concept personnorthamerica michael turner
concept stadiumoreventvenue georgia dome ,
concept : leaguestadiums inv ,
concept sportsleague nfl
concept stadiumoreventvenue georgia dome ,
concept : teamhomestadium inv ,
concept sportsteam falcons
concept stadiumoreventvenue georgia dome ,
concept : athletehomestadium inv ,
concept athlete joey harrington
concept stadiumoreventvenue georgia dome ,
concept : athletehomestadium inv ,
concept athlete roddy white
concept stadiumoreventvenue georgia dome ,
concept : athletehomestadium inv ,
concept coach deangelo hall
concept stadiumoreventvenue georgia dome ,
concept : athletehomestadium inv ,
concept personnorthamerica michael turner
concept sportsleague nfl ,
concept : subpartoforganization inv ,
concept sportsteam oakland raiders
concept sportsteam sd chargers ,
concept : teamplaysinleague ,
concept sportsleague nfl
concept sportsteam sd chargers ,
concept : teamplaysagainstteam ,
concept sportsteam falcons
concept sportsteam sd chargers ,
concept : teamplaysagainstteam inv ,
concept sportsteam falcons
concept sportsteam sd chargers ,
concept : teamplaysagainstteam ,
concept sportsteam oakland raiders
concept sportsteam sd chargers ,
concept : teamplaysagainstteam inv ,
concept sportsteam oakland raiders
concept sportsteam falcons ,
concept : teamplaysinleague ,
concept sportsleague nfl
concept sportsteam falcons ,
concept : teamplaysagainstteam ,
concept sportsteam sd chargers
concept sportsteam falcons ,
concept : teamplaysagainstteam inv ,
concept sportsteam sd chargers
concept sportsteam falcons ,
concept : teamhomestadium ,
concept stadiumoreventvenue georgia dome
concept sportsteam falcons ,
concept : teamplaysagainstteam ,
concept sportsteam oakland raiders
concept sportsteam falcons ,
concept : teamplaysagainstteam inv ,
concept sportsteam oakland raiders
concept sportsteam falcons ,
concept : athleteledsportsteam inv ,
concept athlete joey harrington
concept athlete joey harrington ,
concept : athletehomestadium ,
concept stadiumoreventvenue georgia dome
concept athlete joey harrington ,
concept : athleteledsportsteam ,
concept sportsteam falcons
concept athlete joey harrington ,
concept : athleteplaysforteam ,
concept sportsteam falcons
concept athlete roddy white ,
concept : athletehomestadium ,
concept stadiumoreventvenue georgia dome
concept athlete roddy white ,
concept : athleteplaysforteam ,
concept sportsteam falcons
concept coach deangelo hall ,
concept : athletehomestadium ,
concept stadiumoreventvenue georgia dome
18


## Page 19


Published as a conference paper at ICLR 2020
concept coach deangelo hall ,
concept : athleteplaysforteam ,
concept sportsteam oakland raiders
concept sportsleague nfl ,
concept : teamplaysinleague inv ,
concept sportsteam new york giants
concept sportsteam sd chargers ,
concept : teamplaysagainstteam inv ,
concept sportsteam new york giants
concept sportsteam falcons ,
concept : teamplaysagainstteam ,
concept sportsteam new york giants
concept sportsteam falcons ,
concept : teamplaysagainstteam inv ,
concept sportsteam new york giants
concept sportsteam oakland raiders ,
concept : teamplaysagainstteam inv ,
concept sportsteam new york giants
concept sportsteam oakland raiders ,
concept : teamplaysagainstteam ,
concept sportsteam sd chargers
concept sportsteam oakland raiders ,
concept : teamplaysagainstteam inv ,
concept sportsteam sd chargers
concept sportsteam oakland raiders ,
concept : teamplaysagainstteam ,
concept sportsteam falcons
concept sportsteam oakland raiders ,
concept : teamplaysagainstteam inv ,
concept sportsteam falcons
concept sportsteam oakland raiders ,
concept : agentcompeteswithagent ,
concept sportsteam oakland raiders
concept sportsteam oakland raiders ,
concept : agentcompeteswithagent inv ,
concept sportsteam oakland raiders
concept sportsteam new york giants ,
concept : teamplaysagainstteam ,
concept sportsteam sd chargers
concept sportsteam new york giants ,
concept : teamplaysagainstteam ,
concept sportsteam falcons
concept sportsteam new york giants ,
concept : teamplaysagainstteam inv ,
concept sportsteam falcons
concept sportsteam new york giants ,
concept : teamplaysagainstteam ,
concept sportsteam oakland raiders
10.2
MORE RESULTS
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
Figure 10: AthletePlaysInLeague. The head is concept personnorthamerica matt treanor, the query
relation is concept:athleteplaysinleague, and the tail is concept sportsleague mlb. The left is a full sub-
graph derived with max attending from per step=20, and the right is a further pruned subgraph from
the left based on attention. The big yellow node represents the head, and the big red node represents
the tail. Color on the rest indicates attention scores over a T-step reasoning process, where grey
means less attention, yellow means more attention gained during early steps, and red means gaining
more attention when getting closer to the ﬁnal step.
For the AthletePlaysInLeague task
Query :
( concept personnorthamerica matt treanor ,
concept : athleteplaysinleague ,
concept sportsleague mlb )
Selected key edges :
concept personnorthamerica matt treanor ,
concept : athleteflyouttosportsteamposition ,
concept sportsteamposition center
concept personnorthamerica matt treanor ,
concept : athleteplayssport ,
concept sport baseball
concept sportsteamposition center ,
concept : a t h l e t e f l y o u t t o s p o r t s t e a m p o s i t i o n i n v ,
concept personus orlando hudson
concept sportsteamposition center ,
concept : a t h l e t e f l y o u t t o s p o r t s t e a m p o s i t i o n i n v ,
concept athlete ben hendrickson
concept sportsteamposition center ,
concept : a t h l e t e f l y o u t t o s p o r t s t e a m p o s i t i o n i n v ,
concept coach j j
hardy
concept sportsteamposition center ,
concept : a t h l e t e f l y o u t t o s p o r t s t e a m p o s i t i o n i n v ,
concept athlete hunter pence
concept sport baseball ,
concept : athleteplayssport inv ,
concept personus orlando hudson
concept sport baseball ,
concept : athleteplayssport inv ,
concept athlete ben hendrickson
concept sport baseball ,
concept : athleteplayssport inv ,
concept coach j j
hardy
concept sport baseball ,
concept : athleteplayssport inv ,
concept athlete hunter pence
concept personus orlando hudson ,
concept : athleteplaysinleague ,
concept sportsleague mlb
concept personus orlando hudson ,
concept : athleteplayssport ,
concept sport baseball
concept athlete ben hendrickson ,
concept : coachesinleague ,
concept sportsleague mlb
concept athlete ben hendrickson ,
concept : athleteplayssport ,
concept sport baseball
19


## Page 20


Published as a conference paper at ICLR 2020
concept coach j j
hardy ,
concept : coachesinleague ,
concept sportsleague mlb
concept coach j j
hardy ,
concept : athleteplaysinleague ,
concept sportsleague mlb
concept coach j j
hardy ,
concept : athleteplayssport ,
concept sport baseball
concept athlete hunter pence ,
concept : athleteplaysinleague ,
concept sportsleague mlb
concept athlete hunter pence ,
concept : athleteplayssport ,
concept sport baseball
concept sportsleague mlb ,
concept : coachesinleague inv ,
concept athlete ben hendrickson
concept sportsleague mlb ,
concept : coachesinleague inv ,
concept coach j j
hardy
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
Figure 11: AthleteHomeStadium. The head is concept athlete eli manning, the query relation is
concept:athletehomestadium, and the tail is concept stadiumoreventvenue giants stadium. The left is a full
subgraph derived with max attending from per step=20, and the right is a further pruned subgraph
from the left based on attention. The big yellow node represents the head, and the big red node
represents the tail. Color on the rest indicates attention scores over a T-step reasoning process,
where grey means less attention, yellow means more attention gained during early steps, and red
means gaining more attention when getting closer to the ﬁnal step.
For the AthleteHomeStadium task
Query :
( concept athlete eli manning ,
concept : athletehomestadium ,
concept stadiumoreventvenue giants stadium )
Selected key edges :
concept athlete eli manning ,
concept : personbelongstoorganization ,
concept sportsteam new york giants
concept athlete eli manning ,
concept : athleteplaysforteam ,
concept sportsteam new york giants
concept athlete eli manning ,
concept : athleteledsportsteam ,
concept sportsteam new york giants
concept athlete eli manning ,
concept : athleteplaysinleague ,
concept sportsleague nfl
concept athlete eli manning ,
concept : fatherofperson inv ,
concept male archie manning
concept sportsteam new york giants ,
concept : teamplaysinleague ,
concept sportsleague nfl
concept sportsteam new york giants ,
concept : teamhomestadium ,
concept stadiumoreventvenue giants stadium
concept sportsteam new york giants ,
concept : personbelongstoorganization inv ,
concept athlete eli manning
concept sportsteam new york giants ,
concept : athleteplaysforteam inv ,
concept athlete eli manning
concept sportsteam new york giants ,
concept : athleteledsportsteam inv ,
concept athlete eli manning
concept sportsleague nfl ,
concept : teamplaysinleague inv ,
concept sportsteam new york giants
concept sportsleague nfl ,
concept : agentcompeteswithagent ,
concept sportsleague nfl
concept sportsleague nfl ,
concept : agentcompeteswithagent inv ,
concept sportsleague nfl
concept sportsleague nfl ,
concept : leaguestadiums ,
concept stadiumoreventvenue giants stadium
concept sportsleague nfl ,
concept : athleteplaysinleague inv ,
concept athlete eli manning
concept male archie manning ,
concept : fatherofperson ,
concept athlete eli manning
concept sportsleague nfl ,
concept : leaguestadiums ,
concept stadiumoreventvenue paul brown stadium
concept stadiumoreventvenue giants stadium ,
concept : teamhomestadium inv ,
concept sportsteam new york giants
concept stadiumoreventvenue giants stadium ,
concept : leaguestadiums inv ,
concept sportsleague nfl
concept stadiumoreventvenue giants stadium ,
concept : proxyfor inv ,
c o n c e p t c i t y e a s t r u t h e r f o r d
c onc ept city east rutherford ,
concept : proxyfor ,
concept stadiumoreventvenue giants stadium
concept stadiumoreventvenue paul brown stadium ,
concept : leaguestadiums inv ,
concept sportsleague nfl
For the AthletePlaysSport task
20


## Page 21


Published as a conference paper at ICLR 2020
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
Figure 12: AthletePlaysSport. The head is concept athlete vernon wells, the query relation is con-
cept:athleteplayssport, and the tail is concept sport baseball. The left is a full subgraph derived with
max attending from per step=20, and the right is a further pruned subgraph from the left based on at-
tention. The big yellow node represents the head, and the big red node represents the tail. Color on
the rest indicates attention scores over a T-step reasoning process, where grey means less attention,
yellow means more attention gained during early steps, and red means gaining more attention when
getting closer to the ﬁnal step.
Query :
( concept athlete vernon wells ,
concept : athleteplayssport ,
concept sport baseball )
Selected key edges :
concept athlete vernon wells ,
concept : athleteplaysinleague ,
concept sportsleague mlb
concept athlete vernon wells ,
concept : coachwontrophy ,
concept awardtrophytournament world series
concept athlete vernon wells ,
concept : agentcollaborateswithagent inv ,
concept sportsteam blue jays
concept athlete vernon wells ,
concept : personbelongstoorganization ,
concept sportsteam blue jays
concept athlete vernon wells ,
concept : athleteplaysforteam ,
concept sportsteam blue jays
concept athlete vernon wells ,
concept : athleteledsportsteam ,
concept sportsteam blue jays
concept sportsleague mlb ,
concept : teamplaysinleague inv ,
concept sportsteam dodgers
concept sportsleague mlb ,
concept : teamplaysinleague inv ,
concept sportsteam yankees
concept sportsleague mlb ,
concept : teamplaysinleague inv ,
concept sportsteam pittsburgh pirates
concept awardtrophytournament world series ,
concept : teamwontrophy inv ,
concept sportsteam dodgers
concept awardtrophytournament world series ,
concept : teamwontrophy inv ,
concept sportsteam yankees
concept awardtrophytournament world series ,
concept : awardtrophytournamentisthechampionshipgameofthenationalsport ,
concept sport baseball
concept awardtrophytournament world series ,
concept : teamwontrophy inv ,
concept sportsteam pittsburgh pirates
concept sportsteam blue jays ,
concept : teamplaysinleague ,
concept sportsleague mlb
concept sportsteam blue jays ,
concept : teamplaysagainstteam ,
concept sportsteam yankees
concept sportsteam blue jays ,
concept : teamplayssport ,
concept sport baseball
concept sportsteam dodgers ,
concept : teamplaysagainstteam ,
concept sportsteam yankees
concept sportsteam dodgers ,
concept : teamplaysagainstteam inv ,
concept sportsteam yankees
concept sportsteam dodgers ,
concept : teamwontrophy ,
concept awardtrophytournament world series
concept sportsteam dodgers ,
concept : teamplayssport ,
concept sport baseball
concept sportsteam yankees ,
concept : teamplaysagainstteam ,
concept sportsteam dodgers
concept sportsteam yankees ,
concept : teamplaysagainstteam inv ,
concept sportsteam dodgers
concept sportsteam yankees ,
concept : teamwontrophy ,
concept awardtrophytournament world series
concept sportsteam yankees ,
concept : teamplayssport ,
concept sport baseball
concept sportsteam yankees ,
concept : teamplaysagainstteam ,
concept sportsteam pittsburgh pirates
concept sportsteam yankees ,
concept : teamplaysagainstteam inv ,
concept sportsteam pittsburgh pirates
concept sport baseball ,
concept : teamplayssport inv ,
concept sportsteam dodgers
concept sport baseball ,
concept : teamplayssport inv ,
concept sportsteam yankees
concept sport baseball ,
concept : awardtrophytournamentisthechampionshipgameofthenationalsport inv ,
concept awardtrophytournament world series
concept sport baseball ,
concept : teamplayssport inv ,
concept sportsteam pittsburgh pirates
concept sportsteam pittsburgh pirates ,
concept : teamplaysagainstteam ,
concept sportsteam yankees
concept sportsteam pittsburgh pirates ,
concept : teamplaysagainstteam inv ,
concept sportsteam yankees
21


## Page 22


Published as a conference paper at ICLR 2020
concept sportsteam pittsburgh pirates ,
concept : teamwontrophy ,
concept awardtrophytournament world series
concept sportsteam pittsburgh pirates ,
concept : teamplayssport ,
concept sport baseball
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
Figure 13: TeamPlaysSport. The head is concept sportsteam red wings, the query relation is con-
cept:teamplayssport, and the tail is concept sport hockey.
The left is a full subgraph derived with
max attending from per step=20, and the right is a further pruned subgraph from the left based on
attention. The big yellow node represents the head, and the big red node represents the tail. Color
on the rest indicates attention scores over a T-step reasoning process, where grey means less atten-
tion, yellow means more attention gained during early steps, and red means gaining more attention
when getting closer to the ﬁnal step.
For the TeamPlaysSport task
Query :
( concept sportsteam red wings ,
concept : teamplayssport ,
concept sport hockey )
Selected key edges :
concept sportsteam red wings ,
concept : teamplaysagainstteam ,
concept sportsteam montreal canadiens
concept sportsteam red wings ,
concept : teamplaysagainstteam inv ,
concept sportsteam montreal canadiens
concept sportsteam red wings ,
concept : teamplaysagainstteam ,
concept sportsteam blue jackets
concept sportsteam red wings ,
concept : teamplaysagainstteam inv ,
concept sportsteam blue jackets
concept sportsteam red wings ,
concept : worksfor inv ,
concept athlete lidstrom
concept sportsteam red wings ,
concept : organizationhiredperson ,
concept athlete lidstrom
concept sportsteam red wings ,
concept : athleteplaysforteam inv ,
concept athlete lidstrom
concept sportsteam red wings ,
concept : athleteledsportsteam inv ,
concept athlete lidstrom
concept sportsteam montreal canadiens ,
concept : teamplaysagainstteam ,
concept sportsteam red wings
concept sportsteam montreal canadiens ,
concept : teamplaysagainstteam inv ,
concept sportsteam red wings
concept sportsteam montreal canadiens ,
concept : teamplaysinleague ,
concept sportsleague nhl
concept sportsteam montreal canadiens ,
concept : teamplaysagainstteam ,
concept sportsteam leafs
concept sportsteam montreal canadiens ,
concept : teamplaysagainstteam inv ,
concept sportsteam leafs
concept sportsteam blue jackets ,
concept : teamplaysagainstteam ,
concept sportsteam red wings
concept sportsteam blue jackets ,
concept : teamplaysagainstteam inv ,
concept sportsteam red wings
concept sportsteam blue jackets ,
concept : teamplaysinleague ,
concept sportsleague nhl
concept athlete lidstrom ,
concept : worksfor ,
concept sportsteam red wings
concept athlete lidstrom ,
concept : organizationhiredperson inv ,
concept sportsteam red wings
concept athlete lidstrom ,
concept : athleteplaysforteam ,
concept sportsteam red wings
concept athlete lidstrom ,
concept : athleteledsportsteam ,
concept sportsteam red wings
concept sportsteam red wings ,
concept : teamplaysinleague ,
concept sportsleague nhl
concept sportsteam red wings ,
concept : teamplaysagainstteam ,
concept sportsteam leafs
concept sportsteam red wings ,
concept : teamplaysagainstteam inv ,
concept sportsteam leafs
concept sportsleague nhl ,
concept : agentcompeteswithagent ,
concept sportsleague nhl
concept sportsleague nhl ,
concept : agentcompeteswithagent inv ,
concept sportsleague nhl
concept sportsleague nhl ,
concept : teamplaysinleague inv ,
concept sportsteam leafs
concept sportsteam leafs ,
concept : teamplaysinleague ,
concept sportsleague nhl
concept sportsteam leafs ,
concept : teamplayssport ,
concept sport hockey
22


## Page 23


Published as a conference paper at ICLR 2020
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
Figure 14: OrganizationHeadQuarteredInCity. The head is concept company disney, the query
relation is concept:organizationheadquarteredincity, and the tail is concept city burbank. The left is a
full subgraph derived with max attending from per step=20, and the right is a further pruned subgraph
from the left based on attention. The big yellow node represents the head, and the big red node
represents the tail. Color on the rest indicates attention scores over a T-step reasoning process,
where grey means less attention, yellow means more attention gained during early steps, and red
means gaining more attention when getting closer to the ﬁnal step.
For the OrganizationHeadQuarteredInCity task
Query :
( concept company disney ,
concept : organizationheadquarteredincity ,
concept city burbank )
Selected key edges :
concept company disney ,
concept : headquarteredin ,
concept city burbank
concept company disney ,
concept : subpartoforganization inv ,
concept website network
concept company disney ,
concept : worksfor inv ,
concept ceo robert iger
concept company disney ,
concept : proxyfor inv ,
concept ceo robert iger
concept company disney ,
concept : personleadsorganization inv ,
concept ceo robert iger
concept company disney ,
concept : ceoof inv ,
concept ceo robert iger
concept company disney ,
concept : personleadsorganization inv ,
concept ceo jeffrey katzenberg
concept company disney ,
concept : organizationhiredperson ,
concept ceo jeffrey katzenberg
concept company disney ,
concept : organizationterminatedperson ,
concept ceo jeffrey katzenberg
concept city burbank ,
concept : headquarteredin inv ,
concept company disney
concept city burbank ,
concept : headquarteredin inv ,
concept biotechcompany the walt disney co
concept website network ,
concept : subpartoforganization ,
concept company disney
concept ceo robert iger ,
concept : worksfor ,
concept company disney
concept ceo robert iger ,
concept : proxyfor ,
concept company disney
concept ceo robert iger ,
concept : personleadsorganization ,
concept company disney
concept ceo robert iger ,
concept : ceoof ,
concept company disney
concept ceo robert iger ,
concept : topmemberoforganization ,
concept biotechcompany the walt disney co
concept ceo robert iger ,
concept : organizationterminatedperson inv ,
concept biotechcompany the walt disney co
concept ceo jeffrey katzenberg ,
concept : personleadsorganization ,
concept company disney
concept ceo jeffrey katzenberg ,
concept : organizationhiredperson inv ,
concept company disney
concept ceo jeffrey katzenberg ,
concept : organizationterminatedperson inv ,
concept company disney
concept ceo jeffrey katzenberg ,
concept : worksfor ,
concept recordlabel dreamworks skg
concept ceo jeffrey katzenberg ,
concept : topmemberoforganization ,
concept recordlabel dreamworks skg
concept ceo jeffrey katzenberg ,
concept : organizationterminatedperson inv ,
concept recordlabel dreamworks skg
concept ceo jeffrey katzenberg ,
concept : ceoof ,
concept recordlabel dreamworks skg
concept biotechcompany the walt disney co
,
concept : headquarteredin ,
concept city burbank
concept biotechcompany the walt disney co
,
concept : organizationheadquarteredincity ,
concept city burbank
concept recordlabel dreamworks skg ,
concept : worksfor inv ,
concept ceo jeffrey katzenberg
concept recordlabel dreamworks skg ,
concept : topmemberoforganization inv ,
concept ceo jeffrey katzenberg
concept recordlabel dreamworks skg ,
concept : organizationterminatedperson ,
concept ceo jeffrey katzenberg
concept recordlabel dreamworks skg ,
concept : ceoof inv ,
concept ceo jeffrey katzenberg
concept city burbank ,
concept : a i r p o r t i n c i t y i n v ,
concept transportation burbank glendale pasadena
concept transportation burbank glendale pasadena ,
concept : a i r p o r t i n c i t y ,
concept city burbank
23


## Page 24


Published as a conference paper at ICLR 2020
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
Figure 15:
WorksFor.
The head is concept scientist balmer,
the query relation is con-
cept:worksfor, and the tail is concept university microsoft. The left is a full subgraph derived with
max attending from per step=20, and the right is a further pruned subgraph from the left based on at-
tention. The big yellow node represents the head, and the big red node represents the tail. Color on
the rest indicates attention scores over a T-step reasoning process, where grey means less attention,
yellow means more attention gained during early steps, and red means gaining more attention when
getting closer to the ﬁnal step.
For the WorksFor task
Query :
( concept scientist balmer ,
concept : worksfor ,
concept university microsoft )
Selected key edges :
concept scientist balmer ,
concept : topmemberoforganization ,
concept company microsoft
concept scientist balmer ,
concept : organizationterminatedperson inv ,
concept university microsoft
concept company microsoft ,
concept : topmemberoforganization inv ,
concept personus steve ballmer
concept company microsoft ,
concept : topmemberoforganization inv ,
concept scientist balmer
concept university microsoft ,
concept : agentcollaborateswithagent ,
concept personus steve ballmer
concept university microsoft ,
concept : personleadsorganization inv ,
concept personus steve ballmer
concept university microsoft ,
concept : personleadsorganization inv ,
concept person bill
concept university microsoft ,
concept : organizationterminatedperson ,
concept scientist balmer
concept university microsoft ,
concept : personleadsorganization inv ,
concept person robbie bach
concept personus steve ballmer ,
concept : topmemberoforganization ,
concept company microsoft
concept personus steve ballmer ,
concept : agentcollaborateswithagent inv ,
concept university microsoft
concept personus steve ballmer ,
concept : personleadsorganization ,
concept university microsoft
concept personus steve ballmer ,
concept : worksfor ,
concept university microsoft
concept personus steve ballmer ,
concept : proxyfor ,
c o n c e p t r e t a i l s t o r e m i c r o s o f t
concept personus steve ballmer ,
concept : subpartof ,
c o n c e p t r e t a i l s t o r e m i c r o s o f t
concept personus steve ballmer ,
concept : agentcontrols ,
c o n c e p t r e t a i l s t o r e m i c r o s o f t
concept person bill ,
concept : personleadsorganization ,
concept university microsoft
concept person bill ,
concept : worksfor ,
concept university microsoft
concept person robbie bach ,
concept : personleadsorganization ,
concept university microsoft
concept person robbie bach ,
concept : worksfor ,
concept university microsoft
c o n c e p t r e t a i l s t o r e m i c r o s o f t ,
concept : proxyfor inv ,
concept personus steve ballmer
c o n c e p t r e t a i l s t o r e m i c r o s o f t ,
concept : subpartof inv ,
concept personus steve ballmer
c o n c e p t r e t a i l s t o r e m i c r o s o f t ,
concept : agentcontrols inv ,
concept personus steve ballmer
For the PersonBornInLocation task
Query :
( concept person mark001 ,
concept : personborninlocation ,
concept county york city )
Selected key edges :
concept person mark001 ,
concept : persongraduatedfromuniversity ,
concept university college
concept person mark001 ,
concept : persongraduatedschool ,
concept university college
concept person mark001 ,
concept : persongraduatedfromuniversity ,
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y
concept person mark001 ,
concept : persongraduatedschool ,
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y
concept person mark001 ,
concept : personbornincity ,
concept city hampshire
24


## Page 25


Published as a conference paper at ICLR 2020
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
Figure 16: PersonBornInLocation. The head is concept person mark001, the query relation is con-
cept:personborninlocation, and the tail is concept county york city. The left is a full subgraph derived
with max attending from per step=20, and the right is a further pruned subgraph from the left based on
attention. The big yellow node represents the head, and the big red node represents the tail. Color on
the rest indicates attention scores over a T-step reasoning process, where grey means less attention,
yellow means more attention gained during early steps, and red means gaining more attention when
getting closer to the ﬁnal step.
concept person mark001 ,
concept : hasspouse ,
concept person diane001
concept person mark001 ,
concept : hasspouse inv ,
concept person diane001
concept university college ,
concept : persongraduatedfromuniversity inv ,
concept person mark001
concept university college ,
concept : persongraduatedschool inv ,
concept person mark001
concept university college ,
concept : persongraduatedfromuniversity inv ,
concept person bill
concept university college ,
concept : persongraduatedschool inv ,
concept person bill
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y ,
concept : persongraduatedfromuniversity inv ,
concept person mark001
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y ,
concept : persongraduatedschool inv ,
concept person mark001
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y ,
concept : persongraduatedfromuniversity inv ,
concept person bill
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y ,
concept : persongraduatedschool inv ,
concept person bill
concept city hampshire ,
concept : personbornincity inv ,
concept person mark001
concept person diane001 ,
concept : persongraduatedfromuniversity ,
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y
concept person diane001 ,
concept : persongraduatedschool ,
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y
concept person diane001 ,
concept : hasspouse ,
concept person mark001
concept person diane001 ,
concept : hasspouse inv ,
concept person mark001
concept person diane001 ,
concept : personborninlocation ,
concept county york city
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y ,
concept : persongraduatedfromuniversity inv ,
concept person diane001
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y ,
concept : persongraduatedschool inv ,
concept person diane001
concept person bill ,
concept : personbornincity ,
concept city york
concept person bill ,
concept : personborninlocation ,
concept city york
concept person bill ,
concept : persongraduatedfromuniversity ,
concept university college
concept person bill ,
concept : persongraduatedschool ,
concept university college
concept person bill ,
concept : persongraduatedfromuniversity ,
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y
concept person bill ,
concept : persongraduatedschool ,
c o n c e p t u n i v e r s i t y s t a t e u n i v e r s i t y
concept city york ,
concept : personbornincity inv ,
concept person bill
concept city york ,
concept : personbornincity inv ,
concept person diane001
concept university college ,
concept : persongraduatedfromuniversity inv ,
concept person diane001
concept person diane001 ,
concept : personbornincity ,
concept city york
For the PersonLeadsOrganization task
Query :
( c o n c e p t j o u r n a l i s t b i l l p l a n t e ,
concept : personleadsorganization ,
concept company cnn
pbs )
Selected key edges :
c o n c e p t j o u r n a l i s t b i l l p l a n t e ,
concept : worksfor ,
concept televisionnetwork cbs
c o n c e p t j o u r n a l i s t b i l l p l a n t e ,
concept : agentcollaborateswithagent inv ,
concept televisionnetwork cbs
concept televisionnetwork cbs ,
concept : worksfor inv ,
c o n c e p t j o u r n a l i s t w a l t e r c r o n k i t e
25


## Page 26


Published as a conference paper at ICLR 2020
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
Figure 17: PersonLeadsOrganization. The head is concept journalist bill plante, the query relation
is concept:organizationheadquarteredincity, and the tail is concept company cnn pbs. The left is a full
subgraph derived with max attending from per step=20, and the right is a further pruned subgraph
from the left based on attention. The big yellow node represents the head, and the big red node
represents the tail. Color on the rest indicates attention scores over a T-step reasoning process,
where grey means less attention, yellow means more attention gained during early steps, and red
means gaining more attention when getting closer to the ﬁnal step.
concept televisionnetwork cbs ,
concept : agentcollaborateswithagent ,
c o n c e p t j o u r n a l i s t w a l t e r c r o n k i t e
concept televisionnetwork cbs ,
concept : worksfor inv ,
concept personus scott pelley
concept televisionnetwork cbs ,
concept : worksfor inv ,
concept actor daniel schorr
concept televisionnetwork cbs ,
concept : worksfor inv ,
concept person edward r
murrow
concept televisionnetwork cbs ,
concept : agentcollaborateswithagent ,
concept person edward r
murrow
concept televisionnetwork cbs ,
concept : worksfor inv ,
c o n c e p t j o u r n a l i s t b i l l p l a n t e
concept televisionnetwork cbs ,
concept : agentcollaborateswithagent ,
c o n c e p t j o u r n a l i s t b i l l p l a n t e
c o n c e p t j o u r n a l i s t w a l t e r c r o n k i t e ,
concept : worksfor ,
concept televisionnetwork cbs
c o n c e p t j o u r n a l i s t w a l t e r c r o n k i t e ,
concept : agentcollaborateswithagent inv ,
concept televisionnetwork cbs
c o n c e p t j o u r n a l i s t w a l t e r c r o n k i t e ,
concept : worksfor ,
concept nonprofitorganization cbs evening
concept personus scott pelley ,
concept : worksfor ,
concept televisionnetwork cbs
concept personus scott pelley ,
concept : personleadsorganization ,
concept televisionnetwork cbs
concept personus scott pelley ,
concept : personleadsorganization ,
concept company cnn
pbs
concept actor daniel schorr ,
concept : worksfor ,
concept televisionnetwork cbs
concept actor daniel schorr ,
concept : personleadsorganization ,
concept televisionnetwork cbs
concept actor daniel schorr ,
concept : personleadsorganization ,
concept company cnn
pbs
concept person edward r
murrow ,
concept : worksfor ,
concept televisionnetwork cbs
concept person edward r
murrow ,
concept : agentcollaborateswithagent inv ,
concept televisionnetwork cbs
concept person edward r
murrow ,
concept : personleadsorganization ,
concept televisionnetwork cbs
concept person edward r
murrow ,
concept : personleadsorganization ,
concept company cnn
pbs
concept televisionnetwork cbs ,
concept : organizationheadquarteredincity ,
concept city new york
concept televisionnetwork cbs ,
concept : headquarteredin ,
concept city new york
concept televisionnetwork cbs ,
concept : agentcollaborateswithagent ,
concept personeurope william paley
concept televisionnetwork cbs ,
concept : topmemberoforganization inv ,
concept personeurope william paley
concept company cnn
pbs ,
concept : headquarteredin ,
concept city new york
concept company cnn
pbs ,
concept : personbelongstoorganization inv ,
concept personeurope william paley
concept nonprofitorganization cbs evening ,
concept : worksfor inv ,
c o n c e p t j o u r n a l i s t w a l t e r c r o n k i t e
concept city new york ,
concept : organizationheadquarteredincity inv ,
concept televisionnetwork cbs
concept city new york ,
concept : headquarteredin inv ,
concept televisionnetwork cbs
concept city new york ,
concept : headquarteredin inv ,
concept company cnn
pbs
concept personeurope william paley ,
concept : agentcollaborateswithagent inv ,
concept televisionnetwork cbs
concept personeurope william paley ,
concept : topmemberoforganization ,
concept televisionnetwork cbs
concept personeurope william paley ,
concept : personbelongstoorganization ,
concept company cnn
pbs
concept personeurope william paley ,
concept : personleadsorganization ,
concept company cnn
pbs
For the OrganizationHiredPerson task
26


## Page 27


Published as a conference paper at ICLR 2020
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
Figure 18: OrganizationHiredPerson. The head is concept stateorprovince afternoon, the query rela-
tion is concept:organizationhiredperson, and the tail is concept personmexico ryan whitney. The left is a
full subgraph derived with max attending from per step=20, and the right is a further pruned subgraph
from the left based on attention. The big yellow node represents the head, and the big red node rep-
resents the tail. Color on the rest indicates attention scores over a T-step reasoning process, where
grey means less attention, yellow means more attention gained during early steps, and red means
gaining more attention when getting closer to the ﬁnal step.
Query :
( concept stateorprovince afternoon ,
concept : organizationhiredperson ,
concept personmexico ryan whitney )
Selected key edges :
concept stateorprovince afternoon ,
concept : atdate ,
concept dateliteral n2007
concept stateorprovince afternoon ,
concept : atdate ,
concept date n2003
concept stateorprovince afternoon ,
concept : atdate ,
concept dateliteral n2006
concept dateliteral n2007 ,
concept : atdate inv ,
concept country united states
concept dateliteral n2007 ,
concept : atdate inv ,
concept city home
concept dateliteral n2007 ,
concept : atdate inv ,
concept city service
concept dateliteral n2007 ,
concept : atdate inv ,
c o n c e p t c o u n t r y l e f t p a r t i e s
concept date n2003 ,
concept : atdate inv ,
concept country united states
concept date n2003 ,
concept : atdate inv ,
concept city home
concept date n2003 ,
concept : atdate inv ,
concept city service
concept date n2003 ,
concept : atdate inv ,
c o n c e p t c o u n t r y l e f t p a r t i e s
concept dateliteral n2006 ,
concept : atdate inv ,
concept country united states
concept dateliteral n2006 ,
concept : atdate inv ,
concept city home
concept dateliteral n2006 ,
concept : atdate inv ,
concept city service
concept dateliteral n2006 ,
concept : atdate inv ,
c o n c e p t c o u n t r y l e f t p a r t i e s
concept country united states ,
concept : atdate ,
concept year n1992
concept country united states ,
concept : atdate ,
concept year n1997
concept country united states ,
concept : organizationhiredperson ,
concept personmexico ryan whitney
concept city home ,
concept : atdate ,
concept year n1992
concept city home ,
concept : atdate ,
concept year n1997
concept city home ,
concept : organizationhiredperson ,
concept personmexico ryan whitney
concept city service ,
concept : atdate ,
concept year n1992
concept city service ,
concept : atdate ,
concept year n1997
concept city service ,
concept : organizationhiredperson ,
concept personmexico ryan whitney
c o n c e p t c o u n t r y l e f t p a r t i e s ,
concept : worksfor inv ,
concept personmexico ryan whitney
c o n c e p t c o u n t r y l e f t p a r t i e s ,
concept : organizationhiredperson ,
concept personmexico ryan whitney
concept year n1992 ,
concept : atdate inv ,
concept governmentorganization house
concept year n1992 ,
concept : atdate inv ,
concept country united states
concept year n1992 ,
concept : atdate inv ,
concept city home
concept year n1992 ,
concept : atdate inv ,
concept tradeunion congress
concept year n1997 ,
concept : atdate inv ,
concept governmentorganization house
concept year n1997 ,
concept : atdate inv ,
concept country united states
concept year n1997 ,
concept : atdate inv ,
concept city home
concept personmexico ryan whitney ,
concept : worksfor ,
concept governmentorganization house
27


## Page 28


Published as a conference paper at ICLR 2020
concept personmexico ryan whitney ,
concept : worksfor ,
concept tradeunion congress
concept personmexico ryan whitney ,
concept : worksfor ,
c o n c e p t c o u n t r y l e f t p a r t i e s
concept governmentorganization house ,
concept : personbelongstoorganization inv ,
concept personus party
concept governmentorganization house ,
concept : worksfor inv ,
concept personmexico ryan whitney
concept governmentorganization house ,
concept : organizationhiredperson ,
concept personmexico ryan whitney
concept tradeunion congress ,
concept : organizationhiredperson ,
concept personus party
concept tradeunion congress ,
concept : worksfor inv ,
concept personmexico ryan whitney
concept tradeunion congress ,
concept : organizationhiredperson ,
concept personmexico ryan whitney
c o n c e p t c o u n t r y l e f t p a r t i e s ,
concept : organizationhiredperson ,
concept personus party
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
Figure 19: AgentBelongsToOrganization. The head is concept person mark001, the query relation
is concept:agentbelongstoorganization, and the tail is concept geopoliticallocation world. The left is a
full subgraph derived with max attending from per step=20, and the right is a further pruned subgraph
from the left based on attention. The big yellow node represents the head, and the big red node
represents the tail. Color on the rest indicates attention scores over a T-step reasoning process,
where grey means less attention, yellow means more attention gained during early steps, and red
means gaining more attention when getting closer to the ﬁnal step.
For the AgentBelongsToOrganization task
Query :
( concept person mark001 ,
concept : agentbelongstoorganization ,
c o n c e p t g e o p o l i t i c a l l o c a t i o n w o r l d )
Selected key edges :
concept person mark001 ,
concept : personbelongstoorganization ,
concept sportsteam state university
concept person mark001 ,
concept : agentcollaborateswithagent ,
concept male world
concept person mark001 ,
concept : agentcollaborateswithagent inv ,
concept male world
concept person mark001 ,
concept : personbelongstoorganization ,
c o n c e p t p o l i t i c a l p a r t y c o l l e g e
concept sportsteam state university ,
concept : personbelongstoorganization inv ,
c o n c e p t p o l i t i c i a n j o b s
concept sportsteam state university ,
concept : personbelongstoorganization inv ,
concept person mark001
concept sportsteam state university ,
concept : personbelongstoorganization inv ,
concept person greg001
concept sportsteam state university ,
concept : personbelongstoorganization inv ,
concept person michael002
concept male world ,
concept : agentcollaborateswithagent ,
c o n c e p t p o l i t i c i a n j o b s
concept male world ,
concept : agentcollaborateswithagent inv ,
c o n c e p t p o l i t i c i a n j o b s
concept male world ,
concept : agentcollaborateswithagent ,
concept person mark001
concept male world ,
concept : agentcollaborateswithagent inv ,
concept person mark001
concept male world ,
concept : agentcollaborateswithagent ,
concept person greg001
concept male world ,
concept : agentcollaborateswithagent inv ,
concept person greg001
concept male world ,
concept : agentcontrols ,
concept person greg001
concept male world ,
concept : agentcollaborateswithagent ,
concept person michael002
concept male world ,
concept : agentcollaborateswithagent inv ,
concept person michael002
c o n c e p t p o l i t i c a l p a r t y c o l l e g e ,
concept : personbelongstoorganization inv ,
concept person mark001
c o n c e p t p o l i t i c a l p a r t y c o l l e g e ,
concept : personbelongstoorganization inv ,
concept person greg001
c o n c e p t p o l i t i c a l p a r t y c o l l e g e ,
concept : personbelongstoorganization inv ,
concept person michael002
c o n c e p t p o l i t i c i a n j o b s ,
concept : personbelongstoorganization ,
concept sportsteam state university
c o n c e p t p o l i t i c i a n j o b s ,
concept : agentcollaborateswithagent ,
concept male world
28


## Page 29


Published as a conference paper at ICLR 2020
c o n c e p t p o l i t i c i a n j o b s ,
concept : agentcollaborateswithagent inv ,
concept male world
c o n c e p t p o l i t i c i a n j o b s ,
concept : worksfor ,
c o n c e p t g e o p o l i t i c a l l o c a t i o n w o r l d
concept person greg001 ,
concept : personbelongstoorganization ,
concept sportsteam state university
concept person greg001 ,
concept : agentcollaborateswithagent ,
concept male world
concept person greg001 ,
concept : agentcollaborateswithagent inv ,
concept male world
concept person greg001 ,
concept : agentcontrols inv ,
concept male world
concept person greg001 ,
concept : agentbelongstoorganization ,
c o n c e p t g e o p o l i t i c a l l o c a t i o n w o r l d
concept person greg001 ,
concept : personbelongstoorganization ,
c o n c e p t p o l i t i c a l p a r t y c o l l e g e
concept person greg001 ,
concept : agentbelongstoorganization ,
concept recordlabel friends
concept person michael002 ,
concept : personbelongstoorganization ,
concept sportsteam state university
concept person michael002 ,
concept : agentcollaborateswithagent ,
concept male world
concept person michael002 ,
concept : agentcollaborateswithagent inv ,
concept male world
concept person michael002 ,
concept : agentbelongstoorganization ,
c o n c e p t g e o p o l i t i c a l l o c a t i o n w o r l d
concept person michael002 ,
concept : personbelongstoorganization ,
c o n c e p t p o l i t i c a l p a r t y c o l l e g e
concept geopoliticallocation world ,
concept : worksfor inv ,
concept personmexico ryan whitney
concept geopoliticallocation world ,
concept : organizationhiredperson ,
concept personmexico ryan whitney
concept geopoliticallocation world ,
concept : worksfor inv ,
c o n c e p t p o l i t i c i a n j o b s
concept recordlabel friends ,
concept : organizationhiredperson ,
concept personmexico ryan whitney
concept personmexico ryan whitney ,
concept : worksfor ,
c o n c e p t g e o p o l i t i c a l l o c a t i o n w o r l d
concept personmexico ryan whitney ,
concept : organizationhiredperson inv ,
c o n c e p t g e o p o l i t i c a l l o c a t i o n w o r l d
concept personmexico ryan whitney ,
concept : organizationhiredperson inv ,
concept recordlabel friends
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
Figure 20: TeamPlaysInLeague. The head is concept sportsteam mavericks, the query relation is
concept:teamplaysinleague, and the tail is concept sportsleague nba. The left is a full subgraph derived
with max attending from per step=20, and the right is a further pruned subgraph from the left based on
attention. The big yellow node represents the head, and the big red node represents the tail. Color on
the rest indicates attention scores over a T-step reasoning process, where grey means less attention,
yellow means more attention gained during early steps, and red means gaining more attention when
getting closer to the ﬁnal step.
For the TeamPlaysInLeague task
Query :
( concept sportsteam mavericks ,
concept : teamplaysinleague ,
concept sportsleague nba )
Selected key edges :
concept sportsteam mavericks ,
concept : teamplayssport ,
concept sport basketball
concept sportsteam mavericks ,
concept : teamplaysagainstteam ,
concept sportsteam boston celtics
concept sportsteam mavericks ,
concept : teamplaysagainstteam inv ,
concept sportsteam boston celtics
concept sportsteam mavericks ,
concept : teamplaysagainstteam ,
concept sportsteam spurs
concept sportsteam mavericks ,
concept : teamplaysagainstteam inv ,
concept sportsteam spurs
concept sport basketball ,
concept : teamplayssport inv ,
concept sportsteam college
concept sport basketball ,
concept : teamplayssport inv ,
concept sportsteam marshall university
concept sportsteam boston celtics ,
concept : teamplaysinleague ,
concept sportsleague nba
concept sportsteam spurs ,
concept : teamplaysinleague ,
concept sportsleague nba
concept sportsleague nba ,
concept : agentcompeteswithagent ,
concept sportsleague nba
29


## Page 30


Published as a conference paper at ICLR 2020
concept sportsleague nba ,
concept : agentcompeteswithagent inv ,
concept sportsleague nba
concept sportsteam college ,
concept : teamplaysinleague ,
concept sportsleague international
30

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1906.06826v6
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1906.06826v6_Homogeneous_Network_Embedding_for_Massive_Graphs_via_Reweighted_Personalized_Pag

> Source: 1906.06826v6_Homogeneous_Network_Embedding_for_Massive_Graphs_via_Reweighted_Personalized_Pag.pdf

> Pages: 17

---


## Page 1


Homogeneous Network Embedding for Massive Graphs via
Reweighted Personalized PageRank
[Technical Report]
Renchi Yang∗, Jieming Shi†, Xiaokui Xiao†, Yin Yang§, Sourav S. Bhowmick∗
∗School of Computer Science and Engineering, Nanyang Technological University, Singapore
†School of Computing, National University of Singapore, Singapore
§College of Science and Engineering, Hamad Bin Khalifa University, Qatar
∗{yang0461,assourav}@ntu.edu.sg,†{shijm,xkxiao}@nus.edu.sg,§yyang@hbku.edu.qa
ABSTRACT
Given an input graph G and a node v ∈G, homogeneous
network embedding (HNE) maps the graph structure in the
vicinity of v to a compact, ﬁxed-dimensional feature vector.
This paper focuses on HNE for massive graphs, e.g., with
billions of edges. On this scale, most existing approaches
fail, as they incur either prohibitively high costs, or severely
compromised result utility.
Our proposed solution, called Node-Reweighted PageR-
ank (NRP), is based on a classic idea of deriving embedding
vectors from pairwise personalized PageRank (PPR) values.
Our contributions are twofold: ﬁrst, we design a simple and
eﬃcient baseline HNE method based on PPR that is capa-
ble of handling billion-edge graphs on commodity hardware;
second and more importantly, we identify an inherent draw-
back of vanilla PPR, and address it in our main proposal
NRP.
Speciﬁcally, PPR was designed for a very diﬀerent
purpose, i.e., ranking nodes in G based on their relative im-
portance from a source node’s perspective. In contrast, HNE
aims to build node embeddings considering the whole graph.
Consequently, node embeddings derived directly from PPR
are of suboptimal utility.
The proposed NRP approach overcomes the above deﬁ-
ciency through an eﬀective and eﬃcient node reweighting
algorithm, which augments PPR values with node degree
information, and iteratively adjusts embedding vectors ac-
cordingly. Overall, NRP takes O(m log n) time and O(m)
space to compute all node embeddings for a graph with m
edges and n nodes. Our extensive experiments that com-
pare NRP against 18 existing solutions over 7 real graphs
demonstrate that NRP achieves higher result utility than all
the solutions for link prediction, graph reconstruction and
node classiﬁcation, while being up to orders of magnitude
faster. In particular, on a billion-edge Twitter graph, NRP
terminates within 4 hours, using a single CPU core.
This
work
is
licensed
under
the
Creative
Commons
Attribution-
NonCommercial-NoDerivatives 4.0 International License. To view a copy
of this license, visit http://creativecommons.org/licenses/by-nc-nd/4.0/. For
any use beyond those covered by this license, obtain permission by emailing
info@vldb.org. Copyright is held by the owner/author(s). Publication rights
licensed to the VLDB Endowment.
Proceedings of the VLDB Endowment, Vol. 13, No. 5
ISSN 2150-8097.
DOI: https://doi.org/10.14778/3377369.3377376
PVLDB Reference Format:
Renchi Yang, Jieming Shi, Xiaokui Xiao, Yin Yang, and Sourav
S. Bhowmick.
Homogeneous Network Embedding for Massive
Graphs via Reweighted Personalized PageRank. PVLDB, 13(5):
670-683, 2020.
DOI: https://doi.org/10.14778/3377369.3377376
1.
INTRODUCTION
Given a graph G = (V, E) with n nodes, a network em-
bedding maps each node v ∈G to a compact feature vector
in Rk (k ≪n), such that the embedding vector captures
the graph features surrounding v.
These embedding vec-
tors are then used as inputs in downstream machine learn-
ing operations [44, 49, 58]. A homogeneous network embed-
ding (HNE) is a type of network embedding that reﬂects
the topology of G rather than labels associated with nodes
or edges.
HNE methods have been commonly applied to
various graph mining tasks based on neighboring associated
similarities, including node classiﬁcation [38], link predic-
tion [3], and graph reconstruction [33]. This paper focuses
on HNE computation on massive graphs, e.g., social net-
works involving billions of connections. Clearly, an eﬀective
solution for such a setting must be highly scalable and eﬃ-
cient, while obtaining high result utility.
HNE is a well studied problem in the data mining litera-
ture, and there are a plethora of solutions. However, most
existing solutions fail to compute eﬀective embeddings for
large-scale graphs. For example, as we review in Section 2,
a common approach is to learn node embeddings from ran-
dom walk simulations, e.g., in [18, 34]. However, the num-
ber of possible random walks grows exponentially with the
length of the walk; thus, for longer walks on a large graph, it
is infeasible for the training process to cover even a consid-
erable portion of the random walk space. Another popular
methodology is to construct node embeddings by factorizing
a proximity matrix, e.g., in [66]. The eﬀectiveness of such
methods depends on the proximity measure between node
pairs. As explained in Section 2, capturing multi-hop topo-
logical information generally requires a sophisticated prox-
imity measure; on the other hand, the computation, storage
and factorization of such a proximity matrix often incur pro-
hibitively high costs on large graphs.
This paper revisits an attractive idea: constructing HNEs
by taking advantage of personalized PageRank (PPR) [23].
Speciﬁcally, given a pair of nodes u, v ∈G, the PPR value
π(u, v) of v with respect to u is the probability that a random
1
arXiv:1906.06826v6  [cs.SI]  23 Jun 2020


## Page 2


v2v2
v1v1
v3v3
v4v4
v5v5
v6v6
v7v7
v8v8
v9v9
Figure 1: An example graph G.
Table 1: PPR for v2 and v9 in Fig. 1 (α = 0.15).
vi
v1
v2
v3
v4
v5
v6
v7
v8
v9
π(v2, vi)
0.15
0.269
0.188
0.118
0.17
0.048
0.029
0.019
0.008
π(v4, vi)
0.15
0.118
0.188
0.269
0.17
0.048
0.029
0.019
0.008
π(v7, vi)
0.036
0.043
0.056
0.043
0.093
0.137
0.29
0.187
0.12
π(v9, vi)
0.02
0.024
0.031
0.024
0.056
0.083
0.168
0.311
0.282
walk from u terminates at v. PPR values can be viewed as
a concise summary of an inﬁnite number of random walk
simulations, which, intuitively, should be helpful in building
node embeddings. Realizing the full potential of PPR for
scalable HNE computation, however, is challenging.
One
major hurdle is cost: materializing the PPR between each
pair of nodes clearly takes O(n2) space for n nodes (e.g.,
in [61]), and evaluating even a single PPR value can involve
numerous random walk simulations (e.g., in [45,67]).
Further, we point out that even without considering com-
putational costs, it is still tricky to properly derive HNEs
from PPR values.
The main issue is that PPR was de-
signed to serve a very diﬀerent purpose, i.e., ranking nodes
in G based on their relative importance from a source node’s
perspective. In other words, PPR is essentially a local mea-
sure. On the other hand, HNE aims to summarize nodes
from the view of the whole graph. To illustrate this crit-
ical diﬀerence, consider the example in Fig. 1 with nodes
v1-v9. Observe that between the node pair v2 and v4, there
are three diﬀerent nodes connecting them, i.e., v1, v3 and
v5. In contrast, there is only one common neighbor between
v9 and v7.
Intuitively, if we were to predict a new edge
in the graph, it is more likely to be (v2, v4) than (v9, v7).
For instance, in a social network, the more mutual friends
two users have, the more likely they know each other [4].
However, as shown in Table 1, in terms of PPR values, we
have π(v9, v7) = 0.168 > π(v2, v4) = 0.118, which tends to
predict (v9, v7) over (v2, v4) and contradicts with the above
intuition.
This shows that PPR by itself is not an ideal
proximity measure, at least for the task of link prediction.
This problem is evident in PPR-based HNE methods, e.g.,
in [45, 67], and a similar issue limits the eﬀectiveness of a
recent proposal [61], as explained in Section 2.
This paper addresses both the scalability and result utility
issues of applying PPR to HNE computation with a novel
solution called Node-Reweighted PageRank (NRP). Specif-
ically, we ﬁrst present a simple and eﬀective baseline ap-
proach that overcomes the eﬃciency issue of computing node
embeddings using PPR values. The main proposal NRP then
extends this baseline by addressing the above-mentioned de-
ﬁciency of conventional PPR. Speciﬁcally, NRP augments
PPR values with additional reweighting steps, which cali-
brate the embedding of each node to its in- and out- de-
grees. Intuitively, when a node has a large number of neigh-
bors (e.g., v2 in Fig.
1), its embedding vector should be
weighted up in accordance with its degree, so as to reﬂect
the importance of the node from the perspective of the whole
graph. In NRP, node reweighting is performed using an ef-
fective and scalable algorithm that iteratively adjusts node
embeddings, whose cost is small compared to PPR compu-
tations. Overall, NRP takes O (k(m + kn) log n) time and
O(m + nk) space to construct length-k embeddings of all
nodes in a graph with n nodes and m edges. In the com-
mon case that k is small and the graph is sparse, the above
complexities reduce to O(m log n) time and O(m) space.
We have conducted extensive experiments on 7 popular
real datasets, and compared NRP against 18 existing HNE
solutions on three tasks: link prediction, graph reconstruc-
tion and node classiﬁcation. In all settings, NRP achieves
the best result utility. Meanwhile, with a few exceptions,
NRP is often orders of magnitude faster than its competi-
tors. In particular, on a Twitter graph with 1.2 billion edges,
NRP terminates within 4 hours on a single CPU core.
2.
RELATED WORK
Network embedding is a hot topic in graph mining, for
which there exists a large body of literature as surveyed
in [5, 11, 63].
Here we review the HNE methods that are
most relevant to this work.
Learning HNEs from random walks. A classic method-
ology for HNE computation is to learn embeddings from
random walk simulations.
Earlier methods in this cate-
gory include DeepWalk [34], LINE [42], node2vec [18] and
Walklets [35]. The basic idea is to learn the embedding of
a node v by iteratively “pulling” the embeddings of posi-
tive context nodes (i.e., those that are on the random walks
originating from v) towards that of v, and “pushing” the
embeddings of negative context nodes (i.e., the nodes that
are not connected to v) away from v. Subsequent propos-
als [8, 39] construct a multilayer graph over the original
graph G, and then perform random walks on diﬀerent lay-
ers to derive more eﬀective embeddings. Instead of using
a predeﬁned sampling distribution, SeedNE [16] adaptively
sample negative context nodes in terms of their informa-
tiveness. GraphCSC-M [9] learns the embeddings of diﬀerent
centrality-based random walks, and combines these embed-
dings into one by weighted aggregation. Recent techniques
APP [67] and VERSE [45] improve the quality of embeddings
by reﬁning the procedures for learning from PPR-based ran-
dom walk samples. However, neither of them addresses the
deﬁciency of conventional PPR as described in Section 1.
The main problem of random-walk-based HNE learning in
general is their immense computational costs (proportional
to the number of random walks), which can be prohibitive
for large graphs. The high running time could be reduced
with massively-parallel hardware, e.g., in PBG [29], and/or
with GPU systems, e.g., in Graphy [69]. Nevertheless, they
still incur a high ﬁnancial cost for consuming large amounts
of computational resources.
Learning HNEs without random walks. HNEs can also
be learned directly from the graph structure using a deep
neural network, without performing random walks. Train-
ing such a deep neural network, however, also incurs very
high computational overhead, especially for large graphs
[45]. Notably, SDNE [47] and DNGR [7] employ multi-layer
auto-encoders with a target proximity matrix to learn em-
beddings. GAE [25] combines the graph convolutional net-
2


## Page 3


work [26] and auto-encoder models to learn embeddings.
PRUNE [28] utilizes a Siamese neural network to preserve
both pointwise mutual information and global PageRank
of nodes. NetRA [62] and DRNE [46] learn embeddings by
feeding node sequences to a long short-term memory model
(LSTM). DVNE [68] learns a Gaussian distribution in the
Wasserstein space with the deep variational model as the la-
tent representation of each node. GA [1] applies graph atten-
tion mechanism to a closed-form expectation of the limited
random-walk co-occurrence matrices [34] to learn the em-
beddings. GraphGAN [48], ANE [12] and DWNS [13] adopt
the popular generative adversarial networks (GAN) to accu-
rately model the node connectivity probability. As demon-
strated in our experiments, none of these methods scale to
large graphs.
Constructing HNEs through matrix factorization.
Another popular methodology for HNE is through factor-
izing a proximity matrix M ∈Rn×n, where n is the number
of nodes in the input graph G, and each entry M[i, j] signi-
ﬁes the proximity between a pair of nodes vi, vj ∈G. The
main research question here is how to choose an appropri-
ate M that (i) captures the graph topology well and (ii) is
eﬃcient to compute and factorize on large graphs. Specif-
ically, to satisfy (i), each entry M[i, j] ∈M should accu-
rately reﬂect the proximity between nodes vi, vj via indirect
connections, which can be long and complex paths. Mean-
while, to satisfy (ii) above, the computation / factorization
of M should be done in memory. This means that M should
either be sparse, or be eﬃciently factorized without mate-
rialization. In addition, note that for a directed graph G,
the proximity is also directed, meaning that it is possible
that M[i, j] ̸= M[j, i]. Thus, methods that require M to
be symmetric are limited to undirected graphs and cannot
handle directed graphs.
Earlier factorization-based work, including [2, 6, 43, 55],
directly computes M before factorizing it to obtain node
embeddings. For instance, spectral embedding [43] simply
outputs the top k eigenvectors of the Laplacian matrix of an
undirected graph G as node embeddings. This method has
limited eﬀectiveness [18, 34], as the Laplacian matrix only
captures one-hop connectivity information for each node.
To remedy this problem, one idea is to construct a higher-
order proximity matrix M to capture multi-hop connectivity
for each node [6,55,59]. However, such a higher-order prox-
imity matrix M is usually no longer sparse; consequently,
materializing M becomes prohibitively expensive for large
graphs due to the O(n2) space complexity for n nodes.
Recent work [33, 65, 66] constructs network embeddings
without materializing M, to avoid extreme space overhead.
Many of these methods, however, rely on the assumption
that M is symmetric; consequently, they are limited to undi-
rected graphs as discussed above. For instance, AROPE [66]
ﬁrst applies an eigen-decomposition on the adjacency matrix
A of an undirected graph G, and then utilizes the decom-
position results to derive each node’s embedding to preserve
proximity information, without explicitly constructing M.
Similar approaches have been adopted in [33,65]. In partic-
ular, RandNE [65] uses a Gaussian random projection of M
directly as node embeddings without factorization, in order
to achieve high eﬃciency, at the cost of lower result utility.
The authors of [37] prove that random-walk-based meth-
ods such as as DeepWalk, LINE and node2vec essentially
perform matrix factorizations. Thus, they propose NetMF,
which factorizes a proximity matrix M that approximates
the closed form representation of DeepWalk’s implicit prox-
imity matrix. However, NetMF requires materializing a dense
M, which is infeasible for large graphs. NetSMF [36] im-
proves the eﬃciency of NetMF by sparsifying M using the
theory of spectral sparsiﬁcation. However, NetSMF is still
rather costly as it requires simulating a large number of
random walks to construct M. ProNE [64] learns embed-
dings via matrix factorization with the enhancement of spec-
tral propagation.
However, ProNE is mainly designed for
node classiﬁcation, and its accuracy is less competitive for
other tasks such as link prediction and graph reconstruc-
tion. GRA [30] iteratively ﬁne-tunes the proximity matrix
to obtain enhanced result eﬀectiveness, at the expense of
high comptuational costs.
HNE via Approximate Personalized PageRank. Al-
though the idea of using PPR as the proximity measure
to be preserved in the embeddings is often mentioned in
random-walk-based solutions [45,67], these methods largely
fail to scale due to numerous random walk simulations for
the costly training process. A recent work STRAP [61] ob-
tains better scalability by computing and factorizing a PPR-
based proximity matrix instead. Speciﬁcally, STRAP builds
node embeddings by factorizing the transpose proximity ma-
trix, deﬁned as M = Π + Π⊤, where Π and Π⊤represent
the approximate PPR matrices of the original graph G and
its transpose graph (i.e., obtained by reversing the direction
of each edge in G), respectively.
The space and time complexities of STRAP are O( n
δ ) and
O( m
δ + nk2), respectively, where δ is the error threshold for
PPR values. In the literature of approximate PPR process-
ing (e.g., [41,51,53,54,56]), δ is commonly set to
1
n, which
would lead to prohibitively high space (i.e., O(n2)) and time
(i.e., O(mn + nk2)) costs in STRAP. Instead, in [61], the
authors ﬁx δ to a constant 10−5 and only retain PPR values
greater than δ
2, which compromises result utility. Even so,
STRAP is still far more expensive than the proposed solution
NRP, as shown in our experiments.
Further, as explained in Section 1, conventional PPR is
not an ideal proximity measure for the purpose of HNE
due to the former’s relative nature; this problem propa-
gates to STRAP which uses the PPR-based transpose prox-
imity measure, i.e., π(u, v) + π(v, u) for each node pair
u, v ∈G. For instance, in the example of Table 1, we have
π(v7, v9) + π(v9, v7) = 0.288 > π(v2, v4) + π(v4, v2) = 0.236,
indicating that STRAP also tends to predict (v9, v7) over
(v2, v4) in link prediction, which is counter-intuitive as we
have explained in Section 1.
Other HNE methods. There also exist several techniques
that generate embeddings without random walks, neural
networks or matrix factorization. In particular, NetHiex [31]
applies expectation maximization to learn embeddings that
capture the neighborhood structure of each node, as well as
the latent hierarchical taxonomy in the graph. RaRE [19]
considers both the proximity and popularity of nodes, and
derive embeddings by maximizing a posteriori estimation us-
ing stochastic gradient descent. GraphWave [14] represents
each node’s neighborhood via a low-dimensional embedding
by leveraging heat wavelet diﬀusion patterns, so as to cap-
ture structural roles of nodes in networks. node2hash [50]
transplants the feature hashing technique for word embed-
dings to embed nodes in networks.
A common problem
3


## Page 4


Table 2: Frequently used notations.
Notation
Description
G=(V, E)
A graph G with node set V and edge set E
n, m
The numbers of nodes and edges in G, respec-
tively
din(vi)
The in-degree of node vi
dout(vi)
The out-degree of node vi
A, D, P
The adjacency, out-degree and transition matri-
ces of G
α
The random walk decay factor
k
The dimensionality of the embedding vectors
X, Y
The forward and backward embeddings, respec-
tively
−
→
w v, ←
−
w v
The forward and backward weights for v’s for-
ward and backward embeddings, respectively
with the above methods is that they do not aim to pre-
serve proximity information between nodes; consequently,
they are generally less eﬀective for tasks such as link pre-
diction and graph reconstruction, as demonstrated in our
experiments in Section 5.
3.
SCALABLE PPR COMPUTATION AND
FACTORIZATION
This section presents ApproxPPR, a simple and eﬀective
baseline approach to HNE that obtains node embeddings
through factorizing a conceptual approximate PPR prox-
imity matrix. Unlike previous methods, ApproxPPR scales
to billion-edge graphs without seriously compromising re-
sult quality.
ApproxPPR forms the foundation of the our
main proposal NRP, presented in Section 4.
In what fol-
lows, Section 3.1 overviews ApproxPPR and formally deﬁnes
the main concepts. Section 3.2 presents the main contribu-
tion in ApproxPPR: a scalable approximate PPR factoriza-
tion algorithm. Table 2 summarizes frequent notations used
throughout the paper.
3.1
Overview
As mentioned in Section 1, given an input graph G =
(V, E), the goal of HNE is to construct a size-k embedding
for each node v ∈G, where k is a user-speciﬁed per-node
space budget.
The input graph G can be either directed
or undirected. For simplicity, in the following we assume
that G is directed; for an undirected graph, we simply re-
place each undirected edge (u, v) with two directed ones with
opposing direction, i.e., (u, v) and (v, u). Note that the ca-
pability to handle directed graphs is an advantage of our
methods, compared to existing solutions that are limited to
undirected graphs, e.g., [31,36,64–66].
In a directed graph, each node plays two roles: as the in-
coming end and outgoing end of edges, respectively. These
two roles can have very diﬀerent semantics. For instance,
in a social graph, a user can deliberately choose to follow
users who he/she is interested in, and is followed by users
who are interested in him/her. The follower relationships
and followee relationships of the same user should have dif-
ferent representations. This motivates building two separate
embedding vectors Xv and Yv for each node v, referred to
as the forward and backward embeddings of v, respectively.
In our solutions, we assign equal space budget (i.e.,
k
2 ) to
Xv and Yv.
One advantage of ApproxPPR is that, it uses the PPR
proximity matrix to do the factorization, without actually
matrializing the matrix. Speciﬁcally, the deﬁnition of PPR
is based on random walks, as follows. Suppose that we start
a random walk from a source node u.
At each step, we
terminate the walk with probability α, and continue the
walk (i.e., moving on to a random out-neighbor of u) with
probability 1 −α. Then, for each node v ∈G, we deﬁne its
PPR π(u, v) with respect to source node u as the probability
that the walk originating from u terminates at v.
Formally, let Π be an n×n matrix where Π[i, j] = π(vi, vj)
for the i-th node vi and j-th node vj in G, and P be the
probability transition matrix of G, i.e., P[i, j] =
1
dout(vi),
where vj is an out-neighbor of vi and dout(vi) denotes the
out-degree of vi. Then,
Π = P∞
i=0 α(1 −α)i · Pi.
(1)
ApproxPPR directly uses Π as the proximity matrix, i.e.,
M = Π. The goal is then to factorize Π into the forward
and backward embeddings of nodes of the input graph G,
such that for each pair of nodes u and v, i.e.:
XuY⊤
v ≈π(u, v)
(2)
Remark.
Note that directly computing Π (and subse-
quently factorizing it into the node embeddings X and Y)
is infeasible for a large graph. In particular, Π is a dense
matrix that requires O(n2) space for n nodes, and Eq. (1)
involves summing up an inﬁnite series.
To alleviate this
problem, we could apply an approximate PPR algorithm
[52, 54, 56] to compute the top-L largest PPR values for
each node in G, which reduces the space overhead to O(nL).
Unfortunately, even the state-of-the-art approximate top-L
PPR algorithm, i.e., TopPPR, is insuﬃcient for our pur-
pose.
Speciﬁcally, TopPPR takes O

L
1
4 n
3
4 log n
√gapρ

time to
compute the approximate top-L PPR values for each node,
where gapρ ≤1 is a parameter that quantiﬁes the diﬀerence
between the top-L and non-top-L PPR values [56]. To ap-
proximate the entire Π, we would need to invoke TopPPR
for every node, which incurs time super-quadratic to n.
Empirically, Ref. [56] reports that running TopPPR on a
billion-edge Twitter graph (used in our experiments as well)
takes about 15 seconds CPU time, for L = 500. The same
graph contains over 41 million nodes, meaning that run-
ning TopPPR on each of them would cost over 19 years of
CPU time, which is infeasible even for a powerful computing
cluster. While it is theoretically possible to reduce compu-
tational costs by choosing a small L and/or a large error
threshold in TopPPR, doing so would lead to numerous ze-
ros in Π, which seriously degrades the result quality. We
address this challenge in the next subsection with a simple
and eﬀective solution.
3.2
PPR Approximation
Observe that our goal is to obtain the node embeddings
X and Y, rather than the PPR matrix Π itself.
Thus,
the main idea of ApproxPPR is to integrate the computa-
tion and factorization of Π in the same iterative algorithm.
Speciﬁcally, according to Eq. (1), Π can be viewed as the
weighted sum of proximity values of diﬀerent orders, i.e.,
one-hop proxmity, two-hop proximity, etc.
Therefore, in-
stead of ﬁrst computing Π and then factorizing this dense
4


## Page 5


matrix into node embeddings, we can instead start by fac-
torizing the sparse ﬁrst-order proximity matrix (i.e., P) into
the initial embeddings X and Y, and then iteratively reﬁne
X and Y, thereby incorporating higher-order information
into them.
This allows us to avoid the substantial space
and computational overheads incurred for the construction
and factorization of the n × n dense matrix Π.
First, we consider a truncated version of Π as follows:
Π′ = Pℓ1
i=1 α(1 −α)i · Pi,
(3)
where ℓ1 is a relative large constant (e.g., ℓ1 = 20). In other
words, we set
Π′ = Π −αI −
P+∞
i=ℓ1+1 α(1 −α)i · Pi
,
where I denotes an n × n identity matrix. The rationale is
that when i is suﬃciently large, α(1 −α)i is small, in which
case P+∞
i=ℓ1+1 α(1 −α)i · Pi becomes negligible. In addition,
αI only aﬀects the PPR π(u, u) from each node u to itself,
which has no impact on our objective in Eq. (2) since we
only concern the PPR values between diﬀerent nodes.
To decompose Π′, observe that
Π′ =
Pℓ1
i=1 α(1 −α)i · Pi−1
D−1A,
where A is the adjacency matrix of G, and D is an n×n diag-
onal matrix where the i-th diagonal element is dout(vi). In-
stead of applying exact singular value decomposition (SVD)
that is very time consuming, we factorize A using the BKSVD
algorithm in [32] for randomized SVD, obtaining two n × k′
matrices U, V and a k′ × k′ diagonal matrix Σ given inputs
A and k′, such that UΣV⊤≈A.
In short, BKSVD re-
duces A to a low-dimensional space by the Gaussian random
projection and then performs SVD on the low-dimensional
matrix.
Given a relative error threshold ϵ, BKSVD guar-
antees a (1 + ϵ) error bound for spectral norm low-rank
approximation, which is much tighter than the theoretical
accuracy bounds provided by previous truncated SVD algo-
rithms [10,21,40].
Given the output U, Σ, V from BKSVD, we set
X1 = D−1U
√
Σ and Y = V
√
Σ.
After that, we compute
Xi = (1 −α)PXi−1 + X1 for i = 2, . . . , ℓ1,
and set X = α(1 −α)Xℓ1. This results in
X = Pℓ1
i=1 α(1 −α)iPi−1X1 and
XY⊤= Pℓ1
i=1 α(1 −α)iPi−1 · X1Y⊤
Note that X1Y⊤≈D−1A = P.
It can be veriﬁed that
XY⊤≈Π′. Particularly, the following theorem establishes
the accuracy guarantees of ApproxPPR.
Theorem 1. Given A, D−1, P, the dimensionality k′, the
random walk decay factor α, the number of iterations ℓ1 and
error threshold ϵ for BKSVD as inputs to Algorithm 1, it
returns embedding matrices X and Y (X, Y ∈Rn×k′ ) that
satisfy, for every pair of nodes (u, v) ∈V × V with u ̸= v,
Π[u, v] −(XY⊤)[u, v]

≤(1 + ϵ)σk′+1(1 −α)(1 −(1 −α)ℓ1) + (1 −α)ℓ1+1,
Algorithm 1: ApproxPPR
Input: A, D−1, P, α, k′, ℓ1, ϵ.
Output: X, Y.
1 [U, Σ, V] ←BKSVD(A, k′, ϵ);
2 X1 ←D−1U
√
Σ,
Y ←V
√
Σ;
3 for i ←2 to ℓ1 do
4
Xi ←(1 −α)PXi−1 + X1;
5 X ←α(1 −α)Xℓ1;
6 return X, Y;
and for every node u ∈V ,
X
v∈V
Π[u, v] −(XY⊤)[u, v]

≤√n(1 + ϵ)σk′+1(1 −α)(1 −(1 −α)ℓ1) + (1 −α)ℓ1+1,
where σk′+1 is the (k′ + 1)-th largest singular value of A.
Proof. See Appendix A for the proof.
Theorem 1 indicates that the PPR value between any pair
of nodes preserved in the embedding vectors X and Y has
absolute error at most (1 + ϵ)σk′+1(1 −α)(1 −(1 −α)ℓ1) +
(1−α)ℓ1+1 and average absolute error of
1
√n(1+ϵ)σk′+1(1−
α)(1−(1−α)ℓ1) + 1
n(1−α)ℓ1+1. Observe that the accuracy
of the preserved PPR is restricted by ϵ and σk′+1, namely
the accuracy of the low-rank approximation, i.e., BKSVD.
Finally, we use Xv and Yv as the initial forward and back-
ward embeddings, respectively, for each node v. Algorithm 1
summarizes the pseudo-code for this construction of X and
Y. Next, we present a concrete example.
Example 1. Given input graph G in Fig. 1 and input
parameters k′ = 2, α = 0.15, ℓ1 = 20, we run Algorithm
1 on G.
It ﬁrst applies BKSVD on the adjacency matrix
A ∈R9×9, which produces X1 ∈R9×2 and Y ∈R9×2 as
shown in Fig. 2.
ApproxPPR ﬁrst sets X = X1. Then, in each of the fol-
lowing iterations, the algorithm updates X to 0.85 · PX +
X1. After repeating this process for ℓ1 −1 = 19 iterations,
ApproxPPR scales X by the weight α(1−α) = 0.1275 and re-
turns us X and Y as in Fig. 2. The inner product between
Xu and Yv approximates π(u, v).
For example, consider
node pairs ⟨v2, v4⟩and ⟨v9, v7⟩:
Xv2Y⊤
v4 = [−0.18, 0.004] · [−0.668, −0.359]⊤= 0.119,
Xv9Y⊤
v7 = [−0.157, 0.236] · [−0.105, 0.633]⊤= 0.166,
which are close to π(v2, v4) and π(v9, v7) in Table 1 respec-
tively.
□
Time Complexity. By the analysis in Ref. [32], applying
BKSVD on A requires O

(mk′ + nk′2) log n
ϵ

time, where
ϵ is a constant that controls the tradeoﬀbetween the eﬃ-
ciency and accuracy of SVD. In addition, Lines 2, 4, and 5
in Algorithm 1 respectively run in O(mk′) time. Therefore,
the overall time complexity of Algorithm 1 is
O
log n
ϵ
+ ℓ1

mk′ + log n
ϵ
nk′2

,
which equals O (k(m + kn) log n) when ϵ and ℓ1 are regarded
as constants.
5


## Page 6


Y=


Yv1
Yv2
Yv3
Yv4
Yv5
Yv6
Yv7
Yv8
Yv9


=


−0.652,
0.243
−0.668, −0.359
−0.823, −0.142
−0.668, −0.359
−0.737,
0.547
−0.314,
−0.42
−0.105,
0.633
−0.094, −0.225
−0.071,
0.818


, X1 =


−0.217, −0.121
−0.223,
0.091
−0.206,
0.008
−0.223,
0.091
−0.184,
−0.13
−0.157,
0.4
−0.083,
−0.16
−0.047,
0.481
−0.032, −0.034


, · · · , X=


Xv1
Xv2
Xv3
Xv4
Xv5
Xv6
Xv7
Xv8
Xv9


=


−0.182, −0.014
−0.18,
0.004
−0.14, −0.002
−0.18,
0.004
−0.13, −0.008
−0.182, 0.075
−0.126, 0.072
−0.092, 0.141
−0.157, 0.236


Figure 2: Illustration of Example 1 for the ApproxPPR algorithm.
4.
PROPOSED NRP ALGORITHM
The ApproxPPR algorithm presented in the previous sec-
tion directly uses PPR as the proximity measure. However,
as explained in Section 1, PPR by itself is not suitable for
our purpose since it is a local measure, in the sense that PPR
values are relative with respect to the source node. Conse-
quently, PPR values for diﬀerent source nodes are essen-
tially incomparable, which is the root cause of the counter-
intuitive observation in the example of Fig. 1 and Table 1.
In the proposed algorithm NRP, we address the deﬁciency
of PPR through a technique that we call node reweighting.
Speciﬁcally, for any two nodes u and v, we aim to ﬁnd for-
ward and backward embeddings such that:
XuY⊤
v ≈−→
w u · π(u, v) · ←−
w v
(4)
where π(u, v) is the PPR value of v with respect to node
u as source, −→
w u and ←−
w v are weights assigned to u and v,
respectively. In other words, we let X⊤
u Yv preserve a scaled
version of π(u, v). The goal of NRP is then to ﬁnd approx-
imate node weights so that Eq. (4) properly expresses the
proximity between nodes u and v. In NRP, the node weights
are learned through an eﬃcient optimization algorithm, de-
scribed later in this section. The proposed node reweighting
overcomes the deﬁciency of PPR, which is conﬁrmed in our
experiments.
In the following, Section 4.1 explains the choice of node
weights in NRP. Sections 4.2 and 4.3 elaborate on the com-
putation of node weights. Section 4.4 summarizes the com-
plete NRP algorithm.
4.1
Choice of Node Weights
As discussed before, the problem of PPR as a proximity
measure is that it is a relative measure with respect to the
source node. In particular, the PPR value does not take into
account the number of out-going and in-coming edges that
each node has. To address this issue, NRP assigns to each
node u a forward weight −→
w u and a backward weight ←−
w u, and
uses −→
w u·π(u, v)·←−
w v instead of π(u, v) to gauge the strength
of connection from u to v, as in Eq. (4). To compensate for
the lack of node degree data in PPR values, we choose the
forward and backward weights such that
∀u ∈V ,
X
∀v∈V \u
(−→
w u · π(u, v) · ←−
w v) ≈dout(u), and
∀v ∈V ,
X
∀u∈V \v
(−→
w u · π(u, v) · ←−
w v) ≈din(v).
(5)
In other words, for any nodes u, v ∈G, we aim to ensure
that (i) the “total strength” of connections from u to other
nodes is roughly equal to the out-degree dout(u) of u, and
(ii) the total strength of connection from other nodes to v
is roughly to equal the in-degree din(v) of v. The rationale
is that if u has a large out-degree, then it is more likely to
be connected to other nodes, and hence, the proximity from
u to other nodes should be scaled up accordingly. The case
for a node v with a large in-degree is similar. In Section 5,
we empirically show that this scaling approach signiﬁcantly
improves the eﬀectiveness of our embeddings for not just
link prediction but also other important graph analysis task
such as graph reconstruction.
4.2
Learning Node Weights
Given the output X and Y of ApproxPPR (Algorithm 1),
we use XvY⊤
v as an approximation of π(u, v) for any two
diﬀerent nodes u and v. Then we formulate an objective
function O for tuning node weights according to Eq. (5):
O = min
−
→
w ,←
−
w
X
v






X
u̸=v
−→
w uXuY⊤
v ←−
w v

−din(v)






2
+
X
u






X
v̸=u
−→
w uXuY⊤
v ←−
w v

−dout(u)






2
(6)
+ λ
X
u
 ∥−→
w u∥2 + ∥←−
w u∥2

,
subject to ∀u ∈V, −→
w u, ←−
w u ≥1
n.
To explain, recall that we use −→
w uXuY⊤
v ←−
w v to quantify the
strength of connection from u to v, and hence, for any ﬁxed u
(resp. v), P
u̸=v
 −→
w uXuY⊤
v ←−
w v

measures the total strength
of connections from u to other nodes (resp. from other nodes
to v). Therefore, by minimizing O, we aim to ensure that
the total strength of connections starting from (resp. ending
at) each node u is close to u’s out-degree (resp. in-degree),
subject to a regularization term λ P
u (∥−→
w u∥2 + ∥←−
w u∥2). In
addition, we require that −→
w u, ←−
w u ≥
1
n for all nodes u to
avoid negative node weights.
We derive an approximate solution for Eq. (6) using coor-
dinate descent [57]: We start with an initial solution −→
w v =
dout(v) and ←−
w v = 1 for each node v, and then iteratively
update each weight based on the other 2n −1 weights. In
particular, for any node v∗, the formula for updating ←−
w v∗
is derived by taking the partial derivative of the objective
6


## Page 7


function in Eq. (6) with respect to ←−
w v∗:
∂O
∂←
−
w v∗= 2
h P
u̸=v∗−→
w uXu

Y⊤
v∗
2 ←−
w v∗
−din(v∗)
P
u̸=v∗−→
w uXu

Y⊤
v∗
+ P
u
P
v̸=u,v̸=v∗−→
w uXuY⊤
v ←−
w v
 −→
w uXuY⊤
v∗
+ P
u̸=v∗
 −→
w uXuY⊤
v∗
2 ←−
w v∗
−
 P
u dout(u)−→
w uXu

Y⊤
v∗+ λ←−
w v∗
i
= 2(a3 −a2 −a1) + 2(b1 + b2 + λ)←−
w v∗,
where
a1 =
 P
u dout(u)−→
w uXu

Y⊤
v∗,
a2 =din(v∗)
P
u̸=v∗−→
w uXu

Y⊤
v∗,
a3 = P
u
P
v̸=u,v̸=v∗−→
w uXuY⊤
v ←−
w v
 −→
w uXuY⊤
v∗,
(7)
b1 = P
u̸=v∗
 −→
w uXuY⊤
v∗
2 ,
b2 =
P
u̸=v∗−→
w uXu

Y⊤
v∗
2
.
We identify the value of ←−
w v∗that renders the above par-
tial derivative zero, i.e.,
∂O
∂←
−
w v∗= 0. If the identiﬁed ←−
w v∗is
smaller than
1
n, then we set it to
1
n instead to avoid neg-
ativity.
This leads to the following formula for updating
backward weight ←−
w v∗:
←−
w v∗= max
 1
n, a1 + a2 −a3
b1 + b2 + λ

(8)
The formula for updating −→
w u∗is similar and included in
Appendix B for brevity.
By Eq. (8), each update of ←−
w v∗requires computing a1, a2,
a3, b1 and b2. Towards this end, a straightforward approach
is to compute these variables directly based on their deﬁni-
tions in Eq. (7). This, however, leads to tremendous over-
heads. In particular, computing a1, a2, and b2 requires a lin-
ear scan of Xu for each node u, which requires O(nk′) time.
Deriving b1 requires computing −→
w uXuY⊤
v∗for each node u,
which incurs O(nk′2) overhead. Furthermore, computing b3
requires calculating −→
w uXuY⊤
v ←−
w v for all u ̸= v ̸= v∗, which
takes O(n2k′2) time. Therefore, each update of ←−
w v∗takes
O(n2k′2), which leads to a total overhead of O(n3k′2) for
updating all ←−
w v∗once. Apparently, this overhead is pro-
hibitive for large graphs. To address this deﬁciency, in Sec-
tion 4.3, we present a solution that reduces the overhead to
O(nk′2) instead of O(n3k′2).
4.3
Accelerating Weight Updates
We observe that the updates of diﬀerent node weights
share a large amount of common computation. For exam-
ple, for any node v∗, deriving a1 always requires computing
P
u dout(u)−→
w uXu. Intuitively, if we are able to reuse the re-
sult of such common computation for diﬀerent nodes, then
the overheads of our coordinate descent algorithm could be
signiﬁcantly reduced. In what follows, we elaborate how we
exploit this idea to accelerate the derivation of a1, a2, a3, b1,
and b2.
Computation of a1, a2, b2. By the deﬁnitions of a1, a2, b2
in Eq. (7),
a1 = ξY⊤
v∗, a2 = din(v∗)(χ −−→
w v∗Xv∗)Y⊤
v∗,
and b2 =

(χ −−→
w v∗Xv∗) Y⊤
v∗
2
,
(9)
where ξ =
X
u
dout(u)−→
w uXu, and χ =
X
u
−→
w uXu.
Eq. (9) indicates that the a1 values of all nodes v∗∈V
share a common ξ, while a2 and b2 of each node v∗have
χ in common. Observe that both ξ and χ are independent
of any backward weight. Motivated by this, we propose to
ﬁrst compute ξ ∈R1×k′ and χ ∈R1×k′, which takes O(nk′)
time. After that, we can easily derive a1, a2, and b2 for any
node with precomputed ξ and χ. In that case, each update
of a1, a2, and b2 takes only O(k′) time, due to Eq. (9). This
leads to O(nk′) (instead of O(n2k′)) total computation time
of a1, a2, and b2 for all nodes.
Computation of a3. Note that
a3 =
X
u
 X
v
−→
w uXuY⊤
v ←−
w v
!
−→
w uXuY⊤
v∗
−
X
u
−→
w uXuY⊤
v∗←−
w v∗
 −→
w uXuY⊤
v∗
−
X
v
−→
w vXvY⊤
v ←−
w v
 −→
w vXvY⊤
v∗
+
−→
w v∗Xv∗Y⊤
v∗←−
w v∗
 −→
w v∗Xv∗Y⊤
v∗,
which can be rewritten as:
a3 =ρ1ΛY⊤
v∗−←−
w v∗Yv∗ΛY⊤
v∗−ρ2Y⊤
v∗
+ ←−
w v∗

Xv∗Y⊤
v∗
2 −→
w 2
v∗,
where Λ =
X
u
−→
w 2
u(X⊤
u Xu), ρ1 =
X
v
←−
w vYv,
(10)
and ρ2 =
X
v
−→
w 2
v · ←−
w v

XvY⊤
v

Xv

.
Observe that Λ is independent of any backward weight.
Thus, it can be computed once and reused in the compu-
tation of a3 for all nodes. Meanwhile, both ρ1 and ρ2 are
dependent on all of the backward weights, and hence, can-
not be directly reused if we are to update each backward
weight in turn. However, we note that ρ1 and ρ2 can be
incrementally updated after the change of any single back-
ward weight. Speciﬁcally, suppose that we have computed
ρ1 and ρ2 based on Eq. (10), and then we change the back-
ward weight of v∗from ←−
w ′
v∗as ←−
w v∗. In that case, we can
update ρ1 and ρ2 as:
ρ1 = ρ1 +
 ←−
w v∗−←−
w ′
v∗
Yv∗,
ρ2 = ρ2 +
 ←−
w v∗−←−
w ′
v∗ −→
w 2
v∗

Xv∗Y⊤
v∗

Xv∗.
(11)
Since ←−
w v∗, ←−
w ′
v∗∈R and Xv∗, Yv∗∈R1×k′, each of such
updates takes only O(k′) time.
The initial values of ρ1 and ρ2 can be computed in O(nk′)
time based on Eq. (10), while Λ can be calculated in O(nk′2)
time.
Given Λ, ρ1, and ρ2, we can compute a3 for any
node v∗in O(k′2) time based on Eq. (10). Therefore, the
total time required for computing a3 for all nodes is O(nk′2),
7


## Page 8


Algorithm 2: updateBwdWeights
Input: G, k′, −
→
w, ←
−
w, X, Y.
Output: ←
−
w
1 Compute ξ, χ, ρ1, ρ2, Λ, and Φ based on Eq. (9), (10), and
(13);
2 for r ←1 to k′ do
3
φ[r] = P
u −
→
w 2
uXu[r]2;
4 for v∗∈V in random order do
5
Compute a1, a2, a3, b1, b2 by Eq. (9), (10), and (14);
6
←
−
w ′
v∗= ←
−
w v∗;
7
←
−
w v∗= max
n
1
n, a1+a2−a3
b1+b2+λ
o
;
8
ρ1 = ρ1 +
 ←
−
w v∗−←
−
w ′
v∗

Yv∗;
9
ρ2 = ρ2 +
 ←
−
w v∗−←
−
w ′
v∗
 −
→
w 2
v∗
 Xv∗Y⊤
v∗

Xv∗
10 return ←
−
w;
ξ = [−8.1453, −7.6509], χ = [−3.5227, −3.2933],
ρ1 = [−4.2126, −3.7234], ρ2 = [−1.2659, −1.1678],
Λ =

1.4478,
1.3308
1.3308,
1.2575

, φ = [1.4478, 1.2575].
Figure 3: Illustration for Example 2
which is an signiﬁcant reduction from the O(n3k′2) time
required by the naive solution described in Section 4.2.
Approximation of b1. We observe that the value of b1
is insigniﬁcant compared to b2.
Thus, we propose to ap-
proximate its value instead of deriving it exactly, so as to
reduce computation cost. By the inequality of arithmetic
and geometric means, we have:
1
k′ b1 ≤P
u̸=v∗−→
w 2
u(Pk′
r=1 Xu[r]2Yv∗[r]2) ≤b1.
(12)
Let φ be a length-k′ vector where the r-th (r ∈[1, k′]) ele-
ment is
φ[r] = P
u −→
w 2
uXu[r]2.
(13)
We compute φ in O(nk′) time, and then, based on Eq. (12),
we approximate b1 for each node in O(k′) time with
b1 ≈k′
2
Pk′
r=1 Yv∗[r]2(φ[r] −−→
w 2
v∗Xv∗[r]2).
(14)
Therefore, the total cost for approximating b1 for all nodes
is O(nk′).
Summary. As a summary, Algorithm 2 presents the pseudo-
code of our method for updating the backward weight of
each node. The algorithm ﬁrst computes ξ, χ, ρ1, ρ2, Λ, φ
in O(nk′2) time (Lines 1-3). After that, it examines each
node’s backward weight in random order, and computes
a1, a2, a3, b1, b2 by Eq. (9), (10), and (14), which takes O
 k′2
time per node (Line 5).
Given a1, a2, a3, b1, b2, the algo-
rithm updates the backward weight examined, and then up-
dates ρ1 and ρ2 in O(k′) time (Lines 7-9). The total time
complexity of Algorithm 2 is O(nk′2), which is signiﬁcantly
better than the O(n3k′2)-time method in Section 4.2. We
illustrate Algorithm 2 with an example.
Example 2. Suppose that we invoke Algorithm 2 given
graph G in Fig. 1, k′ = 2, X and Y from Example 1, and
the following ←−
w and −→
w :
←−
w = [1, 1, 1, 1, 1, 1, 1, 1, 1] ,
−→
w = [3, 3, 4, 3, 4, 2, 2, 2, 1] .
The algorithm ﬁrst computes ξ, χ, ρ1, ρ2, Λ and φ accord-
ing to Eq. (9), (10), and (13). Fig. 3 shows the results.
Then, we update each backward weight in a random order
with the above precomputed values. Let’s pick ←−
w v1 for the
ﬁrst update. According to Eq. (9), (10) and (14), we do not
need to perform summations over all 9 nodes as in Eq. (7)
but some multiplications between a 2×2 matrix and a length-
2 vector, as well as inner products between length-2 vectors,
yielding the following results fast:
a1 = ξY⊤
v1 = 7.7968,
a2 = 2(χ −2Xv1)Y⊤
v1 = 5.903,
a3 = ρ1ΛY⊤
v1 −Yv1ΛY⊤
v1 −ρ2Y⊤
v1 = 8.1324,
b1 =
2
X
r=1
Yv1[r]2(φ[r] −−→
w 2
v1Xv1[r]2) = 0.9683,
b2 =

(χ −2Xv1) Y⊤
v1
2
= 8.7113.
Let λ = 0. The backward weight for v1 is updated as
←−
w v1 = max
1
9, a1 + a2 −a3
b1 + b2

= 0.5752,
and then ρ1 and ρ2 are updated accordingly with the updated
←−
w v1 based on Eq. (11) before proceeding to the next backward
weight.
□
Remark. The forward weights −→
w v∗can be learned using an
algorithm very similar to Algorithm 2, with the same space
and time complexities. For brevity, we include the details
in Appendix B.
4.4
Complete NRP Algorithm and Analysis
Algorithm 3 presents the pseudo-code for constructing
embeddings with NRP. Given a graph G, embedding dimen-
sionality k, random walk decay factor α, thresholds ℓ1, ℓ2
and relative error threshold ϵ, it ﬁrst generates the initial
embedding matrices X and Y using Algorithm 1 (Lines 1-2,
see Section 3.2 for details).
After that, it initializes the
forward and backward weights for each node (Lines 3-4)
and then applies coordinate descent to reﬁne the weights
(Lines 5-7). In particular, in each epoch of the coordinate
descent, it ﬁrst invokes Algorithm 2 to update each back-
ward weight once (Line 6), and then applies a similar algo-
rithm to update each forward weight once (Line 7, see Algo-
rithm updateFwdWeights in Appendix B). The total number
of epochs is controlled by ℓ2, which we set to O(log n) for
eﬃciency.
After the coordinate descent terminates, NRP
multiplies the forward (resp. backward) embedding of each
node by its forward (resp. backward) weight to obtain the
ﬁnal embeddings (Lines 8-9).
Complexity Analysis.
NRP has three main steps: Al-
gorithm 1, Algorithm 2, and Algorithm updateFwdWeights.
By the analysis of time complexity in Section 3.2, Algorithm
1 runs in O (k(m + kn) log n) time, and its space overhead
is determined by the number of non-zero entries in the ma-
trices, which is O(m + nk). For Algorithm 2 and Algorithm
updateFwdWeights, each epoch takes O(nk′2) time, as anal-
ysed in Section 4.3. Hence, the time complexities of Algo-
rithm 2 and Algorithm updateFwdWeights are both O(nk′2)
when the number of epochs ℓ2 is a constant. In addition, the
space costs of Algorithm 2 and Algorithm updateFwdWeights
depend on the size of ξ, χ, ρ1, ρ2, Λ, φ and the number of
8


## Page 9


Algorithm 3: NRP
Input: Graph G, embedding dimensionality k, thresholds
ℓ1, ℓ2, random walk decay factor α and error
threshold ϵ
Output: Embedding matrices X and Y.
1 k′ ←k/2;
2 [X, Y] ←ApproxPPR(A, D−1, P, α, k′, ℓ1, ϵ);
3 for v ∈V do
4
−
→
w v = dout(v), ←
−
w v = 1;
5 for l ←1 to ℓ2 do
6
←
−
w = updateBwdWeights(G, k′, −
→
w, ←
−
w, X, Y);
7
−
→
w = updateFwdWeights(G, k′, −
→
w, ←
−
w, X, Y);
8 for v ∈V do
9
Xv = −
→
w v · Xv, Yv = ←
−
w v · Yv;
10 return X, Y;
Table 3: Dataset statistics (K = 103, M = 106, B =
109).
Name
|V |
|E|
Type
#labels
Wiki
4.78K
184.81K
directed
40
BlogCatalog
10.31K
333.98K
undirected
39
Youtube
1.13M
2.99M
undirected
47
TWeibo
2.32M
50.65M
directed
100
Orkut
3.1M
234M
undirected
100
Twitter
41.6M
1.2B
directed
-
Friendster
65.6M
1.8B
undirected
-
weights, which is bounded by O(nk′). As a result, the time
complexity of Algorithm 3 is O (k(m + kn) log n) and its
space complexity is O(m + nk).
5.
EXPERIMENTS
We experimentally evaluate our proposed method, i.e.,
NRP, against 18 existing methods, including 4 classic ones
and 14 recent ones, on three graph analysis tasks: link pre-
diction, graph reconstruction, and node classiﬁcation. We
also study the eﬃciency of all methods and analyze the pa-
rameter choices of NRP. All experiments are conducted us-
ing a single thread on a Linux machine powered by an Intel
Xeon(R) E5-2650 v2@2.60GHz CPU and 96GB RAM.
5.1
Experimental Settings
Datasets. We experiment with seven real networks that
are used in previous work [18,33,45], including two billion-
edge networks: directed network Twitter [27] and undirected
network Friendster [60]. Table 3 shows the dataset statistics.
For Wiki, BlogCatalog, Youtube, and Orkut, we use the node
labels suggested in previous work [18, 34, 45]. For TWeibo,
we collect its node tags from [24] and only keep the top 100
tags in the network, following the practice in [45].
Competitors.
We evaluate NRP against eighteen exist-
ing methods, including four classic methods (i.e., DeepWalk,
node2vec, LINE and DNGR) and fourteen recent methods,
many of which have not been compared against each other
in previous work. To our knowledge, we are the ﬁrst to sys-
tematically evaluate such a large number of existing network
embedding techniques. We categorize the eighteen existing
methods into four groups as follows:
1. factorization-based methods: AROPE [66], RandNE [65],
NetSMF [36], ProNE [64], and STRAP [61];
2. random-walk-based methods: DeepWalk [34], LINE [42],
node2vec [18], PBG [29], APP [67], and VERSE [45];
3. neural-network-based methods: DNGR [7], DRNE [46],
GraphGAN [48], and GA [1];
4. other methods: RaRE [20], NetHiex [31] and GraphWave
[14].
Parameter Settings.
For NRP, we set ℓ1 = 20, ℓ2 =
10, α = 0.15, ϵ = 0.2, and λ = 10.
Note that ℓ1 = 20
means up to 20-order proximities can be preserved in the
embeddings, and most forward and backward weights con-
verge with ℓ2 = 10 epochs. For fair comparison, the random
walk decay factor, α, is set to 0.15, in all PPR-based meth-
ods, including VERSE, APP, STRAP, and NRP. We use the
default parameter settings of all competitors as suggested in
their papers. For instance, the error threshold δ in STRAP is
set to 10−5 as suggested in [61]. We obtain the source codes
of all competitors from their respective authors. Unless oth-
erwise speciﬁed, we set the embedding dimensionality k of
each method to 128.
Note that AROPE, RandNE, NetHiex, GraphWave, NetSMF
and ProNE are designed for undirected graphs only. For a
thorough evaluation, we still report their performance on
the directed graphs, i.e., Wiki, TWeibo, and Twitter, by
omitting the direction of each edge when feeding the graphs
as input to these methods.
In addition, the following methods are designed for some
speciﬁc tasks: e.g., GraphWave and DRNE for structural role
discovery; node2vec, DeepWalk, LINE, DNGR, NetSMF and
ProNE for node classiﬁcation or network visualization. For
completeness, we evaluate all methods over three commonly
used tasks, namely, link prediction, node classiﬁcation, and
graph reconstruction.
We exclude a method if it cannot
report results within 7 days.
5.2
Link Prediction
Link prediction aims to predict which node pairs are likely
to form edges. Following previous work [66], we ﬁrst remove
30% randomly selected edges from the input graph G, and
then construct embeddings on the modiﬁed graph G′. After
that, we form a testing set Etest consisting of (i) the node
pairs corresponding to the 30% removed edges, and (ii) an
equal number of node pairs that are not connected by any
edge in G. Note that on directed graphs, each node pair
(u, v) is ordered, i.e., we aim to predict whether there is a
directed edge from u to v.
Given a method’s embeddings, we compute a score for
each node pair (u, v) in the testing set based on embedding
vectors of u and v, and then evaluate the method’s perfor-
mance by the Area Under Curve (AUC) of the computed
scores. Following their own settings, for AROPE, RandNE,
NetHiex, NetSMF and ProNE, the score for (u, v) is computed
as the inner product u and v’s embedding vectors; for NRP,
ApproxPPR, APP, GA, and STRAP, the score equals the in-
ner product of u’s forward vector and v’s backward vec-
tor. For RaRE, we apply the probability function described
in [19] for computing the score for (u, v).
For DeepWalk,
LINE, node2vec, DNGR, DRNE, GraphGAN, and GraphWave,
we use the edge features approach [31]: (i) for each node
pair (u, v) in G, concatenate u’s and v’s embeddings into
9


## Page 10


VERSE
VERSE
GA
GA
RandNE
RandNE
AROPE
AROPE
APP
APP
NRP
NRP
ProNE
ProNE
node2vec
node2vec
PBG
PBG
STRAP
STRAP
DRNE
DRNE
NetHiex
NetHiex
DeepWalk
DeepWalk
LINE
LINE
GraphGAN
GraphGAN
NetSMF
NetSMF
GraphWave
GraphWave
DNGR
DNGR
ApproxPPR
ApproxPPR
RaRE
RaRE
0.8
0.82
0.84
0.86
0.88
0.9
0.92
16
32
64
128
256
k
AUC
(a) Wiki
0.925
0.935
0.945
0.955
0.965
16
32
64
128
256
k
AUC
(b) BlogCatalog
0.96
0.964
0.968
0.972
0.976
0.98
16
32
64
128
256
k
AUC
(c) TWeibo
0.76
0.8
0.84
0.88
0.92
16
32
64
128
256
k
AUC
(d) Orkut
0.8
0.82
0.84
0.86
0.88
0.9
0.92
16
32
64
128
256
k
AUC
(e) Twitter
0.82
0.86
0.9
0.94
0.98
16
32
64
128
256
k
AUC
(f) Friendster
Figure 4:
Link prediction results vs.
embedding
dimensionality k (best viewed in color).
a length-2k vector; (ii) sample a training set of node pairs
E′
train (with same size as Etest), such that half of the node
pairs are from G′ and the other half are node pairs not con-
nected in G; (iii) feed the length-2k vectors of node pairs
in E′
train into a logistic regression classiﬁer; (iv) then use
the classiﬁer to obtain the scores of node pairs in Etest for
link prediction. For VERSE and PBG, the inner product ap-
proach only works for undirected graphs, since VERSE and
PBG generate only one embedding vector per node, due to
which the inner product approach cannot diﬀerentiate (u, v)
from (v, u). Therefore, on directed graphs, we also employ
the aforementioned edge features approach for VERSE and
PBG.
Fig. 4 shows AUC of each method when k varies from 16
to 256. NRP consistently outperforms all competitors, by a
signiﬁcant margin of up to 3% on Orkut and Friendster, and
a large margin of 0.5% to 2% on other graphs. Compared
with the best competitor, i.e., AROPE, NRP achieves a con-
siderable gain of 1.9% on Orkut when k = 128. Note that
NRP outperforms all the PPR-based competitors, includ-
ing ApproxPPR, APP, VERSE and STRAP, over all datasets,
which conﬁrms the eﬃcacy of our reweighting scheme in
NRP, and validates our analysis of the conventional PPR
deﬁciency in Section 1. Moreover, we observe that VERSE
is worse on directed graphs, i.e., Wiki and TWeibo, al-
though it is the best competitor on undirected graph Blog-
Catalog.
This is because that VERSE generates only one
embedding vector per node, making it fail to capture the
asymmetric transitivity (i.e., direction of edges) in directed
graphs [33, 67], which is critical for link prediction.
Our
method, NRP, instead generates two embedding vectors per
node and successfully distinguishes the edge directions and
thus is more promising. STRAP and GA cannot eﬃciently
handle large graphs (i.e., Youtube, TWeibo, Orkut, Twit-
ter and Friendster), since they require the materialization
of a large n × n matrix, which is extremely costly in terms
of both space and time; in contrast, NRP does not require
to do so.
NRP also consistently outperforms AROPE by
about 2% absolute improvement on all graphs. For the other
competitors, their performance is also less than satisfactory,
as shown in the ﬁgures. In summary, for link prediction,
NRP yields considerable performance improvements com-
pared with the state-of-the-art methods, over graphs with
various sizes.
5.3
Graph Reconstruction
Following previous work, for this task, we (i) take a set S
of node pairs from the input graph G, (ii) compute the score
of each pair using the same approach as in link prediction,
and then (iii) examine the top-K node pairs to identify the
fraction of them that correspond to the edges in G. This
fraction is referred to as the precision@K of the method
considered. On Wiki and BlogCatalog, we let S be the set of
all possible node pairs. Meanwhile, on Youtube and TWeibo,
following previous work [65,66], we construct S by taking a
1% sample of the
 n
2

possible pairs of nodes. We exclude
the results on Orkut and Twitter since 1% of all the possible
node pairs from these two graphs are excessively large.
Fig. 5 shows the performance of all methods for graph
reconstruction, varying K from 10 to 106. For readability,
we split the results of each dataset into two sub-ﬁgures in
vertical, and each sub-ﬁgure compares NRP against a sub-
set of the competitors.
NRP outperforms all competitors
consistently on all datasets. NRP remains highly accurate
when K increases to 104 or even 105, while the precisions
of other methods, especially GA, AROPE, RandNE, APP,
VERSE and STRAP, drop signiﬁcantly.
Speciﬁcally, NRP
achieves at least 90% precision when K reaches 104 on Wiki,
Blogcatalog and TWeibo, which means at least 10% absolute
improvement over state-of-the-art methods. In addition, on
Youtube, NRP achieves 2-8% absolute improvement over the
best competitors, including VERSE. The superiority of NRP
over the other PPR-based methods, i.e., ApproxPPR, APP,
VERSE and STRAP, in graph reconstruction demonstrates
the power of our reweighting scheme. Meanwhile, the im-
provements over all other methods like GA, AROPE and
RandNE implies that NRP accurately captures the structural
information of the input graph via PPR.
5.4
Node Classiﬁcation
Node classiﬁcation aims to predict each node’s label(s)
based on its embeddings. Following previous work [45], we
ﬁrst construct network embeddings from the input graph
G, and use the embeddings and labels of a random subset
of the nodes to train a one-vs-all logistic regression classi-
ﬁer, after which we test the classiﬁer with the embeddings
10


## Page 11


VERSE
VERSE
GA
GA
DRNE
DRNE
RandNE
RandNE
AROPE
AROPE
NetHiex
NetHiex
APP
APP
DeepWalk
DeepWalk
LINE
LINE
NRP
NRP
ProNE
ProNE
PBG
PBG
node2vec
node2vec
GraphGAN
GraphGAN
NetSMF
NetSMF
STRAP
STRAP
GraphWave
GraphWave
DNGR
DNGR
RaRE
RaRE
ApproxPPR
ApproxPPR
0
0.2
0.4
0.6
0.8
1.0
10
102
103
104
105
106
K
precision@K
0
0.2
0.4
0.6
0.8
1.0
10
102
103
104
105
106
K
precision@K
0
0.2
0.4
0.6
0.8
1.0
10
102
103
104
105
106
K
precision@K
0.2
0.4
0.6
0.8
1.0
10
102
103
104
105
106
K
precision@K
0
0.2
0.4
0.6
0.8
1.0
10
102
103
104
105
106
K
precision@K
(a) Wiki
0
0.2
0.4
0.6
0.8
1.0
10
102
103
104
105
106
K
precision@K
(b) BlogCatalog
0
0.2
0.4
0.6
0.8
1.0
10
102
103
104
105
106
K
precision@K
(c) Youtube
0
0.2
0.4
0.6
0.8
1.0
10
102
103
104
105
106
K
precision@K
(d) Tweibo
Figure 5: Graph reconstruction results vs. K (best viewed in color).
0.4
0.43
0.46
0.49
0.52
0.55
0.1
0.3
0.5
0.7
0.9
percentage of nodes
Micro-F1
(a) Wiki
0.32
0.34
0.36
0.38
0.40
0.42
0.1
0.3
0.5
0.7
0.9
percentage of nodes
Micro-F1
(b) BlogCatalog
 0.3
 0.35
 0.4
 0.45
 0.5
0.1
0.3
0.5
0.7
0.9
percentage of nodes
Micro-F1
(c) Youtube
0.34
0.345
0.35
0.355
0.36
0.1
0.3
0.5
0.7
0.9
percentage of nodes
Micro-F1
(d) TWeibo
Figure 6: Node classiﬁcation results (best viewed in color).
and labels of the remaining nodes. In particular, for NRP,
ApproxPPR, APP, GA, and STRAP, we ﬁrst normalize the
forward and backward vectors, respectively, of each node v,
and then concatenate them as the feature representation of v
before feeding it to the classiﬁer. Note that the embeddings
produced by NRP are weighted versions of that produced by
ApproxPPR, and thus, they have the same feature represen-
tation for each node v after the normalization, for the task
of node classiﬁcation.
Fig. 6 shows the Micro-F1 score achieved by each method
when the percentage of nodes used for training varies from
10% to 90% (i.e., 0.1 to 0.9 in the ﬁgures).
The Macro-
F1 results are qualitatively similar and thus omitted for the
interest of space.
NRP consistently outperforms all com-
petitors on Wiki and TWeibo, and has comparable perfor-
mance to ProNE on BlogCatalog and Youtube. Speciﬁcally,
on Wiki, NRP achieves an impressive improvement of at least
3% in Micro-F1 over existing methods and about 1% lead
on TWeibo, which is considerable in contrast to that of our
competitors. This demonstrates that NRP can accurately
capture the graph structure via PPR. On BlogCatalog and
Youtube, NRP, NetHiex, VERSE and ProNE all achieve com-
parable performance. ProNE is slightly better than NRP, but
note that ProNE can only handle undirected graphs and is
speciﬁcally designed for node classiﬁcation task by employ-
ing graph spectrum and graph partition techniques. NetHiex
also requires the input graphs to be undirected. VERSE can-
not achieve the same high-quality performance on directed
graphs (Fig. 6a and 6d) as it does on undirected graphs
(Fig. 6b and 6c).
The reason is that VERSE only gener-
ates one embedding vector per node, and neglects the di-
rections of edges in the directed graphs, while our method
NRP can preserve the directions. Typically, NRP achieves
consistent and outstanding performance for node classiﬁca-
tion task over all the real-world graphs.
5.5
Efﬁciency
Fig. 7 plots the time required by each method to con-
struct embeddings, when k is varied from 16 to 256. Note
that the Y-axis is in log-scale, and that the reported time
excludes the overheads for loading datasets and outputting
embeddings. We also omit any method with processing time
exceeding 7 days. For a fair comparison, all methods are ran
with a single thread.
Among all methods tested, NRP strikes the best balance
between eﬀectiveness and eﬃciency, and is up to 2 orders
of magnitude faster than all methods except ApproxPPR,
ProNE, RandNE and AROPE. In addition, as illustrated in
11


## Page 12


VERSE
VERSE
GA
GA
RandNE
RandNE
AROPE
AROPE
APP
APP
NRP
NRP
ProNE
ProNE
node2vec
node2vec
PBG
PBG
STRAP
STRAP
DRNE
DRNE
NetHiex
NetHiex
DeepWalk
DeepWalk
LINE
LINE
GraphGAN
GraphGAN
NetSMF
NetSMF
GraphWave
GraphWave
DNGR
DNGR
ApproxPPR
ApproxPPR
RaRE
RaRE
10-1
100
101
102
103
16
32
64
128
256
k
running time (second)
(a) Wiki
100
101
102
103
16
32
64
128
256
k
running time (second)
(b) BlogCatalog
102
103
104
105
16
32
64
128
256
k
running time (second)
(c) TWeibo
102
103
104
16
32
64
128
256
k
running time (second)
(d) Orkut
103
104
105
16
32
64
128
256
k
running time (second)
(e) Twitter
104
105
16
32
64
128
256
k
running time (second)
(f) Friendster
Figure 7: Running time vs. embedding dimension-
ality k (best viewed in color).
Fig. 4, 5, and 6, RandNE and AROPE are both less eﬀec-
tive compared to NRP for the three tasks. Furthermore, the
results of RandNE, AROPE, and ProNE on directed graphs
(i.e., Wiki, TWeibo and Twitter) are all inferior to those of
NRP, as shown in Fig. 4, 5, and 6. This is because RandNE,
AROPE, and ProNE are speciﬁcally designed for undirected
graphs instead of directed graphs.
ProNE is also inferior
to NRP in terms of link prediction and graph reconstruc-
tion on undirected graphs. Although ApproxPPR runs faster
than NRP, it is less eﬀective than the latter in terms of
link prediction and graph reconstruction, due to the deﬁ-
ciency of conventional PPR discussed in Section 1. Neither
GA nor STRAP is able to scale to large graphs, which again
manifests the power of our scalable PPR computation. The
remaining methods either rely on expensive training phases
(e.g., DeepWalk and VERSE), or require constructing a huge
matrix (e.g., NetSMF), thereby failing to handle large graphs
eﬃciently as well.
5.6
Parameter Analysis
We study the eﬀect of varying the parameters in NRP,
including α, ϵ, ℓ1 and ℓ2, for link prediction on Wiki, Blog-
catalog and Youtube datasets. Note that α is the decay factor
in PPR (Eq. (1) in Section 3.1); ϵ is the error threshold of
BKSVD used in our PPR approximation (Algorithm 1); ℓ1
is the number of iterations for computing PPR (Algorithm
1); ℓ2 is the number of epochs for reweighting node embed-
dings (Algorithm 3). The AUC results are shown in Fig. 8,
when one of the parameters is varied, the others are kept as
default values in Section 5.1.
Fig. 8a displays the AUC of NRP when we vary the decay
factor α from 0.1 to 0.9. As α increases, the performance
downgrades since only limited local neighborhoods of nodes
are preserved and high-order proximities are failed to be
captured in the embeddings, which is consistent with the
observation in [45,61]. When α = 0.1 or 0.2, the AUC score
is the highest, which holds on all the three datasets. And
thus our choice of α = 0.15 makes sure that the best eﬃcacy
is achieved.
The AUC result of NRP when varying ϵ from 0.1 to 0.9
is depicted in Fig. 8b.
According to Theorem 1, ϵ inﬂu-
ences the accuracy of our PPR approximation. As shown
in Fig. 8b, when ϵ is increased (i.e., the error caused by
BKSVD is larger), the AUC performance of the embedding
decreases, especially on Youtube dataset. Therefore, we set
ϵ to 0.2, which has the same excellent performance as 0.1
but is computationally more eﬃcient.
In Fig. 8c, observe that the AUC of NRP grows signiﬁ-
cantly when we vary ℓ1 from 1 to 15, and keeps stable and
excellent for larger ℓ1 from 15 to 40, which holds for all the
three datasets. Recall that the accuracy of our PPR approx-
imation is aﬀected by ℓ1 as well and when ℓ1 increases, the
approximate PPR scores are more accurate. According to
Fig. 8c, our choice of ℓ1 = 20 is proper and robust.
Fig. 8d shows the AUC of NRP when we vary ℓ2 from 0
to 30. The AUC increases signiﬁcantly when ℓ2 is increased
from 0 to 10, and then keeps stable for larger ℓ2 values,
which is consistent across the three datasets. When ℓ2 = 0,
it is equivalent to disable our reweighting scheme and only
use the conventional PPR for embedding, which is signiﬁ-
cantly inferior to the case that our NRP reweighting scheme
is enabled, e.g., when ℓ2 = 10. Speciﬁcally, on Wiki, the
AUC is increased from 0.78 to 0.91 when ℓ2 is varied from
0 to 10. This validates our insight about the drawback of
vanilla PPR for embeddings and demonstrates the power
of our proposed reweighting scheme. Further, Fig. 8d also
shows that our reweighting scheme converges quickly when
the epochs are increased.
6.
CONCLUSION
This paper presents NRP, a novel, eﬃcient and eﬀective
approach for homogeneous network embedding. NRP con-
structs embedding vectors based on personalized PageRank
values and reweights each node’s embedding vectors based
on an objective function concerning the in-/out- degree of
each node. We show that NRP runs in time almost linear
to the size of the input graph, and that it requires less than
four hours to process a graph with 1.2 billion edges. Exten-
sive experiments on real data also demonstrate that NRP
considerably outperforms the state of the arts in terms of
the accuracy link prediction, graph reconstruction and on
node classiﬁcation tasks.
As for future work, we plan to
study how to extend NRP to handle attributed graphs.
APPENDIX
A Proof of Theorem 1
12


## Page 13


Wiki
Wiki
Blogcatalog
Blogcatalog
Youtube
Youtube
0.6
0.7
0.8
0.9
0.96
0.1
0.3
0.5
0.7
0.9
α
AUC
(a) Varying α
0.7
0.75
0.8
0.85
0.9
0.96
0.1
0.3
0.5
0.7
0.9
ε
AUC
(b) Varying ϵ
0.65
0.7
0.75
0.8
0.85
0.9
0.96
1
2
5
10 15 20 30 40
l1
AUC
(c) Varying ℓ1
0.7
0.75
0.8
0.85
0.9
0.96
0
1
2
5
10 15 20 30
l2
AUC
(d) Varying ℓ2
Figure 8: Link prediction results with varying pa-
rameters (best viewed in color).
Proof. We need the following theorem,
Theorem 2
(Eckart–Young Theorem [17]). Suppose
Ak′ is the rank k′ approximation to A produced by exact
SVD, then
min
rank( b
A)≤k′ ∥A −bA∥2 = ∥A −Ak′∥2 = σk′+1,
(15)
where σk′+1 is the (k′ + 1)-th largest singular value of A.
Recall that X1Y⊤= D−1UΣV⊤, where U, Σ, V are pro-
duced by BKSVD. Then, by Theorem 1 of BKSVD [32] and
Eckart–Young theorem [17], we have
∥A −UΣV⊤∥2 = ∥A −DX1Y⊤∥2 ≤(1 + ϵ)σk′+1,
(16)
where σk′+1 is the k′ + 1 largest singular value of A. Ac-
cording to [17], the following inequalities hold
∥A −DX1Y⊤∥max ≤∥A −DX1Y⊤∥2 ≤(1 + ϵ)σk′+1,
∥A −DX1Y⊤∥1 ≤√n∥A −DX1Y⊤∥2 ≤√n(1 + ϵ)σk′+1,
which indicates that, for any node pair (u, v) ∈V × V ,
|P[u, v] −(X1Y⊤)[u, v]| =
 A[u,v]
d(u) −(X1Y⊤)[u, v]

≤
1
d(u)(1 + ϵ)σk′+1,
(17)
and for any node u ∈V ,
X
u∈V
|P[u, v] −(X1Y⊤)[u, v]| =
X
u∈V

A[u, v]
d(u)
−(X1Y⊤)[u, v]

≤√n(1 + ϵ)σk′+1.
(18)
By Lines 2-5 in Algorithm 1,
XY⊤= α(1 −α)Xℓ1Y⊤= Pℓ1
i=1 Pi−1X1Y⊤.
(19)
By the deﬁnition of Π′ in Eq. (3),
|Π′[u, v] −(XY⊤)[u, v]|
=

ℓ1
X
i=1
α(1 −α)i X
w∈V
Pi−1[u, w] ·

P[w, v] −(XY⊤)[w, v]

(20)
With Eq. (17), (18) and (20), for every node pair (u, v) ∈
V ×V with v ̸= v and every node u ∈V , the follow inequal-
ities hold,
|Π′[u, v] −(XY⊤)[u, v]| ≤σk′+1(1 + ϵ) Pℓ1
i=1 α(1 −α)i.
X
v∈V
|Π′[u, v] −(XY⊤)[u, v]| ≤√nσk′+1(1 + ϵ)
ℓ1
X
i=1
α(1 −α)i.
(21)
In addition, according to Eq. (1) and (3), for every node
pair (u, v) ∈V × V with v ̸= v, we have
|Π[u, v] −Π′[u, v]| ≤P
v∈V |Π[u, v] −Π′[u, v]|
≤1 −Pℓ1
i=0 α(1 −α)i.
(22)
Combining Eq. (21) and (22) obtains the following results,
for every node pair (u, v) ∈V × V with v ̸= v,
Π[u, v] −XY⊤(u, v)

≤
Π[u, v] −Π′[u, v]
 +
Π′[u, v] −(XY⊤)[u, v]

≤(1 + ϵ)σk′+1(1 −α)

1 −(1 −α)ℓ1
+ (1 −α)ℓ1+1,
and for every node u ∈V ,
X
v∈V
Π[u, v] −XY⊤(u, v)

≤
X
v∈V
Π[u, v] −Π′[u, v]
 +
X
v∈V
Π′[u, v] −(XY⊤)[u, v]

≤√n(1 + ϵ)σk′+1(1 −α)

1 −(1 −α)ℓ1
+ (1 −α)ℓ1+1,
which completes our proof.
B Updating Forward Weights
For any node u∗, the formula for updating −→
w u∗is derived
by (i) taking the partial derivative of the objective function
in Eq. (6) with respect to −→
w u∗,
∂O
∂−
→
w u∗= 2
h 
Xu∗P
v̸=u∗←−
w vY⊤
v
2 −→
w u∗
−dout(u∗)Xu∗P
v̸=u∗←−
w vY⊤
v
+ P
v(P
u̸=v,u̸=u∗−→
w uXuY⊤
v ←−
w v)Xu∗Y⊤
v ←−
w v
+ P
v̸=u∗(Xu∗Y⊤
v ←−
w v)2−→
w u∗
−Xu∗P
v din(v)←−
w vY⊤
v + λ−→
w u∗
i
= 2(a′
3 −a′
2 −a′
1) + 2(b′
1 + b′
2 + λ)−→
w u∗,
and then (ii) identifying the value of −→
w u∗that renders the
partial derivative equal to zero. In addition, if the identiﬁed
13


## Page 14


−→
w u∗is smaller than
1
n, then we set it to
1
n instead. Then
the forward weight learning rule is as in Eq. (23):
−→
w u∗= max
 1
n, a′
1 + a′
2 −a′
3
b′
1 + b′
2 + λ

, where
a′
1 =Xu∗
X
v
din(v)←−
w vY⊤
v ,
a′
2 =dout(u∗)Xu∗
X
v̸=u∗
←−
w vY⊤
v ,
a′
3 =
X
v
(
X
u̸=v,u̸=u∗
−→
w uXuY⊤
v ←−
w v)Xu∗Y⊤
v ←−
w v,
b′
1 =
X
v̸=u∗
(Xu∗Y⊤
v ←−
w v)2,
b′
2 =(Xu∗
X
v̸=u∗
←−
w vY⊤
v )2.
(23)
By Eq. (23), each update of −→
w u∗requires computing a′
1, a′
2, a′
3, b′
1
and b′
2, which are similar to the computation of a1, a2, a3, b1
and b2 in Section 4.2. Hence, it takes O(n2k′2) time to up-
date −→
w u∗once, which leads to a total overhead of O(n3k′2)
for updating all −→
w u∗once.
In the following, we present the solution to accelerate
the computation of a′
1, a′
2, a′
3, b′
1, b′
2 for forward weight −→
w u∗.
Since the techniques for updating forward weight −→
w u∗are
similar to that for backward weights, for brevity, we use the
same symbols to represent the intermediate computations of
forward weights as those of backward weights.
Computation of a′
1, a′
2, b′
2. By the deﬁnitions of a1, a2, b2
in Eq. (23),
a′
1 = Xu∗ξ⊤, a′
2 = dout(u∗)Xu∗(χ −←−
w u∗Yu∗)⊤,
and b′
2 =

Xu∗(χ −←−
w u∗Yu∗)⊤2
,
where ξ =
X
v
din(v)←−
w vYv, and χ =
X
v
←−
w vYv.
(24)
Eq. (24) indicates that the a′
1 values of all nodes u∗∈V
share a common ξ, while a′
2 and b′
2 of each node u∗have
χ in common. Observe that both ξ and χ are independent
of any forward weight. Motivated by this, we propose to
ﬁrst compute ξ ∈R1×k′ and χ ∈R1×k′, which takes O(nk′)
time. After that, we can easily derive a′
1, a′
2, and b′
2 for any
node with precomputed ξ and χ. In that case, each update
of a′
1, a′
2, and b′
2 takes only O(k′) time, due to Eq. (24). This
leads to O(nk′) (instead of O(n2k′)) total computation time
of a′
1, a′
2, and b′
2 for all nodes.
Computation of a′
3. Note that
a′
3 = P
v
 P
u −→
w uXuY⊤
v ←−
w v
 ←−
w vXu∗Y⊤
v
−P
v
 −→
w u∗Xu∗Y⊤
v ←−
w v
 ←−
w vXu∗Y⊤
v
−P
v
 −→
w vXvY⊤
v ←−
w v
 ←−
w vXu∗Y⊤
v
+
 −→
w u∗Xu∗Y⊤
u∗←−
w u∗ ←−
w u∗Xu∗Y⊤
u∗,
which can be rewritten as:
a′
3 =ρ1ΛX⊤
u∗−−→
w u∗Xu∗ΛX⊤
u∗−ρ2X⊤
u∗
+ ←−
w 2
u∗

Xu∗Y⊤
u∗
2 −→
w u∗,
where Λ =
X
v
←−
w 2
v(Y⊤
v Yv), ρ1 =
X
u
−→
w uXu,
and ρ2 =
X
v
−→
w v · ←−
w 2
v

XvY⊤
v

Yv

.
(25)
Observe that Λ is independent of any forward weight.
Thus, it can be computed once and reused in the compu-
tation of a′
3 for all nodes. Meanwhile, both ρ1 and ρ2 de-
pendent on all of the foward weights, and hence, cannot be
directly reused if we are to update each foward weight in
turn. However, we note that ρ1 and ρ2 can be incremen-
tally updated after the change of any single forward weight.
Speciﬁcally, suppose that we have computed ρ1 and ρ2 based
on Eq. (25), and then we change the forward weight of u∗
from −→
w ′
u∗as −→
w u∗. In that case, we can update ρ1 and ρ2
as:
ρ1 = ρ1 + (−→
w u∗−−→
w ′
u∗) Xu∗,
ρ2 = ρ2 + (−→
w u∗−−→
w ′
u∗) ←−
w 2
u∗
 Xu∗Y⊤
u∗

Yu∗.
(26)
Each of such updates takes only O(k′) time, since −→
w u∗, −→
w ′
u∗∈
R and Xu∗, Yu∗∈R1×k′.
The initial values of ρ1 and ρ2 can be computed in O(nk′)
time based on Eq. (25), while Λ can be calculated in O(nk′2)
time.
Given Λ, ρ1, and ρ2, we can compute a′
3 for any
node u∗in O(k′2) time based on Eq. (25). Therefore, the
total time required for computing a′
3 for all nodes is O(nk′2),
which is an signiﬁcant reduction from the O(n3k′2) time
required by the naive solution in Equation (23).
Approximation of b1
′. We observe that the value of b′
1
is insigniﬁcant compared to b′
2.
Thus, we propose to ap-
proximate its value instead of deriving it exactly, so as to
reduce computation cost. By the inequality of arithmetic
and geometric means, we have:
1
k′ b′
1 ≤
X
v̸=u∗
←−
w 2
v(
k′
X
r=1
Xu∗[r]2Yv[r]2) ≤b′
1.
(27)
Let φ be a length-k′ vector where the r-th (r ∈[1, k′]) ele-
ment is
φ[r] = P
v ←−
w 2
vYv[r]2.
(28)
We compute φ in O(nk′) time, and then, based on Eq. (27),
we approximate b′
1 for each node in O(k′) time with
b′
1 ≈k′
2
k′
X
r=1
Xu∗[r]2  φ[r] −←−
w 2
u∗Yu∗[r]2
.
(29)
Therefore, the total cost for approximating b′
1 for all nodes
is O(nk′).
Algorithm 4 illustrates the pseudo-code for updating for-
ward weights, which is analogous to Algorithm 2. Based on
the above analysis, it is easy to verify that it has the same
time complexity and space overhead as Algorithm 2.
14


## Page 15


Algorithm 4: updateFwdWeights
Input: G, k′, −
→
w, ←
−
w, X, Y.
Output: −
→
w
1 Compute ξ, χ, ρ1, ρ2, Λ based on Eq. (24), (25);
2 for r ←1 to k′ do
3
φ[r] = P
v ←
−
w 2
vYv[r]2;
4 for u∗∈V in random order do
5
Compute a′
1, a′
2, a′
3, b′
1, b′
2 by Eq. (24), (25), and (29);
6
−
→
w ′
u∗= −
→
w u∗;
7
−
→
w u∗= max
n
1
n, a′
1+a′
2−a′
3
b′
1+b′
2+λ
o
;
8
ρ1 = ρ1 +
 −
→
w u∗−−
→
w ′
u∗

Xu∗;
9
ρ2 = ρ2 +
 −
→
w u∗−−
→
w ′
u∗
 ←
−
w 2
u∗
 Xu∗Y⊤
u∗

Yu∗
10 return −
→
w;
Name
|V |
|E|
|Eold|
|Enew|
Type
VK
78.59K
5.35M
2.68M
2.67M
undirected
Digg
279.63K
1.73M
1.03M
701.59K
directed
Table 4: Dataset statistics (K = 103, M = 106).
VERSE
VERSE
GA
GA
RandNE
RandNE
AROPE
AROPE
APP
APP
NRP
NRP
ProNE
ProNE
node2vec
node2vec
PBG
PBG
STRAP
STRAP
DRNE
DRNE
NetHiex
NetHiex
DeepWalk
DeepWalk
LINE
LINE
GraphGAN
GraphGAN
NetSMF
NetSMF
GraphWave
GraphWave
DNGR
DNGR
ApproxPPR
ApproxPPR
RaRE
RaRE
0.75
0.8
0.85
0.9
0.95
16
32
64
128
256
k
AUC
(a) VK
0.54
0.56
0.58
0.6
0.62
16
32
64
128
256
k
AUC
(b) Digg
Figure 9: Link prediction performance on dynamic
graphs (best viewed in color).
C Additional Experiments
Link Prediction on Evolving Grpahs.
In this set of
experiments, we evaluate the link performance of all meth-
ods on real-world datasets with real new links, i.e., evolv-
ing graphs.
Table 4 shows the statistics of the datasets.
Speciﬁcally, VK [45] and Digg [22] are two real-world so-
cial networks, where each node represents a user and a link
represents the friendship or following relationship. For VK,
|Eold| denotes the social network snapshot of VK in 2016
and |Enew| is the set of new links (i.e., friendships) in 2017.
In terms of Digg, |Eold| is the snapshot of the social network
in 2008 and |Enew| consists of new links (i.e., following rela-
tionships) in 2009. We run all network embedding methods
on |Eold| and and then employ the learned embeddings to
predict the new links |Enew|. Figure 9 plots the AUC results
of all methods on VK and Digg. It can be observed that
NRP achieves similar performance as PPR-based methods
STRAP, VERSE and APP on undirected graph VK. On di-
rected graph Digg, NRP outperforms all competitors by at
least a large margin of 0.7%. The experimental results indi-
cate the eﬀectiveness of NRP in predicting ”real new links”
on real-world datasets.
Scalability Tests.
In this set of experiments, we verify
the scalability of NRP. Following prior work [65,66], we use
100
200
300
400
2e+5
4e+5
6e+5
8e+5
1e+6
the number of nodes
running time (second)
(a) Varying the number of
nodes
500
800
1100
1400
1800
2e+7
4e+7
6e+7
8e+7
1e+8
the number of edges
running time (second)
(b) Varying the number of
edges
Figure 10: Scalability tests.
synthetic graphs of diﬀerent sizes generated by the Erdos
Renyi random graph model [15]. We run NRP on these syn-
thetic graphs with default parameter settings described in
Section 5.1. We record the running time when ﬁxing the
number of nodes (as 106) or ﬁxing the number of edges (as
107) while varying the other, i.e., the number of edges in
{2 × 107, 4 × 107, 6 × 107, 8 × 107, 1 × 108} and the number
of nodes in {2 × 105, 4 × 105, 6 × 105, 8 × 105, 1 × 106}, re-
spectively. Figure 10a and 10b plot the running time of NRP
when varying the number of nodes and the number of edges,
respectively. It can be observed that the running time grows
linearly with the number of nodes and the number of edges,
respectively, conﬁrming the time complexity of NRP as well
as verying the scalability of NRP.
Running Time with Varying Parameters. Figure 11a-
11d depict the results when varying ℓ1, ℓ2, α and ϵ on Wiki,
Blogcatalog, Youtube and Tweibo, respectively. We can ob-
serve that the running time of NRP grows when we increase
the values of ℓ1, ℓ2 and ϵ but remain almost stable when in-
creases α, which accords with the time complexity of NRP,
i.e., O
  log n
ϵ
+ ℓ1

mk′ + log n
ϵ
nk′2 + ℓ2nk′2
.
Especially,
Figre 11b shows that ℓ2 has greater impact on the running
time compared with other parameters.
7.
REFERENCES
[1] S. Abu-El-Haija, B. Perozzi, R. Al-Rfou, and A. A.
Alemi. Watch your step: Learning node embeddings
via graph attention. In NeurIPS, pages 9180–9190,
2018.
[2] A. Ahmed, N. Shervashidze, S. Narayanamurthy,
V. Josifovski, and A. J. Smola. Distributed large-scale
natural graph factorization. In WWW, pages 37–48,
2013.
[3] L. Backstrom and J. Leskovec. Supervised random
walks: Predicting and recommending links in social
networks. In WSDM, pages 635–644, 2011.
[4] M. J. Brzozowski and D. M. Romero. Who should i
follow? recommending people in directed social
networks. In Fifth International AAAI Conference on
Weblogs and Social Media, 2011.
[5] H. Cai, V. W. Zheng, and K. C. Chang. A
comprehensive survey of graph embedding: Problems,
techniques, and applications. TKDE, 30(9):1616–1637,
2018.
[6] S. Cao, W. Lu, and Q. Xu. Grarep: Learning graph
representations with global structural information. In
CIKM, pages 891–900, 2015.
15


## Page 16


Tweibo
Tweibo
Youtube
Youtube
Blogcatalog
Blogcatalog
Wiki
Wiki
100
101
102
103
1
2
5
10 15 20 30 40
l1
running time (second)
(a) Varying ℓ1
100
101
102
103
0
1
2
5
10 15 20 30
l2
running time (second)
(b) Varying ℓ2
100
101
102
103
0.1
0.3
0.5
0.7
0.9
α
running time (second)
(c) Varying α
100
101
102
103
0.1
0.3
0.5
0.7
0.9
ε
running time (second)
(d) Varying ϵ
Figure 11: Running time with varying parameters (best viewed in color).
[7] S. Cao, W. Lu, and Q. Xu. Deep neural networks for
learning graph representations. In AAAI, 2016.
[8] H. Chen, B. Perozzi, Y. Hu, and S. Skiena. HARP:
hierarchical representation learning for networks. In
AAAI, 2018.
[9] H. Chen, H. Yin, T. Chen, Q. V. H. Nguyen, W.-C.
Peng, and X. Li. Exploiting centrality information
with graph convolutions for network representation
learning. In ICDE, pages 590–601, 2019.
[10] K. L. Clarkson and D. P. Woodruﬀ. Low-rank
approximation and regression in input sparsity time.
STOC, pages 81–90, 2013.
[11] P. Cui, X. Wang, J. Pei, and W. Zhu. A survey on
network embedding. TKDE, 31(5):833–852, 2018.
[12] Q. Dai, Q. Li, J. Tang, and D. Wang. Adversarial
network embedding. In AAAI, 2018.
[13] Q. Dai, X. Shen, L. Zhang, Q. Li, and D. Wang.
Adversarial training methods for network embedding.
In WWW, pages 329–339, 2019.
[14] C. Donnat, M. Zitnik, D. Hallac, and J. Leskovec.
Learning structural node embeddings via diﬀusion
wavelets. In KDD, pages 1320–1329, 2018.
[15] L. Erd˝os, A. Knowles, H.-T. Yau, J. Yin, et al.
Spectral statistics of erd˝os–r´enyi graphs i: local
semicircle law. The Annals of Probability, 2013.
[16] H. Gao and H. Huang. Self-paced network embedding.
In KDD, pages 1406–1415, 2018.
[17] G. H. Golub and C. F. Van Loan. Matrix
computations. 1996. Johns Hopkins University, Press,
Baltimore, MD, USA, 1996.
[18] A. Grover and J. Leskovec. node2vec: Scalable feature
learning for networks. In KDD, pages 855–864, 2016.
[19] Y. Gu, Y. Sun, Y. Li, and Y. Yang. Rare: Social rank
regulated large-scale network embedding. In WWW,
pages 359–368, 2018.
[20] Y. Gu, Y. Sun, Y. Li, and Y. Yang. Rare: Social rank
regulated large-scale network embedding. In WWW,
pages 359–368, 2018.
[21] N. Halko, P.-G. Martinsson, and J. A. Tropp. Finding
structure with randomness: Probabilistic algorithms
for constructing approximate matrix decompositions.
SIAM review, 53(2):217–288, 2011.
[22] T. Hogg and K. Lerman. Social dynamics of digg. EPJ
Data Science, 2012.
[23] G. Jeh and J. Widom. Scaling personalized web
search. In WWW, pages 271–279, 2003.
[24] Kaggle, 2012.
https://www.kaggle.com/c/kddcup2012-track1.
[25] T. N. Kipf and M. Welling. Variational graph
auto-encoders. NeurIPS Workshop, 2016.
[26] T. N. Kipf and M. Welling. Semi-supervised
classiﬁcation with graph convolutional networks. In
ICLR, 2017.
[27] H. Kwak, C. Lee, H. Park, and S. Moon. What is
twitter, a social network or a news media? In WWW,
pages 591–600, 2010.
[28] Y.-A. Lai, C.-C. Hsu, W. Chen, M.-Y. Yeh, and S.-D.
Lin. Prune: Preserving proximity and global ranking
for network embedding. In NeurIPS, pages 5257–5266,
2017.
[29] A. Lerer, L. Wu, J. Shen, T. Lacroix, L. Wehrstedt,
A. Bose, and A. Peysakhovich. Pytorch-biggraph: A
large-scale graph embedding system. In SysML, 2019.
[30] X. Liu, T. Murata, K.-S. Kim, C. Kotarasu, and
C. Zhuang. A general view for network embedding as
matrix factorization. In WSDM, pages 375–383, 2019.
[31] J. Ma, P. Cui, X. Wang, and W. Zhu. Hierarchical
taxonomy aware network embedding. In KDD, pages
1920–1929, 2018.
[32] C. Musco and C. Musco. Randomized block krylov
methods for stronger and faster approximate singular
value decomposition. In NeurIPS, pages 1396–1404,
2015.
[33] M. Ou, P. Cui, J. Pei, Z. Zhang, and W. Zhu.
Asymmetric transitivity preserving graph embedding.
In KDD, pages 1105–1114, 2016.
[34] B. Perozzi, R. Al-Rfou, and S. Skiena. Deepwalk:
online learning of social representations. In KDD,
pages 701–710, 2014.
[35] B. Perozzi, V. Kulkarni, H. Chen, and S. Skiena. Don’t
walk, skip!: Online learning of multi-scale network
embeddings. In ASONAM, pages 258–265, 2017.
[36] J. Qiu, Y. Dong, H. Ma, J. Li, C. Wang, K. Wang,
and J. Tang. Netsmf: Large-scale network embedding
as sparse matrix factorization. In WWW, pages
1509–1520, 2019.
[37] J. Qiu, Y. Dong, H. Ma, J. Li, K. Wang, and J. Tang.
Network embedding as matrix factorization: Unifying
deepwalk, line, pte, and node2vec. In WSDM, pages
459–467, 2018.
[38] P. Radivojac, W. T. Cark, T. R. Oron, A. M. Schnoes,
T. Wittkop, A. Sokolov, K. Graim, C. Funk,
K. Verspoor, and et. al. A large-scale evaluation of
16


## Page 17


computational protein function prediction. Nature
methods, 10(3):221, 2013.
[39] L. F. R. Ribeiro, P. H. P. Saverese, and D. R.
Figueiredo. struc2vec: Learning node representations
from structural identity. In KDD, pages 385–394, 2017.
[40] T. Sarlos. Improved approximation algorithms for
large matrices via random projections. In FOCS,
pages 143–152, 2006.
[41] J. Shi, R. Yang, T. Jin, X. Xiao, and Y. Yang.
Realtime top-k personalized pagerank over large
graphs on gpus. PVLDB, 13(1):15–28, 2019.
[42] J. Tang, M. Qu, M. Wang, M. Zhang, J. Yan, and
Q. Mei. LINE: large-scale information network
embedding. In WWW, pages 1067–1077, 2015.
[43] L. Tang and H. Liu. Leveraging social media networks
for classiﬁcation. DMKD, 23(3):447–478, 2011.
[44] R. Trivedi, B. Sisman, X. L. Dong, C. Faloutsos,
J. Ma, and H. Zha. Linknbed: Multi-graph
representation learning with entity linkage. In ACL,
pages 252–262, 2018.
[45] A. Tsitsulin, D. Mottin, P. Karras, and E. M¨uller.
Verse: Versatile graph embeddings from similarity
measures. In WWW, pages 539–548, 2018.
[46] K. Tu, P. Cui, X. Wang, P. S. Yu, and W. Zhu. Deep
recursive network embedding with regular equivalence.
In KDD, pages 2357–2366, 2018.
[47] D. Wang, P. Cui, and W. Zhu. Structural deep
network embedding. In KDD, pages 1225–1234, 2016.
[48] H. Wang, J. Wang, J. Wang, M. Zhao, W. Zhang,
F. Zhang, X. Xing, and M. Guo. Graphgan: Graph
representation learning with generative adversarial
nets. In AAAI, 2018.
[49] J. Wang, P. Huang, H. Zhao, Z. Zhang, B. Zhao, and
D. L. Lee. Billion-scale commodity embedding for
e-commerce recommendation in alibaba. In KDD,
pages 839–848, 2018.
[50] Q. Wang, S. Wang, M. Gong, and Y. Wu. Feature
hashing for network representation learning. In IJCAI,
pages 2812–2818, 2018.
[51] R. Wang, S. Wang, and X. Zhou. Parallelizing
approximate single-source personalized pagerank
queries on shared memory. VLDBJ, 28(6):923–940,
2019.
[52] S. Wang, Y. Tang, X. Xiao, Y. Yang, and Z. Li.
Hubppr: Eﬀective indexing for approximate
personalized pagerank. PVLDB, 10(3):205–216, 2016.
[53] S. Wang, R. Yang, R. Wang, X. Xiao, Z. Wei, W. Lin,
Y. Yang, and N. Tang. Eﬃcient algorithms for
approximate single-source personalized pagerank
queries. TODS, 44(4):18, 2019.
[54] S. Wang, R. Yang, X. Xiao, Z. Wei, and Y. Yang.
FORA: simple and eﬀective approximate single-source
personalized pagerank. In KDD, pages 505–514, 2017.
[55] X. Wang, P. Cui, J. Wang, J. Pei, W. Zhu, and
S. Yang. Community preserving network embedding.
In AAAI, 2017.
[56] Z. Wei, X. He, X. Xiao, S. Wang, S. Shang, and
J. Wen. Topppr: Top-k personalized pagerank queries
with precision guarantees on large graphs. In
SIGMOD, pages 441–456, 2018.
[57] S. J. Wright. Coordinate descent algorithms.
Mathematical Programming, 2015.
[58] L. Y. Wu, A. Fisch, S. Chopra, K. Adams, A. Bordes,
and J. Weston. Starspace: Embed all the things! In
AAAI, 2018.
[59] C. Yang, M. Sun, Z. Liu, and C. Tu. Fast network
embedding enhancement via high order proximity
approximation. In IJCAI, pages 3894–3900, 2017.
[60] J. Yang and J. Leskovec. Deﬁning and evaluating
network communities based on ground-truth. KAIS,
42(1):181–213, 2015.
[61] Y. Yin and Z. Wei. Scalable graph embeddings via
sparse transpose proximities. In KDD, 2019.
[62] W. Yu, C. Zheng, W. Cheng, C. C. Aggarwal, D. Song,
B. Zong, H. Chen, and W. Wang. Learning deep
network representations with adversarially regularized
autoencoders. In KDD, pages 2663–2671, 2018.
[63] D. Zhang, J. Yin, X. Zhu, and C. Zhang. Network
representation learning: A survey. IEEE Trans. Big
Data, 2018.
[64] J. Zhang, Y. Dong, Y. Wang, J. Tang, and M. Ding.
Prone: Fast and scalable network representation
learning. In IJCAI, pages 4278–4284, 2019.
[65] Z. Zhang, P. Cui, H. Li, X. Wang, and W. Zhu.
Billion-scale network embedding with iterative
random projection. In ICDM, pages 787–796, 2018.
[66] Z. Zhang, P. Cui, X. Wang, J. Pei, X. Yao, and
W. Zhu. Arbitrary-order proximity preserved network
embedding. In KDD, pages 2778–2786, 2018.
[67] C. Zhou, Y. Liu, X. Liu, Z. Liu, and J. Gao. Scalable
graph embedding for asymmetric proximity. In AAAI,
2017.
[68] D. Zhu, P. Cui, D. Wang, and W. Zhu. Deep
variational network embedding in wasserstein space.
In KDD, pages 2827–2836, 2018.
[69] Z. Zhu, S. Xu, M. Qu, and J. Tang. Graphvite: A
high-performance cpu-gpu hybrid system for node
embedding. In WWW, pages 2494–2504, 2019.
17

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1906_06826v6_homogeneous_network_embedding_for_massive_graphs_via_reweighted_personalized_pag
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1906_06826V6_HOMOGENEOUS_NETWORK_EMBEDDING_FOR_MASSIVE_GRAPHS_VIA_REWEIGHTED_PERSONALIZED_PAG.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

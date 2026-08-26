---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1905.00566v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1905.00566v1_Graph_Coloring_via_Degeneracy_in_Streaming_and_Other_Space-Conscious_Models

> Source: 1905.00566v1_Graph_Coloring_via_Degeneracy_in_Streaming_and_Other_Space-Conscious_Models.pdf

> Pages: 26

---


## Page 1


Graph Coloring via Degeneracy in Streaming and Other
Space-Conscious Models
Suman K. Bera∗
Amit Chakrabarti∗
Prantar Ghosh∗
May 3, 2019
Abstract
We study the problem of coloring a given graph using a small number of colors in several well-
established models of computation for big data. These include the data streaming model, the general
graph query model, the massively parallel communication (MPC) model, and the CONGESTED-CLIQUE
and the LOCAL models of distributed computation. On the one hand, we give algorithms with sublinear
complexity, for the appropriate notion of complexity in each of these models. Our algorithms color a
graph G using about κ(G) colors, where κ(G) is the degeneracy of G: this parameter is closely related to
the arboricity α(G). As a function of κ(G) alone, our results are close to best possible, since the optimal
number of colors is κ(G) + 1.
On the other hand, we establish certain lower bounds indicating that sublinear algorithms probably
cannot go much further. In particular, we prove that any randomized coloring algorithm that uses at most
κ(G) + 1 colors would require Ω(n2) storage in the one pass streaming model, and Ω(n2) many queries in
the general graph query model, where n is the number of vertices in the graph. These lower bounds hold
even when the value of κ(G) is known in advance; at the same time, our upper bounds do not require κ(G)
to be given in advance.
1
Introduction
Graph coloring is a fundamental topic in combinatorics and the corresponding algorithmic problem of
coloring an input graph with few colors is a basic and heavily studied problem in computer science. It has
numerous applications including in scheduling [TZP18,LS86,Lei79], air traﬃc ﬂow management [BB04],
frequency assignment in wireless networks [BB06,PL96], register allocation [Cha82,CH90,CAC+81]. More
recently, vertex coloring has been used to compute seed vertices in social networks that are then expanded to
detect community structures in the network [MOT14].
Given an n-vertex graph G = (V, E), the task is to assign colors to the vertices in V so that no two adjacent
vertices get the same color. Doing so with the minimum possible number of colors—called the chromatic
number, χ(G)—is famously hard: it is NP-hard to even approximate χ(G) to a factor of n1−ε for any constant
ε > 0 [FK96,Zuc06,KP06]. In the face of this hardness, it is algorithmically interesting to color G with a
possibly suboptimal number of colors depending upon tractable parameters of G. One such simple parameter
is ∆, the maximum degree: a trivial greedy algorithm colors G with ∆+ 1 colors.
We study graph coloring in a number of space-constrained and data-access-constrained settings, including
the data streaming model and certain distributed computing models. In such settings, ﬁnding a coloring with
“about ∆” colors is a fairly nontrivial problem that has been studied from various angles in a ﬂurry of research
over the last decade [ACK19,BCHN18,HSS16,CLP18,PS18,Bar16]. In a recent breakthrough (awarded Best
∗Department of Computer Science, Dartmouth College. Supported in part by NSF under Award CCF-1650992.
1
arXiv:1905.00566v1  [cs.DS]  2 May 2019


## Page 2


Paper at SODA 2019), Assadi, Chen, and Khanna [ACK19] gave sublinear algorithms for (∆+ 1)-coloring an
input graph in such models.
In this work, we focus on colorings that use “about κ” colors, where κ = κ(G) is the degeneracy of G, a
parameter that improves upon ∆. It is deﬁned as follows: κ = min{k : every induced subgraph of G has a
vertex of degree at most k}. Clearly, κ ⩽∆. There is a simple greedy algorithm that runs in linear time and
produces (κ + 1)-coloring; see Section 2. However, just as before, when processing a massive graph under
the constraints of either the space-bounded streaming model or certain distributed computing models, the
inherently sequential nature of the greedy algorithm makes it infeasible.
1.1
Our Results and Techniques
We obtain a number of algorithmic results, as well as several lower bound results.
Algorithms. We give new graph coloring algorithms, parametrized by κ, in the following models: (1) the
data streaming model, where the input is a stream of edge insertions and deletions (i.e., a dynamic graph
stream) resulting in the eventual graph to be colored and we are limited to a work space of e
O(n) bits1, the
so-called semi-streaming setting [FKM+05]; (2) the general graph query model [Gol17], where we may
access the graph using only neighbor queries (what is the ith neighbor of x?) and pair queries (are x and
y adjacent?); (3) the massively parallel communication (MPC) model, where each of a large number of
memory-limited processors holds a sublinear-sized portion of the input data and computation proceeds
using rounds of communication; (4) the congested clique model of distributed computation, where there
is one processor per vertex holding that vertex’s neighborhood information and each round allows each
processor to communicate O(log n) bits to a speciﬁc other processor; and (5) the LOCAL model of distributed
computation, where there is one processor per vertex holding that vertex’s neighborhood information and
each round allows each processor to send an arbitrary amount of information to all its neighbors.
Model
Number of Colors
Complexity Parameters
Source
Streaming
∆+ 1
e
O(n) space,
e
O(n
√
∆) post-processing time
[ACK19]
(one pass)
κ + o(κ)
e
O(n) space,
e
O(n) post-processing time
this paper
Query
∆+ 1
e
O(n3/2) queries
[ACK19]
κ + o(κ)
e
O(n3/2) queries
this paper
MPC
∆+ 1
O(1) rounds,
O(n log3 n) bits per processor
[ACK19]
κ + o(κ)
O(1) rounds,
O(n log2 n) bits per processor
this paper
Congested Clique
∆+ 1
O(1) rounds
[CFG+18]
κ + o(κ)⋆
O(1) rounds
this paper
LOCAL
O(αn1/k)
O(k) rounds,
for k ∈ω(log log n), O(
p
log n)
[KP11]
O(αn1/k log n)
O(k) rounds,
for k ∈ω(
p
log n), o(log n)
this paper
Table 1: Summary of our algorithmic results and basic comparison with most related previous work. In the result marked
(⋆), we require that κ = ω(log2 n). In the ﬁrst two results, the number of colors can be improved to min{∆+ 1, κ + o(κ)}
by running our algorithm alongside that of [ACK19]; in the streaming setting, this would require knowing ∆in advance.
Table 1 summarizes our algorithmic results and provides, in each case, a basic comparison with the most
related result from prior work; more details appear in Section 1.2. As we have noted, κ ⩽∆in every case;
1The e
O(·) notation hides factors polylogarithmic in n.
2


## Page 3


indeed, κ could be arbitrarily better than ∆as shown by the example of a star graph, where κ = 1 whereas
∆= n −1. From a practical standpoint, it is notable that in many real-world large graphs drawn from various
application domains—such as social networks, web graphs, and biological networks—the parameter κ is often
signiﬁcantly smaller than ∆. See Table 2 for some concrete numbers. That said, κ + o(κ) is mathematically
incomparable with ∆+ 1.
Graph Name
|V|
|E|
∆
κ
soc-friendster
66M
2B
5K
305
fb-uci-uni
59M
92M
5K
17
soc-livejournal
4M
28M
3K
214
soc-orkut
3M
106M
27K
231
web-baidu-baike
2M
18M
98K
83
web-hudong
2M
15M
62K
529
web-wikipedia2009
2M
5M
3K
67
web-google
916K
5M
6K
65
bio-mouse-gene
43K
14M
8K
1K
bio-human-gene1
22K
12M
8K
2K
bio-human-gene2
14K
9M
7K
2K
bio-WormNet-v3
16K
763K
1K
165
Table 2: Statistics of several large real-world graphs taken from the application domains of social networks, web graphs,
and biological networks, showing that the degeneracy, κ, is often signiﬁcantly smaller than the maximum degree, ∆.
Source: http://networkrepository.com [RA15].
The parameter κ is also closely related to the arboricity α = α(G), deﬁned as the minimum number of
forests into which the edges of G can be partitioned. It is an easy exercise to show that α ⩽κ ⩽2α −1.
Perhaps even more than these results, our key contribution is a conceptual idea and a corresponding
technical lemma underlying all our algorithms. We show that every graph admits a “small” sized low
degeneracy partition (LDP), which is a partition of its vertex set into “few” blocks such that the subgraph
induced by each block has low degeneracy, roughly logarithmic in n. Moreover, such an LDP can be computed
by a very simple and distributed randomized algorithm: for each vertex, choose a “color” independently and
uniformly at random from a suitable-sized palette (this is not to be confused with the eventual graph coloring
we seek; this random assignment is most probably not a proper coloring of the graph). The resulting color
classes deﬁne the blocks of such a partition, with high probability. Theorem 3.1, the LDP Theorem, makes
this precise.
Given an LDP, a generic graph coloring algorithm is to run the aforementioned minimum-degree-based
greedy algorithm on each block, using distinct palettes for the distinct blocks. We obtain algorithms achieving
our claimed results by suitably implementing this generic algorithm in each computational model.
Lower Bounds.
Recall that a graph with degeneracy κ admits a proper (κ + 1)-coloring. As Table 1
makes clear, there are several space-conscious (∆+ 1)-coloring algorithms known; perhaps we could aim
for improved algorithms that provide (κ + 1)-colorings? We prove that this is not possible in sublinear
space in either the streaming or the query model. In fact, our lower bounds prove more. We show that
distinguishing n-vertex graphs of degeneracy κ from those with chromatic number κ + 2 requires Ω(n2) space
in the streaming model and Ω(n2) queries in the general graph query model. This shows that it is hard to
produce a (κ + 1)-coloring and in fact even to determine the value of κ. These results generalize to the
problems of producing a (κ + λ)-coloring or estimating the degeneracy up to ±λ; the corresponding lower
bounds are Ω(n2/λ2). Furthermore, the streaming lower bounds hold even in the insertion-only model, where
the input stream is simply a listing of the graph’s edges in some order; compare this with our upper bound,
which holds even for dynamic graph streams.
3


## Page 4


A possible criticism of the above lower bounds for coloring is that they seem to depend on it being hard to
estimate the degeneracy κ. Perhaps the coloring problem could become easier if κ was given to the algorithm
in advance? We prove two more lower bounds showing that this is not so: the same Ω(n2/λ2) bounds hold
even with κ known a priori.
Most of our streaming lower bounds use reductions from the index problem in communication complexity
(a standard technique), via a novel gadget that we develop here; one bound uses a reduction from a variant of
disjointness. Our query lower bounds use a related gadget and reductions from basic problems in Boolean
decision tree complexity.
We conclude the paper with a “combinatorial” lower bound that addresses a potential criticism of our
main algorithmic technique: the LDP. Perhaps a more sophisticated graph-theoretic result, such as the Palette
Sparsiﬁcation Theorem of Assadi et al. (see below), could improve the quality of the colorings obtained? We
prove that this is not so: there is no analogous theorem for colorings with “about κ” colors.
1.2
Related Work and Comparisons
Streaming and Query Models. The work closest to ours in spirit is the recent breakthrough of Assadi,
Chen, and Khanna [ACK19]: they give a one-pass streaming (∆+ 1)-coloring algorithm that uses e
O(n) space
(i.e., is semi-streaming) and works on dynamic graph streams. Their algorithm exploits a key structural result
that they establish: choosing a random O(log n)-sized palette from {1, . . . , ∆+ 1} for each vertex allows a
compatible list coloring. They call this the Palette Sparsiﬁcation Theorem. Their algorithm processes each
stream update quickly, but then spends e
O(n
√
∆) time in post-processing. Our algorithm is similarly quick
with the stream updates and has a faster e
O(n)-time post-processing step. Further, our algorithm is “truly
one-pass” in that it does not require foreknowledge of κ or any other parameter of the input graph, whereas
the Assadi et al. algorithm needs to know the precise value of ∆before seeing the stream.
In the same paper, Assadi et al. also consider the graph coloring problem in the query model. They give a
(∆+ 1)-coloring algorithm that makes e
O(n3/2) queries, followed by a fairly elaborate computation that runs
in e
O(n3/2) time and space. Our algorithm has the same complexity parameters and is arguably much simpler:
its post-processing is just the straightforward greedy oﬄine algorithm for (κ + 1)-coloring.
Another recent work on coloring in the streaming model is Radhakrishnan et al. [RSV15], which studies
the problem of 2-coloring an n-uniform hypergraph. In the query model, there are a number of works studying
basic graph problems [GR08,PR07,CRT05] but, to the best of our knowledge, Assadi et al. were the ﬁrst
to study graph coloring in this sense. Also, to the best of our knowledge, there was no previously known
algorithm for O(α)-coloring in a semi-streaming setting, whereas here we obtain (κ + o(κ))-colorings; recall
the bound κ ⩽2α −1.
MPC and Congested Clique Models. The MapReduce framework [DG04] is extensively used in distributed
computing to analyze and process massive data sets. Beame, Koutris, and Suciu [BKS17] deﬁned the
Massively Parallel Communication (MPC) model to abstract out key theoretical features of MapReduce;
it has since become a widely used setting for designing and analyzing big data algorithms, especially for
graph problems. In this model, an input of size m is distributed among p ≈m/S processors, each of which is
computationally unbounded and restricted to S bits of space. The processors operate in synchronous rounds;
in each round, a processor may communicate with all others, subject to the space constraint. The focus is on
using a very small number of rounds.
Another well-studied model for distributed graph algorithms is Congested Clique [LPPP05], where there
are n nodes, each holding the local neighborhood information for one of the n vertices of the input graph. The
nodes communicate in synchronous rounds; in a round, every pair of processors may communicate, but each
message is restricted to O(log n) bits. Behnezhad et al. [BDH18] show that Congested Clique is equivalent to
4


## Page 5


the so-called “semi-MPC model,” deﬁned as MPC with O(n log n) bits of memory per machine: there are
simulations in both directions preserving the round complexity.
Graph coloring has been studied in these models before. Harvey et al. [HLL18] gave a (∆+o(∆))-coloring
algorithm in the MapReduce model; it can be simulated in MPC using O(1) rounds and O(n1+c) space per
machine for some constant c > 0. Parter [Par18] gave a Congested Clique algorithm for (∆+ 1)-coloring
using O(log log ∆· log⋆∆) rounds; Parter and Su [PS18] improved this to O(log⋆∆). The aforementioned
paper of Assadi et al. [ACK19] gives an MPC algorithm for (∆+1)-coloring using O(1)-round and O(n log3 n)
bits of space per machine. Because this space usage is ω(n log n), the equivalence result of Behnezad et
al. [BDH18] does not apply and this doesn’t lead to an O(1)-round Congested Clique algorithm. In contrast,
our MPC algorithm uses only O(n log n) bits of space per machine for graphs with degeneracy ω(log2 n), and
therefore leads to such a Congested Clique algorithm. Chang et al. [CFG+18] have recently designed two
(∆+ 1) list-coloring algorithms: an O(1)-round Congested Clique algorithm, and an O(
p
log log n)-round
MPC algorithm with o(n) space per machine and e
O(m) space in total. To the best of our knowledge, no
O(α)-coloring algorithm was previously known, in either the MPC or the Congested Clique model.
The LOCAL Model. The LOCAL model of distributed computing is “orthogonal” to Congested Clique:
the input setup is similar but, during computation, each node may only communicate with its neighbors in
the input graph, though it may send an arbitrarily long message. As before, the focus is on minimizing the
number of rounds (a.k.a., time). There is a deep body of work on graph coloring in this model. Indeed, graph
coloring is one of the most central “symmetry breaking” problems in distributed computing. We refer the
reader to the monograph by Barenboim and Elkin [BE13] for an excellent overview of the state of the art.
Here, we shall brieﬂy discuss only a few results closely related to our contribution.
There is a long line of work on fast (∆+1)-coloring in the LOCAL model, in the deterministic as well as the
randomized setting [PS96,Bar16,FHK16,Lub86,Joh99,ABI86,SW10,BEPS16] culminating in sublogarithmic
time solutions due to Harris [HSS16] and Chang et al. [CLP18]. Barenboim and Elkin [BE10,BE11] studied
fast distributed coloring algorithms that may use far fewer than ∆colors: in particular, they gave algorithms
that use O(α) colors and run in O(αε log n) time on graphs with arboricity at most α. Recall again that
κ ⩽2α −1, so that a 2α-coloring always exists. They also gave a faster O(log n)-time algorithm using O(α2)
colors. Further, they gave a family of algorithms that produce an O(tα2)-coloring in O(logt n + log⋆n), for
every t such that 2 ⩽t ⩽O( √n/α). Our algorithm for the LOCAL model builds on this latter result.
Kothapalli and Pemmaraju [KP11] focused on arboricity-dependant coloring using very few rounds.
They gave a randomized O(k)-round algorithm that uses O(αn1/k) colors for 2 log log n ⩽k ⩽
p
log n and
O(α1+1/kn1/k+3/k22−2k) colors for k < 2 log log n. We extend their result to the range k ∈ω(
p
log n), o(log n),
using O(αn1/k log n) colors.
Ghaﬀari and Lymouri [GL17] gave a randomized O(α)-coloring algorithm that runs in time O(log n ·
min{log log n, log α}) as well as an O(log n)-time algorithm using min{(2+ε)α+O(log n log log n), O(α log α)}
colors, for any constant ε > 0. However, their technique does not yield a sublogarithmic time algorithm, even
at the cost of a larger palette.
The LDP Technique. As mentioned earlier, our algorithmic results rely on the concept of a low degeneracy
partition (LDP) that we introduce in this work. Some relatives of this idea have been considered before.
Speciﬁcally, Barenboim and Elkin [BE13] deﬁne a d-defective (resp. b-arbdefective) c-coloring to be a vertex
coloring using palette [c] such that every color class induces a subgraph with maximum degree at most d
(resp. arboricity at most b). Obtaining such improper colorings is a useful ﬁrst step towards obtaining proper
colorings. They give deterministic algorithms to obtain good arbdefective colorings [BE11]. However, their
algorithms are elaborate and are based on construction of low outdegree acyclic partial orientations of the
graph’s edges: an expensive step in our space-conscious models.
Elsewhere (Theorem 10.5 of Barenboim and Elkin [BE13]), they note that a useful defective (not
arbdefective) coloring is easily obtained by randomly picking a color for each vertex; this is then useful for
5


## Page 6


computing an O(∆)-coloring.
Our LDP technique can be seen as a simple randomized method for producing an arbdefective coloring.
Crucially, we parametrize our result using degeneracy instead of arboricity and we give sharp—not just
asymptotic—bounds on the degeneracy of each color class.
Other Related Work. Other work considers coloring in the setting of dynamic graph algorithms: edges
are inserted and deleted over time and the goal is to maintain a valid vertex coloring of the graph that must
be updated quickly after each modiﬁcation. Unlike in the streaming setting, there is no space restriction.
Bhattacharya et al. [BCHN18] gave a randomized algorithm that maintains a (∆+ 1)-coloring with O(log ∆)
expected amortized update time and a deterministic algorithm that maintains a (∆+ o(∆))-coloring with
O(polylog ∆) amortized update time. Barba et al. [BCK+17] gave tradeoﬀs between the number of colors
used and update time. However, the techniques in these works do not seem to apply in the streaming setting
due to fundamental diﬀerences in the models.
Estimating the arboricity of a graph in the streaming model is a well studied problem. McGregor et
al. [MTVV15] gave a one pass (1 + ε)-approximation algorithm to estimate the arboricity of graph using e
O(n)
space. Bahmani et al. [BKV12] gave a matching lower bound. Our lower bounds for estimating degeneracy
are quantitatively much larger but they call for much tighter estimates.
2
Preliminaries
Throughout this paper, graphs are simple, undirected, and unweighted. In considering a graph coloring
problem, the input graph will usually be called G and we will put n = |V(G)|. The notation “log x” stands for
log2 x. For an integer k, we denote the set {1, 2, . . . , k} by [k].
For a graph G, we deﬁne ∆(G) = max{deg(v) : v ∈V(G)}. We say that G is k-degenerate if every induced
subgraph of G has a vertex of degree at most k. For instance, every forest is 1-degenerate and an elementary
theorem says that every planar graph is 5-degenerate. The degeneracy κ(G) is the smallest k such that G
is k-degenerate. The arboricity α(G) is the smallest r such that the edge set E(G) can be partitioned into r
forests. When the graph G is clear from the context, we simply write ∆, κ, and α, instead of ∆(G), κ(G), and
α(G).
We note two useful facts: the ﬁrst is immediate from the deﬁnition, and the second is an easy exercise.
Fact 2.1. If an n-vertex graph has degeneracy κ, then it has at most κn edges.
□
Fact 2.2. In every graph, the degeneracy κ and arboricity α satisfy α ⩽κ ⩽2α −1.
□
In analyzing our algorithms, it will be useful to consider certain vertex orderings of graphs and their
connection with the notion of degeneracy, given by Lemma 2.5 below. Although the lemma is folklore, it is
crucial to our analysis, so we include a proof for completeness.
Deﬁnition 2.3. An ordering of G is a list consisting of all its vertices (equivalently, a total order on V(G)).
Given an ordering ◁, for each v ∈V(G), the ordered neighborhood
NG,◁(v) := {w ∈V(G) : {v, w} ∈E(G), v ◁w} ,
i.e., the set of neighbors of v that appear after v in the ordering. The ordered degree odegG,◁(v) := |NG,◁(v)|.
Deﬁnition 2.4. A degeneracy ordering of G is an ordering produced by the following algorithm: starting
with an empty list, repeatedly pick a minimum degree vertex v (breaking ties arbitrarily), append v to the end
of the list, and delete v from G; continue this until G becomes empty.
6


## Page 7


Lemma 2.5. A graph G is k-degenerate iﬀthere exists an ordering ◁such that odegG,◁(v) ⩽k for all
v ∈V(G).
Proof. Suppose that G is k-degenerate. Let ◁= (v1, . . . , vn) be a degeneracy ordering. Then, for each i,
odegG,◁(vi) is the degree of vi in the induced subgraph G \ {v1, . . . , vi−1}. By deﬁnition, this induced subgraph
has a vertex of degree at most k, so vi, being a minimum degree vertex in the subgraph, must have degree at
most k.
On the other hand, suppose that G has an ordering ◁such that odegG,◁(v) ⩽k for all v ∈V(G). Let H
be an induced subgraph of G. Let v be the leftmost (i.e., smallest) vertex in V(H) according to ◁. Then all
neighbors of v in H in fact lie in NG,◁(v), so degH(v) ⩽odegG,◁(v) ⩽k. Therefore, G is k-degenerate.
□
A c-coloring of a graph G is a mapping ψ: V(G) →[c]; it is said to be a proper coloring if it makes no
edge monochromatic: ψ(u) , ψ(v) for all {u, v} ∈E(G). The smallest c such that G has a proper c-coloring is
called the chromatic number χ(G). By considering the vertices of G one at a time and coloring greedily, we
immediately obtain a proper (∆+ 1)-coloring. This idea easily extends to degeneracy-based coloring.
Lemma 2.6. Given unrestricted (“oﬄine”) access to an input graph G, we can produce a proper (κ + 1)-
coloring in linear time.
Proof. Construct a degeneracy ordering (v1, . . . , vn) of G and then consider the vertices one by one in the
order (vn, . . . , v1), coloring greedily. Given a palette of size κ + 1, by the “only if” direction of Lemma 2.5,
there will always be a free color for a vertex when it is considered.
□
Of course, the simple algorithm above is not implementable directly in “sublinear” settings, such as
space-bounded streaming algorithms, query models, or distributed computing models. Nevertheless, we shall
make use of the algorithm on suitably constructed subgraphs of our input graph.
We shall use the following form of the Chernoﬀbound.
Fact 2.7. Let X be a sum of mutually independent indicator random variables. Let µ and δ be real numbers
such that EX ⩽µ and 0 ⩽δ ⩽1. Then, Pr X ⩾(1 + δ)µ ⩽exp

−µδ2/3

.
□
3
A Generic Framework for Coloring
In this section, we give a generic framework for graph coloring that we later instantiate in various compu-
tational models. As a reminder, our focus is on graphs G with a nontrivial upper bound on the degeneracy
κ = κ(G). Each such graph admits a proper (κ + 1)-coloring; our focus will be on obtaining a proper
(κ + o(κ))-coloring eﬃciently.
As a broad outline, our framework calls for coloring G in two phases. The ﬁrst phase produces a low
degeneracy partition (LDP) of G: it partitions V(G) into a “small” number of parts, each of which induces a
subgraph that has “low” degeneracy. This step can be thought of as preprocessing and it is essentially free
(in terms of complexity) in each of our models. The second phase properly colors each part, using a small
number of colors, which is possible because the degeneracy is low. In Section 4, we shall see that the low
degeneracy allows this second phase to be eﬃcient in each of the models we consider.
3.1
A Low Degeneracy Partition and its Application
In this phase of our coloring framework, we assign each vertex a color chosen uniformly at random from [ℓ],
these choices being mutually independent, where ℓis a suitable parameter. For each i ∈[ℓ], let Gi denote the
subgraph of G induced by vertices colored i. We shall call each Gi a block of the vertex partition given by
(G1, . . . ,Gℓ). The next theorem, our main technical tool, provides certain guarantees on this partition given a
suitable choice of ℓ.
7


## Page 8


Theorem 3.1 (LDP Theorem). Let G be an n-vertex graph with degeneracy κ. Let k ∈[1, n] be a “guess” for
the value of κ and let s ⩾Cn log n be a sparsity parameter, where C is a suﬃciently large universal constant.
Put
ℓ=
&2nk
s
'
,
λ = 3
p
κℓlog n ,
(1)
and let ψ: V(G) →[ℓ] be a uniformly random coloring of G. For i ∈[ℓ], let Gi be the subgraph induced by
ψ−1(i). Then, the partition (G1, . . . ,Gℓ) has the following properties.
(i) If k ⩽2κ, then w.h.p., for each i, the degeneracy κ(Gi) ⩽(κ + λ)/ℓ.
(ii) W.h.p., for each i, the block size |V(Gi)| ⩽2n/ℓ.
(iii) If κ ⩽k ⩽2κ, then w.h.p., the number of monochromatic edges |E(G1) ∪· · · ∪E(Gℓ)| ⩽s.
In each case, “w.h.p.” means “with probability at least 1 −1/ poly(n).”
It will be convenient to encapsulate the guarantees of this theorem in a deﬁnition.
Deﬁnition 3.2. Suppose graph G has degeneracy κ. A vertex partition (G1, . . . ,Gℓ) simultaneously satisfying
the degeneracy bound in item (i), the block size bound in item (ii), and the (monochromatic) edge sparsity
bound in item (iii) in Theorem 3.1 is called an (ℓ, s, λ)-LDP of G.
It will turn out that an (ℓ, s, λ)-LDP leads to a proper coloring of G using at most κ + λ + ℓcolors. An
instructive setting of parameters is s = Θ((n log n)/ε2), where ε is either a small constant or a slowly vanishing
function of n, such as 1/ log n. Then, a quick calculation shows that when an accurate guess k ∈[κ, 2κ] is
made, Theorem 3.1 guarantees an LDP that has edge sparsity s = e
O(n) and that leads to an eventual proper
coloring using (1 + O(ε))κ colors. When ε = o(1), this number of colors is κ + o(κ).
Recall that the second phase of our coloring framework involves coloring each Gi separately, exploiting its
low degeneracy. Indeed, given an (ℓ, s, λ)-LDP, each block Gi admits a proper (κ(Gi) + 1)-coloring. Suppose
we use a distinct palette for each block; then the total number of colors used is
ℓ
X
i=1
(κ(Gi) + 1) ⩽ℓ
κ + λ
ℓ
+ 1

= κ + λ + ℓ,
(2)
as claimed above. Of course, even if our ﬁrst phase random coloring ψ yields a suitable LDP, we still
have to collect each block Gi or at least enough information about each block so as to produce a proper
(κ(Gi) + 1)-coloring. How we do this depends on the precise model of computation. We take this up in
Section 4.
3.2
Proof of the LDP Theorem
We now turn to proving the LDP Theorem from Section 3.1. Notice that when k ⩽(C/2) log n, the condition
s ⩾Cn log n results in ℓ= 1, so the vertex partition is the trivial one-block partition, which obviously satisﬁes
all the properties in the theorem. Thus, in our proof, we may assume that k > (C/2) log n.
Proof of Theorem 3.1. We start with item (ii), which is the most straightforward. From eq. (1), we have
ℓ⩽4nk/s, so
n
ℓ⩾s
4k ⩾Cn log n
4k
⩾C log n
4
.
Each block size |V(Gi)| has binomial distribution Bin(n, 1/ℓ), so a Chernoﬀbound gives
Pr
"
|V(Gi)| > 2n
ℓ
#
⩽exp

−n
3ℓ

⩽exp
 
−C log n
12
!
⩽1
n2 ,
8


## Page 9


for suﬃciently large C. By a union bound over the at most n blocks, item (ii) fails with probability at most
1/n.
Items (i) and (iii) include the condition k ⩽2κ, which we shall assume for the rest of the proof. By eq. (1)
and the bounds s ⩾Cn log n and k > (C/2) log n,
ℓ⩽
&
2k
C log n
'
⩽
4k
C log n ⩽
8κ
C log n ,
whence, for suﬃciently large C,
λ ⩽3
s
κ ·
8κ
C log n · log n ⩽κ .
(3)
We now turn to establishing item (i). Let ◁be a degeneracy ordering for G. For each i ∈[ℓ], let ◁i be the
restriction of ◁to V(Gi). Consider a particular vertex v ∈V(G) and let j = ψ(v) be its color. We shall prove
that, w.h.p., odegG,◁j(v) ⩽(κ + λ)/ℓ.
By the “only if” direction of Lemma 2.5, we have odegG,◁(v) = |NG,◁(v)| ⩽κ. Now note that
odegG j,◁j(v) =
X
u∈NG,◁(v)
1{ψ(u)=ψ(v)}
is a sum of mutually independent indicator random variables, each of which has expectation 1/ℓ. Therefore,
E odegG j,◁j(v) = odegG,◁(v)/ℓ⩽κ/ℓ. Since λ ⩽κ by eq. (3), we may use the form of the Chernoﬀbound in
Fact 2.7, which gives us
Pr

odegG j,◁j(v) > κ + λ
ℓ

⩽exp
 
−κ
ℓ
λ2
3κ2
!
= exp
 
−9κℓlog n
3κℓ
!
⩽1
n3 ,
where the equality follows from eq. (1). In words, with probability at least 1 −1/n3, the vertex v has ordered
degree at most (κ + λ)/ℓwithin its own block. By a union bound, with probability at least 1 −1/n2, all n
vertices of G satisfy this property. When this happens, by the “if” direction of Lemma 2.5, it follows that
κ(Gi) ⩽(κ + λ)/ℓfor every i.
Finally, we take up item (iii), which is now straightforward. Assume that the high probability event in
item (i) occurs. Then, by Fact 2.1,
|E(G1) ∪· · · ∪E(Gℓ)| ⩽
ℓ
X
i=1
κ(Gi) |V(Gi)| ⩽κ + λ
ℓ
ℓ
X
i=1
|V(Gi)| = n(κ + λ)
ℓ
⩽2nκ
ℓ
⩽s ,
where the ﬁnal inequality uses the condition κ ⩽k and eq. (1).
□
4
Speciﬁc Sublinear Algorithms for Coloring
We now turn to designing graph coloring algorithms in speciﬁc models of computation for big data, where the
focus is on utilizing space sublinear in the size of the massive input graph. Such models are sometimes termed
space-conscious. In each case, our algorithm ultimately relies on the framework developed in Section 3.
9


## Page 10


4.1
Data Streaming
We begin with the most intensely studied space-conscious model: the data streaming model. For graph
problems, in the basic model, the input is a stream of non-repeated edges that deﬁne the input graph G: this
is called the insertion-only model, since it can be thought of as building up G through a sequence of edge
insertions. In the more general dynamic graph model or turnstile model, the stream is a sequence of edge
updates, each update being either an insertion or a deletion: the net eﬀect is to build up G. Our algorithm will
work in this more general model. Later, we shall give a corresponding lower bound that will hold even in the
insertion-only model (for a lower bound, this is a strength).
We assume that the vertex set V(G) = [n] and the input is a stream σ of at most m = poly(n) updates
to an initially empty graph. An update is a triple (u, v, c), where u, v ∈V(G) and c ∈{−1, 1}: when c = 1,
this token represents an insertion of edge {u, v} and when c = −1, it represents a deletion. Let N =
n
2

and
[[m]] = Z ∩[−m, m]. It is convenient to imagine a vector x ∈[[m]]N of edge multiplicities that starts at zero
and is updated entrywise with each token. The input graph G described by the stream will be the underlying
simple graph, i.e., E(G) will be the set of all edges {u, v} such that xu,v , 0 at the end. We shall say that σ
builds up x and G.
Our algorithm makes use of two data streaming primitives, each a linear sketch. (We can do away with
these sketches in the insertion-only setting; see the end of this section.) The ﬁrst is a sketch for sparse
recovery given by a matrix A (say): given a vector x ∈[[m]]N with sparsity ∥x∥0 ⩽t, there is an eﬃcient
algorithm to reconstruct x from Ax. The second is a sketch for ℓ0 estimation given by a random matrix B
(say): given a vector x ∈[[m]]N, there is an eﬃcient algorithm that takes Bx and computes from it an estimate
of ∥x∥0 that, with probability at least 1 −δ, is a (1 + γ)-multiplicative approximation. It is known that there
exists a suitable A ∈{0, 1}d×N, where d = O(t log(N/t)), where A has column sparsity O(log(N/t)); see, e.g.,
Theorem 9 of Gilbert and Indyk [GI10]. It is also known that there exists a suitable distribution over matrices
giving B ∈{0, 1}d′×N with d′ = O(γ−2 log δ−1 log N(log γ−1 + log log m)). Further, given an update to the ith
entry of x, the resulting updates in Ax and Bx can be eﬀected quickly by generating the required portion of
the ith columns of A and B.
Algorithm 1 One-Pass Streaming Algorithm for Graph Coloring via Degeneracy
1: procedure Color(stream σ, integer k)
▷σ builds up x and G; k ∈[1, n] is a guess for κ(G)
2:
choose s, ℓas in eq. (1) and t, d, d′, A, B as in the above discussion
3:
initialize y ∈[[m]]d and z ∈[[m]]d′ to zero
4:
foreach u ∈[n] do ψ(u) ←uniform random color in [ℓ]
5:
foreach token (u, v, c) in σ do
6:
if ψ(u) = ψ(v) then y ←y + cAu,v; z ←z + cBu,v
7:
if estimate of ∥w∥0 obtained from z is > 5s/4 then abort
8:
w′ ←result of t-sparse recovery from y
▷we expect that w′ = w
9:
foreach i ∈[ℓ] do
10:
Gi ←simple graph induced by {{u, v} : w′
u,v , 0 and ψ(u) = ψ(v) = i}
11:
color Gi using palette {(i, j) : 1 ⩽j ⩽κ(Gi) + 1}; cf. Lemma 2.6
▷net eﬀect is to color G
In our description of Algorithm 1, we use Au,v (resp. Bu,v) to denote the column of A (resp. B) indexed by
{u, v}. The algorithm’s logic results in sketches y = Aw and z = Bw, where w corresponds to the subgraph of
G consisting of ψ-monochromatic edges only (cf. Theorem 3.1), i.e., w is obtained from x by zeroing out all
entries except those indexed by {u, v} with ψ(u) = ψ(v). We choose the parameter t = 2s, where s ⩾Cn log n
is the sparsity parameter from Theorem 3.1, which gives d = O(s log n); we choose γ = 1/4 and δ = 1/n,
giving d′ = O(log3 n).
10


## Page 11


Notice that Algorithm 1 requires a guess for κ := κ(G), which is not known in advance. Our ﬁnal one-pass
algorithm runs O(log n) parallel instances of Color(σ, k), using geometrically spaced guesses k = 2, 4, 8 . . . .
It outputs the coloring produced by the non-aborting run that uses the smallest guess.
Theorem 4.1. Set s = ⌈ε−2n log n⌉, where ε > 0 is a parameter. The above one-pass algorithm processes a
dynamic (i.e., turnstile) graph stream using O(ε−2n log4 n) bits of space and, with high probability, produces
a proper coloring using at most (1 + O(ε))κ colors. In particular, taking ε = 1/ log n, it produces a κ + o(κ)
coloring using e
O(n) space. Each edge update is processed in e
O(1) time and post-processing at the end of the
stream takes e
O(n) time.
Proof. The coloring produced is obviously proper. Let us bound the number of colors used. One of the
parallel runs of Color(σ, k) in 1 will use a value k = k⋆∈(κ, 2κ]. We shall prove that, w.h.p., (a) every
non-aborting run with k ⩽k⋆will use at most (1 + O(ε))κ colors, and (b) the run with k = k⋆will not abort.
We start with (a). Consider a particular run using k ⩽k⋆. By item (i) of Theorem 3.1, each Gi has
degeneracy at most (κ + λ)/ℓ; so if w is correctly recovered by the sparse recovery sketch (i.e., w′ = w in
Algorithm 1), then each Gi is correctly recovered and the run uses at most κ + λ + ℓcolors, as in eq. (2).
Using the values from eq. (1), this number is at most (1 + O(ε))κ. Now, if the run does not abort, then the
estimate of the sparsity ∥w∥0 is at most 5s/4. By the guarantees of the ℓ0-estimation sketch, the true sparsity
is at most (5/4)(5s/4) < 2s = t, so, w.h.p., w is indeed t-sparse and, by the guarantees of the sparse recovery
sketch, w′ = w. Taking a union bound over all O(log n) runs, the bound on the number of colors holds for all
required runs simultaneously, w.h.p.
We now take up (b). Note that ∥w∥0 is precisely the number of ψ-monochromatic edges in G. By item (iii)
of Theorem 3.1, we have ∥w0∥⩽s w.h.p. By the accuracy guarantee of the ℓ0-estimation sketch, in this run
the estimate of ∥w∥0 is at most 5s/4 w.h.p., so the run does not abort.
The space usage of each parallel run is dominated by the computation of y, so it is O(d log m) =
O(s log n log m) = O(ε−2n log3 n), using our setting of s and the assumption m = poly(n). The claims about
the update time and post-processing time follow directly from the properties of a state-of-the-art sparse
recovery scheme, e.g., the scheme based on expander matching pursuit given in Theorem 9 of Gilbert and
Indyk [GI10].
□
Simpliﬁcation for Insertion-Only Streams. Algorithm 1 can be simpliﬁed considerably if the input stream
is insertion-only. We can then initialize each Gi to an empty graph and, upon seeing an edge {u, v} in the
stream, insert it into Gi iﬀψ(u) = ψ(v) = i. We abort if we collect more than s edges; w.h.p., this will not
happen, thanks to Theorem 3.1. Finally, we color the collected graphs Gi greedily, just as in Algorithm 1.
With this simpliﬁcation, the overall space usage drops to O(s log n) = O(ε−2n log2 n) bits.
The reason this does not work for dynamic graph streams is that the number of monochromatic edges
could exceed s by an arbitrary amount mid-stream.
4.2
Query Model
We now turn to the general graph query model, a standard model of space-conscious algorithms for big
graphs where the input graph is random-accessible but the emphasis is on the examining only a tiny (ideally,
sublinear) portion of it; for general background see Chapter 10 of Goldreich’s book [Gol17]. In this model,
the algorithm starts out knowing the vertex set [n] of the input graph G and can access G only through the
following types of queries.
• A pair query Pair({u, v}), where u, v ∈[n]. The query returns 1 if {u, v} ∈E(G) and 0 otherwise. For
better readability, we shall write this query as Pair(u, v).
11


## Page 12


• A neighbor query Neighbor(u, j), where u ∈[n] and j ∈[n −1]. The query returns v ∈[n] where v is
the jth neighbor of u in some underlying ﬁxed ordering of vertex adjacency lists; if deg(v) < j, so that
there does not exist a jth neighbor, the query returns ⊥.
Naturally, when solving a problem in this model, the goal is to do so while minimizing the number of queries.
By adapting the combinatorial machinery from their semi streaming algorithm, Assadi et al. [ACK19]
gave an e
O(n3/2)-query algorithm for ﬁnding a (∆+ 1)-coloring. Our LDP framework gives a considerably
simpler algorithm using κ + o(κ) colors, where κ := κ(G). We remark here that e
O(n3/2) query complexity
is essentially optimal, as Assadi et al. [ACK19] proved a matching lower bound for any (c · ∆)-coloring
algorithm, for any constant c > 1.
Theorem 4.2. Given query access to a graph G, there is a randomized algorithm that, with high probability,
produces a proper coloring of G using κ + o(κ) colors. The algorithm’s worst-case query complexity, running
time, and space usage are all e
O(n3/2).
Proof. The algorithm proceeds in two stages. In the ﬁrst stage, it attempts to extract all edges in G through
neighbor queries alone, aborting when “too many” queries have been made. More precisely, it loops over
all vertices v and, for each v, issues queries Neighbor(v, 1), Neighbor(v, 2), . . . until a query returns ⊥. If
this stage ends up making 3n3/2 queries (say) without having processed every vertex, then it aborts and
the algorithm moves on to the second stage. By Fact 2.1, if κ ⩽√n, then this stage will not abort and the
algorithm will have obtained G completely; it can then (κ + 1)-color G (as in Lemma 2.6) and terminate,
skipping the second stage.
In the second stage, we know that κ > √n. The algorithm now uses a random coloring ψ to construct
an (ℓ, s, λ)-LDP of G using the “guess” k = √n, with s = Θ(ε−2n log n) and ℓ, λ given by Equation (1).
To produce each subgraph Gi in the LDP, the algorithm simply makes all possible queries Pair(u, v) where
ψ(u) = ψ(v). W.h.p., the number of queries made is at most
1
2
X
i∈[ℓ]
|V(Gi)|2 ⩽ℓ
2
 2n
ℓ
!2
⩽2n2s
4nk = Θ
 n3/2 log n
ε2
!
,
where the ﬁrst inequality uses Item (ii) of Theorem 3.1. We can enforce this bound in the worst case by
aborting if it is violated.
Clearly, k ⩽2κ, so Item (i) of Theorem 3.1 applies and by the discussion after Deﬁnition 3.2, the
algorithm uses (1 + O(ε))κ colors. Setting ε = 1/ log n, this number is at most κ + o(κ) and the overall number
of queries remains e
O(n3/2), as required.
□
4.3
MPC and Congested Clique Models
In the Massively Parallel Communication (MPC) model of Beame et al. [BKS17], an input of size m is
distributed adversarially among p processors, each of which has S bits of working memory: here, p and S are
o(m) and, ideally, p ≈m/S . Computation proceeds in synchronous rounds: in each round, a processor carries
out some local computation (of arbitrary time complexity) and then communicates with as many of the other
processors as desired, provided that each processor sends and receives no more than S bits per round. The
primary goal in solving a problem is to minimize the number of rounds.
When the input is an n-vertex graph, the most natural and widely studied setting of MPC is S = e
O(n),
which enables each processor to hold some information about every vertex; this makes many graph problems
tractable. Since the input size m is potentially Ω(n2), it is reasonable to allow p = n many processors. Note
that the input is just a collection of edges, distributed adversarially among these processors, subject to the
memory constraint.
12


## Page 13


Theorem 4.3. There is a randomized O(1)-round MPC algorithm that, given an n-vertex graph G, outputs a
(κ + o(κ))-coloring of G with high probability. The algorithm uses n processors, each with O(n log2 n) bits of
memory.
Proof. Our algorithm will use n processors, each assigned to one vertex. If |E(G)| = O(n log n), then all of G
can be collected at one processor in a single round using |E(G)|·2⌈log n⌉= O(n log2 n) bits of communication
and the problem is solved trivially. Therefore, we may as well assume that |E(G)| = ω(n log n), which implies
κ = ω(log n), by Fact 2.1. We shall ﬁrst give an algorithm assuming that κ is known a priori. Our ﬁnal
algorithm will be a reﬁnement of this preliminary one.
Preliminary algorithm.
Take k = κ. Each processor chooses a random color for its vertex, implicitly
producing a partition (G1, . . . ,Gℓ) that is, w.h.p., an (ℓ, s, λ)-LDP; we take ℓ, λ as in eq. (1), s = Θ(ε−2n log n),
and ε = (k−1 log n)1/4. Note that ε = o(1). In Round 1, each processor sends its chosen color to all others—
this is O(n log n) bits of communication per machine—and as a result every processor learns which of its
vertex’s incident edges are monochromatic. Now each color i ∈[ℓ] is assigned a unique machine Mi and, in
Round 2, all edges in Gi are sent to Mi. Each Mi then locally computes a (κ(Gi) + 1)-coloring of Gi using a
palette disjoint from those of other Mis; by the discussion following Deﬁnition 3.2, this colors G using at
most (1 + O(ε))κ = κ + o(κ) colors.
The communication in Round 2 is bounded by maxi |E(Gi)| · 2⌈log n⌉. By Fact 2.1, items (i) and (ii) of
Theorem 3.1, and eq. (1), the following holds w.h.p. for each i ∈[ℓ]:
|E(Gi)| ⩽κ(Gi)|V(Gi)| ⩽κ + λ
ℓ
2n
ℓ⩽4nκ
ℓ2 ⩽
4nk
(2nk/s)2 = O(ε−2n log n)2
nk
= O
 n log2 n
ε4k
!
= O(n log n) .
(4)
Thus, the communication per processor in Round 2 is O(n log2 n) bits.
Final algorithm. When we don’t know κ in advance, we can make geometrically spaced guesses k, as in
Section 4.1. In Round 1, we choose a random coloring for each such k. In Round 2, we determine the
quantities |E(Gi)| for each k and each subgraph Gi and thereby determine the smallest k such that eq. (4)
holds for every Gi corresponding to this k. We then run Round 3 for only this one k, replicating the logic of
Round 2 of the preliminary algorithm.
Correctness is immediate. We turn to bounding the communication cost. For Round 3, the previous
analysis shows that the communication per processor is O(n log2 n) bits. For Rounds 1 and 2, let us consider
the communication involved for each guess k: since each randomly-chosen color and each cardinality |E(Gi)|
can be described in O(log n) bits, each processor sends and receives at most O(n log n) bits per guess. This is
a total of O(n log2 n) bits, as claimed.
□
The CONGESTED-CLIQUE model [LPPP05] is a well established model of distributed computing for
graph problems. In this model, there are n nodes, each of which holds the local neighborhood information (i.e.,
the incident edges) of one vertex of the input graph G. In each round, every pair of nodes may communicate,
whether or not they are adjacent in G, but the communication is restricted to O(log n) bits. There is no
constraint on a node’s local memory. The goal is to minimize the number of rounds.
Behnezhad et al. [BDH18] built on results of Lenzen [Len13] to show that any algorithm in the semi-MPC
model—deﬁned as MPC with space per machine being O(n log n) bits—can be simulated in the Congested
Clique model, preserving the round complexity up to a constant factor. Based on this, we obtain the following
result.
Theorem 4.4. There is a randomized O(1)-round algorithm in the Congested Clique model that, given a
graph G, w.h.p. ﬁnds a (κ + O(κ3/4 log1/2 n))-coloring. For κ = ω(log2 n), this gives a (κ + o(κ))-coloring.
□
13


## Page 14


Proof. We cannot directly use our algorithm in Theorem 4.3 because it is not a semi-MPC algorithm: it uses
O(n log2 n) bits of space per processor, rather than O(n log n). However, with a more eﬃcient implementation
of Round 1, a more careful analysis of Round 2, and a slight tweak of parameters for Round 3, we can
improve the communication (hence, space) bounds to O(n log n), whereupon the theorem of Behnezhad et
al. [BDH18] completes the proof.
For Round 3, the tweak is to set ε = (k−1 log2 n)1/4 but otherwise replicate the logic of the ﬁnal algorithm
from Theorem 4.3. With this higher value of ε, the bound from eq. (4) improves to |E(Gi)| = O(n). Therefore
the per-processor communication in Round 3 is only O(n log n) bits. The number of colors used is, w.h.p., at
most (1 + O(ε))κ = κ + O(κ3/4 log1/2 n).
For a tighter analysis of the communication cost of Round 2, note that, for a particular guess k, there is
a corresponding ℓgiven by eq. (1) such that each processor need only send/receive ℓcardinalities |E(Gi)|,
each of which can be described in O(log n) bits. Consulting eq. (1), we see that ℓ= O(n2/s) = O(n/ log n).
Therefore, summing over all O(log n) choices of k, each processor communicates at most
O(n/ log n) · O(log n) · O(log n) = O(n log n) bits.
Round 1 appears problematic at ﬁrst, since there are O(log n) many random colorings to be chosen, one
for each guess k. However, note that these colorings need not be independent. Therefore, we can choose
just one random ⌈log n⌉-bit “master color” φ(v) for each vertex v and derive the random colorings for the
various guesses k by using only appropriate length preﬁxes of φ(v). This ensures that each processor only
communicates O(n log n) bits in Round 1.
□
4.4
Distributed Coloring in the LOCAL Model
In the LOCAL model, each node of the input graph G hosts a processor that knows only its own neighborhood.
The processors operate in synchronous rounds, during which they can send and receive messages of arbitrary
length to and from their neighbors. The processors are allowed unbounded local computation in each round.
The key complexity measure is time, deﬁned as the number of rounds used by an algorithm (expected number,
for a randomized algorithm) on a worst-case input.
Graph coloring in the LOCAL model is very heavily studied and is one of the central problems in
distributed algorithms. Here, our focus is on algorithms that properly color the input graph G using a number
of colors that depends on α := α(G), the arboricity of G. Recall that α ⩽κ ⩽2α −1 (Fact 2.2). Unlike
in previous sections, our results will give big-O bounds on the number of colors, so we may as well state
them in terms of α (following established tradition in this line of work) rather than κ. Our focus will be on
algorithms that run in sublogarithmic time, while using not too many colors. See Section 1.2 for a quick
summary of other interesting parameter regimes and Barenboim and Elkin [BE13] for a thorough treatment
of graph coloring in the LOCAL model.
Kothapalli and Pemmaraju [KP11] gave an O(k)-round algorithm that uses O(αn1/k) colors, for all k with
2 log log n ⩽k ⩽
p
log n. We give a new coloring algorithm that, in particular, extends the range of k to which
such a time/quality tradeoﬀapplies: for k ∈ω(
p
log n), o(log n), we can compute an O(αn1/k log n)-coloring
in O(k) rounds.
Our algorithm uses our LDP framework to split the input graph into parts with logarithmic degeneracy
(hence, arboricity) and then invokes an algorithm of Barenboim and Elkin. The following theorem records
the key properties of their algorithm.
Lemma 4.5 (Thm 5.6 of Barenboim and Elkin [BE10]). There is a deterministic distributed algorithm in
the LOCAL model that, given an n-vertex graph G, an upper bound b on α(G), and a parameter t with
2 < t ⩽O( √n/b), produces an O(tb2)-coloring of G in time O

logt n + log⋆n

.
□
Here is the main result of this section.
14


## Page 15


Theorem 4.6. There is a randomized distributed algorithm in the LOCAL model that, given an n-vertex graph
G, an estimate of its arboricity α up to a constant factor, and a parameter t such that 2 < t ⩽O(
p
n/ log n),
produces an O(tα log n)-coloring of G in time O

logt n + log⋆n

.
Proof. To simplify the presentation, we assume that α = α(G). We assume that every node (vertex) knows n
and α. Consider a (ℓ, s, λ)-LDP of G, where we put s = Cn log n, for some large constant C, as in Theorem 3.1.
This setting of s gives ℓ= O(α/ log n). First, each vertex v chooses a color ψ(v) uniformly at random from
[ℓ]. Next, we need to eﬀectively “construct” the blocks Gi, for each i ∈[ℓ]. This is straightforwardly done in
a single round: each vertex v sends ψ(v) to all its neighbors.
At this point, each vertex v knows its neighbors in the block Gψ(v). So it’s now possible to run a distributed
algorithm on each Gi. We invoke the algorithm in Lemma 4.5. The algorithm needs each vertex v to know an
upper bound bi on α(Gi), where i = ψ(v). A useful upper bound of bi = O(log n), which holds w.h.p., is given
by item (i) of Theorem 3.1.
By Lemma 4.5, each Gi can be colored using O(t log2 n) colors, within another O

logt n + log⋆n

rounds,
since 2 < t ⩽O(
p
n/ log n). Using disjoint palettes for the distinct blocks, the total number of colors used for
G is at most ℓ· O(t log2 n) = O(tα log n), as required.
□
The particular form of the tradeoﬀstated in Table 1 is obtained by setting t = n1/k (for some k ⩾3) in the
above theorem.
Corollary 4.7. There is a randomized LOCAL algorithm that, given graph G, estimate α ≈α(G), and a
parameter k with 2 < n1/k ⩽O(
p
n/ log n), ﬁnds an O(αn1/k log n)-coloring of G in time O

k + log⋆n

.
□
5
Lower Bounds
Can we improve the guarantees of our algorithms so that they use at most κ + 1 colors, rather than κ + o(κ)?
After all, every graph G does have a proper (κ(G) + 1)-coloring. The main message of this section is that
answer is a strong “No,” at least in the data streaming and query models. If we insist on a coloring that good,
we would incur the worst possible space or query complexity: Ω(n2). In fact, this holds even if κ is known to
the algorithm in advance. Moreover, all our streaming lower bounds hold even if the input stream consists of
edge insertions alone.
Our lower bounds generalize to the problem of producing a (κ + λ)-coloring. We show that this requires
Ω(n2/λ2) space or query complexity. Such generalizations are based on the following Blow-Up Lemma.
Deﬁnition 5.1. Let G be a graph and λ a positive integer. The blow-up graph Gλ is obtained by replacing
each vertex of G with a copy of the complete graph Kλ and replacing each edge of G with a complete bipartite
graph between the copies of Kλ at its endpoints. More succinctly, Gλ is the lexicographical product G[Kλ].
Lemma 5.2 (Blow-Up Lemma). For all graphs G and positive integers λ, c, if G has a c-clique, then Gλ has
a (cλ)-clique. Also, κ(Gλ) ⩽(κ(G) + 1)λ −1.
Proof. The claim about cliques is immediate. The bound on κ(Gλ) follows by taking a degeneracy ordering
of G and replacing each vertex v by a list of vertices of the clique that replaces v in Gλ, ordering vertices
within the clique arbitrarily.
□
Our lower bounds come in two ﬂavors. The ﬁrst address the hardness of distinguishing low-degeneracy
graphs from high-chromatic-number graphs. This is encapsulated in the following abstract problem.
15


## Page 16


L
R
l
r
C
y
z
(a)
l
L
R
L
R
C
r
l
r
(b)
ai
aj
b
b
j
i
A
B
(c)
Figure 1: Gadget graphs used in (a) Lemma 5.5; (b) Theorem 5.7; (c) Lemma 5.12 and Theorem 5.14.
Deﬁnition 5.3 (graph-dist problem). Consider two graph families: G1 := G1(n, q, λ), consisting of n-vertex
graphs with chromatic number χ ⩾(q + 1)λ, and G2 := G2(n, q, λ), consisting of n-vertex graphs with
κ ⩽qλ −1. Then graph-dist(n, q, λ) is the problem of distinguishing G1 from G2; note that G1 ∩G2 = ∅.
More precisely, given an input graph G on n vertices, the problem is to decide whether G ∈G1 or G ∈G2,
with success probability at least 2/3.
We shall prove that graph-dist is “hard” in the insertion-only streaming setting and in the query setting,
thereby establishing that in these models it is hard to produce a (κ + λ)-coloring. In fact, our proofs will show
that it is just as hard to estimate the parameter κ; this goes to show that the hardness of the coloring problem
is not just because of the large output size.
Lower bounds of the above ﬂavor raise the following question: since estimating κ itself is hard, does the
coloring problem become easier if the value of κ(G) is given in advance, before the algorithm starts to read
G? In fact, the (∆+ 1)-coloring algorithms by Assadi et al. [ACK19] assume that ∆is known in advance.
However, perhaps surprisingly, we prove a second ﬂavor of lower bounds, showing that a priori knowledge
of κ does not help and (κ + 1)-coloring (more generally, (κ + λ)-coloring) remains a hard problem even under
the strong assumption that κ is known in advance.
5.1
Streaming Lower Bounds
In this section, we prove both ﬂavors of lower bounds in the one-pass streaming setting. The next section
takes up the query model.
Our streaming lower bounds use reductions from the index and int-find (intersection ﬁnding, a variant
of disjointness) problems in communication complexity. In the indexN problem, Alice is given a vector
x = (x1, . . . , xN) ∈{0, 1}N and Bob is given an index k ∈[N]. The goal is for Alice to send Bob a (possibly
random) c-bit message that enables Bob to output xk with probability at least 2/3. The smallest c for
which such a protocol exists is called the one-way randomized communication complexity, R→(indexN). In
int-findN, Alice and Bob hold vectors x, y ∈{0, 1}N, interpreted as subsets of [N], satisfying the promise that
|x∩y| = 1. They must ﬁnd the unique index i where xi = yi = 1, using at most c bits of randomized interactive
communication, succeeding with probability at least 2/3. The smallest c for which such a protocol exists is
the randomized communication complexity, R(int-findN). As is well known, R→(indexN) = Ω(N) [Abl96]
and R(int-findN) = Ω(N); the latter is a simple extension of the disjointness lower bound [Raz92].
16


## Page 17


We shall in fact consider instances of indexN where N = p2, for an integer p. Using a canonical
bijection between [N] and [p] × [p], we reinterpret x as a matrix with entries (xi j)i,j∈[p], and Bob’s input as
(y, z) ∈[p] × [p]. We further interpret this matrix x as the bipartite adjacency matrix of a (2p)-vertex balanced
bipartite graph Hx. Such graphs Hx will be key gadgets in the reductions to follow.
Deﬁnition 5.4. For x ∈{0, 1}p×p, a realization of Hx on a list (ℓ1, . . . , ℓp, r1, . . . , rp) of distinct vertices is a
graph on these vertices whose edge set is {{ℓi, rj} : xi j = 1}.
First Flavor: Degeneracy Not Known in Advance. To prove lower bounds of the ﬁrst ﬂavor, we start by
demonstrating the hardness of the abstract problem graph-dist, from Deﬁnition 5.3.
Lemma 5.5. Solving graph-dist(n, q, λ) in one randomized streaming pass requires Ω(n2/λ2) space.
More precisely, there is a constant c > 0 such that for every integer λ ⩾1 and every suﬃciently large
integer q, there is a setting n = n(q, λ) for which every randomized one-pass streaming algorithm for
graph-dist(n, q, λ) requires at least cn2/λ2 bits of space.
Proof. Put p = q −1. We reduce from indexN, where N = p2, using the following plan. Starting with an
empty graph on n = 3λp vertices, Alice adds certain edges based on her input x ∈{0, 1}p×p and then Bob
adds certain other edges based on his input (y, z) ∈[p] × [p]. By design, solving graph-dist(n, q, λ) on the
resulting ﬁnal graph reveals the bit xyz, implying that a one-pass streaming algorithm for graph-dist requires
at least R→(indexN) = Ω(N) = Ω(p2) = Ω(n2/λ2) bits of memory. The details follow.
We ﬁrst consider λ = 1. We use the vertex set L ⊎R ⊎C (the notation “⊎” denotes a disjoint union),
where L = {ℓ1, . . . , ℓp}, R = {r1, . . . , rp}, and |C| = p. Alice introduces the edges of the gadget graph Hx
(from Deﬁnition 5.4), realized on the vertices (ℓ1, . . . , ℓp, r1, . . . , rp). Bob introduces all possible edges within
C ∪{ℓy, rz}, except for {ℓy, rz}. Let G be the resulting graph.
If xyz = 1, then G contains a clique on C ∪{ℓy, rz}, whence χ(G) ⩾p + 2. If, on the other hand, xyz = 0,
then we claim that κ(G) ⩽p. By Lemma 2.5, the claim will follow if we exhibit a vertex ordering ◁such that
odegG,◁(v) ⩽p for all v ∈V(G). We use an ordering where
L ∪R \ {ℓy, rz} ◁ℓy ◁{rz} ∪C
and the ordering within each set is arbitrary. By construction of Hx, each vertex in L ∪R \ {ℓy, rz} has total
degree at most p. For each vertex v ∈{rz} ∪C, we trivially have odegG,◁(v) ⩽p because |C| = p. Finally,
since xyz = 0, the vertex rz is not a neighbor of ℓy; so odegG,◁(ℓy) = |C| = p. This proves the claim.
When λ ⩾1, Alice and Bob introduce edges so as to create the blow-up graph Gλ, as in Deﬁnition 5.1.
By Lemma 5.2, if xyz = 1, then Gλ has a (p + 2)λ-clique, whereas if xyz = 0, then κ(Gλ) ⩽(p + 1)λ −1. In
the former case, χ(Gλ) ⩾(p + 2)λ = (q + 1)λ, so that Gλ ∈G1(n, q, λ); cf. Deﬁnition 5.3. In the latter case,
κ(Gλ) ⩽qλ −1, so that Gλ ∈G2(n, q, λ). Thus, solving graph-dist(n, q, λ) on Gλ reveals xyz.
□
Our coloring lower bounds are straightforward consequences of the above lemma.
Theorem 5.6. Given a single randomized pass over a stream of edges of an n-vertex graph G, succeeding
with probability at least 2/3 at either of the following tasks requires Ω(n2/λ2) space, where λ ⩾1 is an
integer parameter:
(i) produce a proper (κ + λ)-coloring of G;
(ii) produce an estimate ˆκ such that |ˆκ −κ| ⩽λ.
Furthermore, if we require λ = O κ
1
2 −γ, where γ > 0, then neither task admits a semi-streaming algorithm.
17


## Page 18


Proof. An algorithm for either task (i) and or task (ii) immediately solves graph-dist with appropriate
parameters, implying the Ω(n2/λ2) bounds, thanks to Lemma 5.5. For the “furthermore” statement, note that
the graphs in the family G2 constructed in the proof of Lemma 5.5 have κ = Θ(n), so performing either task
with the stated guarantee on λ would require Ω(n1+2γ) space, which is not in e
O(n).
□
Combining the above result with the algorithmic result in Theorem 4.1, we see that producing a (κ + o(κ))-
coloring is possible in semi-streaming space whereas producing a (κ + O κ
1
2−γ)-coloring is not. We leave
open the question of whether this gap can be tightened.
Second Flavor: Degeneracy Known in Advance. We now show that the coloring problem remains just as
hard even if the algorithm knows the degeneracy of the graph before seeing the edge stream.
Theorem 5.7. Given as input an integer κ, followed by a stream of edges of an n-vertex graph G with
degeneracy κ, a randomized one-pass algorithm that produces a proper (κ + λ)-coloring of G requires
Ω(n2/λ2) bits of space. Furthermore, if we require λ = O κ
1
2−γ, where γ > 0, then the task does not admit a
semi-streaming algorithm.
Proof. We reduce from indexN, where N = p2, using a plan analogous to the one used in proving Lemma 5.5.
Alice and Bob will construct a graph on n = 5λp vertices, using their respective inputs x ∈{0, 1}p×p and
(y, z) ∈[p] × [p].
First, we consider the case λ = 1. We use the vertex set L ⊎R ⊎L ⊎R ⊎C, where L = {ℓ1, . . . ℓp},
R = {r1, . . . , rp}, L = {ℓ1, . . . , ℓp}, R = {r1, . . . , rp}, and |C| = p. Let x be the bitwise complement of x. Alice
introduces the edges of the gadget graph Hx (from Deﬁnition 5.4), realized on L ∪R, and the edges of Hx
realized on L ∪R. For ease of notation, put ℓ:= ℓy, r := rz, ℓ:= ℓy, r := rz, and S := C ∪{ℓ, r, ℓ, r}. Bob
introduces all possible edges within S , except for {ℓ, r} and {ℓ, r}. Let G be the resulting graph.
We claim that the degeneracy κ(G) = p + 2. To prove this, we consider the case xyz = 1 (the other case,
xyz = 0, is symmetric). By construction, G contains a clique on the p + 3 vertices in C ∪{ℓ, r, ℓ}; therefore, by
deﬁnition of degeneracy, κ(G) ⩾p + 2. To show that κ(G) ⩽p + 2, it will suﬃce to exhibit a vertex ordering
◁such that odegG,◁(v) ⩽p + 2 for all v ∈V(G). To this end, consider an ordering where
V(G) \ S ◁ℓ◁S \ {ℓ}
and the ordering within each set is arbitrary. Each vertex v ∈V(G) \ S has odegG,◁(v) ⩽deg(v) ⩽p and each
vertex v ∈S \ {ℓ} has odegG,◁(v) ⩽
S \ {ℓ}
 −1 = p + 2. As for the vertex ℓ, since xyz = 1 −xyz = 0, by the
construction in Deﬁnition 5.4, r is not a neighbor of ℓ; therefore, odegG,◁(ℓ) ⩽
S \ {ℓ, r}
 = p + 2.
Let A be a streaming algorithm that behaves as in the theorem statement. Recall that we are considering
λ = 1. Since κ(G) = p + 2 for every instance of indexN, Alice and Bob can simulate A on their constructed
graph G by ﬁrst feeding it the number p + 2, then Alice’s edges, and then Bob’s. When A succeeds, the
coloring it outputs is a proper (p + 3)-coloring; therefore it must repeat a color inside S , as |S | = p + 4. But S
has exactly one pair of non-adjacent vertices: the pair {ℓ, r} if xyz = 0, and the pair {ℓ, r} if xyz = 1. Thus, an
examination of which two vertices in S receive the same color reveals xyz, solving the indexN instance. It
follows that A must use at least R→(indexN) = Ω(N) = Ω(p2) bits of space.
Now consider an arbitrary λ. Alice and Bob proceed as above, except that they simulate A on the blow-up
graph Gλ. Since G always has a (p + 3)-clique and κ(G) = p + 2, the two halves of Lemma 5.2 together imply
κ(Gλ) = (p + 3)λ −1. So, when A succeeds, it properly colors Gλ using at most (p + 4)λ −1 colors. For each
A ⊆V(G), abusing notation, let Aλ denote its corresponding set of vertices in Gλ (cf. Deﬁnition 5.1). Since
|S λ| = (p + 4)λ, there must be a color repetition within S λ. Reasoning as above, this repetition must occur
within {ℓ, r}λ when xyz = 0 and within {ℓ, r}λ when xyz = 1. Therefore, Bob can examine the coloring to solve
indexN, showing that A must use Ω(N) = Ω(p2) = Ω(n2/λ2) space.
The “furthermore” part follows by observing that κ(Gλ) = Θ |V(Gλ)|.
□
18


## Page 19


Multiple Passes. The streaming algorithm from Section 4.1 is one-pass, as are the lower bounds proved
above. Is the coloring problem any easier if we are allowed multiple passes over the edge stream? We now
give a simple argument showing that, if we slightly generalize the problem, it stays just as hard using multiple
(O(1) many) passes.
The generalization is to allow some edges to be repeated in the stream. In other words, the input is a
multigraph ˆG. Clearly, a coloring is proper for ˆG iﬀit is proper for the underlying simple graph G, so the
relevant algorithmic problem is to properly (κ + λ)-color G, where κ := κ(G). Note that our algorithm in
Section 4.1 does, in fact, solve this more general problem.
Theorem 5.8. Given as input an integer κ, followed by a stream of edges of an n-vertex multigraph ˆG
whose underlying simple graph has degeneracy κ, a randomized p-pass algorithm that produces a proper
(κ + λ)-coloring of G requires Ω(n2/(λ2p)) bits of space. This holds even if the stream is insertion-only, with
each edge appearing at most twice.
Proof. As usual, we prove this for λ = 1 and appeal to the Blow-Up Lemma (Lemma 5.2) to generalize.
We reduce from int-findN, with N =
n
2

. Let Alice and Bob treat their inputs as (xi j)1⩽i<j⩽n and (yi j)1⩽i<j⩽n
in some canonical way. Alice (resp. Bob) converts their input into an edge stream consisting of pairs (i, j)
such that i < j and xij = 0 (resp. yij = 0). The concatenation of these streams deﬁnes the multigraph ˆG given
to the coloring algorithm. Let (h, k) be the unique pair such that xhk = yhk = 1. Note that the underlying
simple graph G is Kn minus the edge {h, k}. Therefore, κ = n −2 and so, in a proper (n −1)-coloring of ˆG,
there must be a repeated color and this can only happen at vertices h and k.
Thus, a p-pass (κ + 1)-coloring algorithm using s bits of space leads to a protocol for int-findN using
(2p −1)s bits of communication. Therefore, s = Ω(N/p) = Ω(n2/p).
□
5.2
Query Complexity Lower Bounds
We now turn to the general graph query model [Gol17]. Recall that our algorithm from Section 4.2 produces
a (κ + o(κ))-coloring while making at most e
O(n3/2) queries, without needing to know κ in advance. Here, we
shall prove that the number of colors cannot be improved to κ + 1: that would preclude sublinear complexity.
In fact, we prove more general results, similar in spirit to the streaming lower bounds from the previous
section. For these lower bounds, we use another family of gadget graphs.
Deﬁnition 5.9. Given a large integer p (a size parameter), the gadgets for that size are (2p + 1)-vertex graphs
on vertex set A ⊎B, where A = {a1, . . . , ap+1} and B = {b1, . . . , bp}. Let H be the graph consisting of a clique
on A and a clique on B, with no edges between A and B. For 1 ⩽i < j ⩽p, let Hi j be a graph on the same
vertex set obtained by slightly modifying H as follows (see Figure 1c):
E(Hij) = E(H) \  {ai, aj}, {bi, bj} 	 ∪ {ai, bj}, {aj, bi} 	 .
(5)
Notice that the vertex ap+1 is not touched by any of these modiﬁcations. The relevant properties of these
gadget graphs are as follows.
Lemma 5.10. For all 1 ⩽i < j ⩽p, κ(Hij) = p −1, whereas the chromatic number χ(H) = p + 1.
Proof. The claim about χ(H) is immediate.
Consider a particular graph Hij. The subgraph induced by A \ {ai} is a p-clique, so κ(Hi j) ⩾p −1.
Now consider the following ordering ◁for Hi j: B ◁ai ◁A \ {ai}, where the order within each set is
arbitrary. For each v ∈B, odegHij,◁(v) ⩽deg(v) = p−1. For each v ∈A\{ai}, odegHij,◁(v) ⩽|A\{ai}|−1 = p−1.
Finally, ai has exactly p−1 neighbors in A\{ai} (by construction, aj is not a neighbor), so odegHij,◁(ai) = p−1.
By Lemma 2.5, it follows that κ(Hij) ⩽p −1.
□
19


## Page 20


Our proofs will use these gadget graphs in reductions from a pair of basic problems in decision tree
complexity. Consider inputs that are vectors in {0, 1}N: let 0 denote the all-zero vector and, for i ∈[N], let ei
denote the vector whose ith entry is 1 while all other entries are 0. Let unique-orN and unique-findN denote
the following partial functions on {0, 1}N:
unique-orN(x) =

0 ,
if x = 0 ,
1 ,
if x = ei , for i ∈[N] ,
⋆,
otherwise;
unique-findN(x) =

i ,
if x = ei , for i ∈[N] ,
⋆,
otherwise.
Informally, these problems capture, respectively, the tasks of (a) determining whether there is a needle in
a haystack under the promise that there is at most one needle, and (b) ﬁnding a needle in a haystack under
the promise that there is exactly one needle. Intuitively, solving either of these problems with high accuracy
should require searching almost the entire haystack. Formally, let Rdt
δ (f) denote the δ-error randomized query
complexity (a.k.a. decision tree complexity) of f. Elementary considerations of decision tree complexity lead
to the bounds below (for a thorough discussion, including formal deﬁnitions, we refer the reader to the survey
by Buhrman and de Wolf [BdW02]).
Fact 5.11. For all δ ∈(0, 1
2), we have Rdt
δ (unique-orN) ⩾(1−2δ)N and Rdt
δ (unique-findN) ⩾(1−δ)N −1.
□
With this setup, we turn to lower bounds of the ﬁrst ﬂavor.
Lemma 5.12. Solving graph-dist(n, p, λ) in the general graph query model requires Ω(n2/λ2) queries.
More precisely, there is a constant c > 0 such that for every integer λ ⩾1 and every suﬃciently large
integer p, there is a setting n = n(p, λ) for which every randomized query algorithm for graph-dist(n, p, λ)
requires at least cn2/λ2 queries in the worst case.
Proof. We reduce from unique-orN, where N =
p
2

, using the following plan. Put n = (2p + 1)λ. Let
C be a query algorithm for graph-dist(n, p, λ). Based on C, we shall design a 1
3-error algorithm A for
unique-orN that makes at most as many queries as C. By Fact 5.11, this number of queries must be at least
N/3 = Ω(p2) = Ω(n2/λ2).
As usual, we detail our reduction for λ = 1; the Blow-up Lemma (Lemma 5.2) then handles general λ.
By Lemma 5.10, H ∈G1 whereas each Hi j ∈G2 (cf. Deﬁnition 5.3, taking q = p).
We now design A. Let x ∈{0, 1}N be the input to A. Using a canonical bijection, let us index the bits of
x as xi j, where 1 ⩽i < j ⩽p. Algorithm A simulates C and outputs 1 iﬀC decides that its input lies in G2.
Since C makes queries to a graph, we shall design an oracle for C whose answers, based on query answers for
input x to A, will implicitly deﬁne a graph on vertex set V := A ⊎B, as in Deﬁnition 5.9. The oracle answers
queries as follows.
• For i, j ∈[p], it answers Pair(ai, aj) and Pair(bi, bj) with 1 −xi j.
• For i, j ∈[p], it answers Pair(ai, bj) and Pair(aj, bi) with xi j.
• For i ∈[p], it answers Pair(ap+1, ai) with 1 and Pair(ap+1, bi) with 0.
• For i ∈[p] and d ∈[p −1], it answers Neighbor(ai, d) with aj if xi j = 0 and bj if xi j = 1, where j = d
if d < i, and j = d + 1 otherwise.
• For i, d ∈[p], it answers Neighbor(ai, p) with ap+1 and Neighbor(ap+1, d) with ad.
• For i ∈[p] and d ∈[p −1], it answers Neighbor(bi, d) with bj if xi j = 0 and aj if xi j = 1, where j = d
if d < i, and j = d + 1 otherwise.
• For all other combinations of v ∈V and d ∈N, it answers Neighbor(v, d) = ⊥.
20


## Page 21


By inspection, we see that the graph deﬁned by this oracle is H if x = 0 and is Hi j if x = ei j. Furthermore,
the oracle answers each query by making at most one query to the input x. It follows that A makes at most as
many queries as C and decides unique-orN with error at most 1
3. This completes the proof for λ = 1.
To handle λ > 1, we modify the oracle in the natural way so that the implicitly deﬁned graph is Hλ when
x = 0 and Hλ
i j when x = eij. We omit the details, which are routine.
□
As an immediate consequence of Lemma 5.12, we get the following query lower bounds.
Theorem 5.13. Given query access to an n-vertex graph G, succeeding with probability at least 2/3 at either
of the following tasks requires Ω(n2/λ2) queries, where λ ⩾1 is an integer parameter:
(i) produce a proper (κ + λ)-coloring of G;
(ii) produce an estimate ˆκ such that |ˆκ −κ| ⩽λ.
□
We now prove a lower bound of the second ﬂavor, where the algorithm knows κ in advance.
Theorem 5.14. Given an integer κ and query access to an n-vertex graph G with κ(G) = κ, an algorithm
that, with probability 2
3, produces a proper (κ + λ)-coloring of G must make Ω(n2/λ2) queries.
Proof. We focus on the case λ = 1; the general case is handled by the Blow-up Lemma, as usual.
Let C be an algorithm for the coloring problem. We design an algorithm A for unique-findN, where
N =
p
2

, using the same reduction as in Lemma 5.12, changing the post-processing logic as follows: A
outputs (i, j) as its answer to unique-findN(x), where 1 ⩽i < j ⩽p is such that ai and aj are colored the same
by C.
To prove the correctness of this reduction, note that when x = ei j, the graph deﬁned by the simulated
oracle is Hi j and κ(Hij) = p −1 (Lemma 5.10). Suppose that C is successful, which happens with probability
at least 2
3. Then C properly p-colors Hij. Recall that V(Hi j) = A ⊎B, where |A| = p + 1; there must therefore
be a color repetition within A. The only two non-adjacent vertices inside A are ai and aj, so A correctly
answers (i, j). By Fact 5.11, A must make Ω(N) = Ω(p2) queries.
□
5.3
A Combinatorial Lower Bound
Finally, we explore a connection between degeneracy based coloring and the list coloring problem. In the
latter problem, each vertex has a list of colors and the goal is to ﬁnd a corresponding list coloring—i.e., a
proper coloring of the graph where each vertex receives a color from its list—or to report that none exists.
Assadi et al. [ACK19] proved a beautiful Palette Sparsiﬁcation Theorem, a purely graph-theoretic result that
connects the (∆+ 1)-coloring problem to the list coloring problem.
Deﬁne a graph G to be [ℓ, r]δ-randomly list colorable (brieﬂy, [ℓ, r]δ-RLC) if choosing r random colors
per vertex, independently and uniformly without replacement from the palette [ℓ], permits a list coloring with
probability at least 1 −δ using these chosen lists.2 Their theorem can be paraphrased as follows.
Fact 5.15 (Assadi et al. [ACK19], Theorem 1). There exists a constant c such that every n-vertex graph G is
[∆(G) + 1, c log n]1/n-RLC.
□
Indeed, this theorem is the basis of the various coloring results in their work. Let us outline how things
work in the streaming model, focusing on the space usage. Given an input graph G that is promised to
be [ℓ, r]1/3-RLC, for some parameters ℓ, r that may depend on G, we sample r random colors from [ℓ] for
each vertex before reading the input. Chernoﬀbounds imply that the conﬂict graph—the subgraph of G
consisting only of edges between vertices whose color lists intersect—is of size O(|E(G)|r2/ℓ), w.h.p.. Using
2When r ⩾l, this procedure simply produces the list [ℓ] for every vertex.
21


## Page 22


|E(G)| ⩽n∆/2, taking ℓ= ∆+ 1 and r = O(log n) bounds this size by e
O(n), so a semi-streaming space bound
suﬃces to collect the entire conﬂict graph. (For full details, see Lemma 4.1 in [ACK19].) Finding a list
coloring of the conﬂict graph (which exists with probability at least 2/3) yields an ℓ-coloring of G.
For a similar technique to work in our setting, we would want ℓ≈κ. Recalling that |E(G)| ⩽nκ, for the
space usage to be e
O(n), we need r = O(polylog n). This raises the following combinatorial question: what is
the smallest λ for which we can guarantee that every graph is [κ + λ, O(polylog n)]1/3-RLC?
By the discussion above, our streaming lower bound in Theorem 5.7 already tells us that such a result is
not possible with λ = O(κ
1
2−γ). Our ﬁnal result (Theorem 5.17 below) proves that we can say much more.
Let Jn,t denote the graph Kt + Kn−t, i.e., the graph join of a t-clique and an (n −t)-sized independent set.
More explicitly,
Jn,t = (A ⊎B, E) ,
where |A| = t, |B| = n −t, E = {{u, v} : u ∈A, v ∈A ∪B, u , v} .
(6)
Lemma 5.16. For integers 0 < r ⩽t < n, if Jn,t is [κ + κ/r, r]δ-RLC, then δ ⩾1 −rn/(r + 1)n−t.
Proof. Take a graph Jn,t with vertices partitioned into A and B as in eq. (6). An ordering with B ◁A shows
that κ = κ(Jn,t) = t. We claim that for every choice of colors lists for vertices in A, taken from the palette
[t + t/r], the probability that the chosen lists for B permit a proper list coloring is at most p := rn/(r + 1)n−t.
This will prove that δ ⩾1 −p.
To prove the claim, consider a particular choice of lists for A. Fix a partial coloring ψ of A consistent
with these lists. If ψ is not proper, there is nothing to prove. Otherwise, since A induces a clique, ψ must
assign t distinct colors to A. In order for a choice of lists for B to permit a proper extension of ψ to the entire
graph, every vertex of B must sample a color from the remaining t/r colors in the palette. Since r colors are
chosen per vertex, this event has probability at most
 
r ·
t/r
t + t/r
!|B|
=

r
r + 1
n−t
.
The claimed upper bound on p now follows by a union bound over the rt possible partial colorings ψ.
□
This easily leads to our combinatorial lower bound, given below. In reading the theorem statement, note
that the restriction on edge density strengthens the theorem.
Theorem 5.17. Let n be suﬃciently large and let m be such that n ⩽m ⩽n2/ log2 n. If every n-vertex graph
G with Θ(m) edges is [κ(G) + λ, c log n]1/3-RLC for some parameter λ and some constant c, then we must
have λ > κ(G)/(c log n).
Proof. Suppose not. Put t = ⌈m/n⌉, r = c log n, and consider the graph Jn,t deﬁned in eq. (6). By the bounds
on m, |E(Jn,t)| = t(t −1)/2 + t(n −t) = Θ(nt) = Θ(m). Put κ := κ(Jn,t). By assumption, Jn,t is [κ + κ/r, r]-RLC,
so Lemma 5.16 implies that
2
3 ⩽
rn
(r + 1)n−t =
 
1 −
1
r + 1
!n
(r + 1)t ⩽exp

−
n
r + 1 + t ln(r + 1)

.
Since t = O(n/ log2 n) and r = c log n, this is a contradiction for suﬃciently large n.
□
We remark that the above result rules out the possibility of using a palette sparsiﬁcation theorem along
the lines of Assadi et al. [ACK19] to obtain a semi-streaming coloring algorithm that uses fewer colors than
Algorithm 1 (with the setting ε = 1/ log n).
More generally, suppose we were willing to tolerate a weaker notion of palette sparsiﬁcation by sampling
O(logd n) colors per vertex, for some d ⩾1: this would increase the space complexity of an algorithm based
22


## Page 23


on such sparsiﬁcation by a polylog n factor. By Lemma 5.16, arguing as in Theorem 5.17, we would need to
spend at least κ + κ/Θ(logd n) colors. This is no better than the number of colors obtained using Algorithm 1
with the setting ε = 1/ logd n, which still maintains semi-streaming space. In fact, palette sparsiﬁcation does
not immediately guarantee a post-processing runtime that is better than exponential, because we need to color
the conﬂict graph in post-processing. Meanwhile, recall that Algorithm 1 has e
O(n) post-processing time via a
straightforward greedy algorithm. Furthermore, since there exist “hard” graphs Jn,t at all edge densities from
Θ(n) to Θ(n2/ log2 n), we cannot even hope for a semi-streaming palette-sparsiﬁcation-based algorithm that
might work only for sparse graphs or only for dense graphs.
Acknowledgement
We gratefully acknowledge several helpful discussions we have had with Sepehr Assadi (especially those that
called to our attention a nuance with the Congested Clique algorithm) and Deeparnab Chakrabarty.
References
[ABI86]
Noga Alon, L´aszl´o Babai, and Alon Itai. A fast and simple randomized parallel algorithm for
the maximal independent set problem. Journal of algorithms, 7(4):567–583, 1986.
[Abl96]
Farid Ablayev. Lower bounds for one-way probabilistic communication complexity and their
application to space complexity. Theor. Comput. Sci., 175(2):139–159, 1996.
[ACK19]
Sepehr Assadi, Yu Chen, and Sanjeev Khanna. Sublinear algorithms for (∆+ 1) vertex coloring.
In Proc. 30th Annual ACM-SIAM Symposium on Discrete Algorithms, page To Appear, 2019.
[Bar16]
Leonid Barenboim. Deterministic (∆+ 1)-coloring in sublinear (in ∆) time in static, dynamic,
and faulty networks. Journal of the ACM (JACM), 63(5):47, 2016.
[BB04]
Nicolas Barnier and Pascal Brisset. Graph coloring for air traﬃc ﬂow management. Annals of
operations research, 130(1-4):163–178, 2004.
[BB06]
Balabhaskar Balasundaram and Sergiy Butenko. Graph domination, coloring and cliques in
telecommunications. In Handbook of Optimization in Telecommunications, pages 865–890.
Springer, 2006.
[BCHN18] Sayan Bhattacharya, Deeparnab Chakrabarty, Monika Henzinger, and Danupon Nanongkai.
Dynamic algorithms for graph coloring. In Proc. 39th Annual ACM-SIAM Symposium on
Discrete Algorithms, pages 1–20, 2018.
[BCK+17]
Luis Barba, Jean Cardinal, Matias Korman, Stefan Langerman, Andr´e van Renssen, Marcel
Roeloﬀzen, and Sander Verdonschot. Dynamic graph coloring. In Workshop on Algorithms and
Data Structures, pages 97–108, 2017.
[BDH18]
Soheil Behnezhad, Mahsa Derakhshan, and Mohammad Taghi Hajiaghayi. Brief announcement:
Semi-mapreduce meets congested clique. CoRR, abs/1802.10297, 2018.
[BdW02]
Harry Buhrman and Ronald de Wolf. Complexity measures and decision tree complexity: a
survey. Theor. Comput. Sci., 288(1):21–43, 2002.
[BE10]
Leonid Barenboim and Michael Elkin. Sublogarithmic distributed mis algorithm for sparse
graphs using nash-williams decomposition. Distributed Computing, 22(5-6):363–379, 2010.
23


## Page 24


[BE11]
Leonid Barenboim and Michael Elkin. Deterministic distributed vertex coloring in polylogarith-
mic time. Journal of the ACM (JACM), 58(5):23, 2011.
[BE13]
Leonid Barenboim and Michael Elkin. Distributed Graph Coloring: Fundamentals and Recent
Developments. Synthesis Lectures on Distributed Computing Theory. Morgan & Claypool
Publishers, 2013.
[BEPS16]
Leonid Barenboim, Michael Elkin, Seth Pettie, and Johannes Schneider.
The locality of
distributed symmetry breaking. Journal of the ACM (JACM), 63(3):20, 2016.
[BKS17]
Paul Beame, Paraschos Koutris, and Dan Suciu. Communication steps for parallel query
processing. Journal of the ACM (JACM), 64(6):40, 2017.
[BKV12]
Bahman Bahmani, Ravi Kumar, and Sergei Vassilvitskii. Densest subgraph in streaming and
mapreduce. International Conference on Very Large Data Bases, 5(5):454–465, 2012.
[CAC+81]
Gregory J Chaitin, Marc A Auslander, Ashok K Chandra, John Cocke, Martin E Hopkins, and
Peter W Markstein. Register allocation via coloring. Computer languages, 6(1):47–57, 1981.
[CFG+18]
Yi-Jun Chang, Manuela Fischer, Mohsen Ghaﬀari, Jara Uitto, and Yufan Zheng. Simple
graph coloring algorithms for congested clique and massively parallel computation. CoRR,
abs/1808.08419, 2018.
[CH90]
Fred C Chow and John L Hennessy. The priority-based coloring approach to register allocation.
ACM Transactions on Programming Languages and Systems (TOPLAS), 12(4):501–536, 1990.
[Cha82]
Gregory J Chaitin. Register allocation & spilling via graph coloring. In ACM Sigplan Notices,
volume 17, pages 98–105, 1982.
[CLP18]
Yi-Jun Chang, Wenzheng Li, and Seth Pettie. An optimal distributed (∆+ 1)-coloring algorithm.
In Proc. 50th Annual ACM Symposium on the Theory of Computing, pages 445–456, 2018.
[CRT05]
Bernard Chazelle, Ronitt Rubinfeld, and Luca Trevisan. Approximating the minimum spanning
tree weight in sublinear time. SIAM Journal on computing, 34(6):1370–1379, 2005.
[DG04]
Jeﬀrey Dean and Sanjay Ghemawat. Mapreduce: Simpliﬁed data processing on large clusters. In
6th Symposium on Operating System Design and Implementation (OSDI 2004), San Francisco,
California, USA, December 6-8, 2004, pages 137–150, 2004.
[FHK16]
Pierre Fraigniaud, Marc Heinrich, and Adrian Kosowski. Local conﬂict coloring. In Proc. 57th
Annual IEEE Symposium on Foundations of Computer Science, pages 625–634, 2016.
[FK96]
Uriel Feige and Joe Kilian. Zero knowledge and the chromatic number. In Annual IEEE
Conference on Computational Complexity, page 278, 1996.
[FKM+05] Joan Feigenbaum, Sampath Kannan, Andrew McGregor, Siddharth Suri, and Jian Zhang. On
graph problems in a semi-streaming model. Theor. Comput. Sci., 348(2–3):207–216, 2005.
Preliminary version in Proc. 31st International Colloquium on Automata, Languages and
Programming, pages 531–543, 2004.
[GI10]
Anna C. Gilbert and Piotr Indyk. Sparse recovery using sparse matrices. Proceedings of the
IEEE, 98(6):937–947, 2010.
24


## Page 25


[GL17]
Mohsen Ghaﬀari and Christiana Lymouri. Simple and near-optimal distributed coloring for
sparse graphs. In 31st International Symposium on Distributed Computing (DISC 2017), page 20,
2017.
[Gol17]
Oded Goldreich. Introduction to Property Testing. Cambridge University Press, 2017.
[GR08]
Oded Goldreich and Dana Ron.
Approximating average parameters of graphs.
Random
Structures & Algorithms, 32(4):473–493, 2008.
[HLL18]
Nicholas J. A. Harvey, Christopher Liaw, and Paul Liu. Greedy and local ratio algorithms in the
mapreduce model. In Proceedings of the 30th on Symposium on Parallelism in Algorithms and
Architectures, SPAA 2018, Vienna, Austria, July 16-18, 2018, pages 43–52, 2018.
[HSS16]
David G Harris, Johannes Schneider, and Hsin-Hao Su. Distributed (∆+ 1)-coloring in sublog-
arithmic rounds. In Proc. 48th Annual ACM Symposium on the Theory of Computing, pages
465–478, 2016.
[Joh99]
¨Ojvind Johansson. Simple distributed ∆+ 1-coloring of graphs. Information Processing Letters,
70(5):229–232, 1999.
[KP06]
Subhash Khot and Ashok Kumar Ponnuswami. Better inapproximability results for maxclique,
chromatic number and min-3lin-deletion. In International Colloquium on Automata, Languages
and Programming, pages 226–237, 2006.
[KP11]
Kishore Kothapalli and Sriram Pemmaraju. Distributed graph coloring in a few rounds. In Proc.
30th ACM Symposium on Principles of Distributed Computing, pages 31–40, 2011.
[Lei79]
Frank Thomson Leighton. A graph coloring algorithm for large scheduling problems. Journal
of research of the national bureau of standards, 84(6):489–506, 1979.
[Len13]
Christoph Lenzen. Optimal deterministic routing and sorting on the congested clique. In Proc.
32nd ACM Symposium on Principles of Distributed Computing, pages 42–50, 2013.
[LPPP05]
Zvi Lotker, Boaz Patt-Shamir, Elan Pavlov, and David Peleg. Minimum-weight spanning tree
construction in O(log log n) communication rounds. SIAM J. Comput., 35(1):120–131, 2005.
[LS86]
Vahid Lotﬁand Sanjiv Sarin. A graph coloring algorithm for large scale scheduling problems.
Computers & operations research, 13(1):27–32, 1986.
[Lub86]
Michael Luby. A simple parallel algorithm for the maximal independent set problem. SIAM J.
Comput., 15(4):1036–1053, 1986.
[MOT14]
Farnaz Moradi, Tomas Olovsson, and Philippas Tsigas. A local seed selection algorithm for
overlapping community detection. In 2014 IEEE/ACM International Conference on Advances in
Social Networks Analysis and Mining (ASONAM 2014), pages 1–8, 2014.
[MTVV15] Andrew McGregor, David Tench, Sofya Vorotnikova, and Hoa T Vu. Densest subgraph in
dynamic graph streams. In International Symposium on Mathematical Foundations of Computer
Science, pages 472–482, 2015.
[Par18]
Merav Parter. (∆+1) coloring in the congested clique model. In Proc. 45th International
Colloquium on Automata, Languages and Programming, pages 160:1–160:14, 2018.
25


## Page 26


[PL96]
Taehoon Park and Chae Y Lee. Application of the graph coloring algorithm to the frequency
assignment problem. Journal of the Operations Research society of Japan, 39(2):258–265, 1996.
[PR07]
Michal Parnas and Dana Ron. Approximating the minimum vertex cover in sublinear time and a
connection to distributed algorithms. Theoretical Computer Science, 381(1-3):183–196, 2007.
[PS96]
Alessandro Panconesi and Aravind Srinivasan. On the complexity of distributed network
decomposition. Journal of Algorithms, 20(2):356–374, 1996.
[PS18]
Merav Parter and Hsin-Hao Su. Randomized (Delta+1)-Coloring in O(log* Delta) Congested
Clique Rounds. In Proc. 32nd International Symposium on Distributed Computing, pages
39:1–39:18, 2018.
[RA15]
Ryan A. Rossi and Nesreen K. Ahmed. The network data repository with interactive graph
analytics and visualization. In Proceedings of the Twenty-Ninth AAAI Conference on Artiﬁcial
Intelligence, 2015.
[Raz92]
Alexander Razborov. On the distributional complexity of disjointness. Theor. Comput. Sci.,
106(2):385–390, 1992. Preliminary version in Proc. 17th International Colloquium on Automata,
Languages and Programming, pages 249–253, 1990.
[RSV15]
Jaikumar Radhakrishnan, Saswata Shannigrahi, and Rakesh Venkat. Hypergraph two-coloring
in the streaming model. arXiv preprint arXiv:1512.04188, 2015.
[SW10]
Johannes Schneider and Roger Wattenhofer. A new technique for distributed symmetry breaking.
In Proc. 29th ACM Symposium on Principles of Distributed Computing, pages 257–266, 2010.
[TZP18]
Simon Thevenin, Nicolas Zuﬀerey, and Jean-Yves Potvin. Graph multi-coloring for a job
scheduling application. Discrete Applied Mathematics, 234:218–235, 2018.
[Zuc06]
David Zuckerman. Linear degree extractors and the inapproximability of max clique and
chromatic number. In Proc. 38th Annual ACM Symposium on the Theory of Computing, pages
681–690, 2006.
26

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]

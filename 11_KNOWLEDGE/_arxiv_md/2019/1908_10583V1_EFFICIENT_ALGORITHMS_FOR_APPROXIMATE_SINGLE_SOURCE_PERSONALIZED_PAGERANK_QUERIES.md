---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1908.10583v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1908.10583v1_Efficient_Algorithms_for_Approximate_Single-Source_Personalized_PageRank_Queries

> Source: 1908.10583v1_Efficient_Algorithms_for_Approximate_Single-Source_Personalized_PageRank_Queries.pdf

> Pages: 37

---


## Page 1


1
Efficient Algorithms for Approximate Single-Source
Personalized PageRank Queries
SIBO WANG, The Chinese University of Hong Kong
RENCHI YANG, Nanyang Technological University
RUNHUI WANG, Rutgers University
XIAOKUI XIAO, National University of Singapore
ZHEWEI WEI∗, Renmin University of China
WENQING LIN, Tencent
YIN YANG, Hamad Bin Khalifa University
NAN TANG, Qatar Computing Research Institute, HBKU
Given a graph G, a source node s and a target node t, the personalized PageRank (PPR) of t with respect to s is
the probability that a random walk starting from s terminates at t. An important variant of the PPR query is
single-source PPR (SSPPR), which enumerates all nodes in G, and returns the top-k nodes with the highest PPR
values with respect to a given source s. PPR in general and SSPPR in particular have important applications in
web search and social networks, e.g., in Twitter’s Who-To-Follow recommendation service. However, PPR
computation is known to be expensive on large graphs, and resistant to indexing. Consequently, previous
solutions either use heuristics, which do not guarantee result quality, or rely on the strong computing power
of modern data centers, which is costly.
Motivated by this, we propose effective index-free and index-based algorithms for approximate PPR
processing, with rigorous guarantees on result quality. We first present FORA, an approximate SSPPR solution
that combines two existing methods Forward Push (which is fast but does not guarantee quality) and Monte
Carlo Random Walk (accurate but slow) in a simple and yet non-trivial way, leading to both high accuracy
and efficiency. Further, FORA includes a simple and effective indexing scheme, as well as a module for top-k
selection with high pruning power. Extensive experiments demonstrate that the proposed solutions are orders
of magnitude more efficient than their respective competitors. Notably, on a billion-edge Twitter dataset,
FORA answers a top-500 approximate SSPPR query within 1 second, using a single commodity server.
CCS Concepts: • Mathematics of computing →Graph algorithms.
Additional Key Words and Phrases: Personalized PageRank, Forward Push, Random Walk
∗Corresponding author
Sibo Wang is supported by CUHK Direct Grant No. 4055114, CUHK University Startup Grant No. 4930911 and No. 5501570,
and a donation from Tencent. Xiaokui Xiao is supported by MOE, Singapore under grant MOE2015-T2-2-069, and by NUS,
Singapore under an SUG. Zhewei Wei is supported by in part by National Natural Science Foundation of China (No. 61832017
and No. 61732014).
Authors’ addresses: Sibo Wang, swang@se.cuhk.edu.hk,The Chinese University of Hong Kong; Renchi Yang, yang0461@
ntu.edu.sg,Nanyang Technological University; Runhui Wang, runhui.wang@rutgers.edu,Rutgers University; Xiaokui
Xiao, xkxiao@nus.edu.sg,National University of Singapore; Zhewei Wei, zhewei@ruc.edu.cn,Renmin University of China;
Wenqing Lin, edwlin@tencent.com,Tencent; Yin Yang, yyang@hkbu.edu.qa,Hamad Bin Khalifa University; Nan Tang,
ntang@hkbu.edu.qa,Qatar Computing Research Institute, HBKU.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and
the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2019 Association for Computing Machinery.
0362-5915/2019/8-ART1 $15.00
https://doi.org/10.1145/nnnnnnn.nnnnnnn
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.
arXiv:1908.10583v1  [cs.SI]  28 Aug 2019


## Page 2


1:2
Wang et al.
ACM Reference Format:
Sibo Wang, Renchi Yang, Runhui Wang, Xiaokui Xiao, Zhewei Wei, Wenqing Lin, Yin Yang, and Nan Tang.
2019. Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries. ACM Trans. Datab.
Syst. 1, 1, Article 1 (August 2019), 37 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn
1
INTRODUCTION
Personalized PageRank (PPR) is a fundamental operation first proposed by Google [Page et al. 1999],
a major search engine. Specifically, given a graphG and a pair of nodes s,t inG, the PPR value π(s,t)
is defined as the probability that a random walk starting from s (called the source node) terminates
at t (the target node), which reflects the importance of t with respect to s. One particularly useful
variant of PPR is the single-source PPR (SSPPR), which takes as input a source node s and a parameter
k, and returns the top-k nodes in G with the highest PPR values with respect to s. According to a
recent paper [Gupta et al. 2013], Twitter, a leading microblogging service, applies SSPPR in their
Who-To-Follow application, which recommends to a user s (who is a node in the social graph) a
number of other users (with high PPR values with respect to s) that user s might want to follow.
Clearly, such an application computes SSPPR for every user in the social graph on a regular basis.
Hence, accelerating PPR computation may lead to improved user experience (e.g., faster response
time), as well as reduced operating costs (e.g., lower power consumption in the data center).
Similar to PageRank [Page et al. 1999], PPR computation on a web-scale graph is immensely
expensive, which involves extracting eigenvalues of a n ×n matrix, where n is the number of nodes
that can reach millions or even billions in a social graph. Meanwhile, unlike PageRank, PPR values
cannot be easily materialized: since each pair of source/target nodes lead to a different PPR value,
storing all possible PPR values requires O(n2) space, which is infeasible for large graphs. For these
reasons, much previous work focuses on approximate PPR computation (defined in Section 2.1),
which provides a controllable tradeoff between the execution time and result accuracy. Meanwhile,
compared to heuristic solutions, approximate PPR provides rigorous guarantees on result quality.
However, even under the approximate PPR definition, SSPPR computation remains a challenging
problem, since it requires sifting through all nodes in the graph. To our knowledge, the majority of
existing methods (e.g., [Lofgren et al. 2016, 2014; Wang et al. 2016]) focus on approximate pair-wise
(i.e., with given source and target nodes) PPR computations. A naive solution is to compute pair-
wise PPR π(s,v) for each possible target node v, and subsequently applies top-k selection. Clearly,
the running time of this approach grows linearly to the number of nodes in the graph, which is
costly for large graphs.
Motivated by this, we propose FORA (short for FOward Push and RAndom Walks), an efficient
algorithm for approximate SSPPR computation. The basic idea of FORA is to combine two existing
solutions in a simple and yet non-trivial way, which are (i) Forward Push [Andersen et al. 2007],
which can either computes the exact SSPPR results at a high cost, or terminate early but with no
guarantee at all on the result quality, and (ii) Monte Carlo [Fogaras et al. 2005], which samples and
executes random walks and provides rigorous guarantees on the accuracy of SSPPR results, but is
rather inefficient. In fact, this idea is so effective that even without any indexing, basic FORA already
outperforms its main competitors BiPPR [Lofgren et al. 2016] and HubPPR [Wang et al. 2016]. Then,
we describe a simple and effective indexing scheme for FORA, as well as a novel algorithm for
top-k selection. Extensive experiments using several real graphs demonstrate that FORA is more
than two orders of magnitude faster than BiPPR, and more than an order of magnitude faster than
HubPPR. In particular, on a billion-edge Twitter graph, FORA answers top-500 SSPPR query within
1 second, using a single commodity server.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 3


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:3
2
BACKGROUND
2.1
Problem Definition
Let G = (V, E) be a directed graph. In case the input graph is undirected, we simply convert it to a
directed one by treating each edge as two directed edges of opposing directions. Given a source node
s ∈V and a decay factor α, a random walk (or more precisely, random walk with restart [Fujiwara
et al. 2012]) from s is a traversal of G that starts from s and, at each step, either (i) terminates at the
current node with α probability, or (ii) proceeds to a randomly selected out-neighbor of the current
node. For any node v ∈V , the personalized PageRank (PPR) π(s,v) of v with respect to s is then
the probability that a random walk from s terminates at v [Page et al. 1999].
A single-source PPR (SSPPR) query takes as input a graph G, a source node s, and a parameter
k, and returns the top-k nodes with the highest PPR values with respect to s, together with their
respective PPR values. This paper focuses on approximate SSPPR processing, and we first define a
simpler version of the approximate SSPPR without top-k selection (called approximate whole-graph
SSPPR), as follows.
Definition 2.1 (Approximate Whole-Graph SSPPR). Given a source node s, a threshold δ, an error
boundϵ, and a failure probabilitypf , an approximate whole-graph SSPPR query returns an estimated
PPR ˆπ(s,v) for each node v ∈V , such that for any π(s,v) > δ,
|π(s,v) −ˆπ(s,v)| ≤ϵ · π(s,v)
(1)
holds with at least 1 −pf probability.
The above definition is consistent with existing work, e.g., [Lofgren et al. 2016, 2014; Wang et al.
2016]. Next we define the approximate top-k SSPPR, as follows.
Definition 2.2 (Approximate Top-k SSPPR). Given a source node s, a threshold δ, an error bound
ϵ, a failure probability pf , and a positive integer k, an approximate top-k SSPPR query returns
a sequences of k nodes, v1,v2, · · · ,vk, such that with probability 1 −pf , for any i ∈[1,k] with
π(s,v∗
i ) > δ,
ˆπ(s,vi) ≥(1 −ϵ)π(s,vi)
(2)
π(s,vi) ≥(1 −ϵ) · π(s,v∗
i )
(3)
hold with at least 1 −pf probability, where v∗
i is the node whose actual PPR with respect to s is the
i-th largest.
Note that Equation 2 ensures the accuracy of the estimated PPR values, while Equation 3
guarantees that the i-th result returned has a PPR value close to the i-th largest PPR score. This
definition is consistent with previous work [Wang et al. 2016]. Following previous work [Lofgren
et al. 2016, 2014; Wang et al. 2016], we assume that δ = O(1/n), where n is the number of nodes in
G. The intuition is that, we provide approximation guarantees for nodes with above-average PPR
values.
In addition, most applications of personalized PageRank concern web graphs and social networks,
in which case the underlying input graphs are generally scale-free. That is, for any k ≥1, the
fraction f (k) of nodes in G that have k edges satisfies
f (k) = c · k−γ ,
(4)
where γ is a parameter with 2 ≤γ ≤3, and c is a constant smaller than 1. It can be verified that, in
a scale-free graph with 2 ≤γ ≤3, the average node degree m/n = O(logn). We will analyze the
asymptotic performance of our algorithm on both general graphs and scale-free graphs. Table 1
lists the frequently-used notations throughout the paper.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 4


1:4
Wang et al.
Table 1. Frequently used notations.
Notation Description
G=(V, E)
The input graph G with node set V and edge set E
n,m
The number of nodes and edges in G, respectively
N out(v)
The set of out-neighbors of node v
N in(v)
The set of in-neighbors of node v
π(s,t)
The exact PPR value of t with respect to s
α
The probability that a random walk terminates at a step
δ,ϵ,pf
Parameters of an approximate PPR query, as in Definitions 2.1 and 2.2
rmax
The residue threshold for local update
r(s,v)
The residue of v during a local update process from s
π ◦(s,v)
The reserve of v during a local update process from s
rsum
The sum of all nodes’ residues during a local update process from s
π(s,v∗
k)
The k-th largest PPR value with respect to s
Remark. Our algorithms can also handle SSPPR queries where the source s is not fixed but sampled
from a node distribution. Interested readers are referred to Section 6.3 for details.
2.2
Main Competitors
Monte-Carlo. A classic solution for approximate PPR processing is the Monte-Carlo (MC) approach
[Fogaras et al. 2005]. Given a source node s, MC generates ω random walks from s, and it records,
for each node v, the fraction of random walks f (v) that terminate at v. It then uses f (v) as an
estimation of the PPR ˆπ(s,v) of v with respect to s. According to [Fogaras et al. 2005], MC satisfies
Definition 2.1 with a sufficiently large number of random walks: ω = Ω
 log (1/pf )
ϵ2δ

. According to
Refs. [Lofgren et al. 2016, 2014; Wang et al. 2016] as well as our experiments in Section 8, MC is
rather inefficient. Specifically, the time complexity of MC is O
 log (1/pf )
ϵ2δ

. As will be explained later
in Section 3.2, when δ = O(1/n) and the graph is scale-free, in which case m/n = O(logn), this
time complexity is a factor of 1/ϵ larger than that of FORA even without indexing or top-k pruning.
BiPPR and HubPPR. BiPPR [Lofgren et al. 2016] and its successor HubPPR [Wang et al. 2016] are
currently the states of the art for answering pairwise PPR queries, in which both the source node
s and the target node t are given, and the goal is to approximate the PPR value π(s,t) of t with
respect to s. The main idea of BiPPR is a bi-direction search on the input graph G. The forward
direction simply samples and executes random walks, akin to MC described above. Unlike MC,
however, BiPPR requires a much smaller number of random walks, thanks to additional information
provided by the backward search.
The backward search in BiPPR (dubbed as reverse push) is originally proposed in [Andersen
et al. 2007], and is rather complicated. In a nutshell, the reverse push starts from the target node
t, and recursively propagate residue and reserve values along the reverse directions of edges in G.
Initially, the residue is 1 for node t, and 0 for all other nodes. The original reverse push [Andersen
et al. 2007] requires complete propagation until the residues of all nodes become very small, which
is rather inefficient as pointed out in [Lofgren et al. 2016]. BiPPR performs the same backward
propagations, but terminates early when the residues of all nodes are below a pre-defined threshold.
Then, the method performs forward search, i.e., random walks, utilizing the residue and reserve
information computed during backward search. The main tricky part in BiPPR is how to set this
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 5


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:5
ALGORITHM 1: Forward Push
Input: Graph G, source node s, probability α, residue threshold rmax
Output: π◦(s,v), r(s,v) for all v ∈V
1 r(s,s) ←1;r(s,v) ←0 for all v , s;
2 π◦(s,v) ←0 for all v;
3 while ∃v ∈V such that r(s,v)/|N out (v)| > rmax do
4
for each u ∈Nout (v) do
5
r(s,u) ←r(s,u) + (1 −α) ·
r(s,v)
|N out (v)|
6
π◦(s,v) ←π◦(s,v) + α · r(s,v);
7
r(s,v) ←0;
residue threshold to minimize computation costs, while satisfying Inequality 1. Intuitively, if the
residue threshold is set too high, then the forward search requires numerous random walks to
reach the approximation guarantee; conversely, if the residue threshold is too low, then the cost of
backward search dominates. Ref. [Lofgren et al. 2016] provides a careful analysis, and reports that
a residue threshold of O

ϵ ·
q
m·δ
n·log (1/pf )

strikes a good balance between forward and backward
searches, and achieves a low overall cost for pair-wise PPR computation.
To extend BiPPR to SSPPR, one simple method is to enumerate all nodes in G, and compute the
PPR value for each of them with respect to the source node s. The problem, however, is that the
residue threshold designed in [Lofgren et al. 2016] is not optimized for SSPPR, leading to poor
performance. To explain, observe that applying BiPPR for SSPPR involves one backward search at
each node in G, but only one single forward search from s. Therefore, we improve the performance
of BiPPR by tuning down overhead of each backward search at the cost of a less efficient forward
search. This optimization turns out to be non-trivial, and we present it in Section 6.1. Nevertheless,
the properly optimized version of BiPPR still involves high costs since it either (i) degrades to the
Monte-Carlo approach if the residue threshold is large or (ii) incurs a large number of backward
searches if the residue threshold is small.
HubPPR [Wang et al. 2016] is an index structure based on BiPPR that features an improved
algorithm for top-k queries. Since HubPPR inherits the deficiencies of the BiPPR, it is not suitable
for SSPPR, either. We will demonstrate this in our experiments in Section 8.
Forward Push. Forward Push [Andersen et al. 2006] is an earlier solution that is not as efficient
as BiPPR and HubPPR. We describe it in detail here since the proposed solution FORA uses its
components. Specifically, Forward Push can compute the exact PPR values at a high cost. It can also
be configured to terminate early, but without any guarantee on result quality. Algorithm 1 shows
the pseudo-code of Forward Push for whole-graph SSPPR processing. It takes as input G, a source
node s, a probability value α, and a threshold rmax; its output consists of two values for each node
v in G: a reserve π ◦(s,v) and a residue r(s,v). The reserve π ◦(s,v) is an approximation of π(s,v),
while the residue r(s,v) is a by-product of the algorithm. In the beginning of the algorithm, it sets
r(s,s) = 1 and π ◦(s,s) = 0, and sets r(s,v) = π ◦(s,v) = 0 for any v , s (Lines 1-2 in Algorithm 1).
Subsequently, the residue of s is converted into other nodes’ reserves and residues in an iterative
process (Lines 3-7).
Specifically, in each iteration, the algorithm first identifies every node v with
r(s,v)
|N out (v)| > rmax,
where N out denotes the set of out-neighbors of v (Line 3). After that, it propagates part of v’s
residue to each u of v’s out-neighbors, increasing u’s residue by (1−α) ·
r(s,v)
|N out (v)| . Then, it increases
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 6


1:6
Wang et al.
v’s reserve by α ·r(s,v), and resets v’s residue to r(s,v) = 0. This iterative process terminates when
every node v has
r(s,v)
|N out (v)| ≤rmax (Line 3).
Andersen et al. [Andersen et al. 2006] show that Algorithm 1 runs in O(1/rmax) time, and that
the reserve π ◦(s,v) can be regarded as an estimation of π(s,v). This estimation, however, does not
offer any worst-case assurance in terms of absolute or relative error. As a consequence, Algorithm 1
itself is insufficient for addressing the problem formulated in Definitions 2.1 and 2.2.
TopPPR. Most recently, TopPPR [Wei et al. 2018] is proposed to combine the Forward Push,
Monte-Carlo, and the backward search to process the top-k queries. The main idea is to use the
Filter-Refinement paradigm so as to accelerate the top-k query processing. They first use the
Forward Push and Monte-Carlo approach to derive the upper and lower bound of the PPR π(s,v)
for each target nodev. It further maintains a setC of candidates that are the potential top-k answers
by examining the upper and lower bound of each node. For example, if a node v has an upper
bound π(s,v) that is larger than that of the k-th largest lower bound. Then we know this node will
not be in the top-k answer. When the candidate set is sufficiently small, backward search is started
from these node and refine the upper bound and lower bound of the candidate nodes adaptively.
The algorithm explores the power-law property and achieves a time complexity of O(k
1
4 ·n
3
4 ·log n
√
дapρ) ),
where дapρ is a value that quantifies the difference between the top-k and non-top-k PPR values,
and ρ is a precision parameter to guarantee that at least ρ fraction of the returned nodes are among
the true top-k answers. Notice that дapρ should be no larger than π(s,v∗
k) where π(s,v∗
k) is the k-th
largest PPR with respect to s. Therefore, their time complexity can be written as O(k
1
4 ·n
3
4 ·log n
√
π(s,v∗
k )) ). On
general graphs, the time complexity will degrade to O(m+n·log n
√
π(s,v∗
k ) ). As we will see in Section 5.2 and
Section 8, our top-k algorithm achieves both better theoretical result and practical performance.
Comparison with the conference version [Wang et al. 2017]. We make the following new
contributions over the conference version.
• For whole-graph SSPPR queries, we revised the time complexity analysis to derive a refined
bound (Section 3.2). Then, in Section 4, we further present optimization techniques for whole-
graph SSPPR queries. With the new optimization technique, our index-free method improves
over the solution in [Wang et al. 2017] by 2x. Our new index-based method improves over
the index-based solution in [Wang et al. 2017] by at least 2x and up to 3x with 2x space
consumption, which demonstrates the effectiveness of the new algorithm and a good trade-off
of the new algorithms between the space consumption and query efficiency.
• For top-k SSPPR queries, the solution proposed in [Wang et al. 2017] has a worst time
complexity similar to the whole-graph SSPPR queries. In this paper, we derive a new top-k
algorithm in Section 5.2, whose time complexity depends on the k-th largest PPR value,
denoted as π(s,v∗
k). When π(s,v∗
k) is a constant, we then improve over the whole-graph
SSPPR query by O(1/n); when π(s,v∗
k) is O(1/n), then the time complexity of the top-k
algorithm is identical to that of the whole-graph SSPPR algorithm. Since the k-th largest
PPR is typically in between O(1) and O(1/n), the new proposed algorithm improves over the
solution proposed in [Wang et al. 2017], and is shown to outperform the solution in [Wang
et al. 2017] by around 5x in our experimental evaluation.
• In Section 6, we further extend our results to global PageRank. The results show that it
outperforms the classic Monte-Carlo approach and the Power-Iteration method. In addition,
our new top-k algorithm can be further used to return the top-k nodes with the hightest
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 7


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:7
Table 2. Comparison of approximate whole-graph SSPPR and top-k algorithms with 1 −1/n success proba-
bility (Ref. Table 1 for the definition of ϵ,δ, and π(s,v∗
k)).
Algorithm
Space Overhead
Query Time
whole-graph
Top-k
MC
0
O
 log n
δ ·ϵ2

O

log n
π(s,v∗
k )ϵ2

[Fogaras et al. 2005]
(Using our top-k algorithm)
BiPPR
0
O

1
ϵ
q
mn·log n
δ

[Lofgren et al. 2016]
HubPPR
O(n + m)
O

1
ϵ
q
mn·log n
δ

[Wang et al. 2016]
TopPPR
0
N.A.
O(m+n·log n
q
π(s,v∗
k ) )
(general graphs)
[Wei et al. 2018]
O(k
1
4 ·n
3
4 ·log n
q
π(s,v∗
k ) )
(power-law graphs)
FORA
0
O(min{
√
m·log n
ϵ ·
√
δ
,
O(min{
√
m log n
ϵ ·
q
π(s,v∗
k ),
FORA+
O(min{n +
1
ϵ ·
√
δ
q
m log (1/pf ),m})
log n
ϵ2·δ })
log n
ϵ2·π(s,v∗
k ) })
global PageRank with a time complexity that linearly depends on the inverse of the k-th
largest global PageRank.
• In the experimental evaluation, we have added four game social networks from Tencent
Games to examine the effectiveness of our algorithms in real applications and 2 large syn-
thetic datasets to examine the scalability of our proposed algorithms. Extensive experiments
demonstrate that our solution is also effective on real social networks and is scalable to huge
graphs with up to 8.6 billion edges.
Table 2 list the time complexity and space consumption of all approximate algorithms to provide
ϵ relative error guarantee for PPR values no smaller than δ with at least 1 −1/n probability. As we
can see, the proposed FORA/FORA+ achieves the best time complexity for both the whole-graph
SSPPR and top-k queries.
3
FORA
This section presents the proposed FORA algorithm. We first describe a simpler version of FORA
for whole-graph SSPPR (Definition 2.1) without indexing in Sections 3.1 and Sections 3.2. Then,
we present the indexing scheme of FORA in Section 3.3. We present optimization techniques for
whole-graph SSPPR in Section 4 and top-k query in Section 5.
3.1
Main Idea
As reviewed in Section 2.2, (i) MC is inefficient due to a large number of random walks required
to satisfy the approximation guarantee, (ii) BiPPR and HubPPR either degrade to MC, or require
fewer forward random walks but still incur high cost due to numerous backward search operations,
and (iii) Forward Push with early termination provides no formal guarantee on result quality. The
proposed solution FORA can be understood as a combination of these methods. In particular, FORA
first performs Forward Push with early termination, and subsequently runs random walks. Similar
to BiPPR and HubPPR, FORA utilizes information obtained through Forward Push to significantly
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 8


1:8
Wang et al.
cut down the number of required random walks while satisfying the same result quality guarantees.
But unlike BiPPR and HubPPR, in FORA there is a single invocation of Forward Push starting from
the source node s, while BiPPR and HubPPR invokes numerous backward search operations.
Novelty. The main difference between the proposed approach and BiPPR/HubPPR is that the former
combines forward push and MC, whereas the latter uses MC with backward propagation. The
proposed idea (i.e., using forward instead of backward push) is indeed natural, and highly effective
as shown in experiments (Section 8). Intuitively, forward push limits the search to nodes in the
vicinity of the source node, which is more efficient for SSPPR compared to backward propagation,
since the latter involves numerous nodes far from the source, as explained in Sections 2.2 (which
explains BiPPR).
Combining forward push with MC, however, is far from straightforward. The devil is in the
details. Specifically, in backward propagation, the residue r(v,t) for a given node v is bounded by
rmax, which is a controllable parameter (t is the destination node). In Forward Push (Algorithm
1), the corresponding concept is r(s,v) (s being the source node), which depends on both rmax
and the out-degree of v, which can be as large as O(n) in the worst case. The proposed solution
addresses this challenge with a novel mechanism that utilizes rsum (Algorithm 2), whose correctness
is rigorously established in this section. The novelty of our method lies in the fact that we realize
a natural, effective and yet challenging combination of forward push and MC with a non-trivial
algorithmic design, explained below.
Details. Specifically, the reason that Forward Push with early termination fails to obtain any result
quality guarantee is that it uses π ◦(s,v) to approximate π(s,v), and yet, the two values are not
guaranteed to be close. To mitigate this deficiency, we aim to utilize the residue r(s,v) to improve
the accuracy of π ◦(s,v). Towards this end, we utilize the following result from [Andersen et al.
2006]:
π(s,t) = π ◦(s,t) +
Õ
v ∈V
r(s,v) · π(v,t),
(5)
for any s, t, v in G. Our idea is to derive a rough approximation of π(v,t) for each node v (denoted
as π ′(v,t)), and then combine it with the reserve of each node to compute an estimation of π(s,t):
π(s,t) = π ◦(s,t) +
Õ
v ∈V
r(s,v) · π ′(v,t).
In particular, we derive π ′(v,t) by performing a number of random walks from v, and set π ′(v,t)
to the fraction of walks that ends at t.
It remains to answer two key questions in FORA: (i) how many random walks do we need for
each node v? and (ii) how should we set the residue threshold rmax in Forward Push? It turns out
that although the FORA algorithm itself is simple, deriving the proper values for its parameters is
rather challenging, since they must optimize efficiency while satisfying the result quality guarantee.
In the following, we first present the complete FORA and answer question (i); then we answer
question (ii) in Section 3.2.
Algorithm 2 illustrates the pseudo-code of FORA. Given G, a source node s, a probability value
α, and a residue threshold rmax, FORA first invokes Algorithm 2 on G to obtain a reserve π ◦(s,vi)
and a residue r(s,vi) for each node vi (Line 1 in Algorithm 2). After that, it computes the total
residue of all nodes rsum, based on which it derives a value ω that will be used to decide the number
of random walks required from each node vi (Line 2). Then, it initializes the PPR estimation of each
vi to be ˆπ(s,vi) = π ◦(s,vi), and it proceeds to inspect the nodes whose residues are larger than
zero (Line 3-4).
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 9


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:9
ALGORITHM 2: FORA for Whole-Graph SSPPR
Input: Graph G, source node s, probability α, threshold rmax, relative error threshold ϵ
Output: Estimated PPR ˆπ(s,v)for all v ∈V
1 Invoke Algorithm 1 with input parameters G, s, α, and rmax;
2 let r(s,vi), π◦(s,vi) be the returned residue and reserve of node vi;
3 Let rsum = Í
vi ∈V r(s,vi) and ω = rsum · (2ϵ/3+2)·log (2/pf )
ϵ2·δ
;
4 Let ˆπ(s,vi) = π◦(s,vi) for all vi ∈V ;
5 for vi ∈V with r(s,vi) > 0 do
6
Let ωi = ⌈r(s,vi) · ω/rsum⌉;
7
Let ai = r(s,vi)
rsum · ω
ωi ;
8
for i = 1 to ωi do
9
Generate a random walk W from vi;
10
Let t be the end point of W ;
11
ˆπ(s,t)+ = ai ·rsum
ω
;
12 return ˆπ(s,v1), · · · , ˆπ(s,vn);
For each vi of those nodes, it performs ωi random walks from vi, where
ωi =
r(s,vi)
rsum
· ω

.
If a random walk ends at a node t, then FORA increases ˆπ(s,vi) by ai ·rsum
ω
, where
ai = r(s,vi)
rsum
· ω
ωi
.
After all vi are processed, the algorithm returns ˆπ(s,vi) as the approximated PPR value for vi (Line
11).
To explain why FORA can provide accurate results, let us consider the ωi random walks that it
generates from a node vi. Let Xj(t) be a Bernoulli variable that takes value 1 if the j-th random
walk terminates at t, and value 0 otherwise. By definition,
E[Xj] = π(vi,t).
Then, based on the definition of ω, ωi, and ai, we have
E
"
rsum
ω
·
ωi
Õ
j=1
 ai · Xj

#
= r(s,vi) · π(vi,t).
(6)
Observe that rsum
ω
· Íωi
j=1
 ai · Xj
 is exactly the amount of increment that ˆπ(s,t) receives when
FORA processes vi (see Lines 7-10 in Algorithm 2). We denote this increment as ψi. It follows that
E
" n
Õ
i=1
ψi
#
=
n
Õ
i=1
r(s,vi) · π(vi,t).
(7)
Combining Equations 5 and 7, we can see that FORA returns, for each node v, an estimated PPR
ˆπ(s,v) whose expectation equals π(s,v). Next, we will show that ˆπ(s,v) is very close to π(s,v)
with a high probability. For this purpose, we utilize the following concentration bound:
Theorem 3.1 ([Chung and Lu 2006]). Let X1, · · · ,Xω be independent random variables with
Pr[Xi = 1] = pi and Pr[Xi = 0] = 1 −pi.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 10


1:10
Wang et al.
Let X = 1
ω · Íω
i=1 aiXi with ai > 0, and ν = 1
ω
Íω
i=1 a2
i · pi. Then,
Pr[|X −E[X]| ≥ϕ] ≤2 · exp

−
ϕ2 · ω
2ν + 2aϕ/3

,
where a = max{a1, · · · ,aω}.
To apply Theorem 3.1, let us consider the ω′ = Ín
i=1 ωi random walks generated by FORA. Let
bj = ai if the j-th random walk starts from vi. Then, we have maxj bj = 1, and b2
j ≤bj for any j.
In addition, let Yj(t) be the a random variable that equals 1 if the j-th walk terminates at t, and 0
otherwise. Then, by Theorem 3.1 and Equations 5 and 7, we have the following lemma.
Lemma 3.2. For any node t, given an arbitrary relative error threshold ϵ, an arbitrary absolute
threshold λ we have that:
Pr[|π(s,t) −ˆπ(s,t)| ≥ϵ · π(s,t)] ≤2 · exp

−ϵ2 · ω · π(s,t)
rsum · (2 + 2ϵ/3)

.
(8)
Pr[|π(s,t) −ˆπ(s,t)| ≥λ] ≤2 · exp

−
λ2 · ω
rsum · (2π(s,t) + 2λ/3)

.
(9)
Proof. Firstly, define Y ′
=
1
ω′
Íω′
j=1 bjYj(t), and ν
=
1
ω′
Íω′
j=1 b2
j E[Yj(t)]. Let a
=
max{b1, · · · ,bω′}. By definition, b2
j ≤1, and hence, ν ≤E[Y ′] and a ≤1. By Theorem 3.1, for any
ϕ, we have that Pr[|Y ′ −E[Y ′]| ≥ϕ] ≤2 · exp

−
ϕ2·ω′
2ν+2aϕ/3

. Apply ν ≤E[Y ′], we have that:
Pr[|Y ′ −E[Y ′]| ≥ϕ] ≤2 · exp

−
ϕ2 · ω′
2E[Y ′] + 2aϕ/3

.
Observe that ω′·rsum
ω
(E[Y ′] −Y ′) = π(s,t) −ˆπ(s,t), the above inequality can be rewritten as:
Pr[|π(s,t) −ˆπ(s,t)| ≥ω′ · rsum
ω
ϕ] ≤2 · exp

−
ϕ2 · ω′
2E[Y ′] + 2aϕ/3

.
Besides, by Equation 6, we have that: E[Y ′] ≤
ω
ω′·rsum · π(s,t), it is satisfied that:
Pr[|π(s,t) −ˆπ(s,t)| ≥ω′ · rsum
ω
ϕ] ≤2 · exp
 
−
ϕ2 · ω′
2 ω ·π(s,t)
ω′·rsum + 2aϕ/3
!
.
Let ϕ = ω ·ϵ ·π(s,t)
ω′·rsum , we have:
Pr[|π(s,t) −ˆπ(s,t)| ≥ϵ · π(s,t)] ≤2 · exp

−
ϵ2 · ω · π(s,t)
rsum · (2 + 2a · ϵ/3)

.
Since a ≤1, we get that:
Pr[|π(s,t) −ˆπ(s,t)| ≥ϵ · π(s,t)] ≤2 · exp

−ϵ2 · ω · π(s,t)
rsum · (2 + 2ϵ/3)

.
By setting ϵ = λ/π(s,t), we further have that:
Pr[|π(s,t) −ˆπ(s,t)| ≥λ] ≤2 · exp

−
λ2 · ω
rsum · (2π(s,t) + 2λ/3)

.
This finishes the proof.
□
Lemma 3.3. For any node t with π(s,t) > δ, Algorithm 2 returns an approximated PPR ˆπ(s,t) that
satisfies Equation 1 with at least 1 −pf probability.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 11


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:11
Proof. Since ω = rsum ·
(2ϵ/3+2)·log (2/pf )
ϵ2·δ
, according to Lemma 3.2, we have that:
Pr[|π(s,t) −ˆπ(s,t)| ≥ϵ · π(s,t)] ≤exp

−
ϵ2 · π(s,t)
rsum · (2 + 2ϵ/3) · rsum · (2ϵ/3 + 2) · log (2/pf )
ϵ2 · δ

≤2 exp

−π(s,t)
δ
· log (2/pf )

Since π(s,t) > δ, we have that:
Pr[|π(s,t) −ˆπ(s,t)| ≥ϵ · π(s,t)] < 2 exp(log (2/pf )) = pf .
Also notice that the target t is arbitrarily chosen, and we can derive this bound for all nodes
t ∈V . Hence, the returned answer for the single-source PPR query satisfies Definition 2.1, which
finishes the proof.
□
3.2
Choosing rmax
Recall from Sections 2.2 and 3.1 that parameter rmax determines how quickly we can terminate
Forward Push. A high value for rmax leads to low cost for Forward Push (since it can terminate
early), but high cost for random walks (since a large number of them are required), and vice versa.
Thus, finding the appropriate value of rmax requires modelling the overall running time of FORA.
Recall that, the Forward Push runs in O

1
rmax

time. In addition, the expected time complexity of
the random walk phase is O

rsum ·
(2ϵ/3+2)·log (2/pf )
ϵ2

, since each random walk takes O(1) expected
time to generate. Observe that
rsum =
Õ
vi ∈V
r(s,vi) ≤
Õ
vi ∈V
rmax · |N out(vi)| = m · rmax .
Therefore, the expected running time of Algorithm 2 is
O

1
rmax + m · rmax ·
(2ϵ/3+2)·log (2/pf )
ϵ2·δ

.
Using the method of Lagrange multipliers, we can see that the above time complexity is minimized
when
rmax =
ϵ
√m
·
s
δ
(2ϵ/3 + 2) · log (2/pf ).
(10)
Accordingly, the expected time complexity of Algorithm 2 becomes
O

1
ϵ ·
√
δ
p
m · (2ϵ/3 + 2) · log (2/pf )

.
However, we also note that rsum can be bounded by 1. Therefore, we have to consider two cases.
• Case 1: m · rmax ≤1. Then, it is easy to verify that
1
ϵ ·
√
δ
p
m · (2ϵ/3 + 2) · log (2/pf ) ≤
(2ϵ/3+2)·log (2/pf )
ϵ2·δ
.
Then
the
time
complexity
can
be
bounded
by
O(
1
ϵ ·
√
δ
p
m · (2ϵ/3 + 2) · log (2/pf )).
• Case 2: m · rmax > 1. In this case,
1
ϵ ·
√
δ
p
m · (2ϵ/3 + 2) · log (2/pf ) >
(2ϵ/3+2)·log (2/pf )
ϵ2·δ
. There-
fore, if we set rmax according to Equation 10, we will have sub-optimal performance. To
remedy this issue, we set rmax to
ϵ2·δ
(2ϵ/3+2)·log (2/pf ). Then the time complexity can be bounded
by O(
(2ϵ/3+2)·log (2/pf )
ϵ2·δ
).
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 12


1:12
Wang et al.
Therefore, combining the above two cases, the time complexity of FORA can be bounded by
O

min{
1
ϵ ·
√
δ
p
m · log (2/pf ),
log (2/pf )
ϵ2·δ
}

.
When δ = O(1/n), pf = O(1/n), the above time complexity becomes
O
1
ϵ min{
p
m · n · logn, n · logn
ϵ2
}

for general graphs. When the graph is scale-free, in which casem/n = O(logn), the time complexity
becomes O   1
ϵ n · logn, improving over the MC approach by 1/ϵ.
3.3
Indexing Scheme
Based on FORA, we propose a simple and effective index structure to further improve the efficiency
of whole-graph SSPPR queries. The basic idea is to pre-compute a number of random walks from
each nodev, and then store the destination of each walk. During query processing, if FORA requires
performing x random walks from v, we would inspect the set S of random walk destinations pre-
computed for v, and then retrieve the first x nodes in S. As such, we avoid generating any random
walks on-the-fly, which considerably reduces query overheads.
A natural question to ask is: how many random walks should we pre-compute for each node v?
To answer this question, we first recall that, when the local update phase of FORA terminates, the
residue of each node v is at most |N out(v)| · rmax. Combining this with Lemma 3.3, we can see that
the number of random walks from v required by FORA is
ωmax(v) =

|N out(v)| · rmax · (2ϵ/3 + 2) · log (2/pf )
ϵ2 · δ

.
(11)
If we set rmax according to Equation 10 in which case m · rmax ≤1, we have
ωmax(v) =

|N out(v)| ·
1
ϵ ·
√
m · δ
·
q
(2ϵ/3 + 2) · log (2/pf )

Otherwise, rmax is set to
ϵ2·δ
(2ϵ/3+2)·log (2/pf ), we have
ωmax(v) = |N out(v)|.
In summary, we pre-compute ωmax(v) random walks from each node v, and record the last
nodes of those walks in our index structure. The total space overhead incurred is then bounded by
Õ
v
ωmax(v) ≤min{
Õ
v

|N out(v)| ·
√
(2ϵ/3+2)·log (2/pf )
ϵ ·
√
m·δ

, Í
v |N out(v)|}
≤min{n +
√m
ϵ ·
√
δ
·
q
(2ϵ/3 + 2) · log (2/pf ),m}.
Therefore, we have the following lemma.
Lemma 3.4. The space consumption of our index structure is
O

min{n + 1
ϵ
q
m log (1/pf )
δ
,m}

.
(12)
When δ = O(1/n), pf
= O(1/n), and m/n = O(logn), the above space complexity becomes
O  min{ 1
ϵ n · logn,m} .
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 13


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:13
Remark. One may wonder whether we can also pre-compute the Forward Push result for each
node, so that we can answer each query by a simple combination of pre-processed Forward Push
and random walks, which could lead to higher query efficiency. However, we note that storing
the Forward Push results for all nodes incurs significant space overheads. In particular, it requires
O (min{n, 1/rmax }) space for each node, where rmax is set according to Equation 10. As such, the
total space consumption for preprocessing Forward Push results is
O

min

n2, n
ϵ ·
q
m·log (1/pf )
δ

,
which is prohibitive for large graphs. Therefore, we do not store Forward Push results in our index
structure.
4
OPTIMIZATIONS FOR WHOLE-GRAPH SSPPR QUERIES
In this section, we present optimization techniques to reduce the index size or improve the query
efficiency of our FORA algorithm on whole-graph SSPPR queries. In particular, in Section 4.1,
we will present our technique to reduce the index size by avoiding zero-hop nodes in the index
structure. In Section 4.2, we will present our technique to reduce the query time by balancing the
forward push and the random walk costs.
4.1
Pruning zero-hop random walks
Recall that in FORA, after the local update phase, we sample random walks from each source with
non-zero residues. Our main observation is that: α portion of the random walks is expected to stop at
the current node, and with O(1) time we can immediately record the portion of such random walks
and hence avoid simulating α portion of the total random walks. However, a question is that, can we
still provide approximation guarantee while exploring this pruning strategy? We next demonstrate
how to use the reduction of zero-hop random walk idea to ensure the approximation guarantee.
We first define two random variables π0(s,t) and π1(s,t). We define π0(s,t) as the probability that a
random walk from s immediately stopped at node t, i.e., the length of the random walk is 0; we
further define π1(s,t) as the probability that a random walk from s that stopped at node t after
traversing at least one node, i.e., the length of the random walk is at least 1. Then it is clear that the
personalized PageRank π(s,t) satisfies the following equation.
π(s,t) = π0(s,t) + π1(s,t)
We hence rewrite Equation 5 as follows:
π(s,t) = π ◦(s,t) +
Õ
v ∈V
r(s,v) · (π0(v,t) + π1(v,t)).
Also notice that π0(s,t) either equals α or 0 depending on whether s = t or not. Therefore, the
above equation can be further rewritten as:
π(s,t) = π ◦(s,t) + r(s,t) · α +
Õ
v ∈V
r(s,v) · π1(v,t).
We define a random variable Xv as follows: we randomly select one of a out-neighbor u of v, and
then start a random walk from u. If the random walk stops at t, then Xv = 1, otherwise, Xv = 0.
Then, it is not difficult to verify that (1 −α) · E[X] = π1(s,t).
π(s,t) = π ◦(s,t) + r(s,t) · α +
Õ
v ∈V
(1 −α) · r(s,v) · E[Xv].
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 14


1:14
Wang et al.
Define r ′(s,v) = (1 −α) · r(s,v), we have that:
π(s,t) = π ◦(s,t) + r(s,t) · α +
Õ
v ∈V
r ′(s,v) · E[Xv].
With the above equation, we can then further apply the same technique proposed in Section 3.1.
We define r ′
sum = Í
v ∈V r ′(s,v). Then, by sampling ω′ = r ′
sum ·
(2ϵ/3+2)·log (2/pf )
ϵ2·δ
random walks, we
can provide approximation guarantee for the whole-graph SSPPR queries. With this approach,
when the same rmax is used as Algorithm 5, the maximum number of random walks sampled from
a node v can be bounded by
(1 −α) · rmax · N out(v) · (2ϵ/3 + 2) · log (2/pf )
ϵ2 · δ
,
while previously, it requires
rmax · N out(v) · (2ϵ/3 + 2) · log (2/pf )
ϵ2 · δ
.
Therefore, with this optimization, we can also reduce the index size by α portion. Next, we
further demonstrate our second optimization technique to improve the query efficiency.
4.2
Balancing Forward Push and Random Walk Cost
Recall that in FORA, we set rmax according to Equation 10 to minimize the time complexity of FORA.
However, in practice, the derived rmax may not be the best choice since Equation 10 considers the
worst case while in practice the running time might be quite different. Of course, we may tune
rmax for different dataset and choose rmax that derives the best piratical performance. However,
the tuned rmax will typically be data-dependent. Here we are aiming to propose a solution that
balances the forward push and random walk costs without any dependency on the datasets.
In [Lofgren 2015], they propose a balanced approach for BiPPR by doing the backward propagation
and maintaining the largest residue using a max-heap. Since the total number of random walks
depends linearly on the maximum residue, it estimates the running time of the random walk and
stops the backward propagation as soon as the running time is around the same as the forward
random walk. Our proposed balancing strategy shares the similar spirit as theirs. However, we do
not maintain the priority queue since the number of random walks of FORA depends linearly on
the total sum of the residues instead of the maximum residue. When we finish the forward push,
we can accurately estimate the running time of the random walk part since (i) we know the total
number of random walks; (ii) the average running time of one random walk depends only on α,
which is dataset-independent. Therefore, we can easily estimate the cost of a random walk and
use it for random walk cost estimation no matter what dataset we are running on. Therefore, we
propose the adaptive approach to balance the forward push and random walk cost as shown in
Algorithm 3.
Initially, we start the forward push by setting rmax = 1 and calculate the current accumulated
forward push cost (Algorithm 3 Line 11). Then, it checks if the forward push cost is still lower than
the estimated random walk cost (Algorithm 3 Line 4). If this is the case, the algorithm continue
the forward push process, update the accumulated forward push cost, and update the estimated
random walk cost (Algorithm 3 Lines 5-11). The forward push terminates as soon as the estimated
random walk cost is larger than the forward push cost (Algorithm 3 Line 4). By this strategy, it
guarantees that, when the forward push terminates, the cost will not differ from the random walk
cost by a large margin. The random walk phase is similar to the one in Algorithm 2 except that
here we prune the zero-hop random walks as mentioned in Section 4.1. In particular, we convert
α portion of the residue r(s,vi) to its reserve (Algorithm 3 Line 12), and the residue of node vi is
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 15


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:15
ALGORITHM 3: FORA for Whole-Graph SSPPR with optimization
Input: Graph G, source node s, probability α, relative error threshold ϵ
Output: Estimated PPR ˆπ(s,v)for all v ∈V
1 Let rc be the cost of a random walk, and FC be the running time of the forward push;
2 Let r(s,vi), π◦(s,vi) be the residue and reserve of node vi in forward push, and initially only r(s,s) = 1 while
all other values are zero;
3 Let FC = 0,rmax = 1,rsum = 1,ω = rsum · (2ϵ/3+2)·log (2/pf )
ϵ2·δ
;
4 while ∃v ∈V such that r(s,v)/|N out (v)| > rmax and FC < ω ∗rc do
5
for each u ∈Nout (v) do
6
r(s,u) ←r(s,u) + (1 −α) ·
r(s,v)
|N out (v)|
7
π◦(s,v) ←π◦(s,v) + α · r(s,v);
8
rsum = rsum −α · r(s,v);
9
ω = rsum · (1 −α) · (2ϵ/3+2)·log (2/pf )
ϵ2·δ
;
10
r(s,v) ←0;
11
FC ←current elapsed time;
12 Let ˆπ(s,vi) = π◦(s,vi) + α · r(s,vi) for all vi ∈V ;
13 for vi ∈V with r(s,vi) > 0 do
14
Let r(s,vi) = (1 −α) · r(s,vi),ωi = ⌈r(s,vi)(1 −α) · ω/rsum⌉;
15
Let ai = r(s,vi)
rsum · ω
ωi ;
16
for i = 1 to ωi do
17
Randomly select a out-neighbor u of vi and generate a random walk W from u;
18
Let t be the end point of W ;
19
ˆπ(s,t)+ = ai ·rsum
ω
;
20 return ˆπ(s,v1), · · · , ˆπ(s,vn);
reduced to (1 −α) · vi (Algorithm 3 Line 14). When we sample a random walk from each node vi,
we first randomly select one of its out-neighbor and then do random walk from these nodes thus
avoiding the zero-hop random walks.
As we will see in our experimental evaluation, the balanced strategy can help reduce the average
running time of whole-graph SSPPR queries by almost half, which demonstrates the effectiveness
of the balancing strategy. For the indexing version of our FORA and the top-k algorithm, we tune
rmax to evaluate the trade-off between the index size and the query performance in Section 8.
5
TOP-k SSPPR
In this section, we discuss how FORA handles approximate top-k SSPPR queries.
Rationale. A straightforward approach to answer a top-k SSPPR query with FORA is to first apply
it to perform a whole-graph SSPPR query, and then returns the k nodes with the largest approximate
PPR values. However, if we are to satisfy the accuracy requirement described in Definition 2.2,
we would need to set the parameters of FORA according to the exact k-th largest PPR value
π(s,v∗
k), which is unknown in advance. To address this, a naive solution is to conservatively set
π(s,v∗
k) = 1/n, which, however, would lead to unnecessary overheads.
To avoid the aforementioned overheads, we propose a trial-and-error approach as follows.
We first assume that π(s,v∗
k) is a large value (e.g., 1/k), and we set the parameters of FORA
accordingly to perform a whole-graph SSPPR query. After that, we inspect the results obtained
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 16


1:16
Wang et al.
ALGORITHM 4: Top-k FORA with bound refinement
Input: Graph G, source node s, probability α
Output: k nodes with the highest approximate PPR scores
1 for δ = 1
k , 1
2k , 1
4k , · · · , 1
n do
2
Invoke Algorithm 2 with G, s, α, and rmax set by Equation 10 and fail probability p′
f =
pf
n·log n ;
3
Let C = {v′
1, · · · ,v′
k } be the set that contains the k nodes with the top-k largest lower bounds (from
Theorem 3.1);
4
Let LB(u) and U B(u) be the lower and upper bounds of π(s,u) (from Theorem 3.1);
5
if U B(v′
i) < (1 + ϵ) · LB(v′
i) for i ∈[1,k] and LB(v′
k) ≥δ then
6
Let U be the set of nodes u ∈V \ C such that UB(u) > (1 + ϵ) · LB(v′
k);
7
if u ∈U such that UB(u) < (1 + ϵ) · LB(u)/(1 −ϵ) then
8
return v′
1,v′
2, · · · ,v′
k and their estimated PPR;
to check whether the estimated PPR values are indeed large. If they are not as large as we have
assumed, then we re-run FORA with more conservative parameters, and check the new results
returned. This process is conducted iteratively, until we are confident that the results from FORA
conform to the requirements in Definition 2.2. In this section, we first present a top-k algorithm by
iteratively refining the upper and lower bounds of the top-k PPR results in Section 5.1. Nevertheless,
it is expensive to calculate the upper and lower bounds for each node in each iteration, and it
is unclear whether the algorithm will terminate with δ close to π(s,v∗
k) or not. Therefore, the
expected running time of Algorithm 4 might be identical to that of invoking Algorithm 2 with
δ = 1/n. Therefore, in Section 5.2, we further propose a new top-k query algorithm that provides
guarantee on the expected running time, and that the algorithm has high probability to terminate
with π(s,v∗
k)/4 ≤δ ≤π(s,v∗
k).
5.1
Top-k with bound refinement
Algorithm. Algorithm 4 shows the pseudo-code of the top-k extension of FORA with bound
refinement. The algorithm consists of at most logn iterations. In the i-th iteration, we invoke
Algorithm 2 with δ set to
1
2i−1·k , and the failure probability set to p′
f =
pf
n log n (Lines 1-2 in Algo-
rithm 4). (The reason for this setting will be explained shortly). After we obtain the results from
FORA, we compute an upper bound and a lower bound of each node’s PPR value, and use them to
decide whether the current top-k results are sufficiently accurate (Lines 3-8). If the top-k results
are accurate, then we return them as the top-k answers (Line 8); otherwise, we proceed to the next
iteration. In the following, we elaborate how the upper and lower bounds of each node’s PPR value
is derived.
Define LB0(v) = 0 and UB0(v) = 1 for anyv ∈V . We have the following theorem that establishes
the lower bound LBj(v) and upper bound UBj(v) of π(s,v) in the j-th iteration of Algorithm 4:
Theorem 5.1. In the j-th iteration of Algorithm 4, let ωj be the ω calculated by FORA (Algorithm 2
Line 2) in this iteration, and π ◦
j (s,v) and ˆπj(s,v) be the reserve and estimated PPR of v. Define
ϵj =
v
t
3rsum · log (2/p′
f )
ωj · max{π ◦
j (s,v), LBj−1(s,v)}, and λj = 2/3 log (2/pf ′)
2ωj
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 17


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:17
+
q
4
9r 2sum · log2 (2/p′
f ) + 8rsum · ωj · log (2/p′
f ) · UBj−1(v)
2ωj
Then, with at least 1 −p′
f probability, the following two inequalities hold simultaneously:
ˆπj(s,v)/(1 + ϵj) ≤π(s,v) ≤ˆπj(s,v)/(1 −ϵj)
ˆπj(s,v) −λi ≤π(s,v) ≤ˆπj(s,v) + λi.
Proof. Ref. Appendix A.
□
Theorem 5.1 enables us to derive tight lower and upper bounds of each node’s PPR value in each
iteration. In particular, we set
UBj(v) = min{1, ˆπj(s,v)/(1 −ϵ), ˆπj(s,v) + λi},
LBj(v) = max{ ˆπj(s,v)/(1 + ϵ), ˆπj(s,v) −λi, 0}.
With these upper and lower bounds, the following theorem shows that if Lines 5 and 7 in Algorithm 4
holds, then Algorithm 4 returns the answer for the approximate top-k SSPPR query.
Theorem 5.2 (Approximate Top-k). Let v′
1, · · · ,v′
k be the k nodes with the largest lower bounds in
the j-th iteration of Algorithm 4. LetU be the set of nodesu ∈V \C such thatUBj(u) > (1+ϵ)·LBj(v′
k),
If UB(v′
i) < (1 + ϵ) · LB(v′
i) for i ∈[1,k], LBj(v′
k) ≥δ, and there exists no u ∈U such that
UBj(u) < (1 + ϵ) · LBj(u)/(1 −ϵ), then returning v′
1, · · · ,v′
k and their estimated PPR values would
satisfy the requirements in Definition 2.2 with at least 1 −j · n · p′
f probability.
Proof. Ref. Appendix A.
□
Now recall that the number of iterations in Algorithm 4 is logn, and in each iteration, we assume
that the upper and lower bounds are correct. Hence, by applying union bound, the failure probability
will be at most n logn · p′
f . Note that p′
f =
pf
n log n . The failure probability is hence no more than pf ,
and we guarantee that the returned answer has approximation with at least 1 −pf probability.
5.2
Top-k with improved time complexity
Despite the fact that Algorithm 4 provides superb performance on top-k query processing as shown
in [Wang et al. 2017], there is no guarantee that the running time will depends on δ = π(s,v∗
k)
instead of δ = 1/n. Also, after each iteration, we need to re-calculate the lower- and upper-bounds
for each node, which may take more than half of the query running time. This motivates us to
propose our new top-k algorithm that avoids the overheads of the bound-refinement, and provides
running time guarantees with respect to π(s,v∗
k).
Algorithm. Algorithm 5 shows the pseudo-code of the top-k extension of FORA. The algorithm
consists of at most log2 (n/k) iterations. In the i-th iteration, we invoke Algorithm 2 with δ set
to
1
k ·2i−1 , relative error threshold ϵ ′ = ϵ/2 and the failure probability set to p′
f =
pf
n log2 (n/k) (Lines
1-2 in Algorithm 5). (The reason for this setting will be explained shortly). After we obtain the
results from FORA, we compute the estimated PPR scores for each node and get the k-th largest
estimated PPR value. We compare the k-th estimated PPR score with (1 + ϵ) · δ and use this as
evidence to see whether the current top-k results are sufficiently accurate (Line 4). If the top-k
results are accurate, then we return them as the top-k answers (Lines 5-6); otherwise, we halve
the value of δ and proceed to the next iteration. In the following, we analyze the approximation
guarantee and time complexity of Algorithm 5. Firstly, we have the following lemma about the
value of δ when Algorithm 5 terminates.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 18


1:18
Wang et al.
ALGORITHM 5: Top-k FORA
Input: Graph G, source node s, probability α
Output: k nodes with the highest approximate PPR scores
1 for δ = 1
k , 1
2k · · · , 1
n do
2
Invoke Algorithm 2 with G, s, and α with ϵ′ = ϵ/2, failure probability p′
f =
pf
n log2 (n/k), and rmax set by
Equation 10;
3
Let ˆπ(s,vk) be the k-th largest estimated PPR score returned by Algorithm 2;
4
if ˆπ(s,vk) ≥(1 + ϵ) · δ then
5
Let v′
1,v′
2, · · · ,v′
k be the k nodes with the top-k largest PPR values;
6
return v′
1,v′
2, · · · ,v′
k and their estimated PPR values;
Lemma 5.3. Let vk be the node that has the k-th largest estimated PPR value and ˆπ(s,vk) be the
estimated PPR value for node vk with respect to s. Let v∗
k be the node with the true k-th largest PPR.
Then, when Algorithm 5 terminates, it holds for δ that:
• δ > π(s,v∗
k) with at most n · p′
f /8 probability;
• δ ≤π(s,v∗
k) with at least 1 −log2
1
π(s,v∗
k ) · n · p′
f /8;
• δ ≤π(s,v∗
k)/2x+1 (x = 1, 2, 3 · · · ) with at most
p′
f
2x probability.
Proof. We first consider the case when Algorithm 5 terminates with δ > π(s,v∗
k).
δ > π(s,v∗
k). If δ > π(s,v∗
k) when Algorithm 5 terminates, we know that there exists at least
n −k + 1 nodes such that π(s,v) < δ. Denote X as the set of nodes such that v ∈X if π(s,v) < δ.
For any of these nodes, we consider the probability that their PPR values with respect to s is greater
than (1 + ϵ) · δ. Note that according to Line 2 of Algorithm 5, the number of random walks is set to
rsum ·(ϵ/2·2/3+2)·log (2/p′
f )
(ϵ/2)2·δ
. Let t be a node in X, and λ = ϵ · δ, according to Lemma 3.2, we have that:
Pr[ ˆπ(s,t) −π(s,t) > λ] ≤exp
 
−
λ2
rsum · (2π(s,t) + 2λ/3) ·
4rsum · (2 + ϵ/3) · log (2/p′
f )
ϵ2 · δ
!
≤exp

−
4δ · (2 + ϵ/3)
2 · π(s,t) + 2ϵ · δ/3 · log (2/p′
f )

≤exp

−4δ · (2 + ϵ/3)
2 · δ + 2ϵ · δ/3 · log (2/p′
f )

(δ > π(s,t))
≤exp

−4 · (2 + ϵ/3)
2 + 2ϵ/3
· log (2/p′
f )

< exp

−3 · log (2/p′
f )

< p′
f /8
So, by union bound, it is satisfied that ˆπ(s,t) < π(s,t) + ϵ · δ holds for any node t ∈X with at
least 1 −n · p′
f /8 probability. Also note that π(s,t) < δ. This indicates that with at least probability
1 −n ·p′
f /8, for all nodes t ∈X,it is satisfied that ˆπ(s,t) < (1 +ϵ) ·δ. Since there are at least n −k + 1
nodes in X. It indicates that the returned ˆπ(s,vk) must be no larger than maxv ∈X ˆπ(s,v), which
is less than (1 + ϵ) · δ. However, this contradicts to the fact that Algorithm 5 terminates when
ˆπ(s,vk) ≥(1 + ϵ) · δ. As a result, with at most n · p′
f /8 probability, the algorithm terminates when
δ > π(s,v∗
k).
Next, we consider the probability when Algorithm 5 terminates with δ ≤π(s,v∗
k).
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 19


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:19
δ ≤π(s,v∗
k). Since in Algorithm 5, there are at most log2
1
k ·π(s,vk ∗) iterations such that
δ > π(s,v∗
k). The probability that the algorithm terminates when δ > π(s,v∗
k) is bounded by
log2
1
k ·π(s,v∗
k )n · p′
f /8. Hence, with at least probability 1 −log2
1
k ·π(s,v∗
k )n · p′
f /8, the algorithm
terminates with δ ≤π(s,v∗
k).
Finally, we consider whether δ will be too small when Algorithm 5 terminates.
δ ≤π(s,v∗
k)/2x +1. Consider the k nodes with the k largest PPR values. Denote these nodes as
v∗
1,v∗
2,v∗
3, · · · ,v∗
k. Consider the estimated PPR of v∗
i with respect to s (1 ≤i ≤k). According to
Lemma 3.2, it is satisfied that:
Pr[ ˆπ(s,v∗
i ) ≤(1 + ϵ) · δ] ≤Pr[ ˆπ(s,v∗
i ) ≤(1 + ϵ) · π(s,v∗
k)/2x+1]
(δ ≤π(s,v∗
k)/2x+1)
≤Pr[ ˆπ(s,v∗
i ) ≤(1 + ϵ) · π(s,v∗
i )/2x+1]
(π(s,v∗
k) ≤π(s,v∗
i ))
≤Pr[ ˆπ(s,v∗
i ) ≤(1 −(1 −1/2x) · ϵ) · π(s,v∗
i )]
(1 + ϵ)/2x+1 ≤1 −(1 −1/2x) · ϵ for 0 < ϵ < 1
≤exp
 
−
((1 −1/2x) · ϵ)2 · π(s,v∗
i )
rsum · (2 + 2(1 −1/2x) · ϵ/3) ·
4rsum · (2 + ϵ/3) · log (2/p′
f )
ϵ2 · δ
!
≤exp

−2(1 −1/2x)2 · 2x+1 ·
2(2 + ϵ/3)
2 + 2(1 −1/2x) · ϵ · log (2/p′
f )

2(1 −1/2x)2 > 1,
2(2 + ϵ/3)
2 + (1 −1/2x) > 1
≤exp

−2x+1 · log (2/p′
f )

<
(p′
f )2
2x+1
By union bound, the probability that ˆπ(s,v∗
i ) ≥(1 +ϵ) ·δ holds for any 1 ≤i ≤k simultaneously
is at least 1 −k ·
(p′
f )2
2x+1 ≥1 −
p′
f
2x+1 . Since there are k estimations no smaller than (1 +ϵ) ·δ, Algorithm
5 will terminate. Therefore, Algorithm 5 terminates when δ ≤π(s,v∗
i )/2i+1 with at most
p′
f
2x+1
probability, which finishes the proof.
□
Lemma 5.3 indicates several desired properties of our top-k algorithm. Firstly, the algorithm
stops with δ > π(s,v∗
k) with low probability. Besides, it terminates with δ ≤π(s,v∗
k) with high
probability, which is an important condition for providing approximate top-k answer. Thirdly,
when the algorithm terminates, δ will not deviate from π(s,v∗
k) by a large margin. The larger the
margin is between δ and π(s,v∗
k), the lower the probability it is. By leveraging 5.3, we further have
the following lemma on the time complexity of our top-k algorithm.
Lemma 5.4. The expected running time of Algorithm 5 can be bounded by
O
©­­
«
min{
p
m · log (2/pf )
ϵ ·
q
π(s,v∗
k)
, log (2/pf )
ϵ2 · π(s,v∗
k)}
ª®®
¬
.
Proof. Let c be the constant factor of the time complexity of Algorithm 2 and δ∗be the value of
δ when Algorithm 5 terminates. Suppose that the algorithm terminates after i + 1 iterations, and
note that the time complexity of each iteration is bounded by O

c
ϵ ·
√
δ
p
m · (2ϵ/3 + 2) · log (2/pf )

.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 20


1:20
Wang et al.
Then, the cost C of FORA can be bounded by
C =
1/(2i ·k)
Õ
δ=1/k
c
ϵ ·
√
δ
q
m · (2ϵ/3 + 2) · log (2/pf )
= c
ϵ
q
m · (2ϵ/3 + 2) · log (2/pf ) ·
1/(2i ·k)
Õ
δ=1/k
1
√
δ
≤c
ϵ
q
m · (2ϵ/3 + 2) · log (2/pf ) · 1 + 1/
√
δ∗
1 −1/
√
2
≤c
ϵ
q
m · (2ϵ/3 + 2) · log (2/pf ) ·
4
√
δ∗
Denote
ϕ = 4c
ϵ
q
m · (2ϵ/3 + 2) · log (2/pf ).
Next, we further consider the expected cost of Algorithm 5.
E[C] = Pr[δ > π(s,v∗
k)] · Cδ >π(s,v∗
k ) + Pr[π(s,v∗
k)/4 < δ ≤π(s,v∗
k)] · Cπ(s,v∗
k )/4<δ ≤π(s,v∗
k )
+
log2 (n/π(s,v∗
k ))
Õ
x=1
Pr[π(s,v∗
k)/2i+2 < δ ≤π(s,v∗
k)/2i+1] · Cπ(s,v∗
k )/2i+2<δ ≤π(s,v∗
k )/2i+1
< 1 ·
ϕ
q
π(s,v∗
k)
+ 1 ·
ϕ
q
π(s,v∗
k)/4
+
log2 (n/π(s,v∗
k ))
Õ
i=1
p′
f
2i+1
ϕ
q
π(s,v∗
k)/2i+1
<
4ϕ
q
π(s,v∗
k)
=
16
ϵ ·
q
π(s,v∗
k)
q
m · (2ϵ/3 + 2) · log (2/pf )
Besides, note that the time complexity of each iteration can also be bounded by
O
 (2ϵ/3+2)·log (2/pf )
δ

. Still let c denote the constant in the time complexity. Then, the cost C of
FORA can be bounded by
C = c · (2ϵ/3 + 2) · log (2/pf )
ϵ2
·
1/(2i ·k)
Õ
δ=1/k
1
δ ≤c · (2ϵ/3 + 2) · log (2/pf )
ϵ2
· 2
δ
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 21


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:21
Let ϕ = 2c ·
(2ϵ/3+2)·log (2/pf )
ϵ2
, the expected cost of Algorithm 5 then can be further bounded by:
E[C] = Pr[δ > π(s,v∗
k)] · Cδ >π(s,v∗
k ) + Pr[π(s,v∗
k)/4 < δ ≤π(s,v∗
k)] · Cπ(s,v∗
k )/4<δ ≤π(s,v∗
k )
+
log2 (n/π(s,v∗
k ))
Õ
x=1
Pr[π(s,v∗
k)/2i+2 < δ ≤π(s,v∗
k)/2i+1] · Cπ(s,v∗
k )/2i+2<δ ≤π(s,v∗
k )/2i+1
< 1 ·
ϕ
π(s,v∗
k) + 1 ·
ϕ
π(s,v∗
k)/4 +
log2 (n/π(s,v∗
k ))
Õ
i=1
p′
f
2i+1 ·
ϕ
π(s,v∗
k)/2i+1
<
6ϕ
π(s,v∗
k) = 12c · (2ϵ/3 + 2) · log (2/pf )
ϵ2 · π(s,v∗
k)
Therefore, the expected time complexity of Algorithm 5 can be bounded by
O
©­­
«
min{
p
m · log (2/pf )
ϵ ·
q
π(s,v∗
k)
, log (2/pf )
ϵ2 · π(s,v∗
k)}
ª®®
¬
,
which finishes the proof.
□
It still remains to clarify whether Algorithm 5 returns approximate top-k answers. The following
lemma shows that our algorithm returns approximate top-k answer with high probability.
Lemma 5.5. Algorithm 5 returns an ϵ-approximate top-k answer with at least 1 −pf probability.
Proof. Let v1,v2, · · · ,vk be the returned k nodes by Algorithm 5, and R = {v∗
1,v∗
2, · · · ,v∗
k}
be the k nodes with the real top-k largest PPR values. According to Lemma 5.3, Algorithm 5
terminates with δ ≤π(s,v∗
k) (denoted as Condition C1) with at least 1 −log2
1
π(s,v∗
k ) · n · p′
f /8
probability. When C1 holds, we note that for v∗
i , it is satisfied that, with 1 −p′
f /2 probability,
ˆπ(s,v∗
i ) −π(s,v∗
i ) > ϵ
2 · π(s,v∗
i ). As a result,
ˆπ(s,v∗
i ) −π(s,v∗
i ) > ϵ
2 · π(s,v∗
i ) for any 1 ≤i ≤k
(13)
holds with at least 1 −k · p′
f /2 probability. We denote this condition as C2.
We next consider when conditions C1 and C2 both hold, the probability that the single source
FORA fails to provide an ϵ-approximate top-k answer. When C1 holds, we know that
ˆ
π(s,v∗
i ) >
(1 −ϵ/2) · π(s,v∗
i ). With this condition, ˆπ(s,vi) must be larger than (1 −ϵ/2) · π(s,v∗
i ) since its
estimation is i-th largest and we know that there are at least i nodes with estimated PPR larger than
(1 −ϵ/2) · π(s,v∗
i ), i.e., ˆπ(s,v∗
1), ˆπ(s,v∗
2), · · · , ˆπ(s,v∗
i ). We say a query fails if there exists a returned
node vi such that:
(1) ˆπ(s,vi) > (1 −ϵ/2) · π(s,vi),
(2) π(s,vi) < (1 −ϵ) · π(s,v∗
i ).
Next, we prove that vi fails with very low probability. Let ϵ ′ = (1−ϵ/2)·π(s,v∗
i )
π(s,vi)
−1.
Pr[ ˆπ(s,vi) > (1 −ϵ/2) · π(s,v∗
i )] = Pr[ ˆπ(s,vi) > (1 + ϵ ′) · π(s,vi)]
Since π(s,vi) < (1 −ϵ)π(s,v∗
i ), we have that ϵ ′ > ϵ/2
1−ϵ . Also note that
ϵ ′ · π(s,vi)
π(s,v∗
i ) = (1 −ϵ/2) −π(s,vi)
π(s,v∗
i ) > (1 −ϵ/2) −(1 −ϵ) = ϵ/2.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 22


1:22
Wang et al.
Then, according to Lemma 3.2, it is satisfied that:
Pr[ ˆπ(s,vi) > (1 −ϵ/2) · π(s,v∗
i )] = Pr[(1 + ϵ ′) · π(s,vi)]
≤exp
 
−
(ϵ ′)2 · π(s,vi)
rsum · (2 + 2ϵ ′/3) ·
rsum · (2 + ϵ/3) · log (2/p′
f )
(ϵ/2)2 · δ
!
≤exp
 
−
ϵ ′
(2 + 2ϵ ′/3) · ϵ ′ · π(s,vi)
π(s,v∗
i )
· π(s,v∗
i )
δ
·
(2 + ϵ/3) · log (2/p′
f )
(ϵ/2)2
!
(
ϵ ′
2 + 2ϵ ′/3 is monotonically increasing,ϵ ′ · π(s,vi)
π(s,v∗
i )
> ϵ/2, π(s,v∗
i )
δ
> 1)
≤exp
 
−
ϵ/(2 −2ϵ)
2 + ϵ/(3 −3ϵ) · ϵ/2 · 1 ·
(2 + ϵ/3) · log (2/p′
f )
(ϵ/2)2
!
≤exp

−ϵ/3 + 2
2 −5ϵ/3 · log (2/p′
f )

( ϵ/3 + 2
2 −5ϵ/3 > 1)
≤exp(−log (2/p′
f )) = p′
f /2.
As a result, when C1 holds, the probability that the query does not fail on any node is at least
1 −n ·p′
f by applying union bound on the events that no vi fails and conditio C2 holds. Since in the
worst case, there exists log (n/π(s,v∗
k)) iterations when C1 holds. Therefore, we further have that
the query returns ϵ-approximate answer with at least
1 −(log2
1
π(s,v∗
k) · n · p′
f /8 + log (n/π(s,v∗
k)) · n · p′
f ) ≥1 −pf
probability. This finishes the proof.
□
6
EXTENSIONS
6.1
Extending BiPPR to Whole-Graph SSPPR
Recall from Section 2.2 that in BiPPR, it includes both a forward phase and a backward phase. It
is proved in [Andersen et al. 2007] that the amortized time complexity for the backward phase is
O

m
n·rmax

, and in [Lofgren et al. 2016], it shows that the forward phase requires O
 rmax ·log (1/pf )
ϵ2·δ

time, given the backward phase thresholdrmax. Afterwards, they choosermax = O

ϵ ·
q
m·δ
n·log (1/pf )

to minimize the time complexity for the pairwise PPR query, which is O

1
ϵ
q
m·log (1/pf )
n·δ

. To apply
BiPPR for whole-graph SSPPR queries, a straightforward approach is to use it to answer n point-to-
point PPR queries (i.e., from s to every other node). This, however, leads to a total time complexity
of O

1
ϵ
q
mn·log (1/pf )
δ

, which is a factor of √n larger than that of the whole-graph SSPPR FORA.
To improve this, we observe that the n point-to-point PPR queries share the same forward phase,
and hence, we can conduct the forward phase once and then re-use its results for all n backward
phase. In addition, to reduce the total cost of n backward phases, we can set rmax to a larger value;
although it would require more random walks to be generated in the forward phase, the tradeoff is
still favorable as the overhead of the forward phase has been significantly reduced by the re-usage
of results. Since the backward phase (for all target nodes) has a cost of O

m
rmax

, it can be verified
that, by setting rmax = O

ϵ ·
q
m·δ
log (1/pf )

, the expected time complexity of this optimized version
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 23


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:23
of BiPPR (for SSPPR queries) is
O

1
ϵ ·
√
δ
q
m · log (1/pf )

,
which is identical to that of single-source FORA.
However, as we show in Section 8, the optimized BiPPR is significantly outperformed by Whole-
Graph SSPPR FORA. The reason is that, even after the aforementioned optimization, BiPPR either
degrades to MC when rmax is large, or still requires performing a backward phase from each node
v in G, even if π(s,v) is extremely small and can be omitted. In contrast, single-source FORA does
not suffer from these deficiencies, and avoid examining nodes with very small PPR values. Instead,
it performs a forward search phase, followed by a number of random walks from the nodes visited
in the search; this process tends to avoid examining nodes with very small PPR values, since those
nodes are unlikely to be visited by the forward push or the random walks.
6.2
Extending FORA to Source Distributions
In many real applications of the personalized PageRank, the source s can be a distribution (e.g., on a
set of bookmark pages) instead of a single node. We show that our algorithms for single-source-node
FORA can be extended to the case of arbitrary source distributions.
Let σ be the node distribution that the source node s is sampled from. For any target node t, its
personalized PageRank with respect to σ is defined as [Haveliwala 2002; Lofgren et al. 2016]
π(σ,t) =
Õ
v ∈V
σ(v) · π(v,t),
where σ(v) is the probability that a sample from σ equals v. To apply our algorithms, we modify
Line 1 of Algorithm 1 to set the initial residue of each node v as σ(v). Let π ◦(σ,v) (resp. r(σ,v))
denote the reserve (resp. residue) of node v in the modified version of Forward Push. Then, it is
easy to prove that the following invariant holds for the modified version of Forward Push:
π(σ,t) = π ◦(σ,t) +
Õ
v ∈V
r(σ,v) · π(v,t).
In particular, the initial states satisfy the above invariant, and by induction, it can be proved that
the invariant still holds after every push operation. Given the above invariant, our algorithms can
be applied to compute π(σ,t) without compromising their asymptotic guarantees. Besides, the
indexing scheme presented in Section 3.3 is still applicable, since the maximum number of random
walks required for each node is identical to that in the single-source-node algorithms.
6.3
Extending FORA to Global PageRank
Global PageRank can be regarded as the personalized PageRank with a source distribution of
(1/n, 1/n, · · · , 1/n). According to our discussion in Section 6.3, FORA can further be used to
calculate the global PageRank. The classic solution for PageRank is the Power-Method, which
takes a running time of O(m · log
1
δ ·ϵ ), to provide ϵ-approximation for PageRank scores above the
threshold δ. To apply the Monte-Carlo method, we can first randomly sample source node, record
the number of random walks stops at a nodev, and use the fraction of random walks stopped atv as
the estimated PageRank. To derive ϵ-approximation, the running time will be O
 (2ϵ/3+2)·log (2/pf )
ϵ2·δ

.
When ϵ is moderate, and m >
3
ϵ2·δ , the Monte-Carlo approach achieves a better time complexity.
With the proposed FORA framework, the running time can be bounded by:
O

min{
√
m·log (2/pf )
ϵ ·
√
δ
,
log (2/pf )
ϵ2·δ
}

,
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 24


1:24
Wang et al.
which actually achieves the best asymptotic performance compared to the two existing solutions
when ϵ is moderate and m >
3
ϵ2·δ .
Besides, our top-k algorithm can be further extended to output the top-k nodes with the highest
PageRank scores with a running time of:
O
©­­
«
min{
p
m · log (2/pf )
ϵ ·
q
π(v∗
k)
, log (2/pf )
ϵ2 · π(v∗
k) }
ª®®
¬
,
where π(v∗
k) is the node with the k-th largest PageRank score.
7
OTHER RELATED WORK
Apart from the methods discussed in Section 2.2 , there exists a plethora of techniques for whole-
graph and top-k SSPPR queries. Those techniques, however, are either subsumed by BiPPR and
HubPPR or unable to provide worst-case accuracy guarantees. In particular, a large number of
techniques adopt the matrix-based approach, which formulates PPR values with the following
equation:
πs = α · es + (1 −α) · πs · D−1A,
(14)
where πs is a vector whose i-th element equals π(s,vi), A ∈{0, 1}n×n is the adjacency matrix
of G, and D ∈Rn×n is a diagonal matrix in which each i-th element on its main diagonal equals
the out-degree of vi. Matrix-based methods typically start from an initial guess of πs, and then
iteratively apply Equation 14 to refine the initial guess, until converge is achieved. Recent work
that adopts this approach [Fujiwara et al. 2012; Maehara et al. 2014; Shin et al. 2015; Zhu et al.
2013] propose to decompose the input graph into tree structures or sub-matrices, and utilize the
decomposition to speed up the PPR queries. The state-of-the-art approach for the single-source
and top-k PPR queries in this line of research work is BEAR proposed by Shin et al. [Shin et al.
2015]. However, as shown in [Wang et al. 2016], the best of these methods is still inferior to HubPPR
[Wang et al. 2016] in terms of query efficiency and accuracy.
There also exist methods that follow similar approaches to the forward search method [Andersen
et al. 2006] described in Section 2.2. Berkin et al. [Berkhin 2005] propose to pre-compute the
Forward Push results from several important nodes, and then use these results to speed up the
query performance. Ohsaka et al. [Ohsaka et al. 2015] and Zhang et al. [Zhang et al. 2016] further
design algorithms to update the stored Forward Push results on dynamic graphs. Jeh et al. [Jeh and
Widom 2003] propose the backward search algorithm, which (i) is the reverse variant of the Forward
Push method, and (ii) can calculates the estimated PPRs from all nodes to a target node t. Zhang
et al. [Zhang et al. 2016] also design the algorithms to update the stored backward push results
on dynamic graphs. Nonetheless, none of these solutions in this category provide approximation
guarantees for single-source or top-k PPR queries on directed graphs.
In addition, there are techniques based on the Monte-Carlo framework. Fogaras et al. [Fogaras
et al. 2005] propose techniques to pre-store the random walk results, and use them to speed up the
query processing. Nonetheless, the large space consumption of the technique renders it applicable
only on small graphs. Bahmani et al. [Backstrom and Leskovec 2011], Sarma et al. [Sarma et al. 2013]
and Lin et al. [Lin 2019] investigate the acceleration of the Monte-Carlo approach in distributed
environments. Lofgren et al. propose FastPPR [Lofgren et al. 2014], which significantly outperforms
the Monte-Carlo method in terms of query time. However, FastPPR in turn is subsumed by BiPPR
[Lofgren et al. 2016] in terms of query efficiency. In [Lofgren 2015], Lofgren further proposes to
combine a modified version of Forward Push, random walks, and the backward search algorithm
to reduce the processing time of pairwise PPR queries. Nevertheless, the time complexity of the
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 25


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:25
method remains unclear, since Lofgren does not provide any theoretical analysis on the asymptotic
performance of the method in [Lofgren 2015]. Wang et al. [Wang and Tao 2018] also consider
combine the forward random walks and the back search to accelerate the heavy hitter queries in
personalized PageRank; Wei et al. [Wei et al. 2019] find connections between SimRank and PPR,
combine the forward random walks with backward search, and propose the PRSim algorithm that
can answer SimRank queries with sublinear time on power-law graphs.
Finally, a plethora of research work [Avrachenkov et al. 2011; Bahmani et al. 2011; Fujiwara
et al. 2013, 2012; Gupta et al. 2008; Lofgren et al. 2016] study how to efficiently process the top-k
PPR queries. Gupta et al. [Gupta et al. 2008] propose to use Forward Push to return the top-k
answers. However, their solutions do not provide any approximation guarantee. Avrachenkov et
al. [Avrachenkov et al. 2011] study how to use Monte-Carlo approach to find the top-k nodes.
Nevertheless, the solution does not return estimated PPR values and does not provide any worst-
case assurance. Fujiwara et al. [Fujiwara et al. 2013, 2012] and Shin et al.[Shin et al. 2015] investigate
how to speed up the top-k PPR queries with the matrix decomposition approach. These approaches
either cannot scale to large graphs or do not provide approximation guarantees.
Most recently, Wei et al. propose the index-free TopPPR [Wei et al. 2018], which combines the
Forward Push, random walk, and the backward propagation to answer top-k PPR queries with
precision guarantees. However, as we will see in our experiments, our FORA+ actually achieves
a better performance than TopPPR when we set ρ = 0.99 on large datasets and achieves a better
trade-off among the space consumption, query efficiency, and query accuracy. The main reason
is that FORA+ can benefit from the indexing scheme while TopPPR cannot. It is also difficult
for TopPPR to benefit from indexing scheme since (i) their random walk adopts the √α-random
walk, and all the nodes visited will be used to estimate the PPR scores; (ii) the sources of random
walks in Monte-Carlo phase are generated randomly in TopPPR and it may results in poor cache
performances. In contrast, FORA+ only need to scan the index structures in order and only stores
the destinations in index structure, making it light-weighted and cache-friendly.
8
EXPERIMENTS
In this section, we experimentally evaluate our methods for whole-graph SSPPR queries and
top-k SSPPR queries. For whole-graph (resp. top-k) SSPPR queries, we include our index free
methods FORA, which includes the optimizations as mentioned in Section 4 (resp. Section 5.2), and
their index-based variant, referred to as FORA+, against the states of the art. All experiments are
conducted on a Linux machine with an Intel 2.9GHz CPU and 200GB memory.
8.1
Experimental Settings
Datasets and query sets. We use 6 real graphs: DBLP, Web-St, Pokec, LJ, Orkut, and Twitter, which
are public benchmark datasets used in recent work [Lofgren et al. 2016; Wang et al. 2016]. We
further generate two synthetic datasets using the RMAT random graph generator [Chakrabarti et al.
2004], denoted as RMAT-1 and RMAT-2 to examine the scalability of our proposed top-k algorithms.
Note that RMAT-2 includes 8.6 billion edges. Moreover, we test our methods on four different game
social networks from Tencent Games. Table 3 summarizes the statistics of the datasets. For each
dataset, we choose 50 source nodes uniformly at random, and we generate an SSPPR query from
each chosen node. In addition, we also generate 5 top-k queries from each source node, with k
varying in {100, 200, 300, 400, 500}. Note that the maximum k is set to 500 in accordance to Twitter’s
Who-To-Follow service [Gupta et al. 2013], whose first step requires deriving top-500 PPR results.
Methods. For whole-graph SSPPR queries, we compare our proposed FORA and FORA+ against
three methods: (i) the Monte-Carlo approach, dubbed as MC; (ii) the optimized BiPPR for SSPPR
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 26


1:26
Wang et al.
Table 3. Datasets. (K = 103, M = 106, B = 109)
Name
n
m
Type
Linking Site
DBLP
613.6K
2.0M
undirected
www.dblp.com
Web-St
281.9K
2.3M
directed
www.stanford.edu
Pokec
1.6M
30.6M
directed
pokec.azet.sk
LJ
4.8M
69.0M
directed
www.livejournal.com
Orkut
3.1M
117.2M
undirected
www.orkut.com
Twitter
41.7M
1.5B
directed
twitter.com
RMAT-1
41.7M
1.5B
directed
-
RMAT-2
128M
8.6B
directed
-
X0
26.1M
485.6M
undirected
tencent.com
X1
50.1M
792.0M
undirected
tencent.com
X2
58.2M
1.1B
undirected
tencent.com
X3
74.3M
1.5B
undirected
tencent.com
queries described in Section 6.1; (iii) HubPPR, which is the indexed version of BiPPR. We further
compare our FORA and FORA+ against the version without the optimization techniques (Ref.
Section 4), dubbed as FORA-Basic and FORA-Basic+ for the index-free and index-based methods,
respectively.
For top-k SSPPR queries, we compare our algorithm with the existing approximate solutions:
the single-source BiPPR, the top-k algorithm for HubPPR in [Wang et al. 2016], and the TopPPR
[Wei et al. 2018]. For BiPPR and HubPPR, we use the same ϵ, δ, and pf as FORA. For TopPPR, we
follow the settings in [Wei et al. 2018] and set ρ = 0.99. We further extend our top-k algorithm
(Ref. Algorithm 5) to the Monte-Carlo approach, and denote this algorithm as MC-Topk. We also
include the Forward Push [Andersen et al. 2006] and TPA [Yoon et al. 2018] as a baseline for top-k
SSPPR queries, and we tune their accuracy control parameters on each dataset separately, so that
their precisions for top-k PPR queries are the same as FORA on each dataset. Besides, we also
compare our FORA and FORA+ against the version without the top-k optimization techniques (Ref.
Section 5.2), dubbed as FORA-Basic and FORA-Basic+ for the index-free and index-based algorithms,
respectively.
Parameter setting. Following previous work [Lofgren et al. 2016, 2014; Wang et al. 2016], we
set δ = 1/n,pf = 1/n, and ϵ = 0.5. For our FORA and FORA+, note that the performance and / or
the index size depends on the choice of rmax. On the whole-graph queries, for FORA-Basic and
FORA-Basic+, rmax is set according to Section 3.2; we then use the balanced strategy to auto-decide
the choice of rmax for FORA; for FORA+, we include the optimization technique in Section 4.1 and
tune rmax varying from r ∗
max to 7r ∗
max where r ∗
max is the choice of rmax set according to Equation
10. We find that rmax = 2r ∗
max strikes the best trade-off, and therefore use this setting for FORA+ on
the whole-graph queries. For top-k PPR query, we also tune rmax to find the best index size for our
top-k queries and vary rmax from r ∗
max to 7r ∗
max. As we show in the experiment, when rmax is set
to r ∗
max, it achieves the best trade-off, and therefore we use this setting in our top-k evaluation. For
fair comparison, the index size of HubPPR is set to be the same as that of FORA+ for top-k SSPPR
processing and also FORA-Basic+ (for whole-graph SSPPR processing).
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 27


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:27
Table 4. Whole-graph SSPPR performance (s) (i). (K = 103)
MC
BiPPR
HubPPR
FORA-Basic
FORA
FORA-Basic+
FORA+
DBLP
14.2
3.8
2.8
0.8
0.6
0.09
0.05
Web-St
5.4
3.7
1.6
0.03
0.02
0.01
0.01
Pokec
69.1
24.9
19.6
11.26
6.3
0.9
0.4
LJ
163.5
61.4
50.8
15.5
9.9
1.2
0.6
Orkut
230.6
158.2
126.3
40.1
26.4
4.8
1.7
Twitter
4.3K
3.1K
2.4K
513.8
283.1
63.3
29.8
Table 5. Whole-graph SSPPR performance (s) (ii). (K = 103)
FORA-Basic
FORA
FORA-Basic+
FORA+
X0
527.47
259.9
66.7
31.2
X1
957.4
504.9
130.7
60.4
X2
1072.5
530.4
152.4
63.7
X3
2340.6
1163.3
216.8
97.2
8.2
Whole-Graph SSPPR Queries
In our first set of experiments, we evaluate the efficiency of each method for whole-graph SSPPR
queries on the 6 public datasets. Table 4 reports the average query time of each method. Observe
that both FORA and BiPPR achieve better query performance than MC, which is consistent with our
analysis that the time complexity of FORA and BiPPR is better than that of MC. Moreover, FORA
is at least 4 times faster than BiPPR on most of the datasets. The reason, as we explain in Section
3.2, is that BiPPR either degrades to the MC approach when the backward threshold is large, or
requires conducting a backward search from each node v in G, even if π(s,v) is extremely small.
In contrast, FORA avoids degrading to MC and tends to omit nodes with small PPR values, which
helps improve efficiency. In addition, FORA+ achieves significant speedup over FORA, and is around
10 times faster than the latter on most of the datasets. The HubPPR also improves over BiPPR, but
the improvement is far less than what FORA+ achieves over FORA. Moreover, even without any
index, FORA is still more efficient than HubPPR.
As we can observe from Table 4, with our optimization techniques introduced in Section 4, the
index-free method FORA improves over FORA-Basic by up to 1.8x. Apart from the 6 public datasets,
we further test the effectiveness of our methods on the four social networks from company X. We
omit the results for the baseline methods (MC, BiPPR, and HubPPR) since they incur prohibitive
processing costs. As shown in Table 5, FORA still improves over FORA-Basic by more than 2x almost
on all datasets, which demonstrates the effectiveness of our proposed optimization technique for
online algorithms. For the index-based method, FORA improves over FORA+ by at least twice on
almost all datasets, and up to 2.8x. As shown in Table 8, the space consumption required by FORA+
is twice as that of FORA-Basic+, which demonstrates that our optimization technique achieves a
good trade-off between query time and space consumption.
8.3
Top-k SSPPR Queries
In our second set of experiments, we evaluate the efficiency and accuracy of each method for
top-k SSPPR queries. For our methods, we only include our FORA and FORA+ that includes the
optimizations presented in Section 5.2 to avoid the figures being too crowded. We will examine the
effectivess of our optimization techniques in the next set of experiments.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 28


1:28
Wang et al.
BiPPR
MC-TopK
FORA
HubPPR
Forward Push
TPA
FORA+
TopPPR
101
102
103
104
100
200
300
400
500
running time (ms)
k
102
103
104
105
100
200
300
400
500
running time (ms)
k
(a) DBLP
(b) Pokec
102
103
104
105
100
200
300
400
500
running time (ms)
k
102
103
104
105
106
107
100
200
300
400
500
running time (ms)
k
(c) Orkut
(d) Twitter
Fig. 1. Top-k SSPPR query efficiency: varying k.
8.3.1
Top-k query efficiency. Figures 1 reports the average query time of each method on four
representative datasets: DBLP, Pokec, Orkut, and Twitter. (The results on the other two datasets
are qualitatively similar, and are omitted due to the space constraint.) Note that the y-axis is in
log-scale. Recall that Forward Push provides no approximation guarantee, and we tune the rmax on
each dataset separately, so that it provides the same precision for top-500 SSPPR queries as our
FORA algorithm does. Similarly, for TPA [Yoon et al. 2018], we tune their parameters so that it
provides the best possible precision.
The main observation is that our FORA+ achieves the best performance on all the datasets. For
instance, on Twitter dataset with k = 500, our FORA+ provides similar or better accuracy and NDCG
as competitors, and runs 2x faster than TopPPR, two order of magnitude faster than MC-Topk,
and more than 500x faster than Forward Push, TPA, BiPPR, and HubPPR. This is expected since
our FORA+ applies an iterative approach to refine the top-k answers and terminates immediately
whenever the answer could provide the desired approximation guarantee; it further uses the
indexing scheme to reduce the expensive costs of random walks.
Our FORA is the fastest online algorithm except TopPPR since TopPPR uses a more advanced
filter-refinement paradigm to answer the top-k queries. However, their proposed approach does not
benefit from indexing scheme, and is outperformed by our FORA+. It is also difficult for TopPPR to
benefit from indexing scheme since (i) their random walk adopts the √α-random walk, and all the
nodes visited will be used to estimate the PPR scores; (ii) the sources of random walks in Monte-
Carlo phase are generated randomly in TopPPR and it may results in poor cache performances. In
contrast, FORA+ only need to scan the index structures in order and only stores the destinations in
index structure, making it light-weighted and cache-friendly.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 29


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:29
BiPPR
MC-TopK
FORA
HubPPR
Forward Push
TPA
FORA+
TopPPR
0.96
0.97
0.98
0.99
1.0
100
200
300
400
500
precision
k
0.96
0.97
0.98
0.99
1.0
100
200
300
400
500
precision
k
(a) DBLP
(b) Pokec
0.96
0.97
0.98
0.99
1.0
100
200
300
400
500
precision
k
0.96
0.97
0.98
0.99
1.0
100
200
300
400
500
precision
k
(c) Orkut
(d) Twitter
Fig. 2. Top-k SSPPR query accuracy: varying k.
Another observation is that after extending the MC approach with our top-k algorithm, MC-
Topk achieves more than 20x speedup on Twitter over its single-source alternative. This further
demonstrates the effectiveness of our top-k algorithm proposed in Section 5.2, which improves the
time complexity to O(
log n
ϵ2·π(s,v∗
k )). However, our FORA and FORA+ are still far more efficient than
MC-Topk since FORA and FORA+ explores the forward push to reduce the random walk costs.
Finally, with our index structure, FORA+ further improves over FORA by an order of magnitude,
which demonstrates the effectiveness of the index structure. Notably, on the Twitter social network
with 1.5 billion edges, our FORA+ can answer the top-500 query in 0.8 second.
8.3.2
Top-k query accuracy. To compare the accuracy of the top-k results returned by each method,
we first calculate the ground-truth answer of the top-k queries using the Power Iteration [Page
et al. 1999] method with 100 iterations. Afterwards, we evaluate the top-k results of each algorithm
by their precision and NDCG [Järvelin and Kekäläinen 2000] with respect to the ground truth.
Note that the precision and recall are the same for the top-k SSPPR queries, and is the fraction of
nodes returned by the top-k algorithm that are real top-k nodes. For NDCG, let s be the query node,
v1,v2, · · · ,vk be the k nodes returned by the top-k algorithm, and v∗
1,v∗
2, · · · ,v∗
k be the true top-k
nodes. Then, the NDCG is defined as
1
Zk
Ík
i=1
2π (s,vi )−1
log (i+1) , where Zk = Ík
i=1
2π (s,v∗
k )−1
log (i+1) .
Figure 2 (resp. Figure 3) show the accuracy (resp. NDCG) of the top-k query algorithms on four
datasets: DBLP, Pokec, Orkut, and Twitter. Observe that all methods except TPA consistently provide
high precisions. In the meantime, notice that our FORA+ consistently provides similar precision as
TopPPR and sometimes even slightly better precision than TopPPR on all the tested datasets. In
terms of NDCG, all methods achieve very high NDCG scores, above 0.999 on all datasets.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 30


1:30
Wang et al.
BiPPR
MC-TopK
FORA
HubPPR
Forward Push
TPA
FORA+
TopPPR
 0.999
 0.9992
 0.9994
 0.9996
 0.9998
 1
100
200
300
400
500
NDCG
k
 0.999
 0.9992
 0.9994
 0.9996
 0.9998
 1
100
200
300
400
500
NDCG
k
(a) DBLP
(b) Pokec
 0.999
 0.9992
 0.9994
 0.9996
 0.9998
 1
100
200
300
400
500
NDCG
k
 0.999
 0.9992
 0.9994
 0.9996
 0.9998
 1
100
200
300
400
500
NDCG
k
(c) Orkut
(d) Twitter
Fig. 3. Top-k SSPPR query NDCG: varying k.
8.3.3
Scalability of Top-k algorithms. In this section, we examine the scalability of our FORA+
using synthetic datasets. We first generate a synthetic dataset with the same size as Twitter and
then generate a graph with 8.6 billion edges. The results are reported in Table 6. As we can see, our
FORA+ achieves 3x improvement over TopPPR on both datasets while providing the same accuracy
and NDCG. As we will see in Section 8.5, the space consumption of FORA+ is only 2x and 1.5x that
of TopPPR on RMAT-1 and RMAT-2, respectively. This demonstrates that FORA+ achieves a better
trade-off between query efficiency and space consumption when providing the same accuracy for
the top-k queries.
8.4
Effectiveness of the Top-k optimization
In this set of experiment, we evaluate the effectiveness of the new top-k algorithm proposed in
Section 5.2, which provides improved time complexity, and reduces the time to calculate the bounds
for each node. We present the results for 6 representative datasets: DBLP, Pokec, Orkut, Twitter, X2,
and X3.
Figures 4(a)-(f) demonstrate the running time of FORA and FORA+, against the versions without
the optimization techniques in Section 5.2, referred to as FORA-Basic and FORA-Basic+ for the
index-free and index-based solution, respectively. As we can observe, with the new algorithm,
FORA (resp. FORA+ improves over FORA-Basic (resp. FORA-Basic+) by a large margin. For instance,
on Twitter dataset, FORA (resp. FORA+) improves over FORA-Basic (resp. FORA-Basic+) by around
4x (resp. 6x). The main reason for the significant improvement are two-fold: (i) the time complexity
of FORA and FORA+ depend on
1
π(s,v∗
k ) while FORA-Basic and FORA-Basic+ depend on 1
n ; (ii) FORA
and FORA+ avoids the expensive bound calculation part that are required by FORA-Basic and
FORA-Basic+.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 31


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:31
Table 6. Scalability test on synthetic datasets. (K = 500)
Query Time
Precision
NDCG
RMAT-1
RMAT-2
RMAT-1
RMAT-2
RMAT-1
RMAT-2
FORA+
17.4
149.5
0.993
0.995
0.9999
0.9999
TopPPR
51.1
481.0
0.993
0.995
0.9999
0.9999
FORA-Basic
FORA
FORA+
FORA-Basic+
10−2
10−1
100
100
200
300
400
500
Running time (s)
k
10−1
100
101
100
200
300
400
500
Running time (s)
k
(a) DBLP
(b) Pokec
10−1
100
101
100
200
300
400
500
Running time (s)
k
10−1
100
101
100
200
300
400
500
Running time (s)
k
(c) Orkut
(d) Twitter
10−1
100
101
100
200
300
400
500
Running time (s)
k
10−1
100
101
100
200
300
400
500
Running time (s)
k
(e) X2
(f) X3
Fig. 4. Effectiveness of top-k Optimization: query efficiency.
Next, we report the accuracy of the four methods on the 6 datasets as shown in Figures 5(a)-(f).
As we can observe, all four methods provide similarly high accuracy for the top-k queries on all
datasets. To explain, all four methods share the similar spirit by adaptively refine the top-k answer
and return the approximate answer with theoretical guarantees. Therefore, all the four methods
provide similarly high accuracy.
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 32


1:32
Wang et al.
FORA-Basic
FORA
FORA+
FORA-Basic+
0.96
0.97
0.98
0.99
1.0
100
200
300
400
500
precision
k
0.96
0.97
0.98
0.99
1.0
100
200
300
400
500
precision
k
(a) DBLP
(b) Pokec
0.96
0.97
0.98
0.99
1.0
100
200
300
400
500
precision
k
0.96
0.97
0.98
0.99
1.0
100
200
300
400
500
precision
k
(c) Orkut
(d) Twitter
0.96
0.97
0.98
0.99
1.0
100
200
300
400
500
precision
k
0.96
0.97
0.98
0.99
1.0
100
200
300
400
500
precision
k
(e) X2
(f) X3
Fig. 5. Effectiveness of top-k Optimization: query accuracy.
8.5
Preprocessing Costs
Finally, we inspect the preprocessing costs of our methods against alternatives. We first examine
the preprocessing time of the index-based methods: FORA+, FORA-Origin+, HubPPR, and TPA.
Note that the rmax of FORA+ for whole-graph and top-k queries are different, and therefore the
preprocessing time are shown as seperately in Table 7. The choice of tuned rmax of FORA+ is the
same as that of FORA-Basic, and therefore their preprocessing time are the same. As shown in
Table 7, the preprocessing time of FORA+, FORA-Basic+, HubPPR, and TPA are all moderate. On the
largest dataset X3, our FORA+ for whole graph SSPPR queries (resp. for top-k SSPPR queries) can
still finish index construction in less than 3 hours (resp. less than 1 and half an hour), which is more
than compensated by its high query performance as shown in Table 4. Besides, this preprocessing
time can be further significantly reduced by parallelizing the index construction process.
Next, we examine the space consumption of all methods. Note that each method will need to
store at least a copy of the graph. For MC, FORA, and TPA, they can store only a single copy of the
input graph (each node stores the out-neighbor list). However, for HubPPR, BiPPR and TopPPR, they
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 33


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:33
Table 7. Preprocessing time.
Datasets
HubPPR
TPA
FORA+
(for
whole graph)
FORA-Basic+ & FORA+
(for top-k)
DBLP
26.4
4.4
7.6
3.6
Web-St
9.3
1.3
3.2
1.5
Pokec
90.6
42.5
77.1
34.6
LJ
279.9
112.5
181.3
81.2
Orkut
530.6
177.3
383.5
165.9
Twitter
5088.6
3112.3
5130.4
2255.4
RMAT-1
-
-
-
2695.2
RMAT-2
-
-
-
12076.8
X0
-
-
2031.2
967.14
X1
-
-
5244.5
2428.6
X2
-
-
5721.7
2602.9
X3
-
-
8836.4
4213.5
Table 8. Space consumption.
Datasets
MC/FORA
BiPPR/TopPPR
HubPPR TPA
FORA-Basic+
&
FORA+ (for top-k)
FORA+
(for
whole-graph)
DBLP
18.4MB
36.8MB
127.6MB 23.3MB
109.2MB
200.1MB
Web-St
10.4MB
20.8MB
66.3MB
12.6MB
55.9MB
101.4MB
Pokec
130.8MB
261.5MB
673.5MB 143.6MB 542.7MB
954.6MB
LJ
295.2MB
590.5MB
1.7GB
333.6MB 1.4GB
2.5GB
Orkut
950.1MB
1.9GB
3.5GB
974.9MB 2.6GB
4.2GB
Twitter
6.2GB
12.5GB
25.1GB
6.5GB
18.8GB
31.4GB
RMAT-1
6.2GB
12.5GB
-
-
20.0GB
-
RMAT-2
33.3GB
66.5GB
-
-
96.3GB
-
X0
2.0GB
-
-
-
7.5GB
13.1GB
X1
3.2GB
-
-
-
13.2GB
23.2GB
X2
4.6GB
-
-
-
17.5GB
30.4GB
X3
6.0GB
-
-
-
22.6GB
39.2GB
need to store two copies of the graph (each node stores an out-neighbor and an in-neighbor list)
for efficient random walks and backward propagation.
Table 8 reports the space consumption of all methods. As we can observe, the index size of our
FORA+ for whole-graph queries and top-k queries are no more than 7.5x and 4x of the original
graph, respectively. The space consumption is more than compensated by the superb performance
of FORA+, where we can answer a whole-graph query within 30 seconds and top-k query within
0.9 second on the 1.5 billion edge Twitter graph, which improves over the index-free FORA by
more than an order of magnitude on almost all datasets. This demonstrates the effectiveness and
efficiency of our indexing scheme.
Compared to TopPPR, FORA+ achieves 2x, 3x, and 3.4x improvement on Twitter, RMAT-1, and
RMAT-2, with only 1.5x, 1.6x, and 1.4x space consumption, respectively. The experimental results
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 34


1:34
Wang et al.
Web-St
DBLP
Pokec
Orkut
LJ
Twitter
0.00
0.25
0.50
0.75
1
3
5
7
running time (s)
rmax
0
20
40
60
1
3
5
7
running time (s)
rmax
(a)
(b)
Fig. 6. Tunning rmax for whole-graph SSPPR queries (×r∗max)
Web-St
DBLP
Pokec
Orkut
LJ
Twitter
0.00
0.05
0.10
0.15
0.20
1
3
5
7
running time (s)
rmax
0.0
0.2
0.4
0.8
1.0
1
3
5
7
running time (s)
rmax
(a)
(b)
Fig. 7. Tunning rmax for top-k SSPPR queries (×r∗max)
.
demonstrate that our proposed methods achieve a good trade-off between the space consumption
and query efficiency when providing query answers with identical accuracy.
8.6
Tuning rmax
Finally, we examine the trade-off between the space consumption and query performance of our
FORA+ algorithm by tuning rmax for whole graph queries and top-k queries. Let r ∗
max be the rmax
value set according to Section 3.2. We then vary rmax from r ∗
max to 7r ∗
max. Notice that, the index size
is proportional to rmax and let y be the index size when rmax = r ∗
max. Then, if rmax = 3r ∗
max, then
the index size will be 3y. As we can observe, when we increase the index size for FORA+, the query
performance also improves on almost all datasets for both whole-graph queries and top-k queries.
To explain, by increasing the index size, FORA+ avoids the expensive random walks and thus saving
the query time. However, from the experiment, we can observe that when rmax = 2r ∗
max (resp.
rmax = r ∗
max), FORA+ actually achieves the best trade-off between the query performance and
space consumption on whole-graph queries (resp. top-k queries), and hence in our experiment, we
set rmax = 2r ∗
max (resp. rmax = r ∗
max) for all the whole-graph queries (resp. top-k queries).
9
CONCLUSION
We present FORA, a novel algorithm for approximate single-source personalized PageRank com-
putation. The main ideas include (i) combining Monte-Carlo random walks with Forward Push
in a non-trivial and optimized way (ii) pre-computing and indexing random walk results and (iii)
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 35


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:35
additional pruning based on top-k selection. Compared to existing solutions, FORA involves a
reduced number of random walks, avoids expensive backward searches, and provides rigorous
guarantees on result quality. Extensive experiments demonstrate that FORA outperforms existing
solutions by a large margin, and enables fast responses for top-k SSPPR searches on very large
graphs with little computational resource.
REFERENCES
Reid Andersen, Christian Borgs, Jennifer T. Chayes, John E. Hopcroft, Vahab S. Mirrokni, and Shang-Hua Teng. 2007. Local
Computation of PageRank Contributions. In WAW. 150–165.
Reid Andersen, Fan R. K. Chung, and Kevin J. Lang. 2006. Local Graph Partitioning using PageRank Vectors. In FOCS.
475–486.
Konstantin Avrachenkov, Nelly Litvak, Danil Nemirovsky, Elena Smirnova, and Marina Sokol. 2011. Quick Detection of
Top-k Personalized PageRank Lists. In Algorithms and Models for the Web Graph - 8th International Workshop, WAW 2011,
Atlanta, GA, USA, May 27-29, 2011. Proceedings. 50–61.
Lars Backstrom and Jure Leskovec. 2011. Supervised random walks: predicting and recommending links in social networks.
In WSDM. 635–644.
Bahman Bahmani, Kaushik Chakrabarti, and Dong Xin. 2011. Fast personalized PageRank on MapReduce. In SIGMOD.
973–984.
Pavel Berkhin. 2005. Survey: A Survey on PageRank Computing. Internet Mathematics 2, 1 (2005), 73–120.
Deepayan Chakrabarti, Yiping Zhan, and Christos Faloutsos. 2004. R-MAT: A Recursive Model for Graph Mining. In SDM.
442–446.
Fan R. K. Chung and Lincoln Lu. 2006. Survey: Concentration Inequalities and Martingale Inequalities: A Survey. Internet
Mathematics 3, 1 (2006), 79–127.
Dániel Fogaras, Balázs Rácz, Károly Csalogány, and Tamás Sarlós. 2005. Towards Scaling Fully Personalized PageRank:
Algorithms, Lower Bounds, and Experiments. Internet Mathematics 2, 3 (2005), 333–358.
Yasuhiro Fujiwara, Makoto Nakatsuji, Hiroaki Shiokawa, Takeshi Mishima, and Makoto Onizuka. 2013. Efficient ad-hoc
search for personalized PageRank. In SIGMOD. 445–456.
Yasuhiro Fujiwara, Makoto Nakatsuji, Takeshi Yamamuro, Hiroaki Shiokawa, and Makoto Onizuka. 2012. Efficient personal-
ized pagerank with accuracy assurance. In KDD. 15–23.
Manish S. Gupta, Amit Pathak, and Soumen Chakrabarti. 2008. Fast algorithms for topk personalized pagerank queries. In
WWW. 1225–1226.
Pankaj Gupta, Ashish Goel, Jimmy Lin, Aneesh Sharma, Dong Wang, and Reza Zadeh. 2013. Wtf: The who to follow service
at twitter. In WWW. 505–514.
Taher H. Haveliwala. 2002. Topic-sensitive PageRank. In WWW. 517–526.
Kalervo Järvelin and Jaana Kekäläinen. 2000. IR evaluation methods for retrieving highly relevant documents. In SIGIR.
41–48.
Glen Jeh and Jennifer Widom. 2003. Scaling personalized web search. In WWW. 271–279.
Wenqing Lin. 2019. Distributed Algorithms for Fully Personalized PageRank on Large Graphs. In The World Wide Web
Conference, WWW 2019, San Francisco, CA, USA, May 13-17, 2019. 1084–1094.
Peter Lofgren. 2015. Efficient Algorithms for Personalized PageRank. CoRR abs/1512.04633 (2015).
Peter Lofgren, Siddhartha Banerjee, and Ashish Goel. 2016. Personalized pagerank estimation and search: A bidirectional
approach. In WSDM. 163–172.
Peter A Lofgren, Siddhartha Banerjee, Ashish Goel, and C Seshadhri. 2014. Fast-ppr: Scaling personalized pagerank
estimation for large graphs. In KDD. 1436–1445.
Takanori Maehara, Takuya Akiba, Yoichi Iwata, and Ken-ichi Kawarabayashi. 2014. Computing personalized PageRank
quickly by exploiting graph structures. PVLDB 7, 12 (2014), 1023–1034.
Naoto Ohsaka, Takanori Maehara, and Ken-ichi Kawarabayashi. 2015. Efficient PageRank Tracking in Evolving Networks.
In SIGKDD 2015. 875–884.
Lawrence Page, Sergey Brin, Rajeev Motwani, and Terry Winograd. 1999. The PageRank citation ranking: bringing order to
the web. (1999).
Atish Das Sarma, Anisur Rahaman Molla, Gopal Pandurangan, and Eli Upfal. 2013. Fast Distributed PageRank Computation.
In ICDCN. 11–26.
Kijung Shin, Jinhong Jung, Lee Sael, and U. Kang. 2015. BEAR: Block Elimination Approach for Random Walk with Restart
on Large Graphs. In SIGMOD. 1571–1585.
Sibo Wang, Youze Tang, Xiaokui Xiao, Yin Yang, and Zengxiang Li. 2016. HubPPR: Effective Indexing for Approximate
Personalized PageRank. PVLDB 10, 3 (2016), 205–216. http://www.vldb.org/pvldb/vol10/p205-wang.pdf
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 36


1:36
Wang et al.
Sibo Wang and Yufei Tao. 2018. Efficient Algorithms for Finding Approximate Heavy Hitters in Personalized PageRanks. In
SIGMOD. 1113–1127.
Sibo Wang, Renchi Yang, Xiaokui Xiao, Zhewei Wei, and Yin Yang. 2017. FORA: Simple and Effective Approximate
Single-Source Personalized PageRank. In SIGKDD. 505–514.
Zhewei Wei, Xiaodong He, Xiaokui Xiao, Sibo Wang, Yu Liu, Xiaoyong Du, and Ji-Rong Wen. 2019. PRSim: Sublinear Time
SimRank Computation on Large Power-Law Graphs. In SIGMOD. 1042–1059.
Zhewei Wei, Xiaodong He, Xiaokui Xiao, Sibo Wang, Shuo Shang, and Ji-Rong Wen. 2018. TopPPR: Top-k Personalized
PageRank Queries with Precision Guarantees on Large Graphs. In SIGMOD. 441–456.
Minji Yoon, Jinhong Jung, and U Kang. 2018. TPA: Fast, Scalable, and Accurate method for Approximate Random Walk with
Restart on Billion Scale Graphs. In ICDE.
Hongyang Zhang, Peter Lofgren, and Ashish Goel. 2016. Approximate Personalized PageRank on Dynamic Graphs. In KDD.
1315–1324.
Fanwei Zhu, Yuan Fang, Kevin Chen-Chuan Chang, and Jing Ying. 2013. Incremental and Accuracy-Aware Personalized
PageRank through Scheduled Approximation. PVLDB 6, 6 (2013), 481–492.
APPENDIX
A
PROOF OF THEOREM
Proof of Theorem 5.1. Given ωj, we can derive that:
Pr[|π(s,t) −ˆπ(s,t)| ≥ϵ · π(s,t)] ≤2 · exp

−ϵ2 · ωj · π(s,t)
2 + 2a · ϵ/3

.
Since a ≤1 and π(s,t) ≥π ◦(s,t), and π(s,t) ≥LBj−1(t), we can derive that:
Pr[|π(s,t) −ˆπ(s,t)| ≥ϵ · π(s,t)] ≤
2 exp
 
−
ϵ2 · ωj · max{π ◦
j (s,v), LBj−1(s,v)}
2 + 2ϵ/3
!
.
Let p′
f equal the RHS of the above inequality. We have ϵ ≥
r
3 log (2/p′
f )
ωj ·max{π ◦
j (s,v),LBj−1(s,v)} .
By setting ϵj =
r
3 log (2/p′
f )
ωj ·max{π ◦
j (s,v),LBj−1(s,v)}, we can derive that ˆπj(s,v)/(1 + ϵj) ≤π(s,v) ≤
ˆπj(s,v)/(1 −ϵj) holds with 1 −p′
f probability. Similarly, we have
Pr[|π(s,t) −ˆπ(s,t)| ≥ϵ · π(s,t)] ≤2 exp

−
λ2 · ω
rsum · (2π(s,t) + 2λ/3)

Let p′
f equal the RHS of the above inequality, and note that π(s,t) ≤UBj−1(t). This helps us derive
the designed bound for λj.
Proof of Theorem 5.2. We apply a similar technique in [Wang et al. 2016]. If LBj(v′
i) · (1 + ϵ) >
UBj(v′
i). Then, it can be derived that
ˆπ(v′
i) ≤UBj(v′
i) ≤LBj(v′
i) · (1 + ϵ) ≤(1 + ϵ) · π(s,v′
i).
ˆπ(v′
i) ≥LBj(v′
i) ≥UBj(v′
i)/(1 + ϵ) ≥(1 −ϵ) · π(s,v′
i).
Hence, v′
1, · · · ,v′
k satisfy Equation 2. Let v1, · · · ,vk be the k nodes that have the top-k exact
PPR values. Assume that all bounds are correct, then as LB(v′
l) ≥δ, it indicates that the top-k
PPR values are no smaller than δ. In this case, all the top-k nodes should satisfy ϵ-approximation
guarantee, i.e., they satisfy that UB(vi) < (1 + ϵ) · LB(vi)/(1 −ϵ).
Let U B′
j(1),U B′
j(2), · · ·UB′
j(k) be the top-k largest PPR upper bounds in the j-th iteration. Note
that, the i-th largest PPR satisfy that UB′
j(i) ≥π(s,vi) ≥LBj(s,v′
i).
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.


## Page 37


Efficient Algorithms for Approximate Single-Source Personalized PageRank Queries
1:37
Now assume that one of the upper bounds say UB′
j(i) is not from UB(v1), · · · ,UB(vk). If it
satisfies that LBj(v′
k) · (1 + ϵ) ≥UB′
j(i), it indicates that LBj(v′
i) · (1 + ϵ) ≥UB′
j(i) for all nodes.
Hence, we update the node whose upper bound is minimum among UBj(v′
1), · · · ,UBj(v′
1), we can
still guarantee that LBj(v′
i) · (1 + ϵ) > UBj(v′
i). We repeat this process until UBj(v′
1), · · · ,UBj(v′
k)
are the top-k upper bounds. On the other hand, let U be the set of nodes such that, the node u ∈U
satisfies that U Bj(u) < LBj(v′
k). Then it is still possible that these nodes are from the exact top−k
answers. However, recall that if a node u ∈U is from the top-k, it should satisfy that UB(u) <
(1+ϵ)·LB(u)/(1−ϵ). As a result, if there exists no nodeu ∈U such thatUB(u) < (1+ϵ)·LB(u)/(1−ϵ),
then no node u ∈U is from the top-k answers, in which case it will not affect the approximation
guarantee.
Afterwards, we proceed a bubble sort on the top-k upper bounds in decreasing order. If we
replace two upper bounds UBj(v′
x) and UBj(v′
y) with x < y, then UBj(v′
x) < UBj(v′
y). Also
LBj(v′
x) > LBj(v′
y) from the definition. As
UBj(v′
x)/LBj(v′
y) < UBj(v′
y)/LBj(v′
y) ≤(1 + ϵ)
UBj(v′
y)/LBj(v′
x) < UBj(v′
y)/LBj(v′
y) ≤(1 + ϵ)
When the sort finishes, the inequations still hold. We then have
UB′
j(1) ≤(1 + ϵ) · LBj(v′
i) · · · ,UB′
j(k) ≤(1 + ϵ) · LBj(v′
k).
Also note that
ˆπ(v′
i) ≥LBj(v′
i) ≥
1
1 + ϵUB′
j(i) ≥(1 −ϵ) · π(s,vi),
for all i ∈[1,k]. So, the answer provides approximation guarantee if the bounds from the first to the
j-th iteration are all correct. By applying the union bound, we can obtain that the approximation is
guaranteed with probability at least 1 −n · j · p′
f .
ACM Trans. Datab. Syst., Vol. 1, No. 1, Article 1. Publication date: August 2019.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1908_10583v1_efficient_algorithms_for_approximate_single_source_personalized_pagerank_queries
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1908_10583V1_EFFICIENT_ALGORITHMS_FOR_APPROXIMATE_SINGLE_SOURCE_PERSONALIZED_PAGERANK_QUERIES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1705.10977v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1705.10977v2_Time_is_What_Prevents_Everything_from_Happening_at_Once__Propagation_Time-consci

> Source: 1705.10977v2_Time_is_What_Prevents_Everything_from_Happening_at_Once__Propagation_Time-consci.pdf

> Pages: 14

---


## Page 1


arXiv:1705.10977v2  [cs.DB]  27 Sep 2017
Time is What Prevents Everything from Happening
at Once: Propagation Time-conscious Inﬂuence
Maximization
Hui Li #1, Sourav S Bhowmick ∗2, Jiangtao Cui †3, Jianfeng Ma #4
# School of Cyber Engineering, Xidian University, China
1 hli@xidian.edu.cn,
4 jfma@mail.xidian.edu.cn
∗School of Computer Science and Engineering, Nanyang Technological University, Singapore
2 assourav@ntu.edu.sg
† School of Computer Science and Technology, Xidian University, China
3 cuijt@xidian.edu.cn
Abstract—The inﬂuence maximization (IM) problem as deﬁned
in the seminal paper by Kempe et al. has received widespread
attention from various research communities, leading to the
design of a wide variety of solutions. Unfortunately, this classical
IM problem ignores the fact that time taken for inﬂuence
propagation to reach the largest scope can be signiﬁcant in real-
world social networks, during which the underlying network
itself may have evolved. This phenomenon may have considerable
adverse impact on the quality of selected seeds and as a result
all existing techniques that use this classical deﬁnition as their
building block generate seeds with suboptimal inﬂuence spread.
In this paper, we revisit the classical IM problem and propose
a more realistic version called PROTEUS-IM (Propagation Time-
conscious Inﬂuence Maximization) to replace it by addressing the
aforementioned limitation. Speciﬁcally, as inﬂuence propagation
may take time, we assume that the underlying social network may
evolve during inﬂuence propagation. Consequently, PROTEUS-
IM aims to select seeds in the current network to maximize
inﬂuence spread in the future instance of the network at the
end of inﬂuence propagation process without assuming complete
topological knowledge of the future network. We propose a
greedy and a Reverse Reachable (RR) set-based algorithms called
PROTEUS-GENIE and PROTEUS-SEER, respectively, to address
this problem. Our algorithms utilize the state-of-the-art Forest
Fire Model for modeling network evolution during inﬂuence
propagation to ﬁnd superior quality seeds. Experimental study
on real and synthetic social networks shows that our proposed
algorithms consistently outperform state-of-the-art classical IM
algorithms with respect to seed set quality.
I. INTRODUCTION
With the emergence of large-scale online social networking
applications in the last decade, inﬂuence maximization in
online social networks has been widely considered as one
of the fundamental and popular problems in social data
management and analytics. In the seminal paper by Kempe
et al. [1], this problem is deﬁned as follows. Given a social
network G as well as an inﬂuence propagation (or cascade)
model, the problem of inﬂuence maximization (IM) is to ﬁnd
a set of initial users of size k (referred to as seeds) so that
they eventually inﬂuence the largest number of individuals
(referred to as inﬂuence spread) in G. Effective solutions
to the IM problem open up opportunities for commercial
companies to design intelligent recommendation systems and
viral marketing strategies [2].
Kempe et al. [1] proved that the IM problem is NP-hard, and
presented an elegant greedy approximate algorithm applicable
to several popular cascade models, including the independent
cascade (IC) model, and etc. A key strength of this algorithm
lies in its guarantee that the inﬂuence spread is within (1−1/e)
of the optimal inﬂuence spread where e is the base of the
natural logarithm. Since then a large body of work (e.g., [3],
[4], [5], [6]) have been proposed to improve the efﬁciency of
IM techniques as well as quality of inﬂuence spread. Variants
of this classical IM problem have also been proposed in recent
times such as topic-aware IM [7], conformity-aware IM [8],
and competitive IM [9]. In a latest research, [10] provides a
uniform benchmark to evaluate these classical IM solutions. In
summary, this elegant work by Kempe et al. has had signiﬁcant
inﬂuence on the research community1.
A. Limitations of the Deﬁnition of Classical IM Problem
The classical
IM problem and its solution in [1] are
grounded on the following implicit assumption. Assume that
it takes t time for inﬂuence spread from seed set S to reach
the largest number of nodes in a social network G. Then,
t is assumed to be small so that the topology of G can be
assumed to remain static during t. Consequently, the topology
of G is completely known during the propagation process.
This is important as the dynamics of inﬂuence propagation
for all cascade models in the classical IM problem demands
that neighbors of a node v are known. For example, consider
the popular IC model. In this model, we start with an initial
set of active nodes, and the inﬂuence propagation unfolds in
discrete steps where at step i when a node v becomes active,
it gets a single chance to activate each of its inactive neighbor
w with probability p. If v is successful in activating w, then w
will become active in step i + 1. This process continues until
1 This work has garnered over 4,800 citations in Google Scholar and
received the test-of-time award in ACM KDD 2014.


## Page 2


no more activations are possible. Clearly, successful realization
of this propagation process requires that the neighbors of each
node are known so that inﬂuence can be propagated to its
active neighbor(s).
A large volume of subsequent work on inﬂuence maximiza-
tion (e.g., [3], [4], [6], [8]) also implicitly or explicitly make
the above assumption as they are built on top of the classical
IM problem [1]. Unfortunately, recent studies reveal that the
aforementioned assumption may not hold in practice as time
taken for inﬂuence propagation is signiﬁcant, during which the
topology of these networks evolves rapidly. For instance, [11]
tested the spread of web advertisements through emails and
websites and justiﬁed that on average it takes 1.5 days for an
intermediary node to propagate the messages and the spread
will not reach the largest scope until at least 8 propagations.
That is, each cascade of web advertisement may consume up
to two or more weeks. Meanwhile, it has been reported that
active users of Facebook increased from just a million in 2004
to 1 billion in 2012, 8.57% growth per month on average [12].
Similarly, the number of active users in Twitter increased from
100 million in September 2011 to 200 million in December
2012, 4.73% growth per month [13]. In particular, it has been
shown in [14] that the number of nodes for Answers, Delicious
and LinkedIn grows quadratically to the elapsed weeks; and for
Flickr, it grows exponentially. In summary, the above studies
show that inﬂuence propagation can take signiﬁcant amount of
time to reach the largest scope (several weeks) during which
social networks evolve.
Due to the aforementioned mismatch between the charac-
teristics of real-world social networks and assumption made
by the classical IM problem, the quality of seeds selected
by a state-of-the-art IM algorithm is adversely impacted. In
particular, the seeds S selected from G may not maximize the
spread of inﬂuence due to the evolutionary nature of G during
inﬂuence propagation process. To elaborate further, suppose
the inﬂuence propagation of S takes t′ time and terminates
when there is no other node that can be activated. Meanwhile,
the social network G = (V, E) at time point t evolves to
G′ = (V ′, E′) during t′. Note that the classical IM problem
aims to compute S from G at t ignoring its evolution during t′.
Importantly, S may not exhibit the maximal expected inﬂuence
in G′. That is, the seed set S′ in G′ may not necessarily be
identical to S. Note that it is not possible in practice to run
a state-of-the-art IM algorithm on G′ at time t to get S′ and
then select k seeds from S′ ∩V as S, which is the “best” seed
set in G that exhibits the maximal inﬂuence in G′. This is
because it is unrealistic to assume that the complete topology
of G′ is known at time t. We further illustrate this problem
with the following example.
Example 1: Suppose we wish to select one seed (k = 1) at
time t on the social network G depicted in Fig. 1(a). A state-
of-the-art IM algorithm will run on G to select S = {v1} as
the seed. As inﬂuence propagation may take t′ time, assume
that during this period G evolves to G′ as shown in Fig. 1(b).
Speciﬁcally, two new nodes (i.e., v6 and v7) and three edges
(i.e., −−→
v4v5, −−→
v4v7 and −−→
v3v6) are added during this time period.
v1
v2
v3
v5
v4
v5
v3
v6
v4
v7
v1
v2
v5
v3
v6
v4
v7
v1
v2
v8
Fig. 1: (a) The original network G at time t. (b) The network
G′ at time t′. (c) The network G′′ at time t′′.
Consequently, v1 may not inﬂuence the most number of nodes
after the completion of inﬂuence propagation as during this
period the topology of G has evolved to G′. In fact, v4 is a
better choice as it may inﬂuence more nodes than v1 after t′.
At ﬁrst glance, it may seem that this problem can be easily
addressed by running the IM technique on G′ instead of G,
which may result in seed set S = {v4}. Unfortunately, it is
difﬁcult at time t to predict the topology of G after time t′ > t
(i.e., G′) in order to run an IM technique on the latter! In
other words, the complete topology of the network at time t′ is
unknown at time t. Observe that this problem occurs regardless
of when the IM algorithm is run. For instance, suppose it
is run at time t′ on G′ to select S = {v4}. However, now
G′ may have evolved to G′′ (Fig. 1(c)) during the inﬂuence
propagation process and as a result v4 may not be the optimal
seed for maximizing inﬂuence anymore.
Fundamentally, the manifestation of this problem is due to
the maximization of inﬂuence on a network instance G at time
t (which is consistent with the classical IM problem deﬁnition)
instead of discovering seeds that maximize inﬂuence on a
future instance of the network (i.e., G′ at time t′) assuming that
inﬂuence propagation takes t′ > t time. However, as remarked
earlier it is difﬁcult to know the exact topology of the future
network G′ at time t.
B. Can Recent IM Efforts on Dynamic Networks Address the
Limitations?
Recently, several efforts have studied the IM problem in the
context of dynamic or temporal social networks [15], [16],
[17], [18], [19]. At ﬁrst glance, it may seem that the aforemen-
tioned problem of classical IM can be addressed by deploying
these techniques as they consider evolutionary nature of the
underlying network. Unfortunately, this is not the case as these
techniques either assume that the topology of the network is
completely known at a speciﬁc time point or are oblivious
to the impact of inﬂuence propagation time on the network
state. Broadly, these techniques repeatedly run classical IM
algorithms (or their incremental versions) at different time
points in order to ﬁnd up-to-date seed sets. However, this
strategy cannot address the aforementioned limitation of the
classical IM problem regardless of the way time points are
separated or the choice of IM algorithm. For instance, suppose
Gi at time ti evolves to Gj at time tj where tj > ti. Intuitively,
one may select Si at time ti in order to maximize the inﬂuence
at a different temporal state. However, Si can only assure
that the inﬂuence is maximized in Gi. As remarked earlier,


## Page 3


as inﬂuence propagates from Si, the network evolves as well.
Consequently, whenever inﬂuence of Si reaches the largest
scope, the network may have evolved from Gi to Gj. Hence,
repeatedly selecting seeds using a conventional IM algorithm
or its variant cannot lead to a superior quality seed set that
maximizes inﬂuence at a future time point.
As an example, consider the MaxG algorithm in [15], which
ignores the impact of inﬂuence propagation time. In other
words, it assumes that the topology of the whole network
can be easily observed at any timestamp, which is consis-
tent with the assumption made by classical IM as discussed
earlier. It is worth noting that if the time consumed by the
inﬂuence propagation process is not ignored, the probability
of update operation has to be decayed even if the marginal gain
increases. This is because the later a new node is interchanged
into S, the lesser is the time available for it to propagate to the
inﬂuence scope as expected. In fact, it has been argued in [20],
selecting same seeds at different timepoints may result in
different inﬂuence spread in a dynamic network. The approach
in [21] ﬁrstly separates a time period into several equal-length
intervals (of length h) based on the entire evolution period of
the network. Then, an algorithm is presented to select seeds S
at t in order to maximize the inﬂuence at t+h. Unfortunately, it
demands the future network state as input in order to compute
h. For instance, in order to select S in G at time t in Fig. 1(a),
it requires G′′ at time t′′ (Fig. 1(c)) as input. Obviously, it is
unrealistic to assume that G′′ is completely known at t.
C. Contributions
This paper makes four contributions. First, we theoreti-
cally prove that if the aforementioned assumption related to
evolutionary nature of a social network and the impact of
inﬂuence propagation time on seed selection is jettisoned by
the classical IM problem, then the approximation guarantee for
greedy algorithms that the inﬂuence spread is within (1−1/e)
of the optimal inﬂuence spread does not hold anymore. Note
that a large number of subsequent work [3], [8], [22] have used
this guarantee as the building block to design new algorithms
and derive new results.
Second, we revisit the classical IM problem and redeﬁne
it as PROTEUS-IM2 (Propagation Time-conscious Inﬂuence
Maximization) problem by jettisoning the aforementioned
assumption made by the former. Intuitively, it is deﬁned as
follows. Given a network G0 = (V0, E0) at time t0 that may
evolve to Gr = (Vr, Er) at target time tr, the goal of the
PROTEUS-IM problem is to select seeds S ⊆V0 at time t0
such that information spread from S can reach the largest
scope in Gr instead of G03.
Observe that the PROTEUS-IM problem differs from the
classical IM in the following ways. Firstly, we assume that the
2 The name honors Proteus, a sea god in Greek mythology, noted for his
ability to assume different forms and to prophesy. The PROTEUS-IM problem
discovers seeds from a social network that assumes different form from the
current instance at the end of the inﬂuence propagation process.
3 We shall elaborate in Section III the justiﬁcation for choosing seed set
from G0 and not solely from Gr.
underlying network evolves during the inﬂuence propagation
time tr and the complete topology of the target network Gr
is unknown at time t0. Secondly, the seeds are selected in a
network (G0) whose topology is not identical to the one in
which inﬂuence ﬁnally propagates to the largest scope (Gr).
In comparison, in the classical IM problem these two net-
work topologies are assumed identical. Thirdly, the inﬂuence
propagation path in our problem may consists of nodes and
edges that are currently absent in G0. In comparison, the
inﬂuence propagation path in classical IM, although randomly
distributed, strictly sampled from the edges in the current
network. We also prove that the PROTEUS-IM problem is NP-
hard and the expected inﬂuence is submodular.
Third, we propose a greedy algorithm called PROTEUS-
GENIE to address the PROTEUS-IM problem. Speciﬁcally, it
selects k nodes at time t0 whose expected inﬂuence at time tr
is maximal. A distinguishing feature of the algorithm is that it
takes into account evolution of the underlying network during
inﬂuence propagation process. Note that this is a challenging
problem as we cannot make unrealistic assumption that the
topology of the network at tr is completely known apriori.
To tackle this challenge, we resort to a popular network
evolution model called the Forest Fire Model (FFM) [23] to
predict the topology of the network at time tr4. To the best
of our knowledge, FFM has never been utilized in the context
of IM. Speciﬁcally, PROTEUS-GENIE iteratively selects nodes
with largest marginal gain in expected inﬂuence, taking into
account the evolution of the network predicted by FFM. The
proposed greedy algorithm can be time consuming for large
networks as in each iteration we need to simulate network
evolution and then select the next optimal seed node. Hence,
we propose a Reverse Reachable (RR) set-based algorithm
called PROTEUS-SEER which signiﬁcantly reduces the running
time while preserving similar inﬂuence spread quality. It ﬁrst
selects an instance number θ by utilizing a recent classical IM
technique [24] and then iteratively predict θ instances of the
target network, G′
1, . . . , G′
θ. We select candidate seeds from
each G′
i and aggregate them to ﬁnally select the top-k seeds.
Fourth, we investigate the performance of PROTEUS-GENIE
and PROTEUS-SEER on real-world social networks. Our ex-
perimental study reveals that, as predicted by theory, algo-
rithms designed for the PROTEUS-IM problem consistently
outperform state-of-the-art classical IM techniques in terms
of inﬂuence spread quality for all datasets, even when the
underlying network has changed slightly during inﬂuence
propagation (i.e., tr may be small). Interestingly, our results
emphasize that it is not necessary to possess a complete and
accurate knowledge of the topology of Gr to achieve such
superior performance. Note that this is important as assuming
such complete knowledge renders the IM problem unrealistic.
Additionally, PROTEUS-SEER signiﬁcantly reduces the running
time while preserving similar result quality.
4 As our approach is loosely-coupled with the network evolution model,
other models can also be adopted in this regard.


## Page 4


TABLE I: Key notations used in this paper.
Symbol
Deﬁnition
Gi = (Vi, Ei)
A social network at time ti
k
The number of seeds
S
Seeds set
p
Independent cascade probability
σ(·)
The expected inﬂuence function in static network
σXt(·)
The number of inﬂuenced node through edges Xt
σ(·, t)
The expected inﬂuence of dynamic network at time t
α
Forward burning probability
γ
Backward burning ratio
R
Number of rounds of simulation in computing expected
inﬂuence
I
Number of rounds for simulating the evolution
θ
Number of predicted instances in PROTEUS-SEER
R(v, G)
The set of nodes in G that can reach v
D. Paper Organization
The rest of this paper is organized as follows. We review
classical IM techniques in Section II. We formally deﬁne
the PROTEUS-IM problem in Section III. Sections IV and V
present the PROTEUS-GENIE and PROTEUS-SEER algorithms
to address this problem. We present the experimental results in
Section VI. Finally, we conclude this paper in the last section.
II. CLASSICAL INFLUENCE MAXIMIZATION PROBLEM
In this section, we review related work in classical inﬂuence
maximization (IM) problem for both static and dynamic net-
works. Table I describes the key notations used in this paper.
A. IM in Static Networks
Kempe et al. [1] are the ﬁrst to consider choosing the
seeds for IM problem as a discrete optimization problem.
In their seminal paper, they deﬁned the classical inﬂuence
maximization problem as follows.
Deﬁnition 1: [Classical
Inﬂuence
Maximization
Problem] Let G
=
(V, E) be a network and σ(·) be
the expected inﬂuence of a set of nodes under a given
cascade model, measured by the number of nodes that
are eventually inﬂuenced. Then given a budget k, the
inﬂuence maximization (IM) problem aims to select a seed
set S ⊂V (|S| = k) such that the expected inﬂuence spread
σ(S) is maximized, which can be formally described as
S = arg max
A⊆V,|A|=k
σ(A).
Kempe et al. [1] proposed a general greedy algorithm that
returns near optimal results (i.e., within 1−1/e). Since then a
large body of IM techniques [1], [3], [8], [24], [25] are reported
in the literature to improve efﬁciency, scalability, and inﬂuence
spread quality. As highlighted in Section I, the classical IM
algorithms assume that the topology of the underlying network
is completely known and it does not evolve during inﬂuence
propagation. Hence, they suffer from the limitations discussed
earlier leading to relatively poorer quality of inﬂuence spread
(detailed in Section VI).
Observation 1: The seed set S ⊆V in classical IM problem
(Deﬁnition 1) may not exhibit the largest expected inﬂuence
when the underlying network evolves during inﬂuence prop-
agation. In other words, ∃S′ ⊆V , where |S′| = |S| = k,
S′ ̸= S, such that σ(S) < σ(S′).
Theorem 1:
The approximation guarantee that the inﬂu-
ence spread is within (1−1/e) of the optimal inﬂuence spread
for greedy hill-climbing-based classical IM algorithms does
not hold when the underlying network evolves during inﬂuence
propagation.
Proof: We can easily design a network evolution scenario
justifying that 1 −1/e guarantee does not hold eventually.
Without loss of generality, suppose G0 consists of n nodes
and only one edge. Let G0 evolve in the following way, at
each step, it replicate a copy of G0. For instance, G1 consists
of G0 and G′
0, which are isomorphic but disconnected with
each other; G2 consists of G1 and G′
0, and etc. Thus, Gr
(r > k) will consist of r + 1 disconnected copies of G0.
Suppose we are maximizing the inﬂuence spread using greedy
hill-climbing-based classical IM algorithms in G0. According
to the quality guarantee, σ(Sk, r) ≥(1 −1/e)σ(O0
k, 0), and
obviously σ(O0
k, 0) = k + 1. Therefore (1 −1/e)(k + 1) ≤
σ(Sk, r) ≤k+1. However, we can easily ﬁnd that σ(Or
k, r) =
2k, which can be achieved by selecting 1 seed from each
of k disconnected copies of G0 in Gr. Obviously, ∀k ≥4,
k + 1 < (1 −1/e)2k, that is, σ(Sk, r) < (1 −1/e)σ(Or
k, r).
Remark. Kempe et al. showed in [1] that a non-progressive
(i.e., nodes can switch from inactive to active state and vice
versa) IM problem can be reduced to a progressive (i.e.,
nodes can only switch from inactive to active state but not
vice versa) case in a different graph. Unfortunately, when the
underlying network evolves during inﬂuence propagation, the
IM problem cannot be transformed to a non-progressive case
(and subsequently to progressive case) due to the following
reasons. They designed a new concept, namely layered graph,
which is deﬁned as follows. Given a graph G = (V, E) and
time limit τ, a layered graph Gτ on τ˙|V | contains a copy
vt for each node v in G and each time step t ≤τ. Firstly,
in a non-progressive case, no matter how many layers in the
layered graph Gτ, the topology of the network G = (V, E) in
each layer is completely known. However, in reality a social
network does not satisfy this property. That is, if we model
the evolving network into a layered graph, then the topology
of the network in each layer is unknown and these networks in
different layers are different. Secondly, the inﬂuence in non-
progressive case is measured by the sum over the number
of time steps that all nodes v ∈V are active. However, in
the presence of evolution it cannot be measured in this way.
On one hand, V is not ﬁxed in our problem setting; on the
other hand, the inﬂuence should be measured as the number of
active nodes at a target time tr (i.e., the end of propagation in
progressive IM) instead of summing over the number of steps
the nodes are active.
B. IM in Dynamic Networks
Recently, there have been increasing efforts to address the
IM problem in dynamic networks. Zhuang et al. [15] proposed


## Page 5


an algorithm called MaxG to select seed nodes St at a
speciﬁc time step t. It utilizes a heuristic probing strategy
such that at a target time step, it only needs to probe a limited
number of nodes, whose change in the local connections
can best uncover the actual inﬂuence propagation process.
As remarked in Section I-B, it assumes the topology of the
whole network can be easily observed at any timepoint. The
same limitation also exists in [16], which focuses on track-
ing inﬂuential nodes. More recently, [17] proposed an index
model using RR set introduced in [26] to answer inﬂuence
maximization query at any temporal state during network
evolution. Similar to [15], this work also suffers from two
key drawbacks. Firstly, it assumes that every atomic evolution
step (e.g., single node/edge addition) can be fully observed
at any timepoint, which is unrealistic in practice. Secondly, it
ignores the inﬂuence propagation time and fails to anticipate
the network state during inﬂuence propagation. Consequently,
any answer of [17] (i.e., a set of seeds) towards an inﬂuence
maximization query q at time t may not necessarily generate
the expected inﬂuence cascade as the network, in which
inﬂuence eventually propagates, is typically not the same with
the one at t, based on which it answers q.
Aggarwal et al. [21] studied the problem of selecting seed
nodes S at time t, such that a piece of information propagated
from these nodes will spread to the largest scope (i.e., number
of nodes) at time t + h, taking into account that the network
may evolve during the period from t to t + h. However, as
discussed in Section I-B, it assumes that the complete topology
of the ﬁnal network where inﬂuence eventually propagates to
the largest scope is known and seeds are selected from this
“known” network.
III. PROPAGATION TIME-CONSCIOUS INFLUENCE
MAXIMIZATION
In this section, we revisit this decade-old IM problem and
redeﬁne it to address the aforementioned limitation. We begin
by introducing some terminology that we shall be using in this
paper. Then, we formally redeﬁne the classical IM problem as
propagation time-conscious IM problem.
A. Terminology
We model a social network as directed graph G = (V, E),
where nodes in V represent individuals in the network and
edges in E represent relationships between them. The order
of G is |V | and its size is |E|. Recall that traditional IM
assumes inﬂuence propagates between nodes according to a
speciﬁc cascade model and selects k nodes in V as seeds to
spread a piece of information such that the information will be
propagated to the maximal number of other nodes. However,
such inﬂuence propagation can take tr time in reality (which
can be several weeks). During this time, the social network
may evolve from G0 = (V0, E0) at time t0 to Gr = (Vr, Er)
at time tr. We refer to G0 as current network and Gr as
target network. Correspondingly, t0 and tr are referred to as
current time and target time, respectively. For the sake of
generality, we assume that tr is given by the user as it is
application and network dependent. We assume |Vr| > |V0|
and |Er| > |E0| as most real-world social networks grow
over time. Furthermore, Vr ∩V0 ̸= ∅and Er ∩E0 ̸= ∅.
We denote the expected inﬂuence at time t (i.e., the number
of inﬂuenced nodes at t) for seeds S under a given cascade
model as σ(S, t). For ease of exposition, in the sequel, we
assume the independent cascade (IC) model, where inﬂuence
propagates according to an independent probability pij along
any edge −−→
vivj, for inﬂuence propagation as it is one of the
most popular model in the literature. However, our proposed
problem is also applicable to other types of cascade models.
B. Redeﬁning IM Problem
The classical inﬂuence maximization problem (Deﬁnition 1)
ignores the inﬂuence propagation time which can be signiﬁcant
in reality, during which the underlying social network may
evolve. Hence, we formally redeﬁne this classical inﬂuence
maximization problem as follows.
Deﬁnition 2: [Propagation
Time-conscious
Inﬂuence
Maximization Problem] Let G0 = (V0, E0) be the current
network at time t0 and k be the budget. Let tr > t0 be
the inﬂuence propagation time during when G0 evolves to
Gr = (Vr, Er) where Vr ∩V0 ̸= ∅and Er ∩E0 ̸= ∅.
Then, the goal of Propagation Time-conscious Inﬂuence
Maximization (PROTEUS-IM) Problem is to select a set of
seed nodes S ⊆V0 (|S| = k) at t0 such that the expected
inﬂuence spread σ(S, tr) is maximized at tr assuming that
the complete topology of Gr is unknown at t0. That is,
S = arg max
A⊆V0,|A|=k
σ(A, tr).
Observe that according to the above deﬁnition, seeds are
selected from current instance of the network G0 instead
of future instances of the network i.e., G1, . . . , Gr. This is
because it is difﬁcult to know at t0 which users may potentially
join or leave a social network in the future (before tr), how
will they be connected to other users, and whether they will be
part of the seeds. In fact, as remarked earlier, it is unrealistic to
assume accurate and complete topological knowledge of future
instances of the social network (i.e., Gr) at time t0. Hence,
given that inﬂuence propagation may take tr time, it is more
realistic to choose a seed set S ⊆V0 (i.e., users who currently
exist in the social network) in order to maximize the expected
inﬂuence spread in the target network Gr. Also, observe that
in the classical IM problem, Gr = G0 as the topology of the
network is assumed to be static since tr is negligible.
LEMMA 1: The expected inﬂuence function at an arbitrary
time t for node set S under the IC model, namely σ(·, t),
deﬁned in Deﬁnition 2 is sub-modular.
Proof: Let fXt(v) be the set of nodes that can be
reached from v on a path comprising of the live edges Xt
at time t and σXt(A) be the number of nodes that can be
reached from A = {v0, . . . , vk} through Xt. In other words,
σXt(A) =
 S
v∈A fXt(v)
. Given two node sets S ⊆T ,
consider the following expression: σXt(S S{v}) −σXt(S),
which is the number of elements in fXt(v) that are not
already in S
u∈S fXt(u). It is at least as large as the number


## Page 6


of elements in fXt(v) that are not in S
u∈T fXt(u). Hence,
σXt(S S{v}) −σXt(S) ≥σXt(T S{v}) −σXt(T ), which
is submodular. Moreover, the expected inﬂuence of S at
t for all possible Xt, i.e., σ(S, t), can be computed as
σ(S, t) = P
Xt Prob[Xt]·σXt(S). According to the equation,
σ(S, t) can be viewed as a non-negative linear combination of
submodular functions, which is also submodular.
LEMMA 2: The PROTEUS-IM problem deﬁned in Deﬁni-
tion 2 under the IC model is NP-hard.
Proof: Consider the traditional IM problem in Deﬁnition 1
which has been proved to be NP-hard [1]. We show that this
can be viewed as a special case of the NEW-IM problem.
Given a network G0 = (V0, E0) at t0, suppose we are
solving NEW-IM over G0 at t0. If G0 remains static for a
sufﬁciently long period until the inﬂuence propagation ends
at time tr (i.e., the inﬂuence reaches the largest scope), in
this case G0 is the same with Gr at tr. Therefore, the NEW-
IM in G0 is equivalent to IM in G0. That is, the problem
of maximizing σ(S, tr) in Gr degenerates to the problem of
maximizing σ(S) in G0. Therefore, the NEW-IM is at least as
hard as IM, which is NP-hard.
Since the PROTEUS-IM problem is NP-hard, in the sequel
we present two approximate solutions. It is worth emphasizing
that given the rich body of work on classical IM techniques,
our design principle behind these solutions is not to jettison all
these efforts but to leverage on the beneﬁts of these techniques
wherever possible, while bringing in novel ideas to address the
aforementioned limitations of classical IM. Hence, our ﬁrst
solution is a greedy hill-climbing approach called PROTEUS-
GENIE. Our second solution, called PROTEUS-SEER, exploits
Reverse Reachable (RR) set and is signiﬁcantly more efﬁcient
than PROTEUS-GENIE while preserving good result quality.
IV. A GREEDY SOLUTION
In this section, we present a novel greedy algorithm called
PROTEUS-GENIE (Propagation Time-conscious GrEedy se-
lectioN of Inﬂuential sEeds) that addresses the PROTEUS-
IM problem. Observe that designing such algorithm is chal-
lenging. On one hand, it is unrealistic to assume complete
knowledge of the topology of the target network Gr at time
t0. On the other hand, without knowing the topology of Gr
it is very difﬁcult to compute the expected spread in it using
existing cascade models (e.g., IC model).
We tackle this challenge by predicting the expected topol-
ogy of Gr from G0 by exploiting a popular network evolution
model called the Forest Fire Model [23], [27]. Consequently,
we utilize this predicted topology of Gr to determine the
expected spread in it using an existing cascade model. We
begin by brieﬂy introducing this model. Interestingly, as we
shall see in Section VI, by leveraging the predicted topology of
Gr, our proposed algorithms can consistently produce superior
quality seeds compared to classical IM techniques. That is, we
do not need to know the actual topology of Gr at time tr to
produce superior quality seeds!
A. Forest Fire Model (FFM)
Majority of social networks are evolutionary in nature
and exhibit series of properties and phenomenons, including
shrinking diameter, densiﬁcation power law, etc [23]. Several
network evolution models [14], [23], [27], [28] have been
proposed in the literature to simulate the evolution of real-
world online social networks. Among these models, we chose
the Forest Fire Model (FFM) [23], as it outperforms other
models [27]. Formally, this model is deﬁned as follows.
Deﬁnition 3: [Forest Fire Model] Let Gt be a network at
time t, G1 consist of only the ﬁrst node. Given an incoming
node v at time t, the network Gt−1 at time t−1 can be updated
to Gt according to the following rules.
1) Uniformly select an ambassador node w from Gt−1 and
establish a directed edge from v to w, −→
vw.
2) Sample two numbers x and y, from a pair of binomial
distributions whose means are α/(1 −α) and γα/(1 −
γα), respectively. Afterwards, v uniformly selects x in-
links and y out-links incident to w, respectively. Let
w1, w2, . . . , wx+y be the other ends of the selected links.
In particular, α is a preset forward burning probability,
γ is a preset backward burning ratio such that γα is
backward burning probability.
3) Establish directed edges from v to w1, w2, . . . , wx,
respectively. Similarly, establish directed edges from
wx+1, wx+2, . . . , wx+y to v, respectively. Then, we ap-
ply step (2) recursively for each of w1, w2, . . . , wx until
there is no new link to be added. As this process
continues, nodes can only be visited once such that there
is no cyclic sub-structure.
It has been shown in [23] that the network generated by FFM
satisﬁes majority of real-world network properties, including
not only static ones (e.g., Heavy-tailed in-degrees and out-
degrees [27]) but also dynamic ones (e.g., Densiﬁcation Power
Law and Shrinking Diameter [23]). It has also been demon-
strated in [27] that evolutions of many real-world networks can
be well simulated and predicted using this model. Therefore,
we utilize FFM to predict the evolution of a network at target
time tr. Speciﬁcally, our PROTEUS-GENIE algorithm integrates
the FFM with node selection during inﬂuence maximization to
facilitate discovery of superior quality seeds. We now elaborate
on this algorithm in detail.
B. The PROTEUS-GENIE Algorithm
The goal of the PROTEUS-GENIE algorithm is to greedily
select the nodes with the maximal marginal expected inﬂuence
taking into account the evolution of the underlying network
from time t0 to tr by predicting its topology using FFM.
Intuitively, seeds selection in PROTEUS-GENIE is as follows.
Firstly, given the current network G0 at time t0, it evaluates
the marginal expected inﬂuence of all nodes v ∈V0 that
are predicted to be in Gr at time tr, namely σ(v, tr). Note
that the topological structure of Gr at target time tr > t0
is generated using FFM based on G0. The forward burning
probability and backward burning ratio are selected by ﬁtting


## Page 7


G0
Gr
Gr
(1)
Gr
(2)
Gr
(3)
FF
S1={v1}
S2={v3}
S3={v1}
S={v1}
v1
v2
v3
v4
v5
f1(v3)=2, f1(v2)=1
f2(v1)=3, f2(v2)=2,
f2(v4)=1
f3(v1)=2, f3(v2)=1, 
f3(v3)=2
...
...
f(v1)=5, 
f(v2)=4, 
f(v3)=4
f(v1)=3,
f(v2)=3,
f(v3)=6, 
f(v4)=2
f(v1)=4, 
f(v3)=3,
f(v4)=1
Fig. 2: Greedy seeds selection by the PROTEUS-GENIE algorithm.
the model using the network evolution historical logs before
t0. Secondly, it selects the node with the largest expected
inﬂuence as the ﬁrst node and removes it from Gr. Thirdly, it
performs the previous two steps iteratively for k rounds such
that it selects k seeds as S1. Observe that in previous steps,
we generate one target network Gr using FFM, which results
in a deterministic network at time tr. However, the network
evolution using FFM during t0 to tr is a random process
which cannot be accurately described using a single-round
simulation. Therefore, the previous three steps are executed
for I rounds independently, resulting in I different instances
of Gr, denoted by G(1)
r , G(2)
r , . . . , G(I)
r . Consequently, the
seeds sets S1, . . . , SI are generated after I rounds. Finally,
it aggregates the ranks of these seeds and selects the top-k
nodes with the highest overall ranks as the ﬁnal seed set S.
We now formally describe the algorithm.
The formal procedure is outlined in Algorithm 1. Firstly,
it simulates the evolution of the network G0 to Gr using
FFM (Deﬁnition 3) and then initialize a seed set instance
Si as empty (Lines 3-4). Then, it iteratively selects k seed
nodes into Si (Lines 5-12). For the selection of each seed
node, we generate graph G′
r by removing each edge in Gr
independently with probability 1 −p, resulting in a spanning
graph G′
r = (V ′
r, E′
r). In this manner, E′
r can be viewed as
live edges set Xr at time tr, from which we can compute
the marginal inﬂuence for each v ∈V0. This process repeats
for R times and the marginal inﬂuences of each node are
aggregated (Lines 6-9). Afterwards, the algorithm selects the
nodes with the maximal accumulated marginal inﬂuence so
far (denoted as v∗) and inserts it into Si and removes it from
V ′
0. Meanwhile, it also records the rank of each seed in Si as
Si(·). The above steps are iteratively performed for I times,
until each of S1, . . . , SI is ﬁlled with k seeds (Lines 2-12).
So far, we have I instances of seed node set, each of which
consists of k nodes as well as their ranks Si(·). Hence, for
each of the nodes v that appears in S1, . . . , SI at least once,
the algorithm aggregates its ranks (Lines 13-15). Finally, it
selects the top-k nodes as the ﬁnal seed set S (Lines 16-18).
Example 2: Consider Fig. 2. Suppose k = 1, R = 3, and
I = 3. Let the current network at time t0 is G0 as shown
Algorithm 1: The PROTEUS-GENIE Algorithm.
Input: Current network G0 = (V0, E0), k, p, I, R, target
time tr, forwards burning probability α, backward
burning ratio γ.
Output: Seed set S of nodes, |S| = k
1 begin
2
foreach i = 1 to I do
3
G(i)
r
= (V (i)
r
, E(i)
r ) ←FF(G0, α, γ, tr);
4
Si ←∅, V ′
0 ←V0;
5
foreach j = 1 to k do
6
foreach iter = 1 to R do
7
generate G(i)′
r
= (V (i)′
r
, E(i)′
r
) by
removing each edge −→
uv from
G(i)
r
= (V (i)
r
, E(i)
r ) with probability
1 −p;
8
foreach v ∈V0 do
9
f(v)+ = σE(i)′
r
(Si ∪{v})−σE(i)′
r
(Si);
10
v∗= arg max
v∈V0
f(v);
11
Si = Si ∪{v∗}, Si(v∗) = j;
12
V ′
0 = V ′
0 \ {v∗};
13
S∗=
IS
i=1
Si;
14
foreach v ∈S∗do
15
S∗(v) =
IP
i=1
Si(v);
16
rank v ∈S∗according to S∗(v) in descending order;
17
return S ←top-k items in S∗;
in the left-hand side of the ﬁgure. First, the PROTEUS-GENIE
algorithm utilizes FFM to randomly predict an instance of the
target network G(1)
r
at time tr > t0. Then it randomly removes
each edge with probability 1 −p for R times from G(1)
r . This
results in three instances of inﬂuence. Accordingly, it ﬁnds a
ranked seed set S1 consisting of the top-1 node with the largest
expected inﬂuence scope over these instances. Afterwards,


## Page 8


these steps are repeated twice (i.e., I −1) by randomly
predicting two other instances of the target network, resulting
in G(2)
r
and G(3)
r . Similarly, the algorithm selects another two
seed sets, S2 and S3. Finally, it assembles S1, . . . , S3 into a
bag of nodes S∗= [v1, v3, v1], from which the top-1 node v1
with the maximal frequency is returned.
Theorem 2: The time complexity of the PROTEUS-GENIE
algorithm (Algorithm 1) is O(I(kR|Er|+r|Er|(|V0|+r))+I).
Proof:
The
time
complexity
of
FF
procedure
is
O(r|Er|(|V0| + r)) [23]. In Algorithm 1, in each iteration
for i = 1 to I, the time complexity is O(kR|Er|) [3]
plus the complexity of FF procedure. Thus, ﬁlling all Si
for i = 1, . . . , I requires O(kR|Er| + r|Er|(|V0| + r)).
Therefore, the overall time complexity of Algorithm 1 is
O(I(kR|Er| + r|Er|(|V0| + r)) + I).
Theorem 3: Let Gr
0 be the subgraph that joined G0 during
t0 to tr and ˆGr
0 be the subgraph generated by FFM from t0
to tr. If ˆGr
0 is identical to Gr
0 with probability η, then each
Si corresponding to ˆGr
0 generated by the PROTEUS-GENIE
algorithm (Algorithm 1) is guaranteed to achieve (1 −1/e)-
approximation for PROTEUS-IM with probability η.
Proof: Due to the newly joined edges and nodes, for
each v ∈V0, the expected inﬂuence of it at Gr, namely
σ(v, r) can be separated as two parts, one from original graph
G0 (i.e., σ(v, 0)), the other from the marginal increase in
the expected inﬂuence caused by Gr
0, denoted by f(v, 0, r).
Let ˆf(v, 0, r) be the latter part, then the expected inﬂuence
of v in predicted graph Gr can be computed as: ˆσ(v, r) =
σ(v, 0)+ ˆf(v, 0, r). As ˆGr
0 is identical with Gr
0 with probability
η, then ˆf(v, 0, r) = f(v, 0, r) with probability η. Therefore,
ˆσ(v, r) = σ(v, r) with probability η.
Moreover, as PROTEUS-IM degenerates to classical hill-
climb algorithm if graph Gr is static, which is guaranteed to
be within (1−1/e) of the optimal, then the seeds S selected by
PROTEUS-IM in Gr is within (1−1/e) of the optimal. Putting
it together, the seeds selected by PROTEUS-IM can achieve
(1 −1/e)-approximation with probability η.
Remark. Typically network evolution may be slower than
inﬂuence propagation. However, our framework does not de-
mand any correlation between the time steps of the FFM
and the inﬂuence propagation time. As long as network is
evolving and inﬂuence propagation takes time, our proposed
model and algorithm ﬁt well. In fact, when FFM is extremely
slow (i.e., network hardly evolves) and inﬂuence propagation
is extremely fast (i.e., tr is negligible), the PROTEUS-IM
problem is close to the classical IM problem. Particularly,
in the unrealistic case when FFM is very slow (e.g., each
time only one node is added and we have enough time to
grasp the topology of network at any temporal state) and tr
is negligible, MaxG [15] works well. In contrast, whenever
inﬂuence propagation takes time, our solution ﬁts well.
Furthermore, since in our framework we select seeds from
G0 for maximizing inﬂuence at Gr (as discussed in Sec-
tion III-B), we do not need to care about how G0 evolves to
Gr. This only matters for techniques (e.g., MaxG [15]) where
seeds are iteratively selected during the evolution.
V. A REVERSE REACHABLE SET-BASED SOLUTION
Observe that the time complexity of PROTEUS-GENIE is
highly inﬂuenced by |Er| and |V0| (Theorem 2). These values
are large for real-world networks containing millions of nodes
and hence the efﬁciency of the greedy algorithm can be
adversely affected when dealing with such networks. In this
section, we address this issue by proposing an algorithm
called PROTEUS-SEER (Propagation Time-conscious SEed
SElection using RR set), which leverages the notion of Reverse
Reachable (RR) Set [26] in addition to FFM for seed selection.
For the sake of completeness, we ﬁrst brieﬂy introduce the
concept of RR set before discussing our algorithm to address
the PROTEUS-IM problem.
A. Reverse Reachable Set
Let v be a node in G and g be a graph obtained by removing
each edge e in G with probability 1−p. The reverse reachable
(RR) set [26] for v in g, denoted as R(v, g), is the set of nodes
in g that can reach v. That is, for each node u in the RR set,
there is a directed path from u to v in g. For example, consider
Fig. 1(a). The RR set for node v5 in G contains all nodes in
G that can reach v5. That is, R(v5, G) = {v3, v1, v4}.
Let G be the distribution of g induced by the randomness
in edge removals from G. A random RR set [26] is an RR set
generated on an instance of g randomly sampled from G for
a node selected uniformly at random from g.
Note that the notion of RR set is currently the most efﬁcient
and promising way to answer inﬂuence maximization problem
with guaranteed result quality, and has been recently deployed
in [17], [26] to generate “near-optimal” solution for the IM
problem. However, these techniques either assume the net-
work is static or ignore the inﬂuence propagation time. More
importantly, they cannot be trivially extended to handle the
PROTEUS-IM problem.
B. The PROTEUS-SEER Algorithm
The key idea of the algorithm is to compute the RR set
by considering the evolution of the network due to random
prediction using FFM. Since the target network is randomly
predicted several times, we utilize a bag of nodes to assemble
all instances of the RR sets computed from different random
instances of the predicted network. Speciﬁcally, our algorithm
comprises of the following key steps.
1) First, we use the FFM to simulate the evolution of
G0, from which we get Gr. This process is iteratively
repeated for θ times, such that we can get θ different in-
stances of Gr, denoted by Gr = {G(1)
r , G(2)
r , . . . , G(θ)
r }.
In particular, θ is computed as in [24].
2) Second, for each instance G(i)
r , uniformly sample a
node from Vr as vi, and generate a
RR set for
it denoted as R(vi, G(i)
r ). Consequently, we have
θ such sets, each corresponds to a sampled node.
In
the
sequel,
we
denote
these
sets
as
R
=
{R(v1, G(1)
r ), R(v2, G(2)
r ), . . . , R(vθ, G(θ)
r )}
3) Finally, we greedily select from all RR sets in R the
node w which appears in the most number of RR sets


## Page 9


Algorithm 2: The PROTEUS-SEER Algorithm.
Input: Current network G0 = (V0, E0), seeds number k,
inﬂuence probability p, θ, target time tr, forward
burning probability α, backward burning ratio γ.
Output: Seed set S of nodes, |S| = k.
1 begin
2
S ←∅;
3
foreach i in 1 to θ do
4
G(i)
r
= (V (i)
r
, E(i)
r ) ←FF(G0, α, r, tr) ;
5
uniformly sample vi ∈V (i)
r
;
6
initialize RR set for vi as: R(vi, G(i)
r ) = {vi};
7
foreach v′ ∈R(vi, G(i)
r ) do
8
foreach −→
wv′ ∈E(i)
r
do
9
with probability p, let
R(vi, G(i)
r ) = R(vi, G(i)
r ) ∪{w};
10
R = {R(v1, G(1)
r ), R(v2, G(2)
r ), . . . , R(vθ, G(θ)
r )};
11
RS =
S
Ri∈R
Ri;
12
foreach i = 1 to k do
13
foreach w ∈RS do
14
ct(w, R) =
P
Rj∈R
ct(w, Rj);
15
u = arg max
w∈RS
ct(w, R);
16
S = S ∪{u};
17
foreach Rj ∈R that contains u do
18
remove Rj from R;
19
return S;
Gr
Gr
(1)
Gr
(2)
Gr
(3)
S={v1}
R(v2,G(1)
r)={v1,v3}
R(v4,G(2)
r)={v1,v2}
R(v6
(3),G(3)
r)={v1}
V6
(1)
V7
(1)
V6
(2)
V7
(2)
V6
(3)
V7
(3)
Fig. 3: RR set-based seed selection.
and then remove these sets from R. We iteratively select
k such nodes and then output them as ﬁnal seeds set S.
Algorithm 2 outlines the formal procedure. Similar to the
PROTEUS-GENIE algorithm, it simulates the evolution of G0
based on FFM to generate an instance of target network G(i)
r
=
(V (i)
r
, E(i)
r ) (Line 4). Based on G(i)
r , it uniformly samples a
node vi ∈V (i)
r
and generates a random RR set of this node
with respect to G(i)
r , resulting in R(vi, G(i)
r ) (Lines 5-9). The
generation of each RR set is implemented as a randomized
breath-ﬁrst search on G(i)
r . Given a node vi, it ﬁrst creates an
TABLE II: Datasets.
Network
#nodes
#edges
Degree of Change (DoC)
Syn-G1
4,000
16,033
-
Syn-G2
4,500
17,309
Low
Syn-G3
5,000
18,512
Low
Ph-G1
32,354
264,963
-
Ph-G2
38,558
347,268
Medium
Pa-G1
1,061,606
1,365,903
-
Pa-G2
1,772,362
5,452,113
High
Pa-G3
2,436,431
11,437,592
High
Pa-G4
3,774,768
16,518,948
High
empty queue and then ﬂips a coin for each incoming edge e
of vi. It retrieves the node u with probability p from which e
starts and inserts it into the queue. Subsequently, the algorithm
iteratively extracts the node v at the top of the queue and
examines each incoming edge e of vi. If e starts from an
unvisited node u, it adds u into the queue with probability
p. This iterative process terminates when the queue becomes
empty. Finally, the algorithm collects all nodes visited during
this process (including vi) and use them to form R(vi, G(i)
r ).
The aforementioned steps are repeated (in parallel) for θ
times resulting in R = {R(v1, G(1)′
r
), . . . , R(vθ, G(θ)′
r
)} (Line
10). Let RS be the set of nodes that appear in any of these
R(vi, G(i)′
r
) (Line 11). For all the nodes in RS, the algorithm
greedily selects the one, say u, which appears in the most
number of RR sets in R (Lines 13-16), indicating that u can
reach the maximal number of nodes in v1, v2, . . . , vθ. Then
it removes from S the RR sets where u appears (Lines 17-
18). In particular, we denote ct(u, R(vi, G(i)′
r
)) = 1 if u ∈
R(vi, G(i)′
r
), and 0 otherwise. This seeds selection process is
iteratively performed for k rounds to identify the ﬁnal set of
seed nodes (Lines 12-18).
Theorem 4: The time complexity of the
PROTEUS-SEER
Algorithm is O((|Er| + |Vr|) log |Vr| + r|Er||Vr| + k|Vr|).
Proof: As reported in [24], the time complexity of com-
puting θ is O(ℓ(|Er|+|Vr|) log |Vr|) where ℓis a quality factor
which controls the results quality. The time complexity of evo-
lution simulation based on FFM is O(r|Er||Vr|). The process
of generating a RR set requires a BFS, which is O(|Er|+|Vr|).
As θ has been computed and ﬁxed, then generating all different
RR sets requires O(ℓ(|Er| + |Vr|) log |Vr| + r|Er||Vr|). The
time complexity of seeds selection is O(k|Vr|). Moreover, ℓ
is a predeﬁned quality parameter (always set as 1). Therefore,
the overall time complexity of Algorithm 2 is O((|Er| +
|Vr|) log |Vr| + r|Er||Vr| + k|Vr|).
VI. EXPERIMENTS
In this section, we investigate the performance of PROTEUS-
GENIE and PROTEUS-SEER. All algorithms considered for our
investigation are implemented in C++. We ran all experiments
on 3.2GHz Quad-Core Intel i7 machines with 16GB RAM,
running Windows 7. Note that there is no existing IM algori-
thm that addresses the PROTEUS-IM problem. Hence, we are
conﬁned to use state-of-the-art algorithms designed for the
classical IM problem as baseline methods.


## Page 10


Speciﬁcally, we investigate the following key issues. (1)
Is the seed set selected at target time tr differs signiﬁcantly
from those selected at current time t0? (2) Do our proposed
algorithms designed for the PROTEUS-IM problem consistently
produce superior quality seeds compared to state-of-the-art
algorithms designed for the classical IM problem? (3) Is
the running time of the PROTEUS-SEER algorithm reasonable
for large networks without signiﬁcantly compromising the
quality of inﬂuence spread? (4) What is the impact of various
parameters (e.g., tr, p, I) on the performance of the proposed
algorithms?
A. Experimental Setup
Datasets. Recall from Section I, inﬂuence propagation may
take several weeks to months and different networks may
evolve at varying rates during this period. Hence, we choose
real-world and synthetic datasets for our experiments to
represent these varying degree of change (DoC). Table II
summarizes these datasets. We use two real-world datasets
to generate different snapshots of a network representing
different degree of evolution. The ﬁrst one is high-energy
physics (Hep) paper citation networks collected through Arxiv5
during the period from January 1993 to April 2003 (124
months). It contains the historical logs for the appearance
timestamp of each paper as well as its citation links6. Since
each node is associated with a timestamp indicating when it
has joined the network, we can construct different instances of
the social network at different time points. The networks Ph-
G1 and Ph-G2 represent two temporal states of the citation
graph. The second dataset, Patents7, comprises of information
on almost 3 million U.S. patents granted between January 1963
and December 1999 and all citations made to these patents
between 1975 and 1999 (over 16 million). A speciﬁc temporal
state is extracted by selecting all citations (edges) that appear
before a speciﬁc timestamp. In particular, Pa-G1, Pa-G2, Pa-
G3 and Pa-G4 are selected as four representative temporal
states of this citation network. Note that we can extract any
temporal states (e.g., weekly, monthly, or yearly) from these
two networks. We also generate synthetic datasets using the
Forest Fire model8 (with default α = 0.35 and γ = 0.32)
in order to simulate snapshots of a network with small degree
of changes. Speciﬁcally, we generate three temporal snapshots
with slightly varying number of nodes and edges, denoted by
Syn-G1, Syn-G2, and Syn-G3.
The last column in Table II speciﬁes the degree of change
in the network w.r.t. the number of nodes and edges compared
to the preceding snapshot. In summary, the synthetic datasets
represent networks with small degree of evolution. The real-
world datasets, on the other hand, represent networks with
moderate (Hep) or high (Patents) degree of change. It is worth
emphasizing that different real-world networks may have
different degree of evolution during inﬂuence propagation.
5 http://arxiv.com
6 Downloaded from http://www.cs.cornell.edu/projects/kddcup/datasets.html.
7 Downloaded from http://www.nber.org/patents/.
8 According to steps described in http://snap.stanford.edu/snap-1.8/download.html.
 0
 5
 10
 15
 20
 25
 30
 35
 40
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
Actual rank of seeds at Gr (Syn-G3)
Selected rank of seeds in different Alg.
y=x (Greedy Gr)
PRO-GENIE
Greedy G0
(a) Syn-G1(G0),Syn-G3(Gr)
 0
 5
 10
 15
 20
 25
 30
 35
 40
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
Actual rank of seeds at Gr (Syn-G3)
Selected rank of seeds in different Alg.
y=x (Greedy Gr)
PRO-GENIE
Greedy G0
(b) Syn-G2(G0),Syn-G3(Gr)
Fig. 4: Ranks of seeds generated by different algorithms at
current and target times.
Hence, the seed set selection is impacted by the evolution
characteristics of the underlying network as well as tr.
Forest Fire Model (FFM) parameters. As discussed in Sec-
tion IV-B, the forward burning probability and backward
burning ratio are selected by ﬁtting the model using the
network evolution historical logs before t0. That is, we select
the states of networks before Ph-G1 and Pa-G1, and ﬁt FFM
accordingly. Speciﬁcally, we set α = 0.19, γ = 0.75 for Ph-
Gi; α = 0.15, γ = 0.76 for Pa-Gi.
Algorithms. We run the following IM algorithms under IC
model (with p = 0.01) for our experimental study:
• “Greedy”: MixGreedyIC algorithm [3] to address the
classical IM problem, as it exhibits the best seeds quality.
• “IRIE”: IRIE algorithm proposed in [25].
• “IMM”: IMM algorithm proposed in [24].
• “MaxG”: MaxG algorithm (with ǫ = 0.01) [15], which is
a dynamic IM algorithm that requires the full knowledge
of network evolution. Speciﬁcally, it assumes (a) the
complete evolution logs of the network is known; (b)
each time a new node arrives, there is sufﬁcient time to
update the seeds; and (c) the inﬂuence propagation time
is negligible.
• “PRO-GENIE”: The greedy algorithm in Section IV for
the PROTEUS-IM problem.
• “PRO-SEER”: The RR set-based method proposed in Sec-
tion V to address the PROTEUS-IM problem.
Unless speciﬁed otherwise, we set I = 500 and R = 5, 000
for PRO-GENIE, PRO-SEER, and Greedy, respectively.
B. Experimental Results
Seeds at current and target times. In Section I, we re-
marked that the seeds selected at current time t0 can be
signiﬁcantly different from the seeds selected at target time
tr > t0 due to the evolution of the underlying network.
Hence, we ﬁrst investigate whether this is indeed true. That is,
whether the seeds selected by a state-of-the-art IM algorithm
at t0 differ signiﬁcantly from those selected using the same
algorithm at time tr. To this end, we take a pair of current and
target networks (G0, Gr) at time points t0 and tr. We plot the
ranked seed nodes in Gr on the X-axis by running a classical
IM algorithm on it, which can be considered as the ground-
truth seed set. For clarity, we only consider the top-10 most
inﬂuential seed nodes (ranked by their expected inﬂuence) in
Gr that also exist in G0. Speciﬁcally, in our experiments these


## Page 11


0.89
 0.9
 0.91
 0.92
 0.93
 0.94
 0.95
 0.96
 0.97
 0.98
 0.99
 1
 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
σ(SN,r)/σ(SG,r)
tr-t0 (weeks)
PRO-SEER
IMM
IRIE
(a) G0 =Pa-G1 (k = 50)
 0.89
 0.9
 0.91
 0.92
 0.93
 0.94
 0.95
 0.96
 0.97
 0.98
 0.99
 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
σ(SN,r)/σ(SG,r)
tr-t0 (weeks)
PRO-SEER
IMM
IRIE
(b) G0 =Pa-G3 (k = 50)
 0.86
 0.88
 0.9
 0.92
 0.94
 0.96
 0.98
 1
100%
105%
110%
115%
120%
125%
σ(SN,r)/σ(SG,r)
|Vr|/|V0|×100
PRO-GENIE
PRO-SEER
IMM
IRIE
(c) G0 =Syn-G1 (k = 50)
 0.75
 0.8
 0.85
 0.9
 0.95
 1
100%
125%
150%
175%
200%
225%
σ(SN,r)/σ(SG,r)
|Vr|/|V0|×100
PRO-SEER
IMM
IRIE
(d) G0 =Pa-G1 (k = 50)
Fig. 5: Effect of degree of change. SG and SN are the seeds selected by Greedy on Gr and by different algorithms on G0, respectively.
seeds are selected by running Greedy on Gr. Then, we plot
on Y-axis the corresponding ranks of these seeds in G0 by
running the Greedy and PROTEUS-GENIE algorithms on G0.
Hence, in our plot if a seed v occupies the coordinate (a, b)
then it means that v is ranked a-th at time t0 (i.e., it exhibits the
a-th maximal marginal expected inﬂuence in G0) and ranked
b-th in Gr at time tr. Consequently, the larger the deviation
from y = x, the worse is the quality of selected seeds as the
seeds selected at t0 differ signiﬁcantly from the seeds needed
to maximize inﬂuence at tr (recall that our goal is to identify
k seeds at t0 that maximizes inﬂuence spread at tr).
Note that for networks with high degree of change, it is
intuitive to expect the seeds to be different in G0 and Gr.
Hence, we use the synthetic datasets for this experiment as it
exhibits low degree of change (can be considered as “worst”
case scenario). Fig. 4 plots the ranks of the top-10 seeds at
times t0 and tr for different pairs of networks. For instance,
in Fig. 4(a), G0 and Gr are network snapshots Syn-G1 and
Syn-G3, respectively. We have the following observations.
First, the ranks of seeds selected by Greedy using G0 deviates
signiﬁcantly from those on Gr for all datasets. That is, the
seeds selected by classical IM algorithms at times t0 and tr
differ signiﬁcantly. Consequently, seeds selected at t0 may not
be suitable for maximizing the inﬂuence at tr (further validated
below). Second, the ranks of the seeds selected by PROTEUS-
GENIE at time t0 are relatively closer to the top-10 seeds in
Gr for all datasets, emphasizing the need for reformulating
the classical IM problem as PROTEUS-IM problem.
Effect of degree of change and tr.
The
above
experi-
ments demonstrate that the seeds at current and target times
are different. We now study how the degree of change to
the network impact the inﬂuence and seed set. Observe that
degree of change is correlated with tr. Intuitively, the longer
is the inﬂuence propagation time (tr) the greater is the
degree of change to the network. First, we investigate the
inﬂuence spread quality by varying the duration between G0
and Gr (i.e., inﬂuence propagation time tr). Since inﬂuence
propagation may take weeks, we use the real-world networks
to report the effect of target time tr by selecting several states
of Gr at different target times such that tr−t0 ranges from 0 to
15 weeks. The results are shown in Figures 5(a) and (b), where
G0 are Pa-G1 and Pa-G3, respectively. Note that the procedure
to extract a Gr at a speciﬁc week is same as the one to extract
different snapshots in the Patents network (Section VI-A).
For instance, in Fig. 5(a) we ﬁx G0 as Pa-G1 and acquire
each temporal state of the network at 1, 2, . . ., 15 weeks
after Pa-G1 by selecting all citations (edges) that appear
before the corresponding week. We evaluate the inﬂuence
spread of the seeds selected from G0 by different algorithms
to those selected from different states of Gr using Greedy
(run directly on Gr). Here SN denotes the seeds selected
by different algorithms running on G0 while SG denotes the
ideal solution by running Greedy in Gr. Therefore, the Y-
axis shows the ratio that compares the expected inﬂuence for
different algorithms to that of running Greedy in Gr. When
Gr = G0 (i.e., tr = t0), the problem degenerates to classical
IM. Consequently, seeds of all algorithms share almost the
same quality. However, as tr increases, the quality of seeds
set selected by different algorithms at G0 decreases. Clearly,
in comparison to classical IM techniques, our PROTEUS-SEER
exhibits the highest inﬂuence spread quality for tr > 0.
Next, we vary the effect network change rate by selecting
several states of Gr such that 1 ≤|Vr|/|V0| ≤2.25. Note
that this simulates different degree of change to the topology
of the network G0 at tr. We evaluate the inﬂuence spread of
the seeds selected from G0 by different algorithms to those
selected from different state of Gr using Greedy (run directly
over Gr). The results are shown in Figures 5(c) and (d). When
Gr = G0 (i.e., |Vr|/|V0| = 1), the problem degenerates to
classical IM. As the difference between Gr and G0 increases,
the quality of seeds set selected by different algorithms at G0
decrease. Clearly, our proposed techniques exhibit the highest
inﬂuence spread quality.
Inﬂuence spread for different k. Next, we simulate the
inﬂuence spread of selected seeds for networks with varying k
and investigate whether state-of-the-art IM algorithms exhibit
similar or different inﬂuence spread quality compared to our
proposed algorithms for the PROTEUS-IM problem. Fig. 6 plots
the inﬂuence spreads (with inﬂuence probability p = 0.01)
for different k for networks exhibiting different DoC. In each
of the ﬁgures, we select top-k seeds in G0 using Greedy,
IRIE, IMM, MaxG, PROTEUS-GENIE, and PROTEUS-SEER and
simulate the inﬂuence spread process in Gr. The inﬂuence
spread is measured by the number of eventually inﬂuence
nodes that is averaged over 10,000 simulations. We compare
the inﬂuence spread results with that of the seeds selected
using Greedy in Gr, which can be viewed as the ground-truth
seeds set. Note that closer the inﬂuence spread (computed by a


## Page 12


50
 55
 60
 65
 70
 75
 80
 85
 90
 26
 30
 34
 38
 42
 46
 50
Number of influenced nodes
Seed set size
Greedy Gr
PRO-GENIE
PRO-SEER
IMM
IRIE
MaxG
(a) Low DoC
 12000
 14000
 16000
 18000
 20000
 22000
 24000
 10
 15
 20
 25
 30
 35
 40
 45
 50
Number of influenced nodes
Seed set size
Greedy Gr
PRO-SEER
IMM
IRIE
MaxG
(b) High DoC
 8000
 10000
 12000
 14000
 16000
 18000
 20000
 10
 15
 20
 25
 30
 35
 40
 45
 50
Number of influenced nodes
Seed set size
Greedy Gr
PRO-SEER
IMM
IRIE
MaxG
(c) High DoC
 200
 220
 240
 260
 280
 300
 320
 340
 360
 380
 50
 60
 70
 80
 90
 100
Number of influenced nodes
Seed set size
Greedy Gr
PRO-GENIE
PRO-SEER
Greedy G0
IMM
IRIE
MaxG
(d) Moderate DoC
Fig. 6: Inﬂuence spread of different seeds sets. (a) G0 = Syn-G2, Gr = Syn-G3; (b) G0 = Pa-G3, Gr = Pa-G4; (c) G0 =
Pa-G1, Gr = Pa-G3; (d) G0 = Ph-G1, Gr = Ph-G2.
speciﬁc technique) is to this ground-truth seed set, the better is
its inﬂuence spread quality. Speciﬁcally, (G0, Gr) are chosen
to represent different degree of change (DoC).
Observe that PROTEUS-GENIE and MaxG achieve the best
inﬂuence spread quality, followed by our heuristic approach
PROTEUS-SEER. Notably, MaxG iteratively updates the se-
lected seeds whenever a new node arrives in the network.
Interestingly, despite the impractical assumptions made by
MaxG as mentioned in Section VI-A, it cannot provide
distinguishable performance beneﬁt compared to our algo-
rithms. In other words, PROTEUS-GENIE and PROTEUS-SEER
demonstrate comparable seed set quality without assuming the
knowledge of complete topology of the target network (unlike
MaxG).
In summary, the inﬂuence spread of our proposed
approaches are within 83% - 99% of the ideal solution.
In contrast, the state-of-the-art classical IM approaches only
achieve 65%-89% of the ideal inﬂuence spread.
Running times. Fig. 7 reports the running times of different
algorithms for different DoC. Speciﬁcally, we run Greedy,
IRIE, IMM, PROTEUS-GENIE, and PROTEUS-SEER on G09 for
the three different datasets. Observe that although PROTEUS-
GENIE produces most accurate results, it also consumes the
longest time as it requires I iterations of network evolution
simulations. On the other hand, PROTEUS-SEER is signiﬁcantly
faster than PROTEUS-GENIE as the former avoids huge number
of iterations caused by R and I. Our PROTEUS-SEER ﬁnishes
within an hour on the largest network while providing near-
optimal inﬂuence spread quality. Therefore, PROTEUS-SEER
is suitable for time-sensitive tasks and gives a good balance
between inﬂuence spread quality and running time. Note that
although our techniques are slower than IRIE and IMM, as
reported earlier, these approaches have poorer inﬂuence spread
quality. It is important to reemphasize that the seed set quality
is paramount to companies as they would like to maximize
the inﬂuence spread of their products.
Effect of I. Intuitively, if we increase the number of in-
stances of predicted target network (i.e., I), it may increase
the running time. Fig. 8 reports the running times by varying
I in PROTEUS-GENIE. Obviously, the running time increases
almost linearly with respect to I, which is consistent with
9 MaxG keeps on running during the evolution of a network in contrast
to all other competitors. Hence, for fair comparison its running time is not
included.
Theorem 2. We also investigated the inﬂuence spread quality
by varying I. Clearly, as I increases the quality of selected
seeds also improve. However, the improvement also follows a
diminishing return pattern. If I exceeds 500, the improvement
in seeds quality is within 1%. Note that this phenomenon is
favorable to our framework as we do not need to set I to a
very large value in order to ﬁnd superior quality seeds.
Effect of p. Lastly, we test the inﬂuence spread quality of
networks with different degree of change by varying p to 0.05
and 0.1, respectively. Fig. 9 reports the inﬂuence spread quality
for different experimental settings. Observe that the inﬂuence
spread quality of different algorithms are qualitatively similar
to those reported earlier for p = 0.01.
VII. CONCLUSIONS & FUTURE WORK
The classical inﬂuence maximization (IM) problem as intro-
duced in [1] has been extensively studied in the literature. It
has been a solid foundation for many subsequent algorithmic
improvements to the IM problem with non-trivial performance
guarantees as well as novel variations to the original problem.
Unfortunately, due to the inherent limitation of the problem
deﬁnition, existing techniques will often generate suboptimal
seeds, unless very unrealistic changes happen to the real-
world social networking landscape (either social networks stop
evolving during inﬂuence propagation or inﬂuence propagation
takes negligible time).
In this paper, we present PROTEUS-IM problem, which is
designed to replace the classical version by assuming that
inﬂuence propagation time is not negligible, during which the
underlying network evolves. Hence, it aims to ﬁnd seeds in the
current network that maximizes inﬂuence spread in a future
instance of the network, while considering the evolution of
the network during inﬂuence propagation. We propose a pair
of algorithms called PROTEUS-GENIE and PROTEUS-SEER,
respectively, to address the PROTEUS-IM problem. Speciﬁcally,
our algorithms address the challenge of unknown topology of
the target network by predicting it using a network evolution
model and then leveraging existing cascade models on this
predicted network to discover seeds. Experimental results
conducted over a couple of real-world datasets demonstrate
that our proposed algorithms consistently outperform state-of-
the-art ones designed to address the classical IM problem.


## Page 13


Greedy G_0
IRIE
IMM
PRO-GENIE
PRO-SEER
0.1
1
10
100
1000
10000
Running time (seconds)
Algorithms
(a) G0 = Syn-G1, Gr = Syn-G3
Greedy G_0
IRIE
IMM
PRO-GENIE
PRO-SEER
1
10
100
1000
10000
100000
1000000
1E7
Running time (seconds)
(b) G0 = Ph-G1, Gr = Ph-G2
Greedy G_0
IRIE
IMM
PRO-SEER
0.01
0.1
1
10
100
Running time (hours)
Algorithms
(c) G0 =Pa-G1, Gr =Pa-G3
Greedy G_0
IRIE
IMM
PRO-SEER
0.1
1
10
100
Running time (hours)
Algorithms
(d) G0 =Pa-G3, Gr =Pa-G4
Fig. 7: Running times of different algorithms.
 75
 80
 85
 90
 95
 0
 200
 400
 600
 800
 1000
 1200
 0
 5000
 10000
 15000
 20000
 25000
Number of influenced nodes
Running time (seconds)
I
running time
influenced node
(a) Low DoC
 355
 360
 365
 370
 375
 380
 385
 0
 200
 400
 600
 800
 1000
 1200
 0
 25
 50
 75
 100
 125
 150
 175
 200
 225
Number of influenced nodes
Running time (hours)
I
running time
influenced node
(b) Moderate DoC
Fig. 8: Effect of I (k = 50). (a) G0 = Syn-G1, Gr = Syn-G2;
(b) G0 = Ph-G1, Gr = Ph-G2.
We believe that the
PROTEUS-IM problem can be the
foundation for future research on IM in several directions.
First, it has the potential to catalyze the research community
to revisit theoretical and practical aspects of existing IM so-
lutions (e.g., algorithms, theoretical guarantees) and different
variations of traditional IM problems. Second, the state-of-the-
art Forest Fire Model, which we have utilized to model net-
work evolution, despite demonstrating superior performance
in capturing network evolution, does not incorporate node
or edge deletions. Hence, exploration of a more generalized
network evolution model can further enhance the inﬂuence
spread quality of our proposed solutions.
REFERENCES
[1] D. Kempe, J. M. Kleinberg, and É. Tardos, “Maximizing the spread of
inﬂuence through a social network,” in KDD.
ACM Press, 2003, pp.
137–146.
[2] S. Shirazipourazad, B. Bogard, H. Vachhani, A. Sen, and P. Horn,
“Inﬂuence propagation in adversarial setting: how to defeat competition
with least amount of investment,” in CIKM.
ACM Press, 2012, pp.
585–594.
[3] W. Chen, Y. Wang, and S. Yang, “Efﬁcient inﬂuence maximization in
social networks,” in KDD, 2009.
[4] A. Goyal, W. Lu, and L. V. S. Lakshmanan, “Simpath: An efﬁcient
algorithm for inﬂuence maximization under the linear threshold model,”
in ICDM, 2011.
[5] H. T. Nguyen, M. T. Thai, and T. N. Dinh, “Stop-and-stare: Optimal
sampling algorithms for viral marketing in billion-scale networks,” in
SIGMOD, 2016, pp. 695–710.
[6] K. Huang, S. Wang, G. S. Bevilacqua, X. Xiao, and L. V. S. Laksh-
manan, “Revisiting the stop-and-stare algorithms for inﬂuence maxi-
mization,” PVLDB, vol. 10, no. 9, pp. 913–924, 2017.
[7] S. Chen, J. Fan, G. Li, J. Feng, K. Tan, and J. Tang, “Online topic-aware
inﬂuence maximization,” PVLDB, vol. 8, no. 6, 2015.
[8] H. Li, S. S. Bhowmick, and A. Sun, “Cinema: conformity-aware greedy
algorithm for inﬂuence maximization in online social networks,” in
EDBT.
ACM Press, 2013, pp. 323–334.
[9] T. Carnes, C. Nagarajan, S. M. Wild, and A. van Zuylen, “Maximizing
inﬂuence in a competitive social network: a follower’s perspective,” in
ICEC, 2007.
[10] A. Arora, S. Galhotra, and S. Ranu, “Debunking the myths of inﬂuence
maximization: An in-depth benchmarking study,” in SIGMOD, 2017, pp.
651–666.
[11] J. L. Iribarren and E. Moro, “Impact of human activity patterns on the
dynamics of information diffusion,” Phys. Rev. Lett., vol. 103, p. 038702,
Jul 2009.
[12] G. A. Fowler, “Facebook: One billion and counting,” The Wall Street
Journal (Dow Jones), vol. 2012-10-04, 2012.
[13] S.
Fiegerman.
(2012)
Twitter
now
has
more
than
200
million
monthly
active
users.
http://mashable.com/2012/12/18/twitter-200-million-active-users/.
[14] J. Leskovec, L. Backstrom, R. Kumar, and A. Tomkins, “Microscopic
evolution of social networks,” in KDD, 2008.
[15] H. Zhuang, Y. Sun, J. Tang, J. Zhang, and X. Sun, “Inﬂuence maxi-
mization in dynamic social networks,” in ICDM, 2013.
[16] X. Chen, G. Song, X. He, and K. Xie, “On inﬂuential nodes tracking
in dynamic social networks,” in SDM, 2015.
[17] N. Ohsaka, T. Akiba, Y. Yoshida, and K. Kawarabayashi, “Dynamic
inﬂuence analysis in evolving networks,” PVLDB, vol. 9, no. 12, pp.
1077–1088, 2016.
[18] Y. Wang, Q. Fan, Y. Li, and K. Tan, “Real-time inﬂuence maximization
on dynamic social streams,” PVLDB, vol. 10, no. 7, pp. 805–816, 2017.
[19] G. Tong, W. Wu, S. Tang, and D. Du, “Adaptive inﬂuence maximization
in dynamic social networks,” IEEE/ACM Trans. Netw., vol. 25, no. 1,
pp. 112–125, 2017.
[20] N. T. H. Gayraud, E. Pitoura, and P. Tsaparas, “Diffusion maximization
in evolving social networks,” in COSN, 2015.
[21] C. C. Aggarwal, S. Lin, and P. S. Yu, “On inﬂuential node discovery in
dynamic social networks,” in SDM, 2012.
[22] H. Ma, H. Yang, M. R. Lyu, and I. King, “Mining social networks using
heat diffusion processes for marketing candidates selection,” in CIKM,
2008, pp. 233–242.
[23] J. Leskovec, J. M. Kleinberg, and C. Faloutsos, “Graphs over time:
densiﬁcation laws, shrinking diameters and possible explanations,” in
KDD, 2005, pp. 177–187.
[24] Y. Tang, Y. Shi, and X. Xiao, “Inﬂuence maximization in near-linear
time: A martingale approach,” in SIGMOD, 2015.
[25] K. Jung, W. Heo, and W. Chen, “IRIE: scalable and robust inﬂuence
maximization in social networks,” in ICDM, 2012.
[26] C. Borgs, M. Brautbar, J. T. Chayes, and B. Lucier, “Maximizing social
inﬂuence in nearly optimal time,” in SODA, 2014, pp. 946–957.
[27] D. Chakrabarti and C. Faloutsos, “Graph mining: Laws, generators, and
algorithms,” ACM Comput. Surv., vol. 38, no. 1, 2006.
[28] L. Backstrom, D. P. Huttenlocher, J. M. Kleinberg, and X. Lan, “Group
formation in large social networks: membership, growth, and evolution,”
in KDD, 2006, pp. 44–54.


## Page 14


30000
 40000
 50000
 60000
 70000
 80000
 90000
 100000
 10
 15
 20
 25
 30
 35
 40
 45
 50
Number of influenced nodes
Seed set size
Greedy Gr
PRO-SEER
IMM
IRIE
MaxG
(a) G0 =Pa-G1, Gr =Pa-G3 (High DoC)
 60000
 70000
 80000
 90000
 100000
 110000
 120000
 10
 15
 20
 25
 30
 35
 40
 45
 50
Number of influenced nodes
Seed set size
Greedy Gr
PRO-SEER
IMM
IRIE
MaxG
(b) G0 =Pa-G3, Gr =Pa-G4 (High DoC)
 900
 1000
 1100
 1200
 1300
 1400
 1500
 1600
 1700
 1800
 1900
 50
 60
 70
 80
 90
 100
Number of influenced nodes
Seed set size
Greedy Gr
PRO-GENIE
PRO-SEER
Greedy G0
IMM
IRIE
MaxG
(c) G0 =Ph-G1, Gr =Ph-G2 (Moderate DoC)
 70000
 80000
 90000
 100000
 110000
 120000
 130000
 140000
 150000
 160000
 170000
 180000
 10
 15
 20
 25
 30
 35
 40
 45
 50
Number of influenced nodes
Seed set size
Greedy Gr
PRO-SEER
IMM
IRIE
MaxG
(d) G0 =Pa-G1, Gr =Pa-G3 (High DoC)
 110000
 120000
 130000
 140000
 150000
 160000
 170000
 180000
 190000
 200000
 210000
 220000
 10
 15
 20
 25
 30
 35
 40
 45
 50
Number of influenced nodes
Seed set size
Greedy Gr
PRO-SEER
IMM
IRIE
MaxG
(e) G0 =Pa-G3, Gr =Pa-G4 (High DoC)
 1800
 2000
 2200
 2400
 2600
 2800
 3000
 3200
 3400
 3600
 50
 60
 70
 80
 90
 100
Number of influenced nodes
Seed set size
Greedy Gr
PRO-GENIE
PRO-SEER
Greedy G0
IMM
IRIE
MaxG
(f) G0 =Ph-G1, Gr =Ph-G2 (Moderate DoC)
Fig. 9: Inﬂuence spread vs p: (a-c) p = 0.05; (d-f) p = 0.1.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1703.08831v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1703.08831v1_Token-based_Function_Computation_with_Memory

> Source: 1703.08831v1_Token-based_Function_Computation_with_Memory.pdf

> Pages: 27

---


## Page 1


1
Token-based Function Computation with
Memory
Saber Salehkaleybar, Student Member, IEEE, and S. Jamaloddin Golestani, Fellow, IEEE
Dept. of Electrical Engineering, Sharif University of Technology, Tehran, Iran
Emails: saber saleh@ee.sharif.edu, golestani@ieee.org
Abstract
In distributed function computation, each node has an initial value and the goal is to compute a
function of these values in a distributed manner. In this paper, we propose a novel token-based approach
to compute a wide class of target functions to which we refer as “Token-based function Computation
with Memory” (TCM) algorithm. In this approach, node values are attached to tokens and travel across
the network. Each pair of travelling tokens would coalesce when they meet, forming a token with a new
value as a function of the original token values. In contrast to the Coalescing Random Walk (CRW)
algorithm, where token movement is governed by random walk, meeting of tokens in our scheme is
accelerated by adopting a novel chasing mechanism. We proved that, compared to the CRW algorithm,
the TCM algorithm results in a reduction of time complexity by a factor of at least
p
n/ log(n) in
Erd¨os-Renyi and complete graphs, and by a factor of log(n)/ log(log(n)) in torus networks. Simulation
results show that there is at least a constant factor improvement in the message complexity of TCM
algorithm in all considered topologies. Robustness of the CRW and TCM algorithms in the presence of
node failure is analyzed. We show that their robustness can be improved by running multiple instances
of the algorithms in parallel.
I. INTRODUCTION
Distributed function computation is an essential building block in many network applications
where it is required to compute a function of initial values of nodes in a distributed manner.
For instance, in wireless sensor networks, distributed inference algorithms can be executed
by computing average of the sensor measurements as a subroutine. Examples of distributed
inference in sensor networks include transmitter localization [1], parameter estimation [2], and
data aggregation [3]. As another application, consider a network with n processors in which
each processor has a local utility function and the goal is to obtain the optimal solution of
sum of the utility functions subject to some constraints. This problem has frequently arisen in
network optimization algorithms such as distributed learning [4], link scheduling [5], and network
utility maximization [6]. All these algorithms utilize a distributed sum or average computation
subroutine in solving the optimization problems.
Consider the problem of computing a target function fn(v0
1, · · · , v0
n) in a network with n
nodes, where v0
i is the initial value of node i. A common approach is based on constructing
spanning trees [7], [8]. In this solution, the values would be sent toward the root where the ﬁnal
result is computed and sent back to all nodes over the spanning tree. Although the spanning
tree-based solution is quite efﬁcient in terms of message and time complexities, it is not robust
against network perturbations such as node failures or time-varying topologies. For example, the
ﬁnal result may be dramatically corrupted if a node close to the root fails.
To overcome the above drawback of spanning tree-based solutions, recent approaches take
advantage of local interactions between nodes [9]. In these approaches, each node i which has
a value, chooses one of its neighbors, say node j; The two nodes then update their values
arXiv:1703.08831v1  [cs.DC]  26 Mar 2017


## Page 2


2
based on a predeﬁned rule function g(., .) which is determined by the target function fn(.) (see
Lemma II.1). By iterating this process in the entire network, the target function is computed in
a distributed manner. Let vi and vj be the current values of nodes i and j, respectively. Two
possible options for executing the rule function g(vi, vj) are:
(
1)v+
i = v+
j = g(vi, vj),
2)v+
i = e, v+
j = g(vi, vj),
(1)
where v+
i and v+
j are the updated values of nodes i and j, respectively. The value e is the identity
element of the rule function g(., .), i.e. g(v, e) = g(e, v) = v for any value v.
The ﬁrst option in (1) corresponds to the class of distributed algorithms commonly called
gossip algorithms [9]. The main advantage of these algorithms is that they are robust against
network perturbations due to their simple structure. However, this robust structure is obtained at
the expense of huge time and message complexities [9]. For the ﬁrst option, various updating
rule functions have been proposed for speciﬁc target functions like average [10], min/max, and
sum [11]. For instance, the updating rules g(vi, vj) = (vi +vj)/2 and g(vi, vj) = min(vi, vj) can
be used to compute average and min functions, respectively.
The second updating option can compute a wide class of target functions including the ones
computable by gossip algorithms (see Lemma II.1) and it is much more energy-efﬁcient than the
gossip algorithms [12]. This approach can be easily implemented by a token-based algorithm:
Suppose that each node has a token at the beginning of the algorithm and passes its initial value
to its token. A node is said to be inactive when it does not have a token. If the local clock of
an active node like i ticks, it chooses a random neighbor node, like node j, and sends its token
carrying its value. Upon receiving the token, node j updates its value, and becomes active (if
it is not already)1. Then, node i sets its own value to e, and becomes inactive. From token’s
view, each token walks in the network, randomly, until it meets another token. The two tokens
will then coalesce and form a token with an updated value. This process continues until the
result is aggregated in one token. Finally, the last active node can broadcast the result by a
controlled ﬂooding mechanism2. This computation scheme is called Coalescing Random Walk
(CRW) algorithm after the coalescing random walks [13].
The CRW algorithm offers comparable performance to spanning tree-based solutions in terms
of message complexity [12], making it much more energy-efﬁcient than the gossip algorithms.
However, it is still slow due to deﬁciency in token coalescence when only a few tokens remain in
the network. Hence, authors in [12], modiﬁed the CRW algorithm in order to improve its running
time. In the modiﬁed algorithm, which we call the truncated CRW algorithm, at some point of
time, the execution of the CRW algorithm is terminated and each active node broadcasts the value
of its token via a controlled ﬂooding mechanism, leaving the completion of the computation to
each network node. However, this solution does not lead to a signiﬁcant improvement in time
or message complexity [12].
In this paper, we propose a mechanism to speed up the coalescence of tokens. Suppose that
each token has a unique identiﬁer (UID) besides its carried value. In the proposed mechanism,
each node registers the maximum UID of tokens seen so far, and the outgoing edge taken by the
token with the maximum UID. When a token enters a node previously visited by a token with
1In case of computing the sum function, the updating rule function g(vi, vj) is vi + vj and the identity element is equal to
zero.
2In section II, we will explain how the last active node broadcasts the ﬁnal result.


## Page 3


3
1
ID
2
ID
Figure 1. An example of execution of TCM algorithm in a torus network: Suppose that two tokens are left in the network. Let
the UIDs of the two tokens be ID1 and ID2 where ID1 > ID2. Nodes with shaded patterns are the nodes that token ID1
has visited seen so far. The arrows show the most recent direction taken by token ID1. If token ID2 chooses its left neighbor
node in the next step, it is trapped in the set of shaded nodes and follows a path to token ID1.
higher UID, it follows the registered outgoing edge. Otherwise, it will go to a random chosen
neighbor node, according to a predeﬁned probability. Figure 1 illustrates a scenario where two
tokens are left in the network and show how coalescing is expedited in the proposed scheme.
Since nodes memorize the outgoing edge of a token with maximum UID they have seen, we call
the proposed scheme “Token-based function Computation with Memory” (TCM) Algorithm.
It is interesting to mention an analogy between this scheme and cosmology. Think of tokens
in the network as cosmic dusts in space. Accordingly, the process of function computation is
like forming a planet from cosmic dusts. By running the TCM algorithm, tokens with small
UID (light dusts) are trapped in the set of nodes visited by tokens with higher UID (in the
gravitational ﬁeld of heavy dusts). The coalescing process continues until a single token is left,
similar to birth of a planet.
The main contributions of the paper are as follows:
• We show that the proposed TCM algorithm, by accelerating coalescing of tokens, reduces
the average time complexity by a factor
p
n/ log(n) in complete graphs and Erd¨os-Renyi
model compared to the CRW algorithm and its truncated version. Furthermore, there is at
least log(n)/ log(log(n)) factor improvement in torus networks. Simulation results show that
the TCM algorithm also outperforms the CRW algorithm in terms of message complexity.
• In CRW and TCM algorithms, the ﬁnal result may be corrupted if an active node fails.
Hence, it is quite important to study the robustness of these algorithms under node failures.
In this regard, we evaluate the performance of CRW and TCM algorithms based on a
proposed robustness metric. We show that the robustness can be substantially improved by
running multiple instances of the TCM and CRW algorithms in parallel. We prove that, for
the CRW algorithm, the required number of instances in order to tolerate the failure rate
α/n in complete graphs, is of the order O(nα). While the TCM algorithm needs to run
only O(1) instances in parallel.
• We study the performance of TCM and CRW algorithms under random walk mobility model
[14]. Simulation results show that both algorithms can compute the class of target functions
deﬁned in Lemma II.1 successfully even in high mobility conditions.
The remainder of the paper is organized as follows: In Section II, the TCM algorithm is
described. In Section III, the performances of TCM and CRW algorithms are analyzed and
compared for different network topologies. In Section IV, we study the robustness of both
algorithms in complete graphs. In Section V, the performances of TCM and CRW algorithms are


## Page 4


4
evaluated through simulations and then compared with analytical results. Finally, we conclude
with Section VI.
II. THE TCM ALGORITHM
A. System model
Consider a network of n nodes, where each node i has an initial value v0
i and the goal is to
compute a function fn(v0
1, · · · , v0
n) of initial values in a distributed manner. The topology of the
network is represented by a bidirected graph, G = (V, E), with the vertex set V = {1, ..., n},
and the edge set E ⊆V × V , such that (i, j) ∈E if and only if nodes i and j can communicate
directly. We index ports of node i with {1, · · · , di}, where di is the degree of node i.
It is assumed that the function fn(.) is symmetric for any permutation π of the set {1, · · · , n},
i.e. fn(v0
1, · · · , v0
n) = fn(v0
π1, · · · , v0
πn). This means that it does not matter which node of the
network holds which part of the initial values.
B. Description of the TCM algorithm
Assume that a UID is assigned to each node i.3 At the beginning of the algorithm, each node
has a token to which it passes its UID and initial value. It is also assumed that each node has an
independent clock which ticks according to a Poisson process with rate one. Let the value and
UID of the token at node i be value(i) and ID(i), respectively. We denote the token at node i
by the vector [value(i), size(i), ID(i)]. The role of parameter size(i) will be explained in the
next part.
The TCM algorithm computes the target function fn(.) by passing and merging tokens in the
network. When a node does not have a token, it becomes inactive until a neighbor node gets
in contact with it. Let memory(i) be the maximum UID of the tokens, node i has seen so far.
Algorithm 1 describes how and when an active node i sends or merges tokens. The subroutine
SEND() is executed by each tick of local clock while the subroutine RECEIVE() is activated
upon receiving a token from some neighbor node.
Suppose that the local clock of active node i ticks. Node i decides to send the token
[value(i), size(i), ID(i)] to a neighbor node. In this respect, we make distinction between two
cases:
Case 1- memory(i) = ID(i): In this case, node i decides to pass the token to a random
neighbor node with probability psend. Thus, node i waits for
1
psend number of clock ticks on
average before sending out the token. To implement the waiting mechanism, node i will exit
the subroutine Send() with probability 1 −psend, each time its clock ticks (line 6). Otherwise, it
chooses a random port j, sets the path(i) to j, and sends the token on that port (lines 7-8).
Case 2- ID(i) < memory(i): In this case, node i sends the token on the port path(i) with
probability one.
Now, suppose that node i receives a token [value, size, ID]. If node i is inactive, then the
received token remains unchanged. Otherwise, it will coalesce with the token at nodes i and the
token with greater UID remains in the network (line 15). Then, the parameters value(i), size(i),
and memory(i) are updated to g(value(i), value), size(i) + size, and max(memory(i), ID),
respectively (lines 16-18). The updating rule function g(., .) is determined by the target function
3One can use randomized algorithms to assign UIDs. Each node randomly chooses an integer number in the set {1, · · · , kn2}.
From birthday problem [15], it can be shown that each node gets a UID with high probability if k is large enough. Furthermore,
each node can encode its UID with O(log(n)) bits.


## Page 5


5
Algorithm 1 The TCM algorithm
1: Initialization: memory(i) ←ID(i), path(i) ←{}, value(i) ←v0
i , size(i) ←1 ,∀i ∈{1, · · · , n},
2:
Node i generates token [value(i), size(i), ID(i)].
3: procedure SEND( )
4:
if ID(i) ̸= 0 then
▷ID(i): the UID of token which is now in node i. It is equal to zero for inactive nodes.
5:
if memory(i) = ID(i) then
6:
Break with probability 1 −psend.
7:
choose a port randomly like j.
8:
path(i) ←j
▷path(i): a port number of node i through which the token with highest UID has passed.
9:
end if
10:
Send token [value(i), size(i), ID(i)] on port path(i).
11:
ID(i) ←0,
value(i) ←e,
size(i) ←0.
12:
end if
13: end procedure
14: procedure RECEIVE([value, size, ID])
15:
ID(i) ←max(ID(i), ID)
16:
value(i) ←g(value(i), value)
17:
size(i) ←size(i) + size.
18:
memory(i) ←max(memory(i), ID)
▷memory(i): maximum UID that node i has ever seen.
19: end procedure
fn(.) as explained in Lemma II.1. Furthermore, the value e is the identity element of the rule
function g(., .), i.e. g(v, e) = g(e, v) = v for any value v.
From top view, each token walks randomly in the network until it enters a node visited by
a token with higher UID (Case 1). Then, it follows a path to meet the token with higher UID
(Case 2). We call the walking modes in the ﬁrst and second cases the random walk and chasing
modes, respectively. In the random walk mode, a token walks with the lower speed psend. Thus,
it can be followed by tokens with lower UID more quickly.
C. Termination of the TCM algorithm
The process in Algorithm 1 continues until a few tokens remain in the network. In order to
terminate the algorithm, we consider two options:
• Option 1- Assume that the exact network size, n, is known by all nodes. Furthermore,
each node i has a parameter size(i), beside its initial value which is equal to one at the
beginning. The sum of parameters {size(i), i ∈{1, · · · , n}} can be computed in parallel
to the target function. If the parameter size in an active node reaches n, it can identify
itself as the unique active node in the network. Then, it broadcasts the output of the TCM
algorithm to all nodes by controlled ﬂooding, further explained below.
• Option 2- Suppose that there exists an upper bound on the network size. Then, the execution
time of the TCM algorithm can be adjusted to a time Trun such that, on average, at most
a constant number of active nodes remain after time Trun. Afterwards, each active node
broadcasts the value of its token including the UID. All nodes can obtain the ﬁnal result by
combining values received from the active nodes. In analyzing the performances of CRW
and TCM algorithms, we consider the ﬁrst option.
In controlled ﬂooding, an active node i sends the value and UID of its token to all neighbor
nodes. Each node j, upon receiving this message from a node k for the ﬁrst time, forwards it to
all its neighbor nodes except node k. Since each message is transmitted on each edge at most


## Page 6


6
twice, the time and message complexities of controlled ﬂooding are Θ(diam(G)) and Θ(|E|),
respectively4.
The allocation of memory at node i would be: (memory(i), path(i), size(i), value(i)) where
the possible values of the ﬁrst three entries are in the set {1, · · · , n}. Thus, the TCM algorithm
requires at most Θ(log(n)) bits more storage capacity compared to the CRW algorithm. The
next Lemma identiﬁes the class of target functions fn(v0
1, · · · , v0
n) which can be computed by
the TCM algorithm.
Lemma II.1. The TCM algorithm can compute a collection of symmetric functions {fn(.)} if
there exists an updating rule function g(., .) such that for any permutation π of the set {1, · · · , n},
we have: fn(v0
1, · · · , v0
n) = g(fk(v0
π1, · · · , v0
πk), fn−k(v0
πk+1, · · · , v0
πn)), 1 ≤k ≤n, ∀n.
Proof. The proof is the same as Lemma 3.1 in [12].
A wide class of target functions fulﬁl these requirements such as min/max, average, sum, and
exclusive OR. For instance, updating rule functions g(vi, vj) = vi + vj, g(vi, vj) = max(vi, vj),
and g(vi, vj) = vi ⊕vj are used for computing sum, minimum, and exclusive OR functions,
respectively. The average function can also be computed by dividing the output of the sum
function by the network size which is obtained by summing parameter size of nodes in parallel
to computing the sum function.
III. PERFORMANCE ANALYSIS OF THE CRW AND TCM ALGORITHMS
In this section, we study the performances of CRW and TCM algorithms in complete graphs,
Erd¨os-Renyi model, and torus networks. The considered network topologies may resemble
different practical networks. For instance, the topology of a wireless network, in which all
stations are in transmission range of each other, is typically modelled by a complete graph.
A peer-to-peer network such that all nodes can communicate with each other in the overlay
network, is another example of complete graphs. As we explain later, the Erd¨os-Renyi model is
frequently used as a model to represent social networks. Furthermore, torus network is a simple
structure widely used to model distributed processing systems with grid layout or grid-based
wireless sensor networks.
As a prelude to analyze the performance of the TCM algorithm, we ﬁrst present an analysis of
time and message complexities of the CRW algorithm for complete graphs, although the CRW
algorithm is already analyzed in [17]. Then, we study time complexity of the TCM algorithm in
complete graphs. We also give a naive analysis of message complexity of the TCM algorithm
in complete graphs and time/message complexity of both algorithms in Erd¨os-Renyi model and
torus networks. The summary of time and message complexities for the TCM algorithm and
the CRW/truncated CRW algorithms are given in Table 1. In complete graphs and Erd¨os-Renyi
model, the TCM algorithm reduces the time complexity at least by a factor
p
n/ log(n). In the
case of torus networks, there is an improvement at least by a factor log(n)/ log(log(n)) with
respect to the CRW algorithm. Furthermore, the message complexity of the TCM algorithm is at
most the same as the CRW and truncated CRW algorithms. Simulation results show that there
is at least a constant factor improvement in the message complexity by employing the TCM
algorithm in all considered topologies.
In analyzing the CRW and TCM algorithms, we assume that each token is transmitted
instantaneously. Furthermore, passing a token is counted as sending one message in the network.
4In complete graphs, we can employ gossip algorithm proposed in [16] to broadcast the output with time and message
complexities of the order O(log(n)) and O(n log(n)), respectively.


## Page 7


7
Table I
PERFORMANCE COMPARISON OF THE TCM AND CRW ALGORITHMS IN TERMS OF TIME AND MESSAGE COMPLEXITIES.
(a) Time complexity
Complete graphs
Erd¨os-Renyi model
Torus networks
TCM
O(
p
n log(n))
O(
p
n log(n))
O(n log(log(n)))
CRW
Θ(n)
Θ(n)
Θ(n log(n)) [12]
Truncated CRW
Θ(n)
Θ(n)
Θ(n) [12]
(b) Message complexity
Complete graphs
Erd¨os-Renyi model
Torus networks
TCM
O(n log(n))
O(n log(n))
-
CRW
Θ(n log(n))
Θ(n log(n))
Θ(n log2(n)) [12]
Truncated CRW
Θ(n log(n))
Θ(n log(n))
Θ(n log2(n)) [12]
A. Time and message complexities of the CRW algorithm on complete graphs
Let TCRW and MCRW be the average time and message complexities of the CRW algorithms,
respectively. Next theorem gives a tight bound on TCRW and MCRW.
Theorem III.1. The average time and message complexities of the CRW algorithm in complete
graphs are of the orders Θ(n) and Θ(n log(n)), respectively.
Proof. We can represent the process of token coalescing by a Markov chain with the number
of active nodes remaining in the network deﬁned as the state (see Fig. 2). The chain undergoes
transition from state k to state k −1 if a token chooses an active nodes for the next step, which
occurs with rate k(k−1)
n−1 . Let Tk be the sojourn time in state k. Then the average time complexity
is:
TCRW =
n
X
k=2
E{Tk} =
n
X
k=2
n −1
k(k −1) = (n −1)(1 −1/n) ≈n −2.
(2)
Besides, in state k, on average, (n −1)/(k −1) messages are transmitted before observing a
coalescing event. Therefore, the average message complexity would be5:
MCRW =
n
X
k=2
n −1
k −1 ≈(n −1)(log(n −1) + 0.577).
(3)
Thus, the average time and message complexities of CRW algorithm are of the orders Θ(n)
and Θ(n log(n)), respectively.
B. Time complexity of TCM algorithm on complete graphs
Let the UIDs of the n tokens at the beginning of the algorithm be denoted as ID1, · · · , IDn.
Without loss of generality, assume that ID1 > · · · > IDn. Throughout this section, we also
assume that psend = 1
2.
5
n
X
k=1
1/k ≈log(n) + c where c ≈0.577 is the Euler-Mascheroni Constant.


## Page 8


8
n
n-1
k
k-1
n-2
n
2
−
n
1
)1
(
−
−
n
k
k
Figure 2. Markov chain model for the process of token coalescing in the CRW algorithm. The state k corresponds to k active
nodes in the network.
Deﬁnition III.1. Let Tcoal(IDi), i = 2, · · · , n, denote the time that token IDi coalesces
with a token with a larger UID. Thus, the algorithm running time would be: Trun(n) =
maxi∈{2,··· ,n} Tcoal(IDi).
In the TCM algorithm, token ID1 walks randomly in the network. In each step, it chooses
a random node from the whole set of network nodes except the node where it is currently
presented. After taking j steps, the average number of visited nodes by token ID1 would be:
n −(n −1) × (1 −1/(n −1))j.
Deﬁnition III.2. We call the set of nodes visited by token ID1 during its ﬁrst j movements the
event horizon of ID1, and denote it by EH1(j).
Notice that, in the TCM algorithm, when a token gets in the event horizon of token ID1, it
cannot escape and will eventually coalesce with token ID1. We borrowed the term event horizon
from general relativity, where it refers to “the point of no return”.
Lemma III.1. The size of event horizon of token ID1 after taking 2j steps, i.e. |EH1(2j)|, is
at least E{|EH1(j)|} ≈n(1 −(1 −1/n)j) with probability greater than 1 −e−n/4−jη where
constant η ≥0.05.
Proof. See Appendix A in the supplemental material.
Now, we can obtain an upper bound on the average time complexity of the TCM algorithm,
from Lemma III.1.
Theorem III.2. In complete graphs, the average time complexity of TCM algorithm is of the
order O(
p
n log(n)).
Proof. For a complete proof, see Appendix B in the supplemental material. Here, in order to
provide better insight about the algorithm, we present a naive analysis, that is based on a modiﬁed
model of the network, where Poisson assumption for clock ticks is relaxed. Instead, we adopt a
slotted model for time, where each token in the chasing mode, takes one step in each time slot.
Furthermore, in the random walk mode, we replace the assumption of psend = 1
2 with sending
token every other slot. Tokens which are scheduled to move in a time slot, take steps in a random
order.
In our analysis, we utilize the following inequality that we trust is correct, based on intuition
and simulation veriﬁcation:
Pr{Tcoal(IDi) ≤t} ≥Pr{Tcoal(ID2) ≤t}, 2 ≤i ≤n.
(4)
As an example, simulation results are given for a network with n = 100 nodes in Fig. 3.


## Page 9


9
0
10
20
30
40
50
60
70
80
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Time
Pr{Tcoal(IDi) ≤t}
 
 
ID10
ID5
ID4
ID3
ID2
Figure 3. Cumulative distribution function of coalescing time for different tokens, n = 100.
First, we derive an upper bound on the probability that the token ID2 gets in the event horizon
of ID1 after time slot t. According to the simpliﬁed timing model, token ID1 moves at even
time slots and token ID2 tries to get in the event horizon of token ID1 at the same time slots. In
order to obtain the upper bound, we wait for 2k time slots to have a big enough event horizon
of token ID1. Since the size of event horizon in the next 2k time slots is equal or greater than
the one at time slot 2k, the probability of not hitting the event horizon in time interval [2k, 4k]
is less than (1 −|EH1(k)|/n)k. By bounding |EH1(k)| from below (see Lemma III.1), we have
for k ≥2
p
n log(n):
Pr{TEH1(ID2) > 4k} ≤(1 −E{|EH1(k/2)|}
n
)k × Pr{|EH1(k)| ≤E{|EH1(k/2)|}}
+ Pr{|EH1(k)| ≤E{|EH1(k/2)|}} × 1
≤(1 −E{|EH1(k/2)|}
n
)k + e−n/4−ηk/2
≤e−√
log(n)/nk + e−n/4−ηk/2,
(5)
where the last inequality is obtained by replacing E{|EH1(k/2)|} ≥E{|EH1(⌊
p
n log(n)⌋)|},
for k ≥2
p
n log(n).
When token ID2 reaches the event horizon of token ID1 at time slot 4k, it takes at most
another 4k time slots to coalesce with token ID1. Because the size of |EH1(k)| is at most 2k
and the relative velocity of two tokens is 1/2. From this fact, we have: Pr{Tcoal(ID2) ≤8k} ≥
Pr{TEH1(ID2) ≤4k}. From (5), we can obtain the following:
Pr{Tcoal(ID2) > k} < e−√
log(n)/nk/8 + e−n/4−ηk/16, k ≥16
p
n log n.
(6)


## Page 10


10
Now, an upper bound can be derived on the average time complexity:
E{Trun(n)} =
∞
X
k=1
Pr{Trun(n) > k} =
∞
X
k=1
Pr{ max
i∈{2,··· ,n} Tcoal(IDi) > k}
≤
∞
X
k=1
min(1,
X
i∈{2,··· ,n}
Pr{Tcoal(IDi) > k})
≤a 16
p
n log(n) +
Z ∞
16√
n log(n)
min(1, (n −1) × (e−√
log(n)/nt/8 + e−n/4−ηt/16))dt
≤b 16
p
n log(n) + 8/
p
n log(n) + 16n
η e−n/4−η√
n log(n).
(7)
(a) From the inequalities in (4) and (6).
(b) Due to (n −1) × (e−√
log(n)/nt/8 + e−n/4−ηt/16) ≤1 for t ≥16
p
n log(n).
From (7), we conclude that the average time complexity is of the order O(
p
n log(n)).
Comparing with the CRW algorithm, the TCM algorithm improves the time complexity with at
least a factor of
p
n/ log(n).
C. Message complexity of TCM algorithm on complete graphs
In this part, we give a naive analysis of the message complexity of TCM algorithm in complete
graphs. To obtain the bound on message complexity, we will show that the average number of
messages sent in the TCM algorithm until observing a coalescing event, is less than the case
for the CRW algorithm.
Proposition III.1. The average message complexity of the TCM algorithm is of the order
O(n log(n)) in complete graphs.
Proof. Assume that clock of an active node i ticks at time t and k tokens remain in the network.
Suppose that token IDr is in node i. The token IDr may be in two different modes: Walking
randomly or following another token with higher UID. In the ﬁrst mode, it will choose any node
like j with probability 1/(n −1). Thus, the probability of coalescing is:
1
n −1
X
j∈{1,··· ,n}\{i}
Pr{ζj(t) = 1},
(8)
where ζj(t) is an indicator parameter which is equal to one if node j is active at time t and
otherwise, it is zero. But the expected number of active nodes excluding node i is:
X
j∈{1,··· ,n}\{i}
1×
Pr{ζj(t) = 1} = k −1. Hence, the probability of coalescing in this mode is (k −1)/(n −1).
In the second mode, token IDr follows another token with higher UID and decided to go to
a neighbor node, let say node l. We know that there exist k −1 tokens excluding token IDr
which walk randomly or follow another token on a trajectory of a random walk. Thus, node l is
active with probability at least (k −1)/(n −1). Following the same arguments in analyzing the
message complexity of the CRW algorithm, the message complexity is of the order O(n log(n)).


## Page 11


11
D. Time and message complexities of TCM and CRW algorithms in Erd¨os-Renyi model
In some network applications, it is required to compute a speciﬁc function in social networks,
such as majority voting [18]. Hence, it is quite important to study the performances of TCM and
CRW algorithms in these scenarios. Erd¨os-Renyi model is frequently used as a simple model to
represent social networks [19]. In this part, we use this model to give a naive analysis on the
time and message complexities of TCM and CRW algorithms in social networks.
In Erd¨os-Renyi model, there exists an edge between any two nodes with probability p. It
can be shown that the graph is almost certainly connected, if p ≥2 log(n)/n [20]. The next
two propositions give upper bounds on the time and message complexities of CRW and TCM
algorithms.
Proposition III.2. In the Erd¨os-Renyi model, the average time and message complexities of
CRW algorithm are of the order O(n) and O(n log(n)), respectively.
Proof. Assume that k tokens remain in the network. Consider token IDi walks randomly until
it meets another token. In each step, it may be located in any node. From the token’s view, it
seems that edges are randomly established with probability p in each step. Suppose that token
IDi is in node l at time t. It will choose an active node with probability, Pselec:
Pselec =
X
m∈{q|ζq(t)=1}
n−2
X
j=0
p × Pr{d′
l = j} × 1/(j + 1) = (k −1) × p × E{1/(d′
l + 1)},
(9)
where d′
l is the degree of node l excluding an active node m. The ﬁrst term in summation shows
the probability of having an edge between two nodes l and m. The second term represents
the probability that node l has j number of neighbor nodes excluding the node m and the last
term is the probability that node l chooses active node m from the set of its neighbor nodes.
From Jensen’s inequality and convexity of function f(x) = 1/(x + 1) over x > 0, we have:
Pselec ≥(k−1)p/(E{d′
l}+1) = (k−1)/(n−2+1/p) ≥(k−1)/(n−2+n/(2 log(n))). It can be
easily veriﬁed that Pselec ≥(k −1)/(1.12(n −1)) = Θ((k −1)/(n −1)) for n ≥100. Following
the same arguments in analyzing the performance of CRW algorithm in complete graphs, we
can deduce that the time and message complexities are of the order O(n) and O(n log(n)),
respectively.
Proposition III.3. In the Erd¨os-Renyi model, the average time and message complexities of TCM
algorithm are of the orders O(
p
n log(n)) and O(n log(n)), respectively.
Proof. Suppose that the token IDi is in random walk mode. In each step, it visits each node
with probability p×E{1/(d′
l+1)} ≥1/(n−2+1/p) ≈1/(n−1) for large enough n. Intuitively,
we still have the same bounds on the probabilities Pr{Tcoal(IDi) > t}, 2 ≤i ≤n. By the same
arguments for the case of complete graphs, the time and message complexities are of the order
O(
p
n log(n)) and O(n log(n)), respectively.
E. Time complexity of TCM algorithm on torus networks
In this part, we give a naive analysis on the time complexity of TCM algorithm in torus
networks. We will show that the average running time of the algorithm is of the order
O(n log(log(n))). To obtain the bound, we ﬁrst need to review two lemmas about single random
walks.


## Page 12


12
Figure 4. After k steps, the region of visited nodes by token ID1, is approximately a disc with radius of r =
p
k/n log(k).
The visited nodes are shown by dashed patterns. The average time to hit the disc by a token (depicted by black color) is
Θ(n log(r−1)).
Lemma III.2.
[21] Consider a √n × √n discrete torus. Let Thit be the average time for a
single random walk to hit the set of nodes contained in a disc of radius r < R/2 around a
point x starting from the boundary of a disc of radius R around x. Then, we have: E{Thit} =
Θ(n log(r−1)).
Lemma III.3. [22] Let Vk be the number of nodes visited by a single random walk on Z2 after
k steps. Then, we have: E{Vk} =
πk
log k and variance Var(Vk) = O(k2 log(log(k))
log(k)3 ).
Proposition III.4. In torus networks, the average time complexity of the TCM algorithm is of
the order O(n log(log(n))).
Proof. Consider the token ID1. From Lemma III.3,
πk
log k number of nodes are visited on average
by token ID1 after k steps. To simplify the analysis, we approximate the region of visited nodes
with a disc of radius
p
k/n log k on a unit torus (see Fig. 4). Hence, after k = βn steps, radius
of the disc would be
p
β/ log(βn) where β << 1. Furthermore, any other token IDi (i ≥2)
walks randomly or follows another token on a trajectory of a random walk. Hence, from Lemma
III.2, token IDi hits the disc after Θ(n log(log(n))) average time units if it does not coalesce
with any other token during this time interval. Following that, at most 2n time slots are required
to reach token ID1. Therefore, the time complexity is of the order O(n log(log(n))).
IV. ROBUSTNESS ANALYSIS
In this section, we study the robustness of CRW and TCM algorithms. In the literature of
distributed systems, identifying robust algorithms is done mostly from a qualitative rather than
quantitative perspective. For instance, there is a common belief that gossip algorithms have a
robust structure against network perturbations such as node failures or time-varying topologies
[9]. Nevertheless, this advantage is achieved by huge time and message complexities [9].
To the best of our knowledge, there exist a few works [23], [24] on analyzing the robustness
of distributed function computation (DCF) algorithms. One of the main challenges is that it is
difﬁcult to devise a well deﬁned robustness metric. Despite the challenges, there exist some


## Page 13


13
methodologies for deﬁning a robustness metric in a computing system [25], [26]. Here, we
follow the same approach in these methodologies. To do so, three steps should be taken:
1) First, a metric should be considered for the system performance. In our case, we
consider it as the probability of successful computation at the end of the algorithm, i.e.
Pr{vi = f(v0
1, · · · , v0
n), ∀i ∈{1, · · · , n}, node i has not failed} where vi is the output of node
i. Note that the correct result is a function of initial values of whole nodes.
2) In the second step, network perturbations should be modelled. In the CRW and TCM
algorithms, the ﬁnal result may be corrupted if an active node fails. Thus, studying the impact
of such event on the robustness of these algorithms is quite important. In order to model node
failures, we assume that each node may crash according to exponential distribution with rate λ.
Therefore, the average lifespan of a node is 1/λ. As a result, at most n × (1 −e−λE{Trun(n)})
number of nodes fail on average. We assume that the expected number of crashed nodes during
the execution of the algorithm is at most a small fraction of network size, i.e. λE{Trun(n)} <
−log(1 −α) ≈α where α << 1.
3) At the end, it should be identiﬁed how much perturbation the algorithm can tolerate such
that the performance metric remains in an acceptable region. For this purpose, we deﬁne the
following robustness metric.
Deﬁnition IV.1. The robustness metric, r(ϵ), is deﬁned by the following equation:
r(ϵ) ≜max λ0
s.t. Pr{vi = f(v0
1, · · · , v0
n), ∀i ∈{1, · · ·, n}, node i has not failed|λ = λ0} ≥1 −ϵ,
(10)
Intuitively, the robustness metric shows maximum failure rate which an algorithm can tolerate
such that the probability of successful computation is greater than a desired threshold, 1 −ϵ. In
order to execute CRW and TCM algorithms in the presence of node failure, it is assumed that
each token chooses a random neighbor node for the next clock tick, if the contacting node at
the current moment has been failed.
A. Robustness of CRW algorithm in complete graphs
We ﬁrst derive the probability that node i is active at time t, i.e. Pr{ζi(t) = 1}.
Lemma IV.1. In the non-failure scenario, node i is active at time t with probability Pr{ζi(t) =
1} = 1/(t + 1).
Proof. We use the mean ﬁeld theorem to calculate the probability p(t) = Pr{ζi(t) = 1} (for more
on mean ﬁeld theorem, see [27]). Due to symmetry property of the complete graphs, each node
is active at time t with the same probability p(t). Thus, the portion of active nodes will decrease
with rate −p2(t). Therefore, we have: dp(t)
dt
= −p2(t). By solving the differential equation and
considering the fact that p(0) = 1, we have: p(t) = 1/(t + 1) and E{c(t)} = n/(t + 1) where
c(t) =
n
X
i=1
ζi(t) is the the number of active nodes at time t.
Lemma IV.2. In the CRW algorithm, the probability of successful computation is greater than
n−λn for the node failure rate λ < α/E{Trun(n)}.


## Page 14


14
Proof. The function computation is successful iff none of active nodes fail up to time Trun(n).6
Let F[t0,t1) be the event that none of active nodes fails in the time interval [t0, t1). Thus, the
probability Psucc(t) ≜Pr{F[0,t)}, (t < Trun(n)), satisﬁes the following equation:
Psucc(t + dt) = Psucc(t) × Pr{F[t,t+dt)|F[0,t)},
= Psucc(t) × Ec(t)

Pr{F[t,t+dt)|c(t), F[0,t)}
	
,
=a Psucc(t) × Ec(t){e−λc(t)dt},
= Psucc(t) × Ec(t){1 −λc(t)dt} + O(dt2),
=b Psucc(t) × (1 −λn
t + 1dt).
(a) From property of exponential distribution considered in modelling node failures.
(b) We assume that E{c(t)} ≈n/(t + 1) is not affected by missing a small fraction of nodes.
Therefore, we have:
dPsucc(t)
dt
= −Psucc(t) λn
t + 1.
(11)
By solving the above differential equation, we have: Psucc(t) = (t + 1)−λn. Hence, we can
obtain a lower bound on the probability of successful computation, Psucc, as follows:
Psucc = ETrun(n)

Psucc
 Trun(n)
	
≥(E{Trun(n)} + 1)−λn ≥n−λn.
(12)
The above inequality holds due to Jensen’s inequality and considering the fact that function
f(x) = (x + 1)−nλ, x > 0 is convex.
After some manipulations, it can be easily veriﬁed that: r(ϵ) > log((1 −ϵ)−1)/(n log(n)).
Hence, the single CRW can tolerate failure rates of order O(1/(n log(n))). But, how can
we improve the performance of this algorithm such that it tolerates failure rates of order
α/E{Trun(n)} = α/n? One effective solution is to run multiple CRWs in parallel. More
speciﬁcally, we run R instances of CRW algorithm denoted by 1, . . . , R; As a result, if an
active node fails in some instances of the CRW algorithm, it might be inactive in the other
instances and those instances survive from that node failure.
In order to run multiple instances of the algorithm, tokens carry the index of the corresponding
instance in the execution of the algorithm and can only coalesce with token of the same index.
At the end of the algorithm, nodes decide on the output of an instance which includes as many
values as possible in computing the target function. To do so, we can assume that each node i has
a count parameter size(i) which is equal to one at the beginning of the algorithm (see section
II). The sum of these count parameters is obtained alongside computing the target function of
initial values for each instance of the algorithm. Nodes decide on the output of instance with
maximum count parameter.
Lemma IV.3. To tolerate the failure rate of α/n and get the correct result with probability 1−ϵ,
the number of instances of the CRW algorithm should be greater than:
R > log(ϵ−1)nα.
(13)
6In controlled ﬂooding mechanism, the value of last active node is broadcasted to all nodes. Thus, node failures have negligible
impact on the ﬁnal result in this phase and we neglect it in our analysis.


## Page 15


15
Proof. Assuming that the multiple instances are approximately independent and considering
λ = α/n and Lemma IV.2, the probability of successful computation of the target function with
R instances of CRW algorithm is greater than:
1 −(1−n−α)R ≥1 −ϵ,
→R ≥
log(ϵ)
log(1 −n−α) ≈log(ϵ−1)nα.
(14)
Corollary IV.1. The CRW algorithm is robust against failing α fraction of nodes by running
O(nα) instances of CRW algorithm in parallel. Thus, the message complexity is of the order
O(n1+α log(n)). Since α << 1, this solution imposes low message overhead.
B. Robustness of TCM algorithm in complete graphs
To study the robustness of TCM algorithm, we ﬁrst need to obtain the average percentage of
active nodes at time t. However, deriving E{c(t)}/n for TCM algorithm in complete graphs is
not an easy task as the one for the CRW algorithm. Since it is required to compute the following
sum:
E{c(t)} = 1
n
n
X
i=1
Pr{Tcoal(IDi) > t},
(15)
where obtaining Pr{Tcoal(IDi) > t}, ∀i ∈{2, · · · , n} (or even bounds on them) is quite
challenging. In order to simplify the analysis, we consider a form of function E{c(t)}/n ≈
log2(t+ 2)/(at2 +bt+1) where a = 0.23 and b = 1.8. The reason for choosing this form is that
the average running time is of the order O(
p
n log(n)) and it can also be ﬁtted properly to the
simulation results7. According to this assumption, we can derive the probability of successful
computation by the following lemma.
Lemma IV.4. The probability of successful computation by TCM algorithm is greater than e−γnλ
in complete graphs where γ ≈4.13.
Proof. By the same arguments in the proof of Lemma IV.2, we have:
Psucc(t) = exp

−λ
Z t
0
E{c(τ)}dτ

.
(16)
Since h(t) = e−λt is convex and non-increasing and g(t) =
R t
0 E{c(τ)}dτ is concave
( d
dtE{c(t)} < 0, t > 0), the Psucc(t) = h(g(t)) is convex. Hence, we have from Jensen’s
inequality:
Psucc = ETrun(n)

Psucc
 Trun(n)
	
≥exp

−nλ
Z E{Trun(n)}
0
log2(τ + 2)
aτ 2 + bτ + 1dτ

≥e−γnλ,
(17)
where
R E{Trun(n)}
0
log2(τ+2)
aτ 2+bτ+1dτ ≤
R ∞
0
log2(τ+2)
aτ 2+bτ+1dτ = γ.
Corollary IV.2. From Lemma IV.4, we can see that r(ϵ) is at least ϵ/(γn) for a single TCM
algorithm. Similar to the CRW algorithm, we can run multiple instances of TCM algorithm in
7From simulation results, the root mean square error (RMSE) of ﬁtted function is less than 10−3 for all n ∈[100, 2500].


## Page 16


16
500
1000
1500
2000
2500
60
80
100
120
140
160
180
200
220
Number of nodes
E{Time Complexity}
 
 
simulation
the curve: 4.5√n
(a) The TCM algorithm
100
150
200
250
300
100
150
200
250
300
Number of nodes
E{Time complexity}
 
 
simulation
analysis: n
(b) The CRW algorithm
Figure 5. Average time complexities of TCM and CRW algorithms in complete graphs.
parallel to improve its robustness. In order to tolerate the failure rate of α/n, the required number
of instances running in parallel should be of the order O(1).
V. SIMULATION RESULTS
In this section, we evaluate the performances of TCM and CRW algorithms through simulation.
Simulation results are averaged over 10000 runs for both algorithms in complete graphs, torus
networks, and Erd¨os-Renyi model.
In Fig. 5, average time complexities of TCM and CRW algorithms are given for complete
graphs. In the TCM algorithm, psend is set to
1
2. As it can be seen, simulation results are
close to our analysis. Furthermore, the TCM algorithm outperforms the CRW algorithm by
a scale factor √n. For instance, for n = 256, the average time complexities of TCM and
CRW algorithms are 67 and 255 time units, respectively. Hence, the amount of improvement
is 255/67 = 3.81 ≈n/(4.5n0.5) = 3.56. In Fig. 6, the average message complexities of TCM
and CRW algorithms are depicted in complete graphs. As it can be seen, the average message
complexity of TCM algorithm is always less than half of the one for the CRW algorithm.
In order to study the effect of parameter psend on the running time of TCM algorithm, the
average time complexity is plotted versus psend for the complete graphs in Fig. 7. Intuitively,
the event horizon of token ID1 grows with a pace inversely proportional to psend. On the other
hand, the relative velocity of two tokens is approximately related to 1−psend. Thus, the average
time complexity increases as psend goes to zero or one. Furthermore, the optimal psend gets close
to 0.5 as network size increases.
In Fig. 8, we evaluate the average time and message complexities of TCM and CRW algorithms
in torus networks. We can see that TCM algorithm has at least a gain of log(n) in time complexity
and a scale factor of 2.85 in message complexity. In Fig. 9, the average time and message
complexities of TCM and CRW algorithms are depicted in Erd¨os-Renyi model. According to Fig.
9(a), the TCM algorithm has an improvement in time complexity by a factor √n. Furthermore,
the average message complexity of TCM algorithm is approximately half of the CRW algorithm.


## Page 17


17
500
1000
1500
2000
2500
0
2000
4000
6000
8000
10000
12000
Number of nodes
E{Message Complexity}
 
 
simulation
the curve: 1
2n(log(n) + 0.58)
(a) The TCM algorithm
100
150
200
250
300
600
800
1000
1200
1400
1600
1800
2000
2200
Number of nodes
E{Message Complexity}
 
 
simulation
analysis: n(log(n) + 0.58)
(b) The CRW algorithm
Figure 6. Average message complexities of TCM and CRW algorithms in complete graphs.
0.4
0.5
0.6
0.7
0.8
0.9
1
40
60
80
100
120
140
160
180
200
psend
E{Time Complexity}
 
 
n = 196
n = 400
n = 900
Figure 7. Average time complexity of TCM algorithm versus psend.
In Fig. 10, the probability of successful computation by running one instance of TCM and
CRW algorithms are depicted in the case of complete graphs. The failure rate is set to 0.05/n.
For the TCM algorithm, Psucc is approximately equal to 0.83 for different values of n in the
range [100, 400]. Besides, results from analysis are close to it by an offset of 0.001. In the case
of CRW algorithm, results from the simulation and the analysis are also close to each other. For
this algorithm, Psucc is greater than 0.74 for various values of n in the range [100, 400].
In Fig. 11(a), the message complexities of the TCM and CRW algorithms are plotted versus
failure rate in a complete graph with n = 100 nodes. The number of parallel instances is
determined such that the probability of successful computation is equal to 0.95. As it can be
seen, it is required to run a few more instances of the TCM and CRW algorithms to tolerate
higher failure rate. Furthermore, message complexity of the TCM algorithm is less than the one
for the CRW algorithm. In Fig. 11(b), the time complexities of both algorithms are given versus
failure rate. For higher failure rate, we need to run more instances of the TCM/CRW algorithm


## Page 18


18
100
200
300
400
500
600
700
800
900
0
500
1000
1500
2000
2500
Number of nodes
E{Time Complexity}
 
 
simulation (the TCM algorithm)
simulation (the CRW algorithm)
the curve: 1
3n log(n)
the curve: 3
4n
(a) Average time complexity
100
200
300
400
500
600
700
800
900
0
2000
4000
6000
8000
10000
12000
14000
Number of nodes
E{Message Complexity}
 
 
simulation (the TCM algorithm)
simulation (the CRW algorithm)
the curve: 2n log(n)
the curve: 0.7n log(n)
(b) Average message complexity
Figure 8. Average time and message complexities of TCM and CRW algorithms in torus networks.
100
150
200
250
300
0
50
100
150
200
250
300
350
400
Number of nodes
E{Time Complexity}
 
 
200
400
600
800
40
60
80
100
120
140
 
 
simulation (the TCM algorithm)
simulation (the CRW algorithm)
the curve: n
the curve: 4.5√n
(a) Average time complexity
100
150
200
250
300
200
400
600
800
1000
1200
1400
1600
1800
2000
2200
Number of nodes
E{Message Complexity}
 
 
simulation (the TCM algorithm)
simulation (the CRW algorithm)
(b) Average message complexity
Figure 9. Average time and message complexities of TCM and CRW algorithms in Erd¨os-Renyi model.
to have Psucc = 0.95. On the other hand, executing multiple instance of the algorithms improves
the time complexity. Since the target function is computed if any of the instances is terminated
successfully.
In Fig. 12, the probabilities of successful computation of the TCM and CRW algorithms are
plotted versus number of multiple instances in a complete graph with n = 400 nodes for the
failure rates λ = 0.05/n, 0.1/n. It can be seen that the analytical lower bounds in (12) and (17)
are close to simulation results. Furthermore, Psucc goes to one in all cases when 6 number of
instances are executed in parallel. Thus, the proposed solution makes both algorithms robust
against node failures by running a few number of instances in parallel as we expected from
Corollaries IV.1 and IV.2.
Studying the impact of dynamic topologies on the performance of distributed algorithms is
quite important. Here, we evaluate the performance of TCM and CRW algorithms under node
mobility. There exist different mobility models in the literature of mobile ad hoc networks [14].
In the simulations, we consider the Random Walk (RW) mobility model which is frequently


## Page 19


19
100
150
200
250
300
350
400
0.82
0.825
0.83
0.835
0.84
0.845
0.85
0.855
Number of nodes
Psucc
 
 
simulation
analysis (lower bound)
(a) The TCM algorithm
100
150
200
250
300
350
400
0.72
0.74
0.76
0.78
0.8
0.82
0.84
Number of nodes
Psucc
 
 
simulation
analysis (lower bound)
(b) The CRW algorithm
Figure 10. The probabilities of successful computation in TCM and CRW algorithms for complete graphs, R = 1.
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
x 10
−4
0
500
1000
1500
2000
2500
3000
failure rate (λ)
E{Message Complexity}
 
 
The TCM algorithm
The CRW algorithm
(a) Message complexity
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
x 10
−4
30
40
50
60
70
80
90
100
110
failure rate (λ)
E{Time Complexity}
 
 
2
4
6
8
10
x 10
−4
30
32
34
36
38
40
42
The TCM algorithm
The CRW algorithm
(b) Time complexity
Figure 11.
Average time and message complexities of TCM and CRW algorithms versus failure rate in complete graphs,
n = 100. The dashed lines represent the linear regression between message complexity and failure rate.
used in determining the protocol performance and it can mimic movements of mobile nodes
walking in an unpredictable way [14].
Initially, suppose that nodes are located randomly over a square of unit area. Let [xi(t), yi(t)]
be the location of node i at time t. In the RW mobility model, the differences x(t + h) −x(t)
and y(t + h) −y(t) are two independent normally distributed random variables with zero mean
and variance 2Dh , ∀h > 0 where D is the diffusion coefﬁcient [28]. Thus, the mean square
displacement of a node is related to the parameter D. In particular, the probability of large
displacement increases as diffusion coefﬁcient D grows. We assumed that if a node reaches the
boundary of simulated area, it will be bounced off the boundary according to the same angle.
Furthermore, two nodes are neighbor if the distance between them is less than a ﬁxed transmission
range. The transmission range is set to a value such that the graph remains connected with high
probability for the static case, i.e. D = 0 [29].
In the TCM algorithm, we assume that each node i registers the UID of the node that the token
memory(i) passed to it. Whenever an active node should send a token to a node which is not in


## Page 20


20
1
1.5
2
2.5
3
3.5
4
4.5
5
5.5
6
0.5
0.55
0.6
0.65
0.7
0.75
0.8
0.85
0.9
0.95
1
Number of instances (R)
Psucc
 
 
simulation (the TCM algorithm)
simulation (the CRW algorithm)
analytical lower bound (the TCM algorithm)
analytcial lower bound (the CRW algorithm)
failure rate λ = 0.1/n
failure rate λ = 0.05/n
Figure 12. The probability of successful computation versus number of multiple instances in complete graphs, n = 400.
10
−6
10
−5
10
−4
10
−3
10
−2
60
70
80
90
100
110
120
130
Diﬀusion Coeﬃcient (D)
E{Time Complexity}
 
 
The TCM algorithm
The CRW algorithm
(a) Time complexity
10
−6
10
−5
10
−4
10
−3
10
−2
350
400
450
500
550
600
650
Diﬀusion Coeﬃcient (D)
E{Message Complexity}
 
 
The TCM algorithm
The CRW algorithm
(b) Message complexity
Figure 13. Average time and message complexities of TCM and CRW algorithms versus diffusion coefﬁcient D in a network
with n = 100 nodes which are deployed in a square of unit area. The transmission range is set to 0.18.
its transmission range any more, it will pass its token to a random neighbor node. In Fig. 13, the
time and message complexities of TCM and CRW algorithms are depicted versus the parameter D
in a network with n = 100 nodes. It is noteworthy that both algorithms can compute the class of
target functions deﬁned in Lemma II.1 successfully even in high mobility networks. Furthermore,
the time and message complexities of TCM algorithm increases as the parameter D grows while
node mobility improves the performance of CRW algorithm. In fact, higher mobility weakens
the advantage of chasing mechanism. On the other hand, it gives an opportunity to a completely
randomized solution, i.e. the CRW algorithm, to reduce the coalescing time of distant tokens.
Nevertheless, simulation results show that the TCM algorithm outperforms the CRW algorithm
in both time and message complexities.


## Page 21


21
VI. CONCLUSIONS
In this paper, we proposed the TCM algorithm to compute a wide class of target functions
(such as sum, average, min/max, XOR) in a distributed manner. In complete graph and Erd¨os-
Renyi model, we showed that it reduces running time at least by factor
p
n/ log(n) with respect
to completely randomized solution, i.e. the CRW algorithm, and there is at least a factor of
log(n)/ log(log(n)) improvement in torus networks. We deﬁned a robustness metric to study the
impact of node failures on the performance of CRW and TCM algorithms. The TCM and CRW
algorithms can tolerate the failure rate of α/n by running O(nα) and O(1) instances in parallel,
respectively. Furthermore, simulation results showed that both algorithm can compute the target
functions successfully even in high mobility conditions.
VII. APPENDIX A
Proof of Lemma III.1:
The pdf of |EH1(k)| can be approximated with Gaussian distribution N(µk, σk) where µk =
n −n(1 −1/n)k and σ2
k = n2(1 −1/n)(1 −2/n)k + n(1 −1/n)k −n2(1 −1/n)2k [29]. After
some manipulations, we have:
Pr{|EH1(2k)| ≤E{|EH1(k)|}} ≤1
2e−(µk−µ2k)2/2σ2
2k ≤e−n/4−kη.
(18)
where η ≥0.05. Hence, the size of the set EH1(2k), is greater than E{|EH1(k)|} with probability
at least 1 −e−n/4−kη.
VIII. APPENDIX B
Proof of Theorem III.2:
Consider token IDi (i > 1). Let xi
k be the node visited by token IDi at k-th step and
Si
k = {xi
1, · · · , xi
k} be the history of the corresponding walk. We deﬁne the walk taken by token
IDi as weakly self-avoiding walk, provided that:
Pr{xi
k+1|Si
k}
(
= αk
xi
k+1 ̸∈Si
k,
≤αk
xi
k+1 ∈Si
k,
(19)
for some αk where αk ≥
1
n−1. Thus, in a weakly self-avoiding walk, token IDi visits new nodes
with higher probability than the visited nodes.
Lemma VIII.1. In the TCM algorithm, the path traced by token IDi (i > 1) is a weakly
self-avoiding walk.
Proof. Suppose that the token IDi enters a node xi
k visited by some other token with higher UID.
Let IDi′ be the maximum UID, node xi
k has seen so far. Furthremore, assume that token IDi′ is
in k′ steps and has visited node xi
k in j-th step for the last time, i.e. j = maxω≤k′ ω s.t. xi′
ω = xi
k.
We denote the chasing and random walk modes of token IDi by chasei and RWi, respectively.
Now, for a given history Si
k, we have:
Pr{xi
k+1 = a|Si
k} =
i−1
X
i′=1
h
k′
X
j=1
Pr{xi
k+1 = a|xi′
j = xi
k, chasei, Si
k} × Pr{xi′
j = xi
k, chasei|Si
k}
i
+ Pr{xi
k+1 = a|RWi, Si
k} × Pr{RWi|Si
k}.
(20)


## Page 22


22
i
ID
i
ID ′
i
kx
′
′
i
jx
′
i
jx
′
+1
i
jx
′
−1
i
lx
i
kx
1
−
Figure 14. Token IDi visits node xi
k = xi′
j . Thus, token IDi will not visit nodes {xi
l, · · · , xi
k} in the next step. Tokens are
depicted by black squares.
Suppose that token IDi was in l-th step when token IDi′ was leaving node xi′
j (see Fig.
14). We prove that token IDi will not visit nodes in the set {xi
l, · · · , xi
k} in the next step. By
contradiction, assume that there exists l ≤p ≤k where xi
p = xi′
j+1. However, we have:
∀ω1 ∈{p, · · · , k}, ∃ω2 ∈{j + 1, · · · , k′}, s.t. xi
ω1 = xi′
ω2,
(21)
due to the fact that token IDi is chasing token IDi′. For ω1 = k, the above equation asserts that
token IDi′ revisited node xi
k in some step later than j which is contradiction.
We know that token IDi′ was eventually in the random walk mode in j-th step. Hence, each
node in the set {1, · · · , n}\{xi
l, · · · , xi
k} is selected with probability 1/(n −|{xi
l, · · · , xi
k}|) in
the k + 1-th step. Consequently, we have:
Pr{xi
k+1 = a|xi′
j = xi
k, chasei, Si
k} ≥Pr{xi
k+1 = b|xi′
j = xi
k, chasei, Si
k}
∀j, k, ∀a, b ∈{1, · · · , n}, a ̸∈Si
k, b ∈Si
k.
(22)
From (20) and (22), it can be concluded that:
Pr{xi
k+1 = a|Si
k} ≥Pr{xi
k+1 = b|Si
k}, ∀a, b ∈{1, · · · , n}, a ̸∈Si
k, b ∈Si
k.
(23)
Thus, the proof is complete.
Assume that if token IDi coalesces with token IDj (where IDj > IDi), it virtually sticks
to token IDj. Now, if token IDj meets another token, say IDk with higher UID, token IDj
and all tokens attached to it, stick to token IDk. This process continues until token IDi hits the
event horizon of ID1 by itself or another token. We denote the time for token IDi to hit the
event horizon of token ID1 by TEH1(IDi). Furthermore, let EHi(t) be the set of nodes visited
by token IDi up to time t.
Token ID1 takes steps in the network according to a Poisson process with rate 1/2 (assuming
that psend = 1/2). At each step, it chooses one of nodes except its current node with probability
1/(n−1). Thus, each node (excluding the initial node having token ID1) is not visited by token


## Page 23


23
ID1 up to time t with probability e−t/2(n−1) independently from other nodes. Hence, the pdf of
the number of visited nodes at time t is:
Pr{|EH1(t)| = r} =
n −1
r −1

(1 −e−t/2(n−1))r−1 × (e−t/2(n−1))n−r,
(24)
for 1 ≤r ≤n −1.
Lemma VIII.2. We have the following probabilistic bound on the number of visited nodes by
token ID1 at time 2t:
Pr{|EH1(2t)| ≤E{|EH1(t)|}} ≤e−α0t, t ≤2n,
(25)
where α0 = (1 −log(2))/4.
Proof. From (24) and the proposed upper bound for binomial distribution in [30], we have:
Pr{|EH1(2t)| ≤E{|EH1(t)|}} ≤e−nD,
(26)
where D = a log(a/b) + (1 −a) log((1 −a)/(1 −b)), a = 1 −e−t/2(n−1) and b = 1 −e−t/(n−1).
Besides, we have:
nD = t/2e−t/2(n−1) −(n −1)(1 −e−t/2(n−1))(1 + e−t/2(n−1))
> t/2(1 −log(2)) + t2(log(2) −1)/(8n).
(27)
From above equation, it can be easily seen that nD > t(1 −log(2))/4 for t ≤2n. Therefore,
the proof is complete.
Lemma VIII.3. Let Ni(t0, t0 + 2t) be the number of steps taken by token IDi in time interval
[t0, t0 + 2t]. Then, we have the following bound:
Pr{Ni(t0, t0 + 2t) < ⌊t/2⌋} ≤e−α1t,
(28)
where α1 = log(
p
e/2).
Proof. The random variable Ni(t0, t0+2t) is a Poisson process with rate at least λ2t = 2t×1/2 =
t. Thus, we have from the Chernoff bound:
Pr{Ni(t0, t0 + 2t) ≤⌊t/2⌋} ≤
⌊t/2⌋
X
i=0
e−λ2t(λ2t)i
i!
≤e−t (et)t/2
(t/2)t/2 = (2/e)t/2.
(29)
The proof is complete.
Remark VIII.1. By the same arguments in Lemma VIII.3, it can be shown that: Pr{Ni(t0, t0 +
t) > 2t} ≤e−α2t where α2 = log (4/e).
Given a time t, we say that the event Ei(t) occurs if |EH1(t)\EHi(t)| ≥1/8√n log n. Let


## Page 24


24
E(t) = T
i
Ei(t) and deﬁne t⋆= √n log n. We have:
Pr

Ec(t⋆)
	
≤a
n
X
i=2
Pr{Ec
i (t⋆)} ≤(n −1)E
(
Ni(0,t⋆)
X
j=|EH1(t⋆)|−1/8√n log n
Ni(0, t⋆)
j

P j
EH1(t⋆)P Ni(0,t⋆)−j
EHc
1(t⋆)
)
≤b E
(
(n −1)
Ni(0,t⋆)
X
j=|EH1(t⋆)|−1/8√n log n
Ni(0, t⋆)
j
 |EH1(t⋆)|
n −Ni(0, t⋆)
j
)
≤c (n −1)
 
⌈2√n log n⌉
X
j=⌊1/8√n log n⌋
2√n log n
j
 1/4√n log n
n −2√n log n
j
+ e−α0
√n log n/2 + e−α2
√n log n
!
≤d
1
√n log n.
(30)
(a) The ﬁrst sum is given according to the union bound. The second sum is greater than the
probability of having |EH1(t⋆)∩EHi(t⋆)| ≥j where PEH1(t⋆) and PEHc
1(t⋆) are the probabilities
of choosing a node from the set EH1(t⋆) and {1, · · · , n}\EH1(t⋆), respectively.
(b) From Lemma VIII.1, the path traced by token IDi (i > 1) is a weakly self-avoiding walk.
Thus, we have: PEH1(t⋆) ≤
|EH1(t⋆)|
n−Ni(0,t⋆).
(c) The sum has greater value for larger |Ni(0, t)| and smaller |EH1(t)|. We can obtain this
inequality by bounding the probability Pr{|EH1(t⋆)| < 1/4√n log n} and Pr{Ni(0, t⋆) >
2√n log n} from Lemma VIII.2 and Remark VIII.1, respectively.
(d) From Strling’s approximation, the probability is in the order of O(e−log n√n log n). Thus, it is
less than 1/√n log n for large enough n.
Lemma VIII.4. Assume that the event E(t⋆) occurs. Then, the probability of not hitting the
event horizon of token ID1 by token IDi after t⋆+ 2t is less than the following:
Pr{TEH1(IDi) > t⋆+ 2t|E(t⋆)} ≤e−1
16
√
log n/nt + e−α1t.
(31)
Proof. Suppose that the event E(t⋆) occurs at time t⋆. Thus, the size of the the set
EH1(t)\EHi(t), t > t⋆, will be greater than 1/8
p
n log(n) as far as token IDi does not hit it.
Hence, the probability of not hitting the event horizon of ID1 in time interval [t⋆, t⋆+ 2t] is
less than (1 −1/8√n log n/n)Ni(t⋆,t⋆+2t). By bounding Ni(t⋆, t⋆+ 2t) from below (see Lemma
VIII.3), we have:
Pr{TEH1(IDi) > t⋆+ 2t|E(t⋆)} ≤Pr{Ni(t⋆, t⋆+ 2t) > ⌊t/2⌋} × (1 −1/8
p
n log n/n)t/2
+ Pr{Ni(t⋆, t⋆+ 2t) ≤⌊t/2⌋} × 1,
≤e−1
16
√
log n/nt + e−α1t.
(32)
Lemma VIII.5. Suppose that token IDi hits the event horizon of token ID1 at time t. Then, it
will coalesce with token ID1 in next 3t time units with probability greater than 1−(e−α3t+e−α4t)
where α3 = 1/36 and α4 = log(2/√e).


## Page 25


25
Proof. In worst case scenario, the event horizon of token ID1 is a line with length N1(0, t) and
token IDi hits end of the line at time t. Thus, token IDi reaches token ID1 at time t′ given in
the following equation:
Ni(t, t′) = N1(0, t) + N1(t, t′).
(33)
Let us deﬁne random variable Y (t′) = Ni(t, t′) −N1(t, t′), which is the difference of two
independent Poisson random variables Ni(t, t′) and N1(t, t′) with rates (t′ −t) and (t′ −t)/2,
respectively. Hence, the random variable Y (t′) has Skellam distribution and we have:
Pr{Y (t′) < N1(0, t)} ≤e−(N1(0,t)−1/2(t′−t))2
3(t′−t)
.
(34)
Since
token
ID1
takes
at
most
⌈t⌉
steps
in
time
interval
[0, t]
with
probability
⌈t⌉
X
i=0
e−t/2(t/2)i
i!
≤e−α4t, we have:
Pr{Y (4t) < N1(0, t)} ≤e−α3t + e−α4t.
(35)
Corollary VIII.1. From Lemmas VIII.4 and VIII.5, we have:
Pr{Tcoal(IDi) > 4t⋆+ 8t|E(t⋆)} ≤e−1
16
√
log n/nt + e−α1t + e−α3t + e−α4t,
≤e−1
16
√
log n/nt + 3e−α3t.
(36)
Now, we can obtain an upper bound on the average time complexity:
E{Trun(n)} = E{Trun(n)|E(t⋆)} Pr{E(t⋆)} + E{Trun(n)|Ec(t⋆)} Pr{Ec(t⋆)},
≤a E{Trun(n)|E(t⋆)} + (4n log(n) + 2t⋆) ×
1
√n log n,
=
Z ∞
0
Pr{Trun(n) > τ|E(t⋆)}dτ + 4
p
n log n + 2,
≤b
Z ∞
0
min(1,
X
i∈{2,··· ,n}
Pr{Tcoal(IDi) > τ|E(t⋆)})dτ + 4
p
n log n + 2,
≤c 4t⋆+
Z ∞
0
min(1, (n −1) × (e−
1
128
√
log n/nτ + 3e−α3τ/8))dτ + 4
p
n log n + 2,
≤d
Z 128√
n log(n)
0
1dt +
Z ∞
128√
n log(n)
n × (e−
1
128
√
log n/nτ + 3e−α3τ/8)dτ + 8
p
n log n + 2,
≤128
p
n log(n) + 128
p
n/ log n + 24n
α3
e−16α3
√n log n + 8
p
n log n + 2 = O(
p
n log n).
(37)
(a) Regardless of the event E(t⋆), token ID1 covers the complete graph in t⋆+ 2n log(n)
time units on average [13]. Thus, any token IDi (i > 1) will coalesce with it in at most
2 × (2n log n + t⋆) time units on average. Hence, we have: E{Trun(n)|Ec(t⋆)} ≤4n log n + 2t⋆.
Besides, we know that Pr{Ec(t⋆)} ≤1/√n log n according to (30).


## Page 26


26
(b) According to union bound.
(c) From Corollary VIII.1.
(d) From the fact that ne−
1
128
√
log n/nt ≥1 for t ≤128√n log n.
REFERENCES
[1] J. Almodovar and J. Nelson, “A gossip-based distributed processing algorithm for multiple transmitter localization,” in
Statistical Signal Processing Workshop (SSP), 2012 IEEE, 2012, pp. 169–172.
[2] A. Chiuso, F. Fagnani, L. Schenato, and S. Zampieri, “Gossip algorithms for simultaneous distributed estimation and
classiﬁcation in sensor networks,” Selected Topics in Signal Processing, IEEE Journal of, vol. 5, no. 4, pp. 691–706, 2011.
[3] L. Necchi, A. Bonivento, L. Lavagno, A. Sangiovanni-Vincentelli, and L. Vanzago, “E2rina: an energy efﬁcient and reliable
in-network aggregation for clustered wireless sensor networks,” in Wireless Communications and Networking Conference,
2007.WCNC 2007. IEEE, 2007, pp. 3364–3369.
[4] G. Mateos, J. A. Bazerque, and G. B. Giannakis, “Distributed sparse linear regression,” Signal Processing, IEEE
Transactions on, vol. 58, no. 10, pp. 5262–5276, 2010.
[5] L. Hyang-Won, E. Modiano, and B. Long, “Distributed throughput maximization in wireless networks via random power
allocation,” Mobile Computing, IEEE Transactions on, vol. 11, no. 4, pp. 577–590, 2012.
[6] A. Nedic and A. Ozdaglar, “Distributed subgradient methods for multi-agent optimization,” Automatic Control, IEEE
Transactions on, vol. 54, no. 1, pp. 48–61, 2009.
[7] N. Lynch, Distributed algorithms.
Morgan Kaufmann, 1996.
[8] R. Sappidi, C. Rosenberg, and A. Girard, “Computing statistical functions in wired networks,” Selected Areas in
Communications, IEEE Journal on, vol. 31, no. 4, pp. 731–742, 2013.
[9] A. Dimakis, S. Kar, J. Moura, M. Rabbat, and A. Scaglione, “Gossip algorithms for distributed signal processing,”
Proceedings of the IEEE, vol. 98, no. 11, pp. 1847–1864, 2010.
[10] S. Boyd, A. Ghosh, B. Prabhakar, and D. Shah, “Randomized gossip algorithms,” Information Theory, IEEE Transactions
on, vol. 52, no. 6, pp. 2508–2530, 2006.
[11] O. Ayaso, D. Shah, and M. Dahleh, “Information theoretic bounds for distributed computation over networks of point-to-
point channels,” Information Theory, IEEE Transactions on, vol. 56, no. 12, pp. 6020–6039, 2010.
[12] V. Saligrama and M. Alanyali, “A token-based approach for distributed computation in sensor networks,” Selected Topics
in Signal Processing, IEEE Journal of, vol. 5, no. 4, pp. 817–832, 2011.
[13] C. Cooper, R. Elsasser, H. Ono, and T. Radzik, “Coalescing random walks and voting on connected graphs,” SIAM Journal
on Discrete Mathematics, vol. 27, no. 4, pp. 1748–1758, 2013.
[14] T. Camp, J. Boleng, and V. Davies, “A survey of mobility models for ad hoc network research,” Wireless communications
and mobile computing, vol. 2, no. 5, pp. 483–502, 2002.
[15] N. L. Johnson and S. Kotz, Urn models and their application: an approach to modern discrete probability theory.
Wiley
New York, 1977.
[16] D. Mosk-Aoyama and D. Shah, “Fast distributed algorithms for computing separable functions,” Information Theory, IEEE
Transactions on, vol. 54, no. 7, pp. 2997–3007, 2008.
[17] S. Tavar´e, “Line-of-descent and genealogical processes, and their applications in population genetics models,” Theoretical
population biology, vol. 26, no. 2, pp. 119–164, 1984.
[18] F. Benezit, P. Thiran, and M. Vetterli, “The distributed multiple voting problem,” Selected Topics in Signal Processing,
IEEE Journal of, vol. 5, no. 4, pp. 791–804, 2011.
[19] M. E. Newman, “2 random graphs as models of networks,” Handbook of graphs and networks: From the genome to the
internet, 2006.
[20] P. Erd˝os and A. R´enyi, “On the evolution of random graphs,” Magyar Tud. Akad. Mat. Kutat´o Int. K¨ozl, vol. 5, pp. 17–61,
1960.
[21] A. Dembo, Y. Peres, J. Rosen, and O. Zeitouni, “Cover times for brownian motion and random walks in two dimensions,”
Annals of mathematics, pp. 433–464, 2004.
[22] A. Dvoretzky and P. Erd¨os, “Some problems on random walk in space,” in Proc. 2nd Berkeley Symp, 1951, pp. 353–367.
[23] V. Gupta, C. Langbort, and R. M. Murray, “On the robustness of distributed algorithms,” in Decision and Control, 2006
45th IEEE Conference on.
IEEE, 2006, pp. 3473–3478.
[24] H. J. LeBlanc, H. Zhang, X. Koutsoukos, and S. Sundaram, “Resilient asymptotic consensus in robust networks,” Selected
Areas in Communications, IEEE Journal on, vol. 31, no. 4, pp. 766–781, 2013.
[25] S. Ali, A. A. Maciejewski, H. J. Siegel, and J.-K. Kim, “Measuring the robustness of a resource allocation,” Parallel and
Distributed Systems, IEEE Transactions on, vol. 15, no. 7, pp. 630–641, 2004.
[26] V. Shestak, J. Smith, A. A. Maciejewski, and H. J. Siegel, “Stochastic robustness metric and its use for static resource
allocations,” Journal of Parallel and Distributed Computing, vol. 68, no. 8, pp. 1157–1173, 2008.
[27] H. Takayasu and A. Tretyakov, “Extinction, survival, and dynamical phase transition of branching annihilating random
walk,” Physical review letters, vol. 68, no. 20, pp. 3060–3063, 1992.


## Page 27


27
[28] R. Groenevelt, E. Altman, and P. Nain, “Relaying in mobile ad hoc networks: The brownian motion mobility model,”
Wireless Networks, vol. 12, no. 5, pp. 561–571, 2006.
[29] D. Shah, Gossip algorithms.
Now Publishers Inc., 2009.
[29]
H.-K. Hwang and S. Janson, “Local limit theorems for ﬁnite and inﬁnite urn models,” The Annals of Probability, pp.
992-1022, 2008.
[30] R. Arratia and L. Gordon, “Tutorial on large deviations for the binomial distribution,” Bulletin of mathematical biology,
vol. 51, no. 1, pp. 125-131, 1989.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1703_08831v1_token_based_function_computation_with_memory
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2017/1703_08831V1_TOKEN_BASED_FUNCTION_COMPUTATION_WITH_MEMORY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

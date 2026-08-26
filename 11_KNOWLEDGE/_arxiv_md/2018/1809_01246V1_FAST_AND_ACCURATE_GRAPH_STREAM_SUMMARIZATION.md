---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1809.01246v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1809.01246v1_Fast_and_Accurate_Graph_Stream_Summarization

> Source: 1809.01246v1_Fast_and_Accurate_Graph_Stream_Summarization.pdf

> Pages: 14

---


## Page 1


Fast and Accurate Graph Stream Summarization
Xiangyang Gou, Lei Zou, Chenxingyu Zhao, Tong Yang
Peking University, China
Abstract—A graph stream is a continuous sequence of data
items, in which each item indicates an edge, including its two end-
points and edge weight. It forms a dynamic graph that changes
with every item in the stream. Graph streams play important
roles in cyber security, social networks, cloud troubleshooting
systems and other ﬁelds. Due to the vast volume and high update
speed of graph streams, traditional data structures for graph
storage such as the adjacency matrix and the adjacency list
are no longer sufﬁcient. However, prior art of graph stream
summarization, like CM sketches, gSketches, TCM and gMatrix,
either supports limited kinds of queries or suffers from poor
accuracy of query results. In this paper, we propose a novel
Graph Stream Sketch (GSS for short) to summarize the graph
streams, which has the linear space cost (O(|E|), E is the edge
set of the graph) and the constant update time complexity (O(1))
and supports all kinds of queries over graph streams with the
controllable errors. Both theoretical analysis and experiment
results conﬁrm the superiority of our solution with regard to
the time/space complexity and query results’ precision compared
with the state-of-the-art.
Index Terms—graph, data stream, sketch, approximate query
I. INTRODUCTION
A. Background and Motivations
In the era of big data, data streams propose some technique
challenges for existing systems. Furthermore, the traditional
data stream is modeled as a sequence of isolated items,
and the connections between the items are rarely considered.
However, in many data stream applications, the connections
often play important roles in data analysis, such as ﬁnding
malicious attacks in the network trafﬁc data, mining news
spreading paths among the social network. In these cases
the data is organized as graph streams. A graph stream is
an unbounded sequence of items, in which each item is a
vector with at least three ﬁelds (denoted by (⟨s, d⟩, w)), where
⟨s, d⟩represents an edge between nodes s and d, and w is the
edge weight. These data items together form a dynamic graph
that changes continuously and we call it streaming graph for
convenience. Below we discuss three examples to demonstrate
the usefulness of streaming graph problems.
Use case 1: Network trafﬁc. The network trafﬁc can be seen
as a large dynamic graph, where each edge indicates the
communication between two IP addresses. With the arrival
of packets in the network, the network trafﬁc graph changes
rapidly and constantly. In the network trafﬁc graph, various
kinds of queries are needed, like performing node queries to
ﬁnd malicious attackers, or subgraph queries to locate certain
topology structures in the dynamic networks.
Use case 2: Social networks. In a social network, the in-
teractions among the users can form a graph. The edges
between different nodes may be weighted by the frequencies of
interactions. In such a graph, queries like ﬁnding the potential
friends of a user and tracking the spreading path of a piece of
news are often needed.
Use case 3: Troubleshooting in data centers. Cloud systems
may need to analyze communication log stream to perform
real time troubleshooting. In this situation the graph stream is
the sequence of communication log entries where each entry
is a description of a communication from a source machine
to a destination machine. In such a graph, we may perform
traversal query to ﬁnd out if massages created by a certain
application on a source machine can reach a destination ma-
chine, or perform edge query to ﬁnd the detailed information
of a communication log.
These streaming graphs are very large and change fast. For
example, in Twitter, there are about 100 million user login
data, with 500 million tweets posted per day. For another
example, in large ISP or data centers [1], there could be mil-
lions of packets every second in each link. The large volume
and high dynamicity make it hard to store the graph streams
efﬁciently with traditional data structures like adjacency lists
or adjacency matrices. In the context of graph streams, there
are two requirements for designing a new data structure : (1)
the linear space cost (2) the constant update time. To meet
these two requirements, we can either apply approximated
query data structures for data streams, like the CM sketch [2],
the CU sketch [3] and other sketches [4], [5], or use specialized
graph summarization techniques such as gSketches [6], TCM
[7] and gMatrix [8]. However, existing solutions either support
limited query types or have poor query accuracy. For example,
CM sketches and gSketches fail to answer queries involved
with topology like reachability queries, successor queries and
so on. Though TCM and gMatrix can support these queries,
they have poor accuracy. More details about the related work
are given in Section II. In this paper, we design a novel
data structure–Graph Stream Sketch (GSS for short), which
can support all kinds of queries over streaming graphs with
controllable errors in query results. Both theoretical analysis
and experiment results show that the accuracy of our method
outperforms state-of-the-art by orders of magnitudes.
B. Our Solution
In this paper we propose GSS, which is an approximate
query data structure for graph streams with linear memory
usage, high update speed, high accuracy and supports all kinds
of graph queries and algorithms like [9]–[11]. GSS can also
be used in exiting distributed graph systems [12]–[15]
Like TCM, GSS uses a hash function H(·) to compress the
streaming graph G into a smaller graph Gh which is named a
graph sketch. Each node v in G is mapped into a hash value
arXiv:1809.01246v1  [cs.DS]  4 Sep 2018


## Page 2


H(v). Nodes with the same hash value are combined into
one node in Gh, and the edges connected to them are also
aggregated. An example of the graph stream and the graph
sketch can be referred in Fig.1 and Fig.2. The compression
rate can be controlled by the size of the value range of H(·),
which we represent with M. The higher the compression rate
is, the lower the accuracy is, as more nodes and edges will be
combined.
Different from TCM which uses an adjacency matrix to
store the graph sketch Gh, GSS uses a novel data structure
to store it. This data structure is specially designed for sparse
graphs and can store a much bigger graph sketch with the same
space. As the graph is sparse, the number of nodes is large, but
each node is connected to few edges. Therefore, different from
adjacency matrix which stores edges with the same source
node / destination node in one row / column, we store edges
with different source nodes / destination nodes in the one row
/ column, and distinguish them with ﬁngerprints. Each edge in
the graph sketch is mapped to a bucket in the matrix depending
on its endpoints, and marked with a ﬁngerprint pair. If the
bucket it is mapped is already occupied by other edges, we
store this edge in a buffer B, which is composed of adjacency
lists. With a m × m matrix we can represent a graph sketch
with at most m × F nodes in GSS, where F is the size of the
value range of the ﬁngerprint (for example, a 16-bit ﬁngerprint
has F = 65536). On the other hand, the adjacency matrix can
only store a a graph sketch with at most m nodes. With a
much larger graph sketch, the accuracy is also much higher
compared to TCM.
In GSS, the memory cost and update speed are greatly
inﬂuenced by the size of the buffer B. As the buffer takes
additional memory, and update speed in an adjacency list is
linear with its size. In order to restrict its size, we propose a
technique called square hashing. In this technique each edge is
mapped to multiple buckets, and stored in the ﬁrst empty one
among them. This enlarges the chance that an edge ﬁnds an
empty bucket. Besides, a few nodes in a sparse graph may still
have very high degrees. If one node emits a lot of edges, these
edges have high probability to evict each other when stored
in one row. To solve this problem, In square hashing edges
with source node v are no longer mapped to one row, but r
rows, sharing memory with other source nodes. The higher
degree a node has, the more buckets it may take. It is similar
in the view of columns and destination nodes. This helps to
ease the congestion brought by the skewness in node degrees.
Experiments show that after this modiﬁcation the buffer only
stores less than 0.01% of the edges in the graph stream.
The key contributions of this paper are as follows:
1) We propose GSS, a novel data structure for graph stream
summarization. It has small memory usage, high update
speed, and supports almost all kinds of queries for
graphs. Most important of all, it uses a combination
of ﬁngerprints and hash addresses to achieve very high
accuracy.
2) We propose a technique called square hashing in the
implementation of GSS. It helps to decrease the buffer
size, improve update speed and reduce memory cost. It
also eases the inﬂuence brought by the skewness in node
degrees.
3) We deﬁne 3 graph query primitives and give details
about how GSS supports them. Almost all algorithms
for graphs can be implemented with these primitives.
4) We carry out theoretical analysis and extensive experi-
ments to evaluate the performance of GSS, which show
that when using 1/256 memory size of the state-of-the-
art graph summarization algorithm, our algorithm still
signiﬁcantly outperforms it for most queries.
II. RELATED WORK
In this part we will give a brief introduction about the
related works. The prior arts of graph stream summarization
can be divided into two kinds. The ﬁrst kind is composed
of counter arrays and stores each data item in these arrays
independently, ignoring the connections between them. They
only support queries for edge weights, but do not support any
queries involved with topology of the graph. This kind includes
CM sketches [2], CU sketches [3], gSketches [6] and so on.
The second kind supports all queries in the streaming graph,
but suffers from poor accuracy. This kind includes TCM [7]
and gMatrix [8]. Because of space limitation, in this section
we only introduce the second kind which is more relevant to
our work.
TCM [7] is the state-of -the-art of data structures for graph
stream summarization. It is composed of an adjacency matrix
that stores the compression of the streaming graph. It uses
a hash function H(·) to compress the streaming graph G =
(V, E) into a smaller graph sketch Gh. For each node v in G,
TCM maps it to node H(v) in Gh. For each edge e = −→
s, d in
G, TCM maps it to edge −−−−−−−→
H(s), H(d) in Gh. The weight of
an edge in Gh is an aggregation of the weights of all edges
mapped to it. A hash table that stores the hash value and the
original ID pairs can be built in this map procedure to retrieve
the original node IDs for some queries. Then TCM uses an
adjacency matrix to represent the graph sketch. If we represent
the size of the value range of H(·) with M, we need to build an
M × M adjacency matrix. Each bucket in the matrix contains
a counter. The weight of edge −−−−−−−→
H(s), H(d) in the graph sketch
is added to the counter in the bucket in row H(s), column
H(d).
When the memory is sufﬁcient, we can also build multiple
sketches with different hash functions, and report the most
accurate value in queries.
In order to satisfy the demand on memory usage, the size
of the adjacency matrix, M × M has to be within O(|E|),
which means M ≪|V | for a sparse streaming graph where
|E|
|V | is usually within 10. This means the graph sketch Gh is
usually much smaller than G, a lot of nodes and edges will
be aggregated. As a result, the accuracy of TCM is poor.
The gMatrix [8] is a variant of TCM. Its structure is similar
to TCM. But it uses reversible hash functions to generate graph
sketches. It also extends TCM to more queries like edge heavy
hitters and so on. However, different from the accurate hash


## Page 3


tables, the reversible hash function introduces additional errors
in the reverse procedure. Therefore the accuracy of gMatrix is
no better than TCM, sometimes even worse.
There are some graph algorithms for statistic graph com-
pression [16]–[18] or speciﬁc queries in graph stream pro-
cessing [19]–[21]. However, they are either not suitable for
high dynamic graph streams or too limited in functions. We
do not introduce them in detail due to space limit.
III. PROBLEM DEFINITION
Deﬁnition 1: Graph
Stream: A graph stream is an
unbounded
timing
evolving
sequence
of
items
S
=
{e1, e2, e3......en}, where each item ei = (−→
s, d; t; w) indicates
a directed edge1 from node s to node d, with wight w. The
timepoint ti is also referred as the timestamp of ei. Thus, the
edge streaming sequence S forms a dynamic directed graph
G = (V, E) that changes with the arrival of every item ei,
where V and E denote the set of nodes and the set of edges
in the graph, respectively. We call G a streaming graph for
convenience.
In a graph stream S, an edge −→
s, d may appear multiple
times with different timestamps. The weight of such edge in
the streaming graph G is SUM of all edge weights sharing
the same endpoints. The weight w can be either positive or
negative. An item with w < 0 means deleting a former data
item.
Example 1: A sample graph stream S and the corresponding
streaming graph G are both shown in Fig. 1. Each node has an
ID that uniquely identiﬁes itself. If an edge appears multiple
times, its weights are added up as stated above.
In practice, G is usually a large, sparse and high speed
dynamic graph. The large volume and high dynamicity make
it hard to store graph streams using traditional data structures
such as adjacency lists and adjacency matrices. The large space
cost of O(|V |2) rules out the possibility of using the adjacency
matrix to represent a large sparse graph. On the other hand, the
adjacency list has O(|E|) memory cost, which is acceptable,
but the time cost of inserting an edge is O(|V |), which is
unacceptable due to the high speed of the graph stream.
The goal of our study is to design a linear space cost
data structure with efﬁcient query and update algorithms over
high speed graph streams. To meet that goal, we allow some
approximate query results but with small and controllable
errors. However, traditional graph stream summarization ap-
proaches either cannot answer graph topology queries such as
reachability queries (such as CM sketches [2] and gSketches
[6]) or fail to provide accurate query results (such as TCM [7]
and gMatrix [8]). Therefore, in this paper, we design a novel
graph stream summarization strategy.
In order to give a deﬁnition of the graph stream summa-
rization problem, First we deﬁne the graph sketch as follows:
Deﬁnition 2: Graph Sketch: a graph sketch of G = (V, E)
is a samller graph Gh = (Vh, Eh) where |Vh| ⩽|V | and
|Eh| ⩽|E|. A map function H(·) is used to map each node
1The approach in this paper can be easily extended to handle undirected
graphs.
in V to a node in Vh, and edge e = −→
s, d in E is mapped to
edge −−−−−−−→
H(s), H(d) in Eh. The weight of an edge in Eh is the
SUM of the weights of all edges mapped to it.
Formally, we deﬁne our graph stream summarization problem
as follows.
Graph stream S
Streaming graph G
(a, b; t1; 1) (a, c; t2; 1) (b, d; t3; 1) (a, c; t4; 1) (a, f; t5; 1)
(c, f; t6; 1)
(a, e; t7; 1) (a, c; t8; 3)
(c, f; t9; 1) (d, a; t10; 1)
( d, f; t11; 1) (f, e; t12; 3) (a, g; t13; 1) (e, b; t14, 2) (d, a; t15; 1)
g
a
c
f
d
b
e
1
1
1
1
1
2
2
3
1
5
2
Fig. 1. A sample graph stream
Deﬁnition 3: Graph Stream Summarization: Given a
streaming graph G = (V, E), the graph stream summarization
problem is to design a graph sketch Gh = (Vh, Eh), and the
corresponding data structure DS to represent Gh, where the
following conditions hold:
1) There is a function H(·) that map nodes in V to nodes
in Vh;
2) The space cost of DS is O(|E|);
3) DS changes with each new arriving data item in the
streaming graph and the time complexity of updating
DS should be O(1);
4) DS supports answering any query over the original
streaming graph G with small and controllable errors.
In the context of streaming graphs, G changes with every
data item in the graph stream S, which is mapped to updating
the graph sketch Gh, and conducted in data structure DS. For
every new item (−→
s, d; t; w) in S, we map edge −→
s, d in G to
edge −−−−−−−→
H(s), H(d) in Gh with weight w and then insert it into
Gh. Similarly, queries over G are also mapped to the same
kind of queries over the graph sketch Gh. In order to support
any kind of graph queries, we ﬁrst deﬁne three graph query
primitives as follows, since many kinds of graph queries can
be answered using these primitives.
Deﬁnition 4: Graph Query Primitives: Given a graph
G(V, E), the three graph query primitives are:
• Edge Query: given an edge e = −→
s, d, return its weight
w(e) if it exists in the graph and return −1 if not.
• 1-hop Successor Query: given a node v, return a set of
nodes that are 1-hop reachable from v, and return {−1}
if there is no such node;
• 1-hop Precursor Query: given a node v, return a set of
nodes that can reach node v in 1-hop, and return {−1}
if there is no such node.


## Page 4


With these primitives, we can re-construct the entire graph.
We can ﬁnd all the node IDs in the hash table. Then by car-
rying out 1-hop successor queries or 1-hop precursor queries
for each node, we can ﬁnd all the edges in the graph. The
weight of the edges can be retrieved by the edge queries. As
the graph is reconstructed, all kinds of queries and algorithms
can be supported. In fact, in many situations, it is not necessary
to re-construct the entire graph. We can just follow the speciﬁc
algorithm and use the primitives to get the information when
needed. Therefore, The data structure DS needs to support
these 3 query primitives.
IV. GSS: BASIC VERSION
In this section, we describe a conceptually simple scheme
to help illustrate intuition and beneﬁt of our approach. The
full approach, presented in Section V, is designed with more
optimizations. As stated above, to produce a graph stream
summarization, we ﬁrst need to design a graph sketch Gh =
(Vh, Eh) for the streaming graph G. Initially, we use the same
strategy as TCM to generate the graph sketch. We choose
a hash function H(·) with value range [0, M), then Gh is
generated as following:
1) Initialization: Initially, Vh = ∅, and Eh = ∅.
2) Edge Insertion: For each edge e = (s, d) in E with
weight w, we compute hash values H(s) and H(d). If
either node with ID H(s) or H(d) is not in Vh yet, we
insert it into Vh. Then we set H(e) = −−−−−−−→
H(s), H(d). If
H(e) is not in Eh, we insert H(e) into Eh and set its
weight w(H(e)) = w. If H(e) is in Eh already, we add
w to the weight.
Gh is empty at the beginning and expands with every data item
in the graph stream. We can store ⟨H(v), v⟩pairs with hash
tables to make this mapping procedure reversible. This needs
O|V | additional memory, as |V | ⩽|E|, the overall memory
requirement is still within O(|E|).
a
b
c
d
e
f
g
2
15
5
28
10
18
5
Node
H(v)
Graph Sketch Gh
2
5
18
28
15
10
6
1
1
1
1
1
2
2
2
3
Fig. 2. A sample map function
Example 2: A graph sketch Gh for the streaming graph G
in Figure 1 is shown in Figure 2. The value range of the hash
function H(·) is [0, 32). In the example, nodes c and g are
mapped to the same node with ID 5 in Gh. In Gh, the weight
of edge (2, 5) is 6, which is the summary of the weight of
edge (a, c) and edge (a, g) in G.
Obviously, the size of the value range of the map function
H(·), which we represent with M, will signiﬁcantly inﬂuence
the accuracy of the summarization, especially in the 1-hop
successor / precursor query primitives. In a uniform mapping
with the hash function, each node in G has the probability
1
M to collide with another, which means they are mapped
to the same node in Gh. When there are |V | nodes, the
probability that a node v does not collide with any other
nodes is (1 −
1
M )
|V |−1 ≈e
|V |−1
M
. In the 1-hop successor /
precursor queries, if v collides with others, the query result
about it will deﬁnitely have errors. Therefore we have to
use a large M to maximize this probability.
Figure 3 shows the theoretical results of the relationship
between M and the accuracy of the query primitives .
The results are computed according to analysis in Section
VI-B.
(In the ﬁgure of the edge query, d1 and d2 means
the in-degree of the source node and the out-degree of the
destination node of the queried edge. In the ﬁgure of the 1-
hop successor / precursor query, din and dout means the in-
degree and the out-degree of the queried node, respectively).
The ﬁgure shows that we have to use a large M to achieve
high accuracy in the query primitives, which is not possible
in the prior works. According to Figure 3, only when
M
|V | >
200, the accuracy ratio is larger than 80% in 1-hop successor
/ precursor queries. When
M
|V | ≤1, the accuracy ratio falls
down to nearly 0, which is totally unacceptable.
Both TCM and the gMatrix resort to an adjacency matrix
to represent Gh. In this case, the matrix rank m equals to
M, i.e, the value range of the map function. To keep the
memory usage of the graph sketch within O(|E|) (Condition
2 in Deﬁnition 3), m must be less than
√
E, that means
m = M <
√
E ≪|V | for a sparse streaming graph. According
to our theoretical analysis2 in Figure 3, the query results’
accuracy is quite low in them. Our experiments in Section
VII also conﬁrm the theoretical analysis.
Considering the above limitations, we design a novel data
structure for graph stream summarization, called GSS.
Deﬁnition 5: GSS: Given a streaming graph G = (V, E),
we have a hash function H(·) with value range [0, M) to map
each node v in graph G to node H(v) in graph sketch Gh.
Then we use the following data structure to represent the graph
sketch Gh:
1) GSS consists of a size m × m adjacency matrix X and
an adjacency list buffer B for left-over edges.
2) For each node H(v) in sketch graph Gh, we deﬁne an
address h(v)(0 ⩽h(v) ⩽m) and a ﬁngerprint f(v)(0 ⩽
f(v) ⩽F) where M = m × F and h(v) = ⌊H(v)
F ⌋,
f(v) = H(v)%F.
3) Each edge −−−−−−−→
H(s), H(d) in the graph sketch Gh is mapped
to a bucket in the row h(s), column h(d) of the matrix
X. We record [⟨f(s), f(d)⟩, w] in the corresponding
bucket of the matrix, where w is the edge weight and
f(s), f(d) are ﬁngerprints of the two endpoints.
4) Adjacency list buffer B records all left-over edges in
Gh, whose expected positions in the matrix X have been
occupied by other previous inserted edges already.
2The detailed analyses are given in Section VI-B


## Page 5


M/|V|
ln(d1+d2)
Correct Rate
(a) Edge Query
M/|V|
ln(dout)
Correct Rate
(b) 1-hop Successor Query
M/|V|
ln(din)
Correct Rate
(c) 1-hop Precursor Query
Fig. 3. Inﬂuence of M on Accuracy
Matrix
Buffer
a
b
c
d
e
f
g
2
15
5
28
10
18
5
<0, 2> <1, 7> <0, 5> <3, 4> <1, 2> (2, 2)
(0, 5)
Node
<h(v), f(v)>
H(v)
GSS
Fingerprint Pair
Edge Weight
Node Hash 
Value
0
0
1
1
2
2
3
3
Fig. 4. A sample of the basic version of data structure
When implementing a GSS for a graph stream, in order to
satisfy the O(|E|) memory cost requirement, we usually set
m = α ×
p
|E|, where α should be a constant approximate
to 1. To achieve high accuracy, we set M ≫|V |. This can
be achieved by setting large F, in other words, using long
ﬁngerprints. When the memory is not sufﬁcient, we can also
set smaller M with smaller m and F, but this will decrease
the accuracy.
Example 3: The basic version of GSS to store Gh in Figure
2 is shown in Figure 4. Here we set F = 8. The nodes in
the original streaming graph and their corresponding H(v),
h(v) and f(v) are shown in the table. In this example, edge
−−→
2, 10 and edge −−→
5, 18 in Gh are stored in the buffer because of
collisions with other edges.
We discuss the insertion and primitive query operations over
GSS as follows:
Edge Updating: When a new item (s, d; t; w) comes in
the graph stream S, we map it to an edge −−−−−−−→
H(s), H(d) with
weight w in graph sketch Gh. Then we ﬁnd the bucket in
row h(s), column h(d). If the bucket is empty, we store the
ﬁngerprints pair ⟨f(s), f(d)⟩together with the edge weight w
in the bucket. If it is not empty, we compare the ﬁngerprint
pair of this edge with the ﬁngerprint pair ⟨f(s′), f(d′)⟩that is
in the bucket already. If they are same, we add the weight w
to the existing one; otherwise, it means this bucket has been
occupied by other edges, and we store edge −−−−−−−→
H(s), H(d) in
the adjacency list in the buffer B. We call this kind of edges
as left-over edges.
Graph Query Primitives: The three primitives (deﬁned in
Deﬁnition 4) are all supported with our proposed data structure
GSS.
Edge Query: Given an edge query e = −→
s, d, we work as
follows. We check the bucket in row h(s), column h(d) in
the matrix. Let ⟨f(s′), f(d′)⟩be the ﬁngerprint pair stored at
the bucket. If ⟨f(s′), f(d′)⟩equals to the the ﬁngerprint pair
⟨f(s), f(d)⟩of edge −→
s, d, we return the weight in the bucket.
Otherwise we search the buffer B for edge −−−−−−−→
H(s), H(d) using
the adjacency list. If we cannot ﬁnd it in the matrix X or in the
buffer B, we return −1, i.e. reporting that the edge e = −→
s, d
does not exists.
1-hop Successor Query: To ﬁnd the 1-hop successors of
node v, we work as follows. First, we search all buckets in row
h(v) of the matrix X. If a bucket in row h(v) and column c has
a ﬁngerprint pair ⟨f(v), f(vs)⟩, we add node H(vs) = c×F +
f(vs) to the 1-hop successors set SS. After that, we also need
to search the buffer area to ﬁnd all edges with source node
H(v), and add its destination node to the 1-hop successors
set S. We return −1 if we ﬁnd no result, i.e., |SS| = 0.
Otherwise, for each H(s) in successors set SS, we obtain the
original node IDs by accessing the hash table.
1-hop Precursor Query: To ﬁnd the 1-hop precursors of
node v, we have the analogue operations with 1-hop Successor
Query if we switch the columns and the rows in the matrix
X. The details are omitted due to space limit.
In GSS, we store edges with different source nodes in Gh
in one row of the matrix, because the graph is sparse and
each node is usually connected to very few edges. We can use
ﬁngerprints to distinguish them. For example, edge −−−→
15, 28 and
edge −−−→
10, 15 are all stored in row 1, but they have different
source node ﬁngerprints, namely 2 and 7, thus we know
exactly which nodes they are from. It is similar in columns.
Fingerprints also help us to distinguish edges when they are
mapped into the same bucket. This enables us to apply a map
function with a much larger value range, and generate a much
larger graph sketch with the same size of matrix as TCM. With


## Page 6


a 4 × 4 matrix as in Figure 2, TCM can only support a map
function with M = 4 , and the number of nodes in the graph
sketch will be no more than 4, thus the accuracy will he much
poorer.
V. GSS: AUGMENTED ALGORITHM
As we know, GSS has two parts: a size m × m matrix X
and an adjacency list buffer B for left-over edges. Obviously,
we only need O(1) time to insert an edge into X, but the
linear time O(|B|) if the edge must goto the buffer B, where
|B| represents the number of all left-over edges. Therefore |B|
both inﬂuences the memory and time cost. In this section, we
design several solutions to reduce the size of buffer B.
A. Square Hashing
In the basic version, an edge is pushed into buffer B if
and only if its mapped position in the matrix X has been
occupied. The most intuitive solution is to ﬁnd another bucket
for it. Then where to ﬁnd an empty bucket? We further notice
the skewness in node degrees. In the real-world graphs, node
degrees usually follow the power law distribution. In other
words, a few nodes have very high degrees, while most nodes
have small degrees. Consider a node v that has A out-going
edges in the graph sketch Gh. For a m × m adjacency matrix
X in GSS (see Deﬁnition 5), there are at least A −m edges
that should be inserted into buffer B, as these A edges must be
mapped to the same row (in X) due to the same source vertex
v. These high degree nodes lead to crowed rows and result in
most left-over edges in buffer B. On the other hand, many
other rows are uncrowded. We have the same observation
for columns of matrix X. Is it possible to make use of the
unoccupied positions in uncrowded rows/columns? It is the
motivation of our ﬁrst technique, called square hashing.
For each node with ID H(v) = ⟨h(v), f(v)⟩in Gh, we
compute a sequence of hash addresses {hi(v)|1 ⩽i ⩽r}(0 ⩽
hi(v) < m) for it. Edge −−−−−−−→
H(s), H(d) is stored in the ﬁrst empty
bucket among the r × r buckets with addresses
{(hi(s), hj(d))|(1 ⩽i ⩽r, 1 ⩽j ⩽r)}
where hi(s) is the row index and hj(d) is the column index.
We call these buckets mapped buckets for convenience. Note
that we consider row-ﬁrst layout when selecting the ﬁrst empty
bucket.
Example 4: An example of square hashing is shown in
Figure 5. The inserted edge is mapped to 9 buckets, and the
ﬁrst 2 with address (h1(s), h1(d)) and (h1(s), h2(d)) have
been already occupied. Therefore the edge is inserted in the
third mapped bucket. In the bucket, we store the weight,
the ﬁngerprint pair, together with an index pair ⟨1, 3⟩which
indicates the position of this bucket in the mapped buckets
sequence. We will talk about the use of index pair later.
The following issue is how to generate a good hash address
sequence {hi(v)|1 ≤i ≤r} for a vertex v. There are two
requirements:
Independent: For two nodes v1 and v2, we use P to represent
the probability that ∀1 ≤i ≤r, hi(v1) = hi(v2). Then
we have P = Qr
i=1 Pr(hi(v1) = hi(v2)). In other words,
the randomness of each address in the sequence will not be
h1(d)
h2(d)
h3(d)
h1(s)
h2(s)
h3(s)
Fingerprint < f(s), f(d) >
Index 
<1, 3>
Mapped Bucket
Occupied Bucket
Empty Bucket
Fig. 5. The square hashing
inﬂuenced by others. This requirement will help to maximize
the chance that an edge ﬁnds an empty bucket among the r×r
mapped buckets.
Reversible: Given a bucket in row R and column C and the
content in it, we are able to recover the representation of the
edge e in the graph sketch Gh: −−−−−−−→
H(s), H(d), where e is the
edge in that bucket. This property of indexing is needed in
the 1-hop successor query and the 1-hop precursor query. As
in these queries, we need to check the potential buckets to
see if they contain edges connected to the queried node v and
retrieve the other end point in each qualiﬁed bucket.
To meet the above requirements, we propose to use linear
congruence method [22] to generate a sequence of r random
values {qi(v)|1 ⩽i ⩽r} with f(v) as seeds. We call this se-
quence the linear congruential (LR) sequence for convenience.
The linear congruence method is as following: select a timer
a, small prime b and a module p, then
(
q1(v) = (a × f(v) + b)%p
qi(v) = (a × qi−1(v) + b)%p, (2 ⩽i ⩽r)
(1)
By choosing a, b and p carefully, we can make sure the
cycle of the sequence we generate is much larger than r, and
there will be no repetitive numbers in the sequence [22]. Then
we generate a sequence of hash addresses as following:
{hi(v)|hi(v) = (h(v) + qi(v))%m, 1 ⩽i ⩽r}
(2)
When storing edge −−−−−−−→
H(s), H(d) in the matrix, besides stor-
ing the pair of ﬁngerprints and the edge weight, we also store
an index pair (is, id), supposing that the bucket that contains
this room has an address (his(s), hid(d)). As the length of
the sequence, r, is small, the length of each index will be less
than 4 bits. Therefore storing such a pair will cost little.
Note that the hash sequence {qi(v)|1 ⩽i ⩽r} generated
by the linear congruence method are both independent and
reversible. The independence property has been proved in [8].
We show how to recover the original hash value H(v) based on
the f(v), hi(v) and the index i as follows. First, we compute
the LR sequence {qi(v)} with f(v) following equation 4.
Second we use the equation (h(v) + qi(v))%m = hi(v) to
compute the original hash address h(v). As h(v) < m, the
equation has unique solution. At last we use H(v) = h(v) ×


## Page 7


F + f(v) to compute H(v). Given a bucket in the matrix, the
ﬁngerprint pair (f(s), f(d)) and the index pair (is, id) are all
stored in it, and we have his(s) = R, hid(d) = C, where R
and C are the row index and the column index of the bucket in
the matrix, respectively. Therefore we can retrieve both H(s)
and H(d) as above.
Matrix
Empty Buffer
a
b
c
d
e
f
g
2
15
5
28
10
18
5
<0, 2> <1, 7> <0, 5> <3, 4> <1, 2> (2, 2)
(0, 5)
{1, 0}
{3, 2}
{0, 3}
{2, 1}
{2, 1}
{3, 2}
{0, 3}
Node
<h(v), f(v)>
H(v)
{hi(v)}
GSS
Fingerprint Pair
Edge Weight
Index Pair
0
1
1
0
2
2
3
3
Fig. 6. A sample of the modiﬁed version of data structure
Example 5: An example of the modiﬁed version is shown
in Fig. V-A. In the matrix we stored Gh in Fig. 2, which is a
compressed graph of G in Fig.1. In this example we set F = 8,
m = 4, r = 2, and the equation in the linger congruence
method is(
q1(v) = (5 × f(v) + 3)%8
qi(v) = (5 × qi−1(v) + 3)%8, (2 ⩽i ⩽r)
(3)
Compared to the basic version, in the modiﬁed version all
edges are stored in the matrix, and the number of memory
accesses we need to ﬁnd an edge in the matrix is within 22 =
4. In fact in the example we only need one memory access to
ﬁnd most edges, and 2 for a few ones.
In the following, we illustrate the four basic operators in
this data structure GSS.
Edge Updating: When a new item (s, d, t; w) comes in the
graph stream S, we map it to edge −−−−−−−→
H(s), H(d) in the graph
sketch Gh with weight w. Then we compute two hash address
sequences {hi(s)} and {hi(d)} and check the r2 mapped
buckets with addresses {(hi(s), hj(d))|1 ⩽i ⩽r, 1 ⩽j ⩽r}
one by one. For a bucket in row his(s) and column hid(d),
if it is empty, we store the ﬁngerprint pair (f(s), f(d)) and
the index pair (is, id) and weights w in it, and end the
procedure. If it is not empty, we check the ﬁngerprint pair
(f(s′), f(d′)) and the index pair (i′
s, i′
d) stored in the bucket.
If the ﬁngerprint pair and the index pair are all equal to the
corresponding pairs of the new inserted edge −−−−−−−→
H(s), H(d), we
add w to the weights in it, and end the procedure. Otherwise
it means this bucket has been occupied by other edges and we
consider other hash addresses following the hash sequence. If
all r2 buckets have been occupied, we store edge −−−−−−−→
H(s), H(d)
with weight w in the buffer B, like the basic version of GSS.
Graph Query Primitives: The three graph query primitives
are supported in the modiﬁed data structure as follows:
Edge Query: When querying an edge e = −→
s, d, we map it to
edge −−−−−−−→
H(s), H(d) in the graph sketch, and use the same square
hashingmethod to ﬁnd the r2 mapped buckets and check them
one by one. Once we ﬁnd a bucket in row his(s) and column
hid(d) which contains the ﬁngerprint pair (f(s), f(d)) and
the index pair (is, id), we return its weight as the result. If we
ﬁnd no results in the r2 buckets, we search the buffer for edge
−−−−−−−→
H(s), H(d) and return its weights. If we still can not ﬁnd it,
we return −1.
1-hop Successor Query: to ﬁnd the 1-hop successors of node
v, we map it to node H(v) in Gh. Then we compute its hash
address sequence hi(v) according to H(v), and check the r
rows with index hi(v), (1 ⩽i ⩽r). If a bucket in row his(v),
column C contains ﬁngerprint pair ((f(v), f(x)) and index
pair (is, id) where f(x) is any integer in range [0, F) and
id is any integer in range [1, r],
we use f(x), id and C to
compute H(x) as stated above. Then we add H(x) to the 1-
hop successor set SS. After searching the r rows, we also
need to check the buffer to see if there are any edges with
source node H(v) and add their destination node to SS. We
return −1 if we ﬁnd no result, otherwise we obtain the original
node IDs from SS by accessing the hash table ⟨H(v), v⟩.
1-hop Precursor Query: to answer an 1-hop precursor query,
we have the analogue operations with 1-hop Successor Query
if we switch the columns and the rows in the matrix X. The
details are omitted due to space limit.
After applying square hashing, the edges with source node
H(v) in Gh are on longer stored in a single row, but spread
over r rows with addresses hi(v)(1 ⩽i ⩽r). Similarly,
edges with destination node H(v) are stored in the r different
columns. These rows or columns are shared by the edges with
different source nodes or destination nodes. The higher degree
a node has, the more buckets its edges may take. This eases the
congestion brought by skewness in node degrees. Moreover,
as each bucket has multiple mapped buckets, it has higher
probability to ﬁnd an empty one. Obviously, square hashing
will reduce the number of left-over edges.
B. Further Improvements
There are some other improvements which can be imple-
mented to GSS.
1) Mapped Buckets Sampling: In the modiﬁed version of
GSS, each edge has r2 mapped buckets. We usually set r to
integers from 4 to 16. When the skewness of node degrees
is serious, r can be larger. If we check all the r2 buckets
when inserting an edge, it will be time consuming. To improve
the updating speed, which is very important for graph stream
summarization, we can use a sampling technique to decrease
the time cost. Instead of check all the r2 buckets, we select
k buckets as a sample from the mapped buckets, we call
these buckets candidate buckets for short. For each edge we
only check these k buckets in updating and query, and the
operations are the same as above. The method to select these
k buckets for an edge e is also a linear congruence method.


## Page 8


We add the ﬁngerprint of the source node and the destination
node of e to get a seed seed(e), then we compute a k length
sequence as
(
q1(e) = (a × seed(e) + b)%p
qi(e) = (a × qi−1(e) + b)%p, (2 ⩽i ⩽k)
(4)
where a, b and p are the same integers used above. We choose
the k buckets with address

(hj qi(e)
r
k
%r(s), h(qi(e)%r)(d))|1 ⩽i ⩽k

(5)
{hi(s)} and {hi(d)} are the hash address sequence of the
source node and the destination node, respectively.
2) Multiple Rooms: When the memory is sufﬁcient, we
do not need to use multiple matrices to increase accuracy as
TCM, as the accuracy is already very high. Instead, in order to
further decrease the buffer size, we can separate each bucket
in the matrix into l segments, and each segments contains an
edge, including the weight, the ﬁngerprint pair and the index
pair. We call each segment a room for convenience. When
performing the basic operators, we use the same process as
above the ﬁnd the buckets we need to check, and search all
the rooms in them to ﬁnd qualiﬁed edges or empty rooms.
However, when the rooms in each bucket are stored sepa-
rately, the speed will probably decrease, as we can not fetch
the l rooms in one memory access in most cases, and multiple
memory accesses increase the time cost. As shown in Fig.
V-B2, we separate the bucket into 3 area: the index area, the
ﬁngerprint area, and the weight area. Each area contains the
corresponding parts of the l rooms. When we check this bucket
to ﬁnd certain edges, we can ﬁrst check all the index pairs.
If we ﬁnd a matched index pair, we check the corresponding
ﬁngerprint pair, and if the ﬁngerprint pair is also matched, we
fetch the corresponding weights. If we do not ﬁnd any matched
index pair, we can just move on and do not need to check the
ﬁngerprint pairs any more. As the index pairs are very small,
usually no more than 1 byte, we can fetch all the index pairs
in one memory access. This will omit a lot of unnecessary
memory accesses.
Index Area
Fingerprint Area
Weight Area
Edge  e
Index pair
Fingerprint pair
Weight
Occupied Position
Empty Position
Fig. 7. Bucket Separation
VI. ANALYSIS
A. Memory and Time Cost Analysis
As stated above, GSS has O(|E|) memory cost and constant
update speed. The memory cost of GSS is O(|Eh|+|B|), to be
precise, where |Eh| is the number of edges in the graph sketch
Gh and |B| is the size of buffer. When we use hash table to
store the original ID, additional O(|V |) memory is needed, but
the overall memory cost is still O(|E|). The update time cost
is O(k + |B|
|Eh||B|), where k is the number of sampled buckets
and is a small constant. When an edge is stored in the matrix,
we only need to check at most k candidate buckets, which
takes O(k) time. Each edge has probability
|B|
|Eh| to be stored
in the buffer. When it is stored in the buffer, the update takes
additional O(|B|) time, as the buffer is an adjacency list. In
implementations the buffer stores 0 edges in most cases, which
will be shown in section VI-D and VII-G. Therefore
|B|
|Eh||B|
is also a small constant. When it is necessary to store the ID of
nodes in applications, one insertion to the hash table is needed,
which also takes constant time. Overall, the update time cost
is O(1).
The time cost of queries is based on the algorithms we use.
We consider the time cost of the operators as an evaluation.
The time cost of the edge query operator is the same as the
update, and the time cost of the 1-hop successor query and
1-hop precursor query is O(rm + |B|), where m is the side
length of the matrix and r is the length of the hash address
sequence.
B. Accuracy Analysis
In this part we evaluate the accuracy of GSS. Before we
analyze the probability of errors, we ﬁrst propose the following
theorem:
Theorem 1: The storage of the graph sketch Gh in the data
structure of GSS is accurate. Which means for any edge e1 =
−−−−−−−−−→
H(s1), H(d1) and e2 = −−−−−−−−−→
H(s2), H(d2) in Gh, the weights of
them will be added up if and only if H(s1) = H(s2), H(d1) =
H(d2).
As the buffer is an adjacency list that stores edges in Gh
accurately, we only need to check the matrix. If we want to
prove the storage of the graph sketch is accurate, we need to
prove that if such collision happens to e1 and e2, we have e1 =
e2 in Gh, in other words, H(s1) = H(s2), H(d1) = H(d2)
.We assume that the bucket contains the wights of e1 and e2
is in row R and column C in the matrix. Obviously e1 and e2
must have the same ﬁngerprint pair, otherwise it will be easy
for us to differentiate them. With the same ﬁngerprints, these
two edges will produce the same LR sequences {q(s)} and
{q(d)}. Moreover, this bucket must have the same index pair
for these two edges, and we represent this pair with (c1, c2).
Then we have





(h(s1) + qc1(s1))%m = R
((h(s2) + qc1(s2)))%m = R
qc1(s1) = qc1(s2)
(6)


## Page 9


and





(h(d1) + qc2(d1))%m = C
((h(d2) + qc2(d2)))%m = C
qc2(d1) = qc2(d2)
(7)
With these equations, we can get that h(d1)
=
h(d2),
h(s1) = h(s2) when 0 ⩽h(s1), h(s2), h(d1), h(d2) < m.
With the same ﬁngerprint pair and hash values, we have
H(s1) = H(s2), H(d1) = H(d2). e1 and e2 are the same
edge in Gh. Therefore the storage of Gh is accurate.
This theorem means we only need to consider the procedure
of mapping G to Gh, as all errors happen in this procedure.
We use ˆP to represent the probability of the following event:
Deﬁnition 6: Edge Collision: An edge collision means that
given an edge e, there is at least one e′ in G and e′ ̸= e which
satisﬁes H(e) = H(e′) in the compressed graph Gh.
We set P = 1 −ˆP, and P is the main component of the
error rate of all the 3 graph query primitives.
In the edge query, P is just the correct rate. In the 1-hop
successor query for a node v, the correct rate is P |V |−d, where
|V | is the number of nodes in G, and d is the out-degree of
the queried node. Because we will get a correct answer if and
only if for each v′ in G which is not a 1-hop successor of
v, (v, v′) does not collide with any existing edges, and the
probability of such an event is P. It is the same in the 1-hop
precursor query. Therefore we need to compute P to evaluate
the accuracy of GSS.
C. Collision Rate
Now we show the probability that an edge e suffers from
edge collision, ˆP. For e = −→
s, d in G, we assume there are D
edges with source node s or destination node d in G besides
e, and there are totally |E| edges in G. We represent the size
of the value range of the map function H(·) with M.
For an edge share no common endpoints with e , it will
collide with e when both its source node and destination node
collide with the corresponding node of e. The probability that
it collides with e in map function H(·) is:
p1 =
1
M 2
(8)
The probability that all the |E| −D edges have no collisions
with e is
Pr1 = (1 −p1)|E|−D
(9)
For those D edges connected to e, as one of the two end points
is the same, the probability that such an edge has a collision
with e is
p2 = 1
M
(10)
The probability that all the D edges have no collisions with e
is
Pr2 = (1 −p2)D
(11)
Therefore the correct rate of e, in other words, all the |E|
edges do not have collisions with e in mapping is
P = Pr1 × Pr2
= ((1 −p1)|E|−D) × ((1 −p2)D)
= e−p1×(|E|−D) × e−p2×D
= e−|E|−D
M2
× e−D
M
= e−|E|+(M−1)×D
M2
(12)
And ˆP = 1 −P. In GSS we have M = m × F, where m
is the length of the matrix, and F is the maximum size of
the ﬁngerprints. The above correct rate is usually very high
in applications. For example, suppose that the ﬁngerprints we
use are 8-bit, in other words, F = 256, and when querying
an edge e, we have |E| = 5 × 105,D = 200. We use a matrix
with side length m = 1000. Then the correct rate of this edge
query is e−0.00078 = 0.9992. On the other hand, in TCM the
accuracy analysis is the same as GSS but we have M = m.
This lead to the difference on accuracy with the same size of
matrix. With the same matrix size, TCM only has a probability
of 0.497 to get a correct weight for e.
D. Buffer Size Analysis
After all the improvements, the buffer in GSSis very small.
The mathematical expression of the buffer size is very compli-
cated and is inﬂuenced by many details of the graph. Therefore
we give an expression of the probability that a new edge
e becomes a left-over edge, which means inserted into the
buffer, as a measurement. Assuming that there are already N
different edges in the graph stream, and among them D edges
have common source node or common destination node with
e.
The length of the matrix is m, and each bucket in the
matrix has l rooms. For each node we compute a hash address
sequence with length r. For each edge we choose k candidate
buckets among the r2 mapped buckets. Then the probability
that e becomes a left-over edge is: For each candidate bucket
of e, as the N −D non-adjacent edges are randomly inserted
into the matrix with area m2, the probability that there are a1
non-adjacent edges inserted into it is:
p1(a1) =
N −D
a1

× ( 1
m2 )
a1
× (1 −1
m2 )
N−D−a1
=
N −D
a1

× ( 1
m2 )
a1
× e−N−D−a1
m2
(13)
As the D adjacent edges are randomly inserted in an area of
r × m (r rows or r columns in the matrix), the probability
that there are a2 adjacent edges inserted into this bucket is:
p2(a2) =
D
a2

× (
1
r × m)
a2
× (1 −
1
r × m)
D−a2
=
D
a2

× (
1
r × m)
a2
× e−D−a2
r×m
(14)
The probability that there are already n edges inserted into
this bucket is:
p(n) =
n
X
a=0
p1(a) × p2(n −a)
(15)


## Page 10


The probability that there are less than l edges inserted into
this bucket is:
Pr =
l−1
X
n=0
p(n)
=
l−1
X
n=0
n
X
a=0
p1(a) × p2(n −a)
=
l−1
X
n=0
n
X
a=0
N −D
a
 D
n−a

( 1
m2 )
a
( 1
rm)
n−a
e−( N−D−a
m2
+ D−n+a
rm
)
(16)
This is also the lower bound that the bucket is still available
for e. The probability that e can not be inserted into the matrix
is the probability that all the k candidate buckets are not
available, which is:
P = (1 −Pr)k
(17)
where
Pr =
l−1
X
n=0
n
X
a=0
 
N −D
a
! 
D
n−a
!
( 1
m2 )
a
( 1
rm)
n−a
e−( N−D−a
m2
+ D−n+a
rm
)
(18)
Notice that this is an upper bound as we ignore collisions in
the map procedure from G to Gh. This probability is rather
small. For example if N = 1 × 106, D = 104, we still set
the side length of the matrix to w = 1000, and set r = 8,
l = 3, k = 8, the upper bound probability of insertion failure
is only 0.002. Experiments show that when the size of matrix
is nearly equal to the number of edges, there will be almost
no edges inserted into the buffer.
VII. EXPERIMENTAL EVALUATION
In this section, we show our experimental studies of
GSS.
We compare GSS with TCM on the three graph
query primitives: edge query , 1-hop successor query, 1-hop
precursor query (VII-D) and two compound queries, node
queries (VII-E) and reachability queries (VII-F). We also
evaluate the size of buffer (VI-D)and update speed of GSS
(VII-H). Then we further compare GSS with the state-of-
the-art graph processing algorithms on triangle counting and
subgraph matching VII-I.
All experiments are performed on a server with dual 6-
core CPUs (Intel Xeon CPU E5-2620 @2.0 GHz, 24 threads)
and 62 GB DRAM memory, running Ubuntu. All algorithms
including GSS and TCM are implemented in C++.
A. Data Sets
We choose three real world data sets. Details of three data
sets are described as follows:
1)email-EuAll 3.This data set is communication network
data generated using email data from a large European re-
search institution for a period of 18 months. Each node in
the directed graph corresponds to an email address. Each edge
between node src and dst represents src sent at least one email
to dst. The directed graph contains 265214 nodes and 420045
edges. We use the Zipﬁan distribution to add the weight to each
3http://snap.stanford.edu/data/email-EuAll.html
edge and the edge weight represents the appearance times in
the stream.
2)cit-HepPh4.It is the Arxiv HEP-PH (high energy physics
phenomenology) citation graph. If a paper src cites paper dst,
the data set contains a directed edge from src to dst. The data
set covers 34,546 papers as nodes with 421,578 edges. The
edge weights are also added using Zipﬁan distribution.
3)web-NotreDame 5.It is a web graph collected from the
University of Notre Dame. Nodes represent web pages and
directed edges represent hyperlinks between pages. The data
set contains 325729 nodes and 1497134 edges. We use the
Zipﬁan distribution to generate weights for the edges in the
data set, and insert the edges into the data structure one by one
to simulate the procedure of real-world incremental updating.
4)lkml-reply6.It is a collection of communication records
in the network of the Linux kernel mailing list. It contains
63399 email addresses (nodes) and 1096440 communication
records(edges). Each edge is weighted by its frequency in the
data set, and has a timestamp indicating the communication
time. We feed the data items to the data structure according
to their timestamps to simulate a graph stream.
5)Caida-networkﬂow
7
It
is
the
CAIDA
Internet
Anonymized Traces 2015 Dataset. It contains 445440480
communication records (edges) concerning 2601005 different
IP addresses (nodes). Each edge is weighted by its frequency in
the data set, and has a timestamp indicating the communication
time. We feed the data items to the data structure according
to their timestamps to simulate a graph stream.
The function we use to cumulate the edge weights is addi-
tion. In this case, TCM and GSS only have over-estimations.
The codes are open sourced8
B. Metrics
In this part we give a deﬁnition of the metrics we use in
experiments.
Average Relative Error (ARE): ARE measures the accu-
racy of the reported weights in edge queries and node queries.
Given a query q, the relative error is deﬁned as
RE(q) =
ˆ
f(q)
f(q) −1
where f(q) and
ˆ
f(q) are the real answer and the estimated
value of q. When giving a query set, the average relative error
(ARE) is measured by averaging the relative errors over all
queries int it. A more accuracy data structure will have smaller
ARE.
Average Precision We use average precision as the evalua-
tion metric in 1-hop successor queries, 1-hop precursor queries
and graph pattern matching. Given such a query q, we use SS
to represent the accurate set of 1-hop successors / precursors
of the queried node v, and ˆ
SS to represent the set we get by
4http://snap.stanford.edu/data/email-EuAll.html
5http://konect.uni-koblenz.de/networks/lkml-reply
6http://konect.uni-koblenz.de/networks/lkml-reply
7www.caida. org
8https://github.com/Puppy95/Graph-Stream-Sketch


## Page 11


q. As TCM and GSS have only false positives, which means
SS ⊆ˆ
SS, we deﬁne the precision of q as:
Precision(q) = |SS|
| ˆ
SS|
Average precision of a query set is the average value of the
precision of all queries in it. A more accuracy data structure
will have higher Average Precision
True Negative Recall: It measures the accuracy of the
reachability query. Because connectives of all edges are kept,
there is no false negatives in TCM and GSS, which means
if we can travel to d from s in the streaming graph, the
query result of these data structures will be deﬁnitely yes.
Therefore in experiments we use reachability query sets Q =
{q1, q2, ..., qk} where ∀qi ∈Q, source node s and destination
node d in qi are unreachable. True negative recall is deﬁned
as the number of queries reported as unreachable divided by
the number of all queries in Q.
Buffer Percentage: It measures buffer size of GSS. Buffer
percentage is deﬁned as the number of edges that the buffer
contains divided by the total number of edges in the graph
stream.
C. Experiments settings
In experiments, we implement two kinds of GSS with
different ﬁngerprint sizes: 12 bits and 16 bits, and vary the
matrix size. We use fsize to represent the ﬁngerprint size by
short. We apply all improvements to GSS, and the parameters
are as follows. Each bucket in the matrix contains l = 2 rooms.
The length of the address sequences is r = 16, and the number
of candidate buckets for each edge is k = 16 (r = 8,k = 8 for
the small data set email-EuAlland cit-HepPh). As for TCM,
we apply 4 graph sketches to improve its accuracy, and allow
it to use larger memory, because otherwise the gap between
it and GSS will be so huge that we can hardly compare them
in one ﬁgure. In edge query primitives, we allow TCM to use
8 times memory, and in other queries we implement it with
256 times memory, as its accuracy is too poor in these queries
(in web-NotreDame, we implement it with 16 times memory
because of the limitation of the memory of the server). This
ratio is the memory used by all the 4 sketches in TCM divided
by the memory used by GSS with 16 bit ﬁngerprint. When
the size of GSS varies, the size of matrix in TCM also varies
correspondingly to keep the ratio unchanged.
D. Experiments on query primitives
In this section, we evaluate the performance of GSS in the
3 basic graph query primitives: the edge query, the 1-hop
precursor query and the 1-hop successor query.
Figure 8,
Figure 9, and Figure 10 show that ARE of edge queries and
average precision of 1-hop precursor / successor queries for the
data sets, respectively. To reduce random error introduced by
the selection of the data sample, the edge query set contains all
edges in the graph stream, and the 1-hop precursor / successor
query set contains all nodes in the graph stream. The results
tell us that GSS performs much better in supporting these
query primitives than TCM, especially in the 1-hop precursor
/ successor query primitives. In both GSS and TCM, the ARE
decreases, and the precision increases with the growth of the
width of the matrix. This trend is not very signiﬁcant in
GSS as the accuracy is high and there are no errors in most
experiments. Also, when the length of ﬁngerprint becomes
longer, the accuracy of GSS increases.
E. Experiments on Node Query
In this section, we evaluate the performance of GSS in
estimating the accuracy of node query. A node query for a
node v is to compute the summary of the weights of all edges
with source node v. For each dataset, node query set contains
all nodes in the graph stream. Figure 11 shows the ARE of
node queries in data sets email-EuAll, cit-HepPh and web-
NotreDame, respectively. The ﬁgure shows that although we
unfairly ﬁx the ratio of memory used by TCM and GSS, GSS
still can achieve better performance than TCM.
F. Experiments on Reachability Query
In this section, we evaluate the performance of GSS in
supporting reachability queries. Each reachability query set Q
contains 100 unreachable pairs of nodes which are randomly
generated from the graph. Figure 12 shows the true negative
recall of reachability query for the data sets email-EuAll, cit-
HepPh and web-NotreDame, respectively. From the ﬁgures
we can see that the accuracy of GSS is much higher than
TCM even when TCM uses much larger memory. The gap
varies with the size of the graph. Along with increasing the
memory and the length of the ﬁngerprint, GSS can achieve
better performance. We can also see that the accuracy of TCM
is so poor that it can barely support this query.
G. Experiments on Buffer Size
Figure 13 shows the buffer percentage for the three larger
data sets web-NotreDame,lkml-replyand Caida-networkﬂow.
The four curves in the ﬁgure represent 1)GSS with 1 room
in each bucket and no square hashing. 2) GSS with 2 rooms
in each bucket and no square hashing. 3) GSS with 1 room in
each bucket and square hashing. 4) GSS with 2 rooms in each
bucket and square hashing. The x-label, w, is the side length
of the matrices for the schemes with 2 rooms in each bucket.
When GSS has 1 room in each bucket, the width of the matrix
is 20.5 times larger to make the memory unchanged. The
above results show that the decrement in buffer size brought
by using square hashing and multiple rooms is signiﬁcant,
especially the square hashing. The results also show that the
buffer percentage in the fully improved GSS (2 rooms each
bucket, with square hashing) becomes 0 in most experiments
when the matrix size is close to |E|. In this case, the overhead
brought by the insertion failure in the matrix is nearly 0.
H. Experiment on update speed
In this section we evaluate the update speed of GSS. We
compare the update speed of GSS, TCM and adjacency lists,
the result is shown in Table I. The adjacency list is accelerated
using a map that records the position of the list for each node.
Because the update speed changes little with the matrix size,
we only show the average speed here. The ﬁngerprint size
is 16-bit. TCM is still implemented with the same settings as
above experiments. In each data set we insert all the edges into
the data structure, repeat this procedure 100 times and calcu-
late the average speed. The unit we use is Million Insertions


## Page 12


650
700
750
800
850
900
950
1000
Width
600
0.00
0.01
0.02
0.03
0.04
0.05
Edge query ARE
GSS(fsize=12)
GSS(fsize=16)
TCM(8*memory)
(a) email-EuAll
500
600
800
900
1000
700 
Width
400
0.004 
0.003 
0.002 
0.001 
0.000
Edge query ARE
GSS(fsize=12) 
GSS(fsize=16) 
TCM(8*memory)
(b) cit-HepPh
850
900
950
1000
1050
1100
1150
1200
Width
800
0.00
0.01
0.02
0.03
0.04
Edge query ARE
fsize=12
fsize=16
TCM(8*memory)
(c) web-NotreDame
300
400
500
600
700
800
900
1000
Width
0.00
0.02
0.04
0.06
0.08
0.10
0.12
Edge Query ARE
fsize=12
fsize=16
TCM(8*memory)
(d) lkml-reply
5000
6000
7000
8000
9000
10000
Width
0.0
0.2
0.4
0.6
0.8
Edge Query ARE
fsize=12
fsize=16
TCM(8*memory)
(e) Caida-networkﬂow
Fig. 8. Average Relative Error of Edge Queries
700
800
900
1000
1100
1200
Width
0.2
0.4
0.6
0.8
1.0
Average Precision
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(a) email-EuAll
700
800
900
1000
1100
1200
Width
0.7
0.8
0.9
1.0
Average Precision
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(b) cit-HepPh
700
800
900
1000
1100
1200
Width
0.0
0.2
0.4
0.6
0.8
1.0
Average Precision
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(c) web-NotreDame
300
400
500
600
700
800
900
1000
Width
0.0
0.2
0.4
0.6
0.8
1.0
Average Precision
fsize=12
fsize=16
TCM(256*memory)
(d) lkml-reply
5000
6000
7000
8000
9000
10000
Width
0.0
0.2
0.4
0.6
0.8
1.0
Average Precision
fsize=12
fsize=16
TCM(16*memory)
(e) Caida-networkﬂow
Fig. 9. Average Precision of 1-hop Precursor Queries
TABLE I
UPDATE SPEED (MIPS)
Data Structure
email-EuAll
cit-HepPh
web-
NotreDame
GSS
2.2887
2.61057
2.40976
GSS(no sampling)
2.1245
2.49191
2.32015
TCM
2.10417
2.5498
2.07403
Adjacency Lists
0.578596
0.3384
0.52147
per Second (Mips). From the ﬁgure we can see that the speed
of GSS is similar to TCM, because though more memory
accesses are needed, GSS computes less hash functions. Both
of them are much higher than the adjacency list. We also show
the speed of GSS without candidate bucket sampling. We can
see that the speed without candidate sampling is lower than
the full optimized one. The gap is not very large because most
edges ﬁnd empty bucket in few searches.
I. Experiment on Other Compound Queries
We compare GSS with state-of-the-art graph processing
algorithms in triangle counting and subgraph matching in
this Section. We compare GSS with TRIEST [23] in triangle
counting with the same memory. We use relative error between
the reported results and the true value as evaluation metrics.
TRIEST does not support multiple edges. Therefore we unique
the edges in the dataset for it. The results are shown in Figure
14. The results show that they achieve similarly high accuracy
with relative error less than 1%. We compare GSS with SJ-tree
[24] in subgraph matching. As SJ-tree is an accurate algorithm,
we set GSS to
1
10 of its memory. We use VF2 algorithm when
querying in GSS, other algorithms can also be used. We use
web-NotreDame and search for subgraphs in windows of the
data stream. The edges in the graph are labeled by the ports
and the protocol. We carry out experiment on 5 window sizes,
and for each window size, we randomly select 5 windows in
the stream. In each window, we generate 4 kinds of subgraphs
with 6, 9, 12 and 15 edges and 5 instances in each kind by
random walk. We use the correct rate as evaluation metrics,
which means the percentage of correct matches in the 100
matches for each window size. Experimental results are shown
in Figure 15. We can see that GSS has nearly 100% correct
rate. Both TRIEST an SJ-tree have throughput less than 2×105
edges per second, much lower than the update speed of GSS,
and high update speed is important in high speed streams.
VIII. CONCLUSION
Graph stream summarization is a problem rising in many
ﬁelds. However, as far as we know, there are no prior work
that can support all kinds of queries with high accuracy.


## Page 13


700
800
900
1000
1100
1200
Width
0.0
0.2
0.4
0.6
0.8
1.0
Average Precision
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(a) email-EuAll
700
800
900
1000
1100
1200
Width
0.7
0.8
0.9
1.0
Average Precision
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(b) cit-HepPh
700
800
900
1000
1100
1200
Width
0.2
0.4
0.6
0.8
1.0
Average Precision
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(c) web-NotreDame
300
400
500
600
700
800
900
1000
Width
0.0
0.2
0.4
0.6
0.8
1.0
Average Precision
fsize=12
fsize=16
TCM(256*memory)
(d) lkml-reply
5000
6000
7000
8000
9000
10000
Width
0.0
0.2
0.4
0.6
0.8
1.0
Average Precision
fsize=12
fsize=16
TCM(16*memory)
(e) Caida-networkﬂow
Fig. 10. Average Precision of 1-hop Successor Queries
650
700
750
800
850
900
950
1000
Width
600
0
5
10
15
20
Node query ARE
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(a) email-EuAll
500
600
800
900
1000
700 
Width
400
0
1
2
3
4
Node query ARE
GSS(fsize=12) 
GSS(fsize=16) 
TCM(8*memory)
(b) cit-HepPh
850
900
950
1000
1050
1100
1150
1200
Width
800
0
4
8
12
16
Node query ARE
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(c) web-NotreDame
300
400
500
600
700
800
900
1000
Width
0
2
4
6
8
Node Query ARE
fsize=12
fsize=16
TCM(256*memory)
(d) lkml-reply
5000
6000
7000
8000
9000
10000
Width
0
200
400
600
800
Node Query ARE
fsize=12
fsize=16
TCM(16*memory)
(e) Caida-networkﬂow
Fig. 11. Average Relative Error of Node Queries
In this paper, we propose graph stream summarization data
structure Graph Stream Sketch (GSS). It has O(|E|) memory
usage where |E| is the number of edges in the graph stream,
and O(1) update speed. It supports almost queries based on
graphs and has accuracy which is higher than state-of-the-art
by magnitudes. Both mathematical analysis and experiment
results conﬁrm the superiority of our work.
REFERENCES
[1] S. Guha and A. McGregor, “Graph synopses, sketches, and streams: A
survey,” PVLDB, vol. 5, no. 12, pp. 2030–2031, 2012.
[2] G. Cormode and S. Muthukrishnan, “An improved data stream sum-
mary: The count-min sketch and its applications,” in Latin American
Symposium on Theoretical Informatics, pp. 29–38, 2004.
[3] C. Estan and G. Varghese, “New directions in trafﬁc measurement
and accounting: Focusing on the elephants, ignoring the mice,” ACM
Transactions on Computer Systems (TOCS), vol. 21, no. 3, pp. 270–
313, 2003.
[4] P. Roy, A. Khan, and G. Alonso, “Augmented sketch: Faster and more
accurate stream processing,” in SIGMOD, pp. 1449–1463, ACM, 2016.
[5] D. Thomas, R. Bordawekar, C. C. Aggarwal, and S. Y. Philip, “On
efﬁcient query processing of stream counts on the cell processor,” in
ICDE, pp. 748–759, IEEE, 2009.
[6] P. Zhao, C. C. Aggarwal, and M. Wang, “gsketch: on query estimation
in graph streams,” PVLDB, vol. 5, no. 3, pp. 193–204, 2011.
[7] N. Tang, Q. Chen, and P. Mitra, “Graph stream summarization: From
big bang to big crunch,” in SIGMOD, pp. 1481–1496, 2016.
[8] A. Khan and C. Aggarwal, “Query-friendly compression of graph
streams,” in IEEE/ACM International Conference on Advances in Social
Networks Analysis and Mining, pp. 130–137, 2016.
[9] M. Elkin, “Streaming and fully dynamic centralized algorithms for
constructing and maintaining sparse spanners,” in ICALP, pp. 716–727,
Springer, 2007.
[10] V. Braverman, R. Ostrovsky, and D. Vilenchik, “How hard is counting
triangles in the streaming model?,” in ICALP, pp. 244–254, Springer,
2013.
[11] J. Feigenbaum, S. Kannan, A. McGregor, S. Suri, and J. Zhang, “On
graph problems in a semi-streaming model,” Theoretical Computer
Science, vol. 348, no. 2-3, pp. 207–216, 2005.
[12] J. E. Gonzalez, R. S. Xin, A. Dave, D. Crankshaw, M. J. Franklin,
and I. Stoica, “Graphx: Graph processing in a distributed dataﬂow
framework.,” in OSDI, vol. 14, pp. 599–613, 2014.
[13] J. E. Gonzalez, Y. Low, H. Gu, D. Bickson, and C. Guestrin, “Pow-
ergraph: distributed graph-parallel computation on natural graphs.,” in
OSDI, vol. 12, p. 2, 2012.
[14] G. Malewicz, M. H. Austern, A. J. Bik, J. C. Dehnert, I. Horn, N. Leiser,
and G. Czajkowski, “Pregel: a system for large-scale graph processing,”
in SIGMOD, pp. 135–146, ACM, 2010.
[15] Y. Low, D. Bickson, J. Gonzalez, C. Guestrin, A. Kyrola, and J. M.
Hellerstein, “Distributed graphlab: a framework for machine learning
and data mining in the cloud,” PVLDB, vol. 5, no. 8, pp. 716–727,
2012.
[16] S. Raghavan and H. Garcia-Molina, “Representing web graphs,” in
ICDE, pp. 405–416, IEEE, 2003.


## Page 14


600
650
700
750
800
850
900
950
1000
Width
0.0
0.2
0.4
0.6
0.8
1.0
True negative recall
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(a) email-EuAll
400
500
600
700
800
900
1000
Width
0.0
0.2
0.4
0.6
0.8
1.0
1.2
True negative recall
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(b) cit-HepPh
800
850
900
950
1000
1050
1100
1150
1200
Width
0.0
0.2
0.4
0.6
0.8
1.0
True negative recall
GSS(fsize=12)
GSS(fsize=16)
TCM(256*memory)
(c) email-EuAll
300
400
500
600
700
800
900
1000
Width
0.0
0.2
0.4
0.6
0.8
1.0
True Negative Recall
fsize=12
fsize=16
TCM(256*memory)
(d) cit-HepPh
5000
6000
7000
8000
9000
10000
Width
0.0
0.2
0.4
0.6
0.8
1.0
True Negative Recall
fsize=12
fsize=16
TCM(16*memory)
(e) web-NotreDame
Fig. 12. True Negative Recall of Reachability Queries
800
850
900
950
1000
1050
1100
1150
1200
Width
0.0
0.2
0.4
0.6
0.8
1.0
Buffer Percentage
Room=1
Room=2
Room=1(NoSquareHash)
Room=2(NoSquareHash)
(a) web-NotreDame
300
400
500
600
700
800
900
1000
Width
0.0
0.1
0.2
0.3
0.4
Buffer Percentage
Room=1
Room=2
Room=1(NoSquareHash)
Room=2(NoSquareHash)
(b) lkml-reply
5000
6000
7000
8000
9000
10000
Width
0.00
0.02
0.04
0.06
0.08
Buffer Percentage
Room=1
Room=2
Room=1(NoSquareHash)
Room=2(NoSquareHash)
(c) Caida-networkﬂow
Fig. 13. Buffer Percentage
2.5
3.0
3.5
4.0
4.5
5.0
Memory(MB)
0.000
0.005
0.010
0.015
0.020
Relative Error
GSS 
TRIEST
Fig. 14. Triangle count in cit-HepPh
10000     20000      30000      40000      50000
Windowsize
0.85
0.90
0.95
1.00
1.05
1.10
Correct Rate
GSS
SJtree
Fig. 15. Subgraph matching in web-NotreDame
[17] W. Fan, J. Li, X. Wang, and Y. Wu, “Query preserving graph compres-
sion,” in SIGMOD, pp. 157–168, ACM, 2012.
[18] D. A. Spielman and N. Srivastava, “Graph sparsiﬁcation by effective
resistances,” SIAM Journal on Computing, vol. 40, no. 6, pp. 1913–
1926, 2011.
[19] J. Gao, C. Zhou, J. Zhou, and J. X. Yu, “Continuous pattern detection
over billion-edge graph using distributed framework,” in ICDE, pp. 556–
567, IEEE, 2014.
[20] C. Wang and L. Chen, “Continuous subgraph pattern search over graph
streams,” in ICDE, pp. 393–404, IEEE, 2009.
[21] C. Song, T. Ge, C. Chen, and J. Wang, “Event pattern matching over
graph streams,” PVLDB, vol. 8, no. 4, pp. 413–424, 2014.
[22] P. LEcuyer, “Tables of linear congruential generators of different sizes
and good lattice structure,” Mathematics of Computation, vol. 68,
no. 225, pp. 249–260, 1999.
[23] L. D. Stefani, A. Epasto, M. Riondato, and E. Upfal, “Triest:counting
local and global triangles in fully-dynamic streams with ﬁxed memory
size,” in ACM SIGKDD International Conference on Knowledge Dis-
covery and Data Mining, pp. 825–834, 2016.
[24] S. Choudhury, L. Holder, G. Chin, K. Agarwal, and J. Feo, “A selectivity
based approach to continuous pattern detection in streaming graphs,”
Computer Science, vol. 93, no. 8, pp. 939–945, 2015.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
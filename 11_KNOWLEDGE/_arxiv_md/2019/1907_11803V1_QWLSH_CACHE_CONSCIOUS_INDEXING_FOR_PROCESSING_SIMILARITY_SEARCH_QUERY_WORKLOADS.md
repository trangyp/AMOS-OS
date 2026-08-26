---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1907.11803v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1907.11803v1_qwLSH__Cache-conscious_Indexing_for_Processing_Similarity_Search_Query_Workloads

> Source: 1907.11803v1_qwLSH__Cache-conscious_Indexing_for_Processing_Similarity_Search_Query_Workloads.pdf

> Pages: 9

---


## Page 1


qwLSH: Cache-conscious Indexing for Processing
Similarity Search Query Workloads in
High-Dimensional Spaces∗
Omid Jafari
ojafari@nmsu.edu
New Mexico State University
Las Cruces, New Mexico
John Ossorgin
osso09@nmsu.edu
New Mexico State University
Las Cruces, New Mexico
Parth Nagarkar
nagarkar@nmsu.edu
New Mexico State University
Las Cruces, New Mexico
Abstract
Similarity search queries in high-dimensional spaces are
an important type of queries in many domains such as im-
age processing, machine learning, etc. Since exact similarity
search indexing techniques suffer from the well-known curse
of dimensionality in high-dimensional spaces, approximate
search techniques are often utilized instead. Locality Sensi-
tive Hashing (LSH) has been shown to be an effective approx-
imate search method for solving similarity search queries in
high-dimensional spaces. Often times, queries in real-world
settings arrive as part of a query workload. LSH and its vari-
ants are particularly designed to solve single queries effec-
tively. They suffer from one major drawback while executing
query workloads: they do not take into consideration impor-
tant data characteristics for effective cache utilization while
designing the index structures. In this paper, we present
qwLSH, an index structure for efficiently processing simi-
larity search query workloads in high-dimensional spaces.
We intelligently divide a given cache during processing of a
query workload by using novel cost models. Experimental
results show that, given a query workload, qwLSH is able
to perform faster than existing techniques due to its unique
cost models and strategies.
Keywords
Nearest-neighbor Search, Locality Sensitive Hash-
ing, High-dimensional Search
1
Introduction
The similarity search problem in high-dimensional spaces
is a well-known problem with wide-ranging applications in
domains such as information retrieval, artificial intelligence,
machine learning, etc. Exact tree-based spatial indexing tech-
niques, such as KD-tree, R-tree, SR-tree, etc., are effective
for improving searching in low-dimensional spaces, but as
the dimensions increase (∼>10), they all suffer from the pop-
ular curse of dimensionality problem (where they are often
outperformed even by a brute force linear scan) [9]. One ap-
proach to addressing this curse of dimensionality problem is
to search for approximate solutions instead of exact solutions.
In many applications, where 100% accuracy is unnecessary,
good enough results are acceptable. Approximate solutions
∗This work is supported by NSF #1633330
0.68
0.82
0.87
0.92
0.6
0.7
0.8
0.9
1
25
50
100
250
IndexIO/TotalIO
Dataset Cardinality (in 1000s)
Effect of Cardinality 
on the IndexIO/TotalIO [Dim.=1500]
Figure 1. Effect of Cardinality over the ratio IndexIO/TotalIO.
We create versions of the Deepsat dataset (see Section 6
for more details) with different cardinalities but same dim.
[=1500] for 250 top-50 queries using QALSH alg. [11].
sacrifice accuracy for a much faster performance. Formally,
the goal of the approximate version of the similarity search
problem, also called c-approximate Nearest Neighbor search,
is to return the objects that are within the distance c ×R from
the query object, where c > 1 is an approximate ratio and R
is the distance from the query to the true nearest neighbor.
1.1
Locality Sensitive Hashing
Locality Sensitive Hashing, first proposed in [14], is one of
the most popular solutions for approximate searching in
high-dimensional spaces. The purpose of Locality Sensitive
Hashing (LSH) is to map high-dimensional data to lower
dimensions while preserving the distances in the original
space. The lower dimensional space is generated through a
series of random projections. In this lower dimensional space,
data objects are mapped to individual buckets based on a
hash function, with the intuition that nearby data points
in the original space are mapped to the same hash buckets
in the lower dimensional space with a higher probability
than mapping dissimilar or far away points to the same
buckets. This may lead to misses and false positives. Given a
distance metric and a corresponding LSH family (detailed in
Section 3), LSH data structures control their precision and
recall by using multiple independently chosen hash functions
organized into several hash layers. Since the original work
[14] was proposed, there has been considerable amount of
research done on improving Locality Sensitive Hashing [4, 9–
11, 13, 15, 24, 26, 30].
arXiv:1907.11803v1  [cs.DB]  26 Jul 2019


## Page 2


0.01
0.06
0.18
0.38
0
0.1
0.2
0.3
0.4
50
500
1500
3136
DataIO/TotalIO
Dataset Dimensionality
Effect of Dimensionality 
on the DataIO/TotalIO [Card.=50K]
Figure 2. Effect of Dimensionality over DataIO/TotalIO over
the Deepsat dataset with different dimensionalities but same
card. [=50K] for 250 top-50 queries using QALSH alg. [11].
1.2
Motivation
Often times, in real-world settings, queries arrive as part of
a query workload. Several research works have shown the
benefits of designing index structures particularly for effi-
cient handling of query workloads [3, 8, 17, 18, 20, 27]. Most
of these works focus on partitioning the data space such that
regions that are queried with high frequency are partitioned
with more granularity. e.g., in 2D geographical spaces, points
of interest in downtown areas are queried with much more
frequency than places in the suburbs. Similarly, consider the
following two scenarios for high-dimensional data: (1) Ge-
nomic DNA data, often represented as high-dimensional vec-
tors, require similarity search queries to find similar genomes
given a query genome [5, 7, 22]. Certain common genome
sequences are often queried more times than the rest [22]. (2)
Similarly, earthquake detection or satellite image data, both
high-dimensional data [6, 28], often query certain similar
regions of the space that are of more interest. These queries
can be viewed as part of a query workload. While LSH has
been shown to be effective in processing single queries in
high-dimensional spaces, it is not particularly designed to
handle query workloads efficiently.
Assuming that the index and the data are stored on an
external storage, Locality Sensitive Hashing and its variants
have two main IO operations: (1) accessing the index (de-
noted by IndexIO) in order to find the candidates, and (2)
once the candidates are found, the candidate points need to
be brought from the external storage (denoted by DataIO)
into the main memory to remove false positives. We observe
that these two operations, however, have different costs:
• the IndexIO cost is dependent on the size of the index,
which is in turn dependent on the size of the dataset (also
referred to as cardinality of the dataset), and
• the dataIO cost is dependent on the size of each data point,
i.e. the number of dimensions of the dataset, and the de-
sired number of objects in the result (top-k).
Figures 1 and 2 show our observation. In Figure 1, it can be
seen that as the cardinality of the dataset increases (when the
dimensionality is fixed), the ratio of IndexIO/TotalIO (where
TotalIO = IndexIO + DataIO) increases, because the cost of
IndexIO increases. Similarly, in Figure 2, it can be seen that
as the dimensionality increases, the ratio of DataIO/TotalIO
increases, because the cost of DataIO increases. By using this
important observation, the efficiency of an LSH algorithm
can be further improved by intelligently utilizing the cache
for a given query workload. In this paper, we propose qwLSH,
an index structure that improves the performance of query
workloads in high-dimensional spaces by improving upon
the cache utilization of the system.
1.3
Contributions of this paper
Existing LSH-based index structures are designed to effi-
ciently handle single queries. Given a query workload, they
naively process the queries in the query workload individ-
ually, independent of each other. There is a need for index
structures that can improve the performance of a query work-
load by taking into consideration the important characteris-
tics of the workload. In this paper, we present our proposed
index structure, qwLSH, that can efficiently process similar-
ity search query workloads in high-dimensional spaces. The
following are the contributions of this paper:
• Given the important observation, that different data have
different query processing needs, we intelligently divide a
given cache for efficient processing of a query workload
• We present novel cost models for intelligently dividing a
cache given a query workload
• We present different cache utilization strategies for LSH-
based query workloads
• Finally, we use real datasets to show the efficiency of our
proposed index structure, qwLSH, by comparing against
state-of-the-art algorithms.
To the best of our knowledge, there are no existing works
that particularly tackle the problem of solving query work-
loads in high-dimensional spaces in an efficient manner. In
this paper, we present the design and analysis of qwLSH that
was particularly designed to efficiently execute query work-
loads in high-dimensional spaces. The paper is organized as
follows: in Section 2, we present the related works. In Section
3, we present the key concepts and preliminaries necessary
to understand the problem domain and qwLSH. In Sections 4
and 5, we formalize the problem statement and explain the
design of qwLSH respectively. We present our experimental
analysis in Section 6 and finally conclude in Section 7.
2
Related Work
Similarity search queries in high-dimensional spaces have
wide-ranging applications in various domains such as multi-
media retrieval, artificial intelligence, etc. Exact tree-based
index structures (such as R-trees, KD-trees, etc.) work ef-
ficiently for low-dimensional data, but as the dimensions
increase (∼> 10), their performance degrades and are of-
ten outperformed by brute-force linear scans (a well-known
problem called the curse of dimensionality) [14]. Approxi-
mate techniques were proposed where the performance of
the queries was drastically improved by trading off some


## Page 3


accuracy of the query result. Locality Sensitive Hashing, first
proposed in [14], is a popular approximate technique for
solving similarity search queries in high-dimensional spaces.
The original work was proposed to solve the (R, c)-Near
Neighbor problem, which is a decision-based version of the
Approximate Nearest Neighbor problem [9]. While the LSH
family (explained further in Section 3) in [14] was originally
defined for the Hamming distance, it was later defined for
other distance measures such as the Euclidean distance [9].
Effective Variants of LSH: LSH has been shown to be use-
ful in various domains such as biomedical sciences [5, 7, 22],
geological sciences [6, 28], etc. Several works were subse-
quently proposed [4, 10, 11, 13, 15, 16, 24, 26] to improve
upon the original work. In [4], the authors created a prefix-
tree of hash functions for each hash layer to appropriately
decide on the number of hash functions to use during query
processing in order to return the desired number of top-k
results. In [16], the authors propose a probing technique
to look into neighboring buckets of the query point’s hash
bucket, and hence instead of creating more number of layers
to get the desired number of top-k results, their technique
probes into neighboring buckets. In [26], the authors repre-
sent each of the points in the lower dimensional space using
Z-order (also called Morton) codes which are then further
retrieved effectively by finding the closeby points based on
the distances between their Z-order codes. While these tech-
niques improve upon the original LSH and its most popular
implementation, E2LSH1, they still suffer from having large
index sizes and slow processing speeds. Recently, in [10],
the authors presented C2LSH, in which they proposed two
novel ideas: a “collision counting" approach that counted
the number of times a candidate object is mapped to the
same bucket and a “virtual rehashing" approach that auto-
matically incremented the lookup space in each projection
without having the need to physically rehash the data. In
[11], the authors analyzed the data distribution and created
indexes of different granularity to make their index struc-
ture scalable for different data with different distributions.
In [24], a projection-based method that uses only 6 to 10 ran-
dom projections is presented. While the index size is much
smaller than [10] and [13], the accuracy is much worse and
it is shown to be unstable [13]. In [15], the authors present
SK-LSH, where they propose a novel linear order on the
index files stored on the external storage based on their Z-
order codes. The idea is that if nearby index files are stored
contiguously on the external storage, then the number of
I/Os will be reduced. In [13], the authors build upon the
“collision counting” and the “virtual rehashing” approaches
presented in [10] by proposing to create “query-aware” hash
functions. QALSH builds B-trees on every hash function, and
then given a query object, perform range searches on each of
1https://www.mit.edu/~andoni/LSH/
the B-trees. This method has shown to be the most accurate
and fast LSH-based technique [11].
Query Workloads: Many index structures and systems
have been particularly designed to execute query workloads
efficiently [3, 8, 17, 18, 20, 27]. [8, 19] uses data partitioning
techniques that are query workload-aware on 1D data. In [1–
3, 27], the authors present different query workload-aware
partitioning techniques for existing data structures, such
as R-trees, on 2D spatial data. In [17] and [18], the authors
present unique cost models to bring in the most relevant part
of the index structures into the main memory for future use
based on past query workload statistics for 1D and 2D space
respectively. The above works deal with data partitioning
techniques for 1D and 2D data. To the best of our knowl-
edge, there is no existing work that deals with improving the
efficiency of query workloads in high-dimensional spaces.
Cache-Conscious Querying: There have been several works
that design techniques to reduce cache misses to improve the
query performance [12, 21, 23]. An experimental survey on
cache conscious algorithms can be found at [29]. In the do-
main of LSH and its variants, there is one main work that has
attempted making LSH cache-conscious [25]. The authors
present a caching strategy to improve the index construction
cost. Their main goal is to speed up indexing (and searching)
over streaming Twitter data in a distributed environment. In
the caching strategy presented in their work, the authors
present a hierarchical 2-level hashing approach to reduce
cache misses during the index construction phase. During
query processing, the authors utilize the cache by “software
prefetching", i.e., by prefetching succeeding data items into
the cache. Our cache utilization strategies are very different
than the techniques used in [25]. Our strategies are based
on the important observation as explained in Section 1.2,
and our main goal is to speed up the processing speed of the
entire query workload, which is different from [25].
3
Key Concepts and Preliminaries
In this section, we present the key concepts underlying LSH.
We rely mainly on the terminologies presented in E2LSH2,
C2LSH [10], and QALSH [11].
Let D be a database of n data objects in a d-dimensional
Euclidean space Rd. Let ∥o1,o2∥denote the Euclidean dis-
tance between two objects o1 and o2. Given a query object q
in Rd, the c-ANN search (for an approximation ratio c > 1)
returns all objects o ∈D such that ∥o,q∥≤c × ∥o∗,q∥,
where o∗is the true nearest neighbor of q in D. Similarly,
the c-k-ANN problem finds the top-k objects oi ∈D where
1 ≤i ≤k, and such that ∥oi,q∥≤c × ∥o∗
i ,q∥, where o∗
i is
the true ith nearest neighbor of q.
Definition 3.1 (A Locality Sensitive Hashing Family). A
hash function family H is said to be (r,c, P1, P2)-sensitive if
2https://www.mit.edu/~andoni/LSH/


## Page 4


it satisfies all following conditions for any two points x and y
in a dataset D ⊂Rd:
• if |x −y| ≤r, then Pr[h(x) = h(y)] ≥P1, and
• if |x −y| > cr, then Pr[h(x) = h(y)] ≤P2
Here, c is an approximation ratio, P1 and P2 are probabili-
ties, r is the distance between two points commonly referred
to as the radius, and in order for the definition to work, c > 1
and P1 > P2. The above definition states that the two points
x and y are hashed to the same bucket with a very high prob-
ability ≥P1 if they are close to each other (i.e. the distance
between the two points is less than or equal to r), and if they
are not close to each other (i.e. the distance between the two
points is greater than cr), then they will be hashed to the
same bucket with a low probability ≤P2.
In the original LSH scheme for Euclidean distance, each
hash function is defined as ha,b(v) = a.v+b
w
, where a is a
d-dimensional random vector with entries chosen indepen-
dently from the standard normal distribution and b is a real
number chosen uniformly from [0,w), such that w is the
width of the hash bucket [9]. This leads to the following
collision probability function [15]:
P(r) =
∫w
0
1
r
2
√
2π
e
−t2
2r2 (1 −t
w )dt.
(1)
Note that the collision probability is governed by the width,
w, of the hash bucket: if the size is chosen to be much larger
than the query radius, then there can be a lot of candidates
generated. If the size is chosen to be much smaller than the
query radius, then there can be potentially several misses.
3.1
Collision Counting
C2LSH [10] introduced the technique of “collision counting”
because of which it is not necessary to have l hash layers.
Instead of hash layers, the index requires m hash functions
and a collision count threshold to find the candidate points.
From here on, since each hash function can be viewed as
a single hash layer, we use the terms hash layers and hash
functions interchangeably.
Recent LSH variants (such as C2LSH [10], QALSH [13],
etc.) have an upper bound on the number of candidate objects
returned, i.e., the number of data points that have to be
brought from the external storage into the main memory.
This bound is often controlled by a user-input, “allowed" false
positives, v. Intuitively, higher the v, less time is needed to
find the candidate objects, and vice-versa. As a good trade-off,
these works set v = 100, which is what we continue using
in our work as well. Thus, for a maximum k (i.e. the desired
number of output results) of 100, the maximum number of
data objects that will be read from the disk will be 200 (since
k + v = 200). The basic LSH formulation does not have an
upper bound on the number of candidate points that are
needed to be accessed from the external storage.
4
Problem Specification
In this paper, our goal is to create an efficient index struc-
ture to execute similarity search query workloads in high-
dimensional spaces. Let us consider we are given a query
workload Q that consists of q queries, where ∀q ⊂D. For
each query q ∈Q, given k and an approximation ratio c > 1,
we return the top-k results such that ∥oi,q∥≤c × ∥o∗
i ,q∥,
where o∗
i is the true ith nearest neighbor of q.
As mentioned in Section 1.2, our goal is to leverage the
important observation that datasets with different cardinali-
ties and dimensionalities have different IO costs, and then
design the cache such that it is most effectively utilized for a
given query workload.
Given a cache C, our goal is to divide the cache into two
parts:CI andCD, whereCI is the part of the cache that stores
the index files (i.e. data from the hash buckets) and CD is
the part of the cache that stores the data objects, such that
size(C) = size(CI) + size(CD). Assume cost(C) denotes the
cost of bringing all necessary files (index files + data ob-
jects) into the cache C. Similarly, cost(CI) denotes the cost of
bringing the index files into the cache, and cost(CD) denotes
the cost of bringing the data objects into the cache, such
that cost(C) = cost(CI) + cost(CD). In order to understand
the design of qwLSH, we need to first understand the costs,
cost(CI) and cost(CD), in detail.
cost(CI ): Let us first consider the cost of bringing all nec-
essary index files into CI for a single query, q. Note that,
we have m projections in our index. Let us assume that the
cost for bringing necessary index files for ith projection is:
cost(Cq
Ii ). Also, the amount of data that is read from the index
files is a function of the cardinality of the dataset (Figure 1).
Let us denote this constant as αcard. Thus, we have:
cost(CI) = αcard ×
m
Õ
i=1
(cost(Cq
Ii ))
(2)
cost(CD): Similarly, let us first consider the cost of bringing
all necessary data objects into CD for a single query, q. Note
that, as explained in Section 3, for a single query, the worst
case scenario would be to have to read k+v data objects from
the external storage. Let us denote this as w (i.e. w = k + v).
Let us denote the cost of reading a single jth data object as
cost(Cq
Dj ). The size of each data object is a function of the
dimensionality of the dataset (Figure 2). Let us denote this
constant as αdim. Thus, we have:
cost(CD) = αdim ×
w
Õ
j=1
(cost(Cq
Dj ))
(3)
Note that the above costs are for a single query. When we
have more than 1 query in the given query workload Q,
assuming that there will be at least 1 index file that will be
reused within the queries, cost(CI) will depend on the size of
CI . If a large amount ofC is dedicated toCI , then the cost(CI)
will be less and vice-versa. Conversely, cost(CD) will depend


## Page 5


(a) Strategy 1
(b) Strategy 2
Figure 3. Different Strategies for designing the cache
25K
50K
100K
250K
0
20
40
60
80
100
50
250
500
1500
3136
Cardinality
Optimal Setting for Index Cache 
Size (in % of Total Cache Size)
Dimensionality
Optimal Setting for Index 
Cache Size [DeepSat dataset]
25K
50K
100K
250K
Figure 4. Optimal Setting for Index Cache Size (in % of
the Total Available Cache Size) on different versions of the
Deepsat dataset [16MB Cache Size, |Q|=250]
0
200
400
600
800
0
20
40
60
80
100
TotalIO (in MB)  
Index Cache Size Setting (in %)
Effect of Index Cache Size 
Setting on IO [P53 Dataset]
IndexIO
DataIO
TotalIO
Figure 5. Effect of Index Cache Size Setting on the In-
dexIO, DataIO, and TotalIO for P53 dataset [16MB Cache
Size, |Q|=250]
on the size of CD. Thus, given a query workload Q, we want
to find size(CI) (or size(CD)) such that cost(C) is minimized:
minimize
|Q|
Õ
д=1

αcard ×
m
Õ
i=1
(cost(Cд
Ii ))
+
αdim ×
w
Õ
j=1
(cost(Cд
Dj ))

subject to
size(CI) = size(C) −size(CD).
5
qwLSH
In this section, we describe our proposed index structure,
qwLSH. Given a query workload, our goal is to intelligently
divide the cache based on the cardinality and dimensionality
of the given dataset. In order to do this, we leverage the
detailed cost model presented in Section 4. In this section,
we will present the two strategies for dividing the cache,
along with unique cost models.
Naive Solution: In LSH (and its variants), the cache is not
intelligently divided into two parts: CI and CD. For a given
query workload, the cache (using the default cache replace-
ment policy, such as MRU) will treat the index files and the
data object files equal, regardless of the cardinality and the
dimensionality of the dataset. As shown in Figures 1 and 2,
the cardinality and the dimensionality of the dataset affects
the total size of index files that are read into the cache and
the total size of data objects respectively. We leverage this ob-
servation that naive solutions do not. In Section 6, we show
the benefit of leveraging this observation into designing the
cache intelligently.
5.1
Design of qwLSH
For each query, LSH index structures access each of the m
hash functions in order to find the candidate data object IDs.
Once the candidate data object IDs are found for the query,
the data objects are brought from the external storage in
order to remove the false positives. Given the total cache
size, our goal is to find how much of the total cache size to
allocate to the index cache, CI , and the data cache, CD. Once
we determine the appropriate split between CI and CD, we
use the popular cache replacement policy, MRU, to decide
which index files need to be evicted from CI and which
data files need to be evicted from CD. With the intuition
that queries in query workloads are often times near each
other [3, 18], we choose to use MRU. Before we present the
cost models that we used to determine the appropriate split
between CI and CD, we first present two strategies based on
how the index files are accessed and cached.
Strategy 1: In this strategy, the index cache, CI, is further
divided uniformly between the m hash functions, as shown
in Figure 3a. In each of the sub-index cache, we have an MRU
replacement policy specific to the sub-index cache.
Strategy 2: In this strategy, the index cache,CI , is not further
divided uniformly between the m hash functions, as shown
in Figure 3b. We have a single MRU replacement policy for
the index cache that stores (and if needed, evicts) index files
from different hash functions.
In both strategies, there is a separate MRU replacement policy
for the data cache, CD. The intuition behind Strategy 1 is
that each projection will use the cache uniformly. On the
other hand, the intuition behind Strategy 2 is that some
projections might require bringing more hash buckets into
the cache than others (which would be the case when the data


## Page 6


distribution is skewed or the usage of individual projections
is different).
5.2
Cost Models of qwLSH
We have seen in Figures 1 and 2 that the cardinality and
dimensionality of the dataset affects the size of index files
and data files that need to be read into the cache respectively.
In order to determine the appropriate split between the index
cache, CI, and the data cache, CD, we train a model based
on the size of index files and data files that are read from
the external storage for different settings (cardinality and
dimensionality) on the DeepSat dataset. Figure 4 shows the
optimal setting of the index cache size for different dataset
characteristics that returns the least amount of total IO. This
model validates our observation that different data charac-
teristics utilize the cache differently. For instance, datasets
with low dimensionality (=50) require more index cache uti-
lization (≥80%) since the data points are small in size. On
the contrary, datasets with low cardinality (≤100K) and high
dimensionality (≥500) require less index cache utilization
since the data points are large in size and the number of
index files needed to be brought in memory are low. Hence,
it is beneficial to cache more data points than index files to
reduce the total amount of IO.
Figure 5 shows the effect of different Index Cache size set-
ting on the IndexIO, DataIO, and the TotalIO for P53 dataset.
As the Index Cache size setting increases (i.e. more % of the
cache is allocated to the index cache), as expected, the DataIO
cost increases while the IndexIO cost decreases. When In-
dex Cache size setting is at 40%, the system incurs the least
amount of IO while processing the entire query workload.
The model presented in Figure 4 also estimates the Index
Cache size setting for P53 dataset to be at 40%. Our model
is dependent on the cache size and the number of queries
in the query workload. We show in Section 6 that our novel
index structure can still adapt for different cache sizes and
number of queries.
5.3
Workflow of qwLSH
In order to find the optimal index cache size for efficient
utilization of the cache, we have to first generate a training
model that shows the behavior of different cache sizes for
different dataset settings (Figure 4). Note that, this process is
done offline and does not require the knowledge of the query
workloads beforehand. During query processing, once we
know the characteristics of the dataset (i.e. the cardinality
and dimensionality), we refer to our model to determine
the index cache size and the data cache size. Note that, the
underlying LSH index (that is stored on the disk) is not
changed. In qwLSH, we use a linked list (to decide which
objects to evict or store in the cache) and an unordered hash
map (for fast retrieval of the objects). In Section 6, we show
that this overhead is minimal and the gains achieved from
our novel models outweigh the cost of the overhead.
Parameter
Value range
# of Queries in Query Workload (|Q|)
50; 100; 250;
Total Cache Size (in MB)
8; 16; 20;
Table 1. Parameters and Default Values (in bold)
0
450
900
1350
1800
0
20
40
60
80
100
TotalIO (in MB)
Top-k Value
Effect of k on Audio 
[16MB Cache, |Q|=250]
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
Figure 6. Effect of varying top-k on Audio dataset [16MB
Cache, |Q|=250]
0
350
700
1050
1400
0
20
40
60
80
100
TotalIO (in MB)
Top-k Value
Effect of k on P53 
[16MB Cache, |Q|=250]
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
Figure 7. Effect of varying top-k on P53 dataset [16MB
Cache, |Q|=250]
6
Experimental Evaluation
In this section, we evaluate the effectiveness of our proposed
index structure, qwLSH. For these evaluations, we use several
real data sets with different cardinality and dimensionality,
under different system parameters. All experiments were run
on machines with the following specifications: Intel Core
i7-6700, 16GB RAM, 2TB HDD, and Ubuntu 16.04 operating
system. The reported results are an average of 5 runs. We
used the state-of-the-art QALSH [11] as our base implemen-
tation3. All codes were written in C++-11. We implement a
cache in the existing QALSH code. For all following alterna-
tives, we use the default settings of QALSH (c = 2, w = 2.719,
δ = 1/e) that are mentioned in [11].
Since there is no work that directly aims at solving our prob-
lem, we compare our work with the following alternatives:
• QALSH_Naive: We compare against the baseline QALSH
algorithm.
3qwLSH can be implemented over any state-of-the-art LSH variant.


## Page 7


1,517.74
38.79
588.04
28.43
28.43
0
400
800
1200
1600
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
Audio [16MB Cache, |Q|=250, k=50]
3,656.78
1,953.32
2,729.27
1,953.91
1,953.91
0
1000
2000
3000
4000
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
LabelMe [16MB Cache, |Q|=250, k=50]
1,041.33
430.13
157.22
154.66
157.22
0
300
600
900
1200
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
P53 [16MB Cache, |Q|=250, k=50]
7,122.13
5,255.81
6,140.35
5,255.81
5,255.81
0
2000
4000
6000
8000
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
Sift [16MB Cache, |Q|=250, k=50]
Figure 8. Comparison of qwLSH (TotalIO) against its alternatives (for different real datasets) and default settings
1,517.74
609.30
1,063.23
609.30
689.98
0
400
800
1200
1600
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
Audio [8MB Cache, |Q|=250, k=50]
1,041.33
433.39
501.04
396.10
431.93
0
300
600
900
1200
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
P53 [8MB Cache, |Q|=250, k=50]
1,517.74
38.44
357.84
17.81
18.41
0
400
800
1200
1600
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
Audio [20MB Cache, |Q|=250, k=50]
1,041.33
427.47
122.70
103.65
103.65
0
300
600
900
1200
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
P53 [20MB Cache, |Q|=250, k=50]
Figure 9. Comparison of qwLSH (TotalIO) for varying cache size against its alternatives (for Audio and P53 datasets)
319.21
17.53
114.95
14.74
17.09
0
90
180
270
360
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
Audio [16MB Cache, |Q|=50, k=50]
226.36
90.77
15.78
15.78
15.78
0
70
140
210
280
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
P53 [16MB Cache, |Q|=50, k=50]
626.94
23.14
234.43
17.94
24.29
0
175
350
525
700
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
Audio [16MB Cache, |Q|=100, k=50]
446.15
175.93
41.31
39.24
41.31
0
125
250
375
500
QA_Naive
QA_Ci
QA_CiCd
QA_Opt
qwLSH
TotalIO (in MB)
P53 [16MB Cache, |Q|=100, k=50]
Figure 10. Comparison of qwLSH (TotalIO) for varying number of queries against its alternatives (for Audio and P53 datasets)
• QALSH_Ci: In this alternative, we allocate the maximum
size of 99% (of the total cache size) to CI. Hence, CD will
have 1% of the total cache size allocation.
• QALSH_Cd: Here, we allocate the maximum size of 99%
(of the total cache size) to CD. Hence, CI will have 1% of
the total cache size allocation.
• QALSH_CiCd: In this alternative, we equally divide the
cache into CI and CD, i.e. we allocate 50% (of the total
cache size) to CI and 50% to CD.
• QALSH_Opt: We try 11 different settings for CI (CI =
1, 10, 20, ..., 90, 99) and report the most efficient setting.
6.1
Datasets
In order to train our models, we needed a large dataset with
high-cardinality and high-dimensionality. Due to the lack of
such datasets, we followed the same technique used to gener-
ate the Mnist4 dataset by downloading 324,000 images from
the Deepsat dataset (that consists of airborne images of dif-
ferent land surfaces)5. Each image has 28*28 pixels. For each
pixel, we store the RGB and Near-Infrared value, and hence
for each image, we get a 28*28*4=3136-dimensional point.
From this dataset, we generated 20 different datasets (with
different cardinalities and dimensionalities) to create our
model (Figure 4). In order to test our model and the effective-
ness of qwLSH, for our experiments, we used the following
four commonly used real high-dimensional datasets:
4http://yann.lecun.com/exdb/mnist/
5https://www.kaggle.com/crawford/deepsat-sat6/home
• Audio6 This dataset consists of 54387 192-dimensional
points. It consists of human-labled sound clips.
• LabelMe7 This dataset consists of 181093 512-dim. points.
• P538 This dataset consists of 31008 5409-dimensional points.
Since our test dataset consisted of only 3136 dimensions,
we reduce the dimensionality of each point to 3000.
• Sift9 This dataset consists of 250,000 128-dim. points.
6.2
Evaluation Criteria and Parameters
Note that, our goal is not to improve the accuracy of the
queries in the query workload, but to improve the total run-
time of the query workload. Since we do not change the logic
of the LSH algorithm, the accuracy of each query executed
in qwLSH is the same as the accuracy of the underlying LSH
algorithm. Hence, due to space limitations, we do not report
the accuracy of the individual queries. For that, we ask the
reader to refer to the QALSH paper [11]. We evaluate the
effectiveness of qwLSH by comparing the size of the data
(i.e. the index files and the data objects) that is needed to be
brought into the cache. We do not report the index size or
the index construction cost, since they would be the same as
the underlying LSH implementation that we use, which in
our case is QALSH [11]. We focus on one specific criterion:
size of the data that is needed to be brought into the cache.
6http://www.cs.princeton.edu/cass/audio.tar.gz
7http://labelme.csail.mit.edu/Release3.0/browserTools/php/dataset.php
8https://archive.ics.uci.edu/ml/datasets/p53+Mutants
9http://corpus-texmex.irisa.fr/


## Page 8


On our test datasets, we found that Strategy 1 and Strategy
2 (Section 5.1) gave similar results (mostly because of the
fact that QALSH treats each projection as the same, i.e., the
number of hash buckets brought into the main memory is
the same for each projection). Due to space constraints, we
only evaluate Strategy 1 and compare with the alternatives
presented earlier in this section.
Table 1 shows our default parameter settings and the differ-
ent ranges that we consider. We generate query workloads
by choosing queries from dense regions of the dataset (that
reflects our motivation and prior works [3]). We chose the
maximum cache size setting based on [25].
6.3
Discussion of the Performance Results
We first show the effect of different values of top-k for the
Audio and the P53 dataset in Figures 6 and 7 respectively.
From these figures, it can be seen that k does not have a no-
ticeable effect on the performance of the algorithms. Hence,
in further charts, we only consider k=50 due to space limi-
tations and for simplicity purposes. In our experiments, we
also observed that the alternative, QALSH_Cd, always gave
the worst result (because of insufficient space to cache the
index files). Hence we also omit QALSH_Cd from the charts.
In Figure 8, we compare qwLSH against all alternatives
on the 4 real datasets for the default settings [16MB cache,
|Q|=250]. While for Audio, LabelMe, and Mnist, our proposed
model always matches with the optimal setting (QA_Opt),
QA_Opt for P53 returns a slightly lower IO than qwLSH
(154.66 vs. 157.22). This is because our model returns an
Index Cache size setting of 45.41%. Since we only compare the
setting sizes with increments of 10 (i.e. for 40% and 50%), our
model does not return the most optimal answer. Even with
this small drawback, the difference between the IOs is small.
For LabelMe and Sift, the Index Cache size setting of 99% is
always the most optimal because the IndexIO cost is always
very dominant. Due to this reason (and space limitations),
we only present the results for Audio and P53 datasets in our
next experiments.
Effect of Varying Total Cache Size: Figure 9 shows the
effect of different cache sizes on qwLSH and its proposed
models. It can be seen that our proposed model can adapt to
different cache sizes. While qwLSH does not always return
the most optimal setting, it is still always very close to the
optimal setting. For some scenarios (e.g. Audio, 8MB), the op-
timal answer is close to QA_Ci, whereas for some scenarios
(e.g. P53, 20MB), the optimal answer is closer to QA_CiCd.
In both these scenarios, qwLSH is able to adapt and return
results closer to the optimal setting.
Effect of Varying Number of Queries in the Query Work-
load: Figure 10 shows the effect of different number of
queries in the query workload. It can be seen from Figure
10 that the optimal answer for Audio is closer to QA_Ci,
whereas the optimal answer for P53 is closer to QA_CiCd.
4000
8000
12000
16000
QA_Naive
(Audio)
qwLSH
(Audio)
QA_Naive
(P53)
qwLSH
(P53)
Time (in ms)
Effect of Overhead on Audio and P53
QueryTime
Overhead
Figure 11. Effect of caching overhead on Time (in ms)
qwLSH can always adapt and return results closer to the
optimal setting.
Overhead of qwLSH’s Cache Implementation: Figure
11 shows the negligible overhead of qwLSH when compared
with QALSH_Naive for Audio and P53 datasets. Even with
the caching overhead, qwLSH is still faster than QALSH_Naive
because of the efficient cache utilization and the resultant
savings in the total IO.
7
Conclusion
In this paper, we presented a novel cache-conscious index
structure, qwLSH, for efficient execution of query workloads
in high-dimensional spaces. Traditional LSH-based index
structures are not designed to efficiently query workloads in
high-dimensional spaces. Based on important observations
about the effect of cardinality and dimensionality of a dataset
on cache utilization, we intelligently divided a given cache
during processing of a query workload by using novel cost
models. Experimental analysis over different real datasets
under different settings showed the effectiveness of qwLSH.


## Page 9


References
[1] Daniar Achakeev, Bernhard Seeger, and Peter Widmayer. Sort-based
query-adaptive loading of r-trees. In Proceedings of the 21st ACM
International Conference on Information and Knowledge Management,
CIKM ’12, pages 2080–2084, New York, NY, USA, 2012. ACM.
[2] Ahmed M. Aly, Hazem Elmeleegy, Yan Qi, and Walid Aref. Kangaroo:
Workload-aware processing of range data and range queries in hadoop.
In Proceedings of the Ninth ACM International Conference on Web Search
and Data Mining, WSDM ’16, pages 397–406, New York, NY, USA, 2016.
ACM.
[3] Ahmed M. Aly, Ahmed R. Mahmood, Mohamed S. Hassan, Walid G.
Aref, Mourad Ouzzani, Hazem Elmeleegy, and Thamir Qadah. Aqwa:
Adaptive query workload aware partitioning of big spatial data. Proc.
VLDB Endow., 8(13):2062–2073, September 2015.
[4] Mayank Bawa, Tyson Condie, and Prasanna Ganesan. Lsh forest:
Self-tuning indexes for similarity search. In Proceedings of the 14th
International Conference on World Wide Web, WWW ’05, pages 651–
660, New York, NY, USA, 2005. ACM.
[5] Konstantin Berlin, Sergey Koren, Chen-Shan Chin, James P Drake,
Jane M Landolin, and Adam M Phillippy. Assembling large genomes
with single-molecule sequencing and locality-sensitive hashing. Na-
ture Biotechnology, 33(6):623–630, jun 2015.
[6] Ruben Buaba, Mohamed Gebril, Abdollah Homaifar, Eric Kihn, and
Mikhail Zhizhin. Locality Sensitive Hashing for satellite images using
texture feature vectors. In 2010 IEEE Aerospace Conference, pages 1–10.
IEEE, mar 2010.
[7] Jeremy Buhler. Efficient large-scale sequence comparison by locality-
sensitive hashing. Bioinformatics, 17(5):419–428, may 2001.
[8] Carlo Curino, Evan Jones, Yang Zhang, and Sam Madden. Schism: A
workload-driven approach to database replication and partitioning.
Proc. VLDB Endow., 3(1-2):48–57, September 2010.
[9] Mayur Datar, Nicole Immorlica, Piotr Indyk, and Vahab S. Mirrokni.
Locality-sensitive hashing scheme based on p-stable distributions. In
Proceedings of the Twentieth Annual Symposium on Computational
Geometry, SCG ’04, pages 253–262, New York, NY, USA, 2004. ACM.
[10] Junhao Gan, Jianlin Feng, Qiong Fang, and Wilfred Ng. Locality-
sensitive hashing scheme based on dynamic collision counting. In
Proceedings of the 2012 ACM SIGMOD International Conference on Man-
agement of Data, SIGMOD ’12, pages 541–552, New York, NY, USA,
2012. ACM.
[11] Jinyang Gao, H.V. Jagadish, Beng Chin Ooi, and Sheng Wang. Selec-
tive hashing: Closing the gap between radius search and k-nn search.
In Proceedings of the 21th ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining, KDD ’15, pages 349–358, New
York, NY, USA, 2015. ACM.
[12] Richard A. Hankins and Jignesh M. Patel. Effect of node size on
the performance of cache-conscious b+-trees. In Proceedings of the
2003 ACM SIGMETRICS International Conference on Measurement and
Modeling of Computer Systems, SIGMETRICS ’03, pages 283–294, New
York, NY, USA, 2003. ACM.
[13] Qiang Huang, Jianlin Feng, Yikai Zhang, Qiong Fang, and Wilfred
Ng. Query-aware locality-sensitive hashing for approximate nearest
neighbor search. Proc. VLDB Endow., 9(1):1–12, September 2015.
[14] Piotr Indyk and Rajeev Motwani. Approximate nearest neighbors:
Towards removing the curse of dimensionality. In Proceedings of the
Thirtieth Annual ACM Symposium on Theory of Computing, STOC ’98,
pages 604–613, New York, NY, USA, 1998. ACM.
[15] Yingfan Liu, Jiangtao Cui, Zi Huang, Hui Li, and Heng Tao Shen. Sk-
lsh: An efficient index structure for approximate nearest neighbor
search. Proc. VLDB Endow., 7(9):745–756, May 2014.
[16] Qin Lv, William Josephson, Zhe Wang, Moses Charikar, and Kai Li.
Multi-probe lsh: Efficient indexing for high-dimensional similarity
search. In Proceedings of the 33rd International Conference on Very
Large Data Bases, VLDB ’07, pages 950–961. VLDB Endowment, 2007.
[17] Parth Nagarkar and K. Selçuk Candan. HCS: hierarchical cut selection
for efficiently processing queries on data columns using hierarchical
bitmap indices. In Proceedings of the 17th International Conference
on Extending Database Technology, EDBT 2014, Athens, Greece, March
24-28, 2014., pages 271–282, 2014.
[18] Parth Nagarkar, K. Selçuk Candan, and Aneesha Bhat. Compressed
spatial hierarchical bitmap (cshb) indexes for efficiently processing
spatial range query workloads. PVLDB, 8(12):1382–1393, 2015.
[19] Andrew Pavlo, Carlo Curino, and Stanley Zdonik. Skew-aware auto-
matic database partitioning in shared-nothing, parallel oltp systems.
In Proceedings of the 2012 ACM SIGMOD International Conference on
Management of Data, SIGMOD ’12, pages 61–72, New York, NY, USA,
2012. ACM.
[20] Abdul Quamar, K. Ashwin Kumar, and Amol Deshpande. Sword: Scal-
able workload-aware data placement for transactional workloads. In
Proceedings of the 16th International Conference on Extending Database
Technology, EDBT ’13, pages 430–441, New York, NY, USA, 2013. ACM.
[21] Jun Rao and Kenneth A. Ross. Making b+- trees cache conscious in
main memory. In Proceedings of the 2000 ACM SIGMOD International
Conference on Management of Data, SIGMOD ’00, pages 475–486, New
York, NY, USA, 2000. ACM.
[22] Zeehasham Rasheed, Huzefa Rangwala, and Daniel Barbará.
16S
rRNA metagenome clustering and diversity estimation using locality
sensitive hashing. BMC Systems Biology, 7(Suppl 4):S11, oct 2013.
[23] Stefan Sprenger, Steffen Zeuch, and Ulf Leser. Cache-sensitive skip
list: Efficient range queries on modern cpus. In Spyros Blanas, Rajesh
Bordawekar, Tirthankar Lahiri, Justin Levandoski, and Andrew Pavlo,
editors, Data Management on New Hardware, pages 1–17, Cham, 2017.
Springer International Publishing.
[24] Yifang Sun, Wei Wang, Jianbin Qin, Ying Zhang, and Xuemin Lin. Srs:
Solving c-approximate nearest neighbor queries in high dimensional
euclidean space with a tiny index.
Proc. VLDB Endow., 8(1):1–12,
September 2014.
[25] Narayanan Sundaram, Aizana Turmukhametova, Nadathur Satish,
Todd Mostak, Piotr Indyk, Samuel Madden, and Pradeep Dubey.
Streaming similarity search over one billion tweets using parallel
locality-sensitive hashing. Proc. VLDB Endow., 6(14):1930–1941, Sep-
tember 2013.
[26] Yufei Tao, Ke Yi, Cheng Sheng, and Panos Kalnis. Efficient and accurate
nearest neighbor and closest pair search in high-dimensional space.
ACM Trans. Database Syst., 35(3):20:1–20:46, July 2010.
[27] Kostas Tzoumas, Man Lung Yiu, and Christian S. Jensen. Workload-
aware indexing of continuously moving objects. Proc. VLDB Endow.,
2(1):1186–1197, August 2009.
[28] C. E. Yoon, O. OReilly, K. J. Bergen, and G. C. Beroza. Earthquake
detection through computationally efficient similarity search. Science
Advances, 1(11):e1501057–e1501057, dec 2015.
[29] Kamen Yotov, Tom Roeder, Keshav Pingali, John Gunnels, and Fred
Gustavson. An experimental comparison of cache-oblivious and cache-
conscious programs. In Proceedings of the Nineteenth Annual ACM
Symposium on Parallel Algorithms and Architectures, SPAA ’07, pages
93–104, New York, NY, USA, 2007. ACM.
[30] Yuxin Zheng, Qi Guo, Anthony K.H. Tung, and Sai Wu. Lazylsh:
Approximate nearest neighbor search for multiple distance functions
with a single index. In Proceedings of the 2016 International Conference
on Management of Data, SIGMOD ’16, pages 2023–2037, New York,
NY, USA, 2016. ACM.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
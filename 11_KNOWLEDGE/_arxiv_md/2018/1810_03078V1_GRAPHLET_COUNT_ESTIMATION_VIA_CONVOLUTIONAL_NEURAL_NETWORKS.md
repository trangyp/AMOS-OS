---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1810.03078v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1810.03078v1_Graphlet_Count_Estimation_via_Convolutional_Neural_Networks

> Source: 1810.03078v1_Graphlet_Count_Estimation_via_Convolutional_Neural_Networks.pdf

> Pages: 4

---


## Page 1


Graphlet Count Estimation via Convolutional Neural
Networks
Xutong Liu1∗, Yu-Zhen Janice Chen1∗, John C.S. Lui1, and Konstantin Avrachenkov2
1 The Chinese University of Hong Kong
2 Inria Sophia Antipolis, France
Extended Abstract Accepted by COMPLEX NETWORKS 2018
1
Introduction. Graphlets are deﬁned as k-node connected induced subgraph pat-
terns. For an undirected graph, 3-node graphlets include close triangle ( ) and open
triangle ( ). When k = 4, there are six different types of graphlets, e.g., tailed-triangle
( ) and clique ( ) are two possible 4-node graphlets. The number of each graphlet,
called graphlet count, is a signature which characterizes the local network structure of
a given graph. Graphlet count plays a prominent role in network analysis of many ﬁelds,
most notably bioinformatics [4] and social science [3].
However, enumerating exact graphlet count is inherently difﬁcult and computational
expensive because the number of graphlets grows exponentially large as the graph size
and/or graphlet size k grow [3]. To deal with this difﬁculty, many sampling methods
were proposed for estimating graphlet count with bounded error [2,3,5]. Nevertheless,
these methods require large number of samples to be statistically reliable, which is still
computationally demanding. Moreover, they have to repeat laborious counting proce-
dure even if a new graph is similar or exactly the same as previous studied graphs.
Intuitively, learning from historic graphs can make estimation more accurate and
avoid many repetitive counting to reduce computational cost. Based on this idea, we
propose a convolutional neural network (CNN) framework and two preprocessing tech-
niques to estimate graphlet count.3 Extensive experiments on two types of random
graphs and real world biochemistry graphs show that our framework can offer sub-
stantial speedup on estimating graphlet count of new graphs with high accuracy.
2
Method. Given a set of undirected graphs and a particular type of k-node graphlet,
our objective is to develop a CNN which will be trained using part of dataset with
known graphlet counts. After training, the CNN can quickly and accurately predict
graphlet counts of other unseen graph samples in the set. Our framework takes the
graph adjacency matrix as input and outputs the graphlet count of the input graph. Let
us deﬁne some notations for our CNN. Let O(l) ∈RN(l)×N(l)×C(l) be the output tensor at
layer l, where l = 0,1,2,3, N(l) denotes the width (and height) along each channel and
C(l) denotes the channel size. Let O(l)
i,j,t be the (i, j)th element along the tth channel. We
assign O(0) as the graph adjacency matrix. Mathematically, our CNN structure can be
described as follows:
O(l)
i,j,t = ReLU(W(l)
t
·O(l−1)[i : i+H(l) −1, j : j +H(l) −1, :]+b(l)
t ),
l = 1,2,
(1)
O(3) = ReLU(Flatten(O(2))TW(3) +b(3)).
(2)
∗Both authors contributed equally to this work
3Our code is accessible at https://github.com/jjanicechen/GraphletCountEstimationCNN.git
arXiv:1810.03078v1  [cs.LG]  7 Oct 2018


## Page 2


Equation (1) corresponds to two convolution layers. Each layer applies C(l+1) ﬁlters
over the input feature map O(l−1), and the tth ﬁlter is parameterized by a trainable 3D
weight tensor W(l)
t
∈RH(l)×H(l)×C(l), where H(l) denotes the width (and height) of the
ﬁlter. [a : b,c : d,:] is a slicing function which extracts subset of elements indexing from
a to b in width, c to d in height and all in channel to form a new tensor. · is the sum
of element wise product of two tensors. After adding bias term b(l)
t , we apply ReLU
(max(0,x)) as the activation function to obtain the output feature map O(l). Equation
(2) is associated with the fully connected layer. It ﬂattens the output O(2) into a column
vector, applies W(3), b(3) and ReLU to obtain the estimated graphlet count. Finally, our
CNN is trained with back propagation and mean squared error as the loss function.
The above CNN structure inherits the learning power for local structural informa-
tion of graphs. However, we still need to address the following challenges: (1) The input
adjacency matrix is not consistent because graphs in the training set may have different
sizes. (2) In practice, real world network dataset may not contain sufﬁcient amount of
graph samples for training, which will cause overﬁtting problem. To address these chal-
lenges, we introduce two preprocessing techniques:
Adjacency Matrix Zero Padding. To preserve edge connectivity information of all
training graphs, we consider the largest graph in the training set, and use its dimen-
sion (say N) as the dimension of the input adjacency matrix (N ×N). For other graphs
in the training set, we take each adjacency matrix and pad it with zero till we have an
input matrix of dimension N ×N. This solves the varying input size problem.
Swapping Augmentation. To acquire sufﬁcient data for training, we take advantage of
the graph isomorphism property, where a graph can be expressed by different input
adjacency matrices having the same underlying network structure. Our approach is to
randomly pick indices i and j, then swap the ith row with jth row and ith column with jth
column of the adjacency matrix. We can repeat the swapping operation for each graph
m times to create m more training data. Analogous to ﬂipping or rotation of images, we
improve CNN’s generalization ability and thus improve the accuracy of our model.
3
Data and Metric. Here, we introduce our testing datasets, benchmarking works,
and evaluation metrics.
Random Graph. We synthesize datasets with two random graph models: random ge-
ometric graph (RGG) and Erdos-Renyi (ER) graph. A RGG is constructed by placing
nodes uniformly at random in a unit cube and connecting two nodes by an edge if and
only if their distance is within a given radius r. In a ER graph, the edge between every
two nodes exists with probability p. In each synthetic dataset, we have 3000 training
graphs, 300 validation graphs, and 300 testing graphs.
Empirical Network. We test on three real world biochemistry datasets: MUTAG [6],
NCI1 and NCI109 [7]. MUTAG dataset contains 188 mutagenic compound graphs.
NCI1 and NCI109 each has 4110 and 4127 chemical compound graphs tested on lung
and ovarian cancer cells respectively. For MUTAG, we use swapping augmentation to
increase the number of training samples. We also apply adjacency matrix zero padding
to make all graphs in each dataset have the same size.


## Page 3


Benchmark. We compare CNN with three existing frameworks: GRAFT [5], CC2 [2],
GUISE [1], which are based on edge sampling, color coding, and Markov Chain Monte
Carlo method respectively.
Relative Error. Let ci be the ground truth graphlet count of sample graph i, c′
i be its
estimated count, and there are S samples in the dataset. We compute the mean absolute
error of the estimations, mae = Σ S
i=1|c′
i −ci|/S, and mean of ground truth counts, µ =
Σ S
i=1ci/S. We take relative error as e = mae/µ .
Speed. To ensure a fair comparison, we do not choose running time as the perfor-
mance metric since it highly depends on hardware and implementation (e.g. running
on GPU/CPU). Instead, we measure the number of arithmetic operations they use. For
CNN model, we compute the number of ﬂoating-point operations (FLOPs). For bench-
marking works, we calculate the number of comparison operations in the algorithms.
4
Result. We test our framework on random graph datasets. For approximating 4-
clique counts, our CNN model achieves less than 8% relative error on 50-node RGGs
with radius 0.45 and less than 5% relative error on 50-node ER graphs with edge ex-
isting probability 0.5. We also train our CNN models for estimating 4-path ( ), 3-star
( ), 5-path (
) on the empirical biochemistry datasets. The relative errors on all three
datasets are less than 20% of the ground truth counts. For estimating 4-path on MUTAG
dataset, our model performs especially well making only 6% relative error.
Fig. 1. Comparison of the number of arithmetic operations used for estimating 4-clique counts,
tailed-triangle counts on 50-node ER graphs with edge existing probability 0.5. (a, c) The number
of operations used by each framework. (b, d) The relative error each framework makes.
To compare the speed of our CNN with existing methods, the number of arithmetic
operations used are calculated. For a fair comparison, we tune the number of iterations
for all benchmarking sampling methods, so that they obtain as close relative errors to
that of CNN as possible. Figure 1 (a, c) shows that the numbers of arithmetic opera-
tions used by GRAFT, CC2, or GUISE are signiﬁcantly more than that used by CNN.
This result demonstrates that our CNN based graphlet count estimation approach offers
remarkable speedup on predicting graphlet counts while still maintaining high accuracy.
References
1. Bhuiyan, M. A., Rahman, M., Rahman, M., Al Hasan, M.: Guise: Uniform sampling of
graphlets for large graph analysis. In: 2012 IEEE 12th ICDM. (pp. 91-100). IEEE. (2012)
2. Bressan, M., Chierichetti, F., Kumar, R., Leucci, S., Panconesi, A.: Counting graphlets:
Space vs time. In: Proc. Int. Conf. Web. Search. Data. Min. (pp. 557-566). ACM. (2017)
3. Chen, X., Li, Y., Wang, P., Lui, J.: A general framework for estimating graphlet statistics via
random walk. Proceedings VLDB Endowment 10(3), 253-264 (2016)
4. Prulj, N.: Biological network comparison using graphlet degree distribution. Bioinformatics,
23(2), e177-e183 (2007)


## Page 4


5. Rahman, M., Bhuiyan, M. A., Al Hasan, M.: Graft: An efﬁcient graphlet counting method
for large graph analysis. IEEE Trans. Knowl. Data. Eng., 26(10), 2466-2478 (2014)
6. Vishwanathan, S. V. N., Schraudolph, N. N., Kondor, R., Borgwardt, K. M.: Graph kernels.
J. Mach. Learn. Res, 11(Apr), 1201-1242 (2010)
7. Wale, N., Watson, I. A., Karypis, G.: Comparison of descriptor spaces for chemical com-
pound retrieval and classiﬁcation. KAIS, 14(3), 347-375 (2008)

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
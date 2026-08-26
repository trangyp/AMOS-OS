---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1703.06846v3
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1703.06846v3_Boosting_Dilated_Convolutional_Networks_with_Mixed_Tensor_Decompositions

> Source: 1703.06846v3_Boosting_Dilated_Convolutional_Networks_with_Mixed_Tensor_Decompositions.pdf

> Pages: 32

---


## Page 1


Boosting Dilated Convolutional Networks with
Mixed Tensor Decompositions
Nadav Cohen
COHENNADAV@IAS.EDU
Institute for Advanced Study
Ronen Tamari
RONENT@CS.HUJI.AC.IL
The Hebrew University of Jerusalem
Amnon Shashua
SHASHUA@CS.HUJI.AC.IL
The Hebrew University of Jerusalem
Abstract
The driving force behind deep networks is their ability to compactly represent rich classes of
functions. The primary notion for formally reasoning about this phenomenon is expressive ef-
ﬁciency, which refers to a situation where one network must grow unfeasibly large in order to
realize (or approximate) functions of another. To date, expressive efﬁciency analyses focused on
the architectural feature of depth, showing that deep networks are representationally superior to
shallow ones. In this paper we study the expressive efﬁciency brought forth by connectivity, mo-
tivated by the observation that modern networks interconnect their layers in elaborate ways. We
focus on dilated convolutional networks, a family of deep models delivering state of the art per-
formance in sequence processing tasks. By introducing and analyzing the concept of mixed tensor
decompositions, we prove that interconnecting dilated convolutional networks can lead to expres-
sive efﬁciency. In particular, we show that even a single connection between intermediate layers
can already lead to an almost quadratic gap, which in large-scale settings typically makes the differ-
ence between a model that is practical and one that is not. Empirical evaluation demonstrates how
the expressive efﬁciency of connectivity, similarly to that of depth, translates into gains in accuracy.
This leads us to believe that expressive efﬁciency may serve a key role in the development of new
tools for deep network design.
Keywords: Deep Learning, Expressive Efﬁciency, Dilated Convolutions, Tensor Decompositions
1. Introduction
One of the key attributes fueling the success of deep learning is the ability of deep networks to
compactly represent rich classes of functions. This phenomenon has drawn considerable attention
from the theoretical machine learning community in recent years. The primary notion for formally
reasoning about the representational abilities of different models is expressive efﬁciency. Given two
network architectures A and B, with size parameters (typically the width of layers across a network)
rA and rB, we say that architecture A is expressively efﬁcient w.r.t. architecture B if the following
two conditions hold: (i) any function realized by B with size rB can be realized (or approximated)
by A with size rA ∈O(rB); and (ii) there exist functions realized by A with size rA that cannot
be realized (or approximated) by B unless its size meets rB ∈Ω(f(rA)) for some super-linear
function f. The nature of the function f in condition (ii) determines the type of efﬁciency taking
place – if f is exponential then architecture A is said to be exponentially expressively efﬁcient
w.r.t. architecture B, and if f is polynomial so is the expressive efﬁciency of A over B.
c⃝2017 N. Cohen, R. Tamari & A. Shashua.
arXiv:1703.06846v3  [cs.LG]  13 Feb 2018


## Page 2


COHEN TAMARI SHASHUA
To date, works studying expressive efﬁciency in the context of deep learning (e.g. Delalleau
and Bengio (2011); Pascanu et al. (2013); Montufar et al. (2014); Telgarsky (2015); Eldan and
Shamir (2015); Poole et al. (2016); Raghu et al. (2016); Cohen et al. (2016b); Cohen and Shashua
(2016); Poggio et al. (2015); Mhaskar et al. (2016)) have focused on the architectural feature of
depth, showing instances where deep networks are expressively efﬁcient w.r.t. shallow ones. This
theoretical focus is motivated by the vast empirical evidence supporting the importance of depth
(see LeCun et al. (2015) for a survey of such results). However, it largely overlooks an additional
architectural feature that in recent years is proving to have great impact on the performance of deep
networks – connectivity. Nearly all state of the art networks these days (e.g. Szegedy et al. (2015);
He et al. (2015); Huang et al. (2016b,a)) deviate from the simple feed-forward (chain) approach,
running layers connected under various schemes. Whether or not this relates to expressive efﬁciency
remains to be an open question.
A speciﬁc family of deep networks gaining increased attention in the deep learning community
is that of dilated convolutional networks. These models form the basis of the recent WaveNet (van den
Oord et al. (2016)) and ByteNet (Kalchbrenner et al. (2016)) architectures, which provide state of
the art performance in audio and text processing tasks. Dilated convolutional networks are typically
applied to sequence data, and consist of multiple succeeding convolutional layers, each comprising
non-contiguous ﬁlters with a different dilation (distance between neighboring elements). The choice
of dilations directly affects the space of functions that may be realized by a network, and while no
choice is expressively efﬁcient w.r.t. another, we show in this work that interconnecting networks
with different dilations leads to expressive efﬁciency, and by this demonstrate that connectivity
indeed bears the potential to enhance the expressiveness of deep networks.
Our analysis follows several recent works utilizing tensor decompositions for theoretical studies
of deep learning (see for example Janzamin et al. (2015); Sedghi and Anandkumar (2016)), and in
particular, builds on the equivalence between hierarchical tensor decompositions and convolutional
networks established in Cohen et al. (2016b) and Cohen and Shashua (2016). We show that with
dilated convolutional networks, the choice of dilations throughout a network corresponds to deter-
mination of the mode (dimension) tree underlying the respective decomposition. We then deﬁne
the notion of a mixed tensor decomposition, which blends together multiple mode trees, effectively
creating a large ensemble of hybrid trees formed from all possible combinations. Mixed tensor
decompositions correspond to mixed dilated convolutional networks, i.e. mixtures formed by con-
necting intermediate layers of different dilated convolutional networks. This allows studying the
expressive properties of such mixtures using mathematical machinery from the ﬁeld of tensor anal-
ysis. We fully analyze a particular case of dilated convolutional arithmetic circuits, showing that a
single connection between intermediate layers already leads to an almost quadratic expressive efﬁ-
ciency, which in large-scale settings typically makes the difference between a model that is practical
and one that is not.
An experiment on TIMIT speech corpus (Garofolo et al. (1993)) evaluates the dilated convo-
lutional network architectures covered by our analysis. We ﬁnd that interconnecting intermediate
layers of different networks improves accuracy, with no additional cost in terms of computation
or model capacity. This serves as an indication that with the architectural feature of connectivity,
similarly to the case of depth, expressive efﬁciency and improved accuracies go hand in hand. Ac-
cordingly, we believe expressive efﬁciency may serve a key role in the development of new tools
for deep network design.
2


## Page 3


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
2. Summary of Our Analysis and Contributions
Our analysis begins in sec. 4, where we present the dilated convolutional network underlying
WaveNet (ﬁg. 1). We consider this to be the baseline architecture and, following Cohen and Shashua
(2016), facilitate its study through tensor analysis. The key to introducing tensors into the frame-
work is a discretization of the network’s input-output mapping. Namely, f(x[t−N+1], . . . , x[t]) – a
function realized by the network (t here stands for a natural time index), is conceptually evaluated
on a ﬁnite (exponentially large) number of input points, generated from all possible assignments
of the variables x[t−N+1], . . . , x[t] to each hold one of M predetermined values. This gives rise
to an N-dimensional lookup table, with length M in each axis. We refer to this lookup table as
a grid tensor (eq. 1). It is shown (app. A) that grid tensors brought forth by the baseline dilated
convolutional network can be expressed as a hierarchical tensor decomposition, referred to as the
baseline decomposition (eq. 2).
The baseline decomposition implicitly adheres to a particular tree over tensor modes (axes). This
calls for a generalization, and we indeed deﬁne a general mode tree (def. 1), followed by a corre-
sponding hierarchical tensor decomposition, referred to as the tree decomposition (eq. 3). Different
choices of mode trees lead to tree decompositions characterizing networks with different dilations.
We focus on the tree that corresponds to the baseline network (ﬁg. 2(a)), and on those corresponding
to networks obtained by swapping dilations of different layers (ﬁg. 2(b), for example).
Armed with a framework for representing different dilated convolutional networks through hi-
erarchical tensor decompositions of different mode trees, we head on in sec. 5 and introduce the
notion of a mixed tensor decomposition (eq. 4). The mixed decomposition of two mode trees T
and ¯T is based on a preselected set of nodes present in both trees, referred to as mixture nodes. Indi-
vidual tree decompositions of T and ¯T are run in parallel, where at each mixture node, tensors from
the two decompositions are swapped. If N and ¯
N are the dilated convolutional networks charac-
terized by T and ¯T (respectively), the mixed decomposition characterizes a mixed (interconnected)
network M, formed by rewiring intermediate layers of N into ¯
N, and vice versa (see ﬁg. 3).
The heart of our analysis is sec. 6, where we study the expressive efﬁciency of the mixed net-
work M over the individual networks N and ¯
N. Establishing expressive efﬁciency requires show-
ing that any function realized by N or ¯
N can be realized by M with no more than linear growth in
size, whereas the converse does not hold, i.e. there exist functions realizable by M that cannot be
realized by N or ¯
N unless their size is allowed to grow super-linearly. From a tensor decomposition
perspective, this translates to the following two propositions:
(i) any tensor generated by a tree decomposition of T or ¯T can be realized by their mixed de-
composition with no more than linear growth in size; and
(ii) there exist tensors realizable by the mixed decomposition of T and ¯T that cannot be realized
by their individual tree decompositions without a super-linear growth in size.
We address both propositions through the notion of hybrid mode trees (def. 4; ﬁg. 4), which are
simply mode trees born from combinations of T and ¯T. We prove (claim 5) that the mixed decom-
position of T and ¯T can replicate, with no more than linear growth in size, the tree decomposition
of any hybrid tree H. Since T and ¯T are in particular hybrid mode trees of themselves, we obtain
an afﬁrmative answer to proposition (i). For addressing proposition (ii), we demonstrate a case
(with convolutional arithmetic circuits) where there exists a hybrid tree H whose tree decomposi-
tion generates tensors that require the tree decompositions of T and ¯T to grow super-linearly. Since
the mixed decomposition of T and ¯T can (by claim 5) replicate the tree decomposition of H with
3


## Page 4


COHEN TAMARI SHASHUA
no more than linear growth, proposition (ii) is established, and M is indeed expressively efﬁcient
w.r.t. N and ¯
N (corollary 8).
The central tool for establishing proposition (ii), or more speciﬁcally, for demonstrating the
existence of a hybrid tree H whose tree decomposition requires those of T and ¯T to grow super-
linearly, is a tight analysis of tensors generated by a tree decomposition in terms of their ranks when
arranged as matrices (theorem 7). Matricization ranks under hierarchical tensor decompositions are
of interest from a pure tensor analysis perspective (cf. Hackbusch (2012)), as well as in the context
of deep learning (cf. Cohen and Shashua (2017)). The bounds we provide are much tighter (exact in
many cases) and far more general than those existing in the literature, and we expect them to prove
useful in different applications. The key idea in deriving these bounds is to consider a matricized
form of the tree decomposition, and recursively propagate outwards various matrices (for details see
proof sketch following theorem 7, as well as the complete proof in app. B.2).
To conclude this section, we list below the main contributions of the paper:
• We introduce the notion of a mixed tensor decomposition, and prove that it brings forth a
representational advantage compared to the individual hierarchical decompositions it com-
prises. This development is of interest from a pure tensor analysis perspective, independently
of convolutional networks, or machine learning in general.
• We provide the ﬁrst formal evidence for the fact that interconnectivity – an architectural fea-
ture prevalent in state of the art deep learning, brings forth expressive efﬁciency.
• Our central theorem (theorem 7) provides the most comprehensive characterization to date of
matricization ranks brought forth by hierarchical tensor decompositions.
3. Preliminaries
The constructions and analyses delivered in this paper rely on concepts from the ﬁeld of tensor
analysis. Below we provide the minimal background required in order to follow our arguments.1
The core concept in tensor analysis is a tensor, which for our purposes may simply be thought of
as a multi-dimensional array. The order of a tensor is deﬁned to be the number of indexing entries
in the array, which are referred to as modes. The dimension of a tensor in a particular mode is
deﬁned as the number of values that may be taken by the index in that mode. For example, a 4-by-3
matrix is a tensor of order 2, i.e. it has two modes, with dimension 4 in mode 1 and dimension 3 in
mode 2. If A is a tensor of order N and dimension Mi in each mode i ∈{1, . . . , N}, the space of
all conﬁgurations it can take is denoted, quite naturally, by RM1×···×MN .
A fundamental operator in tensor analysis is the tensor product (also known as outer prod-
uct), which we denote by ⊗. It is an operator that intakes two tensors A ∈RM1×···×MP and
B ∈RMP +1×···×MP +Q (orders P and Q respectively), and returns a tensor A ⊗B ∈RM1×···×MP +Q
(order P +Q) deﬁned by: (A⊗B)d1...dP +Q = Ad1...dP ·BdP +1...dP +Q. In Cohen and Shashua (2016)
a generalization of the tensor product is deﬁned, by replacing multiplication with a general opera-
tor g(·). Speciﬁcally, for a function g : R × R →R that is commutative (g(a, b) = g(b, a) for all
a, b ∈R), the generalized tensor product, denoted ⊗g, is deﬁned to be the operator that for input ten-
sors A ∈RM1×···×MP and B ∈RMP +1×···×MP +Q (orders P and Q respectively), returns the tensor
A ⊗g B ∈RM1×···×MP +Q (order P + Q) given by: (A ⊗g B)d1...dP +Q = g(Ad1...dP , BdP +1...dP +Q).
4


## Page 5


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
An additional operator we will make use of is mode permutation. Let A be a tensor of order N,
and let σ(·) be a permutation over N (bijective mapping from {1, . . . , N} to itself). The mode per-
mutation of A w.r.t. σ(·), which by a slight abuse of notation is denoted σ(A), is the order-N tensor
deﬁned by: σ(A)d1...dN = Adσ(1)...dσ(N). In words, σ(A) is the tensor obtained by rearranging the
modes of A in accordance with σ(·).
When studying tensors, it is oftentimes useful to arrange them as matrices, a procedure referred
to as matricization. Let A be a tensor of order N and dimension Mi in each mode i ∈{1, . . . , N},
and let I ⊂{1, . . . , N} be a set of mode indexes, whose complement {1, . . . , N} \ I we denote
by Ic. We may write I = {i1, . . . , i|I|} where i1 < · · · < i|I|, and similarly Ic = {j1, . . . , j|Ic|}
where j1 < · · · < j|Ic|. The matricization of A w.r.t. I, denoted JAKI, is the Q|I|
t=1 Mit-by-
Q|Ic|
t=1 Mjt matrix holding the entries of A such that Ad1...dN is placed in row index 1 + P|I|
t=1(dit −
1) Q|I|
t′=t+1 Mit′ and column index 1 + P|Ic|
t=1(djt −1) Q|Ic|
t′=t+1 Mjt′. If I = ∅or I = {1, . . . , N},
then by deﬁnition JAKI is a row or column (respectively) vector of dimension QN
t=1 Mt holding
Ad1...dN in entry 1 + PN
t=1(dt −1) QN
t′=t+1 Mt′.
To conclude this section, we hereinafter establish notational conventions that will accompany
us throughout the paper. We denote tensors with uppercase calligraphic letters, e.g. A, and in some
cases, with the Greek letters φ, ϕ or ψ. Subscripts are used to refer to individual tensor entries,
e.g. Ad1...dN ∈R, whereas superscripts indicate the location of a tensor in some annotated collec-
tion, for example Ay stands for the y’th tensor in the collection A1 . . . Ar. Vectors are typically
denoted with boldface lowercase letters, e.g. a, where again subscripts refer to an individual entry
(e.g. aα ∈R), and superscripts to the identity of a vector within some annotated collection (e.g. al,j
is the (l, j)’th vector in the set {al,j}l=1...L,j=1...N). We use non-boldface lowercase or uppercase
letters (e.g. l or L) to denote scalars, and in this case, both subscripts and superscripts distinguish
between objects in an annotated set (e.g. li, li, Li, Li ∈R). Finally, for a positive integer N ∈N,
we use [N] as shorthand for the set {1, . . . , N}.
4. Dilated Convolutional Networks
Dilated convolutional networks are a family of convolutional networks (LeCun and Bengio (1995))
gaining increased attention in the deep learning community. As opposed to more conventional con-
volutional architectures (see for example Krizhevsky et al. (2012)), which are applied primarily to
images and videos, dilated convolutional networks thrive in sequence processing tasks. For exam-
ple, they underlie Google’s WaveNet (van den Oord et al. (2016)) and ByteNet (Kalchbrenner et al.
(2016)) models, which provide state of the art performance in audio and text processing tasks.
4.1. Baseline Architecture
The dilated convolutional network architecture considered as baseline in this paper is the one un-
derlying WaveNet model, depicted in ﬁg. 1. The input to the network is a sequence of vectors
(x[t])t ⊂Rr0, where t is a natural time index.
A size-2 convolutional layer with dilation-1,
i.e. with contiguous ﬁlters, maps this input into the hidden sequence (h(1)[t])t ⊂Rr1. Speciﬁ-
cally, entry γ ∈[r1] of h(1)[t] is obtained by applying the ﬁlter formed by a1,γ,I, a1,γ,II ∈Rr0
to time points t−1, t of the input: h(1)[t]γ = g(

a1,γ,I, x[t−1]

,

a1,γ,II, x[t]

). For reasons that
will shortly become apparent, we use g(·) here to denote the binary function combining two size-1
convolutions into a single size-2 convolution with non-linearity. Different choices of g(·) lead to
5


## Page 6


COHEN TAMARI SHASHUA
size-2 conv:
dilation-1
size-2 conv:
dilation-2
size-2 conv:
dilation-2L-1
Time
t-2L+1
t+1
L-1 
hidden 
layers
N:=2L time points
input
output
0r

1r

2r

1
Lr 

Lr

t
t-1
t-2
t-3
t-2L+2
t-2L



1
1, ,I
1, ,II
[ ]
, [
1] ,
, [ ]
h
t
g
t
t




a
x
a
x






1
1
,y,I
1
, ,II
[ ]
,
[
2
] ,
,
[ ]
L
L
L
L
L y
y
o t
g
t
t





a
h
a
h





2
1
1
2, ,I
2, ,II
[ ]
,
[
2] ,
,
[ ]
h
t
g
t
t




a
h
a
h
Figure 1: Baseline dilated convolutional network architecture (see description in sec. 4.1).
different convolutional operators, for example g(a, b) := max{a + b, 0} leads to standard convolu-
tion followed by rectiﬁed linear activation (ReLU, Nair and Hinton (2010)), whereas g(a, b) = a·b
gives rise to what is known as a convolutional arithmetic circuit (Cohen et al. (2016b)). Fol-
lowing the ﬁrst hidden layer, L−1 size-2 convolutional layers with increasing dilations are ap-
plied. Speciﬁcally, for l = 2, . . ., L−1, hidden layer l maps the sequence (h(l−1)[t])t ⊂Rrl−1
into (h(l)[t])t ⊂Rrl using ﬁlters with dilation-2l−1, i.e. with an internal temporal gap of 2l−1−1
points: h(l)[t]γ = g(

al,γ,I, h(l−1)[t−2l−1]

,

al,γ,II, h(l−1)[t]

). The last convolutional layer maps
(h(L−1)[t])t into network output sequence (o[t])t ⊂RrL using ﬁlters with dilation-2L−1: o[t]y =
g(

aL,y,I, h(L−1)[t−2L−1]

,

aL,y,II, h(L−1)[t]

).
Altogether, the architectural parameters of the network are the number of convolutional layers L,
the convolutional operator g(·), the input dimension r0, the number of channels rl for each hidden
layer l ∈[L−1], and the output dimension rL. The learnable parameters are the convolution weights
al,γ,I, al,γ,II ∈Rrl−1 for channel γ ∈[rl] of layer l ∈[L].
Our interest lies on the representational abilities of the network, i.e. on the properties of the
input-output mappings it can realize. As illustrated in ﬁg. 1, for some ﬁxed time point t, o[t] – net-
work output at time t, is a function of x[t−2L+1] . . . x[t] – network input over the last 2L time
points. Taking into account the temporal stationarity of the network, and denoting for brevity
N:=2L, we may write o[t]y = fy(x[t−N+1], . . . , x[t]) for every y ∈[rL], where the func-
tions {fy(·)}y are independent of the time index t. The latter functions, which obviously depend
on the convolution weights {al,γ,I, al,γ,II}l,γ, completely characterize the input-output mapping re-
alized by the network. We will study these functions through the process of discretization. Namely,
fy(·) – a function of N vector-variables, will be represented by a lookup table (tensor) formed by
varying each vector-variable over a ﬁnite number of possible values. The size of such a lookup
table is exponential in N, thus treating it directly is intractable. However, as we shall see, the
network admits a compact parameterization of lookup tables in terms of the convolution weights
{al,γ,I, al,γ,II}l,γ. This parameterization (eq. 2 below) entails an algebraic structure, and will be
used to study the representational properties of the baseline dilated convolutional network.
For the discretization of fy(·), we choose a collection of vectors v(1) . . . v(M) ∈Rr0, and deﬁne
the following tensor Ay of order N and dimension M in each mode:
Ay
d1...dN := fy(v(d1), . . . , v(dN))
∀d1. . .dN ∈[M]
(1)
6


## Page 7


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
dilation-1
dilation-2
dilation-4
dilation-8
dilation-1
dilation-2
dilation-4
dilation-8












I
II
1,2,3,4
1,3
1,2,3,4
2,4
C
C


(a)


13,14,15,16
1
2
3
4
1
2
3
4







(b)


13,14,15,16
1
2
3
4
1
3
2
4



















I
II
1,2,3,4
1,2
1,2,3,4
3,4
C
C


{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,2}
{3,4}
{5,6}
{15,16}
{7,8}
{9,10}
{11,12}
{13,14}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,5,6,7,8}
{9,10,11,12,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,3}
{2,4}
{5,7}
{14,16}
{6,8}
{9,11}
{10,12}
{13,15}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,9,10,11,12}
{5,6,7,8,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
Figure 2: Best viewed in color. Dilated convolutional networks (left) and the mode trees underlying
their respective tensor decompositions (right). (a) Baseline architecture – dilation 2l−1 in
layer l. (b) Architecture obtained by swapping dilations of even and odd layers.
The vectors v(1) . . . v(M) are referred to as discretizers. They generate the tensor Ay by assigning,
in all possible combinations, the N vector-variables of the function fy(·). We refer to Ay as the
grid tensor of fy(·), reﬂecting the fact that it holds function values over a discrete grid.
The parameterization of {fy(·)}y discretizations mentioned above is in fact a hierarchical de-
composition of the grid tensors {Ay}y. Accordingly, and for the sake of highlighting correspon-
dence to the baseline dilated convolutional network (ﬁg. 1), we refer to this parameterization as the
baseline decomposition. For conciseness, we defer the derivation of the baseline decomposition to
app. A, and hereby lay out its ﬁnal form:
For j = 1. . .N:
φ0,j,γ
| {z }
order 1
= [v(1)
γ , . . . , v(M)
γ
]⊤
∀γ ∈[r0]
For l = 1. . .L , j = 1. . .N/2l:
φl,j,γ
|{z}
order 2l
=
Xrl−1
α=1 al,γ,I
α
· φl−1,2j−1,α
⊗g
Xrl−1
α=1 al,γ,II
α
· φl−1,2j,α
∀γ ∈[rl]
Ay = φL,1,y
∀y ∈[rL]
(2)
al,γ,I
α
and al,γ,II
α
here stand for coordinate α of the convolution weights al,γ,I and al,γ,II respectively,
while v(i)
γ
stands for coordinate γ of the discretizer v(i). Notice that the tensor products here are
generalized (see sec. 3) – based on the network’s convolutional operator g(·). Therefore, strictly
speaking, the baseline decomposition is a generalized tensor decomposition, as deﬁned in Cohen
and Shashua (2016).
4.2. Dilations and Mode Trees
The baseline decomposition (eq. 2), corresponding to the baseline dilated convolutional network
(ﬁg. 1), implicitly adheres to a tree structure – for every (l, j), there exists a group of tensors {φl,j,γ}γ,
7


## Page 8


COHEN TAMARI SHASHUA
formed through combinations of tensors from its “child” groups {φl−1,2j−1,γ}γ and {φl−1,2j,γ}γ.
In this subsection we generalize the underlying tree structure, and show that the resulting decompo-
sitions capture networks with various dilations throughout their convolutional layers. We begin by
deﬁning a general (binary) tree over tensor modes:
Deﬁnition 1 Let N ∈N. A binary mode tree2 over [N] is a full binary tree3 in which:
• Every node is labeled by a subset of [N]
• There are exactly N leaves, labeled {1} . . . {N}
• The label of an interior (non-leaf) node is the union of the labels of its children
If T is a binary mode tree, we identify its nodes with their labels, i.e. with the corresponding subsets
of [N]. The set of all interior nodes is denoted by int(T) ⊂2[N], the children of an interior node
ν ⊂[N] are denoted by CI(ν; T), CII(ν; T) ⊂[N], and the parent of a non-root node ν ⊂[N] is
denoted by P(ν; T). Notice that by deﬁnition, the root node is labeled [N].
Binary mode trees induce hierarchical decompositions of grid tensors. Recall the deﬁnition of
grid tensors in sec. 4.1 (eq. 1), and let T be a binary mode tree over [N]. For every node ν ⊂[N]
in T, we deﬁne a collection of 2|ν|-order tensors {φν,γ}γ∈[r], where r ∈N is a predetermined
constant,4 referred to as the size constant of the decomposition. We also deﬁne, for each interior
node ν∈int(T), two collections of weight vectors – {aν,γ,I}γ∈[r] ⊂Rr and {aν,γ,II}γ∈[r] ⊂Rr.
The hierarchical grid tensor decomposition induced by T traverses through the tree in a depth-ﬁrst
fashion, assigning the tensors of node ν ({φν,γ}γ) through combinations of the tensors of its children
({φCI(ν;T),γ}γ and {φCII(ν;T),γ}γ). This is laid out formally in eq. 3 below, which we refer to as the
tree decomposition.
For j = 1. . .N:
φ{j},γ
| {z }
order 1
= [v(1)
γ , . . . , v(M)
γ
]⊤
∀γ ∈[r]
For ν in int(T) (depth-ﬁrst order):
φν,γ
|{z}
order 2|ν|
= σ(ν;T) Xr
α=1 aν,γ,I
α
· φCI(ν;T),α
⊗g
Xr
α=1 aν,γ,II
α
· φCII(ν;T),α
∀γ ∈[r]
Ay = φ[N],y
∀y ∈[r]
(3)
As in the baseline decomposition (eq. 2), v(i)
γ here stands for coordinate γ of the discretizer v(i). The
permutation σ(ν;T)(·), for an interior node ν∈int(T), arranges the modes of the tensor φν,γ such
that these comply with a sorted ordering of ν. Speciﬁcally, if we denote by i1 < · · · < i|CI(ν;T)| the
elements of CI(ν; T) ⊂[N], and by j1 < · · · < j|CII(ν;T)| the elements of CII(ν; T) ⊂[N], the per-
mutation σ(ν;T) : [2|ν|] →[2|ν|] is the one that sorts the tuple (i1, . . . , i|CI(ν;T)|, j1, . . . , j|CII(ν;T)|)
in ascending order. The ﬁnal outcome of the decomposition, i.e. the generated grid tensors {Ay}y,
are the tensors {φ[N],γ}γ corresponding to the root of T.
Compare the general tree decomposition in eq. 3 to the baseline decomposition in eq. 2. It
is not difﬁcult to see that the latter is a special case of the former. Namely, it corresponds to a
binary mode tree T that is perfect (all leaves have the same depth L = log2 N), and whose depth-l
nodes (l ∈{0, 1, . . . , L}) are (k −1)N/2l + [N/2l] for k ∈[2l].5 This implies that such a mode
8


## Page 9


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
tree, when plugged into the tree decomposition (eq. 3), provides a characterization of the baseline
dilated convolutional network (ﬁg. 1), i.e. a network whose dilation in layer l is 2l−1 (see illustration
in ﬁg. 2(a)). If we were to choose a different mode tree, the corresponding dilated convolutional
network would change.6 For example, assume that L = log2 N is even, and consider a perfect
binary mode tree T whose depth-l nodes (l ∈{0, 1, . . . , L}) are as follows:
• Even l: depth-l nodes are (k −1)N/2l + [N/2l] for k ∈[2l]
• Odd l: depth-l nodes are generated by splitting nodes of depth l-1, such that the ﬁrst and third
quadrants of a split node belong to one child, while the second and fourth belong to the other
In this case, the network characterized by the tree decomposition (eq. 3) is obtained by swapping
dilations of even and odd layers in the baseline architecture, i.e. it has dilation in layer l of 2l−2 if
l is even, and 2l if l is odd (see illustration in ﬁg. 2(b)).
5. Mixed Tensor Decompositions
Let T and ¯T be two binary mode trees over [N] (def. 1). Consider the tree decomposition of grid ten-
sors induced by T (eq. 3). This decomposition iteratively assigns a group of tensors {φν,γ}γ for each
node ν in T, based on weight vectors {aν,γ,I, aν,γ,II}γ deﬁned for each interior node ν∈int(T). The
tree decomposition induced by ¯T operates similarly, but for distinction we use {¯φ¯ν,γ}γ to denote the
tensor group of node ¯ν ∈¯T, and {¯a¯ν,γ,I, ¯a¯ν,γ,II}γ to denote the weights of interior node ¯ν∈int( ¯T).
We will deﬁne a mixed tensor decomposition, blending together the tree decompositions of T and ¯T.
The latter is obtained by choosing a collection of mixture nodes – mix(T, ¯T)⊂int(T)∩int( ¯T).
These are nodes (subsets of [N]) that reside in the interior of both T and ¯T, deﬁning locations in
the tree decompositions at which tensors will be exchanged. If mix(T, ¯T) is chosen as the empty
set, the mixed decomposition simply sums the output tensors generated by the tree decompositions
of T and ¯T ({φ[N],y}y and {¯φ[N],y}y respectively). Otherwise, the tree decompositions of T and ¯T
progress in parallel, until reaching a mixture node µ∈mix(T, ¯T), where they exchange half the
tensors corresponding to that node (half of {φµ,γ}γ is exchanged for half of {¯φµ,γ}γ). The process
continues until all mixture nodes are visited and the root node (of both trees) [N] is reached. At this
point tensors ({φ[N],y}y and {¯φ[N],y}y) are summed and returned as output.
The formal deﬁnition of the mixed decomposition is as follows:
1 : For j = 1. . .N:
2 :
φ{j},γ = ¯φ{j},γ = [v(1)
γ , . . . , v(M)
γ
]⊤
∀γ ∈[r]
r – decomposition size constant
3 : For µ in mix(T, ¯T) ∪{[N]} (inclusion order):
4 :
For ν in int(T) ∩2µ \ {nodes in T already visited} (inclusion order):
5 :
φν,γ = σ(ν;T) Xr
α=1 aν,γ,I
α
· φCI(ν;T),α
⊗g
Xr
α=1 aν,γ,II
α
· φCII(ν;T),α
∀γ ∈[r]
6 :
For ¯ν in int( ¯T) ∩2µ \ {nodes in ¯T already visited} (inclusion order):
7 :
¯φ¯ν,γ = σ(¯ν; ¯T) Xr
α=1 ¯a¯ν,γ,I
α
· ¯φCI(¯ν; ¯T),α
⊗g
Xr
α=1 ¯a¯ν,γ,II
α
· ¯φCII(¯ν; ¯T),α
∀γ ∈[r]
8 :
Swap φµ,γ ←→¯φµ,γ
∀γ ∈[r/2]
9 : Ay = φ[N],y + ¯φ[N],y
∀y ∈[r]
(4)
9


## Page 10


COHEN TAMARI SHASHUA
As in the basic tree decomposition (eq. 3), the ﬁrst step here (lines 1-2) is to assign tensors cor-
responding to the leaf nodes ({1} . . . {N}) via discretizers v(1) . . . v(M). The outer loop in line 3
traverses µ through mixture nodes and the root node in inclusion order, i.e. such that a node (subset
of [N]) is always reached after all nodes strictly contained in it. Lines 4-5 (respectively 6-7) are the
same as in the tree decomposition (eq. 3), except that instead of running through the entire interior
of T (respectively ¯T), they cover a segment of it. This segment continues where the previous ones
left off, and comprises only nodes (subsets of [N]) contained in µ (including µ itself). Line 8 is
where the mixing takes place – here half the tensors corresponding to node µ in the decomposi-
tion of T ({φµ,γ}γ), are exchanged for half the tensors corresponding to µ in the decomposition
of ¯T ({¯φµ,γ}γ). Finally, after µ has reached the root node [N] and the decompositions of T and ¯T
have concluded, line 9 sums the output tensors of these decompositions ({φ[N],y}y and {¯φ[N],y}y
respectively), producing the grid tensors {Ay}y.
In terms of computation and memory, the requirements posed by the mixed decomposition
(eq. 4) are virtually identical to those of running two separate tree decompositions (eq. 3) with T
and ¯T. Speciﬁcally, if the tree decompositions of T and ¯T correspond to input-output mappings
computed by the dilated convolutional networks N and ¯
N (respectively), the mixed decomposition
would correspond to the computation of a mixed dilated convolutional network, formed by sum-
ming the outputs of N and ¯
N, and interconnecting their intermediate layers. The choice of mixture
nodes mix(T, ¯T) in the mixed decomposition determines the locations at which networks N and ¯
N
are interconnected, where an interconnection simply wires into N half the outputs of a convolu-
tional layer in ¯
N, and vice versa. For example, suppose that N is the baseline dilated convolutional
network (dilation 2l−1 in layer l – see sec. 4.1), whereas ¯
N is the network obtained by swapping
dilations of even and odd layers (such that layer l has dilation 2l−2 if l is even, and 2l if l is odd).
The mode trees corresponding to these networks, illustrated in ﬁg. 2 (for the case L:= log2 N=4),
share interior nodes (k −1)N/2l + [N/2l] for l ∈{2, 4, . . . , L}, k ∈[2l]. We may therefore
choose mix(T, ¯T) to be all such nodes (excluding root), and get a mixed decomposition that cor-
responds to a mixed network interconnecting all even layers of N and ¯
N. Illustrations of such
decomposition and network (again, for the case L=4) are given in ﬁg. 3.
The main advantage of the mixed decomposition (eq. 4), and the reason for its deﬁnition, is that
it leads to expressive efﬁciency. That is to say, the mixed dilated convolutional network, formed by
interconnecting intermediate layers of networks with different dilations, can realize functions that
without the interconnections would be expensive, or even impractical to implement. We theoreti-
cally support this in the next section, providing a complete proof for a special case of convolutional
arithmetic circuits (g(a, b) = a·b).
6. Expressive Efﬁciency Analysis
As in sec. 5, let N and ¯
N be two dilated convolutional networks whose input-output mappings are
characterized by the tree decomposition (eq. 3) with mode trees T and ¯T respectively. Consider the
mixed decomposition (eq. 4) resulting from a particular choice of mixture nodes mix(T, ¯T) (subset
of the nodes interior to both T and ¯T), and denote its corresponding mixed dilated convolutional
network by M. We would like to show that M is expressively efﬁcient w.r.t. N and ¯
N, meaning:
(i) any function realized by N or ¯
N can also be realized by M with no more than linear growth
in network size (number of channels in the convolutional layers); (ii) there exist functions realiz-
able by M that cannot be realized by N or ¯
N (or a summation thereof) unless their size (number
10


## Page 11


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
network
N
dilation-1
dilation-2
dilation-8
input
dilation-4
dilation-1
dilation-2
dilation-8
dilation-4
output
(b)
(a)
mix(T,T)
mode tree T
mode tree T
network
N
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,2}
{3,4}
{5,6}
{15,16}
{7,8}
{9,10}
{11,12}
{13,14}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,5,6,7,8}
{9,10,11,12,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,3}
{2,4}
{5,7}
{14,16}
{6,8}
{9,11}
{10,12}
{13,15}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,9,10,11,12}
{5,6,7,8,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
Figure 3: To be viewed in color. (a) Two mode trees T and ¯T (given on the right of ﬁg. 2), along
with a possible choice of mixture nodes mix(T, ¯T) for the mixed decomposition (eq. 4).
(b) Mixed dilated convolutional network resulting from the mixed decomposition. The
networks N and ¯
N corresponding to T and ¯T respectively (ﬁg. 2, left), are combined
through output summation and rewiring of an intermediate convolutional layer (green).
of convolutional channels) is allowed to grow super-linearly. We study the representational abili-
ties of networks through their corresponding tensor decompositions, which as discussed in sec. 4,
parameterize discretizations of input-output mappings (grid tensors). Through the lens of tensor
decompositions, our objective is to address the following two propositions7 (stated informally):
Proposition 2 Consider a tree decomposition (eq. 3) with underlying mode tree T or ¯T and size
constant r = rtree. This decomposition can be realized by a mixed decomposition of T and ¯T (eq. 4)
whose size constant r is linear in rtree.
Proposition 3
Consider a mixed decomposition of T and ¯T (eq. 4) with size constant r = rmix.
This decomposition can generate grid tensors {Ay}y that cannot be generated by tree decomposi-
tions of T or ¯T (eq. 3), or a summation of such, unless their size constant r is super-linear in rmix.
Before heading to a formal treatment of prop. 2 and 3, we brieﬂy convey the intuition behind
our analysis. Recall from sec. 5 that the mixed decomposition (eq. 4) blends together tree decom-
positions (eq. 3) of different mode trees T and ¯T, by traversing upwards through the trees, while
11


## Page 12


COHEN TAMARI SHASHUA
exchanging tensors at each of a preselected set of mixture nodes. We may think of each mixture
node as a decision point that can propagate upwards one of two computations – that carried out
by T or that carried out by ¯T, where in both cases, the chosen computation is propagated upwards
through both T and ¯T. Each combination of decisions across all mixture nodes gives rise to a com-
putational path traversing between T and ¯T, equivalent to a tree decomposition based on a hybrid
mode tree (see illustration in ﬁg. 4). The number of possible hybrid trees is exponential in the num-
ber of mixture nodes, and thus a mixed decomposition is comparable to an exponential ensemble
of tree decompositions. The original tree decompositions, based on T and ¯T, are included in the
ensemble, thus may easily be replicated by the mixed decomposition. On the other hand, many of
the hybrid trees in the mixed decomposition are signiﬁcantly different from T and ¯T, requiring large
size constants from their tree decompositions.
As a ﬁrst step in formalizing the above intuition, we deﬁne the notion of a hybrid mode tree:
Deﬁnition 4 Let T and ¯T be binary mode trees over [N] (def. 1), and let mix(T, ¯T) be a corre-
sponding collection of mixture nodes, i.e. a set of nodes (subsets of [N]) contained in the interior of
both T and ¯T. We say that H is a hybrid mode tree of T and ¯T w.r.t. mix(T, ¯T), if it is a binary
mode tree over [N], whose interior may be generated by the following process:
int(H) = ∅
For µ in mix(T, ¯T) ∪{[N]} (inclusion order):
S = int(T) ∩2µ \ {nodes in T already assigned to S}
¯S = int( ¯T) ∩2µ \ {nodes in ¯T already assigned to ¯S}
int(H) = int(H)∪S
or int(H) = int(H)∪¯S
In words, for every µ that is either a mixture node or the root node, int(H) includes a segment from
either int(T) or int( ¯T), where the segment comprises all descendants of µ (including µ itself) from
which the path to µ does not cross any other mixture node (see illustration in ﬁg. 4).
Claim 5 below states that with proper weight setting, a mixed decomposition of T and ¯T (eq. 4)
with size constant r=rmix can realize any tree decomposition (eq. 3) with size constant r=rmix/2,
if the underlying mode tree is a hybrid of T and ¯T. Since T and ¯T are in particular hybrid mode
trees of themselves, we obtain an afﬁrmative answer to prop. 2.
Claim 5
Let T and ¯T be binary mode trees over [N] (def. 1), and let mix(T, ¯T) be a corre-
sponding collection of mixture nodes (a set of nodes contained in the interior of both T and ¯T).
Consider a mixed decomposition of T and ¯T w.r.t. mix(T, ¯T) (eq. 4), and denote its size con-
stant r by rmix. Let H be a hybrid mode tree of T and ¯T w.r.t. mix(T, ¯T) (def. 4), and con-
sider the respective tree decomposition (eq. 3), with size constant r=rmix/2. For any setting of
weights {aν,γ,I, aν,γ,II}ν,γ leading to grid tensors {Ay}y in this tree decomposition, there exists a
setting of weights {aν,γ,I, aν,γ,II}ν,γ and {¯a¯ν,γ,I, ¯a¯ν,γ,II}¯ν,γ in the mixed decomposition, independent
of the discretizers v(1) . . . v(M) (see sec. 4), that leads to the same grid tensors.8
Proof [sketch – complete proof is given in app. B.1] We prove the claim constructively, by assigning
weights to the mixed decomposition of T and ¯T such that it mimics the tree decomposition of H.
For distinction, we add the relevant mode tree to our notation of weights, letting {aT,ν,γ,I, aT,ν,γ,II ∈
12


## Page 13


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
mode tree T
mode tree T
hybrid mode trees
mixture
nodes
root
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,2}
{3,4}
{5,6}
{15,16}
{7,8}
{9,10}
{11,12}
{13,14}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,5,6,7,8}
{9,10,11,12,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,3}
{2,4}
{5,7}
{14,16}
{6,8}
{9,11}
{10,12}
{13,15}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,9,10,11,12}
{5,6,7,8,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
{1}
{2}
{3}
{4}
{9}
{10}
{11}
{12}
{1,2}
{3,4}
{9,10}
{11,12}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,5,6,7,8}
{9,10,11,12,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,2}
{3,4}
{5,6}
{15,16}
{7,8}
{9,10}
{11,12}
{13,14}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,5,6,7,8}
{9,10,11,12,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,3}
{2,4}
{5,7}
{14,16}
{6,8}
{9,11}
{10,12}
{13,15}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,9,10,11,12}
{5,6,7,8,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
{5}
{6}
{7}
{8}
{5,7}
{6,8}
{13}
{14}
{15}
{16}
{14,16}
{13,15}
leaves
(a)
(b)
Figure 4: Best viewed in color. (a) Two mode trees T and ¯T along with a possible choice of mixture
nodes (same as in ﬁg. 3(a)). (b) Sample of the resulting hybrid mode trees (def. 4). Each
hybrid tree is a combination of segments from T and ¯T, where a segment comprises all
non-leaf descendants of a certain root node or mixture node, from which the path to that
node does not cross any other mixture node.
Rrmix}ν∈int(T),γ∈[rmix] and {a ¯T,ν,γ,I, a ¯T,ν,γ,II ∈Rrmix}ν∈int( ¯T),γ∈[rmix] stand for the weights in the
mixed decomposition of T and ¯T, while {aH,ν,γ,I, aH,ν,γ,II ∈Rrmix/2}ν∈int(H),γ∈[rmix/2] represent
the weights in the tree decomposition of H. We also denote by t(ν), for each node ν∈int(H), the
source tree (T or ¯T) from which it originated (see def. 4).
The assignment of {aT,ν,γ,I, aT,ν,γ,II}ν,γ and {a ¯T,ν,γ,I, a ¯T,ν,γ,II}ν,γ proceeds as follows. All
weights are initialized with zeros. Afterwards, for each ν∈int(H), {aH,ν,γ,I, aH,ν,γ,II}γ (weights
of ν in the tree decomposition of H) are copied into {at(ν),ν,γ,I, at(ν),ν,γ,II}γ (weights of the respec-
tive node at the respective source tree in the mixed decomposition of T and ¯T). There are twice
as many vectors in {at(ν),ν,γ,I, at(ν),ν,γ,II}γ than there are in {aH,ν,γ,I, aH,ν,γ,II}γ, and each vector
is of twice the dimension. The choices of which vectors to use, and which coordinates to use in
the selected vectors, are made such that computations traverse properly between trees. Speciﬁcally,
if P(ν; H) (parent of ν in H) originated from the same tree (T or ¯T) as ν, higher index vectors
(rmix/2 < γ ≤rmix) in {at(ν),ν,γ,I, at(ν),ν,γ,II}γ are used, as they correspond to computations (ten-
sors) that are not exchanged between trees (see eq. 4). On the other hand, if P(ν; H) originated
from the tree opposite to t(ν), lower index vectors (1 ≤γ ≤rmix/2) in {at(ν),ν,γ,I, at(ν),ν,γ,II}γ are
used, in accordance with the fact that they realize computations (tensors) that will be transferred be-
tween trees. The second aforementioned choice – which coordinates to use in the selected vectors,
is made analogously, based on the trees from which CI(ν; H) and CII(ν; H) (children of ν in H)
came from.
13


## Page 14


COHEN TAMARI SHASHUA
tiling
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,2}
{3,4}
{5,6}
{15,16}
{7,8}
{9,10}
{11,12}
{13,14}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,5,6,7,8}
{9,10,11,12,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
index set
mode tree T








;
3,4 , 5,6,7,8 , 9 , 11,12
T


I


3,4,5,6,7,8,9,11,12

I
Figure 5: Mode tree T along with a speciﬁc index set I and the resulting tiling Θ(I; T) (def. 6).
Claim 5 not only addresses prop. 2, but also brings forth a strategy for treating prop. 3. The strat-
egy is to ﬁnd a hybrid mode tree H distinct enough from T and ¯T, such that its tree decomposition,
easily realized by the mixed decomposition according to claim 5, poses a signiﬁcant challenge for
the individual tree decompositions of T and ¯T. Hereinafter we pursue this line of reasoning, focus-
ing on the particular case where the convolutional operator g(·) is a simple product – g(a, b)=a·b. In
this case the tree and mixed decompositions (eq. 3 and 4 respectively) are standard (non-generalized)
tensor decompositions (⊗g≡⊗– see sec. 3), and the corresponding dilated convolutional networks
are convolutional arithmetic circuits. We focus on this special case since it allows the use of a plu-
rality of algebraic tools for theoretical analysis, while at the same time corresponding to models
showing promising results in practice (see for example Cohen et al. (2016a); Sharir et al. (2016)).
Full treatment of additional cases, such as g(a, b)= max{a + b, 0}, corresponding to networks with
ReLU activation, is left for future work.
For establishing the difﬁculty experienced by the tree decompositions of T and ¯T in replicating
that of a hybrid tree H, we analyze ranks of matricized grid tensors. Speciﬁcally, we consider
the tree decomposition (eq. 3) of a general mode tree, and derive tight upper and lower bounds on
the ranks of generated grid tensors when these are subject to matricization w.r.t. a general index
set I ⊂[N] (see sec. 3). The bounds we derive (theorem 7 below) highly depend on both the
underlying mode tree and the index set, and this allows ﬁnding index sets for which ranks tend to
be higher with the hybrid mode tree H than they are with the original mode trees T and ¯T. Under
such index sets, the only way for T and ¯T to match ranks generated with H is through a signiﬁcant
increase in the size constant of their tree decompositions – precisely the sought-after result.
To crisply phrase our main theorem, we deﬁne the notion of an index set tiled by a mode tree:
Deﬁnition 6 Let T be a binary mode tree over [N] (def. 1), and let I ⊂[N] be a non-empty set
of indexes. A tiling of I by T is a collection of nodes in the tree, denoted Θ(I; T), which meets the
following requirements:
• S
ν∈Θ(I;T) ν = I
• ν ∈Θ(I; T) =⇒P(ν; T) ̸⊂I
In words, Θ(I; T) is a set of nodes in T whose disjoint union gives I, where each node is maximal,
i.e. its parent in the tree is not a subset of I (see illustration in ﬁg. 5).
It is not difﬁcult to see that for any mode tree T and non-empty index set I, the tiling Θ(I; T) exists
and is determined uniquely. As theorem 7 below states, this tiling, along with that of I’s comple-
14


## Page 15


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
ment (Ic:=[N]\I), characterizes the ranks of grid tensors generated by the tree decomposition of T
when these are matricized w.r.t. I.
Theorem 7
Let T be a binary mode tree over [N] (def. 1), and consider the corresponding tree
decomposition (eq. 3) with discretizers v(1) . . . v(M) spanning Rr. Assume that g(·) is the product
operator (g(a, b) = a·b), and suppose the generated grid tensors {Ay}y are matricized (see sec. 3)
w.r.t. an index set I ⊂[N], ∅̸= I ̸= [N], whose complement we denote by Ic := [N] \ I. Then,
the ranks of the grid tensor matricizations {JAyKI}y are:
• no greater than rmin{|Θ(I;T)|,|Θ(Ic;T)|}
• at least r|{(ν1,ν2)∈Θ(I;T)×Θ(Ic;T): ν1 and ν2 are siblings in T with depth>1}| almost always, i.e. for all
conﬁgurations of weights {aν,γ,I, aν,γ,II}ν,γ but a set of Lebesgue measure zero
Proof [sketch – complete proof is given in app. B.2] The proof proceeds in three stages. In the
ﬁrst stage we matricize the tree decomposition of T, i.e. transform it from a tensor decomposition
generating {Ay}y to a matrix decomposition generating {JAyKI}y. In this transformation, instances
of the tensor product ⊗convert to a Kronecker product ⊙. The second stage of the proof establishes
the upper bound stated in the theorem, by showing that for each y, JAyKI is equal to a product of
matrices, one of which has size r|Θ(I;T)|-by-r|Θ(Ic;T)|. The key idea in this stage is the propagation
of elements out of the matrix decomposition, using the relation (AA′)⊙(BB′) = (A⊙A′)(B⊙B′).
The third and ﬁnal stage of the proof establishes the lower bound stated in the theorem. Here again,
elements are propagated out of the matrix decomposition, allowing the construction of a concrete
conﬁguration of weights ({aν,γ,I, aν,γ,II}ν,γ) for which the lower bound holds. The fact that the
lower bound holds almost always is then a direct corollary of app. C, where it is shown that the tree
decomposition admits maximal matricization ranks almost always when g(·) is the product operator.
The study of matricization ranks under hierarchical tensor decompositions is of signiﬁcant in-
terest, particularly in the context of deep learning. Cohen et al. (2016b) proved the lower bound
in the theorem for the speciﬁc case where T is the mode tree corresponding to the baseline dilated
convolutional network (see ﬁg. 2(a)), and I = {1, 3, . . . , N−1}. The result was used to estab-
lish exponential expressive efﬁciency of deep convolutional arithmetic circuits w.r.t. shallow ones.
Cohen and Shashua (2017) later extended the analysis by deriving upper bounds for arbitrary index
sets I, using them to study the ability of deep convolutional arithmetic circuits to model correlations
among regions of their input. The bounds used in Cohen and Shashua (2017) were loose, and in
fact trivial for many choices of index sets I. We here treat arbitrary mode trees T and index sets I,
proving upper and lower bounds that are tight, oftentimes exact. Such tight bounds are necessary
for identifying expressive efﬁciency that is not exponential, as we do in this paper. The key to deriv-
ing the bounds is the aforementioned idea of propagating elements out of a matrix decomposition.
As stated previously, given two binary mode trees over [N] (def. 1) – T and ¯T, with a corre-
sponding collection of mixture nodes mix(T, ¯T) (set of nodes interior to both T and ¯T), the bounds
in theorem 7 can be used to ﬁnd an index set I ⊂[N] and a hybrid mode tree H (def. 4), such
that the tree decomposition (eq. 3) of H generates grid tensors whose ranks under matricization
w.r.t. I are much higher than those brought forth by the tree decompositions of T and ¯T. Consider
our exemplar mode trees illustrated in ﬁg. 2. Speciﬁcally, let T be the mode tree corresponding to
the baseline dilated convolutional network (dilation 2l−1 in layer l∈[L]=[log2 N] – see sec. 4.1),
15


## Page 16


COHEN TAMARI SHASHUA
index set
complement
tilings
mode tree T
mode tree T
hybrid mode tree H
mixture
nodes
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,2}
{3,4}
{5,6}
{15,16}
{7,8}
{9,10}
{11,12}
{13,14}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,5,6,7,8}
{9,10,11,12,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
{9}
{10}
{11}
{12}
{13}
{14}
{15}
{16}
{1,3}
{2,4}
{5,7}
{14,16}
{6,8}
{9,11}
{10,12}
{13,15}
{1,2,3,4}
{5,6,7,8}
{9,10,11,12}
{13,14,15,16}
{1,2,3,4,9,10,11,12}
{5,6,7,8,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
{1}
{2}
{3}
{4}
{1,2}
{3,4}
{13}
{14}
{15}
{16}
{14,16}
{13,15}
{5}
{6}
{7}
{8}
{5,6}
{7,8}
{9}
{10}
{11}
{12}
{9,11}
{10,12}







;
1 , 3 , 5 , 7 , 9,10 , 13,14
T


I







;
2 , 4 , 6 , 8 , 11,12 , 15,16
c T


I
tilings







;
1,3 , 5,7 , 9 , 10 , 13 , 14
T


I







;
2,4 , 6,8 , 11 , 12 , 15 , 16
c T


I
tilings





;
1 , 3 , 5 , 7 , 9 , 10 , 13 , 14
H


I





;
2 , 4 , 6 , 8 , 11 , 12 , 15 , 16
c H


I


1,3,5,7,9,10,13,14

I


2,4,6,8,11,12,15,16
c 
I
{1,2,3,4,9,10,11,12}
{5,6,7,8,13,14,15,16}
{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
{1,2,3,4}
{13,14,15,16}
{5,6,7,8}
{9,10,11,12}
Figure 6: Best viewed in color. Two mode trees T and ¯T with a possible choice of mixture nodes
(same as in ﬁg. 3(a) and 4(a)), along with a particular formed hybrid tree H. An index
set I and its complement Ic are tiled into more pieces by H than they are by T and ¯T,
leading the former to generate grid tensors with higher matricization ranks (theorem 7).
and let ¯T be the mode tree corresponding to the network obtained by swapping dilations of even
and odd layers (such that layer l has dilation 2l−2 if l is even, and 2l if l is odd). As described in
sec. 4.2, T is a perfect binary tree whose depth-l nodes, l ∈{0, 1, . . . , L}, are (k−1)N/2l +[N/2l]
for k ∈[2l]. ¯T is also perfect and has the same even-depth nodes, but its odd-depth nodes differ –
they are generated by splitting parents into children holding non-contiguous quadrants. Suppose we
choose mix(T, ¯T) to include the set of nodes in T and ¯T whose depth is L−2, and consider the hy-
brid mode tree H formed by taking the segments (see def. 4) of the ﬁrst half of these nodes from T,
and the rest of the tree from ¯T. An illustration of T, ¯T and H in this setting, for the case L = 4, is
given in ﬁg. 6. Now, let the index set I consist of every second index in [N/2], and every second pair
of indexes in N/2+[N/2], i.e. I := {2k−1 : k ∈[N/4]}∪{N/2+4k−k′ : k ∈[N/8], k′ = 2, 3}.
As illustrated in ﬁg. 6, the mode tree T tiles (see def. 6) the lower half of I into singletons, and its
upper half into pairs. The same applies to T’s tiling of I’s complement Ic := [N] \ I. Moreover,
for every node in the former tiling Θ(I; T), there exists a sibling in the latter Θ(Ic; T) (and vice
versa). By theorem 7, this implies that the tree decomposition of T generates grid tensors whose
matricizations w.r.t. I have rank rN/4+N/8. A similar situation occurs with the mode tree ¯T, under
which I and Ic are tiled into pairs in their lower halves and into singletons in their top halves (see
illustration in ﬁg. 6). This also leads to matricized grid tensors of rank rN/4+N/8. On the other hand,
the hybrid mode tree H tiles I and Ic entirely into singletons (see illustration in ﬁg. 6), leading (by
theorem 7) to grid tensor matricization ranks of rN/2. This means that if we were to replicate grid
tensors generated by the tree decomposition of H using those of T or ¯T (or a summation thereof),
we would need to increase the size constant r super-linearly – by a power of 4/3 (at least).
The above example can be generalized, by considering swapping the dilations of more than two
layers at once. In particular, if T is the mode tree corresponding to the baseline dilated convolutional
network (dilation 2l−1 in layer l), ¯T is the mode tree corresponding to the network obtained by
swapping dilations of groups of k layers (dilation 2⌈l/k⌉·k−1−((l−1) mod k) in layer l), and the set of
mixture nodes includes all nodes of depth L−k, a hybrid mode tree H and an index set I can be
16


## Page 17


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
found, such that the tree decomposition of H generates grid tensors whose ranks when matricized
w.r.t. I can only be matched by the tree decompositions of T and ¯T if their size constant r is
increased by a power of 2/(1 + 21−k). Since the mixed decomposition of T and ¯T (eq. 4) can
realize the tree decomposition of H with double the size constant (claim 5), we conclude that it
can, with size constant 2r, generate grid tensors whose matricization ranks (w.r.t. I) require the tree
decompositions of T and ¯T to have size constant r2/(1+21−k) – super-linearly larger. Therefore, in
this particular setting, prop. 3 holds and the mixed decomposition of T and ¯T is indeed expressively
efﬁcient w.r.t. their tree decompositions. Taking into account the fact that the mixed decomposition
admits maximal matricization ranks almost always when g(·) is the product operator (see app. C),
we formalize the result in network terms:
Corollary 8
Let N be the baseline dilated convolutional network (dilation 2l−1 in layer l – see
sec. 4.1), and let ¯
N be the network obtained by swapping dilations of groups of k layers (dila-
tion 2⌈l/k⌉·k−1−((l−1) mod k) in layer l). Denote by M the mixed dilated convolutional network ob-
tained by summing the outputs of N and ¯
N, while interconnecting their k’th intermediate layer
(and possibly additional layers). Assume the networks’ convolutional operator g(·) is a product.
Then, besides a negligible set, all functions realized by M with r channels in the layers of each
interconnected network, cannot be realized by N or ¯
N (or a summation thereof) if the number of
channels in each layer is less than (r/2)2/(1+21−k).
Corollary 8 (along with claim 5) demonstrates that interconnecting intermediate layers of dif-
ferent dilated convolutional networks can bring forth expressive efﬁciency. That is to say, through
cross-connections between networks, we are able to represent functions that would otherwise be
expensive, or even impractical to implement. The lower bound in corollary 8 – (r/2)2/(1+21−k), is
essentially quadratic when k ≥4. For example, if k = 4 and the number of channels r in each
interconnected network is 128, the lower bound would imply that in order to maintain representa-
tional abilities with an individual network (or a summation of the networks), over 1500 channels in
each layer are required – far beyond acceptable practice in deep learning.
7. Experiment
To assess the practical implications of the expressive efﬁciency brought forth by mixing dilated
convolutional networks, a simple experiment was conducted. We trained a baseline dilated convolu-
tional network N (dilation 2l−1 in layer l ∈[L] – see sec. 4.1) with architectural parameters similar
to those used in WaveNet (van den Oord et al. (2016)), to classify individual phonemes in the TIMIT
acoustic speech corpus (Garofolo et al. (1993)). In addition to the baseline model, we also trained a
companion network ¯
N obtained by swapping dilations of even and odd layers (such that layer l has
dilation 2l−2 if l is even, and 2l if l is odd). As discussed in sec. 5, the mode trees corresponding to
these networks (illustrated in ﬁg. 2) – T and ¯T, share interior nodes of even depth, thus any subset
of those nodes may serve as mixture nodes for a mixed decomposition (eq. 4). We evaluate mixed
dilated convolutional networks M corresponding to different choices of mixture nodes (see ﬁg. 3
for illustration of a particular case). Speciﬁcally, we consider choices of the following form:
mix(T, ¯T) := {ν ∈int(T)∩int( ¯T) : depth of ν (in T and ¯T) ≥threshold}
Varying the threshold yields mixed networks with a varying number of interconnections. In the
extreme case mix(T, ¯T) = ∅(high threshold), M simply sums the outputs of N and ¯
N. As
17


## Page 18


COHEN TAMARI SHASHUA
0
2
4
6
8
10
Connections up to layer
0.68
0.69
0.70
0.71
0.72
Accuracy
TIMIT Individual Phoneme Classification
Validation Set
Train Set
Figure 7: Experimental results – increasing the number of interconnections between hidden layers
of different dilated convolutional networks improves accuracy, with no additional cost in
computation or model capacity.
the threshold decreases interconnections between hidden layers are added – starting from hidden
layer 2, then including hidden layer 4, and so on. The intuition from our analysis (sec. 6) is that
additional interconnections result in a larger ensemble of hybrid mode trees, which in turn boosts the
expressive power of the mixed network M. As ﬁg. 7 shows, this intuition indeed complies with the
results in practice – classiﬁcation accuracy improves as we increase the number of interconnections,
without any additional cost in terms of computation or model capacity.9
It is important to stress that our objective in the experiment was to evaluate, in the most con-
trolled setting possible, the exact models covered by our analysis. We did not compare to state
of the art results, as all phoneme recognition rates reported in the literature deviate from our ba-
sic setting – they heavily rely on data pre-processing (e.g. Mel-Frequency Cepstral Coefﬁcients),
prediction post-processing (e.g. Conditional Random Fields), or both. The recent DeepLab model
(Chen et al. (2016)) has demonstrated that when combined with other techniques, mixing dilated
convolutions can lead to state of the art image segmentation performance. We are currently pursuing
similar results in the context of sequence processing tasks.
To conclude this section, we brieﬂy convey implementation details behind the experiment.
TIMIT dataset is an acoustic-phonetic corpus comprising 6300 sentences manually labeled at the
phoneme level. We split the data into train and validation sets in accordance with Halberstadt
(1998), and as advised by Lee and Hon (1989), mapped the 61 possible phoneme labels into 39
plus an additional “garbage” label. The task was then to classify individual phonemes into one of
the latter categories. In accordance with WaveNet, the baseline dilated convolutional network had
ReLU activation (g(a, b)= max{a+b, 0} – see sec. 4.1),10 32 channels per layer, and input vec-
tors of dimension 256 holding one-hot quantizations of the audio signal. The number of layers L
was set to 12, corresponding to an input window of N=2L=4096 samples, spanning 250ms of
audio signal – standard practice with TIMIT dataset. The framework chosen for running the exper-
iment was Caffe toolbox (Jia et al. (2014)), and we used Adam optimizer (Kingma and Ba (2014))
for training (with default hyper-parameters: moment decay rates β1 = 0.9, β2 = 0.999; learning
rate α = 0.001). Weight decay and batch size were set to 10−5 and 128 respectively. Models were
trained for 35000 iterations, with learning rate decreased by a factor of 10 after 80% of iterations
took place.
18


## Page 19


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
8. Conclusion
Nearly all state of the art deep networks these days (e.g. Szegedy et al. (2015); He et al. (2015);
Huang et al. (2016b,a)) deviate from the simple feed-forward (chain) approach, employing various
connectivity schemes between their layers. In this paper we studied the representational implications
of connectivity in the context of dilated convolutional networks, a family of deep models deliver-
ing state of the art performance in audio and text processing tasks, underlying Google’s WaveNet
(van den Oord et al. (2016)) and ByteNet (Kalchbrenner et al. (2016)). We formulated our study
through the notion of expressive efﬁciency, which refers to a situation where one network must
grow unfeasibly large to realize (or approximate) functions of another. Our analysis shows that
interconnecting hidden layers of different dilated convolutional networks can bring forth a model
that is expressively efﬁcient w.r.t. the individual networks it comprises. In particular, we show that
a single connection between hidden layers can already lead to an almost quadratic gap, which in
large-scale settings typically makes the difference between a model that is practical and one that is
not. We empirically evaluate the analyzed networks, and ﬁnd that the expressive efﬁciency brought
forth by interconnectivity coincides with improved accuracies.
To date, formal analyses studying expressive efﬁciency have focused on the architectural feature
of depth, showing instances where deep networks are expressively efﬁcient w.r.t. shallow ones.
These studies were motivated by the vast empirical evidence supporting the importance of depth.
Our work thus provides a second exemplar of an architectural feature for which expressive efﬁciency
and superior accuracies go hand in hand. This leads us to believe that expressive efﬁciency may
serve a key role in the development of new tools for deep network design.
Notes
1 The viewpoint we adopt is actually a concrete special case of a more abstract algebraic viewpoint of tensor analysis,
as presented for example in Hackbusch (2012). We limit ourselves to this concrete viewpoint since it sufﬁces for our
needs and is easier to grasp.
2 Binary mode trees lead to decompositions (eq. 3) that correspond to networks with size-2 convolutions. We limit
ourselves to this case for simplicity of presentation. Our formulation can easily be extended to account for convolu-
tions of arbitrary size by considering mode trees that are not necessarily binary, and by modifying the decomposition
in eq. 3 to take (generalized) tensor products between an arbitrary number of tensors (not necessarily two).
3 A full binary tree is a tree in which all interior (non-leaf) nodes have exactly two children.
4 In general the number of tensors in the collection may vary across nodes, but for simplicity of presentation we
assume here that all collections comprise exactly r tensors.
5 If c is a scalar and S is a set, c + S stands for the set obtained by adding c to each element in S.
6 It is important to stress that not all choices of mode trees lead to networks resembling ones used in practice. For
example, if different leaves in a tree have different depths, different inputs in the corresponding network pass through
a different number of layers. Conversely, not every type of dilated convolutional network used in practice corresponds
to a mode tree – only ones in which an input is connected to the output through a single path.
7 A few remarks are in order at this point:
• The number of channels in each layer of N or ¯
N corresponds to the constant r in the respective tree decompo-
sition (eq. 3 with underlying mode tree T or ¯T respectively). Similarly, the number of channels in each layer
of each interconnected network in M corresponds to r in the respective mixed decomposition (eq. 4). In both
the tree and mixed decompositions, r, referred to as the size constant, stands for the number of tensors {φν,γ}γ
(respectively {¯φ¯ν,γ}γ) held in each node ν (respectively ¯ν). We set this number uniformly across nodes, corre-
sponding to uniformly sized layers across networks, merely for simplicity of presentation. Our formulations and
analysis can easily be adapted to account for varying layer sizes, by allowing different nodes in a decomposition
19


## Page 20


COHEN TAMARI SHASHUA
to hold a different number of tensors. Note that an implication of our uniform setting is that a network’s input and
output dimensions vary along with the size of its hidden layers. When replicating a function realized by a network
using a larger network, we simply pad input vectors with zeros, and ignore the excess output coordinates.
• An additional simpliﬁcation we made relates to weight sharing. In both the tree and mixed decompositions, each
interior node ν (respectively ¯ν) has a separate set of weights {aν,γ,I, aν,γ,II}γ (respectively {¯a¯ν,γ,I, ¯a¯ν,γ,II}γ).
This implies that in the corresponding networks, convolution ﬁlters may vary through time, i.e. different weights
may be used against different portions of a convolved sequence. The more commonplace setting of stationary
ﬁlters (standard convolutions) is obtained by restricting different nodes in a decomposition to possess the same
weights. We do not introduce such restrictions into our formulations, as they make little difference in terms of the
analysis, but on the other hand signiﬁcantly burden presentation.
8 In accordance with the remark given at the beginning of this section, when using the (larger) mixed decomposition,
we pad discretizers with zeros, and ignore the excess output tensors.
9 We note that in addition to the mixed dilated convolutional network M, we also evaluated the individual networks N
and ¯
N – both reached accuracies comparable to M in the case of zero interconnections (output summation only).
10 The case of convolutional arithmetic circuits (g(a, b)=a·b) was also evaluated, leading to the exact same trends as
those observed with ReLU (ﬁg. 7).
Acknowledgments
This work was supported by Intel grant ICRI-CI #9-2012-6133, by ISF Center grant 1790/12, and
by the European Research Council (TheoryDL project). Nadav Cohen was supported by a Google
Doctoral Fellowship in Machine Learning.
References
Richard Bellman. Introduction to matrix analysis, volume 960. SIAM, 1970.
Richard Caron and Tim Traynor. The zero set of a polynomial. WSMR Report 05-02, 2005.
Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos, Kevin Murphy, and Alan L Yuille. Deeplab:
Semantic image segmentation with deep convolutional nets, atrous convolution, and fully connected crfs.
arXiv preprint arXiv:1606.00915, 2016.
Nadav Cohen and Amnon Shashua. Convolutional rectiﬁer networks as generalized tensor decompositions.
International Conference on Machine Learning (ICML), 2016.
Nadav Cohen and Amnon Shashua. Inductive bias of deep convolutional networks through pooling geometry.
International Conference on Learning Representations (ICLR), 2017.
Nadav Cohen, Or Sharir, and Amnon Shashua. Deep simnets. IEEE Conference on Computer Vision and
Pattern Recognition (CVPR), 2016a.
Nadav Cohen, Or Sharir, and Amnon Shashua. On the expressive power of deep learning: A tensor analysis.
Conference On Learning Theory (COLT), 2016b.
Olivier Delalleau and Yoshua Bengio. Shallow vs. deep sum-product networks. In Advances in Neural
Information Processing Systems, pages 666–674, 2011.
Ronen Eldan and Ohad Shamir.
The power of depth for feedforward neural networks.
arXiv preprint
arXiv:1512.03965, 2015.
20


## Page 21


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
John S Garofolo, Lori F Lamel, William M Fisher, Jonathon G Fiscus, and David S Pallett. Darpa timit
acoustic-phonetic continous speech corpus cd-rom. nist speech disc 1-1.1. NASA STI/Recon technical
report n, 93, 1993.
Wolfgang Hackbusch.
Tensor Spaces and Numerical Tensor Calculus, volume 42 of Springer Series in
Computational Mathematics. Springer Science & Business Media, Berlin, Heidelberg, February 2012.
Andrew K Halberstadt. Heterogeneous acoustic measurements and multiple classiﬁers for speech recogni-
tion. PhD thesis, Massachusetts Institute of Technology, 1998.
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition.
arXiv preprint arXiv:1512.03385, 2015.
Gao Huang, Zhuang Liu, Kilian Q Weinberger, and Laurens van der Maaten. Densely connected convolu-
tional networks. arXiv preprint arXiv:1608.06993, 2016a.
Gao Huang, Yu Sun, Zhuang Liu, Daniel Sedra, and Kilian Q Weinberger. Deep networks with stochastic
depth. In European Conference on Computer Vision, pages 646–661. Springer, 2016b.
Majid Janzamin, Hanie Sedghi, and Anima Anandkumar. Beating the Perils of Non-Convexity: Guaranteed
Training of Neural Networks using Tensor Methods. CoRR abs/1506.08473, 2015.
Yangqing Jia, Evan Shelhamer, Jeff Donahue, Sergey Karayev, Jonathan Long, Ross Girshick, Sergio Guadar-
rama, and Trevor Darrell. Caffe: Convolutional architecture for fast feature embedding. In Proceedings of
the 22nd ACM international conference on Multimedia, pages 675–678. ACM, 2014.
Frank Jones. Lebesgue integration on Euclidean space. Jones & Bartlett Learning, 2001.
Nal Kalchbrenner, Lasse Espeholt, Karen Simonyan, Aaron van den Oord, Alex Graves, and Koray
Kavukcuoglu. Neural machine translation in linear time. arXiv preprint arXiv:1610.10099, 2016.
Diederik Kingma and Jimmy Ba.
Adam:
A method for stochastic optimization.
arXiv preprint
arXiv:1412.6980, 2014.
Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. ImageNet Classiﬁcation with Deep Convolutional
Neural Networks. Advances in Neural Information Processing Systems, pages 1106–1114, 2012.
Yann LeCun and Yoshua Bengio. Convolutional networks for images, speech, and time series. The handbook
of brain theory and neural networks, 3361(10), 1995.
Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning. Nature, 521(7553):436–444, May 2015.
K-F Lee and H-W Hon. Speaker-independent phone recognition using hidden markov models. IEEE Trans-
actions on Acoustics, Speech, and Signal Processing, 37(11):1641–1648, 1989.
Hrushikesh Mhaskar, Qianli Liao, and Tomaso Poggio. Learning real and boolean functions: When is deep
better than shallow. arXiv preprint arXiv:1603.00988, 2016.
Guido F Montufar, Razvan Pascanu, Kyunghyun Cho, and Yoshua Bengio. On the number of linear regions
of deep neural networks. In Advances in Neural Information Processing Systems, pages 2924–2932, 2014.
Vinod Nair and Geoffrey E Hinton. Rectiﬁed linear units improve restricted boltzmann machines. In Pro-
ceedings of the 27th International Conference on Machine Learning (ICML-10), pages 807–814, 2010.
Razvan Pascanu, Guido Montufar, and Yoshua Bengio. On the number of inference regions of deep feed
forward networks with piece-wise linear activations. arXiv preprint arXiv, 1312, 2013.
21


## Page 22


COHEN TAMARI SHASHUA
Tomaso Poggio, Fabio Anselmi, and Lorenzo Rosasco. I-theory on depth vs width: hierarchical function
composition. Technical report, Center for Brains, Minds and Machines (CBMM), 2015.
Ben Poole, Subhaneil Lahiri, Maithreyi Raghu, Jascha Sohl-Dickstein, and Surya Ganguli. Exponential ex-
pressivity in deep neural networks through transient chaos. In Advances In Neural Information Processing
Systems, pages 3360–3368, 2016.
Maithra Raghu, Ben Poole, Jon Kleinberg, Surya Ganguli, and Jascha Sohl-Dickstein. On the expressive
power of deep neural networks. arXiv preprint arXiv:1606.05336, 2016.
Hanie Sedghi and Anima Anandkumar. Training input-output recurrent neural networks through spectral
methods. arXiv preprint arXiv:1603.00954, 2016.
Or Sharir, Ronen Tamari, Nadav Cohen, and Amnon Shashua. Tensorial mixture models. arXiv preprint
arXiv:1610.04167, 2016.
Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan,
Vincent Vanhoucke, and Andrew Rabinovich. Going Deeper with Convolutions. CVPR, 2015.
Matus Telgarsky. Representation beneﬁts of deep feedforward networks. arXiv preprint arXiv:1509.08101,
2015.
A¨aron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalch-
brenner, Andrew Senior, and Koray Kavukcuoglu. Wavenet: A generative model for raw audio. CoRR
abs/1609.03499, 2016.
22


## Page 23


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
Appendix A. Derivation of the Baseline Decomposition
In this appendix we derive the baseline decomposition (eq. 2) – a parameterization of grid tensors
(eq. 1) discretizing input-output mappings of the baseline dilated convolutional network (ﬁg. 1).
As discussed in sec. 4.1, o[t] – the network output at time t, is a function of x[t-N+1] . . . x[t] –
its input over the last N := 2L time points. We would like to show that for any d1. . .dN ∈
[M], entry (d1, . . . , dN) of a tensor Ay generated by eq. 2, is equal to coordinate y of network
output o[t] under the following input assignment: x[t-N+1] = v(d1), . . . , x[t] = v(dN). To achieve
this, we prove by induction that under the latter assignment, for every l ∈[L] ∪{0}, j ∈[N/2l]
and γ ∈[rl], coordinate γ of the network’s depth-l sequence (input (x[t])t for l = 0; hidden
sequence (h(l)[t])t for l ∈[L −1]; output (o[t])t for l = L) at time t −N + j·2l, is equal to
entry (d(j−1)2l+1, . . . , d(j−1)2l+2l) of the tensor φl,j,γ in the baseline decomposition (eq. 2). The
desired result then follows from the case l = L, j = 1, γ = y.
When l = 0, the inductive hypothesis is trivial – coordinate γ of the input sequence at time t −
N+j, i.e. x[t−N+j]γ, is by deﬁnition of our assignment equal to v(dj)
γ
– entry dj of the tensor φ0,j,γ
(see eq. 2). Assume now that the inductive hypothesis holds whenever l = k, and consider the
tensor φk+1,j,γ for some j ∈[N/2k+1] and γ ∈[rk+1]. From the baseline decomposition (eq. 2):
φk+1,j,γ =
Xrk
α=1 ak+1,γ,I
α
· φk,2j−1,α
⊗g
Xrk
α=1 ak+1,γ,II
α
· φk,2j,α
Focusing on entry (d(j−1)2k+1+1, . . . , d(j−1)2k+1+2k+1) of the left-hand side, while recalling the
deﬁnition of the generalized tensor product ⊗g (sec. 3), we may write:
φk+1,j,γ
d(j−1)2k+1+1,...,d(j−1)2k+1+2k+1 =
g
Prk
α=1 ak+1,γ,I
α
· φk,2j−1,α
d(2j−2)2k+1,...,d(2j−2)2k+2k, Prk
α=1 ak+1,γ,II
α
· φk,2j,α
d(2j−1)2k+1,...,d(2j−1)2k+2k

(5)
By our inductive assumption:
φk,2j−1,α
d(2j−2)2k+1,...,d(2j−2)2k+2k
=
h(k)[t −N + (2j −1)·2k]α
∀α ∈[rk]
φk,2j,α
d(2j−1)2k+1,...,d(2j−1)2k+2k
=
h(k)[t −N + 2j·2k]α
∀α ∈[rk]
where we overload notation in the case k = 0, letting (h(0)[t])t stand for the input sequence (x[t])t.
Plugging the latter into eq. 5, we obtain:
φk+1,j,γ
d(j−1)2k+1+1,...,d(j−1)2k+1+2k+1 =
g
 
ak+1,γ,I, h(k)[t −N + (2j −1)·2k]

,

ak+1,γ,II, h(k)[t −N + 2j·2k]

By the deﬁnition of the baseline dilated convolutional network (sec. 4.1), the latter expression is
precisely equal to coordinate γ of the sequence (h(k+1)[t])t (or (o[t])t if k = L −1) at time t −
N + j·2k+1. This proves that our inductive hypothesis holds when l = k + 1, and in general.
Appendix B. Deferred Proofs
B.1. Proof of Claim 5
We initiate the proof by introducing notations that will allow a more compact presentation. Here-
inafter, we let {aH,ν,γ,I, aH,ν,γ,II ∈Rrmix/2}ν∈int(H),γ∈[rmix/2] stand for the weights in the tree
23


## Page 24


COHEN TAMARI SHASHUA
decomposition of the hybrid mode tree H (eq. 3 with size constant r = rmix/2 and underly-
ing mode tree given by def. 4). Similarly, we use {aT,ν,γ,I, aT,ν,γ,II ∈Rrmix}ν∈int(T),γ∈[rmix]
and {a ¯T,ν,γ,I, a ¯T,ν,γ,II ∈Rrmix}ν∈int( ¯T),γ∈[rmix] to denote the weights, corresponding to T and ¯T
(respectively), in the mixed decomposition (eq. 4 with size constant r = rmix). Recall that by con-
struction (def. 4), int(H) – the interior of H, consists of different segments (collections of nodes),
each taken from either int(T) or int( ¯T). We deﬁne t : int(H) →{T, ¯T} to be the function indi-
cating which tree an interior node in H came from. Speciﬁcally, if the node ν∈int(H) originated
from T we have t(ν) = T, and on the other hand, if its source is ¯T then t(ν) = ¯T. By convention,
feeding t(·) with an argument outside int(H) yields something that is different from both T and ¯T.
For example, if ν∈int(H) is the root node, i.e. ν = [N], then P(ν; H) – its parent in H, is unde-
ﬁned and we have t(P(ν; H))̸=t(ν). Similarly, if the child CI(ν; H) of ν∈int(H) is a leaf, it is
outside the domain of t(·) and thus t(ν)̸=t(CI(ν; H)).
Given a setting of weights {aH,ν,γ,I, aH,ν,γ,II}ν,γ for the tree decomposition of H, we would like
to show that there exists a setting of weights {aT,ν,γ,I, aT,ν,γ,II}ν,γ and {a ¯T,ν,γ,I, a ¯T,ν,γ,II}ν,γ for the
mixed decomposition of T and ¯T, such that the latter generates grid tensors identical to those of
the former. More precisely, for any collection of discretizers {v(i) ∈Rrmix/2}i∈[M] fed into the
tree decomposition of H, leading the latter to produce grid tensors {Ay}y∈[rmix/2], we would like
the mixed decomposition to be such that when fed with the padded discretizers {[(v(i))⊤0]⊤∈
Rrmix}i∈[M], the ﬁrst rmix/2 grid tensors it generates are equal to {Ay}y∈[rmix/2]. We prove ex-
istence of the sought after weight setting constructively, by presenting an explicit procedure for
assigning {aT,ν,γ,I, aT,ν,γ,II}ν,γ and {a ¯T,ν,γ,I, a ¯T,ν,γ,II}ν,γ based on {aH,ν,γ,I, aH,ν,γ,II}ν,γ:
Initialize:
aT,ν,γ,I = aT,ν,γ,II = 0
∀ν∈int(T), γ ∈[rmix]
a
¯T,ν,γ,I = a
¯T,ν,γ,II = 0
∀ν∈int( ¯T), γ ∈[rmix]
For ν in int(H) (depth-ﬁrst order):
at(ν),ν,γ+ 1
2 rmix,I =
( 
0⊤(aH,ν,γ,I)⊤⊤
, t(ν) = t(CI(ν; H))

(aH,ν,γ,I)⊤0⊤⊤
, t(ν) ̸= t(CI(ν; H))
∀γ ∈[rmix/2]
at(ν),ν,γ+ 1
2 rmix,II =
( 
0⊤(aH,ν,γ,II)⊤⊤
, t(ν) = t(CII(ν; H))

(aH,ν,γ,II)⊤0⊤⊤
, t(ν) ̸= t(CII(ν; H))
∀γ ∈[rmix/2]
If t(P(ν; H)) ̸= t(ν) :
Swap at(ν),ν,γ,I ←→at(ν),ν,γ+ 1
2 rmix,I
∀γ ∈[rmix/2]
Swap at(ν),ν,γ,II ←→at(ν),ν,γ+ 1
2 rmix,II ∀γ ∈[rmix/2]
(6)
The idea behind this assignment is as follows. The computation corresponding to a node in the
tree decomposition of H, is carried out, in the mixed decomposition of T and ¯T, by the re-
spective node in the respective source tree. That is to say, the computation of ν∈int(H) in the
tree decomposition is carried out by ν∈int(t(ν)) in the mixed decomposition. ν∈int(t(ν)) uses
half (rmix/2) of its weight vectors, and in each used weight vector, half (rmix/2) of the coordi-
nates hold actual (non-zero) values – a copy of the respective weight from ν∈int(H). The choice
of which weight vectors to use, and which coordinates to use in the active weight vectors, de-
24


## Page 25


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
pends on the tree-transitioning scheme. If the parent of ν in H came from the same tree as ν,
i.e. t(P(ν; H)) = t(ν), ν∈int(t(ν)) in the mixed decomposition uses weight vectors with higher
indexes (γ∈rmix/2 + [rmix/2]), as these relate to tensors that are not exchanged (see eq. 4). On
the other hand, if t(P(ν; H))̸=t(ν), weight vectors with lower indexes (γ ∈[rmix/2]) are used, so
that the computations (tensors) will be sent to the opposite tree. The analogous rationale holds for
the children of ν in H (CI(ν; H) and CII(ν; H)). If a child came from the same tree as ν, upper
coordinates of the appropriate weight vectors are used, so that computations (tensors) coming from
the present tree are collected. On the other hand, if the child came from the opposite tree, lower co-
ordinates are used and computations (tensors) from that tree are fetched. Altogether, the assignment
in eq. 6 meets our requirements, and thus concludes the proof.
■
B.2. Proof of Theorem 7
Since we are dealing with a single particular mode tree T, we omit it from our notations throughout
the proof. Speciﬁcally, we denote by CI(ν) and CII(ν) (instead of CI(ν; T) and CII(ν; T)) the
children of an interior node ν∈int(T); by Θ(I) and Θ(Ic) (instead of Θ(I; T) and Θ(Ic; T))
the tilings of I and Ic (respectively) w.r.t. T (see def. 6); and by σ(ν)(·) (instead of σ(ν;T)(·)) the
permutation corresponding to ν∈int(T) in the tree decomposition (eq. 3).
The ﬁrst stage of the proof is to derive a matricized form of the tree decomposition, shedding
light into the manner in which grid tensor matricizations {JAyKI}y are generated. As a preparatory
step in this direction, we deﬁne the notion of an index set reduction. Let ν ⊂[N] be a node in T,
whose elements we denote by i1 < · · · < i|ν|. The reduction of I onto ν is deﬁned as follows:
I|ν := {j ∈[|ν|] : ij ∈I ∩ν}
(7)
In words, it is the set of indexes corresponding to the intersection I ∩ν inside ν. Besides index set
reduction, an additional tool we will be using is the Kronecker product – a matrix operator we denote
by ⊙. For two matrices A ∈RM1×M2 and B ∈RN1×N2, A⊙B is the matrix in RM1N1×M2N2
holding AijBkl in row index (i −1)N1 + k and column index (j −1)N2 + l.
Consider the central relation in the tree decomposition (eq. 3), while noticing that ⊗g ≡⊗in
our setting (g(·) is the product operator – see sec. 3):
φν,γ
|{z}
order 2|ν|
= σ(ν) Xr
α=1 aν,γ,I
α
· φCI(ν),α
⊗
Xr
α=1 aν,γ,II
α
· φCII(ν),α
(8)
Suppose we would like to matricize the tensor φν,γ w.r.t. the reduction I|ν. If all elements of CI(ν)
were smaller than those of CII(ν), the permutation σ(ν)(·) would be the identity (see sec. 4.2), and
the following matrix relation would hold:
Jφν,γKI|ν
=
rXr
α=1 aν,γ,I
α
· φCI(ν),α
⊗
Xr
α=1 aν,γ,II
α
· φCII(ν),αz
I|ν
=
rXr
α=1 aν,γ,I
α
· φCI(ν),αz
I|CI(ν)
⊙
rXr
α=1 aν,γ,II
α
· φCII(ν),αz
I|CII(ν)
=
Xr
α=1 aν,γ,I
α
· JφCI(ν),αKI|CI(ν)

⊙
Xr
α=1 aν,γ,II
α
· JφCII(ν),αKI|CII(ν)

25


## Page 26


COHEN TAMARI SHASHUA
In general however, elements in CI(ν) could be greater than ones in CII(ν), and so eq. 8 includes a
tensor mode sorting via σ(ν)(·). In matricized form, this amounts to rearranging rows and columns
through appropriate permutation matrices Q(ν) and ¯Q(ν) respectively:
Jφν,γKI|ν = Q(ν) Xr
α=1 aν,γ,I
α
· JφCI(ν),αKI|CI(ν)

⊙
Xr
α=1 aν,γ,II
α
· JφCII(ν),αKI|CII(ν)

¯Q(ν)
We thus arrive at the following matrix form of eq. 3, referred to as the matricized tree decomposition:
For j = 1. . .N:
Jφ{j},γKI|{j} =
r
[v(1)
γ , . . . , v(M)
γ
]⊤z
I|{j}
∀γ ∈[r]
For ν in int(T) (depth-ﬁrst order):
Jφν,γKI|ν = Q(ν)
  
r
X
α=1
aν,γ,I
α
JφCI(ν),αKI|CI(ν)
!
⊙
 
r
X
α=1
aν,γ,II
α
JφCII(ν),αKI|CII(ν)
!!
¯Q(ν) ∀γ ∈[r]
JAyKI = Jφ[N],yKI|[N] ∀y ∈[r]
(9)
Next, we move on to the second stage of the proof, where we establish the upper bound stated
in the theorem:
rankJAyKI ≤rmin{|Θ(I)|,|Θ(Ic)|}
∀y
(10)
We begin by “propagating outwards” the permutation matrices Q([N]) and ¯Q([N]) corresponding to
the root node [N] in the matricized tree decomposition (eq. 9). Namely, for every γ ∈[r], we
replace the matrix Jφ[N],γKI|[N] by:
B[N],γ :=
 
r
X
α=1
a[N],γ,I
α
JφCI([N]),αKI|CI([N])
!
⊙
 
r
X
α=1
a[N],γ,II
α
JφCII([N]),αKI|CII([N])
!
and accordingly move Q([N]) and ¯Q([N]) to the assignments of {JAyKI}y. This gives rise to the
following decomposition:
For j = 1. . .N:
Jφ{j},γKI|{j} =
r
[v(1)
γ , . . . , v(M)
γ
]⊤z
I|{j}
∀γ ∈[r]
For ν in int(T) \ {[N]} (depth-ﬁrst order):
Jφν,γKI|ν = Q(ν)
  
r
X
α=1
aν,γ,I
α
JφCI(ν),αKI|CI(ν)
!
⊙
 
r
X
α=1
aν,γ,II
α
JφCII(ν),αKI|CII(ν)
!!
¯Q(ν) ∀γ ∈[r]
B[N],γ =
 
r
X
α=1
a[N],γ,I
α
JφCI([N]),αKI|CI([N])
!
⊙
 
r
X
α=1
a[N],γ,II
α
JφCII([N]),αKI|CII([N])
!
∀γ ∈[r]
JAyKI = Q([N])B[N],y ¯Q([N]) ∀y ∈[r]
Consider now CI([N]) – a child of the root node [N], and suppose we would like to similarly prop-
agate outwards its permutation matrices Q(CI([N])) and ¯Q(CI([N])). We may deﬁne, for every γ∈[r]:
BCI([N]),γ :=
 
r
X
α=1
aCI([N]),γ,I
α
JφCI(CI([N])),αKI|CI(CI([N]))
!
⊙
 
r
X
α=1
aCI([N]),γ,II
α
JφCII(CI([N])),αKI|CII(CI([N]))
!
26


## Page 27


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
which in turn implies:
B[N],γ
=
 
r
X
α=1
a[N],γ,I
α
Q(CI([N]))BCI([N]),α ¯Q(CI([N]))
!
⊙
 
r
X
α=1
a[N],γ,II
α
JφCII([N]),αKI|CII([N])
!
=
 
Q(CI([N]))
 
r
X
α=1
a[N],γ,I
α
BCI([N]),α
!
¯Q(CI([N]))
!
⊙
 
r
X
α=1
a[N],γ,II
α
JφCII([N]),αKI|CII([N])
!
Now, for any matrices A, A′, B, B′ such that AA′ and BB′ are deﬁned, the following equality
holds: (AA′)⊙(BB′) = (A⊙A′)(B⊙B′) (see Bellman (1970) for proof). We may therefore write:
B[N],γ =

Q(CI([N]))⊙I
   
r
X
α=1
a[N],γ,I
α
BCI([N]),α
!
⊙
 
r
X
α=1
a[N],γ,II
α
JφCII([N]),αKI|CII([N])
!! 
¯Q(CI([N]))⊙¯I

where I and ¯I are identity matrices of appropriate sizes.
Propagating outwards the matrices
Q(CI([N]))⊙I and ¯Q(CI([N]))⊙¯I (while redeﬁning B[N],γ appropriately), we arrive at the following
decomposition:
For j = 1. . .N:
Jφ{j},γKI|{j} =
r
[v(1)
γ , . . . , v(M)
γ
]⊤z
I|{j}
∀γ ∈[r]
For ν in int(T) \ {[N], CI([N])} (depth-ﬁrst order):
Jφν,γKI|ν = Q(ν)
  
r
X
α=1
aν,γ,I
α
JφCI(ν),αKI|CI(ν)
!
⊙
 
r
X
α=1
aν,γ,II
α
JφCII(ν),αKI|CII(ν)
!!
¯Q(ν) ∀γ ∈[r]
BCI([N]),γ =
 
r
X
α=1
aCI([N]),γ,I
α
JφCI(CI([N])),αKI|CI(CI([N]))
!
⊙
 
r
X
α=1
aCI([N]),γ,II
α
JφCII(CI([N])),αKI|CII(CI([N]))
!
∀γ ∈[r]
B[N],γ =
 
r
X
α=1
a[N],γ,I
α
BCI([N]),α
!
⊙
 
r
X
α=1
a[N],γ,II
α
JφCII([N]),αKI|CII([N])
!
∀γ ∈[r]
JAyKI =

Q([N])(Q(CI([N]))⊙I)

B[N],y 
( ¯Q(CI([N]))⊙¯I) ¯Q([N])
∀y ∈[r]
Continuing this process, we propagate outwards the permutation matrices Q(ν) and ¯Q(ν) of all
nodes ν in the tree that are not members of the tilings Θ(I) or Θ(Ic) (see def. 6), and are not
27


## Page 28


COHEN TAMARI SHASHUA
descendants of such. This brings forth the following decomposition:
For j = 1. . .N:
Jφ{j},γKI|{j} =
r
[v(1)
γ , . . . , v(M)
γ
]⊤z
I|{j}
∀γ ∈[r]
For ν in int(T)∩{nodes in Θ(I) or Θ(Ic) or descendants of such} (depth-ﬁrst order):
Jφν,γKI|ν = Q(ν)
  
r
X
α=1
aν,γ,I
α
JφCI(ν),αKI|CI(ν)
!
⊙
 
r
X
α=1
aν,γ,II
α
JφCII(ν),αKI|CII(ν)
!!
¯Q(ν) ∀γ ∈[r]
For ν in Θ(I) ∪Θ(Ic):
Bν,γ = Jφν,γKI|ν ∀γ ∈[r]
For ν in int(T)\{nodes in Θ(I) or Θ(Ic) or descendants of such} (depth-ﬁrst order):
Bν,γ =
 
r
X
α=1
aν,γ,I
α
BCI(ν),α
!
⊙
 
r
X
α=1
aν,γ,II
α
BCII(ν),α
!
∀γ ∈[r]
JAyKI = A·B[N],y· ¯A ∀y ∈[r], for appropriate matrices A and ¯A
Consider now a node ν∈int(T) whose child belongs to a tiling – without loss of generality CI(ν)
belongs to Θ(I). Notice that in this case BCI(ν),α is a column vector for every α ∈[r]. We may
thus deﬁne BCI(ν) to be the matrix whose α’th column is BCI(ν),α, and get the following equalities:
Bν,γ =

BCI(ν)aν,γ,I
⊙
Xr
α=1 aν,γ,II
α
BCII(ν),α
=

BCI(ν)⊙I
 
aν,γ,I ⊙
Xr
α=1 aν,γ,II
α
BCII(ν),α
where again, I is an appropriately sized identity matrix. This implies that we can propagate out-
wards BCI(ν)⊙I, just as we have done with permutation matrices. Applying this procedure to all
nodes in the tilings Θ(I) and Θ(Ic), we arrive at the decomposition below:
For ν in Θ(I):
Bν,γ = e(γ)
∀γ ∈[r]
For ν in Θ(Ic):
Bν,γ = (e(γ))⊤
∀γ ∈[r]
For ν in int(T)\{nodes in Θ(I) or Θ(Ic) or descendants of such} (depth-ﬁrst order):
Bν,γ =
 
r
X
α=1
aν,γ,I
α
BCI(ν),α
!
⊙
 
r
X
α=1
aν,γ,II
α
BCII(ν),α
!
∀γ ∈[r]
JAyKI = A·B[N],y· ¯A ∀y ∈[r], for appropriate matrices A and ¯A
Notice that for compactness in writing we made use of the fact that aν,γ,I = Pr
α=1 aν,γ,II
α
e(α),
where e(α), α ∈[r], is the vector in Rr holding 1 in entry α and 0 in the rest. Note also that
in this decomposition, as opposed to the previous ones, the matrices A and ¯A are not global
constants that depend only on T. Rather, they also depend on Jφν,γKI|ν for tiling nodes ν ∈
Θ(I)∪Θ(Ic), and thus are ultimately determined through a hidden computation that is not speciﬁed
above. This hidden computation is outside our scope, as we are only interested in the size of the
matrices {B[N],y}y. It is not difﬁcult to see that this size is precisely r|Θ(I)|-by-r|Θ(Ic)|, meaning
that the ranks of {B[N],y}y are no more than rmin{|Θ(I)|,|Θ(Ic)|}. Since these ranks are greater than
or equal to those of {JAyKI}y, the sought after upper bound (eq. 10) indeed holds.
28


## Page 29


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
In the third and ﬁnal stage of the proof, we establish the lower bound stated in the theorem,
namely, that for all conﬁgurations of weights {aν,γ,I, aν,γ,II}ν,γ but a set of Lebesgue measure zero:
rankJAyKI ≥r|{(ν1,ν2)∈Θ(I)×Θ(Ic): ν1 and ν2 are siblings in T with depth>1}|
∀y
(11)
We reduce the problem in three successive steps:
• A tree decomposition (eq. 3) with a product operator g(·) admits maximal matricization ranks
almost always (see app. C). Therefore, to prove that eq. 11 holds for all weight settings but
a set of Lebesgue measure zero, it sufﬁces to ﬁnd a particular weight setting for which the
inequality holds.
• By assumption, the discretizers {v(i)}i∈[M] span Rr. Without loss of generality, assume
that {v(i)}i∈[r] are linearly independent, and consider the sub-tensors of {Ay}y formed by
restricting their indexes to the range 1. . .r (instead of 1. . .M). The matricizations of these
sub-tensors w.r.t. I are sub-matrices of {JAyKI}y, thus any lower bound on ranks of the
former matricizations immediately translates to a lower bound on ranks of the latter. Since
the sub-tensors are precisely the grid tensors that would have been generated by the tree
decomposition (eq. 3) had we omitted the trailing discretizers {v(i)}i∈[M]\[r], establishing
eq. 11 in the case M = r proves that it holds in general (M≥r).
• Bearing in mind that we assume M = r (and linear independence of {v(i)}i∈[r]), denote
by V the r-by-r matrix holding v(i) in its i’th row, i.e. V := [v(1) · · · v(r)]⊤. From the
tree decomposition (eq. 3) it is evident that the discretizers affect generated grid tensors only
through products of the form V aν,γI or V aν,γII, where ν is a parent of a leaf node in T.
Since V is invertible ({v(i)}i∈[r] are linearly independent), its exact value has no effect on
the class of representable grid tensors – any change it undergoes may be accounted for by the
weights aν,γI and aν,γII that multiply it (these weights do not appear elsewhere in the decom-
position). Accordingly, for establishing a lower bound on achievable grid tensor matricization
ranks, the value of V is irrelevant (so long as it is invertible), and we may assume, without
loss of generality, that V is the identity matrix, i.e. that v(i) = e(i) for all i ∈[r].
Taking into account the above reductions, our objective is to show that there exists a setting of
weights {aν,γ,I, aν,γ,II}ν,γ, such that the following special case of the matricized tree decomposition
(eq. 9) generates matricizations meeting the lower bound in eq. 11:
For j in I:
Jφ{j},γKI|{j} = e(γ)
∀γ ∈[r]
For j in Ic:
Jφ{j},γKI|{j} = (e(γ))⊤
∀γ ∈[r]
For ν in int(T) (depth-ﬁrst order):
Jφν,γKI|ν = Q(ν)
  
r
X
α=1
aν,γ,I
α
JφCI(ν),αKI|CI(ν)
!
⊙
 
r
X
α=1
aν,γ,II
α
JφCII(ν),αKI|CII(ν)
!!
¯Q(ν) ∀γ ∈[r]
JAyKI = Jφ[N],yKI|[N]
∀y ∈[r]
29


## Page 30


COHEN TAMARI SHASHUA
Similarly to the procedure carried out in the second stage of the proof (establishing the upper bound
in eq. 10), we now propagate outwards the permutation matrices Q(ν) and ¯Q(ν) corresponding to all
interior nodes ν∈int(T). This brings forth the following decomposition:
For j in I:
B{j},γ = e(γ)
∀γ ∈[r]
For j in Ic:
B{j},γ = (e(γ))⊤
∀γ ∈[r]
For ν in int(T) (depth-ﬁrst order):
Bν,γ =
 
r
X
α=1
aν,γ,I
α
BCI(ν),α
!
⊙
 
r
X
α=1
aν,γ,II
α
BCII(ν),α
!
∀γ ∈[r]
JAyKI = A·B[N],y· ¯A ∀y ∈[r], for appropriate matrices A and ¯A
(12)
The matrices A and ¯A in the assignments of {JAyKI}y essentially collect all permutation ma-
trices {Q(ν)}ν and { ¯Q(ν)}ν (respectively) that have been propagated outwards. Speciﬁcally, A
(respectively ¯A) is a product of factors, each of the form I⊙Q(ν)⊙I′ (respectively I⊙¯Q(ν)I′) for
a different interior node ν and appropriately sized identity matrices I and I′. Since permutation
matrices are invertible, and since the Kronecker product between two invertible matrices is invert-
ible as well (see Bellman (1970) for proof), we conclude that the matrices A and ¯A are invertible.
Therefore, for every y ∈[r], the rank of JAyKI is equal to that of B[N],y. It thus sufﬁces to ﬁnd a
setting of weights {aν,γ,I, aν,γ,II}ν,γ for which:
rank(B[N],γ) ≥r|{(ν1,ν2)∈Θ(I)×Θ(Ic): ν1 and ν2 are siblings in T with depth>1}|
∀γ ∈[r]
(13)
Disregard the trivial case where there exist siblings ν1 ∈Θ(I) and ν2 ∈Θ(Ic) of depth 1,1 and
consider the following weight setting:
• ν is a node in Θ(I) or Θ(Ic), or a descendant of such:
aν,γ,I = aν,γ,II = e(γ)
∀γ ∈[r]
• ν has one child in Θ(I) and the other in Θ(Ic):
aν,γ,I = aν,γ,II = e(γ)
∀γ ∈[r]
• ν is the root node [N]:
aν,γ,I = aν,γ,II = e(1)
∀γ ∈[r]
• ν meets neither of the above (0 and 1 here denote the all-zero and all-one vectors in Rr,
respectively):
aν,1,I =
 1
, CI(ν) has one child in Θ(I) and the other in Θ(Ic)
e(1)
, otherwise
aν,1,II =
 1
, CII(ν) has one child in Θ(I) and the other in Θ(Ic)
e(1)
, otherwise
aν,γ,I = aν,γ,II = 0
∀γ ∈[r] \ {1}
1. In this case I and Ic are the children of the root node [N], and the maximal rank of B[N],γ is 1 for every γ ∈[r].
30


## Page 31


BOOSTING DILATED CONVOLUTIONAL NETWORKS WITH MIXED TENSOR DECOMPOSITIONS
Plugging this into the decomposition in eq. 12, one readily sees that:
• For every ν ∈Θ(I), {Bν,γ}γ∈[r] are indicator column vectors (one entry holds 1, the rest
hold 0) such that Bν,γ̸=Bν,γ′ if γ ̸= γ′. The same holds for ν ∈Θ(Ic), but with the vectors
being rows.
• If ν has one child in Θ(I) and the other in Θ(Ic), {Bν,γ}γ∈[r] are indicator matrices, where
both the row and column indexes of the active entry do not repeat as γ varies.
• The matrices {B[N],γ}γ∈[r] corresponding to the root node [N] are equal to one another, given
by a joint Kronecker product between all of the following:
– Bν,1 for every node ν in either Θ(I) or Θ(Ic) which does not have a sibling in the other
– Pr
α=1 Bν,α for every node ν that has one child in Θ(I) and the other in Θ(Ic)
According to the ﬁrst observation above, Bν,1 has rank 1 for every ν in Θ(I) or Θ(Ic). The second
observation implies that Pr
α=1 Bν,α has rank r for every node ν that has one child in Θ(I) and
the other in Θ(Ic). In turn, and while taking into account the rank-multiplicative property of the
Kronecker product (rank(A⊙A′) = rank(A)·rank(A′) – see Bellman (1970) for proof), the third
observation implies:
rank(B[N],γ) = r|{(ν1,ν2)∈Θ(I)×Θ(Ic): ν1 and ν2 are siblings in T}|
∀γ ∈[r]
We thus have found weights {aν,γ,I, aν,γ,II}ν,γ for which eq. 13 holds.2 This establishes the sought
after lower bound on matricization ranks (eq. 11), completing the proof of the theorem.
■
Appendix C. Maximality of Matricization Ranks
In the proof of theorem 7 (app. B.2), and in the derivation of corollary 8 (sec. 6), we made use of the
fact that a tree or mixed decomposition (eq. 3 or 4 respectively), with a product operator g(·), admits
maximal matricization ranks almost always. That is to say, for any index set I ⊂[N], the ranks of
generated grid tensors {Ay}y when matricized w.r.t. I, attain their maximum possible values (which
depend on both the decomposition and I) for all conﬁgurations of weights ({aν,γ,I, aν,γ,II}ν,γ for
the tree decomposition, {aν,γ,I, aν,γ,II}ν,γ and {¯a¯ν,γ,I, ¯a¯ν,γ,II}¯ν,γ for the mixed decomposition) but
a set of Lebesgue measure zero. Hereinafter we justify this assertion.
When equipped with the product operator (g(a, b) = a·b), a tree or mixed decomposition gen-
erates grid tensors {Ay}y whose entries are polynomials in the decomposition weights. Therefore,
for any index set I ⊂[N], the entries of the matricizations {JAyKI}y are, too, polynomials in the
decomposition weights. Claim 9 below implies that for a particular index y, the rank of JAyKI is
maximal almost always, i.e. for all weight settings but a set of measure zero. Since the union of
ﬁnitely many zero measure sets is itself a zero measure set (see Jones (2001) for example), we con-
clude that the ranks of {JAyKI}y are jointly maximal almost always, which is what we set out to
prove.
2. This applies to all but the trivial case where I is such that there exist siblings ν1 ∈Θ(I) and ν2 ∈Θ(Ic) of depth 1
(I and Ic are the children of the root node [N]). In the latter case the lower bound in eq. 13 can be met trivially.
31


## Page 32


COHEN TAMARI SHASHUA
Claim 9
Let D, M1, M2 ∈N, and consider a polynomial function mapping weights α ∈RD to
matrices A(α) ∈RM1×M2 (“polynomial” here means that all entries of A(α) are polynomials
in α). Denote R = maxα∈RD rank(A(α)), and consider the set S := {α ∈RD : rank(A(α)) <
R}. This set has Lebesgue measure zero.
Proof We disregard the trivial case where R = 0. Let α0 be a point at which R is attained
(rank(A(α0)) = R), and assume without loss of generality that the top-left R×R minor of A(α0),
i.e. the determinant of A(α0)1:R,1:R, is non-zero. The function p : RD →R deﬁned by p(α) =
det(A(α)1:R,1:R) is a polynomial, which by construction does not vanish everywhere (p(α0) ̸= 0).
The zero set of a polynomial is either the entire space, or a set of Lebesgue measure zero (see Caron
and Traynor (2005) for proof). Therefore, the zero set of p(·) has Lebesgue measure zero. Now, for
every α∈S:
rank(A(α)) < R =⇒rank(A(α)1:R,1:R) < R =⇒p(α) := det(A(α)1:R,1:R) = 0
S is thus contained in the zero set of p(·), and therefore too, has Lebesgue measure zero.
32

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
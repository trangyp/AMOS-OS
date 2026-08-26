---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1902.01107v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1902.01107v1_TCM-NOMA__Joint_Multi-user_Codeword_Design_and_Detection_in_Trellis_Coded_Modula

> Source: 1902.01107v1_TCM-NOMA__Joint_Multi-user_Codeword_Design_and_Detection_in_Trellis_Coded_Modula.pdf

> Pages: 13

---


## Page 1


arXiv:1902.01107v1  [cs.IT]  4 Feb 2019
1
TCM-NOMA: Joint Multi-user Codeword Design
and Detection in Trellis Coded Modulation based
NOMA for Beyond 5G
Boya Di∗, Student Member, IEEE, Lingyang Song∗, Fellow, IEEE, Yonghui Li†, Fellow, IEEE, Geoffrey Ye Li‡, Fellow, IEEE
Abstract—In this paper, we propose a novel non-orthogonal
multiple access (NOMA) scheme based on trellis-coded mod-
ulation (TCM). Different from those in the traditional code-
domain NOMA, the incoming data streams of multiple users
are jointly coded and mapped to the codewords so as to improve
the coding gain of the system without any bandwidth extension.
Both codeword design and multi-user detection are considered
to optimize the TCM for NOMA. The multi-dimensional (MD)
constellation is carefully selected and a new set partitioning
algorithm is developed for MD signal set labeling. To achieve
the trade-off between the BER performance and complexity,
a suboptimal two-layer Viterbi algorithm is proposed for joint
decoding. Simulation results show that our proposed TCM-based
NOMA scheme performs signiﬁcantly better than the traditional
code-domain NOMA and OFDMA schemes in terms of the BER
performance under the same channel conditions.
Index Terms—Non-orthogonal multiple access, trellis coded
modulation, codeword design, multi-user detection.
I. INTRODUCTION
The past few years have witnessed the explosive growth
of demand for massive data transmission brought by the
increasing number of mobile devices and applications [2].
The traditional orthogonal frequency division multiple access
(OFDMA) techniques in the fourth-generation (4G) networks
fail to achieve the adequate exertion of the frequency resources
due to its orthogonal nature [3], [4]. This also causes access
congestion especially in a dense network, urging for more
efﬁcient solutions. Capable of supporting massive connectivity
and improving the spectral efﬁciency [5], non-orthogonal
multiple access (NOMA) has drawn widespread attention as
a promising candidate to solve the above issues in future
communications [6], [7].
In NOMA systems [8], [9], multiple users are allowed
to share the same resources, such as a subchannel, a time
slot and so on. One of the efﬁcient schemes is the code-
domain NOMA [10], [12]. Speciﬁcally, the incoming data of
each layer are mapped to a sparse codeword in which the
non-zero elements correspond to the occupying subcarriers of
each layer. After superimposing the codewords of multiple
layers, the transmitter sends multiple data streams to the
The
Part of this paper was presented in the International Conference on
Communications (ICC) [1], 2018.
B. Di and L. Song are with the School of Electrical Engineering and
Computer Science, Peking University, China. Y. Li is with the School of
Electrical and Information Engineering, The University of Sydney, Australia.
G.Y. Li is with School of Electrical and Computer Engineering, Georgia
Institute of Technology, USA.
receiver simultaneously over a limited number of subcarriers,
achieving the overloading function [13]. Each layer is assigned
a pre-deﬁned codebook where the mapping between non-
zero elements and the data streams is constructed based on
multi-dimensional (MD) modulation techniques [11], [12].
To decode the superimposed codeword, the belief probability
based massage passing algorithm (MPA) [14] has been applied
at the receiver.
For the code-domain NOMA, previous works [15]–[18]
have discussed various schemes to improve the coding gain.
In [15], a constellation optimization method has been devel-
oped in which the structure of the MD complex constellation
has been optimized based on the star-QAM constellation.
In [16], the Turbo TCM technique has been utilized to generate
the multi-dimensional codebooks for each user separately,
and the pure MPA has been adopted for decoding. In [17],
a new constellation has been proposed and analyzed based
on a novel performance criterion. In [18], a low-complexity
detector has been designed for an uplink NOMA system
based on the adaptive Gaussian approximation. Most existing
works [15]–[18] focus on either optimizing the procedures of
MD constellation construction or improving the performance
of MPA under the framework in [12]. However, the practical
utilization of NOMA systems can be further improved if joint
multi-user codeword design can be achieved.
In this paper, we jointly design codewords for multiple users
simultaneously via MD trellis-coded modulation (TCM) tech-
niques. The data streams of different users are jointly coded
and mapped directly to the sparse codewords. Traditionally,
TCM techniques [19] have been well investigated as a suitable
approach to jointly optimize the error control coding and mod-
ulation through the signal set expansion instead of bandwidth
expansion. Differently, we consider the MD-TCM technique
purely as a method to design codewords for NOMA users,
instead of replacing the channel coding. New challenges have
been posed on both the codeword design and the multi-user
detection. On one hand, due to the multiplexing nature, the
mapping from the MD constellation point to the superimposed
codeword is different from that in the traditional MD-TCM
scheme. Therefore, a new method for selecting and labeling
the MD constellation should be considered. On the other hand,
due to the entanglement of encoding and multiplexing, the
traditional MPA or Viterbi algorithm cannot be directly applied
to decode the TCM-based NOMA signals, requiring a new
decoding scheme.
To tackle the above challenges, we design new encoding


## Page 2


2
and decoding schemes for joint codeword design in an over-
loaded NOMA system to improve the coding gain. Over each
subcarrier, the data streams of multiple users are rearranged
into one data sequence, which is then coded and mapped to an
MD constellation point. Our main contributions in this paper
can be summarized as below:
• To construct the TCM encoder, a novel bipartite set
partitioning algorithm based on farthest-point optimiza-
tion (FPO) [20] is proposed and analyzed such that the
minimum free squared Euclidean (MFSE) distance of the
system can be maximized.
• A maximum likelihood sequence detection (MLSD) is
developed. To balance the complexity and the BER
performance, we also propose a suboptimal two-layer
joint decoding scheme based on the Viterbi algorithm.
The non-orthogonal nature of NOMA is utilized in this
scheme and the decoding complexity is analyzed.
• Simulation results show that the proposed scheme signif-
icantly outperforms the traditional code-domain NOMA
and OFDMA in terms of the BER performance. The
inﬂuence of system parameters on the BER performance
and decoding complexity is also investigated.
The rest of this paper is organized as follows. In Section
II, we introduce the framework of TCM-based NOMA. In
Section III, we discuss the TCM-based NOMA encoder design
criteria and detailed steps. Based on the criteria, an FPO-based
bipartite set partitioning algorithm is proposed and analyzed.
In Section IV, we provide an optimal MLSD decoding scheme.
To balance the complexity and BER performance, we also
develop a suboptimal two-layer soft-decision based Viterbi
algorithm. Simulation results are presented in Section V, and
ﬁnally, we conclude the paper in Section VI.
II. SYSTEM MODEL
In this section, we ﬁrst introduce downlink code-domain
NOMA and then present the key idea of TCM-based joint
NOMA codeword design.
A. Code-Domain NOMA Multiplexing
The general structure of a code-domain NOMA system is
shown in Fig. 1. In the ﬁgure, the BS sends J data streams,
each to a NOMA user. The available bandwidth is divided into
K orthogonal subcarriers. Different from orthogonal access,
multiple users can share the same subcarrier simultaneously.
At the transmitter, the data stream1 of each user j in time
unit t, denoted by bj [t] =
 b1
j [t] , · · · , bq
j [t]

, is transmitted
over N (N ≪K) subcarriers. Data stream bj [t] is mapped
to a sparse codeword xj [t] =

x(1)
j
[t] , · · · , x(K)
j
[t]

of length
K, in which N nonzero elements of this codeword represent
the set of intended signal points and (K −N) zero elements
correspond to the unoccupied subcarriers of user j. All J
NOMA users are multiplexed over K shared subcarriers.
1In Fig. 1, we omit the subscript t due to the limited space.
Therefore, the received signal over subcarrier k can be ex-
pressed as
y(k) [t] = h(k) [t]
J
X
j=1
x(k)
j
[t] + n(k) [t],
(1)
where the channel coefﬁcient of subcarrier k in time unit
t is denoted by h(k) [t] and the additive white Gaussian
noise (AWGN) is denoted as n(k) [t] ∼CN
 0, σ2
, with σ2
as the noise variance.
B. Mapping Matrix Design
The occupied subcarrier set of each user is ﬁxed, that is,
for each user the positions of non-zero elements in the sparse
codeword with respect to any data streams are the same. We
can use a binary K × J matrix F to depict such mapping
relation where each variable fk,j in F indicates whether user
j occupies subcarrier k, i.e., whether x(k)
j
[t] is a non-zero
element.
Since each codeword contains N non-zero elements out of
K, there are CN
K possible mappings between the subcarriers
and each user. Note that different users occupy different
subset of subcarriers. Therefore, at most J = CN
K users can
be supported simultaneously. Denote df as the number of
users sharing the same subcarrier in this case. We then have
df = CN−1
K−1.
For the NOMA system in Fig. 1 where J = 6, K = 4, N =
2, and df = 3, a widely used mapping matrix is presented as
below:
F =


1
1
0
0
0
1
1
0
0
1
1
0
0
1
1
1
0
0
0
0
1
0
1
1


(2)
In Fig. 1, we use a square marked by 1 to represent an occupied
subcarrier by each user, otherwise a blank square marked by 0.
With the mapping matrix F, we can then denote the set of users
occupying subcarrier k as J (k) = {j|1 ≤j ≤J, fk,j = 1}.
For example, for the mapping matrix in (2), we have J (1) =
{1, 2, 6}.
C. TCM-based Joint NOMA Codeword Design
In the traditional NOMA scheme [10], the codeword of
each user, xj [t], is only related to its data stream bj [t]. Each
user independently selects a codeword from a pre-deﬁned
codebook. Though such a design provides a straightforward
decoding method, it greatly limits the potential coding gain
due to the independent coding of each user. In addition,
channel coding needs to be performed ahead of the MD
modulation in the existing scheme. Therefore, extra bandwidth
expansion is required when both the channel coding and
modulation are considered, leading to inefﬁcient utilization of
frequency resources.
To tackle the above two issues, we jointly determine the
non-zero elements of all the users over each subcarrier based
on their data streams. We consider a joint coding and modula-
tion scheme MD-TCM in which the binary convolutional code
and M-ary constellation are combined to obtain the coding


## Page 3


3
User 1
User 2
User 6
Mapping
Mapping
Mapping
K
1
1
0
0
K
1
1
0
0
1
1
0
0
Ă
K
df =3 bit 
streams
MD-TCM
Encoder 1
Ă
MD-TCM
Encoder K
Ă
K encoders
df complex points
Ă
superposition
superposition
superimposed 
codeword
K
Inner layer 
detection
Output
Ă
Outer layer 
Viterbi for 
joint 
decoding
df = 3 bit 
streams
Parallel to 
serial
df complex 
points
Parallel to 
serial
Joint MLSD
Positions of 
occupied 
subcarriers
Inner layer 
detection
Base Station
Receiver of each user
Data 
Sequence
1st element of the 
superimposed 
codeword
K-th element of 
the superimposed 
codeword
Fig. 1.
The general structure of a code-domain NOMA system with joint coded modulation in which J = 6, K = 4, N = 2, df = 3, and the mapping
matrix is shown in equation (2).
gain through the signal set expansion instead of the bandwidth
expansion. The key idea can be illustrated as below.
1) TCM-based NOMA Encoding: Given the set of users
occupying subcarrier k, J (k), the data sequence transmitting
over subcarrier k consists of data streams from df users in time
unit t, which can be denoted as b(k) [t] =

bj [t]|j ∈J (k)	
.
As mentioned above, according to the ﬁrst row of the mapping
matrix F in equation (2), we have J (1) = {1, 2, 6}. Therefore,
the data streams for user 1, 2, and 6 in the current time slot
t in Fig. 1, i.e., b1 [t] = 01, b2 [t] = 10, and b6 [t] = 11,
respectively, are transmitted over subcarrier 1. Thus, we have
b(1) [t] = 011011.
In each time unit t, a data sequence b(k) [t] is encoded
into a sequence c(k) [t] and then mapped to an MD constel-
lation point via the MD-TCM technique such that the event-
error probability can be minimized. Each component of the
MD constellation point represents a non-zero element of the
sparse codewords over subcarrier k, i.e., x(k)
j , j ∈J (k). In
Fig. 1, after passing the MD-TCM encoder, the data sequence
b(1) [t] = (011011) is ﬁrst encoded as c(1) [t] = (1011011)
and then projected onto a 6D constellation point consisting
of three 2D components, i.e., x(1)
1
[t], x(1)
2
[t], and x(1)
6
[t] in
Fig. 1.
The k-th element of the superimposed codeword in time
unit t can be obtained by adding these 2D components
P
j∈J (k) x(k)
j
[t], carrying the information of all users in
J (k). The superimposed codeword is then determined after
all K elements are obtained through the above process. In
Fig. 1, the ﬁrst element of the superimposed codeword is

x(1)
1
[t] + x(1)
2
[t] + x(1)
6
[t]

. Other elements in the superim-
posed codeword can be similarly obtained, represented by the
dark squares in a vertical column.
2) TCM-based NOMA Decoding: At the receiver of each
user, we jointly decode the data streams of all users by
utilizing the soft-decision Viterbi based MLSD. Depending
on the mapping matrix F, the same data stream of each user
transmits over different subcarriers, which can be utilized for
joint decoding and is different from the traditional Viterbi
algorithm.
In each step of the sequence detection, we ﬁrst estimate the
transmitted signal points by utilizing the above non-orthogonal
nature. We then update the survivor paths based on the soft-
decision Viterbi algorithm. The data streams of each user can
be recovered based on the survivor paths.
III. TCM-BASED NOMA ENCODER DESIGN
In this section, we ﬁrst discuss the criteria for TCM-based
NOMA encoder design. and then illustrate three phases of the
encoder design in detail.
A. Encoder Design Criteria
1) Notations: We assume that the number of subcarriers
is K = 2p, and the number of bits to be coded and trans-
mitted for each user j in each time unit t is q = |bj [t] |,
1 ≤j ≤J, ∀t > 0. For example, in Fig. 1, we have
q = 2 for each user. The sequence of non-zero elements in
the sparse codewords with respect to subcarrier k is denoted
as x(k) [t] =
n
x(k)
j
[t]|j ∈J (k)o
.
As shown in Fig. 2, we utilize the conventional lattice or star
constellation to construct an MD mother constellation from
which we select the signal set. To be speciﬁc, given a M-
QAM constellation L with size M, a df×M-QAM mother
constellation Ldf can be constructed with the size of M df . In
Fig. 2, we have a 3×16QAM mother constellation L3.
Since the original constellation L is composed of 2D
signal points, the MD mother constellation consists of 2df-
D points. Each 2df-D point Al ∈Ldf is denoted by Al =
 al1, al2, · · · , aldf

with 1 ≤l ≤M df , in which ali repre-
sents a signal point from the original M-QAM constellation L.
We denote the position of a 2df-D point Al in the 2D plane2
2For convenience, we denote the position zl of the signal point Al in the
form of a complex number. The coordinates of this point in the 2D plane is
(Re (zl) , Im (zl)). In the remaining part of this paper, when we mention the
position of a 2df -D point Al, we refer to its position in the 2D plane.


## Page 4


4
Multi-D
(0,0,0) (0,0,3) Ă (0,0,15)
(0,1,0) (0,1,1) Ă (0,1,15)
Ă 
(15,15,1) (15,15,2) Ă (15,15,15)
1
0
2
3
4
5
6
7
8
9
10
11
12
13
14
15
Signal set 
selection
(1,2,4) (1,2,9) Ă (1,2,15)
(2,3,8) (2,3,10) Ă (2,3,15)
Ă 
(13,14,15) (14,15,15) Ă 
points
 points
 points
Ă 
Ă 
4 coded 
bits
 points
 points
 points
 points
Ă 
Ă 
Ă 
 points
 points
 points
 points
0
1
0
0
0
0
1
1
1
1
Ă
Ă 
Ă 
Ă 
 one point
0
1
one point
0
1
 one point
3 uncoded 
bits
Subcarrier-
based
Set partitioning
TCM-based
Set partitioning
1
2
3
4
5
J=6
10
11
0
1
Ă 
Ă 
Ă 
p
p
0
1
0
1
Ă 
Superposition
Ă 
Fig. 2.
MD-TCM based NOMA encoder diagram with J = 6, K = 4,
df = 3, M = 16, r = 3, p = 2, and q = 2.
as zl = Pdf
i=1 ali. For example, if we have three 2D points ex-
tracted from L, say, (1 + 1i), (−3 + 3i), and (−1 −1i) where
i = √−1, and then a 6D point A1 in Fig. 2 constructed from
these points is denoted by A7 = (1 + 1i, −3 + 3i, −1 −3i),
and its position in the 2D plane is z7 = (−3 + 1i).
2) Criteria: With the above deﬁnitions, the process of
coded modulation can be described as below. According to
the TCM principle, in each time unit t, r out of qdf bits from
the data sequence b(k) [t] are sent into a convolutional encoder
of rate r/ (r + 1). The rest of qdf −r uncoded bits from b(k) [t]
will determine a speciﬁc point in a subset of Ldf with the size
of 2qdf−r. In this way, the coded sequence c(k) [t] with the
length of qdf + 1 is mapped to a unique 2df-D constellation
point Al
∈Ldf . The kth element in the superimposed
codeword can be determined based on the position of a chosen
2df-D point Al, i.e., z(k) = P
j∈J (k)xj(k) [t] = Pdf
i=1 ali.
Take Fig. 2 as an example. For subcarrier 1, the data
sequence to be transmitted is b(1) [t] = 011011. Given a
signal constellation A(1) of size 128, the ﬁrst three bits of this
sequence are sent into a convolutional encoder of rate 3/4 such
that the output four coded bits, say, 1011, select a signal subset
of size 8, say, A2
6. A speciﬁc 6D point of A2
6, say, A7, is then
selected based on the remaining three uncoded bits of b(1) [t].
The value of the ﬁrst element in the superimposed codeword
is actually the position of A7. The mapping between the coded
(or uncoded) bits and the signal subset (or a 6D point) will be
illustrated in Section III.B-2.
To minimize the event-error probability [19], we aim to
jointly design the coding and modulation so that the MFSE
distance between any two coded sequences, denoted by d2
free,
can be maximized. In other words, we aim to construct an
optimal mapping from the transmitted data sequence over
each subcarrier to the corresponding non-zero elements in the
codewords, i.e., b(k) →c(k) →Al →x(k), 1 ≤k ≤K,
Al ∈Ldf . Since the mapping is not related to t, we omit it in
the remaining part of this section.
As mentioned above, not all bits of sequence b(k) participate
in the convolution computation, and thus, there exist parallel
branches between two states of the convolutional encoder,
brought by the uncoded bits. According to the TCM principle,
d2
free is determined by two terms: 1) the minimum squared
Euclidean (MSE) distance δ2
free between different trellis paths
longer than one branch; 2) the MSE distance δ2
min between
the parallel branches of the encoder. Therefore, we have
d2
free = min
n
δ2
free, δ2
min
o
. In Subsections III.B and III.C,
we illustrate how to calculate δ2
min and δ2
free, respectively, as
well as the relationship between them.
B. Joint Encoding
Three phases are illustrated as below, i.e., 1) signal set
selection; 2) signal set labeling; 3) convolutional encoder
construction.
1) Signal Set Selection: A signal set is selected from the
MD mother constellation so as to satisfy the following two
constraints on a) the size of the set; b) the uniqueness of
each point’s position in the set. For successful decoding, each
coded data sequence c(k) of length (qdf +1) is required to be
mapped to a unique position. For generality, we also assume
that any two coded data sequences c(k) and c(k′) transmitted
over different subcarriers k and k′ are mapped to two different
positions3. Since there are K subcarriers, 2p+qdf+1 unique
positions in total are required for the selected signal set.
Therefore, we aim to construct a signal set A0 of size
2p+qdf+1 from the MD mother constellation Ldf such that
the positions of any two points projecting in the 2D plane are
different, which can be mathematically formulated as:
ﬁnd A0
(3a)
s.t. zl ̸= zl′, ∀Al, Al′ ∈A0, l ̸= l′,
(3b)
|A0| = 2p+qdf+1,
(3c)
A0 ⊆Ldf .
(3d)
This problem can be solved by the following two steps.
a) Obtaining a unique constellation: Note that in the
MD mother constellation Ldf , there may exist more than
one 2df-D constellation points sharing the same position in
the 2D plane. Denote the set of points sharing the same
positions as As. To keep the uniqueness of each signal point,
we can only select one point Al∗∈As as a member of
A0 while all the other points are removed. To improve the
diversity among df non-zero elements of the sparse codewords
transmitting over the same subcarrier, we select the MD point
with the largest variance among its 2D components, i.e.,
l∗= arg max
Al∈As var (Al). Note that the size of A0 is required
to be no smaller than 2p+qdf+1; otherwise, the MD mother
constellation Ldf is required to be reconstructed.
b) Shaping: After step a), we denote the current constel-
lation as Ac. If the size of Ac is larger than 2p+qdf+1, we
continue to remove points until constraint (3c) is satisﬁed. For
a constellation, its average energy is required to be minimized
while the MFSE distance between points can be as large as
3In the simulation, we will show both cases where different signal sets or
identical signal sets are allocated to different subcarriers.


## Page 5


5
possible. Therefore, we tend to remove those points close to
their neighbors but far away from the original point. A greedy
algorithm is adopted for shaping based on the above criterion.
We sort the constellation points in Ac as Aπ(1), Aπ(2), · · ·
such that
min
Ar∈Ac,r̸=π(j)

zπ(j) −zr

zπ(j)
2
≤
min
Ar∈Ac,r̸=π(j′)

zπ(j′) −zr

zπ(j′)
2
,
(4)
holds ∀j ≤j′, where the numerator in the fraction is the
MFSE distance between point Aπ(j) and other points in Ac,
and the denominator represents the energy of point Aπ(j). We
remove the points one by one in Ac starting from Aπ(1) until
the size of the remained signal set is 2p+qdf+1, i.e., the target
set A0 is obtained.
2) Signal Set Labeling: Signal set labeling refers to the
process in which each coded sequence c(k), 1 ≤k ≤K is
assigned a unique signal point in A0 such that the MFSE
distance can be maximized. As shown in Fig. 2, two steps of
signal set labeling for NOMA are listed as below:
• Subcarrier-based
Set
Partitioning:
As
mentioned
above, any two coded sequences c(k) and c(k′) are
assigned to different signal points in A0. Therefore, we
divide A0 into K subsets with the equal size, i.e., A0 →

A(1), A(2), · · · , A(K)	
. Each subset A(k) corresponds
to all possible signal points transmitting over subcarrier
k, satisfying
A(k) = 2qdf +1.
• TCM-based Set Partitioning: For each subcarrier k,
a signal point in Ak is assigned to a coded sequence
c(k) such that the MFSE distance can be maximized. To
construct the mapping based on the above criterion, we
adopt the set partitioning technique in which a binary
partitioning tree is utilized [19]. In each level of the tree,
the current signal set is divided into two subsets such
that the minimum squared subset distance (MSSD), that
is, the MSE distance between signal points in the same
subset, is maximized. In the last level of the tree, the leaf
node refers to a constellation point. Each constellation
point can be reached via a unique path through the tree.
Overall Set Partitioning Process: To further maximize
the MFSE distance of the coding scheme with respect to
each subcarrier, we consider adopting the binary-tree based
set partitioning technique in the ﬁrst step as well. This is
to say, given A0, we aim to maximize the MSSD of each
subset A(k). For the system shown in Fig. 1 and Fig. 2,
the signal set labeling can be described as below. We ﬁrst
construct a super binary partitioning tree of 29 levels with
the root node A0. The ﬁrst level of the tree consists of two
subsets divided from A0, denoted by A1
1 and A2
1. For level
2 ≤j ≤29 of the tree, each branch node Ai
j represents a
point set which will be divided into two subsets in the next
level, i.e., A2i−1
j+1
and A2i
j+1. The signal sets obtained after
the subcarrier-based set partitioning can be found in level 2
of the tree, i.e., {A(1), · · · , A(4)} =

A1
2, · · · , A4
2
	
. In the
last level of the tree, we have Al
9 = {Al} , Al ∈A0, i.e.,
each leaf node represents a speciﬁc signal point. The coded
sequence mapped to this point is labeled by the path towards
this leaf node. For example, we have A1
9 = {A1} implying
that the coded sequence 0000000 transmitted over subcarrier
1 is mapped to the signal point A1 ∈A(1).
Based on the binary subtree for each subcarrier k, A(k), we
observe that δ2
min can be obtained by inspecting the minimum
MSSD of the subsets in the (r + 1)th level of the subtree, i.e.,
the (p + r + 1)th level of the binary tree in Fig. 2.
δ2
min =
min
1≤i≤2r+1
n
∆

A(k−1)·2r+1+i
p+r+1
o
.
(5)
Basic Bipartite Set Partitioning Operation: Note that the
basic operation in the above process is to divide a signal set
into two subsets with the equal size. We now formulate this
basic bipartite set partitioning problem and propose a novel
algorithm to solve it.
a) Problem Formulation: Given a signal set Ab, we aim
to divide it into two subsets A1
b and A2
b with equal size such
that the MSSD is maximized. The MSSD of each subset Aj
b
is given by
∆

Aj
b

=
min
l,l′∈Aj
b,l̸=l′ ∥zl −zl′∥2
2 , j = 1, 2.
(6)
Therefore, an optimal bipartite set partitioning of Ab, i.e.,
Ab →{A1
b, A2
b}, can be obtained by solving the following
problem:
max
{A1
b,A2
b}

min
1≤j≤2 ∆

Aj
b

(7a)
s.t.
Aj
b
 = 1
2 |Ab| , j = 1, 2,
(7b)
Aj
b ⊂Ab, j = 1, 2,
(7c)
∆

Aj
b

> 0, j = 1, 2.
(7d)
This is a non-trivial problem due to its combinatorial nature
and the irregular positions of the points. The traditional multi-
level coding technique [24] which is originally designed for
partitioning lattice or star constellations does not ﬁt this
case any more. We then propose a modiﬁed farthest point
optimization algorithm to address this problem, as illustrated
below.
b) Algorithm Design: We observe that the distribution
of the points in our formulated problem has the blue noise
properties, i.e., i) the signal points cover a certain area and
there are no “holes” or “clusters” in the 2D plane; ii) the
points in the selected set are distributed almost irregularly.
Such properties have drawn great attention in the researches
on point set generation [21] where a farthest point optimization
(FPO) strategy [20] has been utilized for generating point
distributions with high-quality “blue noise” characteristics, i.e.,
large point spacing in a given area.
Instead of point generation, we aim to select points for each
subset given the point distribution. By extending the FPO
strategy, we then propose a novel bipartite set partitioning
(FPO-BSP) algorithm to solve problem (7), consisting of two
phases: i) initial subset construction; ii) FPO iteration. Details
of the algorithm are shown in Algorithm 1 and are illustrated
as below.


## Page 6


6
For convenience, we ﬁrst present three different distance
metrics. Given a signal point Al, its minimum distance to a
set Ax is deﬁned as
dl (Ax) =
min
Ar∈Ax,r̸=l |zl −zr| .
(8)
Based on this deﬁnition, the MSSD of a set Ax in (6) can be
rewritten by
∆(Ax) = min
Al∈Ax dl (Ax) .
(9)
The average minimum distance of a set Ax, denoted by ¯d (Ax),
can be obtained based on each point’s minimum distance, i.e.,
¯d (Ax) =
1
|Ax|
X
Al∈Ax
dl (Ax).
(10)
Since we tend to divide the target signal set into two subsets
where the points are spread out as far as possible, both the
MSSD and the average minimum distance of the subsets are
encouraged to be maximized.
i) Initial Subset Construction: As shown in Phase 1 of
Algorithm 1, we adopt a greedy method to divide the target
set into two initial subsets. For the target set Ab of size |Ab|,
there are L = C2
|Ab| pairs of points in total. We sort these pairs
in the increasing order of the distance between two points (line
2 in Algorithm 1). The list Γ can be mathematically presented
as
Γ =
 Aα(1), Aβ(1)

,
 Aα(2), Aβ(2)

, · · · ,
 Aα(L), Aβ(L)
	
,
(11)
satisfying that
zα(j) −zβ(j)
 ≤
zα(j′) −zβ(j′)
 , 1 ≤j ≤j′ ≤L.
(12)
As shown in line 3 of Algorithm 1, we initialize two
subsets as A1
b =

Aα(1)
	
and A2
b =

Aβ(1)
	
. The remaining
pairs of points in list Γ are then traversed to be added into
different subsets (line 5-21). To be speciﬁc, we consider a pair
 Aα(j), Aβ(j)

. If both points never show up in the current
subsets, we then add Aα(j) and Aβ(j) separately into A˜α
b and
A
˜β
b in which ˜α, ˜β ∈Z+ such that the minimum distance
between the members of this pair and the subsets can be
maximized (line 15-17), i.e.,
min
n
dα(j)
 A˜α
b

, dβ(j)

A
˜β
b
o
≥min
n
dα(j)

A
˜β
b

,
dβ(j)
 A˜α
b
	
, ˜α + ˜β = 3.
(13)
However, when the distance between Aα(j) and Aβ(j) is larger
than the MSSD of current subsets, i.e.,
zα(j) −zβ(j)
 >
max

∆
 A1
b

, ∆
 A2
b
	
, then it is not necessary that Aα(j)
and Aβ(j) are divided into two subsets. Each of them selects a
subset with a large minimum distance to join (line 11-13). If
one of the points in the target pair has already been added in a
subset in previous operations, then the other point is naturally
added to another subset (line 19-21). The whole process ends
when the size of one subset reaches |Ab| /2. The left unchosen
points in list Γ are then added to the other set which has not
been fully ﬁlled (line 6-9).
ii) FPO Iteration: Based on the above initialized subsets,
we then perform the FPO iteration as shown in Phase 2 of
Algorithm 1. The key idea of the FPO method is illustrated
as below. Given two initial subsets A1
b and A2
b, we consider
replacing each point in subset A1
b with the farthest position
for this subset, which is selected from the other subset A2
b.
The farthest position4 for A1
b, deﬁned as Ar∗∈A2
b, can be
obtained by searching A2
b,
r∗= arg max
r∈A2
b
dr
 A1
b

.
(14)
For each point Al ∈A1
b, it is ﬁrst removed from A1
b and
inserted into A2
b (line 28). We then search for the farthest po-
sition for A1
b\ {Al} from the set A2
b ∪{Al} based on equation
(14) (line 29-34). When all points in A1
b are traversed once,
one FPO iteration is ﬁnished (line 25-35). During multiple
FPO iterations, both the MSSD and the average minimum
distance of the subsets will be increasing until convergence,
which will be proved in detail in Proposition 1.
Delaunay Triangulation for FPO: Note that in the FPO
method, a large amount of operations such as point searching,
removing, and inserting are required. To achieve a low compu-
tational complexity, we introduce the Delaunay triangulation
(DT) method to construct a dynamic graph in which the
relative positions of points can be better depicted and easily
traced.
Deﬁnition 1: Given a point set Ax, a DT refers to a
triangulation D such that no point in Ax lies inside the
circumcircle of any triangle in D. Any edge in a DT is called
a Delaunay edge.
In a DT, each triangle follows the property of empty cir-
cumcircle. One commonly used method for constructing such
a triangulation is the on-line DT method [22]. Starting from
a certain point in the set, the neighboring points are inserted
one by one to form the triangles while the property of empty
circumcircle is guaranteed. Given a formulated triangulation
D, point inserting and removing can be completed ﬂexibly via
the local optimization procedure in which Delaunay edges are
added or removed within a localized area.
Remark 1: In Algorithm 1, we refer to the above operations
as DT-INSERT (D, Al) and DT-REMOVE (D, Al), implying
the point Al inserting into D and removing from D, respec-
tively.
Remark 2: In each FPO iteration, suppose that the DT
constructed from the set Ax is D. The minimum distance
between a point Al and Ax can be obtained by searching the
Delaunay neighbors5 of Al in D instead of searching all points
in Ax. We refer to this operation as DT-SEARCH (D, Al).
Algorithm Interpretation of Phase 2: Algorithm 1 with
respect to DT can be re-interpreted in detail as below. Follow-
ing the on-line DT method, the triangulations of two initial
point subsets A1
b and A2
b are constructed, denoted by D1 and
D2. As shown in Phase 1, points are added into two subsets
in sequence (line 4, 14, 18, 22). In each FPO iteration, for
each vertex Al ∈D1, the minimum distance between Al and
4Different from the researches on point distribution generating [20], we
cannot generate new points in the given set, and thus, we redeﬁne the farthest
position as the farthest position in the existing points of the set.
5The Delaunay neighbors of Al refer to those points in D sharing the same
edges with Al.


## Page 7


7
A1
b, i.e., dl
 A1
b

, can be obtained by searching the Delaunay
neighbors of Al in D1 (line 26). After recording the current
minimum distance dmax = dl
 A1
b

, vertex Al is removed
from D1 and inserted into D2 (line 27-29). We then traverse
the vertices in the newly constructed D2 to search for the
farthest position of D1 (line 30-36). If the MSSD of A2
b will
not decrease and dr∗ A1
b\ {Al}

will not be smaller than the
MSSD of A1
b, Al is then replaced by the farthest position of
D1 (line 35-37). The sizes of two subsets maintain to be equal
since we just swap a new point in D2 with an old one in D1.
The FPO iterations will not stop until no changes can be made
to D1 and D2 (line 38).
c) Analysis of the Proposed Algorithm: The convergence
and complexity of the FPO-BSP algorithm are analyzed as
below. The proof of Proposition 1 can be found in Appendix
A.
Proposition 1: In each FPO iteration of Algorithm 1,
the average minimum distance and MSSD of subset A1
b are
increasing, and the MSSD of subset A2
b are non-decreasing.
Therefore, Phase 2 is guaranteed to converge.
Remark 3: Since the MSSD of two initial subsets of Phase
1 are usually different, we set the subset with a smaller MSSD
as A1
b and the other one as A2
b, and then send them to Phase
2. Based on Proposition 1, the MSSD of A1
b and A2
b will be
more balanced after the iterations.
As discussed in Appendix B, the complexity of Phase 1 is
O

|Ab|2 log |Ab|

and the complexity of each FPO iteration
in Phase 2 is O (|Ab| log |Ab|).
3) Convolutional Encoder Design: As mentioned in Sub-
section II.A.2, a convolutional encoder is adopted in the TCM-
based NOMA scheme to generate (r + 1) coded bits. We now
illustrate how to design the rate r/(r + 1) and the structure of
the convolutional encoder.
As shown in equation (5) and Fig. 2, rate r/(r + 1)
determines the level of set partitioning p + r + 1 in a way
that the value of δ2
min increases with r. Since the decoding
complexity also grows with r, a trade-off should be reached
between δ2
min and the complexity.
For the different rate r/(r + 1) with 1 ≤r ≤qdf −2, the
optimal convolutional encoder that maximizes δ2
free is differ-
ent. For simplicity, we assume that the same convolutional
encoder of rate r/(r + 1) is designed for different subcarriers.
The diagram of a systematic feedback convolutional encoder
(Fig. 18-16 in [19]) is adopted. Note that in the traditional
MD-TCM scheme, the distance between any two nodes Al
and Al′ is
df
P
i=1
|zli −zl′i|. This can be considered as an upper
bound of the distance between these two nodes in our proposed
TCM-based NOMA scheme since we have
df
X
i=1
|zli −zl′i| ≥

df
X
i=1
(zli −zl′i)

.
(15)
Therefore, we adopt the structure of the convolutional encoder
for df× M-PSK/QAM in the MD-TCM scheme [19]. For
a given rate r/(r + 1), the value of δ2
free increases with
the number of register states, V , in the encoder. However,
a large value of V increases the decoding complexity as well,
Algorithm 1 FPO-based bipartite set partitioning (FPO-BSP)
algorithm
Input: a point set Ab of size N
Output: two subsets A1
b and A2
b of size N/2 with maximized
MSSD
1: Phase 1: Initial Subset Construction
2: Construct a list L based on equations (11) and (12).
3: Set A1
b =

Aα(1)
	
and A2
b =

Aβ(1)
	
.
4: Initialize D1 =

Aα(1)
	
and D2 =

Aβ(1)
	
.
5: for j = 2 to L do
6:
if
A1
b
 = N/2 or
A2
b
 = N/2 then
7:
Add remained points to the subset not fully ﬁlled.
8:
break;
9:
else if

Aα(j), Aβ(j)
	
̸⊂A1
b ∪A2
b then
10:
if
pα(j) −pβ(j)
 > max

∆
 A1
b

, ∆
 A2
b
	
then
11:
For each point Al ∈

Aα(j), Aβ(j)
	
, set i∗=
arg max
i=1,2 dl
 Ai
b

.
12:
Al joins the subset Ai∗
b .
13:
else if Aα(j), Aβ(j) /∈A1
b ∪A2
b then
14:
Find ˜α and ˜β that satisﬁes inequality (13).
15:
Add Aα(j) and Aβ(j) into A˜α
b and A
˜β
b , respec-
tively.
16:
else
17:
Set Al as the point in

Aα(j), Aβ(j)
	
which is
not a member of A1
b ∪A2
b.
18:
Add Al to the subset of which the other point
is not a member, say, A2
b.
19: Construct two DTs D1 and D2.
20: Phase 2: FPO Iteration
21: repeat
22:
for each vertex Al in D1 do
23:
Obtain dl
 A1
b

by DT-SEARCH (D1, Al) in Re-
mark 2
24:
Set (Ar∗, dmax) =
 Al, dl
 A1
b

25:
Set ∆min = ∆
 A2
b

26:
DT-REMOVE(D1, Al) and DT-INSERT(D2, Al)
based on Remark 1
27:
for each vertex Al′ in D2 do
28:
DT-INSERT(D1, Al′)
29:
Obtain dl′  A1
b

by DT-SEARCH(D1, Al′)
30:
Obtain dl
 A2
b

by DT-SEARCH(D2, Al)
31:
DT-REMOVE(D1, Al′)
32:
if dl′  A1
b

> dmax and dl
 A2
b

≥∆min then
33:
Set (Ar∗, dmax) =
 Al′, dl′  A1
b

34:
DT-REMOVE(Ar∗, D2), DT-INSERT(Ar∗, D1).
35: until D1 and D2 do not change
36: return A1
b and A2
b
requiring a trade-off between δ2
free and V . Since the optimal
convolutional encoders have always been found by computer
search [24], we do not illustrate the detailed process in this
paper.
Note that the above method is suitable for the AWGN
channels. However, for the Rayleigh fading, the number of
parallel branches should be reduced and the encoder state


## Page 8


8
diagram should be redesigned such that a) the shorted error
event path length can be increased [25]; b) the product of
the squared branch distance with respect to that path can
be maximized [26]. Given an encoder designed for AWGN
channels, we can modify the state diagram by reducing the
parallel branches based on the above criteria.
IV. TCM-BASED NOMA DECODER DESIGN
Due to the non-orthogonal nature of the NOMA, signals of
multiple users are superimposed and transmitted over the same
subcarrier, and thus a joint decoding technique is required.
Since the convolutional encoding is adopted, an efﬁcient se-
quence detection should be considered in the decoding scheme.
In this section, we design a two-layer Viterbi-based algorithm
for the joint TCM-based NOMA decoding in which the soft-
decision based MLSD technique is utilized.
A. Criterion for Joint Decoding
We assume that η data sequences are sent into each
TCM encoder sequentially, i.e., one sequence per time
unit. Denote m as the number of time units required for
the encoder registers to be cleared. The set of coded se-
quences is
 c(k) [1] , c(k) [2] , · · · , c(k) [η + m]

. In the tradi-
tional ML detection, the decoder should produce a set of
estimated ˆc(k) of c(k) given the received sequence such that
η+m
P
t=1
log P
 y(k) [t]|c(k) [t]

can be maximized.
However, due to the multiplexing nature of NOMA, the
input data sequences of different encoders overlap with each
other, which can be utilized for joint decoding. For example,
given the mapping matrix in (2), the data streams of users 1,
2, and 3 are coded and transmitted over subcarrier 1, and that
of users 1, 4, and 5 over subcarrier 2. A successful decoding
scheme requires that the decoded data sequence of the same
user obtained from different subcarriers in the one time unit
should be the same. In other words, the data sequence of
user 1 decoded from the ﬁrst two subcarriers, i.e., b(1)
1
[t] and
b(2)
1
[t], should be identical and the same is true with other
users. Mathematically, we have
b(k)
j
[t] = b(k′)
j
[t] , if j = J (k) ∩J (k′), 1 ≤k, k′ ≤K. (16)
Based on the above idea, we consider to adopt the cross
check in the ML detection for joint NOMA decoding. Given
the encoder state of time unit (t −1) and the input data
sequence of time unit t, a TCM encoder only produce
one out of 2qdf+1 possible code sequences as the output.
To depict this, we introduce a binary probability variable
P

c|s(k) [t −1] , b(k) [t]

in which s(k) [t −1] is the encoder
state in time unit (t −1). Given s(k) [t −1] and b(k) [t], the
probability of obtaining c over subcarrier k is
P

c|s(k) [t−1], b(k) [t]

=



1,
if c is the output of
the encoder in unit t,
0,
otherwise.
(17)
By combining condition (16) and deﬁnition (17), we present
the following proposition.
Proposition
2:
Given
the
encoder
states

s(k) [t −1] |1 ≤k ≤K
	
in time unit t −1, if K code
sequences in time unit t are correctly estimated, then the
following condition is satisﬁed:
K
Y
k=1
P

ˆc(k) [t] |s(k) [t −1] , b(k) [t]

= 1, ∀1 ≤t ≤η + m,
(18)
in
which
the
kit
of
data
sequences
B [t]
=
n
b(k) [t] |1 ≤k ≤K
o
satisﬁes condition (16).
For convenience, we denote a kit of code sequences as
ˆC [t] =
n
ˆc(k) [t] |1 ≤k ≤K
o
. Since there are K encoders,
we deﬁne the super encoder state in time unit t as the
combination of encoder states of all K encoders, i.e., S[t] =

s(1) [t] , s(2) [t] , ..., s(K) [t]
	
. Proposition 2 provides a neces-
sary condition, and thus, there may exist multiple qualiﬁed
kits of code sequences in each time unit t. For any possible
super encoder state S[t −1], the set of qualiﬁed kits of coded
sequences satisfying Proposition 2 in time unit t is contained
in C [t].
The criterion for joint NOMA decoding can then be de-
scribed as below. The decoder is required to estimate ˆc(k)
given the received sequence y by optimizing the following
problem:
max
ˆC[t]
η+m
X
t=1
K
X
k=1
log P

y(k) [t] |ˆc(k) [t]

(19a)
s.t. ˆC [t] ∈C [t] ,
(19b)
in which PK
k=1 log P

y(k) [t] |ˆc(k) [t]

is called the branch
metrics.
B. Joint Decoding Scheme Design
To solve the ML detection problem in (19), we ﬁrst present
an optimal solution extended from the Viterbi algorithm [27].
To obtain a more practical solution with tolerable complexity,
we then design a suboptimal two-layer Viterbi-based decoding
algorithm.
1) Optimal Maximum Likelihood Decoding Scheme: For
each encoder, we assume that the number of registers is V , and
thus there are 2V encoder states. Since there are K encoders,
we have 2KV super encoder states in total. A super encoder
state diagram can then be constructed based on the 2KV super
encoder states. Considering the cross check requirement of the
NOMA decoder, we assume that one super encoder state can
only transfer to another if the input data sequences and output
coded sequences, i.e., B [t] and C [t], satisfy Proposition 2.
Given the super encoder state diagram, the soft-decision
based Viterbi algorithm [27] can then be performed. For each
super encoder state, we aim to update the survivor path in each
time unit. A survivor path in time unit t refers to a record
consisting of a series of super encoder states S [t′], 1 ≤t′ ≤t
and the branch between every two sequent states S [t′ −1]
and S [t′]. A branch is denoted by the estimated input data
sequences and output code sequences, i.e., B [t′] and C [t′].


## Page 9


9
Mathematically, a survivor path with respect to S [t] can be
given by
S [0]
B[1],C[1]
−−−−−→S [1] →· · · →S [t′]
B[t′+1],C[t′+1]
−−−−−−−−−−→
S [t′ + 1] →· · · →S [t] .
(20)
To update the survivor path for each S [t], we utilize the
branch metrics in (19a) to select a state S [t −1] as well
as the branch bridging S [t −1] and S [t]. Speciﬁcally, the
branch metrics in each time unit t can be depicted by the
total Euclidean distances between K received signals and
the signal points mapped to the candidate code sequences,
i.e.,
K
P
k=1
d
 y(k) [t] , g
 c(k) [t]

, in which g (·) maps a coded
sequence to the output signal point in the constellation.
In the last time unit η + m, we select the shortest survivor
path terminated with an all-zero super encoder state as the ﬁnal
path. The optimality of this cross-check based soft-decision
Viterbi algorithm can be guaranteed since the ﬁnal survivor
path is always the ML path (Theorem 12.1 in [19]).
2) Suboptimal Two-layer Viterbi-based Joint Decoding
Scheme: In the optimal decoding algorithm, for each time unit
the decoder is required to traverse all 2KV super encoder states
and possible branches to update the survivor path for each
super encoder state, leading to a prohibitively high computa-
tion complexity. To reduce the complexity, we consider only
checking the most possible super encoder states and branches
to update no more than λ survivor paths in each time unit in
the suboptimal decoding scheme.
a) Inner Layer Soft-decision Viterbi Operation: For
convenience, we denote the set of stored super encoder states
corresponding to the survivor paths in time unit (t −1) as
S [t −1] = {S1 [t −1] , S2 [t −1] , ..., Sλ [t −1]}. For each
Si[t−1], we ﬁrst illustrate how to select the candidate branches
based on the received signals over K subcarriers in time unit
t. The inner layer operation is performed over each subcarrier
k separately.
For a received signal point y(k) [t], most candidate output
signal points lie in the neighborhood of the received signal
point since the noise power obeys the Gaussian distribution
with a given variance σ2. Therefore, instead of recoding all
the signal points corresponding to potential branches, we only
record those lying in the neighborhood6.
To be speciﬁc, for each subcarrier k, given the current
encoder state s(k)
i
[t −1], the set of all possible input data
sequences is denoted as B and |B| = 2qdf . The set of all
possible output coded sequences can be denoted as C(k)
poss,i [t]
such that each c(k) [t] ∈C(k)
poss,i [t] satisﬁes that
P

c(k) [t] |s(k)
i
[t −1] , b(k)
= 1, ∀b(k) ∈B.
(21)
The candidate output signal points over subcarrier k can then
be obtained by
A(k)
cand,i [t] =
n
Al ∈Ak|d

y(k) [t] , Al

≤aσ2, Al =
g

c(k) [t]

, c(k) [t] ∈C(k)
poss,i [t]
o
,
(22)
6The neighborhood of the received signal point can be deﬁned by a circle
whose center is this signal point.
where d

y(k)
t
, Al

is the Euclidean distance between y(k)
t
and
the signal point Al, a is the radius parameter. Based on the
deﬁnitions of A(k)
cand,i [t] and C(k)
poss,i [t], we observe that each
Al ∈A(k)
cand,i [t] corresponds to an output coded sequence
and an input data sequence. For convenience, we denote
them as members in the set of candidate coded sequences
C(k)
cand,i [t] and the set of candidate data sequences B(k)
cand,i [t],
respectively.
b) Outer Layer Soft-decision Viterbi Operation: In time
unit t, given a stored super encoder state Si[t −1] and the
outcome from the inner layer operation, we perform the cross
check to obtain the survivor paths for time unit t.
For each super encoder state Si [t −1], multiple candidate
branches are generated based on C(k)
cand,i [t] and B(k)
cand,i [t].
Speciﬁcally, a candidate branch (Ccand,i [t] , Bcand,i [t]) can
be constructed by
Ccand,i [t] =
n
c(k) [t] |c(k) [t] ∈C(k)
cand,i [t] , 1 ≤k ≤K
o
Bcand,i [t] =
n
b(k) [t] |b(k) [t] ∈B(k)
cand,i [t] , 1 ≤k ≤K
o
,
(23)
in which P

c(k) [t] |s(k)
i
[t −1] , b(k)
= 1 for 1 ≤k ≤K.
The set C [t] (deﬁned in Section III.A) can then be con-
structed by performing the cross check on the candidate
branches. If a candidate branch (Ccand,i [t] , Bcand,i [t]) sat-
isﬁes Proposition 2, we refer to it as a qualiﬁed branch. For
the qualiﬁed branch, we then add Ccand,i [t] into the set C [t]
and record the corresponding super encoder state Si [t −1].
Given the set C [t], we then select at most λ survivor paths
for time unit t based on the total path lengths. For each
Ccand,i [t] ∈C [t], we can obtain the super encoder state S [t]
based on the corresponding input Bcand,i [t] and the previous
state Si [t −1]. The path length with respect to S [t] is then
calculated as
PLength (S [t]) = PLength (Si [t −1])
+
XK
k=1 d

y(k) [t] , g

c(k) [t]

,
(24)
in which c(k) [t] ∈Ccand,i [t] and PLength (Si [t −1]) is the
history total path length with respect to Si [t −1].
Based on the above equation, we select up to λ code
sequences from C [t] and the corresponding survivor paths with
respect to various super encoder states S [t].
c) Overall Suboptimal Decoding Scheme: The whole
algorithm is presented in detail in Algorithm 2. In each time
unit t, we aim to update the survivor paths based on the
stored paths in time unit t −1 and the received signals in
time unit t. Speciﬁcally, for each subcarrier k and each stored
encoder state s(k)
i
[t −1] (1 ≤i ≤λ), we ﬁrst perform an
inner layer soft-decision operation (line 5-9). The sets of
candidate output coded sequences and input bit sequences
are selected and temporally stored given the received signal
y(k) [t]. We then perform the outer layer soft-decision Viterbi
operation (line 10-20) in which the set of qualiﬁed branches
satisfying Proposition 2 is selected based on the candidate
coded sequences and bit sequences. By sorting the path lengths
with respect to these selected branches, we update up to λ
survivor paths and super encoder states in time unit t with the
shortest path lengths (line 19-20). After η + m time units, the


## Page 10


10
shortest survivor path terminating at the all-zero super encoder
state is selected as the ﬁnal path (line 21-22). Different from
the traditional Viterbi algorithm, the decoded bit sequence is
already stored in each time unit, and thus, it can be directly
obtained from the ﬁnal path.
Algorithm 2 Two-layer Soft-decision Viterbi Algorithm for
Joint NOMA Decoding
Input: K received signal sequences y(1), y(2), · · · , y(K) of
length η + m, the TCM encoder state diagram, NOMA
mapping matrix F, noise variance σ2, channel coefﬁcients
Output:
J decoded bit sequences for J users
1: Initialization:
2: Set S [0] as the all-zero super encoder state
3: Set S [0] = {S [0]}
4: for t = 1 to η + m do
5:
Set C [t] = ∅
6:
for i = 1 to |S [t −1]| do
7:
for k = 1 to K do
8:
Construct the set of candidate output signal
points A(k)
cand,i [t] according to (22)
9:
Obtain
the
candidate
sets
C(k)
cand,i [t]
and
B(k)
cand,i [t] based on (21) and (22)
10:
repeat
11:
Construct
the
candidate
branch
(Ccand,i [t] , Bcand,i [t]) from C(k)
cand,i [t] and B(k)
cand,i [t]
according to (23)
12:
if the candidate branch never shows up and
satisﬁes Proposition 2 then
13:
Add Ccand,i [t] to C [t]
14:
Record Bcand,i [t] and Si [t −1]
15:
until there is no new candidate branch any more
16:
for each C [t] ∈C [t] do
17:
Obtain S [t] based on the recorded Bcand [t] and
S [t −1]
18:
Calculate the path length PLength (S [t]) accord-
ing to (24)
19:
Sort the obtained path lengths and update the ﬁrst λ
paths with the shortest lengths
20:
as survivor paths (shown in (20))
21: Select the shortest survivor path in time unit η +m which
terminates at the all-zero super
22: encoder state as the ﬁnal path
23: return the decoded bit sequences corresponding to the
ﬁnal path
d) Computational Complexity Analysis: The computa-
tional complexity of Algorithm 2 in each time unit t comes
from three parts:
• Inner layer operation (line 6-9): For each super encoder
state Si [t −1] and each subcarrier k, at most 2qdf bit se-
quences are checked to construct C(k)
cand,i [t] and B(k)
cand,i [t]
based on (21) and (22). Since there are K subcarriers and
at most λ stored super encoder states in time unit t, the
complexity of the inner layer operation is O
 λK2qdf 
.
Note that in a practical NOMA scheme, we usually set
qdf ≤6 such that the complexity is tolerable.
• Searching for qualiﬁed branches (line 10-15): Suppose
that the number of candidate bit sequences for each
super encoder state Si [t −1] and each subcarrier k is
M (k)
i
and M (k)
i
≤2qdf . For each Si [t −1], the number
of candidate branches is QK
k=1 M (k)
i
. The process of
checking whether a candidate branch satisﬁes Proposition
2 can be performed when constructing such a branch.
Therefore, the complexity of constructing all qualiﬁed
branches is O

λ QK
k=1 M (k)
i

. In practice, the value of
M (k)
i
is directly inﬂuenced by the radius parameter a and
σ2 in (22), as will be discussed in Section V.
• Updating survivor paths (line 16-20): Suppose that the
number of qualiﬁed branches7 given a super encoder state
Si [t −1] is Qi, i.e., |C [t]| = Pλ
i=1 Qi. To update the
survivor paths, we need to sort the qualiﬁed branches
and the complexity can be given by O
Pλ
i=1 Qi
2
.
The total complexity of Algorithm 2 can be obtained by adding
up the above three parts. We will present detailed results in
Fig. 5 in Section V.
V. SIMULATION RESULTS
In this section, we consider a NOMA system as shown in
Fig. 1. For the convolutional encoder in AWGN channels, the
coefﬁcients of the parity-check sequences in octal form are
selected based on the look-up table in [24]. For simplicity,
we only assume perfect channel state information at the
receiver. The link-level performance of our proposed TCM-
based NOMA scheme is compared with the traditional 4-point
code-domain NOMA scheme in [10]. To evaluate the design of
the MD-constellation for TCM-based NOMA, we also propose
a lattice constellation TCM (LC-TCM) based NOMA scheme
as comparison, in which the constellation A(k) constructed
for each subcarrier k is the same as the traditional 2D lattice
constellation [28] of size 2qdf+1. Major simulation parameters
are listed in Table I.
Fig. 3 and Fig. 4 illustrate the BER performance versus
the Eb/N0 over an AWGN channel with and without channel
coding of rate 1/2, respectively. We set λ = 25 and a = 5,
and the spectrum efﬁciency are 3 bits/tone and 1.5 bits/tone,
respectively. In both ﬁgures, the BER performance of the
TCM-based NOMA outperforms that of the traditional code-
domain NOMA scheme with high Eb/N0 and the gap between
them increases with Eb/N0. When Eb/N0 is small, the error
correcting capacity of the TCM system is restricted due to
the high noise level, which is very common in the coded
systems. This leads to a worse performance than the traditional
scheme. However, as Eb/N0 increases, the inﬂuence of bursty
channel errors on the TCM-based NOMA becomes smaller,
and thus, the performance gain obtained from the joint coded
7The upper bound of Qi is closely related to the mapping matrix F. For ex-
ample, based on F in (2), we have Qmax = M(1)
i
·min
n
2q(df −1), M(2)
i
o
·
2q. The detailed proof is omitted due to the limitation of space.


## Page 11


11
TABLE I
MAJOR SIMULATION PARAMETERS
Parameter
Value
The number of users sharing the same subcarrier
df
3
The number of non-zero elements in a sparse
codeword N
2
The number of bits to be coded for a user in
each time unit q
2
Convolutional encoder rate r/(r + 1)
3/4
MD mother constellation
df ×16QAM
Frame length
1000 bits
Spectral efﬁciency
1.5 or 3 bis/tone
radius parameter a
4 ∼6
Maximum number of survivor paths in each time
unit λ
5 ∼35
Number of register states V
4
Interleaver size
32×16 (in symbol)
Maximum Doppler shift in Rayleigh channels
50 Hz
Sampling frequency for Rayleigh channels
1/1800 s
7
8
9
10
11
12
13
14
15
16
17
Eb/N0 (dB)
10-7
10-6
10-5
10-4
10-3
10-2
10-1
100
BER
Traditional code-domain NOMA [9]
TCM-based NOMA
LC-TCM based NOMA
OFDMA - 8PSK
Fig. 3.
BER v.s. Eb/N0 over AWGN channels without channel coding.
7
8
9
10
11
12
13
14
15
16
Eb/N0 (dB)
10-7
10-6
10-5
10-4
10-3
10-2
10-1
BER
Traditional code-domain NOMA [9]
OFDMA - 8PSK
TCM-based NOMA
Fig. 4.
BER v.s. Eb/N0 over AWGN channels with convolutional channel
coding of rate 1/2.
modulation grows. Fig. 3 also shows that the TCM-based
NOMA outperforms the LC-TCM based NOMA scheme. The
lattice constellation applied in the LC-TCM based scheme fails
0
200
400
600
800
1000
1200
1400
1600
0
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
Number of qualified branches
C.D.F. of the number of qualified branches
 
 
Eb/N0 = 12, λ = 25, a = 5
Eb/N0 = 11, λ = 25, a = 5
Eb/N0 = 10, λ = 25, a = 5
Eb/N0 = 12, λ = 25, a = 6
Eb/N0 = 10, λ = 15, a = 5
Fig. 5.
C.D.F. of the number of qualiﬁed branches in Algorithm 2.
2
4
6
8
10
12
Eb/N0 (dB)
10-8
10-6
10-4
10-2
100
BER
 = 5
 = 25
 = 35
Fig. 6.
BER performance v.s. Eb/N0 with different number of survivor
paths.
10
11
12
13
14
15
16
17
18
19
20
Eb/N0(dB)
10-4
10-3
10-2
10-1
100
BER
Traditional code-domain NOMA [9]
TCM-based NOMA
OFDM - 8PSK
LC-TCM based NOMA
Fig. 7.
BER v.s. Eb/N0 over Rayleigh fading channels.
to optimize the positions of multiple MD points, leading to
a small MFSE distance of the system and bad performance


## Page 12


12
compared to the proposed scheme. This implies that the con-
struction of the MD-mother constellation is of vital importance
for joint coded modulation.
Speciﬁcally, In Fig. 3 we observe that without channel
coding, the BER performance of the traditional code-domain
NOMA is worse than that of the OFDMA scheme due to
the existence of multi-user interference. Beneﬁted from the
joint codeword design of different users, our proposed TCM-
based NOMA can achieve a better BER performance than
both the OFDMA scheme and the traditional NOMA scheme
when Eb/N0 is over 11 dB. This implies that TCM-based
NOMA provides a method to compensate for the degraded
performance of traditional NOMA when the channel coding
is not considered. In Fig. 4, the traditional NOMA scheme
outperforms the OFDMA scheme when channel coding is
adopted, which is in consistent with existing works on NOMA.
To evaluate the computational complexity of our proposed
decoding scheme, we adopt the number of qualiﬁed branches
for each time unit t as the metrics, i.e., |C [t]| = Pλ
i=1 Qi,
mentioned in Section IV.B.2.d. Fig. 5 shows the cumulative
distribution function (C.D.F.) of |C [t]|, Pr (|C [t]| ≤˜c), versus
˜c for different Eb/N0 and decoding parameters. For a ﬁxed
number of limited survivor paths λ and radius parameter a,
the complexity grows as Eb/N0 decreases. A smaller Eb/N0
implies a higher noise level σ2, and thus the number of
candidate output signal points grows according to (22), leading
to more candidate branches and higher complexity. This also
reveals the reason that the complexity increases with the radius
parameter a when Eb/N0 and λ are ﬁxed. Besides, Fig. 5 also
shows that the complexity of our proposed decoding scheme
decreases with λ becoming smaller.
Fig. 6 shows the BER performance of the TCM-based
NOMA scheme versus the Eb/N0 over an AWGN channel
for different numbers of survivor paths λ. As λ increases,
the BER performance improves since the probability that a
correct path can be found in the survivor paths is larger. Note
that when Eb/N0 is too small or high enough, the increase
of λ does not have much inﬂuence on the BER performance.
When Eb/N0 is small, it is still hard for the decoder to select
the right path from a large number of survivor paths due to
interference caused by high noise level. When Eb/N0 is large
enough, the correct path is usually the shortest survivor path
for each time unit, and thus, it is not necessary to increase λ
any more. Since both the BER performance and the complexity
grow with λ, a trade-off can be achieved between these two
metrics.
Fig. 7 presents the BER performance versus the Eb/N0 over
a Rayleigh channel with λ = 25 and a = 6. Compared to the
case with an AWGN channel, the encoder state diagram is
modiﬁed as mentioned in Section III.B.3 and the interleaving
across the time-frequency resources is performed. Since the
number of branches leaving from one state is larger than
that of the registers in the convolutional encoder, the shortest
error path length is limited. Therefore, when Eb/N0 is small,
the bursty channel errors of the fading channels may be
beyond the scope of the system’s error control capacity. As
Eb/N0 grows, the performance gain brought by joint encoding
exceeds the negative effects caused by the noise level. Thus,
our proposed scheme signiﬁcantly outperforms the traditional
NOMA scheme when Eb/N0 is larger than 13dB. Fig. 7 also
shows that 1) the carefully designed MD constellation in the
TCM-based NOMA scheme brings better BER performance
than the lattice constellation in the LC-TCM scheme; 2)
the traditional code-domain NOMA outperforms the OFDMA
scheme in Rayleigh fading environments.
VI. CONCLUSIONS
In this paper, we have proposed a TCM-based NOMA
scheme in which the codewords of multiple users are jointly
designed based on the MD-TCM techniques, aiming at im-
proving the coding gain of the system. For the encoder
design, an MD constellation is constructed and the signal
set is selected and labeled to maximize the MFSE distance
of the system. To perform the joint decoding, the detection
criteria for MLSD are formulated in which the non-orthogonal
nature is utilized. A suboptimal two-layer soft-decision Viterbi
decoding scheme is then proposed. Simulation results have
showed that the TCM-based NOMA scheme performed better
than the traditional code-domain NOMA scheme and OFDMA
scheme in terms of the BER performance for both the AWGN
channels and the Rayleigh fading channels with or without
channel coding.
APPENDIX A
PROOF OF PROPOSITION 1
As shown in Algorithm 1, in each FPO iteration, a point
Al ∈A1
b is swapped with the farthest point of A1
b, i.e., Ar∗∈
A2
b. Based on line 35-36 in Algorithm 1, after swapping the
minimum distance between Ar∗and A1
b is larger than that
between Al and A1
b, i.e.,
dr∗ A1
b ∪{Ar∗} \Al

> dl
 A1
b

,
(25)
and the minimum distance between Al and A2
b is no smaller
than the MSSD of A2
b. Based on (9), we can infer that the
MSSD of A1
b is also increasing since the minimum distance
of each point in A1
b is increasing. According to (10) and (25),
the average minimum distance of the updated subset A1
b, i.e.,
¯d
 A1
b

, is larger than that of the original subset A1
b after one
FPO iteration. Since there always exists an upper bound of
¯d
 A1
b

, Phase 2 will stop within a limited number of iterations.
APPENDIX B
PROOF OF COMPLEXITY OF ALGORITHM 1
For convenience, we assume that |Ab| = N. In Phase 1,
the complexity of the sorting process in line 2 is O (L log L)
with L = C2
N. The insertion of a point into the DT is O (1),
and thus, the complexity of the greedy algorithm (line 5-22) is
O (N). Therefore, the complexity of Phase 1 is O
 N 2 log N

.
For each FPO iteration of Phase 2, the complexity of the
DT-SEARCH operation is O (g) in which g is the number
of a point’s Delaunay neighbors. It is commonly assumed that
g = O (1) for well-distributed point sets [23]. From line 25-37,
the complexity is O
 N 2
in the worst case. By using a binary
search tree to update the vertices in the DT, the complexity of
one FPO iteration can be reduced to O (N log N) [20].


## Page 13


13
REFERENCES
[1] B. Di, L. Song, Y. Li, and S. Zhang, “Trellis coded modulation for code-
domain non-orthogonal multiple access networks,” in IEEE Int. Conf.
Commun. (ICC), Kansas, MI, May 2018.
[2] Z. Ding, L. Dai, and V. Poor, “MIMO-NOMA design for small packet
transmission in the Internet of Things,” IEEE Access, pp. 1393-1405,
vol. 4, Apr. 2016.
[3] B. Di, L. Song, Y. Li, and G. Li, “Non-orthogonal multiple access
for high-reliable and low-latency V2X communications in 5G systems,”
IEEE J. Sel. Areas Commun., pp. 2383-2397, vol. 35, no. 10, Oct. 2017.
[4] L. Song, Y. Li, Z. Ding, and H. Poor, “Resource management in non-
orthogonal multiple access networks for 5G and beyond,” IEEE Network,
pp. 8-14, vol. 31, no. 4, Aug. 2017.
[5] Z. Ding, P. Fan, and H. Poor, “Impact of user pairing on 5G nonorthogo-
nal multiple-access downlink transmissions,” IEEE Trans. Veh. Technol.,
vol. 65, no. 8, pp. 6010-6023, Aug. 2016.
[6] Z. Ding, X. Lei, G. Karagiannidis, R. Schober, J. Yuan, V. Bhargava,
“A survey on non-orthogonal multiple access for 5G networks: research
challenges and future trends,” IEEE J. Sel. Areas Commun., pp. 2181-
2195, vol. 35, no. 10, Oct. 2017.
[7] L. Dai, B. Wang, Y. Yuan, S. Han, C. I, and Z. Wang, “Non-orthogonal
multiple access for 5G: solutions, challenges, opportunities, and future
research trends,” IEEE Communications Magazine, pp. 74-81, vol. 53,
no. 9, Sept. 2015.
[8] Y. Saito, Y. Kishiyama, A. Benjebbour, T. Nakamura, A. Li, and
K. Higuchi, “Non-orthogonal multiple access (NOMA) for cellular
future radio access,” in IEEE Veh. Tech. Conf. (VTC), Dresden, Germany,
Jun. 2013.
[9] B. Di, L. Song, and Y. Li, “Sub-channel assignment, power allocation
and user scheduling for non-orthogonal multiple access networks,” IEEE
Trans. Wireless Commun., pp. 7686-7698, vol. 15, no. 11, Nov. 2016.
[10] H. Nikopour, and H. Baligh, “Sparse Code Multiple Access,” IEEE
Int. Symp. Personal Indoor and Mobile Radio Commun., pp. 332-336,
Sept. 2013, London, UK.
[11] M. Beko, and R.Dinis, “Designing Good Multi-Dimensional Constel-
lations,” IEEE Wireless Commun. Lett., vol. 1, no. 3, pp. 221-224,
Jun. 2012.
[12] M. Taherzadeh, H. Nikopour, A. Bayesteh, and H. Baligh, “SCMA
codebook design,” IEEE Veh. Tech. Conf., pp. 1-5, Sep. 2014, Vancouver,
BC.
[13] M. Vaeri, Z. Ding, and H.V. Poor, Multiple access techniques for 5G
wireless networks and beyond, Springer, 2019.
[14] Y. Wu, S. Zhang, and Y. Chen, “Iterative multiuser receiver in sparse
code multiple access systems,” IEEE Int. Commun. Conf., London, UK,
May 2015.
[15] L. Yu, X. Lei, P. Fan, and D. Chen, “An optimized design of SCMA
codebook based on star-QAM signaling constellations,” in Int. Conf.
Wireless Commun. & Signal Process. (WCSP), pp. 1-5, Oct. 2015,
Nanjing, China.
[16] C. Yan, G. Kang, and N. Zhang, “A dimension distance-based SCMA
codebook design,” IEEE Access, pp. 5471-5479, vol. 5, Mar. 2017.
[17] J. Bao, Z. Ma, Z. Ding, G. Karagiannidis, and Z. Zhu, “On the design of
multiuser codebooks for uplink SCMA systems,” IEEE Commun. Lett.,
pp. 1920-1923, vol. 20, no. 10, Oct. 2016.
[18] Y. Du, B. Dong, Z. Chen, J. Fang, P. Gao, and Z. Liu, “Low-complexity
detector in sparse code multiple access systems,” IEEE Commun. Lett.,
pp. 1812-1815, vol. 20, no. 9, Sept. 2016.
[19] S. Lin, and D. Costello, Error control coding, Prentice Hall, 2004.
[20] T. Schlomer, D. Heck, and O. Deussen, “Farther-point optimized point
sets with maximum minimum distance”, in Proceedings of the ACM
SIGGRAPH Symposium on High Performance Graphics, pp. 135-142,
Vancouver, Canada, Aug. 2011.
[21] Z. Chen, Z. Yuan, Y. Choi, L. Liu, and W. Wang, “Variational blue noise
sampling”, IEEE Trans. Visualization Computer Graphics, pp. 1784-
1796, vol. 18, no. 10, Oct. 2012.
[22] L. Floriani, and E. Puppo, “An on-line algorithm for constrained Delau-
nay triangulation,” CVGIP: Graphical Models and Image Processing,
pp. 290-300, vol. 54, no. 4, July. 1992.
[23] J. Erickson, “Dense point sets have sparse Delaunay triangulations,”
Discrete & Computational Geometry, pp. 83-115, vol. 33, no. 1,
Jan. 2005.
[24] S. Pietrobon, R. Deng, A. LaFanechere, G. Ungerboeck, and D. Costello,
“Trellis coded multi-dimensional phase modulation,” IEEE Trans. In-
form. Theory, pp. 63-89, vol. 36, no. 1, Jan. 1990.
[25] D. Divsalar, and M. Simon, “The design of trellis coded MPSK for
fading channels: performance criteria,” IEEE Trans. Commun., pp. 1004-
1012, vol. 36, no. 9, Sept. 1988.
[26] S. Jamali, and T. Le-Ngoc, “A new 4-state 8PSK TCM scheme for fast
fading, shadowed mobile radio channels,” IEEE Trans. Veh. Technol.,
pp. 216-222, vol. 40, no. 1, Feb. 1991.
[27] J. Hagenauer, and P. Hoeher, “A Viterbi algorithm with soft-decision out-
puts and its applications,” in IEEE Global Commun. Conf. (GlobeCom),
Dallas, TX, Dec. 1989.
[28] G. Forney, and L. Wei, “Multidimensional constellations-Part I: intro-
duction, ﬁgures of merit, and generalized cross constellations,” IEEE
Trans. Inf. Theory, vol. 7, no. 6, pp. 877-892, Aug. 1989.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
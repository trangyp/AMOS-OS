---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1210.2107v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1210.2107v2_On_Optimal_TCM_Encoders

> Source: 1210.2107v2_On_Optimal_TCM_Encoders.pdf

> Pages: 12

---


## Page 1


arXiv:1210.2107v2  [cs.IT]  25 Mar 2013
Preprint, September 17, 2018.
1
On Optimal TCM Encoders
Alex Alvarado, Member, IEEE, Alexandre Graell i Amat, Senior Member, IEEE,
Fredrik Br¨annstr¨om, Member, IEEE, and Erik Agrell, Senior Member, IEEE
Abstract—An asymptotically optimal trellis-coded modulation
(TCM) encoder requires the joint design of the encoder and
the binary labeling of the constellation. Since analytical ap-
proaches are unknown, the only available solution is to perform
an exhaustive search over the encoder and the labeling. For
large constellation sizes and/or many encoder states, however,
an exhaustive search is unfeasible. Traditional TCM designs
overcome this problem by using a labeling that follows the set-
partitioning principle and by performing an exhaustive search
over the encoders. In this paper we study binary labelings for
TCM and show how they can be grouped into classes, which
considerably reduces the search space in a joint design. For 8-ary
constellations, the number of different binary labelings that must
be tested is reduced from 8! = 40320 to 240. For the particular
case of an 8-ary pulse amplitude modulation constellation, this
number is further reduced to 120 and for 8-ary phase shift keying
to only 30. An algorithm to generate one labeling in each class
is also introduced. Asymptotically optimal TCM encoders are
tabulated which are up to 0.3 dB better than the previously best
known encoders.
Index Terms—Binary reﬂected Gray code, bit-interleaved
coded modulation, coded modulation, convolutional encoder,
performance bounds, set-partitioning, trellis-coded modulation,
Viterbi decoding.
I. INTRODUCTION
The ﬁrst breakthrough in coding for the bandwidth-limited
regime came with Ungerboeck’s trellis-coded modulation
(TCM) [1]–[4] in the early 80s where the concept of labeling
by set-partitioning (SP) was introduced. TCM was quickly
adopted in the modem standards in the early 90s and is a
well studied topic [5], [6, Sec. 8.12], [7, Ch. 18]. Another
important discovery in coded modulation (CM) design came
in 1992 when Zehavi introduced the so-called bit-interleaved
coded modulation (BICM) [8], [9], usually referred to as a
pragmatic approach for CM [10].
The design philosophies behind TCM and BICM for the
additive white Gaussian noise (AWGN) channel are quite dif-
ferent. Ungerboeck’s scheme is constructed coupling together
a convolutional encoder and a constellation labeled using the
Parts of this work were presented at the Information Theory and Appli-
cations (ITA) Workshop, San Diego, CA, February 2012, and at the IEEE
International Symposium on Information Theory (ISIT) 2012, Cambridge,
MA, July 2012.
Research supported by the European Community’s Seventh’s Framework
Programme (FP7/2007-2013) under grant agreement No. 271986, by the
Swedish Research Council under grants #621-2006-4872 and #621-2011-
5950, and by the Swedish Agency for Innovation Systems (VINNOVA) under
the P36604-1 MAGIC project. The calculations were performed on resources
provided by the Swedish National Infrastructure for Computing (SNIC) at
C3SE.
A. Alvarado is with the Department of Engineering, University of
Cambridge, UK (email: alex.alvarado@ieee.org). A. Graell i Amat, F.
Br¨annstr¨om and Erik Agrell are with the Department of Signals and
Systems, Chalmers University of Technology, Gothenburg, Sweden (email:
{alexandre.graell,fredrik.brannstrom, agrell}@chalmers.se).
SP principle. For constellations having certain symmetries, SP
can be achieved by using the natural binary code (NBC) [2,
Fig. 4], [4, Fig. 3]. On the other hand, BICM is typically a
concatenation of a convolutional encoder and a constellation
labeled by the binary reﬂected Gray code (BRGC) [11], [12]
through a bit-level interleaver. The BRGC is often used in
BICM because it maximizes the BICM generalized mutual
information for medium and high signal-to-noise ratios [9,
Sec. III], [13, Sec. IV]. In TCM, the selection of the con-
volutional encoder is done so that the minimum Euclidean
distance (MED) is maximized, while in BICM the encoders
are the ones optimized for binary transmission. BICM systems
are then based on maximum free Hamming distance codes
[7, Sec. 12.3] or on the so-called optimum distance spectrum
(ODS) encoders ﬁrst tabulated in [14, Tables III–V] and [15,
Tables II–IV] and later extended in [16].
It was recently shown in [17] that if the interleaver is
removed in BICM, its performance over the AWGN channel
is greatly improved. This was later analyzed in detail in [18]
for a rate R = 1/2 encoder and a 4-ary pulse amplitude
modulation (PAM) constellation, where the system in [17]
was called “BICM with trivial interleavers” (BICM-T) and
recognized as a TCM transmitter used with a BICM receiver.
Moreover, BICM-T was shown to perform asymptotically as
well as TCM (in terms of MED) [2, Table I] if properly
chosen convolutional encoders are used [18, Table III]. The
transmitters in [2, Table I] and [18, Table III] for the 8-
state (memory ν = 3) convolutional encoder1 are shown in
Fig. 1 (a) and Fig. 1 (c), respectively.
The authors in [18] failed to note that in fact the optimal
TCM encoder found when analyzing BICM-T is equivalent2
to the one proposed by Ungerboeck 30 years ago [19]. For a
4PAM constellation, one simple (although not unique) way of
obtaining Ungerboeck’s SP is by using the NBC. Moreover,
the NBC can be generated using the BRGC plus one binary
addition (which we call transform) applied to its inputs, as
shown in Fig. 1(b). If the transform is included in the mapper,
the encoder in Fig. 1(a) is obtained, while if it is included
in the convolutional encoder, the TCM encoder in Fig. 1(c)
is obtained. This equivalence also applies to encoders with
larger number of states3 and simply reveals that for 4PAM,
a TCM transceiver based on a BRGC mapper will have
identical performance to Ungerboeck’s TCM if the encoder is
properly modiﬁed, where the modiﬁcation is the application of
1Throughout this paper, all polynomial generators are given in octal.
2We use “equivalent” to denote two encoders with the same input-output
relationship. This is formally deﬁned in Sec. III.
3This equivalence does not directly hold because [18, Table III] lists the
encoders in lexicographic order and because for some values of ν there are
more than one encoder with identical performance.


## Page 2


Preprint, September 17, 2018.
2
(a)
(b)
(c)
i1,n
i1,n
i1,n
xn
xn
xn
Transform
SP Mapper (NBC)
BRGC Mapper
BRGC Mapper
G = [13, 4]
G = [13, 4]
G = [13, 17]
x1
x1
x1
x2
x2
x2
x3
x3
x3
x4
x4
x4
00
00
00
01
01
01
10
10
10
11
11
11
Fig. 1.
Three equivalent TCM encoders [19]: (a) convolutional encoder with
polynomial generators G = [13, 4] and an SP mapper [2]; (c) convolutional
encoder with polynomial generators G = [13, 17] and a BRGC mapper [18].
The encoder in (b) shows how a transformation based on a binary addition
can be included in the mapper (to go from (b) to (a)) or in the encoder (to
go from (b) to (c)).
a simple transform. The equivalence between TCM encoders
and encoders optimized for the BRGC and the NBC as well
as the relationship between the encoders in [18] and [2] were
ﬁrst pointed out to us by R. F. H. Fischer [19]. The idea of
applying a linear transformation to the labeling/encoder can be
traced back to [20, Fig. 6.5] (see also [21] and [22, Ch. 2]).
TCM designs based on SP are considered heuristic [23,
Sec. 3.4], and thus, they do not necessarily lead to an optimal
design [24, p. 680].4 The problem of using non-SP labelings
for TCM has been studied in [24, Sec. 13.2.1], [26, Sec. 8.6],
and [27]. TCM encoders using the BRGC were designed in
[25], by searching over convolutional encoders maximizing the
MED. In [20, Ch. 6] and [21], a non-Gray non-SP labeling was
used and TCM encoders with optimal spectrum were tabulated.
In a related work, Wesel et al. introduced in [28] the concept
of the edge proﬁle (EP) of a labeling, and argued that in most
cases, the EP can be used to ﬁnd equivalent TCM encoders in
terms of MED. The EP is also claimed to be a good indication
of the quality of a labeling for TCM in [28, Sec. I]; however, its
optimality is not proven. Consequently, an exhaustive search
over labelings with optimal EP does not necessarily lead to an
optimal design [29].
In summary, as clearly explained in [28, Sec. I], traditional
TCM designs either optimize the encoder for a constellation
labeled using the SP principle, or simply connect a convolu-
tional encoder designed for binary transmission with an ad-
4Indeed, the results in [25, Tables 2–3], [20, Ch. 6] and [21] show the
suboptimality of the SP principle in terms of the multiplicities associated
with the events at MED.
hoc binary labeling. It has been known for many years that
optimal TCM encoders are obtained only by jointly designing
the convolutional encoder and the labeling of a TCM encoder
[7, p. 966]. However, to the best of our knowledge, there are
no works formally addressing this problem, and thus, optimal
TCM encoders are yet to be found.
In this paper, we address the joint design of the feedforward
convolutional encoder and the labeling for TCM. To this end,
we show that binary labelings can be grouped into different
classes that lead to equivalent TCM encoders. The classes are
closely related to the Hadamard classes introduced in [30] in
the context of vector quantization. This classiﬁcation allows
us to formally prove that in any TCM encoder, the NBC can
be replaced by many other labelings (including the BRGC)
without causing any performance degradation, provided that
the encoder is properly selected. This explains the asymptotic
equivalence between BICM-T and TCM observed in [18].
Moreover, since the classiﬁcation reduces the number of
labelings that must be tested in an exhaustive search, we
use it to tabulate optimal TCM encoders for 4-ary and 8-ary
constellations.
II. PRELIMINARIES
A. Notation Convention
Throughout this paper, scalars are denoted by italic letters x,
row vectors by boldface letters x = [x1, . . . , xN], temporal se-
quences by underlined boldface letters x = [x[1], . . . , x[Ns]],
and matrices by capital boldface letters X where xi,j repre-
sents the entry of X at row i, column j. The transpose of
a matrix/vector is denoted by [·]T. Matrices are sometimes
expressed in the compact form X = [x1; x2; . . . ; xM], where
xi = [xi,1, . . . , xi,N] is the ith row. Sets are denoted using cal-
ligraphic letters C and the binary set is deﬁned as B ≜{0, 1}.
Binary addition is denoted by a ⊕b.
The probability mass function (PMF) of the random variable
Y is denoted by PY (y) and the probability density function
(PDF) of the random variable Y
by pY (y). Conditional
PDFs are denoted as pY |X(y|x). The tail probability of a
standard Gaussian random variable is denoted by Q(x) ≜
1
√
2π
R ∞
x e−ξ2/2 dξ.
B. TCM Encoder
We consider the TCM encoder shown in Fig. 2 where a
feedforward convolutional encoder of rate R = k/m is serially
connected to a mapper ΦL and the index L emphasizes the
dependency of the mapper on the labeling (deﬁned later). At
each discrete time instant n, the information bits i1,n, . . . , ik,n
are fed to the convolutional encoder, which is fully determined
by k different νp-stage shift registers with p = 1, . . . , k,
and the way the input sequences are connected (through the
registers) to its outputs. Closely following the notation of
[7, Sec. 11.1], we denote the memory of the convolutional
encoder by ν = Pk
p=1 νp, and the number of states by 2ν. The
connection between the input and output bits is deﬁned by the
binary representation of the convolutional encoder matrix [31,


## Page 3


Preprint, September 17, 2018.
3
i1,n
ik,n
u1,n
um,n
Conv.
Encoder
TCM Encoder
· · ·
· · ·
ΦL
x[n]
Fig. 2.
Generic TCM encoder under consideration: A feedforward convolu-
tional encoder of rate R = k/m with 2ν states serially concatenated with a
memoryless m-bit mapper ΦL.
eq. (11.6)]
G ≜


g(1)
1
g(2)
1
. . .
g(m)
1
g(1)
2
g(2)
2
. . .
g(m)
2
...
...
...
...
g(1)
k
g(2)
k
. . .
g(m)
k


,
(1)
where g(l)
p
≜[g(l)
p,1, . . . , g(l)
p,νp+1]T ∈Bνp+1 is a column
vector representing the connection between the pth input
sequence and the lth output sequence with l = 1, . . . , m. The
coefﬁcients g(l)
p,1, . . . , g(l)
p,νp+1 are associated with the input bits
ip,n, . . . , ip,n−νp, respectively, and G ∈B(ν+k)×m. Through-
out this paper, we will show the vectors g(l)
p
deﬁning G either
in binary or octal notation. When shown in octal notation, g(l)
p,1
represents the most signiﬁcant bit (see Fig. 1).
The convolutional encoder matrix (1) allows us to express
the output of the convolutional encoder at time n, which we
deﬁne as un ≜[u1,n, . . . , um,n], as a function of (ν + k)
information bits, i.e.,
un = jnG,
(2)
where jn ≜[i(1)
n , . . . , i(k)
n ] with i(p)
n
≜[ip,n, . . . , ip,n−νp] are
the information bits, and the matrix multiplication is in GF(2).
The coded bits un are mapped to real N-dimensional
constellation symbols using the mapper ΦL : Bm →X,
where X ⊂RN is the constellation used for transmission, with
|X| = M = 2m. We use x[n] ∈X to denote the transmitted
symbols at time n and the matrix X = [x1; x2; . . . ; xM]
with xq ∈RN and q = 1, . . . , M to denote the ordered
constellation points. We assume that the symbols are equally
likely and that the constellation X is normalized to unit energy,
i.e., Es ≜EX[∥X∥2] = 1/M P
x∈X ∥x∥2 = 1. As shown in
Fig. 2, each symbol represents k information bits.
The binary labeling of the qth symbol in X is denoted by
cq = [cq,1, . . . , cq,m] ∈Bm, where cq,l is the bit associated
with the lth input of the mapper in Fig. 2. The labeling matrix
is deﬁned as L = [c1; c2; . . . ; cM], where cq in L corresponds
to the binary label of the symbol xq in X. Throughout this
paper, we will show the vectors cq in L in either binary or
integer notation.
C. Binary Labelings for TCM
The NBC of order m is deﬁned as N m ≜[n1; n2; . . . ; nM]
where nq = [nq,1, . . . , nq,m] ∈Bm is the base-2 representa-
tion of the integer q−1 and nq,m is the least signiﬁcant bit. The
BRGC of order m is deﬁned as Bm ≜[b1; b2; . . . ; bM] where
bq = [bq,1, . . . , bq,m] ∈Bm. The bits of the BRGC can be
generated from the NBC as bq,1 = nq,1 and bq,l = nq,l−1⊕nq,l
for l = 2, . . . , m. Alternatively, we have nq,l = bq,1 ⊕
. . . ⊕bq,l−1 ⊕bq,l for l = 1, . . . , m, or, in matrix notation,
Bm = N mT and N m = BmT −1, where
T =


1 1 0 . . . 0 0
0 1 1 . . . 0 0
0 0 1 . . . 0 0
...
... ...
0 0 0 . . . 1 1
0 0 0 . . . 0 1


,
T −1 =


1 1 1 . . . 1 1
0 1 1 . . . 1 1
0 0 1 . . . 1 1
...
... ...
0 0 0 . . . 1 1
0 0 0 . . . 0 1


.
(3)
Example 1: The NBC and BRGC of order m = 3 are
N 3 =


0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1


,
B3 =


0 0 0
0 0 1
0 1 1
0 1 0
1 1 0
1 1 1
1 0 1
1 0 0


,
(4)
where the pivots of the labeling matrices (deﬁned in Sec. III-B)
are highlighted.
To formally deﬁne the SP principle for a given constella-
tion X and labeling L, we deﬁne Xl([um+1−l, . . . , um]) ≜
{xq ∈X : [cq,m+1−l, . . . , cq,m] = [um+1−l, . . . , um], q =
1, . . . , M} ⊂X for l = 1, . . . , m −1. Additionally, we deﬁne
the minimum intra-Euclidean distance (intra-ED) at level l as
δl ≜
min
xi,xj∈Xl(u)
i̸=j,u∈Bl
∥xi −xj∥,
l = 1, . . . , m −1.
(5)
and the MED of the constellation as δ0.
Deﬁnition 1 (Set-partitioning [2]): For a given constella-
tion X, the labeling L is said to follow the SP principle if
δ0 < δ1 < . . . < δm−1.
Example 2: Consider an 8PSK constellation (formally de-
ﬁned in Sec. V). It can be easily veriﬁed that if this constella-
tion is labeled by the NBC in (4), an SP-labeled constellation
is obtained. Although the NBC is the most intuitive form
for generating an SP labeling for MPSK constellations, it is
not unique. As an example, consider the semi set-partitioning
(SSP) labeling proposed in [32, Fig. 2(c)] and the so-called
modiﬁed set-partitioning (MSP) labeling [33, Fig. 2(b)]:
LSSP =


0 0 0
1 0 1
0 1 0
1 1 1
1 0 0
0 0 1
1 1 0
0 1 1


,
LMSP =


0 0 0
0 0 1
0 1 0
1 1 1
1 0 0
1 0 1
1 1 0
0 1 1


.
(6)
It can be shown that both labelings follow the SP principle in
Deﬁnition 1.
Example 2 shows that there are multiple labelings that
follow the SP principle. It can be shown that this is also the


## Page 4


Preprint, September 17, 2018.
4
case for MPAM constellations, and that in this case, the NBC
is also an SP labeling.
D. System Optimization and Search Problems
For a given constellation X and memory ν, a TCM encoder
is fully deﬁned by the convolutional encoder matrix G and the
labeling of the constellation L, and thus, a TCM encoder is
deﬁned by the pair Θ = [G, L].
For given integers k, m, and ν, we deﬁne the convolutional
encoder universe as the set Gk,m,ν of all (ν + k) × m binary
matrices5 G which result in a noncatastrophic feedforward
encoder and equally likely symbols.6 We are also interested
in the labeling universe, deﬁned for a given integer m as the
set Lm of all M × m binary matrices whose M rows are all
distinct.
To the best of our knowledge, there are no works addressing
the problem of designing a TCM encoder by exhaustively
searching over the labeling universe and the convolutional
encoder universe. We believe the reason for this is that an
exhaustive search over encoders and labelings is unfeasible
[34, Sec. I]. For example, for 8-ary constellations, there are in
general 8! = 40320 different binary labelings. In this paper,
we show how a joint optimization over all G ∈Gk,m,ν and
L ∈Lm can be restricted, without loss of generality, to a joint
optimization over all G ∈Gk,m,ν and a subset of Lm.
III. EQUIVALENT LABELINGS FOR TCM ENCODERS
In this section, we show that binary labelings can be
grouped into classes, and that all the labelings belonging to
the same class lead to equivalent TCM encoders. This analysis
is inspired by the one in [30], where the so-called Hadamard
classes were used to solve a related search problem in source
coding.
A. Equivalent TCM Encoders
The transmitted symbol at time n of a given TCM encoder
Θ = [G, L] can be expressed using (2) as
x[n] = ΦL(un) = ΦL(jnG).
(7)
Deﬁnition 2: Two TCM encoders Θ = [G, L] and ˜Θ =
[ ˜G, ˜L] are said to be equivalent if they give the same output
symbol for the same information bit sequence, i.e., if they
fulﬁll ΦL(jG) = Φ˜L(j ˜G) for any j ∈Bν+k.
The concept of “equivalent encoders” is more restrictive
than the more well-known concept of “equivalent codes”. Two
equivalent encoders have the same bit error rate (BER) and
frame error rate (FER), whereas two equivalent codes have
the same FER but in general different BER. In this paper,
where BER is an important ﬁgure of merit, we are therefore
more interested in equivalent encoders.
From now on we use Tm to denote the set of all binary
invertible m × m matrices.
5Note that whenever G is given in its binary form, ν1, . . . , νk are also
needed to interpret G correctly according to (1).
6For some matrices G, the symbols x[n] can be nonequally likely. This
would induce nonequally likely symbols (signal shaping) which we do not
consider in this work.
Lemma 1: ΦL(c) = Φ˜L(cT ) where ˜L = LT , for any two
mappers ΦL and Φ˜L that use the same constellation X, any
T ∈Tm, and any c ∈Bm.
Proof: Let vq ≜[0, . . . , 0, 1, 0, . . ., 0] be a vector of
length M, where the one is in position q. From the deﬁ-
nition of the labeling matrix L, it follows that cq = vqL
for q = 1, . . . , M. The mapping ΦL satisﬁes by deﬁnition
ΦL(cq) = xq for q = 1, . . . , M, or, making the dependency
on L explicit,
ΦL(c) = xq,
if c = vqL
(8)
for any c ∈Bm. Similarly, for any c ∈Bm,
Φ˜L(cT ) = xq,
if cT = vq ˜L
= xq,
if c = vqL,
(9)
where the last step follows because L = ˜LT −1. Since the
right-hand sides of (8) and (9) are equal, Φ˜L(cT ) = ΦL(c)
for all c ∈Bm.
The following theorem is the main result of this paper.
Theorem 1: For any G ∈Gk,m,ν, L ∈Lm, and T ∈Tm,
the two TCM encoders Θ = [G, L] and ˜Θ = [ ˜G, ˜L] are
equivalent, where ˜L = LT and ˜G = GT .
Proof: For any j ∈Bν+k, Φ˜L(j ˜G) = Φ˜L(jGT ) =
ΦL(jG), where the last equality follows by Lemma 1. The
theorem now follows using Deﬁnition 2.
Theorem 1 shows that a full search over Gk,m,ν and Lm will
include many pairs of equivalent TCM encoders. Therefore, an
optimal TCM encoder with given parameters can be found by
searching over a subset of Gk,m,ν and the whole set Lm or vice
versa. In this paper, we choose the latter approach, searching
over a subset of Lm.
B. Matrix Factorization
We brieﬂy summarize here some matrix algebra. The fol-
lowing deﬁnition of a reduced column echelon matrix comes
from [35, pp. 183–184], adapted to the fact that we only
consider binary labeling matrices L whose columns are all
nonzero. The ﬁrst nonzero element of the kth column is called
the kth pivot of L. The pivots for N 3 and B3 are highlighted
in (4).
Deﬁnition 3: A matrix L ∈BM×m is a reduced column
echelon matrix if the following two conditions are fulﬁlled:
1) Every row with a pivot has all its other entries zero.
2) The pivot in column l is located in a row below the pivot
in column l + 1, for l = 1, . . . , m −1.
The matrix N 3 in Example 1 (or more generally N m) is
an example of a reduced column echelon matrix. On the other
hand, Bm is not a reduced column echelon matrix because it
does not fulﬁll the ﬁrst condition in Deﬁnition 3.
The following theorem will be used to develop an efﬁcient
search algorithm in the next section. We refer the reader to
[35, p. 187, Corollary 1] for a proof. From now on we use
Rm to denote the set of all reduced column echelon binary
matrices.


## Page 5


Preprint, September 17, 2018.
5
TABLE I
NUMBER OF CLASSES (MR = |Rm|), THEIR CARDINALITY
(MT = |Tm|), AND THE TOTAL NUMBER OF LABELINGS (2m!) FOR
DIFFERENT VALUES OF m.
m
1
2
3
4
5
6
MR 2
4
240
1.038 · 109
2.632 · 1028 6.294 · 1078
MT 1
6
168
20160
9.999 · 106
2.016 · 1010
2m! 2 24 40320 2.092 · 1013 2.631 · 1035 1.269 · 1089
Theorem 2: Any binary labeling L ∈Lm can be uniquely
factorized as
L = LRT ,
(10)
where T ∈Tm and LR ∈Rm.
Theorem 2 shows that all binary labeling matrices L can
be uniquely generated by ﬁnding all the invertible matrices T
(the set Tm) and all reduced column echelon matrices LR (the
set Rm). In particular, we have [36, eq. (1)], [30, eq. (18)]
MT ≜|Tm| =
m
Y
l=1
(2m −2l−1),
(11)
MR ≜|Rm| =
2m!
Qm
l=1(2m −2l−1).
(12)
In Table I, the values for MR and MT for 1 ≤m ≤6
are shown. In this table we also show the number of binary
labelings (|Lm| = 2m! = MRMT), i.e., the number of
matrices L in the labeling universe.
The modiﬁed Hadamard class associated with the reduced
column echelon matrix LR is deﬁned as the set of matrices L
that can be generated via (10) by applying all T ∈Tm. Note
that these modiﬁed Hadamard classes are narrower than the
regular Hadamard classes deﬁned in [30], each including M
reduced column echelon matrices. There are thus MR modiﬁed
Hadamard classes, each with cardinality MT.
As a consequence of Theorems 1 and 2, the two TCM
encoders [G, L] and [GT −1, LR] are equivalent for any
G ∈Gk,m,ν and L ∈Lm, where LR and T are given by
the factorization (10). In other words, all nonequivalent TCM
encoders can be generated using one member of each modiﬁed
Hadamard class only, and thus, a joint optimization over all
G ∈Gk,m,ν and L ∈Lm can be reduced to an optimization
over all G ∈Gk,m,ν and L ∈Rm with no loss in performance.
This means that the search space is reduced by at least a
factor of MT = M!/MR. For example, for 8-ary constellations
(m = 3), the total number of different binary labelings that
must be tested is reduced from 8! = 40320 to 240. Moreover,
as we will see in Sec. V, this can be reduced even further if
the constellation X possesses certain symmetries.
C. Modiﬁed Full Linear Search Algorithm
The problem of ﬁnding the set Rm of reduced column
echelon matrices for a given m can be solved by using a
modiﬁed version of the full linear search algorithm (FLSA)
introduced in [30, Sec. VIII]. We call this algorithm the mod-
iﬁed FLSA (MFLSA). The MFLSA generates one member of
Algorithm 1 Modiﬁed full linear search algorithm (MFLSA)
Input: The order m
Output: Print the MR different reduced column echelon vectors r
1: r ←[0, 1, . . . , M −1]
2: loop
3:
print r
4:
index ←0
5:
while rM = index do
6:
[rindex+1, . . . , rM] ←[rM, rindex+1, . . . , rM−1]
7:
index ←index + 1
8:
while index is a power of 2 do
9:
index ←index + 1
10:
end while
11:
if index = M −1 then
12:
Quit
13:
end if
14:
end while
15:
Find pointer such that rpointer = index
16:
Swap rpointer and rpointer+1
17: end loop
each modiﬁed Hadamard class, the one that corresponds to a
reduced column echelon matrix LR. Its pseudocode is shown
in Algorithm 1. In this algorithm, the vector r = [r1, . . . , rM]
denotes the integer representation of the rows of the matrix LR
where rq = cq,m+2cq,m−1+. . .+2m−1cq,1 for q = 1, . . . , M.
The ﬁrst labeling generated (line 1) is always the NBC.
Then the algorithm proceeds by generating all permutations
thereof, under the condition that no power of two (1, 2, 4, . . .)
is preceded by a larger value. By Deﬁnition 3, this simple
condition assures that only reduced column echelon matrices
are generated.
Example 3: For m = 2, the MFLSA returns the following
reduced column echelon matrices:
R2 =









0 0
0 1
1 0
1 1

,


0 1
0 0
1 0
1 1

,


0 1
1 0
0 0
1 1

,


0 1
1 0
1 1
0 0









,
(13)
where the ﬁrst element in R2 is the NBC deﬁned in Sec. II-C
and again we highlighted the pivots of the matrices. The 6
binary invertible matrices for m = 2 are
T2 =

0 1
1 0

,

0 1
1 1

,

1 0
0 1

,

1 0
1 1

,

1 1
0 1

,

1 1
1 0

.
(14)
Using Theorem 2, all the 24 binary labelings in L2 (see
Table I) can be generated by multiplying the matrices in R2
and T2.
Example 4: For m =
3, the reduced column echelon
matrices generated by the MFLSA are shown in Table II (in
integer notation). The MFLSA ﬁrst generates row number one,
then row number two, then row number three, etc., where each
row is generated from left to right. The ﬁrst column in the
table corresponds to the output of the FLSA of [30]. Columns
two to eight show the additional matrices generated by the
MFLSA, which are obtained from the ﬁrst column by shifting
the symbol zero to the right. In this table we also highlight
the labelings generated by the MFLSA that at the same time
have optimal EP [28] for 8PAM and 8PSK (see Sec. V).
Example 5: If we study the labelings in Example 2, we


## Page 6


Preprint, September 17, 2018.
6
TABLE II
REDUCED COLUMN ECHELON MATRICES FOR m = 3 GENERATED BY THE MFLSA. THE MFLSA FIRST GENERATES ROW NUMBER ONE, THEN ROW
NUMBER TWO, ETC. THE LABELINGS SHOWN IN BOLDFACE HAVE OPTIMAL EP FOR 8PAM (FIRST FOUR COLUMNS) AND FOR 8PSK (FIRST COLUMN).
0 1 2 3 4 5 6 7
1 0 2 3 4 5 6 7
1 2 0 3 4 5 6 7
1 2 3 0 4 5 6 7
1 2 3 4 0 5 6 7
1 2 3 4 5 0 6 7
1 2 3 4 5 6 0 7
1 2 3 4 5 6 7 0
0 1 2 4 3 5 6 7
1 0 2 4 3 5 6 7
1 2 0 4 3 5 6 7
1 2 4 0 3 5 6 7
1 2 4 3 0 5 6 7
1 2 4 3 5 0 6 7
1 2 4 3 5 6 0 7
1 2 4 3 5 6 7 0
0 1 2 4 5 3 6 7
1 0 2 4 5 3 6 7
1 2 0 4 5 3 6 7
1 2 4 0 5 3 6 7
1 2 4 5 0 3 6 7
1 2 4 5 3 0 6 7
1 2 4 5 3 6 0 7
1 2 4 5 3 6 7 0
0 1 2 4 5 6 3 7
1 0 2 4 5 6 3 7
1 2 0 4 5 6 3 7
1 2 4 0 5 6 3 7
1 2 4 5 0 6 3 7
1 2 4 5 6 0 3 7
1 2 4 5 6 3 0 7
1 2 4 5 6 3 7 0
0 1 2 4 5 6 7 3
1 0 2 4 5 6 7 3
1 2 0 4 5 6 7 3
1 2 4 0 5 6 7 3
1 2 4 5 0 6 7 3
1 2 4 5 6 0 7 3
1 2 4 5 6 7 0 3
1 2 4 5 6 7 3 0
0 1 2 3 4 6 5 7
1 0 2 3 4 6 5 7
1 2 0 3 4 6 5 7
1 2 3 0 4 6 5 7
1 2 3 4 0 6 5 7
1 2 3 4 6 0 5 7
1 2 3 4 6 5 0 7
1 2 3 4 6 5 7 0
0 1 2 4 3 6 5 7
1 0 2 4 3 6 5 7
1 2 0 4 3 6 5 7
1 2 4 0 3 6 5 7
1 2 4 3 0 6 5 7
1 2 4 3 6 0 5 7
1 2 4 3 6 5 0 7
1 2 4 3 6 5 7 0
0 1 2 4 6 3 5 7
1 0 2 4 6 3 5 7
1 2 0 4 6 3 5 7
1 2 4 0 6 3 5 7
1 2 4 6 0 3 5 7
1 2 4 6 3 0 5 7
1 2 4 6 3 5 0 7
1 2 4 6 3 5 7 0
0 1 2 4 6 5 3 7
1 0 2 4 6 5 3 7
1 2 0 4 6 5 3 7
1 2 4 0 6 5 3 7
1 2 4 6 0 5 3 7
1 2 4 6 5 0 3 7
1 2 4 6 5 3 0 7
1 2 4 6 5 3 7 0
0 1 2 4 6 5 7 3
1 0 2 4 6 5 7 3
1 2 0 4 6 5 7 3
1 2 4 0 6 5 7 3
1 2 4 6 0 5 7 3
1 2 4 6 5 0 7 3
1 2 4 6 5 7 0 3
1 2 4 6 5 7 3 0
0 1 2 3 4 6 7 5
1 0 2 3 4 6 7 5
1 2 0 3 4 6 7 5
1 2 3 0 4 6 7 5
1 2 3 4 0 6 7 5
1 2 3 4 6 0 7 5
1 2 3 4 6 7 0 5
1 2 3 4 6 7 5 0
0 1 2 4 3 6 7 5
1 0 2 4 3 6 7 5
1 2 0 4 3 6 7 5
1 2 4 0 3 6 7 5
1 2 4 3 0 6 7 5
1 2 4 3 6 0 7 5
1 2 4 3 6 7 0 5
1 2 4 3 6 7 5 0
0 1 2 4 6 3 7 5
1 0 2 4 6 3 7 5
1 2 0 4 6 3 7 5
1 2 4 0 6 3 7 5
1 2 4 6 0 3 7 5
1 2 4 6 3 0 7 5
1 2 4 6 3 7 0 5
1 2 4 6 3 7 5 0
0 1 2 4 6 7 3 5
1 0 2 4 6 7 3 5
1 2 0 4 6 7 3 5
1 2 4 0 6 7 3 5
1 2 4 6 0 7 3 5
1 2 4 6 7 0 3 5
1 2 4 6 7 3 0 5
1 2 4 6 7 3 5 0
0 1 2 4 6 7 5 3
1 0 2 4 6 7 5 3
1 2 0 4 6 7 5 3
1 2 4 0 6 7 5 3
1 2 4 6 0 7 5 3
1 2 4 6 7 0 5 3
1 2 4 6 7 5 0 3
1 2 4 6 7 5 3 0
0 1 2 3 4 5 7 6
1 0 2 3 4 5 7 6
1 2 0 3 4 5 7 6
1 2 3 0 4 5 7 6
1 2 3 4 0 5 7 6
1 2 3 4 5 0 7 6
1 2 3 4 5 7 0 6
1 2 3 4 5 7 6 0
0 1 2 4 3 5 7 6
1 0 2 4 3 5 7 6
1 2 0 4 3 5 7 6
1 2 4 0 3 5 7 6
1 2 4 3 0 5 7 6
1 2 4 3 5 0 7 6
1 2 4 3 5 7 0 6
1 2 4 3 5 7 6 0
0 1 2 4 5 3 7 6
1 0 2 4 5 3 7 6
1 2 0 4 5 3 7 6
1 2 4 0 5 3 7 6
1 2 4 5 0 3 7 6
1 2 4 5 3 0 7 6
1 2 4 5 3 7 0 6
1 2 4 5 3 7 6 0
0 1 2 4 5 7 3 6
1 0 2 4 5 7 3 6
1 2 0 4 5 7 3 6
1 2 4 0 5 7 3 6
1 2 4 5 0 7 3 6
1 2 4 5 7 0 3 6
1 2 4 5 7 3 0 6
1 2 4 5 7 3 6 0
0 1 2 4 5 7 6 3
1 0 2 4 5 7 6 3
1 2 0 4 5 7 6 3
1 2 4 0 5 7 6 3
1 2 4 5 0 7 6 3
1 2 4 5 7 0 6 3
1 2 4 5 7 6 0 3
1 2 4 5 7 6 3 0
0 1 2 3 4 7 5 6
1 0 2 3 4 7 5 6
1 2 0 3 4 7 5 6
1 2 3 0 4 7 5 6
1 2 3 4 0 7 5 6
1 2 3 4 7 0 5 6
1 2 3 4 7 5 0 6
1 2 3 4 7 5 6 0
0 1 2 4 3 7 5 6
1 0 2 4 3 7 5 6
1 2 0 4 3 7 5 6
1 2 4 0 3 7 5 6
1 2 4 3 0 7 5 6
1 2 4 3 7 0 5 6
1 2 4 3 7 5 0 6
1 2 4 3 7 5 6 0
0 1 2 4 7 3 5 6
1 0 2 4 7 3 5 6
1 2 0 4 7 3 5 6
1 2 4 0 7 3 5 6
1 2 4 7 0 3 5 6
1 2 4 7 3 0 5 6
1 2 4 7 3 5 0 6
1 2 4 7 3 5 6 0
0 1 2 4 7 5 3 6
1 0 2 4 7 5 3 6
1 2 0 4 7 5 3 6
1 2 4 0 7 5 3 6
1 2 4 7 0 5 3 6
1 2 4 7 5 0 3 6
1 2 4 7 5 3 0 6
1 2 4 7 5 3 6 0
0 1 2 4 7 5 6 3
1 0 2 4 7 5 6 3
1 2 0 4 7 5 6 3
1 2 4 0 7 5 6 3
1 2 4 7 0 5 6 3
1 2 4 7 5 0 6 3
1 2 4 7 5 6 0 3
1 2 4 7 5 6 3 0
0 1 2 3 4 7 6 5
1 0 2 3 4 7 6 5
1 2 0 3 4 7 6 5
1 2 3 0 4 7 6 5
1 2 3 4 0 7 6 5
1 2 3 4 7 0 6 5
1 2 3 4 7 6 0 5
1 2 3 4 7 6 5 0
0 1 2 4 3 7 6 5
1 0 2 4 3 7 6 5
1 2 0 4 3 7 6 5
1 2 4 0 3 7 6 5
1 2 4 3 0 7 6 5
1 2 4 3 7 0 6 5
1 2 4 3 7 6 0 5
1 2 4 3 7 6 5 0
0 1 2 4 7 3 6 5
1 0 2 4 7 3 6 5
1 2 0 4 7 3 6 5
1 2 4 0 7 3 6 5
1 2 4 7 0 3 6 5
1 2 4 7 3 0 6 5
1 2 4 7 3 6 0 5
1 2 4 7 3 6 5 0
0 1 2 4 7 6 3 5
1 0 2 4 7 6 3 5
1 2 0 4 7 6 3 5
1 2 4 0 7 6 3 5
1 2 4 7 0 6 3 5
1 2 4 7 6 0 3 5
1 2 4 7 6 3 0 5
1 2 4 7 6 3 5 0
0 1 2 4 7 6 5 3
1 0 2 4 7 6 5 3
1 2 0 4 7 6 5 3
1 2 4 0 7 6 5 3
1 2 4 7 0 6 5 3
1 2 4 7 6 0 5 3
1 2 4 7 6 5 0 3
1 2 4 7 6 5 3 0
ﬁnd that the SSP belongs to the ﬁrst modiﬁed Hadamard class
(LR = N 3) while the MSP belongs to a different class, i.e.,
LSSP = N 3


1 0 0
0 1 0
1 0 1

,
LMSP = LR


1 1 1
0 1 0
0 0 1

,
(15)
where LT
R = [0, 1, 2, 4, 7, 6, 5, 3] (in integer notation) is the
233th labeling generated by the MFLSA (see Table II). This
shows that the NBC does not span all the labelings that follow
the SP principle.
D. NBC and BRGC
Another way of interpreting the result in Theorem 1 is that
for any TCM encoder ˜Θ = [ ˜G, ˜L], a new equivalent TCM
encoder can be generated using an encoder G = ˜GT −1 and
a labeling L = ˜LT −1 that belongs to the same modiﬁed
Hadamard class as the original labeling ˜L. One direct conse-
quence of this result is that any TCM encoder using the NBC
labeling N m and a convolutional encoder G is equivalent to
a TCM encoder using the BRGC Bm and a convolutional
encoder GT with T given by (3). This is formalized in the
following theorem.
Theorem 3: The BRGC and the NBC of any order m
belong to the same modiﬁed Hadamard class.
Proof: The BRGC and NBC are related via Bm =
N mT , with T given by (3). The theorem now follows from
Theorem 2 and the deﬁnition of a modiﬁed Hadamard class.
Example 6: For the two TCM encoders in Fig. 1, the NBC
and BRGC labelings are related via B2 = N 2T , i.e.,


0 0
0 1
1 1
1 0

=


0 0
0 1
1 0
1 1


1 1
0 1

.
(16)
Thus, the BRGC and the NBC of order m = 2 belong to the
same modiﬁed Hadamard class, and convolutional encoders
can be chosen to make the two resulting TCM encoders equiv-
alent. This was illustrated in Fig. 1, where the transform block
corresponds to the transform matrix T = [1, 1; 0, 1] = T −1.
Since N 2 = B2T −1, the TCM encoders [G[13,17], B2] and
[G[13,4], N 2] are equivalent, where
G[13,4] =
1 0 1 1
0 1 0 0
T
= G[13,17]T −1 =
1 0 1 1
1 1 1 1
T 1 1
0 1

.
Example 6 and Theorem 3 explain, in part, the results
obtained in [18], where it is shown that the encoders in [18,
Table III] used with the BRGC perform asymptotically as well
as Ungerboeck’s TCM.7
IV. ERROR PROBABILITY ANALYSIS
The results in Sec. III are valid for any memoryless channel
model and any receiver; however, from now on we focus on the
AWGN channel and a maximum likelihood (ML) decoder. In
this section, we brieﬂy review bounds on the error probability
of TCM encoders under these constraints. These bounds will
be used in Sec. IV-B to deﬁne optimal TCM encoders. The
bounds we develop can be found in standard textbooks, see,
7The “in part” comes from the fact that the system studied in [18] uses a
(suboptimal) BICM receiver.


## Page 7


Preprint, September 17, 2018.
7
e.g., [5, Ch. 4] and [23, Ch. 6], and are re-derived here to
make the paper self-contained.
Since TCM encoders are in general not linear8, the proba-
bility of error depends on the transmitted sequence, i.e., it is
not possible to make the assumption that the all-zero sequence
was transmitted [5, p. 101]. This constraint can be lifted if the
TCM encoder is “regular” [37, Lemma 2], “superlinear” [34,
Sec. II-D], “scrambled” [18], or “uniform” [38], [7, Ch. 18].
However, regularity, superlinearity and uniformity do not hold
for all constellation and labelings9, and thus, we cannot use it
in this paper.
We consider a baseband-equivalent discrete-time real-valued
multi-dimensional AWGN channel. The transmitted sequence
of equally likely symbols is denoted by x = [x[1], . . . , x[Ns]]
where x[n] ∈X is the N-dimensional symbol transmitted
at discrete time n and Ns is the block length. The received
sequence of symbols is y = [y[1], . . . , y[Ns]], where y[n] =
x[n]+z[n] ∈RN is the received vector at time instant n. The
channel noise z[n] ∈RN is an N-dimensional vector with
samples of independent and identically distributed (i.i.d.) ran-
dom variables with zero mean and variance N0/2 per dimen-
sion. The signal-to-noise ratio (SNR) is deﬁned as Es/N0 =
1/N0. The conditional transition PDF of the channel is given
by pY |X(y|xq) = (N0π)−N
2 exp
 −N0
−1∥y −xq∥2
.
A. Error Bounds
Let Xℓbe the set of all length-ℓsymbol sequences that start
at an arbitrary time instant and encoder state. Let ˆ
Xℓ(x) be
the set of length-ℓsequences ˆx ̸= x that start and end at the
same encoder state as x ∈Xℓand where all the other ℓ−1
intermediate states are different. An error event occurs when
the decoder chooses a sequence ˆx ∈ˆ
Xℓ(x) which is different
from the transmitted sequence x. Using the union bound, the
probability of an error event of an ML TCM decoder at a
given time instant can be upper-bounded as [5, eq. (4.1)]10
Pe ≤
∞
X
ℓ=1
X
x∈Xℓ
PX(x)
X
ˆx∈ˆ
Xℓ(x)
PEP(x, ˆx),
(17)
where PEP(x, ˆx) is the pairwise error probability (PEP)
and PX(x) is the probability that the encoder generates the
sequence x.
Assuming i.i.d. information bits, the probability of the
sequence starting at a given state is 1/2ν. There are 2k equally
likely branches leaving each state of the trellis at each time
instant, and thus,
PX(x) = 1
2ν
1
2kℓ.
(18)
The PEP depends only on the accumulated squared ED (SED)
8Note that the usual deﬁnition of linearity applies to codes in GF(q)N .
However, since TCM codes are deﬁned over the real numbers, the usual
deﬁnition of linearity does not apply.
9For 8PSK for example, there is in fact no binary labeling that gives a
regular TCM encoder [23, Sec. 3.3].
10All the bounds in this section are dependent on the TCM encoder Θ.
However, to alleviate the notation, we omit writing out Θ as an explicit
argument.
between x and ˆx and can be shown to be
PEP(x, ˆx) = Q


v
u
u
t Es
2N0
ℓ
X
n=1
∥x[n] −ˆx[n]∥2

.
(19)
Let Ad2,ℓdenote the number of pairs x ∈Xℓand ˆx ∈
ˆ
Xℓ(x) at accumulated SED d2 = Pℓ
n=1 ∥x[n] −ˆx[n]∥2 and
let Aw,d2,ℓdenote the number of pairs at accumulated SED d2
generated by input sequences at Hamming distance w. Using
(18)–(19) and the deﬁnition of Ad2,ℓ, (17) can be expressed
as
Pe ≤
X
d2∈D
Ad2Q


s
d2Es
2N0

,
(20)
where
Ad2 ≜
∞
X
ℓ=1
1
2ν
1
2kℓAd2,ℓ=
∞
X
ℓ=1
1
2ν
1
2kℓ
∞
X
w=1
Aw,d2,ℓ
(21)
is the distance multiplicity of the TCM encoder. In (20) D
is the set of all possible accumulated SEDs between any two
sequences, i.e., all the values of d2 for which Ad2 ̸= 0.
To obtain a bound on the BER, each error event must be
weighted by the number of bits in error (w out of k), i.e.,
BER ≤
X
d2∈D
Bd2Q


s
d2Es
2N0

,
(22)
where
Bd2 ≜
∞
X
ℓ=1
1
2ν
1
2kℓ
∞
X
w=1
w
k Aw,d2,ℓ
(23)
is the bit multiplicity of the TCM encoder.
Finally, to obtain a bound on the FER we generalize the
bound presented in [39] for convolutional codes to obtain
FER ≤Ns
X
d2∈D
Ad2Q


s
d2Es
2N0

.
(24)
B. Optimum Distance Spectrum TCM Encoders
In this section we deﬁne TCM encoders that are optimal
for asymptotically high SNR. These deﬁnitions will be used
in Sec. V to tabulate optimized TCM encoders for different
conﬁgurations.
We call the inﬁnite set of triplets {d2, Ad2, Bd2} the distance
spectrum (DS) of a given TCM encoder Θ = [G, L], where
d2 ∈D. We also deﬁne the ith SED of a given TCM encoder
by d2
i with i = 1, 2, 3, . . ., where d2
i+1 > d2
i and d2
1 is the
minimum SED of the TCM encoder. These SEDs correspond
to the ordered set of SEDs in D. Based on (22) and (24) we
deﬁne an optimum DS-TCM (ODS-TCM) as follows.
Deﬁnition 4: A TCM encoder Θ
=
[G, L] with DS
{d2, Ad2, Bd2} is said to have a superior DS to another TCM
encoder ˜Θ = [ ˜G, ˜L] with DS { ˜d2, ˜A ˜d2, ˜B ˜d2} if one of the
following conditions is fulﬁlled:
1) d2
1 > ˜d2
1, or
2) d2
1 = ˜d2
1, Ad2
1 < ˜A ˜d2
1 and Bd2
1 < ˜B ˜d2
1, or


## Page 8


Preprint, September 17, 2018.
8
3) there exist an integer l > 1 such that d2
i = ˜d2
i , Ad2
i = ˜A ˜d2
i
and Bd2
i = ˜B ˜d2
i for i = 1, 2, . . . , l −1 and d2
l > ˜d2
l or
d2
l = ˜d2
l , Ad2
l < ˜A ˜d2
l and Bd2
l < ˜B ˜d2
l .
Deﬁnition 5: For a given constellation X and memory ν,
the TCM encoder Θ = [G, L] is said to be an ODS-TCM
encoder if no other TCM encoder ˜Θ = [ ˜G, ˜L], for all ˜G ∈
Gk,m,ν and ˜L ∈Lm, has a superior DS compared to Θ.
An ODS-TCM encoder in Deﬁnition 5 is the asymptotically
optimal TCM encoder in terms of BER and FER for a
given block length Ns. Unlike the more classical deﬁnition of
optimal encoders, ODS-TCM encoders are deﬁned as encoders
that are optimal in terms of both Ad2 and Bd2. This implies
that in principle, for some combinations of k, m, ν, it is
possible that no ODS-TCM encoder exists. As we will see in
Sec. V, this is not an uncommon situation. Moreover, by using
this somehow nonstandard deﬁnition we avoid listing encoders
that have optimal BER performance but possibly rather poor
FER performance (or vice versa). This situation happens for
R = 1/2 and 4PAM, as we will show in Sec. V-A.
V. NUMERICAL RESULTS
In this section we study well-structured one- and two-
dimensional constellations, i.e., MPAM and MPSK con-
stellations. An MPAM constellation is deﬁned by X
=
[x1, x2, . . . , xM]T with xq
= −(M + 1 −2q)∆∈R,
q = 1, . . . , M, and ∆2 = 3/(M 2 −1) so that Es = 1.
An MPSK constellation is deﬁned by X = [x1; x2; . . . ; xM]
with xq = [cos (2π(q −1)/M), sin (2π(q −1)/M)] ∈R2
and q = 1, . . . , M.
In the following sections we show results of exhaustive
searches over Gk,m,ν and Rm, and thus, these results should
be understood as a complete answer to the problem of jointly
designing the feedforward encoder and the labeling for TCM
encoders. The ODS-TCM encoders presented are obtained by
comparing the ﬁrst ﬁve nonzero elements in the spectrum,
which we numerically calculate using a generalization of
the algorithm presented in [31, Sec. 12.4.3].11 On the other
hand, the bounds used to compare with simulation results
were calculated using 20 terms. The tabulated results are
ordered ﬁrst in terms of the output of the MFLSA, then in
lexicographic order for the memories ν1, . . . , νk, and then in
lexicographic order for the encoder matrices G. This ordering
becomes relevant when there are multiple TCM encoder with
identical (and optimal) ﬁve-term DS.
A. ODS-TCM Encoders for MPAM
MPAM constellations are symmetric around zero. Because
of this, two TCM encoders based on an MPAM constellation,
the ﬁrst one using the labeling L = [c1; c2; . . . ; cM−1; cM]
and the second one using a “reverse” labeling L′
=
[cM; cM−1; . . . ; c2; c1], are equivalent for any M. This result
implies that the number of binary labelings that give nonequiv-
alent TCM encoders is MR/2. Speciﬁcally, for m = 2 and
m = 3 (4PAM and 8PAM), only 2 and 120 labelings need
11Note that if more than ﬁve elements are considered different ODS-TCM
encoders might be found.
2
3
4
5
6
7
8
10
−7
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
10
−1
10
0
 
 
Es/N0 [dB]
FER/BER
FER Bound
BER Bound
Sim. [·]U
Sim. [·]AB
ν = 4
ν = 6
Fig. 3.
BER/FER bounds in (22) and (24) and simulations for Ungerboeck’s
encoders and the ODS-TCM encoders in Table III for Ns = 1000, 4PAM,
R = 1/2 (1 [bit/symbol]), and ν = 4, 6.
to be evaluated, respectively, instead of 24 and 40320 in an
exhaustive search, see Table I.
To generate only the MR/2 nonequivalent labelings for
MPAM, the MFLSA in Algorithm 1 can be modiﬁed as
follows. Replace M on lines 5 and 6 with e(index), where
the integer function e(q) is deﬁned as M/2 if q = 0 and M
otherwise. This has the effect of only generating labelings in
which the all-zero label is among the ﬁrst M/2 positions (i.e.,
the ﬁrst 4 columns of Table II for 8PAM).
1) R = 1/2 and 4PAM: The results obtained for R = 1/2
and 4PAM and different values of ν are shown in Table III. The
table reports the DS as well as the labeling and convolutional
encoder for the ODS-TCM encoders (shown as [·]AB). For
ν = 5, however, no ODS-TCM encoder was found, i.e., there
is no TCM encoder that is optimal in terms of both Ad2 and
Bd2. Instead, we list the TCM encoder with best Ad2 among
those with optimal Bd2 (shown as [·]B), or vice versa (shown
as [·]A). In this table we also include Ungerboeck’s encoders12,
which we denote by [·]U. When Ungerboeck’s labeling (NBC)
or Ungerboeck’s convolutional encoder coincide with [·]AB or
[·]B, we use the notation [·]UAB or [·]UB, respectively. The
results in Table III show that no gains in terms of MED are
obtained and that the NBC is indeed the optimal labeling
for all memories. The key difference between Ungerboeck’s
design and the ODS-TCM encoders is the better multiplicities
obtained. To compare the gains obtained by the ODS-TCM
encoders over Ungerboeck’s encoders, we show in Fig. 3 their
BER/FER for ν = 4, 6. This ﬁgure clearly shows the gains
obtained by using the ODS-TCM encoders which are visible
not only at high SNR, but also for low SNR values (see,
e.g., the FER markers for ν = 6).
12Ungerboeck did not report results for ν = 1, and thus, we do not include
them in the Tables, i.e., we only show the ODS-TCM encoder for ν = 1.


## Page 9


Preprint, September 17, 2018.
9
TABLE III
DISTANCE SPECTRUM OF ODS-TCM ENCODERS ([·]AB) AND UNGERBOECK’S ENCODERS ([·]U) FOR k = 1 [BIT/SYMBOL] AND 4PAM (m = 2). THE
NOTATION [·]A AND [·]B IS USED WHEN NO ODS-TCM ENCODER WAS FOUND.
ν
LT
G
Distance Spectrum {d2, Ad2, Bd2 }
1 [0,1,2,3]AB
[3,1]AB
{4.00, 0.50, 0.50},
{4.80, 0.50, 1.00},
{5.60, 0.50, 1.50},
{6.40,0.50, 2.00},
{7.20, 0.50, 2.50}
2 [0,1,2,3]UAB [5,2]U
{7.20, 1.00, 1.00},
{8.00, 1.25, 2.50},
{8.80, 1.75, 5.25},
{9.60,2.56, 10.25},
{10.40, 3.81, 19.06}
[7,2]AB
{7.20, 0.50, 0.50},
{8.00, 1.25, 2.50},
{8.80, 1.63, 4.88},
{9.60,2.56, 10.25},
{10.40, 3.78, 18.91}
3 [0,1,2,3]UAB [13,4]UAB
{8.00, 0.25, 0.50},
{8.80, 1.00, 3.00},
{9.60, 1.56, 6.25},
{10.40, 2.75,9.75},
{11.20, 3.14, 16.84}
4 [0,1,2,3]UAB [23,4]U
{8.80, 0.63, 1.88},
{9.60, 0.50, 2.00},
{10.40, 2.00, 6.00},
{11.20, 2.02,10.09},
{12.00, 2.03, 13.22}
[23,10]AB
{8.80, 0.13, 0.38},
{9.60, 0.50, 2.00},
{10.40, 1.88, 5.38},
{11.20, 2.39,10.34},
{12.00, 3.72, 21.03}
5 [0,1,2,3]UAB [45,10]UB
{10.40, 1.13, 1.63}, {11.20, 1.52, 5.09},
{12.00, 2.59, 12.16},
{12.80, 3.58,22.13},
{13.60, 5.29, 38.60}
[55,4]A
{10.40, 0.75, 1.75}, {11.20, 2.13, 8.75},
{12.00, 2.14, 10.48},
{12.80, 4.47,24.75},
{13.60, 5.45, 37.01}
6 [0,1,2,3]UAB [103,24]U
{11.20, 2.34, 5.91}, {12.80, 2.82, 22.01}, {14.40, 7.60, 57.35},
{16.00, 31.39,268.35}, {17.60, 74.37, 779.76}
[107,32]AB
{11.20, 0.13, 0.50}, {12.00, 1.44, 5.81},
{12.80, 1.41, 5.77},
{13.60, 1.73,12.58},
{14.40, 4.58, 31.53}
7 [0,1,2,3]UAB [235,126]U
{12.80, 2.19, 8.19}, {14.40, 3.05, 17.66}, {16.00, 10.09, 89.43},
{17.60, 25.03,231.04}, {19.20, 90.45, 920.63}
[313,126]AB
{12.80, 1.46, 8.02}, {14.40, 4.77, 34.60}, {16.00, 15.42, 130.51}, {17.60, 35.60,375.08}, {19.20, 103.30, 1213.89}
8 [0,1,2,3]UAB [515,362]U
{13.60, 0.53, 4.66}, {14.40, 1.89, 10.79}, {15.20, 1.66, 14.10},
{16.00, 3.81,30.45},
{16.80, 6.03, 49.34}
[677,362]AB
{13.60, 0.36, 2.05}, {14.40, 1.06, 6.41},
{15.20, 1.47, 11.09},
{16.00, 3.44,23.69},
{16.80, 5.25, 41.32}
2) R = 2/3 and 8PAM: The results for R = 2/3 and
8PAM are shown in Table IV. For ν = 1, 2, 3, 4, 6 the reported
encoders are in the form [·]AB, while for ν = 5 no ODS-TCM
was found, and we use the same notation as for 4PAM. Unlike
for R = 1/2, the parity-check matrix reported by Ungerboeck
for R = 2/3 speciﬁes the code but not the encoder. To have a
fair comparison between Ungerboeck’s codes with the ODS-
TCM encoders, we ﬁrst listed all the convolutional encoders
that give Ungerboeck’s parity-check matrix and then pick the
one with optimal Bd2 (all of them have the same Ad2). These
are the encoders reported in Table IV as [·]U. Even though
Ungerboeck’s encoders in Table IV are the best encoders for
that particular parity-check matrix, they coincide with the [·]B
encoders only for one out of six cases (ν = 5). For all the other
cases, the ODS-TCM encoders result in a better spectrum.
Also, unlike for 4PAM, Table IV shows that the NBC is not the
optimal labeling. For example, for ν = 4, the optimal labeling
is LT = [1, 2, 4, 0, 6, 5, 3, 7]AB, which does not follow the SP
principle (cf. Deﬁnition 1). In Fig. 4, we show the BER/FER
results obtained by the ODS-TCM encoders for R = 2/3,
8PAM, and ν = 4, 6. This ﬁgure shows the tightness of the
bounds and again gains over Ungerboeck’s encoders.
B. ODS-TCM Encoders for MPSK
A TCM encoder based on an MPSK constellation is not
affected by a circular rotation of its labeling, i.e., without
loss of generality it can be assumed that the all zero label
is assigned to the constellation point x1 = [1, 0]. The conse-
quence of this is that for MPSK constellations, the number
of reduced column echelon matrices that give nonequivalent
TCM encoders is further reduced by a factor of M. In view
of the results in Table I, for 4PSK, there is only one labeling
that needs to be tested, e.g., the NBC. For m ≥3, the
nonequivalent labelings can be obtained from the MFLSA by
setting index ←3 in line 4, which gives the FLSA of [30].
For example, for M = 8, the output corresponds to the ﬁrst
column of Table II, which gives 30 labelings.
10
10.5
11
11.5
12
12.5
13
13.5
14
14.5
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
10
−1
10
0
 
 
Es/N0 [dB]
FER/BER
FER Bound
BER Bound
Sim. [·]U
Sim. [·]AB
ν = 4
ν = 6
Fig. 4.
BER/FER bounds in (22) and (24) and simulations for Ungerboeck’s
encoders and the ODS-TCM encoders in Table IV for Ns = 1000, 8PAM,
R = 2/3 (2 [bit/symbol]), and ν = 4, 6.
1) R = 1/2 and 4PSK: In this case there is only one
labeling to be tested (the NBC), and thus, only a search over
the encoders needs to be performed. Moreover, without loss
of generality, we can use the BRGC instead (because it is
in the same Hadamard class as the NBC) and search over
encoders for this labeling. Since 4PSK with the BRGC can
be considered as two independent 2PAM constellations (one
in each dimension), the design of TCM encoders in this case
boils down to selecting convolutional encoders with optimal
spectrum (in the sense of Deﬁnition 5).
We have performed an exhaustive search for convolutional
encoders with optimal spectrum up to ν = 12 and found that
our results coincide with those reported in [40, Table I]. For
ν = 1, 2, 3, 4, 5, 6, 11, 12 the optimal convolutional encoders


## Page 10


Preprint, September 17, 2018.
10
TABLE IV
DISTANCE SPECTRUM OF ODS-TCM ENCODERS ([·]AB) AND UNGERBOECK’S ENCODERS ([·]U) FOR k = 2 [BIT/SYMBOL] AND 8PAM (m = 3). THE
NOTATION [·]A AND [·]B IS USED WHEN NO ODS-TCM ENCODER WAS FOUND.
ν
LT
G
Distance Spectrum {d2, Ad2 , Bd2}
1 [1,2,4,0,6,5,3,7]AB
[1,1,1; 1,3,0]AB
{0.95, 1.13, 0.84},
{1.14, 1.13, 1.69},
{1.33, 1.13, 2.53},
{1.52, 1.13, 3.38},
{1.71, 1.13,4.22}
2 [0,1,2,3,4,5,6,7]UAB [1,0,0; 0,5,2]U
{1.71, 2.25, 1.88},
{1.90, 3.52, 5.11},
{2.10, 6.05, 12.35},
{2.29, 10.56, 27.64},
{2.48, 18.47, 58.91}
[1,0,0; 0,7,2]AB
{1.71, 1.69, 1.69},
{1.90, 3.52, 5.11},
{2.10, 6.01, 12.34},
{2.29, 10.56, 27.64},
{2.48, 18.46, 58.91}
3 [0,1,2,3,4,5,6,7]U
[1,0,0; 0,13,4]U
{1.90, 1.27, 2.11},
{2.10, 3.38, 6.75},
{2.29, 5.49, 14.14},
{2.48, 12.45, 32.48},
{2.67, 18.59, 64.81}
[1,2,4,0,6,5,3,7]AB
[1,1,1; 2,15,0]AB
{1.90, 1.27, 1.90},
{2.10, 3.38, 8.44},
{2.29, 5.49, 17.25},
{2.48, 12.45, 38.50},
{2.67, 18.59, 74.81}
4 [0,1,2,3,4,5,6,7]U
[1,0,0; 0,23,4]U
{2.10, 2.64, 5.59},
{2.29, 2.53, 6.75},
{2.48, 6.75, 13.50},
{2.67, 12.11, 40.55},
{2.86, 15.99, 66.51}
[1,2,4,0,6,5,3,7]AB
[1,1,1; 2,31,0]AB
{2.10, 0.95, 1.90},
{2.29, 2.53, 7.59},
{2.48, 7.91, 21.78},
{2.67, 13.21, 45.70},
{2.86, 19.77, 88.01}
5 [0,1,2,3,4,5,6,7]UAB [1,0,0; 0,45,10]UB
{2.48, 4.32, 6.54},
{2.67, 7.99, 19.45},
{2.86, 14.26, 46.29},
{3.05, 27.05, 102.83},
{3.24, 44.27, 201.33}
[1,0,0; 0,55,4]A
{2.48, 3.80, 6.96},
{2.67, 8.74, 21.63},
{2.86, 13.53, 45.10},
{3.05, 29.51, 106.50},
{3.24, 44.49, 198.08}
6 [0,1,2,3,4,5,6,7]UAB [1,0,0; 0,103,24]U
{2.67, 10.74, 22.97}, {3.05, 19.91, 86.93}, {3.43, 72.68, 343.40}, {3.81, 353.99, 1927.40}, {4.19, 1137.86, 7442.94}
[1,0,0; 0,107,32]AB
{2.67, 1.42, 4.27},
{2.86, 8.46, 24.43},
{3.05, 12.94, 40.47},
{3.24, 15.68, 74.20},
{3.43, 40.61, 182.47}
([·]AB) are in fact the encoders from [16, Table I] (which were
initially optimized only in terms of Bd2). For ν = 7, 8, 9, 10
we found that no optimal encoder exists, i.e., the convolutional
encoders optimal in terms of Ad2 are not optimal in terms of
Bd2 and vice versa.13 These encoders are in fact shown in [40,
Table I]14, which extends the results in [14]–[16] because it
considers both Ad2 and Bd2 as optimization criteria.
Based on the discussion above, we conclude that an ODS-
TCM encoders can be constructed by concatenating the en-
coders in [40, Table I] with a 4PSK constellation labeled
by the BRGC. Alternatively, ODS-TCM encoders can be
obtained by using a 4PSK constellation labeled by the NBC
and using the encoders in [40, Table I] after applying the
transformation T −1 = [1, 1; 0, 1]. For example, for ν = 8,
we found G[515,677] and G[435,657] to be the optimal encoders
in terms of Ad2 and Bd2, respectively, and thus, the two pairs
of equivalent ODS-TCM encoders are Θ = [G[515,677], B2]
and ˜Θ = [G[515,677]T −1, N 2], and Θ = [G[435,657], B2] and
˜Θ = [G[435,657]T −1, N 2].
2) R = 2/3 and 8PSK: The results obtained for R = 2/3
and 8PSK are shown in Table V. Somehow disappointingly,
this table shows that the NBC is indeed the optimal labeling
in all the cases, and thus, the selection of the labeling for
this particular conﬁguration does not provide any gains over
Ungerboeck’s TCM schemes. The better spectrum obtained by
the ODS-TCM encoders in this case then comes only from the
selection of the convolutional encoder.
In Fig. 5, we show the DS for the encoders in Table V with
ν = 4. It is clear from the ﬁgure that an encoder optimal in
terms of Ad2 can be suboptimal in terms of Bd2, and vice
versa. In addition, the ﬁgure shows how the set of SEDs D
is in general different for different encoders. It also shows
how Ungerboeck’s encoder is optimal in terms of Ad2 for the
term at MED, but in general suboptimal if the whole DS is
considered.
We note that depending on ν, the ODS-TCM encoders in
Table V have inferior, equivalent, or superior Bd2 spectrum to
13Convolutional encoders with optimal Ad2 and memories up to ν = 26
have been recently published in [41, Table 7.1].
14Although the search in [40] was performed only considering events at
minimum Hamming distance and not over the whole spectrum.
5
5.5
6
6.5
7
10
0
10
1
 
 
d2
i
Distance Spectrum
Ad2
Bd2
[·]A
[·]B
[·]U
Fig. 5.
DS for encoders with ν = 4 for R = 2/3 and 8PSK from Table V.
those listed in [23, Table 3.2], [20, Table 6.10].15 The reason
for this is that the codes tabulated in [23, Table 3.2], [20,
Table 6.10] are found by searching over parity check matrices
and then converted to feedback encoders (in observer canoni-
cal form [20, Fig. 2.2]). On the other hand, we search over a
different set of encoders, namely, over all the noncatastrophic
feedforward encoders.
All labelings we found for the ODS-TCM encoders (i.e., the
highlighted labelings in Table II and the optimal ones in
Tables IV and V) have optimal EP. This makes us conjecture
that good TCM encoders can be found by using the EP of [28]
on top of the proposed classiﬁcation. This approach would
indeed reduce the search space (for example, for 8PAM and
8PSK constellations, only eight and two labelings, respec-
tively, would need to be tested). However, it would not allow
us to claim optimality in the sense of Deﬁnition 5.
15To have a fair comparison, the values of Bd2 listed in [23, Table 3.2],
[20, Table 6.10] should be scaled by a factor 1/k = 1/2.


## Page 11


Preprint, September 17, 2018.
11
TABLE V
DISTANCE SPECTRUM OF ODS-TCM ENCODERS ([·]AB) AND UNGERBOECK’S ENCODERS ([·]U) FOR k = 2 [BIT/SYMBOL] AND 8PSK (m = 3). THE
NOTATION [·]A AND [·]B IS USED WHEN NO ODS-TCM ENCODER WAS FOUND.
ν
LT
G
Distance Spectrum {d2, Ad2, Bd2 }
1 [0,1,2,3,4,5,6,7]AB
[1,0,0; 0,1,2]AB
{2.59, 2.00, 1.50},
{3.17, 2.00, 3.00},
{3.76, 2.00, 4.50},
{4.00,1.00, 0.50},
{4.34, 2.00, 6.00}
2 [0,1,2,3,4,5,6,7]UAB [1,0,0; 0,5,2]UAB
{4.00, 1.00, 0.50},
{4.59, 4.00, 4.00},
{5.17, 8.00, 14.00},
{5.76,16.00, 38.00}, {6.34, 32.00, 96.00}
3 [0,1,2,3,4,5,6,7]UAB [1,2,0; 4,1,2]U
{4.59, 2.00, 2.50},
{5.17, 4.00, 8.50},
{5.76, 8.00, 25.00},
{6.00,1.00, 0.50},
{6.34, 16.00, 66.00}
[1,2,0; 4,5,2]AB
{4.59, 2.00, 2.00},
{5.17, 4.00, 8.50},
{5.76, 8.00, 25.00},
{6.00,1.00, 0.50},
{6.34, 16.00, 66.00}
4 [0,1,2,3,4,5,6,7]UAB
[2,7,0; 7,3,2]U
{5.17, 2.25, 5.50},
{5.76, 4.63, 14.13},
{6.00, 1.00, 0.50},
{6.34,6.06, 26.50},
{6.59, 4.00, 5.50}
[2,7,0; 7,1,2]A
{5.17, 2.25, 5.00},
{5.76, 3.88, 11.56},
{6.00, 1.00, 0.50},
{6.34,9.56, 38.81},
{6.59, 4.00, 5.50}
[1,4,2; 6,1,0]B
{5.17, 2.50, 5.00},
{5.76, 3.75, 11.25},
{6.34, 8.13, 32.44},
{6.59,3.50, 4.50},
{6.93, 16.19, 80.94}
5 [0,1,2,3,4,5,6,7]UAB [1,2,0; 30,25,16]U
{5.76, 4.00, 10.50}, {6.00, 1.00, 0.50},
{6.34, 4.00, 16.25},
{6.93,4.00, 24.13},
{7.17, 3.00, 7.50}
[1,2,0; 30,25,10]AB
{5.76, 2.00, 5.75},
{6.00, 1.00, 0.50},
{6.34, 3.63, 15.56},
{6.59,3.00, 5.50},
{6.93, 8.06, 40.63}
6 [0,1,2,3,4,5,6,7]UAB
[4,11,0; 13,4,6]U
{6.34, 5.25, 22.56}, {7.17, 10.00, 28.88}, {7.51, 14.53, 98.50},
{8.00,3.00, 3.75},
{8.34, 38.56, 199.78}
[1,6,0; 27,25,12]A
{6.34, 3.25, 12.00}, {7.17, 7.25, 17.88},
{7.51, 19.13, 119.17}, {8.00,3.00, 5.00},
{8.34, 36.69, 159.69}
[1,6,0; 35,31,6]B
{6.34, 3.56, 11.50}, {7.17, 7.25, 16.88},
{7.51, 16.58, 92.05},
{8.00,3.50, 4.75},
{8.34, 30.63, 150.81}
VI. CONCLUSIONS
In this paper we analyzed the problem of jointly designing
the feedforward convolutional encoder and the labeling of a
TCM encoder. It was shown that the number of labelings that
need to be checked can be reduced if they are grouped into
modiﬁed Hadamard classes. This classiﬁcation allowed us to
prove that it is always possible to design a TCM encoder based
on the BRGC with identical performance to the one proposed
by Ungerboeck in 1982. The numerical results show that in
most cases, the NBC is the optimal binary labeling for TCM
encoders and that gains up to 0.3 dB over the previously best
known TCM schemes can indeed be obtained.
The classiﬁcation of labelings presented this paper does
not make any assumption on the channel nor on the receiver.
Because of this, the presented design methodology can be used
to design optimal TCM encoders for other channels as well
as for suboptimal (BICM) decoders.
The algorithm introduced in this paper to ﬁnd all the label-
ings that need to be tested in an exhaustive search becomes
impractical for constellations with more than 16 points. In this
case, a suboptimal solution based on an algorithm (inspired by
the linearity increasing swap algorithm of [30, Sec. IX]) that
generates a subset of (good) labelings could be devised. This
approach could also be combined with the concept of labelings
with optimal EP [28]. The design of such an algorithm is left
for further investigation.
ACKNOWLEDGEMENT
The authors would like to thank R. F. H. Fischer for pointing
out the equivalence between TCM encoders with encoders
optimized for the BRGC and the NBC, and showing how
the encoders in [18] and [2] are related. These observations
inspired this full paper. The authors would also like to thank
R. D. Wesel for fruitful discussions.
REFERENCES
[1] G. Ungerboeck and I. Csajka, “On improving data-link performance
by increasing channel alphabet and introducing sequence decoding,”
in International Symposium on Information Theory (ISIT), Ronneby,
Sweden, June 1976, (Book of abstracts).
[2] G. Ungerboeck, “Channel coding with multilevel/phase signals,” IEEE
Trans. Inf. Theory, vol. 28, no. 1, pp. 55–67, Jan. 1982.
[3] ——, “Trellis-coded modulation with redundant signal sets Part I:
Introduction,” IEEE Commun. Mag., vol. 25, no. 2, pp. 5–11, Feb. 1987.
[4] ——, “Trellis-coded modulation with redundant signal sets Part II: State
of the art,” IEEE Commun. Mag., vol. 25, no. 2, pp. 12–21, Feb. 1987.
[5] E. Biglieri, D. Divsalar, P. J. McLane, and M. K. Simon, Introduction
to Trellis-Coded Modulation with Applications.
Macmillan, 1991.
[6] J. G. Proakis and M. Salehi, Digital Communications, 5th ed. McGraw-
Hill, 2008.
[7] S. Lin and D. J. Costello, Jr., Error Control Coding, 2nd ed. Englewood
Cliffs, NJ: Prentice Hall, 2004.
[8] E. Zehavi, “8-PSK trellis codes for a Rayleigh channel,” IEEE Trans.
Commun., vol. 40, no. 3, pp. 873–884, May 1992.
[9] G. Caire, G. Taricco, and E. Biglieri, “Bit-interleaved coded modula-
tion,” IEEE Trans. Inf. Theory, vol. 44, no. 3, pp. 927–946, May 1998.
[10] A. Guill´en i F`abregas, A. Martinez, and G. Caire, “Bit-interleaved
coded modulation,” Foundations and Trends in Communications and
Information Theory, vol. 5, no. 1–2, pp. 1–153, 2008.
[11] F. Gray, “Pulse code communications,” U. S. Patent 2 632 058, Mar.
1953.
[12] E. Agrell, J. Lassing, E. G. Str¨om, and T. Ottosson, “On the optimality
of the binary reﬂected Gray code,” IEEE Trans. Inf. Theory, vol. 50,
no. 12, pp. 3170–3182, Dec. 2004.
[13] A. Alvarado, F. Br¨annstr¨om, and E. Agrell, “High SNR bounds for the
BICM capacity,” in IEEE Information Theory Workshop (ITW), Paraty,
Brazil, Oct. 2011.
[14] J.-J. Chang, D.-J. Hwang, and M.-C. Lin, “Some extended results on the
search for good convolutional codes,” IEEE Trans. Inf. Theory, vol. 43,
no. 6, pp. 1682–1697, Sep. 1997.
[15] I. E. Bocharova and B. D. Kudryashov, “Rational rate punctured
convolutional codes for soft-decision Viterbi decoding,” IEEE Trans.
Inf. Theory, vol. 43, no. 4, pp. 1305–1313, July 1997.
[16] P. Frenger, P. Orten, and T. Ottosson, “Convolutional codes with op-
timum distance spectrum,” IEEE Trans. Commun., vol. 3, no. 11, pp.
317–319, Nov. 1999.
[17] C. Stierstorfer, R. F. H. Fischer, and J. B. Huber, “Optimizing BICM
with convolutional codes for transmission over the AWGN channel,” in
International Zurich Seminar on Communications, Zurich, Switzerland,
Mar. 2010.
[18] A. Alvarado, L. Szczecinski, and E. Agrell, “On BICM receivers for
TCM transmission,” IEEE Trans. Commun., vol. 59, no. 10, pp. 2692–
2702, Oct. 2011.
[19] R. F. H. Fischer, private communication, Jan. 2011.
[20] W. Zhang, “Finite state systems in mobile communications,” Ph.D.
dissertation, University of South Australia, Adelaide, Australia, Feb.
1996.
[21] W. Zhang, C. Schlegel, and P. Alexander, “The bit error rate reduction
for systematic 8PSK trellis codes by a Gray scrambler,” in IEEE
International Conference on Universal Wireless Access, Melbourne,
Australia, Apr. 1994.
[22] P. K. Gray, “Serially concatenated trellis coded modulation,” Ph.D.


## Page 12


Preprint, September 17, 2018.
12
dissertation, University of South Australia, Adelaide, Australia, Mar.
1999.
[23] C. B. Schlegel and L. C. Perez, Trellis and Turbo Coding, 1st ed.
John
Wiley & Sons, 2004.
[24] J. B. Barry, E. A. Lee, and D. G. Messerschmitt, Digital Communication,
3rd ed.
Springer, 2004.
[25] J. Du and M. Kasahara, “Improvements of the information-bit error rate
of trellis code modulation systems,” The Transactions of the IEICE, vol.
E 72, no. 5, pp. 609–614, May 1989.
[26] G. C. Clark, Jr. and J. B. Cain, Error-correction coding for digital
communications, 2nd ed.
Plenum Press, 1981.
[27] A. J. Viterbi, J. K. Wolf, E. Zehavi, and R. Padovani, “A pragmatic
approach to trellis-coded modulation,” IEEE Commun. Mag., vol. 27,
no. 7, pp. 11–19, July 1989.
[28] R. D. Wesel, X. Liu, J. M. Ciofﬁ, and C. Komninakis, “Constellation
labeling for linear encoders,” IEEE Trans. Inf. Theory, vol. 47, no. 6,
pp. 2417–2431, Sep. 2001.
[29] R. D. Wesel, private communication, July 2012.
[30] P. Knagenhjelm and E. Agrell, “The Hadamard transform—a tool for
index assignment,” IEEE Trans. Inf. Theory, vol. 42, no. 4, pp. 1139–
1151, July 1996.
[31] S. Benedetto and E. Biglieri, Principles of Digital Transmission with
Wireless Applications.
Kluwer Academic, 1999.
[32] X. Li, A. Chindapol, and J. A. Ritcey, “Bit-interlaved coded modulation
with iterative decoding and 8PSK signaling,” IEEE Trans. Commun.,
vol. 50, no. 6, pp. 1250–1257, Aug. 2002.
[33] N. H. Tran and H. H. Nguyen, “Signal mappings of 8-ary constellations
for bit interleaved coded modulation with iterative decoding,” IEEE
Trans. Broadcast., vol. 52, no. 1, pp. 92–99, Mar. 2006.
[34] S. Benedetto, M. A. Marsan, G. Albertengo, and E. Giachin, “Combined
coding and modulation: Theory and applications,” IEEE Trans. Inf.
Theory, vol. 34, no. 2, pp. 223–236, Mar. 1988.
[35] G. Birkhoff and S. Mac Lane, A Survey of Modern Algebra, 4th ed.
New York: Macmillan, 1977.
[36] P. F. Duvall, Jr. and P. W. Harley, III, “A note on counting matrices,”
SIAM Journal on Applied Mathematics, vol. 20, no. 3, pp. 374–377,
May 1971.
[37] A. R. Calderbank and N. J. A. Sloane, “New trellis codes based on
lattices and cosets,” IEEE Trans. Inf. Theory, vol. IT-33, no. 2, pp. 177–
195, Mar. 1987.
[38] E. Zehavi and J. K. Wolf, “On the performance evaluation of trellis
codes,” IEEE Trans. Inf. Theory, vol. IT-33, no. 2, pp. 196–202, Mar.
1987.
[39] G. Caire and E. Viterbo, “Upper bound on the frame error probability
of terminated trellis codes,” IEEE Commun. Lett., vol. 2, no. 1, pp. 2–4,
Jan. 1998.
[40] N. Sone, M. Mohri, M. Morii, and H. Sasano, “On good convolutional
codes with optimal free distance for rates 1/2, 1/3 and 1/4,” IEICE Trans.
Commun., vol. E84-B, no. 1, pp. 116–119, Jan. 2001.
[41] F. Hug, “Codes on graphs and more,” Ph.D. dissertation, Lund Univer-
sity, Lund, Sweden, May 2012.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
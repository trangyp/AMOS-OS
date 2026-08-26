---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1912.10074v1
source: arxiv
tags: [arxiv, knowledge, math, quantum, reference]
---
# 1912.10074v1_Trellis-Coded_Non-Orthogonal_Multiple_Access

> Source: 1912.10074v1_Trellis-Coded_Non-Orthogonal_Multiple_Access.pdf

> Pages: 5

---


## Page 1


arXiv:1912.10074v1  [cs.IT]  20 Dec 2019
1
Trellis-Coded Non-Orthogonal Multiple Access
Xun Zou, Student Member, IEEE, Mehdi Ganji, Student Member, IEEE, and Hamid Jafarkhani, Fellow, IEEE
Abstract—In this letter, we propose a trellis-coded non-
orthogonal multiple access (NOMA) scheme. The signals for dif-
ferent users are produced by trellis coded modulation (TCM) and
then superimposed on different power levels. By interpreting the
encoding process via the tensor product of trellises, we introduce
a joint detection method based on the Viterbi algorithm. Then, we
determine the optimal power allocation between the two users
by maximizing the free distance of the tensor product trellis.
Finally, we manifest that the trellis-coded NOMA outperforms
the uncoded NOMA at high signal-to-noise ratio (SNR).
Index Terms—Non-orthogonal multiple access, trellis coded
modulation, superposition coding.
I. INTRODUCTION
Non-orthogonal multiple access (NOMA) is envisaged as
one of the potential technologies in the next generation
wireless communication systems. Users in NOMA systems
can share the non-orthogonal resources, e.g., the frequency
spectrum and the time slot. From a uniﬁed perspective,
NOMA consists of code-domain NOMA and power-domain
NOMA [1].
Both code-domain and power-domain NOMA have been
extensively studied in the existing literature. In the power-
domain NOMA systems, the signals of different users are
assigned different powers. Then, one major challenge is the
optimal power allocation as discussed, for example, in [2, 3].
The optimal power can be determined according to the channel
conditions to maximize users’ achievable rates. Superposi-
tion coding and successive interference cancellation (SIC)
techniques are utilized at the transmitter and the receiver,
respectively. Again, there are many studies on how to perform
these techniques efﬁciently, for example [4, 5].
The code-domain NOMA has its origin in code divi-
sion multiple access (CDMA), including sparse code mul-
tiple access (SCMA) [6] and trellis coded multiple access
(TCMA) [7]. The signals of multiple users are separated by
user-speciﬁc features, e.g., the uniquely assigned codeword of
each user. In the code-domain NOMA, the main efforts are
devoted to the multi-user detection, for example, the design
of multidimensional constellations [6, 8]. To the best of our
knowledge, the joint design of the code-domain and power-
domain NOMA has never been studied.
In this work, we apply trellis coded modulation (TCM) to
the power-domain NOMA, taking advantages of the coding
gain and the power optimization. Utilizing superposition cod-
ing, the signals for multiple users are superimposed on differ-
ent power levels. Compared with [8], the main contribution of
this work is introducing the power allocation to code-domain
This work was supported in part by the NSF Award CCF-1526780. The au-
thors are with the Center for Pervasive Communications and Computing, De-
partment of Electrical Engineering and Computer Science, University of Cal-
ifornia, Irvine, CA, 92697 USA (email: {xzou4, mganji, hamidj}@uci.edu).
NOMA. The performance can be improved by allocating
proper powers to the signals of different users. Instead of
utilizing TCM purely for codeword design in [8], TCM is
employed in this work to jointly optimize the error control
coding and modulation. Therefore, the Viterbi algorithm can
be directly applied to the proposed scheme. By interpreting the
modulating process via the tensor product of trellises [9, 10],
we implement the maximum likelihood sequence detection
(MLSD) based on the Viterbi algorithm [11]. Furthermore,
we derive the optimal power allocation between the two users
by maximizing the free distance of the tensor product trellis.
The key difference between the trellis-coded NOMA and
the traditional TCMA lies in the multiple access scheme.
In TCMA, the signals of multiple users are differentiated
by their unique features, for example, convolutional encoder,
constellation, or interleaver [12]. However, in the trellis-coded
NOMA, the signals are differentiated only by the power levels.
Furthermore, for the ﬁrst time, we provide insight into the
power optimization for the superimposed TCM signals.
II. SYSTEM MODEL
In this letter, we consider a downlink NOMA system con-
sisting of one base station (BS) and two users. Superposition
coding is employed at the transmitter. The power allocated
to User i’s signal is denoted as Pi, i = 1, 2. The channel
coefﬁcient between the BS and User i is represented by hi.
We adopt the block fading channel model, i.e., the channel
remains static within each block and changes independently
from one block to another [2, 3]. We assume that the channel
state information is perfectly known by the BS and users.
Without loss of generality, we assume that |h1|2 > |h2|2.
To stipulate the user fairness, we set P2 > P1. In what
follows, the 8-phase-shift keying (PSK) 4-state TCM serves
as an example of TCM [13], which is depicted in Fig. 1. The
trellis diagram and the 8-PSK mapping are shown in Figs. 2
(a) and (b), respectively. In Figs. 1 and 2, x1 and x2 represent
the uncoded bits while z0 and z1 denote the coded bits via the
convolutional encoder. For the sake of brevity, we employ the
signal constellation with unit signal power, i.e., Eb = 1. Note
that the proposed scheme can be applied to the case where
two users employ different modulations/trellises and also the
case of more than two users.
In the proposed trellis-coded NOMA, the signals for Users 1
and 2 are ﬁrst modulated by TCM, as shown in Figs. 1 and
2, and then superimposed on different power levels. Using
superposition coding, the nth transmitted symbol at the BS
is given by √P1a1(n) + √P2a2(n) where ai(n) is the nth
symbol for User i after TCM. Then, the nth received sample
at User i is given by
yi(n) = hi
hp
P1a1(n) +
p
P2a2(n)
i
+ wi(n),
(1)


## Page 2


2
T
T
x2(n)
x1(n)
x2(n)
z1(n)
z0(n)
s1(n)
s0(n)
Signal 
Mapping
a(n)
Fig. 1: Illustration of an 8-PSK 4-state TCM encoder.
00/000
10/100
00/001
10/101
x2x1/x2z1z0
s1s0
00
01
10
11
Time n
Time n+1
000
001
010
011
100
101
111
110
(a)
(b)
1
Fig. 2: (a) Trellis representation of 8-PSK 4-state TCM. (b) The
mapping of 8-PSK constellation.
where wi(n) ∼CN(0, σ2
i ) is the additive noise. At users,
the modulated symbols are detected and then the binary
information bits are recovered from the modulated symbols,
which will be explained in the next section.
III. TENSOR PRODUCT OF TRELLISES AND DETECTION
DESIGN
In this section, we ﬁrst present the separate detection
method with SIC. Then, we propose the joint detection method
based on a novel trellis structure known as “tensor product of
trellises”.
A. Separate Detection with SIC
In the separate detection scheme, the signals for Users 1
and 2 are detected separately. User 2 (the weak user) detects
its own signal by considering User 1’s signal as noise. User 1
(the strong user) utilizes SIC, i.e., ﬁrst detects User 2’s signal,
removes it from the superimposed signal, and then detects
its own signal. The Viterbi algorithm [11] can be employed
to determine the sequence with the minimum Euclidean dis-
tance from the received sequence using the 4-state trellis in
Fig. 2 (a).
B. Joint Detection with Tensor Product of Trellises
First, we review the concept of the tensor product of
trellises [9, 10]. Let us consider trellises T1 and T2 with r1
and r2 states, respectively, and S(l)
i , i = 1, · · · , rl, denotes the
ith state of Tl. The tensor product of T1 and T2, denoted as
T1 ⊗T2, can be represented as a trellis with r1 × r2 states.
Each state in T1 ⊗T2 is given by S(1)
i
S(2)
j
, i = 1, · · · , r1,
j = 1, · · · , r2. The state transition from S(1)
i
S(2)
j
to S(1)
k S(2)
l
exists if and only if there exist transitions from S(1)
i
to S(1)
k
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
S(1)S(2)
Fig. 3: Underlying tensor product of trellises.
in T1 and from S(2)
j
to S(2)
l
in T2. One can easily extend the
deﬁnition of the tensor product trellis to the case of more than
two trellises.
Let us revisit the modulating process of two users’ signals
in Section II. The symbols for Users 1 and 2 are modulated
independently through the 4-state trellis, shown in Fig. 2 (a).
Let T1 and T2 stand for the trellises employed to modulate the
symbols for Users 1 and 2, respectively. The tensor product
trellis T1 ⊗T2 is the 16-state trellis in Fig. 3. Every pair of
state transitions in T1 and T2 can be represented by a unique
transition path in T1 ⊗T2. For example, let us assume that the
state of T1 transits from S(1)
i
to S(1)
k
producing the modulated
symbol a1 and the state of T2 transits from S(2)
j
to S(2)
l
generating the modulated symbol a2. From the perspective
of T1 ⊗T2, the state transits from S(1)
i
S(2)
j
to S(1)
k S(2)
l
and
the superimposed symbol √P1a1 +√P2a2 is produced. Since
every state transition can be realized by two parallel paths in
T1 and T2, as shown in Fig. 2 (a), every state transition in
T1 ⊗T2 includes 2 × 2 = 4 parallel paths.
The description of the tensor product trellis demonstrates the
equivalence of the trellis-coded NOMA and the TCM using
the tensor product trellis. The joint detection is to detect both
users’ signals jointly by treating the trellis-coded NOMA as
a regular TCM with the tensor product trellis. In the joint
detection, the Viterbi algorithm is implemented using the
tensor product trellis. It is worth mentioning that there is no
necessity to modulate the signals for Users 1 and 2 jointly
using the tensor product trellis at the transmitter. The trans-
mitted symbols for each user can be modulated independently
according to its own trellis by applying an appropriate power
allocation scheme to ensure a good decoding performance (as
shown in Section V).
Since the Viterbi algorithm can be employed in joint de-
coding, the computational complexity increases linearly with


## Page 3


3
the number of decoded symbols, N. More speciﬁcally, if the
number of states in Ti (i = 1, 2) is Ki and the total number
of edges in Ti is Li, the computational complexity of the
joint detection method is given by O(N(K1K2 + L1L2))
while that of the separate detection method with SIC is
O(N(K1 + K2 + L1 + L2)).
IV. POWER OPTIMIZATION
In this section, we study the power allocation to optimize
the performance of the joint detection scheme. The power
allocation is optimized under two power constraints. One is
the sum power constraint, i.e., P1 + P2 ≤P where P is
the total transmit power. The other constraint is P1 < P2
which is added with no loss of generality. We adopt the
free distance of the tensor product trellis, dfree, to measure
the performance, which is widely used in the existing TCM
studies, for example [14]. A larger free distance results in
a better performance at high signal-to-noise ratio (SNR). As
will be illustrated later, the free distance is a function of the
power coefﬁcients P1 and P2. We obtain the optimal powers
by maximizing the free distance.
The
free
distance
is
deﬁned
as
the
minimum
Eu-
clidean distance between any pair of valid and distinct
sequences
produced
by
a
given
trellis,
i.e.,
dfree
=
arg mina1,a2∈V,a1̸=a2 ||a1−a2|| where V is the set of all valid
sequences. The free distance can be determined by choosing
the minimum of two candidates: the minimum Euclidean
distance between the symbols produced by the parallel paths,
i.e., dparallel, and that between the sequences which diverge
from the same state and then merge at the same state, i.e.,
dD&M. The subscript D&M is the acronym for “diverging and
merging”. In what follows, we analyze these two distances
separately. Assume that there are two different paths in T1⊗T2
producing √P1u1 + √P2v1 and √P1u2 + √P2v2, where u1
and u2 are the modulated symbols of T1 and v1 and v2 are
those of T2.
A. Parallel Paths
First, we study the case where √P1u1 + √P2v1 and
√P1u2+√P2v2 are produced by the parallel paths in T1⊗T2.
Fig. 4 illustrates the possible positions of √P1u1 + √P2v1
and √P1u2 + √P2v2 in the superimposed constellation when
v1 and v2 are chosen from {1, −1}. Because of symmetry,
the minimum Euclidean distance for all the other choices will
be the same. In Fig. 4, there are four different markers, hol-
low/solid square/circle. The superimposed symbols depicted
by the same marker are the symbols produced by the parallel
paths for a speciﬁc state transition in T1 ⊗T2. Every state
transition in T1 ⊗T2 can be realized by four parallel paths.
Therefore, there are four positions for every marker. The
minimum Euclidean distance between parallel paths can be
found by calculating the Euclidean distance between the points
sharing the same marker. It is clear from Fig. 4 that the
minimum Euclidean distance is either δ1 or δ2. Thus,
dparallel=min {δ1, δ2}=min
n
2
p
P2−2
p
P1, 2
p
P1
o
. (2)
Fig. 4: Illustration of the minimum Euclidean distance in the super-
imposed constellation.
0000
0000
1100
1100
1000
1001
0100
0110
ddiverge
dmerge
dmid
Fig. 5: Illustration of the diverging-and-merging paths with the
minimum Euclidean distance.
B. Diverging-and-Merging Paths
Second, we study the Euclidean distance between the se-
quences which diverge from the same state and then merge
at the same state. It can be shown that if two sequences
diverge from any state, it takes at least three transitions to
merge at the same state. We utilize the exhaustive search to
ﬁnd a pair of sequences with the minimum Euclidean distance
among all pairs of distinct sequences, which is shown in
Fig. 5. Note that all valid codewords start and end at state
zero. However, any common sub-sequence will not contribute
to dfree. Therefore, to calculate dfree in Fig. 5, we need to
consider the state transitions 1100 →1000 →0100 →1100
and 1100 →1001 →0110 →1100. As shown in Fig. 5,
the squared Euclidean distance between the diverging-and-
merging paths is given by
d2
D&M = d2
diverge + d2
mid + d2
merge.
(3)
First, let us focus on the diverging paths in Fig. 5. Ac-
cording to Fig. 2, the superimposed symbol produced by the
path 1100 →1000 is given by √P1u1 + √P2v1, where
u1 ∈{ej3π/4, ej7π/4} and v1 ∈{1, −1}. Similarly, the
superimposed symbol produced by 1100 →1001 is given
by √P1u2 + √P2v2, where u2 ∈{ej3π/4, ej7π/4} and v2 ∈
{ejπ/2, ej3π/2}. The positions of the superimposed symbols
can be shown in Fig. 6. The minimum Euclidean distance
between the diverging paths is given by
ddiverge = δ3 = |
p
2P2 −2
p
P1|.
One can employ the same approach to derive the minimum
Euclidean distance between the merging paths and ﬁnd that
dmerge = ddiverge.
Second, we investigate the Euclidean distance dmid in
Fig. 5. The superimposed symbol produced by the path
1000 →0100 is given by √P1u1 + √P2v1, where u1 ∈
{1, −1} and v1 ∈{1, −1}. Similarly, the superimposed sym-
bol produced by the path 1001 →0110 is given by √P1u2 +
√P2v2, where u2 ∈{1, −1} and v2 ∈{ejπ/4, ej5π/4}. The
positions of the superimposed symbols can be shown in Fig. 7.


## Page 4


4
1100- > 001
1100 1000
Fig. 6: Illustration of the minimum Euclidean distance between the
symbols produced by diverging paths.
1001->0110
1000->0100
Fig. 7: Illustration of the minimum Euclidean distance between the
symbols in the intermediate stage of the diverging-and-merging paths.
According to Fig. 7, the minimum Euclidean distance dmid is
given by
d2
mid = min{δ2
4, δ2
5}
= (2−
√
2)P2 + min
n
0, 4P1 + 2
p
P1P2
√
2 −2
o
.
To summarize, the minimum Euclidean distance between
the diverging-and-merging paths is given by
d2
D&M =d2
diverge + d2
mid + d2
merge
=

6 −
√
2

P2 + 8P1 −8
p
2P1P2
+ min
n
0, 4P1 + 2
p
P1P2
√
2 −2
o
.
(4)
C. Free Distance
The free distance of T1 ⊗T2 is determined by ﬁnding the
minimum of dparallel and dD&M, i.e.,
d2
free = min{d2
parallel, d2
D&M}
= min

4P1,4
p
P2 −
p
P1
2
,

6 −
√
2

P2 + 8P1
−8
p
2P1P2+min
n
0,4P1+2
p
P1P2
√
2−2
oo
. (5)
The optimal powers can be derived by maximizing the free
distance, i.e.,
[P ∗
1 , P ∗
2 ] = arg max
P1,P2 d2
free, s.t. P1 + P2 ≤P,
(6)
where P is the total transmit power. According to (5),
one can derive that dfree is maximized when 4P1
=
6
8
10
12
14
16
18
SNR (dB)
10-8
10-6
10-4
10-2
100
BER
Fig. 8: BER vs. SNR for TCMA, uncoded and trellis-coded NOMA
when P1 = 0.1, P2 = 1, |h1|2 = 2, |h2|2 = 1.
 6 −
√
2

P2 + 8P1 −8√2P1P2, which then results in P ∗
1
P ∗
2 =

2
√
2−√
2+
√
2
2
2
≈0.2404. Besides, to combat the channel
noise, P1 + P2 should be maximized. As a result, P ∗
1
=
0.2404
1+0.2404P ≈0.1938P and P ∗
2 ≈0.8062P.
While we presented the results for a two-user scenario with
8-PSK 4-state TCM, our approach can be generalized to any
TCM.
V. SIMULATION RESULTS
In this section, we present the simulation results of the 8-
PSK 4-state trellis-coded NOMA (TC-NOMA), TCMA, and
the uncoded NOMA (UC-NOMA) with 4-PSK. We ensure
a fair comparison among these schemes since the TCM is
implemented without consuming extra bandwidth compared
with the uncoded modulation [13]. In our simulation, we
employ bit error ratio (BER) as the measure of performance.
In the uncoded NOMA, the maximum likelihood detection is
employed. We also present the results for the TCMA where
the signals for Users 1 and 2 are modulated by the identical
trellis shown in Fig. 2 but differentiated by constellation [7].
In TCMA, the constellation used by one user is the other
user’s constellation rotated by π/8. In contrast to the trellis-
coded NOMA, the transmitted signal in TCMA is given by
p
(P1 + P2) /2[a1(n) + a2(n)], which ensures a fair compar-
ison by using the same sum transmit power.
First, we show the BER as a function of SNR for NOMA
and TCMA schemes in Figs. 8 and 9 when P2 = 1 and
P1 = 0.1 or 0.3, respectively. SNR is given by
1
σ2 where σ2
is the variance of noise. For P1 = 0.1 or 0.3, it is manifested
that at high-SNR, similar to conventional TCM [13], the
trellis-coded NOMA using the joint detection outperforms the
uncoded NOMA. Besides, the trellis-coded NOMA using the
separate detection achieves a similar performance to that using
the joint detection when P1 = 0.1. In contrast, there is a
huge gap between the BER curves of the separate detection
and those of the joint detection when P1 = 0.3. This is be-
cause of the severe inter-user interference when detecting two


## Page 5


5
6
8
10
12
14
16
SNR (dB)
10-8
10-6
10-4
10-2
100
BER
Fig. 9: BER vs. SNR for TCMA, uncoded and trellis-coded NOMA
when P1 = 0.3, P2 = 1, |h1|2 = 2, |h2|2 = 1.
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
10-6
10-4
10-2
100
BER
UC-NOMA, 4-state, 18dB
TC-NOMA, 4-state, 18dB
TCMA, 4-state, 18dB
UC-NOMA, 4-state, 16dB
TC-NOMA, 4-state, 16dB
TCMA, 4-state, 16dB
TC-NOMA, 8-state, 18dB
TC-NOMA, 8-state, 16dB
SNR=16dB
SNR=18dB
Fig. 10: BER vs. P1/P2 for TCMA, uncoded and trellis-coded
NOMA schemes at users employing the joint detection when P1 +
P2 = 1.
user’s signals separately and the error propagation problem in
SIC. Furthermore, using the joint detection, the trellis-coded
NOMA outperforms TCMA at high-SNR in Figs. 8 and 9.
Moreover, in the trellis-coded NOMA, the signals of different
users can also employ different constellations. The curves
with “TC-NOMA, Joint, Rotate” in Fig. 9 are for the case
where the constellation used by one user is the other user’s
constellation rotated by π/8. The trellis-coded NOMA with
constellation rotation achieves a better performance compared
with the trellis-coded or uncoded NOMA without constellation
rotation and TCMA. It can be explained intuitively by con-
sidering how the constellation rotation affects the Euclidean
distance between superimposed symbols. According to Figs. 4
and 6, the minimum Euclidean distance may increase if the
constellation of User 1’s signal rotates by π/8, which then
improves the performance.
Fig. 10 shows how the average BER changes with the power
ratio P1/P2 using the joint detection at SNRs 16dB and 18dB
for the 4-state trellis in Fig. 2 and the 8-state trellis in Fig. 12.8
of [14]. It is shown that the minimum BER is achieved when
P1/P2 ≈0.25 for the uncoded NOMA and the 8-state trellis-
coded NOMA. The optimal power ratio for the 4-state trellis-
coded NOMA is 0.24 for SNR=16dB and 0.22 for SNR=18dB,
which are close to the optimal power ratio of 0.2404 derived
in Section IV. Moreover, the trellis-coded NOMA in its best
case scenario outperforms the uncoded NOMA in its best case
scenario. Besides, the performance of TCMA does not change
with P1/P2. By choosing the proper powers, the trellis-coded
NOMA outperforms TCMA.
VI. CONCLUSIONS
In this letter, we study the trellis-coded NOMA and propose
a joint detection method based on the tensor product of
trellises. Besides, we derive the optimal power allocation
between the two users by maximizing the free distance of
the tensor product trellis. Simulation results demonstrate that
the trellis-coded NOMA outperforms the uncoded NOMA and
TCMA using an appropriate power allocation. The study of the
trellis-coded NOMA systems with more than two users is our
future work.
REFERENCES
[1] Q. Wang, R. Zhang, L.-L. Yang, and L. Hanzo, “Non-orthogonal
multiple access: A uniﬁed perspective,” IEEE Wireless Com-
mun., vol. 25, no. 2, pp. 10–16, Apr. 2018.
[2] X. Liu and H. Jafarkhani, “Downlink non-orthogonal multiple
access with limited feedback,” IEEE Trans. Wireless Commun.,
vol. 16, pp. 6151–6164, Sep. 2017.
[3] J. Choi, “Power allocation for max-sum rate and max-min rate
proportional fairness in NOMA,” IEEE Commun. Lett., vol. 20,
no. 10, pp. 2055–2058, Oct. 2016.
[4] S. Vanka, S. Srinivasa, Z. Gong, P. Vizi, K. Stamatiou, and
M. Haenggi, “Superposition coding strategies: Design and ex-
perimental evaluation,” IEEE Trans. Wireless Commun., vol. 11,
no. 7, pp. 2628–2639, Jul. 2012.
[5] R. Zhang and L. Hanzo, “A uniﬁed treatment of superposition
coding aided communications: Theory and practice,” IEEE
Commun. Surveys Tuts., vol. 13, no. 3, pp. 503–520, Third
Quarter 2011.
[6] H. Nikopour and H. Baligh, “Sparse code multiple access,” in
Proc. IEEE PIMRC, London, UK, Sep. 2013, pp. 332–336.
[7] T. Aulin and R. Espineira, “Trellis coded multiple access
(TCMA),” in Proc. IEEE ICC, Vancouver, BC, Canada, Jun.
1999, pp. 1177–1181.
[8] B. Di, L. Song, Y. Li, and G. Y. Li, “TCM-NOMA: Joint multi-
user codeword design and detection in trellis coded modulation
based NOMA for beyond 5G,” IEEE J. Sel. Topics Signal
Process., vol. 13, no. 3, pp. 766–780, Jun. 2019.
[9] H. Jafarkhani and V. Tarokh, “Design of successively reﬁnable
trellis-coded quantizers,” IEEE Trans. Inf. Theory, vol. 45, no. 5,
pp. 1490–1497, Jul. 1999.
[10] ——, “Multiple description trellis-coded quantization,” IEEE
Trans. Commun., vol. 47, no. 6, pp. 799 – 803, Jun. 1999.
[11] A. Viterbi, “Convolutional codes and their performance in
communication systems,” IEEE Trans. Comm. Tech., vol. 19,
no. 5, pp. 751–772, Oct. 1971.
[12] F. Brannstrom, T. M. Aulin, and L. K. Rasmussen, “Iterative de-
tectors for trellis-code multiple-access,” IEEE Trans. Commun.,
vol. 50, no. 9, pp. 1478–1485, Sep. 2002.
[13] G. Ungerboeck, “Trellis-coded modulation with redundant sig-
nal sets part I: Introduction,” IEEE Commun. Mag., vol. 25,
no. 2, pp. 5–11, Feb. 1987.
[14] S. Benedetto and E. Biglieri, Principles of digital transmission:
with wireless applications.
Springer Science & Business
Media, 1999.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1912_10074v1_trellis_coded_non_orthogonal_multiple_access
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2019/1912_10074V1_TRELLIS_CODED_NON_ORTHOGONAL_MULTIPLE_ACCESS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

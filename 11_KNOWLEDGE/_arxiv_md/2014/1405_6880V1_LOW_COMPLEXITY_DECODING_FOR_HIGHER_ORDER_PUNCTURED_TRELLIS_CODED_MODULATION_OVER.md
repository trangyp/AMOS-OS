---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1405.6880v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1405.6880v1_Low_Complexity_Decoding_for_Higher_Order_Punctured_Trellis-Coded_Modulation_Over

> Source: 1405.6880v1_Low_Complexity_Decoding_for_Higher_Order_Punctured_Trellis-Coded_Modulation_Over.pdf

> Pages: 4

---


## Page 1


Low Complexity Decoding for Higher Order
Punctured Trellis-Coded Modulation Over
Intersymbol Interference Channels
Fabian Schuh and Johannes B. Huber
Institute for Information Transmission, Friedrich-Alexander-Universit¨at Erlangen-N¨urnberg, Germany
mail: {schuh, huber}@LNT.de
Abstract—Trellis-coded modulation (TCM) is a power and
bandwidth efﬁcient digital transmission scheme which offers
very low structural delay of the data stream. Classical TCM
uses a signal constellation of twice the cardinality compared
to an uncoded transmission with one bit of redundancy per
PAM symbol, i.e., application of codes with rates
n−1
n
when
2n denotes the cardinality of the signal constellation. Recently
published work allows rate adjustment for TCM by means of
puncturing the convolutional code (CC) on which a TCM scheme
is based on. In this paper it is shown how punctured TCM-signals
transmitted over intersymbol interference (ISI) channels can
favorably be decoded. Signiﬁcant complexity reductions at only
minor performance loss can be achieved by means of reduced
state sequence estimation.
Index Terms—trellis-coded modulation (TCM); punctured con-
volutional codes; Viterbi-Algorithm (VA); reduced state sequence
estimation (RSSE); intersymbol interference (ISI);
I. INTRODUCTION
Ungerboeck’s trellis-coded modulation (TCM) [1], [2] is an
attractive digital transmission scheme when very low structural
delay of the data stream is desired. Low structural latency is
ensured by the use of convolutional codes instead of block
codes (cf. [3]) and the dispense with interleaving (as opposed
to convolutionally bit-interleaved coded modulation [4]). By
expanding a constellation from 2n−1 to 2n signal points and
employing a rate- n−1
n
convolutional encoder one can improve
the robustness of the transmission against noise by up to 6 dB
without any further costs besides computational effort [1].
A recently published paper proposes to perform rate ad-
justment for TCM by means of puncturing the convolutional
code (CC) on which a TCM scheme is based on. There, metric
computations and trellis diagram become time-variant [5], [6].
Here, transmission over an ISI channel is considered which
requires to apply a TCM-ISI super trellis for optimum decod-
ing. As a result, the Viterbi algorithm (VA) has to be extended
in order to handle both coded and uncoded bits in an optimal
way (Please notice, that usual iterative equalization/decoding
here is not possible due to lack of interleaver.).
II. SYSTEM MODEL
This paper deals with convolutionally encoded pulse-
amplitude modulated (PAM) transmission as depicted in Fig. 1.
Here, the term PAM is used for complex-valued signal con-
stellations as well including amplitude-shift keying (ASK),
phase-shift keying (PSK) or quadrature-amplitude modulation
(QAM) A binary data sequence ⟨u⟩is split into nu parallel
uc[l]
C
P
L
A
h[k]
uu[k]
. . .
c[k]
ℓ[k]
nu
nc
nc −1
a[k]
Fig. 1.
System model for punctured trellis-coded modulation (P-TCM) with
nu = 2 and nc = 2.
uncoded sequences uu[k] and nc −1 parallel sequences uc[l]
that are encoded using a rate- nc−1
nc
binary convolutional en-
coder C with generator polynomials gij(D), 1 ≤i ≤nc; 1 ≤
j ≤nc −1 with max. degree ν, delay operator D, nc −1
parallel binary-input symbols and nc parallel output symbols
at each time instant.
At each output of the encoder, the symbols traverse through
a puncturing system with puncturing scheme P = [Pij], Pij ∈
{0, 1} ;
1 < i ≤nc;
1 < j < Ωand period Ω. For
each (nc −1)-tuple of encoder input symbols the puncturing
scheme cyclically advances by one step. Where Pij is zero,
the current symbol at the output is discarded, accordingly.
The punctured nc-ary encoded output symbols c[k] together
with the uncoded input symbols uu[l] form a label ℓ[k] by
which the corresponding signal point out of M = 2nu+nc-
ary constellation is selected. The transmit signal traverses
through a dispersive discrete-time ISI channel modelled by
a FIR-ﬁlter with memory L for L + 1 channel coefﬁcients
h[k], 0 < k < L (i.e., T-spaced sampling after the Whitened
Matched Filter [7]).
III. TRELLIS-BASED DECODING
For sake of simplicity, we use for the following explanations
a simple example, i.e., a rate 1
2 mother code (e.g., nc = 1) and
a memory-1 ISI channel. Fig. 3 illustrates the extension of the
trellis states by the uncoded symbols that are stored in the
ISI channel. The two bars (
gi
) represent the generator
polynomials g1 and g2 which generate the MSB and LSB
of the (punctured) convolutional code (rate- 1
2 mother code).
This notation was introduced in [5], [6]. As the ISI channel
stores the last L transmitted signal points, a super trellis
needs to track not only the coded output of the (punctured)
convolutional encoder but also the L·nu last uncoded symbols.
Thus, for each uncoded symbol and each channel tap (except
for h[0]) an additional binary memory element must be added
arXiv:1405.6880v1  [cs.IT]  27 May 2014


## Page 2


h[0]
h[1]
h[0]
h[1]
h[0]
h[1]
h[0]
h[1]
h[0]
h[1]
T2
T0
T1
T2
T0
k + 5
k + 4
k + 3
k + 2
k + 1
k
k −1
k −2
k −3
k −4
k −5
k −6
Fig. 2.
State transitions of the transmitter FSM with R = 7
3 and the relations
between generator polynomials, FSM-state/input and channel state for a
memory-1 ISI-channel with one uncoded bit stored in the states (crosshatched
block).
due to
puncturing
coded symbol
for h[0]
coded symbol
for h[1]
uncoded symbol
for h[1]
Fig. 3.
Layout of a particular trellis state showing the individual components
of the state (nu = 1, L = 1, ν = 2).
to the FSM, e.g., for nu = 2 and L = 2 a total of 4
additional memory elements have to be spent. As a result,
the joint CC+ISI (super) trellis quickly becomes prohibitively
large. However we will show later that reduced-state sequence-
estimation (RSSE) techniques can be applied here, such that
the computational complexity can be reduced signiﬁcantly
with only minor performance loss.
We ﬁrst brieﬂy consider an algorithm to construct the
trellis of this ﬁnite state machine. In order to achieve optimal
decoding we need to consider the coded and uncoded symbols
in the ﬁnite-state machine as they take part in the memory
of the CC and the ISI channel. However, as the uncoded
symbols directly propagate to the mapper the uncoded symbols
immediately affect the selection of the signal point and thus
the input of the ISI channel.
To algorithmically handle the time-variant mapping we
introduced [5] a set of so-called generator offsets Ti which
describe, depending on the puncturing scheme, modulation
size, and time instant, the relations between generator polyno-
mials, input value, FSM state, and mapping to MSB or LSB,
respectively. For each new generator offset Ti a new trellis
segment arises, e.g., the number of generator offsets equals
the number of trellis segments in one trellis period.
The setup of a trellis representation of CC+ISI is deﬁned by
means of algorithm 1 in an abstract manner. The major steps
are in line 10 and line 11 which fetches the uncoded symbols
from the trellis state and appends it to the encoding results in
order to perform the labeling. Then, L + 1 signal points are
selected and weighted with the channel coefﬁcients in line 13.
The routines GETCURRENTSTATE and GETNEXTSTATE
have to evaluate the current and next state to construct
the trellis as described in detail in [5], [6]. Addition-
ally, we here also have to consider the uncoded symbols
(GETUNCODEDFROMSTATE). The prototype routines for our
Algorithm 1 Building the FSM for P-TCM with nu > 0 over
ISI channels
Require: h ←{h[0], h[1], h[2], . . .}
Require: Z number of states
1: for all s : 1 →Z do
2:
for all u ∈Fnc+nu
2
do
3:
for all i : 1 →Λ do
4:
d ←{u, s0, s1, . . . sZ−1}
5:
s−←GETCURRENTSTATE(d, Ti)
6:
s+ ←GETNEXTSTATE(d, Ti)
7:
for κ : 0 →(length(h) −1) do
8:
e(κ) ←P-ENCODER(Ti, κ, goct, d)
9:
end for
10:
uh ←GETUNCODEDFROMSTATE(u, Ti)
11:
ℓ←LABELING(
(
uh
,
X
κ
e(κ)
)
)
12:
m ←CONSTELLATION(ℓ)
13:
h(Ti, s−, u) ←m⊤· h
▷hypotheses
14:
T(Ti, s−, u) ←s+
▷next state
15:
end for
16:
end for
17: end for
18: function P-ENCODER(Ti, κ, goct, d)
19:
for i ∈{MSB, LSB} do
20:
FIFOi ←shifts according to Ti, and κ
21:
e(i) ←FIFO⊤
i · gi,dual
22:
end for
23: end function
example (P =

(1 1)⊤(0 1)⊤
, ν = 2, L = 1) are given in
algorithm 2 and return the content of the delay elements on
the FIFO according to Fig. 2. Here, counting starts at the most
left elements for each generator offset Ti.
Algorithm 2 Prototype routines for the exemplary rate
7
3
transmission scheme with a memory-2 convolutional code and
the puncturing scheme P =

(1 1)⊤(0 1)⊤
(see Fig. 2.
Additional nu = 1 uncoded bits are used to address the signal
points.
1: function GETCURRENTSTATE(d, Ti)
2:
if i = 0 then return d({3, 4, 5, 6})
3:
else if i = 1 then return d({2, 3, 4, 5})
4:
else if i = 2 then return d({2, 3, 4, 5})
5:
end if
6: end function
7: function GETNEXTSTATE(d, Ti)
8:
if i = 0 then return d({2, 3, 4})
9:
else if i = 1 then return d({1, 2, 3, 4})
10:
else if i = 2 then return d({1, 2, 3, 4})
11:
end if
12: end function
As a result, a matrix of hypotheses h(Ti) and a matrix of
state transitions T(Ti) span a time-variant trellis with 2(nu+nc)


## Page 3


branches per state that can be used to optimally decode
punctured TCM over ISI channels by means of a modiﬁed
Viterbi algorithm. Here, Ti denotes the i-th trellis segment out
of the set of Λ segments. Hence, Λ is nominated as trellis
period. The modiﬁcations necessary for the Viterbi algorithm
comprise two separate path registers for uncoded and coded
symbols. This is due to the differing symbol phases w.r.t. the
puncturing matrix, e.g., differing data speed of uu and uc (cf.,
Fig. 1). The metric computations are described in the next
section.
IV. REDUCED-STATE SEQUENCE ESTIMATION
We will now describe the application of RSSE by recalling
the basic principles of Delayed Decision Feedback Sequence
Estimation [8] (DFSE). We will brieﬂy show the metric
calculations before giving numerical simulation results.
A. State Reduction Techniques (PAM without channel code)
1) DFSE: When equalizing uncoded digital PAM signaling
over a discrete-time ISI channel with L+1 taps using delayed
decision feedback sequence estimation (DFSE), a trellis is
constructed from the ﬁrst ˜L ≤L taps only. Thus, the number
of states is reduced from M L to M ˜L. For ˜L = L DFSE is
equivalent to MLSE decoding via full-state VA. In contrast,
when ˜L = 0, the resulting trellis has a single state and, thus,
represents a decision feedback equalization (DFE). Hence,
DFSE allows an efﬁcient way to trade between full-state VA
and one-state DFE [8]. The remaining L + 1 −˜L channel taps
are considered in a delayed decision-feedback equalization
(DFE) that is performed in each trellis state using the delayed
path register of the corresponding state.
The main difference to full state equalization appears in
the metric computation for each time instant. From eq. (1)
it can be seen that the state speciﬁc path register preg[k, s] is
delayed by ˜L and its elements are multiplied by the subsequent
channel coefﬁcients hdfe[h] which have not been considered in
the trellis. The branch metric λ(s, u) (e.g., Euclidean distance
of the received symbol y[k] to the hypotheses h(s, u) for the
state s and symbols u) thus includes a DFE-term δ:
δ =
X
κ
preg[k −˜L + κ, s] · hdfse[κ]
(1)
λ(s, u) =
y[k] −h(s, u) −δ
2
2) RSSE: In RSSE, on the other hand, Z arbitrary MLSE
states, each with 2nc+nu−1 = M
2 possible branches to adjacent
states, are combined into ZR =
Z
2J ; J ∈N hyperstates [9],
[10] each having 2J substates and 2K ·2J branches. A certain
assignment of states to hyperstates is called partitioning [10].
Instead of having 2K arriving branches at each of the Z
MLSE states we get a set of 2K ·2J branches at each of the ZR
hyperstates. The total number of available branches remains
2K · Z. However, when using RSSE only 2K branches are
possible (i.e., enabled) from each state, at a given time instant.
The availability of branches is determined by the path register
in each state, and is thus a form of decision-feedback.
The main difference of DFSE and RSSE to MLSE is, that
we decide for a surviving path prematurely resulting in a
truncation of error events. A loss in Euclidean distance appears
if an error event with minimum Euclidean distance gets trun-
cated. Therefore the performance of RSSE strongly depends
on the partitioning of the states into hyperstates. However,
survivor-decision speciﬁes the sub-state within a hyperstate
uniquely and thus allows correct metric calculation. Instead of
exhaustively search for the optimum state partitioning, which
maximizes the intra-hyperstate distance [10], we exploit the
minimum phase characteristics of the ISI channel which is, as
described above, fully integrated into our trellis.
For a minimum phase channel impulse response the prior
channel input symbols are weighted fewer than more recent
once and, thus, affect the metric less. Hence, the intra-
hyperstate distance is maximized when states are combined
with respect to elder positions in the state number. This
particular partitioning is equivalent to DFSE for ISI channels
and will be called DFSE partitioning. The minimum phase ISI
channel is the last element to affect the received symbols and
is also fully integrated into the FSM. Thus we can apply the
DFSE partitioning to use RSSE for punctured TCM (P-TCM)
over ISI channels.
B. Implementation Issues
Algorithm 3 Metric calculations for total RSSE – Jth partition
1: qc ←log2(nr. hyperstates)
2: for all s ∈S do
3:
for all u ∈A · K do
4:
for all κ = 0 →J −1 do
▷active branches
5:
if κ ≤L then
6:
ζ[κ] = preg,uncoded(Ltraceback −L + κ, s)
7:
else
8:
ζ[κ] = preg,coded(Ltraceback −L −qc + κ, s)
9:
end if
10:
end for
11:
λ(ζ, u) ←Γ(ζ) +
y[k] −h(ζ, u)
2
12:
end for
13: end for
Most importantly, in terms of implementation, we need
to distinguish between two path registers, namely one for
the uncoded symbols prec,uncoded, that pass through the ISI
channel only, and one for the coded symbols preg,coded. Hence,
when performing the feedback in RSSE both registers need to
be considered, depending on the partition depth J. Algorithm 3
shows the application of both path registers in order to select
the available paths by means of an indicator variable ζ which
speciﬁes the active branches by means of decision-feedback.
C. Numerical Results
Numerical result of a computer simulation of a transmission
scheme with the following parameters are given. The total
transmission rate is
7
3 with a memory-2 convolutional code
with generator polynomials [7, 3]8 and the puncturing scheme
P =

(1 1)⊤(0 1)⊤
. To increase the transmission rate
from
4
3 to
7
3 additional nu = 1 uncoded bits are used to


## Page 4


6
8
10
12
14
16
18
20
10−4
10−3
10−2
10−1
100
10 log10

Eb
N0

in dB
BER
hard decision
soft decision
RSSE (32)
RSSE (64)
RSSE (256)
full-state VA (2048)
10
12
14
16
18
20
22
25
27
29
211
BER = 10−3
10 log10

Eb
N0

in dB
Complexity
Fig. 4.
BER Performance and computational decoder complexity for a rate 7
3 transmission scheme with a memory-2 convolutional code ([7, 3]8) and the
puncturing scheme P =

(1 1)⊤(0 1)⊤
. Additional nu = 1 uncoded bits are used to address the signal points and the ISI channel has memory L = 2.
address a signal points from an 8-ASK constellation (cf.,
Fig. 5). Additionally, square QAM constellations may be built
from two independent ASK constellations in in-phase and
quadrature component to further increase transmission rate
without increasing the signal bandwidth. Thus, for all usual
PAM constellations P-TCM is favorably based on the one-
dimensional 4-ASK constellation because ﬁne tuning of the
transmission rate is possible by means of puncturing and
addition of uncoded bits. The transmit signal traverses through
an ISI channel h[κ] with memory L = 2 plus additive white
Gaussian noise.
uc[l]
C
P
8-ASK
h[k]
uu[k]
+
n[k]
a[k]
Fig. 5.
System model for punctured trellis-coded modulation (P-TCM) with
nu = 1 and nc = 2.
We use the following unit energy channel h[κ]:
hlin[κ] = L −κ + 1
L + 1
for 0 ≤κ ≤L
h[κ] =
1
rP
γ
|hlin[γ]|2 hlin[κ]
Figure 4 shows bit error rates versus
Eb
N0 from simula-
tions. We compare the results of our proposed approach with
separated equalization and decoding using BCJR and DFSE
for soft-/hard equalization of the ISI and a full-state VA for
decoding of the CC. Note that, due to the objective of very
low structural delay of the data stream no interleaver is appli-
cable and thus no iterative equalization-decoding procedure
is possible. Clearly, the proposed scheme outperforms the
separated approaches by several decibels. However, the full-
state trellis complexity number1 is 2048 and thus signiﬁcantly
higher when compared to the separated approaches. Hence we
reduce the computational complexity by sacriﬁcing optimality
by reduced-state sequence estimation (RSSE). By this, we
can reduce the complexity number from 2048 down to 256
without noticeable loss in performance. When further reduc-
ing to a complexity number of 64 the performance is still
1The computation trellis complexity number is deﬁned as the number of
metric calculations per information bit.
slightly better as the soft-equalization and decoding approach,
although the latter has a complexity number of roughly 1369.
Computational complexity1 over Eb
N0 that is required to achieve
a bit error probability of less than 10−3 is shown in Fig. 5.
Obviously our approach allows to reduce the complexity to 26
and still outperforms the separate soft-equalization/decoding
approach.
V. CONCLUSION
It has been shown that maximum-likelihood decoding for
punctured TCM can be achieved with low computational
complexity and very good performance even for transmission
over ISI channels. Thus, punctured TCM can be applied as a
low-latency transmission scheme with high spectral efﬁciency.
An additional beneﬁt is the improved ﬂexibility in transmission
rate due to the ﬂexible choice of the puncturing scheme, in
contrast to classical TCM which can only achieve integer
rates.
REFERENCES
[1] G. Ungerboeck, “Channel coding with multilevel/phase signals,” IEEE
Transactions on Information Theory, vol. IT-28, no. 1, pp. 55 – 67, jan
1982.
[2] ——, “Trellis-coded modulation with redundant signal sets; part i:
Introduction; part ii: State of the art,” Communications Magazine, IEEE,
vol. 25, no. 2, pp. 5 –21, February 1987.
[3] T. Hehn and J. B. Huber, “LDPC Codes and Convolutional Codes
with Equal Structural Delay: A Comparison,” IEEE Transactions on
Communications, vol. 57, no. 6, pp. 1683–1692, June 2009. [Online].
Available: http://www.lit.lnt.de/papers/tr com 2009 hehn.pdf
[4] E. Zehavi, “8-PSK Trellis Codes for a Rayleigh Channel,” IEEE Trans-
actions on Communications, vol. 40, no. 5, pp. 873 –884, may 1992.
[5] F. Schuh and J. Huber, “Low Complexity Decoding for Punctured
Trellis-Coded Modulation over Intersymbol Interference Channels,” in
accepted for 2014 International Zurich Seminar on Communications,
Feb. 2014.
[6] F. Schuh, A. Schenk, and J. Huber, “Punctured Trellis-Coded Modula-
tion,” in submitted to ICC 2014, Jun. 2014.
[7] J. Forney, G., “Maximum-likelihood Sequence Estimation of Digital
Sequences in the Presence of Intersymbol Interference,” IEEE Trans.
Inf. Theory, vol. 18, no. 3, pp. 363–378, 1972.
[8] A. Duel-Hallen and C. Heegard, “Delayed Decision-Feedback Sequence
Estimation,” IEEE Trans. Commun., vol. 37, no. 5, pp. 428–436, May
1989.
[9] J. Huber, Trelliscodierung: Grundlagen und Anwendungen in der digi-
talen ¨Ubertragungstechnik.
Springer, 1992.
[10] B. Spinnler and J. Huber, “Design of Hyper States for Reduced-State
Sequence Estimation,” in Proc. IEEE Int. Conf. Communications ICC
’95 Seattle, vol. 1, 1995, pp. 1–6.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
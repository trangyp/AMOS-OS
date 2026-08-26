---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1312.1482v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1312.1482v1_Low_Complexity_Decoding_for_Punctured_Trellis-Coded_Modulation_Over_Intersymbol_

> Source: 1312.1482v1_Low_Complexity_Decoding_for_Punctured_Trellis-Coded_Modulation_Over_Intersymbol_.pdf

> Pages: 4

---


## Page 1


1
Low Complexity Decoding for Punctured
Trellis-Coded Modulation Over Intersymbol
Interference Channels
Fabian Schuh and Johannes B. Huber
Institute for Information Transmission, Friedrich-Alexander-Universit¨at Erlangen-N¨urnberg, Germany
mail: {schuh, huber}@LNT.de
Abstract—Classical trellis-coded modulation (TCM) as intro-
duced by Ungerboeck in 1976/1983 uses a signal constellation of
twice the cardinality compared to an uncoded transmission with
one bit of redundancy per PAM symbol, i.e., application of codes
with rates
n−1
n
when 2n denotes the cardinality of the signal
constellation. The original approach therefore only comprises
integer transmission rates, i.e., R = {2, 3, 4 . . .}, additionally,
when transmitting over an intersymbol interference (ISI) channel
an optimum decoding scheme would perform equalization and
decoding of the channel code jointly.
In this paper, we allow rate adjustment for TCM by means of
puncturing the convolutional code (CC) on which a TCM scheme
is based on. In this case a nontrivial mapping of the output
symbols of the CC to signal points results in a time-variant trellis.
We propose an efﬁcient technique to integrate an ISI-channel
into this trellis and show that the computational complexity can
be signiﬁcantly reduced by means of a reduced state sequence
estimation (RSSE) algorithm for time-variant trellises.
Index Terms—trellis-coded modulation (TCM); punctured con-
volutional codes; Viterbi-Algorithm (VA); ISI-channel;
I. INTRODUCTION
Ungerboeck’s trellis-coded modulation (TCM) [1] is a band-
width efﬁcient digital transmission scheme when very low
overall latency is desired. Low latency is ensured by the use
of convolutional codes instead of block codes (cf. [2]) and the
dispense with interleaving (as opposed to conventional bit-
interleaved coded modulation [3]).
Ungerboeck showed that a signiﬁcant increase in the
Asymptotic Coding Gain (ACG) can be achieved when con-
sidering channel coding and modulation jointly. By expanding
the constellation from 2n−1 to 2n signal points and employing
a rate- n−1
n
convolutional encoder one can improve the robust-
ness of the transmission against noise by up to 6 dB without
any further costs besides some computational effort. However,
TCM is strictly limited to integer transmission rates.
Our approach applies punctured TCM (P-TCM) with an
arbitrary rate. We extend P-TCM to intersymbol interference
(ISI)-channel scenarios. In this case, ML-decoding can be
performed by efﬁciently incorporating the ISI-channel into the
trellis.
We show that reduced-state sequence estimation (RSSE) can
be applied in order to reduce computational complexity. We
were able to show in [4], [5] that for minimum phase channels,
the number of states to decode must not be signiﬁcantly higher
than the number of states in the channel encoder. In this
paper we will describe the application of RSSE to P-TCM
and discuss the partitioning of the time-variant trellis into
hyperstates.
This paper is structured as follows: In Sec. II we ﬁrst
introduce notation and present the system model. Sec. III
brieﬂy recapitulates a presentation technique that enables
the implementation of punctured encoding. The application
of RSSE for P-TCM is given in Sec. IV. Final results of
numerical simulation and conclusions are given in Sec. V and
Sec. VI, respectively.
II. SYSTEM MODEL
This paper deals with convolutionally encoded pulse-
amplitude modulated (PAM) transmission as depicted in Fig. 1.
(Here, the term PAM is used for complex-valued signal con-
stellations A as well including amplitude-shift keying (ASK),
phase-shift keying (PSK) or quadrature-amplitude modulation
(QAM).) A binary data sequence ⟨u⟩is encoded using a rate-
u[l]
C
P
L
A
h[k]
c[k]
ℓ[k]
y[k]
nc
Fig. 1.
Concatenation of a rate- 1
2 convolutional encoder C and puncturing
P with labeling and modulation (nu = 0, nc = 2).
nc−1
nc
binary convolutional encoder C with generator polyno-
mials gij(D), 1 ≤i ≤nc; 1 ≤j ≤nc−1, with delay operator
D, nc −1 parallel binary-input symbols and nc parallel output
symbols at each time instant.
At each output of the encoder, the symbols traverse through
a puncturing system with puncturing matrix P = [Pij], Pij ∈
{0, 1} ; 1 < i ≤nc; 1 < j < Ωand period Ω. For each
(nc)-tuple of encoder output symbols the puncturing scheme
cyclically advances by one step. Where Pij is zero, the current
symbol at the output is discarded, accordingly.
The punctured encoded output symbols c[k] are labeled to
ℓ[k] before being mapped to the M = 2nu+nc = 2n-ary signal
constellation A.
The modulated (possibly complex-valued) transmit signal
traverses through a memory-L discrete-time ISI-channel with
L + 1 channel coefﬁcients h[k] with k denoting the discrete
time index.
The task of the receiver is to estimate for the information
bits given the transmit signal y[k] plus additive noise. Here,
we focus on perfect channel knowledge at the receiver-side.
arXiv:1312.1482v1  [cs.IT]  5 Dec 2013


## Page 2


2
III. PUNCTURED TRELLIS-CODED MODULATION
In the following, we will brieﬂy recapitulate punctured
convolutional trellis coded transmission over ISI-channel sce-
narios as introduced in [5].
In contrast to classical TCM, our approach using punctured
convolutional codes results in nontrivial mapping of coded bits
to modulation symbols. As a consequence, the trellis is time-
variant as already described in [5]–[7].
In order to brieﬂy recapitulate decoding concept for punc-
tured trellis coded modulation, we focus on 4-ary ASK-
modulation, a memory-2 convolutional code, and a short
puncturing scheme namely P =

(1 1)⊤(0 1)⊤
. Note that,
whenever the number of erased bits in one period of the punc-
turing scheme is not dividable by log2(M), the puncturing
scheme has to be repeated until this condition is fulﬁlled.
This restriction ensures that entire modulation symbols can be
constructed by the ﬁnite state machine (FSM). In our example,
the puncturing period (e.g.,

(1 1)⊤(0 1)⊤
) has to be applied
twice. As can be seen from the encoding process in Fig. 2, the
third and the seventh encoded symbol are punctured and do
not contribute to the labeling and modulation process. Thus,
the second symbol, i.e., a[k + 1], contains information about
u[l+1] and u[l+2] and the third symbol, i.e., a[k+2], contains
information about u[l + 2] and u[l + 3].
u[l]
u[l + 1]
u[l + 2]
u[l + 3]
g1
g2
g1
g2
g1
g2
g1
g2
MSB
LSB
MSB
LSB
MSB
LSB
×
×
ℓ[k]
ℓ[k + 1]
ℓ[k + 2]
a[k]
a[k + 1]
a[k + 2]
P
P
Fig. 2.
Encoding process for a rate- 2
3 punctured convolutional code and
natural labeling. Overall transmission rate R = 4
3 .
When decoding the second symbol (e.g., a[k+1]), a decision
can be made for u[l + 1] but not for u[l + 2], as a portion of
information will be received in the consecutive symbol. Thus,
the trellis has to be expanded in order to use the symbols
a[k + 1] and a[k + 2] when decoding u[l + 2]. As sample
trellis is given in Fig. 3.
Γ0
Γ1
Γ2
Fig. 3.
Time-variant trellis for a punctured rate-2/3 convolutional code. In
the ﬁrst to VA steps, two transitions arrive at each state, i.e., one bit can be
estimate, whereas the third step allows an estimation for two bits.
To algorithmically handle the time-variant mapping we in-
troduced a set of so-called generator offsets Ti which describe,
depending on the puncturing scheme, modulation size, and
time instant, the relations between generator polynomials,
input value, FSM state, and mapping to MSB or LSB, respec-
tively. For each new generator offset Ti a new trellis segment
MSB
LSB
h[0]
h[1]
h[0]
h[1]
h[0]
h[1]
T0
T2
T1
T0
T2
T1
k + 3 k + 2 k + 1
k
k −1 k −2 k −3 k −4
Fig. 4.
State transitions of the transmitter FSM with R = 4/3 and the
relations between generator polynomials, FSM-state/input and channel state
for a memory-1 ISI-channel.
arises, e.g., the number of generator offsets equals the number
of trellis segments in one trellis period.
When transmitting over an ISI-channel, several symbols are
stored in the memory of the ISI-channel independently from
the encoding and puncturing process. Thus, multiple generator
offsets Ti have to be considered simultaneously. This can be
seen from Fig. 4 for a memory-1 channel. There, the resulting
sequence of used generator offsets is depicted. This scheme
can easily be extended to arbitrary lengths of the ISI-channel.
A detailed description as well as an algorithm to construct
such trellises will be given in a separate full-length paper.
IV. REDUCED-STATE SEQUENCE ESTIMATION
Reduced-state sequence estimation (RSSE) [8] is proposed
to reduce the number of states at the cost of small loss in
Euclidean distance. In order to introduce RSSE for P-TCM, we
ﬁrst brieﬂy recapitulate delayed decision-feedback sequence
estimation (DFSE) [9].
A. Delayed Decision Feedback Sequence Estimation
When equalizing (uncoded) digital PAM signaling over a
discrete-time ISI-channel with L+1 tabs using DFSE (i.e., no
decoding), the trellis is constructed from the ﬁrst ˜L ≤L tabs
only. Thus, the number of states is reduced from M L to M ˜L.
The remaining L + 1 −˜L channel tabs are considered
in a delayed decision-feedback equalization (DFE) that is
performed in each trellis state using the delayed path register
of the corresponding state.
The main difference to full state equalization appears in the
metric computation for each time instant. From (1) it becomes
clear that the state speciﬁc path register preg[k, s] is delayed by
˜L and its elements are multiplied by the subsequent channel
coefﬁcients hdfe[h] which have not been considered in the
trellis. The branch metric λ(s, u) (e.g., Euclidean distance of
the received symbol y[k] to the hypotheses h(s, u) for the
states s and bits u) thus includes the correction factor δ:
δ =
X
κ
preg[k −˜L + κ, s] · hdfse[κ]
(1)
λ(s, u) =
y[k] −h(s, u) −δ
2
B. Reduced State Sequence Estimation
For our coded transmission over ISI-channel we consider
RSSE instead. Here, Z arbitrary MLSE states, each with
M = 2K possible branches to adjacent states, are combined


## Page 3


3
into ZR =
Z
2J ; J ∈N hyperstates [10] each having 2J
substates and 2K ·2J branches. A certain assignment of states
to hyperstates is called a partitioning [10].
Instead of having 2K arriving branches at each of the Z
MLSE states we get a set of 2K · 2J branches at each of
the ZR hyperstates. The total number of available branches
remains 2K ·Z. However, when using RSSE only 2K branches
are possible (i.e., enabled) from each state, at a given time
instant. The availability of branches is determined by the path
registers, and thus form a decision-feedback.
The metric computation in this case can be implemented
as depicted in Algorithm 1. Note that with line 6 only M
branches are activated. Thus, the VA has to decide between M
survivor branches at each state giving an estimate for log2(M)
bits.
Algorithm 1 Metric calculations for RSSE
1: ˜L ←log2(nr. hyperstates)/ log2(M)
2: ℓ←log2(nr. substates)/ log2(M)
3: for all s ∈S do
4:
for all u ∈A · K do
5:
for all κ = 1 →ℓdo
6:
ζ[κ] = preg(end −˜L + κ, s)
▷active branches
7:
end for
8:
λ(s, u) ←
y[k] −h(ζ, u)
2
▷branch metric
9:
λ(s, u) ←λ(s, u) + Γ(s)
▷acc. path metric
10:
end for
11: end for
For time-variant trellises some modiﬁcations to the under-
lying VA are necessary, which are described in [5].
The main difference to MLSE is, that we decide for a
surviving path prematurely resulting in a truncation of error
events. A loss in Euclidean distance appears if an error event
with minimum Euclidean distance gets truncated. Therefore
the performance of RSSE strongly depends on the partitioning
of the states into hyperstates. Instead of exhaustively search
for the optimum state partitioning, which maximizes the
intra-hyperstate distance [10], we exploit the minimum phase
characteristics of the ISI-channel which is, as described above,
fully integrated into our trellis.
For a minimum phase channel impulse response the prior
channel input symbols are weighted less than more recent ones
and, thus, affect the metric less. The elder the symbols, the fur-
ther back it is stored in the vector presentation of a particular
trellis state. Hence, the intra-hyperstate distance is maximized
when states are combined with respect to elder positions in
the state number. This particular partitioning is equivalent to
DFSE for ISI-channels (which is the optimum partitioning for
equalization of minimum phase ISI-channels [10]) and will
in the latter be called DFSE partitioning. As the minimum
phase ISI-channel is the last element to affect the transmitted
symbols and is also fully integrated into the trellis, we can
apply the DFSE partitioning to use RSSE for P-TCM over ISI-
channels. An implementation of this set partitioning for the Jth
level exploiting the minimum phase characteristics is shown
in Algorithm 2. The columns in the resulting matrix p(z, i)
deﬁne the states that have to be grouped into hyperstates.
Algorithm 2 DFSE Partitioning for RSSE
1: i, z ←1
2: for ℓ= 1 →Z do
3:
if ℓmod J = 0 then
4:
z ←z + 1
5:
end if
6:
p(z, i) = ℓ
7:
i ←i + 1
8: end for
In the following we will focus on our state design and
two possibilities to apply DFSE partitioning to time-variant
trellises.
C. State Design
In Fig. 5 a single trellis state in the VA is depicted as a
FIFO. Input values to the FSM are represented by the branches
at the left-hand side, whereas values that drop of the FIFO
are stored within the state-speciﬁc path register preg(k, s) at
the right-hand side. During decoding when entering a trellis
MLSE states
path register
t
0
1
MLSE states
path register
RSSE states
path register
enable
branch
eventually
punctured
bit
t
Fig. 5.
Graphical representation of our state design for punctured convolu-
tional coding with and without reduced-state sequence estimation.
segment that is split, i.e., has an increased number of states,
the two possibilities for the punctured bit are tracked using an
additional delay element, indicated by the hatched block ( ).
When DFSE partitioning is performed, the states can be
reduced as shown in Fig. 5. There, fewer FIFO elements are
used to deﬁne the trellis state, while the remaining ones are
used as feedback to enable branches for the next trellis step
for that particular state.
An implementation of this algorithm needs to ensure that
when entering a split trellis segment, i.e., increased number
of states, the right path register is chosen as source for the
decision feedback.
D. State Partitioning
As already mentioned, a DFSE partitioning of the ﬁrst order,
i.e., reducing the number of states in each trellis segment
by a factor of two, combining states that differ in the eldest
position, into hyperstates. Hence, when applied to a punctured
TCM, each trellis segment undergoes the same partitioning.
A resulting reduced-state trellis is depicted on the left-hand
side of Fig. 6 for J = 1 and J = 2. As a consequence, non-
existing states from the original trellis are also partitioned (cf.,
ﬁrst trellis segment).


## Page 4


4
uniform
segment-dependent
×
×
×
×
×
×
Fig. 6.
Illustration of uniform and segment-dependent partitioning for
J = {1, 2}.
Due to the reduction of non-existing states, and hence
reduced minimum Euclidean distance, we propose to partition
those segments ﬁrst that are split and keeping the others unpar-
titioned. As can be seen from the ﬁrst-level state reduction in
Fig. 6 (right-hand side, above), the ﬁrst segment contains two
transitions in each state, and thus is not partitioned, whereas
in segment two and three, each state has four transitions, due
to the state partitioning.
Apparently, the ﬁrst segment may be handled with a full
state VA, while the other two segments need to be decoded
via RSSE using the path register in each state.
The right-hand side of Fig. 6 show the segment-depending
partitioning and state reduction for J = 1 and J = 2. The
segments for J = 1 show four, and eight transitions per state,
respectively. At this point RSSE has to consider a different
amount of information in the path register for each segment.
The resulting trellis shows a less decreased minimum Eu-
clidean distance when compared to the uniform partitioning
but has a slightly higher computational complexity because
of the extra states. Thus, the segment-dependent partitioning
technique enables an even more ﬂexible way to trade between
complexity and performance.
V. NUMERICAL RESULTS
In this section we will give numerical simulation results
and investigate several ISI-channels for punctured TCM. We
analyse the decoder complexity as number of branch metric
calculations per information bit and show that this approach
enables a ﬂexible trade-off between computational complexity
and performance.
Due to the minimum phase characteristics of the ISI-channel
the partitioning of the trellis states into hyperstates leads to
the smallest possible loss in Euclidean distance. Hence, if,
for instance, the ISI-channel is an equal tab delay line, the
loss in Euclidean distance is higher than for an exponentially
decaying channel because of the premature decisions for a
surviving path.
To see this effect we conducted simulations over different
ISI-channels of unit energy and plotted the complexity number
over the required Eb
N0 to achieve a bit error probability of less
than 10−3. The unit energy channels are deﬁned as:
hexp[κ] =
1
qP
κ
|hexp[κ]|2 e (−κ/κ0)
for 0 ≤κ ≤L
hlin[κ] =
1
qP
κ
|hlin[κ]|2
L −κ + 1
L + 1
for 0 ≤κ ≤L
6
8
10
12
14
16
18
20
0
200
400
BER = 10−3
10 log10

Eb
N0

in dB
Computational Complexity
partitioning
uniform
segment dependent
Fig. 7.
Decoding complexity for a P-TCM transmission scheme with gener-
ator polynomials [13 15]oct, puncturing scheme

(1 1)⊤(0 1)⊤
(Rate: 4
3 )
natural labeling and 4-ASK signaling over three different ISI-channels
hexp[κ] (κ0 = 1), hlin[κ], hequ[κ] (solid: Uniform partitioning, dashed:
Segment-dependent partitioning).
hequ[κ] =
1
qP
κ
|hequ[κ]|2 =
1
√
L
for 0 ≤κ ≤L
The results can be seen in Fig. 7. As should be clear to
the reader, the loss in Euclidean distance is smallest for an
exponentially decaying ISI-channel.
VI. CONCLUSION
It has been shown that TCM can be extended by puncturing.
Furthermore, an efﬁcient MLSE decoder for P-TCM over ISI-
channels was proposed and investigated.
The numerical simulation results clearly show that we can
achieve a soft trade-off between spectral and power efﬁciency
easier and more ﬂexibly than by means of traditional TCM.
REFERENCES
[1] G. Ungerboeck, “Trellis-coded modulation with redundant signal sets;
part i: Introduction; part ii: State of the art,” Communications Magazine,
IEEE, vol. 25, no. 2, pp. 5 –21, February 1987.
[2] T. Hehn and J. B. Huber, “LDPC Codes and Convolutional Codes
with Equal Structural Delay: A Comparison,” IEEE Transactions on
Communications, vol. 57, no. 6, pp. 1683–1692, June 2009.
[3] E. Zehavi, “8-PSK Trellis Codes for a Rayleigh Channel,” IEEE Trans-
actions on Communications, vol. 40, no. 5, pp. 873 –884, may 1992.
[4] F. Schuh, A. Schenk, and J. Huber, “Reduced complexity Super-Trellis
decoding for convolutionally encoded transmission over ISI-Channels,”
in 2013 International Conference on Computing, Networking and
Communications, Signal Processing for Communications Symposium
(ICNC’13 - SPC), San Diego, USA, Jan. 2013.
[5] ——, “Matched decoding for punctured convolutional encoded trans-
mission over ISI-Channels,” in 9th International ITG Conference on
Systems, Communications and Coding 2013 (SCC’2013), Munich, Ger-
many, Jan. 2013.
[6] T. Woerz and R. Schweikert, “Performance of punctured pragmatic
codes,” in Global Telecommunications Conference, 1995. GLOBECOM
’95., IEEE, vol. 1, nov 1995, pp. 664 –669 vol.1.
[7] F. Schuh, A. Schenk, and J. Huber, “Punctured Trellis-Coded Modula-
tion,” in submitted to ICC 2014, Jun. 2014.
[8] M. Eyuboglu and S. Qureshi, “Reduced-State Sequence Estimation With
Set Partitioning and Decision Feedback,” IEEE Trans. Commun., vol. 36,
no. 1, pp. 13–20, Jan. 1988.
[9] A. Duel-Hallen and C. Heegard, “Delayed Decision-Feedback Sequence
Estimation,” IEEE Trans. Commun., vol. 37, no. 5, pp. 428–436, May
1989.
[10] B. Spinnler and J. Huber, “Design of Hyper States for Reduced-State
Sequence Estimation,” in Proc. IEEE Int. Conf. Communications ICC
’95 Seattle, vol. 1, 1995, pp. 1–6.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1312_1482v1_low_complexity_decoding_for_punctured_trellis_coded_modulation_over_intersymbol
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2013/1312_1482V1_LOW_COMPLEXITY_DECODING_FOR_PUNCTURED_TRELLIS_CODED_MODULATION_OVER_INTERSYMBOL.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

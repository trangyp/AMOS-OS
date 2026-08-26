---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1301.4050v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1301.4050v1_Punctured_Trellis-Coded_Modulation

> Source: 1301.4050v1_Punctured_Trellis-Coded_Modulation.pdf

> Pages: 5

---


## Page 1


Punctured Trellis-Coded Modulation
Fabian Schuh, Andreas Schenk, and Johannes B. Huber
Institute for Information Transmission, Friedrich-Alexander-Universit¨at Erlangen-N¨urnberg, Germany
mail: {schuh, schenk, huber}@LNT.de
Abstract—THIS PAPER IS ELIGIBLE FOR THE STUDENT
PAPER AWARD
In classic trellis-coded modulation (TCM) signal constellations
of twice the cardinality are applied when compared to an uncoded
transmission enabling transmission of one bit of redundancy per
PAM-symbol, i.e., rates of
K
K+1 when 2K+1 denotes the cardi-
nality of the signal constellation. In order to support different
rates, multi-dimensional (i.e., D-dimensional) constellations had
been proposed by means of combining subsequent one- or two-
dimensional modulation steps, resulting in TCM-schemes with
1
D bit redundancy per real dimension. In contrast, in this paper
we propose to perform rate adjustment for TCM by means of
puncturing the convolutional code (CC) on which a TCM-scheme
is based on. It is shown, that due to the nontrivial mapping of
the output symbols of the CC to signal points in the case of
puncturing, a modiﬁcation of the corresponding Viterbi-decoder
algorithm and an optimization of the CC and the puncturing
scheme are necessary.
Index
Terms—trellis-coded
modulation
(TCM);
multi-
dimensional
and
pragmatic
TCM;
punctured
convolutional
codes; Viterbi-Algorithm (VA);
I. INTRODUCTION
Ungerboeck’s trellis-coded modulation (TCM) [1], [2] is an
attractive digital transmission scheme when low over-all delay
is desired. Low latency is ensured by the use of convolutional
codes instead of block codes (cf. [3]) and the dispense with
interleaving (as opposed to convolutional bit-interleaved coded
modulation [4]).
Ungerboeck showed that a signiﬁcant increase in Asymp-
totic Coding Gain (ACG) can be achieved when considering
channel coding and modulation jointly. By expanding the
constellation from 2K to 2K+1 signal points and employing
a rate-
K
K+1 convolutional encoder one can improve the noise
robustness of the transmission by upto 6 dB without any fur-
ther costs besides computational effort [1]. High transmission
rates can be achieved when additional uncoded bits are used
to address the signal points. The most important modiﬁcation
to Ungerboeck’s TCM propbably is the extension to multiple
dimensions [5] accommodating non-integer transmission rates
by grouping consecutive modulation symbols and constructing
a D-dimensional signal space.
Alternatively, in this paper, puncturing the channel code
from a mother code is considered. As already described in [6],
[7], in this case metric computations become time-dependent,
as does the trellis diagram. In contrast to the modiﬁed metric
increment suggested in [7], we propose Maximum-Likelihood
This work was supported by Federal Ministry of Economics and Technology
(BMWi) within the project C-PMSE.
(ML) decoding using a modiﬁed Viterbi algorithm (VA). Thus
our approach enables ML-decoding of pragmatic punctured
TCM for arbitrary rates. We performed extensive computer
simulations in order to optimization the CC and the puncturing
scheme.
This approach can be extended to ISI-channel scenarios. In
this case, ML-decoding can be performed using the matched
decoding scheme of [8], [9].
This paper is structured as follows: First, we brieﬂy intro-
duce notation and the system model in consideration in Sec. II.
Sec. III recapitulates TCM and introduces a presentation tech-
nique that enables the implementation of punctured encoding
in Sec. IV. A code search has been performed to ﬁnd the best
codes for out purpose in Sec. V. Final results and conclusions
are given in Sec. VI and Sec. VII, respectively.
II. SYSTEM MODEL
This paper deals with convolutionally encoded pulse-
amplitude modulated (PAM) transmission1 as depicted in
Fig. 1. A binary data sequence ⟨u⟩is split into nu parallel
uc[ν]
C
P
L
M
uui[ν]
. . .
c[k]
ℓ[k]
nu
nc
kc
m[k]
Fig. 1.
System model for punctured trellis-coded modulation (P-TCM).
uncoded sequences uu[ν] and kc parallel sequences uc[ν] that
are encoded using a rate- kc
nc binary convolutional C encoder
with generator polynomials [ gij ] , 1 ≤i ≤nc; 1 ≤j ≤kc,
with kc parallel input symbols and nc parallel output symbols
at each time instant. At each output of the encoder, the symbols
traverse through a puncturing system with puncturing scheme
P = [Pij] ∈{0, 1} ; 1 < i ≤nc; 1 < j < Ωand period
Ω. For each encoder input symbol the puncturing scheme
cyclically advances by one step. Where Pij is zero, the current
symbol at the output is discarded, accordingly. The punctured
nc-ary encoded output symbols c[k] together with the uncoded
input symbols uu[ν] are labeled to ℓ[k] before being mapped
to the M = 2nu+nc-ary signal constellation.
Throughout this paper we will use the following notation:
• u[ν] ∈{0, 1} is the binary input sequence for the encoder
at time instant ν
1here, the term PAM is used for complex-valued signal constellations as
well including amplitude-shift keying (ASK), phase-shift keying (PSK) or
quadrature-amplitude modulation (QAM)
arXiv:1301.4050v1  [cs.IT]  17 Jan 2013


## Page 2


• c[k] ∈{0, 1} denotes the encoded (possibly punctured)
symbol
• ℓ[k] ∈L denotes the signal number from the set of
labelings L (e.g., natural labeling)
• m[k] ∈M is the modulated symbol (e.g., bipolar ASK).
M denotes the modulation alphabet of size M = |M|
• P = [Pij] ∈P denotes the puncturing scheme
The overall transmission rate of this scheme is R
=
RcRpnc + nu with Rc =
kc
nc and Rp being the rate of the
channel encoding and puncturing, respectively. The rate of the
puncturing can be calculate from the puncturing scheme by:
Rp =
ncΩ
P
i
P
j
Pij
.
(1)
III. TRELLIS-CODED MODULATION
In order to introduce maximum-likelihood sequence esti-
mation (MLSE) for punctured TCM, we ﬁrst brieﬂy recall the
encoding and mapping process for non-punctured TCM and
introduce a representation for the encoding process and the
state transitions of the ﬁnite-state-machine (FSM) (cf., [2]).
A. System Model
In the case of TCM, the number of output symbols from
a rate- kc
nc encoder is related to the size of the modulation
alphabet M so that nc = log2(M) and kc = nc −1 holds.
Fig. 2 shows an example of such a TCM transmitter with
nu = 0, kc = 1 and a rate- 1
2 encoder. Obviously, one of
the two channel encoder output symbols (before puncturing)
contains redundancy only.
u[k]
C
L
M
c[k]
ℓ[k]
m[k]
nc
kc
Fig. 2.
Concatenation of a rate- 1
2 convolutional encoder C, a labeling and
modulation. No puncturing is applied (ku = 0, kc = 1, nc = 2).
The coded bits are mapped onto a single transmit symbol
m[k] out of a modulation alphabet of size 2nc. Thus, after
labeling and modulation, the overall transmission rate of TCM
is R = kc + nu. The decoding trellis is well-known, time-
invariant and has 2kc state transitions for each state.
In the following we describe the encoding process and the
FSM to span a trellis. For simplicity of explanation, we focus
on a rate- 1
2 encoder and 4-ary modulation. We restrict ourselfs
to nonrecursive encoding [1].
Fig. 3 illustrates the encoding process. The uncoded unipo-
lar information sequence u[k] ∈{0, 1} is inserted into
the FSM as input values and later passes through all delay
elements describing the state of the FSM. Here, the generator
polynomials g1 and g2 process the input symbol together
with the FSM state synchronously at each time instant. The
resulting encoded bits, denoted by MSB and LSB, respec-
tively, are labeled into ℓ[k] and modulated in m[k] to the
4-ary symbol alphabet of the transmission scheme, e.g., via
m[k] = 2(2MSB + LSB) −1 for natural labeling and bipolar
ASK (cf., Sec III-B).
u[k]
u[k + 1]
u[k + 2]
u[k + 3]
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
MSB
LSB
ℓ[k]
ℓ[k + 1]
ℓ[k + 2]
ℓ[k + 3]
m[k]
m[k + 1]
m[k + 2]
m[k + 3]
Fig. 3.
Encoding process for a rate- 1
2 convolutional code and 4-ary natural
mapping. Overall transmission rate R = 1.
Fig. 4 depicts the state transitions of the FSM, when no
puncturing is involved. The states are represented as memory
elements in a ﬁrst-in ﬁrst-out (FIFO) register. The time-
invariance of the trellis becomes clear, as each input symbol
passes the same encoding procedure with g1 and g2, and
labeling and modulation are independent of the time instant.
As we will see later, this statement does not hold for punctured
coding. We use the following representation:
• dark gray blocks ( ) declare the trellis state
• light gray blocks ( ) deﬁne the input values to the FSM
and thus, the state transitions
• bars (
g1
) describe an arbitrary generator polynomials
in binary representation
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
k + 2
k + 1
k
k −1
k −2
Fig. 4.
State transitions of the transmitter FSM and the relations between
generator polynomials and FSM-state/input with ν = 2.
B. Labelings and Modulation
Labeling and modulation can either be implemented using
a lookup table for L and M, or via analytical formulas.
E.g., for the 4-ary natural labeling we multiply the MSB
by 2 and add the LSB, i.e., ℓ[k] = 2MSB[k] + LSB[k]. An
implementation of an ASK modulator can be seen as unipolar
binary symbols ℓ[k], mapped onto bipolar symbols m[k] within
an alphabet of size M with m[k] = (ℓ[k] · 2) −(M −1).
Different labelings are easily incorporated, e.g., a Gray
labeling can be achieved by ℓ[k] = (1 −MSB[k])(2MSB[k] +
LSB[k]) + (MSB[k])(2MSB[k] + (1 −LSB[k])).
C. Trellis-based Decoding
In the following section we will brieﬂy describe the appli-
cation of a trellis-based decoding algorithm for Ungerboeck’s
TCM. The trellis encoder of the transmitter can be used to
generate the hypothesis and the state transitions of a FSM.
The full-state receiver for a non-punctured coding is depicted
in Fig. 5 and uses the hypothesis to calculate the metrics
λi[k], e.g., squared Euclidean distances between the received
signal and the hypothesis, for the noisy received signal. The


## Page 3


trellis-based decoding algorithm, such as the VA, estimates
the transmitted data sequence by the use of the trellis and the
metrics.
m[k]
+
Metric
calculation
λi[k]
Trellis-based
decoding
algorithm
n[k]
ˆu[k]
Fig. 5.
The full-state trellis-based decoding, e.g., with the VA.
IV. PUNCTURED TRELLIS-CODED MODULATION
In the following, we will describe the necessary modiﬁca-
tions when punctured coding is applied.
A. System Model
A system model of punctured convolutional coding, without
transmission of uncoded bits, i.e., nu = 0, is depicted in Fig. 6.
u[k]
C
P
L
M
c[k]
ℓ[k]
m[k]
nc
kc
Fig. 6.
Concatenation of a rate- 1
2 convolutional encoder C and puncturing
P with labeling and modulation (ku = 0, kc = 1, nc = 2).
By coded modulation with puncturing, we can achieve a
transmission rate of R = RcRpRm. For reasons we will see
later, our approach is constraint to nc = 2, i.e., Rc = 1
2. Hence,
the transmission rate is only determined by Rp ∈[ 1, 2 [.
Note that in the latter, the mother code deﬁnes the size of the
modulation alphabet while the rate is increased by puncturing.
In the following, we exemplarily focus on ku = 0, kc = 1,
nc = 2 and the puncturing scheme [ 1 1; 0 1 ].
First, we describe the encoding process and state transitions
when punctured codes are used, and discuss the FSM for
punctured convolutional codes as well as the modiﬁcations
necessary for the VA to run in the resulting trellis.
When punctured convolutional codes are used, the relation
that one uncoded information bit results in one modulation
symbol is not valid any longer. Note that, whenever the number
of erased bits in one period of the puncturing scheme is
not devideable by log2(M), the puncturing scheme has to
be repeated until this condition is fulﬁlled. This restriction
ensures that entire modulation symbols can be constructed by
the FSM. In our case, the puncturing period (e.g., [ 1 1; 0 1 ])
is applied twice. As can be seen from the encoding procress in
Fig. 7, the third and the seventh encoded symbol is punctured
and does not contribute to the labeling and mapping process.
The transitions of the FSM, depicted in Fig. 8, show two
differences when compared to non-punctured FSM transitions
(cf., Fig. 4). These are described subsequently.
1) Generator Offsets Ti: It becomes clear that the strict
relations between the MSB, LSB and the generator polynomial
g1 and g2, respectively, no longer hold. The second symbol,
i.e., m[ν+1], contains information about u[ν+1] and u[ν+2].
In addition, the MSB is now generated by g2 instead of g1.
Accordingly, the LSB, which was generated by g2 in the non-
punctured case, is now generated by g1. It is also clear that
the third symbol is generated by u[ν + 2] and u[ν + 3] using
the generator polynomial g2 twice.
u[ν]
u[ν + 1]
u[ν + 2]
u[ν + 3]
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
m[k]
m[k + 1]
m[k + 2]
Fig. 7.
Encoding process for a rate- 2
3 punctured convolutional code and
natural labeling. Overall transmission rate R = 4
3 .
g1
g2
g2
g1
g2
g2
g1
g2
T0
T1
T2
T0
MSB
LSB
MSB
LSB
MSB
LSB
MSB
LSB
ν + 5
ν + 4
ν + 3
ν + 2
ν + 1
ν
ν −1
ν −2
Fig. 8.
State transitions of the transmitter FSM and the relations between
generator polynomials and FSM-state/input.
To handle these relations we introduce a set of so called
generator offsets Ti which describe, depending on the punc-
turing scheme, modulation size and time instant, the relations
between generator polynomials, input value, FSM state, and
mapping to MSB or LSB, respectively.
In our example, T1 indicates that the MSB output symbol
can be determined by the memory ( ) only, regardless of
the current input symbol. On the other hand, in order to
calculate the LSB we have to use the input value ( ) and g1.
Obviously, the information in the LSB is one step ahead of
the MSB. Thus, we need to extend the trellis at this point
and can calculate the MSB using the FSM state and the
generator polynomial g2. Note that in case of M = 4, T0
indicates that no puncturing is active, i.e., an even number of
puncturings occurred up to time instant ν, and the generator
polynomials are synchronized with LSB and MSB. T1 is
used, whenever an odd number of puncturings has happened
and T2 is used when the next puncturing synchronize the
generator polynomials with MSB and LSB again. The number
of generator offsets needed to describe all steps depends on the
size of the modulation alphabet, whereas the generator offsets
depend also on the puncturing scheme.
2) State Extension: The FSM transitions in Fig. 8 show
that the symbol m[ν +1] contains information on the uncoded
information bits u[ν + 1], for which the MSB output was
punctured, and the consecutive information bit u[ν + 2]. We
see that, when generating the output, the calculation of the
LSB is one step ahead to the MSB and considers one extra
information bit. This results in a trellis that has to be expanded
(i.e., splitted) by a factor of two. This can be easily seen
from Fig. 8 as the generator polynomials in the second step
(generator offsets T1) now cover four blocks instead of just
three. However, for a 4-ary transmission, when puncturing is


## Page 4


performed a second time, MSB and LSB are resynchronized
with the generator polynomials and a so called merge happens
in the trellis.
When considering M > 4, a resynchronization will appear
after log2(M) punctured bits. Extending the FSM to handle
nc > 2 does not seem to be a good alternative choice,
due to an increasing number of generator offsets and the
signiﬁcant increase of computational complexity. Hence, we
restrict ourselves to nc = 2 for complexity reasons.
Therefore, a trellis based decoding algorithm, such as the
VA, has to be performed on a time-variant trellis diagram.
An example trellis for a punctured convolutional code with a
constraint length ν = 2 will be given below.
B. Trellis-based Decoding
In the following we will exemplarily describe trellis-based
decoding for punctured convolutional codes.
When using the puncturing scheme [ 1 0; 1 1 ] introduced
above the VA has to estimate four bits within three symbols
from the trellis transitions. In order to see the modiﬁcations
of the VA we need to consider the state extension.
Using Fig. 8, we deﬁne in each step T0, . . . , T2 the input
value to be the ﬁrst value which is used by either g1 or g2. As
a result, in step T0 the values at time instants k = {ν; ν + 4}
can be deﬁned as input values. When in step T1 or T2, the input
value is at time instant k = {ν + 2; ν + 3}. Unfortunately
we cannot estimate the value for u[ν + 2] in T1, nor can we
estimate u[ν + 3] in T2, because one half of the information
has not been received, yet, (i.e., missing information is located
in the MSB in T2 and T0, respectively).
However, as all information on u[ν+1] (for which the output
of g1 was punctured) has been received in T1 we can estimate
it. To do so we have to evaluate the MSB of the survivor
state which is selected by the survivor path during the add-
compare-select procedure within the VA. In T2, as already
mentioned, selecting the survivor path allows a decision for
two information bits (the MSB of the survivor and the input
value) namely u[ν + 3] and u[ν + 4]. At this point one has
to evalutate the survivor state for the ﬁrst information bit, and
the survivor transition for the second one.
×
×
×
×
×
×
×
×
−1
−1
−1
+1
+1
+1
11
10
01
00
+1
011
1 11
+1
1 11
11
T0
T1
T2
copy
state
metric
Fig. 9.
Sample Trellis for Decoding
Fig. 9 illustrates where the information bits are located
(boxed) by running the VA over one period of the trellis. As
one can see the ﬁrst two steps T0 have two transitions arriving
at each state resulting in an estimation of a single bit per state.
However, in the last step T2 the decision for a survivor gives
an estimate on two bits. The path register of the VA has to
consider the fact that now four bits have been estimated within
three received symbols. The last step can be described as a
state merging, where the split is performed in the ﬁrst step,
e.g. by copying the state metrics of the ﬁrst four states into
the last four states.
C. Increased Transmission Rate
In order to increase the transmission rate one can extend the
size of the modulation alphabet and transmit nu additional un-
coded bits per modulation step, following the set-partitioning
principle [1]. This TCM approach is well-understood and shall
now be extended with puncturing as depicted in Fig. 1. By this,
the total transmission rate is increased to (here, Rc · nc = 1)
RPTCM = Rp + nu
with nu and nc denoting the number of uncoded and coded
bits per symbol, respectively. In contrast to Ungerboeck’s
TCM, our proposed approach allows to adapt to an arbitrary
transmission rate.
The resulting trellis is equal to that in Fig. 9 with 2nu
parallel branches at each state. Each pair of parallel branches
contain one uncoded bit information per trellis segment. How-
ever, three steps in the time-variant trellis contain four coded
information bits. Thus, the total number of bits per trellis
period is seven. We see, that the transmission of the coded
and uncoded bits are not synchronized any longer.
V. CODES AND PUNCTURING SCHEMES
As there is no analytical method known to the authors to ﬁnd
the optimal combination of channel (mother) code, puncturing
and labeling for a given modulation scheme and constraint
length, jointly, an exhaustive search was performed.
The search was carried out for convolutional codes with
constraint length 5 (memory-4, i.e., ν = 4), natural labeling,
and ASK modulation. The signal-to-noise power ratio Eb
N0 was
between 6 and 12 dB and a transmission of 105 informations
bits was performed.
In order to readuce the seach space, the puncturing schemes
P
= [Pij] ∈P; i ∈[1, 2] ; j
∈[2, · · · , Ω], with the
puncturing period Ω, are used to deﬁne the transmission rate
and are constructed in such a way that the sum of the columns
i follow the rule
2
X
i=1
Pij =
(
2
if j = 1
1
else.
(2)
Hence, the rate of the puncturing scheme is Rp = Ω+1
Ω.
The resulting generator polynomials in octal notation and
puncturing schemes for the 16-state convolutional encoder are
listed in Tab. I.


## Page 5


TABLE I
BEST MEMORY-4 (ν = 4) CODES AND PUNCTURING SCHEMES FOR
PUNCTURED CONVOLUTIONAL CODING WITH Rc = 1
2 , Rp = Ω+1
Ω.
R
Rc · Rp
polynomials
puncturing scheme
4/3
2/3
26, 37
8
1 0
1 1

3/2
3/4
36, 23
8
1 1 1
1 0 0

8/5
4/5
34, 31
8
1 0 10
1 1 0 1

5/3
5/6
04, 37
8
1 1 1 1 0
1 0 0 0 1

12/7
6/7
34, 31
8
1 0 1 0 1 0
1 1 0 1 0 1

0
5
10
15
20
25
1
2
3
4
5
6
7
8
4ASK
8ASK
16ASK
4QAM
16QAM
32QAM
BPSK
4ASK/4QAM
8ASK
16ASK/16QAM
32QAM
BER = 10−3
10 log10

Eb
N0

in dB
Rate
bit
symbol
Fig. 10.
Spectral efﬁciency vs. required Eb
N0 for a bit error rate of BER =
10−3. Channel codes with 24 states. Shannon capacity constraint (dashed
line, real-/complex-valued), Constellation capacity (dash-dotted line, ASK and
QAM). Asterisk markers: proposed approach. Empty markers: Ungerboeck’s
TCM, D = 1
VI. NUMERICAL RESULTS
Fig. 10 shows the simulation results for ASK modulation
schemes. The 16-state channel codes are punctured from a
rate 1
2 mother code using the puncturing scheme as deﬁndes
in Table I. Higher transmission rates are achieved by additional
uncoded bits and expansion of the constellation (cf., Fig. 1),
following the set partitioning principle.
Additionally,
two
consecutive
ASK
channel
symbols
are modulated to a two-dimensional quadrature-amplitude-
modulation (QAM) symbol to further increase transmission
rate without increasing the signal bandwidth.
The results clearly indicate that punctured TCM enables soft
transitions between classical TCM rates (integers) by punctur-
ing. By this means, the shape of the constellation constraint
capacity can be closely approximated using punctured TCM.
VII. CONCLUSION
It has been shown that TCM can be extended by puncturing.
We sketched the modiﬁcations necessary for the VA to prop-
erly work on the resulting time-variant trellises. Additionally,
we conducted a computer search to optimize for the channel
encoder and the puncturing scheme for ASK modulation. We
further increased the transmission rate by appending uncoded
information bits and thus enlarging the signal constellation as
well as by implementing QAM transmission scheme using two
subsequent ASK symbols.
The numerical simulation results clearly show that we can
achieve a soft tradeoff between spectral and power efﬁciency
easier and more ﬂexible than by means of traditional TCM
and multidimensional TCM.
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
[5] L.-F. Wei, “Trellis-coded modulation with multidimensional constella-
tions,” IEEE Transactions on Information Theory, vol. 33, no. 4, pp. 483
– 501, jul 1987.
[6] A. Viterbi, J. Wolf, E. Zehavi, and R. Padovani, “A pragmatic approach
to trellis-coded modulation,” Communications Magazine, IEEE, vol. 27,
no. 7, pp. 11 –19, july 1989.
[7] T. Woerz and R. Schweikert, “Performance of punctured pragmatic
codes,” in Global Telecommunications Conference, 1995. GLOBECOM
’95., IEEE, vol. 1, nov 1995, pp. 664 –669 vol.1.
[8] F. Schuh, A. Schenk, and J. Huber, “Reduced complexity Super-Trellis
decoding for convolutionally encoded transmission over ISI-Channels,” in
2013 International Conference on Computing, Networking and Commu-
nications, Signal Processing for Communications Symposium (ICNC’13
- SPC), San Diego, USA, Jan. 2013.
[9] ——, “Matched decoding for punctured convolutional encoded transmis-
sion over ISI-Channels,” in 9th International ITG Conference on Systems,
Communications and Coding 2013 (SCC’2013), Munich, Germany, Jan.
2013.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1109.0827v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1109.0827v1_A_Trellis_Coded_Modulation_Scheme_for_the_Fading_Relay_Channel

> Source: 1109.0827v1_A_Trellis_Coded_Modulation_Scheme_for_the_Fading_Relay_Channel.pdf

> Pages: 18

---


## Page 1


arXiv:1109.0827v1  [cs.IT]  5 Sep 2011
A Trellis Coded Modulation Scheme for the Fading
Relay Channel
Vijayvaradharaj T Muralidharan
Dept. of ECE, Indian Institute of Science
Bangalore 560012, India
Email: tmvijay@ece.iisc.ernet.in
B. Sundar Rajan
Dept. of ECE, Indian Institute of Science,
Bangalore 560012, India
Email: bsrajan@ece.iisc.ernet.in
Abstract—A decode and forward protocol based Trellis Coded
Modulation (TCM) scheme for the half-duplex relay channel, in a
Rayleigh fading environment, is presented. The proposed scheme
can achieve any spectral efﬁciency greater than or equal to one
bit per channel use (bpcu). A near-ML decoder for the suggested
TCM scheme is proposed. It is shown that the high SNR per-
formance of this near-ML decoder approaches the performance
of the optimal ML decoder. The high SNR performance of this
near-ML decoder is independent of the strength of the Source-
Relay link and approaches the performance of the optimal ML
decoder with an ideal Source-Relay link. Based on the derived
Pair-wise Error Probability (PEP) bounds, design criteria to
maximize the diversity and coding gains are obtained. Simulation
results show a large gain in SNR for the proposed TCM scheme
over uncoded communication as well as the direct transmission
without the relay. Also, it is shown that even for the uncoded
transmission scheme, the choice of the labelling scheme (mapping
from bits to complex symbols) used at the source and the relay
signiﬁcantly impacts the BER vs SNR performance. We provide
a good labelling scheme for 2l-PSK signal set, where l ≥2 is an
integer.
I. PRELIMINARIES AND BACKGROUND
Fig. 1.
The Relay Channel
We consider the Rayleigh fading relay channel shown in
Fig. 1, consisting of the source node S, the relay node R and
the destination node D. It is assumed that R can operate only
in the half-duplex mode, i.e., it cannot receive and transmit
simultaneously in the same frequency band. It is assumed
that R has perfect knowledge about the instantaneous value
of the fade coefﬁcient associated with the S-R link and D
has perfect knowledge about the instantaneous values of the
fade coefﬁcients associated with the S-R, R-D and S-D links.
Throughout, the phase during which the relay is in reception
mode is referred to as Phase 1 and the phase during which the
relay is in transmission mode is referred to as Phase 2.
In all practical scenarios the S-R and R-D links are stronger
than the S-D link. As a result, the use of coding schemes
which involve both S and R, can potentially outperform the
coding schemes involving S alone. The problem addressed
in this paper is the design of a Trellis Coded Modulation
(TCM) scheme for the relay channel, which achieves a spectral
efﬁciency greater than or equal to one bit per channel use
(bpcu) and provides a large gain compared to the TCM scheme
for the direct transmission without the relay.
A comparison of the proposed TCM scheme is made
with the uncoded transmission scheme for the relay channel
operating in the Decode and Forward (DF) mode, in which no
coding is done at S and R, which is described as follows: At S,
uncoded bits are directly mapped onto complex symbols from
a signal set during Phase 1 and transmitted. During Phase 2,
S and R map the uncoded bits (S uses the same bits as in
Phase 1 and R uses the bits it decoded during Phase 1) onto
complex symbols from a signal set for transmission. The signal
sets used at S during Phase 1, S during Phase 2 and R during
Phase 2 are assumed to be the same, but the mapping from
bits to complex symbols can be different.
A. The Proposed Scheme
The proposed TCM scheme for the fading relay channel is
shown in Fig. 2(a) and Fig. 2(b) (shown at the top of the next
page). It is assumed that TCM encoding at S during Phase 1
and Phase 2 and at R during Phase 2 take place using the same
encoder, but the labelling schemes used for mapping coded bits
onto signal points can be different. By a trellis, we refer to the
states of the TCM encoder, the edges connecting these states
in two successive stages and the complex numbers which are
labelled on these edges. By a path in the trellis, we refer to the
sequence of connected edges (the complex numbers labelled
on the edges are not included). Let TS1, TS2 and TR represent
the trellises used for encoding by S during Phase 1, by S
during Phase 2 and by R during Phase 2 respectively. Since
the encoder corresponding to the trellises TS1, TS2 and TR are
the same, they differ only in the complex numbers labelled on
the edges. Let ζ denote the set of edges connecting the states in
two successive stages of the trellis. The labelling of the edges
in the trellis TS1 is given by the map Xs1 : ζ −→S, where S
is the signal set used at S and R. Similarly, the maps Xs2 and
Xr are deﬁned for the the trellises TS2 and TR respectively.
During Phase 1, input bits at S are encoded by the TCM
encoder, mapped onto complex symbols from the signal set
S and interleaved by the block interleaver as shown in Fig.


## Page 2


(a) Phase 1
(b) Phase 2
Fig. 2.
The TCM Scheme
2(a). Each transmission made is assumed to be a block of L
complex symbols. After each transmission, the encoder state is
brought back to the all zeros state by appending zero input bits
at the end. Let PS denote the path in the trellis corresponding
to the output of the TCM encoder at S. Let xi
s1(PS) denote
the symbol to be transmitted corresponding to the ith branch
of the path PS, where 1 ≤i ≤L.
The received complex signal sequence at R and D during
Phase 1 are given by,
Y i
r
= hi
srxi
s1(PS) + zr;
Y i
d1
= hi
sd1xi
s1(PS) + zd1;

1 ≤i ≤L
where hi
sr and hi
sd1 are the independent zero mean circularly
symmetric complex Gaussian fading coefﬁcients associated
with the S-R and S-D links respectively with the corresponding
variances given by σ2
sr and σ2
sd. The additive noises zr and
zd1 are assumed to be CN(0, 1), where CN(0, 1) denotes
the standard circularly symmetric complex Gaussian random
variable. An interleaver with sufﬁciently large block length is
assumed to make the block fading channel appear as a fading
channel with independent fade coefﬁcients for successive
channel uses. At R, after deinterleaving, an ML decoder using
the Viterbi algorithm is used to decode the bits (Fig. 2(a)).
Let PR denote the path in the trellis to which R decodes. At
D, the received complex numbers are deinterleaved and stored
(Fig. 2(a)).
During Phase 2, S encodes the same bits used during
Phase 1 and R encodes the bits it decoded during Phase 1,
using the TCM encoder. The encoded bits at S and R are
mapped onto complex symbols from the signal set S (possibly
with different mappings and also possibly different from the
mapping used at S during Phase 1) and interleaved using the
block interleavers (same as the interleaver used at S during
Phase 1) as shown in Fig. 2(b). Let xi
s2(PS) and xi
r(PR)
denote the symbols transmitted by S and R respectively during
Phase 2, corresponding to the ith branch of the paths PS and
PR, where 1 ≤i ≤L.
The received complex signal sequence at D during Phase 2
is given by,
Y i
d2 = hi
sd2xi
s2(PS) + hi
rdxi
r(PR) + zd2,
where 1 ≤i ≤L. The random variables hi
sd2 and hi
rd
are the independent zero mean circularly symmetric complex
Gaussian fading coefﬁcients associated with the S-D and R-D
links respectively with the corresponding variances given by
σ2
sd and σ2
rd. The additive noise zd2 is CN(0, 1). Throughout,
it is assumed that σ2
sd ≪σ2
rd, due to the proximity of the relay
to the destination than the source to the destination.
During Phase 2, at D the received complex numbers are
deinterleaved and along with the complex numbers stored
during Phase 1 are fed to the proposed near-ML TCM decoder
described in Section III.
B. Background and Related Work
Achievable rates and upper bounds on the capacity for the
discrete memoryless relay channel for the full-duplex and
the more practical half-duplex relay channel were obtained
in [1], [2]. These results were extended for the half duplex
Gaussian relay channel in [3]. Optimal power allocation
strategies to maximize the achievable rate for the Rayleigh
fading relay channel were investigated in [4]. Several protocols
like Amplify and Forward (AF), Decode and Forward (DF),
Compress and Forward (CF) were proposed [5]. Power allo-
cation strategies for the Non Orthogonal DF (NODF) protocol


## Page 3


were discussed in [6]. Non-orthogonal relay protocols offer
higher spectral efﬁciency when compared with orthogonal
relay protocols [7], [8], [9]. Hence, the proposed TCM scheme
in this paper is based on the NODF protocol.
A turbo-coding scheme for the full duplex and more prac-
tical half-duplex relay channels were proposed in [10], [11].
These coding schemes achieve a spectral efﬁciency strictly less
than one bpcu, i.e., they pay in bandwidth. Coding schemes for
the relay channel with bandwidth constraints, which achieve
a spectral efﬁciency greater than or equal to one bpcu are not
reported in the literature, to the best of our knowledge. In this
paper, we propose a Trellis Coded Modulation (TCM) scheme
for the half-duplex relay channel for any spectral efﬁciency
greater than or equal to one bpcu.
Implementation as well as the performance analysis of the
optimal ML decoder for the relay channel operating in the
DF mode is complicated [12], [13]. To solve these problems,
several sub-optimal decoders for uncoded DF scheme were
proposed in [12], [13], [14] and [15]. These problems carry
over to coded communication using DF protocol as well. If
the decoder at D is designed assuming that R always decodes
the bits correctly, the diversity order obtained is dependent on
whether the relay decoded correctly or not. To circumvent this
problem, relay selection strategies [16], fountain codes [17],
Cyclic Redundancy Check (CRC) codes [18] etc. are used. To
solve these problems of ﬁnding a decoder with implementable
complexity and tractable performance analysis, we propose a
near-ML decoder, whose performance at high SNR approaches
the performance of the optimal ML decoder. The form of this
decoder allows a DF scheme in which the relay need not
check whether it has decoded correctly before forwarding the
message. This eliminates the need for embedding CRC bits as
well as the need for feedback from the relay to the source.
Furthermore, the diversity order of the proposed scheme does
not depend on whether the relay decoded correctly or not.
The proposed TCM scheme is different from the Co-
operative Multiple Trellis Coded Modulation (CMTCM)
scheme proposed in [18] in the following aspects:
• The presence of embedded CRC bits and feedback from
R to S is assumed in [18], whereas we make no such
assumptions.
• Interleaving/Deinterleaving
is
not
assumed
in
[18]
whereas we assume interleaving/deinterleaving which
makes the quasi-static fading scenario appear as a fast
fading scenario.
C. Contributions and Organization
The main contributions of this paper are as follows:
• A TCM scheme for the fading relay channel is proposed
which achieves any spectral efﬁciency greater than or
equal to one bpcu.
• A near-ML decoder is obtained for the proposed TCM
scheme. The relay need not check whether it has decoded
correctly before forwarding the message which eliminates
the need for embedded CRC bits as well as the feedback
from the relay to the source.
• The proposed near-ML decoder enables the formulation
of design criteria to maximize the diversity order and the
coding gain.
• Bounds on the PEP are derived for the near-ML decoder
based on which the criteria to maximize the diversity
order and coding gain are obtained.
• The BER vs SNR performance of the near-ML decoder
proposed with a non-ideal S-R link, at high SNR, ap-
proaches the performance of the optimal ML decoder
with an ideal S-R link. This implies that the high SNR
performance of the near-ML decoder for the relay channel
with a non-ideal S-R link approaches the performance of
the optimal ML decoder.
• It is shown that even for the uncoded transmission
scheme, a proper choice of the labelling at S and R
provides a signiﬁcant performance improvement. We give
a good labelling scheme for 2l-PSK signal set, where
l ≥2 is an integer.
• Simulation results show a large gain in the BER vs SNR
performance for the proposed TCM scheme over the
uncoded transmission scheme as well as the TCM scheme
for the direct transmission without the relay.
The organization of the rest of the paper is as follows: In
Section II, the bounds on the ergodic capacity of the fading
relay channel with Gaussian input alphabet are compared with
the capacity bounds when the input is constrained to take
values from a ﬁnite signal set. The description of the near-ML
decoder for the TCM scheme constitutes Section III. In Section
IV, the PEP expressions are derived, based on which the code
design criteria to maximize the diversity order and coding gain
are obtained. In Section V, effect of the choice of the labelling
scheme for the uncoded transmission scheme is discussed and
a good labelling scheme for 2l-PSK constellation is presented.
In Section VI, TCM code design examples are presented.
Simulation results are presented in Section VII.
Notations: For a random variable Xs which takes value
from the set S, we use xs,i to represent the i-th element
of S. Ez[Y ] denotes the expectation of Y with respect to
the random variable z. Throughout, log refers to log2 and
C(a) denotes log(1 + a). Let CN(0, In) denote the stan-
dard circularly symmetric complex Gaussian random vector
of length n. Also let N(0, c) denote the scalar real valued
Gaussian random variable with mean zero and variance c.
For simplicity, distinction is not made between the random
variable and a particular realization of the random variable,
in expressions involving probabilities of random variables. In
some probability expressions involving conditioning of the
fading coefﬁcients, the fact that the probability is conditioned
on the values taken by the fading coefﬁcients is not explicitly
written, as it can be understood from the context. For a set A,
|A| denotes the cardinality of A. For two sets A and B, A∪B
denotes the union of the sets A and B. The superscript (.)T
denotes the transpose operation. The set {x | c(x)} denotes
the set of all values of x for which the condition c(x) is
satisﬁed. ℜ(x) denotes the real part of the complex number


## Page 4


R1 ≜I(Xs1 ; Yr)] = log(Ms1 ) −
1
Ms1
Ms1 −1
X
i1=0
Ezr

log


PMs1 −1
i=0
exp
 −|zr −hsrxs1,i + hsrxs1,i1 |2
exp(−|zr|2)




(1)
R2 ≜I(Xs2 ; Yd2|Xr)] = log(Ms2 ) −
1
Ms2
Ms2 −1
X
i1=0
Ezd2

log


PMs2 −1
i=0
exp  −|zd2 −hsdxs2,i + hsdxs2,i1|2
exp(−|zd2|2)




(2)
R3 ≜I(Xs1 ; Yd1)] = log(Ms1 ) −
1
Ms1
Ms1 −1
X
i1=0
Ezd1

log


PMs1 −1
i=0
exp
 −|zd1 −hsdxs1,i + hsdxs1,i1 |2
exp(−|zd1|2)




(3)
R4 ≜I(Xs2 , Xr; Yd2) = log(Ms2 Mr)
−
1
Ms2Mr
Ms2 −1
X
i1=0
Mr−1
X
j1=0
Ezd2

log


PMs2 −1
i=0
PMr−1
j=0
exp
 −|zd2 −hsdxs2,i −hrdxr,j + hsdxs2,i1 + hrdxr,j1|2
exp(−|zd2|2)




(4)
R5 ≜I(Xs1 ; Yr, Yd1 )] = log(Ms1 ) −
1
Ms1
Ms1 −1
X
i1=0
Ezr,zd1

log


PMs1 −1
i=0
exp  −|zr −hsrxs1,i + hsrxs1,i1 |2 −|zd1 −hsdxs1,i + hsdxs1,i1 |2
exp(−|zr|2 −|zd1|2)




(5)
x. Throughout, ES denotes the average energy in dB of the
signal set S used at the source and the relay. Let Q[.] denote
the complementary CDF of the standard Gaussian random
variable.
II. INFORMATION THEORETIC LIMITS
Throughout this section, the achievable rate of the decode
and forward scheme is taken to be the lower bound on the
capacity and the cut-set bound [1] is taken to be the upper
bound on the capacity.
For the half duplex relay channel, the received signal at R
during Phase 1 is given by,
Yr = hsrXs1 + zr.
The received signal at D during Phase 1 and phase 2 are
given by,
Yd1 = hsdXs1 + zd1;
Yd2 = hsdXs2 + hrdXr + zd2.
where Xs1 and Xs2 denote the symbols transmitted by S
during Phase 1 and Phase 2 respectively, Xr denotes the
symbol transmitted by R during Phase 2. The random variables
zd1, zd2 and zr are independent and CN(0, 1).
For the relay channel with Gaussian input alphabet, the
lower and upper bounds on the capacity are given by [3] [4],
CG
L = 1
2 max
0≤β≤1 min
Ehsr
C  |hsr|2ES
 + Ehsd
C  (1 −β)|hsd|2ES
 ,
Ehsd[C  |hsd|2ES
]
+Ehsd,hrd
h
C

|hsd|2ES + |hrd|2ES + 2
p
β|hsd||hrd|ES
io
;
(6)
CG
U = 1
2 max
0≤β≤1 min

Ehsd,hsr [C
 (|hsd|2 + |hsr|2)ES

]
+ Ehsd

C
 (1 −β)|hsd|2ES

,
Ehsd,hrd
h
C

|hsd|2ES + |hrd|2ES + 2
p
β|hsd||hrd|ES
i
+Ehsd
C  |hsd|2ES
	 .
(7)
To compute the achievable rate bounds with ﬁnite input
constellation, assume Xs1 ∈Ss1, Xs2 ∈Ss2 and Xr ∈Sr,
where Ss1, Ss2 and Sr are signal sets such that |Ss1| = Ms1,
|Ss2| = Ms2 and |Sr| = Mr. Deﬁne R4 = I(Xs1; Yr), R5 =
I(Xs2; Yd2|Xr), R6 = I(Xs1; Yd1), R7 = I(Xs2, Xr; Yd2) and
R8 = I(Xs1; Yr, Yd1). It is assumed that coding schemes in
which all the possible choices for (Xs1, Xs2, Xr) occur with
equal probability only are of interest. This forces the marginal
distributions of Xs1, Xs2, Xr to be independent and uniformly
distributed.
The achievable rate bounds of the half duplex relay channel
with ﬁnite input constellation can be shown to be [19],
CCC
L
= min
 1
2Ehsr [R1] + 1
2 Ehsd [R2] ,
1
2Ehsd [R3] + 1
2Ehsd,hrd [R4]

;
(8)
CCC
U
= min
 1
2Ehsr,hsd [R5] + 1
2Ehsd [R2] ,
1
2Ehsd [R3] + 1
2Ehsd,hrd [R4]

.
(9)
where R1-R5 are given by (1)-(5), shown at the top of this
page.
The expressions for the capacity bounds (6), (7), (8) and (9)
can be evaluated using Monte-Carlo simulations. The plots
for the ES Vs Capacity bounds for the relay channel with
Gaussian alphabet as well as 4-PSK and 8-PSK constellations,
for σ2
sd=0 dB, σ2
sr=15 dB, σ2
rd=15 dB, are shown in Fig. 3.
Fig. 3 also shows the capacity with Gaussian alphabet and
the constellation constrained capacity with 4-PSK signal set
for the direct transmission (S-D link). From Fig. 3, it is clear
that the use of relay can provide signiﬁcant advantage over the
direct transmission. From Fig. 3, we can see that for a spectral
efﬁciency of 1 bpcu, for σ2
sd=0 dB, σ2
sr=15 dB, σ2
rd=15 dB,
the achievable rate using DF scheme for 4-PSK and 8-PSK
input constellations are about 3.5 dB and 1.5 dB away from
that of the Gaussian alphabet. Hence in order to be within 1.5


## Page 5


dB away from the achievable rate of the DF scheme using
Gaussian alphabet, for a spectral efﬁciency equal to 1 bpcu,
8 point signal set needs to be used. Hence, in the proposed
TCM scheme, to achieve a spectral efﬁciency r bpcu, a signal
set with 22r+1 points is used.
Note 1: To achieve a spectral efﬁciency of r bpcu, a total
of 2r bits get transmitted from S to D in the two Phases of
relaying.
The value of ES required for a BER of 10−4 and the
diversity order for the different schemes achieving a spectral
efﬁciency of 1 bpcu are shown in Table I, at the top of the
next page (The details regarding the design of TCM schemes
for the relay channel are presented in Section VI and ES vs
BER plots are given in Section VII. The TCM schemes for the
direct transmission were designed based on the design criteria
for TCM for fading channels [21]). From Table I, it can be
seen that the proposed schemes for the relay channel, which
exploit the fact that the S-R and R-D links are better than
the S-D link, outperform the corresponding schemes for the
direct transmission without relay. From Fig. 3, we see that the
capacity of the direct transmission without relay with 4 PSK
signal set and Gaussian alphabet are respectively 2 dB and 1.5
dB, which are greater than the value of ES (0 dB) required
for the 16 state TCM scheme for the relay channel, for a BER
of 10−4. This means that under the given assumptions, the
proposed 16 state 8 PSK TCM scheme for the relay channel,
will outperform even the best possible coding scheme for the
direct transmission without relay. The claim made above is
valid even for other values of the variances of the fading links,
possibly with a higher number of states if not with 16 states.
−15
−10
−5
0
5
10
15
20
25
0.5
1
1.5
2
2.5
3
ES in dB
Rate in bpcu
 
 
Direct Tx. − Gaussian Alphabet
Direct Tx. − 4 PSK
Relay Channel − Gaussian Alphabet− Lower Bound
Relay Channel − Gaussian Alphabet− Upper Bound
Relay Channel − 4 PSK − Lower Bound
Relay Channel − 4 PSK − Upper Bound
Relay Channel − 8 PSK − Lower Bound
Relay Channel − 8 PSK − Upper Bound
Fig. 3.
Rate vs ES for Half Duplex relay Channel with σ2
sd=0 dB, σ2
sr=15
dB, σ2
rd=15 dB
III. A NEAR-ML TCM DECODER
The trellis used for decoding at D is constructed as described
in the following subsection. The reason why the decoding
trellis is of the form described will be clear by the end of
Subsection B of this section.
Fig. 4.
4-PSK signal set
Fig. 5.
Trellises TS1, TR and TS2
Fig. 6.
Trellis TD used for decoding at D


## Page 6


TABLE I
COMPARISON OF DIFFERENT SCHEMES FOR A SPECTRAL EFFICIENCY OF 1 BPCU
Scheme
Diversity Order
ES in dB for BER = 10−4
Direct Tx. - BPSK
1
37 dB
Direct Tx. - 2 State TCM
2
18 dB
Direct Tx. - 4 State TCM
3
12 dB
Relay Channel - Uncoded Tx. Scheme
2
12.5 dB
Relay Channel - 2 State TCM
2
8 dB
Relay Channel - 4 State TCM
4
3 dB
Relay Channel - 8 State TCM
4
1.5 dB
Relay Channel - 16 State TCM
6
0 dB
A. Decoding Trellis at D
Let {ai, ai+1} and {bi, bi+1} respectively denote any two
pairs of states in the ith and i + 1th stages of the trellises
TS1 and TR. Let Eai,ai+1 and Ebi,bi+1 denote the sets of edges
from ai to ai+1 and bi to bi+1 respectively.
The trellis used for decoding at D, denoted as TD,
is
constructed
as
follows:
The
states
of
TD
at
the
ith
and
i + 1th
stages
are
denoted
by
the
two
tu-
ples [ai, bi] and [ai+1, bi+1] respectively. The set of edges
from [ai, bi] to [ai+1, bi+1], denoted as E[ai,bi],[ai+1,bi+1],
contains an edge denoted by the pair {eai,ai+1, ebi,bi+1}
if
eai,ai+1
∈
Eai,ai+1
and
ebi,bi+1
∈
Ebi,bi+1.
The
edge {eai,ai+1, ebi,bi+1} is labelled with the four tuple
(Xs1(eai,ai+1), Xs2(eai,ai+1), Xs1(ebi,bi+1), Xr(ebi,bi+1))
∈
S4.
Note 2: Even though encoding at S and R during the two
Phases take place using a total of three trellises, the edges
connecting the states in two successive stages in the trellis
TD are constructed based on the trellises TS1 and TR. The
reason is as follows: The uncoded bits at the input of the TCM
encoders at S during Phase 1 and Phase 2 are the same. Hence,
the encoded paths in the trellises TS1 and TS2 are always the
same (though the complex signal sequences may be different,
due to different labellings) and it is enough to consider one
of the two trellises TS1 and TS2.
Example 1: For the trellis triple {TS1, TS2, TR} (shown in
Fig. 5), labelled with signal points from S (shown in Fig. 4),
the trellis TD is shown in Fig. 6.
The decoding metric for the proposed near-ML decoder is
obtained in the following subsection.
B. Near-ML Decoding Metric
By assumption, R has perfect knowledge about the instanta-
neous value of the fade coefﬁcient associated with the S-R link
and D has perfect knowledge about the instantaneous values
of the fade coefﬁcients associated with the S-R, R-D and S-D
links. Let AL denote the set of all paths of length L in the
trellis (since the TCM encoder used at S during Phase 1, at
S during Phase 2 and at R during Phase 2 are the same, the
set AL is the same for the trellises TS1, TS2 and TR). Let PS
denote the path which corresponds to the symbols transmitted
by the source during Phase 1. Let PR denote the path to which
the Viterbi decoder at R decodes during Phase 1, i.e.,
PR = arg min
P∈AL
L
X
i=1
Y i
r −hi
srxi
s1 (P)
2 .
The optimal ML decoder at D decides in favour of the path,
ˆPS = arg
max
PS∈AL
P r
n
Y 1,L
d1 , Y 1,L
d2 |PS
o
,
where Y 1,L
d1
and Y 1,L
d2
denote the sequences Y 1
d1, Y 2
d1, ...., Y L
d1
and Y 1
d2, Y 2
d2, ...., Y L
d2 respectively and Pr
n
Y 1,L
d1 , Y 1,L
d2 |PS
o
is
the probability that Y 1,L
d1
and Y 1,L
d2
are the received sequences
by D during Phase 1 and Phase 2, given that the path
corresponding to the complex numbers transmitted by S is
PS. The probability which needs to be maximized is given
by,
P r
n
Y 1,L
d1 , Y 1,L
d2 |PS
o
=
X
PR∈AL
P r
n
Y 1,L
d1 , Y 1,L
d2 |PS, PR
o
P r {PR|PS} .
(10)
where Pr
n
Y 1,L
d1 , Y 1,L
d2 |PS, PR
o
is the probability that Y 1,L
d1
and Y 1,L
d2
are the received sequences by D during Phase 1 and
Phase 2, given that the paths corresponding to the complex
numbers transmitted by S and R are PS and PR respectively.
The quantity Pr {PR|PS} is the probability that R decodes
to the path PR given that PS is the path corresponding to the
complex symbols transmitted by S.
The probability Pr {PR|PS} can be upper bounded by the
corresponding PEP, i.e.,
P r {PR|PS} ≤
L
Y
i=1
Q
" hi
sr
 xi
s1 (PR) −xi
s1 (PS)

√
2
#
≤exp
(
−1
4
L
X
i=1
hi
sr
 xi
s1 (PS) −xi
s1 (PR)2
)
,
(11)
and we also have,
P r
n
Y 1,L
d1 , Y 1,L
d2 |PS, PR
o
=
1
π2L exp
(
−
L
X
i=1
Y i
d1 −hi
sd1xi
s1 (PS)

2
+
Y i
d2 −hi
sd2xi
s2 (PS) −hi
rdxi
r (PR)

2
.
(12)


## Page 7


P r
n
Y 1,L
d1 , Y 1,L
d2
|PS
o
≤
1
π2L
X
PR∈AL
exp
(
−
L
X
i=1
Y i
d1 −hi
sd1xi
s1 (PS)

2 +
Y i
d2 −hi
sd2xi
s2 (PS) −hi
rdxi
r (PR)

2 + 1
4
hi
sr

xi
s1 (PR) −xi
s1 (PS)

2)
(13)
φi (PS, PR) =
Y i
d1 −hi
sd1xi
s1 (PS)

2 +
Y i
d2 −hi
sd2xi
s2 (PS) −hi
rdxi
r (PR)

2 + 1
4
hi
sr

xi
s1 (PS) −xi
s1 (PR)

2
(14)
Substituting (11) and (12) in (10) we get (13), shown at the
top of the next page.
If we maximize only the dominant exponential in the upper
bound (13), then the decoded path is given by,
ˆPS = arg
min
PS∈AL
(
min
PR∈AL
L
X
i=1
φi (PS, PR)
)
,
(15)
where the metric φi (PS, PR) is given by (14) (shown at the
top of the next page).
This near-ML decoder given by (15) involves minimizing
the additive metric over two distinct paths and hence the
decoding takes place in the trellis TD described in the previous
subsection. Throughout, it is assumed that decoding at D takes
place using this near-ML decoder.
The branch metric for the Viterbi decoder corresponding to
the edge {eai,ai+1, ebi,bi+1} in TD can be obtained from (14)
and is given by
fi 
eai,ai+1, ebi,bi+1

=
Y i
d1 −hi
sd1Xs1(eai,ai+1)

2
+
Y i
d2 −hi
sd2Xs2(eai,ai+1) −hi
rdXr(ebi,bi+1)

2
+ 1
4
hi
sr

Xs1(eai,ai+1) −Xs1(ebi,bi+1)

2
.
For example, for the edge from state [1, 0] to state [0, 1]
in TD in Example 1, denoted as {e1,0, e0,1}, from Fig. 6,
the four tuple (Xs1(e1,0), Xs2(e1,0), Xs1(e0,1), Xr(e0,1)) is
(s2, s2, s3, s4) and hence the decoding metric is given by,
fi (e1,0, e0,1) =
Y i
d1 −hi
sd1s2

2
+
Y i
d2 −hi
sd2s2 −hi
rds4

2
+ 1
4
hi
sr (s2 −s3)
2 .
Let K denote the number of branches which originate from
each state and let N denote the number of states in the
trellises TS1, TS2 and TR,. In the N 2 state trellis TD, K2
branches originate from a state. As a result, in each step, the
Viterbi algorithm used for decoding involves N 2K2 additions
and N 2 comparisons of K2 values. Hence the decoding
complexity of the proposed near-ML decoder is approximately
2N 2K2/(log2K) operations per decoded bit, since log2 K bits
get transmitted in the two phases of relaying.
IV. PEP ANALYSIS OF THE NEAR-ML DECODER
AND CODE DESIGN CRITERIA
The following Lemma is useful for the PEP analysis of the
near-ML decoder.
Lemma 1: Consider a communication system with one
transmitter and one receiver. The transmitter transmits one
of the two n-dimensional complex vectors x1 and x2 ∈Cn
corresponding to two messages. The received n-dimensional
complex vector y = x + z ∈Cn, where x ∈{x1, x2} and
z is CN(0, In). The decoding rule used at the receiver is
as follows: The decoder decides in favour of message 1, if
||y−x1||2 ≤||y−x2||2+c and it decides in favour of message
2 otherwise, where c ∈R is a constant. Then the probability
that the decoder decides in favour of message 2, given that
message 1 was transmitted is upper bounded as,
Pr (1 −→2) ≤1
2 exp

−||x1 −x2||2
4
−c
2

.
Proof:
We have,
P r (1 −→2) = P r   ||y −x1||2 ≥||y −x2||2 + c | x = x1

= P r

ℜ

y −x1 + x2
2
∗
(x2 −x1)

≥c
2
 x = x1)
= P r

ℜ

z + x1 −x2
2
∗
(x2 −x1)

≥c
2

= P r

ℜ

z∗
x2 −x1
||x2 −x1||

≥
c
2||x2 −x1|| + ||x2 −x1||
2

Since z is CN(0,In), it can be shown that ℜ

z∗x2 −x1
||x2 −x1||

is N

0, 1
2

.
Hence,
P r (1 −→2) = Q
√
2
 ||x1 −x2||
2
+
c
2||x2 −x1||

≤exp
(
−
 ||x1 −x2||
2
+
c
2||x2 −x1||
2)
≤exp

−||x1 −x2||2
4
−c
2

.
A. PEP Analysis of the Near-ML Decoder
In this subsection, an upper bound on the PEP that a
transmitted path PS at S is decoded by the near-ML decoder
at D as ˜PS is derived.
For the trellis TS1, let ηs1(PS, ˜PS) denote the set of values
of i for which xi
s1(PS) and xi
s1( ˜PS) are different, for 1 ≤


## Page 8


i ≤L. Similarly, ηs2(PS, ˜PS) and ηr(PS, ˜PS) are deﬁned for
the trellises TS2 and TR respectively.
Theorem 1: For the proposed TCM scheme, the PEP that a
transmitted path PS in the trellis is decoded as ˜PS, under the
proposed near-ML decoder, is upper bounded by (16) (shown
at the top of the next page).
Proof: The PEP that a transmitted path PS is decoded as
˜PS at D is
P r
n
PS −→˜PS
o
=
X
PR∈AL
P r
n
PS −→˜PS|PR
o
P r {PR|PS} ,
(17)
where PR is the path to which R decodes. The probability
Pr {PR|PS} is upper bounded by (11).
Also,
P r
n
PS −→˜PS|PR
o
= P r
(
min
˜
PR∈AL
L
X
i=1
φi

PS, ˜PR

≥
min
˜
PR∈AL
L
X
i=1
φi( ˜PS, ˜PR)| (PS, PR)
)
.
(18)
Let F1 and F2 be two sets deﬁned as,
F1 =
(
Y 1,L
d1 , Y 1,L
d2

|
min
˜
PR∈AL
L
X
i=1
φi

PS, ˜PR

≥
min
˜
PR∈AL
L
X
i=1
φi( ˜PS, ˜PR)
)
,
F2 =
(
Y 1,L
d1 , Y 1,L
d2

|
L
X
i=1
φi (PS, PR) ≥
min
˜
PR∈AL
L
X
i=1
φi( ˜PS, ˜PR)
)
.
Since F1 ⊂F2, from (18) we have,
P r
n
PS −→˜PS|PR
o
≤P r
( L
X
i=1
φi (PS, PR) ≥
min
˜
PR∈AL
L
X
i=1
φi( ˜PS, ˜PR)| (PS, PR)
)
(19)
Let F3 be the set deﬁned as,
F3 =
[
˜
PR∈AL
(
Y 1,L
d1 , Y 1,L
d2

|
L
X
i=1
φi (PS, PR) ≥
L
X
i=1
φi( ˜PS, ˜PR)
)
.
From (19), noting that F2 ⊂F3 and using the union bound,
we have,
P r
n
PS −→˜PS|PR
o
≤
X
˜
PR∈AL
P r
( L
X
i=1
φi (PS, PR) ≥
L
X
i=1
φi

˜PS, ˜PR

| (PS, PR)
)
.
(20)
The probability inside the summation in (20) can be upper
bounded using Lemma 1. The constant c, the vectors xi, i ∈
{1, 2} and the vector y , deﬁned in Lemma 1, are chosen as
given by (21)-(24) (shown at the top of the next page).
Using Lemma 1 in (20) gives rise to (25) ((25)-(27) are
shown on the next page). Substituting (11) and (25) in (17)
gives (26). Taking expectation in (26) with respect to hi
sd1,
hi
sd2, hi
rd and hi
sr, 1 ≤i ≤L, yields (27) which is the same
as (16).
The criteria to maximize the diversity order of the proposed
TCM scheme is obtained in the following subsection.
B. Diversity Criteria
Fig. 7.
Example illustrating the notion of unmerged length between two
paths
Deﬁnition 1: The unmerged length between the paths P1
and P2 in the trellis, denoted as h(P1, P2) is the number of
branches in which the paths P1 and P2 differ. For example, for
the paths P1 and P2 of length 6 shown in Fig. 7, the unmerged
length h(P1, P2) = 5. The unmerged length of the code is the
minimum value of h(P1, P2), over all possible pairs of paths
(P1, P2) in the trellis.
Note 3: Since the unmerged length between a pair of paths
P1, P2 is the same in all three trellises TS1, TS2 and TR, we
simply refer to it as the unmerged length in the trellis, without
mentioning whether the trellis is TS1, TS2 or TR.
For two paths PS and ˜PS whose unmerged length is equal
to the unmerged length of the code, the ﬁrst term in the
PEP upper bound given by (16) is of diversity order upper
bounded by twice the unmerged length of the code, since
both |ηs1(PS, ˜PS)| and |ηs1(PS, ˜PS)∪ηr(PS, ˜PS)| are upper
bounded by the unmerged length of the code. Hence, the
diversity order of the proposed TCM scheme is upper bounded
by twice the unmerged length of the code. The mappings XS1,
XS2 and XR should be chosen such that this bound is met with
equality.
For two arbitrary paths PS and ˜PS in the trellis, let the
diversity order corresponding to the error event

PS −→˜PS

be denoted as D(PS, ˜PS).
Corollary 1: For the proposed TCM scheme, D(PS, ˜PS) is
bounded as,


## Page 9


P r
n
PS −→˜
PS
o
≤






Y
i∈ηs1 (PS , ˜
PS )


1
1 +
σsd

xi
s1 (PS) −xi
s1( ˜
PS)

2
4


Y
i∈{ηs2 (PS , ˜
PS )∪ηr(PS , ˜
PS )}


1
1 +
σsd

xi
s2 (PS) −xi
s2( ˜
PS)

2 +
σrd

xi
r (PS) −xi
r( ˜
PS)

2
4








+
X
PR∈AL
PR̸=PS
X
˜
PR∈AL
˜
PR̸= ˜
PS






Y
i∈ηs1 (PS , ˜
PS )


1
1 +
σsd

xi
s1 (PS) −xi
s1( ˜
PS)

2
4


Y
i∈{ηs2 (PS , ˜
PS )∪ηr(PR, ˜
PR)}


1
1 +
σsd

xi
s2 (PS) −xi
s2( ˜
PS)

2 +
σrd

xi
r (PR) −xi
r( ˜
PR)

2
4


Y
i∈{ηs1 (PS ,PR)∪ηs1 ( ˜
PS , ˜
PR)}


1
1 +
σsr

xi
s1( ˜
PR) −xi
s1( ˜
PS)

2 +
σsr

xi
s1(PS) −xi
s1(PR)

2
8








(16)
c = 1
4
L
X
i=1
hi
sr

xi
s1( ˜PR) −xi
s1( ˜PS)

2
−
hi
sr
 xi
s1(PR) −xi
s1(PS)
2
(21)
x1 = [h1
sd1x1
s1(PS), h2
sd1x2
s1(PS), ..., hL
sd1xL
s1(PS), h1
sd2x1
s2(PS) + h1
rdx1
rd(PR), h2
sd2x2
s2(PS) + h2
rdx2
rd(PR), ..., hL
sd2xL
s2(PS) + hL
rdxL
rd(PR)]T
(22)
x2 = [h1
sd1x1
s1( ˜PS), h2
sd1x2
s1( ˜PS), ..., hL
sd1xL
s1( ˜PS), h1
sd2x1
s2( ˜PS) + h1
rdx1
rd( ˜PR), h2
sd2x2
s2( ˜PS) + h2
rdx2
rd( ˜PR), ..., hL
sd2xL
s2( ˜PS) + hL
rdxL
rd( ˜PR)]T
(23)
y = [Y 1
d1, Y 2
d1, ..., Y L
d1, Y 1
d2, Y 2
d2, ..., Y L
d2]T
(24)
P r
n
PS −→˜
PS|PR
o
≤
X
˜
PR∈AL
exp
( L
X
i=1

−1
2
hi
sd1

xi
s1 (PS) −xi
s1( ˜
PS)

2
−1
2
hi
sd2

xi
s2 (PS) −xi
s2( ˜
PS)

+ hi
rd

xi
r (PR) −xi
r( ˜
PR)

2
−1
8
hi
sr

xi
s1( ˜
PR) −xi
s1( ˜
PS)

2 + 1
8
hi
sr

xi
s1(PR) −xi
s1(PS)

2
(25)
P r
n
PS −→˜
PS
o
≤
X
PR∈AL
X
˜
PR∈AL
exp
( L
X
i=1

−1
2
hi
sd1

xi
s1 (PS) −xi
s1( ˜
PS)

2 −1
2
hi
sd2

xi
s2 (PS) −xi
s2( ˜
PS)

+ hi
rd

xi
r (PR) −xi
r( ˜
PR)

2
−1
8
hi
sr

xi
s1( ˜
PR) −xi
s1( ˜
PS)

2 −1
8
hi
sr

xi
s1(PS) −xi
s1(PR)

2
(26)
P r
n
PS −→˜
PS
o
≤
X
PR∈AL
X
˜
PR∈AL
L
Y
i=1








1
1 +
σsd

xi
s1 (PS) −(xi
s1( ˜
PS)

2
4




1
1 +
σsd

xi
s2 (PS) −(xi
s2( ˜
PS)

2 +
σrd

xi
r (PR) −xi
r( ˜
PR)

2
4




1
1 +
σsr

xi
s1( ˜
PR) −xi
s1( ˜
PS)

2 +
σsr

xi
s1(PS) −xi
s1(PR)

2
8








(27)
P r

PS −→˜
PS

≤K
Y
i∈ηs1 (PS , ˜
PS )


1
σsd

xis1 (PS) −(xis1( ˜
PS)

2


Y
i∈{ηs2 (PS , ˜
PS )∪ηr(PS , ˜
PS )}


1
σsd

xis2 (PS) −(xis2( ˜
PS)

2
+
σrd

xir (PS) −xir( ˜
PS)

2


(28)


## Page 10


|ηs1(PS, ˜PS)| + |ηs2(PS, ˜PS)| ≤D(PS, ˜PS)
≤min
n
|ηs1(PS, ˜PS)| + |ηs2(Ps, ˜PS) ∪ηr(PS, ˜PS)|,
2|ηs1(PS, ˜PS)| + |ηs2(Ps, ˜PS)|
o
,
(29)
with equality on both the sides if and only if ηr(PS, ˜PS) is a
subset of ηs2(PS, ˜PS).
Proof: From (16), D(PS, ˜PS) is given by,
D(PS, ˜PS) = |ηs1(PS, ˜PS)| +
min
PR, ˜
PR
n
|ηs2(Ps, ˜PS) ∪ηr(PR, ˜PR)|
+|ηs1( ˜PR, ˜PS) ∪ηs1(PR, PS)|
o
,
≥|ηs1(Ps, ˜PS)| +
min
PR, ˜
PR
|ηs2(Ps, ˜PS) ∪ηr(PR, ˜PR)|
+
min
PR, ˜
PR
|ηs1( ˜PR, ˜PS) ∪ηs1(PR, PS)|.
(30)
The quantity |ηs2(Ps, ˜PS) ∪ηr(PR, ˜PR)| attains the min-
imum value, for the case when PR = ˜PR, in which case
ηr(PR, ˜PR) is an empty set, or for the case when the set
ηr(PR, ˜PR) is a subset of ηs2(Ps, ˜PS). In both the cases the
minimum value attained is |ηs2(Ps, ˜PS)|.
The minimum value of |ηs1( ˜PR, ˜PS) ∪ηs1(PR, PS)| equal
to zero is attained when PR = PS and ˜PR = ˜PS.
Hence from (30) we get the lower bound in (29).
The lower bound in (29) is met with equality if both the
minima in (30) are attained for the same choice of the pair
(PR, ˜PR), which occurs if and only if PR = PS, ˜PR = ˜PS
and the the set ηr(PR, ˜PR) is a subset of ηs2(PS, ˜PS). In
other words, equality in (30) occurs if and only if ηr(PS, ˜PS)
is a subset of ηs2(PS, ˜PS).
The choice PR = PS and ˜PR = ˜PS results in,
|ηs2(Ps, ˜PS) ∪ηr(PR, ˜PR)|
+|ηs1( ˜PR, ˜PS) ∪ηs1(PR, PS)| = |ηs2(Ps, ˜PS) ∪ηr(PS, ˜PS)|. (31)
The choice PR = ˜PR = ˜PS results in,
|ηs2(Ps, ˜PS) ∪ηr(PR, ˜PR)|
+|ηs1( ˜PR, ˜PS) ∪ηs1(PR, PS)| = |ηs2(Ps, ˜PS)| + |ηs1(PS, ˜PS)|.
(32)
From (31) and (32) we get the upper bound in (29).
Equality in both the lower and upper bounds of (29) occurs
if and only if ηr(PS, ˜PS) is a subset of ηs2(PS, ˜PS).
Deﬁnition 2: The effective length of a pair of paths
(PS, ˜PS) in the trellis TS1 is deﬁned to be the cardinality
of the set ηs1(PS, ˜PS). The effective length of the trellis TS1
is deﬁned to be minimum among the effective lengths of all
possible pairs of paths (PS, ˜PS). In a similar way, the effective
lengths of the trellises TS2 and TR can be deﬁned.
Deﬁnition 3: The generalized effective length of a pair of
paths (PS, ˜PS) in the trellis pair (TS2, TR) is deﬁned to be
the cardinality of the set
n
ηs2(PS, ˜PS) ∪ηr(PS, ˜PS)
o
.
Note 4: If the labellings Xs2 and Xr are the same, the
generalized effective length of the pair of paths reduces to the
effective length of the pair of paths in the trellis TS2, which is
equal to the effective length of the pair of paths in the trellis
TR.
If Xs1 and Xs2 are chosen such that the effective lengths of
the trellises TS1 and TS2 are equal to the unmerged length of
the code, then for every pair of paths (PS, ˜PS), |ηs1(PS, ˜PS)|
and |ηs2(PS, ˜PS)| are greater than the unmerged length of
the code. In that case, from the lower bound in Corollary 1
and from the fact that the diversity order cannot exceed twice
the unmerged length of the code, it follows that the diversity
order for the proposed scheme is equal to twice the unmerged
length of the code. Hence, a sufﬁcient condition to obtain
maximum diversity order is to maximize the effective lengths of
the trellises TS1 and TS2, independent of the labelling Xr. This
is not surprising, since during Phase 2 the source encodes the
same bits it encoded and transmitted during Phase 1, maximum
diversity order is obtained irrespective of whether the relay
transmits during Phase 2 or not. But since σ2
sd ≪σ2
rd, from
(28) it can be seen that the coding gain is greatly reduced
if the relay does not transmit during Phase 2. It is shown in
the following subsection that the effective length of TR also
should equal the unmerged length of the code to avoid this
reduction in coding gain.
Even though the above condition guarantees maximum
diversity, there is no simple expression for D(PS, ˜PS) (Corol-
lary 1 gives only the upper and lower bounds) and hence it
is not clear which error events contribute to the minimum
diversity order. Proposition 1 below gives the conditions under
which an error event results in the minimum diversity order.
Proposition 1: Assuming that the sufﬁcient condition to
obtain full diversity is satisﬁed, the error event corresponding
to a pair of paths contributes to the minimum diversity order
if and only if the effective length of the pair of paths in TS1
and the generalized effective length of the pair of paths in
(TS2, TR), are equal to the unmerged length of the code.
Proof: Let PS and ¯PS be two paths in the trellis. The
maps XS1 and XS2 are chosen such that the effective lengths
of the trellises TS1 and TS2 are equal to the unmerged length
of the code.
From the lower bound in Corollary 1, D(PS, ¯PS) is greater
than or equal to twice the unmerged length of the code, since
|ηs1(PS, ¯PS)| and |ηs2(PS, ¯PS)| are greater than or equal to
the unmerged length of the code. Equality can occur only
when the set ηr(PS, ¯PS) is a subset of ηs2(PS, ¯PS), and
the effective lengths of the pair (PS, ¯PS) in both the trellises
TS1 and TS2, i.e., |ηs1(PS, ¯PS)| and |ηs2(PS, ¯PS)|, are equal
to the unmerged length of the code. Clearly, ηr(PS, ¯PS) is
not a subset of ηs2(PS, ¯PS), if and only if |ηr(PS, ¯PS) ∪
ηs2(PS, ¯PS)| ⪈|ηs2(PS, ¯PS)|, in which case the generalized
effective length of the pair of paths (PS, ¯PS) in the trellis pair
(TS2, TR) is greater than unmerged length of the code. Hence,
the error event corresponding to a pair of paths give rise to the
minimum diversity order, if and only if the conditions given
in the statement of the Proposition are satisﬁed.


## Page 11


In the rest of the paper, it is assumed that the sufﬁcient
condition to obtain maximum diversity is satisﬁed.
For a pair of paths PS and ˜PS resulting in the minimum
diversity, only the ﬁrst term in (16) gives rise to minimum
diversity order. Neglecting terms of higher diversity order in
(16), we get (28) (shown on the previous to the previous page),
where K is a positive constant.
The criterion to maximize the coding gain is obtained in the
following subsection.
C. Coding Gain Criterion
Let m1(PS, ˜PS) denote the product distance of the pair of
paths (PS, ˜PS) in the trellis TS1, i.e.,
m1(PS, ˜PS) =
Y
i∈ηs1 (PS, ˜
PS)
xi
s1 (PS) −xi
s1( ˜PS)

2
.
Deﬁnition 4: The generalized product distance of the pair
of paths (PS, ˜PS) corresponding to the trellis pair (TS2, TR)
denoted as m2(PS, ˜PS) is deﬁned as,
m2(PS, ˜PS) =
Y
i∈{ηs2 (PS, ˜
PS)∪ηr(PS, ˜
PS)}

γ
xi
s2 (PS) −xi
s2( ˜PS)

2
+
xi
r (PS) −xi
r( ˜PS)

2
,
(33)
where γ = σ2
sd/σ2
rd.
Note 5: If the labelling used for the trellises TR and TS2 are
the same, the generalized product distance of the pair of paths
(PS, ˜PS) corresponding to the trellis pair (TS2, TR), reduces
within a constant scaling factor to the product distance of the
pair of paths (PS, ˜PS) in the trellis TR, which is equal to the
product distance of the pair of paths (PS, ˜PS) in the trellis
TS2.
Deﬁnition 5: Consider the trellis triplet (TS1, TS2, TR). The
combined product distance of the pair of paths (PS, ˜PS),
denoted by m(PS, ˜PS), is deﬁned as the product of the product
distance of the pair of paths (PS, ˜PS) in the trellis TS1 and
the generalised product distance of the pair of paths (PS, ˜PS)
corresponding to the trellis pair (TS2, TR), i.e.,
m(PS, ˜PS) =
h
m1(PS, ˜PS)m2(PS, ˜PS)
i
.
Deﬁnition 6: The combined product distance of the trellis
triplet (TS1, TS2, TR), which is also the coding gain metric de-
noted by G, is deﬁned to be the minimum value of m(PS, ˜PS),
i.e.,
G =
min
(PS, ˜
PS)∈ZP
h
m(PS, ˜PS)
i
.
where ZP denotes the set of all pairs of paths (PS, ˜PS) whose
effective length in TS1 and the generalized effective length in
(TS2, TR) are equal to the unmerged length of the code.
From (28), it can be seen that the combined product distance
of the trellis triplet (TS1, TS2, TR) needs to be maximized, to
maximize the coding gain. For a pair of paths (PS, ˜PS) which
contribute to the minimum diversity order, if the effective
length of (PS, ˜PS) in the trellis TR is not equal to the
unmerged length of the code, then xi
r(PS) = xi
r( ˜PS) for some
i ∈ηr(PS, ˜PS). In that case m2(PS, ˜PS) is greatly reduced
since γ ≪1. In order to avoid this, the effective length of the
trellis TR should be made equal to the unmerged length of the
code.
D. Near Optimality of the Proposed Near-ML decoder
The following argument proves the high SNR near optimal-
ity of the proposed near-ML decoder for the TCM scheme.
Consider the situation where the S-R link is ideal, i.e., the
relay decodes all the bits correctly. The optimal ML decoder
at D decides in favour of the path given by,
ˆPS = arg
min
PS∈AL
 L
X
i=1
Y i
d1 −hi
sd1xi
s1 (PS)

2
+
Y i
d2 −hi
sd2xi
s2 (PS) −hi
rdxi
r (PS)

2
.
For this case, the PEP that the path PS is decoded as ˜PS
is upper bounded by (34) (shown at the top of the next page).
Taking expectation with respect to the fading coefﬁcients, we
get (35) (shown at the top of the next page). From (28) and
(35), we see that the high SNR bounds on the PEP for the
proposed near ML decoder with a non-ideal S-R link is same
as that of the optimal ML decoder with an ideal S-R link, if
we consider only the error events giving rise to the minimum
diversity order. The simulation results presented in Section VII
conﬁrm that the BER vs SNR performance of the proposed
near ML decoder with a non-ideal S-R link approaches the
performance of optimal ML decoder with an ideal S-R link,
at high SNR. The high SNR performance of the optimal ML
decoder for the proposed TCM scheme, with a non-ideal S-R
link cannot be better than that of optimal ML decoder for the
case when the S-R link is ideal. This implies the high SNR
performance of the proposed near-ML decoder approaches the
performance of the optimal ML decoder.
From (28), it is clearly seen that even for the uncoded
transmission scheme, choosing the labelling schemes used at S
and R properly can potentially yield a signiﬁcant performance
improvement. The effect of the choice of labelling on the
performance for the uncoded transmission scheme is discussed
in the following section.
V. THE UNCODED TRANSMISSION SCHEME
Consider the uncoded transmission scheme in which bits
are directly mapped onto complex symbols at S and R. A
collection of log2M bits constitutes a message. Let M =
{1, 2, ..., M} denote this message set. The uncoded transmis-
sion scheme has an equivalent one state trellis representa-
tion, with M edges connecting two successive stages. The
unmerged length between every pair of distinct paths is one
and hence no distinction needs to be made between paths and
edges. The index i in the transmitted complex numbers xi
s1(.),
xi
s2(.) and xi
r(.) can be dropped and they are the same as the


## Page 12


P r
n
PS −→˜
PS
o
≤exp
( L
X
i=1

−1
2
hi
sd1

xi
s1 (PS) −(xi
s1( ˜
PS)

2 −1
2
hi
sd2

xi
s2 (PS) −(xi
s2( ˜
PS)

+ hi
rd

xi
r (PS) −xi
r( ˜
PS)

2)
(34)
P r

PS −→˜
PS

≤K
Y
i∈ηs1 (PS , ˜
PS )


1
σsd

xis1 (PS) −(xis1( ˜
PS)

2


Y
i∈{ηs2 (PS , ˜
PS )∪ηr(PS , ˜
PS )}


1
σsd

xis2 (PS) −(xis2( ˜
PS)

2
+
σrd

xir (PS) −xir( ˜
PS)

2


(35)
labellings on the edges Xs1(.), Xs2(.) and Xr(.). Each path
(edge) in the trellis is identiﬁed by the message a ∈M which
gets transmitted.
Corollary 2: For the uncoded transmission scheme, the PEP
that the decoder at D decides in favour of message ¯a ∈M
given that the message transmitted by the source was a ∈M
is upper bounded as,
P r (a −→¯a) ≤


1
1 + 1
4 |σsd|2|xs1(a) −xs1(¯a)|2




1
1 + 1
4 |σsd|2|xs2(a) −xs2(¯a)|2 + 1
4|σrd|2|xr(a) −xr(¯a)|2


+ H.O.T.
where H.O.T denotes the terms of diversity order greater than
2.
Proof: From (16), replacing the paths PS, ˜PS, PR and
˜PR by the corresponding message indices, we get (36) (shown
at the top of the next page). Neglecting terms of diversity order
greater than 2 gives the result.
From Corollary 2, it follows that the diversity order of the
uncoded transmission scheme is two and in order to minimise
the PEP, we need to maximize the following:

1 + 1
4|σsd|2|xs1(a) −xs1(¯a)|2


1 + 1
4|σsd|2|xs2(a) −xs2(¯a)|2 + 1
4 |σrd|2|xr(a) −xr(¯a)|2

.
At high SNR we need to maximize the metric,
m(a, ¯a) =|xs1(a) −xs1(¯a)|2

γ|xs2(a) −xs2(¯a)|2 + |xr(a) −xr(¯a)|2
,
over all message pairs (a, ¯a).
By a labelling scheme, we refer to the triplet (Xs1, Xs2, Xr).
Let L denote a labelling scheme used at S and R. Let us deﬁne,
d(L) =
min
a,¯a,a̸=¯a m(a, ¯a),
where a, ¯a ∈M.
Let L0 denote the labelling scheme in which the mapping
from bits to complex symbols, used by S (during Phase 1 and
Phase 2) and R (during Phase 2), are the same. Similar to
d(L), d(L0) can be deﬁned for the labelling scheme L0.
Deﬁnition 7: The Labelling Gain of the labelling scheme
L, which is a measure of the performance gain provided by
L over L0, is given by,
LG(L) = 10 log10
 d(L)
d(L0)

dB.
It is important to note that the Labelling Gain is calculated
based on the upper bound on the PEP, taking into consider-
ation only those pair of messages a and ¯a which contribute
dominantly to the metric m(a, ¯a). The actual high SNR gain
provided by the labelling scheme L over the scheme L0 need
not equal LG(L).
Throughout, the phrase with our labelling means that S and
R use the labelling scheme which is described in the following
subsection and with constant labelling means that S and R use
the labelling scheme L0.
A. A Labelling Scheme for PSK Constellation
In this subsection, we provide a good labelling scheme for
2l-PSK constellation, where l ≥2 is an integer. Let sk =
exp (jk2π/M), where 0 ≤k ≤M −1 and M = 2l, denote
the signal points in the 2l-PSK signal set.
Let ¯L denote the labelling scheme described as follows: The
maps Xs1, Xr and Xs2 are given by,
Xs1(k) = sk,
Xr(k) =
 sk,
if k is even,
s(k+M/2
mod M),
if k is odd,
Xs2(k) = sk,
where 0 ≤k ≤M −1.
Theorem 2: For the labelling scheme ¯L, with 2l-PSK signal
set, the labelling gain, assuming γ ≪1, is approximately given
by,
LG( ¯L) ≈

20 log10

cot(π/2l)

, for l = 2, 3;
20 log10
4 cos2(π/2l) , for l ≥4.
(37)
Proof: Let us deﬁne,
d1(k, k′) = |Xs1(k) −Xs1(k′)|
= | exp(jk2π/M) −exp(jk′2π/M)|
= |1 −exp(j(k′ −k)2π/M)|,
where 0 ≤k, k′ ≤M −1.


## Page 13


P r(a −→¯a) ≤
M
X
l=1






1
1 + |σds
 xs1 (a) −xs1 (¯a) |2
4




1
1 + |σds
 xs2 (a) −xs2 (¯a) |2
4
+ |σdr (xr (a) −xr (l)) |2
4




1
1 + |σrs
 xs1 (¯a) −xs1 (l) |2
8






+
M
X
j=1,j̸=a
M
X
m=1






1
1 + |σds
 xs1 (a) −xs1 (¯a) |2
4




1
1 + |σds
 xs2 (a) −xs2 (¯a) |2
4
+ |σdr (xr (j) −xr (m)) |2
4




1
1 + |σrs
 xs1 (a) −xs1 (j)

|2
8
+ |σrs
 xs1 (¯a) −xs1 (m)

|2
8





(36)
Since d1(k, k′) depends only on |k −k′|, let us denote it by
d1(n), where 0 ≤|k −k′| = n ≤M . Then,
d1(n) = |1 −exp(jn2π/M)|
= 2| sin(πn/M)|,
(38)
where 0 ≤n ≤M. Similarly, let us deﬁne,
d2(n) = |Xr(k) −Xr(k′)|
=

|1 −exp(jn2π/M)|, for n even
|1 + exp(jn2π/M)|, for n odd
=

2| sin(πn/M)|, for n even
2| cos(πn/M)|, for n odd
.
(39)
Since γ ≪1, we have
d( ¯L) ≈min
k̸=k′ |Xs1(k) −Xs1(k′)|2|Xr(k) −Xr(k′)|2
=
min
1≤n≤M d2
1(n)d2
2(n)
=
min
1≤n≤M( min
n even[d2
1(n)d2
2(n)], min
n odd[d2
1(n)d2
2(n)]).
(40)
From (38) and (39) we have,
min
1≤n≤M
n even
[d2
1(n)d2
2(n)] =
min
1≤n≤M
n even
[16 sin4(πn/M)]
= 16 sin4(2π/M)
(41)
and similarly,
min
1≤n≤M
n odd
[d2
1(n)d2
2(n)] =
min
1≤n≤M
n odd
[16 sin2(πn/M) cos2(πn/M)]
= 4 sin2(2π/M).
(42)
Substituting (41) and (42) in (40) we have,
d( ¯L) ≈min[16 sin4(2π/M), 4 sin2(2π/M)].
(43)
Also, we have
d(L0) ≈
min
1≤n≤M d4
1(n)
= 16 sin4(π/M).
(44)
Hence, from (43) and (44), by deﬁnition of LG( ¯L), we have,
LG( ¯L) = 20 log10[min(cot(π/M), 4 cos2(π/M))].
It can be veriﬁed that cot(π/M) ⪈4 cos2(π/M) for M ⪈
12, from which we get (37).
It can be seen from Theorem 2 that for l = 2, the labelling
gain LG( ¯L) ≈0 dB. In other words, for the uncoded transmis-
sion scheme using 4 PSK, using different labelling schemes
at S and R does not provide any performance improvement.
It can be seen that cot(π/2l) for l = 3, and 4 cos2(π/2l) for
l ≥4 are greater than one, whence the approximate value of
LG( ¯L) is greater than 0 dB for l ≥3. Since LG( ¯L) is always
greater than the approximate value given by Theorem 2, for
the uncoded transmission scheme using 2l PSK, using our
labelling scheme provides advantage over constant labelling,
for all l ≥3. Furthermore, since 4 cos2(π/2l) is an increasing
function of l, the labelling gain increases with increasing
size of the PSK constellation. Simulation results presented in
Section VII conﬁrm that the uncoded transmission with our
labelling outperforms the uncoded transmission with constant
labelling.
VI. TCM CODE DESIGN GUIDELINES AND
EXAMPLES
A. TCM Code Design Guidelines
Let the generalized product distance m2(PS, ˜PS) be split
into two parts as,
m2(PS, ˜PS) = m21(PS, ˜PS) + m22(PS, ˜PS),
where the product distances m21(PS, ˜PS) and m22(PS, ˜PS)
are given by,


## Page 14


m21(PS, ˜PS) =
Y
i∈η2(PS, ˜
PS)
xi
r (PS) −xi
r( ˜PS)

2
,
m22(PS, ˜PS) =
Y
i∈η2(PS, ˜
PS)
γ
xi
s2 (PS) −xi
s2( ˜PS)

2
.
Let G1 and G2 be two metrics deﬁned as,
G1 =
min
(PS, ˜
PS)∈YP
h
m1(PS, ˜PS)
i
,
G2 =
min
(PS, ˜
PS)∈ZP
h
m1(PS, ˜PS)m21(PS, ˜PS)
i
,
where YP denotes the set of pairs of paths whose effective
length is equal to the effective length of the trellis TS1.
The code design guidelines are summarized below. Some
of the design rules for TCM for the point to point AWGN and
fading channels ( [20], [21]), carry over for the relay channel
as well.
• Since trellises with parallel transitions limit the effective
length of the trellis to one, they should be avoided.
• Signal points from the signal set should occur with equal
frequency.
• In a trellis with regularity and symmetry, two branches
which emerge from the same state form a part of a pair
of paths which differ by a unmerged length equal to the
unmerged length of the code. Since the coding gain metric
G involves parameters m1(PS, ˜PS), m21(PS, ˜PS) and
m22(PS, ˜PS), which are of the form of product of the
branch Euclidean distances of the pair of paths (PS, ˜PS),
signal points assigned to branches emerging from the
same state should be from the same Ungerboeck partition
[20].
Since γ ≪1, the values of G and G2 are nearly equal and
instead of maximizing G, G2 can be maximized. In the design
examples presented, the choice of Xs1 is made such that the
effective length of TS1 is maximized and the value of G1 is
made large. The choice of Xs2 and Xr are made such that
the effective length of TS2 is maximized and the value of G2
is made large. In the design examples presented, while the
diversity order obtained is maximum, it is not claimed that
the value of G2 for all the cases is maximum. As was the case
with TCM for fading channel, maximizing the coding gain is
a separate problem in itself, as it heavily depends on the trellis
and the signal set used.
B. Code Design Examples
In all the trellis diagrams shown, the labellings on the edges
are shown to the left of each state. The triple inside [.], when
read from left to right, denotes the labellings (Xs1, Xr, Xs2)
corresponding to the edges emerging from top to bottom (the
labellings Xs1, Xr, Xs2 are shown in the same trellis diagram
instead of three different trellis diagrams). In Examples 2,
3, 4 and 5 considered in this subsection, S transmits two
information bits to D in the two phases of relaying.
Example 2: Consider the case where encoding at S and R
take place using a two state trellis (Fig. 9) with 8 PSK signal
Fig. 8.
8-PSK signal set
Fig. 9.
Two State Trellis
set with signal points labelled as shown in Fig. 8. Let δ0,
δ1, δ2 and δ3 denote the ordered squared Euclidean distances
between the points in the 8 PSK signal set, i.e., δ0 = (2 −
√
2) = 0.586, δ1 = 2, δ2 = (2 +
√
2) = 3.414 and δ3 = 4.
Since the unmerged length of the code is equal to one, the
diversity order cannot exceed two. The choice of Xs1 shown
in Fig. 9 results in the value of the effective length of the trellis
TS1 equal to one and maximizes G1. The value of G1 = δ3 = 4.
Choosing Xr and Xs2 same as Xs1 results in the value of the
effective length of TS2 equal to one and maximizes G2. For this
example, the diversity order is 2 and the coding gain metric
G = δ3(δ3 + γδ3) = 16.5056, for γ = 0.0316.
Example 3: Consider the case where encoding at S and R
take place using a four state trellis (Fig. 10) with 8 PSK signal
set. The unmerged length of the code is two and hence the
diversity order cannot exceed four. From [22], the choice of
Xs1 shown in Fig. 10 results in a value of the effective length
of TS1 equal to two and G1 = δ0δ3 = 2.344.
If Xs1, Xs2 and Xr are chosen based on the design criteria
for the fading channel (Jamali et al. labelling [22]), the value
obtained for the metric G2 = (δ0δ3)2 = 5.49. Instead, if the
labellings Xs1, Xs2 and Xr are chosen as shown in Fig. 10 the
value of G2 = δ0δ1δ2δ3 = 16 and the effective length of TS2
equal to two. For this example, the diversity order is 4 and
the coding gain metric G = δ0δ3(δ1δ2 + γδ0δ3) = 16.1735,
for γ = 0.0316.
Example 4: Consider the case where encoding at S and R
take place using an eight state trellis (Fig. 11) with 8 PSK
signal set. For this trellis, the diversity order cannot exceed


## Page 15


Fig. 10.
Four State Trellis
four since the unmerged length of the code is two. From [23],
the choice of Xs1 shown in Fig. 11 (which is the same as
Ungerboeck’s labelling [20]) results in a value of the effective
length equal to two and G1 = δ1δ3 = 8. Choosing Xr and
Xs2 same as Xs1 results in G2 = (δ1δ3)2 = 64 and ensures
that the effective length of in TS2 is equal to two. For this
example, the diversity order is 4 and the coding gain metric
G = (δ1δ3)2(1 + γ) = 66.0224, for γ = 0.0316. Increasing
the number of states from 4 to 8, while it provides an increase
in the coding gain, does not provide diversity advantage.
Fig. 11.
8 State Trellis
Example 5: Consider the case where encoding at S and R
take place using a sixteen state trellis shown in Fig. 12. The
unmerged length of the code is three and hence the diversity
order cannot exceed six. From [22], the choice of Xs1 shown
in Fig. 12 (which is the same as Ungerboeck’s labelling [20])
results in a value of the effective length of TS1 equal to three
and G1 = δ0δ1δ3 = 4.68. Labellings Xr and Xs2 chosen
to be the same as Xs1 result in G2 = (δ0δ1δ3)2 = 21.96
and the effective length of TS2 equal to three. For this
example, the diversity order is 6 and the coding gain metric
G = (δ0δ1δ3)2(1 + γ) = 22.66, for γ = 0.0316.
Fig. 12.
16 State Trellis
In the following example we consider the case where 3 bits
of information get transmitted from S to D in the two phases
of relaying.
Example 6: Consider the case where encoding at S and R
take place using an eight state trellis (Fig. 14) with 16 PSK
signal set whose points are labelled as shown in Fig. 13. For
this trellis the diversity order cannot exceed four, since the
unmerged length of the code is two. The choice of Xs1 shown
in Fig. 14 results in a value of G1 = 0.0892 and ensures that


## Page 16


Fig. 14.
8 State Trellis
Fig. 13.
16 PSK Signal Set
the effective length of TS1 is two.The labellings Xr and Xs2
shown in Fig. 14 result in G2 = 0.1177 and ensures that the
effective length of TS2 is two.For this example, the diversity
order is 4 and the coding gain metric G = 0.1295, for γ = 0.1.
VII. SIMULATION RESULTS
The ES vs BER plots for the different schemes achieving a
spectral efﬁciency of 1 bpcu are shown in Fig. 15, for σ2
sd = 0
dB, σ2
sr = 15 dB and σ2
rd = 15 dB. The diversity order and
the value of ES required at a BER of 10−4 are summarized
in Table I. As observed in the previous section, the uncoded
transmission scheme provides a diversity order 2. We observe
that using a 2 state trellis provides a diversity order 2 as
expected. At a BER of 10−4, the 2 state 8 PSK TCM scheme
provides 4.5 dB gain over the uncoded transmission scheme
using 4 PSK. When the number of states is increased to 4,
−10
−5
0
5
10
15
20
25
30
35
10
−4
10
−3
10
−2
10
−1
 
 
E
S in dB
BER
Direct Tx. − BPSK
Direct Tx. − 2 State TCM
Direct Tx. − 4 State TCM
Relay Channel − Uncoded Tx. Scheme
Relay Channel − 2 State TCM
Relay Channel − 4 State TCM − Our Labelling
Relay Channel − 8 State TCM
Relay Channel − 16 State TCM
Relay Channel − 4 State TCM−Jamali et al Labelling
Fig. 15.
ES vs BER for the uncoded transmission scheme using 4 PSK
and TCM Schemes for σ2
sd = 0 dB, σ2
sr = 10 dB and σ2
rd = 10 dB
we see that the diversity order increases to 4 as predicted and
at a BER of 10−4 a large gain of 9.5 dB is obtained over
the uncoded transmission scheme using 4 PSK. Also, it can
be seen from Fig. 15, it can be seen that the 4 state 8 PSK
scheme with our labelling provides a gain of 0.6 dB over the
case when S and R use Jamali et al. labelling. Increasing the
number of states to 8, from Fig. 15 the diversity order stays


## Page 17


TABLE II
COMPARISON OF UNCODED 8 PSK TRANSMISSION SCHEME AND 16 PSK TCM SCHEMES
Scheme
Diversity Order ES in dB for BER = 10−4
Uncoded Transmission Scheme - 8 PSK - With Constant Labelling
2
20 dB
Uncoded Transmission Scheme - 8 PSK - With Our Labelling
2
18 dB
Relay Channel - 8 State TCM
4
12.5 dB
2
4
6
8
10
12
14
16
18
20
10
−4
10
−3
10
−2
10
−1
E
S in dB
BER
 
 
Relay Channel  − 8 State TCM
Uncoded Transmission Scheme − 8 PSK With Our Labelling
Uncoded Transmission Scheme − 8 PSK With Constant Labelling
Fig. 16.
ES vs BER for the uncoded transmission scheme using 8 PSK
and TCM Schemes for σ2
sd = 0 dB, σ2
sr = 10 dB and σ2
rd = 10 dB
−2
0
2
4
6
8
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
E
S in dB
BER
 
 
4 State TCM − Ideal S−R link
4 State TCM − Non−Ideal S−R link 
Fig. 17.
ES vs BER comparison for the proposed TCM scheme with ideal
and non-ideal S-R links for σ2
sd = 0 dB, σ2
sr = 10 dB and σ2
rd = 10 dB
at 4 but a coding gain of 1.5 dB is obtained over the 4 state
8 PSK TCM scheme. With the 16 state 8 PSK TCM scheme,
a diversity order of 6 is obtained and a gain of 1.5 dB is
obtained over the 8 state 8 PSK TCM scheme. In essence, at
a BER of 10−4, a large gain of 12.5 dB is obtained using the
16 state 8 PSK TCM scheme over the uncoded transmission
scheme using 4 PSK.
Fig. 16 shows the plots comparing the uncoded transmission
scheme using 8 PSK with our labelling and with constant
labelling, and the 8 state 16 PSK TCM scheme, for σ2
sd = 0
dB, σ2
sr = 10 dB and σ2
rd = 10 dB. At a BER of 10−4 the
uncoded transmission scheme using 8 PSK with our labelling
and 8 state 16 PSK TCM provide a gain of 2 dB and 7.5
dB respectively over the 8 PSK uncoded transmission scheme
with constant labelling. The diversity order and the value of
ES required at a BER of 10−4 are summarized in Table II.
Fig. 17 shows the ES vs BER plot for the 4 state 8 PSK
TCM scheme, for the cases where the S-R link is ideal and
non-ideal, for σ2
sd = 0 dB, σ2
sr = 10 dB and σ2
rd = 10 dB. As
observed in Section IV E, the high SNR performance of the
proposed near-ML decoder with non-ideal S-R link approaches
the performance of the optimal ML decoder with an ideal S-R
link.
VIII. DISCUSSION
A TCM scheme for the half duplex fading relay channel was
proposed. A near-ML decoder whose high SNR performance
approaches the performance of the optimal ML decoder was
obtained. Based on the expression for PEP bounds, code
design criteria to maximize the diversity order and coding gain
were formulated. Maximizing the diversity order can be done
by a proper choice of the labellings used at the source during
Phase 1 and Phase 2. A uniﬁed procedure to ﬁnd the labelling
scheme which maximizes the coding gain for all signal sets
and trellises is not known and will be an interesting topic for
further research.
ACKNOWLEDGEMENT
This work was supported partly by the DRDO-IISc program
on Advanced Research in Mathematical Engineering through
a research grant as well as the INAE Chair Professorship grant
to B. S. Rajan.
REFERENCES
[1] T. M. Cover and A. El Gamal, “Capacity theorems for the relay channel”,
IEEE Trans. on Inform. Theory, vol. 25, no. 5, pp. 572–584, Sep. 1979.
[2] M. A. Khojastepour, A. Sabharwal, and B. Aazhang, “On the capacity of
cheap relay networks”, Conference on Information Sciences and Systems,
Baltimore, USA, March 2003.
[3] M. A. Khojastepour, A. Sabharwal, and B. Aazhang, “On the capacity of
cheap relay networks”, IEEE GLOBECOM, USA, December 2003.


## Page 18


[4] A. Host-Madsen and J. Zhang, “Capacity bounds and power allocation
for wireless relay channels”, IEEE Trans. on Inform. Theory, vol. 51, no.
6, pp. 2020-2040, June 2005.
[5] Gerhard Kramer, Michael Gastpar and Piyush Gupta, “Cooperative Strate-
gies and Capacity Theorems for Relay Networks”, IEEE Trans On Inform.
Theory, Vol. 51, NO. 9, Ssptember 2005.
[6] Zhang Yong, Xu YouYun and Cai YueMing, “Power allocation for non-
orthogonal decode and forward cooperation protocol”, Sci China Ser F-Inf
Sci, 2009, 52: 1037-1042.
[7] R. Nabar, H. Bolcskei, and F. W. Kneubhler, “Fading relay channels:
Performance limits and space-time signal design”, IEEE J. Sel. Areas
Commun., vol. 22, pp. 1099-1109, Aug. 2004.
[8] K. Azarian, H. E. Gamal, and P. Schniter, “On the achievable diversity
multiplexing tradeoff in half-duplex cooperative channels”, IEEE Trans.
Inf. Theory, vol. 51, pp. 4152-4172, Dec 2005.
[9] P. Elia, K. Vinodh, M. Anand, and P. V. Kumar, ”D-MG Tradeoff and
Optimal Codes for a Class of AF and DF Cooperative Communication
Protocols”, ISIT 2007, pp. 681-685.
[10] Z. Zhang and T. M. Duman, “Capacity-approaching turbo coding and
iterative decoding for relay channels”, IEEE Trans. Commun., vol. 53, no.
11, pp. 1895-1905, Nov. 2005.
[11] Z. Zhang and T. M. Duman,, “Capacity-approaching turbo coding for
half-duplex relaying”, IEEE Trans. Commun., vol. 55, no. 10, pp. 1895-
1906, Oct. 2007.
[12] Andrew Sendonaris, Elza Erkip and Behnaam Aazhang, “User Coopera-
tion Diversity Part II: Implementation Aspects and Performance Analysis”,
IEEE Transactions on Communications, Vol. 51, No. 11, November 2003.
[13] Tairan Wang, Alfonso Cano, Georgios B. Giannakis and J. Nicholas
Laneman, “High-Performance Cooperative Demodulation With Decode-
and-Forward Relays”, IEEE Transactions on Communications, Vol. 55,
No. 7, July 2007.
[14] Deqiang Chen and J. Nicholas Laneman, “Modulation and Demodula-
tion for Cooperative Diversity in Wireless Systems”, IEEE Transactions
On Wireless Communications, Vol. 5, No. 7, July 2006.
[15] Xianglan Jin, Dong-Sup Jin, Jong-Seon No, Dong-Joon Shin, “On
the Diversity Analysis of Decode-and-Forward Protocol With Multiple
Antennas”, ISIT 2009, Seoul, South Korea.
[16] R. Tannious and A. Nosratinia, “Spectrally-efﬁcient relay selection with
limited feedback”, IEEE J. Select. Areas Commun., vol. 26, no. 8, pp.
1419 1428, Oct. 2008.
[17] Xi Liu, Teng Joon Lim, “Fountain codes over fading relay channels”,
IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, VOL. 8,
NO. 6, JUNE 2009.
[18] Jialing Li and Andrej Stefanov, “Cooperative Multiple Trellis Coded
Modulation”,IEEE Transactions On Communications, Vol. 57, No. 3,
March 2009.
[19] Vijayvaradharaj T. Muralidharan and B. Sundar Rajan, “Bounds on
the Achievable Rate for the Fading Relay Channel with Finite Input
Constellations,” available online at arXiv: http://arxiv.org/abs/1102.4272
[cs.IT], 21 Feb. 2011.
[20] Ungerboeck G,“Channel coding with multilevel/phase signals”, IEEE
Transactions On Information Theory, Jan 1982.
[21] Dariush Divsalar, “The Design of Trellis Coded MPSK for Fading
Channels: Performance Criteria”, IEEE Transactions On Communications,
Vol. 36, No. 9, September 1988.
[22] S. Hamidreza Jamali and Ngoc Tho Le,“Coded-modulation techniques
for fading channels”,Kluwer Acdemic Publishers 1994.
[23] C. Schlegel and D. J. Costello,Jr.,“Bandwidth efﬁcient coding for fading
channels: Code construction and performance analysis”, IEEE J. Select.
Areas Commun., Vol. SAC-7, pp. 1356-1368, Dec. 1989.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1008.2750v2
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1008.2750v2_On_BICM_receivers_for_TCM_transmission

> Source: 1008.2750v2_On_BICM_receivers_for_TCM_transmission.pdf

> Pages: 28

---


## Page 1


arXiv:1008.2750v2  [cs.IT]  8 Dec 2010
1
On BICM receivers for TCM transmission
Alex Alvarado, Leszek Szczecinski§, and Erik Agrell
Department of Signals and Systems, Communication Systems Group
Chalmers University of Technology, Gothenburg, Sweden
§INRS-EMT, Montreal, Canada
alex.alvarado@chalmers.se, leszek@emt.inrs.ca, agrell@chalmers.se
Abstract
Recent results have shown that the performance of bit-interleaved coded modulation (BICM) using
convolutional codes in nonfading channels can be signiﬁcantly improved when the interleaver takes
a trivial form (BICM-T), i.e., when it does not interleave the bits at all. In this paper, we give a
formal explanation for these results and show that BICM-T is in fact the combination of a TCM
transmitter and a BICM receiver. To predict the performance of BICM-T, a new type of distance spectrum
for convolutional codes is introduced, analytical bounds based on this spectrum are developed, and
asymptotic approximations are also presented. It is shown that the minimum distance of the code is
not the relevant optimization criterion for BICM-T. Optimal convolutional codes for different constrain
lengths are tabulated and asymptotic gains of about 2 dB are obtained. These gains are found to be
the same as those obtained by Ungerboeck’s one-dimensional trellis coded modulation (1D-TCM), and
therefore, in nonfading channels, BICM-T is shown to be asymptotically as good as 1D-TCM.
Index Terms
Bit-interleaved Coded Modulation, Binary Reﬂected Gray Code, Coded Modulation, Convolutional
Codes, Interleaver, Quadrature Amplitude Modulation, Pulse Amplitude Modulation, Set Partitioning,
Trellis Coded Modulation.
This work was partially supported by the European Commission under projects NEWCOM++ (216715) and FP7/2007-
2013 (236068), and by the Swedish Research Council, Sweden (2006-5599). When this work was submitted for publication,
L. Szczecinski was on sabbatical leave with CNRS, Laboratory of Signals and Systems, Gif-sur-Yvette, France. Parts of this
work will be presented at the Allerton Conference on Communication, Control, and Computing, IL, USA, September 2010.
August 27, 2018
DRAFT


## Page 2


2
I. INTRODUCTION
Coded modulation (CM) was introduced in 1974 when Massey proposed the idea of jointly
designing the channel encoder and modulator [1]. This inspired Ungerboeck’s trellis coded
modulation (TCM) [2], and Imai and Hirakawa’s multilevel coding [3]. Bit-interleaved coded
modulation (BICM) [4]–[6] appeared in 1992 as an alternative for CM in fading channels. One
particularly appealing feature of BICM is that all the operations are bit-wise, i.e., off-the-shelf
binary codes and Gray-mapped constellations are used at the transmitter’s side and connected
via a bit-level interleaver. At the receiver’s side, reliability metrics for the coded bits (L-values)
are calculated by the demapper, de-interleaved, and then fed to a binary decoder. This structure
gives the designer the ﬂexibility to choose the modulator and the encoder independently, which
in turn allows, for example, for an easy adaptation of the transmission to the channel conditions
(adaptive modulation and coding). This ﬂexibility is arguably the main advantage of BICM over
other CM schemes, and also the reason of why it is used in almost all of the current wireless
communications standards, e.g., HSPA, IEEE 802.11a/g, IEEE 802.16, and DVB-S2 [6, Ch. 1].
Bit-interleaving before modulation was introduced in Zehavi’s original paper [4] on BICM.
Bit-interleaving is indeed crucial in fading channels since it guarantees that consecutive coded
bits to be sent over symbols affected by independent fades. This results in an increase (compared
to TCM) of the so-called code diversity (the suitable performance measure in fading channels),
and therefore, BICM is the preferred alternative for CM in fading channels. BICM can also be
used in nonfading channels. However, in this scenario, and compared with TCM, BICM gives a
smaller minimum Euclidean distance (the proper performance metric in nonfading channels), and
also a smaller constraint capacity [5]. If a Gray labeling is used, the capacity loss is small, and
therefore, BICM is still considered valid option for CM over nonfading channels. However, the
decrease in minimum Euclidean distance makes BICM less appealing than TCM in nonfading
channels.
The use of a bit-level interleaver in nonfading channels has been inherited from the original
works on BICM by Zehavi [4] and Caire et al. [5]. It simpliﬁes the performance analysis of
BICM and is implicitly considered mandatory in the literature. However, the reasons for its
presence are seldom discussed.
Previously, we have shown in [7] how—by using multiple interleavers—the performance
August 27, 2018
DRAFT


## Page 3


3
of BICM can be improved in nonfading channels. Recently, however, it has been shown in
[8] that in nonfading channels, considerably larger gains (a few decibels) can be obtained if
the interleaver is completely removed from the tranceiver’s conﬁgurations. In other words, it
was shown that in nonfading channels BICM without an interleaver performs better than the
conventional conﬁgurations of [4], [5]. The results presented in [8] are solely numerical and an
explanation behind such an improvement is not given. In particular, [8] does not explain why the
obtained gains depend on the constraint length of the convolutional code (CC). Nevertheless, in
[8] some intuitive explanations (using the notion of unequal error protection) and a bit labeling
optimization are presented.
In this paper, we present a formal study of BICM with trivial interleavers (BICM-T) in
nonfading channels, i.e., the BICM system introduced in [8] where no interleaving is performed.
We recognize BICM-T as the combination of a TCM transmitter and a BICM receiver and we
develop analytical bounds that give a formal explanation of why BICM-T with CCs performs
well in nonfading channels. We also introduce a new type of distance spectrum for the CCs which
allows us to analytically corroborate the results presented in [8]. These gains are shown to appear
even for one of the simplest conﬁguration one could think of, i.e., when the constraint length
K = 3 convolutional code with generators (5, 7) is used together with 4-ary pulse amplitude
modulation (PAM). Asymptotic bounds are also developed and used to show that for the (5, 7)
code and 4-PAM, an asymptotic gain of 2.55 dB is obtained compared to an uncoded system
with the same spectral efﬁciency. Motivated by the fact that this gain is the same obtained by
Ungeroboeck’s one-dimensional TCM (1D-TCM), we search and tabulate optimum convolutional
codes for BICM-T. We show that a properly design BICM system without interleaving performs
asymptotically as well as 1D-TCM, and therefore, BICM-T should be considered as a good
alternative for CM in nonfading channels. The main contribution if this paper is to present an
analytical model for BICM-T which is used to explain the results presented in [8] and also to
design a BICM-T system in nonfading channels.
II. SYSTEM MODEL AND PRELIMINARIES
Throughout this paper, we use boldface letters ct = [c1,t, . . . , cL,t] to denote lenght-L row
vectors and capital boldface letters C = [cT
1, . . . , cT
N] to denote matrices, where (·)T denotes
transposition. We use dH(C) to denote the total Hamming weight of the matrix C. We denote
August 27, 2018
DRAFT


## Page 4


4
probability by Pr(·) and the probability density function (pdf) of a random variable Λ by pΛ(λ).
The convolution between two pdfs is denoted by pΛ1(λ) ∗pΛ2(λ) and {pΛ(λ)}∗w denotes the w-
fold self-convolution of the pdf pΛ(λ). A Gaussian distribution with mean value µ and variance
σ2 is denoted by N (µ, σ2), the Gaussian function with the same parameters by ψ(λ; µ, σ) ≜
1
√
2πσ exp(−(λ−µ)2
2σ2 ), and the Q-function by Q(x) ≜
1
√
2π
R ∞
x exp

−u2
2

du. All the polynomial
generators of the convolutional codes (CC) are given in octal notation.
A. System Model
The BICM system model under consideration is presented in Fig. 1. We use a constraint length
K rate R = 1
2 convolutional encoder connected to a 16-ary quadrature amplitude modulation (16-
QAM) labeled by the binary reﬂected Gray code (BRGC) [9]. This conﬁguration is indeed very
simple yet practical yielding a spectral efﬁciency of two bits per real channel use. This example
is not restrictive, of course, yet simpliﬁes the presentation of the main ideas. The generalization
to other modulations and coding rate is naturally possible but would obviously increase the
complexity of notation potentially hindering the main concepts of the analysis presented in this
paper.
The input sequence i = [i1, . . . , iN] is fed to the encoder (ENC) which at each time instant
t = 1, . . . , N generates two coded bits ct = [c1,t, c2,t]. We use the matrix C = [cT
1, . . . , cT
N]
of size 2 × N to represent the transmitted codeword. These coded bits are interleaved by Π,
where the different interleaving alternatives will be discussed in detail in Sec. II-B. The coded
and interleaved bits are then mapped to a 16-QAM symbol, where the 16-QAM constellation is
formed by the direct product of two 4-ary pulse amplitude modulation (4-PAM) constellations
labeled by the BRGC. Therefore, we analyze the real part of the constellation only, i.e., one
of the constituent 4-PAM constellations. The mapper is deﬁned as Φ : {[11], [10], [00], [01]} →
{−3∆, −∆, ∆, 3∆}, where we deﬁne
∆≜1
√
5
(1)
so that the PAM constellation normalized to unit average symbol energy, i.e., Es = 1.
A quick inspection of the BRGC for 4-PAM reveals that the BRGC offers unequal error
protection (UEP) to the transmitted bits depending on their position. In particular, the bit at
August 27, 2018
DRAFT


## Page 5


5
the ﬁrst position (k = 1) receives higher protection1 than the bit at the second position k = 2.
More details about this can be found in [7]. Moreover, for k = 2 a bit labeled by zero (inner
constellation points) will receive a lower protection than a bit labeled by one transmitted in
the same bit position (outer constellation points), and therefore, the binary-input soft-output
(BISO) channel for k = 2 is nonsymmetric. To simplify the analysis, we “symmetrize” the
channel by randomly inverting the bits before mapping them to the 4-PAM symbol, i.e., ˜C =
Π(C) ⊕S, where ⊕represents modulo-2 element-wise addition and the elements of the matrix
S = [sT
1, . . . , sT
N] ∈{0, 1}2×N where st = [s1,t, s2,t] are randomly generated vectors of bits. Such
a scrambling symmetrizes the BISO channel but it does not eliminate the UEP. We note that the
scrambling is introduced only to simplify the analysis, and therefore, it is not shown in Fig. 1
nor used in the simulations. This symmetrization was in fact proposed in [5], and as we will see
in Sec. IV, the bounds developed based on this symmetrization perfectly match the numerical
simulations.
At each time t = 1, . . . , N, the coded and scrambled bits ˜ct are mapped to a symbol xt, where
xt = Φ(˜ct) ∈X and X is the 4-PAM constellation. The symbols xt are sent over an additive
white Gaussian noise (AWGN) channel so the received signal is given by yt = xt + zt, where
zt is a zero-mean Gaussian noise with variance N0/2. The signal-to-noise ratio is deﬁned as
γ ≜Es/N0 = 1/N0. At the receiver’s side, reliability metrics for the bits are calculated by the
demapper Φ−1 in the form of logarithmic-likelihood ratios (L-values) as
˜lk,t = log Pr(˜ck,t = 1|yt)
Pr(˜ck,t = 0|yt).
(2)
Since ˜ck,t = ck,t ⊕sk,t, it can be shown that lk,t = (−1)sk,t˜lk,t, i.e., after “descrambling”, the sign
of the L-values is changed using (−1)sk,t. These L-values are deinterleaved and then passed to
the decoder which calculates an estimate of the information sequence ˆi.
B. The interleaver
Throughout this paper, three interleaving alternatives will be analyzed, cf. the block Π in Fig. 1.
The ﬁrst interleaving alternative is BICM with a single interleaver (BICM-S) introduced in [5].
1The “protection” may be deﬁned in different ways, where probably the simplest one is the bit error probability per bit position
at the demapper’s output.
August 27, 2018
DRAFT


## Page 6


6
It is the most commonly used in the literature and corresponds to an interleaver that randomly
permutes the bits C prior to modulation, where the permutation is random in two “dimensions,”
i.e., it permutes the bits over the bit positions and over time. The second alternative is BICM
with multiple interleavers (M-interleavers, BICM-M) where the interleaver permutes the bits
randomly only over time (and not over the bit positions). This can be seen as a particularization
of the interleaver of BICM-S following an additional constraint: bits from the kth encoder’s
output must be assigned to the kth modulator’s input. BICM-M was formally analyzed in [7]
and in fact corresponds to the original model introduced by Zehavi in [4] (BICM) and Li in [10]
(BICM with iterative decoding, BICM-ID). Recently, M-interleavers have also been proven to
be asymptotically optimum for BICM-ID [11]. The last interleaving alternative, on which this
paper focuses, is BICM with a trivial interleaver (BICM-T), i.e., when the interleaver Π in Fig. 1
is simply not present [8].
When BICM-T is considered, the resulting system is the one shown in Fig. 2. A careful
examination of Fig. 2 reveals that the structure of the transmitter of BICM-T is the same as the
transmitter of Ungerboeck’s one-dimensional TCM [2] or the TCM transmitter in [12, Fig. 4.17].
The transmitter of BICM-T can also be considered a particular case of the so-caled “general
TCM” [13, Fig. 18.11] when k = ˜k (using the notation of [13]) and when the BRGC is used
instead of Ungerboeck’s set-partitioning. The receiver of BICM-T in Fig. 2 corresponds to a
conventional BICM receiver, where L-values for each bit are computed and fed to a soft-input
Viterbi decoder (VD). The difference between this receiver’s structure and a TCM receiver is
that bit-level processing is used instead of a symbol-by-symbol VD. In conclusion, the BICM-T
system introduced in [8] is simply a BRGC-based TCM transmitter used in conjunction with a
BICM receiver. Nevertheless, through this paper, we use the name BICM-T to reﬂect the fact
that this transmitter/receiver structure can be considered as a particular case of the BICM system
in [4], [5], where the interleaver takes a trivial form.
August 27, 2018
DRAFT


## Page 7


7
C. The Decoder
A maximum likelihood sequence decoder (e.g., the VD) chooses the most likely coded se-
quence ˆC using the vector of channel observations y = [y1, . . . , yN] as
ˆC = max
C∈D

log
 Pr{C|y}
	
(3)
= max
C∈D
(
log
 N
Y
t=1
Pr{ct|yt}
!)
,
(4)
where D is the set of all codewords, where to pass from (3) to (4) we used the memoryless
property of the channel. If we assume that the bits [c1,t, c2,t] are independent, we obtain
log
 N
Y
t=1
Pr{ct|yt}
!
= log
 2
Y
k=1
N
Y
t=1
Pr{ck,t|y}
!
.
(5)
Under this independence assumption and by using the relation between an L-value l and the
bit’s probabilities of being b ∈{0, 1}
Pr{b|y} =
ebl
1 + el ,
(6)
we obtain
log
 2
Y
k=1
N
Y
t=1
Pr{ck,t|y}
!
=
2
X
k=1
N
X
t=1
log
 Pr{ck,t|y}

=
2
X
k=1
N
X
t=1
ck,tlk,t −
2
X
k=1
N
X
t=1
log(1 + exp(lk,t)).
(7)
Since the second term in (7) is independent of C, it is irrelevant to the decision of the decoder
in (4). Therefore, the ﬁnal decision of the decoder can be written as
ˆC = max
C∈D
(
2
X
k=1
N
X
t=1
ck,tlk,t
)
.
(8)
In a BICM system with convolutional codes, the decoder is implemented using an off-the-shelf
soft-input VD, which assumes that the bits are independent, and thus, uses the relation in (5)
(i.e., it uses the decision rule in (8)). The relation in (5) is in indeed valid when BICM-S [5]
or BICM-M [4], [7], [11] conﬁgurations are used, since in those cases, the use of a random
interleaver (cf. Sec. II-B) assure that the bits [c1,t, c2,t] are transmitted in different symbols, and
therefore, are affected by different noise realizations.
However, when BICM-T with a soft-input VD is considered, and since the bits [c1,t, c2,t] are
affected by the same noise realization, the relation in (5) does not hold, i.e., the two L-values
August 27, 2018
DRAFT


## Page 8


8
passed to the decoder at any time instant t are not independent. Nevertheless, the decoder treats
the bits as independent and still uses the decision rule in (8). In principle, it would be possible
to design a decoder for BICM-T that takes into account this inconsistency, i.e., a decoder that
does not assume independent bits. However, this is out of the scope of this paper and would also
go against the ﬂexibility offered by BICM. Moreover, we will show in the following section that
even with this inconsistency, BICM-T in nonfading channels outperforms BICM-S and BICM-M.
III. PERFORMANCE EVALUATION
A. BER Performance
Because of the symmetrization of the channel, we can, without loss of generality, assume that
the all-zero codeword was transmitted. We deﬁne E as the set of codewords corresponding to
paths in the trellis of the code diverging from the zero-state at the arbitrarily chosen instant t = t0,
and remerging with it after T trellis stages. We also denote these codewords as E ≜[eT
1, . . . , eT
T],
where et = [e1,t, e2,t]. Then, the bit error rate (BER) can be upper-bounded using a union bound
(UB) as
BER ≤UB ≜
X
E∈E
PEP(E)dH(iE),
(9)
where dH(iE) is the Hamming weight of the input sequence iE corresponding to the codeword
E, and the pairwise error probability (PEP) is given by (cf. (8))
PEP(E) = Pr
(t0+T−1
X
t=t0
 e1,tl1,t + e2,tl2,t

> 0
)
.
(10)
The general expression for the PEP in (10) and the UB in (9) reduce to well-known particular
cases if simplifying assumptions for the distribution of lk,t are adopted.
1) Independent and identically distributed L-values (BICM-S): In BICM-S, the L-values lk,t
passed to the decoder are independent and identically distributed (i.i.d.). They can be described
using the conditional pdf p(λ|b) with b ∈{0, 1} and where the pdf is independent of k and t.
In this case, the PEP in (10) depends only on the Hamming weight of the codeword E, i.e.,
PEP(E) = PEPS(dH(E))
=
Z ∞
0
{p(λ|b = 0)}∗dH(E) dλ.
(11)
August 27, 2018
DRAFT


## Page 9


9
The UB in (9) can be expressed as
UBS =
X
w
PEPS(w)
X
E∈Dw
dH(iE)
(12)
=
X
w
PEPS(w)βC
w,
(13)
where Dw represents the set of codewords with Hamming weight w, i.e., Dw ≜{E ∈E :
dH(E) = w}. To pass from (12) to (13) we group the codewords E that have the same Hamming
weight and add their contributions, which results in the well-known weight distribution spectrum
of the code βC
w. The expression in (13) is the most common expression for the UB for BICM,
cf. [5, eq. (26)], [6, eq. (4.12)].
2) Independent but not identically distributed L-values (BICM-M): In BICM-M, the L-values
passed to the each decoder’s input are independent, however, their conditional pdf depends
on the bit’s position k = 1, 2. Thus, the L-values are modeled by the set of conditional pdfs
{p1(λ|b), p2(λ|b)}. The PEP in this case is given by
PEP(E) = PEPM(wE,1, wE,2)
=
Z ∞
0
{p1(λ|b1 = 0)}∗wE,1 ∗{p2(λ|b2 = 0)}∗wE,2 dλ,
(14)
where wE,k is the Hamming weight of the kth row of E. The UB in (9) can be expressed as
UBM =
X
w1,w2
PEPM(w1, w2)
X
E∈Dw1,w2
dH(iE)
=
X
w1,w2
PEPM(w1, w2)βC
w1,w2,
(15)
where Dw1,w2 is the set of codewords with generalized Hamming weight [w1, w2] (wk in its kth
row), i.e., Dw1,w2 ≜{E ∈E : w1 = wE,1, w2 = wE,2}, and βC
w1,w2 is the generalized weight
distribution spectrum of the code that takes into account the errors at each encoder’s output
separately. The UB in (15) was shown in [7] to be useful when analyzing the UEP introduced
by the binary labeling and also to optimize the interleaver and the code.
3) BICM without bit-interleaving (BICM-T): For BICM-T, yet a different particularization of
(10) must be adopted. Let ΛE be the metric associated to the codeword E and assume without
loss of generality that t0 = t. This metric is a sum of independent random variables, i.e.,
ΛE ≜Λt + Λt+1 + Λt+2 + . . . ,
(16)
August 27, 2018
DRAFT


## Page 10


10
where Λt = e1,tl1,t + e2,tl2,t corresponds to the elements deﬁning the PEP in (10). We then
express the tth metric as
Λt(et, st) =



















0,
if et = [0, 0]
(−1)s1,t˜l1,t,
if et = [1, 0]
(−1)s2,t˜l2,t,
if et = [0, 1]
P2
k=1(−1)sk,t˜lk,t,
if et = [1, 1]
,
(17)
where we use Λt(et, st) to show that Λt depends on the scrambling’s outcome st (through ˜lk,t)
and the error pattern at time t, et.
Since ˜lk,t are random variables (that depend on k and xt), according to (17), there exist
three pdfs that can be used to model the individual metrics in (16). We denote the set of these
three conditional pdfs by {p1(λ|b1), p2(λ|b2), pΣ(λ|b)}, for the three relevant cases deﬁned in
(17), respectively. We note that pΣ(λ|b) is conditioned not only on one bit, but on the pair of
transmitted bits b = [b1, b2], where b1, b2, and b represent the bits c1,t, c2,t, and ct, respectively.
From (16), and due to the independence of the individual metrics, the PEP in (10) can be
expressed as
PEP(E) = PEPT(wE,1, wE,2, wE,Σ)
=
Z ∞
0
{p1(λ|b1 = 0)}∗wE,1 ∗{p2(λ|b2 = 0)}∗wE,2 ∗{pΣ(λ|b = [0, 0])}∗wE,Σ dλ,
(18)
where wE,k is the number of columns in E where only the kth row of E is one, and wE,Σ is the
number columns in E where both entries are equal to one. Clearly
dH(E) = wE,1 + wE,2 + 2wE,Σ.
(19)
Example 1 (Error event at minimum Hamming distance of (5, 7) code): Consider the constraint
length K = 3 optimum distance spectrum convolutional code (ODSCC) with polynomial gener-
ators (5, 7) [14, Table I]. The free distance of the code is dfree
H
= 5, and βC
5 = 1, i.e., there is one
divergent path at Hamming distance ﬁve from the all-zero codeword, and the Hamming weight
of that path is dH(iE) = 1. Moreover, it is possible to show that this codeword is
E =

1
0
1
1
1
1

,
August 27, 2018
DRAFT


## Page 11


11
i.e., dH(E) = 5, wE,1 = 0, wE,2 = 1, and wE,Σ = 2. Also, wE,1 = 2 and wE,2 = 3.
We deﬁne Dw1,w2,wΣ as the set of codewords E with w1 columns such that et = [1, 0], w2
columns with et = [0, 1], and wΣ columns with et = [1, 1], i.e., Dw1,w2,wΣ ≜{E ∈E : w1 =
wE,1, w2 = wE,2, wΣ = wE,Σ}. Using this, the UB expression in (9) for BICM-T is given by
UBT =
X
w1,w2,wΣ
PEPT(w1, w2, wΣ)
X
E∈Dw1,w2,wΣ
dH(iE)
=
X
w1,w2,wΣ
PEPT(w1, w2, wΣ)βC
w1,w2,wΣ,
(20)
where βC
w1,w2,wΣ is a weight distribution spectrum of the code C that not only considers the
generalized weight [w1, w2] of the codewords, but takes into account the temporal behavior,
i.e., it considers the case when et = [1, 1] as a different kind of event. This differs from βC
w1,w2,
where such an event will be simply considered as an extra contribution to the total generalized
weight.
B. PDF of the L-values
In order to calculate the PEP for BICM-T in (18) we need the compute the set of conditional
pdfs {p1(λ|b1), p2(λ|b2), pΣ(λ|b)}. In this subsection we show how to ﬁnd approximations for
these PDFs.
The L-values in (2) can be expressed as
˜lk,t = log
P
x∈Xk,1 p(yt|x)
P
x∈Xk,0 p(yt|x),
(21)
where Xk,b is the set of constellation symbols labeled with b at bit position k. Using the fact that
the channel is Gaussian and if the so-called max-log approximation log(ea + eb) ≈max{a, b}
is used, the L-values can be expressed as
˜lk,t(yt|st) ≈γ

min
x∈Xk,0(yt −x)2 −min
x∈Xk,1(yt −x)2

,
(22)
where from now on we use the notation ˜lk,t(yt|st) to emphasize that the L-values depend on the
received signal and the scrambler’s outcome st. In fact, the L-values depend on the transmitted
symbol xt, however, and since ct = 0 and no interleaving is performed, xt is completely
determined by st.
The L-value in (22) is a piece-wise linear function of yt. Moreover, the L-values Λt(et, st) in
(17) are linear combinations of ˜lk,t(yt|st) in (22), and therefore, they are also piece-wise linear
August 27, 2018
DRAFT


## Page 12


12
functions of yt. Two cases are of particular interest, namely, when et = [1, 0] or et = [0, 1],
and when et = [1, 1]. The piece-wise linear relationships for ﬁrst case are shown in in Fig. 3 a)
for 4-PAM. In this ﬁgure we also show the constellation symbols and we use the notation
st = [0/1, :] and st = [:, 0/1] to show that for et = [1, 0] and et = [0, 1] the L-values Λt(et, st)
are independent of s2,t and s1,t, respectively. In Fig. 3 b), the four possible cases when et = [1, 1]
are shown.
For a given transmitted symbol xt (determined by st), the received signal yt is a Gaussian
random variable with mean xt and variance N0/2. Therefore, each L-value Λt(et, st) in (17) is a
sum of piece-wise Gaussian functions2. In order to obtain expressions that are easy to work with,
we use the so-called zero-crossing approximation of the L-values proposed in [15, Sec. III-C]
which replaces all the Gaussian pieces required in the max-log model of L-values by a single
Gaussian function. Intuitively, this approximation states that
Λt(yt|et, st) ≈ˆa(et, st)yt + ˆb(et, st),
(23)
where ˆa(et, st) and ˆb(et, st) are the slope and the free coefﬁcient of the closest linear piece to
the transmitted symbol xt.
In Table I we show the values of ˆa(et, st) and ˆb(et, st) deﬁning (23) for 4-PAM, where for
notation simplicity we have deﬁned
α ≜4γ∆2.
(24)
To clarify how these coefﬁcients are obtained, consider for example et = [0, 1]. In this case, for
st = [1, 1], which corresponds to xt = −3∆, the closest linear piece intersecting the x-axis is
the left-most part of the curve labeled in Fig. 3 by et = [0, 1] and st = [:, 1] (dashed-dotted line).
If for example et = [0, 1] and st = [0, 0] (xt = ∆), the closest linear piece is the right-most
piece labeled by et = [0, 1] and st = [:, 0] (dashed line). All the other values in Table I can be
found by a similar direct inspection of Fig. 3.
Using the approximation in (23), the L-values can be modeled as Gaussian random variables
where their mean and variance depend on st, γ, and et, i.e.,
pΛt(λ|et, st) = ψ
 λ; ˆµ(et, st), ˆσ2(et, st)

,
(25)
2Closed-form expressions for these pdfs of Λt(et, st) when et = [1, 0] and et = [1, 0] (cf. Fig. 3 a) were presented in [15].
August 27, 2018
DRAFT


## Page 13


13
where the mean value and variance are given by
ˆµ(et, st) = xtˆa(et, st) + ˆb(et, st)
(26)
ˆσ2(et, st) = [ˆa(et, st)]2N0
2 .
(27)
In Table II we show the obtained mean values and variances for the same cases presented in
Table I.
To obtain the pdf of Λt in (17), we simply average (25) over the symbols, which are assumed
to be equiprobable. This results in the following expression
pΛt(λ) =











1
2

ψ
 λ; −3α, 2α

+ ψ
 λ; −α, 2α

,
if et = [1, 0]
ψ
 λ; −α, 2α

,
if et = [0, 1]
ψ
 λ; −4α, 8α

,
if et = [1, 1]
.
(28)
IV. DISCUSSION AND APPLICATIONS
In the previous section, we developed approximations for the pdf of the L-values passed to the
decoder in BICM-T. In this section we use them to quantify the gains offered by BICM-T over
BICM-S, to deﬁne asymptotically optimum CCs, and to compare BICM-T with Ungerboeck’s
1D-TCM.
A. Performance of BICM-T
Expression (28) show the pdf of the L-values needed to compute the UB of BICM-T, cf. (18)
and (20). Moreover, due to the simpliﬁcations introduced in the previous subsections the results
in (28) only involve Gaussian pdfs, which greatly simpliﬁes the PEP computation in (18).
Theorem 1: The UB for BICM-T is
UBT =
X
w1,w2,wΣ
βC
w1,w2,wΣ
1
2
w1
w1
X
j=0
w1
j

Q
 s
(w1 + w2 + 4wΣ + 2j)2
(w1 + w2 + 4wΣ)
2γ
5
!
.
(29)
Proof: Inserting (28) in (18), changing the convolution of sums into a sum of convolutions,
and using ψ(λ; µ1, σ2
1) ∗. . . ∗ψ(λ; µJ, σ2
J) = ψ(λ; PJ
j=1 µj, PJ
j=1 σ2
j), the PEP in (18) can be
expressed as
PEPT(w1, w2, wΣ) =
Z ∞
0
1
2
w1
w1
X
j=0
w1
j

ψ
 λ; µ1,2,Σ,j, σ2
1,2,Σ

dλ,
(30)
August 27, 2018
DRAFT


## Page 14


14
where
µ1,2,Σ,j = −(w1 + w2 + 4wΣ + 2j)α
(31)
σ2
1,2,Σ = 2(w1 + w2 + 4wΣ)α.
(32)
By using the deﬁnition of α in (24) and ∆in (1), and (31) and (32) in (30), and the UB deﬁnition
in (20), the expression in (29) is obtained.
In Fig. 4, numerical results for BICM-T with 4-PAM labeled with the BRGC and using
the ODSCCs (5, 7) (K = 3) and (247, 371) (K = 8) [14, Table I] are shown. For BICM-
M two conﬁgurations are considered for each code. The ﬁrst one is when all the bits from
the ﬁrst encoder’s output are assigned to the ﬁrst modulator’s input and all the bits from the
second encoder’s output are sent to the second modulator’s input. The second alternative simply
corresponds to the opposite, i.e., all the bits from the ﬁrst encoder’s output are sent over k = 2
and the bits from the second encoder’s output are sent over k = 1. This is equivalent to deﬁning
the code by simply swapping the order of the polynomial generators. For these two particular
codes, the conﬁguration that minimizes the BER for medium to high SNR is the second one,
i.e., when all the bits generated by the polynomial (7) or (371) are sent over k = 1 and all the
bits generated by the polynomial (5) or (247) are sent over k = 2. We denote the conﬁguration
that minimizes (or maximizes) the BER by “Best” (or “Worst”).
To compute the UB for BICM-S and BICM-M, we use the expressions in [7, eq. (22)–(23)],
and for BICM-T we use Theorem 1. All the UB computations were carried out considering a
truncated spectrum of the code, i.e., {w, w1, w2, wΣ} ≤30 which is calculated numerically using
a breadth ﬁrst search algorithm [16]. The results in Fig. 4 show that the UB developed in this
paper for BICM-T predict well the simulation results. Also, these results show that for these
particular codes, the gains obtained by using BICM-M instead of BICM-S are small, although
larger gains were obtained in [7] for other codes/conﬁgurations. On the other hand, the gains by
using BICM-T instead of BICM-S for a BER target of 10−7 are approximately 2 dB for K = 3
and 1 dB for K = 8. Moreover, these gains are obtained by decreasing the complexity of the
system, i.e., by not doing interleaving/de-interleaving.
August 27, 2018
DRAFT


## Page 15


15
B. Asymptotic Performance
In this subsection, we analyze the performance of BICM-T for asymptotically high SNR and
we compare it with BICM-S.
Theorem 2: The asymptotic UB for BICM-T and a given code C can be expressed as
UB′
T = MCQ
 r
2γAC
5
!
,
(33)
where
AC ≜
min
w1,w2,wΣ
βC
w1,w2,wΣ̸=0
(w1 + w2 + 4wΣ)
(34)
MC =
X
w1,w2,wΣ
βC
w1,w2,wΣ̸=0
w1+w2+4wΣ=A
βC
w1,w2,wΣ
1
2
w1
.
(35)
Proof: The UB in (29) is a sum of weighted Q-functions. For high SNR, and for each
(w1, w2, wΣ) there is a Q-function that dominates the the inner sum in (29). This is obtained for
j = 0, which completes the proof.
For comparison purposes, we present here the performance of BICM-S at asymptotically high
SNR. This can be obtained for example by particularizing [7, eq. (25)] to the conventional BICM
conﬁguration with one single interleaver. The asymptotic performance of BICM-S is given by
UB′
S =
3
4
dfree
H
βC
dfree
H Q
 r
2dfree
H γ
5
!
,
(36)
where dfree
H
is the free Hamming distance of the code which can be expressed as dfree
H
= wfree
1
+
wfree
2
+ 2wfree
Σ , cf. (19).
In Fig. 4, we show asymptotic UBs for K = 3. For BICM-T we used Theorem 2, for BICM-
S we use (36), and for BICM-M we use [7, eq. (25)]. All of them are shown to follow the
simulation results quite well. Similar results can be obtained for the code with K = 8, however,
we do not show those results not to overcrowd the ﬁgure.
The asymptotic gain (AG) obtained by using BICM-T instead of BICM-S is obtained directly
from Theorem 2 and (36), as stated in the following corollary.
Corollary 3: The AG obtained by using BICM-T instead of BICM-S
AGS→T = 10 log10

AC
wfree
1
+ wfree
2
+ 2wfree
Σ

.
(37)
August 27, 2018
DRAFT


## Page 16


16
Example 2 (AG for the (5, 7) code): For the particular code (5, 7), it is possible to see that
the solution of (34) corresponds to the event at minimum Hamming distance3, i.e., dfree
H
= 5,
wE,1 = 0, wE,2 = 1, wE,Σ = 2 (cf. Example 1), and therefore, AC = 9. This result in an AG
of 10 log10
  9
5

≈2.55 dB. Moreover, since the input sequence that generates the codeword at
minimum Hamming distance has Hamming weight one (βC
0,1,2 = 1), we obtain MC
0,1,2 = 1 for
the conﬁguration “Worst”. If the polynomials are swapped (which corresponds to swapping the
rows of E), i.e., if we consider the code (7, 5), we obtain wE,1 = 1, wE,2 = 0, wE,Σ = 2 and
the same AC (since AC does not depend on the order of the polynomials). However, in this case
MC
1,0,2 = 1/2. These two asymptotic bounds are shown in Fig. 4, where the inﬂuence of the
coefﬁcient MC can be observed in both numerical results and asymptotic bounds.
C. Asymptotically Optimum Convolutional Codes
Optimum CCs are usually deﬁned in terms of minimum distance, i.e., good CCs are the one that
for a given rate and constraint length have the maximum free distance (MFD) [17, Sec. 8.2.5].
The MFD criterion can be reﬁned if the multiplicities associated to the different weights are
considered [14], [13, Sec. 12.3]. This optimality criterion resulted in the ODSCCs which are
optimal in both binary transmission and in BICM-S, cf. (36). for BICM-M, we have shown in
[7] that dfree
H
is still a good indicator of the optimality of the code (as well as its multiplicity),
however, a generalized weight distribution spectrum of the code should be considered, cf. βC
w1,w2
in (15). If BICM-T is considered, and as a direct consequence of Theorem 2, asymptotically
optimum convolutional codes (AOCCs) can be deﬁned.
Deﬁnition 1 (Asymptotically optimum convolutional codes for BICM-T): A CC is said to be
an AOCC if among all codes with the same K and R = 1/2 it has the highest AC, and among
all codes with the same K and R = 1/2 it has the lowest multiplicity MC.
We have performed an exhaustive numerical search for AOCCs based on Deﬁnition 1. We
considered for constraint lengths K = 3, 4, . . . , 8 and all codes with free distance 0 < dfree
H
≤ˆdfree
H ,
where ˆdfree
H
is the free distance of the ODSCC. The spectrum was truncated as w1 + w2 + 4wΣ ≤
ˆdfree
H +8 and the search was performed in lexicographic order. The results are shown in Table III,
where we also include the ODSCCs for comparison. If there exist more than one AOCC for a
3However, this is not always true for other codes.
August 27, 2018
DRAFT


## Page 17


17
given K, we present the ﬁrst one in the list. These results show that in general the minimum free
distance of the code is not the proper criterion in BICM-T, i.e., codes that are not MFD codes
perform better than the ODSCCs, cf. K = 6, 7. In fact, only for K = 3 the ODSCC is also
optimum for BICM-T4. In this table we also present the AG that BICM-T offers with respect
to BICM-S. The values obtained are around 2 dB.
In Fig. 5, we show the values of AC and MC for all the possible codes with K = 5. This
ﬁgure shows that for K = 5 the AOCC and the ODSCCs have the same asymptotic performance
(same AC), however, the multiplicity of the AOCC is smaller. In Fig. 6, we show similar results
for K = 6, where we only show a subset of all the possible codes. This ﬁgure shows that
for K = 6, the ODSCC gives a worse (smaller AC) asymptotic performance compared to the
AOCC. Moreover, the AOCC code in this case has dfree
H
= 7 while the ODSCC has dfree
H
= 8,
cf. Table III. The same phenomenon occurs for K = 7.
D. BICM-T vs. TCM
As mentioned in Sec. II-B, the transmitter of BICM-T is identical to the transmitter of
Ungerboeck’s 1D-TCM. In this subsection we compare their asymptotic performance.
We have previously deﬁned in (37) the AG of BICM-T over BICM-S. It is also possible to
deﬁne the AG of BICM-T compared to uncoded transmission with the same spectral efﬁciency
(uncoded 2-PAM). Since the minimum squared Euclidean distance of the 2-PAM constellation
is 4, the AG is given by
AGUC→T = 10 log10
AC
5

.
(38)
The AG in (38) is tabulated in the last column of Table III. For K = 3, AGUC→T is equal
to 2.55 dB, which is the same as AGS→T. This is because BICM-S with K = 3 does not offer
any AG compared to uncoded 2-PAM. Analyzing the results in the last column of Table III, we
ﬁnd that they are the same ones obtained by 1D-TCM, cf. [2, Table I]. This simply states that
if BICM-T is used with the correct CC, it performs asymptotically as well as 1D-TCM, and
therefore, it should be considered as good alternative for CM in nonfading channels. However,
this is not the case if BICM-S is used, or if BICM-T is used with the ODSCCs.
4For K = 4 the AOCC (13, 17) has, in fact, the same spectrum βC
w1,w2,wΣ than the ODSCC (15, 17). The AOCC appears
in the list because of the lexicographic order search.
August 27, 2018
DRAFT


## Page 18


18
V. CONCLUSIONS
In this paper, we gave a formal explanation of why gains can be obtained when BICM-T is
used in nonfading channels. BICM-T was shown to be a TCM transmitter used with a BICM
receiver. An analytical model was developed and a new type of distance spectrum for the code
was introduced, which is the relevant characteristic to optimize CCs for BICM-T. The analytical
model was used to validate the numerical results and to show that the use of the ODSCCs, which
rely on the regular minimum free distance criterion, is suboptimal.
For simplicity, the analysis presented in this paper was done only for a simple BICM conﬁg-
uration, and therefore, it is still unknown what the performance gains will be in a more general
setup, e.g., when the number of encoder’s outputs is not the same as the modulator’s input, for
different spectral efﬁciencies, or when a less trivial (but still not inﬁnitely long and random)
interleaver is used. All these questions are left for further investigation.
August 27, 2018
DRAFT


## Page 19


19
REFERENCES
[1] J. L. Massey, “Coding and modulation in digital communications,” in International Z¨urich Seminar on Digital Communi-
cations, Z¨urich, Switzerland, Mar. 1974.
[2] G. Ungerboeck, “Channel coding with multilevel/phase signals,” IEEE Trans. Inf. Theory, vol. 28, no. 1, pp. 55–67, Jan.
1982.
[3] H. Imai and S. Hirakawa, “A new multilevel coding method using error-correcting codes,” IEEE Trans. Inf. Theory, vol. 23,
no. 3, pp. 371–377, May 1977.
[4] E. Zehavi, “8-PSK trellis codes for a Rayleigh channel,” IEEE Trans. Commun., vol. 40, no. 3, pp. 873–884, May 1992.
[5] G. Caire, G. Taricco, and E. Biglieri, “Bit-interleaved coded modulation,” IEEE Trans. Inf. Theory, vol. 44, no. 3, pp.
927–946, May 1998.
[6] A. Guill´en i F`abregas, A. Martinez, and G. Caire, “Bit-interleaved coded modulation,” Foundations and Trends in
Communications and Information Theory, vol. 5, no. 1–2, pp. 1–153, 2008.
[7] A. Alvarado, E. Agrell, L. Szczecinski, and A. Svensson, “Exploiting UEP in QAM-based BICM: Interleaver and code
design,” IEEE Trans. Commun., vol. 58, no. 2, pp. 500–510, Feb. 2010.
[8] C. Stierstorfer, R. Fischer, and J. Huber, “Optimizing BICM with convolutional codes for transmission over the AWGN
channel,” in 2010 International Zurich Seminar on Communications, Zurich, Switzerland, Mar. 2010.
[9] E. Agrell, J. Lassing, E. G. Str¨om, and T. Ottosson, “On the optimality of the binary reﬂected Gray code,” IEEE Trans.
Inf. Theory, vol. 50, no. 12, pp. 3170–3182, Dec. 2004.
[10] X. Li and J. Ritcey, “Bit-interleaved coded modulation with iterative decoding using soft feedback,” Electronic Letters,
vol. 34, no. 10, pp. 942–943, May 1998.
[11] A. Alvarado, L. Szczecinski, E. Agrell, and A. Svensson, “On BICM-ID with multiple interleavers,” IEEE Commun. Lett.,
vol. 14, no. 9, Sep. 2010.
[12] S. H. Jamali and T. Le-Ngoc, Coded-Modulation Techniques for Fading Channels.
Kluwer Academic Publishers, 1994.
[13] S. Lin and D. J. Costello, Jr., Error Control Coding, 2nd ed.
Englewood Cliffs, NJ, USA: Prentice-Hall, Inc., 2004.
[14] P. Frenger, P. Orten, and T. Ottosson, “Convolutional codes with optimum distance spectrum,” IEEE Trans. Commun.,
vol. 3, no. 11, pp. 317–319, Nov. 1999.
[15] A. Alvarado, L. Szczecinski, R. Feick, and L. Ahumada, “Distribution of L-values in Gray-mapped M 2-QAM: Closed-form
approximations and applications,” IEEE Trans. Commun., vol. 57, no. 7, pp. 2071–2079, July 2009.
[16] J. Belzile and D. Haccoun, “Bidirectional breadth-ﬁrst algorithms for the decoding of convolutional codes,” IEEE Trans.
Commun., vol. 41, no. 2, pp. 370–380, Feb. 1993.
[17] J. G. Proakis, Digital Communications, 4th ed.
McGraw-Hill, 2000.
August 27, 2018
DRAFT


## Page 20


FIGURES
20
i
ENC
C
Π(C)
Π
Φ
x
z
y
Φ−1
Π−1
Π(L)
L
DEC
ˆi
Fig. 1.
Model of BICM transmission.
August 27, 2018
DRAFT


## Page 21


FIGURES
21
it
ENC
c1,t
c2,t
Φ
xt
zt
yt
Φ−1
l1,t
l2,t
DEC
ˆit
Fig. 2.
BICM-T system analyzed in this paper for any time instant t.
August 27, 2018
DRAFT


## Page 22


FIGURES
22
∆
∆
3∆
3∆
−∆
−∆
−3∆
−3∆
0
0
−4γ∆2
−4γ∆2
−8γ∆2
−8γ∆2
4γ∆2
4γ∆2
8γ∆2
8γ∆2
a) Cases when et = [1, 0] or et = [0, 1]
b) Cases when et = [1, 1]
et = [1, 0]
et = [1, 0]
st = [0, :]
st = [1, :]
et = [0, 1]
st = [:, 0]
st = [:, 1]
et = [0, 1]
st = [0, 0]
st = [1, 1]
st = [1, 0]
st = [0, 1]
yt
yt
Λt(et, st)
Λt(et, st)
Fig. 3.
Piece-wise relation between the L-values Λt(et, st) in (17) and the received signal yt for 4-PAM for all the possible
values of et and st. The relation for the case when et = [1, 0] or et = [0, 1] is shown in a), and the relation when et = [1, 1]
is shown in b). The transmitted symbols are shown with black squares.
August 27, 2018
DRAFT


## Page 23


FIGURES
23
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
10
−8
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
 
 
SNR γ [dB]
BER
BICM-S [5]
BICM-M (“Best”) [7]
BICM-T (“Worst”)
BICM-T (“Best”)
UBs
Asymptotic UB
K = 3
K = 8
Fig. 4.
BER for BICM using the (5, 7) and (247, 371) ODSCCs [14] and 4-PAM labeled with the BRGC, and for BICM-S
[5], BICM-M [7], and BICM-T. The simulations are shown with markers and the UB with solid lines. The asymptotic UB is
shown with dashed lines.
August 27, 2018
DRAFT


## Page 24


FIGURES
24
0
20
40
60
80
100
120
140
160
180
200
2
4
6
8
10
12
 
 
0
20
40
60
80
100
120
140
160
180
200
10
−2
10
−1
10
0
10
1
 
 
C
C
AC
MC
ODSCC
AOCC
(g1, g2)
(g2, g1)
Fig. 5.
Values of AC and M C for all the possible CCs with K = 5. The ODSCC and the AOCC are shown with ﬁlled markers.
August 27, 2018
DRAFT


## Page 25


FIGURES
25
570
580
590
600
610
620
630
640
650
660
670
0
2
4
6
8
10
12
14
 
 
570
580
590
600
610
620
630
640
650
660
670
10
−1
10
0
 
 
C
C
AC
MC
ODSCC
AOCC
(g1, g2)
(g2, g1)
Fig. 6.
Values of AC and M C for all the possible CCs with K = 6. The ODSCC and the AOCC are shown with ﬁlled markers.
August 27, 2018
DRAFT


## Page 26


TABLES
26
TABLE I
VALUES OF ˆa(et, st) AND ˆb(et, st) IN (23) FOR 4-PAM FOUND BY DIRECT INSPECTION OF FIG. 3.
st = [1, 1]
st = [1, 0]
st = [0, 0]
st = [0, 1]
ˆa(et, st)
ˆb(et, st)
ˆa(et, st)
ˆb(et, st)
ˆa(et, st)
ˆb(et, st)
ˆa(et, st)
ˆb(et, st)
et = [1, 0]
+α/∆
0
+α/∆
0
−α/∆
0
−α/∆
0
et = [0, 1]
+α/∆
+2α
−α/∆
−2α
+α/∆
−2α
−α/∆
+2α
et = [1, 1]
+2α/∆
+2α
+2α/∆
−2α
−2α/∆
−2α
−2α/∆
+2α
August 27, 2018
DRAFT


## Page 27


TABLES
27
TABLE II
VALUES OF ˆµ(et, st) AND ˆσ2(et, st) GIVEN IN (26) AND (27) FOR 4-PAM.
st = [1, 1]
st = [1, 0]
st = [0, 0]
st = [0, 1]
ˆµ(et, st)
ˆσ2(et, st)
ˆµ(et, st)
ˆσ2(et, st)
ˆµ(et, st)
ˆσ2(et, st)
ˆµ(et, st)
ˆσ2(et, st)
et = [1, 0]
−3α
2α
−α
2α
−α
2α
−3α
2α
et = [0, 1]
−α
2α
−α
2α
−α
2α
−α
2α
et = [1, 1]
−4α
8α
−4α
8α
−4α
8α
−4α
8α
August 27, 2018
DRAFT


## Page 28


TABLES
28
TABLE III
AOCCS, ODSCCS, COEFFICIENTS AC AND M C, AND AGS.
K
AOCCs
ODSCCs
AG [dB]
(g1, g2)
dfree
H
AC
M C
(g1, g2)
dfree
H
AGS→T
AGUC→T
3
(7, 5)
5
9
0.50
(5, 7)
5
2.55
2.55
4
(13, 17)
6
10
0.50
(15, 17)
6
2.22
3.01
5
(23, 33)
7
11
0.38
(23, 35)
7
1.96
3.42
6
(45, 55)
7
13
1.62
(53, 75)
8
2.11
4.15
7
(107, 135)
9
14
0.50
(133, 171)
10
1.46
4.47
8
(313, 235)
10
16
8.02
(247, 371)
10
2.04
5.05
August 27, 2018
DRAFT

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]

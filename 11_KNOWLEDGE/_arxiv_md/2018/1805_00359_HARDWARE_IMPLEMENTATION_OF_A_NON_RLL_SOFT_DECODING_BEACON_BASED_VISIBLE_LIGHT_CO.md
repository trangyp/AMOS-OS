---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1805.00359
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1805.00359_Hardware_Implementation_of_A_Non-RLL_Soft-decoding_Beacon-based_Visible_Light_Co

> Source: 1805.00359_Hardware_Implementation_of_A_Non-RLL_Soft-decoding_Beacon-based_Visible_Light_Co.pdf

> Pages: 6

---


## Page 1


Hardware Implementation of A Non-RLL
Soft-decoding Beacon-based Visible Light
Communication Receiver
Duc-Phuc Nguyen†, Dinh-Dung Le†, Thi-Hong Tran†, Huu-Thuan Huynh‡ and Yasuhiko Nakashima†
†Graduate School of Science and Technology, Nara Institute of Science and Technology (NAIST)
630-0192 Takayama-cho, Ikoma-shi, Nara-ken, Japan
Email: (nguyen.phuc.ni6, le.dung.ku9, hong, nakashim)@is.naist.jp
‡Ho Chi Minh City - University of Science
227 Nguyen Van Cu Str., Ward. 4, Dist.5, Ho Chi Minh City - Vietnam, Email: hhthuan@hcmus.edu.vn
Abstract—Visible light communication (VLC)-based beacon
systems, which usually transmit identiﬁcation (ID) information in
small-size data frames are applied widely in indoor localization
applications. There is one fact that ﬂicker of LED light should be
avoid in any VLC systems. Current ﬂicker mitigation solutions
based on run-length limited (RLL) codes suffer from reduced
code rates, or are limited to hard-decoding forward error
correction (FEC) decoders. Recently, soft-decoding techniques
of RLL-codes are proposed to support soft-decoding FEC algo-
rithms, but they contain potentials of high-complexity and time-
consuming computations. Fortunately, non-RLL direct current
(DC)-balance solutions can overcome the drawbacks of RLL-
based algorithms, however, they meet some difﬁculties in system
latency or inferior error-correction performances. Recently, non-
RLL ﬂicker mitigation solution based on Polar code has proved
to be an optimal approach due to its natural equal probabilities of
short runs of 1’s and 0’s with high error-correction performance.
However, we found that this solution can only maintain the DC
balance only when the data frame length is sufﬁciently long.
Accordingly, short beacon-based data frames might still be a big
challenge for ﬂicker mitigation in such non-RLL cases. In this
paper, we introduce a ﬂicker mitigation solution designed for
VLC-based beacon systems that combines a simple pre-scrambler
with a Polar encoder which has a codeword smaller than the
previous work 8 times. We also propose a hardware architecture
for the proposed compact non-RLL VLC receiver for the ﬁrst
time. Also, a 3-bit soft-decision ﬁlter is introduce to enable soft-
decoding of Polar decoder to improve the performance of the
receiver.
Index Terms—Hardware implementation, Non-RLL, Soft-
decoding, Visible Light Communication, Receiver.
I. INTRODUCTION
VLC simultaneously provides both illumination and com-
munication services. VLC system conveys modulated digital
information via a transmit (TX) front-end and light-emitting
diode (LED)’s light. The brightness and stability of the light
are affected by the distribution of the 1’s and 0’s in the data
frames. As a result, ﬂicker mitigation which based on DC-
balance techniques is considered as one of essential concerns
in any VLC systems. In VLC-beacon-based indoor localization
systems, unique ID information are transmitted from VLC-
LED bulbs for purposes such as identifying objects and
locations [1]. Furthermore, beacon-based frames have been
introduced in some publications with the sizes of 158-bit
[1], 56-bit [2] or 34 symbols (0.96ms) [3]. We found that
the 158-bit beacon-based frame which is deﬁned by Standard
of Japan Electronics and Information Technology Industries
Association (JEITA) should be considered in this paper [3],
[4].
Table I summarizes proposals related to FEC and ﬂicker
mitigation for VLC. The conventional solution is deﬁned in
the IEEE 802.15.7 VLC standard and employs Reed-Solomon
(RS) codes, Convolutional Codes (CC) and hard-decoding
RLL (hard-RLL) algorithms [5]. However, the applicability
of hard-RLL methods is limited to hard-decoding FEC codes
[5]–[7]; consequently, the error-correction performance of the
entire system is restricted. Recently, soft-decoding RLL (soft-
RLL) solutions have been proposed in [8]–[11]. These tech-
niques permit soft-decoding FEC algorithms to be applied to
improve the bit-error-rate (BER) performance of VLC systems,
but they also include heavy computational efforts, with many
additions and multiplications. Zunaira et al. have proposed
replacing the classic RLL codes with a recursive Unity-Rate
Code (URC) as the inner code and a 17-subcode IRregular
Convolutional Code (IRCC) as the outer code [12]. Although
this method can achieve a dimming level of approximately
50% with good BER performance, however, the system latency
is increased with the iterative-decoding IRCC-URC scheme.
In addition, the long codeword lengths, which ranges from
1000 to 5000 bits, reduce the compatibility of this proposal
to VLC-based beacon systems in which beacon-based frame
sizes are always small [1], [2] . As an alternative approach,
Kim et al. have proposed two coding schemes based on the
modiﬁed Reed-Muller (RM) codes [7]. Although this method
can guarantee DC balance at exactly 50%, but it has inherent
drawbacks of a low code rate and an inferior error-correction
performance compared with turbo codes, low-density parity-
check (LDPC) codes or polar codes. In addition, Lee and
Kwon have proposed the use of puncturing and pseudo-
noise sequence scrambling with compensation symbols (CSs)
[13]. This proposal can achieve very good BER performance;
however, puncturing with CSs will lead to redundant bits in
arXiv:1805.00359v2  [eess.SP]  30 May 2018


## Page 2


TABLE I
OVERVIEW OF FEC AND FLICKER MITIGATION SOLUTIONS FOR VLC
FEC solution
Flicker mitigation
RS, CC [5]
Hard-RLL
Multi-RS hard-decoding [6]
Hard-RLL
LDPC [14]
Hard-RLL
RS soft-decoding [8], [9]
Soft-RLL
Polar code [10], [11]
Soft-RLL
Irregular CC [12]
Unity-Rate Code
Reed-Muller [7]
Modiﬁed original code
Turbo code [13]
Puncture + Scrambling
Fountain code [15]
Scrambling
Convolutional code, Viterbi [16]
Enhanced Miller code
Polar code (N=2048) [17]
Flicker-free
Pre-scrambled polar code
(JEITA’s beacon frame size),
proposed method (K=158, N=256 )
Flicker-free
the messages, thereby reducing the transmission efﬁciency.
Another coding scheme based on fountain code, with greatly
improved transmission efﬁciency, was mentioned in [15].
However, this scheme requires feedback information and thus
is not suitable for broadcasting scenarios in VLC-based beacon
systems. Recently, Xuanxuan Lu et al. have reported a new
class of enhanced Miller codes, termed eMiller codes which
is a class of RLL codes known for high-bandwidth efﬁciency
[16]. She also proposed an improved version of Viterbi algo-
rithm, termed mnVA to further enhance the performance of her
proposed eMiller. It can be seen from her simulation results
that eMiller helps improve the performance of the whole VLC
system; and this code seems to be a promising for VLC
applications. However, two main drawbacks of this approach
are the code-rate = 1/2 is still not optimized if compared
with non-RLL approaches, and an increasing in computational
complexity.
Advantages of Polar code are exploited deeply together with
soft-decoding of RLL codes have been introduced at [10], [11].
According to these publications, Manchester and 4B6B codes
are used as RLL solutions for the VLC transmitter. As a result,
their BER performances have been improved remarkably with
a ﬂexibility of Polar code’s code-rate. However, we found
that code-rate = 1/2 of Manchester code, or code-rate =
0.67 of 4B6B are not the best optimization solution for
transmission efﬁciency enhancement, if compared with non-
RLL approaches. Moreover, soft-decoding of RLL codes are
time-consuming works which includes multiplication, expo-
nential and logarithm computations. Fang et al. have recently
proposed a non-RLL polar-code-based solution for dimmable
VLC [17]. This approach has shown promising results in
weight distribution and run-length distribution. Moreover, this
solution also show an improved transmission efﬁciency while
achieving a high coding gain compared with RS and LDPC
codes. We have found that this solution can overcome the
drawbacks of related works mentioned above; speciﬁcally, it
SC
Polar 
Decoder
(256,158)
De-
scra
mbler
3-bit 
soft-
decision
Filter
ADC
Low-end
Microcontroller
RX
Front
-end
VLC RECEIVER
Photodiode
id
P2S
Frame
Decaps-
ulation
IDs Creator
TX
Front-end
Pre-scrambled Polar 
Encoder (256,158)
OOK
Mod.
Beacon
Frame 
Creator
id-0
TX
Front-end
TX
Front-end
TX
Front-end
id-1
id-2
id-3
VLC TRANSMITER
Fig. 1. Block diagram of our beacon-based VLC receiver
offers non-iterative decoding, a ﬂexible code rate, and a high
BER performance without requiring feedback information.
However, we also found that the big obstacle of this proposal
is the equal probabilities of short runs of 1’s and 0’s can only
be achieved with a long codeword length; as chosen to be
N=2048. Although, it is stated that, in low-throughput VLC
systems, such as beacon-based ones, long data frames must
be avoided. It is evident that a solution [17] based on a polar
encoder alone is not applicable in such VLC-based beacon
systems because DC balance is not guaranteed for short data
frames. In this paper, we propose a fast-convergence non-RLL
DC-balance scheme based on a pre-scrambled polar encoder.
Consequently, the proposed method can guarantee DC balance
around the range of (41.25%, 63.75%) by a Polar encoder has a
codeword length of N=256 and input frame length equals 158-
bit (JEITA’s beacon-frame length) [3], [4], which is 8 times
shorter than the codeword length of N=2048 required for the
polar-code-based solution proposed in [17]. Furthermore, as
an advantage of the non-RLL solution, our proposal also show
a better code-rate (0.617) compared with RLL related works
mentioned in Table.I.
II. OUR PROPOSED SYSTEM
Our proposed system is presented in Fig.1 in which VLC
transmitter’s functions are processed by a ﬁrmware program
on a low-end micro-controller; while the VLC receiver is
implemented on an FPGA with a novel hardware architecture.
In a digital transmission system, a data scrambler plays an
important role because it causes energy to be spread more
uniformly. At the transmitter, a pseudorandom cipher sequence
is modulo-2 added to the data sequence to produce a scrambled
data sequence.
Describe the generating polynomial P(x) by Eq.1.
P(x) =
N
X
q=0
cq.xq
(1)


## Page 3


where c0 = 1 and equals 0 or 1 for other indexes.
We have found that the output bit probability distributions
(BPD) of the pre-scrambler in different generating polynomi-
als seem to differ slightly. Therefore, we propose a simple
generating polynomial presented in Eq.(2):
P(x) = x15 + x14 + 1
(2)
Meanwhile, Polar codes can be classiﬁed into two types:
non-systematic and systematic codes. Typically, a polar code
is speciﬁed by a triple consisting of three parameters: (N, K, I),
where N is the code length, K is the message length, and I is
the set of information bit indices. Let d be a vector of N bits,
including information bits. The generator matrix is deﬁned as
G = (F ⊗n)I. Then, given a pre-scrambled message u of K
bits in length, a codeword x is generated as Eq.(3).
x = u.G = d.F ⊗n
(3)
Systematic polar codes were introduced to achieve a better
error-correction performance compared with non-systematic
polar codes [18]. A Polar encoder is formed by many layers
of XOR gates, with a complexity of
N
2 log2N XORs. The
output bit probability distribution of a Polar encoder naturally
becomes centralized at approximately 50% 1’s and 50% 0’s
when the codeword length increases [17]. We have selected the
Polar code as the main FEC scheme for our non-RLL VLC
transmitter/receiver for several reasons:
1) Unusual
code
rates
are
supported.
Speciﬁcally,
a
(256;158) polar code, which has a code rate of 0.617, is
suitable for a beacon-based frame size deﬁned by JEITA
K=158 [1], [4].
2) The encoder’s output bit probability distribution is nat-
urally centralized at 50% 1’s and 50% 0’s when code-
length is long enough[17].
3) High error-correction performance can be achieved with
low hardware complexity [19].
4) The inherently short run lengths of a polar encoder can
help mitigate the lighting ﬂicker [17].
Through experiment results, we have found that a pre-
scrambler can help to ensure a fast convergence of the output
probability distribution of an inner (256;158) Polar encoder.
As a result, DC balance in a VLC-based beacon system can
be guaranteed by the proposed system depicted in Fig.1. On-
Off Keying (OOK) modulation is considered because of its
simplicity. Also, at the receiver, we have implemented a soft-
decision ﬁlter which extracts log-likelihood ratio (LLR) values
calculated from received signals’ voltages. Speciﬁcally, in the
case of VLC AWGN channel, the log-likelihood ratio (LLR)
values could be calculated by Eq.(4).
LLR(yi) = ln P(xi = 0|yi)
P(xi = 1|yi)
(4)
where yi is the received sample and the conditional probability
is generally calculated by Eq.(5).
P(xi|yi = ∆) =
1
p
2πσ2
∆
e
−(yi−µ∆)2
2σ2
∆
(5)
TABLE II
3-BIT SOFT-DECISION FILTER’S MAPPING TABLE
Comparator
Range
Output LLR values
0
[Vpeak−; Vt−3]
-1.1943
1
[Vt−3 ; Vt−2]
-0.3547
2
[Vt−2 ; Vt−1]
-0.2116
3
[Vt−1 ; Vt]
-0.0702
4
[Vt ; Vt+1]
0.0656
5
[Vt+1 ; Vt+2]
0.2185
6
[Vt+2 ; Vt+3]
0.3630
7
[Vt+3 ; Vpeak+]
1.2017
where µ∆and σ∆are the mean value and standard deviation
for ∆= 0, 1. However, when making real prototype of soft-
decoding VLC receiver, we found that it is unfeasible in
estimating the LLRs using such Eq.(4) and Eq.(5) due to µ∆
and σ∆can not be estimated in real wireless optical channels.
Therefore, in this paper, we propose applying a soft-decision
ﬁlter which is ﬁrst introduced in optical communication sys-
tems for our prototype of VLC receiver [20]. The analog to
digital converter (ADC) converts received analog signals to
digital signals. The ﬁlter analyses these digital signals and cal-
culate log-likehood ratio (LLR) values to feed to soft-decoding
Polar decoder. The soft-decision ﬁlter includes 2N−1 decision
thresholds to compare with the incoming received signal,
where N is the number of quantization bits. Previous research
on soft-decision ﬁlter in optical communication systems has
shown that 3-bit soft decision was the optimum solution [20].
In the case of N=3 for 3-bit soft decision, seven thresholds
from Vt+3 to Vt−3 are established from the error probabilities
of the two possible received signals 0 and 1. We have deﬁned
a mapping table with output LLR values are carefully chosen
from training simulation results on MATLAB. Table II shows
ranges of comparison and its output LLR values.
III. EXPERIMENTAL RESULTS
In this section, we present evaluations of bit probability
distribution, run-length, BER/FER performances on our pro-
posal. Due to the hardware implementation, we also present
the FPGA and ASIC synthesis results.
A. Centralized bit probability distribution
Regarding the previously proposed non-RLL solution based
only on a polar encoder [17], the authors demonstrated the
ﬂuctuation of the code weight distribution around the 50%
dimming level. Speciﬁcally, in case of a polar encoder has
N=2048, the percentage of 1’s was reported to ﬂuctuate in
the range of (42.1875%, 57.8125%) [17]. However, we have
found that this ﬂuctuation range can only be achieved when the
proportions of 1’s and 0’s in the input data (before the Polar
encoder) are approximately equal 50%. Unfortunately, the bit
ratio of the input data is unknown beforehand because of the
randomness of the data, and this input bit ratio greatly affects
the output bit ratio of the FEC encoder. If the minimum and
maximum bit ratios are included, the real ﬂuctuation range of


## Page 4


Soft-Decision Filter
Parallel to Serial (P2S)
clk
D-FF
D-FF
D-FF
D-FF
D
Q
D
Q
D
Q
D
Q
Scheduling Control
Bit Indicator
FSM
Decoding layers
Encoder selector
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
PE
SUCCESSIVE CANCELATION POLAR DECODER (256,158)
DE-SCRAMBLER
reg
reg
128
64
32
16
8
4
2
D-FF
D
Q
D-FF
D
Q
D-FF
D
Q
Output
Fig. 2. The proposed hardware architecture of non-RLL VLC receiver
photodiode
3-BIT SOFT-DECISION FILTER
Threshold
Adjustment
Comparator 1
SNR
12
4
5
4
iSelect[11:8]
iSelect[7:0]
Comparator 2
Comparator 3
Comparator 4
Comparator 5
Comparator 6
Comparator 7 
ADC
Trans-
former
9
SC
Polar
Decoder
(256;158)
5
5
5
5
5
5
5
oLLR_0
oLLR_1
oLLR_2
oLLR_3
oLLR_253
oLLR_254
oLLR_255
oLLR_252
iData
Comparator 0
Mapping
Lookup-
table
LLR
Fig. 3. The proposed hardware architecture of 3-bit soft-decision ﬁlter
the output bit probability distribution of a polar encoder with
2048-bit codewords is (41.25%, 61.25%). In this paper, we
evaluate our proposed method using a bad case of input bit
ratio which includes 10% of zero bits and 90% of one bits.
A simulation was conducted with 10,000 158-bit data frames.
Both systematic polar encoder (SPE) and non-systematic po-
lar encoder are implemented to evaluate the pre-scrambler.
Regarding with experimental results presented in Fig.4, we
can also see that an NSPE shows a better centralized bit
distribution compared with that of a SPE regardless of whether
pre-scrambling is applied or not. This can be explained is
because the information bits transparently appear as part of
Fig. 4.
Bit-1 output probability distribution in beacon frames (256-bit) in
cases of non-scrambled/scrambled NSPE, SPE
the codeword, the output probability distribution of a SPE is
not well centralized if compared with NSPE’s one. Especially
when a pre-scrambler is not used, the probability distribution
of the SPE tends toward 85% one bits which might affects
strongly on ﬂicker phenomenon. Fig.4 shows the impact of
a pre-scrambler on the output bit probability distribution of
the NSPE and SPE. Notably, DC balance is not guaranteed
in the case of SPE-NSPE(256;158) if a pre-scrambler is not
applied because the encoder’s output bit probability distribu-
tion spreads over a large range of percentages (32.5%, 85%)
in case of NSPE; or (67.5%,100%) in case of SPE. However,
when a pre-scrambler is applied, the ﬂuctuation ranges of the
pre-scrambled (256;158) SPE, NSPE converge to (41.25%,
63.75%), whereas the ﬂuctuation ranges of polar encoders with
codeword lengths of 2048 and 1024 are (41.25%, 61.25%) and
(38.75%, 67.5%), respectively. Thus, pre-scrambling causes
the output bit probability distribution of a (256;158) Polar
encoder to be approximately equal to those of (1024;512) and
(2048;1024) encoders. In other words, considering the frame
size of beacon-based systems, a pre-scrambler is necessary
to ensure faster convergence to a centralized bit probability
distribution. Therefore, compared with the non-RLL DC-
balance solution based only on a polar encoder with 2048-
bit codewords presented in [17], our proposed method can
achieve the same output bit probability distribution with a
shorter codeword length by a factor of 8.
B. Run-length reduction performance
Evaluating the ﬂicker mitigation also requires a considera-
tion on run-length of all frames. In the simulation model, we
have sent 10000 frames of 158-bit with the percentage of bit-0
changes from 0% to 100%. The results have been presented
in Fig.5. Accordingly, the maximum run-lengths are reduced
remarkably in case of the pre-scrambler is applied for Polar
encoders. Speciﬁcally, the maximum run-length reduction gain


## Page 5


Fig. 5. Run-length reduction performance when the pre-scrambler is applied
for NSPE, SPE
that NSPE can achieve is 1.9; while an even better effect
on SPE is the gain of 4.08 when 90% of bit-0 appears in
a data frame. The relationship of maximum run-length and
the transmit frequency that ﬂicker mitigation is guaranteed
can be expressed by Eq.(6). While Fmin−F M is the minimum
frequency that ﬂicker mitigation is guaranteed; maxRL is the
maximum run-length and MFTP is stated around 5 ms [17].
Hence, the minimum frequency that the ﬂicker mitigation in
our proposed system is guaranteed is 2.5 Khz, which is still
much smaller than the minimum frequency deﬁned in [5].
Fmin−F M =
1
MFTP * maxRL
(6)
C. Bit-error-rate (BER), frame-error-rate (FER) performance
Fig.6 shows the BER performances of our work compared
with some related works. We both applied the non-systematic
and systematic Polar codes which have code-rate = 0.617
(256;158) to evaluate the performance. Also, Fig.7 presents the
FER performances of our works. Although systematic Polar
decoder achieves better BER performance than non-systematic
decoder does. However, FER performances of them are the
same for all cases. Besides, It can be noticed that in term of
BER, FER evaluations, our works outperform Bit-level Soft
(BLS) RLL based on Reed-Solomon(RS) code solutions at
code-rates (15/11), (15/7) and (15/3), which are ﬁrst mentioned
in [8]. Furthermore, BER, FER performances of our non-RLL
solution also outperform our previous work which is based on
soft-decoding of 4B6B and Polar code[11]. Besides, we have
selected other typical BER performances which are introduced
in related works [6], [7], [16] to make comparisons with our
proposed receiver (Fig.6).
D. FPGA and ASIC Implementation of proposed VLC receiver
Tab.III and Tab.IV summarize the FPGA and ASIC syn-
thesis results of our non-RLL VLC receiver. The proposed
hardware architecture is deﬁned by Verilog HDL and be ver-
iﬁed by ModelSim. FPGA synthesis process is conducted by
Fig. 6. BER performances of the proposed VLC receiver and some related
works in VLC-AWGN channel
TABLE III
FPGA SYNTHESYS RESULTS OF OUR VLC RECEIVER
Receiver
Polar Decoder
Device
Cyclone IV
Cyclone IV
Model
1200mV 0C
1200mV 0C
Fmax
29.31
28.87
LE/LUT
12134/114480 (10.6%)
10455/114480 (9%)
Registers
3109
1544
Memory bits
1152
0
Altera Quartus II, while ASIC synthesis is done by Synopsys’
Design Compiler. The selected technology library is VDEC
Rohm 180nm. It can be inferred from Tab.III that the Polar
decoder is the largest block of our VLC decoder. In particular,
Polar decoder takes 86% logic resource of the whole receiver.
The frequency of the proposed VLC receiver is also restricted
at 25 Mhz (maximum frequency is 29.31 Mhz) due to the
non-registered decoding architecture of successive cancellation
(SC) Polar decoder. However, the max operation frequency
can be increased by adding more buffering registers in the
processing elements (PEs) network of Polar decoder with
extra complexity and latency. We also estimate the through-
out, energy-per-bit and hardware efﬁciency of the proposed
receiver by Eq.(7)(8)(9), and results are presented in Tab.IV.
Thoughput [b/s] =
N [b]
DN [sec]
(7)
Energy-per-bit [J/b] =
Power [W]
Thoughput [b/s]
(8)
Hardware Efﬁciency [b/s/m2] = Throughput [b/s]
Area [m2]
(9)


## Page 6


Fig. 7. FER performances of the proposed VLC receiver and some related
works in VLC-AWGN channel
TABLE IV
ASIC SYNTHESIS RESULTS OF OUR VLC RECEIVER
Receiver
Technology [nm]
180
Voltage [V ]
1.8
Area [µm2]
573724.56
Frequency [Mhz]
25
Power [mW]
3.5022
Throughput [Mb/s]
16.58
Energy-per-bit [pJ/b]
211.2
Hardware Efﬁciency [Mb/s/mm2]
28.75
Latency [clock]
386
IV. CONCLUSION
We have proposed a non-RLL DC-balance solution con-
sisting of a pre-scrambler based on a simple generating
polynomial combined with a Polar encoder. The proposed
method has a centralized bit probability distribution, with
approximately equal numbers of zero and one bits. Moreover,
the maximum run-length of bit-0 is reduced remarkably when
a pre-scrambler is applied with a Polar encoder. Therefore,
DC-balance can be maintained even with the short data frames
of VLC-based beacon systems. Moreover, the non-RLL nature
of the proposal reduces the complexity of the VLC receiver
with great improvements on information code-rate. Besides,
we also introduced a 3-bit soft-decision ﬁlter which enables
soft decoding of polar decoder can be implemented in real
VLC receiver prototypes to enhance the error-correction per-
formances. Also, BER and FER performances of the proposed
receiver are evaluated and some discussions on them are given.
Finally, we have introduced a novel hardware architecture for
the proposed non-RLL VLC receiver with FPGA and ASIC
synthesis results are given in details.
ACKNOWLEDGMENT
This work was supported by JSPS KAKENHI Grant Num-
ber JP16K18105.
REFERENCES
[1] S. Yoshizawa, S. Handa, F. Sasamori, O. Takyu; "A Simple but Effective
Approach for Visible Light Beacon-based Positioning Systems with
Smartphone", Proceedings of IEEE CSPA2016, pp.32-25, March 2016.
[2] Qing Liang and Ming Liu; "Plugo: a VLC Systematic Perspective of
Large-scale Indoor Localization",arXiv: 1709.06926v1, [cs.NI], August
15th, 2017.
[3] T. Yamazato, N. Kawagita, H. Okada, T. Fujii, T. Yendo, S. Arai, K.
Kamamura; "The Uplink Visible Light Communication Beacon System
for Universal Trafﬁc Management", IEEE Access, pp.22282-22290, Vol.5,
November 2017.
[4] Latif Ullah Khan; "Visible light communication: Applications, architec-
ture, standardization and research challenges",Digital Communications
and Networks , Volume 3, Issue 2, Pages 78-88, May 2017.
[5] Sridhar Rajagopal, Richard D. Roberts, Sang-Kyu Lim; "IEEE 802.15.7
Visible Light Communication: Modulation Schemes and Dimming Sup-
port", IEEE Communications Magazine, 50.3, March 2012.
[6] Wang He, and Sunghwan Kim; "New RLL decoding algorithm for
multiple candidates in visible light communication",
IEEE Photonics
Technology Letters 27.1, pp.15-17, 2015.
[7] Kim, Sunghwan, and Sung-Yoon Jung; "Novel FEC coding scheme for
dimmable visible light communication based on the modiﬁed Reed-
Muller codes.", IEEE Photonics Technology Letters 23.20, pp.1514-1516,
2011.
[8] Wang He, and Sunghwan Kim; "Bit-Level Soft Run-Length Limited
Decoding Algorithm for Visible Light Communication", IEEE Photonics
Technology Letters 28.3, pp.237-240, 2016.
[9] Wang He, and Sunghwan Kim; "Soft-Input Soft-Output Run-Length
Limited Decoding for Visible Light Communication",
IEEE Photonics
Technology Letters 28.3, pp.225-228, 2016.
[10] Wang He, and Sunghwan Kim; "Dimming Control Systems with Polar
Codes in Visible Light Communication",
IEEE Photonics Technology
Letters Vol.29, No.19, October 1, 2017.
[11] Dinh Dung Le, Duc Phuc Nguyen, Thi Hong Tran, Yasuhiko Nakashima;
"Joint Polar and Run-length Limited Decoding Scheme for Visible Light
Communications", IEICE Communication Express, Vol.7, Issue 1, pp.19-
24, Jan. ,2018.
[12] Babar, Zunaira, et al.; "Unity-Rate Codes Maximize the Normalized
Throughput of On-Off Keying Visible Light Communication",
IEEE
Photonics Technology Letters; pp.291-294, Vol.29, Issue.3, Feb. 2017.
[13] S. H. Lee and J. K. Kwon; "Turbo code-based error correction scheme
for dimmable visible light communication systems",
IEEE Photonics
Technology Letters, vol. 24, no. 17, pp.1463-1465, 2012.
[14] Kim, Sunghwan; "Adaptive fec codes suitable for variable dimming
values in visible light communication",
IEEE Photonics Technology
Letters, vol. 27, no. 9, pp.967-969, 2015.
[15] Feng, Lifang, Rose Qingyang Hu, Jianping Wang, Peng Xu; "Fountain
code-based error control scheme for dimmable visible light communica-
tion systems." Optics Communications, vol. 347, pp.20-24, 2015.
[16] Xuanxuan Lu and Jing Li; "New Miller Codes for Run-length Control
in Visible Light Communications".IEEE Transactions on Wireless Com-
munications, Vol. 17, No. 3, March, 2018.
[17] Fang, Junbin, et al. ; "An Efﬁcient Flicker-free FEC Coding Scheme for
Dimmable Visible Light Communication Based on Polar Codes", IEEE
Photonics Journal, vol.9, no.3, pp.1-10, June 2017.
[18] Harish Vangala, Yi Hong, Emanuele Viterbo; "Efﬁcient Algorithms for
Systematic Polar Encoding", IEEE Communications Letters 20.6, pp.17-
20, 2016.
[19] D. Phuc Ng., D. Dung Le, T. Hong Tran, T. Nakada, Y. Nakashima; "A
Compact Low-latency Systematic Successive Cancellation Polar Decoder
for Visible Light Communication", IEICE Technical Report, CPSY2017-
2, DC2017-2, May 2017.
[20] Tagami, H., Kobayashi, T., Miyata, Y., Ouchi, K., Sawada, K., Kubo,
K., Kuno, K., Yoshida, H., Shimizu, K., Mizuochi, T. and Motoshima,
K.; "A 3-bit soft-decision IC for powerful forward error correction in
10-Gb/s optical communication systems". IEEE journal of solid-state
circuits, 40(8), pp.1695-1705, 2005.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1602.08765v1
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1602.08765v1_Designing_A_Dimmable_OPPM-Based_VLC_System_Under_Channel_Constraints

> Source: 1602.08765v1_Designing_A_Dimmable_OPPM-Based_VLC_System_Under_Channel_Constraints.pdf

> Pages: 6

---


## Page 1


Designing A Dimmable OPPM-Based VLC System
Under Channel Constraints
Ata Chizari†, Mohammad Vahid Jamali†, Jawad A. Salehi†, Fellow, IEEE, and Akbar Dargahi‡
† Optical Networks Research Laboratoy (ONRL), Sharif University of Technology (SUT), Tehran, IRAN
‡Department of Electrical Engineering, Shahid Beheshti University (SBU), Tehran, IRAN
Email: {chizari.ata, mohammad.v.jamali}@gmail.com, jasalehi@sharif.edu, a-dargahi@sbu.ac.ir
Abstract—In this paper, we design a dimming compatible
visible light communication (VLC) system in a standard ofﬁce
room according to illumination standards under channel con-
straints. We use overlapping pulse position modulation (OPPM)
to support dimming control by changing the code weights. The
system parameters such as a valid interval for dimming together
with an upper bound for bit rate according to the channel delay
spread are investigated. Moreover, considering the dispersive
VLC channel and using Monte Carlo (MC) simulations, a method
is proposed to determine the minimum code length in different
dimming levels in order to achieve a valid bit error rate (BER).
Finally, trellis coded modulation (TCM) is suggested to be applied
to OPPM in order to take advantage of consequent coding gain
which could be up to 3 dB.
Index Terms—visible light communications, system design,
overlapping PPM, dimming control, Monte Carlo simulation.
I. INTRODUCTION
Visible light communication (VLC) is an attractive ﬁeld of
optical wireless communications (OWC) that exploits visible
light emitting diodes (VLEDs) as optical sources. This tech-
nology which has emerged in recent years, uses the visible
band of the electromagnetic spectrum. As a result, it offers
an immense unregulated bandwidth for communication in
the presence of illumination. Furthermore, as light does not
penetrate through walls, secure communication along with en-
abling frequency reuse between two rooms would be possible.
Moreover, since the active area of photo-detectors (PDs) used
in VLC is thousands of times greater than the wavelength
of light, multipath fading does not occur, however, multipath
distortion still can exist in such systems [1].
The demand for wireless bandwidth capacity as predicted
by Cisco (Cisco VNI. Feb 2015) shows a 10 times growth
in mobile trafﬁc for the next ﬁve years. On the other hand,
during the same years, the mobile carriers are predicted to
be accelerated by 9% [2]. In addition, most of mobile trafﬁc
takes place in indoor environments and at ﬁxed locations. This
makes VLC a highly probable technology for wireless access
networks of the future home and ofﬁce.
As mentioned earlier, VLC provides illumination in par-
allel to communication. Additionally, ﬂicker mitigation and
intensity control, also known as dimming control, are two
noticeable requirements of such systems according to IEEE
802.15.7 task group [3]. Thus, utilizing robust modulation
schemes that supply high data rate along with dimming
control are imperative. Some dimming adaptable procedures
for ﬂicker-free high data rate VLC systems based on IEEE
802.15.17 standard are studied in [4].
Among different kinds of modulation schemes, pulse po-
sition modulation (PPM) and its families are appropriate for
intensity modulation with direct detection (IM/DD) commu-
nication systems such as VLC, since the chips within a code
word can directly modulate a driver at the transmitter side. In
recent years, many research interests have been attracted to
overlapping PPM (OPPM) and its applications due to its high
spectral efﬁciency and low bandwidth requirement. In [5] a
method for supporting dimming by changing the amplitude
of OPPM symbol pulses is proposed. Nevertheless, this may
result in undesired chromaticity shift of the emitted light due
to the characteristics of LEDs [6]. Researchers in [7] proposed
multiple PPM (MPPM) to support dimming while transmitting
data stream. They explored that MPPM outperforms variable
PPM (VPPM) and variable on-off keying (VOOK), in terms
of spectral efﬁciency and power requirement. Moreover, a
solution to address the dimming control along with data
transmission is suggested in [8] by changing OPPM code word
weight.
This research is inspired by the need to design a VLC
system with more spectral efﬁciency and less power require-
ment. In this paper, regarding dimming support by changing
code weights of OPPM symbols [8], we consider a practical
scenario within a standard room, and we design a system
according to constraining parameters. To do so, we ﬁrst deter-
mine an interval for dimming percentage in which the illumi-
nation standards are taken into account. Then, we calculate the
maximum data rate for inter-symbol interference- (ISI-) free
transmission by simulating the dispersive channel response.
Next, we propose a method to determine the maximum usable
code length corresponding to a maximum bit error rate (BER)
in the presence of different brightness percentages. Owing
the fact that the modiﬁcation in modulation and using coding
schemes are essential to performance enhancement of VLC
systems [9], we suggest to apply trellis coded modulation
(TCM) in order to take advantage of the corresponding coding
gain which results in an improvement in the power requirement
of OPPM. Also, the validity of such application is depicted by
simulation results.
II. SYSTEM AND CHANNEL MODEL
A. System model
VLC systems use IM/DD transmission approach since it is
an efﬁcient technique in short range indoor wireless optical
applications. In this work, we assume the non-directed line-
of-sight (LOS) VLC link in which transmitters and receivers
arXiv:1602.08765v1  [cs.IT]  28 Feb 2016


## Page 2


Fig. 1: System and channel model where Tx, and PD stand for driver
and LED array, and photo-detector circuit, respectively.
have a wide range of transmission and ﬁeld of view (FOV),
respectively (see Fig. 1). Considering the baseband channel
model for optical system, the photo-current generated by the
receiver PD is given by;
Y (t) = RX(t) ∗h(t) + n(t),
(1)
where R denotes the PD responsivity, X(t) is the transmitter
optical power, ∗represents the convolution operator, and n(t)
is the receiver noise. This noise can be modeled as a signal
dependent additive white Gaussian noise (AWGN) with double
sided power spectral density of N0 as [10];
N0 = σ2
shot + σ2
th + (RP (ISI)
r
)2,
(2)
in which σ2
shot, σ2
th, and P (ISI)
r
are shot noise variance, thermal
noise variance, and the received power due to multipath reﬂec-
tion, respectively1 [10]. Moreover, the fact that X(t) represents
the instantaneous optical power, necessitates X(t) > 0 as well
as
lim
T →∞
1
2T
R T
−T X(t)dt < P, where P is the average optical
power constraint of the transmitter LED [1].
B. Dimming Support in OPPM
Consider an L-ary modulation scheme in the presence of
AWGN and the maximum likelihood (ML) sequence detection,
as well. The L non-negative symbols {x1(t), x2(t), ..., xL(t)}
are sent with the bit rate Rb every T = logL
2 /Rb seconds. The
average signal power is [11];
P = 1
L
L
X
i=1
⟨xi(t)⟩,
(3)
where ⟨.⟩=
lim
T →∞
1
2T
R T
−T x(t)dt. Assuming high signal to
noise ratio (SNR), the BER is dominated by two nearest
signals and is given by Q(dmin/√4N0), where d2
min =
min
i̸=j
R
(xi(t) −xj(t))2dt is the minimum Euclidean distance
between any pairs of valid symbols.
Looking at Fig. 1, the electrical bit sequence, ai, is turned
to parallel to be modulated by OPPM encoder. Then, after
passing through ﬁlter and being normalized, the resulted
modulated symbols, xi, will be sent to block Tx, containing
1Note that based on comprehensive study of [10], the term σ2
shot itself
takes both incoming optical signal (desired and undesired interfering signals)
and ambient background light into account.
Fig. 2: Dimming control approach in OPPM, by changing the code
weight. Dashed lines represent the transmitted optical power P.
driver circuit and LED arrays. In the case of OPPM, the
symbol interval T is divided to n chips and the temporal signal
equation would be;
x(t) = P
w
√
nT
n−1
X
k=0
ck
r n
T p(t −k T
n ),
(4)
where cks, for k = 0, 1, ..., n −1, are binary n-tuples of
weight w, and p(t) is a rectangular pulse with unit amplitude
in the interval [0, T/n]. Note that x(t) is always positive and
fulﬁlls the power constraint mentioned in (3). The w ones are
restricted to be successive whereby the bandwidth requirement
in this modulation scheme becomes smaller compared to that
of L-PPM or MPPM. This advantage is offset by a reduction
in the number of OPPM alphabet size. The number of symbols
in OPPM is L = n −w + 1 and the bandwidth requirement is
given by;
B(OPPM) =
n/w
logL
2 /Rb
.
(5)
Hence, the maximum achievable bit rate and the spectral
efﬁciency can be respectively calculated as follows [11];
Rb < B(OPPM)∆logL
2 ,
SE = 1
∆logL
2 ,
(6)
where ∆= w/n denotes the duty cycle. Now, in contem-
plation of controlling the intensity of incident light, one can
change the weight of symbols, w, while remaining the number
of chips, n, unchanged [8]. This technique is shown in Fig. 2
in which four dimming levels are illustrated. Obviously, in the
cases of ∆= 1 and 0, i.e., full brightness and full darkness,
respectively, no data could be transmitted. We also refer to
100
√
∆% as the perceived brightness percentage in that it is
more compatible with the nonlinear response of the human
eye to the linear changes in the intensity of visible light [4].
C. Channel Model
The photo-current generated by PD is proportional to the
received optical power; therefore, the SNR in a VLC link is
proportional to the square of received average optical power.
This issue makes VLC system vulnerable to the link length,
i.e., by increasing the distance between the transmitter and the


## Page 3


receiver, the SNR will signiﬁcantly decrease due to the path
loss. The SNR is given by [1];
SNR = (RP (LOS)
r
)2
N0B(OPPM) = (RH(LOS)(0)Pt)2
N0B(OPPM)
,
(7)
where t and r stand for transmitted and received terms,
respectively. H(LOS)(0) is the portion of channel DC gain
arising from the LOS link. The total channel DC gain resulted
from both LOS and non-LOS (NLOS) links is deﬁned as
H(0) =
R +∞
−∞h(t)dt. Furthermore, the transfer function H(f)
would be H(LOS)(f) + Hdif(f), in which the contribution
due to the LOS link depends on the distance between the
transmitter and the receiver, d0, as illustrated in Fig. 1; while
the second term relies on modulation frequency besides the
room dimensions. The impulse response in the time domain is
deﬁned as H(LOS)(0)δ(t −d0/c), where δ(.) represents Dirac
delta function and c is the light velocity. Additionally, the
channel DC gain is [12];
H(LOS)(0) =



Ar m+1
2πd2
0 cosm(φ0)Ts(ψ0)
×g(ψ0) cos(ψ0),
0 ≤ψ0 ≤FOV
0,
Otherwise
(8)
where Ar denotes the PD active area, m is Lambert’s mode
number of a radiation lobe, −1/log2(cos(φ1/2)) in which φ1/2
represents the semi-angle at half power of an LED, Ts(.) and
g(.) represent the optical bandpass ﬁlter transmission and non-
imaging concentrator gain of the receiver, and φ0 and ψ0 are
the angle of irradiance and incidence, respectively, as shown
in Fig. 1. Thus, the received optical power from LOS path is
P (LOS)
r
= H(LOS)(0)Pt.
For the sake of simplicity, we consider only the ﬁrst reﬂec-
tion which is more dominant than the higher order reﬂections.
So, the NLOS channel response is given by [12];
hl(t,S,Rx)=
ℜ
X
j=1
(m+1)ρjAr∆A
2πd2sjd2
Rxj
cosm(φsj)cos(ψsj)Ts(ψRxj)
× g(ψRxj) cos(φRxj) cos(ψRxj)δ(t−
dsj+dRxj
c
)
=HNLOS(0)δ(t −
dsj + dRxj
c
),
(9)
where S represents the reﬂectors’ surface (consists of four
walls in the hypothetical room), ρj is reﬂection index of the
jth reﬂector, ∆A is the element area of reﬂectors, and ℜ
denotes the number of reﬂectors, i.e., walls. For a diffused
link scenario, two components are involved. First, elements
of surfaces receive light from transmitter LED. Second, these
elements re-emit a portion of received light to PD, as depicted
in Fig. 1.
III. SYSTEM DESIGN AND SIMULATION RESULTS
In this section, we design a system according to what was
introduced in Section II. To do so, we ﬁrst investigate a
valid interval for dimming by which the illumination standards
within a room are taken into account. Then, we obtain the
maximum bit rate at which the ISI could be neglected and we
compare it with the maximum achievable bit rate offered by
Fig. 3: The hypothetical ofﬁce room containing four Landmarks and
a PD.
TABLE I: System parameters.
Transmitter side
Number of LED ﬁxtures
4
LED ﬁxture area
0.5 × 0.5 m2
Number of LEDs within a ﬁxture
324
LED spacing in a ﬁxture
2.8 cm
LED power
63 mW
Semi-angle at half power
70◦
Center luminous intensity
9.5 cd
Receiver side (Photo-detector)
Position
(1, 1, 0.85) m
Area
1 cm2
FOV
60◦
Ambient light current
27 mA
Responsivity
0.28 A/W
OPPM modulation, at a predetermined modulation bandwidth,
with respect to different dimming levels. Afterward, we pro-
pose a well-known coding scheme, namely TCM, to be applied
to OPPM in order to take advantage of the offered coding gain.
Finally, from the BER point of view, the minimum required
code length to reach a maximum probability of error regarding
channel constrains are investigated using MC simulations.
With respect to designing a dimming compatible indoor
VLC system assuming practical situation of an ofﬁce room,
we contemplate a 5 × 5 × 3 m3 room having four ﬁxtures of
LEDs as well as a table of height 0.85 m under one of the
ﬁxtures with a PD on its center. This scenario is shown in Fig.
3. Furthermore, the speciﬁcation of transmitters and receivers
utilized in simulations is summarized in Table 1 where some
of LED and PD parameters are extracted from [13].
A. Illumination Standards
The main goal of VLC systems is to provide illumination
as well as communication. Therefore, in an ofﬁce environment
the illumination generated by LEDs must satisfy illumination
standards. The horizontal illuminance resulted by OPPM mod-
ulation with dimming support on a surface is given by;
Eh = w
n
I0 cosm (φ0) cos (ψ0)
d2
0
,
(10)
where I0 represents the center luminous intensity of LEDs.
According to [13], the standard illuminance level within an


## Page 4


Fig. 4: Received illuminance at the location of PD versus perceived
brightness percentage.
300
300
300
300
400
400
400
400
400
400
400
400
400
500
500
500
500
500
500
500
500
600
600
600
600
600
600
Room width (m)
Room length (m)
−2
−1
0
1
2
−2
−1
0
1
2
Fig. 5: Distribution of brightness within the room at 80% of
perceived brightness.
ofﬁce room is between 200 and 800 lux. The variation of
horizontal illuminance in terms of different dimming levels
in the hypothetical room is depicted in Fig. 4. Note that
this ﬁgure is obtained at the position of PD shown in Fig.
3. Hence, concerning the illumination budget, a range of 44
to 90 percent of perceived brightness would be achievable.
Moreover, the distribution of illuminance within the room at
80% of perceived brightness is illustrated in Fig. 5. It is worth
to be mentioned that the acquired interval for dimming, fulﬁlls
the standard around the table on which the PD is installed.
B. Maximum Achievable Bit Rate
The bit rate in VLC systems is affected by multipath
reﬂections. An established criterion for deﬁning its upper
bound is root mean square (RMS) of delay spread which is
given by [12];
D =
sR
(t −µ)2 h2 (t) dt
R
h2 (t) dt
,
(11)
where µ =
R
th2(t)dt/
R
h2(t)dt is the mean delay resulted
by NLOS paths and h(t) is the dispersive channel impulse
response, described in (8). Therefore, to guarantee an ISI-
free transmission, the maximum bit rate should be less than
−2.5
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
2.5
−2.5
−2
−1.5
−1
−0.5
0
0.5
1
1.5
2
2.5
0
0.5
1
1.5
Room length (m)
Room width (m)
RMS delay (ns)
Fig. 6: Distribution of RMS delay spread within the given room.
40
50
60
70
80
90
10
6
10
7
10
8
Perceived brightness percentage
Bit rate
VOOK
MPPM (n=32)
OPPM (n=32)
Fig. 7: Maximum bit rate theoretically achievable in terms of
allowable dimming interval [8].
1/(10D). The delay spread parameter depends on room di-
mensions, location of transceivers, and also the FOV of PD.
Fig. 6 depicts the distribution of RMS delay spread within the
room. This parameter at the position of PD in the hypothetical
room is obtained as 1.28 ns. Hence, the bit rate would be upper
bounded by 78 Mbps. On the other hand, the maximum bit
rate theoretically achievable for different modulation schemes,
namely VOOK, MPPM, and OPPM, versus 44 to 90 percent
of perceived brightness is illustrated in Fig. 7. The OPPM
modulation scheme not only gives the highest bit rate (e.g.,
up to 50 Mbps compared to MPPM and VOOK [7] which
give 20 Mbps and 7 Mbps, respectively, at 80% of perceived
brightness), but also referring (6) the peak value of OPPM bit
rate, which is 50 Mbps, is less than the upper bound achieved
due to channel constraint, namely 78 Mbps. Note that the
modulation bandwidth of LEDs is supposed to be about 20
MHz, because although the bandwidth offered by off-the-shelf
phosphor-based LEDs is about 2 MHz, it could be improved
to 20 MHz by installing a blue ﬁlter on PD in order to remove
the yellowish component of the received light [12].
C. Trellis Coded OPPM
It is widely known that TCM improves system performance
without increasing the required bandwidth. Since OPPM sym-
bols have relatively low duty cycle and equal energy, if
the duty cycle ∆stands ﬁx, then doubling the number of
symbols L leads the bandwidth to remain constant [14]. For
this reason, the number of chips of the eventuated TCM 2L-
OPPM can be calculated as nc =
2L−1
1−∆and the equivalent
weight would be wc = ∆nc. However, by applying TCM
to OPPM the minimum hamming distance between symbols


## Page 5


Fig. 8: 1, 2, 4, and 8-state set partitioning.
decreases which causes to a growth in the probability of error.
Fortunately, the arisen coding gain via set partitioning retrieves
the performance degradation of reduced minimum hamming
distance. Fig. 8 outlines the set partitioning of the OPPM with
n = 16. The bandwidth requirement of the TCM 2L-OPPM
is the same as uncoded OPPM and can be calculated using
(5), yet the required average power could be lessened as is
described in the following.
Considering the minimum hamming distance as d
=
P
w
√
dnT = 2 for uncoded OPPM [11], the BER would be;
BER = Q(P
√
dnT
2w√N0
).
(12)
By solving the last equation for P, the average required optical
power of the uncoded OPPM can be extracted as;
P (OPPM)
uc
= 2w
r
N0
2nT Q−1(BER).
(13)
Nevertheless, for TCM 2L-OPPM we have;
P (2L−OPPM)
TCM
= 2∆w
s
N0
dc 2L−1
1−∆T Q−1(BER),
(14)
where dc is the minimum hamming distance between TCM
2L-OPPM symbols. Therefore, the consequent coding gain,
in terms of dB, is given by;
P (OPPM)
uc
P (2L−OPPM)
TCM
=10log10
 
L−1
2L−1
r
dc
2
2L−1
L−1
!
≈10log10
 r
dc
4
!
.
(15)
For the sake of achieving the coding gain, dc needs to be
greater than four, e.g., examine 9-OPPM with w = 8. A coding
gain equal to 1.2 dB is attainable by choosing a 4-state set
partitioning of the TCM 18-OPPM with wc = 17 along with
the same bandwidth requirement. Altogether, the superiority of
trellis coded OPPM over uncoded OPPM is depicted in Fig.
9, in which the power requirement to achieve a BER of 10−6
through the given room is plotted in terms of the qualiﬁed
dimming interval. As mentioned in (15), although the required
power for uncoded and TCM 2L-OPPM with dc = 4 are the
same, increasing dc to 8 and 16 leads to a reduction of 2.55
dB and 3 dB in power requirement, respectively with the same
bit rate.
D. Minimum Required Code Length
As the third part of system design considered in this paper,
we need to analyze the system from the BER viewpoint.
Referring (12) and assuming d = 2 for uncoded OPPM and
also T = logL
2 /Rb, one can write;
BER = Q(P
w
s
n logL
2
2RbN0
).
(16)
40
45
50
55
60
65
70
75
80
85
90
−5
−2
1
4
7
10
13
16
19
22
25
Perceived brightness percentage
Required power (dBm)
Uncoded OPPM (n=32)
TCM 2L−OPPM dc=4
TCM 2L−OPPM dc=8
TCM 2L−OPPM dc=16
Fig. 9: Average optical power requirement of OPPM (BER = 10−6)
in terms of allowable dimming interval at the location of PD within
the hypothetical room.
In this equation, n is the code length which needs to be chosen
in order to achieve an acceptable bit error probability. To do
so, the maximum BER of 3×10−3 as a threshold for forward
error correction (FEC) is supposed. The parameter N0 in (16)
contains the contributions of shot noise, thermal noise, and
multipath reﬂections. Therefore, we simulate the system shown
in Fig. 1 in two steps.
Step I: A transmitter containing OPPM encoder sends mod-
ulated symbols through the channel in which the noise is
considered to be AWGN. At the receiver side the temporal data
streams after passing through a ﬁlter which is matched with
the transmitted pulse shape, p(t), and being sampled with rate
1/T, are detected using a hard decision block. Finally, the bit
error probability is calculated using MC simulation, in terms
of different SNRs. This procedure is repeated for 4 dimming
levels, namely 35, 50, 75, and 86% which are illustrated in
Fig. 10, respectively. Furthermore, in each dimming level, such
simulation is done with 5 different code lengths.
Step II: In this step, to consider channel and receiver con-
straints, including the effects of multipath reﬂectors, signal
dependent shot noise, and thermal noise [10], the ratio of re-
ceived optical power to sum of noise contributions is simulated
within the hypothetical room to determine the channel SNR
according to Eq. (7). Fig. 11 depicts the SNR in terms of
a range of dimming levels. As a consequence, to choose an
appropriate code length for a speciﬁc dimming level, one can
extract the amount of channel SNR in order to determine the
probability of error from the corresponding curve (Fig. 10).
For instance, for 50% of dimming, the channel SNR using
Fig. 11 would be −0.5 dB. Then, regarding Fig. 10(b) the
code lengths 32, 64, and 128 have BER values less than
the predetermined BER threshold, i.e., 3 × 10−3. Thus, the
minimum code length of 32 can be used in this dimming
level. Table II summarizes minimum code length appropriate
for different levels of dimming.
IV. CONCLUSION
In this research, we investigated the design of a VLC system
which supports dimming. We exploited OPPM due to its less
power requirement in comparison to MPPM. The dimming
control was addressed by changing the code weights while
remaining the code lengths unchanged. At ﬁrst, the dimming


## Page 6


−9 −8 −7 −6 −5 −4 −3 −2 −1
0
1
2
3
4
1e−6
1e−5
1e−4
1e−3
1e−2
SNR (dB)
Bit error probability
n=8 (MC)
n=16 (MC)
n=32 (MC)
n=64 (MC)
n=128 (MC)
Theoretical 
FEC Limit
(a) 35%
−5
−4
−3
−2
−1
0
1
2
3
4
5
6
7
1e−6
1e−5
1e−4
1e−3
1e−2
SNR (dB)
Bit error probability
n=8 (MC)
n=16 (MC)
n=32 (MC)
n=64 (MC)
n=128 (MC)
Theoretical
FEC Limit
(b) 50%
−3 −2 −1
0
1
2
3
4
5
6
7
8
9
10
1e−6
1e−5
1e−4
1e−3
1e−2
SNR (dB)
Bit error probability
n=8 (MC)
n=16 (MC)
n=32 (MC)
n=64 (MC)
n=128 (MC)
Theoretical
FEC Limit
(c) 75%
1
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
1e−6
1e−5
1e−4
1e−3
1e−2
SNR (dB)
Bit error probability
n=8 (MC)
n=16 (MC)
n=32 (MC)
n=64 (MC)
n=128 (MC)
Theoretical
FEC Limit
(d) 86%
Fig. 10: Bit error probability of OPPM versus SNR for various perceived brightness percentages.
TABLE II: Minimum acceptable code length for various perceived
brightness percentages.
Dimming level (%)
Channel SNR (dB)
Minimum acceptable n
35
−6.2
128
50
−0.5
32
75
6.5
8
86
8.5
8
30
35
40
45
50
55
60
65
70
75
80
85
90
−10
−8
−6
−4
−2
0
2
4
6
8
10
Perceived brightness percentage
Channel SNR (dB)
Fig. 11: Simulation of channel SNR within the hypothetical room
at the location of PD for different levels of perceived brightness
percentages.
interval of 44 to 90 percent was determined according to
illumination standards in a hypothetical ofﬁce room. Then,
an upper bound of 78 Mbps for ISI-free transmission was
obtained via simulation of dispersive channel. Moreover, TCM
was suggested to be applied to OPPM in order to take advan-
tage of about 3 dB coding gain. Finally, the minimum code
length that achieves a minimum BER for different dimming
levels was obtained via MC simulation.
REFERENCES
[1] J. M. Kahn and J. R. Barry, “Wireless infrared communications,”
Proceedings of the IEEE, vol. 85, no. 2, pp. 265–298, 1997.
[2] N. Chi, H. Haas, M. Kavehrad, and T. D. Little, “Visible light commu-
nications: demand factors, beneﬁts and opportunities [guest editorial],”
IEEE Wireless Communications, vol. 22, no. 2, pp. 5–7, 2015.
[3] S. Rajagopal et al., “TG7 technical considerations document,” IEEE
802.15.7 Task Group Document, July, 2015.
[4] S. Rajagopal, R. D. Roberts, and S.-K. Lim, “IEEE 802.15. 7 visible
light communication: modulation schemes and dimming support,” IEEE
Commun. Mag., vol. 50, no. 3, pp. 72–82, 2012.
[5] B. Bai, Z. Xu, and Y. Fan, “Joint LED dimming and high capacity
visible light communication by overlapping PPM,” in Proc. IEEE Annual
Wireless and Opt. Commun. Conf., May 2010, pp. 71–75.
[6] M. Dyble, N. Narendran, A. Bierman, and T. Klein, “Impact of dimming
white LEDs: chromaticity shifts due to different dimming methods,” in
Proc. SPIE, vol. 5941, 2005, p. 59411H.
[7] K. Lee and H. Park, “Modulations for visible light communications
with dimming control,” IEEE Photon. Technol. Lett., vol. 23, no. 16,
pp. 1136–1138, 2011.
[8] J. E. Gancarz, H. Elgala, and T. D. Little, “Overlapping PPM for band-
limited visible light communication and dimming,” Journal of Solid
State Lighting, vol. 2, no. 1, p. 3, 2015.
[9] S. H. Lee, S.-Y. Jung, and J. K. Kwon, “Modulation and coding for
dimmable visible light communication,” IEEE Commun. Mag., vol. 53,
no. 2, pp. 136–143, 2015.
[10] T. Komine and M. Nakagawa, “Fundamental analysis for visible-light
communication system using LED lights,” IEEE Trans. Consumer
Electronics, vol. 50, no. 1, pp. 100–107, 2004.
[11] H. Park and J. R. Barry, “Modulation analysis for wireless infrared
communications,” in Proc. IEEE Intern. Conf. Commun. (ICC), vol. 2.
IEEE, 1995, pp. 1182–1186.
[12] Z. Ghassemlooy, W. Popoola, and S. Rajbhandari, Optical wireless
communications: system and channel modelling with Matlab R⃝.
CRC
Press, 2012.
[13] J. Grubor, O. Jamett, J. Walewski, S. Randel, and K.-D. Langer,
“High-speed wireless indoor communication via visible light,” ITG
Fachbericht, pp. 203–208, 2007.
[14] C. N. Georghiades, “Some implications of TCM for optical direct-
detection channels,” IEEE Trans. Commun., vol. 37, no. 5, pp. 481–487,
1989.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.06452v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1811.06452v1_Review_of_isolation_enhancement_with_the_help_of_Theory_of_characteristic_modes

> Source: 1811.06452v1_Review_of_isolation_enhancement_with_the_help_of_Theory_of_characteristic_modes.pdf

> Pages: 5

---


## Page 1


Review of isolation enhancement with the help of
Theory of characteristic modes
Farhan Ammar Ahmad
Department of Electrical Engineering
University of of Management and Technology Lahore,
Sialkot Campus, Pakistan
farhan.sayal@post.umt.edu.pk
Abstract—Multiple-input-multiple-output (MIMO) antennas
performance can be degraded due to the poor isolation between
the MIMO antenna elements. In this paper a review of the differ-
ent isolation enhancement schemes available in the literature is
presented. Empirically the isolation between the antennas can
be improved by placing the antenna as far as possible and
it can be enhanced further by introducing different isolation
enhancement schemes. Theory of characteristic modes (TCM)
was recently proposed that had useful beneﬁts. TCM was also
used to enhance the isolation. This papers will also focus on the
different approaches of TCM, to enhance the isolation.
Index Terms—MIMO antennas, DGS, TCM, isolation enhance-
ment, Antennas
I. INTRODUCTION
Theory of characteristic modes (TCM) was developed by
Garbacez [1] but it gained importance after it was revisited
in [2] by diagonalizing the impedance matrix of the body.
Mathematically [3]–[6]
[Z]In = (1 + jλn)[R]In
(1)
Where Z represents the impedance and Z = R + jX, In
represents the current eigen vector and 1 + jλn represents the
eigen value. Further simpliﬁcation of the (1) gives
[X]In = λn[R]In
(2)
It can be also represented as
[X]Jn = λn[R]Jn
(3)
Here Jn represents the current density eigen vector. From
Theorem of Reciprocity we know that, If Z is a linear
symmetric operator then the Hermitian parts of of Z (R and
X) will be also linear symmetric operator [3]. Thus we can
conclude that the eigen values will be always real and we
can assume that the eigen vectors will always be real and
equiphasal. Eigen value gives us an information about the
behavior of a modes at a particular frequency whether it will
resonate or store electrical energy or store mechanical energy.
Modal Signiﬁcance (MS) is a parameter depending on the
eigen value and gives us an information about the contribution
of a particular mode at a particular frequency. Mathematically
it is given by
MSn =

1
1 + jλn

(4)
At resonance the value of MS is equal to 1 and the 3 dB BW
corresponds to 0.707 value. The radiation pattern associated
with these real eigen modes are orthogonal to one another.
TCM is widely used for the analysis of various different
types of antennas such as wire antennas [7], handset antennas
[8], small antennas [9], dielectric antennas [10], printed MIMO
antennas [11]–[15] and slot antennas [16]–[18]
Multiple-input-multiple-output
(MIMO)
antennas
are
widely used for the enhancement of antenna capacity and this
technology will be used for 4G as well as 5G communications
[19], [20]. The performance of such antennas can be degraded
by if the antennas are not properly isolated [20], [21].
Recently TCM was used to enhance the isolation between the
MIMO antenna elements.
The main contribution of this paper will be to review the
empirical method procedure (EMP) used for the isolation en-
hancement as well as we will review the isolation enhancement
from the perspective of TCM. The short comings as well as
the signiﬁcance of the methods proposed in the literature w.r.t
TCM will be highlighted. Section II will brieﬂy discuss the
different methods present in the literature from EMP method
while section III will discuss isolation enhancement from the
perspective of TCM. The conclusion is provided in section IV.
II. ISOLATION ENHANCEMENT USING EMP
From EMP perspective the isolation between MIMO anten-
nas can be enhanced by the use of meta surfaces or electromag-
netic bandgap structures [22]–[24], parasitic elements [25],
[26], neutralization line technique [27], [28], optimization
of the antenna system conﬁguration [29], [30], decoupling
networks [31], and the use of Defected ground structures
(DGS) [11], [34]–[43]. Among all the aforementioned port
isolation enhancement methods, DGS is the least complex and
expensive.
Meta-material (Single layer or Double layer) are used for
the miniaturization as well as for isolation. They suppress the
surface waves between the antennas resulting in an enhanced
isolation [22]–[24]. Meta-materials normally involve larger
and bulky formations that needs to be properly optimized. The
isolation enhancement cant be obtained easily, if miniaturiza-
tion is the major objective. Isolation improvement in [31] by
the use of decoupling methods normally compromises of two
arXiv:1811.06452v1  [eess.SP]  15 Nov 2018


## Page 2


stages; matching network and then a decoupling network. In
decoupling network reactive elements are designed between
the antenna feeding ports to improve the isolation, such
networks require more space and generates additional cost.
In addition neutralization line technique was proposed in [27],
[28]. These lines deliver certain amount of signal to the neigh-
boring antenna that counteracts for the coupling between them.
The major drawback is huge amount of optimization involved
in the adjustment of the width, length and the location of
connection point of these lines. More than one neutralization
line is needed to improve the isolation over wide frequency
bandwidth and this complicates the process further. Parasitic
elements also uses the idea of ﬁeld cancellation to enhance the
isolation between the antennas [25], [26]. The major draw back
is the optimization of the shape and the dimensions of parasitic
element that play signiﬁcant role in isolation enhancement.
In [34] a periodic S shaped DGS was used to improve the
isolation between two patch antennas to 23 dB. Two DGS (T-
shaped and Line slot) were used to improve the isolation to
18 dB over a wide frequency range of 3.1-10.6 GHz in [35].
Two DGS were used to address two different frequency bands.
A DGS etched in a square ring fashion was used to improve
isolation by 7 dB, for a square patch surrounded by a square
ring patch design in [36]. An isolation was improved to 17 dB
for a 2 element, 4 shaped dual band design, where the length
of the rectangular slot and spirals in the DGS were used to
tune the frequency band in [37]. In [38] an isolation of 15 dB
was achieved for a 2 element MIMO antenna by combining
two isolation enhancement mechanisms that are orthogonal
placement of antennas and introducing a slit in the ground.
Isolation enhancement for a MIMO antenna system for more
than 2 elements is difﬁcult. Isolation was enhanced to 12dB
for a very closely packed 4-element MIMO design, where
they used four wideband DGS with multi objective fractional
factorial design [39]. A slitted pattern was etched between
2-element PIFA and wire monopole design that enhanced
the isolation to reach 20 dB [40]. Moreover the study was
extended to 4-element PIFA (aligned along a line) to get an
isolation of 12 dB. Two DGS were used in [41] to improve
isolation of a 4-element MIMO design. A rectangular slot and
a stair case slot were used to enhance the isolation to 12 dB
between the horizontal and verticals antennas respectively. For
an 8-element MIMO design a very complicated DGS that
consist of closed loop frequency selective surfaces and quad
strips connected with a circular arc were used to improve
isolation to 15 dB respectively [43].
The main problem in the DGS method to enhance isolation
is the shape, size, number of DGS, position and the huge
amount of optimization involved in the placement of DGS.
We observed that from the perspective of EMP there is no
systematic method to enhance the isolation, all of the available
literature rely on the past experience and different parametric
studies to obtain the enhanced isolation. This was the reason
that the TCM was used for the isolation enhancement to
develop a proper methodology for isolation enhancement.
III. ISOLATION ENHANCEMENT USING TCM
The presence of the any antenna or deformation in the
chassis greatly affect the chassis modes [44]–[48]. TCM was
used in [49]–[53] to enhance the isolation between the MIMO
antenna designs. It was demonstrated in [49] that the current
in PIFA is more localized as compared Monopole and this is
the reason that PIFA antennas are narrow band as compared
to Monopole antennas. At the same time MIMO PIFA antenna
design has better isolation because of its localized current
nature. For frequencies less than 1 GHz, the chassis starts
contributing to the antenna performance because now the
electrical length of the antenna is huge. So for a MIMO
antennas the situation will worsen because now all the antenna
will excite the chassis modes. For frequency of 1 GHz, the
antenna is having only one chassis mode having electric ﬁeld
maxima at the edge and electric ﬁeld minima at the center.
An electrical antenna placed at the edge will effectively excite
the chassis modes while antenna placed at the center will not.
Antennas placed at the mentioned position achieved a 5 dB
more isolation as compared to the antennas placed at the edges
of the chassis [49]. A magnetic and electrical antenna placed
at the edges will have improved isolation because the electrical
antenna will excite chassis currents while the magnetic antenna
will not [50]. Co-located antennas were introduced in [50],
to have very compact MIMO antenna design. To have better
isolation, the co-located Magnetic and electric antenna excite
the chassis currents in opposite direction. In [49], [50], only
the behavior of the ﬁrst mode using TCM was observed and
analysis were based on it.
The selective excitation of characteristic modes that have
orthogonal behavior can enhance the isolation. In [54], a feed
network (consisting of 4 hybrid 180 couplers) and 4 capacitive
coupler were designed to excite the four different modes of
the antenna. The modes excited due to its orthogonal nature
results in an enhanced isolation. The asymmetry in the ground
plane produces a natural tilt and increase in directivity [55].
Two antennas were placed at asymmetrical ground plane such
that both of them excite different characteristic modes, it will
help in getting highly isolated and highly uncorrelated beams.
In [56], the lower order modes were separated by the use
of decoupling network and GA was used to synthesize low
Quality factor MIMO antenna. Quality factor is inversely
proportional to the antenna bandwidth. A monopole (excited
via CCE) and chassis (excited via ICE) combination was used
to implement highly isolated MIMO design [57]. From the
combination of CM, a new set of Radiation modes can be
formed. The radiation modes formed are highly orthogonal to
one another thus resulting in highly uncorrelated beams [58].
In [59], out-of-band interference was improved by the use
of TCM. In Aeroplane for communication they use antenna
at 2.8 to 24 MHz with very strong power, the harmonics
of this antenna are also high power and thus affects the
communication of other antennas. Such type of interference is
called out-of-band interference. The Methodology adopted was
to calculate the Modal mutual admittance (MMA) and Modal


## Page 3


Self admittance of the antenna. CMA analysis of the higher
frequency antenna (with low power) is calculated. Functional
and non-functional modes of the ﬁrst antenna is calculated.
Modes contributing to real communication are known as
functional while the modes contributing to interference are
known as non-functional. Non-functional modes are blocked
by inductor loading with the help of TCM. The value of
the inductor shall be properly optimized to block the non-
functional mode.
In [60], designs made with the application of TCM were
compared with the empirically made designs. 5 designs were
opted from different papers with 2 designs opted from TCM
and 3 opted by empirical method. All of the selected designs
were MIMO design and they were compared in 7 different real
time scenarios. The scenarios were that ﬁrst all the designs
performance was observed in the presence of a box then 3
scenarios in which the antenna was hold by one hand and
then 3 scenarios in which the antenna was hold by two hands.
TCM design recorded 3 times high multiplexing efﬁciency as
compared to conventional design and for all the 7 scenarios,
TCM designs performed with ME of 1.6 dB better.
Now all these methods focus on the isolation enhancement
for frequentness around 1 GHz [49], [50]. At 1 GHz, for a
normal chassis only one chassis mode is present. The problem
will escalate, if we consider frequency greater than 1.5 GHz as
now more than one mode will be present. As the point where
one mode was having current minima (a possible location for
the placement of the second antenna), another mode current
maxima lies over there. Thus we are left with no possible
location.
In [12], a possible solution to this problem was proposed,
where the DGS was used to enhance the isolation between
two MIMO antennas. A methodology was also proposed to
predict whether the isolation can be enhanced or not. The
block diagram of the methodology is shown in the Figure
1. After the designing of MIMO antennas the characteristic
modes were identiﬁed. The modes were classiﬁed as coupling
and non-coupling modes based on the current distribution and
its resemblance with the chassis current distribution in the
presence of the excitation sources. Non-coupling modes are the
one contributing to the radiation while the coupling modes are
contributing to the port coupling thus degrading the isolation
performance. If there exists a certain location on the chassis,
where the DGS placed can block the coupling mode but at
the same time does not effect the non-coupling mode the
isolation between the antenna elements can be enhanced but if
there does not exist any such location, the isolation between
the antenna elements cannot be enhanced. The method was
applied to different antenna designs and it achieved the most
signiﬁcant enhancement in the isolation as compared to other
designs in the literature.
IV. CONCLUSION
In this paper, a summary of different available techniques
to enhance the isolation between MIMO antenna elements is
Figure 1: Block diagram of Proposed Isolation enhancement
scheme that can predict whether the isolation can be enhanced
or not [12]
proposed. The shortcomings of the different EMP based ap-
proaches is discussed. The TCM based approaches to enhance
the port isolation between the MIMO antenna elements are
also discussed. It was lastly shown that a new method to
enhance the isolation between the MIMO antennas with the
help of TCM was proposed. The method is able to predict
whether the isolation can be enhanced or not.
REFERENCES
[1] Garbacz. R.J., A generalized expansion for radiated and scattered ﬁelds,
Ohio State University, Columbus, 1968.
[2] Harrington, R. F., and J. R. Mautz, “Theory of Characteristic Modes
for Conducting Bodies”, IEEE Trans. Antennas Propag., 19, 622–628,
1971.
[3] Fabres, M. C. Systematic Design of Antennas Using the Theory, Univer-
sidad Politecnia de Valencia, 2007
[4] Antonino Daviu, E., Analysis and design of antennas for wireless com-
munications using modal methods, Universidad Politecnia de Valencia,
2008
[5] A. Ghalib, Current Engineering methods applied to the design of MIMO
Antennas, King Fahd University of Petroleum and Minerals (KFUPM),
Saudi Arabia, 2018.
[6] A. Ghalib and MS. Sharawi, “A comparison between the antenna current
green function and theory of characteristic modes, 2016 IEEE Middle


## Page 4


East Conference on Antennas and Propagation (MECAP) IEEE, 2016:1-
4.
[7] Cabedo-Fabr´es, M., A. Valero-Nogueira, and M. Ferrando-Bataller,
“Systematic study of elliptical loop antennas using characteristic modes,”
IEEE Antennas and Propagation Society International Symposium (AP-
SURSI), Vol. 1, 2002
[8] Ethier, J., E. Lanoue, and D. McNamara, “MIMO handheld antenna
design approach using characteristic mode concepts” Microw. Opt.
Technol. Lett., 50, 1724–1727, 2008.
[9] Newman, E., “Small antenna location synthesis using characteristic
modes”, IEEE Trans. Antennas Propag., 27, 530–531, 1979.
[10] Harrington, R. F., J. R. Mautz, and Y. Chang, “Characteristic modes
for dieletric and magnetic bodies,” IEEE Trans. Antennas Propag., 20,
194–198, 1972.
[11] M. Ikram, R. Hussain, A. Ghalib, and M. S. Sharawi, “Compact 4-
element mimo antenna with isolation enhancement for 4g lte terminals,”
in 2016 IEEE International Symposium on Antennas and Propagation
(APSURSI), pp. 535–536, June 2016.
[12] A. Ghalib and M. S. Sharawi, “TCM Analysis of Defected Ground
Structures for MIMO Antenna Designs in Mobile Terminals,” IEEE
Access, vol. 5, pp. 19680-19692, 2017.
[13] A. Ghalib, “Theory of Characteristic modes application to MIMO
Antennas,” Forum for Electromagnetic research methods and application
Technologies, vol. 29, Communication 1, 2018.
[14] A. Ghalib and M. S. Sharawi, “Analyzing DGS behavior for a MIMO
antenna system using theory of characteristic modes,” 2016 IEEE Middle
East Conference on Antennas and Propagation (MECAP), Beirut, 2016,
pp. 1-4.
[15] R. Hussain, A. Ghalib and M. S. Sharawi, “Annular Slot-Based Minia-
turized Frequency-Agile MIMO Antenna System,” IEEE Antennas and
Wireless Propagation Letters, vol. 16, pp. 2489-2492, 2017.
[16] A. Ghalib, R. Hussain and MS. Sharawi, ”Analysis of slot-based
radiators using TCM and its application in MIMO antennas”, Inter-
national Journal of RF and Microwave Computer-Aided Engineering,
2018;e21544.
[17] A. Ghalib, R. Hussain, and M. S. Sharawi, “Characteristic modes of
circular slot antennas etched on a ﬁnite ground plane,” 2017 IEEE
International Symposium on Antennas and Propagation & USNC/URSI
National Radio Science Meeting, IEEE, 167-168, 2017.
[18] A. Ghalib, R. Hussain, MS. Sharawi, “Low proﬁle frequency agile
MIMO slot antenna with TCM characterization,” 2017 11th European
Conference on Antennas and Propagation (EUCAP). IEEE, 2017, 2652-
2655.
[19] A. Ghalib, M. S. Sharawi, H. Attia and R. Mittra, “Broadband Substrate
Integrated Waveguide Slotted Array Antenna at mm-Wave Bands,” 2018
IEEE MTT-S International Microwave Workshop Series on 5G Hardware
and System Technologies (IMWS-5G), Dublin, 2018, pp. 1-3
[20] Mohammad S. Sharawi, Printed MIMO Antenna Engineering Norwood,
MA, USA: Artech House, 2014.
[21] A. Ghalib, S. Clauzier, M. S. Sharawi and Y. M. M. Antar, “A slotted
waveguide based MIMO antenna system for wireless access points,”
2016 IEEE International Symposium on Antennas and Propagation
(APSURSI), Fajardo, 2016, pp. 1459-1460
[22] G. Zhai, Z. N. Chen, and X. Qing, “Enhanced isolation of a closely
spaced four-element mimo antenna system using metamaterial mush-
room,” IEEE Transactions on Antennas and Propagation, vol. 63,
pp. 3362–3370, Aug 2015.
[23] D. K. Ntaikos and T. V. Yioultsis, “Compact split-ring resonator-loaded
multiple-input-multiple-output antenna with electrically small elements
and reduced mutual coupling,” IET Microwaves, Antennas Propagation,
vol. 7, pp. 421–429, April 2013.
[24] C. C. Hsu, K. H. Lin, and H. L. Su, “Implementation of broadband
isolator using metamaterial-inspired resonators and a t-shaped branch
for mimo antennas,” IEEE Transactions on Antennas and Propagation,
vol. 59, pp. 3936–3939, Oct 2011.
[25] S. Soltani and R. D. Murch, “A compact planar printed mimo antenna
design,” IEEE Transactions on Antennas and Propagation, vol. 63,
pp. 1140–1149, March 2015.
[26] A. C. K. Mak, C. R. Rowell, and R. D. Murch, “Isolation enhancement
between two closely packed antennas,” IEEE Transactions on Antennas
and Propagation, vol. 56, pp. 3411–3419, Nov 2008.
[27] Y. Wang and Z. Du, “A wideband printed dual-antenna with three neu-
tralization lines for mobile terminals,” IEEE Transactions on Antennas
and Propagation, vol. 62, pp. 1495–1500, March 2014.
[28] A. Diallo, C. Luxey, P. L. Thuc, R. Staraj, and G. Kossiavas, “Study
and reduction of the mutual coupling between two mobile phone pifas
operating in the dcs1800 and umts bands,” IEEE Transactions on
Antennas and Propagation, vol. 54, pp. 3063–3074, Nov 2006.
[29] R. R. Ramirez and F. D. Flaviis, “A mutual coupling study of linear and
circular polarized microstrip antennas for diversity wireless systems,”
IEEE Transactions on Antennas and Propagation, vol. 51, pp. 238–248,
Feb 2003.
[30] B. Wu and K. M. Luk, “A 4-port diversity antenna with high isola-
tion for mobile communications,” IEEE Transactions on Antennas and
Propagation, vol. 59, pp. 1660–1667, May 2011.
[31] C.-Y. Lui, Y.-S. Wang, and S.-J. Chung, “Two nearby dual-band antennas
with high port isolation,” in 2008 IEEE Antennas and Propagation
Society International Symposium, pp. 1–4, July 2008.
[32] H. Kim and S. Kahng, “Design of a compact four MIMO handset
antenna structure,” Microwave Journal, vol. 59, no. 4, pp. 162-174, 2016.
[33] S. Kahng, J. Jeon, J. Anguera, and T. Park, “A compact MIMO antenna
using CRLH conﬁguration double-layered folded ring radiations with
planar mushroom decoupling structure,” IEEE Antennas Propagation
Magazine, vol. 57, no. 4, pp. 123-130, Apr. 2015.
[34] K. Wei, J. Li, L. Wang, Z. Xing, and R. Xu, “S-shaped periodic defected
ground structures to reduce microstrip antenna array mutual coupling,”
Electronics Letters, vol. 52, no. 15, pp. 1288–1290, 2016.
[35] C. M. Luo, J. S. Hong, and L. L. Zhong, “Isolation enhancement
of a very compact uwb-mimo slot antenna with two defected ground
structures,” IEEE Antennas and Wireless Propagation Letters, vol. 14,
pp. 1766–1769, 2015.
[36] R. Anitha, V. P. Sarin, P. Mohanan, and K. Vasudevan, “Enhanced
isolation with defected ground structure in mimo antenna,” Electronics
Letters, vol. 50, no. 24, pp. 1784–1786, 2014.
[37] M. S. Sharawi, A. B. Numan, M. U. Khan, and D. N. Aloi, “A dual-
element dual-band mimo antenna system with enhanced isolation for
mobile terminals,” IEEE Antennas and Wireless Propagation Letters,
vol. 11, pp. 1006–1009, 2012.
[38] J. Ren, W. Hu, Y. Yin, and R. Fan, “Compact printed mimo antenna for
uwb applications,” IEEE Antennas and Wireless Propagation Letters,
vol. 13, pp. 1517–1520, 2014.
[39] Y. S. Chen and C. P. Chang, “Design of a four-element multiple-
input-multiple-output antenna for compact long-term evolution small-
cell base stations,” IET Microwaves, Antennas Propagation, vol. 10,
no. 4, pp. 385–392, 2016.
[40] C. Y. Chiu, C. H. Cheng, R. D. Murch, and C. R. Rowell, “Reduction
of mutual coupling between closely-packed antenna elements,” IEEE
Transactions on Antennas and Propagation, vol. 55, pp. 1732–1738,
June 2007.
[41] R. Hussain and M. S. Sharawi, “Planar meandered-f-shaped 4-element
reconﬁgurable multiple-input-multiple-output antenna system with iso-
lation enhancement for cognitive radio platforms,” IET Microwaves,
Antennas Propagation, vol. 10, no. 1, pp. 45–52, 2016.
[42] M. Ikram, R. Hussain, O. Hammi, and M. S. Sharawi, “An l-shaped
4-element monopole mimo antenna system with enhanced isolation
for mobile applications,” Microwave and Optical Technology Letters,
vol. 58, no. 11, pp. 2587–2591, 2016.
[43] R. Saleem, M. Bilal, K. B. Bajwa, and M. F. Shaﬁque, “Eight-element
uwb-mimo array with three distinct isolation mechanisms,” Electronics
Letters, vol. 51, no. 4, pp. 311–313, 2015.
[44] A. Ghalib, MS. Sharawi, “Analyzing antenna effects on mobile chassis
currents using theory of characteristic modes” Microw Opt Technol Lett.
60(8), 1898-1905, 2018.
[45] A. Ghalib, MS. Sharawi, ”Effects of actual antenna excitation on natural
radiation modes”, 2017 11th European Conference on Antennas and
Propagation (EUCAP), IEEE, 2017, 3467-3470.
[46] A. Ghalib and M. S. Sharawi, “MIMO Antenna elements effect on
chassis Modes” 2018 I.E. International Symposium on Antennas and
Propagation & USNC/URSI National Radio Science Meeting, IEEE,
2018
[47] A. Ghalib,and M. S. Sharawi, “Effect of Antenna element placement on
chassis Modes,” 2018 I.E. International Symposium on Antennas and
Propagation & USNC/URSI National Radio Science Meeting, IEEE,
2018
[48] A. Ghalib, and M. S. Sharawi, “Excitation shape and placement effects
on natural radiating modes,” 2017 IEEE International Symposium on
Antennas and Propagation & USNC/URSI National Radio Science
Meeting, IEEE, 165-166, 2017.


## Page 5


[49] H. Li, Y. Tan, B. K. Lau, Z. Ying and S. He, “Characteristic Mode
Based Tradeoff Analysis of Antenna-Chassis Interactions for Multiple
Antenna Terminals,” IEEE Transactions on Antennas and Propagation,
vol. 60, no. 2, pp. 490-502, Feb. 2012.
[50] H. Li, B. K. Lau, Z. Ying and S. He, “Decoupling of Multiple Antennas
in Terminals With Chassis Excitation Using Polarization Diversity,
Angle Diversity and Current Control,” IEEE Transactions on Antennas
and Propagation, vol. 60, no. 12, pp. 5947-5957, Dec. 2012.
[51] H. Li, J. Xiong, Z. Ying and S. L. He, “Compact and low proﬁle co-
located MIMO antenna structure with polarisation diversity and high
port isolation,” IEEE Electronics Letters, vol. 46, no. 2, pp. 108-110,
January 2010.
[52] H. Li, B. K. Lau, Y. Tan, S. He and Z. Ying, “Impact of current
localization on the performance of compact MIMO antennas,” IEEE 5th
European Conference on Antennas and Propagation (EUCAP), Rome,
pp. 2423-2426, 2011.
[53] H. Li, B. K. Lau and Z. Ying, “Optimal multiple antenna design
for compact MIMO terminals with ground plane excitation,”
IEEE
International Workshop on Antenna Technology (iWAT), Hong Kong,
pp. 218-221, 2011.
[54] S. K. Chaudhury, W. L. Schroeder and H. J. Chaloupka, “MIMO antenna
system based on orthogonality of the characteristic modes of a mobile
device,” 2nd International ITG Conference on Antennas, Munich, pp.
58-62 2007.
[55] I. Szini, A. Tatomirescu and G. F. Pedersen, “On Small Terminal MIMO
Antennas, Harmonizing Characteristic Modes With Ground Plane Ge-
ometry,” IEEE Transactions on Antennas and Propagation, vol. 63, no.
4, pp. 1487-1497, April 2015.
[56] B. Yang and J. J. Adams, “Systematic Shape Optimization of Symmetric
MIMO Antennas Using Characteristic Modes,” IEEE Transactions on
Antennas and Propagation, vol. 64, no. 7, pp. 2668-2678, July 2016.
[57] R. Martens, J. Holopainen, E. Saﬁn, J. Ilvonen and D. Manteuffel, “Op-
timal Dual-Antenna Design in a Small Terminal Multiantenna System,”
IEEE Antennas and Wireless Propagation Letters, vol. 12, no. , pp.
1700-1703, 2013.
[58] M. Bouezzeddine and W. L. Schroeder, “Design of a Wideband, Tunable
Four-Port MIMO Antenna System With High Isolation Based on the
Theory of Characteristic Modes,” IEEE Transactions on Antennas and
Propagation, vol. 64, no. 7, pp. 2679-2688, July 2016.
[59] Q. Wu, W. Su, Z. Li and D. Su, “Reduction in Out-of-Band Antenna
Coupling Using Characteristic Mode Analysis,” IEEE Transactions on
Antennas and Propagation, vol. 64, no. 7, pp. 2732-2742, July 2016.
[60] I. Vasilev and B. K. Lau, “On User Effects in MIMO Handset Antennas
Designed Using Characteristic Modes,” IEEE Antennas and Wireless
Propagation Letters, vol. 15, no. , pp. 758-761, 2016.

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1811_06452v1_review_of_isolation_enhancement_with_the_help_of_theory_of_characteristic_modes
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1811_06452V1_REVIEW_OF_ISOLATION_ENHANCEMENT_WITH_THE_HELP_OF_THEORY_OF_CHARACTERISTIC_MODES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

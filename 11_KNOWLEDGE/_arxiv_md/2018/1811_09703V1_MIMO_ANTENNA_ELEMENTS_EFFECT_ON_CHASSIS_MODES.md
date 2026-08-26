---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1811.09703v1
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1811.09703v1_MIMO_Antenna_Elements_Effect_on_Chassis_Modes

> Source: 1811.09703v1_MIMO_Antenna_Elements_Effect_on_Chassis_Modes.pdf

> Pages: 3

---


## Page 1


MIMO Antenna Elements Effect on Chassis Modes
Asim Ghalib and Mohammad S. Sharawi
Electrical Engineering Department
King Fahd University of Petroleum and Minerals (KFUPM)
email:{g201405200,msharawi}@kfupm.edu.sa
Abstract—In this paper, a 4-element printed multiple-input-
multiple-output (MIMO) loop antenna having a bandwidth of
400 MHz is proposed. The effect of the MIMO antenna on the
chassis modes system is analyzed via the theory of characteristic
modes (TCM), and it is shown that chassis CM are not enough
for the full analysis. A defected-ground-structure (DGS) is also
proposed to enhance the isolation between the antenna elements
by blocking the coupling modes.
I. INTRODUCTION
Theory of characteristic modes (TCM) was initially devel-
oped by Garbacz [1] but it gained importance after it was
revisited in [2]. Characteristic modes (CM) are given [3], [4]
[X]Jn = λn[R]Jn
(1)
where, X and R represents the imaginary and real part of the
impedance matrix Z. λn is the eigenvalue corresponding to
eigenfunction i.e. current density (Jn). TCM is widely used
for the design and analysis of various type of antennas and
designs made with TCM are more robust [5]–[9].
One of the performance metrics of multiple-input-multiple-
output (MIMO) is port isolation [10]. Alot of empirical
methods such as decoupling networks, parasitic element, neu-
tralization technique and defected ground structure (DGS) are
proposed in literature to enhance the isolation. All the method
relies on empirical approach. TCM was also used to improve
the isolation between MIMO antennas [11]–[13]. In [11], it
was observed that if we restrict our study to less than 1 GHz,
only one chassis mode will be present. So, if two antennas
are placed in a such way that one of them excite the chassis
while the other antenna does not excite the chassis, this can
yield better isolation. So, one antenna was placed at the electric
ﬁeld maxima (coupling to chassis) and the other one at electric
ﬁeld minima (not coupling to chassis), as a result 5dB isolation
improvement was achieved.
Several LTE bands use frequencies greater than 1.5 GHz,
thus it means that we have to deal with more than one
chassis mode. Let us assume the case when we have two
chassis modes (for a frequency greater than 1.83 GHz and
a chassis size of 120x60 mm2), we can see that there are
no locations on the chassis where the modes have electric
ﬁeld minima or maxima at the same time. Normally when one
mode has maxima the other mode has minima at that location.
This means that the method proposed in [11] has limitations.
Secondly, only the chassis modes are discussed and analysis
This work is supported by DSR-KFUPM under Project no. KAUST-002.
are made based on it. The effect of the single antenna and
MIMO antennas on the chassis modes are totally ignored. In
this work, we try to answer these effects. Besides we present
a 4-element MIMO loop antenna with enhanced isolation.
II. ANALYSIS PROCESS
To analyze the effect of multiple antennas, we followed a
systematic procedure. We considered a normal mobile chassis
of 120x60 mm2 dimensions. The effect of 1-element, 2 and 4-
element loop antennas on the chassis modes was investigated.
For brevity reasons, the 1-element and 2-element printed loop
antenna cases are not shown separately. The top view and
bottom view of the proposed design is shown in the Fig. 1(a)
and 1(b), respectively, while the reﬂection and isolation curves
are shown in the Fig. 1(c). The antenna is designed on an
FR4 substrate having a dielectric constant of 4.0 and substrate
thickness of 0.8 mm.
Figure 1: 4 element MIMO loop antenna, where (a) top view,
(b) bottom view and (c) Reﬂection and isolation curves without
the DGS. SP and FP refers to the shorting and feeding point
respectively. All dimensions are in mm.
The CM and the modal signiﬁcance (MS) curve of the
ground plan are shown in the Figs. 2(1a-1f) and 3(a) respec-
tively. The MS curves of the chassis modes are signiﬁcantly
affected after the introduction of the antenna as shown in the
Fig. 3(b). For brevity the current distributions are not shown.
Mode 1 radiating BW is severely affected. The other modes
i.e. mode 2 to 6 are slightly affected. This proves that the
presence of the antenna affects the CM. In the presence of the
antenna all the current maxima shift to the antenna element.
The MS curves of a 2-element MIMO antenna placed at
the shorter edge of the chassis are shown in the Figure 3(c).
arXiv:1811.09703v1  [eess.SP]  23 Nov 2018


## Page 2


We can observe that as compared to the case of chassis and
single antenna, the CM of the chassis are affected more. We
can observe that the MS curves of the modes 1, 4 and 6 are
severely affected. Mode 4 seems to be effected because the
antennas are placed at the corners of the shorter edge and mode
4 has current maxima at the shorter edge of the chassis. Mode
6 has started contributing to the radiating BW. The amount
of affect on mode 1 seems to be same for the single and 2-
element cases.
The CM and the MS curves for the 4-element MIMO case
are shown in Fig. 2(2a-2f) and 3(d) respectively. As expected
the 4-element MIMO case has highly affected the chassis
modes as compared to 1 and 2-element MIMO cases. The
current maxima lies on the antenna element and the radiating
BW of almost all the modes are affected.This validates that the
affect of the antennas especially multiple antennas cannot be
ignored and we need to take them into account while analyzing
them.
Figure 2: CM current distribution, where (1) ground plane, (2)
4-element MIMO loop antenna.(a)-(f) represents mode 1 to 6.
Figure 3: MS curve where, (a) chassis (120x60 mm2), (b)
1 element printed loop antenna on a chassis, (c) 2-element
printed MIMO loop antenna installed on shorter edge of the
chassis and (d) 4-element printed MIMO loop antenna.
An isolation of 10 dB (poor) can be observed between Ant-
1 and 3 as shown in the Fig. 1(c). If we carefully observe the
CM current distribution of the chassis and 4-element MIMO
in Figs. 2(1a-2f), we can observe that modes 1, 5 and 6 are
contributing to the coupling while modes 2 and 3 are not
contributing because they have a current null (observe the blue
spot in the middle of the chassis). This means to improve
the isolation we need to block the coupling modes while the
non-coupling modes will remain unaffected. Remember that in
the impedance BW of interest, only the ﬁrst four modes are
present in the radiating BW and all the modes have current
maxima across the antenna element. So, placing a defected
ground structure (DGS) at the middle of the chassis will not
affect the non-coupling mode but will block the coupling
mode. The proposed DGS is shown in Fig. 1(b). It enhanced
the isolation by 11 dB i.e. from -11 dB to -22 dB as shown in
the Fig. 4(a). It slightly shifted the resonance of Ant-1 and 3
but the effective BW is still from 2.2 GHz to 2.6 GHz i.e. 400
MHz on a VSWR<2 criteria. We can observe in Fig. 4(b) and
4(c) that the current coupling has been signiﬁcantly reduced.
Figure 4: 4-element MIMO loop antenna, where (a) Reﬂection
and isolation curves, (b) current distribution when antenna 1
is excited in the absence of the DGS and (c) presence of DGS.
III. CONCLUSION
The effect of MIMO antennas on mobile chassis cannot be
ignored because they severely affect the chassis modes. In the
presence of the antenna the current distribution shifts to the
antenna elements. A DGS was proposed to stop the coupling
modes that enhanced the isolation of a 4-element printed loop
based MIMO design by 11 dB.
REFERENCES
[1] R. Garbacz, “A generalized expansion for radiated and scattered ﬁelds,”
Ph.D. dissertation, Ohio State University, Columbus, 1968.
[2] M. Cabedo Fabres, “Systematic design of antennas using the theory of
characteristic modes,” Ph.D. dissertation, University of Politecnica de
Valencia, 2007. [Online]. Available: https://riunet.upv.es/handle/10251/
1883
[3] A.
Ghalib,
R.
Hussain,
and
M.
S.
Sharawi,
“Analysis
of
slot-based
radiators
using
TCM
and
its
application
in
MIMO
antennas,” International Journal of RF and Microwave Computer-
Aided
Engineering,
p.
e21544,
oct
2018.
[Online].
Available:
http://doi.wiley.com/10.1002/mmce.21544
[4] A. Ghalib and M. S. Sharawi, “Analyzing antenna effects on mobile
chassis currents using theory of characteristic modes,” Microwave and
Optical Technology Letters, vol. 60, no. 8, pp. 1898–1905, aug 2018.
[Online]. Available: http://doi.wiley.com/10.1002/mop.31257
[5] I. Vasilev and B. K. Lau, “On User Effects in MIMO Handset Antennas
Designed Using Characteristic Modes,” IEEE Antennas and Wireless
Propagation Letters, vol. 15, pp. 758–761, 2016. [Online]. Available:
http://ieeexplore.ieee.org/document/7219365/


## Page 3


[6] A. Ghalib, R. Hussain, and M. S. Sharawi, “Low proﬁle frequency
agile MIMO slot antenna with TCM characterization,” in 2017 11th
European Conference on Antennas and Propagation (EUCAP).
IEEE,
mar 2017, pp. 2652–2655. [Online]. Available: http://ieeexplore.ieee.
org/document/7928198/
[7] M. Ikram, R. Hussain, A. Ghalib, and M. S. Sharawi, “Compact
4-element MIMO antenna with isolation enhancement for 4G LTE
terminals,” in 2016 IEEE International Symposium on Antennas and
Propagation (APSURSI).
IEEE, jun 2016, pp. 535–536. [Online].
Available: http://ieeexplore.ieee.org/document/7695976/
[8] A. Ghalib and M. S. Sharawi, “Effects of actual antenna excitation
on natural radiation modes,” in 2017 11th European Conference on
Antennas and Propagation (EUCAP). IEEE, mar 2017, pp. 3467–3470.
[Online]. Available: http://ieeexplore.ieee.org/document/7928168/
[9] ——, “Analyzing DGS behavior for a MIMO antenna system using
theory of characteristic modes,” in 2016 IEEE Middle East Conference
on Antennas and Propagation (MECAP).
IEEE, sep 2016, pp. 1–4.
[Online]. Available: http://ieeexplore.ieee.org/document/7790087/
[10] M. S. Sharawi, “Printed Multi-Band MIMO Antenna Systems and
Their Performance Metrics [Wireless Corner],” IEEE Antennas and
Propagation Magazine, vol. 55, no. 5, pp. 218–232, oct 2013. [Online].
Available: http://ieeexplore.ieee.org/document/6735522/
[11] H.
Li,
Y.
Tan,
and
B.
K.
Lau,
“Characteristic
Mode
Based
Tradeoff
Analysis
of
Antenna-Chassis
Interactions
for
Multiple
Antenna Terminals,” IEEE Transactions on Antennas and Propagation,
vol.
60,
no.
2,
pp.
490–502,
feb
2012.
[Online].
Available:
http://ieeexplore.ieee.org/document/6060882/
[12] A. Ghalib and M. S. Sharawi, “{TCM} Analysis of Defected
Ground Structures for MIMO Antenna Designs in Mobile Terminals,”
IEEE Access, vol. 5, pp. 19 680–19 692, 2017. [Online]. Available:
http://ieeexplore.ieee.org/document/8010273/
[13] H. Li, B. K. Lau, Z. Ying, and S. He, “Decoupling of Multiple
Antennas in Terminals With Chassis Excitation Using Polarization
Diversity, Angle Diversity and Current Control,” IEEE Transactions on
Antennas and Propagation, vol. 60, no. 12, pp. 5947–5957, dec 2012.
[Online]. Available: http://ieeexplore.ieee.org/document/6266702/

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1811_09703v1_mimo_antenna_elements_effect_on_chassis_modes
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2018/1811_09703V1_MIMO_ANTENNA_ELEMENTS_EFFECT_ON_CHASSIS_MODES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

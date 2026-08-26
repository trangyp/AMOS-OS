---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1611.03275
source: arxiv
tags: [arxiv, knowledge, math, reference]
---
# 1611.03275_Neutrino_Monte-Carlo_Event_Generators_and_Cross-section_Data

> Source: 1611.03275_Neutrino_Monte-Carlo_Event_Generators_and_Cross-section_Data.pdf

> Pages: 6

---


## Page 1


Neutrino Monte-Carlo Event Generators and Cross-section Data
P. Stowell1, S. Cartwright1, L. Pickering2, C. Wret2, C. Wilkinson3
1University of Sheﬃeld, 2Imperial College London, 3University of Bern
In recent years a number of new theoretical models have been implemented into Monte-Carlo
neutrino interaction event generators. Being able to compare multiple model predictions is
invaluable to the ﬁeld, especially as it is unfortunately still unclear which one provides the
best ﬁt to the entire collection of neutrino cross-section data.
Using a recently developed
neutrino generator tuning framework (NUISANCE), we review a selection of models in the
NEUT and NuWro generators through comparisons to existing bubble chamber, MINERvA,
and MiniBooNE cross-section data.
1
Introduction
There are currently multiple neutrino event generators available, providing a large range of dif-
ferent interaction models to choose from when trying to construct a complete nuclear scattering
model. The NUISANCE framework 1 has recently been released to try and provide the neutrino
community with the necessary tools to help select and tune these diﬀerent generators by making
comparisons to existing cross-section data. The structure of NUISANCE allows multiple gener-
ators to be read into the same analysis routines, enforcing consistency of the signal selections
applied and ensuring any diﬀerences observed are due to the underlying physics assumptions
in each model being compared. Providing an interface between generator reweighting engines
and ROOT’s minimiser libraries 2 has created a powerful tool that can be used to automatically
tune generator models to multiple datasets by scanning the parameter space and minimising
a likelihood test statistic. In these proceedings preliminary tuning results of several diﬀerent
components of the NEUT 3 and NuWro 4 generator models are compared.
2
Bubble Chamber Tunings
Fermi motion and binding energy eﬀects are small for deuterium targets.
This allows good
constraints to be placed on neutrino-nucleon interaction models through ﬁts to deuterium-ﬁlled
bubble chamber data. Cross-section and event rate distributions from charged-current (CC)
neutrino quasi-elastic (QE) and charged pion production (1π+) measurements from the ANL,
BNL, BEBC, and FNAL experiments, were chosen for these studies 5,6,7,8,9,10,11,12. The mea-
sured cross-section and event rate distributions were digitised and added as dataset comparison
routines into the NUISANCE framework so the data could be included in joint likelihood ﬁts of
the generator models.
The nominal NEUT and NuWro free nucleon models for QE and 1π+ scattering of free
nucleons were chosen as candidate models to be tuned with the NUISANCE framework. These
generators both use the Llewellyn-Smith13 (LS) model to describe quasi-elastic scattering, and
the Rein-Sehgal14 (RS) model to describe pion production, their main diﬀerence being that
NEUT simulates multiple nuclear resonances using the RS model, whereas NuWro simulates
arXiv:1611.03275v1  [hep-ex]  10 Nov 2016


## Page 2


Table 1: Tuning results for the free nucleon interaction models in the NEUT and NuWro Monte-Carlo generators.
Quasi-elastic
Resonance
Model
MQE
A
(GeV)
χ2/DOF
M1π
A (GeV)
C5
A
χ2/DOF
NEUT 5.3.6
1.04 ± 0.03
159.8 / 146
0.89 ± 0.04
1.02 ± 0.05
102.8 / 102
NuWro v12
1.03 ± 0.03
154.4 / 146
0.92 ± 0.04
1.04 ± 0.05
111.2 / 102
 [GeV]
ν
E
2
4
6
]
2
) [cm
ν
(E
σ
0
10
20
39
−
10
×
DATA
NEUT Best Fit
NUWRO Best Fit
]
-4
c
2
 [GeV
QE
2
Q
1
2
Events
0
50
100
DATA
NEUT Best Fit
NUWRO Best Fit
Figure 1 – Comparisons of the best ﬁt predictions in the NEUT and NuWro generators to CCQE data. (left)
ANL Eν cross-section data used to constrain the ANL CCQE normalisation. (right) BNL Q2 event rate data
used to place an additional shape constraint on the BNL cross-section predictions.
only the ∆(1232) component, relying on a ∆/DIS extrapolation to populate the higher order
resonances. Both generators have “reweight engines” allowing the user to make model predic-
tions over a range of model parameters after event generation 15. These reweight engines were
used to study variations in a set of free model parameters. For the QE model only the quasi-
elastic axial mass parameter (MQE
A ) was treated as free. In the pion production model both the
resonant axial mass (M1π
A ), and the axial coupling constant (C5
A) were treated as free.
The overall similarity between the two generators provides an additional validation test of
the tuning results. Since both generators use the LS and RS models it is expected they should
obtain similar best ﬁt results when tuning to distributions where the majority of events originate
from low hadronic mass events (W < 1.4 GeV). The published ﬂux distributions were used to
generate charged-current events in each generator. The target in each case was considered to be
a free proton and neutron to give a combined deuteron cross-section without binding energy or
Fermi motion eﬀects. From these Monte-Carlo (MC) samples, events were selected that matched
the published signal selections and normalised to give matching cross-section predictions. In the
cases where only event rate information was given the predictions were normalised to match
the integrated event rate in the data. An additional correction was applied to the QE model
predictions to convert them from free nucleon predictions to that for a bound deuteron 16. This
correction, applied as a function of true Q2, was found to have a negligible eﬀect on the ﬁts but
was left in to maintain consistency with tuning studies shown in the original publications 5.
A joint likelihood was formed within the NUISANCE framework by ﬁrst selecting a single
distribution from each publication to place a constraint on the normalisation for that mea-
surement (e.g. CCQE σ(Eν)). An additional shape-only likelihood was then added for each
remaining distribution in the measurement itself (e.g. CCQE Q2 Event Rates) to form a total
likelihood for that measurement. The purpose of adding these shape-only terms is to minimise
any bias that may be introduced when a model is tuned to only a single distribution, whilst try-
ing to avoid issues with over-counting placing too strong a constraint on the total cross-section.
These likelihoods for each dataset were added uncorrelated to form a total likelihood for the
chosen models in the study. The NUISANCE tuning framework was set up to automatically
scan the parameter space until a best ﬁt parameter set was found. The results can be seen in
Table 1, with examples of the best ﬁt predictions for both generators in Figs. 1 and 2. Both
generators were found to be capable of describing the data with an acceptable goodness-of-ﬁt.


## Page 3


(GeV)
ν
 E
1
1.5
2
2.5
3
/proton)
2
) (cm
ν
(E
σ
 
0
5
10
15
39
−
10
×
DATA
NEUT Best Fit
NUWRO Best Fit
*)
θ
 cos(
1
−
0.5
−
0
0.5
1
 Number of events
20
40
60
80
DATA
NEUT Best Fit
NUWRO Best Fit
Figure 2 – Comparisons of the best ﬁt predictions in the NEUT and NuWro generators to CC1π data. (left)
BNL Eν cross-section data used to constrain the BNL CC1π normalisation (right) ANL Adler Angle event rate
data used to place an additional shape constraint on the BNL cross-section predictions. Eﬀects of higher order
resonances can be seen in the diﬀerence between NEUT and NuWro at low angles.
The disagreement seen between the generators in the quasi-elastic χ2 results are due to slight
diﬀerences in the generated MC statistics, whereas the diﬀerences in the 1π+ ﬁts arise from
fundamental diﬀerences in the generator models themselves. This can be seen in Fig. 2 where
higher order resonances can be seen contributing to the NEUT prediction at high angles in-
troducing a diﬀerence between the two generator predictions. In both cases the diﬀerences are
not large enough to signiﬁcantly shift the tuning results, with both generators ﬁnding best ﬁt
results in agreement with one another, providing a set of free nucleon parameters suitable for
propagation to future nuclear tuning studies.
3
NuWro/NEUT LFG Tunings
When extending neutrino interaction models to nuclear targets, an inclusive generator model
must also consider how the presence of the nuclear medium can modify the interaction. We
consider the latest model available in the NEUT 5.3.6 generator, consisting of a Relativistic
Fermi Gas17 (RFG) with relativistic RPA correction and a Nieves multi-nucleon model18 (NEUT
RFG+Nieves). The choice of nuclear spectral function to model nucleon binding energy and
Fermi motion introduces a problem in generator model tuning, since multiple discrete models are
available. It is believed that any direct measurements of quasi-elastic scattering are also likely
to be sensitive to additional multi-nucleon interaction channels (2p2h) that can produce ﬁnal
states of similar topologies to true quasi-elastic scattering inside the nucleus 18. For comparison
we also consider two alternative models in the NuWro generator, a model with a local Fermi gas
RPA correction and a Nieves 2p2h model (NuWro LFG+Nieves), and a RFG with a transverse
enhancement model19 (NuWro RFG+TEM).
Each model was tested against MiniBooNE and MINERvA CCQE data in both neutrino
and anti-neutrino runs 20,22,21,23. Although the collaborations deﬁne their signal as “true CCQE
interactions”, experience suggests that all four measurements are in fact sensitive to both CCQE
and 2p2h interaction channels. Model predictions corresponding to each dataset were therefore
produced by generating events with the published ﬂux distribution and selecting only those
events which originated from one of these two interaction channels. A joint sample likelihood
for the study was deﬁned using MiniBooNE Tµ −cos θµ data with shape-only uncorrelated errors
and a ﬂoating normalisation, and MINERvA Q2
QE data with full covariance between neutrino
and antineutrino distributions, matching the method used in Ref. 2. To look at variations in
both of the interaction channels, the quasi-elastic axial mass (alters only CCQE interactions)
and 2p2h normalisation (alters only 2p2h interactions) were treated as free parameters that
could could be changed to improve agreement between the data and MC.
The χ2 values shown in Table 2 are unrealistically small, because the MiniBooNE 2D distri-
bution public data release does not provide bin-to-bin correlations. When varying both param-


## Page 4


Table 2: Tuning results for the NEUT and NuWro CCQE+2p2h models when compared in joint ﬁts to MiniBooNE
and MINERvA quasi-elastic cross-section data.
Model
MA (GeV)
2p2h Norm (%)
χ2/DOF
NuWro LFG+Nieves
1.16 ± 0.03
8.3 ± 11.9
100.74 / 229
NuWro RFG+TEM
1.15 ± 0.03
21.3 ± 12.5
93.62 / 229
NEUT RFG+Nieves
1.14 ± 0.03
25.5 ± 12.4
106.25 / 229
)
2
 (GeV
QE
2
 Q
0.0
0.5
1.0
1.5
2.0
)
2
/GeV
2
 (cm
2
QE
/dQ
σ
 d
0
5
10
15
20
39
−
10
×
Data
NEUT RFG+Rel.RPA
NuWro LFG+Nieves
NuWro RFG+TEM
)
2
 (GeV
QE
2
 Q
0.0
0.5
1.0
1.5
2.0
)
2
/GeV
2
 (cm
2
QE
/dQ
σ
 d
0
5
10
15
39
−
10
×
Data
NEUT RFG+Rel.RPA
NuWro LFG+Nieves
NuWro RFG+TEM
Figure 3 – Comparison of the best ﬁt MC predictions in NEUT and NuWro to MINERvA CCQE data. The clear
diﬀerence in the normalisation between the MC and data arises from the MINERvA data placing a much stronger
constraint on the cross-section shape than its normalisation.
eters freely similar results were found for all three models, an inﬂation of the axial mass away
from the bubble chamber tuning result, and a large suppression of the 2p2h cross-section nor-
malisation compared to the nominal prediction. Both parameters were estimated to be highly
correlated when using MINUIT’s HESSE24 routine to estimate parameter errors, a feature of the
strong shape-constraint that the MINERvA dataset places on the ﬁt. The use of a local Fermi
gas model was insuﬃcient to relieve the tensions seen in previous joint ﬁt studies to this data
and a signiﬁcant model variation is likely needed to relieve the tensions whilst still maintaining
consistency with other theoretical and experimental constraints. One signiﬁcant problem with
this method of tuning individual interaction channels to this data is that an unknown frac-
tion of pion-less delta decay events was subtracted from the each distribution, directly by the
MiniBooNE collaboration in their background subtraction procedure, and indirectly by MIN-
ERvA in their cut on their recoil energy deposited inside the detector outside the interaction
vertex. If reliable constraints on free cross-section parameters for nuclear targets are to be ex-
tracted, a series of dedicated tuning studies using more inclusive signal deﬁnitions with minimal
model-dependent background corrections is required.
4
MINERvA CC-inclusive comparisons
The MINERvA collaboration has attempted to study the presence of nuclear eﬀects in neutrino
carbon interactions directly through the extraction of both the 3-momentum transfer (q3) and
hadronic recoil energy for a given event 25. The variable “energy available” (Eav) is deﬁned as
the sum of kinetic energy of protons and charged pions, and the total energy of neutral pions,
electrons, and photons, leaving the nucleus. Subtracting the muon energy from the observed
energy deposited around the vertex allows a CC-inclusive event selection to be unfolded into a
diﬀerential cross-section measurement in terms of Eav and q3. Comparisons between this data
and GENIE have shown disagreement in the “dip” region at high q3 between the quasi-elastic
and resonance peaks (0.4 < q3/GeV < 0.6) . Similar diﬀerences between model predictions and
data have been observed by the NOvA collaboration when studying hadronic recoil energy, and
it has been suggested that changes to how we model 2p2h interactions could relieve this tension.
For comparison the best ﬁt results from the NEUT and NuWro tunings to both bubble
chamber and carbon measurements are compared to this “recoil energy data” in Fig. 4. Simple


## Page 5


0
2
4
6
/GeV < 0.2
3
 q
≤
a) 0.0 
0
0.1
0.2
0.3
0.4
0.
0
2
4
6
/GeV < 0.5
3
 q
≤
d) 0.4 
/GeV < 0.3
3
 q
≤
b) 0.2 
0
0.1
0.2
0.3
0.4
0.
/GeV < 0.6
3
 q
≤
e) 0.5 
/GeV < 0.4
3
 q
≤
c) 0.3 
0
0.1
0.2
0.3
0.4
0.
/GeV < 0.8
3
 q
≤
f) 0.6 
]
2
/GeV
2
cm
-42
| [10
3
d|q
av
/dE
σ
2
d
 [GeV]
av
Energy Available E
Figure 4 – Comparison of the previous NEUT and NuWro tuning results to MINERvA low recoil scattering
data. Shown are the NEUT predictions using the bubble chamber tuning (blue), the NEUT predictions using
the CCQE tuning (red), the NuWro LFG+Nieves predictions with bubble chamber tuning (purple), and CCQE
tuning (green). The dashed lines of matching colour show the predicted 2p2h contribution to the cross-section in
each bin.
variations in the axial mass and 2p2h normalisation are found to be incapable of ﬁlling in the
disagreement between the data and MC, but the large shape disagreement in the “dip” region
is signiﬁcantly smaller for NuWro as a result of using a local Fermi gas model. Since the signal
deﬁnition is CC-inclusive and extremely sensitive to ﬁnal state particle multiplicities, it is also
possible to create similar predictions through multiple smaller variations of diﬀerent features
of the inclusive generator model. For example, Fig. 5 shows the diﬀerent contributions to the
NEUT and 2p2h cross-section from pn and nn pairs. This fraction of these pairs currently has a
reasonably large uncertainty assigned, and is just one of many examples of free parameters that
could be used to sculpt the total CC-inclusive prediction to better match the data.
The major complication of trying to use such a measurement on its own to understand
where models may be deﬁcient is that ﬁnal state “recoil energy” variables will be extremely
sensitive to ﬁnal state interaction models. Changes in these models can cause events to migrate
in “recoil energy” space making it diﬃcult to disentangle which exact features of the model may
be problematic. Since no measurements have been made in these kinematic variables in the past,
it is diﬃcult to tell in which of the many interaction channels or FSI model the tensions may
really lie, and a full CC-inclusive model tuning with additional constraints from CC0π/CC1π
data may be required to extract reliable results from these recoil energy measurements.
5
Conclusion
The NUISANCE tuning group has deﬁned a publicly accessible framework that supports neu-
trino event generator tuning. Early studies of the NEUT and NuWro generator free nucleon
models have found that both generators obtain consistent results when tuning to deuterium
bubble chamber data. One weakness of these tunings is the lack of correlations across bubble
chamber experiments, and future studies will look at correlating ﬂux uncertainties in the stud-
ies to obtain more reliable best ﬁt parameters. When compared to nuclear CCQE data from
MINERvA and MiniBooNE, both generators were also found to produce very similar tuning
results despite much clearer diﬀerences between the models investigated. The use of alternative
spectral function deﬁnitions was found to make little diﬀerence in the observed suppression of
the 2p2h normalisation, hinting that the diﬃculties in achieving good agreement between these
experiments may lie with the cross-section extraction methods used to obtain the data itself.
Finally, comparisons of the ﬁt results to MINERvA CC-inclusive showed that more signiﬁcant
modiﬁcations to the full cross-section model are required to obtain a reasonable agreement with


## Page 6


0
2
4
6
/GeV < 0.2
3
 q
≤
a) 0.0 
0
0.1
0.2
0.3
0.4
0.
0
2
4
6
/GeV < 0.5
3
 q
≤
d) 0.4 
/GeV < 0.3
3
 q
≤
b) 0.2 
0
0.1
0.2
0.3
0.4
0.
/GeV < 0.6
3
 q
≤
e) 0.5 
/GeV < 0.4
3
 q
≤
c) 0.3 
0
0.1
0.2
0.3
0.4
0.
/GeV < 0.8
3
 q
≤
f) 0.6 
]
2
/GeV
2
cm
-42
| [10
3
d|q
av
/dE
σ
2
d
 [GeV]
av
Energy Available E
Figure 5 – Comparison of NEUT 2p2h pp/nn pair contributions in the Eav variable. Each prediction has been
scaled up by a factor of 10 so that its shape is clear. Shown in red and blue are the nn and pn contributions
respectively.
newer CC-inclusive cross-section data.
Acknowledgments
The author wishes to thank the UK STFC for supporting this work.
References
1. P.
Stowell,
L.
Pickering,
C.
Wilkinson,
C.
Wret,
“NUISANCE
Framework”,
http://nuisance.hepforge.org/
2. Brun, Rene, and Fons Rademakers. Nucl. Instrum. Meth. A 389.1 (1997)
3. Y. Hayato, Acta Phys. Polon. B 40, 2477 (2009).
4. C. Juszczak, Acta Phys. Polon. B 40, 2507 (2009)
5. S. J. Barish et al., Phys. Rev. D 16, 3103 (1977).
6. Radecky et al. Phys Rev D, 3rd series, volume 25, number 5, 1 March 1982, p 1161-1173
7. Thpr: Derrick et al. Phys Rev D, Vol 23, Number 3, 1 Feb 1981, p 569-575
8. N. J. Baker et al., Phys. Rev. D 23, 2499 (1981).
9. Kitagaki et al. Phys Rev D, Vol 34, Number 9, 1 November 1986, p 2554-2565
10. K. Furuno et al., (NuInt02), UC Irvine, U.S.A., KEK Preprint 2003-48
11. T. Kitagaki et al., Phys. Rev. D 28, 436 (1983).
12. D. Allasia et al., Nucl. Phys. B 343, 285 (1990).
13. Smith, CH Llewellyn Physics Reports 3 5 1972
14. D. Rein and L. M. Sehgal, Annals Phys. 133, 79 (1981).
15. L. Pickering, P. Stowell and J. Sobczyk, arXiv:1610.07053 [hep-ex].
16. S. K. Singh, Nucl. Phys. B 36, 419 (1972).
17. R. A. Smith and E. J. Moniz, Nucl. Phys. B 43, 605 (1972)
18. J. Nieves, I. Ruiz Simo and M. J. Vicente Vacas, Phys. Rev. C 83, 045501 (2011)
19. A. Bodek, H. S. Budd and M. E. Christy, Eur. Phys. J. C 71, 1726 (2011)
20. A. A. Aguilar-Arevalo et al. [MiniBooNE], Phys. Rev. D 81, 092005 (2010)
21. G. A. Fiorentini et al. [MINERvA], Phys. Rev. Lett. 111, 022502 (2013)
22. A. A. Aguilar-Arevalo et al. [MiniBooNE], Phys. Rev. D 88, no. 3, 032001 (2013)
23. L. Fields et al. [MINERvA], Phys. Rev. Lett. 111, no. 2, 022501 (2013)
24. J., F., and M. I. N. U. I. T. Roos. Comp. Physics Comm. 10.6 (1975): 343-367.
25. P. A. Rodrigues et al. [MINERvA Collaboration], Phys. Rev. Lett. 116, 071802 (2016)

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
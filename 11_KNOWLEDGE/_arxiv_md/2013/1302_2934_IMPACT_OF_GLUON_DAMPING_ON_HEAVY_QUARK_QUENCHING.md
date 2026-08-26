---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1302.2934
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1302.2934_Impact_of_gluon_damping_on_heavy-quark_quenching

> Source: 1302.2934_Impact_of_gluon_damping_on_heavy-quark_quenching.pdf

> Pages: 4

---


## Page 1


arXiv:1302.2934v1  [hep-ph]  12 Feb 2013
Impact of gluon damping on heavy-quark quenching
M. Nahrgang(1,2), M. Bluhm(3), P. B. Gossiaux(1), J. Aichelin(1)
(1) SUBATECH, Universit´e de Nantes, EMN, IN2P3/CNRS, 4 rue Alfred Kastler, 44307
Nantes cedex 3, France
(2) Frankfurt Institute for Advanced Studies (FIAS), Ruth-Moufang-Str. 1, 60438 Frankfurt
am Main, Germany
(3) Dipartimento di Fisica, Universit`a degli Studi di Torino and INFN, Sezione di Torino, via
Giuria 1, 10125 Torino, Italy
E-mail: nahrgang@subatech.in2p3.fr
Abstract.
In this conference contribution, we discuss the inﬂuence of gluon-bremsstrahlung
damping in hot, absorptive QCD matter on the heavy-quark radiation spectra. Within our
Monte-Carlo implementation for the description of the heavy-quark in-medium propagation we
demonstrate that as a consequence of gluon damping the quenching of heavy quarks becomes
signiﬁcantly aﬀected at higher transverse momenta.
1. Introduction
The fundamental properties of strongly interacting matter are investigated in ultra-relativistic
heavy-ion collisions. With these experiments one aims at understanding the basic processes in
QCD matter at ﬁnite temperature T and/or baryon density. For this purpose heavy quarks are
a particularly clean probe of the formed matter because they are predominantly produced from
initial hard scatterings of participating nucleons.
Subsequently they undergo collisional and
radiative processes through interactions with the locally thermalized light quarks and gluons in
the surrounding medium.
These interactions with the medium constituents lead to a thermalization of heavy quarks
with small transverse momentum pT, while those with a large pT suﬀer from a signiﬁcant in-
medium energy loss. This is reﬂected in sensitive observables such as the nuclear modiﬁcation
factor RAA. Results from RHIC for the heavy-ﬂavour decay non-photonic single electron RAA
as well as the RAA of D-mesons [1] indicate indeed a substantial quenching of heavy quarks at
higher pT up to 10 GeV. The data from the latest measurements at the LHC [2] was able to
extend this pT -range up to 30 GeV for very central collisions. This oﬀers a new and unique
opportunity for testing our understanding of in-medium energy loss mechanisms, with the
prospect of disentangling eventually the diﬀerent contributions from collisional and radiative
energy loss processes.
Radiative processes are considered to be the dominant contribution to parton energy loss
at larger parton energies, but they may become aﬀected by coherence eﬀects in the medium,
cf. the review in [3]. As a consequence of the destructive interference of radiation amplitudes
from successive scatterings oﬀmedium constituents within the formation length lf of gluon-
bremsstrahlung, the radiation spectrum is suppressed for larger gluon energies ω. This is the
QCD-analog of the Landau-Pomerantschuk-Migdal (LPM) eﬀect [4]. Other eﬀects may alter


## Page 2


the radiation pattern as well. For example, the dielectric polarization of the medium modiﬁes
the dispersion relation of radiated gluons which aquire an eﬀective in-medium mass mg. This
leads to a signiﬁcant reduction of the radiation spectrum in the soft-ω region [5, 6]. Similarly,
dissipative eﬀects in the QCD medium may diminish the radiative energy loss of heavy quarks
as advocated in [7].
In these proceedings, we discuss the dissipative eﬀect of gluon damping on the radiation
spectra of heavy quarks. Focussing on the implementation of the novel eﬀect into our Monte-
Carlo approach to the heavy-quark in-medium propagation [8, 9] we show that damping
mechanisms inﬂuence the RAA of heavy quarks in a pronounced way.
2. Gluon damping phenomenology
In an absorptive plasma, mechanisms, which lead to the damping of bremsstrahlung gluons,
can reduce the radiative energy loss of traversing, highly-energetic charges. This phenomenon
was ﬁrst demonstrated in [10] for asymptotic electric charges in electro-magnetic plasmas by
modelling the dispersive medium via a complex index of refraction and then advocated in [7] to
be of relevance also in the absorptive Quark-Gluon Plasma (QGP). In fact, dissipative eﬀects
such as quark–anti-quark pair creation or secondary gluon-bremsstrahlung generation introduce
an additional scale in the medium. If this damping length scale ld, which is related to the gluon
damping rate Γ as ld ≃1/Γ, is smaller than or of the order of lf of the nascent gluon, absorptive
mechanisms will reduce the probability for the formation of gluon-bremsstrahlung and, thus,
inﬂuence the radiative energy loss of partons. This might be particularly important in the case
of the large formation lengths in coherent emission processes.
Even though the aforementioned mechanisms represent higher-order eﬀects in perturbative
QCD, they might be relevant for the matter investigated in the laboratory.
For example,
the damping rate due to secondary gluon-bremsstrahlung formation is parametrically given as
Γ ∼g4T up to logarithmic corrections of order O(1/g) [7]. Consequently, higher temperatures
imply a larger damping rate and thus a smaller ld. Moreover, the formation length of gluon
radiation [7] increases for a given x = ω/E with increasing energy E of the emitting parton.
Thus, for large E (as long as Γ > 1/L, where L is the parton path length in the medium) and/or
large T dissipative eﬀects will be important for the radiation spectra of partons, a situation that
is likely to be encountered experimentally at the LHC.
3. Medium-modiﬁcation of the heavy-quark radiation spectrum
The Gunion-Bertsch (GB) gluon radiation spectrum [11] originating from single, independent
scatterings of massless partons was generalized within scalar QCD to the case of massive partons
in [12]. Medium-modiﬁcations of this heavy-quark GB-spectrum due to coherence eﬀects were
discussed in detail in [13]. In Fig. 1, we show the radiation spectra of both cases for charm and
bottom quarks at diﬀerent parton energies E.
In order to highlight quantitatively the additional impact of gluon damping eﬀects on the
bremsstrahlung spectrum oﬀheavy quarks, we make use of a scaling ansatz advocated in [14]
according to which the global radiation intensity becomes modiﬁed due to medium eﬀects via
d2I = d2IGB·˜lf/l0
f. Here, the scale l0
f ≃2x(1−x)E/(m2
g+x2m2
s) with the parton mass ms denotes
the formation length in a single, independent scattering process [7, 13] and ˜lf = min(ld, lf) is
given by the minimum between the damping length ld and the in-medium formation length lf
discussed in [7] fulﬁlling lf ≤l0
f. Figure 1 exhibits the correspondingly modiﬁed spectra for
two diﬀerent values of Γ. As evident, damping eﬀects may reduce the heavy-quark radiation
spectrum signiﬁcantly in an intermediate ω-region, where the inﬂuence of the dissipative eﬀects
increases with both increasing Γ and E.
This reduction is stronger than the reduction due
to the LPM-eﬀect. Moreover, with larger Γ and larger E the spectra become more and more
quark-mass independent.


## Page 3


0.1
1
10
ω/GeV
0
0.2
0.4
0.6
0.8
1
d I/dωdz
2
T=250 MeV, E=20 GeV
c-quark
GB
LPM
0.1
1
10
ω/GeV
0
0.2
0.4
0.6
0.8
1
d I/dωdz
2
T=250 MeV, E=20 GeV
b-quark
GB
LPM
0.1
1
10
ω/GeV
0
0.2
0.4
0.6
0.8
1
d I/dωdz
2
T=250 MeV, E=40 GeV
c-quark
GB
LPM
0.1
1
10
ω/GeV
0
0.2
0.4
0.6
0.8
1
d I/dωdz
2
T=250 MeV, E=40 GeV
b-quark
GB
LPM
Figure 1.
(Colour online) Suppression of the heavy-quark Gunion-Bertsch (GB) radiation
spectrum (thick solid curves) due to LPM-eﬀect (thinner solid curves) and gluon damping eﬀect
(dash-dotted curves for a damping rate Γ = 0.5 T and dashed curves for Γ = 0.75 T, with the
ﬁxed gluon mass of mg = 2 T). Left panels are for charm quarks with mc = 1.5 GeV, right
panels for bottom quarks with mb = 5.1 GeV, while the upper (lower) row shows the results for
a quark energy E of 20 GeV (40 GeV).
4. Inﬂuence of gluon damping on the quenching of heavy quarks
To study the consequences of gluon damping on observables, we include the modiﬁed radiation
spectra illustrated above in the Monte-Carlo approach [8, 9] to the heavy-quark propagation in
the medium. The interaction of the heavy quarks with the light partons in the QGP amounts
in collisional and radiative processes, which are described in detail in [8, 9, 12, 13], while the
evolution of the medium is obtained from the ﬂuid dynamic expansion presented in [15]. Any
theoretical uncertainty aﬀecting the model is assumed to be captured in one global factor K which
rescales the interaction rates and which is obtained from calibration to the available RHIC data.
In this spirit it is possible to reproduce the available heavy-ﬂavour data at RHIC energies for
both purely collisional and collisional plus radiative (without damping) energy loss scenarios
as was demonstrated in [8, 12, 13].
At LHC energies, the pT -range is extended and we are
able to identify diﬀerent trends in the RAA for these two scenarios, cf. [16]. Counter-intuitively,
available D-meson data from central Pb+Pb collisions at the LHC [2] seem to favour the purely
collisional energy loss scenario [16]. This indicates that a reduction of the radiative energy loss
component would be necessary in order to reconcile the model with the data. As illustrated in
Fig. 2, one possibility for such a reduction could be the inclusion of gluon damping mechanisms.


## Page 4


Pb+Pb  2.76 TeV
0-20%; KH Hydro
El. + LPM HK=0.7L
c quarks
b quarks
pT@GeVcD
5
10
15
20
25
30
35
0.5
1.0
1.5
RAA
Figure 2.
(Colour online) RAA of charm (thin
curves) and bottom quarks (thick curves) with (solid)
and without (dashed) the eﬀect of gluon damping.
The damping rate is Γ = 0.75 T. For details cf. [16].
Here, we show the RAA of charm and
bottom quarks for the collisional plus
radiative energy loss scenario (dashed
curves), which includes the LPM eﬀect
but no dissipative eﬀects. The inclusion
of gluon damping mechanisms results in
the solid curves. As evident, when one
neglects gluon damping eﬀects, the RAA
stays almost ﬂat for pT ≥5 GeV for
the charm quarks and for pT ≥15 GeV
for the heavier bottom quarks.
Once
gluon damping is taken into account,
the nuclear modiﬁcation factor increases
visibly at higher transverse momenta.
In the shown pT -range predominantly
charm quarks are aﬀected,
while the
eﬀect sets in for bottom quarks only at
larger pT. Details, however, depend on
the value of the gluon damping rate.
5. Conclusions
We discussed the inﬂuence of gluon damping in the absorptive QGP on the quenching of
heavy quarks in ultra-relativistic heavy-ion collisions. In addition to the known modiﬁcation of
radiation spectra due to coherence eﬀects, gluon damping eﬀects reduce signiﬁcantly the spectra
in an intermediate ω-region for large gluon damping rates Γ and/or large parton energies E.
Consequently, in the absorptive QGP heavy quarks become less quenched at large transverse
momenta. With increasing pT , the quenching seems to become quark-mass independent which
would be visible in a prominent behaviour of the heavy-ﬂavour meson RAA as advocated in [16].
MN and MB thank the organisers of the conference Heavy Ion Collisions in the LHC Era,
Quy Nhon, Vietnam, 16-20 July 2012, for ﬁnancing their participation. MB acknowledges the
ﬁnancial support received from the SaporeGravis Network of Hadron Physics I3 (I3HP3). MN
thanks her parents for ﬁnancing her ﬂight to Vietnam.
References
[1] STAR Collab., Phys. Rev. Lett. 98 (2007) 192301; Erratum-ibid. 106 (2011) 159902; PHENIX Collab., Phys.
Rev. C 84 (2011) 044905; X. Dong [for the STAR Collab.], arXiv:1210.6677 [nucl-ex].
[2] ALICE Collab., JHEP 09 (2012) 112.
[3] S. Peign´e and A. V. Smilga, Phys. Usp. 52 (2009) 659.
[4] R. Baier, Y. Dokshitzer, A. M¨uller, S. Peign´e, D. Schiﬀ, Nucl. Phys. B 483 (1997) 291; ibid. 484 (1997) 265.
[5] B. K¨ampfer and O. P. Pavlenko, Phys. Lett. B 477 (2000) 171.
[6] M. Djordjevic and M. Gyulassy, Phys. Rev. C 68 (2003) 034914; Phys. Lett. B 560 (2003) 37.
[7] M. Bluhm, P. B. Gossiaux, T. Gousset, J. Aichelin, arXiv:1204.2469 [hep-ph]; arXiv:1209.1149 [hep-ph].
[8] P. B. Gossiaux and J. Aichelin, Phys. Rev. C 78 (2008) 014904.
[9] P. B. Gossiaux, R. Bierkandt, J. Aichelin, Phys. Rev. C 79 (2009) 044906.
[10] M. Bluhm, P. B. Gossiaux, J. Aichelin, Phys. Rev. Lett. 107 (2011) 265004; J. Phys. G 38 (2011) 124119.
[11] J. F. Gunion and G. Bertsch, Phys. Rev. D 25 (1982) 746.
[12] P. B. Gossiaux, J. Aichelin, T. Gousset, V. Guiho, J. Phys. G 37 (2010) 094019.
[13] P. B. Gossiaux, arXiv:1209.0844 [hep-ph].
[14] V. M. Galitsky and I. I. Gurevich, Il Nuovo Cimento 32 (1964) 396.
[15] P. F. Kolb, J. Sollfrank, U. Heinz, Phys. Rev. C 62 (2000) 054909.
[16] P. B. Gossiaux, M. Nahrgang, M. Bluhm, T. Gousset, J. Aichelin, Quark Matter 2012 proceedings.

---
**Related:** [[00-Home]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
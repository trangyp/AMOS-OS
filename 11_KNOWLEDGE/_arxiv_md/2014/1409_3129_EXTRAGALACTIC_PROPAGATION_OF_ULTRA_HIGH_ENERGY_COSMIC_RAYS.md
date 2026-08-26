---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1409.3129
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1409.3129_Extragalactic_Propagation_of_Ultra-High_Energy_Cosmic_Rays

> Source: 1409.3129_Extragalactic_Propagation_of_Ultra-High_Energy_Cosmic_Rays.pdf

> Pages: 8

---


## Page 1


EXTRAGALACTIC PROPAGATION OF
ULTRA-HIGH ENERGY COSMIC RAYS
DANIEL KUEMPEL
RWTH Aachen University, III. Physikalisches Institut A,
Otto-Blumenthal-Straße, 52056 Aachen, Germany
More than 100 years after the discovery of cosmic rays and various experimental eﬀorts, the
origin of ultra-high energy cosmic rays (E > 1017 eV) remains unclear. The understanding of
production and propagation eﬀects of these highest energetic particles in the universe is one
of the most intense research ﬁelds of high-energy astrophysics. With the advent of advanced
simulation engines developed during the last couple of years, and the increase of experimental
data, we are now in a unique position to model source and propagation parameters in an
unprecedented precision and compare it to measured data from large scale observatories. In
this paper we revisit the most important propagation eﬀects of cosmic rays through photon
backgrounds and magnetic ﬁelds and introduce recent developments of propagation codes.
Finally, by comparing the results to experimental data, possible implications on astrophysical
parameters are given.
1
Introduction
The observation of cosmic rays with ultra-high energies poses interesting questions. Even more
than 50 years after the detection of particles of 100 EeV 1 (1 EeV = 1018 eV) many issues are
still unanswered. What mechanism in the universe can accelerate particles to such high ener-
gies? What is their origin and what kind of particles are they? What can they tell us about
fundamental and particle physics? Is there a maximal energy they can reach? To tackle these
problems large-scale observatories have been built at various locations enabling the observation
of diﬀerent parts of the sky. Today, the most prominent sites are the Pierre Auger Observatory2,3
in the southern hemisphere located in the Argentinean Pampa Amarilla and the Telescope Ar-
ray 4 (TA) in the northern hemisphere in Millard County, Utah, USA. The measurement of the
particle ﬂux, elemental composition, arrival directions and temporal variations are of central
importance to get a clue of an answer. However, to interpret the observations a detailed knowl-
edge of particle propagation eﬀects is essential. In fact, the propagation of ultra-high energy
cosmic rays (UHECR) from the source to the observer modiﬁes the original source spectra and
chemical composition due to interactions with low energy photons and matter. Propagation
also inﬂuences the sky distribution of arriving charged cosmic rays due to deﬂections in cosmic
magnetic ﬁelds. The open question of the chemical composition of highest-energy cosmic rays is
in fact linked to the question on the size of deﬂection in cosmic magnetic ﬁelds. Any consistent
interpretation of the nature and origin of ultra-high energy cosmic rays thus has to include
propagation in a three-dimensional environment. With the advent of advanced simulation en-
gines, described in more detail in Sec. 4, we are now in a unique position to model source and
propagation parameters in an unprecedented precision using computer clusters.
The paper is organized as follows: in Sec. 2 we will revisit the most important interaction
arXiv:1409.3129v2  [astro-ph.HE]  20 Sep 2014


## Page 2


Figure 1 – Spectral density of the CMB (blue line), infrared background (IRB, green line) 5, and universal radio
background (URB, red line) 6 as a function of energy and frequency.
processes for ultra-high energy cosmic rays and their secondaries. Deﬂections in galactic and
extragalactic magnetic ﬁelds are discussed in Sec. 3. The current status of public propagation
codes is given in Sec. 4. Finally, some prospects are given in Sec. 5 on comparing results of
simulations with measurements from large-scale observatories before concluding in Sec. 6.
2
Propagation eﬀects en route to Earth
In the following we shall review the most important aspects of particle propagation through the
universe. Except in very close vicinity to the source, only background photons and magnetic
ﬁelds are relevant to estimate the interactions. In the intergalactic medium the most important
photon background is the cosmic microwave background radiation (CMB) with a typical energy
of about 10−3 eV. In addition, cosmic rays can interact with optical and infrared backgrounds
as well as with radio waves. The spectral density in the interstellar medium is shown in Fig. 1.
As a consequence of the high energies of cosmic rays with Lorentz factors Γ = E/m, background
photons are seen highly blue-shifted in the nucleus rest frame with the relevant energy ϵ′ =
ϵΓ(1 −cos ϑ), with the photon energy ϵ in the laboratory frame and the collision angle ϑ. The
interaction length λ of a cosmic ray through an isotropic background can be calculated as
λ−1(E) =
Z ∞
0
n(ϵ)σavg(ϵ) dϵ ,
(1)
where n(ϵ) is the spectral number density of the background particles (cf. Fig. 1) and σavg(ϵ)
the cross section for the relevant process averaged over all collision angles ϑ.
2.1
Photo-pion production
The pion production for a head-on collision of a nucleon N with a background photon γ can be
described as N + γ −→N + π, with a threshold energy of
EN,π
thres = mπ(mN + mπ/2)
2ϵ
≈6.8 · 1019 
ϵ
10−3 eV
−1
eV ,
(2)


## Page 3


where mπ and mN are the masses of the pion and the nucleon and ϵ ∼10−3 eV represents a
typical energy of a CMB photon. Due to the high inelasticity a η of the process and the dense
CMB photons it was already realized in the 1960s by Greisen 7 and Zatsepin & Kuz’min 8,
that the universe is opaque for ultra-high energy particles, leading to the so-called GZK ﬂux
suppression. A prominent example of photo-pion production by protons is given by
p + γ →∆+ →
 n + π+
with branching ratio 1/3
p + π0
with branching ratio 2/3 ,
(3)
where a proton interacts electromagnetically with a photon and excites the proton to the ∆+
resonance before decaying via strong interactions. In the channel that conserves the charge of
the original nucleon mostly neutral pions are produced which decay into secondary gamma rays
π0 →γ + γ, whereas charge exchange reactions produce mostly charged pions which eventually
decay into electrons, positrons and neutrinos. In fact, these are the main production channels
for ultra-high energy secondary photons and neutrinos by hadronic cosmic rays, cf. Sec. 2.5.
Pion production by nuclei can be described in good approximation by the superposition model.
Here nuclei are treated as a superposition of Z free protons and A −Z free neutrons b. Note
that the energy carried away by a pion is only η/A of the energy of the primary nucleus with
an increased threshold of EN,π
thres · A.
2.2
Pair production
Another important interaction process is pair production by a nucleus X with mass number A
and atomic number Z on a photon A
ZX + γ −→
A
ZX + e+ + e−. This reaction has a threshold
energy of
Ee±
thres = me(mX + me)
ϵ
≈4.8 · 1017 A

ϵ
10−3 eV
−1
eV ,
(4)
and a relatively small inelasticity of about η ∼10−3. Therefore, pair production is typically
treated as a continuous energy-loss process, but is especially important when calculating sec-
ondary photons below PeV energies.
2.3
Photodisintegration of nuclei
In a photodisintegration process a photon is absorbed by an atomic nucleus leading to an excited
nuclear state before splitting into two or more parts. Depending on the photon energy ϵ′ in the
rest frame of the nuclei diﬀerent processes are dominant. At low photon energies up to 30 MeV,
the giant dipole resonance with the emission of one or two nucleons is the most important
contribution. At higher energies, between 30 MeV and 150 MeV, the quasi-deuteron process
dominates with predominantly multi-nucleon emission. The eﬀective loss rate can be described
as
1
E
dE
dt

eﬀ
= 1
A
dA
dt =
X
i
i
ARA,i(E)
(5)
where RA,i is the rate for emission of i nucleons from a nucleus of mass A.
2.4
Other energy-loss processes
An important loss process which dominates near or below the pair production threshold are
redshift losses due to the expansion of the universe. This adiabatic fractional energy loss can be
described as
−1
E
dE
dt

adiabatic
= H0 ,
(6)
athe inelasticity is typically η = 0.2 close to the threshold and η = 0.5 far above the threshold.
bthe binding energy is neglected.


## Page 4


Figure 2 – Left: Energy-loss length χLoss =
  1
E
dE
dx
−1 of primary protons as a function of energy. Diﬀerent energy-
loss processes on various photon backgrounds (CMB, infrared, optical and ultra-violet) are indicated. Center:
Energy loss length for iron as a function of the Lorentz factor Γ.
Diﬀerent contributions of pair production
and photodisintegration on various backgrounds are indicated. Right: Energy loss length for diﬀerent nuclei as a
function of energy. In all three ﬁgures, the eﬀect of adiabatic expansion of the universe is indicated by a horizontal
dashed line. (From 9)
where H0 is the Hubble constant.
Another relevant propagation eﬀect is nuclear decay of unstable particles produced e.g. by pho-
todisintegration or photo-pion processes. A nuclear decay can change the energy of the particle
as well as the nucleus type.
A graphical illustration of various processes of energy loss for protons as well as for nuclei is
shown in Fig. 2. For protons, the energy loss is dominated below a few EeV by the expansion of
the universe. At intermediate energies, pair production on the CMB is most relevant while at en-
ergies above ∼70 EeV pion production becomes dominant. For iron nuclei photodisintegration
represents the most important loss mechanism at high energies.
2.5
Secondary photons
As already discussed in Sec. 2.1 photo-pion production by protons is the main production channel
for ultra-high energy secondary photons. Since photons have no charge, they are not deﬂected by
magnetic ﬁelds. However, the existing cosmic photon background creates additional interactions.
The dominant process is the attenuation of the ultra-high energy photons due to pair production
on background photons, γUHE + γb →e+ + e−.
The produced e± can again interact with
background photons via inverse Compton scattering resulting in an electromagnetic cascade
that ends at GeV-TeV energies where the universe becomes increasingly transparent for photons.
Typical energy-loss lengths are 7 −15 Mpc at 10 EeV and 5 −30 Mpc at 100 EeV 10.
3
Magnetic ﬁelds
During the propagation charged cosmic rays are deﬂected by extragalactic and galactic magnetic
ﬁelds. Considering a particle with charge Z and energy E in [PeV], the Larmor radius rL in [pc]
can be estimated as
rL
pc

= 1.1
 E
PeV
 µG
B
 1
Z
(7)
with the magnetic ﬁeld B in [µG].
The parameter space for magnetic ﬁelds in the universe is large, since ﬁeld strengths and es-
pecially ﬁeld orientations are not well constrained. Especially for extragalactic magnetic ﬁelds
predictions vary a lot. Their origin is not well understood 11 and theories vary from the cre-
ation in the primordial universe 12 to magnetic pollution from astrophysical sources (e.g. 13)


## Page 5


Figure 3 – Left: Expected deﬂection of primary protons injected in the direction of intersecting longitude and
latitude lines (dotted line) at the edge of the galaxy using the JF2012 galactic ﬁeld model. The sky map is given
in galactic coordinates. The color code refers to the energy of the injected proton. Right: Mean deﬂection of
protons arriving isotropically at the edge of the galaxy using the JF2012 model. The blue line represents the
mean deﬂection seen from the Pierre Auger Observatory site in the southern hemisphere recording particles up
to 60◦in zenith angle. The green line corresponds to the Telescope Array site in the northern hemisphere also
recording particles up to 60◦in zenith angle. The shaded area indicates the central 68% quantile. Simulations
are done using the cosmic-ray propagation code CRPropa 3.0, cf. Sec. 4.
such as jets from radio galaxies. Typical strengths are expected to be ∼1 −40 µG in the core
of clusters of galaxies 14 and 10−16 −10−6 G in ﬁlaments. The simulation and prediction of
large-scale magnetic ﬁelds is a dedicated task. Assuming that the ﬁelds are induced in galaxies,
one would expect stronger ﬁelds in high-peaked density regions and a nearly suppressed ﬁeld
in voids. To model more realistic inhomogeneous conﬁgurations various groups have developed
large-scale structure simulations including magnetic ﬁelds, e.g. 15,16,17. However, these simula-
tions lead to discrepant results due to the variety of assumptions that have to be made. To
constrain the strength of extragalactic magnetic ﬁelds further observations are needed, e.g. via
the arrival directions of charged cosmic rays at ultra-high energies, through the observation of
extended gamma-ray emission around point sources in connection with the time delay in gamma-
ray ﬂares 18, or through Faraday rotation measurements, e.g. with the future Square Kilometer
Array 19.
When considering extragalactic propagation of cosmic rays, also deﬂections within the Milky
Way may become important. Concerning galactic magnetic ﬁelds there has been much progress
in recent years. To constrain the strength of the ﬁeld the best available methods are Faraday ro-
tation measures (e.g. used in20) and polarized synchrotron radiation which are both line-of-sight
integrated quantities. A combination of both measurements including recent observations lead
to the construction of a new galactic ﬁeld model introduced in 2012 by Jansson and Farrar 21,22
(JF2012). One improvement compared to previous simulations is to allow for a possibility of a
large-scale out-of-plane component as well as structured random ﬁelds. Typical ﬁeld strengths
are of the order of µG and not uniform, which implies that the angular deﬂection depends
strongly on the observed direction as shown in Fig. 3.
This is important when considering
anisotropies at ultra-high energy. At lower energies, e.g. for a primary proton of energy 1 PeV
in a galactic ﬁeld of 3 µG the Larmor radius is ∼0.4 pc. With a diameter of the Milky Way
of ∼30 kpc it is not expected to ﬁnd any point sources of charged cosmic rays. At ultra-high
energies there is a possibility to detect point sources and small-scale anisotropy using charged
particles. A detailed knowledge of the magnetic ﬁeld structure helps to interpret results from
diﬀerent experiments being sensitive to diﬀerent parts of the sky. An example is given in Fig.


## Page 6


3 (right) selecting the Telescope Array and the Pierre Auger Observatory representing the cur-
rently largest cosmic-ray observatories for ultra-high energy particles. According to the JF2012
model, on average, the expected deﬂection of protons arriving isotropically at the edge of the
galaxy is smaller for TA compared to the Pierre Auger Observatory. This is interesting when
comparing results on anisotropy studies at both sites such as recent indications of intermediate-
scale anisotropy of cosmic rays in the northern sky with TA 23.
4
Simulation engines
To interpret the data collected by large-scale observatories it is necessary to develop tools that
simulate the propagation of ultra-high energy cosmic rays over several orders of magnitude in
energy and length scales, ranging from hundreds of Mpc down to galactic scales of order kpc
including their interactions, discussed in Sects. 2 and 3. There has been much progress in re-
cent years and the currently most advanced public code is CRPropa c 24,25. During propagation
CRPropa takes into account structured magnetic ﬁelds and ambient photon backgrounds in-
cluding all relevant particle interactions. To enable multi-messenger analyses, secondary γ-rays
and neutrinos are tracked and propagated to the observer. The code is continuously extended
to handle the increasing data collected by large-scale observatories and to scan the large pa-
rameter space with high statistics, cf. Sec. 5.
The latest version CRPropa 3.0 26 reﬂects a
complete redesign of the code structure, compared to the second version, to facilitate high per-
formance computing and comprises new physical features. Simulations can be done either in a
one-dimensional or three-dimensional mode. Furthermore, to take into account cosmic evolu-
tion eﬀects in anisotropy studies and magnetic suppression in spectrum and composition studies,
the latest version is augmented with a four-dimensional propagation taking into account only
particles that arrive at a speciﬁc observer time. Another major improvement is the ability to
take galactic deﬂections into account. This is realized by a lensing technique described in 27
and applied in Fig. 3. Photon cascades can be simulated using the electromagnetic cascade
codes DINT 28 or EleCa 29. Other propagation codes are e.g. HERMES 30, SimProp 31 or Trans-
portCR 32.
5
Multiparameter challenge
Simulation of cosmic-ray propagation involves a set of assumptions that have to be made. This
stems from the fact that many unknown or uncertain parameters enter the simulation. E.g.
sources of ultra-high energy cosmic rays are still under controversial debate, i.e. parameters
such as total number, position, size, luminosity, composition, spectral index and emission pat-
terns have to be estimated. Furthermore, during propagation background photon ﬁelds and
magnetic ﬁeld strength oﬀer a wide parameter range. One way to disentangle information on
the UHECR universe is to compare simulations with experimental data in form of suitable ob-
servables. From the observational point of view only direction and energy of the primary particle
are known via the observation of extensive air showers at large-scale observatories. For example,
the shape of the observed energy spectrum gives information on the sources, as well as on the
propagation through the cosmic structures including the GZK eﬀect. However, given the large
parameter space in simulations, the spectrum alone can not unambiguously constrain diﬀerent
astrophysical scenarios and additional observables are needed. A more indirect measurement of
the composition of the particle is given by the interpretation of air-shower observables such as
the depth of shower maximum, usually referred to as Xmax and given in g/cm2, and air-shower
ﬂuctuations. Several groups have started confronting data with simulations to constrain astro-
physical scenarios, e.g. 9,33,34,35,36,37. These simulations indicate that typically a source with a
hard spectral index is needed to explain current measurements, unless a nearby source or some
chttps://crpropa.desy.de


## Page 7


1021
1022
1023
1024
1025
1018
1019
1020
1021
E3 J(E) (eV2 m-2 s-1 sr-1)
E (eV)
p
He
CNO
MgAlSi
Fe
 650
 700
 750
 800
 850
1018
1019
1020
<Xmax> (g/cm2)
E (eV)
EPOS
Sybill
QGSJet1
QGSJet2
 10
 20
 30
 40
 50
 60
 70
1018
1019
1020
σ(Xmax) (g/cm2)
E (eV)
proton expectation
iron expectation
proton expectation
iron expectation
all
Figure 4 – Left: Propagated cosmic-ray spectrum of protons and nuclei given an injection spectral index of β = −1
and maximum energy at the source of Emax = Z × 5 · 1018 eV. Solid lines indicate primary particles as labelled.
The grey band shows the ﬂux of secondaries alone. Red dots represent the measured cosmic-ray spectrum at the
Pierre Auger Observatory. Center: Mean Xmax as a function of energy using the same choice of parameters as
for the spectrum plot. The red band illustrates the result of the simulation. The proton and iron expectations
using diﬀerent interaction models are indicated. The grey band denotes the energy range in which the Auger ﬂux
is not reproduced. Right: Same as the middle ﬁgure, but using its dispersion σ(Xmax). Figure adapted from 37.
References on interaction models and Pierre Auger data are given therein.
additional component is assumed. An example for a ﬁt to spectrum and composition measure-
ments is given in Fig. 4. Given the derived hard injection spectra of β = −1 the Pierre Auger
Observatory spectrum can only be ﬁtted for energies ≳5 × 1018 eV. The lower energy part
requires introducing a second population such as an additional class of extragalactic sources
emitting mainly light elements, or a galactic cosmic-ray component 37.
However, the latter
argument requires a dominant proton fraction above ≳1018 eV which is disfavored by upper
limits on anisotropy obtained by the Pierre Auger Observatory 38 stating that the fraction of
protons should not exceed ∼10% . This already indicates that it is necessary to include as much
information as possible in terms of observables into the analysis.
Most commonly, comparisons to spectrum and composition data have been performed. By
utilizing arrival directions as well as secondary particles (photons, neutrinos), the parameter
space can be further constrained enabling a multi-messenger approach. As an example, multi-
plets of UHECR which exhibit energy ordering according to their angular distances relates to
coherent magnetic ﬁelds. With their detection magnetic ﬁeld strength can be quantiﬁed. Fur-
thermore, high level observables such as energy-energy-correlations quantify eﬀects of turbulent
magnetic ﬁelds. So-called event-shape observables, which are being adapted from high-energy
particle physics, have sensitivity to the density of sources, and probe deﬂections of UHECR in
coherent magnetic ﬁelds. In addition, secondary messengers can be compared with observations
down to the TeV energy range, refer to e.g. 39.
6
Conclusion
The simulation of cosmic-ray propagation plays an essential role in understanding astrophysical
processes at ultra-high energies. Taking into account the great wealth of data of unprecedented
quality and quantity now being accumulated at large-scale observatories and sophisticated sim-
ulations based on advanced theoretical and experimental knowledge, the confrontation of data
with results of simulations will lead to valuable constraints on the parameter space of theoret-
ical models and will in this way contribute to new scientiﬁc information about the high-energy
universe. It is still too early to draw decisive conclusions on astrophysical scenarios and more
messengers have to be included in the analysis in a multi-messenger approach.


## Page 8


Acknowledgments
It is a pleasure to thank the organizers for inviting me to the exciting 10th Rencontres du Vietnam
conference on “Very High Energy Phenomena in the Universe” held at the International Center
of Interdisciplinary Science Education (ICISE) in the city of Quy Nhon / Vietnam. The author
is grateful to stimulating discussions with David Walz who provided Figs. 1 and 3. Financial
support by the German Academic Exchange Service (DAAD) is thankfully acknowledged.
References
1. J. Linsley, Phys. Rev. Lett. 10, 146 (1963)
2. J. Abraham et al. [Pierre Auger Collaboration] Nucl. Instrum. Meth. A, 523, 50 (2004)
3. J. Abraham et al. [Pierre Auger Collaboration] Nucl. Instrum. Meth. A, 620, 227 (2010)
4. T. Abu-Zayyad et al. [TA Collaboration] Nucl. Instrum. Meth. A, 689, 87 (2012)
5. T. M. Kneiske et al., Astron. Astrophys. 413, 807 (2004)
6. R. J. Protheroe and P. L. Biermann, Astropart. Phys. 6, 45 (1996)
7. K. Greisen, Phys. Rev. Lett. 16, 748 (1966)
8. G. T. Zatsepin and V. A. Kuz’min, JETP Lett. 4, 78 (1966)
9. D. Allard, Astropart. Phys. 39-40, 33 (2012)
10. M. Risse and P. Homola, Mod. Phys. Lett. A 22, 749 (2007)
11. R. M. Kulsrud and E. G. Zweibel, Rept. Prog. Phys. 71 0046091 (2008)
12. L. M. Widrow, Rev. Mod. Phys. 74, 775 (2002)
13. E. Scannapieco et al. Mon. Not. Roy. Astron. Soc. 365, 615 (2006)
14. K. Kotera and A. V. Olinto, Annu. Rev. Astro. Astrophys., 49, 119 (2011)
15. G. Sigl et al., Phys. Rev. D 70, 043007 (2004)
16. K. Dolag et al., JCAP 0501, 009 (2005)
17. S. Das et al., Astrophys. J. 682, 29 (2008)
18. A. Neronov and D. V. Semikoz, Phys. Rev. D 80, 123012 (2009)
19. R. Beck et al., SKA and the Magnetic Universe, pp. 103, Berlin: Springer-Verlag (2007)
20. M. S. Pshirkov et al., Astrophys. J. 738, 192 (2011)
21. R. Jansson and G. R. Farrar, Astrophys. J. 757, 14 (2012)
22. R. Jansson and G. R. Farrar, Astrophys. J. Lett. 761, L11 (2012)
23. R. U. Abbasi et al. [Telescope Array Collaboration], Astrophys. J. 790, L21 (2014)
24. E. Armengaud et al. Astropart. Phys. 28, 463 (2007)
25. K.-H. Kampert et al. Astropart. Phys. 42, 41 (2013)
26. R. A. Batista et al., Proc. 33rd ICRC, Rio de Janeiro, Brazil, arXiv:1307.2643 (2013)
27. H. P. Bretz et al., Astropart. Phys. 54, 110 (2014)
28. S. Lee, Phys. Rev. D 58, 043004 (1998)
29. M. Settimo and M. De Domenico, Astropart. Phys. 62, 92 (2015)
30. M. De Domenico, Europ. Phys. J. Plus 128, 99 (2013)
31. R. Aloisio et al., JCAP 10, 007 (2005)
32. O. E. Kalashev and E. Kido, arXiv:1406.0735
33. A. M. Taylor, Astropart. Phys. 54, 48 (2014)
34. D. Hooper and A. M. Taylor, Astropart. Phys. 33, 151 (2010)
35. A. M. Taylor et al., Phys. Rev. D 84, 105007 (2011)
36. T. K. Gaisser et al., Front. Phys. China 8, 748 (2013)
37. R. Aloisio et al., arXiv:1312.7459
38. P. Abreu et al. [Pierre Auger Collaboration], Astrophys. J. Lett. 762, L13 (2013)
39. G. Sigl and A. van Vliet, arXiv:1407.6577

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1409_3129_extragalactic_propagation_of_ultra_high_energy_cosmic_rays
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2014/1409_3129_EXTRAGALACTIC_PROPAGATION_OF_ULTRA_HIGH_ENERGY_COSMIC_RAYS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

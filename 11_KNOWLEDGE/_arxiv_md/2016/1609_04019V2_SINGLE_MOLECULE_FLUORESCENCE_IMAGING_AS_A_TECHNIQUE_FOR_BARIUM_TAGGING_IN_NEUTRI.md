---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1609.04019v2
source: arxiv
tags: [arxiv, knowledge, reference, unclassified]
---
# 1609.04019v2_Single_Molecule_Fluorescence_Imaging_as_a_Technique_for_Barium_Tagging_in_Neutri

> Source: 1609.04019v2_Single_Molecule_Fluorescence_Imaging_as_a_Technique_for_Barium_Tagging_in_Neutri.pdf

> Pages: 17

---


## Page 1


Preprint typeset in JINST style - HYPER VERSION
Single Molecule Fluorescence Imaging as a
Technique for Barium Tagging in Neutrinoless
Double Beta Decay
B. J. P. Jones, A. D. McDonald and D. R. Nygren
University of Texas at Arlington,
502 Yates St, Arlington, TX 76019, United States of America
E-mail: ben.jones@uta.edu, austin.mcdonald@uta.edu, nygren@uta.edu
ABSTRACT: Background rejection is key to success for future neutrinoless double beta decay ex-
periments. To achieve sensitivity to effective Majorana lifetimes of ∼1028 years, backgrounds
must be controlled to better than 0.1 count per ton per year, beyond the reach of any present tech-
nology. In this paper we propose a new method to identify the birth of the barium daughter ion
in the neutrinoless double beta decay of 136Xe. The method adapts Single Molecule Fluorescent
Imaging, a technique from biochemistry research with demonstrated single ion sensitivity. We ex-
plore possible SMFI dyes suitable for the problem of barium ion detection in high pressure xenon
gas, and develop a ﬁber-coupled sensing system with which we can detect the presence of bulk
Ba++ ions remotely. We show that our sensor produces signal-to-background ratios as high as 85
in response to Ba++ ions when operated in aqueous solution. We then describe the next stage of
this R&D program, which will be to demonstrate chelation and ﬂuorescence in xenon gas. If a suc-
cessful barium ion tag can be developed using SMFI adapted for high pressure xenon gas detectors,
the ﬁrst essentially zero background, ton-scale neutrinoless double beta decay technology could be
realized.
KEYWORDS: Gaseous detectors;Scintillators, scintillation and light emission processes (solid, gas
and liquid scintillators); Very low-energy charged particle detectors; neutrinoless double beta
decay.
arXiv:1609.04019v2  [physics.ins-det]  20 Sep 2016


## Page 2


Contents
1.
Signals and backgrounds in neutrinoless double beta decay
1
2.
Xenon TPC detectors and barium tagging
3
3.
Single molecule ﬂuorescent imaging
4
4.
SMFI for barium detection
6
5.
Prospects for testing SMFI barium sensors in xenon gas
11
6.
Conclusions
13
1. Signals and backgrounds in neutrinoless double beta decay
The nature of the neutrino is one of the open fundamental questions of nuclear and particle physics.
The existence of a non-zero neutrino mass has been established through the discovery of ﬂavor
oscillations. This allows for the possibility that neutrinos are Majorana fermions, with deep impli-
cations for cosmology and particle physics. The only known experimental method to establish the
Majorana nature of the neutrino is a robust observation of neutrinoless double beta decay (0νββ).
The process of double beta decay is possible in even-even nuclei in which the nucleus A
ZX is
stable relative to A
Z+1X but unstable relative to A
Z+2X. In these cases, the nucleus can, according
to the standard model, decay via the reaction A
ZX →A
Z+2 X + 2e−+ 2¯ν, with the ﬁnal state kinetic
energy shared between the two detectable electrons and two invisible neutrinos. If and only if the
neutrino is a Majorana fermion, a similar process with no neutrinos in the ﬁnal state may occur,
A
ZX →A
Z+2 X +2e−.
Various isotopes have been used as target media in 0νββ searches. The strongest limits on
lifetime, which under most nuclear matrix element models also correspond to the strongest effective
Majorana mass limits, have been obtained using 136Xe [1, 2]. The present limit sits at T0νββ >
1.07×1026 yr at 90% CL [1] . Discovery of 0νββ is possible at any lifetime beyond this limit if
the neutrino mass ordering is normal, or in a range of lifetimes reaching up to τ ∼1028 yr if the
ordering is inverted. If the mass ordering is normal, discovery of 0νββ would also represent a
measurement of the absolute neutrino mass scale. Given the inverted ordering, on the other hand,
the absolute mass scale can likely not be determined, but the Majorana nature is falsiﬁable as well as
discoverable. A goal for future 0νββ searches is to reach sensitivities near the maximum lifetime
in the inverted scenario [3] which is around a hundred times beyond present experimental limits.
Reaching this sensitivity with a ton scale detector in a practical scenario of a few years of running
requires backgrounds to be controlled at the level b ≲0.1, with background index b expressed
– 1 –


## Page 3


in units of counts per ton per year per in the energy region of interest (ROI). This condition is,
unfortunately, not satisﬁed by any existing technology.
The backgrounds to 0νββ searches can be divided into two classes. The ﬁrst of these is
the two-neutrino process A
ZX →A
Z+2 X +2e−+2¯ν, which is expected to occur at a rate at least 106
higher than the neutrinoless mode. The only way to distinguish the neutrinoless mode from the two-
neutrino mode is by sufﬁciently precise reconstruction of the event energy. For xenon detectors, an
energy resolution better than ≲2% FWHM at the Q-value for 0νββ, Qββ, is required to achieve
a background index of b2ν ≲0.1 from the two-neutrino mode. Energy resolution is sufﬁciently
critical for the sensitivity of the experiment that a signiﬁcant margin of safety in the experimental
design is desirable. An energy resolution of 1.0% FWHM at 662 keV has been demonstrated using
high pressure gaseous xenon (HPGXe) detectors [4]. If extrapolation to Qββ is not compromised by
systematics, an energy resolution of 0.57% may be realized. The presently commissioning NEXT-
NEW detector will test the extrapolation of this resolution to larger experimental scales [5]. The
energy resolutions of present generation liquid xenon (LXe) and liquid-scintillator-dissolved xenon
(LSXe) detectors are 3.6% and 11.1% FWHM respectively [1, 2], giving background indices from
the two-neutrino mode of 1 and 84 for these two technologies [1, 6].
The second class of backgrounds is from ambient radioactivity and detector materials. None
of the contemporary experimental techniques that have placed signiﬁcant limits has been free of
such backgrounds. Levels of experimentally determined or projected background for current con-
tenders lie in the range 4 < b < 300 according to an independent assessment [7]. That assessment
reported overall background indices, after all cuts, of 9 (HPGXe), 130 (LXe) and 210 (LSXe)1, all
signiﬁcantly in excess of the target value b ≲0.1. There are four known ways to further remove
radioactive backgrounds:
• Improve energy resolution
• Implement or improve event topology reconstruction
• Improve radiopurity and / or shielding
• Implement decay daughter identiﬁcation (tagging)
Improved energy resolution allows a smaller ROI to be deﬁned around Qββ, thus reducing
contributions from backgrounds with broad energy spectra. The energy resolutions of various
xenon-based technologies were discussed above. Event topological reconstruction involves distin-
guishing the two-electron signature of real double beta decay events from the signatures of beta-
and gamma-induced backgrounds. In HPGXe detectors, for example, simulations indicate that a
factor of approximately 10−7 background suppression for γ-induced events can be obtained through
differences in topological characteristics.
Despite the clear power of energy and topological reconstruction as background rejection tools,
achieving a further factor of 100 improvement for the present lowest-background technologies
appears to be a formidable task. The third method, background reduction by improved radio-
purity and shielding, represents an attempt to assert that an event satisfying all true event criteria is
1Since the report, a campaign to remove 110mAg from Kamland-Zen has led to reduction of this background. Publi-
cation [1], reporting only the background in the inner 25% of the ﬁducial volume, shows a factor two improvement.
– 2 –


## Page 4


unlikely to be background; credibility thus depends crucially on credibility of a background model.
At the ton-scale, it will be extremely difﬁcult to demonstrate a priori that the background level is
b < 0.1, however heroic the radio-purity campaign.
An alternative approach – to assert that an event is both very likely to be a true event and very
unlikely to be a background event – may turn out to be an essential step. Detection of creation of a
daughter atom, in space and time, is the only known concept to realize such a powerful event-by-
event criterion. The double beta decay of 136Xe in either gas [8] or liquid [9, 10, 11], appears to
offer opportunities to develop this capability.
Both HPGXe and LXe time projection chambers (TPCs) are being actively pursued as pos-
sible 0νββ technologies. Each medium has distinct advantages and disadvantages: HPGXe pro-
vides ﬁne energy resolution and topological signature, whereas LXe offers the possibility of self-
shielding using a monolithic volume of enriched xenon to produce an effectively lower-background
inner region. The two media also invite different approaches to the problem of barium tagging. To
our knowledge, no barium tagging method has yet been proposed for LSXe detectors.
In this paper we present a novel barium tagging method for HPGXe detectors using single
molecular ﬂuorescent imaging (SMFI) [12, 13]. SMFI is based on conversion of weakly ﬂuorescent
molecular precursors into strongly ﬂuorescent ones by chelation with doubly charged ions, and has
become a major element in the arsenals of contemporary biology and biochemistry2. In xenon gas,
at or near room temperature, it appears plausible that single barium ions may be captured leading to
a detectable ﬂuorescent state. If this is the case, these techniques may be extendable to the problem
of 0νββ at the ton-scale and allow the realization of an essentially background-free experiment.
2. Xenon TPC detectors and barium tagging
Detection of the daughter atom in 0νββ has been long recognized as a strong positive criterion for
discovery [14], since no conventional process can introduce a new atom with Z+2. In the decay
136Xe to barium, with or without neutrinos, it is very likely that the disruptive departure of the
nascent electrons from the nucleus will leave the daughter barium atom in a highly ionized state
[15]. The barium ion rapidly captures electrons from nearby neutral xenon atoms until further cap-
ture is energetically disfavored. The process stops at the doubly ionized state Ba++ because the
second ionization potential of barium (10.004 eV) is very far below the ﬁrst ionization potential
of xenon (12.14 eV), relative to kT. Depending on xenon density, nearby free electrons liberated
by the two emergent beta particles can further neutralize the Ba++ ion. In LXe, electrons thermal-
ize very near to sources of ionization leading to signiﬁcant charge recombination, so the taggable
barium ions are expected to be distributed across the Ba, Ba+ and Ba++ charge states. This expec-
tation is supported by measurements made by the EXO collaboration, which show a distribution
of charge states in ions produced in decays of radon daughters in LXe [16]. In pure xenon gas, at
atomic densities nearly two orders of magnitude smaller than LXe, our simulations indicate that
recombination is very unlikely and that the dication Ba++ will be the dominant outcome. This
feature alone implies that different barium tagging methods may be optimal for each medium.
2The 2014 Nobel Prize in Chemistry was awarded to three physicists for their seminal contributions to SMFI.
– 3 –


## Page 5


Previous barium tagging work in liquid xenon
To detect the barium daughter in LXe, attention has been given by others to spectroscopic fea-
tures of the singly ionized state, Ba+. This atomic conﬁguration permits a sequence of repetitive
excitation/de-excitation cycles with alternating red and blue light involving a long-lived triplet D
state [14]. However, this sequence must be performed in an ion trap, which must be held at a high
quality vacuum to prevent collisional broadening [17] and rapid quenching of the D state. Repeated
detection of an alternating sequence of photons of two colors from a single atom is nevertheless a
robust determination of the presence of Ba+.
An alternative approach is to perform the ﬂuorescence cycle in a crystal of frozen xenon [18].
To identify barium ions in a running LXe detector using this method, a cryogenic probe must
be inserted into the active volume of the TPC at the position of an observed 0νββ candidate to
execute an electrostatic capture. After electrostatic capture of the ion, a localized region is frozen.
This solid xenon block can be either spectroscopically probed in situ, or extracted for probing
outside the detector [19]. In practice, the sequence of extraction from a large mass of high-purity
cryogenic liquid, reliable conversion to a singly charged state, efﬁcient transport into a low-pressure
trap or solid probe region and extended spectral interrogation, with credible spatial and temporal
correlation to the 0νββ event candidate, is clearly challenging and is not yet demonstrated.
Previous barium tagging work in gaseous xenon
Gas-phase barium tagging has also been explored [9, 10, 11]. Because Ba++ has a noble-gas-like
electronic shell conﬁguration, it does not have low-energy transitions which can be exploited for
atomic ﬂuorescence tagging. For this reason, the primary approach to gas-phase barium tagging
has been to convert Ba++ into Ba+, transport it efﬁciently to from its origin to a vacuum trap via
an RF carpet and differential pumping, then capture and probe the singly-charged state using the
two-color method.
3. Single molecule ﬂuorescent imaging
In this paper we describe a new method for automatic in situ identiﬁcation of Ba++ in high pres-
sure xenon gas, based on the technique of Single Molecular Fluorescence Imaging. Developed
Figure 1. The structure of Fluo-3 is shown before and after complex formation [20].
– 4 –


## Page 6


Fluorescein	
  
BAPTA	
  
Fluo-­‐3	
  
Fluo-­‐4	
  
F	
  
F	
  
Figure 2. Structures of some important molecules described in this paper : ﬂuorescein, BAPTA, Fluo-3 and
Fluo-4.
originally by physicists, Single Molecular Fluorescence Imaging (SMFI) has been adopted and ad-
vanced by biologists and chemists to an array of highly sophisticated techniques. In SMFI, a small
optically thin region is interrogated repeatedly with typically blue or near-UV photons that excite
a molecule of interest. If the molecule is complexed with a doubly charged ion, often Ca++ in bio-
logical studies, the resulting adduct ﬂuoresces strongly, whereas ion-free un-complexed molecules
respond very weakly. Image-intensiﬁed CCD cameras are used to detect single photons with pixel-
scale spatial resolution. Repeated interrogations provide statistically precise identiﬁcation and lo-
calization of a single molecule—even inside living cells. The interrogation rate can exceed 105 per
second and ﬂuorescence quantum yields approach unity in many cases. Fluorescence detection is
facilitated by an inherent Stokes shift or a delay in response time relative to pulsed excitation.
A wide variety of molecules for SMFI purposes now exists. Of interest are ﬂuorophores such
as Fluo-3, Fluo-4, and Rhod-2 which chelate Ca++. Calcium chelation by Fluo-3, one of the most
commonly used calcium sensitive in ﬂuoresence microscopy, is shown schematically in Fig. 1 [20].
Fluo-4 is chemically similar to Fluo-3, but with the chlorine atoms replaced by ﬂuorine for a higher
light yield and increased stability against photobleaching. Rhod-2 is a derivative of rhodamine with
correspondingly longer wavelength ﬂuorescence response, commonly used in two-color imaging.
For this work we have focussed on Fluo-3 and Fluo-4 dyes, though Rhod-2 and dyes more specially
tailored for barium [21] appear to hold equal promise given our current understanding.
Fluo-3 and Fluo-4 are both derived from the ﬂuorescein molecule, which is shown in Figure 2,
top left. The excitation and emission spectra of ﬂuorescein, calcium chelated Fluo-3 and calcium
chelated Fluo-4 are shown in Figure 3. All these ﬂuors have excitation that peaks in the blue
with emission in the green, though Fluo-3 has a somewhat different wavelength dependence to
the others, making it slightly less bright at our chosen excitation wavelength of 488 nm. Fluo-
3 and Fluo-4, shown in Figure 2, bottom left and right, effectively consist of a ﬂuorescein-like
molecule bonded to a calcium-chelating molecule called BAPTA, which is shown in Figure 2,
– 5 –


## Page 7


Figure 3. Absorption (dashed) and emission (solid) spectra of ﬂuorescein precursor, and chelated Fluo-3
and Fluo-4 dyes, using data reported by [25]
top right. When the molecule is isolated from doubly charged ions, the BAPTA-like part has many
vibrational degrees of freedom, allowing de-excitation of the ﬂuorescein-like part without emission
of a photon. Thus non-chelated Fluo-3 and Fluo-4, when excited with blue light, de-excite non-
radiatively. In the presence of Ca++, on the other hand, the BAPTA-like part of the molecule forms
a rigid cage around the ion, which has the effect of redistributing electrons within the complex and
preventing vibrational de-excitation, thus restoring the ﬂuorescence emission from the ﬂuorescein-
like part. In this way, the dye transitions from a non-ﬂuorescent state to a ﬂuorescent one in the
presence of Ca++, making it a powerful tool for calcium sensing [22, 23, 24].
Quoted response ratios between unchelated and calcium-chelated states of Fluo-3 and Fluo-4
vary from 60 to more than 100 in biological milieu. Although barium is uncommon in biochemistry
research, the fact that barium and calcium are congeners suggests that techniques for Ca++ may
have relevance for Ba++, and that dyes developed for calcium sensitivity may be used directly for
barium tagging. In the next section we study the properties of Ba++-chelated Fluo-3 and Fluo-
4, and implement a detection system which we intend to use for studying dye chelation remotely
inside a xenon gas environment.
4. SMFI for barium detection
The difﬁcult process of realizing SMFI-based barium tagging can be broadly broken into four steps
of increasing difﬁculty: 1) identify dyes which provide a strong ﬂuorescent response to barium
dications; 2) develop a scanning system which can be used to tag barium ions remotely inside
a large detector; 3) establish whether the chelation and ﬂuorescence behavior is maintained in a
HPGXe environment; 4) optimize the detection technique to the single molecule regime. In this
section we describe progress on items (1) and (2), and Section 5 will brieﬂy outline plans to address
item (3) as the next immediate goal. Extension to the single molecule regime is not described
in this paper, though single ion detection with these techniques has precedents, both in aqueous
solutions and in living organisms. Assuming chelation does occur in gas, single ion sensitivity in
HPGXe is plausibly achievable, helped by the fact that the inert environment of a HPGXe detector
– 6 –


## Page 8


Figure 4. Photograph (top) and diagram (bottom) of the optical system.
is expected to be more favorable to survival of the dye/Ba++ complex than aqueous environments
where photobleaching by reactive oxygen species is a limiting effect [22, 23].
For the studies described in this paper we use a 488 nm argon ion laser as an excitation light
source. Our goal is to demonstrate sensing of barium dications at a remote location using a ﬁber-
coupled optical system. For gas-phase tests, this will be connected to a total internal reﬂection
ﬂuorescence sensor, described in Section 5. The optical system is shown in Figure 4. Excitation
light is coupled into a 1000 µm high numerical aperture (0.5 NA) multimode ﬁber using a 20×
microscope objective (Olympus pln20x with 0.4 NA). The ﬁber carries the excitation light to a
– 7 –


## Page 9


400
450
500
550
600
650
Wavelength / nm
0
20
40
60
80
100
Reflection or Transmission
transmission of DM
reflection of DM
short pass filter
long pass filter
450
460
470
480
490
500
Wavelength / nm
10-3
10-2
10-1
100
Intensity (arb. units)
Laser - unfiltered
Laser - filtered
Figure 5. Left: The transmission/reﬂection of the DM overlayed with the transmission of the SPF and LPF.
Right: Argon ion laser spectrum before and after excitation ﬁltering. The dominant feature is the laser peak
at 488 nm. Secondary peaks such as the one at 470 nm are removed by the ﬁlter optics.
cuvette containing the ﬂuorescent mixture approximately 1 m away. To avoid introducing long-
wavelength background light into the sample, the laser light is ﬁltered ﬁrst with a 488 nm laser line
ﬁlter, and then with a 500 nm short pass ﬁlter, before being reﬂected from a dichroic mirror (DM)
with 500 nm cutoff wavelength. The excitation power was measured at the sample, and we ﬁnd that
in idle mode the laser produces 110 µW at sample and when run at full power can deliver 1.1 mW.
A fraction of the sample ﬂuorescence emission is captured and guided back along the ﬁber
with the >500 nm component passing through the dichroic mirror. This long wavelength light is
focussed by a second 20× objective into a ﬁber which runs to a CCD spectrometer (CCS100 from
Thorlabs). The excitation optics were aligned using the 488 nm laser with a neutral density ﬁlter
at the aperture, and the detection optics were aligned using a red HeNe laser focussed into the far
end of the ﬁber to maximize transmission. The full system is operated inside a dark box, with the
spectrometer on the outside connected using an SMA optical ﬁber feedthrough. A plot showing
the short-pass, long-pass, and dichroic transmission and reﬂection spectra in Figure 5, left, and the
ﬁltered and unﬁltered laser power spectrum are shown in Figure 5, right.
The samples used in these studies are aqueous solutions held in plastic cuvettes, placed inside a
custom-made cuvette holder that ﬁxes the ﬁber at a constant height in the solution. The system was
exercised ﬁrst with ﬂuorescein solution since it has approximately the same ﬂuorescence spectrum
as chelated Fluo-4 and can be studied independently of the degree of chelation. In calibration
runs we observed a pH dependence to the ﬂuorescence intensity of ﬂuorescein, shown in Figure
6, left. For this reason, in all subsequent studies a pH buffer consisting of imidazole and HCl is
used to hold the solution at pH 7.2. This is necessary because the ionic barium compounds we
will introduce into the solution are somewhat basic, whereas Fluo-4 is a carboxylic acid derivative.
Thus, testing these at various concentrations without a buffer would introduce undesirable effects
on the ﬂuorescence from pH changes alone. To ensure the pH was properly stabilized, several of
– 8 –


## Page 10


0.0
0.2
0.4
0.6
0.8
1.0
Buffer to Total Volume Ratio
4
5
6
7
8
pH 
6
8
10
12
14
16
Intensity in ROI (arb. units)
450
475
500
525
550
575
600
625
Wavelength / nm
0.0
0.2
0.4
0.6
0.8
1.0
Intensity (arb. units)
10µM Fluorescein
5µM Fluorescein
1µM Fluorescein
0µM Fluorescein
Figure 6. Left: pH dependence of ﬂuorescein emission, which led us to stabilize solutions with imidazole /
HCl buffer. Right: detected ﬂuoresence spectrum from pH-stabilized ﬂuorescein solutions probed with the
ﬁber detection system.
the samples described were tested for their pH after scanning, and a consistent result pH∼7 was
obtained in all cases. Such stabilization will not be required in HPGXe, since the concept of pH is
not applicable in dry environments.
To make ﬂuorescein test samples, ﬁrst a 100 µM stock solution of ﬂuorescein was mixed.
Samples made from the stock solution had a ﬁnal volume of 550 µL. They contained 50 µL of
the buffer solution, and the other 500 µ L was pure water and ﬂuorescein stock solution mixed to
the desired molality by micro-pipette. The detected ﬂuorescence spectra for various quantities of
ﬂuorescein dye are shown in Figure 6, right. It is notable that following emission and excitation
ﬁltering, the background at the excitation wavelength from the laser is suppressed to negligible
levels at the CCD. An approximately linear relationship between ﬂuorescein concentration and ﬂu-
orescence intensity is observed. The repeatability of the measurement was quantiﬁed by preparing
ﬁve independent samples and scanning them, giving a spread of 2.5 % between measurements,
which is affected both by the reproducibility of the solutions and the placement of the ﬁber. This
number can be taken as an estimate of the systematic uncertainty on relative measurements in all
subsequent studies.
Once the system was conﬁgured for sensitivity at the appropriate emission wavelengths, Ba++
detection studies were instigated. A stock solution of ﬂuorophore was mixed to 100µM. Fluo-3
and Fluo-4 are highly sensitive dyes with dissociation constant (kd) in the nano-molar range, and
even in the very clean water used for these studies (Sigma Aldrich ACS reagent, for ultratrace
analysis) the residual calcium ion concentration of 0.2 µg/kg (5 nM) gave a signiﬁcant ﬂuorescent
background. To suppress this background we use a standard method in high-sensitivity calcium
detection [26], which is to introduce the non-ﬂuorescent chelator BAPTA which eliminates the
majority of the free ions. During optimization of our protocol we also found the background could
be reduced by using plastic rather than glass vials and by rinsing all elements with three washes of
– 9 –


## Page 11


450
475
500
525
550
575
600
625
Wavelength / nm
0.0
0.2
0.4
0.6
0.8
1.0
Intensity (arb. units)
Fluo-4
Fmax
Fmin = 85. 22
460µM Ba+ +
291µM Ba+ +
235µM Ba+ +
177µM Ba+ +
118µM Ba+ +
60µM Ba+ +
0µM Ba+ +
450
475
500
525
550
575
600
625
Wavelength / nm
0.0
0.2
0.4
0.6
0.8
1.0
Intensity (arb. units)
Fluo-4
Fmax
Fmin = 291. 83
497µM Ca+ +
449µM Ca+ +
400µM Ca+ +
352µM Ca+ +
302µM Ca+ +
203µM Ca+ +
102µM Ca+ +
51µM Ca+ +
0µM Ca+ +
450
475
500
525
550
575
600
625
Wavelength / nm
0.0
0.2
0.4
0.6
0.8
1.0
Intensity (arb. units)
Fluo-3
Fmax
Fmin = 17. 4
348µM Ba+ +
142µM Ba+ +
106µM Ba+ +
71µM Ba+ +
36µM Ba+ +
0µM Ba+ +
450
475
500
525
550
575
600
625
Wavelength / nm
0.0
0.2
0.4
0.6
0.8
1.0
Intensity (arb. units)
Fluo-3
Fmax
Fmin = 254. 77
265µM Ca+ +
228µM Ca+ +
191µM Ca+ +
153µM Ca+ +
115µM Ca+ +
77µM Ca+ +
39µM Ca+ +
0µM Ca+ +
Figure 7. Ca++ (left) and Ba++ (right) induced ﬂuorescence in Fluo-4 (top) and Fluo-3 (bottom) dye
solutions. These dyes, developed for calcium dication detection, show a clear afﬁnity for barium dications,
making them potentially suitable for SMFI in high pressure xenon gas TPCs.
clean water.
A sample was mixed with Fluo-3 or Fluo-4 to a volume of 500 µL, containing 50 µL of buffer
solution, 260 µM BAPTA, 10 µM of ﬂuorophore. We measured both the response to Ca++ ions
and the response to Ba++ ions in different concentrations. At some ion concentration the sig-
nal saturates at ﬂuorescence intensity Fmax, and we report the relative size of the saturated signal
strength to the background ﬂuorescence level, Fmin. Curves for intermediate ion concentrations can
be normalized to these numbers. Dications were added in the form of calcium / barium perchlorate,
which dissociates readily in solution into Ca++ / Ba++ and ClO−
4 ions. The salt was pre-mixed at
a concentration of 5.95 mM for barium perchlorate and 6.43 mM for calcium perchlorate, this con-
centrated solution allowing a sizable ion concentration to be added to pre-mixed samples without
– 10 –


## Page 12


signiﬁcant volume change or dilution.
Both calcium and barium induced ﬂuorescence were clearly observed in both Fluo-4 and Fluo-
3 samples, at concentrations between 30µM and 500 µM. At the peak ﬂuorescence intensity, the
signal to background ratio (Fmax/Fmin) is 85.22 for barium and 291.83 for calcium in Fluo-4, and
17.40 for barium and 254.77 for calcium in Fluo-3. The background before any dications were
added is believed to derive from uncaptured free Ca++ and other free metal ions in the puriﬁed
water. The maximum signal to background ratio is driven by this background intensity and by the
saturation point of the dye with each cation type. Both dyes show a higher afﬁnity for calcium than
barium, but the difference in afﬁnities is signiﬁcantly smaller for Fluo-4 than Fluo-3, as shown by
the improved signal-to-background ratio. The emission spectrum for barium- and calcium-chelated
dyes are found to be almost identical in shape, though both Fluo-3 and Fluo-4 have a barium-
chelated spectrum peaking at wavelengths 2-3 nm shorter than the calcium-chelated spectrum.
The clear observation of barium-induced ﬂuorescence demonstrates that 1) Fluo-3 and Fluo-4
are suitable dyes for barium sensing and that 2) our remote scanning system is capable of barium
ion detection at the end of a ﬁber. The small residual background, though not problematic for
this investigation, will be the focus of further optimization. Although no free Ca++ or other doubly
charged metal dications are expected in HPGXe detectors, preparation of barium-sensitive coatings
which are free of pre-chelated molecules is an important requirement for production of sensitive
single-barium-ion sensors. Other chelators including EGTA and EDTA [27], as well as calcium
sponges with BAPTA-like molecules bonded onto polystyrene beads [28] are available for these
purposes and are being investigated. Furthermore, as well as suppressing the free-ion background,
BAPTA also competes with the SMFI dyes when dications are introduced, thus reducing ﬂuores-
cence response per ion. For this reason, addition of BAPTA in sensors for dry environments is to
be avoided where single ion sensitivity is desired.
5. Prospects for testing SMFI barium sensors in xenon gas
In the previous section we described the development of a system for sensing production of barium
dications using a ﬁber-coupled optical system. The next stage of this work is to translate these stud-
ies from an aqueous environment to a dry noble gas. We are presently constructing a high-pressure
xenon test stand with a barium plasma source which will deliver a beam of Ba++, separated from
the plasma by time-of-ﬂight, into a sensing region where barium-sensitive electrodes can be tested.
This device will be used to establish whether barium-sensitive SMFI dyes continue to function in
HPGXe environments.
The barium sensing concept we will deploy is based on total internal reﬂection ﬂuorescence
(TIRF) microscopy. In TIRF, the evanescent electromagnetic wave at a light-guide or ﬁber surface
excites ﬂuorophores within a few hundred nanometers of the interface. This is shown schematically
in Figure 8, left from [29], and is a common microscopy technique in biological sciences. It is
especially appropriate for tasks where speciﬁc sensitivity to near-surface ﬂuorophores is desirable.
Figure 8, right shows data from [30] where TIRF was used to reveal the actin polymerization
bursts at endocytic sites in mammalian cells. Reviews of the technique applied to both single- and
multiple-molecular ﬂuorescence imaging can be found in [31, 32].
– 11 –


## Page 13


For our detection elements, we will place a relatively negative cathode behind a coated ﬁber
to focus drifting positive ions onto a region where a coating of barium-sensitive dye has been
deposited onto the ﬁber surface. Because the ﬂuorescent molecules of the coating are emitting in
the near-ﬁeld regime relative to the dielectric interface, evanescent excitation of the ﬂuorophore will
result in some ﬂuorescence emission back into the ﬁber. This returning light will be dichroically
separated, using the same system used in the aqueous studies of Section 4.
The major questions to be addressed by these studies are:
• Can SMFI dyes be used for ion detection in a non-aqueous environment?
• What are the ﬂuorescence yields and spectroscopic properties of such dyes in HPGXe?
• What is the barium capture efﬁciency in HPGXe?
• What are the drift properties (mobility, diffusion, etc) of Ba++ in HPGXe and can it be
efﬁciently focused onto a detection element?
Our TIRF-based sensors can only be properly operated in a dry environment, since the coating
is water-soluble. However, as a ﬁrst test of our sensitivity to TIRF ﬂuorescence a preliminary study
was made using a 4 µL droplet of ﬂuorescein solution. A clean ﬁber with the outer jacket removed
was placed with its side in the droplet. Fluorescence light is generated which is both visible by
eye and detectable in our spectrometer. Light emitted outside the ﬁber cannot enter a ﬁber mode
unless it was produced by a ﬂuorophore in the near-ﬁeld regime to the ﬁber/water interface - this
tells us that the detected green light seen at the spectrometer is a result of TIRF ﬂuorescence.
A photograph of this test and the spectrometer output are shown in Figure 9. Using this system
and a barium sensitive SMFI dye coating, we plan to use the methods described in this paper to
detect Ba++ ions isolated by our HPGXe barium ion source. This work will be presented in future
publications.
5μm	
  
Figure 8. Left: illustration showing the use of TIRF to identify actin polymerization bursts in mammalian
cells, from [29]. Right: image from a similar study, published in [30]
– 12 –


## Page 14


Figure 9. Left: Photograph showing TIRF excitation. Visible green ﬂuorescence light emanates from a bead
of liquid at the side of a ﬁber. Right: Fluoresence response as seen at the spectrometer, showing that some
of the emitted light couples back into the ﬁber modes due to TIRF emission in the near-ﬁeld regime.
6. Conclusions
To discover Majorana neutrinos even in the most pessimistic cases allowed by the inverted mass
ordering requires ton-scale experiments and a background rejection capability sufﬁcient to achieve
b < 0.1 ct (ROI) ton−1 yr−1. Meeting this challenge requires suppression of backgrounds rates by a
factor of 40 to 3000, perhaps beyond the capabilities of existing technologies. Thus, the technical
challenge presented to the 0νββ ﬁeld is very substantial, if not daunting.
Techniques that can reliably identify the daughter ion in 0νββ experiments are strongly mo-
tivated since these could provide a nearly background-free positive criterion for discovery. In this
paper we have outlined a new concept for barium daughter tagging in high-pressure xenon gas TPCs
using the technique of SMFI. SMFI techniques are routinely used with single molecule sensitivity
in living cells and aqueous media and may hold promise for ton-scale 0νββ detectors.
By using a dye optimized for sensitivity to Ca++ we have developed a sensor which can detect
the presence of bulk Ba++ ions in aqueous solution using a ﬁber-coupled optical system. Signal
to background ratios as large as 85 have been achieved for barium detection with this device. This
sensitivity is sufﬁcient for explorations of whether this dye and others like it can capture barium
ions and exhibit Ba++-induced ﬂuorescence in dry noble environments.
The next step of this R&D program involves operating a total internal reﬂection ﬂuorescence
(TIRF) sensitive electrode coupled to our optical system under exposure to a pure Ba++ beam in
xenon gas. Positive results would suggest signiﬁcant promise in the SMFI barium tagging concept
and a possible path to discovery for the ﬁeld of neutrinoless double beta decay.
– 13 –


## Page 15


Acknowledgments
We thank Rasika Dias and Sandy Dasgupta of UT Arlington for helpful chemistry guidance, and
Sebastian Raquena and Zygmunt (Karol) Gryczynski of Texas Christian University for valuable
early discussions about SMFI. Thanks also to Jonathan Asaadi for a careful reading of this paper
and insightful comments. This work was supported by the University of Texas at Arlington.
References
[1]
A. Gando et al. “Search for Majorana Neutrinos near the Inverted Mass Hierarchy Re-
gion with KamLAND-Zen”. In: Phys. Rev. Lett. 117 (2016), p. 082503. DOI: 10.1103/
PhysRevLett.117.082503. arXiv:1605.02889 [hep-ex].
[2]
J. B. Albert et al. “Search for Majorana neutrinos with the ﬁrst two years of EXO-200 data”.
In: Nature 510 (2014), pp. 229–234. DOI: 10.1038/nature13432. arXiv:1402.6956
[nucl-ex].
[3]
Nuclear Science Advisory Committee. “Long Range Plan For Nuclear Science”.
[4]
Electroluminescent Tpc. “Near-Intrinsic Energy Resolution for 30 to 662 keV Gamma Rays
in a High Pressure Xenon”. In: (2012). arXiv:arXiv:1211.4474v1. URL: https:
//arxiv.org/pdf/1211.4474v1.pdf.
[5]
Next Collaboration. “Development of NEW , towards the ﬁrst physics results of NEXT”. In:
Nucl.Part.Phys.Proc. 275 (2016), pp. 2621–2623. DOI: 10.1016/j.nuclphysbps.
2015.10.009.
[6]
Caio Licciardi. “Recent Results and Status of the EXO-200 and the nEXO Experiment”.
Talk at the ICHEP2016 Conference.
[7]
Nuclear Science Advistory Committee. “NSAC Long Range Planning Meeting”. Neutrino-
less Double Beta Decay, Kitty Hawk, NC, April 18, 2015.
[8]
D. Nygren. “Detection of the barium daughter in 136Xe ->136Ba + 2e- by in situ single-
molecule ﬂuorescence imaging”. Frontier Detectors for Frontier Physics, Elba, Italy, May
24-30, To be published in Nuclear Instruments and Methods in Physics Research Section A:
Accelerators, Spectrometers, Detectors and Associated Equipment, 2016. 2016.
[9]
Thomas Brunner et al. “An RF-only ion-funnel for extraction from high-pressure gases”. In:
International Journal of Mass Spectrometry 379 (2015), pp. 110–120. DOI: 10.1016/j.
ijms.2015.01.003. arXiv:1412.1144 [physics.ins-det].
[10]
B. Flatt et al. “A linear RFQ ion trap for the Enriched Xenon Observatory”. In: Nuclear
Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, De-
tectors and Associated Equipment A578 (2007), pp. 399–408. DOI: 10.1016/j.nima.
2007.05.123. arXiv:0704.1646 [physics.ins-det].
[11]
D. Sinclair et al. “Prospects for Barium Tagging in Gaseous Xenon”. In: Journal of Physics
Conference Series 309 (2011), p. 012005. DOI: 10 . 1088 / 1742 - 6596 / 309 / 1 /
012005.
– 14 –


## Page 16


[12]
Bernard Valeur and Mário Nuno Berberan-Santos. Molecular ﬂuorescence: principles and
applications. John Wiley & Sons, 2012.
[13]
Joseph R Lakowicz. Principles of ﬂuorescence spectroscopy. Springer Science & Business
Media, 2013.
[14]
M. K. Moe. “New approach to the detection of neutrinoless double beta decay”. In: Physical
Review C44 (1991), pp. 931–934. DOI: 10.1103/PhysRevC.44.931.
[15]
Alex E. S. Green. “Single Electron Shakeoff Probability Following the Beta Decay of Kryp-
ton”. In: Physical Review 107 (6 1957), pp. 1646–1650. DOI: 10.1103/PhysRev.107.
1646. URL: http://link.aps.org/doi/10.1103/PhysRev.107.1646.
[16]
J. B. Albert et al. “Measurements of the ion fraction and mobility of alpha- and beta-
decay products in liquid xenon using the EXO-200 detector”. In: Phys. Rev. C 92 (4 2015),
p. 045504. DOI: 10.1103/PhysRevC.92.045504. URL: http://link.aps.
org/doi/10.1103/PhysRevC.92.045504.
[17]
M. Danilov et al. “Detection of very small neutrino masses in double beta decay using laser
tagging”. In: Physics Letters B480 (2000), pp. 12–18. DOI: 10.1016/S0370-2693(00)
00404-4. arXiv:hep-ex/0002003 [hep-ex].
[18]
B. Mong et al. “Spectroscopy of Ba and Ba+ deposits in solid xenon for barium tagging in
nEXO”. In: Physical Review A91.2 (2015), p. 022505. DOI: 10.1103/PhysRevA.91.
022505. arXiv:1410.2624 [physics.atom-ph].
[19]
K. Twelker et al. “An apparatus to manipulate and identify individual Ba ions from bulk
liquid Xe”. In: Review of Scientiﬁc Instruments 85 (2014), p. 095114. DOI: 10.1063/1.
4895646. arXiv:1407.0618 [physics.ins-det].
[20]
Dojindo Molecular Industries, Inc. Japan.
[21]
Yoshio Nakahara, Toshiyuki Kida, Yohji Nakatsuji, and Mitsuru Akashi. “A novel ﬂuores-
cent indicator for Ba 2 + in aqueous micellar solutions”. In: Chemical Communications 1
(2004), pp. 224–225. URL: http://pubs.rsc.org/en/content/articlepdf/
2004/cc/b311613a.
[22]
D Thomas, S C Tovey, T J Collins, M D Bootman, M J Berridge, and P Lipp. “A com-
parison of ﬂuorescent Ca2+ indicator properties and their use in measuring elementary and
global Ca2+ signals.” In: Cell calcium 28.4 (2000), pp. 213–23. ISSN: 0143-4160. DOI:
10 . 1054 / ceca . 2000 . 0152. URL: http : / / www . sciencedirect . com /
science/article/pii/S0143416000901520.
[23]
a E Oliver, G a Baker, R D Fugate, F Tablin, and J H Crowe. “Effects of temperature on
calcium-sensitive ﬂuorescent probes.” In: Biophysical journal 78.April (2000), pp. 2116–
2126. ISSN: 00063495. DOI: 10.1016/S0006- 3495(00)76758- 0. URL: http:
//dx.doi.org/10.1016/S0006-3495(00)76758-0.
[24]
R Madelaine Paredes, Julie C Etzler, Lora Talley Watts, and James D Lechleiter. “NIH Pub-
lic Access”. In: 46.3 (2009), pp. 143–151. DOI: 10.1016/j.ymeth.2008.09.025.
Chemical.
– 15 –


## Page 17


[25]
Thermo Fisher Scientiﬁc. “Thermo Fisher Fluoresence SpectraViewer”. https://www.
thermofisher . com / us / en / home / life - science / cell - analysis /
labeling-chemistry/fluorescence-spectraviewer.html.
[26]
Iain Johnson and Michelle T.Z. Spence. Molecular Probes Handbook, A Guide to Fluores-
cent Probes and Labeling Technologies, 11th Edition. Invitrogen, 2010.
[27]
J A McGuigan, D Lüthi, and A Buri. “Calcium buffer solutions and how to make them: a
do it yourself guide.” In: Canadian journal of physiology and pharmacology 69.11 (1991),
pp. 1733–49. ISSN: 0008-4212. DOI: 10.1139/y91-257. URL: http://www.ncbi.
nlm.nih.gov/pubmed/1804518.
[28]
Molecular Probes. “Calcium Sponge S”. https://tools.thermofisher.com/
content/sfs/manuals/mp03040.pdf.
[29]
Marko Kaksonen, Christopher P Toret, and David G Drubin. “Harnessing actin dynamics for
clathrin-mediated endocytosis”. In: Nature Reviews Molecular Cell Biology 7.6 (June 2006),
pp. 404–414. ISSN: 1471-0072. URL: http://dx.doi.org/10.1038/nrm1940.
[30]
Christien J Merriﬁeld. “Seeing is believing: imaging actin dynamics at single sites of endocy-
tosis”. In: Trends in Cell Biology 14.7 (Oct. 2015), pp. 352–358. DOI: 10.1016/j.tcb.
2004.05.008. URL: http://dx.doi.org/10.1016/j.tcb.2004.05.008.
[31]
Kenneth N Fish. “Total Internal Reﬂection Fluorescence (TIRF) Microscopy”. In: Current
protocols in cytometry / editorial board, J. Paul Robinson, managing editor ... [et al.] 0 12
(Oct. 2009), Unit12.18–Unit12.18. ISSN: 1934-9297. DOI: 10 . 1002 / 0471142956 .
cy1218s50. URL: http : / / www . ncbi . nlm . nih . gov / pmc / articles /
PMC4540339/.
[32]
N Stuurman and RD Vale. “Imaging single molecules using total internal reﬂection ﬂuo-
rescence microscopy”. In: Live Cell Imaging, A Laboratory Manual Cold Spring Harbor
Laboratory Press: Cold Spring Harbor, New York (2006), pp. 585–601.
– 16 –

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1609_04019v2_single_molecule_fluorescence_imaging_as_a_technique_for_barium_tagging_in_neutri
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1609_04019V2_SINGLE_MOLECULE_FLUORESCENCE_IMAGING_AS_A_TECHNIQUE_FOR_BARIUM_TAGGING_IN_NEUTRI.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

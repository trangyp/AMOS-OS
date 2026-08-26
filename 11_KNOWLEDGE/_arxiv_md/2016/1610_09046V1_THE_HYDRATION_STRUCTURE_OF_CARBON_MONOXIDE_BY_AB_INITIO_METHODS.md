---
canon-group: reference
rscf-state: source-claim
arxiv_id: 1610.09046v1
source: arxiv
tags: [arxiv, knowledge, quantum, reference]
---
# 1610.09046v1_The_Hydration_Structure_of_Carbon_Monoxide_by_Ab_Initio_Methods

> Source: 1610.09046v1_The_Hydration_Structure_of_Carbon_Monoxide_by_Ab_Initio_Methods.pdf

> Pages: 19

---


## Page 1


APS/123-QED
The Hydration Structure of Carbon Monoxide by Ab Initio Methods
Ernest Awoonor-Williams1 and Christopher N. Rowley1, a)
Department of Chemistry, Memorial University of Newfoundland, St. John’s, NL,
Canada
(Dated: 21 August 2018)
The solvation of carbon monoxide (CO) in liquid water is important for understand-
ing its toxicological eﬀects and biochemical roles. In this paper, we use ab initio
molecular dynamics (AIMD) and CCSD(T)-F12 calculations to assess the accuracy
of the Straub and Karplus molecular mechanical (MM) model for CO(aq).
The
CCSD(T)-F12 CO–H2O potential energy surfaces show that the most stable structure
corresponds to water donating a hydrogen bond to the C center. The MM-calculated
surface it incorrectly predicts that the O atom is a stronger hydrogen bond acceptor
than the C atom. The AIMD simulations indicate that CO is solvated like a hy-
drophobic solute, with very limited hydrogen bonding with water. The MM model
tends to overestimate the degree of hydrogen bonding and overestimates the atomic
radius of the C atom. The calculated Gibbs energy of hydration is in good agree-
ment with experiment (9.3 kJ mol−1 calc. vs 10.7 kJ mol−1 exptl.). The calculated
diﬀusivity of CO(aq) in TIP3P-model water was 5.19 × 10−5 cm2/s calc., more than
double the experimental value of 2.32 × 10−5 cm2/s.
PACS numbers: 61.20.Ja
a)Electronic mail: crowley@mun.ca
1
arXiv:1610.09046v1  [physics.chem-ph]  28 Oct 2016


## Page 2


I.
INTRODUCTION
Carbon monoxide (CO) is a highly toxic gas,1 with a OSHA Permissible Exposure Limit
of only 50 ppm.2 This toxicity originates from the coordination of CO to metalloproteins like
hemoglobin.3 Over the last two decades, CO has also been identiﬁed as a gasotransmitter
that serves as an endogenous signaling molecule in trace concentrations.4,5 This has spurred
the development of CO-releasing molecules (CORMs) to allow controlled delivery of carbon
monoxide to cellular targets.6–9
The intermolecular interactions of CO are remarkably complex. CO possesses a modest
dipole moment (µ0 = 0.12 D),10 but has a large negative quadrupole moment (Θzz =
(−8.77 ± 0.31) × 10−40 C m2).11 The origin of this quadrupole moment is apparent in the
calculated electrostatic potential (ESP) of CO; the ends of the molecule have a negative ESP
due to the C and O lone pairs, while the molecular surface in the vicinity of the C atom has
a positive ESP.12
Straub and Karplus developed an early molecular mechanical (MM) model of CO for
molecular dynamics (MD) simulations of CO–myoglobin dissociation.13 The model has a
Lennard-Jones terms centered at the C and O atoms.
Electrostatic interactions in this
model are described using 3 point charges; charges are placed on both the C and O atoms
as well as one on the C–O bond midpoint. This model has been used extensively to model
CO dynamics in biomolecular systems since then,14–21 although it has not been validated by
modern methods.
The structure and energetics of solute–solvent interactions can be challenging to study
experimentally, so it can be diﬃcult to validate empirical models like this based on experi-
mental quantities alone. Quantum chemical methods provide another approach for validat-
ing molecular mechanical models. High-level ab initio methods like CCSD(T) can now be
used routinely to calculate accurate interaction energies of small molecules. Similarly, ab
initio molecular dynamics (AIMD) can be used to generate a ﬁrst-principles comparison the
structure liquids and solutions by calculating the energy and forces using a quantum chemi-
cal method (e.g., density functional theory, DFT). These methods are valuable for providing
ﬁrst-principles estimates of the solvation structure and can be used to assess aspects of MM
models.22–27
In this paper, we compare the solvation of CO in liquid water calculated using the molec-
2


## Page 3


ular mechanical models of Straub and Karplus and an ab initio molecular dynamics simu-
lation. In support of this, we also calculate the potential energy surfaces (PES) for a water
molecule serving as a hydrogen bond donor and acceptor to a CO molecule using CCSD(T)-
F12. The solvation energy and diﬀusivity of the MM model in TIP3P-model water are also
compared to experiment.
II.
THEORY AND METHODS
A.
Ab Initio Calculations
The DFT and CCSD(T)-F12 CO–H2O potential energy surfaces and interaction energies
were calculated using TURBOMOLE v7.028. The CCSD(T) surface used the explicitly cor-
related F12 method29 using a density-ﬁtting basis set. The aug-cc-pVQZ basis set was used
for all atoms.30,31 The DFT calculations were performed using the PBE exchange-correlation
functional32 and the aug-cc-pVTZ basis set. The Grimme D3 correction for dispersion was
applied.33 The TURBOMOLE input ﬁle is included in Supplementary Information.
B.
Molecular Mechanical Calculations
1.
Parameters and Simulation Cell
Calculations of the MM CO–H2O potential energy surfaces and the MD simulations struc-
ture of CO(aq) were performed using CHARMM c40b2.34 The parameters for the Straub
and Karplus model for CO are given in Table I. The water molecules were represented using
the CHARMM variant of the TIP3P-model.35,36
For the simulations of CO in bulk water, a cubic simulation cell was used with an average
cell length of 30.8 ˚A. Lennard-Jones interactions were scaled to zero using a switching
function over the 10–12 ˚A range. Electrostatic interactions were calculated using the Particle
Mesh Ewald (PME) method using a 32 × 32 × 32 grid.37 The simulation cell contained 995
water molecules and 1 CO molecule. The simulations to calculate the solvation energies
and the radial distribution functions (rdf) used a Langevin thermostat (γ = 5 ps−1) and
an Andersen–Hoover barostat.38,39 The CHARMM input ﬁle is included in Supplementary
Information.
3


## Page 4


2.
Gibbs Energy of Hydration Calculations
The Gibbs energy of hydration for CO was calculated using the staged decoupling pro-
tocol of Deng et al.40,41.
The electrostatic and dispersion components of the hydration
energy were calculated by an 11-window thermodynamic integration simulation ( λ =
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, and 1.0).
The two states, denoted A and B, correspond to the states where the given solvent–
solute interaction is calculated or neglected, respectively. These states are coupled by the
thermodynamic integration (TI) variable λ, through the deﬁnition of a linearly-interpolated
potential,
V(λ) = (1 −λ)VA + λVB,
(1)
Here VA and VB are the potential energies of the A and B states.
The repulsive component of the Gibbs energy was calculated using a staged procedure
where the repulsive component of the solvent–solute Lennard-Jones interaction potential
was reduced to zero using a 9 stage free energy perturbation (FEP) approach.40,41
For each TI or FEP simulation, the system was equilibrated for 1 ns followed by a 2
ns sampling simulation. The Gibbs energies were calculated using the Weighted Histogram
Analysis Method (WHAM).42 The reported Gibbs energy was calculated from an average of
three independent simulations.
3.
Diﬀusion Calculations
Simulations used to calculate the CO diﬀusion coeﬃcient were performed with a Nos´e
thermostat with a response time of 0.1 ps. The systems were equilibrated for 1 ns before a 2
ns trajectory was collected. The reported diﬀusivity was calculated from an average of three
independent simulations.
The CO diﬀusion coeﬃcient (DPBC) under periodic boundary
conditions was calculated using the Einstein relation,
DPBC = 1
6t⟨|ri(t) −ri(0)|2⟩,
(2)
where r(t) is the position of the molecule at time, t.
4


## Page 5


TABLE I. Parameters for the Straub and Karplus13 molecular mechanical model for CO
parameter
value
qC (e)
-0.75
qO (e)
-0.85
qCOM (e)
1.6
ϵCC (kJ mol−1)
0.109647
ϵOO (kJ mol−1)
0.6658335
σCC (˚A)
3.83
σOO (˚A)
3.12
kC≡O (kJ mol−1 ˚A−2)
4666
re (˚A)
1.128
Yeh and Hummer found that the viscosity of a liquid simulated under periodic bound-
ary conditions depends on the size of the system, which spuriously lowers the calculated
diﬀusivities.43 A correction was applied to our calculated diﬀusivities using,
D = DPBC + 2.837297 kBT
6πηL.
(3)
Here, η is the solvent viscosity and L is the length of the simulation cell.
C.
AIMD Simulations
The AIMD simulations of aqueous CO were performed using CP2K version 2.6.44 The
MOLOPT-TZVP basis set was used for all atoms.45 The PBE exchange-correlation func-
tional was used32 with the Grimme D3 correction for dispersion.33 The simulation was initi-
ated from an equilibrium structure calculated using the MM model. A canonical-ensemble
simulation (NVT) was performed using Langevin dynamics with a bath temperature of
298.15 K and a friction coeﬃcient (γ) of 1 ps−1. A 1 fs time step was used. The O–H
bonds were constrained to 0.96 ˚A using the SHAKE algorithm.46 The cell contained one CO
molecule and 190 water molecules. The cell dimensions were 17.8 ˚A × 17.8 ˚A × 17.8 ˚A. A
15 ps equilibration simulation was performed prior to a 50 ps simulation. The 50 ps sim-
ulation was used to calculate the RDF. The CP2K input ﬁle is included in Supplementary
5


## Page 6


TABLE II. The calculated and experimental electric properties of CO. The MM model is the 3
point model of Straub and Karplus. The DFT results were calculated using the PBE XC functional
and the aug-cc-pVTZ basis set. The CCSD(T) calculations were performed with the aug-cc-pVQZ
basis set.
method
µ0
Θzz
(D)
(×10−40 C m2)
MM
0.27a
−8.17
DFT
0.19
−6.72
CCSD(T) 0.12
−6.58
exptl.
0.12
−6.47 ± 0.13
a The negative pole of the dipole of the MM model is on the O end of the CO, opposite to the QM models
and experimental data.
Information.
III.
RESULTS AND DISCUSSION
A.
Electric Properties
The models predict signiﬁcantly diﬀerent values for the electric moments of CO (Table
II). The CCSD(T) results are in the closest agreement with experiment; the dipole moment
is equal to the experimental value to two decimal places (µ0 = 0.12 D) and the quadrupole
moment is predicted correctly within the uncertainty of the experimental value. The DFT
model overestimates both moments, predicting a dipole moment of 0.19 D (a 58% overes-
timate) and a quadrupole of −6.72 × 10−40 C m2 (a 3 % overestimate). This performance
is typical for the PBE functional.47 Both QM methods predict the correct direction of the
dipole vector, where the positive pole is on the O end of the molecule and the negative pole
is on the C end (i.e., −CO+).48
The electric moments of the MM model are in poorer agreement with experiment. The
magnitude of the dipole is signiﬁcantly overestimated (µ0 = 0.27 D) and its direction points
from the O atom to the C atom, (+CO−). The quadrupole moment of this model is −8.17×
10−40 C m2 , 26% larger than the experimental value.
The oﬀ-center charge of the MM model is located at the bond midpoint. Although this
simpliﬁes the implementation and parameterization, this does not reﬂect the true electronic
6


## Page 7


FIG. 1. The electrostatic potential surface of CO calculated using MP2/aug-cc-pVTZ. The blue
isosurface corresponds to a negative ESP that interacts favorably with positive charges (ESP(r) =
−0.006 a.u.).
The red isosurface corresponds to a positive ESP that interacts favorably with
negative charges (ESP(r) = +0.006 a.u.).
distribution in CO. The electrostatic potential is positive in the space near the nuclei and
negative in the space on opposite ends of the molecule. The negative ESP lobe adjacent
to the C atom is particularly large. This is consistent with the MO theory description of
CO, where the HOMO is a σ bond with a large lobe protruding from the C atom along the
bond axis.49 Based on this, a more realistic representation of the ESP would be achieved if
the oﬀ-center charge was negative and located in the space opposite to the C atom.12 This
type of oﬀ-center charge has been successfully used to describe the electrostatic interactions
of molecules with a σ-hole,27,50–52 although not all molecular simulation codes support this
type of site at present.
B.
Optimized Structures
The minimum energy structure of the H2O–CO interactions corresponds to the C atom
of the CO serving a hydrogen bond acceptor (Figure 2). The interaction energies calculated
using the three models are collected in Table
III. The CCSD(T)-F12 predicts a modest
interaction energy of −9.6 kJ mol−1.
The DFT-calculated interaction energy is slightly
weaker, with an interaction energy of −8.9 kJ mol−1. The interaction energy calculated
7


## Page 8


FIG. 2. Minimum energy structure of the CO–H2O complex. The most stable structure for the
CCSD(T) and DFT structures corresponds to the water molecule donating a hydrogen bond to the
C atom of the monoxide.
TABLE III. The calculated CO–H2O interaction energies using the MM model of Straub
and Karplus, the DFT model (PBE/aug-cc-pVTZ), and CCSD(T) (CCSD(T)-F12/aug-cc-
pVQZ//MP2/aug-cc-pVTZ).
method
∆E (kJ/mol)
MM
−5.1
DFT
−8.9
CCSD(T)-F12
−9.6
using the MM model is only −5.1 kJ mol−1, signiﬁcantly weaker than the CCSD(T)-F12
interaction energy. The reversed polarity of the dipole in the MM model causes this minimum
to be higher energy hydrogen bond to the O atom with an interaction energy of −10.9 kJ
mol−1.
C.
Potential Energy Surfaces
Two-dimensional potential energy surfaces were calculated for the interaction between
CO and H2O molecules. The CO and H2O molecules were ﬁxed at their experimental gas
phase structures. The coordinates were deﬁned in terms of the distance between the center
of the C–O bond and the O–C — O(H2) angle. In the ﬁrst surface, the vector bisecting the
H–O–H angle points towards the midpoint of CO, with the water O atom oriented towards
the CO (donor). In the second surface, one of the O–H bonds of the water molecule points
towards the center of the CO molecule (acceptor).
The calculated potential energy surfaces for both donor and acceptor surfaces using the
CCSD(T)-F12, DFT, and MM models are represented in Figs. 3 and 4. For consistency and
to reduce the surface to 2D, both the H2O and the CO molecules were maintained at their
8


## Page 9


C
O
H
O
H
θ
C
O
θ
H
O
H
donor
acceptor
r
r
rigid experimental gas phase geometry in all conﬁgurations. The DFT PES provides an
indication of the accuracy of the AIMD simulations because the same exchange-correlation
functional (PBE) is used to calculate the potential energy of the CO–water simulation cell
in the AIMD simulations and also use a triple-ζ basis set.
The qualitative features of the surfaces calculated with the three models are generally
consistent. For the calculated donor surface plots (Figure 3), the region of lowest energy
minimum corresponds to a dipole–quadrupole interaction between the H2O and the monox-
ide, where the interaction is strongest at the midpoint of the CO bond. The location of the
minimum is approximately θ = 100◦and r = 3.2 ˚A in both QM surfaces. The stability of
this mode of interaction is modest; on the CCSD(T)-F12 surface, the minimum is roughly
−6 kJ mol−1. This minimum is slightly higher in energy in the DFT and MM models, with
energies in the −4 – −5 kJ mol−1 range. The location of the MM minimum is somewhat
diﬀerent than the QM surfaces; it is centered at θ = 90 ◦and r = 3.4 ˚A.
There are two minima on the acceptor surfaces. The minimum at θ = 180 ◦corresponds
to the C atom of the monoxide molecule accepting a hydrogen bond from the water along the
C–O bond axis, while the minimum at θ = 0◦corresponds to the O atom of the monoxide
molecule accepting a hydrogen bond from the water along the C–O bond axis.
In the
CCSD(T)-F12 and DFT surfaces, the minimum around θ = 0 ◦is higher energy than the
θ = 180 ◦minimum; the potential energy of about Emin = −5 kJ mol−1.
The most signiﬁcant diﬀerence of the acceptor surface calculated using the MM model
in comparison to the CCSD(T)-F12 is that the minimum corresponding to donation to the
C atom is less stable (−5 kJ mol−1) and the minimum corresponding to donation to the O
atom is more stable (−10 kJ mol−1) surface. The reversal of the stability of these minima is
a consequence of the incorrect polarity of the dipole of the MM model, where the negative
end is on the O atom and the positive end is on the C atom.
9


## Page 10


-10
-5
0
5
10
r (Å)
r (Å)
r (Å)
θ (deg)
θ (deg)
θ (deg)
(a)
(b)
(c)
3
4
5
6
0
50
100
150
0
50
100
150
0
50
100
150
2
3
4
5
6
2
3
4
5
6
2
FIG. 3. Potential energy surfaces of the CO–H2O interaction where the bisector of the H–O–H
angle is directed towards the center of geometry of CO. The surfaces are calculated using (a)
CCSD(T)-F12/aug-cc-pVQZ, (b) PBE-D3/aug-cc-pVTZ, and (c) Straub and Karplus MM model.
10


## Page 11


-10
-5
0
5
10
r (Å)
r (Å)
r (Å)
θ (deg)
θ (deg)
θ (deg)
(a)
(b)
(c)
0
50
100
150
0
50
100
150
0
50
100
150
3
4
5
6
3
4
5
6
3
4
5
6
FIG. 4.
Potential energy surfaces of the CO–H2O interaction where one of the O–H bonds is
directed towards the center of geometry of CO. The surfaces are calculated using (a) CCSD(T)-
F12/aug-cc-pVQZ, (b) DFT (PBE-D3/aug-cc-pVTZ), and (c) Straub and Karplus MM model.
11


## Page 12


g(r)
0
0.5
1
1.5
2
0
2
4
6
8
0
0.5
1
1.5
2
0
2
4
6
8
0
0.5
1
1.5
2
0
2
4
6
8
0
0.5
1
1.5
2
0
2
4
6
8
C–OH2
C–HOH
O–HOH
O–OH2
r (Å)
r (Å)
r (Å)
r (Å)
AIMD
MM
(a)
(b)
(c)
(d)
g(r)
g(r)
g(r)
FIG. 5. Radial distribution functions of CO(aq) calculated from AIMD and MM trajectories. (a)
C–O(H2), (b) O–O(H2), (c) C–HOH, and (d) O–HOH.
D.
Radial Distribution Functions
To examine CO–H2O interactions in bulk water, radial distribution functions were calcu-
lated from the AIMD and MM trajectories of CO(aq). Figure 5 (a) shows the rdf between
the water O atom and the monoxide C atom and Figure 5 (c) shows the rdf between the
water O atom and the monoxide O atom. Figure 5 (b) and (d) shows the rdfs of C and
O ends with water hydrogen atoms, which can be used to infer the formation of CO–H2O
hydrogen bonds.
The most signiﬁcant diﬀerence between these two models is that the ﬁrst peak of the
C–O(H2) rdf occurs at a 0.1 ˚A larger distance than the AIMD value. This suggests that
the Lennard-Jones radius of the monoxide carbon atom in the MM model is too large. This
is consistent with the potential energy surfaces plotted in Figure 3, where the MM surface
12


## Page 13


TABLE IV. The Gibbs energy of hydration of the MM model for CO. All values are in kJ mol−1.
The experimental value is estimated from the solubility constant reported in Ref. 57. The standard
state used is 1 M gas →1 M solution.
component
∆G (kJ/mol)
electrostatic
−2.8
dispersion
−15.5
repulsive
29.1
total
10.7 ± 0.2
exptl.
9.3
is more strongly repulsive at C–O(H2) distances in the 3–4 ˚A range in comparison to the
CCSD(T)-F12 surface.
The position of the ﬁrst peak of the MM O–OH2 rdf agrees well with the AIMD result,
suggesting that the MM Lennard-Jones radius of O is reasonable. The ﬁrst coordination
sphere of the rdfs calculated from the AIMD simulations are more pronounced than in the
MM simulations, although this aspect of AIMD simulations of liquid water is not entirely
reliable due to a trend of over-structuring liquid water at STP.53–55
Both models have very modest shoulders on the left-side of the ﬁrst peak of the rdf
for the distance between the monoxide C-atom and the water hydrogen (Figure 5 (c)).
This indicates that neither model predicts that there are strong hydrogen bonds between
the monoxide carbon and water molecules in aqueous solutions. This is apparent in the
Wannier-localized orbitals,56 which shows carbon-centered lone pair to be too distant from
the water hydrogen atoms to serve as a strong hydrogen bond acceptor (Figure 6).
The ﬁrst peak of the MM RDF for the monoxide oxygen and water hydrogen distance
(Figure 5 (d)) has a shoulder on the left side between 1.9 and 2.1 ˚A that is consistent with a
water molecule donating a hydrogen bond to the monoxide oxygen. This shoulder is much
more pronounced in the rdf calculated from the MM simulation and is a minor feature in
the AIMD rdf. This is consistent with the QM potential energy surfaces, which show that
the MM model overestimates the strength of hydrogen bonds where the monoxide oxygen
is the acceptor.
13


## Page 14


FIG. 6. The Wannier-localized orbital of the AIMD simulation of CO(aq) corresponding to the
carbon-centered lone pair. The MO is rendered by the red and blue mesh surfaces. The surfaces
are plotted at an isocontour value of |ψ| = 0.016 a.u.
E.
Hydration Energy
To quantify how accurately this model predicts the CO–water interactions, the Gibbs
energy of hydration of CO was calculated using alchemical FEP (Table III E). This analysis
indicates that the hydration energy calculated using the MM model is in reasonably good
agreement with experiment (10.7 kJ mol−1 vs 9.3 kJ mol−1, respectively). The electrostatic
interactions between CO and water are weak, contributing only −2.8 kJ mol−1 to the hydra-
tion energy. The component from dispersion is considerably stronger, contributing −15.5
kJ mol−1. These interactions are counteracted by a large repulsive energy of 29.1 kJ mol−1.
These interactions are generally consistent with the hydration of a non-polar solute.26
F.
Diﬀusion Coeﬃcient
The calculated diﬀusivity of CO in liquid water at 30
◦C was calculated using the ﬁnite-
size corrected Einstein relation (Eqn 3. A diﬀusivity of D = 5.19 ± 0.82 × 10−5 cm2/s was
calculated. This is considerably larger than the experimental value of D = 2.32±0.07×10−5
cm2/s.58. The TIP3P water model predicts a viscosity that is signiﬁcantly lower than the
experimental value, so by the Stokes–Einstein equation, the diﬀusivity of the solutes is this
medium will be overestimated.59 A CO model developed for use with water models like
14


## Page 15


TIP4P-200560 or TIP4P-FB61 that have more accurate viscosities could provide improved
diﬀusivities.
IV.
CONCLUSIONS
AIMD simulations, CCSD(T)-F12 calculations, and MM MD simulations were used to
study the solvation of CO in liquid water. The AIMD simulations indicated that there are
no persistent water–CO hydrogen bonds, although the CCSD(T) potential energy surfaces
and AIMD rdfs indicated that CO forms its strongest interactions with water when the lone
pair on the C atom serves as a hydrogen bond acceptor. The weakness of these interactions
is consistent with the poor solubility of CO in liquid water.
These QM calculations were compared to the results from the MM model of Straub and
Karplus. This model overestimates the dipole and quadrupole moments and predicts the
opposite polarity of the dipole moment. This causes hydrogen bonds to the monoxide O
atom to be the preferred interaction, while the QM calculations indicate that hydrogen
bonds to the C atom are stronger. In comparison to the AIMD results, the atomic radius of
the MM monoxide C atom model appears to be slightly too large by roughly 0.05 ˚A. Despite
these limitations, the ∆G◦
hydr of this model is in very good agreement with the experimental
value (9 kJ mol−1 calc. vs 10 kJ mol−1 exptl.). The diﬀusivity the MM model is signiﬁcantly
higher than the experimental value (5.19 × 10−5 cm2/s calc. vs 2.32 × 10−5 cm2/s exptl.).
An improved MM model could likely be designed by repositioning the oﬀ-center charge
to be located in the place of the C-centered lone pair and changing the charges to reﬂect the
actual electric moments. The Lennard-Jones radius of the C atom should also be increased.
Improving the diﬀusivity would require developing a model that can be used with a water
model with an accurate viscosity.
SUPPLEMENTARY MATERIAL
See supplementary material for CP2K, CHARMM, and TURBOMOLE input ﬁles.
15


## Page 16


ACKNOWLEDGEMENTS
The authors thank NSERC of Canada for funding through the Discovery Grant program
(Application 418505-2012). EAW thanks the School of Graduate studies at Memorial Uni-
versity for a graduate fellowship. EAW also thanks ACENET for an Advanced Research
Computing Fellowship. Computational resources were provided by Compute Canada (RAPI:
djk-615-ab) through the Calcul Quebec and ACENET consortia.
REFERENCES
1C. C. Romao, W. A. Blattler, J. D. Seixas, and G. J. L. Bernardes, Chem. Soc. Rev. 41,
3571 (2012).
2Occupational Safety and Health Administration, “Occupational safety and health stan-
dards, table z-1 limits for air contaminants.” (Accessed October 16, 2015),
http://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1416170084502&uri=
CELEX:32014R0269.
3L. D. Prockop and R. I. Chichkova, J. Neurol. Sci. 262, 122 (2007).
4A. K. Mustafa, M. M. Gadalla, and S. H. Snyder, Sci. Signal. 2, re2 (2009).
5R. Motterlini and L. E. Otterbein, Nat. Rev. Drug Discov. 9, 728 (2010).
6R.
Motterlini,
Biochem.
Soc.
Trans.
35,
1142
(2007),
http://www.biochemsoctrans.org/content/35/5/1142.full.pdf.
7S. Romanski, B. Kraus, U. Schatzschneider, J.-M. Neud¨orﬂ, S. Amslinger,
and H.-G.
Schmalz, Angew. Chem. Int. Ed. 50, 2392 (2011).
8U. Schatzschneider, Br. J. Pharmacol. 172, 1638 (2015).
9P. V. Simpson and U. Schatzschneider, “Small signaling molecules and co-releasing
molecules (corms) for the modulation of the cellular redox metabolism,” in Redox-Active
Therapeutics, edited by I. Batini´c-Haberle, J. S. Rebou¸cas, and I. Spasojevi´c (Springer
International Publishing, Cham, 2016) pp. 311–334.
10J. Muenter, J. Mol. Spectrosc. 55, 490 (1975).
11N. Chetty and V. W. Couling, J. Chem. Phys. 134, 164307 (2011), 10.1063/1.3585605.
12H. Kim, V. D. Doan, W. J. Cho, R. Valero, Z. A. Tehrani, J. M. L. Madridejos, and K. S.
Kim, Scientiﬁc Reports , 16307 (2015), 10.1038/srep16307.
16


## Page 17


13J. E. Straub and M. Karplus, Chem. Phys. 158, 221 (1991).
14C. Zheng, V. Makarov,
and P. G. Wolynes, J. Am. Chem. Soc. 118, 2818 (1996),
http://dx.doi.org/10.1021/ja9523092.
15J. Meller and R. Elber, Biophys. J. 74, 789 (1998).
16D. Vitkup, G. A. Petsko, and M. Karplus, Nat. Struct. Mol. Biol 4, 202 (1997).
17J.-C. Lambry, M. H. Vos,
and J.-L. Martin, J. Phys. Chem. A 103, 10132 (1999),
http://dx.doi.org/10.1021/jp992587d.
18D. E. Sagnella, J. E. Straub, T. A. Jackson, M. Lim,
and P. A. Anﬁnrud, Proc. Natl.
Acad. Sci. U.S.A. 96, 14324 (1999), http://www.pnas.org/content/96/25/14324.full.pdf.
19C. Bossa, M. Anselmi, D. Roccatano, A. Amadei, B. Vallone, M. Brunori, and A. D. Nola,
Biophys. J. 86, 3855 (2004).
20M. DAbramo, A. Di Nola,
and A. Amadei, J. Phys. Chem. B 113, 16346 (2009),
http://dx.doi.org/10.1021/jp903165p.
21L. U. L. Brinkmann and J. S. Hub, Proc. Natl. Acad. Sci. U.S.A.
(2016),
10.1073/pnas.1603539113.
22T. W. Whitﬁeld,
S. Varma,
E. Harder,
G. Lamoureux,
S. B. Rempe,
and
B.
Roux,
Journal
of
Chemical
Theory
and
Computation
3,
2068
(2007),
http://dx.doi.org/10.1021/ct700172b.
23C. N. Rowley and B. Roux, J. Chem. Theory Comput. 8, 3526 (2012).
24S.
Riahi,
B.
Roux,
and
C.
N.
Rowley,
Can
J.
Chem.
91,
552
(2013),
http://www.nrcresearchpress.com/doi/pdf/10.1139/cjc-2012-0515.
25S.
Riahi
and
C.
N.
Rowley,
J.
Phys.
Chem.
B
117,
5222
(2013),
http://pubs.acs.org/doi/pdf/10.1021/jp401847s.
26S. Riahi and C. N. Rowley, J. Phys. Chem. B 118, 1373 (2014).
27A. N. S. Adluri, J. N. Murphy, T. Tozer, and C. N. Rowley, J. Phys. Chem. B 119, 13422
(2015).
28“TURBOMOLE V7.0 2015, a development of University of Karlsruhe and Forschungszen-
trum Karlsruhe GmbH, 1989-2007, TURBOMOLE GmbH, since 2007; available from
http://www.turbomole.com.”.
29C. H¨attig,
D. P. Tew,
and A. K¨ohn, J. Chem. Phys. 132, 231102 (2010),
10.1063/1.3442368.
30T. H. Dunning, Jr., J. Chem. Phys. 90, 1007 (1989).
17


## Page 18


31R. A. Kendall, T. H. Dunning, and R. J. Harrison, J. Chem. Phys. 96, 6796 (1992).
32J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).
33S. Grimme, J. Antony, S. Ehrlich,
and H. Krieg, J. Chem. Phys. 132, 154104 (2010),
10.1063/1.3382344.
34B. R. Brooks, I. C. L. Brooks, J. A. D. Mackerell, L. Nilsson, R. J. Petrella, B. Roux,
Y. Won, G. Archontis, C. Bartels, S. Boresch,
and et al., J. Comput. Chem. 30, 1545
(2009).
35W. L. Jorgensen, J. Chandrasekhar, J. D. Madura, R. W. Impey,
and M. L. Klein, J.
Chem. Phys. 79, 926 (1983).
36J. A. D. MacKerell, D. Bashford, M. Bellott, J. R. L. Dunbrack, J. D. Evanseck, M. J.
Field, S. Fischer, J. Gao, H. Guo, S. Ha, D. Joseph-McCarthy, L. Kuchnir, K. Kuczera,
F. T. K. Lau, C. Mattos, S. Michnick, T. Ngo, D. T. Nguyen, B. Prodhom, W. E. Reiher,
B. Roux, M. Schlenkrich, J. C. Smith, R. Stote, J. Straub, M. Watanabe, J. Wi´Orkiewicz-
Kuczera, D. Yin, and M. Karplus, J. Phys. Chem. B 102, 3586 (1998).
37T. Darden, D. York, and L. Pedersen, J. Chem. Phys. 98, 10089 (1993).
38H. C. Andersen, J. Chem. Phys. 72, 2384 (1980).
39W. G. Hoover, Phys. Rev. A 34, 2499 (1986).
40Y. Deng and B. Roux, J. Phys. Chem. B 108, 16567 (2004).
41Y. Deng and B. Roux, J. Phys. Chem. B 113, 2234 (2009).
42S. Kumar, J. M. Rosenberg, D. Bouzida, R. H. Swendsen, and P. A. Kollman, J. Comput.
Chem. 13, 1011 (1992).
43I.-C.
Yeh
and
G.
Hummer,
J.
Phys.
Chem.
B
108,
15873
(2004),
http://dx.doi.org/10.1021/jp0477147.
44J. VandeVondele, M. Krack, F. Mohamed, M. Parrinello, T. Chassaing, and J. Hutter,
Comp. Phys. Comm. 167, 103 (2005).
45J. VandeVondele and J. Hutter, J. Chem. Phys. 127, 114105 (2007), 10.1063/1.2770708.
46J.-P. Ryckaert, G. Ciccotti, and H. J. C. Berendsen, J. Comput. Phys. 23, 327 (1977).
47A.
L.
Hickey
and
C.
N.
Rowley,
J.
Phys.
Chem.
A
118,
3678
(2014),
http://dx.doi.org/10.1021/jp502475e.
48W. Meerts, F. D. Leeuw, and A. Dymanus, Chem. Phys. 22, 319 (1977).
49M. Bochmann, Organometallics 1 (Oxford University Press, 1994).
50M. A. A. Ibrahim, J. Comput. Chem. 32, 2564 (2011).
18


## Page 19


51M.
Kol´aˇr
and
P.
Hobza,
J.
Chem.
Theory
Comput.
8,
1325
(2012),
http://dx.doi.org/10.1021/ct2008389.
52W. L. Jorgensen and P. Schyman, J. Chem. Theory Comput. 8, 3895 (2012),
http://dx.doi.org/10.1021/ct300180w.
53T. D. K¨uhne, M. Krack, and M. Parrinello, J. Chem. Theory Comput. 5, 235 (2009).
54I.-C. Lin, A. P. Seitsonen, I. Tavernelli, and U. Rothlisberger, J. Chem. Theory Comput.
8, 3902 (2012).
55T. A. Pham, T. Ogitsu, E. Y. Lau, and E. Schwegler, J. Chem. Phys. 145, 154501 (2016),
http://dx.doi.org/10.1063/1.4964865.
56A. Ambrosetti and P. L. Silvestrelli, “Introduction to maximally localized wannier func-
tions,” in Reviews in Computational Chemistry (John Wiley & Sons, Inc, 2016) pp. 327–
368.
57B. B. Breman, A. A. C. M. Beenackers, E. W. J. Rietjens, and R. J. H. Stege, J. Chem.
Eng. Data 39, 647 (1994), http://dx.doi.org/10.1021/je00016a004.
58D. Wise and G. Houghton, Chem. Eng. Sci. 23, 1211 (1968).
59M.
A.
Gonz´alez
and
J.
L.
F.
Abascal,
J.
Chem.
Phys.
132,
096101
(2010),
http://dx.doi.org/10.1063/1.3330544.
60S. Tazi, A. Boan, M. Salanne, V. Marry, P. Turq, and B. Rotenberg, J. Phys. Condens.
Matter 24, 284117 (2012).
61L.-P. Wang, T. J. Martinez,
and V. S. Pande, J. Phys. Chem. Lett. 5, 1885 (2014),
http://dx.doi.org/10.1021/jz500737m.
19

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
RSCF-NODE
node_id: 1610_09046v1_the_hydration_structure_of_carbon_monoxide_by_ab_initio_methods
node_type: note
path: 11_KNOWLEDGE/_arxiv_md/2016/1610_09046V1_THE_HYDRATION_STRUCTURE_OF_CARBON_MONOXIDE_BY_AB_INITIO_METHODS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
